# sglang MiMo V2 Flash 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/mimo_v2_flash.py` | `1924c63d6` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 3
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-05-14 | `1924c63d6` | 性能/后端优化 | [BUG FIX] fix pp parallel bug for mimo model | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py` |
| 2026-04-14 | `47165f0fc` | 性能/后端优化 | [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash) | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-04-03 | `30f4f1133` | 性能/后端优化 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` |

## 逐 Commit 审计卡

### Commit `1924c63d6` - [BUG FIX] fix pp parallel bug for mimo model

- 完整 hash: `1924c63d64f72fbbb4623956150b176dcdcde29c`
- 时间/作者: 2026-05-14 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/models/mimo_v2_flash.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `47165f0fc` - [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash)

- 完整 hash: `47165f0fcf27c6d38edd4d230d750311f98ba387`
- 时间/作者: 2026-04-14 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `30f4f1133` - support mimo-v2-flash-int4 with triton attn

- 完整 hash: `30f4f1133f9a4d57d8cd3b971230048e0cf15b04`
- 时间/作者: 2026-04-03 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## v0.5.8_dev 到 v0.5.12_dev 本地独有提交补充

### 覆盖说明

- 来源索引: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- 来源工作树: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交。
- 本章节提交数: 2
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-04-03 | `968d82d7f` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` 等 4 个文件 |
| 2026-04-03 | `b4a02fae7` | `v0.5.9_dev..v0.5.10_dev` | 模型支持/运行时入口 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` 等 4 个文件 |

### 逐 Commit 审计卡

#### Commit `968d82d7f` - support mimo-v2-flash-int4 with triton attn

- 完整 hash: `968d82d7f8205f78236c345136a7cbf363f8fd9d`
- 时间/作者: 2026-04-03 / shiqiang
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- 重复/备注: 重复 patch-id: 与 v0.5.9_dev..v0.5.10_dev 的 b4a02fae7 相同
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `b4a02fae7` - support mimo-v2-flash-int4 with triton attn

- 完整 hash: `b4a02fae7e09fe663276907645cb77af61c25198`
- 时间/作者: 2026-04-03 / shiqiang
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- 重复/备注: 重复 patch-id: 与 v0.5.8_dev..v0.5.9_dev 的 968d82d7 相同
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->

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
| `python/sglang/srt/models/mimo_v2.py` | `1e2fec228`, `123e9539e`, `cb50fb561` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `1e2fec228`, `cb50fb561` |
| `python/sglang/srt/layers/layernorm.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/topk.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/fp8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/moe_wna16.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/mxfp4.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_fp8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_int8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/model_executor/model_runner.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/bailing_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v4.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/hunyuan_v3.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/mimo_v2_nextn.py` | `cb50fb561`, `4af5b4974` |
| `python/sglang/srt/models/minimax_m2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/qwen2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/qwen3.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/qwen3_5.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/qwen3_moe.py` | `1e2fec228`, `123e9539e` |
| ... | 另有 120 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-09-11 | `cb50fb561` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support mimo v2 flash channel fp8 for 5.18 (#343) | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py` |
| 2026-09-14 | `4af5b4974` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Mimo v2 pro update and bug fix (#354) | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/mimo_v2_nextn.py` |

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

#### Commit `cb50fb561` - feat: support mimo v2 flash channel fp8 for 5.18 (#343)

- 完整 hash: `cb50fb561aa174070f79fa98f7bd1638660970d6`
- 时间/作者: 2026-09-11 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/mimo_v2.py`; `python/sglang/srt/models/mimo_v2_nextn.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4af5b4974` - Mimo v2 pro update and bug fix (#354)

- 完整 hash: `4af5b4974cc38a4e57896270d069b526e2db00ba`
- 时间/作者: 2026-09-14 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/mimo_v2_nextn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/mimo_v2_nextn.py`
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`
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
