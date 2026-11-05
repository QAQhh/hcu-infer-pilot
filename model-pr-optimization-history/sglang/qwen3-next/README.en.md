# sglang Qwen3 Next Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/qwen3_next_80b_a3b_instruct.mdx` | no direct PR-number commit |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/qwen3_next_80b_a3b_instruct.mdx` | no direct PR-number commit |
| `python/sglang/srt/configs/qwen3_next.py` | [#10233](https://github.com/sgl-project/sglang/pull/10233), [#11585](https://github.com/sgl-project/sglang/pull/11585), [#12525](https://github.com/sgl-project/sglang/pull/12525) |
| `python/sglang/srt/models/qwen3_next.py` | [#10233](https://github.com/sgl-project/sglang/pull/10233), [#10322](https://github.com/sgl-project/sglang/pull/10322), [#10379](https://github.com/sgl-project/sglang/pull/10379), [#10622](https://github.com/sgl-project/sglang/pull/10622), [#11969](https://github.com/sgl-project/sglang/pull/11969), [#12525](https://github.com/sgl-project/sglang/pull/12525), [#13081](https://github.com/sgl-project/sglang/pull/13081), [#14607](https://github.com/sgl-project/sglang/pull/14607), [#16164](https://github.com/sgl-project/sglang/pull/16164), [#17016](https://github.com/sgl-project/sglang/pull/17016), [#17373](https://github.com/sgl-project/sglang/pull/17373), [#17613](https://github.com/sgl-project/sglang/pull/17613), ... (24 total) |
| `python/sglang/srt/models/qwen3_next_mtp.py` | [#10233](https://github.com/sgl-project/sglang/pull/10233), [#10322](https://github.com/sgl-project/sglang/pull/10322), [#10392](https://github.com/sgl-project/sglang/pull/10392), [#26204](https://github.com/sgl-project/sglang/pull/26204) |
| `test/manual/4-gpu-models/test_qwen3_next_models.py` | no direct PR-number commit |
| `test/manual/4-gpu-models/test_qwen3_next_models_mtp_archived.py` | no direct PR-number commit |
| `test/registered/attention/test_qwen3_next_deterministic.py` | no direct PR-number commit |
| `test/registered/e2e/models/test_qwen3_next_models.py` | no direct PR-number commit |
| `test/registered/e2e/models/test_qwen3_next_models_extra.py` | no direct PR-number commit |
| `test/registered/e2e/models/test_qwen3_next_models_mtp.py` | no direct PR-number commit |
| `test/registered/npu/accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py` | no direct PR-number commit |
| `test/registered/npu/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_next.py` | no direct PR-number commit |
| `test/registered/npu/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_next.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 26
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 26
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-09-11 | [#10233](https://github.com/sgl-project/sglang/pull/10233) | merged | Qwen3-Next support | `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py` |
| 2025-09-11 | [#10322](https://github.com/sgl-project/sglang/pull/10322) | merged | [bugfix] fix norm type error in qwen3_next model | `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py` |
| 2025-09-12 | [#10379](https://github.com/sgl-project/sglang/pull/10379) | merged | Support Qwen3-Next on Ascend NPU | `python/sglang/srt/models/qwen3_next.py` |
| 2025-09-13 | [#10392](https://github.com/sgl-project/sglang/pull/10392) | merged | [Fix] Support qwen3-next MTP+DP | `python/sglang/srt/models/qwen3_next_mtp.py` |
| 2025-09-18 | [#10622](https://github.com/sgl-project/sglang/pull/10622) | merged | support qwen3-next-fp8 deepep | `python/sglang/srt/models/qwen3_next.py` |
| 2025-10-15 | [#11585](https://github.com/sgl-project/sglang/pull/11585) | merged | Clean up some Qwen3-Next and deterministic code | `python/sglang/srt/configs/qwen3_next.py` |
| 2025-10-30 | [#11969](https://github.com/sgl-project/sglang/pull/11969) | merged | [NPU] bugfix for Qwen3-Next and performance update | `python/sglang/srt/models/qwen3_next.py` |
| 2025-11-25 | [#13081](https://github.com/sgl-project/sglang/pull/13081) | merged | Support piecewise cuda graph for Qwen3-next | `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-03 | [#16164](https://github.com/sgl-project/sglang/pull/16164) | merged | [NPU] Adapt qwen3-next W8A8 on NPU | `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-16 | [#17016](https://github.com/sgl-project/sglang/pull/17016) | merged | [bugfix] fix qwen3-next alt_stream none issue | `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-22 | [#17373](https://github.com/sgl-project/sglang/pull/17373) | merged | refactor Qwen3-Next with a new RadixLinearAttention | `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-30 | [#12525](https://github.com/sgl-project/sglang/pull/12525) | merged | [CPU] Optimize Qwen3-next model on CPU | `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py` |
| 2026-02-01 | [#14607](https://github.com/sgl-project/sglang/pull/14607) | merged | support qwen3-next eagle3 | `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-14 | [#17613](https://github.com/sgl-project/sglang/pull/17613) | merged | [Perf] refactor piecewise cuda graph support of Qwen3-Next | `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-22 | [#18917](https://github.com/sgl-project/sglang/pull/18917) | merged | [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill | `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-27 | [#19434](https://github.com/sgl-project/sglang/pull/19434) | merged | [Qwen3-Next] Support gdn fused_rms_norm_gated | `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-28 | [#17627](https://github.com/sgl-project/sglang/pull/17627) | merged | [feat] Support nvfp4 quantized model of Qwen3-Next | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-20 | [#19321](https://github.com/sgl-project/sglang/pull/19321) | merged | [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-26 | [#21313](https://github.com/sgl-project/sglang/pull/21313) | merged | bugfix for weight loading for qwen3-next | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-26 | [#21496](https://github.com/sgl-project/sglang/pull/21496) | merged | Revert "bugfix for weight loading for qwen3-next" | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-30 | [#21662](https://github.com/sgl-project/sglang/pull/21662) | merged | [Fix] Fix weight_loader property assignment for qwen3-next FP8 models | `python/sglang/srt/models/qwen3_next.py` |
| 2026-04-27 | [#21698](https://github.com/sgl-project/sglang/pull/21698) | merged | [npu]fix: qwen3-next w8a8 precision bugs | `python/sglang/srt/models/qwen3_next.py` |
| 2026-04-29 | [#23619](https://github.com/sgl-project/sglang/pull/23619) | merged | Enable Qwen3-Next MoE all-reduce fusion | `python/sglang/srt/models/qwen3_next.py` |
| 2026-05-20 | [#23925](https://github.com/sgl-project/sglang/pull/23925) | merged | [NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next | `python/sglang/srt/models/qwen3_next.py` |
| 2026-06-11 | [#26204](https://github.com/sgl-project/sglang/pull/26204) | merged | Optimize Qwen3 Next FP8 MoE on H200 | `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py` |
| 2026-10-27 | [#45739](https://github.com/sgl-project/sglang/pull/45739) | merged | [Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950 | `python/sglang/srt/models/qwen3_next.py` |

## Per-PR Diff Audit Cards

### PR #10233 - Qwen3-Next support

- Link: https://github.com/sgl-project/sglang/pull/10233
- Status/date: merged / 2025-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`; associated commits `30c6e1f56967`
- Diff scope read: GitHub Pull Request files API returned 19 files, +3224/-8, 3452 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Qwen3-Next support"; model line: Qwen3 Next; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`; technical summary: Covers "Qwen3-Next support"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` added +1072/-0 (1072 lines); hunks: -0,0 +1,1072; symbols: fused_qkvzba_split_reshape_cat_kernel, fused_qkvzba_split_reshape_cat, fused_gdn_gating_kernel, fused_gdn_gating, touching `fused_qkvzba_split_reshape_cat_kernel, fused_qkvzba_split_reshape_cat, fused_gdn_gating_kernel`; `python/sglang/srt/configs/qwen3_next.py` added +326/-0 (326 lines); hunks: -0,0 +1,326; symbols: HybridLayerType, Qwen3NextConfig, to, __init__, touching `HybridLayerType, Qwen3NextConfig, to`; `python/sglang/srt/models/qwen3_next_mtp.py` added +117/-0 (117 lines); hunks: -0,0 +1,117; symbols: Qwen3NextForCausalLMMTP, __init__, forward, load_weights, touching `Qwen3NextForCausalLMMTP, __init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` added +1072/-0 (1072 lines); hunks: -0,0 +1,1072; symbols: fused_qkvzba_split_reshape_cat_kernel, fused_qkvzba_split_reshape_cat, fused_gdn_gating_kernel, fused_gdn_gating
  - `python/sglang/srt/configs/qwen3_next.py` added +326/-0 (326 lines); hunks: -0,0 +1,326; symbols: HybridLayerType, Qwen3NextConfig, to, __init__
  - `python/sglang/srt/models/qwen3_next_mtp.py` added +117/-0 (117 lines); hunks: -0,0 +1,117; symbols: Qwen3NextForCausalLMMTP, __init__, forward, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -0,0 +1,1072 @@
+import enum
+import logging
+from typing import Any, Dict, Iterable, Optional, Set, Tuple
+import torch
+import torch.nn.functional as F
+from torch import nn
diff -- python/sglang/srt/configs/qwen3_next.py
@@ -0,0 +1,326 @@
+# coding=utf-8
+# Copyright 2024 The Qwen team, Alibaba Group and the HuggingFace Inc. team. All rights reserved.
+#
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
diff -- python/sglang/srt/models/qwen3_next_mtp.py
@@ -0,0 +1,117 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` added +1072/-0; `python/sglang/srt/configs/qwen3_next.py` added +326/-0; `python/sglang/srt/models/qwen3_next_mtp.py` added +117/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10322 - [bugfix] fix norm type error in qwen3_next model

- Link: https://github.com/sgl-project/sglang/pull/10322
- Status/date: merged / 2025-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`; associated commits `4a0e0be2a2b4`
- Diff scope read: GitHub Pull Request files API returned 2 files, +10/-51, 89 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[bugfix] fix norm type error in qwen3_next model"; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`; technical summary: Covers "[bugfix] fix norm type error in qwen3_next model"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +9/-42 (51 lines); hunks: -518,24 +518,10 @@ def __init__(; -685,23 +671,10 @@ def __init__(; symbols: __init__, get_layer, forward, touching `__init__, get_layer, forward`; `python/sglang/srt/models/qwen3_next_mtp.py` modified +1/-9 (10 lines); hunks: -54,15 +54,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +9/-42 (51 lines); hunks: -518,24 +518,10 @@ def __init__(; -685,23 +671,10 @@ def __init__(; symbols: __init__, get_layer, forward
  - `python/sglang/srt/models/qwen3_next_mtp.py` modified +1/-9 (10 lines); hunks: -54,15 +54,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -518,24 +518,10 @@ def __init__(
-        if getattr(
-            config, "use_gemma_rms_norm", getattr(config, "apply_layernorm_1p", False)
-        ):
-            logger.warning_once(
-                "Using Gemma RMSNorm for input normalization and post attn normalization."
-            )
diff -- python/sglang/srt/models/qwen3_next_mtp.py
@@ -54,15 +54,7 @@ def __init__(
-        if getattr(
-            config, "use_gemma_rms_norm", getattr(config, "apply_layernorm_1p", False)
-        ):
-            logger.warning_once(
-                "Using Gemma RMSNorm for input normalization and post attn normalization."
-            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +9/-42; `python/sglang/srt/models/qwen3_next_mtp.py` modified +1/-9
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10379 - Support Qwen3-Next on Ascend NPU

- Link: https://github.com/sgl-project/sglang/pull/10379
- Status/date: merged / 2025-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `16cd550c8554`
- Diff scope read: GitHub Pull Request files API returned 10 files, +79/-26, 281 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support Qwen3-Next on Ascend NPU"; model line: Qwen3 Next; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "Support Qwen3-Next on Ascend NPU"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +6/-3 (9 lines); hunks: -46,10 +46,11; -327,7 +328,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, forward, touching `__init__, fix_query_key_value_ordering, _forward_input_proj`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +6/-3 (9 lines); hunks: -46,10 +46,11; -327,7 +328,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -46,10 +46,11 @@
-from sglang.srt.utils import add_prefix, is_cuda, make_layers, set_weight_attrs
+from sglang.srt.utils import add_prefix, is_cuda, is_npu, make_layers, set_weight_attrs
+_is_npu = is_npu()
@@ -327,7 +328,7 @@ def __init__(
-            device=torch.cuda.current_device(),
+            device=torch.get_device_module().current_device(),
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +6/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10392 - [Fix] Support qwen3-next MTP+DP

- Link: https://github.com/sgl-project/sglang/pull/10392
- Status/date: merged / 2025-09-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next_mtp.py`; associated commits `9752861002d7`
- Diff scope read: GitHub Pull Request files API returned 4 files, +29/-18, 120 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Support qwen3-next MTP+DP"; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next_mtp.py`; technical summary: Covers "[Fix] Support qwen3-next MTP+DP"; the main implementation surface is `python/sglang/srt/models/qwen3_next_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next_mtp.py` modified +5/-2 (7 lines); hunks: -85,8 +85,11 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next_mtp.py` modified +5/-2 (7 lines); hunks: -85,8 +85,11 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next_mtp.py
@@ -85,8 +85,11 @@ def forward(
-        input_embeds = self.pre_fc_norm_embedding(input_embeds)
-        hidden_states = self.pre_fc_norm_hidden(forward_batch.spec_info.hidden_states)
+        hidden_states = forward_batch.spec_info.hidden_states
+        # Some idle batch has 0 batch size. GemmaRMSNorm.forward would fail due to bs=0.
+        if not forward_batch.forward_mode.is_idle():
+            input_embeds = self.pre_fc_norm_embedding(input_embeds)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next_mtp.py` modified +5/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/mem_cache/memory_pool.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10622 - support qwen3-next-fp8 deepep

- Link: https://github.com/sgl-project/sglang/pull/10622
- Status/date: merged / 2025-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `1344ebc8333d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +93/-9, 204 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support qwen3-next-fp8 deepep"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "support qwen3-next-fp8 deepep"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +29/-8 (37 lines); hunks: -13,6 +13,7; -46,7 +47,14; symbols: forward, __init__, routed_experts_weights_of_layer, touching `forward, __init__, routed_experts_weights_of_layer`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +29/-8 (37 lines); hunks: -13,6 +13,7; -46,7 +47,14; symbols: forward, __init__, routed_experts_weights_of_layer
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -13,6 +13,7 @@
+from sglang.srt.eplb.expert_distribution import get_global_expert_distribution_recorder
@@ -46,7 +47,14 @@
-from sglang.srt.utils import add_prefix, is_cuda, is_npu, make_layers, set_weight_attrs
+from sglang.srt.utils import (
+    LazyValue,
+    add_prefix,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +29/-8
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11585 - Clean up some Qwen3-Next and deterministic code

- Link: https://github.com/sgl-project/sglang/pull/11585
- Status/date: merged / 2025-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_next.py`; associated commits `6b143d62a297`
- Diff scope read: GitHub Pull Request files API returned 4 files, +1/-15, 47 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Clean up some Qwen3-Next and deterministic code"; model line: Qwen3 Next; category: model implementation change; main diff: `python/sglang/srt/configs/qwen3_next.py`; technical summary: Covers "Clean up some Qwen3-Next and deterministic code"; the main implementation surface is `python/sglang/srt/configs/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/configs/qwen3_next.py` modified +0/-3 (3 lines); hunks: -27,12 +27,9; symbols: HybridLayerType, Qwen3NextConfig, touching `HybridLayerType, Qwen3NextConfig`.
- Code diff details:
  - `python/sglang/srt/configs/qwen3_next.py` modified +0/-3 (3 lines); hunks: -27,12 +27,9; symbols: HybridLayerType, Qwen3NextConfig
- Key code excerpts:

```diff
diff -- python/sglang/srt/configs/qwen3_next.py
@@ -27,12 +27,9 @@
-# NOTE: HybridLayerType
-    swa_attention = "swa_attention"
-    mamba2 = "mamba"
```

- Reviewed files:
  - runtime: `python/sglang/srt/configs/qwen3_next.py` modified +0/-3
- Risk and verification: The diff ships test coverage in `python/sglang/test/test_deterministic.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #11969 - [NPU] bugfix for Qwen3-Next and performance update

- Link: https://github.com/sgl-project/sglang/pull/11969
- Status/date: merged / 2025-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `cafebef1546e`
- Diff scope read: GitHub Pull Request files API returned 7 files, +68/-21, 162 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] bugfix for Qwen3-Next and performance update"; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[NPU] bugfix for Qwen3-Next and performance update"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -478,6 +478,13 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -478,6 +478,13 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -478,6 +478,13 @@ def forward(
+        # Add padding for DP-Attn
+        if is_dp_attention_enabled():
+            core_attn_out_pad = torch.zeros_like(z)
+            core_attn_out_pad[: core_attn_out.shape[0], :] = core_attn_out
+            core_attn_out = core_attn_out_pad
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +7/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/moe/topk.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13081 - Support piecewise cuda graph for Qwen3-next

- Link: https://github.com/sgl-project/sglang/pull/13081
- Status/date: merged / 2025-11-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `d64bf6c6ce70`
- Diff scope read: GitHub Pull Request files API returned 6 files, +112/-3, 191 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support piecewise cuda graph for Qwen3-next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "Support piecewise cuda graph for Qwen3-next"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +62/-1 (63 lines); hunks: -5,6 +5,7; -53,9 +54,13; symbols: fused_qkvzba_split_reshape_cat_kernel, fix_query_key_value_ordering, _forward_input_proj, forward, touching `fused_qkvzba_split_reshape_cat_kernel, fix_query_key_value_ordering, _forward_input_proj`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +62/-1 (63 lines); hunks: -5,6 +5,7; -53,9 +54,13; symbols: fused_qkvzba_split_reshape_cat_kernel, fix_query_key_value_ordering, _forward_input_proj, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -5,6 +5,7 @@
+from sglang.srt.compilation.piecewise_context_manager import get_forward_context
@@ -53,9 +54,13 @@
+from sglang.srt.compilation.piecewise_context_manager import get_forward_context
+from sglang.srt.utils import direct_register_custom_op
@@ -349,7 +354,11 @@ def fix_query_key_value_ordering(self, mixed_qkvz, mixed_ba):
-        DUAL_STREAM_TOKEN_THRESHOLD = 1024 if not _is_npu else 0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +62/-1
- Risk and verification: The diff ships test coverage in `test/srt/models/test_qwen3_next_models.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #16164 - [NPU] Adapt qwen3-next W8A8 on NPU

- Link: https://github.com/sgl-project/sglang/pull/16164
- Status/date: merged / 2026-01-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `6bc5a52fd2d4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +18/-5, 121 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Adapt qwen3-next W8A8 on NPU"; model line: Qwen3 Next; category: model implementation change; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[NPU] Adapt qwen3-next W8A8 on NPU"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +18/-5 (23 lines); hunks: -202,6 +202,7 @@ def __init__(; -229,6 +230,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, touching `__init__, fix_query_key_value_ordering`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +18/-5 (23 lines); hunks: -202,6 +202,7 @@ def __init__(; -229,6 +230,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -202,6 +202,7 @@ def __init__(
+        prefix: str = "",
@@ -229,6 +230,7 @@ def __init__(
+            prefix=add_prefix("conv1d", prefix),
@@ -241,14 +243,16 @@ def __init__(
+            prefix=add_prefix("in_proj_qkvz", prefix),
-            quant_config=None,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +18/-5
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17016 - [bugfix] fix qwen3-next alt_stream none issue

- Link: https://github.com/sgl-project/sglang/pull/17016
- Status/date: merged / 2026-01-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `6f10e17b4a68`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[bugfix] fix qwen3-next alt_stream none issue"; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[bugfix] fix qwen3-next alt_stream none issue"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +5/-1 (6 lines); hunks: -358,7 +358,11 @@ def _forward_input_proj(self, hidden_states: torch.Tensor):; symbols: _forward_input_proj, touching `_forward_input_proj`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +5/-1 (6 lines); hunks: -358,7 +358,11 @@ def _forward_input_proj(self, hidden_states: torch.Tensor):; symbols: _forward_input_proj
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -358,7 +358,11 @@ def _forward_input_proj(self, hidden_states: torch.Tensor):
-        if seq_len < DUAL_STREAM_TOKEN_THRESHOLD:
+        if (
+            seq_len < DUAL_STREAM_TOKEN_THRESHOLD
+            and self.alt_stream is not None
+            and get_is_capture_mode()
+        ):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17373 - refactor Qwen3-Next with a new RadixLinearAttention

- Link: https://github.com/sgl-project/sglang/pull/17373
- Status/date: merged / 2026-01-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `419bbcee10a5`
- Diff scope read: GitHub Pull Request files API returned 3 files, +200/-106, 444 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "refactor Qwen3-Next with a new RadixLinearAttention"; model line: Qwen3 Next; category: model implementation change; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "refactor Qwen3-Next with a new RadixLinearAttention"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +21/-37 (58 lines); hunks: -29,6 +29,7; -60,8 +61,6; symbols: fused_qkvzba_split_reshape_cat_kernel, __init__, fix_query_key_value_ordering, forward, touching `fused_qkvzba_split_reshape_cat_kernel, __init__, fix_query_key_value_ordering`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +21/-37 (58 lines); hunks: -29,6 +29,7; -60,8 +61,6; symbols: fused_qkvzba_split_reshape_cat_kernel, __init__, fix_query_key_value_ordering, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -29,6 +29,7 @@
+from sglang.srt.layers.radix_linear_attention import RadixLinearAttention
@@ -60,8 +61,6 @@
-from sglang.srt.compilation.piecewise_context_manager import get_forward_context
@@ -305,6 +304,20 @@ def __init__(
+        self.linear_attn = RadixLinearAttention(
+            layer_id=layer_id,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +21/-37
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12525 - [CPU] Optimize Qwen3-next model on CPU

- Link: https://github.com/sgl-project/sglang/pull/12525
- Status/date: merged / 2026-01-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next.py`; associated commits `336dc4579e94`
- Diff scope read: GitHub Pull Request files API returned 13 files, +366/-41, 685 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CPU] Optimize Qwen3-next model on CPU"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`; technical summary: Covers "[CPU] Optimize Qwen3-next model on CPU"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +31/-5 (36 lines); hunks: -46,6 +46,8; -56,6 +58,8; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, _forward, touching `__init__, fix_query_key_value_ordering, _forward_input_proj`; `python/sglang/srt/configs/qwen3_next.py` modified +7/-0 (7 lines); hunks: -20,8 +20,11; -276,6 +279,10 @@ def full_attention_layer_ids(self):; symbols: HybridLayerType, full_attention_layer_ids, mamba2_cache_params, touching `HybridLayerType, full_attention_layer_ids, mamba2_cache_params`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +31/-5 (36 lines); hunks: -46,6 +46,8; -56,6 +58,8; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, _forward
  - `python/sglang/srt/configs/qwen3_next.py` modified +7/-0 (7 lines); hunks: -20,8 +20,11; -276,6 +279,10 @@ def full_attention_layer_ids(self):; symbols: HybridLayerType, full_attention_layer_ids, mamba2_cache_params
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -46,6 +46,8 @@
+    cpu_has_amx_support,
+    is_cpu,
@@ -56,6 +58,8 @@
+_is_cpu = is_cpu()
+_is_amx_available = cpu_has_amx_support()
@@ -209,8 +213,16 @@ def __init__(
diff -- python/sglang/srt/configs/qwen3_next.py
@@ -20,8 +20,11 @@
+from sglang.srt.configs.update_config import adjust_tp_num_heads_if_necessary
+from sglang.srt.utils import is_cpu
+_is_cpu = is_cpu()
@@ -276,6 +279,10 @@ def full_attention_layer_ids(self):
+        if _is_cpu:
+            world_size = get_attention_tp_size()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +31/-5; `python/sglang/srt/configs/qwen3_next.py` modified +7/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/layers/amx_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14607 - support qwen3-next eagle3

- Link: https://github.com/sgl-project/sglang/pull/14607
- Status/date: merged / 2026-02-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `3ca29dffc72a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +73/-6, 156 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support qwen3-next eagle3"; model line: Qwen3 Next; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "support qwen3-next eagle3"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +73/-6 (79 lines); hunks: -531,12 +531,18 @@ def forward(; -753,10 +759,16 @@ def forward(; symbols: forward, get_layer, set_eagle3_layers_to_capture, touching `forward, get_layer, set_eagle3_layers_to_capture`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +73/-6 (79 lines); hunks: -531,12 +531,18 @@ def forward(; -753,10 +759,16 @@ def forward(; symbols: forward, get_layer, set_eagle3_layers_to_capture
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -531,12 +531,18 @@ def forward(
+        captured_last_layer_outputs: Optional[list[torch.Tensor]] = None,
-        hidden_states, residual = self.layer_communicator.prepare_attn(
-            hidden_states, residual, forward_batch
+        hidden_states, residual = (
+            self.layer_communicator.prepare_attn_and_capture_last_layer_outputs(
+                hidden_states,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +73/-6
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17613 - [Perf] refactor piecewise cuda graph support of Qwen3-Next

- Link: https://github.com/sgl-project/sglang/pull/17613
- Status/date: merged / 2026-02-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `8be18c655d0f`
- Diff scope read: GitHub Pull Request files API returned 5 files, +80/-34, 196 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] refactor piecewise cuda graph support of Qwen3-Next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[Perf] refactor piecewise cuda graph support of Qwen3-Next"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +2/-19 (21 lines); hunks: -316,7 +316,7 @@ def __init__(; -405,23 +405,6 @@ def forward(; symbols: __init__, forward, _forward, touching `__init__, forward, _forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +2/-19 (21 lines); hunks: -316,7 +316,7 @@ def __init__(; -405,23 +405,6 @@ def forward(; symbols: __init__, forward, _forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -316,7 +316,7 @@ def __init__(
-        self.linear_attn = RadixLinearAttention(
+        self.attn = RadixLinearAttention(
@@ -405,23 +405,6 @@ def forward(
-        if forward_batch.forward_mode.is_extend() and get_forward_context() is not None:
-            output = torch.empty_like(hidden_states)
-            gdn_with_output(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +2/-19
- Risk and verification: The diff ships test coverage in `test/registered/models/test_qwen3_next_models_pcg.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #18917 - [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill

- Link: https://github.com/sgl-project/sglang/pull/18917
- Status/date: merged / 2026-02-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `5995bfec6368`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-7, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +1/-7 (8 lines); hunks: -405,17 +405,11 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +1/-7 (8 lines); hunks: -405,17 +405,11 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -405,17 +405,11 @@ def forward(
-        is_cuda_graph = forward_batch.forward_mode.is_cuda_graph()
-        if (
-            self.num_v_heads // self.num_k_heads in [1, 2, 4]
-            and is_cuda_graph
-            and not _is_cpu
-        ):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +1/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #19434 - [Qwen3-Next] Support gdn fused_rms_norm_gated

- Link: https://github.com/sgl-project/sglang/pull/19434
- Status/date: merged / 2026-02-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `d2885a9094c3`
- Diff scope read: GitHub Pull Request files API returned 4 files, +411/-299, 758 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Qwen3-Next] Support gdn fused_rms_norm_gated"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[Qwen3-Next] Support gdn fused_rms_norm_gated"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +20/-8 (28 lines); hunks: -53,6 +53,9; -291,14 +294,23 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +20/-8 (28 lines); hunks: -53,6 +53,9; -291,14 +294,23 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -53,6 +53,9 @@
+from sglang.srt.layers.attention.fla.fused_norm_gate import FusedRMSNormGated
@@ -291,14 +294,23 @@ def __init__(
-        self.norm = RMSNormGated(
-            self.head_v_dim,
-            eps=self.layer_norm_epsilon,
-            group_size=None,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +20/-8
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17627 - [feat] Support nvfp4 quantized model of Qwen3-Next

- Link: https://github.com/sgl-project/sglang/pull/17627
- Status/date: merged / 2026-02-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `a2ea5941d562`
- Diff scope read: GitHub Pull Request files API returned 2 files, +83/-1, 105 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[feat] Support nvfp4 quantized model of Qwen3-Next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[feat] Support nvfp4 quantized model of Qwen3-Next"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +12/-1 (13 lines); hunks: -625,13 +625,19 @@ def __init__(; -1123,6 +1129,11 @@ def load_weights(; symbols: __init__, load_weights, touching `__init__, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +12/-1 (13 lines); hunks: -625,13 +625,19 @@ def __init__(; -1123,6 +1129,11 @@ def load_weights(; symbols: __init__, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -625,13 +625,19 @@ def __init__(
+        # qkv_proj is not quantized for fp4
-            quant_config=quant_config,
+            quant_config=(
+                quant_config
+                if quant_config is not None
+                and quant_config.get_name() != "modelopt_fp4"
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +12/-1
- Risk and verification: The diff ships test coverage in `test/registered/models/test_qwen3_next_models_fp4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #19321 - [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj

- Link: https://github.com/sgl-project/sglang/pull/19321
- Status/date: merged / 2026-03-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `d9794ef9f760`
- Diff scope read: GitHub Pull Request files API returned 2 files, +107/-17, 207 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +83/-11 (94 lines); hunks: -20,6 +20,7; -245,28 +246,38 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _make_packed_weight_loader, weight_loader, touching `__init__, fix_query_key_value_ordering, _make_packed_weight_loader`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +83/-11 (94 lines); hunks: -20,6 +20,7; -245,28 +246,38 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _make_packed_weight_loader, weight_loader
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -20,6 +20,7 @@
+    MergedColumnParallelLinear,
@@ -245,28 +246,38 @@ def __init__(
-        projection_size_qkvz = self.key_dim * 2 + self.value_dim * 2
-        projection_size_ba = self.num_v_heads * 2
-        self.in_proj_qkvz = ColumnParallelLinear(
-            input_size=self.hidden_size,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +83/-11
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21313 - bugfix for weight loading for qwen3-next

- Link: https://github.com/sgl-project/sglang/pull/21313
- Status/date: merged / 2026-03-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `0906e45cec97`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "bugfix for weight loading for qwen3-next"; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "bugfix for weight loading for qwen3-next"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -135,10 +135,10 @@ def __init__(
-        self.in_proj_qkvz.weight.weight_loader = self._make_packed_weight_loader(
+        self.in_proj_qkvz.weight._weight_loader = self._make_packed_weight_loader(
-        self.in_proj_ba.weight.weight_loader = self._make_packed_weight_loader(
+        self.in_proj_ba.weight._weight_loader = self._make_packed_weight_loader(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21496 - Revert "bugfix for weight loading for qwen3-next"

- Link: https://github.com/sgl-project/sglang/pull/21496
- Status/date: merged / 2026-03-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `a93065679b63`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Revert "bugfix for weight loading for qwen3-next""; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "Revert "bugfix for weight loading for qwen3-next""; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -135,10 +135,10 @@ def __init__(
-        self.in_proj_qkvz.weight._weight_loader = self._make_packed_weight_loader(
+        self.in_proj_qkvz.weight.weight_loader = self._make_packed_weight_loader(
-        self.in_proj_ba.weight._weight_loader = self._make_packed_weight_loader(
+        self.in_proj_ba.weight.weight_loader = self._make_packed_weight_loader(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21662 - [Fix] Fix weight_loader property assignment for qwen3-next FP8 models

- Link: https://github.com/sgl-project/sglang/pull/21662
- Status/date: merged / 2026-03-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `62a63eeff76d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +17/-4, 36 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Fix weight_loader property assignment for qwen3-next FP8 models"; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[Fix] Fix weight_loader property assignment for qwen3-next FP8 models"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +17/-4 (21 lines); hunks: -135,11 +135,11 @@ def __init__(; -216,6 +216,19 @@ def __init__(; symbols: __init__, _override_weight_loader, _make_packed_weight_loader, touching `__init__, _override_weight_loader, _make_packed_weight_loader`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +17/-4 (21 lines); hunks: -135,11 +135,11 @@ def __init__(; -216,6 +216,19 @@ def __init__(; symbols: __init__, _override_weight_loader, _make_packed_weight_loader
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -135,11 +135,11 @@ def __init__(
-        self.in_proj_qkvz.weight.weight_loader = self._make_packed_weight_loader(
-            self.in_proj_qkvz
+        self._override_weight_loader(
+            self.in_proj_qkvz, self._make_packed_weight_loader(self.in_proj_qkvz)
-        self.in_proj_ba.weight.weight_loader = self._make_packed_weight_loader(
-            self.in_proj_ba
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +17/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21698 - [npu]fix: qwen3-next w8a8 precision bugs

- Link: https://github.com/sgl-project/sglang/pull/21698
- Status/date: merged / 2026-04-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `f2b84b90ac86`
- Diff scope read: GitHub Pull Request files API returned 1 files, +22/-5, 41 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[npu]fix: qwen3-next w8a8 precision bugs"; model line: Qwen3 Next; category: bug fix; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[npu]fix: qwen3-next w8a8 precision bugs"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +22/-5 (27 lines); hunks: -65,6 +65,14; -223,11 +231,20 @@ def _override_weight_loader(module, new_loader):; symbols: Qwen3GatedDeltaNet, __init__, _override_weight_loader, _make_packed_weight_loader, touching `Qwen3GatedDeltaNet, __init__, _override_weight_loader`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +22/-5 (27 lines); hunks: -65,6 +65,14; -223,11 +231,20 @@ def _override_weight_loader(module, new_loader):; symbols: Qwen3GatedDeltaNet, __init__, _override_weight_loader, _make_packed_weight_loader
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -65,6 +65,14 @@
+if _is_npu:
+    from sgl_kernel_npu.fla.utils import (
+        fused_qkvzba_split_reshape_cat as fused_qkvzba_split_reshape_cat_npu,
+    )
+    fused_qkvzba_split_reshape_cat = fused_qkvzba_split_reshape_cat_npu
@@ -223,11 +231,20 @@ def _override_weight_loader(module, new_loader):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +22/-5
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23619 - Enable Qwen3-Next MoE all-reduce fusion

- Link: https://github.com/sgl-project/sglang/pull/23619
- Status/date: merged / 2026-04-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `13afe8acdff3`
- Diff scope read: GitHub Pull Request files API returned 1 files, +46/-23, 90 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Enable Qwen3-Next MoE all-reduce fusion"; model line: Qwen3 Next; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "Enable Qwen3-Next MoE all-reduce fusion"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +46/-23 (69 lines); hunks: -428,6 +428,48 @@ def forward(; -510,18 +552,8 @@ def forward(; symbols: forward, _apply_qwen3_next_mlp, Qwen3HybridLinearDecoderLayer, __init__, touching `forward, _apply_qwen3_next_mlp, Qwen3HybridLinearDecoderLayer`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +46/-23 (69 lines); hunks: -428,6 +428,48 @@ def forward(; -510,18 +552,8 @@ def forward(; symbols: forward, _apply_qwen3_next_mlp, Qwen3HybridLinearDecoderLayer, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -428,6 +428,48 @@ def forward(
+def _apply_qwen3_next_mlp(
+    layer: nn.Module,
+    hidden_states: torch.Tensor,
+    residual: Optional[torch.Tensor],
+    forward_batch: ForwardBatch,
+) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +46/-23
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23925 - [NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next

- Link: https://github.com/sgl-project/sglang/pull/23925
- Status/date: merged / 2026-05-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `55ba03db6a46`
- Diff scope read: GitHub Pull Request files API returned 3 files, +194/-19, 284 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +49/-8 (57 lines); hunks: -69,6 +69,9; -751,14 +754,8 @@ def _apply_qk_norm(; symbols: _apply_qk_norm, self_attention, forward_prepare_native, forward_prepare_npu, touching `_apply_qk_norm, self_attention, forward_prepare_native`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +49/-8 (57 lines); hunks: -69,6 +69,9; -751,14 +754,8 @@ def _apply_qk_norm(; symbols: _apply_qk_norm, self_attention, forward_prepare_native, forward_prepare_npu
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -69,6 +69,9 @@
+    from sgl_kernel_npu.norm.split_qkv_rmsnorm_rope import (
+        split_qkvgate_gemma_rmsnorm_rope,
+    )
@@ -751,14 +754,8 @@ def _apply_qk_norm(
-    def self_attention(
-        self,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +49/-8
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26204 - Optimize Qwen3 Next FP8 MoE on H200

- Link: https://github.com/sgl-project/sglang/pull/26204
- Status/date: merged / 2026-06-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`; associated commits `06e0df5899aa`
- Diff scope read: GitHub Pull Request files API returned 5 files, +427/-28, 589 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Optimize Qwen3 Next FP8 MoE on H200"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`; technical summary: Covers "Optimize Qwen3 Next FP8 MoE on H200"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +39/-9 (48 lines); hunks: -6,10 +6,12; -35,6 +37,11; symbols: __init__, routed_experts_weights_of_layer, touching `__init__, routed_experts_weights_of_layer`; `python/sglang/srt/models/qwen3_next_mtp.py` modified +13/-1 (14 lines); hunks: -59,7 +59,6 @@ def __init__(; -86,6 +85,19 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +39/-9 (48 lines); hunks: -6,10 +6,12; -35,6 +37,11; symbols: __init__, routed_experts_weights_of_layer
  - `python/sglang/srt/models/qwen3_next_mtp.py` modified +13/-1 (14 lines); hunks: -59,7 +59,6 @@ def __init__(; -86,6 +85,19 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -6,10 +6,12 @@
+from sglang.jit_kernel.triton.gdn_fused_proj import fused_qkvzba_split_reshape_cat
+from sglang.srt.layers.attention.fla.fused_norm_gate import FusedRMSNormGated
@@ -35,6 +37,11 @@
+from sglang.srt.model_executor.cuda_graph_config import (
+    Backend,
+    Phase,
diff -- python/sglang/srt/models/qwen3_next_mtp.py
@@ -59,7 +59,6 @@ def __init__(
-        # self.determine_num_fused_shared_experts("Qwen3NextForCausalLMMTP")
@@ -86,6 +85,19 @@ def __init__(
+        # Mirror Qwen3NextForCausalLM.__init__'s shared-expert fusion setup so
+        # the inherited load_weights() can find the attribute on the MTP path.
+        # We compute it from the actual MTP MoE layer (1 layer with is_nextn=True),
+        # not hardcode it — when the layer's MoE pre-fuses the shared expert,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +39/-9; `python/sglang/srt/models/qwen3_next_mtp.py` modified +13/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=513,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=513,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`, `python/sglang/srt/models/qwen2_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #45739 - [Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950

- Link: https://github.com/sgl-project/sglang/pull/45739
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_next.py`; associated commits `db90f584d2f4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +57/-1, 96 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_next.py`; technical summary: Covers "[Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950"; the main implementation surface is `python/sglang/srt/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_next.py` modified +57/-1 (58 lines); hunks: -1,4 +1,5; -63,8 +64,10; symbols: _fused_attention_prologue, _apply_qk_norm, forward_prepare_fused, forward_prepare_native, touching `_fused_attention_prologue, _apply_qk_norm, forward_prepare_fused`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_next.py` modified +57/-1 (58 lines); hunks: -1,4 +1,5; -63,8 +64,10; symbols: _fused_attention_prologue, _apply_qk_norm, forward_prepare_fused, forward_prepare_native
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -1,4 +1,5 @@
+import functools
@@ -63,8 +64,10 @@
+    get_bool_env_var,
+    is_gfx95_supported,
@@ -77,9 +80,32 @@
+_use_aiter = get_bool_env_var("SGLANG_USE_AITER") and _is_hip
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +57/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
