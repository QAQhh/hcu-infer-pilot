# sglang Qwen3 Coder Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/qwen3.py` | `b63cd7645`, `e9d6aefa9` |

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

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 16 (merges: 1)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `1e2fec228`, `700649f36`, `4603df038`, `050129f5b`, `f4d13c6b8`, `b290dcf39` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e`, `f8bfbc60f`, `050129f5b` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `1e2fec228`, `75a242b3a`, `700649f36`, `b290dcf39` |
| `python/sglang/srt/layers/quantization/unquant.py` | `1e2fec228`, `f8bfbc60f`, `700649f36`, `44d9bdc2e` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `123e9539e`, `f8bfbc60f`, `b290dcf39` |
| `python/sglang/srt/models/qwen3_5.py` | `1e2fec228`, `6e5326678`, `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/layers/moe/moe_runner/aiter.py` | `1e2fec228`, `f8bfbc60f`, `44d9bdc2e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `1e2fec228`, `123e9539e`, `f4d13c6b8` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | `1e2fec228`, `123e9539e`, `71117e8d9` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `123e9539e`, `f8bfbc60f`, `ff5ffaa1a` |
| `python/sglang/srt/layers/quantization/w8a8_fp8.py` | `1e2fec228`, `123e9539e`, `6fd9d5644` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/models/qwen3_moe.py` | `1e2fec228`, `123e9539e`, `b3632f0be` |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `f8bfbc60f` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/arg_groups/overrides.py` | `1e2fec228`, `f8bfbc60f` |
| `python/sglang/srt/configs/__init__.py` | `f8bfbc60f`, `44d9bdc2e` |
| `python/sglang/srt/configs/model_config.py` | `f8bfbc60f`, `44d9bdc2e` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `1e2fec228`, `f8bfbc60f` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/linear/gdn_backend.py` | `1e2fec228`, `f8bfbc60f` |
| `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` | `1e2fec228`, `700649f36` |
| `python/sglang/srt/layers/communicator.py` | `6e5326678`, `123e9539e` |
| `python/sglang/srt/layers/layernorm.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/topk.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `1e2fec228`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py` | `1e2fec228`, `71117e8d9` |
| `python/sglang/srt/layers/quantization/fp8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `1e2fec228`, `123e9539e` |
| ... | 209 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` and 109 files in total |
| 2026-07-22 | `6e5326678` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(dcu): use runtime server args in Qwen3.5 paths | `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` and 91 files in total |
| 2026-08-20 | `9ca1b25f7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #210 from HYGON-AI/main_dev_qwen3.8 | no direct file change / merge |
| 2026-08-31 | `75a242b3a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): running Qwen3-0.6B dismatch shape of one step off policy | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-09-03 | `f8bfbc60f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): Qwen3.8 flash next open support (#281) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` and 100 files in total |
| 2026-09-04 | `71117e8d9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): qwen38 flash next int8 w8a8 support (#310) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py` |
| 2026-09-04 | `ff5ffaa1a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): keep DeepSeek W4A8 Linear quantized while Qwen3.8 uses expe… (#312) | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-09-08 | `700649f36` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 【Feat】Qwen3.6‑35B‑A3B supported dflash2 (#331) | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` and 5 files in total |
| 2026-09-11 | `4603df038` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]Qwen3.6-35B-A3B 支持--speculative-algorithm DSPARK (#341) | `python/sglang/srt/configs/dspark.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` and 5 files in total |
| 2026-09-12 | `050129f5b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [bugfix] Isolate the use of --speculative-algorithm DSPARK for the Qwen3.6-35B-A3B model family via the SGLANG_USE_QWEN_DSPARK environment variable. (#352) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` and 6 files in total |
| 2026-09-12 | `44d9bdc2e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(qwen3_8): support AITER EP and INT8 PLE offload (#350) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` and 9 files in total |
| 2026-09-17 | `f4d13c6b8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Feat]Qwen3.6-35B-A3B DFLASH性能优化 (#388) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/manual/test_hcu_dflash_native_block16.py` |
| 2026-10-09 | `b3632f0be` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen3_moe): quantise MoE gate for compressed-tensors FP8 checkpoints (#492) | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-10-13 | `b290dcf39` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat] 优化 HCU 上 Qwen3.6-35B-A3B 使用 DFLASH 时（--speculative-algorithm DFLASH）的性能 (#522) | `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` and 5 files in total |
| 2026-10-16 | `6fd9d5644` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Bugfix] 修复Qwen3.5-122B-A10B-Channel-FP8重复输出的问题 (#545) | `python/sglang/srt/layers/quantization/w8a8_fp8.py` |

### Per-Commit Audit Cards

#### Commit `1e2fec228` - feat(hcu): port runtime and kernel rename

- Full hash: `1e2fec228a9a8b1e781c3592eff356eeb8b584ed`
- Date/author: 2026-07-20 / tianlinyang77
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/jit_kernel/dsv4/moe.py`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/mxfp8.py` 等 109 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/check_env.py`; `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/fp8_blockwise_gemm.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/mxfp8.py`; `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` 等 80 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `sgl-kernel/tests/test_moe_align.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `6e5326678` - fix(dcu): use runtime server args in Qwen3.5 paths

- Full hash: `6e5326678d6dcac6c8ab88be605b9318b8d0cd70`
- Date/author: 2026-07-22 / lizhigong
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/communicator.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `123e9539e` - fix lint: satisfy pre-commit on the forward-port diff

- Full hash: `123e9539ea23dde2f1a12b0374c1375bbfb10989`
- Date/author: 2026-07-31 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py` 等 91 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py` 等 14 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py` 等 19 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py` 等 56 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_mmlu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `9ca1b25f7` - Merge pull request #210 from HYGON-AI/main_dev_qwen3.8

- Full hash: `9ca1b25f7f912a086d4a5c6a4706a3b373eae0be`
- Date/author: 2026-08-20 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `75a242b3a` - fix(attention): running Qwen3-0.6B dismatch shape of one step off policy

- Full hash: `75a242b3ab043e57ac78035ee9214eba19329ca7`
- Date/author: 2026-08-31 / xingjinliang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f8bfbc60f` - feat(hcu): Qwen3.8 flash next open support (#281)

- Full hash: `f8bfbc60fbb9400391ab7cbf8f1c725bda5c2b59`
- Date/author: 2026-09-03 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`, `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh`, `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh`, `python/sglang/kernels/ops/attention/qsa_indexer.py`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/kernels/ops/elementwise/fast_topk.py` 等 100 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/hc_mix_triton.py`; `python/sglang/srt/layers/hyperconnection.py`; `python/sglang/srt/layers/rotary_embedding/mrope_rope_index.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/configs/qwen4_exp.py`; `python/sglang/srt/configs/update_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/pool_configurator.py` 等 15 个文件
  - runtime-perf: `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`; `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`; `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh`; `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh`; `python/sglang/kernels/ops/attention/qsa_indexer.py`; `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`; `python/sglang/kernels/ops/elementwise/fast_topk.py`; `python/sglang/kernels/ops/elementwise/hc_combine.py` 等 45 个文件
  - tests: `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_aime25.py`; `python/sglang/test/simple_eval_aime26.py`; `test/hcu_humaneval_judge.py`; `test/registered/kernels/benchmark/attention/bench_qsa_indexer.py`; `test/registered/kernels/benchmark/elementwise/bench_fast_topk.py`; `test/registered/kernels/benchmark/elementwise/bench_hc_combine.py`; `test/registered/kernels/benchmark/layernorm/bench_grouped_gemma_rmsnorm.py` 等 25 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `71117e8d9` - feat(hcu): qwen38 flash next int8 w8a8 support (#310)

- Full hash: `71117e8d988a4a0eba516d007cee1f91eadc563b`
- Date/author: 2026-09-04 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `ff5ffaa1a` - fix(hcu): keep DeepSeek W4A8 Linear quantized while Qwen3.8 uses expe… (#312)

- Full hash: `ff5ffaa1a5b662fb48d2895f414c7a3adcd845b6`
- Date/author: 2026-09-04 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `700649f36` - 【Feat】Qwen3.6‑35B‑A3B supported dflash2 (#331)

- Full hash: `700649f36306ad88b7322362f3262154b7b3adff`
- Date/author: 2026-09-08 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/dflash.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`; `python/sglang/srt/layers/quantization/unquant.py`; `python/sglang/srt/models/dflash.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `4603df038` - [feat]Qwen3.6-35B-A3B 支持--speculative-algorithm DSPARK (#341)

- Full hash: `4603df038bccfa86a42db00202c1cd25c8d6529b`
- Date/author: 2026-09-11 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/dspark.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/utils/hf_transformers/config.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/configs/dspark.py`; `python/sglang/srt/models/dspark.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/speculative/dflash_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `050129f5b` - [bugfix] Isolate the use of --speculative-algorithm DSPARK for the Qwen3.6-35B-A3B model family via the SGLANG_USE_QWEN_DSPARK environment variable. (#352)

- Full hash: `050129f5b3406b3b003378dccd3009433df76d7a`
- Date/author: 2026-09-12 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dspark_components/dspark_config.py`, `python/sglang/srt/utils/hf_transformers/config.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/dspark.py`; `python/sglang/srt/speculative/dspark_components/dspark_config.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/speculative/dflash_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `44d9bdc2e` - feat(qwen3_8): support AITER EP and INT8 PLE offload (#350)

- Full hash: `44d9bdc2e91331a912ac4d613381c8f044893dd0`
- Date/author: 2026-09-12 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`, `python/sglang/srt/models/qwen4_exp.py`, `python/sglang/srt/utils/hf_transformers/common.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py` 等 9 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/utils/hf_transformers/common.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/models/qwen4_exp.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/quantization/unquant.py`
  - tests: `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`; `test/registered/unit/layers/moe/test_aiter_runner.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f4d13c6b8` - [Feat]Qwen3.6-35B-A3B DFLASH性能优化 (#388)

- Full hash: `f4d13c6b88c6a3494b1036d62de54f6849d73eed`
- Date/author: 2026-09-17 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/manual/test_hcu_dflash_native_block16.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`
  - tests: `test/manual/test_hcu_dflash_native_block16.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b3632f0be` - fix(qwen3_moe): quantise MoE gate for compressed-tensors FP8 checkpoints (#492)

- Full hash: `b3632f0be3bf48b1bf48d0444e4be4f1ee4bc63b`
- Date/author: 2026-10-09 / liuzj512
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b290dcf39` - [feat] 优化 HCU 上 Qwen3.6-35B-A3B 使用 DFLASH 时（--speculative-algorithm DFLASH）的性能 (#522)

- Full hash: `b290dcf39562e7ae6ed5f1646bbd20d1e1d8c7fc`
- Date/author: 2026-10-13 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/speculative/dflash.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/speculative/dflash_worker_v2.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `6fd9d5644` - [Bugfix] 修复Qwen3.5-122B-A10B-Channel-FP8重复输出的问题 (#545)

- Full hash: `6fd9d5644212bf13a4b5394a6b5a2007fa49e68b`
- Date/author: 2026-10-16 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
