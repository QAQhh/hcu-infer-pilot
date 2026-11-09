#!/usr/bin/env python3
"""Validate final Hygon Triton optimizer deliverables.

This is intentionally stricter than the runtime scripts: it checks whether the
human-facing deliverable contains the evidence and explanations that make a run
auditable, not just whether the kernel benchmarked successfully.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_SECTION_ALIASES = [
    ("最终 Kernel 快照", ["## Final Kernel Snapshot", "## 最终 Kernel 快照", "## 最终 Kernel 快照与指标"]),
    ("算子计算逻辑", ["## Kernel Computation Logic", "## 算子计算逻辑"]),
    ("最终指标", ["## Final Case Metrics", "## 最终指标", "## 最终 Kernel 快照与指标"]),
    ("尝试时间线", ["## Attempt Timeline", "## 尝试时间线"]),
]

REQUIRED_EXPLANATION_MARKER_ALIASES = [
    ("指标来源", ["Metric Provenance", "指标来源"]),
    ("配置搜索", ["Autotune / Config Sweep", "配置搜索"]),
    ("知识沉淀", ["知识沉淀", "optimization_memory", "triton_optimization_memory.md"]),
]

ARTIFACT_EXTS = {".ttir", ".ttgir", ".amdgcn", ".hsaco"}
# Fingerprints of UTF-8 Chinese mis-decoded then re-saved; not display text.
MOJIBAKE_MARKERS = ["\u9225", "\u9474", "\u7eee", "\u93bb", "\u6d93", "\u7584", "\u59e3"]
FORMULA_RE = re.compile(
    r"(\b[A-Za-z_]\w*(?:\[[^\]]+\])?\s*=)|"
    r"(\\sum|\\max|\\operatorname)|"
    r"(\b(?:max|sum|softmax|exp|exp2|dot|einsum)\s*\()|"
    r"(@)|"
    r"(\u2200)"
)
PY_REF_RE = re.compile(r"```(?:python)?[\s\S]*?(?:def\s+reference\b|torch\.|np\.|numpy\.)[\s\S]*?```")
REFERENCE_PLACEHOLDER_RE = re.compile(
    r"```(?:python)?\s*def\s+reference\(\.\.\.\):[\s\S]*?\.\.\.\s*```",
    re.IGNORECASE,
)
VALID_REQUIRED_SHAPE_FAMILY_NAMES = {"small", "middle", "large"}
VALID_MERGE_POLICIES = {
    "runtime_config_dispatch",
    "runtime_variant_dispatch",
    "runtime_config_or_variant_dispatch",
    "single_config_proven",
}


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def _read_json(path: Path) -> dict:
    return json.loads(_read_text(path))


def _section_body(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    rest = text[start + len(heading) :]
    match = re.search(r"\n## ", rest)
    return rest[: match.start()] if match else rest


def _section_body_any(text: str, headings: list[str]) -> str:
    for heading in headings:
        body = _section_body(text, heading)
        if body:
            return body
    return ""


def _has_chinese(text: str, min_chars: int = 80) -> bool:
    return len(re.findall(r"[\u4e00-\u9fff]", text)) >= min_chars


def _artifact_counts(root: Path) -> dict[str, int]:
    counts = {ext: 0 for ext in sorted(ARTIFACT_EXTS)}
    if not root.exists():
        return counts
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in counts:
            counts[path.suffix] += 1
    return counts


def _require_artifact_family(errors: list[str], root: Path, label: str) -> None:
    counts = _artifact_counts(root)
    missing = [ext for ext, count in counts.items() if count == 0]
    if missing:
        errors.append(f"{label} missing artifact types {missing}: {root}")


def _resolve_path(value: str | None, base: Path) -> Path | None:
    if not value:
        return None
    path = Path(value)
    return path if path.is_absolute() else base / path


def _find_shape_family_plan(run_dir: Path, case_dir: Path | None, explicit: Path | None) -> Path | None:
    if explicit:
        return explicit
    candidates = []
    if case_dir:
        candidates.append(case_dir / "shape_family_plan.json")
    candidates.extend([
        run_dir / "shape_family_plan.json",
        run_dir.parent / "shape_family_plan.json",
    ])
    return next((path for path in candidates if path.is_file()), None)


def _find_dispatch_manifest(
    run_dir: Path,
    case_dir: Path | None,
    plan_path: Path,
    explicit: Path | None,
) -> Path:
    if explicit:
        return explicit
    candidates = []
    if case_dir:
        candidates.append(case_dir / "dispatch_manifest.json")
    candidates.extend([
        plan_path.parent / "dispatch_manifest.json",
        run_dir / "dispatch_manifest.json",
        run_dir.parent / "dispatch_manifest.json",
    ])
    return next((path for path in candidates if path.is_file()), candidates[0])


def _load_shape_family_plan(path: Path | None, errors: list[str]) -> tuple[dict | None, bool]:
    if not path:
        return None, False
    try:
        plan = _read_json(path)
    except json.JSONDecodeError as exc:
        errors.append(f"shape_family_plan.json is not valid JSON: {path}: {exc}")
        return None, False
    return plan, bool(plan.get("required", False))


def _manifest_families(manifest: dict) -> list[dict]:
    families = manifest.get("families", [])
    if isinstance(families, dict):
        out = []
        for name, item in families.items():
            if isinstance(item, dict):
                out.append({"name": name, **item})
        return out
    return families if isinstance(families, list) else []


def _check_family_run(errors: list[str], family: dict, manifest_dir: Path) -> None:
    name = str(family.get("name") or "")
    run_dir = _resolve_path(family.get("run_dir"), manifest_dir)
    if not run_dir:
        errors.append(f"dispatch_manifest family '{name}' missing run_dir")
        return
    for rel in ["summary.md", "final_kernel.py", "final_config.json", "final_kernel_manifest.json", "final_bench.json"]:
        if not (run_dir / rel).is_file():
            errors.append(f"family '{name}' missing finalized artifact: {run_dir / rel}")
    bench_path = _resolve_path(family.get("final_bench"), manifest_dir) or (run_dir / "final_bench.json")
    if bench_path.is_file():
        try:
            bench = _read_json(bench_path)
            if not bench.get("correctness", {}).get("passed"):
                errors.append(f"family '{name}' final bench correctness.passed is not true: {bench_path}")
        except json.JSONDecodeError as exc:
            errors.append(f"family '{name}' final bench is not valid JSON: {bench_path}: {exc}")
    else:
        errors.append(f"family '{name}' missing final bench: {bench_path}")


def _validate_shape_family_merge(
    errors: list[str],
    warnings: list[str],
    run_dir: Path,
    case_dir: Path | None,
    summary_text: str,
    shape_family_plan: Path | None,
    dispatch_manifest: Path | None,
) -> None:
    plan_path = _find_shape_family_plan(run_dir, case_dir, shape_family_plan)
    if not plan_path:
        return
    plan, required = _load_shape_family_plan(plan_path, errors)
    if not plan:
        return
    if not required:
        return
    families = plan.get("families", [])
    if not isinstance(families, list) or not families:
        errors.append(f"shape_family_plan.json required=true but has no families: {plan_path}")
        return
    if len(families) > 3:
        errors.append(f"shape_family_plan.json supports at most 3 families, got {len(families)}: {plan_path}")
    plan_names = {str(f.get("name") or "") for f in families if isinstance(f, dict)}
    bad_names = sorted(name for name in plan_names if name not in VALID_REQUIRED_SHAPE_FAMILY_NAMES)
    if bad_names:
        errors.append(f"shape_family_plan.json required=true has unsupported family names {bad_names}; use small/middle/large")

    manifest_path = _find_dispatch_manifest(run_dir, case_dir, plan_path, dispatch_manifest)
    if not manifest_path.is_file():
        errors.append(f"shape family plan requires dispatch_manifest.json: {manifest_path}")
        return
    try:
        manifest = _read_json(manifest_path)
    except json.JSONDecodeError as exc:
        errors.append(f"dispatch_manifest.json is not valid JSON: {manifest_path}: {exc}")
        return
    policy = str(manifest.get("merge_policy") or plan.get("merge_policy") or "")
    if policy not in VALID_MERGE_POLICIES:
        errors.append(f"dispatch_manifest merge_policy must be one of {sorted(VALID_MERGE_POLICIES)}, got {policy!r}")
    manifest_families = _manifest_families(manifest)
    manifest_names = {str(f.get("name") or "") for f in manifest_families}
    missing = sorted(plan_names - manifest_names)
    extra = sorted(manifest_names - plan_names)
    if missing:
        errors.append(f"dispatch_manifest missing families from plan: {missing}")
    if extra:
        warnings.append(f"dispatch_manifest has extra families not in plan: {extra}")
    for family in manifest_families:
        _check_family_run(errors, family, manifest_path.parent)
    final_kernel = _resolve_path(manifest.get("final_kernel"), manifest_path.parent) or (case_dir / "final_kernel.py" if case_dir else run_dir / "final_kernel.py")
    if not final_kernel.is_file():
        errors.append(f"dispatch_manifest final_kernel missing: {final_kernel}")
    if summary_text and not re.search(r"Shape Family|shape family|dispatch|Dispatch|runtime_config", summary_text):
        errors.append("summary.md must explain shape-family split and final runtime dispatch/merge policy")


def validate(
    run_dir: Path,
    case_dir: Path | None = None,
    shape_family_plan: Path | None = None,
    dispatch_manifest: Path | None = None,
) -> tuple[bool, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    plan_path = _find_shape_family_plan(run_dir, case_dir, shape_family_plan)
    plan, plan_required = _load_shape_family_plan(plan_path, errors)

    summary = run_dir / "summary.md"
    if not summary.is_file():
        errors.append(f"summary.md missing: {summary}")
        text = ""
    else:
        text = _read_text(summary)
    if plan_required and case_dir:
        case_summary = next((path for path in [case_dir / "summary.md", case_dir / "optimization_summary.md"] if path.is_file()), None)
        if case_summary:
            text = _read_text(case_summary)

    for label, aliases in REQUIRED_SECTION_ALIASES:
        if not any(alias in text for alias in aliases):
            errors.append(f"required section missing from summary.md: {label} ({' / '.join(aliases)})")

    for label, aliases in REQUIRED_EXPLANATION_MARKER_ALIASES:
        if not any(alias in text for alias in aliases):
            errors.append(f"summary.md missing required explanation marker: {label} ({' / '.join(aliases)})")

    if text and not _has_chinese(text):
        errors.append("summary.md must be written in Chinese by default, preserving required English headings")

    logic = _section_body_any(text, ["## Kernel Computation Logic", "## 算子计算逻辑"])
    if logic:
        semantic_logic = REFERENCE_PLACEHOLDER_RE.sub("", logic)
        has_formula = bool(FORMULA_RE.search(semantic_logic))
        if not has_formula:
            errors.append(
                "Kernel Computation Logic must include a mathematical formula; "
                "Python Reference Form is not a substitute"
            )
        if re.search(r"###\s+Python Reference Form|\bdef\s+reference\s*\(", semantic_logic, re.IGNORECASE):
            errors.append("summary.md should not include Python Reference Form; keep the final report formula-first")
    memory = _section_body(text, "## 知识沉淀")
    if memory and re.search(r"Agent\s*必须|交付前请补充|TODO|待填写", memory, re.IGNORECASE):
        errors.append("知识沉淀 section still contains a placeholder; state whether triton_optimization_memory.md was appended or why it was not")
    if memory and "not_appended_by_summarize" in memory:
        warnings.append("知识沉淀 section still has summarize.py's provisional status; final review should replace it with appended/not_appended plus reason")
    if any(marker in text for marker in MOJIBAKE_MARKERS):
        warnings.append("summary.md appears to contain mojibake; rewrite generated template text in UTF-8 Chinese")

    for rel in [
        "final_kernel.py",
        "final_config.json",
        "final_kernel_manifest.json",
        "final_bench.json",
        "attempt_timeline.json",
        "attempt_timeline.svg",
    ]:
        if not (run_dir / rel).is_file():
            errors.append(f"required final file missing: {run_dir / rel}")

    _require_artifact_family(errors, run_dir / "irs" / "final_cache", "final_cache")
    kernel_artifact_roots = list((run_dir / "iterv1" / "irs" / "kernel").glob("*"))
    if not kernel_artifact_roots:
        errors.append("promoted iteration kernel IRs missing under iterv*/irs/kernel")
    else:
        has_full_kernel_artifacts = False
        for root in kernel_artifact_roots:
            counts = _artifact_counts(root)
            if all(counts[ext] > 0 for ext in ARTIFACT_EXTS):
                has_full_kernel_artifacts = True
                break
        if not has_full_kernel_artifacts:
            errors.append("no promoted iteration artifact directory contains ttir, ttgir, amdgcn, and hsaco")

    final_bench = run_dir / "final_bench.json"
    if final_bench.is_file():
        try:
            bench = json.loads(_read_text(final_bench))
            if not bench.get("correctness", {}).get("passed"):
                errors.append("final_bench.json correctness.passed is not true")
            if not bench.get("disable_autotune", False):
                warnings.append("final_bench.json does not record disable_autotune=true")
            if not bench.get("active_config"):
                errors.append("final_bench.json missing active_config")
        except json.JSONDecodeError as exc:
            errors.append(f"final_bench.json is not valid JSON: {exc}")

    if case_dir and plan_required:
        for rel in ["final_kernel.py", "dispatch_manifest.json"]:
            if not (case_dir / rel).is_file():
                errors.append(f"multi-family case output missing: {case_dir / rel}")
    elif case_dir:
        for rel in [
            "optimized_kernel.py",
            "optimized_config.json",
            "optimization_summary.md",
            "final_bench.json",
            "final_kernel_manifest.json",
            "attempt_timeline.json",
            "attempt_timeline.svg",
        ]:
            if not (case_dir / rel).is_file():
                errors.append(f"case output missing: {case_dir / rel}")
        _require_artifact_family(errors, case_dir / "irs" / "final_cache", "case final_cache")
        _require_artifact_family(errors, case_dir / "irs" / "iterv1_kernel", "case iterv1_kernel")

    _validate_shape_family_merge(
        errors,
        warnings,
        run_dir,
        case_dir,
        text,
        plan_path,
        dispatch_manifest,
    )

    return (not errors, errors, warnings)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--case-dir", default="")
    parser.add_argument("--shape-family-plan", default="")
    parser.add_argument("--dispatch-manifest", default="")
    args = parser.parse_args()

    ok, errors, warnings = validate(
        Path(args.run_dir).resolve(),
        Path(args.case_dir).resolve() if args.case_dir else None,
        Path(args.shape_family_plan).resolve() if args.shape_family_plan else None,
        Path(args.dispatch_manifest).resolve() if args.dispatch_manifest else None,
    )
    payload = {"valid": ok, "errors": errors, "warnings": warnings}
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
