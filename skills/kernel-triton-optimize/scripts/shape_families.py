#!/usr/bin/env python3
"""Create a small shape-family plan before per-family Triton optimization.

The optimizer loop is intentionally single-shape. When benchmark shapes are
many or have a large span, run separate normal optimization loops for at most
three families (small/middle/large), then merge the champions with runtime
config or variant dispatch.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


FAMILY_NAMES = ("small", "middle", "large")


def _read_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_json(path: str | Path, payload: Any) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _normalize_cases(data: Any) -> list[dict]:
    if isinstance(data, list):
        cases = data
    elif isinstance(data, dict):
        if isinstance(data.get("cases"), list):
            cases = data["cases"]
        elif isinstance(data.get("shapes"), list):
            cases = data["shapes"]
        else:
            cases = [data]
    else:
        raise TypeError("shape input must be a JSON object, list, or {'cases'|'shapes': list}")
    out = []
    for idx, case in enumerate(cases):
        if not isinstance(case, dict):
            raise TypeError(f"shape case {idx} is not an object")
        dims = dict(case.get("dims", case))
        name = str(case.get("name") or dims.get("name") or f"case_{idx + 1}")
        dims.pop("name", None)
        out.append({"name": name, "dims": dims})
    return out


def _numeric_dims(cases: list[dict]) -> dict[str, list[float]]:
    values: dict[str, list[float]] = {}
    for case in cases:
        for key, value in case["dims"].items():
            if isinstance(value, bool):
                continue
            if isinstance(value, (int, float)) and value > 0:
                values.setdefault(key, []).append(float(value))
    return {key: vals for key, vals in values.items() if vals}


def _choose_key_dim(cases: list[dict], requested: str) -> str | None:
    values = _numeric_dims(cases)
    if requested:
        return requested if requested in values else None
    for preferred in ("M", "rows", "N", "K", "seqlen", "seq_len", "tokens"):
        if preferred in values:
            return preferred
    best_key = None
    best_span = -1.0
    for key, vals in values.items():
        lo, hi = min(vals), max(vals)
        span = hi / lo if lo > 0 else hi
        if span > best_span:
            best_key = key
            best_span = span
    return best_key


def _span(values: list[float]) -> float:
    if not values:
        return 1.0
    lo, hi = min(values), max(values)
    return hi / lo if lo > 0 else math.inf


def _family_count(case_count: int, span: float, *, max_families: int) -> int:
    if case_count <= 1:
        return 1
    if max_families <= 1:
        return 1
    if case_count == 2:
        return 2
    if span >= 16.0 or case_count >= 6:
        return min(3, max_families)
    return min(2, max_families)


def _bucket_cases(cases: list[dict], key_dim: str, count: int) -> list[list[dict]]:
    ordered = sorted(cases, key=lambda c: float(c["dims"].get(key_dim, 0)))
    if count <= 1:
        return [ordered]
    buckets = []
    n = len(ordered)
    for idx in range(count):
        start = round(idx * n / count)
        end = round((idx + 1) * n / count)
        buckets.append(ordered[start:end])
    return [bucket for bucket in buckets if bucket]


def _representative(bucket: list[dict], key_dim: str) -> dict:
    ordered = sorted(bucket, key=lambda c: float(c["dims"].get(key_dim, 0)))
    return ordered[len(ordered) // 2]


def build_plan(
    cases: list[dict],
    *,
    key_dim: str = "",
    max_families: int = 3,
    min_cases: int = 2,
    span_threshold: float = 4.0,
    force: bool = False,
) -> dict:
    key = _choose_key_dim(cases, key_dim)
    values = [float(c["dims"][key]) for c in cases if key and key in c["dims"] and isinstance(c["dims"][key], (int, float))]
    span = _span(values)
    reasons = []
    if len(cases) >= min_cases:
        reasons.append("many_shapes")
    if span >= span_threshold:
        reasons.append("large_shape_span")
    required = bool(force or reasons)
    count = _family_count(len(cases), span, max_families=max(1, min(3, max_families))) if required and key else 1
    buckets = _bucket_cases(cases, key, count) if key else [cases]
    names = FAMILY_NAMES if len(buckets) == 3 else ("small", "large") if len(buckets) == 2 else ("single",)
    families = []
    for name, bucket in zip(names, buckets):
        rep = _representative(bucket, key) if key else bucket[0]
        vals = [float(c["dims"][key]) for c in bucket if key and key in c["dims"] and isinstance(c["dims"][key], (int, float))]
        guard = {"key_dim": key, "min": min(vals), "max": max(vals)} if vals else {}
        families.append({
            "name": name,
            "representative": rep,
            "dims": rep["dims"],
            "guard": guard,
            "cases": bucket,
            "run_dir": None,
        })
    return {
        "version": 1,
        "required": required,
        "reason": reasons or (["forced"] if force else []),
        "key_dim": key,
        "shape_count": len(cases),
        "span": span,
        "max_families": max_families,
        "workflow": "separate_runs_then_merge",
        "merge_policy": "runtime_config_or_variant_dispatch",
        "families": families,
        "final_required_artifacts": [
            "dispatch_manifest.json",
            "final_kernel.py",
            "one final_bench per family",
        ] if required else [],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shapes", required=True, help="Shape JSON: dict, list, or {'cases'|'shapes': list}.")
    parser.add_argument("--out", required=True, help="Output shape_family_plan.json path.")
    parser.add_argument("--key-dim", default="", help="Dimension used for bucketing, e.g. M or rows.")
    parser.add_argument("--max-families", type=int, default=3, choices=[1, 2, 3])
    parser.add_argument("--min-cases", type=int, default=2)
    parser.add_argument("--span-threshold", type=float, default=4.0)
    parser.add_argument("--force", action="store_true", help="Create families even if automatic triggers do not fire.")
    args = parser.parse_args()
    cases = _normalize_cases(_read_json(args.shapes))
    plan = build_plan(
        cases,
        key_dim=args.key_dim,
        max_families=args.max_families,
        min_cases=args.min_cases,
        span_threshold=args.span_threshold,
        force=args.force,
    )
    _write_json(args.out, plan)
    print(json.dumps({
        "out": args.out,
        "required": plan["required"],
        "reason": plan["reason"],
        "key_dim": plan["key_dim"],
        "families": [f["name"] for f in plan["families"]],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
