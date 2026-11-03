# sglang Qwen3.6 本地提交优化历史

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
- 本章节提交数: 8（其中 merge 0）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `700649f36`, `4603df038`, `050129f5b`, `f4d13c6b8`, `b290dcf39` |
| `.github/workflows/nightly-test-hcu.yml` | `9b86479ac`, `5d0386fd4` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `700649f36`, `b290dcf39` |
| `python/sglang/srt/models/dspark.py` | `4603df038`, `050129f5b` |
| `python/sglang/srt/speculative/dflash_utils.py` | `4603df038`, `050129f5b` |
| `python/sglang/srt/utils/hf_transformers/config.py` | `4603df038`, `050129f5b` |
| `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py` | `5d0386fd4`, `b86a8dc74` |
| `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py` | `5d0386fd4`, `b86a8dc74` |
| `test/run_suite.py` | `9b86479ac`, `5d0386fd4` |
| `.github/workflows/pr-test-hcu.yml` | `5d0386fd4` |
| `.gitignore` | `9b86479ac` |
| `THIRD_PARTY_NOTICES.md` | `9b86479ac` |
| `python/sglang/kernels/ops/speculative/dflash.py` | `b290dcf39` |
| `python/sglang/srt/configs/dspark.py` | `4603df038` |
| `python/sglang/srt/environ.py` | `050129f5b` |
| `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` | `700649f36` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `f4d13c6b8` |
| `python/sglang/srt/layers/quantization/unquant.py` | `700649f36` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `b290dcf39` |
| `python/sglang/srt/models/dflash.py` | `700649f36` |
| `python/sglang/srt/speculative/dflash_worker_v2.py` | `b290dcf39` |
| `python/sglang/srt/speculative/dspark_components/dspark_config.py` | `050129f5b` |
| `python/sglang/test/hcu_cookbook_utils.py` | `9b86479ac` |
| `python/sglang/test/hcu_reasoning_code_utils.py` | `9b86479ac` |
| `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` | `9b86479ac` |
| `scripts/ci/hcu/hcu_ci_judge_humaneval.sh` | `9b86479ac` |
| `test/hcu_humaneval_judge.py` | `9b86479ac` |
| `test/manual/test_hcu_dflash_native_block16.py` | `f4d13c6b8` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen35_397b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen36_35b_a3b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_30b_a3b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_32b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/infra/test_hcu_server_guard_failures_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/kernels/test_attention_reference_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` | `5d0386fd4` |
| ... | 另有 4 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-21 | `9b86479ac` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | test(hcu): add MATH-500 and HumanEval nightly coverage | `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md` 等 14 个文件 |
| 2026-08-06 | `5d0386fd4` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci(hcu): expand functional and numerical coverage | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py` 等 16 个文件 |
| 2026-08-07 | `b86a8dc74` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | test(hcu): bound backend smoke test setup | `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py` |
| 2026-09-08 | `700649f36` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 【Feat】Qwen3.6‑35B‑A3B supported dflash2 (#331) | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` 等 5 个文件 |
| 2026-09-11 | `4603df038` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]Qwen3.6-35B-A3B 支持--speculative-algorithm DSPARK (#341) | `python/sglang/srt/configs/dspark.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` 等 5 个文件 |
| 2026-09-12 | `050129f5b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [bugfix] Isolate the use of --speculative-algorithm DSPARK for the Qwen3.6-35B-A3B model family via the SGLANG_USE_QWEN_DSPARK environment variable. (#352) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` 等 6 个文件 |
| 2026-09-17 | `f4d13c6b8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Feat]Qwen3.6-35B-A3B DFLASH性能优化 (#388) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/manual/test_hcu_dflash_native_block16.py` |
| 2026-10-13 | `b290dcf39` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat] 优化 HCU 上 Qwen3.6-35B-A3B 使用 DFLASH 时（--speculative-algorithm DFLASH）的性能 (#522) | `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 5 个文件 |

### 逐 Commit 审计卡

#### Commit `9b86479ac` - test(hcu): add MATH-500 and HumanEval nightly coverage

- 完整 hash: `9b86479ac4f933649d4f777d1ffb92bfbfc375ab`
- 时间/作者: 2026-07-21 / tianlinyang77
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_reasoning_code_utils.py`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`, `test/hcu_humaneval_judge.py` 等 14 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `.gitignore`; `THIRD_PARTY_NOTICES.md`; `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_reasoning_code_utils.py`; `test/hcu_humaneval_judge.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen35_397b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen36_35b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_30b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_32b_hcu.py`; `test/run_suite.py` 等 9 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `5d0386fd4` - ci(hcu): expand functional and numerical coverage

- 完整 hash: `5d0386fd4cfda35ce75a6519dd6008fac8d2dcc9`
- 时间/作者: 2026-08-06 / LvJIA-RG
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`, `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py`, `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py`, `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`, `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py` 等 16 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - tests: `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`; `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py`; `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py`; `test/registered/hcu/infra/test_hcu_server_guard_failures_hcu.py`; `test/registered/hcu/kernels/test_attention_reference_hcu.py` 等 14 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `b86a8dc74` - test(hcu): bound backend smoke test setup

- 完整 hash: `b86a8dc74ff9d3a2f535122c85966923e04f5037`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `700649f36` - 【Feat】Qwen3.6‑35B‑A3B supported dflash2 (#331)

- 完整 hash: `700649f36306ad88b7322362f3262154b7b3adff`
- 时间/作者: 2026-09-08 / chenyuege
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/dflash.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`; `python/sglang/srt/layers/quantization/unquant.py`; `python/sglang/srt/models/dflash.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4603df038` - [feat]Qwen3.6-35B-A3B 支持--speculative-algorithm DSPARK (#341)

- 完整 hash: `4603df038bccfa86a42db00202c1cd25c8d6529b`
- 时间/作者: 2026-09-11 / chenyuege
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/dspark.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/utils/hf_transformers/config.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/configs/dspark.py`; `python/sglang/srt/models/dspark.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/speculative/dflash_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `050129f5b` - [bugfix] Isolate the use of --speculative-algorithm DSPARK for the Qwen3.6-35B-A3B model family via the SGLANG_USE_QWEN_DSPARK environment variable. (#352)

- 完整 hash: `050129f5b3406b3b003378dccd3009433df76d7a`
- 时间/作者: 2026-09-12 / chenyuege
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dspark_components/dspark_config.py`, `python/sglang/srt/utils/hf_transformers/config.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/dspark.py`; `python/sglang/srt/speculative/dspark_components/dspark_config.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/speculative/dflash_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f4d13c6b8` - [Feat]Qwen3.6-35B-A3B DFLASH性能优化 (#388)

- 完整 hash: `f4d13c6b88c6a3494b1036d62de54f6849d73eed`
- 时间/作者: 2026-09-17 / chenyuege
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/manual/test_hcu_dflash_native_block16.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`
  - tests: `test/manual/test_hcu_dflash_native_block16.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b290dcf39` - [feat] 优化 HCU 上 Qwen3.6-35B-A3B 使用 DFLASH 时（--speculative-algorithm DFLASH）的性能 (#522)

- 完整 hash: `b290dcf39562e7ae6ed5f1646bbd20d1e1d8c7fc`
- 时间/作者: 2026-10-13 / chenyuege
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/speculative/dflash.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/speculative/dflash_worker_v2.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
