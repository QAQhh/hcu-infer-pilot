# vllm Step 3.5 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/models/multimodal/processing/test_step3_vl_image_embeds.py` | no direct PR-number commit |
| `tests/parser/engine/test_step3p5.py` | [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `tests/reasoning/test_step3p5_reasoning_parser.py` | [#34211](https://github.com/vllm-project/vllm/pull/34211), [#53174](https://github.com/vllm-project/vllm/pull/53174), [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `tests/tool_parsers/test_step3p5_tool_parser.py` | [#33690](https://github.com/vllm-project/vllm/pull/33690), [#51810](https://github.com/vllm-project/vllm/pull/51810), [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/model_executor/models/step3_text.py` | no direct PR-number commit |
| `vllm/model_executor/models/step3_vl.py` | no direct PR-number commit |
| `vllm/model_executor/models/step3p5.py` | [#33523](https://github.com/vllm-project/vllm/pull/33523), [#33755](https://github.com/vllm-project/vllm/pull/33755), [#34478](https://github.com/vllm-project/vllm/pull/34478), [#41892](https://github.com/vllm-project/vllm/pull/41892) |
| `vllm/model_executor/models/step3p5_mtp.py` | [#33523](https://github.com/vllm-project/vllm/pull/33523), [#48883](https://github.com/vllm-project/vllm/pull/48883) |
| `vllm/parser/step3p5.py` | [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/reasoning/step3p5_engine_reasoning_parser.py` | [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/tool_parsers/step3p5_tool_parser.py` | [#33523](https://github.com/vllm-project/vllm/pull/33523), [#33690](https://github.com/vllm-project/vllm/pull/33690), [#51810](https://github.com/vllm-project/vllm/pull/51810), [#59321](https://github.com/vllm-project/vllm/pull/59321) |
| `vllm/transformers_utils/configs/step3_vl.py` | no direct PR-number commit |
| `vllm/transformers_utils/processors/step3_vl.py` | no direct PR-number commit |
| `vllm/v1/spec_decode/step3p5.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 10
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 10

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
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

## Per-PR Diff Audit Cards

### PR #59321 - [Frontend] Port Step-3.5 parsers to the streaming parser engine

- Link: https://github.com/vllm-project/vllm/pull/59321
- Status/date: merged / 2026-10-01
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/engine/test_step3p5.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/parser/step3p5.py`, `vllm/reasoning/step3p5_engine_reasoning_parser.py` and 6 files; associated commits `a5105dba0561`
- Diff scope read: GitHub Pull Request files API returned 12 files, +236/-1647, 2026 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Frontend] Port Step-3.5 parsers to the streaming parser engine"; model line: Step 3.5; category: docs/tests/CI; main diff: `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`; technical summary: Covers "[Frontend] Port Step-3.5 parsers to the streaming parser engine"; the main implementation surface is `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/step3p5_tool_parser.py` modified +2/-1458 (1460 lines); hunks: -1,1464 +1,8; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks, touching `StreamingXMLToolCallParser, __init__, reset_streaming_state`; `tests/tool_parsers/test_step3p5_tool_parser.py` modified +12/-57 (69 lines); hunks: -847,7 +847,7 @@ def test_extract_tool_calls_streaming_incremental(; -867,43 +867,6 @@ def test_extract_tool_calls_streaming_incremental(; symbols: test_extract_tool_calls_streaming_incremental, test_extract_tool_calls_complex_type_with_single_quote, test_extract_tool_calls_streaming_mixed_content_and_multiple_tool_calls, test_extract_tool_calls_non_streaming_mixed_content_and_multiple_tool_calls, touching `test_extract_tool_calls_streaming_incremental, test_extract_tool_calls_complex_type_with_single_quote, test_extract_tool_calls_streaming_mixed_content_and_multiple_tool_calls`; `tests/reasoning/test_step3p5_reasoning_parser.py` modified +9/-9 (18 lines); hunks: -4,8 +4,8; -112,7 +112,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning, touching `step3p5_tokenizer, test_reasoning`; `vllm/reasoning/step3p5_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6.
- Code diff details:
  - `vllm/tool_parsers/step3p5_tool_parser.py` modified +2/-1458 (1460 lines); hunks: -1,1464 +1,8; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks
  - `tests/tool_parsers/test_step3p5_tool_parser.py` modified +12/-57 (69 lines); hunks: -847,7 +847,7 @@ def test_extract_tool_calls_streaming_incremental(; -867,43 +867,6 @@ def test_extract_tool_calls_streaming_incremental(; symbols: test_extract_tool_calls_streaming_incremental, test_extract_tool_calls_complex_type_with_single_quote, test_extract_tool_calls_streaming_mixed_content_and_multiple_tool_calls, test_extract_tool_calls_non_streaming_mixed_content_and_multiple_tool_calls
  - `tests/reasoning/test_step3p5_reasoning_parser.py` modified +9/-9 (18 lines); hunks: -4,8 +4,8; -112,7 +112,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning
  - `vllm/reasoning/step3p5_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `tests/parser/engine/test_step3p5.py` added +122/-0 (122 lines); hunks: -0,0 +1,122; symbols: mock_tokenizer, parser, test_parser_names_resolve_to_engine_adapters, test_enable_thinking_false_is_ignored
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` modified +2/-1458; `vllm/reasoning/step3p5_engine_reasoning_parser.py` added +6/-0; `vllm/parser/step3p5.py` added +49/-0
  - tests: `tests/tool_parsers/test_step3p5_tool_parser.py` modified +12/-57; `tests/reasoning/test_step3p5_reasoning_parser.py` modified +9/-9; `tests/parser/engine/test_step3p5.py` added +122/-0
- Risk and verification: The diff ships test coverage in `tests/parser/engine/test_step3p5.py`, `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_step3p5_reasoning_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #51810 - [Bugfix] Route Step3p5 forced tool choices through XML parser

- Link: https://github.com/vllm-project/vllm/pull/51810
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`; associated commits `5e887a078b76`
- Diff scope read: GitHub Pull Request files API returned 3 files, +83/-82, 240 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Route Step3p5 forced tool choices through XML parser"; model line: Step 3.5; category: bug fix; main diff: `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`; technical summary: Covers "[Bugfix] Route Step3p5 forced tool choices through XML parser"; the main implementation surface is `vllm/tool_parsers/step3p5_tool_parser.py`, `tests/tool_parsers/test_step3p5_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/step3p5_tool_parser.py` modified +15/-61 (76 lines); hunks: -22,7 +22,11; -421,43 +425,14 @@ def _fix_missing_equals_in_function_tag(self, chunk: str)...; symbols: _fix_missing_equals_in_function_tag, _validate_function_name, _validate_parameter_name, _should_skip_element, touching `_fix_missing_equals_in_function_tag, _validate_function_name, _validate_parameter_name`; `tests/tool_parsers/test_step3p5_tool_parser.py` modified +25/-21 (46 lines); hunks: -5,6 +5,7; -386,26 +387,29 @@ def test_extract_tool_calls_fallback_no_tags(step3p5_tool_...; symbols: test_extract_tool_calls_fallback_no_tags, test_extract_tool_calls_type_conversion, touching `test_extract_tool_calls_fallback_no_tags, test_extract_tool_calls_type_conversion`.
- Code diff details:
  - `vllm/tool_parsers/step3p5_tool_parser.py` modified +15/-61 (76 lines); hunks: -22,7 +22,11; -421,43 +425,14 @@ def _fix_missing_equals_in_function_tag(self, chunk: str)...; symbols: _fix_missing_equals_in_function_tag, _validate_function_name, _validate_parameter_name, _should_skip_element
  - `tests/tool_parsers/test_step3p5_tool_parser.py` modified +25/-21 (46 lines); hunks: -5,6 +5,7; -386,26 +387,29 @@ def test_extract_tool_calls_fallback_no_tags(step3p5_tool_...; symbols: test_extract_tool_calls_fallback_no_tags, test_extract_tool_calls_type_conversion
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` modified +15/-61
  - tests: `tests/tool_parsers/test_step3p5_tool_parser.py` modified +25/-21
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/tool_parsers/test_structural_tag_registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53174 - [Bugfix] Fix Step-3.5 reasoning parser for structured outputs

- Link: https://github.com/vllm-project/vllm/pull/53174
- Status/date: merged / 2026-09-09
- Trace source: `git log --name-only -- <model-files>` found it through `tests/reasoning/test_step3p5_reasoning_parser.py`; associated commits `26fec6d183c3`
- Diff scope read: GitHub Pull Request files API returned 2 files, +26/-91, 201 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Step-3.5 reasoning parser for structured outputs"; model line: Step 3.5; category: bug fix; main diff: `tests/reasoning/test_step3p5_reasoning_parser.py`; technical summary: Covers "[Bugfix] Fix Step-3.5 reasoning parser for structured outputs"; the main implementation surface is `tests/reasoning/test_step3p5_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/reasoning/test_step3p5_reasoning_parser.py` modified +20/-23 (43 lines); hunks: -25,12 +25,11 @@ def step3p5_tokenizer():; -72,7 +71,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning, touching `step3p5_tokenizer, test_reasoning`.
- Code diff details:
  - `tests/reasoning/test_step3p5_reasoning_parser.py` modified +20/-23 (43 lines); hunks: -25,12 +25,11 @@ def step3p5_tokenizer():; -72,7 +71,7 @@ def step3p5_tokenizer():; symbols: step3p5_tokenizer, test_reasoning
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/reasoning/test_step3p5_reasoning_parser.py` modified +20/-23
- Risk and verification: The diff ships test coverage in `tests/reasoning/test_step3p5_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #48883 - fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix

- Link: https://github.com/vllm-project/vllm/pull/48883
- Status/date: merged / 2026-07-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/step3p5_mtp.py`; associated commits `f98061ce6cb0`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-2, 31 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix"; model line: Step 3.5; category: bug fix; main diff: `vllm/model_executor/models/step3p5_mtp.py`; technical summary: Covers "fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix"; the main implementation surface is `vllm/model_executor/models/step3p5_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/step3p5_mtp.py` modified +11/-2 (13 lines); hunks: -32,11 +32,18 @@ def __init__(; -55,7 +62,9 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/step3p5_mtp.py` modified +11/-2 (13 lines); hunks: -32,11 +32,18 @@ def __init__(; -55,7 +62,9 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/step3p5_mtp.py` modified +11/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/step3p5_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41892 - [Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports)

- Link: https://github.com/vllm-project/vllm/pull/41892
- Status/date: merged / 2026-05-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/step3p5.py`; associated commits `3b1ef03be4a3`
- Diff scope read: GitHub Pull Request files API returned 3 files, +46/-4, 97 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports)"; model line: Step 3.5; category: bug fix; main diff: `vllm/model_executor/models/step3p5.py`; technical summary: Covers "[Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports)"; the main implementation surface is `vllm/model_executor/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/step3p5.py` modified +6/-0 (6 lines); hunks: -817,6 +817,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, Step3p5ForCausalLM, touching `load_weights, Step3p5ForCausalLM`.
- Code diff details:
  - `vllm/model_executor/models/step3p5.py` modified +6/-0 (6 lines); hunks: -817,6 +817,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, Step3p5ForCausalLM
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/step3p5.py
@@ -817,6 +817,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+    # Required so quantization exclude lists match fused module prefixes.
+    packed_modules_mapping = {
+        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
+        "gate_up_proj": ["gate_proj", "up_proj"],
+    }
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/step3p5.py` modified +6/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_w8a8_int8.py`, `vllm/model_executor/models/step3p5.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34211 - [Bugfix] Fix step3p5 reasoning with interleaved thinking

- Link: https://github.com/vllm-project/vllm/pull/34211
- Status/date: merged / 2026-02-25
- Trace source: `git log --name-only -- <model-files>` found it through `tests/reasoning/test_step3p5_reasoning_parser.py`; associated commits `af5e6afa0af2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +387/-14, 423 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix step3p5 reasoning with interleaved thinking"; model line: Step 3.5; category: bug fix; main diff: `tests/reasoning/test_step3p5_reasoning_parser.py`; technical summary: Covers "[Bugfix] Fix step3p5 reasoning with interleaved thinking"; the main implementation surface is `tests/reasoning/test_step3p5_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/reasoning/test_step3p5_reasoning_parser.py` added +341/-0 (341 lines); hunks: -0,0 +1,341; symbols: step3p5_tokenizer, test_reasoning, test_step3p5_streaming_drops_leading_newline, touching `step3p5_tokenizer, test_reasoning, test_step3p5_streaming_drops_leading_newline`.
- Code diff details:
  - `tests/reasoning/test_step3p5_reasoning_parser.py` added +341/-0 (341 lines); hunks: -0,0 +1,341; symbols: step3p5_tokenizer, test_reasoning, test_step3p5_streaming_drops_leading_newline
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/reasoning/test_step3p5_reasoning_parser.py` added +341/-0
- Risk and verification: The diff ships test coverage in `tests/reasoning/test_step3p5_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #34478 - [Model] Add NVFP4 quantization support for Step3.5-Flash

- Link: https://github.com/vllm-project/vllm/pull/34478
- Status/date: merged / 2026-02-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/step3p5.py`; associated commits `b7892a3beff0`
- Diff scope read: GitHub Pull Request files API returned 5 files, +204/-4, 291 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Add NVFP4 quantization support for Step3.5-Flash"; model line: Step 3.5; category: performance/backend optimization; main diff: `vllm/model_executor/models/step3p5.py`; technical summary: Covers "[Model] Add NVFP4 quantization support for Step3.5-Flash"; the main implementation surface is `vllm/model_executor/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/step3p5.py` modified +71/-1 (72 lines); hunks: -2,7 +2,8; -231,6 +232,7 @@ def __init__(; symbols: __init__, load_weights, touching `__init__, load_weights`.
- Code diff details:
  - `vllm/model_executor/models/step3p5.py` modified +71/-1 (72 lines); hunks: -2,7 +2,8; -231,6 +232,7 @@ def __init__(; symbols: __init__, load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/step3p5.py` modified +71/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_nvfp4_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #33755 - [Model] Enable Step3p5ForCausalLM testing

- Link: https://github.com/vllm-project/vllm/pull/33755
- Status/date: merged / 2026-02-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/step3p5.py`; associated commits `db4ede974343`
- Diff scope read: GitHub Pull Request files API returned 3 files, +28/-32, 115 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Enable Step3p5ForCausalLM testing"; model line: Step 3.5; category: docs/tests/CI; main diff: `vllm/model_executor/models/step3p5.py`; technical summary: Covers "[Model] Enable Step3p5ForCausalLM testing"; the main implementation surface is `vllm/model_executor/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/step3p5.py` modified +12/-25 (37 lines); hunks: -36,7 +36,6; -770,37 +769,17 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/step3p5.py` modified +12/-25 (37 lines); hunks: -36,7 +36,6; -770,37 +769,17 @@ def __init__(; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/step3p5.py` modified +12/-25
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #33690 - [Bugfix] Fix step3p5 parser when using mtp

- Link: https://github.com/vllm-project/vllm/pull/33690
- Status/date: merged / 2026-02-05
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`; associated commits `82914d2ae8d0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +1455/-5, 1508 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix step3p5 parser when using mtp"; model line: Step 3.5; category: bug fix; main diff: `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`; technical summary: Covers "[Bugfix] Fix step3p5 parser when using mtp"; the main implementation surface is `tests/tool_parsers/test_step3p5_tool_parser.py`, `vllm/tool_parsers/step3p5_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_step3p5_tool_parser.py` added +1435/-0 (1435 lines); hunks: -0,0 +1,1435; symbols: step3p5_tokenizer, step3p5_tool_parser, sample_tools, assert_tool_calls, touching `step3p5_tokenizer, step3p5_tool_parser, sample_tools`; `vllm/tool_parsers/step3p5_tool_parser.py` modified +20/-5 (25 lines); hunks: -97,11 +97,26 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; -110,7 +125,7 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; symbols: parse_single_streaming_chunks, touching `parse_single_streaming_chunks`.
- Code diff details:
  - `tests/tool_parsers/test_step3p5_tool_parser.py` added +1435/-0 (1435 lines); hunks: -0,0 +1,1435; symbols: step3p5_tokenizer, step3p5_tool_parser, sample_tools, assert_tool_calls
  - `vllm/tool_parsers/step3p5_tool_parser.py` modified +20/-5 (25 lines); hunks: -97,11 +97,26 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; -110,7 +125,7 @@ def parse_single_streaming_chunks(self, xml_chunk: str) -> D...; symbols: parse_single_streaming_chunks
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_step3p5_tool_parser.py` added +1435/-0
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` modified +20/-5
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_step3p5_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #33523 - [Models] Step-3.5-Flash

- Link: https://github.com/vllm-project/vllm/pull/33523
- Status/date: merged / 2026-02-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/step3p5.py`, `vllm/model_executor/models/step3p5_mtp.py`, `vllm/tool_parsers/step3p5_tool_parser.py`; associated commits `c3b40dc3e74d`
- Diff scope read: GitHub Pull Request files API returned 18 files, +3107/-4, 3270 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Models] Step-3.5-Flash"; model line: Step 3.5; category: performance/backend optimization; main diff: `vllm/tool_parsers/step3p5_tool_parser.py`, `vllm/model_executor/models/step3p5.py`, `vllm/model_executor/models/step3p5_mtp.py`; technical summary: Covers "[Models] Step-3.5-Flash"; the main implementation surface is `vllm/tool_parsers/step3p5_tool_parser.py`, `vllm/model_executor/models/step3p5.py`, `vllm/model_executor/models/step3p5_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/step3p5_tool_parser.py` added +1511/-0 (1511 lines); hunks: -0,0 +1,1511; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks, touching `StreamingXMLToolCallParser, __init__, reset_streaming_state`; `vllm/model_executor/models/step3p5.py` added +894/-0 (894 lines); hunks: -0,0 +1,894; symbols: FP32ReplicatedLinear, forward, Step3p5MLP, __init__, touching `FP32ReplicatedLinear, forward, Step3p5MLP`; `vllm/model_executor/models/step3p5_mtp.py` added +315/-0 (315 lines); hunks: -0,0 +1,315; symbols: SharedHead, __init__, forward, Step3p5AMultiTokenPredictorLayer, touching `SharedHead, __init__, forward`; `vllm/transformers_utils/configs/step3p5.py` added +100/-0 (100 lines); hunks: -0,0 +1,100; symbols: Step3p5Config, __init__, touching `Step3p5Config, __init__`.
- Code diff details:
  - `vllm/tool_parsers/step3p5_tool_parser.py` added +1511/-0 (1511 lines); hunks: -0,0 +1,1511; symbols: StreamingXMLToolCallParser, __init__, reset_streaming_state, parse_single_streaming_chunks
  - `vllm/model_executor/models/step3p5.py` added +894/-0 (894 lines); hunks: -0,0 +1,894; symbols: FP32ReplicatedLinear, forward, Step3p5MLP, __init__
  - `vllm/model_executor/models/step3p5_mtp.py` added +315/-0 (315 lines); hunks: -0,0 +1,315; symbols: SharedHead, __init__, forward, Step3p5AMultiTokenPredictorLayer
  - `vllm/transformers_utils/configs/step3p5.py` added +100/-0 (100 lines); hunks: -0,0 +1,100; symbols: Step3p5Config, __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/tool_parsers/step3p5_tool_parser.py` added +1511/-0; `vllm/model_executor/models/step3p5.py` added +894/-0; `vllm/model_executor/models/step3p5_mtp.py` added +315/-0; `vllm/transformers_utils/configs/step3p5.py` added +100/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/core/test_activation.py`, `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
