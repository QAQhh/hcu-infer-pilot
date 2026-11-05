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

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 8 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/qwen3_5.py` | `1e2fec228`, `6e5326678`, `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `1e2fec228`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/linear/gdn_backend.py` | `1e2fec228`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/unquant.py` | `1e2fec228`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/w8a8_fp8.py` | `1e2fec228`, `123e9539e`, `6fd9d5644` |
| `python/sglang/srt/model_executor/model_runner.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_v2.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_v4.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/qwen3_vl.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/speculative/draft_utils.py` | `1e2fec228`, `7b3548f97`, `f8bfbc60f` |
| `.github/workflows/nightly-test-hcu.yml` | `9b86479ac`, `2b4271498` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/arg_groups/overrides.py` | `1e2fec228`, `f8bfbc60f` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/aiter_backend.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/triton_backend.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/vision.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/communicator.py` | `6e5326678`, `123e9539e` |
| `python/sglang/srt/layers/layernorm.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/mega_moe.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/moe/moe_runner/aiter.py` | `1e2fec228`, `f8bfbc60f` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/topk.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `1e2fec228`, `f8bfbc60f` |
| ... | 244 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` and 109 files in total |
| 2026-07-21 | `9b86479ac` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | test(hcu): add MATH-500 and HumanEval nightly coverage | `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md` and 14 files in total |
| 2026-07-22 | `6e5326678` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(dcu): use runtime server args in Qwen3.5 paths | `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` and 91 files in total |
| 2026-08-07 | `2b4271498` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` and 11 files in total |
| 2026-08-25 | `7b3548f97` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` and 48 files in total |
| 2026-09-03 | `f8bfbc60f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): Qwen3.8 flash next open support (#281) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` and 100 files in total |
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

#### Commit `9b86479ac` - test(hcu): add MATH-500 and HumanEval nightly coverage

- Full hash: `9b86479ac4f933649d4f777d1ffb92bfbfc375ab`
- Date/author: 2026-07-21 / tianlinyang77
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_reasoning_code_utils.py`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`, `test/hcu_humaneval_judge.py` 等 14 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `.gitignore`; `THIRD_PARTY_NOTICES.md`; `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_reasoning_code_utils.py`; `test/hcu_humaneval_judge.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen35_397b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen36_35b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_30b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_32b_hcu.py`; `test/run_suite.py` 等 9 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

#### Commit `2b4271498` - ci(hcu): publish nine-model accuracy results

- Full hash: `2b4271498f3d9031d0080accfa4dea9eccd10a59`
- Date/author: 2026-08-07 / LvJIA-RG
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `7b3548f97` - fix lint: apply pre-commit fixes across the 20260824 sync diff

- Full hash: `7b3548f97409d83b7e7dde4c3ad71e2f30955267`
- Date/author: 2026-08-25 / RyeYuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/utils.py` 等 48 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/hardware_backend/npu/utils.py`; `python/sglang/srt/sampling/sampling_batch_info.py`; `python/sglang/srt/speculative/draft_utils.py`; `python/sglang/srt/speculative/eagle_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`; `python/sglang/kernels/ops/moe/ep_moe_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 22 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_server_args.py`; `test/registered/hicache/test_hicache_storage_3fs_backend.py`; `test/registered/openai_server/validation/test_matched_stop.py`; `test/registered/pp/test_pp_single_node.py`; `test/registered/profiling/test_start_profile.py`; `test/registered/unit/entrypoints/openai/test_serving_embedding.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/unit/function_call/test_json_schema_constraint.py` 等 13 个文件
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

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## Local-only branch update from release/20260825_v0.5.18 to release_v0.5.18_deepseekv4

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-05
- Commits in this section: 0 (merges: 0)
- Branch segments: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

- No local-only commit in these branch segments belongs to this bucket.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
