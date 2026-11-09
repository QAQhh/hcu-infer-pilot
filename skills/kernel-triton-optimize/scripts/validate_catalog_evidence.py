#!/usr/bin/env python3
"""Validate TTGIR/ISA evidence claims from triton_optimization_catalog.md.

Runs on the selected HCU runtime target. For each method, compiles a minimal kernel and checks
that the claimed TTGIR/ISA patterns actually appear in the output.

Usage:
  python validate_catalog_evidence.py [--out-dir DIR]

Outputs:
  evidence_validation_results.json — per-method pass/fail with matched patterns
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import torch
import triton
import triton.language as tl

# ---------------------------------------------------------------------------
# Test kernels — one per evidence claim
# ---------------------------------------------------------------------------

# P1: triton.dot_mmac_shape — tt.dot, #ttg.dot_op<, #ttg.amd_mfma<
@triton.jit
def matmul_kernel(
    A, B, C, M, N, K,
    stride_am, stride_ak, stride_bk, stride_bn, stride_cm, stride_cn,
    BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr,
):
    pid = tl.program_id(0)
    num_pid_m = tl.cdiv(M, BLOCK_M)
    pid_m = pid % num_pid_m
    pid_n = pid // num_pid_m
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    a_ptrs = A + offs_m[:, None] * stride_am + offs_k[None, :] * stride_ak
    b_ptrs = B + offs_k[:, None] * stride_bk + offs_n[None, :] * stride_bn
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    for k in range(0, tl.cdiv(K, BLOCK_K)):
        a = tl.load(a_ptrs, mask=offs_m[:, None] < M, other=0.0)
        b = tl.load(b_ptrs, mask=offs_n[None, :] < N, other=0.0)
        acc += tl.dot(a, b)
        a_ptrs += BLOCK_K * stride_ak
        b_ptrs += BLOCK_K * stride_bk
    c_ptrs = C + offs_m[:, None] * stride_cm + offs_n[None, :] * stride_cn
    tl.store(c_ptrs, acc, mask=(offs_m[:, None] < M) & (offs_n[None, :] < N))


# P3: triton.num_stages_pipeline — ttg.async_wait, ttg.async_commit_group
@triton.jit
def matmul_pipelined_kernel(
    A, B, C, M, N, K,
    stride_am, stride_ak, stride_bk, stride_bn, stride_cm, stride_cn,
    BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr,
):
    pid = tl.program_id(0)
    num_pid_m = tl.cdiv(M, BLOCK_M)
    pid_m = pid % num_pid_m
    pid_n = pid // num_pid_m
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    a_ptrs = A + offs_m[:, None] * stride_am + offs_k[None, :] * stride_ak
    b_ptrs = B + offs_k[:, None] * stride_bk + offs_n[None, :] * stride_bn
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    for k in tl.range(0, tl.cdiv(K, BLOCK_K), num_stages=3):
        a = tl.load(a_ptrs, mask=offs_m[:, None] < M, other=0.0)
        b = tl.load(b_ptrs, mask=offs_n[None, :] < N, other=0.0)
        acc += tl.dot(a, b)
        a_ptrs += BLOCK_K * stride_ak
        b_ptrs += BLOCK_K * stride_bk
    c_ptrs = C + offs_m[:, None] * stride_cm + offs_n[None, :] * stride_cn
    tl.store(c_ptrs, acc, mask=(offs_m[:, None] < M) & (offs_n[None, :] < N))


# P2 Memory: triton.mask_simplification — mask removal via constexpr
@triton.heuristics({"EVEN_N": lambda args: args["N"] % args["BLOCK_SIZE"] == 0})
@triton.jit
def elementwise_mask_removed_kernel(
    X, Y, N,
    BLOCK_SIZE: tl.constexpr,
    EVEN_N: tl.constexpr,
):
    pid = tl.program_id(0)
    offs = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    if EVEN_N:
        x = tl.load(X + offs)
    else:
        x = tl.load(X + offs, mask=offs < N)
    y = x + 1.0
    if EVEN_N:
        tl.store(Y + offs, y)
    else:
        tl.store(Y + offs, y, mask=offs < N)


# Elementwise with mask (for comparison)
@triton.jit
def elementwise_with_mask_kernel(X, Y, N, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    offs = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = offs < N
    x = tl.load(X + offs, mask=mask)
    y = x + 1.0
    tl.store(Y + offs, y, mask=mask)


# triton.ilp_unroll — tl.static_range
@triton.jit
def unrolled_kernel(X, Y, N, BLOCK_SIZE: tl.constexpr, UNROLL_FACTOR: tl.constexpr):
    pid = tl.program_id(0)
    offs = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = offs < N
    x = tl.load(X + offs, mask=mask)
    acc = x
    for i in tl.static_range(UNROLL_FACTOR):
        acc = acc + x
    tl.store(Y + offs, acc, mask=mask)


# triton.barrier_scope_reduction — ttg.local_barrier
@triton.jit
def barrier_kernel(X, Y, N, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    offs = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = offs < N
    x = tl.load(X + offs, mask=mask)
    tl.debug_barrier()
    tl.store(Y + offs, x, mask=mask)


# ---------------------------------------------------------------------------
# Cache extraction helpers
# ---------------------------------------------------------------------------

def _get_triton_cache_dir() -> Path:
    cache_dir = os.environ.get("TRITON_CACHE_DIR", "")
    if cache_dir:
        return Path(cache_dir)
    return Path.home() / ".triton" / "cache"


def _clear_triton_cache():
    """Remove all entries from Triton cache so each kernel gets a fresh entry."""
    cache_dir = _get_triton_cache_dir()
    if cache_dir.is_dir():
        import shutil
        for entry in cache_dir.iterdir():
            if entry.is_dir():
                shutil.rmtree(entry, ignore_errors=True)


def _find_latest_cache_entry(kernel_name: str) -> Path | None:
    cache_dir = _get_triton_cache_dir()
    if not cache_dir.is_dir():
        return None
    for entry in sorted(cache_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
        # Check multiple TTGIR naming conventions:
        # Upstream: __triton__.ttgir
        # HCU fork: kernel.ttgir or <name>.ttgir
        for ttgir_name in ["__triton__.ttgir", "kernel.ttgir"]:
            if (entry / ttgir_name).is_file():
                return entry
        # Also check for any .ttgir file
        for f in entry.iterdir():
            if f.suffix == ".ttgir":
                return entry
    return None


def _extract_ttgir(cache_entry: Path) -> str | None:
    for ttgir_name in ["__triton__.ttgir", "kernel.ttgir"]:
        ttgir_path = cache_entry / ttgir_name
        if ttgir_path.is_file():
            return ttgir_path.read_text(encoding="utf-8", errors="ignore")
    for f in cache_entry.iterdir():
        if f.suffix == ".ttgir":
            return f.read_text(encoding="utf-8", errors="ignore")
    return None


def _extract_hsaco(cache_entry: Path) -> Path | None:
    for f in cache_entry.iterdir():
        if f.suffix == ".hsaco" or f.name.endswith(".hsaco"):
            return f
    return None


def _run_dccobjdump(hsaco_path: Path) -> str | None:
    try:
        result = subprocess.run(
            ["dccobjdump", "-d", str(hsaco_path)],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            return result.stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


# ---------------------------------------------------------------------------
# Pattern matching
# ---------------------------------------------------------------------------

def _check_patterns(text: str, patterns: list[str], label: str) -> dict:
    matched = []
    unmatched = []
    for pat in patterns:
        if re.search(pat, text):
            matched.append(pat)
        else:
            unmatched.append(pat)
    return {"label": label, "matched": matched, "unmatched": unmatched, "pass": len(unmatched) == 0}


# ---------------------------------------------------------------------------
# Validation tests
# ---------------------------------------------------------------------------

def validate_dot_mmac_shape(results: dict):
    """P1 Compute: tt.dot, #ttg.dot_op<, #ttg.amd_mfma<"""
    print("[1/8] triton.dot_mmac_shape ...")
    _clear_triton_cache()
    M, N, K = 128, 128, 64
    A = torch.randn((M, K), device="cuda", dtype=torch.float16)
    B = torch.randn((K, N), device="cuda", dtype=torch.float16)
    C = torch.empty((M, N), device="cuda", dtype=torch.float32)
    grid = (triton.cdiv(M, 16) * triton.cdiv(N, 16),)
    matmul_kernel[grid](
        A, B, C, M, N, K,
        A.stride(0), A.stride(1), B.stride(0), B.stride(1), C.stride(0), C.stride(1),
        BLOCK_M=16, BLOCK_N=16, BLOCK_K=32,
    )
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("matmul_kernel")
    ttgir = _extract_ttgir(entry) if entry else None
    isa = None
    if entry:
        hsaco = _extract_hsaco(entry)
        if hsaco:
            isa = _run_dccobjdump(hsaco)

    r = {"ttgir_available": ttgir is not None, "isa_available": isa is not None}
    if ttgir:
        r["ttgir"] = _check_patterns(ttgir, [
            r"\btt\.dot(?:_scaled)?\b",
            r"#ttg\.dot_op<",
            r"#ttg\.amd_mfma<",
        ], "ttgir_patterns")
    if isa:
        r["isa"] = _check_patterns(isa, [
            r"\bv_mmac(?:_[a-z0-9]+)+\b",
        ], "isa_patterns")
    results["triton.dot_mmac_shape"] = r


def validate_mask_simplification(results: dict):
    """P2 Memory: mask removal -> tt.load without mask -> amdg.buffer_load"""
    print("[2/8] triton.mask_simplification ...")
    _clear_triton_cache()
    N = 4096
    BLOCK = 1024
    X = torch.randn((N,), device="cuda", dtype=torch.float32)
    Y = torch.empty_like(X)

    # With mask removed (EVEN_N = True because N % BLOCK == 0)
    grid = (triton.cdiv(N, BLOCK),)
    elementwise_mask_removed_kernel[grid](X, Y, N, BLOCK_SIZE=BLOCK)
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("elementwise_mask_removed_kernel")
    ttgir_no_mask = _extract_ttgir(entry) if entry else None

    # With mask (for comparison)
    elementwise_with_mask_kernel[grid](X, Y, N, BLOCK_SIZE=BLOCK)
    torch.cuda.synchronize()

    entry2 = _find_latest_cache_entry("elementwise_with_mask_kernel")
    ttgir_with_mask = _extract_ttgir(entry2) if entry2 else None

    r = {
        "ttgir_no_mask_available": ttgir_no_mask is not None,
        "ttgir_with_mask_available": ttgir_with_mask is not None,
    }
    if ttgir_no_mask:
        # Without mask, expect amdg.buffer_load without mask operand
        r["no_mask"] = _check_patterns(ttgir_no_mask, [
            r"\bamdg\.buffer_load\b",
        ], "buffer_load_without_mask")
        # Check no mask on tt.load in the hot path (tt.load without mask arg)
        load_lines = [l for l in ttgir_no_mask.split("\n") if "tt.load" in l]
        r["no_mask_tt_load_lines"] = load_lines[:5]
    if ttgir_with_mask:
        load_lines = [l for l in ttgir_with_mask.split("\n") if "tt.load" in l]
        r["with_mask_tt_load_lines"] = load_lines[:5]
    results["triton.mask_simplification"] = r


def validate_num_stages_pipeline(results: dict):
    """P1 Latency: ttg.async_wait, ttg.async_commit_group"""
    print("[3/8] triton.num_stages_pipeline ...")
    _clear_triton_cache()
    M, N, K = 128, 128, 64
    A = torch.randn((M, K), device="cuda", dtype=torch.float16)
    B = torch.randn((K, N), device="cuda", dtype=torch.float16)
    C = torch.empty((M, N), device="cuda", dtype=torch.float32)
    grid = (triton.cdiv(M, 16) * triton.cdiv(N, 16),)
    matmul_pipelined_kernel[grid](
        A, B, C, M, N, K,
        A.stride(0), A.stride(1), B.stride(0), B.stride(1), C.stride(0), C.stride(1),
        BLOCK_M=16, BLOCK_N=16, BLOCK_K=32,
    )
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("matmul_pipelined_kernel")
    ttgir = _extract_ttgir(entry) if entry else None
    r = {"ttgir_available": ttgir is not None}
    if ttgir:
        r["ttgir"] = _check_patterns(ttgir, [
            r"\bttg\.async_wait\b",
            r"\bttg\.async_commit_group\b",
        ], "pipeline_patterns")
    results["triton.num_stages_pipeline"] = r


def validate_barrier_scope_reduction(results: dict):
    """P3 Latency: ttg.local_barrier, amdg.wait_barrier"""
    print("[5/8] triton.barrier_scope_reduction ...")
    _clear_triton_cache()
    N = 4096
    X = torch.randn((N,), device="cuda", dtype=torch.float32)
    Y = torch.empty_like(X)
    grid = (triton.cdiv(N, 1024),)
    barrier_kernel[grid](X, Y, N, BLOCK_SIZE=1024)
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("barrier_kernel")
    ttgir = _extract_ttgir(entry) if entry else None
    r = {"ttgir_available": ttgir is not None}
    if ttgir:
        r["ttgir"] = _check_patterns(ttgir, [
            r"\bttg\.local_barrier\b",
            r"\bamdg\.wait_barrier\b",
        ], "barrier_patterns")
    results["triton.barrier_scope_reduction"] = r


def validate_ilp_unroll(results: dict):
    """P2 Latency: tl.static_range unroll — check expanded IR"""
    print("[4/8] triton.ilp_unroll ...")
    _clear_triton_cache()
    N = 4096
    X = torch.randn((N,), device="cuda", dtype=torch.float32)
    Y = torch.empty_like(X)
    grid = (triton.cdiv(N, 1024),)
    unrolled_kernel[grid](X, Y, N, BLOCK_SIZE=1024, UNROLL_FACTOR=4)
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("unrolled_kernel")
    ttgir = _extract_ttgir(entry) if entry else None
    r = {"ttgir_available": ttgir is not None}
    if ttgir:
        # static_range should produce expanded (unrolled) IR, not a loop
        has_loop = bool(re.search(r"\bscf\.for\b", ttgir))
        load_count = len(re.findall(r"\btt\.load\b", ttgir))
        add_count = len(re.findall(r"\btt\.add\b", ttgir))
        r["has_scf_for"] = has_loop
        r["tt_load_count"] = load_count
        r["tt_add_count"] = add_count
        r["note"] = "static_range(4) should expand loop body 4x; more add ops than a single-loop version"
    results["triton.ilp_unroll"] = r


def validate_layout_conversion(results: dict):
    """P7 Memory: ttg.convert_layout between #ttg.blocked and #ttg.dot_op"""
    print("[6/8] triton.layout_conversion_optimization ...")
    _clear_triton_cache()
    M, N, K = 128, 128, 64
    A = torch.randn((M, K), device="cuda", dtype=torch.float16)
    B = torch.randn((K, N), device="cuda", dtype=torch.float16)
    C = torch.empty((M, N), device="cuda", dtype=torch.float32)
    grid = (triton.cdiv(M, 16) * triton.cdiv(N, 16),)
    # Reuse the matmul kernel — it must convert blocked->dot_op before tl.dot
    matmul_kernel[grid](
        A, B, C, M, N, K,
        A.stride(0), A.stride(1), B.stride(0), B.stride(1), C.stride(0), C.stride(1),
        BLOCK_M=16, BLOCK_N=16, BLOCK_K=32,
    )
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("matmul_kernel")
    ttgir = _extract_ttgir(entry) if entry else None
    r = {"ttgir_available": ttgir is not None}
    if ttgir:
        r["ttgir"] = _check_patterns(ttgir, [
            r"\bttg\.convert_layout\b",
            r"\b#ttg\.blocked\b",
            r"\b#ttg\.dot_op<",
        ], "layout_conversion_patterns")
        convert_count = len(re.findall(r"\bttg\.convert_layout\b", ttgir))
        r["convert_layout_count"] = convert_count
    results["triton.layout_conversion_optimization"] = r


def validate_coalesced_load_store(results: dict):
    """P1 Memory: #ttg.blocked with contiguous order"""
    print("[7/8] triton.coalesced_load_store ...")
    _clear_triton_cache()
    N = 4096
    X = torch.randn((N,), device="cuda", dtype=torch.float32)
    Y = torch.empty_like(X)
    grid = (triton.cdiv(N, 1024),)
    elementwise_with_mask_kernel[grid](X, Y, N, BLOCK_SIZE=1024)
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("elementwise_with_mask_kernel")
    ttgir = _extract_ttgir(entry) if entry else None
    r = {"ttgir_available": ttgir is not None}
    if ttgir:
        r["ttgir"] = _check_patterns(ttgir, [
            r"\b#ttg\.blocked\b",
        ], "blocked_layout_patterns")
    results["triton.coalesced_load_store"] = r


def validate_lds_tiling(results: dict):
    """P4 Memory: ttg.local_alloc, ttg.local_load, ttg.local_store"""
    print("[8/8] triton.lds_tiling ...")
    _clear_triton_cache()
    M, N, K = 128, 128, 64
    A = torch.randn((M, K), device="cuda", dtype=torch.float16)
    B = torch.randn((K, N), device="cuda", dtype=torch.float16)
    C = torch.empty((M, N), device="cuda", dtype=torch.float32)
    grid = (triton.cdiv(M, 16) * triton.cdiv(N, 16),)
    # Pipelined matmul with num_stages > 1 should produce LDS staging
    matmul_pipelined_kernel[grid](
        A, B, C, M, N, K,
        A.stride(0), A.stride(1), B.stride(0), B.stride(1), C.stride(0), C.stride(1),
        BLOCK_M=16, BLOCK_N=16, BLOCK_K=32,
    )
    torch.cuda.synchronize()

    entry = _find_latest_cache_entry("matmul_pipelined_kernel")
    ttgir = _extract_ttgir(entry) if entry else None
    r = {"ttgir_available": ttgir is not None}
    if ttgir:
        r["ttgir"] = _check_patterns(ttgir, [
            r"\bttg\.local_alloc\b",
            r"\bttg\.local_load\b",
            r"\bttg\.local_store\b",
            r"\bttg\.async_copy_global_to_local\b",
        ], "lds_tiling_patterns")
    results["triton.lds_tiling"] = r


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Triton version: {triton.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Device: {torch.cuda.get_device_name(0)}")
    print(f"Cache dir: {_get_triton_cache_dir()}")
    print()

    results: dict = {}

    try:
        validate_dot_mmac_shape(results)
    except Exception as e:
        results.setdefault("triton.dot_mmac_shape", {})["error"] = str(e)

    try:
        validate_mask_simplification(results)
    except Exception as e:
        results.setdefault("triton.mask_simplification", {})["error"] = str(e)

    try:
        validate_num_stages_pipeline(results)
    except Exception as e:
        results.setdefault("triton.num_stages_pipeline", {})["error"] = str(e)

    try:
        validate_ilp_unroll(results)
    except Exception as e:
        results.setdefault("triton.ilp_unroll", {})["error"] = str(e)

    try:
        validate_barrier_scope_reduction(results)
    except Exception as e:
        results.setdefault("triton.barrier_scope_reduction", {})["error"] = str(e)

    try:
        validate_layout_conversion(results)
    except Exception as e:
        results.setdefault("triton.layout_conversion_optimization", {})["error"] = str(e)

    try:
        validate_coalesced_load_store(results)
    except Exception as e:
        results.setdefault("triton.coalesced_load_store", {})["error"] = str(e)

    try:
        validate_lds_tiling(results)
    except Exception as e:
        results.setdefault("triton.lds_tiling", {})["error"] = str(e)

    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    for method, data in results.items():
        if "error" in data:
            status = "ERROR"
        elif "ttgir" in data and isinstance(data["ttgir"], dict):
            status = "PASS" if data["ttgir"]["pass"] else "FAIL"
        elif "no_mask" in data and isinstance(data["no_mask"], dict):
            status = "PASS" if data["no_mask"]["pass"] else "FAIL"
        else:
            status = "INCONCLUSIVE"
        print(f"  {method}: {status}")

    out_path = out_dir / "evidence_validation_results.json"
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
