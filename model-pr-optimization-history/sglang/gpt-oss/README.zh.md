# sglang GPT-OSS 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/OpenAI/GPT-OSS.mdx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/gpt-oss-deployment.jsx` | 无直接 PR 号提交 |
| `python/sglang/srt/arg_groups/model_overrides/gpt_oss.py` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/gpt_oss_detector.py` | [#9043](https://github.com/sgl-project/sglang/pull/9043), [#9190](https://github.com/sgl-project/sglang/pull/9190), [#9657](https://github.com/sgl-project/sglang/pull/9657) |
| `python/sglang/srt/models/gpt_oss.py` | [#8824](https://github.com/sgl-project/sglang/pull/8824), [#8843](https://github.com/sgl-project/sglang/pull/8843), [#8944](https://github.com/sgl-project/sglang/pull/8944), [#9028](https://github.com/sgl-project/sglang/pull/9028), [#9146](https://github.com/sgl-project/sglang/pull/9146), [#9161](https://github.com/sgl-project/sglang/pull/9161), [#9359](https://github.com/sgl-project/sglang/pull/9359), [#9433](https://github.com/sgl-project/sglang/pull/9433), [#9469](https://github.com/sgl-project/sglang/pull/9469), [#9783](https://github.com/sgl-project/sglang/pull/9783), [#14197](https://github.com/sgl-project/sglang/pull/14197), [#16775](https://github.com/sgl-project/sglang/pull/16775), ... (25 total) |
| `python/sglang/test/gpt_oss_common.py` | [#16426](https://github.com/sgl-project/sglang/pull/16426) |
| `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` | [#26884](https://github.com/sgl-project/sglang/pull/26884) |
| `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` | [#27204](https://github.com/sgl-project/sglang/pull/27204) |
| `test/registered/amd/accuracy/mi45x/test_gpt_oss_w4a8_mxfp4_eval_mi45x.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` | [#34645](https://github.com/sgl-project/sglang/pull/34645) |
| `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` | [#34645](https://github.com/sgl-project/sglang/pull/34645) |
| `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` | [#31732](https://github.com/sgl-project/sglang/pull/31732) |
| `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` | [#39611](https://github.com/sgl-project/sglang/pull/39611) |
| `test/registered/e2e/models/test_gpt_oss_4gpu_mxfp4.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_gpt_oss_sm120.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models_large/test_gpt_oss_120b.py` | 无直接 PR 号提交 |
| `test/registered/e2e/moe/test_paged_experts_gpt_oss.py` | 无直接 PR 号提交 |
| `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` | [#21570](https://github.com/sgl-project/sglang/pull/21570) |
| `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` | [#30050](https://github.com/sgl-project/sglang/pull/30050) |
| `test/registered/page_major/test_page_major_gpt_oss.py` | 无直接 PR 号提交 |
| `test/registered/unit/models/test_gpt_oss_expert_loader_layout.py` | 无直接 PR 号提交 |
| `test/registered/unit/models/test_gpt_oss_runai_ownership.py` | [#38908](https://github.com/sgl-project/sglang/pull/38908) |

## PR 覆盖总览

- git 追溯 PR 数: 34
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 34
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #8824 - Add initial support for gpt-oss

- 链接: https://github.com/sgl-project/sglang/pull/8824
- 状态/时间: merged / 2025-08-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `c1d2061f97ae`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+1595/-47，可读 patch 2185 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add initial support for gpt-oss」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Add initial support for gpt-oss」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` added +923/-0 (923 lines); hunks: -0,0 +1,923; symbols: GptOssConfig, __init__, get_attention_sliding_window_size, GptOssSparseMoeBlock，涉及 `GptOssConfig, __init__, get_attention_sliding_window_size`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` added +923/-0 (923 lines); hunks: -0,0 +1,923; symbols: GptOssConfig, __init__, get_attention_sliding_window_size, GptOssSparseMoeBlock
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` added +923/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/triton_ops/decode_attention.py`, `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #8843 - Support mxfp4 for GPT-OSS

- 链接: https://github.com/sgl-project/sglang/pull/8843
- 状态/时间: merged / 2025-08-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `168033d5fb1e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+791/-325，可读 patch 1320 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support mxfp4 for GPT-OSS」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Support mxfp4 for GPT-OSS」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +209/-9 (218 lines); hunks: -25,6 +25,8; -108,11 +110,15 @@ def __init__(; symbols: __init__, _get_default_weight_mapping, load_weights，涉及 `__init__, _get_default_weight_mapping, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +209/-9 (218 lines); hunks: -25,6 +25,8; -108,11 +110,15 @@ def __init__(; symbols: __init__, _get_default_weight_mapping, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +209/-9
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`, `python/sglang/srt/layers/quantization/__init__.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #8944 - Expert Parallelism for GPT-OSS

- 链接: https://github.com/sgl-project/sglang/pull/8944
- 状态/时间: merged / 2025-08-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `1d24db834803`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+269/-119，可读 patch 956 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Expert Parallelism for GPT-OSS」；模型线: GPT-OSS；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Expert Parallelism for GPT-OSS」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +54/-47 (101 lines); hunks: -28,6 +28,7; -96,11 +97,6 @@ def __init__(; symbols: __init__, _load_mxfp4_experts_weights，涉及 `__init__, _load_mxfp4_experts_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +54/-47 (101 lines); hunks: -28,6 +28,7; -96,11 +97,6 @@ def __init__(; symbols: __init__, _load_mxfp4_experts_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +54/-47
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9043 - (gpt-oss, oai, chat): Remove Harmony Integration and Implement Native GPT-OSS Tool Call Support

- 链接: https://github.com/sgl-project/sglang/pull/9043
- 状态/时间: merged / 2025-08-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/gpt_oss_detector.py`；关联提交 `a21849013607`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+717/-409，可读 patch 1293 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「(gpt-oss, oai, chat): Remove Harmony Integration and Implement Native GPT-OSS Tool Call Support」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/gpt_oss_detector.py`；技术摘要: 覆盖「(gpt-oss, oai, chat): Remove Harmony Integration and Implement Native GPT-OSS Tool Call Support」；主要实现面是 `python/sglang/srt/function_call/gpt_oss_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/gpt_oss_detector.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse，涉及 `GptOssDetector, __init__, has_tool_call`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/gpt_oss_detector.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/gpt_oss_detector.py` added +331/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/entrypoints/harmony_utils.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/protocol.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9146 - Fix gpt-oss ~2x memory consumption issue

- 链接: https://github.com/sgl-project/sglang/pull/9146
- 状态/时间: merged / 2025-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `9394ed63867d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+19/-7，可读 patch 47 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix gpt-oss ~2x memory consumption issue」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Fix gpt-oss ~2x memory consumption issue」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +19/-7 (26 lines); hunks: -64,7 +64,13; -655,6 +661,18 @@ def __init__(; symbols: __init__, routed_experts_weights_of_layer, forward, _load_normal_weights，涉及 `__init__, routed_experts_weights_of_layer, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +19/-7 (26 lines); hunks: -64,7 +64,13; -655,6 +661,18 @@ def __init__(; symbols: __init__, routed_experts_weights_of_layer, forward, _load_normal_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +19/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9028 - Support FA3 backend for gpt-oss

- 链接: https://github.com/sgl-project/sglang/pull/9028
- 状态/时间: merged / 2025-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `0ff6d1fce122`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+24/-6，可读 patch 121 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support FA3 backend for gpt-oss」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Support FA3 backend for gpt-oss」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -294,7 +294,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -294,7 +294,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -294,7 +294,7 @@ def __init__(
-            torch.empty(self.num_heads, dtype=torch.float32), requires_grad=False
+            torch.empty(self.num_heads, dtype=torch.bfloat16), requires_grad=False
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/pyproject.toml`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9161 - Fix broken trtllm_mha attn backend with gpt-oss

- 链接: https://github.com/sgl-project/sglang/pull/9161
- 状态/时间: merged / 2025-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `6b7c24712cda`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix broken trtllm_mha attn backend with gpt-oss」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Fix broken trtllm_mha attn backend with gpt-oss」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -293,8 +293,12 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -293,8 +293,12 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9359 - Support DP attention with GPT-OSS

- 链接: https://github.com/sgl-project/sglang/pull/9359
- 状态/时间: merged / 2025-08-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `c10b8e6a0f2a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+6/-5，可读 patch 25 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support DP attention with GPT-OSS」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Support DP attention with GPT-OSS」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1123,7 +1123,7 @@ def _load_normal_weights(; symbols: _load_normal_weights，涉及 `_load_normal_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1123,7 +1123,7 @@ def _load_normal_weights(; symbols: _load_normal_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -1123,7 +1123,7 @@ def _load_normal_weights(
-                            start = tp_rank * param.numel()
+                            start = get_attention_tp_rank() * param.numel()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/server_args.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9433 - [fix] Fix mxfp4 weight loading bug with TP sharding in GPT-OSS

- 链接: https://github.com/sgl-project/sglang/pull/9433
- 状态/时间: merged / 2025-08-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `dae9a80f43e8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-3，可读 patch 46 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[fix] Fix mxfp4 weight loading bug with TP sharding in GPT-OSS」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[fix] Fix mxfp4 weight loading bug with TP sharding in GPT-OSS」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +9/-1 (10 lines); hunks: -16,6 +16,7; -788,18 +789,25 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights，涉及 `_load_mxfp4_experts_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +9/-1 (10 lines); hunks: -16,6 +16,7; -788,18 +789,25 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +9/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9469 - fix: tmp revert gpt oss tp sharding on hopper

- 链接: https://github.com/sgl-project/sglang/pull/9469
- 状态/时间: merged / 2025-08-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `849957bc76c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-3，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: tmp revert gpt oss tp sharding on hopper」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「fix: tmp revert gpt oss tp sharding on hopper」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -793,9 +793,12 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights，涉及 `_load_mxfp4_experts_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -793,9 +793,12 @@ def _load_mxfp4_experts_weights(self, weights):; symbols: _load_mxfp4_experts_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +6/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9190 - Fix Harmony reasoning parser for and auto-separation for gpt-oss models

- 链接: https://github.com/sgl-project/sglang/pull/9190
- 状态/时间: merged / 2025-08-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/gpt_oss_detector.py`；关联提交 `a0a77d937b99`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+1681/-556，可读 patch 2406 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Harmony reasoning parser for and auto-separation for gpt-oss models」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/gpt_oss_detector.py`；技术摘要: 覆盖「Fix Harmony reasoning parser for and auto-separation for gpt-oss models」；主要实现面是 `python/sglang/srt/function_call/gpt_oss_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +144/-256 (400 lines); hunks: -1,7 +1,7; -10,60 +10,31; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse，涉及 `GptOssDetector, __init__, has_tool_call`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/gpt_oss_detector.py` modified +144/-256 (400 lines); hunks: -1,7 +1,7; -10,60 +10,31; symbols: GptOssDetector, __init__, has_tool_call, detect_and_parse
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +144/-256
- 验证与风险: diff 自带测试面 `test/srt/run_suite.py`, `test/srt/test_harmony_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #9783 - support fp8 kvcache for hybrid attn backend on GPT-OSS

- 链接: https://github.com/sgl-project/sglang/pull/9783
- 状态/时间: merged / 2025-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `9db8025376b2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-4，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support fp8 kvcache for hybrid attn backend on GPT-OSS」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「support fp8 kvcache for hybrid attn backend on GPT-OSS」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +5/-4 (9 lines); hunks: -193,8 +193,9 @@ def forward_normal(; -341,7 +342,7 @@ def forward_prepare(; symbols: forward_normal, _enable_fused_set_kv_buffer, forward_prepare, forward_core，涉及 `forward_normal, _enable_fused_set_kv_buffer, forward_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +5/-4 (9 lines); hunks: -193,8 +193,9 @@ def forward_normal(; -341,7 +342,7 @@ def forward_prepare(; symbols: forward_normal, _enable_fused_set_kv_buffer, forward_prepare, forward_core
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +5/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9657 - fix: gpt-oss streaming dropping normal content when tools are provided but not used

- 链接: https://github.com/sgl-project/sglang/pull/9657
- 状态/时间: merged / 2025-09-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/gpt_oss_detector.py`；关联提交 `28c79dc84ab8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+23/-0，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: gpt-oss streaming dropping normal content when tools are provided but not used」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/gpt_oss_detector.py`；技术摘要: 覆盖「fix: gpt-oss streaming dropping normal content when tools are provided but not used」；主要实现面是 `python/sglang/srt/function_call/gpt_oss_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +23/-0 (23 lines); hunks: -81,6 +81,29 @@ def parse_streaming_increment(; symbols: parse_streaming_increment，涉及 `parse_streaming_increment`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/gpt_oss_detector.py` modified +23/-0 (23 lines); hunks: -81,6 +81,29 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/gpt_oss_detector.py` modified +23/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/gpt_oss_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16426 - Fix gpt_oss_common import path and migrate core tests

- 链接: https://github.com/sgl-project/sglang/pull/16426
- 状态/时间: merged / 2026-01-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/test/gpt_oss_common.py`；关联提交 `0c474273c514`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+48/-26，可读 patch 255 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix gpt_oss_common import path and migrate core tests」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/test/gpt_oss_common.py`；技术摘要: 覆盖「Fix gpt_oss_common import path and migrate core tests」；主要实现面是 `python/sglang/test/gpt_oss_common.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/test/gpt_oss_common.py` renamed +0/-0 (0 lines)。
- 代码 diff 细节:
  - `python/sglang/test/gpt_oss_common.py` renamed +0/-0 (0 lines)
- 关键代码摘录:

```diff
No textual patch was returned by GitHub for the selected changed files.
```

- 已读文件:
  - tests: `python/sglang/test/gpt_oss_common.py` renamed +0/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/gpt_oss_common.py`, `test/registered/core/test_deterministic.py`, `test/registered/core/test_gpt_oss_1gpu.py`, `test/registered/core/test_hidden_states.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14197 - [NPU]Support GPT-OSS for NPU

- 链接: https://github.com/sgl-project/sglang/pull/14197
- 状态/时间: merged / 2026-01-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `733de6be31e2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+96/-17，可读 patch 244 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]Support GPT-OSS for NPU」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[NPU]Support GPT-OSS for NPU」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +20/-15 (35 lines); hunks: -71,9 +71,10; -129,6 +130,7 @@ def __init__(; symbols: __init__, forward_prepare，涉及 `__init__, forward_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +20/-15 (35 lines); hunks: -71,9 +71,10; -129,6 +130,7 @@ def __init__(; symbols: __init__, forward_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +20/-15
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17553 - [NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py

- 链接: https://github.com/sgl-project/sglang/pull/17553
- 状态/时间: merged / 2026-01-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `61abff66c150`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -492,7 +492,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -492,7 +492,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -492,7 +492,7 @@ def __init__(
-        if is_npu:
+        if _is_npu:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18405 - [PCG] GPT OSS Triton Kernel Support

- 链接: https://github.com/sgl-project/sglang/pull/18405
- 状态/时间: merged / 2026-02-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `2bd8363486e4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+68/-32，可读 patch 228 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[PCG] GPT OSS Triton Kernel Support」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[PCG] GPT OSS Triton Kernel Support」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +21/-4 (25 lines); hunks: -25,6 +25,10; -72,6 +76,7; symbols: forward_normal, moe_impl, GptOssAttention, __init__，涉及 `forward_normal, moe_impl, GptOssAttention`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +21/-4 (25 lines); hunks: -25,6 +25,10; -72,6 +76,7; symbols: forward_normal, moe_impl, GptOssAttention, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +21/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/model_executor/model_runner.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20755 - Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+

- 链接: https://github.com/sgl-project/sglang/pull/20755
- 状态/时间: merged / 2026-03-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `bbe25b24126d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+65/-2，可读 patch 91 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +65/-2 (67 lines); hunks: -75,10 +75,34; -97,6 +121,45 @@ def get_attention_sliding_window_size(config):; symbols: GptOssConfig, get_attention_sliding_window_size, TinyGemmLinear, __init__，涉及 `GptOssConfig, get_attention_sliding_window_size, TinyGemmLinear`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +65/-2 (67 lines); hunks: -75,10 +75,34; -97,6 +121,45 @@ def get_attention_sliding_window_size(config):; symbols: GptOssConfig, get_attention_sliding_window_size, TinyGemmLinear, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +65/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21570 - [4/n] Support gpt oss 20b lora

- 链接: https://github.com/sgl-project/sglang/pull/21570
- 状态/时间: merged / 2026-04-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`, `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`；关联提交 `566b4a4f1ccc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+195/-24，可读 patch 328 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[4/n] Support gpt oss 20b lora」；模型线: GPT-OSS；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/gpt_oss.py`, `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`；技术摘要: 覆盖「[4/n] Support gpt oss 20b lora」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`, `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +8/-0 (8 lines); hunks: -17,6 +17,7; -651,6 +652,13 @@ def forward(; symbols: forward, GptOssForCausalLM, should_apply_lora, __init__，涉及 `forward, GptOssForCausalLM, should_apply_lora`；`test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: kl_v2, get_prompt_logprobs, TestLoRAGptOss20BLogprobDiff, test_lora_gpt_oss_20b_logprob_accuracy，涉及 `kl_v2, get_prompt_logprobs, TestLoRAGptOss20BLogprobDiff`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +8/-0 (8 lines); hunks: -17,6 +17,7; -651,6 +652,13 @@ def forward(; symbols: forward, GptOssForCausalLM, should_apply_lora, __init__
  - `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: kl_v2, get_prompt_logprobs, TestLoRAGptOss20BLogprobDiff, test_lora_gpt_oss_20b_logprob_accuracy
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +8/-0
  - tests: `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py` added +151/-0
- 验证与风险: diff 自带测试面 `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_8b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #16775 - [CPU] Add GPT-OSS model optimization for CPU

- 链接: https://github.com/sgl-project/sglang/pull/16775
- 状态/时间: merged / 2026-05-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `3ecf2c76ad1b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 35 个文件，+2023/-553，可读 patch 3996 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CPU] Add GPT-OSS model optimization for CPU」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[CPU] Add GPT-OSS model optimization for CPU」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +20/-1 (21 lines); hunks: -81,6 +81,7; -89,6 +90,7; symbols: _load_mxfp4_experts_weights, _load_normal_weights，涉及 `_load_mxfp4_experts_weights, _load_normal_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +20/-1 (21 lines); hunks: -81,6 +81,7; -89,6 +90,7; symbols: _load_mxfp4_experts_weights, _load_normal_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +20/-1
- 验证与风险: diff 自带测试面 `test/registered/cpu/test_decode.py`, `test/registered/cpu/test_extend.py`, `test/registered/cpu/test_gemm.py`, `test/registered/cpu/test_mla.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26884 - [AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path

- 链接: https://github.com/sgl-project/sglang/pull/26884
- 状态/时间: merged / 2026-06-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`；关联提交 `4226a6f13aa6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+87/-20，可读 patch 206 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`；技术摘要: 覆盖「[AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` modified +12/-2 (14 lines); hunks: -75,7 +75,14 @@ def __post_init__(self):; -93,7 +100,10 @@ def __post_init__(self):; symbols: __post_init__，涉及 `__post_init__`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` modified +12/-2 (14 lines); hunks: -75,7 +75,14 @@ def __post_init__(self):; -93,7 +100,10 @@ def __post_init__(self):; symbols: __post_init__
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` modified +12/-2
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27063 - [AMD] Optimize gpt-oss-120B performance

- 链接: https://github.com/sgl-project/sglang/pull/27063
- 状态/时间: merged / 2026-06-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `1c73ff8ad3fd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+1874/-54，可读 patch 2160 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Optimize gpt-oss-120B performance」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[AMD] Optimize gpt-oss-120B performance」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +74/-5 (79 lines); hunks: -84,6 +84,7; -92,6 +93,7; symbols: forward, _resolve_moe_input_pad_multiple, GptOssSparseMoeBlock, __init__，涉及 `forward, _resolve_moe_input_pad_multiple, GptOssSparseMoeBlock`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +74/-5 (79 lines); hunks: -84,6 +84,7; -92,6 +93,7; symbols: forward, _resolve_moe_input_pad_multiple, GptOssSparseMoeBlock, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +74/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27528 - Fix GPT-OSS MXFP4 hidden size reshape on SM10X

- 链接: https://github.com/sgl-project/sglang/pull/27528
- 状态/时间: merged / 2026-06-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `dc24a2682190`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix GPT-OSS MXFP4 hidden size reshape on SM10X」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Fix GPT-OSS MXFP4 hidden size reshape on SM10X」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +2/-1 (3 lines); hunks: -208,6 +208,7 @@ def __init__(; -291,7 +292,7 @@ def forward_normal(; symbols: __init__, forward_normal，涉及 `__init__, forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +2/-1 (3 lines); hunks: -208,6 +208,7 @@ def __init__(; -291,7 +292,7 @@ def forward_normal(; symbols: __init__, forward_normal
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -208,6 +208,7 @@ def __init__(
+        self.hidden_size = config.hidden_size
@@ -291,7 +292,7 @@ def forward_normal(
-        hidden_dim_unpadded = self.experts.hidden_size
+        hidden_dim_unpadded = self.hidden_size
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27941 - Enable PDL for GPT-OSS tinygemm router

- 链接: https://github.com/sgl-project/sglang/pull/27941
- 状态/时间: merged / 2026-06-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `cb9140ee6108`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 25 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable PDL for GPT-OSS tinygemm router」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Enable PDL for GPT-OSS tinygemm router」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +2/-2 (4 lines); hunks: -26,6 +26,7; -161,7 +162,7 @@ def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Op...; symbols: forward, _load_normal_weights，涉及 `forward, _load_normal_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +2/-2 (4 lines); hunks: -26,6 +26,7; -161,7 +162,7 @@ def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Op...; symbols: forward, _load_normal_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27204 - [AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8

- 链接: https://github.com/sgl-project/sglang/pull/27204
- 状态/时间: merged / 2026-06-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`；关联提交 `a5e6dd37677f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+948/-3，可读 patch 998 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`；技术摘要: 覆盖「[AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +14/-3 (17 lines); hunks: -879,12 +879,23 @@ def load_weights(; symbols: load_weights，涉及 `load_weights`；`test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_one_example, get_few_shot_examples，涉及 `ModelConfig, __post_init__, get_one_example`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +14/-3 (17 lines); hunks: -879,12 +879,23 @@ def load_weights(; symbols: load_weights
  - `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_one_example, get_few_shot_examples
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +14/-3
  - tests: `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py` added +251/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31649 - Enable GPT-OSS TinyGEMM on CUDA 13

- 链接: https://github.com/sgl-project/sglang/pull/31649
- 状态/时间: merged / 2026-07-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `8bf2ab9be931`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-2，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable GPT-OSS TinyGEMM on CUDA 13」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Enable GPT-OSS TinyGEMM on CUDA 13」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +1/-2 (3 lines); hunks: -72,7 +72,6; -94,7 +93,7。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +1/-2 (3 lines); hunks: -72,7 +72,6; -94,7 +93,7
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -72,7 +72,6 @@
-    get_cuda_version,
@@ -94,7 +93,7 @@
-if _is_tinygemm_supported and get_cuda_version()[0] < 13:
+if _is_tinygemm_supported:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +1/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31732 - Support GPT-OSS zigzag CP with TRTLLM-MHA

- 链接: https://github.com/sgl-project/sglang/pull/31732
- 状态/时间: merged / 2026-07-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`；关联提交 `9668d9ea72ae`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+143/-33，可读 patch 289 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support GPT-OSS zigzag CP with TRTLLM-MHA」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`；技术摘要: 覆盖「Support GPT-OSS zigzag CP with TRTLLM-MHA」；主要实现面是 `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` added +32/-0 (32 lines); hunks: -0,0 +1,32; symbols: TestGptOss4GpuMxfp4CP, test_mxfp4_120b，涉及 `TestGptOss4GpuMxfp4CP, test_mxfp4_120b`。
- 代码 diff 细节:
  - `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` added +32/-0 (32 lines); hunks: -0,0 +1,32; symbols: TestGptOss4GpuMxfp4CP, test_mxfp4_120b
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py` added +32/-0
- 验证与风险: diff 自带测试面 `test/registered/cp/test_gpt_oss_4gpu_mxfp4_cp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #32334 - [Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states

- 链接: https://github.com/sgl-project/sglang/pull/32334
- 状态/时间: merged / 2026-07-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `5df193b4ac0f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+36/-6，可读 patch 82 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +19/-6 (25 lines); hunks: -720,15 +720,25 @@ def forward(; -1319,15 +1329,18 @@ def set_eagle3_layers_to_capture(self, layer_ids: Option...; symbols: forward, set_eagle3_layers_to_capture, set_dflash_layers_to_capture，涉及 `forward, set_eagle3_layers_to_capture, set_dflash_layers_to_capture`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +19/-6 (25 lines); hunks: -720,15 +720,25 @@ def forward(; -1319,15 +1329,18 @@ def set_eagle3_layers_to_capture(self, layer_ids: Option...; symbols: forward, set_eagle3_layers_to_capture, set_dflash_layers_to_capture
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +19/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/llama_eagle3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30050 - [MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale

- 链接: https://github.com/sgl-project/sglang/pull/30050
- 状态/时间: merged / 2026-08-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`；关联提交 `553dc0f936ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+1100/-43，可读 patch 1372 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale」；模型线: GPT-OSS；类别: 文档/测试/CI；主要 diff: `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`；技术摘要: 覆盖「[MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale」；主要实现面是 `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: _available_gb, TestGptOssMlxCorrectness, setUpClass, tearDownClass，涉及 `_available_gb, TestGptOssMlxCorrectness, setUpClass`。
- 代码 diff 细节:
  - `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: _available_gb, TestGptOssMlxCorrectness, setUpClass, tearDownClass
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py` added +371/-0
- 验证与风险: diff 自带测试面 `test/registered/mlx/models_e2e/test_gpt_oss_mlx_correctness.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`, `test/registered/unit/hardware_backend/mlx/test_sliding_window_attention.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #34645 - [AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly

- 链接: https://github.com/sgl-project/sglang/pull/34645
- 状态/时间: merged / 2026-08-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`, `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`；关联提交 `d91c3682b0b4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+283/-0，可读 patch 319 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`；技术摘要: 覆盖「[AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly」；主要实现面是 `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` added +107/-0 (107 lines); hunks: -0,0 +1,107; symbols: TestNightlyGptOssPerformanceMI35x, setUpClass, test_bench_one_batch，涉及 `TestNightlyGptOssPerformanceMI35x, setUpClass, test_bench_one_batch`；`test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` added +106/-0 (106 lines); hunks: -0,0 +1,106; symbols: TestNightlyGptOssPerformanceAMD, setUpClass, test_bench_one_batch，涉及 `TestNightlyGptOssPerformanceAMD, setUpClass, test_bench_one_batch`。
- 代码 diff 细节:
  - `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` added +107/-0 (107 lines); hunks: -0,0 +1,107; symbols: TestNightlyGptOssPerformanceMI35x, setUpClass, test_bench_one_batch
  - `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` added +106/-0 (106 lines); hunks: -0,0 +1,106; symbols: TestNightlyGptOssPerformanceAMD, setUpClass, test_bench_one_batch
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py` added +107/-0; `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py` added +106/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/nightly_bench_utils.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`, `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37199 - fix(gpt-oss): avoid duplicate MoE reduction with DP attention

- 链接: https://github.com/sgl-project/sglang/pull/37199
- 状态/时间: merged / 2026-09-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `28457f0dcab4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+40/-5，可读 patch 87 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(gpt-oss): avoid duplicate MoE reduction with DP attention」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「fix(gpt-oss): avoid duplicate MoE reduction with DP attention」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +16/-3 (19 lines); hunks: -44,7 +44,10; -329,7 +332,9 @@ def forward_normal(; symbols: forward_normal, __init__, forward，涉及 `forward_normal, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +16/-3 (19 lines); hunks: -44,7 +44,10; -329,7 +332,9 @@ def forward_normal(; symbols: forward_normal, __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +16/-3
- 验证与风险: diff 自带测试面 `test/registered/models_e2e/test_gpt_oss_4gpu_mxfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38908 - Fix gpt-oss RunAI streamer weight ownership

- 链接: https://github.com/sgl-project/sglang/pull/38908
- 状态/时间: merged / 2026-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`, `test/registered/unit/models/test_gpt_oss_runai_ownership.py`；关联提交 `fd3222670660`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+126/-12，可读 patch 163 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix gpt-oss RunAI streamer weight ownership」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_gpt_oss_runai_ownership.py`, `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「Fix gpt-oss RunAI streamer weight ownership」；主要实现面是 `test/registered/unit/models/test_gpt_oss_runai_ownership.py`, `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_gpt_oss_runai_ownership.py` added +94/-0 (94 lines); hunks: -0,0 +1,94; symbols: _streamed, _Mxfp4QuantConfig, get_name, TestGptOssRunaiOwnership，涉及 `_streamed, _Mxfp4QuantConfig, get_name`；`python/sglang/srt/models/gpt_oss.py` modified +32/-12 (44 lines); hunks: -66,7 +66,10; -953,20 +956,25 @@ def load_weights(; symbols: load_weights, _load_weights_mxfp4, experts, get_attention_sliding_window_size，涉及 `load_weights, _load_weights_mxfp4, experts`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_gpt_oss_runai_ownership.py` added +94/-0 (94 lines); hunks: -0,0 +1,94; symbols: _streamed, _Mxfp4QuantConfig, get_name, TestGptOssRunaiOwnership
  - `python/sglang/srt/models/gpt_oss.py` modified +32/-12 (44 lines); hunks: -66,7 +66,10; -953,20 +956,25 @@ def load_weights(; symbols: load_weights, _load_weights_mxfp4, experts, get_attention_sliding_window_size
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/unit/models/test_gpt_oss_runai_ownership.py` added +94/-0
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +32/-12
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_gpt_oss_runai_ownership.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39611 - [CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss

- 链接: https://github.com/sgl-project/sglang/pull/39611
- 状态/时间: merged / 2026-09-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`；关联提交 `47a157f257f1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+25/-63，可读 patch 106 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`；技术摘要: 覆盖「[CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss」；主要实现面是 `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` modified +25/-63 (88 lines); hunks: -6,10 +6,6; -23,69 +19,35 @@ class TestDisaggregationDWDPGptOss(PDDisaggregationServerBase):; symbols: TestDisaggregationDWDPGptOss, setUpClass, start_prefill, start_decode，涉及 `TestDisaggregationDWDPGptOss, setUpClass, start_prefill`。
- 代码 diff 细节:
  - `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` modified +25/-63 (88 lines); hunks: -6,10 +6,6; -23,69 +19,35 @@ class TestDisaggregationDWDPGptOss(PDDisaggregationServerBase):; symbols: TestDisaggregationDWDPGptOss, setUpClass, start_prefill, start_decode
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py` modified +25/-63
- 验证与风险: diff 自带测试面 `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43624 - [Model] Keep gpt-oss router logits batch-invariant under deterministic inference

- 链接: https://github.com/sgl-project/sglang/pull/43624
- 状态/时间: merged / 2026-10-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/gpt_oss.py`；关联提交 `7187bb593ea3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-0，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Keep gpt-oss router logits batch-invariant under deterministic inference」；模型线: GPT-OSS；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/gpt_oss.py`；技术摘要: 覆盖「[Model] Keep gpt-oss router logits batch-invariant under deterministic inference」；主要实现面是 `python/sglang/srt/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -137,8 +137,11 @@ class TinyGemmLinear(ReplicatedLinear):; symbols: TinyGemmLinear, __init__，涉及 `TinyGemmLinear, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -137,8 +137,11 @@ class TinyGemmLinear(ReplicatedLinear):; symbols: TinyGemmLinear, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/gpt_oss.py
@@ -137,8 +137,11 @@ class TinyGemmLinear(ReplicatedLinear):
+        # tinygemm serves only up to 128 tokens, so with it a token's router
+        # logits would depend on how many tokens share its batch.
+            and not get_exec().deterministic.enable_deterministic_inference
```

- 已读文件:
  - runtime: `python/sglang/srt/models/gpt_oss.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
