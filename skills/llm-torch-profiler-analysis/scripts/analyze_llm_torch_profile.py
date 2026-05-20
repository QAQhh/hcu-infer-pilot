"""Compact triage entrypoint for unified LLM torch-profiler analysis."""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import triage_kernel_helpers as kernel_helpers
import triage_overlap_helpers as overlap_helpers
from profile_common import (
    DEFAULT_DECODE_INPUT_LEN,
    DEFAULT_DECODE_OUTPUT_LEN,
    DEFAULT_PREFILL_INPUT_LEN,
    DEFAULT_PREFILL_OUTPUT_LEN,
    DEFAULT_WARMUP_STEPS,
    PROFILE_WORKLOAD_CHOICES,
    discover_trace_targets,
    framework_display_name,
    load_server_args,
    load_trace_json,
    parse_stage,
    resolve_framework,
    run_profiler,
)

MIN_RENDER_SHARE_PCT = 1.0
MIN_KERNEL_TABLE_ROWS = 15
MAPPING_KERNEL_SAMPLE_LIMIT_PER_NAME = 16
BUBBLE_MIN_GAP_US = 10.0
BUBBLE_RENDER_ROWS = 20


def add_boolean_flag(
    parser: argparse.ArgumentParser, name: str, default: bool, help_text: str
) -> None:
    if default:
        parser.add_argument(f"--no-{name}", dest=name, action="store_false", help=help_text)
        parser.set_defaults(**{name: True})
    else:
        parser.add_argument(f"--{name}", dest=name, action="store_true", help=help_text)
        parser.set_defaults(**{name: False})


def build_triage_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="analyze_llm_torch_profile.py",
        description=(
            "Compact LLM torch-profiler triage entrypoint for SGLang, vLLM, and "
            "TensorRT-LLM. "
            "This prints the kernel, overlap-opportunity, fuse-pattern, and "
            "bubble-gap sections in one analysis document. "
            "Use either a single trace/profile input or a mapping+formal two-trace pair."
        ),
    )
    parser.add_argument(
        "--framework",
        type=str,
        default="auto",
        choices=["auto", "sglang", "vllm", "trtllm", "tllm", "tensorrt-llm"],
        help=(
            "Serving framework. Use auto to detect from trace contents, path hints, "
            "or URL features."
        ),
    )
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Single trace file or profile directory to triage.",
    )
    parser.add_argument(
        "--url",
        type=str,
        default=None,
        help=(
            "Running server URL for single-trace triage. SGLang supports direct "
            "capture via sglang.profiler. vLLM and TensorRT-LLM require a server-side "
            "torch-profiler output path exposed via --output-dir."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help=(
            "Trace output dir when using --url. For vLLM this should match the "
            "server's torch_profiler_dir. For TensorRT-LLM it should match the "
            "directory or file path configured by TLLM_TORCH_PROFILE_TRACE."
        ),
    )
    parser.add_argument(
        "--profile-prefix",
        type=str,
        default="triage-trace",
        help=(
            "Profile prefix when generating a trace from --url. SGLang uses it "
            "directly; vLLM and TensorRT-LLM may ignore it on the HTTP profiler path."
        ),
    )
    parser.add_argument(
        "--mapping-input",
        type=str,
        default=None,
        help="Graph-off mapping trace file or directory.",
    )
    parser.add_argument(
        "--mapping-url",
        type=str,
        default=None,
        help="Running graph-off server URL for the mapping trace.",
    )
    parser.add_argument(
        "--formal-input",
        type=str,
        default=None,
        help="Formal graph-on trace file or directory.",
    )
    parser.add_argument(
        "--formal-url",
        type=str,
        default=None,
        help="Running graph-on server URL for the formal trace.",
    )
    parser.add_argument(
        "--mapping-output-dir",
        type=str,
        default=None,
        help="Trace output dir when using --mapping-url.",
    )
    parser.add_argument(
        "--formal-output-dir",
        type=str,
        default=None,
        help="Trace output dir when using --formal-url.",
    )
    parser.add_argument(
        "--mapping-profile-prefix",
        type=str,
        default="mapping-trace",
        help="Profile prefix for the mapping trace.",
    )
    parser.add_argument(
        "--formal-profile-prefix",
        type=str,
        default="formal-trace",
        help="Profile prefix for the formal trace.",
    )
    parser.add_argument(
        "--num-steps",
        type=int,
        default=5,
        help="Active profiler steps when generating traces from URLs.",
    )
    parser.add_argument(
        "--warmup-steps",
        type=int,
        default=DEFAULT_WARMUP_STEPS,
        help="Warmup steps to run before arming the profiler for URL capture.",
    )
    add_boolean_flag(
        parser,
        "profile_by_stage",
        True,
        "Enable stage-separated profiling capture.",
    )
    add_boolean_flag(
        parser,
        "merge_profiles",
        False,
        "Merge generated profiler outputs when supported.",
    )
    parser.add_argument("--probe-requests", type=int, default=1)
    parser.add_argument(
        "--probe-prompt",
        type=str,
        default=(
            "Repeat the word profiler many times with spaces so the server performs several decode steps. "
            "Do not add explanations."
        ),
    )
    parser.add_argument("--probe-max-new-tokens", type=int, default=None)
    parser.add_argument("--probe-delay", type=float, default=0.5)
    parser.add_argument(
        "--profile-workload",
        choices=PROFILE_WORKLOAD_CHOICES,
        default="both",
        help=(
            "Live-capture workload shape. Default 'both' captures separate "
            "prefill and decode profiles instead of one mixed request. Use "
            "'legacy' to keep the old --probe-prompt behavior."
        ),
    )
    parser.add_argument(
        "--prefill-input-len",
        type=int,
        default=DEFAULT_PREFILL_INPUT_LEN,
        help="Synthetic input length for the prefill profile workload.",
    )
    parser.add_argument(
        "--prefill-output-len",
        type=int,
        default=DEFAULT_PREFILL_OUTPUT_LEN,
        help="Output length for the prefill profile workload.",
    )
    parser.add_argument(
        "--decode-input-len",
        type=int,
        default=DEFAULT_DECODE_INPUT_LEN,
        help="Synthetic input length for the decode profile workload.",
    )
    parser.add_argument(
        "--decode-output-len",
        type=int,
        default=DEFAULT_DECODE_OUTPUT_LEN,
        help="Output length for the decode profile workload.",
    )
    parser.add_argument(
        "--start-step",
        type=int,
        default=None,
        help="Pass through to sglang.profiler when generating traces from URLs.",
    )
    parser.add_argument(
        "--pid-substring",
        type=str,
        default=None,
        help="Restrict overlap analysis to PIDs containing this substring.",
    )
    parser.add_argument(
        "--kernel-table-limit",
        type=int,
        default=0,
        help="How many kernel rows to print per stage. Use 0 for all kernels.",
    )
    parser.add_argument(
        "--overlap-table-limit",
        type=int,
        default=0,
        help="How many overlap rows to print per stage. Use 0 for all kernels.",
    )
    return parser


def parse_triage_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = build_triage_parser()
    args = parser.parse_args(argv)

    single_trace_mode = bool(args.input) or bool(args.url)
    dual_trace_mode = any(
        [
            args.mapping_input,
            args.mapping_url,
            args.formal_input,
            args.formal_url,
        ]
    )

    if single_trace_mode and dual_trace_mode:
        parser.error(
            "Use either single-trace mode (--input/--url) or two-trace mode "
            "(--mapping-* plus --formal-*), not both."
        )

    if single_trace_mode:
        if bool(args.input) == bool(args.url):
            parser.error("Provide exactly one of --input or --url.")
        return args

    if bool(args.mapping_input) == bool(args.mapping_url):
        parser.error("Provide exactly one of --mapping-input or --mapping-url.")
    if bool(args.formal_input) == bool(args.formal_url):
        parser.error("Provide exactly one of --formal-input or --formal-url.")
    return args


def resolve_profile_targets(
    *,
    label: str,
    input_path: Optional[str],
    url: Optional[str],
    output_dir: Optional[str],
    profile_prefix: Optional[str],
    args: argparse.Namespace,
) -> Tuple[List[Path], Optional[dict], str]:
    if bool(input_path) == bool(url):
        raise ValueError(f"{label} trace requires exactly one of input path or URL.")

    if url:
        framework = resolve_framework(
            args.framework,
            input_path=Path(output_dir).resolve() if output_dir else None,
            url=url,
        )
        target_dir = run_profiler(
            url=url,
            output_dir=output_dir,
            num_steps=args.num_steps,
            profile_by_stage=args.profile_by_stage,
            merge_profiles=args.merge_profiles,
            profile_prefix=profile_prefix,
            probe_requests=max(0, args.probe_requests),
            probe_prompt=args.probe_prompt,
            probe_max_new_tokens=args.probe_max_new_tokens,
            probe_delay=args.probe_delay,
            warmup_steps=args.warmup_steps,
            start_step=args.start_step,
            framework=framework,
            framework_hint_path=output_dir,
            profile_workload=args.profile_workload,
            prefill_input_len=args.prefill_input_len,
            prefill_output_len=args.prefill_output_len,
            decode_input_len=args.decode_input_len,
            decode_output_len=args.decode_output_len,
        )
        traces, server_args = discover_trace_targets(target_dir, all_traces=False)
        resolved_framework = resolve_framework(
            args.framework,
            input_path=target_dir,
            url=url,
            server_args=server_args,
        )
        return traces, server_args, resolved_framework

    resolved = Path(input_path).resolve()
    traces, server_args = discover_trace_targets(resolved, all_traces=False)
    if server_args is None:
        server_args = load_server_args(resolved)
    framework = resolve_framework(
        args.framework, input_path=resolved, server_args=server_args
    )
    return traces, server_args, framework


def build_mapping_kernel_map(trace_paths: Sequence[Path], framework: str) -> dict:
    stage_site_stats = defaultdict(
        lambda: defaultdict(lambda: defaultdict(kernel_helpers.MappingSiteAggregate))
    )
    stage_kernel_categories: Dict[str, Dict[str, str]] = defaultdict(dict)
    global_site_stats = defaultdict(
        lambda: defaultdict(kernel_helpers.MappingSiteAggregate)
    )
    global_kernel_categories: Dict[str, str] = {}

    for trace_path in trace_paths:
        trace = load_trace_json(trace_path)
        kernels, cpu_ops, python_frames, launch_events, pid, _ = (
            kernel_helpers.extract_trace_data(trace)
        )
        if not kernels:
            continue
        cpu_ops_by_external_id = kernel_helpers.build_cpu_op_index(cpu_ops)
        launches_by_correlation = kernel_helpers.build_launch_index(launch_events)
        site_context_cache = {}
        default_stage = parse_stage(trace_path)
        for stage, stage_kernels in kernel_helpers.group_kernels_by_stage(
            kernels, default_stage
        ).items():
            sampled_stage_kernels = (
                stage_kernels
                if framework == "sglang"
                else sample_kernels_for_mapping(stage_kernels)
            )
            local_site_stats = kernel_helpers.aggregate_kernel_sites(
                sampled_stage_kernels,
                cpu_ops_by_external_id,
                python_frames,
                launches_by_correlation=launches_by_correlation,
                site_context_cache=site_context_cache,
            )
            kernel_categories = {
                kernel.canonical_name: kernel.category for kernel in stage_kernels
            }
            kernel_helpers.merge_site_stats(stage_site_stats[stage], local_site_stats)
            kernel_helpers.merge_site_stats(global_site_stats, local_site_stats)
            stage_kernel_categories[stage].update(kernel_categories)
            global_kernel_categories.update(kernel_categories)

    stage_payloads = {
        stage: kernel_helpers.build_stage_payload(
            dict(site_stats), stage_kernel_categories.get(stage, {})
        )
        for stage, site_stats in stage_site_stats.items()
    }
    global_payload = kernel_helpers.build_stage_payload(
        dict(global_site_stats), global_kernel_categories
    )
    return {"stages": stage_payloads, "global": global_payload}


def stage_index(stage: str) -> int:
    return {"extend": 0, "prefill": 0, "decode": 1, "all": 2}.get(stage, 99)


def sample_kernels_for_mapping(
    kernels: Sequence[kernel_helpers.KernelEvent],
    per_name_limit: int = MAPPING_KERNEL_SAMPLE_LIMIT_PER_NAME,
) -> List[kernel_helpers.KernelEvent]:
    if per_name_limit <= 0:
        return list(kernels)

    grouped: Dict[str, List[kernel_helpers.KernelEvent]] = defaultdict(list)
    for kernel in kernels:
        grouped[kernel.canonical_name].append(kernel)

    sampled: List[kernel_helpers.KernelEvent] = []
    for kernel_name in sorted(grouped):
        items = grouped[kernel_name]
        if len(items) <= per_name_limit:
            sampled.extend(items)
            continue
        for sample_idx in range(per_name_limit):
            pos = round(sample_idx * (len(items) - 1) / (per_name_limit - 1))
            sampled.append(items[pos])
    sampled.sort(key=lambda kernel: (kernel.ts, kernel.name))
    return sampled


def stage_display(stage: str) -> str:
    return kernel_helpers.stage_label(stage)


def stage_workload_note(stage: str, args: argparse.Namespace) -> str:
    if stage in {"extend", "prefill"}:
        return f"input_len={args.prefill_input_len}, output_len={args.prefill_output_len}"
    if stage == "decode":
        return f"input_len={args.decode_input_len}, output_len={args.decode_output_len}"
    return (
        "input/output lengths: "
        f"prefill {args.prefill_input_len}->{args.prefill_output_len}, "
        f"decode {args.decode_input_len}->{args.decode_output_len}"
    )


def pick_stage_value(stage_to_value: Dict[str, object], stage: str) -> Optional[object]:
    if stage in stage_to_value:
        return stage_to_value[stage]
    if "all" in stage_to_value:
        return stage_to_value["all"]
    if len(stage_to_value) == 1:
        return next(iter(stage_to_value.values()))
    return None


def render_stages(stage_to_value: Dict[str, object]) -> List[str]:
    stages = set(stage_to_value)
    if any(stage != "all" for stage in stages):
        stages.discard("all")
    return sorted(stages, key=stage_index)


def build_overlap_stage_bundle_map(
    trace_paths: Sequence[Path],
    *,
    label_prefix: str,
    server_args: Optional[dict],
    pid_substring: Optional[str],
) -> Dict[str, overlap_helpers.TraceBundle]:
    stage_bundles: Dict[str, overlap_helpers.TraceBundle] = {}
    for trace_path in sorted(
        trace_paths, key=lambda item: (stage_index(parse_stage(item)), item.name)
    ):
        trace_json = load_trace_json(trace_path)
        raw_events = trace_json.get(
            "traceEvents",
            trace_json if isinstance(trace_json, list) else [],
        )
        events, pid = overlap_helpers.extract_kernel_events(trace_json, pid_substring)
        if not events:
            continue
        default_stage = parse_stage(trace_path)
        stage_groups = overlap_helpers.group_events_by_stage(events, default_stage)
        for stage in render_stages(stage_groups):
            if stage in stage_bundles:
                continue
            stage_bundles[stage] = overlap_helpers.TraceBundle(
                label=f"{label_prefix}-{stage}",
                trace_path=trace_path,
                server_args=server_args,
                raw_events=raw_events,
                events=stage_groups[stage],
                pid=pid,
            )
        if "all" in stage_groups and not stage_bundles:
            stage_bundles["all"] = overlap_helpers.TraceBundle(
                label=f"{label_prefix}-all",
                trace_path=trace_path,
                server_args=server_args,
                raw_events=raw_events,
                events=stage_groups["all"],
                pid=pid,
            )
    return stage_bundles


def group_rows_by_stage(rows: Sequence[dict]) -> List[Tuple[str, List[dict]]]:
    grouped: Dict[str, List[dict]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("stage") or "all")].append(row)
    return [
        (stage, grouped[stage]) for stage in sorted(grouped.keys(), key=stage_index)
    ]


def render_kernel_table_for_stage(rows: Sequence[dict]) -> List[str]:
    lines = [
        "| Kernel | Category | GPU time | Share | Launches | Python location (site share) | CPU op |",
        "| --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    if not rows:
        lines.append(
            "| No kernel rows at or above 1.0% share. | - | - | - | - | - | - |"
        )
        return lines
    for row in rows:
        lines.append(
            "| {kernel} | {category} | {gpu_time} | {share:.1f}% | {launches} | {location} | {cpu_op} |".format(
                kernel=kernel_helpers.escape_md_cell(row["kernel"]),
                category=kernel_helpers.escape_md_cell(row["category"]),
                gpu_time=kernel_helpers.format_ms(row["total_us"]),
                share=row["share_pct"],
                launches=row["launches"],
                location=kernel_helpers.escape_md_cell(row["location"]),
                cpu_op=kernel_helpers.escape_md_cell(row["cpu_op"]),
            )
        )
    return lines


def render_stage_section_tables(
    rows: Sequence[dict],
    *,
    render_stage_fn,
    stage_label_prefix: str = "#####",
    stage_note_fn=None,
) -> List[str]:
    if not rows:
        return render_stage_fn([])
    stage_groups = group_rows_by_stage(rows)
    if len(stage_groups) == 1 and stage_groups[0][0] == "all":
        return render_stage_fn(stage_groups[0][1])

    lines: List[str] = []
    for index, (stage, stage_rows) in enumerate(stage_groups):
        note = f" ({stage_note_fn(stage)})" if stage_note_fn else ""
        lines.append(f"{stage_label_prefix} {stage_display(stage)}{note}")
        lines.extend(render_stage_fn(stage_rows))
        if index != len(stage_groups) - 1:
            lines.append("")
    return lines


def render_kernel_tables(rows: Sequence[dict], args: argparse.Namespace) -> List[str]:
    return render_stage_section_tables(
        rows,
        render_stage_fn=render_kernel_table_for_stage,
        stage_note_fn=lambda stage: stage_workload_note(stage, args),
    )


def select_kernel_rows_for_render(
    rows: Sequence[kernel_helpers.KernelRow],
    *,
    total_us: float,
    table_limit: int,
) -> List[Tuple[kernel_helpers.KernelRow, float]]:
    selected: List[Tuple[kernel_helpers.KernelRow, float]] = []
    seen = set()
    limited_rows = kernel_helpers.limit_kernel_rows(rows, table_limit)
    for row in limited_rows:
        share_pct = kernel_helpers.pct(row.total_us, total_us)
        if share_pct < MIN_RENDER_SHARE_PCT:
            continue
        selected.append((row, share_pct))
        seen.add(row.name)

    target_rows = MIN_KERNEL_TABLE_ROWS
    if table_limit > 0:
        target_rows = min(target_rows, table_limit)
    if len(selected) >= target_rows:
        return selected

    for row in limited_rows:
        if row.name in seen:
            continue
        selected.append((row, kernel_helpers.pct(row.total_us, total_us)))
        seen.add(row.name)
        if len(selected) >= target_rows:
            break
    return selected


def stage_trace_label(stage: str) -> str:
    label = kernel_helpers.stage_label(stage)
    if label == "extend/prefill":
        return "Extend/prefill"
    return label[:1].upper() + label[1:] if label else label


def bubble_ms(value_us: float) -> str:
    return f"{value_us / 1000.0:.3f} ms"


def bubble_trace_root(trace_paths: Sequence[Path]) -> Optional[Path]:
    if not trace_paths:
        return None
    common = os.path.commonpath([str(path.parent) for path in trace_paths])
    return Path(common)


def bubble_kernel_site(payload: dict, kernel_name: str) -> Tuple[str, str]:
    entry = kernel_helpers.relaxed_kernel_entry_lookup(payload.get("kernels", {}), kernel_name)
    loc, cpu = kernel_helpers.best_site_summary(entry)
    return loc or "-", cpu or "-"


def bubble_global_idle_stats(kernels: Sequence[kernel_helpers.KernelEvent]) -> dict:
    intervals = sorted((kernel.ts, kernel.ts + kernel.dur) for kernel in kernels)
    if not intervals:
        return {
            "count": 0,
            "total": 0.0,
            "busy": 0.0,
            "window": 0.0,
            "max": 0.0,
            "avg": 0.0,
        }

    merged = []
    cur_start, cur_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))

    gaps = []
    for (_, prev_end), (next_start, _) in zip(merged, merged[1:]):
        gap = next_start - prev_end
        if gap > 0:
            gaps.append(gap)

    total = sum(gaps)
    window = merged[-1][1] - merged[0][0]
    busy = sum(end - start for start, end in merged)
    return {
        "count": len(gaps),
        "total": total,
        "busy": busy,
        "window": window,
        "max": max(gaps) if gaps else 0.0,
        "avg": total / len(gaps) if gaps else 0.0,
    }


def bubble_per_stream_gaps(
    kernels: Sequence[kernel_helpers.KernelEvent],
) -> Tuple[List[dict], Dict[str, List[kernel_helpers.KernelEvent]]]:
    by_stream = defaultdict(list)
    for kernel in kernels:
        by_stream[kernel.tid].append(kernel)

    gaps: List[dict] = []
    for stream, items in by_stream.items():
        items.sort(key=lambda kernel: (kernel.ts, kernel.dur))
        for prev_kernel, next_kernel in zip(items, items[1:]):
            gap = next_kernel.ts - (prev_kernel.ts + prev_kernel.dur)
            if gap > 0:
                gaps.append(
                    {
                        "stream": stream,
                        "gap": gap,
                        "prev": prev_kernel,
                        "next": next_kernel,
                    }
                )
    gaps.sort(key=lambda item: item["gap"], reverse=True)
    return gaps, by_stream


def bubble_group_prev_next_gaps(gaps: Sequence[dict], payload: dict):
    output = defaultdict(lambda: [0.0, 0, 0.0, Counter()])
    for gap in gaps:
        prev_kernel = gap["prev"]
        next_kernel = gap["next"]
        prev_loc, _ = bubble_kernel_site(payload, prev_kernel.canonical_name)
        next_loc, next_cpu = bubble_kernel_site(payload, next_kernel.canonical_name)
        key = (
            gap["stream"],
            prev_kernel.canonical_name,
            prev_loc.split("<br>")[0],
            next_kernel.canonical_name,
            next_loc.split("<br>")[0],
        )
        output[key][0] += gap["gap"]
        output[key][1] += 1
        output[key][2] = max(output[key][2], gap["gap"])
        output[key][3][next_cpu.split("<br>")[0]] += 1
    return sorted(output.items(), key=lambda item: item[1][0], reverse=True)


def bubble_group_next_operator(gaps: Sequence[dict], payload: dict):
    output = defaultdict(lambda: [0.0, 0, 0.0, Counter()])
    for gap in gaps:
        next_kernel = gap["next"]
        next_loc, next_cpu = bubble_kernel_site(payload, next_kernel.canonical_name)
        key = (next_kernel.canonical_name, next_loc.split("<br>")[0])
        output[key][0] += gap["gap"]
        output[key][1] += 1
        output[key][2] = max(output[key][2], gap["gap"])
        output[key][3][next_cpu.split("<br>")[0]] += 1
    return sorted(output.items(), key=lambda item: item[1][0], reverse=True)


def render_bubble_gap_rows(gaps: Sequence[dict], payload: dict, total_gap: float) -> List[str]:
    lines = [
        "| 排名 | Stream | Gap 总时长 | 占比 | 出现次数 | 最大单次 gap | 前一个 kernel 名字 | 前一个 kernel 的 python 端调用位置 | 后一个 kernel 名字 | 后一个 kernel 的 python 端调用位置 | CPU op |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |",
    ]
    grouped = bubble_group_prev_next_gaps(gaps, payload)
    for rank, (
        (
            stream,
            prev_kernel_name,
            prev_loc,
            next_kernel_name,
            next_loc,
        ),
        (gap_total, count, max_gap, cpu_counter),
    ) in enumerate(grouped[:BUBBLE_RENDER_ROWS], 1):
        next_cpu = cpu_counter.most_common(1)[0][0] if cpu_counter else "-"
        lines.append(
            f"| {rank} | {stream} | {bubble_ms(gap_total)} | "
            f"{kernel_helpers.pct(gap_total, total_gap):.1f}% | {count} | "
            f"{bubble_ms(max_gap)} | "
            f"`{kernel_helpers.escape_md_cell(prev_kernel_name)}` | "
            f"{kernel_helpers.escape_md_cell(prev_loc)} | "
            f"`{kernel_helpers.escape_md_cell(next_kernel_name)}` | "
            f"{kernel_helpers.escape_md_cell(next_loc)} | "
            f"{kernel_helpers.escape_md_cell(next_cpu)} |"
        )
    if not grouped[:BUBBLE_RENDER_ROWS]:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - |")
    return lines


def render_bubble_next_kernel_rows(
    gaps: Sequence[dict], payload: dict, total_gap: float
) -> List[str]:
    lines = [
        "| 排名 | 后一个 kernel 名字 | python 端调用位置 | CPU op | Gap 总量 | 占 >=10us gap 比例 | 次数 | 最大 gap |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    grouped = bubble_group_next_operator(gaps, payload)
    for rank, ((kernel_name, loc), (gap_total, count, max_gap, cpu_counter)) in enumerate(
        grouped[:BUBBLE_RENDER_ROWS], 1
    ):
        cpu = cpu_counter.most_common(1)[0][0] if cpu_counter else "-"
        lines.append(
            f"| {rank} | `{kernel_helpers.escape_md_cell(kernel_name)}` | "
            f"{kernel_helpers.escape_md_cell(loc)} | {kernel_helpers.escape_md_cell(cpu)} | "
            f"{bubble_ms(gap_total)} | {kernel_helpers.pct(gap_total, total_gap):.1f}% | "
            f"{count} | {bubble_ms(max_gap)} |"
        )
    if not grouped[:BUBBLE_RENDER_ROWS]:
        lines.append("| - | - | - | - | - | - | - | - |")
    return lines


def render_bubble_stage_section(
    stage: str,
    trace_path: Path,
    kernels: Sequence[kernel_helpers.KernelEvent],
    payload: dict,
    pid: str,
) -> List[str]:
    gstats = bubble_global_idle_stats(kernels)
    stream_gaps, streams = bubble_per_stream_gaps(kernels)
    big_gaps = [gap for gap in stream_gaps if gap["gap"] >= BUBBLE_MIN_GAP_US]
    total_stream_gap = sum(gap["gap"] for gap in stream_gaps)
    big_stream_gap = sum(gap["gap"] for gap in big_gaps)

    lines: List[str] = []
    lines.append(f"## {kernel_helpers.stage_label(stage)} 阶段")
    lines.append("")
    lines.append(f"- Trace 文件: `{trace_path}`")
    lines.append(f"- GPU pid: `{pid}`")
    lines.append(f"- Kernel 数量: `{len(kernels)}`")
    lines.append(f"- Stream 数量: `{len(streams)}`")
    lines.append("")
    lines.append("### Global Idle Bubble")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("| --- | ---: |")
    lines.append(f"| Global wall window | {kernel_helpers.format_ms(gstats['window'])} |")
    lines.append(f"| Global busy union | {kernel_helpers.format_ms(gstats['busy'])} |")
    lines.append(
        f"| Global idle bubble 总量 | {kernel_helpers.format_ms(gstats['total'])} |"
    )
    lines.append(
        f"| Global idle 占比 | {kernel_helpers.pct(gstats['total'], gstats['window']):.2f}% |"
    )
    lines.append(f"| Global idle gap 数量 | {gstats['count']} |")
    lines.append(f"| 最大单个 Global idle gap | {kernel_helpers.format_ms(gstats['max'])} |")
    lines.append(f"| 平均 Global idle gap | {kernel_helpers.format_ms(gstats['avg'])} |")
    lines.append("")
    lines.append("### Per-Stream Gap 总览")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("| --- | ---: |")
    lines.append(f"| Per-stream gap 总量 | {kernel_helpers.format_ms(total_stream_gap)} |")
    lines.append(
        f"| >=10us 的 per-stream gap 总量 | {kernel_helpers.format_ms(big_stream_gap)} |"
    )
    lines.append(f"| >=10us 的 per-stream gap 数量 | {len(big_gaps)} |")
    lines.append("")
    lines.append("### Top Per-Stream Gap 合并表")
    lines.append("")
    lines.extend(render_bubble_gap_rows(big_gaps, payload, big_stream_gap))
    lines.append("")
    lines.append("### Gap 按后一个 kernel 聚合")
    lines.append("")
    lines.extend(render_bubble_next_kernel_rows(big_gaps, payload, big_stream_gap))
    return lines


def render_bubble_analysis(
    stage_records: Dict[str, dict],
    trace_paths: Sequence[Path],
) -> List[str]:
    lines: List[str] = []
    if not stage_records:
        return lines

    lines.append("## 算子间空泡分析")
    lines.append("")
    lines.append("### 分析 trace 目录")
    lines.append("")
    trace_root = bubble_trace_root(trace_paths)
    if trace_root is not None:
        lines.append(f"- Trace 根目录: `{trace_root}`")
    for stage in sorted(stage_records, key=stage_index):
        trace_path = stage_records[stage]["trace_path"]
        lines.append(f"- {stage_trace_label(stage)} trace: `{trace_path}`")
    lines.append("")
    lines.append("### 指标说明")
    lines.append("")
    lines.append("| 指标 | 说明 |")
    lines.append("| --- | --- |")
    lines.append(
        "| Global idle bubble | 把所有 GPU stream 的 kernel interval 合并后，统计没有任何 GPU kernel 运行的间隔，更接近真实 GPU 空闲。 |"
    )
    lines.append(
        "| Per-stream gap | 在同一个 stream 上，相邻两个 kernel 之间的间隔。这个间隔可能和其他 stream 的 kernel 重叠，因此主要用来定位算子链断点。 |"
    )
    lines.append("")
    lines.append("#### Global Idle Bubble 说明")
    lines.append("")
    lines.append(
        "`Global idle bubble` 是设备视角的空泡。计算时会先把同一个 GPU 上所有 stream 的 kernel 执行区间合并成一个全局 busy 时间线，然后统计这些 busy 区间之间没有任何 kernel 运行的间隔。"
    )
    lines.append("")
    lines.append(
        "因此这个指标更接近“GPU 真的空着没有干活”的时间。它适合用来判断是否存在明显的全局调度空洞、CPU 没及时提交 kernel、同步等待、数据传输等待等问题。如果 `Global idle bubble` 占比很低，说明即使某个 stream 上有间隔，其他 stream 往往仍有 kernel 在运行，设备整体没有长时间闲置。"
    )
    lines.append("")
    lines.append("表中的几个字段含义如下:")
    lines.append("")
    lines.append("- `Global wall window`: 当前 trace 中第一个 kernel 开始到最后一个 kernel 结束的总时间窗口。")
    lines.append("- `Global busy union`: 合并所有 stream 后，至少有一个 kernel 正在运行的总时间。")
    lines.append("- `Global idle bubble 总量`: `Global wall window - Global busy union`，即全局没有 kernel 运行的总时间。")
    lines.append("- `Global idle 占比`: `Global idle bubble 总量 / Global wall window`。")
    lines.append("- `最大单个 Global idle gap`: 单次最长的全局空闲间隔，用来定位是否有少数特别大的空泡。")
    lines.append("")
    lines.append("#### Per-Stream Gap 说明")
    lines.append("")
    lines.append(
        "`Per-stream gap` 是 stream 内算子链视角的间隔。计算时只看同一个 stream 上相邻两个 kernel，后一个 kernel 的开始时间减去前一个 kernel 的结束时间，就是这两个 kernel 之间的 gap。"
    )
    lines.append("")
    lines.append(
        "这个指标不等同于真实 GPU 空闲，因为某个 stream 空着时，其他 stream 可能正在运行 kernel。所以 `Per-stream gap` 的总量通常会大于 `Global idle bubble`，两者不能直接相加，也不能把 per-stream gap 全部理解成设备浪费时间。"
    )
    lines.append("")
    lines.append(
        "`Per-stream gap` 的主要用途是定位“算子链在哪些位置断开”。本报告会把相同 `stream + 前一个 kernel + 前一个 python 端调用位置 + 后一个 kernel + 后一个 python 端调用位置` 的 gap 合并到一行，累加其耗时，便于看出空泡集中出现在哪些前后算子位置。"
    )
    lines.append("")
    lines.append("表中的几个字段含义如下:")
    lines.append("")
    lines.append("- `Stream`: gap 所在的 GPU stream。")
    lines.append("- `Gap 总时长`: 相同前后位置的 gap 累加耗时。")
    lines.append("- `占比`: 该类 gap 在当前阶段 `>=10us` per-stream gap 总量中的比例。")
    lines.append("- `出现次数`: 相同前后位置重复出现的次数。")
    lines.append("- `最大单次 gap`: 该类 gap 中最长的一次。")
    lines.append("- `前一个/后一个 kernel 名字`: gap 两侧的 kernel。")
    lines.append("- `python 端调用位置`: kernel 对应的主要 Python 调用位置，用来回溯源码路径。")

    for stage in sorted(stage_records, key=stage_index):
        info = stage_records[stage]
        lines.append("")
        lines.extend(
            render_bubble_stage_section(
                stage,
                info["trace_path"],
                info["kernels"],
                info["payload"],
                info["pid"],
            )
        )
    return lines


def render_overlap_table_for_stage(rows: Sequence[dict]) -> List[str]:
    lines = [
        "| Priority | Verdict | Kernel | Python scope | Formal signal | Dep risk | Recommendation |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    if not rows:
        lines.append(
            "| - | - | No rows cleared the 1.0% reporting bar. Use mapping/formal mode for overlap attribution. | - | - | - | - |"
        )
        return lines
    for row in rows:
        formal_signal = (
            f"{row['total_us']:.1f} us, share {row['share_pct']:.1f}%, "
            f"excl {row['exclusive_ratio'] * 100:.1f}% / hid {row['hidden_ratio'] * 100:.1f}%"
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    row["priority"],
                    row["verdict"],
                    kernel_helpers.escape_md_cell(row["kernel"]),
                    kernel_helpers.escape_md_cell(row["python_scope"]),
                    kernel_helpers.escape_md_cell(formal_signal),
                    overlap_helpers.dependency_risk_label(row["dependency_signal"]),
                    row["recommendation"],
                ]
            )
            + " |"
        )
    return lines


def render_overlap_tables(rows: Sequence[dict]) -> List[str]:
    return render_stage_section_tables(
        rows,
        render_stage_fn=render_overlap_table_for_stage,
    )


def render_fuse_table_for_stage(rows: Sequence[dict]) -> List[str]:
    lines = [
        "| Pattern | Confidence | Related GPU time | Share | Evidence kernels | Current kernel Python location | Candidate fused Python path | Rationale |",
        "| --- | --- | ---: | ---: | --- | --- | --- | --- |",
    ]
    if not rows:
        lines.append(
            "| No medium-confidence source-backed fusion opportunity matched this trace. | - | - | - | - | - | - | - |"
        )
        return lines
    for row in rows:
        lines.append(
            "| {pattern} | {confidence} | {gpu_time} | {share:.1f}% | {evidence} | {current_locations} | {candidate_path} | {rationale} |".format(
                pattern=kernel_helpers.escape_md_cell(row["pattern"]),
                confidence=kernel_helpers.escape_md_cell(row["confidence"]),
                gpu_time=kernel_helpers.format_ms(row["related_us"]),
                share=row["share_pct"],
                evidence=kernel_helpers.escape_md_cell(row["evidence"]),
                current_locations=kernel_helpers.escape_md_cell(
                    row["current_locations"]
                ),
                candidate_path=kernel_helpers.escape_md_cell(row["candidate_path"]),
                rationale=kernel_helpers.escape_md_cell(row["rationale"]),
            )
        )
    return lines


def render_fuse_tables(rows: Sequence[dict]) -> List[str]:
    return render_stage_section_tables(
        rows,
        render_stage_fn=render_fuse_table_for_stage,
    )


def run_triage(args: argparse.Namespace) -> int:
    single_trace_mode = bool(args.input) or bool(args.url)
    if single_trace_mode:
        formal_traces, formal_server_args, formal_framework = resolve_profile_targets(
            label="input",
            input_path=args.input,
            url=args.url,
            output_dir=args.output_dir,
            profile_prefix=args.profile_prefix,
            args=args,
        )
        mapping_traces = formal_traces
        mapping_server_args = formal_server_args
        mapping_framework = formal_framework
    else:
        mapping_traces, mapping_server_args, mapping_framework = (
            resolve_profile_targets(
                label="mapping",
                input_path=args.mapping_input,
                url=args.mapping_url,
                output_dir=args.mapping_output_dir,
                profile_prefix=args.mapping_profile_prefix,
                args=args,
            )
        )
        formal_traces, formal_server_args, formal_framework = resolve_profile_targets(
            label="formal",
            input_path=args.formal_input,
            url=args.formal_url,
            output_dir=args.formal_output_dir,
            profile_prefix=args.formal_profile_prefix,
            args=args,
        )

    mapping_kernel_map = build_mapping_kernel_map(mapping_traces, mapping_framework)

    kernel_rows_rendered: List[dict] = []
    fuse_rows_rendered: List[dict] = []
    formal_stage_payloads: Dict[str, dict] = {}
    bubble_stage_records: Dict[str, dict] = {}

    for formal_trace in formal_traces:
        trace = load_trace_json(formal_trace)
        kernels, cpu_ops, python_frames, launch_events, pid, _ = (
            kernel_helpers.extract_trace_data(trace)
        )
        if not kernels:
            continue
        default_stage = parse_stage(formal_trace)
        stage_groups = kernel_helpers.group_kernels_by_stage(kernels, default_stage)
        formal_cpu_ops_by_external_id = kernel_helpers.build_cpu_op_index(cpu_ops)
        formal_launches_by_correlation = kernel_helpers.build_launch_index(
            launch_events
        )
        formal_site_context_cache = {}
        for stage_name, stage_kernels in stage_groups.items():
            local_site_stats = kernel_helpers.aggregate_kernel_sites(
                stage_kernels,
                formal_cpu_ops_by_external_id,
                python_frames,
                launches_by_correlation=formal_launches_by_correlation,
                site_context_cache=formal_site_context_cache,
            )
            formal_stage_payloads[stage_name] = kernel_helpers.build_stage_payload(
                local_site_stats,
                {kernel.canonical_name: kernel.category for kernel in stage_kernels},
            )
            bubble_stage_records[stage_name] = {
                "trace_path": formal_trace,
                "pid": pid,
                "kernels": stage_kernels,
                "payload": formal_stage_payloads[stage_name],
            }
        trace_total_us = sum(kernel.dur for kernel in kernels)
        for stage in sorted(stage_groups, key=stage_index):
            stage_kernels = stage_groups[stage]
            if not stage_kernels:
                continue
            total_us = sum(kernel.dur for kernel in stage_kernels)
            if (
                stage == "all"
                and default_stage == "all"
                and kernel_helpers.pct(total_us, trace_total_us) < MIN_RENDER_SHARE_PCT
            ):
                continue
            kernel_stats = kernel_helpers.aggregate(
                stage_kernels, key_fn=lambda item: item.canonical_name
            )
            kernel_categories = {
                kernel.canonical_name: kernel.category for kernel in stage_kernels
            }
            full_kernel_rows = kernel_helpers.build_kernel_rows(
                stage=stage,
                kernel_stats=kernel_stats,
                kernel_categories=kernel_categories,
                local_stage_payload=formal_stage_payloads.get(stage, {"kernels": {}}),
                external_kernel_map=mapping_kernel_map,
            )
            visible_kernel_rows = select_kernel_rows_for_render(
                full_kernel_rows,
                total_us=total_us,
                table_limit=args.kernel_table_limit,
            )
            for row, share_pct in visible_kernel_rows:
                kernel_rows_rendered.append(
                    {
                        "stage": stage,
                        "kernel": row.name,
                        "category": row.category,
                        "total_us": row.total_us,
                        "share_pct": share_pct,
                        "launches": row.aggregate.count,
                        "location": row.location,
                        "cpu_op": row.cpu_op,
                    }
                )
            for item in kernel_helpers.detect_fusion_opportunities(
                kernel_rows=full_kernel_rows,
                total_us=total_us,
                server_args=formal_server_args or mapping_server_args,
                framework=formal_framework,
            ):
                share_pct = kernel_helpers.pct(item.related_us, total_us)
                if share_pct < MIN_RENDER_SHARE_PCT:
                    continue
                fuse_rows_rendered.append(
                    {
                        "stage": stage,
                        "pattern": item.pattern,
                        "confidence": item.confidence,
                        "related_us": item.related_us,
                        "share_pct": share_pct,
                        "evidence": item.evidence,
                        "current_locations": item.current_locations,
                        "candidate_path": item.candidate_path,
                        "rationale": item.rationale,
                    }
                )

    overlap_rows_rendered: List[dict] = []
    if not single_trace_mode:
        mapping_overlap_bundles = build_overlap_stage_bundle_map(
            mapping_traces,
            label_prefix="mapping",
            server_args=mapping_server_args,
            pid_substring=args.pid_substring,
        )
        formal_overlap_bundles = build_overlap_stage_bundle_map(
            formal_traces,
            label_prefix="formal",
            server_args=formal_server_args,
            pid_substring=args.pid_substring,
        )
        for stage in render_stages(formal_overlap_bundles):
            formal_bundle = pick_stage_value(formal_overlap_bundles, stage)
            mapping_bundle = pick_stage_value(mapping_overlap_bundles, stage)
            if formal_bundle is None or mapping_bundle is None:
                continue
            formal_bundle.overlap_stats = overlap_helpers.analyze_overlap(
                formal_bundle.events
            )
            aggregates = overlap_helpers.aggregate_events(formal_bundle.events)
            source_map = overlap_helpers.build_kernel_source_map(
                mapping_bundle,
                kernel_map_entry_lookup=lambda stage_name, kernel_name: (
                    kernel_helpers.lookup_kernel_map_entry(
                        mapping_kernel_map, stage_name, kernel_name
                    )
                    if mapping_kernel_map
                    else None
                ),
                stage=stage,
            )
            source_map = overlap_helpers.merge_source_map_from_kernel_payload(
                source_map,
                pick_stage_value(formal_stage_payloads, stage),
            )
            stage_rows = overlap_helpers.build_action_rows(
                aggregates,
                source_map,
                formal_bundle.events,
                formal_bundle.overlap_stats["total_busy_us"],
                table_limit=max(0, args.overlap_table_limit),
            )
            for row in stage_rows:
                if row.share_pct < MIN_RENDER_SHARE_PCT:
                    continue
                overlap_rows_rendered.append(
                    {
                        "stage": stage,
                        "priority": row.priority,
                        "verdict": row.verdict,
                        "kernel": row.kernel,
                        "python_scope": row.python_scope,
                        "total_us": row.total_us,
                        "share_pct": row.share_pct,
                        "exclusive_ratio": row.exclusive_ratio,
                        "hidden_ratio": row.hidden_ratio,
                        "dependency_signal": row.dependency_signal,
                        "recommendation": row.recommendation,
                    }
                )

    lines: List[str] = []
    lines.append("Triage View")
    lines.append(f"Mode: {'single-trace' if single_trace_mode else 'mapping-formal'}")
    if single_trace_mode:
        lines.append(f"Framework: {framework_display_name(formal_framework)}")
        lines.append(f"Input traces: {', '.join(str(path) for path in formal_traces)}")
    else:
        if mapping_framework == formal_framework:
            lines.append(f"Framework: {framework_display_name(formal_framework)}")
        else:
            lines.append(
                f"Mapping framework: {framework_display_name(mapping_framework)}"
            )
            lines.append(
                f"Formal framework: {framework_display_name(formal_framework)}"
            )
        lines.append(
            f"Mapping traces: {', '.join(str(path) for path in mapping_traces)}"
        )
        lines.append(f"Formal traces: {', '.join(str(path) for path in formal_traces)}")
    if formal_server_args or mapping_server_args:
        server_args = formal_server_args or mapping_server_args
        model = server_args.get("model_path") or server_args.get("model")
        if model:
            lines.append(f"Model: {model}")
    lines.append("")
    lines.append("Kernel Table")
    lines.extend(render_kernel_tables(kernel_rows_rendered, args))
    lines.append("")
    lines.append("Overlap Opportunity Table")
    lines.extend(render_overlap_tables(overlap_rows_rendered))
    lines.append("")
    lines.append("Fuse Opportunity Table")
    lines.extend(render_fuse_tables(fuse_rows_rendered))
    lines.append("")
    lines.extend(render_bubble_analysis(bubble_stage_records, formal_traces))
    print("\n".join(lines).rstrip())
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = list(argv or sys.argv[1:])
    triage_parser = build_triage_parser()

    if not argv or argv[0] in {"-h", "--help"}:
        triage_parser.print_help()
        return 0

    if argv[0] == "triage":
        argv = argv[1:]
    elif not argv[0].startswith("-"):
        triage_parser.error(
            "This skill exposes only the triage workflow. "
            "Use single-trace mode (--input/--url) or mapping+formal two-trace mode."
        )
        return 2

    return run_triage(parse_triage_args(argv))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
