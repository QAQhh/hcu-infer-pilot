# vllm Qwen3.5 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `vllm/model_executor/models/qwen3_5.py` | `4dc838d3e`, `843c1822d` |
| `vllm/model_executor/models/qwen3_5_mtp.py` | `4dc838d3e`, `843c1822d` |
| `vllm/transformers_utils/configs/qwen3_5.py` | `4dc838d3e` |
| `vllm/transformers_utils/configs/qwen3_5_moe.py` | `4dc838d3e` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 7
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-23 | `be03cbe82` | 缺陷修复 | [BugFix] 合入官方pr，修复Qwen3/Qwen3.5 tool calling 不能正确调用工具的bug (github #36774) | `vllm/tool_parsers/qwen3coder_tool_parser.py` |
| 2026-03-16 | `b5ca585e7` | 通用实现调整 | Merge branch 'v0.15.1-dev-qwen3.5' into 'v0.15.1-dev' |  |
| 2026-03-16 | `9c122e36b` | 缺陷修复 | Fix Qwen3/Qwen3.5 Reasoning Parser (#34779) | `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py` |
| 2026-02-28 | `b5e8d01eb` | 缺陷修复 | 修复qwen3.5的使用dtype为fp16的picecwise的推理模式 | `vllm/model_executor/layers/layernorm.py` |
| 2026-02-24 | `35006c0f1` | 通用实现调整 | Merge branch '0.15.1-dev-qwen3_5' into 'v0.15.1-dev' |  |
| 2026-02-16 | `4dc838d3e` | 性能/后端优化 | add qwen3_5 | `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-16 | `843c1822d` | 调度/缓存/PD | Add qwen3_5 | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py` |

## 逐 Commit 审计卡

### Commit `be03cbe82` - [BugFix] 合入官方pr，修复Qwen3/Qwen3.5 tool calling 不能正确调用工具的bug (github #36774)

- 完整 hash: `be03cbe824b2af6999dbbc3c92f6cbe270cb0116`
- 时间/作者: 2026-03-23 / jujil
- 自动分类: 缺陷修复
- 主要文件: `vllm/tool_parsers/qwen3coder_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tool_parsers/qwen3coder_tool_parser.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b5ca585e7` - Merge branch 'v0.15.1-dev-qwen3.5' into 'v0.15.1-dev'

- 完整 hash: `b5ca585e76a7fd8ac9211db1c6f7618f42b914ec`
- 时间/作者: 2026-03-16 / zhangqha
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `9c122e36b` - Fix Qwen3/Qwen3.5 Reasoning Parser  (#34779)

- 完整 hash: `9c122e36b5d6e6a2a333cc9bdecf9ca0cc147abe`
- 时间/作者: 2026-03-16 / jujil
- 自动分类: 缺陷修复
- 主要文件: `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/reasoning/qwen3_reasoning_parser.py`
  - runtime-model: `vllm/entrypoints/openai/chat_completion/serving.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b5e8d01eb` - 修复qwen3.5的使用dtype为fp16的picecwise的推理模式

- 完整 hash: `b5e8d01ebde8ea1a2d82d014d62a96a9e5fd1e2a`
- 时间/作者: 2026-02-28 / yangql1
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/layernorm.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `35006c0f1` - Merge branch '0.15.1-dev-qwen3_5' into 'v0.15.1-dev'

- 完整 hash: `35006c0f17ed9d6210875c9b51d106920f1a16c8`
- 时间/作者: 2026-02-24 / zhuwenwen
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `4dc838d3e` - add qwen3_5

- 完整 hash: `4dc838d3e0bfb95155155f658a227d1958ca371c`
- 时间/作者: 2026-02-16 / Rayyyyy
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/qwen3_5.py`, `vllm/transformers_utils/configs/qwen3_5_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_utils.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/qwen3_5.py`; `vllm/model_executor/models/qwen3_5_mtp.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/qwen3_5.py`
  - runtime-perf: `vllm/transformers_utils/configs/qwen3_5_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `843c1822d` - Add qwen3_5

- 完整 hash: `843c1822de92edd962da42bbc490512a60aadbd5`
- 时间/作者: 2026-02-16 / Rayyyyy
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/speculative.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/models/qwen3_5.py`; `vllm/model_executor/models/qwen3_5_mtp.py`; `vllm/model_executor/models/qwen3_next.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/model_arch_config_convertor.py`
  - tests: `tests/models/registry.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
