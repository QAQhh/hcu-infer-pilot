# sglang Qwen4-Exp (Qwen3.8-Flash-Next) 本地提交优化历史

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 11（其中 merge 0）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
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
| ... | 另有 74 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-09-03 | `f8bfbc60f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): Qwen3.8 flash next open support (#281) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` 等 100 个文件 |
| 2026-09-12 | `44d9bdc2e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(qwen3_8): support AITER EP and INT8 PLE offload (#350) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` 等 9 个文件 |
| 2026-09-14 | `5817f8359` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4): correct INT8 PLE dequant on GPU path and enable AITER EP offload (#365) | `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/qwen4_exp.py` |
| 2026-09-15 | `b04678a94` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(qwen4): load INT8 MTP fc projections with ReplicatedLinear (#378) | `python/sglang/srt/models/qwen4_exp_mtp.py` |
| 2026-09-17 | `f6a092ec7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4): flatten MTP fc_hidden input before quantized GEMM (#391) | `python/sglang/srt/models/qwen4_exp_mtp.py` |
| 2026-09-20 | `2b8d2b04a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4): support channelwise FP8 and INT8 PLE ngram embeddings (#413) | `python/sglang/srt/models/qwen4_exp.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py` |
| 2026-09-23 | `c3bbbd807` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): serve packed channel INT4 MoE and route QSA MQA through BoltOPs (#434) | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/attention/qsa/boltops_mqa.py`, `python/sglang/srt/layers/attention/qsa/mqa.py` 等 6 个文件 |
| 2026-10-13 | `3b5ca6e33` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4_exp): BF16 PLE offload OOM, channel-FP8/INT8 aiter accuracy, and PLE/MTP decode graph fixes (#513) | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py` 等 27 个文件 |
| 2026-10-16 | `7586e89f5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(qwen4-exp): calibrate QSA e4m3 KV scales during graph capture (#551) | `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` |
| 2026-10-20 | `8bec8605f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(qwen4_exp): fall int8/fp8 PLE pinned alloc back to pageable + hostRegister on HIP OOM (#572) | `python/sglang/srt/models/qwen4_exp.py` |
| 2026-10-21 | `414c323ef` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Perf] qwen4-exp: Enable fp8 e4m3 QSA indexer decode with incremental shadow pool (#574) | `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/mem_cache/qsa_kv_pool.py` 等 4 个文件 |

### 逐 Commit 审计卡

#### Commit `f8bfbc60f` - feat(hcu): Qwen3.8 flash next open support (#281)

- 完整 hash: `f8bfbc60fbb9400391ab7cbf8f1c725bda5c2b59`
- 时间/作者: 2026-09-03 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`, `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh`, `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh`, `python/sglang/kernels/ops/attention/qsa_indexer.py`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/kernels/ops/elementwise/fast_topk.py` 等 100 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/hc_mix_triton.py`; `python/sglang/srt/layers/hyperconnection.py`; `python/sglang/srt/layers/rotary_embedding/mrope_rope_index.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/configs/qwen4_exp.py`; `python/sglang/srt/configs/update_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/pool_configurator.py` 等 15 个文件
  - runtime-perf: `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`; `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`; `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh`; `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh`; `python/sglang/kernels/ops/attention/qsa_indexer.py`; `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`; `python/sglang/kernels/ops/elementwise/fast_topk.py`; `python/sglang/kernels/ops/elementwise/hc_combine.py` 等 45 个文件
  - tests: `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_aime25.py`; `python/sglang/test/simple_eval_aime26.py`; `test/hcu_humaneval_judge.py`; `test/registered/kernels/benchmark/attention/bench_qsa_indexer.py`; `test/registered/kernels/benchmark/elementwise/bench_fast_topk.py`; `test/registered/kernels/benchmark/elementwise/bench_hc_combine.py`; `test/registered/kernels/benchmark/layernorm/bench_grouped_gemma_rmsnorm.py` 等 25 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `44d9bdc2e` - feat(qwen3_8): support AITER EP and INT8 PLE offload (#350)

- 完整 hash: `44d9bdc2e91331a912ac4d613381c8f044893dd0`
- 时间/作者: 2026-09-12 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`, `python/sglang/srt/models/qwen4_exp.py`, `python/sglang/srt/utils/hf_transformers/common.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/utils/hf_transformers/common.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/models/qwen4_exp.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/quantization/unquant.py`
  - tests: `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`; `test/registered/unit/layers/moe/test_aiter_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `5817f8359` - fix(qwen4): correct INT8 PLE dequant on GPU path and enable AITER EP offload (#365)

- 完整 hash: `5817f8359cc0e12df00566e820ed19cccb589d55`
- 时间/作者: 2026-09-14 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/qwen4_exp.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/unquant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b04678a94` - fix(qwen4): load INT8 MTP fc projections with ReplicatedLinear (#378)

- 完整 hash: `b04678a944551b4af5db812e652f36a53eaa89d8`
- 时间/作者: 2026-09-15 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen4_exp_mtp.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/qwen4_exp_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `f6a092ec7` - fix(qwen4): flatten MTP fc_hidden input before quantized GEMM (#391)

- 完整 hash: `f6a092ec7c1693600de5bf530255a91771b00e1c`
- 时间/作者: 2026-09-17 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen4_exp_mtp.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/qwen4_exp_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `2b8d2b04a` - fix(qwen4): support channelwise FP8 and INT8 PLE ngram embeddings (#413)

- 完整 hash: `2b8d2b04a5a730f2b9031342af00932f583003f1`
- 时间/作者: 2026-09-20 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen4_exp.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
  - tests: `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`; `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c3bbbd807` - fix(hcu): serve packed channel INT4 MoE and route QSA MQA through BoltOPs (#434)

- 完整 hash: `c3bbbd8074795a43345da8ff18e11153bc0424af`
- 时间/作者: 2026-09-23 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/attention/qsa/boltops_mqa.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`, `python/sglang/srt/models/qwen4_exp.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/attention/qsa/boltops_mqa.py`; `python/sglang/srt/layers/attention/qsa/mqa.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `3b5ca6e33` - fix(qwen4_exp): BF16 PLE offload OOM, channel-FP8/INT8 aiter accuracy, and PLE/MTP decode graph fixes (#513)

- 完整 hash: `3b5ca6e335086811dbc412c69d77226bad8f2722`
- 时间/作者: 2026-10-13 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` 等 27 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/layers/rotary_embedding/mrope.py`; `python/sglang/srt/speculative/eagle_info.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner_components/misc_utils.py`; `python/sglang/srt/models/qwen4_exp.py`; `python/sglang/srt/models/qwen4_exp_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/qsa/mqa.py`; `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`; `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`; `python/sglang/srt/layers/moe/token_dispatcher/standard.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`; `python/sglang/srt/layers/quantization/unquant.py` 等 16 个文件
  - tests: `python/sglang/test/few_shot_gsm8k.py`; `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`; `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload_tp4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `7586e89f5` - fix(qwen4-exp): calibrate QSA e4m3 KV scales during graph capture (#551)

- 完整 hash: `7586e89f5e06e1ff2a8fb8c0f5a8e8ab3c66bab5`
- 时间/作者: 2026-10-16 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `8bec8605f` - fix(qwen4_exp): fall int8/fp8 PLE pinned alloc back to pageable + hostRegister on HIP OOM (#572)

- 完整 hash: `8bec8605fc9619f491cb9f401256274981037de2`
- 时间/作者: 2026-10-20 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen4_exp.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/qwen4_exp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `414c323ef` - [Perf] qwen4-exp: Enable fp8 e4m3 QSA indexer decode with incremental shadow pool (#574)

- 完整 hash: `414c323ef3681a87dec34ee4427dca788458d2d3`
- 时间/作者: 2026-10-21 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/mem_cache/qsa_kv_pool.py`, `test/registered/kernels/test_qsa.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/qsa/mqa.py`; `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`; `python/sglang/srt/mem_cache/qsa_kv_pool.py`
  - tests: `test/registered/kernels/test_qsa.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## release/20260825_v0.5.18 到 release_v0.5.18_deepseekv4 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 0（其中 merge 0）
- 分支更新段: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

- 该分支更新段内没有归入本桶的本地独有提交。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
