# sglang Qwen3 Core 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/qwen3.py` | `b63cd7645`, `e9d6aefa9` |
| `python/sglang/srt/models/qwen3_moe.py` | `466a1d6a4`, `e9d6aefa9` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 9
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
| 2026-04-21 | `466a1d6a4` | 性能/后端优化 | 将qwen3_moe文件中的SGLANG_USE_FUSED_BAILING_RMS_ROTARY修改为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-04-09 | `b8cd509f4` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-04-02 | `28dec61dd` | 模型支持/运行时入口 | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |
| 2026-03-31 | `b63cd7645` | 性能/后端优化 | 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py` |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |

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

### Commit `466a1d6a4` - 将qwen3_moe文件中的SGLANG_USE_FUSED_BAILING_RMS_ROTARY修改为SGLANG_USE_FUSED_RMS_ROTARY

- 完整 hash: `466a1d6a4caa1403fb6608748c3111ddc152cdf2`
- 时间/作者: 2026-04-21 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `b63cd7645` - 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY

- 完整 hash: `b63cd76459510fb534dde7d8df2ca438099aa881`
- 时间/作者: 2026-03-31 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/qwen3.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/models/bailing_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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
| 2026-03-06 | `4c7028bf2` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | qwen系列模型算子融合 | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py` 等 9 个文件 |
| 2026-03-31 | `2befcb806` | `v0.5.9_dev..v0.5.10_dev` | 模型支持/运行时入口 | 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py` 等 4 个文件 |

### 逐 Commit 审计卡

#### Commit `4c7028bf2` - qwen系列模型算子融合

- 完整 hash: `4c7028bf269fffb15649d58adf43a8ce1bb51066`
- 时间/作者: 2026-03-06 / liucong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/bailing_moe.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
  - other: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/environ.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `2befcb806` - 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY

- 完整 hash: `2befcb8061ad02de8471f06bc482eb5b7b827243`
- 时间/作者: 2026-03-31 / liucong8560
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/qwen3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
  - other: `python/sglang/srt/environ.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
