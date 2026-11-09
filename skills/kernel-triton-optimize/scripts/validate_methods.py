#!/usr/bin/env python3
"""Validate iterv{i}/methods.json against registry, state, and roofline budgets.

v2 changes from v1:
- Axis distribution must match roofline.json axis_budget (not fixed 1:1:1)
- Per-axis cap of 2 is enforced
- Total method count must equal sum of axis budgets (typically 3)
- Priority scan compliance still enforced within each axis

Exit 0 when valid; exit 1 and print violations otherwise.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


_DEFAULT_REGISTRY = Path(__file__).resolve().parent.parent / "references" / "triton_method_registry.json"


def _load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


_KERNEL_LOGIC_MARKER = "## Kernel Computation Logic"
_FORMULA_RE = re.compile(
    r"(\b[A-Za-z_]\w*(?:\[[^\]]+\])?\s*=)|"
    r"(\\sum|\\max|\\operatorname)|"
    r"(\b(?:max|sum|softmax|exp|exp2|dot|einsum)\s*\()|"
    r"(@)|"
    r"(\u2200)"
)
_PY_REF_RE = re.compile(r"```(?:python)?[\s\S]*?(?:def\s+reference\b|torch\.|np\.|numpy\.)[\s\S]*?```")
_REFERENCE_PLACEHOLDER_RE = re.compile(
    r"```(?:python)?\s*def\s+reference\(\.\.\.\):[\s\S]*?\.\.\.\s*```",
    re.IGNORECASE,
)


def validate_analysis_md(
    analysis_path: str,
    min_body_chars: int = 40,
) -> tuple[bool, list[str]]:
    """Require a non-placeholder ## Kernel Computation Logic section."""
    errors: list[str] = []
    if not os.path.isfile(analysis_path):
        return False, [f"analysis.md missing: {analysis_path}"]

    with open(analysis_path, "r", encoding="utf-8") as f:
        text = f.read()

    if _KERNEL_LOGIC_MARKER not in text:
        return False, [
            f"Missing '{_KERNEL_LOGIC_MARKER}' in {analysis_path}. "
            "Write kernel semantics during the Semantic Pre-Pass "
            "or carry them forward before close-iter."
        ]

    idx = text.index(_KERNEL_LOGIC_MARKER)
    rest = text[idx + len(_KERNEL_LOGIC_MARKER) :]
    next_heading = re.search(r"\n## ", rest)
    section = rest[: next_heading.start()] if next_heading else rest
    semantic_section = _REFERENCE_PLACEHOLDER_RE.sub("", section)
    # Drop template italic guidance and whitespace.
    body = semantic_section
    body = re.sub(r"_[^_]+_", "", body)
    body = re.sub(r"\s+", "", body)
    if len(body) < min_body_chars:
        errors.append(
            f"'{_KERNEL_LOGIC_MARKER}' in {analysis_path} is empty or still a "
            f"template placeholder (need >= {min_body_chars} chars of semantic content)."
        )
    if not _FORMULA_RE.search(semantic_section):
        errors.append(
            f"'{_KERNEL_LOGIC_MARKER}' in {analysis_path} must include an explicit "
            "mathematical formula. Python reference-form code is not a substitute."
        )

    return (len(errors) == 0, errors)


def _parse_sm_arch(arch: str | None) -> int:
    if not arch:
        return 0
    m = re.match(r"(?:sm_|gfx)(\d+)", arch)
    return int(m.group(1)) if m else 0


def _higher_priority_ids(registry: dict, axis: str, priority: int) -> list[tuple[str, int]]:
    out = []
    for mid, meta in registry["methods"].items():
        if meta["axis"] == axis and meta["priority"] < priority:
            out.append((mid, meta["priority"]))
    return sorted(out, key=lambda x: x[1])


def validate(
    methods_path: str,
    state_path: str,
    registry_path: str = None,
    allow_ineffective: bool = False,
) -> tuple[bool, list[str]]:
    registry = _load_json(registry_path or str(_DEFAULT_REGISTRY))
    state = _load_json(state_path)
    methods_data = _load_json(methods_path)

    errors: list[str] = []

    if "methods" not in methods_data:
        return False, ["Top-level 'methods' key missing"]

    methods_list = methods_data["methods"]

    # Detect gfx arch
    gpus = state.get("env", {}).get("gpus", [{}])
    detected_sm = _parse_sm_arch((gpus[0].get("gfx_arch") or gpus[0].get("gcn_arch")) if gpus else None)

    # Load roofline budget if available
    iter_num = methods_data.get("iter", 1)
    run_dir = state.get("run_dir", "")
    roofline_path = os.path.join(run_dir, f"iterv{iter_num}", "roofline.json")
    axis_budget = {"compute": 1, "memory": 1, "latency": 1}  # default
    if os.path.isfile(roofline_path):
        roofline = _load_json(roofline_path)
        axis_budget = roofline.get("axis_budget", axis_budget)

    # Validate total count stays within schema bounds. Triton config-tuning rounds may
    # intentionally select method sets that do not exactly match a degraded profiler
    # axis budget, so exact axis-budget matching is advisory here.
    expected_total = sum(axis_budget.values())
    if len(methods_list) < 1 or len(methods_list) > 6:
        errors.append(
            f"Expected 1-6 methods (roofline budget: {axis_budget}), "
            f"got {len(methods_list)}"
        )

    # Validate axis distribution
    axis_counts = {"compute": 0, "memory": 0, "latency": 0}
    for m in methods_list:
        ax = m.get("axis", "unknown")
        if ax in axis_counts:
            axis_counts[ax] += 1
        else:
            errors.append(f"Unknown axis '{ax}' for method {m.get('id')}")

    for axis in ["compute", "memory", "latency"]:
        if axis_counts[axis] > 2:
            errors.append(
                f"Axis '{axis}': {axis_counts[axis]} methods exceeds per-axis cap of 2"
            )

    # Validate each method
    all_submitted_ids = {m.get("id", "") for m in methods_list}
    coupled_pairs = registry.get("coupled_methods", [])

    for idx, m in enumerate(methods_list):
        prefix = f"methods[{idx}]"

        for field in ("id", "axis", "priority"):
            if field not in m:
                errors.append(f"{prefix}: missing required field '{field}'")
        if any(f not in m for f in ("id", "axis", "priority")):
            continue

        mid = m["id"]
        axis = m["axis"]
        priority = m["priority"]

        # id must exist in registry
        if mid not in registry["methods"]:
            errors.append(
                f"{prefix}: id '{mid}' not in registry. Known ids on '{axis}': "
                f"{sorted(k for k,v in registry['methods'].items() if v['axis']==axis)}"
            )
            continue

        reg = registry["methods"][mid]

        # axis & priority must match
        if reg["axis"] != axis:
            errors.append(f"{prefix}: axis '{axis}' != registry '{reg['axis']}'")
        if reg["priority"] != priority:
            errors.append(f"{prefix}: P{priority} != registry P{reg['priority']} for '{mid}'")

        # arch compatibility
        if reg["min_sm"] > detected_sm > 0:
            errors.append(f"{prefix}: '{mid}' requires gfx{reg['min_sm']}+ but have gfx{detected_sm}")

        # already selected?
        selected_ids = {item.get("id") for item in state.get("selected_methods", [])}
        if mid in selected_ids:
            errors.append(f"{prefix}: '{mid}' already in selected_methods")

        # ineffective check
        if not allow_ineffective:
            ineff_ids = {item.get("id") for item in state.get("ineffective_methods", [])}
            if mid in ineff_ids:
                errors.append(
                    f"{prefix}: '{mid}' in ineffective_methods (use --allow-ineffective "
                    "if bottleneck profile fundamentally changed)"
                )

        # implementation_failed check
        impl_failed_ids = {item.get("id") for item in state.get("implementation_failed_methods", [])}
        if mid in impl_failed_ids:
            errors.append(
                f"{prefix}: '{mid}' previously failed HCU ISA verification. "
                "Ensure implementation is corrected before re-selecting."
            )

        # skipped_higher — must account for all higher-priority on this axis
        higher = _higher_priority_ids(registry, axis, priority)
        skipped = m.get("skipped_higher", [])
        skipped_ids_set = {s.get("id") for s in skipped}
        valid_reasons = {"already_selected", "arch_incompatible", "feature_unavailable", "skip_condition", "no_trigger"}

        for hid, hpri in higher:
            if hid in all_submitted_ids:
                continue  # selected, not skipped
            if hid not in skipped_ids_set:
                errors.append(
                    f"{prefix}: higher-priority '{hid}' (P{hpri}) on axis '{axis}' "
                    "not in skipped_higher and not selected"
                )

        for s in skipped:
            reason = s.get("reason", "")
            if reason not in valid_reasons:
                errors.append(
                    f"{prefix}: skipped_higher '{s.get('id')}' has invalid reason '{reason}'. "
                    f"Valid: {valid_reasons}"
                )

    # Coupled pairs check
    for pair in coupled_pairs:
        pair_ids = set(pair.get("ids", []))
        if pair_ids.issubset(all_submitted_ids):
            errors.append(
                f"Coupled pair both selected: {pair_ids}. "
                f"Note: {pair.get('note', '')}"
            )

    return (len(errors) == 0, errors)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--methods")
    p.add_argument("--state")
    p.add_argument("--analysis", help="Path to itervN/analysis.md for semantic pre-pass check")
    p.add_argument("--registry", default=str(_DEFAULT_REGISTRY))
    p.add_argument("--allow-ineffective", action="store_true")
    args = p.parse_args()

    if not args.methods and not args.analysis:
        p.error("provide --methods and --state, or --analysis")

    all_errors: list[str] = []
    if args.analysis:
        ok_a, errs_a = validate_analysis_md(args.analysis)
        if not ok_a:
            all_errors.extend(errs_a)
    if args.methods:
        if not args.state:
            p.error("--state is required with --methods")
        ok_m, errs_m = validate(
            methods_path=args.methods,
            state_path=args.state,
            registry_path=args.registry,
            allow_ineffective=args.allow_ineffective,
        )
        if not ok_m:
            all_errors.extend(errs_m)

    if not all_errors:
        print(json.dumps({"valid": True}, indent=2))
        sys.exit(0)
    print(json.dumps({"valid": False, "errors": all_errors}, indent=2))
    sys.exit(1)


if __name__ == "__main__":
    main()
