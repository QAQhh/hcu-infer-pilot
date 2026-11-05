# sglang Mixtral Quark INT4/FP8 MoE 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` | `e9d6aefa9` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | `e9d6aefa9` |
| `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` | `e9d6aefa9` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 1
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |

## 逐 Commit 审计卡

### Commit `e9d6aefa9` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- 完整 hash: `e9d6aefa947699a1edc971ecc2e3fdd2053f525f`
- 时间/作者: 2026-03-30 / lizhigong
- 自动分类: 性能/后端优化
- 主要文件: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py` 等 25 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/server_args.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 4（其中 merge 0）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/layernorm.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/moe/topk.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` | `1e2fec228`, `416bbd9b9`, `8effe1350` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/model_executor/model_runner.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/utils/common.py` | `1e2fec228`, `416bbd9b9`, `8effe1350` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/ops/speculative/cache_locs.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/arg_groups/overrides.py` | `1e2fec228`, `416bbd9b9` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` | `1e2fec228`, `416bbd9b9` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/layers/attention/triton_backend.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/layers/communicator.py` | `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/dp_attention.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/moe/moe_runner/aiter.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/fp8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/moe_wna16.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/mxfp4.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` | `1e2fec228`, `416bbd9b9` |
| ... | 另有 253 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-07-20 | `416bbd9b9` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | chore(hcu): complete platform wording cleanup | `NOTICE`, `THIRD_PARTY_NOTICES.md`, `docs/internal/dcu-main-catchup-20260629-conflict-review.md` 等 28 个文件 |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-09-30 | `8effe1350` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(minimax-m3): optimize prefill and decode on HCU gfx938 (#453) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py` 等 140 个文件 |

### 逐 Commit 审计卡

#### Commit `1e2fec228` - feat(hcu): port runtime and kernel rename

- 完整 hash: `1e2fec228a9a8b1e781c3592eff356eeb8b584ed`
- 时间/作者: 2026-07-20 / tianlinyang77
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/jit_kernel/dsv4/moe.py`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/mxfp8.py` 等 109 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/check_env.py`; `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/fp8_blockwise_gemm.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/mxfp8.py`; `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` 等 80 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `sgl-kernel/tests/test_moe_align.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `416bbd9b9` - chore(hcu): complete platform wording cleanup

- 完整 hash: `416bbd9b953c3ba3dc5faa651bec8d4087ef1998`
- 时间/作者: 2026-07-20 / reverie-hub
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `NOTICE`, `THIRD_PARTY_NOTICES.md`, `docs/internal/dcu-main-catchup-20260629-conflict-review.md`, `docs/internal/dcu-main-catchup-20260703-conflict-review.md`, `docs/internal/dcu-main-catchup-20260706-conflict-review.md`, `docs/internal/dcu-main-catchup-20260709-conflict-review.md`, `docs/internal/dcu-main-catchup-20260710-conflict-review.md`, `docs/internal/dcu-main-catchup-20260712-conflict-review.md` 等 28 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-catchup-20260629-conflict-review.md`; `docs/internal/dcu-main-catchup-20260703-conflict-review.md`; `docs/internal/dcu-main-catchup-20260706-conflict-review.md`; `docs/internal/dcu-main-catchup-20260709-conflict-review.md`; `docs/internal/dcu-main-catchup-20260710-conflict-review.md`; `docs/internal/dcu-main-catchup-20260712-conflict-review.md`; `docs/internal/dcu-main-catchup-20260713-conflict-review.md`; `docs/internal/dcu-main-catchup-20260714-conflict-review.md` 等 17 个文件
  - other: `NOTICE`; `THIRD_PARTY_NOTICES.md`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/pynccl_wrapper.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`; `python/sglang/srt/distributed/device_communicators/pynccl_wrapper.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`
  - tests: `python/sglang/multimodal_gen/test/server/test_server_common.py`; `python/sglang/multimodal_gen/test/server/test_server_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

#### Commit `8effe1350` - feat(minimax-m3): optimize prefill and decode on HCU gfx938 (#453)

- 完整 hash: `8effe13508725f3c871dceb5dfbfbbfc6f959a89`
- 时间/作者: 2026-09-30 / WenQ7
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py`, `python/sglang/benchmark/serving.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/activation.cu`, `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`, `python/sglang/kernels/aot/include/utils.h` 等 140 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/minimax_router_gemv.py`
  - other: `python/sglang/benchmark/serving.py`; `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/eplb_manager.py`; `python/sglang/srt/eplb/expert_distribution.py`; `python/sglang/srt/eplb/expert_location_dispatch.py`; `python/sglang/srt/eplb/load_aware_dispatch.py`; `python/sglang/srt/eplb/lplb_solver.py` 等 19 个文件
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`; `python/sglang/srt/model_executor/cpu_graph_runner.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/runner/eager_runner.py`; `python/sglang/srt/models/llama_eagle3.py` 等 14 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/activation.cu`; `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`; `python/sglang/kernels/aot/include/utils.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`; `python/sglang/kernels/jit/csrc/moe/moe_topk_sigmoid.cuh` 等 65 个文件
  - tests: `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`; `test/registered/attention/test_verify_shared_kv.py`; `test/registered/cp/test_cp_strategy_unit.py`; `test/registered/kernels/ops/attention/test_minimax_prefill_grouped_union.py`; `test/registered/kernels/ops/attention/test_verify_mla_split_policy.py`; `test/registered/kernels/ops/kvcache/test_scaled_fp8_kv_store.py`; `test/registered/kernels/ops/speculative/test_draft_extend_kv_metadata.py` 等 39 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## release/20260825_v0.5.18 到 release_v0.5.18_deepseekv4 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 1（其中 merge 0）
- 分支更新段: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `docs/internal/dcu-main-conflict-ledger.md` | `2c0d45485` |
| `docs/internal/dcu-main-daily-20260721-conflict-review.md` | `2c0d45485` |
| `docs/internal/dcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md` | `2c0d45485` |
| `docs/internal/dcu-v0.5.15-post1-dev-plan.md` | `2c0d45485` |
| `docs/internal/hcu-main-conflict-ledger.md` | `2c0d45485` |
| `docs/internal/hcu-main-daily-20260721-conflict-review.md` | `2c0d45485` |
| `docs/internal/hcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md` | `2c0d45485` |
| `docs/internal/hcu-v0.5.15-post1-dev-plan.md` | `2c0d45485` |
| `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh` | `2c0d45485` |
| `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | `2c0d45485` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` | `2c0d45485` |
| `python/sglang/srt/environ.py` | `2c0d45485` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `2c0d45485` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `2c0d45485` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` | `2c0d45485` |
| `python/sglang/srt/managers/scheduler_components/dp_attn.py` | `2c0d45485` |
| `python/sglang/srt/server_args.py` | `2c0d45485` |
| `scripts/ci/hcu/check_hcu_runtime_text.py` | `2c0d45485` |
| `scripts/ci/hcu/hcu_rename_allowlist.txt` | `2c0d45485` |
| `test/registered/hicache/test_hicache_variants.py` | `2c0d45485` |
| `test/run_suite.py` | `2c0d45485` |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | `2c0d45485` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sanitize HCU platform naming and runtime messages | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-daily-20260721-conflict-review.md`, `docs/internal/dcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md` 等 21 个文件 |

### 逐 Commit 审计卡

#### Commit `2c0d45485` - Sanitize HCU platform naming and runtime messages

- 完整 hash: `2c0d4548542c4aa98ff7b9144f7d597aca889211`
- 时间/作者: 2026-08-21 / reverie-hub
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-daily-20260721-conflict-review.md`, `docs/internal/dcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md`, `docs/internal/dcu-v0.5.15-post1-dev-plan.md`, `docs/internal/hcu-main-conflict-ledger.md`, `docs/internal/hcu-main-daily-20260721-conflict-review.md`, `docs/internal/hcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md`, `docs/internal/hcu-v0.5.15-post1-dev-plan.md` 等 21 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`; `docs/internal/dcu-main-daily-20260721-conflict-review.md`; `docs/internal/dcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md`; `docs/internal/dcu-v0.5.15-post1-dev-plan.md`; `docs/internal/hcu-main-conflict-ledger.md`; `docs/internal/hcu-main-daily-20260721-conflict-review.md`; `docs/internal/hcu-v0.5.15-post1-dev-forward-port-20260722-conflict-review.md`; `docs/internal/hcu-v0.5.15-post1-dev-plan.md`
  - other: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`; `python/sglang/srt/environ.py`; `scripts/ci/hcu/check_hcu_runtime_text.py`; `scripts/ci/hcu/hcu_rename_allowlist.txt`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`; `python/sglang/srt/layers/attention/dsa_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`; `python/sglang/srt/managers/scheduler_components/dp_attn.py`
  - tests: `test/registered/hicache/test_hicache_variants.py`; `test/run_suite.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
