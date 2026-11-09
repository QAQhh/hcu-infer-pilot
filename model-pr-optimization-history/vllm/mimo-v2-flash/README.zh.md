# vllm MiMo V2 Flash 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/models/multimodal/test_mimo_v2_omni.py` | [#49815](https://github.com/vllm-project/vllm/pull/49815), [#58900](https://github.com/vllm-project/vllm/pull/58900), [#64179](https://github.com/vllm-project/vllm/pull/64179) |
| `tests/models/quantization/test_mimo_v2_qkv_shard.py` | [#57508](https://github.com/vllm-project/vllm/pull/57508), [#58184](https://github.com/vllm-project/vllm/pull/58184), [#59053](https://github.com/vllm-project/vllm/pull/59053) |
| `tests/models/quantization/test_mimo_v2_w4a16_routing.py` | [#58262](https://github.com/vllm-project/vllm/pull/58262) |
| `tests/models/test_mimo_v2_attention_backend.py` | [#64064](https://github.com/vllm-project/vllm/pull/64064) |
| `tests/v1/e2e/spec_decode/mtp/mimo/__init__.py` | 无直接 PR 号提交 |
| `tests/v1/e2e/spec_decode/mtp/mimo/test_mtp.py` | 无直接 PR 号提交 |
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

## PR 覆盖总览

- git 追溯 PR 数: 22
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 22

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #64179 - [Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6

- 链接: https://github.com/vllm-project/vllm/pull/64179
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`；关联提交 `0e5b2ba118cf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+111/-2，可读 patch 145 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6」；模型线: MiMo V2 Flash；类别: 文档/测试/CI；主要 diff: `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`；技术摘要: 覆盖「[Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6」；主要实现面是 `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/test_mimo_v2_omni.py` modified +101/-0 (101 lines); hunks: -5,6 +5,11; -73,3 +78,99 @@ def test_window_attention_applies_sinks(vision_attn_env, num_...; symbols: test_window_attention_applies_sinks, _build_attention, _stub_encoder_parallelism, _attention_inputs，涉及 `test_window_attention_applies_sinks, _build_attention, _stub_encoder_parallelism`；`vllm/model_executor/models/mimo_v2_omni.py` modified +8/-1 (9 lines); hunks: -162,7 +162,12 @@ def __init__(; -1229,6 +1234,8 @@ def get_dummy_mm_data(; symbols: __init__, get_dummy_mm_data, MiMoV2OmniForCausalLM，涉及 `__init__, get_dummy_mm_data, MiMoV2OmniForCausalLM`。
- 代码 diff 细节:
  - `tests/models/multimodal/test_mimo_v2_omni.py` modified +101/-0 (101 lines); hunks: -5,6 +5,11; -73,3 +78,99 @@ def test_window_attention_applies_sinks(vision_attn_env, num_...; symbols: test_window_attention_applies_sinks, _build_attention, _stub_encoder_parallelism, _attention_inputs
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +8/-1 (9 lines); hunks: -162,7 +162,12 @@ def __init__(; -1229,6 +1234,8 @@ def get_dummy_mm_data(; symbols: __init__, get_dummy_mm_data, MiMoV2OmniForCausalLM
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/test_mimo_v2_omni.py` modified +101/-0
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` modified +8/-1
- 验证与风险: diff 自带测试面 `tests/models/multimodal/test_mimo_v2_omni.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64064 - [ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6

- 链接: https://github.com/vllm-project/vllm/pull/64064
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/test_mimo_v2_attention_backend.py`, `vllm/model_executor/models/mimo_v2.py`；关联提交 `a6c3635e3660`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+637/-31，可读 patch 826 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6」；模型线: MiMo V2 Flash；类别: 性能/后端优化；主要 diff: `tests/models/test_mimo_v2_attention_backend.py`, `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6」；主要实现面是 `tests/models/test_mimo_v2_attention_backend.py`, `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/test_mimo_v2_attention_backend.py` added +205/-0 (205 lines); hunks: -0,0 +1,205; symbols: bf16_default_dtype, restore_diffkv_head_size_v, state, _build_attention，涉及 `bf16_default_dtype, restore_diffkv_head_size_v, state`；`vllm/model_executor/models/mimo_v2.py` modified +19/-7 (26 lines); hunks: -317,15 +317,24 @@ def __init__(; -337,8 +346,11 @@ def __init__(; symbols: __init__, attribute，涉及 `__init__, attribute`。
- 代码 diff 细节:
  - `tests/models/test_mimo_v2_attention_backend.py` added +205/-0 (205 lines); hunks: -0,0 +1,205; symbols: bf16_default_dtype, restore_diffkv_head_size_v, state, _build_attention
  - `vllm/model_executor/models/mimo_v2.py` modified +19/-7 (26 lines); hunks: -317,15 +317,24 @@ def __init__(; -337,8 +346,11 @@ def __init__(; symbols: __init__, attribute
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/test_mimo_v2_attention_backend.py` added +205/-0
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +19/-7
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_cache.py`, `tests/models/test_mimo_v2_attention_backend.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58184 - [Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have

- 链接: https://github.com/vllm-project/vllm/pull/58184
- 状态/时间: merged / 2026-10-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`；关联提交 `79218659a6d7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+65/-0，可读 patch 83 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have」；主要实现面是 `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +62/-0 (62 lines); hunks: -14,6 +14,8; -405,3 +407,63 @@ def test_wrong_chunk_count_is_detected():; symbols: test_wrong_chunk_count_is_detected, test_load_weights_pairs_split_fp8_qkv_proj_and_skips_absent_layers，涉及 `test_wrong_chunk_count_is_detected, test_load_weights_pairs_split_fp8_qkv_proj_and_skips_absent_layers`；`vllm/model_executor/models/mimo_v2.py` modified +3/-0 (3 lines); hunks: -1020,6 +1020,9 @@ def _try_load_fp8_qkv_proj(; symbols: _try_load_fp8_qkv_proj，涉及 `_try_load_fp8_qkv_proj`。
- 代码 diff 细节:
  - `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +62/-0 (62 lines); hunks: -14,6 +14,8; -405,3 +407,63 @@ def test_wrong_chunk_count_is_detected():; symbols: test_wrong_chunk_count_is_detected, test_load_weights_pairs_split_fp8_qkv_proj_and_skips_absent_layers
  - `vllm/model_executor/models/mimo_v2.py` modified +3/-0 (3 lines); hunks: -1020,6 +1020,9 @@ def _try_load_fp8_qkv_proj(; symbols: _try_load_fp8_qkv_proj
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +62/-0
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_mimo_v2_qkv_shard.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59053 - [Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default

- 链接: https://github.com/vllm-project/vllm/pull/59053
- 状态/时间: merged / 2026-10-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`；关联提交 `3b518982806c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+327/-18，可读 patch 452 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default」；模型线: MiMo V2 Flash；类别: 性能/后端优化；主要 diff: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default」；主要实现面是 `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +179/-5 (184 lines); hunks: -17,7 +17,11; -76,10 +80,10 @@ def _quantize_chunks(truth, num_heads, num_kv_heads, head_di...; symbols: _quantize_chunks, _owned_rows, _owned_index，涉及 `_quantize_chunks, _owned_rows, _owned_index`；`vllm/model_executor/models/mimo_v2.py` modified +148/-13 (161 lines); hunks: -234,6 +234,7 @@ def __init__(; -260,16 +261,36 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +179/-5 (184 lines); hunks: -17,7 +17,11; -76,10 +80,10 @@ def _quantize_chunks(truth, num_heads, num_kv_heads, head_di...; symbols: _quantize_chunks, _owned_rows, _owned_index
  - `vllm/model_executor/models/mimo_v2.py` modified +148/-13 (161 lines); hunks: -234,6 +234,7 @@ def __init__(; -260,16 +261,36 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/quantization/test_mimo_v2_qkv_shard.py` modified +179/-5
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +148/-13
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_mimo_v2_qkv_shard.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58128 - [Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash

- 链接: https://github.com/vllm-project/vllm/pull/58128
- 状态/时间: merged / 2026-10-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`；关联提交 `21d93d0d8c0e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+111/-15，可读 patch 321 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash」；模型线: MiMo V2 Flash；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash」；主要实现面是 `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -24,7 +24,7; -64,6 +64,7 @@ def __init__(; symbols: __init__，涉及 `__init__`；`vllm/model_executor/models/mimo_v2.py` modified +6/-0 (6 lines); hunks: -372,6 +372,10 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = "...; -389,6 +393,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -24,7 +24,7; -64,6 +64,7 @@ def __init__(; symbols: __init__
  - `vllm/model_executor/models/mimo_v2.py` modified +6/-0 (6 lines); hunks: -372,6 +372,10 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = "...; -389,6 +393,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""...; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1; `vllm/model_executor/models/mimo_v2.py` modified +6/-0
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_triton_unified_attention_diffkv.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58262 - [ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942

- 链接: https://github.com/vllm-project/vllm/pull/58262
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_mimo_v2_w4a16_routing.py`；关联提交 `16d4ac4ba3a0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+192/-5，可读 patch 219 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942」；模型线: MiMo V2 Flash；类别: 性能/后端优化；主要 diff: `tests/models/quantization/test_mimo_v2_w4a16_routing.py`；技术摘要: 覆盖「[ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942」；主要实现面是 `tests/models/quantization/test_mimo_v2_w4a16_routing.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_mimo_v2_w4a16_routing.py` added +176/-0 (176 lines); hunks: -0,0 +1,176; symbols: mimo_routing_method, mimo_moe_config, test_ungrouped_sigmoid_router_is_deepseekv3, test_aiter_w4a16_supports_mimo_routing，涉及 `mimo_routing_method, mimo_moe_config, test_ungrouped_sigmoid_router_is_deepseekv3`。
- 代码 diff 细节:
  - `tests/models/quantization/test_mimo_v2_w4a16_routing.py` added +176/-0 (176 lines); hunks: -0,0 +1,176; symbols: mimo_routing_method, mimo_moe_config, test_ungrouped_sigmoid_router_is_deepseekv3, test_aiter_w4a16_supports_mimo_routing
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/quantization/test_mimo_v2_w4a16_routing.py` added +176/-0
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_mimo_v2_w4a16_routing.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58938 - [Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images

- 链接: https://github.com/vllm-project/vllm/pull/58938
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2_omni.py`；关联提交 `8aaeef343a10`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+20/-4，可读 patch 45 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/mimo_v2_omni.py`；技术摘要: 覆盖「[Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images」；主要实现面是 `vllm/model_executor/models/mimo_v2_omni.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2_omni.py` modified +20/-4 (24 lines); hunks: -69,7 +69,10; -670,6 +673,14 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, MiMoV2OmniMultiModalDataParser, MiMoV2OmniProcessingInfo, get_supported_mm_limits，涉及 `load_weights, MiMoV2OmniMultiModalDataParser, MiMoV2OmniProcessingInfo`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +20/-4 (24 lines); hunks: -69,7 +69,10; -670,6 +673,14 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, MiMoV2OmniMultiModalDataParser, MiMoV2OmniProcessingInfo, get_supported_mm_limits
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` modified +20/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/mimo_v2_omni.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #58019 - [Frontend] Support strict MiMo-V2.6 tool calling

- 链接: https://github.com/vllm-project/vllm/pull/58019
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/parser/mimo.py`, `vllm/reasoning/mimo_engine_reasoning_parser.py`, `vllm/tool_parsers/mimo_tool_parser.py`；关联提交 `dfc8e0f3e2ad`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 17 个文件，+243/-15，可读 patch 437 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Frontend] Support strict MiMo-V2.6 tool calling」；模型线: MiMo V2 Flash；类别: 模型支持/运行时入口；主要 diff: `vllm/tool_parsers/mimo_tool_parser.py`, `vllm/reasoning/mimo_engine_reasoning_parser.py`, `vllm/parser/mimo.py`；技术摘要: 覆盖「[Frontend] Support strict MiMo-V2.6 tool calling」；主要实现面是 `vllm/tool_parsers/mimo_tool_parser.py`, `vllm/reasoning/mimo_engine_reasoning_parser.py`, `vllm/parser/mimo.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/tool_parsers/mimo_tool_parser.py` added +25/-0 (25 lines); hunks: -0,0 +1,25; symbols: MiMoToolParser, get_structural_tag，涉及 `MiMoToolParser, get_structural_tag`；`vllm/reasoning/mimo_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6；`vllm/parser/mimo.py` added +42/-0 (42 lines); hunks: -0,0 +1,42; symbols: _mimo_arg_converter, MiMoParser, __init__，涉及 `_mimo_arg_converter, MiMoParser, __init__`。
- 代码 diff 细节:
  - `vllm/tool_parsers/mimo_tool_parser.py` added +25/-0 (25 lines); hunks: -0,0 +1,25; symbols: MiMoToolParser, get_structural_tag
  - `vllm/reasoning/mimo_engine_reasoning_parser.py` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `vllm/parser/mimo.py` added +42/-0 (42 lines); hunks: -0,0 +1,42; symbols: _mimo_arg_converter, MiMoParser, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/tool_parsers/mimo_tool_parser.py` added +25/-0; `vllm/reasoning/mimo_engine_reasoning_parser.py` added +6/-0; `vllm/parser/mimo.py` added +42/-0
- 验证与风险: diff 自带测试面 `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt`, `requirements/test/xpu.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58142 - [Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls

- 链接: https://github.com/vllm-project/vllm/pull/58142
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`；关联提交 `77e52645e9ba`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+12/-3，可读 patch 29 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`；技术摘要: 覆盖「[Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls」；主要实现面是 `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2.py` modified +6/-2 (8 lines); hunks: -742,8 +742,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`；`vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -266,7 +266,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2.py` modified +6/-2 (8 lines); hunks: -742,8 +742,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1 (7 lines); hunks: -266,7 +266,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +6/-2; `vllm/model_executor/models/mimo_v2_mtp.py` modified +6/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #58900 - [Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture)

- 链接: https://github.com/vllm-project/vllm/pull/58900
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/test_mimo_v2_omni.py`；关联提交 `0da126676e38`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+15/-27，可读 patch 66 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture)」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `tests/models/multimodal/test_mimo_v2_omni.py`；技术摘要: 覆盖「[Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture)」；主要实现面是 `tests/models/multimodal/test_mimo_v2_omni.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/test_mimo_v2_omni.py` modified +3/-18 (21 lines); hunks: -5,13 +5,7; -21,20 +15,11; symbols: vision_attn_env，涉及 `vision_attn_env`。
- 代码 diff 细节:
  - `tests/models/multimodal/test_mimo_v2_omni.py` modified +3/-18 (21 lines); hunks: -5,13 +5,7; -21,20 +15,11; symbols: vision_attn_env
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/test_mimo_v2_omni.py` modified +3/-18
- 验证与风险: diff 自带测试面 `tests/models/multimodal/test_mimo_v2_omni.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #57784 - [Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2

- 链接: https://github.com/vllm-project/vllm/pull/57784
- 状态/时间: merged / 2026-09-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`；关联提交 `9b2f34cad446`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+21/-6，可读 patch 109 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2」；模型线: MiMo V2 Flash；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`；技术摘要: 覆盖「[Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2」；主要实现面是 `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2.py` modified +8/-5 (13 lines); hunks: -27,6 +27,7; -156,14 +157,16 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/model_executor/models/mimo_v2_omni.py` modified +4/-1 (5 lines); hunks: -52,6 +52,7; -1209,7 +1210,9 @@ def get_dummy_mm_data(; symbols: get_dummy_mm_data, MiMoV2OmniForCausalLM，涉及 `get_dummy_mm_data, MiMoV2OmniForCausalLM`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2.py` modified +8/-5 (13 lines); hunks: -27,6 +27,7; -156,14 +157,16 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +4/-1 (5 lines); hunks: -52,6 +52,7; -1209,7 +1210,9 @@ def get_dummy_mm_data(; symbols: get_dummy_mm_data, MiMoV2OmniForCausalLM
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +8/-5; `vllm/model_executor/models/mimo_v2_omni.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/qwen3_dflash.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #57508 - [Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too)

- 链接: https://github.com/vllm-project/vllm/pull/57508
- 状态/时间: merged / 2026-09-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`；关联提交 `211e252d0b4f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+415/-63，可读 patch 543 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too)」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`；技术摘要: 覆盖「[Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too)」；主要实现面是 `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_mimo_v2_qkv_shard.py` added +225/-0 (225 lines); hunks: -0,0 +1,225; symbols: _chunk_rows, _quantize_chunks, _owned_rows, _dequantize，涉及 `_chunk_rows, _quantize_chunks, _owned_rows`；`vllm/model_executor/models/mimo_v2.py` modified +141/-55 (196 lines); hunks: -50,6 +50,7; -460,6 +461,28 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _requantize_fp8, _shard_fp8_qkv_proj, MiMoV2Model，涉及 `is_compressed_softmax_layer, _requantize_fp8, _shard_fp8_qkv_proj`；`vllm/model_executor/models/mimo_v2_mtp.py` modified +49/-8 (57 lines); hunks: -45,7 +45,7; -266,6 +266,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `tests/models/quantization/test_mimo_v2_qkv_shard.py` added +225/-0 (225 lines); hunks: -0,0 +1,225; symbols: _chunk_rows, _quantize_chunks, _owned_rows, _dequantize
  - `vllm/model_executor/models/mimo_v2.py` modified +141/-55 (196 lines); hunks: -50,6 +50,7; -460,6 +461,28 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _requantize_fp8, _shard_fp8_qkv_proj, MiMoV2Model
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +49/-8 (57 lines); hunks: -45,7 +45,7; -266,6 +266,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/quantization/test_mimo_v2_qkv_shard.py` added +225/-0
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +141/-55; `vllm/model_executor/models/mimo_v2_mtp.py` modified +49/-8
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_mimo_v2_qkv_shard.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #49815 - [Bugfix][MiMo] Apply vision attention sinks in the window attention path

- 链接: https://github.com/vllm-project/vllm/pull/49815
- 状态/时间: merged / 2026-08-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`；关联提交 `c3cac8c63d91`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+132/-12，可读 patch 200 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][MiMo] Apply vision attention sinks in the window attention path」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`；技术摘要: 覆盖「[Bugfix][MiMo] Apply vision attention sinks in the window attention path」；主要实现面是 `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/test_mimo_v2_omni.py` added +91/-0 (91 lines); hunks: -0,0 +1,91; symbols: vision_attn_env, _reference, test_window_attention_applies_sinks，涉及 `vision_attn_env, _reference, test_window_attention_applies_sinks`；`vllm/model_executor/models/mimo_v2_omni.py` modified +27/-10 (37 lines); hunks: -193,7 +193,7 @@ def __init__(; -214,21 +214,38 @@ def _forward_window_attn(; symbols: __init__, _forward_window_attn，涉及 `__init__, _forward_window_attn`。
- 代码 diff 细节:
  - `tests/models/multimodal/test_mimo_v2_omni.py` added +91/-0 (91 lines); hunks: -0,0 +1,91; symbols: vision_attn_env, _reference, test_window_attention_applies_sinks
  - `vllm/model_executor/models/mimo_v2_omni.py` modified +27/-10 (37 lines); hunks: -193,7 +193,7 @@ def __init__(; -214,21 +214,38 @@ def _forward_window_attn(; symbols: __init__, _forward_window_attn
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/multimodal/test_mimo_v2_omni.py` added +91/-0
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` modified +27/-10
- 验证与风险: diff 自带测试面 `tests/models/multimodal/test_mimo_v2_omni.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43117 - fix(processor): route MiMo-V2-Omni media fetch through MediaConnector

- 链接: https://github.com/vllm-project/vllm/pull/43117
- 状态/时间: merged / 2026-07-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/transformers_utils/processors/mimo_v2_omni.py`；关联提交 `54503ecec0f3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+22/-76，可读 patch 190 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(processor): route MiMo-V2-Omni media fetch through MediaConnector」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `vllm/transformers_utils/processors/mimo_v2_omni.py`；技术摘要: 覆盖「fix(processor): route MiMo-V2-Omni media fetch through MediaConnector」；主要实现面是 `vllm/transformers_utils/processors/mimo_v2_omni.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/transformers_utils/processors/mimo_v2_omni.py` modified +22/-76 (98 lines); hunks: -7,33 +7,21; -62,7 +50,7; symbols: ImageInput, VideoInput, AudioInput, _smart_resize，涉及 `ImageInput, VideoInput, AudioInput`。
- 代码 diff 细节:
  - `vllm/transformers_utils/processors/mimo_v2_omni.py` modified +22/-76 (98 lines); hunks: -7,33 +7,21; -62,7 +50,7; symbols: ImageInput, VideoInput, AudioInput, _smart_resize
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/transformers_utils/processors/mimo_v2_omni.py` modified +22/-76
- 验证与风险: runtime 路径改动集中在 `vllm/transformers_utils/processors/mimo_v2_omni.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46104 - [Spec Decode] Support SWA + DFlash for MiMo

- 链接: https://github.com/vllm-project/vllm/pull/46104
- 状态/时间: merged / 2026-07-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2.py`；关联提交 `9969466a5978`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+243/-25，可读 patch 500 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec Decode] Support SWA + DFlash for MiMo」；模型线: MiMo V2 Flash；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[Spec Decode] Support SWA + DFlash for MiMo」；主要实现面是 `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2.py` modified +16/-3 (19 lines); hunks: -53,7 +53,12; -539,7 +544,7 @@ def _shard_fp8_qkv_proj(; symbols: _shard_fp8_qkv_proj, MiMoV2Model, __init__, forward，涉及 `_shard_fp8_qkv_proj, MiMoV2Model, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2.py` modified +16/-3 (19 lines); hunks: -53,7 +53,12; -539,7 +544,7 @@ def _shard_fp8_qkv_proj(; symbols: _shard_fp8_qkv_proj, MiMoV2Model, __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +16/-3
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45200 - [Models] Fix MiMo v2.x QKV TP sharding + FP4 support

- 链接: https://github.com/vllm-project/vllm/pull/45200
- 状态/时间: merged / 2026-06-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2.py`；关联提交 `b5adb027ad03`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+170/-5，可读 patch 245 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Models] Fix MiMo v2.x QKV TP sharding + FP4 support」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[Models] Fix MiMo v2.x QKV TP sharding + FP4 support」；主要实现面是 `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2.py` modified +160/-5 (165 lines); hunks: -35,6 +35,10; -455,6 +459,85 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _shard_fp8_qkv_proj, MiMoV2Model, __init__，涉及 `is_compressed_softmax_layer, _shard_fp8_qkv_proj, MiMoV2Model`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2.py` modified +160/-5 (165 lines); hunks: -35,6 +35,10; -455,6 +459,85 @@ def is_compressed_softmax_layer(self) -> bool:; symbols: is_compressed_softmax_layer, _shard_fp8_qkv_proj, MiMoV2Model, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +160/-5
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/models/mimo_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41797 - [Attention] add triton diff-kv backend for mimo

- 链接: https://github.com/vllm-project/vllm/pull/41797
- 状态/时间: merged / 2026-06-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2.py`；关联提交 `f81daf888063`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+1041/-9，可读 patch 1103 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention] add triton diff-kv backend for mimo」；模型线: MiMo V2 Flash；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[Attention] add triton diff-kv backend for mimo」；主要实现面是 `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2.py` modified +21/-7 (28 lines); hunks: -47,9 +47,7; -292,11 +290,27 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2.py` modified +21/-7 (28 lines); hunks: -47,9 +47,7; -292,11 +290,27 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +21/-7
- 验证与风险: diff 自带测试面 `tests/kernels/attention/test_triton_unified_attention_diffkv.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41905 - [SpecDecoding] extend mtp support for mimo 2.5

- 链接: https://github.com/vllm-project/vllm/pull/41905
- 状态/时间: merged / 2026-05-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2_mtp.py`；关联提交 `2ee8c2a56e41`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-10，可读 patch 57 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[SpecDecoding] extend mtp support for mimo 2.5」；模型线: MiMo V2 Flash；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/mimo_v2_mtp.py`；技术摘要: 覆盖「[SpecDecoding] extend mtp support for mimo 2.5」；主要实现面是 `vllm/model_executor/models/mimo_v2_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2_mtp.py` modified +3/-10 (13 lines); hunks: -49,7 +49,7; -170,10 +170,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward, compute_logits，涉及 `__init__, forward, compute_logits`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2_mtp.py` modified +3/-10 (13 lines); hunks: -49,7 +49,7; -170,10 +170,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward, compute_logits
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2_mtp.py` modified +3/-10
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/mimo_v2_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41029 - [Model] update for mimo v25

- 链接: https://github.com/vllm-project/vllm/pull/41029
- 状态/时间: merged / 2026-04-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_v2.py`；关联提交 `7a1eb8ac2ec4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+10/-8，可读 patch 74 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] update for mimo v25」；模型线: MiMo V2 Flash；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/mimo_v2.py`；技术摘要: 覆盖「[Model] update for mimo v25」；主要实现面是 `vllm/model_executor/models/mimo_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2.py` modified +1/-1 (2 lines); hunks: -733,7 +733,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, MiMoV2ProForCausalLM, MiMoV2ForCausalLM，涉及 `load_weights, MiMoV2ProForCausalLM, MiMoV2ForCausalLM`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2.py` modified +1/-1 (2 lines); hunks: -733,7 +733,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, MiMoV2ProForCausalLM, MiMoV2ForCausalLM
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/mimo_v2.py
@@ -733,7 +733,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-class MiMoV2ProForCausalLM(MiMoV2FlashForCausalLM):
+class MiMoV2ForCausalLM(MiMoV2FlashForCausalLM):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40967 - [Model] Add MiMo-V2.5 support

- 链接: https://github.com/vllm-project/vllm/pull/40967
- 状态/时间: merged / 2026-04-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_audio.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/transformers_utils/configs/mimo_v2_omni.py` 等 6 个文件；关联提交 `c245d35ff467`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 16 个文件，+4737/-5，可读 patch 4920 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add MiMo-V2.5 support」；模型线: MiMo V2 Flash；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/mimo_audio.py`, `vllm/transformers_utils/processors/mimo_v2_omni.py`；技术摘要: 覆盖「[Model] Add MiMo-V2.5 support」；主要实现面是 `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/mimo_audio.py`, `vllm/transformers_utils/processors/mimo_v2_omni.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_v2_omni.py` added +1488/-0 (1488 lines); hunks: -0,0 +1,1488; symbols: MiMoVisionMLP, MiMoVisionPatchEmbed, MiMoVisionPatchMerger, __init__，涉及 `MiMoVisionMLP, MiMoVisionPatchEmbed, MiMoVisionPatchMerger`；`vllm/model_executor/models/mimo_audio.py` added +1389/-0 (1389 lines); hunks: -0,0 +1,1389; symbols: _vq_default, _ema_inplace, _laplace_smoothing, _uniform_init，涉及 `_vq_default, _ema_inplace, _laplace_smoothing`；`vllm/transformers_utils/processors/mimo_v2_omni.py` added +1285/-0 (1285 lines); hunks: -0,0 +1,1285; symbols: ImageInput, VideoInput, AudioInput, VideoAudioInput，涉及 `ImageInput, VideoInput, AudioInput`；`vllm/model_executor/models/mimo_v2_mtp.py` added +373/-0 (373 lines); hunks: -0,0 +1,373; symbols: MiMoV2MTPLayer, __init__, forward, _MiMoV2MTPLayers，涉及 `MiMoV2MTPLayer, __init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_v2_omni.py` added +1488/-0 (1488 lines); hunks: -0,0 +1,1488; symbols: MiMoVisionMLP, MiMoVisionPatchEmbed, MiMoVisionPatchMerger, __init__
  - `vllm/model_executor/models/mimo_audio.py` added +1389/-0 (1389 lines); hunks: -0,0 +1,1389; symbols: _vq_default, _ema_inplace, _laplace_smoothing, _uniform_init
  - `vllm/transformers_utils/processors/mimo_v2_omni.py` added +1285/-0 (1285 lines); hunks: -0,0 +1,1285; symbols: ImageInput, VideoInput, AudioInput, VideoAudioInput
  - `vllm/model_executor/models/mimo_v2_mtp.py` added +373/-0 (373 lines); hunks: -0,0 +1,373; symbols: MiMoV2MTPLayer, __init__, forward, _MiMoV2MTPLayers
  - `vllm/transformers_utils/configs/mimo_v2_omni.py` added +65/-0 (65 lines); hunks: -0,0 +1,65; symbols: Mimo_VLVisionConfig, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_v2_omni.py` added +1488/-0; `vllm/model_executor/models/mimo_audio.py` added +1389/-0; `vllm/transformers_utils/processors/mimo_v2_omni.py` added +1285/-0; `vllm/model_executor/models/mimo_v2_mtp.py` added +373/-0; `vllm/transformers_utils/configs/mimo_v2_omni.py` added +65/-0; `vllm/model_executor/models/mimo_v2.py` renamed +22/-2
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25136 - [spec decode] Fix MTP inference path for MiMo-7B model

- 链接: https://github.com/vllm-project/vllm/pull/25136
- 状态/时间: merged / 2025-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo_mtp.py`；关联提交 `c4cb0af98a8e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-6，可读 patch 61 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[spec decode] Fix MTP inference path for MiMo-7B model」；模型线: MiMo V2 Flash；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/mimo_mtp.py`；技术摘要: 覆盖「[spec decode] Fix MTP inference path for MiMo-7B model」；主要实现面是 `vllm/model_executor/models/mimo_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_mtp.py` modified +14/-4 (18 lines); hunks: -241,17 +241,27 @@ def load_weights(self, weights: Iterable[tuple[str,; symbols: load_weights, map_model_name_to_mtp_param_name, _rewrite_spec_layer_name，涉及 `load_weights, map_model_name_to_mtp_param_name, _rewrite_spec_layer_name`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_mtp.py` modified +14/-4 (18 lines); hunks: -241,17 +241,27 @@ def load_weights(self, weights: Iterable[tuple[str,; symbols: load_weights, map_model_name_to_mtp_param_name, _rewrite_spec_layer_name
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_mtp.py` modified +14/-4
- 验证与风险: runtime 路径改动集中在 `vllm/config/speculative.py`, `vllm/model_executor/models/mimo_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17433 - [Model] Support MiMo-7B inference with MTP

- 链接: https://github.com/vllm-project/vllm/pull/17433
- 状态/时间: merged / 2025-05-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/mimo.py`, `vllm/model_executor/models/mimo_mtp.py`；关联提交 `acee8f48aa9c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+507/-4，可读 patch 576 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Support MiMo-7B inference with MTP」；模型线: MiMo V2 Flash；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/mimo_mtp.py`, `vllm/model_executor/models/mimo.py`；技术摘要: 覆盖「[Model] Support MiMo-7B inference with MTP」；主要实现面是 `vllm/model_executor/models/mimo_mtp.py`, `vllm/model_executor/models/mimo.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/mimo_mtp.py` added +283/-0 (283 lines); hunks: -0,0 +1,283; symbols: MiMoMultiTokenPredictorLayer, __init__, forward, MiMoMultiTokenPredictor，涉及 `MiMoMultiTokenPredictorLayer, __init__, forward`；`vllm/model_executor/models/mimo.py` added +190/-0 (190 lines); hunks: -0,0 +1,190; symbols: MiMoModel, forward, load_weights, MiMoForCausalLM，涉及 `MiMoModel, forward, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/mimo_mtp.py` added +283/-0 (283 lines); hunks: -0,0 +1,283; symbols: MiMoMultiTokenPredictorLayer, __init__, forward, MiMoMultiTokenPredictor
  - `vllm/model_executor/models/mimo.py` added +190/-0 (190 lines); hunks: -0,0 +1,190; symbols: MiMoModel, forward, load_weights, MiMoForCausalLM
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/mimo_mtp.py` added +283/-0; `vllm/model_executor/models/mimo.py` added +190/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
