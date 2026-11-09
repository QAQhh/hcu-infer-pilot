#!/usr/bin/env python3
"""Branch-and-Select: compile and benchmark K candidate kernels in parallel.

All K branches share the same method combination (from methods.json) but
differ in hyperparameters (tile size, num_stages, num_warps, etc.).

The agent generates K kernels under iterv{i}/branches/b{1..K}/kernel.<ext>.

This script:
  1. Compiles all K kernels (can be parallelized)
  2. Benchmarks each kernel with validation
  3. Selects champion = fastest valid kernel
  4. Copies champion to iterv{i}/kernel.<ext>
  5. Returns non-champions as frontier candidates in state

Writes iterv{i}/branch_results.json.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


_BUNDLED_BENCHMARK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "benchmark.py")
KERNEL_EXTS = (".hip", ".cu", ".cpp", ".cc", ".cxx", ".py")


def _load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: str, obj) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def _append_timeline_event(iter_dir: str, event: dict) -> str:
    path = os.path.join(iter_dir, "attempt_timeline.json")
    try:
        events = _load_json(path) if os.path.isfile(path) else []
    except Exception:
        events = []
    if not isinstance(events, list):
        events = [events]
    event.setdefault("timestamp", _dt.datetime.now().isoformat(timespec="seconds"))
    event.setdefault("sequence", len(events) + 1)
    events.append(event)
    _write_json(path, events)
    return path


def _dims_argv(dims: dict) -> list[str]:
    return [f"--{k}={v}" for k, v in dims.items()]


def _ptr_size_argv(ptr_size: int) -> list[str]:
    return ["--ptr-size", str(ptr_size)] if ptr_size and ptr_size > 0 else []


def _config_argv(args: argparse.Namespace | None = None, branch_dir: str = "") -> list[str]:
    out: list[str] = []
    if args is not None:
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
    branch_config = os.path.join(branch_dir, "config.json") if branch_dir else ""
    if branch_config and os.path.isfile(branch_config) and "--config-path" not in out:
        out.extend(["--config-path", branch_config, "--disable-autotune"])
    return out


def _change_vs_previous_best(previous_ms, ms) -> dict:
    if previous_ms is None or ms is None:
        return {
            "speedup_vs_previous_best": None,
            "change_vs_previous_best_pct": None,
            "delta_vs_previous_best_ms": None,
        }
    if previous_ms <= 0 or ms <= 0:
        return {
            "speedup_vs_previous_best": None,
            "change_vs_previous_best_pct": None,
            "delta_vs_previous_best_ms": None,
        }
    return {
        "speedup_vs_previous_best": previous_ms / ms,
        "change_vs_previous_best_pct": ((previous_ms - ms) / previous_ms) * 100.0,
        "delta_vs_previous_best_ms": previous_ms - ms,
    }


def _is_improvement(previous_ms, ms, noise_threshold_pct) -> bool:
    if previous_ms is None or ms is None:
        return False
    if previous_ms <= 0 or ms <= 0:
        return False
    threshold = 1.0 - (float(noise_threshold_pct or 0.0) / 100.0)
    return ms < previous_ms * threshold


def _load_methods(iter_dir: str) -> list[dict]:
    methods_path = os.path.join(iter_dir, "methods.json")
    if not os.path.isfile(methods_path):
        return []
    try:
        methods = _load_json(methods_path).get("methods", [])
    except Exception:
        return []
    if not isinstance(methods, list):
        return []
    return [
        {
            "id": item.get("id") or item.get("name"),
            "name": item.get("name") or item.get("id"),
            "axis": item.get("axis"),
        }
        for item in methods if isinstance(item, dict)
    ]


def _branch_timeline_event(
    *,
    state: dict,
    iter_dir: str,
    iteration: int,
    results: list[dict],
    champion: dict | None,
    champion_improved: bool,
) -> dict:
    previous_best_ms = state.get("best_metric_ms")
    methods = _load_methods(iter_dir)
    branches = []
    champion_index = champion.get("branch_index") if champion else None
    for r in results:
        branch = dict(r)
        branch.update(_change_vs_previous_best(previous_best_ms, r.get("ms")))
        if not r.get("passed"):
            branch["status"] = "failure"
            branch["outcome"] = "correctness_or_benchmark_failed"
        elif r.get("branch_index") == champion_index and champion_improved:
            branch["status"] = "success"
            branch["outcome"] = "selected_and_promoted"
        elif r.get("branch_index") == champion_index:
            branch["status"] = "failure"
            branch["outcome"] = "selected_but_not_faster_than_previous_best"
        elif _is_improvement(previous_best_ms, r.get("ms"), state.get("noise_threshold_pct")):
            branch["status"] = "success"
            branch["outcome"] = "improved_but_not_selected"
        else:
            branch["status"] = "failure"
            branch["outcome"] = "valid_but_not_selected"
        branches.append(branch)

    event = {
        "kind": "branch_explore",
        "iter": iteration,
        "catalog_reference": "references/triton_optimization_catalog.md",
        "methods": methods,
        "previous_best_ms": previous_best_ms,
        "noise_threshold_pct": state.get("noise_threshold_pct"),
        "status": "success" if champion_improved else "failure",
        "outcome": "promoted_global_best" if champion_improved else "no_branch_promoted",
        "champion_branch": champion_index,
        "champion_ms": champion.get("ms") if champion else None,
        "branches": branches,
    }
    if champion:
        event.update(_change_vs_previous_best(previous_best_ms, champion.get("ms")))
    return event


def _bench_kernel(
    benchmark_py: str,
    kernel_path: str,
    ref_path: str,
    dims: dict,
    ptr_size: int,
    json_out: str,
    warmup: int = 10,
    repeat: int = 20,
    extra_args: list[str] | None = None,
) -> dict:
    """Run the benchmark wrapper on a kernel. Returns parsed result or error dict."""
    cmd = [
        sys.executable, benchmark_py, kernel_path,
        "--ref", ref_path,
        "--warmup", str(warmup),
        "--repeat", str(repeat),
        "--json-out", json_out,
    ] + _ptr_size_argv(ptr_size) + (extra_args or []) + _dims_argv(dims)

    Path(json_out).parent.mkdir(parents=True, exist_ok=True)
    stderr_out = json_out.replace(".json", ".stderr.txt")

    try:
        r = subprocess.run(
            cmd, capture_output=True, text=True,
            encoding="utf-8", errors="ignore",
        )
    except OSError as e:
        return {"error": str(e), "passed": False}

    # Save stderr for debugging
    with open(stderr_out, "w", encoding="utf-8") as f:
        f.write("---STDOUT---\n")
        f.write(r.stdout or "")
        f.write("\n---STDERR---\n")
        f.write(r.stderr or "")

    if os.path.isfile(json_out):
        return _load_json(json_out)

    return {
        "error": "no_json_output",
        "stderr": (r.stderr or "")[-2000:],
        "passed": False,
    }


def run(state_path: str, iteration: int, benchmark_py: str = None,
        warmup: int = 10, repeat: int = 20, args: argparse.Namespace | None = None) -> dict:
    state = _load_json(state_path)
    run_dir = state["run_dir"]
    iter_dir = os.path.join(run_dir, f"iterv{iteration}")
    bench_py = benchmark_py or _BUNDLED_BENCHMARK
    branches_dir = os.path.join(iter_dir, "branches")
    ref_file = state["ref_file"]
    dims = state.get("dims", {})
    ptr_size = state.get("ptr_size", 0)
    num_branches = state.get("branches", 4)
    previous_best_ms = state.get("best_metric_ms")
    threshold = 1.0 - (state.get("noise_threshold_pct", 2.0) / 100.0)

    # Discover branches
    branch_dirs = []
    for i in range(1, num_branches + 1):
        bd = os.path.join(branches_dir, f"b{i}")
        if os.path.isdir(bd):
            # Check if there's a kernel file
            kernel = None
            for ext in KERNEL_EXTS:
                candidate = os.path.join(bd, f"kernel{ext}")
                if os.path.isfile(candidate):
                    kernel = candidate
                    break
            if kernel:
                branch_dirs.append({"index": i, "dir": bd, "kernel": kernel})

    if not branch_dirs:
        # Fallback: check if there's a single kernel directly in iter_dir
        for ext in KERNEL_EXTS:
            candidate = os.path.join(iter_dir, f"kernel{ext}")
            if os.path.isfile(candidate):
                branch_dirs.append({
                    "index": 0, "dir": iter_dir, "kernel": candidate,
                })
                break

    if not branch_dirs:
        sys.exit(f"No branch kernels found under {branches_dir}")

    print(f"[branch_explore] Found {len(branch_dirs)} branches", file=sys.stderr)

    # Benchmark all branches
    results = []
    for branch in branch_dirs:
        idx = branch["index"]
        kernel = branch["kernel"]
        json_out = os.path.join(branch["dir"], "bench.json")

        print(f"[branch {idx}] Benchmarking {os.path.basename(kernel)}...",
              file=sys.stderr)

        bench_result = _bench_kernel(
            bench_py, kernel, ref_file, dims, ptr_size, json_out, warmup, repeat,
            extra_args=_config_argv(args, branch["dir"]),
        )

        passed = bool(bench_result.get("correctness", {}).get("passed", False))
        ms = None
        if bench_result.get("kernel"):
            ms = bench_result["kernel"].get("average_ms")

        results.append({
            "branch_index": idx,
            "kernel": kernel,
            "passed": passed,
            "ms": ms,
            "bench_json": json_out,
            "error": bench_result.get("error"),
        })

        status = "PASS" if passed else "FAIL"
        ms_str = f"{ms:.4f} ms" if ms else "N/A"
        print(f"[branch {idx}] {status}  {ms_str}", file=sys.stderr)

    # Select champion: fastest valid branch
    valid_results = [r for r in results if r["passed"] and r["ms"] is not None]

    if not valid_results:
        event = _branch_timeline_event(
            state=state,
            iter_dir=iter_dir,
            iteration=iteration,
            results=results,
            champion=None,
            champion_improved=False,
        )
        timeline_path = _append_timeline_event(iter_dir, event)
        output = {
            "iter": iteration,
            "status": "all_branches_failed",
            "branches": results,
            "champion": None,
            "attempt_timeline": timeline_path,
        }
        _write_json(os.path.join(iter_dir, "branch_results.json"), output)
        print(json.dumps(output, indent=2))
        sys.exit(2)

    champion = min(valid_results, key=lambda r: r["ms"])
    champion_improved = (
        previous_best_ms is None
        or (champion.get("ms") is not None and champion["ms"] < previous_best_ms * threshold)
    )

    # Copy champion kernel to iterv{i}/kernel.<ext>
    champ_kernel = champion["kernel"]
    ext = os.path.splitext(champ_kernel)[1]
    dest = os.path.join(iter_dir, f"kernel{ext}")
    if os.path.abspath(champ_kernel) != os.path.abspath(dest):
        shutil.copy2(champ_kernel, dest)

    # Also copy champion bench.json to iter_dir
    champ_bench = os.path.join(os.path.dirname(champ_kernel), "bench.json")
    dest_bench = os.path.join(iter_dir, "bench.json")
    if os.path.isfile(champ_bench) and os.path.abspath(champ_bench) != os.path.abspath(dest_bench):
        shutil.copy2(champ_bench, dest_bench)

    champ_config = os.path.join(os.path.dirname(champ_kernel), "config.json")
    dest_config = os.path.join(iter_dir, "config.json")
    if os.path.isfile(champ_config) and os.path.abspath(champ_config) != os.path.abspath(dest_config):
        shutil.copy2(champ_config, dest_config)

    # Build frontier from non-champion valid results
    frontier_entries = []
    for r in valid_results:
        if r["branch_index"] != champion["branch_index"]:
            frontier_entries.append({
                "iter": iteration,
                "branch_index": r["branch_index"],
                "kernel": r["kernel"],
                "ms": r["ms"],
                "delta_from_champion": round(r["ms"] - champion["ms"], 4),
            })

    output = {
        "iter": iteration,
        "status": "champion_selected",
        "champion": {
            "branch_index": champion["branch_index"],
            "kernel": dest,
            "ms": champion["ms"],
            "config": dest_config if os.path.isfile(dest_config) else None,
            "promoted_candidate": champion_improved,
            **_change_vs_previous_best(previous_best_ms, champion["ms"]),
        },
        "branches": [
            {
                **r,
                **_change_vs_previous_best(previous_best_ms, r.get("ms")),
            }
            for r in results
        ],
        "frontier": frontier_entries,
        "total_branches": len(branch_dirs),
        "valid_branches": len(valid_results),
    }
    event = _branch_timeline_event(
        state=state,
        iter_dir=iter_dir,
        iteration=iteration,
        results=output["branches"],
        champion=output["champion"],
        champion_improved=champion_improved,
    )
    output["attempt_timeline"] = _append_timeline_event(iter_dir, event)

    _write_json(os.path.join(iter_dir, "branch_results.json"), output)
    print(json.dumps(output, indent=2))
    return output


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--state", required=True)
    p.add_argument("--iter", type=int, required=True)
    p.add_argument("--benchmark", default=None)
    p.add_argument("--warmup", type=int, default=10)
    p.add_argument("--repeat", type=int, default=20)
    p.add_argument("--config-json", default="")
    p.add_argument("--config-path", default="")
    p.add_argument("--config-key", default="")
    p.add_argument("--target-arch", default="")
    p.add_argument("--disable-autotune", action="store_true")
    args = p.parse_args()
    run(args.state, args.iter, args.benchmark, args.warmup, args.repeat, args)


if __name__ == "__main__":
    main()
