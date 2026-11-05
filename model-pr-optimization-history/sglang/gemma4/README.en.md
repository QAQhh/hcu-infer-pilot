# sglang Gemma 4 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/Google/Gemma4.mdx` | [#46816](https://github.com/sgl-project/sglang/pull/46816) |
| `docs/src/snippets/autoregressive/gemma4-deployment.jsx` | no direct PR-number commit |
| `python/sglang/kernels/ops/layernorm/gemma4_fused_ops.py` | no direct PR-number commit |
| `python/sglang/kernels/ops/moe/gemma4_routing.py` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/gemma4.py` | no direct PR-number commit |
| `python/sglang/srt/dllm/algorithm/gemma4_renoise.py` | no direct PR-number commit |
| `python/sglang/srt/function_call/gemma4_detector.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952) |
| `python/sglang/srt/models/gemma4_audio.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952) |
| `python/sglang/srt/models/gemma4_causal.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#22498](https://github.com/sgl-project/sglang/pull/22498), [#23280](https://github.com/sgl-project/sglang/pull/23280), [#24048](https://github.com/sgl-project/sglang/pull/24048), [#24436](https://github.com/sgl-project/sglang/pull/24436), [#24696](https://github.com/sgl-project/sglang/pull/24696), [#25054](https://github.com/sgl-project/sglang/pull/25054), [#25284](https://github.com/sgl-project/sglang/pull/25284), [#26026](https://github.com/sgl-project/sglang/pull/26026), [#26147](https://github.com/sgl-project/sglang/pull/26147), [#26502](https://github.com/sgl-project/sglang/pull/26502), [#27471](https://github.com/sgl-project/sglang/pull/27471), ... (13 total) |
| `python/sglang/srt/models/gemma4_mm.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#22498](https://github.com/sgl-project/sglang/pull/22498), [#24048](https://github.com/sgl-project/sglang/pull/24048), [#24436](https://github.com/sgl-project/sglang/pull/24436), [#24696](https://github.com/sgl-project/sglang/pull/24696), [#25054](https://github.com/sgl-project/sglang/pull/25054), [#25284](https://github.com/sgl-project/sglang/pull/25284), [#26147](https://github.com/sgl-project/sglang/pull/26147), [#27471](https://github.com/sgl-project/sglang/pull/27471), [#31672](https://github.com/sgl-project/sglang/pull/31672), [#42019](https://github.com/sgl-project/sglang/pull/42019), [#46816](https://github.com/sgl-project/sglang/pull/46816) |
| `python/sglang/srt/models/gemma4_mtp.py` | [#24436](https://github.com/sgl-project/sglang/pull/24436), [#26026](https://github.com/sgl-project/sglang/pull/26026), [#32440](https://github.com/sgl-project/sglang/pull/32440) |
| `python/sglang/srt/models/gemma4_unified.py` | [#35809](https://github.com/sgl-project/sglang/pull/35809) |
| `python/sglang/srt/models/gemma4_vision.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#22498](https://github.com/sgl-project/sglang/pull/22498) |
| `python/sglang/srt/multimodal/processors/gemma4.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#26320](https://github.com/sgl-project/sglang/pull/26320) |
| `python/sglang/srt/multimodal/processors/gemma4_unified.py` | no direct PR-number commit |
| `test/registered/attention/test_gemma4_swa_triton_oob_regression.py` | no direct PR-number commit |
| `test/registered/attention/test_gemma4_unified_swa_virtual_ids.py` | no direct PR-number commit |
| `test/registered/e2e/models/test_gemma4_fp8_per_expert_loading.py` | no direct PR-number commit |
| `test/registered/kernels/ops/layernorm/test_gemma4_qkv_norm.py` | no direct PR-number commit |
| `test/registered/kernels/ops/moe/test_gemma4_expert_activation.py` | no direct PR-number commit |
| `test/registered/kernels/ops/moe/test_gemma4_fused_routing.py` | no direct PR-number commit |
| `test/registered/pp/test_pp_gemma4.py` | no direct PR-number commit |
| `test/registered/spec/test_gemma4_dflash_31b_extra.py` | [#27471](https://github.com/sgl-project/sglang/pull/27471) |
| `test/registered/spec/test_gemma4_mtp_31b_extra.py` | [#24552](https://github.com/sgl-project/sglang/pull/24552), [#27101](https://github.com/sgl-project/sglang/pull/27101) |
| `test/registered/unit/dllm/algorithm/test_gemma4_sampling_cuda.py` | no direct PR-number commit |
| `test/registered/unit/dllm/test_gemma4_cuda_graph.py` | no direct PR-number commit |
| `test/registered/unit/dllm/test_gemma4_renoise.py` | no direct PR-number commit |
| `test/registered/unit/dllm/test_gemma4_uniform_lifecycle.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 21
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 21
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-07 | [#21952](https://github.com/sgl-project/sglang/pull/21952) | merged | [New Model] Gemma 4 | `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_audio.py` |
| 2026-05-04 | [#24048](https://github.com/sgl-project/sglang/pull/24048) | merged | [VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar | `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py` |
| 2026-05-07 | [#24436](https://github.com/sgl-project/sglang/pull/24436) | merged | [Gemma 4] Adding MTP support | `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py` |
| 2026-05-10 | [#24696](https://github.com/sgl-project/sglang/pull/24696) | merged | [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader | `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py` |
| 2026-05-19 | [#25284](https://github.com/sgl-project/sglang/pull/25284) | merged | Support Gemma4 Pipeline Parallelism | `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py` |
| 2026-05-21 | [#25054](https://github.com/sgl-project/sglang/pull/25054) | merged | Support Gemma4 MoE NVFP4 | `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py` |
| 2026-05-23 | [#26026](https://github.com/sgl-project/sglang/pull/26026) | merged | [bug fix] Fix 3 issues when using Gemma4 MTP | `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py` |
| 2026-05-28 | [#24552](https://github.com/sgl-project/sglang/pull/24552) | merged | [Gemma4] Add test for MTP models | `test/registered/spec/test_gemma4_mtp_31b_extra.py` |
| 2026-06-02 | [#26502](https://github.com/sgl-project/sglang/pull/26502) | merged | perf(gemma4): single-launch fused router (topk + softmax + scale) | `python/sglang/srt/models/gemma4_causal.py` |
| 2026-06-03 | [#27101](https://github.com/sgl-project/sglang/pull/27101) | merged | [Gemma4] Use hard GSM8K accuracy floor for 31B MTP test | `test/registered/spec/test_gemma4_mtp_31b_extra.py` |
| 2026-06-05 | [#23280](https://github.com/sgl-project/sglang/pull/23280) | merged | [XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU | `python/sglang/srt/models/gemma4_causal.py` |
| 2026-06-09 | [#26320](https://github.com/sgl-project/sglang/pull/26320) | merged | fix(gemma4): register image/video/audio token_regex for HF-expanded prompts | `python/sglang/srt/multimodal/processors/gemma4.py` |
| 2026-06-12 | [#26147](https://github.com/sgl-project/sglang/pull/26147) | merged | [NPU] Add Gemma4 Sliding Window Attention support on Ascend backend | `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py` |
| 2026-06-17 | [#27471](https://github.com/sgl-project/sglang/pull/27471) | merged | add dflash gemma4 support | `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py` |
| 2026-07-19 | [#31672](https://github.com/sgl-project/sglang/pull/31672) | merged | fix(gemma4): prevent attention mask offset overflow | `python/sglang/srt/models/gemma4_mm.py` |
| 2026-08-17 | [#22498](https://github.com/sgl-project/sglang/pull/22498) | merged | [CPU] Add support for Gemma4 on Xeon | `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_vision.py` |
| 2026-08-19 | [#32440](https://github.com/sgl-project/sglang/pull/32440) | merged | fix(gemma4): quantize MTP bridge projections | `python/sglang/srt/models/gemma4_mtp.py` |
| 2026-09-15 | [#35809](https://github.com/sgl-project/sglang/pull/35809) | merged | fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration | `python/sglang/srt/models/gemma4_unified.py` |
| 2026-10-03 | [#42311](https://github.com/sgl-project/sglang/pull/42311) | merged | [Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries | `python/sglang/srt/models/gemma4_causal.py` |
| 2026-10-10 | [#42019](https://github.com/sgl-project/sglang/pull/42019) | merged | [Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support | `python/sglang/srt/models/gemma4_mm.py` |
| 2026-11-02 | [#46816](https://github.com/sgl-project/sglang/pull/46816) | merged | [Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend | `python/sglang/srt/models/gemma4_mm.py`, `docs/cookbook/autoregressive/Google/Gemma4.mdx` |

## Per-PR Diff Audit Cards

### PR #21952 - [New Model] Gemma 4

- Link: https://github.com/sgl-project/sglang/pull/21952
- Status/date: merged / 2026-04-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/gemma4_detector.py`, `python/sglang/srt/models/gemma4_audio.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_vision.py` and 6 files; associated commits `2813cb6d9a5b`
- Diff scope read: GitHub Pull Request files API returned 35 files, +6007/-70, 6694 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[New Model] Gemma 4"; model line: Gemma 4; category: model implementation change; main diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_audio.py`; technical summary: Covers "[New Model] Gemma 4"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_audio.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` added +1009/-0 (1009 lines); hunks: -0,0 +1,1009; symbols: get_attention_sliding_window_size, Gemma4Router, __init__, fuse_scale, touching `get_attention_sliding_window_size, Gemma4Router, __init__`; `python/sglang/srt/models/gemma4_mm.py` added +878/-0 (878 lines); hunks: -0,0 +1,878; symbols: Gemma4ImagePixelInputs, Gemma4AudioInputs, Gemma4MultimodalEmbedder, __init__, touching `Gemma4ImagePixelInputs, Gemma4AudioInputs, Gemma4MultimodalEmbedder`; `python/sglang/srt/models/gemma4_audio.py` added +873/-0 (873 lines); hunks: -0,0 +1,873; symbols: Gemma4AudioRelativePositionEmbedding, __init__, _get_timing_signal_1d_pos, _relative_shift, touching `Gemma4AudioRelativePositionEmbedding, __init__, _get_timing_signal_1d_pos`; `python/sglang/srt/models/gemma4_vision.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: _rotate_half, _apply_rotary, Gemma4VisionRotaryEmbedding, __init__, touching `_rotate_half, _apply_rotary, Gemma4VisionRotaryEmbedding`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` added +1009/-0 (1009 lines); hunks: -0,0 +1,1009; symbols: get_attention_sliding_window_size, Gemma4Router, __init__, fuse_scale
  - `python/sglang/srt/models/gemma4_mm.py` added +878/-0 (878 lines); hunks: -0,0 +1,878; symbols: Gemma4ImagePixelInputs, Gemma4AudioInputs, Gemma4MultimodalEmbedder, __init__
  - `python/sglang/srt/models/gemma4_audio.py` added +873/-0 (873 lines); hunks: -0,0 +1,873; symbols: Gemma4AudioRelativePositionEmbedding, __init__, _get_timing_signal_1d_pos, _relative_shift
  - `python/sglang/srt/models/gemma4_vision.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: _rotate_half, _apply_rotary, Gemma4VisionRotaryEmbedding, __init__
  - `python/sglang/srt/function_call/gemma4_detector.py` added +445/-0 (445 lines); hunks: -0,0 +1,445; symbols: _parse_gemma4_value, _parse_gemma4_array, _parse_gemma4_args, _find_matching_brace
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -0,0 +1,1009 @@
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -0,0 +1,878 @@
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/gemma4_audio.py
@@ -0,0 +1,873 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` added +1009/-0; `python/sglang/srt/models/gemma4_mm.py` added +878/-0; `python/sglang/srt/models/gemma4_audio.py` added +873/-0; `python/sglang/srt/models/gemma4_vision.py` added +599/-0; `python/sglang/srt/function_call/gemma4_detector.py` added +445/-0; `python/sglang/srt/multimodal/processors/gemma4.py` added +145/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/function_call/test_function_call_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #24048 - [VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar

- Link: https://github.com/sgl-project/sglang/pull/24048
- Status/date: merged / 2026-05-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; associated commits `e5c58eb9d627`
- Diff scope read: GitHub Pull Request files API returned 5 files, +158/-6, 223 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar"; model line: Gemma 4; category: performance/backend optimization; main diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; technical summary: Covers "[VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +29/-2 (31 lines); hunks: -27,7 +27,10; -545,12 +548,36 @@ def forward(; symbols: forward, touching `forward`; `python/sglang/srt/models/gemma4_mm.py` modified +20/-0 (20 lines); hunks: -224,6 +224,26 @@ def __init__(; symbols: __init__, model, satisfies, __setattr__, touching `__init__, model, satisfies`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +29/-2 (31 lines); hunks: -27,7 +27,10; -545,12 +548,36 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/gemma4_mm.py` modified +20/-0 (20 lines); hunks: -224,6 +224,26 @@ def __init__(; symbols: __init__, model, satisfies, __setattr__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -27,7 +27,10 @@
-from sglang.srt.layers.gemma4_fused_ops import gemma_rmsnorm_residual_scalar
+from sglang.srt.layers.gemma4_fused_ops import (
+    gemma_dual_rmsnorm_residual_scalar,
+    gemma_rmsnorm_residual_scalar,
+)
@@ -545,12 +548,36 @@ def forward(
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -224,6 +224,26 @@ def __init__(
+    @property
+    def model(self):
+        # Alias .model to .language_model so this class satisfies the piecewise
+        # CUDA graph gate (which checks `hasattr(model, "model")`). Implemented
+        # as a property to avoid registering a duplicate submodule in
+        # `_modules`, which would double state_dict keys and disturb
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +29/-2; `python/sglang/srt/models/gemma4_mm.py` modified +20/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/gemma4_fused_ops.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24436 - [Gemma 4] Adding MTP support

- Link: https://github.com/sgl-project/sglang/pull/24436
- Status/date: merged / 2026-05-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_mtp.py`; associated commits `d2c1034163cd`
- Diff scope read: GitHub Pull Request files API returned 11 files, +1949/-7, 2060 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Gemma 4] Adding MTP support"; model line: Gemma 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`; technical summary: Covers "[Gemma 4] Adding MTP support"; the main implementation surface is `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mtp.py` added +398/-0 (398 lines); hunks: -0,0 +1,398; symbols: _get_text_config, _resolve_target_text_model, Gemma4AssistantForCausalLM, __init__, touching `_get_text_config, _resolve_target_text_model, Gemma4AssistantForCausalLM`; `python/sglang/srt/models/gemma4_mm.py` modified +5/-0 (5 lines); hunks: -256,6 +256,11 @@ def pad_input_ids(; symbols: pad_input_ids, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size, touching `pad_input_ids, get_input_embeddings, get_embed_and_head`; `python/sglang/srt/models/gemma4_causal.py` modified +3/-0 (3 lines); hunks: -878,6 +878,9 @@ def __init__(; symbols: __init__, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size, touching `__init__, get_input_embeddings, get_embed_and_head`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_mtp.py` added +398/-0 (398 lines); hunks: -0,0 +1,398; symbols: _get_text_config, _resolve_target_text_model, Gemma4AssistantForCausalLM, __init__
  - `python/sglang/srt/models/gemma4_mm.py` modified +5/-0 (5 lines); hunks: -256,6 +256,11 @@ def pad_input_ids(; symbols: pad_input_ids, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size
  - `python/sglang/srt/models/gemma4_causal.py` modified +3/-0 (3 lines); hunks: -878,6 +878,9 @@ def __init__(; symbols: __init__, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mtp.py
@@ -0,0 +1,398 @@
+# Copyright 2026 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -256,6 +256,11 @@ def pad_input_ids(
+    def get_embed_and_head(self) -> Tuple[torch.Tensor, torch.Tensor]:
+        # Gemma 4 multimodal ties its LM head to the text embed_tokens
+        embed = self.language_model.embed_tokens.weight
+        return embed, embed
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -878,6 +878,9 @@ def __init__(
+    def get_embed_and_head(self) -> Tuple[torch.Tensor, torch.Tensor]:
+        return self.model.embed_tokens.weight, self.lm_head.weight
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mtp.py` added +398/-0; `python/sglang/srt/models/gemma4_mm.py` modified +5/-0; `python/sglang/srt/models/gemma4_causal.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24696 - [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader

- Link: https://github.com/sgl-project/sglang/pull/24696
- Status/date: merged / 2026-05-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; associated commits `d3fd91ed9726`
- Diff scope read: GitHub Pull Request files API returned 4 files, +317/-15, 369 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader"; model line: Gemma 4; category: performance/backend optimization; main diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; technical summary: Covers "[Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +58/-15 (73 lines); hunks: -29,6 +29,7; -339,22 +340,64 @@ def forward(; symbols: forward, touching `forward`; `python/sglang/srt/models/gemma4_mm.py` modified +35/-0 (35 lines); hunks: -787,6 +787,41 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +58/-15 (73 lines); hunks: -29,6 +29,7; -339,22 +340,64 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/gemma4_mm.py` modified +35/-0 (35 lines); hunks: -787,6 +787,41 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -29,6 +29,7 @@
+    gemma_qkv_rmsnorm,
@@ -339,22 +340,64 @@ def forward(
-        q = q.unflatten(-1, (self.num_heads, self.head_dim))
-        q = self.q_norm(q)
-        q = q.flatten(-2, -1)
-        # Check if we should use shared KV cache
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -787,6 +787,41 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+            # Per-expert checkpoint format used by compressed-tensors / FP8
+            # (e.g. RedHatAI/*-FP8-Dynamic). Each expert is stored as a
+            # separate key with shape (out, in):
+            #   experts.<id>.gate_proj.{weight,weight_scale}
+            #   experts.<id>.up_proj.{weight,weight_scale}
+            #   experts.<id>.down_proj.{weight,weight_scale}
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +58/-15; `python/sglang/srt/models/gemma4_mm.py` modified +35/-0
- Risk and verification: The diff ships test coverage in `test/registered/models/test_gemma4_fp8_per_expert_loading.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #25284 - Support Gemma4 Pipeline Parallelism

- Link: https://github.com/sgl-project/sglang/pull/25284
- Status/date: merged / 2026-05-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; associated commits `4c0ce0345d0d`
- Diff scope read: GitHub Pull Request files API returned 5 files, +487/-68, 867 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support Gemma4 Pipeline Parallelism"; model line: Gemma 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; technical summary: Covers "Support Gemma4 Pipeline Parallelism"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +212/-34 (246 lines); hunks: -14,7 +14,7; -25,6 +25,7; symbols: get_attention_sliding_window_size, pp_filter_load_weight, Gemma4Router, __init__, touching `get_attention_sliding_window_size, pp_filter_load_weight, Gemma4Router`; `python/sglang/srt/models/gemma4_mm.py` modified +133/-33 (166 lines); hunks: -28,11 +28,14; -43,13 +46,17; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +212/-34 (246 lines); hunks: -14,7 +14,7; -25,6 +25,7; symbols: get_attention_sliding_window_size, pp_filter_load_weight, Gemma4Router, __init__
  - `python/sglang/srt/models/gemma4_mm.py` modified +133/-33 (166 lines); hunks: -28,11 +28,14; -43,13 +46,17; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -14,7 +14,7 @@
-from typing import Iterable, List, Optional, Set, Tuple
+from typing import Iterable, List, Optional, Set, Tuple, Union
@@ -25,6 +25,7 @@
+    get_pp_group,
@@ -45,8 +46,9 @@
+from sglang.srt.layers.utils import PPMissingLayer, get_layer_id
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -28,11 +28,14 @@
+from sglang.srt.distributed import get_pp_group
+from sglang.srt.layers.utils import PPMissingLayer
+from sglang.srt.layers.vocab_parallel_embedding import ParallelLMHead
@@ -43,13 +46,17 @@
-from sglang.srt.model_executor.forward_batch_info import ForwardBatch, ForwardMode
+from sglang.srt.model_executor.forward_batch_info import (
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +212/-34; `python/sglang/srt/models/gemma4_mm.py` modified +133/-33
- Risk and verification: The diff ships test coverage in `python/sglang/test/test_utils.py`, `test/registered/distributed/test_pp_single_node.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #25054 - Support Gemma4 MoE NVFP4

- Link: https://github.com/sgl-project/sglang/pull/25054
- Status/date: merged / 2026-05-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; associated commits `847cbada9c42`
- Diff scope read: GitHub Pull Request files API returned 9 files, +271/-118, 605 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support Gemma4 MoE NVFP4"; model line: Gemma 4; category: performance/backend optimization; main diff: `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`; technical summary: Covers "Support Gemma4 MoE NVFP4"; the main implementation surface is `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mm.py` modified +88/-61 (149 lines); hunks: -33,6 +33,7; -817,6 +818,27 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, touching `load_weights`; `python/sglang/srt/models/gemma4_causal.py` modified +81/-27 (108 lines); hunks: -42,6 +42,7; -1140,14 +1141,31 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_mm.py` modified +88/-61 (149 lines); hunks: -33,6 +33,7; -817,6 +818,27 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
  - `python/sglang/srt/models/gemma4_causal.py` modified +81/-27 (108 lines); hunks: -42,6 +42,7; -1140,14 +1141,31 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -33,6 +33,7 @@
+from sglang.srt.layers.moe.fused_moe_triton.layer import FusedMoE
@@ -817,6 +818,27 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+        # Per-expert checkpoint format used by compressed-tensors / FP8
+        # (e.g. RedHatAI/*-FP8-Dynamic) and by ModelOpt NVFP4
+        # (e.g. nvidia/Gemma-4-*-NVFP4). Each expert is stored as a
+        # separate key with shape (out, in):
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -42,6 +42,7 @@
+from sglang.srt.layers.moe.fused_moe_triton.layer import FusedMoE
@@ -1140,14 +1141,31 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-        expert_params_mapping = [
+        fused_expert_params_mapping = [
+        # Per-expert checkpoint format used by compressed-tensors / FP8
+        # (e.g. RedHatAI/*-FP8-Dynamic) and by ModelOpt NVFP4
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +88/-61; `python/sglang/srt/models/gemma4_causal.py` modified +81/-27
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/cutlass_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26026 - [bug fix] Fix 3 issues when using Gemma4 MTP

- Link: https://github.com/sgl-project/sglang/pull/26026
- Status/date: merged / 2026-05-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`; associated commits `89ff2bc1115c`
- Diff scope read: GitHub Pull Request files API returned 3 files, +20/-11, 66 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[bug fix] Fix 3 issues when using Gemma4 MTP"; model line: Gemma 4; category: bug fix; main diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`; technical summary: Covers "[bug fix] Fix 3 issues when using Gemma4 MTP"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +11/-6 (17 lines); hunks: -1147,7 +1147,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -1159,11 +1160,15 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights, touching `load_weights`; `python/sglang/srt/models/gemma4_mtp.py` modified +2/-0 (2 lines); hunks: -21,6 +21,7; -72,6 +73,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +11/-6 (17 lines); hunks: -1147,7 +1147,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -1159,11 +1160,15 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights
  - `python/sglang/srt/models/gemma4_mtp.py` modified +2/-0 (2 lines); hunks: -21,6 +21,7; -72,6 +73,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -1147,7 +1147,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-        num_experts = self.config.num_experts
+        # Dense subclasses (e.g. the Gemma4 MTP assistant) reuse this.
+        num_experts = getattr(self.config, "num_experts", None) or 0
@@ -1159,11 +1160,15 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-        per_expert_params_mapping = FusedMoE.make_expert_params_mapping(
-            ckpt_gate_proj_name="gate_proj",
diff -- python/sglang/srt/models/gemma4_mtp.py
@@ -21,6 +21,7 @@
+from sglang.srt.distributed import get_pp_group
@@ -72,6 +73,7 @@ def __init__(
+        self.pp_group = get_pp_group()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +11/-6; `python/sglang/srt/models/gemma4_mtp.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/server_args.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24552 - [Gemma4] Add test for MTP models

- Link: https://github.com/sgl-project/sglang/pull/24552
- Status/date: merged / 2026-05-28
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/spec/test_gemma4_mtp_31b_extra.py`; associated commits `9040feebd854`
- Diff scope read: GitHub Pull Request files API returned 3 files, +535/-0, 538 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Gemma4] Add test for MTP models"; model line: Gemma 4; category: docs/tests/CI; main diff: `test/registered/spec/test_gemma4_mtp_31b_extra.py`; technical summary: Covers "[Gemma4] Add test for MTP models"; the main implementation surface is `test/registered/spec/test_gemma4_mtp_31b_extra.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/spec/test_gemma4_mtp_31b_extra.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4MTP31B, _server_env, touching `get_server_info, get_avg_spec_accept_length, TestGemma4MTP31B`.
- Code diff details:
  - `test/registered/spec/test_gemma4_mtp_31b_extra.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4MTP31B, _server_env
- Key code excerpts:

```diff
diff -- test/registered/spec/test_gemma4_mtp_31b_extra.py
@@ -0,0 +1,185 @@
+import os
+import unittest
+from types import SimpleNamespace
+from typing import Optional
+import requests
+from sglang.srt.utils import kill_process_tree
```

- Reviewed files:
  - tests: `test/registered/spec/test_gemma4_mtp_31b_extra.py` added +185/-0
- Risk and verification: The diff ships test coverage in `test/registered/spec/test_frozen_kv_mtp.py`, `test/registered/spec/test_gemma4_mtp_26b_a4b_extra.py`, `test/registered/spec/test_gemma4_mtp_31b_extra.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #26502 - perf(gemma4): single-launch fused router (topk + softmax + scale)

- Link: https://github.com/sgl-project/sglang/pull/26502
- Status/date: merged / 2026-06-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`; associated commits `5ae8d286d2b8`
- Diff scope read: GitHub Pull Request files API returned 3 files, +229/-0, 248 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "perf(gemma4): single-launch fused router (topk + softmax + scale)"; model line: Gemma 4; category: performance/backend optimization; main diff: `python/sglang/srt/models/gemma4_causal.py`; technical summary: Covers "perf(gemma4): single-launch fused router (topk + softmax + scale)"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +9/-0 (9 lines); hunks: -30,6 +30,7; -220,6 +221,14 @@ def routing_function(; symbols: routing_function, touching `routing_function`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +9/-0 (9 lines); hunks: -30,6 +30,7; -220,6 +221,14 @@ def routing_function(; symbols: routing_function
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -30,6 +30,7 @@
+    gemma4_fused_routing,
@@ -220,6 +221,14 @@ def routing_function(
+            if (
+                gating_output.is_cuda
+                and gating_output.dim() == 2
+                and gating_output.dtype
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +9/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/test_gemma4_fused_routing.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27101 - [Gemma4] Use hard GSM8K accuracy floor for 31B MTP test

- Link: https://github.com/sgl-project/sglang/pull/27101
- Status/date: merged / 2026-06-03
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/spec/test_gemma4_mtp_31b_extra.py`; associated commits `6d5361569988`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-6, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Gemma4] Use hard GSM8K accuracy floor for 31B MTP test"; model line: Gemma 4; category: docs/tests/CI; main diff: `test/registered/spec/test_gemma4_mtp_31b_extra.py`; technical summary: Covers "[Gemma4] Use hard GSM8K accuracy floor for 31B MTP test"; the main implementation surface is `test/registered/spec/test_gemma4_mtp_31b_extra.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/spec/test_gemma4_mtp_31b_extra.py` modified +2/-6 (8 lines); hunks: -28,14 +28,10.
- Code diff details:
  - `test/registered/spec/test_gemma4_mtp_31b_extra.py` modified +2/-6 (8 lines); hunks: -28,14 +28,10
- Key code excerpts:

```diff
diff -- test/registered/spec/test_gemma4_mtp_31b_extra.py
@@ -28,14 +28,10 @@
-GSM8K_SCORE_MARGIN = 0.03
-# Initial values are seeded from current Gemma4 GSM8K observations in the
-# cookbook. Replace each top-k entry with exact MTP first-200-sample scores as
-# CI calibration data becomes available.
-OBSERVED_GSM8K_SCORES = {1: 0.805, 3: 0.805}
-GSM8K_SCORE_THRESHOLD = min(OBSERVED_GSM8K_SCORES.values()) - GSM8K_SCORE_MARGIN
```

- Reviewed files:
  - tests: `test/registered/spec/test_gemma4_mtp_31b_extra.py` modified +2/-6
- Risk and verification: The diff ships test coverage in `test/registered/spec/test_gemma4_mtp_31b_extra.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #23280 - [XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU

- Link: https://github.com/sgl-project/sglang/pull/23280
- Status/date: merged / 2026-06-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`; associated commits `2c8357f79471`
- Diff scope read: GitHub Pull Request files API returned 6 files, +348/-34, 641 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU"; model line: Gemma 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/gemma4_causal.py`; technical summary: Covers "[XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +44/-17 (61 lines); hunks: -34,6 +34,7; -56,6 +57,9; symbols: __init__, fuse_scale, forward, routing_function, touching `__init__, fuse_scale, forward`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +44/-17 (61 lines); hunks: -34,6 +34,7; -56,6 +57,9; symbols: __init__, fuse_scale, forward, routing_function
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -34,6 +34,7 @@
+    gemma_routing_post_topk,
@@ -56,6 +57,9 @@
+from sglang.srt.models.utils import (
+    create_fused_set_kv_buffer_arg,
+)
@@ -145,7 +149,8 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +44/-17
- Risk and verification: The diff ships test coverage in `test/registered/xpu/test_gemma_4_e2b.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #26320 - fix(gemma4): register image/video/audio token_regex for HF-expanded prompts

- Link: https://github.com/sgl-project/sglang/pull/26320
- Status/date: merged / 2026-06-09
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/gemma4.py`; associated commits `98fe7e326ed4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +13/-0, 30 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(gemma4): register image/video/audio token_regex for HF-expanded prompts"; model line: Gemma 4; category: bug fix; main diff: `python/sglang/srt/multimodal/processors/gemma4.py`; technical summary: Covers "fix(gemma4): register image/video/audio token_regex for HF-expanded prompts"; the main implementation surface is `python/sglang/srt/multimodal/processors/gemma4.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/gemma4.py` modified +13/-0 (13 lines); hunks: -12,6 +12,7; -41,9 +42,21 @@ def __init__(self, hf_config, server_args, _processor, *args,...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/gemma4.py` modified +13/-0 (13 lines); hunks: -12,6 +12,7; -41,9 +42,21 @@ def __init__(self, hf_config, server_args, _processor, *args,...; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/gemma4.py
@@ -12,6 +12,7 @@
+import re
@@ -41,9 +42,21 @@ def __init__(self, hf_config, server_args, _processor, *args, **kwargs):
+            image_token="<|image|>",
+            image_token_regex=re.compile(
+                r"<\|image>(?:<\|image\|>)+<image\|>|<\|image\|>"
+            ),
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/gemma4.py` modified +13/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/gemma4.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26147 - [NPU] Add Gemma4 Sliding Window Attention support on Ascend backend

- Link: https://github.com/sgl-project/sglang/pull/26147
- Status/date: merged / 2026-06-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`; associated commits `3a3a75946404`
- Diff scope read: GitHub Pull Request files API returned 14 files, +563/-132, 979 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Add Gemma4 Sliding Window Attention support on Ascend backend"; model line: Gemma 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`; technical summary: Covers "[NPU] Add Gemma4 Sliding Window Attention support on Ascend backend"; the main implementation surface is `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mm.py` modified +10/-3 (13 lines); hunks: -608,9 +608,16 @@ def forward(; symbols: forward, touching `forward`; `python/sglang/srt/models/gemma4_causal.py` modified +3/-1 (4 lines); hunks: -295,7 +295,9 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_mm.py` modified +10/-3 (13 lines); hunks: -608,9 +608,16 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/gemma4_causal.py` modified +3/-1 (4 lines); hunks: -295,7 +295,9 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -608,9 +608,16 @@ def forward(
-            ple_ids[input_ids == self.config.image_token_id] = pad_id
-            ple_ids[input_ids == self.config.video_token_id] = pad_id
-            ple_ids[input_ids == self.config.audio_token_id] = pad_id
+            # Use torch.where instead of boolean indexing for NPU graph compatibility
+            ple_ids = torch.where(
+                input_ids == self.config.image_token_id, pad_id, ple_ids
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -295,7 +295,9 @@ def __init__(
-            config.sliding_window if layer_type == "sliding_attention" else None
+            get_attention_sliding_window_size(config)
+            if layer_type == "sliding_attention"
+            else -1
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +10/-3; `python/sglang/srt/models/gemma4_causal.py` modified +3/-1
- Risk and verification: The diff ships test coverage in `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_gemma_4_26b_a4b_it_llm.py`, `test/manual/ascend/llm_models/test_npu_gemma_4_31b_llm.py`, `test/manual/ascend/llm_models/test_npu_gemma_4_e2b_llm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27471 - add dflash gemma4 support

- Link: https://github.com/sgl-project/sglang/pull/27471
- Status/date: merged / 2026-06-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py`; associated commits `5ea0d1d09381`
- Diff scope read: GitHub Pull Request files API returned 4 files, +211/-16, 259 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "add dflash gemma4 support"; model line: Gemma 4; category: performance/backend optimization; main diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py`; technical summary: Covers "add dflash gemma4 support"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +8/-0 (8 lines); hunks: -1127,6 +1127,14 @@ def get_attention_sliding_window_size(self):; symbols: get_attention_sliding_window_size, dtype, set_dflash_layers_to_capture, forward, touching `get_attention_sliding_window_size, dtype, set_dflash_layers_to_capture`; `python/sglang/srt/models/gemma4_mm.py` modified +8/-0 (8 lines); hunks: -301,6 +301,14 @@ def get_embed_and_head(self) -> Tuple[torch.Tensor, torch.T...; symbols: get_embed_and_head, get_attention_sliding_window_size, set_dflash_layers_to_capture, prepare_attn_masks, touching `get_embed_and_head, get_attention_sliding_window_size, set_dflash_layers_to_capture`; `test/registered/spec/test_gemma4_dflash_31b_extra.py` added +177/-0 (177 lines); hunks: -0,0 +1,177; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4DFlash31B, _common_server_args, touching `get_server_info, get_avg_spec_accept_length, TestGemma4DFlash31B`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +8/-0 (8 lines); hunks: -1127,6 +1127,14 @@ def get_attention_sliding_window_size(self):; symbols: get_attention_sliding_window_size, dtype, set_dflash_layers_to_capture, forward
  - `python/sglang/srt/models/gemma4_mm.py` modified +8/-0 (8 lines); hunks: -301,6 +301,14 @@ def get_embed_and_head(self) -> Tuple[torch.Tensor, torch.T...; symbols: get_embed_and_head, get_attention_sliding_window_size, set_dflash_layers_to_capture, prepare_attn_masks
  - `test/registered/spec/test_gemma4_dflash_31b_extra.py` added +177/-0 (177 lines); hunks: -0,0 +1,177; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4DFlash31B, _common_server_args
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -1127,6 +1127,14 @@ def get_attention_sliding_window_size(self):
+    def set_dflash_layers_to_capture(self, layer_ids: list[int]):
+        if layer_ids is None:
+            raise ValueError(
+                "DFLASH requires explicit layer_ids for aux hidden capture."
+            )
+        self.capture_aux_hidden_states = True
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -301,6 +301,14 @@ def get_embed_and_head(self) -> Tuple[torch.Tensor, torch.Tensor]:
+    def set_dflash_layers_to_capture(self, layer_ids: List[int]):
+        if layer_ids is None:
+            raise ValueError(
+                "DFLASH requires explicit layer_ids for aux hidden capture."
+            )
+        self.capture_aux_hidden_states = True
diff -- test/registered/spec/test_gemma4_dflash_31b_extra.py
@@ -0,0 +1,177 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +8/-0; `python/sglang/srt/models/gemma4_mm.py` modified +8/-0
  - tests: `test/registered/spec/test_gemma4_dflash_31b_extra.py` added +177/-0
- Risk and verification: The diff ships test coverage in `test/registered/spec/test_gemma4_dflash_31b_extra.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31672 - fix(gemma4): prevent attention mask offset overflow

- Link: https://github.com/sgl-project/sglang/pull/31672
- Status/date: merged / 2026-07-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_mm.py`; associated commits `609fe1c0d1a6`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(gemma4): prevent attention mask offset overflow"; model line: Gemma 4; category: bug fix; main diff: `python/sglang/srt/models/gemma4_mm.py`; technical summary: Covers "fix(gemma4): prevent attention mask offset overflow"; the main implementation surface is `python/sglang/srt/models/gemma4_mm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mm.py` modified +1/-1 (2 lines); hunks: -335,7 +335,7 @@ def prepare_attn_masks(; symbols: prepare_attn_masks, touching `prepare_attn_masks`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_mm.py` modified +1/-1 (2 lines); hunks: -335,7 +335,7 @@ def prepare_attn_masks(; symbols: prepare_attn_masks
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -335,7 +335,7 @@ def prepare_attn_masks(
-            forward_batch.batch_size + 1, dtype=torch.int32, device=input_ids.device
+            forward_batch.batch_size + 1, dtype=torch.int64, device=input_ids.device
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gemma4_mm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22498 - [CPU] Add support for Gemma4 on Xeon

- Link: https://github.com/sgl-project/sglang/pull/22498
- Status/date: merged / 2026-08-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_vision.py`; associated commits `b6d7602914d1`
- Diff scope read: GitHub Pull Request files API returned 27 files, +514/-106, 1253 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CPU] Add support for Gemma4 on Xeon"; model line: Gemma 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_vision.py`; technical summary: Covers "[CPU] Add support for Gemma4 on Xeon"; the main implementation surface is `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_vision.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mm.py` modified +29/-11 (40 lines); hunks: -59,13 +59,20; -241,9 +248,15 @@ def __init__(; symbols: __init__, forward, load_weights, get_embed_and_head, touching `__init__, forward, load_weights`; `python/sglang/srt/models/gemma4_causal.py` modified +27/-9 (36 lines); hunks: -74,6 +74,21 @@ def get_attention_sliding_window_size(config):; -109,11 +124,12 @@ def pp_filter_load_weight(; symbols: get_attention_sliding_window_size, load_tied_lm_head, pp_filter_load_weight, __init__, touching `get_attention_sliding_window_size, load_tied_lm_head, pp_filter_load_weight`; `python/sglang/srt/models/gemma4_vision.py` modified +25/-6 (31 lines); hunks: -30,7 +30,17; -173,7 +183,9 @@ def __init__(; symbols: __init__, _select_backend, forward, touching `__init__, _select_backend, forward`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_mm.py` modified +29/-11 (40 lines); hunks: -59,13 +59,20; -241,9 +248,15 @@ def __init__(; symbols: __init__, forward, load_weights, get_embed_and_head
  - `python/sglang/srt/models/gemma4_causal.py` modified +27/-9 (36 lines); hunks: -74,6 +74,21 @@ def get_attention_sliding_window_size(config):; -109,11 +124,12 @@ def pp_filter_load_weight(; symbols: get_attention_sliding_window_size, load_tied_lm_head, pp_filter_load_weight, __init__
  - `python/sglang/srt/models/gemma4_vision.py` modified +25/-6 (31 lines); hunks: -30,7 +30,17; -173,7 +183,9 @@ def __init__(; symbols: __init__, _select_backend, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -59,13 +59,20 @@
-from sglang.srt.models.gemma4_causal import Gemma4TextModel, pp_filter_load_weight
+from sglang.srt.models.gemma4_causal import (
+    Gemma4TextModel,
+    load_tied_lm_head,
+    pp_filter_load_weight,
+)
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -74,6 +74,21 @@ def get_attention_sliding_window_size(config):
+def load_tied_lm_head(
+    loaded_weight, *, params_dict, loaded_params, head_param_name="lm_head.weight"
+):
+    """Load a tied embedding into an lm_head the runtime could not alias.
+    No-op when this rank holds no lm_head.
+    """
diff -- python/sglang/srt/models/gemma4_vision.py
@@ -30,7 +30,17 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +29/-11; `python/sglang/srt/models/gemma4_causal.py` modified +27/-9; `python/sglang/srt/models/gemma4_vision.py` modified +25/-6
- Risk and verification: The diff ships test coverage in `python/sglang/test/cpu_test_utils.py`, `test/registered/cpu/test_extend.py`, `test/registered/cpu/test_moe.py`, `test/registered/cpu/test_rope.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #32440 - fix(gemma4): quantize MTP bridge projections

- Link: https://github.com/sgl-project/sglang/pull/32440
- Status/date: merged / 2026-08-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_mtp.py`; associated commits `b1707996e8c5`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(gemma4): quantize MTP bridge projections"; model line: Gemma 4; category: bug fix; main diff: `python/sglang/srt/models/gemma4_mtp.py`; technical summary: Covers "fix(gemma4): quantize MTP bridge projections"; the main implementation surface is `python/sglang/srt/models/gemma4_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mtp.py` modified +2/-2 (4 lines); hunks: -91,7 +91,7 @@ def __init__(; -103,7 +103,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_mtp.py` modified +2/-2 (4 lines); hunks: -91,7 +91,7 @@ def __init__(; -103,7 +103,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mtp.py
@@ -91,7 +91,7 @@ def __init__(
-            quant_config=None,
+            quant_config=quant_config,
@@ -103,7 +103,7 @@ def __init__(
-            quant_config=None,
+            quant_config=quant_config,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mtp.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gemma4_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #35809 - fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration

- Link: https://github.com/sgl-project/sglang/pull/35809
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_unified.py`; associated commits `08b192240540`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration"; model line: Gemma 4; category: bug fix; main diff: `python/sglang/srt/models/gemma4_unified.py`; technical summary: Covers "fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration"; the main implementation surface is `python/sglang/srt/models/gemma4_unified.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_unified.py` modified +2/-1 (3 lines); hunks: -190,7 +190,8 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_unified.py` modified +2/-1 (3 lines); hunks: -190,7 +190,8 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_unified.py
@@ -190,7 +190,8 @@ def __init__(
-        if self.pp_group.world_size == 1 and text_tie:
+        self.lm_head_is_tied = self.pp_group.world_size == 1 and text_tie
+        if self.lm_head_is_tied:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_unified.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/gemma4_unified.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #42311 - [Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries

- Link: https://github.com/sgl-project/sglang/pull/42311
- Status/date: merged / 2026-10-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_causal.py`; associated commits `71b04e02cfd8`
- Diff scope read: GitHub Pull Request files API returned 10 files, +433/-174, 1082 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries"; model line: Gemma 4; category: model implementation change; main diff: `python/sglang/srt/models/gemma4_causal.py`; technical summary: Covers "[Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries"; the main implementation surface is `python/sglang/srt/models/gemma4_causal.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_causal.py` modified +96/-46 (142 lines); hunks: -33,6 +33,16; -219,6 +229,7 @@ def __init__(; symbols: __init__, routing_function, forward, touching `__init__, routing_function, forward`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_causal.py` modified +96/-46 (142 lines); hunks: -33,6 +33,16; -219,6 +229,7 @@ def __init__(; symbols: __init__, routing_function, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_causal.py
@@ -33,6 +33,16 @@
+from sglang.srt.layers.aux_hidden_states import AuxHiddenStateList
+from sglang.srt.layers.layer_boundary import (
+    SumGroup,
+    declare_attn,
+    declare_ffn,
+    make_stages,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +96/-46
- Risk and verification: The diff ships test coverage in `test/registered/unit/layer_boundary/test_boundary_output_contracts.py`, `test/registered/unit/models/test_zaya_mod_tp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #42019 - [Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support

- Link: https://github.com/sgl-project/sglang/pull/42019
- Status/date: merged / 2026-10-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/gemma4_mm.py`; associated commits `37678784c637`
- Diff scope read: GitHub Pull Request files API returned 11 files, +485/-25, 824 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support"; model line: Gemma 4; category: model support/runtime entry; main diff: `python/sglang/srt/models/gemma4_mm.py`; technical summary: Covers "[Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support"; the main implementation surface is `python/sglang/srt/models/gemma4_mm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mm.py` modified +44/-4 (48 lines); hunks: -335,11 +335,51 @@ def prepare_attn_masks(; -413,10 +453,10 @@ def prepare_attn_masks(; symbols: prepare_attn_masks, get_image_feature, touching `prepare_attn_masks, get_image_feature`.
- Code diff details:
  - `python/sglang/srt/models/gemma4_mm.py` modified +44/-4 (48 lines); hunks: -335,11 +335,51 @@ def prepare_attn_masks(; -413,10 +453,10 @@ def prepare_attn_masks(; symbols: prepare_attn_masks, get_image_feature
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -335,11 +335,51 @@ def prepare_attn_masks(
-        Currently only the TritonAttnBackend supports this.
+        Triton and FA4 use causal attention for image spans split across chunks.
-        if not isinstance(get_attn_backend(), TritonAttnBackend):
+        attn_backend = get_attn_backend()
+        prefill_backend = getattr(attn_backend, "prefill_backend", attn_backend)
+        if getattr(prefill_backend, "fa_impl_ver", None) == 4:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +44/-4
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/attention/test_flash_attention_4.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46816 - [Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend

- Link: https://github.com/sgl-project/sglang/pull/46816
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/Google/Gemma4.mdx`, `python/sglang/srt/models/gemma4_mm.py`; associated commits `cc69762cb73c`
- Diff scope read: GitHub Pull Request files API returned 6 files, +139/-9, 259 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend"; model line: Gemma 4; category: bug fix; main diff: `python/sglang/srt/models/gemma4_mm.py`, `docs/cookbook/autoregressive/Google/Gemma4.mdx`; technical summary: Covers "[Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend"; the main implementation surface is `python/sglang/srt/models/gemma4_mm.py`, `docs/cookbook/autoregressive/Google/Gemma4.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/gemma4_mm.py` modified +30/-2 (32 lines); hunks: -66,7 +66,7; -327,17 +327,29 @@ def prepare_attn_masks(; symbols: prepare_attn_masks, touching `prepare_attn_masks`; `docs/cookbook/autoregressive/Google/Gemma4.mdx` modified +1/-0 (1 lines); hunks: -107,6 +107,7 @@ The Gemma 4 series offers models in various sizes and archit....
- Code diff details:
  - `python/sglang/srt/models/gemma4_mm.py` modified +30/-2 (32 lines); hunks: -66,7 +66,7; -327,17 +327,29 @@ def prepare_attn_masks(; symbols: prepare_attn_masks
  - `docs/cookbook/autoregressive/Google/Gemma4.mdx` modified +1/-0 (1 lines); hunks: -107,6 +107,7 @@ The Gemma 4 series offers models in various sizes and archit...
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -66,7 +66,7 @@
-from sglang.srt.utils import add_prefix, cpu_has_amx_support, is_cpu
+from sglang.srt.utils import add_prefix, cpu_has_amx_support, is_cpu, is_xpu
@@ -327,17 +327,29 @@ def prepare_attn_masks(
+        sliding_layers_only: bool = True,
-        tokens), not across items.
+        tokens), not across items, and only for checkpoints with
diff -- docs/cookbook/autoregressive/Google/Gemma4.mdx
@@ -107,6 +107,7 @@ The Gemma 4 series offers models in various sizes and architectures, optimized f
+- **Attention backend on Intel XPU (BMG)**: for the 12B, 26B-A4B and 31B models (`use_bidirectional_attention: "vision"`), `--attention-backend intel_xpu` gives image tokens bidir
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +30/-2
  - docs: `docs/cookbook/autoregressive/Google/Gemma4.mdx` modified +1/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/dllm/test_gemma4_diffusion.py`, `test/registered/xpu/test_xpu_gemma_bidirectional_attn.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
