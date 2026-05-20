# sglang Intern-S1 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/function_call/internlm_detector.py` | no direct commit |
| `python/sglang/srt/models/interns1.py` | no direct commit |
| `python/sglang/srt/models/interns1pro.py` | `3e7ecb78a` |
| `python/sglang/srt/multimodal/processors/interns1pro.py` | `3e7ecb78a` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 2
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-05 | `3e7ecb78a` | 性能/后端优化 | model: support interns1-pro (#18145) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/interns1pro.py` |
| 2026-01-26 | `539924037` | 缺陷修复 | fix(processor): support InternS1 text_config in InternVL processor (#17040) | `python/sglang/srt/multimodal/processors/internvl.py` |

## Per-Commit Audit Cards

### Commit `3e7ecb78a` - model: support interns1-pro (#18145)

- Full hash: `3e7ecb78a60f8e1d889cfe25c88006577783d903`
- Date/author: 2026-02-05 / RunningLeon
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/interns1pro.py`, `python/sglang/srt/models/qwen3_vl_moe.py`, `python/sglang/srt/multimodal/processors/interns1pro.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/multimodal/processors/interns1pro.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/interns1pro.py`
  - runtime-perf: `python/sglang/srt/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `539924037` - fix(processor): support InternS1 text_config in InternVL processor (#17040)

- Full hash: `539924037fbc6b64a75c554ed338cb8c5abe5343`
- Date/author: 2026-01-26 / Mahdi-CV
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/multimodal/processors/internvl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.
