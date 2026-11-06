# vllm DeepSeek V3.1 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `examples/ray_serving/elastic_ep/serve_deepseek_v2.sh` | 无直接 PR 号提交 |
| `examples/tool_chat_template_deepseekv31.jinja` | [#23454](https://github.com/vllm-project/vllm/pull/23454) |
| `tests/tool_parsers/test_deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `vllm/model_executor/models/deepseek_mtp.py` | 无直接 PR 号提交 |
| `vllm/model_executor/models/deepseek_v2.py` | 无直接 PR 号提交 |
| `vllm/tool_parsers/deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |

## PR 覆盖总览

- git 追溯 PR 数: 2
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 2

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-19 | [#60362](https://github.com/vllm-project/vllm/pull/60362) | merged | [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers | `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py` |
| 2025-08-23 | [#23454](https://github.com/vllm-project/vllm/pull/23454) | merged | Support DeepSeek-V3.1 tool call | `examples/tool_chat_template_deepseekv31.jinja` |

## 逐 PR diff 审计卡

### PR #60362 - [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers

- 链接: https://github.com/vllm-project/vllm/pull/60362
- 状态/时间: merged / 2026-10-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`；关联提交 `e347836d68be`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+55/-4，可读 patch 108 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers」；模型线: DeepSeek V3.1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`；技术摘要: 覆盖「[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers」；主要实现面是 `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments，涉及 `test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments`；`vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments
  - `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv31_tool_parser.py
@@ -1,8 +1,11 @@
+import json
+from tests.tool_parsers.utils import run_tool_extraction
@@ -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):
+@pytest.mark.parametrize("streaming", [True, False])
+def test_extract_tool_calls_with_multiline_arguments(parser, streaming):
+    # The model may pretty-print the JSON arguments over several lines.
diff -- vllm/tool_parsers/deepseekv31_tool_parser.py
@@ -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Tool] | None = None):
+        # The arguments may be pretty-printed over several lines.
-            r"<｜tool▁call▁begin｜>(?P<function_name>.*?)<｜tool▁sep｜>(?P<function_arguments>.*?)<｜tool▁call▁end｜>"
+            r"<｜tool▁call▁begin｜>(?P<function_name>.*?)<｜tool▁sep｜>(?P<function_arguments>[\s\S]*?)<｜tool▁call▁end｜>"
-            r"(?P<function_name>.*)<｜tool▁sep｜>(?P<function_arguments>.*)"
+            r"(?P<function_name>.*)<｜tool▁sep｜>(?P<function_arguments>[\s\S]*)"
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0
  - runtime: `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_deepseekv3_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23454 - Support DeepSeek-V3.1 tool call

- 链接: https://github.com/vllm-project/vllm/pull/23454
- 状态/时间: merged / 2025-08-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/tool_chat_template_deepseekv31.jinja`；关联提交 `b8f17f5d980e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+468/-0，可读 patch 491 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support DeepSeek-V3.1 tool call」；模型线: DeepSeek V3.1；类别: 模型支持/运行时入口；主要 diff: `examples/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「Support DeepSeek-V3.1 tool call」；主要实现面是 `examples/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91。
- 代码 diff 细节:
  - `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- 关键代码摘录:

```diff
diff -- examples/tool_chat_template_deepseekv31.jinja
@@ -0,0 +1,91 @@
+{% if not add_generation_prompt is defined %}
+  {% set add_generation_prompt = false %}
+{% endif %}
+{% if not thinking is defined %}
+  {% set thinking = false %}
+{% endif %}
```

- 已读文件:
  - docs: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0
- 验证与风险: runtime 路径改动集中在 `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv31_tool_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
