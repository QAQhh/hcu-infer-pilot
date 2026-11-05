# sglang MiMo V2 Flash Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/Xiaomi/MiMo-V2-Flash.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx` | [#40622](https://github.com/sgl-project/sglang/pull/40622) |
| `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` | [#40622](https://github.com/sgl-project/sglang/pull/40622), [#40969](https://github.com/sgl-project/sglang/pull/40969) |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx` | [#40577](https://github.com/sgl-project/sglang/pull/40577) |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_flash.mdx` | no direct PR-number commit |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/mimo_v2_flash.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/mimo-v2-flash-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/mimo-v25-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx` | [#40622](https://github.com/sgl-project/sglang/pull/40622), [#40969](https://github.com/sgl-project/sglang/pull/40969) |
| `python/sglang/kernels/ops/attention/mimo_local_attention.py` | [#42101](https://github.com/sgl-project/sglang/pull/42101) |
| `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` | [#41668](https://github.com/sgl-project/sglang/pull/41668), [#41886](https://github.com/sgl-project/sglang/pull/41886), [#42172](https://github.com/sgl-project/sglang/pull/42172) |
| `python/sglang/srt/entrypoints/openai/transcription_adapters/mimo_v2_asr.py` | [#26278](https://github.com/sgl-project/sglang/pull/26278) |
| `python/sglang/srt/function_call/mimo_detector.py` | [#15207](https://github.com/sgl-project/sglang/pull/15207) |
| `python/sglang/srt/models/mimo.py` | [#6059](https://github.com/sgl-project/sglang/pull/6059) |
| `python/sglang/srt/models/mimo_audio.py` | [#23811](https://github.com/sgl-project/sglang/pull/23811), [#26278](https://github.com/sgl-project/sglang/pull/26278), [#31343](https://github.com/sgl-project/sglang/pull/31343), [#42101](https://github.com/sgl-project/sglang/pull/42101) |
| `python/sglang/srt/models/mimo_mtp.py` | [#6059](https://github.com/sgl-project/sglang/pull/6059), [#7370](https://github.com/sgl-project/sglang/pull/7370) |
| `python/sglang/srt/models/mimo_v2.py` | [#23808](https://github.com/sgl-project/sglang/pull/23808), [#23811](https://github.com/sgl-project/sglang/pull/23811), [#24931](https://github.com/sgl-project/sglang/pull/24931), [#25455](https://github.com/sgl-project/sglang/pull/25455), [#26278](https://github.com/sgl-project/sglang/pull/26278), [#29493](https://github.com/sgl-project/sglang/pull/29493), [#31343](https://github.com/sgl-project/sglang/pull/31343), [#37565](https://github.com/sgl-project/sglang/pull/37565), [#40448](https://github.com/sgl-project/sglang/pull/40448), [#40888](https://github.com/sgl-project/sglang/pull/40888), [#40890](https://github.com/sgl-project/sglang/pull/40890), [#41108](https://github.com/sgl-project/sglang/pull/41108), ... (14 total) |
| `python/sglang/srt/models/mimo_v2_asr.py` | [#26278](https://github.com/sgl-project/sglang/pull/26278), [#31343](https://github.com/sgl-project/sglang/pull/31343) |
| `python/sglang/srt/models/mimo_v2_nextn.py` | [#23808](https://github.com/sgl-project/sglang/pull/23808), [#23811](https://github.com/sgl-project/sglang/pull/23811) |
| `python/sglang/srt/models/mimo_vl.py` | [#23811](https://github.com/sgl-project/sglang/pull/23811), [#29994](https://github.com/sgl-project/sglang/pull/29994), [#31343](https://github.com/sgl-project/sglang/pull/31343), [#40888](https://github.com/sgl-project/sglang/pull/40888) |
| `python/sglang/srt/multimodal/processors/mimo_audio.py` | [#26278](https://github.com/sgl-project/sglang/pull/26278), [#41667](https://github.com/sgl-project/sglang/pull/41667) |
| `python/sglang/srt/multimodal/processors/mimo_v2.py` | [#23811](https://github.com/sgl-project/sglang/pull/23811), [#24931](https://github.com/sgl-project/sglang/pull/24931), [#25588](https://github.com/sgl-project/sglang/pull/25588), [#26278](https://github.com/sgl-project/sglang/pull/26278), [#40888](https://github.com/sgl-project/sglang/pull/40888), [#41667](https://github.com/sgl-project/sglang/pull/41667) |
| `python/sglang/srt/multimodal/processors/mimo_v2_asr.py` | [#26278](https://github.com/sgl-project/sglang/pull/26278) |
| `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py` | [#37565](https://github.com/sgl-project/sglang/pull/37565) |
| `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py` | [#29131](https://github.com/sgl-project/sglang/pull/29131) |
| `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py` | [#28223](https://github.com/sgl-project/sglang/pull/28223) |
| `test/registered/e2e/models/test_mimo_v2.py` | no direct PR-number commit |
| `test/registered/e2e/models/test_mimo_v2_flash.py` | no direct PR-number commit |
| `test/registered/npu/llm_models/test_npu_mimo_7b_rl.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_mimo_vl_7b_rl.py` | no direct PR-number commit |
| `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mimo.py` | no direct PR-number commit |
| `test/registered/unit/models/test_mimo_fused_qkv_loader_layout.py` | no direct PR-number commit |
| `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py` | [#41108](https://github.com/sgl-project/sglang/pull/41108) |

## PR Coverage Summary

- Git-traced PRs: 29
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 29
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-05-22 | [#6059](https://github.com/sgl-project/sglang/pull/6059) | merged | Support XiaomiMiMo inference with mtp | `python/sglang/srt/models/mimo_mtp.py`, `python/sglang/srt/models/mimo.py` |
| 2025-06-20 | [#7370](https://github.com/sgl-project/sglang/pull/7370) | merged | Clean unused import for mimo mtp model | `python/sglang/srt/models/mimo_mtp.py` |
| 2025-12-19 | [#15207](https://github.com/sgl-project/sglang/pull/15207) | merged | [Feature] Xiaomi `MiMo-V2-Flash` day0 support | `python/sglang/srt/function_call/mimo_detector.py` |
| 2026-04-28 | [#23808](https://github.com/sgl-project/sglang/pull/23808) | merged | [Feature] Xiaomi MiMo-V2.5-Pro day0 support | `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py` |
| 2026-04-30 | [#23811](https://github.com/sgl-project/sglang/pull/23811) | merged | [Feature] Xiaomi MiMo-V2.5 day0 support | `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_vl.py` |
| 2026-05-18 | [#24931](https://github.com/sgl-project/sglang/pull/24931) | merged | feat(mimo-v2): add EPD disaggregation support | `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_v2.py` |
| 2026-05-19 | [#25588](https://github.com/sgl-project/sglang/pull/25588) | merged | perf(mimo-v2-epd): enable GPU image preprocess and parallel video decode | `python/sglang/srt/multimodal/processors/mimo_v2.py` |
| 2026-06-10 | [#25455](https://github.com/sgl-project/sglang/pull/25455) | merged | [NPU] MiMo-V2-Flash Adaptation | `python/sglang/srt/models/mimo_v2.py` |
| 2026-06-11 | [#26278](https://github.com/sgl-project/sglang/pull/26278) | merged | Support MiMo v2 ASR | `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2_asr.py` |
| 2026-06-15 | [#28223](https://github.com/sgl-project/sglang/pull/28223) | merged | [NPU] Add MiMo-V2-Flash manual testcases | `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py` |
| 2026-06-29 | [#29493](https://github.com/sgl-project/sglang/pull/29493) | merged | [NPU][Bugfix] Add scoring_func for mimo_v2 | `python/sglang/srt/models/mimo_v2.py` |
| 2026-07-04 | [#29994](https://github.com/sgl-project/sglang/pull/29994) | merged | fix(mimo-vl): pass padded_context_dim to Qwen2_5_VisionPatchMerger | `python/sglang/srt/models/mimo_vl.py` |
| 2026-07-15 | [#31343](https://github.com/sgl-project/sglang/pull/31343) | merged | Fix MiMo-V2 on Blackwell: FA3 fallback and TP-aware audio weight loading | `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2_asr.py`, `python/sglang/srt/models/mimo_v2.py` |
| 2026-07-21 | [#29131](https://github.com/sgl-project/sglang/pull/29131) | merged | [NPU] Adapt MiMo-V2.5-W8A8 | `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py` |
| 2026-09-12 | [#37565](https://github.com/sgl-project/sglang/pull/37565) | merged | [NPU] Support DFlash speculative decoding for MiMo-V2.5-Pro (mxfp4) | `python/sglang/srt/models/mimo_v2.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py` |
| 2026-09-20 | [#40448](https://github.com/sgl-project/sglang/pull/40448) | merged | [Feature] Xiaomi MiMo-V2.6/MiMo-V2.6-Pro day0 support | `python/sglang/srt/models/mimo_v2.py` |
| 2026-09-21 | [#40577](https://github.com/sgl-project/sglang/pull/40577) | merged | [Docs][NPU] Add MiMo-V2.5-Pro FP4 DFlash best practice on Ascend NPU | `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx` |
| 2026-09-21 | [#40622](https://github.com/sgl-project/sglang/pull/40622) | merged | Add MiMo-V2.6 cookbook | `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx` |
| 2026-09-23 | [#40969](https://github.com/sgl-project/sglang/pull/40969) | merged | [Doc] Add H200 recipes to MiMo-V2.6 cookbook | `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` |
| 2026-09-30 | [#41667](https://github.com/sgl-project/sglang/pull/41667) | merged | [Fix] Keep MiMo-V2 processor available without TorchCodec | `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py` |
| 2026-10-01 | [#41886](https://github.com/sgl-project/sglang/pull/41886) | merged | [Perf] Use FA4 by default for MiMo on SM100 | `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` |
| 2026-10-01 | [#41668](https://github.com/sgl-project/sglang/pull/41668) | merged | [Fix] Select the MXFP4 MoE runner for MiMo-V2 packed experts on SM100 | `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` |
| 2026-10-02 | [#42172](https://github.com/sgl-project/sglang/pull/42172) | merged | [Fix] Select the Marlin MoE runner for MiMo-V2 packed MXFP4 experts on SM90 | `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` |
| 2026-10-05 | [#42101](https://github.com/sgl-project/sglang/pull/42101) | merged | [Perf] Optimize MiMo local audio attention on Hopper | `python/sglang/srt/models/mimo_audio.py`, `python/sglang/kernels/ops/attention/mimo_local_attention.py` |
| 2026-10-06 | [#40888](https://github.com/sgl-project/sglang/pull/40888) | merged | fix(mimo-vl): keep multimodal features when capturing aux hidden states, and correct vision preprocessing | `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_vl.py` |
| 2026-10-14 | [#43639](https://github.com/sgl-project/sglang/pull/43639) | merged | [Perf] Enable native MXFP4 routing and CuTeDSL fusion for MiMo | `python/sglang/srt/models/mimo_v2.py` |
| 2026-10-15 | [#43106](https://github.com/sgl-project/sglang/pull/43106) | merged | Fuse MiMo verification RoPE and KV cache writes | `python/sglang/srt/models/mimo_v2.py` |
| 2026-10-31 | [#40890](https://github.com/sgl-project/sglang/pull/40890) | merged | [Perf] [NPU] mimo: fold attention_value_scale into o_proj weights | `python/sglang/srt/models/mimo_v2.py` |
| 2026-11-05 | [#41108](https://github.com/sgl-project/sglang/pull/41108) | merged | [Perf] mimo-v2: Optimize router GEMM with the HPC-Ops bf16xfp32 kernel | `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py`, `python/sglang/srt/models/mimo_v2.py` |

## Per-PR Diff Audit Cards

### PR #6059 - Support XiaomiMiMo inference with mtp

- Link: https://github.com/sgl-project/sglang/pull/6059
- Status/date: merged / 2025-05-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo.py`, `python/sglang/srt/models/mimo_mtp.py`; associated commits `a6ae3af15e84`
- Diff scope read: GitHub Pull Request files API returned 6 files, +344/-6, 388 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support XiaomiMiMo inference with mtp"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `python/sglang/srt/models/mimo_mtp.py`, `python/sglang/srt/models/mimo.py`; technical summary: Covers "Support XiaomiMiMo inference with mtp"; the main implementation surface is `python/sglang/srt/models/mimo_mtp.py`, `python/sglang/srt/models/mimo.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_mtp.py` added +220/-0 (220 lines); hunks: -0,0 +1,220; symbols: MiMoMultiTokenPredictorLayer, __init__, forward, MiMoMTP, touching `MiMoMultiTokenPredictorLayer, __init__, forward`; `python/sglang/srt/models/mimo.py` renamed +0/-0 (0 lines).
- Code diff details:
  - `python/sglang/srt/models/mimo_mtp.py` added +220/-0 (220 lines); hunks: -0,0 +1,220; symbols: MiMoMultiTokenPredictorLayer, __init__, forward, MiMoMTP
  - `python/sglang/srt/models/mimo.py` renamed +0/-0 (0 lines)
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_mtp.py
@@ -0,0 +1,220 @@
+# Adapted from https://github.com/vllm-project/vllm/pull/17433/files  and deepseek_nextn.py
+from functools import partial
+from typing import Any, Dict, Iterable, Optional, Tuple
+import torch
+from torch import nn
+from transformers import PretrainedConfig
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_mtp.py` added +220/-0; `python/sglang/srt/models/mimo.py` renamed +0/-0
- Risk and verification: The diff ships test coverage in `test/srt/models/test_mtp_models.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #7370 - Clean unused import for mimo mtp model

- Link: https://github.com/sgl-project/sglang/pull/7370
- Status/date: merged / 2025-06-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_mtp.py`; associated commits `dea8aa7ab8e8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-18, 36 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Clean unused import for mimo mtp model"; model line: MiMo V2 Flash; category: model implementation change; main diff: `python/sglang/srt/models/mimo_mtp.py`; technical summary: Covers "Clean unused import for mimo mtp model"; the main implementation surface is `python/sglang/srt/models/mimo_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_mtp.py` modified +2/-18 (20 lines); hunks: -7,33 +7,17; symbols: MiMoMultiTokenPredictorLayer, touching `MiMoMultiTokenPredictorLayer`.
- Code diff details:
  - `python/sglang/srt/models/mimo_mtp.py` modified +2/-18 (20 lines); hunks: -7,33 +7,17; symbols: MiMoMultiTokenPredictorLayer
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_mtp.py
@@ -7,33 +7,17 @@
-from sglang.srt.distributed import (
-    get_tensor_model_parallel_rank,
-    get_tensor_model_parallel_world_size,
-    split_tensor_along_last_dim,
-    tensor_model_parallel_all_gather,
-)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_mtp.py` modified +2/-18
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/mimo_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15207 - [Feature] Xiaomi `MiMo-V2-Flash` day0 support

- Link: https://github.com/sgl-project/sglang/pull/15207
- Status/date: merged / 2025-12-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/mimo_detector.py`; associated commits `160a06cab23f`
- Diff scope read: GitHub Pull Request files API returned 38 files, +5396/-169, 6509 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Xiaomi `MiMo-V2-Flash` day0 support"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/function_call/mimo_detector.py`; technical summary: Covers "[Feature] Xiaomi `MiMo-V2-Flash` day0 support"; the main implementation surface is `python/sglang/srt/function_call/mimo_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/mimo_detector.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: _get_param_type, _convert_param_value, MiMoDetector, __init__, touching `_get_param_type, _convert_param_value, MiMoDetector`.
- Code diff details:
  - `python/sglang/srt/function_call/mimo_detector.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: _get_param_type, _convert_param_value, MiMoDetector, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/mimo_detector.py
@@ -0,0 +1,281 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/mimo_detector.py` added +281/-0
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #23808 - [Feature] Xiaomi MiMo-V2.5-Pro day0 support

- Link: https://github.com/sgl-project/sglang/pull/23808
- Status/date: merged / 2026-04-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py`; associated commits `1a55646dcdf0`
- Diff scope read: GitHub Pull Request files API returned 5 files, +80/-23, 280 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Xiaomi MiMo-V2.5-Pro day0 support"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py`; technical summary: Covers "[Feature] Xiaomi MiMo-V2.5-Pro day0 support"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` renamed +27/-8 (35 lines); hunks: -76,7 +76,7; -178,7 +178,7 @@ class MiMoV2MoE(nn.Module):; symbols: MiMoV2MoE, __init__, forward, MiMoV2DecoderLayer, touching `MiMoV2MoE, __init__, forward`; `python/sglang/srt/models/mimo_v2_nextn.py` renamed +21/-6 (27 lines); hunks: -28,6 +28,7; -39,23 +40,23; symbols: MiMoV2MTPLayer, __init__, forward, MiMoV2MTP, touching `MiMoV2MTPLayer, __init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` renamed +27/-8 (35 lines); hunks: -76,7 +76,7; -178,7 +178,7 @@ class MiMoV2MoE(nn.Module):; symbols: MiMoV2MoE, __init__, forward, MiMoV2DecoderLayer
  - `python/sglang/srt/models/mimo_v2_nextn.py` renamed +21/-6 (27 lines); hunks: -28,6 +28,7; -39,23 +40,23; symbols: MiMoV2MTPLayer, __init__, forward, MiMoV2MTP
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -76,7 +76,7 @@
-MiMoV2FlashConfig = None
+MiMoV2Config = None
@@ -178,7 +178,7 @@ class MiMoV2MoE(nn.Module):
-        config: MiMoV2FlashConfig,
+        config: MiMoV2Config,
@@ -562,7 +562,7 @@ def forward(
diff -- python/sglang/srt/models/mimo_v2_nextn.py
@@ -28,6 +28,7 @@
+    get_attention_tp_size,
@@ -39,23 +40,23 @@
-from sglang.srt.models.mimo_v2_flash import (
+from sglang.srt.models.mimo_v2 import (
-    MiMoV2FlashForCausalLM,
+    MiMoV2ForCausalLM,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` renamed +27/-8; `python/sglang/srt/models/mimo_v2_nextn.py` renamed +21/-6
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23811 - [Feature] Xiaomi MiMo-V2.5 day0 support

- Link: https://github.com/sgl-project/sglang/pull/23811
- Status/date: merged / 2026-04-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_nextn.py`, `python/sglang/srt/models/mimo_vl.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`; associated commits `651af06a0b5e`
- Diff scope read: GitHub Pull Request files API returned 16 files, +4369/-87, 4885 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Xiaomi MiMo-V2.5 day0 support"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_vl.py`; technical summary: Covers "[Feature] Xiaomi MiMo-V2.5 day0 support"; the main implementation surface is `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/mimo_v2.py` added +2039/-0 (2039 lines); hunks: -0,0 +1,2039; symbols: ImageInput, __post_init__, VideoInput, AudioInput, touching `ImageInput, __post_init__, VideoInput`; `python/sglang/srt/models/mimo_audio.py` added +1350/-0 (1350 lines); hunks: -0,0 +1,1350; symbols: flash_attn_varlen_func, _compute_default_rope_parameters, _dynamic_rope_update, longrope_frequency_update, touching `flash_attn_varlen_func, _compute_default_rope_parameters, _dynamic_rope_update`; `python/sglang/srt/models/mimo_vl.py` added +507/-0 (507 lines); hunks: -0,0 +1,507; symbols: MiMoVLVisionConfig, __init__, MiMoVisionPatchEmbed, sync_proj_weight_linear_format, touching `MiMoVLVisionConfig, __init__, MiMoVisionPatchEmbed`; `python/sglang/srt/models/mimo_v2.py` modified +222/-13 (235 lines); hunks: -13,13 +13,14; -63,11 +64,18; symbols: load_mimo_v2_qkv_proj_weight, MiMoV2MLP, __init__, routed_experts_weights_of_layer, touching `load_mimo_v2_qkv_proj_weight, MiMoV2MLP, __init__`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/mimo_v2.py` added +2039/-0 (2039 lines); hunks: -0,0 +1,2039; symbols: ImageInput, __post_init__, VideoInput, AudioInput
  - `python/sglang/srt/models/mimo_audio.py` added +1350/-0 (1350 lines); hunks: -0,0 +1,1350; symbols: flash_attn_varlen_func, _compute_default_rope_parameters, _dynamic_rope_update, longrope_frequency_update
  - `python/sglang/srt/models/mimo_vl.py` added +507/-0 (507 lines); hunks: -0,0 +1,507; symbols: MiMoVLVisionConfig, __init__, MiMoVisionPatchEmbed, sync_proj_weight_linear_format
  - `python/sglang/srt/models/mimo_v2.py` modified +222/-13 (235 lines); hunks: -13,13 +13,14; -63,11 +64,18; symbols: load_mimo_v2_qkv_proj_weight, MiMoV2MLP, __init__, routed_experts_weights_of_layer
  - `python/sglang/srt/models/mimo_v2_nextn.py` modified +12/-7 (19 lines); hunks: -19,6 +19,7; -28,7 +29,6; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/mimo_v2.py
@@ -0,0 +1,2039 @@
+"""MiMoV2 multimodal processor -- protocol, utilities, and processor."""
+import asyncio
+import base64
+import copy
+import io
+import json
diff -- python/sglang/srt/models/mimo_audio.py
@@ -0,0 +1,1350 @@
+"""MiMo audio: tokenizer, encoding utilities, and audio encoder."""
+# Audio tokenizer adapted from https://github.com/XiaomiMiMo/MiMo-Audio-Tokenizer.git
+import logging
+import math
+import os
+import typing as tp
diff -- python/sglang/srt/models/mimo_vl.py
@@ -0,0 +1,507 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/mimo_v2.py` added +2039/-0; `python/sglang/srt/models/mimo_audio.py` added +1350/-0; `python/sglang/srt/models/mimo_vl.py` added +507/-0; `python/sglang/srt/models/mimo_v2.py` modified +222/-13; `python/sglang/srt/models/mimo_v2_nextn.py` modified +12/-7
- Risk and verification: The diff ships test coverage in `python/sglang/test/server_fixtures/mmmu_fixture.py`, `test/registered/8-gpu-models/test_mimo_models.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #24931 - feat(mimo-v2): add EPD disaggregation support

- Link: https://github.com/sgl-project/sglang/pull/24931
- Status/date: merged / 2026-05-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`; associated commits `784fe7e99b80`
- Diff scope read: GitHub Pull Request files API returned 7 files, +961/-289, 1710 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat(mimo-v2): add EPD disaggregation support"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "feat(mimo-v2): add EPD disaggregation support"; the main implementation surface is `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +559/-110 (669 lines); hunks: -268,6 +268,49 @@ def __post_init__(self):; -445,6 +488,207 @@ def __init__(; symbols: __post_init__, _decode_frames_and_timestamps, _ffprobe_has_audio, MiMoProcessor, touching `__post_init__, _decode_frames_and_timestamps, _ffprobe_has_audio`; `python/sglang/srt/models/mimo_v2.py` modified +148/-28 (176 lines); hunks: -68,7 +68,11; -1007,6 +1011,11 @@ class MiMoV2ForCausalLM(nn.Module):; symbols: MiMoV2ForCausalLM, __init__, routed_experts_weights_of_layer, touching `MiMoV2ForCausalLM, __init__, routed_experts_weights_of_layer`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +559/-110 (669 lines); hunks: -268,6 +268,49 @@ def __post_init__(self):; -445,6 +488,207 @@ def __init__(; symbols: __post_init__, _decode_frames_and_timestamps, _ffprobe_has_audio, MiMoProcessor
  - `python/sglang/srt/models/mimo_v2.py` modified +148/-28 (176 lines); hunks: -68,7 +68,11; -1007,6 +1011,11 @@ class MiMoV2ForCausalLM(nn.Module):; symbols: MiMoV2ForCausalLM, __init__, routed_experts_weights_of_layer
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/mimo_v2.py
@@ -268,6 +268,49 @@ def __post_init__(self):
+def _decode_frames_and_timestamps(vdw, ele):
+    # Shared E/D frame-sampling recipe: smart_nframes + linspace + permute.
+    total_frames, video_fps = len(vdw), vdw.avg_fps
+    nframes = smart_nframes(ele, total_frames=total_frames, video_fps=video_fps)
+    idx = list(np.unique(np.linspace(0, total_frames - 1, num=nframes, dtype=np.int64)))
+    video_tensor = vdw.get_frames_as_tensor(idx).permute(0, 3, 1, 2).float()
diff -- python/sglang/srt/models/mimo_v2.py
@@ -68,7 +68,11 @@
-from sglang.srt.managers.schedule_batch import MultimodalDataItem, MultimodalInputs
+from sglang.srt.managers.schedule_batch import (
+    Modality,
+    MultimodalDataItem,
+    MultimodalInputs,
+)
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +559/-110; `python/sglang/srt/models/mimo_v2.py` modified +148/-28
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/managers/mm_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25588 - perf(mimo-v2-epd): enable GPU image preprocess and parallel video decode

- Link: https://github.com/sgl-project/sglang/pull/25588
- Status/date: merged / 2026-05-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/mimo_v2.py`; associated commits `f0763859edbb`
- Diff scope read: GitHub Pull Request files API returned 3 files, +75/-8, 188 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "perf(mimo-v2-epd): enable GPU image preprocess and parallel video decode"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/multimodal/processors/mimo_v2.py`; technical summary: Covers "perf(mimo-v2-epd): enable GPU image preprocess and parallel video decode"; the main implementation surface is `python/sglang/srt/multimodal/processors/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +26/-2 (28 lines); hunks: -359,11 +359,13 @@ def __init__(; -546,6 +548,20 @@ def _as_dict(obj):; symbols: __init__, _as_dict, _load_video_for_encoder, preprocess_for_encoder, touching `__init__, _as_dict, _load_video_for_encoder`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +26/-2 (28 lines); hunks: -359,11 +359,13 @@ def __init__(; -546,6 +548,20 @@ def _as_dict(obj):; symbols: __init__, _as_dict, _load_video_for_encoder, preprocess_for_encoder
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/mimo_v2.py
@@ -359,11 +359,13 @@ def __init__(
+        video_decode_num_threads=0,
+        self.video_decode_num_threads = video_decode_num_threads
@@ -546,6 +548,20 @@ def _as_dict(obj):
+        image_cfg = (mm_config or {}).get("image", {})
+        if "device" in image_cfg:
+            kwargs["device"] = image_cfg["device"]
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +26/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/utils/video_decoder.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25455 - [NPU] MiMo-V2-Flash Adaptation

- Link: https://github.com/sgl-project/sglang/pull/25455
- Status/date: merged / 2026-06-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`; associated commits `2947781ce6b3`
- Diff scope read: GitHub Pull Request files API returned 9 files, +419/-67, 740 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] MiMo-V2-Flash Adaptation"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "[NPU] MiMo-V2-Flash Adaptation"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +8/-2 (10 lines); hunks: -282,7 +282,11 @@ def __init__(; -299,7 +303,9 @@ def __init__(; symbols: __init__, get_moe_weights, touching `__init__, get_moe_weights`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +8/-2 (10 lines); hunks: -282,7 +282,11 @@ def __init__(; -299,7 +303,9 @@ def __init__(; symbols: __init__, get_moe_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -282,7 +282,11 @@ def __init__(
-        if get_moe_a2a_backend().is_deepep() or get_moe_a2a_backend().is_mooncake():
+        if (
+            get_moe_a2a_backend().is_deepep()
+            or get_moe_a2a_backend().is_mooncake()
+            or get_moe_a2a_backend().is_ascend_fuseep()
+        ):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +8/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26278 - Support MiMo v2 ASR

- Link: https://github.com/sgl-project/sglang/pull/26278
- Status/date: merged / 2026-06-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/entrypoints/openai/transcription_adapters/mimo_v2_asr.py`, `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_asr.py`, `python/sglang/srt/multimodal/processors/mimo_audio.py` and 7 files; associated commits `ec0eb6cce8a1`
- Diff scope read: GitHub Pull Request files API returned 9 files, +991/-434, 1757 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support MiMo v2 ASR"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2_asr.py`; technical summary: Covers "Support MiMo v2 ASR"; the main implementation surface is `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2_asr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +51/-276 (327 lines); hunks: -3,21 +3,16; -39,20 +34,14; symbols: ImageInput, __post_init__, AudioInput, VideoAudioInput, touching `ImageInput, __post_init__, AudioInput`; `python/sglang/srt/multimodal/processors/mimo_audio.py` added +318/-0 (318 lines); hunks: -0,0 +1,318; symbols: AudioInput, __post_init__, MiMoAudioPipeline, __init__, touching `AudioInput, __post_init__, MiMoAudioPipeline`; `python/sglang/srt/multimodal/processors/mimo_v2_asr.py` added +286/-0 (286 lines); hunks: -0,0 +1,286; symbols: _Content, MiMoV2ASRProcessor, __init__, __getattr__, touching `_Content, MiMoV2ASRProcessor, __init__`; `python/sglang/srt/models/mimo_audio.py` modified +99/-92 (191 lines); hunks: -8,7 +8,7; -1141,72 +1141,89 @@ def output_local_config(self):; symbols: output_local_config, MiMoAudioEncoder, AudioEncoderMixin, __init__, touching `output_local_config, MiMoAudioEncoder, AudioEncoderMixin`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +51/-276 (327 lines); hunks: -3,21 +3,16; -39,20 +34,14; symbols: ImageInput, __post_init__, AudioInput, VideoAudioInput
  - `python/sglang/srt/multimodal/processors/mimo_audio.py` added +318/-0 (318 lines); hunks: -0,0 +1,318; symbols: AudioInput, __post_init__, MiMoAudioPipeline, __init__
  - `python/sglang/srt/multimodal/processors/mimo_v2_asr.py` added +286/-0 (286 lines); hunks: -0,0 +1,286; symbols: _Content, MiMoV2ASRProcessor, __init__, __getattr__
  - `python/sglang/srt/models/mimo_audio.py` modified +99/-92 (191 lines); hunks: -8,7 +8,7; -1141,72 +1141,89 @@ def output_local_config(self):; symbols: output_local_config, MiMoAudioEncoder, AudioEncoderMixin, __init__
  - `python/sglang/srt/models/mimo_v2_asr.py` added +162/-0 (162 lines); hunks: -0,0 +1,162; symbols: _maybe_override_audio_attn_for_blackwell, MiMoV2ASRForCausalLM, __init__, pad_input_ids
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/mimo_v2.py
@@ -3,21 +3,16 @@
-import io
-import os
-import time
-from collections import OrderedDict
-import pybase64
@@ -39,20 +34,14 @@
diff -- python/sglang/srt/multimodal/processors/mimo_audio.py
@@ -0,0 +1,318 @@
+"""Stateful audio preprocessing pipeline shared by MiMo multimodal and ASR processors."""
+import io
+import math
+import os
+import time
+from collections import OrderedDict
diff -- python/sglang/srt/multimodal/processors/mimo_v2_asr.py
@@ -0,0 +1,286 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +51/-276; `python/sglang/srt/multimodal/processors/mimo_audio.py` added +318/-0; `python/sglang/srt/multimodal/processors/mimo_v2_asr.py` added +286/-0; `python/sglang/srt/models/mimo_audio.py` modified +99/-92; `python/sglang/srt/models/mimo_v2_asr.py` added +162/-0; `python/sglang/srt/models/mimo_v2.py` modified +24/-66
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/__init__.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/mimo_v2_asr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28223 - [NPU] Add MiMo-V2-Flash manual testcases

- Link: https://github.com/sgl-project/sglang/pull/28223
- Status/date: merged / 2026-06-15
- Trace source: `git log --name-only -- <model-files>` found it through `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py`; associated commits `3df6e2f9681a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +40/-0, 48 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Add MiMo-V2-Flash manual testcases"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py`; technical summary: Covers "[NPU] Add MiMo-V2-Flash manual testcases"; the main implementation surface is `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py` added +39/-0 (39 lines); hunks: -0,0 +1,39; symbols: TestMiMoV2FlashGraphWithMTP, touching `TestMiMoV2FlashGraphWithMTP`.
- Code diff details:
  - `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py` added +39/-0 (39 lines); hunks: -0,0 +1,39; symbols: TestMiMoV2FlashGraphWithMTP
- Key code excerpts:

```diff
diff -- test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py
@@ -0,0 +1,39 @@
+import unittest
+from sglang.test.ascend.gsm8k_ascend_mixin import GSM8KAscendMixin
+from sglang.test.ascend.test_ascend_utils import MIMO_V2_FLASH_WEIGHTS_PATH
+from sglang.test.test_utils import CustomTestCase
+class TestMiMoV2FlashGraphWithMTP(GSM8KAscendMixin, CustomTestCase):
+    """Testcase: Verify the inference accuracy of MiMo-V2-Flash on GSM8K with cuda graph and MTP (speculative decoding).
```

- Reviewed files:
  - tests: `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py` added +39/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29493 - [NPU][Bugfix] Add scoring_func for mimo_v2

- Link: https://github.com/sgl-project/sglang/pull/29493
- Status/date: merged / 2026-06-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`; associated commits `d5133e925bbd`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU][Bugfix] Add scoring_func for mimo_v2"; model line: MiMo V2 Flash; category: bug fix; main diff: `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "[NPU][Bugfix] Add scoring_func for mimo_v2"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +1/-0 (1 lines); hunks: -270,6 +270,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +1/-0 (1 lines); hunks: -270,6 +270,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -270,6 +270,7 @@ def __init__(
+            scoring_func=config.scoring_func,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/mimo_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #29994 - fix(mimo-vl): pass padded_context_dim to Qwen2_5_VisionPatchMerger

- Link: https://github.com/sgl-project/sglang/pull/29994
- Status/date: merged / 2026-07-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_vl.py`; associated commits `b28bc1060f1e`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-0, 12 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(mimo-vl): pass padded_context_dim to Qwen2_5_VisionPatchMerger"; model line: MiMo V2 Flash; category: bug fix; main diff: `python/sglang/srt/models/mimo_vl.py`; technical summary: Covers "fix(mimo-vl): pass padded_context_dim to Qwen2_5_VisionPatchMerger"; the main implementation surface is `python/sglang/srt/models/mimo_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_vl.py` modified +5/-0 (5 lines); hunks: -301,6 +301,11 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/mimo_vl.py` modified +5/-0 (5 lines); hunks: -301,6 +301,11 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_vl.py
@@ -301,6 +301,11 @@ def __init__(
+            # MiMo-VL's merger MLP is square (intermediate == context_dim * merge**2),
+            # so no dim padding is needed. The Qwen2.5-VL formula num_heads * head_dim
+            # over-sizes it here because MiMo uses qk_channels (64) for head_dim rather
+            # than hidden_size // num_heads, which would mismatch the checkpoint.
+            padded_context_dim=hidden_size,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_vl.py` modified +5/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/mimo_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31343 - Fix MiMo-V2 on Blackwell: FA3 fallback and TP-aware audio weight loading

- Link: https://github.com/sgl-project/sglang/pull/31343
- Status/date: merged / 2026-07-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_asr.py`, `python/sglang/srt/models/mimo_vl.py`; associated commits `5abec3fbf879`
- Diff scope read: GitHub Pull Request files API returned 4 files, +110/-92, 281 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix MiMo-V2 on Blackwell: FA3 fallback and TP-aware audio weight loading"; model line: MiMo V2 Flash; category: bug fix; main diff: `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2_asr.py`, `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "Fix MiMo-V2 on Blackwell: FA3 fallback and TP-aware audio weight loading"; the main implementation surface is `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2_asr.py`, `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_audio.py` modified +90/-59 (149 lines); hunks: -20,17 +20,9; -477,6 +469,22 @@ def get_position_ids(lengths):; symbols: flash_attn_varlen_func, get_position_ids, _audio_rope_applier, AudioEncoderAttention, touching `flash_attn_varlen_func, get_position_ids, _audio_rope_applier`; `python/sglang/srt/models/mimo_v2_asr.py` modified +0/-32 (32 lines); hunks: -18,43 +18,12; -84,7 +53,6 @@ def __init__(; symbols: _maybe_override_audio_attn_for_blackwell, __init__, touching `_maybe_override_audio_attn_for_blackwell, __init__`; `python/sglang/srt/models/mimo_v2.py` modified +19/-0 (19 lines); hunks: -1277,6 +1277,25 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights, touching `load_weights`; `python/sglang/srt/models/mimo_vl.py` modified +1/-1 (2 lines); hunks: -279,7 +279,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/mimo_audio.py` modified +90/-59 (149 lines); hunks: -20,17 +20,9; -477,6 +469,22 @@ def get_position_ids(lengths):; symbols: flash_attn_varlen_func, get_position_ids, _audio_rope_applier, AudioEncoderAttention
  - `python/sglang/srt/models/mimo_v2_asr.py` modified +0/-32 (32 lines); hunks: -18,43 +18,12; -84,7 +53,6 @@ def __init__(; symbols: _maybe_override_audio_attn_for_blackwell, __init__
  - `python/sglang/srt/models/mimo_v2.py` modified +19/-0 (19 lines); hunks: -1277,6 +1277,25 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights
  - `python/sglang/srt/models/mimo_vl.py` modified +1/-1 (2 lines); hunks: -279,7 +279,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_audio.py
@@ -20,17 +20,9 @@
+from sglang.srt.layers.attention.vision import VisionAttention
-from sglang.srt.utils import is_cuda
-if is_cuda():
-    from sgl_kernel.flash_attn import flash_attn_varlen_func
-else:
-    def flash_attn_varlen_func(*args, **kwargs):
diff -- python/sglang/srt/models/mimo_v2_asr.py
@@ -18,43 +18,12 @@
-from sglang.srt.models import mimo_audio as _mimo_audio_module
-def _maybe_override_audio_attn_for_blackwell() -> None:
-    """Swap mimo_audio.flash_attn_varlen_func to upstream FA2 on GPUs that
-    sgl-kernel's FA3 doesn't support.
-    sgl-kernel FA3 only covers sm80/86/89/90 — on Blackwell consumer cards
-    (sm_120 / RTX 50xx) its varlen kernel raises NotImplementedError. ASR is
diff -- python/sglang/srt/models/mimo_v2.py
@@ -1277,6 +1277,25 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_audio.py` modified +90/-59; `python/sglang/srt/models/mimo_v2_asr.py` modified +0/-32; `python/sglang/srt/models/mimo_v2.py` modified +19/-0; `python/sglang/srt/models/mimo_vl.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_asr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #29131 - [NPU] Adapt MiMo-V2.5-W8A8

- Link: https://github.com/sgl-project/sglang/pull/29131
- Status/date: merged / 2026-07-21
- Trace source: `git log --name-only -- <model-files>` found it through `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py`; associated commits `d6ef68881e26`
- Diff scope read: GitHub Pull Request files API returned 3 files, +54/-0, 69 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Adapt MiMo-V2.5-W8A8"; model line: MiMo V2 Flash; category: docs/tests/CI; main diff: `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py`; technical summary: Covers "[NPU] Adapt MiMo-V2.5-W8A8"; the main implementation surface is `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py` added +49/-0 (49 lines); hunks: -0,0 +1,49; symbols: TestMiMoV25W8A8GraphWithMTP, touching `TestMiMoV25W8A8GraphWithMTP`.
- Code diff details:
  - `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py` added +49/-0 (49 lines); hunks: -0,0 +1,49; symbols: TestMiMoV25W8A8GraphWithMTP
- Key code excerpts:

```diff
diff -- test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py
@@ -0,0 +1,49 @@
+import unittest
+from sglang.test.ascend.gsm8k_ascend_mixin import GSM8KAscendMixin
+from sglang.test.ascend.test_ascend_utils import MIMO_V2_5_W8A8_WEIGHTS_PATH
+from sglang.test.test_utils import CustomTestCase
+class TestMiMoV25W8A8GraphWithMTP(GSM8KAscendMixin, CustomTestCase):
+    """Testcase: Verify the inference accuracy of MiMo-V2.5-W8A8 on GSM8K with cuda graph and MTP (speculative decoding).
```

- Reviewed files:
  - tests: `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py` added +49/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37565 - [NPU] Support DFlash speculative decoding for MiMo-V2.5-Pro (mxfp4)

- Link: https://github.com/sgl-project/sglang/pull/37565
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py`; associated commits `a984c78330a8`
- Diff scope read: GitHub Pull Request files API returned 15 files, +742/-81, 1341 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Support DFlash speculative decoding for MiMo-V2.5-Pro (mxfp4)"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/models/mimo_v2.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py`; technical summary: Covers "[NPU] Support DFlash speculative decoding for MiMo-V2.5-Pro (mxfp4)"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +62/-5 (67 lines); hunks: -31,6 +31,10; -873,10 +877,16 @@ def forward(; symbols: forward, __init__, touching `forward, __init__`; `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py` added +47/-0 (47 lines); hunks: -0,0 +1,47; symbols: TestMiMoV25ProFP4GraphWithDFlash, touching `TestMiMoV25ProFP4GraphWithDFlash`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +62/-5 (67 lines); hunks: -31,6 +31,10; -873,10 +877,16 @@ def forward(; symbols: forward, __init__
  - `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py` added +47/-0 (47 lines); hunks: -0,0 +1,47; symbols: TestMiMoV25ProFP4GraphWithDFlash
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -31,6 +31,10 @@
+from sglang.srt.layers.aux_hidden_states import (
+    AuxHiddenStateAccumulator,
+    AuxHiddenStatePacker,
+)
@@ -873,10 +877,16 @@ def forward(
+        captured_last_layer_outputs: Optional[AuxHiddenStateAccumulator] = None,
diff -- test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py
@@ -0,0 +1,47 @@
+import unittest
+from sglang.test.ascend.gsm8k_ascend_mixin import GSM8KAscendMixin
+from sglang.test.ascend.test_ascend_utils import (
+    MIMO_V2_5_PRO_FP4_DFLASH_DRAFT_WEIGHTS_PATH,
+    MIMO_V2_5_PRO_FP4_DFLASH_WEIGHTS_PATH,
+)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +62/-5
  - tests: `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py` added +47/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_5_pro_fp4_dflash.py`, `test/registered/spec/dspark/test_dspark_stacked_ctx_kv_parity.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #40448 - [Feature] Xiaomi MiMo-V2.6/MiMo-V2.6-Pro day0 support

- Link: https://github.com/sgl-project/sglang/pull/40448
- Status/date: merged / 2026-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`; associated commits `983e643854f1`
- Diff scope read: GitHub Pull Request files API returned 3 files, +26/-6, 82 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Xiaomi MiMo-V2.6/MiMo-V2.6-Pro day0 support"; model line: MiMo V2 Flash; category: model support/runtime entry; main diff: `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "[Feature] Xiaomi MiMo-V2.6/MiMo-V2.6-Pro day0 support"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +18/-4 (22 lines); hunks: -349,7 +349,7 @@ def __init__(; -359,7 +359,7 @@ def __init__(; symbols: __init__, forward, MiMoV2MoE, touching `__init__, forward, MiMoV2MoE`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +18/-4 (22 lines); hunks: -349,7 +349,7 @@ def __init__(; -359,7 +359,7 @@ def __init__(; symbols: __init__, forward, MiMoV2MoE
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -349,7 +349,7 @@ def __init__(
-        self.dtype = torch.float32
+        self.dtype = getattr(torch, getattr(config, "moe_router_dtype", "float32"))
@@ -359,7 +359,7 @@ def __init__(
-                else self.dtype
+                else torch.float32
@@ -368,9 +368,15 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +18/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/mimo_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #40577 - [Docs][NPU] Add MiMo-V2.5-Pro FP4 DFlash best practice on Ascend NPU

- Link: https://github.com/sgl-project/sglang/pull/40577
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx`; associated commits `69d1e5cfe06e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +175/-0, 190 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Docs][NPU] Add MiMo-V2.5-Pro FP4 DFlash best practice on Ascend NPU"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx`; technical summary: Covers "[Docs][NPU] Add MiMo-V2.5-Pro FP4 DFlash best practice on Ascend NPU"; the main implementation surface is `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx` added +170/-0 (170 lines); hunks: -0,0 +1,170.
- Code diff details:
  - `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx` added +170/-0 (170 lines); hunks: -0,0 +1,170
- Key code excerpts:

```diff
diff -- docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx
@@ -0,0 +1,170 @@
+---
+title: "MiMo-V2.5-Pro"
+metatags:
+  description: "Best Practice for MiMo-V2.5-Pro on Ascend NPU"
+---
+<Note>
```

- Reviewed files:
  - docs: `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx` added +170/-0
- Risk and verification: This is mostly docs/examples in `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #40622 - Add MiMo-V2.6 cookbook

- Link: https://github.com/sgl-project/sglang/pull/40622
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`; associated commits `2261c2e6188a`
- Diff scope read: GitHub Pull Request files API returned 5 files, +264/-2, 289 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add MiMo-V2.6 cookbook"; model line: MiMo V2 Flash; category: docs/tests/CI; main diff: `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`; technical summary: Covers "Add MiMo-V2.6 cookbook"; the main implementation surface is `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx` added +138/-0 (138 lines); hunks: -0,0 +1,138; `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` added +124/-0 (124 lines); hunks: -0,0 +1,124; `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx` modified +0/-1 (1 lines); hunks: -2,7 +2,6.
- Code diff details:
  - `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx` added +138/-0 (138 lines); hunks: -0,0 +1,138
  - `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` added +124/-0 (124 lines); hunks: -0,0 +1,124
  - `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx` modified +0/-1 (1 lines); hunks: -2,7 +2,6
- Key code excerpts:

```diff
diff -- docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx
@@ -0,0 +1,138 @@
+// Instantiated from cookbook-add-model/templates/config.jsx.tmpl.
+// Recipes: https://github.com/sgl-project/sglang/pull/40448
+// SGLang: 983e643854f15cf9ef4370a49dfd74b6af54c3e3.
+// B300 validation reported by the model team. Public V2.6 checkpoints are
+// XiaomiMiMo/MiMo-V2.6-{Flash,Pro}-RL (MXFP4 experts, bf16 router, bundled
+// dflash/ drafter); modelNames are served aliases, and the checkpoint paths
diff -- docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx
@@ -0,0 +1,124 @@
+---
+title: MiMo-V2.6
+description: "Deploy MiMo-V2.6-Flash and Pro with SGLang on NVIDIA B300 GPUs, using MXFP4 MoE weights, BF16 routing, DFlash decoding, and a 1M-token context window."
+tag: NEW
+---
+## Deployment
diff -- docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx
@@ -2,7 +2,6 @@
```

- Reviewed files:
  - docs: `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx` added +138/-0; `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` added +124/-0; `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx` modified +0/-1
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/cookbook/autoregressive/intro.mdx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #40969 - [Doc] Add H200 recipes to MiMo-V2.6 cookbook

- Link: https://github.com/sgl-project/sglang/pull/40969
- Status/date: merged / 2026-09-23
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`; associated commits `ffac53d779c0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +41/-8, 100 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] Add H200 recipes to MiMo-V2.6 cookbook"; model line: MiMo V2 Flash; category: docs/tests/CI; main diff: `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`; technical summary: Covers "[Doc] Add H200 recipes to MiMo-V2.6 cookbook"; the main implementation surface is `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx` modified +36/-3 (39 lines); hunks: -1,13 +1,14; -35,7 +36,7 @@ export const config = {; `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` modified +5/-5 (10 lines); hunks: -1,12 +1,12; -69,7 +69,7 @@ import { Playground } from "/src/snippets/_playground.jsx";.
- Code diff details:
  - `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx` modified +36/-3 (39 lines); hunks: -1,13 +1,14; -35,7 +36,7 @@ export const config = {
  - `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` modified +5/-5 (10 lines); hunks: -1,12 +1,12; -69,7 +69,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- Key code excerpts:

```diff
diff -- docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx
@@ -1,13 +1,14 @@
-// B300 validation reported by the model team. Public V2.6 checkpoints are
+// B300 validation reported by the model team. H200 cells reuse the B300
+// recipes with `--moe-runner-backend marlin` in place of deep_gemm. Public V2.6 checkpoints are
-  supportedHardware: ["b300"],
+  supportedHardware: ["h200", "b300"],
@@ -35,7 +36,7 @@ export const config = {
diff -- docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx
@@ -1,12 +1,12 @@
-description: "Deploy MiMo-V2.6-Flash and Pro with SGLang on NVIDIA B300 GPUs, using MXFP4 MoE weights, BF16 routing, DFlash decoding, and a 1M-token context window."
+description: "Deploy MiMo-V2.6-Flash and Pro with SGLang on NVIDIA H200 and B300 GPUs, using MXFP4 MoE weights, BF16 routing, DFlash decoding, and a 1M-token context window."
-The recipes below target **MiMo-V2.6-Flash on 4× B300** and **MiMo-V2.6-Pro on 8× B300**, each on a single node. Both use MXFP4 MoE weights, a BF16 MoE router, and DFlash speculat
+The recipes below target **MiMo-V2.6-Flash on 4× H200 or B300** and **MiMo-V2.6-Pro on 8× H200 or B300**, each on a single node. Both use MXFP4 MoE weights, a BF16 MoE router, and
@@ -69,7 +69,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-      <th style={{textAlign: "left", padding: "10px 12px", backgroundColor: "rgba(255,255,255,0.05)"}}>B300 recipe</th>
```

- Reviewed files:
  - docs: `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx` modified +36/-3; `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx` modified +5/-5
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #41667 - [Fix] Keep MiMo-V2 processor available without TorchCodec

- Link: https://github.com/sgl-project/sglang/pull/41667
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`; associated commits `488869c2d0f3`
- Diff scope read: GitHub Pull Request files API returned 2 files, +11/-3, 43 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Keep MiMo-V2 processor available without TorchCodec"; model line: MiMo V2 Flash; category: bug fix; main diff: `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`; technical summary: Covers "[Fix] Keep MiMo-V2 processor available without TorchCodec"; the main implementation surface is `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/mimo_audio.py` modified +5/-2 (7 lines); hunks: -17,9 +17,12; `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +6/-1 (7 lines); hunks: -16,7 +16,6; -33,6 +32,7; symbols: _as_dict, has_audio_track, touching `_as_dict, has_audio_track`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/mimo_audio.py` modified +5/-2 (7 lines); hunks: -17,9 +17,12
  - `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +6/-1 (7 lines); hunks: -16,7 +16,6; -33,6 +32,7; symbols: _as_dict, has_audio_track
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/mimo_audio.py
@@ -17,9 +17,12 @@
-except ImportError:
+except (ImportError, OSError, RuntimeError) as e:
+    # TorchCodec may be installed but unable to load its FFmpeg libraries.
-        "torchcodec is not installed; audio inputs will fail at request time"
+        "torchcodec is unavailable; video audio-track detection and "
+        "audio decoding via AudioDecoder are disabled: %s",
diff -- python/sglang/srt/multimodal/processors/mimo_v2.py
@@ -16,7 +16,6 @@
-from torchcodec.decoders import AudioDecoder
@@ -33,6 +32,7 @@
+    AudioDecoder,
@@ -452,6 +452,11 @@ def _as_dict(obj):
+        if AudioDecoder is None:
+            raise ValueError(
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/mimo_audio.py` modified +5/-2; `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +6/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41886 - [Perf] Use FA4 by default for MiMo on SM100

- Link: https://github.com/sgl-project/sglang/pull/41886
- Status/date: merged / 2026-10-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`; associated commits `a702970ecbb7`
- Diff scope read: GitHub Pull Request files API returned 2 files, +32/-6, 74 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Use FA4 by default for MiMo on SM100"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`; technical summary: Covers "[Perf] Use FA4 by default for MiMo on SM100"; the main implementation surface is `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +5/-0 (5 lines); hunks: -5,6 +5,7; -22,6 +23,10 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) -> d...; symbols: _mimo_v2_overrides, touching `_mimo_v2_overrides`.
- Code diff details:
  - `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +5/-0 (5 lines); hunks: -5,6 +5,7; -22,6 +23,10 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) -> d...; symbols: _mimo_v2_overrides
- Key code excerpts:

```diff
diff -- python/sglang/srt/arg_groups/model_overrides/mimo_v2.py
@@ -5,6 +5,7 @@
+    is_attention_backend_not_set,
@@ -22,6 +23,10 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) -> dict:
+    if get_platform().is_sm100 and is_attention_backend_not_set(cfg):
+        overrides["attention_backend"] = "fa4"
+        logger.info("MiMoV2 on SM100: attention_backend=fa4.")
```

- Reviewed files:
  - runtime: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +5/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/test_model_overrides.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41668 - [Fix] Select the MXFP4 MoE runner for MiMo-V2 packed experts on SM100

- Link: https://github.com/sgl-project/sglang/pull/41668
- Status/date: merged / 2026-10-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`; associated commits `80bb3fb6511a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +45/-4, 80 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Select the MXFP4 MoE runner for MiMo-V2 packed experts on SM100"; model line: MiMo V2 Flash; category: bug fix; main diff: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`; technical summary: Covers "[Fix] Select the MXFP4 MoE runner for MiMo-V2 packed experts on SM100"; the main implementation surface is `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +15/-4 (19 lines); hunks: -6,6 +6,7; -27,13 +28,23 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) ->...; symbols: _mimo_v2_overrides, touching `_mimo_v2_overrides`.
- Code diff details:
  - `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +15/-4 (19 lines); hunks: -6,6 +6,7; -27,13 +28,23 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) ->...; symbols: _mimo_v2_overrides
- Key code excerpts:

```diff
diff -- python/sglang/srt/arg_groups/model_overrides/mimo_v2.py
@@ -6,6 +6,7 @@
+    model_config_of,
@@ -27,13 +28,23 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) -> dict:
-    # On Blackwell "auto" falls through to the triton fused-MoE runner, ~12%
-    # slower at bs=1 decode. FP4 checkpoints use flashinfer_mxfp4 instead.
+    # Mixed checkpoints also advertise quant_method=fp8; select the runner
+    # using the routed-expert layout already resolved by ModelConfig.
```

- Reviewed files:
  - runtime: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +15/-4
- Risk and verification: The diff ships test coverage in `test/registered/unit/test_model_overrides.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #42172 - [Fix] Select the Marlin MoE runner for MiMo-V2 packed MXFP4 experts on SM90

- Link: https://github.com/sgl-project/sglang/pull/42172
- Status/date: merged / 2026-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`; associated commits `6be84e1b72df`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-0, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Select the Marlin MoE runner for MiMo-V2 packed MXFP4 experts on SM90"; model line: MiMo V2 Flash; category: bug fix; main diff: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`; technical summary: Covers "[Fix] Select the Marlin MoE runner for MiMo-V2 packed MXFP4 experts on SM90"; the main implementation surface is `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +9/-0 (9 lines); hunks: -47,4 +47,13 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) -> d...; symbols: _mimo_v2_overrides, touching `_mimo_v2_overrides`.
- Code diff details:
  - `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +9/-0 (9 lines); hunks: -47,4 +47,13 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) -> d...; symbols: _mimo_v2_overrides
- Key code excerpts:

```diff
diff -- python/sglang/srt/arg_groups/model_overrides/mimo_v2.py
@@ -47,4 +47,13 @@ def _mimo_v2_overrides(server_args: Any, hf_config: Any) -> dict:
+    elif (
+        get_platform().is_sm90
+        and cfg.moe_runner_backend == "auto"
+        and get_quantization_config(hf_config) == "fp8"
+        and model_config_of(server_args).is_fp4_experts
+    ):
```

- Reviewed files:
  - runtime: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py` modified +9/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #42101 - [Perf] Optimize MiMo local audio attention on Hopper

- Link: https://github.com/sgl-project/sglang/pull/42101
- Status/date: merged / 2026-10-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/mimo_local_attention.py`, `python/sglang/srt/models/mimo_audio.py`; associated commits `abd6c374c71c`
- Diff scope read: GitHub Pull Request files API returned 2 files, +181/-0, 209 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Optimize MiMo local audio attention on Hopper"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/models/mimo_audio.py`, `python/sglang/kernels/ops/attention/mimo_local_attention.py`; technical summary: Covers "[Perf] Optimize MiMo local audio attention on Hopper"; the main implementation surface is `python/sglang/srt/models/mimo_audio.py`, `python/sglang/kernels/ops/attention/mimo_local_attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_audio.py` modified +66/-0 (66 lines); hunks: -14,8 +14,13; -26,10 +31,58; symbols: _mimo_local_attention_forward, _compute_default_rope_parameters, build_audio_encoder, touching `_mimo_local_attention_forward, _compute_default_rope_parameters, build_audio_encoder`; `python/sglang/kernels/ops/attention/mimo_local_attention.py` added +115/-0 (115 lines); hunks: -0,0 +1,115; symbols: _mimo_local_attention_kernel, mimo_local_attention, touching `_mimo_local_attention_kernel, mimo_local_attention`.
- Code diff details:
  - `python/sglang/srt/models/mimo_audio.py` modified +66/-0 (66 lines); hunks: -14,8 +14,13; -26,10 +31,58; symbols: _mimo_local_attention_forward, _compute_default_rope_parameters, build_audio_encoder
  - `python/sglang/kernels/ops/attention/mimo_local_attention.py` added +115/-0 (115 lines); hunks: -0,0 +1,115; symbols: _mimo_local_attention_kernel, mimo_local_attention
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_audio.py
@@ -14,8 +14,13 @@
+from transformers import AttentionInterface
+from transformers.masking_utils import (
+    ALL_MASK_ATTENTION_FUNCTIONS,
+    AttentionMaskInterface,
+)
@@ -26,10 +31,58 @@
diff -- python/sglang/kernels/ops/attention/mimo_local_attention.py
@@ -0,0 +1,115 @@
+"""Attention for MiMo's independent groups of at most four audio tokens."""
+import torch
+import triton
+import triton.language as tl
+@triton.jit
+def _mimo_local_attention_kernel(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_audio.py` modified +66/-0; `python/sglang/kernels/ops/attention/mimo_local_attention.py` added +115/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/ops/attention/mimo_local_attention.py`, `python/sglang/srt/models/mimo_audio.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #40888 - fix(mimo-vl): keep multimodal features when capturing aux hidden states, and correct vision preprocessing

- Link: https://github.com/sgl-project/sglang/pull/40888
- Status/date: merged / 2026-10-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_vl.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`; associated commits `679d2851ba28`
- Diff scope read: GitHub Pull Request files API returned 3 files, +27/-14, 82 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(mimo-vl): keep multimodal features when capturing aux hidden states, and correct vision preprocessing"; model line: MiMo V2 Flash; category: bug fix; main diff: `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_vl.py`; technical summary: Covers "fix(mimo-vl): keep multimodal features when capturing aux hidden states, and correct vision preprocessing"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/models/mimo_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +10/-11 (21 lines); hunks: -1326,16 +1326,11 @@ def forward(; -1344,13 +1339,17 @@ def forward(; symbols: forward, touching `forward`; `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +10/-2 (12 lines); hunks: -214,8 +214,16 @@ def __post_init__(self):; symbols: __post_init__, touching `__post_init__`; `python/sglang/srt/models/mimo_vl.py` modified +7/-1 (8 lines); hunks: -318,6 +318,10 @@ def __init__(; -328,7 +332,9 @@ def apply_index(self, tensor: torch.Tensor, index: torch.Ten...; symbols: __init__, apply_index, _post_init, get_window_index_1d, touching `__init__, apply_index, _post_init`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +10/-11 (21 lines); hunks: -1326,16 +1326,11 @@ def forward(; -1344,13 +1339,17 @@ def forward(; symbols: forward
  - `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +10/-2 (12 lines); hunks: -214,8 +214,16 @@ def __post_init__(self):; symbols: __post_init__
  - `python/sglang/srt/models/mimo_vl.py` modified +7/-1 (8 lines); hunks: -318,6 +318,10 @@ def __init__(; -328,7 +332,9 @@ def apply_index(self, tensor: torch.Tensor, index: torch.Ten...; symbols: __init__, apply_index, _post_init, get_window_index_1d
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -1326,16 +1326,11 @@ def forward(
-        if self.capture_aux_hidden_states:
-            hidden_states, hidden_states_before_norm, aux_hidden_states = self.model(
-                input_ids,
-                positions,
-                forward_batch,
-                input_embeds,
diff -- python/sglang/srt/multimodal/processors/mimo_v2.py
@@ -214,8 +214,16 @@ def __post_init__(self):
-_QWEN2VL_PIXEL_MEAN = torch.Tensor([123.675, 116.28, 103.53]).view(-1, 1, 1)
-_QWEN2VL_PIXEL_STD = torch.Tensor([58.395, 57.12, 57.375]).view(-1, 1, 1)
+# OPENAI_CLIP stats, matching Qwen2VLImageProcessor (preprocessor_config.json
+# image_mean/image_std with do_rescale 1/255). Kept in 0-255 space because
+# standardize_batch sees un-rescaled PIL tensors. ImageNet values were wrong
+# for MiMo-VL and scrambled colors.
diff -- python/sglang/srt/models/mimo_vl.py
@@ -318,6 +318,10 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +10/-11; `python/sglang/srt/multimodal/processors/mimo_v2.py` modified +10/-2; `python/sglang/srt/models/mimo_vl.py` modified +7/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_vl.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #43639 - [Perf] Enable native MXFP4 routing and CuTeDSL fusion for MiMo

- Link: https://github.com/sgl-project/sglang/pull/43639
- Status/date: merged / 2026-10-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`; associated commits `c54ba66cd40f`
- Diff scope read: GitHub Pull Request files API returned 8 files, +203/-48, 567 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Enable native MXFP4 routing and CuTeDSL fusion for MiMo"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "[Perf] Enable native MXFP4 routing and CuTeDSL fusion for MiMo"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +99/-10 (109 lines); hunks: -26,6 +26,7; -37,12 +38,18; symbols: __init__, forward, forward_normal, touching `__init__, forward, forward_normal`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +99/-10 (109 lines); hunks: -26,6 +26,7; -37,12 +38,18; symbols: __init__, forward, forward_normal
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -26,6 +26,7 @@
+from sglang.srt.environ import envs
@@ -37,12 +38,18 @@
+from sglang.srt.layers.flashinfer_comm_fusion import uses_cutedsl_ar_fusion
+from sglang.srt.layers.layer_boundary.fusions.cutedsl import (
+    CuteDSLFusion,
+    MoeDeferredFinalize,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +99/-10
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/ops/moe/smallm_router_gfx950/__init__.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/overrides.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #43106 - Fuse MiMo verification RoPE and KV cache writes

- Link: https://github.com/sgl-project/sglang/pull/43106
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`; associated commits `93dbe88183df`
- Diff scope read: GitHub Pull Request files API returned 7 files, +283/-0, 358 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fuse MiMo verification RoPE and KV cache writes"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "Fuse MiMo verification RoPE and KV cache writes"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +30/-0 (30 lines); hunks: -78,6 +78,7; -801,13 +802,42 @@ def forward_core(self, intermediate_state):; symbols: forward_core, _forward_rope_store, forward, touching `forward_core, _forward_rope_store, forward`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +30/-0 (30 lines); hunks: -78,6 +78,7; -801,13 +802,42 @@ def forward_core(self, intermediate_state):; symbols: forward_core, _forward_rope_store, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -78,6 +78,7 @@
+from sglang.srt.layers.rotary_embedding.base import RotaryEmbedding
@@ -801,13 +802,42 @@ def forward_core(self, intermediate_state):
+    def _forward_rope_store(self, qkv, positions, forward_batch):
+        from sglang.srt.model_executor.forward_context import get_attn_backend
+        query = self.rotary_emb.try_bf16_rope_store(
+            qkv,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +30/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/jit/csrc/elementwise/pos_enc.cuh`, `python/sglang/kernels/ops/attention/rope.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #40890 - [Perf] [NPU] mimo: fold attention_value_scale into o_proj weights

- Link: https://github.com/sgl-project/sglang/pull/40890
- Status/date: merged / 2026-10-31
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`; associated commits `c7290006d1db`
- Diff scope read: GitHub Pull Request files API returned 2 files, +53/-4, 99 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] [NPU] mimo: fold attention_value_scale into o_proj weights"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "[Perf] [NPU] mimo: fold attention_value_scale into o_proj weights"; the main implementation surface is `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/mimo_v2.py` modified +46/-3 (49 lines); hunks: -708,6 +708,9 @@ def __init__(; -785,7 +788,7 @@ def forward_prepare(; symbols: __init__, forward_prepare, _forward_rope_store, forward, touching `__init__, forward_prepare, _forward_rope_store`.
- Code diff details:
  - `python/sglang/srt/models/mimo_v2.py` modified +46/-3 (49 lines); hunks: -708,6 +708,9 @@ def __init__(; -785,7 +788,7 @@ def forward_prepare(; symbols: __init__, forward_prepare, _forward_rope_store, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/mimo_v2.py
@@ -708,6 +708,9 @@ def __init__(
+        # Set once attention_value_scale has been folded into o_proj weights,
+        # disabling the runtime V multiply (see _fold_attention_value_scale_into_o_proj).
+        self.v_scale_folded = False
@@ -785,7 +788,7 @@ def forward_prepare(
-        if self.v_scale is not None:
+        if self.v_scale is not None and not self.v_scale_folded:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +46/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/mimo_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41108 - [Perf] mimo-v2: Optimize router GEMM with the HPC-Ops bf16xfp32 kernel

- Link: https://github.com/sgl-project/sglang/pull/41108
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/mimo_v2.py`, `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py`; associated commits `fe6a8a32fd2d`
- Diff scope read: GitHub Pull Request files API returned 4 files, +121/-6, 179 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] mimo-v2: Optimize router GEMM with the HPC-Ops bf16xfp32 kernel"; model line: MiMo V2 Flash; category: performance/backend optimization; main diff: `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py`, `python/sglang/srt/models/mimo_v2.py`; technical summary: Covers "[Perf] mimo-v2: Optimize router GEMM with the HPC-Ops bf16xfp32 kernel"; the main implementation surface is `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py`, `python/sglang/srt/models/mimo_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py` added +84/-0 (84 lines); hunks: -0,0 +1,84; symbols: _mimo_config, TestMiMoV2RouterHpcGemm, _make_gate, test_benchmarked_shape_dispatches_with_min_m, touching `_mimo_config, TestMiMoV2RouterHpcGemm, _make_gate`; `python/sglang/srt/models/mimo_v2.py` modified +27/-0 (27 lines); hunks: -23,6 +23,7; -116,6 +117,18; symbols: load_mimo_v2_qkv_proj_weight, __init__, forward, touching `load_mimo_v2_qkv_proj_weight, __init__, forward`.
- Code diff details:
  - `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py` added +84/-0 (84 lines); hunks: -0,0 +1,84; symbols: _mimo_config, TestMiMoV2RouterHpcGemm, _make_gate, test_benchmarked_shape_dispatches_with_min_m
  - `python/sglang/srt/models/mimo_v2.py` modified +27/-0 (27 lines); hunks: -23,6 +23,7; -116,6 +117,18; symbols: load_mimo_v2_qkv_proj_weight, __init__, forward
- Key code excerpts:

```diff
diff -- test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py
@@ -0,0 +1,84 @@
+"""Unit tests for MiMo-V2 router GEMM dispatch to the HPC-Ops bf16xfp32 kernel."""
+import unittest
+from types import SimpleNamespace
+from unittest.mock import patch
+import torch
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/models/mimo_v2.py
@@ -23,6 +23,7 @@
+from sglang.kernels.ops.gemm.bf16_fp32 import linear_bf16_fp32
@@ -116,6 +117,18 @@
+# Minimum m (num_tokens) from which the HPC-Ops bf16xfp32 router GEMM is at
+# least as fast as cublas, benchmarked per router shape
+# (hidden_size, n_routed_experts) on H100; below it the dispatcher falls back.
+# Opt-in via SGLANG_OPT_BF16_FP32_GEMM_ALGO=hpc, for two reasons: the split
```

- Reviewed files:
  - tests: `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py` added +84/-0
  - runtime: `python/sglang/srt/models/mimo_v2.py` modified +27/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/benchmark/gemm/bench_bf16xfp32_router_gemm.py`, `test/registered/kernels/ops/gemm/test_linear_bf16_fp32_hpc.py`, `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
