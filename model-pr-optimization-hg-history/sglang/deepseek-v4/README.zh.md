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
