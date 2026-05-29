# sglang DeepSeek V3.1 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `47b08354a`, `e9d6aefa9` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `47b08354a` |
| `python/sglang/srt/models/deepseek_v2.py` | `2854c89b4`, `79349e551`, `2b0bed239`, `e9d6aefa9` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 5
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-04-16 | `47b08354a` | 缺陷修复 | 1. 修复mqa logits chunk bug 2.将FP8 MLA BMM权重在加载时转为BF16，避免forward中重复cast | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-03-31 | `79349e551` | 性能/后端优化 | 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` |
| 2026-03-30 | `2b0bed239` | 性能/后端优化 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |

## 逐 Commit 审计卡

### Commit `47b08354a` - 1. 修复mqa logits chunk bug 2.将FP8 MLA BMM权重在加载时转为BF16，避免forward中重复cast

- 完整 hash: `47b08354ad96b97bb18c738bac89349ee9cec5bc`
- 时间/作者: 2026-04-16 / niuhb
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
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

### Commit `79349e551` - 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug

- 完整 hash: `79349e5510a7485abc9102a64f972c07d2f8790b`
- 时间/作者: 2026-03-31 / niuhb
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/deepseek_v2.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/setup_hip.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/setup_hip.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2b0bed239` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- 完整 hash: `2b0bed23943bee2e93916979aabc272268a11a1c`
- 时间/作者: 2026-03-30 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
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
- 本章节提交数: 8
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-03-18 | `c6c74dbdc` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM5 Test | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py` 等 16 个文件 |
| 2026-03-26 | `5f51de15a` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | GLM-5 adaptation | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 6 个文件 |
| 2026-03-30 | `00db89c86` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |
| 2026-03-30 | `7bfdade34` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |
| 2026-03-31 | `b4de83009` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` 等 7 个文件 |
| 2026-05-09 | `fe8d278ca` | `v0.5.10_dev..v0.5.11_dev` | 缺陷修复 | debugging qwen3.5 model | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 6 个文件 |
| 2026-05-08 | `ba7aa00c9` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix bug | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-05-18 | `43efcafdc` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix init error when use qwen 3.5 | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 7 个文件 |

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

#### Commit `00db89c86` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- 完整 hash: `00db89c86ed93c08a883ffa6b708babf8e89743c`
- 时间/作者: 2026-03-30 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `7bfdade34` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- 完整 hash: `7bfdade34395bd4ae7c723b64de68a990820d0b2`
- 时间/作者: 2026-03-30 / maxiao1
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `b4de83009` - 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug

- 完整 hash: `b4de83009ba8c4f8bce8a242ecd6a2af0f0237ff`
- 时间/作者: 2026-03-31 / niuhb
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/deepseek_v2.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/setup_hip.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_kernel.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/setup_hip.py`
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

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

#### Commit `ba7aa00c9` - fix bug

- 完整 hash: `ba7aa00c97719d471e95a869baf3bea0ca59d297`
- 时间/作者: 2026-05-08 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
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
