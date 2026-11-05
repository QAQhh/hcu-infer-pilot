# sglang Mistral Small 4 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/Mistral/Devstral-2.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/Mistral/Ministral-3.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/Mistral/Mistral-Large-4.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/Mistral/Mistral-Medium-3.5.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/Mistral/Mistral-Small-4.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/ministral-3-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/mistral-medium-3-5-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/mistral-small-4-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/configs/mistralai/mistral-large-4-benchmarks.jsx` | no direct PR-number commit |
| `docs/src/snippets/configs/mistralai/mistral-large-4.jsx` | no direct PR-number commit |
| `python/sglang/srt/function_call/mistral_detector.py` | [#6597](https://github.com/sgl-project/sglang/pull/6597), [#14921](https://github.com/sgl-project/sglang/pull/14921), [#20708](https://github.com/sgl-project/sglang/pull/20708) |
| `python/sglang/srt/models/ministral3.py` | [#14251](https://github.com/sgl-project/sglang/pull/14251), [#29111](https://github.com/sgl-project/sglang/pull/29111) |
| `python/sglang/srt/models/mistral.py` | [#108](https://github.com/sgl-project/sglang/pull/108), [#5099](https://github.com/sgl-project/sglang/pull/5099), [#39185](https://github.com/sgl-project/sglang/pull/39185), [#45656](https://github.com/sgl-project/sglang/pull/45656) |
| `python/sglang/srt/models/mistral_eagle.py` | no direct PR-number commit |
| `python/sglang/srt/models/mistral_large_3.py` | [#14213](https://github.com/sgl-project/sglang/pull/14213), [#14466](https://github.com/sgl-project/sglang/pull/14466), [#14485](https://github.com/sgl-project/sglang/pull/14485) |
| `python/sglang/srt/models/mistral_large_3_eagle.py` | [#14466](https://github.com/sgl-project/sglang/pull/14466), [#14485](https://github.com/sgl-project/sglang/pull/14485), [#20708](https://github.com/sgl-project/sglang/pull/20708), [#33785](https://github.com/sgl-project/sglang/pull/33785) |
| `python/sglang/srt/utils/hf_transformers/mistral_utils.py` | [#30396](https://github.com/sgl-project/sglang/pull/30396), [#35215](https://github.com/sgl-project/sglang/pull/35215), [#35915](https://github.com/sgl-project/sglang/pull/35915) |
| `test/manual/models/test_mistral_large3_basic.py` | no direct PR-number commit |
| `test/registered/e2e/models_large/test_mistral_large3.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_mistral_small_3_1_24b_instruct_2503.py` | no direct PR-number commit |
| `test/registered/unit/constrained/test_mistral_common_xgrammar.py` | [#35215](https://github.com/sgl-project/sglang/pull/35215) |
| `test/registered/unit/function_call/test_mistral_detector.py` | [#21399](https://github.com/sgl-project/sglang/pull/21399) |
| `test/registered/unit/models/test_mistral3_vision_feature.py` | [#39185](https://github.com/sgl-project/sglang/pull/39185), [#45656](https://github.com/sgl-project/sglang/pull/45656) |
| `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` | [#35915](https://github.com/sgl-project/sglang/pull/35915) |

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
| 2024-01-26 | [#108](https://github.com/sgl-project/sglang/pull/108) | merged | Fix Mistral model loading | `python/sglang/srt/models/mistral.py` |
| 2025-05-17 | [#5099](https://github.com/sgl-project/sglang/pull/5099) | merged | model(vlm): mistral 3.1 | `python/sglang/srt/models/mistral.py` |
| 2025-05-26 | [#6597](https://github.com/sgl-project/sglang/pull/6597) | merged | feat: Improve Mistral and Qwen25 function call parsing | `python/sglang/srt/function_call/mistral_detector.py` |
| 2025-12-04 | [#14213](https://github.com/sgl-project/sglang/pull/14213) | merged | Add Mistral Large 3 support. | `python/sglang/srt/models/mistral_large_3.py` |
| 2025-12-04 | [#14251](https://github.com/sgl-project/sglang/pull/14251) | merged | ministral3 | `python/sglang/srt/models/ministral3.py` |
| 2025-12-05 | [#14466](https://github.com/sgl-project/sglang/pull/14466) | merged | Add Mistral Large 3 Eagle Support | `python/sglang/srt/models/mistral_large_3_eagle.py`, `python/sglang/srt/models/mistral_large_3.py` |
| 2025-12-12 | [#14921](https://github.com/sgl-project/sglang/pull/14921) | merged | update mistral detector | `python/sglang/srt/function_call/mistral_detector.py` |
| 2025-12-13 | [#14485](https://github.com/sgl-project/sglang/pull/14485) | merged | Mistral Large 3 NVFP4 support | `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py` |
| 2026-03-18 | [#20708](https://github.com/sgl-project/sglang/pull/20708) | merged | Add Mistral Small 4 (Pixtral) support | `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py` |
| 2026-04-06 | [#21399](https://github.com/sgl-project/sglang/pull/21399) | merged | [CI] Add unit tests for function_call detectors (hermes, llama32, mistral) | `test/registered/unit/function_call/test_mistral_detector.py` |
| 2026-06-25 | [#29111](https://github.com/sgl-project/sglang/pull/29111) | merged | [Bugfix] Fix Ministral3 init argument forwarding | `python/sglang/srt/models/ministral3.py` |
| 2026-07-09 | [#30396](https://github.com/sgl-project/sglang/pull/30396) | merged | Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral) | `python/sglang/srt/utils/hf_transformers/mistral_utils.py` |
| 2026-08-06 | [#33785](https://github.com/sgl-project/sglang/pull/33785) | merged | Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__ | `python/sglang/srt/models/mistral_large_3_eagle.py` |
| 2026-08-19 | [#35215](https://github.com/sgl-project/sglang/pull/35215) | merged | [Constrained] Support MistralCommon tokenizers in the XGrammar backend | `test/registered/unit/constrained/test_mistral_common_xgrammar.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py` |
| 2026-08-24 | [#35915](https://github.com/sgl-project/sglang/pull/35915) | merged | [OpenAI] Drop empty assistant turns for mistral_common tokenizers | `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py` |
| 2026-09-18 | [#39185](https://github.com/sgl-project/sglang/pull/39185) | merged | Fix Mistral3 retaining every vision-tower layer to read one | `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py` |
| 2026-10-23 | [#45656](https://github.com/sgl-project/sglang/pull/45656) | merged | [Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it | `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py` |

## Per-PR Diff Audit Cards

### PR #108 - Fix Mistral model loading

- Link: https://github.com/sgl-project/sglang/pull/108
- Status/date: merged / 2024-01-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral.py`; associated commits `cd6872334e9e`
- Diff scope read: GitHub Pull Request files API returned 1 files, +10/-0, 11 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Mistral model loading"; model line: Mistral Small 4; category: bug fix; main diff: `python/sglang/srt/models/mistral.py`; technical summary: Covers "Fix Mistral model loading"; the main implementation surface is `python/sglang/srt/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mistral.py` added +10/-0 (10 lines); hunks: -0,0 +1,10; symbols: MistralForCausalLM, __init__, touching `MistralForCausalLM, __init__`.
- Code diff details:
  - `python/sglang/srt/models/mistral.py` added +10/-0 (10 lines); hunks: -0,0 +1,10; symbols: MistralForCausalLM, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mistral.py
@@ -0,0 +1,10 @@
+"""Inference-only Mistral model."""
+from sglang.srt.models.llama2 import LlamaForCausalLM
+class MistralForCausalLM(LlamaForCausalLM):
+    def __init__(self, *args, **kwargs):
+        super().__init__(*args, **kwargs)
+EntryClass = MistralForCausalLM
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mistral.py` added +10/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #5099 - model(vlm): mistral 3.1

- Link: https://github.com/sgl-project/sglang/pull/5099
- Status/date: merged / 2025-05-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral.py`; associated commits `64825b839521`
- Diff scope read: GitHub Pull Request files API returned 6 files, +152/-21, 272 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "model(vlm): mistral 3.1"; model line: Mistral Small 4; category: model implementation change; main diff: `python/sglang/srt/models/mistral.py`; technical summary: Covers "model(vlm): mistral 3.1"; the main implementation surface is `python/sglang/srt/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mistral.py` modified +71/-1 (72 lines); hunks: -13,11 +13,81; symbols: MistralForCausalLM, [REDACTED_MISTRAL_API_KEY], __init__, get_image_feature, touching `MistralForCausalLM, [REDACTED_MISTRAL_API_KEY], __init__`.
- Code diff details:
  - `python/sglang/srt/models/mistral.py` modified +71/-1 (72 lines); hunks: -13,11 +13,81; symbols: MistralForCausalLM, [REDACTED_MISTRAL_API_KEY], __init__, get_image_feature
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mistral.py
@@ -13,11 +13,81 @@
+from typing import List, Union
+import torch
+from transformers.models.mistral3.modeling_mistral3 import Mistral3MultiModalProjector
+from sglang.srt.managers.schedule_batch import MultimodalDataItem
-EntryClass = MistralForCausalLM
+class [REDACTED_MISTRAL_API_KEY]:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mistral.py` modified +71/-1
- Risk and verification: The diff ships test coverage in `test/srt/test_vision_openai_server.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #6597 - feat: Improve Mistral and Qwen25 function call parsing

- Link: https://github.com/sgl-project/sglang/pull/6597
- Status/date: merged / 2025-05-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/mistral_detector.py`; associated commits `16f69b1f65c6`
- Diff scope read: GitHub Pull Request files API returned 7 files, +318/-61, 529 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: Improve Mistral and Qwen25 function call parsing"; model line: Mistral Small 4; category: model implementation change; main diff: `python/sglang/srt/function_call/mistral_detector.py`; technical summary: Covers "feat: Improve Mistral and Qwen25 function call parsing"; the main implementation surface is `python/sglang/srt/function_call/mistral_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/mistral_detector.py` modified +72/-26 (98 lines); hunks: -1,4 +1,5; -11,12 +12,14; symbols: MistralDetector, __init__, has_tool_call, _clean_text, touching `MistralDetector, __init__, has_tool_call`.
- Code diff details:
  - `python/sglang/srt/function_call/mistral_detector.py` modified +72/-26 (98 lines); hunks: -1,4 +1,5; -11,12 +12,14; symbols: MistralDetector, __init__, has_tool_call, _clean_text
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/mistral_detector.py
@@ -1,4 +1,5 @@
+import logging
@@ -11,12 +12,14 @@
+logger = logging.getLogger(__name__)
-      [TOOL_CALLS] [{"name":"xxx", "arguments":{...}}]
+      [TOOL_CALLS] [{"name":"func1", "arguments":{...}}, {"name":"func2", "arguments":{...}}]
@@ -32,21 +35,6 @@ def has_tool_call(self, text: str) -> bool:
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/mistral_detector.py` modified +72/-26
- Risk and verification: The diff ships test coverage in `test/srt/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14213 - Add Mistral Large 3 support.

- Link: https://github.com/sgl-project/sglang/pull/14213
- Status/date: merged / 2025-12-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral_large_3.py`; associated commits `842807843671`
- Diff scope read: GitHub Pull Request files API returned 16 files, +1400/-120, 2012 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add Mistral Large 3 support."; model line: Mistral Small 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/mistral_large_3.py`; technical summary: Covers "Add Mistral Large 3 support."; the main implementation surface is `python/sglang/srt/models/mistral_large_3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mistral_large_3.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: MistralLarge3ForCausalLM, load_weights, _iterable_remap_mistral_to_ds, touching `MistralLarge3ForCausalLM, load_weights, _iterable_remap_mistral_to_ds`.
- Code diff details:
  - `python/sglang/srt/models/mistral_large_3.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: MistralLarge3ForCausalLM, load_weights, _iterable_remap_mistral_to_ds
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mistral_large_3.py
@@ -0,0 +1,81 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Iterable
+import regex as re
+import torch
+from sglang.srt.models.deepseek_v2 import DeepseekV3ForCausalLM
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mistral_large_3.py` added +81/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14251 - ministral3

- Link: https://github.com/sgl-project/sglang/pull/14251
- Status/date: merged / 2025-12-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/ministral3.py`; associated commits `6d37e7088337`
- Diff scope read: GitHub Pull Request files API returned 14 files, +245/-26, 405 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "ministral3"; model line: Mistral Small 4; category: model implementation change; main diff: `python/sglang/srt/models/ministral3.py`; technical summary: Covers "ministral3"; the main implementation surface is `python/sglang/srt/models/ministral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/ministral3.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: _get_llama_4_attn_scale, Ministral3Attention, __init__, forward, touching `_get_llama_4_attn_scale, Ministral3Attention, __init__`.
- Code diff details:
  - `python/sglang/srt/models/ministral3.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: _get_llama_4_attn_scale, Ministral3Attention, __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/ministral3.py
@@ -0,0 +1,157 @@
+from typing import Any, Dict, Optional
+import torch
+from transformers import PretrainedConfig
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
+from sglang.srt.model_executor.forward_batch_info import ForwardBatch
+from sglang.srt.models.llama import (
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/ministral3.py` added +157/-0
- Risk and verification: The diff ships test coverage in `test/srt/models/test_ministral3_models.py`, `test/srt/run_suite.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14466 - Add Mistral Large 3 Eagle Support

- Link: https://github.com/sgl-project/sglang/pull/14466
- Status/date: merged / 2025-12-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`; associated commits `205f041e9619`
- Diff scope read: GitHub Pull Request files API returned 9 files, +313/-62, 550 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add Mistral Large 3 Eagle Support"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/mistral_large_3_eagle.py`, `python/sglang/srt/models/mistral_large_3.py`; technical summary: Covers "Add Mistral Large 3 Eagle Support"; the main implementation surface is `python/sglang/srt/models/mistral_large_3_eagle.py`, `python/sglang/srt/models/mistral_large_3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mistral_large_3_eagle.py` added +105/-0 (105 lines); hunks: -0,0 +1,105; symbols: MistralLarge3Model, __init__, forward, MistralLarge3ForCausalLMEagle, touching `MistralLarge3Model, __init__, forward`; `python/sglang/srt/models/mistral_large_3.py` modified +0/-3 (3 lines); hunks: -72,9 +72,6 @@ def _iterable_remap_mistral_to_ds(; symbols: _iterable_remap_mistral_to_ds, touching `_iterable_remap_mistral_to_ds`.
- Code diff details:
  - `python/sglang/srt/models/mistral_large_3_eagle.py` added +105/-0 (105 lines); hunks: -0,0 +1,105; symbols: MistralLarge3Model, __init__, forward, MistralLarge3ForCausalLMEagle
  - `python/sglang/srt/models/mistral_large_3.py` modified +0/-3 (3 lines); hunks: -72,9 +72,6 @@ def _iterable_remap_mistral_to_ds(; symbols: _iterable_remap_mistral_to_ds
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -0,0 +1,105 @@
+from typing import Optional
+import torch
+from torch import nn
+from transformers import PretrainedConfig
+from python.sglang.srt.layers.attention.nsa.utils import is_nsa_enable_prefill_cp
+from sglang.srt.distributed import get_pp_group
diff -- python/sglang/srt/models/mistral_large_3.py
@@ -72,9 +72,6 @@ def _iterable_remap_mistral_to_ds(
-            if name.endswith(".weight_scale") and ".experts." not in name:
-                name = re.sub(r"\.weight_scale$", ".weight_scale_inv", name)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mistral_large_3_eagle.py` added +105/-0; `python/sglang/srt/models/mistral_large_3.py` modified +0/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14921 - update mistral detector

- Link: https://github.com/sgl-project/sglang/pull/14921
- Status/date: merged / 2025-12-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/mistral_detector.py`; associated commits `fd1ebbb0d614`
- Diff scope read: GitHub Pull Request files API returned 2 files, +274/-34, 361 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "update mistral detector"; model line: Mistral Small 4; category: model implementation change; main diff: `python/sglang/srt/function_call/mistral_detector.py`; technical summary: Covers "update mistral detector"; the main implementation surface is `python/sglang/srt/function_call/mistral_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/mistral_detector.py` modified +240/-34 (274 lines); hunks: -1,47 +1,49; -51,31 +53,235 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: MistralDetector, __init__, has_tool_call, detect_and_parse, touching `MistralDetector, __init__, has_tool_call`.
- Code diff details:
  - `python/sglang/srt/function_call/mistral_detector.py` modified +240/-34 (274 lines); hunks: -1,47 +1,49; -51,31 +53,235 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: MistralDetector, __init__, has_tool_call, detect_and_parse
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/mistral_detector.py
@@ -1,47 +1,49 @@
-import re
-from typing import List
+from typing import Any, List, Optional, Tuple
+    ToolCallItem,
+from sglang.srt.function_call.utils import _is_complete_json
-    Detector for Mistral model function call format.
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/mistral_detector.py` modified +240/-34
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14485 - Mistral Large 3 NVFP4 support

- Link: https://github.com/sgl-project/sglang/pull/14485
- Status/date: merged / 2025-12-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`; associated commits `f6031adf0875`
- Diff scope read: GitHub Pull Request files API returned 11 files, +502/-36, 707 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Mistral Large 3 NVFP4 support"; model line: Mistral Small 4; category: performance/backend optimization; main diff: `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`; technical summary: Covers "Mistral Large 3 NVFP4 support"; the main implementation surface is `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mistral_large_3.py` modified +1/-1 (2 lines); hunks: -1,5 +1,5; `python/sglang/srt/models/mistral_large_3_eagle.py` modified +2/-0 (2 lines); hunks: -1,3 +1,5.
- Code diff details:
  - `python/sglang/srt/models/mistral_large_3.py` modified +1/-1 (2 lines); hunks: -1,5 +1,5
  - `python/sglang/srt/models/mistral_large_3_eagle.py` modified +2/-0 (2 lines); hunks: -1,3 +1,5
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mistral_large_3.py
@@ -1,5 +1,5 @@
+# Adapted from https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mistral_large_3.py
-# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -1,3 +1,5 @@
+# Adapted from https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mistral_large_3_eagle.py
+# SPDX-License-Identifier: Apache-2.0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mistral_large_3.py` modified +1/-1; `python/sglang/srt/models/mistral_large_3_eagle.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20708 - Add Mistral Small 4 (Pixtral) support

- Link: https://github.com/sgl-project/sglang/pull/20708
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`; associated commits `6b8a6545b231`
- Diff scope read: GitHub Pull Request files API returned 18 files, +360/-124, 868 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add Mistral Small 4 (Pixtral) support"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`; technical summary: Covers "Add Mistral Small 4 (Pixtral) support"; the main implementation surface is `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/mistral_detector.py` modified +17/-9 (26 lines); hunks: -90,19 +90,27 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: detect_and_parse, parse_streaming_increment, touching `detect_and_parse, parse_streaming_increment`; `python/sglang/srt/models/mistral_large_3_eagle.py` modified +11/-3 (14 lines); hunks: -18,7 +18,10; -99,9 +102,14 @@ def __init__(; symbols: MistralLarge3Model, MistralLarge3EagleModel, __init__, touching `MistralLarge3Model, MistralLarge3EagleModel, __init__`.
- Code diff details:
  - `python/sglang/srt/function_call/mistral_detector.py` modified +17/-9 (26 lines); hunks: -90,19 +90,27 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: detect_and_parse, parse_streaming_increment
  - `python/sglang/srt/models/mistral_large_3_eagle.py` modified +11/-3 (14 lines); hunks: -18,7 +18,10; -99,9 +102,14 @@ def __init__(; symbols: MistralLarge3Model, MistralLarge3EagleModel, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/mistral_detector.py
@@ -90,19 +90,27 @@ def detect_and_parse(self, text: str, tools: List[Tool]) -> StreamingParseResult
-        parsed = self._try_parse_compact_args_format(tool_part)
-        if not parsed:
+        # Loop to extract all consecutive compact tool calls.
+        all_calls: list = []
+        remaining = tool_part
+        while remaining:
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -18,7 +18,10 @@
-class MistralLarge3Model(DeepseekV2Model):
+class MistralLarge3EagleModel(DeepseekV2Model):
+    """EAGLE draft model with an fc layer that fuses token embeddings and
+    target-model hidden states before passing through transformer layers."""
@@ -99,9 +102,14 @@ def __init__(
-        config.quant_config = quant_config
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/mistral_detector.py` modified +17/-9; `python/sglang/srt/models/mistral_large_3_eagle.py` modified +11/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/deepseek_ocr.py`, `python/sglang/srt/configs/deepseekvl2.py`, `python/sglang/srt/configs/janus_pro.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21399 - [CI] Add unit tests for function_call detectors (hermes, llama32, mistral)

- Link: https://github.com/sgl-project/sglang/pull/21399
- Status/date: merged / 2026-04-06
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/unit/function_call/test_mistral_detector.py`; associated commits `30f5b8760851`
- Diff scope read: GitHub Pull Request files API returned 3 files, +595/-0, 598 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Add unit tests for function_call detectors (hermes, llama32, mistral)"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `test/registered/unit/function_call/test_mistral_detector.py`; technical summary: Covers "[CI] Add unit tests for function_call detectors (hermes, llama32, mistral)"; the main implementation surface is `test/registered/unit/function_call/test_mistral_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/function_call/test_mistral_detector.py` added +224/-0 (224 lines); hunks: -0,0 +1,224; symbols: TestMistralDetector, setUp, test_has_tool_call_json_array_format, test_has_tool_call_compact_format, touching `TestMistralDetector, setUp, test_has_tool_call_json_array_format`.
- Code diff details:
  - `test/registered/unit/function_call/test_mistral_detector.py` added +224/-0 (224 lines); hunks: -0,0 +1,224; symbols: TestMistralDetector, setUp, test_has_tool_call_json_array_format, test_has_tool_call_compact_format
- Key code excerpts:

```diff
diff -- test/registered/unit/function_call/test_mistral_detector.py
@@ -0,0 +1,224 @@
+"""Unit tests for MistralDetector — no server, no model loading."""
+import json
+from sglang.srt.entrypoints.openai.protocol import Function, Tool
+from sglang.srt.function_call.mistral_detector import MistralDetector
+from sglang.test.ci.ci_register import register_cpu_ci
+from sglang.test.test_utils import CustomTestCase
```

- Reviewed files:
  - tests: `test/registered/unit/function_call/test_mistral_detector.py` added +224/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/function_call/test_hermes_detector.py`, `test/registered/unit/function_call/test_llama32_detector.py`, `test/registered/unit/function_call/test_mistral_detector.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29111 - [Bugfix] Fix Ministral3 init argument forwarding

- Link: https://github.com/sgl-project/sglang/pull/29111
- Status/date: merged / 2026-06-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/ministral3.py`; associated commits `ddda4f90288b`
- Diff scope read: GitHub Pull Request files API returned 1 files, +37/-17, 99 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Ministral3 init argument forwarding"; model line: Mistral Small 4; category: bug fix; main diff: `python/sglang/srt/models/ministral3.py`; technical summary: Covers "[Bugfix] Fix Ministral3 init argument forwarding"; the main implementation surface is `python/sglang/srt/models/ministral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/ministral3.py` modified +37/-17 (54 lines); hunks: -31,6 +31,7 @@ def __init__(; -40,18 +41,19 @@ def __init__(; symbols: __init__, forward, Ministral3DecoderLayer, touching `__init__, forward, Ministral3DecoderLayer`.
- Code diff details:
  - `python/sglang/srt/models/ministral3.py` modified +37/-17 (54 lines); hunks: -31,6 +31,7 @@ def __init__(; -40,18 +41,19 @@ def __init__(; symbols: __init__, forward, Ministral3DecoderLayer
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/ministral3.py
@@ -31,6 +31,7 @@ def __init__(
+        start_layer: int = 0,
@@ -40,18 +41,19 @@ def __init__(
-            config,
-            hidden_size,
-            num_heads,
-            num_kv_heads,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/ministral3.py` modified +37/-17
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/ministral3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #30396 - Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral)

- Link: https://github.com/sgl-project/sglang/pull/30396
- Status/date: merged / 2026-07-09
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/utils/hf_transformers/mistral_utils.py`; associated commits `7132af28de0b`
- Diff scope read: GitHub Pull Request files API returned 4 files, +138/-12, 190 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral)"; model line: Mistral Small 4; category: bug fix; main diff: `python/sglang/srt/utils/hf_transformers/mistral_utils.py`; technical summary: Covers "Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral)"; the main implementation surface is `python/sglang/srt/utils/hf_transformers/mistral_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +34/-1 (35 lines); hunks: -11,7 +11,12; -430,6 +435,34 @@ def wrap_as_pixtral(processor, config):; symbols: adapt_config_dict, wrap_as_pixtral, is_bare_tekken_checkpoint, retry_without_mistral_common_kwargs, touching `adapt_config_dict, wrap_as_pixtral, is_bare_tekken_checkpoint`.
- Code diff details:
  - `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +34/-1 (35 lines); hunks: -11,7 +11,12; -430,6 +435,34 @@ def wrap_as_pixtral(processor, config):; symbols: adapt_config_dict, wrap_as_pixtral, is_bare_tekken_checkpoint, retry_without_mistral_common_kwargs
- Key code excerpts:

```diff
diff -- python/sglang/srt/utils/hf_transformers/mistral_utils.py
@@ -11,7 +11,12 @@
-from .common import _ensure_sub_configs, download_from_hf
+from .common import (
+    _cached_file_exists,
+    _ensure_sub_configs,
+    _remote_file_exists,
+    download_from_hf,
```

- Reviewed files:
  - runtime: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +34/-1
- Risk and verification: The diff ships test coverage in `test/registered/unit/tokenizer/test_tekken_tokenizer_routing.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #33785 - Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__

- Link: https://github.com/sgl-project/sglang/pull/33785
- Status/date: merged / 2026-08-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral_large_3_eagle.py`; associated commits `dd7e4c91e2e1`
- Diff scope read: GitHub Pull Request files API returned 2 files, +25/-54, 118 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__"; model line: Mistral Small 4; category: bug fix; main diff: `python/sglang/srt/models/mistral_large_3_eagle.py`; technical summary: Covers "Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__"; the main implementation surface is `python/sglang/srt/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mistral_large_3_eagle.py` modified +6/-46 (52 lines); hunks: -4,19 +4,12; -31,50 +24,17 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/mistral_large_3_eagle.py` modified +6/-46 (52 lines); hunks: -4,19 +4,12; -31,50 +24,17 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -4,19 +4,12 @@
-from torch import nn
-from sglang.srt.configs.model_config import is_deepseek_dsa
-from sglang.srt.distributed import get_pp_group
-from sglang.srt.layers.attention.dsa.utils import is_dsa_enable_prefill_cp
-from sglang.srt.layers.layernorm import RMSNorm
-from sglang.srt.layers.utils.cp_utils import is_prefill_context_parallel_enabled
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mistral_large_3_eagle.py` modified +6/-46
- Risk and verification: The diff ships test coverage in `test/registered/8-gpu-models/test_mistral_large3.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #35215 - [Constrained] Support MistralCommon tokenizers in the XGrammar backend

- Link: https://github.com/sgl-project/sglang/pull/35215
- Status/date: merged / 2026-08-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `test/registered/unit/constrained/test_mistral_common_xgrammar.py`; associated commits `3391ab3712bb`
- Diff scope read: GitHub Pull Request files API returned 3 files, +168/-1, 189 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Constrained] Support MistralCommon tokenizers in the XGrammar backend"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `test/registered/unit/constrained/test_mistral_common_xgrammar.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`; technical summary: Covers "[Constrained] Support MistralCommon tokenizers in the XGrammar backend"; the main implementation surface is `test/registered/unit/constrained/test_mistral_common_xgrammar.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/constrained/test_mistral_common_xgrammar.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: _StubTekkenizer, __init__, id_to_piece, id_to_byte_piece, touching `_StubTekkenizer, __init__, id_to_piece`; `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +43/-0 (43 lines); hunks: -634,4 +634,47 @@ def _safe_apply_chat_template(messages, **kwargs):; symbols: _safe_apply_chat_template, init_xgrammar, touching `_safe_apply_chat_template, init_xgrammar`.
- Code diff details:
  - `test/registered/unit/constrained/test_mistral_common_xgrammar.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: _StubTekkenizer, __init__, id_to_piece, id_to_byte_piece
  - `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +43/-0 (43 lines); hunks: -634,4 +634,47 @@ def _safe_apply_chat_template(messages, **kwargs):; symbols: _safe_apply_chat_template, init_xgrammar
- Key code excerpts:

```diff
diff -- test/registered/unit/constrained/test_mistral_common_xgrammar.py
@@ -0,0 +1,112 @@
+import sys
+import pytest
+from sglang.srt.utils.hf_transformers.mistral_utils import (
+    patch_mistral_common_tokenizer,
+)
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/utils/hf_transformers/mistral_utils.py
@@ -634,4 +634,47 @@ def _safe_apply_chat_template(messages, **kwargs):
+    def init_xgrammar():
+        from xgrammar import TokenizerInfo
+        tekken = getattr(
+            getattr(tokenizer.tokenizer, "instruct_tokenizer", None), "tokenizer", None
+        )
+        if tekken is None or not hasattr(tekken, "id_to_byte_piece"):
```

- Reviewed files:
  - tests: `test/registered/unit/constrained/test_mistral_common_xgrammar.py` added +112/-0
  - runtime: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +43/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/constrained/test_mistral_common_xgrammar.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #35915 - [OpenAI] Drop empty assistant turns for mistral_common tokenizers

- Link: https://github.com/sgl-project/sglang/pull/35915
- Status/date: merged / 2026-08-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`; associated commits `0c1e9bda5773`
- Diff scope read: GitHub Pull Request files API returned 2 files, +125/-0, 136 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[OpenAI] Drop empty assistant turns for mistral_common tokenizers"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`; technical summary: Covers "[OpenAI] Drop empty assistant turns for mistral_common tokenizers"; the main implementation surface is `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` added +86/-0 (86 lines); hunks: -0,0 +1,86; symbols: _user, _assistant, _MistralCommonStub, name, touching `_user, _assistant, _MistralCommonStub`; `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +39/-0 (39 lines); hunks: -628,9 +628,48 @@ def _adapt_placeholder_messages_for_mistral_common(messages):; symbols: _adapt_placeholder_messages_for_mistral_common, _assistant_content_is_empty, _drop_empty_assistant_messages, _safe_apply_chat_template, touching `_adapt_placeholder_messages_for_mistral_common, _assistant_content_is_empty, _drop_empty_assistant_messages`.
- Code diff details:
  - `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` added +86/-0 (86 lines); hunks: -0,0 +1,86; symbols: _user, _assistant, _MistralCommonStub, name
  - `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +39/-0 (39 lines); hunks: -628,9 +628,48 @@ def _adapt_placeholder_messages_for_mistral_common(messages):; symbols: _adapt_placeholder_messages_for_mistral_common, _assistant_content_is_empty, _drop_empty_assistant_messages, _safe_apply_chat_template
- Key code excerpts:

```diff
diff -- test/registered/unit/tokenizer/test_mistral_empty_assistant.py
@@ -0,0 +1,86 @@
+import unittest
+from sglang.srt.utils.hf_transformers.mistral_utils import (
+    patch_mistral_common_tokenizer,
+)
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=3, suite="base-a-test-cpu")
diff -- python/sglang/srt/utils/hf_transformers/mistral_utils.py
@@ -628,9 +628,48 @@ def _adapt_placeholder_messages_for_mistral_common(messages):
+    def _assistant_content_is_empty(content):
+        if content is None:
+            return True
+        if isinstance(content, str):
+            return not content.strip()
+        if isinstance(content, list):
```

- Reviewed files:
  - tests: `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` added +86/-0
  - runtime: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +39/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39185 - Fix Mistral3 retaining every vision-tower layer to read one

- Link: https://github.com/sgl-project/sglang/pull/39185
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral.py`, `test/registered/unit/models/test_mistral3_vision_feature.py`; associated commits `2394b231c226`
- Diff scope read: GitHub Pull Request files API returned 3 files, +133/-12, 168 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Mistral3 retaining every vision-tower layer to read one"; model line: Mistral Small 4; category: bug fix; main diff: `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`; technical summary: Covers "Fix Mistral3 retaining every vision-tower layer to read one"; the main implementation surface is `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/models/test_mistral3_vision_feature.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: RecordingTower, __init__, __call__, _model, touching `RecordingTower, __init__, __call__`; `python/sglang/srt/models/mistral.py` modified +12/-6 (18 lines); hunks: -115,16 +115,22 @@ def get_image_feature(self, items: List[MultimodalDataItem...; symbols: get_image_feature, touching `get_image_feature`.
- Code diff details:
  - `test/registered/unit/models/test_mistral3_vision_feature.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: RecordingTower, __init__, __call__, _model
  - `python/sglang/srt/models/mistral.py` modified +12/-6 (18 lines); hunks: -115,16 +115,22 @@ def get_image_feature(self, items: List[MultimodalDataItem...; symbols: get_image_feature
- Key code excerpts:

```diff
diff -- test/registered/unit/models/test_mistral3_vision_feature.py
@@ -0,0 +1,109 @@
+"""Pixtral adaptors should not ask the vision tower for every layer to read one.
+The tower materialises one hidden-state tensor per layer when hidden states are
+requested, ~49x the tensor the model actually consumes. These tests pin that the
+final-layer case takes the cheap path and that both paths agree, for each
+adaptor that reads the Pixtral tower this way.
+"""
diff -- python/sglang/srt/models/mistral.py
@@ -115,16 +115,22 @@ def get_image_feature(self, items: List[MultimodalDataItem]) -> torch.Tensor:
+        # Requesting hidden states materialises one tensor per layer (~1.8 GiB per
+        # 1540px image); the plain forward returns the same tensor as the last entry.
+        last_layer_only = self.vision_feature_layer == -1
-            image_outputs = self.vision_tower(
-                pixel_values, image_sizes, output_hidden_states=True
-            )
```

- Reviewed files:
  - tests: `test/registered/unit/models/test_mistral3_vision_feature.py` added +109/-0
  - runtime: `python/sglang/srt/models/mistral.py` modified +12/-6
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_mistral3_vision_feature.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45656 - [Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it

- Link: https://github.com/sgl-project/sglang/pull/45656
- Status/date: merged / 2026-10-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mistral.py`, `test/registered/unit/models/test_mistral3_vision_feature.py`; associated commits `4542fc8f598e`
- Diff scope read: GitHub Pull Request files API returned 3 files, +125/-27, 223 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it"; model line: Mistral Small 4; category: bug fix; main diff: `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`; technical summary: Covers "[Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it"; the main implementation surface is `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/models/test_mistral3_vision_feature.py` modified +107/-1 (108 lines); hunks: -6,6 +6,8; -15,7 +17,7; symbols: test_features_are_concatenated_per_item, _bare_mistral3, RecordingLoader, __init__, touching `test_features_are_concatenated_per_item, _bare_mistral3, RecordingLoader`; `python/sglang/srt/models/mistral.py` modified +15/-25 (40 lines); hunks: -15,14 +15,17; -88,22 +91,18 @@ def _remap_mistral_to_llama(; symbols: _remap_mistral_to_llama, [REDACTED_MISTRAL_API_KEY], __init__, touching `_remap_mistral_to_llama, [REDACTED_MISTRAL_API_KEY], __init__`.
- Code diff details:
  - `test/registered/unit/models/test_mistral3_vision_feature.py` modified +107/-1 (108 lines); hunks: -6,6 +6,8; -15,7 +17,7; symbols: test_features_are_concatenated_per_item, _bare_mistral3, RecordingLoader, __init__
  - `python/sglang/srt/models/mistral.py` modified +15/-25 (40 lines); hunks: -15,14 +15,17; -88,22 +91,18 @@ def _remap_mistral_to_llama(; symbols: _remap_mistral_to_llama, [REDACTED_MISTRAL_API_KEY], __init__
- Key code excerpts:

```diff
diff -- test/registered/unit/models/test_mistral3_vision_feature.py
@@ -6,6 +6,8 @@
+import subprocess
+import sys
@@ -15,7 +17,7 @@
-register_cpu_ci(est_time=10, suite="base-a-test-cpu")
+register_cpu_ci(est_time=40, suite="base-a-test-cpu")
@@ -105,5 +107,109 @@ def test_features_are_concatenated_per_item(self):
diff -- python/sglang/srt/models/mistral.py
@@ -15,14 +15,17 @@
-from typing import List
+from typing import List, Optional
+from transformers import LlavaConfig
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
+from sglang.srt.models.llava import LlavaForConditionalGeneration
@@ -88,22 +91,18 @@ def _remap_mistral_to_llama(
```

- Reviewed files:
  - tests: `test/registered/unit/models/test_mistral3_vision_feature.py` modified +107/-1
  - runtime: `python/sglang/srt/models/mistral.py` modified +15/-25
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_mistral3_vision_feature.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
