# vllm ERNIE 4.5 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/model_executor/test_ernie45_vl_mrope.py` | [#39753](https://github.com/vllm-project/vllm/pull/39753) |
| `tests/reasoning/test_ernie45_reasoning_parser.py` | [#25027](https://github.com/vllm-project/vllm/pull/25027) |
| `tests/tool_parsers/test_ernie45_moe_tool_parser.py` | no direct PR-number commit |
| `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py` | no direct PR-number commit |
| `vllm/model_executor/models/ernie45.py` | [#21735](https://github.com/vllm-project/vllm/pull/21735) |
| `vllm/model_executor/models/ernie45_moe.py` | [#25936](https://github.com/vllm-project/vllm/pull/25936), [#26684](https://github.com/vllm-project/vllm/pull/26684), [#27316](https://github.com/vllm-project/vllm/pull/27316) |
| `vllm/model_executor/models/ernie45_vl.py` | [#39753](https://github.com/vllm-project/vllm/pull/39753), [#45254](https://github.com/vllm-project/vllm/pull/45254), [#51461](https://github.com/vllm-project/vllm/pull/51461) |
| `vllm/model_executor/models/ernie45_vl_moe.py` | [#25936](https://github.com/vllm-project/vllm/pull/25936), [#26885](https://github.com/vllm-project/vllm/pull/26885) |
| `vllm/model_executor/models/ernie_mtp.py` | no direct PR-number commit |
| `vllm/reasoning/ernie45_reasoning_parser.py` | [#25027](https://github.com/vllm-project/vllm/pull/25027), [#27973](https://github.com/vllm-project/vllm/pull/27973), [#46255](https://github.com/vllm-project/vllm/pull/46255) |
| `vllm/tool_parsers/ernie45_tool_parser.py` | no direct PR-number commit |

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
| 2026-08-11 | [#51461](https://github.com/vllm-project/vllm/pull/51461) | merged | [MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs | `vllm/model_executor/models/ernie45_vl.py` |
| 2026-08-06 | [#45254](https://github.com/vllm-project/vllm/pull/45254) | merged | [MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference | `vllm/model_executor/models/ernie45_vl.py` |
| 2026-07-01 | [#46255](https://github.com/vllm-project/vllm/pull/46255) | merged | fix(reasoning): guard rfind in ernie45 streaming branch | `vllm/reasoning/ernie45_reasoning_parser.py` |
| 2026-04-14 | [#39753](https://github.com/vllm-project/vllm/pull/39753) | merged | [Model] Use mm_features for Ernie-4.5 VL M-RoPE | `vllm/model_executor/models/ernie45_vl.py`, `tests/model_executor/test_ernie45_vl_mrope.py` |
| 2025-11-04 | [#27973](https://github.com/vllm-project/vllm/pull/27973) | merged | [Model] fix ernie45 reasoning_parser | `vllm/reasoning/ernie45_reasoning_parser.py` |
| 2025-10-27 | [#27316](https://github.com/vllm-project/vllm/pull/27316) | merged | [Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple | `vllm/model_executor/models/ernie45_moe.py` |
| 2025-10-16 | [#26885](https://github.com/vllm-project/vllm/pull/26885) | merged | [Model][Bugfix] fix ernie45 vl run failed from shared experts optimization | `vllm/model_executor/models/ernie45_vl_moe.py` |
| 2025-10-14 | [#26684](https://github.com/vllm-project/vllm/pull/26684) | merged | [Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code | `vllm/model_executor/models/ernie45_moe.py` |
| 2025-10-13 | [#25027](https://github.com/vllm-project/vllm/pull/25027) | merged | [Model] Add reasoning_parser and tool_parser for Ernie45 thinking | `vllm/reasoning/ernie45_reasoning_parser.py`, `tests/reasoning/test_ernie45_reasoning_parser.py` |
| 2025-09-30 | [#25936](https://github.com/vllm-project/vllm/pull/25936) | merged | [Bugfix][Model]fix ernie45 moe gate&bias dtype to float32 | `vllm/model_executor/models/ernie45_vl_moe.py`, `vllm/model_executor/models/ernie45_moe.py` |
| 2025-07-28 | [#21735](https://github.com/vllm-project/vllm/pull/21735) | merged | [`Ernie 4.5`] Name Change for Base 0.3B Model | `vllm/model_executor/models/ernie45.py` |

## Per-PR Diff Audit Cards

### PR #51461 - [MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs

- Link: https://github.com/vllm-project/vllm/pull/51461
- Status/date: merged / 2026-08-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/ernie45_vl.py`; associated commits `b2506d62aec7`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-1, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs"; model line: ERNIE 4.5; category: bug fix; main diff: `vllm/model_executor/models/ernie45_vl.py`; technical summary: Covers "[MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs"; the main implementation surface is `vllm/model_executor/models/ernie45_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45_vl.py` modified +3/-1 (4 lines); hunks: -1721,7 +1721,7 @@ def encoder_eager_forward(; -1731,6 +1731,8 @@ def postprocess_encoder_output(; symbols: encoder_eager_forward, postprocess_encoder_output, touching `encoder_eager_forward, postprocess_encoder_output`.
- Code diff details:
  - `vllm/model_executor/models/ernie45_vl.py` modified +3/-1 (4 lines); hunks: -1721,7 +1721,7 @@ def encoder_eager_forward(; -1731,6 +1731,8 @@ def postprocess_encoder_output(; symbols: encoder_eager_forward, postprocess_encoder_output
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45_vl.py
@@ -1721,7 +1721,7 @@ def encoder_eager_forward(
-        output: torch.Tensor,
+        outputs: dict[str, torch.Tensor],
@@ -1731,6 +1731,8 @@ def postprocess_encoder_output(
+        # Ernie only uses the single "default" encoder path.
+        output = outputs["default"]
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45_vl.py` modified +3/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/ernie45_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #45254 - [MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference

- Link: https://github.com/vllm-project/vllm/pull/45254
- Status/date: merged / 2026-08-06
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/ernie45_vl.py`; associated commits `777b01d1a86e`
- Diff scope read: GitHub Pull Request files API returned 4 files, +289/-13, 374 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference"; model line: ERNIE 4.5; category: performance/backend optimization; main diff: `vllm/model_executor/models/ernie45_vl.py`; technical summary: Covers "[MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference"; the main implementation surface is `vllm/model_executor/models/ernie45_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45_vl.py` modified +260/-13 (273 lines); hunks: -77,12 +77,18; -453,13 +459,43 @@ def compute_attn_mask_seqlen(self, cu_seqlens: torch.Tenso...; symbols: compute_attn_mask_seqlen, forward, prepare_encoder_metadata, touching `compute_attn_mask_seqlen, forward, prepare_encoder_metadata`.
- Code diff details:
  - `vllm/model_executor/models/ernie45_vl.py` modified +260/-13 (273 lines); hunks: -77,12 +77,18; -453,13 +459,43 @@ def compute_attn_mask_seqlen(self, cu_seqlens: torch.Tenso...; symbols: compute_attn_mask_seqlen, forward, prepare_encoder_metadata
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45_vl.py
@@ -77,12 +77,18 @@
+    SupportsEncoderCudaGraph,
-from .utils import AutoWeightsLoader, WeightsMapper, maybe_prefix
+from .utils import (
+    AutoWeightsLoader,
+    WeightsMapper,
+    maybe_prefix,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45_vl.py` modified +260/-13
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/generation/test_vit_cudagraph.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46255 - fix(reasoning): guard rfind in ernie45 streaming branch

- Link: https://github.com/vllm-project/vllm/pull/46255
- Status/date: merged / 2026-07-01
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/reasoning/ernie45_reasoning_parser.py`; associated commits `9294dd27eb9c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(reasoning): guard rfind in ernie45 streaming branch"; model line: ERNIE 4.5; category: bug fix; main diff: `vllm/reasoning/ernie45_reasoning_parser.py`; technical summary: Covers "fix(reasoning): guard rfind in ernie45 streaming branch"; the main implementation surface is `vllm/reasoning/ernie45_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-1 (3 lines); hunks: -114,7 +114,8 @@ def extract_reasoning_streaming(; symbols: extract_reasoning_streaming, touching `extract_reasoning_streaming`.
- Code diff details:
  - `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-1 (3 lines); hunks: -114,7 +114,8 @@ def extract_reasoning_streaming(; symbols: extract_reasoning_streaming
- Key code excerpts:

```diff
diff -- vllm/reasoning/ernie45_reasoning_parser.py
@@ -114,7 +114,8 @@ def extract_reasoning_streaming(
-                content = content[:response_end_idx]
+                if response_end_idx != -1:
+                    content = content[:response_end_idx]
```

- Reviewed files:
  - runtime: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `vllm/reasoning/ernie45_reasoning_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #39753 - [Model] Use mm_features for Ernie-4.5 VL M-RoPE

- Link: https://github.com/vllm-project/vllm/pull/39753
- Status/date: merged / 2026-04-14
- Trace source: `git log --name-only -- <model-files>` found it through `tests/model_executor/test_ernie45_vl_mrope.py`, `vllm/model_executor/models/ernie45_vl.py`; associated commits `0008729abfbd`
- Diff scope read: GitHub Pull Request files API returned 2 files, +196/-123, 339 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Use mm_features for Ernie-4.5 VL M-RoPE"; model line: ERNIE 4.5; category: docs/tests/CI; main diff: `vllm/model_executor/models/ernie45_vl.py`, `tests/model_executor/test_ernie45_vl_mrope.py`; technical summary: Covers "[Model] Use mm_features for Ernie-4.5 VL M-RoPE"; the main implementation surface is `vllm/model_executor/models/ernie45_vl.py`, `tests/model_executor/test_ernie45_vl_mrope.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45_vl.py` modified +53/-123 (176 lines); hunks: -23,9 +23,8; -1401,131 +1400,62 @@ def get_mrope_input_positions(; symbols: get_mrope_input_positions, iter_mm_grid_thw, _parse_and_validate_image_input, touching `get_mrope_input_positions, iter_mm_grid_thw, _parse_and_validate_image_input`; `tests/model_executor/test_ernie45_vl_mrope.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: _force_cpu_default_device, DummyConfig, make_model, make_mm_feature, touching `_force_cpu_default_device, DummyConfig, make_model`.
- Code diff details:
  - `vllm/model_executor/models/ernie45_vl.py` modified +53/-123 (176 lines); hunks: -23,9 +23,8; -1401,131 +1400,62 @@ def get_mrope_input_positions(; symbols: get_mrope_input_positions, iter_mm_grid_thw, _parse_and_validate_image_input
  - `tests/model_executor/test_ernie45_vl_mrope.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: _force_cpu_default_device, DummyConfig, make_model, make_mm_feature
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45_vl.py
@@ -23,9 +23,8 @@
-import itertools
-from collections.abc import Callable, Iterable, Mapping, Sequence
+from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
@@ -1401,131 +1400,62 @@ def get_mrope_input_positions(
-        kwargs = MultiModalFeatureSpec.gather_kwargs(
-            mm_features,
diff -- tests/model_executor/test_ernie45_vl_mrope.py
@@ -0,0 +1,143 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from dataclasses import dataclass
+import pytest
+import torch
+from vllm.model_executor.models.ernie45_vl import (
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45_vl.py` modified +53/-123
  - tests: `tests/model_executor/test_ernie45_vl_mrope.py` added +143/-0
- Risk and verification: The diff ships test coverage in `tests/model_executor/test_ernie45_vl_mrope.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27973 - [Model] fix ernie45 reasoning_parser

- Link: https://github.com/vllm-project/vllm/pull/27973
- Status/date: merged / 2025-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/reasoning/ernie45_reasoning_parser.py`; associated commits `43a6acfb7de8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 11 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] fix ernie45 reasoning_parser"; model line: ERNIE 4.5; category: bug fix; main diff: `vllm/reasoning/ernie45_reasoning_parser.py`; technical summary: Covers "[Model] fix ernie45 reasoning_parser"; the main implementation surface is `vllm/reasoning/ernie45_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-2 (4 lines); hunks: -36,8 +36,8 @@ def end_token(self) -> str:; symbols: end_token, __init__, touching `end_token, __init__`.
- Code diff details:
  - `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-2 (4 lines); hunks: -36,8 +36,8 @@ def end_token(self) -> str:; symbols: end_token, __init__
- Key code excerpts:

```diff
diff -- vllm/reasoning/ernie45_reasoning_parser.py
@@ -36,8 +36,8 @@ def end_token(self) -> str:
-    def __init__(self, tokenizer: PreTrainedTokenizerBase):
-        super().__init__(tokenizer)
+    def __init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
+        super().__init__(tokenizer, *args, **kwargs)
```

- Reviewed files:
  - runtime: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `vllm/reasoning/ernie45_reasoning_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27316 - [Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple

- Link: https://github.com/vllm-project/vllm/pull/27316
- Status/date: merged / 2025-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/ernie45_moe.py`; associated commits `63b22e0dbb90`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-0, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple"; model line: ERNIE 4.5; category: bug fix; main diff: `vllm/model_executor/models/ernie45_moe.py`; technical summary: Covers "[Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple"; the main implementation surface is `vllm/model_executor/models/ernie45_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45_moe.py` modified +2/-0 (2 lines); hunks: -215,6 +215,8 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/ernie45_moe.py` modified +2/-0 (2 lines); hunks: -215,6 +215,8 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45_moe.py
@@ -215,6 +215,8 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
+        else:
+            final_hidden_states = final_hidden_states[1]
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45_moe.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/ernie45_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26885 - [Model][Bugfix] fix ernie45 vl run failed from shared experts optimization

- Link: https://github.com/vllm-project/vllm/pull/26885
- Status/date: merged / 2025-10-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/ernie45_vl_moe.py`; associated commits `e51928793e10`
- Diff scope read: GitHub Pull Request files API returned 1 files, +22/-5, 55 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][Bugfix] fix ernie45 vl run failed from shared experts optimization"; model line: ERNIE 4.5; category: bug fix; main diff: `vllm/model_executor/models/ernie45_vl_moe.py`; technical summary: Covers "[Model][Bugfix] fix ernie45 vl run failed from shared experts optimization"; the main implementation surface is `vllm/model_executor/models/ernie45_vl_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45_vl_moe.py` modified +22/-5 (27 lines); hunks: -341,7 +341,10 @@ def forward(; -353,16 +356,26 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/ernie45_vl_moe.py` modified +22/-5 (27 lines); hunks: -341,7 +341,10 @@ def forward(; -353,16 +356,26 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45_vl_moe.py
@@ -341,7 +341,10 @@ def forward(
-            final_hidden_states = torch.zeros_like(hidden_states)
+            final_experts_hidden_states = torch.zeros_like(hidden_states)
+            final_shared_ouput = (
+                torch.zeros_like(hidden_states) if self.has_shared_experts else None
+            )
@@ -353,16 +356,26 @@ def forward(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45_vl_moe.py` modified +22/-5
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/ernie45_vl_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26684 - [Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code

- Link: https://github.com/vllm-project/vllm/pull/26684
- Status/date: merged / 2025-10-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/ernie45_moe.py`; associated commits `01ad27faff35`
- Diff scope read: GitHub Pull Request files API returned 1 files, +22/-12, 71 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code"; model line: ERNIE 4.5; category: bug fix; main diff: `vllm/model_executor/models/ernie45_moe.py`; technical summary: Covers "[Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code"; the main implementation surface is `vllm/model_executor/models/ernie45_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45_moe.py` modified +22/-12 (34 lines); hunks: -23,7 +23,8; -139,10 +140,10 @@ def __init__(; symbols: __init__, load_weights, touching `__init__, load_weights`.
- Code diff details:
  - `vllm/model_executor/models/ernie45_moe.py` modified +22/-12 (34 lines); hunks: -23,7 +23,8; -139,10 +140,10 @@ def __init__(; symbols: __init__, load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45_moe.py
@@ -23,7 +23,8 @@
-from collections.abc import Iterable
+import typing
+from collections.abc import Callable, Iterable
@@ -139,10 +140,10 @@ def __init__(
-        parallel_config = vllm_config.parallel_config
+        eplb_config = vllm_config.parallel_config.eplb_config
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45_moe.py` modified +22/-12
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/ernie45_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25027 - [Model] Add reasoning_parser and tool_parser for Ernie45 thinking

- Link: https://github.com/vllm-project/vllm/pull/25027
- Status/date: merged / 2025-10-13
- Trace source: `git log --name-only -- <model-files>` found it through `tests/reasoning/test_ernie45_reasoning_parser.py`, `vllm/reasoning/ernie45_reasoning_parser.py`; associated commits `782505ed8eb4`
- Diff scope read: GitHub Pull Request files API returned 7 files, +870/-0, 909 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Add reasoning_parser and tool_parser for Ernie45 thinking"; model line: ERNIE 4.5; category: docs/tests/CI; main diff: `vllm/reasoning/ernie45_reasoning_parser.py`, `tests/reasoning/test_ernie45_reasoning_parser.py`; technical summary: Covers "[Model] Add reasoning_parser and tool_parser for Ernie45 thinking"; the main implementation surface is `vllm/reasoning/ernie45_reasoning_parser.py`, `tests/reasoning/test_ernie45_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/reasoning/ernie45_reasoning_parser.py` added +169/-0 (169 lines); hunks: -0,0 +1,169; symbols: Ernie45ReasoningParser, start_token, end_token, __init__, touching `Ernie45ReasoningParser, start_token, end_token`; `tests/reasoning/test_ernie45_reasoning_parser.py` added +124/-0 (124 lines); hunks: -0,0 +1,124; symbols: ernie45_tokenizer, test_reasoning, touching `ernie45_tokenizer, test_reasoning`.
- Code diff details:
  - `vllm/reasoning/ernie45_reasoning_parser.py` added +169/-0 (169 lines); hunks: -0,0 +1,169; symbols: Ernie45ReasoningParser, start_token, end_token, __init__
  - `tests/reasoning/test_ernie45_reasoning_parser.py` added +124/-0 (124 lines); hunks: -0,0 +1,124; symbols: ernie45_tokenizer, test_reasoning
- Key code excerpts:

```diff
diff -- vllm/reasoning/ernie45_reasoning_parser.py
@@ -0,0 +1,169 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Sequence
+from transformers import PreTrainedTokenizerBase
+from vllm.entrypoints.openai.protocol import ChatCompletionRequest, DeltaMessage
+from vllm.logger import init_logger
diff -- tests/reasoning/test_ernie45_reasoning_parser.py
@@ -0,0 +1,124 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from transformers import AutoTokenizer
+from tests.reasoning.utils import run_reasoning_extraction
+from vllm.reasoning import ReasoningParser, ReasoningParserManager
```

- Reviewed files:
  - runtime: `vllm/reasoning/ernie45_reasoning_parser.py` added +169/-0
  - tests: `tests/reasoning/test_ernie45_reasoning_parser.py` added +124/-0
- Risk and verification: The diff ships test coverage in `tests/reasoning/test_ernie45_reasoning_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #25936 - [Bugfix][Model]fix ernie45 moe gate&bias dtype to float32

- Link: https://github.com/vllm-project/vllm/pull/25936
- Status/date: merged / 2025-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/ernie45_moe.py`, `vllm/model_executor/models/ernie45_vl_moe.py`; associated commits `ef6e0e7132ec`
- Diff scope read: GitHub Pull Request files API returned 2 files, +13/-7, 83 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model]fix ernie45 moe gate&bias dtype to float32"; model line: ERNIE 4.5; category: bug fix; main diff: `vllm/model_executor/models/ernie45_vl_moe.py`, `vllm/model_executor/models/ernie45_moe.py`; technical summary: Covers "[Bugfix][Model]fix ernie45 moe gate&bias dtype to float32"; the main implementation surface is `vllm/model_executor/models/ernie45_vl_moe.py`, `vllm/model_executor/models/ernie45_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45_vl_moe.py` modified +10/-5 (15 lines); hunks: -199,7 +199,7 @@ def __init__(; -209,6 +209,7 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`; `vllm/model_executor/models/ernie45_moe.py` modified +3/-2 (5 lines); hunks: -120,11 +120,12 @@ def __init__(; -157,7 +158,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/ernie45_vl_moe.py` modified +10/-5 (15 lines); hunks: -199,7 +199,7 @@ def __init__(; -209,6 +209,7 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/ernie45_moe.py` modified +3/-2 (5 lines); hunks: -120,11 +120,12 @@ def __init__(; -157,7 +158,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45_vl_moe.py
@@ -199,7 +199,7 @@ def __init__(
-            torch.empty(2, config.moe_num_experts[0]))
+            torch.empty(2, config.moe_num_experts[0], dtype=torch.float32))
@@ -209,6 +209,7 @@ def __init__(
+                params_dtype=torch.float32,
@@ -238,6 +239,7 @@ def __init__(
+                params_dtype=torch.float32,
diff -- vllm/model_executor/models/ernie45_moe.py
@@ -120,11 +120,12 @@ def __init__(
+                                     params_dtype=torch.float32,
-            torch.empty(config.moe_num_experts))
+            torch.empty(config.moe_num_experts, dtype=torch.float32))
@@ -157,7 +158,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
-        router_logits, _ = self.gate(hidden_states)
+        router_logits, _ = self.gate(hidden_states.to(dtype=torch.float32))
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45_vl_moe.py` modified +10/-5; `vllm/model_executor/models/ernie45_moe.py` modified +3/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/ernie45_moe.py`, `vllm/model_executor/models/ernie45_vl_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21735 - [`Ernie 4.5`] Name Change for Base 0.3B Model

- Link: https://github.com/vllm-project/vllm/pull/21735
- Status/date: merged / 2025-07-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/ernie45.py`; associated commits `656c24f1b5d8`
- Diff scope read: GitHub Pull Request files API returned 4 files, +8/-8, 51 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[`Ernie 4.5`] Name Change for Base 0.3B Model"; model line: ERNIE 4.5; category: model implementation change; main diff: `vllm/model_executor/models/ernie45.py`; technical summary: Covers "[`Ernie 4.5`] Name Change for Base 0.3B Model"; the main implementation surface is `vllm/model_executor/models/ernie45.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/ernie45.py` modified +1/-1 (2 lines); hunks: -28,7 +28,7; symbols: Ernie4_5_ForCausalLM, Ernie4_5ForCausalLM, __init__, touching `Ernie4_5_ForCausalLM, Ernie4_5ForCausalLM, __init__`.
- Code diff details:
  - `vllm/model_executor/models/ernie45.py` modified +1/-1 (2 lines); hunks: -28,7 +28,7; symbols: Ernie4_5_ForCausalLM, Ernie4_5ForCausalLM, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/ernie45.py
@@ -28,7 +28,7 @@
-class Ernie4_5_ForCausalLM(LlamaForCausalLM):
+class Ernie4_5ForCausalLM(LlamaForCausalLM):
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/ernie45.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
