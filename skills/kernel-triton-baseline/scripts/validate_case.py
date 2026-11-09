#!/usr/bin/env python3
"""Validate a generated Hygon Triton baseline case."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", required=True)
    parser.add_argument("--optimizer-skill", default="")
    args = parser.parse_args()
    case = Path(args.case_dir)
    manifest = json.loads((case / "baseline_manifest.json").read_text(encoding="utf-8"))
    optimizer = Path(args.optimizer_skill) if args.optimizer_skill else Path(__file__).resolve().parents[2] / "kernel-triton-optimize"
    dims = manifest.get("shape_overrides") or {}
    preflight = optimizer / "scripts" / "preflight.py"
    benchmark = optimizer / "scripts" / "benchmark.py"
    rc1 = subprocess.call([sys.executable, str(preflight), "--baseline", str(case / "kernel.py"), "--ref", str(case / "ref.py"), "--dims", json.dumps(dims)])
    if rc1 != 0:
        sys.exit(rc1)
    cmd = [
        sys.executable,
        str(benchmark),
        str(case / "kernel.py"),
        "--ref",
        str(case / "ref.py"),
        "--json-out",
        str(case / "baseline_bench.json"),
        "--disable-autotune",
    ]
    cmd.extend([f"--{k}={v}" for k, v in dims.items()])
    sys.exit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
