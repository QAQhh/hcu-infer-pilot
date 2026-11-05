# sglang GLM-4.6/4.7 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/GLM/GLM-4.6.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/GLM/GLM-4.6V.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/GLM/GLM-4.7-Flash.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/GLM/GLM-4.7.mdx` | 无直接 PR 号提交 |
| `python/sglang/srt/arg_groups/model_overrides/glm4_moe.py` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/glm47_moe_detector.py` | [#15333](https://github.com/sgl-project/sglang/pull/15333), [#15753](https://github.com/sgl-project/sglang/pull/15753), [#28149](https://github.com/sgl-project/sglang/pull/28149), [#38890](https://github.com/sgl-project/sglang/pull/38890) |
| `python/sglang/srt/function_call/glm4_moe_detector.py` | [#13989](https://github.com/sgl-project/sglang/pull/13989), [#15333](https://github.com/sgl-project/sglang/pull/15333), [#15753](https://github.com/sgl-project/sglang/pull/15753), [#38890](https://github.com/sgl-project/sglang/pull/38890) |
| `python/sglang/srt/models/glm4_moe.py` | [#13873](https://github.com/sgl-project/sglang/pull/13873), [#14585](https://github.com/sgl-project/sglang/pull/14585), [#15333](https://github.com/sgl-project/sglang/pull/15333), [#17166](https://github.com/sgl-project/sglang/pull/17166), [#21403](https://github.com/sgl-project/sglang/pull/21403), [#21660](https://github.com/sgl-project/sglang/pull/21660), [#21851](https://github.com/sgl-project/sglang/pull/21851) |
| `python/sglang/srt/models/glm4_moe_lite.py` | [#21851](https://github.com/sgl-project/sglang/pull/21851), [#22509](https://github.com/sgl-project/sglang/pull/22509), [#26088](https://github.com/sgl-project/sglang/pull/26088), [#28516](https://github.com/sgl-project/sglang/pull/28516), [#31388](https://github.com/sgl-project/sglang/pull/31388) |
| `python/sglang/srt/models/glm4_moe_lite_nextn.py` | [#26088](https://github.com/sgl-project/sglang/pull/26088) |
| `python/sglang/srt/models/glm4_moe_nextn.py` | [#13873](https://github.com/sgl-project/sglang/pull/13873) |
| `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` | [#21534](https://github.com/sgl-project/sglang/pull/21534) |
| `test/registered/attention/test_glm4_moe_lite_deterministic.py` | [#33945](https://github.com/sgl-project/sglang/pull/33945) |
| `test/registered/moe/test_glm4_moe_models.py` | 无直接 PR 号提交 |
| `test/registered/unit/function_call/test_glm47_schema_types.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 17
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 17
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #13873 - Feat: GLM-4.6 supports shared experts fusion

- 链接: https://github.com/sgl-project/sglang/pull/13873
- 状态/时间: merged / 2025-12-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；关联提交 `982db4ebac26`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+252/-24，可读 patch 431 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Feat: GLM-4.6 supports shared experts fusion」；模型线: GLM-4.6/4.7；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；技术摘要: 覆盖「Feat: GLM-4.6 supports shared experts fusion」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +74/-19 (93 lines); hunks: -85,6 +85,7; -352,8 +353,14 @@ def __init__(; symbols: __init__, forward, forward_normal_dual_stream，涉及 `__init__, forward, forward_normal_dual_stream`；`python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-0 (4 lines); hunks: -139,6 +139,10 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +74/-19 (93 lines); hunks: -85,6 +85,7; -352,8 +353,14 @@ def __init__(; symbols: __init__, forward, forward_normal_dual_stream
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-0 (4 lines); hunks: -139,6 +139,10 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +74/-19; `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=161,N=192,device_name=NVIDIA_H200,dtype=fp8_w8a8,per_channel_quant=True.json`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_config.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14585 - [Glm46v] Bug fix for accuracy drop and unable to launch server

- 链接: https://github.com/sgl-project/sglang/pull/14585
- 状态/时间: merged / 2025-12-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `cf0478d602ce`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+308/-29，可读 patch 530 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Glm46v] Bug fix for accuracy drop and unable to launch server」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「[Glm46v] Bug fix for accuracy drop and unable to launch server」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -361,6 +361,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -361,6 +361,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -361,6 +361,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/pyproject.toml`, `python/sglang/srt/configs/qwen3_omni.py`, `python/sglang/srt/configs/qwen3_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13989 - Fix GLM-4.6 tool calls don't support streaming output for arguments i…

- 链接: https://github.com/sgl-project/sglang/pull/13989
- 状态/时间: merged / 2025-12-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm4_moe_detector.py`；关联提交 `80554598d33b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+527/-81，可读 patch 700 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix GLM-4.6 tool calls don't support streaming output for arguments i…」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/glm4_moe_detector.py`；技术摘要: 覆盖「Fix GLM-4.6 tool calls don't support streaming output for arguments i…」；主要实现面是 `python/sglang/srt/function_call/glm4_moe_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +498/-66 (564 lines); hunks: -2,16 +2,43; -21,32 +48,90 @@ def get_argument_type(func_name: str, arg_key: str, defined_...; symbols: get_argument_type, StreamState, parse_arguments，涉及 `get_argument_type, StreamState, parse_arguments`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +498/-66 (564 lines); hunks: -2,16 +2,43; -21,32 +48,90 @@ def get_argument_type(func_name: str, arg_key: str, defined_...; symbols: get_argument_type, StreamState, parse_arguments
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +498/-66
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #15333 - [GLM-4.7] GLM-4.7 Tool Parser and Doc Update

- 链接: https://github.com/sgl-project/sglang/pull/15333
- 状态/时间: merged / 2025-12-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`；关联提交 `b82c7a0ae744`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+809/-394，可读 patch 1356 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-4.7] GLM-4.7 Tool Parser and Doc Update」；模型线: GLM-4.6/4.7；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「[GLM-4.7] GLM-4.7 Tool Parser and Doc Update」；主要实现面是 `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/glm47_moe_detector.py` added +584/-0 (584 lines); hunks: -0,0 +1,584; symbols: StreamState, get_argument_type, _convert_to_number, parse_arguments，涉及 `StreamState, get_argument_type, _convert_to_number`；`python/sglang/srt/function_call/glm4_moe_detector.py` modified +5/-2 (7 lines); hunks: -43,9 +43,12 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number，涉及 `get_argument_type, _convert_to_number`；`python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -12,7 +12,7。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/glm47_moe_detector.py` added +584/-0 (584 lines); hunks: -0,0 +1,584; symbols: StreamState, get_argument_type, _convert_to_number, parse_arguments
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +5/-2 (7 lines); hunks: -43,9 +43,12 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -12,7 +12,7
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/glm47_moe_detector.py` added +584/-0; `python/sglang/srt/function_call/glm4_moe_detector.py` modified +5/-2; `python/sglang/srt/models/glm4_moe.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #15753 - Fix GLM-4.7 MoE Detector complex JSON Schema type parsing

- 链接: https://github.com/sgl-project/sglang/pull/15753
- 状态/时间: merged / 2026-01-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`；关联提交 `8ef5b9052825`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+869/-20，可读 patch 989 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix GLM-4.7 MoE Detector complex JSON Schema type parsing」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `test/registered/function_call/test_glm47_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`；技术摘要: 覆盖「Fix GLM-4.7 MoE Detector complex JSON Schema type parsing」；主要实现面是 `test/registered/function_call/test_glm47_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/function_call/test_glm47_moe_detector.py` modified +678/-3 (681 lines); hunks: -3,7 +3,11; -1172,5 +1176,676 @@ def test_streamed_raw_length_multiple_empty_returns(self):; symbols: test_streamed_raw_length_multiple_empty_returns, TestGlm4ComplexJsonSchema, setUp, test_get_argument_type_simple_type，涉及 `test_streamed_raw_length_multiple_empty_returns, TestGlm4ComplexJsonSchema, setUp`；`python/sglang/srt/function_call/glm47_moe_detector.py` modified +43/-10 (53 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _get_value_type, _format_value_complete，涉及 `get_argument_type, _get_value_type, _format_value_complete`；`python/sglang/srt/function_call/glm4_moe_detector.py` modified +44/-6 (50 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number, _get_value_type, _format_value_complete，涉及 `get_argument_type, _convert_to_number, _get_value_type`。
- 代码 diff 细节:
  - `test/registered/function_call/test_glm47_moe_detector.py` modified +678/-3 (681 lines); hunks: -3,7 +3,11; -1172,5 +1176,676 @@ def test_streamed_raw_length_multiple_empty_returns(self):; symbols: test_streamed_raw_length_multiple_empty_returns, TestGlm4ComplexJsonSchema, setUp, test_get_argument_type_simple_type
  - `python/sglang/srt/function_call/glm47_moe_detector.py` modified +43/-10 (53 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _get_value_type, _format_value_complete
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +44/-6 (50 lines); hunks: -12,6 +12,7; -31,6 +32,14 @@ def get_argument_type(; symbols: get_argument_type, _convert_to_number, _get_value_type, _format_value_complete
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/function_call/test_glm47_moe_detector.py` modified +678/-3
  - runtime: `python/sglang/srt/function_call/glm47_moe_detector.py` modified +43/-10; `python/sglang/srt/function_call/glm4_moe_detector.py` modified +44/-6
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_glm47_moe_detector.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17166 - [Fix] GLM 4.7 + NVFP4 + MTP

- 链接: https://github.com/sgl-project/sglang/pull/17166
- 状态/时间: merged / 2026-01-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `2ff0880a0ed1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+114/-9，可读 patch 206 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] GLM 4.7 + NVFP4 + MTP」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「[Fix] GLM 4.7 + NVFP4 + MTP」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +5/-1 (6 lines); hunks: -63,7 +63,10; -376,6 +379,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +5/-1 (6 lines); hunks: -63,7 +63,10; -376,6 +379,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21534 - [AMD] Add GLM-4.7-FP8 accuracy CI test for MI35x

- 链接: https://github.com/sgl-project/sglang/pull/21534
- 状态/时间: merged / 2026-03-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`；关联提交 `7078e385ea13`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+96/-0，可读 patch 118 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add GLM-4.7-FP8 accuracy CI test for MI35x」；模型线: GLM-4.6/4.7；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`；技术摘要: 覆盖「[AMD] Add GLM-4.7-FP8 accuracy CI test for MI35x」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: TestGLM47FP8EvalMI35x, test_glm_47_fp8，涉及 `TestGLM47FP8EvalMI35x, test_glm_47_fp8`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: TestGLM47FP8EvalMI35x, test_glm_47_fp8
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py` added +61/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_glm47_fp8_eval_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21660 - [GLM-V and GLM-4.7] Cast to FP32 before gate projection for GLM model.

- 链接: https://github.com/sgl-project/sglang/pull/21660
- 状态/时间: merged / 2026-03-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `ad064c2f4e33`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-1，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-V and GLM-4.7] Cast to FP32 before gate projection for GLM model.」；模型线: GLM-4.6/4.7；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「[GLM-V and GLM-4.7] Cast to FP32 before gate projection for GLM model.」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +6/-1 (7 lines); hunks: -327,9 +327,14 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +6/-1 (7 lines); hunks: -327,9 +327,14 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +6/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21851 - GLM-4.7 and GLM-4.7-Flash Loading and import format

- 链接: https://github.com/sgl-project/sglang/pull/21851
- 状态/时间: merged / 2026-04-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`；关联提交 `b7ae3b5a9a57`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+139/-86，可读 patch 486 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-4.7 and GLM-4.7-Flash Loading and import format」；模型线: GLM-4.6/4.7；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`；技术摘要: 覆盖「GLM-4.7 and GLM-4.7-Flash Loading and import format」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +130/-57 (187 lines); hunks: -15,13 +15,15; -62,6 +64,7; symbols: __init__, get_moe_weights，涉及 `__init__, get_moe_weights`；`python/sglang/srt/models/glm4_moe_lite.py` modified +9/-29 (38 lines); hunks: -12,13 +12,15; -29,12 +31,14; symbols: forward, __init__, load_weights，涉及 `forward, __init__, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +130/-57 (187 lines); hunks: -15,13 +15,15; -62,6 +64,7; symbols: __init__, get_moe_weights
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +9/-29 (38 lines); hunks: -12,13 +12,15; -29,12 +31,14; symbols: forward, __init__, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +130/-57; `python/sglang/srt/models/glm4_moe_lite.py` modified +9/-29
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21403 - [AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8

- 链接: https://github.com/sgl-project/sglang/pull/21403
- 状态/时间: merged / 2026-04-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `7e4e1dcd7ac8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+149/-13，可读 patch 269 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8」；模型线: GLM-4.6/4.7；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「[AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +58/-3 (61 lines); hunks: -289,7 +289,9 @@ def forward_prepare(; -865,6 +867,51 @@ def __init__(; symbols: forward_prepare, __init__, _detect_fp8_per_token_quant, _detect_attn_quant_format，涉及 `forward_prepare, __init__, _detect_fp8_per_token_quant`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +58/-3 (61 lines); hunks: -289,7 +289,9 @@ def forward_prepare(; -865,6 +867,51 @@ def __init__(; symbols: forward_prepare, __init__, _detect_fp8_per_token_quant, _detect_attn_quant_format
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +58/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22509 - [NPU]Fix GLM-4.7-Flash failed on NPU

- 链接: https://github.com/sgl-project/sglang/pull/22509
- 状态/时间: merged / 2026-04-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe_lite.py`；关联提交 `92f28e9ba80b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-2，可读 patch 27 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]Fix GLM-4.7-Flash failed on NPU」；模型线: GLM-4.6/4.7；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4_moe_lite.py`；技术摘要: 覆盖「[NPU]Fix GLM-4.7-Flash failed on NPU」；主要实现面是 `python/sglang/srt/models/glm4_moe_lite.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe_lite.py` modified +3/-1 (4 lines); hunks: -20,7 +20,6; -81,6 +80,9。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +3/-1 (4 lines); hunks: -20,7 +20,6; -81,6 +80,9
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -20,7 +20,6 @@
-from sgl_kernel import dsv3_router_gemm
@@ -81,6 +80,9 @@
+if _is_cuda:
+    from sgl_kernel import dsv3_router_gemm
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +3/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe_lite.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26088 - GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP

- 链接: https://github.com/sgl-project/sglang/pull/26088
- 状态/时间: merged / 2026-05-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py`；关联提交 `7ef06bfc06ec`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+799/-86，可读 patch 1076 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP」；模型线: GLM-4.6/4.7；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py`；技术摘要: 覆盖「GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP」；主要实现面是 `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe_lite.py` modified +603/-81 (684 lines); hunks: -1,4 +1,4; -12,77 +12,81; symbols: forward, __init__, Glm4MoeLiteSparseMoeBlock，涉及 `forward, __init__, Glm4MoeLiteSparseMoeBlock`；`python/sglang/srt/models/glm4_moe_lite_nextn.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: Glm4MoeLiteModelNextN, __init__, forward, Glm4MoeLiteForCausalLMNextN，涉及 `Glm4MoeLiteModelNextN, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +603/-81 (684 lines); hunks: -1,4 +1,4; -12,77 +12,81; symbols: forward, __init__, Glm4MoeLiteSparseMoeBlock
  - `python/sglang/srt/models/glm4_moe_lite_nextn.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: Glm4MoeLiteModelNextN, __init__, forward, Glm4MoeLiteForCausalLMNextN
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +603/-81; `python/sglang/srt/models/glm4_moe_lite_nextn.py` added +182/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4_moe_lite.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28149 - Support GLM-4.7 function calling via structural tags

- 链接: https://github.com/sgl-project/sglang/pull/28149
- 状态/时间: merged / 2026-06-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm47_moe_detector.py`；关联提交 `f79a6b5c3355`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+104/-6，可读 patch 137 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support GLM-4.7 function calling via structural tags」；模型线: GLM-4.6/4.7；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/glm47_moe_detector.py`；技术摘要: 覆盖「Support GLM-4.7 function calling via structural tags」；主要实现面是 `python/sglang/srt/function_call/glm47_moe_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/glm47_moe_detector.py` modified +41/-6 (47 lines); hunks: -3,10 +3,15; -17,6 +22,21; symbols: _glm47_native_structural_tag_available, StreamState, _parse_argument_pairs, supports_structural_tag，涉及 `_glm47_native_structural_tag_available, StreamState, _parse_argument_pairs`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/glm47_moe_detector.py` modified +41/-6 (47 lines); hunks: -3,10 +3,15; -17,6 +22,21; symbols: _glm47_native_structural_tag_available, StreamState, _parse_argument_pairs, supports_structural_tag
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/glm47_moe_detector.py` modified +41/-6
- 验证与风险: diff 自带测试面 `test/registered/unit/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #28516 - [NPU] Add MTP support for GLM-4.7-Flash

- 链接: https://github.com/sgl-project/sglang/pull/28516
- 状态/时间: merged / 2026-06-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe_lite.py`；关联提交 `2a9cce5d2757`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+38/-2，可读 patch 74 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Add MTP support for GLM-4.7-Flash」；模型线: GLM-4.6/4.7；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm4_moe_lite.py`；技术摘要: 覆盖「[NPU] Add MTP support for GLM-4.7-Flash」；主要实现面是 `python/sglang/srt/models/glm4_moe_lite.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe_lite.py` modified +2/-0 (2 lines); hunks: -548,6 +548,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +2/-0 (2 lines); hunks: -548,6 +548,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -548,6 +548,8 @@ def __init__(
+        # Required for MTP: Glm4MoeLiteModelNextN bypasses Glm4MoeLiteForCausalLM.__init__
+        config.moe_layer_freq = 1
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/models/glm4_moe_lite.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31388 - [NPU]revert add scoring func for GLM 4.7 Flash

- 链接: https://github.com/sgl-project/sglang/pull/31388
- 状态/时间: merged / 2026-07-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe_lite.py`；关联提交 `871c6482037e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+1/-2，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]revert add scoring func for GLM 4.7 Flash」；模型线: GLM-4.6/4.7；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm4_moe_lite.py`；技术摘要: 覆盖「[NPU]revert add scoring func for GLM 4.7 Flash」；主要实现面是 `python/sglang/srt/models/glm4_moe_lite.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe_lite.py` modified +0/-1 (1 lines); hunks: -225,7 +225,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe_lite.py` modified +0/-1 (1 lines); hunks: -225,7 +225,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe_lite.py
@@ -225,7 +225,6 @@ def __init__(
-            **({"scoring_func": "sigmoid"}),
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe_lite.py` modified +0/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/glm4_moe_lite.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33945 - feat: support deterministic FA4 for GLM-4.7-Flash

- 链接: https://github.com/sgl-project/sglang/pull/33945
- 状态/时间: merged / 2026-08-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/attention/test_glm4_moe_lite_deterministic.py`；关联提交 `2d76d537e551`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+86/-7，可读 patch 151 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: support deterministic FA4 for GLM-4.7-Flash」；模型线: GLM-4.6/4.7；类别: 性能/后端优化；主要 diff: `test/registered/attention/test_glm4_moe_lite_deterministic.py`；技术摘要: 覆盖「feat: support deterministic FA4 for GLM-4.7-Flash」；主要实现面是 `test/registered/attention/test_glm4_moe_lite_deterministic.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/attention/test_glm4_moe_lite_deterministic.py` added +68/-0 (68 lines); hunks: -0,0 +1,68; symbols: below, TestGlm4MoeLiteFa4Deterministic, get_model, get_server_args，涉及 `below, TestGlm4MoeLiteFa4Deterministic, get_model`。
- 代码 diff 细节:
  - `test/registered/attention/test_glm4_moe_lite_deterministic.py` added +68/-0 (68 lines); hunks: -0,0 +1,68; symbols: below, TestGlm4MoeLiteFa4Deterministic, get_model, get_server_args
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/attention/test_glm4_moe_lite_deterministic.py` added +68/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/test_deterministic_utils.py`, `test/registered/attention/test_glm4_moe_lite_deterministic.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38890 - Support non-strict GLM47 tool calls with EBNF constraints

- 链接: https://github.com/sgl-project/sglang/pull/38890
- 状态/时间: merged / 2026-09-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`；关联提交 `17ba2c2e7c7b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+834/-22，可读 patch 1073 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support non-strict GLM47 tool calls with EBNF constraints」；模型线: GLM-4.6/4.7；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`；技术摘要: 覆盖「Support non-strict GLM47 tool calls with EBNF constraints」；主要实现面是 `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +495/-1 (496 lines); hunks: -1,8 +1,12; -660,3 +664,493 @@ def supports_structural_tag(self) -> bool:; symbols: supports_structural_tag, structure_info, _GlmTrieNode, __init__，涉及 `supports_structural_tag, structure_info, _GlmTrieNode`；`python/sglang/srt/function_call/glm47_moe_detector.py` modified +4/-0 (4 lines); hunks: -179,6 +179,7 @@ class Glm47MoeDetector(BaseFormatDetector):; -809,6 +810,9 @@ def _parse_argument_pairs(; symbols: Glm47MoeDetector, __init__, _parse_argument_pairs, parses_required_natively，涉及 `Glm47MoeDetector, __init__, _parse_argument_pairs`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +495/-1 (496 lines); hunks: -1,8 +1,12; -660,3 +664,493 @@ def supports_structural_tag(self) -> bool:; symbols: supports_structural_tag, structure_info, _GlmTrieNode, __init__
  - `python/sglang/srt/function_call/glm47_moe_detector.py` modified +4/-0 (4 lines); hunks: -179,6 +179,7 @@ class Glm47MoeDetector(BaseFormatDetector):; -809,6 +810,9 @@ def _parse_argument_pairs(; symbols: Glm47MoeDetector, __init__, _parse_argument_pairs, parses_required_natively
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +495/-1; `python/sglang/srt/function_call/glm47_moe_detector.py` modified +4/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/constrained/test_grammar_manager.py`, `test/registered/unit/constrained/test_reasoner_grammar_backend.py`, `test/registered/unit/entrypoints/openai/test_protocol.py`, `test/registered/unit/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
