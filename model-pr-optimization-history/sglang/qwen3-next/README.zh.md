# sglang Qwen3 Next 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/qwen3_next_80b_a3b_instruct.mdx` | 无直接 PR 号提交 |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/qwen3_next_80b_a3b_instruct.mdx` | 无直接 PR 号提交 |
| `python/sglang/srt/configs/qwen3_next.py` | [#10233](https://github.com/sgl-project/sglang/pull/10233), [#11585](https://github.com/sgl-project/sglang/pull/11585), [#12525](https://github.com/sgl-project/sglang/pull/12525) |
| `python/sglang/srt/models/qwen3_next.py` | [#10233](https://github.com/sgl-project/sglang/pull/10233), [#10322](https://github.com/sgl-project/sglang/pull/10322), [#10379](https://github.com/sgl-project/sglang/pull/10379), [#10622](https://github.com/sgl-project/sglang/pull/10622), [#11969](https://github.com/sgl-project/sglang/pull/11969), [#12525](https://github.com/sgl-project/sglang/pull/12525), [#13081](https://github.com/sgl-project/sglang/pull/13081), [#14607](https://github.com/sgl-project/sglang/pull/14607), [#16164](https://github.com/sgl-project/sglang/pull/16164), [#17016](https://github.com/sgl-project/sglang/pull/17016), [#17373](https://github.com/sgl-project/sglang/pull/17373), [#17613](https://github.com/sgl-project/sglang/pull/17613), ... (24 total) |
| `python/sglang/srt/models/qwen3_next_mtp.py` | [#10233](https://github.com/sgl-project/sglang/pull/10233), [#10322](https://github.com/sgl-project/sglang/pull/10322), [#10392](https://github.com/sgl-project/sglang/pull/10392), [#26204](https://github.com/sgl-project/sglang/pull/26204) |
| `test/manual/4-gpu-models/test_qwen3_next_models.py` | 无直接 PR 号提交 |
| `test/manual/4-gpu-models/test_qwen3_next_models_mtp_archived.py` | 无直接 PR 号提交 |
| `test/registered/attention/test_qwen3_next_deterministic.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_qwen3_next_models.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_qwen3_next_models_extra.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_qwen3_next_models_mtp.py` | 无直接 PR 号提交 |
| `test/registered/npu/accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py` | 无直接 PR 号提交 |
| `test/registered/npu/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_next.py` | 无直接 PR 号提交 |
| `test/registered/npu/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_next.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 26
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 26
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #10233 - Qwen3-Next support

- 链接: https://github.com/sgl-project/sglang/pull/10233
- 状态/时间: merged / 2025-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`；关联提交 `30c6e1f56967`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 19 个文件，+3224/-8，可读 patch 3452 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Qwen3-Next support」；模型线: Qwen3 Next；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`；技术摘要: 覆盖「Qwen3-Next support」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` added +1072/-0 (1072 lines); hunks: -0,0 +1,1072; symbols: fused_qkvzba_split_reshape_cat_kernel, fused_qkvzba_split_reshape_cat, fused_gdn_gating_kernel, fused_gdn_gating，涉及 `fused_qkvzba_split_reshape_cat_kernel, fused_qkvzba_split_reshape_cat, fused_gdn_gating_kernel`；`python/sglang/srt/configs/qwen3_next.py` added +326/-0 (326 lines); hunks: -0,0 +1,326; symbols: HybridLayerType, Qwen3NextConfig, to, __init__，涉及 `HybridLayerType, Qwen3NextConfig, to`；`python/sglang/srt/models/qwen3_next_mtp.py` added +117/-0 (117 lines); hunks: -0,0 +1,117; symbols: Qwen3NextForCausalLMMTP, __init__, forward, load_weights，涉及 `Qwen3NextForCausalLMMTP, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` added +1072/-0 (1072 lines); hunks: -0,0 +1,1072; symbols: fused_qkvzba_split_reshape_cat_kernel, fused_qkvzba_split_reshape_cat, fused_gdn_gating_kernel, fused_gdn_gating
  - `python/sglang/srt/configs/qwen3_next.py` added +326/-0 (326 lines); hunks: -0,0 +1,326; symbols: HybridLayerType, Qwen3NextConfig, to, __init__
  - `python/sglang/srt/models/qwen3_next_mtp.py` added +117/-0 (117 lines); hunks: -0,0 +1,117; symbols: Qwen3NextForCausalLMMTP, __init__, forward, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` added +1072/-0; `python/sglang/srt/configs/qwen3_next.py` added +326/-0; `python/sglang/srt/models/qwen3_next_mtp.py` added +117/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10322 - [bugfix] fix norm type error in qwen3_next model

- 链接: https://github.com/sgl-project/sglang/pull/10322
- 状态/时间: merged / 2025-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`；关联提交 `4a0e0be2a2b4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+10/-51，可读 patch 89 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[bugfix] fix norm type error in qwen3_next model」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`；技术摘要: 覆盖「[bugfix] fix norm type error in qwen3_next model」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +9/-42 (51 lines); hunks: -518,24 +518,10 @@ def __init__(; -685,23 +671,10 @@ def __init__(; symbols: __init__, get_layer, forward，涉及 `__init__, get_layer, forward`；`python/sglang/srt/models/qwen3_next_mtp.py` modified +1/-9 (10 lines); hunks: -54,15 +54,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +9/-42 (51 lines); hunks: -518,24 +518,10 @@ def __init__(; -685,23 +671,10 @@ def __init__(; symbols: __init__, get_layer, forward
  - `python/sglang/srt/models/qwen3_next_mtp.py` modified +1/-9 (10 lines); hunks: -54,15 +54,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +9/-42; `python/sglang/srt/models/qwen3_next_mtp.py` modified +1/-9
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10379 - Support Qwen3-Next on Ascend NPU

- 链接: https://github.com/sgl-project/sglang/pull/10379
- 状态/时间: merged / 2025-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `16cd550c8554`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+79/-26，可读 patch 281 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support Qwen3-Next on Ascend NPU」；模型线: Qwen3 Next；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「Support Qwen3-Next on Ascend NPU」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +6/-3 (9 lines); hunks: -46,10 +46,11; -327,7 +328,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, forward，涉及 `__init__, fix_query_key_value_ordering, _forward_input_proj`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +6/-3 (9 lines); hunks: -46,10 +46,11; -327,7 +328,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +6/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10392 - [Fix] Support qwen3-next MTP+DP

- 链接: https://github.com/sgl-project/sglang/pull/10392
- 状态/时间: merged / 2025-09-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next_mtp.py`；关联提交 `9752861002d7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+29/-18，可读 patch 120 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Support qwen3-next MTP+DP」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next_mtp.py`；技术摘要: 覆盖「[Fix] Support qwen3-next MTP+DP」；主要实现面是 `python/sglang/srt/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next_mtp.py` modified +5/-2 (7 lines); hunks: -85,8 +85,11 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next_mtp.py` modified +5/-2 (7 lines); hunks: -85,8 +85,11 @@ def forward(; symbols: forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next_mtp.py` modified +5/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/mem_cache/memory_pool.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10622 - support qwen3-next-fp8 deepep

- 链接: https://github.com/sgl-project/sglang/pull/10622
- 状态/时间: merged / 2025-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `1344ebc8333d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+93/-9，可读 patch 204 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support qwen3-next-fp8 deepep」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「support qwen3-next-fp8 deepep」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +29/-8 (37 lines); hunks: -13,6 +13,7; -46,7 +47,14; symbols: forward, __init__, routed_experts_weights_of_layer，涉及 `forward, __init__, routed_experts_weights_of_layer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +29/-8 (37 lines); hunks: -13,6 +13,7; -46,7 +47,14; symbols: forward, __init__, routed_experts_weights_of_layer
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +29/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #11585 - Clean up some Qwen3-Next and deterministic code

- 链接: https://github.com/sgl-project/sglang/pull/11585
- 状态/时间: merged / 2025-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/qwen3_next.py`；关联提交 `6b143d62a297`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+1/-15，可读 patch 47 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Clean up some Qwen3-Next and deterministic code」；模型线: Qwen3 Next；类别: 模型实现调整；主要 diff: `python/sglang/srt/configs/qwen3_next.py`；技术摘要: 覆盖「Clean up some Qwen3-Next and deterministic code」；主要实现面是 `python/sglang/srt/configs/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/configs/qwen3_next.py` modified +0/-3 (3 lines); hunks: -27,12 +27,9; symbols: HybridLayerType, Qwen3NextConfig，涉及 `HybridLayerType, Qwen3NextConfig`。
- 代码 diff 细节:
  - `python/sglang/srt/configs/qwen3_next.py` modified +0/-3 (3 lines); hunks: -27,12 +27,9; symbols: HybridLayerType, Qwen3NextConfig
- 关键代码摘录:

```diff
diff -- python/sglang/srt/configs/qwen3_next.py
@@ -27,12 +27,9 @@
-# NOTE: HybridLayerType
-    swa_attention = "swa_attention"
-    mamba2 = "mamba"
```

- 已读文件:
  - runtime: `python/sglang/srt/configs/qwen3_next.py` modified +0/-3
- 验证与风险: diff 自带测试面 `python/sglang/test/test_deterministic.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #11969 - [NPU] bugfix for Qwen3-Next and performance update

- 链接: https://github.com/sgl-project/sglang/pull/11969
- 状态/时间: merged / 2025-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `cafebef1546e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+68/-21，可读 patch 162 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] bugfix for Qwen3-Next and performance update」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[NPU] bugfix for Qwen3-Next and performance update」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -478,6 +478,13 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -478,6 +478,13 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -478,6 +478,13 @@ def forward(
+        # Add padding for DP-Attn
+        if is_dp_attention_enabled():
+            core_attn_out_pad = torch.zeros_like(z)
+            core_attn_out_pad[: core_attn_out.shape[0], :] = core_attn_out
+            core_attn_out = core_attn_out_pad
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/moe/topk.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13081 - Support piecewise cuda graph for Qwen3-next

- 链接: https://github.com/sgl-project/sglang/pull/13081
- 状态/时间: merged / 2025-11-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `d64bf6c6ce70`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+112/-3，可读 patch 191 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support piecewise cuda graph for Qwen3-next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「Support piecewise cuda graph for Qwen3-next」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +62/-1 (63 lines); hunks: -5,6 +5,7; -53,9 +54,13; symbols: fused_qkvzba_split_reshape_cat_kernel, fix_query_key_value_ordering, _forward_input_proj, forward，涉及 `fused_qkvzba_split_reshape_cat_kernel, fix_query_key_value_ordering, _forward_input_proj`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +62/-1 (63 lines); hunks: -5,6 +5,7; -53,9 +54,13; symbols: fused_qkvzba_split_reshape_cat_kernel, fix_query_key_value_ordering, _forward_input_proj, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +62/-1
- 验证与风险: diff 自带测试面 `test/srt/models/test_qwen3_next_models.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #16164 - [NPU] Adapt qwen3-next W8A8 on NPU

- 链接: https://github.com/sgl-project/sglang/pull/16164
- 状态/时间: merged / 2026-01-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `6bc5a52fd2d4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+18/-5，可读 patch 121 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Adapt qwen3-next W8A8 on NPU」；模型线: Qwen3 Next；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[NPU] Adapt qwen3-next W8A8 on NPU」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +18/-5 (23 lines); hunks: -202,6 +202,7 @@ def __init__(; -229,6 +230,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering，涉及 `__init__, fix_query_key_value_ordering`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +18/-5 (23 lines); hunks: -202,6 +202,7 @@ def __init__(; -229,6 +230,7 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +18/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17016 - [bugfix] fix qwen3-next alt_stream none issue

- 链接: https://github.com/sgl-project/sglang/pull/17016
- 状态/时间: merged / 2026-01-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `6f10e17b4a68`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[bugfix] fix qwen3-next alt_stream none issue」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[bugfix] fix qwen3-next alt_stream none issue」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +5/-1 (6 lines); hunks: -358,7 +358,11 @@ def _forward_input_proj(self, hidden_states: torch.Tensor):; symbols: _forward_input_proj，涉及 `_forward_input_proj`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +5/-1 (6 lines); hunks: -358,7 +358,11 @@ def _forward_input_proj(self, hidden_states: torch.Tensor):; symbols: _forward_input_proj
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17373 - refactor Qwen3-Next with a new RadixLinearAttention

- 链接: https://github.com/sgl-project/sglang/pull/17373
- 状态/时间: merged / 2026-01-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `419bbcee10a5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+200/-106，可读 patch 444 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「refactor Qwen3-Next with a new RadixLinearAttention」；模型线: Qwen3 Next；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「refactor Qwen3-Next with a new RadixLinearAttention」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +21/-37 (58 lines); hunks: -29,6 +29,7; -60,8 +61,6; symbols: fused_qkvzba_split_reshape_cat_kernel, __init__, fix_query_key_value_ordering, forward，涉及 `fused_qkvzba_split_reshape_cat_kernel, __init__, fix_query_key_value_ordering`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +21/-37 (58 lines); hunks: -29,6 +29,7; -60,8 +61,6; symbols: fused_qkvzba_split_reshape_cat_kernel, __init__, fix_query_key_value_ordering, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +21/-37
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #12525 - [CPU] Optimize Qwen3-next model on CPU

- 链接: https://github.com/sgl-project/sglang/pull/12525
- 状态/时间: merged / 2026-01-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_next.py`；关联提交 `336dc4579e94`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+366/-41，可读 patch 685 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CPU] Optimize Qwen3-next model on CPU」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`；技术摘要: 覆盖「[CPU] Optimize Qwen3-next model on CPU」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/configs/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +31/-5 (36 lines); hunks: -46,6 +46,8; -56,6 +58,8; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, _forward，涉及 `__init__, fix_query_key_value_ordering, _forward_input_proj`；`python/sglang/srt/configs/qwen3_next.py` modified +7/-0 (7 lines); hunks: -20,8 +20,11; -276,6 +279,10 @@ def full_attention_layer_ids(self):; symbols: HybridLayerType, full_attention_layer_ids, mamba2_cache_params，涉及 `HybridLayerType, full_attention_layer_ids, mamba2_cache_params`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +31/-5 (36 lines); hunks: -46,6 +46,8; -56,6 +58,8; symbols: __init__, fix_query_key_value_ordering, _forward_input_proj, _forward
  - `python/sglang/srt/configs/qwen3_next.py` modified +7/-0 (7 lines); hunks: -20,8 +20,11; -276,6 +279,10 @@ def full_attention_layer_ids(self):; symbols: HybridLayerType, full_attention_layer_ids, mamba2_cache_params
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +31/-5; `python/sglang/srt/configs/qwen3_next.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/layers/amx_utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14607 - support qwen3-next eagle3

- 链接: https://github.com/sgl-project/sglang/pull/14607
- 状态/时间: merged / 2026-02-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `3ca29dffc72a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+73/-6，可读 patch 156 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support qwen3-next eagle3」；模型线: Qwen3 Next；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「support qwen3-next eagle3」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +73/-6 (79 lines); hunks: -531,12 +531,18 @@ def forward(; -753,10 +759,16 @@ def forward(; symbols: forward, get_layer, set_eagle3_layers_to_capture，涉及 `forward, get_layer, set_eagle3_layers_to_capture`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +73/-6 (79 lines); hunks: -531,12 +531,18 @@ def forward(; -753,10 +759,16 @@ def forward(; symbols: forward, get_layer, set_eagle3_layers_to_capture
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +73/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17613 - [Perf] refactor piecewise cuda graph support of Qwen3-Next

- 链接: https://github.com/sgl-project/sglang/pull/17613
- 状态/时间: merged / 2026-02-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `8be18c655d0f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+80/-34，可读 patch 196 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] refactor piecewise cuda graph support of Qwen3-Next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[Perf] refactor piecewise cuda graph support of Qwen3-Next」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +2/-19 (21 lines); hunks: -316,7 +316,7 @@ def __init__(; -405,23 +405,6 @@ def forward(; symbols: __init__, forward, _forward，涉及 `__init__, forward, _forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +2/-19 (21 lines); hunks: -316,7 +316,7 @@ def __init__(; -405,23 +405,6 @@ def forward(; symbols: __init__, forward, _forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +2/-19
- 验证与风险: diff 自带测试面 `test/registered/models/test_qwen3_next_models_pcg.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #18917 - [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill

- 链接: https://github.com/sgl-project/sglang/pull/18917
- 状态/时间: merged / 2026-02-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `5995bfec6368`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-7，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +1/-7 (8 lines); hunks: -405,17 +405,11 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +1/-7 (8 lines); hunks: -405,17 +405,11 @@ def forward(; symbols: forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +1/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19434 - [Qwen3-Next] Support gdn fused_rms_norm_gated

- 链接: https://github.com/sgl-project/sglang/pull/19434
- 状态/时间: merged / 2026-02-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `d2885a9094c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+411/-299，可读 patch 758 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3-Next] Support gdn fused_rms_norm_gated」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[Qwen3-Next] Support gdn fused_rms_norm_gated」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +20/-8 (28 lines); hunks: -53,6 +53,9; -291,14 +294,23 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +20/-8 (28 lines); hunks: -53,6 +53,9; -291,14 +294,23 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +20/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17627 - [feat] Support nvfp4 quantized model of Qwen3-Next

- 链接: https://github.com/sgl-project/sglang/pull/17627
- 状态/时间: merged / 2026-02-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `a2ea5941d562`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+83/-1，可读 patch 105 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[feat] Support nvfp4 quantized model of Qwen3-Next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[feat] Support nvfp4 quantized model of Qwen3-Next」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +12/-1 (13 lines); hunks: -625,13 +625,19 @@ def __init__(; -1123,6 +1129,11 @@ def load_weights(; symbols: __init__, load_weights，涉及 `__init__, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +12/-1 (13 lines); hunks: -625,13 +625,19 @@ def __init__(; -1123,6 +1129,11 @@ def load_weights(; symbols: __init__, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +12/-1
- 验证与风险: diff 自带测试面 `test/registered/models/test_qwen3_next_models_fp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #19321 - [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj

- 链接: https://github.com/sgl-project/sglang/pull/19321
- 状态/时间: merged / 2026-03-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `d9794ef9f760`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+107/-17，可读 patch 207 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +83/-11 (94 lines); hunks: -20,6 +20,7; -245,28 +246,38 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _make_packed_weight_loader, weight_loader，涉及 `__init__, fix_query_key_value_ordering, _make_packed_weight_loader`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +83/-11 (94 lines); hunks: -20,6 +20,7; -245,28 +246,38 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, _make_packed_weight_loader, weight_loader
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +83/-11
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21313 - bugfix for weight loading for qwen3-next

- 链接: https://github.com/sgl-project/sglang/pull/21313
- 状态/时间: merged / 2026-03-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `0906e45cec97`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「bugfix for weight loading for qwen3-next」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「bugfix for weight loading for qwen3-next」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -135,10 +135,10 @@ def __init__(
-        self.in_proj_qkvz.weight.weight_loader = self._make_packed_weight_loader(
+        self.in_proj_qkvz.weight._weight_loader = self._make_packed_weight_loader(
-        self.in_proj_ba.weight.weight_loader = self._make_packed_weight_loader(
+        self.in_proj_ba.weight._weight_loader = self._make_packed_weight_loader(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21496 - Revert "bugfix for weight loading for qwen3-next"

- 链接: https://github.com/sgl-project/sglang/pull/21496
- 状态/时间: merged / 2026-03-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `a93065679b63`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "bugfix for weight loading for qwen3-next"」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「Revert "bugfix for weight loading for qwen3-next"」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -135,10 +135,10 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_next.py
@@ -135,10 +135,10 @@ def __init__(
-        self.in_proj_qkvz.weight._weight_loader = self._make_packed_weight_loader(
+        self.in_proj_qkvz.weight.weight_loader = self._make_packed_weight_loader(
-        self.in_proj_ba.weight._weight_loader = self._make_packed_weight_loader(
+        self.in_proj_ba.weight.weight_loader = self._make_packed_weight_loader(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21662 - [Fix] Fix weight_loader property assignment for qwen3-next FP8 models

- 链接: https://github.com/sgl-project/sglang/pull/21662
- 状态/时间: merged / 2026-03-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `62a63eeff76d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+17/-4，可读 patch 36 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Fix weight_loader property assignment for qwen3-next FP8 models」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[Fix] Fix weight_loader property assignment for qwen3-next FP8 models」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +17/-4 (21 lines); hunks: -135,11 +135,11 @@ def __init__(; -216,6 +216,19 @@ def __init__(; symbols: __init__, _override_weight_loader, _make_packed_weight_loader，涉及 `__init__, _override_weight_loader, _make_packed_weight_loader`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +17/-4 (21 lines); hunks: -135,11 +135,11 @@ def __init__(; -216,6 +216,19 @@ def __init__(; symbols: __init__, _override_weight_loader, _make_packed_weight_loader
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +17/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21698 - [npu]fix: qwen3-next w8a8 precision bugs

- 链接: https://github.com/sgl-project/sglang/pull/21698
- 状态/时间: merged / 2026-04-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `f2b84b90ac86`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+22/-5，可读 patch 41 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[npu]fix: qwen3-next w8a8 precision bugs」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[npu]fix: qwen3-next w8a8 precision bugs」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +22/-5 (27 lines); hunks: -65,6 +65,14; -223,11 +231,20 @@ def _override_weight_loader(module, new_loader):; symbols: Qwen3GatedDeltaNet, __init__, _override_weight_loader, _make_packed_weight_loader，涉及 `Qwen3GatedDeltaNet, __init__, _override_weight_loader`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +22/-5 (27 lines); hunks: -65,6 +65,14; -223,11 +231,20 @@ def _override_weight_loader(module, new_loader):; symbols: Qwen3GatedDeltaNet, __init__, _override_weight_loader, _make_packed_weight_loader
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +22/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23619 - Enable Qwen3-Next MoE all-reduce fusion

- 链接: https://github.com/sgl-project/sglang/pull/23619
- 状态/时间: merged / 2026-04-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `13afe8acdff3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+46/-23，可读 patch 90 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable Qwen3-Next MoE all-reduce fusion」；模型线: Qwen3 Next；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「Enable Qwen3-Next MoE all-reduce fusion」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +46/-23 (69 lines); hunks: -428,6 +428,48 @@ def forward(; -510,18 +552,8 @@ def forward(; symbols: forward, _apply_qwen3_next_mlp, Qwen3HybridLinearDecoderLayer, __init__，涉及 `forward, _apply_qwen3_next_mlp, Qwen3HybridLinearDecoderLayer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +46/-23 (69 lines); hunks: -428,6 +428,48 @@ def forward(; -510,18 +552,8 @@ def forward(; symbols: forward, _apply_qwen3_next_mlp, Qwen3HybridLinearDecoderLayer, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +46/-23
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23925 - [NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next

- 链接: https://github.com/sgl-project/sglang/pull/23925
- 状态/时间: merged / 2026-05-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `55ba03db6a46`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+194/-19，可读 patch 284 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +49/-8 (57 lines); hunks: -69,6 +69,9; -751,14 +754,8 @@ def _apply_qk_norm(; symbols: _apply_qk_norm, self_attention, forward_prepare_native, forward_prepare_npu，涉及 `_apply_qk_norm, self_attention, forward_prepare_native`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +49/-8 (57 lines); hunks: -69,6 +69,9; -751,14 +754,8 @@ def _apply_qk_norm(; symbols: _apply_qk_norm, self_attention, forward_prepare_native, forward_prepare_npu
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +49/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26204 - Optimize Qwen3 Next FP8 MoE on H200

- 链接: https://github.com/sgl-project/sglang/pull/26204
- 状态/时间: merged / 2026-06-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`；关联提交 `06e0df5899aa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+427/-28，可读 patch 589 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Optimize Qwen3 Next FP8 MoE on H200」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`；技术摘要: 覆盖「Optimize Qwen3 Next FP8 MoE on H200」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +39/-9 (48 lines); hunks: -6,10 +6,12; -35,6 +37,11; symbols: __init__, routed_experts_weights_of_layer，涉及 `__init__, routed_experts_weights_of_layer`；`python/sglang/srt/models/qwen3_next_mtp.py` modified +13/-1 (14 lines); hunks: -59,7 +59,6 @@ def __init__(; -86,6 +85,19 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +39/-9 (48 lines); hunks: -6,10 +6,12; -35,6 +37,11; symbols: __init__, routed_experts_weights_of_layer
  - `python/sglang/srt/models/qwen3_next_mtp.py` modified +13/-1 (14 lines); hunks: -59,7 +59,6 @@ def __init__(; -86,6 +85,19 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +39/-9; `python/sglang/srt/models/qwen3_next_mtp.py` modified +13/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=513,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=513,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`, `python/sglang/srt/models/qwen2_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #45739 - [Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/45739
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_next.py`；关联提交 `db90f584d2f4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+57/-1，可读 patch 96 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_next.py`；技术摘要: 覆盖「[Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950」；主要实现面是 `python/sglang/srt/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_next.py` modified +57/-1 (58 lines); hunks: -1,4 +1,5; -63,8 +64,10; symbols: _fused_attention_prologue, _apply_qk_norm, forward_prepare_fused, forward_prepare_native，涉及 `_fused_attention_prologue, _apply_qk_norm, forward_prepare_fused`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_next.py` modified +57/-1 (58 lines); hunks: -1,4 +1,5; -63,8 +64,10; symbols: _fused_attention_prologue, _apply_qk_norm, forward_prepare_fused, forward_prepare_native
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_next.py` modified +57/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
