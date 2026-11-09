#!/usr/bin/env python3
"""Rebuild HCU RAG indexes after learned-experience review.

This wrapper is intentionally conservative. It verifies that learned experience
cards are reviewed, refuses to index pending cards by default, and defaults to a
dry-run. Use --execute when the review report is acceptable.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
TOOLS_DIR = SCRIPT_DIR.parents[2] / "tools"
if TOOLS_DIR.is_dir() and str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
try:
    from repo_paths import (
        default_embedding_model,
        default_experience_inbox,
        default_kb_path,
        default_rag_index_path,
        repo_root_from,
    )
except ImportError:
    default_embedding_model = None
    default_experience_inbox = None
    default_kb_path = None
    default_rag_index_path = None
    repo_root_from = None

DEFAULT_REPO_ROOT = repo_root_from(SCRIPT_DIR) if repo_root_from else SCRIPT_DIR.parents[3]
DEFAULT_KB_PATH = default_kb_path(DEFAULT_REPO_ROOT) if default_kb_path else DEFAULT_REPO_ROOT / "knowledge-base"
DEFAULT_INDEX_PATH = default_rag_index_path(DEFAULT_REPO_ROOT) if default_rag_index_path else DEFAULT_REPO_ROOT / "indexes" / "hcu-rag-kb-index"
DEFAULT_REVIEW_REPORT = Path("experience_review_report.json")
DEFAULT_INBOX = default_experience_inbox(DEFAULT_REPO_ROOT) if default_experience_inbox else DEFAULT_KB_PATH / "learned-experiences"
DEFAULT_EMBEDDING_MODEL = default_embedding_model(DEFAULT_REPO_ROOT) if default_embedding_model else DEFAULT_REPO_ROOT / "models" / "bge-large-en-v1.5"

APPROVED_STATUSES = {"approved", "review_approved"}


def _utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _read_json(path: str | Path) -> dict[str, Any]:
    p = Path(path).expanduser()
    if not p.is_file():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _write_json(path: str | Path, payload: dict[str, Any]) -> None:
    p = Path(path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _cmd_text(cmd: list[str | Path]) -> str:
    import shlex

    return " ".join(shlex.quote(str(item)) for item in cmd)


def _parse_frontmatter(content: str) -> dict[str, str]:
    if not content.startswith("---"):
        return {}
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip("\"'")
    return meta


def _scan_experience_cards(inbox: Path) -> list[dict[str, Any]]:
    if not inbox.exists():
        return []
    cards: list[dict[str, Any]] = []
    for path in sorted(inbox.rglob("*.md")):
        try:
            meta = _parse_frontmatter(path.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
        if meta.get("type") != "learned-kernel-experience":
            continue
        status = str(meta.get("status") or "review_required").strip().lower()
        cards.append(
            {
                "id": meta.get("id") or path.stem,
                "path": str(path),
                "status": status,
                "index_eligible": status in APPROVED_STATUSES,
            }
        )
    return cards


def _review_cards(report: dict[str, Any], inbox: Path) -> list[dict[str, Any]]:
    cards = report.get("cards")
    if isinstance(cards, list):
        return [item for item in cards if isinstance(item, dict)]
    return _scan_experience_cards(inbox)


def _backup_index(index_path: Path, backup_root: Path, *, dry_run: bool) -> str:
    if not index_path.exists() or not any(index_path.iterdir() if index_path.is_dir() else []):
        return ""
    backup_root.mkdir(parents=True, exist_ok=True)
    backup_path = backup_root / f"{index_path.name}.{_utc_stamp()}"
    if dry_run:
        return str(backup_path)
    if index_path.is_dir():
        shutil.copytree(index_path, backup_path)
    else:
        shutil.copy2(index_path, backup_path)
    return str(backup_path)


def _run_build(
    *,
    repo_root: Path,
    kb_path: Path,
    index_path: Path,
    mode: str,
    embedding_model: str,
    device: str,
    env: dict[str, str],
    logs_dir: Path,
    dry_run: bool,
) -> dict[str, Any]:
    builder = shutil.which("hcu-rag-kb-build-index")
    if builder:
        cmd: list[str | Path] = [builder]
    else:
        src_root = repo_root / "hcu-rag-kb-mcp" / "src"
        env["PYTHONPATH"] = str(src_root) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
        cmd = [sys.executable, "-m", "hcu_rag_kb_mcp.index_builder"]
    cmd.extend(
        [
            "--kb-path",
            kb_path,
            "--output-path",
            index_path,
            "--force",
            "--device",
            device,
        ]
    )
    if mode == "bm25":
        cmd.append("--bm25-only")
    elif mode == "full":
        cmd.extend(["--model", embedding_model])
    else:
        raise ValueError(f"unsupported rebuild mode: {mode}")
    step: dict[str, Any] = {"cmd": [str(item) for item in cmd], "cmd_text": _cmd_text(cmd)}
    if dry_run:
        step.update({"status": "planned", "returncode": 0})
        return step
    logs_dir.mkdir(parents=True, exist_ok=True)
    stdout_path = logs_dir / "rag_index_rebuild.stdout.txt"
    stderr_path = logs_dir / "rag_index_rebuild.stderr.txt"
    proc = subprocess.run(
        cmd,
        cwd=str(repo_root),
        env=env,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="ignore",
    )
    stdout_path.write_text(proc.stdout or "", encoding="utf-8")
    stderr_path.write_text(proc.stderr or "", encoding="utf-8")
    step.update(
        {
            "status": "ok" if proc.returncode == 0 else "failed",
            "returncode": proc.returncode,
            "stdout": str(stdout_path),
            "stderr": str(stderr_path),
        }
    )
    return step


def _markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# RAG Index Rebuild After Review",
        "",
        f"- status: `{report.get('status', '')}`",
        f"- mode: `{report.get('mode', '')}`",
        f"- knowledge_base: `{report.get('knowledge_base', '')}`",
        f"- index_path: `{report.get('index_path', '')}`",
        f"- approved cards: `{report.get('approved_cards', 0)}`",
        f"- pending cards: `{report.get('pending_cards', 0)}`",
        f"- backup: `{report.get('backup_path', '')}`",
        "",
        "## Command",
        "",
        f"`{(report.get('rebuild_step') or {}).get('cmd_text', '')}`",
    ]
    failures = report.get("hard_gate_failures", []) or []
    if failures:
        lines.extend(["", "## Hard Gate Failures", ""])
        for item in failures:
            lines.append(f"- {item.get('gate', '')}: {item.get('message', '')}")
    warnings = report.get("soft_gate_warnings", []) or []
    if warnings:
        lines.extend(["", "## Warnings", ""])
        for item in warnings:
            lines.append(f"- {item.get('gate', '')}: {item.get('message', '')}")
    return "\n".join(lines).rstrip() + "\n"


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    repo_root = Path(args.repo_root).expanduser().resolve()
    kb_path = Path(args.kb_path).expanduser().resolve()
    index_path = Path(args.index_path).expanduser().resolve()
    inbox = Path(args.inbox).expanduser().resolve()
    review_report_path = Path(args.review_report).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    logs_dir = output_dir / "logs"
    report_path = output_dir / "rag_index_rebuild_report.json"
    report_md = output_dir / "rag_index_rebuild_report.md"
    hard_failures: list[dict[str, str]] = []
    soft_warnings: list[dict[str, str]] = []

    review_report = _read_json(review_report_path)
    cards = _review_cards(review_report, inbox)
    approved = [card for card in cards if str(card.get("status", "")).lower() in APPROVED_STATUSES or card.get("index_eligible")]
    pending = [
        card
        for card in cards
        if str(card.get("status", "")).lower() not in APPROVED_STATUSES
        and str(card.get("status", "")).lower() not in {"rejected", "review_rejected"}
    ]
    if not kb_path.is_dir():
        hard_failures.append({"gate": "knowledge_base_path", "message": f"knowledge base not found: {kb_path}"})
    if not review_report and not args.allow_missing_review_report:
        hard_failures.append(
            {
                "gate": "review_report",
                "message": f"review report not found or unreadable: {review_report_path}",
            }
        )
    if pending and not args.allow_pending:
        hard_failures.append(
            {
                "gate": "pending_review_cards",
                "message": f"{len(pending)} learned experience card(s) are pending review; use --allow-pending only for dry audit rebuilds.",
            }
        )
    if not approved:
        soft_warnings.append(
            {
                "gate": "no_approved_experiences",
                "message": "No approved learned-experience cards were found. Rebuild is still valid for other KB changes.",
            }
        )
    dry_run = args.dry_run or not args.execute
    env = os.environ.copy()
    env["HCU_RAG_MCP_REPO_ROOT"] = str(repo_root)
    env["HCU_RAG_MCP_KB_PATH"] = str(kb_path)
    env["HCU_RAG_MCP_INDEX_PATH"] = str(index_path)
    if args.embedding_model:
        env["HCU_RAG_MCP_EMBEDDING_MODEL"] = str(Path(args.embedding_model).expanduser())
    backup_path = _backup_index(index_path, Path(args.backup_dir).expanduser().resolve(), dry_run=dry_run)
    rebuild_step: dict[str, Any]
    if hard_failures:
        rebuild_step = {"status": "blocked", "cmd": [], "cmd_text": ""}
    else:
        rebuild_step = _run_build(
            repo_root=repo_root,
            kb_path=kb_path,
            index_path=index_path,
            mode=args.mode,
            embedding_model=args.embedding_model,
            device=args.device,
            env=env,
            logs_dir=logs_dir,
            dry_run=dry_run,
        )
        if rebuild_step.get("status") == "failed":
            hard_failures.append({"gate": "index_rebuild", "message": "hcu-rag-kb-build-index failed"})
    status = "blocked" if hard_failures else ("planned" if dry_run else "completed")
    report: dict[str, Any] = {
        "schema_version": 1,
        "status": status,
        "mode": args.mode,
        "dry_run": dry_run,
        "knowledge_base": str(kb_path),
        "index_path": str(index_path),
        "review_report": str(review_report_path),
        "inbox": str(inbox),
        "approved_cards": len(approved),
        "pending_cards": len(pending),
        "backup_path": backup_path,
        "rebuild_step": rebuild_step,
        "artifacts": {
            "rebuild_report_json": str(report_path),
            "rebuild_report_md": str(report_md),
            "stdout": rebuild_step.get("stdout", ""),
            "stderr": rebuild_step.get("stderr", ""),
        },
        "hard_gate_failures": hard_failures,
        "soft_gate_warnings": soft_warnings,
        "policy": {
            "default_mode": "dry_run",
            "bm25_default": True,
            "full_rebuild_requires_explicit_mode": True,
            "unreviewed_experience_cards": "blocked unless --allow-pending",
        },
    }
    _write_json(report_path, report)
    report_md.parent.mkdir(parents=True, exist_ok=True)
    report_md.write_text(_markdown_report(report), encoding="utf-8")
    return report, 2 if hard_failures else int(rebuild_step.get("returncode", 0) or 0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Safely rebuild HCU RAG index after learned-experience review")
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT))
    parser.add_argument("--kb-path", default=str(DEFAULT_KB_PATH))
    parser.add_argument("--index-path", default=str(DEFAULT_INDEX_PATH))
    parser.add_argument("--inbox", default=str(DEFAULT_INBOX))
    parser.add_argument("--review-report", default=str(DEFAULT_REVIEW_REPORT))
    parser.add_argument("--output-dir", default="rag_index_rebuild_after_review")
    parser.add_argument("--backup-dir", default=str(DEFAULT_REPO_ROOT / "indexes" / "backups"))
    parser.add_argument("--mode", choices=["bm25", "full"], default="bm25")
    parser.add_argument("--embedding-model", default=str(DEFAULT_EMBEDDING_MODEL))
    parser.add_argument("--device", choices=["auto", "cuda", "cpu"], default="auto")
    parser.add_argument("--execute", action="store_true", help="Actually run the rebuild. Default is dry-run.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--allow-pending", action="store_true")
    parser.add_argument("--allow-missing-review-report", action="store_true")
    args = parser.parse_args()
    report, code = run(args)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
