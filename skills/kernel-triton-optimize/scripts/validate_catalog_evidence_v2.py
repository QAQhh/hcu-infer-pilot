#!/usr/bin/env python3
"""Remote HCU evidence probes for the Triton optimization catalog.

This script is intentionally conservative: it only reports "artifact_proof" for
methods whose catalog evidence can be checked by a standalone TTGIR/ISA pattern.
Methods that require before/after deltas, source/config mapping, correctness, or
timing are reported as "auto_delta_required" or "supporting_only". There is no
human/manual evidence path in the automatic tuner.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import torch
import triton
import triton.language as tl


@triton.jit
def matmul_kernel(A, B, C, M: tl.constexpr, N: tl.constexpr, K: tl.constexpr,
                  BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr):
    pid = tl.program_id(0)
    num_pid_m = tl.cdiv(M, BLOCK_M)
    pid_m = pid % num_pid_m
    pid_n = pid // num_pid_m
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    a_ptrs = A + offs_m[:, None] * K + offs_k[None, :]
    b_ptrs = B + offs_k[:, None] * N + offs_n[None, :]
    acc = tl.zeros((BLOCK_M, BLOCK_N), tl.float32)
    for _ in tl.range(0, K, BLOCK_K):
        a = tl.load(a_ptrs)
        b = tl.load(b_ptrs)
        acc += tl.dot(a, b)
        a_ptrs += BLOCK_K
        b_ptrs += BLOCK_K * N
    tl.store(C + offs_m[:, None] * N + offs_n[None, :], acc)


@triton.heuristics({"EVEN_N": lambda args: args["N"] % args["BLOCK_SIZE"] == 0})
@triton.jit
def copy_mask_split_kernel(X, Y, N: tl.constexpr, BLOCK_SIZE: tl.constexpr, EVEN_N: tl.constexpr):
    offs = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    if EVEN_N:
        x = tl.load(X + offs)
        tl.store(Y + offs, x)
    else:
        mask = offs < N
        x = tl.load(X + offs, mask=mask, other=0.0)
        tl.store(Y + offs, x, mask=mask)


@triton.jit
def copy_masked_kernel(X, Y, N: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    offs = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = offs < N
    x = tl.load(X + offs, mask=mask, other=0.0)
    tl.store(Y + offs, x, mask=mask)


@triton.jit
def static_range_kernel(X, Y, N: tl.constexpr, BLOCK_SIZE: tl.constexpr, UNROLL: tl.constexpr):
    offs = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    x = tl.load(X + offs)
    acc = x
    for _ in tl.static_range(0, UNROLL):
        acc += x
    tl.store(Y + offs, acc)


@triton.jit
def barrier_kernel(X, Y, N: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    offs = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    x = tl.load(X + offs)
    tl.debug_barrier()
    tl.store(Y + offs, x)


@triton.jit
def cache_kernel(X, Y, N: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    offs = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    x = tl.load(X + offs, cache_modifier=".cg")
    tl.store(Y + offs, x)


@triton.jit
def math_kernel(X, Y, N: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    offs = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    x = tl.load(X + offs)
    y = tl.rsqrt(x * x + 1.0) + 1.0 / (x + 2.0)
    tl.store(Y + offs, y)


@triton.jit
def fp8_dot_kernel(A, B, C, M: tl.constexpr, N: tl.constexpr, K: tl.constexpr,
                   BM: tl.constexpr, BN: tl.constexpr, BK: tl.constexpr):
    pid = tl.program_id(0)
    pid_m = pid % tl.cdiv(M, BM)
    pid_n = pid // tl.cdiv(M, BM)
    offs_m = pid_m * BM + tl.arange(0, BM)
    offs_n = pid_n * BN + tl.arange(0, BN)
    offs_k = tl.arange(0, BK)
    a = tl.load(A + offs_m[:, None] * K + offs_k[None, :])
    b = tl.load(B + offs_k[:, None] * N + offs_n[None, :])
    acc = tl.dot(a, b, out_dtype=tl.float32)
    tl.store(C + offs_m[:, None] * N + offs_n[None, :], acc)


def cache_dir() -> Path:
    return Path(os.environ.get("TRITON_CACHE_DIR", Path.home() / ".triton" / "cache"))


def reset_cache() -> None:
    root = cache_dir()
    if root.is_dir():
        for child in root.iterdir():
            if child.is_dir():
                shutil.rmtree(child, ignore_errors=True)
            else:
                child.unlink(missing_ok=True)


def latest_artifacts() -> dict[str, str]:
    root = cache_dir()
    if not root.is_dir():
        return {}
    entries = sorted(root.rglob("*"), key=lambda p: p.stat().st_mtime if p.exists() else 0, reverse=True)
    out: dict[str, str] = {}
    for path in entries:
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in {".ttir", ".ttgir", ".llir", ".amdgcn", ".hsaco", ".json"} and suffix[1:] not in out:
            out[suffix[1:]] = str(path)
    return out


def read_text(path: str | None) -> str:
    if not path:
        return ""
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def dump_isa(hsaco: str | None, out_dir: Path) -> str:
    if not hsaco:
        return ""
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "dccobjdump",
        f"--inputs={Path(hsaco).resolve()}",
        "--show-sass",
        "--show-instruction-encoding",
        "--separate-functions",
        f"--output={out_dir}",
    ]
    try:
        proc = subprocess.run(cmd, text=True, capture_output=True, timeout=90)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return str(exc)
    texts = [proc.stdout or "", proc.stderr or ""]
    for path in out_dir.rglob("*"):
        if path.is_file() and path.stat().st_size < 20_000_000:
            texts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(texts)


def read_amdgcn_and_dump(artifacts: dict[str, str], out_dir: Path) -> str:
    return "\n".join([read_text(artifacts.get("amdgcn")), dump_isa(artifacts.get("hsaco"), out_dir)])


def has(pattern: str, text: str) -> bool:
    return bool(re.search(pattern, text, re.IGNORECASE))


def bench(fn, warmup: int = 5, repeat: int = 20) -> float:
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()
    start_event = torch.cuda.Event(enable_timing=True)
    end_event = torch.cuda.Event(enable_timing=True)
    start_event.record()
    for _ in range(repeat):
        fn()
    end_event.record()
    torch.cuda.synchronize()
    return start_event.elapsed_time(end_event) / repeat


def compile_matmul(out_dir: Path) -> dict:
    reset_cache()
    m = n = k = 128
    a = torch.randn((m, k), device="cuda", dtype=torch.float16)
    b = torch.randn((k, n), device="cuda", dtype=torch.float16)
    c = torch.empty((m, n), device="cuda", dtype=torch.float32)
    grid = (triton.cdiv(m, 32) * triton.cdiv(n, 32),)
    ms = bench(lambda: matmul_kernel[grid](a, b, c, m, n, k, BLOCK_M=32, BLOCK_N=32, BLOCK_K=32, num_warps=4))
    art = latest_artifacts()
    ttgir = read_text(art.get("ttgir"))
    isa = read_amdgcn_and_dump(art, out_dir / "isa_matmul")
    return {"artifacts": art, "ttgir": ttgir, "isa": isa, "ms": ms}


def compile_copy(mask_split: bool, out_dir: Path) -> dict:
    reset_cache()
    n = 4096
    block = 256
    x = torch.randn((n,), device="cuda", dtype=torch.float32)
    y = torch.empty_like(x)
    grid = (triton.cdiv(n, block),)
    if mask_split:
        ms = bench(lambda: copy_mask_split_kernel[grid](x, y, n, BLOCK_SIZE=block, num_warps=4))
    else:
        ms = bench(lambda: copy_masked_kernel[grid](x, y, n, BLOCK_SIZE=block, num_warps=4))
    art = latest_artifacts()
    ttgir = read_text(art.get("ttgir"))
    isa = read_amdgcn_and_dump(art, out_dir / ("isa_copy_split" if mask_split else "isa_copy_masked"))
    return {"artifacts": art, "ttgir": ttgir, "isa": isa, "ms": ms}


def compile_low_precision_dot(out_dir: Path) -> dict:
    reset_cache()
    m = n = k = 128
    bm = bn = bk = 32
    a = torch.randn((m, k), device="cuda", dtype=torch.float16).to(torch.float8_e4m3fn)
    b = torch.randn((k, n), device="cuda", dtype=torch.float16).to(torch.float8_e4m3fn)
    c = torch.empty((m, n), device="cuda", dtype=torch.float32)
    grid = (triton.cdiv(m, bm) * triton.cdiv(n, bn),)
    try:
        fp8_dot_kernel[grid](a, b, c, m, n, k, BM=bm, BN=bn, BK=bk, num_warps=4)
        torch.cuda.synchronize()
        error = None
    except Exception as exc:  # noqa: BLE001 - validator records compiler failures as evidence.
        error = str(exc)
    art = latest_artifacts()
    ttgir = read_text(art.get("ttgir"))
    isa = read_amdgcn_and_dump(art, out_dir / "isa_fp8_dot") if not error else read_text(art.get("amdgcn"))
    return {"artifacts": art, "ttgir": ttgir, "isa": isa, "error": error}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="hygon_tmp/catalog_evidence_results")
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("TRITON_CACHE_DIR", str(out_dir / "triton_cache"))

    results: dict[str, dict] = {
        "_env": {
            "torch": torch.__version__,
            "triton": triton.__version__,
            "cuda_available": torch.cuda.is_available(),
            "device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
            "cache_dir": str(cache_dir()),
        }
    }
    if not torch.cuda.is_available():
        raise SystemExit("torch.cuda is not available; run this inside the selected HCU container")

    mm = compile_matmul(out_dir)
    results["triton.dot_mmac_shape"] = {
        "proof_status": "artifact_proof" if (has(r"tt\.dot", mm["ttgir"]) and has(r"#ttg\.amd_mfma<", mm["ttgir"])) or has(r"\bv_mmac", mm["isa"]) else "failed",
        "required": "tt.dot/#ttg.amd_mfma or v_mmac/MMOP",
        "matched": {
            "tt_dot": has(r"tt\.dot", mm["ttgir"]),
            "amd_mfma": has(r"#ttg\.amd_mfma<", mm["ttgir"]),
            "v_mmac": has(r"\bv_mmac", mm["isa"]),
        },
        "ms": mm["ms"],
        "artifacts": mm["artifacts"],
    }
    results["triton.layout_conversion_optimization"] = {
        "proof_status": "supporting_only",
        "required": "before/after reduction in hot-path ttg.convert_layout count plus timing",
        "convert_layout_count": len(re.findall(r"ttg\.convert_layout", mm["ttgir"])),
        "reason": "A single post-compile ttg.convert_layout count is an opportunity signal, not proof.",
    }
    results["triton.num_stages_pipeline"] = {
        "proof_status": "supporting_only",
        "required": "active num_stages config plus before/after timing/resource pressure",
        "matched": {
            "ttg_async_wait": has(r"ttg\.async_wait", mm["ttgir"]),
            "ttg_async_commit_group": has(r"ttg\.async_commit_group", mm["ttgir"]),
            "amdg_async_wait": has(r"amdg\.async_wait", mm["ttgir"]),
        },
    }
    results["triton.matrix_ds_mls"] = {
        "proof_status": "artifact_proof" if (
            has(r"tt\.matrix_load", mm["ttgir"]) or
            has(r"amdg\.matrix_load_to_local", mm["ttgir"]) or
            has(r"amdg\.local_load_packed_tranposed", mm["ttgir"]) or
            has(r"\b(?:matrix_load|mls|ds_read_m32x16_b16|ds_read_matrix)", mm["isa"])
        ) else "auto_delta_required",
        "required": "matrix-load/local-load-packed TTGIR or DS matrix-read ISA, plus unique-value correctness",
        "reason": "Generic tl.dot usually proves MMAC, not MLS; this result is expected to be auto_delta_required unless the build lowers through MLS.",
    }

    lowp = compile_low_precision_dot(out_dir)
    lowp_ttgir = lowp.get("ttgir", "")
    lowp_isa = lowp.get("isa", "")
    lowp_error = lowp.get("error")
    lowp_patterns = {
        "tt_dot": has(r"tt\.dot\b", lowp_ttgir),
        "tt_dot_scaled": has(r"tt\.dot_scaled", lowp_ttgir),
        "fp8_type": has(r"f8E[45]M[23]", lowp_ttgir),
        "supporting_lowp_isa": has(r"\b(?:v_cvt|v_mmac)[a-z0-9_]*(?:fp8|bf8|tf32)", lowp_isa),
        "unsupported_dot_scale": bool(lowp_error and "Unsupported DotScaleOp" in lowp_error),
    }
    lowp_frontend_proof = (
        (lowp_patterns["tt_dot"] and lowp_patterns["fp8_type"]) or lowp_patterns["tt_dot_scaled"]
    )
    results["triton.low_precision_fp8_bf8"] = {
        "proof_status": "artifact_proof" if (
            not lowp_error and lowp_frontend_proof
        ) else "failed" if lowp_error and (lowp_patterns["tt_dot_scaled"] or lowp_patterns["fp8_type"]) else "auto_delta_required",
        "required": "successful final compile plus either tl.dot/tt.dot with f8/bf8 operands or tt.dot_scaled; low-precision ISA strings are supporting evidence",
        "matched": lowp_patterns,
        "error": lowp_error,
        "artifacts": lowp.get("artifacts", {}),
    }

    split = compile_copy(True, out_dir)
    masked = compile_copy(False, out_dir)
    results["triton.mask_simplification"] = {
        "proof_status": "supporting_only",
        "required": "before/after mask/predicate reduction, correctness for aligned and tail cases, timing",
        "split_mask_count": len(re.findall(r"\bmask\b", split["ttgir"])),
        "masked_mask_count": len(re.findall(r"\bmask\b", masked["ttgir"])),
        "split_ms": split["ms"],
        "masked_ms": masked["ms"],
    }
    results["triton.vectorized_load_store"] = {
        "proof_status": "artifact_proof" if has(r"(?:global|buffer|flat)_(?:load|store)_(?:dwordx[234]|b(?:64|128))", split["isa"]) else "auto_delta_required",
        "required": "wide load/store ISA such as dwordx2/x3/x4 or b64/b128, plus fewer memory instructions/timing",
        "artifacts": split["artifacts"],
    }
    results["triton.coalesced_load_store"] = {
        "proof_status": "auto_delta_required",
        "required": "source contiguous addressing plus bandwidth/timing comparison against strided/scattered baseline",
        "reason": "Generic TTGIR/ISA load-store families are intentionally not treated as proof.",
    }
    results["triton.block_size"] = {
        "proof_status": "auto_delta_required",
        "required": "accepted finite BLOCK_SIZE configs, correctness, and timing",
    }

    reset_cache()
    n = 4096
    x = torch.randn((n,), device="cuda", dtype=torch.float32)
    y = torch.empty_like(x)
    grid = (triton.cdiv(n, 256),)
    static_ms = bench(lambda: static_range_kernel[grid](x, y, n, BLOCK_SIZE=256, UNROLL=4, num_warps=4))
    art = latest_artifacts()
    ttgir = read_text(art.get("ttgir"))
    results["triton.ilp_unroll"] = {
        "proof_status": "supporting_only",
        "required": "range vs tl.static_range before/after loop/instruction/resource delta plus timing",
        "has_scf_for": has(r"\bscf\.for\b", ttgir),
        "add_like_count": len(re.findall(r"\b(?:arith\.addf|tt\.add)\b", ttgir)),
        "ms": static_ms,
    }

    reset_cache()
    barrier_ms = bench(lambda: barrier_kernel[grid](x, y, n, BLOCK_SIZE=256, num_warps=4))
    art = latest_artifacts()
    ttgir = read_text(art.get("ttgir"))
    isa = read_amdgcn_and_dump(art, out_dir / "isa_barrier")
    results["triton.barrier_scope_reduction"] = {
        "proof_status": "supporting_only",
        "required": "before/after fewer hot-path barriers/waits plus correctness/timing",
        "matched": {
            "ttg_local_barrier": has(r"ttg\.local_barrier", ttgir),
            "amdg_wait_barrier": has(r"amdg\.wait_barrier", ttgir),
            "s_barrier": has(r"\bs_barrier\b", isa),
        },
        "ms": barrier_ms,
    }

    reset_cache()
    cache_ms = bench(lambda: cache_kernel[grid](x, y, n, BLOCK_SIZE=256, num_warps=4))
    art = latest_artifacts()
    ttgir = read_text(art.get("ttgir"))
    isa = read_amdgcn_and_dump(art, out_dir / "isa_cache")
    results["triton.cache_policy_buffer_ops"] = {
        "proof_status": "artifact_proof" if has(r"cacheModifier\s*=\s*cg", ttgir) and has(r"\bglc\b.*\bslc\b", isa) else "auto_delta_required",
        "required": "explicit cache modifier in TTGIR and glc/slc or equivalent ISA bits, plus timing for optimization claim",
        "matched": {
            "cache_modifier_cg": has(r"cacheModifier\s*=\s*cg", ttgir),
            "glc_slc": has(r"\bglc\b.*\bslc\b", isa),
        },
        "ms": cache_ms,
    }

    reset_cache()
    math_ms = bench(lambda: math_kernel[grid](x, y, n, BLOCK_SIZE=256, num_warps=4))
    art = latest_artifacts()
    isa = read_amdgcn_and_dump(art, out_dir / "isa_math")
    results["triton.fast_math_lowering"] = {
        "proof_status": "supporting_only" if has(r"\bv_(?:rsq|sqrt|rcp|exp|log|sin|cos)(?:_[a-z0-9]+)*\b", isa) else "auto_delta_required",
        "required": "baseline vs approximate math sequence delta, explicit tolerance, accuracy, and timing",
        "matched": {
            "math_isa": has(r"\bv_(?:rsq|sqrt|rcp|exp|log|sin|cos)(?:_[a-z0-9]+)*\b", isa),
        },
        "ms": math_ms,
    }

    manual = {
        "triton.program_geometry_occupancy": "same kernel across program geometry configs with active config, occupancy/resource metadata, timing",
        "triton.work_granularity": "before/after per-program or per-lane work change with active config/source delta, resource_usage from metadata/AMDGCN/xcu/hipprof or instruction/request delta, correctness, and timing",
        "triton.register_pressure_control": "large vs smaller live-range/tile case with VGPR/SGPR/spill metadata delta and timing",
        "triton.fast_math_lowering": "baseline vs approximate math source under tolerance with changed sequence, accuracy, timing",
        "triton.layout_stride_transform": "source stride/layout rewrite with non-contiguous correctness and bandwidth/timing",
        "triton.async_copy_global_to_lds": "kernel that emits amdg.buffer_load_to_local or ttg.async_copy_global_to_local plus final LDS ISA/waits",
        "triton.tile_shape": "finite tile registry or config sweep with accepted BLOCK_M/BLOCK_N/BLOCK_K, active config, correctness, and timing",
        "triton.cache_policy_buffer_ops": "controlled cache_modifier/eviction_policy or cache-swizzle branch with artifact separation and timing",
        "triton.epilogue_fusion": "two-kernel post-op baseline vs fused epilogue with kernel-count/global-traffic reduction and timing",
        "triton.split_k_streamk": "source/config split-K or Stream-K partitioning, split-major partial buffer, dedicated Triton reduction kernel, correctness, and tail/timing",
        "triton.persistent_programs": "source/grid persistent mapping with tail balance/occupancy/timing",
        "triton.runtime_config_key": "required practice only: finite shape-family registry with accepted configs, guards, fallback, and fixed-config timing for the carried method",
    }
    for method, required in manual.items():
        results.setdefault(method, {"proof_status": "auto_delta_required", "required": required})

    out = out_dir / "evidence_validation_results.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v.get("proof_status") for k, v in results.items() if k != "_env"}, indent=2))
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
