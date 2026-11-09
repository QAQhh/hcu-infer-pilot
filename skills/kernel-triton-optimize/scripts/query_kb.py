#!/usr/bin/env python3
"""Collect local HCU RAG KB evidence for a Hygon Triton optimization run."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path


def _run(cmd: list[str], timeout: int) -> dict:
    started = dt.datetime.now().isoformat(timespec="seconds")
    try:
        proc = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return {
            "cmd": cmd,
            "started_at": started,
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
    except Exception as exc:  # noqa: BLE001 - evidence collection must not hide failures.
        return {
            "cmd": cmd,
            "started_at": started,
            "returncode": None,
            "stdout": "",
            "stderr": f"{type(exc).__name__}: {exc}",
        }


def _split_env_command(value: str) -> list[str]:
    return shlex.split(value, posix=(os.name != "nt"))


def _resolve_command(env_var: str, entrypoint: str, module: str) -> list[str] | None:
    env_value = os.environ.get(env_var)
    if env_value:
        return _split_env_command(env_value)

    exe = shutil.which(entrypoint)
    if exe:
        return [exe]

    try:
        module_spec = importlib.util.find_spec(module)
    except ModuleNotFoundError:
        module_spec = None
    if module_spec:
        return [sys.executable, "-m", module]

    return None


def _default_queries(args: argparse.Namespace) -> tuple[list[str], list[tuple[str, str]]]:
    arch = args.target_arch or "gfx938"
    op_kind = args.op_kind or "Triton kernel"
    context = " ".join(part for part in [args.context, f"dims={args.dims}" if args.dims else ""] if part).strip()

    query_topics = [
        f"hygon-extend Triton {arch} num_warps num_stages program geometry",
        f"hygon-extend Triton {arch} tl.dot tl.matrix_load MMAC MLS",
        f"hygon-extend Triton {arch} {op_kind} config tuning",
    ]
    optimize_topics = [
        (f"Triton {op_kind} kernel", context or f"Hygon HCU {arch} config tuning and codegen evidence"),
    ]
    return query_topics, optimize_topics


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)


def _first_lines(text: str, limit: int = 40) -> str:
    lines = text.strip().splitlines()
    if len(lines) > limit:
        return "\n".join(lines[:limit] + [f"... ({len(lines) - limit} more lines)"])
    return "\n".join(lines)


def _write_markdown(path: Path, payload: dict) -> None:
    lines = [
        "# KB Evidence",
        "",
        f"- **Status**: {payload.get('status')}",
        f"- **Created at**: {payload.get('created_at')}",
        f"- **Target arch**: {payload.get('target_arch') or 'unknown'}",
        f"- **Op kind**: {payload.get('op_kind') or 'unknown'}",
        f"- **Context**: {payload.get('context') or 'n/a'}",
        "",
        "## Commands",
        "",
    ]
    for idx, item in enumerate(payload.get("commands", []), start=1):
        lines.extend([
            f"### Command {idx}",
            "",
            "```bash",
            " ".join(shlex.quote(str(part)) for part in item.get("cmd", [])),
            "```",
            "",
            f"- returncode: `{item.get('returncode')}`",
            "",
        ])
        stdout = _first_lines(item.get("stdout", ""))
        stderr = _first_lines(item.get("stderr", ""))
        if stdout:
            lines.extend(["**stdout excerpt**", "", "```text", stdout, "```", ""])
        if stderr:
            lines.extend(["**stderr excerpt**", "", "```text", stderr, "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def _warning_text(payload: dict) -> str:
    reason = payload.get("reason") or "Local HCU KB query did not produce usable evidence."
    return "\n".join([
        "============================================================",
        "WARNING: LOCAL HCU RAG KB UNAVAILABLE",
        "============================================================",
        str(reason),
        "",
        "This optimization run is allowed to continue, but the iteration",
        "is KB-degraded. Do not claim that Hygon/Triton architecture,",
        "codegen, config, or method-selection decisions are KB-backed.",
        "Use benchmark, profiling, Triton cache/IR, source inspection,",
        "and dccobjdump evidence instead.",
        "============================================================",
        "",
    ])


def _write_warning(path: Path, payload: dict) -> None:
    path.write_text(_warning_text(payload), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local hcu-rag-kb evidence queries for Hygon Triton optimization.")
    parser.add_argument("--out-dir", required=True, help="Run or iteration directory where evidence files are written.")
    parser.add_argument("--iter", type=int, default=None, help="Optional iteration number for metadata only.")
    parser.add_argument("--op-kind", default=None, help="Workload kind, e.g. matmul, attention, memory, elementwise.")
    parser.add_argument("--target-arch", default=None, help="Target gfx arch, e.g. gfx936 or gfx938.")
    parser.add_argument("--context", default="", help="Extra bottleneck/kernel context.")
    parser.add_argument("--dims", default="", help="Shape JSON or shape summary.")
    parser.add_argument("--query", action="append", default=[], help="Additional hcu-rag-kb-query topic.")
    parser.add_argument("--optimize", action="append", default=[], help="Additional hcu-rag-kb-optimize code_type.")
    parser.add_argument("--timeout", type=int, default=180, help="Per-command timeout seconds.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero if KB query is unavailable or all queries fail.")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    query_cmd = _resolve_command("HCU_RAG_KB_QUERY", "hcu-rag-kb-query", "hcu_rag_kb_mcp.query_cli")
    optimize_cmd = _resolve_command("HCU_RAG_KB_OPTIMIZE", "hcu-rag-kb-optimize", "hcu_rag_kb_mcp.optimize_cli")

    payload = {
        "status": "unknown",
        "created_at": dt.datetime.now().isoformat(timespec="seconds"),
        "iteration": args.iter,
        "target_arch": args.target_arch,
        "op_kind": args.op_kind,
        "context": args.context,
        "dims": args.dims,
        "query_cmd": query_cmd,
        "optimize_cmd": optimize_cmd,
        "commands": [],
    }

    if not query_cmd and not optimize_cmd:
        payload["status"] = "unavailable"
        payload["reason"] = (
            "Neither hcu-rag-kb-query/hcu-rag-kb-optimize nor the "
            "hcu_rag_kb_mcp query/optimize Python modules are available locally."
        )
        _write_json(out_dir / "kb_unavailable.json", payload)
        _write_warning(out_dir / "kb_warning.txt", payload)
        print(_warning_text(payload))
        if args.strict:
            sys.exit(2)
        return

    query_topics, optimize_topics = _default_queries(args)
    query_topics.extend(args.query)
    optimize_topics.extend((topic, args.context) for topic in args.optimize)

    if query_cmd:
        payload["commands"].append(_run(query_cmd + ["--show-paths"], args.timeout))
        for topic in query_topics:
            payload["commands"].append(_run(query_cmd + [topic], args.timeout))

    if optimize_cmd:
        for code_type, context in optimize_topics:
            cmd = optimize_cmd + [code_type]
            if args.target_arch:
                cmd.extend(["--gpu-model", args.target_arch])
            if context:
                cmd.extend(["--context", context])
            payload["commands"].append(_run(cmd, args.timeout))

    successes = [item for item in payload["commands"] if item.get("returncode") == 0 and item.get("stdout")]
    payload["status"] = "ok" if successes else "failed"

    if payload["status"] == "ok":
        _write_json(out_dir / "kb_evidence.json", payload)
        _write_markdown(out_dir / "kb_evidence.md", payload)
        return

    payload["reason"] = "Local HCU KB commands were found, but all evidence queries failed or returned no output."
    _write_json(out_dir / "kb_unavailable.json", payload)
    _write_warning(out_dir / "kb_warning.txt", payload)
    print(_warning_text(payload))
    if args.strict:
        sys.exit(3)


if __name__ == "__main__":
    main()
