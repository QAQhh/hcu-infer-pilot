#!/usr/bin/env python3
"""Benchmark a Python/Triton operator module with optional correctness checks.

The module contract is:

  setup(**dims, seed=..., config=..., disable_autotune=..., target_arch=...)
      -> {"inputs": dict, "outputs": list, ...}
  run_kernel(**kwargs) -> None

setup may additionally return kernel_kwargs, reference_inputs, active_config,
config_source, config_key, and config_hit. These are recorded in bench.json so
profiling can prove it used a fixed config.

ref.py only needs Python-callable reference(**kwargs) for correctness. It may use
pure Python/PyTorch, Triton, HIPC, or another backend wrapped behind Python. By
default this benchmark skips reference timing so tuning/profile measure kernel.py
only; pass --bench-reference when reference latency or speedup_vs_reference is
required. Optional ref.py module attribute REF_BACKEND = "triton"|"pytorch"|"hipc"|...
is recorded in bench.json when present.
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import os
import sys
from pathlib import Path
from typing import Any

try:
    import torch
except ModuleNotFoundError:  # allow --help on hosts without PyTorch
    torch = None


def _write_json(path: str, payload: dict) -> None:
    if not path:
        return
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _load_module(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _jsonable_scalar(value: Any) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    try:
        import numpy as np  # type: ignore
        if isinstance(value, np.generic):
            return value.item()
    except Exception:
        pass
    return str(value)


def _triton_config_to_dict(config: Any) -> dict:
    if config is None:
        return {}
    if hasattr(config, "all_kwargs"):
        data = config.all_kwargs()
    elif hasattr(config, "kwargs"):
        data = dict(getattr(config, "kwargs") or {})
        for key in ("num_warps", "num_stages", "num_ctas", "maxnreg"):
            if hasattr(config, key):
                value = getattr(config, key)
                if value is not None:
                    data[key] = value
    elif isinstance(config, dict):
        data = config
    else:
        return {}
    return {str(k): _jsonable_scalar(v) for k, v in dict(data).items()}


def _collect_triton_autotune_winners(module: Any) -> list[dict]:
    winners = []
    for name, value in vars(module).items():
        best = getattr(value, "best_config", None)
        config = _triton_config_to_dict(best)
        if not config:
            continue
        winners.append({
            "name": name,
            "config": config,
            "repr": str(best),
        })
    return winners


def _merged_autotune_config(winners: list[dict]) -> tuple[dict, bool]:
    merged: dict = {}
    conflict = False
    for item in winners:
        config = item.get("config") or {}
        for key, value in config.items():
            if key in merged and merged[key] != value:
                conflict = True
            merged[key] = value
    return merged, conflict


def _clone_value(value: Any) -> Any:
    if isinstance(value, torch.Tensor):
        return value.clone()
    return copy.deepcopy(value)


def _load_config(path: str, key: str) -> tuple[dict | None, str, bool]:
    if not path:
        return None, "", False
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, list):
        if key:
            for item in data:
                if isinstance(item, dict) and item.get("config_key") == key:
                    return dict(item.get("config") or {}), key, True
            return None, key, False
        first = data[0] if data else {}
        if isinstance(first, dict) and "config" in first:
            return dict(first.get("config") or {}), str(first.get("config_key", "")), bool(data)
        return dict(first), "", bool(data)
    if isinstance(data, dict):
        if "config" in data:
            return dict(data.get("config") or {}), str(data.get("config_key", key)), True
        if key and key in data:
            item = data[key]
            if isinstance(item, dict) and "config" in item:
                return dict(item.get("config") or {}), key, True
            return dict(item), key, True
        return dict(data), key, True
    raise TypeError(f"unsupported config file format: {path}")


def _parse_config(args: argparse.Namespace) -> tuple[dict | None, str, bool, str]:
    if args.config_json:
        cfg = json.loads(args.config_json)
        if not isinstance(cfg, dict):
            raise TypeError("--config-json must decode to a JSON object")
        return cfg, args.config_key, True, "fixed"
    cfg, key, hit = _load_config(args.config_path, args.config_key)
    if cfg is not None:
        return cfg, key, hit, "registry" if hit else "fallback"
    return None, args.config_key, False, "none"


def _detect_arch(device_index: int | None = None) -> str:
    if torch.cuda.is_available():
        if device_index is None:
            device_index = torch.cuda.current_device()
        props = torch.cuda.get_device_properties(device_index)
        gcn = getattr(props, "gcnArchName", None)
        if gcn:
            return str(gcn).split(":", 1)[0]
    return "unknown"


def _setup_python(
    solution_file: str,
    dims: dict,
    seed: int,
    config: dict | None,
    config_key: str,
    config_hit: bool,
    config_source: str,
    disable_autotune: bool,
    target_arch: str,
) -> dict:
    module = _load_module(solution_file, "_hygon_triton_kernel")
    if not hasattr(module, "setup") or not hasattr(module, "run_kernel"):
        raise AttributeError(f"{solution_file} must define setup(**kwargs) and run_kernel(**kwargs)")

    prepared = module.setup(
        **dict(
            dims,
            seed=seed,
            config=config,
            config_key=config_key,
            disable_autotune=disable_autotune,
            target_arch=target_arch,
        )
    )
    if not isinstance(prepared, dict) or not isinstance(prepared.get("inputs"), dict):
        raise TypeError("setup() must return a dict containing {'inputs': dict, 'outputs': list}")
    if not isinstance(prepared.get("outputs"), (list, tuple)):
        raise TypeError("setup() must return {'outputs': list}")

    inputs = prepared["inputs"]
    outputs = list(prepared["outputs"])
    for name in outputs:
        if name not in inputs:
            raise ValueError(f"output {name!r} missing from setup()['inputs']")
        if isinstance(inputs[name], torch.Tensor):
            inputs[name].zero_()

    kernel_kwargs = dict(inputs)
    kernel_kwargs.update(prepared.get("kernel_kwargs") or {})
    reference_inputs = prepared.get("reference_inputs")
    if reference_inputs is None:
        reference_inputs = {k: _clone_value(v) for k, v in inputs.items() if k not in set(prepared.get("kernel_kwargs", {}))}
    else:
        reference_inputs = {k: _clone_value(v) for k, v in reference_inputs.items()}

    tensor_inputs = {k: v for k, v in inputs.items() if isinstance(v, torch.Tensor)}
    pristine_tensors = {k: v.clone() for k, v in tensor_inputs.items()}
    output_specs = [(name, str(inputs[name].dtype).replace("torch.", "")) for name in outputs]
    signature = []
    for name, value in inputs.items():
        if isinstance(value, torch.Tensor):
            signature.append({"name": name, "type": f"tensor[{str(value.dtype).replace('torch.', '')}]", "shape": list(value.shape), "is_const": name not in outputs})
        else:
            signature.append({"name": name, "type": type(value).__name__, "is_const": True})

    active_config = dict(prepared.get("active_config") or config or {})
    return {
        "backend": "triton_python",
        "signature": signature,
        "callable": lambda: module.run_kernel(**kernel_kwargs),
        "tensor_inputs": tensor_inputs,
        "reference_inputs": reference_inputs,
        "pristine_tensors": pristine_tensors,
        "output_specs": output_specs,
        "ptr_elems": sum(t.numel() for t in tensor_inputs.values()),
        "total_ptr_bytes": sum(t.numel() * t.element_size() for t in tensor_inputs.values()),
        "active_config": active_config,
        "config_source": prepared.get("config_source") or config_source,
        "config_key": prepared.get("config_key") or config_key,
        "config_hit": bool(prepared.get("config_hit", config_hit or bool(config))),
        "disable_autotune": disable_autotune,
        "autotune_winner_getter": lambda: _collect_triton_autotune_winners(module),
    }


def _reset_tensor_inputs(state: dict) -> None:
    for name, tensor in state["tensor_inputs"].items():
        snap = state["pristine_tensors"].get(name)
        if snap is not None:
            tensor.copy_(snap)


def _time_iterations(fn, warmup: int, repeat: int) -> list[float]:
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)
    times = []
    for _ in range(repeat):
        start.record()
        fn()
        end.record()
        torch.cuda.synchronize()
        times.append(float(start.elapsed_time(end)))
    return times


def _stats(times: list[float]) -> dict:
    ordered = sorted(times)
    return {
        "average_ms": sum(times) / len(times),
        "median_ms": ordered[len(ordered) // 2],
        "min_ms": min(times),
        "max_ms": max(times),
        "samples_ms": times,
    }


def _validate_outputs(kernel_tensors: dict, ref_tensors: dict, output_specs: list[tuple[str, str]], atol: float, rtol: float) -> bool:
    all_pass = True
    for name, ptype in output_specs:
        kt = kernel_tensors[name].float()
        rt = ref_tensors[name].float()
        ok = torch.allclose(kt, rt, atol=atol, rtol=rtol)
        all_pass = all_pass and ok
        max_diff = (kt - rt).abs().max().item()
        mean_diff = (kt - rt).abs().mean().item()
        print(f"[validate] {name} ({ptype}) {'PASS' if ok else 'FAIL'} max={max_diff:.6e} mean={mean_diff:.6e}")
    return all_pass


def _refresh_active_config_from_autotune(result: dict, state: dict) -> None:
    getter = state.get("autotune_winner_getter")
    if not callable(getter):
        return
    winners = getter()
    if winners:
        result["autotune_best_configs"] = winners
    if result.get("active_config"):
        return
    merged, conflict = _merged_autotune_config(winners)
    if not merged or conflict:
        if conflict:
            result["autotune_config_conflict"] = True
        return
    result["active_config"] = merged
    result["config_source"] = "triton_autotune_best_config"
    result["config_key"] = winners[0].get("name", result.get("config_key") or "autotune_best")
    result["config_hit"] = True


def run(args: argparse.Namespace, dims: dict) -> None:
    if torch is None:
        raise ModuleNotFoundError("torch is required to run the benchmark")
    torch.cuda.set_device(args.gpu)
    target_arch = args.target_arch or args.arch or _detect_arch(args.gpu)
    config, config_key, config_hit, config_source = _parse_config(args)
    has_ref = bool(args.ref)
    result = {
        "solution_file": os.path.abspath(args.solution_file),
        "backend": "triton_python",
        "ref_file": os.path.abspath(args.ref) if has_ref else "",
        "has_reference": has_ref,
        "dims": dims,
        "warmup": args.warmup,
        "repeat": args.repeat,
        "gpu_index": args.gpu,
        "gpu_name": torch.cuda.get_device_name(args.gpu),
        "arch": target_arch,
        "seed": args.seed,
        "active_config": config or {},
        "config_source": config_source,
        "config_key": config_key,
        "config_hit": config_hit,
        "disable_autotune": args.disable_autotune,
        "correctness": {"checked": has_ref, "passed": None, "atol": args.atol if has_ref else None, "rtol": args.rtol if has_ref else None},
        "kernel": None,
        "reference": None,
        "reference_timing_skipped": bool(args.skip_reference_bench),
        "speedup_vs_reference": None,
        "ref_backend": None,
        "error": None,
    }
    try:
        state = _setup_python(
            args.solution_file,
            dims,
            args.seed,
            config,
            config_key,
            config_hit,
            config_source,
            args.disable_autotune,
            target_arch,
        )
    except Exception as exc:  # noqa: BLE001
        result["error"] = {"code": "setup_failed", "stage": "setup", "message": str(exc)}
        if has_ref:
            result["correctness"]["passed"] = False
        _write_json(args.json_out, result)
        raise

    for key in ("signature", "ptr_elems", "total_ptr_bytes", "active_config", "config_source", "config_key", "config_hit", "disable_autotune"):
        result[key] = state.get(key)

    ref_fn = None
    if has_ref:
        ref_mod = _load_module(args.ref, "_hygon_triton_ref")
        if not hasattr(ref_mod, "reference"):
            raise AttributeError(f"{args.ref} must define reference(**kwargs)")
        ref_fn = ref_mod.reference
        result["ref_backend"] = getattr(ref_mod, "REF_BACKEND", None)
        atol = float(getattr(ref_mod, "atol", args.atol))
        rtol = float(getattr(ref_mod, "rtol", args.rtol))
        ref_inputs = {name: _clone_value(value) for name, value in state["reference_inputs"].items()}
        _reset_tensor_inputs(state)
        state["callable"]()
        torch.cuda.synchronize()
        _refresh_active_config_from_autotune(result, state)
        ref_fn(**ref_inputs)
        torch.cuda.synchronize()
        kernel_outputs = {name: state["tensor_inputs"][name] for name, _ in state["output_specs"]}
        ref_outputs = {name: ref_inputs[name] for name, _ in state["output_specs"]}
        passed = _validate_outputs(kernel_outputs, ref_outputs, state["output_specs"], atol, rtol)
        result["correctness"].update({"passed": passed, "atol": atol, "rtol": rtol, "output_tensor_count": len(state["output_specs"])})
        if not passed:
            _write_json(args.json_out, result)
            sys.exit(1)

    if has_ref and ref_fn is not None and not args.skip_reference_bench:
        ref_bench_inputs = {name: _clone_value(value) for name, value in state["reference_inputs"].items()}
        result["reference"] = _stats(_time_iterations(lambda: ref_fn(**ref_bench_inputs), args.warmup, args.repeat))
        if result["reference"]["average_ms"] > 0:
            result["reference"]["bandwidth_gbps_rough"] = state["total_ptr_bytes"] / (result["reference"]["average_ms"] / 1000) / 1e9

    _reset_tensor_inputs(state)
    result["kernel"] = _stats(_time_iterations(state["callable"], args.warmup, args.repeat))
    _refresh_active_config_from_autotune(result, state)
    if result["kernel"]["average_ms"] > 0:
        result["kernel"]["bandwidth_gbps_rough"] = state["total_ptr_bytes"] / (result["kernel"]["average_ms"] / 1000) / 1e9
    if result.get("reference") and result["reference"]["average_ms"] > 0:
        result["speedup_vs_reference"] = result["reference"]["average_ms"] / result["kernel"]["average_ms"]

    print(json.dumps({
        "backend": "triton_python",
        "gpu": result["gpu_name"],
        "arch": target_arch,
        "correct": result["correctness"]["passed"],
        "kernel_ms": result["kernel"]["average_ms"],
        "active_config": result["active_config"],
        "config_source": result["config_source"],
        "json_out": args.json_out,
    }, indent=2))
    _write_json(args.json_out, result)


def main() -> None:
    parser = argparse.ArgumentParser(description="Hygon Triton Python operator benchmark")
    parser.add_argument("solution_file")
    parser.add_argument("--backend", default="auto", choices=["auto", "python", "triton"])
    parser.add_argument("--ref", default="")
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--repeat", type=int, default=20)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--arch", default="")
    parser.add_argument("--target-arch", default="")
    parser.add_argument("--atol", type=float, default=1e-4)
    parser.add_argument("--rtol", type=float, default=1e-3)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--json-out", default="")
    parser.add_argument("--config-json", default="")
    parser.add_argument("--config-path", default="")
    parser.add_argument("--config-key", default="")
    parser.add_argument("--disable-autotune", action="store_true")
    parser.add_argument("--bench-reference", dest="skip_reference_bench", action="store_false",
                        help="Also time ref.reference() and report speedup_vs_reference")
    parser.add_argument("--skip-reference-bench", dest="skip_reference_bench", action="store_true",
                        help="Skip ref.reference() timing; correctness is still checked")
    parser.set_defaults(skip_reference_bench=True)
    args, unknown = parser.parse_known_args()
    dims = {}
    for item in unknown:
        if item.startswith("--") and "=" in item:
            key, val = item[2:].split("=", 1)
            try:
                dims[key] = int(val)
            except ValueError:
                try:
                    dims[key] = float(val)
                except ValueError:
                    dims[key] = val
        else:
            print(f"Warning: ignoring unknown arg `{item}`", file=sys.stderr)
    run(args, dims)


if __name__ == "__main__":
    main()
