# sglang GLM-5/5.1 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| - | 无本地独有提交 |

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
| 2026-04-30 | `752ed6468` | 性能/后端优化 | 修复glm5w4a8重排逻辑，减少显存占用 | `python/sglang/srt/layers/quantization/w4a8_utils.py` |
| 2026-04-30 | `262fa654e` | 调度/缓存/PD | 【GLM5】NSA indexer新增bf16路径 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-04-28 | `74f1c1b27` | 调度/缓存/PD | 合入官方pr，解决glm5跑pd分离时page计算不一致崩溃 | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-04-25 | `78557fe3d` | 通用实现调整 | 【GLM5】避免DCU路径加载TileLang和TVM依赖 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-04-23 | `c40804b20` | 性能/后端优化 | 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合 3. 融合get_logits_head_gate算子 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |

## 逐 Commit 审计卡

### Commit `752ed6468` - 修复glm5w4a8重排逻辑，减少显存占用

- 完整 hash: `752ed6468ffafbcd5743df06e40eb5ef2685a29c`
- 时间/作者: 2026-04-30 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/w4a8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/w4a8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `262fa654e` - 【GLM5】NSA indexer新增bf16路径

- 完整 hash: `262fa654e806f504f9a20f5b7438975bb719d891`
- 时间/作者: 2026-04-30 / maxiao1
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `74f1c1b27` - 合入官方pr，解决glm5跑pd分离时page计算不一致崩溃

- 完整 hash: `74f1c1b27935b7b6fc83c3d25f962cc31e4f625e`
- 时间/作者: 2026-04-28 / maxiao1
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `78557fe3d` - 【GLM5】避免DCU路径加载TileLang和TVM依赖

- 完整 hash: `78557fe3d0893bb8173b1322ef08fe722accf2af`
- 时间/作者: 2026-04-25 / maxiao1
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c40804b20` - 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合  3. 融合get_logits_head_gate算子

- 完整 hash: `c40804b203877a1affe2cc3862fc26dc29b8efdd`
- 时间/作者: 2026-04-23 / maxiao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2854c89b4` - 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化

- 完整 hash: `2854c89b4ee838989dea9b7e403840dfcf4d7116`
- 时间/作者: 2026-04-10 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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
| 2026-03-18 | `c6c74dbdc` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM5 Test | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py` 等 16 个文件 |
| 2026-03-26 | `5f51de15a` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM-5 adaptation | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 6 个文件 |
| 2026-03-27 | `40a938509` | `v0.5.8_dev..v0.5.9_dev` | 调度/缓存/PD | add prefill flashmla_sparse kv_cache fp8 for GLM-5 | `python/sglang/srt/layers/attention/nsa_backend.py`, `sgl-kernel/setup_rocm.py` |
| 2026-03-30 | `511c78385` | `v0.5.8_dev..v0.5.9_dev` | 调度/缓存/PD | GLM5 MTP adapt | `python/sglang/srt/layers/attention/nsa_backend.py` |

### 逐 Commit 审计卡

#### Commit `c6c74dbdc` - GLM5 Test

- 完整 hash: `c6c74dbdca35022867b4b68400fe87f9d7666790`
- 时间/作者: 2026-03-18 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 16 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` 等 10 个文件
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `5f51de15a` - GLM-5 adaptation

- 完整 hash: `5f51de15a2c8993abd00cc90d8c22f976b9da7dc`
- 时间/作者: 2026-03-26 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `40a938509` - add prefill flashmla_sparse kv_cache fp8 for GLM-5

- 完整 hash: `40a93850978de3f1418bc484079c3ed252ec34c4`
- 时间/作者: 2026-03-27 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/layers/attention/nsa_backend.py`, `sgl-kernel/setup_rocm.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`; `sgl-kernel/setup_rocm.py`
- 验证与风险: 涉及调度、缓存、PD 或 MTP 路径；需要验证 prefill/decode 时序、首 token 正确性、并发与长上下文稳定性。

#### Commit `511c78385` - GLM5 MTP adapt

- 完整 hash: `511c78385d2165c95fcd3e73a79dcca93b4430f8`
- 时间/作者: 2026-03-30 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/layers/attention/nsa_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
- 验证与风险: 涉及调度、缓存、PD 或 MTP 路径；需要验证 prefill/decode 时序、首 token 正确性、并发与长上下文稳定性。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
