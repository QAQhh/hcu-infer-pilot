#!/usr/bin/env python3
"""Check or filter SGLang history docs to keep only local fork commits.

The SGLang docs under this knowledge base must not duplicate commits that are
reachable from the upstream GitHub repository `sgl-project/sglang`. This helper
uses local `refs/remotes/github-official/*` refs in the SGLang worktree as the
official baseline.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SGLANG_DOC_ROOT = ROOT / "sglang"
DEFAULT_SGLANG_WORKTREE = Path(
    "/public/home/yangyn1/work_space/2026/sglang/sglang"
)
DEFAULT_OFFICIAL_REF_PREFIX = "refs/remotes/github-official"


def run_git(worktree: Path, args: list[str]) -> str:
    proc = subprocess.run(
        ["git", "-c", f"safe.directory={worktree}", *args],
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise SystemExit(f"git command failed: {' '.join(args)}\n{proc.stderr}")
    return proc.stdout


def official_commits(worktree: Path, ref_prefix: str) -> tuple[set[str], set[str]]:
    refs = [
        line.strip()
        for line in run_git(
            worktree,
            ["for-each-ref", "--format=%(refname)", ref_prefix],
        ).splitlines()
        if line.strip()
    ]
    if not refs:
        raise SystemExit(
            "missing official SGLang refs. Fetch them first, e.g.:\n"
            "git fetch https://github.com/sgl-project/sglang.git "
            "'+refs/heads/*:refs/remotes/github-official/*'"
        )
    full = set(run_git(worktree, ["rev-list", *refs]).splitlines())
    short = {sha[:9] for sha in full}
    return full, short


def markdown_files() -> list[Path]:
    return sorted(SGLANG_DOC_ROOT.glob("*/README.*.md"))


def official_refs_in_text(text: str, official_full: set[str], official_short: set[str]) -> set[str]:
    refs = set()
    refs.update(sha for sha in re.findall(r"`([0-9a-f]{40})`", text) if sha in official_full)
    refs.update(sha for sha in re.findall(r"`([0-9a-f]{9})`", text) if sha in official_short)
    return refs


def check_docs(worktree: Path, ref_prefix: str) -> int:
    official_full, official_short = official_commits(worktree, ref_prefix)
    bad: list[tuple[Path, set[str]]] = []
    for path in markdown_files():
        refs = official_refs_in_text(path.read_text(encoding="utf-8"), official_full, official_short)
        if refs:
            bad.append((path, refs))

    print(f"official refs checked: {len(official_full)} commits")
    print(f"SGLang docs checked: {len(markdown_files())} files")
    if not bad:
        print("official residual commits: 0")
        return 0

    print(f"official residual docs: {len(bad)}")
    for path, refs in bad:
        sample = ", ".join(f"`{sha}`" for sha in sorted(refs)[:8])
        print(f"- {path.relative_to(ROOT)}: {sample}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify SGLang history docs contain only local fork commits."
    )
    parser.add_argument(
        "--sglang-worktree",
        type=Path,
        default=DEFAULT_SGLANG_WORKTREE,
        help="Local SGLang git worktree used for official-ref comparison.",
    )
    parser.add_argument(
        "--official-ref-prefix",
        default=DEFAULT_OFFICIAL_REF_PREFIX,
        help="Local ref prefix for fetched sgl-project/sglang refs.",
    )
    args = parser.parse_args()
    return check_docs(args.sglang_worktree, args.official_ref_prefix)


if __name__ == "__main__":
    raise SystemExit(main())
