# sglang Step 3.5 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/configs/step3p5.py` | `980d2936c` |
| `python/sglang/srt/models/step3p5.py` | `980d2936c` |
| `python/sglang/srt/models/step3p5_mtp.py` | `980d2936c` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 2
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-04 | `562c3ff2d` | 性能/后端优化 | [Feature] implement the standard multi-layer MTP for step3p5 (#18564) | `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-02-03 | `980d2936c` | 性能/后端优化 | model: support Step-3.5-Flash (#18084) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py` |

## Per-Commit Audit Cards

### Commit `562c3ff2d` - [Feature]  implement the standard multi-layer MTP for step3p5 (#18564)

- Full hash: `562c3ff2d0e40420869138495397dc3d5f5edd6f`
- Date/author: 2026-03-04 / qwe
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `980d2936c` - model: support Step-3.5-Flash (#18084)

- Full hash: `980d2936cd9a94a6346fb678a8134d5776fdf996`
- Date/author: 2026-02-03 / Yuhao Yang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py`, `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_loader/loader.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/function_call/function_call_parser.py`; `python/sglang/srt/model_loader/loader.py`; `python/sglang/srt/parser/reasoning_parser.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/step3p5.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/step3p5.py`; `python/sglang/srt/models/step3p5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/models/mimo_v2_flash_nextn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
