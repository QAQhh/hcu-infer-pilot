#!/usr/bin/env python3
"""Classify failed branch results and generate safe repair candidates.

This is a bounded automatic repair layer.  It does not guess arbitrary kernel
fixes; it classifies common failures and creates retry branches from the latest
known-good kernel when all generated candidates fail.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

KERNEL_EXTS = (".hip", ".cu", ".cpp", ".cc", ".cxx", ".py")


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _find_kernel(directory: Path) -> Path | None:
    for ext in KERNEL_EXTS:
        path = directory / f"kernel{ext}"
        if path.is_file():
            return path
    return None


def _read_failure_text(branch_dir: Path, bench_json: Path | None = None) -> str:
    parts: list[str] = []
    if bench_json and bench_json.is_file():
        try:
            parts.append(json.dumps(_read_json(bench_json), ensure_ascii=False))
        except Exception:
            pass
    for name in ("bench.stderr.txt", "compile.stderr.txt", "stderr.txt"):
        path = branch_dir / name
        if path.is_file():
            parts.append(path.read_text(encoding="utf-8", errors="ignore")[-6000:])
    return "\n".join(parts)


def _classify(text: str) -> list[str]:
    low = text.lower()
    classes: list[str] = []
    if any(token in low for token in ("compilation failed", "error:", "undefined reference", "no such file", "cannot find")):
        classes.append("compile_error")
    if any(token in low for token in ("cannot parse parameter", "cannot find `extern", "missing dimension")):
        classes.append("contract_error")
    if any(token in low for token in ("fail max=", '"passed": false', '"correct": false', "validation_failed")):
        classes.append("correctness_error")
    if any(token in low for token in ("out of memory", "memory access fault", "illegal memory", "segmentation fault", "hiperror")):
        classes.append("runtime_error")
    if any(token in low for token in ("index", "indices", "out of bounds", "bounds", "oob")) and any(token in low for token in ("fail", "incorrect", "validation", "mismatch")):
        classes.append("possible_index_mapping_error")
    if any(token in low for token in ("reduction", "sum", "max", "softmax", "layernorm", "nan", "inf")) and any(token in low for token in ("fail", "incorrect", "validation", "mismatch")):
        classes.append("possible_reduction_semantic_error")
    if any(token in low for token in ("atomic", "duplicate", "nondetermin", "race")) and any(token in low for token in ("fail", "incorrect", "validation", "mismatch")):
        classes.append("possible_atomic_semantic_error")
    if any(token in low for token in ("mask", "causal", "padding", "ragged", "jagged", "offset", "length")) and any(token in low for token in ("fail", "incorrect", "validation", "mismatch")):
        classes.append("possible_mask_or_ragged_semantic_error")
    if not classes:
        classes.append("unknown_failure")
    return classes


def _best_source(state: dict[str, Any]) -> Path:
    for key in ("best_file", "baseline_file"):
        value = str(state.get(key) or "")
        if value and Path(value).is_file():
            return Path(value)
    raise SystemExit("state has no usable best_file or baseline_file")


def _replace_block_dim(text: str, value: str) -> tuple[str, bool]:
    pattern = re.compile(r"\bdim3\s+block\s*\(([^)]*)\)\s*;")
    match = pattern.search(text)
    if not match:
        return text, False
    start, end = match.span(1)
    return text[:start] + value + text[end:], True


def _add_launch_bounds(text: str, bound: int) -> tuple[str, bool]:
    pattern = re.compile(r"__global__(\s+)(?!__launch_bounds__)(void\s+)")
    new_text, count = pattern.subn(rf"__global__\1__launch_bounds__({bound}) \2", text, count=1)
    return new_text, count > 0


def _remove_launch_bounds(text: str) -> tuple[str, bool]:
    new_text, count = re.subn(r"__launch_bounds__\s*\([^)]*\)\s+", "", text, count=1)
    return new_text, count > 0


def _add_restrict(text: str) -> tuple[str, bool]:
    pattern = re.compile(r"\b((?:const\s+)?(?:float|double|int|long|short|unsigned\s+int)\s*\*)\s*(?!__restrict__)([A-Za-z_]\w*)")

    def repl(match: re.Match[str]) -> str:
        local = match.group(0)
        if "restrict" in local:
            return local
        return f"{match.group(1)} __restrict__ {match.group(2)}"

    new_text, count = pattern.subn(repl, text)
    return new_text, count > 0


def _emit_variant(src: Path, dst: Path, transforms: list[str]) -> tuple[bool, list[str]]:
    text = src.read_text(encoding="utf-8", errors="ignore")
    applied: list[str] = []
    out = text
    for transform in transforms:
        changed = False
        if transform == "block_128":
            out, changed = _replace_block_dim(out, "128")
        elif transform == "block_256":
            out, changed = _replace_block_dim(out, "256")
        elif transform == "remove_launch_bounds":
            out, changed = _remove_launch_bounds(out)
        elif transform == "launch_bounds_256":
            out, changed = _add_launch_bounds(out, 256)
        elif transform == "restrict":
            out, changed = _add_restrict(out)
        if changed:
            applied.append(transform)
    if not applied or out == text:
        return False, []
    dst.write_text(
        "// Generated by repair_branches.py. Validate before promotion.\n"
        f"// Transforms: {', '.join(applied)}\n\n"
        + out,
        encoding="utf-8",
    )
    return True, applied


def _repair_plans(failures: list[dict[str, Any]]) -> list[list[str]]:
    classes = {cls for item in failures for cls in item.get("classes", [])}
    plans: list[list[str]] = []
    if "compile_error" in classes:
        plans.extend([["remove_launch_bounds"], ["block_128"]])
    if "correctness_error" in classes or "runtime_error" in classes:
        plans.extend([["block_128"], ["block_256"], ["remove_launch_bounds"], ["restrict"]])
    if not plans:
        plans.extend([["block_128"], ["restrict"], ["launch_bounds_256"]])
    unique: list[list[str]] = []
    seen = set()
    for plan in plans:
        key = tuple(plan)
        if key in seen:
            continue
        seen.add(key)
        unique.append(plan)
    return unique


def _failure_guidance(failures: list[dict[str, Any]]) -> list[dict[str, Any]]:
    classes = {cls for item in failures for cls in item.get("classes", [])}
    out: list[dict[str, Any]] = []
    if "contract_error" in classes:
        out.append(
            {
                "class": "contract_error",
                "action": "re-run preflight and inspect solve(...) signature, dims, and ref.py argument names",
                "automation": "blocked_until_contract_fixed",
            }
        )
    if "compile_error" in classes:
        out.append(
            {
                "class": "compile_error",
                "action": "try conservative launch-bound/block edits, then inspect compiler stderr for unsupported syntax or missing headers",
                "automation": "repair_branches emits remove_launch_bounds/block variants",
            }
        )
    if "correctness_error" in classes:
        out.append(
            {
                "class": "correctness_error",
                "action": "prefer current-best fallback; inspect generated indexing, bounds, dtype, and reduction initialization",
                "automation": "repair_branches emits safer block/restrict/no-launch-bound variants",
            }
        )
    if "runtime_error" in classes:
        out.append(
            {
                "class": "runtime_error",
                "action": "treat as possible OOB, alignment, or resource issue; reduce block size and remove launch bounds first",
                "automation": "repair_branches emits block_128/block_256/remove_launch_bounds variants",
            }
        )
    if "possible_index_mapping_error" in classes:
        out.append(
            {
                "class": "possible_index_mapping_error",
                "action": "inspect index dtype, bounds, negative-index policy, flattening order, and stride/layout mapping before retrying generated branches",
                "automation": "semantic repair is agent-required; do not accept mechanical repair without index parity tests",
            }
        )
    if "possible_reduction_semantic_error" in classes:
        out.append(
            {
                "class": "possible_reduction_semantic_error",
                "action": "inspect reduction identity, row/segment bounds, numerical stability, epsilon, and accumulation dtype",
                "automation": "semantic repair is agent-required; add boundary and all-equal/empty reduction tests",
            }
        )
    if "possible_atomic_semantic_error" in classes:
        out.append(
            {
                "class": "possible_atomic_semantic_error",
                "action": "inspect duplicate-index distribution, deterministic requirement, output initialization, and atomic equivalence",
                "automation": "semantic repair is agent-required; run high-duplicate and repeat-run tolerance tests",
            }
        )
    if "possible_mask_or_ragged_semantic_error" in classes:
        out.append(
            {
                "class": "possible_mask_or_ragged_semantic_error",
                "action": "inspect mask direction, padding value, empty rows, offsets monotonicity, max length, and invalid-token zeroing",
                "automation": "semantic repair is agent-required; regenerate contract with mask/ragged capture before kernel changes",
            }
        )
    if "unknown_failure" in classes or not out:
        out.append(
            {
                "class": "unknown_failure",
                "action": "preserve logs, retry no-op fallback, then manually inspect branch stderr and bench.json",
                "automation": "repair_branches emits conservative fallback variants only",
            }
        )
    return out


def _semantic_repair_checklist(failures: list[dict[str, Any]]) -> list[str]:
    classes = {cls for item in failures for cls in item.get("classes", [])}
    checklist: list[str] = []
    if "possible_index_mapping_error" in classes:
        checklist.extend(
            [
                "index bounds include 0 and last valid id",
                "negative or padding index policy matches reference",
                "flattened index mapping preserves original stride/layout",
            ]
        )
    if "possible_reduction_semantic_error" in classes:
        checklist.extend(
            [
                "reduction identity matches reference for empty groups",
                "softmax/norm uses stable max/epsilon/accumulation dtype",
                "row or segment limits match captured shape exactly",
            ]
        )
    if "possible_atomic_semantic_error" in classes:
        checklist.extend(
            [
                "output initialization occurs exactly once before accumulation",
                "duplicate-index accumulation is additive and tolerance allows atomic ordering",
                "deterministic mode has fallback or non-atomic algorithm",
            ]
        )
    if "possible_mask_or_ragged_semantic_error" in classes:
        checklist.extend(
            [
                "causal mask direction and diagonal convention are captured",
                "offsets are monotonic and final offset equals nnz",
                "padding/invalid-token values are preserved",
            ]
        )
    return sorted(set(checklist))


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    state_path = Path(args.state).expanduser().resolve()
    state = _read_json(state_path)
    run_dir = Path(state["run_dir"])
    iter_dir = run_dir / f"iterv{int(args.iter)}"
    branch_results_path = iter_dir / "branch_results.json"
    branch_results = _read_json(branch_results_path) if branch_results_path.is_file() else {"branches": []}
    branches = branch_results.get("branches", []) if isinstance(branch_results.get("branches"), list) else []
    failures = []
    plan_records: list[dict[str, Any]] = []
    for item in branches:
        if item.get("passed"):
            continue
        try:
            idx = int(item.get("branch_index"))
        except (TypeError, ValueError):
            continue
        branch_dir = iter_dir / "branches" / f"b{idx}"
        text = _read_failure_text(branch_dir, branch_dir / "bench.json")
        failures.append(
            {
                "branch_index": idx,
                "kernel": item.get("kernel"),
                "classes": _classify(text),
                "error": item.get("error"),
            }
        )

    repair_records = []
    if args.emit_noop_retry:
        src = _best_source(state)
        branches_dir = iter_dir / "branches"
        count = int(args.branches or state.get("branches", 1) or 1)
        branch_plan = {"iter": int(args.iter), "source": str(src), "include_noop_fallback": True, "selected_methods": [], "repair": True, "branches": []}
        plans = _repair_plans(failures)
        plan_records = [{"branch_offset": idx + 2, "transforms": plan} for idx, plan in enumerate(plans)]
        for idx in range(1, count + 1):
            branch_dir = branches_dir / f"b{idx}"
            branch_dir.mkdir(parents=True, exist_ok=True)
            dst = branch_dir / f"kernel{src.suffix}"
            mode = "repair_noop_copy_best"
            applied: list[str] = []
            if idx > 1 and src.suffix.lower() in {".hip", ".cu", ".cpp", ".cc", ".cxx"} and idx - 2 < len(plans):
                ok, applied = _emit_variant(src, dst, plans[idx - 2])
                if ok:
                    mode = "repair_conservative_transform"
                else:
                    shutil.copy2(src, dst)
            else:
                shutil.copy2(src, dst)
            record = {
                "branch": idx,
                "source": str(src),
                "kernel": str(dst),
                "mode": mode,
                "repair_transforms": applied,
                "claimed_method_ids": [],
                "claimed_methods": [],
            }
            branch_plan["branches"].append(record)
            repair_records.append(record)
        _write_json(iter_dir / "branch_plan.json", branch_plan)

    report = {
        "iter": int(args.iter),
        "state": str(state_path),
        "failure_count": len(failures),
        "failures": failures,
        "failure_guidance": _failure_guidance(failures),
        "semantic_repair_checklist": _semantic_repair_checklist(failures),
        "planned_repairs": plan_records if args.emit_noop_retry else [],
        "repair_branches": repair_records,
        "next_action": "rerun orchestrate.py close-iter" if repair_records else "inspect failure classes and add a method-specific repair generator",
    }
    _write_json(iter_dir / "repair_report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report, 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify failed branches and optionally emit no-op retry branches")
    parser.add_argument("--state", required=True)
    parser.add_argument("--iter", type=int, required=True)
    parser.add_argument("--branches", type=int, default=0)
    parser.add_argument("--emit-noop-retry", action="store_true")
    args = parser.parse_args()
    _, code = run(args)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
