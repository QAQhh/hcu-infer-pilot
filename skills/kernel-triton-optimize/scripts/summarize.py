#!/usr/bin/env python3
"""Render run_dir/summary.md from state.json + per-iteration artifacts (v2).

Includes roofline history, axis budget tracking, attribution results,
and HCU ISA verification status.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
from pathlib import Path


def _read(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _fmt_ms(v) -> str:
    return f"{v:.4f} ms" if v is not None else "n/a"


def _fmt_speedup(v) -> str:
    return f"{v:.2f}x" if v is not None else "n/a"


def _fmt_num(v, suffix: str = "", digits: int = 2) -> str:
    if v is None:
        return "n/a"
    try:
        return f"{float(v):.{digits}f}{suffix}"
    except (TypeError, ValueError):
        return str(v)


def _fmt_bytes(v) -> str:
    try:
        value = float(v)
    except (TypeError, ValueError):
        return "n/a"
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value /= 1024
        idx += 1
    return f"{value:.2f} {units[idx]}"


def _fmt_pct(v) -> str:
    if v is None:
        return "n/a"
    try:
        value = float(v)
    except (TypeError, ValueError):
        return str(v)
    sign = "+" if value >= 0 else ""
    return f"{sign}{value:.2f}%"


def _fmt_percent_plain(v, digits: int = 2) -> str:
    if v is None:
        return "n/a"
    try:
        return f"{float(v):.{digits}f}%"
    except (TypeError, ValueError):
        return str(v)


def _safe_float(value):
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _tool_status(info: dict) -> str:
    if not info:
        return "unavailable"
    if not info.get("available"):
        return "unavailable"
    version = info.get("version") or info.get("path") or "available"
    return str(version)


def _method_bullets(methods: list[dict]) -> str:
    if not methods:
        return "_(none)_"
    lines = []
    for m in methods:
        axis = m.get("axis", "?")
        name = m.get("name", m.get("id", "?"))
        extra = ""
        if "iter" in m:
            extra = f" _(iter {m['iter']})_"
        if "attribution_ms" in m and m["attribution_ms"] is not None:
            extra += f" - attribution +{m['attribution_ms']:.3f}ms"
        if "speedup_vs_best_before" in m and m["speedup_vs_best_before"] is not None:
            extra += f" - speedup {m['speedup_vs_best_before']:.2f}x"
        if "note" in m:
            extra += f" [{m['note']}]"
        lines.append(f"- **[{axis}]** {name}{extra}")
    return "\n".join(lines)


def _effective_methods_for_summary(state: dict) -> list[dict]:
    methods: list[dict] = []
    seen: set[str] = set()
    for method in state.get("effective_methods", []) or []:
        if not isinstance(method, dict):
            continue
        name = str(method.get("name") or method.get("id") or "")
        if name and name not in seen:
            methods.append(method)
            seen.add(name)
    for hist in state.get("history", []) or []:
        if not isinstance(hist, dict) or hist.get("status") != "improved":
            continue
        ids = hist.get("methods") or []
        names = hist.get("method_names") or ids
        for idx, name in enumerate(names):
            label = str(name)
            if not label or label in seen:
                continue
            methods.append({
                "id": ids[idx] if idx < len(ids) else label,
                "name": label,
                "axis": "promoted",
                "iter": hist.get("iter"),
                "speedup_vs_best_before": hist.get("speedup_vs_best_before"),
            })
            seen.add(label)
    return methods


def _timeline_table(state: dict) -> str:
    rows = [
        "| Iter | 状态 | 方法 | ms | 相对前最佳 | 相对 reference |",
        "|------|------|------|----|------------|----------------|",
    ]
    for h in state.get("history", []):
        methods = ", ".join(h.get("method_names") or h.get("methods") or [])
        rows.append(
            f"| {h['iter']} "
            f"| {h['status']} "
            f"| {methods} "
            f"| {_fmt_ms(h.get('ms'))} "
            f"| {_fmt_speedup(h.get('speedup_vs_best_before'))} "
            f"| {_fmt_speedup(h.get('speedup_vs_ref'))} |"
        )
    return "\n".join(rows)


def _md_cell(value) -> str:
    text = "-" if value is None or value == "" else str(value)
    return text.replace("|", "\\|").replace("\n", "<br>")


def _attempt_event_key(event: dict) -> tuple:
    return (
        event.get("iter"),
        event.get("kind"),
        event.get("sequence"),
        event.get("timestamp"),
        event.get("champion_branch"),
        event.get("champion_config_key"),
    )


def _load_attempt_events(state: dict, run_dir: str) -> list[dict]:
    events: list[dict] = []
    seen = set()
    for event in state.get("attempt_timeline", []):
        if not isinstance(event, dict):
            continue
        key = _attempt_event_key(event)
        events.append(event)
        seen.add(key)

    run = Path(run_dir)
    for iter_dir in sorted(run.glob("iterv*")):
        path = iter_dir / "attempt_timeline.json"
        if not path.is_file():
            continue
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(loaded, dict):
            loaded = [loaded]
        if not isinstance(loaded, list):
            continue
        for event in loaded:
            if not isinstance(event, dict):
                continue
            key = _attempt_event_key(event)
            if key in seen:
                continue
            events.append(event)
            seen.add(key)
        analysis = iter_dir / "analysis.md"
        if analysis.is_file() and not any(
            e.get("kind") == "semantic_rewrite" and e.get("iter") == _iter_no_from_dir(iter_dir)
            for e in events
            if isinstance(e, dict)
        ):
            synthetic = _semantic_rewrite_event_from_analysis(analysis)
            if synthetic:
                key = _attempt_event_key(synthetic)
                if key not in seen:
                    events.append(synthetic)
                    seen.add(key)
    return sorted(events, key=lambda e: (e.get("iter") or 0, e.get("sequence") or 0, e.get("timestamp") or ""))


def _iter_no_from_dir(iter_dir: Path) -> int | None:
    try:
        return int(iter_dir.name.replace("iterv", "", 1))
    except ValueError:
        return None


def _semantic_rewrite_event_from_analysis(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    heading_re = re.compile(
        r"^#{2,4}\s+(?P<title>.*(?:Promoted\s+Semantic\s+Rewrite|Semantic\s+Rewrite|语义重写).*)$",
        re.IGNORECASE | re.MULTILINE,
    )
    match = heading_re.search(text)
    if not match:
        return None
    title = match.group("title").strip()
    iter_no = _iter_no_from_dir(path.parent)
    promoted = "promoted" in title.lower() or "已采纳" in title or "晋级" in title
    return {
        "kind": "semantic_rewrite",
        "iter": iter_no,
        "sequence": -10,
        "candidate": title,
        "status": "success" if promoted else "failure",
        "outcome": "recorded_in_analysis_md",
        "analysis": str(path),
    }


def _load_catalog_method_lookup() -> dict[str, dict]:
    """Load current method axis/priority metadata from the installed skill files."""
    references_dir = Path(__file__).resolve().parents[1] / "references"
    lookup: dict[str, dict] = {}

    registry_path = references_dir / "triton_method_registry.json"
    if registry_path.is_file():
        try:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception:
            registry = {}
        for method_id, meta in (registry.get("methods") or {}).items():
            if isinstance(meta, dict):
                entry = dict(meta)
                entry.setdefault("id", method_id)
                lookup[str(method_id)] = entry

    catalog_path = references_dir / "triton_optimization_catalog.md"
    if catalog_path.is_file():
        axis = None
        axis_re = re.compile(r"^##\s+(Compute|Memory|Latency)\s+Axis\b", re.IGNORECASE)
        method_re = re.compile(r"^###\s+P(\d+)\s*:\s*`([^`]+)`")
        try:
            lines = catalog_path.read_text(encoding="utf-8").splitlines()
        except Exception:
            lines = []
        for line in lines:
            axis_match = axis_re.match(line)
            if axis_match:
                axis = axis_match.group(1).lower()
                continue
            method_match = method_re.match(line)
            if method_match and axis:
                priority, method_id = method_match.groups()
                entry = lookup.setdefault(method_id, {"id": method_id})
                # The Markdown catalog is what humans edit/read, so keep these
                # display fields synchronized with its current headings.
                entry["axis"] = axis
                entry["priority"] = int(priority)

    return lookup


def _load_iter_method_lookup(run_dir: str) -> dict[int, dict[str, dict]]:
    catalog_lookup = _load_catalog_method_lookup()
    lookup: dict[int, dict[str, dict]] = {}
    run = Path(run_dir)
    for iter_dir in sorted(run.glob("iterv*")):
        if not iter_dir.is_dir():
            continue
        try:
            iter_no = int(iter_dir.name.replace("iterv", "", 1))
        except ValueError:
            continue
        methods_path = iter_dir / "methods.json"
        if not methods_path.is_file():
            continue
        try:
            data = json.loads(methods_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        methods = data.get("methods", [])
        if not isinstance(methods, list):
            continue
        for method in methods:
            if not isinstance(method, dict):
                continue
            method_id = method.get("id")
            if not method_id:
                continue
            method_id = str(method_id)
            merged = dict(method)
            catalog_method = catalog_lookup.get(method_id)
            if catalog_method:
                merged.update({
                    k: catalog_method[k]
                    for k in ("axis", "priority")
                    if k in catalog_method
                })
            lookup.setdefault(iter_no, {})[method_id] = merged
    return lookup


def _axis_label(axis) -> str:
    axis_str = str(axis or "?").strip()
    labels = {
        "compute": "Compute Axis",
        "memory": "Memory Axis",
        "latency": "Latency Axis",
    }
    return labels.get(axis_str.lower(), f"{axis_str.title()} Axis" if axis_str != "?" else "Unknown Axis")


def _priority_label(priority) -> str:
    if priority is None or priority == "":
        return "P?"
    text = str(priority).strip()
    return text.upper() if text.lower().startswith("p") else f"P{text}"


def _format_attempt_method(method, iter_lookup: dict[str, dict]) -> str:
    if isinstance(method, dict):
        method_id = str(method.get("id") or method.get("name") or "?")
        registry_method = iter_lookup.get(method_id, {})
        merged = dict(registry_method)
        merged.update({k: v for k, v in method.items() if v is not None and v != ""})
    else:
        method_id = str(method)
        merged = dict(iter_lookup.get(method_id, {}))
        merged.setdefault("id", method_id)
    axis = _axis_label(merged.get("axis"))
    priority = _priority_label(merged.get("priority"))
    method_id = str(merged.get("id") or method_id)
    return f"{axis} {priority}: {method_id}"


def _attempt_method_label(event: dict, method_lookup: dict[int, dict[str, dict]] | None = None) -> str:
    method_lookup = method_lookup or {}
    iter_lookup = method_lookup.get(event.get("iter"), {})
    labels = []
    for method in event.get("methods", []) or []:
        labels.append(_format_attempt_method(method, iter_lookup))
    return "<br>".join(labels)


def _config_tune_status(event: dict) -> str:
    """Classify a merged config sweep by its best result vs the previous best."""
    if event.get("passed") is False:
        return "failure"
    outcome = str(event.get("outcome") or "").lower()
    if "no_config_promoted" in outcome or "not_faster" in outcome:
        return "failure"
    change_pct = _safe_float(event.get("change_vs_previous_best_pct"))
    if change_pct is not None:
        return "success" if change_pct > 0.0 else "failure"
    speedup = _safe_float(event.get("speedup_vs_previous_best"))
    if speedup is not None:
        return "success" if speedup > 1.0 else "failure"
    ms = _safe_float(event.get("champion_ms", event.get("ms")))
    previous = _safe_float(event.get("previous_best_ms"))
    if ms is not None and previous is not None:
        return "success" if ms < previous else "failure"
    return event.get("status") or "failure"


def _flatten_attempts(events: list[dict], method_lookup: dict[int, dict[str, dict]] | None = None) -> list[dict]:
    rows: list[dict] = []
    attempt_no = 0
    for event in events:
        kind = event.get("kind", "attempt")
        method_label = _attempt_method_label(event, method_lookup)
        if kind == "branch_explore":
            candidates = event.get("branches") if isinstance(event.get("branches"), list) else []
            for candidate in candidates:
                if not isinstance(candidate, dict):
                    continue
                attempt_no += 1
                rows.append({
                    "attempt": attempt_no,
                    "iter": event.get("iter"),
                    "kind": kind,
                    "candidate": f"b{candidate.get('branch_index', '?')}",
                    "status": candidate.get("status") or ("success" if event.get("status") == "success" else "failure"),
                    "outcome": candidate.get("outcome") or event.get("outcome"),
                    "ms": candidate.get("ms"),
                    "change_pct": candidate.get("change_vs_previous_best_pct"),
                    "delta_ms": candidate.get("delta_vs_previous_best_ms"),
                    "speedup": candidate.get("speedup_vs_previous_best"),
                    "passed": candidate.get("passed"),
                    "methods": method_label,
                    "previous_best_ms": event.get("previous_best_ms"),
                })
            if candidates:
                continue

        attempt_no += 1
        configs = event.get("configs") if isinstance(event.get("configs"), list) else []
        candidate_name = (
            event.get("candidate")
            or event.get("rewrite")
            or event.get("champion_branch")
            or event.get("champion_config_key")
            or kind
        )
        if kind == "config_tune":
            if configs:
                candidate_name = f"config_sweep({len(configs)} configs"
            else:
                candidate_name = f"config_sweep({candidate_name}"
            if event.get("champion_config_key"):
                candidate_name += f", best={event['champion_config_key']}"
            candidate_name += ")"
        status = event.get("status") or "failure"
        if kind == "config_tune":
            status = _config_tune_status(event)
        rows.append({
            "attempt": attempt_no,
            "iter": event.get("iter"),
            "kind": kind,
            "candidate": candidate_name,
            "status": status,
            "outcome": event.get("outcome"),
            "ms": event.get("champion_ms", event.get("ms")),
            "change_pct": event.get("change_vs_previous_best_pct"),
            "delta_ms": event.get("delta_vs_previous_best_ms"),
            "speedup": event.get("speedup_vs_previous_best"),
            "passed": event.get("passed"),
            "methods": method_label,
            "previous_best_ms": event.get("previous_best_ms"),
            "config_count": len(configs) if kind == "config_tune" else None,
        })
    return rows


def _write_attempt_timeline_svg(rows: list[dict], baseline_ms, out_path: str) -> str:
    measured = [row for row in rows if row.get("ms") is not None]
    if not measured and baseline_ms is None:
        return ""

    width, height = 980, 420
    left, right, top, bottom = 72, 30, 32, 58
    plot_w = width - left - right
    plot_h = height - top - bottom
    values = [float(row["ms"]) for row in measured]
    if baseline_ms is not None:
        values.append(float(baseline_ms))
    min_y = min(values)
    max_y = max(values)
    pad = max((max_y - min_y) * 0.12, max_y * 0.03, 0.001)
    y_min = max(0.0, min_y - pad)
    y_max = max_y + pad
    total_x = max(len(rows), 1)

    def x_pos(idx: int) -> float:
        if total_x <= 1:
            return left + plot_w / 2
        return left + ((idx - 1) / (total_x - 1)) * plot_w

    def y_pos(ms: float) -> float:
        return top + (y_max - ms) / (y_max - y_min) * plot_h

    def wrap_text(value, max_chars: int = 52) -> list[str]:
        text = re.sub(r"\s+", " ", str(value or "")).strip()
        if not text:
            return []
        chunks: list[str] = []
        while len(text) > max_chars:
            cut = text.rfind(" ", 0, max_chars)
            if cut < max_chars // 2:
                cut = max_chars
            chunks.append(text[:cut].strip())
            text = text[cut:].strip()
        if text:
            chunks.append(text)
        return chunks

    def tooltip_lines(row: dict) -> list[str]:
        result = "success" if row.get("status") == "success" else "not promoted"
        methods = re.sub(r"<br\s*/?>", "; ", str(row.get("methods") or "-"))
        lines = [
            f"#{row.get('attempt')} iter {row.get('iter', '-')} {row.get('kind', '-')}: {result}",
        ]
        lines.extend(wrap_text(f"candidate: {row.get('candidate', '-')}", 56))
        lines.append(f"time: {_fmt_ms(row.get('ms'))}, vs previous best: {_fmt_pct(row.get('change_pct'))}")
        outcome = row.get("outcome")
        if outcome:
            lines.extend(wrap_text(f"outcome: {outcome}", 56))
        if methods and methods != "-":
            lines.extend(wrap_text(f"methods: {methods}", 56))
        return lines[:8]

    def tooltip_svg(row: dict, x: float, y: float) -> str:
        tip_lines = tooltip_lines(row)
        line_h = 14
        tip_w = 360
        tip_h = 18 + line_h * len(tip_lines)
        tx = x + 14
        if tx + tip_w > width - 8:
            tx = x - tip_w - 14
        ty = y - tip_h - 12
        if ty < 8:
            ty = y + 14
        items = [
            f'<g class="tooltip" transform="translate({tx:.1f},{ty:.1f})">',
            f'<rect class="tipbox" width="{tip_w}" height="{tip_h}" rx="6"/>',
        ]
        for i, line in enumerate(tip_lines):
            cls = "tiptext" if i == 0 else "tipmuted"
            items.append(
                f'<text class="{cls}" x="10" y="{16 + i * line_h}">{html.escape(line)}</text>'
            )
        items.append("</g>")
        return "".join(items)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#334155;font-size:12px}.small{font-size:11px;fill:#64748b}.axis{stroke:#94a3b8;stroke-width:1}.grid{stroke:#e2e8f0;stroke-width:1}.best{fill:none;stroke:#2563eb;stroke-width:2.4}.success{fill:#16a34a;stroke:white;stroke-width:1.5}.fail{stroke:#dc2626;stroke-width:2.2;stroke-linecap:round}.measure{fill:#cbd5e1;opacity:.55}.baseline{stroke:#7c3aed;stroke-width:1.6;stroke-dasharray:7 5}.band{fill:#f8fafc}.band2{fill:#eef6ff}.attempt-point{cursor:pointer}.attempt-point:focus{outline:none}.hit{fill:transparent;pointer-events:all}.tooltip{display:none;pointer-events:none}.attempt-point:hover .tooltip,.attempt-point:focus .tooltip{display:block}.tipbox{fill:#111827;stroke:#475569;stroke-width:1;opacity:.96}.tiptext{fill:#f8fafc;font-size:11px;font-weight:600}.tipmuted{fill:#d1d5db;font-size:10.5px}</style>',
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
    ]

    iters = sorted({row.get("iter") for row in rows if row.get("iter") is not None})
    for i, iter_no in enumerate(iters):
        iter_rows = [row for row in rows if row.get("iter") == iter_no]
        if not iter_rows:
            continue
        x1 = x_pos(min(row["attempt"] for row in iter_rows)) - 8
        x2 = x_pos(max(row["attempt"] for row in iter_rows)) + 8
        cls = "band" if i % 2 == 0 else "band2"
        parts.append(f'<rect class="{cls}" x="{max(left, x1):.1f}" y="{top}" width="{max(1, min(width - right, x2) - max(left, x1)):.1f}" height="{plot_h}" opacity="0.65"/>')
        parts.append(f'<text class="small" x="{max(left + 4, x1 + 4):.1f}" y="{top + 16}">iter {html.escape(str(iter_no))}</text>')

    for tick in range(5):
        value = y_min + (y_max - y_min) * tick / 4
        y = y_pos(value)
        parts.append(f'<line class="grid" x1="{left}" y1="{y:.1f}" x2="{width - right}" y2="{y:.1f}"/>')
        parts.append(f'<text class="small" x="{left - 10}" y="{y + 4:.1f}" text-anchor="end">{value:.4g}</text>')

    parts.append(f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{height - bottom}"/>')
    parts.append(f'<line class="axis" x1="{left}" y1="{height - bottom}" x2="{width - right}" y2="{height - bottom}"/>')
    parts.append(f'<text x="{width / 2:.1f}" y="{height - 16}" text-anchor="middle">attempt order</text>')
    parts.append(f'<text x="18" y="{height / 2:.1f}" transform="rotate(-90 18 {height / 2:.1f})" text-anchor="middle">latency (ms, lower is better)</text>')

    if baseline_ms is not None:
        y = y_pos(float(baseline_ms))
        parts.append(f'<line class="baseline" x1="{left}" y1="{y:.1f}" x2="{width - right}" y2="{y:.1f}"/>')
        parts.append(f'<text class="small" x="{width - right - 4}" y="{y - 6:.1f}" text-anchor="end">baseline {float(baseline_ms):.4g} ms</text>')

    best_points = []
    best = float(baseline_ms) if baseline_ms is not None else None
    for row in rows:
        ms = row.get("ms")
        if ms is not None:
            value = float(ms)
            if best is None or value < best:
                best = value
        if best is not None:
            best_points.append(f'{x_pos(row["attempt"]):.1f},{y_pos(best):.1f}')
    if best_points:
        parts.append(f'<polyline class="best" points="{" ".join(best_points)}"/>')

    for row in rows:
        x = x_pos(row["attempt"])
        ms = row.get("ms")
        title = (
            f"attempt {row['attempt']} | iter {row.get('iter')} | {row.get('candidate')} | "
            f"{_fmt_ms(ms)} | {_fmt_pct(row.get('change_pct'))} vs previous best | {row.get('outcome')}"
        )
        safe_title = html.escape(title)
        if ms is None:
            y = height - bottom - 5
        else:
            y = y_pos(float(ms))
        parts.append('<g class="attempt-point" tabindex="0">')
        parts.append(f'<title>{safe_title}</title>')
        parts.append(f'<circle class="hit" cx="{x:.1f}" cy="{y:.1f}" r="13"/>')
        if row.get("status") == "success":
            parts.append(f'<circle class="success" cx="{x:.1f}" cy="{y:.1f}" r="5"/>')
        else:
            parts.append(f'<line class="fail" x1="{x - 4:.1f}" y1="{y - 4:.1f}" x2="{x + 4:.1f}" y2="{y + 4:.1f}"/>')
            parts.append(f'<line class="fail" x1="{x - 4:.1f}" y1="{y + 4:.1f}" x2="{x + 4:.1f}" y2="{y - 4:.1f}"/>')
        parts.append(tooltip_svg(row, x, y))
        parts.append("</g>")

    parts.append(f'<circle class="success" cx="{left + 8}" cy="{top + 8}" r="4"/><text class="small" x="{left + 18}" y="{top + 12}">promoted success</text>')
    parts.append(f'<line class="fail" x1="{left + 150}" y1="{top + 4}" x2="{left + 158}" y2="{top + 12}"/><line class="fail" x1="{left + 150}" y1="{top + 12}" x2="{left + 158}" y2="{top + 4}"/><text class="small" x="{left + 166}" y="{top + 12}">failed / not promoted</text>')
    parts.append(f'<line class="best" x1="{left + 330}" y1="{top + 8}" x2="{left + 360}" y2="{top + 8}"/><text class="small" x="{left + 368}" y="{top + 12}">best-so-far</text>')
    parts.append("</svg>")

    svg_content = "\n".join(parts)
    svg_path = Path(out_path).with_name("attempt_timeline.svg")
    svg_path.write_text(svg_content, encoding="utf-8")
    return str(svg_path)


def _attempt_timeline_table(rows: list[dict], limit: int = 80) -> str:
    if not rows:
        return "- 没有发现 `attempt_timeline.json`；本次 summary 只能展示每轮最终历史，无法画出分支/配置尝试曲线。"
    lines = [
        "| # | Iter | 类型 | 候选 | 结果 | ms | vs 前最佳 | 说明 | 方法 |",
        "|---|------|------|------|------|----|-----------|------|------|",
    ]
    for row in rows[:limit]:
        result = "成功" if row.get("status") == "success" else "失败"
        methods = row.get("methods") or "-"
        lines.append(
            f"| {row['attempt']} "
            f"| {row.get('iter', '-')} "
            f"| {row.get('kind', '-')} "
            f"| `{_md_cell(row.get('candidate', '-'))}` "
            f"| {result} "
            f"| {_fmt_ms(row.get('ms'))} "
            f"| {_fmt_pct(row.get('change_pct'))} "
            f"| {_md_cell(row.get('outcome') or '-')} "
            f"| {_md_cell(methods)} |"
        )
    if len(rows) > limit:
        lines.append(f"| ... | ... | ... | ... | ... | ... | ... | 还有 {len(rows) - limit} 条，见 `attempt_timeline.json` | ... |")
    return "\n".join(lines)


def _iteration_step_timeline_table(state: dict, attempt_rows: list[dict]) -> str:
    by_iter: dict[int, list[dict]] = {}
    for row in attempt_rows:
        try:
            iter_no = int(row.get("iter"))
        except (TypeError, ValueError):
            continue
        by_iter.setdefault(iter_no, []).append(row)
    for h in state.get("history", []):
        try:
            iter_no = int(h.get("iter"))
        except (TypeError, ValueError):
            continue
        by_iter.setdefault(iter_no, [])

    if not by_iter:
        return _timeline_table(state)

    history_by_iter = {
        int(h["iter"]): h
        for h in state.get("history", [])
        if isinstance(h, dict) and h.get("iter") is not None
    }
    lines = [
        "| Iter | 优化动作 | 结果 | 最佳/候选 ms | 相对前最佳 | 备注 |",
        "|------|----------|------|--------------|------------|------|",
    ]
    for iter_no in sorted(by_iter):
        rows = by_iter.get(iter_no, [])
        hist = history_by_iter.get(iter_no, {})
        action_parts = []
        for row in rows:
            kind = row.get("kind")
            if kind == "config_tune":
                action_parts.append(f"config sweep: `{row.get('candidate')}`")
            elif kind == "semantic_rewrite":
                action_parts.append(f"semantic rewrite: `{row.get('candidate')}`")
            elif kind == "branch_explore":
                action_parts.append(f"branch `{row.get('candidate')}`")
            else:
                action_parts.append(f"{kind}: `{row.get('candidate')}`")
        if not action_parts and hist:
            action_parts.append(", ".join(hist.get("method_names") or hist.get("methods") or ["iteration close"]))
        promoted = [row for row in rows if row.get("status") == "success"]
        best_row = min(
            [row for row in rows if row.get("ms") is not None],
            key=lambda row: float(row["ms"]),
            default=None,
        )
        status = hist.get("status") or ("success" if promoted else "failure" if rows else "-")
        ms = hist.get("ms") if hist.get("ms") is not None else (best_row.get("ms") if best_row else None)
        speedup = hist.get("speedup_vs_best_before") or (best_row.get("speedup") if best_row else None)
        note = "; ".join(
            f"{row.get('kind')}={row.get('outcome')}"
            for row in rows
            if row.get("outcome")
        )
        lines.append(
            f"| {iter_no} "
            f"| {_md_cell('<br>'.join(action_parts) or '-')} "
            f"| {_md_cell(status)} "
            f"| {_fmt_ms(ms)} "
            f"| {_fmt_speedup(speedup)} "
            f"| {_md_cell(note or '-')} |"
        )
    return "\n".join(lines)


def _roofline_table(state: dict) -> str:
    rows = [
        "| Iter | Profiler | Bound | delta_compute | delta_memory | delta_latency | HBM GB/s | L2 Hit% | Budget (c,m,l) |",
        "|------|----------|-------|-----------|----------|-----------|----------|---------|----------------|",
    ]
    for r in state.get("roofline_history", []):
        budget = r.get("axis_budget", {})
        budget_str = f"({budget.get('compute','-')},{budget.get('memory','-')},{budget.get('latency','-')})"
        rows.append(
            f"| {r['iter']} "
            f"| {r.get('profiler', '-')} "
            f"| {r.get('bound', '?')} "
            f"| {r.get('delta_compute', '?')} "
            f"| {r.get('delta_memory', '?')} "
            f"| {r.get('delta_latency', '?')} "
            f"| {_fmt_num(r.get('hbm_bandwidth_gbs'), '', 2)} "
            f"| {_fmt_num(r.get('l2_hit_rate_pct'), '', 2)} "
            f"| {budget_str} |"
        )
    return "\n".join(rows)


def _kb_status(run_dir: str) -> tuple[str, list[dict]]:
    rows: list[dict] = []
    run = Path(run_dir)
    for iter_dir in sorted(run.glob("iterv*")):
        if not iter_dir.is_dir():
            continue
        status = "missing"
        path = ""
        reason = ""
        evidence = iter_dir / "kb_evidence.json"
        unavailable = iter_dir / "kb_unavailable.json"
        if evidence.is_file():
            status = "ok"
            path = str(evidence)
        elif unavailable.is_file():
            status = "unavailable"
            path = str(unavailable)
            try:
                reason = json.loads(unavailable.read_text(encoding="utf-8")).get("reason", "")
            except Exception:
                reason = ""
        rows.append({"iter": iter_dir.name, "status": status, "path": path, "reason": reason})

    if not rows:
        return "missing", []
    if any(row["status"] == "unavailable" for row in rows):
        return "degraded", rows
    if any(row["status"] == "missing" for row in rows):
        return "partial", rows
    return "ok", rows


def _best_history(state: dict) -> dict:
    best_file = os.path.abspath(state.get("best_file") or "")
    best_ms = state.get("best_metric_ms")
    for h in reversed(state.get("history", [])):
        h_file = os.path.abspath(h.get("kernel_file") or "")
        if best_file and h_file == best_file:
            return h
        if best_ms is not None and h.get("ms") == best_ms:
            return h
    return {}


def _final_bench(state: dict, run_dir: str) -> tuple[dict, str]:
    final_tune = state.get("final_tune") if isinstance(state.get("final_tune"), dict) else {}
    final_tune_path = final_tune.get("path")
    if final_tune_path and os.path.isfile(final_tune_path):
        try:
            tune = _read(final_tune_path)
        except Exception:
            tune = {}
        best = tune.get("best") if isinstance(tune.get("best"), dict) else {}
        bench_json = best.get("bench_json")
        best_ms = best.get("ms")
        state_best = state.get("best_metric_ms")
        same_best = (
            best_ms is not None
            and state_best is not None
            and abs(float(best_ms) - float(state_best)) <= max(1e-9, abs(float(state_best)) * 1e-6)
        )
        if bench_json and same_best and os.path.isfile(bench_json):
            return _read(bench_json), bench_json

    best = _best_history(state)
    candidates = []
    if best.get("iter") is not None:
        candidates.append(os.path.join(run_dir, f"iterv{best['iter']}", "bench.json"))
    best_file = os.path.abspath(state.get("best_file") or "")
    if best_file:
        candidates.append(os.path.join(os.path.dirname(best_file), "bench.json"))
    candidates.append(os.path.join(run_dir, "baseline", "bench.json"))
    for path in candidates:
        if path and os.path.isfile(path):
            return _read(path), path
    return {}, ""


def _final_roofline(state: dict, run_dir: str) -> tuple[dict, str]:
    for h in reversed(state.get("history", [])):
        if h.get("iter") is None:
            continue
        path = os.path.join(run_dir, f"iterv{h['iter']}", "roofline.json")
        if os.path.isfile(path):
            return _read(path), path
    for r in reversed(state.get("roofline_history", [])):
        if r.get("iter") is None:
            continue
        path = os.path.join(run_dir, f"iterv{r['iter']}", "roofline.json")
        if os.path.isfile(path):
            return _read(path), path
    return {}, ""


def _final_hcu_top(state: dict, run_dir: str) -> tuple[dict, str]:
    for h in reversed(state.get("history", [])):
        if h.get("iter") is None:
            continue
        path = os.path.join(run_dir, f"iterv{h['iter']}", "hcu_top.json")
        if os.path.isfile(path):
            return _read(path), path
    for r in reversed(state.get("roofline_history", [])):
        if r.get("iter") is None:
            continue
        path = os.path.join(run_dir, f"iterv{r['iter']}", "hcu_top.json")
        if os.path.isfile(path):
            return _read(path), path
    return {}, ""


def _active_config(state: dict, bench: dict) -> dict:
    return (
        state.get("best_config")
        or bench.get("active_config")
        or (_best_history(state).get("active_config") if _best_history(state) else None)
        or {}
    )


def _extract_markdown_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    rest = text.split(marker, 1)[1]
    next_heading = rest.find("\n## ")
    body = rest[:next_heading] if next_heading >= 0 else rest
    return body.strip()


def _has_python_reference(body: str) -> bool:
    if "```" not in body:
        return False
    return bool(re.search(r"\bdef\s+reference\b|\btorch\.|\bnp\.|\bnumpy\.", body))


def _has_formula(body: str) -> bool:
    formula_terms = [
        r"\b[A-Za-z_]\w*(?:\[[^\]]+\])?\s*=",
        r"\\sum",
        r"\\max",
        r"\\operatorname",
        r"\bmax\s*\(",
        r"\bsum\s*\(",
        r"\bsoftmax\s*\(",
        r"\bexp2?\s*\(",
        r"\bdot\s*\(",
        r"\beinsum\b",
        r"@",
        r"\u2200",
    ]
    return any(re.search(pattern, body) for pattern in formula_terms)


def _strip_python_reference_form(body: str) -> str:
    """Keep summary semantics formula-first by removing executable reference dumps."""
    text = re.sub(
        r"\n?###\s+Python Reference Form[\s\S]*?(?=\n###\s+|\n##\s+|\Z)",
        "\n",
        body,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\n?```(?:python)?[\s\S]*?\bdef\s+reference\b[\s\S]*?```\n?",
        "\n",
        text,
        flags=re.IGNORECASE,
    )
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _kernel_logic_section(state: dict, run_dir: str) -> str:
    """Copy semantic write-up, keeping the final report formula-first."""
    candidates: list[Path] = []
    best = _best_history(state)
    if best.get("iter") is not None:
        candidates.append(Path(run_dir) / f"iterv{best['iter']}" / "analysis.md")

    for hist in reversed(state.get("history", [])):
        if hist.get("iter") is not None:
            path = Path(run_dir) / f"iterv{hist['iter']}" / "analysis.md"
            if path not in candidates:
                candidates.append(path)

    for path in candidates:
        if not path.is_file():
            continue
        try:
            body = _extract_markdown_section(path.read_text(encoding="utf-8"), "Kernel Computation Logic")
        except OSError:
            continue
        if body:
            body = _strip_python_reference_form(body)
            lines = [f"_来源：`{path}`。_", "", body]
            if not _has_formula(body):
                lines.extend([
                    "",
                    "> **语义补充**：这里仍缺少显式数学公式。最终交付前请补成 `out[i] = ...`、`C[m,n] = ...` 或 LaTeX 求和式，而不是粘贴 Python Reference Form。",
                ])
            return "\n".join(lines)

    return (
        "_Degraded evidence: no non-empty `## Kernel Computation Logic` section was "
        "found in the promoted iteration's `analysis.md`. Fill this section with "
        "tensor roles, shape assumptions, and mathematical formulas before treating "
        "the summary as complete._"
    )


def _latency_us(kernel_stats: dict) -> float | None:
    ms = kernel_stats.get("average_ms") or kernel_stats.get("median_ms") or kernel_stats.get("min_ms")
    try:
        return float(ms) * 1000.0
    except (TypeError, ValueError):
        return None


def _compute_unit_label(derived: dict) -> str:
    unit = str(derived.get("compute_throughput_unit") or "")
    if "IOPs" in unit:
        return "TOP/s"
    return "TFLOP/s"


def _compute_domain_label(derived: dict) -> str:
    kind = str(derived.get("compute_util_kind") or "").lower()
    if kind == "mmop":
        return "MMAC/MMOP"
    if kind == "valu":
        return "VALU"
    return "compute"


def _first_existing(paths: list[str]) -> Path | None:
    for item in paths:
        path = Path(item)
        if path.is_file():
            return path
    return None


def _parse_amdgcn_resources(path: Path | None) -> dict:
    if not path:
        return {}
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {}

    def int_field(pattern: str) -> int | None:
        match = re.search(pattern, text, re.IGNORECASE)
        return int(match.group(1)) if match else None

    return {
        "amdgcn_path": str(path),
        "num_sgprs": int_field(r";\s*NumSgprs:\s*(\d+)"),
        "num_vgprs": int_field(r";\s*NumVgprs:\s*(\d+)"),
        "scratch_bytes": int_field(r";\s*ScratchSize:\s*(\d+)"),
        "lds_bytes": int_field(r";\s*LDSByteSize:\s*(\d+)\s*bytes/workgroup"),
        "sgpr_blocks": int_field(r";\s*SGPRBlocks:\s*(\d+)"),
        "vgpr_blocks": int_field(r";\s*VGPRBlocks:\s*(\d+)"),
        "sgprs_for_waves_per_eu": int_field(r";\s*NumSGPRsForWavesPerEU:\s*(\d+)"),
        "vgprs_for_waves_per_eu": int_field(r";\s*NumVGPRsForWavesPerEU:\s*(\d+)"),
        "occupancy_waves_per_eu": int_field(r";\s*Occupancy:\s*(\d+)"),
    }


def _kernel_resource_metrics(bench: dict, hcu_top: dict) -> dict:
    """Load static resource metrics from Triton metadata and AMDGCN comments."""
    manifest_path = hcu_top.get("artifact_manifest")
    manifest = {}
    if manifest_path and Path(manifest_path).is_file():
        try:
            manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            manifest = {}

    artifacts = manifest.get("artifacts") or {}
    metadata_path = _first_existing([
        p for p in artifacts.get("metadata", [])
        if not Path(p).name.startswith("__grp_")
    ] + artifacts.get("metadata", []))
    amdgcn_path = _first_existing(artifacts.get("amdgcn", []))

    metadata = {}
    if metadata_path:
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            metadata = {}

    amdgcn = _parse_amdgcn_resources(amdgcn_path)
    active_config = bench.get("active_config") or {}
    return {
        "triton_config": active_config,
        "triton_metadata_path": str(metadata_path) if metadata_path else "",
        "amdgcn_path": amdgcn.get("amdgcn_path", ""),
        "triton_num_warps": metadata.get("num_warps"),
        "triton_num_stages": metadata.get("num_stages"),
        "triton_waves_per_eu": metadata.get("waves_per_eu"),
        "triton_shared_bytes": metadata.get("shared"),
        "triton_profile_scratch_bytes": metadata.get("profile_scratch_size"),
        **amdgcn,
    }


def _compact_config(config: dict) -> str:
    if not config:
        return "n/a"
    order = ["BLOCK_M", "BLOCK_N", "BLOCK_K", "BLOCK_SIZE", "num_warps", "num_stages", "waves_per_eu"]
    parts = []
    for key in order:
        if key in config:
            short = {
                "BLOCK_M": "BM",
                "BLOCK_N": "BN",
                "BLOCK_K": "BK",
                "BLOCK_SIZE": "BS",
                "num_warps": "warps",
                "num_stages": "stages",
                "waves_per_eu": "waves/EU",
            }[key]
            parts.append(f"{short}={config[key]}")
    for key in sorted(k for k in config if k not in order):
        parts.append(f"{key}={config[key]}")
    return ", ".join(parts)


def _fmt_bytes_value(value) -> str:
    if value is None:
        return "n/a"
    try:
        return f"{int(value)} bytes"
    except (TypeError, ValueError):
        return str(value)


def _md_path_link(path: str) -> str:
    if not path or path == "n/a":
        return "n/a"
    label = Path(path).name or path
    return f"[{label}]({path})"


def _shape_label(state: dict, bench: dict | None = None) -> str:
    dims = state.get("dims") or (bench or {}).get("dims") or {}
    if not isinstance(dims, dict) or not dims:
        return "n/a"
    preferred = ["case", "N", "T", "H", "K", "BT", "BC", "headdim_k", "fixlen", "shape_family"]
    keys = [key for key in preferred if key in dims]
    keys.extend(sorted(key for key in dims if key not in keys))
    return ", ".join(f"{key}={dims[key]}" for key in keys)


def _final_ms_for_summary(state: dict, final_bench: dict) -> float | None:
    best_ms = state.get("best_metric_ms")
    if best_ms is not None:
        return best_ms
    kernel = final_bench.get("kernel") or {}
    return kernel.get("average_ms") or kernel.get("median_ms") or kernel.get("min_ms")


def _overview_table(
    state: dict,
    final_bench: dict,
    baseline_ms,
    best_ms,
    final_speedup,
    final_roofline: dict,
    active_config: dict,
) -> str:
    util = (
        f"compute `{_fmt_percent_plain(final_roofline.get('compute_util_pct'))}`, "
        f"memory `{_fmt_percent_plain(final_roofline.get('memory_util_pct'))}`"
    )
    rows = [
        "| shape | baseline | best | speedup | final config | xcu 利用率 |",
        "|-------|----------|------|---------|--------------|------------|",
        (
            f"| `{_shape_label(state, final_bench)}` "
            f"| `{_fmt_ms(baseline_ms)}` "
            f"| `{_fmt_ms(best_ms)}` "
            f"| **{_fmt_speedup(final_speedup)}** "
            f"| `{_compact_config(active_config)}` "
            f"| {util} |"
        ),
    ]
    return "\n".join(rows)


def _final_case_metrics_table(bench: dict, bench_path: str, roofline: dict, hcu_top: dict) -> str:
    kernel = bench.get("kernel") or {}
    derived = hcu_top.get("derived_metrics") or {}
    resources = _kernel_resource_metrics(bench, hcu_top)
    case_name = bench.get("case") or bench.get("config_key") or "final"
    path = bench.get("solution_file") or bench_path or "n/a"
    latency = _latency_us(kernel)
    logical_gbps = kernel.get("bandwidth_gbps_rough")
    hbm_gbps = roofline.get("hbm_bandwidth_gbs")
    l2_hit = roofline.get("l2_hit_rate_pct")
    compute_throughput = derived.get("compute_throughput_tops")
    compute_domain = _compute_domain_label(derived)
    compute_unit = _compute_unit_label(derived)
    hbm_header = "HBM GB/s"
    compute_util_header = f"compute util%<br>({compute_domain} {compute_unit} / peak)"
    memory_header = "memory util%"
    xcu_compute_header = f"xcu throughput<br>({compute_domain} {compute_unit})"
    lds_value = f"{_fmt_bytes_value(resources.get('lds_bytes'))} / {_fmt_bytes_value(resources.get('triton_shared_bytes'))}"
    rows = [
        f"| case | path | latency_us | rough TFLOPS | rough GB/s | {xcu_compute_header} | {compute_util_header} | {hbm_header} | {memory_header} | L2 Cache Hit% | Triton config | LDS size<br>(ISA / Triton shared, bytes) | occupancy<br>(ISA waves/EU) | SGPR<br>(per thread) | VGPR<br>(per thread) | scratch<br>(bytes) |",
        "|------|------|------------|--------------|------------|-------------|----------|----------|---------|---------------|---------------|----------|-----------|------|------|---------|",
        (
            f"| {case_name} "
            f"| {_md_path_link(path)} "
            f"| {_fmt_num(latency, '', 2)} "
            f"| n/a "
            f"| {_fmt_num(logical_gbps, '', 2)} "
            f"| {_fmt_num(compute_throughput, '', 2)} "
            f"| {_fmt_num(roofline.get('compute_util_pct'), '', 2)} "
            f"| {_fmt_num(hbm_gbps, '', 2)} "
            f"| {_fmt_num(roofline.get('memory_util_pct'), '', 2)} "
            f"| {_fmt_num(l2_hit, '', 2)} "
            f"| `{_compact_config(resources.get('triton_config') or {})}` "
            f"| {lds_value} "
            f"| {_fmt_num(resources.get('occupancy_waves_per_eu'), ' waves/EU', 0)} "
            f"| {_fmt_num(resources.get('num_sgprs'), ' SGPR/thread', 0)} "
            f"| {_fmt_num(resources.get('num_vgprs'), ' VGPR/thread', 0)} "
            f"| {_fmt_bytes_value(resources.get('scratch_bytes'))} |"
        ),
    ]
    return "\n".join(rows)


def _correctness_summary(bench: dict) -> str:
    correctness = bench.get("correctness") or {}
    if not correctness.get("checked"):
        return "not checked"
    status = "passed" if correctness.get("passed") is True else "failed" if correctness.get("passed") is False else "unknown"
    return (
        f"{status}, atol={correctness.get('atol', 'n/a')}, "
        f"rtol={correctness.get('rtol', 'n/a')}, outputs={correctness.get('output_tensor_count', 'n/a')}"
    )


def _toolchain_summary(env: dict) -> str:
    return (
        f"Triton `{env.get('libs', {}).get('triton', {}).get('version', '?')}`, "
        f"PyTorch `{env.get('libs', {}).get('torch', {}).get('version', '?')}`, "
        f"xcu `{_tool_status(env.get('xcu', {}) or {})}`, "
        f"hipprof `{_tool_status(env.get('hipprof', {}) or {})}`, "
        f"dccobjdump `{_tool_status(env.get('dccobjdump', {}) or {})}`"
    )


def _artifact_links(*paths: str | None) -> str:
    links = [_md_path_link(path) for path in paths if path]
    return "<br>".join(links) if links else "n/a"


def _final_kernel_snapshot_and_metrics_section(
    state: dict,
    run_dir: str,
    final_bench: dict,
    final_bench_path: str,
    final_roofline: dict,
    final_roofline_path: str,
    final_hcu_top: dict,
    final_hcu_top_path: str,
    active_config: dict,
    baseline_ms,
    best_ms,
    final_speedup,
) -> str:
    env = state.get("env", {}) or {}
    gpu = (env.get("gpus") or [{}])[0]
    kernel = final_bench.get("kernel") or {}
    resources = _kernel_resource_metrics(final_bench, final_hcu_top)
    derived = final_hcu_top.get("derived_metrics") or {}
    final_kernel = os.path.join(run_dir, "final_kernel.py")
    if not os.path.isfile(final_kernel):
        final_kernel = state.get("best_file") or final_bench.get("solution_file") or "n/a"
    source_kernel = state.get("best_file") or final_bench.get("solution_file") or "n/a"
    avg_ms = kernel.get("average_ms")
    median_ms = kernel.get("median_ms")
    min_ms = kernel.get("min_ms")
    timing_detail = (
        f"best `{_fmt_ms(best_ms)}`; "
        f"avg `{_fmt_ms(avg_ms)}`, median `{_fmt_ms(median_ms)}`, min `{_fmt_ms(min_ms)}`"
    )
    xcu_dispatch = final_hcu_top.get("selected_kernel") or "n/a"
    if final_hcu_top.get("dispatch_id") is not None:
        xcu_dispatch = f"{xcu_dispatch} (dispatch {final_hcu_top.get('dispatch_id')}, {_fmt_num(final_hcu_top.get('duration_us'), ' us')})"

    snapshot_rows = [
        "### 快照",
        "",
        "| 项目 | 值 |",
        "|------|----|",
        f"| Final kernel | {_md_path_link(final_kernel)} |",
        f"| Source kernel | {_md_path_link(source_kernel)} |",
        f"| Shape / dims | `{_shape_label(state, final_bench)}` |",
        f"| GPU / arch | `{gpu.get('name', '?')}`, `{gpu.get('gfx_arch') or gpu.get('gcn_arch') or '?'}`, {gpu.get('compute_units', '?')} CU, {_fmt_num(gpu.get('total_memory_mb'), ' MiB', 0)} |",
        f"| Toolchain | {_toolchain_summary(env)} |",
        f"| Active config | `{_compact_config(active_config)}` |",
        f"| Correctness | `{_correctness_summary(final_bench)}` |",
        f"| xcu kernel | `{xcu_dispatch}` |",
        f"| Artifacts | {_artifact_links(final_bench_path, final_hcu_top_path, final_roofline_path)} |",
    ]

    metric_rows = [
        "",
        "### 指标",
        "",
        "| baseline | best | speedup | final timing | logical GB/s | HBM GB/s | L2 hit | compute util | memory util | roofline |",
        "|----------|------|---------|--------------|--------------|----------|--------|--------------|-------------|----------|",
        (
            f"| `{_fmt_ms(baseline_ms)}` "
            f"| `{_fmt_ms(best_ms)}` "
            f"| **{_fmt_speedup(final_speedup)}** "
            f"| {timing_detail} "
            f"| {_fmt_num(kernel.get('bandwidth_gbps_rough'), ' GB/s')} "
            f"| {_fmt_num(final_roofline.get('hbm_bandwidth_gbs'), ' GB/s')} "
            f"| {_fmt_percent_plain(final_roofline.get('l2_hit_rate_pct'))} "
            f"| {_fmt_percent_plain(final_roofline.get('compute_util_pct'))} "
            f"| {_fmt_percent_plain(final_roofline.get('memory_util_pct'))} "
            f"| `{final_roofline.get('bound', 'n/a')}` |"
        ),
        "",
        "| xcu throughput | L2 bandwidth | VL1 coalescing | VL1 stalled on L2 data | global load/store eff | LDS conflict | occupancy | SGPR / VGPR | scratch |",
        "|----------------|--------------|----------------|------------------------|-----------------------|--------------|-----------|-------------|---------|",
        (
            f"| {_fmt_num(derived.get('compute_throughput_tops'), ' ' + _compute_unit_label(derived))} "
            f"| {_fmt_num(final_roofline.get('l2_bandwidth_gbs'), ' GB/s')} "
            f"| {_fmt_percent_plain(final_roofline.get('vl1_buffer_coalescing_pct'))} "
            f"| {_fmt_percent_plain(final_roofline.get('vl1_stalled_l2_data_pct'))} "
            f"| {_fmt_percent_plain(final_roofline.get('global_load_efficiency_pct'))} / {_fmt_percent_plain(final_roofline.get('global_store_efficiency_pct'))} "
            f"| {_fmt_num(final_roofline.get('lds_bank_conflict'), '')} "
            f"| {_fmt_num(resources.get('occupancy_waves_per_eu'), ' waves/EU', 0)} "
            f"| {_fmt_num(resources.get('num_sgprs'), '', 0)} / {_fmt_num(resources.get('num_vgprs'), '', 0)} "
            f"| {_fmt_bytes_value(resources.get('scratch_bytes'))} |"
        ),
    ]
    if final_roofline.get("notes"):
        metric_rows.extend([
            "",
            "> " + "; ".join(str(x) for x in final_roofline.get("notes", [])),
        ])
    return "\n".join(snapshot_rows + metric_rows)


def _resource_metrics_table(bench: dict, bench_path: str, hcu_top: dict) -> str:
    resources = _kernel_resource_metrics(bench, hcu_top)
    case_name = bench.get("case") or bench.get("config_key") or "final"
    path = bench.get("solution_file") or bench_path or "n/a"
    lds_value = f"{_fmt_bytes_value(resources.get('lds_bytes'))} / {_fmt_bytes_value(resources.get('triton_shared_bytes'))}"
    rows = [
        "| case | path | Triton config | LDS size (ISA / Triton shared, bytes) | occupancy (ISA waves/EU) | SGPR (per thread) | VGPR (per thread) | scratch (bytes) |",
        "|------|------|---------------|---------------------------------------|--------------------------|-------------------|-------------------|-----------------|",
        (
            f"| {case_name} "
            f"| `{path}` "
            f"| `{_compact_config(resources.get('triton_config') or {})}` "
            f"| {lds_value} "
            f"| {_fmt_num(resources.get('occupancy_waves_per_eu'), ' waves/EU', 0)} "
            f"| {_fmt_num(resources.get('num_sgprs'), ' SGPR/thread', 0)} "
            f"| {_fmt_num(resources.get('num_vgprs'), ' VGPR/thread', 0)} "
            f"| {_fmt_bytes_value(resources.get('scratch_bytes'))} |"
        ),
    ]
    return "\n".join(rows)


def _metric_provenance_section(final_bench: dict, bench_path: str, roofline: dict, hcu_top_path: str | None) -> str:
    profiler = roofline.get("profiler") or final_bench.get("profiler") or "n/a"
    hcu_top = {}
    derived = {}
    if hcu_top_path and Path(hcu_top_path).is_file():
        try:
            hcu_top = json.loads(Path(hcu_top_path).read_text(encoding="utf-8"))
            derived = hcu_top.get("derived_metrics") or {}
        except (OSError, json.JSONDecodeError):
            derived = {}
    resources = _kernel_resource_metrics(final_bench, hcu_top) if hcu_top else {}
    compute_source = derived.get("compute_util_source") or "n/a"
    compute_kind = derived.get("compute_util_kind") or "n/a"
    compute_throughput = derived.get("compute_throughput_tops")
    compute_throughput_source = derived.get("compute_throughput_source") or "n/a"
    compute_peak = derived.get("compute_peak_tops")
    compute_peak_source = derived.get("compute_peak_source") or "n/a"
    compute_unit = _compute_unit_label(derived)
    compute_throughput_pct = None
    try:
        if compute_peak and compute_throughput:
            compute_throughput_pct = float(compute_throughput) / float(compute_peak) * 100.0
    except (TypeError, ValueError):
        compute_throughput_pct = None
    memory_source = derived.get("memory_util_source") or "n/a"
    lines = [
        f"- **Timing**: kernel-only benchmark timing from `{bench_path or 'n/a'}`；默认不计 `ref.py` 耗时。",
        "- **logical GB/s**: benchmark 可见 tensor bytes / kernel time，仅表示逻辑带宽，不等价于硬件 HBM。",
        f"- **Hardware counters**: profiler=`{profiler}`；HBM/L2/utilization 来自 `hcu_top.json` / `roofline.json`，缺失即写 `n/a`。",
        f"- **compute util**: `{compute_source}`；throughput/peak=`{_fmt_num(compute_throughput, '', 2)} / {_fmt_num(compute_peak, '', 2)} {compute_unit}`，domain=`{compute_kind}`。",
        f"- **memory util**: `{memory_source}`；HBM bandwidth 使用 `L2_Fabric-Rd BW + L2_Fabric-Wr BW`。",
        f"- **static resources**: metadata `{resources.get('triton_metadata_path') or 'n/a'}`，AMDGCN `{resources.get('amdgcn_path') or 'n/a'}`，HCU metrics `{hcu_top_path or 'n/a'}`。",
    ]
    return "\n".join(lines)


def _config_sweep_section(state: dict, final_bench: dict, active_config: dict, attempt_rows: list[dict] | None = None) -> str:
    config_source = (
        final_bench.get("config_source")
        or final_bench.get("active_config_source")
        or state.get("config_source")
        or "n/a"
    )
    disable_autotune = final_bench.get("disable_autotune")
    lines = [
        f"- **Active config**: `{json.dumps(active_config, ensure_ascii=False) if active_config else 'n/a'}`",
        f"- **Config source**: `{config_source}`",
        f"- **disable_autotune recorded**: `{disable_autotune if disable_autotune is not None else 'n/a'}`",
    ]
    baseline_autotune = state.get("baseline_autotune")
    if isinstance(baseline_autotune, dict):
        selected = baseline_autotune.get("selected_config")
        lines.append(
            "- **Baseline autotune fairness**: "
            f"`{baseline_autotune.get('status', 'n/a')}`"
            + (f", selected=`{json.dumps(selected, ensure_ascii=False)}`" if selected else "")
        )
        if baseline_autotune.get("guidance"):
            lines.append(f"  - {baseline_autotune['guidance']}")
    tune_rows = [row for row in (attempt_rows or []) if row.get("kind") == "config_tune"]
    if tune_rows:
        lines.append("")
        lines.append("| Iter | 结果 | best ms | vs 前最佳 | 说明 |")
        lines.append("|------|------|---------|-----------|------|")
        for row in tune_rows:
            result = "成功" if row.get("status") == "success" else "失败"
            lines.append(
                f"| {row.get('iter', '-')} "
                f"| {result} "
                f"| {_fmt_ms(row.get('ms'))} "
                f"| {_fmt_pct(row.get('change_pct'))} "
                f"| {_md_cell(row.get('outcome') or row.get('candidate') or '-')} |"
            )
    elif state.get("tune_history") or state.get("accepted_configs") or state.get("final_tune"):
        lines.append("- **Config sweep evidence**: state 中记录了 tune/final_tune/accepted config 结果，但未找到可渲染的 `config_tune` timeline 事件；请检查 `iterv*/attempt_timeline.json`。")
    else:
        lines.append("- **Config sweep evidence**: 本 summary 未发现自动 tune/config sweep 记录；若本轮没有重跑 final tuning iteration，需要在 `## 回顾` 中写明跳过原因。")
    return "\n".join(lines)


def _attempt_summary(row: dict) -> str:
    parts = [f"iter {row.get('iter', '-')}", str(row.get("kind") or "attempt")]
    candidate = row.get("candidate")
    if candidate:
        parts.append(f"`{candidate}`")
    ms = _fmt_ms(row.get("ms"))
    if ms != "n/a":
        parts.append(ms)
    change = _fmt_pct(row.get("change_pct"))
    if change != "n/a":
        parts.append(f"vs 前最佳 {change}")
    outcome = row.get("outcome")
    if outcome:
        parts.append(str(outcome))
    return " / ".join(parts)


def _history_win_summary(entry: dict) -> str:
    methods = ", ".join(entry.get("method_names") or entry.get("methods") or ["promoted change"])
    return (
        f"iter {entry.get('iter', '-')} / {methods} / {_fmt_ms(entry.get('ms'))} / "
        f"vs 前最佳 {_fmt_speedup(entry.get('speedup_vs_best_before'))}"
    )


def _retrospective_section(
    state: dict,
    final_bench: dict,
    attempt_rows: list[dict],
    baseline_ms=None,
    final_roofline: dict | None = None,
) -> str:
    correctness = (final_bench.get("correctness") or {}).get("passed")
    correctness_text = "通过" if correctness is True else "未通过" if correctness is False else "n/a"
    best_ms = state.get("best_metric_ms")
    speedup = (float(baseline_ms) / float(best_ms)) if baseline_ms and best_ms else None
    final_roofline = final_roofline or {}

    lines = [
        "### 结果",
        "",
        f"- correctness `{correctness_text}`；baseline `{_fmt_ms(baseline_ms)}`，best `{_fmt_ms(best_ms)}`，总加速 **{_fmt_speedup(speedup)}**。",
    ]

    promoted = [
        row for row in attempt_rows
        if row.get("status") == "success"
    ]
    measured_wins = [
        row for row in promoted
        if (_safe_float(row.get("change_pct")) or 0.0) > 0.0
    ]
    history_wins = [
        entry for entry in state.get("history", [])
        if isinstance(entry, dict)
        and entry.get("status") == "improved"
        and (_safe_float(entry.get("speedup_vs_best_before")) or 0.0) > 1.0
    ]
    if history_wins:
        history_wins.sort(key=lambda entry: _safe_float(entry.get("iter")) or 0.0)
        lines.extend([
            "",
            "### 做了什么 / 收益",
            "",
            "- " + "\n- ".join(_history_win_summary(entry) for entry in history_wins),
        ])
    elif measured_wins:
        measured_wins.sort(key=lambda row: _safe_float(row.get("change_pct")) or 0.0, reverse=True)
        lines.extend([
            "",
            "### 做了什么 / 收益",
            "",
            "- " + "\n- ".join(_attempt_summary(row) for row in measured_wins[:4]),
        ])
    elif promoted:
        lines.extend([
            "",
            "### 做了什么 / 收益",
            "",
            "- " + "\n- ".join(_attempt_summary(row) for row in promoted[:4]),
        ])
    else:
        lines.extend([
            "",
            "### 做了什么 / 收益",
            "",
            "- timeline 中没有记录明确成功的优化尝试；若 best 有变化，请补齐 `semantic_rewrite` / `config_tune` / branch 事件。",
        ])

    failed = [row for row in attempt_rows if row.get("status") != "success"]
    lines.extend(["", "### 无效尝试 / 停止原因", ""])
    if failed:
        lines.append("- 未 promoted 的尝试：" + "; ".join(_attempt_summary(row) for row in failed[:4]) + "。")
    else:
        lines.append("- timeline 中没有失败事件。")

    final_tune = state.get("final_tune") if isinstance(state.get("final_tune"), dict) else {}
    if final_tune.get("completed"):
        promoted_text = final_tune.get("promoted")
        lines.append(f"- Final tuning 已执行；promoted=`{promoted_text if promoted_text is not None else 'n/a'}`，证据 `{final_tune.get('path') or 'n/a'}`。")
    elif final_tune:
        lines.append(f"- Final tuning 有记录但未完成；状态 `{final_tune.get('status') or final_tune.get('reason') or 'n/a'}`。")
    else:
        lines.append("- state 中未记录 final tuning；若本次确实跳过，需要在最终交付前写明原因。")

    lines.extend(["", "### 当前瓶颈", ""])
    if final_roofline:
        bound = final_roofline.get("bound", "n/a")
        reliable = final_roofline.get("utilization_reliable")
        lines.append(
            f"- Roofline 判定 `{bound}`；compute `{_fmt_percent_plain(final_roofline.get('compute_util_pct'))}`，"
            f"memory `{_fmt_percent_plain(final_roofline.get('memory_util_pct'))}`，L2 hit `{_fmt_percent_plain(final_roofline.get('l2_hit_rate_pct'))}`，"
            f"HBM `{_fmt_num(final_roofline.get('hbm_bandwidth_gbs'), ' GB/s')}`。"
        )
        if reliable is False:
            lines.append("- 利用率计数器标记为不可靠；只能把 timing 作为强证据。")
        if final_roofline.get("vl1_stalled_l2_data_pct") is not None:
            lines.append(
                f"- VL1 stalled on L2 data `{_fmt_percent_plain(final_roofline.get('vl1_stalled_l2_data_pct'))}`，"
                f"global load/store efficiency `{_fmt_percent_plain(final_roofline.get('global_load_efficiency_pct'))}` / `{_fmt_percent_plain(final_roofline.get('global_store_efficiency_pct'))}`。"
            )
    else:
        lines.append("- 没有最终 roofline 证据；瓶颈判断需回到 timing/profile 重新补证。")

    lines.extend(["", "### 下一步", ""])
    if state.get("frontier"):
        lines.append("- 先复查未探索分支/frontier，再决定是否扩大 config sweep 或回到 Formula-First 语义重写。")
    elif failed and not measured_wins:
        lines.append("- 回到 `## Formula-First Analysis`，优先确认是否存在未尝试的算法级重写，而不是继续扩大低层 config。")
    elif str(final_roofline.get("bound", "")).lower() == "compute":
        lines.append("- 优先围绕已验证的 dot/MMAC 路径做小范围 ablation：tile shape、work granularity、backend config 和寄存器/occupancy 取舍。")
    elif str(final_roofline.get("bound", "")).lower() in {"memory", "bandwidth"}:
        lines.append("- 优先检查 load/store 合并、K/G 复用、layout convert 与 L2/VL1 行为；扩大 config sweep 前先做一两个源级复用假设。")
    else:
        lines.append("- 若继续迭代，优先围绕已证明有效的 rewrite/config 做小范围 ablation，避免重新展开低收益搜索。")

    return "\n".join(lines)


def _xcu_highlight_lines(roofline: dict) -> list[str]:
    fields = [
        ("L2 bandwidth", "l2_bandwidth_gbs", " GB/s"),
        ("VL1 buffer coalescing", "vl1_buffer_coalescing_pct", "%"),
        ("VL1 stalled on L2 data", "vl1_stalled_l2_data_pct", "%"),
        ("Global load efficiency", "global_load_efficiency_pct", "%"),
        ("Global store efficiency", "global_store_efficiency_pct", "%"),
        ("LDS bank conflict", "lds_bank_conflict", ""),
    ]
    lines = []
    for label, key, suffix in fields:
        value = roofline.get(key)
        if value is not None:
            lines.append(f"- **{label}**: {_fmt_num(value, suffix)}")
    return lines


def _kernel_uses_tf32_dot(kernel_path: str | None) -> bool:
    if not kernel_path or not os.path.isfile(kernel_path):
        return False
    try:
        text = Path(kernel_path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return (
        'input_precision="tf32"' in text
        or "input_precision='tf32'" in text
        or 'input_precision = "tf32"' in text
        or "input_precision = 'tf32'" in text
    )


def _tf32_correctness_lines(bench: dict) -> list[str]:
    correctness = bench.get("correctness") or {}
    if not correctness.get("checked"):
        return [
            "- **Correctness vs ref.py**: not checked (no `--ref` in benchmark)",
        ]
    passed = correctness.get("passed")
    status = "passed" if passed is True else "failed" if passed is False else "unknown"
    lines = [
        f"- **Correctness vs ref.py**: **{status}**",
        f"- **atol / rtol**: `{correctness.get('atol', 'n/a')}` / `{correctness.get('rtol', 'n/a')}`",
    ]
    if passed is False:
        lines.append(
            "- **Promotion rule**: a TF32 branch that fails correctness must not be promoted; "
            "revert to full-precision f32 `tl.dot` or fix the kernel."
        )
    if bench.get("reference_timing_skipped"):
        lines.append(
            "- **Reference timing**: skipped (`benchmark.py` default; "
            "reported speedups are kernel vs baseline, not vs ref latency)"
        )
    if bench.get("ref_backend"):
        lines.append(f"- **ref.py backend**: `{bench['ref_backend']}` (valid when exposed through Python-callable `reference()`)")
    return lines


def _tf32_warning_section(kernel_path: str | None, bench: dict) -> list[str]:
    if not _kernel_uses_tf32_dot(kernel_path):
        return []
    lines = [
        "## TF32 精度提醒",
        "",
        "> **WARNING: 最终 champion 在 f32 矩阵乘路径上使用了 `tl.dot(..., input_precision=\"tf32\")`。**",
        "> TF32 会在 MMAC 内对操作数做 TF32 舍入，累加结果仍为 f32，**不保证与全精度 f32 点积逐元素一致**。",
        "> 部署到生产前请在你的业务精度预算下自行复验；如需全精度 f32 MMAC，请改回默认 `input_precision`。",
        "",
    ]
    lines.extend(_tf32_correctness_lines(bench))
    lines.append("")
    return lines


def render(state_path: str, out_path: str) -> None:
    state = _read(state_path)
    run_dir = state["run_dir"]

    baseline_bench_path = os.path.join(run_dir, "baseline", "bench.json")
    baseline_ms = None
    if os.path.isfile(baseline_bench_path):
        b = _read(baseline_bench_path)
        baseline_ms = (b.get("kernel") or {}).get("average_ms")

    attempt_events = _load_attempt_events(state, run_dir)
    method_lookup = _load_iter_method_lookup(run_dir)
    attempt_rows = _flatten_attempts(attempt_events, method_lookup)
    attempt_svg = _write_attempt_timeline_svg(attempt_rows, baseline_ms, out_path)

    env = state.get("env", {})
    kb_overall, kb_rows = _kb_status(run_dir)
    final_bench, final_bench_path = _final_bench(state, run_dir)
    final_roofline, final_roofline_path = _final_roofline(state, run_dir)
    final_hcu_top, final_hcu_top_path = _final_hcu_top(state, run_dir)
    best_ms = _final_ms_for_summary(state, final_bench)
    final_speedup = (baseline_ms / best_ms) if (baseline_ms and best_ms and best_ms > 0) else None
    xcu_info = env.get("xcu", {}) or {}
    active_config = _active_config(state, final_bench)

    lines = []

    # ===== 概要：开门见山 =====
    lines.append("# 优化总结")
    lines.append("")
    lines.append("## 概要")
    lines.append("")
    lines.append(_overview_table(state, final_bench, baseline_ms, best_ms, final_speedup, final_roofline, active_config))
    lines.append("")

    # 有效方法一句话总结
    effective = _effective_methods_for_summary(state)
    if effective:
        method_names = [m.get("name", m.get("id", "?")) for m in effective]
        lines.append(f"主要有效手段：{', '.join(method_names)}。")
    ineffective = state.get("ineffective_methods", [])
    if ineffective:
        inef_names = [m.get("name", m.get("id", "?")) for m in ineffective]
        lines.append(f"未带来收益的手段：{', '.join(inef_names)}。")

    # 硬件利用率一句话
    compute_util = final_roofline.get("compute_util_pct")
    memory_util = final_roofline.get("memory_util_pct")
    if compute_util is not None or memory_util is not None:
        lines.append(f"当前瓶颈：Roofline 判定 `{final_roofline.get('bound', 'n/a')}`，"
                     f"计算利用率 {_fmt_percent_plain(compute_util)}，内存利用率 {_fmt_percent_plain(memory_util)}。")
    lines.append("")

    # ===== TF32 警告 =====
    best_kernel_path = state.get("best_file")
    if not best_kernel_path or not os.path.isabs(best_kernel_path):
        candidate = os.path.join(run_dir, "final_kernel.py")
        if os.path.isfile(candidate):
            best_kernel_path = candidate
    tf32_lines = _tf32_warning_section(best_kernel_path, final_bench)
    if tf32_lines:
        lines.extend(tf32_lines)

    # 降级证据警告
    if kb_overall in {"degraded", "partial", "missing"}:
        lines.append("> **注意：本地 HCU RAG KB 不可用或不完整。**"
                     " 本轮优化有效，但 Hygon/Triton 架构/codegen/config 相关结论未经 KB 支撑，"
                     "需源码、Triton IR/cache 或 `dccobjdump` 单独验证。")
        lines.append("")

    if not xcu_info.get("available"):
        lines.append("> **注意：未检测到 `xcu`。** 硬件计数器数据可能不完整；请安装 XCompute 以获取可靠的 HBM/L2/利用率数据。")
        lines.append("")

    # ===== 最终 Kernel 快照与指标 =====
    lines.append("## 最终 Kernel 快照与指标")
    lines.append("")
    lines.append(_final_kernel_snapshot_and_metrics_section(
        state,
        run_dir,
        final_bench,
        final_bench_path,
        final_roofline,
        final_roofline_path,
        final_hcu_top,
        final_hcu_top_path,
        active_config,
        baseline_ms,
        best_ms,
        final_speedup,
    ))
    lines.append("")

    # ===== 算子计算逻辑 =====
    lines.append("## 算子计算逻辑")
    lines.append("")
    lines.append(_kernel_logic_section(state, run_dir))
    lines.append("")

    # ===== 尝试时间线（合并版）=====
    lines.append("## 尝试时间线")
    lines.append("")
    lines.append("每个点是一条实际测试过的分支或配置：绿色圆点表示成功，红叉表示失败；蓝线表示 best-so-far。纵轴是执行时间，越低越好。"
                 "同一轮的 config sweep 合并为一行，取最优 config 的耗时。")
    lines.append("")
    if attempt_svg:
        svg_name = os.path.basename(attempt_svg)
        lines.append(f"[打开交互式 SVG 尝试时间线]({svg_name})")
        lines.append("")
        lines.append(
            f'<object data="{svg_name}" type="image/svg+xml" width="100%" height="420">'
            f'尝试时间线 SVG: <a href="{svg_name}">{svg_name}</a>'
            f'</object>'
        )
        lines.append("")
        lines.append("_每个尝试点在 SVG 内都有 hover 信息；若当前 Markdown 预览器不显示 tooltip，请直接打开上面的 SVG 文件。_")
        lines.append("")
    lines.append(_attempt_timeline_table(attempt_rows))
    lines.append("")

    # ===== 迭代时间线 =====
    lines.append("## 迭代时间线")
    lines.append("")
    lines.append(_iteration_step_timeline_table(state, attempt_rows))
    lines.append("")

    # ===== Roofline 历史 =====
    lines.append("## Roofline 历史")
    lines.append("")
    lines.append(_roofline_table(state))
    if any(r.get("degraded") for r in state.get("roofline_history", [])):
        lines.append("")
        lines.append("_Roofline 分类降级：profiler 计数器不可用，显示的瓶颈是回退分类，非实测证明。_")
    lines.append("")

    # ===== 方法汇总（合并为一个大节）=====
    lines.append("## 方法汇总")
    lines.append("")
    if effective:
        lines.append("### 有效方法")
        lines.append("")
        lines.append(_method_bullets(effective))
        lines.append("")
    if ineffective:
        lines.append("### 无效方法")
        lines.append("")
        lines.append(_method_bullets(ineffective))
        lines.append("")
    impl_failed = state.get("implementation_failed_methods", [])
    if impl_failed:
        lines.append("### 实现失败方法")
        lines.append("")
        lines.append(_method_bullets(impl_failed))
        lines.append("")

    # ===== 配置搜索 =====
    lines.append("## 配置搜索")
    lines.append("")
    lines.append(_config_sweep_section(state, final_bench, active_config, attempt_rows))
    lines.append("")

    # ===== 指标来源 =====
    lines.append("## 指标来源")
    lines.append("")
    lines.append(_metric_provenance_section(final_bench, final_bench_path, final_roofline, final_hcu_top_path))
    lines.append("")

    # ===== 知识沉淀 =====
    lines.append("## 知识沉淀")
    lines.append("")
    lines.append("- **status**: `not_appended_by_summarize`")
    lines.append("- **reason**: `summarize.py` 不会自动修改 `references/triton_optimization_memory.md`；最终审查时应根据 promoted rewrite/config-sensitive pattern 的通用性、正确性和 timing 证据，把本节改成 `appended` 或 `not_appended` 并写明原因。")
    lines.append("")

    # ===== KB 证据 =====
    if kb_rows:
        lines.append("## KB 证据")
        lines.append("")
        lines.append(f"本地 KB 状态：`{kb_overall}`。只列需要关注的缺口；完整状态见各 `iterv*/kb_*` artifact。")
        lines.append("")
        shown = [row for row in kb_rows if row["status"] != "ok"][:8]
        if not shown:
            lines.append("- KB evidence complete.")
        else:
            lines.append("| Iter | 状态 | 文件 | 原因 |")
            lines.append("|------|------|------|------|")
        for row in shown:
            lines.append(
                f"| {row['iter']} | {row['status']} | `{row['path'] or '-'}` | {row['reason'] or '-'} |"
            )
        hidden = len([row for row in kb_rows if row["status"] != "ok"]) - len(shown)
        if hidden > 0:
            lines.append(f"| ... | ... | ... | 另有 {hidden} 条，见 run dir |")
        lines.append("")

    # ===== 未探索分支 =====
    if state.get("frontier"):
        lines.append("## 未探索分支")
        lines.append("")
        for fe in state["frontier"][:10]:
            lines.append(
                f"- iter {fe.get('iter')} branch {fe.get('branch_index')}: "
                f"{_fmt_ms(fe.get('ms'))} "
                f"(+{fe.get('delta_from_champion', '?')}ms from champion)"
            )
        lines.append("")

    # ===== 回顾 =====
    lines.append("## 回顾与下一步")
    lines.append("")
    lines.append(_retrospective_section(state, final_bench, attempt_rows, baseline_ms, final_roofline))
    lines.append("")

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(json.dumps({"summary": out_path}, indent=2))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--state", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    render(args.state, args.out)


if __name__ == "__main__":
    main()
