#!/usr/bin/env python3
"""Parse common MMDetection/MMEngine text or JSON logs into stable-window statistics."""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
import tempfile
from pathlib import Path


ITER_RE = re.compile(
    r"(?:Epoch(?:\([^)]*\))?\s*\[\s*(?P<epoch>\d+)\s*\]\s*"
    r"\[\s*(?P<inner>\d+)(?:\s*/\s*(?P<total>\d+))?\s*\]"
    r"|(?:Iter|iter)(?:\([^)]*\))?\s*\[?\s*(?P<iter>\d+)(?:\s*/\s*\d+)?\s*\]?)"
)
PAIR_RE = re.compile(r"(?P<key>[A-Za-z][A-Za-z0-9_./-]*):\s*(?P<value>[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)")
INDEX_KEYS = {"sequence", "global_step", "iter", "step", "epoch", "inner_iter", "iters_per_epoch"}


def percentile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    pos = (len(ordered) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    return ordered[lo] if lo == hi else ordered[lo] * (hi - pos) + ordered[hi] * (pos - lo)


def parse_json_record(record: dict, sequence: int) -> dict:
    output = {"sequence": sequence}
    for key, value in record.items():
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            output[key] = float(value)
    for key in ("global_step", "step", "iter"):
        value = record.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value)):
            output["global_step"] = int(value)
            output["iter"] = int(value)
            break
    return output


def parse_text_line(line: str, sequence: int) -> dict | None:
    match = ITER_RE.search(line)
    pairs = {item.group("key"): float(item.group("value")) for item in PAIR_RE.finditer(line)}
    if not match and not pairs:
        return None
    record = {"sequence": sequence, **pairs}
    if match:
        if match.group("epoch"):
            epoch = int(match.group("epoch"))
            inner = int(match.group("inner"))
            record.update({"epoch": epoch, "inner_iter": inner})
            if match.group("total"):
                total = int(match.group("total"))
                global_step = (epoch - 1) * total + inner
                record.update({"iters_per_epoch": total, "global_step": global_step, "iter": global_step})
        else:
            explicit_iter = int(match.group("iter"))
            record.update({"global_step": explicit_iter, "iter": explicit_iter})
    return record


def load_records(path: Path) -> list[dict]:
    records = []
    for sequence, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("{"):
            try:
                payload = json.loads(stripped)
            except json.JSONDecodeError:
                payload = None
            if isinstance(payload, dict):
                records.append(parse_json_record(payload, sequence))
                continue
        record = parse_text_line(stripped, sequence)
        if record:
            records.append(record)
    return records


def record_step(record: dict) -> int:
    return int(record.get("global_step", record.get("iter", record["sequence"])))


def select_window(records: list[dict], start: int | None, end: int | None, tail: int | None) -> list[dict]:
    selected = records
    if start is not None:
        selected = [record for record in selected if record_step(record) >= start]
    if end is not None:
        selected = [record for record in selected if record_step(record) <= end]
    if tail:
        selected = selected[-tail:]
    return selected


def metric_summary(values: list[float]) -> dict:
    mean = statistics.fmean(values)
    std = statistics.stdev(values) if len(values) > 1 else 0.0
    return {
        "n": len(values),
        "mean": mean,
        "median": statistics.median(values),
        "p90": percentile(values, 0.90),
        "p95": percentile(values, 0.95),
        "min": min(values),
        "max": max(values),
        "std": std,
        "cv": std / abs(mean) if mean else None,
    }


def summarize(records: list[dict]) -> dict:
    metrics: dict[str, list[float]] = {}
    for record in records:
        for key, value in record.items():
            if key not in INDEX_KEYS and isinstance(value, (int, float)):
                metrics.setdefault(key, []).append(float(value))
    warnings = [
        f"metric {key} missing in {len(records) - len(values)} selected records"
        for key, values in metrics.items()
        if len(values) != len(records)
    ]
    if any("epoch" in record and "global_step" not in record for record in records):
        warnings.append("epoch record lacks /iters_per_epoch; sequence number used as its monotonic filter index")
    steps = [record_step(record) for record in records]
    if any(current <= previous for previous, current in zip(steps, steps[1:])):
        warnings.append("selected record indexes are not strictly increasing; inspect mixed/restarted logs")
    return {
        "records": len(records),
        "global_step_first": record_step(records[0]) if records else None,
        "global_step_last": record_step(records[-1]) if records else None,
        "iter_first": record_step(records[0]) if records else None,
        "iter_last": record_step(records[-1]) if records else None,
        "epoch_first": records[0].get("epoch") if records else None,
        "epoch_last": records[-1].get("epoch") if records else None,
        "inner_iter_first": records[0].get("inner_iter") if records else None,
        "inner_iter_last": records[-1].get("inner_iter") if records else None,
        "metrics": {key: metric_summary(values) for key, values in sorted(metrics.items())},
        "warnings": warnings,
    }


def self_test() -> None:
    sample = """Epoch [1][99/100] time: 2.0, data_time: 0.3, loss: 4.0
Epoch(train) [2][ 1/100] time: 1.5, data_time: 0.2, loss: 3.0
{"global_step": 102, "time": 1.0, "data_time": 0.1, "loss": 2.0}
"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "train.log"
        path.write_text(sample)
        result = summarize(load_records(path))
        assert result["records"] == 3
        assert result["metrics"]["time"]["median"] == 1.5
        assert result["metrics"]["loss"]["mean"] == 3.0
        assert result["global_step_first"] == 99
        assert result["global_step_last"] == 102
        selected = select_window(load_records(path), 100, None, None)
        assert [record_step(record) for record in selected] == [101, 102]
    print("self-test: PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("log", nargs="?", type=Path)
    parser.add_argument("--start", type=int, help="Minimum monotonic global step to include.")
    parser.add_argument("--end", type=int, help="Maximum monotonic global step to include.")
    parser.add_argument("--tail", type=int, help="Keep the last N records after global-step filtering.")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.log is None:
        parser.error("log is required unless --self-test is used")
    if args.tail is not None and args.tail < 0:
        parser.error("--tail must be non-negative")
    if args.start is not None and args.end is not None and args.end < args.start:
        parser.error("--end must be greater than or equal to --start")
    records = select_window(load_records(args.log), args.start, args.end, args.tail)
    result = summarize(records)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2, allow_nan=False)
    print()
    return 0 if records else 1


if __name__ == "__main__":
    raise SystemExit(main())
