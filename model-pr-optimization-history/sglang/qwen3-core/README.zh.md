# sglang Qwen3 Core 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` | [#43551](https://github.com/sgl-project/sglang/pull/43551), [#47785](https://github.com/sgl-project/sglang/pull/47785), [#48051](https://github.com/sgl-project/sglang/pull/48051) |
| `docs/src/snippets/autoregressive/qwen3-deployment.jsx` | [#43554](https://github.com/sgl-project/sglang/pull/43554) |
| `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py` | [#39126](https://github.com/sgl-project/sglang/pull/39126) |
| `python/sglang/srt/models/qwen3.py` | [#4693](https://github.com/sgl-project/sglang/pull/4693), [#6250](https://github.com/sgl-project/sglang/pull/6250), [#6990](https://github.com/sgl-project/sglang/pull/6990), [#7312](https://github.com/sgl-project/sglang/pull/7312), [#7681](https://github.com/sgl-project/sglang/pull/7681), [#7740](https://github.com/sgl-project/sglang/pull/7740), [#10574](https://github.com/sgl-project/sglang/pull/10574), [#15223](https://github.com/sgl-project/sglang/pull/15223), [#15390](https://github.com/sgl-project/sglang/pull/15390), [#16115](https://github.com/sgl-project/sglang/pull/16115), [#17535](https://github.com/sgl-project/sglang/pull/17535), [#19532](https://github.com/sgl-project/sglang/pull/19532), ... (24 total) |
| `python/sglang/srt/models/qwen3_moe.py` | [#4693](https://github.com/sgl-project/sglang/pull/4693), [#5917](https://github.com/sgl-project/sglang/pull/5917), [#6120](https://github.com/sgl-project/sglang/pull/6120), [#6250](https://github.com/sgl-project/sglang/pull/6250), [#6533](https://github.com/sgl-project/sglang/pull/6533), [#6598](https://github.com/sgl-project/sglang/pull/6598), [#6652](https://github.com/sgl-project/sglang/pull/6652), [#6709](https://github.com/sgl-project/sglang/pull/6709), [#6820](https://github.com/sgl-project/sglang/pull/6820), [#7740](https://github.com/sgl-project/sglang/pull/7740), [#8751](https://github.com/sgl-project/sglang/pull/8751), [#9973](https://github.com/sgl-project/sglang/pull/9973), ... (37 total) |
| `python/sglang/srt/models/qwen3_moe_mtp.py` | [#26468](https://github.com/sgl-project/sglang/pull/26468) |
| `test/registered/cpu/test_qwen3.py` | [#31171](https://github.com/sgl-project/sglang/pull/31171) |
| `test/registered/lora/test_lora_qwen3.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 59
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 59
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2025-04-18 | [#4693](https://github.com/sgl-project/sglang/pull/4693) | merged | [Model] Adding Qwen3 and Qwen3MoE | `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3.py` |
| 2025-04-30 | [#5917](https://github.com/sgl-project/sglang/pull/5917) | merged | [qwen3] support qwen3 ep moe | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-05-18 | [#6250](https://github.com/sgl-project/sglang/pull/6250) | merged | Add pipeline parallelism for Qwen2 and Qwen3 Model | `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py` |
| 2025-05-22 | [#6120](https://github.com/sgl-project/sglang/pull/6120) | merged | Support qwen3 deepep | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-05-24 | [#6533](https://github.com/sgl-project/sglang/pull/6533) | merged | support eplb for qwen3 | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-05-26 | [#6598](https://github.com/sgl-project/sglang/pull/6598) | merged | qwen3moe support two batch overlap | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-05-27 | [#6652](https://github.com/sgl-project/sglang/pull/6652) | merged | Fix qwen3 tbo/dp-lm-head | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-05-29 | [#6709](https://github.com/sgl-project/sglang/pull/6709) | merged | Fix PP for Qwen3 MoE | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-06-05 | [#6820](https://github.com/sgl-project/sglang/pull/6820) | merged | Fix Qwen3MoE missing token padding optimization | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-06-09 | [#6990](https://github.com/sgl-project/sglang/pull/6990) | merged | support qwen3 emebedding | `python/sglang/srt/models/qwen3.py` |
| 2025-07-03 | [#7681](https://github.com/sgl-project/sglang/pull/7681) | merged | support qwen3 dense model dp attention | `python/sglang/srt/models/qwen3.py` |
| 2025-07-03 | [#7740](https://github.com/sgl-project/sglang/pull/7740) | merged | [optimize] add two stream norm for qwen3 | `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py` |
| 2025-07-20 | [#7312](https://github.com/sgl-project/sglang/pull/7312) | merged | Add get_hidden_dim to qwen3.py for correct lora | `test/srt/models/lora/test_lora_qwen3.py`, `python/sglang/srt/models/qwen3.py` |
| 2025-08-06 | [#8751](https://github.com/sgl-project/sglang/pull/8751) | merged | [1/3] Optimize Slime Update Weights: Remove QWen3MOE Load Weight Overhead | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-09-04 | [#9973](https://github.com/sgl-project/sglang/pull/9973) | merged | Optimize Qwen3-moe model by using flashinfer fused allreduce | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-09-23 | [#10574](https://github.com/sgl-project/sglang/pull/10574) | merged | [Ascend]optimize Qwen3 on Ascend | `python/sglang/srt/models/qwen3.py` |
| 2025-09-26 | [#10749](https://github.com/sgl-project/sglang/pull/10749) | merged | Fuse write kv buffer into rope for qwen3 moe & bailing moe | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-10-01 | [#10985](https://github.com/sgl-project/sglang/pull/10985) | merged | Quick Fix: fix Qwen3-VL launch failure caused by MRotaryEmbedding arg | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-10-16 | [#10911](https://github.com/sgl-project/sglang/pull/10911) | merged | model: qwen3-omni (thinker-only) | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-10-29 | [#12002](https://github.com/sgl-project/sglang/pull/12002) | merged | Eagle3 DP attention for Qwen3 MoE | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-11-18 | [#13489](https://github.com/sgl-project/sglang/pull/13489) | merged | Flashinfer TRTLLM-GEN-MoE + Qwen3 | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-12-07 | [#13998](https://github.com/sgl-project/sglang/pull/13998) | merged | [apply][2/2] Fused qk_norm_rope for Qwen3-MoE | `python/sglang/srt/models/qwen3_moe.py` |
| 2025-12-17 | [#15223](https://github.com/sgl-project/sglang/pull/15223) | merged | [bug fix][pp] fix qwen3 model load | `python/sglang/srt/models/qwen3.py` |
| 2025-12-24 | [#15390](https://github.com/sgl-project/sglang/pull/15390) | merged | [NPU]qwen3 pp bugfix | `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py` |
| 2026-01-08 | [#16115](https://github.com/sgl-project/sglang/pull/16115) | merged | [NPU][Bugfix] Fix qwen3 error when enable-dp-lm-head | `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py` |
| 2026-01-28 | [#15904](https://github.com/sgl-project/sglang/pull/15904) | merged | [NPU] NZ for non-quantized MOE, Qwen3 MOE double memory consumption fix | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-02-03 | [#17535](https://github.com/sgl-project/sglang/pull/17535) | merged | Update weight rename check for Qwen3 Embeddings | `python/sglang/srt/models/qwen3.py` |
| 2026-02-08 | [#18189](https://github.com/sgl-project/sglang/pull/18189) | merged | [ModelOpt] Fix broken Qwen3-235B-A22B-Instruct-2507-NVFP4 launch | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-03-03 | [#19532](https://github.com/sgl-project/sglang/pull/19532) | merged | [NPU] bugs fix: fix a condition bug when using speculative inference on Qwen3 and Qwen3 moe | `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py` |
| 2026-03-20 | [#20931](https://github.com/sgl-project/sglang/pull/20931) | merged | [Bugifx] qwen3 rope parameter compatibility | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-03-22 | [#18233](https://github.com/sgl-project/sglang/pull/18233) | merged | Support Qwen3 MoE context parallel | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-03-24 | [#21195](https://github.com/sgl-project/sglang/pull/21195) | merged | Enable the qwen3 test | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-04-01 | [#21458](https://github.com/sgl-project/sglang/pull/21458) | merged | [AMD] Optimize Qwen3-VL decode - fuse QK-norm + 3D mRoPE + KV cache write | `python/sglang/srt/models/qwen3.py` |
| 2026-04-14 | [#22739](https://github.com/sgl-project/sglang/pull/22739) | merged | Restore Qwen3 rope config fallback | `python/sglang/srt/models/qwen3.py` |
| 2026-04-25 | [#23731](https://github.com/sgl-project/sglang/pull/23731) | merged | Fix Qwen3 MoE double-reduce when DP attention + EP + reduce_scatterv (#23729) | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-04-26 | [#23734](https://github.com/sgl-project/sglang/pull/23734) | merged | Fix Qwen3 MoE: also guard EP all-reduce with not use_reduce_scatter (follow-up to #23731) | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-05-02 | [#20520](https://github.com/sgl-project/sglang/pull/20520) | merged | [NPU]TP Communications compression For Qwen3 models for NPU | `python/sglang/srt/models/qwen3.py` |
| 2026-05-29 | [#26468](https://github.com/sgl-project/sglang/pull/26468) | merged | [Model] Add Qwen3-MoE MTP | `python/sglang/srt/models/qwen3_moe_mtp.py`, `python/sglang/srt/models/qwen3_moe.py` |
| 2026-05-31 | [#26798](https://github.com/sgl-project/sglang/pull/26798) | merged | Make qwen3's set_embed_and_head idempotent | `python/sglang/srt/models/qwen3.py` |
| 2026-06-29 | [#29505](https://github.com/sgl-project/sglang/pull/29505) | merged | [NPU] Qwen3-VL-30B use split_qkv_rmsnorm_rope for extend | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-06-30 | [#29627](https://github.com/sgl-project/sglang/pull/29627) | merged | [NPU] Qwen3-VL-8B use split_qkv_rmsnorm_rope for extend | `python/sglang/srt/models/qwen3.py` |
| 2026-07-15 | [#31171](https://github.com/sgl-project/sglang/pull/31171) | merged | [CPU] add fused input proj for qwen3.5 | `test/registered/cpu/test_qwen3.py` |
| 2026-07-29 | [#30768](https://github.com/sgl-project/sglang/pull/30768) | merged | :sparkles: [llm][npu][quant] Add W8A8 MXFP8 quantization for Qwen3 MoE on Ascend NPU | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-08-08 | [#34006](https://github.com/sgl-project/sglang/pull/34006) | merged | Fix Qwen3-MoE producing garbage with the mori a2a backend | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-08-14 | [#34810](https://github.com/sgl-project/sglang/pull/34810) | merged | fix(qwen3): support DeepEP-class backends and early EPLB state | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-09-13 | [#39126](https://github.com/sgl-project/sglang/pull/39126) | merged | [Qwen3.8] Enable NVIDIA NVFP4 on DGX Spark with file-backed PLE and PDL router fix | `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py` |
| 2026-09-23 | [#40870](https://github.com/sgl-project/sglang/pull/40870) | merged | [Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-10-04 | [#40190](https://github.com/sgl-project/sglang/pull/40190) | merged | [XPU] Enable fused QK-norm + RoPE for Qwen3-MoE | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-10-10 | [#43551](https://github.com/sgl-project/sglang/pull/43551) | merged | [Docs] Document Qwen3-4B/8B H200 mixed-chunk latency tradeoffs | `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` |
| 2026-10-10 | [#43554](https://github.com/sgl-project/sglang/pull/43554) | merged | [Docs] Let the Qwen3 B300 recipe use the default attention backend | `docs/src/snippets/autoregressive/qwen3-deployment.jsx` |
| 2026-10-15 | [#44266](https://github.com/sgl-project/sglang/pull/44266) | merged | [Fix] [AMD] qwen3: Fix KV cache write in the fused QK-norm + mRoPE decode path | `python/sglang/srt/models/qwen3.py` |
| 2026-10-16 | [#44267](https://github.com/sgl-project/sglang/pull/44267) | merged | [Perf] [AMD] qwen3: Fuse QK-norm + RoPE + KV cache write for dense Qwen3 decode | `python/sglang/srt/models/qwen3.py` |
| 2026-10-20 | [#39580](https://github.com/sgl-project/sglang/pull/39580) | merged | [Fix] eplb: Fix Qwen3 MoE output corruption after EPLB rebalance | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-10-29 | [#46832](https://github.com/sgl-project/sglang/pull/46832) | merged | [Perf] [AMD] qwen3: Use the fused QK-norm + RoPE + KV write in decode with an fp8 KV cache | `python/sglang/srt/models/qwen3.py` |
| 2026-10-31 | [#46908](https://github.com/sgl-project/sglang/pull/46908) | merged | [Perf] [NVIDIA] qwen3: Reuse fused QK-norm/RoPE kernel for decode | `python/sglang/srt/models/qwen3.py` |
| 2026-11-03 | [#48051](https://github.com/sgl-project/sglang/pull/48051) | merged | [Doc] qwen: Use TRT-LLM MHA for the B300 Qwen3-VL-4B recipe | `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` |
| 2026-11-03 | [#47993](https://github.com/sgl-project/sglang/pull/47993) | merged | [Perf] [NVIDIA] qwen3: Reuse the table QK-norm/RoPE kernel for MRoPE decode | `python/sglang/srt/models/qwen3.py` |
| 2026-11-05 | [#44491](https://github.com/sgl-project/sglang/pull/44491) | merged | [Perf] qwen3: Fuse SiLU*mul with the NVFP4 quantization of down_proj in Qwen2MLP | `python/sglang/srt/models/qwen3.py` |
| 2026-11-05 | [#47785](https://github.com/sgl-project/sglang/pull/47785) | merged | [Perf] [NVIDIA] qwen3: Fuse prefill QK norm and RoPE with contiguous Q | `python/sglang/srt/models/qwen3.py`, `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` |

## 逐 PR diff 审计卡

### PR #4693 - [Model] Adding Qwen3 and Qwen3MoE

- 链接: https://github.com/sgl-project/sglang/pull/4693
- 状态/时间: merged / 2025-04-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；关联提交 `4db463b1ad6e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+780/-14，可读 patch 840 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Adding Qwen3 and Qwen3MoE」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Model] Adding Qwen3 and Qwen3MoE」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` added +423/-0 (423 lines); hunks: -0,0 +1,423; symbols: Qwen3MoeSparseMoeBlock, __init__, forward, Qwen3MoeAttention，涉及 `Qwen3MoeSparseMoeBlock, __init__, forward`；`python/sglang/srt/models/qwen3.py` added +335/-0 (335 lines); hunks: -0,0 +1,335; symbols: Qwen3Attention, __init__, _apply_qk_norm, forward，涉及 `Qwen3Attention, __init__, _apply_qk_norm`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` added +423/-0 (423 lines); hunks: -0,0 +1,423; symbols: Qwen3MoeSparseMoeBlock, __init__, forward, Qwen3MoeAttention
  - `python/sglang/srt/models/qwen3.py` added +335/-0 (335 lines); hunks: -0,0 +1,335; symbols: Qwen3Attention, __init__, _apply_qk_norm, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -0,0 +1,423 @@
+# Adapted from qwen2_moe.py
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
diff -- python/sglang/srt/models/qwen3.py
@@ -0,0 +1,335 @@
+# Adapted from qwen2.py
+from functools import partial
+from typing import Any, Dict, Iterable, Optional, Tuple
+import torch
+from torch import nn
+from sglang.srt.distributed import (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` added +423/-0; `python/sglang/srt/models/qwen3.py` added +335/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/models/qwen2.py`, `python/sglang/srt/models/qwen2_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #5917 - [qwen3] support qwen3 ep moe

- 链接: https://github.com/sgl-project/sglang/pull/5917
- 状态/时间: merged / 2025-04-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `e330f2b86cd2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+16/-6，可读 patch 86 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[qwen3] support qwen3 ep moe」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[qwen3] support qwen3 ep moe」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +8/-3 (11 lines); hunks: -40,6 +40,7; -48,6 +49,7; symbols: __init__, load_weights，涉及 `__init__, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +8/-3 (11 lines); hunks: -40,6 +40,7; -48,6 +49,7; symbols: __init__, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -40,6 +40,7 @@
+from sglang.srt.layers.moe.ep_moe.layer import EPMoE
@@ -48,6 +49,7 @@
+from sglang.srt.managers.schedule_batch import global_server_args_dict
@@ -73,12 +75,13 @@ def __init__(
-        self.experts = FusedMoE(
+        MoEImpl = EPMoE if global_server_args_dict["enable_ep_moe"] else FusedMoE
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +8/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6250 - Add pipeline parallelism for Qwen2 and Qwen3 Model

- 链接: https://github.com/sgl-project/sglang/pull/6250
- 状态/时间: merged / 2025-05-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；关联提交 `11553c1a3727`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+340/-73，可读 patch 736 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add pipeline parallelism for Qwen2 and Qwen3 Model」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Add pipeline parallelism for Qwen2 and Qwen3 Model」；主要实现面是 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +52/-10 (62 lines); hunks: -1,12 +1,14; -19,15 +21,18; symbols: Qwen3Attention, __init__, forward, start_layer，涉及 `Qwen3Attention, __init__, forward`；`python/sglang/srt/models/qwen3_moe.py` modified +49/-10 (59 lines); hunks: -17,6 +17,7; -28,6 +29,7; symbols: Qwen3MoeSparseMoeBlock, __init__, forward, start_layer，涉及 `Qwen3MoeSparseMoeBlock, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +52/-10 (62 lines); hunks: -1,12 +1,14; -19,15 +21,18; symbols: Qwen3Attention, __init__, forward, start_layer
  - `python/sglang/srt/models/qwen3_moe.py` modified +49/-10 (59 lines); hunks: -17,6 +17,7; -28,6 +29,7; symbols: Qwen3MoeSparseMoeBlock, __init__, forward, start_layer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -1,12 +1,14 @@
+import logging
+    get_pp_group,
@@ -19,15 +21,18 @@
+from sglang.srt.layers.utils import get_layer_id
-from sglang.srt.model_executor.forward_batch_info import ForwardBatch
+from sglang.srt.model_executor.forward_batch_info import ForwardBatch, PPProxyTensors
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -17,6 +17,7 @@
+import logging
@@ -28,6 +29,7 @@
+    get_pp_group,
@@ -57,19 +59,22 @@
+from sglang.srt.layers.utils import get_layer_id
-from sglang.srt.model_executor.forward_batch_info import ForwardBatch
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +52/-10; `python/sglang/srt/models/qwen3_moe.py` modified +49/-10
- 验证与风险: diff 自带测试面 `test/srt/test_pp_single_node.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #6120 - Support qwen3 deepep

- 链接: https://github.com/sgl-project/sglang/pull/6120
- 状态/时间: merged / 2025-05-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `fc0e3b91744b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+125/-8，可读 patch 207 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support qwen3 deepep」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Support qwen3 deepep」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +121/-7 (128 lines); hunks: -32,6 +32,7; -54,8 +55,10; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +121/-7 (128 lines); hunks: -32,6 +32,7; -54,8 +55,10; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -32,6 +32,7 @@
+    parallel_state,
@@ -54,8 +55,10 @@
-from sglang.srt.layers.moe.ep_moe.layer import EPMoE
+from sglang.srt.layers.moe.ep_moe.layer import DeepEPMoE, EPMoE
+from sglang.srt.layers.moe.ep_moe.token_dispatcher import DeepEPDispatcher
+from sglang.srt.layers.moe.topk import select_experts
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +121/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6533 - support eplb for qwen3

- 链接: https://github.com/sgl-project/sglang/pull/6533
- 状态/时间: merged / 2025-05-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `e6f113569e51`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+46/-25，可读 patch 187 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support eplb for qwen3」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「support eplb for qwen3」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +39/-22 (61 lines); hunks: -55,7 +55,7; -67,6 +67,8; symbols: Qwen3MoeSparseMoeBlock, __init__, forward, forward_normal，涉及 `Qwen3MoeSparseMoeBlock, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +39/-22 (61 lines); hunks: -55,7 +55,7; -67,6 +67,8; symbols: Qwen3MoeSparseMoeBlock, __init__, forward, forward_normal
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -55,7 +55,7 @@
-from sglang.srt.layers.moe.ep_moe.layer import DeepEPMoE, EPMoE
+from sglang.srt.layers.moe.ep_moe.layer import get_moe_impl_class
@@ -67,6 +67,8 @@
+from sglang.srt.managers.expert_location import ModelConfigForExpertLocation
+from sglang.srt.managers.expert_location_dispatch import ExpertLocationDispatchInfo
@@ -86,28 +88,25 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +39/-22
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/managers/expert_distribution.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6598 - qwen3moe support two batch overlap

- 链接: https://github.com/sgl-project/sglang/pull/6598
- 状态/时间: merged / 2025-05-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `f9bab3d59100`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+351/-28，可读 patch 515 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「qwen3moe support two batch overlap」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「qwen3moe support two batch overlap」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +200/-11 (211 lines); hunks: -68,6 +68,9; -79,6 +82,7; symbols: __init__, forward_deepep, op_gate, op_select_experts，涉及 `__init__, forward_deepep, op_gate`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +200/-11 (211 lines); hunks: -68,6 +68,9; -79,6 +82,7; symbols: __init__, forward_deepep, op_gate, op_select_experts
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -68,6 +68,9 @@
+from sglang.srt.managers.expert_distribution import (
+    get_global_expert_distribution_recorder,
+)
@@ -79,6 +82,7 @@
+from sglang.srt.two_batch_overlap import MaybeTboDeepEPDispatcher
@@ -137,7 +141,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +200/-11
- 验证与风险: diff 自带测试面 `test/srt/test_two_batch_overlap.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #6652 - Fix qwen3 tbo/dp-lm-head

- 链接: https://github.com/sgl-project/sglang/pull/6652
- 状态/时间: merged / 2025-05-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `b18416fbf869`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+3/-1，可读 patch 25 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix qwen3 tbo/dp-lm-head」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Fix qwen3 tbo/dp-lm-head」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +1/-0 (1 lines); hunks: -688,6 +688,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +1/-0 (1 lines); hunks: -688,6 +688,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -688,6 +688,7 @@ def __init__(
+            use_attn_tp_group=global_server_args_dict["enable_dp_lm_head"],
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/two_batch_overlap.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6709 - Fix PP for Qwen3 MoE

- 链接: https://github.com/sgl-project/sglang/pull/6709
- 状态/时间: merged / 2025-05-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `e06b07610597`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+60/-4，可读 patch 85 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix PP for Qwen3 MoE」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Fix PP for Qwen3 MoE」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +3/-3 (6 lines); hunks: -812,9 +812,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +3/-3 (6 lines); hunks: -812,9 +812,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -812,9 +812,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-            layer_id: layer.mlp.get_moe_weights()
-            for layer_id, layer in enumerate(self.model.layers)
-            if isinstance(layer.mlp, Qwen3MoeSparseMoeBlock)
+            layer_id: self.model.layers[layer_id].mlp.get_moe_weights()
+            for layer_id in range(self.start_layer, self.end_layer)
+            if isinstance(self.model.layers[layer_id].mlp, Qwen3MoeSparseMoeBlock)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +3/-3
- 验证与风险: diff 自带测试面 `test/srt/test_pp_single_node.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #6820 - Fix Qwen3MoE missing token padding optimization

- 链接: https://github.com/sgl-project/sglang/pull/6820
- 状态/时间: merged / 2025-06-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `5aff1e9392d0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+5/-3，可读 patch 49 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Qwen3MoE missing token padding optimization」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Fix Qwen3MoE missing token padding optimization」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +2/-0 (2 lines); hunks: -193,6 +193,7 @@ def forward_deepep(; -260,6 +261,7 @@ def op_select_experts(self, state):; symbols: forward_deepep, op_select_experts，涉及 `forward_deepep, op_select_experts`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +2/-0 (2 lines); hunks: -193,6 +193,7 @@ def forward_deepep(; -260,6 +261,7 @@ def op_select_experts(self, state):; symbols: forward_deepep, op_select_experts
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -193,6 +193,7 @@ def forward_deepep(
+                num_token_non_padded=forward_batch.num_token_non_padded,
@@ -260,6 +261,7 @@ def op_select_experts(self, state):
+                num_token_non_padded=state.forward_batch.num_token_non_padded,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6990 - support qwen3 emebedding

- 链接: https://github.com/sgl-project/sglang/pull/6990
- 状态/时间: merged / 2025-06-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `451ffe74d907`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+3/-0，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support qwen3 emebedding」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「support qwen3 emebedding」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +2/-0 (2 lines); hunks: -333,6 +333,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +2/-0 (2 lines); hunks: -333,6 +333,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -333,6 +333,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+            if "Embedding" in self.config.name_or_path:
+                name = add_prefix(name, "model")
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +2/-0
- 验证与风险: diff 自带测试面 `test/srt/models/test_embedding_models.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #7681 - support qwen3 dense model dp attention

- 链接: https://github.com/sgl-project/sglang/pull/7681
- 状态/时间: merged / 2025-07-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `646cef2e2ea5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+49/-17，可读 patch 139 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support qwen3 dense model dp attention」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「support qwen3 dense model dp attention」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +42/-16 (58 lines); hunks: -14,6 +14,8; -54,18 +56,21 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +42/-16 (58 lines); hunks: -14,6 +14,8; -54,18 +56,21 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -14,6 +14,8 @@
+from sglang.srt.layers.communicator import LayerCommunicator, LayerScatterModes
+from sglang.srt.layers.dp_attention import get_attention_tp_rank, get_attention_tp_size
@@ -54,18 +56,21 @@ def __init__(
-        assert self.total_num_heads % self.tp_size == 0
-        self.num_heads = self.total_num_heads // self.tp_size
+        attn_tp_rank = get_attention_tp_rank()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +42/-16
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2.py`, `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7740 - [optimize] add two stream norm for qwen3

- 链接: https://github.com/sgl-project/sglang/pull/7740
- 状态/时间: merged / 2025-07-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；关联提交 `264dc6e74462`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+54/-10，可读 patch 229 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[optimize] add two stream norm for qwen3」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[optimize] add two stream norm for qwen3」；主要实现面是 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +24/-5 (29 lines); hunks: -23,15 +23,17; -49,6 +51,7 @@ def __init__(; symbols: Qwen3Attention, __init__, _apply_qk_norm，涉及 `Qwen3Attention, __init__, _apply_qk_norm`；`python/sglang/srt/models/qwen3_moe.py` modified +24/-5 (29 lines); hunks: -67,6 +67,7; -76,11 +77,12; symbols: Qwen3MoeSparseMoeBlock, __init__, _apply_qk_norm，涉及 `Qwen3MoeSparseMoeBlock, __init__, _apply_qk_norm`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +24/-5 (29 lines); hunks: -23,15 +23,17; -49,6 +51,7 @@ def __init__(; symbols: Qwen3Attention, __init__, _apply_qk_norm
  - `python/sglang/srt/models/qwen3_moe.py` modified +24/-5 (29 lines); hunks: -67,6 +67,7; -76,11 +77,12; symbols: Qwen3MoeSparseMoeBlock, __init__, _apply_qk_norm
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -23,15 +23,17 @@
+from sglang.srt.model_executor.cuda_graph_runner import get_is_capture_mode
-from sglang.srt.utils import add_prefix
+from sglang.srt.utils import add_prefix, is_cuda
+_is_cuda = is_cuda()
@@ -49,6 +51,7 @@ def __init__(
+        alt_stream: Optional[torch.cuda.Stream] = None,
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -67,6 +67,7 @@
+from sglang.srt.model_executor.cuda_graph_runner import get_is_capture_mode
@@ -76,11 +77,12 @@
-from sglang.srt.utils import DeepEPMode, add_prefix, is_non_idle_and_non_empty
+from sglang.srt.utils import DeepEPMode, add_prefix, is_cuda, is_non_idle_and_non_empty
+_is_cuda = is_cuda()
@@ -352,6 +354,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +24/-5; `python/sglang/srt/models/qwen3_moe.py` modified +24/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7312 - Add get_hidden_dim to qwen3.py for correct lora

- 链接: https://github.com/sgl-project/sglang/pull/7312
- 状态/时间: merged / 2025-07-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `877e35d7754c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+240/-2，可读 patch 296 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add get_hidden_dim to qwen3.py for correct lora」；模型线: Qwen3 Core；类别: 文档/测试/CI；主要 diff: `test/srt/models/lora/test_lora_qwen3.py`, `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「Add get_hidden_dim to qwen3.py for correct lora」；主要实现面是 `test/srt/models/lora/test_lora_qwen3.py`, `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/srt/models/lora/test_lora_qwen3.py` added +209/-0 (209 lines); hunks: -0,0 +1,209; symbols: TestLoRA, _run_lora_multiple_batch_on_model_cases, test_ci_lora_models, test_all_lora_models，涉及 `TestLoRA, _run_lora_multiple_batch_on_model_cases, test_ci_lora_models`；`python/sglang/srt/models/qwen3.py` modified +24/-0 (24 lines); hunks: -330,6 +330,30 @@ def __init__(; symbols: __init__, get_input_embeddings, get_hidden_dim, forward，涉及 `__init__, get_input_embeddings, get_hidden_dim`。
- 代码 diff 细节:
  - `test/srt/models/lora/test_lora_qwen3.py` added +209/-0 (209 lines); hunks: -0,0 +1,209; symbols: TestLoRA, _run_lora_multiple_batch_on_model_cases, test_ci_lora_models, test_all_lora_models
  - `python/sglang/srt/models/qwen3.py` modified +24/-0 (24 lines); hunks: -330,6 +330,30 @@ def __init__(; symbols: __init__, get_input_embeddings, get_hidden_dim, forward
- 关键代码摘录:

```diff
diff -- test/srt/models/lora/test_lora_qwen3.py
@@ -0,0 +1,209 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/qwen3.py
@@ -330,6 +330,30 @@ def __init__(
+    def get_hidden_dim(self, module_name: str) -> Tuple[int]:
+        # return input_dim, output_dim
+        if module_name in ["q_proj", "qkv_proj"]:
+            return (
+                self.config.hidden_size,
+                self.config.head_dim * self.config.num_attention_heads,
```

- 已读文件:
  - tests: `test/srt/models/lora/test_lora_qwen3.py` added +209/-0
  - runtime: `python/sglang/srt/models/qwen3.py` modified +24/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/runners.py`, `test/srt/models/lora/test_lora.py`, `test/srt/models/lora/test_lora_qwen3.py`, `test/srt/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #8751 - [1/3] Optimize Slime Update Weights: Remove QWen3MOE Load Weight Overhead

- 链接: https://github.com/sgl-project/sglang/pull/8751
- 状态/时间: merged / 2025-08-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `89588179cfe4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+26/-6，可读 patch 65 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[1/3] Optimize Slime Update Weights: Remove QWen3MOE Load Weight Overhead」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[1/3] Optimize Slime Update Weights: Remove QWen3MOE Load Weight Overhead」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +26/-6 (32 lines); hunks: -766,7 +766,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -805,11 +808,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: load_weights, get_model_config_for_expert_location，涉及 `load_weights, get_model_config_for_expert_location`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +26/-6 (32 lines); hunks: -766,7 +766,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -805,11 +808,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: load_weights, get_model_config_for_expert_location
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -766,7 +766,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-        params_dict = dict(self.named_parameters())
+        # Cache params_dict to avoid repeated expensive traversal of model parameters
+        if not hasattr(self, "_cached_params_dict"):
+            self._cached_params_dict = dict(self.named_parameters())
+        params_dict = self._cached_params_dict
@@ -805,11 +808,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +26/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9973 - Optimize Qwen3-moe model by using flashinfer fused allreduce

- 链接: https://github.com/sgl-project/sglang/pull/9973
- 状态/时间: merged / 2025-09-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `ec15c8360e73`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+52/-12，可读 patch 157 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Optimize Qwen3-moe model by using flashinfer fused allreduce」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Optimize Qwen3-moe model by using flashinfer fused allreduce」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +39/-8 (47 lines); hunks: -42,7 +42,10; -57,10 +60,17; symbols: forward, get_moe_weights, forward_normal, __init__，涉及 `forward, get_moe_weights, forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +39/-8 (47 lines); hunks: -42,7 +42,10; -57,10 +60,17; symbols: forward, get_moe_weights, forward_normal, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -42,7 +42,10 @@
-from sglang.srt.layers.moe import get_moe_a2a_backend
+from sglang.srt.layers.moe import (
+    get_moe_a2a_backend,
+    should_use_flashinfer_cutlass_moe_fp4_allgather,
+)
@@ -57,10 +60,17 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +39/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10574 - [Ascend]optimize Qwen3 on Ascend

- 链接: https://github.com/sgl-project/sglang/pull/10574
- 状态/时间: merged / 2025-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `e22f3a5ec914`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+81/-2，可读 patch 170 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Ascend]optimize Qwen3 on Ascend」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Ascend]optimize Qwen3 on Ascend」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +18/-2 (20 lines); hunks: -30,12 +30,19; -235,9 +242,18 @@ def forward(; symbols: Qwen3Attention, forward，涉及 `Qwen3Attention, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +18/-2 (20 lines); hunks: -30,12 +30,19; -235,9 +242,18 @@ def forward(; symbols: Qwen3Attention, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -30,12 +30,19 @@
-from sglang.srt.utils import add_prefix, is_cuda
+from sglang.srt.utils import (
+    add_prefix,
+    get_cmo_stream,
+    is_cuda,
+    is_npu,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +18/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/model_executor/model_runner.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10749 - Fuse write kv buffer into rope for qwen3 moe & bailing moe

- 链接: https://github.com/sgl-project/sglang/pull/10749
- 状态/时间: merged / 2025-09-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `a5095d62623f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+105/-34，可读 patch 207 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fuse write kv buffer into rope for qwen3 moe & bailing moe」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Fuse write kv buffer into rope for qwen3 moe & bailing moe」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +22/-2 (24 lines); hunks: -60,6 +60,10; -412,15 +416,31 @@ def forward_prepare(; symbols: forward_prepare, forward_core，涉及 `forward_prepare, forward_core`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +22/-2 (24 lines); hunks: -60,6 +60,10; -412,15 +416,31 @@ def forward_prepare(; symbols: forward_prepare, forward_core
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -60,6 +60,10 @@
+from sglang.srt.models.utils import (
+    create_fused_set_kv_buffer_arg,
+    enable_fused_set_kv_buffer,
+)
@@ -412,15 +416,31 @@ def forward_prepare(
-        q, k = self.rotary_emb(positions, q, k)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +22/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10985 - Quick Fix: fix Qwen3-VL launch failure caused by MRotaryEmbedding arg

- 链接: https://github.com/sgl-project/sglang/pull/10985
- 状态/时间: merged / 2025-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `61305291430a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+14/-2，可读 patch 58 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Quick Fix: fix Qwen3-VL launch failure caused by MRotaryEmbedding arg」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Quick Fix: fix Qwen3-VL launch failure caused by MRotaryEmbedding arg」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +10/-2 (12 lines); hunks: -51,7 +51,7; -358,6 +358,10 @@ def __init__(; symbols: __init__, forward_prepare, forward_core，涉及 `__init__, forward_prepare, forward_core`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +10/-2 (12 lines); hunks: -51,7 +51,7; -358,6 +358,10 @@ def __init__(; symbols: __init__, forward_prepare, forward_core
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -51,7 +51,7 @@
-from sglang.srt.layers.rotary_embedding import get_rope
+from sglang.srt.layers.rotary_embedding import MRotaryEmbedding, get_rope
@@ -358,6 +358,10 @@ def __init__(
+        self.compatible_with_fused_kv_buffer = (
+            False if isinstance(self.rotary_emb, MRotaryEmbedding) else True
+        )
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +10/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10911 - model: qwen3-omni (thinker-only)

- 链接: https://github.com/sgl-project/sglang/pull/10911
- 状态/时间: merged / 2025-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `86b04d25b3f6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 16 个文件，+1947/-328，可读 patch 2837 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「model: qwen3-omni (thinker-only)」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「model: qwen3-omni (thinker-only)」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +2/-1 (3 lines); hunks: -661,13 +661,14 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +2/-1 (3 lines); hunks: -661,13 +661,14 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -661,13 +661,14 @@ def __init__(
+        decoder_layer_type=Qwen3MoeDecoderLayer,
-            decoder_layer_type=Qwen3MoeDecoderLayer,
+            decoder_layer_type=decoder_layer_type,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +2/-1
- 验证与风险: diff 自带测试面 `test/srt/test_vision_openai_server_a.py`, `test/srt/test_vision_openai_server_b.py`, `test/srt/test_vision_openai_server_common.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #12002 - Eagle3 DP attention for Qwen3 MoE

- 链接: https://github.com/sgl-project/sglang/pull/12002
- 状态/时间: merged / 2025-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `750940ae3660`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+219/-27，可读 patch 372 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Eagle3 DP attention for Qwen3 MoE」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Eagle3 DP attention for Qwen3 MoE」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +16/-8 (24 lines); hunks: -539,10 +539,16 @@ def forward(; -774,13 +780,15 @@ def set_eagle3_layers_to_capture(self, layer_ids: Optional...; symbols: forward, set_eagle3_layers_to_capture, load_weights，涉及 `forward, set_eagle3_layers_to_capture, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +16/-8 (24 lines); hunks: -539,10 +539,16 @@ def forward(; -774,13 +780,15 @@ def set_eagle3_layers_to_capture(self, layer_ids: Optional...; symbols: forward, set_eagle3_layers_to_capture, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -539,10 +539,16 @@ def forward(
+        captured_last_layer_outputs: Optional[List[torch.Tensor]] = None,
-        hidden_states, residual = self.layer_communicator.prepare_attn(
-            hidden_states, residual, forward_batch
+        hidden_states, residual = (
+            self.layer_communicator.prepare_attn_and_capture_last_layer_outputs(
+                hidden_states,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +16/-8
- 验证与风险: diff 自带测试面 `python/sglang/test/test_utils.py`, `test/srt/run_suite.py`, `test/srt/test_eagle_dp_attention.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #13489 - Flashinfer TRTLLM-GEN-MoE + Qwen3

- 链接: https://github.com/sgl-project/sglang/pull/13489
- 状态/时间: merged / 2025-11-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `92ad2ff9ce0e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+43/-1，可读 patch 72 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Flashinfer TRTLLM-GEN-MoE + Qwen3」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Flashinfer TRTLLM-GEN-MoE + Qwen3」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +2/-0 (2 lines); hunks: -49,6 +49,7; -111,6 +112,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +2/-0 (2 lines); hunks: -49,6 +49,7; -111,6 +112,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -49,6 +49,7 @@
+from sglang.srt.layers.moe.utils import RoutingMethodType
@@ -111,6 +112,7 @@ def __init__(
+            routing_method_type=RoutingMethodType.Renormalize,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/server_args.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13998 - [apply][2/2] Fused qk_norm_rope for Qwen3-MoE

- 链接: https://github.com/sgl-project/sglang/pull/13998
- 状态/时间: merged / 2025-12-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `26d95008b65b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+199/-22，可读 patch 317 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[apply][2/2] Fused qk_norm_rope for Qwen3-MoE」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[apply][2/2] Fused qk_norm_rope for Qwen3-MoE」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +193/-22 (215 lines); hunks: -18,10 +18,12; -73,6 +75,13; symbols: compute_yarn_parameters, get_mscale, find_correction_dim, find_correction_range，涉及 `compute_yarn_parameters, get_mscale, find_correction_dim`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +193/-22 (215 lines); hunks: -18,10 +18,12; -73,6 +75,13; symbols: compute_yarn_parameters, get_mscale, find_correction_dim, find_correction_range
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -18,10 +18,12 @@
-from typing import Any, Dict, Iterable, List, Optional, Tuple
+import math
+from typing import Any, Dict, Iterable, List, Optional, Tuple, TypeVar
+from transformers import PretrainedConfig
@@ -73,6 +75,13 @@
+_is_cuda = is_cuda()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +193/-22
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/server_args.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #15223 - [bug fix][pp] fix qwen3 model load

- 链接: https://github.com/sgl-project/sglang/pull/15223
- 状态/时间: merged / 2025-12-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `e9abb52576ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-3，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[bug fix][pp] fix qwen3 model load」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[bug fix][pp] fix qwen3 model load」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +3/-3 (6 lines); hunks: -392,13 +392,13 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +3/-3 (6 lines); hunks: -392,13 +392,13 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -392,13 +392,13 @@ def __init__(
-                    self.model.embed_tokens.weight, dst=self.pp_group.last_rank
+                    self.model.embed_tokens.weight, dst=self.pp_group.world_size - 1
-                    size=(config.vocab_size, config.hidden_size),
+                    size=self.lm_head.weight.shape,
-                    src=self.pp_group.first_rank,
+                    src=0,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +3/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #15390 - [NPU]qwen3 pp bugfix

- 链接: https://github.com/sgl-project/sglang/pull/15390
- 状态/时间: merged / 2025-12-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；关联提交 `8bf7f240b654`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-3，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]qwen3 pp bugfix」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[NPU]qwen3 pp bugfix」；主要实现面是 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +3/-2 (5 lines); hunks: -167,10 +167,10 @@ def forward_prepare_native(self, positions, hidden_states):; -205,6 +205,7 @@ def forward(; symbols: forward_prepare_native, forward_prepare_npu, forward，涉及 `forward_prepare_native, forward_prepare_npu, forward`；`python/sglang/srt/models/qwen3_moe.py` modified +1/-1 (2 lines); hunks: -542,7 +542,7 @@ def forward_prepare_npu(; symbols: forward_prepare_npu，涉及 `forward_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +3/-2 (5 lines); hunks: -167,10 +167,10 @@ def forward_prepare_native(self, positions, hidden_states):; -205,6 +205,7 @@ def forward(; symbols: forward_prepare_native, forward_prepare_npu, forward
  - `python/sglang/srt/models/qwen3_moe.py` modified +1/-1 (2 lines); hunks: -542,7 +542,7 @@ def forward_prepare_npu(; symbols: forward_prepare_npu
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -167,10 +167,10 @@ def forward_prepare_native(self, positions, hidden_states):
-    def forward_prepare_npu(self, positions, hidden_states):
+    def forward_prepare_npu(self, positions, hidden_states, forward_batch):
-        if self.attn.layer_id == 0:
+        if self.attn.layer_id == forward_batch.token_to_kv_pool.start_layer:
@@ -205,6 +205,7 @@ def forward(
+                forward_batch=forward_batch,
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -542,7 +542,7 @@ def forward_prepare_npu(
-        if self.attn.layer_id == 0:
+        if self.attn.layer_id == forward_batch.token_to_kv_pool.start_layer:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +3/-2; `python/sglang/srt/models/qwen3_moe.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16115 - [NPU][Bugfix] Fix qwen3 error when enable-dp-lm-head

- 链接: https://github.com/sgl-project/sglang/pull/16115
- 状态/时间: merged / 2026-01-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；关联提交 `7dd679cbb93a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+52/-16，可读 patch 166 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU][Bugfix] Fix qwen3 error when enable-dp-lm-head」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[NPU][Bugfix] Fix qwen3 error when enable-dp-lm-head」；主要实现面是 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +4/-3 (7 lines); hunks: -161,12 +161,12 @@ def forward_prepare_npu(self, positions, hidden_states, fo...; -372,6 +372,7 @@ def __init__(; symbols: forward_prepare_npu, __init__，涉及 `forward_prepare_npu, __init__`；`python/sglang/srt/models/qwen3_moe.py` modified +3/-3 (6 lines); hunks: -523,12 +523,12 @@ def forward_prepare_npu(; symbols: forward_prepare_npu，涉及 `forward_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +4/-3 (7 lines); hunks: -161,12 +161,12 @@ def forward_prepare_npu(self, positions, hidden_states, fo...; -372,6 +372,7 @@ def __init__(; symbols: forward_prepare_npu, __init__
  - `python/sglang/srt/models/qwen3_moe.py` modified +3/-3 (6 lines); hunks: -523,12 +523,12 @@ def forward_prepare_npu(; symbols: forward_prepare_npu
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -161,12 +161,12 @@ def forward_prepare_npu(self, positions, hidden_states, forward_batch):
-            self.q_norm.weight,
-            self.k_norm.weight,
-            self.q_norm.variance_epsilon,
+            eps=self.q_norm.variance_epsilon,
+            q_weight=self.q_norm.weight,
+            k_weight=self.k_norm.weight,
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -523,12 +523,12 @@ def forward_prepare_npu(
-            self.q_norm.weight,
-            self.k_norm.weight,
-            self.q_norm.variance_epsilon,
+            eps=self.q_norm.variance_epsilon,
+            q_weight=self.q_norm.weight,
+            k_weight=self.k_norm.weight,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +4/-3; `python/sglang/srt/models/qwen3_moe.py` modified +3/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py`, `python/sglang/srt/models/llama.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #15904 - [NPU] NZ for non-quantized MOE, Qwen3 MOE double memory consumption fix

- 链接: https://github.com/sgl-project/sglang/pull/15904
- 状态/时间: merged / 2026-01-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `b77b0ffd6021`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+111/-49，可读 patch 296 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] NZ for non-quantized MOE, Qwen3 MOE double memory consumption fix」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[NPU] NZ for non-quantized MOE, Qwen3 MOE double memory consumption fix」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +10/-7 (17 lines); hunks: -71,6 +71,7; -1119,14 +1120,16 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights, get_model_config_for_expert_location，涉及 `load_weights, get_model_config_for_expert_location`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +10/-7 (17 lines); hunks: -71,6 +71,7; -1119,14 +1120,16 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights, get_model_config_for_expert_location
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -71,6 +71,7 @@
+    LazyValue,
@@ -1119,14 +1120,16 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-        # TODO mimic deepseek
-        # Lazy initialization of expert weights cache to avoid slowing down load_weights
-            self.routed_experts_weights_of_layer = {
-                layer_id: self.model.layers[layer_id].mlp.get_moe_weights()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +10/-7
- 验证与风险: diff 自带测试面 `test/registered/ascend/test_ascend_memory_consumption.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17535 - Update weight rename check for Qwen3 Embeddings

- 链接: https://github.com/sgl-project/sglang/pull/17535
- 状态/时间: merged / 2026-02-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `793bf9fc0649`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update weight rename check for Qwen3 Embeddings」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「Update weight rename check for Qwen3 Embeddings」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +5/-1 (6 lines); hunks: -490,7 +490,11 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +5/-1 (6 lines); hunks: -490,7 +490,11 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -490,7 +490,11 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-            if "Embedding" in self.config.name_or_path:
+            if not name.startswith("model.") and (
+                name.startswith("layers.")
+                or name.startswith("embed_tokens.")
+                or name.startswith("norm.")
+            ):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18189 - [ModelOpt] Fix broken Qwen3-235B-A22B-Instruct-2507-NVFP4 launch

- 链接: https://github.com/sgl-project/sglang/pull/18189
- 状态/时间: merged / 2026-02-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `ca36d88fa640`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-0，可读 patch 15 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ModelOpt] Fix broken Qwen3-235B-A22B-Instruct-2507-NVFP4 launch」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[ModelOpt] Fix broken Qwen3-235B-A22B-Instruct-2507-NVFP4 launch」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +8/-0 (8 lines); hunks: -890,6 +890,14 @@ def __init__(; symbols: __init__, Qwen3MoeForCausalLM，涉及 `__init__, Qwen3MoeForCausalLM`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +8/-0 (8 lines); hunks: -890,6 +890,14 @@ def __init__(; symbols: __init__, Qwen3MoeForCausalLM
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -890,6 +890,14 @@ def __init__(
+    # Mapping from fused module names to their component weight names.
+    # Required for quantization configs (e.g., ModelOpt FP4) to correctly identify
+    # which layers should be skipped based on the exclude_modules/ignore list.
+    packed_modules_mapping = {
+        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
+        "gate_up_proj": ["gate_proj", "up_proj"],
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +8/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19532 - [NPU] bugs fix: fix a condition bug when using speculative inference on Qwen3 and Qwen3 moe

- 链接: https://github.com/sgl-project/sglang/pull/19532
- 状态/时间: merged / 2026-03-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；关联提交 `365ca1edb5af`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+8/-2，可读 patch 24 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] bugs fix: fix a condition bug when using speculative inference on Qwen3 and Qwen3 moe」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[NPU] bugs fix: fix a condition bug when using speculative inference on Qwen3 and Qwen3 moe」；主要实现面是 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +4/-1 (5 lines); hunks: -181,7 +181,10 @@ def forward(; symbols: forward，涉及 `forward`；`python/sglang/srt/models/qwen3_moe.py` modified +4/-1 (5 lines); hunks: -620,7 +620,10 @@ def forward_prepare(; symbols: forward_prepare，涉及 `forward_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +4/-1 (5 lines); hunks: -181,7 +181,10 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/qwen3_moe.py` modified +4/-1 (5 lines); hunks: -620,7 +620,10 @@ def forward_prepare(; symbols: forward_prepare
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -181,7 +181,10 @@ def forward(
-        if not _is_npu or forward_batch.forward_mode.is_extend():
+        if (
+            not _is_npu
+            or forward_batch.forward_mode.is_extend_or_draft_extend_or_mixed()
+        ):
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -620,7 +620,10 @@ def forward_prepare(
-        if not _is_npu or forward_batch.forward_mode.is_extend():
+        if (
+            not _is_npu
+            or forward_batch.forward_mode.is_extend_or_draft_extend_or_mixed()
+        ):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +4/-1; `python/sglang/srt/models/qwen3_moe.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20931 - [Bugifx] qwen3 rope parameter compatibility

- 链接: https://github.com/sgl-project/sglang/pull/20931
- 状态/时间: merged / 2026-03-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `46a76af97bec`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-3，可读 patch 28 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugifx] qwen3 rope parameter compatibility」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[Bugifx] qwen3 rope parameter compatibility」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +4/-3 (7 lines); hunks: -78,6 +78,7; -566,7 +567,7 @@ def forward_prepare_native(; symbols: forward_prepare_native, apply_qk_norm_rope, __init__，涉及 `forward_prepare_native, apply_qk_norm_rope, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +4/-3 (7 lines); hunks: -78,6 +78,7; -566,7 +567,7 @@ def forward_prepare_native(; symbols: forward_prepare_native, apply_qk_norm_rope, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -78,6 +78,7 @@
+from sglang.srt.utils.hf_transformers_utils import get_rope_config
@@ -566,7 +567,7 @@ def forward_prepare_native(
-            theta = self.config.rope_parameters["rope_theta"]
+            theta = self.rope_theta
@@ -691,8 +692,8 @@ def __init__(
-        rope_theta = config.rope_parameters["rope_theta"]
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +4/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18233 - Support Qwen3 MoE context parallel

- 链接: https://github.com/sgl-project/sglang/pull/18233
- 状态/时间: merged / 2026-03-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `bb737d7a829b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 19 个文件，+968/-73，可读 patch 1552 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support Qwen3 MoE context parallel」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Support Qwen3 MoE context parallel」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +35/-5 (40 lines); hunks: -26,11 +26,14; -59,6 +62,11; symbols: __init__, forward_normal, get_input_embeddings, forward，涉及 `__init__, forward_normal, get_input_embeddings`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +35/-5 (40 lines); hunks: -26,11 +26,14; -59,6 +62,11; symbols: __init__, forward_normal, get_input_embeddings, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -26,11 +26,14 @@
+    get_attn_context_model_parallel_rank,
+    get_attn_context_model_parallel_world_size,
+    get_moe_data_parallel_world_size,
+    get_moe_tensor_parallel_world_size,
-    get_tensor_model_parallel_world_size,
-    tensor_model_parallel_all_reduce,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +35/-5
- 验证与风险: diff 自带测试面 `python/sglang/test/attention/test_flashattn_backend.py`, `test/registered/4-gpu-models/test_qwen3_30b.py`, `test/registered/8-gpu-models/test_qwen3_235b.py`, `test/registered/unit/managers/test_prefill_adder.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21195 - Enable the qwen3 test

- 链接: https://github.com/sgl-project/sglang/pull/21195
- 状态/时间: merged / 2026-03-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `dac148167c80`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+6/-5，可读 patch 32 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable the qwen3 test」；模型线: Qwen3 Core；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Enable the qwen3 test」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +4/-0 (4 lines); hunks: -33,6 +33,7; -321,6 +322,9 @@ def forward_normal(; symbols: forward_normal，涉及 `forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +4/-0 (4 lines); hunks: -33,6 +33,7; -321,6 +322,9 @@ def forward_normal(; symbols: forward_normal
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -33,6 +33,7 @@
+    moe_expert_parallel_all_reduce,
@@ -321,6 +322,9 @@ def forward_normal(
+        if self.ep_size > 1 and not should_allreduce_fusion:
+            final_hidden_states = moe_expert_parallel_all_reduce(final_hidden_states)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +4/-0
- 验证与风险: diff 自带测试面 `test/registered/4-gpu-models/test_qwen3_30b.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21458 - [AMD] Optimize Qwen3-VL decode - fuse QK-norm + 3D mRoPE + KV cache write

- 链接: https://github.com/sgl-project/sglang/pull/21458
- 状态/时间: merged / 2026-04-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `912494f59665`, `a188208e9a03`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+101/-3，可读 patch 152 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Optimize Qwen3-VL decode - fuse QK-norm + 3D mRoPE + KV cache write」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[AMD] Optimize Qwen3-VL decode - fuse QK-norm + 3D mRoPE + KV cache write」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +101/-3 (104 lines); hunks: -19,6 +19,7; -30,13 +31,25; symbols: __init__, forward_prepare_native, forward_prepare_npu, forward_prepare_aiter_fused_mrope，涉及 `__init__, forward_prepare_native, forward_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +101/-3 (104 lines); hunks: -19,6 +19,7; -30,13 +31,25; symbols: __init__, forward_prepare_native, forward_prepare_npu, forward_prepare_aiter_fused_mrope
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -19,6 +19,7 @@
+from sglang.srt.layers.rotary_embedding.mrope import MRotaryEmbedding
@@ -30,13 +31,25 @@
-from sglang.srt.utils import add_prefix, is_cuda, is_npu
+from sglang.srt.utils import add_prefix, get_bool_env_var, is_cuda, is_hip, is_npu
+_is_hip = is_hip()
+_use_aiter = get_bool_env_var("SGLANG_USE_AITER") and _is_hip
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +101/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22739 - Restore Qwen3 rope config fallback

- 链接: https://github.com/sgl-project/sglang/pull/22739
- 状态/时间: merged / 2026-04-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `520ce526b919`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-2，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Restore Qwen3 rope config fallback」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「Restore Qwen3 rope config fallback」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +10/-2 (12 lines); hunks: -316,8 +316,16 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +10/-2 (12 lines); hunks: -316,8 +316,16 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -316,8 +316,16 @@ def __init__(
-        rope_theta = config.rope_parameters["rope_theta"]
-        rope_scaling = config.rope_parameters
+        if (
+            hasattr(config, "rope_parameters")
+            and config.rope_parameters
+            and "rope_theta" in config.rope_parameters
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +10/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23731 - Fix Qwen3 MoE double-reduce when DP attention + EP + reduce_scatterv (#23729)

- 链接: https://github.com/sgl-project/sglang/pull/23731
- 状态/时间: merged / 2026-04-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `71029abd640f`, `99b59b279ce2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-1，可读 patch 29 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Qwen3 MoE double-reduce when DP attention + EP + reduce_scatterv (#23729)」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Fix Qwen3 MoE double-reduce when DP attention + EP + reduce_scatterv (#23729)」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +7/-1 (8 lines); hunks: -50,6 +50,7; -331,14 +332,19 @@ def forward_normal(; symbols: forward_normal，涉及 `forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +7/-1 (8 lines); hunks: -50,6 +50,7; -331,14 +332,19 @@ def forward_normal(; symbols: forward_normal
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -50,6 +50,7 @@
+    should_use_dp_reduce_scatterv,
@@ -331,14 +332,19 @@ def forward_normal(
-        if self.ep_size > 1 and not should_allreduce_fusion:
+        if (
+            self.ep_size > 1
+            and not should_allreduce_fusion
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +7/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23734 - Fix Qwen3 MoE: also guard EP all-reduce with not use_reduce_scatter (follow-up to #23731)

- 链接: https://github.com/sgl-project/sglang/pull/23734
- 状态/时间: merged / 2026-04-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `71029abd640f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Qwen3 MoE: also guard EP all-reduce with not use_reduce_scatter (follow-up to #23731)」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Fix Qwen3 MoE: also guard EP all-reduce with not use_reduce_scatter (follow-up to #23731)」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +1/-0 (1 lines); hunks: -335,6 +335,7 @@ def forward_normal(; symbols: forward_normal，涉及 `forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +1/-0 (1 lines); hunks: -335,6 +335,7 @@ def forward_normal(; symbols: forward_normal
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -335,6 +335,7 @@ def forward_normal(
+            and not use_reduce_scatter
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20520 - [NPU]TP Communications compression For Qwen3 models for NPU

- 链接: https://github.com/sgl-project/sglang/pull/20520
- 状态/时间: merged / 2026-05-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `83bf5d6869c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+191/-10，可读 patch 346 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]TP Communications compression For Qwen3 models for NPU」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[NPU]TP Communications compression For Qwen3 models for NPU」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +1/-1 (2 lines); hunks: -419,7 +419,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +1/-1 (2 lines); hunks: -419,7 +419,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -419,7 +419,7 @@ def forward(
-        hidden_states = self.mlp(hidden_states)
+        hidden_states = self.mlp(hidden_states, forward_batch=forward_batch)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/registered/ascend/llm_models/test_npu_llama_2_7b_communications_compression.py`, `test/registered/ascend/llm_models/test_npu_qwen3_8b_communications_quantization.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26468 - [Model] Add Qwen3-MoE MTP

- 链接: https://github.com/sgl-project/sglang/pull/26468
- 状态/时间: merged / 2026-05-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_moe_mtp.py`；关联提交 `cf66693b3530`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+163/-4，可读 patch 206 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add Qwen3-MoE MTP」；模型线: Qwen3 Core；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_moe_mtp.py`, `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[Model] Add Qwen3-MoE MTP」；主要实现面是 `python/sglang/srt/models/qwen3_moe_mtp.py`, `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe_mtp.py` added +131/-0 (131 lines); hunks: -0,0 +1,131; symbols: Qwen3MoeForCausalLMMTP, __init__, set_embed_and_head, forward，涉及 `Qwen3MoeForCausalLMMTP, __init__, set_embed_and_head`；`python/sglang/srt/models/qwen3_moe.py` modified +18/-1 (19 lines); hunks: -1111,7 +1111,9 @@ def set_dflash_layers_to_capture(self, layer_ids: List[int]):; -1132,6 +1134,21 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: set_dflash_layers_to_capture, load_weights，涉及 `set_dflash_layers_to_capture, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe_mtp.py` added +131/-0 (131 lines); hunks: -0,0 +1,131; symbols: Qwen3MoeForCausalLMMTP, __init__, set_embed_and_head, forward
  - `python/sglang/srt/models/qwen3_moe.py` modified +18/-1 (19 lines); hunks: -1111,7 +1111,9 @@ def set_dflash_layers_to_capture(self, layer_ids: List[int]):; -1132,6 +1134,21 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: set_dflash_layers_to_capture, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe_mtp.py
@@ -0,0 +1,131 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -1111,7 +1111,9 @@ def set_dflash_layers_to_capture(self, layer_ids: List[int]):
-    def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+    def load_weights(
+        self, weights: Iterable[Tuple[str, torch.Tensor]], is_mtp: bool = False
+    ):
@@ -1132,6 +1134,21 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+            if is_mtp:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe_mtp.py` added +131/-0; `python/sglang/srt/models/qwen3_moe.py` modified +18/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_moe_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26798 - Make qwen3's set_embed_and_head idempotent

- 链接: https://github.com/sgl-project/sglang/pull/26798
- 状态/时间: merged / 2026-05-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `13ca55afa3f8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-2，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Make qwen3's set_embed_and_head idempotent」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「Make qwen3's set_embed_and_head idempotent」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +4/-2 (6 lines); hunks: -674,8 +674,10 @@ def get_embed_and_head(self):; symbols: get_embed_and_head, set_embed_and_head，涉及 `get_embed_and_head, set_embed_and_head`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +4/-2 (6 lines); hunks: -674,8 +674,10 @@ def get_embed_and_head(self):; symbols: get_embed_and_head, set_embed_and_head
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -674,8 +674,10 @@ def get_embed_and_head(self):
-        del self.model.embed_tokens.weight
-        del self.lm_head.weight
+        if hasattr(self.model.embed_tokens, "weight"):
+            del self.model.embed_tokens.weight
+        if hasattr(self.lm_head, "weight"):
+            del self.lm_head.weight
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +4/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #29505 - [NPU] Qwen3-VL-30B use split_qkv_rmsnorm_rope for extend

- 链接: https://github.com/sgl-project/sglang/pull/29505
- 状态/时间: merged / 2026-06-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `f85cc94d82a5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-4，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Qwen3-VL-30B use split_qkv_rmsnorm_rope for extend」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[NPU] Qwen3-VL-30B use split_qkv_rmsnorm_rope for extend」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +1/-4 (5 lines); hunks: -661,10 +661,7 @@ def forward_prepare(; symbols: forward_prepare，涉及 `forward_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +1/-4 (5 lines); hunks: -661,10 +661,7 @@ def forward_prepare(; symbols: forward_prepare
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -661,10 +661,7 @@ def forward_prepare(
-        if (
-            not _is_npu
-            or forward_batch.forward_mode.is_extend_or_draft_extend_or_mixed()
-        ):
+        if not _is_npu:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +1/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #29627 - [NPU] Qwen3-VL-8B use split_qkv_rmsnorm_rope for extend

- 链接: https://github.com/sgl-project/sglang/pull/29627
- 状态/时间: merged / 2026-06-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `ff51acd67b22`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-4，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Qwen3-VL-8B use split_qkv_rmsnorm_rope for extend」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[NPU] Qwen3-VL-8B use split_qkv_rmsnorm_rope for extend」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +1/-4 (5 lines); hunks: -287,10 +287,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +1/-4 (5 lines); hunks: -287,10 +287,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -287,10 +287,7 @@ def forward(
-        elif (
-            not _is_npu
-            or forward_batch.forward_mode.is_extend_or_draft_extend_or_mixed()
-        ):
+        elif not _is_npu:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +1/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31171 - [CPU] add fused input proj for qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/31171
- 状态/时间: merged / 2026-07-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/cpu/test_qwen3.py`；关联提交 `41e0b4b3695e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+238/-94，可读 patch 471 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CPU] add fused input proj for qwen3.5」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `test/registered/cpu/test_qwen3.py`；技术摘要: 覆盖「[CPU] add fused input proj for qwen3.5」；主要实现面是 `test/registered/cpu/test_qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/cpu/test_qwen3.py` modified +82/-58 (140 lines); hunks: -1,10 +1,11; -85,69 +86,92 @@ def fix_query_key_value_ordering_reshape_cat_contiguous(; symbols: fix_query_key_value_ordering_reshape_cat_contiguous, TestQwen3, test_fused_qkvzba_split_reshape_cat, test_fused_input_proj，涉及 `fix_query_key_value_ordering_reshape_cat_contiguous, TestQwen3, test_fused_qkvzba_split_reshape_cat`。
- 代码 diff 细节:
  - `test/registered/cpu/test_qwen3.py` modified +82/-58 (140 lines); hunks: -1,10 +1,11; -85,69 +86,92 @@ def fix_query_key_value_ordering_reshape_cat_contiguous(; symbols: fix_query_key_value_ordering_reshape_cat_contiguous, TestQwen3, test_fused_qkvzba_split_reshape_cat, test_fused_input_proj
- 关键代码摘录:

```diff
diff -- test/registered/cpu/test_qwen3.py
@@ -1,10 +1,11 @@
-import unittest
+import sys
+import pytest
+from sglang.srt.utils import is_host_cpu_arm64
-from sglang.test.test_utils import CustomTestCase
@@ -85,69 +86,92 @@ def fix_query_key_value_ordering_reshape_cat_contiguous(
```

- 已读文件:
  - tests: `test/registered/cpu/test_qwen3.py` modified +82/-58
- 验证与风险: diff 自带测试面 `test/registered/cpu/test_qwen3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30768 - :sparkles: [llm][npu][quant] Add W8A8 MXFP8 quantization for Qwen3 MoE on Ascend NPU

- 链接: https://github.com/sgl-project/sglang/pull/30768
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `f05c92fb6d65`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 18 个文件，+627/-42，可读 patch 888 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「:sparkles: [llm][npu][quant] Add W8A8 MXFP8 quantization for Qwen3 MoE on Ascend NPU」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「:sparkles: [llm][npu][quant] Add W8A8 MXFP8 quantization for Qwen3 MoE on Ascend NPU」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +11/-1 (12 lines); hunks: -271,11 +271,21 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +11/-1 (12 lines); hunks: -271,11 +271,21 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -271,11 +271,21 @@ def __init__(
+        # Router gate: description-driven quant, mirroring vllm-ascend. Only the
+        # offline ModelSlim path (which carries a per-layer quant_model_description)
+        # may quantise the gate — if the checkpoint stored it as MXFP8 it is loaded
+        # and dequantised correctly instead of cast to bf16 without its block scale.
+        # The online Fp8/mxfp8 path keeps the gate in bf16 (unchanged, verified).
+        gate_quant_config = (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +11/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/hardware_backend/npu/moe/init_routing.py`, `python/sglang/srt/hardware_backend/npu/moe/matmul.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34006 - Fix Qwen3-MoE producing garbage with the mori a2a backend

- 链接: https://github.com/sgl-project/sglang/pull/34006
- 状态/时间: merged / 2026-08-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `cea16bf22933`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Qwen3-MoE producing garbage with the mori a2a backend」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「Fix Qwen3-MoE producing garbage with the mori a2a backend」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +1/-0 (1 lines); hunks: -300,6 +300,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +1/-0 (1 lines); hunks: -300,6 +300,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -300,6 +300,7 @@ def forward(
+            and not get_moe_a2a_backend().is_mori()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34810 - fix(qwen3): support DeepEP-class backends and early EPLB state

- 链接: https://github.com/sgl-project/sglang/pull/34810
- 状态/时间: merged / 2026-08-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `d8399af70cf6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-3，可读 patch 42 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(qwen3): support DeepEP-class backends and early EPLB state」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「fix(qwen3): support DeepEP-class backends and early EPLB state」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +11/-3 (14 lines); hunks: -52,6 +52,7; -284,7 +285,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +11/-3 (14 lines); hunks: -52,6 +52,7; -284,7 +285,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -52,6 +52,7 @@
+    is_deepep_class_backend,
@@ -284,7 +285,7 @@ def __init__(
-        if get_moe_a2a_backend().is_deepep():
+        if is_deepep_class_backend():
@@ -299,8 +300,7 @@ def forward(
-            not get_moe_a2a_backend().is_deepep()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +11/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #39126 - [Qwen3.8] Enable NVIDIA NVFP4 on DGX Spark with file-backed PLE and PDL router fix

- 链接: https://github.com/sgl-project/sglang/pull/39126
- 状态/时间: merged / 2026-09-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py`；关联提交 `cebca698e2da`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 21 个文件，+1376/-31，可读 patch 1715 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3.8] Enable NVIDIA NVFP4 on DGX Spark with file-backed PLE and PDL router fix」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py`；技术摘要: 覆盖「[Qwen3.8] Enable NVIDIA NVFP4 on DGX Spark with file-backed PLE and PDL router fix」；主要实现面是 `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py` modified +45/-2 (47 lines); hunks: -10,12 +10,25; -38,8 +51,38 @@ def _qwen3_moe_family_overrides(server_args: Any, hf_config:...; symbols: _mixed_precision_moe_quant_algos, _qwen3_moe_family_overrides，涉及 `_mixed_precision_moe_quant_algos, _qwen3_moe_family_overrides`。
- 代码 diff 细节:
  - `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py` modified +45/-2 (47 lines); hunks: -10,12 +10,25; -38,8 +51,38 @@ def _qwen3_moe_family_overrides(server_args: Any, hf_config:...; symbols: _mixed_precision_moe_quant_algos, _qwen3_moe_family_overrides
- 关键代码摘录:

```diff
diff -- python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py
@@ -10,12 +10,25 @@
+from sglang.srt.environ import envs
+def _mixed_precision_moe_quant_algos(hf_config: Any) -> set:
+    """quant_algo values ModelOpt MIXED_PRECISION assigns to `*.experts` layers."""
+    quantization_config = getattr(hf_config, "quantization_config", None)
+    if not isinstance(quantization_config, dict):
+        return set()
```

- 已读文件:
  - runtime: `python/sglang/srt/arg_groups/model_overrides/qwen3_moe.py` modified +45/-2
- 验证与风险: diff 自带测试面 `test/registered/kernel/embeddings/test_qwen4_ple_offload.py`, `test/registered/unit/layers/quantization/test_fp8_moe_runner_fallback.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`, `test/registered/unit/models/test_qwen4_exp_ple_table.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40870 - [Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE

- 链接: https://github.com/sgl-project/sglang/pull/40870
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `e1048a215ce9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+190/-74，可读 patch 324 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE」；模型线: Qwen3 Core；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +3/-23 (26 lines); hunks: -63,7 +63,7; -907,29 +907,9 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +3/-23 (26 lines); hunks: -63,7 +63,7; -907,29 +907,9 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -63,7 +63,7 @@
-from sglang.srt.runtime_context import get_exec, get_forward, get_parallel, get_stream
+from sglang.srt.runtime_context import get_exec, get_parallel, get_stream
@@ -907,29 +907,9 @@ def forward(
-        fuse_mlp_allreduce = (
-            self.layer_communicator.should_fuse_mlp_allreduce_with_next_layer(
-                forward_batch
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +3/-23
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/test_communicator_ffn_exit.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40190 - [XPU] Enable fused QK-norm + RoPE for Qwen3-MoE

- 链接: https://github.com/sgl-project/sglang/pull/40190
- 状态/时间: merged / 2026-10-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `9631f6f2d085`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+130/-6，可读 patch 169 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU] Enable fused QK-norm + RoPE for Qwen3-MoE」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[XPU] Enable fused QK-norm + RoPE for Qwen3-MoE」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +29/-6 (35 lines); hunks: -77,17 +77,21; -573,12 +577,17 @@ def __init__(; symbols: __init__, apply_qk_norm_rope，涉及 `__init__, apply_qk_norm_rope`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +29/-6 (35 lines); hunks: -77,17 +77,21; -573,12 +577,17 @@ def __init__(; symbols: __init__, apply_qk_norm_rope
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -77,17 +77,21 @@
+    is_xpu,
+_is_xpu = is_xpu()
+if _is_xpu:
+    from sgl_kernel import fused_inplace_qknorm_rope
@@ -573,12 +577,17 @@ def __init__(
-            and _is_cuda
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +29/-6
- 验证与风险: diff 自带测试面 `test/registered/xpu/test_fused_inplace_qknorm_rope_xpu.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43551 - [Docs] Document Qwen3-4B/8B H200 mixed-chunk latency tradeoffs

- 链接: https://github.com/sgl-project/sglang/pull/43551
- 状态/时间: merged / 2026-10-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`；关联提交 `587b6d622d16`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Document Qwen3-4B/8B H200 mixed-chunk latency tradeoffs」；模型线: Qwen3 Core；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`；技术摘要: 覆盖「[Docs] Document Qwen3-4B/8B H200 mixed-chunk latency tradeoffs」；主要实现面是 `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0 (1 lines); hunks: -45,6 +45,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/...。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0 (1 lines); hunks: -45,6 +45,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/...
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.mdx
@@ -45,6 +45,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/qwen3-deployment.j
+- **Qwen3-4B and Qwen3-8B on H200:** For concurrent requests with long prompts, benchmark `--enable-mixed-chunk` to mix decode requests into chunked-prefill batches. This can redu
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #43554 - [Docs] Let the Qwen3 B300 recipe use the default attention backend

- 链接: https://github.com/sgl-project/sglang/pull/43554
- 状态/时间: merged / 2026-10-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/autoregressive/qwen3-deployment.jsx`；关联提交 `f61163b4b0fe`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-1，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Let the Qwen3 B300 recipe use the default attention backend」；模型线: Qwen3 Core；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/autoregressive/qwen3-deployment.jsx`；技术摘要: 覆盖「[Docs] Let the Qwen3 B300 recipe use the default attention backend」；主要实现面是 `docs/src/snippets/autoregressive/qwen3-deployment.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen3-deployment.jsx` modified +0/-1 (1 lines); hunks: -338,7 +338,6 @@ export const Qwen3Deployment = () => {。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen3-deployment.jsx` modified +0/-1 (1 lines); hunks: -338,7 +338,6 @@ export const Qwen3Deployment = () => {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen3-deployment.jsx
@@ -338,7 +338,6 @@ export const Qwen3Deployment = () => {
-      cmd += ' \\\n  --attention-backend flashinfer';
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen3-deployment.jsx` modified +0/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/autoregressive/qwen3-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #44266 - [Fix] [AMD] qwen3: Fix KV cache write in the fused QK-norm + mRoPE decode path

- 链接: https://github.com/sgl-project/sglang/pull/44266
- 状态/时间: merged / 2026-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `2f5407da286b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+242/-52，可读 patch 346 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [AMD] qwen3: Fix KV cache write in the fused QK-norm + mRoPE decode path」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Fix] [AMD] qwen3: Fix KV cache write in the fused QK-norm + mRoPE decode path」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +80/-52 (132 lines); hunks: -65,6 +65,65; -204,65 +263,26 @@ def forward_prepare_npu(self, positions, hidden_states, fo...; symbols: aiter_fused_qk_norm_rope_set_kv, Qwen3Attention, __init__, forward_prepare_npu，涉及 `aiter_fused_qk_norm_rope_set_kv, Qwen3Attention, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +80/-52 (132 lines); hunks: -65,6 +65,65; -204,65 +263,26 @@ def forward_prepare_npu(self, positions, hidden_states, fo...; symbols: aiter_fused_qk_norm_rope_set_kv, Qwen3Attention, __init__, forward_prepare_npu
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -65,6 +65,65 @@
+def aiter_fused_qk_norm_rope_set_kv(
+    qkv: torch.Tensor,
+    q_norm: RMSNorm,
+    k_norm: RMSNorm,
+    rotary_emb: MRotaryEmbedding,
+    positions: torch.Tensor,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +80/-52
- 验证与风险: diff 自带测试面 `test/registered/amd/test_qwen3_aiter_fused_qk_norm_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44267 - [Perf] [AMD] qwen3: Fuse QK-norm + RoPE + KV cache write for dense Qwen3 decode

- 链接: https://github.com/sgl-project/sglang/pull/44267
- 状态/时间: merged / 2026-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `a448fdf3161a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+84/-38，可读 patch 215 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [AMD] qwen3: Fuse QK-norm + RoPE + KV cache write for dense Qwen3 decode」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Perf] [AMD] qwen3: Fuse QK-norm + RoPE + KV cache write for dense Qwen3 decode」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +61/-36 (97 lines); hunks: -18,7 +18,7; -50,6 +50,7; symbols: aiter_fused_qk_norm_rope_set_kv, __init__, forward_prepare_npu，涉及 `aiter_fused_qk_norm_rope_set_kv, __init__, forward_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +61/-36 (97 lines); hunks: -18,7 +18,7; -50,6 +50,7; symbols: aiter_fused_qk_norm_rope_set_kv, __init__, forward_prepare_npu
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -18,7 +18,7 @@
-from sglang.srt.layers.rotary_embedding import get_rope
+from sglang.srt.layers.rotary_embedding import RotaryEmbedding, get_rope
@@ -50,6 +50,7 @@
+_has_fused_qk_norm_rope = False
@@ -58,6 +59,13 @@
+    try:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +61/-36
- 验证与风险: diff 自带测试面 `test/registered/amd/test_qwen3_aiter_fused_qk_norm_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39580 - [Fix] eplb: Fix Qwen3 MoE output corruption after EPLB rebalance

- 链接: https://github.com/sgl-project/sglang/pull/39580
- 状态/时间: merged / 2026-10-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_moe.py`；关联提交 `9db58ab54751`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-1，可读 patch 22 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] eplb: Fix Qwen3 MoE output corruption after EPLB rebalance」；模型线: Qwen3 Core；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_moe.py`；技术摘要: 覆盖「[Fix] eplb: Fix Qwen3 MoE output corruption after EPLB rebalance」；主要实现面是 `python/sglang/srt/models/qwen3_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_moe.py` modified +11/-1 (12 lines); hunks: -338,10 +338,20 @@ def forward_normal(; symbols: forward_normal，涉及 `forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_moe.py` modified +11/-1 (12 lines); hunks: -338,10 +338,20 @@ def forward_normal(; symbols: forward_normal
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_moe.py
@@ -338,10 +338,20 @@ def forward_normal(
+        dispatch_info = (
+            ExpertLocationDispatchInfo.init_new(layer_id=self.layer_id)
+            if get_exec().moe.enable_eplb
+            else None
+        )
-            topk_output = self.topk(hidden_states, router_logits)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_moe.py` modified +11/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46832 - [Perf] [AMD] qwen3: Use the fused QK-norm + RoPE + KV write in decode with an fp8 KV cache

- 链接: https://github.com/sgl-project/sglang/pull/46832
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `fc778ea2af2d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+152/-35，可读 patch 302 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [AMD] qwen3: Use the fused QK-norm + RoPE + KV write in decode with an fp8 KV cache」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Perf] [AMD] qwen3: Use the fused QK-norm + RoPE + KV write in decode with an fp8 KV cache」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +45/-15 (60 lines); hunks: -52,6 +52,8; -93,8 +95,10 @@ def aiter_fused_qk_norm_rope_set_kv(; symbols: aiter_fused_qk_norm_rope_set_kv, _host_kv_scale, Qwen3Attention, __init__，涉及 `aiter_fused_qk_norm_rope_set_kv, _host_kv_scale, Qwen3Attention`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +45/-15 (60 lines); hunks: -52,6 +52,8; -93,8 +95,10 @@ def aiter_fused_qk_norm_rope_set_kv(; symbols: aiter_fused_qk_norm_rope_set_kv, _host_kv_scale, Qwen3Attention, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -52,6 +52,8 @@
+    from aiter import dtypes as aiter_dtypes
@@ -93,8 +95,10 @@ def aiter_fused_qk_norm_rope_set_kv(
-    head_dim) pool buffers. ``k_scale`` / ``v_scale`` must be CPU tensors: the
-    kernel reads them on the host. Returns q as (num_tokens, num_heads * head_dim).
+    head_dim) pool buffers, in ``qkv``'s dtype or ``aiter.dtypes.fp8``. An fp8
+    cache stores k / k_scale and v / v_scale; other caches ignore the scales.
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +45/-15
- 验证与风险: diff 自带测试面 `test/registered/amd/test_qwen3_aiter_fused_qk_norm_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #46908 - [Perf] [NVIDIA] qwen3: Reuse fused QK-norm/RoPE kernel for decode

- 链接: https://github.com/sgl-project/sglang/pull/46908
- 状态/时间: merged / 2026-10-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `8368f86fd7a7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+372/-15，可读 patch 465 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [NVIDIA] qwen3: Reuse fused QK-norm/RoPE kernel for decode」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Perf] [NVIDIA] qwen3: Reuse fused QK-norm/RoPE kernel for decode」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +48/-10 (58 lines); hunks: -5,6 +5,8; -251,6 +253,19 @@ def __init__(; symbols: __init__, _aiter_fused_kv_scales, forward_prepare_native, forward_prepare_npu，涉及 `__init__, _aiter_fused_kv_scales, forward_prepare_native`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +48/-10 (58 lines); hunks: -5,6 +5,8; -251,6 +253,19 @@ def __init__(; symbols: __init__, _aiter_fused_kv_scales, forward_prepare_native, forward_prepare_npu
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -5,6 +5,8 @@
+from sglang.kernels.ops.attention.table_qk_norm_rope import table_qk_norm_rope_
+from sglang.srt.environ import envs
@@ -251,6 +253,19 @@ def __init__(
+        # Qwen3 guarantees matching norm eps and full-head NeoX RoPE; these
+        # CUDA head sizes also select the non-fallback RoPE implementation.
+        self.use_table_qk_norm_rope = (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +48/-10
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_table_qk_norm_rope.py`, `test/registered/unit/models/test_qwen3_qk_norm_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #48051 - [Doc] qwen: Use TRT-LLM MHA for the B300 Qwen3-VL-4B recipe

- 链接: https://github.com/sgl-project/sglang/pull/48051
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`；关联提交 `18b714464feb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+7/-1，可读 patch 29 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] qwen: Use TRT-LLM MHA for the B300 Qwen3-VL-4B recipe」；模型线: Qwen3 Core；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`；技术摘要: 覆盖「[Doc] qwen: Use TRT-LLM MHA for the B300 Qwen3-VL-4B recipe」；主要实现面是 `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0 (1 lines); hunks: -42,6 +42,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/...。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0 (1 lines); hunks: -42,6 +42,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/...
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.mdx
@@ -42,6 +42,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/qwen3-deployment.j
+- **Qwen3-8B on B300 (BF16, TP1):** SGLang selects `trtllm_mha` by default when speculative decoding is disabled. If your launch command sets `--attention-backend flashinfer`, rem
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3-VL.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`, `docs/src/snippets/autoregressive/qwen3-vl-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #47993 - [Perf] [NVIDIA] qwen3: Reuse the table QK-norm/RoPE kernel for MRoPE decode

- 链接: https://github.com/sgl-project/sglang/pull/47993
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `80121f264fff`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+205/-45，可读 patch 422 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [NVIDIA] qwen3: Reuse the table QK-norm/RoPE kernel for MRoPE decode」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Perf] [NVIDIA] qwen3: Reuse the table QK-norm/RoPE kernel for MRoPE decode」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +18/-1 (19 lines); hunks: -262,9 +262,20 @@ def __init__(; -309,7 +320,12 @@ def forward_prepare_native(self, positions, hidden_states,...; symbols: __init__, forward_prepare_native，涉及 `__init__, forward_prepare_native`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +18/-1 (19 lines); hunks: -262,9 +262,20 @@ def __init__(; -309,7 +320,12 @@ def forward_prepare_native(self, positions, hidden_states,...; symbols: __init__, forward_prepare_native
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -262,9 +262,20 @@ def __init__(
-            and type(self.rotary_emb) is RotaryEmbedding
+            and (
+                type(self.rotary_emb) is RotaryEmbedding
+                or (
+                    # At head_dim 256, triton_mrope_fused's BF16 rounding differs.
+                    type(self.rotary_emb) is MRotaryEmbedding
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +18/-1
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_table_qk_norm_rope.py`, `test/registered/unit/models/test_qwen3_qk_norm_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44491 - [Perf] qwen3: Fuse SiLU*mul with the NVFP4 quantization of down_proj in Qwen2MLP

- 链接: https://github.com/sgl-project/sglang/pull/44491
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3.py`；关联提交 `f85fef81a8a9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+205/-63，可读 patch 399 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] qwen3: Fuse SiLU*mul with the NVFP4 quantization of down_proj in Qwen2MLP」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`；技术摘要: 覆盖「[Perf] qwen3: Fuse SiLU*mul with the NVFP4 quantization of down_proj in Qwen2MLP」；主要实现面是 `python/sglang/srt/models/qwen3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +5/-1 (6 lines); hunks: -38,7 +38,10; -476,6 +479,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +5/-1 (6 lines); hunks: -38,7 +38,10; -476,6 +479,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -38,7 +38,10 @@
-from sglang.srt.models.utils import apply_qk_norm
+from sglang.srt.models.utils import (
+    apply_qk_norm,
+    maybe_enable_silu_fp4_quant_fusion,
+)
@@ -476,6 +479,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +5/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47785 - [Perf] [NVIDIA] qwen3: Fuse prefill QK norm and RoPE with contiguous Q

- 链接: https://github.com/sgl-project/sglang/pull/47785
- 状态/时间: merged / 2026-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`, `python/sglang/srt/models/qwen3.py`；关联提交 `c07ec416dabf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+501/-30，可读 patch 700 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [NVIDIA] qwen3: Fuse prefill QK norm and RoPE with contiguous Q」；模型线: Qwen3 Core；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3.py`, `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`；技术摘要: 覆盖「[Perf] [NVIDIA] qwen3: Fuse prefill QK norm and RoPE with contiguous Q」；主要实现面是 `python/sglang/srt/models/qwen3.py`, `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3.py` modified +53/-1 (54 lines); hunks: -5,6 +5,7; -31,6 +32,7; symbols: __init__, forward_prepare_native，涉及 `__init__, forward_prepare_native`；`docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0 (1 lines); hunks: -47,6 +47,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/...。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3.py` modified +53/-1 (54 lines); hunks: -5,6 +5,7; -31,6 +32,7; symbols: __init__, forward_prepare_native
  - `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0 (1 lines); hunks: -47,6 +47,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/...
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3.py
@@ -5,6 +5,7 @@
+from sglang.kernels.ops.attention.qk_norm_rope import qk_norm_rope
@@ -31,6 +32,7 @@
+from sglang.srt.model_executor.forward_mode import ForwardMode
@@ -40,7 +42,13 @@
-from sglang.srt.runtime_context import get_exec, get_parallel, get_stream
+from sglang.srt.runtime_context import (
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.mdx
@@ -47,6 +47,7 @@ import { Qwen3Deployment } from "/src/snippets/autoregressive/qwen3-deployment.j
+- **Opt-in fused dense prefill:** `--enable-fused-qk-norm-rope` also fuses QK normalization and cached RoPE for ordinary dense-Qwen3 prefill on Hopper, with FP16/BF16, head dimens
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3.py` modified +53/-1
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/benchmark/attention/bench_qk_norm_rope.py`, `test/registered/kernels/ops/attention/test_table_qk_norm_rope.py`, `test/registered/unit/models/test_qwen3_qk_norm_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
