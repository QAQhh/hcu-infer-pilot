# sglang Intern-S1 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/InternLM/Intern-S1.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/intern-s1-deployment.jsx` | no direct PR-number commit |
| `python/sglang/srt/function_call/internlm_detector.py` | [#14866](https://github.com/sgl-project/sglang/pull/14866) |
| `python/sglang/srt/models/interns1.py` | [#8350](https://github.com/sgl-project/sglang/pull/8350), [#9299](https://github.com/sgl-project/sglang/pull/9299), [#12367](https://github.com/sgl-project/sglang/pull/12367), [#28629](https://github.com/sgl-project/sglang/pull/28629) |
| `python/sglang/srt/models/interns1pro.py` | [#18145](https://github.com/sgl-project/sglang/pull/18145) |
| `python/sglang/srt/multimodal/processors/interns1pro.py` | [#18145](https://github.com/sgl-project/sglang/pull/18145) |
| `test/registered/unit/models/test_interns1pro_fope_loader_layout.py` | no direct PR-number commit |
| `test/registered/unit/models/test_interns1pro_processor.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 6
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 6
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-07-26 | [#8350](https://github.com/sgl-project/sglang/pull/8350) | merged | model: support intern-s1 | `python/sglang/srt/models/interns1.py` |
| 2025-08-19 | [#9299](https://github.com/sgl-project/sglang/pull/9299) | merged | support for interns1-mini | `python/sglang/srt/models/interns1.py` |
| 2025-11-03 | [#12367](https://github.com/sgl-project/sglang/pull/12367) | merged | [Bug] Fix Intern-S1 model accuracy and support /generate interface with input_ids | `python/sglang/srt/models/interns1.py` |
| 2025-12-16 | [#14866](https://github.com/sgl-project/sglang/pull/14866) | merged | Adding tool calling and reasoning parser support for Intern-S1 | `python/sglang/srt/function_call/internlm_detector.py` |
| 2026-02-04 | [#18145](https://github.com/sgl-project/sglang/pull/18145) | merged | support interns1-pro | `python/sglang/srt/models/interns1pro.py`, `python/sglang/srt/multimodal/processors/interns1pro.py` |
| 2026-06-18 | [#28629](https://github.com/sgl-project/sglang/pull/28629) | merged | [Bugfix] Fix Intern-S1 FP8 expert count lookup | `python/sglang/srt/models/interns1.py` |

## Per-PR Diff Audit Cards

### PR #8350 - model: support intern-s1

- Link: https://github.com/sgl-project/sglang/pull/8350
- Status/date: merged / 2025-07-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/interns1.py`; associated commits `b7094a5ef197`
- Diff scope read: GitHub Pull Request files API returned 10 files, +616/-63, 986 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "model: support intern-s1"; model line: Intern-S1; category: model support/runtime entry; main diff: `python/sglang/srt/models/interns1.py`; technical summary: Covers "model: support intern-s1"; the main implementation surface is `python/sglang/srt/models/interns1.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/interns1.py` added +328/-0 (328 lines); hunks: -0,0 +1,328; symbols: InternS1ForConditionalGeneration, __init__, _update_hf_config, pixel_shuffle, touching `InternS1ForConditionalGeneration, __init__, _update_hf_config`.
- Code diff details:
  - `python/sglang/srt/models/interns1.py` added +328/-0 (328 lines); hunks: -0,0 +1,328; symbols: InternS1ForConditionalGeneration, __init__, _update_hf_config, pixel_shuffle
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/interns1.py
@@ -0,0 +1,328 @@
+from typing import Iterable, List, Optional, Set, Tuple
+import torch
+from torch import nn
+from transformers import PretrainedConfig
+from sglang.srt.distributed import parallel_state
+from sglang.srt.layers.moe.ep_moe.layer import get_moe_impl_class
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/interns1.py` added +328/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/lang/chat_template.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9299 - support for interns1-mini

- Link: https://github.com/sgl-project/sglang/pull/9299
- Status/date: merged / 2025-08-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/interns1.py`; associated commits `a31ea4482436`
- Diff scope read: GitHub Pull Request files API returned 2 files, +7/-2, 30 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support for interns1-mini"; model line: Intern-S1; category: model support/runtime entry; main diff: `python/sglang/srt/models/interns1.py`; technical summary: Covers "support for interns1-mini"; the main implementation surface is `python/sglang/srt/models/interns1.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/interns1.py` modified +5/-0 (5 lines); hunks: -21,6 +21,7; -70,6 +71,10 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/interns1.py` modified +5/-0 (5 lines); hunks: -21,6 +21,7; -70,6 +71,10 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/interns1.py
@@ -21,6 +21,7 @@
+from sglang.srt.models.qwen3 import Qwen3ForCausalLM
@@ -70,6 +71,10 @@ def __init__(
+        elif config.text_config.architectures[0] == "Qwen3ForCausalLM":
+            self.language_model = Qwen3ForCausalLM(
+                config=config.text_config, quant_config=quant_config
+            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/interns1.py` modified +5/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/interns1.py`, `python/sglang/srt/models/qwen3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12367 - [Bug] Fix Intern-S1 model accuracy and support /generate interface with input_ids

- Link: https://github.com/sgl-project/sglang/pull/12367
- Status/date: merged / 2025-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/interns1.py`; associated commits `65f1d065c5cf`
- Diff scope read: GitHub Pull Request files API returned 3 files, +8/-41, 110 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug] Fix Intern-S1 model accuracy and support /generate interface with input_ids"; model line: Intern-S1; category: bug fix; main diff: `python/sglang/srt/models/interns1.py`; technical summary: Covers "[Bug] Fix Intern-S1 model accuracy and support /generate interface with input_ids"; the main implementation surface is `python/sglang/srt/models/interns1.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/interns1.py` modified +3/-21 (24 lines); hunks: -1,4 +1,4; -50,16 +50,13 @@ def __init__(; symbols: __init__, pixel_shuffle, extract_feature, load_weights, touching `__init__, pixel_shuffle, extract_feature`.
- Code diff details:
  - `python/sglang/srt/models/interns1.py` modified +3/-21 (24 lines); hunks: -1,4 +1,4; -50,16 +50,13 @@ def __init__(; symbols: __init__, pixel_shuffle, extract_feature, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/interns1.py
@@ -1,4 +1,4 @@
-from typing import Iterable, List, Optional, Set, Tuple
+from typing import Iterable, List, Optional, Tuple
@@ -50,16 +50,13 @@ def __init__(
-        self.ps_version = getattr(config, "ps_version", "v1")
-        # self.template = getattr(config, 'template', 'internvl2_5')
-        logger.info(f"ps_version: {self.ps_version}")
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/interns1.py` modified +3/-21
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/interns1.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/multimodal/processors/internvl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14866 - Adding tool calling and reasoning parser support for Intern-S1

- Link: https://github.com/sgl-project/sglang/pull/14866
- Status/date: merged / 2025-12-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/internlm_detector.py`; associated commits `5e96beb3e559`
- Diff scope read: GitHub Pull Request files API returned 6 files, +290/-14, 361 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Adding tool calling and reasoning parser support for Intern-S1"; model line: Intern-S1; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/internlm_detector.py`; technical summary: Covers "Adding tool calling and reasoning parser support for Intern-S1"; the main implementation surface is `python/sglang/srt/function_call/internlm_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/internlm_detector.py` added +248/-0 (248 lines); hunks: -0,0 +1,248; symbols: InternlmDetector, __init__, has_tool_call, get_arguments, touching `InternlmDetector, __init__, has_tool_call`.
- Code diff details:
  - `python/sglang/srt/function_call/internlm_detector.py` added +248/-0 (248 lines); hunks: -0,0 +1,248; symbols: InternlmDetector, __init__, has_tool_call, get_arguments
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/internlm_detector.py
@@ -0,0 +1,248 @@
+# modified from https://github.com/InternLM/lmdeploy/blob/main/lmdeploy/serve/openai/tool_parser/internlm2_parser.py
+import json
+import logging
+import re
+from typing import List
+from sglang.srt.entrypoints.openai.protocol import Tool
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/internlm_detector.py` added +248/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/constrained/xgrammar_backend.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18145 - support interns1-pro

- Link: https://github.com/sgl-project/sglang/pull/18145
- Status/date: merged / 2026-02-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/interns1pro.py`, `python/sglang/srt/multimodal/processors/interns1pro.py`; associated commits `3e7ecb78a60f`
- Diff scope read: GitHub Pull Request files API returned 6 files, +586/-2, 647 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support interns1-pro"; model line: Intern-S1; category: model support/runtime entry; main diff: `python/sglang/srt/models/interns1pro.py`, `python/sglang/srt/multimodal/processors/interns1pro.py`; technical summary: Covers "support interns1-pro"; the main implementation surface is `python/sglang/srt/models/interns1pro.py`, `python/sglang/srt/multimodal/processors/interns1pro.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/interns1pro.py` added +252/-0 (252 lines); hunks: -0,0 +1,252; symbols: InternS1ProTextAttention, __init__, forward_prepare_npu, InternS1ProTextDecoderLayer, touching `InternS1ProTextAttention, __init__, forward_prepare_npu`; `python/sglang/srt/multimodal/processors/interns1pro.py` added +118/-0 (118 lines); hunks: -0,0 +1,118; symbols: InternS1_1ImageProcessor, get_mm_data, process_mm_data_async, touching `InternS1_1ImageProcessor, get_mm_data, process_mm_data_async`.
- Code diff details:
  - `python/sglang/srt/models/interns1pro.py` added +252/-0 (252 lines); hunks: -0,0 +1,252; symbols: InternS1ProTextAttention, __init__, forward_prepare_npu, InternS1ProTextDecoderLayer
  - `python/sglang/srt/multimodal/processors/interns1pro.py` added +118/-0 (118 lines); hunks: -0,0 +1,118; symbols: InternS1_1ImageProcessor, get_mm_data, process_mm_data_async
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/interns1pro.py
@@ -0,0 +1,252 @@
+import functools
+import logging
+from typing import Any, Dict, Iterable, Optional, Tuple
+import torch
+from transformers import PretrainedConfig
+from sglang.srt.layers.dp_attention import get_attention_tp_rank, get_attention_tp_size
diff -- python/sglang/srt/multimodal/processors/interns1pro.py
@@ -0,0 +1,118 @@
+import time
+from typing import List, Union
+from sglang.srt.managers.schedule_batch import Modality, MultimodalDataItem
+from sglang.srt.models.interns1pro import InternS1ProForConditionalGeneration
+from sglang.srt.multimodal.processors.qwen_vl import (
+    QwenVLImageProcessor,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/interns1pro.py` added +252/-0; `python/sglang/srt/multimodal/processors/interns1pro.py` added +118/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/layers/rotary_embedding.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28629 - [Bugfix] Fix Intern-S1 FP8 expert count lookup

- Link: https://github.com/sgl-project/sglang/pull/28629
- Status/date: merged / 2026-06-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/interns1.py`; associated commits `b7d7dfb4ed5a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Intern-S1 FP8 expert count lookup"; model line: Intern-S1; category: bug fix; main diff: `python/sglang/srt/models/interns1.py`; technical summary: Covers "[Bugfix] Fix Intern-S1 FP8 expert count lookup"; the main implementation surface is `python/sglang/srt/models/interns1.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/interns1.py` modified +1/-1 (2 lines); hunks: -211,7 +211,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/interns1.py` modified +1/-1 (2 lines); hunks: -211,7 +211,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/interns1.py
@@ -211,7 +211,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-                num_experts=self.config.num_experts,
+                num_experts=self.config.text_config.num_experts,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/interns1.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/interns1.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
