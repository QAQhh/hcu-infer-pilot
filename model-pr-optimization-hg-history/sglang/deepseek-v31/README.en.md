# sglang DeepSeek V3.1 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `47b08354a`, `e9d6aefa9` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `47b08354a` |
| `python/sglang/srt/models/deepseek_v2.py` | `2854c89b4`, `79349e551`, `2b0bed239`, `e9d6aefa9` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 5
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-16 | `47b08354a` | 缺陷修复 | 1. 修复mqa logits chunk bug 2.将FP8 MLA BMM权重在加载时转为BF16，避免forward中重复cast | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-03-31 | `79349e551` | 性能/后端优化 | 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` |
| 2026-03-30 | `2b0bed239` | 性能/后端优化 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |

## Per-Commit Audit Cards

### Commit `47b08354a` - 1. 修复mqa logits chunk bug 2.将FP8 MLA BMM权重在加载时转为BF16，避免forward中重复cast

- Full hash: `47b08354ad96b97bb18c738bac89349ee9cec5bc`
- Date/author: 2026-04-16 / niuhb
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
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

### Commit `79349e551` - 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug

- Full hash: `79349e5510a7485abc9102a64f972c07d2f8790b`
- Date/author: 2026-03-31 / niuhb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/deepseek_v2.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/setup_hip.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/setup_hip.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2b0bed239` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- Full hash: `2b0bed23943bee2e93916979aabc272268a11a1c`
- Date/author: 2026-03-30 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
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
- Commits in this section: 8
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-03-18 | `c6c74dbdc` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM5 Test | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py` 等 16 个文件 |
| 2026-03-26 | `5f51de15a` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM-5 adaptation | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 6 个文件 |
| 2026-03-30 | `00db89c86` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |
| 2026-03-30 | `7bfdade34` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |
| 2026-03-31 | `b4de83009` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` 等 7 个文件 |
| 2026-05-09 | `fe8d278ca` | `v0.5.10_dev..v0.5.11_dev` | 缺陷修复 | debugging qwen3.5 model | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 6 个文件 |
| 2026-05-08 | `ba7aa00c9` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix bug | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-05-18 | `43efcafdc` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix init error when use qwen 3.5 | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 7 个文件 |

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

#### Commit `00db89c86` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- Full hash: `00db89c86ed93c08a883ffa6b708babf8e89743c`
- Date/author: 2026-03-30 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `7bfdade34` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- Full hash: `7bfdade34395bd4ae7c723b64de68a990820d0b2`
- Date/author: 2026-03-30 / maxiao1
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `b4de83009` - 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug

- Full hash: `b4de83009ba8c4f8bce8a242ecd6a2af0f0237ff`
- Date/author: 2026-03-31 / niuhb
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/deepseek_v2.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/setup_hip.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_kernel.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/setup_hip.py`
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

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

#### Commit `ba7aa00c9` - fix bug

- Full hash: `ba7aa00c97719d471e95a869baf3bea0ca59d297`
- Date/author: 2026-05-08 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
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
- Commits in this section: 21 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/deepseek_v2.py` | `b5f9777d2`, `6e0a964d1`, `0f6c8298b`, `1e2fec228`, `123e9539e`, `3d0f94345`, `94bacd49a`, `8a11867b1`, `7b3548f97`, `551a71d4d`, `37f23f55a`, `98e923533`, ... (16 total) |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e`, `3d0f94345`, `8a11867b1`, `7b3548f97`, `602fb4a30`, `76e87a951` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e`, `94bacd49a`, `7b3548f97`, `551a71d4d`, `602fb4a30` |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `3d0f94345`, `31576cba7`, `8a11867b1`, `551a71d4d` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `1e2fec228`, `123e9539e`, `551a71d4d`, `2ac651d8f`, `3c2b52667` |
| `python/sglang/srt/models/deepseek_v4.py` | `1e2fec228`, `123e9539e`, `7b3548f97`, `37f23f55a`, `602fb4a30` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e`, `7b3548f97`, `c9a84fca9` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e`, `7b3548f97`, `602fb4a30` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `1e2fec228`, `94bacd49a`, `8a11867b1`, `551a71d4d` |
| `python/sglang/srt/layers/attention/hcu_mla_backend.py` | `1e2fec228`, `31576cba7`, `f31521614`, `2bf2890f8` |
| `python/sglang/srt/model_executor/model_runner.py` | `1e2fec228`, `123e9539e`, `3d0f94345`, `7b3548f97` |
| `python/sglang/srt/speculative/draft_utils.py` | `1e2fec228`, `7b3548f97`, `f31521614`, `2bf2890f8` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e`, `2bf2890f8` |
| `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` | `1e2fec228`, `551a71d4d`, `76e87a951` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `1e2fec228`, `31576cba7`, `8084b5cac` |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `1e2fec228`, `f31521614`, `2bf2890f8` |
| `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | `123e9539e`, `76e87a951`, `2ac651d8f` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `1e2fec228`, `123e9539e`, `76e87a951` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | `551a71d4d`, `98e923533`, `c9a84fca9` |
| `python/sglang/srt/models/qwen3_5.py` | `1e2fec228`, `123e9539e`, `7b3548f97` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh` | `551a71d4d`, `76e87a951` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/arg_groups/overrides.py` | `1e2fec228`, `551a71d4d` |
| `python/sglang/srt/configs/model_config.py` | `3d0f94345`, `551a71d4d` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `3d0f94345` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `1e2fec228`, `3d0f94345` |
| `python/sglang/srt/disaggregation/prefill.py` | `123e9539e`, `3d0f94345` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/aiter_backend.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/linear/gdn_backend.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/triton_backend.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/vision.py` | `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/communicator.py` | `123e9539e`, `76e87a951` |
| `python/sglang/srt/layers/layernorm.py` | `1e2fec228`, `123e9539e` |
| ... | 205 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-14 | `b5f9777d2` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | Fix DCU DSV4 hash top-k router dtype | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-07-14 | `6e0a964d1` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | Fix DeepSeek fused RMS quant MoE path | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-07-15 | `0f6c8298b` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | Revert "Fix DeepSeek fused RMS quant MoE path" | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` and 109 files in total |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` and 91 files in total |
| 2026-08-06 | `3d0f94345` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(hcu): fully revert files owned by the skipped source commits | `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py` and 20 files in total |
| 2026-08-04 | `31576cba7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: integrate hcu_mla and causal_conv1d modules | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` and 5 files in total |
| 2026-08-11 | `8084b5cac` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | merge: fix kimi-k3 merge conflict | `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-08-19 | `94bacd49a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): reuse sorted DSA TopK indices | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-08-19 | `8a11867b1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(hcu): extend DSA LayerSplit for PP and HiCache | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` and 11 files in total |
| 2026-08-25 | `7b3548f97` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` and 48 files in total |
| 2026-09-10 | `551a71d4d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Feature/hy4 ihc tilelang 5commits (#336) | `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh` and 25 files in total |
| 2026-09-15 | `37f23f55a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(dsv4): auto-dispatch BF16-to-FP32 GEMM backends (#375) | `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh`, `python/sglang/kernels/ops/attention/dsv4/gemm.py`, `python/sglang/kernels/ops/attention/dsv4/hcu_linear_bf16_fp32.py` and 10 files in total |
| 2026-09-17 | `98e923533` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(glm53): 修正 FP8 权重映射并优化 HCU Decode 路径 (#384) | `benchmark/glm53/README.md`, `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` and 6 files in total |
| 2026-09-20 | `602fb4a30` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [FEAT] Support the BCG with CP-V2 and expect to improve TTFT from 10%… (#407) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/cp/bcg.py` and 9 files in total |
| 2026-09-30 | `76e87a951` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): serve DeepSeek-V3.2 INT8, FP8, and BF16 in sglang0.5.18 (#466) | `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/communicator.py` and 9 files in total |
| 2026-10-08 | `f31521614` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): enable EAGLE draft decoding for DeepSeek MLA (#477) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/models/deepseek_v2.py` and 4 files in total |
| 2026-10-09 | `2bf2890f8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): correct DeepSeek-V3.1 FP8 decode under CUDA graph (#483) | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py` and 5 files in total |
| 2026-10-12 | `2ac651d8f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(w4a8): 兼容 GLM5.3-w4a8 模型的 compressed-tensors 打包权重 (#506) | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-10-12 | `c9a84fca9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Perf][HCU] Optimize Kimi K3 decode fusions 20261010 (#507) | `.gitignore`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py` and 17 files in total |
| 2026-10-15 | `3c2b52667` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(GLM5.3 w4a8): skip unused packed expert shape metadata (#539) | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |

### Per-Commit Audit Cards

#### Commit `b5f9777d2` - Fix DCU DSV4 hash top-k router dtype

- Full hash: `b5f9777d2609d174738aa48de8263c819fa94e0d`
- Date/author: 2026-07-14 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 缺陷修复
- Main files: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `6e0a964d1` - Fix DeepSeek fused RMS quant MoE path

- Full hash: `6e0a964d1e09d90dbde14d9c8d4372bf59166b1c`
- Date/author: 2026-07-14 / yuchenyang
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `0f6c8298b` - Revert "Fix DeepSeek fused RMS quant MoE path"

- Full hash: `0f6c8298b20d1d9ef639999d21cf372f3f181b28`
- Date/author: 2026-07-15 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

#### Commit `3d0f94345` - fix(hcu): fully revert files owned by the skipped source commits

- Full hash: `3d0f9434512ab52e842d3e42549756f022d0b572`
- Date/author: 2026-08-06 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/cache_controller.py` 等 20 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/speculative/eagle_info.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/jit_kernel/dsv4/compress.py`; `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`; `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `31576cba7` - feat: integrate hcu_mla and causal_conv1d modules

- Full hash: `31576cba7da75ca463fc1fee1d4010dc2ea0bd47`
- Date/author: 2026-08-04 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/hcu_mla_backend.py`; `python/sglang/srt/layers/attention/linear/kda_backend.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `8084b5cac` - merge: fix kimi-k3 merge conflict

- Full hash: `8084b5cacf215104abd62eb2e5e548a0f019302a`
- Date/author: 2026-08-11 / zhaosong1
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `94bacd49a` - perf(hcu): reuse sorted DSA TopK indices

- Full hash: `94bacd49a0dd8c64d6cc6aebcb8d118df1bb7d45`
- Date/author: 2026-08-19 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `8a11867b1` - feat(hcu): extend DSA LayerSplit for PP and HiCache

- Full hash: `8a11867b1b679a724ee546d40ffedab9c36da4c1`
- Date/author: 2026-08-19 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/base.py`, `python/sglang/srt/mem_cache/pool_host/common.py`, `python/sglang/srt/mem_cache/pool_host/mla.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/communicator_dsa_cp.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa_backend.py`; `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/pool_host/base.py`; `python/sglang/srt/mem_cache/pool_host/common.py`; `python/sglang/srt/mem_cache/pool_host/mla.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

#### Commit `551a71d4d` - Feature/hy4 ihc tilelang 5commits (#336)

- Full hash: `551a71d4d6966366e76378c06be035079ef96963`
- Date/author: 2026-09-10 / liuzj512
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/hy_v4.py`, `python/sglang/srt/configs/model_config.py` 等 25 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/expert_location_dispatch.py`; `python/sglang/srt/layers/hy4_ihc_tilelang.py`; `python/sglang/srt/utils/hf_transformers/common.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/hy_v4.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/hunyuan_v4.py`; `python/sglang/srt/models/hunyuan_v4_nextn.py` 等 9 个文件
  - runtime-perf: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`; `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`; `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`; `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`; `python/sglang/srt/layers/attention/dsa_backend.py`; `python/sglang/srt/layers/radix_attention.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`
  - tests: `test/manual/layers/test_hy4_ihc_tilelang.py`; `test/registered/unit/models/test_hunyuan_v4_nextn_weight_loading.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `37f23f55a` - perf(dsv4): auto-dispatch BF16-to-FP32 GEMM backends (#375)

- Full hash: `37f23f55a0a348e10240369a3c8d112a62efed35`
- Date/author: 2026-09-15 / Yongqiang Duan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh`, `python/sglang/kernels/ops/attention/dsv4/gemm.py`, `python/sglang/kernels/ops/attention/dsv4/hcu_linear_bf16_fp32.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/utils/aiter.py`, `test/registered/hcu/kernels/test_linear_bf16_fp32_hcu.py` 等 10 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/utils/aiter.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh`; `python/sglang/kernels/ops/attention/dsv4/gemm.py`; `python/sglang/kernels/ops/attention/dsv4/hcu_linear_bf16_fp32.py`; `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`
  - tests: `test/registered/hcu/kernels/test_linear_bf16_fp32_hcu.py`; `test/registered/hcu/perf/bench_linear_bf16_fp32_hcu.py`; `test/registered/unit/test_linear_bf16_fp32_dispatch.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

#### Commit `602fb4a30` - [FEAT] Support the BCG with CP-V2 and expect to improve TTFT from 10%… (#407)

- Full hash: `602fb4a30f93bd40a5eda61e5bc02906fc8d4825`
- Date/author: 2026-09-20 / YuanYuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v2.py` 等 9 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/layers/cp/bcg.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/runner/eager_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/managers/scheduler_components/dp_attn.py`; `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `76e87a951` - fix(hcu): serve DeepSeek-V3.2 INT8, FP8, and BF16 in sglang0.5.18 (#466)

- Full hash: `76e87a951d7a7423cf9686ef4109f98d25c2a0cf`
- Date/author: 2026-09-30 / lipenghui
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 9 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/communicator.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`; `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f31521614` - fix(hcu): enable EAGLE draft decoding for DeepSeek MLA (#477)

- Full hash: `f315216140b16b55ca249cfb07516128fa0949ef`
- Date/author: 2026-10-08 / zhangang1221
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/speculative/draft_utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/speculative/draft_utils.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/hcu_mla_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2bf2890f8` - fix(hcu): correct DeepSeek-V3.1 FP8 decode under CUDA graph (#483)

- Full hash: `2bf2890f8830987c79057b5784515cbe21fdb3e5`
- Date/author: 2026-10-09 / lipenghui
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/speculative/draft_utils.py`, `test/registered/unit/distributed/test_aiter_custom_all_reduce_config.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/speculative/draft_utils.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/hcu_mla_backend.py`
  - tests: `test/registered/unit/distributed/test_aiter_custom_all_reduce_config.py`
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

#### Commit `c9a84fca9` - [Perf][HCU] Optimize Kimi K3 decode fusions 20261010 (#507)

- Full hash: `c9a84fca9624adb32d1848a05298a39ca6f0409f`
- Date/author: 2026-10-12 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `.gitignore`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py`, `python/sglang/kernels/ops/kimi_k3/csrc/mla_post_hip.cu`, `python/sglang/kernels/ops/kimi_k3/mla_post_hip.py`, `python/sglang/kernels/ops/mamba/csrc/mamba_state_indices_hip.cu`, `python/sglang/kernels/ops/mamba/mamba_state_indices.py`, `python/sglang/kernels/ops/mamba/mamba_state_indices_hip.py` 等 17 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `.gitignore`; `python/sglang/srt/layers/attn_residual.py`; `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py`; `python/sglang/kernels/ops/kimi_k3/csrc/mla_post_hip.cu`; `python/sglang/kernels/ops/kimi_k3/mla_post_hip.py`; `python/sglang/kernels/ops/mamba/csrc/mamba_state_indices_hip.cu`; `python/sglang/kernels/ops/mamba/mamba_state_indices.py`; `python/sglang/kernels/ops/mamba/mamba_state_indices_hip.py`; `python/sglang/srt/distributed/parallel_state.py` 等 12 个文件
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
- Commits in this section: 2 (merges: 0)
- Branch segments: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/kernels/ops/attention/dsv4/attn.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/arg_groups/deepseek_v4_hook.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/disaggregation/decode.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/disaggregation/prefill.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/disaggregation/utils.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/environ.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/cp/interleave.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/engram.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/logits_processor.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/moe/mega_moe.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/moe/topk.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/layers/utils/hcu_cp_utils.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/managers/schedule_batch.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_helpers.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_pool.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/mem_cache/cp_cache_layer_split/staging.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/mem_cache/cp_cache_layer_split/transfer.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/mem_cache/cp_cache_layer_split/validation.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/model_executor/pool_configurator.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/model_executor/runner/eager_runner.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/models/deepseek_v2.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/models/deepseek_v4.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/models/deepseek_v4_dspark.py` | `15c7204b7`, `5343b311c` |
| `python/sglang/srt/multimodal/dsv41/vl_routing.py` | `15c7204b7`, `5343b311c` |
| `test/registered/unit/layers/cp/test_interleave_cp_gather_memory.py` | `15c7204b7`, `5343b311c` |
| `test/registered/unit/layers/moe/test_hcu_compressed_tensors_w4a8_deepep_ll.py` | `15c7204b7`, `5343b311c` |
| `test/registered/unit/layers/test_engram_idle.py` | `15c7204b7`, `5343b311c` |
| `test/registered/unit/mem_cache/test_cp_cache_layer_split_async_pages.py` | `15c7204b7`, `5343b311c` |
| `test/registered/unit/mem_cache/test_cp_cache_layer_split_dspark.py` | `15c7204b7`, `5343b311c` |
| `test/registered/unit/mem_cache/test_dsv4_compressed_pools.py` | `15c7204b7`, `5343b311c` |
| `test/registered/unit/model_executor/test_eager_runner_cp_aux.py` | `15c7204b7`, `5343b311c` |
| ... | 150 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-10-26 | `15c7204b7` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [Feat] [HCU] dsv4.1: Sync feature branch updates into main (#594) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `python/sglang/kernels/aot/benchmark/bench_rope_fp4.py` and 139 files in total |
| 2026-11-03 | `5343b311c` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Feat/20261102 Sync latest deepseek-v4.1 optimizations to main (#640) | `python/sglang/kernels/ops/attention/dsv4/attn.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_rope_hcu.py` and 93 files in total |

### Per-Commit Audit Cards

#### Commit `15c7204b7` - [Feat] [HCU] dsv4.1: Sync feature branch updates into main (#594)

- Full hash: `15c7204b7a3b6edaa222cff80018d8e5f2b2ad0e`
- Date/author: 2026-10-26 / YuanYuan
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `python/sglang/kernels/aot/benchmark/bench_rope_fp4.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/rope_fp4.hip`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h`, `python/sglang/kernels/aot/python/sgl_kernel/__init__.py`, `python/sglang/kernels/aot/python/sgl_kernel/elementwise.py` 等 139 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/parallel.py`; `python/sglang/srt/arg_groups/model_hook.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py` 等 21 个文件
  - runtime-model: `python/sglang/srt/configs/deepseek_v41.py`; `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/model_executor/runner/eager_runner.py`; `python/sglang/srt/model_executor/runner_utils/deepep_adapter.py` 等 12 个文件
  - runtime-perf: `python/sglang/kernels/aot/benchmark/bench_rope_fp4.py`; `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/rope_fp4.hip`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/python/sgl_kernel/__init__.py`; `python/sglang/kernels/aot/python/sgl_kernel/elementwise.py`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py` 等 64 个文件
  - tests: `python/sglang/kernels/aot/tests/test_rope_fp4.py`; `test/manual/dsv4/lightop_fp4_indexer.md`; `test/manual/dsv4/test_lightop_fp4_indexer.py`; `test/manual/dsv4/test_rebase_contracts.py`; `test/registered/attention/unittests/dsv4/test_hcu_store_dispatch.py`; `test/registered/attention/unittests/dsv4/test_layer_split_fused_store.py`; `test/registered/cp/test_cp_strategy_unit.py`; `test/registered/kernels/ops/attention/test_dsv41_candidate_blocks_lightop.py` 等 40 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `5343b311c` - Feat/20261102 Sync latest deepseek-v4.1 optimizations to main (#640)

- Full hash: `5343b311c2951da5dcd3617e9a91b76cb9070e04`
- Date/author: 2026-11-03 / YuanYuan
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/dsv4/attn.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_rope_hcu.py`, `python/sglang/kernels/ops/moe/fill_padded_rows.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/configs/model_config.py` 等 93 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/fields/exec_.py`; `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`; `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/encoder/preprocessor.py`; `python/sglang/srt/disaggregation/encoder/receiver.py`; `python/sglang/srt/disaggregation/mooncake/conn.py` 等 26 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/disaggregation/encoder/server.py`; `python/sglang/srt/model_executor/encoder_swa_replay.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/model_executor/runner/eager_runner.py`; `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_fused_mhc.py`; `python/sglang/srt/models/deepseek_v2.py` 等 10 个文件
  - runtime-perf: `python/sglang/kernels/ops/attention/dsv4/attn.py`; `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`; `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_rope_hcu.py`; `python/sglang/kernels/ops/moe/fill_padded_rows.py`; `python/sglang/srt/distributed/device_communicators/cuda_wrapper.py`; `python/sglang/srt/eplb/lplb_hip_waterfill.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/low_ratio_backend_hip.py` 等 31 个文件
  - tests: `test/registered/kernels/ops/attention/test_fp4_indexer.py`; `test/registered/unit/disaggregation/test_encode_receiver.py`; `test/registered/unit/layers/attention/test_dsv41_rope_fq_store.py`; `test/registered/unit/layers/cp/test_interleave_cp_gather_memory.py`; `test/registered/unit/layers/dsv41_hcu_indexq_rounding.json`; `test/registered/unit/layers/moe/test_hcu_compressed_tensors_w4a8_deepep_ll.py`; `test/registered/unit/layers/moe/test_topk_padding_hcu_guard.py`; `test/registered/unit/layers/quantization/test_compressed_tensors_w8a8_int8_hcu_layout.py` 等 26 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
