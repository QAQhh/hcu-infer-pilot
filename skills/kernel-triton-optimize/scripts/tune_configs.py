#!/usr/bin/env python3
"""Fixed-config tuning sweep for Hygon Triton Python kernels."""

from __future__ import annotations

import argparse
import datetime as _dt
import itertools
import json
import os
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_BENCHMARK = SCRIPT_DIR / "benchmark.py"

_DEFAULT_MATMUL_CANDIDATES: list[dict] = [
    {"BLOCK_M": 16, "BLOCK_N": 16, "BLOCK_K": 32, "num_warps": 1, "num_stages": 1},
    {"BLOCK_M": 32, "BLOCK_N": 32, "BLOCK_K": 32, "num_warps": 2, "num_stages": 1},
    {"BLOCK_M": 64, "BLOCK_N": 64, "BLOCK_K": 32, "num_warps": 4, "num_stages": 2},
    {"BLOCK_M": 64, "BLOCK_N": 128, "BLOCK_K": 32, "num_warps": 4, "num_stages": 2},
    {"BLOCK_M": 128, "BLOCK_N": 64, "BLOCK_K": 32, "num_warps": 4, "num_stages": 2},
    # aiter MoE: MI300X-DEFAULT small/medium + top small-M (see aiter/ops/triton/configs/moe/)
    {"BLOCK_M": 64, "BLOCK_N": 64, "BLOCK_K": 64, "num_warps": 8, "num_stages": 2},
    {"BLOCK_M": 128, "BLOCK_N": 128, "BLOCK_K": 128, "num_warps": 8, "num_stages": 2},
    {"BLOCK_M": 16, "BLOCK_N": 128, "BLOCK_K": 128, "num_warps": 4, "num_stages": 1},
]


def _read(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: str | Path, payload) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _append_timeline_event(iter_dir: Path, event: dict) -> str:
    path = iter_dir / "attempt_timeline.json"
    try:
        events = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else []
    except Exception:
        events = []
    if not isinstance(events, list):
        events = [events]
    event.setdefault("timestamp", _dt.datetime.now().isoformat(timespec="seconds"))
    event.setdefault("sequence", len(events) + 1)
    events.append(event)
    _write_json(path, events)
    return str(path)


def _dims_argv(dims: dict) -> list[str]:
    return [f"--{k}={v}" for k, v in dims.items()]


def _unique_configs(configs: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for cfg in configs:
        clean = {str(k): int(v) if isinstance(v, bool | int | float) else v for k, v in dict(cfg).items()}
        key = json.dumps(clean, sort_keys=True, separators=(",", ":"))
        if key not in seen:
            seen.add(key)
            out.append(clean)
    return out


def _default_candidates(op_kind: str, search_level: str) -> list[dict]:
    if op_kind == "memory":
        quick = [
            {"BLOCK_SIZE": 64, "num_warps": 1, "num_stages": 1},
            {"BLOCK_SIZE": 128, "num_warps": 2, "num_stages": 1},
            {"BLOCK_SIZE": 256, "num_warps": 4, "num_stages": 1},
            {"BLOCK_SIZE": 512, "num_warps": 4, "num_stages": 1},
            {"BLOCK_SIZE": 1024, "num_warps": 4, "num_stages": 1},
        ]
        if search_level == "quick":
            return quick
        blocks = [64, 128, 256, 512, 1024, 2048]
        warps = [1, 2, 4, 8]
        stages = [1, 2]
        return _unique_configs(quick + [
            {"BLOCK_SIZE": b, "num_warps": w, "num_stages": s}
            for b in blocks
            for w in warps
            for s in stages
        ])
    if op_kind == "matmul":
        if search_level == "quick":
            return list(_DEFAULT_MATMUL_CANDIDATES)
        ms = [16, 32, 64, 128]
        ns = [16, 32, 64, 128]
        ks = [32, 64, 128]
        warps = [2, 4, 8]
        stages = [1, 2]
        return _unique_configs(list(_DEFAULT_MATMUL_CANDIDATES) + [
            {"BLOCK_M": m, "BLOCK_N": n, "BLOCK_K": k, "num_warps": w, "num_stages": s}
            for m in ms
            for n in ns
            for k in ks
            for w in warps
            for s in stages
        ])
    return _default_candidates("memory", search_level)


def _neighbor_values(key: str, value: int, search_level: str) -> list[int]:
    if key == "num_warps":
        vals = [1, 2, 4, 8]
    elif key == "num_stages":
        vals = [1, 2]
    elif key in {"waves_per_eu", "kpack"}:
        vals = [1, 2, 4, 8] if key == "waves_per_eu" else [1, 2]
    elif key == "matrix_instr_nonkdim":
        vals = [0, 16, 32]
    elif key.startswith("BLOCK") or key.endswith("_BLOCK") or key.endswith("_SIZE"):
        common = [16, 32, 64, 128, 256, 512, 1024, 2048]
        vals = common if search_level == "broad" else common + [4096]
        vals += [max(1, value // 2), value, value * 2]
    else:
        vals = [value]
    if key == "matrix_instr_nonkdim":
        return sorted({int(v) for v in vals if int(v) >= 0})
    return sorted({int(v) for v in vals if int(v) > 0})


def _neighbor_candidates(state: dict, search_level: str) -> list[dict]:
    base = state.get("best_config")
    if not isinstance(base, dict) or not base:
        return []
    numeric = {
        str(k): int(v)
        for k, v in base.items()
        if isinstance(v, bool | int | float)
    }
    if not numeric:
        return []

    out = [dict(numeric)]
    keys = list(numeric)
    for key in keys:
        for val in _neighbor_values(key, numeric[key], search_level):
            cfg = dict(numeric)
            cfg[key] = val
            out.append(cfg)

    if search_level == "deep":
        block_keys = [k for k in keys if k.startswith("BLOCK") or k.endswith("_SIZE")]
        control_keys = [k for k in keys if k in {"num_warps", "num_stages", "waves_per_eu"}]
        for bk in block_keys:
            for ck in control_keys:
                for bv in _neighbor_values(bk, numeric[bk], search_level):
                    for cv in _neighbor_values(ck, numeric[ck], search_level):
                        cfg = dict(numeric)
                        cfg[bk] = bv
                        cfg[ck] = cv
                        out.append(cfg)
    return _unique_configs(out)


def _default_max_configs(search_level: str) -> int:
    if search_level == "quick":
        return 8
    if search_level == "broad":
        return 64
    return 96


def _load_candidates(path: str, op_kind: str, max_configs: int, search_level: str, state: dict) -> list[dict]:
    if path:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if isinstance(data, dict) and "configs" in data:
            data = data["configs"]
        if not isinstance(data, list):
            raise TypeError("candidate config file must be a list or {'configs': list}")
        configs = [dict(item.get("config", item)) for item in data if isinstance(item, dict)]
    else:
        configs = _neighbor_candidates(state, search_level) + _default_candidates(op_kind, search_level)
    return _unique_configs(configs)[:max_configs]


def _config_key(arch: str, op_kind: str, dims: dict, idx: int) -> str:
    dim_part = ":".join(f"{k}{v}" for k, v in sorted(dims.items()))
    return f"{arch}:{op_kind}:{dim_part}:cfg{idx:03d}"


def _change_vs_previous_best(previous_ms, ms) -> dict:
    if previous_ms is None or ms is None or previous_ms <= 0 or ms <= 0:
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
    if previous_ms is None or ms is None or previous_ms <= 0 or ms <= 0:
        return False
    threshold = 1.0 - (float(noise_threshold_pct or 0.0) / 100.0)
    return ms < previous_ms * threshold


def _upsert_path_history(items, iteration: int, path: str) -> list[dict]:
    out = [item for item in (items or []) if not (isinstance(item, dict) and item.get("iter") == iteration)]
    out.append({"iter": int(iteration), "path": os.path.abspath(path)})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--iter", type=int, default=1)
    parser.add_argument("--which", default="best_input", choices=["best_input", "kernel"])
    parser.add_argument("--benchmark", default=str(DEFAULT_BENCHMARK))
    parser.add_argument("--candidates", default="")
    parser.add_argument("--op-kind", default="auto", choices=["auto", "memory", "matmul"])
    parser.add_argument("--search-level", default="quick", choices=["quick", "broad", "deep"])
    parser.add_argument("--max-configs", type=int, default=None)
    parser.add_argument("--warmup", type=int, default=5)
    parser.add_argument("--repeat", type=int, default=10)
    parser.add_argument("--accept-threshold-pct", type=float, default=2.0)
    parser.add_argument("--final-tune", action="store_true",
                        help="Mark this sweep as the pre-finalization tuning iteration.")
    parser.add_argument("--promote-if-better", action="store_true",
                        help="When the best passing config beats state.best_metric_ms beyond the noise threshold, write it to state.best_config.")
    args = parser.parse_args()

    state = _read(args.state)
    run_dir = state["run_dir"]
    iter_dir = Path(run_dir) / f"iterv{args.iter}"
    tune_dir = iter_dir / "tune"
    tune_dir.mkdir(parents=True, exist_ok=True)
    dims = state.get("dims", {})
    arch = state.get("env", {}).get("primary_gfx_arch") or state.get("target_arch") or "unknown"
    op_kind = args.op_kind
    if op_kind == "auto":
        op_kind = "matmul" if {"M", "N", "K"}.issubset(dims) else "memory"
    kernel = state["best_file"] if args.which == "best_input" else next((str(iter_dir / f"kernel{ext}") for ext in (".py", ".hip") if (iter_dir / f"kernel{ext}").is_file()), state["best_file"])
    max_configs = args.max_configs if args.max_configs is not None else _default_max_configs(args.search_level)
    configs = _load_candidates(args.candidates, op_kind, max_configs, args.search_level, state)
    results = []
    for idx, cfg in enumerate(configs, start=1):
        key = _config_key(arch, op_kind, dims, idx)
        out_dir = tune_dir / f"config_{idx:03d}"
        out_dir.mkdir(parents=True, exist_ok=True)
        json_out = out_dir / "bench.json"
        cmd = [
            sys.executable, args.benchmark, kernel,
            "--ref", state["ref_file"],
            "--warmup", str(args.warmup),
            "--repeat", str(args.repeat),
            "--json-out", str(json_out),
            "--config-json", json.dumps(cfg, separators=(",", ":")),
            "--config-key", key,
            "--target-arch", arch,
            "--disable-autotune",
        ] + _dims_argv(dims)
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        (out_dir / "bench.stdout.txt").write_text(proc.stdout or "", encoding="utf-8")
        (out_dir / "bench.stderr.txt").write_text(proc.stderr or "", encoding="utf-8")
        bench = _read(json_out) if json_out.is_file() else {}
        passed = bool(bench.get("correctness", {}).get("passed", False))
        ms = (bench.get("kernel") or {}).get("average_ms")
        results.append({"config_key": key, "config": cfg, "returncode": proc.returncode, "passed": passed, "ms": ms, "bench_json": str(json_out)})

    valid = [r for r in results if r["passed"] and r["ms"] is not None]
    valid.sort(key=lambda r: r["ms"])
    baseline_ms = state.get("best_metric_ms")
    threshold = 1.0 - (state.get("noise_threshold_pct", 2.0) / 100.0)
    accepted = []
    for r in valid[: min(3, len(valid))]:
        speedup = (baseline_ms / r["ms"]) if baseline_ms and r["ms"] else None
        accepted.append({
            "config_key": r["config_key"],
            "arch": arch,
            "op_kind": op_kind,
            "shape_guard": dims,
            "dtype": "unknown",
            "layout": "contiguous",
            "config": r["config"],
            "evidence": {
                "bench_json": r["bench_json"],
                "median_ms": r["ms"],
                "correctness": r["passed"],
                "speedup_vs_state_best": speedup,
                "noise_threshold_pct": args.accept_threshold_pct,
            },
        })
    tune_results = {
        "iter": args.iter,
        "kernel": kernel,
        "op_kind": op_kind,
        "search_level": args.search_level,
        "max_configs": max_configs,
        "baseline_ms": baseline_ms,
        "best": valid[0] if valid else None,
        "results": [
            {
                **r,
                **_change_vs_previous_best(baseline_ms, r.get("ms")),
            }
            for r in results
        ],
    }
    best = tune_results["best"]
    best_improved = bool(
        best
        and baseline_ms is not None
        and best.get("ms") is not None
        and best["ms"] < baseline_ms * threshold
    )
    event_results = []
    best_key = best.get("config_key") if best else None
    for r in tune_results["results"]:
        item = dict(r)
        if not item.get("passed"):
            item["status"] = "failure"
            item["outcome"] = "correctness_or_benchmark_failed"
        elif item.get("config_key") == best_key and best_improved:
            item["status"] = "success"
            item["outcome"] = "best_config_candidate"
        elif item.get("config_key") == best_key:
            item["status"] = "failure"
            item["outcome"] = "best_config_but_not_faster_than_previous_best"
        elif _is_improvement(baseline_ms, item.get("ms"), state.get("noise_threshold_pct")):
            item["status"] = "success"
            item["outcome"] = "improved_but_not_selected"
        else:
            item["status"] = "failure"
            item["outcome"] = "valid_but_not_selected"
        event_results.append(item)
    tune_results["attempt_timeline"] = _append_timeline_event(iter_dir, {
        "kind": "config_tune",
        "iter": args.iter,
        "catalog_reference": "references/triton_optimization_catalog.md",
        "op_kind": op_kind,
        "search_level": args.search_level,
        "max_configs": max_configs,
        "kernel": kernel,
        "previous_best_ms": baseline_ms,
        "noise_threshold_pct": state.get("noise_threshold_pct"),
        "status": "success" if best_improved else "failure",
        "outcome": "accepted_faster_config" if best_improved else "no_config_promoted",
        "champion_config_key": best_key,
        "champion_ms": best.get("ms") if best else None,
        **_change_vs_previous_best(baseline_ms, best.get("ms") if best else None),
        "configs": event_results,
    })
    _write_json(iter_dir / "tune_results.json", tune_results)
    _write_json(iter_dir / "accepted_configs.json", accepted)
    lines = ["# Config Acceptance", ""]
    for item in accepted:
        ev = item["evidence"]
        lines.append(f"- `{item['config_key']}`: {ev['median_ms']:.6f} ms, speedup_vs_state_best={ev.get('speedup_vs_state_best')}")
    if not accepted:
        lines.append("- No passing configs.")
    (iter_dir / "config_acceptance.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    if args.final_tune or args.promote_if_better:
        state["tune_history"] = _upsert_path_history(
            state.get("tune_history", []),
            args.iter,
            str(iter_dir / "tune_results.json"),
        )
        state["accepted_configs"] = accepted
        final_tune = {
            "completed": bool(args.final_tune),
            "iter": int(args.iter),
            "path": os.path.abspath(iter_dir / "tune_results.json"),
            "accepted_configs": os.path.abspath(iter_dir / "accepted_configs.json"),
            "search_level": args.search_level,
            "max_configs": max_configs,
            "best_config_key": best_key,
            "best_ms": best.get("ms") if best else None,
            "previous_best_ms": baseline_ms,
            "promoted": False,
            "outcome": "no_config_promoted",
        }
        if best_improved and args.promote_if_better and best:
            promoted_config_path = iter_dir / "config.json"
            _write_json(promoted_config_path, best["config"])
            state["best_config"] = best["config"]
            state["best_config_path"] = os.path.abspath(promoted_config_path)
            state["best_metric_ms"] = best["ms"]
            final_tune["promoted"] = True
            final_tune["promoted_config"] = os.path.abspath(promoted_config_path)
            final_tune["outcome"] = "promoted_final_config"
        elif best_improved and not args.promote_if_better:
            final_tune["outcome"] = "better_config_found_not_promoted"
        state["final_tune"] = final_tune
        _write_json(args.state, state)
    print(json.dumps({"accepted": accepted, "best": tune_results["best"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
