# Model PR Optimization History

This directory stores open-source community PR-driven model optimization
histories by serving framework. These records are documentation, not installable
per-model skills: the directory acts as one queryable knowledge base for
model-family PR evidence. The sibling `model-pr-optimization-hg-history` tree
stores local `sglang` and `vllm` worktree commit history; profiler-linked
lookups should check both trees.

- `sglang/`: SGLang model histories, audits, and a `shared/` fallback bucket for framework-wide PRs.
- `vllm/`: vLLM model histories, audits, and a `shared/` fallback bucket for framework-wide PRs.
- `SKILL.md`: agent instructions for using this directory as knowledge.
- `scripts/query.py`: small local search helper for model slugs, doc paths, and
  keyword snippets.

Each model history is bilingual when practical (`README.zh.md` and
`README.en.md`) and should be grounded in inspected PR diffs, source files, and
validation/risk notes.

PRs that cannot be safely anchored to a single model family should go into the
framework `shared/` bucket instead of being dropped. That bucket is for
framework-wide runtime, parser, CI, or utility changes that still matter for
profiling and optimization work.

Quick queries:

```bash
python3 scripts/query.py --list
python3 scripts/query.py --framework sglang --model qwen3-core --paths-only
python3 scripts/query.py --framework vllm "qwen3 fused qk norm"
```

SGLang SOTA and Humanize loops should read the matching SGLang community PR
history before patch planning, read vLLM community PR history when vLLM is the
leading competitor, also check `model-pr-optimization-hg-history` for local fork
commits, and save the short extracted evidence under
`history/model-pr-history-notes.md`.
