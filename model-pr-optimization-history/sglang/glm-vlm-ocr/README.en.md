# sglang GLM VLM/OCR Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/GLM/GLM-OCR.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/glm-ocr-deployment.jsx` | no direct PR-number commit |
| `python/sglang/srt/models/glm4v.py` | [#9884](https://github.com/sgl-project/sglang/pull/9884), [#10147](https://github.com/sgl-project/sglang/pull/10147), [#17582](https://github.com/sgl-project/sglang/pull/17582), [#20033](https://github.com/sgl-project/sglang/pull/20033), [#39088](https://github.com/sgl-project/sglang/pull/39088) |
| `python/sglang/srt/models/glm4v_moe.py` | [#20463](https://github.com/sgl-project/sglang/pull/20463), [#20740](https://github.com/sgl-project/sglang/pull/20740), [#21134](https://github.com/sgl-project/sglang/pull/21134) |
| `python/sglang/srt/models/glm_ocr.py` | [#17582](https://github.com/sgl-project/sglang/pull/17582), [#20463](https://github.com/sgl-project/sglang/pull/20463), [#20740](https://github.com/sgl-project/sglang/pull/20740), [#21134](https://github.com/sgl-project/sglang/pull/21134), [#37597](https://github.com/sgl-project/sglang/pull/37597) |
| `python/sglang/srt/models/glm_ocr_nextn.py` | [#17582](https://github.com/sgl-project/sglang/pull/17582), [#39088](https://github.com/sgl-project/sglang/pull/39088) |
| `python/sglang/srt/multimodal/processors/glm4v.py` | [#17582](https://github.com/sgl-project/sglang/pull/17582), [#18885](https://github.com/sgl-project/sglang/pull/18885), [#37971](https://github.com/sgl-project/sglang/pull/37971), [#43871](https://github.com/sgl-project/sglang/pull/43871) |
| `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` | [#37971](https://github.com/sgl-project/sglang/pull/37971), [#43871](https://github.com/sgl-project/sglang/pull/43871) |

## PR Coverage Summary

- Git-traced PRs: 12
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 12
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-09-05 | [#9884](https://github.com/sgl-project/sglang/pull/9884) | merged | [Bug Fix] Fix Glm4vVisionBlock norm | `python/sglang/srt/models/glm4v.py` |
| 2025-09-08 | [#10147](https://github.com/sgl-project/sglang/pull/10147) | merged | Fix: (glm4v) Add missing field | `python/sglang/srt/models/glm4v.py` |
| 2026-01-27 | [#17582](https://github.com/sgl-project/sglang/pull/17582) | merged | [GLM-OCR] Support GLM-OCR Model | `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py` |
| 2026-02-16 | [#18885](https://github.com/sgl-project/sglang/pull/18885) | merged | Fix GLM-4V processor registration when glm_ocr is unavailable | `python/sglang/srt/multimodal/processors/glm4v.py` |
| 2026-03-08 | [#20033](https://github.com/sgl-project/sglang/pull/20033) | merged | [VLM] Replace conv3d proj with linear for GLM4V | `python/sglang/srt/models/glm4v.py` |
| 2026-03-14 | [#20463](https://github.com/sgl-project/sglang/pull/20463) | merged | [Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr | `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py` |
| 2026-03-18 | [#20740](https://github.com/sgl-project/sglang/pull/20740) | merged | Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr" | `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py` |
| 2026-03-23 | [#21134](https://github.com/sgl-project/sglang/pull/21134) | merged | [Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix | `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py` |
| 2026-09-05 | [#37971](https://github.com/sgl-project/sglang/pull/37971) | merged | fix(glm4v): disambiguate mixed image video offsets | `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py` |
| 2026-09-19 | [#39088](https://github.com/sgl-project/sglang/pull/39088) | merged | Fix GLM-OCR MTP multimodal embeddings and positions | `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/models/glm4v.py` |
| 2026-10-18 | [#43871](https://github.com/sgl-project/sglang/pull/43871) | merged | [Fix] glm4v: Clamp request video budgets to the deployment limit | `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py` |
| 2026-11-05 | [#37597](https://github.com/sgl-project/sglang/pull/37597) | merged | [Feat] [CPU] glm_ocr: Add model support | `python/sglang/srt/models/glm_ocr.py` |

## Per-PR Diff Audit Cards

### PR #9884 - [Bug Fix] Fix Glm4vVisionBlock norm

- Link: https://github.com/sgl-project/sglang/pull/9884
- Status/date: merged / 2025-09-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v.py`; associated commits `0f6ac5e21db0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +4/-4, 27 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug Fix] Fix Glm4vVisionBlock norm"; model line: GLM VLM/OCR; category: bug fix; main diff: `python/sglang/srt/models/glm4v.py`; technical summary: Covers "[Bug Fix] Fix Glm4vVisionBlock norm"; the main implementation surface is `python/sglang/srt/models/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4v.py` modified +1/-2 (3 lines); hunks: -93,9 +93,8 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4v.py` modified +1/-2 (3 lines); hunks: -93,9 +93,8 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4v.py
@@ -93,9 +93,8 @@ def __init__(
+            rms_norm_eps=config.rms_norm_eps,
-        self.norm1 = Glm4vRMSNorm(config.hidden_size, eps=config.rms_norm_eps)
-        self.norm2 = Glm4vRMSNorm(config.hidden_size, eps=config.rms_norm_eps)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4v.py` modified +1/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/qwen2_5_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10147 - Fix: (glm4v) Add missing field

- Link: https://github.com/sgl-project/sglang/pull/10147
- Status/date: merged / 2025-09-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v.py`; associated commits `8116804e4f6e`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-0, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix: (glm4v) Add missing field"; model line: GLM VLM/OCR; category: bug fix; main diff: `python/sglang/srt/models/glm4v.py`; technical summary: Covers "Fix: (glm4v) Add missing field"; the main implementation surface is `python/sglang/srt/models/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4v.py` modified +3/-0 (3 lines); hunks: -497,6 +497,9 @@ def __init__(; symbols: __init__, get_image_feature, touching `__init__, get_image_feature`.
- Code diff details:
  - `python/sglang/srt/models/glm4v.py` modified +3/-0 (3 lines); hunks: -497,6 +497,9 @@ def __init__(; symbols: __init__, get_image_feature
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4v.py
@@ -497,6 +497,9 @@ def __init__(
+        # For EAGLE3 support
+        self.capture_aux_hidden_states = False
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4v.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4v.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17582 - [GLM-OCR] Support GLM-OCR Model

- Link: https://github.com/sgl-project/sglang/pull/17582
- Status/date: merged / 2026-01-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py`; associated commits `7106f6c8e150`
- Diff scope read: GitHub Pull Request files API returned 9 files, +679/-29, 851 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM-OCR] Support GLM-OCR Model"; model line: GLM VLM/OCR; category: model support/runtime entry; main diff: `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py`; technical summary: Covers "[GLM-OCR] Support GLM-OCR Model"; the main implementation surface is `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm_ocr.py` added +435/-0 (435 lines); hunks: -0,0 +1,435; symbols: GlmOcrRMSNorm, GlmOcrVisionMLP, GlmOcrVisionBlock, __init__, touching `GlmOcrRMSNorm, GlmOcrVisionMLP, GlmOcrVisionBlock`; `python/sglang/srt/models/glm_ocr_nextn.py` added +162/-0 (162 lines); hunks: -0,0 +1,162; symbols: GlmOcrModelNextN, __init__, forward, GlmOcrForConditionalGenerationNextN, touching `GlmOcrModelNextN, __init__, forward`; `python/sglang/srt/multimodal/processors/glm4v.py` modified +6/-1 (7 lines); hunks: -3,14 +3,19; symbols: Glm4vImageProcessor, __init__, touching `Glm4vImageProcessor, __init__`; `python/sglang/srt/models/glm4v.py` modified +0/-2 (2 lines); hunks: -758,8 +758,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/glm_ocr.py` added +435/-0 (435 lines); hunks: -0,0 +1,435; symbols: GlmOcrRMSNorm, GlmOcrVisionMLP, GlmOcrVisionBlock, __init__
  - `python/sglang/srt/models/glm_ocr_nextn.py` added +162/-0 (162 lines); hunks: -0,0 +1,162; symbols: GlmOcrModelNextN, __init__, forward, GlmOcrForConditionalGenerationNextN
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +6/-1 (7 lines); hunks: -3,14 +3,19; symbols: Glm4vImageProcessor, __init__
  - `python/sglang/srt/models/glm4v.py` modified +0/-2 (2 lines); hunks: -758,8 +758,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm_ocr.py
@@ -0,0 +1,435 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/glm_ocr_nextn.py
@@ -0,0 +1,162 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/multimodal/processors/glm4v.py
@@ -3,14 +3,19 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm_ocr.py` added +435/-0; `python/sglang/srt/models/glm_ocr_nextn.py` added +162/-0; `python/sglang/srt/multimodal/processors/glm4v.py` modified +6/-1; `python/sglang/srt/models/glm4v.py` modified +0/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/glm4.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18885 - Fix GLM-4V processor registration when glm_ocr is unavailable

- Link: https://github.com/sgl-project/sglang/pull/18885
- Status/date: merged / 2026-02-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/glm4v.py`; associated commits `206accd15de3`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-4, 33 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix GLM-4V processor registration when glm_ocr is unavailable"; model line: GLM VLM/OCR; category: bug fix; main diff: `python/sglang/srt/multimodal/processors/glm4v.py`; technical summary: Covers "Fix GLM-4V processor registration when glm_ocr is unavailable"; the main implementation surface is `python/sglang/srt/multimodal/processors/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/glm4v.py` modified +12/-4 (16 lines); hunks: -3,20 +3,28; symbols: Glm4vImageProcessor, __init__, touching `Glm4vImageProcessor, __init__`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +12/-4 (16 lines); hunks: -3,20 +3,28; symbols: Glm4vImageProcessor, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/glm4v.py
@@ -3,20 +3,28 @@
-from sglang.srt.models.glm_ocr import GlmOcrForConditionalGeneration
+try:
+    from sglang.srt.models.glm_ocr import GlmOcrForConditionalGeneration
+except ImportError:
+    GlmOcrForConditionalGeneration = None
-        Glm4vForConditionalGeneration,
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/glm4v.py` modified +12/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/glm4v.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20033 - [VLM] Replace conv3d proj with linear for GLM4V

- Link: https://github.com/sgl-project/sglang/pull/20033
- Status/date: merged / 2026-03-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v.py`; associated commits `97a2a9be0f45`
- Diff scope read: GitHub Pull Request files API returned 2 files, +192/-9, 228 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Replace conv3d proj with linear for GLM4V"; model line: GLM VLM/OCR; category: model implementation change; main diff: `python/sglang/srt/models/glm4v.py`; technical summary: Covers "[VLM] Replace conv3d proj with linear for GLM4V"; the main implementation surface is `python/sglang/srt/models/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4v.py` modified +26/-9 (35 lines); hunks: -211,16 +211,26 @@ def __init__(; -446,10 +456,16 @@ def __init__(; symbols: __init__, forward, copy_conv3d_weight_to_linear, Glm4vPatchMerger, touching `__init__, forward, copy_conv3d_weight_to_linear`.
- Code diff details:
  - `python/sglang/srt/models/glm4v.py` modified +26/-9 (35 lines); hunks: -211,16 +211,26 @@ def __init__(; -446,10 +456,16 @@ def __init__(; symbols: __init__, forward, copy_conv3d_weight_to_linear, Glm4vPatchMerger
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4v.py
@@ -211,16 +211,26 @@ def __init__(
-    def forward(self, x: torch.Tensor) -> torch.Tensor:
-        x = x.view(
-            -1,
-            self.in_channels,
-            self.temporal_patch_size,
-            self.patch_size,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4v.py` modified +26/-9
- Risk and verification: The diff ships test coverage in `test/registered/vlm/test_patch_embed_perf.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #20463 - [Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr

- Link: https://github.com/sgl-project/sglang/pull/20463
- Status/date: merged / 2026-03-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; associated commits `c330b687a116`
- Diff scope read: GitHub Pull Request files API returned 2 files, +6/-0, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr"; model line: GLM VLM/OCR; category: bug fix; main diff: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; technical summary: Covers "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr"; the main implementation surface is `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4v_moe.py` modified +3/-0 (3 lines); hunks: -281,5 +281,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`; `python/sglang/srt/models/glm_ocr.py` modified +3/-0 (3 lines); hunks: -431,5 +431,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/glm4v_moe.py` modified +3/-0 (3 lines); hunks: -281,5 +281,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
  - `python/sglang/srt/models/glm_ocr.py` modified +3/-0 (3 lines); hunks: -431,5 +431,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4v_moe.py
@@ -281,5 +281,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+        if not is_nextn:
+            self.visual.patch_embed.copy_conv3d_weight_to_linear()
diff -- python/sglang/srt/models/glm_ocr.py
@@ -431,5 +431,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+        if not is_nextn:
+            self.visual.patch_embed.copy_conv3d_weight_to_linear()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4v_moe.py` modified +3/-0; `python/sglang/srt/models/glm_ocr.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20740 - Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr"

- Link: https://github.com/sgl-project/sglang/pull/20740
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; associated commits `f15b3338c9f3`
- Diff scope read: GitHub Pull Request files API returned 2 files, +0/-6, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr""; model line: GLM VLM/OCR; category: bug fix; main diff: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; technical summary: Covers "Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr""; the main implementation surface is `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4v_moe.py` modified +0/-3 (3 lines); hunks: -281,8 +281,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`; `python/sglang/srt/models/glm_ocr.py` modified +0/-3 (3 lines); hunks: -431,8 +431,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/glm4v_moe.py` modified +0/-3 (3 lines); hunks: -281,8 +281,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
  - `python/sglang/srt/models/glm_ocr.py` modified +0/-3 (3 lines); hunks: -431,8 +431,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4v_moe.py
@@ -281,8 +281,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
-        if not is_nextn:
-            self.visual.patch_embed.copy_conv3d_weight_to_linear()
diff -- python/sglang/srt/models/glm_ocr.py
@@ -431,8 +431,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
-        if not is_nextn:
-            self.visual.patch_embed.copy_conv3d_weight_to_linear()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4v_moe.py` modified +0/-3; `python/sglang/srt/models/glm_ocr.py` modified +0/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21134 - [Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix

- Link: https://github.com/sgl-project/sglang/pull/21134
- Status/date: merged / 2026-03-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; associated commits `fcaad42b0038`
- Diff scope read: GitHub Pull Request files API returned 3 files, +16/-9, 74 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix"; model line: GLM VLM/OCR; category: bug fix; main diff: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; technical summary: Covers "[Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix"; the main implementation surface is `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm4v_moe.py` modified +7/-7 (14 lines); hunks: -158,6 +158,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -196,13 +203,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, touching `load_weights`; `python/sglang/srt/models/glm_ocr.py` modified +4/-1 (5 lines); hunks: -26,6 +26,7; -151,6 +152,7 @@ class GlmOcrVisionModel(Glm4vVisionModel):; symbols: GlmOcrVisionModel, __init__, touching `GlmOcrVisionModel, __init__`.
- Code diff details:
  - `python/sglang/srt/models/glm4v_moe.py` modified +7/-7 (14 lines); hunks: -158,6 +158,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -196,13 +203,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
  - `python/sglang/srt/models/glm_ocr.py` modified +4/-1 (5 lines); hunks: -26,6 +26,7; -151,6 +152,7 @@ class GlmOcrVisionModel(Glm4vVisionModel):; symbols: GlmOcrVisionModel, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm4v_moe.py
@@ -158,6 +158,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+            if "language_model." in name:
+                name = name.replace("language_model.", "")
+            if "model.visual." in name:
+                name = name.replace("model.visual.", "visual.")
+            if "rotary_emb.inv_freq" in name:
+                continue
diff -- python/sglang/srt/models/glm_ocr.py
@@ -26,6 +26,7 @@
+    GlmOcrTextConfig,
@@ -151,6 +152,7 @@ class GlmOcrVisionModel(Glm4vVisionModel):
+        text_config: GlmOcrTextConfig,
@@ -203,7 +205,7 @@ def __init__(
-            context_dim=vision_config.out_hidden_size * vision_config.in_channels,
+            context_dim=text_config.intermediate_size,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm4v_moe.py` modified +7/-7; `python/sglang/srt/models/glm_ocr.py` modified +4/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37971 - fix(glm4v): disambiguate mixed image video offsets

- Link: https://github.com/sgl-project/sglang/pull/37971
- Status/date: merged / 2026-09-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/glm4v.py`, `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`; associated commits `e980c1a2f133`
- Diff scope read: GitHub Pull Request files API returned 3 files, +153/-7, 194 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(glm4v): disambiguate mixed image video offsets"; model line: GLM VLM/OCR; category: bug fix; main diff: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`; technical summary: Covers "fix(glm4v): disambiguate mixed image video offsets"; the main implementation surface is `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` added +101/-0 (101 lines); hunks: -0,0 +1,101; symbols: _processor, test_glm4v_partitions_shared_image_and_video_token_offsets, test_glm4v_keeps_interleaved_media_offsets_in_their_modalities, test_glm4v_uses_default_offsets_when_token_ids_are_distinct, touching `_processor, test_glm4v_partitions_shared_image_and_video_token_offsets, test_glm4v_keeps_interleaved_media_offsets_in_their_modalities`; `python/sglang/srt/multimodal/processors/glm4v.py` modified +33/-2 (35 lines); hunks: -1,12 +1,12; -296,6 +296,37 @@ def __init__(self, hf_config, server_args, _processor, *arg...; symbols: __init__, get_mm_item_offsets, is_video_offset, compute_mrope_positions, touching `__init__, get_mm_item_offsets, is_video_offset`.
- Code diff details:
  - `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` added +101/-0 (101 lines); hunks: -0,0 +1,101; symbols: _processor, test_glm4v_partitions_shared_image_and_video_token_offsets, test_glm4v_keeps_interleaved_media_offsets_in_their_modalities, test_glm4v_uses_default_offsets_when_token_ids_are_distinct
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +33/-2 (35 lines); hunks: -1,12 +1,12; -296,6 +296,37 @@ def __init__(self, hf_config, server_args, _processor, *arg...; symbols: __init__, get_mm_item_offsets, is_video_offset, compute_mrope_positions
- Key code excerpts:

```diff
diff -- test/registered/unit/multimodal/test_glm4v_mixed_offsets.py
@@ -0,0 +1,101 @@
+import pytest
+import torch
+from sglang.srt.managers.schedule_batch import Modality
+from sglang.srt.multimodal.processors.base_processor import MultimodalSpecialTokens
+from sglang.srt.multimodal.processors.glm4v import Glm4vImageProcessor
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/multimodal/processors/glm4v.py
@@ -1,12 +1,12 @@
-from typing import List, Union
+from typing import List, Tuple, Union
-from sglang.srt.managers.schedule_batch import MultimodalProcessorOutput
+from sglang.srt.managers.schedule_batch import Modality, MultimodalProcessorOutput
@@ -296,6 +296,37 @@ def __init__(self, hf_config, server_args, _processor, *args, **kwargs):
+    def get_mm_item_offsets(
```

- Reviewed files:
  - tests: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` added +101/-0
  - runtime: `python/sglang/srt/multimodal/processors/glm4v.py` modified +33/-2
- Risk and verification: The diff ships test coverage in `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39088 - Fix GLM-OCR MTP multimodal embeddings and positions

- Link: https://github.com/sgl-project/sglang/pull/39088
- Status/date: merged / 2026-09-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/glm_ocr_nextn.py`; associated commits `929230a6f015`
- Diff scope read: GitHub Pull Request files API returned 17 files, +108/-6, 248 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix GLM-OCR MTP multimodal embeddings and positions"; model line: GLM VLM/OCR; category: bug fix; main diff: `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/models/glm4v.py`; technical summary: Covers "Fix GLM-OCR MTP multimodal embeddings and positions"; the main implementation surface is `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/models/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm_ocr_nextn.py` modified +19/-3 (22 lines); hunks: -36,6 +36,7; -86,9 +87,20 @@ def forward(; symbols: forward, __init__, touching `forward, __init__`; `python/sglang/srt/models/glm4v.py` modified +1/-1 (2 lines); hunks: -668,7 +668,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/glm_ocr_nextn.py` modified +19/-3 (22 lines); hunks: -36,6 +36,7; -86,9 +87,20 @@ def forward(; symbols: forward, __init__
  - `python/sglang/srt/models/glm4v.py` modified +1/-1 (2 lines); hunks: -668,7 +668,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm_ocr_nextn.py
@@ -36,6 +36,7 @@
+from sglang.srt.utils.hf_transformers_utils import get_rope_config
@@ -86,9 +87,20 @@ def forward(
-            hidden_states = self.embed_tokens(input_ids)
-        else:
-            hidden_states = input_embeds
+            input_embeds = forward_batch.mm_input_embeds
diff -- python/sglang/srt/models/glm4v.py
@@ -668,7 +668,7 @@ def forward(
-        if self.is_mrope_enabled:
+        if self.is_mrope_enabled and forward_batch.mrope_positions is not None:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm_ocr_nextn.py` modified +19/-3; `python/sglang/srt/models/glm4v.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsa_attention.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py`, `python/sglang/test/kits/attention_unittest/attention_methods/gdn_attention.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #43871 - [Fix] glm4v: Clamp request video budgets to the deployment limit

- Link: https://github.com/sgl-project/sglang/pull/43871
- Status/date: merged / 2026-10-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/glm4v.py`, `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`; associated commits `5a930cfd88b7`
- Diff scope read: GitHub Pull Request files API returned 5 files, +266/-14, 377 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] glm4v: Clamp request video budgets to the deployment limit"; model line: GLM VLM/OCR; category: bug fix; main diff: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`; technical summary: Covers "[Fix] glm4v: Clamp request video budgets to the deployment limit"; the main implementation surface is `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` modified +179/-1 (180 lines); hunks: -1,9 +1,19; -97,5 +107,173 @@ def test_glm4v_uses_default_offsets_when_token_ids_are_dist...; symbols: test_glm4v_uses_default_offsets_when_token_ids_are_distinct, _Glm5NextLikeVideoProcessor, _Glm4vLikeVideoProcessor, sample_frames, touching `test_glm4v_uses_default_offsets_when_token_ids_are_distinct, _Glm5NextLikeVideoProcessor, _Glm4vLikeVideoProcessor`; `python/sglang/srt/multimodal/processors/glm4v.py` modified +74/-5 (79 lines); hunks: -16,7 +16,7; -34,6 +34,7; symbols: _glm_video_metadata, glm_processor_video_config, _glm_effective_presize_budget, _glm_video_budget_ceiling, touching `_glm_video_metadata, glm_processor_video_config, _glm_effective_presize_budget`.
- Code diff details:
  - `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` modified +179/-1 (180 lines); hunks: -1,9 +1,19; -97,5 +107,173 @@ def test_glm4v_uses_default_offsets_when_token_ids_are_dist...; symbols: test_glm4v_uses_default_offsets_when_token_ids_are_distinct, _Glm5NextLikeVideoProcessor, _Glm4vLikeVideoProcessor, sample_frames
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +74/-5 (79 lines); hunks: -16,7 +16,7; -34,6 +34,7; symbols: _glm_video_metadata, glm_processor_video_config, _glm_effective_presize_budget, _glm_video_budget_ceiling
- Key code excerpts:

```diff
diff -- test/registered/unit/multimodal/test_glm4v_mixed_offsets.py
@@ -1,9 +1,19 @@
+import numpy as np
+from pydantic import ValidationError
+from sglang.srt.entrypoints.openai.protocol import ChatCompletionMessageContentVideoURL
+from sglang.srt.multimodal.processors import glm4v as glm4v_module
-from sglang.srt.multimodal.processors.glm4v import Glm4vImageProcessor
+from sglang.srt.multimodal.processors.glm4v import (
diff -- python/sglang/srt/multimodal/processors/glm4v.py
@@ -16,7 +16,7 @@
-from sglang.srt.utils import GLM_MEDIA_CONFIG_KEYS
+from sglang.srt.utils import GLM_MEDIA_CONFIG_KEYS, print_warning_once
@@ -34,6 +34,7 @@
+GLM_VIDEO_FRAME_PIXELS_PER_TOKEN = (GLM_VIDEO_PATCH_SIZE * GLM_VIDEO_MERGE_SIZE) ** 2
@@ -116,6 +117,8 @@ def glm_processor_video_config(processor):
+    if (max_duration := getattr(processor, "max_duration", None) or 0) > 0:
```

- Reviewed files:
  - tests: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` modified +179/-1
  - runtime: `python/sglang/srt/multimodal/processors/glm4v.py` modified +74/-5
- Risk and verification: The diff ships test coverage in `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37597 - [Feat] [CPU] glm_ocr: Add model support

- Link: https://github.com/sgl-project/sglang/pull/37597
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glm_ocr.py`; associated commits `3e9ce4394443`
- Diff scope read: GitHub Pull Request files API returned 7 files, +306/-252, 824 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] [CPU] glm_ocr: Add model support"; model line: GLM VLM/OCR; category: model support/runtime entry; main diff: `python/sglang/srt/models/glm_ocr.py`; technical summary: Covers "[Feat] [CPU] glm_ocr: Add model support"; the main implementation surface is `python/sglang/srt/models/glm_ocr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glm_ocr.py` modified +1/-0 (1 lines); hunks: -205,6 +205,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/glm_ocr.py` modified +1/-0 (1 lines); hunks: -205,6 +205,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glm_ocr.py
@@ -205,6 +205,7 @@ def __init__(
+                    num_dummy_heads=vision_config.num_dummy_heads,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glm_ocr.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `test/registered/cpu/test_conv3d_embed.py`, `test/registered/cpu/test_norm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
