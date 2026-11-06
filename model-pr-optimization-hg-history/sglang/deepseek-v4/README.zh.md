# sglang DeepSeek V4 本地提交优化历史

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

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## v0.5.8_dev 到 v0.5.12_dev 本地独有提交补充

### 覆盖说明

- 来源索引: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- 来源工作树: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交。
- 本章节提交数: 17
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-04-28 | `14671daae` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | patch for deepseekv4 | `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h` 等 11 个文件 |
| 2026-04-28 | `24f89924a` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | Ignore error exceptions and allow the service to start. | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` 等 7 个文件 |
| 2026-04-28 | `bc0809390` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix jit for compress_forward | `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` 等 4 个文件 |
| 2026-04-28 | `dbd0d5c1d` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix jit for compress_fused_norm_rope_inplace | `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/attention/dsv4/compressor.py` |
| 2026-04-29 | `66bb0d501` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | [compile fix] rename all '__grid_constant__' with global SGL_GRID_CONSTANT to avoid compiling issues | `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh` 等 16 个文件 |
| 2026-04-29 | `6f3103454` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | 修复CompressorPrefillPlan中使用jit kernel编译deepseek_v4/common.cuh时报错的问题 | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/include/sgl_kernel/utils.h` |
| 2026-04-29 | `cf0af79d2` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix topk_transform_512 jit | `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`, `python/sglang/srt/layers/attention/dsv4/metadata.py` 等 6 个文件 |
| 2026-04-30 | `51f4fe3e1` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix mhc | `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-04-30 | `53c8956fd` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | [compile fix] replace cuda_fp8 with hip/hip_fp8 to avoid jit compile errors | `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh` 等 4 个文件 |
| 2026-04-30 | `83e281dc0` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | first version for fp8 block | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-05-06 | `0c411213f` | `v0.5.11_dev..v0.5.12_dev` | 性能/后端优化 | 删除deepgemm meta | `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-05-07 | `070988441` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | support fp8 channel-wise load weight | `python/sglang/srt/models/deepseek_v4.py` |
| 2026-05-09 | `0dbd5074d` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | 接入lightop的Marlin MOE W8A8算子 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-05-09 | `452e413c1` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | [bug fix] fix the dpsk-v4 mtp start issue, but multi-request input is failed still | `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-05-09 | `7ecb521af` | `v0.5.11_dev..v0.5.12_dev` | 调度/缓存/PD | 1. add aiter moe; 2. split attn for prefill/decode | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 4 个文件 |
| 2026-05-20 | `139c5c455` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | backup dcu deepseek v4 debug state | `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/mhc.py` |
| 2026-05-21 | `b306ccfe4` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | 适配deepseekv4 | `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh` 等 19 个文件 |

### 逐 Commit 审计卡

#### Commit `14671daae` - patch for deepseekv4

- 完整 hash: `14671daae3602521808d74d3a8879cc525fbb2f3`
- 时间/作者: 2026-04-28 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 11 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/layers/attention/dsv4/metadata.py`; `python/sglang/srt/layers/mhc.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 10 个文件
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `24f89924a` - Ignore error exceptions and allow the service to start.

- 完整 hash: `24f89924ad7b1c8bf3638e369185562510848b14`
- 时间/作者: 2026-04-28 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `bc0809390` - fix jit for compress_forward

- 完整 hash: `bc0809390ff44101388966a545729bcfb47e4a33`
- 时间/作者: 2026-04-28 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `dbd0d5c1d` - fix jit for compress_fused_norm_rope_inplace

- 完整 hash: `dbd0d5c1d5487d095e0a9dcc2f85fccacb3f2fa4`
- 时间/作者: 2026-04-28 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/attention/dsv4/compressor.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/srt/layers/attention/dsv4/compressor.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `66bb0d501` - [compile fix] rename all '__grid_constant__' with global SGL_GRID_CONSTANT to avoid compiling issues

- 完整 hash: `66bb0d501453dbc6d3cdab54e50e120a1e49462c`
- 时间/作者: 2026-04-29 / YuanYuan
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/rmsnorm.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh` 等 16 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/rmsnorm.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh` 等 16 个文件
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `6f3103454` - 修复CompressorPrefillPlan中使用jit kernel编译deepseek_v4/common.cuh时报错的问题

- 完整 hash: `6f31034548aa5e75156ca0d11c790b52cfdb2e81`
- 时间/作者: 2026-04-29 / lipenghui
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/include/sgl_kernel/utils.h`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/jit_kernel/include/sgl_kernel/utils.h`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `cf0af79d2` - fix topk_transform_512 jit

- 完整 hash: `cf0af79d2b9e5d7dde3034ae033148484137d255`
- 时间/作者: 2026-04-29 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`; `python/sglang/srt/layers/attention/dsv4/metadata.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `51f4fe3e1` - fix mhc

- 完整 hash: `51f4fe3e15958a80d5b010553e39773306ae770b`
- 时间/作者: 2026-04-30 / flyingdown
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/mhc.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `53c8956fd` - [compile fix] replace cuda_fp8 with hip/hip_fp8 to avoid jit compile errors

- 完整 hash: `53c8956fd09e16724610ba75e79396b68c1ea1e9`
- 时间/作者: 2026-04-30 / yuanyuan
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `83e281dc0` - first version for fp8 block

- 完整 hash: `83e281dc0fba863706e4c153364b92bf890b7a4c`
- 时间/作者: 2026-04-30 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`
  - other: `python/sglang/srt/managers/tp_worker.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `0c411213f` - 删除deepgemm meta

- 完整 hash: `0c411213f0a7d161d8b123c0cbae4937fb47ac2c`
- 时间/作者: 2026-05-06 / flyingdown
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/model_executor/model_runner.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- 验证与风险: 涉及性能或后端路径；复用前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `070988441` - support fp8 channel-wise load weight

- 完整 hash: `070988441ce2e10efb6b1f92b6eabf26c01985bd`
- 时间/作者: 2026-05-07 / flyingdown
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `0dbd5074d` - 接入lightop的Marlin MOE W8A8算子

- 完整 hash: `0dbd5074d1c37570390f3edd2af0460d6160867e`
- 时间/作者: 2026-05-09 / lj1999
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `452e413c1` - [bug fix] fix the dpsk-v4 mtp start issue, but multi-request input is failed still

- 完整 hash: `452e413c154ce1524a19ca3edf1c2a11a18fa059`
- 时间/作者: 2026-05-09 / yuanyuan
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`, `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `7ecb521af` - 1. add aiter moe; 2. split attn for prefill/decode

- 完整 hash: `7ecb521af66be463683f38b2ff26f9db46b477f9`
- 时间/作者: 2026-05-09 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`
  - other: `python/sglang/srt/environ.py`
- 验证与风险: 涉及调度、缓存、PD 或 MTP 路径；需要验证 prefill/decode 时序、首 token 正确性、并发与长上下文稳定性。

#### Commit `139c5c455` - backup dcu deepseek v4 debug state

- 完整 hash: `139c5c455ad3b6d448b812be3ce633af6fa64d2f`
- 时间/作者: 2026-05-20 / lizhigong
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/mhc.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`; `python/sglang/srt/layers/mhc.py`
  - other: `python/sglang/srt/environ.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `b306ccfe4` - 适配deepseekv4

- 完整 hash: `b306ccfe4ef332f3c1b5c5cec620f6ba64998ebd`
- 时间/作者: 2026-05-21 / lizhigong
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 19 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`; `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 18 个文件
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 48（其中 merge 1）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/deepseek_v4.py` | `94659d14a`, `1b2694156`, `249a70dbe`, `fc241f4ad`, `ad2ff869c`, `6bf9d1872`, `84a8a08ac`, `1e2fec228`, `470ae85b5`, `25ffedc22`, `123e9539e`, `e7106de94`, ... (25 total) |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e`, `59fb95973`, `7b3548f97`, `726db6820`, `c18c8d4bb`, `c338e5fd0`, `551a71d4d`, `055812e0d`, `fc7ebb3d0`, `602fb4a30`, `ea1c297dc`, ... (15 total) |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `ad2ff869c`, `d703c086f`, `1e2fec228`, `123e9539e`, `725659198`, `a596be0dc`, `7b3548f97`, `726db6820`, `ddbbccde8`, `1316e9887`, `c338e5fd0`, `4f224d2b6`, ... (15 total) |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `c4cc0a73b`, `1e2fec228`, `123e9539e`, `59fb95973`, `7b3548f97`, `726db6820`, `4c367dbd5`, `4f224d2b6`, `6bf8197dd`, `055812e0d`, `2ed02ec34`, `ea1c297dc`, ... (14 total) |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `3d0f94345`, `726db6820`, `ddbbccde8`, `551a71d4d`, `4f224d2b6`, `6bf8197dd`, `fc7ebb3d0`, `2ed02ec34` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1b2694156`, `1e2fec228`, `123e9539e`, `e7106de94`, `3d0f94345`, `7b3548f97`, `726db6820`, `602fb4a30`, `76e87a951` |
| `python/sglang/srt/models/deepseek_v2.py` | `b5f9777d2`, `1e2fec228`, `123e9539e`, `3d0f94345`, `7b3548f97`, `551a71d4d`, `37f23f55a`, `602fb4a30`, `76e87a951` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `1e2fec228`, `3d0f94345`, `726db6820`, `ddbbccde8`, `4f224d2b6`, `6bf8197dd`, `2ed02ec34`, `100533036` |
| `python/sglang/srt/disaggregation/prefill.py` | `123e9539e`, `3d0f94345`, `726db6820`, `ddbbccde8`, `4f224d2b6`, `6bf8197dd`, `2ed02ec34`, `100533036` |
| `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` | `ad2ff869c`, `59fb95973`, `726db6820`, `ddbbccde8`, `4f224d2b6`, `6bf8197dd`, `fc7ebb3d0`, `2ed02ec34` |
| `docs/internal/dcu-main-conflict-ledger.md` | `249a70dbe`, `ad2ff869c`, `84a8a08ac`, `b5f9777d2`, `25ffedc22`, `a596be0dc`, `a0840f493` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `5b19ad464`, `1e2fec228`, `a596be0dc`, `59fb95973`, `7b3548f97`, `726db6820`, `c18c8d4bb` |
| `python/sglang/srt/layers/attention/dsv4/compressor_v2.py` | `59fb95973`, `726db6820`, `c18c8d4bb`, `4c367dbd5`, `4f224d2b6`, `6bf8197dd`, `2ed02ec34` |
| `python/sglang/srt/layers/moe/mega_moe.py` | `94659d14a`, `1e2fec228`, `e876bb9ff`, `470ae85b5`, `25ffedc22`, `7b3548f97`, `23d1def83` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `3d0f94345`, `726db6820`, `4f224d2b6`, `6bf8197dd`, `2ed02ec34` |
| `python/sglang/srt/arg_groups/overrides.py` | `1e2fec228`, `e876bb9ff`, `470ae85b5`, `551a71d4d`, `4ba29d557` |
| `python/sglang/srt/disaggregation/common/conn.py` | `3d0f94345`, `726db6820`, `4f224d2b6`, `6bf8197dd`, `2ed02ec34` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e`, `7b3548f97`, `ddbbccde8`, `c18c8d4bb` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `1e2fec228`, `25ffedc22`, `123e9539e`, `726db6820`, `4c367dbd5` |
| `python/sglang/srt/managers/scheduler.py` | `123e9539e`, `3d0f94345`, `726db6820`, `100533036`, `4ba29d557` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `25ffedc22`, `123e9539e`, `7b3548f97`, `ddbbccde8` |
| `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py` | `4f224d2b6`, `6bf8197dd`, `fc7ebb3d0`, `2ed02ec34`, `100533036` |
| `python/sglang/srt/model_executor/model_runner.py` | `fc241f4ad`, `1e2fec228`, `123e9539e`, `3d0f94345`, `7b3548f97` |
| `python/sglang/srt/utils/common.py` | `1e2fec228`, `e876bb9ff`, `470ae85b5`, `a596be0dc`, `7b3548f97` |
| `python/sglang/srt/arg_groups/speculative_hook.py` | `e7106de94`, `726db6820`, `ddbbccde8`, `551a71d4d` |
| `python/sglang/srt/managers/scheduler_pp_mixin.py` | `3d0f94345`, `7b3548f97`, `726db6820`, `ddbbccde8` |
| `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py` | `4f224d2b6`, `6bf8197dd`, `fc7ebb3d0`, `2ed02ec34` |
| `python/sglang/jit_kernel/include/sgl_kernel/tensor.h` | `f2d0e86d7`, `1e2fec228`, `a596be0dc` |
| `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh` | `551a71d4d`, `4ba29d557`, `76e87a951` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `25ffedc22`, `123e9539e` |
| `python/sglang/srt/arg_groups/deepseek_v4_hook.py` | `94659d14a`, `e876bb9ff`, `ddbbccde8` |
| `python/sglang/srt/disaggregation/utils.py` | `3d0f94345`, `726db6820`, `ddbbccde8` |
| `python/sglang/srt/distributed/bootstrap.py` | `4f224d2b6`, `6bf8197dd`, `2ed02ec34` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `5b19ad464`, `1e2fec228`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` | `1e2fec228`, `551a71d4d`, `76e87a951` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `1e2fec228`, `551a71d4d`, `4ba29d557` |
| `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | `123e9539e`, `726db6820`, `76e87a951` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `1e2fec228`, `123e9539e`, `76e87a951` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `1e2fec228`, `123e9539e`, `726db6820` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `1e2fec228`, `25ffedc22`, `123e9539e` |
| ... | 另有 293 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-17 | `94659d14a` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [dsv4] cp support megamoe | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-06-24 | `5b19ad464` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [fix(deepseek-v4)]: keep DCU on non-HIP attention backend + compressor | `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py` |
| 2026-06-24 | `1b2694156` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | [fix(deepseek-v4)]: remove unused codes and use ScheduleBatch extend_lens/prefix_lens in init_new | `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-06-30 | `c4cc0a73b` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(dsv4): preserve DCU elementwise and topk paths | `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` |
| 2026-06-30 | `f2d0e86d7` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(dsv4): repair DCU sgl-kernel and JIT build | `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `sgl-kernel/setup_hip.py` |
| 2026-07-02 | `249a70dbe` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [Addition] deliver one validation doc and support multi-stream in hip backend | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-07-03 | `fc241f4ad` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | [BugFix] Sync to official changes to remove first pre-warmup of mHC | `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-07-06 | `ad2ff869c` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] Backport partial bugfixes from C10 and also have to assign SGLANG_USE_AITER_AG=0 to ensure accuracy now | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` 等 9 个文件 |
| 2026-07-13 | `6bf9d1872` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(dcu): reconcile DSV4 prewarm and fused Q imports | `python/sglang/srt/models/deepseek_v4.py` |
| 2026-07-14 | `84a8a08ac` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | [BugFix] skip pre-warmup of mHC for DCU and update validation docs | `docs/internal/dcu-main-catchup-20260703-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-07-14 | `b5f9777d2` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | Fix DCU DSV4 hash top-k router dtype | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-07-17 | `d703c086f` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] Fix the accuracy issues of DeepSeek-V4 in TP/CP/DP/EP | `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/mem_cache/allocator/paged.py` |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-07-21 | `e876bb9ff` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [FEAT] support cp+MegaMoE in prefill w/o cuda-graph | `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py` 等 5 个文件 |
| 2026-07-21 | `470ae85b5` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | style: apply pre-commit formatting (black/isort/ruff) | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` 等 4 个文件 |
| 2026-07-29 | `25ffedc22` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(hcu): repair forward-port compatibility gaps | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` 等 15 个文件 |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-07-31 | `e7106de94` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | V0.5.15.post1 dev to support dspark on HCU (#142) | `python/sglang/benchmark/dspark_sps_profiler.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/overlap_utils.py` 等 8 个文件 |
| 2026-08-06 | `3d0f94345` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(hcu): fully revert files owned by the skipped source commits | `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py` 等 20 个文件 |
| 2026-08-06 | `725659198` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | Revert "fix assert when mtp enable and step >1" | `python/sglang/srt/layers/attention/deepseek_v4_backend.py` |
| 2026-07-21 | `a596be0dc` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] Fix DeepSeek-V4 pure-TP startup after official main daily 20260721 merge | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/utils/compile.py` 等 7 个文件 |
| 2026-08-05 | `a0840f493` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [BugFix] recall hcu changes in pre_mhc changes to fix the accuracy issues | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-08-24 | `59fb95973` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(hcu): add INT8 indexer cache for DeepSeek-V4 | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py` 等 6 个文件 |
| 2026-08-25 | `7b3548f97` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` 等 48 个文件 |
| 2026-08-26 | `726db6820` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Merge all deepseek-v4 updated features including DSpark and more into v0.5.18 release. | `docs/internal/README_BF16_FLASHMLA.md`, `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/arg_groups/speculative_hook.py` 等 44 个文件 |
| 2026-08-27 | `d8a06d0c2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | Merge pull request #247 from RyeYuan/feat/rye_20260827_deepseek-v4_dspark_radix-cache | 无直接文件变更/merge |
| 2026-09-01 | `ddbbccde8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(dsv4): support PP/DSpark and CP-aware sparse prefill on HCU (#274) | `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 32 个文件 |
| 2026-09-01 | `c18c8d4bb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | compressor 通信优化 RLC（all-to-all + 本地压缩 + all-gather） (#275) | `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py` 等 8 个文件 |
| 2026-09-01 | `1316e9887` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): enable W4A8 DeepEP aiter path and FlashMLA workspace reuse (#265) | `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-09-07 | `4c367dbd5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(dsv4,hcu): support BF16/FP8 and INT8/INT8 indexer paths on gfx936 (#323) | `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/kernels/ops/attention/dsv4/__init__.py` 等 8 个文件 |
| 2026-09-08 | `c338e5fd0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(dsv4): optimize EP gather, paged K-cache, and mHC CP split (#327) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-09-09 | `e2c65d880` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | refactor(dsv4): use categorized LightOp mHC API (#332) | `python/sglang/srt/models/deepseek_v4.py` |
| 2026-09-10 | `551a71d4d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Feature/hy4 ihc tilelang 5commits (#336) | `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh` 等 25 个文件 |
| 2026-09-15 | `37f23f55a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(dsv4): auto-dispatch BF16-to-FP32 GEMM backends (#375) | `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh`, `python/sglang/kernels/ops/attention/dsv4/gemm.py`, `python/sglang/kernels/ops/attention/dsv4/hcu_linear_bf16_fp32.py` 等 10 个文件 |
| 2026-09-16 | `4f224d2b6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(dsv4): support paged MQA logits for prefill (#389) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 29 个文件 |
| 2026-09-16 | `6bf8197dd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Revert "perf(dsv4): support paged MQA logits for prefill (#389)" (#390) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 29 个文件 |
| 2026-09-17 | `055812e0d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Perf] DSV4：融合 Indexer Q 侧 INT8 量化，减少冗余量化算子 (#396) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/csrc/q_indexer_int8.cu`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 4 个文件 |
| 2026-09-17 | `fc7ebb3d0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | [Unified Cache] Improve Mooncake direct I/O, observability, and reliability (#398) | `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` 等 13 个文件 |
| 2026-09-18 | `2ed02ec34` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(dsv4): support paged MQA logits for prefill、support and optimize CP LayerSplit cache with Mooncake direct L3 (#395) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 25 个文件 |
| 2026-09-20 | `602fb4a30` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [FEAT] Support the BCG with CP-V2 and expect to improve TTFT from 10%… (#407) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/cp/bcg.py` 等 9 个文件 |
| 2026-09-23 | `ea1c297dc` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf: 为 HCU gfx936 DeepSeek-V4 增加 INT8 Persistent Paged MQA Logits (#436) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/csrc/paged_mqa_pers_jit.cu`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 4 个文件 |
| 2026-09-30 | `100533036` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [Fix][Unified Cache] Retry external KV abort cleanup after forward and source drain (#455) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mooncake/source_drain.py`, `python/sglang/srt/disaggregation/prefill.py` 等 21 个文件 |
| 2026-09-30 | `4ba29d557` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [HY4][HCU] Enable fp8_e4m3 KV cache with learnable attention sink (#418) | `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/dsa_backend.py` 等 4 个文件 |
| 2026-09-30 | `08ea4dec7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(dsv4): resolve Flash-0731 W4A8 API and general_fc accuracy issues (#450) | `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/function_call/base_format_detector.py` 等 9 个文件 |
| 2026-09-30 | `76e87a951` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): serve DeepSeek-V3.2 INT8, FP8, and BF16 in sglang0.5.18 (#466) | `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/communicator.py` 等 9 个文件 |
| 2026-10-15 | `ea3acdbe9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(dsv4): add opt-in paged MQA logits row chunking (#536) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` |
| 2026-10-16 | `23d1def83` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [FEAT] support megamoe with deegemm in deepseek-v4 (#525) | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py` |
| 2026-10-27 | `9f60f813d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [DSV4][HCU] Fix speculative compression state retention and configure Torch Top512 sorting (#597) | `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` |

### 逐 Commit 审计卡

#### Commit `94659d14a` - [dsv4] cp support megamoe

- 完整 hash: `94659d14a39813dd07318b6c681c213c9ec498bd`
- 时间/作者: 2026-06-17 / SYChen123
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `5b19ad464` - [fix(deepseek-v4)]: keep DCU on non-HIP attention backend + compressor

- 完整 hash: `5b19ad46427f6f9ecc81f830bbc49e418ddc3d2e`
- 时间/作者: 2026-06-24 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `1b2694156` - [fix(deepseek-v4)]: remove unused codes and use ScheduleBatch extend_lens/prefix_lens in init_new

- 完整 hash: `1b2694156d787b4f0248e43ff987f0d85ba6b075`
- 时间/作者: 2026-06-24 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c4cc0a73b` - fix(dsv4): preserve DCU elementwise and topk paths

- 完整 hash: `c4cc0a73b69ec48614c91ca8e586a29152fc171a`
- 时间/作者: 2026-06-30 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f2d0e86d7` - fix(dsv4): repair DCU sgl-kernel and JIT build

- 完整 hash: `f2d0e86d71b3242666d72f22fce42bea42b1667f`
- 时间/作者: 2026-06-30 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `sgl-kernel/setup_hip.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `sgl-kernel/setup_hip.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `249a70dbe` - [Addition] deliver one validation doc and support multi-stream in hip backend

- 完整 hash: `249a70dbef3117794005c238f5cfbd8c40487579`
- 时间/作者: 2026-07-02 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `fc241f4ad` - [BugFix] Sync to official changes to remove first pre-warmup of mHC

- 完整 hash: `fc241f4ad3244b6822ca0829f49ccc7283772727`
- 时间/作者: 2026-07-03 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/mhc.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `ad2ff869c` - [BugFix] Backport partial bugfixes from C10 and also have to assign SGLANG_USE_AITER_AG=0 to ensure accuracy now

- 完整 hash: `ad2ff869c60361435978336aa2faa4d79e648f53`
- 时间/作者: 2026-07-06 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py`, `test/manual/core/test_dsv4_cached_loc_invalidation.py`, `test/manual/core/test_dsv4_hicache_swa_translation_cache.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`; `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`
  - tests: `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py`; `test/manual/core/test_dsv4_cached_loc_invalidation.py`; `test/manual/core/test_dsv4_hicache_swa_translation_cache.py`; `test/manual/core/test_dsv4_stale_loc_crash.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `6bf9d1872` - fix(dcu): reconcile DSV4 prewarm and fused Q imports

- 完整 hash: `6bf9d18729fc409cb64b99ad842b9eb0282c5385`
- 时间/作者: 2026-07-13 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `84a8a08ac` - [BugFix] skip pre-warmup of mHC for DCU and update validation docs

- 完整 hash: `84a8a08ac230ba2fd78f8c902c5073aef51f949f`
- 时间/作者: 2026-07-14 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: `docs/internal/dcu-main-catchup-20260703-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-catchup-20260703-conflict-review.md`; `docs/internal/dcu-main-conflict-ledger.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `b5f9777d2` - Fix DCU DSV4 hash top-k router dtype

- 完整 hash: `b5f9777d2609d174738aa48de8263c819fa94e0d`
- 时间/作者: 2026-07-14 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `d703c086f` - [BugFix] Fix the accuracy issues of DeepSeek-V4 in TP/CP/DP/EP

- 完整 hash: `d703c086ff42655c602b85c9f0ac935215f8c4cc`
- 时间/作者: 2026-07-17 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/mem_cache/allocator/paged.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/mem_cache/allocator/paged.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

#### Commit `e876bb9ff` - [FEAT] support cp+MegaMoE in prefill w/o cuda-graph

- 完整 hash: `e876bb9ff3176ca4590a1deec0d69082d1195af3`
- 时间/作者: 2026-07-21 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/managers/scheduler_components/dp_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `470ae85b5` - style: apply pre-commit formatting (black/isort/ruff)

- 完整 hash: `470ae85b5277b2fdb97ef98268c9e241e3383d6b`
- 时间/作者: 2026-07-21 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `25ffedc22` - fix(hcu): repair forward-port compatibility gaps

- 完整 hash: `25ffedc2276699992e11eec0bddc867a8862663b`
- 时间/作者: 2026-07-29 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` 等 15 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` 等 9 个文件
  - tests: `python/sglang/multimodal_gen/test/server/test_server_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`
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

#### Commit `e7106de94` - V0.5.15.post1 dev to support dspark on HCU (#142)

- 完整 hash: `e7106de947db9db2d8dee246d40a276b0bcc728e`
- 时间/作者: 2026-07-31 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/benchmark/dspark_sps_profiler.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `python/sglang/srt/speculative/dspark_components/kernels/dspark_draft_model.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/benchmark/dspark_sps_profiler.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/managers/overlap_utils.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/deepseek_v4_dspark.py`; `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`
  - runtime-perf: `python/sglang/srt/speculative/dspark_components/kernels/dspark_draft_model.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `3d0f94345` - fix(hcu): fully revert files owned by the skipped source commits

- 完整 hash: `3d0f9434512ab52e842d3e42549756f022d0b572`
- 时间/作者: 2026-08-06 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/cache_controller.py` 等 20 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/speculative/eagle_info.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/jit_kernel/dsv4/compress.py`; `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`; `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `725659198` - Revert "fix assert when mtp enable and step >1"

- 完整 hash: `725659198b33689a1ab18146ed00c502d9d5a15e`
- 时间/作者: 2026-08-06 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `a596be0dc` - [BugFix] Fix DeepSeek-V4 pure-TP startup after official main daily 20260721 merge

- 完整 hash: `a596be0dc0287d572cc64f5ea0c589f1da706b7e`
- 时间/作者: 2026-07-21 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/utils/compile.py`, `python/sglang/srt/hardware_backend/npu/utils.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - other: `python/sglang/srt/hardware_backend/npu/utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/utils/compile.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `a0840f493` - [BugFix] recall hcu changes in pre_mhc changes to fix the accuracy issues

- 完整 hash: `a0840f493c5012862925011a80a13f0d7dd68579`
- 时间/作者: 2026-08-05 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `59fb95973` - feat(hcu): add INT8 indexer cache for DeepSeek-V4

- 完整 hash: `59fb959732955303211b872cd79e56c8fa50679e`
- 时间/作者: 2026-08-24 / luosyx
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/hcu_int8_index_k_cache.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`; `python/sglang/srt/layers/attention/dsv4/hcu_int8_index_k_cache.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`
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

#### Commit `726db6820` - Merge all deepseek-v4 updated features including DSpark and more into v0.5.18 release.

- 完整 hash: `726db6820363a4f74a42b607b2447f403102e91a`
- 时间/作者: 2026-08-26 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/README_BF16_FLASHMLA.md`, `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/fake/conn.py` 等 44 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/internal/README_BF16_FLASHMLA.md`
  - other: `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/common/utils.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/fake/conn.py`; `python/sglang/srt/disaggregation/hidden_events.py`; `python/sglang/srt/disaggregation/hidden_state.py` 等 20 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/draft_worker_common.py`; `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`; `python/sglang/srt/layers/attention/dsv4/hcu_int8_index_k_cache.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 17 个文件
  - tests: `test/registered/spec/dspark/test_dspark_draft_path_default.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `d8a06d0c2` - Merge pull request #247 from RyeYuan/feat/rye_20260827_deepseek-v4_dspark_radix-cache

- 完整 hash: `d8a06d0c23d998bfa56a9f49345b08406aee5fc1`
- 时间/作者: 2026-08-27 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 调度/缓存/PD
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `ddbbccde8` - feat(dsv4): support PP/DSpark and CP-aware sparse prefill on HCU (#274)

- 完整 hash: `ddbbccde8cc167817faf2f643dfd79c6f4f9e6e6`
- 时间/作者: 2026-09-01 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` 等 32 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/nixl/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/managers/utils.py`; `python/sglang/srt/speculative/dspark_components/dspark_kv_inject.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner_components/layer_setup.py`; `python/sglang/srt/model_executor/runner_utils/buffers.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/deepseek_v4_dspark.py`; `python/sglang/srt/models/dspark.py`; `python/sglang/srt/models/kimi_k3.py`; `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/server_args.py` 等 10 个文件
  - runtime-perf: `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`; `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` 等 11 个文件
  - tests: `test/registered/unit/disaggregation/test_disaggregation_wire.py`; `test/registered/unit/disaggregation/test_pp_pd_consensus.py`; `test/registered/unit/spec/test_dspark_pp_context.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `c18c8d4bb` - compressor 通信优化 RLC（all-to-all + 本地压缩 + all-gather） (#275)

- 完整 hash: `c18c8d4bb72a97c17384da51d1a225fb2b573983`
- 时间/作者: 2026-09-01 / Yongqiang Duan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/rlc.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`; `python/sglang/srt/layers/attention/dsv4/rlc.py`; `python/sglang/srt/layers/dp_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `1316e9887` - fix(hcu): enable W4A8 DeepEP aiter path and FlashMLA workspace reuse (#265)

- 完整 hash: `1316e9887593219d484dcc21ff00a70c1f0baff2`
- 时间/作者: 2026-09-01 / lipenghui
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4c367dbd5` - feat(dsv4,hcu): support BF16/FP8 and INT8/INT8 indexer paths on gfx936 (#323)

- 完整 hash: `4c367dbd52b3da177ec12f8bee9f6a5b36eda06f`
- 时间/作者: 2026-09-07 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/kernels/ops/attention/dsv4/__init__.py`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/kernels/ops/attention/dsv4/elementwise.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`; `python/sglang/kernels/ops/attention/dsv4/__init__.py`; `python/sglang/kernels/ops/attention/dsv4/compress.py`; `python/sglang/kernels/ops/attention/dsv4/elementwise.py`; `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `c338e5fd0` - perf(dsv4): optimize EP gather, paged K-cache, and mHC CP split (#327)

- 完整 hash: `c338e5fd0e5125d886c53438d42e2fccfd10f3cf`
- 时间/作者: 2026-09-08 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `e2c65d880` - refactor(dsv4): use categorized LightOp mHC API (#332)

- 完整 hash: `e2c65d880dcd94e9397040b2b1bcdda38ac73e46`
- 时间/作者: 2026-09-09 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `551a71d4d` - Feature/hy4 ihc tilelang 5commits (#336)

- 完整 hash: `551a71d4d6966366e76378c06be035079ef96963`
- 时间/作者: 2026-09-10 / liuzj512
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/hy_v4.py`, `python/sglang/srt/configs/model_config.py` 等 25 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/expert_location_dispatch.py`; `python/sglang/srt/layers/hy4_ihc_tilelang.py`; `python/sglang/srt/utils/hf_transformers/common.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/hy_v4.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/hunyuan_v4.py`; `python/sglang/srt/models/hunyuan_v4_nextn.py` 等 9 个文件
  - runtime-perf: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`; `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`; `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`; `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`; `python/sglang/srt/layers/attention/dsa_backend.py`; `python/sglang/srt/layers/radix_attention.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`
  - tests: `test/manual/layers/test_hy4_ihc_tilelang.py`; `test/registered/unit/models/test_hunyuan_v4_nextn_weight_loading.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `37f23f55a` - perf(dsv4): auto-dispatch BF16-to-FP32 GEMM backends (#375)

- 完整 hash: `37f23f55a0a348e10240369a3c8d112a62efed35`
- 时间/作者: 2026-09-15 / Yongqiang Duan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh`, `python/sglang/kernels/ops/attention/dsv4/gemm.py`, `python/sglang/kernels/ops/attention/dsv4/hcu_linear_bf16_fp32.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/utils/aiter.py`, `test/registered/hcu/kernels/test_linear_bf16_fp32_hcu.py` 等 10 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/utils/aiter.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh`; `python/sglang/kernels/ops/attention/dsv4/gemm.py`; `python/sglang/kernels/ops/attention/dsv4/hcu_linear_bf16_fp32.py`; `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`
  - tests: `test/registered/hcu/kernels/test_linear_bf16_fp32_hcu.py`; `test/registered/hcu/perf/bench_linear_bf16_fp32_hcu.py`; `test/registered/unit/test_linear_bf16_fp32_dispatch.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4f224d2b6` - perf(dsv4): support paged MQA logits for prefill (#389)

- 完整 hash: `4f224d2b67e3e542d720cc88fc1aa53f6a2c8e49`
- 时间/作者: 2026-09-16 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 29 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/bootstrap.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/__init__.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/broadcast.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_helpers.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_layout.py` 等 18 个文件
  - tests: `test/registered/unit/mem_cache/test_cp_cache_layer_split_deepseek_v4.py`; `test/registered/unit/mem_cache/test_cp_cache_layer_split_hcu.py`; `test/registered/unit/mem_cache/test_cp_cache_layer_split_ownership.py`; `test/registered/unit/mem_cache/test_linker_pool_assembler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `6bf8197dd` - Revert "perf(dsv4): support paged MQA logits for prefill (#389)" (#390)

- 完整 hash: `6bf8197ddaf145e26b22b54a494a0ad7ff2b90aa`
- 时间/作者: 2026-09-16 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 29 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/bootstrap.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/__init__.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/broadcast.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_helpers.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_layout.py` 等 18 个文件
  - tests: `test/registered/unit/mem_cache/test_cp_cache_layer_split_deepseek_v4.py`; `test/registered/unit/mem_cache/test_cp_cache_layer_split_hcu.py`; `test/registered/unit/mem_cache/test_cp_cache_layer_split_ownership.py`; `test/registered/unit/mem_cache/test_linker_pool_assembler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `055812e0d` - [Perf] DSV4：融合 Indexer Q 侧 INT8 量化，减少冗余量化算子 (#396)

- 完整 hash: `055812e0daa35545c9167f588f9b34c29047d93b`
- 时间/作者: 2026-09-17 / Yongqiang Duan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/csrc/q_indexer_int8.cu`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/q_indexer_int8_jit.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsv4/csrc/q_indexer_int8.cu`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/attention/dsv4/q_indexer_int8_jit.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `fc7ebb3d0` - [Unified Cache] Improve Mooncake direct I/O, observability, and reliability (#398)

- 完整 hash: `fc7ebb3d09b6d29684a1c9a237a1fcfac48075f8`
- 时间/作者: 2026-09-17 / leichuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py` 等 13 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/observability/metrics_collector.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/mem_cache/cache_init_params.py`; `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`; `python/sglang/srt/mem_cache/hicache_storage.py`; `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`; `python/sglang/srt/mem_cache/kv_cache_builder.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`
  - tests: `test/registered/unit/mem_cache/test_mooncake_group_semantics.py`; `test/registered/unit/server_args/test_server_args.py`; `test/registered/unit/test_server_args_cli_metadata.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2ed02ec34` - feat(dsv4): support paged MQA logits for prefill、support and optimize CP LayerSplit cache with Mooncake direct L3 (#395)

- 完整 hash: `2ed02ec34d6cd61d0c28f55f24f82b30099a706d`
- 时间/作者: 2026-09-18 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 25 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/bootstrap.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/__init__.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/broadcast.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_helpers.py`; `python/sglang/srt/mem_cache/cp_cache_layer_split/deepseek_v4_layout.py` 等 18 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `602fb4a30` - [FEAT] Support the BCG with CP-V2 and expect to improve TTFT from 10%… (#407)

- 完整 hash: `602fb4a30f93bd40a5eda61e5bc02906fc8d4825`
- 时间/作者: 2026-09-20 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v2.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/layers/cp/bcg.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/runner/eager_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/managers/scheduler_components/dp_attn.py`; `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `ea1c297dc` - perf: 为 HCU gfx936 DeepSeek-V4 增加 INT8 Persistent Paged MQA Logits (#436)

- 完整 hash: `ea1c297dc23343cbe5c6b619f3094325fb5fe45b`
- 时间/作者: 2026-09-23 / Yongqiang Duan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/csrc/paged_mqa_pers_jit.cu`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/paged_mqa_pers_jit.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsv4/csrc/paged_mqa_pers_jit.cu`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/attention/dsv4/paged_mqa_pers_jit.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `100533036` - [Fix][Unified Cache] Retry external KV abort cleanup after forward and source drain (#455)

- 完整 hash: `10053303694ba99167f7e17c585757fe3cf851bb`
- 时间/作者: 2026-09-30 / ybhe1110
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mooncake/source_drain.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cleanup.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py` 等 21 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/mooncake/source_drain.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/managers/schedule_batch.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/cleanup.py`; `python/sglang/srt/mem_cache/common.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`; `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`; `python/sglang/srt/mem_cache/unified_radix_cache.py`
  - tests: `python/sglang/test/kits/linker_load_failure_kit.py`; `python/sglang/test/mooncake_utils.py`; `test/registered/radix_cache/unified_radix_tree/linker/test_unified_cache_linker_kl_dsv4.py`; `test/registered/radix_cache/unified_radix_tree/linker/test_unified_cache_linker_kl_glm52.py`; `test/registered/unit/disaggregation/test_external_kv_abort_drain.py`; `test/registered/unit/disaggregation/test_external_kv_cleanup_resources.py`; `test/registered/unit/disaggregation/test_pp_pd_consensus.py`; `test/registered/unit/disaggregation/test_prefill_abort_cleanup.py` 等 11 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4ba29d557` - [HY4][HCU] Enable fp8_e4m3 KV cache with learnable attention sink (#418)

- 完整 hash: `4ba29d557c3a31a852cb7fa4fc0979630c36fff8`
- 时间/作者: 2026-09-30 / liuzj512
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/managers/scheduler.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/overrides.py`
  - runtime-perf: `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`; `python/sglang/srt/layers/attention/dsa_backend.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `08ea4dec7` - fix(dsv4): resolve Flash-0731 W4A8 API and general_fc accuracy issues (#450)

- 完整 hash: `08ea4dec71b0244d41b646c32dd322c9c234fd41`
- 时间/作者: 2026-09-30 / zhengzhi
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/function_call/base_format_detector.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`, `python/sglang/srt/function_call/deepseekv4_detector.py`, `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/function_call/base_format_detector.py`; `python/sglang/srt/function_call/deepseekv32_detector.py`; `python/sglang/srt/function_call/deepseekv4_detector.py`; `python/sglang/srt/function_call/function_call_parser.py`; `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-model: `python/sglang/srt/entrypoints/openai/serving_chat.py`
  - tests: `test/registered/unit/entrypoints/openai/test_serving_chat.py`; `test/registered/unit/function_call/test_deepseekv4_detector.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `76e87a951` - fix(hcu): serve DeepSeek-V3.2 INT8, FP8, and BF16 in sglang0.5.18 (#466)

- 完整 hash: `76e87a951d7a7423cf9686ef4109f98d25c2a0cf`
- 时间/作者: 2026-09-30 / lipenghui
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/communicator.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`; `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `ea3acdbe9` - feat(dsv4): add opt-in paged MQA logits row chunking (#536)

- 完整 hash: `ea3acdbe95df8893fe41b06c1fcf1477cb46d85e`
- 时间/作者: 2026-10-15 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `23d1def83` - [FEAT] support megamoe with deegemm in deepseek-v4 (#525)

- 完整 hash: `23d1def83c9e84999ca0803543f4438a882432bd`
- 时间/作者: 2026-10-16 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `9f60f813d` - [DSV4][HCU] Fix speculative compression state retention and configure Torch Top512 sorting (#597)

- 完整 hash: `9f60f813d33d69d931d2f0a83c134aaeeb306e0f`
- 时间/作者: 2026-10-27 / chaoyujiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`; `python/sglang/srt/layers/attention/dsv4/indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
