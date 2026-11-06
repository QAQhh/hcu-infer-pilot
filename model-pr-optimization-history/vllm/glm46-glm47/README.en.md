# vllm GLM-4.6/4.7 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/parser/engine/test_glm47_moe.py` | [#64535](https://github.com/vllm-project/vllm/pull/64535) |
| `tests/reasoning/test_glm4_moe_reasoning_parser.py` | no direct PR-number commit |
| `tests/tool_parsers/test_glm47_moe_tool_parser.py` | [#37386](https://github.com/vllm-project/vllm/pull/37386) |
| `tests/tool_parsers/test_glm4_moe_tool_parser.py` | [#37386](https://github.com/vllm-project/vllm/pull/37386) |
| `vllm/model_executor/models/glm4_moe.py` | [#30876](https://github.com/vllm-project/vllm/pull/30876) |
| `vllm/model_executor/models/glm4_moe_lite.py` | [#31386](https://github.com/vllm-project/vllm/pull/31386) |
| `vllm/model_executor/models/glm4_moe_lite_mtp.py` | [#31386](https://github.com/vllm-project/vllm/pull/31386) |
| `vllm/model_executor/models/glm4_moe_mtp.py` | [#27597](https://github.com/vllm-project/vllm/pull/27597), [#31386](https://github.com/vllm-project/vllm/pull/31386) |
| `vllm/parser/glm47_moe.py` | [#64535](https://github.com/vllm-project/vllm/pull/64535) |
| `vllm/reasoning/glm47_moe_reasoning_parser.py` | no direct PR-number commit |
| `vllm/tool_parsers/glm47_moe_tool_parser.py` | [#30876](https://github.com/vllm-project/vllm/pull/30876), [#37386](https://github.com/vllm-project/vllm/pull/37386), [#56403](https://github.com/vllm-project/vllm/pull/56403) |

## PR Coverage Summary

- Git-traced PRs: 6
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 6

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-10-29 | [#64535](https://github.com/vllm-project/vllm/pull/64535) | merged | [Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming | `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py` |
| 2026-10-02 | [#56403](https://github.com/vllm-project/vllm/pull/56403) | merged | [Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag | `vllm/tool_parsers/glm47_moe_tool_parser.py` |
| 2026-03-18 | [#37386](https://github.com/vllm-project/vllm/pull/37386) | merged | fix(glm47): improve tool call parsing and content normalization | `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py` |
| 2026-01-19 | [#31386](https://github.com/vllm-project/vllm/pull/31386) | merged | [GLM-4.7] GLM Model support for GLM-Lite | `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2025-12-20 | [#30876](https://github.com/vllm-project/vllm/pull/30876) | merged | GLM-4.7 Tool Parser and Doc Update | `vllm/tool_parsers/glm47_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py` |
| 2025-11-12 | [#27597](https://github.com/vllm-project/vllm/pull/27597) | merged | [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint. | `vllm/model_executor/models/glm4_moe_mtp.py` |

## Per-PR Diff Audit Cards

### PR #64535 - [Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming

- Link: https://github.com/vllm-project/vllm/pull/64535
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`; associated commits `255431b5ed87`
- Diff scope read: GitHub Pull Request files API returned 2 files, +112/-8, 181 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming"; model line: GLM-4.6/4.7; category: bug fix; main diff: `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`; technical summary: Covers "[Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming"; the main implementation surface is `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/parser/engine/test_glm47_moe.py` modified +61/-0 (61 lines); hunks: -18,6 +18,7; -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):; symbols: test_thinking_disabled, _pieces, counting_converter, test_repeated_closed_args_stream_non_streaming_arguments, touching `test_thinking_disabled, _pieces, counting_converter`; `vllm/parser/glm47_moe.py` modified +51/-8 (59 lines); hunks: -64,18 +64,47; -86,14 +115,20 @@ def _glm47_parse_args(; symbols: _ClosedArgs, __init__, _glm47_parse_args, _glm47_arg_converter, touching `_ClosedArgs, __init__, _glm47_parse_args`.
- Code diff details:
  - `tests/parser/engine/test_glm47_moe.py` modified +61/-0 (61 lines); hunks: -18,6 +18,7; -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):; symbols: test_thinking_disabled, _pieces, counting_converter, test_repeated_closed_args_stream_non_streaming_arguments
  - `vllm/parser/glm47_moe.py` modified +51/-8 (59 lines); hunks: -64,18 +64,47; -86,14 +115,20 @@ def _glm47_parse_args(; symbols: _ClosedArgs, __init__, _glm47_parse_args, _glm47_arg_converter
- Key code excerpts:

```diff
diff -- tests/parser/engine/test_glm47_moe.py
@@ -18,6 +18,7 @@
+from vllm.parser import glm47_moe
@@ -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):
+# A model stuck in a loop repeats closed argument pairs inside one call.
+LOOP_HEAD = (
+    f"{THINK_END}{TOOL_CALL_START}Write\n"
+    "<arg_key>file_path</arg_key><arg_value>/repo/app.py</arg_value>\n"
diff -- vllm/parser/glm47_moe.py
@@ -64,18 +64,47 @@
+class _ClosedArgs:
+    """Closed key/value pairs of a raw argument text, reused by longer texts.
+    Raw arguments only grow while a call streams, so a parse of a text that
+    extends ``text`` resumes after its last closed value.
+    """
+    __slots__ = ("text", "params", "outside")
```

- Reviewed files:
  - tests: `tests/parser/engine/test_glm47_moe.py` modified +61/-0
  - runtime: `vllm/parser/glm47_moe.py` modified +51/-8
- Risk and verification: The diff ships test coverage in `tests/parser/engine/test_glm47_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56403 - [Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag

- Link: https://github.com/vllm-project/vllm/pull/56403
- Status/date: merged / 2026-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tool_parsers/glm47_moe_tool_parser.py`; associated commits `d1a974c14031`
- Diff scope read: GitHub Pull Request files API returned 5 files, +729/-2, 795 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag"; model line: GLM-4.6/4.7; category: model implementation change; main diff: `vllm/tool_parsers/glm47_moe_tool_parser.py`; technical summary: Covers "[Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag"; the main implementation surface is `vllm/tool_parsers/glm47_moe_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +3/-0 (3 lines); hunks: -4,8 +4,11; symbols: Glm47MoeModelToolParser, touching `Glm47MoeModelToolParser`.
- Code diff details:
  - `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +3/-0 (3 lines); hunks: -4,8 +4,11; symbols: Glm47MoeModelToolParser
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/glm47_moe_tool_parser.py
@@ -4,8 +4,11 @@
+from vllm.tool_parsers.tool_strict_level import ToolStrictLevel
+    # Constrain auto tool calls with the shallow tag by default.
+    default_tool_strict_level = ToolStrictLevel.FUNCTION
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +3/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_structural_tag_registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37386 - fix(glm47): improve tool call parsing and content normalization

- Link: https://github.com/vllm-project/vllm/pull/37386
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`; associated commits `fad09e8a1f51`
- Diff scope read: GitHub Pull Request files API returned 4 files, +193/-6, 244 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(glm47): improve tool call parsing and content normalization"; model line: GLM-4.6/4.7; category: bug fix; main diff: `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`; technical summary: Covers "fix(glm47): improve tool call parsing and content normalization"; the main implementation surface is `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_glm47_moe_tool_parser.py` added +168/-0 (168 lines); hunks: -0,0 +1,168; symbols: glm47_tokenizer, glm47_tool_parser, mock_request, TestGlm47ExtractToolCalls, touching `glm47_tokenizer, glm47_tool_parser, mock_request`; `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +16/-2 (18 lines); hunks: -1,6 +1,16; -14,10 +24,14; symbols: Glm47MoeModelToolParser, __init__, touching `Glm47MoeModelToolParser, __init__`; `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +3/-3 (6 lines); hunks: -107,7 +107,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; -152,7 +152,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; symbols: test_extract_tool_calls_no_tools, touching `test_extract_tool_calls_no_tools`.
- Code diff details:
  - `tests/tool_parsers/test_glm47_moe_tool_parser.py` added +168/-0 (168 lines); hunks: -0,0 +1,168; symbols: glm47_tokenizer, glm47_tool_parser, mock_request, TestGlm47ExtractToolCalls
  - `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +16/-2 (18 lines); hunks: -1,6 +1,16; -14,10 +24,14; symbols: Glm47MoeModelToolParser, __init__
  - `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +3/-3 (6 lines); hunks: -107,7 +107,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; -152,7 +152,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; symbols: test_extract_tool_calls_no_tools
- Key code excerpts:

```diff
diff -- tests/tool_parsers/test_glm47_moe_tool_parser.py
@@ -0,0 +1,168 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# ruff: noqa: E501
+"""Tests for the GLM-4.7 tool call parser."""
+import json
+from unittest.mock import Mock
diff -- vllm/tool_parsers/glm47_moe_tool_parser.py
@@ -1,6 +1,16 @@
+"""
+GLM-4.7 Tool Call Parser.
+GLM-4.7 uses a slightly different tool call format compared to GLM-4.5:
+  - The function name may appear on the same line as ``<tool_call>`` without
+    a newline separator before the first ``<arg_key>``.
+  - Tool calls may have zero arguments
diff -- tests/tool_parsers/test_glm4_moe_tool_parser.py
@@ -107,7 +107,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, mock_request):
```

- Reviewed files:
  - tests: `tests/tool_parsers/test_glm47_moe_tool_parser.py` added +168/-0; `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +3/-3
  - runtime: `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +16/-2
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31386 - [GLM-4.7] GLM Model support for GLM-Lite

- Link: https://github.com/vllm-project/vllm/pull/31386
- Status/date: merged / 2026-01-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`; associated commits `71832ba71e77`
- Diff scope read: GitHub Pull Request files API returned 9 files, +1135/-1, 1208 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM-4.7] GLM Model support for GLM-Lite"; model line: GLM-4.6/4.7; category: model support/runtime entry; main diff: `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`; technical summary: Covers "[GLM-4.7] GLM Model support for GLM-Lite"; the main implementation surface is `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe_lite.py` added +642/-0 (642 lines); hunks: -0,0 +1,642; symbols: Glm4MoeLiteMLP, Glm4MoeLite, Glm4LiteMixtureOfExperts, Glm4MoeLiteAttention, touching `Glm4MoeLiteMLP, Glm4MoeLite, Glm4LiteMixtureOfExperts`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` added +464/-0 (464 lines); hunks: -0,0 +1,464; symbols: SharedHead, __init__, forward, Glm4MoeLiteMultiTokenPredictorLayer, touching `SharedHead, __init__, forward`; `vllm/model_executor/models/glm4_moe_mtp.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe_lite.py` added +642/-0 (642 lines); hunks: -0,0 +1,642; symbols: Glm4MoeLiteMLP, Glm4MoeLite, Glm4LiteMixtureOfExperts, Glm4MoeLiteAttention
  - `vllm/model_executor/models/glm4_moe_lite_mtp.py` added +464/-0 (464 lines); hunks: -0,0 +1,464; symbols: SharedHead, __init__, forward, Glm4MoeLiteMultiTokenPredictorLayer
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_moe_lite.py
@@ -0,0 +1,642 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Copyright 2025 The ZhipuAI Team.
+# Copyright 2023 The vLLM team.
+# Copyright 2022 EleutherAI and the HuggingFace Inc. team. All rights reserved.
+#
diff -- vllm/model_executor/models/glm4_moe_lite_mtp.py
@@ -0,0 +1,464 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Copyright 2025 The ZhipuAI Team.
+# Copyright 2023 The vLLM team.
+# Copyright 2022 EleutherAI and the HuggingFace Inc. team. All rights reserved.
+#
diff -- vllm/model_executor/models/glm4_moe_mtp.py
@@ -21,7 +21,8 @@
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe_lite.py` added +642/-0; `vllm/model_executor/models/glm4_moe_lite_mtp.py` added +464/-0; `vllm/model_executor/models/glm4_moe_mtp.py` modified +2/-1
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30876 - GLM-4.7 Tool Parser and Doc Update

- Link: https://github.com/vllm-project/vllm/pull/30876
- Status/date: merged / 2025-12-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`; associated commits `8a7a41437490`
- Diff scope read: GitHub Pull Request files API returned 5 files, +38/-3, 73 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "GLM-4.7 Tool Parser and Doc Update"; model line: GLM-4.6/4.7; category: docs/tests/CI; main diff: `vllm/tool_parsers/glm47_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "GLM-4.7 Tool Parser and Doc Update"; the main implementation surface is `vllm/tool_parsers/glm47_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/glm47_moe_tool_parser.py` added +23/-0 (23 lines); hunks: -0,0 +1,23; symbols: Glm47MoeModelToolParser, __init__, touching `Glm47MoeModelToolParser, __init__`; `vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8.
- Code diff details:
  - `vllm/tool_parsers/glm47_moe_tool_parser.py` added +23/-0 (23 lines); hunks: -0,0 +1,23; symbols: Glm47MoeModelToolParser, __init__
  - `vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/glm47_moe_tool_parser.py
@@ -0,0 +1,23 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import regex as re
+from vllm.logger import init_logger
+from vllm.tokenizers import TokenizerLike
+from vllm.tool_parsers.glm4_moe_tool_parser import Glm4MoeModelToolParser
diff -- vllm/model_executor/models/glm4_moe.py
@@ -21,7 +21,8 @@
-"""Inference-only GLM-4.5, GLM-4.6 model compatible with HuggingFace weights."""
+"""Inference-only GLM-4.5, GLM-4.6, GLM-4.7 model
+compatible with HuggingFace weights."""
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/glm47_moe_tool_parser.py` added +23/-0; `vllm/model_executor/models/glm4_moe.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe.py`, `vllm/tool_parsers/__init__.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27597 - [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.

- Link: https://github.com/vllm-project/vllm/pull/27597
- Status/date: merged / 2025-11-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe_mtp.py`; associated commits `d3ade61e429f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-4, 23 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint."; model line: GLM-4.6/4.7; category: bug fix; main diff: `vllm/model_executor/models/glm4_moe_mtp.py`; technical summary: Covers "[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint."; the main implementation surface is `vllm/model_executor/models/glm4_moe_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_moe_mtp.py
@@ -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+        spec_layer = self.model.mtp_start_layer_idx
-            spec_layer = get_spec_layer_idx_from_weight_name(self.config, name)
-            if spec_layer is None:
-                continue
-            name = self._rewrite_spec_layer_name(spec_layer, name)
+            if name == "lm_head.weight":
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
