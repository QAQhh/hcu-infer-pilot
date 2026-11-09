#!/usr/bin/env python3
"""Emit a self-contained final Triton kernel with the champion config baked in."""

from __future__ import annotations

import argparse
import ast
import json
import os
from pathlib import Path


def _read(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: str | Path, payload: dict) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _best_history_entry(state: dict) -> dict:
    best = os.path.abspath(state.get("best_file", ""))
    for item in reversed(state.get("history", [])):
        if os.path.abspath(item.get("kernel_file", "")) == best and item.get("status") == "improved":
            return item
    return (state.get("history") or [{}])[-1]


def _load_final_config(state: dict, entry: dict) -> tuple[dict, str]:
    config = state.get("best_config")
    if isinstance(config, dict) and config:
        return dict(config), "state.best_config"

    config_path = state.get("best_config_path") or entry.get("config_path")
    if config_path and os.path.isfile(config_path):
        value = _read(config_path)
        if isinstance(value, dict):
            return dict(value.get("config", value)), config_path

    active = entry.get("active_config")
    if isinstance(active, dict) and active:
        return dict(active), "state.history.active_config"

    run_dir = Path(state["run_dir"])
    iter_id = entry.get("iter")
    if iter_id:
        bench_path = run_dir / f"iterv{iter_id}" / "bench.json"
        if bench_path.is_file():
            bench = _read(bench_path)
            active = bench.get("active_config")
            if isinstance(active, dict) and active:
                return dict(active), str(bench_path)

    return {}, "none"


def _replace_default_config(source: str, config: dict) -> tuple[str, bool]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source, False
    lines = source.splitlines()
    replacement = f"DEFAULT_CONFIG = {repr(config)}"
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == "DEFAULT_CONFIG" for target in node.targets):
            start = node.lineno - 1
            end = getattr(node, "end_lineno", node.lineno)
            lines[start:end] = [replacement]
            return "\n".join(lines) + ("\n" if source.endswith("\n") else ""), True
    return source.rstrip() + "\n\n" + replacement + "\n", False


def _line_offsets(source: str) -> list[int]:
    offsets = []
    total = 0
    for line in source.splitlines(keepends=True):
        offsets.append(total)
        total += len(line)
    return offsets


def _replace_run_kernel_defaults(source: str, config: dict) -> tuple[str, list[str]]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source, []
    func = next((node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "run_kernel"), None)
    if func is None:
        return source, []

    args = func.args.args
    defaults = func.args.defaults
    default_args = args[len(args) - len(defaults):]
    offsets = _line_offsets(source)
    replacements: list[tuple[int, int, str, str]] = []
    for arg, default in zip(default_args, defaults):
        if arg.arg not in config:
            continue
        if not hasattr(default, "lineno") or not hasattr(default, "end_lineno"):
            continue
        start = offsets[default.lineno - 1] + default.col_offset
        end = offsets[default.end_lineno - 1] + default.end_col_offset
        replacements.append((start, end, repr(config[arg.arg]), arg.arg))

    replaced_names: list[str] = []
    for start, end, value, name in sorted(replacements, reverse=True):
        source = source[:start] + value + source[end:]
        replaced_names.append(name)
    replaced_names.reverse()
    return source, replaced_names


def _kb_summary(run_dir: Path) -> dict:
    iterations = []
    for iter_dir in sorted(run_dir.glob("iterv*")):
        if not iter_dir.is_dir():
            continue
        evidence = iter_dir / "kb_evidence.json"
        unavailable = iter_dir / "kb_unavailable.json"
        warning = iter_dir / "kb_warning.txt"
        item = {
            "iter": iter_dir.name,
            "status": "missing",
            "evidence_file": None,
            "warning_file": str(warning) if warning.is_file() else None,
            "reason": "",
        }
        if evidence.is_file():
            item["status"] = "ok"
            item["evidence_file"] = str(evidence)
        elif unavailable.is_file():
            item["status"] = "unavailable"
            item["evidence_file"] = str(unavailable)
            try:
                item["reason"] = json.loads(unavailable.read_text(encoding="utf-8")).get("reason", "")
            except Exception:
                item["reason"] = ""
        iterations.append(item)

    if not iterations:
        status = "missing"
    elif any(item["status"] == "unavailable" for item in iterations):
        status = "degraded"
    elif any(item["status"] == "missing" for item in iterations):
        status = "partial"
    else:
        status = "ok"
    return {
        "status": status,
        "warning": (
            "LOCAL HCU RAG KB UNAVAILABLE OR INCOMPLETE; do not claim KB-backed "
            "Hygon/Triton architecture, codegen, config, or method-selection decisions."
        ) if status in {"degraded", "partial", "missing"} else "",
        "iterations": iterations,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--config-out", required=True)
    parser.add_argument("--manifest-out", required=True)
    args = parser.parse_args()

    state = _read(args.state)
    entry = _best_history_entry(state)
    config, config_source = _load_final_config(state, entry)
    best_file = state.get("best_file")
    if not best_file or not os.path.isfile(best_file):
        raise SystemExit(f"best_file not found: {best_file}")

    source = Path(best_file).read_text(encoding="utf-8")
    final_source, replaced = _replace_default_config(source, config)
    final_source, run_kernel_defaults = _replace_run_kernel_defaults(final_source, config)
    header = (
        "# Generated by kernel-triton-optimize finalize.\n"
        f"# Source: {os.path.abspath(best_file)}\n"
        f"# Config source: {config_source}\n"
    )
    Path(args.out).write_text(header + final_source, encoding="utf-8")
    _write_json(args.config_out, config)
    manifest = {
        "final_kernel": os.path.abspath(args.out),
        "source_kernel": os.path.abspath(best_file),
        "config": config,
        "config_source": config_source,
        "local_kb": _kb_summary(Path(state["run_dir"])),
        "default_config_replaced": replaced,
        "run_kernel_defaults_replaced": run_kernel_defaults,
        "best_metric_ms": state.get("best_metric_ms"),
        "best_config_path": state.get("best_config_path"),
        "history_entry": entry,
    }
    _write_json(args.manifest_out, manifest)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
