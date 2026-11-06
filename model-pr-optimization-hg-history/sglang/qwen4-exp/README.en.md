# sglang Qwen4-Exp (Qwen3.8-Flash-Next) Local Commit Optimization History

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 11 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/qwen4_exp.py` | `f8bfbc60f`, `44d9bdc2e`, `5817f8359`, `2b8d2b04a`, `c3bbbd807`, `3b5ca6e33`, `8bec8605f` |
| `python/sglang/srt/layers/attention/qsa/mqa.py` | `f8bfbc60f`, `c3bbbd807`, `3b5ca6e33`, `414c323ef` |
| `python/sglang/srt/layers/quantization/unquant.py` | `f8bfbc60f`, `44d9bdc2e`, `5817f8359`, `3b5ca6e33` |
| `python/sglang/srt/models/qwen4_exp_mtp.py` | `f8bfbc60f`, `b04678a94`, `f6a092ec7`, `3b5ca6e33` |
| `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py` | `f8bfbc60f`, `44d9bdc2e`, `2b8d2b04a`, `3b5ca6e33` |
| `python/sglang/srt/layers/attention/qsa/qsa_indexer.py` | `f8bfbc60f`, `3b5ca6e33`, `414c323ef` |
| `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` | `f8bfbc60f`, `3b5ca6e33`, `7586e89f5` |
| `python/sglang/srt/mem_cache/qsa_kv_pool.py` | `f8bfbc60f`, `3b5ca6e33`, `414c323ef` |
| `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py` | `f8bfbc60f`, `2b8d2b04a`, `3b5ca6e33` |
| `python/sglang/srt/arg_groups/overrides.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/configs/__init__.py` | `f8bfbc60f`, `44d9bdc2e` |
| `python/sglang/srt/configs/model_config.py` | `f8bfbc60f`, `44d9bdc2e` |
| `python/sglang/srt/layers/moe/moe_runner/aiter.py` | `f8bfbc60f`, `44d9bdc2e` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `f8bfbc60f`, `c3bbbd807` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py` | `f8bfbc60f`, `44d9bdc2e` |
| `python/sglang/srt/server_args.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/speculative/eagle_worker_v2.py` | `f8bfbc60f`, `3b5ca6e33` |
| `python/sglang/srt/utils/hf_transformers/common.py` | `f8bfbc60f`, `44d9bdc2e` |
| `test/registered/kernels/test_qsa.py` | `f8bfbc60f`, `414c323ef` |
| `benchmark/kernels/fused_moe_triton/common_utils.py` | `f8bfbc60f` |
| `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/ops/attention/qsa_indexer.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/elementwise/fast_topk.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/elementwise/hc_combine.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/elementwise/hc_mix.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/gemm/flashinfer_pr4266_dense_bf16_gemm_sm100_splitk.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/layernorm/grouped_gemma_rmsnorm.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | `c3bbbd807` |
| `python/sglang/kernels/ops/qwen4_ple.py` | `f8bfbc60f` |
| `python/sglang/srt/arg_groups/speculative_hook.py` | `f8bfbc60f` |
| `python/sglang/srt/configs/qwen3_5.py` | `f8bfbc60f` |
| ... | 74 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-09-03 | `f8bfbc60f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): Qwen3.8 flash next open support (#281) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` and 100 files in total |
| 2026-09-12 | `44d9bdc2e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(qwen3_8): support AITER EP and INT8 PLE offload (#350) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` and 9 files in total |
| 2026-09-14 | `5817f8359` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4): correct INT8 PLE dequant on GPU path and enable AITER EP offload (#365) | `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/qwen4_exp.py` |
| 2026-09-15 | `b04678a94` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(qwen4): load INT8 MTP fc projections with ReplicatedLinear (#378) | `python/sglang/srt/models/qwen4_exp_mtp.py` |
| 2026-09-17 | `f6a092ec7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4): flatten MTP fc_hidden input before quantized GEMM (#391) | `python/sglang/srt/models/qwen4_exp_mtp.py` |
| 2026-09-20 | `2b8d2b04a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4): support channelwise FP8 and INT8 PLE ngram embeddings (#413) | `python/sglang/srt/models/qwen4_exp.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py` |
| 2026-09-23 | `c3bbbd807` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): serve packed channel INT4 MoE and route QSA MQA through BoltOPs (#434) | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/attention/qsa/boltops_mqa.py`, `python/sglang/srt/layers/attention/qsa/mqa.py` and 6 files in total |
| 2026-10-13 | `3b5ca6e33` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4_exp): BF16 PLE offload OOM, channel-FP8/INT8 aiter accuracy, and PLE/MTP decode graph fixes (#513) | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py` and 27 files in total |
| 2026-10-16 | `7586e89f5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(qwen4-exp): calibrate QSA e4m3 KV scales during graph capture (#551) | `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` |
| 2026-10-20 | `8bec8605f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4_exp): fall int8/fp8 PLE pinned alloc back to pageable + hostRegister on HIP OOM (#572) | `python/sglang/srt/models/qwen4_exp.py` |
| 2026-10-21 | `414c323ef` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Perf] qwen4-exp: Enable fp8 e4m3 QSA indexer decode with incremental shadow pool (#574) | `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/mem_cache/qsa_kv_pool.py` and 4 files in total |

### Per-Commit Audit Cards

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

#### Commit `5817f8359` - fix(qwen4): correct INT8 PLE dequant on GPU path and enable AITER EP offload (#365)

- Full hash: `5817f8359cc0e12df00566e820ed19cccb589d55`
- Date/author: 2026-09-14 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/qwen4_exp.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/unquant.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b04678a94` - fix(qwen4): load INT8 MTP fc projections with ReplicatedLinear (#378)

- Full hash: `b04678a944551b4af5db812e652f36a53eaa89d8`
- Date/author: 2026-09-15 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen4_exp_mtp.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/qwen4_exp_mtp.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `f6a092ec7` - fix(qwen4): flatten MTP fc_hidden input before quantized GEMM (#391)

- Full hash: `f6a092ec7c1693600de5bf530255a91771b00e1c`
- Date/author: 2026-09-17 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen4_exp_mtp.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/qwen4_exp_mtp.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `2b8d2b04a` - fix(qwen4): support channelwise FP8 and INT8 PLE ngram embeddings (#413)

- Full hash: `2b8d2b04a5a730f2b9031342af00932f583003f1`
- Date/author: 2026-09-20 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen4_exp.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
  - tests: `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`; `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `c3bbbd807` - fix(hcu): serve packed channel INT4 MoE and route QSA MQA through BoltOPs (#434)

- Full hash: `c3bbbd8074795a43345da8ff18e11153bc0424af`
- Date/author: 2026-09-23 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/attention/qsa/boltops_mqa.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`, `python/sglang/srt/models/qwen4_exp.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/attention/qsa/boltops_mqa.py`; `python/sglang/srt/layers/attention/qsa/mqa.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `3b5ca6e33` - fix(qwen4_exp): BF16 PLE offload OOM, channel-FP8/INT8 aiter accuracy, and PLE/MTP decode graph fixes (#513)

- Full hash: `3b5ca6e335086811dbc412c69d77226bad8f2722`
- Date/author: 2026-10-13 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` 等 27 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/layers/rotary_embedding/mrope.py`; `python/sglang/srt/speculative/eagle_info.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner_components/misc_utils.py`; `python/sglang/srt/models/qwen4_exp.py`; `python/sglang/srt/models/qwen4_exp_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/qsa/mqa.py`; `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`; `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`; `python/sglang/srt/layers/moe/token_dispatcher/standard.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`; `python/sglang/srt/layers/quantization/unquant.py` 等 16 个文件
  - tests: `python/sglang/test/few_shot_gsm8k.py`; `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`; `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `7586e89f5` - fix(qwen4-exp): calibrate QSA e4m3 KV scales during graph capture (#551)

- Full hash: `7586e89f5e06e1ff2a8fb8c0f5a8e8ab3c66bab5`
- Date/author: 2026-10-16 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `8bec8605f` - fix(qwen4_exp): fall int8/fp8 PLE pinned alloc back to pageable + hostRegister on HIP OOM (#572)

- Full hash: `8bec8605fc9619f491cb9f401256274981037de2`
- Date/author: 2026-10-20 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen4_exp.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `414c323ef` - [Perf] qwen4-exp: Enable fp8 e4m3 QSA indexer decode with incremental shadow pool (#574)

- Full hash: `414c323ef3681a87dec34ee4427dca788458d2d3`
- Date/author: 2026-10-21 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/mem_cache/qsa_kv_pool.py`, `test/registered/kernels/test_qsa.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/qsa/mqa.py`; `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`; `python/sglang/srt/mem_cache/qsa_kv_pool.py`
  - tests: `test/registered/kernels/test_qsa.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
