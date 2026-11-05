# sglang GLM VLM/OCR 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/GLM/GLM-OCR.mdx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/glm-ocr-deployment.jsx` | 无直接 PR 号提交 |
| `python/sglang/srt/models/glm4v.py` | [#9884](https://github.com/sgl-project/sglang/pull/9884), [#10147](https://github.com/sgl-project/sglang/pull/10147), [#17582](https://github.com/sgl-project/sglang/pull/17582), [#20033](https://github.com/sgl-project/sglang/pull/20033), [#39088](https://github.com/sgl-project/sglang/pull/39088) |
| `python/sglang/srt/models/glm4v_moe.py` | [#20463](https://github.com/sgl-project/sglang/pull/20463), [#20740](https://github.com/sgl-project/sglang/pull/20740), [#21134](https://github.com/sgl-project/sglang/pull/21134) |
| `python/sglang/srt/models/glm_ocr.py` | [#17582](https://github.com/sgl-project/sglang/pull/17582), [#20463](https://github.com/sgl-project/sglang/pull/20463), [#20740](https://github.com/sgl-project/sglang/pull/20740), [#21134](https://github.com/sgl-project/sglang/pull/21134), [#37597](https://github.com/sgl-project/sglang/pull/37597) |
| `python/sglang/srt/models/glm_ocr_nextn.py` | [#17582](https://github.com/sgl-project/sglang/pull/17582), [#39088](https://github.com/sgl-project/sglang/pull/39088) |
| `python/sglang/srt/multimodal/processors/glm4v.py` | [#17582](https://github.com/sgl-project/sglang/pull/17582), [#18885](https://github.com/sgl-project/sglang/pull/18885), [#37971](https://github.com/sgl-project/sglang/pull/37971), [#43871](https://github.com/sgl-project/sglang/pull/43871) |
| `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` | [#37971](https://github.com/sgl-project/sglang/pull/37971), [#43871](https://github.com/sgl-project/sglang/pull/43871) |

## PR 覆盖总览

- git 追溯 PR 数: 12
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 12
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #9884 - [Bug Fix] Fix Glm4vVisionBlock norm

- 链接: https://github.com/sgl-project/sglang/pull/9884
- 状态/时间: merged / 2025-09-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v.py`；关联提交 `0f6ac5e21db0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-4，可读 patch 27 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug Fix] Fix Glm4vVisionBlock norm」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4v.py`；技术摘要: 覆盖「[Bug Fix] Fix Glm4vVisionBlock norm」；主要实现面是 `python/sglang/srt/models/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4v.py` modified +1/-2 (3 lines); hunks: -93,9 +93,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4v.py` modified +1/-2 (3 lines); hunks: -93,9 +93,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4v.py
@@ -93,9 +93,8 @@ def __init__(
+            rms_norm_eps=config.rms_norm_eps,
-        self.norm1 = Glm4vRMSNorm(config.hidden_size, eps=config.rms_norm_eps)
-        self.norm2 = Glm4vRMSNorm(config.hidden_size, eps=config.rms_norm_eps)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4v.py` modified +1/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/qwen2_5_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10147 - Fix: (glm4v) Add missing field

- 链接: https://github.com/sgl-project/sglang/pull/10147
- 状态/时间: merged / 2025-09-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v.py`；关联提交 `8116804e4f6e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-0，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix: (glm4v) Add missing field」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4v.py`；技术摘要: 覆盖「Fix: (glm4v) Add missing field」；主要实现面是 `python/sglang/srt/models/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4v.py` modified +3/-0 (3 lines); hunks: -497,6 +497,9 @@ def __init__(; symbols: __init__, get_image_feature，涉及 `__init__, get_image_feature`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4v.py` modified +3/-0 (3 lines); hunks: -497,6 +497,9 @@ def __init__(; symbols: __init__, get_image_feature
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm4v.py
@@ -497,6 +497,9 @@ def __init__(
+        # For EAGLE3 support
+        self.capture_aux_hidden_states = False
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4v.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4v.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17582 - [GLM-OCR] Support GLM-OCR Model

- 链接: https://github.com/sgl-project/sglang/pull/17582
- 状态/时间: merged / 2026-01-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py`；关联提交 `7106f6c8e150`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+679/-29，可读 patch 851 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-OCR] Support GLM-OCR Model」；模型线: GLM VLM/OCR；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py`；技术摘要: 覆盖「[GLM-OCR] Support GLM-OCR Model」；主要实现面是 `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm_ocr.py` added +435/-0 (435 lines); hunks: -0,0 +1,435; symbols: GlmOcrRMSNorm, GlmOcrVisionMLP, GlmOcrVisionBlock, __init__，涉及 `GlmOcrRMSNorm, GlmOcrVisionMLP, GlmOcrVisionBlock`；`python/sglang/srt/models/glm_ocr_nextn.py` added +162/-0 (162 lines); hunks: -0,0 +1,162; symbols: GlmOcrModelNextN, __init__, forward, GlmOcrForConditionalGenerationNextN，涉及 `GlmOcrModelNextN, __init__, forward`；`python/sglang/srt/multimodal/processors/glm4v.py` modified +6/-1 (7 lines); hunks: -3,14 +3,19; symbols: Glm4vImageProcessor, __init__，涉及 `Glm4vImageProcessor, __init__`；`python/sglang/srt/models/glm4v.py` modified +0/-2 (2 lines); hunks: -758,8 +758,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm_ocr.py` added +435/-0 (435 lines); hunks: -0,0 +1,435; symbols: GlmOcrRMSNorm, GlmOcrVisionMLP, GlmOcrVisionBlock, __init__
  - `python/sglang/srt/models/glm_ocr_nextn.py` added +162/-0 (162 lines); hunks: -0,0 +1,162; symbols: GlmOcrModelNextN, __init__, forward, GlmOcrForConditionalGenerationNextN
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +6/-1 (7 lines); hunks: -3,14 +3,19; symbols: Glm4vImageProcessor, __init__
  - `python/sglang/srt/models/glm4v.py` modified +0/-2 (2 lines); hunks: -758,8 +758,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm_ocr.py` added +435/-0; `python/sglang/srt/models/glm_ocr_nextn.py` added +162/-0; `python/sglang/srt/multimodal/processors/glm4v.py` modified +6/-1; `python/sglang/srt/models/glm4v.py` modified +0/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/glm4.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18885 - Fix GLM-4V processor registration when glm_ocr is unavailable

- 链接: https://github.com/sgl-project/sglang/pull/18885
- 状态/时间: merged / 2026-02-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/multimodal/processors/glm4v.py`；关联提交 `206accd15de3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-4，可读 patch 33 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix GLM-4V processor registration when glm_ocr is unavailable」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `python/sglang/srt/multimodal/processors/glm4v.py`；技术摘要: 覆盖「Fix GLM-4V processor registration when glm_ocr is unavailable」；主要实现面是 `python/sglang/srt/multimodal/processors/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/multimodal/processors/glm4v.py` modified +12/-4 (16 lines); hunks: -3,20 +3,28; symbols: Glm4vImageProcessor, __init__，涉及 `Glm4vImageProcessor, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +12/-4 (16 lines); hunks: -3,20 +3,28; symbols: Glm4vImageProcessor, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/multimodal/processors/glm4v.py` modified +12/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/multimodal/processors/glm4v.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20033 - [VLM] Replace conv3d proj with linear for GLM4V

- 链接: https://github.com/sgl-project/sglang/pull/20033
- 状态/时间: merged / 2026-03-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v.py`；关联提交 `97a2a9be0f45`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+192/-9，可读 patch 228 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[VLM] Replace conv3d proj with linear for GLM4V」；模型线: GLM VLM/OCR；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/glm4v.py`；技术摘要: 覆盖「[VLM] Replace conv3d proj with linear for GLM4V」；主要实现面是 `python/sglang/srt/models/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4v.py` modified +26/-9 (35 lines); hunks: -211,16 +211,26 @@ def __init__(; -446,10 +456,16 @@ def __init__(; symbols: __init__, forward, copy_conv3d_weight_to_linear, Glm4vPatchMerger，涉及 `__init__, forward, copy_conv3d_weight_to_linear`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4v.py` modified +26/-9 (35 lines); hunks: -211,16 +211,26 @@ def __init__(; -446,10 +456,16 @@ def __init__(; symbols: __init__, forward, copy_conv3d_weight_to_linear, Glm4vPatchMerger
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4v.py` modified +26/-9
- 验证与风险: diff 自带测试面 `test/registered/vlm/test_patch_embed_perf.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #20463 - [Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr

- 链接: https://github.com/sgl-project/sglang/pull/20463
- 状态/时间: merged / 2026-03-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；关联提交 `c330b687a116`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+6/-0，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；技术摘要: 覆盖「[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr」；主要实现面是 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4v_moe.py` modified +3/-0 (3 lines); hunks: -281,5 +281,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`；`python/sglang/srt/models/glm_ocr.py` modified +3/-0 (3 lines); hunks: -431,5 +431,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4v_moe.py` modified +3/-0 (3 lines); hunks: -281,5 +281,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
  - `python/sglang/srt/models/glm_ocr.py` modified +3/-0 (3 lines); hunks: -431,5 +431,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4v_moe.py` modified +3/-0; `python/sglang/srt/models/glm_ocr.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20740 - Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr"

- 链接: https://github.com/sgl-project/sglang/pull/20740
- 状态/时间: merged / 2026-03-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；关联提交 `f15b3338c9f3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+0/-6，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr"」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；技术摘要: 覆盖「Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr"」；主要实现面是 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4v_moe.py` modified +0/-3 (3 lines); hunks: -281,8 +281,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`；`python/sglang/srt/models/glm_ocr.py` modified +0/-3 (3 lines); hunks: -431,8 +431,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4v_moe.py` modified +0/-3 (3 lines); hunks: -281,8 +281,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
  - `python/sglang/srt/models/glm_ocr.py` modified +0/-3 (3 lines); hunks: -431,8 +431,5 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4v_moe.py` modified +0/-3; `python/sglang/srt/models/glm_ocr.py` modified +0/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21134 - [Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix

- 链接: https://github.com/sgl-project/sglang/pull/21134
- 状态/时间: merged / 2026-03-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；关联提交 `fcaad42b0038`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+16/-9，可读 patch 74 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；技术摘要: 覆盖「[Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix」；主要实现面是 `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm4v_moe.py` modified +7/-7 (14 lines); hunks: -158,6 +158,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -196,13 +203,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`；`python/sglang/srt/models/glm_ocr.py` modified +4/-1 (5 lines); hunks: -26,6 +26,7; -151,6 +152,7 @@ class GlmOcrVisionModel(Glm4vVisionModel):; symbols: GlmOcrVisionModel, __init__，涉及 `GlmOcrVisionModel, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm4v_moe.py` modified +7/-7 (14 lines); hunks: -158,6 +158,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -196,13 +203,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
  - `python/sglang/srt/models/glm_ocr.py` modified +4/-1 (5 lines); hunks: -26,6 +26,7; -151,6 +152,7 @@ class GlmOcrVisionModel(Glm4vVisionModel):; symbols: GlmOcrVisionModel, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm4v_moe.py` modified +7/-7; `python/sglang/srt/models/glm_ocr.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37971 - fix(glm4v): disambiguate mixed image video offsets

- 链接: https://github.com/sgl-project/sglang/pull/37971
- 状态/时间: merged / 2026-09-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/multimodal/processors/glm4v.py`, `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`；关联提交 `e980c1a2f133`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+153/-7，可读 patch 194 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(glm4v): disambiguate mixed image video offsets」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`；技术摘要: 覆盖「fix(glm4v): disambiguate mixed image video offsets」；主要实现面是 `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` added +101/-0 (101 lines); hunks: -0,0 +1,101; symbols: _processor, test_glm4v_partitions_shared_image_and_video_token_offsets, test_glm4v_keeps_interleaved_media_offsets_in_their_modalities, test_glm4v_uses_default_offsets_when_token_ids_are_distinct，涉及 `_processor, test_glm4v_partitions_shared_image_and_video_token_offsets, test_glm4v_keeps_interleaved_media_offsets_in_their_modalities`；`python/sglang/srt/multimodal/processors/glm4v.py` modified +33/-2 (35 lines); hunks: -1,12 +1,12; -296,6 +296,37 @@ def __init__(self, hf_config, server_args, _processor, *arg...; symbols: __init__, get_mm_item_offsets, is_video_offset, compute_mrope_positions，涉及 `__init__, get_mm_item_offsets, is_video_offset`。
- 代码 diff 细节:
  - `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` added +101/-0 (101 lines); hunks: -0,0 +1,101; symbols: _processor, test_glm4v_partitions_shared_image_and_video_token_offsets, test_glm4v_keeps_interleaved_media_offsets_in_their_modalities, test_glm4v_uses_default_offsets_when_token_ids_are_distinct
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +33/-2 (35 lines); hunks: -1,12 +1,12; -296,6 +296,37 @@ def __init__(self, hf_config, server_args, _processor, *arg...; symbols: __init__, get_mm_item_offsets, is_video_offset, compute_mrope_positions
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` added +101/-0
  - runtime: `python/sglang/srt/multimodal/processors/glm4v.py` modified +33/-2
- 验证与风险: diff 自带测试面 `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39088 - Fix GLM-OCR MTP multimodal embeddings and positions

- 链接: https://github.com/sgl-project/sglang/pull/39088
- 状态/时间: merged / 2026-09-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/glm_ocr_nextn.py`；关联提交 `929230a6f015`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 17 个文件，+108/-6，可读 patch 248 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix GLM-OCR MTP multimodal embeddings and positions」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/models/glm4v.py`；技术摘要: 覆盖「Fix GLM-OCR MTP multimodal embeddings and positions」；主要实现面是 `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/models/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm_ocr_nextn.py` modified +19/-3 (22 lines); hunks: -36,6 +36,7; -86,9 +87,20 @@ def forward(; symbols: forward, __init__，涉及 `forward, __init__`；`python/sglang/srt/models/glm4v.py` modified +1/-1 (2 lines); hunks: -668,7 +668,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm_ocr_nextn.py` modified +19/-3 (22 lines); hunks: -36,6 +36,7; -86,9 +87,20 @@ def forward(; symbols: forward, __init__
  - `python/sglang/srt/models/glm4v.py` modified +1/-1 (2 lines); hunks: -668,7 +668,7 @@ def forward(; symbols: forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/glm_ocr_nextn.py` modified +19/-3; `python/sglang/srt/models/glm4v.py` modified +1/-1
- 验证与风险: diff 自带测试面 `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsa_attention.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py`, `python/sglang/test/kits/attention_unittest/attention_methods/gdn_attention.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43871 - [Fix] glm4v: Clamp request video budgets to the deployment limit

- 链接: https://github.com/sgl-project/sglang/pull/43871
- 状态/时间: merged / 2026-10-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/multimodal/processors/glm4v.py`, `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`；关联提交 `5a930cfd88b7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+266/-14，可读 patch 377 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] glm4v: Clamp request video budgets to the deployment limit」；模型线: GLM VLM/OCR；类别: 缺陷修复；主要 diff: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`；技术摘要: 覆盖「[Fix] glm4v: Clamp request video budgets to the deployment limit」；主要实现面是 `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`, `python/sglang/srt/multimodal/processors/glm4v.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` modified +179/-1 (180 lines); hunks: -1,9 +1,19; -97,5 +107,173 @@ def test_glm4v_uses_default_offsets_when_token_ids_are_dist...; symbols: test_glm4v_uses_default_offsets_when_token_ids_are_distinct, _Glm5NextLikeVideoProcessor, _Glm4vLikeVideoProcessor, sample_frames，涉及 `test_glm4v_uses_default_offsets_when_token_ids_are_distinct, _Glm5NextLikeVideoProcessor, _Glm4vLikeVideoProcessor`；`python/sglang/srt/multimodal/processors/glm4v.py` modified +74/-5 (79 lines); hunks: -16,7 +16,7; -34,6 +34,7; symbols: _glm_video_metadata, glm_processor_video_config, _glm_effective_presize_budget, _glm_video_budget_ceiling，涉及 `_glm_video_metadata, glm_processor_video_config, _glm_effective_presize_budget`。
- 代码 diff 细节:
  - `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` modified +179/-1 (180 lines); hunks: -1,9 +1,19; -97,5 +107,173 @@ def test_glm4v_uses_default_offsets_when_token_ids_are_dist...; symbols: test_glm4v_uses_default_offsets_when_token_ids_are_distinct, _Glm5NextLikeVideoProcessor, _Glm4vLikeVideoProcessor, sample_frames
  - `python/sglang/srt/multimodal/processors/glm4v.py` modified +74/-5 (79 lines); hunks: -16,7 +16,7; -34,6 +34,7; symbols: _glm_video_metadata, glm_processor_video_config, _glm_effective_presize_budget, _glm_video_budget_ceiling
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py` modified +179/-1
  - runtime: `python/sglang/srt/multimodal/processors/glm4v.py` modified +74/-5
- 验证与风险: diff 自带测试面 `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37597 - [Feat] [CPU] glm_ocr: Add model support

- 链接: https://github.com/sgl-project/sglang/pull/37597
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm_ocr.py`；关联提交 `3e9ce4394443`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+306/-252，可读 patch 824 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] [CPU] glm_ocr: Add model support」；模型线: GLM VLM/OCR；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/glm_ocr.py`；技术摘要: 覆盖「[Feat] [CPU] glm_ocr: Add model support」；主要实现面是 `python/sglang/srt/models/glm_ocr.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm_ocr.py` modified +1/-0 (1 lines); hunks: -205,6 +205,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm_ocr.py` modified +1/-0 (1 lines); hunks: -205,6 +205,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm_ocr.py
@@ -205,6 +205,7 @@ def __init__(
+                    num_dummy_heads=vision_config.num_dummy_heads,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm_ocr.py` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/cpu/test_conv3d_embed.py`, `test/registered/cpu/test_norm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
