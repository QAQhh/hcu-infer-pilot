# sglang Step 3.5 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/configs/step3p5.py` | `980d2936c` |
| `python/sglang/srt/models/step3p5.py` | `980d2936c` |
| `python/sglang/srt/models/step3p5_mtp.py` | `980d2936c` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 2
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-04 | `562c3ff2d` | 性能/后端优化 | [Feature] implement the standard multi-layer MTP for step3p5 (#18564) | `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-02-03 | `980d2936c` | 性能/后端优化 | model: support Step-3.5-Flash (#18084) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py` |

## 逐 Commit 审计卡

### Commit `562c3ff2d` - [Feature]  implement the standard multi-layer MTP for step3p5 (#18564)

- 完整 hash: `562c3ff2d0e40420869138495397dc3d5f5edd6f`
- 时间/作者: 2026-03-04 / qwe
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `980d2936c` - model: support Step-3.5-Flash (#18084)

- 完整 hash: `980d2936cd9a94a6346fb678a8134d5776fdf996`
- 时间/作者: 2026-02-03 / Yuhao Yang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py`, `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_loader/loader.py` 等 15 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/function_call/function_call_parser.py`; `python/sglang/srt/model_loader/loader.py`; `python/sglang/srt/parser/reasoning_parser.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/step3p5.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/step3p5.py`; `python/sglang/srt/models/step3p5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/models/mimo_v2_flash_nextn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
