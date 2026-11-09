#!/usr/bin/env python3
"""Unified HCU profiler entrypoint.

Preference order:
  1. xcu / XCompute when available.
  2. hipprof when xcu is missing or fails.

Both backends write iterv{i}/hcu_top.json for roofline.py.  The fallback is
explicitly recorded so summary.md can warn users to install xcu instead of
silently presenting hipprof raw-counter evidence as precise utilization.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
XCU_CANDIDATES = (
    "/opt/xcompute-4.4.4/XCompute/bin/xcu",
    "/opt/xcompute/XCompute/bin/xcu",
)


def _find_xcu() -> str | None:
    env = os.environ.get("XCU_BIN_PATH", "")
    if env and os.path.isfile(env):
        return env
    for candidate in XCU_CANDIDATES:
        if os.path.isfile(candidate):
            return candidate
    return shutil.which("xcu")


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    print(f"[run] {' '.join(cmd)}", file=sys.stderr)
    return subprocess.run(cmd, text=True)


def _state_run_dir(state_path: str) -> str:
    with open(state_path, "r", encoding="utf-8") as f:
        state = json.load(f)
    return state["run_dir"]


def _annotate_top(iter_dir: str, payload: dict) -> None:
    path = Path(iter_dir) / "hcu_top.json"
    if not path.is_file():
        return
    try:
        top = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return
    top.update(payload)
    path.write_text(json.dumps(top, indent=2, ensure_ascii=False), encoding="utf-8")


def _write_degraded_top(iter_dir: str, payload: dict) -> None:
    path = Path(iter_dir) / "hcu_top.json"
    top = {
        "degraded": True,
        "compute": [],
        "memory": [],
        "latency": [],
    }
    top.update(payload)
    path.write_text(json.dumps(top, indent=2, ensure_ascii=False), encoding="utf-8")


def _filter_passthrough_for_hipprof(argv: list[str]) -> list[str]:
    """Drop xcu-only passthrough flags before invoking hipprof fallback."""
    flags_without_values = {"--no-kernel-filter", "--quick", "--no-auto-select"}
    flags_with_values = {"--sections", "--timeout"}
    out: list[str] = []
    skip_next = False
    for item in argv:
        if skip_next:
            skip_next = False
            continue
        if item in flags_without_values:
            continue
        if item in flags_with_values:
            skip_next = True
            continue
        if any(item.startswith(flag + "=") for flag in flags_with_values):
            continue
        out.append(item)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--state", required=True)
    p.add_argument("--iter", required=True, type=int)
    p.add_argument("--which", required=True, choices=["best_input", "kernel"])
    p.add_argument("--profiler", default="auto", choices=["auto", "xcu", "hipprof"])
    p.add_argument("--xcu-bin", default="")
    p.add_argument("--hipprof-bin", default="")
    args, passthrough = p.parse_known_args()

    run_dir = _state_run_dir(args.state)
    iter_dir = os.path.join(run_dir, f"iterv{args.iter}")
    os.makedirs(iter_dir, exist_ok=True)

    xcu_available = bool(args.xcu_bin or _find_xcu())
    tried: list[dict] = []
    install_hint = (
        "xcu is not available on this HCU runtime host. Install the latest internal "
        "xprofiler, hsa-aqlprofile, and XCompute packages, then ensure xcu is on PATH "
        "or set XCU_BIN_PATH=/opt/xcompute/XCompute/bin/xcu."
    )

    if args.profiler in {"auto", "xcu"} and xcu_available:
        cmd = [
            sys.executable, str(SCRIPT_DIR / "profile_xcu.py"),
            "--state", args.state,
            "--iter", str(args.iter),
            "--which", args.which,
        ]
        if args.xcu_bin:
            cmd.extend(["--xcu-bin", args.xcu_bin])
        cmd.extend(passthrough)
        result = _run(cmd)
        tried.append({"profiler": "xcu", "returncode": result.returncode})
        if result.returncode == 0 or args.profiler == "xcu":
            _annotate_top(iter_dir, {
                "profiler_selection": {
                    "selected": "xcu",
                    "preference": "xcu>hipprof",
                    "attempts": tried,
                }
            })
            sys.exit(result.returncode)

    if args.profiler == "xcu" and not xcu_available:
        _write_degraded_top(iter_dir, {
            "reason": "xcu not available",
            "profiler": "xcu",
            "install_hint": install_hint,
            "profiler_selection": {
                "selected": None,
                "preference": "xcu>hipprof",
                "attempts": tried,
                "install_hint": install_hint,
            }
        })
        print(json.dumps({"error": "xcu not available", "install_hint": install_hint}, indent=2), file=sys.stderr)
        sys.exit(2)

    if args.profiler in {"auto", "hipprof"}:
        cmd = [
            sys.executable, str(SCRIPT_DIR / "profile_hipprof.py"),
            "--state", args.state,
            "--iter", str(args.iter),
            "--which", args.which,
        ]
        if args.hipprof_bin:
            cmd.extend(["--hipprof-bin", args.hipprof_bin])
        cmd.extend(_filter_passthrough_for_hipprof(passthrough))
        result = _run(cmd)
        tried.append({"profiler": "hipprof", "returncode": result.returncode})
        payload = {
            "profiler_selection": {
                "selected": "hipprof",
                "preference": "xcu>hipprof",
                "attempts": tried,
                "xcu_available": xcu_available,
            }
        }
        if not xcu_available:
            payload["install_hint"] = install_hint
            payload["profiler_selection"]["install_hint"] = install_hint
        else:
            payload["profiler_selection"]["xcu_fallback_reason"] = "xcu attempt failed; hipprof fallback used"
        _annotate_top(iter_dir, payload)
        sys.exit(result.returncode)

    print(json.dumps({"error": "no profiler attempted", "attempts": tried}, indent=2), file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
