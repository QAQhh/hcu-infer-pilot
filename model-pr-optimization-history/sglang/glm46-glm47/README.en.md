# sglang GLM-4.6/4.7 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/GLM/GLM-4.6.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/GLM/GLM-4.6V.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/GLM/GLM-4.7-Flash.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/GLM/GLM-4.7.mdx` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/glm4_moe.py` | no direct PR-number commit |
| `python/sglang/srt/function_call/glm47_moe_detector.py` | [#15333](https://github.com/sgl-project/sglang/pull/15333), [#15753](https://github.com/sgl-project/sglang/pull/15753), [#28149](https://github.com/sgl-project/sglang/pull/28149), [#38890](https://github.com/sgl-project/sglang/pull/38890) |
| `python/sglang/srt/function_call/glm4_moe_detector.py` | [#13989](https://github.com/sgl-project/sglang/pull/13989), [#15333](https://github.com/sgl-project/sglang/pull/15333), [#15753](https://github.com/sgl-project/sglang/pull/15753), [#38890](https://github.com/sgl-project/sglang/pull/38890) |
| `python/sglang/srt/models/glm4_moe.py` | [#13873](https://github.com/sgl-project/sglang/pull/13873), [#14585](https://github.com/sgl-project/sglang/pull/14585), [#15333](https://github.com/sgl-project/sglang/pull/15333), [#17166](https://github.com/sgl-project/sglang/pull/17166), [#21403](https://github.com/sgl-project/sglang/pull/21403), [#21660](https://github.com/sgl-project/sglang/pull/21660), [#21851](https://github.com/sgl-project/sglang/pull/21851) |
| `python/sglang/srt/models/glm4_moe_lite.py` | [#21851](https://github.com/sgl-project/sglang/pull/21851), [#22509](https://github.com/sgl-project/sglang/pull/22509), [#26088](https://github.com/sgl-project/sglang/pull/26088), [#28516](https://github.com/sgl-project/sglang/pull/28516), [#31388](https://github.com/sgl-project/sglang/pull/31388) |
| `python/sglang/srt/models/glm4_moe_lite_nextn.py` | [#26088](https://github.com/sgl-project/sglang/pull/26088) |
| `python/sglang/srt/models/glm4_moe_nextn.py` | [#13873](https://github.com/sgl-project/sglang/pull/13873) |
| `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` | [#21534](https://github.com/sgl-project/sglang/pull/21534) |
| `test/registered/attention/test_glm4_moe_lite_deterministic.py` | [#33945](https://github.com/sgl-project/sglang/pull/33945) |
| `test/registered/moe/test_glm4_moe_models.py` | no direct PR-number commit |
| `test/registered/unit/function_call/test_glm47_schema_types.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 17
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 17
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-12-01 | [#13873](https://github.com/sgl-project/sglang/pull/13873) | merged | Feat: GLM-4.6 supports shared experts fusion | `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py` |
| 2025-12-08 | [#14585](https://github.com/sgl-project/sglang/pull/14585) | merged | [Glm46v] Bug fix for accuracy drop and unable to launch server | `python/sglang/srt/models/glm4_moe.py` |
| 2025-12-13 | [#13989](https://github.com/sgl-project/sglang/pull/13989) | merged | Fix GLM-4.6 tool calls don't support streaming output for arguments i… | `python/sglang/srt/function_call/glm4_moe_detector.py` |
| 2025-12-20 | [#15333](https://github.com/sgl-project/sglang/pull/15333) | merged | [GLM-4.7] GLM-4.7 Tool Parser and Doc Update | `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py` |
| 2026-01-09 | [#15753](https://github.com/sgl-project/sglang/pull/15753) | merged | Fix GLM-4.7 MoE Detector complex JSON Schema type parsing | `test/registered/function_call/test_glm47_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py` |
| 2026-01-21 | [#17166](https://github.com/sgl-project/sglang/pull/17166) | merged | [Fix] GLM 4.7 + NVFP4 + MTP | `python/sglang/srt/models/glm4_moe.py` |
| 2026-03-28 | [#21534](https://github.com/sgl-project/sglang/pull/21534) | merged | [AMD] Add GLM-4.7-FP8 accuracy CI test for MI35x | `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` |
| 2026-03-30 | [#21660](https://github.com/sgl-project/sglang/pull/21660) | merged | [GLM-V and GLM-4.7] Cast to FP32 before gate projection for GLM model. | `python/sglang/srt/models/glm4_moe.py` |
| 2026-04-04 | [#21851](https://github.com/sgl-project/sglang/pull/21851) | merged | GLM-4.7 and GLM-4.7-Flash Loading and import format | `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py` |
| 2026-04-11 | [#21403](https://github.com/sgl-project/sglang/pull/21403) | merged | [AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8 | `python/sglang/srt/models/glm4_moe.py` |
| 2026-04-22 | [#22509](https://github.com/sgl-project/sglang/pull/22509) | merged | [NPU]Fix GLM-4.7-Flash failed on NPU | `python/sglang/srt/models/glm4_moe_lite.py` |
| 2026-05-26 | [#26088](https://github.com/sgl-project/sglang/pull/26088) | merged | GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP | `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py` |
| 2026-06-14 | [#28149](https://github.com/sgl-project/sglang/pull/28149) | merged | Support GLM-4.7 function calling via structural tags | `python/sglang/srt/function_call/glm47_moe_detector.py` |
| 2026-06-18 | [#28516](https://github.com/sgl-project/sglang/pull/28516) | merged | [NPU] Add MTP support for GLM-4.7-Flash | `python/sglang/srt/models/glm4_moe_lite.py` |
| 2026-07-16 | [#31388](https://github.com/sgl-project/sglang/pull/31388) | merged | [NPU]revert add scoring func for GLM 4.7 Flash | `python/sglang/srt/models/glm4_moe_lite.py` |
| 2026-08-12 | [#33945](https://github.com/sgl-project/sglang/pull/33945) | merged | feat: support deterministic FA4 for GLM-4.7-Flash | `test/registered/attention/test_glm4_moe_lite_deterministic.py` |
| 2026-09-15 | [#38890](https://github.com/sgl-project/sglang/pull/38890) | merged | Support non-strict GLM47 tool calls with EBNF constraints | `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py` |

## Per-PR Diff Audit Cards

### PR #13873 - Feat: GLM-4.6 supports shared experts fusion

- Link: https://github.com/sgl-project/sglang/pull/13873
- Status/date: merged / 2025-12-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; associated commits `982db4ebac26`
- Diff scope read: GitHub Pull Request files API returned 7 files, +252/-24, 431 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Feat: GLM-4.6 supports shared experts fusion"; model line: GLM-4.6/4.7; category: model support/runtime entry; main diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; technical summary: Covers "Feat: GLM-4.6 supports shared experts fusion"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +74/-19 (93 lines); hunks: -85,6 +85,7; -352,8 +353,14 @@ def __init__(; symbols: __init__, forward, forward_normal_dual_stream, touching `__init__, forward, forward_normal_dual_stream`; `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-0 (4 lines); hunks: -139,6 +139,10 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +74/-19 (93 lines); hunks: -85,6 +85,7; -352,8 +353,14 @@ def __init__(; symbols: __init__, forward, forward_normal_dual_stream
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-0 (4 lines); hunks: -139,6 +139,10 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -85,6 +85,7 @@
+    log_info_on_rank0,
@@ -352,8 +353,14 @@ def __init__(
+        self.moe_ep_size = get_moe_expert_parallel_world_size()
+        self.num_fused_shared_experts = (
+            0
+            if get_global_server_args().disable_shared_experts_fusion
diff -- python/sglang/srt/models/glm4_moe_nextn.py
@@ -139,6 +139,10 @@ def __init__(
+        self.num_fused_shared_experts = (
+            0 if get_global_server_args().disable_shared_experts_fusion else 1
+        )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +74/-19; `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=161,N=192,device_name=NVIDIA_H200,dtype=fp8_w8a8,per_channel_quant=True.json`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_config.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14585 - [Glm46v] Bug fix for accuracy drop and unable to launch server

- Link: https://github.com/sgl-project/sglang/pull/14585
- Status/date: merged / 2025-12-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `cf0478d602ce`
- Diff scope read: GitHub Pull Request files API returned 12 files, +308/-29, 530 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Glm46v] Bug fix for accuracy drop and unable to launch server"; model line: GLM-4.6/4.7; category: bug fix; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "[Glm46v] Bug fix for accuracy drop and unable to launch server"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -361,6 +361,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -361,6 +361,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -361,6 +361,7 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/pyproject.toml`, `python/sglang/srt/configs/qwen3_omni.py`, `python/sglang/srt/configs/qwen3_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13989 - Fix GLM-4.6 tool calls don't support streaming output for arguments i…

- Link: https://github.com/sgl-project/sglang/pull/13989
- Status/date: merged / 2025-12-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm4_moe_detector.py`; associated commits `80554598d33b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +527/-81, 700 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix GLM-4.6 tool calls don't support streaming output for arguments i…"; model line: GLM-4.6/4.7; category: bug fix; main diff: `python/sglang/srt/function_call/glm4_moe_detector.py`; technical summary: Covers "Fix GLM-4.6 tool calls don't support streaming output for arguments i…"; the main implementation surface is `python/sglang/srt/function_call/glm4_moe_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +498/-66 (564 lines); hunks: -2,16 +2,43; -21,32 +48,90 @@ def get_argument_type(func_name: str, arg_key: str, defined_...; symbols: get_argument_type, StreamState, parse_arguments, touching `get_argument_type, StreamState, parse_arguments`.
- Code diff details:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +498/-66 (564 lines); hunks: -2,16 +2,43; -21,32 +48,90 @@ def get_argument_type(func_name: str, arg_key: str, defined_...; symbols: get_argument_type, StreamState, parse_arguments
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -2,16 +2,43 @@
-from typing import List
+from enum import Enum
+from typing import Any, Dict, List, Optional, Tuple
-from sglang.srt.function_call.core_types import StreamingParseResult, _GetInfoFunc
+from sglang.srt.function_call.core_types import (
+    StreamingParseResult,
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +498/-66
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #15333 - [GLM-4.7] GLM-4.7 Tool Parser and Doc Update

- Link: https://github.com/sgl-project/sglang/pull/15333
- Status/date: merged / 2025-12-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`; associated commits `b82c7a0ae744`
- Diff scope read: GitHub Pull Request files API returned 7 files, +809/-394, 1356 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM-4.7] GLM-4.7 Tool Parser and Doc Update"; model line: GLM-4.6/4.7; category: docs/tests/CI; main diff: `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "[GLM-4.7] GLM-4.7 Tool Parser and Doc Update"; the main implementation surface is `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/glm47_moe_detector.py` added +584/-0 (584 lines); hunks: -0,0 +1,584; symbols: StreamState, get_argument_type, _convert_to_number, parse_arguments, touching `StreamState, get_argument_type, _convert_to_number`; `python/sglang/srt/function_call/glm4_moe_detector.py` modified +5/-2 (7 lines); hunks: -43,9 +43,12 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number, touching `get_argument_type, _convert_to_number`; `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -12,7 +12,7.
- Code diff details:
  - `python/sglang/srt/function_call/glm47_moe_detector.py` added +584/-0 (584 lines); hunks: -0,0 +1,584; symbols: StreamState, get_argument_type, _convert_to_number, parse_arguments
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +5/-2 (7 lines); hunks: -43,9 +43,12 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -12,7 +12,7
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/glm47_moe_detector.py
@@ -0,0 +1,584 @@
+import ast
+import json
+import logging
+import re
+from enum import Enum
+from typing import Any, Dict, List, Optional, Tuple
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -43,9 +43,12 @@ def get_argument_type(
-    if arg_key not in tool.function.parameters["properties"]:
+    properties = (tool.function.parameters or {}).get("properties", {})
+    if not isinstance(properties, dict):
+        properties = {}
+    if arg_key not in properties:
-    return tool.function.parameters["properties"][arg_key].get("type", None)
diff -- python/sglang/srt/models/glm4_moe.py
@@ -12,7 +12,7 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/glm47_moe_detector.py` added +584/-0; `python/sglang/srt/function_call/glm4_moe_detector.py` modified +5/-2; `python/sglang/srt/models/glm4_moe.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #15753 - Fix GLM-4.7 MoE Detector complex JSON Schema type parsing

- Link: https://github.com/sgl-project/sglang/pull/15753
- Status/date: merged / 2026-01-09
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`; associated commits `8ef5b9052825`
- Diff scope read: GitHub Pull Request files API returned 4 files, +869/-20, 989 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix GLM-4.7 MoE Detector complex JSON Schema type parsing"; model line: GLM-4.6/4.7; category: bug fix; main diff: `test/registered/function_call/test_glm47_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`; technical summary: Covers "Fix GLM-4.7 MoE Detector complex JSON Schema type parsing"; the main implementation surface is `test/registered/function_call/test_glm47_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/function_call/test_glm47_moe_detector.py` modified +678/-3 (681 lines); hunks: -3,7 +3,11; -1172,5 +1176,676 @@ def test_streamed_raw_length_multiple_empty_returns(self):; symbols: test_streamed_raw_length_multiple_empty_returns, TestGlm4ComplexJsonSchema, setUp, test_get_argument_type_simple_type, touching `test_streamed_raw_length_multiple_empty_returns, TestGlm4ComplexJsonSchema, setUp`; `python/sglang/srt/function_call/glm47_moe_detector.py` modified +43/-10 (53 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _get_value_type, _format_value_complete, touching `get_argument_type, _get_value_type, _format_value_complete`; `python/sglang/srt/function_call/glm4_moe_detector.py` modified +44/-6 (50 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number, _get_value_type, _format_value_complete, touching `get_argument_type, _convert_to_number, _get_value_type`.
- Code diff details:
  - `test/registered/function_call/test_glm47_moe_detector.py` modified +678/-3 (681 lines); hunks: -3,7 +3,11; -1172,5 +1176,676 @@ def test_streamed_raw_length_multiple_empty_returns(self):; symbols: test_streamed_raw_length_multiple_empty_returns, TestGlm4ComplexJsonSchema, setUp, test_get_argument_type_simple_type
  - `python/sglang/srt/function_call/glm47_moe_detector.py` modified +43/-10 (53 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _get_value_type, _format_value_complete
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +44/-6 (50 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number, _get_value_type, _format_value_complete
- Key code excerpts:

```diff
diff -- test/registered/function_call/test_glm47_moe_detector.py
@@ -3,7 +3,11 @@
-from sglang.srt.function_call.glm47_moe_detector import Glm47MoeDetector
+from sglang.srt.function_call.glm4_moe_detector import Glm4MoeDetector
+from sglang.srt.function_call.glm47_moe_detector import (
+    Glm47MoeDetector,
+    get_argument_type,
+)
diff -- python/sglang/srt/function_call/glm47_moe_detector.py
@@ -12,6 +12,7 @@
+from sglang.srt.function_call.utils import infer_type_from_json_schema
@@ -31,6 +32,14 @@ def get_argument_type(
+    Supports complex JSON Schema definitions including:
+    - Direct type field (including type arrays)
+    - anyOf/oneOf: parameter can be any of multiple types
+    - enum: parameter must be one of enum values
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -12,6 +12,7 @@
```

- Reviewed files:
  - tests: `test/registered/function_call/test_glm47_moe_detector.py` modified +678/-3
  - runtime: `python/sglang/srt/function_call/glm47_moe_detector.py` modified +43/-10; `python/sglang/srt/function_call/glm4_moe_detector.py` modified +44/-6
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_glm47_moe_detector.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #17166 - [Fix] GLM 4.7 + NVFP4 + MTP

- Link: https://github.com/sgl-project/sglang/pull/17166
- Status/date: merged / 2026-01-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `2ff0880a0ed1`
- Diff scope read: GitHub Pull Request files API returned 6 files, +114/-9, 206 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] GLM 4.7 + NVFP4 + MTP"; model line: GLM-4.6/4.7; category: bug fix; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "[Fix] GLM 4.7 + NVFP4 + MTP"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +5/-1 (6 lines); hunks: -63,7 +63,10; -376,6 +379,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +5/-1 (6 lines); hunks: -63,7 +63,10; -376,6 +379,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -63,7 +63,10 @@
-from sglang.srt.layers.moe.utils import filter_moe_weight_param_global_expert
+from sglang.srt.layers.moe.utils import (
+    RoutingMethodType,
+    filter_moe_weight_param_global_expert,
+)
@@ -376,6 +379,7 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21534 - [AMD] Add GLM-4.7-FP8 accuracy CI test for MI35x

- Link: https://github.com/sgl-project/sglang/pull/21534
- Status/date: merged / 2026-03-28
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`; associated commits `7078e385ea13`
- Diff scope read: GitHub Pull Request files API returned 2 files, +96/-0, 118 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add GLM-4.7-FP8 accuracy CI test for MI35x"; model line: GLM-4.6/4.7; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`; technical summary: Covers "[AMD] Add GLM-4.7-FP8 accuracy CI test for MI35x"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: TestGLM47FP8EvalMI35x, test_glm_47_fp8, touching `TestGLM47FP8EvalMI35x, test_glm_47_fp8`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: TestGLM47FP8EvalMI35x, test_glm_47_fp8
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py
@@ -0,0 +1,61 @@
+"""MI35x GLM-4.7-FP8 GSM8K Accuracy Evaluation Test (8-GPU)
+Tests GLM-4.7-FP8 accuracy using GSM8K benchmark on MI35x.
+Registry: nightly-amd-8-gpu-mi35x-glm47-fp8 suite
+"""
+import os
+# Set HF cache for MI35x
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` added +61/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #21660 - [GLM-V and GLM-4.7] Cast to FP32 before gate projection for GLM model.

- Link: https://github.com/sgl-project/sglang/pull/21660
- Status/date: merged / 2026-03-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `ad064c2f4e33`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-1, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM-V and GLM-4.7] Cast to FP32 before gate projection for GLM model."; model line: GLM-4.6/4.7; category: model implementation change; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "[GLM-V and GLM-4.7] Cast to FP32 before gate projection for GLM model."; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +6/-1 (7 lines); hunks: -327,9 +327,14 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +6/-1 (7 lines); hunks: -327,9 +327,14 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -327,9 +327,14 @@ def __init__(
+        # GLM requires FP32 gate projection; cache to avoid per-forward cast.
+        # FIXME: if gate weight is updated at runtime (e.g. expert rebalancing), _weight_fp32 must be invalidated.
+        self.register_buffer("_weight_fp32", None, persistent=False)
-        logits = F.linear(hidden_states, self.weight, None)
+        if self._weight_fp32 is None:
+            self._weight_fp32 = self.weight.data.to(torch.float32)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +6/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21851 - GLM-4.7 and GLM-4.7-Flash Loading and import format

- Link: https://github.com/sgl-project/sglang/pull/21851
- Status/date: merged / 2026-04-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`; associated commits `b7ae3b5a9a57`
- Diff scope read: GitHub Pull Request files API returned 2 files, +139/-86, 486 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "GLM-4.7 and GLM-4.7-Flash Loading and import format"; model line: GLM-4.6/4.7; category: performance/backend optimization; main diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`; technical summary: Covers "GLM-4.7 and GLM-4.7-Flash Loading and import format"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +130/-57 (187 lines); hunks: -15,13 +15,15; -62,6 +64,7; symbols: __init__, get_moe_weights, touching `__init__, get_moe_weights`; `python/sglang/srt/models/glm4_moe_lite.py` modified +9/-29 (38 lines); hunks: -12,13 +12,15; -29,12 +31,14; symbols: forward, __init__, load_weights, touching `forward, __init__, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +130/-57 (187 lines); hunks: -15,13 +15,15; -62,6 +64,7; symbols: __init__, get_moe_weights
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +9/-29 (38 lines); hunks: -12,13 +12,15; -29,12 +31,14; symbols: forward, __init__, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -15,13 +15,15 @@
+import re
+from sglang.srt.batch_overlap.single_batch_overlap import SboFlags
@@ -62,6 +64,7 @@
+from sglang.srt.layers.moe.kt_ep_wrapper import KTEPWrapperMethod
@@ -172,7 +175,7 @@ def __init__(
-        rope_theta: float = 10000,
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -12,13 +12,15 @@
-"""Inference-only GLM-Lite model compatible with HuggingFace weights"""
+"""Inference-only GLM-4.7-Flash model compatible with HuggingFace weights"""
+import re
+from sgl_kernel import dsv3_router_gemm
@@ -29,12 +31,14 @@
+from sglang.srt.layers.attention.nsa.utils import is_nsa_enable_prefill_cp
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +130/-57; `python/sglang/srt/models/glm4_moe_lite.py` modified +9/-29
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21403 - [AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8

- Link: https://github.com/sgl-project/sglang/pull/21403
- Status/date: merged / 2026-04-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `7e4e1dcd7ac8`
- Diff scope read: GitHub Pull Request files API returned 3 files, +149/-13, 269 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8"; model line: GLM-4.6/4.7; category: performance/backend optimization; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "[AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +58/-3 (61 lines); hunks: -289,7 +289,9 @@ def forward_prepare(; -865,6 +867,51 @@ def __init__(; symbols: forward_prepare, __init__, _detect_fp8_per_token_quant, _detect_attn_quant_format, touching `forward_prepare, __init__, _detect_fp8_per_token_quant`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +58/-3 (61 lines); hunks: -289,7 +289,9 @@ def forward_prepare(; -865,6 +867,51 @@ def __init__(; symbols: forward_prepare, __init__, _detect_fp8_per_token_quant, _detect_attn_quant_format
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -289,7 +289,9 @@ def forward_prepare(
-        if hidden_states.shape[0] == 0:
+        # hidden_states can be a (fp8_tensor, scale) tuple from fused RMSNorm+Quant
+        hs = hidden_states[0] if isinstance(hidden_states, tuple) else hidden_states
+        if hs.shape[0] == 0:
@@ -865,6 +867,51 @@ def __init__(
+        # Detect if QKV uses aiter FP8 per-token quant so we can fuse
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +58/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22509 - [NPU]Fix GLM-4.7-Flash failed on NPU

- Link: https://github.com/sgl-project/sglang/pull/22509
- Status/date: merged / 2026-04-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe_lite.py`; associated commits `92f28e9ba80b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +4/-2, 27 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]Fix GLM-4.7-Flash failed on NPU"; model line: GLM-4.6/4.7; category: bug fix; main diff: `python/sglang/srt/models/glm4_moe_lite.py`; technical summary: Covers "[NPU]Fix GLM-4.7-Flash failed on NPU"; the main implementation surface is `python/sglang/srt/models/glm4_moe_lite.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe_lite.py` modified +3/-1 (4 lines); hunks: -20,7 +20,6; -81,6 +80,9.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +3/-1 (4 lines); hunks: -20,7 +20,6; -81,6 +80,9
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -20,7 +20,6 @@
-from sgl_kernel import dsv3_router_gemm
@@ -81,6 +80,9 @@
+if _is_cuda:
+    from sgl_kernel import dsv3_router_gemm
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +3/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe_lite.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26088 - GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP

- Link: https://github.com/sgl-project/sglang/pull/26088
- Status/date: merged / 2026-05-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py`; associated commits `7ef06bfc06ec`
- Diff scope read: GitHub Pull Request files API returned 4 files, +799/-86, 1076 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP"; model line: GLM-4.6/4.7; category: performance/backend optimization; main diff: `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py`; technical summary: Covers "GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP"; the main implementation surface is `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe_lite.py` modified +603/-81 (684 lines); hunks: -1,4 +1,4; -12,77 +12,81; symbols: forward, __init__, Glm4MoeLiteSparseMoeBlock, touching `forward, __init__, Glm4MoeLiteSparseMoeBlock`; `python/sglang/srt/models/glm4_moe_lite_nextn.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: Glm4MoeLiteModelNextN, __init__, forward, Glm4MoeLiteForCausalLMNextN, touching `Glm4MoeLiteModelNextN, __init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +603/-81 (684 lines); hunks: -1,4 +1,4; -12,77 +12,81; symbols: forward, __init__, Glm4MoeLiteSparseMoeBlock
  - `python/sglang/srt/models/glm4_moe_lite_nextn.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: Glm4MoeLiteModelNextN, __init__, forward, Glm4MoeLiteForCausalLMNextN
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -1,4 +1,4 @@
-# Copyright 2025-2026 SGLang Team
+# Copyright 2026-2027 SGLang Team
@@ -12,77 +12,81 @@
-"""Inference-only GLM-4.7-Flash model compatible with HuggingFace weights"""
+"""Inference-only GLM-4.7-Flash model compatible with HuggingFace weights."""
-from typing import Iterable, Optional, Tuple
diff -- python/sglang/srt/models/glm4_moe_lite_nextn.py
@@ -0,0 +1,182 @@
+# Copyright 2026-2027 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +603/-81; `python/sglang/srt/models/glm4_moe_lite_nextn.py` added +182/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4_moe_lite.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28149 - Support GLM-4.7 function calling via structural tags

- Link: https://github.com/sgl-project/sglang/pull/28149
- Status/date: merged / 2026-06-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm47_moe_detector.py`; associated commits `f79a6b5c3355`
- Diff scope read: GitHub Pull Request files API returned 2 files, +104/-6, 137 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support GLM-4.7 function calling via structural tags"; model line: GLM-4.6/4.7; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/glm47_moe_detector.py`; technical summary: Covers "Support GLM-4.7 function calling via structural tags"; the main implementation surface is `python/sglang/srt/function_call/glm47_moe_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/glm47_moe_detector.py` modified +41/-6 (47 lines); hunks: -3,10 +3,15; -17,6 +22,21; symbols: _glm47_native_structural_tag_available, StreamState, _parse_argument_pairs, supports_structural_tag, touching `_glm47_native_structural_tag_available, StreamState, _parse_argument_pairs`.
- Code diff details:
  - `python/sglang/srt/function_call/glm47_moe_detector.py` modified +41/-6 (47 lines); hunks: -3,10 +3,15; -17,6 +22,21; symbols: _glm47_native_structural_tag_available, StreamState, _parse_argument_pairs, supports_structural_tag
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/glm47_moe_detector.py
@@ -3,10 +3,15 @@
-from typing import Any, Dict, List, Optional, Tuple
-from sglang.srt.entrypoints.openai.protocol import Tool
-from sglang.srt.function_call.base_format_detector import BaseFormatDetector
+from functools import lru_cache
+from typing import Any, Dict, List, Literal, Optional, Tuple, Union
+from sglang.srt.entrypoints.openai.protocol import Tool, ToolChoice
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/glm47_moe_detector.py` modified +41/-6
- Risk and verification: The diff ships test coverage in `test/registered/unit/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #28516 - [NPU] Add MTP support for GLM-4.7-Flash

- Link: https://github.com/sgl-project/sglang/pull/28516
- Status/date: merged / 2026-06-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe_lite.py`; associated commits `2a9cce5d2757`
- Diff scope read: GitHub Pull Request files API returned 2 files, +38/-2, 74 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Add MTP support for GLM-4.7-Flash"; model line: GLM-4.6/4.7; category: performance/backend optimization; main diff: `python/sglang/srt/models/glm4_moe_lite.py`; technical summary: Covers "[NPU] Add MTP support for GLM-4.7-Flash"; the main implementation surface is `python/sglang/srt/models/glm4_moe_lite.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe_lite.py` modified +2/-0 (2 lines); hunks: -548,6 +548,8 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +2/-0 (2 lines); hunks: -548,6 +548,8 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -548,6 +548,8 @@ def __init__(
+        # Required for MTP: Glm4MoeLiteModelNextN bypasses Glm4MoeLiteForCausalLM.__init__
+        config.moe_layer_freq = 1
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/models/glm4_moe_lite.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31388 - [NPU]revert add scoring func for GLM 4.7 Flash

- Link: https://github.com/sgl-project/sglang/pull/31388
- Status/date: merged / 2026-07-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe_lite.py`; associated commits `871c6482037e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +1/-2, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]revert add scoring func for GLM 4.7 Flash"; model line: GLM-4.6/4.7; category: performance/backend optimization; main diff: `python/sglang/srt/models/glm4_moe_lite.py`; technical summary: Covers "[NPU]revert add scoring func for GLM 4.7 Flash"; the main implementation surface is `python/sglang/srt/models/glm4_moe_lite.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe_lite.py` modified +0/-1 (1 lines); hunks: -225,7 +225,6 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +0/-1 (1 lines); hunks: -225,7 +225,6 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -225,7 +225,6 @@ def __init__(
-            **({"scoring_func": "sigmoid"}),
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +0/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/glm4_moe_lite.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #33945 - feat: support deterministic FA4 for GLM-4.7-Flash

- Link: https://github.com/sgl-project/sglang/pull/33945
- Status/date: merged / 2026-08-12
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/attention/test_glm4_moe_lite_deterministic.py`; associated commits `2d76d537e551`
- Diff scope read: GitHub Pull Request files API returned 6 files, +86/-7, 151 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: support deterministic FA4 for GLM-4.7-Flash"; model line: GLM-4.6/4.7; category: performance/backend optimization; main diff: `test/registered/attention/test_glm4_moe_lite_deterministic.py`; technical summary: Covers "feat: support deterministic FA4 for GLM-4.7-Flash"; the main implementation surface is `test/registered/attention/test_glm4_moe_lite_deterministic.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/attention/test_glm4_moe_lite_deterministic.py` added +68/-0 (68 lines); hunks: -0,0 +1,68; symbols: below, TestGlm4MoeLiteFa4Deterministic, get_model, get_server_args, touching `below, TestGlm4MoeLiteFa4Deterministic, get_model`.
- Code diff details:
  - `test/registered/attention/test_glm4_moe_lite_deterministic.py` added +68/-0 (68 lines); hunks: -0,0 +1,68; symbols: below, TestGlm4MoeLiteFa4Deterministic, get_model, get_server_args
- Key code excerpts:

```diff
diff -- test/registered/attention/test_glm4_moe_lite_deterministic.py
@@ -0,0 +1,68 @@
+"""Deterministic inference for GLM-4.7-Flash (Glm4MoeLiteForCausalLM) on Blackwell.
+Two entry paths matter. The fa4 backend is what this model needs for
+deterministic absorbed MLA, and the unspecified-backend path has to reach
+triton through the absorbed-MLA arch probe instead of the flashinfer default
+that every non-absorbed model gets on Blackwell.
+Usage:
```

- Reviewed files:
  - tests: `test/registered/attention/test_glm4_moe_lite_deterministic.py` added +68/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/test_deterministic_utils.py`, `test/registered/attention/test_glm4_moe_lite_deterministic.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #38890 - Support non-strict GLM47 tool calls with EBNF constraints

- Link: https://github.com/sgl-project/sglang/pull/38890
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`; associated commits `17ba2c2e7c7b`
- Diff scope read: GitHub Pull Request files API returned 14 files, +834/-22, 1073 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support non-strict GLM47 tool calls with EBNF constraints"; model line: GLM-4.6/4.7; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`; technical summary: Covers "Support non-strict GLM47 tool calls with EBNF constraints"; the main implementation surface is `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +495/-1 (496 lines); hunks: -1,8 +1,12; -660,3 +664,493 @@ def supports_structural_tag(self) -> bool:; symbols: supports_structural_tag, structure_info, _GlmTrieNode, __init__, touching `supports_structural_tag, structure_info, _GlmTrieNode`; `python/sglang/srt/function_call/glm47_moe_detector.py` modified +4/-0 (4 lines); hunks: -179,6 +179,7 @@ class Glm47MoeDetector(BaseFormatDetector):; -809,6 +810,9 @@ def _parse_argument_pairs(; symbols: Glm47MoeDetector, __init__, _parse_argument_pairs, parses_required_natively, touching `Glm47MoeDetector, __init__, _parse_argument_pairs`.
- Code diff details:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +495/-1 (496 lines); hunks: -1,8 +1,12; -660,3 +664,493 @@ def supports_structural_tag(self) -> bool:; symbols: supports_structural_tag, structure_info, _GlmTrieNode, __init__
  - `python/sglang/srt/function_call/glm47_moe_detector.py` modified +4/-0 (4 lines); hunks: -179,6 +179,7 @@ class Glm47MoeDetector(BaseFormatDetector):; -809,6 +810,9 @@ def _parse_argument_pairs(; symbols: Glm47MoeDetector, __init__, _parse_argument_pairs, parses_required_natively
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -1,8 +1,12 @@
+import hashlib
+from collections import deque
+from dataclasses import dataclass
-from typing import Any, Dict, List, Optional, Tuple
+from functools import lru_cache
+from typing import Any, Dict, List, Literal, Optional, Set, Tuple
diff -- python/sglang/srt/function_call/glm47_moe_detector.py
@@ -179,6 +179,7 @@ class Glm47MoeDetector(BaseFormatDetector):
+        self.use_full_assistant_constraint = False
@@ -809,6 +810,9 @@ def _parse_argument_pairs(
+    def parses_required_natively(self) -> bool:
+        return self.use_full_assistant_constraint
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +495/-1; `python/sglang/srt/function_call/glm47_moe_detector.py` modified +4/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/constrained/test_grammar_manager.py`, `test/registered/unit/constrained/test_reasoner_grammar_backend.py`, `test/registered/unit/entrypoints/openai/test_protocol.py`, `test/registered/unit/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
