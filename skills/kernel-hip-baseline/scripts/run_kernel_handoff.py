#!/usr/bin/env python3
"""Drive advisor kernel handoff into baseline generation and kernel optimization.

This is the deterministic bridge for:

    kernel_handoff_manifest -> baseline-generator -> kernel-optimizer setup
    -> optional automatic optimizer loop

By default it stops after optimizer setup so callers can inspect the generated
contract. Pass --auto-loop to continue through the optimizer's measured
open-iter -> branch generation -> close-iter -> finalize loop.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
BASELINE_SKILL_DIR = SCRIPT_DIR.parent
OPTIMIZER_SCRIPT_DIR = BASELINE_SKILL_DIR.parent / "kernel-hip-optimize" / "scripts"

PYTHON_REF_EXTS = {".py"}
SOURCE_EXTS = {".py", ".cu", ".cuh", ".cpp", ".cc", ".cxx", ".hip"}
BASELINE_EXTS = {".hip", ".cu", ".cpp", ".cc", ".cxx", ".py"}


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _cmd_str(cmd: list[str | Path]) -> str:
    return " ".join(shlex.quote(str(item)) for item in cmd)


def _load_handoff(path: Path) -> dict[str, Any]:
    payload = _read_json(path)
    manifest = payload.get("kernel_handoff_manifest", payload)
    if not isinstance(manifest, dict):
        raise SystemExit(f"{path} does not contain a kernel_handoff_manifest object")
    if "routing" not in manifest or "handoff_targets" not in manifest:
        raise SystemExit(f"{path} is not an advisor kernel handoff manifest")
    return manifest


def _normalize_dims(value: Any) -> dict[str, int]:
    if not isinstance(value, dict):
        return {}
    out: dict[str, int] = {}
    for key, raw in value.items():
        if isinstance(raw, bool):
            continue
        try:
            out[str(key)] = int(raw)
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"dims value for {key!r} must be int-like, got {raw!r}") from exc
    return out


def _dims_from_manifest(manifest: dict[str, Any], target_name: str) -> dict[str, int]:
    targets = manifest.get("handoff_targets", {}) or {}
    target = targets.get(target_name, {}) or {}
    contract = manifest.get("operator_contract", {}) or {}
    for value in (target.get("dims"), contract.get("dims")):
        dims = _normalize_dims(value)
        if dims:
            return dims
    return {}


def _ptr_size_from_manifest(manifest: dict[str, Any], target_name: str, dims: dict[str, int]) -> int:
    targets = manifest.get("handoff_targets", {}) or {}
    target = targets.get(target_name, {}) or {}
    contract = manifest.get("operator_contract", {}) or {}
    for value in (target.get("ptr_size_hint"), contract.get("ptr_size_hint")):
        try:
            hint = int(value)
        except (TypeError, ValueError):
            hint = 0
        if hint > 0:
            return hint
    if {"M", "N", "K"}.issubset(dims):
        return max(dims["M"] * dims["K"], dims["K"] * dims["N"], dims["M"] * dims["N"])
    if "N" in dims:
        return int(dims["N"])
    positives = [v for v in dims.values() if v > 0]
    return max(positives) if positives else 0


def _slug(text: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_.-]+", "_", text.strip())
    clean = clean.strip("._-")
    return clean[:80] or "kernel_handoff"


def _default_case_dir(manifest: dict[str, Any], out_root: Path) -> Path:
    hotspot = manifest.get("hotspot", {}) or {}
    name = hotspot.get("candidate_op") or hotspot.get("operator_family") or "kernel_handoff"
    ts = _dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    return out_root / f"{_slug(str(name))}_{ts}"


def _manifest_workdir(manifest: dict[str, Any]) -> Path | None:
    source = manifest.get("source", {}) or {}
    workdir = str(source.get("workdir", "") or "").strip()
    if not workdir:
        return None
    return Path(workdir).expanduser().resolve()


def _resolve_path(path_text: str, manifest_path: Path, manifest: dict[str, Any]) -> Path:
    raw = Path(path_text).expanduser()
    if raw.is_absolute():
        return raw
    manifest_relative = (manifest_path.parent / raw).resolve()
    if manifest_relative.exists():
        return manifest_relative
    workdir = _manifest_workdir(manifest)
    if workdir:
        workdir_relative = (workdir / raw).resolve()
        if workdir_relative.exists():
            return workdir_relative
    return manifest_relative


def _reference_candidates(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    targets = manifest.get("handoff_targets", {}) or {}
    baseline_target = targets.get("baseline_generator", {}) or {}
    contract = manifest.get("operator_contract", {}) or {}
    candidates: list[dict[str, Any]] = []
    preferred_path = str(baseline_target.get("preferred_reference_path", "") or "").strip()
    if preferred_path:
        candidates.append(
            {
                "path": preferred_path,
                "kind": str(baseline_target.get("preferred_reference_kind", "") or ""),
                "source": "handoff_targets.baseline_generator.preferred_reference_path",
            }
        )
    preferred = contract.get("preferred_reference", {}) or {}
    if preferred.get("path"):
        item = dict(preferred)
        item["source"] = "operator_contract.preferred_reference"
        candidates.append(item)
    for item in contract.get("reference_candidates", []) or []:
        if isinstance(item, dict) and item.get("path"):
            copied = dict(item)
            copied["source"] = "operator_contract.reference_candidates"
            candidates.append(copied)

    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in candidates:
        path_text = str(item.get("path", "") or "").strip()
        if not path_text or path_text in seen:
            continue
        seen.add(path_text)
        out.append(item)
    return out


def _choose_python_reference(manifest: dict[str, Any], manifest_path: Path) -> tuple[Path | None, list[str]]:
    reasons: list[str] = []
    for item in _reference_candidates(manifest):
        path_text = str(item.get("path", "") or "").strip()
        resolved = _resolve_path(path_text, manifest_path, manifest)
        suffix = resolved.suffix.lower()
        if suffix not in SOURCE_EXTS:
            reasons.append(f"skip {path_text}: unsupported source extension {suffix or '<none>'}")
            continue
        if suffix not in PYTHON_REF_EXTS:
            reasons.append(f"skip {path_text}: automatic baseline scaffold currently supports Python reference files only")
            continue
        if not resolved.is_file():
            reasons.append(f"skip {path_text}: file not found after path resolution")
            continue
        return resolved, reasons
    return None, reasons


def _operator_to_baseline_op(manifest: dict[str, Any], forced: str) -> str:
    if forced != "auto":
        return forced
    family = str((manifest.get("hotspot", {}) or {}).get("operator_family", "") or "").lower()
    if "matmul" in family or "gemm" in family:
        return "matmul"
    if "reduction" in family or "softmax" in family or "norm" in family:
        return "reduction"
    if "elementwise" in family:
        return "elementwise"
    return "auto"


def _run_step(name: str, cmd: list[str | Path], logs_dir: Path, dry_run: bool) -> dict[str, Any]:
    item: dict[str, Any] = {"name": name, "cmd": [str(part) for part in cmd], "cmd_text": _cmd_str(cmd)}
    if dry_run:
        item["status"] = "planned"
        return item
    logs_dir.mkdir(parents=True, exist_ok=True)
    stdout_path = logs_dir / f"{name}.stdout.txt"
    stderr_path = logs_dir / f"{name}.stderr.txt"
    proc = subprocess.run(cmd, text=True, capture_output=True, encoding="utf-8", errors="ignore")
    stdout_path.write_text(proc.stdout or "", encoding="utf-8")
    stderr_path.write_text(proc.stderr or "", encoding="utf-8")
    item.update(
        {
            "status": "ok" if proc.returncode == 0 else "failed",
            "returncode": proc.returncode,
            "stdout": str(stdout_path),
            "stderr": str(stderr_path),
        }
    )
    return item


def _parse_json_from_stdout(path_text: str) -> dict[str, Any]:
    if not path_text:
        return {}
    path = Path(path_text)
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for start in range(len(lines)):
        candidate = "\n".join(lines[start:])
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            return data
    return {}


def _reference_analysis_errors(analysis_path: Path) -> list[str]:
    if not analysis_path.is_file():
        return [f"ref analysis missing: {analysis_path}"]
    analysis = _read_json(analysis_path)
    chosen = analysis.get("chosen_reference") or {}
    sig = analysis.get("signature_hint") or {}
    unsupported = [str(item) for item in (analysis.get("unsupported_assumptions") or [])]
    errors: list[str] = []
    if not chosen:
        errors.append("no chosen Python reference function")
    chosen_name = str(chosen.get("name", "") or "")
    explicit_names = {"reference", "torch_ref", "golden", "ref", "oracle", "gold"}
    if chosen_name not in explicit_names:
        errors.append(
            f"chosen function `{chosen_name or '<none>'}` is not an explicit reference/oracle name; "
            "auto handoff requires reference/torch_ref/golden/ref/oracle/gold"
        )
    tensor_args = sig.get("tensor_args") or []
    output_args = sig.get("output_args") or []
    return_style = str(sig.get("return_style", "") or "")
    if not tensor_args:
        errors.append("no tensor-like input arguments in chosen reference")
    if return_style == "unknown" and not output_args:
        errors.append("chosen reference has unknown output contract")
    for item in unsupported:
        lowered = item.lower()
        if "unknown" in lowered or "no tensor-like" in lowered or "oracle" in lowered or "no plain python reference" in lowered:
            errors.append(item)
    return errors


def _blocked_report(
    *,
    status: str,
    reason: str,
    manifest_path: Path,
    manifest: dict[str, Any],
    case_dir: Path,
    args: argparse.Namespace,
    extra: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], int]:
    targets = manifest.get("handoff_targets", {}) or {}
    report = {
        "status": status,
        "reason": reason,
        "manifest": str(manifest_path.resolve()),
        "case_dir": str(case_dir.resolve()),
        "routing": manifest.get("routing", {}),
        "handoff_targets": {
            "baseline_generator": targets.get("baseline_generator", {}),
            "kernel_optimizer": targets.get("kernel_optimizer", {}),
        },
        "dry_run": bool(args.dry_run),
    }
    if extra:
        report.update(extra)
    return report, 0 if args.dry_run else 2


def _direct_optimizer_inputs(manifest: dict[str, Any], manifest_path: Path) -> tuple[Path, Path, dict[str, int], int]:
    target = ((manifest.get("handoff_targets", {}) or {}).get("kernel_optimizer", {}) or {})
    baseline = str(target.get("baseline_kernel_path", "") or "").strip()
    ref = str(target.get("python_reference_path", "") or "").strip()
    if not baseline or not ref:
        raise SystemExit("kernel optimizer target is ready but baseline/ref path is missing")
    baseline_path = _resolve_path(baseline, manifest_path, manifest)
    ref_path = _resolve_path(ref, manifest_path, manifest)
    if baseline_path.suffix.lower() not in BASELINE_EXTS:
        raise SystemExit(f"unsupported baseline extension: {baseline_path}")
    if ref_path.suffix.lower() != ".py":
        raise SystemExit(f"optimizer reference must be a Python file: {ref_path}")
    dims = _dims_from_manifest(manifest, "kernel_optimizer")
    ptr_size = _ptr_size_from_manifest(manifest, "kernel_optimizer", dims)
    return baseline_path, ref_path, dims, ptr_size


def _optimizer_setup(
    *,
    baseline: Path,
    ref: Path,
    dims: dict[str, int],
    ptr_size: int,
    case_dir: Path,
    args: argparse.Namespace,
) -> tuple[dict[str, Any], dict[str, Any]]:
    logs_dir = case_dir / "logs"
    dims_json = json.dumps(dims, separators=(",", ":"))
    cmd: list[str | Path] = [
        sys.executable,
        OPTIMIZER_SCRIPT_DIR / "orchestrate.py",
        "setup",
        "--baseline",
        baseline,
        "--ref",
        ref,
        "--dims",
        dims_json,
        "--ptr-size",
        str(ptr_size),
        "--iterations",
        str(args.iterations),
        "--branches",
        str(args.branches),
        "--ncu-num",
        str(args.ncu_num),
        "--warmup",
        str(args.warmup),
        "--repeat",
        str(args.repeat),
        "--noise-threshold-pct",
        str(args.noise_threshold_pct),
    ]
    if args.env_out:
        cmd.extend(["--env-out", args.env_out])
    step = _run_step("optimizer_setup", cmd, logs_dir, args.dry_run)
    setup_info = _parse_json_from_stdout(step.get("stdout", ""))
    run_dir = str(setup_info.get("run_dir", "") or "")
    if run_dir:
        setup_info["next_auto_command"] = (
            f"{shlex.quote(sys.executable)} "
            f"{shlex.quote(str(OPTIMIZER_SCRIPT_DIR / 'auto_kernel_optimize.py'))} "
            f"--run-dir {shlex.quote(run_dir)} --iter 1 --prepare-only"
        )
        setup_info["next_auto_loop_command"] = (
            f"{shlex.quote(sys.executable)} "
            f"{shlex.quote(str(OPTIMIZER_SCRIPT_DIR / 'run_auto_loop.py'))} "
            f"--run-dir {shlex.quote(run_dir)} --max-iters {int(args.auto_loop_max_iters)} "
            f"--branches {int(args.branches)} --warmup {int(args.warmup)} --repeat {int(args.repeat)} --finalize"
        )
    return step, setup_info


def _optimizer_auto_loop(
    *,
    run_dir: str,
    case_dir: Path,
    args: argparse.Namespace,
) -> tuple[dict[str, Any], dict[str, Any]]:
    logs_dir = case_dir / "logs"
    run_dir_arg = run_dir or "<optimizer-run-dir-from-setup>"
    if not run_dir and not args.dry_run:
        return (
            {
                "name": "optimizer_auto_loop",
                "status": "failed",
                "returncode": 2,
                "error": "optimizer setup did not return run_dir",
            },
            {},
        )

    cmd: list[str | Path] = [
        sys.executable,
        OPTIMIZER_SCRIPT_DIR / "run_auto_loop.py",
        "--run-dir",
        run_dir_arg,
        "--start-iter",
        str(args.auto_loop_start_iter),
        "--max-iters",
        str(args.auto_loop_max_iters),
        "--branches",
        str(args.branches),
        "--warmup",
        str(args.warmup),
        "--repeat",
        str(args.repeat),
        "--retries",
        str(args.retries),
        "--selection-policy",
        args.selection_policy,
        "--branch-mode",
        args.branch_mode,
    ]
    if not args.no_auto_loop_finalize:
        cmd.append("--finalize")
    if args.auto_loop_prepare_only:
        cmd.append("--prepare-only")
    if args.no_repair_on_fail:
        cmd.append("--no-repair-on-fail")
    step = _run_step("optimizer_auto_loop", cmd, logs_dir, args.dry_run)
    loop_info = _parse_json_from_stdout(step.get("stdout", ""))
    return step, loop_info


def _maybe_run_optimizer_auto_loop(report: dict[str, Any], setup_info: dict[str, Any], case_dir: Path, args: argparse.Namespace) -> tuple[dict[str, Any], int | None]:
    if not args.auto_loop:
        return report, None
    run_dir = str(setup_info.get("run_dir", "") or "")
    loop_step, loop_info = _optimizer_auto_loop(run_dir=run_dir, case_dir=case_dir, args=args)
    report["steps"].append(loop_step)
    report["optimizer_auto_loop"] = loop_info
    if loop_step.get("returncode", 0) not in (0, None):
        report["status"] = "optimizer_auto_loop_failed"
        return report, int(loop_step.get("returncode", 1) or 1)
    report["status"] = "optimizer_auto_loop_completed" if not args.dry_run else "optimizer_auto_loop_planned"
    if loop_info.get("report"):
        report["auto_loop_report"] = loop_info.get("report")
    if loop_info.get("run_dir"):
        report["optimizer_run_dir"] = loop_info.get("run_dir")
    return report, 0


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    if args.auto_loop and args.skip_optimizer_setup:
        raise SystemExit("--auto-loop cannot be combined with --skip-optimizer-setup")
    manifest_path = Path(args.manifest).expanduser().resolve()
    manifest = _load_handoff(manifest_path)
    out_root = Path(args.out_root).expanduser().resolve()
    case_dir = Path(args.case_dir).expanduser().resolve() if args.case_dir else _default_case_dir(manifest, out_root).resolve()
    if case_dir.exists() and any(case_dir.iterdir()) and not args.force:
        raise SystemExit(f"case dir already exists and is not empty: {case_dir} (use --force)")
    case_dir.mkdir(parents=True, exist_ok=True)

    routing = manifest.get("routing", {}) or {}
    targets = manifest.get("handoff_targets", {}) or {}
    baseline_target = targets.get("baseline_generator", {}) or {}
    optimizer_target = targets.get("kernel_optimizer", {}) or {}
    report: dict[str, Any] = {
        "status": "started",
        "manifest": str(manifest_path),
        "case_dir": str(case_dir),
        "dry_run": bool(args.dry_run),
        "routing": routing,
        "steps": [],
    }

    if not bool(routing.get("route_allows_kernel")):
        return _blocked_report(
            status="blocked_by_route",
            reason="advisor route does not allow kernel handoff",
            manifest_path=manifest_path,
            manifest=manifest,
            case_dir=case_dir,
            args=args,
        )

    if bool(optimizer_target.get("ready")):
        baseline, ref, dims, ptr_size = _direct_optimizer_inputs(manifest, manifest_path)
        report.update(
            {
                "status": "optimizer_ready",
                "baseline": str(baseline),
                "ref": str(ref),
                "dims": dims,
                "ptr_size": ptr_size,
            }
        )
        if args.skip_optimizer_setup:
            report["status"] = "optimizer_ready_skipped_setup"
            return report, 0
        setup_step, setup_info = _optimizer_setup(
            baseline=baseline,
            ref=ref,
            dims=dims,
            ptr_size=ptr_size,
            case_dir=case_dir,
            args=args,
        )
        report["steps"].append(setup_step)
        report["optimizer_setup"] = setup_info
        if setup_step.get("returncode", 0) not in (0, None):
            report["status"] = "optimizer_setup_failed"
            return report, int(setup_step.get("returncode", 1) or 1)
        report["status"] = "optimizer_setup_ready" if not args.dry_run else "optimizer_setup_planned"
        report, loop_exit = _maybe_run_optimizer_auto_loop(report, setup_info, case_dir, args)
        if loop_exit is not None:
            return report, loop_exit
        return report, 0

    if not bool(baseline_target.get("ready")):
        return _blocked_report(
            status="contract_incomplete",
            reason="baseline_generator target is not ready",
            manifest_path=manifest_path,
            manifest=manifest,
            case_dir=case_dir,
            args=args,
        )

    dims = _dims_from_manifest(manifest, "baseline_generator")
    if not dims:
        return _blocked_report(
            status="contract_incomplete",
            reason="missing dims_json",
            manifest_path=manifest_path,
            manifest=manifest,
            case_dir=case_dir,
            args=args,
        )
    ref_path, candidate_notes = _choose_python_reference(manifest, manifest_path)
    if ref_path is None:
        return _blocked_report(
            status="unsupported_reference_contract",
            reason="no existing Python reference source could be resolved for automatic baseline generation",
            manifest_path=manifest_path,
            manifest=manifest,
            case_dir=case_dir,
            args=args,
            extra={"reference_candidate_notes": candidate_notes},
        )

    ptr_size = _ptr_size_from_manifest(manifest, "baseline_generator", dims)
    dims_json = json.dumps(dims, separators=(",", ":"))
    op = _operator_to_baseline_op(manifest, args.op)
    logs_dir = case_dir / "logs"
    _write_json(case_dir / "advisor_kernel_handoff_manifest.json", manifest)
    _write_json(case_dir / "shape.json", dims)
    report.update(
        {
            "status": "baseline_generation_started",
            "reference": str(ref_path),
            "dims": dims,
            "ptr_size": ptr_size,
            "baseline_op": op,
            "reference_candidate_notes": candidate_notes,
        }
    )

    inspect_cmd: list[str | Path] = [
        sys.executable,
        SCRIPT_DIR / "inspect_ref.py",
        "--ref",
        ref_path,
        "--dims",
        dims_json,
        "--out",
        case_dir / "ref_analysis.json",
    ]
    inspect_step = _run_step("inspect_ref", inspect_cmd, logs_dir, args.dry_run)
    report["steps"].append(inspect_step)
    if inspect_step.get("returncode", 0) not in (0, None):
        report["status"] = "inspect_ref_failed"
        return report, int(inspect_step.get("returncode", 1) or 1)
    if not args.dry_run:
        oracle_errors = _reference_analysis_errors(case_dir / "ref_analysis.json")
        if oracle_errors and not args.allow_weak_reference:
            report["status"] = "reference_contract_incomplete"
            report["reason"] = "chosen reference is not a reliable tensor oracle"
            report["reference_analysis_errors"] = oracle_errors
            report["next_action"] = (
                "Extract a small model-local reference file that exposes `reference(...)`, "
                "`torch_ref(...)`, `golden(...)`, or `ref(...)` with tensor inputs and a clear output."
            )
            return report, 2

    generate_cmd: list[str | Path] = [
        sys.executable,
        SCRIPT_DIR / "generate_baseline.py",
        "--analysis",
        case_dir / "ref_analysis.json",
        "--out-dir",
        case_dir,
        "--op",
        op,
        "--output-name",
        args.output_name,
    ]
    generate_step = _run_step("generate_baseline", generate_cmd, logs_dir, args.dry_run)
    report["steps"].append(generate_step)
    if generate_step.get("returncode", 0) not in (0, None):
        report["status"] = "generate_baseline_failed"
        return report, int(generate_step.get("returncode", 1) or 1)

    baseline_manifest_path = case_dir / "baseline_manifest.json"
    baseline_manifest = {} if args.dry_run else _read_json(baseline_manifest_path)
    report["baseline_manifest"] = str(baseline_manifest_path)
    if args.skip_optimizer_setup:
        report["status"] = "baseline_generated" if not args.dry_run else "baseline_generation_planned"
        return report, 0

    baseline = Path(baseline_manifest.get("kernel", case_dir / "kernel.hip"))
    ref = Path(baseline_manifest.get("ref", case_dir / "ref.py"))
    ptr_size = int(baseline_manifest.get("ptr_size_hint") or ptr_size or 0)
    setup_step, setup_info = _optimizer_setup(
        baseline=baseline,
        ref=ref,
        dims=dims,
        ptr_size=ptr_size,
        case_dir=case_dir,
        args=args,
    )
    report["steps"].append(setup_step)
    report["optimizer_setup"] = setup_info
    if setup_step.get("returncode", 0) not in (0, None):
        report["status"] = "optimizer_setup_failed"
        return report, int(setup_step.get("returncode", 1) or 1)
    report["status"] = "closed_loop_setup_ready" if not args.dry_run else "closed_loop_setup_planned"
    report, loop_exit = _maybe_run_optimizer_auto_loop(report, setup_info, case_dir, args)
    if loop_exit is not None:
        return report, loop_exit
    return report, 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Run advisor kernel handoff through baseline generation, optimizer setup, and optional auto loop")
    parser.add_argument("--manifest", required=True, help="kernel_handoff_manifest.json or optimization_context.json")
    parser.add_argument("--out-root", default="./hygon_kernel_handoff_cases", help="Root used when --case-dir is not set")
    parser.add_argument("--case-dir", default="", help="Explicit output case directory")
    parser.add_argument("--report-out", default="", help="Optional report path. Defaults to <case-dir>/handoff_run_report.json")
    parser.add_argument("--force", action="store_true", help="Allow using a non-empty case directory")
    parser.add_argument("--dry-run", action="store_true", help="Only emit planned commands and readiness decisions")
    parser.add_argument("--skip-optimizer-setup", action="store_true", help="Stop after baseline generation or direct optimizer readiness")
    parser.add_argument("--allow-weak-reference", action="store_true", help="Allow placeholder baseline generation when inspect_ref reports a weak oracle")
    parser.add_argument("--op", default="auto", choices=["auto", "elementwise", "matmul", "reduction", "unknown"])
    parser.add_argument("--output-name", default="out")
    parser.add_argument("--iterations", type=int, default=3)
    parser.add_argument("--branches", type=int, default=4)
    parser.add_argument("--ncu-num", type=int, default=5)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--repeat", type=int, default=20)
    parser.add_argument("--retries", type=int, default=0)
    parser.add_argument("--noise-threshold-pct", type=float, default=2.0)
    parser.add_argument("--env-out", default="", help="Optional optimizer env.json output path")
    parser.add_argument("--auto-loop", action="store_true", help="After optimizer setup, run the automatic kernel optimizer loop")
    parser.add_argument("--auto-loop-start-iter", type=int, default=1)
    parser.add_argument("--auto-loop-max-iters", type=int, default=0, help="0 means use optimizer state.iterations_total")
    parser.add_argument("--auto-loop-prepare-only", action="store_true", help="Generate methods/branches but do not close optimizer iterations")
    parser.add_argument("--no-auto-loop-finalize", action="store_true", help="Do not call optimizer finalize after --auto-loop")
    parser.add_argument("--selection-policy", default="evidence", choices=["evidence", "priority"])
    parser.add_argument("--branch-mode", default="method_transform", choices=["method_transform", "noop"])
    parser.add_argument("--no-repair-on-fail", action="store_true", help="Do not retry failed branch exploration with no-op branches")
    args = parser.parse_args()

    report, exit_code = run(args)
    report_path = Path(args.report_out).expanduser().resolve() if args.report_out else Path(report["case_dir"]) / "handoff_run_report.json"
    _write_json(report_path, report)
    report["report"] = str(report_path)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
