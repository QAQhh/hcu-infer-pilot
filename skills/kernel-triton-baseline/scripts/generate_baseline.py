#!/usr/bin/env python3
"""Generate conservative benchmark-compatible Triton baseline cases."""

from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
from typing import Any

AUTO_GENERATED_OPS = frozenset({
    "matmul",
    "reduction",
    "elementwise",
    "elementwise_copy",
    "elementwise_add",
    "elementwise_mul",
})

_PY_RESERVED_RENAMES = {
    "in": "inp",
    "lambda": "lambda_",
    "def": "def_",
}


def _py_name(name: str) -> str:
    return _PY_RESERVED_RENAMES.get(name, name)


def _read(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _copy_ref(ref_file: str, out_dir: Path) -> str:
    src = Path(ref_file)
    dst = out_dir / f"ref_original{src.suffix or '.txt'}"
    if src.resolve() != dst.resolve():
        shutil.copy2(src, dst)
    return dst.name


def _native_ref_adapter(analysis: dict, original_name: str, output_name: str) -> str:
    sig = analysis.get("signature_hint") or {}
    dims = analysis.get("dims") or {}
    output_name = _py_name(output_name)
    tensor_args = [_py_name(name) for name in (sig.get("tensor_args") or ["x"])]
    input_tensors = [name for name in tensor_args if name != output_name] or list(tensor_args)
    op_kind = analysis.get("classification", {}).get("op_kind", "elementwise_copy")
    language = (analysis.get("classification", {}).get("frameworks") or ["native"])[0]
    public = list(dict.fromkeys(tensor_args + [output_name] + list(dims)))
    if op_kind == "matmul" and len(input_tensors) >= 2:
        expr = f"torch.matmul({input_tensors[0]}, {input_tensors[1]})"
        atol, rtol = "1e-2", "1e-2"
    elif op_kind == "reduction" and input_tensors:
        expr = f"{input_tensors[0]}.sum()"
        atol, rtol = "1e-3", "1e-3"
    elif op_kind == "elementwise_add" and len(input_tensors) >= 2:
        expr = f"{input_tensors[0]} + {input_tensors[1]}"
        atol, rtol = "1e-4", "1e-4"
    elif op_kind == "elementwise_mul" and len(input_tensors) >= 2:
        expr = f"{input_tensors[0]} * {input_tensors[1]}"
        atol, rtol = "1e-4", "1e-4"
    else:
        expr = input_tensors[0]
        atol, rtol = "1e-4", "1e-4"
    return f'''from __future__ import annotations

import torch

# Generated from {language.upper()} source `{original_name}`.

atol = {atol}
rtol = {rtol}


def reference({", ".join(public)}):
    {output_name}.copy_(({expr}).reshape_as({output_name}))
'''


def _cuda_ref_adapter(analysis: dict, original_name: str, output_name: str) -> str:
    return _native_ref_adapter(analysis, original_name, output_name)


def _ref_adapter(analysis: dict, original_name: str, output_name: str) -> str:
    if not original_name.endswith(".py"):
        return _native_ref_adapter(analysis, original_name, output_name)
    chosen = analysis.get("chosen_reference") or {}
    sig = analysis.get("signature_hint") or {}
    dims = analysis.get("dims") or {}
    fn_name = chosen.get("name") or "reference"
    tensor_args = sig.get("tensor_args") or ["x"]
    dim_args = list(dims)
    public = list(dict.fromkeys(tensor_args + [output_name] + dim_args))
    call_args = ", ".join([a for a in tensor_args + dim_args if a in public])
    return f'''from __future__ import annotations

import importlib.util
from pathlib import Path

_ORIG_PATH = Path(__file__).with_name("{original_name}")
_SPEC = importlib.util.spec_from_file_location("_hygon_triton_ref_original", _ORIG_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"cannot import {{_ORIG_PATH}}")
_orig = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_orig)

atol = getattr(_orig, "atol", 1e-3)
rtol = getattr(_orig, "rtol", 1e-3)


def reference({", ".join(public)}):
    result = _orig.{fn_name}({call_args})
    if result is not None:
        {output_name}.copy_(result.reshape_as({output_name}))
'''


def _elementwise_kernel(analysis: dict, output_name: str = "out") -> str:
    sig = analysis.get("signature_hint") or {}
    output_name = _py_name(output_name)
    tensor_args = [_py_name(name) for name in (sig.get("tensor_args") or ["x"])]
    input_tensors = [name for name in tensor_args if name != output_name] or ["x"]
    first_tensor = input_tensors[0]
    dims = analysis.get("dims") or {}
    size_name = "N" if "N" in dims else (next(iter(dims), "N"))
    default_n = int(dims.get(size_name, 1048576))
    op_kind = analysis.get("classification", {}).get("op_kind", "elementwise_copy")
    if op_kind == "elementwise":
        op_kind = "elementwise_add" if len(input_tensors) >= 2 else "elementwise_copy"
    # Resolve dtype from inputs_schema or default to float32
    inputs_schema = analysis.get("inputs_schema") or []
    dtype_name = "float32"
    for entry in inputs_schema:
        if entry.get("name") in input_tensors:
            dtype_name = entry.get("dtype", "float32")
            break
    kernel_params = ", ".join(input_tensors + [output_name])
    setup_tensors = "\n".join(
        f'    {name} = torch.randn((N,), device="cuda", dtype=torch.{dtype_name})' for name in input_tensors
    )
    inputs_dict = ", ".join(
        [f'"{name}": {name}' for name in input_tensors]
        + [f'"{output_name}": {output_name}', '"N": N']
    )
    load_lines = "\n".join(
        f'    v{i} = tl.load({name} + offs, mask=mask, other=0.0)'
        for i, name in enumerate(input_tensors)
    )
    if op_kind == "elementwise_add" and len(input_tensors) >= 2:
        expr = "v0 + v1"
    elif op_kind == "elementwise_mul" and len(input_tensors) >= 2:
        expr = "v0 * v1"
    else:
        expr = "v0"
    run_args = ", ".join(input_tensors + [output_name, "N"])
    launch_args = ", ".join(input_tensors + [output_name, "N", "BLOCK_SIZE"])
    return f'''from __future__ import annotations

import torch
import triton
import triton.language as tl


DEFAULT_CONFIG = {{"BLOCK_SIZE": 128, "num_warps": 4, "num_stages": 1, "waves_per_eu": 1}}


@triton.jit
def _kernel({kernel_params}, N: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    offs = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = offs < N
{load_lines}
    tl.store({output_name} + offs, {expr}, mask=mask)


def _cfg(config):
    out = dict(DEFAULT_CONFIG)
    if config:
        out.update(config)
    return out


def setup(**kwargs):
    N = int(kwargs.get("{size_name}", {default_n}))
    seed = kwargs.get("seed", 42)
    torch.manual_seed(seed)
{setup_tensors}
    {output_name} = torch.empty_like({first_tensor})
    cfg = _cfg(kwargs.get("config"))
    return {{"inputs": {{{inputs_dict}}}, "outputs": ["{output_name}"], "kernel_kwargs": cfg, "active_config": cfg, "config_source": "fixed" if kwargs.get("config") else "baseline", "config_key": kwargs.get("config_key", ""), "config_hit": bool(kwargs.get("config"))}}


def run_kernel({run_args}, BLOCK_SIZE=128, num_warps=4, num_stages=1, waves_per_eu=1):
    grid = (triton.cdiv(N, BLOCK_SIZE),)
    _kernel[grid]({launch_args}, num_warps=num_warps, num_stages=num_stages, waves_per_eu=waves_per_eu)
'''


def _reduction_kernel(analysis: dict, output_name: str = "out") -> str:
    sig = analysis.get("signature_hint") or {}
    tensor_args = sig.get("tensor_args") or ["x"]
    output_name = _py_name(output_name)
    raw_inputs = [name for name in tensor_args if name != (sig.get("output_args") or [output_name])[0]]
    input_name = _py_name(raw_inputs[0] if raw_inputs else "x")
    dims = analysis.get("dims") or {}
    size_name = "N" if "N" in dims else next(iter(dims), "N")
    default_n = int(dims.get(size_name, 1048576))
    return f'''from __future__ import annotations

import torch
import triton
import triton.language as tl


DEFAULT_CONFIG = {{"BLOCK_SIZE": 256, "num_warps": 4, "num_stages": 1, "waves_per_eu": 1}}


@triton.jit
def _reduce_kernel({input_name}, {output_name}, N: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    offs = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = offs < N
    block_sum = tl.sum(tl.load({input_name} + offs, mask=mask, other=0.0))
    tl.atomic_add({output_name}, block_sum)


def _cfg(config):
    out = dict(DEFAULT_CONFIG)
    if config:
        out.update(config)
    return out


def setup(**kwargs):
    N = int(kwargs.get("{size_name}", {default_n}))
    seed = kwargs.get("seed", 42)
    torch.manual_seed(seed)
    {input_name} = torch.randn((N,), device="cuda", dtype=torch.float32)
    {output_name} = torch.zeros((1,), device="cuda", dtype=torch.float32)
    cfg = _cfg(kwargs.get("config"))
    return {{"inputs": {{"{input_name}": {input_name}, "{output_name}": {output_name}, "N": N}}, "outputs": ["{output_name}"], "kernel_kwargs": cfg, "active_config": cfg, "config_source": "fixed" if kwargs.get("config") else "baseline", "config_key": kwargs.get("config_key", ""), "config_hit": bool(kwargs.get("config"))}}


def run_kernel({input_name}, {output_name}, N, BLOCK_SIZE=256, num_warps=4, num_stages=1, waves_per_eu=1):
    grid = (triton.cdiv(N, BLOCK_SIZE),)
    _reduce_kernel[grid]({input_name}, {output_name}, N, BLOCK_SIZE, num_warps=num_warps, num_stages=num_stages, waves_per_eu=waves_per_eu)
'''


def _matmul_kernel(analysis: dict, output_name: str = "out") -> str:
    dims = analysis.get("dims") or {}
    default_m = int(dims.get("M", 1024))
    default_n = int(dims.get("N", 1024))
    default_k = int(dims.get("K", 1024))
    return f'''from __future__ import annotations

import torch
import triton
import triton.language as tl


DEFAULT_CONFIG = {{"BLOCK_M": 16, "BLOCK_N": 16, "BLOCK_K": 32, "num_warps": 1, "num_stages": 1, "waves_per_eu": 1}}


@triton.jit
def _matmul_kernel(A, B, C, M: tl.constexpr, N: tl.constexpr, K: tl.constexpr,
                   stride_am: tl.constexpr, stride_ak: tl.constexpr,
                   stride_bk: tl.constexpr, stride_bn: tl.constexpr,
                   stride_cm: tl.constexpr, stride_cn: tl.constexpr,
                   BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr):
    pid = tl.program_id(0)
    num_pid_m = tl.cdiv(M, BLOCK_M)
    num_pid_n = tl.cdiv(N, BLOCK_N)
    pid_m = pid % num_pid_m
    pid_n = pid // num_pid_m
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    a_ptrs = A + offs_m[:, None] * stride_am + offs_k[None, :] * stride_ak
    b_ptrs = B + offs_k[:, None] * stride_bk + offs_n[None, :] * stride_bn
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    for k in range(0, K, BLOCK_K):
        a = tl.load(a_ptrs, mask=(offs_m[:, None] < M) & (offs_k[None, :] + k < K), other=0.0)
        b = tl.load(b_ptrs, mask=(offs_k[:, None] + k < K) & (offs_n[None, :] < N), other=0.0)
        acc += tl.dot(a, b)
        a_ptrs += BLOCK_K * stride_ak
        b_ptrs += BLOCK_K * stride_bk
    c = C + offs_m[:, None] * stride_cm + offs_n[None, :] * stride_cn
    tl.store(c, acc, mask=(offs_m[:, None] < M) & (offs_n[None, :] < N))


def _cfg(config):
    out = dict(DEFAULT_CONFIG)
    if config:
        out.update(config)
    return out


def setup(**kwargs):
    M, N, K = int(kwargs.get("M", {default_m})), int(kwargs.get("N", {default_n})), int(kwargs.get("K", {default_k}))
    seed = kwargs.get("seed", 42)
    torch.manual_seed(seed)
    A = torch.randn((M, K), device="cuda", dtype=torch.float16)
    B = torch.randn((K, N), device="cuda", dtype=torch.float16)
    {output_name} = torch.empty((M, N), device="cuda", dtype=torch.float32)
    cfg = _cfg(kwargs.get("config"))
    return {{"inputs": {{"A": A, "B": B, "{output_name}": {output_name}, "M": M, "N": N, "K": K}}, "outputs": ["{output_name}"], "kernel_kwargs": cfg, "active_config": cfg, "config_source": "fixed" if kwargs.get("config") else "baseline", "config_key": kwargs.get("config_key", ""), "config_hit": bool(kwargs.get("config"))}}


def run_kernel(A, B, {output_name}, M, N, K, BLOCK_M=16, BLOCK_N=16, BLOCK_K=32, num_warps=1, num_stages=1, waves_per_eu=1):
    grid = (triton.cdiv(M, BLOCK_M) * triton.cdiv(N, BLOCK_N),)
    _matmul_kernel[grid](A, B, {output_name}, M, N, K, A.stride(0), A.stride(1), B.stride(0), B.stride(1), {output_name}.stride(0), {output_name}.stride(1), BLOCK_M, BLOCK_N, BLOCK_K, num_warps=num_warps, num_stages=num_stages, waves_per_eu=waves_per_eu)
'''


def _resolve_op_kind(analysis: dict, op: str) -> str:
    if op != "auto":
        return op
    return analysis.get("classification", {}).get("op_kind", "unknown")


def _inputs_schema(op_kind: str, tensor_args: list[str]) -> list[dict]:
    if op_kind == "matmul":
        names = tensor_args[:2] if len(tensor_args) >= 2 else ["A", "B"]
        return [
            {"name": names[0], "dtype": "float16", "shape_expr": ["M", "K"], "layout": "contiguous"},
            {"name": names[1], "dtype": "float16", "shape_expr": ["K", "N"], "layout": "contiguous"},
        ]
    return [{"name": name, "dtype": "float32", "shape_expr": ["N"], "layout": "contiguous"} for name in tensor_args]


def _resolve_output_name(analysis: dict, cli_name: str) -> str:
    outs = (analysis.get("signature_hint") or {}).get("output_args") or []
    return _py_name(outs[0] if outs else cli_name)


def generate(analysis_path: str, out_dir: str, op: str, output_name: str) -> dict:
    analysis = _read(analysis_path)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    original_name = _copy_ref(analysis["ref_file"], out)
    _write(out / "ref_analysis.json", json.dumps(analysis, indent=2, ensure_ascii=False) + "\n")
    dims = analysis.get("dims") or {}
    op_kind = _resolve_op_kind(analysis, op)
    output_name = _resolve_output_name(analysis, output_name)
    tensor_args = (analysis.get("signature_hint") or {}).get("tensor_args") or ["x"]
    input_tensors = [_py_name(name) for name in tensor_args if name != output_name] or ["x"]
    schema_inputs = tensor_args if op_kind == "matmul" else input_tensors
    unsupported = list(analysis.get("unsupported_assumptions") or [])
    if op_kind == "matmul":
        baseline_config = {"BLOCK_M": 16, "BLOCK_N": 16, "BLOCK_K": 32, "num_warps": 1, "num_stages": 1, "waves_per_eu": 1}
    elif op_kind == "reduction":
        baseline_config = {"BLOCK_SIZE": 256, "num_warps": 4, "num_stages": 1, "waves_per_eu": 1}
    else:
        baseline_config = {"BLOCK_SIZE": 128, "num_warps": 4, "num_stages": 1, "waves_per_eu": 1}
    manifest = {
        "case_dir": str(out.resolve()),
        "kernel": str((out / "kernel.py").resolve()),
        "ref": str((out / "ref.py").resolve()),
        "shape_hints": dims,
        "shape_overrides": {},
        "op_kind": op_kind,
        "target_arches": ["gfx936", "gfx938"],
        "inputs_schema": _inputs_schema(op_kind, schema_inputs),
        "outputs_schema": [{
            "name": output_name,
            "dtype": "float32",
            "shape_expr": ["M", "N"] if op_kind == "matmul" else (["1"] if op_kind == "reduction" else ["N"]),
            "layout": "contiguous",
        }],
        "tolerance": {"atol": 1e-3, "rtol": 1e-3},
        "baseline_config": baseline_config,
        "config_schema": {"keys": list(baseline_config), "fixed_for_profiling": True},
        "unsupported_assumptions": unsupported,
        "auto_generated": False,
    }
    if op_kind not in AUTO_GENERATED_OPS:
        unsupported.append(f"op_kind {op_kind!r} is not auto-generated; hand-author kernel.py and re-run validate_case.py")
        manifest["unsupported_assumptions"] = unsupported
        manifest["auto_generated"] = False
        _write(out / "ref.py", _ref_adapter(analysis, original_name, output_name))
        _write(out / "baseline_manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
        raise SystemExit(
            f"generate_baseline: op_kind={op_kind!r} requires agent-authored kernel.py. "
            f"Wrote ref.py and baseline_manifest.json under {out}; inspect unsupported_assumptions."
        )
    _write(out / "ref.py", _ref_adapter(analysis, original_name, output_name))
    if op_kind == "matmul":
        kernel = _matmul_kernel(analysis, output_name)
    elif op_kind == "reduction":
        kernel = _reduction_kernel(analysis, output_name)
    else:
        kernel = _elementwise_kernel(analysis, output_name)
    _write(out / "kernel.py", kernel)
    manifest["auto_generated"] = True
    _write(out / "baseline_manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--op", default="auto", choices=["auto", "elementwise", "elementwise_copy", "elementwise_add", "elementwise_mul", "reduction", "matmul", "unknown"])
    parser.add_argument("--output-name", default="out")
    args = parser.parse_args()
    print(json.dumps(generate(args.analysis, args.out_dir, args.op, args.output_name), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
