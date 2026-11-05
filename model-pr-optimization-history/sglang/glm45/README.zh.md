# sglang GLM-4.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/GLM/GLM-4.5.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/GLM/GLM-4.5V.mdx` | 无直接 PR 号提交 |
| `python/sglang/srt/arg_groups/model_overrides/glm4_moe.py` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/glm4_moe_detector.py` | [#8224](https://github.com/sgl-project/sglang/pull/8224), [#8445](https://github.com/sgl-project/sglang/pull/8445), [#11017](https://github.com/sgl-project/sglang/pull/11017) |
| `python/sglang/srt/models/glm4_moe.py` | [#8224](https://github.com/sgl-project/sglang/pull/8224), [#8456](https://github.com/sgl-project/sglang/pull/8456), [#8729](https://github.com/sgl-project/sglang/pull/8729), [#8804](https://github.com/sgl-project/sglang/pull/8804), [#11017](https://github.com/sgl-project/sglang/pull/11017), [#11665](https://github.com/sgl-project/sglang/pull/11665), [#11800](https://github.com/sgl-project/sglang/pull/11800), [#22961](https://github.com/sgl-project/sglang/pull/22961), [#40870](https://github.com/sgl-project/sglang/pull/40870) |
| `python/sglang/srt/models/glm4_moe_lite.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/glm4_moe_lite_nextn.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/glm4_moe_nextn.py` | [#8224](https://github.com/sgl-project/sglang/pull/8224), [#11017](https://github.com/sgl-project/sglang/pull/11017), [#11800](https://github.com/sgl-project/sglang/pull/11800), [#25524](https://github.com/sgl-project/sglang/pull/25524) |
| `test/registered/attention/test_glm4_moe_lite_deterministic.py` | 无直接 PR 号提交 |
| `test/registered/moe/test_glm4_moe_models.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 11
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 11
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2025-07-28 | [#8224](https://github.com/sgl-project/sglang/pull/8224) | merged | GLM-4.5 Model Support | `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/function_call/glm4_moe_detector.py` |
| 2025-07-28 | [#8445](https://github.com/sgl-project/sglang/pull/8445) | merged | GLM-4.5 Model Support Follow-up | `python/sglang/srt/function_call/glm4_moe_detector.py` |
| 2025-07-28 | [#8456](https://github.com/sgl-project/sglang/pull/8456) | merged | fix GLM4_MOE launch with compressed_tensor quant model | `python/sglang/srt/models/glm4_moe.py` |
| 2025-08-03 | [#8729](https://github.com/sgl-project/sglang/pull/8729) | merged | use fp32 for e_score_correction_bias in GLM-4.5 | `python/sglang/srt/models/glm4_moe.py` |
| 2025-08-05 | [#8804](https://github.com/sgl-project/sglang/pull/8804) | merged | GLM-4.5 and GLM-4.5-Air both support | `python/sglang/srt/models/glm4_moe.py` |
| 2025-09-28 | [#11017](https://github.com/sgl-project/sglang/pull/11017) | merged | Update GLM-4.5 Model Doc | `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py` |
| 2025-10-18 | [#11665](https://github.com/sgl-project/sglang/pull/11665) | merged | fix(glm45): disable reduce scatter | `python/sglang/srt/models/glm4_moe.py` |
| 2025-10-24 | [#11800](https://github.com/sgl-project/sglang/pull/11800) | merged | Refactoring GLM-4.5 and GLM-4.5V related implementations | `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py` |
| 2026-04-28 | [#22961](https://github.com/sgl-project/sglang/pull/22961) | merged | [NPU] Fix issue and support GLM-4.5V | `python/sglang/srt/models/glm4_moe.py` |
| 2026-05-19 | [#25524](https://github.com/sgl-project/sglang/pull/25524) | merged | [Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP | `python/sglang/srt/models/glm4_moe_nextn.py` |
| 2026-09-23 | [#40870](https://github.com/sgl-project/sglang/pull/40870) | merged | [Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE | `python/sglang/srt/models/glm4_moe.py` |

## 逐 PR diff 审计卡

### PR #8224 - GLM-4.5 Model Support

- 链接: https://github.com/sgl-project/sglang/pull/8224
- 状态/时间: merged / 2025-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；关联提交 `6d6a8bc278ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+1673/-7，可读 patch 1853 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-4.5 Model Support」；模型线: GLM-4.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`；技术摘要: 覆盖「GLM-4.5 Model Support」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` added +1034/-0 (1034 lines); hunks: -0,0 +1,1034; symbols: Glm4MoeMLP, __init__, forward, Glm4MoeAttention，涉及 `Glm4MoeMLP, __init__, forward`；`python/sglang/srt/models/glm4_moe_nextn.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: Glm4MoeModelNextN, __init__, forward, Glm4MoeForCausalLMNextN，涉及 `Glm4MoeModelNextN, __init__, forward`；`python/sglang/srt/function_call/glm4_moe_detector.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: get_argument_type, parse_arguments, Glm4MoeDetector, __init__，涉及 `get_argument_type, parse_arguments, Glm4MoeDetector`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` added +1034/-0 (1034 lines); hunks: -0,0 +1,1034; symbols: Glm4MoeMLP, __init__, forward, Glm4MoeAttention
  - `python/sglang/srt/models/glm4_moe_nextn.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: Glm4MoeModelNextN, __init__, forward, Glm4MoeForCausalLMNextN
  - `python/sglang/srt/function_call/glm4_moe_detector.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: get_argument_type, parse_arguments, Glm4MoeDetector, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -0,0 +1,1034 @@
+# Copyright 2025-2026 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/glm4_moe_nextn.py
@@ -0,0 +1,167 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -0,0 +1,165 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` added +1034/-0; `python/sglang/srt/models/glm4_moe_nextn.py` added +167/-0; `python/sglang/srt/function_call/glm4_moe_detector.py` added +165/-0
- 验证与风险: diff 自带测试面 `test/srt/openai_server/features/test_enable_thinking.py`, `test/srt/openai_server/function_call/test_openai_function_calling.py`, `test/srt/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #8445 - GLM-4.5 Model Support Follow-up

- 链接: https://github.com/sgl-project/sglang/pull/8445
- 状态/时间: merged / 2025-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm4_moe_detector.py`；关联提交 `581e7dcb92a7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+44/-15，可读 patch 168 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-4.5 Model Support Follow-up」；模型线: GLM-4.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/glm4_moe_detector.py`；技术摘要: 覆盖「GLM-4.5 Model Support Follow-up」；主要实现面是 `python/sglang/srt/function_call/glm4_moe_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +1/-2 (3 lines); hunks: -156,8 +156,7 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf，涉及 `build_ebnf`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +1/-2 (3 lines); hunks: -156,8 +156,7 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -156,8 +156,7 @@ def build_ebnf(self, tools: List[Tool]):
-            # GLM4Moe is not compatible with multiple tool_calls under tool_choice condition: it will output unlimited tool_calls...
-            # tool_call_separator="\\n",
+            tool_call_separator="\\n",
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +1/-2
- 验证与风险: diff 自带测试面 `test/srt/openai_server/features/test_enable_thinking.py`, `test/srt/openai_server/function_call/test_openai_function_calling.py`, `test/srt/openai_server/function_call/test_tool_choice.py`, `test/srt/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #8456 - fix GLM4_MOE launch with compressed_tensor quant model

- 链接: https://github.com/sgl-project/sglang/pull/8456
- 状态/时间: merged / 2025-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `25f73c6cf3c2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix GLM4_MOE launch with compressed_tensor quant model」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「fix GLM4_MOE launch with compressed_tensor quant model」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -795,6 +795,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -795,6 +795,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -795,6 +795,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+                    or self.quant_config.get_name() == "compressed_tensors"
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #8729 - use fp32 for e_score_correction_bias in GLM-4.5

- 链接: https://github.com/sgl-project/sglang/pull/8729
- 状态/时间: merged / 2025-08-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `760286e3d378`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「use fp32 for e_score_correction_bias in GLM-4.5」；模型线: GLM-4.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「use fp32 for e_score_correction_bias in GLM-4.5」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -343,7 +343,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -343,7 +343,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -343,7 +343,7 @@ def __init__(
-            torch.empty((config.n_routed_experts))
+            torch.empty((config.n_routed_experts), dtype=torch.float32)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #8804 - GLM-4.5 and GLM-4.5-Air both support

- 链接: https://github.com/sgl-project/sglang/pull/8804
- 状态/时间: merged / 2025-08-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `a4b0d5c9e5cb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-2，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-4.5 and GLM-4.5-Air both support」；模型线: GLM-4.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「GLM-4.5 and GLM-4.5-Air both support」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +1/-2 (3 lines); hunks: -785,7 +785,7 @@ def __init__(; -797,7 +797,6 @@ def determine_num_fused_shared_experts(; symbols: __init__, determine_num_fused_shared_experts，涉及 `__init__, determine_num_fused_shared_experts`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-2 (3 lines); hunks: -785,7 +785,7 @@ def __init__(; -797,7 +797,6 @@ def determine_num_fused_shared_experts(; symbols: __init__, determine_num_fused_shared_experts
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -785,7 +785,7 @@ def __init__(
-        self, architecture: str = "DeepseekV3ForCausalLM"
+        self, architecture: str = "Glm4MoeForCausalLM"
@@ -797,7 +797,6 @@ def determine_num_fused_shared_experts(
-            or self.config.n_routed_experts != 128
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #11017 - Update GLM-4.5 Model Doc

- 链接: https://github.com/sgl-project/sglang/pull/11017
- 状态/时间: merged / 2025-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；关联提交 `abb6781573a8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+11/-12，可读 patch 88 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update GLM-4.5 Model Doc」；模型线: GLM-4.5；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；技术摘要: 覆盖「Update GLM-4.5 Model Doc」；主要实现面是 `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +3/-3 (6 lines); hunks: -39,7 +39,7 @@ def parse_arguments(json_value):; -53,7 +53,7 @@ def __init__(self):; symbols: parse_arguments, Glm4MoeDetector, __init__, has_tool_call，涉及 `parse_arguments, Glm4MoeDetector, __init__`；`python/sglang/srt/models/glm4_moe.py` modified +3/-3 (6 lines); hunks: -12,7 +12,7; -785,9 +785,9 @@ def determine_num_fused_shared_experts(; symbols: determine_num_fused_shared_experts，涉及 `determine_num_fused_shared_experts`；`python/sglang/srt/models/glm4_moe_nextn.py` modified +2/-2 (4 lines); hunks: -12,7 +12,7; -48,7 +48,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +3/-3 (6 lines); hunks: -39,7 +39,7 @@ def parse_arguments(json_value):; -53,7 +53,7 @@ def __init__(self):; symbols: parse_arguments, Glm4MoeDetector, __init__, has_tool_call
  - `python/sglang/srt/models/glm4_moe.py` modified +3/-3 (6 lines); hunks: -12,7 +12,7; -785,9 +785,9 @@ def determine_num_fused_shared_experts(; symbols: determine_num_fused_shared_experts
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +2/-2 (4 lines); hunks: -12,7 +12,7; -48,7 +48,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -39,7 +39,7 @@ def parse_arguments(json_value):
-    Detector for GLM-4.5 models.
+    Detector for GLM-4.5 and GLM-4.6 models.
@@ -53,7 +53,7 @@ def __init__(self):
-        """Check if the text contains a glm-4.5 format tool call."""
+        """Check if the text contains a glm-4.5 / glm-4.6 format tool call."""
@@ -102,7 +102,7 @@ def parse_streaming_increment(
diff -- python/sglang/srt/models/glm4_moe.py
@@ -12,7 +12,7 @@
-"""Inference-only GLM-4.5 model compatible with HuggingFace weights"""
+"""Inference-only GLM-4.5, GLM-4.6 model compatible with HuggingFace weights"""
@@ -785,9 +785,9 @@ def determine_num_fused_shared_experts(
-            disable_reason = "Only GLM-4.5 on NV-platform with capability >= 80 can use shared experts fusion optimization."
+            disable_reason = "Only GLM-4.5 or GLM-4.6 on NV-platform with capability >= 80 can use shared experts fusion optimization."
-            disable_reason = "Deepseek and GLM-4.5 can not use shared experts fusion optimization under expert parallelism."
diff -- python/sglang/srt/models/glm4_moe_nextn.py
@@ -12,7 +12,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +3/-3; `python/sglang/srt/models/glm4_moe.py` modified +3/-3; `python/sglang/srt/models/glm4_moe_nextn.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #11665 - fix(glm45): disable reduce scatter

- 链接: https://github.com/sgl-project/sglang/pull/11665
- 状态/时间: merged / 2025-10-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `f7ab9554554f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(glm45): disable reduce scatter」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「fix(glm45): disable reduce scatter」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -662,7 +662,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -662,7 +662,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -662,7 +662,7 @@ def __init__(
-            allow_reduce_scatter=True,
+            allow_reduce_scatter=False,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #11800 - Refactoring GLM-4.5 and GLM-4.5V related implementations

- 链接: https://github.com/sgl-project/sglang/pull/11800
- 状态/时间: merged / 2025-10-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；关联提交 `4060ed37cb67`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+356/-565，可读 patch 1370 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Refactoring GLM-4.5 and GLM-4.5V related implementations」；模型线: GLM-4.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`；技术摘要: 覆盖「Refactoring GLM-4.5 and GLM-4.5V related implementations」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +322/-354 (676 lines); hunks: -15,7 +15,7; -27,10 +27,16; symbols: __init__, forward, Glm4MoeSparseMoeBlock，涉及 `__init__, forward, Glm4MoeSparseMoeBlock`；`python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-14 (18 lines); hunks: -12,7 +12,8; -33,7 +34,7; symbols: forward, Glm4MoeForCausalLMNextN, __init__，涉及 `forward, Glm4MoeForCausalLMNextN, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +322/-354 (676 lines); hunks: -15,7 +15,7; -27,10 +27,16; symbols: __init__, forward, Glm4MoeSparseMoeBlock
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-14 (18 lines); hunks: -12,7 +12,8; -33,7 +34,7; symbols: forward, Glm4MoeForCausalLMNextN, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -15,7 +15,7 @@
-from typing import Any, Dict, Iterable, Optional, Tuple
+from typing import Any, Dict, Iterable, Optional, Tuple, Union
@@ -27,10 +27,16 @@
+    parallel_state,
+from sglang.srt.distributed.device_communicators.pynccl_allocator import (
+    use_symmetric_memory,
diff -- python/sglang/srt/models/glm4_moe_nextn.py
@@ -12,7 +12,8 @@
-"""Inference-only GLM-4.5, GLM-4.6 NextN Speculative Decoding."""
+"""Inference-only GLM-4.5, GLM-4.6 Speculative Decoding."""
@@ -33,7 +34,7 @@
-from sglang.srt.utils import BumpAllocator, add_prefix
+from sglang.srt.utils import add_prefix
@@ -84,14 +85,6 @@ def forward(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +322/-354; `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-14
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/models/glm4v_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22961 - [NPU] Fix issue and support GLM-4.5V

- 链接: https://github.com/sgl-project/sglang/pull/22961
- 状态/时间: merged / 2026-04-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `9ffc0cc67ee5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+17/-5，可读 patch 36 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Fix issue and support GLM-4.5V」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「[NPU] Fix issue and support GLM-4.5V」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +17/-5 (22 lines); hunks: -314,18 +314,30 @@ def forward_prepare(; symbols: forward_prepare，涉及 `forward_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +17/-5 (22 lines); hunks: -314,18 +314,30 @@ def forward_prepare(; symbols: forward_prepare
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -314,18 +314,30 @@ def forward_prepare(
+            if self.use_qk_norm:
+                eps = self.q_norm.variance_epsilon
+                q_weight = self.q_norm.weight
+                k_weight = self.k_norm.weight
+                q_bias = getattr(self.q_norm, "bias", None)
+                k_bias = getattr(self.k_norm, "bias", None)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +17/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25524 - [Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP

- 链接: https://github.com/sgl-project/sglang/pull/25524
- 状态/时间: merged / 2026-05-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe_nextn.py`；关联提交 `2bcb6d2f8244`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-25，可读 patch 79 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4_moe_nextn.py`；技术摘要: 覆盖「[Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP」；主要实现面是 `python/sglang/srt/models/glm4_moe_nextn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe_nextn.py` modified +11/-25 (36 lines); hunks: -12,9 +12,8; -23,7 +22,6; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +11/-25 (36 lines); hunks: -12,9 +12,8; -23,7 +22,6; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe_nextn.py
@@ -12,9 +12,8 @@
-"""Inference-only GLM-4.5, GLM-4.6 Speculative Decoding."""
+"""Inference-only GLM-4.5, GLM-4.6 and GLM-4.7 Speculative Decoding."""
-import contextlib
@@ -23,7 +22,6 @@
-from sglang.srt.environ import temp_set_env
@@ -36,7 +34,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe_nextn.py` modified +11/-25
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4_moe_nextn.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #40870 - [Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE

- 链接: https://github.com/sgl-project/sglang/pull/40870
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4_moe.py`；关联提交 `e1048a215ce9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+190/-74，可读 patch 324 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE」；模型线: GLM-4.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/glm4_moe.py`；技术摘要: 覆盖「[Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE」；主要实现面是 `python/sglang/srt/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4_moe.py` modified +3/-23 (26 lines); hunks: -83,7 +83,7; -964,29 +964,9 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4_moe.py` modified +3/-23 (26 lines); hunks: -83,7 +83,7; -964,29 +964,9 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -83,7 +83,7 @@
-from sglang.srt.runtime_context import get_exec, get_forward, get_parallel, get_stream
+from sglang.srt.runtime_context import get_exec, get_parallel, get_stream
@@ -964,29 +964,9 @@ def forward(
-        fuse_mlp_allreduce = (
-            self.layer_communicator.should_fuse_mlp_allreduce_with_next_layer(
-                forward_batch
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +3/-23
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/test_communicator_ffn_exit.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
