#!/usr/bin/env python3
"""Run the bundled benchmark for a given iteration (or baseline seed).

Default benchmark.py mode is correctness via ref.py and kernel timing only.

Subcommands:
  seed-baseline   Benchmark the baseline kernel and capture initial timing.
  benchmark       Benchmark iterv{i}/kernel.<ext>.

Both write JSON under the appropriate directory. `benchmark` additionally
captures stderr so the agent can inspect it on validation failure.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


_BUNDLED_BENCHMARK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "benchmark.py")
KERNEL_EXTS = (".hip", ".cu", ".cpp", ".cc", ".cxx", ".py")


def _read(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _dims_argv(dims: dict) -> list[str]:
    return [f"--{k}={v}" for k, v in dims.items()]


def _ptr_size_argv(ptr_size: int) -> list[str]:
    return ["--ptr-size", str(ptr_size)] if ptr_size and ptr_size > 0 else []


def _config_argv(args: argparse.Namespace) -> list[str]:
    out: list[str] = []
    for attr, flag in (
        ("config_json", "--config-json"),
        ("config_path", "--config-path"),
        ("config_key", "--config-key"),
        ("target_arch", "--target-arch"),
    ):
        value = getattr(args, attr, "")
        if value:
            out.extend([flag, str(value)])
    if getattr(args, "disable_autotune", False):
        out.append("--disable-autotune")
    return out


def _run_bench(
    *,
    benchmark_py: str,
    solution: str,
    ref: str,
    dims: dict,
    ptr_size: int,
    json_out: str,
    stderr_out: str,
    warmup: int,
    repeat: int,
    extra_args: list[str] | None = None,
) -> int:
    cmd = [
        sys.executable, benchmark_py, solution,
        "--ref", ref,
        "--warmup", str(warmup),
        "--repeat", str(repeat),
        "--json-out", json_out,
    ] + _ptr_size_argv(ptr_size) + (extra_args or []) + _dims_argv(dims)
    print(f"[bench] {' '.join(cmd)}", file=sys.stderr)

    Path(json_out).parent.mkdir(parents=True, exist_ok=True)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    except OSError as e:
        with open(stderr_out, "w", encoding="utf-8") as f:
            f.write(f"Failed to exec benchmark: {e}\n")
        return -1

    with open(stderr_out, "w", encoding="utf-8") as f:
        f.write("---STDOUT---\n")
        f.write(r.stdout or "")
        f.write("\n---STDERR---\n")
        f.write(r.stderr or "")

    # benchmark.py exits 1 on validation failure but still writes json-out
    # (we rely on the correctness.passed field)
    if not os.path.isfile(json_out):
        # Catastrophic — write a minimal JSON for downstream consumers
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump({
                "correctness": {"passed": False, "checked": True},
                "kernel": None,
                "reference": None,
                "error": {
                    "code": "benchmark_crashed",
                    "stage": "subprocess",
                    "message": (r.stderr or "")[-2000:],
                },
            }, f, indent=2)
    return r.returncode


def cmd_seed_baseline(args: argparse.Namespace) -> None:
    state = _read(args.state)
    run_dir = state["run_dir"]
    out_dir = os.path.join(run_dir, "baseline")
    os.makedirs(out_dir, exist_ok=True)
    json_out = os.path.join(out_dir, "bench.json")
    stderr_out = os.path.join(out_dir, "bench.stderr.txt")

    _run_bench(
        benchmark_py=os.path.abspath(args.benchmark),
        solution=state["baseline_file"],
        ref=state["ref_file"],
        dims=state.get("dims", {}),
        ptr_size=state.get("ptr_size", 0),
        json_out=json_out,
        stderr_out=stderr_out,
        warmup=args.warmup,
        repeat=args.repeat,
        extra_args=_config_argv(args),
    )

    # Push baseline ms into state via state.py CLI (keep one place that writes state)
    # We call the sibling script so concurrent locking semantics live in one file.
    sibling = os.path.join(os.path.dirname(__file__), "state.py")
    rc = subprocess.call([
        sys.executable, sibling, "set-baseline-metric",
        "--state", args.state, "--bench", json_out,
    ])
    sys.exit(rc)


def cmd_benchmark(args: argparse.Namespace) -> None:
    state = _read(args.state)
    run_dir = state["run_dir"]
    iter_dir = os.path.join(run_dir, f"iterv{args.iter}")
    candidates = [os.path.join(iter_dir, f"kernel{ext}") for ext in KERNEL_EXTS]
    kernel = next((c for c in candidates if os.path.isfile(c)), None)
    if not kernel:
        sys.exit(f"No iterv{args.iter}/kernel.(hip|cu|cpp|cc|cxx|py) found.")

    json_out = os.path.join(iter_dir, "bench.json")
    stderr_out = os.path.join(iter_dir, "bench.stderr.txt")
    _run_bench(
        benchmark_py=os.path.abspath(args.benchmark),
        solution=kernel,
        ref=state["ref_file"],
        dims=state.get("dims", {}),
        ptr_size=state.get("ptr_size", 0),
        json_out=json_out,
        stderr_out=stderr_out,
        warmup=args.warmup,
        repeat=args.repeat,
        extra_args=_config_argv(args),
    )
    # Return the result summary on stdout for the orchestrator to consume
    res = _read(json_out)
    summary = {
        "iter": args.iter,
        "kernel": kernel,
        "passed": bool(res.get("correctness", {}).get("passed", False)),
        "ms": (res.get("kernel") or {}).get("average_ms"),
        "ref_ms": (res.get("reference") or {}).get("average_ms"),
        "speedup_vs_ref": res.get("speedup_vs_reference"),
        "error": res.get("error"),
        "bench_json": json_out,
        "stderr_log": stderr_out,
    }
    print(json.dumps(summary, indent=2))


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("seed-baseline")
    ps.add_argument("--state", required=True)
    ps.add_argument("--benchmark", default=_BUNDLED_BENCHMARK,
                    help="Path to benchmark.py (default: bundled; skips reference timing by default)")
    ps.add_argument("--warmup", type=int, default=10)
    ps.add_argument("--repeat", type=int, default=20)
    ps.add_argument("--config-json", default="")
    ps.add_argument("--config-path", default="")
    ps.add_argument("--config-key", default="")
    ps.add_argument("--target-arch", default="")
    ps.add_argument("--disable-autotune", action="store_true")
    ps.set_defaults(func=cmd_seed_baseline)

    pb = sub.add_parser("benchmark")
    pb.add_argument("--state", required=True)
    pb.add_argument("--iter", type=int, required=True)
    pb.add_argument("--benchmark", default=_BUNDLED_BENCHMARK,
                    help="Path to benchmark.py (default: bundled; skips reference timing by default)")
    pb.add_argument("--warmup", type=int, default=10)
    pb.add_argument("--repeat", type=int, default=20)
    pb.add_argument("--config-json", default="")
    pb.add_argument("--config-path", default="")
    pb.add_argument("--config-key", default="")
    pb.add_argument("--target-arch", default="")
    pb.add_argument("--disable-autotune", action="store_true")
    pb.set_defaults(func=cmd_benchmark)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
