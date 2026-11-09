#!/usr/bin/env python3
"""Compute HCU roofline-like gaps and allocate per-axis method budgets."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from hcu_specs import gpu_peak_spec
except ModuleNotFoundError:
    def gpu_peak_spec(env: dict | None, *, compute_kind: str | None = None, precision: str | None = None) -> dict:
        env = env or {}
        gpu = (env.get("gpus") or [{}])[0]
        arch = gpu.get("gfx_arch") or gpu.get("gcn_arch") or env.get("primary_gfx_arch")
        peak_compute = _safe_float(gpu.get("peak_compute_tops") or gpu.get("peak_flops_tflops"), default=0.0)
        peak_bw = _safe_float(gpu.get("peak_bw_gbs") or gpu.get("peak_hbm_bandwidth_gbs"), default=0.0)
        return {
            "model": gpu.get("model") or "unknown",
            "label": gpu.get("name") or "unknown",
            "arch": arch or "unknown",
            "compute_kind": compute_kind or "unknown",
            "precision": precision or "unknown",
            "cu": gpu.get("compute_units"),
            "clock_mhz": gpu.get("clock_mhz") or gpu.get("sclk_mhz"),
            "peak_compute_tops": peak_compute or None,
            "peak_bw_gbs": peak_bw or None,
            "source": "hcu_specs.py unavailable; using explicit env GPU peaks only",
            "specs_available": False,
        }

TOTAL_BUDGET = 3
MAX_PER_AXIS = 2
NEAR_PEAK_THRESHOLD = 0.15
TIE_BREAK_ORDER = ["memory", "latency", "compute"]


def _safe_float(value, default=0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _find_metric_item(hcu_top: dict, patterns: list[str], axis: str | None = None) -> dict | None:
    axes = [axis] if axis else ["compute", "memory", "latency"]
    for ax in axes:
        for item in hcu_top.get(ax, []):
            name = item.get("name") or item.get("metric") or ""
            lname = name.lower()
            if any(p.lower() in lname for p in patterns):
                return item
    return None


def _find_metric(hcu_top: dict, patterns: list[str], axis: str | None = None) -> float:
    item = _find_metric_item(hcu_top, patterns, axis)
    if item is not None:
        return _safe_float(item.get("value"))
    return 0.0


def _derived_metric(hcu_top: dict, key: str) -> float | None:
    derived = hcu_top.get("derived_metrics") or {}
    value = derived.get(key)
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _percent_from_metric(item: dict | None) -> tuple[float | None, str]:
    """Return utilization fraction only when the metric is explicitly a percent.

    hipprof PMC files often contain raw event counts (for example
    GRBM_GUI_ACTIVE or TA_TA_BUSY). Those values can be much larger than 100
    and must not be divided by 100 or clamped into a fake utilization.
    """
    if not item:
        return None, "missing"
    name = (item.get("name") or item.get("metric") or "").lower()
    unit = (item.get("unit") or "").lower()
    value = _safe_float(item.get("value"), default=float("nan"))
    percent_tokens = ("pct", "percent", "%", "util", "utilization", "occupancy")
    is_percent = unit in {"%", "percent", "pct"} or any(token in name for token in percent_tokens)
    if not is_percent:
        return None, f"raw_counter:{item.get('name') or item.get('metric')}"
    if value != value:
        return None, "nan"
    if 0.0 <= value <= 1.0:
        return value, "fraction"
    if 0.0 <= value <= 100.0:
        return value / 100.0, "percent"
    return None, f"percent_out_of_range:{value}"


def compute_deltas(hcu_top: dict, env: dict) -> dict:
    if hcu_top.get("degraded", False):
        return {
            "delta_compute": 0.50,
            "delta_memory": 0.50,
            "delta_latency": 0.50,
            "compute_util_pct": None,
            "memory_util_pct": None,
            "max_stall_pct": None,
            "degraded": True,
            "utilization_reliable": False,
            "notes": ["hcu_top is degraded; roofline gaps are fallback values."],
        }

    notes: list[str] = []
    compute_kind = (hcu_top.get("derived_metrics") or {}).get("compute_util_kind")
    spec = gpu_peak_spec(env, compute_kind=compute_kind)
    if not spec.get("specs_available", True):
        notes.append("hcu_specs.py unavailable; HCU-Analyzer peak/ridge fields are degraded unless env provides explicit GPU peaks.")
    compute_derived = _derived_metric(hcu_top, "compute_util_pct")
    memory_derived = _derived_metric(hcu_top, "memory_util_pct")
    hbm_bw = _derived_metric(hcu_top, "hbm_bandwidth_gbs")
    sq_busy_item = _find_metric_item(
        hcu_top,
        [
            "compute_utilization_pct",
            "COMPUTE_UTIL",
            "ALU_UTIL",
            "VALU_UTIL",
            "SQ_UTIL",
            "SQ_BUSY_CYCLES",
            "GRBM_GUI_ACTIVE",
        ],
        "compute",
    )
    sq_cycles_item = _find_metric_item(hcu_top, ["SQ_CYCLES", "GRBM_COUNT"], "compute")
    sq_busy = _safe_float((sq_busy_item or {}).get("value"))
    sq_cycles = _safe_float((sq_cycles_item or {}).get("value"))
    mmop = _find_metric(hcu_top, ["SQ_INSTS_MMOP", "MMOP", "MMAC"], "compute")
    if compute_derived is not None:
        compute_util = max(0.0, min(1.0, compute_derived / 100.0))
        compute_note = "xcu derived compute_util_pct"
    elif sq_busy > 0 and sq_cycles > 0 and sq_busy <= sq_cycles:
        compute_util = min(1.0, sq_busy / sq_cycles)
        compute_note = "SQ busy/cycles ratio"
    else:
        compute_util, compute_note = _percent_from_metric(sq_busy_item)
    if compute_util is None:
        delta_c = 0.50
        notes.append(
            f"compute utilization unavailable ({compute_note}); raw PMC counters are not treated as percentages."
        )
    else:
        delta_c = max(0.0, 1.0 - compute_util)
    if mmop > 0 and compute_util is None:
        notes.append("MMOP/MMAC-like activity was present, but no reliable utilization denominator was found.")

    memory_item = _find_metric_item(
        hcu_top,
        [
            "memory_utilization_pct",
            "HBM_BANDWIDTH_UTIL",
            "VL1-Bandwidth(Pct of Peak)",
            "TCC_BUSY",
            "TCP_TOTAL_CACHE_ACCESSES",
            "TCP_TCC_READ_REQ",
        ],
        "memory",
    )
    if memory_derived is not None:
        memory_util = max(0.0, min(1.0, memory_derived / 100.0))
        memory_note = "xcu derived memory_util_pct"
    elif hbm_bw is not None and spec["peak_bw_gbs"]:
        memory_util = max(0.0, min(1.0, hbm_bw / spec["peak_bw_gbs"]))
        memory_note = f"hbm_bandwidth_gbs / HCU-Analyzer peak_bw_gbs ({spec['peak_bw_gbs']})"
    else:
        memory_util, memory_note = _percent_from_metric(memory_item)
    if memory_util is None:
        delta_m = 0.50
        notes.append(
            f"memory utilization unavailable ({memory_note}); use benchmark logical GB/s or hardware bandwidth counters instead."
        )
    else:
        delta_m = max(0.0, 1.0 - memory_util)

    stalls = []
    for item in hcu_top.get("latency", []):
        name = (item.get("name") or "").lower()
        if any(token in name for token in ("stall", "latency", "wait", "wave_cycles", "barrier")):
            value, stall_note = _percent_from_metric(item)
            if value is None:
                notes.append(
                    f"latency metric {item.get('name') or item.get('metric')} is a raw counter ({stall_note}); it is not a stall percentage."
                )
            else:
                stalls.append(max(0.0, min(1.0, value)))
    delta_l = max(stalls) if stalls else 0.50

    sqtt = hcu_top.get("sqtt_analysis") or {}
    if isinstance(sqtt, dict) and not sqtt.get("error"):
        waitcnt_count = _safe_float(sqtt.get("waitcnt_count"))
        branch_count = _safe_float(sqtt.get("branch_count"))
        stall_hits = sqtt.get("stall_like_hits") or []
        if waitcnt_count > 0 or stall_hits:
            delta_l = max(delta_l, 0.65)
        if branch_count > 0:
            delta_l = max(delta_l, 0.55)

    codeobj = hcu_top.get("codeobj_analyze") or {}
    if isinstance(codeobj, dict):
        flags = set(codeobj.get("pressure_flags") or [])
        if "high_vgpr" in flags or "high_sgpr" in flags:
            delta_c = max(delta_c, 0.55)
            delta_l = max(delta_l, 0.55)

    measured_peak = _derived_metric(hcu_top, "compute_peak_tops")
    peak_compute = measured_peak if measured_peak and measured_peak > 0 else spec["peak_compute_tops"]
    peak_bw = spec["peak_bw_gbs"]
    ai_ridge = (peak_compute * 1e12) / (peak_bw * 1e9) if peak_compute and peak_bw else None
    utilization_reliable = compute_util is not None or memory_util is not None
    l2_hit = _derived_metric(hcu_top, "l2_hit_rate_pct")
    l1_hit = _derived_metric(hcu_top, "l1_hit_rate_pct")
    l2_bw = _derived_metric(hcu_top, "l2_bandwidth_gbs")
    coalescing = _derived_metric(hcu_top, "vl1_buffer_coalescing_pct")
    vl1_stalled_l2 = _derived_metric(hcu_top, "vl1_stalled_l2_data_pct")
    load_eff = _derived_metric(hcu_top, "global_load_efficiency_pct")
    store_eff = _derived_metric(hcu_top, "global_store_efficiency_pct")
    lds_conflict = _derived_metric(hcu_top, "lds_bank_conflict")
    return {
        "delta_compute": round(delta_c, 4),
        "delta_memory": round(delta_m, 4),
        "delta_latency": round(delta_l, 4),
        "compute_util_pct": round(compute_util * 100, 2) if compute_util is not None else None,
        "memory_util_pct": round(memory_util * 100, 2) if memory_util is not None else None,
        "l2_hit_rate_pct": round(l2_hit, 2) if l2_hit is not None else None,
        "l1_hit_rate_pct": round(l1_hit, 2) if l1_hit is not None else None,
        "hbm_bandwidth_gbs": round(hbm_bw, 2) if hbm_bw is not None else None,
        "l2_bandwidth_gbs": round(l2_bw, 2) if l2_bw is not None else None,
        "vl1_buffer_coalescing_pct": round(coalescing, 2) if coalescing is not None else None,
        "vl1_stalled_l2_data_pct": round(vl1_stalled_l2, 2) if vl1_stalled_l2 is not None else None,
        "global_load_efficiency_pct": round(load_eff, 2) if load_eff is not None else None,
        "global_store_efficiency_pct": round(store_eff, 2) if store_eff is not None else None,
        "lds_bank_conflict": round(lds_conflict, 4) if lds_conflict is not None else None,
        "profiler": hcu_top.get("profiler"),
        "max_stall_pct": round(max(stalls) * 100, 2) if stalls else None,
        "ai_ridge": round(ai_ridge, 2) if ai_ridge is not None else None,
        "peak_compute_tops": round(peak_compute, 4) if peak_compute is not None else None,
        "peak_compute_source": (
            "xcu percent-of-peak inferred denominator" if measured_peak and measured_peak > 0 else spec["source"]
        ),
        "peak_bw_gbs": round(peak_bw, 2) if peak_bw else None,
        "hcu_model": spec["model"],
        "hcu_model_label": spec["label"],
        "hcu_arch": spec["arch"],
        "hcu_compute_kind": spec["compute_kind"],
        "hcu_peak_precision": spec["precision"],
        "hcu_cu": spec["cu"],
        "hcu_clock_mhz": spec["clock_mhz"],
        "sqtt_informed": bool(sqtt and not sqtt.get("error")),
        "codeobj_informed": bool(codeobj and codeobj.get("available")),
        "degraded": not utilization_reliable,
        "utilization_reliable": utilization_reliable,
        "notes": notes,
    }


def allocate_budget(delta_c: float, delta_m: float, delta_l: float) -> dict:
    deltas = {"compute": delta_c, "memory": delta_m, "latency": delta_l}
    for axis in deltas:
        if deltas[axis] < 0.10:
            deltas[axis] = 0.0
    total = sum(deltas.values())
    if total < 0.01:
        return {"compute": 1, "memory": 1, "latency": 1}
    raw = {axis: TOTAL_BUDGET * deltas[axis] / total for axis in deltas}
    budgets = {axis: int(round(raw[axis])) for axis in deltas}
    overflow = 0
    for axis in budgets:
        if budgets[axis] > MAX_PER_AXIS:
            overflow += budgets[axis] - MAX_PER_AXIS
            budgets[axis] = MAX_PER_AXIS
    for axis in sorted(deltas, key=lambda a: -deltas[a]):
        if overflow <= 0:
            break
        if budgets[axis] < MAX_PER_AXIS:
            take = min(overflow, MAX_PER_AXIS - budgets[axis])
            budgets[axis] += take
            overflow -= take
    while sum(budgets.values()) != TOTAL_BUDGET:
        if sum(budgets.values()) < TOTAL_BUDGET:
            best = max((a for a in TIE_BREAK_ORDER if budgets[a] < MAX_PER_AXIS), key=lambda a: raw[a] - budgets[a], default=None)
            if best is None:
                break
            budgets[best] += 1
        else:
            worst = min((a for a in reversed(TIE_BREAK_ORDER) if budgets[a] > 0), key=lambda a: raw[a] - budgets[a], default=None)
            if worst is None:
                break
            budgets[worst] -= 1
    return budgets


def run(state_path: str, iteration: int) -> dict:
    with open(state_path, "r", encoding="utf-8-sig") as f:
        state = json.load(f)
    iter_dir = os.path.join(state["run_dir"], f"iterv{iteration}")
    top_path = os.path.join(iter_dir, "hcu_top.json")
    if not os.path.isfile(top_path):
        sys.exit(f"hcu_top.json not found at {top_path}")
    with open(top_path, "r", encoding="utf-8-sig") as f:
        hcu_top = json.load(f)

    deltas = compute_deltas(hcu_top, state.get("env", {}))
    dc, dm, dl = deltas["delta_compute"], deltas["delta_memory"], deltas["delta_latency"]
    near_peak = (
        not deltas.get("degraded", False)
        and dc < NEAR_PEAK_THRESHOLD
        and dm < NEAR_PEAK_THRESHOLD
        and dl < NEAR_PEAK_THRESHOLD
    )
    max_delta = max(dc, dm, dl)
    if deltas.get("degraded", False) and not deltas.get("utilization_reliable", False):
        bound = "unknown"
    else:
        bound = "near_peak" if near_peak else "compute" if max_delta == dc else "bandwidth" if max_delta == dm else "latency"
    result = {**deltas, "bound": bound, "near_peak": near_peak, "axis_budget": allocate_budget(dc, dm, dl)}
    out_path = os.path.join(iter_dir, "roofline.json")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--state", required=True)
    p.add_argument("--iter", type=int, required=True)
    args = p.parse_args()
    run(args.state, args.iter)


if __name__ == "__main__":
    main()
