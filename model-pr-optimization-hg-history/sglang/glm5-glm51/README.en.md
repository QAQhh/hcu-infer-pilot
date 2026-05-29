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
