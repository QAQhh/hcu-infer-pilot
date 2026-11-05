# sglang Qwen VLM/Omni/ASR 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/qwen3_vl.py` | `c1d308c60`, `32bd2422e` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 2
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |

## 逐 Commit 审计卡

### Commit `c1d308c60` - 修复qwen3.5-397b-fp8报错问题

- 完整 hash: `c1d308c602379d71d746bc50ed785c2bee05ba99`
- 时间/作者: 2026-04-29 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/index.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `32bd2422e` - 修复qwen3.5模型memory_Async问题

- 完整 hash: `32bd2422e7d17f0cee10413aad4a223ffb25dd74`
- 时间/作者: 2026-04-23 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/sampling/sampling_batch_info.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/sampling/sampling_batch_info.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 3（其中 merge 0）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/environ.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/models/qwen3_5.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/models/qwen3_vl.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/distributed/parallel_state.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/linear/gdn_backend.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/unquant.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/model_executor/model_runner.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_v2.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_v4.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/server_args.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/speculative/draft_utils.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/speculative/eagle_worker_v2.py` | `123e9539e`, `f8bfbc60f` |
| `benchmark/kernels/fused_moe_triton/common_utils.py` | `f8bfbc60f` |
| `python/sglang/check_env.py` | `123e9539e` |
| `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh` | `123e9539e` |
| `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` | `123e9539e` |
| `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh` | `123e9539e` |
| `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh` | `7b3548f97` |
| `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu` | `7b3548f97` |
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
| `python/sglang/kernels/ops/moe/ep_moe_kernels.py` | `7b3548f97` |
| ... | 另有 172 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-08-25 | `7b3548f97` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` 等 48 个文件 |
| 2026-09-03 | `f8bfbc60f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): Qwen3.8 flash next open support (#281) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` 等 100 个文件 |

### 逐 Commit 审计卡

#### Commit `123e9539e` - fix lint: satisfy pre-commit on the forward-port diff

- 完整 hash: `123e9539ea23dde2f1a12b0374c1375bbfb10989`
- 时间/作者: 2026-07-31 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py` 等 91 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py` 等 14 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py` 等 19 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py` 等 56 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_mmlu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `7b3548f97` - fix lint: apply pre-commit fixes across the 20260824 sync diff

- 完整 hash: `7b3548f97409d83b7e7dde4c3ad71e2f30955267`
- 时间/作者: 2026-08-25 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/utils.py` 等 48 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/hardware_backend/npu/utils.py`; `python/sglang/srt/sampling/sampling_batch_info.py`; `python/sglang/srt/speculative/draft_utils.py`; `python/sglang/srt/speculative/eagle_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`; `python/sglang/kernels/ops/moe/ep_moe_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 22 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_server_args.py`; `test/registered/hicache/test_hicache_storage_3fs_backend.py`; `test/registered/openai_server/validation/test_matched_stop.py`; `test/registered/pp/test_pp_single_node.py`; `test/registered/profiling/test_start_profile.py`; `test/registered/unit/entrypoints/openai/test_serving_embedding.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/unit/function_call/test_json_schema_constraint.py` 等 13 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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
