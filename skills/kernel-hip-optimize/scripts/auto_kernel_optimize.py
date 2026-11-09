#!/usr/bin/env python3
"""Automatic kernel optimizer loop.

This script validates the optimizer state machine after `orchestrate.py setup`:

    state.json/run_dir -> methods.json -> no-op branch -> close-iter -> finalize

Method selection is evidence-driven: roofline allocates per-axis budget, then
hcu_top/SQTT/code-object evidence ranks registry methods for each axis.

It keeps a no-op fallback branch by default, then emits method-aware branch
kernels when the current best source matches a supported generator.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DEFAULT_REGISTRY = SKILL_DIR / "references" / "method_registry.json"
DEFAULT_FAMILY_CATALOG = SKILL_DIR / "references" / "kernel_family_catalog.json"
KERNEL_EXTS = (".hip", ".cu", ".cpp", ".cc", ".cxx", ".py")
AXES = ("compute", "memory", "latency")
DELTA_KEYS = {"compute": "delta_compute", "memory": "delta_memory", "latency": "delta_latency"}
TRIGGER_THRESHOLD = 0.05


MATRIX_SPECIFIC_METHODS = {
    "compute.mmac_tensor_core",
    "compute.mixed_precision_fp8_bf8",
    "memory.lds_tiling",
    "memory.global_to_lds_async",
    "memory.matrix_load_mls",
    "memory.ds_read_matrix_layout",
    "memory.lds_bank_conflict",
    "memory.ck_tile_named_pipeline",
    "latency.persistent_scheduler",
    "latency.split_k_streamk",
}

CK_TILE_TEMPLATE_ENV = "HYGON_CK_TILE_TEMPLATE"
FLAT_SAFE_FUNCTIONS = {"expf", "sqrtf", "rsqrtf", "sinf", "cosf", "tanhf", "fmaxf", "fminf"}
INDEXING_METHODS = {
    "memory.coalesced_access",
    "compute.thread_coarsening",
    "compute.register_pressure_control",
    "latency.ilp_unroll",
    "latency.waitcnt_pipeline",
}
ROW_REDUCTION_METHODS = {
    "memory.coalesced_access",
    "compute.thread_coarsening",
    "latency.reduce_barrier",
    "latency.wavefront_shuffle_ds_bpermute",
    "compute.register_pressure_control",
    "compute.fast_math_intrinsics",
}
COMPLEX_FAMILY_TRIGGER_TERMS = {
    "attention": [
        "attention",
        "qk",
        "qkv",
        "av",
        "causal",
        "mask",
        "rel_bias",
        "relative_bias",
        "paged",
        "flash",
        "score",
    ],
    "gather_scatter_index_add_embedding_backward": [
        "gather",
        "scatter",
        "index_add",
        "index_select",
        "embedding",
        "bincount",
        "atomicadd",
        "backward",
    ],
    "jagged_ragged_sparse": [
        "jagged",
        "ragged",
        "sparse",
        "offsets",
        "lengths",
        "csr",
        "dense_to_jagged",
        "jagged_to_dense",
        "pack",
        "pad",
    ],
    "segmented_reduction": [
        "segment",
        "segmented",
        "reduce_by_key",
        "histogram",
        "bincount",
        "bucket",
        "group_reduce",
    ],
    "custom_autograd_backward": [
        "backward",
        "grad",
        "autograd",
        "index_select_backward",
        "embedding_backward",
        "scatter_backward",
    ],
    "softmax_layernorm_row_reduction": [
        "softmax",
        "layernorm",
        "layer_norm",
        "rmsnorm",
        "rms_norm",
        "row_reduce",
        "row_reduction",
        "normalization",
    ],
    "matmul_gemm": [
        "matmul",
        "gemm",
        "bmm",
        "batched_gemm",
        "linear",
        "dense",
        "grouped_gemm",
        "moe_gemm",
        "ck_tile",
        "mmac",
        "mfma",
    ],
    "topk_sort_selection": [
        "topk",
        "top_k",
        "sort",
        "argsort",
        "partial_sort",
        "selection",
        "select",
        "beam",
        "sampling",
        "routing",
        "expert",
    ],
    "layout_transform_copy_pack": [
        "transpose",
        "permute",
        "contiguous",
        "copy",
        "pack",
        "unpack",
        "pad",
        "unpad",
        "reshape",
        "layout",
        "dense_to_jagged",
        "jagged_to_dense",
        "memcpy",
        "memset",
    ],
    "conv_pool_stencil": [
        "conv",
        "convolution",
        "depthwise",
        "pool",
        "maxpool",
        "avgpool",
        "stencil",
        "im2col",
        "winograd",
        "miopen",
    ],
    "quant_dequant_cast_pack": [
        "quant",
        "dequant",
        "fp8",
        "int8",
        "int4",
        "cast",
        "convert",
        "pack_bits",
        "unpack_bits",
        "scale",
        "zero_point",
        "saturation",
    ],
    "communication_collective_fusion": [
        "allreduce",
        "all_reduce",
        "allgather",
        "all_gather",
        "reduce_scatter",
        "broadcast",
        "collective",
        "rccl",
        "deepep",
        "flux",
        "comm_fusion",
        "overlap",
    ],
    "random_dropout_sampling": [
        "dropout",
        "random",
        "rng",
        "sampling",
        "multinomial",
        "bernoulli",
        "curand",
        "rocrand",
        "philox",
    ],
    "host_device_bubble": [
        "bubble",
        "gap",
        "hipmemcpy",
        "memcpy",
        "sync",
        "synchronize",
        "allocation",
        "dataloader",
        "host",
        "cpu_wait",
        "stream_wait",
    ],
}


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _run(cmd: list[str | Path], *, dry_run: bool) -> dict[str, Any]:
    item: dict[str, Any] = {
        "cmd": [str(part) for part in cmd],
        "cmd_text": " ".join(str(part) for part in cmd),
    }
    if dry_run:
        item["status"] = "planned"
        return item
    proc = subprocess.run(cmd, text=True, capture_output=True, encoding="utf-8", errors="ignore")
    item.update(
        {
            "status": "ok" if proc.returncode == 0 else "failed",
            "returncode": proc.returncode,
            "stdout_tail": (proc.stdout or "")[-4000:],
            "stderr_tail": (proc.stderr or "")[-4000:],
        }
    )
    return item


def _methods_by_id(methods: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(method.get("id") or ""): method for method in methods}


def _claim_methods(methods: list[dict[str, Any]], ids: list[str]) -> list[dict[str, Any]]:
    by_id = _methods_by_id(methods)
    claimed: list[dict[str, Any]] = []
    for mid in ids:
        if mid in by_id:
            claimed.append(by_id[mid])
    return claimed


def _state_path(args: argparse.Namespace) -> Path:
    if args.state:
        return Path(args.state).expanduser().resolve()
    if args.run_dir:
        return (Path(args.run_dir).expanduser().resolve() / "state.json")
    raise SystemExit("pass --state or --run-dir")


def _axis_budget(run_dir: Path, iteration: int) -> dict[str, int]:
    default = {"compute": 1, "memory": 1, "latency": 1}
    roofline_path = run_dir / f"iterv{iteration}" / "roofline.json"
    if not roofline_path.is_file():
        return default
    roofline = _read_json(roofline_path)
    raw = roofline.get("axis_budget", default)
    if not isinstance(raw, dict):
        return default
    return {axis: max(0, int(raw.get(axis, 0) or 0)) for axis in AXES}


def _load_iteration_evidence(run_dir: Path, iteration: int) -> tuple[dict[str, Any], dict[str, Any]]:
    iter_dir = run_dir / f"iterv{iteration}"
    roofline_path = iter_dir / "roofline.json"
    hcu_top_path = iter_dir / "hcu_top.json"
    roofline = _read_json(roofline_path) if roofline_path.is_file() else {}
    hcu_top = _read_json(hcu_top_path) if hcu_top_path.is_file() else {}
    return roofline, hcu_top


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return default
    if math.isnan(out) or math.isinf(out):
        return default
    return out


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _normalize_high_bad(value: float) -> float:
    if value <= 0:
        return 0.0
    if value <= 1:
        return _clamp01(value)
    if value <= 100:
        return _clamp01(value / 100.0)
    # Raw counters do not have a universal scale. Large nonzero counters are
    # strong trigger evidence but should not swamp roofline/SQTT evidence.
    return _clamp01(math.log10(value + 1.0) / 6.0)


def _normalize_low_bad(value: float) -> float:
    if value <= 0:
        return 1.0
    if value <= 1:
        return _clamp01(1.0 - value)
    if value <= 100:
        return _clamp01(1.0 - value / 100.0)
    return 0.0


def _metric_patterns(trigger_metric: str) -> list[str]:
    text = (trigger_metric or "").strip()
    if not text or text.lower() in {"manual", "dccobjdump", "hipprof --sqtt"}:
        return []
    return [part for part in text.split("|") if part]


def _all_metrics(hcu_top: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for axis in AXES:
        raw_items = hcu_top.get(axis, [])
        if not isinstance(raw_items, list):
            continue
        for item in raw_items:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name") or item.get("metric") or "")
            if not name:
                continue
            rows.append(
                {
                    "axis": axis,
                    "name": name,
                    "value": _safe_float(item.get("value")),
                    "unit": str(item.get("unit") or ""),
                    "samples": item.get("samples"),
                    "source_files": item.get("source_files", []),
                    "higher_is_worse": item.get("higher_is_worse"),
                }
            )
    return rows


def _match_trigger_metrics(trigger_metric: str, hcu_top: dict[str, Any]) -> list[dict[str, Any]]:
    patterns = _metric_patterns(trigger_metric)
    if not patterns:
        return []
    regex = re.compile("|".join(f"(?:{pat})" for pat in patterns), re.IGNORECASE)
    matches = []
    for item in _all_metrics(hcu_top):
        if regex.search(item["name"]):
            matches.append(item)
    return matches


def _parse_gfx_arch(state: dict[str, Any]) -> int:
    gpus = ((state.get("env", {}) or {}).get("gpus") or [{}])
    arch = ""
    if gpus:
        arch = str(gpus[0].get("gfx_arch") or gpus[0].get("gcn_arch") or "")
    digits = "".join(ch for ch in arch if ch.isdigit())
    try:
        return int(digits)
    except ValueError:
        return 0


def _gfx_arch_key(state: dict[str, Any]) -> str:
    gpus = ((state.get("env", {}) or {}).get("gpus") or [{}])
    arch = ""
    if gpus:
        arch = str(gpus[0].get("gfx_arch") or gpus[0].get("gcn_arch") or "")
    if not arch:
        arch = str((state.get("env", {}) or {}).get("primary_gfx_arch") or "")
    digits = "".join(ch for ch in arch if ch.isdigit())
    return f"gfx{digits}" if digits else ""


def _available_features(state: dict[str, Any], registry: dict[str, Any]) -> set[str]:
    arch_key = _gfx_arch_key(state)
    feature_map = registry.get("arch_feature_map", {})
    if isinstance(feature_map, dict) and arch_key in feature_map:
        return {str(item) for item in feature_map.get(arch_key, [])}
    detected_arch = _parse_gfx_arch(state)
    if detected_arch >= 938 and "gfx938" in feature_map:
        return {str(item) for item in feature_map.get("gfx938", [])}
    if detected_arch >= 936 and "gfx936" in feature_map:
        return {str(item) for item in feature_map.get("gfx936", [])}
    return set()


def _missing_required_features(meta: dict[str, Any], features: set[str]) -> list[str]:
    required = {str(item) for item in meta.get("required_features", [])}
    if not required or not features:
        return []
    return sorted(required - features)


def _is_arch_compatible(meta: dict[str, Any], detected_arch: int) -> bool:
    min_sm = int(meta.get("min_sm", 0) or 0)
    return not (detected_arch and min_sm > detected_arch)


def _skipped_higher(
    registry_methods: dict[str, Any],
    *,
    axis: str,
    selected_priority: int,
    selected_score: float,
    selected_ids: set[str],
    ineffective_ids: set[str],
    impl_failed_ids: set[str],
    detected_arch: int,
    features: set[str],
    scored_candidates: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    skipped: list[dict[str, Any]] = []
    for mid, meta in sorted(registry_methods.items(), key=lambda item: int(item[1].get("priority", 99))):
        if meta.get("axis") != axis:
            continue
        priority = int(meta.get("priority", 99))
        if priority >= selected_priority:
            continue
        reason = "no_trigger"
        min_sm = int(meta.get("min_sm", 0) or 0)
        if mid in selected_ids:
            reason = "already_selected"
        elif mid in impl_failed_ids:
            reason = "skip_condition"
        elif mid in ineffective_ids:
            reason = "skip_condition"
        elif detected_arch and min_sm > detected_arch:
            reason = "arch_incompatible"
        elif _missing_required_features(meta, features):
            reason = "feature_unavailable"
        else:
            candidate_score = float((scored_candidates.get(mid) or {}).get("score", 0.0))
            if candidate_score >= TRIGGER_THRESHOLD:
                reason = "skip_condition"
        item: dict[str, Any] = {"id": mid, "priority": priority, "reason": reason}
        candidate_score = float((scored_candidates.get(mid) or {}).get("score", 0.0))
        if reason == "skip_condition" and candidate_score > 0:
            item["detail"] = f"weaker_evidence_score={candidate_score:.4f} < selected_score={selected_score:.4f}"
        elif reason == "no_trigger":
            item["detail"] = f"evidence_score={candidate_score:.4f} below trigger threshold {TRIGGER_THRESHOLD:.2f}"
        skipped.append(item)
    return skipped


def _axis_delta(axis: str, roofline: dict[str, Any]) -> float:
    return _clamp01(_safe_float(roofline.get(DELTA_KEYS[axis]), 0.0))


def _roofline_axis_score(axis: str, roofline: dict[str, Any]) -> tuple[float, list[dict[str, Any]]]:
    evidence: list[dict[str, Any]] = []
    delta = _axis_delta(axis, roofline)
    if delta > 0:
        evidence.append({"metric": DELTA_KEYS[axis], "value": delta, "unit": "ratio"})
    bound = str(roofline.get("bound") or "")
    if (axis == "memory" and bound == "bandwidth") or bound == axis:
        delta = max(delta, 0.75)
        evidence.append({"metric": "roofline_bound_match", "value": 1.0, "unit": bound})
    if axis == "latency" and bound == "latency":
        delta = max(delta, 0.75)
    return delta, evidence


def _metric_trigger_score(meta: dict[str, Any], hcu_top: dict[str, Any]) -> tuple[float, list[dict[str, Any]]]:
    direction = str(meta.get("trigger_direction") or "manual")
    matches = _match_trigger_metrics(str(meta.get("trigger_metric") or ""), hcu_top)
    if not matches:
        return 0.0, []

    scored: list[tuple[float, dict[str, Any]]] = []
    for item in matches:
        value = _safe_float(item.get("value"))
        if direction == "low_is_bad":
            score = _normalize_low_bad(value)
        elif direction == "high_is_bad":
            score = _normalize_high_bad(value)
        else:
            # Manual triggers use metric presence as weak evidence; specialized
            # SQTT/codeobj helpers below may strengthen it.
            score = 0.30 + 0.30 * _normalize_high_bad(value)
        scored.append((score, item))

    scored.sort(key=lambda pair: pair[0], reverse=True)
    evidence = [
        {
            "metric": item["name"],
            "value": _safe_float(item.get("value")),
            "unit": str(item.get("unit") or ""),
        }
        for score, item in scored[:4]
        if score > 0
    ]
    return (scored[0][0] if scored else 0.0), evidence


def _sqtt_score(mid: str, meta: dict[str, Any], hcu_top: dict[str, Any]) -> tuple[float, list[dict[str, Any]]]:
    sqtt = hcu_top.get("sqtt_analysis") or {}
    if not isinstance(sqtt, dict) or sqtt.get("error"):
        return 0.0, []
    if not any(
        sqtt.get(key)
        for key in (
            "file_count",
            "csv_row_count",
            "trace_event_count",
            "instruction_count",
            "waitcnt_count",
            "branch_count",
            "stall_like_hits",
            "category_counts",
        )
    ):
        return 0.0, []

    trigger = f"{mid} {meta.get('trigger_metric', '')} {meta.get('name', '')}".lower()
    score = 0.0
    evidence: list[dict[str, Any]] = []

    waitcnt = _safe_float(sqtt.get("waitcnt_count"))
    if waitcnt > 0 and any(token in trigger for token in ("wait", "stall", "latency", "pipeline")):
        score = max(score, 0.78)
        evidence.append({"metric": "sqtt.waitcnt_count", "value": waitcnt, "unit": "count"})

    stall_hits = sqtt.get("stall_like_hits") or []
    if isinstance(stall_hits, list) and stall_hits and any(token in trigger for token in ("wait", "stall", "latency", "issue")):
        score = max(score, 0.72)
        evidence.append({"metric": "sqtt.stall_like_hits", "value": float(len(stall_hits)), "unit": "sites"})

    branch_count = _safe_float(sqtt.get("branch_count"))
    if branch_count > 0 and any(token in trigger for token in ("branch", "scheduler", "issue", "loop", "ilp")):
        score = max(score, 0.55)
        evidence.append({"metric": "sqtt.branch_count", "value": branch_count, "unit": "count"})

    categories = sqtt.get("category_counts") or {}
    if isinstance(categories, dict):
        lds_count = _safe_float(categories.get("lds"))
        vmem_count = _safe_float(categories.get("vmem"))
        matrix_count = _safe_float(categories.get("matrix"))
        if lds_count > 0 and any(token in trigger for token in ("lds", "bank", "matrix-read", "matrix_load")):
            score = max(score, 0.50)
            evidence.append({"metric": "sqtt.category.lds", "value": lds_count, "unit": "inst"})
        if vmem_count > 0 and any(token in trigger for token in ("global", "tcc", "cache", "vector", "coalesced")):
            score = max(score, 0.45)
            evidence.append({"metric": "sqtt.category.vmem", "value": vmem_count, "unit": "inst"})
        if matrix_count <= 0 and "mmac" in trigger and (categories or _safe_float(sqtt.get("instruction_count")) > 0):
            score = max(score, 0.35)
            evidence.append({"metric": "sqtt.category.matrix", "value": matrix_count, "unit": "inst"})

    return score, evidence[:4]


def _codeobj_score(mid: str, meta: dict[str, Any], hcu_top: dict[str, Any]) -> tuple[float, list[dict[str, Any]]]:
    codeobj = hcu_top.get("codeobj_analyze") or {}
    if not isinstance(codeobj, dict):
        return 0.0, []
    flags = {str(item) for item in codeobj.get("pressure_flags") or []}
    trigger = f"{mid} {meta.get('trigger_metric', '')} {meta.get('name', '')}".lower()
    score = 0.0
    evidence: list[dict[str, Any]] = []

    if flags and any(token in trigger for token in ("vgpr", "sgpr", "occupancy", "register", "salu", "valu")):
        score = max(score, 0.82 if "register_pressure" in mid else 0.55)
        if "high_vgpr" in flags and codeobj.get("max_vgpr") is not None:
            evidence.append({"metric": "codeobj.max_vgpr", "value": _safe_float(codeobj.get("max_vgpr")), "unit": "regs"})
        if "high_sgpr" in flags and codeobj.get("max_sgpr") is not None:
            evidence.append({"metric": "codeobj.max_sgpr", "value": _safe_float(codeobj.get("max_sgpr")), "unit": "regs"})

    if codeobj.get("max_lds") is not None and any(token in trigger for token in ("lds", "matrix_load", "bank")):
        lds = _safe_float(codeobj.get("max_lds"))
        if lds > 0:
            score = max(score, 0.35)
            evidence.append({"metric": "codeobj.max_lds", "value": lds, "unit": "bytes"})

    return score, evidence[:4]


def _method_evidence_score(
    mid: str,
    meta: dict[str, Any],
    *,
    roofline: dict[str, Any],
    hcu_top: dict[str, Any],
) -> dict[str, Any]:
    axis = str(meta.get("axis") or "")
    axis_score, axis_evidence = _roofline_axis_score(axis, roofline) if axis in AXES else (0.0, [])
    metric_score, metric_evidence = _metric_trigger_score(meta, hcu_top)
    sqtt_score, sqtt_evidence = _sqtt_score(mid, meta, hcu_top)
    codeobj_score, codeobj_evidence = _codeobj_score(mid, meta, hcu_top)

    trigger_score = max(metric_score, sqtt_score, codeobj_score)
    if trigger_score <= 0 and str(meta.get("trigger_direction") or "") == "manual" and axis_score > 0:
        trigger_score = min(0.40, axis_score * 0.50)

    # Axis severity says whether this axis deserves attention; trigger evidence
    # says which method inside that axis deserves the branch slot.
    if axis_score > 0 and trigger_score > 0:
        score = 0.35 * axis_score + 0.65 * trigger_score
    elif axis_score > 0:
        score = 0.20 * axis_score
    else:
        score = 0.0

    evidence = axis_evidence + metric_evidence + sqtt_evidence + codeobj_evidence
    deduped: list[dict[str, Any]] = []
    seen = set()
    for item in evidence:
        key = (item.get("metric"), item.get("unit"))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return {
        "score": _clamp01(score),
        "trigger_strength": _clamp01(max(trigger_score, score if hcu_top.get("degraded") else 0.0)),
        "axis_score": axis_score,
        "metric_score": metric_score,
        "sqtt_score": sqtt_score,
        "codeobj_score": codeobj_score,
        "evidence": deduped[:8],
    }


def _expected_metric_shift(meta: dict[str, Any]) -> str:
    trigger = str(meta.get("trigger_metric") or "")
    direction = str(meta.get("trigger_direction") or "")
    if not trigger or direction == "manual":
        return "Expected shift must be confirmed by hipprof/SQTT/dccobjdump for this manual method."
    if direction == "high_is_bad":
        return f"Expect lower `{trigger}` or reduced related stall/memory pressure after the branch."
    if direction == "low_is_bad":
        return f"Expect higher effective `{trigger}` or improved occupancy/utilization after the branch."
    return f"Expect measurable movement in `{trigger}` after the branch."


def _would_violate_coupled(mid: str, chosen_ids: set[str], registry: dict[str, Any]) -> bool:
    for pair in registry.get("coupled_methods", []):
        ids = {str(item) for item in pair.get("ids", [])}
        if mid in ids and ids.intersection(chosen_ids):
            return True
    return False


def _skip_reason_for_candidate(
    mid: str,
    meta: dict[str, Any],
    *,
    selected_ids: set[str],
    ineffective_ids: set[str],
    impl_failed_ids: set[str],
    detected_arch: int,
    features: set[str],
) -> str:
    if mid in selected_ids:
        return "already_selected"
    if mid in impl_failed_ids or mid in ineffective_ids:
        return "skip_condition"
    if not _is_arch_compatible(meta, detected_arch):
        return "arch_incompatible"
    if _missing_required_features(meta, features):
        return "feature_unavailable"
    return ""


def _candidate_capability_adjustment(mid: str, meta: dict[str, Any], capability: dict[str, Any]) -> tuple[float, str]:
    """Bias method selection toward methods that can produce real branches.

    Direct profiler/roofline evidence still matters most. This adjustment only
    prevents the automatic loop from spending branch slots on methods that are
    theoretically valid but have no safe generator for the recognized contract.
    """
    family = str(capability.get("family") or "unknown")
    actionable = set(str(item) for item in capability.get("actionable_method_ids", []) or [])
    discouraged = set(str(item) for item in capability.get("discouraged_method_ids", []) or [])
    axis = str(meta.get("axis") or "")
    boost = 0.0
    note = ""

    if mid in actionable:
        boost = 0.55 if family != "generic" else 0.20
        note = f"branch_generator_available:{family}"
    elif mid in discouraged:
        boost = -0.45
        note = f"not_actionable_for_contract:{family}"
    elif family in {"flat_elementwise", "flat_copy"} and mid in MATRIX_SPECIFIC_METHODS:
        boost = -0.55
        note = f"matrix_method_blocked_for:{family}"
    elif family == "matmul" and mid in {
        "compute.mmac_tensor_core",
        "memory.global_to_lds_async",
        "memory.matrix_load_mls",
        "memory.ds_read_matrix_layout",
        "memory.ck_tile_named_pipeline",
    }:
        if not bool(capability.get("ck_tile_ready")):
            boost = -0.35
            note = "ck_tile_or_mmac_generator_not_ready"
    elif family in {
        "flat_copy",
        "flat_elementwise",
        "flat_scale",
        "flat_axpy",
        "flat_reduction_sum",
        "matmul",
        "gather",
        "scatter",
        "index_add",
        "softmax",
        "layernorm",
    } and actionable and mid not in actionable:
        boost = -0.30
        note = f"no_specialized_generator_for_contract:{family}"
    elif family == "generic" and axis in AXES:
        boost = 0.05
        note = "generic_transform_available"
    return boost, note


def _score_with_capability(scored: dict[str, Any], boost: float) -> tuple[float, float]:
    base = float(scored.get("score", 0.0) or 0.0)
    trigger = float(scored.get("trigger_strength", 0.0) or 0.0)
    return _clamp01(base + boost), _clamp01(max(trigger, base + max(boost, 0.0)))


def _method_record(
    *,
    mid: str,
    meta: dict[str, Any],
    axis: str,
    scored: dict[str, Any],
    score_for_selection: float,
    trigger_strength: float,
    skipped_higher: list[dict[str, Any]],
    capability_note: str,
    fallback: bool,
) -> dict[str, Any]:
    evidence = list(scored.get("evidence", []) or [])
    if capability_note:
        evidence.append({"metric": "branch_generator_capability", "value": 1.0, "unit": capability_note})
    selection_kind = "fallback for" if fallback else "for"
    description = (
        "Selected by evidence-driven auto optimizer "
        f"{selection_kind} `{axis}` axis. Roofline delta={scored['axis_score']:.2f}; "
        f"raw_score={float(scored.get('score', 0.0)):.2f}; "
        f"selection_score={score_for_selection:.2f}; "
        f"trigger_strength={trigger_strength:.2f}. Branch generator will emit "
        "contract-aware HIP source variants plus an optional no-op fallback."
    )
    return {
        "id": mid,
        "name": str(meta.get("name", mid)),
        "axis": axis,
        "priority": int(meta.get("priority", 99)),
        "description": description,
        "skipped_higher": skipped_higher,
        "hcu_evidence": evidence[:10],
        "trigger_strength": round(trigger_strength, 4),
        "selection_score": round(score_for_selection, 4),
        "generator_capability": capability_note,
        "expected_metric_shift": _expected_metric_shift(meta),
    }


def _select_methods(
    state: dict[str, Any],
    registry: dict[str, Any],
    axis_budget: dict[str, int],
    *,
    roofline: dict[str, Any],
    hcu_top: dict[str, Any],
    selection_policy: str,
    generator_capability: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    methods = registry.get("methods", {})
    selected_ids = {str(item.get("id", "")) for item in state.get("selected_methods", [])}
    ineffective_ids = {str(item.get("id", "")) for item in state.get("ineffective_methods", [])}
    impl_failed_ids = {str(item.get("id", "")) for item in state.get("implementation_failed_methods", [])}
    detected_arch = _parse_gfx_arch(state)
    features = _available_features(state, registry)
    capability = generator_capability or {"family": "generic", "actionable_method_ids": []}
    picked: list[dict[str, Any]] = []

    for axis in AXES:
        needed = int(axis_budget.get(axis, 0) or 0)
        if needed <= 0:
            continue
        candidates: list[dict[str, Any]] = []
        scored_candidates: dict[str, dict[str, Any]] = {}
        for mid, meta in methods.items():
            if meta.get("axis") != axis:
                continue
            skip_reason = _skip_reason_for_candidate(
                mid,
                meta,
                selected_ids=selected_ids,
                ineffective_ids=ineffective_ids,
                impl_failed_ids=impl_failed_ids,
                detected_arch=detected_arch,
                features=features,
            )
            if skip_reason:
                continue
            scored = _method_evidence_score(mid, meta, roofline=roofline, hcu_top=hcu_top)
            cap_boost, cap_note = _candidate_capability_adjustment(mid, meta, capability)
            selection_score, selection_trigger = _score_with_capability(scored, cap_boost)
            scored["capability_boost"] = round(cap_boost, 4)
            scored["capability_note"] = cap_note
            scored["selection_score"] = selection_score
            scored["selection_trigger_strength"] = selection_trigger
            scored_candidates[mid] = scored
            priority = int(meta.get("priority", 99))
            if selection_policy == "priority":
                rank = (0, priority)
            else:
                # Evidence first, then registry priority as a stable tie-break.
                # Low/no-trigger methods are allowed only as fallback when an
                # axis has budget but no method is directly triggered.
                rank = (-float(scored["selection_score"]), priority)
            candidates.append({"id": mid, "meta": meta, "score": scored, "priority": priority, "rank": rank})
        candidates.sort(key=lambda item: item["rank"])
        axis_count = 0
        triggered = [item for item in candidates if float(item["score"].get("selection_score", 0.0)) >= TRIGGER_THRESHOLD]
        pool = candidates if selection_policy == "priority" else triggered if len(triggered) >= needed else candidates
        for item in pool:
            if axis_count >= needed:
                break
            mid = item["id"]
            meta = item["meta"]
            if _would_violate_coupled(mid, {str(m["id"]) for m in picked}, registry):
                continue
            scored = item["score"]
            priority = int(meta.get("priority", 99))
            score_for_selection = float(scored.get("selection_score", scored.get("score", 0.0)))
            trigger_strength = float(scored.get("selection_trigger_strength", scored.get("trigger_strength", 0.0)))
            if selection_policy == "priority" and trigger_strength <= 0:
                trigger_strength = float(scored.get("score", 0.0))
            picked.append(
                _method_record(
                    mid=mid,
                    meta=meta,
                    axis=axis,
                    scored=scored,
                    score_for_selection=score_for_selection,
                    trigger_strength=trigger_strength,
                    skipped_higher=_skipped_higher(
                        methods,
                        axis=axis,
                        selected_priority=priority,
                        selected_score=score_for_selection,
                        selected_ids=selected_ids,
                        ineffective_ids=ineffective_ids,
                        impl_failed_ids=impl_failed_ids,
                        detected_arch=detected_arch,
                        features=features,
                        scored_candidates=scored_candidates,
                    ),
                    capability_note=str(scored.get("capability_note") or ""),
                    fallback=False,
                )
            )
            axis_count += 1
        if axis_count < needed and pool is not candidates:
            for item in candidates:
                if axis_count >= needed:
                    break
                mid = item["id"]
                if mid in {str(m["id"]) for m in picked}:
                    continue
                if _would_violate_coupled(mid, {str(m["id"]) for m in picked}, registry):
                    continue
                meta = item["meta"]
                scored = item["score"]
                priority = int(meta.get("priority", 99))
                trigger_strength = float(scored.get("selection_trigger_strength", scored.get("trigger_strength", 0.0)))
                score_for_selection = float(scored.get("selection_score", scored.get("score", 0.0)))
                picked.append(
                    _method_record(
                        mid=mid,
                        meta=meta,
                        axis=axis,
                        scored=scored,
                        score_for_selection=score_for_selection,
                        trigger_strength=trigger_strength,
                        skipped_higher=_skipped_higher(
                            methods,
                            axis=axis,
                            selected_priority=priority,
                            selected_score=score_for_selection,
                            selected_ids=selected_ids,
                            ineffective_ids=ineffective_ids,
                            impl_failed_ids=impl_failed_ids,
                            detected_arch=detected_arch,
                            features=features,
                            scored_candidates=scored_candidates,
                        ),
                        capability_note=str(scored.get("capability_note") or ""),
                        fallback=True,
                    )
                )
                axis_count += 1
        if axis_count < needed:
            raise SystemExit(f"cannot select {needed} methods for axis {axis}; selected {axis_count}")
    return picked


def _kernel_source_path(state: dict[str, Any]) -> Path:
    for key in ("best_file", "baseline_file"):
        value = str(state.get(key, "") or "")
        if value:
            path = Path(value).expanduser().resolve()
            if path.is_file():
                return path
    raise SystemExit("state has no existing best_file/baseline_file")


def _source_is_transformable(src: Path) -> bool:
    if src.suffix.lower() not in {".hip", ".cu", ".cpp", ".cc", ".cxx"}:
        return False
    try:
        text = src.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return "__global__" in text or 'extern "C" void solve' in text


def _load_family_catalog(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"families": {}}
    return _read_json(path)


def _flatten_evidence_text(*objects: Any) -> str:
    chunks: list[str] = []

    def visit(value: Any) -> None:
        if value is None:
            return
        if isinstance(value, str):
            chunks.append(value)
            return
        if isinstance(value, (int, float, bool)):
            chunks.append(str(value))
            return
        if isinstance(value, dict):
            for key, item in value.items():
                chunks.append(str(key))
                visit(item)
            return
        if isinstance(value, list):
            for item in value:
                visit(item)

    for obj in objects:
        visit(obj)
    return " ".join(chunks).lower()


def _family_match_score(family_id: str, family_meta: dict[str, Any], evidence_text: str) -> tuple[float, list[str]]:
    terms = list(COMPLEX_FAMILY_TRIGGER_TERMS.get(family_id, []))
    terms.extend(str(item).lower() for item in family_meta.get("aliases", []) or [])
    matched: list[str] = []
    score = 0.0
    for term in terms:
        normalized = str(term).strip().lower()
        if not normalized:
            continue
        if normalized in evidence_text:
            if normalized not in matched:
                matched.append(normalized)
            score += 1.0 if len(normalized) >= 5 else 0.5
    return min(score, 10.0), matched[:16]


def _build_kernel_family_guidance(
    *,
    catalog: dict[str, Any],
    state: dict[str, Any],
    roofline: dict[str, Any],
    hcu_top: dict[str, Any],
    generator_capability: dict[str, Any],
) -> dict[str, Any]:
    families = catalog.get("families", {}) if isinstance(catalog, dict) else {}
    if not isinstance(families, dict) or not families:
        return {
            "status": "catalog_missing",
            "catalog_version": catalog.get("$version", "") if isinstance(catalog, dict) else "",
            "matched_families": [],
            "primary_family": "",
            "agent_guidance": [],
        }

    src = _kernel_source_path(state)
    source_text = ""
    if src.is_file() and src.suffix.lower() in {".hip", ".cu", ".cpp", ".cc", ".cxx", ".py"}:
        try:
            source_text = src.read_text(encoding="utf-8", errors="ignore")[:200000]
        except OSError:
            source_text = ""
    evidence_text = _flatten_evidence_text(
        src.name,
        str(src),
        source_text,
        state.get("dims", {}),
        state.get("hotspot", {}),
        state.get("operator_contract", {}),
        state.get("kernel_handoff_manifest", {}),
        roofline,
        hcu_top,
        generator_capability,
    )

    matched: list[dict[str, Any]] = []
    generator_family = str(generator_capability.get("family") or "")
    for family_id, family_meta in families.items():
        if not isinstance(family_meta, dict):
            continue
        score, terms = _family_match_score(str(family_id), family_meta, evidence_text)
        aliases = {str(item).lower() for item in family_meta.get("aliases", []) or []}
        if generator_family and (generator_family == family_id or generator_family.lower() in aliases):
            score += 3.0
            terms = sorted(set(terms + [f"generator:{generator_family}"]))
        if score <= 0:
            continue
        matched.append(
            {
                "family": str(family_id),
                "priority": int(family_meta.get("priority", 99)),
                "score": round(score, 4),
                "matched_terms": terms,
                "scope": family_meta.get("scope", ""),
                "required_contract_fields": family_meta.get("required_contract_fields", []),
                "candidate_methods": family_meta.get("candidate_methods", []),
                "branch_generator_plan": family_meta.get("branch_generator_plan", []),
                "correctness_gates": family_meta.get("correctness_gates", []),
                "semantic_traps": family_meta.get("semantic_traps", []),
                "stop_reasons": family_meta.get("stop_reasons", []),
                "library_references": family_meta.get("library_references", []),
            }
        )
    matched.sort(key=lambda item: (-float(item["score"]), int(item["priority"]), str(item["family"])))
    primary = matched[0] if matched else {}
    guidance = []
    if primary:
        guidance = [
            f"Treat `{primary['family']}` as the primary complex family before adding unsafe generic rewrites.",
            "Capture or confirm the listed contract fields before model integration.",
            "Run the listed correctness gates before accepting a branch into the project.",
            "Use stop_reasons to switch targets when profile/e2e evidence shows low remaining upside.",
        ]
    else:
        guidance = [
            "No P0 complex family matched. Continue with generator_capability and method registry, but record new reusable experience if agent finds a recurring family."
        ]
    return {
        "status": "matched" if matched else "no_match",
        "catalog_version": catalog.get("$version", ""),
        "source": str(src),
        "primary_family": primary.get("family", ""),
        "matched_families": matched[:5],
        "agent_guidance": guidance,
        "policy": "advisory_only_agent_must_review",
    }


def _add_restrict_pointers(text: str) -> tuple[str, bool]:
    ptr_types = (
        r"(?:const\s+)?(?:float|double|int|long|short|char|"
        r"unsigned\s+char|unsigned\s+short|unsigned\s+int)\s*\*"
    )
    pattern = re.compile(rf"\b({ptr_types})\s*(?!__restrict__)([A-Za-z_]\w*)")

    def repl(match: re.Match[str]) -> str:
        prefix = match.group(1)
        name = match.group(2)
        # Avoid duplicating restrict when the local text already has it in a
        # spacing form the regex did not catch.
        local = match.group(0)
        if "__restrict__" in local or "restrict" in local:
            return local
        return f"{prefix} __restrict__ {name}"

    new_text, count = pattern.subn(repl, text)
    return new_text, count > 0


def _add_unroll_pragmas(text: str, *, limit: int = 4) -> tuple[str, bool]:
    lines = text.splitlines()
    out: list[str] = []
    inserted = 0
    for line in lines:
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]
        if inserted < limit and stripped.startswith("for ") or (inserted < limit and stripped.startswith("for(")):
            previous = next((candidate.strip() for candidate in reversed(out) if candidate.strip()), "")
            if "#pragma unroll" not in previous:
                out.append(f"{indent}#pragma unroll")
                inserted += 1
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), inserted > 0


def _add_launch_bounds(text: str, bound: int) -> tuple[str, bool]:
    pattern = re.compile(r"__global__(\s+)(?!__launch_bounds__)(void\s+)")
    new_text, count = pattern.subn(rf"__global__\1__launch_bounds__({bound}) \2", text, count=1)
    return new_text, count > 0


def _replace_block_dim(text: str, variant: str) -> tuple[str, bool]:
    pattern = re.compile(r"\bdim3\s+block\s*\(([^)]*)\)\s*;")
    match = pattern.search(text)
    if not match:
        return text, False
    raw = match.group(1)
    parts = [part.strip() for part in raw.split(",")]
    if not parts or not all(re.fullmatch(r"\d+", part) for part in parts):
        return text, False
    if len(parts) >= 2:
        replacements = {
            "block_32x8": "32, 8",
            "block_8x32": "8, 32",
            "block_16x8": "16, 8",
            "block_8x16": "8, 16",
        }
    else:
        replacements = {
            "block_64": "64",
            "block_128": "128",
            "block_256": "256",
        }
    new_args = replacements.get(variant)
    if not new_args or new_args == raw:
        return text, False
    start, end = match.span(1)
    return text[:start] + new_args + text[end:], True


def _solve_signature_text(text: str) -> str:
    match = re.search(r'extern\s+"C"\s+void\s+solve\s*\(([\s\S]*?)\)\s*\{', text)
    return match.group(1) if match else ""


def _clean_param_token(token: str) -> str:
    token = re.sub(r"/\*.*?\*/", "", token, flags=re.S)
    token = re.sub(r"//[^\n]*", "", token)
    token = re.sub(r"\b__restrict__\b|\b__restrict\b|\brestrict\b", "", token)
    return " ".join(token.split())


def _parse_solve_params(text: str) -> list[dict[str, Any]]:
    signature = _solve_signature_text(text)
    if not signature:
        return []
    params: list[dict[str, Any]] = []
    for raw in signature.split(","):
        token = _clean_param_token(raw)
        if not token:
            continue
        is_const = bool(re.search(r"\bconst\b", token))
        clean = re.sub(r"\bconst\b", "", token).strip()
        ptr = re.match(
            r"(?P<type>float|double|int|long|short|char|unsigned\s+char|unsigned\s+short|unsigned\s+int)\s*\*\s*(?P<name>[A-Za-z_]\w*)$",
            clean,
        )
        if ptr:
            params.append({"kind": "ptr", "type": " ".join(ptr.group("type").split()), "name": ptr.group("name"), "is_const": is_const})
            continue
        scalar = re.match(r"(?P<type>float|double|int|long|size_t|unsigned\s+int)\s+(?P<name>[A-Za-z_]\w*)$", clean)
        if scalar:
            params.append({"kind": "scalar", "type": scalar.group("type"), "name": scalar.group("name"), "is_const": False})
            continue
        params.append({"kind": "unknown", "raw": raw.strip(), "name": ""})
    return params


def _dtype_kind(dtype: str) -> str:
    normalized = " ".join(str(dtype).split())
    if normalized in {"float", "double"}:
        return "floating"
    if normalized in {"int", "long", "short", "char", "unsigned char", "unsigned short", "unsigned int"}:
        return "integer"
    return "unknown"


def _compact_source(text: str) -> str:
    return re.sub(r"\s+", "", text)


def _detect_matmul_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if not all(name in dims for name in ("M", "N", "K")):
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if len(const_ptrs) < 2 or len(out_ptrs) < 1:
        return None
    if not all(name in scalars for name in ("M", "N", "K")):
        return None
    dtype = str(const_ptrs[0]["type"])
    if dtype not in {"float", "double"}:
        return None
    if any(str(item["type"]) != dtype for item in const_ptrs[:2] + out_ptrs[:1]):
        return None
    # Require a recognizable M/N/K matmul access pattern before replacing the
    # whole source. This avoids rewriting arbitrary three-tensor kernels.
    compact = re.sub(r"\s+", "", text)
    a, b, out = const_ptrs[0]["name"], const_ptrs[1]["name"], out_ptrs[0]["name"]
    if f"{a}[row*K+k]" not in compact or f"{b}[k*N+col]" not in compact or f"{out}[row*N+col]" not in compact:
        return None
    return {
        "params": params,
        "dtype": dtype,
        "a": a,
        "b": b,
        "out": out,
        "m": "M",
        "n": "N",
        "k": "K",
    }


def _detect_flat_elementwise_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if "N" not in dims:
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if "N" not in scalars or len(const_ptrs) < 1 or len(out_ptrs) != 1:
        return None
    dtype = str(out_ptrs[0]["type"])
    if dtype not in {"float", "double"}:
        return None
    if any(str(item["type"]) != dtype for item in ptrs):
        return None
    compact = re.sub(r"\s+", "", text)
    out_name = out_ptrs[0]["name"]
    if f"{out_name}[i]=" not in compact and f"{out_name}[idx]=" not in compact:
        return None
    if not any(f"{item['name']}[i]" in compact or f"{item['name']}[idx]" in compact for item in const_ptrs):
        return None
    rhs = ""
    index_name = "i"
    assign_re = re.compile(rf"\b{re.escape(out_name)}\s*\[\s*(i|idx)\s*\]\s*=\s*([^;]+);")
    match = assign_re.search(text)
    if match:
        index_name = match.group(1)
        rhs = match.group(2).strip()
    if not rhs:
        return None
    # Keep the source expression only when it references the same flat index
    # and does not contain obvious control-flow or side-effect constructs.
    if any(token in rhs for token in ("=", "++", "--", "?", ":", "{", "}")):
        return None
    if index_name != "i":
        rhs = re.sub(rf"\b{re.escape(index_name)}\b", "i", rhs)
    return {"params": params, "dtype": dtype, "inputs": const_ptrs, "out": out_ptrs[0], "n": "N", "rhs": rhs}


def _detect_flat_copy_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    contract = _detect_flat_elementwise_contract(text, state)
    if not contract or len(contract["inputs"]) != 1:
        return None
    src = contract["inputs"][0]["name"]
    rhs = re.sub(r"\s+", "", str(contract.get("rhs") or ""))
    if rhs != f"{src}[i]":
        return None
    return contract


def _flat_rhs_input_names(rhs: str, inputs: list[dict[str, Any]]) -> set[str]:
    return {str(item["name"]) for item in inputs if re.search(rf"\b{re.escape(str(item['name']))}\s*\[\s*i\s*\]", rhs)}


def _is_flat_linear_rhs(rhs: str, inputs: list[dict[str, Any]]) -> bool:
    names = _flat_rhs_input_names(rhs, inputs)
    if not names or len(names) > 3:
        return False
    stripped = rhs
    for name in names:
        stripped = re.sub(rf"\b{re.escape(name)}\s*\[\s*i\s*\]", "X", stripped)
    for fn in FLAT_SAFE_FUNCTIONS:
        stripped = stripped.replace(fn, "F")
    return not bool(re.search(r"[^A-Za-z0-9_\[\]\(\)\+\-\*/\., fF]", stripped))


def _detect_flat_axpy_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    contract = _detect_flat_elementwise_contract(text, state)
    if not contract or len(contract["inputs"]) < 2:
        return None
    rhs = str(contract.get("rhs") or "")
    names = _flat_rhs_input_names(rhs, contract["inputs"])
    if len(names) < 2 or not _is_flat_linear_rhs(rhs, contract["inputs"]):
        return None
    contract = dict(contract)
    contract["family"] = "flat_axpy"
    contract["rhs_input_names"] = sorted(names)
    return contract


def _detect_flat_scale_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    contract = _detect_flat_elementwise_contract(text, state)
    if not contract or len(contract["inputs"]) != 1:
        return None
    rhs = str(contract.get("rhs") or "")
    src = contract["inputs"][0]["name"]
    if re.sub(r"\s+", "", rhs) == f"{src}[i]":
        return None
    if not _is_flat_linear_rhs(rhs, contract["inputs"]):
        return None
    contract = dict(contract)
    contract["family"] = "flat_scale"
    return contract


def _detect_flat_reduction_sum_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if "N" not in dims:
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if "N" not in scalars or len(const_ptrs) != 1 or len(out_ptrs) != 1:
        return None
    if str(const_ptrs[0].get("type")) != str(out_ptrs[0].get("type")) or str(out_ptrs[0].get("type")) not in {"float", "double"}:
        return None
    compact = re.sub(r"\s+", "", text)
    src = const_ptrs[0]["name"]
    out = out_ptrs[0]["name"]
    has_sum_loop = f"{src}[i]" in compact and ("sum+=" in compact or "acc+=" in compact)
    has_output0 = f"{out}[0]=" in compact or f"atomicAdd({out}" in compact
    if not has_sum_loop or not has_output0:
        return None
    return {"params": params, "dtype": out_ptrs[0]["type"], "inputs": const_ptrs, "out": out_ptrs[0], "n": "N", "family": "flat_reduction_sum"}


def _detect_flat_fill_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if "N" not in dims:
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if "N" not in scalars or len(out_ptrs) != 1:
        return None
    dtype = str(out_ptrs[0].get("type"))
    if dtype not in {"float", "double", "int", "long", "unsigned char"}:
        return None
    out_name = str(out_ptrs[0]["name"])
    assign_re = re.compile(rf"\b{re.escape(out_name)}\s*\[\s*(i|idx)\s*\]\s*=\s*([^;]+);")
    match = assign_re.search(text)
    if not match:
        return None
    rhs = match.group(2).strip()
    ptr_names = {str(item.get("name")) for item in ptrs}
    if any(re.search(rf"\b{re.escape(name)}\s*\[", rhs) for name in ptr_names):
        return None
    if any(token in rhs for token in ("++", "--", "?", ":", "{", "}")):
        return None
    if not re.fullmatch(r"[A-Za-z_]\w*|[-+]?\d+(?:\.\d+)?(?:f)?", rhs.replace(" ", "")):
        return None
    return {
        "family": "flat_fill",
        "params": params,
        "dtype": dtype,
        "out": out_ptrs[0],
        "n": "N",
        "value_expr": rhs,
    }


def _detect_row_reduction_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if not {"M", "N"}.issubset(dims):
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if len(const_ptrs) != 1 or len(out_ptrs) != 1 or not {"M", "N"}.issubset(scalars):
        return None
    dtype = str(const_ptrs[0].get("type"))
    if dtype != str(out_ptrs[0].get("type")) or dtype not in {"float", "double"}:
        return None
    compact = _compact_source(text)
    src = str(const_ptrs[0]["name"])
    out = str(out_ptrs[0]["name"])
    if f"{src}[row*N+" not in compact or f"{out}[row]" not in compact:
        return None
    op = ""
    if any(token in compact for token in ("fmaxf(", "max(", "local_max", "acc=fmax", "acc=max")):
        op = "max"
    elif "sum+=" in compact or "acc+=" in compact or "local_sum" in compact:
        op = "sum"
    if not op:
        return None
    return {
        "family": f"row_reduction_{op}",
        "params": params,
        "dtype": dtype,
        "src": const_ptrs[0],
        "out": out_ptrs[0],
        "m": "M",
        "n": "N",
        "op": op,
    }


def _detect_row_top1_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if not {"M", "N"}.issubset(dims):
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if len(const_ptrs) != 1 or len(out_ptrs) < 1 or not {"M", "N"}.issubset(scalars):
        return None
    value = const_ptrs[0]
    index_out = next((item for item in out_ptrs if _dtype_kind(str(item.get("type"))) == "integer"), None)
    value_out = next((item for item in out_ptrs if str(item.get("type")) == str(value.get("type")) and _dtype_kind(str(item.get("type"))) == "floating"), None)
    if index_out is None:
        return None
    compact = _compact_source(text)
    src_name = str(value["name"])
    idx_out_name = str(index_out["name"])
    if f"{src_name}[row*N+" not in compact or f"{idx_out_name}[row]" not in compact:
        return None
    if not any(token in compact for token in ("best", "argmax", "max_idx", "maxidx", ">")):
        return None
    return {
        "family": "row_top1",
        "params": params,
        "dtype": str(value.get("type")),
        "src": value,
        "index_out": index_out,
        "value_out": value_out,
        "m": "M",
        "n": "N",
    }


def _detect_gather_scatter_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if "N" not in dims:
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if "N" not in scalars or len(out_ptrs) != 1:
        return None
    out = out_ptrs[0]
    index_ptrs = [
        item for item in const_ptrs
        if _dtype_kind(str(item.get("type"))) == "integer"
        or re.search(r"(idx|index|indices|ids)", str(item.get("name")), re.I)
    ]
    value_ptrs = [item for item in const_ptrs if _dtype_kind(str(item.get("type"))) == "floating"]
    if not index_ptrs or not value_ptrs or str(out.get("type")) not in {"float", "double"}:
        return None
    compact = _compact_source(text)
    out_name = str(out["name"])
    for index in index_ptrs:
        idx_name = str(index["name"])
        for src in value_ptrs:
            src_name = str(src["name"])
            gather_pat = rf"{re.escape(out_name)}\[(i|idx)\]={re.escape(src_name)}\[{re.escape(idx_name)}\[(i|idx)\]\]"
            scatter_pat = rf"{re.escape(out_name)}\[{re.escape(idx_name)}\[(i|idx)\]\]={re.escape(src_name)}\[(i|idx)\]"
            index_add_pat = rf"atomicAdd\(&?{re.escape(out_name)}\[{re.escape(idx_name)}\[(i|idx)\]\],?{re.escape(src_name)}\[(i|idx)\]\)"
            plus_eq_pat = rf"{re.escape(out_name)}\[{re.escape(idx_name)}\[(i|idx)\]\]\+={re.escape(src_name)}\[(i|idx)\]"
            if re.search(gather_pat, compact):
                return {
                    "family": "gather",
                    "params": params,
                    "dtype": out["type"],
                    "src": src,
                    "indices": index,
                    "out": out,
                    "n": "N",
                }
            if re.search(index_add_pat, compact) or re.search(plus_eq_pat, compact):
                return {
                    "family": "index_add",
                    "params": params,
                    "dtype": out["type"],
                    "src": src,
                    "indices": index,
                    "out": out,
                    "n": "N",
                }
            if re.search(scatter_pat, compact):
                return {
                    "family": "scatter",
                    "params": params,
                    "dtype": out["type"],
                    "src": src,
                    "indices": index,
                    "out": out,
                    "n": "N",
                }
    return None


def _detect_softmax_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if not {"M", "N"}.issubset(dims):
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if len(const_ptrs) != 1 or len(out_ptrs) != 1 or not {"M", "N"}.issubset(scalars):
        return None
    if str(const_ptrs[0].get("type")) != "float" or str(out_ptrs[0].get("type")) != "float":
        return None
    compact = _compact_source(text)
    src, out = const_ptrs[0]["name"], out_ptrs[0]["name"]
    if "expf(" not in compact or f"{src}[row*N+" not in compact or f"{out}[row*N+" not in compact:
        return None
    if "sum" not in compact and "denom" not in compact:
        return None
    return {"family": "softmax", "params": params, "dtype": "float", "src": const_ptrs[0], "out": out_ptrs[0], "m": "M", "n": "N"}


def _detect_layernorm_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if not {"M", "N"}.issubset(dims):
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if len(const_ptrs) < 1 or len(out_ptrs) != 1 or not {"M", "N"}.issubset(scalars):
        return None
    if str(const_ptrs[0].get("type")) != "float" or str(out_ptrs[0].get("type")) != "float":
        return None
    compact = _compact_source(text)
    src, out = const_ptrs[0]["name"], out_ptrs[0]["name"]
    if f"{src}[row*N+" not in compact or f"{out}[row*N+" not in compact:
        return None
    if "rsqrtf(" not in compact and "sqrtf(" not in compact:
        return None
    if not any(token in compact for token in ("mean", "var", "sumsq")):
        return None
    gamma = next((item for item in const_ptrs[1:] if re.search(r"(gamma|weight|scale)", str(item.get("name")), re.I)), None)
    beta = next((item for item in const_ptrs[1:] if re.search(r"(beta|bias)", str(item.get("name")), re.I)), None)
    eps = next((str(item.get("name")) for item in params if item.get("kind") == "scalar" and re.search(r"(eps|epsilon)", str(item.get("name")), re.I)), "")
    return {
        "family": "layernorm",
        "params": params,
        "dtype": "float",
        "src": const_ptrs[0],
        "out": out_ptrs[0],
        "gamma": gamma,
        "beta": beta,
        "eps": eps,
        "m": "M",
        "n": "N",
    }


def _detect_flat_cast_or_scale_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    contract = _detect_flat_elementwise_contract(text, state)
    if not contract or len(contract.get("inputs", [])) < 1:
        return None
    rhs = str(contract.get("rhs") or "")
    lowered = rhs.lower()
    if not any(token in lowered for token in ("static_cast", "float(", "__half", "scale", "clamp", "min", "max")):
        return None
    out_type = str(contract.get("out", {}).get("type") or "")
    in_types = {str(item.get("type") or "") for item in contract.get("inputs", [])}
    if out_type in in_types and "scale" not in lowered and "clamp" not in lowered:
        return None
    out = dict(contract)
    out["family"] = "flat_cast_or_scale"
    return out


def _detect_2d_transpose_contract(text: str, state: dict[str, Any]) -> dict[str, Any] | None:
    dims = state.get("dims", {}) or {}
    if not {"M", "N"}.issubset(dims):
        return None
    params = _parse_solve_params(text)
    if not params or any(item.get("kind") == "unknown" for item in params):
        return None
    ptrs = [item for item in params if item.get("kind") == "ptr"]
    const_ptrs = [item for item in ptrs if item.get("is_const")]
    out_ptrs = [item for item in ptrs if not item.get("is_const")]
    scalars = {item.get("name"): item for item in params if item.get("kind") == "scalar"}
    if len(const_ptrs) != 1 or len(out_ptrs) != 1 or not {"M", "N"}.issubset(scalars):
        return None
    dtype = str(const_ptrs[0].get("type"))
    if dtype != str(out_ptrs[0].get("type")) or dtype not in {"float", "double", "int", "long", "unsigned char"}:
        return None
    compact = _compact_source(text)
    src, out = const_ptrs[0]["name"], out_ptrs[0]["name"]
    patterns = [
        f"{out}[col*M+row]={src}[row*N+col]",
        f"{out}[x*M+y]={src}[y*N+x]",
        f"{out}[j*M+i]={src}[i*N+j]",
    ]
    if not any(pattern in compact for pattern in patterns):
        return None
    return {"family": "transpose_2d", "params": params, "dtype": dtype, "src": const_ptrs[0], "out": out_ptrs[0], "m": "M", "n": "N"}


def _is_ck_tile_ready(state: dict[str, Any]) -> bool:
    ck_info = (state.get("env", {}) or {}).get("ck_tile", {}) or {}
    return bool(ck_info.get("available"))


def _detect_generator_capability(state: dict[str, Any]) -> dict[str, Any]:
    """Detect which source generators can actually be used for the current best kernel."""
    src = _kernel_source_path(state)
    capability: dict[str, Any] = {
        "source": str(src),
        "family": "generic",
        "actionable_method_ids": [
            "memory.coalesced_access",
            "compute.register_pressure_control",
            "latency.ilp_unroll",
            "latency.waitcnt_pipeline",
        ],
        "discouraged_method_ids": [],
        "specialized_generators": [],
        "ck_tile_ready": _is_ck_tile_ready(state),
        "notes": [],
    }
    if not _source_is_transformable(src):
        capability.update(
            {
                "family": "non_transformable",
                "actionable_method_ids": [],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS),
                "notes": ["source is not HIP/C++ transformable; only no-op branches are safe"],
            }
        )
        return capability

    text = src.read_text(encoding="utf-8", errors="ignore")
    row_top1_contract = _detect_row_top1_contract(text, state)
    if row_top1_contract:
        capability.update(
            {
                "family": "topk_sort_selection",
                "actionable_method_ids": [
                    "memory.coalesced_access",
                    "compute.thread_coarsening",
                    "compute.register_pressure_control",
                    "latency.reduce_barrier",
                    "latency.wavefront_shuffle_ds_bpermute",
                    "latency.ilp_unroll",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS),
                "specialized_generators": ["row_top1_block"],
            }
        )
        capability["notes"].append("row_top1 generator is only valid for exact per-row argmax/top1 contracts; full top-k ordering remains manual")
        return capability

    gather_contract = _detect_gather_scatter_contract(text, state)
    if gather_contract:
        family = str(gather_contract["family"])
        generators = {
            "gather": ["gather_coalesced", "gather_coarsened"],
            "scatter": ["scatter_coarsened"],
            "index_add": ["index_add_atomic_coarsened"],
        }[family]
        capability.update(
            {
                "family": family,
                "actionable_method_ids": sorted(INDEXING_METHODS),
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": generators,
            }
        )
        if family == "index_add":
            capability["notes"].append("index_add generator uses atomicAdd; correctness gate must validate duplicate-index semantics")
        return capability

    if _detect_softmax_contract(text, state):
        capability.update(
            {
                "family": "softmax",
                "actionable_method_ids": sorted(ROW_REDUCTION_METHODS),
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": ["softmax_row_block"],
            }
        )
        return capability

    if _detect_layernorm_contract(text, state):
        capability.update(
            {
                "family": "layernorm",
                "actionable_method_ids": sorted(ROW_REDUCTION_METHODS),
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": ["layernorm_row_block"],
            }
        )
        return capability

    row_reduction_contract = _detect_row_reduction_contract(text, state)
    if row_reduction_contract:
        capability.update(
            {
                "family": "softmax_layernorm_row_reduction",
                "actionable_method_ids": sorted(ROW_REDUCTION_METHODS),
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": [f"{row_reduction_contract['family']}_block"],
            }
        )
        capability["notes"].append("row reduction generator supports simple per-row sum/max only; compound reductions still require manual contract review")
        return capability

    if _detect_2d_transpose_contract(text, state):
        capability.update(
            {
                "family": "layout_transform_copy_pack",
                "actionable_method_ids": [
                    "memory.coalesced_access",
                    "memory.aligned_layout_transform",
                    "compute.thread_coarsening",
                    "compute.register_pressure_control",
                    "latency.ilp_unroll",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS),
                "specialized_generators": ["transpose_2d_tiled"],
            }
        )
        capability["notes"].append("2D transpose generator preserves shape/layout only for simple out[col*M+row]=src[row*N+col] contracts")
        return capability

    if _detect_flat_cast_or_scale_contract(text, state):
        capability.update(
            {
                "family": "quant_dequant_cast_pack",
                "actionable_method_ids": [
                    "memory.coalesced_access",
                    "compute.thread_coarsening",
                    "compute.register_pressure_control",
                    "latency.ilp_unroll",
                    "memory.epilogue_fusion",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS),
                "specialized_generators": ["flat_cast_or_scale_coarsened"],
            }
        )
        capability["notes"].append("cast/scale generator is only valid for flat elementwise conversion with captured rounding/saturation semantics")
        return capability

    if _detect_flat_fill_contract(text, state):
        capability.update(
            {
                "family": "layout_transform_copy_pack",
                "actionable_method_ids": [
                    "memory.coalesced_access",
                    "memory.vectorized_global_access",
                    "compute.thread_coarsening",
                    "compute.register_pressure_control",
                    "latency.ilp_unroll",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS),
                "specialized_generators": ["flat_fill_coarsened"],
            }
        )
        capability["notes"].append("flat fill generator is valid only for simple out[i]=constant/scalar fill contracts")
        return capability

    if _detect_flat_reduction_sum_contract(text, state):
        capability.update(
            {
                "family": "flat_reduction_sum",
                "actionable_method_ids": [
                    "memory.coalesced_access",
                    "compute.thread_coarsening",
                    "latency.ilp_unroll",
                    "latency.reduce_barrier",
                    "compute.register_pressure_control",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": ["flat_reduction_block_sum"],
            }
        )
        return capability

    if _detect_flat_copy_contract(text, state):
        capability.update(
            {
                "family": "flat_copy",
                "actionable_method_ids": [
                    "memory.vectorized_global_access",
                    "memory.coalesced_access",
                    "compute.thread_coarsening",
                    "compute.register_pressure_control",
                    "latency.ilp_unroll",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS),
                "specialized_generators": ["flat_copy_float4", "flat_elementwise_coarsened"],
            }
        )
        return capability

    if _detect_flat_axpy_contract(text, state):
        capability.update(
            {
                "family": "flat_axpy",
                "actionable_method_ids": [
                    "compute.thread_coarsening",
                    "memory.coalesced_access",
                    "compute.register_pressure_control",
                    "latency.ilp_unroll",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": ["flat_elementwise_coarsened", "flat_axpy_vectorized"],
            }
        )
        return capability

    if _detect_flat_scale_contract(text, state):
        capability.update(
            {
                "family": "flat_scale",
                "actionable_method_ids": [
                    "compute.thread_coarsening",
                    "memory.coalesced_access",
                    "compute.register_pressure_control",
                    "latency.ilp_unroll",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": ["flat_elementwise_coarsened"],
            }
        )
        return capability

    if _detect_flat_elementwise_contract(text, state):
        capability.update(
            {
                "family": "flat_elementwise",
                "actionable_method_ids": [
                    "compute.thread_coarsening",
                    "memory.coalesced_access",
                    "compute.register_pressure_control",
                    "latency.ilp_unroll",
                ],
                "discouraged_method_ids": list(MATRIX_SPECIFIC_METHODS | {"memory.vectorized_global_access"}),
                "specialized_generators": ["flat_elementwise_coarsened"],
            }
        )
        return capability

    if _detect_matmul_contract(text, state):
        actionable = [
            "memory.lds_tiling",
            "latency.ilp_unroll",
            "compute.register_pressure_control",
            "compute.launch_config_wave64",
        ]
        specialized = ["matmul_tiled_lds"]
        if capability["ck_tile_ready"]:
            actionable.extend(["memory.ck_tile_named_pipeline", "compute.mmac_tensor_core"])
            specialized.append("ck_tile_template")
        capability.update(
            {
                "family": "matmul",
                "actionable_method_ids": actionable,
                "discouraged_method_ids": ["memory.vectorized_global_access", "memory.cache_policy_glc_slc"],
                "specialized_generators": specialized,
            }
        )
        if not capability["ck_tile_ready"]:
            capability["notes"].append("CK Tile headers are not available; MMAC/CK Tile methods are diagnostic-only for this loop")
        return capability

    capability["notes"].append("no specialized contract detected; using generic source transforms only")
    return capability


def _param_decl(param: dict[str, Any], *, restrict_ptrs: bool) -> str:
    if param.get("kind") == "ptr":
        const = "const " if param.get("is_const") else ""
        restrict = " __restrict__" if restrict_ptrs else ""
        return f"{const}{param['type']}*{restrict} {param['name']}"
    if param.get("kind") == "scalar":
        return f"{param['type']} {param['name']}"
    return str(param.get("raw") or "")


def _matmul_tiled_source(contract: dict[str, Any], *, tile: int, unroll: bool, launch_bounds: int | None) -> str:
    dtype = contract["dtype"]
    a, b, out = contract["a"], contract["b"], contract["out"]
    m, n, kdim = contract["m"], contract["n"], contract["k"]
    params = contract["params"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    kernel_params = solve_decl
    launch_bounds_attr = f"__launch_bounds__({launch_bounds}) " if launch_bounds else ""
    unroll_line = "#pragma unroll\n            " if unroll else ""
    zero = "0.0" if dtype == "double" else "0.0f"
    return f"""#include <hip/hip_runtime.h>

#ifndef HYGON_AUTO_TILE
#define HYGON_AUTO_TILE {tile}
#endif

__global__ {launch_bounds_attr}void hygon_auto_matmul_tiled(
    {kernel_params}
) {{
    __shared__ {dtype} As[HYGON_AUTO_TILE][HYGON_AUTO_TILE + 1];
    __shared__ {dtype} Bs[HYGON_AUTO_TILE][HYGON_AUTO_TILE + 1];

    int tx = threadIdx.x;
    int ty = threadIdx.y;
    int row = blockIdx.y * HYGON_AUTO_TILE + ty;
    int col = blockIdx.x * HYGON_AUTO_TILE + tx;
    {dtype} acc = {zero};

    for (int tile_k = 0; tile_k < {kdim}; tile_k += HYGON_AUTO_TILE) {{
        int a_col = tile_k + tx;
        int b_row = tile_k + ty;
        As[ty][tx] = (row < {m} && a_col < {kdim}) ? {a}[row * {kdim} + a_col] : {zero};
        Bs[ty][tx] = (b_row < {kdim} && col < {n}) ? {b}[b_row * {n} + col] : {zero};
        __syncthreads();
        {unroll_line}for (int kk = 0; kk < HYGON_AUTO_TILE; ++kk) {{
            acc += As[ty][kk] * Bs[kk][tx];
        }}
        __syncthreads();
    }}

    if (row < {m} && col < {n}) {{
        {out}[row * {n} + col] = acc;
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(HYGON_AUTO_TILE, HYGON_AUTO_TILE);
    dim3 grid(({n} + HYGON_AUTO_TILE - 1) / HYGON_AUTO_TILE,
              ({m} + HYGON_AUTO_TILE - 1) / HYGON_AUTO_TILE);
    hygon_auto_matmul_tiled<<<grid, block>>>({call_args});
}}
"""


def _flat_elementwise_coarsened_source(contract: dict[str, Any], *, elems_per_thread: int, launch_bounds: int | None) -> str:
    dtype = contract["dtype"]
    params = contract["params"]
    n = contract["n"]
    out = contract["out"]["name"]
    rhs = str(contract.get("rhs") or "")
    if not rhs:
        raise ValueError("flat elementwise contract has no RHS expression")
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    launch_bounds_attr = f"__launch_bounds__({launch_bounds}) " if launch_bounds else ""
    return f"""#include <hip/hip_runtime.h>

#ifndef HYGON_ELEMS_PER_THREAD
#define HYGON_ELEMS_PER_THREAD {elems_per_thread}
#endif

__global__ {launch_bounds_attr}void hygon_auto_elementwise_coarsened({solve_decl}) {{
    int base = (blockIdx.x * blockDim.x + threadIdx.x) * HYGON_ELEMS_PER_THREAD;
    #pragma unroll
    for (int j = 0; j < HYGON_ELEMS_PER_THREAD; ++j) {{
        int i = base + j;
        if (i < {n}) {{
            {out}[i] = static_cast<{dtype}>({rhs});
        }}
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(256);
    dim3 grid(({n} + block.x * HYGON_ELEMS_PER_THREAD - 1) / (block.x * HYGON_ELEMS_PER_THREAD));
    hygon_auto_elementwise_coarsened<<<grid, block>>>({call_args});
}}
"""


def _flat_copy_vectorized_source(contract: dict[str, Any], *, vec: int) -> str:
    if contract["dtype"] != "float" or vec != 4:
        raise ValueError("only float4 vectorized copy is currently supported")
    params = contract["params"]
    n = contract["n"]
    src = contract["inputs"][0]["name"]
    out = contract["out"]["name"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    return f"""#include <hip/hip_runtime.h>

__global__ void hygon_auto_copy_float4({solve_decl}) {{
    int v = blockIdx.x * blockDim.x + threadIdx.x;
    int i = v * 4;
    const float4* src4 = reinterpret_cast<const float4*>({src});
    float4* out4 = reinterpret_cast<float4*>({out});
    if (i + 3 < {n}) {{
        out4[v] = src4[v];
    }} else {{
        for (int j = 0; j < 4; ++j) {{
            int idx = i + j;
            if (idx < {n}) {out}[idx] = {src}[idx];
        }}
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(256);
    dim3 grid(({n} + block.x * 4 - 1) / (block.x * 4));
    hygon_auto_copy_float4<<<grid, block>>>({call_args});
}}
"""


def _flat_copy_dual_load_source(contract: dict[str, Any]) -> str:
    if contract["dtype"] != "float":
        raise ValueError("only float dual-load copy is currently supported")
    params = contract["params"]
    n = contract["n"]
    src = contract["inputs"][0]["name"]
    out = contract["out"]["name"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    return f"""#include <hip/hip_runtime.h>

__global__ void hygon_auto_copy_two_per_thread({solve_decl}) {{
    int i = (blockIdx.x * blockDim.x + threadIdx.x) * 2;
    if (i < {n}) {{
        {out}[i] = {src}[i];
    }}
    if (i + 1 < {n}) {{
        {out}[i + 1] = {src}[i + 1];
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(256);
    dim3 grid(({n} + block.x * 2 - 1) / (block.x * 2));
    hygon_auto_copy_two_per_thread<<<grid, block>>>({call_args});
}}
"""


def _flat_axpy_vectorized_source(contract: dict[str, Any]) -> str:
    if contract["dtype"] != "float":
        raise ValueError("only float flat axpy vectorization is currently supported")
    params = contract["params"]
    n = contract["n"]
    out = contract["out"]["name"]
    rhs = str(contract.get("rhs") or "")
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    rhs_vec = rhs
    for item in contract["inputs"]:
        name = str(item["name"])
        rhs_vec = re.sub(rf"\b{re.escape(name)}\s*\[\s*i\s*\]", f"{name}[idx]", rhs_vec)
    return f"""#include <hip/hip_runtime.h>

__global__ void hygon_auto_axpy_four_per_thread({solve_decl}) {{
    int base = (blockIdx.x * blockDim.x + threadIdx.x) * 4;
    #pragma unroll
    for (int j = 0; j < 4; ++j) {{
        int idx = base + j;
        if (idx < {n}) {{
            {out}[idx] = static_cast<float>({rhs_vec});
        }}
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(256);
    dim3 grid(({n} + block.x * 4 - 1) / (block.x * 4));
    hygon_auto_axpy_four_per_thread<<<grid, block>>>({call_args});
}}
"""


def _flat_reduction_block_sum_source(contract: dict[str, Any], *, block_size: int) -> str:
    dtype = str(contract["dtype"])
    if dtype != "float":
        raise ValueError("only float reduction sum is currently supported")
    params = contract["params"]
    n = contract["n"]
    src = contract["inputs"][0]["name"]
    out = contract["out"]["name"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    return f"""#include <hip/hip_runtime.h>

#ifndef HYGON_REDUCE_BLOCK
#define HYGON_REDUCE_BLOCK {block_size}
#endif

__global__ __launch_bounds__(HYGON_REDUCE_BLOCK) void hygon_auto_reduce_sum({solve_decl}) {{
    __shared__ float smem[HYGON_REDUCE_BLOCK];
    int tid = threadIdx.x;
    int i = blockIdx.x * blockDim.x * 2 + tid;
    float acc = 0.0f;
    if (i < {n}) {{
        acc += {src}[i];
    }}
    if (i + blockDim.x < {n}) {{
        acc += {src}[i + blockDim.x];
    }}
    smem[tid] = acc;
    __syncthreads();

    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {{
        if (tid < stride) {{
            smem[tid] += smem[tid + stride];
        }}
        __syncthreads();
    }}
    if (tid == 0) {{
        atomicAdd({out}, smem[0]);
    }}
}}

extern "C" void solve({solve_decl}) {{
    hipMemset({out}, 0, sizeof(float));
    dim3 block(HYGON_REDUCE_BLOCK);
    dim3 grid(({n} + block.x * 2 - 1) / (block.x * 2));
    hygon_auto_reduce_sum<<<grid, block>>>({call_args});
}}
"""


def _indexing_coarsened_source(contract: dict[str, Any], *, elems_per_thread: int, block_size: int) -> str:
    dtype = str(contract["dtype"])
    if dtype != "float":
        raise ValueError("only float gather/scatter/index_add generators are currently supported")
    family = str(contract["family"])
    params = contract["params"]
    n = contract["n"]
    src = contract["src"]["name"]
    indices = contract["indices"]["name"]
    out = contract["out"]["name"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    if family == "gather":
        statement = f"{out}[i] = {src}[static_cast<long>({indices}[i])];"
        kernel_name = "hygon_auto_gather_coarsened"
    elif family == "scatter":
        statement = f"{out}[static_cast<long>({indices}[i])] = {src}[i];"
        kernel_name = "hygon_auto_scatter_coarsened"
    elif family == "index_add":
        statement = f"atomicAdd(&{out}[static_cast<long>({indices}[i])], {src}[i]);"
        kernel_name = "hygon_auto_index_add_atomic"
    else:
        raise ValueError(f"unsupported indexing family: {family}")
    return f"""#include <hip/hip_runtime.h>

#ifndef HYGON_INDEX_ELEMS_PER_THREAD
#define HYGON_INDEX_ELEMS_PER_THREAD {elems_per_thread}
#endif

__global__ __launch_bounds__({block_size}) void {kernel_name}({solve_decl}) {{
    int base = (blockIdx.x * blockDim.x + threadIdx.x) * HYGON_INDEX_ELEMS_PER_THREAD;
    #pragma unroll
    for (int j = 0; j < HYGON_INDEX_ELEMS_PER_THREAD; ++j) {{
        int i = base + j;
        if (i < {n}) {{
            {statement}
        }}
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block({block_size});
    dim3 grid(({n} + block.x * HYGON_INDEX_ELEMS_PER_THREAD - 1) / (block.x * HYGON_INDEX_ELEMS_PER_THREAD));
    {kernel_name}<<<grid, block>>>({call_args});
}}
"""


def _softmax_row_block_source(contract: dict[str, Any], *, block_size: int) -> str:
    params = contract["params"]
    src = contract["src"]["name"]
    out = contract["out"]["name"]
    m, n = contract["m"], contract["n"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    return f"""#include <hip/hip_runtime.h>
#include <math.h>
#include <float.h>

#ifndef HYGON_SOFTMAX_BLOCK
#define HYGON_SOFTMAX_BLOCK {block_size}
#endif

__global__ __launch_bounds__(HYGON_SOFTMAX_BLOCK) void hygon_auto_softmax_row({solve_decl}) {{
    int row = blockIdx.x;
    int tid = threadIdx.x;
    __shared__ float smem[HYGON_SOFTMAX_BLOCK];
    float local_max = -FLT_MAX;
    for (int col = tid; col < {n}; col += blockDim.x) {{
        float v = {src}[row * {n} + col];
        local_max = fmaxf(local_max, v);
    }}
    smem[tid] = local_max;
    __syncthreads();
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {{
        if (tid < stride) smem[tid] = fmaxf(smem[tid], smem[tid + stride]);
        __syncthreads();
    }}
    float max_v = smem[0];
    float local_sum = 0.0f;
    for (int col = tid; col < {n}; col += blockDim.x) {{
        local_sum += expf({src}[row * {n} + col] - max_v);
    }}
    smem[tid] = local_sum;
    __syncthreads();
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {{
        if (tid < stride) smem[tid] += smem[tid + stride];
        __syncthreads();
    }}
    float inv_sum = 1.0f / smem[0];
    for (int col = tid; col < {n}; col += blockDim.x) {{
        {out}[row * {n} + col] = expf({src}[row * {n} + col] - max_v) * inv_sum;
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(HYGON_SOFTMAX_BLOCK);
    dim3 grid({m});
    hygon_auto_softmax_row<<<grid, block>>>({call_args});
}}
"""


def _layernorm_row_block_source(contract: dict[str, Any], *, block_size: int) -> str:
    params = contract["params"]
    src = contract["src"]["name"]
    out = contract["out"]["name"]
    gamma = contract.get("gamma")
    beta = contract.get("beta")
    gamma_name = str(gamma["name"]) if isinstance(gamma, dict) else ""
    beta_name = str(beta["name"]) if isinstance(beta, dict) else ""
    eps_name = str(contract.get("eps") or "")
    eps_expr = eps_name if eps_name else "1.0e-5f"
    gamma_expr = f"{gamma_name}[col]" if gamma_name else "1.0f"
    beta_expr = f"{beta_name}[col]" if beta_name else "0.0f"
    m, n = contract["m"], contract["n"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    return f"""#include <hip/hip_runtime.h>
#include <math.h>

#ifndef HYGON_LAYERNORM_BLOCK
#define HYGON_LAYERNORM_BLOCK {block_size}
#endif

__global__ __launch_bounds__(HYGON_LAYERNORM_BLOCK) void hygon_auto_layernorm_row({solve_decl}) {{
    int row = blockIdx.x;
    int tid = threadIdx.x;
    __shared__ float smem[HYGON_LAYERNORM_BLOCK];
    float local_sum = 0.0f;
    for (int col = tid; col < {n}; col += blockDim.x) {{
        local_sum += {src}[row * {n} + col];
    }}
    smem[tid] = local_sum;
    __syncthreads();
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {{
        if (tid < stride) smem[tid] += smem[tid + stride];
        __syncthreads();
    }}
    float mean = smem[0] / static_cast<float>({n});
    float local_var = 0.0f;
    for (int col = tid; col < {n}; col += blockDim.x) {{
        float centered = {src}[row * {n} + col] - mean;
        local_var += centered * centered;
    }}
    smem[tid] = local_var;
    __syncthreads();
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {{
        if (tid < stride) smem[tid] += smem[tid + stride];
        __syncthreads();
    }}
    float inv_std = rsqrtf(smem[0] / static_cast<float>({n}) + {eps_expr});
    for (int col = tid; col < {n}; col += blockDim.x) {{
        float norm = ({src}[row * {n} + col] - mean) * inv_std;
        {out}[row * {n} + col] = norm * {gamma_expr} + {beta_expr};
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(HYGON_LAYERNORM_BLOCK);
    dim3 grid({m});
    hygon_auto_layernorm_row<<<grid, block>>>({call_args});
}}
"""


def _transpose_2d_tiled_source(contract: dict[str, Any], *, tile: int) -> str:
    dtype = str(contract["dtype"])
    params = contract["params"]
    src = contract["src"]["name"]
    out = contract["out"]["name"]
    m, n = contract["m"], contract["n"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    return f"""#include <hip/hip_runtime.h>

#ifndef HYGON_TRANSPOSE_TILE
#define HYGON_TRANSPOSE_TILE {tile}
#endif

__global__ void hygon_auto_transpose_2d({solve_decl}) {{
    __shared__ {dtype} tile[HYGON_TRANSPOSE_TILE][HYGON_TRANSPOSE_TILE + 1];
    int x = blockIdx.x * HYGON_TRANSPOSE_TILE + threadIdx.x;
    int y = blockIdx.y * HYGON_TRANSPOSE_TILE + threadIdx.y;
    if (x < {n} && y < {m}) {{
        tile[threadIdx.y][threadIdx.x] = {src}[y * {n} + x];
    }}
    __syncthreads();
    int ox = blockIdx.y * HYGON_TRANSPOSE_TILE + threadIdx.x;
    int oy = blockIdx.x * HYGON_TRANSPOSE_TILE + threadIdx.y;
    if (ox < {m} && oy < {n}) {{
        {out}[oy * {m} + ox] = tile[threadIdx.x][threadIdx.y];
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(HYGON_TRANSPOSE_TILE, HYGON_TRANSPOSE_TILE);
    dim3 grid(({n} + HYGON_TRANSPOSE_TILE - 1) / HYGON_TRANSPOSE_TILE,
              ({m} + HYGON_TRANSPOSE_TILE - 1) / HYGON_TRANSPOSE_TILE);
    hygon_auto_transpose_2d<<<grid, block>>>({call_args});
}}
"""


def _flat_cast_or_scale_source(contract: dict[str, Any], *, elems_per_thread: int, launch_bounds: int | None) -> str:
    return _flat_elementwise_coarsened_source(contract, elems_per_thread=elems_per_thread, launch_bounds=launch_bounds)


def _flat_fill_coarsened_source(contract: dict[str, Any], *, elems_per_thread: int, launch_bounds: int | None) -> str:
    dtype = str(contract["dtype"])
    params = contract["params"]
    n = contract["n"]
    out = str(contract["out"]["name"])
    value_expr = str(contract.get("value_expr") or "0")
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    launch_bounds_attr = f"__launch_bounds__({launch_bounds}) " if launch_bounds else ""
    return f"""#include <hip/hip_runtime.h>

#ifndef HYGON_FILL_ELEMS_PER_THREAD
#define HYGON_FILL_ELEMS_PER_THREAD {elems_per_thread}
#endif

__global__ {launch_bounds_attr}void hygon_auto_flat_fill({solve_decl}) {{
    int base = (blockIdx.x * blockDim.x + threadIdx.x) * HYGON_FILL_ELEMS_PER_THREAD;
    #pragma unroll
    for (int j = 0; j < HYGON_FILL_ELEMS_PER_THREAD; ++j) {{
        int i = base + j;
        if (i < {n}) {{
            {out}[i] = static_cast<{dtype}>({value_expr});
        }}
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(256);
    dim3 grid(({n} + block.x * HYGON_FILL_ELEMS_PER_THREAD - 1) / (block.x * HYGON_FILL_ELEMS_PER_THREAD));
    hygon_auto_flat_fill<<<grid, block>>>({call_args});
}}
"""


def _row_reduction_block_source(contract: dict[str, Any], *, block_size: int) -> str:
    dtype = str(contract["dtype"])
    if dtype not in {"float", "double"}:
        raise ValueError("row reduction generator supports float/double only")
    params = contract["params"]
    src = str(contract["src"]["name"])
    out = str(contract["out"]["name"])
    m, n = contract["m"], contract["n"]
    op = str(contract.get("op") or "sum")
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    zero = "-1.7976931348623157e308" if dtype == "double" and op == "max" else "-FLT_MAX" if op == "max" else "0.0"
    combine = "fmax" if dtype == "double" and op == "max" else "fmaxf" if op == "max" else ""
    update = (
        f"acc = {combine}(acc, {src}[row * {n} + col]);"
        if op == "max"
        else f"acc += {src}[row * {n} + col];"
    )
    reduce_line = (
        f"smem[tid] = {combine}(smem[tid], smem[tid + stride]);"
        if op == "max"
        else "smem[tid] += smem[tid + stride];"
    )
    include_float = "#include <float.h>\n" if op == "max" and dtype == "float" else ""
    return f"""#include <hip/hip_runtime.h>
{include_float}
#ifndef HYGON_ROW_REDUCE_BLOCK
#define HYGON_ROW_REDUCE_BLOCK {block_size}
#endif

__global__ __launch_bounds__(HYGON_ROW_REDUCE_BLOCK) void hygon_auto_row_reduce({solve_decl}) {{
    int row = blockIdx.x;
    int tid = threadIdx.x;
    __shared__ {dtype} smem[HYGON_ROW_REDUCE_BLOCK];
    {dtype} acc = static_cast<{dtype}>({zero});
    for (int col = tid; col < {n}; col += blockDim.x) {{
        {update}
    }}
    smem[tid] = acc;
    __syncthreads();
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {{
        if (tid < stride) {{
            {reduce_line}
        }}
        __syncthreads();
    }}
    if (tid == 0) {{
        {out}[row] = smem[0];
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(HYGON_ROW_REDUCE_BLOCK);
    dim3 grid({m});
    hygon_auto_row_reduce<<<grid, block>>>({call_args});
}}
"""


def _row_top1_block_source(contract: dict[str, Any], *, block_size: int) -> str:
    dtype = str(contract["dtype"])
    if dtype != "float":
        raise ValueError("row_top1 generator currently supports float scores only")
    params = contract["params"]
    src = str(contract["src"]["name"])
    index_out = str(contract["index_out"]["name"])
    value_out = str(contract["value_out"]["name"]) if isinstance(contract.get("value_out"), dict) else ""
    m, n = contract["m"], contract["n"]
    solve_decl = ", ".join(_param_decl(param, restrict_ptrs=True) for param in params)
    call_args = ", ".join(str(param["name"]) for param in params if param.get("name"))
    value_store = f"{value_out}[row] = best_v;" if value_out else ""
    return f"""#include <hip/hip_runtime.h>
#include <float.h>

#ifndef HYGON_TOP1_BLOCK
#define HYGON_TOP1_BLOCK {block_size}
#endif

__global__ __launch_bounds__(HYGON_TOP1_BLOCK) void hygon_auto_row_top1({solve_decl}) {{
    int row = blockIdx.x;
    int tid = threadIdx.x;
    __shared__ float smem_v[HYGON_TOP1_BLOCK];
    __shared__ int smem_i[HYGON_TOP1_BLOCK];
    float best_v = -FLT_MAX;
    int best_i = 0;
    for (int col = tid; col < {n}; col += blockDim.x) {{
        float v = {src}[row * {n} + col];
        if (v > best_v || (v == best_v && col < best_i)) {{
            best_v = v;
            best_i = col;
        }}
    }}
    smem_v[tid] = best_v;
    smem_i[tid] = best_i;
    __syncthreads();
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {{
        if (tid < stride) {{
            float other_v = smem_v[tid + stride];
            int other_i = smem_i[tid + stride];
            if (other_v > smem_v[tid] || (other_v == smem_v[tid] && other_i < smem_i[tid])) {{
                smem_v[tid] = other_v;
                smem_i[tid] = other_i;
            }}
        }}
        __syncthreads();
    }}
    if (tid == 0) {{
        {index_out}[row] = smem_i[0];
        {value_store}
    }}
}}

extern "C" void solve({solve_decl}) {{
    dim3 block(HYGON_TOP1_BLOCK);
    dim3 grid({m});
    hygon_auto_row_top1<<<grid, block>>>({call_args});
}}
"""


def _ck_tile_candidate_sources(text: str, state: dict[str, Any], methods: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    ids = {str(method.get("id") or "") for method in methods}
    if not any("ck_tile" in mid or "mmac_tensor_core" in mid for mid in ids):
        return []
    ck_info = (state.get("env", {}) or {}).get("ck_tile", {}) or {}
    if not ck_info.get("available"):
        return []
    template = os.environ.get(CK_TILE_TEMPLATE_ENV, "").strip()
    if not template:
        return []
    template_path = Path(template).expanduser().resolve()
    if not template_path.is_file():
        return []
    src = template_path.read_text(encoding="utf-8", errors="ignore")
    if "ck_tile" not in src and "ck::" not in src:
        return []
    return [
        {
            "generator": "ck_tile_template",
            "plan": {"template": str(template_path), "include_dir": ck_info.get("include_dir", "")},
            "source": src,
            "claimed_method_ids": [
                mid
                for mid in ids
                if mid in {"memory.ck_tile_named_pipeline", "compute.mmac_tensor_core", "memory.matrix_load_mls"}
            ],
        }
    ]


def _specialized_branch_sources(text: str, state: dict[str, Any], methods: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    ids = {str(method.get("id") or "") for method in methods}
    out: list[dict[str, Any]] = []

    ck_tile = _ck_tile_candidate_sources(text, state, methods, limit)
    out.extend(ck_tile)
    if len(out) >= limit:
        return out[:limit]

    top1_contract = _detect_row_top1_contract(text, state)
    if top1_contract and any("top" in mid or "reduce_barrier" in mid or "thread_coarsening" in mid or "coalesced_access" in mid or "ilp_unroll" in mid for mid in ids):
        for block_size in (256, 128):
            try:
                out.append(
                    {
                        "generator": "row_top1_block",
                        "plan": {"block_size": block_size},
                        "source": _row_top1_block_source(top1_contract, block_size=block_size),
                        "claimed_method_ids": [
                            mid
                            for mid in ids
                            if "reduce_barrier" in mid or "thread_coarsening" in mid or "coalesced_access" in mid or "ilp_unroll" in mid
                        ],
                    }
                )
            except ValueError:
                pass
            if len(out) >= limit:
                return out[:limit]

    indexing_contract = _detect_gather_scatter_contract(text, state)
    if indexing_contract and any(mid in INDEXING_METHODS or "coalesced_access" in mid or "thread_coarsening" in mid or "waitcnt" in mid for mid in ids):
        family = str(indexing_contract["family"])
        plans = [
            {"elems_per_thread": 2, "block_size": 256},
            {"elems_per_thread": 4, "block_size": 256},
        ]
        for plan in plans:
            try:
                out.append(
                    {
                        "generator": {
                            "gather": "gather_coarsened",
                            "scatter": "scatter_coarsened",
                            "index_add": "index_add_atomic_coarsened",
                        }[family],
                        "plan": plan,
                        "source": _indexing_coarsened_source(
                            indexing_contract,
                            elems_per_thread=int(plan["elems_per_thread"]),
                            block_size=int(plan["block_size"]),
                        ),
                        "claimed_method_ids": [
                            mid
                            for mid in ids
                            if mid in INDEXING_METHODS or "coalesced_access" in mid or "thread_coarsening" in mid or "waitcnt" in mid
                        ],
                    }
                )
            except ValueError:
                pass
            if len(out) >= limit:
                return out[:limit]

    softmax_contract = _detect_softmax_contract(text, state)
    if softmax_contract and any(mid in ROW_REDUCTION_METHODS or "reduce_barrier" in mid or "fast_math" in mid for mid in ids):
        for block_size in (256, 128):
            out.append(
                {
                    "generator": "softmax_row_block",
                    "plan": {"block_size": block_size},
                    "source": _softmax_row_block_source(softmax_contract, block_size=block_size),
                    "claimed_method_ids": [
                        mid
                        for mid in ids
                        if mid in ROW_REDUCTION_METHODS or "reduce_barrier" in mid or "fast_math" in mid
                    ],
                }
            )
            if len(out) >= limit:
                return out[:limit]

    layernorm_contract = _detect_layernorm_contract(text, state)
    if layernorm_contract and any(mid in ROW_REDUCTION_METHODS or "reduce_barrier" in mid or "fast_math" in mid for mid in ids):
        for block_size in (256, 128):
            out.append(
                {
                    "generator": "layernorm_row_block",
                    "plan": {"block_size": block_size},
                    "source": _layernorm_row_block_source(layernorm_contract, block_size=block_size),
                    "claimed_method_ids": [
                        mid
                        for mid in ids
                        if mid in ROW_REDUCTION_METHODS or "reduce_barrier" in mid or "fast_math" in mid
                    ],
                }
            )
            if len(out) >= limit:
                return out[:limit]

    row_reduce_contract = _detect_row_reduction_contract(text, state)
    if row_reduce_contract and any(mid in ROW_REDUCTION_METHODS or "reduce_barrier" in mid or "coalesced_access" in mid for mid in ids):
        for block_size in (256, 128):
            try:
                out.append(
                    {
                        "generator": f"{row_reduce_contract['family']}_block",
                        "plan": {"block_size": block_size, "op": row_reduce_contract["op"]},
                        "source": _row_reduction_block_source(row_reduce_contract, block_size=block_size),
                        "claimed_method_ids": [
                            mid
                            for mid in ids
                            if mid in ROW_REDUCTION_METHODS or "reduce_barrier" in mid or "coalesced_access" in mid
                        ],
                    }
                )
            except ValueError:
                pass
            if len(out) >= limit:
                return out[:limit]

    transpose_contract = _detect_2d_transpose_contract(text, state)
    if transpose_contract and any("coalesced_access" in mid or "aligned_layout" in mid or "thread_coarsening" in mid for mid in ids):
        for tile in (16, 32):
            try:
                out.append(
                    {
                        "generator": "transpose_2d_tiled",
                        "plan": {"tile": tile},
                        "source": _transpose_2d_tiled_source(transpose_contract, tile=tile),
                        "claimed_method_ids": [
                            mid
                            for mid in ids
                            if "coalesced_access" in mid or "aligned_layout" in mid or "thread_coarsening" in mid
                        ],
                    }
                )
            except ValueError:
                pass
            if len(out) >= limit:
                return out[:limit]

    cast_contract = _detect_flat_cast_or_scale_contract(text, state)
    if cast_contract and any("coalesced_access" in mid or "thread_coarsening" in mid or "epilogue_fusion" in mid or "ilp_unroll" in mid for mid in ids):
        for elems_per_thread in (2, 4):
            try:
                out.append(
                    {
                        "generator": "flat_cast_or_scale_coarsened",
                        "plan": {"elems_per_thread": elems_per_thread, "launch_bounds": 256},
                        "source": _flat_cast_or_scale_source(
                            cast_contract,
                            elems_per_thread=elems_per_thread,
                            launch_bounds=256,
                        ),
                        "claimed_method_ids": [
                            mid
                            for mid in ids
                            if "coalesced_access" in mid or "thread_coarsening" in mid or "epilogue_fusion" in mid or "ilp_unroll" in mid
                        ],
                    }
                )
            except ValueError:
                pass
            if len(out) >= limit:
                return out[:limit]

    fill_contract = _detect_flat_fill_contract(text, state)
    if fill_contract and any("coalesced_access" in mid or "vectorized_global_access" in mid or "thread_coarsening" in mid or "ilp_unroll" in mid for mid in ids):
        for elems_per_thread in (4, 2):
            try:
                out.append(
                    {
                        "generator": "flat_fill_coarsened",
                        "plan": {"elems_per_thread": elems_per_thread, "launch_bounds": 256},
                        "source": _flat_fill_coarsened_source(
                            fill_contract,
                            elems_per_thread=elems_per_thread,
                            launch_bounds=256,
                        ),
                        "claimed_method_ids": [
                            mid
                            for mid in ids
                            if "coalesced_access" in mid or "vectorized_global_access" in mid or "thread_coarsening" in mid or "ilp_unroll" in mid
                        ],
                    }
                )
            except ValueError:
                pass
            if len(out) >= limit:
                return out[:limit]

    reduction_contract = _detect_flat_reduction_sum_contract(text, state)
    if reduction_contract and any("thread_coarsening" in mid or "ilp_unroll" in mid or "reduce_barrier" in mid or "coalesced_access" in mid for mid in ids):
        for block_size in (256, 128):
            try:
                out.append(
                    {
                        "generator": "flat_reduction_block_sum",
                        "plan": {"block_size": block_size},
                        "source": _flat_reduction_block_sum_source(reduction_contract, block_size=block_size),
                        "claimed_method_ids": [
                            mid
                            for mid in ids
                            if "thread_coarsening" in mid or "ilp_unroll" in mid or "reduce_barrier" in mid or "coalesced_access" in mid
                        ],
                    }
                )
            except ValueError:
                pass
            if len(out) >= limit:
                return out[:limit]

    copy_contract = _detect_flat_copy_contract(text, state)
    if copy_contract and any("vectorized_global_access" in mid or "coalesced_access" in mid for mid in ids):
        try:
            out.append(
                {
                    "generator": "flat_copy_float4",
                    "plan": {"vec": 4},
                    "source": _flat_copy_vectorized_source(copy_contract, vec=4),
                    "claimed_method_ids": [mid for mid in ids if "vectorized_global_access" in mid or "coalesced_access" in mid],
                }
            )
        except ValueError:
            pass
        if len(out) < limit:
            try:
                out.append(
                    {
                        "generator": "flat_copy_two_per_thread",
                        "plan": {"elems_per_thread": 2},
                        "source": _flat_copy_dual_load_source(copy_contract),
                        "claimed_method_ids": [mid for mid in ids if "coalesced_access" in mid or "thread_coarsening" in mid],
                    }
                )
            except ValueError:
                pass
        if len(out) >= limit:
            return out[:limit]

    axpy_contract = _detect_flat_axpy_contract(text, state)
    if axpy_contract and any("thread_coarsening" in mid or "ilp_unroll" in mid or "coalesced_access" in mid for mid in ids):
        try:
            out.append(
                {
                    "generator": "flat_axpy_vectorized",
                    "plan": {"elems_per_thread": 4},
                    "source": _flat_axpy_vectorized_source(axpy_contract),
                    "claimed_method_ids": [mid for mid in ids if "thread_coarsening" in mid or "ilp_unroll" in mid or "coalesced_access" in mid],
                }
            )
        except ValueError:
            pass
        if len(out) >= limit:
            return out[:limit]

    elem_contract = _detect_flat_elementwise_contract(text, state)
    if elem_contract and any("thread_coarsening" in mid or "ilp_unroll" in mid or "register_pressure" in mid for mid in ids):
        plans = [
            {"elems_per_thread": 2, "launch_bounds": 256},
            {"elems_per_thread": 4, "launch_bounds": 256},
        ]
        for plan in plans:
            out.append(
                {
                    "generator": "flat_elementwise_coarsened",
                    "plan": plan,
                    "source": _flat_elementwise_coarsened_source(
                        elem_contract,
                        elems_per_thread=int(plan["elems_per_thread"]),
                        launch_bounds=int(plan["launch_bounds"]),
                    ),
                    "claimed_method_ids": [mid for mid in ids if "thread_coarsening" in mid or "ilp_unroll" in mid or "register_pressure" in mid],
                }
            )
            if len(out) >= limit:
                return out[:limit]

    wants_matmul = any(
        token in mid
        for mid in ids
        for token in (
            "mmac_tensor_core",
            "lds_tiling",
                "vectorized_global_access",
                "thread_coarsening",
                "ilp_unroll",
                "register_pressure",
            )
        )
    if not wants_matmul:
        return out[:limit]
    contract = _detect_matmul_contract(text, state)
    if not contract:
        return out[:limit]
    claim_ids = [
        mid
        for mid in ids
        if any(
            token in mid
            for token in (
                "lds_tiling",
                "register_pressure",
                "thread_coarsening",
                "launch_config",
                "ilp_unroll",
            )
        )
    ]
    # Tiled LDS changes memory access shape but does not guarantee vectorized
    # global load/store ISA. Do not claim vectorized_global_access unless a
    # dedicated vectorized generator produced that branch.
    plans = [
        {"tile": 16, "unroll": True, "launch_bounds": 256},
        {"tile": 8, "unroll": True, "launch_bounds": 128},
        {"tile": 32, "unroll": True, "launch_bounds": 1024},
    ]
    for plan in plans[: max(0, limit - len(out))]:
        src = _matmul_tiled_source(contract, tile=int(plan["tile"]), unroll=bool(plan["unroll"]), launch_bounds=plan["launch_bounds"])
        out.append({"generator": "matmul_tiled_lds", "plan": plan, "source": src, "claimed_method_ids": claim_ids})
    return out[:limit]


def _method_transform_tags(methods: list[dict[str, Any]]) -> set[str]:
    ids = {str(method.get("id") or "") for method in methods}
    tags: set[str] = set()
    if any("vectorized_global_access" in mid or "coalesced_access" in mid or "aligned_layout" in mid for mid in ids):
        tags.add("restrict")
        tags.add("block_wide")
    if any("register_pressure" in mid or "launch_config" in mid for mid in ids):
        tags.add("launch_bounds")
        tags.add("block_occupancy")
    if any("waitcnt" in mid or "ilp" in mid or "thread_coarsening" in mid for mid in ids):
        tags.add("unroll")
    if any("fast_math" in mid for mid in ids):
        tags.add("unroll")
    if not tags and methods:
        tags.add("restrict")
    return tags


def _candidate_transform_plans(tags: set[str], count: int) -> list[list[str]]:
    base: list[list[str]] = []
    if "restrict" in tags:
        base.append(["restrict"])
    if "unroll" in tags:
        base.append(["unroll"])
    if "restrict" in tags and "unroll" in tags:
        base.append(["restrict", "unroll"])
    if "block_wide" in tags:
        base.extend([["block_32x8"], ["block_8x32"]])
    if "block_occupancy" in tags:
        base.extend([["block_16x8"], ["block_8x16"], ["block_128"]])
    if "launch_bounds" in tags:
        base.extend([["launch_bounds_256"], ["launch_bounds_128"], ["restrict", "launch_bounds_256"]])
    if "restrict" in tags and "block_wide" in tags:
        base.extend([["restrict", "block_32x8"], ["restrict", "block_8x32"]])
    if "restrict" in tags and "unroll" in tags and "launch_bounds" in tags:
        base.append(["restrict", "unroll", "launch_bounds_256"])

    unique: list[list[str]] = []
    seen = set()
    for plan in base:
        key = tuple(plan)
        if key in seen:
            continue
        seen.add(key)
        unique.append(plan)
        if len(unique) >= count:
            break
    return unique


def _apply_transform_plan(text: str, plan: list[str]) -> tuple[str, list[str]]:
    applied: list[str] = []
    out = text
    for item in plan:
        changed = False
        if item == "restrict":
            out, changed = _add_restrict_pointers(out)
        elif item == "unroll":
            out, changed = _add_unroll_pragmas(out)
        elif item.startswith("launch_bounds_"):
            out, changed = _add_launch_bounds(out, int(item.rsplit("_", 1)[1]))
        elif item.startswith("block_"):
            out, changed = _replace_block_dim(out, item)
        if changed:
            applied.append(item)
    return out, applied


def _prepare_method_branches(
    run_dir: Path,
    iteration: int,
    state: dict[str, Any],
    branches: int,
    methods: list[dict[str, Any]],
    *,
    include_noop_fallback: bool,
) -> list[dict[str, Any]]:
    src = _kernel_source_path(state)
    iter_dir = run_dir / f"iterv{iteration}"
    branch_infos: list[dict[str, Any]] = []
    branch_count = max(1, branches)
    next_branch = 1

    if include_noop_fallback:
        branch_dir = iter_dir / "branches" / f"b{next_branch}"
        branch_dir.mkdir(parents=True, exist_ok=True)
        dst = branch_dir / f"kernel{src.suffix}"
        shutil.copy2(src, dst)
        branch_infos.append(
            {
                "branch": next_branch,
                "source": str(src),
                "kernel": str(dst),
                "mode": "noop_fallback",
                "claimed_method_ids": [],
                "claimed_methods": [],
            }
        )
        next_branch += 1

    if next_branch <= branch_count and _source_is_transformable(src):
        text = src.read_text(encoding="utf-8", errors="ignore")
        specialized = _specialized_branch_sources(text, state, methods, branch_count - next_branch + 1)
        for generated in specialized:
            if next_branch > branch_count:
                break
            branch_dir = iter_dir / "branches" / f"b{next_branch}"
            branch_dir.mkdir(parents=True, exist_ok=True)
            dst = branch_dir / f"kernel{src.suffix}"
            header = (
                "// Generated by auto_kernel_optimize.py.\n"
                f"// Iteration {iteration}, branch {next_branch}, generator: {generated['generator']}, plan: {generated['plan']}\n"
                "// Correctness and speed are validated by branch_explore.py before promotion.\n\n"
            )
            dst.write_text(header + str(generated["source"]), encoding="utf-8")
            branch_infos.append(
                {
                    "branch": next_branch,
                    "source": str(src),
                    "kernel": str(dst),
                    "mode": "specialized_generator",
                    "generator": generated["generator"],
                    "plan": generated["plan"],
                    "claimed_method_ids": generated.get("claimed_method_ids", []),
                    "claimed_methods": _claim_methods(methods, list(generated.get("claimed_method_ids", []))),
                }
            )
            next_branch += 1

        tags = _method_transform_tags(methods)
        plans = _candidate_transform_plans(tags, branch_count - next_branch + 1)
        for plan in plans:
            if next_branch > branch_count:
                break
            new_text, applied = _apply_transform_plan(text, plan)
            if not applied or new_text == text:
                continue
            branch_dir = iter_dir / "branches" / f"b{next_branch}"
            branch_dir.mkdir(parents=True, exist_ok=True)
            dst = branch_dir / f"kernel{src.suffix}"
            header = (
                "// Generated by auto_kernel_optimize.py.\n"
                f"// Iteration {iteration}, branch {next_branch}, transforms: {', '.join(applied)}\n"
                "// Correctness and speed are validated by branch_explore.py before promotion.\n\n"
            )
            dst.write_text(header + new_text, encoding="utf-8")
            branch_infos.append(
                {
                    "branch": next_branch,
                    "source": str(src),
                    "kernel": str(dst),
                    "mode": "method_transform",
                    "requested_transforms": plan,
                    "applied_transforms": applied,
                    "claimed_method_ids": [method.get("id") for method in methods],
                    "claimed_methods": methods,
                }
            )
            next_branch += 1

    while next_branch <= branch_count:
        branch_dir = iter_dir / "branches" / f"b{next_branch}"
        branch_dir.mkdir(parents=True, exist_ok=True)
        dst = branch_dir / f"kernel{src.suffix}"
        shutil.copy2(src, dst)
        branch_infos.append(
            {
                "branch": next_branch,
                "source": str(src),
                "kernel": str(dst),
                "mode": "noop_fill",
                "claimed_method_ids": [],
                "claimed_methods": [],
            }
        )
        next_branch += 1

    _write_json(
        iter_dir / "branch_plan.json",
        {
            "iter": iteration,
            "source": str(src),
            "include_noop_fallback": include_noop_fallback,
            "selected_methods": [method.get("id") for method in methods],
            "branches": branch_infos,
        },
    )
    return branch_infos


def _prepare_noop_branches(run_dir: Path, iteration: int, state: dict[str, Any], branches: int) -> list[dict[str, Any]]:
    src = _kernel_source_path(state)
    iter_dir = run_dir / f"iterv{iteration}"
    branch_infos: list[dict[str, Any]] = []
    for idx in range(1, max(1, branches) + 1):
        branch_dir = iter_dir / "branches" / f"b{idx}"
        branch_dir.mkdir(parents=True, exist_ok=True)
        dst = branch_dir / f"kernel{src.suffix}"
        shutil.copy2(src, dst)
        branch_infos.append(
            {
                "branch": idx,
                "source": str(src),
                "kernel": str(dst),
                "mode": "noop_copy_best",
                "claimed_method_ids": [],
                "claimed_methods": [],
            }
        )
    _write_json(
        iter_dir / "branch_plan.json",
        {
            "iter": iteration,
            "source": str(src),
            "include_noop_fallback": True,
            "selected_methods": [],
            "branches": branch_infos,
        },
    )
    return branch_infos


def _evidence_summary(hcu_top: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    metrics = _all_metrics(hcu_top)
    metrics.sort(key=lambda item: _normalize_high_bad(_safe_float(item.get("value"))), reverse=True)
    return [
        {
            "axis": item["axis"],
            "metric": item["name"],
            "value": _safe_float(item.get("value")),
            "unit": str(item.get("unit") or ""),
        }
        for item in metrics[:limit]
    ]


def _write_analysis(
    iter_dir: Path,
    iteration: int,
    axis_budget: dict[str, int],
    methods: list[dict[str, Any]],
    branch_infos: list[dict[str, Any]],
    *,
    roofline: dict[str, Any],
    hcu_top: dict[str, Any],
    selection_policy: str,
    generator_capability: dict[str, Any],
    family_guidance: dict[str, Any],
) -> Path:
    lines = [
        f"# Auto Kernel Optimize Iteration {iteration}",
        "",
        f"Selection policy: `{selection_policy}`.",
        "",
        "This iteration selects methods from roofline/hcu_top evidence and validates the automatic optimizer state flow.",
        "",
        "## Axis Budget",
        "",
        "```json",
        json.dumps(axis_budget, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Roofline Summary",
        "",
        f"- bound: `{roofline.get('bound', 'unknown')}`",
        f"- delta_compute: `{roofline.get('delta_compute', 'n/a')}`",
        f"- delta_memory: `{roofline.get('delta_memory', 'n/a')}`",
        f"- delta_latency: `{roofline.get('delta_latency', 'n/a')}`",
        f"- degraded: `{roofline.get('degraded', hcu_top.get('degraded', False))}`",
        "",
        "## HCU Evidence Summary",
        "",
    ]
    summary = _evidence_summary(hcu_top)
    if summary:
        for item in summary:
            lines.append(f"- `{item['axis']}` `{item['metric']}` = `{item['value']}` {item['unit']}".rstrip())
    else:
        lines.append("- no hcu_top metrics found; selector fell back to registry priority inside roofline axis budget")
    lines.extend(
        [
            "",
            "## Generator Capability",
            "",
            f"- family: `{generator_capability.get('family', 'unknown')}`",
            f"- source: `{generator_capability.get('source', '')}`",
            f"- specialized_generators: `{', '.join(generator_capability.get('specialized_generators', []) or []) or '-'}`",
            f"- actionable_methods: `{', '.join(generator_capability.get('actionable_method_ids', []) or []) or '-'}`",
            f"- discouraged_methods: `{', '.join(generator_capability.get('discouraged_method_ids', []) or []) or '-'}`",
        ]
    )
    for note in generator_capability.get("notes", []) or []:
        lines.append(f"- note: {note}")
    primary_family = str(family_guidance.get("primary_family") or "")
    matched_families = family_guidance.get("matched_families", []) or []
    lines.extend(
        [
            "",
            "## Kernel Family Guidance",
            "",
            f"- status: `{family_guidance.get('status', 'unknown')}`",
            f"- primary_family: `{primary_family or '-'}`",
            f"- policy: `{family_guidance.get('policy', 'advisory_only_agent_must_review')}`",
        ]
    )
    if matched_families:
        for item in matched_families[:3]:
            methods_hint = ", ".join(str(mid) for mid in item.get("candidate_methods", [])[:6]) or "-"
            terms = ", ".join(str(term) for term in item.get("matched_terms", [])[:8]) or "-"
            lines.append(
                f"- match `{item.get('family')}` score={item.get('score')} terms=`{terms}` candidate_methods=`{methods_hint}`"
            )
        first = matched_families[0]
        gates = first.get("correctness_gates", []) or []
        traps = first.get("semantic_traps", []) or []
        if gates:
            lines.append("- primary correctness gates:")
            for gate in gates[:6]:
                lines.append(f"  - {gate}")
        if traps:
            lines.append("- primary semantic traps:")
            for trap in traps[:5]:
                lines.append(f"  - {trap}")
    else:
        for note in family_guidance.get("agent_guidance", []) or []:
            lines.append(f"- note: {note}")
    lines.extend(
        [
            "",
            "## Selected Methods",
            "",
        ]
    )
    for method in methods:
        lines.append(
            f"- `{method['id']}` ({method['axis']}, P{method['priority']}): "
            f"{method['name']} | trigger={method.get('trigger_strength', 0)}"
        )
        evidence = method.get("hcu_evidence") or []
        if evidence:
            for item in evidence[:4]:
                lines.append(f"  - evidence: `{item.get('metric')}` = `{item.get('value')}` {item.get('unit', '')}".rstrip())
        else:
            lines.append("  - evidence: no direct trigger metric; selected as fallback within axis budget")
        lines.append(f"  - expected: {method.get('expected_metric_shift', '')}")
    lines.extend(
        [
            "",
            "## Branches",
            "",
        ]
    )
    for info in branch_infos:
        generator = info.get("generator") or info.get("mode") or "-"
        claims = ", ".join(str(mid) for mid in info.get("claimed_method_ids", []) or []) or "-"
        lines.append(f"- b{info['branch']}: `{generator}` -> `{info['kernel']}` | claims: `{claims}`")
    lines.extend(
        [
            "",
            "## Limitation",
            "",
            "Branch generation is conservative. It reserves a no-op fallback when enabled, then emits simple method-driven HIP source variants.",
            "Only branch_explore.py can promote a candidate after compile, correctness, and benchmark checks.",
            "",
        ]
    )
    path = iter_dir / "analysis.md"
    _write_text(path, "\n".join(lines))
    return path


def _iteration_already_closed(run_dir: Path, iteration: int) -> bool:
    iter_dir = run_dir / f"iterv{iteration}"
    return (iter_dir / "branch_results.json").is_file() and (iter_dir / "bench.json").is_file()


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    state_path = _state_path(args)
    state = _read_json(state_path)
    run_dir = Path(state.get("run_dir", state_path.parent)).expanduser().resolve()
    if not run_dir.is_dir():
        raise SystemExit(f"run_dir not found: {run_dir}")
    iteration = int(args.iter)
    iter_dir = run_dir / f"iterv{iteration}"
    iter_dir.mkdir(parents=True, exist_ok=True)

    registry = _read_json(Path(args.registry).expanduser().resolve())
    family_catalog = _load_family_catalog(Path(args.family_catalog).expanduser().resolve())
    roofline, hcu_top = _load_iteration_evidence(run_dir, iteration)
    axis_budget = _axis_budget(run_dir, iteration)
    selection_policy = str(args.selection_policy or "evidence")
    generator_capability = _detect_generator_capability(state)
    family_guidance = _build_kernel_family_guidance(
        catalog=family_catalog,
        state=state,
        roofline=roofline,
        hcu_top=hcu_top,
        generator_capability=generator_capability,
    )
    methods = _select_methods(
        state,
        registry,
        axis_budget,
        roofline=roofline,
        hcu_top=hcu_top,
        selection_policy=selection_policy,
        generator_capability=generator_capability,
    )
    branches = int(args.branches or state.get("branches", 1) or 1)
    report: dict[str, Any] = {
        "status": "started",
        "run_dir": str(run_dir),
        "state": str(state_path),
        "iter": iteration,
        "axis_budget": axis_budget,
        "selection_policy": selection_policy,
        "generator_capability": generator_capability,
        "kernel_family_guidance": family_guidance,
        "roofline": roofline,
        "hcu_top_summary": _evidence_summary(hcu_top),
        "dry_run": bool(args.dry_run),
        "steps": [],
    }

    methods_path = iter_dir / "methods.json"
    family_guidance_path = iter_dir / "kernel_family_guidance.json"
    branch_infos: list[dict[str, Any]] = []
    if not args.dry_run:
        _write_json(family_guidance_path, family_guidance)
        _write_json(methods_path, {"iter": iteration, "methods": methods})
        if args.branch_mode == "noop":
            branch_infos = _prepare_noop_branches(run_dir, iteration, state, branches)
        else:
            branch_infos = _prepare_method_branches(
                run_dir,
                iteration,
                state,
                branches,
                methods,
                include_noop_fallback=not args.no_noop_fallback,
            )
        analysis_path = _write_analysis(
            iter_dir,
            iteration,
            axis_budget,
            methods,
            branch_infos,
            roofline=roofline,
            hcu_top=hcu_top,
            selection_policy=selection_policy,
            generator_capability=generator_capability,
            family_guidance=family_guidance,
        )
    else:
        analysis_path = iter_dir / "analysis.md"
        src = _kernel_source_path(state)
        branch_infos = [
            {
                "branch": idx,
                "source": str(src),
                "kernel": str(iter_dir / "branches" / f"b{idx}" / f"kernel{src.suffix}"),
                "mode": "planned_method_transform" if args.branch_mode != "noop" and idx > 1 else "planned_noop_fallback",
            }
            for idx in range(1, max(1, branches) + 1)
        ]
    report.update(
        {
            "methods_json": str(methods_path),
            "kernel_family_guidance_json": str(family_guidance_path),
            "analysis_md": str(analysis_path),
            "methods": methods,
            "branches": branch_infos,
        }
    )

    validate_cmd: list[str | Path] = [
        sys.executable,
        SCRIPT_DIR / "validate_methods.py",
        "--methods",
        methods_path,
        "--state",
        state_path,
    ]
    if args.allow_ineffective:
        validate_cmd.append("--allow-ineffective")
    report["steps"].append({"name": "validate_methods", **_run(validate_cmd, dry_run=args.dry_run)})
    if not args.dry_run and report["steps"][-1].get("returncode", 0) != 0:
        report["status"] = "validate_methods_failed"
        return report, int(report["steps"][-1].get("returncode", 1))

    if args.prepare_only:
        report["status"] = "prepared" if not args.dry_run else "prepare_planned"
        return report, 0

    if not args.force_close and _iteration_already_closed(run_dir, iteration):
        report["status"] = "iteration_already_closed"
        report["reason"] = "branch_results.json and bench.json already exist; use --force-close to rerun close-iter"
        return report, 0

    close_cmd: list[str | Path] = [
        sys.executable,
        SCRIPT_DIR / "orchestrate.py",
        "close-iter",
        "--run-dir",
        run_dir,
        "--iter",
        str(iteration),
        "--warmup",
        str(args.warmup),
        "--repeat",
        str(args.repeat),
        "--retries",
        str(args.retries),
    ]
    report["steps"].append({"name": "close_iter", **_run(close_cmd, dry_run=args.dry_run)})
    if not args.dry_run and report["steps"][-1].get("returncode", 0) != 0:
        report["status"] = "close_iter_failed"
        return report, int(report["steps"][-1].get("returncode", 1))

    if args.finalize:
        finalize_cmd: list[str | Path] = [
            sys.executable,
            SCRIPT_DIR / "orchestrate.py",
            "finalize",
            "--run-dir",
            run_dir,
        ]
        report["steps"].append({"name": "finalize", **_run(finalize_cmd, dry_run=args.dry_run)})
        if not args.dry_run and report["steps"][-1].get("returncode", 0) != 0:
            report["status"] = "finalize_failed"
            return report, int(report["steps"][-1].get("returncode", 1))
    report["status"] = "completed" if not args.dry_run else "planned"
    return report, 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Automatic evidence-driven kernel optimizer loop")
    parser.add_argument("--run-dir", default="", help="Optimizer run directory containing state.json")
    parser.add_argument("--state", default="", help="Explicit state.json path")
    parser.add_argument("--iter", type=int, default=1)
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    parser.add_argument("--family-catalog", default=str(DEFAULT_FAMILY_CATALOG))
    parser.add_argument("--branches", type=int, default=0, help="Override branch count; default uses state.branches")
    parser.add_argument("--warmup", type=int, default=2)
    parser.add_argument("--repeat", type=int, default=5)
    parser.add_argument("--retries", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--selection-policy", default="evidence", choices=["evidence", "priority"])
    parser.add_argument("--branch-mode", default="method_transform", choices=["method_transform", "noop"])
    parser.add_argument("--no-noop-fallback", action="store_true", help="Do not reserve branch 1 as current-best fallback")
    parser.add_argument("--prepare-only", action="store_true", help="Write methods/branches/analysis but do not close iteration")
    parser.add_argument("--finalize", action="store_true", help="Call orchestrate.py finalize after close-iter")
    parser.add_argument("--force-close", action="store_true", help="Rerun close-iter even if branch_results.json already exists")
    parser.add_argument("--allow-ineffective", action="store_true")
    parser.add_argument("--report-out", default="", help="Optional report path. Defaults to <run_dir>/auto_kernel_optimize_report.json")
    args = parser.parse_args()

    report, exit_code = run(args)
    out_path = Path(args.report_out).expanduser().resolve() if args.report_out else Path(report["run_dir"]) / "auto_kernel_optimize_report.json"
    _write_json(out_path, report)
    report["report"] = str(out_path)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
