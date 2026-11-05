# sglang Hunyuan3 Preview 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| - | 无本地独有提交 |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 0
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| - | - | - | no local-only commit found | - |

## 逐 Commit 审计卡

### 本地提交检索结论

- 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；当前基线历史中没有保留的本地独有提交。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 10（其中 merge 1）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/hunyuan_v3.py` | `1e2fec228`, `123e9539e`, `32f86c628`, `aa89102b1`, `c2544d8ae`, `a12f08de7`, `f2379b09c` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `1e2fec228`, `a12f08de7`, `f2379b09c` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e`, `a12f08de7` |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `a12f08de7` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `f2379b09c` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `1e2fec228`, `a12f08de7` |
| `python/sglang/srt/disaggregation/prefill.py` | `123e9539e`, `f2379b09c` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
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
| `python/sglang/srt/model_executor/model_runner.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/bailing_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v4.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/mimo_v2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/minimax_m2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/qwen2.py` | `1e2fec228`, `123e9539e` |
| ... | 另有 124 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-08-26 | `32f86c628` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hy3): align LightOp routed scaling factor handling | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-08-26 | `c063dda9a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Merge pull request #234 from liuzj512/fix/hy3-lightop-rsf | 无直接文件变更/merge |
| 2026-09-03 | `aa89102b1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hy3): align MoE forward context with current API (#292) | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-09-04 | `c2544d8ae` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): repair two upstream-refactor call-site regressions (#303) | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-09-07 | `a12f08de7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Hy3 support sp ep (#311) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 9 个文件 |
| 2026-09-14 | `feff664df` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Hy3 sp ep lightop clean (#355) | `python/sglang/srt/layers/moe/utils.py` |
| 2026-09-14 | `f2379b09c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat:Hy3 support sp ep (#360) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` 等 5 个文件 |
| 2026-11-03 | `2c841655f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): limit INT8 marlin MoE bypass to DeepSeek so HY3 keeps lightop (#639) | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |

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

#### Commit `32f86c628` - fix(hy3): align LightOp routed scaling factor handling

- 完整 hash: `32f86c628bcd8baebe8eb2b2a6a0b3924c73f566`
- 时间/作者: 2026-08-26 / liuzj512
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c063dda9a` - Merge pull request #234 from liuzj512/fix/hy3-lightop-rsf

- 完整 hash: `c063dda9a0f7dfdcab84c15cd7c1baa27cb860e9`
- 时间/作者: 2026-08-26 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `aa89102b1` - fix(hy3): align MoE forward context with current API (#292)

- 完整 hash: `aa89102b1dacca122aec18d43547cb86e979d217`
- 时间/作者: 2026-09-03 / liuzj512
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c2544d8ae` - fix(hcu): repair two upstream-refactor call-site regressions (#303)

- 完整 hash: `c2544d8ae1a60d2b91ba275ed997bf1da4e1e833`
- 时间/作者: 2026-09-04 / Jane
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `a12f08de7` - Hy3 support sp ep (#311)

- 完整 hash: `a12f08de78065aa75f5fefa6e6c17c738d022e53`
- 时间/作者: 2026-09-07 / Jane
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/common.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/fake/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
  - tests: `test/registered/unit/models/test_hunyuan_v3_sp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `feff664df` - Hy3 sp ep lightop clean (#355)

- 完整 hash: `feff664dfee687c0238ee95f5980467334093f29`
- 时间/作者: 2026-09-14 / liuzj512
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f2379b09c` - feat:Hy3 support sp ep (#360)

- 完整 hash: `f2379b09c820f2ad5e9217af1c8a21a20b7b3d73`
- 时间/作者: 2026-09-14 / Jane
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2c841655f` - fix(hcu): limit INT8 marlin MoE bypass to DeepSeek so HY3 keeps lightop (#639)

- 完整 hash: `2c841655fe7852cde42eaaff2c1d414cf4038df1`
- 时间/作者: 2026-11-03 / lipenghui
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
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
