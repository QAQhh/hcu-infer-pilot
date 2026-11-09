#!/usr/bin/env python3
"""Review learned kernel-experience cards before they enter stable retrieval.

The default mode is conservative: scan and report only. Promotion requires an
explicit --approve target or a card that was already manually marked
review_approved. This keeps generated optimizer lessons out of the stable RAG
path until semantic and benchmark contracts have been reviewed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TOOLS_DIR = SCRIPT_DIR.parents[2] / "tools"
if TOOLS_DIR.is_dir() and str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
try:
    from repo_paths import default_experience_inbox, repo_root_from
except ImportError:
    default_experience_inbox = None
    repo_root_from = None
REPO_ROOT = repo_root_from(SCRIPT_DIR) if repo_root_from else SKILL_DIR.parent.parent
DEFAULT_INBOX = default_experience_inbox(REPO_ROOT) if default_experience_inbox else SKILL_DIR / "knowledge-base" / "learned-experiences"
DEFAULT_APPROVED_CATALOG = SKILL_DIR / "references" / "learned_kernel_experiences.approved.jsonl"

APPROVED_STATUSES = {"approved", "review_approved"}
REJECTED_STATUSES = {"rejected", "review_rejected"}
PENDING_STATUSES = {"", "review_required", "pending_review"}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_name(value: str) -> str:
    text = re.sub(r"[^0-9A-Za-z_.-]+", "-", str(value).strip().lower()).strip("-")
    return text or "kernel-experience"


def _parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---"):
        return {}, content
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, content
    end_idx = -1
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx < 0:
        return {}, content
    meta: dict[str, str] = {}
    for line in lines[1:end_idx]:
        raw = line.strip()
        if not raw or raw.startswith("#") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        text = value.strip()
        if len(text) >= 2 and ((text[0] == text[-1] == '"') or (text[0] == text[-1] == "'")):
            text = text[1:-1]
        meta[key.strip()] = text
    return meta, "".join(lines[end_idx + 1 :])


def _format_scalar(value: Any) -> str:
    text = str(value)
    if not text:
        return '""'
    if any(ch in text for ch in [":", "#", "[", "]", "{", "}", ","]) or text.strip() != text:
        return json.dumps(text, ensure_ascii=False)
    return text


def _frontmatter_text(meta: dict[str, Any]) -> str:
    preferred = [
        "title",
        "type",
        "id",
        "kernel_family",
        "status",
        "created_at",
        "reviewed_at",
        "reviewer",
        "review_notes",
    ]
    keys = [key for key in preferred if key in meta]
    keys.extend(sorted(key for key in meta if key not in keys))
    lines = ["---"]
    for key in keys:
        lines.append(f"{key}: {_format_scalar(meta[key])}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def _replace_frontmatter(content: str, meta: dict[str, Any]) -> str:
    _old, body = _parse_frontmatter(content)
    return _frontmatter_text(meta) + body.lstrip("\n")


def _read_card(path: Path) -> dict[str, Any]:
    content = path.read_text(encoding="utf-8", errors="ignore")
    meta, body = _parse_frontmatter(content)
    card_id = str(meta.get("id") or path.stem)
    status = str(meta.get("status") or "").strip().lower()
    card_type = str(meta.get("type") or "").strip()
    family = str(meta.get("kernel_family") or "").strip()
    issues: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    if card_type != "learned-kernel-experience":
        issues.append({"gate": "card_type", "message": "frontmatter type must be learned-kernel-experience"})
    if not family:
        issues.append({"gate": "kernel_family", "message": "kernel_family is missing"})
    if status in PENDING_STATUSES:
        warnings.append({"gate": "review_status", "message": "card still requires review"})
    elif status in APPROVED_STATUSES:
        pass
    elif status in REJECTED_STATUSES:
        warnings.append({"gate": "review_status", "message": "card is rejected and will not be indexed"})
    else:
        issues.append({"gate": "review_status", "message": f"unsupported status: {status}"})
    required_terms = [
        ("result_section", "## Result"),
        ("validation_gates", "Required Validation Gates"),
        ("policy_section", "## Policy"),
        ("semantic_contract", "semantic"),
        ("benchmark_contract", "benchmark"),
    ]
    lowered = body.lower()
    for gate, term in required_terms:
        if term.lower() not in lowered:
            warnings.append({"gate": gate, "message": f"card body does not mention {term!r}"})
    return {
        "id": card_id,
        "path": str(path),
        "filename": path.name,
        "status": status or "review_required",
        "type": card_type,
        "kernel_family": family,
        "created_at": meta.get("created_at", ""),
        "reviewed_at": meta.get("reviewed_at", ""),
        "reviewer": meta.get("reviewer", ""),
        "issues": issues,
        "warnings": warnings,
        "index_eligible": card_type == "learned-kernel-experience" and status in APPROVED_STATUSES and not issues,
        "reviewable": card_type == "learned-kernel-experience" and status in PENDING_STATUSES and not issues,
        "_meta": meta,
        "_content": content,
    }


def _scan_cards(inbox: Path) -> list[dict[str, Any]]:
    if not inbox.exists():
        return []
    cards: list[dict[str, Any]] = []
    for path in sorted(inbox.rglob("*.md")):
        if path.name in {"README.md", "INDEX.md", "CONTRIBUTING.md"}:
            continue
        try:
            card = _read_card(path)
        except OSError as exc:
            cards.append(
                {
                    "id": path.stem,
                    "path": str(path),
                    "filename": path.name,
                    "status": "read_failed",
                    "type": "",
                    "kernel_family": "",
                    "issues": [{"gate": "read_card", "message": str(exc)}],
                    "warnings": [],
                    "index_eligible": False,
                    "reviewable": False,
                    "_meta": {},
                    "_content": "",
                }
            )
            continue
        if card["type"] == "learned-kernel-experience" or "learned-experience" in str(path.parent):
            cards.append(card)
    return cards


def _match_targets(cards: list[dict[str, Any]], targets: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
    matched: list[dict[str, Any]] = []
    missing: list[str] = []
    for target in targets:
        text = str(target).strip()
        if not text:
            continue
        path = Path(text).expanduser()
        found: dict[str, Any] | None = None
        for card in cards:
            card_path = Path(str(card["path"]))
            if (
                text == card["id"]
                or text == card["filename"]
                or path == card_path
                or path.name == card["filename"]
            ):
                found = card
                break
        if found is None:
            missing.append(text)
        elif found not in matched:
            matched.append(found)
    return matched, missing


def _write_card_status(
    card: dict[str, Any],
    *,
    status: str,
    reviewer: str,
    notes: str,
    dry_run: bool,
) -> dict[str, Any]:
    meta = dict(card.get("_meta") or {})
    meta["id"] = str(meta.get("id") or card["id"])
    meta["status"] = status
    meta["reviewed_at"] = _utc_now()
    if reviewer:
        meta["reviewer"] = reviewer
    if notes:
        meta["review_notes"] = notes
    if not dry_run:
        path = Path(str(card["path"]))
        path.write_text(_replace_frontmatter(str(card.get("_content") or ""), meta), encoding="utf-8")
    updated = dict(card)
    updated["status"] = status
    updated["reviewed_at"] = meta["reviewed_at"]
    updated["reviewer"] = meta.get("reviewer", "")
    updated["_meta"] = meta
    updated["index_eligible"] = status in APPROVED_STATUSES and not card.get("issues")
    updated["reviewable"] = False
    updated["warnings"] = [
        warning
        for warning in card.get("warnings", []) or []
        if warning.get("gate") != "review_status"
    ]
    return updated


def _catalog_row(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": card["id"],
        "status": card["status"],
        "kernel_family": card.get("kernel_family", ""),
        "source_card": card["path"],
        "reviewed_at": card.get("reviewed_at", ""),
        "reviewer": card.get("reviewer", ""),
        "type": "learned-kernel-experience",
    }


def _sync_approved_catalog(cards: list[dict[str, Any]], catalog: Path, *, dry_run: bool) -> int:
    approved = [card for card in cards if card.get("index_eligible")]
    if dry_run:
        return len(approved)
    catalog.parent.mkdir(parents=True, exist_ok=True)
    catalog.write_text(
        "".join(json.dumps(_catalog_row(card), ensure_ascii=False, sort_keys=True) + "\n" for card in approved),
        encoding="utf-8",
    )
    return len(approved)


def _counts(cards: list[dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for card in cards:
        key = str(card.get("status") or "unknown")
        out[key] = out.get(key, 0) + 1
    return out


def _write_markdown_report(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Learned Kernel Experience Review",
        "",
        f"- status: `{report.get('status', '')}`",
        f"- inbox: `{report.get('inbox', '')}`",
        f"- total cards: `{report.get('cards_total', 0)}`",
        f"- approved for index: `{report.get('approved_for_index_count', 0)}`",
        f"- pending review: `{report.get('pending_review_count', 0)}`",
        f"- approved catalog: `{report.get('artifacts', {}).get('approved_catalog', '')}`",
        "",
        "## Counts",
        "",
    ]
    for key, value in sorted((report.get("counts_by_status") or {}).items()):
        lines.append(f"- {key}: `{value}`")
    actions = report.get("actions", {}) or {}
    if actions:
        lines.extend(["", "## Actions", ""])
        for key, values in actions.items():
            lines.append(f"- {key}: `{', '.join(str(item) for item in values) or '-'}`")
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
    lines.extend(["", "## Cards", ""])
    for card in report.get("cards", []) or []:
        lines.append(
            f"- `{card.get('id', '')}` status=`{card.get('status', '')}` "
            f"family=`{card.get('kernel_family', '')}` index_eligible=`{card.get('index_eligible', False)}`"
        )
        if card.get("issues"):
            for issue in card["issues"]:
                lines.append(f"  - issue {issue.get('gate', '')}: {issue.get('message', '')}")
        if card.get("warnings"):
            for warning in card["warnings"][:3]:
                lines.append(f"  - warning {warning.get('gate', '')}: {warning.get('message', '')}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    inbox = Path(args.inbox).expanduser().resolve()
    report_json = Path(args.report_json).expanduser().resolve()
    report_md = Path(args.report_md).expanduser().resolve()
    approved_catalog = Path(args.approved_catalog).expanduser().resolve()
    cards = _scan_cards(inbox)
    hard_failures: list[dict[str, str]] = []
    soft_warnings: list[dict[str, str]] = []
    actions: dict[str, list[str]] = {"approved": [], "rejected": [], "skipped": []}

    approve_targets, missing_approve = _match_targets(cards, args.approve or [])
    reject_targets, missing_reject = _match_targets(cards, args.reject or [])
    for target in missing_approve:
        hard_failures.append({"gate": "approve_target", "message": f"approve target not found: {target}"})
    for target in missing_reject:
        hard_failures.append({"gate": "reject_target", "message": f"reject target not found: {target}"})

    updated_by_path = {str(card["path"]): card for card in cards}
    if not hard_failures:
        for card in approve_targets:
            if card.get("issues") and not args.allow_incomplete:
                actions["skipped"].append(card["id"])
                hard_failures.append(
                    {
                        "gate": "approve_incomplete_card",
                        "message": f"{card['id']} has unresolved issues; rerun with --allow-incomplete only after agent review.",
                    }
                )
                continue
            updated = _write_card_status(
                card,
                status="review_approved",
                reviewer=args.reviewer,
                notes=args.notes,
                dry_run=args.dry_run,
            )
            updated_by_path[str(card["path"])] = updated
            actions["approved"].append(card["id"])
        for card in reject_targets:
            updated = _write_card_status(
                card,
                status="review_rejected",
                reviewer=args.reviewer,
                notes=args.notes,
                dry_run=args.dry_run,
            )
            updated_by_path[str(card["path"])] = updated
            actions["rejected"].append(card["id"])

    final_cards = sorted(updated_by_path.values(), key=lambda item: str(item["path"]))
    approved_catalog_count = _sync_approved_catalog(final_cards, approved_catalog, dry_run=args.dry_run)
    pending_count = sum(1 for card in final_cards if card.get("status") in PENDING_STATUSES)
    approved_count = sum(1 for card in final_cards if card.get("index_eligible"))
    issue_count = sum(len(card.get("issues") or []) for card in final_cards)
    if pending_count:
        soft_warnings.append(
            {
                "gate": "pending_review_cards",
                "message": f"{pending_count} learned experience card(s) still require review and will be skipped by index rebuild.",
            }
        )
    if issue_count:
        soft_warnings.append({"gate": "card_quality_issues", "message": f"{issue_count} card issue(s) need review."})
    public_cards = [
        {key: value for key, value in card.items() if not key.startswith("_")}
        for card in final_cards
    ]
    report: dict[str, Any] = {
        "schema_version": 1,
        "status": "blocked" if hard_failures else ("planned" if args.dry_run else "completed"),
        "inbox": str(inbox),
        "cards_total": len(final_cards),
        "counts_by_status": _counts(final_cards),
        "approved_for_index_count": approved_count,
        "pending_review_count": pending_count,
        "approved_catalog_count": approved_catalog_count,
        "actions": actions,
        "cards": public_cards,
        "artifacts": {
            "review_report_json": str(report_json),
            "review_report_md": str(report_md),
            "approved_catalog": str(approved_catalog),
        },
        "policy": {
            "unreviewed_indexing": "forbidden",
            "index_eligible_statuses": sorted(APPROVED_STATUSES),
            "requires_explicit_approval": True,
        },
        "hard_gate_failures": hard_failures,
        "soft_gate_warnings": soft_warnings,
    }
    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_markdown_report(report_md, report)
    return report, 2 if hard_failures else 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Review learned kernel-experience cards")
    parser.add_argument("--inbox", default=str(DEFAULT_INBOX))
    parser.add_argument("--report-json", default="experience_review_report.json")
    parser.add_argument("--report-md", default="experience_review_report.md")
    parser.add_argument("--approved-catalog", default=str(DEFAULT_APPROVED_CATALOG))
    parser.add_argument("--approve", action="append", default=[], help="Experience id, filename, or path to mark review_approved.")
    parser.add_argument("--reject", action="append", default=[], help="Experience id, filename, or path to mark review_rejected.")
    parser.add_argument("--reviewer", default="")
    parser.add_argument("--notes", default="")
    parser.add_argument("--allow-incomplete", action="store_true", help="Allow explicit approval even when review warnings/issues exist.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    report, code = run(args)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
