#!/usr/bin/env python3
"""Rebuild local framework commit-history docs.

This generator writes `model-pr-optimization-hg-history` from the local
`sglang` and `vllm` worktrees. It intentionally does not call GitHub APIs:
`model-pr-optimization-history` tracks open-source community PRs, while this
tree tracks local fork commits.

For SGLang, this tree must not duplicate upstream `sgl-project/sglang`
history. The generator filters out any commit reachable from local
`refs/remotes/github-official/*` refs and keeps only local fork commits.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from rebuild_model_pr_history_from_git import (
    MODEL_FILTERS,
    MODEL_ORDER,
    MODEL_TITLES,
    SHARED_BUCKET,
    clean_block,
    is_global_excluded,
    matches_any,
    md_escape,
    selected_files,
    shared_bucket_files,
)


ROOT = Path(__file__).resolve().parents[1]
COMMON_ROOT = ROOT.parent
FRAMEWORK_ROOTS = {
    "sglang": Path(os.environ.get("SGLANG_HG_HISTORY_ROOT", str(COMMON_ROOT / "sglang"))),
    "vllm": Path(os.environ.get("VLLM_HG_HISTORY_ROOT", str(COMMON_ROOT / "vllm"))),
}
HISTORY_ROOT = Path(
    os.environ.get(
        "MODEL_PR_HG_HISTORY_ROOT",
        str(ROOT / "model-pr-optimization-hg-history"),
    )
)
# Labels shown in generated docs; keep machine-specific paths out of the KB.
WORKTREE_LABELS = {
    "sglang": os.environ.get("SGLANG_HG_HISTORY_LABEL", "HYGON-AI/sglang-das"),
    "vllm": os.environ.get("VLLM_HG_HISTORY_LABEL", "HYGON-AI/vllm-plugin-das"),
}
TODAY = date.today().isoformat()

COMMIT_LIMIT = int(os.environ.get("MODEL_PR_HG_HISTORY_LIMIT", "3000"))
MAX_COMMITS_PER_DOC = int(os.environ.get("MODEL_PR_HG_HISTORY_MAX_DOC_COMMITS", "80"))
SGLANG_OFFICIAL_REF_PREFIX = os.environ.get(
    "SGLANG_HG_HISTORY_OFFICIAL_REF_PREFIX",
    "refs/remotes/github-official",
)
SGLANG_REQUIRE_OFFICIAL_FILTER = (
    os.environ.get("SGLANG_HG_HISTORY_REQUIRE_OFFICIAL_FILTER", "1") != "0"
)
SGLANG_DISABLE_OFFICIAL_FILTER = (
    os.environ.get("SGLANG_HG_HISTORY_DISABLE_OFFICIAL_FILTER", "0") == "1"
)
LOCAL_MODEL_TITLES = dict(MODEL_TITLES)
LOCAL_MODEL_TITLES[SHARED_BUCKET] = "Shared Framework Commits"


@dataclass
class CommitInfo:
    sha: str
    short: str
    date: str
    author: str
    subject: str
    files: list[str] = field(default_factory=list)


def run(cmd: list[str], cwd: Path, check: bool = True, stdin_text: str | None = None) -> str:
    if cmd and cmd[0] == "git":
        cmd = ["git", "-c", f"safe.directory={cwd}", *cmd[1:]]
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        input=stdin_text,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{proc.stderr}")
    return proc.stdout


def official_sglang_commits() -> set[str]:
    """Return commits reachable from the official GitHub SGLang refs.

    The refs are expected to be fetched locally, for example:

    git fetch https://github.com/sgl-project/sglang.git \
      '+refs/heads/*:refs/remotes/github-official/*'

    We do not fetch here because this generator must remain deterministic in
    offline/internal environments. If the refs are missing, fail closed by
    default instead of writing GitHub upstream commits into the local history.
    """

    if SGLANG_DISABLE_OFFICIAL_FILTER:
        return set()

    repo = FRAMEWORK_ROOTS["sglang"]
    refs = [
        line.strip()
        for line in run(
            ["git", "for-each-ref", "--format=%(refname)", SGLANG_OFFICIAL_REF_PREFIX],
            repo,
        ).splitlines()
        if line.strip()
    ]
    if not refs:
        message = (
            "missing local official SGLang refs for local-only filtering: "
            f"{SGLANG_OFFICIAL_REF_PREFIX}. Fetch them with: "
            "git fetch https://github.com/sgl-project/sglang.git "
            "'+refs/heads/*:refs/remotes/github-official/*'"
        )
        if SGLANG_REQUIRE_OFFICIAL_FILTER:
            raise RuntimeError(message)
        print(f"warning: {message}")
        return set()
    # Feed the refs through stdin: the local sgl-project/sglang ref set can hold
    # thousands of entries, which exceeds the Windows command-line length limit
    # (WinError 206) when expanded into argv.
    return set(
        run(["git", "rev-list", "--stdin"], repo, stdin_text="\n".join(refs) + "\n").splitlines()
    )


def git_files(framework: str) -> list[str]:
    out = run(["git", "ls-files"], FRAMEWORK_ROOTS[framework])
    files = [line.strip() for line in out.splitlines() if line.strip()]
    return [path for path in files if not is_global_excluded(path)]


def parse_commits(framework: str) -> list[CommitInfo]:
    fmt = "\x02%H\x01%h\x01%ad\x01%an\x01%s"
    out = run(
        [
            "git",
            "log",
            f"--max-count={COMMIT_LIMIT}",
            "--date=short",
            # Rename detection needs blob contents; on a blob:none partial clone
            # that triggers lazy fetches and fails in offline/sandboxed runs.
            "--no-renames",
            f"--format={fmt}",
            "--name-only",
        ],
        FRAMEWORK_ROOTS[framework],
    )
    commits: list[CommitInfo] = []
    current: CommitInfo | None = None
    for line in out.splitlines():
        if line.startswith("\x02"):
            if current:
                commits.append(current)
            parts = line[1:].split("\x01", 4)
            if len(parts) == 5:
                sha, short, when, author, subject = parts
                current = CommitInfo(sha=sha, short=short, date=when, author=author, subject=subject)
            else:
                current = None
            continue
        if current:
            path = line.strip()
            if path and not is_global_excluded(path):
                current.files.append(path)
    if current:
        commits.append(current)
    return commits


def filter_local_only_commits(
    framework: str,
    commits: list[CommitInfo],
    official_commits: set[str],
) -> list[CommitInfo]:
    if framework != "sglang" or SGLANG_DISABLE_OFFICIAL_FILTER:
        return commits
    filtered = [commit for commit in commits if commit.sha not in official_commits]
    removed = len(commits) - len(filtered)
    print(
        "sglang local-only filter: "
        f"removed {removed} upstream GitHub commits, kept {len(filtered)} local commits"
    )
    return filtered


def file_category(path: str) -> str:
    lower = path.lower()
    if lower.startswith((".github/", ".buildkite/")) or "workflow" in lower:
        return "ci"
    if "test/" in lower or "tests/" in lower:
        return "tests"
    if lower.startswith(("docs", "examples", "benchmark", "benchmarks")):
        return "docs-bench"
    if any(token in lower for token in ("kernel", "attention", "moe", "quant", "cache", "scheduler", "sampler", "distributed", "flash", "hip", "cuda", "rocm")):
        return "runtime-perf"
    if any(token in lower for token in ("/models/", "model_executor", "entrypoints", "server", "router", "worker", "config")):
        return "runtime-model"
    return "other"


def classify_subject(subject: str, files: list[str]) -> str:
    lower = " ".join([subject, *files]).lower()
    if any(token in lower for token in ("perf", "性能", "opt", "优化", "fuse", "flash", "kernel", "cuda", "hip", "rocm", "aiter", "deepgemm", "moe", "quant")):
        return "性能/后端优化"
    if any(token in lower for token in ("fix", "bug", "修复", "error", "crash", "vmfault", "wrong", "regression")):
        return "缺陷修复"
    if any(token in lower for token in ("cache", "hicache", "kv", "pd", "scheduler", "prefill", "decode", "disagg")):
        return "调度/缓存/PD"
    if any(token in lower for token in ("support", "add", "新增", "适配", "model", "tokenizer", "parser")):
        return "模型支持/运行时入口"
    if any(token in lower for token in ("test", "ci", "doc", "docs", "benchmark", "bench")):
        return "测试/文档/基准"
    return "通用实现调整"


def commit_matches_files(commit: CommitInfo, selected: set[str]) -> bool:
    return any(path in selected for path in commit.files)


def commit_matches_model_hint(commit: CommitInfo, model: str) -> bool:
    title = MODEL_TITLES.get(model, model)
    candidates = {
        model.lower(),
        model.replace("-", "_").lower(),
        model.replace("-", " ").lower(),
        title.lower(),
        title.replace("/", " ").lower(),
        title.replace("-", " ").lower(),
        title.replace(".", "").lower(),
    }
    filt = MODEL_FILTERS.get(commit_framework_hint(commit), {}).get(model, {})
    for pattern in filt.get("include", []):
        token = pattern.strip("*").replace(".py", "").replace(".mdx", "").lower()
        if len(token) >= 4 and not any(ch in token for ch in "[]{}"):
            candidates.add(token)

    haystack_raw = " ".join([commit.subject, *commit.files]).lower()
    haystacks = {
        haystack_raw,
        haystack_raw.replace("-", "_"),
        haystack_raw.replace("_", "-"),
        haystack_raw.replace("-", " "),
        haystack_raw.replace("_", " "),
    }
    for candidate in candidates:
        candidate = re.sub(r"\s+", " ", candidate).strip()
        if len(candidate) >= 4 and any(candidate in haystack for haystack in haystacks):
            return True
    return False


def commit_framework_hint(commit: CommitInfo) -> str:
    if any(path.startswith(("vllm/", "csrc/", "benchmarks/")) for path in commit.files):
        return "vllm"
    return "sglang"


def model_commits(model: str, files: list[str], commits: list[CommitInfo]) -> list[CommitInfo]:
    selected = set(files)
    matched = [
        commit
        for commit in commits
        if commit_matches_files(commit, selected) or commit_matches_model_hint(commit, model)
    ]
    return matched[:MAX_COMMITS_PER_DOC]


def shared_commits(framework: str, model_to_shas: dict[str, set[str]], commits: list[CommitInfo]) -> list[CommitInfo]:
    model_shas = set().union(*model_to_shas.values()) if model_to_shas else set()
    shared_roots = tuple(
        root
        for root in (
            ".github/",
            ".buildkite/",
            "benchmark",
            "benchmarks",
            "csrc/",
            "docs",
            "examples",
            "python/",
            "scripts/",
            "sgl-kernel/",
            "sglang/",
            "test",
            "tests",
            "tools/",
            "vllm/",
        )
    )
    chosen: list[CommitInfo] = []
    for commit in commits:
        if commit.sha in model_shas:
            continue
        relevant = [path for path in commit.files if path.startswith(shared_roots) or "/" not in path]
        if not relevant:
            continue
        if framework == "vllm" and any(path.startswith("vllm/model_executor/models/") for path in relevant):
            continue
        if framework == "sglang" and any("/models/" in path for path in relevant):
            continue
        chosen.append(commit)
        if len(chosen) >= MAX_COMMITS_PER_DOC:
            break
    return chosen


def changed_files_text(commit: CommitInfo, limit: int = 8) -> str:
    if not commit.files:
        return "未记录文件"
    files = ", ".join(f"`{path}`" for path in commit.files[:limit])
    if len(commit.files) > limit:
        files += f" 等 {len(commit.files)} 个文件"
    return files


def grouped_files(commit: CommitInfo) -> str:
    groups: dict[str, list[str]] = defaultdict(list)
    for path in commit.files:
        groups[file_category(path)].append(f"`{path}`")
    if not groups:
        return "  - 未记录文件"
    lines: list[str] = []
    for category in sorted(groups):
        values = groups[category]
        suffix = "" if len(values) <= 8 else f" 等 {len(values)} 个文件"
        lines.append(f"  - {category}: " + "; ".join(values[:8]) + suffix)
    return "\n".join(lines)


def validation_note_zh(commit: CommitInfo) -> str:
    categories = {file_category(path) for path in commit.files}
    if "runtime-perf" in categories:
        return "涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。"
    if "runtime-model" in categories:
        return "涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。"
    if "tests" in categories:
        return "提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。"
    if "ci" in categories:
        return "主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。"
    return "未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。"


def validation_note_en(commit: CommitInfo) -> str:
    categories = {file_category(path) for path in commit.files}
    if "runtime-perf" in categories:
        return "Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests."
    if "runtime-model" in categories:
        return "Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness."
    if "tests" in categories:
        return "Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke."
    if "ci" in categories:
        return "Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work."
    return "No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check."


def card_zh(commit: CommitInfo) -> str:
    return clean_block(
        f"""\
        ### Commit `{commit.short}` - {commit.subject}

        - 完整 hash: `{commit.sha}`
        - 时间/作者: {commit.date} / {commit.author}
        - 自动分类: {classify_subject(commit.subject, commit.files)}
        - 主要文件: {changed_files_text(commit)}
        - 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
        - 已读文件:
        {grouped_files(commit)}
        - 验证与风险: {validation_note_zh(commit)}
        """
    )


def card_en(commit: CommitInfo) -> str:
    return clean_block(
        f"""\
        ### Commit `{commit.short}` - {commit.subject}

        - Full hash: `{commit.sha}`
        - Date/author: {commit.date} / {commit.author}
        - Auto category: {classify_subject(commit.subject, commit.files)}
        - Main files: {changed_files_text(commit)}
        - Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
        - Reviewed files:
        {grouped_files(commit)}
        - Risk and verification: {validation_note_en(commit)}
        """
    )


def coverage_table(files: list[str], commits: list[CommitInfo], lang: str) -> str:
    header = "| 文件 | 本地提交 |" if lang == "zh" else "| File | Local commits |"
    empty = "当前主线没有匹配到实现文件" if lang == "zh" else "No matching implementation file on current main"
    rows = [header, "| --- | --- |"]
    if not files:
        rows.append(f"| - | {empty} |")
        return "\n".join(rows)
    for path in files[:80]:
        hits = [commit for commit in commits if path in commit.files]
        text = ", ".join(f"`{commit.short}`" for commit in hits[:12])
        if len(hits) > 12:
            text += f", ... ({len(hits)} total)"
        rows.append(f"| `{path}` | {text or ('无直接提交' if lang == 'zh' else 'no direct commit')} |")
    if len(files) > 80:
        rows.append(f"| ... | {len(files) - 80} more files omitted from table; all were used for git tracing. |")
    return "\n".join(rows)


def timeline(commits: list[CommitInfo], lang: str) -> str:
    if lang == "zh":
        rows = ["| 日期 | Commit | 分类 | 标题 | 主要文件 |", "| --- | --- | --- | --- | --- |"]
    else:
        rows = ["| Date | Commit | Category | Title | Main files |", "| --- | --- | --- | --- | --- |"]
    if not commits:
        rows.append("| - | - | - | no local commit found | - |")
        return "\n".join(rows)
    for commit in commits:
        files = ", ".join(f"`{path}`" for path in commit.files[:3])
        rows.append(
            f"| {commit.date} | `{commit.short}` | {classify_subject(commit.subject, commit.files)} | {md_escape(commit.subject)} | {md_escape(files)} |"
        )
    return "\n".join(rows)


def render_zh(framework: str, model: str, files: list[str], commits: list[CommitInfo]) -> str:
    title = LOCAL_MODEL_TITLES[model]
    cards = "\n\n".join(card_zh(commit) for commit in commits)
    if not cards:
        cards = "### 本地提交检索结论\n\n- 未确认到可归入该模型桶的本地提交；如果后续出现实现文件或提交，需要重新生成本地历史。"
    filter_note = ""
    if framework == "sglang" and not SGLANG_DISABLE_OFFICIAL_FILTER:
        filter_note = "\n- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。"
    body = clean_block(
        f"""\
        # {framework} {title} 本地提交优化历史

        ## 模型实现文件覆盖

        {coverage_table(files, commits, "zh")}

        ## 本地提交覆盖总览

        - 来源工作树: `{WORKTREE_LABELS[framework]}`
        - 生成日期: {TODAY}
        - 文档提交数: {len(commits)}
        - 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
        - 追溯命令: `git log --name-only`{filter_note}

        ## 时间线

        {timeline(commits, "zh")}

        ## 逐 Commit 审计卡

        {cards}
        """
    )
    return body.strip() + "\n"


def render_en(framework: str, model: str, files: list[str], commits: list[CommitInfo]) -> str:
    title = LOCAL_MODEL_TITLES[model]
    cards = "\n\n".join(card_en(commit) for commit in commits)
    if not cards:
        cards = "### Local commit search conclusion\n\n- No local commit was confirmed for this model bucket; regenerate local history when implementation files or commits appear."
    filter_note = ""
    if framework == "sglang" and not SGLANG_DISABLE_OFFICIAL_FILTER:
        filter_note = "\n- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits."
    body = clean_block(
        f"""\
        # {framework} {title} Local Commit Optimization History

        ## Implementation File Coverage

        {coverage_table(files, commits, "en")}

        ## Local Commit Coverage Summary

        - Source worktree: `{WORKTREE_LABELS[framework]}`
        - Generated date: {TODAY}
        - Commits in this document: {len(commits)}
        - Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
        - Trace command: `git log --name-only`{filter_note}

        ## Timeline

        {timeline(commits, "en")}

        ## Per-Commit Audit Cards

        {cards}
        """
    )
    return body.strip() + "\n"


def write_indexes() -> None:
    model_lines = "\n".join(f"- `{model}`" for model in MODEL_ORDER)
    for framework, title in (("sglang", "SGLang"), ("vllm", "vLLM")):
        filter_policy = ""
        if framework == "sglang" and not SGLANG_DISABLE_OFFICIAL_FILTER:
            filter_policy = (
                "\nFilter policy:\n\n"
                "- SGLang bucket docs keep only local fork commits that are not "
                "reachable from local `refs/remotes/github-official/*`, fetched "
                "from `sgl-project/sglang`.\n"
                "- Buckets with no remaining local-only commits keep an explicit "
                "empty result row instead of preserving GitHub upstream commits.\n"
            )
        path = HISTORY_ROOT / framework / "README.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"# {title} Local Commit Optimization History\n{filter_policy}\nCurrent buckets:\n\n{model_lines}\n",
            encoding="utf-8",
        )


def rebuild(dry_run: bool = False, frameworks: tuple[str, ...] = ("sglang", "vllm")) -> None:
    if not dry_run:
        HISTORY_ROOT.mkdir(parents=True, exist_ok=True)
    official_by_framework = {
        "sglang": official_sglang_commits() if "sglang" in frameworks else set(),
        "vllm": set(),
    }
    if not dry_run:
        write_indexes()
    for framework in frameworks:
        all_files = git_files(framework)
        commits = filter_local_only_commits(
            framework,
            parse_commits(framework),
            official_by_framework[framework],
        )
        model_to_commits: dict[str, list[CommitInfo]] = {}
        model_to_shas: dict[str, set[str]] = {}
        for model in [m for m in MODEL_ORDER if m != SHARED_BUCKET]:
            files = selected_files(framework, model, all_files)
            chosen = model_commits(model, files, commits)
            model_to_commits[model] = chosen
            model_to_shas[model] = {commit.sha for commit in chosen}
            if dry_run:
                print(f"{framework}/{model}: files={len(files)} commits={len(chosen)}")
                continue
            out_dir = HISTORY_ROOT / framework / model
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "README.zh.md").write_text(render_zh(framework, model, files, chosen), encoding="utf-8")
            (out_dir / "README.en.md").write_text(render_en(framework, model, files, chosen), encoding="utf-8")

        shared_files = shared_bucket_files(framework, all_files)
        shared = shared_commits(framework, model_to_shas, commits)
        if dry_run:
            print(f"{framework}/{SHARED_BUCKET}: files={len(shared_files)} commits={len(shared)}")
            continue
        out_dir = HISTORY_ROOT / framework / SHARED_BUCKET
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "README.zh.md").write_text(render_zh(framework, SHARED_BUCKET, shared_files, shared), encoding="utf-8")
        (out_dir / "README.en.md").write_text(render_en(framework, SHARED_BUCKET, shared_files, shared), encoding="utf-8")


def main() -> int:
    global SGLANG_DISABLE_OFFICIAL_FILTER
    global SGLANG_OFFICIAL_REF_PREFIX
    global SGLANG_REQUIRE_OFFICIAL_FILTER

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--framework",
        action="append",
        choices=("sglang", "vllm"),
        help=(
            "Only rebuild the given framework; repeat for both. Defaults to all. "
            "Use this when one local worktree is not a complete clone, so its "
            "docs are not overwritten with partial history."
        ),
    )
    parser.add_argument(
        "--sglang-official-ref-prefix",
        default=SGLANG_OFFICIAL_REF_PREFIX,
        help=(
            "Local ref prefix containing fetched sgl-project/sglang refs. "
            "Used to filter upstream GitHub commits out of SGLang hg-history."
        ),
    )
    parser.add_argument(
        "--allow-missing-sglang-official-filter",
        action="store_true",
        help=(
            "Do not fail when official SGLang refs are missing. This is only "
            "for diagnostics; normal SGLang history regeneration should fail closed."
        ),
    )
    parser.add_argument(
        "--disable-sglang-official-filter",
        action="store_true",
        help=(
            "Disable SGLang official GitHub filtering. This should not be used "
            "for committed model-pr-optimization-hg-history updates."
        ),
    )
    args = parser.parse_args()
    SGLANG_OFFICIAL_REF_PREFIX = args.sglang_official_ref_prefix
    SGLANG_REQUIRE_OFFICIAL_FILTER = not args.allow_missing_sglang_official_filter
    SGLANG_DISABLE_OFFICIAL_FILTER = args.disable_sglang_official_filter
    frameworks = tuple(args.framework) if args.framework else ("sglang", "vllm")
    missing = [str(FRAMEWORK_ROOTS[name]) for name in frameworks if not FRAMEWORK_ROOTS[name].exists()]
    if missing:
        raise SystemExit(f"missing local framework worktrees: {', '.join(missing)}")
    rebuild(dry_run=args.dry_run, frameworks=frameworks)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
