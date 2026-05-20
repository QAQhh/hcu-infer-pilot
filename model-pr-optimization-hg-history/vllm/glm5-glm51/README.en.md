# vllm GLM-5/5.1 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| - | No matching implementation file on current main |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 9
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-05-13 | `8f95efb7b` | 性能/后端优化 | [FEATURE] GLM5 W4A8 EP 低延迟模式适配 | `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-04-24 | `ba6f21012` | 性能/后端优化 | [FEATURE] GLM5 FP8 EP适配 | `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/config.py` |
| 2026-04-14 | `6efaf21a0` | 性能/后端优化 | [BUGFIX]修复deepgemm算子导致的GLM5 W8A8精度问题。 | `tests/kernels/moe/untest_silu_mul_fp8_quant_deep_gemm.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py` |
| 2026-04-08 | `bcb2ba6c2` | 调度/缓存/PD | [FEATURE] DuSwiftConnector support glm5 model PD （attention sparse_attn_indexer layer_name change ） | `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-26 | `714c12dad` | 性能/后端优化 | Merge branch 'wanghl_glm5_kernel_opt' into 'v0.15.1-dev' |  |
| 2026-03-12 | `3b38e285e` | 缺陷修复 | Merge branch 'v0.15.1-dev-lxh-glm5-fix' into 'v0.15.1-dev' |  |
| 2026-03-12 | `5b9ad7221` | 缺陷修复 | Fix：GLM-5量化模型mla_attention layout修复&&sparse_attn fp8支持 | `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-11 | `66979358b` | 缺陷修复 | feat:修复dsa的mqa接口兼容glm5 | `vllm/model_executor/layers/sparse_attn_indexer.py` |
| 2026-03-11 | `03a3c5226` | 性能/后端优化 | Fix：Extend MAX_VPT from 32 to 256 to accommodate large-scale MoE models (e.g., GLM-5-quantized model). | `csrc/moe/moe_fused_gate.cu` |

## Per-Commit Audit Cards

### Commit `8f95efb7b` - [FEATURE] GLM5 W4A8 EP 低延迟模式适配

- Full hash: `8f95efb7bbce02ad735b6e3a06a4471c54bff300`
- Date/author: 2026-05-13 / chenhw5
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py`, `vllm/model_executor/layers/quantization/utils/w4a8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/quantization/slimquant_w4a8_marlin.py`; `vllm/model_executor/layers/quantization/utils/w4a8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ba6f21012` - [FEATURE] GLM5 FP8 EP适配

- Full hash: `ba6f210128913946db49f8376d6e40f7241cb981`
- Date/author: 2026-04-24 / chenhw5
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/deepep_ll_prepare_finalize.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/all2all_utils.py`; `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/deepep_ll_prepare_finalize.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6efaf21a0` - [BUGFIX]修复deepgemm算子导致的GLM5 W8A8精度问题。

- Full hash: `6efaf21a099bc08f8e39b2325f632a93a5cca86f`
- Date/author: 2026-04-14 / chenhw5
- Auto category: 性能/后端优化
- Main files: `tests/kernels/moe/untest_silu_mul_fp8_quant_deep_gemm.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`, `vllm/utils/import_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/utils/import_utils.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`
  - tests: `tests/kernels/moe/untest_silu_mul_fp8_quant_deep_gemm.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bcb2ba6c2` - [FEATURE] DuSwiftConnector support glm5 model PD （attention sparse_attn_indexer layer_name change ）

- Full hash: `bcb2ba6c247f1e6863e292e30a3da7202f1dc9e8`
- Date/author: 2026-04-08 / xiabo
- Auto category: 调度/缓存/PD
- Main files: `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
  - runtime-perf: `vllm/distributed/kv_transfer/kv_connector/v1/du/du_swift_connector.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `714c12dad` - Merge branch 'wanghl_glm5_kernel_opt' into 'v0.15.1-dev'

- Full hash: `714c12daddb5e86c07625b14d839e0d39e968e2c`
- Date/author: 2026-03-26 / wangmin6
- Auto category: 性能/后端优化
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `3b38e285e` - Merge branch 'v0.15.1-dev-lxh-glm5-fix' into 'v0.15.1-dev'

- Full hash: `3b38e285efc11930c1272a16beaf246215b821c5`
- Date/author: 2026-03-12 / wangmin6
- Auto category: 缺陷修复
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `5b9ad7221` - Fix：GLM-5量化模型mla_attention layout修复&&sparse_attn fp8支持

- Full hash: `5b9ad722132a1a838ff210b6cd3c6442c7fe3dc5`
- Date/author: 2026-03-12 / lixh6
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `66979358b` - feat:修复dsa的mqa接口兼容glm5

- Full hash: `66979358b38aeb9b3a140109a7fb0ec3ac2d0f3a`
- Date/author: 2026-03-11 / liuchy5
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/layers/sparse_attn_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/sparse_attn_indexer.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `03a3c5226` - Fix：Extend MAX_VPT from 32 to 256 to accommodate large-scale MoE models (e.g., GLM-5-quantized model).

- Full hash: `03a3c52266eae1ff2d701c05a508378b7bba79b8`
- Date/author: 2026-03-11 / lixh6
- Auto category: 性能/后端优化
- Main files: `csrc/moe/moe_fused_gate.cu`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `csrc/moe/moe_fused_gate.cu`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
