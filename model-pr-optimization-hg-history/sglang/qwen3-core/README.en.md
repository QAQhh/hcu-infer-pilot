# sglang Qwen3 Core Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/qwen3.py` | `b63cd7645`, `e9d6aefa9` |
| `python/sglang/srt/models/qwen3_moe.py` | `466a1d6a4`, `e9d6aefa9` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 9
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
| 2026-04-21 | `466a1d6a4` | 性能/后端优化 | 将qwen3_moe文件中的SGLANG_USE_FUSED_BAILING_RMS_ROTARY修改为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-04-09 | `b8cd509f4` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-04-02 | `28dec61dd` | 模型支持/运行时入口 | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |
| 2026-03-31 | `b63cd7645` | 性能/后端优化 | 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py` |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |

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

### Commit `466a1d6a4` - 将qwen3_moe文件中的SGLANG_USE_FUSED_BAILING_RMS_ROTARY修改为SGLANG_USE_FUSED_RMS_ROTARY

- Full hash: `466a1d6a4caa1403fb6608748c3111ddc152cdf2`
- Date/author: 2026-04-21 / liucong8560
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `b63cd7645` - 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY

- Full hash: `b63cd76459510fb534dde7d8df2ca438099aa881`
- Date/author: 2026-03-31 / liucong8560
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/qwen3.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/models/bailing_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e9d6aefa9` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- Full hash: `e9d6aefa947699a1edc971ecc2e3fdd2053f525f`
- Date/author: 2026-03-30 / lizhigong
- Auto category: 性能/后端优化
- Main files: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README_DCU.md`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py` 等 25 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/server_args.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## Local-only dev branch update from v0.5.8_dev to v0.5.12_dev

### Coverage Note

- Source index: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- Source worktree: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs.
- Commits in this section: 2
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-03-06 | `4c7028bf2` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | qwen系列模型算子融合 | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py` 等 9 个文件 |
| 2026-03-31 | `2befcb806` | `v0.5.9_dev..v0.5.10_dev` | 模型支持/运行时入口 | 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py` 等 4 个文件 |

### Per-Commit Audit Cards

#### Commit `4c7028bf2` - qwen系列模型算子融合

- Full hash: `4c7028bf269fffb15649d58adf43a8ce1bb51066`
- Date/author: 2026-03-06 / liucong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/bailing_moe.py` 等 9 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
  - other: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/environ.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `2befcb806` - 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY

- Full hash: `2befcb8061ad02de8471f06bc482eb5b7b827243`
- Date/author: 2026-03-31 / liucong8560
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/qwen3.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
  - other: `python/sglang/srt/environ.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
