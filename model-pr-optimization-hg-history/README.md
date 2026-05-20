# Model Optimization Local Commit History

This directory stores local framework commit histories by serving framework.
These records are documentation, not installable per-model skills: the
directory acts as one queryable knowledge base for model-family evidence from
the local `/public/home/yangyn1/work_space/2026/minmax/skills/sglang` and
`/public/home/yangyn1/work_space/2026/minmax/skills/vllm` worktrees. It is
checked by `llm-torch-profiler-analysis` together with the open-source
community PR history in `model-pr-optimization-history` when looking for prior
kernel, overlap, or fusion ideas.

- `sglang/`: local SGLang model histories, audits, and a `shared/` fallback bucket for framework-wide commits.
- `vllm/`: local vLLM model histories, audits, and a `shared/` fallback bucket for framework-wide commits.
- `SKILL.md`: agent instructions for using this directory as knowledge.
- `scripts/query.py`: small local search helper for model slugs, doc paths, and
  keyword snippets.

Each model history is bilingual when practical (`README.zh.md` and
`README.en.md`) and should be grounded in local git commits, source files, and
validation/risk notes.

Commits that cannot be safely anchored to a single model family should go into
the framework `shared/` bucket instead of being dropped. That bucket is for
framework-wide runtime, parser, CI, cache, kernel, scheduler, or utility changes
that still matter for profiling and optimization work.

Quick queries:

```bash
python3 scripts/query.py --list
python3 scripts/query.py --framework sglang --model qwen3-core --paths-only
python3 scripts/query.py --framework vllm "qwen3 fused qk norm"
```

SGLang SOTA and Humanize loops should read the matching local SGLang history
before patch planning, read local vLLM history when vLLM is the leading
competitor, also check `model-pr-optimization-history` for community PR
precedents, and save the short extracted evidence under
`history/model-pr-history-notes.md`.
