#!/usr/bin/env python3
"""Append branch-segment local-only commit blocks to model-pr-optimization-hg-history.

`rebuild_model_pr_hg_history_from_local_git.py` rewrites every bucket from the
tip of one worktree and keeps at most 80 commits per document. This helper
instead adds one marker-delimited block per bucket for explicit branch
segments such as `v0.5.12_dev..v0.5.15.post1_dev`, and leaves the existing
text untouched, so cards generated earlier from other worktrees survive.
Re-running replaces only its own block.

Only commits that are not reachable from the fetched `sgl-project/sglang`
refs are kept. Missing official refs are a hard error, as in the generator.
It reads commit metadata only (`git log --no-renames --name-only`), so it
works on a blobless clone without network access.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from rebuild_model_pr_hg_history_from_local_git import (
    LOCAL_MODEL_TITLES,
    changed_files_text,
    classify_subject,
    grouped_files,
    validation_note_en,
    validation_note_zh,
)
from rebuild_model_pr_history_from_git import (
    MODEL_FILTERS,
    MODEL_ORDER,
    SHARED_BUCKET,
    matches_any,
    md_escape,
)


ROOT = Path(__file__).resolve().parents[1]
UNCLASSIFIED = "unclassified"
SHARED_ROOTS = (
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
)
FILE_TABLE_LIMIT = 40
MAX_CARDS = 80
# Squash syncs of official main and repo-wide renames touch thousands of files and
# would land in every model bucket; the largest genuine model commit here has 140.
BULK_FILE_THRESHOLD = 150
EXTRA_BUCKET = "qwen4-exp"
LOCAL_MODEL_TITLES[EXTRA_BUCKET] = "Qwen4-Exp (Qwen3.8-Flash-Next)"
BUCKETS = [*(model for model in MODEL_ORDER if model != SHARED_BUCKET), EXTRA_BUCKET, SHARED_BUCKET]
# Names the base filter table predates: extra file globs and word-boundary subject hints.
EXTRA_INCLUDE = {
    "deepseek-v4": ["*/dsv4/*", "*dsv4*"],
    "hunyuan3-preview": ["*hunyuan_v3*"],
    EXTRA_BUCKET: ["*qwen4*"],
}
WORD_HINTS = {
    "deepseek-v4": [r"\bdsv4\b"],
    "glm5-glm51": [r"\bglm[ -]?5"],
    "hunyuan3-preview": [r"\bhy3\b"],
    "kimi": [r"\bk3\b"],
    EXTRA_BUCKET: [r"qwen4"],
}
MERGE_NOTE = {"zh": "无直接文件变更/merge", "en": "no direct file change / merge"}


@dataclass
class Commit:
    sha: str
    date: str
    author: str
    subject: str
    segment: str
    is_merge: bool
    files: list[str] = field(default_factory=list)

    @property
    def short(self) -> str:
        return self.sha[:9]


def run_git(repo: Path, *args: str) -> str:
    env = {**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_TERMINAL_PROMPT": "0"}
    proc = subprocess.run(
        ["git", "-c", f"safe.directory={repo}", *args],
        cwd=repo,
        env=env,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{proc.stderr}")
    return proc.stdout


def require_official_refs(repo: Path, prefix: str) -> None:
    refs = run_git(repo, "for-each-ref", "--format=%(refname)", prefix).split()
    if not refs:
        raise SystemExit(
            f"missing official SGLang refs under {prefix}. Fetch them first: "
            "git fetch https://github.com/sgl-project/sglang.git "
            "'+refs/heads/*:refs/remotes/github-official/*'"
        )


def segment_commits(
    repo: Path, *, base: str, head: str, ref_prefix: str, official_prefix: str
) -> tuple[list[Commit], int]:
    label = f"{base}..{head}"
    fmt = "\x02%H\x01%ad\x01%an\x01%P\x01%s"
    span = f"{ref_prefix}/{base}..{ref_prefix}/{head}"
    in_range = int(run_git(repo, "rev-list", "--count", span).strip())
    out = run_git(
        repo, "log", "--no-renames", "--name-only", "--date=short", f"--format={fmt}",
        span, "--not", f"--glob={official_prefix}/*",
    )
    commits: list[Commit] = []
    for line in out.splitlines():
        if line.startswith("\x02"):
            sha, when, author, parents, subject = line[1:].split("\x01", 4)
            commits.append(Commit(sha, when, author, subject, label, len(parents.split()) > 1))
        elif line.strip() and commits:
            commits[-1].files.append(line.strip())
    commits.reverse()
    commits.sort(key=lambda commit: commit.date)
    return commits, in_range


def name_hints(model: str) -> set[str]:
    title = LOCAL_MODEL_TITLES.get(model, model).lower()
    include = MODEL_FILTERS["sglang"].get(model, {}).get("include", [])
    hints = {
        model.lower(),
        model.replace("-", "_").lower(),
        model.replace("-", " ").lower(),
        title,
        title.replace("/", " "),
        title.replace("-", " "),
        title.replace(".", ""),
    }
    for pattern in include:
        token = pattern.strip("*").replace(".py", "").replace(".mdx", "").lower()
        if len(token) >= 4 and not any(ch in token for ch in "[]{}"):
            hints.add(token)
    return {re.sub(r"\s+", " ", hint).strip() for hint in hints if len(hint) >= 4}


def matching_models(commit: Commit, hints: dict[str, set[str]]) -> list[str]:
    subject = commit.subject.lower()
    subject_variants = {subject, subject.replace("-", "_"), subject.replace("_", "-"), subject.replace("-", " "), subject.replace("_", " ")}
    models = []
    for model in BUCKETS:
        if model == SHARED_BUCKET:
            continue
        filt = MODEL_FILTERS["sglang"].get(model, {})
        include = [*filt.get("include", []), *EXTRA_INCLUDE.get(model, [])]
        exclude = filt.get("exclude", [])
        by_file = any(matches_any(path, include) and not matches_any(path, exclude) for path in commit.files)
        by_name = any(hint in text for hint in hints[model] for text in subject_variants)
        by_word = any(re.search(pattern, subject) for pattern in WORD_HINTS.get(model, []))
        if by_file or by_name or by_word:
            models.append(model)
    return models


def assign_buckets(commits: list[Commit]) -> dict[str, list[Commit]]:
    hints = {model: name_hints(model) for model in BUCKETS if model != SHARED_BUCKET}
    buckets: dict[str, list[Commit]] = {model: [] for model in BUCKETS}
    buckets[UNCLASSIFIED] = []
    for commit in commits:
        if len(commit.files) > BULK_FILE_THRESHOLD:
            buckets[UNCLASSIFIED].append(commit)
            continue
        models = matching_models(commit, hints)
        for model in models:
            buckets[model].append(commit)
        if models:
            continue
        relevant = any(path.startswith(SHARED_ROOTS) or "/" not in path for path in commit.files)
        buckets[SHARED_BUCKET if relevant else UNCLASSIFIED].append(commit)
    return buckets


LABELS = {
    "zh": {
        "heading": "## {a} 到 {b} 本地独有提交补充",
        "coverage": "### 覆盖说明",
        "repo": "- 来源仓库: `{repo}`；分支端点: {tips}",
        "scope": "- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。",
        "date": "- 生成日期: {today}",
        "count": "- 本章节提交数: {n}（其中 merge {merges}）",
        "segments": "- 分支更新段: {segments}",
        "note": "- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。",
        "files": "### 涉及文件",
        "files_cols": ["| 文件 | 本地提交 |", "| --- | --- |"],
        "files_more": "| ... | 另有 {n} 个文件未列出 |",
        "timeline": "### 时间线",
        "timeline_cols": ["| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |", "| --- | --- | --- | --- | --- | --- |"],
        "cards": "### 逐 Commit 审计卡",
        "cards_cap": "- 时间线列出全部 {total} 个提交；审计卡只保留最近的 {shown} 个。",
        "empty": "- 该分支更新段内没有归入本桶的本地独有提交。",
        "full": "- 完整 hash: `{sha}`",
        "who": "- 时间/作者: {date} / {author}",
        "seg": "- 分支更新段: `{segment}`",
        "category": "- 自动分类: {category}",
        "main": "- 主要文件: {files}",
        "signal": "- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。",
        "touched": "- 涉及文件（按路径分组，未逐文件阅读）:",
        "risk": "- 验证与风险: {note}",
        "merge_risk": "合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。",
        "more_files": " 等 {n} 个文件",
    },
    "en": {
        "heading": "## Local-only branch update from {a} to {b}",
        "coverage": "### Coverage Note",
        "repo": "- Source repository: `{repo}`; branch tips: {tips}",
        "scope": "- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.",
        "date": "- Generated date: {today}",
        "count": "- Commits in this section: {n} (merges: {merges})",
        "segments": "- Branch segments: {segments}",
        "note": "- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.",
        "files": "### Touched Files",
        "files_cols": ["| File | Local commits |", "| --- | --- |"],
        "files_more": "| ... | {n} more files omitted |",
        "timeline": "### Timeline",
        "timeline_cols": ["| Date | Commit | Branch update | Category | Title | Main files |", "| --- | --- | --- | --- | --- | --- |"],
        "cards": "### Per-Commit Audit Cards",
        "cards_cap": "- The timeline lists all {total} commits; audit cards cover only the most recent {shown}.",
        "empty": "- No local-only commit in these branch segments belongs to this bucket.",
        "full": "- Full hash: `{sha}`",
        "who": "- Date/author: {date} / {author}",
        "seg": "- Branch update: `{segment}`",
        "category": "- Auto category: {category}",
        "main": "- Main files: {files}",
        "signal": "- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.",
        "touched": "- Touched files (grouped by path, not read file by file):",
        "risk": "- Risk and verification: {note}",
        "merge_risk": "A merge commit has no direct file diff; the substance is in the commits it brings in.",
        "more_files": " and {n} files in total",
    },
}


def main_files(commit: Commit, lang: str) -> str:
    if commit.is_merge and not commit.files:
        return MERGE_NOTE[lang]
    first = ", ".join(f"`{path}`" for path in commit.files[:3])
    return first + (LABELS[lang]["more_files"].format(n=len(commit.files)) if len(commit.files) > 3 else "")


def card(commit: Commit, lang: str) -> str:
    text = LABELS[lang]
    note_fn = validation_note_zh if lang == "zh" else validation_note_en
    files = MERGE_NOTE[lang] if commit.is_merge and not commit.files else changed_files_text(commit)
    risk = text["merge_risk"] if commit.is_merge and not commit.files else note_fn(commit)
    lines = [
        f"#### Commit `{commit.short}` - {commit.subject}",
        "",
        text["full"].format(sha=commit.sha),
        text["who"].format(date=commit.date, author=commit.author),
        text["seg"].format(segment=commit.segment),
        text["category"].format(category=classify_subject(commit.subject, commit.files)),
        text["main"].format(files=files),
        text["signal"],
    ]
    if commit.files:
        lines += [text["touched"], grouped_files(commit)]
    lines.append(text["risk"].format(note=risk))
    return "\n".join(lines)


def files_table(commits: list[Commit], lang: str) -> list[str]:
    text = LABELS[lang]
    hits: dict[str, list[str]] = defaultdict(list)
    for commit in commits:
        for path in commit.files:
            hits[path].append(commit.short)
    ranked = sorted(hits.items(), key=lambda item: (-len(item[1]), item[0]))
    rows = list(text["files_cols"])
    for path, shorts in ranked[:FILE_TABLE_LIMIT]:
        shown = ", ".join(f"`{short}`" for short in shorts[:12])
        rows.append(f"| `{path}` | {shown}" + (f", ... ({len(shorts)} total)" if len(shorts) > 12 else "") + " |")
    if len(ranked) > FILE_TABLE_LIMIT:
        rows.append(text["files_more"].format(n=len(ranked) - FILE_TABLE_LIMIT))
    return rows


def render_block(lang: str, *, key: str, a: str, b: str, repo_label: str, tips: str, today: str, segments: list[str], commits: list[Commit]) -> str:
    text = LABELS[lang]
    merges = sum(commit.is_merge for commit in commits)
    lines = [
        f"<!-- {key}_START -->",
        text["heading"].format(a=a, b=b),
        "",
        text["coverage"],
        "",
        text["repo"].format(repo=repo_label, tips=tips),
        text["scope"],
        text["date"].format(today=today),
        text["count"].format(n=len(commits), merges=merges),
        text["segments"].format(segments=", ".join(f"`{seg}`" for seg in segments)),
        text["note"],
        "",
    ]
    if not commits:
        lines += [text["empty"]]
    else:
        lines += [text["files"], "", *files_table(commits, lang), "", text["timeline"], "", *text["timeline_cols"]]
        for commit in commits:
            lines.append(
                f"| {commit.date} | `{commit.short}` | `{commit.segment}` | {classify_subject(commit.subject, commit.files)} "
                f"| {md_escape(commit.subject)} | {md_escape(main_files(commit, lang))} |"
            )
        carded = commits[-MAX_CARDS:]
        lines += ["", text["cards"], ""]
        if len(carded) < len(commits):
            lines += [text["cards_cap"].format(shown=len(carded), total=len(commits)), ""]
        lines.append("\n\n".join(card(commit, lang) for commit in carded))
    lines += ["", f"<!-- {key}_END -->"]
    return "\n".join(lines)


def upsert_block(path: Path, key: str, block: str) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n") if path.exists() else ""
    pattern = re.compile(rf"<!-- {re.escape(key)}_START -->.*?<!-- {re.escape(key)}_END -->", re.S)
    if pattern.search(text):
        text = pattern.sub(lambda _: block, text)
        action = "replaced"
    else:
        text = text.rstrip("\n") + ("\n\n" if text.strip() else "") + block
        action = "appended"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    return action


def write_buckets(history_root: Path, key: str, buckets: dict[str, list[Commit]], **kwargs: object) -> None:
    for bucket, commits in buckets.items():
        for lang in ("zh", "en"):
            path = history_root / "sglang" / bucket / f"README.{lang}.md"
            if not path.exists():
                title = LOCAL_MODEL_TITLES.get(bucket, bucket)
                header = f"# sglang {title} 本地提交优化历史" if lang == "zh" else f"# sglang {title} Local Commit Optimization History"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(header + "\n", encoding="utf-8", newline="\n")
            block = render_block(lang, key=key, commits=commits, **kwargs)
            upsert_block(path, key, block)


def duplicate_groups(commits: list[Commit]) -> list[list[Commit]]:
    groups: dict[tuple[str, tuple[str, ...]], list[Commit]] = defaultdict(list)
    for commit in commits:
        if not commit.is_merge and commit.files:
            groups[(commit.subject, tuple(sorted(commit.files)))].append(commit)
    return [group for group in groups.values() if len(group) > 1]


def write_index(
    path: Path, *, a: str, b: str, repo_label: str, tips: str, today: str, segments: list[str],
    in_range: dict[str, int], commits: list[Commit], buckets: dict[str, list[Commit]],
) -> None:
    by_segment = {seg: [c for c in commits if c.segment == seg] for seg in segments}
    lines = [
        f"# SGLang {a}..{b} 分支更新本地独有提交索引",
        "",
        "## 范围与口径",
        "",
        f"- 来源仓库: `{repo_label}`；分支端点: {tips}",
        "- 官方仓库: `https://github.com/sgl-project/sglang.git`",
        "- 官方 refs: 已 fetch 到本地 `refs/remotes/github-official/*`",
        "- 筛选方法: 每个分支更新段内，commit hash 不可从官方 GitHub refs 到达，即记录为本地 fork 独有提交。",
        "- 说明: 合并提交也保留；合并提交没有直接文件 diff 时，`主要涉及` 标记为 `无直接文件变更/merge`。",
        f"- 生成日期: {today}",
        "",
        "## 数量汇总",
        "",
        "| 分支更新段 | 范围内提交数 | 本地独有提交数 | 其中 merge |",
        "| --- | ---: | ---: | ---: |",
    ]
    for seg in segments:
        items = by_segment[seg]
        lines.append(f"| `{seg}` | {in_range[seg]} | {len(items)} | {sum(c.is_merge for c in items)} |")
    lines.append(f"| 合计 | {sum(in_range.values())} | {len(commits)} | {sum(c.is_merge for c in commits)} |")
    lines += ["", "## 分桶分布", "", "| 桶 | 提交数 |", "| --- | ---: |"]
    lines += [f"| `{bucket}` | {len(items)} |" for bucket, items in buckets.items() if items]
    lines += ["", "- 同一提交可同时进入多个模型桶，所以各桶之和大于本地独有提交总数。"]
    dups = duplicate_groups(commits)
    lines += ["", "## 重复检查", "", "- 本次未计算 `git patch-id`（克隆不含文件内容）；仅按「标题相同且文件集相同」检查疑似重复。"]
    if dups:
        for group in dups:
            lines.append(f"- 疑似重复: {', '.join(f'`{c.short}`' for c in group)}，标题 `{md_escape(group[0].subject)}`。索引中均保留。")
    else:
        lines.append("- 未发现标题与文件集都相同的提交。")
    lines += ["", "## 提交索引"]
    models_of = defaultdict(list)
    for bucket, items in buckets.items():
        for commit in items:
            models_of[commit.sha].append(bucket)
    for seg in segments:
        lines += ["", f"### `{seg}`", "", "| 日期 | Commit | 作者 | 概要 | 主要涉及 | 归入的桶 |", "| --- | --- | --- | --- | --- | --- |"]
        for commit in by_segment[seg]:
            lines.append(
                f"| {commit.date} | `{commit.short}` | {md_escape(commit.author)} | {md_escape(commit.subject)} "
                f"| {md_escape(main_files(commit, 'zh'))} | {', '.join(models_of[commit.sha])} |"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def print_dry_run(buckets: dict[str, list[Commit]], commits: list[Commit]) -> None:
    print(f"local-only commits: {len(commits)} (merges {sum(c.is_merge for c in commits)})")
    for bucket, items in buckets.items():
        print(f"  {bucket}: {len(items)}")
    placed = {c.sha for items in buckets.values() for c in items}
    print(f"placed in at least one bucket: {len(placed)} / {len(commits)}")
    for name in (SHARED_BUCKET, UNCLASSIFIED):
        print(f"--- {name} samples")
        for commit in buckets[name][:60]:
            print(f"  {commit.short} {commit.date} {commit.subject[:90]}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, type=Path, help="sglang-das git repository with fetched branches and official refs")
    parser.add_argument("--history-root", type=Path, default=ROOT / "model-pr-optimization-hg-history")
    parser.add_argument("--ref-prefix", default="refs/remotes/origin")
    parser.add_argument("--official-ref-prefix", default="refs/remotes/github-official")
    parser.add_argument("--segment", action="append", required=True, help="BASE..HEAD branch names under --ref-prefix; repeat in order")
    parser.add_argument("--repo-label", default="HYGON-AI/sglang-das")
    parser.add_argument("--block-key", default="LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18")
    parser.add_argument("--index-name", default="LOCAL_ONLY_COMMITS_v0.5.12_dev_to_v0.5.18_by_branch.md")
    parser.add_argument("--today", default=date.today().isoformat())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo = args.repo.resolve()
    require_official_refs(repo, args.official_ref_prefix)
    pairs = [tuple(seg.split("..", 1)) for seg in args.segment]
    commits: list[Commit] = []
    in_range: dict[str, int] = {}
    seen: set[str] = set()
    for base, head in pairs:
        items, total = segment_commits(
            repo, base=base, head=head, ref_prefix=args.ref_prefix, official_prefix=args.official_ref_prefix
        )
        in_range[f"{base}..{head}"] = total
        fresh = [commit for commit in items if commit.sha not in seen]
        seen.update(commit.sha for commit in fresh)
        commits.extend(fresh)
    buckets = assign_buckets(commits)
    print_dry_run(buckets, commits)
    if args.dry_run:
        return 0

    a, b = pairs[0][0], pairs[-1][1]
    tips = ", ".join(
        f"`{name}`@`{run_git(repo, 'rev-parse', '--short=9', f'{args.ref_prefix}/{name}').strip()}`"
        for name in dict.fromkeys(name for pair in pairs for name in pair)
    )
    shared = dict(a=a, b=b, repo_label=args.repo_label, tips=tips, today=args.today)
    write_buckets(args.history_root, args.block_key, buckets, segments=list(in_range), **shared)
    index_path = args.history_root / "sglang" / args.index_name
    write_index(
        index_path, a=a, b=b, repo_label=args.repo_label, tips=tips, today=args.today,
        segments=list(in_range), in_range=in_range, commits=commits, buckets=buckets,
    )
    print(f"wrote {len(buckets) * 2} bucket blocks and {index_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
