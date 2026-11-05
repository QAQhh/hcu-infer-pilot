# sglang Step 3.5 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `python/sglang/srt/configs/step3p5.py` | [#18084](https://github.com/sgl-project/sglang/pull/18084) |
| `python/sglang/srt/models/step3p5.py` | [#18084](https://github.com/sgl-project/sglang/pull/18084), [#22076](https://github.com/sgl-project/sglang/pull/22076), [#22773](https://github.com/sgl-project/sglang/pull/22773), [#41082](https://github.com/sgl-project/sglang/pull/41082), [#41198](https://github.com/sgl-project/sglang/pull/41198), [#41437](https://github.com/sgl-project/sglang/pull/41437), [#41754](https://github.com/sgl-project/sglang/pull/41754), [#42302](https://github.com/sgl-project/sglang/pull/42302) |
| `python/sglang/srt/models/step3p5_mtp.py` | [#18084](https://github.com/sgl-project/sglang/pull/18084) |
| `test/registered/e2e/models/test_step3p5_flash_chain_mtp.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 8
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 8
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-02 | [#18084](https://github.com/sgl-project/sglang/pull/18084) | merged | add Step-3.5-Flash model support | `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`, `python/sglang/srt/configs/step3p5.py` |
| 2026-04-04 | [#22076](https://github.com/sgl-project/sglang/pull/22076) | merged | Tiny fix step3.5-flash launch crash | `python/sglang/srt/models/step3p5.py` |
| 2026-04-16 | [#22773](https://github.com/sgl-project/sglang/pull/22773) | merged | [Step3p5] Optimize allreduce in MoE layers | `python/sglang/srt/models/step3p5.py` |
| 2026-09-24 | [#41082](https://github.com/sgl-project/sglang/pull/41082) | merged | [Fix] Step-3.5: stop dense layers from summing their output twice under DP attention | `python/sglang/srt/models/step3p5.py` |
| 2026-09-25 | [#41198](https://github.com/sgl-project/sglang/pull/41198) | merged | [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit | `python/sglang/srt/models/step3p5.py` |
| 2026-09-27 | [#41437](https://github.com/sgl-project/sglang/pull/41437) | merged | [Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit | `python/sglang/srt/models/step3p5.py` |
| 2026-09-30 | [#41754](https://github.com/sgl-project/sglang/pull/41754) | merged | [Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends | `python/sglang/srt/models/step3p5.py` |
| 2026-10-03 | [#42302](https://github.com/sgl-project/sglang/pull/42302) | merged | [Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1 | `python/sglang/srt/models/step3p5.py` |

## Per-PR Diff Audit Cards

### PR #18084 - add Step-3.5-Flash model support

- Link: https://github.com/sgl-project/sglang/pull/18084
- Status/date: merged / 2026-02-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/step3p5.py`, `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`; associated commits `980d2936cd9a`
- Diff scope read: GitHub Pull Request files API returned 15 files, +1557/-12, 1711 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "add Step-3.5-Flash model support"; model line: Step 3.5; category: performance/backend optimization; main diff: `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`, `python/sglang/srt/configs/step3p5.py`; technical summary: Covers "add Step-3.5-Flash model support"; the main implementation surface is `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`, `python/sglang/srt/configs/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` added +1037/-0 (1037 lines); hunks: -0,0 +1,1037; symbols: Step3p5MLP, __init__, forward, Step3p5MoEMLP, touching `Step3p5MLP, __init__, forward`; `python/sglang/srt/models/step3p5_mtp.py` added +336/-0 (336 lines); hunks: -0,0 +1,336; symbols: get_spec_layer_idx_from_weight_name, SharedHead, __init__, forward, touching `get_spec_layer_idx_from_weight_name, SharedHead, __init__`; `python/sglang/srt/configs/step3p5.py` added +97/-0 (97 lines); hunks: -0,0 +1,97; symbols: Step3p5Config, __init__, touching `Step3p5Config, __init__`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` added +1037/-0 (1037 lines); hunks: -0,0 +1,1037; symbols: Step3p5MLP, __init__, forward, Step3p5MoEMLP
  - `python/sglang/srt/models/step3p5_mtp.py` added +336/-0 (336 lines); hunks: -0,0 +1,336; symbols: get_spec_layer_idx_from_weight_name, SharedHead, __init__, forward
  - `python/sglang/srt/configs/step3p5.py` added +97/-0 (97 lines); hunks: -0,0 +1,97; symbols: Step3p5Config, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -0,0 +1,1037 @@
+import logging
+import os
+from typing import Any, Dict, Iterable, Optional, Tuple, Union
+import torch
+import torch.nn.functional as F
+from torch import nn
diff -- python/sglang/srt/models/step3p5_mtp.py
@@ -0,0 +1,336 @@
+import logging
+from collections.abc import Iterable
+from typing import Optional
+import torch
+import torch.nn as nn
+from transformers import PretrainedConfig
diff -- python/sglang/srt/configs/step3p5.py
@@ -0,0 +1,97 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` added +1037/-0; `python/sglang/srt/models/step3p5_mtp.py` added +336/-0; `python/sglang/srt/configs/step3p5.py` added +97/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22076 - Tiny fix step3.5-flash launch crash

- Link: https://github.com/sgl-project/sglang/pull/22076
- Status/date: merged / 2026-04-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/step3p5.py`; associated commits `ef130312434c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-1, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Tiny fix step3.5-flash launch crash"; model line: Step 3.5; category: bug fix; main diff: `python/sglang/srt/models/step3p5.py`; technical summary: Covers "Tiny fix step3.5-flash launch crash"; the main implementation surface is `python/sglang/srt/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` modified +0/-1 (1 lines); hunks: -667,7 +667,6 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` modified +0/-1 (1 lines); hunks: -667,7 +667,6 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -667,7 +667,6 @@ def __init__(
-        self.padding_idx = config.pad_token_id
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +0/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/step3p5.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22773 - [Step3p5] Optimize allreduce in MoE layers

- Link: https://github.com/sgl-project/sglang/pull/22773
- Status/date: merged / 2026-04-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/step3p5.py`; associated commits `b8794baa6d61`
- Diff scope read: GitHub Pull Request files API returned 1 files, +59/-57, 211 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Step3p5] Optimize allreduce in MoE layers"; model line: Step 3.5; category: performance/backend optimization; main diff: `python/sglang/srt/models/step3p5.py`; technical summary: Covers "[Step3p5] Optimize allreduce in MoE layers"; the main implementation surface is `python/sglang/srt/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` modified +59/-57 (116 lines); hunks: -1,5 +1,3; -57,7 +55,6; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` modified +59/-57 (116 lines); hunks: -1,5 +1,3; -57,7 +55,6; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -1,5 +1,3 @@
-import logging
-import os
@@ -57,7 +55,6 @@
-logger = logging.getLogger(__name__)
@@ -69,6 +66,9 @@ def __init__(
+        tp_size: Optional[int] = None,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +59/-57
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/step3p5.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41082 - [Fix] Step-3.5: stop dense layers from summing their output twice under DP attention

- Link: https://github.com/sgl-project/sglang/pull/41082
- Status/date: merged / 2026-09-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/step3p5.py`; associated commits `7c9f74c6e109`
- Diff scope read: GitHub Pull Request files API returned 2 files, +67/-4, 79 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Step-3.5: stop dense layers from summing their output twice under DP attention"; model line: Step 3.5; category: bug fix; main diff: `python/sglang/srt/models/step3p5.py`; technical summary: Covers "[Fix] Step-3.5: stop dense layers from summing their output twice under DP attention"; the main implementation surface is `python/sglang/srt/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` modified +6/-4 (10 lines); hunks: -633,10 +633,12 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` modified +6/-4 (10 lines); hunks: -633,10 +633,12 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -633,10 +633,12 @@ def forward(
-            hidden_states = self.mlp(hidden_states)
-            # Dense MLP uses reduce_results=True, so the output is already
-            # all-reduced.  Do NOT set the fusion flag — otherwise the next
-            # layer would all-reduce again, multiplying values by world_size.
+            # The dense MLP all-reduces its own output unless postprocess
+            # reduce-scatters it; it never leaves the sum to the next layer.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +6/-4
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41198 - [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit

- Link: https://github.com/sgl-project/sglang/pull/41198
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/step3p5.py`; associated commits `b7f6d04a9af1`
- Diff scope read: GitHub Pull Request files API returned 6 files, +50/-219, 402 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit"; model line: Step 3.5; category: model implementation change; main diff: `python/sglang/srt/models/step3p5.py`; technical summary: Covers "[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit"; the main implementation surface is `python/sglang/srt/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` modified +24/-41 (65 lines); hunks: -11,11 +11,7; -609,45 +605,32 @@ def forward(; symbols: forward, Step3p5Model, touching `forward, Step3p5Model`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` modified +24/-41 (65 lines); hunks: -11,11 +11,7; -609,45 +605,32 @@ def forward(; symbols: forward, Step3p5Model
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -11,11 +11,7 @@
-from sglang.srt.layers.communicator import (
-    LayerCommunicator,
-    LayerScatterModes,
-    UnreducedOutput,
-)
+from sglang.srt.layers.communicator import LayerCommunicator, LayerScatterModes
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +24/-41
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41437 - [Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit

- Link: https://github.com/sgl-project/sglang/pull/41437
- Status/date: merged / 2026-09-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/step3p5.py`; associated commits `55d2ee554635`
- Diff scope read: GitHub Pull Request files API returned 3 files, +31/-17, 110 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit"; model line: Step 3.5; category: model implementation change; main diff: `python/sglang/srt/models/step3p5.py`; technical summary: Covers "[Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit"; the main implementation surface is `python/sglang/srt/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` modified +5/-11 (16 lines); hunks: -572,6 +572,9 @@ def __init__(; -618,18 +621,9 @@ def forward(; symbols: __init__, forward, Step3p5Model, touching `__init__, forward, Step3p5Model`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` modified +5/-11 (16 lines); hunks: -572,6 +572,9 @@ def __init__(; -618,18 +621,9 @@ def forward(; symbols: __init__, forward, Step3p5Model
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -572,6 +572,9 @@ def __init__(
+            # The dense MLP all-reduces its own output unless postprocess
+            # reduce-scatters it; it never leaves the sum to the next layer.
+            allow_deferred_ffn_reduction=self.use_moe,
@@ -618,18 +621,9 @@ def forward(
-        # The dense MLP all-reduces its own output unless postprocess
-        # reduce-scatters it; it never leaves the sum to the next layer.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +5/-11
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_last_layer_communicator.py`, `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41754 - [Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends

- Link: https://github.com/sgl-project/sglang/pull/41754
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/step3p5.py`; associated commits `9ee065e49a12`
- Diff scope read: GitHub Pull Request files API returned 1 files, +33/-19, 135 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends"; model line: Step 3.5; category: bug fix; main diff: `python/sglang/srt/models/step3p5.py`; technical summary: Covers "[Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends"; the main implementation surface is `python/sglang/srt/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` modified +33/-19 (52 lines); hunks: -4,9 +4,6; -32,6 +29,7; symbols: forward, get_moe_weights, forward_normal, touching `forward, get_moe_weights, forward_normal`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` modified +33/-19 (52 lines); hunks: -4,9 +4,6; -32,6 +29,7; symbols: forward, get_moe_weights, forward_normal
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -4,9 +4,6 @@
-from sglang.srt.distributed import (
-    tensor_model_parallel_all_reduce,
-)
@@ -32,6 +29,7 @@
+    should_use_flashinfer_cutlass_moe_fp4_allgather,
@@ -50,7 +48,7 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +33/-19
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/step3p5.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #42302 - [Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1

- Link: https://github.com/sgl-project/sglang/pull/42302
- Status/date: merged / 2026-10-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/step3p5.py`; associated commits `be20e7453cc8`
- Diff scope read: GitHub Pull Request files API returned 2 files, +18/-8, 62 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1"; model line: Step 3.5; category: bug fix; main diff: `python/sglang/srt/models/step3p5.py`; technical summary: Covers "[Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1"; the main implementation surface is `python/sglang/srt/models/step3p5.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/step3p5.py` modified +10/-2 (12 lines); hunks: -236,7 +236,13 @@ def forward_deepep(; -252,8 +258,10 @@ def forward_deepep(; symbols: forward_deepep, touching `forward_deepep`.
- Code diff details:
  - `python/sglang/srt/models/step3p5.py` modified +10/-2 (12 lines); hunks: -236,7 +236,13 @@ def forward_deepep(; -252,8 +258,10 @@ def forward_deepep(; symbols: forward_deepep
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -236,7 +236,13 @@ def forward_deepep(
-            router_logits, _ = self.gate(hidden_states)
+            if self.need_fp32_gate:
+                router_logits = torch.matmul(
+                    hidden_states.to(torch.float32),
+                    self.gate.weight.t().to(torch.float32),
+                )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +10/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/sarvam_moe.py`, `python/sglang/srt/models/step3p5.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
