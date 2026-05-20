# sglang GLM-5/5.1 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `docs/platforms/ascend_npu_glm5_examples.md` | `2d583799e`, `210d0fbae`, `56891e46b`, `f65c885e7`, `123f57b84`, `c34832c02` |
| `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` | `23adb5075` |
| `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` | `23adb5075` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 18
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-04-30 | `752ed6468` | 性能/后端优化 | 修复glm5w4a8重排逻辑，减少显存占用 | `python/sglang/srt/layers/quantization/w4a8_utils.py` |
| 2026-04-30 | `262fa654e` | 调度/缓存/PD | 【GLM5】NSA indexer新增bf16路径 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-04-28 | `74f1c1b27` | 调度/缓存/PD | 合入官方pr，解决glm5跑pd分离时page计算不一致崩溃 | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-04-25 | `78557fe3d` | 通用实现调整 | 【GLM5】避免DCU路径加载TileLang和TVM依赖 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-04-23 | `c40804b20` | 性能/后端优化 | 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合 3. 融合get_logits_head_gate算子 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-03-25 | `2d583799e` | 调度/缓存/PD | Update ascend docs (#20846) | `docs/platforms/ascend_npu_best_practice.md`, `docs/platforms/ascend_npu_deepseek_example.md`, `docs/platforms/ascend_npu_glm5_examples.md` |
| 2026-03-17 | `da2447891` | 性能/后端优化 | [AMD] Fix CI: update transformers in Qwen 3.5 and GLM-5 nightly tests (#20750) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml` |
| 2026-03-17 | `210d0fbae` | 调度/缓存/PD | Update ascend docs (#20674) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md` |
| 2026-03-09 | `be63f982b` | 性能/后端优化 | [V32/GLM5] Control the threshold of applying dense attention with an environ (#20062) | `docs/references/environment_variables.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-03-07 | `d28f35240` | 通用实现调整 | [V32/GLM5] Change default setting of V32 nvfp4 on TP4 (#20086) | `python/sglang/srt/server_args.py` |
| 2026-02-25 | `56891e46b` | 模型支持/运行时入口 | [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md` |
| 2026-02-24 | `23adb5075` | 性能/后端优化 | [AMD] [GLM-5 Day 0] Add GLM-5 nightly test (#18911) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` |
| 2026-02-22 | `eddf19329` | 性能/后端优化 | [DSv32] [GLM5] Improve Model Quality by Avoiding FP32 Precision Loss in `weights_proj` (#19041) | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py` |
| 2026-02-17 | `1b659bcb0` | 性能/后端优化 | Fix GLM-5 fused shared expert (#18804) | `python/sglang/srt/models/glm4_moe.py` |
| 2026-02-13 | `f65c885e7` | 测试/文档/基准 | Modify glm5 readme on npu (#18768) | `docs/platforms/ascend_npu_glm5_examples.md` |
| 2026-02-12 | `123f57b84` | 调度/缓存/PD | update glm5 readme on npu (#18657) | `docs/platforms/ascend_npu_glm5_examples.md` |
| 2026-02-12 | `c34832c02` | 测试/文档/基准 | glm5 md (#18655) | `docs/platforms/ascend_npu_glm5_examples.md` |

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

### Commit `2d583799e` - Update ascend docs (#20846)

- 完整 hash: `2d583799ebb8ba67732e8bc5c70e814734491337`
- 时间/作者: 2026-03-25 / amote-i
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/platforms/ascend_npu_best_practice.md`, `docs/platforms/ascend_npu_deepseek_example.md`, `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_support_features.md`, `docs/platforms/ascend_npu_support_models.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_best_practice.md`; `docs/platforms/ascend_npu_deepseek_example.md`; `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_support_features.md`; `docs/platforms/ascend_npu_support_models.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `da2447891` - [AMD] Fix CI: update transformers in Qwen 3.5 and GLM-5 nightly tests (#20750)

- 完整 hash: `da24478913f5fbac87644c3679e051ed5276fdbe`
- 时间/作者: 2026-03-17 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `210d0fbae` - Update ascend docs (#20674)

- 完整 hash: `210d0fbaef41bb18a83320e1fbe8f50c9d0c9ead`
- 时间/作者: 2026-03-17 / amote-i
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`; `docs/platforms/ascend_npu_support_features.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `be63f982b` - [V32/GLM5] Control the threshold of applying dense attention with an environ (#20062)

- 完整 hash: `be63f982b7b7f0451a3ccbb13f6fe2ecf6c39796`
- 时间/作者: 2026-03-09 / Baizhou Zhang
- 自动分类: 性能/后端优化
- 主要文件: `docs/references/environment_variables.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/server_args.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/references/environment_variables.md`
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
  - tests: `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`; `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d28f35240` - [V32/GLM5] Change default setting of V32 nvfp4 on TP4 (#20086)

- 完整 hash: `d28f35240a28de1e09967975e258b3dd7e74924f`
- 时间/作者: 2026-03-07 / Baizhou Zhang
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `56891e46b` - [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339)

- 完整 hash: `56891e46bc1ac4f75e8e541b61810f777cda8209`
- 时间/作者: 2026-02-25 / Hexq0210
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `23adb5075` - [AMD] [GLM-5 Day 0] Add GLM-5 nightly test (#18911)

- 完整 hash: `23adb50751d50638e52504ea223ad9d6677fd478`
- 时间/作者: 2026-02-24 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_gsm8k_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `eddf19329` - [DSv32] [GLM5] Improve Model Quality by Avoiding FP32 Precision Loss in `weights_proj` (#19041)

- 完整 hash: `eddf193292d310b416473815cffb0c9d13985be2`
- 时间/作者: 2026-02-22 / Ziang Li
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `test/registered/kernels/test_nsa_indexer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`; `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
  - tests: `test/registered/kernels/test_nsa_indexer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1b659bcb0` - Fix GLM-5 fused shared expert (#18804)

- 完整 hash: `1b659bcb088fd303ee472c0720eeb1a3797cffa1`
- 时间/作者: 2026-02-17 / Frank Minors
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/glm4_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/glm4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f65c885e7` - Modify glm5 readme on npu (#18768)

- 完整 hash: `f65c885e7ccda97c31a8d6619d1620ff8bdb008e`
- 时间/作者: 2026-02-13 / BourneSun0527
- 自动分类: 测试/文档/基准
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `123f57b84` - update glm5 readme on npu (#18657)

- 完整 hash: `123f57b84bbaeb23e673d33598279fcf564f9607`
- 时间/作者: 2026-02-12 / fy
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c34832c02` - glm5 md (#18655)

- 完整 hash: `c34832c02c28360cca5657f26741001dd9d3fe7c`
- 时间/作者: 2026-02-12 / liupeng374
- 自动分类: 测试/文档/基准
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。
