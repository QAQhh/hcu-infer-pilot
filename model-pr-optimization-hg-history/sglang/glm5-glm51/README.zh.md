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

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 11（其中 merge 3）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `502516539`, `723ac998c` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `2ac651d8f`, `3c2b52667` |
| `python/sglang/srt/utils/hf_transformers/config.py` | `0cf9a653e`, `502516539` |
| `test/registered/unit/utils/test_hf_transformers.py` | `0cf9a653e`, `502516539` |
| `.github/workflows/nightly-test-hcu.yml` | `2b4271498` |
| `.github/workflows/pr-test-hcu.yml` | `723ac998c` |
| `benchmark/glm53/README.md` | `98e923533` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `100533036` |
| `python/sglang/srt/disaggregation/mooncake/source_drain.py` | `100533036` |
| `python/sglang/srt/disaggregation/prefill.py` | `100533036` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `723ac998c` |
| `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py` | `723ac998c` |
| `python/sglang/srt/environ.py` | `723ac998c` |
| `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` | `723ac998c` |
| `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py` | `98e923533` |
| `python/sglang/srt/layers/attention/dsa/utils.py` | `723ac998c` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `723ac998c` |
| `python/sglang/srt/layers/cp/cp_decode_attn_tp.py` | `723ac998c` |
| `python/sglang/srt/layers/cp/interleave.py` | `723ac998c` |
| `python/sglang/srt/layers/cp/utils.py` | `723ac998c` |
| `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | `2ac651d8f` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `723ac998c` |
| `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | `98e923533` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `723ac998c` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `2ac651d8f` |
| `python/sglang/srt/managers/overlap_utils.py` | `98e923533` |
| `python/sglang/srt/managers/schedule_batch.py` | `100533036` |
| `python/sglang/srt/managers/scheduler.py` | `100533036` |
| `python/sglang/srt/mem_cache/cleanup.py` | `100533036` |
| `python/sglang/srt/mem_cache/common.py` | `100533036` |
| `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py` | `100533036` |
| `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` | `100533036` |
| `python/sglang/srt/mem_cache/unified_radix_cache.py` | `100533036` |
| `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py` | `723ac998c` |
| `python/sglang/srt/model_executor/pool_configurator.py` | `502516539` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | `98e923533` |
| `python/sglang/srt/models/deepseek_v2.py` | `98e923533` |
| `python/sglang/srt/server_args.py` | `723ac998c` |
| `python/sglang/srt/speculative/eagle_utils.py` | `723ac998c` |
| `python/sglang/srt/speculative/eagle_worker_v2.py` | `723ac998c` |
| ... | 另有 37 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-08-07 | `2b4271498` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` 等 11 个文件 |
| 2026-08-19 | `0cf9a653e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(glm5.2): restore raw DSA config fields | `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/unit/utils/test_hf_transformers.py` |
| 2026-08-26 | `502516539` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | style: format GLM 5.2 forward-port files | `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/utils/hf_transformers/config.py` 等 5 个文件 |
| 2026-08-27 | `cff97568f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge feature/glm52-forward-port-v0.5.18 into release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `11852ed1c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #256 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port | 无直接文件变更/merge |
| 2026-08-31 | `3a160688a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #262 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port | 无直接文件变更/merge |
| 2026-09-17 | `98e923533` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(glm53): 修正 FP8 权重映射并优化 HCU Decode 路径 (#384) | `benchmark/glm53/README.md`, `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` 等 6 个文件 |
| 2026-09-30 | `100533036` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [Fix][Unified Cache] Retry external KV abort cleanup after forward and source drain (#455) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mooncake/source_drain.py`, `python/sglang/srt/disaggregation/prefill.py` 等 21 个文件 |
| 2026-10-09 | `723ac998c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 修复 GLM-5.1/5.2 DSA 服务兼容性并优化 CP decode FlashMLA (#475) | `.github/workflows/pr-test-hcu.yml`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py` 等 32 个文件 |
| 2026-10-12 | `2ac651d8f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(w4a8): 兼容 GLM5.3-w4a8 模型的 compressed-tensors 打包权重 (#506) | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-10-15 | `3c2b52667` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(GLM5.3 w4a8): skip unused packed expert shape metadata (#539) | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |

### 逐 Commit 审计卡

#### Commit `2b4271498` - ci(hcu): publish nine-model accuracy results

- 完整 hash: `2b4271498f3d9031d0080accfa4dea9eccd10a59`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `0cf9a653e` - fix(glm5.2): restore raw DSA config fields

- 完整 hash: `0cf9a653eda76ddefec1c3044692433d1d033a36`
- 时间/作者: 2026-08-19 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/unit/utils/test_hf_transformers.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/utils/hf_transformers/config.py`
  - tests: `test/registered/unit/utils/test_hf_transformers.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `502516539` - style: format GLM 5.2 forward-port files

- 完整 hash: `5025165399aca0f6c482556c12bf53fbc4b870fd`
- 时间/作者: 2026-08-26 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/moe/test_topk_padded_region.py`, `test/registered/unit/utils/test_hf_transformers.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - tests: `test/registered/moe/test_topk_padded_region.py`; `test/registered/unit/utils/test_hf_transformers.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `cff97568f` - Merge feature/glm52-forward-port-v0.5.18 into release/20260825_v0.5.18

- 完整 hash: `cff97568fd17b74e707f3552bafc924abfa175de`
- 时间/作者: 2026-08-27 / luosyx
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `11852ed1c` - Merge pull request #256 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port

- 完整 hash: `11852ed1c2f6b2b26cb168a892c927efe95cbb7a`
- 时间/作者: 2026-08-28 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `3a160688a` - Merge pull request #262 from luosyx/feature/release-20260825_v0.5.18-glm52-forward-port

- 完整 hash: `3a160688a388a5ddcb84d8bfe1ca2451df609dda`
- 时间/作者: 2026-08-31 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `98e923533` - fix(glm53): 修正 FP8 权重映射并优化 HCU Decode 路径 (#384)

- 完整 hash: `98e92353399b9cf708523b02834b4894a3aa3321`
- 时间/作者: 2026-09-17 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/glm53/README.md`, `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `benchmark/glm53/README.md`
  - other: `python/sglang/srt/managers/overlap_utils.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`
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

#### Commit `723ac998c` - 修复 GLM-5.1/5.2 DSA 服务兼容性并优化 CP decode FlashMLA (#475)

- 完整 hash: `723ac998c384e495b66f57119382a3434d2d4152`
- 时间/作者: 2026-10-09 / qieshiniao
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/cp/cp_decode_attn_tp.py` 等 32 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/layers/cp/cp_decode_attn_tp.py`; `python/sglang/srt/layers/cp/interleave.py`; `python/sglang/srt/layers/cp/utils.py`; `python/sglang/srt/speculative/eagle_utils.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`; `python/sglang/srt/speculative/frozen_kv_mtp_worker_v2.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`; `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`; `python/sglang/srt/layers/attention/dsa/utils.py`; `python/sglang/srt/layers/attention/dsa_backend.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`
  - tests: `test/registered/hcu/unit/test_hcu_cp_decode_attn_tp_scale.py`; `test/registered/hcu/unit/test_hcu_dsa_cp_alignment.py`; `test/registered/hcu/unit/test_hcu_eagle_sampling_compat.py`; `test/registered/hcu/unit/test_hcu_eagle_verify_sync.py`; `test/registered/hcu/unit/test_hcu_flashmla_decode_h16.py`; `test/registered/hcu/unit/test_hcu_flashmla_decode_h16_memory.py`; `test/registered/hcu/unit/test_hcu_lightop_moe_routing_api.py`; `test/registered/hcu/unit/test_hcu_multimem_all_gather_guard.py` 等 13 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2ac651d8f` - fix(w4a8): 兼容 GLM5.3-w4a8 模型的 compressed-tensors 打包权重 (#506)

- 完整 hash: `2ac651d8f6b78dcc8214119e733c4ba55be15945`
- 时间/作者: 2026-10-12 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `3c2b52667` - fix(GLM5.3 w4a8): skip unused packed expert shape metadata (#539)

- 完整 hash: `3c2b5266717c24b831160a3c2f8c09b7f765d313`
- 时间/作者: 2026-10-15 / Songge
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
