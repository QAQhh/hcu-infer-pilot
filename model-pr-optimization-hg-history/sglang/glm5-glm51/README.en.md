# sglang GLM-5/5.1 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| - | no local-only commit |

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
| 2026-04-30 | `752ed6468` | 性能/后端优化 | 修复glm5w4a8重排逻辑，减少显存占用 | `python/sglang/srt/layers/quantization/w4a8_utils.py` |
| 2026-04-30 | `262fa654e` | 调度/缓存/PD | 【GLM5】NSA indexer新增bf16路径 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-04-28 | `74f1c1b27` | 调度/缓存/PD | 合入官方pr，解决glm5跑pd分离时page计算不一致崩溃 | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-04-25 | `78557fe3d` | 通用实现调整 | 【GLM5】避免DCU路径加载TileLang和TVM依赖 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-04-23 | `c40804b20` | 性能/后端优化 | 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合 3. 融合get_logits_head_gate算子 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |

## Per-Commit Audit Cards

### Commit `752ed6468` - 修复glm5w4a8重排逻辑，减少显存占用

- Full hash: `752ed6468ffafbcd5743df06e40eb5ef2685a29c`
- Date/author: 2026-04-30 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/w4a8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/w4a8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `262fa654e` - 【GLM5】NSA indexer新增bf16路径

- Full hash: `262fa654e806f504f9a20f5b7438975bb719d891`
- Date/author: 2026-04-30 / maxiao1
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `74f1c1b27` - 合入官方pr，解决glm5跑pd分离时page计算不一致崩溃

- Full hash: `74f1c1b27935b7b6fc83c3d25f962cc31e4f625e`
- Date/author: 2026-04-28 / maxiao1
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/mooncake/conn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `78557fe3d` - 【GLM5】避免DCU路径加载TileLang和TVM依赖

- Full hash: `78557fe3d0893bb8173b1322ef08fe722accf2af`
- Date/author: 2026-04-25 / maxiao1
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c40804b20` - 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合  3. 融合get_logits_head_gate算子

- Full hash: `c40804b203877a1affe2cc3862fc26dc29b8efdd`
- Date/author: 2026-04-23 / maxiao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2854c89b4` - 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化

- Full hash: `2854c89b4ee838989dea9b7e403840dfcf4d7116`
- Date/author: 2026-04-10 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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
| 2026-03-18 | `c6c74dbdc` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM5 Test | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py` 等 16 个文件 |
| 2026-03-26 | `5f51de15a` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM-5 adaptation | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 6 个文件 |
| 2026-03-27 | `40a938509` | `v0.5.8_dev..v0.5.9_dev` | 调度/缓存/PD | add prefill flashmla_sparse kv_cache fp8 for GLM-5 | `python/sglang/srt/layers/attention/nsa_backend.py`, `sgl-kernel/setup_rocm.py` |
| 2026-03-30 | `511c78385` | `v0.5.8_dev..v0.5.9_dev` | 调度/缓存/PD | GLM5 MTP adapt | `python/sglang/srt/layers/attention/nsa_backend.py` |

### Per-Commit Audit Cards

#### Commit `c6c74dbdc` - GLM5 Test

- Full hash: `c6c74dbdca35022867b4b68400fe87f9d7666790`
- Date/author: 2026-03-18 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 16 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` 等 10 个文件
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `5f51de15a` - GLM-5 adaptation

- Full hash: `5f51de15a2c8993abd00cc90d8c22f976b9da7dc`
- Date/author: 2026-03-26 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `40a938509` - add prefill flashmla_sparse kv_cache fp8 for GLM-5

- Full hash: `40a93850978de3f1418bc484079c3ed252ec34c4`
- Date/author: 2026-03-27 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/nsa_backend.py`, `sgl-kernel/setup_rocm.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`; `sgl-kernel/setup_rocm.py`
- Risk and verification: Touches scheduling, cache, PD, or MTP paths; verify prefill/decode ordering, first-token correctness, concurrency, and long-context stability.

#### Commit `511c78385` - GLM5 MTP adapt

- Full hash: `511c78385d2165c95fcd3e73a79dcca93b4430f8`
- Date/author: 2026-03-30 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/nsa_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches scheduling, cache, PD, or MTP paths; verify prefill/decode ordering, first-token correctness, concurrency, and long-context stability.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 11 (merges: 3)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `502516539`, `723ac998c` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `2ac651d8f`, `3c2b52667` |
| `python/sglang/srt/utils/hf_transformers/config.py` | `0cf9a653e`, `502516539` |
| `test/registered/unit/utils/test_hf_transformers.py` | `0cf9a653e`, `502516539` |
| `.github/workflows/nightly-test-hcu.yml` | `2b4271498` |
| `.github/workflows/pr-test-hcu.yml` | `723ac998c` |
| `benchmark/glm53/README.md` | `98e923533` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `100533036` |
| `python/sglang/srt/disaggregation/mooncake/source_drain.py` | `100533036` |
| `python/sglang/srt/disaggregation/prefill.py` | `100533036` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `723ac998c` |
| `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py` | `723ac998c` |
| `python/sglang/srt/environ.py` | `723ac998c` |
| `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` | `723ac998c` |
| `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py` | `98e923533` |
| `python/sglang/srt/layers/attention/dsa/utils.py` | `723ac998c` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `723ac998c` |
| `python/sglang/srt/layers/cp/cp_decode_attn_tp.py` | `723ac998c` |
| `python/sglang/srt/layers/cp/interleave.py` | `723ac998c` |
| `python/sglang/srt/layers/cp/utils.py` | `723ac998c` |
| `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | `2ac651d8f` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `723ac998c` |
| `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | `98e923533` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `723ac998c` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `2ac651d8f` |
| `python/sglang/srt/managers/overlap_utils.py` | `98e923533` |
| `python/sglang/srt/managers/schedule_batch.py` | `100533036` |
| `python/sglang/srt/managers/scheduler.py` | `100533036` |
| `python/sglang/srt/mem_cache/cleanup.py` | `100533036` |
| `python/sglang/srt/mem_cache/common.py` | `100533036` |
| `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py` | `100533036` |
| `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` | `100533036` |
| `python/sglang/srt/mem_cache/unified_radix_cache.py` | `100533036` |
| `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py` | `723ac998c` |
| `python/sglang/srt/model_executor/pool_configurator.py` | `502516539` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | `98e923533` |
| `python/sglang/srt/models/deepseek_v2.py` | `98e923533` |
| `python/sglang/srt/server_args.py` | `723ac998c` |
| `python/sglang/srt/speculative/eagle_utils.py` | `723ac998c` |
| `python/sglang/srt/speculative/eagle_worker_v2.py` | `723ac998c` |
| ... | 37 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-08-07 | `2b4271498` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` and 11 files in total |
| 2026-08-19 | `0cf9a653e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(glm5.2): restore raw DSA config fields | `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/unit/utils/test_hf_transformers.py` |
| 2026-08-26 | `502516539` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | style: format GLM 5.2 forward-port files | `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/utils/hf_transformers/config.py` and 5 files in total |
| 2026-08-27 | `cff97568f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge feature/glm52-forward-port-v0.5.18 into release/20260825_v0.5.18 | no direct file change / merge |
| 2026-08-28 | `11852ed1c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #256 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port | no direct file change / merge |
| 2026-08-31 | `3a160688a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #262 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port | no direct file change / merge |
| 2026-09-17 | `98e923533` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(glm53): 修正 FP8 权重映射并优化 HCU Decode 路径 (#384) | `benchmark/glm53/README.md`, `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` and 6 files in total |
| 2026-09-30 | `100533036` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [Fix][Unified Cache] Retry external KV abort cleanup after forward and source drain (#455) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mooncake/source_drain.py`, `python/sglang/srt/disaggregation/prefill.py` and 21 files in total |
| 2026-10-09 | `723ac998c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 修复 GLM-5.1/5.2 DSA 服务兼容性并优化 CP decode FlashMLA (#475) | `.github/workflows/pr-test-hcu.yml`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py` and 32 files in total |
| 2026-10-12 | `2ac651d8f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(w4a8): 兼容 GLM5.3-w4a8 模型的 compressed-tensors 打包权重 (#506) | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-10-15 | `3c2b52667` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(GLM5.3 w4a8): skip unused packed expert shape metadata (#539) | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |

### Per-Commit Audit Cards

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

#### Commit `0cf9a653e` - fix(glm5.2): restore raw DSA config fields

- Full hash: `0cf9a653eda76ddefec1c3044692433d1d033a36`
- Date/author: 2026-08-19 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/unit/utils/test_hf_transformers.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/utils/hf_transformers/config.py`
  - tests: `test/registered/unit/utils/test_hf_transformers.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `502516539` - style: format GLM 5.2 forward-port files

- Full hash: `5025165399aca0f6c482556c12bf53fbc4b870fd`
- Date/author: 2026-08-26 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/moe/test_topk_padded_region.py`, `test/registered/unit/utils/test_hf_transformers.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - tests: `test/registered/moe/test_topk_padded_region.py`; `test/registered/unit/utils/test_hf_transformers.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `cff97568f` - Merge feature/glm52-forward-port-v0.5.18 into release/20260825_v0.5.18

- Full hash: `cff97568fd17b74e707f3552bafc924abfa175de`
- Date/author: 2026-08-27 / luosyx
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `11852ed1c` - Merge pull request #256 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port

- Full hash: `11852ed1c2f6b2b26cb168a892c927efe95cbb7a`
- Date/author: 2026-08-28 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `3a160688a` - Merge pull request #262 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port

- Full hash: `3a160688a388a5ddcb84d8bfe1ca2451df609dda`
- Date/author: 2026-08-31 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `98e923533` - fix(glm53): 修正 FP8 权重映射并优化 HCU Decode 路径 (#384)

- Full hash: `98e92353399b9cf708523b02834b4894a3aa3321`
- Date/author: 2026-09-17 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `benchmark/glm53/README.md`, `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - docs-bench: `benchmark/glm53/README.md`
  - other: `python/sglang/srt/managers/overlap_utils.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `100533036` - [Fix][Unified Cache] Retry external KV abort cleanup after forward and source drain (#455)

- Full hash: `10053303694ba99167f7e17c585757fe3cf851bb`
- Date/author: 2026-09-30 / ybhe1110
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mooncake/source_drain.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cleanup.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py` 等 21 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/mooncake/source_drain.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/managers/schedule_batch.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/cleanup.py`; `python/sglang/srt/mem_cache/common.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`; `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`; `python/sglang/srt/mem_cache/unified_radix_cache.py`
  - tests: `python/sglang/test/kits/linker_load_failure_kit.py`; `python/sglang/test/mooncake_utils.py`; `test/registered/radix_cache/unified_radix_tree/linker/test_unified_cache_linker_kl_dsv4.py`; `test/registered/radix_cache/unified_radix_tree/linker/test_unified_cache_linker_kl_glm52.py`; `test/registered/unit/disaggregation/test_external_kv_abort_drain.py`; `test/registered/unit/disaggregation/test_external_kv_cleanup_resources.py`; `test/registered/unit/disaggregation/test_pp_pd_consensus.py`; `test/registered/unit/disaggregation/test_prefill_abort_cleanup.py` 等 11 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `723ac998c` - 修复 GLM-5.1/5.2 DSA 服务兼容性并优化 CP decode FlashMLA (#475)

- Full hash: `723ac998c384e495b66f57119382a3434d2d4152`
- Date/author: 2026-10-09 / qieshiniao
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test-hcu.yml`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/cp/cp_decode_attn_tp.py` 等 32 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/layers/cp/cp_decode_attn_tp.py`; `python/sglang/srt/layers/cp/interleave.py`; `python/sglang/srt/layers/cp/utils.py`; `python/sglang/srt/speculative/eagle_utils.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`; `python/sglang/srt/speculative/frozen_kv_mtp_worker_v2.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`; `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`; `python/sglang/srt/layers/attention/dsa/utils.py`; `python/sglang/srt/layers/attention/dsa_backend.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`
  - tests: `test/registered/hcu/unit/test_hcu_cp_decode_attn_tp_scale.py`; `test/registered/hcu/unit/test_hcu_dsa_cp_alignment.py`; `test/registered/hcu/unit/test_hcu_eagle_sampling_compat.py`; `test/registered/hcu/unit/test_hcu_eagle_verify_sync.py`; `test/registered/hcu/unit/test_hcu_flashmla_decode_h16.py`; `test/registered/hcu/unit/test_hcu_flashmla_decode_h16_memory.py`; `test/registered/hcu/unit/test_hcu_lightop_moe_routing_api.py`; `test/registered/hcu/unit/test_hcu_multimem_all_gather_guard.py` 等 13 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2ac651d8f` - fix(w4a8): 兼容 GLM5.3-w4a8 模型的 compressed-tensors 打包权重 (#506)

- Full hash: `2ac651d8f6b78dcc8214119e733c4ba55be15945`
- Date/author: 2026-10-12 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `3c2b52667` - fix(GLM5.3 w4a8): skip unused packed expert shape metadata (#539)

- Full hash: `3c2b5266717c24b831160a3c2f8c09b7f765d313`
- Date/author: 2026-10-15 / Songge
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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
