#!/usr/bin/env python3
"""Append a manual optimization attempt event to iterv*/attempt_timeline.json."""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
from pathlib import Path


def _read_json(path: str | Path, default):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return default


def _write_json(path: str | Path, payload) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _optional_float(value: str | None):
    if value in (None, ""):
        return None
    return float(value)


def _change_vs_previous(previous_ms, ms) -> dict:
    if previous_ms is None or ms is None or previous_ms <= 0 or ms <= 0:
        return {
            "speedup_vs_previous_best": None,
            "change_vs_previous_best_pct": None,
            "delta_vs_previous_best_ms": None,
        }
    return {
        "speedup_vs_previous_best": previous_ms / ms,
        "change_vs_previous_best_pct": ((previous_ms - ms) / previous_ms) * 100.0,
        "delta_vs_previous_best_ms": previous_ms - ms,
    }


def _iter_dir(args: argparse.Namespace) -> Path:
    if args.iter_dir:
        return Path(args.iter_dir).resolve()
    if not args.run_dir or args.iter is None:
        raise SystemExit("pass either --iter-dir or both --run-dir and --iter")
    return Path(args.run_dir).resolve() / f"iterv{args.iter}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Record a manual semantic/config/source optimization attempt."
    )
    parser.add_argument("--run-dir", default="")
    parser.add_argument("--iter-dir", default="")
    parser.add_argument("--iter", type=int, default=None)
    parser.add_argument("--kind", required=True,
                        choices=["semantic_rewrite", "config_tune", "manual_attempt", "analysis_only"])
    parser.add_argument("--candidate", required=True,
                        help="Short candidate/rewrite name shown in summary.md")
    parser.add_argument("--status", required=True, choices=["success", "failure", "pending"])
    parser.add_argument("--outcome", required=True,
                        help="Short outcome such as promoted_before_config_tune, rejected_not_equivalent, no_timing")
    parser.add_argument("--ms", default="", help="Candidate/champion latency in ms, if measured")
    parser.add_argument("--previous-best-ms", default="",
                        help="Previous best latency in ms. Defaults to state.best_metric_ms when --run-dir is given.")
    parser.add_argument("--kernel", default="", help="Candidate kernel path, if any")
    parser.add_argument("--bench-json", default="", help="Benchmark evidence path, if any")
    parser.add_argument("--analysis", default="", help="analysis.md path, if any")
    parser.add_argument("--proof", default="",
                        help="Short correctness/equivalence proof note")
    parser.add_argument("--metadata-json", default="",
                        help="Extra JSON object to merge into the event")
    args = parser.parse_args()

    iter_dir = _iter_dir(args)
    run_dir = Path(args.run_dir).resolve() if args.run_dir else iter_dir.parent
    state = _read_json(run_dir / "state.json", {})
    previous_ms = _optional_float(args.previous_best_ms)
    if previous_ms is None:
        previous_ms = state.get("best_metric_ms")
    ms = _optional_float(args.ms)

    event = {
        "kind": args.kind,
        "iter": args.iter if args.iter is not None else int(iter_dir.name.replace("iterv", "", 1)),
        "candidate": args.candidate,
        "status": args.status,
        "outcome": args.outcome,
        "previous_best_ms": previous_ms,
        "ms": ms,
    }
    event.update(_change_vs_previous(previous_ms, ms))
    for key, value in (
        ("kernel", args.kernel),
        ("bench_json", args.bench_json),
        ("analysis", args.analysis),
        ("proof", args.proof),
    ):
        if value:
            event[key] = os.path.abspath(value)
    if args.metadata_json:
        extra = json.loads(args.metadata_json)
        if not isinstance(extra, dict):
            raise SystemExit("--metadata-json must decode to a JSON object")
        event.update(extra)

    path = iter_dir / "attempt_timeline.json"
    events = _read_json(path, [])
    if isinstance(events, dict):
        events = [events]
    if not isinstance(events, list):
        events = []
    event.setdefault("timestamp", _dt.datetime.now().isoformat(timespec="seconds"))
    event.setdefault("sequence", len(events) + 1)
    events.append(event)
    _write_json(path, events)
    print(json.dumps({"attempt_timeline": str(path), "event": event}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
