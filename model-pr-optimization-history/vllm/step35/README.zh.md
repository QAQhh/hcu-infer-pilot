# vllm Step 3.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/models/multimodal/processing/test_step3_vl_image_embeds.py` | 无直接 PR 号提交 |
| `tests/parser/engine/test_step3p5.py` | [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `tests/reasoning/test_step3p5_reasoning_parser.py` | [#34211](https://github.com/vllm-project/vllm/pull/34211), [#53174](https://github.com/vllm-project/vllm/pull/53174), [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `tests/tool_parsers/test_step3p5_tool_parser.py` | [#33690](https://github.com/vllm-project/vllm/pull/33690), [#51810](https://github.com/vllm-project/vllm/pull/51810), [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/model_executor/models/step3_text.py` | 无直接 PR 号提交 |
| `vllm/model_executor/models/step3_vl.py` | 无直接 PR 号提交 |
| `vllm/model_executor/models/step3p5.py` | [#33523](https://github.com/vllm-project/vllm/pull/33523), [#33755](https://github.com/vllm-project/vllm/pull/33755), [#34478](https://github.com/vllm-project/vllm/pull/34478), [#41892](https://github.com/vllm-project/vllm/pull/41892) |
| `vllm/model_executor/models/step3p5_mtp.py` | [#33523](https://github.com/vllm-project/vllm/pull/33523), [#48883](https://github.com/vllm-project/vllm/pull/48883) |
| `vllm/parser/step3p5.py` | [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/reasoning/step3p5_engine_reasoning_parser.py` | [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/tool_parsers/step3p5_tool_parser.py` | [#33523](https://github.com/vllm-project/vllm/pull/33523), [#33690](https://github.com/vllm-project/vllm/pull/33690), [#51810](https://github.com/vllm-project/vllm/pull/51810), [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/transformers_utils/configs/step3_vl.py` | 无直接 PR 号提交 |
| `vllm/transformers_utils/processors/step3_vl.py` | 无直接 PR 号提交 |
| `vllm/v1/spec_decode/step3p5.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 10
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 10

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-01 | [#59321](https://github.com/vllm-project/vllm/pull/59321) | merged | [Frontend] Port Step-3.5 parsers to the streaming parser engine | `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/reasoning/test_step3p5_reasoning_parser.py` |
| 2026-09-29 | [#51810](https://github.com/vllm-project/vllm/pull/51810) | merged | [Bugfix] Route Step3p5 forced tool choices through XML parser | `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py` |
| 2026-09-09 | [#53174](https://github.com/vllm-project/vllm/pull/53174) | merged | [Bugfix] Fix Step-3.5 reasoning parser for structured outputs | `tests/reasoning/test_step3p5_reasoning_parser.py` |
| 2026-07-29 | [#48883](https://github.com/vllm-project/vllm/pull/48883) | merged | fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix | `vllm/model_executor/models/step3p5_mtp.py` |
| 2026-05-13 | [#41892](https://github.com/vllm-project/vllm/pull/41892) | merged | [Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports) | `vllm/model_executor/models/step3p5.py` |
| 2026-02-25 | [#34211](https://github.com/vllm-project/vllm/pull/34211) | merged | [Bugfix] Fix step3p5 reasoning with interleaved thinking | `tests/reasoning/test_step3p5_reasoning_parser.py` |
| 2026-02-22 | [#34478](https://github.com/vllm-project/vllm/pull/34478) | merged | [Model] Add NVFP4 quantization support for Step3.5-Flash | `vllm/model_executor/models/step3p5.py` |
| 2026-02-07 | [#33755](https://github.com/vllm-project/vllm/pull/33755) | merged | [Model] Enable Step3p5ForCausalLM testing | `vllm/model_executor/models/step3p5.py` |
| 2026-02-05 | [#33690](https://github.com/vllm-project/vllm/pull/33690) | merged | [Bugfix] Fix step3p5 parser when using mtp | `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py` |
| 2026-02-02 | [#33523](https://github.com/vllm-project/vllm/pull/33523) | merged | [Models] Step-3.5-Flash | `vllm/tool_parsers/step3p5_tool_parser.py`, `vllm/model_executor/models/step3p5.py`, `vllm/model_executor/models/step3p5_mtp.py` |

## 逐 PR diff 审计卡

### PR #59321 - [Frontend] Port Step-3.5 parsers to the streaming parser engine

- 链接: https://github.com/vllm-project/vllm/pull/59321
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/engine/test_step3p5.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/parser/step3p5.py`, `vllm/reasoning/step3p5_engine_reasoning_parser.py` 等 6 个文件；关联提交 `a5105dba0561`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+236/-1647，可读 patch 2026 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Frontend] Port Step-3.5 parsers to the streaming parser engine」；模型线: Step 3.5；类别: 文档/测试/CI；主要 diff: `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`；技术摘要: 覆盖「[Frontend] Port Step-3.5 parsers to the streaming parser engine」；主要实现面是 `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/step3p5_tool_parser.py` modified +2/-1458 (1460 lines); hunks: -1,1464 +1,8; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks，涉及 `StreamingXMLToolCallParser, __init__, reset_streaming_state`；`tests/tool_parsers/test_step3p5_tool_parser.py` modified +12/-57 (69 lines); hunks: -847,7 +847,7 @@ def test_extract_tool_calls_streaming_incremental(; -867,43 +867,6 @@ def test_extract_tool_calls_streaming_incremental(; symbols: test_extract_tool_calls_streaming_incremental, test_extract_tool_calls_complex_type_with_single_quote, test_extract_tool_calls_streaming_mixed_content_and_multiple_tool_calls, test_extract_tool_calls_non_streaming_mixed_content_and_multiple_tool_calls，涉及 `test_extract_tool_calls_streaming_incremental, test_extract_tool_calls_complex_type_with_single_quote, test_extract_tool_calls_streaming_mixed_content_and_multiple_tool_calls`；`tests/reasoning/test_step3p5_reasoning_parser.py` modified +9/-9 (18 lines); hunks: -4,8 +4,8; -112,7 +112,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning，涉及 `step3p5_tokenizer, test_reasoning`；`vllm/reasoning/step3p5_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6。
- 代码 diff 细节:
  - `vllm/tool_parsers/step3p5_tool_parser.py` modified +2/-1458 (1460 lines); hunks: -1,1464 +1,8; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks
  - `tests/tool_parsers/test_step3p5_tool_parser.py` modified +12/-57 (69 lines); hunks: -847,7 +847,7 @@ def test_extract_tool_calls_streaming_incremental(; -867,43 +867,6 @@ def test_extract_tool_calls_streaming_incremental(; symbols: test_extract_tool_calls_streaming_incremental, test_extract_tool_calls_complex_type_with_single_quote, test_extract_tool_calls_streaming_mixed_content_and_multiple_tool_calls, test_extract_tool_calls_non_streaming_mixed_content_and_multiple_tool_calls
  - `tests/reasoning/test_step3p5_reasoning_parser.py` modified +9/-9 (18 lines); hunks: -4,8 +4,8; -112,7 +112,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning
  - `vllm/reasoning/step3p5_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `tests/parser/engine/test_step3p5.py` added +122/-0 (122 lines); hunks: -0,0 +1,122; symbols: mock_tokenizer, parser, test_parser_names_resolve_to_engine_adapters, test_enable_thinking_false_is_ignored
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/step3p5_tool_parser.py
@@ -1,1464 +1,8 @@
-import json
-from collections.abc import Sequence
-from typing import Any
-from xml.parsers.expat import ParserCreate
-import regex as re
+from vllm.parser.engine.registered_adapters import Step3p5ParserToolAdapter
diff -- tests/tool_parsers/test_step3p5_tool_parser.py
@@ -847,7 +847,7 @@ def test_extract_tool_calls_streaming_incremental(
-            assert chunk.tool_calls[0].function.arguments == ""
+            assert not chunk.tool_calls[0].function.arguments
@@ -867,43 +867,6 @@ def test_extract_tool_calls_streaming_incremental(
-def test_extract_tool_calls_complex_type_with_single_quote(step3p5_tokenizer):
-    """Test parameter type conversion based on tool schema."""
-    tools = [
diff -- tests/reasoning/test_step3p5_reasoning_parser.py
@@ -4,8 +4,8 @@
```

- 已读文件:
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` modified +2/-1458; `vllm/reasoning/step3p5_engine_reasoning_parser.py` added +6/-0; `vllm/parser/step3p5.py` added +49/-0
  - tests: `tests/tool_parsers/test_step3p5_tool_parser.py` modified +12/-57; `tests/reasoning/test_step3p5_reasoning_parser.py` modified +9/-9; `tests/parser/engine/test_step3p5.py` added +122/-0
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_step3p5.py`, `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51810 - [Bugfix] Route Step3p5 forced tool choices through XML parser

- 链接: https://github.com/vllm-project/vllm/pull/51810
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`；关联提交 `5e887a078b76`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+83/-82，可读 patch 240 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Route Step3p5 forced tool choices through XML parser」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Route Step3p5 forced tool choices through XML parser」；主要实现面是 `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/step3p5_tool_parser.py` modified +15/-61 (76 lines); hunks: -22,7 +22,11; -421,43 +425,14 @@ def _fix_missing_equals_in_function_tag(self, chunk: str)...; symbols: _fix_missing_equals_in_function_tag, _validate_function_name, _validate_parameter_name, _should_skip_element，涉及 `_fix_missing_equals_in_function_tag, _validate_function_name, _validate_parameter_name`；`tests/tool_parsers/test_step3p5_tool_parser.py` modified +25/-21 (46 lines); hunks: -5,6 +5,7; -386,26 +387,29 @@ def test_extract_tool_calls_fallback_no_tags(step3p5_tool_...; symbols: test_extract_tool_calls_fallback_no_tags, test_extract_tool_calls_type_conversion，涉及 `test_extract_tool_calls_fallback_no_tags, test_extract_tool_calls_type_conversion`。
- 代码 diff 细节:
  - `vllm/tool_parsers/step3p5_tool_parser.py` modified +15/-61 (76 lines); hunks: -22,7 +22,11; -421,43 +425,14 @@ def _fix_missing_equals_in_function_tag(self, chunk: str)...; symbols: _fix_missing_equals_in_function_tag, _validate_function_name, _validate_parameter_name, _should_skip_element
  - `tests/tool_parsers/test_step3p5_tool_parser.py` modified +25/-21 (46 lines); hunks: -5,6 +5,7; -386,26 +387,29 @@ def test_extract_tool_calls_fallback_no_tags(step3p5_tool_...; symbols: test_extract_tool_calls_fallback_no_tags, test_extract_tool_calls_type_conversion
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/step3p5_tool_parser.py
@@ -22,7 +22,11 @@
-from vllm.tool_parsers.utils import safe_literal_eval
+from vllm.tool_parsers.utils import (
+    find_tool_name,
+    find_tool_properties,
+    safe_literal_eval,
+)
diff -- tests/tool_parsers/test_step3p5_tool_parser.py
@@ -5,6 +5,7 @@
+from openai.types.responses import FunctionTool
@@ -386,26 +387,29 @@ def test_extract_tool_calls_fallback_no_tags(step3p5_tool_parser, sample_tools):
-def test_extract_tool_calls_type_conversion(step3p5_tokenizer):
-    """Test parameter type conversion based on tool schema."""
-    tools = [
-        ChatCompletionToolsParam(
```

- 已读文件:
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` modified +15/-61
  - tests: `tests/tool_parsers/test_step3p5_tool_parser.py` modified +25/-21
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/tool_parsers/test_structural_tag_registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #53174 - [Bugfix] Fix Step-3.5 reasoning parser for structured outputs

- 链接: https://github.com/vllm-project/vllm/pull/53174
- 状态/时间: merged / 2026-09-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_step3p5_reasoning_parser.py`；关联提交 `26fec6d183c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+26/-91，可读 patch 201 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Step-3.5 reasoning parser for structured outputs」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `tests/reasoning/test_step3p5_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix] Fix Step-3.5 reasoning parser for structured outputs」；主要实现面是 `tests/reasoning/test_step3p5_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_step3p5_reasoning_parser.py` modified +20/-23 (43 lines); hunks: -25,12 +25,11 @@ def step3p5_tokenizer():; -72,7 +71,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning，涉及 `step3p5_tokenizer, test_reasoning`。
- 代码 diff 细节:
  - `tests/reasoning/test_step3p5_reasoning_parser.py` modified +20/-23 (43 lines); hunks: -25,12 +25,11 @@ def step3p5_tokenizer():; -72,7 +71,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_step3p5_reasoning_parser.py
@@ -25,12 +25,11 @@ def step3p5_tokenizer():
-# need to get into parser again to remove newline after </think>
-    "is_reasoning_end": False,
+    "is_reasoning_end": True,
@@ -72,7 +71,7 @@ def step3p5_tokenizer():
-    "is_reasoning_end": False,
+    "is_reasoning_end": True,
```

- 已读文件:
  - tests: `tests/reasoning/test_step3p5_reasoning_parser.py` modified +20/-23
- 验证与风险: diff 自带测试面 `tests/reasoning/test_step3p5_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #48883 - fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix

- 链接: https://github.com/vllm-project/vllm/pull/48883
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/step3p5_mtp.py`；关联提交 `f98061ce6cb0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-2，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/step3p5_mtp.py`；技术摘要: 覆盖「fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix」；主要实现面是 `vllm/model_executor/models/step3p5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/step3p5_mtp.py` modified +11/-2 (13 lines); hunks: -32,11 +32,18 @@ def __init__(; -55,7 +62,9 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/step3p5_mtp.py` modified +11/-2 (13 lines); hunks: -32,11 +32,18 @@ def __init__(; -55,7 +62,9 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/step3p5_mtp.py
@@ -32,11 +32,18 @@ def __init__(
+        prefix: str = "",
+        # Give the head its prefix so the quant config's exclude_modules matcher
+        # can skip it; without one it defaults to "" and never matches, so a
+        # checkpoint-excluded (BF16) MTP head gets quantized -> load crash.
-            config.vocab_size, config.hidden_size, quant_config=quant_config
+            config.vocab_size,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/step3p5_mtp.py` modified +11/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/step3p5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41892 - [Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports)

- 链接: https://github.com/vllm-project/vllm/pull/41892
- 状态/时间: merged / 2026-05-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/step3p5.py`；关联提交 `3b1ef03be4a3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+46/-4，可读 patch 97 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports)」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/step3p5.py`；技术摘要: 覆盖「[Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports)」；主要实现面是 `vllm/model_executor/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/step3p5.py` modified +6/-0 (6 lines); hunks: -817,6 +817,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, Step3p5ForCausalLM，涉及 `load_weights, Step3p5ForCausalLM`。
- 代码 diff 细节:
  - `vllm/model_executor/models/step3p5.py` modified +6/-0 (6 lines); hunks: -817,6 +817,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, Step3p5ForCausalLM
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/step3p5.py
@@ -817,6 +817,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+    # Required so quantization exclude lists match fused module prefixes.
+    packed_modules_mapping = {
+        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
+        "gate_up_proj": ["gate_proj", "up_proj"],
+    }
```

- 已读文件:
  - runtime: `vllm/model_executor/models/step3p5.py` modified +6/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_w8a8_int8.py`, `vllm/model_executor/models/step3p5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34211 - [Bugfix] Fix step3p5 reasoning with interleaved thinking

- 链接: https://github.com/vllm-project/vllm/pull/34211
- 状态/时间: merged / 2026-02-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_step3p5_reasoning_parser.py`；关联提交 `af5e6afa0af2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+387/-14，可读 patch 423 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix step3p5 reasoning with interleaved thinking」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `tests/reasoning/test_step3p5_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix] Fix step3p5 reasoning with interleaved thinking」；主要实现面是 `tests/reasoning/test_step3p5_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_step3p5_reasoning_parser.py` added +341/-0 (341 lines); hunks: -0,0 +1,341; symbols: step3p5_tokenizer, test_reasoning, test_step3p5_streaming_drops_leading_newline，涉及 `step3p5_tokenizer, test_reasoning, test_step3p5_streaming_drops_leading_newline`。
- 代码 diff 细节:
  - `tests/reasoning/test_step3p5_reasoning_parser.py` added +341/-0 (341 lines); hunks: -0,0 +1,341; symbols: step3p5_tokenizer, test_reasoning, test_step3p5_streaming_drops_leading_newline
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_step3p5_reasoning_parser.py
@@ -0,0 +1,341 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from transformers import AutoTokenizer
+from tests.reasoning.utils import run_reasoning_extraction
+from vllm.reasoning import ReasoningParser, ReasoningParserManager
```

- 已读文件:
  - tests: `tests/reasoning/test_step3p5_reasoning_parser.py` added +341/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_step3p5_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #34478 - [Model] Add NVFP4 quantization support for Step3.5-Flash

- 链接: https://github.com/vllm-project/vllm/pull/34478
- 状态/时间: merged / 2026-02-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/step3p5.py`；关联提交 `b7892a3beff0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+204/-4，可读 patch 291 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add NVFP4 quantization support for Step3.5-Flash」；模型线: Step 3.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/step3p5.py`；技术摘要: 覆盖「[Model] Add NVFP4 quantization support for Step3.5-Flash」；主要实现面是 `vllm/model_executor/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/step3p5.py` modified +71/-1 (72 lines); hunks: -2,7 +2,8; -231,6 +232,7 @@ def __init__(; symbols: __init__, load_weights，涉及 `__init__, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/step3p5.py` modified +71/-1 (72 lines); hunks: -2,7 +2,8; -231,6 +232,7 @@ def __init__(; symbols: __init__, load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/step3p5.py
@@ -2,7 +2,8 @@
-from collections.abc import Iterable
+import typing
+from collections.abc import Callable, Iterable
@@ -231,6 +232,7 @@ def __init__(
+                quant_config=quant_config,
@@ -640,12 +642,22 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/step3p5.py` modified +71/-1
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_nvfp4_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33755 - [Model] Enable Step3p5ForCausalLM testing

- 链接: https://github.com/vllm-project/vllm/pull/33755
- 状态/时间: merged / 2026-02-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/step3p5.py`；关联提交 `db4ede974343`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+28/-32，可读 patch 115 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Enable Step3p5ForCausalLM testing」；模型线: Step 3.5；类别: 文档/测试/CI；主要 diff: `vllm/model_executor/models/step3p5.py`；技术摘要: 覆盖「[Model] Enable Step3p5ForCausalLM testing」；主要实现面是 `vllm/model_executor/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/step3p5.py` modified +12/-25 (37 lines); hunks: -36,7 +36,6; -770,37 +769,17 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/step3p5.py` modified +12/-25 (37 lines); hunks: -36,7 +36,6; -770,37 +769,17 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/step3p5.py
@@ -36,7 +36,6 @@
-    DEFAULT_VOCAB_PADDING_SIZE,
@@ -770,37 +769,17 @@ def __init__(
-        lora_config = vllm_config.lora_config
-        self.config = config
-        self.vllm_config = vllm_config
-        self.moe_layers: list[FusedMoEBlock] = []
```

- 已读文件:
  - runtime: `vllm/model_executor/models/step3p5.py` modified +12/-25
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33690 - [Bugfix] Fix step3p5 parser when using mtp

- 链接: https://github.com/vllm-project/vllm/pull/33690
- 状态/时间: merged / 2026-02-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`；关联提交 `82914d2ae8d0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+1455/-5，可读 patch 1508 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix step3p5 parser when using mtp」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Fix step3p5 parser when using mtp」；主要实现面是 `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_step3p5_tool_parser.py` added +1435/-0 (1435 lines); hunks: -0,0 +1,1435; symbols: step3p5_tokenizer, step3p5_tool_parser, sample_tools, assert_tool_calls，涉及 `step3p5_tokenizer, step3p5_tool_parser, sample_tools`；`vllm/tool_parsers/step3p5_tool_parser.py` modified +20/-5 (25 lines); hunks: -97,11 +97,26 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; -110,7 +125,7 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; symbols: parse_single_streaming_chunks，涉及 `parse_single_streaming_chunks`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_step3p5_tool_parser.py` added +1435/-0 (1435 lines); hunks: -0,0 +1,1435; symbols: step3p5_tokenizer, step3p5_tool_parser, sample_tools, assert_tool_calls
  - `vllm/tool_parsers/step3p5_tool_parser.py` modified +20/-5 (25 lines); hunks: -97,11 +97,26 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; -110,7 +125,7 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; symbols: parse_single_streaming_chunks
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_step3p5_tool_parser.py
@@ -0,0 +1,1435 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import json
+from collections.abc import Generator
+import pytest
+from vllm.entrypoints.openai.chat_completion.protocol import (
diff -- vllm/tool_parsers/step3p5_tool_parser.py
@@ -97,11 +97,26 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> DeltaMessage:
+        entry_call_id = self.current_call_id
+        entry_tool_call_index = self.tool_call_index
+        fallback_call_id = None
+        if entry_call_id is not None:
+            if (
+                self.current_call_id == entry_call_id
```

- 已读文件:
  - tests: `tests/tool_parsers/test_step3p5_tool_parser.py` added +1435/-0
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` modified +20/-5
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_step3p5_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33523 - [Models] Step-3.5-Flash

- 链接: https://github.com/vllm-project/vllm/pull/33523
- 状态/时间: merged / 2026-02-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/step3p5.py`, `vllm/model_executor/models/step3p5_mtp.py`, `vllm/tool_parsers/step3p5_tool_parser.py`；关联提交 `c3b40dc3e74d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 18 个文件，+3107/-4，可读 patch 3270 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Models] Step-3.5-Flash」；模型线: Step 3.5；类别: 性能/后端优化；主要 diff: `vllm/tool_parsers/step3p5_tool_parser.py`, `vllm/model_executor/models/step3p5.py`, `vllm/model_executor/models/step3p5_mtp.py`；技术摘要: 覆盖「[Models] Step-3.5-Flash」；主要实现面是 `vllm/tool_parsers/step3p5_tool_parser.py`, `vllm/model_executor/models/step3p5.py`, `vllm/model_executor/models/step3p5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/step3p5_tool_parser.py` added +1511/-0 (1511 lines); hunks: -0,0 +1,1511; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks，涉及 `StreamingXMLToolCallParser, __init__, reset_streaming_state`；`vllm/model_executor/models/step3p5.py` added +894/-0 (894 lines); hunks: -0,0 +1,894; symbols: FP32ReplicatedLinear, forward, Step3p5MLP, __init__，涉及 `FP32ReplicatedLinear, forward, Step3p5MLP`；`vllm/model_executor/models/step3p5_mtp.py` added +315/-0 (315 lines); hunks: -0,0 +1,315; symbols: SharedHead, __init__, forward, Step3p5AMultiTokenPredictorLayer，涉及 `SharedHead, __init__, forward`；`vllm/transformers_utils/configs/step3p5.py` added +100/-0 (100 lines); hunks: -0,0 +1,100; symbols: Step3p5Config, __init__，涉及 `Step3p5Config, __init__`。
- 代码 diff 细节:
  - `vllm/tool_parsers/step3p5_tool_parser.py` added +1511/-0 (1511 lines); hunks: -0,0 +1,1511; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks
  - `vllm/model_executor/models/step3p5.py` added +894/-0 (894 lines); hunks: -0,0 +1,894; symbols: FP32ReplicatedLinear, forward, Step3p5MLP, __init__
  - `vllm/model_executor/models/step3p5_mtp.py` added +315/-0 (315 lines); hunks: -0,0 +1,315; symbols: SharedHead, __init__, forward, Step3p5AMultiTokenPredictorLayer
  - `vllm/transformers_utils/configs/step3p5.py` added +100/-0 (100 lines); hunks: -0,0 +1,100; symbols: Step3p5Config, __init__
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/step3p5_tool_parser.py
@@ -0,0 +1,1511 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import ast
+import json
+from collections.abc import Sequence
+from typing import Any
diff -- vllm/model_executor/models/step3p5.py
@@ -0,0 +1,894 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only Jurassic model."""
+from collections.abc import Iterable
+from typing import Any
+import torch
diff -- vllm/model_executor/models/step3p5_mtp.py
@@ -0,0 +1,315 @@
```

- 已读文件:
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` added +1511/-0; `vllm/model_executor/models/step3p5.py` added +894/-0; `vllm/model_executor/models/step3p5_mtp.py` added +315/-0; `vllm/transformers_utils/configs/step3p5.py` added +100/-0
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_activation.py`, `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
