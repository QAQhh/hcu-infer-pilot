# sglang ERNIE 4.5 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` | [#42303](https://github.com/sgl-project/sglang/pull/42303) |
| `python/sglang/srt/models/ernie45_moe_vl.py` | [#42303](https://github.com/sgl-project/sglang/pull/42303), [#42304](https://github.com/sgl-project/sglang/pull/42304) |
| `python/sglang/srt/models/ernie45_vl.py` | no direct PR-number commit |
| `python/sglang/srt/multimodal/processors/ernie45_vl.py` | no direct PR-number commit |
| `test/manual/models/test_ernie45_vl_visual_mask.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 2
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 2
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-10-03 | [#42303](https://github.com/sgl-project/sglang/pull/42303) | merged | [Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues | `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` |
| 2026-10-03 | [#42304](https://github.com/sgl-project/sglang/pull/42304) | merged | [Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries | `python/sglang/srt/models/ernie45_moe_vl.py` |

## Per-PR Diff Audit Cards

### PR #42303 - [Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues

- Link: https://github.com/sgl-project/sglang/pull/42303
- Status/date: merged / 2026-10-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`, `python/sglang/srt/models/ernie45_moe_vl.py`; associated commits `f89ead192f3c`
- Diff scope read: GitHub Pull Request files API returned 8 files, +65/-10, 168 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues"; model line: ERNIE 4.5; category: bug fix; main diff: `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`; technical summary: Covers "[Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues"; the main implementation surface is `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/ernie45_moe_vl.py` modified +0/-2 (2 lines); hunks: -25,7 +25,6; -479,7 +478,6 @@ def __init__(; symbols: __init__, touching `__init__`; `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` added +19/-0 (19 lines); hunks: -0,0 +1,19; symbols: _ernie45_vl_overrides, touching `_ernie45_vl_overrides`.
- Code diff details:
  - `python/sglang/srt/models/ernie45_moe_vl.py` modified +0/-2 (2 lines); hunks: -25,7 +25,6; -479,7 +478,6 @@ def __init__(; symbols: __init__
  - `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` added +19/-0 (19 lines); hunks: -0,0 +1,19; symbols: _ernie45_vl_overrides
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/ernie45_moe_vl.py
@@ -25,7 +25,6 @@
-from sglang.srt.layers.dp_attention import is_dp_attention_enabled
@@ -479,7 +478,6 @@ def __init__(
-                enable_tp=not is_dp_attention_enabled(),
diff -- python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py
@@ -0,0 +1,19 @@
+"""Config-time override declarations for ernie45_vl."""
+from typing import Any
+from sglang.srt.arg_groups.model_override_base import (
+    _register_for,
+    resolving_view,
+)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/ernie45_moe_vl.py` modified +0/-2; `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` added +19/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #42304 - [Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries

- Link: https://github.com/sgl-project/sglang/pull/42304
- Status/date: merged / 2026-10-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/ernie45_moe_vl.py`; associated commits `2fa17a64671b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +126/-100, 403 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries"; model line: ERNIE 4.5; category: model implementation change; main diff: `python/sglang/srt/models/ernie45_moe_vl.py`; technical summary: Covers "[Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries"; the main implementation surface is `python/sglang/srt/models/ernie45_moe_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/ernie45_moe_vl.py` modified +66/-58 (124 lines); hunks: -16,15 +16,18; -107,6 +110,7 @@ def __init__(; symbols: __init__, forward, _is_moe_layer, Ernie4_5_VLMoeDecoderLayer, touching `__init__, forward, _is_moe_layer`.
- Code diff details:
  - `python/sglang/srt/models/ernie45_moe_vl.py` modified +66/-58 (124 lines); hunks: -16,15 +16,18; -107,6 +110,7 @@ def __init__(; symbols: __init__, forward, _is_moe_layer, Ernie4_5_VLMoeDecoderLayer
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/ernie45_moe_vl.py
@@ -16,15 +16,18 @@
-from typing import Any, Dict, Optional, Tuple, Union
+from typing import Any, Dict, Optional, Union
-from sglang.srt.distributed import (
-    tensor_model_parallel_all_reduce,
+from sglang.srt.layers.layer_boundary import (
+    declare_attn,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/ernie45_moe_vl.py` modified +66/-58
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/models/exaone_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
