# vllm DeepSeek V3.1 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `examples/ray_serving/elastic_ep/serve_deepseek_v2.sh` | no direct PR-number commit |
| `examples/tool_chat_template_deepseekv31.jinja` | [#23454](https://github.com/vllm-project/vllm/pull/23454) |
| `tests/tool_parsers/test_deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `vllm/model_executor/models/deepseek_mtp.py` | no direct PR-number commit |
| `vllm/model_executor/models/deepseek_v2.py` | no direct PR-number commit |
| `vllm/tool_parsers/deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |

## PR Coverage Summary

- Git-traced PRs: 2
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 2

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-10-19 | [#60362](https://github.com/vllm-project/vllm/pull/60362) | merged | [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers | `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py` |
| 2025-08-23 | [#23454](https://github.com/vllm-project/vllm/pull/23454) | merged | Support DeepSeek-V3.1 tool call | `examples/tool_chat_template_deepseekv31.jinja` |

## Per-PR Diff Audit Cards

### PR #60362 - [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers

- Link: https://github.com/vllm-project/vllm/pull/60362
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`; associated commits `e347836d68be`
- Diff scope read: GitHub Pull Request files API returned 4 files, +55/-4, 108 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers"; model line: DeepSeek V3.1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`; technical summary: Covers "[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers"; the main implementation surface is `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments, touching `test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments`; `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments
  - `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0
  - runtime: `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_deepseekv3_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #23454 - Support DeepSeek-V3.1 tool call

- Link: https://github.com/vllm-project/vllm/pull/23454
- Status/date: merged / 2025-08-23
- Trace source: `git log --name-only -- <model-files>` found it through `examples/tool_chat_template_deepseekv31.jinja`; associated commits `b8f17f5d980e`
- Diff scope read: GitHub Pull Request files API returned 4 files, +468/-0, 491 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support DeepSeek-V3.1 tool call"; model line: DeepSeek V3.1; category: model support/runtime entry; main diff: `examples/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "Support DeepSeek-V3.1 tool call"; the main implementation surface is `examples/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91.
- Code diff details:
  - `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- Key code excerpts:

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

- Reviewed files:
  - docs: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0
- Risk and verification: Runtime changes concentrate in `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv31_tool_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
