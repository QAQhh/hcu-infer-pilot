# sglang GPT-OSS Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/OpenAI/GPT-OSS.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/gpt-oss-deployment.jsx` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/gpt_oss.py` | no direct PR-number commit |
| `python/sglang/srt/function_call/gpt_oss_detector.py` | [#9043](https://github.com/sgl-project/sglang/pull/9043), [#9190](https://github.com/sgl-project/sglang/pull/9190), [#9657](https://github.com/sgl-project/sglang/pull/9657) |
| `python/sglang/srt/models/gpt_oss.py` | [#8824](https://github.com/sgl-project/sglang/pull/8824), [#8843](https://github.com/sgl-project/sglang/pull/8843), [#8944](https://github.com/sgl-project/sglang/pull/8944), [#9028](https://github.com/sgl-project/sglang/pull/9028), [#9146](https://github.com/sgl-project/sglang/pull/9146), [#9161](https://github.com/sgl-project/sglang/pull/9161), [#9359](https://github.com/sgl-project/sglang/pull/9359), [#9433](https://github.com/sgl-project/sglang/pull/9433), [#9469](https://github.com/sgl-project/sglang/pull/9469), [#9783](https://github.com/sgl-project/sglang/pull/9783), [#14197](https://github.com/sgl-project/sglang/pull/14197), [#16775](https://github.com/sgl-project/sglang/pull/16775), ... (25 total) |
| `python/sglang/test/gpt_oss_common.py` | [#16426](https://github.com/sgl-project/sglang/pull/16426) |
| `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` | [#26884](https://github.com/sgl-project/sglang/pull/26884) |
| `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` | [#27204](https://github.com/sgl-project/sglang/pull/27204) |
| `test/registered/amd/accuracy/mi45x/test_gpt_oss_w4a8_mxfp4_eval_mi45x.py` | no direct PR-number commit |
| `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` | [#34645](https://github.com/sgl-project/sglang/pull/34645) |
| `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` | [#34645](https://github.com/sgl-project/sglang/pull/34645) |
| `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` | [#31732](https://github.com/sgl-project/sglang/pull/31732) |
| `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` | [#39611](https://github.com/sgl-project/sglang/pull/39611) |
| `test/registered/e2e/models/test_gpt_oss_4gpu_mxfp4.py` | no direct PR-number commit |
| `test/registered/e2e/models/test_gpt_oss_sm120.py` | no direct PR-number commit |
| `test/registered/e2e/models_large/test_gpt_oss_120b.py` | no direct PR-number commit |
| `test/registered/e2e/moe/test_paged_experts_gpt_oss.py` | no direct PR-number commit |
| `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` | [#21570](https://github.com/sgl-project/sglang/pull/21570) |
| `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` | [#30050](https://github.com/sgl-project/sglang/pull/30050) |
| `test/registered/page_major/test_page_major_gpt_oss.py` | no direct PR-number commit |
| `test/registered/unit/models/test_gpt_oss_expert_loader_layout.py` | no direct PR-number commit |
| `test/registered/unit/models/test_gpt_oss_runai_ownership.py` | [#38908](https://github.com/sgl-project/sglang/pull/38908) |

## PR Coverage Summary

- Git-traced PRs: 34
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 34
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-08-05 | [#8824](https://github.com/sgl-project/sglang/pull/8824) | merged | Add initial support for gpt-oss | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-06 | [#8843](https://github.com/sgl-project/sglang/pull/8843) | merged | Support mxfp4 for GPT-OSS | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-08 | [#8944](https://github.com/sgl-project/sglang/pull/8944) | merged | Expert Parallelism for GPT-OSS | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-12 | [#9043](https://github.com/sgl-project/sglang/pull/9043) | merged | (gpt-oss, oai, chat): Remove Harmony Integration and Implement Native GPT-OSS Tool Call Support | `python/sglang/srt/function_call/gpt_oss_detector.py` |
| 2025-08-13 | [#9146](https://github.com/sgl-project/sglang/pull/9146) | merged | Fix gpt-oss ~2x memory consumption issue | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-13 | [#9028](https://github.com/sgl-project/sglang/pull/9028) | merged | Support FA3 backend for gpt-oss | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-13 | [#9161](https://github.com/sgl-project/sglang/pull/9161) | merged | Fix broken trtllm_mha attn backend with gpt-oss | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-20 | [#9359](https://github.com/sgl-project/sglang/pull/9359) | merged | Support DP attention with GPT-OSS | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-21 | [#9433](https://github.com/sgl-project/sglang/pull/9433) | merged | [fix] Fix mxfp4 weight loading bug with TP sharding in GPT-OSS | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-22 | [#9469](https://github.com/sgl-project/sglang/pull/9469) | merged | fix: tmp revert gpt oss tp sharding on hopper | `python/sglang/srt/models/gpt_oss.py` |
| 2025-08-25 | [#9190](https://github.com/sgl-project/sglang/pull/9190) | merged | Fix Harmony reasoning parser for and auto-separation for gpt-oss models | `python/sglang/srt/function_call/gpt_oss_detector.py` |
| 2025-09-01 | [#9783](https://github.com/sgl-project/sglang/pull/9783) | merged | support fp8 kvcache for hybrid attn backend on GPT-OSS | `python/sglang/srt/models/gpt_oss.py` |
| 2025-09-15 | [#9657](https://github.com/sgl-project/sglang/pull/9657) | merged | fix: gpt-oss streaming dropping normal content when tools are provided but not used | `python/sglang/srt/function_call/gpt_oss_detector.py` |
| 2026-01-07 | [#16426](https://github.com/sgl-project/sglang/pull/16426) | merged | Fix gpt_oss_common import path and migrate core tests | `python/sglang/test/gpt_oss_common.py` |
| 2026-01-18 | [#14197](https://github.com/sgl-project/sglang/pull/14197) | merged | [NPU]Support GPT-OSS for NPU | `python/sglang/srt/models/gpt_oss.py` |
| 2026-01-22 | [#17553](https://github.com/sgl-project/sglang/pull/17553) | merged | [NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py | `python/sglang/srt/models/gpt_oss.py` |
| 2026-02-12 | [#18405](https://github.com/sgl-project/sglang/pull/18405) | merged | [PCG] GPT OSS Triton Kernel Support | `python/sglang/srt/models/gpt_oss.py` |
| 2026-03-24 | [#20755](https://github.com/sgl-project/sglang/pull/20755) | merged | Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+ | `python/sglang/srt/models/gpt_oss.py` |
| 2026-04-02 | [#21570](https://github.com/sgl-project/sglang/pull/21570) | merged | [4/n] Support gpt oss 20b lora | `python/sglang/srt/models/gpt_oss.py`, `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` |
| 2026-05-29 | [#16775](https://github.com/sgl-project/sglang/pull/16775) | merged | [CPU] Add GPT-OSS model optimization for CPU | `python/sglang/srt/models/gpt_oss.py` |
| 2026-06-02 | [#26884](https://github.com/sgl-project/sglang/pull/26884) | merged | [AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path | `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` |
| 2026-06-08 | [#27063](https://github.com/sgl-project/sglang/pull/27063) | merged | [AMD] Optimize gpt-oss-120B performance | `python/sglang/srt/models/gpt_oss.py` |
| 2026-06-08 | [#27528](https://github.com/sgl-project/sglang/pull/27528) | merged | Fix GPT-OSS MXFP4 hidden size reshape on SM10X | `python/sglang/srt/models/gpt_oss.py` |
| 2026-06-12 | [#27941](https://github.com/sgl-project/sglang/pull/27941) | merged | Enable PDL for GPT-OSS tinygemm router | `python/sglang/srt/models/gpt_oss.py` |
| 2026-06-30 | [#27204](https://github.com/sgl-project/sglang/pull/27204) | merged | [AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8 | `python/sglang/srt/models/gpt_oss.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` |
| 2026-07-20 | [#31649](https://github.com/sgl-project/sglang/pull/31649) | merged | Enable GPT-OSS TinyGEMM on CUDA 13 | `python/sglang/srt/models/gpt_oss.py` |
| 2026-07-20 | [#31732](https://github.com/sgl-project/sglang/pull/31732) | merged | Support GPT-OSS zigzag CP with TRTLLM-MHA | `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` |
| 2026-07-31 | [#32334](https://github.com/sgl-project/sglang/pull/32334) | merged | [Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states | `python/sglang/srt/models/gpt_oss.py` |
| 2026-08-10 | [#30050](https://github.com/sgl-project/sglang/pull/30050) | merged | [MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale | `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` |
| 2026-08-16 | [#34645](https://github.com/sgl-project/sglang/pull/34645) | merged | [AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly | `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` |
| 2026-09-06 | [#37199](https://github.com/sgl-project/sglang/pull/37199) | merged | fix(gpt-oss): avoid duplicate MoE reduction with DP attention | `python/sglang/srt/models/gpt_oss.py` |
| 2026-09-12 | [#38908](https://github.com/sgl-project/sglang/pull/38908) | merged | Fix gpt-oss RunAI streamer weight ownership | `test/registered/unit/models/test_gpt_oss_runai_ownership.py`, `python/sglang/srt/models/gpt_oss.py` |
| 2026-09-15 | [#39611](https://github.com/sgl-project/sglang/pull/39611) | merged | [CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss | `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` |
| 2026-10-11 | [#43624](https://github.com/sgl-project/sglang/pull/43624) | merged | [Model] Keep gpt-oss router logits batch-invariant under deterministic inference | `python/sglang/srt/models/gpt_oss.py` |

## Per-PR Diff Audit Cards

### PR #8824 - Add initial support for gpt-oss

- Link: https://github.com/sgl-project/sglang/pull/8824
- Status/date: merged / 2025-08-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `c1d2061f97ae`
- Diff scope read: GitHub Pull Request files API returned 12 files, +1595/-47, 2185 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add initial support for gpt-oss"; model line: GPT-OSS; category: model support/runtime entry; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Add initial support for gpt-oss"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` added +923/-0 (923 lines); hunks: -0,0 +1,923; symbols: GptOssConfig, __init__, get_attention_sliding_window_size, GptOssSparseMoeBlock, touching `GptOssConfig, __init__, get_attention_sliding_window_size`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` added +923/-0 (923 lines); hunks: -0,0 +1,923; symbols: GptOssConfig, __init__, get_attention_sliding_window_size, GptOssSparseMoeBlock
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -0,0 +1,923 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` added +923/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/triton_ops/decode_attention.py`, `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #8843 - Support mxfp4 for GPT-OSS

- Link: https://github.com/sgl-project/sglang/pull/8843
- Status/date: merged / 2025-08-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `168033d5fb1e`
- Diff scope read: GitHub Pull Request files API returned 9 files, +791/-325, 1320 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support mxfp4 for GPT-OSS"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Support mxfp4 for GPT-OSS"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +209/-9 (218 lines); hunks: -25,6 +25,8; -108,11 +110,15 @@ def __init__(; symbols: __init__, _get_default_weight_mapping, load_weights, touching `__init__, _get_default_weight_mapping, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +209/-9 (218 lines); hunks: -25,6 +25,8; -108,11 +110,15 @@ def __init__(; symbols: __init__, _get_default_weight_mapping, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -25,6 +25,8 @@
+    get_moe_expert_parallel_rank,
+    get_moe_expert_parallel_world_size,
@@ -108,11 +110,15 @@ def __init__(
+            quant_config_name = (
+                quant_config.get_name() if quant_config is not None else None
+            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +209/-9
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`, `python/sglang/srt/layers/quantization/__init__.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #8944 - Expert Parallelism for GPT-OSS

- Link: https://github.com/sgl-project/sglang/pull/8944
- Status/date: merged / 2025-08-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `1d24db834803`
- Diff scope read: GitHub Pull Request files API returned 8 files, +269/-119, 956 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Expert Parallelism for GPT-OSS"; model line: GPT-OSS; category: model implementation change; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Expert Parallelism for GPT-OSS"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +54/-47 (101 lines); hunks: -28,6 +28,7; -96,11 +97,6 @@ def __init__(; symbols: __init__, _load_mxfp4_experts_weights, touching `__init__, _load_mxfp4_experts_weights`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +54/-47 (101 lines); hunks: -28,6 +28,7; -96,11 +97,6 @@ def __init__(; symbols: __init__, _load_mxfp4_experts_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -28,6 +28,7 @@
+    get_moe_tensor_parallel_world_size,
@@ -96,11 +97,6 @@ def __init__(
-        if self.tp_size > config.num_local_experts:
-            raise ValueError(
-                f"Tensor parallel size {self.tp_size} is greater than "
-                f"the number of experts {config.num_local_experts}."
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +54/-47
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9043 - (gpt-oss, oai, chat): Remove Harmony Integration and Implement Native GPT-OSS Tool Call Support

- Link: https://github.com/sgl-project/sglang/pull/9043
- Status/date: merged / 2025-08-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/gpt_oss_detector.py`; associated commits `a21849013607`
- Diff scope read: GitHub Pull Request files API returned 10 files, +717/-409, 1293 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "(gpt-oss, oai, chat): Remove Harmony Integration and Implement Native GPT-OSS Tool Call Support"; model line: GPT-OSS; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/gpt_oss_detector.py`; technical summary: Covers "(gpt-oss, oai, chat): Remove Harmony Integration and Implement Native GPT-OSS Tool Call Support"; the main implementation surface is `python/sglang/srt/function_call/gpt_oss_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/gpt_oss_detector.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse, touching `GptOssDetector, __init__, has_tool_call`.
- Code diff details:
  - `python/sglang/srt/function_call/gpt_oss_detector.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/gpt_oss_detector.py
@@ -0,0 +1,331 @@
+import json
+import logging
+import re
+from typing import List
+from sglang.srt.entrypoints.openai.protocol import Tool
+from sglang.srt.function_call.base_format_detector import BaseFormatDetector
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/gpt_oss_detector.py` added +331/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/entrypoints/harmony_utils.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/protocol.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9146 - Fix gpt-oss ~2x memory consumption issue

- Link: https://github.com/sgl-project/sglang/pull/9146
- Status/date: merged / 2025-08-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `9394ed63867d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +19/-7, 47 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix gpt-oss ~2x memory consumption issue"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Fix gpt-oss ~2x memory consumption issue"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +19/-7 (26 lines); hunks: -64,7 +64,13; -655,6 +661,18 @@ def __init__(; symbols: __init__, routed_experts_weights_of_layer, forward, _load_normal_weights, touching `__init__, routed_experts_weights_of_layer, forward`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +19/-7 (26 lines); hunks: -64,7 +64,13; -655,6 +661,18 @@ def __init__(; symbols: __init__, routed_experts_weights_of_layer, forward, _load_normal_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -64,7 +64,13 @@
-from sglang.srt.utils import add_prefix, is_cuda, is_flashinfer_available, make_layers
+from sglang.srt.utils import (
+    LazyValue,
+    add_prefix,
+    is_cuda,
+    is_flashinfer_available,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +19/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9028 - Support FA3 backend for gpt-oss

- Link: https://github.com/sgl-project/sglang/pull/9028
- Status/date: merged / 2025-08-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `0ff6d1fce122`
- Diff scope read: GitHub Pull Request files API returned 4 files, +24/-6, 121 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support FA3 backend for gpt-oss"; model line: GPT-OSS; category: model support/runtime entry; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Support FA3 backend for gpt-oss"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -294,7 +294,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -294,7 +294,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -294,7 +294,7 @@ def __init__(
-            torch.empty(self.num_heads, dtype=torch.float32), requires_grad=False
+            torch.empty(self.num_heads, dtype=torch.bfloat16), requires_grad=False
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/pyproject.toml`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9161 - Fix broken trtllm_mha attn backend with gpt-oss

- Link: https://github.com/sgl-project/sglang/pull/9161
- Status/date: merged / 2025-08-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `6b7c24712cda`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix broken trtllm_mha attn backend with gpt-oss"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Fix broken trtllm_mha attn backend with gpt-oss"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -293,8 +293,12 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -293,8 +293,12 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -293,8 +293,12 @@ def __init__(
+        # Choose dtype of sinks based on attention backend: trtllm_mha requires float32,
+        # others can use bfloat16
+        attn_backend = global_server_args_dict.get("attention_backend")
+        sinks_dtype = torch.float32 if attn_backend == "trtllm_mha" else torch.bfloat16
-            torch.empty(self.num_heads, dtype=torch.bfloat16), requires_grad=False
+            torch.empty(self.num_heads, dtype=sinks_dtype), requires_grad=False
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9359 - Support DP attention with GPT-OSS

- Link: https://github.com/sgl-project/sglang/pull/9359
- Status/date: merged / 2025-08-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `c10b8e6a0f2a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +6/-5, 25 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support DP attention with GPT-OSS"; model line: GPT-OSS; category: model support/runtime entry; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Support DP attention with GPT-OSS"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1123,7 +1123,7 @@ def _load_normal_weights(; symbols: _load_normal_weights, touching `_load_normal_weights`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1123,7 +1123,7 @@ def _load_normal_weights(; symbols: _load_normal_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -1123,7 +1123,7 @@ def _load_normal_weights(
-                            start = tp_rank * param.numel()
+                            start = get_attention_tp_rank() * param.numel()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/server_args.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9433 - [fix] Fix mxfp4 weight loading bug with TP sharding in GPT-OSS

- Link: https://github.com/sgl-project/sglang/pull/9433
- Status/date: merged / 2025-08-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `dae9a80f43e8`
- Diff scope read: GitHub Pull Request files API returned 2 files, +11/-3, 46 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[fix] Fix mxfp4 weight loading bug with TP sharding in GPT-OSS"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[fix] Fix mxfp4 weight loading bug with TP sharding in GPT-OSS"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +9/-1 (10 lines); hunks: -16,6 +16,7; -788,18 +789,25 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights, touching `_load_mxfp4_experts_weights`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +9/-1 (10 lines); hunks: -16,6 +16,7; -788,18 +789,25 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -16,6 +16,7 @@
+import math
@@ -788,18 +789,25 @@ def _load_mxfp4_experts_weights(self, weights):
+        assert (
+            intermediate_size % mxfp4_block == 0
+        ), f"{intermediate_size=} must be divisible by {mxfp4_block=}"
-        per_rank_intermediate_size_block = intermediate_size_block // moe_tp_size
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +9/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9469 - fix: tmp revert gpt oss tp sharding on hopper

- Link: https://github.com/sgl-project/sglang/pull/9469
- Status/date: merged / 2025-08-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `849957bc76c3`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-3, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: tmp revert gpt oss tp sharding on hopper"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "fix: tmp revert gpt oss tp sharding on hopper"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -793,9 +793,12 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights, touching `_load_mxfp4_experts_weights`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -793,9 +793,12 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -793,9 +793,12 @@ def _load_mxfp4_experts_weights(self, weights):
-        per_rank_intermediate_size_block = math.ceil(
-            intermediate_size_block / moe_tp_size
-        )
+        if _is_sm100_supported:
+            per_rank_intermediate_size_block = math.ceil(
+                intermediate_size_block / moe_tp_size
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +6/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9190 - Fix Harmony reasoning parser for and auto-separation for gpt-oss models

- Link: https://github.com/sgl-project/sglang/pull/9190
- Status/date: merged / 2025-08-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/gpt_oss_detector.py`; associated commits `a0a77d937b99`
- Diff scope read: GitHub Pull Request files API returned 8 files, +1681/-556, 2406 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Harmony reasoning parser for and auto-separation for gpt-oss models"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/function_call/gpt_oss_detector.py`; technical summary: Covers "Fix Harmony reasoning parser for and auto-separation for gpt-oss models"; the main implementation surface is `python/sglang/srt/function_call/gpt_oss_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +144/-256 (400 lines); hunks: -1,7 +1,7; -10,60 +10,31; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse, touching `GptOssDetector, __init__, has_tool_call`.
- Code diff details:
  - `python/sglang/srt/function_call/gpt_oss_detector.py` modified +144/-256 (400 lines); hunks: -1,7 +1,7; -10,60 +10,31; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/gpt_oss_detector.py
@@ -1,7 +1,7 @@
-from typing import List
+from typing import List, Optional
@@ -10,60 +10,31 @@
+from sglang.srt.harmony_parser import HarmonyParser
-    Detector for T4-style function calls with channel format.
+    Detector for T4-style function calls using HarmonyParser.
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +144/-256
- Risk and verification: The diff ships test coverage in `test/srt/run_suite.py`, `test/srt/test_harmony_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #9783 - support fp8 kvcache for hybrid attn backend on GPT-OSS

- Link: https://github.com/sgl-project/sglang/pull/9783
- Status/date: merged / 2025-09-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `9db8025376b2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-4, 30 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support fp8 kvcache for hybrid attn backend on GPT-OSS"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "support fp8 kvcache for hybrid attn backend on GPT-OSS"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +5/-4 (9 lines); hunks: -193,8 +193,9 @@ def forward_normal(; -341,7 +342,7 @@ def forward_prepare(; symbols: forward_normal, _enable_fused_set_kv_buffer, forward_prepare, forward_core, touching `forward_normal, _enable_fused_set_kv_buffer, forward_prepare`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +5/-4 (9 lines); hunks: -193,8 +193,9 @@ def forward_normal(; -341,7 +342,7 @@ def forward_prepare(; symbols: forward_normal, _enable_fused_set_kv_buffer, forward_prepare, forward_core
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -193,8 +193,9 @@ def forward_normal(
-def _enable_fused_set_kv_buffer():
-    return _is_cuda
+def _enable_fused_set_kv_buffer(forward_batch: ForwardBatch):
+    """Enable fused set_kv_buffer only on CUDA with bfloat16 KV cache."""
+    return _is_cuda and forward_batch.token_to_kv_pool.dtype == torch.bfloat16
@@ -341,7 +342,7 @@ def forward_prepare(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +5/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9657 - fix: gpt-oss streaming dropping normal content when tools are provided but not used

- Link: https://github.com/sgl-project/sglang/pull/9657
- Status/date: merged / 2025-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/gpt_oss_detector.py`; associated commits `28c79dc84ab8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +23/-0, 30 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: gpt-oss streaming dropping normal content when tools are provided but not used"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/function_call/gpt_oss_detector.py`; technical summary: Covers "fix: gpt-oss streaming dropping normal content when tools are provided but not used"; the main implementation surface is `python/sglang/srt/function_call/gpt_oss_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +23/-0 (23 lines); hunks: -81,6 +81,29 @@ def parse_streaming_increment(; symbols: parse_streaming_increment, touching `parse_streaming_increment`.
- Code diff details:
  - `python/sglang/srt/function_call/gpt_oss_detector.py` modified +23/-0 (23 lines); hunks: -81,6 +81,29 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/gpt_oss_detector.py
@@ -81,6 +81,29 @@ def parse_streaming_increment(
+        # If there are no parsed events and the chunk contains no Harmony structural
+        # markers, treat it as plain text and pass it through. This fixes a bug where
+        # normal content was held in the buffer when tools were provided but not used.
+        if not events:
+            has_harmony_markers = any(
+                marker in self._buffer
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +23/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/gpt_oss_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16426 - Fix gpt_oss_common import path and migrate core tests

- Link: https://github.com/sgl-project/sglang/pull/16426
- Status/date: merged / 2026-01-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/test/gpt_oss_common.py`; associated commits `0c474273c514`
- Diff scope read: GitHub Pull Request files API returned 15 files, +48/-26, 255 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix gpt_oss_common import path and migrate core tests"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/test/gpt_oss_common.py`; technical summary: Covers "Fix gpt_oss_common import path and migrate core tests"; the main implementation surface is `python/sglang/test/gpt_oss_common.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/test/gpt_oss_common.py` renamed +0/-0 (0 lines).
- Code diff details:
  - `python/sglang/test/gpt_oss_common.py` renamed +0/-0 (0 lines)
- Key code excerpts:

```diff
No textual patch was returned by GitHub for the selected changed files.
```

- Reviewed files:
  - tests: `python/sglang/test/gpt_oss_common.py` renamed +0/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/gpt_oss_common.py`, `test/registered/core/test_deterministic.py`, `test/registered/core/test_gpt_oss_1gpu.py`, `test/registered/core/test_hidden_states.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14197 - [NPU]Support GPT-OSS for NPU

- Link: https://github.com/sgl-project/sglang/pull/14197
- Status/date: merged / 2026-01-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `733de6be31e2`
- Diff scope read: GitHub Pull Request files API returned 4 files, +96/-17, 244 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]Support GPT-OSS for NPU"; model line: GPT-OSS; category: model support/runtime entry; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[NPU]Support GPT-OSS for NPU"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +20/-15 (35 lines); hunks: -71,9 +71,10; -129,6 +130,7 @@ def __init__(; symbols: __init__, forward_prepare, touching `__init__, forward_prepare`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +20/-15 (35 lines); hunks: -71,9 +71,10; -129,6 +130,7 @@ def __init__(; symbols: __init__, forward_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -71,9 +71,10 @@
-from sglang.srt.utils import LazyValue, add_prefix, is_cuda, make_layers
+from sglang.srt.utils import LazyValue, add_prefix, is_cuda, is_npu, make_layers
+_is_npu = is_npu()
@@ -129,6 +130,7 @@ def __init__(
@@ -305,20 +307,20 @@ def forward_prepare(
-        q, k = self.rotary_emb(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +20/-15
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17553 - [NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py

- Link: https://github.com/sgl-project/sglang/pull/17553
- Status/date: merged / 2026-01-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `61abff66c150`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -492,7 +492,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -492,7 +492,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -492,7 +492,7 @@ def __init__(
-        if is_npu:
+        if _is_npu:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18405 - [PCG] GPT OSS Triton Kernel Support

- Link: https://github.com/sgl-project/sglang/pull/18405
- Status/date: merged / 2026-02-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `2bd8363486e4`
- Diff scope read: GitHub Pull Request files API returned 6 files, +68/-32, 228 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[PCG] GPT OSS Triton Kernel Support"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[PCG] GPT OSS Triton Kernel Support"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +21/-4 (25 lines); hunks: -25,6 +25,10; -72,6 +76,7; symbols: forward_normal, moe_impl, GptOssAttention, __init__, touching `forward_normal, moe_impl, GptOssAttention`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +21/-4 (25 lines); hunks: -25,6 +25,10; -72,6 +76,7; symbols: forward_normal, moe_impl, GptOssAttention, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -25,6 +25,10 @@
+from sglang.srt.compilation.piecewise_context_manager import (
+    get_forward_context,
+    is_in_piecewise_cuda_graph,
+)
@@ -72,6 +76,7 @@
+from sglang.srt.utils.custom_op import register_custom_op
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +21/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/model_executor/model_runner.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20755 - Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+

- Link: https://github.com/sgl-project/sglang/pull/20755
- Status/date: merged / 2026-03-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `bbe25b24126d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +65/-2, 91 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +65/-2 (67 lines); hunks: -75,10 +75,34; -97,6 +121,45 @@ def get_attention_sliding_window_size(config):; symbols: GptOssConfig, get_attention_sliding_window_size, TinyGemmLinear, __init__, touching `GptOssConfig, get_attention_sliding_window_size, TinyGemmLinear`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +65/-2 (67 lines); hunks: -75,10 +75,34; -97,6 +121,45 @@ def get_attention_sliding_window_size(config):; symbols: GptOssConfig, get_attention_sliding_window_size, TinyGemmLinear, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -75,10 +75,34 @@
-from sglang.srt.utils import LazyValue, add_prefix, is_npu, make_layers
+from sglang.srt.utils import (
+    LazyValue,
+    add_prefix,
+    is_blackwell_supported,
+    is_cuda,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +65/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21570 - [4/n] Support gpt oss 20b lora

- Link: https://github.com/sgl-project/sglang/pull/21570
- Status/date: merged / 2026-04-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`, `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`; associated commits `566b4a4f1ccc`
- Diff scope read: GitHub Pull Request files API returned 7 files, +195/-24, 328 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[4/n] Support gpt oss 20b lora"; model line: GPT-OSS; category: docs/tests/CI; main diff: `python/sglang/srt/models/gpt_oss.py`, `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`; technical summary: Covers "[4/n] Support gpt oss 20b lora"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`, `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +8/-0 (8 lines); hunks: -17,6 +17,7; -651,6 +652,13 @@ def forward(; symbols: forward, GptOssForCausalLM, should_apply_lora, __init__, touching `forward, GptOssForCausalLM, should_apply_lora`; `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: kl_v2, get_prompt_logprobs, TestLoRAGptOss20BLogprobDiff, test_lora_gpt_oss_20b_logprob_accuracy, touching `kl_v2, get_prompt_logprobs, TestLoRAGptOss20BLogprobDiff`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +8/-0 (8 lines); hunks: -17,6 +17,7; -651,6 +652,13 @@ def forward(; symbols: forward, GptOssForCausalLM, should_apply_lora, __init__
  - `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: kl_v2, get_prompt_logprobs, TestLoRAGptOss20BLogprobDiff, test_lora_gpt_oss_20b_logprob_accuracy
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -17,6 +17,7 @@
+import re
@@ -651,6 +652,13 @@ def forward(
+    _lora_pattern_moe = re.compile(
+        r"^(?:model\.layers\.\d+\.(?:self_attn\.(?:qkv_proj|o_proj)|mlp\.experts)|lm_head|model\.embed_tokens)$"
+    )
+    def should_apply_lora(self, module_name: str) -> bool:
diff -- test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py
@@ -0,0 +1,151 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +8/-0
  - tests: `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` added +151/-0
- Risk and verification: The diff ships test coverage in `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_8b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #16775 - [CPU] Add GPT-OSS model optimization for CPU

- Link: https://github.com/sgl-project/sglang/pull/16775
- Status/date: merged / 2026-05-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `3ecf2c76ad1b`
- Diff scope read: GitHub Pull Request files API returned 35 files, +2023/-553, 3996 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CPU] Add GPT-OSS model optimization for CPU"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[CPU] Add GPT-OSS model optimization for CPU"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +20/-1 (21 lines); hunks: -81,6 +81,7; -89,6 +90,7; symbols: _load_mxfp4_experts_weights, _load_normal_weights, touching `_load_mxfp4_experts_weights, _load_normal_weights`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +20/-1 (21 lines); hunks: -81,6 +81,7; -89,6 +90,7; symbols: _load_mxfp4_experts_weights, _load_normal_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -81,6 +81,7 @@
+    is_cpu,
@@ -89,6 +90,7 @@
+_is_cpu = is_cpu()
@@ -881,7 +883,8 @@ def _load_mxfp4_experts_weights(self, weights):
-            weight = weight.cuda()
+            if _is_cuda:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +20/-1
- Risk and verification: The diff ships test coverage in `test/registered/cpu/test_decode.py`, `test/registered/cpu/test_extend.py`, `test/registered/cpu/test_gemm.py`, `test/registered/cpu/test_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #26884 - [AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path

- Link: https://github.com/sgl-project/sglang/pull/26884
- Status/date: merged / 2026-06-02
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`; associated commits `4226a6f13aa6`
- Diff scope read: GitHub Pull Request files API returned 5 files, +87/-20, 206 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path"; model line: GPT-OSS; category: bug fix; main diff: `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`; technical summary: Covers "[AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` modified +12/-2 (14 lines); hunks: -75,7 +75,14 @@ def __post_init__(self):; -93,7 +100,10 @@ def __post_init__(self):; symbols: __post_init__, touching `__post_init__`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` modified +12/-2 (14 lines); hunks: -75,7 +75,14 @@ def __post_init__(self):; -93,7 +100,10 @@ def __post_init__(self):; symbols: __post_init__
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py
@@ -75,7 +75,14 @@ def __post_init__(self):
-        env_vars={"SGLANG_USE_AITER": "1"},
+        # AITER MXFP4 fused-MoE for gpt-oss uses the SEPARATED gate/up tile
+        # layout (matches `gptoss_fp4_tuned_fmoe.csv` flydsl entries and the
+        # Mxfp4MoEMethod weight shuffle). Other AITER MXFP4 callers default
+        # to INTERLEAVE, so opt out explicitly here.
+        env_vars={
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` modified +12/-2
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27063 - [AMD] Optimize gpt-oss-120B performance

- Link: https://github.com/sgl-project/sglang/pull/27063
- Status/date: merged / 2026-06-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `1c73ff8ad3fd`
- Diff scope read: GitHub Pull Request files API returned 11 files, +1874/-54, 2160 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Optimize gpt-oss-120B performance"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[AMD] Optimize gpt-oss-120B performance"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +74/-5 (79 lines); hunks: -84,6 +84,7; -92,6 +93,7; symbols: forward, _resolve_moe_input_pad_multiple, GptOssSparseMoeBlock, __init__, touching `forward, _resolve_moe_input_pad_multiple, GptOssSparseMoeBlock`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +74/-5 (79 lines); hunks: -84,6 +84,7; -92,6 +93,7; symbols: forward, _resolve_moe_input_pad_multiple, GptOssSparseMoeBlock, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -84,6 +84,7 @@
+    is_hip,
@@ -92,6 +93,7 @@
+_is_hip = is_hip()
@@ -165,6 +167,36 @@ def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Optional[torch.Tensor]
+def _resolve_moe_input_pad_multiple(
+    quant_config: Optional[QuantizationConfig],
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +74/-5
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27528 - Fix GPT-OSS MXFP4 hidden size reshape on SM10X

- Link: https://github.com/sgl-project/sglang/pull/27528
- Status/date: merged / 2026-06-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `dc24a2682190`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-1, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix GPT-OSS MXFP4 hidden size reshape on SM10X"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Fix GPT-OSS MXFP4 hidden size reshape on SM10X"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +2/-1 (3 lines); hunks: -208,6 +208,7 @@ def __init__(; -291,7 +292,7 @@ def forward_normal(; symbols: __init__, forward_normal, touching `__init__, forward_normal`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +2/-1 (3 lines); hunks: -208,6 +208,7 @@ def __init__(; -291,7 +292,7 @@ def forward_normal(; symbols: __init__, forward_normal
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -208,6 +208,7 @@ def __init__(
+        self.hidden_size = config.hidden_size
@@ -291,7 +292,7 @@ def forward_normal(
-        hidden_dim_unpadded = self.experts.hidden_size
+        hidden_dim_unpadded = self.hidden_size
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27941 - Enable PDL for GPT-OSS tinygemm router

- Link: https://github.com/sgl-project/sglang/pull/27941
- Status/date: merged / 2026-06-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `cb9140ee6108`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 25 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Enable PDL for GPT-OSS tinygemm router"; model line: GPT-OSS; category: model support/runtime entry; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Enable PDL for GPT-OSS tinygemm router"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +2/-2 (4 lines); hunks: -26,6 +26,7; -161,7 +162,7 @@ def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Op...; symbols: forward, _load_normal_weights, touching `forward, _load_normal_weights`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +2/-2 (4 lines); hunks: -26,6 +26,7; -161,7 +162,7 @@ def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Op...; symbols: forward, _load_normal_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -26,6 +26,7 @@
+from sglang.jit_kernel.utils import is_arch_support_pdl
@@ -161,7 +162,7 @@ def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Optional[torch.Tensor]
-            tinygemm_bf16(x, self.weight, out, self.bias)
+            tinygemm_bf16(x, self.weight, out, self.bias, use_pdl=is_arch_support_pdl())
@@ -1094,7 +1095,6 @@ def _load_normal_weights(
-        tp_rank = get_tensor_model_parallel_rank()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27204 - [AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8

- Link: https://github.com/sgl-project/sglang/pull/27204
- Status/date: merged / 2026-06-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`; associated commits `a5e6dd37677f`
- Diff scope read: GitHub Pull Request files API returned 6 files, +948/-3, 998 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`; technical summary: Covers "[AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +14/-3 (17 lines); hunks: -879,12 +879,23 @@ def load_weights(; symbols: load_weights, touching `load_weights`; `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_one_example, get_few_shot_examples, touching `ModelConfig, __post_init__, get_one_example`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +14/-3 (17 lines); hunks: -879,12 +879,23 @@ def load_weights(; symbols: load_weights
  - `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_one_example, get_few_shot_examples
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -879,12 +879,23 @@ def load_weights(
-        if quant_config_name != "mxfp4":
-            self._load_normal_weights(
+        if quant_config_name == "mxfp4":
+            self._load_weights_mxfp4(
+        elif quant_config_name == "quark":
+            from sglang.srt.layers.quantization.quark.weights import (
diff -- test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py
@@ -0,0 +1,251 @@
+"""MI35x GPT-OSS W4A8 MXFP4-FP8 GSM8K Completion Evaluation Test (8-GPU)
+Tests the AMD Quark `gpt-oss-120b-w-mxfp4-a-fp8` checkpoint (MXFP4
+weights + static per-tensor FP8 activations) using few-shot completion
+benchmark on MI35x.
+Registry: nightly-amd-8-gpu-mi35x suite
+"""
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +14/-3
  - tests: `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` added +251/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31649 - Enable GPT-OSS TinyGEMM on CUDA 13

- Link: https://github.com/sgl-project/sglang/pull/31649
- Status/date: merged / 2026-07-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `8bf2ab9be931`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-2, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Enable GPT-OSS TinyGEMM on CUDA 13"; model line: GPT-OSS; category: performance/backend optimization; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Enable GPT-OSS TinyGEMM on CUDA 13"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +1/-2 (3 lines); hunks: -72,7 +72,6; -94,7 +93,7.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-2 (3 lines); hunks: -72,7 +72,6; -94,7 +93,7
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -72,7 +72,6 @@
-    get_cuda_version,
@@ -94,7 +93,7 @@
-if _is_tinygemm_supported and get_cuda_version()[0] < 13:
+if _is_tinygemm_supported:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31732 - Support GPT-OSS zigzag CP with TRTLLM-MHA

- Link: https://github.com/sgl-project/sglang/pull/31732
- Status/date: merged / 2026-07-20
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`; associated commits `9668d9ea72ae`
- Diff scope read: GitHub Pull Request files API returned 5 files, +143/-33, 289 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support GPT-OSS zigzag CP with TRTLLM-MHA"; model line: GPT-OSS; category: performance/backend optimization; main diff: `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`; technical summary: Covers "Support GPT-OSS zigzag CP with TRTLLM-MHA"; the main implementation surface is `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` added +32/-0 (32 lines); hunks: -0,0 +1,32; symbols: TestGptOss4GpuMxfp4CP, test_mxfp4_120b, touching `TestGptOss4GpuMxfp4CP, test_mxfp4_120b`.
- Code diff details:
  - `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` added +32/-0 (32 lines); hunks: -0,0 +1,32; symbols: TestGptOss4GpuMxfp4CP, test_mxfp4_120b
- Key code excerpts:

```diff
diff -- test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py
@@ -0,0 +1,32 @@
+import unittest
+from sglang.test.ci.ci_register import register_cuda_ci
+from sglang.test.gpt_oss_common import BaseTestGptOss
+register_cuda_ci(est_time=220, stage="extra-b", runner_config="4-gpu-b200")
+class TestGptOss4GpuMxfp4CP(BaseTestGptOss):
+    def test_mxfp4_120b(self):
```

- Reviewed files:
  - tests: `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` added +32/-0
- Risk and verification: The diff ships test coverage in `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #32334 - [Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states

- Link: https://github.com/sgl-project/sglang/pull/32334
- Status/date: merged / 2026-07-31
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `5df193b4ac0f`
- Diff scope read: GitHub Pull Request files API returned 2 files, +36/-6, 82 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +19/-6 (25 lines); hunks: -720,15 +720,25 @@ def forward(; -1319,15 +1329,18 @@ def set_eagle3_layers_to_capture(self, layer_ids: Option...; symbols: forward, set_eagle3_layers_to_capture, set_dflash_layers_to_capture, touching `forward, set_eagle3_layers_to_capture, set_dflash_layers_to_capture`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +19/-6 (25 lines); hunks: -720,15 +720,25 @@ def forward(; -1319,15 +1329,18 @@ def set_eagle3_layers_to_capture(self, layer_ids: Option...; symbols: forward, set_eagle3_layers_to_capture, set_dflash_layers_to_capture
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -720,15 +720,25 @@ def forward(
+        # Capture hidden-state boundaries: boundary 0 is the embedding output,
+        # and boundary i + 1 is the output after transformer block i.
+        if self.start_layer in self.layers_to_capture:
+            aux_hidden_states.append(
+                hidden_states + residual if residual is not None else hidden_states
+            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +19/-6
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/llama_eagle3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #30050 - [MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale

- Link: https://github.com/sgl-project/sglang/pull/30050
- Status/date: merged / 2026-08-10
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`; associated commits `553dc0f936ea`
- Diff scope read: GitHub Pull Request files API returned 12 files, +1100/-43, 1372 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale"; model line: GPT-OSS; category: docs/tests/CI; main diff: `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`; technical summary: Covers "[MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale"; the main implementation surface is `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: _available_gb, TestGptOssMlxCorrectness, setUpClass, tearDownClass, touching `_available_gb, TestGptOssMlxCorrectness, setUpClass`.
- Code diff details:
  - `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: _available_gb, TestGptOssMlxCorrectness, setUpClass, tearDownClass
- Key code excerpts:

```diff
diff -- test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py
@@ -0,0 +1,371 @@
+"""Correctness tests for gpt-oss served on the SGLang MLX backend.
+gpt-oss interleaves sliding-window (window=128) and full-attention layers and
+uses per-head attention sinks, so it exercises the MLX backend's
+sliding-window path end to end. Two guards:
+1. ``TestGptOssMlxCorrectness`` — black-box serving smoke against a running
+   server, including a >128-token prompt so the sliding window actually
```

- Reviewed files:
  - tests: `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` added +371/-0
- Risk and verification: The diff ships test coverage in `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`, `test/registered/unit/hardware_backend/mlx/test_sliding_window_attention.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #34645 - [AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly

- Link: https://github.com/sgl-project/sglang/pull/34645
- Status/date: merged / 2026-08-16
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`, `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`; associated commits `d91c3682b0b4`
- Diff scope read: GitHub Pull Request files API returned 4 files, +283/-0, 319 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly"; model line: GPT-OSS; category: performance/backend optimization; main diff: `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`; technical summary: Covers "[AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly"; the main implementation surface is `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` added +107/-0 (107 lines); hunks: -0,0 +1,107; symbols: TestNightlyGptOssPerformanceMI35x, setUpClass, test_bench_one_batch, touching `TestNightlyGptOssPerformanceMI35x, setUpClass, test_bench_one_batch`; `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` added +106/-0 (106 lines); hunks: -0,0 +1,106; symbols: TestNightlyGptOssPerformanceAMD, setUpClass, test_bench_one_batch, touching `TestNightlyGptOssPerformanceAMD, setUpClass, test_bench_one_batch`.
- Code diff details:
  - `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` added +107/-0 (107 lines); hunks: -0,0 +1,107; symbols: TestNightlyGptOssPerformanceMI35x, setUpClass, test_bench_one_batch
  - `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` added +106/-0 (106 lines); hunks: -0,0 +1,106; symbols: TestNightlyGptOssPerformanceAMD, setUpClass, test_bench_one_batch
- Key code excerpts:

```diff
diff -- test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py
@@ -0,0 +1,107 @@
+"""MI35x nightly performance benchmark for GPT-OSS (8-GPU).
+Benchmarks the MXFP4 GPT-OSS checkpoints (openai/gpt-oss-20b,
+openai/gpt-oss-120b) with the same TP8 AITER server configuration the MI35x
+GPT-OSS accuracy test uses, so a throughput change here points at the
+serving stack rather than at a different recipe.
+Registry: nightly-perf-8-gpu-mi35x-gpt-oss suite
diff -- test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py
@@ -0,0 +1,106 @@
+"""MI30x nightly performance benchmark for GPT-OSS (8-GPU).
+Benchmarks the bf16 GPT-OSS conversions (lmsys/gpt-oss-20b-bf16,
+lmsys/gpt-oss-120b-bf16) with the same TP8 AITER server configuration the
+MI30x GPT-OSS accuracy test uses, so a throughput change here points at the
+serving stack rather than at a different recipe.
+MI30x cannot serve the MXFP4 checkpoints natively, which is why the model
```

- Reviewed files:
  - tests: `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` added +107/-0; `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` added +106/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/nightly_bench_utils.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`, `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37199 - fix(gpt-oss): avoid duplicate MoE reduction with DP attention

- Link: https://github.com/sgl-project/sglang/pull/37199
- Status/date: merged / 2026-09-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `28457f0dcab4`
- Diff scope read: GitHub Pull Request files API returned 2 files, +40/-5, 87 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(gpt-oss): avoid duplicate MoE reduction with DP attention"; model line: GPT-OSS; category: bug fix; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "fix(gpt-oss): avoid duplicate MoE reduction with DP attention"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +16/-3 (19 lines); hunks: -44,7 +44,10; -329,7 +332,9 @@ def forward_normal(; symbols: forward_normal, __init__, forward, touching `forward_normal, __init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +16/-3 (19 lines); hunks: -44,7 +44,10; -329,7 +332,9 @@ def forward_normal(; symbols: forward_normal, __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -44,7 +44,10 @@
-from sglang.srt.layers.moe import get_moe_a2a_backend
+from sglang.srt.layers.moe import (
+    get_moe_a2a_backend,
+    should_skip_post_experts_all_reduce,
+)
@@ -329,7 +332,9 @@ def forward_normal(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +16/-3
- Risk and verification: The diff ships test coverage in `test/registered/models_e2e/test_gpt_oss_4gpu_mxfp4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #38908 - Fix gpt-oss RunAI streamer weight ownership

- Link: https://github.com/sgl-project/sglang/pull/38908
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`, `test/registered/unit/models/test_gpt_oss_runai_ownership.py`; associated commits `fd3222670660`
- Diff scope read: GitHub Pull Request files API returned 2 files, +126/-12, 163 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix gpt-oss RunAI streamer weight ownership"; model line: GPT-OSS; category: bug fix; main diff: `test/registered/unit/models/test_gpt_oss_runai_ownership.py`, `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "Fix gpt-oss RunAI streamer weight ownership"; the main implementation surface is `test/registered/unit/models/test_gpt_oss_runai_ownership.py`, `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/models/test_gpt_oss_runai_ownership.py` added +94/-0 (94 lines); hunks: -0,0 +1,94; symbols: _streamed, _Mxfp4QuantConfig, get_name, TestGptOssRunaiOwnership, touching `_streamed, _Mxfp4QuantConfig, get_name`; `python/sglang/srt/models/gpt_oss.py` modified +32/-12 (44 lines); hunks: -66,7 +66,10; -953,20 +956,25 @@ def load_weights(; symbols: load_weights, _load_weights_mxfp4, experts, get_attention_sliding_window_size, touching `load_weights, _load_weights_mxfp4, experts`.
- Code diff details:
  - `test/registered/unit/models/test_gpt_oss_runai_ownership.py` added +94/-0 (94 lines); hunks: -0,0 +1,94; symbols: _streamed, _Mxfp4QuantConfig, get_name, TestGptOssRunaiOwnership
  - `python/sglang/srt/models/gpt_oss.py` modified +32/-12 (44 lines); hunks: -66,7 +66,10; -953,20 +956,25 @@ def load_weights(; symbols: load_weights, _load_weights_mxfp4, experts, get_attention_sliding_window_size
- Key code excerpts:

```diff
diff -- test/registered/unit/models/test_gpt_oss_runai_ownership.py
@@ -0,0 +1,94 @@
+"""Hermetic unit tests for gpt-oss RunAI-streamed weight ownership.
+The RunAI streamer hands out zero-copy views into a staging buffer it reuses
+between tensors, so a view read after later tensors arrive can come back as
+garbage. `_load_weights_mxfp4` therefore has to consume the expert weights as
+they are yielded, and take its own copy of anything it keeps for later.
+Pure Python (no GPU, no model weights): the model object is built without
diff -- python/sglang/srt/models/gpt_oss.py
@@ -66,7 +66,10 @@
-from sglang.srt.model_loader.weight_utils import default_weight_loader
+from sglang.srt.model_loader.weight_utils import (
+    RUNAI_STREAMER_TENSOR_ATTR,
+    default_weight_loader,
+)
@@ -953,20 +956,25 @@ def load_weights(
```

- Reviewed files:
  - tests: `test/registered/unit/models/test_gpt_oss_runai_ownership.py` added +94/-0
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +32/-12
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_gpt_oss_runai_ownership.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39611 - [CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss

- Link: https://github.com/sgl-project/sglang/pull/39611
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`; associated commits `47a157f257f1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +25/-63, 106 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss"; model line: GPT-OSS; category: bug fix; main diff: `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`; technical summary: Covers "[CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss"; the main implementation surface is `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` modified +25/-63 (88 lines); hunks: -6,10 +6,6; -23,69 +19,35 @@ class TestDisaggregationDWDPGptOss(PDDisaggregationServerBase):; symbols: TestDisaggregationDWDPGptOss, setUpClass, start_prefill, start_decode, touching `TestDisaggregationDWDPGptOss, setUpClass, start_prefill`.
- Code diff details:
  - `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` modified +25/-63 (88 lines); hunks: -6,10 +6,6; -23,69 +19,35 @@ class TestDisaggregationDWDPGptOss(PDDisaggregationServerBase):; symbols: TestDisaggregationDWDPGptOss, setUpClass, start_prefill, start_decode
- Key code excerpts:

```diff
diff -- test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py
@@ -6,10 +6,6 @@
-from sglang.test.test_utils import (
-    DEFAULT_TIMEOUT_FOR_SERVER_LAUNCH,
-    popen_launch_pd_server,
-)
@@ -23,69 +19,35 @@ class TestDisaggregationDWDPGptOss(PDDisaggregationServerBase):
+    # Drive the base fixture's launchers rather than reimplementing them, so
```

- Reviewed files:
  - tests: `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` modified +25/-63
- Risk and verification: The diff ships test coverage in `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #43624 - [Model] Keep gpt-oss router logits batch-invariant under deterministic inference

- Link: https://github.com/sgl-project/sglang/pull/43624
- Status/date: merged / 2026-10-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gpt_oss.py`; associated commits `7187bb593ea3`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-0, 12 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Keep gpt-oss router logits batch-invariant under deterministic inference"; model line: GPT-OSS; category: model implementation change; main diff: `python/sglang/srt/models/gpt_oss.py`; technical summary: Covers "[Model] Keep gpt-oss router logits batch-invariant under deterministic inference"; the main implementation surface is `python/sglang/srt/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -137,8 +137,11 @@ class TinyGemmLinear(ReplicatedLinear):; symbols: TinyGemmLinear, __init__, touching `TinyGemmLinear, __init__`.
- Code diff details:
  - `python/sglang/srt/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -137,8 +137,11 @@ class TinyGemmLinear(ReplicatedLinear):; symbols: TinyGemmLinear, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -137,8 +137,11 @@ class TinyGemmLinear(ReplicatedLinear):
+        # tinygemm serves only up to 128 tokens, so with it a token's router
+        # logits would depend on how many tokens share its batch.
+            and not get_exec().deterministic.enable_deterministic_inference
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
