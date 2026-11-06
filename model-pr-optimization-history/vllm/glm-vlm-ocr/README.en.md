# vllm GLM VLM/OCR Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/models/multimodal/processing/test_glm4_1v.py` | [#48729](https://github.com/vllm-project/vllm/pull/48729) |
| `vllm/model_executor/models/glm4_1v.py` | [#21678](https://github.com/vllm-project/vllm/pull/21678), [#22751](https://github.com/vllm-project/vllm/pull/22751), [#33005](https://github.com/vllm-project/vllm/pull/33005), [#34483](https://github.com/vllm-project/vllm/pull/34483), [#37962](https://github.com/vllm-project/vllm/pull/37962), [#47155](https://github.com/vllm-project/vllm/pull/47155), [#48729](https://github.com/vllm-project/vllm/pull/48729), [#55389](https://github.com/vllm-project/vllm/pull/55389) |
| `vllm/model_executor/models/glm4v.py` | no direct PR-number commit |
| `vllm/model_executor/models/glm_ocr.py` | [#33005](https://github.com/vllm-project/vllm/pull/33005), [#33350](https://github.com/vllm-project/vllm/pull/33350), [#37962](https://github.com/vllm-project/vllm/pull/37962), [#55389](https://github.com/vllm-project/vllm/pull/55389) |
| `vllm/model_executor/models/glm_ocr_mtp.py` | [#33005](https://github.com/vllm-project/vllm/pull/33005), [#56447](https://github.com/vllm-project/vllm/pull/56447), [#62234](https://github.com/vllm-project/vllm/pull/62234) |
| `vllm/transformers_utils/processors/glm4v.py` | no direct PR-number commit |

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
| 2026-11-04 | [#62234](https://github.com/vllm-project/vllm/pull/62234) | merged | [Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden. | `vllm/model_executor/models/glm_ocr_mtp.py` |
| 2026-09-30 | [#55389](https://github.com/vllm-project/vllm/pull/55389) | merged | [Model] Extend device-side mm normalization to GLM4V/GLM5Next | `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py` |
| 2026-09-11 | [#56447](https://github.com/vllm-project/vllm/pull/56447) | merged | [Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture | `vllm/model_executor/models/glm_ocr_mtp.py` |
| 2026-07-17 | [#48729](https://github.com/vllm-project/vllm/pull/48729) | merged | [Bugfix][GLM4V] Fix video dummy profiling and memory usage | `vllm/model_executor/models/glm4_1v.py`, `tests/models/multimodal/processing/test_glm4_1v.py` |
| 2026-07-03 | [#47155](https://github.com/vllm-project/vllm/pull/47155) | merged | [GLM4V] Avoid GLM4V processor init during startup metadata reads | `vllm/model_executor/models/glm4_1v.py` |
| 2026-03-26 | [#37962](https://github.com/vllm-project/vllm/pull/37962) | merged | [bug-fix] GLM OCR Patch Merger context_dim | `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm4_1v.py` |
| 2026-02-13 | [#34483](https://github.com/vllm-project/vllm/pull/34483) | merged | [Bugfix] Fix encoder cache underestimation for GLM-4V/GLM-OCR single image | `vllm/model_executor/models/glm4_1v.py` |
| 2026-01-29 | [#33350](https://github.com/vllm-project/vllm/pull/33350) | merged | [Bugfix] Fix broken GLM-OCR initialization | `vllm/model_executor/models/glm_ocr.py` |
| 2026-01-26 | [#33005](https://github.com/vllm-project/vllm/pull/33005) | merged | [GLM-OCR] GLM-OCR with MTP Support | `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm_ocr_mtp.py`, `vllm/model_executor/models/glm4_1v.py` |
| 2025-08-13 | [#22751](https://github.com/vllm-project/vllm/pull/22751) | merged | [Model] Decouple glm4v | `vllm/model_executor/models/glm4_1v.py` |
| 2025-07-28 | [#21678](https://github.com/vllm-project/vllm/pull/21678) | merged | Migrate Glm4vImageInputs, Glm4vVideoInputs to TensorSchema | `vllm/model_executor/models/glm4_1v.py` |

## Per-PR Diff Audit Cards

### PR #62234 - [Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.

- Link: https://github.com/vllm-project/vllm/pull/62234
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm_ocr_mtp.py`; associated commits `62966a7e00c4`
- Diff scope read: GitHub Pull Request files API returned 9 files, +166/-14, 282 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden."; model line: GLM VLM/OCR; category: bug fix; main diff: `vllm/model_executor/models/glm_ocr_mtp.py`; technical summary: Covers "[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden."; the main implementation surface is `vllm/model_executor/models/glm_ocr_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm_ocr_mtp.py` modified +6/-2 (8 lines); hunks: -99,8 +99,12 @@ def forward(; symbols: forward, GlmOcrMultiTokenPredictor, touching `forward, GlmOcrMultiTokenPredictor`.
- Code diff details:
  - `vllm/model_executor/models/glm_ocr_mtp.py` modified +6/-2 (8 lines); hunks: -99,8 +99,12 @@ def forward(; symbols: forward, GlmOcrMultiTokenPredictor
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm_ocr_mtp.py
@@ -99,8 +99,12 @@ def forward(
-        hidden_states = residual + hidden_states
-        return hidden_states
+        # Apply the final norm once (fused add+norm) and recycle the
+        # post-final-norm hidden into the next draft step; compute_logits uses
+        # it directly. Matches the GLM MTP recycle contract from #47448 and
+        # vllm/models/glm5next/common/mtp.py.
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm_ocr_mtp.py` modified +6/-2
- Risk and verification: The diff ships test coverage in `tests/v1/e2e/spec_decode/mtp/glm/__init__.py`, `tests/v1/e2e/spec_decode/mtp/glm/test_mtp.py`, `tests/v1/spec_decode/test_llm_base_proposer_sampling.py`, `tests/v1/spec_decode/test_mtp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55389 - [Model] Extend device-side mm normalization to GLM4V/GLM5Next

- Link: https://github.com/vllm-project/vllm/pull/55389
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`; associated commits `0a30bc3f9ac3`
- Diff scope read: GitHub Pull Request files API returned 7 files, +114/-10, 279 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Extend device-side mm normalization to GLM4V/GLM5Next"; model line: GLM VLM/OCR; category: model implementation change; main diff: `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`; technical summary: Covers "[Model] Extend device-side mm normalization to GLM4V/GLM5Next"; the main implementation surface is `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_1v.py` modified +16/-7 (23 lines); hunks: -61,6 +61,10; -616,6 +620,7 @@ def __init__(; symbols: __init__, forward, Glm4vForConditionalGeneration, get_placeholder_str, touching `__init__, forward, Glm4vForConditionalGeneration`; `vllm/model_executor/models/glm_ocr.py` modified +12/-2 (14 lines); hunks: -48,6 +48,7; -254,9 +255,17 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/glm4_1v.py` modified +16/-7 (23 lines); hunks: -61,6 +61,10; -616,6 +620,7 @@ def __init__(; symbols: __init__, forward, Glm4vForConditionalGeneration, get_placeholder_str
  - `vllm/model_executor/models/glm_ocr.py` modified +12/-2 (14 lines); hunks: -48,6 +48,7; -254,9 +255,17 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_1v.py
@@ -61,6 +61,10 @@
+from vllm.model_executor.layers.fusion.mm_input_norm import (
+    IdentityInputNorm,
+    build_mm_input_norm,
+)
@@ -616,6 +620,7 @@ def __init__(
+        input_norm: nn.Module | None = None,
diff -- vllm/model_executor/models/glm_ocr.py
@@ -48,6 +48,7 @@
+from vllm.model_executor.layers.fusion.mm_input_norm import build_mm_input_norm
@@ -254,9 +255,17 @@ def __init__(
+        input_norm: nn.Module | None = None,
-        super().__init__(text_config, vision_config, norm_eps, quant_config, prefix)
+        super().__init__(
+            text_config,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +16/-7; `vllm/model_executor/models/glm_ocr.py` modified +12/-2
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/generation_ppl_test/test_glm.py`, `tests/models/multimodal/processing/test_glm5next.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56447 - [Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture

- Link: https://github.com/vllm-project/vllm/pull/56447
- Status/date: merged / 2026-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm_ocr_mtp.py`; associated commits `89dbb2644552`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture"; model line: GLM VLM/OCR; category: bug fix; main diff: `vllm/model_executor/models/glm_ocr_mtp.py`; technical summary: Covers "[Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture"; the main implementation surface is `vllm/model_executor/models/glm_ocr_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm_ocr_mtp.py` modified +2/-1 (3 lines); hunks: -86,7 +86,8 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/glm_ocr_mtp.py` modified +2/-1 (3 lines); hunks: -86,7 +86,8 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm_ocr_mtp.py
@@ -86,7 +86,8 @@ def forward(
-        inputs_embeds[positions[0] == 0] = 0
+        token_positions = positions[0] if positions.ndim == 2 else positions
+        inputs_embeds.masked_fill_((token_positions == 0).unsqueeze(-1), 0)
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm_ocr_mtp.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm_ocr_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #48729 - [Bugfix][GLM4V] Fix video dummy profiling and memory usage

- Link: https://github.com/vllm-project/vllm/pull/48729
- Status/date: merged / 2026-07-17
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_glm4_1v.py`, `vllm/model_executor/models/glm4_1v.py`; associated commits `bf578e1abdff`
- Diff scope read: GitHub Pull Request files API returned 2 files, +72/-49, 212 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][GLM4V] Fix video dummy profiling and memory usage"; model line: GLM VLM/OCR; category: bug fix; main diff: `vllm/model_executor/models/glm4_1v.py`, `tests/models/multimodal/processing/test_glm4_1v.py`; technical summary: Covers "[Bugfix][GLM4V] Fix video dummy profiling and memory usage"; the main implementation surface is `vllm/model_executor/models/glm4_1v.py`, `tests/models/multimodal/processing/test_glm4_1v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_1v.py` modified +20/-49 (69 lines); hunks: -40,6 +40,7; -49,6 +50,7; symbols: get_video_processor, _get_processor_class_name, _get_image_max_pixels, _get_video_max_pixels, touching `get_video_processor, _get_processor_class_name, _get_image_max_pixels`; `tests/models/multimodal/processing/test_glm4_1v.py` modified +52/-0 (52 lines); hunks: -1,16 +1,68; symbols: test_get_max_video_frames_matches_glm_resize, test_encoder_cudagraph_uses_model_video_frame_limit, touching `test_get_max_video_frames_matches_glm_resize, test_encoder_cudagraph_uses_model_video_frame_limit`.
- Code diff details:
  - `vllm/model_executor/models/glm4_1v.py` modified +20/-49 (69 lines); hunks: -40,6 +40,7; -49,6 +50,7; symbols: get_video_processor, _get_processor_class_name, _get_image_max_pixels, _get_video_max_pixels
  - `tests/models/multimodal/processing/test_glm4_1v.py` modified +52/-0 (52 lines); hunks: -1,16 +1,68; symbols: test_get_max_video_frames_matches_glm_resize, test_encoder_cudagraph_uses_model_video_frame_limit
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_1v.py
@@ -40,6 +40,7 @@
+from transformers.image_processing_base import ImageProcessingMixin
@@ -49,6 +50,7 @@
+from transformers.video_processing_utils import BaseVideoProcessor
@@ -94,6 +96,8 @@
+from vllm.transformers_utils.processor import get_processor_cls_name_from_config
+from vllm.transformers_utils.utils import convert_model_repo_to_path
diff -- tests/models/multimodal/processing/test_glm4_1v.py
@@ -1,16 +1,68 @@
+from unittest.mock import Mock
+from vllm.model_executor.models.glm4_1v import (
+    Glm4vForConditionalGeneration,
+    Glm4vProcessingInfo,
+)
+@pytest.mark.parametrize(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +20/-49
  - tests: `tests/models/multimodal/processing/test_glm4_1v.py` modified +52/-0
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_glm4_1v.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #47155 - [GLM4V] Avoid GLM4V processor init during startup metadata reads

- Link: https://github.com/vllm-project/vllm/pull/47155
- Status/date: merged / 2026-07-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_1v.py`; associated commits `d6d39c111e60`
- Diff scope read: GitHub Pull Request files API returned 1 files, +67/-8, 113 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM4V] Avoid GLM4V processor init during startup metadata reads"; model line: GLM VLM/OCR; category: model implementation change; main diff: `vllm/model_executor/models/glm4_1v.py`; technical summary: Covers "[GLM4V] Avoid GLM4V processor init during startup metadata reads"; the main implementation surface is `vllm/model_executor/models/glm4_1v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_1v.py` modified +67/-8 (75 lines); hunks: -997,23 +997,50 @@ def get_image_processor(self, **kwargs: object) -> Glm4vIm...; -1092,7 +1119,40 @@ def _get_image_max_pixels(self) -> int:; symbols: get_image_processor, get_video_processor, _get_processor_class_name, _get_longest_edge, touching `get_image_processor, get_video_processor, _get_processor_class_name`.
- Code diff details:
  - `vllm/model_executor/models/glm4_1v.py` modified +67/-8 (75 lines); hunks: -997,23 +997,50 @@ def get_image_processor(self, **kwargs: object) -> Glm4vIm...; -1092,7 +1119,40 @@ def _get_image_max_pixels(self) -> int:; symbols: get_image_processor, get_video_processor, _get_processor_class_name, _get_longest_edge
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_1v.py
@@ -997,23 +997,50 @@ def get_image_processor(self, **kwargs: object) -> Glm4vImageProcessor:
+    def _get_processor_class_name(self) -> str | None:
+        from vllm.transformers_utils.processor import (
+            get_processor_cls_name_from_config,
+        )
+        from vllm.transformers_utils.utils import convert_model_repo_to_path
+        return get_processor_cls_name_from_config(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +67/-8
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_1v.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37962 - [bug-fix] GLM OCR Patch Merger context_dim

- Link: https://github.com/vllm-project/vllm/pull/37962
- Status/date: merged / 2026-03-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`; associated commits `757eafcf37ba`
- Diff scope read: GitHub Pull Request files API returned 2 files, +14/-4, 72 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[bug-fix] GLM OCR Patch Merger context_dim"; model line: GLM VLM/OCR; category: bug fix; main diff: `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm4_1v.py`; technical summary: Covers "[bug-fix] GLM OCR Patch Merger context_dim"; the main implementation surface is `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm4_1v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm_ocr.py` modified +8/-3 (11 lines); hunks: -35,7 +35,10; -250,12 +253,13 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__, touching `GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__`; `vllm/model_executor/models/glm4_1v.py` modified +6/-1 (7 lines); hunks: -38,7 +38,10; -604,6 +607,7 @@ def forward(; symbols: forward, Glm4vVisionTransformer, __init__, touching `forward, Glm4vVisionTransformer, __init__`.
- Code diff details:
  - `vllm/model_executor/models/glm_ocr.py` modified +8/-3 (11 lines); hunks: -35,7 +35,10; -250,12 +253,13 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__
  - `vllm/model_executor/models/glm4_1v.py` modified +6/-1 (7 lines); hunks: -38,7 +38,10; -604,6 +607,7 @@ def forward(; symbols: forward, Glm4vVisionTransformer, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm_ocr.py
@@ -35,7 +35,10 @@
-    from transformers.models.glm_ocr.configuration_glm_ocr import GlmOcrVisionConfig
+    from transformers.models.glm_ocr.configuration_glm_ocr import (
+        GlmOcrTextConfig,
+        GlmOcrVisionConfig,
+    )
@@ -250,12 +253,13 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):
diff -- vllm/model_executor/models/glm4_1v.py
@@ -38,7 +38,10 @@
-from transformers.models.glm4v.configuration_glm4v import Glm4vVisionConfig
+from transformers.models.glm4v.configuration_glm4v import (
+    Glm4vTextConfig,
+    Glm4vVisionConfig,
+)
@@ -604,6 +607,7 @@ def forward(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm_ocr.py` modified +8/-3; `vllm/model_executor/models/glm4_1v.py` modified +6/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34483 - [Bugfix] Fix encoder cache underestimation for GLM-4V/GLM-OCR single image

- Link: https://github.com/vllm-project/vllm/pull/34483
- Status/date: merged / 2026-02-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_1v.py`; associated commits `dcf6ee8592b4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +22/-2, 40 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix encoder cache underestimation for GLM-4V/GLM-OCR single image"; model line: GLM VLM/OCR; category: bug fix; main diff: `vllm/model_executor/models/glm4_1v.py`; technical summary: Covers "[Bugfix] Fix encoder cache underestimation for GLM-4V/GLM-OCR single image"; the main implementation surface is `vllm/model_executor/models/glm4_1v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_1v.py` modified +22/-2 (24 lines); hunks: -869,9 +869,28 @@ def _get_vision_info(; -884,7 +903,8 @@ def get_num_image_tokens(; symbols: _get_vision_info, _get_image_max_pixels, get_image_size_with_most_features, get_num_image_tokens, touching `_get_vision_info, _get_image_max_pixels, get_image_size_with_most_features`.
- Code diff details:
  - `vllm/model_executor/models/glm4_1v.py` modified +22/-2 (24 lines); hunks: -869,9 +869,28 @@ def _get_vision_info(; -884,7 +903,8 @@ def get_num_image_tokens(; symbols: _get_vision_info, _get_image_max_pixels, get_image_size_with_most_features, get_num_image_tokens
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_1v.py
@@ -869,9 +869,28 @@ def _get_vision_info(
+    def _get_image_max_pixels(self) -> int:
+        """Read max_pixels from the HF image processor config.
+        Despite the name, ``longest_edge`` is a pixel **area** (total pixel
+        count), not an edge length.  The HF processor passes it directly to
+        ``smart_resize`` as the ``max_pixels`` argument, which constrains
+        ``t_bar * h_bar * w_bar <= max_pixels``.
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +22/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_1v.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #33350 - [Bugfix] Fix broken GLM-OCR initialization

- Link: https://github.com/vllm-project/vllm/pull/33350
- Status/date: merged / 2026-01-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm_ocr.py`; associated commits `5e73e4900c80`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix broken GLM-OCR initialization"; model line: GLM VLM/OCR; category: bug fix; main diff: `vllm/model_executor/models/glm_ocr.py`; technical summary: Covers "[Bugfix] Fix broken GLM-OCR initialization"; the main implementation surface is `vllm/model_executor/models/glm_ocr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm_ocr.py` modified +1/-1 (2 lines); hunks: -249,7 +249,7 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__, touching `GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__`.
- Code diff details:
  - `vllm/model_executor/models/glm_ocr.py` modified +1/-1 (2 lines); hunks: -249,7 +249,7 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm_ocr.py
@@ -249,7 +249,7 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):
-        vision_config: GlmOcrVisionConfig,
+        vision_config: "GlmOcrVisionConfig",
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm_ocr.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm_ocr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #33005 - [GLM-OCR] GLM-OCR with MTP Support

- Link: https://github.com/vllm-project/vllm/pull/33005
- Status/date: merged / 2026-01-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm_ocr_mtp.py`; associated commits `bb17e8f11c38`
- Diff scope read: GitHub Pull Request files API returned 14 files, +873/-8, 1048 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM-OCR] GLM-OCR with MTP Support"; model line: GLM VLM/OCR; category: model support/runtime entry; main diff: `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm_ocr_mtp.py`, `vllm/model_executor/models/glm4_1v.py`; technical summary: Covers "[GLM-OCR] GLM-OCR with MTP Support"; the main implementation surface is `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm_ocr_mtp.py`, `vllm/model_executor/models/glm4_1v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm_ocr.py` added +389/-0 (389 lines); hunks: -0,0 +1,389; symbols: GlmOcrVisionMLP, GlmOcrVisionAttention, __init__, split_qkv, touching `GlmOcrVisionMLP, GlmOcrVisionAttention, __init__`; `vllm/model_executor/models/glm_ocr_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: GlmOcrMultiTokenPredictorLayer, __init__, forward, GlmOcrMultiTokenPredictor, touching `GlmOcrMultiTokenPredictorLayer, __init__, forward`; `vllm/model_executor/models/glm4_1v.py` modified +3/-2 (5 lines); hunks: -24,7 +24,8; -1418,7 +1419,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/glm_ocr.py` added +389/-0 (389 lines); hunks: -0,0 +1,389; symbols: GlmOcrVisionMLP, GlmOcrVisionAttention, __init__, split_qkv
  - `vllm/model_executor/models/glm_ocr_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: GlmOcrMultiTokenPredictorLayer, __init__, forward, GlmOcrMultiTokenPredictor
  - `vllm/model_executor/models/glm4_1v.py` modified +3/-2 (5 lines); hunks: -24,7 +24,8; -1418,7 +1419,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm_ocr.py
@@ -0,0 +1,389 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Adapted from
+# https://github.com/huggingface/transformers/blob/main/src/transformers/models/Glm4v/modeling_Glm4v.py
+# Copyright 2026 The ZhipuAI Team.
+# Copyright 2026 The vLLM team.
diff -- vllm/model_executor/models/glm_ocr_mtp.py
@@ -0,0 +1,285 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Copyright 2026 The ZhipuAI Team.
+# Copyright 2026 The vLLM team.
+# Copyright 2022 EleutherAI and the HuggingFace Inc. team. All rights reserved.
+#
diff -- vllm/model_executor/models/glm4_1v.py
@@ -24,7 +24,8 @@
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm_ocr.py` added +389/-0; `vllm/model_executor/models/glm_ocr_mtp.py` added +285/-0; `vllm/model_executor/models/glm4_1v.py` modified +3/-2
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/generation/test_common.py`, `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22751 - [Model] Decouple glm4v

- Link: https://github.com/vllm-project/vllm/pull/22751
- Status/date: merged / 2025-08-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_1v.py`; associated commits `fde0b611a37e`
- Diff scope read: GitHub Pull Request files API returned 3 files, +23/-7, 58 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Decouple glm4v"; model line: GLM VLM/OCR; category: model implementation change; main diff: `vllm/model_executor/models/glm4_1v.py`; technical summary: Covers "[Model] Decouple glm4v"; the main implementation surface is `vllm/model_executor/models/glm4_1v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_1v.py` modified +21/-5 (26 lines); hunks: -1227,10 +1227,7 @@ class Glm4vForConditionalGeneration(nn.Module, SupportsMu...; -1567,7 +1564,26 @@ def get_mm_mapping(self) -> MultiModelKeys:; symbols: Glm4vForConditionalGeneration, get_mm_mapping, Glm4vMoeForConditionalGeneration, touching `Glm4vForConditionalGeneration, get_mm_mapping, Glm4vMoeForConditionalGeneration`.
- Code diff details:
  - `vllm/model_executor/models/glm4_1v.py` modified +21/-5 (26 lines); hunks: -1227,10 +1227,7 @@ class Glm4vForConditionalGeneration(nn.Module, SupportsMu...; -1567,7 +1564,26 @@ def get_mm_mapping(self) -> MultiModelKeys:; symbols: Glm4vForConditionalGeneration, get_mm_mapping, Glm4vMoeForConditionalGeneration
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_1v.py
@@ -1227,10 +1227,7 @@ class Glm4vForConditionalGeneration(nn.Module, SupportsMultiModal,
-        "gate_up_proj": [
-            "gate_proj",
-            "up_proj",
-        ],
+        "gate_up_proj": ["gate_up_proj"]
@@ -1567,7 +1564,26 @@ def get_mm_mapping(self) -> MultiModelKeys:
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +21/-5
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/registry.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21678 - Migrate Glm4vImageInputs, Glm4vVideoInputs to TensorSchema

- Link: https://github.com/vllm-project/vllm/pull/21678
- Status/date: merged / 2025-07-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_1v.py`; associated commits `88e46c7c8dfa`
- Diff scope read: GitHub Pull Request files API returned 2 files, +69/-66, 218 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Migrate Glm4vImageInputs, Glm4vVideoInputs to TensorSchema"; model line: GLM VLM/OCR; category: model implementation change; main diff: `vllm/model_executor/models/glm4_1v.py`; technical summary: Covers "Migrate Glm4vImageInputs, Glm4vVideoInputs to TensorSchema"; the main implementation surface is `vllm/model_executor/models/glm4_1v.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_1v.py` modified +46/-65 (111 lines); hunks: -29,7 +29,7; -70,6 +70,7; symbols: Glm4vImagePixelInputs, Glm4vImageEmbeddingInputs, Glm4vVideoPixelInputs, touching `Glm4vImagePixelInputs, Glm4vImageEmbeddingInputs, Glm4vVideoPixelInputs`.
- Code diff details:
  - `vllm/model_executor/models/glm4_1v.py` modified +46/-65 (111 lines); hunks: -29,7 +29,7; -70,6 +70,7; symbols: Glm4vImagePixelInputs, Glm4vImageEmbeddingInputs, Glm4vVideoPixelInputs
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_1v.py
@@ -29,7 +29,7 @@
-from typing import Any, Callable, Literal, Optional, TypedDict, Union
+from typing import Annotated, Any, Callable, Literal, Optional, Union
@@ -70,6 +70,7 @@
+from vllm.utils.tensor_schema import TensorSchema, TensorShape
@@ -88,80 +89,68 @@
-class Glm4vImagePixelInputs(TypedDict):
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +46/-65
- Risk and verification: The diff ships test coverage in `tests/standalone_tests/test_tensor_schema.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
