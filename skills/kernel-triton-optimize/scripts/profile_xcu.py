#!/usr/bin/env python3
"""Profile a Triton/HIP kernel with XCompute xcu and emit hcu_top.json.

The output schema intentionally matches profile_hipprof.py enough for
roofline.py and summarize.py to consume it.  xcu is preferred on Hygon HCU
because it exposes higher-level Memory Workload / Speed-of-Light metrics such
as L2 hit rate and HBM bandwidth that are not reliably recoverable from
hipprof raw PMC CSVs alone.

The metric mapping uses schema and bottleneck heuristics compatible with
GEAK's AMD Metrix MCP service:
  https://github.com/AMD-AGI/GEAK/tree/main/mcp_tools/metrix-mcp
It mirrors AMD Metrix from AMDResearch IntelliKit:
  https://github.com/AMDResearch/intellikit/tree/main/metrix
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    from hcu_specs import gpu_peak_spec
except ModuleNotFoundError:
    def gpu_peak_spec(env: dict | None, *, compute_kind: str | None = None, precision: str | None = None) -> dict:
        env = env or {}
        gpu = (env.get("gpus") or [{}])[0]
        arch = gpu.get("gfx_arch") or gpu.get("gcn_arch") or env.get("primary_gfx_arch")
        peak_compute = _parse_float(gpu.get("peak_compute_tops") or gpu.get("peak_flops_tflops"))
        peak_bw = _parse_float(gpu.get("peak_bw_gbs") or gpu.get("peak_hbm_bandwidth_gbs"))
        return {
            "model": gpu.get("model") or "unknown",
            "label": gpu.get("name") or "unknown",
            "arch": arch or "unknown",
            "compute_kind": compute_kind or "unknown",
            "precision": precision or "unknown",
            "cu": gpu.get("compute_units"),
            "clock_mhz": gpu.get("clock_mhz") or gpu.get("sclk_mhz"),
            "peak_compute_tops": peak_compute,
            "peak_bw_gbs": peak_bw,
            "source": "hcu_specs.py unavailable; using explicit env GPU peaks only",
            "specs_available": False,
        }

from profile_hipprof import (
    KERNEL_EXTS,
    _BUNDLED_BENCHMARK,
    _active_config_for_manifest,
    _config_argv,
    _detect_backend,
    _dims_argv,
    _effective_config_args,
    _new_profile_cache_dir,
    _ptr_size_argv,
    _read,
    _write_json,
)


QUICK_SECTIONS = "memory_workload"
FULL_SECTIONS = "memory_workload,speed_of_light,compute_workload"
XCU_CANDIDATES = (
    "/opt/xcompute-4.4.4/XCompute/bin/xcu",
    "/opt/xcompute/XCompute/bin/xcu",
)
SKIP_KERNEL_PATTERNS = (
    "vectorized_elementwise",
    "distribution_",
    "reduce_kernel",
    "fillBuffer",
    "copyBuffer",
    "Cijk_",
    "at::native",
    "rocclr",
)
_JIT_NAME_RE = re.compile(
    r"@triton\.jit[^\n]*\n(?:[ \t]*@[^\n]*\n)*[ \t]*def[ \t]+([A-Za-z_][A-Za-z0-9_]*)"
)


def _jit_names(kernel_path: str) -> list[str]:
    try:
        text = Path(kernel_path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    return _JIT_NAME_RE.findall(text)


def _default_kernel_filter(kernel_path: str) -> str:
    """xcu -K substring from the first @triton.jit name (e.g. chunk_kda_fwd_* -> chunk_kda)."""
    names = _jit_names(kernel_path)
    if not names:
        return ""
    parts = [p for p in names[0].split("_") if p]
    return "_".join(parts[:2]) if len(parts) >= 2 else names[0]


def _kernel_filter_source(args: argparse.Namespace, solution: str) -> str:
    if args.kernel_name:
        return "cli"
    if args.no_kernel_filter:
        return "disabled"
    if not str(solution).endswith(".py"):
        return "non_python"
    if args.kernel_filter:
        return "triton_jit_default"
    return "not_detected"


@dataclass
class KernelProfile:
    dispatch_id: int
    kernel_name: str
    duration_us: float = 0.0
    raw_metrics: dict[str, float] = field(default_factory=dict)
    metric_units: dict[str, str] = field(default_factory=dict)
    source_file: str = ""


def _find_xcu(explicit: str = "") -> str | None:
    if explicit:
        return explicit if os.path.isfile(explicit) or shutil.which(explicit) else None
    env = os.environ.get("XCU_BIN_PATH", "")
    if env and os.path.isfile(env):
        return env
    for candidate in XCU_CANDIDATES:
        if os.path.isfile(candidate):
            return candidate
    return shutil.which("xcu")


def _parse_float(value: Any) -> float | None:
    text = str(value or "").strip().replace(",", "")
    if not text or text.upper() in {"N/A", "NA", "NULL", "-"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _parse_xcu_csv(path: Path) -> tuple[dict[str, float], dict[str, str]]:
    metrics: dict[str, float] = {}
    units: dict[str, str] = {}
    try:
        rows = csv.reader(path.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return metrics, units
    for parts in rows:
        if len(parts) < 3:
            continue
        name = (parts[0] or "").strip()
        unit = (parts[1] or "").strip()
        if not name or name.lower().startswith(("memory ", "compute ", "dispatch ")):
            continue
        value = _parse_float(parts[2])
        if value is None:
            continue
        metrics[name] = value
        units[name] = unit
    return metrics, units


def _parse_dispatch_summary(path: Path) -> dict[int, tuple[str, float]]:
    out: dict[int, tuple[str, float]] = {}
    if not path.is_file():
        return out
    try:
        f = path.open(newline="", encoding="utf-8", errors="replace")
    except OSError:
        return out
    with f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dispatch_id = int(row.get("Dispatch id", row.get("dispatch id", -1)))
            except (TypeError, ValueError):
                continue
            kernel = (row.get("Kernel") or row.get("kernel") or "").strip()
            duration_ms = _parse_float(row.get("Duration [ms]", row.get("duration [ms]", "")))
            out[dispatch_id] = (kernel, (duration_ms or 0.0) * 1000.0)
    return out


def _collect_profiles(output_dir: Path) -> list[KernelProfile]:
    durations: dict[int, tuple[str, float]] = {}
    for summary in output_dir.glob("*_dispatch_results_summary_info.csv"):
        durations.update(_parse_dispatch_summary(summary))

    profiles: list[KernelProfile] = []
    pattern = re.compile(r"^(\d+)_(.+)\.csv$")
    for csv_path in sorted(output_dir.glob("*.csv")):
        if csv_path.name.endswith("_dispatch_results_summary_info.csv"):
            continue
        match = pattern.match(csv_path.name)
        if not match:
            continue
        dispatch_id = int(match.group(1))
        kernel_from_file = match.group(2)
        raw, units = _parse_xcu_csv(csv_path)
        kernel_from_summary, duration_us = durations.get(dispatch_id, ("", 0.0))
        profiles.append(KernelProfile(
            dispatch_id=dispatch_id,
            kernel_name=kernel_from_summary or kernel_from_file,
            duration_us=duration_us,
            raw_metrics=raw,
            metric_units=units,
            source_file=str(csv_path),
        ))
    return profiles


def _select_profiles(profiles: list[KernelProfile], kernel_filter: str = "", auto_select: bool = True) -> list[KernelProfile]:
    selected = profiles
    if kernel_filter:
        needle = kernel_filter.strip("*").lower()
        selected = [p for p in selected if needle in p.kernel_name.lower()]
    if auto_select and not kernel_filter:
        candidates = [
            p for p in selected
            if not any(skip in p.kernel_name for skip in SKIP_KERNEL_PATTERNS)
        ]
        if candidates:
            selected = [max(candidates, key=lambda p: p.duration_us)]
    return selected


def _metric_axis(name: str) -> str:
    lname = name.lower()
    if any(t in lname for t in ("l2", "vl1", "l1", "hbm", "fabric", "lds", "cache", "coalesc", "read", "write", "bandwidth", "ta-", "td-")):
        return "memory"
    if any(t in lname for t in ("stall", "wait", "latency", "barrier", "idle", "wave cycles")):
        return "latency"
    if any(t in lname for t in ("compute", "alu", "valu", "salu", "mfma", "mma", "mmac", "sq_", "occupancy", "ipc", "cu-", "busy")):
        return "compute"
    return "memory"


def _is_percent(name: str, unit: str) -> bool:
    lname = name.lower()
    lunit = unit.lower()
    return lunit in {"%", "percent", "pct"} or any(t in lname for t in ("pct", "percent", "rate", "ratio", "util", "busy", "occupancy", "hit rate"))


def _metric_item(name: str, value: float, unit: str, source_file: str) -> dict:
    axis = _metric_axis(name)
    return {
        "name": name,
        "value": value,
        "unit": unit,
        "higher_is_worse": axis == "latency" or any(t in name.lower() for t in ("conflict", "stall", "wait")),
        "samples": 1,
        "source_files": [os.path.basename(source_file)] if source_file else [],
    }


def _first_raw(raw: dict[str, float], names: tuple[str, ...]) -> float | None:
    for name in names:
        if name in raw:
            return raw[name]
    return None


def _best_percent_metric(raw: dict[str, float], units: dict[str, str], patterns: tuple[str, ...]) -> tuple[float | None, str]:
    compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
    for name, value in raw.items():
        unit = units.get(name, "")
        if not _is_percent(name, unit):
            continue
        if any(p.search(name) for p in compiled):
            if 0.0 <= value <= 1.0:
                return value * 100.0, name
            if 0.0 <= value <= 100.0:
                return value, name
    return None, ""


def _has_mmop_activity(raw: dict[str, float]) -> bool:
    for name, value in raw.items():
        lname = name.lower()
        if not any(token in lname for token in ("mmop", "mmac", "mfma", "matrix")):
            continue
        if "util" in lname:
            continue
        if value > 0:
            return True
    return False


def _select_compute_util(raw: dict[str, float], units: dict[str, str]) -> tuple[float | None, str, str]:
    """Pick the compute utilization domain that matches the kernel's ISA class.

    Matrix-core kernels should be judged by MMOP/MMAC utilization. Pure
    elementwise/reduction kernels with no matrix activity should use VALU.
    SALU is intentionally not used as the generic compute proxy because it can
    make vector-heavy kernels look almost idle.
    """
    if _has_mmop_activity(raw):
        value, source = _best_percent_metric(raw, units, (
            r"\bmmop.*util\b",
            r"\bmmac.*util\b",
            r"\bmfma.*util\b",
        ))
        if source:
            return value, source, "mmop"
        return None, "MMOP/MMAC activity present but no MMOP/MMAC utilization percent", "mmop"

    value, source = _best_percent_metric(raw, units, (
        r"\bvalu.*util\b",
        r"\bvalu.*(active|busy|peak)",
    ))
    if source:
        return value, f"{source} (no MMOP/MMAC activity)", "valu"

    value, source = _best_percent_metric(raw, units, (
        r"compute.*(util|busy|active|peak)",
        r"sq.*(util|busy|active)",
        r"cu.*(util|busy|active)",
    ))
    if source:
        return value, f"{source} (fallback; no MMOP/MMAC or VALU utilization)", "generic"
    return None, "no MMOP/MMAC, VALU, or generic compute utilization percent", "unknown"


def _compute_throughput_gops(raw: dict[str, float], compute_kind: str) -> tuple[float | None, str, str]:
    """Return measured compute throughput for the selected compute domain."""
    if compute_kind == "mmop":
        for name in (
            "MMOP FLOPs(F8/F6/F4)",
            "MMOP FLOPs(BF16)",
            "MMOP FLOPs(F16)",
            "MMOP FLOPs(F32)",
            "MMOP FLOPs(F64)",
            "MMOP FLOPs(TF32)",
            "MMOP IOPs(I8/U8)",
            "MMOP IOPs(I4/U4)",
        ):
            value = raw.get(name)
            if value and value > 0:
                unit = "GFLOPs/s" if "FLOPs" in name else "GIOPs/s"
                return value, name, unit
    if compute_kind == "valu":
        for name in ("VALU FLOPs", "VALU IOPs"):
            value = raw.get(name)
            if value and value > 0:
                unit = "GFLOPs/s" if "FLOPs" in name else "GIOPs/s"
                return value, name, unit
    return None, "", ""


def _compute_peak_from_pop(
    raw: dict[str, float],
    throughput: float | None,
    compute_kind: str,
    state: dict | None = None,
) -> tuple[float | None, str]:
    """Infer a domain peak from xcu percent-of-peak metrics when available."""
    if throughput is not None and throughput > 0:
        pop_names = ("mmop_flops_pop", "mmop_iops_pop") if compute_kind == "mmop" else ("valu_flops_pop", "valu_iops_pop")
        for name in pop_names:
            pct = raw.get(name)
            if pct and pct > 0:
                return throughput / (pct / 100.0), name
    spec = gpu_peak_spec((state or {}).get("env", {}), compute_kind=compute_kind)
    peak = spec.get("peak_compute_tops")
    if peak:
        source_prefix = "HCU-Analyzer" if spec.get("specs_available", True) else "explicit env"
        return float(peak) * 1000.0, (
            f"{source_prefix} {spec['model']} {spec['compute_kind']} {spec['precision']} "
            f"{spec['cu']}CU@{spec['clock_mhz']}MHz"
        )
    return None, ""


def _derived_l2_bandwidth(raw: dict[str, float], duration_us: float) -> float | None:
    l2_req = _first_raw(raw, ("L2-Req", "L2 Req", "L2_Request"))
    if l2_req is None or duration_us <= 0:
        return None
    return (l2_req * 128.0) / (duration_us / 1e6) / 1e9


def _efficiency_pct(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator is None or denominator <= 0:
        return None
    return min(100.0, numerator / denominator * 100.0)


def _build_hcu_top(
    *,
    profile: KernelProfile,
    all_profiles: list[KernelProfile],
    state: dict,
    solution: str,
    out_dir: Path,
    log_path: str,
    sections: str,
    xcu_bin: str,
    kernel_filter: str = "",
    kernel_filter_source: str = "",
) -> dict:
    raw = profile.raw_metrics
    units = profile.metric_units

    read_bw = _first_raw(raw, ("L2_Fabric-Rd BW", "L2_Fabric-Read BW", "HBM-Rd BW", "HBM Read BW")) or 0.0
    write_bw = _first_raw(raw, ("L2_Fabric-Wr BW", "L2_Fabric-Write BW", "HBM-Wr BW", "HBM Write BW")) or 0.0
    hbm_bw = read_bw + write_bw
    memory_util, memory_source = _best_percent_metric(raw, units, (
        r"hbm.*util",
        r"memory.*util",
    ))
    if memory_util is None and hbm_bw > 0:
        mem_spec = gpu_peak_spec(state.get("env", {}))
        peak_bw = mem_spec.get("peak_bw_gbs")
        if peak_bw:
            memory_util = min(100.0, hbm_bw / float(peak_bw) * 100.0)
            source_prefix = "HCU-Analyzer" if mem_spec.get("specs_available", True) else "explicit env"
            memory_source = f"L2_Fabric/HBM BW / {source_prefix} {mem_spec['model']} peak_bw_gbs({peak_bw})"

    _compute_pipe_active, _compute_pipe_source, compute_kind = _select_compute_util(raw, units)
    compute_throughput, compute_throughput_source, compute_throughput_unit = _compute_throughput_gops(raw, compute_kind)
    compute_peak, compute_peak_source = _compute_peak_from_pop(raw, compute_throughput, compute_kind, state)
    compute_util = None
    compute_source = ""
    if compute_throughput is not None and compute_peak is not None and compute_peak > 0:
        compute_util = min(100.0, compute_throughput / compute_peak * 100.0)
        compute_source = f"{compute_throughput_source} / inferred_{compute_kind}_peak_from({compute_peak_source})"

    l2_hit = _first_raw(raw, ("L2-Hit Rate", "L2 Hit Rate", "L2_Cache Hit Rate"))
    l1_hit = _first_raw(raw, ("VL1-Hit Rate", "L1-Hit Rate", "VL1 Hit Rate"))
    lds_conflict = _first_raw(raw, ("LDS-Bank Conficts/Access", "LDS-Bank Conflicts/Access", "LDS-Bank Conflict Rate"))
    lds_util = _first_raw(raw, ("LDS-Utilization", "LDS Utilization"))
    lds_bandwidth = _first_raw(raw, ("LDS-Bandwidth", "LDS Bandwidth"))
    lds_instrs = _first_raw(raw, ("LDS-Instrs", "LDS Instrs"))
    coalescing = _first_raw(raw, ("VL1-Buffer Coalescing", "VL1 Buffer Coalescing"))
    vl1_util = _first_raw(raw, ("VL1-Util", "VL1 Util"))
    vl1_stalled_l2 = _first_raw(raw, ("VL1-Stalled on L2 Data", "VL1 Stalled on L2 Data"))
    ta_busy = _first_raw(raw, ("TA-Busy", "TA Busy"))
    td_busy = _first_raw(raw, ("TD-Busy", "TD Busy"))
    il1_hit = _first_raw(raw, ("IL1-Hit Rate", "IL1 Hit Rate"))
    utcl1_hit = _first_raw(raw, ("VL1_UTCL1-Hit Ratio", "UTCL1-Hit Ratio", "UTCL1 Hit Ratio"))
    l2_read_req = _first_raw(raw, ("VL1_L2-Read", "L2-Read Req", "L2 Read Req"))
    l2_write_req = _first_raw(raw, ("VL1_L2-Write", "L2-Write Req", "L2 Write Req"))
    td_load = _first_raw(raw, ("TD-Load Instr", "TD Load Instr"))
    td_store = _first_raw(raw, ("TD-Store Instr", "TD Store Instr"))
    global_load_eff = _efficiency_pct(td_load, l2_read_req)
    global_store_eff = _efficiency_pct(td_store, l2_write_req)
    l2_bandwidth = _derived_l2_bandwidth(raw, profile.duration_us)

    by_axis = {"compute": [], "memory": [], "latency": []}
    for name, value in sorted(raw.items()):
        item = _metric_item(name, value, units.get(name, ""), profile.source_file)
        by_axis[_metric_axis(name)].append(item)

    derived: dict[str, Any] = {
        "kernel_name": profile.kernel_name,
        "dispatch_id": profile.dispatch_id,
        "duration_us": profile.duration_us,
        "hbm_bandwidth_gbs": round(hbm_bw, 4) if hbm_bw else None,
        "hbm_read_bandwidth_gbs": round(read_bw, 4) if read_bw else None,
        "hbm_write_bandwidth_gbs": round(write_bw, 4) if write_bw else None,
        "memory_util_pct": round(memory_util, 4) if memory_util is not None else None,
        "memory_util_source": memory_source or None,
        "compute_util_pct": round(compute_util, 4) if compute_util is not None else None,
        "compute_util_source": compute_source or None,
        "compute_util_kind": compute_kind,
        "compute_throughput_tops": round(compute_throughput / 1000.0, 4) if compute_throughput is not None else None,
        "compute_throughput_source": compute_throughput_source or None,
        "compute_throughput_unit": compute_throughput_unit or None,
        "compute_peak_tops": round(compute_peak / 1000.0, 4) if compute_peak is not None else None,
        "compute_peak_source": compute_peak_source or None,
        "l2_hit_rate_pct": round(l2_hit, 4) if l2_hit is not None else None,
        "l1_hit_rate_pct": round(l1_hit, 4) if l1_hit is not None else None,
        "lds_bank_conflict": round(lds_conflict, 4) if lds_conflict is not None else None,
        "lds_util_pct": round(lds_util, 4) if lds_util is not None else None,
        "lds_bandwidth_gbs": round(lds_bandwidth, 4) if lds_bandwidth is not None else None,
        "lds_instrs": round(lds_instrs, 4) if lds_instrs is not None else None,
        "vl1_buffer_coalescing_pct": round(coalescing, 4) if coalescing is not None else None,
        "vl1_util_pct": round(vl1_util, 4) if vl1_util is not None else None,
        "vl1_stalled_l2_data_pct": round(vl1_stalled_l2, 4) if vl1_stalled_l2 is not None else None,
        "ta_busy_pct": round(ta_busy, 4) if ta_busy is not None else None,
        "td_busy_pct": round(td_busy, 4) if td_busy is not None else None,
        "il1_hit_rate_pct": round(il1_hit, 4) if il1_hit is not None else None,
        "utcl1_hit_ratio_pct": round(utcl1_hit, 4) if utcl1_hit is not None else None,
        "global_load_efficiency_pct": round(global_load_eff, 4) if global_load_eff is not None else None,
        "global_store_efficiency_pct": round(global_store_eff, 4) if global_store_eff is not None else None,
        "l2_bandwidth_gbs": round(l2_bandwidth, 4) if l2_bandwidth is not None else None,
    }

    if compute_util is not None:
        by_axis["compute"].insert(0, {
            "name": "compute_utilization_pct",
            "value": compute_util,
            "unit": "%",
            "higher_is_worse": False,
            "source": compute_source,
            "kind": compute_kind,
        })
    if memory_util is not None:
        by_axis["memory"].insert(0, {
            "name": "memory_utilization_pct",
            "value": memory_util,
            "unit": "%",
            "higher_is_worse": False,
            "source": memory_source,
        })
    if hbm_bw:
        by_axis["memory"].insert(1, {
            "name": "hbm_bandwidth_gbs",
            "value": hbm_bw,
            "unit": "GB/s",
            "higher_is_worse": False,
            "source": "L2_Fabric-Rd BW + L2_Fabric-Wr BW",
        })

    metric_count = sum(len(v) for v in by_axis.values())
    notes = ["Profiling backend: xcu (XCompute)."]
    if memory_util is None:
        notes.append(
            "memory utilization unavailable: xcu does not expose HBM peak-normalized utilization; use hbm_bandwidth_gbs instead."
        )
    if compute_util is None:
        notes.append(
            "compute utilization unavailable: no measured compute throughput and matching percent-of-peak denominator were found."
        )
    if l2_hit is None:
        notes.append("L2 hit rate unavailable in selected xcu sections/output.")

    return {
        "degraded": metric_count == 0,
        "reason": None if metric_count else f"xcu produced no parseable metrics; see {log_path}",
        "profiled_file": solution,
        "backend": _detect_backend(solution),
        "profiler": "xcu",
        "profiler_output": str(out_dir),
        "xcu_output": str(out_dir),
        "xcu_log": log_path,
        "xcu_bin": xcu_bin,
        "xcu_sections": sections,
        "xcu_kernel_filter": kernel_filter or None,
        "xcu_kernel_filter_source": kernel_filter_source or None,
        "selected_kernel": profile.kernel_name,
        "dispatch_id": profile.dispatch_id,
        "duration_us": profile.duration_us,
        "available_dispatches": [
            {"dispatch_id": p.dispatch_id, "kernel_name": p.kernel_name, "duration_us": p.duration_us}
            for p in all_profiles
        ],
        "metric_count_collected": metric_count,
        "derived_metrics": derived,
        "notes": notes,
        **{axis: values[: max(20, state.get("ncu_num", state.get("hcu_num", 5)))] for axis, values in by_axis.items()},
    }


def _ensure_xprof_runtime() -> dict[str, Any]:
    """Best-effort compatibility shim for XCompute installations."""
    rocm_lib = Path("/opt/rocm/lib")
    candidates = (
        (Path("/opt/rocm-6.3.3/lib/libxprofiler.so"), Path("/opt/rocm-6.3.3/lib/xprofiler/metrics.xml")),
        (Path("/opt/dtk/lib/libxprofiler.so"), Path("/opt/dtk/lib/xprofiler/metrics.xml")),
    )
    src_so = src_xml = None
    for so, xml in candidates:
        if so.exists():
            src_so, src_xml = so, xml
            break
    if src_so is None:
        return {"attempted": False, "reason": "libxprofiler.so source not found"}
    try:
        rocm_lib.mkdir(parents=True, exist_ok=True)
        (rocm_lib / "xprofiler").mkdir(parents=True, exist_ok=True)
        dst_so = rocm_lib / "libxprofiler.so"
        dst_xml = rocm_lib / "xprofiler" / "metrics.xml"
        if not dst_so.exists():
            dst_so.symlink_to(src_so.resolve())
        if src_xml and src_xml.exists() and not dst_xml.exists():
            dst_xml.symlink_to(src_xml.resolve())
        return {"attempted": True, "ok": True, "libxprofiler": str(src_so), "metrics_xml": str(src_xml)}
    except OSError as exc:
        return {"attempted": True, "ok": False, "error": str(exc)}


def _run_xcu(
    *,
    xcu_bin: str,
    output_dir: Path,
    sections: str,
    benchmark_py: str,
    solution: str,
    state: dict,
    args: argparse.Namespace,
    env: dict[str, str],
) -> tuple[int, str, list[str]]:
    bench_cmd = [
        sys.executable, benchmark_py, solution,
        "--warmup", str(args.warmup),
        "--repeat", str(args.repeat),
    ]
    bench_cmd.extend(_ptr_size_argv(state.get("ptr_size", 0)))
    bench_cmd.extend(_config_argv(args))
    bench_cmd.extend(_dims_argv(state.get("dims", {})))
    bench_str = " ".join(shlex.quote(part) for part in bench_cmd)

    cmd = [
        xcu_bin, "profile",
        "-S", sections,
        "-D", str(output_dir),
        "-F", "csv",
    ]
    kernel_filter = getattr(args, "kernel_filter", "") or ""
    if kernel_filter:
        cmd.extend(["-K", kernel_filter.strip("*")])
    full_cmd = " ".join(shlex.quote(part) for part in cmd) + " " + bench_str
    run_env = env.copy()
    run_env["xcompute_lightweight"] = "ON"
    if run_env.get("HIP_VISIBLE_DEVICES") == "":
        run_env.pop("HIP_VISIBLE_DEVICES", None)

    print(f"[xcu] {full_cmd}", file=sys.stderr)
    try:
        result = subprocess.run(
            full_cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=args.timeout,
            env=run_env,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return -1, str(exc), [full_cmd]
    return result.returncode, (result.stdout or "") + "\n---STDERR---\n" + (result.stderr or ""), [full_cmd]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--state", required=True)
    p.add_argument("--iter", required=True, type=int)
    p.add_argument("--which", required=True, choices=["best_input", "kernel"])
    p.add_argument("--benchmark", default=_BUNDLED_BENCHMARK)
    p.add_argument("--warmup", type=int, default=1)
    p.add_argument("--repeat", type=int, default=3)
    p.add_argument("--xcu-bin", default="")
    p.add_argument("--kernel-name", default="", help="xcu -K filter; default: first two tokens of first @triton.jit def")
    p.add_argument("--no-kernel-filter", action="store_true", help="Profile all dispatches (no xcu -K)")
    p.add_argument("--sections", default=FULL_SECTIONS)
    p.add_argument("--quick", action="store_true")
    p.add_argument("--no-auto-select", action="store_true")
    p.add_argument("--timeout", type=int, default=900)
    p.add_argument("--promote-if-best", action="store_true")
    p.add_argument("--config-json", default="")
    p.add_argument("--config-path", default="")
    p.add_argument("--config-key", default="")
    p.add_argument("--disable-autotune", action="store_true")
    p.add_argument("--target-arch", default="")
    args = p.parse_args()

    xcu_bin = _find_xcu(args.xcu_bin)
    state = _read(args.state)
    run_dir = state["run_dir"]
    iter_dir = os.path.join(run_dir, f"iterv{args.iter}")
    os.makedirs(iter_dir, exist_ok=True)
    args = _effective_config_args(args, state, iter_dir)

    if args.which == "best_input":
        solution = state["best_file"]
        rep_name = "best_input.xcu"
    else:
        solution = next((os.path.join(iter_dir, f"kernel{ext}") for ext in KERNEL_EXTS if os.path.isfile(os.path.join(iter_dir, f"kernel{ext}"))), None)
        if not solution:
            sys.exit(f"No iterv{args.iter}/kernel.(hip|cu|cpp|cc|cxx|py) found.")
        rep_name = "kernel.xcu"

    if args.kernel_name:
        args.kernel_filter = args.kernel_name.strip("*")
    elif args.no_kernel_filter or not str(solution).endswith(".py"):
        args.kernel_filter = ""
    else:
        args.kernel_filter = _default_kernel_filter(solution)
    args.kernel_filter_source = _kernel_filter_source(args, solution)
    if args.kernel_filter:
        print(f"[xcu] kernel filter (-K): {args.kernel_filter}", file=sys.stderr)

    if not xcu_bin:
        top = {
            "degraded": True,
            "reason": "xcu not available",
            "profiled_file": solution,
            "backend": _detect_backend(solution),
            "profiler": "xcu",
            "xcu_kernel_filter": args.kernel_filter or None,
            "xcu_kernel_filter_source": args.kernel_filter_source,
            "selected_kernel": None,
            "install_hint": (
                "Install XCompute/xcu on the HCU runtime host. Use the latest internal "
                "xprofiler, hsa-aqlprofile, and XCompute packages for the target OS."
            ),
            "compute": [],
            "memory": [],
            "latency": [],
        }
        _write_json(os.path.join(iter_dir, "hcu_top.json"), top)
        print(json.dumps(top, indent=2, ensure_ascii=False))
        sys.exit(2)

    profile_cache_dir = _new_profile_cache_dir(iter_dir, args.which, "xcu")
    profile_env = os.environ.copy()
    profile_env["TRITON_CACHE_DIR"] = profile_cache_dir
    os.environ["TRITON_CACHE_DIR"] = profile_cache_dir

    sections = QUICK_SECTIONS if args.quick else args.sections
    out_dir = Path(iter_dir) / rep_name
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = os.path.join(iter_dir, f"{rep_name}.log")
    runtime_setup = _ensure_xprof_runtime()
    artifact_since_unix = time.time()
    rc, log, commands = _run_xcu(
        xcu_bin=xcu_bin,
        output_dir=out_dir,
        sections=sections,
        benchmark_py=os.path.abspath(args.benchmark),
        solution=solution,
        state=state,
        args=args,
        env=profile_env,
    )
    Path(log_path).write_text(
        json.dumps({"commands": commands, "runtime_setup": runtime_setup}, indent=2, ensure_ascii=False)
        + "\n\n"
        + log,
        encoding="utf-8",
    )
    if rc != 0:
        top = {
            "degraded": True,
            "reason": f"xcu rc={rc}; see {log_path}",
            "profiled_file": solution,
            "backend": _detect_backend(solution),
            "profiler": "xcu",
            "profiler_output": str(out_dir),
            "xcu_output": str(out_dir),
            "xcu_log": log_path,
            "xcu_bin": xcu_bin,
            "xcu_sections": sections,
            "xcu_kernel_filter": args.kernel_filter or None,
            "xcu_kernel_filter_source": args.kernel_filter_source,
            "selected_kernel": None,
            "triton_cache_dir": profile_cache_dir,
            "compute": [],
            "memory": [],
            "latency": [],
        }
        _write_json(os.path.join(iter_dir, "hcu_top.json"), top)
        print(json.dumps(top, indent=2, ensure_ascii=False))
        sys.exit(1)

    profiles = _collect_profiles(out_dir)
    selected = _select_profiles(profiles, args.kernel_filter, auto_select=not args.no_auto_select)
    if len(selected) > 1:
        selected = [max(selected, key=lambda p: p.duration_us)]
    if not selected:
        top = {
            "degraded": True,
            "reason": f"xcu produced no kernel CSV profiles in {out_dir}; see {log_path}",
            "profiled_file": solution,
            "backend": _detect_backend(solution),
            "profiler": "xcu",
            "profiler_output": str(out_dir),
            "xcu_output": str(out_dir),
            "xcu_log": log_path,
            "xcu_bin": xcu_bin,
            "xcu_sections": sections,
            "xcu_kernel_filter": args.kernel_filter or None,
            "xcu_kernel_filter_source": args.kernel_filter_source,
            "selected_kernel": None,
            "available_dispatches": [
                {"dispatch_id": p.dispatch_id, "kernel_name": p.kernel_name, "duration_us": p.duration_us}
                for p in profiles
            ],
            "triton_cache_dir": profile_cache_dir,
            "compute": [],
            "memory": [],
            "latency": [],
        }
        _write_json(os.path.join(iter_dir, "hcu_top.json"), top)
        print(json.dumps(top, indent=2, ensure_ascii=False))
        sys.exit(1)

    top = _build_hcu_top(
        profile=selected[0],
        all_profiles=profiles,
        state=state,
        solution=solution,
        out_dir=out_dir,
        log_path=log_path,
        sections=sections,
        xcu_bin=xcu_bin,
        kernel_filter=args.kernel_filter,
        kernel_filter_source=args.kernel_filter_source,
    )
    top["triton_cache_dir"] = profile_cache_dir

    artifact_manifest = None
    extract_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract_triton_irs.py")
    if solution.endswith(".py") and os.path.isfile(extract_script):
        manifest_name = f"{args.which}.artifact_manifest.json"
        manifest_path = os.path.join(iter_dir, manifest_name)
        archive_dir = os.path.join(iter_dir, "irs", args.which)
        cmd = [
            sys.executable, extract_script,
            "--kernel", solution,
            "--iter-dir", iter_dir,
            "--out", manifest_path,
            "--active-config-json", json.dumps(_active_config_for_manifest(args)),
            "--since-unix", str(artifact_since_unix),
            "--archive-dir", archive_dir,
        ]
        subprocess.run(cmd, text=True)
        if os.path.isfile(manifest_path):
            artifact_manifest = manifest_path
            shutil.copy2(manifest_path, os.path.join(iter_dir, "artifact_manifest.json"))
    top["artifact_manifest"] = artifact_manifest

    _write_json(os.path.join(iter_dir, "hcu_top.json"), top)

    if args.which == "kernel" and args.promote_if_best and os.path.abspath(solution) == os.path.abspath(state.get("best_file", "")):
        state["best_hipprof_output"] = str(out_dir)
        state["best_profile_output"] = str(out_dir)
        state["best_profile_backend"] = "xcu"
        with open(args.state, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

    print(json.dumps({
        "profiler": "xcu",
        "xcu_output": str(out_dir),
        "hcu_top": os.path.join(iter_dir, "hcu_top.json"),
        "degraded": top.get("degraded"),
        "metrics": top.get("metric_count_collected"),
        "selected_kernel": top.get("selected_kernel"),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
