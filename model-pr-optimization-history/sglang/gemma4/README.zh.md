# sglang Gemma 4 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/Google/Gemma4.mdx` | [#46816](https://github.com/sgl-project/sglang/pull/46816) |
| `docs/src/snippets/autoregressive/gemma4-deployment.jsx` | 无直接 PR 号提交 |
| `python/sglang/kernels/ops/layernorm/gemma4_fused_ops.py` | 无直接 PR 号提交 |
| `python/sglang/kernels/ops/moe/gemma4_routing.py` | 无直接 PR 号提交 |
| `python/sglang/srt/arg_groups/model_overrides/gemma4.py` | 无直接 PR 号提交 |
| `python/sglang/srt/dllm/algorithm/gemma4_renoise.py` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/gemma4_detector.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952) |
| `python/sglang/srt/models/gemma4_audio.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952) |
| `python/sglang/srt/models/gemma4_causal.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#22498](https://github.com/sgl-project/sglang/pull/22498), [#23280](https://github.com/sgl-project/sglang/pull/23280), [#24048](https://github.com/sgl-project/sglang/pull/24048), [#24436](https://github.com/sgl-project/sglang/pull/24436), [#24696](https://github.com/sgl-project/sglang/pull/24696), [#25054](https://github.com/sgl-project/sglang/pull/25054), [#25284](https://github.com/sgl-project/sglang/pull/25284), [#26026](https://github.com/sgl-project/sglang/pull/26026), [#26147](https://github.com/sgl-project/sglang/pull/26147), [#26502](https://github.com/sgl-project/sglang/pull/26502), [#27471](https://github.com/sgl-project/sglang/pull/27471), ... (13 total) |
| `python/sglang/srt/models/gemma4_mm.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#22498](https://github.com/sgl-project/sglang/pull/22498), [#24048](https://github.com/sgl-project/sglang/pull/24048), [#24436](https://github.com/sgl-project/sglang/pull/24436), [#24696](https://github.com/sgl-project/sglang/pull/24696), [#25054](https://github.com/sgl-project/sglang/pull/25054), [#25284](https://github.com/sgl-project/sglang/pull/25284), [#26147](https://github.com/sgl-project/sglang/pull/26147), [#27471](https://github.com/sgl-project/sglang/pull/27471), [#31672](https://github.com/sgl-project/sglang/pull/31672), [#42019](https://github.com/sgl-project/sglang/pull/42019), [#46816](https://github.com/sgl-project/sglang/pull/46816) |
| `python/sglang/srt/models/gemma4_mtp.py` | [#24436](https://github.com/sgl-project/sglang/pull/24436), [#26026](https://github.com/sgl-project/sglang/pull/26026), [#32440](https://github.com/sgl-project/sglang/pull/32440) |
| `python/sglang/srt/models/gemma4_unified.py` | [#35809](https://github.com/sgl-project/sglang/pull/35809) |
| `python/sglang/srt/models/gemma4_vision.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#22498](https://github.com/sgl-project/sglang/pull/22498) |
| `python/sglang/srt/multimodal/processors/gemma4.py` | [#21952](https://github.com/sgl-project/sglang/pull/21952), [#26320](https://github.com/sgl-project/sglang/pull/26320) |
| `python/sglang/srt/multimodal/processors/gemma4_unified.py` | 无直接 PR 号提交 |
| `test/registered/attention/test_gemma4_swa_triton_oob_regression.py` | 无直接 PR 号提交 |
| `test/registered/attention/test_gemma4_unified_swa_virtual_ids.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_gemma4_fp8_per_expert_loading.py` | 无直接 PR 号提交 |
| `test/registered/kernels/ops/layernorm/test_gemma4_qkv_norm.py` | 无直接 PR 号提交 |
| `test/registered/kernels/ops/moe/test_gemma4_expert_activation.py` | 无直接 PR 号提交 |
| `test/registered/kernels/ops/moe/test_gemma4_fused_routing.py` | 无直接 PR 号提交 |
| `test/registered/pp/test_pp_gemma4.py` | 无直接 PR 号提交 |
| `test/registered/spec/test_gemma4_dflash_31b_extra.py` | [#27471](https://github.com/sgl-project/sglang/pull/27471) |
| `test/registered/spec/test_gemma4_mtp_31b_extra.py` | [#24552](https://github.com/sgl-project/sglang/pull/24552), [#27101](https://github.com/sgl-project/sglang/pull/27101) |
| `test/registered/unit/dllm/algorithm/test_gemma4_sampling_cuda.py` | 无直接 PR 号提交 |
| `test/registered/unit/dllm/test_gemma4_cuda_graph.py` | 无直接 PR 号提交 |
| `test/registered/unit/dllm/test_gemma4_renoise.py` | 无直接 PR 号提交 |
| `test/registered/unit/dllm/test_gemma4_uniform_lifecycle.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 21
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 21
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #21952 - [New Model] Gemma 4

- 链接: https://github.com/sgl-project/sglang/pull/21952
- 状态/时间: merged / 2026-04-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/gemma4_detector.py`, `python/sglang/srt/models/gemma4_audio.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_vision.py` 等 6 个文件；关联提交 `2813cb6d9a5b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 35 个文件，+6007/-70，可读 patch 6694 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[New Model] Gemma 4」；模型线: Gemma 4；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_audio.py`；技术摘要: 覆盖「[New Model] Gemma 4」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_audio.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` added +1009/-0 (1009 lines); hunks: -0,0 +1,1009; symbols: get_attention_sliding_window_size, Gemma4Router, __init__, fuse_scale，涉及 `get_attention_sliding_window_size, Gemma4Router, __init__`；`python/sglang/srt/models/gemma4_mm.py` added +878/-0 (878 lines); hunks: -0,0 +1,878; symbols: Gemma4ImagePixelInputs, Gemma4AudioInputs, Gemma4MultimodalEmbedder, __init__，涉及 `Gemma4ImagePixelInputs, Gemma4AudioInputs, Gemma4MultimodalEmbedder`；`python/sglang/srt/models/gemma4_audio.py` added +873/-0 (873 lines); hunks: -0,0 +1,873; symbols: Gemma4AudioRelativePositionEmbedding, __init__, _get_timing_signal_1d_pos, _relative_shift，涉及 `Gemma4AudioRelativePositionEmbedding, __init__, _get_timing_signal_1d_pos`；`python/sglang/srt/models/gemma4_vision.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: _rotate_half, _apply_rotary, Gemma4VisionRotaryEmbedding, __init__，涉及 `_rotate_half, _apply_rotary, Gemma4VisionRotaryEmbedding`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` added +1009/-0 (1009 lines); hunks: -0,0 +1,1009; symbols: get_attention_sliding_window_size, Gemma4Router, __init__, fuse_scale
  - `python/sglang/srt/models/gemma4_mm.py` added +878/-0 (878 lines); hunks: -0,0 +1,878; symbols: Gemma4ImagePixelInputs, Gemma4AudioInputs, Gemma4MultimodalEmbedder, __init__
  - `python/sglang/srt/models/gemma4_audio.py` added +873/-0 (873 lines); hunks: -0,0 +1,873; symbols: Gemma4AudioRelativePositionEmbedding, __init__, _get_timing_signal_1d_pos, _relative_shift
  - `python/sglang/srt/models/gemma4_vision.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: _rotate_half, _apply_rotary, Gemma4VisionRotaryEmbedding, __init__
  - `python/sglang/srt/function_call/gemma4_detector.py` added +445/-0 (445 lines); hunks: -0,0 +1,445; symbols: _parse_gemma4_value, _parse_gemma4_array, _parse_gemma4_args, _find_matching_brace
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` added +1009/-0; `python/sglang/srt/models/gemma4_mm.py` added +878/-0; `python/sglang/srt/models/gemma4_audio.py` added +873/-0; `python/sglang/srt/models/gemma4_vision.py` added +599/-0; `python/sglang/srt/function_call/gemma4_detector.py` added +445/-0; `python/sglang/srt/multimodal/processors/gemma4.py` added +145/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/function_call/test_function_call_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #24048 - [VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar

- 链接: https://github.com/sgl-project/sglang/pull/24048
- 状态/时间: merged / 2026-05-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；关联提交 `e5c58eb9d627`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+158/-6，可读 patch 223 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar」；模型线: Gemma 4；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；技术摘要: 覆盖「[VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +29/-2 (31 lines); hunks: -27,7 +27,10; -545,12 +548,36 @@ def forward(; symbols: forward，涉及 `forward`；`python/sglang/srt/models/gemma4_mm.py` modified +20/-0 (20 lines); hunks: -224,6 +224,26 @@ def __init__(; symbols: __init__, model, satisfies, __setattr__，涉及 `__init__, model, satisfies`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +29/-2 (31 lines); hunks: -27,7 +27,10; -545,12 +548,36 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/gemma4_mm.py` modified +20/-0 (20 lines); hunks: -224,6 +224,26 @@ def __init__(; symbols: __init__, model, satisfies, __setattr__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +29/-2; `python/sglang/srt/models/gemma4_mm.py` modified +20/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/gemma4_fused_ops.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24436 - [Gemma 4] Adding MTP support

- 链接: https://github.com/sgl-project/sglang/pull/24436
- 状态/时间: merged / 2026-05-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_mtp.py`；关联提交 `d2c1034163cd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+1949/-7，可读 patch 2060 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Gemma 4] Adding MTP support」；模型线: Gemma 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`；技术摘要: 覆盖「[Gemma 4] Adding MTP support」；主要实现面是 `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mtp.py` added +398/-0 (398 lines); hunks: -0,0 +1,398; symbols: _get_text_config, _resolve_target_text_model, Gemma4AssistantForCausalLM, __init__，涉及 `_get_text_config, _resolve_target_text_model, Gemma4AssistantForCausalLM`；`python/sglang/srt/models/gemma4_mm.py` modified +5/-0 (5 lines); hunks: -256,6 +256,11 @@ def pad_input_ids(; symbols: pad_input_ids, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size，涉及 `pad_input_ids, get_input_embeddings, get_embed_and_head`；`python/sglang/srt/models/gemma4_causal.py` modified +3/-0 (3 lines); hunks: -878,6 +878,9 @@ def __init__(; symbols: __init__, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size，涉及 `__init__, get_input_embeddings, get_embed_and_head`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mtp.py` added +398/-0 (398 lines); hunks: -0,0 +1,398; symbols: _get_text_config, _resolve_target_text_model, Gemma4AssistantForCausalLM, __init__
  - `python/sglang/srt/models/gemma4_mm.py` modified +5/-0 (5 lines); hunks: -256,6 +256,11 @@ def pad_input_ids(; symbols: pad_input_ids, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size
  - `python/sglang/srt/models/gemma4_causal.py` modified +3/-0 (3 lines); hunks: -878,6 +878,9 @@ def __init__(; symbols: __init__, get_input_embeddings, get_embed_and_head, get_attention_sliding_window_size
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mtp.py` added +398/-0; `python/sglang/srt/models/gemma4_mm.py` modified +5/-0; `python/sglang/srt/models/gemma4_causal.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24696 - [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader

- 链接: https://github.com/sgl-project/sglang/pull/24696
- 状态/时间: merged / 2026-05-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；关联提交 `d3fd91ed9726`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+317/-15，可读 patch 369 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader」；模型线: Gemma 4；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；技术摘要: 覆盖「[Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +58/-15 (73 lines); hunks: -29,6 +29,7; -339,22 +340,64 @@ def forward(; symbols: forward，涉及 `forward`；`python/sglang/srt/models/gemma4_mm.py` modified +35/-0 (35 lines); hunks: -787,6 +787,41 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +58/-15 (73 lines); hunks: -29,6 +29,7; -339,22 +340,64 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/gemma4_mm.py` modified +35/-0 (35 lines); hunks: -787,6 +787,41 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +58/-15; `python/sglang/srt/models/gemma4_mm.py` modified +35/-0
- 验证与风险: diff 自带测试面 `test/registered/models/test_gemma4_fp8_per_expert_loading.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25284 - Support Gemma4 Pipeline Parallelism

- 链接: https://github.com/sgl-project/sglang/pull/25284
- 状态/时间: merged / 2026-05-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；关联提交 `4c0ce0345d0d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+487/-68，可读 patch 867 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support Gemma4 Pipeline Parallelism」；模型线: Gemma 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；技术摘要: 覆盖「Support Gemma4 Pipeline Parallelism」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +212/-34 (246 lines); hunks: -14,7 +14,7; -25,6 +25,7; symbols: get_attention_sliding_window_size, pp_filter_load_weight, Gemma4Router, __init__，涉及 `get_attention_sliding_window_size, pp_filter_load_weight, Gemma4Router`；`python/sglang/srt/models/gemma4_mm.py` modified +133/-33 (166 lines); hunks: -28,11 +28,14; -43,13 +46,17; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +212/-34 (246 lines); hunks: -14,7 +14,7; -25,6 +25,7; symbols: get_attention_sliding_window_size, pp_filter_load_weight, Gemma4Router, __init__
  - `python/sglang/srt/models/gemma4_mm.py` modified +133/-33 (166 lines); hunks: -28,11 +28,14; -43,13 +46,17; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +212/-34; `python/sglang/srt/models/gemma4_mm.py` modified +133/-33
- 验证与风险: diff 自带测试面 `python/sglang/test/test_utils.py`, `test/registered/distributed/test_pp_single_node.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25054 - Support Gemma4 MoE NVFP4

- 链接: https://github.com/sgl-project/sglang/pull/25054
- 状态/时间: merged / 2026-05-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；关联提交 `847cbada9c42`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+271/-118，可读 patch 605 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support Gemma4 MoE NVFP4」；模型线: Gemma 4；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`；技术摘要: 覆盖「Support Gemma4 MoE NVFP4」；主要实现面是 `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mm.py` modified +88/-61 (149 lines); hunks: -33,6 +33,7; -817,6 +818,27 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`；`python/sglang/srt/models/gemma4_causal.py` modified +81/-27 (108 lines); hunks: -42,6 +42,7; -1140,14 +1141,31 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mm.py` modified +88/-61 (149 lines); hunks: -33,6 +33,7; -817,6 +818,27 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
  - `python/sglang/srt/models/gemma4_causal.py` modified +81/-27 (108 lines); hunks: -42,6 +42,7; -1140,14 +1141,31 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +88/-61; `python/sglang/srt/models/gemma4_causal.py` modified +81/-27
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/cutlass_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26026 - [bug fix] Fix 3 issues when using Gemma4 MTP

- 链接: https://github.com/sgl-project/sglang/pull/26026
- 状态/时间: merged / 2026-05-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`；关联提交 `89ff2bc1115c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-11，可读 patch 66 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[bug fix] Fix 3 issues when using Gemma4 MTP」；模型线: Gemma 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`；技术摘要: 覆盖「[bug fix] Fix 3 issues when using Gemma4 MTP」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +11/-6 (17 lines); hunks: -1147,7 +1147,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -1159,11 +1160,15 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights，涉及 `load_weights`；`python/sglang/srt/models/gemma4_mtp.py` modified +2/-0 (2 lines); hunks: -21,6 +21,7; -72,6 +73,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +11/-6 (17 lines); hunks: -1147,7 +1147,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -1159,11 +1160,15 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights
  - `python/sglang/srt/models/gemma4_mtp.py` modified +2/-0 (2 lines); hunks: -21,6 +21,7; -72,6 +73,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +11/-6; `python/sglang/srt/models/gemma4_mtp.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/server_args.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24552 - [Gemma4] Add test for MTP models

- 链接: https://github.com/sgl-project/sglang/pull/24552
- 状态/时间: merged / 2026-05-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/spec/test_gemma4_mtp_31b_extra.py`；关联提交 `9040feebd854`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+535/-0，可读 patch 538 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Gemma4] Add test for MTP models」；模型线: Gemma 4；类别: 文档/测试/CI；主要 diff: `test/registered/spec/test_gemma4_mtp_31b_extra.py`；技术摘要: 覆盖「[Gemma4] Add test for MTP models」；主要实现面是 `test/registered/spec/test_gemma4_mtp_31b_extra.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/spec/test_gemma4_mtp_31b_extra.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4MTP31B, _server_env，涉及 `get_server_info, get_avg_spec_accept_length, TestGemma4MTP31B`。
- 代码 diff 细节:
  - `test/registered/spec/test_gemma4_mtp_31b_extra.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4MTP31B, _server_env
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/spec/test_gemma4_mtp_31b_extra.py` added +185/-0
- 验证与风险: diff 自带测试面 `test/registered/spec/test_frozen_kv_mtp.py`, `test/registered/spec/test_gemma4_mtp_26b_a4b_extra.py`, `test/registered/spec/test_gemma4_mtp_31b_extra.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26502 - perf(gemma4): single-launch fused router (topk + softmax + scale)

- 链接: https://github.com/sgl-project/sglang/pull/26502
- 状态/时间: merged / 2026-06-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`；关联提交 `5ae8d286d2b8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+229/-0，可读 patch 248 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「perf(gemma4): single-launch fused router (topk + softmax + scale)」；模型线: Gemma 4；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gemma4_causal.py`；技术摘要: 覆盖「perf(gemma4): single-launch fused router (topk + softmax + scale)」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +9/-0 (9 lines); hunks: -30,6 +30,7; -220,6 +221,14 @@ def routing_function(; symbols: routing_function，涉及 `routing_function`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +9/-0 (9 lines); hunks: -30,6 +30,7; -220,6 +221,14 @@ def routing_function(; symbols: routing_function
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +9/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/test_gemma4_fused_routing.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27101 - [Gemma4] Use hard GSM8K accuracy floor for 31B MTP test

- 链接: https://github.com/sgl-project/sglang/pull/27101
- 状态/时间: merged / 2026-06-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/spec/test_gemma4_mtp_31b_extra.py`；关联提交 `6d5361569988`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-6，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Gemma4] Use hard GSM8K accuracy floor for 31B MTP test」；模型线: Gemma 4；类别: 文档/测试/CI；主要 diff: `test/registered/spec/test_gemma4_mtp_31b_extra.py`；技术摘要: 覆盖「[Gemma4] Use hard GSM8K accuracy floor for 31B MTP test」；主要实现面是 `test/registered/spec/test_gemma4_mtp_31b_extra.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/spec/test_gemma4_mtp_31b_extra.py` modified +2/-6 (8 lines); hunks: -28,14 +28,10。
- 代码 diff 细节:
  - `test/registered/spec/test_gemma4_mtp_31b_extra.py` modified +2/-6 (8 lines); hunks: -28,14 +28,10
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/spec/test_gemma4_mtp_31b_extra.py` modified +2/-6
- 验证与风险: diff 自带测试面 `test/registered/spec/test_gemma4_mtp_31b_extra.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23280 - [XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU

- 链接: https://github.com/sgl-project/sglang/pull/23280
- 状态/时间: merged / 2026-06-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`；关联提交 `2c8357f79471`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+348/-34，可读 patch 641 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU」；模型线: Gemma 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gemma4_causal.py`；技术摘要: 覆盖「[XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +44/-17 (61 lines); hunks: -34,6 +34,7; -56,6 +57,9; symbols: __init__, fuse_scale, forward, routing_function，涉及 `__init__, fuse_scale, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +44/-17 (61 lines); hunks: -34,6 +34,7; -56,6 +57,9; symbols: __init__, fuse_scale, forward, routing_function
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +44/-17
- 验证与风险: diff 自带测试面 `test/registered/xpu/test_gemma_4_e2b.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26320 - fix(gemma4): register image/video/audio token_regex for HF-expanded prompts

- 链接: https://github.com/sgl-project/sglang/pull/26320
- 状态/时间: merged / 2026-06-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/multimodal/processors/gemma4.py`；关联提交 `98fe7e326ed4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+13/-0，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(gemma4): register image/video/audio token_regex for HF-expanded prompts」；模型线: Gemma 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/multimodal/processors/gemma4.py`；技术摘要: 覆盖「fix(gemma4): register image/video/audio token_regex for HF-expanded prompts」；主要实现面是 `python/sglang/srt/multimodal/processors/gemma4.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/multimodal/processors/gemma4.py` modified +13/-0 (13 lines); hunks: -12,6 +12,7; -41,9 +42,21 @@ def __init__(self, hf_config, server_args, _processor, *args,...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/multimodal/processors/gemma4.py` modified +13/-0 (13 lines); hunks: -12,6 +12,7; -41,9 +42,21 @@ def __init__(self, hf_config, server_args, _processor, *args,...; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/multimodal/processors/gemma4.py` modified +13/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/multimodal/processors/gemma4.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26147 - [NPU] Add Gemma4 Sliding Window Attention support on Ascend backend

- 链接: https://github.com/sgl-project/sglang/pull/26147
- 状态/时间: merged / 2026-06-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`；关联提交 `3a3a75946404`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+563/-132，可读 patch 979 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Add Gemma4 Sliding Window Attention support on Ascend backend」；模型线: Gemma 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`；技术摘要: 覆盖「[NPU] Add Gemma4 Sliding Window Attention support on Ascend backend」；主要实现面是 `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mm.py` modified +10/-3 (13 lines); hunks: -608,9 +608,16 @@ def forward(; symbols: forward，涉及 `forward`；`python/sglang/srt/models/gemma4_causal.py` modified +3/-1 (4 lines); hunks: -295,7 +295,9 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mm.py` modified +10/-3 (13 lines); hunks: -608,9 +608,16 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/gemma4_causal.py` modified +3/-1 (4 lines); hunks: -295,7 +295,9 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +10/-3; `python/sglang/srt/models/gemma4_causal.py` modified +3/-1
- 验证与风险: diff 自带测试面 `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_gemma_4_26b_a4b_it_llm.py`, `test/manual/ascend/llm_models/test_npu_gemma_4_31b_llm.py`, `test/manual/ascend/llm_models/test_npu_gemma_4_e2b_llm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27471 - add dflash gemma4 support

- 链接: https://github.com/sgl-project/sglang/pull/27471
- 状态/时间: merged / 2026-06-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py`；关联提交 `5ea0d1d09381`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+211/-16，可读 patch 259 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「add dflash gemma4 support」；模型线: Gemma 4；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py`；技术摘要: 覆盖「add dflash gemma4 support」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +8/-0 (8 lines); hunks: -1127,6 +1127,14 @@ def get_attention_sliding_window_size(self):; symbols: get_attention_sliding_window_size, dtype, set_dflash_layers_to_capture, forward，涉及 `get_attention_sliding_window_size, dtype, set_dflash_layers_to_capture`；`python/sglang/srt/models/gemma4_mm.py` modified +8/-0 (8 lines); hunks: -301,6 +301,14 @@ def get_embed_and_head(self) -> Tuple[torch.Tensor, torch.T...; symbols: get_embed_and_head, get_attention_sliding_window_size, set_dflash_layers_to_capture, prepare_attn_masks，涉及 `get_embed_and_head, get_attention_sliding_window_size, set_dflash_layers_to_capture`；`test/registered/spec/test_gemma4_dflash_31b_extra.py` added +177/-0 (177 lines); hunks: -0,0 +1,177; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4DFlash31B, _common_server_args，涉及 `get_server_info, get_avg_spec_accept_length, TestGemma4DFlash31B`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +8/-0 (8 lines); hunks: -1127,6 +1127,14 @@ def get_attention_sliding_window_size(self):; symbols: get_attention_sliding_window_size, dtype, set_dflash_layers_to_capture, forward
  - `python/sglang/srt/models/gemma4_mm.py` modified +8/-0 (8 lines); hunks: -301,6 +301,14 @@ def get_embed_and_head(self) -> Tuple[torch.Tensor, torch.T...; symbols: get_embed_and_head, get_attention_sliding_window_size, set_dflash_layers_to_capture, prepare_attn_masks
  - `test/registered/spec/test_gemma4_dflash_31b_extra.py` added +177/-0 (177 lines); hunks: -0,0 +1,177; symbols: get_server_info, get_avg_spec_accept_length, TestGemma4DFlash31B, _common_server_args
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +8/-0; `python/sglang/srt/models/gemma4_mm.py` modified +8/-0
  - tests: `test/registered/spec/test_gemma4_dflash_31b_extra.py` added +177/-0
- 验证与风险: diff 自带测试面 `test/registered/spec/test_gemma4_dflash_31b_extra.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31672 - fix(gemma4): prevent attention mask offset overflow

- 链接: https://github.com/sgl-project/sglang/pull/31672
- 状态/时间: merged / 2026-07-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_mm.py`；关联提交 `609fe1c0d1a6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(gemma4): prevent attention mask offset overflow」；模型线: Gemma 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gemma4_mm.py`；技术摘要: 覆盖「fix(gemma4): prevent attention mask offset overflow」；主要实现面是 `python/sglang/srt/models/gemma4_mm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mm.py` modified +1/-1 (2 lines); hunks: -335,7 +335,7 @@ def prepare_attn_masks(; symbols: prepare_attn_masks，涉及 `prepare_attn_masks`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mm.py` modified +1/-1 (2 lines); hunks: -335,7 +335,7 @@ def prepare_attn_masks(; symbols: prepare_attn_masks
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gemma4_mm.py
@@ -335,7 +335,7 @@ def prepare_attn_masks(
-            forward_batch.batch_size + 1, dtype=torch.int32, device=input_ids.device
+            forward_batch.batch_size + 1, dtype=torch.int64, device=input_ids.device
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gemma4_mm.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22498 - [CPU] Add support for Gemma4 on Xeon

- 链接: https://github.com/sgl-project/sglang/pull/22498
- 状态/时间: merged / 2026-08-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_vision.py`；关联提交 `b6d7602914d1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 27 个文件，+514/-106，可读 patch 1253 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CPU] Add support for Gemma4 on Xeon」；模型线: Gemma 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_vision.py`；技术摘要: 覆盖「[CPU] Add support for Gemma4 on Xeon」；主要实现面是 `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_vision.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mm.py` modified +29/-11 (40 lines); hunks: -59,13 +59,20; -241,9 +248,15 @@ def __init__(; symbols: __init__, forward, load_weights, get_embed_and_head，涉及 `__init__, forward, load_weights`；`python/sglang/srt/models/gemma4_causal.py` modified +27/-9 (36 lines); hunks: -74,6 +74,21 @@ def get_attention_sliding_window_size(config):; -109,11 +124,12 @@ def pp_filter_load_weight(; symbols: get_attention_sliding_window_size, load_tied_lm_head, pp_filter_load_weight, __init__，涉及 `get_attention_sliding_window_size, load_tied_lm_head, pp_filter_load_weight`；`python/sglang/srt/models/gemma4_vision.py` modified +25/-6 (31 lines); hunks: -30,7 +30,17; -173,7 +183,9 @@ def __init__(; symbols: __init__, _select_backend, forward，涉及 `__init__, _select_backend, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mm.py` modified +29/-11 (40 lines); hunks: -59,13 +59,20; -241,9 +248,15 @@ def __init__(; symbols: __init__, forward, load_weights, get_embed_and_head
  - `python/sglang/srt/models/gemma4_causal.py` modified +27/-9 (36 lines); hunks: -74,6 +74,21 @@ def get_attention_sliding_window_size(config):; -109,11 +124,12 @@ def pp_filter_load_weight(; symbols: get_attention_sliding_window_size, load_tied_lm_head, pp_filter_load_weight, __init__
  - `python/sglang/srt/models/gemma4_vision.py` modified +25/-6 (31 lines); hunks: -30,7 +30,17; -173,7 +183,9 @@ def __init__(; symbols: __init__, _select_backend, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +29/-11; `python/sglang/srt/models/gemma4_causal.py` modified +27/-9; `python/sglang/srt/models/gemma4_vision.py` modified +25/-6
- 验证与风险: diff 自带测试面 `python/sglang/test/cpu_test_utils.py`, `test/registered/cpu/test_extend.py`, `test/registered/cpu/test_moe.py`, `test/registered/cpu/test_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #32440 - fix(gemma4): quantize MTP bridge projections

- 链接: https://github.com/sgl-project/sglang/pull/32440
- 状态/时间: merged / 2026-08-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_mtp.py`；关联提交 `b1707996e8c5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(gemma4): quantize MTP bridge projections」；模型线: Gemma 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gemma4_mtp.py`；技术摘要: 覆盖「fix(gemma4): quantize MTP bridge projections」；主要实现面是 `python/sglang/srt/models/gemma4_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mtp.py` modified +2/-2 (4 lines); hunks: -91,7 +91,7 @@ def __init__(; -103,7 +103,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mtp.py` modified +2/-2 (4 lines); hunks: -91,7 +91,7 @@ def __init__(; -103,7 +103,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gemma4_mtp.py
@@ -91,7 +91,7 @@ def __init__(
-            quant_config=None,
+            quant_config=quant_config,
@@ -103,7 +103,7 @@ def __init__(
-            quant_config=None,
+            quant_config=quant_config,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mtp.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gemma4_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35809 - fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration

- 链接: https://github.com/sgl-project/sglang/pull/35809
- 状态/时间: merged / 2026-09-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_unified.py`；关联提交 `08b192240540`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration」；模型线: Gemma 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gemma4_unified.py`；技术摘要: 覆盖「fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration」；主要实现面是 `python/sglang/srt/models/gemma4_unified.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_unified.py` modified +2/-1 (3 lines); hunks: -190,7 +190,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_unified.py` modified +2/-1 (3 lines); hunks: -190,7 +190,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gemma4_unified.py
@@ -190,7 +190,8 @@ def __init__(
-        if self.pp_group.world_size == 1 and text_tie:
+        self.lm_head_is_tied = self.pp_group.world_size == 1 and text_tie
+        if self.lm_head_is_tied:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_unified.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gemma4_unified.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42311 - [Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries

- 链接: https://github.com/sgl-project/sglang/pull/42311
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_causal.py`；关联提交 `71b04e02cfd8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+433/-174，可读 patch 1082 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries」；模型线: Gemma 4；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/gemma4_causal.py`；技术摘要: 覆盖「[Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries」；主要实现面是 `python/sglang/srt/models/gemma4_causal.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_causal.py` modified +96/-46 (142 lines); hunks: -33,6 +33,16; -219,6 +229,7 @@ def __init__(; symbols: __init__, routing_function, forward，涉及 `__init__, routing_function, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_causal.py` modified +96/-46 (142 lines); hunks: -33,6 +33,16; -219,6 +229,7 @@ def __init__(; symbols: __init__, routing_function, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_causal.py` modified +96/-46
- 验证与风险: diff 自带测试面 `test/registered/unit/layer_boundary/test_boundary_output_contracts.py`, `test/registered/unit/models/test_zaya_mod_tp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #42019 - [Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support

- 链接: https://github.com/sgl-project/sglang/pull/42019
- 状态/时间: merged / 2026-10-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gemma4_mm.py`；关联提交 `37678784c637`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+485/-25，可读 patch 824 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support」；模型线: Gemma 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gemma4_mm.py`；技术摘要: 覆盖「[Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support」；主要实现面是 `python/sglang/srt/models/gemma4_mm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mm.py` modified +44/-4 (48 lines); hunks: -335,11 +335,51 @@ def prepare_attn_masks(; -413,10 +453,10 @@ def prepare_attn_masks(; symbols: prepare_attn_masks, get_image_feature，涉及 `prepare_attn_masks, get_image_feature`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mm.py` modified +44/-4 (48 lines); hunks: -335,11 +335,51 @@ def prepare_attn_masks(; -413,10 +453,10 @@ def prepare_attn_masks(; symbols: prepare_attn_masks, get_image_feature
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +44/-4
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_flash_attention_4.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #46816 - [Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend

- 链接: https://github.com/sgl-project/sglang/pull/46816
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Google/Gemma4.mdx`, `python/sglang/srt/models/gemma4_mm.py`；关联提交 `cc69762cb73c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+139/-9，可读 patch 259 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend」；模型线: Gemma 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gemma4_mm.py`, `docs/cookbook/autoregressive/Google/Gemma4.mdx`；技术摘要: 覆盖「[Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend」；主要实现面是 `python/sglang/srt/models/gemma4_mm.py`, `docs/cookbook/autoregressive/Google/Gemma4.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gemma4_mm.py` modified +30/-2 (32 lines); hunks: -66,7 +66,7; -327,17 +327,29 @@ def prepare_attn_masks(; symbols: prepare_attn_masks，涉及 `prepare_attn_masks`；`docs/cookbook/autoregressive/Google/Gemma4.mdx` modified +1/-0 (1 lines); hunks: -107,6 +107,7 @@ The Gemma 4 series offers models in various sizes and archit...。
- 代码 diff 细节:
  - `python/sglang/srt/models/gemma4_mm.py` modified +30/-2 (32 lines); hunks: -66,7 +66,7; -327,17 +327,29 @@ def prepare_attn_masks(; symbols: prepare_attn_masks
  - `docs/cookbook/autoregressive/Google/Gemma4.mdx` modified +1/-0 (1 lines); hunks: -107,6 +107,7 @@ The Gemma 4 series offers models in various sizes and archit...
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gemma4_mm.py` modified +30/-2
  - docs: `docs/cookbook/autoregressive/Google/Gemma4.mdx` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/dllm/test_gemma4_diffusion.py`, `test/registered/xpu/test_xpu_gemma_bidirectional_attn.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
