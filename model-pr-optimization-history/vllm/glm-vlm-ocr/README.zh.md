# vllm GLM VLM/OCR 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/models/multimodal/processing/test_glm4_1v.py` | [#48729](https://github.com/vllm-project/vllm/pull/48729) |
| `vllm/model_executor/models/glm4_1v.py` | [#21678](https://github.com/vllm-project/vllm/pull/21678), [#22751](https://github.com/vllm-project/vllm/pull/22751), [#33005](https://github.com/vllm-project/vllm/pull/33005), [#34483](https://github.com/vllm-project/vllm/pull/34483), [#37962](https://github.com/vllm-project/vllm/pull/37962), [#47155](https://github.com/vllm-project/vllm/pull/47155), [#48729](https://github.com/vllm-project/vllm/pull/48729), [#55389](https://github.com/vllm-project/vllm/pull/55389) |
| `vllm/model_executor/models/glm4v.py` | 无直接 PR 号提交 |
| `vllm/model_executor/models/glm_ocr.py` | [#33005](https://github.com/vllm-project/vllm/pull/33005), [#33350](https://github.com/vllm-project/vllm/pull/33350), [#37962](https://github.com/vllm-project/vllm/pull/37962), [#55389](https://github.com/vllm-project/vllm/pull/55389) |
| `vllm/model_executor/models/glm_ocr_mtp.py` | [#33005](https://github.com/vllm-project/vllm/pull/33005), [#56447](https://github.com/vllm-project/vllm/pull/56447), [#62234](https://github.com/vllm-project/vllm/pull/62234) |
| `vllm/transformers_utils/processors/glm4v.py` | 无直接 PR 号提交 |

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

## 逐 PR diff 审计卡

### PR #62234 - [Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.

- 链接: https://github.com/vllm-project/vllm/pull/62234
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm_ocr_mtp.py`；关联提交 `62966a7e00c4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+166/-14，可读 patch 282 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm_ocr_mtp.py`；技术摘要: 覆盖「[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.」；主要实现面是 `vllm/model_executor/models/glm_ocr_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm_ocr_mtp.py` modified +6/-2 (8 lines); hunks: -99,8 +99,12 @@ def forward(; symbols: forward, GlmOcrMultiTokenPredictor，涉及 `forward, GlmOcrMultiTokenPredictor`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm_ocr_mtp.py` modified +6/-2 (8 lines); hunks: -99,8 +99,12 @@ def forward(; symbols: forward, GlmOcrMultiTokenPredictor
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm_ocr_mtp.py` modified +6/-2
- 验证与风险: diff 自带测试面 `tests/v1/e2e/spec_decode/mtp/glm/__init__.py`, `tests/v1/e2e/spec_decode/mtp/glm/test_mtp.py`, `tests/v1/spec_decode/test_llm_base_proposer_sampling.py`, `tests/v1/spec_decode/test_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55389 - [Model] Extend device-side mm normalization to GLM4V/GLM5Next

- 链接: https://github.com/vllm-project/vllm/pull/55389
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`；关联提交 `0a30bc3f9ac3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+114/-10，可读 patch 279 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Extend device-side mm normalization to GLM4V/GLM5Next」；模型线: GLM VLM/OCR；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`；技术摘要: 覆盖「[Model] Extend device-side mm normalization to GLM4V/GLM5Next」；主要实现面是 `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_1v.py` modified +16/-7 (23 lines); hunks: -61,6 +61,10; -616,6 +620,7 @@ def __init__(; symbols: __init__, forward, Glm4vForConditionalGeneration, get_placeholder_str，涉及 `__init__, forward, Glm4vForConditionalGeneration`；`vllm/model_executor/models/glm_ocr.py` modified +12/-2 (14 lines); hunks: -48,6 +48,7; -254,9 +255,17 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_1v.py` modified +16/-7 (23 lines); hunks: -61,6 +61,10; -616,6 +620,7 @@ def __init__(; symbols: __init__, forward, Glm4vForConditionalGeneration, get_placeholder_str
  - `vllm/model_executor/models/glm_ocr.py` modified +12/-2 (14 lines); hunks: -48,6 +48,7; -254,9 +255,17 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +16/-7; `vllm/model_executor/models/glm_ocr.py` modified +12/-2
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation_ppl_test/test_glm.py`, `tests/models/multimodal/processing/test_glm5next.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #56447 - [Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture

- 链接: https://github.com/vllm-project/vllm/pull/56447
- 状态/时间: merged / 2026-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm_ocr_mtp.py`；关联提交 `89dbb2644552`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm_ocr_mtp.py`；技术摘要: 覆盖「[Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture」；主要实现面是 `vllm/model_executor/models/glm_ocr_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm_ocr_mtp.py` modified +2/-1 (3 lines); hunks: -86,7 +86,8 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm_ocr_mtp.py` modified +2/-1 (3 lines); hunks: -86,7 +86,8 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm_ocr_mtp.py
@@ -86,7 +86,8 @@ def forward(
-        inputs_embeds[positions[0] == 0] = 0
+        token_positions = positions[0] if positions.ndim == 2 else positions
+        inputs_embeds.masked_fill_((token_positions == 0).unsqueeze(-1), 0)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm_ocr_mtp.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm_ocr_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #48729 - [Bugfix][GLM4V] Fix video dummy profiling and memory usage

- 链接: https://github.com/vllm-project/vllm/pull/48729
- 状态/时间: merged / 2026-07-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/processing/test_glm4_1v.py`, `vllm/model_executor/models/glm4_1v.py`；关联提交 `bf578e1abdff`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+72/-49，可读 patch 212 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][GLM4V] Fix video dummy profiling and memory usage」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_1v.py`, `tests/models/multimodal/processing/test_glm4_1v.py`；技术摘要: 覆盖「[Bugfix][GLM4V] Fix video dummy profiling and memory usage」；主要实现面是 `vllm/model_executor/models/glm4_1v.py`, `tests/models/multimodal/processing/test_glm4_1v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_1v.py` modified +20/-49 (69 lines); hunks: -40,6 +40,7; -49,6 +50,7; symbols: get_video_processor, _get_processor_class_name, _get_image_max_pixels, _get_video_max_pixels，涉及 `get_video_processor, _get_processor_class_name, _get_image_max_pixels`；`tests/models/multimodal/processing/test_glm4_1v.py` modified +52/-0 (52 lines); hunks: -1,16 +1,68; symbols: test_get_max_video_frames_matches_glm_resize, test_encoder_cudagraph_uses_model_video_frame_limit，涉及 `test_get_max_video_frames_matches_glm_resize, test_encoder_cudagraph_uses_model_video_frame_limit`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_1v.py` modified +20/-49 (69 lines); hunks: -40,6 +40,7; -49,6 +50,7; symbols: get_video_processor, _get_processor_class_name, _get_image_max_pixels, _get_video_max_pixels
  - `tests/models/multimodal/processing/test_glm4_1v.py` modified +52/-0 (52 lines); hunks: -1,16 +1,68; symbols: test_get_max_video_frames_matches_glm_resize, test_encoder_cudagraph_uses_model_video_frame_limit
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +20/-49
  - tests: `tests/models/multimodal/processing/test_glm4_1v.py` modified +52/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/processing/test_glm4_1v.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47155 - [GLM4V] Avoid GLM4V processor init during startup metadata reads

- 链接: https://github.com/vllm-project/vllm/pull/47155
- 状态/时间: merged / 2026-07-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_1v.py`；关联提交 `d6d39c111e60`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+67/-8，可读 patch 113 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM4V] Avoid GLM4V processor init during startup metadata reads」；模型线: GLM VLM/OCR；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_1v.py`；技术摘要: 覆盖「[GLM4V] Avoid GLM4V processor init during startup metadata reads」；主要实现面是 `vllm/model_executor/models/glm4_1v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_1v.py` modified +67/-8 (75 lines); hunks: -997,23 +997,50 @@ def get_image_processor(self, **kwargs: object) -> Glm4vIm...; -1092,7 +1119,40 @@ def _get_image_max_pixels(self) -> int:; symbols: get_image_processor, get_video_processor, _get_processor_class_name, _get_longest_edge，涉及 `get_image_processor, get_video_processor, _get_processor_class_name`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_1v.py` modified +67/-8 (75 lines); hunks: -997,23 +997,50 @@ def get_image_processor(self, **kwargs: object) -> Glm4vIm...; -1092,7 +1119,40 @@ def _get_image_max_pixels(self) -> int:; symbols: get_image_processor, get_video_processor, _get_processor_class_name, _get_longest_edge
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +67/-8
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_1v.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37962 - [bug-fix] GLM OCR Patch Merger context_dim

- 链接: https://github.com/vllm-project/vllm/pull/37962
- 状态/时间: merged / 2026-03-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`；关联提交 `757eafcf37ba`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+14/-4，可读 patch 72 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[bug-fix] GLM OCR Patch Merger context_dim」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm4_1v.py`；技术摘要: 覆盖「[bug-fix] GLM OCR Patch Merger context_dim」；主要实现面是 `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm4_1v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm_ocr.py` modified +8/-3 (11 lines); hunks: -35,7 +35,10; -250,12 +253,13 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__，涉及 `GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__`；`vllm/model_executor/models/glm4_1v.py` modified +6/-1 (7 lines); hunks: -38,7 +38,10; -604,6 +607,7 @@ def forward(; symbols: forward, Glm4vVisionTransformer, __init__，涉及 `forward, Glm4vVisionTransformer, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm_ocr.py` modified +8/-3 (11 lines); hunks: -35,7 +35,10; -250,12 +253,13 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__
  - `vllm/model_executor/models/glm4_1v.py` modified +6/-1 (7 lines); hunks: -38,7 +38,10; -604,6 +607,7 @@ def forward(; symbols: forward, Glm4vVisionTransformer, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm_ocr.py` modified +8/-3; `vllm/model_executor/models/glm4_1v.py` modified +6/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34483 - [Bugfix] Fix encoder cache underestimation for GLM-4V/GLM-OCR single image

- 链接: https://github.com/vllm-project/vllm/pull/34483
- 状态/时间: merged / 2026-02-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_1v.py`；关联提交 `dcf6ee8592b4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+22/-2，可读 patch 40 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix encoder cache underestimation for GLM-4V/GLM-OCR single image」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_1v.py`；技术摘要: 覆盖「[Bugfix] Fix encoder cache underestimation for GLM-4V/GLM-OCR single image」；主要实现面是 `vllm/model_executor/models/glm4_1v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_1v.py` modified +22/-2 (24 lines); hunks: -869,9 +869,28 @@ def _get_vision_info(; -884,7 +903,8 @@ def get_num_image_tokens(; symbols: _get_vision_info, _get_image_max_pixels, get_image_size_with_most_features, get_num_image_tokens，涉及 `_get_vision_info, _get_image_max_pixels, get_image_size_with_most_features`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_1v.py` modified +22/-2 (24 lines); hunks: -869,9 +869,28 @@ def _get_vision_info(; -884,7 +903,8 @@ def get_num_image_tokens(; symbols: _get_vision_info, _get_image_max_pixels, get_image_size_with_most_features, get_num_image_tokens
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +22/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_1v.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33350 - [Bugfix] Fix broken GLM-OCR initialization

- 链接: https://github.com/vllm-project/vllm/pull/33350
- 状态/时间: merged / 2026-01-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm_ocr.py`；关联提交 `5e73e4900c80`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix broken GLM-OCR initialization」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm_ocr.py`；技术摘要: 覆盖「[Bugfix] Fix broken GLM-OCR initialization」；主要实现面是 `vllm/model_executor/models/glm_ocr.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm_ocr.py` modified +1/-1 (2 lines); hunks: -249,7 +249,7 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__，涉及 `GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm_ocr.py` modified +1/-1 (2 lines); hunks: -249,7 +249,7 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):; symbols: GlmOcrPatchMerger, GlmOcrVisionTransformer, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm_ocr.py
@@ -249,7 +249,7 @@ class GlmOcrPatchMerger(Glm4vPatchMerger):
-        vision_config: GlmOcrVisionConfig,
+        vision_config: "GlmOcrVisionConfig",
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm_ocr.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm_ocr.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33005 - [GLM-OCR] GLM-OCR with MTP Support

- 链接: https://github.com/vllm-project/vllm/pull/33005
- 状态/时间: merged / 2026-01-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm_ocr_mtp.py`；关联提交 `bb17e8f11c38`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+873/-8，可读 patch 1048 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-OCR] GLM-OCR with MTP Support」；模型线: GLM VLM/OCR；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm_ocr_mtp.py`, `vllm/model_executor/models/glm4_1v.py`；技术摘要: 覆盖「[GLM-OCR] GLM-OCR with MTP Support」；主要实现面是 `vllm/model_executor/models/glm_ocr.py`, `vllm/model_executor/models/glm_ocr_mtp.py`, `vllm/model_executor/models/glm4_1v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm_ocr.py` added +389/-0 (389 lines); hunks: -0,0 +1,389; symbols: GlmOcrVisionMLP, GlmOcrVisionAttention, __init__, split_qkv，涉及 `GlmOcrVisionMLP, GlmOcrVisionAttention, __init__`；`vllm/model_executor/models/glm_ocr_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: GlmOcrMultiTokenPredictorLayer, __init__, forward, GlmOcrMultiTokenPredictor，涉及 `GlmOcrMultiTokenPredictorLayer, __init__, forward`；`vllm/model_executor/models/glm4_1v.py` modified +3/-2 (5 lines); hunks: -24,7 +24,8; -1418,7 +1419,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm_ocr.py` added +389/-0 (389 lines); hunks: -0,0 +1,389; symbols: GlmOcrVisionMLP, GlmOcrVisionAttention, __init__, split_qkv
  - `vllm/model_executor/models/glm_ocr_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: GlmOcrMultiTokenPredictorLayer, __init__, forward, GlmOcrMultiTokenPredictor
  - `vllm/model_executor/models/glm4_1v.py` modified +3/-2 (5 lines); hunks: -24,7 +24,8; -1418,7 +1419,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm_ocr.py` added +389/-0; `vllm/model_executor/models/glm_ocr_mtp.py` added +285/-0; `vllm/model_executor/models/glm4_1v.py` modified +3/-2
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation/test_common.py`, `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22751 - [Model] Decouple glm4v

- 链接: https://github.com/vllm-project/vllm/pull/22751
- 状态/时间: merged / 2025-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_1v.py`；关联提交 `fde0b611a37e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+23/-7，可读 patch 58 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Decouple glm4v」；模型线: GLM VLM/OCR；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_1v.py`；技术摘要: 覆盖「[Model] Decouple glm4v」；主要实现面是 `vllm/model_executor/models/glm4_1v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_1v.py` modified +21/-5 (26 lines); hunks: -1227,10 +1227,7 @@ class Glm4vForConditionalGeneration(nn.Module, SupportsMu...; -1567,7 +1564,26 @@ def get_mm_mapping(self) -> MultiModelKeys:; symbols: Glm4vForConditionalGeneration, get_mm_mapping, Glm4vMoeForConditionalGeneration，涉及 `Glm4vForConditionalGeneration, get_mm_mapping, Glm4vMoeForConditionalGeneration`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_1v.py` modified +21/-5 (26 lines); hunks: -1227,10 +1227,7 @@ class Glm4vForConditionalGeneration(nn.Module, SupportsMu...; -1567,7 +1564,26 @@ def get_mm_mapping(self) -> MultiModelKeys:; symbols: Glm4vForConditionalGeneration, get_mm_mapping, Glm4vMoeForConditionalGeneration
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +21/-5
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/registry.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21678 - Migrate Glm4vImageInputs, Glm4vVideoInputs to TensorSchema

- 链接: https://github.com/vllm-project/vllm/pull/21678
- 状态/时间: merged / 2025-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_1v.py`；关联提交 `88e46c7c8dfa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+69/-66，可读 patch 218 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Migrate Glm4vImageInputs, Glm4vVideoInputs to TensorSchema」；模型线: GLM VLM/OCR；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_1v.py`；技术摘要: 覆盖「Migrate Glm4vImageInputs, Glm4vVideoInputs to TensorSchema」；主要实现面是 `vllm/model_executor/models/glm4_1v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_1v.py` modified +46/-65 (111 lines); hunks: -29,7 +29,7; -70,6 +70,7; symbols: Glm4vImagePixelInputs, Glm4vImageEmbeddingInputs, Glm4vVideoPixelInputs，涉及 `Glm4vImagePixelInputs, Glm4vImageEmbeddingInputs, Glm4vVideoPixelInputs`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_1v.py` modified +46/-65 (111 lines); hunks: -29,7 +29,7; -70,6 +70,7; symbols: Glm4vImagePixelInputs, Glm4vImageEmbeddingInputs, Glm4vVideoPixelInputs
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_1v.py` modified +46/-65
- 验证与风险: diff 自带测试面 `tests/standalone_tests/test_tensor_schema.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
