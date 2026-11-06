# vllm GLM-4.6/4.7 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/parser/engine/test_glm47_moe.py` | [#64535](https://github.com/vllm-project/vllm/pull/64535) |
| `tests/reasoning/test_glm4_moe_reasoning_parser.py` | 无直接 PR 号提交 |
| `tests/tool_parsers/test_glm47_moe_tool_parser.py` | [#37386](https://github.com/vllm-project/vllm/pull/37386) |
| `tests/tool_parsers/test_glm4_moe_tool_parser.py` | [#37386](https://github.com/vllm-project/vllm/pull/37386) |
| `vllm/model_executor/models/glm4_moe.py` | [#30876](https://github.com/vllm-project/vllm/pull/30876) |
| `vllm/model_executor/models/glm4_moe_lite.py` | [#31386](https://github.com/vllm-project/vllm/pull/31386) |
| `vllm/model_executor/models/glm4_moe_lite_mtp.py` | [#31386](https://github.com/vllm-project/vllm/pull/31386) |
| `vllm/model_executor/models/glm4_moe_mtp.py` | [#27597](https://github.com/vllm-project/vllm/pull/27597), [#31386](https://github.com/vllm-project/vllm/pull/31386) |
| `vllm/parser/glm47_moe.py` | [#64535](https://github.com/vllm-project/vllm/pull/64535) |
| `vllm/reasoning/glm47_moe_reasoning_parser.py` | 无直接 PR 号提交 |
| `vllm/tool_parsers/glm47_moe_tool_parser.py` | [#30876](https://github.com/vllm-project/vllm/pull/30876), [#37386](https://github.com/vllm-project/vllm/pull/37386), [#56403](https://github.com/vllm-project/vllm/pull/56403) |

## PR 覆盖总览

- git 追溯 PR 数: 6
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 6

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-29 | [#64535](https://github.com/vllm-project/vllm/pull/64535) | merged | [Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming | `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py` |
| 2026-10-02 | [#56403](https://github.com/vllm-project/vllm/pull/56403) | merged | [Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag | `vllm/tool_parsers/glm47_moe_tool_parser.py` |
| 2026-03-18 | [#37386](https://github.com/vllm-project/vllm/pull/37386) | merged | fix(glm47): improve tool call parsing and content normalization | `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py` |
| 2026-01-19 | [#31386](https://github.com/vllm-project/vllm/pull/31386) | merged | [GLM-4.7] GLM Model support for GLM-Lite | `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2025-12-20 | [#30876](https://github.com/vllm-project/vllm/pull/30876) | merged | GLM-4.7 Tool Parser and Doc Update | `vllm/tool_parsers/glm47_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py` |
| 2025-11-12 | [#27597](https://github.com/vllm-project/vllm/pull/27597) | merged | [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint. | `vllm/model_executor/models/glm4_moe_mtp.py` |

## 逐 PR diff 审计卡

### PR #64535 - [Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming

- 链接: https://github.com/vllm-project/vllm/pull/64535
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`；关联提交 `255431b5ed87`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+112/-8，可读 patch 181 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`；技术摘要: 覆盖「[Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming」；主要实现面是 `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/parser/engine/test_glm47_moe.py` modified +61/-0 (61 lines); hunks: -18,6 +18,7; -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):; symbols: test_thinking_disabled, _pieces, counting_converter, test_repeated_closed_args_stream_non_streaming_arguments，涉及 `test_thinking_disabled, _pieces, counting_converter`；`vllm/parser/glm47_moe.py` modified +51/-8 (59 lines); hunks: -64,18 +64,47; -86,14 +115,20 @@ def _glm47_parse_args(; symbols: _ClosedArgs, __init__, _glm47_parse_args, _glm47_arg_converter，涉及 `_ClosedArgs, __init__, _glm47_parse_args`。
- 代码 diff 细节:
  - `tests/parser/engine/test_glm47_moe.py` modified +61/-0 (61 lines); hunks: -18,6 +18,7; -140,6 +141,15 @@ def test_thinking_disabled(self, no_thinking_parser):; symbols: test_thinking_disabled, _pieces, counting_converter, test_repeated_closed_args_stream_non_streaming_arguments
  - `vllm/parser/glm47_moe.py` modified +51/-8 (59 lines); hunks: -64,18 +64,47; -86,14 +115,20 @@ def _glm47_parse_args(; symbols: _ClosedArgs, __init__, _glm47_parse_args, _glm47_arg_converter
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/parser/engine/test_glm47_moe.py` modified +61/-0
  - runtime: `vllm/parser/glm47_moe.py` modified +51/-8
- 验证与风险: diff 自带测试面 `tests/parser/engine/test_glm47_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56403 - [Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag

- 链接: https://github.com/vllm-project/vllm/pull/56403
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/tool_parsers/glm47_moe_tool_parser.py`；关联提交 `d1a974c14031`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+729/-2，可读 patch 795 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag」；模型线: GLM-4.6/4.7；类别: 模型实现调整；主要 diff: `vllm/tool_parsers/glm47_moe_tool_parser.py`；技术摘要: 覆盖「[Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag」；主要实现面是 `vllm/tool_parsers/glm47_moe_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +3/-0 (3 lines); hunks: -4,8 +4,11; symbols: Glm47MoeModelToolParser，涉及 `Glm47MoeModelToolParser`。
- 代码 diff 细节:
  - `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +3/-0 (3 lines); hunks: -4,8 +4,11; symbols: Glm47MoeModelToolParser
- 关键代码摘录:

```diff
diff -- vllm/tool_parsers/glm47_moe_tool_parser.py
@@ -4,8 +4,11 @@
+from vllm.tool_parsers.tool_strict_level import ToolStrictLevel
+    # Constrain auto tool calls with the shallow tag by default.
+    default_tool_strict_level = ToolStrictLevel.FUNCTION
```

- 已读文件:
  - runtime: `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_structural_tag_registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37386 - fix(glm47): improve tool call parsing and content normalization

- 链接: https://github.com/vllm-project/vllm/pull/37386
- 状态/时间: merged / 2026-03-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`；关联提交 `fad09e8a1f51`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+193/-6，可读 patch 244 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(glm47): improve tool call parsing and content normalization」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`；技术摘要: 覆盖「fix(glm47): improve tool call parsing and content normalization」；主要实现面是 `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_glm47_moe_tool_parser.py` added +168/-0 (168 lines); hunks: -0,0 +1,168; symbols: glm47_tokenizer, glm47_tool_parser, mock_request, TestGlm47ExtractToolCalls，涉及 `glm47_tokenizer, glm47_tool_parser, mock_request`；`vllm/tool_parsers/glm47_moe_tool_parser.py` modified +16/-2 (18 lines); hunks: -1,6 +1,16; -14,10 +24,14; symbols: Glm47MoeModelToolParser, __init__，涉及 `Glm47MoeModelToolParser, __init__`；`tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +3/-3 (6 lines); hunks: -107,7 +107,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; -152,7 +152,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; symbols: test_extract_tool_calls_no_tools，涉及 `test_extract_tool_calls_no_tools`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_glm47_moe_tool_parser.py` added +168/-0 (168 lines); hunks: -0,0 +1,168; symbols: glm47_tokenizer, glm47_tool_parser, mock_request, TestGlm47ExtractToolCalls
  - `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +16/-2 (18 lines); hunks: -1,6 +1,16; -14,10 +24,14; symbols: Glm47MoeModelToolParser, __init__
  - `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +3/-3 (6 lines); hunks: -107,7 +107,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; -152,7 +152,7 @@ def test_extract_tool_calls_no_tools(glm4_moe_tool_parser, m...; symbols: test_extract_tool_calls_no_tools
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/tool_parsers/test_glm47_moe_tool_parser.py` added +168/-0; `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +3/-3
  - runtime: `vllm/tool_parsers/glm47_moe_tool_parser.py` modified +16/-2
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31386 - [GLM-4.7] GLM Model support for GLM-Lite

- 链接: https://github.com/vllm-project/vllm/pull/31386
- 状态/时间: merged / 2026-01-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`；关联提交 `71832ba71e77`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+1135/-1，可读 patch 1208 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-4.7] GLM Model support for GLM-Lite」；模型线: GLM-4.6/4.7；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`；技术摘要: 覆盖「[GLM-4.7] GLM Model support for GLM-Lite」；主要实现面是 `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe_lite.py` added +642/-0 (642 lines); hunks: -0,0 +1,642; symbols: Glm4MoeLiteMLP, Glm4MoeLite, Glm4LiteMixtureOfExperts, Glm4MoeLiteAttention，涉及 `Glm4MoeLiteMLP, Glm4MoeLite, Glm4LiteMixtureOfExperts`；`vllm/model_executor/models/glm4_moe_lite_mtp.py` added +464/-0 (464 lines); hunks: -0,0 +1,464; symbols: SharedHead, __init__, forward, Glm4MoeLiteMultiTokenPredictorLayer，涉及 `SharedHead, __init__, forward`；`vllm/model_executor/models/glm4_moe_mtp.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe_lite.py` added +642/-0 (642 lines); hunks: -0,0 +1,642; symbols: Glm4MoeLiteMLP, Glm4MoeLite, Glm4LiteMixtureOfExperts, Glm4MoeLiteAttention
  - `vllm/model_executor/models/glm4_moe_lite_mtp.py` added +464/-0 (464 lines); hunks: -0,0 +1,464; symbols: SharedHead, __init__, forward, Glm4MoeLiteMultiTokenPredictorLayer
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe_lite.py` added +642/-0; `vllm/model_executor/models/glm4_moe_lite_mtp.py` added +464/-0; `vllm/model_executor/models/glm4_moe_mtp.py` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30876 - GLM-4.7 Tool Parser and Doc Update

- 链接: https://github.com/vllm-project/vllm/pull/30876
- 状态/时间: merged / 2025-12-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`；关联提交 `8a7a41437490`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+38/-3，可读 patch 73 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-4.7 Tool Parser and Doc Update」；模型线: GLM-4.6/4.7；类别: 文档/测试/CI；主要 diff: `vllm/tool_parsers/glm47_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「GLM-4.7 Tool Parser and Doc Update」；主要实现面是 `vllm/tool_parsers/glm47_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/glm47_moe_tool_parser.py` added +23/-0 (23 lines); hunks: -0,0 +1,23; symbols: Glm47MoeModelToolParser, __init__，涉及 `Glm47MoeModelToolParser, __init__`；`vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8。
- 代码 diff 细节:
  - `vllm/tool_parsers/glm47_moe_tool_parser.py` added +23/-0 (23 lines); hunks: -0,0 +1,23; symbols: Glm47MoeModelToolParser, __init__
  - `vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -21,7 +21,8
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/tool_parsers/glm47_moe_tool_parser.py` added +23/-0; `vllm/model_executor/models/glm4_moe.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe.py`, `vllm/tool_parsers/__init__.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27597 - [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.

- 链接: https://github.com/vllm-project/vllm/pull/27597
- 状态/时间: merged / 2025-11-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe_mtp.py`；关联提交 `d3ade61e429f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-4，可读 patch 23 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_moe_mtp.py`；技术摘要: 覆盖「[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.」；主要实现面是 `vllm/model_executor/models/glm4_moe_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
