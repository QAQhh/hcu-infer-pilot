#!/usr/bin/env python3
"""Generate conservative ablation kernels for the current champion.

The generated ablations are intentionally simple and metadata-driven.  They
prefer branch_plan alternatives with fewer claimed methods; when no such
candidate exists, they create a no-op copy and mark the attribution as neutral.
"""

from __future__ import annotations

import argparse
import json
import os
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


def _method_slug(method_id: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in method_id).strip("_") or "unknown"


def _find_kernel(directory: Path) -> Path | None:
    for ext in KERNEL_EXTS:
        path = directory / f"kernel{ext}"
        if path.is_file():
            return path
    return None


def _branch_by_index(plan: dict[str, Any], idx: int) -> dict[str, Any]:
    for item in plan.get("branches", []) or []:
        try:
            if int(item.get("branch")) == int(idx):
                return item
        except (TypeError, ValueError):
            continue
    return {}


def _load_methods(iter_dir: Path) -> list[dict[str, Any]]:
    champion = iter_dir / "champion_methods.json"
    methods = champion if champion.is_file() else iter_dir / "methods.json"
    if not methods.is_file():
        return []
    raw = _read_json(methods).get("methods", [])
    return [item for item in raw if isinstance(item, dict)]


def _select_ablation_source(iter_dir: Path, method_id: str, champion_branch: int | None, champion_kernel: Path) -> tuple[Path, str]:
    plan_path = iter_dir / "branch_plan.json"
    if not plan_path.is_file():
        return champion_kernel, "noop_no_branch_plan"
    plan = _read_json(plan_path)
    alternatives: list[tuple[int, Path, str]] = []
    for item in plan.get("branches", []) or []:
        try:
            idx = int(item.get("branch"))
        except (TypeError, ValueError):
            continue
        if champion_branch is not None and idx == champion_branch:
            continue
        claims = {str(mid) for mid in item.get("claimed_method_ids", []) or []}
        if method_id in claims:
            continue
        kernel_text = str(item.get("kernel") or "")
        kernel = Path(kernel_text) if kernel_text else _find_kernel(iter_dir / "branches" / f"b{idx}")
        if kernel and kernel.is_file():
            mode = str(item.get("mode") or "branch_alternative")
            alternatives.append((idx, kernel, mode))
    if alternatives:
        # Prefer no-op fallback if present, otherwise the first branch without
        # this method claim.
        alternatives.sort(key=lambda entry: (0 if "noop" in entry[2] else 1, entry[0]))
        idx, kernel, mode = alternatives[0]
        return kernel, f"branch_{idx}_{mode}"
    return champion_kernel, "noop_no_claim_free_branch"


def _source_kind_to_confidence(source_kind: str) -> dict[str, Any]:
    if source_kind.startswith("branch_") and "noop" not in source_kind:
        return {
            "confidence": "medium",
            "meaning": "uses another valid generated branch without this method claim; benchmark can estimate contribution but branch may differ in other details",
            "expected_attribution": "benchmark_required",
        }
    if "noop" in source_kind:
        return {
            "confidence": "low",
            "meaning": "no true method-minus-one branch exists; attribution is neutral placeholder unless manually replaced",
            "expected_attribution": "neutral",
        }
    return {
        "confidence": "low",
        "meaning": "unknown ablation source type",
        "expected_attribution": "neutral",
    }


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    state_path = Path(args.state).expanduser().resolve()
    state = _read_json(state_path)
    iter_dir = Path(state["run_dir"]) / f"iterv{int(args.iter)}"
    branch_results_path = iter_dir / "branch_results.json"
    branch_results = _read_json(branch_results_path) if branch_results_path.is_file() else {}
    champion = branch_results.get("champion", {}) if isinstance(branch_results.get("champion"), dict) else {}
    champion_branch = champion.get("branch_index")
    try:
        champion_branch = int(champion_branch) if champion_branch is not None else None
    except (TypeError, ValueError):
        champion_branch = None

    champion_kernel = _find_kernel(iter_dir)
    if champion_kernel is None:
        raise SystemExit(f"no champion kernel found in {iter_dir}")

    methods = _load_methods(iter_dir)
    out_root = iter_dir / "ablations"
    records = []
    for method in methods:
        mid = str(method.get("id") or "")
        if not mid:
            continue
        src, source_kind = _select_ablation_source(iter_dir, mid, champion_branch, champion_kernel)
        method_dir = out_root / _method_slug(mid)
        method_dir.mkdir(parents=True, exist_ok=True)
        dst = method_dir / f"kernel{src.suffix}"
        if src.resolve() != dst.resolve():
            shutil.copy2(src, dst)
        confidence = _source_kind_to_confidence(source_kind)
        record = {
            "method_id": mid,
            "method": method,
            "source_kernel": str(src),
            "ablated_kernel": str(dst),
            "source_kind": source_kind,
            "expected_attribution": confidence["expected_attribution"],
            "confidence": confidence["confidence"],
            "meaning": confidence["meaning"],
        }
        records.append(record)

    true_ablation_count = sum(1 for item in records if item.get("expected_attribution") == "benchmark_required")
    neutral_count = sum(1 for item in records if item.get("expected_attribution") == "neutral")
    manifest = {
        "iter": int(args.iter),
        "state": str(state_path),
        "champion_kernel": str(champion_kernel),
        "champion_branch": champion_branch,
        "summary": {
            "method_count": len(methods),
            "benchmark_required_count": true_ablation_count,
            "neutral_placeholder_count": neutral_count,
            "note": "Neutral placeholders should not be interpreted as proof that a method contributed or failed.",
        },
        "ablations": records,
    }
    _write_json(out_root / "ablation_manifest.json", manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest, 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate conservative ablation kernels from branch_plan/champion metadata")
    parser.add_argument("--state", required=True)
    parser.add_argument("--iter", type=int, required=True)
    args = parser.parse_args()
    _, code = run(args)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
