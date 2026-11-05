# sglang GLM-4.5 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/GLM/GLM-4.5.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/GLM/GLM-4.5V.mdx` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/glm4_moe.py` | no direct PR-number commit |
| `python/sglang/srt/function_call/glm4_moe_detector.py` | [#8224](https://github.com/sgl-project/sglang/pull/8224), [#8445](https://github.com/sgl-project/sglang/pull/8445), [#11017](https://github.com/sgl-project/sglang/pull/11017) |
| `python/sglang/srt/models/glm4_moe.py` | [#8224](https://github.com/sgl-project/sglang/pull/8224), [#8456](https://github.com/sgl-project/sglang/pull/8456), [#8729](https://github.com/sgl-project/sglang/pull/8729), [#8804](https://github.com/sgl-project/sglang/pull/8804), [#11017](https://github.com/sgl-project/sglang/pull/11017), [#11665](https://github.com/sgl-project/sglang/pull/11665), [#11800](https://github.com/sgl-project/sglang/pull/11800), [#22961](https://github.com/sgl-project/sglang/pull/22961), [#40870](https://github.com/sgl-project/sglang/pull/40870) |
| `python/sglang/srt/models/glm4_moe_lite.py` | no direct PR-number commit |
| `python/sglang/srt/models/glm4_moe_lite_nextn.py` | no direct PR-number commit |
| `python/sglang/srt/models/glm4_moe_nextn.py` | [#8224](https://github.com/sgl-project/sglang/pull/8224), [#11017](https://github.com/sgl-project/sglang/pull/11017), [#11800](https://github.com/sgl-project/sglang/pull/11800), [#25524](https://github.com/sgl-project/sglang/pull/25524) |
| `test/registered/attention/test_glm4_moe_lite_deterministic.py` | no direct PR-number commit |
| `test/registered/moe/test_glm4_moe_models.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 11
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 11
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
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

## Per-PR Diff Audit Cards

### PR #8224 - GLM-4.5 Model Support

- Link: https://github.com/sgl-project/sglang/pull/8224
- Status/date: merged / 2025-07-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; associated commits `6d6a8bc278ea`
- Diff scope read: GitHub Pull Request files API returned 14 files, +1673/-7, 1853 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "GLM-4.5 Model Support"; model line: GLM-4.5; category: model support/runtime entry; main diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`; technical summary: Covers "GLM-4.5 Model Support"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` added +1034/-0 (1034 lines); hunks: -0,0 +1,1034; symbols: Glm4MoeMLP, __init__, forward, Glm4MoeAttention, touching `Glm4MoeMLP, __init__, forward`; `python/sglang/srt/models/glm4_moe_nextn.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: Glm4MoeModelNextN, __init__, forward, Glm4MoeForCausalLMNextN, touching `Glm4MoeModelNextN, __init__, forward`; `python/sglang/srt/function_call/glm4_moe_detector.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: get_argument_type, parse_arguments, Glm4MoeDetector, __init__, touching `get_argument_type, parse_arguments, Glm4MoeDetector`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` added +1034/-0 (1034 lines); hunks: -0,0 +1,1034; symbols: Glm4MoeMLP, __init__, forward, Glm4MoeAttention
  - `python/sglang/srt/models/glm4_moe_nextn.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: Glm4MoeModelNextN, __init__, forward, Glm4MoeForCausalLMNextN
  - `python/sglang/srt/function_call/glm4_moe_detector.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: get_argument_type, parse_arguments, Glm4MoeDetector, __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` added +1034/-0; `python/sglang/srt/models/glm4_moe_nextn.py` added +167/-0; `python/sglang/srt/function_call/glm4_moe_detector.py` added +165/-0
- Risk and verification: The diff ships test coverage in `test/srt/openai_server/features/test_enable_thinking.py`, `test/srt/openai_server/function_call/test_openai_function_calling.py`, `test/srt/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #8445 - GLM-4.5 Model Support Follow-up

- Link: https://github.com/sgl-project/sglang/pull/8445
- Status/date: merged / 2025-07-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm4_moe_detector.py`; associated commits `581e7dcb92a7`
- Diff scope read: GitHub Pull Request files API returned 6 files, +44/-15, 168 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "GLM-4.5 Model Support Follow-up"; model line: GLM-4.5; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/glm4_moe_detector.py`; technical summary: Covers "GLM-4.5 Model Support Follow-up"; the main implementation surface is `python/sglang/srt/function_call/glm4_moe_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +1/-2 (3 lines); hunks: -156,8 +156,7 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf, touching `build_ebnf`.
- Code diff details:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +1/-2 (3 lines); hunks: -156,8 +156,7 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/glm4_moe_detector.py
@@ -156,8 +156,7 @@ def build_ebnf(self, tools: List[Tool]):
-            # GLM4Moe is not compatible with multiple tool_calls under tool_choice condition: it will output unlimited tool_calls...
-            # tool_call_separator="\\n",
+            tool_call_separator="\\n",
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +1/-2
- Risk and verification: The diff ships test coverage in `test/srt/openai_server/features/test_enable_thinking.py`, `test/srt/openai_server/function_call/test_openai_function_calling.py`, `test/srt/openai_server/function_call/test_tool_choice.py`, `test/srt/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #8456 - fix GLM4_MOE launch with compressed_tensor quant model

- Link: https://github.com/sgl-project/sglang/pull/8456
- Status/date: merged / 2025-07-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `25f73c6cf3c2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix GLM4_MOE launch with compressed_tensor quant model"; model line: GLM-4.5; category: bug fix; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "fix GLM4_MOE launch with compressed_tensor quant model"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -795,6 +795,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-0 (1 lines); hunks: -795,6 +795,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -795,6 +795,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+                    or self.quant_config.get_name() == "compressed_tensors"
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #8729 - use fp32 for e_score_correction_bias in GLM-4.5

- Link: https://github.com/sgl-project/sglang/pull/8729
- Status/date: merged / 2025-08-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `760286e3d378`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "use fp32 for e_score_correction_bias in GLM-4.5"; model line: GLM-4.5; category: model implementation change; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "use fp32 for e_score_correction_bias in GLM-4.5"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -343,7 +343,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -343,7 +343,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -343,7 +343,7 @@ def __init__(
-            torch.empty((config.n_routed_experts))
+            torch.empty((config.n_routed_experts), dtype=torch.float32)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #8804 - GLM-4.5 and GLM-4.5-Air both support

- Link: https://github.com/sgl-project/sglang/pull/8804
- Status/date: merged / 2025-08-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `a4b0d5c9e5cb`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-2, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "GLM-4.5 and GLM-4.5-Air both support"; model line: GLM-4.5; category: model support/runtime entry; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "GLM-4.5 and GLM-4.5-Air both support"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +1/-2 (3 lines); hunks: -785,7 +785,7 @@ def __init__(; -797,7 +797,6 @@ def determine_num_fused_shared_experts(; symbols: __init__, determine_num_fused_shared_experts, touching `__init__, determine_num_fused_shared_experts`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-2 (3 lines); hunks: -785,7 +785,7 @@ def __init__(; -797,7 +797,6 @@ def determine_num_fused_shared_experts(; symbols: __init__, determine_num_fused_shared_experts
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -785,7 +785,7 @@ def __init__(
-        self, architecture: str = "DeepseekV3ForCausalLM"
+        self, architecture: str = "Glm4MoeForCausalLM"
@@ -797,7 +797,6 @@ def determine_num_fused_shared_experts(
-            or self.config.n_routed_experts != 128
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11017 - Update GLM-4.5 Model Doc

- Link: https://github.com/sgl-project/sglang/pull/11017
- Status/date: merged / 2025-09-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; associated commits `abb6781573a8`
- Diff scope read: GitHub Pull Request files API returned 5 files, +11/-12, 88 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Update GLM-4.5 Model Doc"; model line: GLM-4.5; category: docs/tests/CI; main diff: `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; technical summary: Covers "Update GLM-4.5 Model Doc"; the main implementation surface is `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +3/-3 (6 lines); hunks: -39,7 +39,7 @@ def parse_arguments(json_value):; -53,7 +53,7 @@ def __init__(self):; symbols: parse_arguments, Glm4MoeDetector, __init__, has_tool_call, touching `parse_arguments, Glm4MoeDetector, __init__`; `python/sglang/srt/models/glm4_moe.py` modified +3/-3 (6 lines); hunks: -12,7 +12,7; -785,9 +785,9 @@ def determine_num_fused_shared_experts(; symbols: determine_num_fused_shared_experts, touching `determine_num_fused_shared_experts`; `python/sglang/srt/models/glm4_moe_nextn.py` modified +2/-2 (4 lines); hunks: -12,7 +12,7; -48,7 +48,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/function_call/glm4_moe_detector.py` modified +3/-3 (6 lines); hunks: -39,7 +39,7 @@ def parse_arguments(json_value):; -53,7 +53,7 @@ def __init__(self):; symbols: parse_arguments, Glm4MoeDetector, __init__, has_tool_call
  - `python/sglang/srt/models/glm4_moe.py` modified +3/-3 (6 lines); hunks: -12,7 +12,7; -785,9 +785,9 @@ def determine_num_fused_shared_experts(; symbols: determine_num_fused_shared_experts
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +2/-2 (4 lines); hunks: -12,7 +12,7; -48,7 +48,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/glm4_moe_detector.py` modified +3/-3; `python/sglang/srt/models/glm4_moe.py` modified +3/-3; `python/sglang/srt/models/glm4_moe_nextn.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11665 - fix(glm45): disable reduce scatter

- Link: https://github.com/sgl-project/sglang/pull/11665
- Status/date: merged / 2025-10-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `f7ab9554554f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(glm45): disable reduce scatter"; model line: GLM-4.5; category: bug fix; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "fix(glm45): disable reduce scatter"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -662,7 +662,7 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -662,7 +662,7 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4_moe.py
@@ -662,7 +662,7 @@ def __init__(
-            allow_reduce_scatter=True,
+            allow_reduce_scatter=False,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11800 - Refactoring GLM-4.5 and GLM-4.5V related implementations

- Link: https://github.com/sgl-project/sglang/pull/11800
- Status/date: merged / 2025-10-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; associated commits `4060ed37cb67`
- Diff scope read: GitHub Pull Request files API returned 4 files, +356/-565, 1370 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Refactoring GLM-4.5 and GLM-4.5V related implementations"; model line: GLM-4.5; category: model implementation change; main diff: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`; technical summary: Covers "Refactoring GLM-4.5 and GLM-4.5V related implementations"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +322/-354 (676 lines); hunks: -15,7 +15,7; -27,10 +27,16; symbols: __init__, forward, Glm4MoeSparseMoeBlock, touching `__init__, forward, Glm4MoeSparseMoeBlock`; `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-14 (18 lines); hunks: -12,7 +12,8; -33,7 +34,7; symbols: forward, Glm4MoeForCausalLMNextN, __init__, touching `forward, Glm4MoeForCausalLMNextN, __init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +322/-354 (676 lines); hunks: -15,7 +15,7; -27,10 +27,16; symbols: __init__, forward, Glm4MoeSparseMoeBlock
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-14 (18 lines); hunks: -12,7 +12,8; -33,7 +34,7; symbols: forward, Glm4MoeForCausalLMNextN, __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +322/-354; `python/sglang/srt/models/glm4_moe_nextn.py` modified +4/-14
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/models/glm4v_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22961 - [NPU] Fix issue and support GLM-4.5V

- Link: https://github.com/sgl-project/sglang/pull/22961
- Status/date: merged / 2026-04-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `9ffc0cc67ee5`
- Diff scope read: GitHub Pull Request files API returned 1 files, +17/-5, 36 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Fix issue and support GLM-4.5V"; model line: GLM-4.5; category: bug fix; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "[NPU] Fix issue and support GLM-4.5V"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +17/-5 (22 lines); hunks: -314,18 +314,30 @@ def forward_prepare(; symbols: forward_prepare, touching `forward_prepare`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +17/-5 (22 lines); hunks: -314,18 +314,30 @@ def forward_prepare(; symbols: forward_prepare
- Key code excerpts:

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

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +17/-5
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25524 - [Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP

- Link: https://github.com/sgl-project/sglang/pull/25524
- Status/date: merged / 2026-05-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe_nextn.py`; associated commits `2bcb6d2f8244`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-25, 79 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP"; model line: GLM-4.5; category: bug fix; main diff: `python/sglang/srt/models/glm4_moe_nextn.py`; technical summary: Covers "[Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP"; the main implementation surface is `python/sglang/srt/models/glm4_moe_nextn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe_nextn.py` modified +11/-25 (36 lines); hunks: -12,9 +12,8; -23,7 +22,6; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe_nextn.py` modified +11/-25 (36 lines); hunks: -12,9 +12,8; -23,7 +22,6; symbols: __init__, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe_nextn.py` modified +11/-25
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4_moe_nextn.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #40870 - [Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE

- Link: https://github.com/sgl-project/sglang/pull/40870
- Status/date: merged / 2026-09-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4_moe.py`; associated commits `e1048a215ce9`
- Diff scope read: GitHub Pull Request files API returned 5 files, +190/-74, 324 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE"; model line: GLM-4.5; category: model implementation change; main diff: `python/sglang/srt/models/glm4_moe.py`; technical summary: Covers "[Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE"; the main implementation surface is `python/sglang/srt/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4_moe.py` modified +3/-23 (26 lines); hunks: -83,7 +83,7; -964,29 +964,9 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/glm4_moe.py` modified +3/-23 (26 lines); hunks: -83,7 +83,7; -964,29 +964,9 @@ def forward(; symbols: forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4_moe.py` modified +3/-23
- Risk and verification: The diff ships test coverage in `test/registered/unit/layers/test_communicator_ffn_exit.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
