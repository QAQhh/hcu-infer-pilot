#!/usr/bin/env python3
"""Run the automatic kernel optimizer loop end to end.

The loop wires together:

    open-iter -> auto_kernel_optimize -> close-iter -> next iteration -> finalize

It assumes `orchestrate.py setup` has already created a run directory with
state.json. `setup` already profiles iteration 1, so this driver only opens an
iteration when roofline/hcu_top are missing.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_BENCHMARK = SCRIPT_DIR / "benchmark.py"


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _run(cmd: list[str | Path], *, dry_run: bool) -> dict[str, Any]:
    item: dict[str, Any] = {
        "cmd": [str(part) for part in cmd],
        "cmd_text": " ".join(str(part) for part in cmd),
    }
    if dry_run:
        item["status"] = "planned"
        return item
    proc = subprocess.run(cmd, text=True, capture_output=True, encoding="utf-8", errors="ignore")
    item.update(
        {
            "status": "ok" if proc.returncode == 0 else "failed",
            "returncode": proc.returncode,
            "stdout_tail": (proc.stdout or "")[-8000:],
            "stderr_tail": (proc.stderr or "")[-8000:],
        }
    )
    return item


def _extract_json_object(text: str) -> dict[str, Any]:
    if not text:
        return {}
    decoder = json.JSONDecoder()
    for idx, ch in enumerate(text):
        if ch != "{":
            continue
        try:
            obj, _ = decoder.raw_decode(text[idx:])
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            return obj
    return {}


def _iter_ready(run_dir: Path, iteration: int) -> bool:
    iter_dir = run_dir / f"iterv{iteration}"
    return (iter_dir / "roofline.json").is_file() and (iter_dir / "hcu_top.json").is_file()


def _is_near_peak(run_dir: Path, iteration: int) -> bool:
    roofline_path = run_dir / f"iterv{iteration}" / "roofline.json"
    if not roofline_path.is_file():
        return False
    return bool(_read_json(roofline_path).get("near_peak", False))


def _iteration_closed(run_dir: Path, iteration: int) -> bool:
    iter_dir = run_dir / f"iterv{iteration}"
    return (iter_dir / "branch_results.json").is_file() and (iter_dir / "bench.json").is_file()


def _auto_prepare_cmd(args: argparse.Namespace, run_dir: Path, iteration: int, benchmark: Path, branch_override: int, *, branch_mode: str) -> list[str | Path]:
    cmd: list[str | Path] = [
        sys.executable,
        SCRIPT_DIR / "auto_kernel_optimize.py",
        "--run-dir",
        run_dir,
        "--iter",
        str(iteration),
        "--branches",
        str(branch_override),
        "--selection-policy",
        args.selection_policy,
        "--branch-mode",
        branch_mode,
        "--warmup",
        str(args.warmup),
        "--repeat",
        str(args.repeat),
        "--retries",
        str(args.retries),
        "--prepare-only",
    ]
    if args.no_noop_fallback and branch_mode != "noop":
        cmd.append("--no-noop-fallback")
    if args.allow_ineffective:
        cmd.append("--allow-ineffective")
    return cmd


def _close_iter_cmd(args: argparse.Namespace, run_dir: Path, iteration: int, benchmark: Path) -> list[str | Path]:
    return [
        sys.executable,
        SCRIPT_DIR / "orchestrate.py",
        "close-iter",
        "--run-dir",
        run_dir,
        "--iter",
        str(iteration),
        "--benchmark",
        benchmark,
        "--warmup",
        str(args.warmup),
        "--repeat",
        str(args.repeat),
        "--retries",
        str(args.retries),
    ]


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    run_dir = Path(args.run_dir).expanduser().resolve()
    state_path = run_dir / "state.json"
    if not state_path.is_file():
        raise SystemExit(f"state.json not found: {state_path}")

    state = _read_json(state_path)
    total = int(state.get("iterations_total", 1) or 1)
    start_iter = int(args.start_iter)
    max_iters = int(args.max_iters or total)
    stop_iter = min(total, start_iter + max_iters - 1)
    benchmark = Path(args.benchmark).expanduser().resolve()
    branch_override = int(args.branches or state.get("branches", 1) or 1)

    report: dict[str, Any] = {
        "status": "started",
        "run_dir": str(run_dir),
        "state": str(state_path),
        "start_iter": start_iter,
        "stop_iter": stop_iter,
        "dry_run": bool(args.dry_run),
        "iterations": [],
        "steps": [],
    }

    exit_code = 0
    last_iter = start_iter - 1
    for iteration in range(start_iter, stop_iter + 1):
        iter_record: dict[str, Any] = {"iter": iteration, "steps": []}
        report["iterations"].append(iter_record)
        last_iter = iteration

        if not _iter_ready(run_dir, iteration):
            open_cmd: list[str | Path] = [
                sys.executable,
                SCRIPT_DIR / "orchestrate.py",
                "open-iter",
                "--run-dir",
                run_dir,
                "--iter",
                str(iteration),
                "--benchmark",
                benchmark,
            ]
            step = {"name": "open_iter", **_run(open_cmd, dry_run=args.dry_run)}
            iter_record["steps"].append(step)
            if not args.dry_run and step.get("returncode", 0) != 0:
                iter_record["status"] = "open_iter_failed"
                report["status"] = "failed"
                return report, int(step.get("returncode", 1))
        else:
            iter_record["steps"].append({"name": "open_iter", "status": "skipped", "reason": "roofline and hcu_top already exist"})

        if not args.dry_run and _is_near_peak(run_dir, iteration):
            iter_record["status"] = "near_peak_stop"
            report["status"] = "near_peak_stop"
            break

        auto_cmd = _auto_prepare_cmd(args, run_dir, iteration, benchmark, branch_override, branch_mode=args.branch_mode)
        step = {"name": "auto_kernel_optimize", **_run(auto_cmd, dry_run=args.dry_run)}
        iter_record["steps"].append(step)
        if not args.dry_run and step.get("returncode", 0) != 0:
            iter_record["status"] = "auto_kernel_optimize_failed"
            report["status"] = "failed"
            return report, int(step.get("returncode", 1))

        close_cmd = _close_iter_cmd(args, run_dir, iteration, benchmark)
        if args.prepare_only:
            iter_record["status"] = "prepared"
            continue
        if _iteration_closed(run_dir, iteration) and not args.force_close:
            iter_record["steps"].append({"name": "close_iter", "status": "skipped", "reason": "iteration already closed"})
        else:
            step = {"name": "close_iter", **_run(close_cmd, dry_run=args.dry_run)}
            iter_record["steps"].append(step)
            if not args.dry_run and step.get("returncode", 0) != 0:
                if args.repair_on_fail and int(step.get("returncode", 1)) == 2 and args.branch_mode != "noop":
                    repair_classify_cmd: list[str | Path] = [
                        sys.executable,
                        SCRIPT_DIR / "repair_branches.py",
                        "--state",
                        state_path,
                        "--iter",
                        str(iteration),
                        "--branches",
                        str(branch_override),
                        "--emit-noop-retry",
                    ]
                    repair_classify = {"name": "repair_classify_and_emit", **_run(repair_classify_cmd, dry_run=False)}
                    iter_record["steps"].append(repair_classify)
                    repair_prepare = {"name": "repair_prepare_noop", **_run(_auto_prepare_cmd(args, run_dir, iteration, benchmark, branch_override, branch_mode="noop"), dry_run=False)}
                    iter_record["steps"].append(repair_prepare)
                    if repair_prepare.get("returncode", 0) == 0:
                        repair_close = {"name": "repair_close_iter", **_run(_close_iter_cmd(args, run_dir, iteration, benchmark), dry_run=False)}
                        iter_record["steps"].append(repair_close)
                        if repair_close.get("returncode", 0) == 0:
                            iter_record["status"] = "closed_after_noop_repair"
                            continue
                iter_record["status"] = "close_iter_failed"
                report["status"] = "failed"
                return report, int(step.get("returncode", 1))
            close_summary = _extract_json_object(str(step.get("stdout_tail") or ""))
            iter_record["close_summary"] = close_summary
            if close_summary.get("early_stop"):
                iter_record["status"] = "early_stop_after_close"
                report["status"] = "early_stop"
                break
        iter_record["status"] = "closed" if not args.dry_run else "planned"

    if args.finalize and not args.prepare_only:
        finalize_cmd: list[str | Path] = [
            sys.executable,
            SCRIPT_DIR / "orchestrate.py",
            "finalize",
            "--run-dir",
            run_dir,
        ]
        step = {"name": "finalize", **_run(finalize_cmd, dry_run=args.dry_run)}
        report["steps"].append(step)
        if not args.dry_run and step.get("returncode", 0) != 0:
            report["status"] = "finalize_failed"
            return report, int(step.get("returncode", 1))

    if report.get("status") == "started":
        report["status"] = "prepared" if args.prepare_only else "completed" if not args.dry_run else "planned"
    report["last_iter"] = last_iter
    state = _read_json(state_path) if state_path.is_file() and not args.dry_run else state
    report["best_metric_ms"] = state.get("best_metric_ms")
    report["best_file"] = state.get("best_file")
    return report, exit_code


def main() -> None:
    parser = argparse.ArgumentParser(description="Run automatic kernel optimizer loop")
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--start-iter", type=int, default=1)
    parser.add_argument("--max-iters", type=int, default=0, help="0 means up to state.iterations_total")
    parser.add_argument("--benchmark", default=str(DEFAULT_BENCHMARK))
    parser.add_argument("--branches", type=int, default=0, help="0 means use state.branches")
    parser.add_argument("--warmup", type=int, default=2)
    parser.add_argument("--repeat", type=int, default=5)
    parser.add_argument("--retries", type=int, default=0)
    parser.add_argument("--selection-policy", default="evidence", choices=["evidence", "priority"])
    parser.add_argument("--branch-mode", default="method_transform", choices=["method_transform", "noop"])
    parser.add_argument("--no-noop-fallback", action="store_true")
    parser.add_argument("--allow-ineffective", action="store_true")
    parser.add_argument("--repair-on-fail", action="store_true", default=True, help="If branch exploration fails, retry once with no-op branches")
    parser.add_argument("--no-repair-on-fail", dest="repair_on_fail", action="store_false")
    parser.add_argument("--prepare-only", action="store_true", help="Stop after generating methods and branches each iteration")
    parser.add_argument("--finalize", action="store_true")
    parser.add_argument("--force-close", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report-out", default="")
    args = parser.parse_args()

    report, exit_code = run(args)
    out_path = Path(args.report_out).expanduser().resolve() if args.report_out else Path(args.run_dir).expanduser().resolve() / "auto_loop_report.json"
    _write_json(out_path, report)
    report["report"] = str(out_path)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
