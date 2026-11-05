# sglang Hunyuan3 Preview 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` | [#36823](https://github.com/sgl-project/sglang/pull/36823) |
| `docs/cookbook/autoregressive/Tencent/Hy3.mdx` | 无直接 PR 号提交 |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` | [#30223](https://github.com/sgl-project/sglang/pull/30223) |
| `docs/src/snippets/autoregressive/hunyuan3-preview-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/configs/tencent/hy3-benchmarks.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/configs/tencent/hy3.jsx` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/hunyuan_detector.py` | [#23533](https://github.com/sgl-project/sglang/pull/23533) |
| `test/registered/unit/function_call/test_hunyuan_detector.py` | [#23533](https://github.com/sgl-project/sglang/pull/23533) |

## PR 覆盖总览

- git 追溯 PR 数: 3
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 3
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-04-24 | [#23533](https://github.com/sgl-project/sglang/pull/23533) | merged | support Hy3 preview | `test/registered/unit/function_call/test_hunyuan_detector.py`, `python/sglang/srt/function_call/hunyuan_detector.py` |
| 2026-08-11 | [#30223](https://github.com/sgl-project/sglang/pull/30223) | merged | Add Hunyuan3 On Ascend Doc | `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` |
| 2026-08-28 | [#36823](https://github.com/sgl-project/sglang/pull/36823) | merged | [Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview" | `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` |

## 逐 PR diff 审计卡

### PR #23533 - support Hy3 preview

- 链接: https://github.com/sgl-project/sglang/pull/23533
- 状态/时间: merged / 2026-04-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/hunyuan_detector.py`, `test/registered/unit/function_call/test_hunyuan_detector.py`；关联提交 `6d038614760f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 25 个文件，+4095/-3，可读 patch 4205 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support Hy3 preview」；模型线: Hunyuan3 Preview；类别: 文档/测试/CI；主要 diff: `test/registered/unit/function_call/test_hunyuan_detector.py`, `python/sglang/srt/function_call/hunyuan_detector.py`；技术摘要: 覆盖「support Hy3 preview」；主要实现面是 `test/registered/unit/function_call/test_hunyuan_detector.py`, `python/sglang/srt/function_call/hunyuan_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/function_call/test_hunyuan_detector.py` added +733/-0 (733 lines); hunks: -0,0 +1,733; symbols: _make_tools, TestHunyuanDetectorHasToolCall, setUp, test_has_tool_call_true，涉及 `_make_tools, TestHunyuanDetectorHasToolCall, setUp`；`python/sglang/srt/function_call/hunyuan_detector.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: HunyuanDetector, __init__, _normalize_type, _get_arg_schema，涉及 `HunyuanDetector, __init__, _normalize_type`。
- 代码 diff 细节:
  - `test/registered/unit/function_call/test_hunyuan_detector.py` added +733/-0 (733 lines); hunks: -0,0 +1,733; symbols: _make_tools, TestHunyuanDetectorHasToolCall, setUp, test_has_tool_call_true
  - `python/sglang/srt/function_call/hunyuan_detector.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: HunyuanDetector, __init__, _normalize_type, _get_arg_schema
- 关键代码摘录:

```diff
diff -- test/registered/unit/function_call/test_hunyuan_detector.py
@@ -0,0 +1,733 @@
+"""Unit tests for HunyuanDetector - no server, no model loading."""
+import json
+import unittest
+from sglang.srt.entrypoints.openai.protocol import Function, Tool
+from sglang.srt.function_call.hunyuan_detector import HunyuanDetector
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/function_call/hunyuan_detector.py
@@ -0,0 +1,476 @@
+import json
+import logging
+import re
+from typing import Any, Dict, List, Optional, Set
+from sglang.srt.entrypoints.openai.protocol import Tool
+from sglang.srt.environ import envs
```

- 已读文件:
  - tests: `test/registered/unit/function_call/test_hunyuan_detector.py` added +733/-0
  - runtime: `python/sglang/srt/function_call/hunyuan_detector.py` added +476/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/function_call/test_hunyuan_detector.py`, `test/registered/unit/parser/test_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30223 - Add Hunyuan3 On Ascend Doc

- 链接: https://github.com/sgl-project/sglang/pull/30223
- 状态/时间: merged / 2026-08-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`；关联提交 `f148eb6e6ea5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+389/-0，可读 patch 397 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add Hunyuan3 On Ascend Doc」；模型线: Hunyuan3 Preview；类别: 文档/测试/CI；主要 diff: `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`；技术摘要: 覆盖「Add Hunyuan3 On Ascend Doc」；主要实现面是 `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` added +388/-0 (388 lines); hunks: -0,0 +1,388。
- 代码 diff 细节:
  - `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` added +388/-0 (388 lines); hunks: -0,0 +1,388
- 关键代码摘录:

```diff
diff -- docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx
@@ -0,0 +1,388 @@
+---
+title: "Hy3"
+metatags:
+  description: "Deploy Hy3 model with SGLang on Ascend NPUs, including single-node deployment and speculative decoding."
+---
+## Introduction
```

- 已读文件:
  - docs: `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` added +388/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36823 - [Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview"

- 链接: https://github.com/sgl-project/sglang/pull/36823
- 状态/时间: merged / 2026-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`；关联提交 `989e51ba9c4c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+12/-12，可读 patch 87 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview"」；模型线: Hunyuan3 Preview；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`；技术摘要: 覆盖「[Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview"」；主要实现面是 `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` modified +3/-3 (6 lines); hunks: -1,12 +1,12。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` modified +3/-3 (6 lines); hunks: -1,12 +1,12
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx
@@ -1,12 +1,12 @@
-title: Hunyuan 3 Preview
+title: Hy3 preview
-    description: "Deploy Tencent Hunyuan 3 Preview BF16 (~276B / ~20B active MoE) on NVIDIA GPUs with SGLang — hybrid thinking, native tool calling, 256K context, and built-in MTP
+    description: "Deploy Tencent Hy3 preview BF16 (~276B / ~20B active MoE) on NVIDIA GPUs with SGLang — hybrid thinking, native tool calling, 256K context, and built-in MTP specu
-Hunyuan 3 Preview (Hy3-preview) is Tencent's preview of its third-generation flagship MoE language model, featuring hybrid thinking, native tool calling, long-context reasoning, a
+Hy3 preview is Tencent's preview of its third-generation flagship MoE language model, featuring hybrid thinking, native tool calling, long-context reasoning, and Multi-Token Predi
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` modified +3/-3
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`, `docs/cookbook/autoregressive/Tencent/Hy4-Preview.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
