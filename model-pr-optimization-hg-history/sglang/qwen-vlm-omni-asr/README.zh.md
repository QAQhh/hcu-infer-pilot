# sglang Qwen VLM/Omni/ASR 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/qwen3_vl.py` | `c1d308c60`, `32bd2422e` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 2
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |

## 逐 Commit 审计卡

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
