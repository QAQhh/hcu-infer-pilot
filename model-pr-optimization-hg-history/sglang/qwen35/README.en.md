# sglang Qwen3.5 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/qwen3_5.py` | `94a624b83` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 6
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-05-07 | `9f67deca2` | 性能/后端优化 | 支持qwen3.5-awq模型 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py` |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `94a624b83` | 性能/后端优化 | 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-09 | `b8cd509f4` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-04-02 | `28dec61dd` | 模型支持/运行时入口 | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |

## Per-Commit Audit Cards

### Commit `9f67deca2` - 支持qwen3.5-awq模型

- Full hash: `9f67deca24b100410fe69d142a4ebca4fe26cc34`
- Date/author: 2026-05-07 / maxiao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py`, `python/sglang/srt/utils/common.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/moe_wna16.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c1d308c60` - 修复qwen3.5-397b-fp8报错问题

- Full hash: `c1d308c602379d71d746bc50ed785c2bee05ba99`
- Date/author: 2026-04-29 / liucong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/index.py`; `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `32bd2422e` - 修复qwen3.5模型memory_Async问题

- Full hash: `32bd2422e7d17f0cee10413aad4a223ffb25dd74`
- Date/author: 2026-04-23 / liucong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/sampling/sampling_batch_info.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/sampling/sampling_batch_info.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `94a624b83` - 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子

- Full hash: `94a624b8364de497a4a7ee4a6f9def06e18d90c9`
- Date/author: 2026-04-23 / liucong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_5.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b8cd509f4` - [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能

- Full hash: `b8cd509f45f9a51adee404eb9104358653e869d1`
- Date/author: 2026-04-09 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `28dec61dd` - support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k

- Full hash: `28dec61dd674f482fe34b5251ff0cd050ca2184c`
- Date/author: 2026-04-02 / liucong
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## Local-only dev branch update from v0.5.8_dev to v0.5.12_dev

### Coverage Note

- Source index: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- Source worktree: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs.
- Commits in this section: 4
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-04-02 | `44081352b` | `v0.5.9_dev..v0.5.10_dev` | 调度/缓存/PD | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |
| 2026-04-09 | `f6730ce49` | `v0.5.9_dev..v0.5.10_dev` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-05-09 | `fe8d278ca` | `v0.5.10_dev..v0.5.11_dev` | 缺陷修复 | debugging qwen3.5 model | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 6 个文件 |
| 2026-05-18 | `43efcafdc` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix init error when use qwen 3.5 | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 7 个文件 |

### Per-Commit Audit Cards

#### Commit `44081352b` - support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k

- Full hash: `44081352b950ed172c2d04b776db732a49f2f9b4`
- Date/author: 2026-04-02 / liucong
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
- Risk and verification: Touches scheduling, cache, PD, or MTP paths; verify prefill/decode ordering, first-token correctness, concurrency, and long-context stability.

#### Commit `f6730ce49` - [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能

- Full hash: `f6730ce492512fded4d0c8a7c751303c39cce828`
- Date/author: 2026-04-09 / chenyue3
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate with prefill/decode traces, end-to-end throughput, and correctness smoke tests before reusing.

#### Commit `fe8d278ca` - debugging qwen3.5 model

- Full hash: `fe8d278ca9cb6dc45627610fe18b831cecae5ab9`
- Date/author: 2026-05-09 / lizhigong
- Branch update: `v0.5.10_dev..v0.5.11_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/moe_align_block_size.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/linear.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/moe_align_block_size.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `43efcafdc` - fix init error when use qwen 3.5

- Full hash: `43efcafdcda164d8d40a15c624b301c82528833a`
- Date/author: 2026-05-18 / lizhigong
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
  - other: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/model_executor/forward_batch_info.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
