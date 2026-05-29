# sglang Qwen3.5 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/qwen3_5.py` | `94a624b83` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 6
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-05-07 | `9f67deca2` | 性能/后端优化 | 支持qwen3.5-awq模型 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py` |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `94a624b83` | 性能/后端优化 | 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-09 | `b8cd509f4` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-04-02 | `28dec61dd` | 模型支持/运行时入口 | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |

## 逐 Commit 审计卡

### Commit `9f67deca2` - 支持qwen3.5-awq模型

- 完整 hash: `9f67deca24b100410fe69d142a4ebca4fe26cc34`
- 时间/作者: 2026-05-07 / maxiao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py`, `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/moe_wna16.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `94a624b83` - 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子

- 完整 hash: `94a624b8364de497a4a7ee4a6f9def06e18d90c9`
- 时间/作者: 2026-04-23 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b8cd509f4` - [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能

- 完整 hash: `b8cd509f45f9a51adee404eb9104358653e869d1`
- 时间/作者: 2026-04-09 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `28dec61dd` - support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k

- 完整 hash: `28dec61dd674f482fe34b5251ff0cd050ca2184c`
- 时间/作者: 2026-04-02 / liucong
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## v0.5.8_dev 到 v0.5.12_dev 本地独有提交补充

### 覆盖说明

- 来源索引: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- 来源工作树: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交。
- 本章节提交数: 4
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-04-02 | `44081352b` | `v0.5.9_dev..v0.5.10_dev` | 调度/缓存/PD | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |
| 2026-04-09 | `f6730ce49` | `v0.5.9_dev..v0.5.10_dev` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-05-09 | `fe8d278ca` | `v0.5.10_dev..v0.5.11_dev` | 缺陷修复 | debugging qwen3.5 model | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 6 个文件 |
| 2026-05-18 | `43efcafdc` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix init error when use qwen 3.5 | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 7 个文件 |

### 逐 Commit 审计卡

#### Commit `44081352b` - support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k

- 完整 hash: `44081352b950ed172c2d04b776db732a49f2f9b4`
- 时间/作者: 2026-04-02 / liucong
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
- 验证与风险: 涉及调度、缓存、PD 或 MTP 路径；需要验证 prefill/decode 时序、首 token 正确性、并发与长上下文稳定性。

#### Commit `f6730ce49` - [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能

- 完整 hash: `f6730ce492512fded4d0c8a7c751303c39cce828`
- 时间/作者: 2026-04-09 / chenyue3
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `fe8d278ca` - debugging qwen3.5 model

- 完整 hash: `fe8d278ca9cb6dc45627610fe18b831cecae5ab9`
- 时间/作者: 2026-05-09 / lizhigong
- 分支更新段: `v0.5.10_dev..v0.5.11_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/moe_align_block_size.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/linear.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/moe_align_block_size.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `43efcafdc` - fix init error when use qwen 3.5

- 完整 hash: `43efcafdcda164d8d40a15c624b301c82528833a`
- 时间/作者: 2026-05-18 / lizhigong
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
  - other: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/model_executor/forward_batch_info.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
