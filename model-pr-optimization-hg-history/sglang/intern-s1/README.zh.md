# sglang Intern-S1 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/function_call/internlm_detector.py` | 无直接提交 |
| `python/sglang/srt/models/interns1.py` | 无直接提交 |
| `python/sglang/srt/models/interns1pro.py` | `3e7ecb78a` |
| `python/sglang/srt/multimodal/processors/interns1pro.py` | `3e7ecb78a` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 2
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-05 | `3e7ecb78a` | 性能/后端优化 | model: support interns1-pro (#18145) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/interns1pro.py` |
| 2026-01-26 | `539924037` | 缺陷修复 | fix(processor): support InternS1 text_config in InternVL processor (#17040) | `python/sglang/srt/multimodal/processors/internvl.py` |

## 逐 Commit 审计卡

### Commit `3e7ecb78a` - model: support interns1-pro (#18145)

- 完整 hash: `3e7ecb78a60f8e1d889cfe25c88006577783d903`
- 时间/作者: 2026-02-05 / RunningLeon
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/interns1pro.py`, `python/sglang/srt/models/qwen3_vl_moe.py`, `python/sglang/srt/multimodal/processors/interns1pro.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/multimodal/processors/interns1pro.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/interns1pro.py`
  - runtime-perf: `python/sglang/srt/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `539924037` - fix(processor): support InternS1 text_config in InternVL processor (#17040)

- 完整 hash: `539924037fbc6b64a75c554ed338cb8c5abe5343`
- 时间/作者: 2026-01-26 / Mahdi-CV
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/multimodal/processors/internvl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。
