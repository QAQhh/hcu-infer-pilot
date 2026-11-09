#!/usr/bin/env python3
"""Summarize benchmark samples and compare baseline/candidate series."""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
import sys
import tempfile
from pathlib import Path


def percentile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = (len(ordered) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def bootstrap_ci(values: list[float], statistic, *, samples: int = 5000, seed: int = 20260716) -> tuple[float, float]:
    rng = random.Random(seed)
    count = len(values)
    estimates = []
    for _ in range(samples):
        draw = [values[rng.randrange(count)] for _ in range(count)]
        estimates.append(float(statistic(draw)))
    return percentile(estimates, 0.025), percentile(estimates, 0.975)


def summarize(values: list[float]) -> dict:
    if not values:
        raise ValueError("series has no samples after warmup/filtering")
    if any(isinstance(value, bool) or not isinstance(value, (int, float)) for value in values):
        raise ValueError("series contains a boolean or non-numeric sample")
    if not all(math.isfinite(value) and value > 0 for value in values):
        raise ValueError("benchmark samples must be finite and strictly positive")
    mean = statistics.fmean(values)
    median = statistics.median(values)
    std = statistics.stdev(values) if len(values) > 1 else 0.0
    deviations = [abs(value - median) for value in values]
    ci_low, ci_high = bootstrap_ci(values, statistics.median)
    return {
        "n": len(values),
        "mean": mean,
        "median": median,
        "min": min(values),
        "max": max(values),
        "p90": percentile(values, 0.90),
        "p95": percentile(values, 0.95),
        "p99": percentile(values, 0.99),
        "std": std,
        "cv": std / abs(mean) if mean else None,
        "mad": statistics.median(deviations),
        "median_bootstrap_ci95": [ci_low, ci_high],
    }


def _numbers_from_json(payload, field: str | None) -> list[float]:
    if isinstance(payload, list):
        if not payload:
            return []
        if all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in payload):
            return [float(item) for item in payload]
        if field and all(isinstance(item, dict) and field in item for item in payload):
            if any(isinstance(item[field], bool) for item in payload):
                raise ValueError("JSON field contains a boolean sample")
            return [float(item[field]) for item in payload]
    if isinstance(payload, dict):
        if field and field in payload and isinstance(payload[field], list):
            if any(isinstance(item, bool) for item in payload[field]):
                raise ValueError("JSON field contains a boolean sample")
            return [float(item) for item in payload[field]]
        if "samples" in payload and isinstance(payload["samples"], list):
            if any(isinstance(item, bool) for item in payload["samples"]):
                raise ValueError("JSON samples contain a boolean value")
            return [float(item) for item in payload["samples"]]
    raise ValueError("JSON must be a numeric list, records containing --field, or {'samples': [...]}")


def load_values(path: Path, field: str | None) -> list[float]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return _numbers_from_json(json.loads(path.read_text()), field)
    if suffix in {".jsonl", ".ndjson"}:
        records = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        return _numbers_from_json(records, field)
    if suffix in {".csv", ".tsv"}:
        delimiter = "\t" if suffix == ".tsv" else ","
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle, delimiter=delimiter)
            if field is None:
                if not reader.fieldnames or len(reader.fieldnames) != 1:
                    raise ValueError("CSV/TSV with multiple columns requires --field")
                field = reader.fieldnames[0]
            return [float(row[field]) for row in reader if row.get(field, "").strip()]
    values = []
    for line in path.read_text().splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            values.append(float(stripped))
    return values


def compare(baseline: list[float], candidate: list[float], mode: str, paired: bool = False) -> dict:
    base_summary = summarize(baseline)
    cand_summary = summarize(candidate)
    base_median = float(base_summary["median"])
    cand_median = float(cand_summary["median"])
    speedup = base_median / cand_median if mode == "latency" else cand_median / base_median
    result = {"mode": mode, "speedup_from_medians": speedup, "baseline": base_summary, "candidate": cand_summary}
    if paired:
        if len(baseline) != len(candidate):
            raise ValueError("--paired requires baseline and candidate to have equal sample counts")
        pair_speedups = [(base / cand if mode == "latency" else cand / base) for base, cand in zip(baseline, candidate)]
        low, high = bootstrap_ci(pair_speedups, statistics.median)
        result["paired"] = {"median_speedup": statistics.median(pair_speedups), "speedup_bootstrap_ci95": [low, high], "n": len(pair_speedups)}
    else:
        rng = random.Random(20260716)
        speedups = []
        for _ in range(5000):
            base_draw = [baseline[rng.randrange(len(baseline))] for _ in baseline]
            cand_draw = [candidate[rng.randrange(len(candidate))] for _ in candidate]
            base_draw_median = statistics.median(base_draw)
            cand_draw_median = statistics.median(cand_draw)
            speedups.append(base_draw_median / cand_draw_median if mode == "latency" else cand_draw_median / base_draw_median)
        result["unpaired_speedup_bootstrap_ci95"] = [percentile(speedups, 0.025), percentile(speedups, 0.975)]
    return result


def self_test() -> None:
    with tempfile.TemporaryDirectory() as directory:
        base_path = Path(directory) / "base.json"
        cand_path = Path(directory) / "candidate.jsonl"
        base_path.write_text(json.dumps([10, 10.2, 9.8, 10.1, 9.9]))
        cand_path.write_text("\n".join(json.dumps({"latency_ms": value}) for value in [8, 8.2, 7.9, 8.1, 8]))
        baseline = load_values(base_path, None)
        candidate = load_values(cand_path, "latency_ms")
        result = compare(baseline, candidate, "latency")
        assert 1.2 < result["speedup_from_medians"] < 1.3
        assert result["unpaired_speedup_bootstrap_ci95"][0] > 1.0
        assert result["baseline"]["p99"] >= result["baseline"]["p95"]
        assert compare(baseline, candidate, "latency", paired=True)["paired"]["n"] == 5
        for invalid in ([1.0, 0.0], [1.0, float("nan")]):
            try:
                summarize(invalid)
            except ValueError:
                pass
            else:
                raise AssertionError("invalid samples must be rejected")
        try:
            _numbers_from_json([True, 1.0], None)
        except ValueError:
            pass
        else:
            raise AssertionError("boolean samples must be rejected")
    print("self-test: PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", nargs="?", type=Path)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--field", help="Field in JSON records or CSV/TSV")
    parser.add_argument("--warmup", type=int, default=0, help="Drop this many leading samples")
    parser.add_argument("--mode", choices=("latency", "throughput"), default="latency")
    parser.add_argument("--paired", action="store_true", help="Treat equal-position samples as genuinely matched pairs.")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.baseline is None:
        parser.error("baseline is required unless --self-test is used")
    if args.warmup < 0:
        parser.error("--warmup must be non-negative")
    baseline = load_values(args.baseline, args.field)[args.warmup :]
    result = {"series": summarize(baseline)} if args.candidate is None else compare(baseline, load_values(args.candidate, args.field)[args.warmup :], args.mode, paired=args.paired)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2, allow_nan=False)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
