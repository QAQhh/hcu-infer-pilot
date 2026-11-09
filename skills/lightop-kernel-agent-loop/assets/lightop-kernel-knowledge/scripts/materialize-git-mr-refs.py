#!/usr/bin/env python3
"""Materialize GitLab-style merge-request refs as PR evidence bundles.

This supports repositories whose web/API merge-request endpoints are gated but
whose git refs expose refs/merge-requests/<id>/{head,merge}.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from _knowledge_root import knowledge_root


BUNDLE_ROOT = Path("evidence") / "pull-bundles"
SNAPSHOT_DIR = "source-snapshot"
DIFF_NAME = "review.diff"
UPSTREAM_NAME = "upstream.json"
ORIGIN_NAME = "ORIGIN.yaml"

SOURCE_SUFFIXES = {
    ".c",
    ".cc",
    ".cpp",
    ".cu",
    ".cuh",
    ".h",
    ".hh",
    ".hpp",
    ".inl",
    ".inc",
    ".py",
    ".pyi",
    ".cmake",
    ".txt",
    ".md",
    ".yaml",
    ".yml",
    ".json",
    ".sh",
}

PATH_HINTS = {
    "attention",
    "benchmark",
    "bench",
    "binding",
    "csrc",
    "dispatch",
    "export",
    "fp8",
    "gemm",
    "gfx",
    "hip",
    "kernel",
    "lightop",
    "moe",
    "profile",
    "quant",
    "rocm",
    "test",
}


def git_text(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def git_bytes(repo: Path, *args: str, check: bool = True) -> bytes:
    result = subprocess.run(["git", *args], cwd=repo, check=False, capture_output=True)
    if check and result.returncode != 0:
        msg = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(msg or f"git {' '.join(args)} failed")
    return result.stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relpath(path: str) -> Path | None:
    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts:
        return None
    if any(any(ch in part for ch in '<>:"|?*') for part in pure.parts):
        return None
    return Path(*pure.parts)


def scalar_log(repo: Path, rev: str, fmt: str) -> str:
    return git_text(repo, "log", "-1", f"--format={fmt}", rev)


def fetch_repo(remote_url: str) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="kernelpilot-mr-"))
    try:
        git_text(tmp, "init", ".")
        git_text(tmp, "remote", "add", "origin", remote_url)
        git_text(
            tmp,
            "fetch",
            "--no-tags",
            "--prune",
            "origin",
            "+refs/heads/*:refs/remotes/origin/*",
            "+refs/merge-requests/*/head:refs/remotes/origin/merge-requests/*/head",
            "+refs/merge-requests/*/merge:refs/remotes/origin/merge-requests/*/merge",
        )
        return tmp
    except Exception:
        shutil.rmtree(tmp, ignore_errors=True)
        raise


def discover_merge_requests(repo: Path) -> dict[int, dict[str, str]]:
    rows = git_text(
        repo,
        "for-each-ref",
        "--format=%(refname:short) %(objectname)",
        "refs/remotes/origin/merge-requests",
        check=False,
    )
    out: dict[int, dict[str, str]] = {}
    for line in rows.splitlines():
        match = re.match(r"origin/merge-requests/(\d+)/(head|merge)\s+([0-9a-f]{40})$", line)
        if not match:
            continue
        number = int(match.group(1))
        kind = match.group(2)
        oid = match.group(3)
        out.setdefault(number, {})[kind] = oid
    return {number: refs for number, refs in sorted(out.items()) if refs.get("head")}


def resolve_ref(repo: Path, ref: str) -> str | None:
    value = git_text(repo, "rev-parse", "--verify", ref, check=False)
    return value.strip() or None


def resolve_default_ref(repo: Path, branch: str) -> str:
    candidates = [branch, "master", "main"]
    for candidate in candidates:
        ref = f"refs/remotes/origin/{candidate}"
        if resolve_ref(repo, ref):
            return ref
    heads = git_text(repo, "for-each-ref", "--format=%(refname)", "refs/remotes/origin", check=False)
    for line in heads.splitlines():
        if "/merge-requests/" not in line:
            return line.strip()
    raise RuntimeError("no default branch ref found")


def diff_base_and_target(repo: Path, refs: dict[str, str], default_ref: str) -> tuple[str, str]:
    head_sha = refs["head"]
    merge_sha = refs.get("merge")
    if merge_sha:
        parents = git_text(repo, "rev-list", "--parents", "-n", "1", merge_sha).split()
        if len(parents) >= 2:
            return parents[1], merge_sha
    base = git_text(repo, "merge-base", default_ref, head_sha, check=False)
    if not base:
        base = git_text(repo, "rev-parse", default_ref)
    return base, head_sha


def changed_paths(repo: Path, base: str, target: str) -> list[str]:
    text = git_text(repo, "diff", "--name-only", "--find-renames", base, target, check=False)
    return [line.strip() for line in text.splitlines() if line.strip()]


def changed_paths_with_status(repo: Path, base: str, target: str) -> list[tuple[str, str]]:
    text = git_text(repo, "diff", "--name-status", "--find-renames", base, target, check=False)
    rows: list[tuple[str, str]] = []
    for line in text.splitlines():
        parts = line.split("\t")
        if not parts:
            continue
        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            rows.append((status, parts[2]))
        elif len(parts) >= 2:
            rows.append((status, parts[1]))
    return rows


def is_source_candidate(path: str) -> bool:
    lower = path.lower()
    suffix = PurePosixPath(path).suffix.lower()
    if PurePosixPath(path).name == "CMakeLists.txt":
        return True
    if suffix in SOURCE_SUFFIXES:
        return True
    return any(hint in lower for hint in PATH_HINTS)


def classify(repo_id: str, repo_name: str, title: str, paths: list[str]) -> dict[str, list[str]]:
    text = " ".join([repo_id, repo_name, title, *paths]).lower()
    tags = {"dcu", "rocm", "hip"}
    architectures = {"dcu", "gfx928", "gfx936", "gfx938"}
    techniques: set[str] = set()
    hardware_features: set[str] = set()
    kernel_types: set[str] = set()
    languages: set[str] = set()

    if "lightop" in text:
        tags.add("lightop")
    if "flash" in text or "attention" in text or "fa" in repo_id:
        tags.update({"attention", "flash-attention"})
        kernel_types.add("attention")
    if "cutlass" in text:
        tags.add("cutlass")
    if "moe" in text or "expert" in text:
        tags.add("moe")
        kernel_types.add("moe")
    if "gemm" in text or "bmm" in text or "matmul" in text:
        tags.add("gemm")
        kernel_types.add("gemm")
    if "norm" in text or "rms" in text or "layernorm" in text:
        tags.add("norm")
        kernel_types.add("norm")
    if "softmax" in text:
        tags.add("softmax")
        kernel_types.add("softmax")
    if "topk" in text:
        tags.add("topk")
        kernel_types.add("topk")
    if "quant" in text or "fp8" in text or "int8" in text or "w8a8" in text or "w4a8" in text:
        tags.add("quantization")
        kernel_types.add("quantization")
        techniques.add("quantization")
    if "fuse" in text or "fused" in text:
        techniques.add("kernel-fusion")
    if "dispatch" in text or "config" in text or "gfx" in text:
        techniques.add("dispatch")
    if "bench" in text or "perf" in text:
        tags.add("benchmark")
        techniques.add("benchmarking")
    if "profile" in text or "hipprof" in text or "rocprof" in text:
        techniques.add("profiling")
    if "cmake" in text or "setup.py" in text or "build" in text:
        techniques.add("build-system")
    if "layout" in text or "transpose" in text or "permute" in text:
        techniques.add("layout-transform")
    if "lds" in text:
        hardware_features.add("lds")
    if "mfma" in text:
        hardware_features.add("mfma")
    for token in ("bf16", "fp16", "fp8", "int8", "w8a8", "w4a8"):
        if token in text:
            hardware_features.add(token)

    for path in paths:
        suffix = PurePosixPath(path).suffix.lower()
        if suffix in {".cu", ".cuh"}:
            languages.update({"hip", "cuda-cpp"})
        elif suffix in {".cc", ".cpp", ".c", ".h", ".hpp", ".hh"}:
            languages.add("cpp")
        elif suffix == ".py":
            languages.add("python")
        elif suffix in {".cmake"} or PurePosixPath(path).name == "CMakeLists.txt":
            languages.add("cmake")
        elif suffix == ".json":
            languages.add("json")
        elif suffix in {".yaml", ".yml"}:
            languages.add("yaml")
        elif suffix == ".md":
            languages.add("markdown")
        elif suffix in {".sh"}:
            languages.add("shell")

    if not techniques:
        techniques.add("implementation")
    if not kernel_types:
        kernel_types.add("runtime")
    if not languages:
        languages.add("unknown")

    return {
        "architectures": sorted(architectures),
        "tags": sorted(tags),
        "techniques": sorted(techniques),
        "hardware_features": sorted(hardware_features),
        "kernel_types": sorted(kernel_types),
        "languages": sorted(languages),
    }


def write_source_snapshot(
    repo: Path,
    bundle: Path,
    target: str,
    rows: list[tuple[str, str]],
    max_files: int,
    max_file_bytes: int,
) -> list[dict[str, Any]]:
    snapshot_root = bundle / SNAPSHOT_DIR
    snapshot_root.mkdir(parents=True, exist_ok=True)
    files: list[dict[str, Any]] = []
    selected = 0
    for status, upstream_path in rows:
        if status.startswith("D"):
            continue
        if selected >= max_files:
            break
        if not is_source_candidate(upstream_path):
            continue
        safe = safe_relpath(upstream_path)
        if safe is None:
            continue
        data = git_bytes(repo, "show", f"{target}:{upstream_path}", check=False)
        if not data:
            continue
        truncated = len(data) > max_file_bytes
        if truncated:
            data = data[:max_file_bytes] + b"\n\n/* truncated by materialize-git-mr-refs.py */\n"
        local_path = Path(SNAPSHOT_DIR) / safe
        out = bundle / local_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        files.append(
            {
                "local_path": local_path.as_posix(),
                "role": "upstream-file",
                "mode": "verbatim",
                "upstream_path": upstream_path,
                "sha256": sha256(data),
                **({"size_cap_truncated": True} if truncated else {}),
            }
        )
        selected += 1
    return files


def render_page(repo_id: str, entry: dict[str, Any]) -> str:
    number = entry["number"]
    frontmatter = {
        "id": f"pr-{repo_id}-{number}",
        "repo": entry["repo"],
        "pr": number,
        "title": entry["title"],
        "author": entry["author"],
        "date": entry["date"],
        "url": entry["url"],
        "source_category": "upstream-code",
        "architectures": entry["architectures"],
        "tags": entry["tags"],
        "techniques": entry["techniques"],
        "hardware_features": entry["hardware_features"],
        "kernel_types": entry["kernel_types"],
        "languages": entry["languages"],
        "captured_at": entry["captured_at"],
        "status": entry["status"],
        "merge_sha": entry.get("merge_sha", "unknown"),
        "inclusion_reason": entry["inclusion_reason"],
        "changed_paths": entry["changed_paths"],
        "artifact_dir": entry["artifact_dir"],
    }
    body = [
        f"# {entry['title']}",
        "",
        f"- Repository: `{entry['repo']}`",
        f"- MR: [{number}]({entry['url']})",
        f"- Decision: `{entry['decision']}`",
        f"- Reason: {entry['inclusion_reason']}",
        "",
        "## Changed Paths",
        "",
    ]
    body.extend(f"- `{path}`" for path in entry["changed_paths"][:80])
    body.extend(["", "## Artifact Bundle", "", f"`{entry['artifact_dir']}`"])
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=200) + "---\n" + "\n".join(body) + "\n"


def materialize_one(
    repo: Path,
    root: Path,
    repo_id: str,
    repo_name: str,
    web_url: str,
    default_ref: str,
    number: int,
    refs: dict[str, str],
    args: argparse.Namespace,
    captured_at: str,
) -> dict[str, Any]:
    bundle = root / BUNDLE_ROOT / repo_id / f"mr-{number}"
    if bundle.exists() and args.force:
        shutil.rmtree(bundle)
    bundle.mkdir(parents=True, exist_ok=True)

    head_sha = refs["head"]
    merge_sha = refs.get("merge")
    base, target = diff_base_and_target(repo, refs, default_ref)
    title = scalar_log(repo, head_sha, "%s") or f"MR-{number}"
    author = scalar_log(repo, head_sha, "%an") or "unknown"
    date = scalar_log(repo, head_sha, "%cs") or captured_at[:10]
    changed = changed_paths(repo, base, target)
    status_rows = changed_paths_with_status(repo, base, target)

    diff = git_bytes(repo, "diff", "--binary", "--find-renames", base, target, check=False)
    truncated_diff = len(diff) > args.max_diff_bytes
    if truncated_diff:
        diff = diff[: args.max_diff_bytes] + b"\n\n# truncated by materialize-git-mr-refs.py\n"
    (bundle / DIFF_NAME).write_bytes(diff)

    snapshot_files = write_source_snapshot(
        repo,
        bundle,
        target,
        status_rows,
        args.max_snapshot_files,
        args.max_snapshot_file_bytes,
    )

    mr_url = f"{web_url.rstrip('/')}/-/merge_requests/{number}"
    classes = classify(repo_id, repo_name, title, changed)
    artifact_dir = (BUNDLE_ROOT / repo_id / f"mr-{number}").as_posix()
    upstream = {
        "repo": repo_name,
        "repo_id": repo_id,
        "remote_url": args.url,
        "url": mr_url,
        "mr": number,
        "state_hint": "git-ref-only",
        "status_note": "Web/API state was not available; status is treated as open for reviewable MR evidence.",
        "title": title,
        "author": author,
        "date": date,
        "head_sha": head_sha,
        "merge_ref_sha": merge_sha,
        "base_sha": base,
        "target_sha": target,
        "default_branch": args.default_branch,
        "changed_paths": changed,
        "captured_at": captured_at,
    }
    (bundle / UPSTREAM_NAME).write_text(json.dumps(upstream, indent=2, ensure_ascii=False), encoding="utf-8")

    origin_files = [
        {
            "local_path": DIFF_NAME,
            "role": "pr-diff",
            "mode": "upstream-patch",
            "sha256": sha256(diff),
            **({"size_cap_truncated": True} if truncated_diff else {}),
        },
        *snapshot_files,
    ]
    origin = {
        "origin_url": mr_url,
        "upstream_repo": repo_name,
        "license": "unknown",
        "retrieved_at": captured_at,
        "asset_mode": "verbatim",
        "upstream_sha": target,
        "files": origin_files,
        **({"size_cap_truncated": True} if truncated_diff or any(item.get("size_cap_truncated") for item in snapshot_files) else {}),
    }
    (bundle / ORIGIN_NAME).write_text(yaml.safe_dump(origin, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")

    readme = [
        f"# mr-{number}: {title}",
        "",
        f"- Repository: `{repo_name}`",
        f"- URL: {mr_url}",
        f"- Head SHA: `{head_sha}`",
        f"- Merge-ref SHA: `{merge_sha or 'not exposed'}`",
        f"- Base SHA: `{base}`",
        f"- Target SHA: `{target}`",
        f"- Diff: `{DIFF_NAME}`",
        f"- Source snapshot: `{len(snapshot_files)}` captured under `{SNAPSHOT_DIR}/`",
        "",
        "See `ORIGIN.yaml` for upstream refs and fetch status.",
        "",
    ]
    (bundle / "README.md").write_text("\n".join(readme), encoding="utf-8")

    entry = {
        "number": number,
        "pr": number,
        "title": title,
        "repo": repo_name,
        "url": mr_url,
        "date": date,
        "author": author,
        "captured_at": captured_at,
        "decision": "include",
        "status": "open",
        "reason": "git merge-request refs materialized into LightOp/DCU knowledge",
        "inclusion_reason": "Use as LightOp/DCU upstream MR evidence; web/API MR state was unavailable, so validate portability against local LightOp before reuse.",
        "seed_source": "git-merge-request-refs",
        "head_ref_oid": head_sha,
        "merge_sha": merge_sha or "unknown",
        "base_sha": base,
        "target_sha": target,
        "changed_paths": changed,
        "artifact_dir": artifact_dir,
        **classes,
    }
    return entry


def write_candidate_ledger(root: Path, repo_id: str, repo_name: str, entries: list[dict[str, Any]], captured_at: str) -> None:
    ledger = {
        "repo": repo_name,
        "searched_at": captured_at[:10],
        "keywords_used": ["lightop", "dcu", "rocm", "hip", "merge-request-refs"],
        "total_candidates": len(entries),
        "included": len(entries),
        "excluded": 0,
        "deferred": 0,
        "prs": entries,
    }
    out = root / "candidates" / f"{repo_id}.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(ledger, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")


def write_source_pages(root: Path, repo_id: str, entries: list[dict[str, Any]], force: bool) -> int:
    out_dir = root / "sources" / "prs" / repo_id
    out_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for entry in entries:
        path = out_dir / f"PR-{entry['number']}.md"
        if path.exists() and not force:
            continue
        path.write_text(render_page(repo_id, entry), encoding="utf-8")
        count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-id", required=True, help="local knowledge repo id")
    parser.add_argument("--repo", required=True, help="display repository name")
    parser.add_argument("--url", required=True, help="git remote URL")
    parser.add_argument("--web-url", default=None, help="browser URL; defaults to --url without .git")
    parser.add_argument("--default-branch", default="master")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--max-snapshot-files", type=int, default=12)
    parser.add_argument("--max-snapshot-file-bytes", type=int, default=512_000)
    parser.add_argument("--max-diff-bytes", type=int, default=20_000_000)
    args = parser.parse_args()

    root = knowledge_root()
    captured_at = datetime.now(timezone.utc).isoformat()
    web_url = args.web_url or re.sub(r"\.git$", "", args.url.rstrip("/"))
    worktree = fetch_repo(args.url)
    try:
        default_ref = resolve_default_ref(worktree, args.default_branch)
        refs_by_mr = discover_merge_requests(worktree)
        entries = [
            materialize_one(
                worktree,
                root,
                args.repo_id,
                args.repo,
                web_url,
                default_ref,
                number,
                refs,
                args,
                captured_at,
            )
            for number, refs in refs_by_mr.items()
        ]
        write_candidate_ledger(root, args.repo_id, args.repo, entries, captured_at)
        pages = write_source_pages(root, args.repo_id, entries, args.force)
        print(
            json.dumps(
                {
                    "repo_id": args.repo_id,
                    "merge_requests": len(entries),
                    "pages_written": pages,
                    "candidate_ledger": f"candidates/{args.repo_id}.yaml",
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    finally:
        shutil.rmtree(worktree, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
