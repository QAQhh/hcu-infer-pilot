# vllm Qwen3.5 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `vllm/model_executor/models/qwen3_5.py` | `4dc838d3e`, `843c1822d` |
| `vllm/model_executor/models/qwen3_5_mtp.py` | `4dc838d3e`, `843c1822d` |
| `vllm/transformers_utils/configs/qwen3_5.py` | `4dc838d3e` |
| `vllm/transformers_utils/configs/qwen3_5_moe.py` | `4dc838d3e` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 7
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-23 | `be03cbe82` | 缺陷修复 | [BugFix] 合入官方pr，修复Qwen3/Qwen3.5 tool calling 不能正确调用工具的bug (github #36774) | `vllm/tool_parsers/qwen3coder_tool_parser.py` |
| 2026-03-16 | `b5ca585e7` | 通用实现调整 | Merge branch 'v0.15.1-dev-qwen3.5' into 'v0.15.1-dev' |  |
| 2026-03-16 | `9c122e36b` | 缺陷修复 | Fix Qwen3/Qwen3.5 Reasoning Parser (#34779) | `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py` |
| 2026-02-28 | `b5e8d01eb` | 缺陷修复 | 修复qwen3.5的使用dtype为fp16的picecwise的推理模式 | `vllm/model_executor/layers/layernorm.py` |
| 2026-02-24 | `35006c0f1` | 通用实现调整 | Merge branch '0.15.1-dev-qwen3_5' into 'v0.15.1-dev' |  |
| 2026-02-16 | `4dc838d3e` | 性能/后端优化 | add qwen3_5 | `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-16 | `843c1822d` | 调度/缓存/PD | Add qwen3_5 | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py` |

## Per-Commit Audit Cards

### Commit `be03cbe82` - [BugFix] 合入官方pr，修复Qwen3/Qwen3.5 tool calling 不能正确调用工具的bug (github #36774)

- Full hash: `be03cbe824b2af6999dbbc3c92f6cbe270cb0116`
- Date/author: 2026-03-23 / jujil
- Auto category: 缺陷修复
- Main files: `vllm/tool_parsers/qwen3coder_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tool_parsers/qwen3coder_tool_parser.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `b5ca585e7` - Merge branch 'v0.15.1-dev-qwen3.5' into 'v0.15.1-dev'

- Full hash: `b5ca585e76a7fd8ac9211db1c6f7618f42b914ec`
- Date/author: 2026-03-16 / zhangqha
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `9c122e36b` - Fix Qwen3/Qwen3.5 Reasoning Parser  (#34779)

- Full hash: `9c122e36b5d6e6a2a333cc9bdecf9ca0cc147abe`
- Date/author: 2026-03-16 / jujil
- Auto category: 缺陷修复
- Main files: `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/qwen3_reasoning_parser.py`
  - runtime-model: `vllm/entrypoints/openai/chat_completion/serving.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b5e8d01eb` - 修复qwen3.5的使用dtype为fp16的picecwise的推理模式

- Full hash: `b5e8d01ebde8ea1a2d82d014d62a96a9e5fd1e2a`
- Date/author: 2026-02-28 / yangql1
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/layernorm.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `35006c0f1` - Merge branch '0.15.1-dev-qwen3_5' into 'v0.15.1-dev'

- Full hash: `35006c0f17ed9d6210875c9b51d106920f1a16c8`
- Date/author: 2026-02-24 / zhuwenwen
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `4dc838d3e` - add qwen3_5

- Full hash: `4dc838d3e0bfb95155155f658a227d1958ca371c`
- Date/author: 2026-02-16 / Rayyyyy
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/qwen3_5.py`, `vllm/transformers_utils/configs/qwen3_5_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_utils.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/qwen3_5.py`; `vllm/model_executor/models/qwen3_5_mtp.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/qwen3_5.py`
  - runtime-perf: `vllm/transformers_utils/configs/qwen3_5_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `843c1822d` - Add qwen3_5

- Full hash: `843c1822de92edd962da42bbc490512a60aadbd5`
- Date/author: 2026-02-16 / Rayyyyy
- Auto category: 调度/缓存/PD
- Main files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/speculative.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/models/qwen3_5.py`; `vllm/model_executor/models/qwen3_5_mtp.py`; `vllm/model_executor/models/qwen3_next.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/model_arch_config_convertor.py`
  - tests: `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
