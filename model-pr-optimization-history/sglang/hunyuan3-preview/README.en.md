# sglang Hunyuan3 Preview Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` | [#36823](https://github.com/sgl-project/sglang/pull/36823) |
| `docs/cookbook/autoregressive/Tencent/Hy3.mdx` | no direct PR-number commit |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` | [#30223](https://github.com/sgl-project/sglang/pull/30223) |
| `docs/src/snippets/autoregressive/hunyuan3-preview-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/configs/tencent/hy3-benchmarks.jsx` | no direct PR-number commit |
| `docs/src/snippets/configs/tencent/hy3.jsx` | no direct PR-number commit |
| `python/sglang/srt/function_call/hunyuan_detector.py` | [#23533](https://github.com/sgl-project/sglang/pull/23533) |
| `test/registered/unit/function_call/test_hunyuan_detector.py` | [#23533](https://github.com/sgl-project/sglang/pull/23533) |

## PR Coverage Summary

- Git-traced PRs: 3
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 3
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-24 | [#23533](https://github.com/sgl-project/sglang/pull/23533) | merged | support Hy3 preview | `test/registered/unit/function_call/test_hunyuan_detector.py`, `python/sglang/srt/function_call/hunyuan_detector.py` |
| 2026-08-11 | [#30223](https://github.com/sgl-project/sglang/pull/30223) | merged | Add Hunyuan3 On Ascend Doc | `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` |
| 2026-08-28 | [#36823](https://github.com/sgl-project/sglang/pull/36823) | merged | [Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview" | `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` |

## Per-PR Diff Audit Cards

### PR #23533 - support Hy3 preview

- Link: https://github.com/sgl-project/sglang/pull/23533
- Status/date: merged / 2026-04-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/hunyuan_detector.py`, `test/registered/unit/function_call/test_hunyuan_detector.py`; associated commits `6d038614760f`
- Diff scope read: GitHub Pull Request files API returned 25 files, +4095/-3, 4205 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support Hy3 preview"; model line: Hunyuan3 Preview; category: docs/tests/CI; main diff: `test/registered/unit/function_call/test_hunyuan_detector.py`, `python/sglang/srt/function_call/hunyuan_detector.py`; technical summary: Covers "support Hy3 preview"; the main implementation surface is `test/registered/unit/function_call/test_hunyuan_detector.py`, `python/sglang/srt/function_call/hunyuan_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/function_call/test_hunyuan_detector.py` added +733/-0 (733 lines); hunks: -0,0 +1,733; symbols: _make_tools, TestHunyuanDetectorHasToolCall, setUp, test_has_tool_call_true, touching `_make_tools, TestHunyuanDetectorHasToolCall, setUp`; `python/sglang/srt/function_call/hunyuan_detector.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: HunyuanDetector, __init__, _normalize_type, _get_arg_schema, touching `HunyuanDetector, __init__, _normalize_type`.
- Code diff details:
  - `test/registered/unit/function_call/test_hunyuan_detector.py` added +733/-0 (733 lines); hunks: -0,0 +1,733; symbols: _make_tools, TestHunyuanDetectorHasToolCall, setUp, test_has_tool_call_true
  - `python/sglang/srt/function_call/hunyuan_detector.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: HunyuanDetector, __init__, _normalize_type, _get_arg_schema
- Key code excerpts:

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

- Reviewed files:
  - tests: `test/registered/unit/function_call/test_hunyuan_detector.py` added +733/-0
  - runtime: `python/sglang/srt/function_call/hunyuan_detector.py` added +476/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/function_call/test_hunyuan_detector.py`, `test/registered/unit/parser/test_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30223 - Add Hunyuan3 On Ascend Doc

- Link: https://github.com/sgl-project/sglang/pull/30223
- Status/date: merged / 2026-08-11
- Trace source: `git log --name-only -- <model-files>` found it through `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`; associated commits `f148eb6e6ea5`
- Diff scope read: GitHub Pull Request files API returned 2 files, +389/-0, 397 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add Hunyuan3 On Ascend Doc"; model line: Hunyuan3 Preview; category: docs/tests/CI; main diff: `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`; technical summary: Covers "Add Hunyuan3 On Ascend Doc"; the main implementation surface is `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` added +388/-0 (388 lines); hunks: -0,0 +1,388.
- Code diff details:
  - `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` added +388/-0 (388 lines); hunks: -0,0 +1,388
- Key code excerpts:

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

- Reviewed files:
  - docs: `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` added +388/-0
- Risk and verification: This is mostly docs/examples in `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #36823 - [Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview"

- Link: https://github.com/sgl-project/sglang/pull/36823
- Status/date: merged / 2026-08-28
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`; associated commits `989e51ba9c4c`
- Diff scope read: GitHub Pull Request files API returned 2 files, +12/-12, 87 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview""; model line: Hunyuan3 Preview; category: docs/tests/CI; main diff: `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`; technical summary: Covers "[Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview""; the main implementation surface is `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` modified +3/-3 (6 lines); hunks: -1,12 +1,12.
- Code diff details:
  - `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` modified +3/-3 (6 lines); hunks: -1,12 +1,12
- Key code excerpts:

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

- Reviewed files:
  - docs: `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` modified +3/-3
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`, `docs/cookbook/autoregressive/Tencent/Hy4-Preview.mdx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
