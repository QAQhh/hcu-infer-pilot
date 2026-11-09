#!/usr/bin/env python3
"""HCU architecture specs and peak formulas used by profiler/roofline scripts.

Formulas mirror HCU-Analyzer's TFLOPS calculator:
  /zhenxin/obsidian-book/raw/ai-compiler/specs-docs/hcu_tflops_calculator.py
Memory bandwidth values mirror HCU-Analyzer BMZ/NMZ perfdata tables.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


NA = None


@dataclass(frozen=True)
class HcuModelSpec:
    key: str
    label: str
    target: str
    default_cu: int
    default_clock_mhz: int
    max_cu: int
    peak_bw_gbs: float | None
    aliases: tuple[str, ...] = ()


MODELS: Mapping[str, HcuModelSpec] = {
    "bw_b0_nmz": HcuModelSpec(
        "bw_b0_nmz", "BW B0-NMZ(shensuan3)", "gfx938", 64, 1350, 64, 2000.0,
        ("b0", "nmz", "bw b0-nmz", "bw1100"),
    ),
    "bw_a0_bmz": HcuModelSpec(
        "bw_a0_bmz", "BW A0-BMZ(shensuan3)", "gfx936", 80, 1500, 80, 1800.0,
        ("a0", "bmz", "bw a0-bmz", "bw1000", "bw150", "bw151"),
    ),
    "yueying": HcuModelSpec("yueying", "YueYing", "gfx92a", 128, 1500, 128, None, ("yy",)),
    "kme": HcuModelSpec("kme", "KME(shensuan2)", "gfx928", 128, 1500, 128, 2000.0, ("zd", "kme-zd")),
    "km": HcuModelSpec("km", "KM(shensuan2)", "gfx928", 128, 1500, 128, 1500.0, ("km-zd",)),
    "zf": HcuModelSpec("zf", "ZF(shensuan1)", "gfx926", 64, 1200, 64, None),
}

ARCH_DEFAULT_MODEL = {
    "gfx936": "bw_a0_bmz",
    "gfx938": "bw_b0_nmz",
    "gfx928": "kme",
    "gfx92a": "yueying",
    "gfx926": "zf",
}

MMOP_SHAPES: Mapping[str, tuple[int, int, int]] = {
    "fp64": (16, 16, 4),
    "fp32_*2": (16, 16, 8),
    "fp32": (16, 16, 4),
    "tf32": (16, 16, 8),
    "fp16": (16, 16, 16),
    "bf16": (16, 16, 16),
    "fp8": (16, 16, 32),
    "fp4_k32": (16, 16, 32),
    "fp4_k64": (16, 16, 64),
    "int8": (16, 16, 32),
    "int4": (16, 16, 64),
}

MMOP_CYCLES: Mapping[str, Mapping[str, int | None]] = {
    "zf": {"fp64": NA, "fp32_*2": NA, "fp32": NA, "tf32": NA, "fp16": NA, "bf16": NA, "fp8": NA, "fp4_k32": NA, "fp4_k64": NA, "int8": NA, "int4": NA},
    "km": {"fp64": 64, "fp32_*2": NA, "fp32": 64, "tf32": NA, "fp16": NA, "bf16": NA, "fp8": NA, "fp4_k32": NA, "fp4_k64": NA, "int8": NA, "int4": NA},
    "kme": {"fp64": NA, "fp32_*2": 64, "fp32": 64, "tf32": 32, "fp16": 32, "bf16": 32, "fp8": NA, "fp4_k32": NA, "fp4_k64": NA, "int8": 32, "int4": NA},
    "bw_a0_bmz": {"fp64": 32, "fp32_*2": 32, "fp32": 32, "tf32": 8, "fp16": 8, "bf16": 8, "fp8": NA, "fp4_k32": NA, "fp4_k64": NA, "int8": 8, "int4": 8},
    "bw_b0_nmz": {"fp64": 32, "fp32_*2": 32, "fp32": 32, "tf32": 8, "fp16": 8, "bf16": 8, "fp8": 8, "fp4_k32": NA, "fp4_k64": NA, "int8": 8, "int4": 16},
    "yueying": {"fp64": NA, "fp32_*2": NA, "fp32": 64, "tf32": 32, "fp16": 32, "bf16": 32, "fp8": 32, "fp4_k32": 32, "fp4_k64": NA, "int8": 32, "int4": NA},
}

FMA_FACTORS: Mapping[str, Mapping[str, float | None]] = {
    "zf": {"fp64": 1, "fp32": 1, "fp16": 2, "int8": 4, "int4": 8},
    "km": {"fp64": 1, "fp32": 1, "fp16": 2, "int8": 4, "int4": 8},
    "kme": {"fp64": NA, "fp32": 1, "fp16": 2, "int8": 4, "int4": 8},
    "bw_a0_bmz": {"fp64": 1, "fp32": 2, "fp16": 2, "int8": 4, "int4": 8},
    "bw_b0_nmz": {"fp64": 1, "fp32": 2, "fp16": 2, "int8": 4, "int4": 8},
    "yueying": {"fp64": 1 / 16, "fp32": 1, "fp16": 2, "int8": 4, "int4": 8},
}


def normalize_name(name: str) -> str:
    return str(name or "").strip().lower().replace("-", "_").replace(" ", "_")


def resolve_model(name: str | None) -> str | None:
    wanted = normalize_name(name or "")
    if not wanted:
        return None
    for key, spec in MODELS.items():
        if wanted == key or wanted == normalize_name(spec.label):
            return key
        if wanted == normalize_name(spec.target):
            return key
        if any(wanted == normalize_name(alias) for alias in spec.aliases):
            return key
    return None


def model_for_arch(arch: str | None) -> str | None:
    return ARCH_DEFAULT_MODEL.get(normalize_name(arch or ""))


def mmop_tops(model: str, precision: str, cu: int, clock_mhz: int) -> float | None:
    cycles = MMOP_CYCLES.get(model, {}).get(precision)
    shape = MMOP_SHAPES.get(precision)
    if cycles is None or shape is None:
        return None
    m, n, k = shape
    return m * n * k * 2 / cycles * 4 * cu * clock_mhz / 1_000 / 1_000


def fma_tops(model: str, precision: str, cu: int, clock_mhz: int) -> float | None:
    factor = FMA_FACTORS.get(model, {}).get(precision)
    if factor is None:
        return None
    return cu * clock_mhz / 1_000 * 64 * 2 / 1_000 * factor


def default_precision_for_kind(kind: str | None) -> str:
    return "fp16" if kind == "mmop" else "fp32"


def gpu_peak_spec(
    env: dict | None,
    *,
    compute_kind: str | None = None,
    precision: str | None = None,
) -> dict:
    env = env or {}
    gpu = (env.get("gpus") or [{}])[0]
    arch = gpu.get("gfx_arch") or gpu.get("gcn_arch") or env.get("primary_gfx_arch")
    model = resolve_model(gpu.get("model") or gpu.get("name")) or model_for_arch(arch) or "bw_b0_nmz"
    spec = MODELS[model]
    cu = int(gpu.get("compute_units") or spec.default_cu)
    cu = max(1, min(cu, spec.max_cu))
    clock_mhz = int(gpu.get("clock_mhz") or gpu.get("sclk_mhz") or spec.default_clock_mhz)
    kind = compute_kind if compute_kind in {"mmop", "valu", "fma"} else "mmop"
    prec = precision or default_precision_for_kind(kind)
    peak = mmop_tops(model, prec, cu, clock_mhz) if kind == "mmop" else fma_tops(model, prec, cu, clock_mhz)
    if peak is None and kind != "mmop":
        peak = fma_tops(model, "fp32", cu, clock_mhz)
        prec = "fp32"
    if peak is None:
        peak = mmop_tops(model, "fp16", cu, clock_mhz)
        prec = "fp16"
        kind = "mmop"
    bw = float(gpu.get("peak_bw_gbs") or spec.peak_bw_gbs or 0.0)
    return {
        "model": model,
        "label": spec.label,
        "arch": arch or spec.target,
        "compute_kind": kind,
        "precision": prec,
        "cu": cu,
        "clock_mhz": clock_mhz,
        "peak_compute_tops": peak,
        "peak_bw_gbs": bw,
        "source": "HCU-Analyzer tflops formula + perfdata bandwidth table",
    }
