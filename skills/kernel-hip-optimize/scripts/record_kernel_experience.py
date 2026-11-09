#!/usr/bin/env python3
"""Record reusable kernel optimization experience from optimizer artifacts.

This script writes reviewable knowledge artifacts. It does not rebuild the RAG
index and it does not change optimizer rules by default.
"""

from __future__ import annotations

import argparse
import hashlib
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
DEFAULT_KB_INBOX = default_experience_inbox(REPO_ROOT) if default_experience_inbox else SKILL_DIR / "knowledge-base" / "learned-experiences"
DEFAULT_EXPERIENCE_CATALOG = SKILL_DIR / "references" / "learned_kernel_experiences.jsonl"


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


def _write_text(path: str | Path, text: str) -> None:
    p = Path(path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _safe_name(value: str) -> str:
    text = re.sub(r"[^0-9A-Za-z_.-]+", "-", str(value).strip().lower())
    text = text.strip("-")
    return text or "kernel-experience"


def _sha1_text(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8", errors="ignore")).hexdigest()[:12]


def _load_optimizer_state(run_dir: Path | None, state_path: Path | None) -> dict[str, Any]:
    if state_path and state_path.is_file():
        return _read_json(state_path)
    if run_dir and (run_dir / "state.json").is_file():
        return _read_json(run_dir / "state.json")
    return {}


def _latest_iter_dir(run_dir: Path | None, state: dict[str, Any]) -> Path | None:
    if not run_dir or not run_dir.is_dir():
        return None
    current_iter = int(_safe_float(state.get("current_iter"), 0.0))
    if current_iter > 0 and (run_dir / f"iterv{current_iter}").is_dir():
        return run_dir / f"iterv{current_iter}"
    candidates = [p for p in run_dir.glob("iterv*") if p.is_dir()]
    if not candidates:
        return None
    candidates.sort(key=lambda p: (p.stat().st_mtime, p.name), reverse=True)
    return candidates[0]


def _load_latest_artifacts(run_dir: Path | None, state: dict[str, Any]) -> dict[str, Any]:
    iter_dir = _latest_iter_dir(run_dir, state)
    if iter_dir is None:
        return {}
    return {
        "iter_dir": str(iter_dir),
        "branch_results": _read_json(iter_dir / "branch_results.json"),
        "branch_plan": _read_json(iter_dir / "branch_plan.json"),
        "methods": _read_json(iter_dir / "methods.json"),
        "family_guidance": _read_json(iter_dir / "kernel_family_guidance.json"),
        "champion_methods": _read_json(iter_dir / "champion_methods.json"),
        "roofline": _read_json(iter_dir / "roofline.json"),
        "hcu_top": _read_json(iter_dir / "hcu_top.json"),
        "analysis_md": str(iter_dir / "analysis.md") if (iter_dir / "analysis.md").is_file() else "",
    }


def _best_branch_from_results(branch_results: dict[str, Any]) -> dict[str, Any]:
    for key in ("best_branch", "best", "champion", "winner"):
        value = branch_results.get(key)
        if isinstance(value, dict):
            return value
    rows = branch_results.get("branches") or branch_results.get("results") or []
    best: dict[str, Any] = {}
    best_ms = float("inf")
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, dict):
            continue
        if not bool(row.get("passed", row.get("correct", row.get("ok", True)))):
            continue
        ms = _safe_float(row.get("ms") or row.get("best_ms") or row.get("median_ms"), float("inf"))
        if ms < best_ms:
            best = row
            best_ms = ms
    return best


def _infer_family(kernel_result: dict[str, Any], artifacts: dict[str, Any], state: dict[str, Any]) -> str:
    for value in [
        _as_dict(kernel_result.get("operator_contract")).get("family"),
        _as_dict(_as_dict(kernel_result.get("operator_contract")).get("operator")).get("family"),
        _as_dict(_as_dict(kernel_result.get("operator_contract")).get("semantic_fields")).get("operator_family"),
        _as_dict(artifacts.get("family_guidance")).get("primary_family"),
        _as_dict(state.get("generator_capability")).get("family"),
    ]:
        text = str(value or "").strip()
        if text:
            return text
    matched = _as_list(_as_dict(artifacts.get("family_guidance")).get("matched_families"))
    if matched and isinstance(matched[0], dict):
        return str(matched[0].get("family") or "")
    return "unknown"


def _method_ids_from_artifacts(kernel_result: dict[str, Any], artifacts: dict[str, Any], best_branch: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for source in [
        best_branch.get("claimed_method_ids"),
        _as_dict(artifacts.get("champion_methods")).get("claimed_method_ids"),
        _as_dict(artifacts.get("champion_methods")).get("method_ids"),
        _as_dict(kernel_result.get("optimizer")).get("selected_method_ids"),
    ]:
        for item in _as_list(source):
            text = str(item).strip()
            if text and text not in out:
                out.append(text)
    if out:
        return out
    for method in _as_list(_as_dict(artifacts.get("methods")).get("methods")):
        if isinstance(method, dict):
            text = str(method.get("id") or "").strip()
            if text and text not in out:
                out.append(text)
    return out


def _build_experience(args: argparse.Namespace) -> dict[str, Any]:
    run_dir = Path(args.run_dir).expanduser().resolve() if args.run_dir else None
    state_path = Path(args.state).expanduser().resolve() if args.state else None
    kernel_result_path = Path(args.kernel_result_manifest).expanduser().resolve() if args.kernel_result_manifest else None
    kernel_result = _read_json(kernel_result_path) if kernel_result_path else {}
    state = _load_optimizer_state(run_dir, state_path)
    if not run_dir and state.get("run_dir"):
        run_dir = Path(str(state["run_dir"])).expanduser().resolve()
    artifacts = _load_latest_artifacts(run_dir, state)
    best_branch = _best_branch_from_results(_as_dict(artifacts.get("branch_results")))
    family = str(args.family or _infer_family(kernel_result, artifacts, state) or "unknown")
    method_ids = _method_ids_from_artifacts(kernel_result, artifacts, best_branch)
    performance = _as_dict(kernel_result.get("performance"))
    best_ms = (
        _safe_float(performance.get("best_metric_ms"), 0.0)
        or _safe_float(best_branch.get("ms") or best_branch.get("best_ms") or best_branch.get("median_ms"), 0.0)
    )
    baseline_ms = _safe_float(performance.get("baseline_metric_ms"), 0.0)
    speedup = _safe_float(performance.get("speedup_vs_baseline"), 0.0)
    if not speedup and baseline_ms > 0 and best_ms > 0:
        speedup = baseline_ms / best_ms
    title_seed = " ".join(
        [
            family,
            str(best_branch.get("generator") or ""),
            " ".join(method_ids),
            str(run_dir or ""),
        ]
    )
    exp_id = _safe_name(args.experience_id or f"{family}-{_sha1_text(title_seed)}")
    return {
        "schema_version": 1,
        "id": exp_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "review_required",
        "source": {
            "run_dir": str(run_dir or ""),
            "state": str(state_path or (run_dir / "state.json" if run_dir else "")),
            "kernel_result_manifest": str(kernel_result_path or ""),
            "iter_dir": str(artifacts.get("iter_dir") or ""),
        },
        "kernel_family": family,
        "generator": str(best_branch.get("generator") or best_branch.get("mode") or ""),
        "plan": best_branch.get("plan") if isinstance(best_branch.get("plan"), dict) else {},
        "method_ids": method_ids,
        "performance": {
            "baseline_ms": baseline_ms,
            "best_ms": best_ms,
            "speedup_vs_baseline": speedup,
        },
        "semantic_contract": {
            "required": True,
            "notes": [
                "Only promote this experience after correctness, parity, and benchmark contract checks passed.",
                "Treat generated source patterns as candidates, not proof of semantic equivalence.",
            ],
        },
        "profile_evidence": {
            "roofline_bound": _as_dict(artifacts.get("roofline")).get("bound", ""),
            "family_guidance_status": _as_dict(artifacts.get("family_guidance")).get("status", ""),
            "primary_family": _as_dict(artifacts.get("family_guidance")).get("primary_family", ""),
            "top_hcu_metrics": _as_list(_as_dict(artifacts.get("hcu_top")).get("compute"))[:3]
            + _as_list(_as_dict(artifacts.get("hcu_top")).get("memory"))[:3]
            + _as_list(_as_dict(artifacts.get("hcu_top")).get("latency"))[:3],
        },
        "reusable_pattern": {
            "when_to_try": args.when_to_try or "Use as a candidate when the same family, contract fields, and profiler symptoms recur.",
            "do_not_use_when": args.do_not_use_when or "Do not use when semantic contract, shape/layout, duplicate-index, RNG, or aliasing rules differ.",
            "validation_gates": [
                "compile",
                "operator_correctness",
                "microbench",
                "profile_diff",
                "project_accuracy_or_parity",
            ],
        },
        "agent_notes": args.notes,
    }


def _experience_markdown(exp: dict[str, Any]) -> str:
    perf = _as_dict(exp.get("performance"))
    pattern = _as_dict(exp.get("reusable_pattern"))
    lines = [
        "---",
        f"title: Learned Kernel Experience - {exp.get('kernel_family', 'unknown')}",
        "type: learned-kernel-experience",
        f"kernel_family: {exp.get('kernel_family', '')}",
        f"status: {exp.get('status', 'review_required')}",
        f"created_at: {exp.get('created_at', '')}",
        "---",
        "",
        f"# Learned Kernel Experience: {exp.get('kernel_family', 'unknown')}",
        "",
        "This card is generated from optimizer artifacts and must be reviewed before it is treated as stable guidance.",
        "",
        "## Source",
        "",
    ]
    for key, value in _as_dict(exp.get("source")).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Result",
            "",
            f"- generator: `{exp.get('generator', '')}`",
            f"- methods: `{', '.join(str(item) for item in _as_list(exp.get('method_ids'))) or '-'}`",
            f"- baseline_ms: `{perf.get('baseline_ms', 0)}`",
            f"- best_ms: `{perf.get('best_ms', 0)}`",
            f"- speedup_vs_baseline: `{perf.get('speedup_vs_baseline', 0)}`",
            "",
            "## Reusable Pattern",
            "",
            f"- when_to_try: {pattern.get('when_to_try', '')}",
            f"- do_not_use_when: {pattern.get('do_not_use_when', '')}",
            "",
            "## Required Validation Gates",
            "",
        ]
    )
    for gate in _as_list(pattern.get("validation_gates")):
        lines.append(f"- {gate}")
    notes = str(exp.get("agent_notes") or "").strip()
    if notes:
        lines.extend(["", "## Agent Notes", "", notes])
    lines.extend(
        [
            "",
            "## Policy",
            "",
            "This is a candidate pattern for future agents. It should inform RAG retrieval and action planning, but it must not override semantic, benchmark, parity, accuracy, or profile-diff gates.",
            "",
        ]
    )
    return "\n".join(lines)


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    exp = _build_experience(args)
    out_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else Path.cwd() / "learned_kernel_experience"
    catalog_path = Path(args.catalog).expanduser().resolve() if args.catalog else DEFAULT_EXPERIENCE_CATALOG
    kb_inbox = Path(args.kb_inbox).expanduser().resolve() if args.kb_inbox else DEFAULT_KB_INBOX
    out_json = out_dir / f"{exp['id']}.json"
    out_md = out_dir / f"{exp['id']}.md"
    report: dict[str, Any] = {
        "schema_version": 1,
        "status": "planned" if args.dry_run else "completed",
        "experience_id": exp["id"],
        "artifacts": {
            "experience_json": str(out_json),
            "experience_md": str(out_md),
            "catalog_jsonl": str(catalog_path),
            "kb_inbox_md": str(kb_inbox / f"{exp['id']}.md"),
        },
        "experience": exp,
        "notes": [
            "Generated experience is review_required and does not rebuild the RAG index.",
            "Run the RAG index rebuild separately after review if semantic quality is acceptable.",
        ],
    }
    if args.dry_run:
        return report, 0
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_json, exp)
    _write_text(out_md, _experience_markdown(exp))
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    with catalog_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(exp, ensure_ascii=False, sort_keys=True) + "\n")
    if not args.no_kb_inbox:
        kb_inbox.mkdir(parents=True, exist_ok=True)
        _write_text(kb_inbox / f"{exp['id']}.md", _experience_markdown(exp))
    _write_json(out_dir / "record_kernel_experience_report.json", report)
    return report, 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Record reusable kernel optimization experience")
    parser.add_argument("--run-dir", default="", help="Kernel optimizer run_dir containing state.json and iterv*/ artifacts.")
    parser.add_argument("--state", default="", help="Explicit optimizer state.json.")
    parser.add_argument("--kernel-result-manifest", default="", help="Optional kernel_result_manifest.json from auto runner.")
    parser.add_argument("--family", default="", help="Optional kernel family override.")
    parser.add_argument("--experience-id", default="")
    parser.add_argument("--when-to-try", default="")
    parser.add_argument("--do-not-use-when", default="")
    parser.add_argument("--notes", default="")
    parser.add_argument("--output-dir", default="")
    parser.add_argument("--catalog", default=str(DEFAULT_EXPERIENCE_CATALOG))
    parser.add_argument("--kb-inbox", default=str(DEFAULT_KB_INBOX))
    parser.add_argument("--no-kb-inbox", action="store_true", help="Do not copy Markdown into the RAG knowledge-base inbox.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    report, code = run(args)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
