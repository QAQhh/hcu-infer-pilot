# sglang Nemotron Super 本地提交优化历史

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
- 本章节提交数: 1（其中 merge 0）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `test/registered/4-gpu-models/test_qwen3_next_models.py` | `e47388196` |
| `test/registered/attention/test_fa3.py` | `e47388196` |
| `test/registered/attention/test_local_attn.py` | `e47388196` |
| `test/registered/core/test_gpt_oss_1gpu.py` | `e47388196` |
| `test/registered/core/test_page_size.py` | `e47388196` |
| `test/registered/core/test_score_api.py` | `e47388196` |
| `test/registered/disaggregation/test_dp_attention_large.py` | `e47388196` |
| `test/registered/embedding/test_embedding_models.py` | `e47388196` |
| `test/registered/embedding/test_encoder_embedding_models.py` | `e47388196` |
| `test/registered/embedding/test_input_embeddings.py` | `e47388196` |
| `test/registered/embedding/test_openai_embedding.py` | `e47388196` |
| `test/registered/eval/test_eval_accuracy_large.py` | `e47388196` |
| `test/registered/eval/test_moe_eval_accuracy_large.py` | `e47388196` |
| `test/registered/lora/test_lora_backend.py` | `e47388196` |
| `test/registered/metrics/test_metrics.py` | `e47388196` |
| `test/registered/metrics/test_priority_metrics.py` | `e47388196` |
| `test/registered/mla/test_mla.py` | `e47388196` |
| `test/registered/mla/test_mla_deepseek_v3.py` | `e47388196` |
| `test/registered/models/test_cross_encoder_models.py` | `e47388196` |
| `test/registered/models/test_nvidia_nemotron_nano_v2.py` | `e47388196` |
| `test/registered/models/test_qwen_models.py` | `e47388196` |
| `test/registered/models/test_reward_models.py` | `e47388196` |
| `test/registered/openai_server/basic/test_protocol.py` | `e47388196` |
| `test/registered/openai_server/basic/test_serving_chat.py` | `e47388196` |
| `test/registered/openai_server/basic/test_serving_completions.py` | `e47388196` |
| `test/registered/openai_server/basic/test_serving_rerank.py` | `e47388196` |
| `test/registered/openai_server/features/test_enable_thinking.py` | `e47388196` |
| `test/registered/openai_server/features/test_reasoning_content.py` | `e47388196` |
| `test/registered/openai_server/function_call/test_tool_choice.py` | `e47388196` |
| `test/registered/ops/test_repeat_interleave.py` | `e47388196` |
| `test/registered/perf/test_bench_one_batch_1gpu.py` | `e47388196` |
| `test/registered/quant/test_bnb.py` | `e47388196` |
| `test/registered/quant/test_eval_fp8_accuracy.py` | `e47388196` |
| `test/registered/quant/test_torchao.py` | `e47388196` |
| `test/registered/quant/test_w4a8_deepseek_v3.py` | `e47388196` |
| `test/registered/rotary/test_mrope.py` | `e47388196` |
| `test/registered/scheduler/test_abort.py` | `e47388196` |
| `test/registered/scheduler/test_chunked_prefill.py` | `e47388196` |
| `test/registered/scheduler/test_no_chunked_prefill.py` | `e47388196` |
| `test/registered/scheduler/test_no_overlap_scheduler.py` | `e47388196` |
| ... | 另有 4 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-08-06 | `e47388196` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci: migrate legacy CUDA suite= registrations to stage=/runner_config= | `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_local_attn.py` 等 44 个文件 |

### 逐 Commit 审计卡

#### Commit `e47388196` - ci: migrate legacy CUDA suite= registrations to stage=/runner_config=

- 完整 hash: `e473881969aef386533c0fb29ce8fd036a733560`
- 时间/作者: 2026-08-06 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_local_attn.py`, `test/registered/core/test_gpt_oss_1gpu.py`, `test/registered/core/test_page_size.py`, `test/registered/core/test_score_api.py`, `test/registered/disaggregation/test_dp_attention_large.py`, `test/registered/embedding/test_embedding_models.py` 等 44 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_local_attn.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_page_size.py`; `test/registered/core/test_score_api.py`; `test/registered/disaggregation/test_dp_attention_large.py`; `test/registered/embedding/test_embedding_models.py` 等 44 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

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
