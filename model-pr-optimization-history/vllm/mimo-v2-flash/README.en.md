# vllm MiMo V2 Flash Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/models/multimodal/test_mimo_v2_omni.py` | [#49815](https://github.com/vllm-project/vllm/pull/49815), [#58900](https://github.com/vllm-project/vllm/pull/58900), [#64179](https://github.com/vllm-project/vllm/pull/64179) |
| `tests/models/quantization/test_mimo_v2_qkv_shard.py` | [#57508](https://github.com/vllm-project/vllm/pull/57508), [#58184](https://github.com/vllm-project/vllm/pull/58184), [#59053](https://github.com/vllm-project/vllm/pull/59053) |
| `tests/models/quantization/test_mimo_v2_w4a16_routing.py` | [#58262](https://github.com/vllm-project/vllm/pull/58262) |
| `tests/models/test_mimo_v2_attention_backend.py` | [#64064](https://github.com/vllm-project/vllm/pull/64064) |
| `tests/v1/e2e/spec_decode/mtp/mimo/__init__.py` | no direct PR-number commit |
| `tests/v1/e2e/spec_decode/mtp/mimo/test_mtp.py` | no direct PR-number commit |
| `vllm/model_executor/models/mimo.py` | [#17433](https://github.com/vllm-project/vllm/pull/17433) |
| `vllm/model_executor/models/mimo_audio.py` | [#40967](https://github.com/vllm-project/vllm/pull/40967) |
| `vllm/model_executor/models/mimo_mtp.py` | [#17433](https://github.com/vllm-project/vllm/pull/17433), [#25136](https://github.com/vllm-project/vllm/pull/25136) |
| `vllm/model_executor/models/mimo_v2.py` | [#40967](https://github.com/vllm-project/vllm/pull/40967), [#41029](https://github.com/vllm-project/vllm/pull/41029), [#41797](https://github.com/vllm-project/vllm/pull/41797), [#45200](https://github.com/vllm-project/vllm/pull/45200), [#46104](https://github.com/vllm-project/vllm/pull/46104), [#57508](https://github.com/vllm-project/vllm/pull/57508), [#57784](https://github.com/vllm-project/vllm/pull/57784), [#58128](https://github.com/vllm-project/vllm/pull/58128), [#58142](https://github.com/vllm-project/vllm/pull/58142), [#58184](https://github.com/vllm-project/vllm/pull/58184), [#59053](https://github.com/vllm-project/vllm/pull/59053), [#64064](https://github.com/vllm-project/vllm/pull/64064) |
| `vllm/model_executor/models/mimo_v2_mtp.py` | [#40967](https://github.com/vllm-project/vllm/pull/40967), [#41905](https://github.com/vllm-project/vllm/pull/41905), [#57508](https://github.com/vllm-project/vllm/pull/57508), [#58128](https://github.com/vllm-project/vllm/pull/58128), [#58142](https://github.com/vllm-project/vllm/pull/58142) |
| `vllm/model_executor/models/mimo_v2_omni.py` | [#40967](https://github.com/vllm-project/vllm/pull/40967), [#49815](https://github.com/vllm-project/vllm/pull/49815), [#57784](https://github.com/vllm-project/vllm/pull/57784), [#58938](https://github.com/vllm-project/vllm/pull/58938), [#64179](https://github.com/vllm-project/vllm/pull/64179) |
| `vllm/parser/mimo.py` | [#58019](https://github.com/vllm-project/vllm/pull/58019) |
| `vllm/reasoning/mimo_engine_reasoning_parser.py` | [#58019](https://github.com/vllm-project/vllm/pull/58019) |
| `vllm/tool_parsers/mimo_tool_parser.py` | [#58019](https://github.com/vllm-project/vllm/pull/58019) |
| `vllm/transformers_utils/configs/mimo_v2_omni.py` | [#40967](https://github.com/vllm-project/vllm/pull/40967) |
| `vllm/transformers_utils/processors/mimo_v2_omni.py` | [#40967](https://github.com/vllm-project/vllm/pull/40967), [#43117](https://github.com/vllm-project/vllm/pull/43117) |

## PR Coverage Summary

- Git-traced PRs: 22
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 22

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-11-02 | [#64179](https://github.com/vllm-project/vllm/pull/64179) | merged | [Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6 | `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py` |
| 2026-10-29 | [#64064](https://github.com/vllm-project/vllm/pull/64064) | merged | [ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6 | `tests/models/test_mimo_v2_attention_backend.py`, `vllm/model_executor/models/mimo_v2.py` |
| 2026-10-20 | [#58184](https://github.com/vllm-project/vllm/pull/58184) | merged | [Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have | `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py` |
| 2026-10-20 | [#59053](https://github.com/vllm-project/vllm/pull/59053) | merged | [Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default | `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py` |
| 2026-10-06 | [#58128](https://github.com/vllm-project/vllm/pull/58128) | merged | [Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash | `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/model_executor/models/mimo_v2.py` |
| 2026-09-30 | [#58262](https://github.com/vllm-project/vllm/pull/58262) | merged | [ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942 | `tests/models/quantization/test_mimo_v2_w4a16_routing.py` |
| 2026-09-29 | [#58938](https://github.com/vllm-project/vllm/pull/58938) | merged | [Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images | `vllm/model_executor/models/mimo_v2_omni.py` |
| 2026-09-29 | [#58019](https://github.com/vllm-project/vllm/pull/58019) | merged | [Frontend] Support strict MiMo-V2.6 tool calling | `vllm/tool_parsers/mimo_tool_parser.py`, `vllm/reasoning/mimo_engine_reasoning_parser.py`, `vllm/parser/mimo.py` |
| 2026-09-29 | [#58142](https://github.com/vllm-project/vllm/pull/58142) | merged | [Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls | `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py` |
| 2026-09-28 | [#58900](https://github.com/vllm-project/vllm/pull/58900) | merged | [Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture) | `tests/models/multimodal/test_mimo_v2_omni.py` |
| 2026-09-20 | [#57784](https://github.com/vllm-project/vllm/pull/57784) | merged | [Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2 | `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py` |
| 2026-09-19 | [#57508](https://github.com/vllm-project/vllm/pull/57508) | merged | [Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too) | `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py` |
| 2026-08-10 | [#49815](https://github.com/vllm-project/vllm/pull/49815) | merged | [Bugfix][MiMo] Apply vision attention sinks in the window attention path | `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py` |
| 2026-07-11 | [#43117](https://github.com/vllm-project/vllm/pull/43117) | merged | fix(processor): route MiMo-V2-Omni media fetch through MediaConnector | `vllm/transformers_utils/processors/mimo_v2_omni.py` |
| 2026-07-01 | [#46104](https://github.com/vllm-project/vllm/pull/46104) | merged | [Spec Decode] Support SWA + DFlash for MiMo | `vllm/model_executor/models/mimo_v2.py` |
| 2026-06-15 | [#45200](https://github.com/vllm-project/vllm/pull/45200) | merged | [Models] Fix MiMo v2.x QKV TP sharding + FP4 support | `vllm/model_executor/models/mimo_v2.py` |
| 2026-06-11 | [#41797](https://github.com/vllm-project/vllm/pull/41797) | merged | [Attention] add triton diff-kv backend for mimo | `vllm/model_executor/models/mimo_v2.py` |
| 2026-05-09 | [#41905](https://github.com/vllm-project/vllm/pull/41905) | merged | [SpecDecoding] extend mtp support for mimo 2.5 | `vllm/model_executor/models/mimo_v2_mtp.py` |
| 2026-04-28 | [#41029](https://github.com/vllm-project/vllm/pull/41029) | merged | [Model] update for mimo v25 | `vllm/model_executor/models/mimo_v2.py` |
| 2026-04-27 | [#40967](https://github.com/vllm-project/vllm/pull/40967) | merged | [Model] Add MiMo-V2.5 support | `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/mimo_audio.py`, `vllm/transformers_utils/processors/mimo_v2_omni.py` |
| 2025-09-18 | [#25136](https://github.com/vllm-project/vllm/pull/25136) | merged | [spec decode] Fix MTP inference path for MiMo-7B model | `vllm/model_executor/models/mimo_mtp.py` |
| 2025-05-12 | [#17433](https://github.com/vllm-project/vllm/pull/17433) | merged | [Model] Support MiMo-7B inference with MTP | `vllm/model_executor/models/mimo_mtp.py`, `vllm/model_executor/models/mimo.py` |

## Per-PR Diff Audit Cards

### PR #64179 - [Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6

- Link: https://github.com/vllm-project/vllm/pull/64179
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`; associated commits `0e5b2ba118cf`
- Diff scope read: GitHub Pull Request files API returned 3 files, +111/-2, 145 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6"; model line: MiMo V2 Flash; category: docs/tests/CI; main diff: `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`; technical summary: Covers "[Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6"; the main implementation surface is `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/test_mimo_v2_omni.py` modified +101/-0 (101 lines); hunks: -5,6 +5,11; -73,3 +78,99 @@ def test_window_attention_applies_sinks(vision_attn_env, num_...; symbols: test_window_attention_applies_sinks, _build_attention, _stub_encoder_parallelism, _attention_inputs, touching `test_window_attention_applies_sinks, _build_attention, _stub_encoder_parallelism`; `vllm/model_executor/models/mimo_v2_omni.py` modified +8/-1 (9 lines); hunks: -162,7 +162,12 @@ def __init__(; -1229,6 +1234,8 @@ def get_dummy_mm_data(; symbols: __init__, get_dummy_mm_data, MiMoV2OmniForCausalLM, touching `__init__, get_dummy_mm_data, MiMoV2OmniForCausalLM`.
- Code diff details:
  - `tests/models/multimodal/test_mimo_v2_omni.py` modified +101/-0 (101 lines); hunks: -5,6 +5,11; -73,3 +78,99 @@ def test_window_attention_applies_sinks(vision_attn_env, num_...; symbols: test_window_attention_applies_sinks, _build_attention, _stub_encoder_parallelism, _attention_inputs
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +8/-1 (9 lines); hunks: -162,7 +162,12 @@ def __init__(; -1229,6 +1234,8 @@ def get_dummy_mm_data(; symbols: __init__, get_dummy_mm_data, MiMoV2OmniForCausalLM
- Key code excerpts:

```diff
diff -- tests/models/multimodal/test_mimo_v2_omni.py
@@ -5,6 +5,11 @@
+from vllm.config.multimodal import MultiModalConfig
+from vllm.model_executor.models import mimo_v2_omni
+from vllm.model_executor.models.interfaces import (
+    supports_multimodal_encoder_tp_data,
+)
@@ -73,3 +78,99 @@ def test_window_attention_applies_sinks(vision_attn_env, num_kv_heads):
diff -- vllm/model_executor/models/mimo_v2_omni.py
@@ -162,7 +162,12 @@ def __init__(
-        self.tp_rank = parallel_state.get_tensor_model_parallel_rank()
+        # Data parallel runs the whole encoder on every rank, so the rank has to
+        # collapse with the size: otherwise the per-head slices below start past
+        # the end of the head range on ranks > 0.
+        self.tp_rank = (
+            0 if use_data_parallel else parallel_state.get_tensor_model_parallel_rank()
```

- Reviewed files:
  - tests: `tests/models/multimodal/test_mimo_v2_omni.py` modified +101/-0
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` modified +8/-1
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/test_mimo_v2_omni.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64064 - [ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6

- Link: https://github.com/vllm-project/vllm/pull/64064
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_mimo_v2_attention_backend.py`, `vllm/model_executor/models/mimo_v2.py`; associated commits `a6c3635e3660`
- Diff scope read: GitHub Pull Request files API returned 10 files, +637/-31, 826 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `tests/models/test_mimo_v2_attention_backend.py`, `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6"; the main implementation surface is `tests/models/test_mimo_v2_attention_backend.py`, `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_mimo_v2_attention_backend.py` added +205/-0 (205 lines); hunks: -0,0 +1,205; symbols: bf16_default_dtype, restore_diffkv_head_size_v, state, _build_attention, touching `bf16_default_dtype, restore_diffkv_head_size_v, state`; `vllm/model_executor/models/mimo_v2.py` modified +19/-7 (26 lines); hunks: -317,15 +317,24 @@ def __init__(; -337,8 +346,11 @@ def __init__(; symbols: __init__, attribute, touching `__init__, attribute`.
- Code diff details:
  - `tests/models/test_mimo_v2_attention_backend.py` added +205/-0 (205 lines); hunks: -0,0 +1,205; symbols: bf16_default_dtype, restore_diffkv_head_size_v, state, _build_attention
  - `vllm/model_executor/models/mimo_v2.py` modified +19/-7 (26 lines); hunks: -317,15 +317,24 @@ def __init__(; -337,8 +346,11 @@ def __init__(; symbols: __init__, attribute
- Key code excerpts:

```diff
diff -- tests/models/test_mimo_v2_attention_backend.py
@@ -0,0 +1,205 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MiMo-V2.6 has head_dim 192 but v_head_dim 128, so only backends that keep
+V's width out of the K path can serve it. An explicit ``--attention-backend``
+from that set has to be honored; any other request has to fall back to the
+DiffKV auto-pick with a warning rather than mount a backend that cannot serve
diff -- vllm/model_executor/models/mimo_v2.py
@@ -317,15 +317,24 @@ def __init__(
-        # Use DiffKV backend when V has a different head dim than K.
-        # Auto-pick FA-DiffKV when FA3/4 is usable on this device, else fall
-        # back to TRITON_ATTN_DIFFKV.  Users can force a choice via
-        # `--attention-backend <FLASH_ATTN_DIFFKV|TRITON_ATTN_DIFFKV>`.
+        # V has a different head dim than K. Honor an explicit backend that
+        # declares it can serve that geometry; anything else keeps the auto-pick
```

- Reviewed files:
  - tests: `tests/models/test_mimo_v2_attention_backend.py` added +205/-0
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +19/-7
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_cache.py`, `tests/models/test_mimo_v2_attention_backend.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58184 - [Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have

- Link: https://github.com/vllm-project/vllm/pull/58184
- Status/date: merged / 2026-10-20
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`; associated commits `79218659a6d7`
- Diff scope read: GitHub Pull Request files API returned 2 files, +65/-0, 83 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have"; model line: MiMo V2 Flash; category: bug fix; main diff: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have"; the main implementation surface is `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +62/-0 (62 lines); hunks: -14,6 +14,8; -405,3 +407,63 @@ def test_wrong_chunk_count_is_detected():; symbols: test_wrong_chunk_count_is_detected, test_load_weights_pairs_split_fp8_qkv_proj_and_skips_absent_layers, touching `test_wrong_chunk_count_is_detected, test_load_weights_pairs_split_fp8_qkv_proj_and_skips_absent_layers`; `vllm/model_executor/models/mimo_v2.py` modified +3/-0 (3 lines); hunks: -1020,6 +1020,9 @@ def _try_load_fp8_qkv_proj(; symbols: _try_load_fp8_qkv_proj, touching `_try_load_fp8_qkv_proj`.
- Code diff details:
  - `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +62/-0 (62 lines); hunks: -14,6 +14,8; -405,3 +407,63 @@ def test_wrong_chunk_count_is_detected():; symbols: test_wrong_chunk_count_is_detected, test_load_weights_pairs_split_fp8_qkv_proj_and_skips_absent_layers
  - `vllm/model_executor/models/mimo_v2.py` modified +3/-0 (3 lines); hunks: -1020,6 +1020,9 @@ def _try_load_fp8_qkv_proj(; symbols: _try_load_fp8_qkv_proj
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_mimo_v2_qkv_shard.py
@@ -14,6 +14,8 @@
+from types import SimpleNamespace
@@ -405,3 +407,63 @@ def test_wrong_chunk_count_is_detected():
+def test_load_weights_pairs_split_fp8_qkv_proj_and_skips_absent_layers(monkeypatch):
+    """Through ``MiMoV2Model.load_weights``: a layer's fused fp8 ``qkv_proj``
+    weight and scale arriving in separate calls (AutoWeightsLoader groups, #58142)
+    still load; the pair for a layer the instance does not have (checkpoint
diff -- vllm/model_executor/models/mimo_v2.py
@@ -1020,6 +1020,9 @@ def _try_load_fp8_qkv_proj(
+        if f"{prefix}.weight" not in params_dict:
+            # Layer absent from this instance, e.g. truncated num_hidden_layers.
+            return True
```

- Reviewed files:
  - tests: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +62/-0
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +3/-0
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_mimo_v2_qkv_shard.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59053 - [Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default

- Link: https://github.com/vllm-project/vllm/pull/59053
- Status/date: merged / 2026-10-20
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`; associated commits `3b518982806c`
- Diff scope read: GitHub Pull Request files API returned 2 files, +327/-18, 452 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default"; the main implementation surface is `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +179/-5 (184 lines); hunks: -17,7 +17,11; -76,10 +80,10 @@ def _quantize_chunks(truth, num_heads, num_kv_heads, head_di...; symbols: _quantize_chunks, _owned_rows, _owned_index, touching `_quantize_chunks, _owned_rows, _owned_index`; `vllm/model_executor/models/mimo_v2.py` modified +148/-13 (161 lines); hunks: -234,6 +234,7 @@ def __init__(; -260,16 +261,36 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +179/-5 (184 lines); hunks: -17,7 +17,11; -76,10 +80,10 @@ def _quantize_chunks(truth, num_heads, num_kv_heads, head_di...; symbols: _quantize_chunks, _owned_rows, _owned_index
  - `vllm/model_executor/models/mimo_v2.py` modified +148/-13 (161 lines); hunks: -234,6 +234,7 @@ def __init__(; -260,16 +261,36 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_mimo_v2_qkv_shard.py
@@ -17,7 +17,11 @@
-from vllm.model_executor.models.mimo_v2 import _shard_fp8_qkv_proj
+from vllm.model_executor.models.mimo_v2 import (
+    _fused_qkv_kv_chunk_rows,
+    _shard_fp8_qkv_proj,
+    _split_qkv,
+)
diff -- vllm/model_executor/models/mimo_v2.py
@@ -234,6 +234,7 @@ def __init__(
+        fused_qkv_chunks: int = 0,
@@ -260,16 +261,36 @@ def __init__(
-        self.qkv_proj = QKVParallelLinear(
-            hidden_size,
-            self.head_dim,
-            self.total_num_heads,
```

- Reviewed files:
  - tests: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +179/-5
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +148/-13
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_mimo_v2_qkv_shard.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58128 - [Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash

- Link: https://github.com/vllm-project/vllm/pull/58128
- Status/date: merged / 2026-10-06
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`; associated commits `21d93d0d8c0e`
- Diff scope read: GitHub Pull Request files API returned 5 files, +111/-15, 321 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash"; the main implementation surface is `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -24,7 +24,7; -64,6 +64,7 @@ def __init__(; symbols: __init__, touching `__init__`; `vllm/model_executor/models/mimo_v2.py` modified +6/-0 (6 lines); hunks: -372,6 +372,10 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = "...; -389,6 +393,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -24,7 +24,7; -64,6 +64,7 @@ def __init__(; symbols: __init__
  - `vllm/model_executor/models/mimo_v2.py` modified +6/-0 (6 lines); hunks: -372,6 +372,10 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = "...; -389,6 +393,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""...; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2_mtp.py
@@ -24,7 +24,7 @@
-from vllm.config import VllmConfig
+from vllm.config import CacheConfig, VllmConfig
@@ -64,6 +64,7 @@ def __init__(
+        cache_config: CacheConfig | None = None,
@@ -100,6 +101,7 @@ def __init__(
+            cache_config=cache_config,
diff -- vllm/model_executor/models/mimo_v2.py
@@ -372,6 +372,10 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = "") -> None:
+        # cache_config.sliding_window holds MiMo's SWA window; global layers
+        # would otherwise fall back to it in Attention.
+        cache_config = vllm_config.cache_config
+        cache_config.sliding_window = None
@@ -389,6 +393,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = "") -> None:
+                cache_config=cache_config,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1; `vllm/model_executor/models/mimo_v2.py` modified +6/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_triton_unified_attention_diffkv.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58262 - [ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942

- Link: https://github.com/vllm-project/vllm/pull/58262
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_mimo_v2_w4a16_routing.py`; associated commits `16d4ac4ba3a0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +192/-5, 219 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `tests/models/quantization/test_mimo_v2_w4a16_routing.py`; technical summary: Covers "[ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942"; the main implementation surface is `tests/models/quantization/test_mimo_v2_w4a16_routing.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_mimo_v2_w4a16_routing.py` added +176/-0 (176 lines); hunks: -0,0 +1,176; symbols: mimo_routing_method, mimo_moe_config, test_ungrouped_sigmoid_router_is_deepseekv3, test_aiter_w4a16_supports_mimo_routing, touching `mimo_routing_method, mimo_moe_config, test_ungrouped_sigmoid_router_is_deepseekv3`.
- Code diff details:
  - `tests/models/quantization/test_mimo_v2_w4a16_routing.py` added +176/-0 (176 lines); hunks: -0,0 +1,176; symbols: mimo_routing_method, mimo_moe_config, test_ungrouped_sigmoid_router_is_deepseekv3, test_aiter_w4a16_supports_mimo_routing
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_mimo_v2_w4a16_routing.py
@@ -0,0 +1,176 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Routing support for the AITER Triton MXFP4 W4A16 MoE backend.
+MiMo-V2.6 uses an ungrouped sigmoid router with a per-expert correction bias
+(``scoring_func=sigmoid``, ``topk_method=noaux_tc``, ``n_group == 1``), which
+``get_routing_method_type`` classifies as ``RoutingMethodType.DeepSeekV3``.
```

- Reviewed files:
  - tests: `tests/models/quantization/test_mimo_v2_w4a16_routing.py` added +176/-0
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_mimo_v2_w4a16_routing.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58938 - [Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images

- Link: https://github.com/vllm-project/vllm/pull/58938
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2_omni.py`; associated commits `8aaeef343a10`
- Diff scope read: GitHub Pull Request files API returned 1 files, +20/-4, 45 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images"; model line: MiMo V2 Flash; category: bug fix; main diff: `vllm/model_executor/models/mimo_v2_omni.py`; technical summary: Covers "[Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images"; the main implementation surface is `vllm/model_executor/models/mimo_v2_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2_omni.py` modified +20/-4 (24 lines); hunks: -69,7 +69,10; -670,6 +673,14 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, MiMoV2OmniMultiModalDataParser, MiMoV2OmniProcessingInfo, get_supported_mm_limits, touching `load_weights, MiMoV2OmniMultiModalDataParser, MiMoV2OmniProcessingInfo`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +20/-4 (24 lines); hunks: -69,7 +69,10; -670,6 +673,14 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, MiMoV2OmniMultiModalDataParser, MiMoV2OmniProcessingInfo, get_supported_mm_limits
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2_omni.py
@@ -69,7 +69,10 @@
-from .qwen2_vl import _create_qwen2vl_field_factory
+from .qwen2_vl import (
+    Qwen2VLMultiModalDataParser,
+    _create_qwen2vl_field_factory,
+)
@@ -670,6 +673,14 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` modified +20/-4
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mimo_v2_omni.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58019 - [Frontend] Support strict MiMo-V2.6 tool calling

- Link: https://github.com/vllm-project/vllm/pull/58019
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/parser/mimo.py`, `vllm/reasoning/mimo_engine_reasoning_parser.py`, `vllm/tool_parsers/mimo_tool_parser.py`; associated commits `dfc8e0f3e2ad`
- Diff scope read: GitHub Pull Request files API returned 17 files, +243/-15, 437 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Frontend] Support strict MiMo-V2.6 tool calling"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `vllm/tool_parsers/mimo_tool_parser.py`, `vllm/reasoning/mimo_engine_reasoning_parser.py`, `vllm/parser/mimo.py`; technical summary: Covers "[Frontend] Support strict MiMo-V2.6 tool calling"; the main implementation surface is `vllm/tool_parsers/mimo_tool_parser.py`, `vllm/reasoning/mimo_engine_reasoning_parser.py`, `vllm/parser/mimo.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mimo_tool_parser.py` added +25/-0 (25 lines); hunks: -0,0 +1,25; symbols: MiMoToolParser, get_structural_tag, touching `MiMoToolParser, get_structural_tag`; `vllm/reasoning/mimo_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6; `vllm/parser/mimo.py` added +42/-0 (42 lines); hunks: -0,0 +1,42; symbols: _mimo_arg_converter, MiMoParser, __init__, touching `_mimo_arg_converter, MiMoParser, __init__`.
- Code diff details:
  - `vllm/tool_parsers/mimo_tool_parser.py` added +25/-0 (25 lines); hunks: -0,0 +1,25; symbols: MiMoToolParser, get_structural_tag
  - `vllm/reasoning/mimo_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `vllm/parser/mimo.py` added +42/-0 (42 lines); hunks: -0,0 +1,42; symbols: _mimo_arg_converter, MiMoParser, __init__
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mimo_tool_parser.py
@@ -0,0 +1,25 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from xgrammar.structural_tag import TriggeredTagsFormat
+from vllm.parser.engine.registered_adapters import MiMoParserToolAdapter
+from vllm.tool_parsers.tool_strict_level import ToolStrictLevel
+class MiMoToolParser(MiMoParserToolAdapter):  # type: ignore[valid-type, misc]
diff -- vllm/reasoning/mimo_engine_reasoning_parser.py
@@ -0,0 +1,6 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from vllm.parser.engine.registered_adapters import MiMoParserReasoningAdapter
+__all__ = ["MiMoParserReasoningAdapter"]
diff -- vllm/parser/mimo.py
@@ -0,0 +1,42 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mimo_tool_parser.py` added +25/-0; `vllm/reasoning/mimo_engine_reasoning_parser.py` added +6/-0; `vllm/parser/mimo.py` added +42/-0
- Risk and verification: The diff ships test coverage in `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt`, `requirements/test/xpu.txt`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58142 - [Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls

- Link: https://github.com/vllm-project/vllm/pull/58142
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`; associated commits `77e52645e9ba`
- Diff scope read: GitHub Pull Request files API returned 2 files, +12/-3, 29 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls"; model line: MiMo V2 Flash; category: bug fix; main diff: `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`; technical summary: Covers "[Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls"; the main implementation surface is `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2.py` modified +6/-2 (8 lines); hunks: -742,8 +742,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, touching `load_weights`; `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -266,7 +266,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2.py` modified +6/-2 (8 lines); hunks: -742,8 +742,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -266,7 +266,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2.py
@@ -742,8 +742,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-        # sharded together.
-        pending_fp8_qkv_proj: dict[str, dict[str, torch.Tensor]] = {}
+        # sharded together. The state must outlive this call: AutoWeightsLoader
+        # delegates per contiguous group of names, so a pair can straddle two
+        # calls and would otherwise be dropped silently.
+        pending_fp8_qkv_proj = getattr(self, "_pending_fp8_qkv_proj", None)
diff -- vllm/model_executor/models/mimo_v2_mtp.py
@@ -266,7 +266,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-        pending_qkv_proj: dict[str, dict[str, torch.Tensor]] = {}
+        # The pairing state must outlive this call: AutoWeightsLoader delegates
+        # per contiguous group of names, so a pair can straddle two calls and
+        # would otherwise be dropped silently.
+        pending_qkv_proj = getattr(self, "_pending_qkv_proj", None)
+        if pending_qkv_proj is None:
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +6/-2; `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58900 - [Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture)

- Link: https://github.com/vllm-project/vllm/pull/58900
- Status/date: merged / 2026-09-28
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/test_mimo_v2_omni.py`; associated commits `0da126676e38`
- Diff scope read: GitHub Pull Request files API returned 2 files, +15/-27, 66 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture)"; model line: MiMo V2 Flash; category: bug fix; main diff: `tests/models/multimodal/test_mimo_v2_omni.py`; technical summary: Covers "[Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture)"; the main implementation surface is `tests/models/multimodal/test_mimo_v2_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/test_mimo_v2_omni.py` modified +3/-18 (21 lines); hunks: -5,13 +5,7; -21,20 +15,11; symbols: vision_attn_env, touching `vision_attn_env`.
- Code diff details:
  - `tests/models/multimodal/test_mimo_v2_omni.py` modified +3/-18 (21 lines); hunks: -5,13 +5,7; -21,20 +15,11; symbols: vision_attn_env
- Key code excerpts:

```diff
diff -- tests/models/multimodal/test_mimo_v2_omni.py
@@ -5,13 +5,7 @@
-from tests.utils import ensure_current_vllm_config
-from vllm.distributed.parallel_state import (
-    init_distributed_environment,
-    initialize_model_parallel,
-)
-from vllm.utils.network_utils import get_open_port
```

- Reviewed files:
  - tests: `tests/models/multimodal/test_mimo_v2_omni.py` modified +3/-18
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/test_mimo_v2_omni.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57784 - [Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2

- Link: https://github.com/vllm-project/vllm/pull/57784
- Status/date: merged / 2026-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`; associated commits `9b2f34cad446`
- Diff scope read: GitHub Pull Request files API returned 3 files, +21/-6, 109 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`; technical summary: Covers "[Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2"; the main implementation surface is `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2.py` modified +8/-5 (13 lines); hunks: -27,6 +27,7; -156,14 +157,16 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`; `vllm/model_executor/models/mimo_v2_omni.py` modified +4/-1 (5 lines); hunks: -52,6 +52,7; -1209,7 +1210,9 @@ def get_dummy_mm_data(; symbols: get_dummy_mm_data, MiMoV2OmniForCausalLM, touching `get_dummy_mm_data, MiMoV2OmniForCausalLM`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2.py` modified +8/-5 (13 lines); hunks: -27,6 +27,7; -156,14 +157,16 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +4/-1 (5 lines); hunks: -52,6 +52,7; -1209,7 +1210,9 @@ def get_dummy_mm_data(; symbols: get_dummy_mm_data, MiMoV2OmniForCausalLM
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2.py
@@ -27,6 +27,7 @@
+from vllm.model_executor.layers.fused_moe.router.gate_linear import GateLinear
@@ -156,14 +157,16 @@ def __init__(
-        self.gate = nn.Linear(
+        self.gate = GateLinear(
-            dtype=self.gate_dtype,
+            params_dtype=self.gate_dtype,
diff -- vllm/model_executor/models/mimo_v2_omni.py
@@ -52,6 +52,7 @@
+    SupportsEagle3,
@@ -1209,7 +1210,9 @@ def get_dummy_mm_data(
-class MiMoV2OmniForCausalLM(nn.Module, SupportsMultiModal, SupportsPP, SupportsQuant):
+class MiMoV2OmniForCausalLM(
+    nn.Module, SupportsMultiModal, SupportsPP, SupportsQuant, SupportsEagle3
+):
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +8/-5; `vllm/model_executor/models/mimo_v2_omni.py` modified +4/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/qwen3_dflash.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57508 - [Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too)

- Link: https://github.com/vllm-project/vllm/pull/57508
- Status/date: merged / 2026-09-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`; associated commits `211e252d0b4f`
- Diff scope read: GitHub Pull Request files API returned 3 files, +415/-63, 543 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too)"; model line: MiMo V2 Flash; category: bug fix; main diff: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`; technical summary: Covers "[Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too)"; the main implementation surface is `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_mimo_v2_qkv_shard.py` added +225/-0 (225 lines); hunks: -0,0 +1,225; symbols: _chunk_rows, _quantize_chunks, _owned_rows, _dequantize, touching `_chunk_rows, _quantize_chunks, _owned_rows`; `vllm/model_executor/models/mimo_v2.py` modified +141/-55 (196 lines); hunks: -50,6 +50,7; -460,6 +461,28 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _requantize_fp8, _shard_fp8_qkv_proj, MiMoV2Model, touching `is_compressed_softmax_layer, _requantize_fp8, _shard_fp8_qkv_proj`; `vllm/model_executor/models/mimo_v2_mtp.py` modified +49/-8 (57 lines); hunks: -45,7 +45,7; -266,6 +266,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `tests/models/quantization/test_mimo_v2_qkv_shard.py` added +225/-0 (225 lines); hunks: -0,0 +1,225; symbols: _chunk_rows, _quantize_chunks, _owned_rows, _dequantize
  - `vllm/model_executor/models/mimo_v2.py` modified +141/-55 (196 lines); hunks: -50,6 +50,7; -460,6 +461,28 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _requantize_fp8, _shard_fp8_qkv_proj, MiMoV2Model
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +49/-8 (57 lines); hunks: -45,7 +45,7; -266,6 +266,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_mimo_v2_qkv_shard.py
@@ -0,0 +1,225 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Unit test for MiMo-V2 fused fp8 ``qkv_proj`` sharding.
+The checkpoint stores the fused QKV pre-sharded at ``num_key_value_heads``
+chunks (``ckpt_tp``), each holding that slice's ``[Q_c | K_c | V_c]`` rows with
+its own block scale grid. ``ckpt_tp`` is not the layer's KV-head count: a
diff -- vllm/model_executor/models/mimo_v2.py
@@ -50,6 +50,7 @@
+from vllm.utils.math_utils import cdiv
@@ -460,6 +461,28 @@ def is_compressed_softmax_layer(self) -> bool:
+def _requantize_fp8(
+    grouped: torch.Tensor, rows_rank: int, block: int, dtype: torch.dtype
+) -> tuple[torch.Tensor, torch.Tensor]:
+    """Block-quantize a rank's ``[Q | K | V]`` rows back to fp8.
diff -- vllm/model_executor/models/mimo_v2_mtp.py
@@ -45,7 +45,7 @@
```

- Reviewed files:
  - tests: `tests/models/quantization/test_mimo_v2_qkv_shard.py` added +225/-0
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +141/-55; `vllm/model_executor/models/mimo_v2_mtp.py` modified +49/-8
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_mimo_v2_qkv_shard.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #49815 - [Bugfix][MiMo] Apply vision attention sinks in the window attention path

- Link: https://github.com/vllm-project/vllm/pull/49815
- Status/date: merged / 2026-08-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`; associated commits `c3cac8c63d91`
- Diff scope read: GitHub Pull Request files API returned 3 files, +132/-12, 200 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][MiMo] Apply vision attention sinks in the window attention path"; model line: MiMo V2 Flash; category: bug fix; main diff: `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`; technical summary: Covers "[Bugfix][MiMo] Apply vision attention sinks in the window attention path"; the main implementation surface is `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/test_mimo_v2_omni.py` added +91/-0 (91 lines); hunks: -0,0 +1,91; symbols: vision_attn_env, _reference, test_window_attention_applies_sinks, touching `vision_attn_env, _reference, test_window_attention_applies_sinks`; `vllm/model_executor/models/mimo_v2_omni.py` modified +27/-10 (37 lines); hunks: -193,7 +193,7 @@ def __init__(; -214,21 +214,38 @@ def _forward_window_attn(; symbols: __init__, _forward_window_attn, touching `__init__, _forward_window_attn`.
- Code diff details:
  - `tests/models/multimodal/test_mimo_v2_omni.py` added +91/-0 (91 lines); hunks: -0,0 +1,91; symbols: vision_attn_env, _reference, test_window_attention_applies_sinks
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +27/-10 (37 lines); hunks: -193,7 +193,7 @@ def __init__(; -214,21 +214,38 @@ def _forward_window_attn(; symbols: __init__, _forward_window_attn
- Key code excerpts:

```diff
diff -- tests/models/multimodal/test_mimo_v2_omni.py
@@ -0,0 +1,91 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MiMo-V2 vision window attention has to apply the per-head sink logits."""
+import pytest
+import torch
+from tests.utils import ensure_current_vllm_config
diff -- vllm/model_executor/models/mimo_v2_omni.py
@@ -193,7 +193,7 @@ def __init__(
-        # Sink attention weights (loaded but not used in vLLM flash_attn)
+        # Per-head sink logits, applied in the window attention path.
@@ -214,21 +214,38 @@ def _forward_window_attn(
-        """Window attention via flash_attn_varlen_func with window_size."""
-        from vllm.vllm_flash_attn import flash_attn_varlen_func
+        """Window attention with the per-head sink applied to key 0.
```

- Reviewed files:
  - tests: `tests/models/multimodal/test_mimo_v2_omni.py` added +91/-0
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` modified +27/-10
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/test_mimo_v2_omni.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #43117 - fix(processor): route MiMo-V2-Omni media fetch through MediaConnector

- Link: https://github.com/vllm-project/vllm/pull/43117
- Status/date: merged / 2026-07-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/processors/mimo_v2_omni.py`; associated commits `54503ecec0f3`
- Diff scope read: GitHub Pull Request files API returned 1 files, +22/-76, 190 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(processor): route MiMo-V2-Omni media fetch through MediaConnector"; model line: MiMo V2 Flash; category: bug fix; main diff: `vllm/transformers_utils/processors/mimo_v2_omni.py`; technical summary: Covers "fix(processor): route MiMo-V2-Omni media fetch through MediaConnector"; the main implementation surface is `vllm/transformers_utils/processors/mimo_v2_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/processors/mimo_v2_omni.py` modified +22/-76 (98 lines); hunks: -7,33 +7,21; -62,7 +50,7; symbols: ImageInput, VideoInput, AudioInput, _smart_resize, touching `ImageInput, VideoInput, AudioInput`.
- Code diff details:
  - `vllm/transformers_utils/processors/mimo_v2_omni.py` modified +22/-76 (98 lines); hunks: -7,33 +7,21; -62,7 +50,7; symbols: ImageInput, VideoInput, AudioInput, _smart_resize
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/processors/mimo_v2_omni.py
@@ -7,33 +7,21 @@
-import copy
-import io
-from io import BytesIO
-import requests
-try:
-    from torchcodec.decoders import AudioDecoder
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/processors/mimo_v2_omni.py` modified +22/-76
- Risk and verification: Runtime changes concentrate in `vllm/transformers_utils/processors/mimo_v2_omni.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #46104 - [Spec Decode] Support SWA + DFlash for MiMo

- Link: https://github.com/vllm-project/vllm/pull/46104
- Status/date: merged / 2026-07-01
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2.py`; associated commits `9969466a5978`
- Diff scope read: GitHub Pull Request files API returned 4 files, +243/-25, 500 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Spec Decode] Support SWA + DFlash for MiMo"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[Spec Decode] Support SWA + DFlash for MiMo"; the main implementation surface is `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2.py` modified +16/-3 (19 lines); hunks: -53,7 +53,12; -539,7 +544,7 @@ def _shard_fp8_qkv_proj(; symbols: _shard_fp8_qkv_proj, MiMoV2Model, __init__, forward, touching `_shard_fp8_qkv_proj, MiMoV2Model, __init__`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2.py` modified +16/-3 (19 lines); hunks: -53,7 +53,12; -539,7 +544,7 @@ def _shard_fp8_qkv_proj(; symbols: _shard_fp8_qkv_proj, MiMoV2Model, __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2.py
@@ -53,7 +53,12 @@
-from .interfaces import MixtureOfExperts, SupportsPP
+from .interfaces import (
+    EagleModelMixin,
+    MixtureOfExperts,
+    SupportsEagle3,
+    SupportsPP,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +16/-3
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45200 - [Models] Fix MiMo v2.x QKV TP sharding + FP4 support

- Link: https://github.com/vllm-project/vllm/pull/45200
- Status/date: merged / 2026-06-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2.py`; associated commits `b5adb027ad03`
- Diff scope read: GitHub Pull Request files API returned 2 files, +170/-5, 245 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Models] Fix MiMo v2.x QKV TP sharding + FP4 support"; model line: MiMo V2 Flash; category: bug fix; main diff: `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[Models] Fix MiMo v2.x QKV TP sharding + FP4 support"; the main implementation surface is `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2.py` modified +160/-5 (165 lines); hunks: -35,6 +35,10; -455,6 +459,85 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _shard_fp8_qkv_proj, MiMoV2Model, __init__, touching `is_compressed_softmax_layer, _shard_fp8_qkv_proj, MiMoV2Model`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2.py` modified +160/-5 (165 lines); hunks: -35,6 +35,10; -455,6 +459,85 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _shard_fp8_qkv_proj, MiMoV2Model, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2.py
@@ -35,6 +35,10 @@
+from vllm.model_executor.layers.quantization.utils.quant_utils import (
+    GroupShape,
+    scaled_quantize,
+)
@@ -455,6 +459,85 @@ def is_compressed_softmax_layer(self) -> bool:
+def _shard_fp8_qkv_proj(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +160/-5
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/models/mimo_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41797 - [Attention] add triton diff-kv backend for mimo

- Link: https://github.com/vllm-project/vllm/pull/41797
- Status/date: merged / 2026-06-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2.py`; associated commits `f81daf888063`
- Diff scope read: GitHub Pull Request files API returned 8 files, +1041/-9, 1103 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Attention] add triton diff-kv backend for mimo"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[Attention] add triton diff-kv backend for mimo"; the main implementation surface is `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2.py` modified +21/-7 (28 lines); hunks: -47,9 +47,7; -292,11 +290,27 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2.py` modified +21/-7 (28 lines); hunks: -47,9 +47,7; -292,11 +290,27 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2.py
@@ -47,9 +47,7 @@
-from vllm.v1.attention.backends.flash_attn_diffkv import (
-    FlashAttentionDiffKVBackend,
-)
+from vllm.v1.attention.backends.registry import AttentionBackendEnum
@@ -292,11 +290,27 @@ def __init__(
-        # Use DiffKV backend when V has a different head dim than K
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +21/-7
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_triton_unified_attention_diffkv.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41905 - [SpecDecoding] extend mtp support for mimo 2.5

- Link: https://github.com/vllm-project/vllm/pull/41905
- Status/date: merged / 2026-05-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2_mtp.py`; associated commits `2ee8c2a56e41`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-10, 57 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[SpecDecoding] extend mtp support for mimo 2.5"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `vllm/model_executor/models/mimo_v2_mtp.py`; technical summary: Covers "[SpecDecoding] extend mtp support for mimo 2.5"; the main implementation surface is `vllm/model_executor/models/mimo_v2_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2_mtp.py` modified +3/-10 (13 lines); hunks: -49,7 +49,7; -170,10 +170,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward, compute_logits, touching `__init__, forward, compute_logits`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +3/-10 (13 lines); hunks: -49,7 +49,7; -170,10 +170,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward, compute_logits
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2_mtp.py
@@ -49,7 +49,7 @@
-# only the first layer and only one speculative token.
+# only the first layer
@@ -170,10 +170,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
-        if spec_cfg.num_speculative_tokens != 1:
-            raise ValueError(
-                "MiMo-V2 MTP in vLLM only supports num_speculative_tokens=1."
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2_mtp.py` modified +3/-10
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mimo_v2_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41029 - [Model] update for mimo v25

- Link: https://github.com/vllm-project/vllm/pull/41029
- Status/date: merged / 2026-04-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_v2.py`; associated commits `7a1eb8ac2ec4`
- Diff scope read: GitHub Pull Request files API returned 6 files, +10/-8, 74 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] update for mimo v25"; model line: MiMo V2 Flash; category: model implementation change; main diff: `vllm/model_executor/models/mimo_v2.py`; technical summary: Covers "[Model] update for mimo v25"; the main implementation surface is `vllm/model_executor/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2.py` modified +1/-1 (2 lines); hunks: -733,7 +733,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, MiMoV2ProForCausalLM, MiMoV2ForCausalLM, touching `load_weights, MiMoV2ProForCausalLM, MiMoV2ForCausalLM`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2.py` modified +1/-1 (2 lines); hunks: -733,7 +733,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, MiMoV2ProForCausalLM, MiMoV2ForCausalLM
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2.py
@@ -733,7 +733,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-class MiMoV2ProForCausalLM(MiMoV2FlashForCausalLM):
+class MiMoV2ForCausalLM(MiMoV2FlashForCausalLM):
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #40967 - [Model] Add MiMo-V2.5 support

- Link: https://github.com/vllm-project/vllm/pull/40967
- Status/date: merged / 2026-04-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_audio.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/transformers_utils/configs/mimo_v2_omni.py` and 6 files; associated commits `c245d35ff467`
- Diff scope read: GitHub Pull Request files API returned 16 files, +4737/-5, 4920 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Add MiMo-V2.5 support"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/mimo_audio.py`, `vllm/transformers_utils/processors/mimo_v2_omni.py`; technical summary: Covers "[Model] Add MiMo-V2.5 support"; the main implementation surface is `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/mimo_audio.py`, `vllm/transformers_utils/processors/mimo_v2_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_v2_omni.py` added +1488/-0 (1488 lines); hunks: -0,0 +1,1488; symbols: MiMoVisionMLP, MiMoVisionPatchEmbed, MiMoVisionPatchMerger, __init__, touching `MiMoVisionMLP, MiMoVisionPatchEmbed, MiMoVisionPatchMerger`; `vllm/model_executor/models/mimo_audio.py` added +1389/-0 (1389 lines); hunks: -0,0 +1,1389; symbols: _vq_default, _ema_inplace, _laplace_smoothing, _uniform_init, touching `_vq_default, _ema_inplace, _laplace_smoothing`; `vllm/transformers_utils/processors/mimo_v2_omni.py` added +1285/-0 (1285 lines); hunks: -0,0 +1,1285; symbols: ImageInput, VideoInput, AudioInput, VideoAudioInput, touching `ImageInput, VideoInput, AudioInput`; `vllm/model_executor/models/mimo_v2_mtp.py` added +373/-0 (373 lines); hunks: -0,0 +1,373; symbols: MiMoV2MTPLayer, __init__, forward, _MiMoV2MTPLayers, touching `MiMoV2MTPLayer, __init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/mimo_v2_omni.py` added +1488/-0 (1488 lines); hunks: -0,0 +1,1488; symbols: MiMoVisionMLP, MiMoVisionPatchEmbed, MiMoVisionPatchMerger, __init__
  - `vllm/model_executor/models/mimo_audio.py` added +1389/-0 (1389 lines); hunks: -0,0 +1,1389; symbols: _vq_default, _ema_inplace, _laplace_smoothing, _uniform_init
  - `vllm/transformers_utils/processors/mimo_v2_omni.py` added +1285/-0 (1285 lines); hunks: -0,0 +1,1285; symbols: ImageInput, VideoInput, AudioInput, VideoAudioInput
  - `vllm/model_executor/models/mimo_v2_mtp.py` added +373/-0 (373 lines); hunks: -0,0 +1,373; symbols: MiMoV2MTPLayer, __init__, forward, _MiMoV2MTPLayers
  - `vllm/transformers_utils/configs/mimo_v2_omni.py` added +65/-0 (65 lines); hunks: -0,0 +1,65; symbols: Mimo_VLVisionConfig, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_v2_omni.py
@@ -0,0 +1,1488 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import math
+from collections.abc import Callable, Iterable, Mapping, Sequence
+from functools import partial
+from typing import Any
diff -- vllm/model_executor/models/mimo_audio.py
@@ -0,0 +1,1389 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""MiMo audio: tokenizer, encoding utilities, and audio encoder.
+Ported from SGLang's mimo_audio.py.
+Audio tokenizer adapted from https://github.com/XiaomiMiMo/MiMo-Audio-Tokenizer.git
+"""
diff -- vllm/transformers_utils/processors/mimo_v2_omni.py
@@ -0,0 +1,1285 @@
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` added +1488/-0; `vllm/model_executor/models/mimo_audio.py` added +1389/-0; `vllm/transformers_utils/processors/mimo_v2_omni.py` added +1285/-0; `vllm/model_executor/models/mimo_v2_mtp.py` added +373/-0; `vllm/transformers_utils/configs/mimo_v2_omni.py` added +65/-0; `vllm/model_executor/models/mimo_v2.py` renamed +22/-2
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #25136 - [spec decode] Fix MTP inference path for MiMo-7B model

- Link: https://github.com/vllm-project/vllm/pull/25136
- Status/date: merged / 2025-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo_mtp.py`; associated commits `c4cb0af98a8e`
- Diff scope read: GitHub Pull Request files API returned 3 files, +20/-6, 61 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[spec decode] Fix MTP inference path for MiMo-7B model"; model line: MiMo V2 Flash; category: bug fix; main diff: `vllm/model_executor/models/mimo_mtp.py`; technical summary: Covers "[spec decode] Fix MTP inference path for MiMo-7B model"; the main implementation surface is `vllm/model_executor/models/mimo_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_mtp.py` modified +14/-4 (18 lines); hunks: -241,17 +241,27 @@ def load_weights(self, weights: Iterable[tuple[str,; symbols: load_weights, map_model_name_to_mtp_param_name, _rewrite_spec_layer_name, touching `load_weights, map_model_name_to_mtp_param_name, _rewrite_spec_layer_name`.
- Code diff details:
  - `vllm/model_executor/models/mimo_mtp.py` modified +14/-4 (18 lines); hunks: -241,17 +241,27 @@ def load_weights(self, weights: Iterable[tuple[str,; symbols: load_weights, map_model_name_to_mtp_param_name, _rewrite_spec_layer_name
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_mtp.py
@@ -241,17 +241,27 @@ def load_weights(self, weights: Iterable[tuple[str,
+        # append mtp_start_layer_idx
+        pattern = r"(model\.mtp_layers\.)(\d+)(\.)"
+        match = re.match(pattern, name)
+        if match:
+            original_num = int(match.group(2))
+            new_num = original_num + self.config.num_hidden_layers
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_mtp.py` modified +14/-4
- Risk and verification: Runtime changes concentrate in `vllm/config/speculative.py`, `vllm/model_executor/models/mimo_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17433 - [Model] Support MiMo-7B inference with MTP

- Link: https://github.com/vllm-project/vllm/pull/17433
- Status/date: merged / 2025-05-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mimo.py`, `vllm/model_executor/models/mimo_mtp.py`; associated commits `acee8f48aa9c`
- Diff scope read: GitHub Pull Request files API returned 7 files, +507/-4, 576 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Support MiMo-7B inference with MTP"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `vllm/model_executor/models/mimo_mtp.py`, `vllm/model_executor/models/mimo.py`; technical summary: Covers "[Model] Support MiMo-7B inference with MTP"; the main implementation surface is `vllm/model_executor/models/mimo_mtp.py`, `vllm/model_executor/models/mimo.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mimo_mtp.py` added +283/-0 (283 lines); hunks: -0,0 +1,283; symbols: MiMoMultiTokenPredictorLayer, __init__, forward, MiMoMultiTokenPredictor, touching `MiMoMultiTokenPredictorLayer, __init__, forward`; `vllm/model_executor/models/mimo.py` added +190/-0 (190 lines); hunks: -0,0 +1,190; symbols: MiMoModel, forward, load_weights, MiMoForCausalLM, touching `MiMoModel, forward, load_weights`.
- Code diff details:
  - `vllm/model_executor/models/mimo_mtp.py` added +283/-0 (283 lines); hunks: -0,0 +1,283; symbols: MiMoMultiTokenPredictorLayer, __init__, forward, MiMoMultiTokenPredictor
  - `vllm/model_executor/models/mimo.py` added +190/-0 (190 lines); hunks: -0,0 +1,190; symbols: MiMoModel, forward, load_weights, MiMoForCausalLM
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mimo_mtp.py
@@ -0,0 +1,283 @@
+# SPDX-License-Identifier: Apache-2.0
+# Adapted from
+# https://github.com/vllm-project/vllm/blob/v0.7.3/vllm/model_executor/models/deepseek_mtp.py
+# Copyright 2025 Xiaomi Corporation.
+# Copyright 2023 The vLLM team.
+# Copyright 2024 DeepSeek-AI team.
diff -- vllm/model_executor/models/mimo.py
@@ -0,0 +1,190 @@
+# SPDX-License-Identifier: Apache-2.0
+# Adapted from
+# https://github.com/huggingface/transformers/blob/v4.28.0/src/transformers/models/qwen2/modeling_qwen2.py
+# Copyright 2025 Xiaomi Corporation.
+# Copyright 2024 The Qwen team.
+# Copyright 2023 The vLLM team.
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mimo_mtp.py` added +283/-0; `vllm/model_executor/models/mimo.py` added +190/-0
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
