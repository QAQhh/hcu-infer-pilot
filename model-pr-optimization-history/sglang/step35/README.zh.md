# sglang Step 3.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `python/sglang/srt/configs/step3p5.py` | [#18084](https://github.com/sgl-project/sglang/pull/18084) |
| `python/sglang/srt/models/step3p5.py` | [#18084](https://github.com/sgl-project/sglang/pull/18084), [#22076](https://github.com/sgl-project/sglang/pull/22076), [#22773](https://github.com/sgl-project/sglang/pull/22773), [#41082](https://github.com/sgl-project/sglang/pull/41082), [#41198](https://github.com/sgl-project/sglang/pull/41198), [#41437](https://github.com/sgl-project/sglang/pull/41437), [#41754](https://github.com/sgl-project/sglang/pull/41754), [#42302](https://github.com/sgl-project/sglang/pull/42302) |
| `python/sglang/srt/models/step3p5_mtp.py` | [#18084](https://github.com/sgl-project/sglang/pull/18084) |
| `test/registered/e2e/models/test_step3p5_flash_chain_mtp.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 8
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 8
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-02 | [#18084](https://github.com/sgl-project/sglang/pull/18084) | merged | add Step-3.5-Flash model support | `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`, `python/sglang/srt/configs/step3p5.py` |
| 2026-04-04 | [#22076](https://github.com/sgl-project/sglang/pull/22076) | merged | Tiny fix step3.5-flash launch crash | `python/sglang/srt/models/step3p5.py` |
| 2026-04-16 | [#22773](https://github.com/sgl-project/sglang/pull/22773) | merged | [Step3p5] Optimize allreduce in MoE layers | `python/sglang/srt/models/step3p5.py` |
| 2026-09-24 | [#41082](https://github.com/sgl-project/sglang/pull/41082) | merged | [Fix] Step-3.5: stop dense layers from summing their output twice under DP attention | `python/sglang/srt/models/step3p5.py` |
| 2026-09-25 | [#41198](https://github.com/sgl-project/sglang/pull/41198) | merged | [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit | `python/sglang/srt/models/step3p5.py` |
| 2026-09-27 | [#41437](https://github.com/sgl-project/sglang/pull/41437) | merged | [Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit | `python/sglang/srt/models/step3p5.py` |
| 2026-09-30 | [#41754](https://github.com/sgl-project/sglang/pull/41754) | merged | [Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends | `python/sglang/srt/models/step3p5.py` |
| 2026-10-03 | [#42302](https://github.com/sgl-project/sglang/pull/42302) | merged | [Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1 | `python/sglang/srt/models/step3p5.py` |

## 逐 PR diff 审计卡

### PR #18084 - add Step-3.5-Flash model support

- 链接: https://github.com/sgl-project/sglang/pull/18084
- 状态/时间: merged / 2026-02-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/step3p5.py`, `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`；关联提交 `980d2936cd9a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+1557/-12，可读 patch 1711 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「add Step-3.5-Flash model support」；模型线: Step 3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`, `python/sglang/srt/configs/step3p5.py`；技术摘要: 覆盖「add Step-3.5-Flash model support」；主要实现面是 `python/sglang/srt/models/step3p5.py`, `python/sglang/srt/models/step3p5_mtp.py`, `python/sglang/srt/configs/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` added +1037/-0 (1037 lines); hunks: -0,0 +1,1037; symbols: Step3p5MLP, __init__, forward, Step3p5MoEMLP，涉及 `Step3p5MLP, __init__, forward`；`python/sglang/srt/models/step3p5_mtp.py` added +336/-0 (336 lines); hunks: -0,0 +1,336; symbols: get_spec_layer_idx_from_weight_name, SharedHead, __init__, forward，涉及 `get_spec_layer_idx_from_weight_name, SharedHead, __init__`；`python/sglang/srt/configs/step3p5.py` added +97/-0 (97 lines); hunks: -0,0 +1,97; symbols: Step3p5Config, __init__，涉及 `Step3p5Config, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` added +1037/-0 (1037 lines); hunks: -0,0 +1,1037; symbols: Step3p5MLP, __init__, forward, Step3p5MoEMLP
  - `python/sglang/srt/models/step3p5_mtp.py` added +336/-0 (336 lines); hunks: -0,0 +1,336; symbols: get_spec_layer_idx_from_weight_name, SharedHead, __init__, forward
  - `python/sglang/srt/configs/step3p5.py` added +97/-0 (97 lines); hunks: -0,0 +1,97; symbols: Step3p5Config, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -0,0 +1,1037 @@
+import logging
+import os
+from typing import Any, Dict, Iterable, Optional, Tuple, Union
+import torch
+import torch.nn.functional as F
+from torch import nn
diff -- python/sglang/srt/models/step3p5_mtp.py
@@ -0,0 +1,336 @@
+import logging
+from collections.abc import Iterable
+from typing import Optional
+import torch
+import torch.nn as nn
+from transformers import PretrainedConfig
diff -- python/sglang/srt/configs/step3p5.py
@@ -0,0 +1,97 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` added +1037/-0; `python/sglang/srt/models/step3p5_mtp.py` added +336/-0; `python/sglang/srt/configs/step3p5.py` added +97/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22076 - Tiny fix step3.5-flash launch crash

- 链接: https://github.com/sgl-project/sglang/pull/22076
- 状态/时间: merged / 2026-04-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/step3p5.py`；关联提交 `ef130312434c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-1，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Tiny fix step3.5-flash launch crash」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/step3p5.py`；技术摘要: 覆盖「Tiny fix step3.5-flash launch crash」；主要实现面是 `python/sglang/srt/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` modified +0/-1 (1 lines); hunks: -667,7 +667,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` modified +0/-1 (1 lines); hunks: -667,7 +667,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -667,7 +667,6 @@ def __init__(
-        self.padding_idx = config.pad_token_id
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +0/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/step3p5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22773 - [Step3p5] Optimize allreduce in MoE layers

- 链接: https://github.com/sgl-project/sglang/pull/22773
- 状态/时间: merged / 2026-04-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/step3p5.py`；关联提交 `b8794baa6d61`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+59/-57，可读 patch 211 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Step3p5] Optimize allreduce in MoE layers」；模型线: Step 3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/step3p5.py`；技术摘要: 覆盖「[Step3p5] Optimize allreduce in MoE layers」；主要实现面是 `python/sglang/srt/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` modified +59/-57 (116 lines); hunks: -1,5 +1,3; -57,7 +55,6; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` modified +59/-57 (116 lines); hunks: -1,5 +1,3; -57,7 +55,6; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -1,5 +1,3 @@
-import logging
-import os
@@ -57,7 +55,6 @@
-logger = logging.getLogger(__name__)
@@ -69,6 +66,9 @@ def __init__(
+        tp_size: Optional[int] = None,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +59/-57
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/step3p5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41082 - [Fix] Step-3.5: stop dense layers from summing their output twice under DP attention

- 链接: https://github.com/sgl-project/sglang/pull/41082
- 状态/时间: merged / 2026-09-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/step3p5.py`；关联提交 `7c9f74c6e109`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+67/-4，可读 patch 79 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Step-3.5: stop dense layers from summing their output twice under DP attention」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/step3p5.py`；技术摘要: 覆盖「[Fix] Step-3.5: stop dense layers from summing their output twice under DP attention」；主要实现面是 `python/sglang/srt/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` modified +6/-4 (10 lines); hunks: -633,10 +633,12 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` modified +6/-4 (10 lines); hunks: -633,10 +633,12 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -633,10 +633,12 @@ def forward(
-            hidden_states = self.mlp(hidden_states)
-            # Dense MLP uses reduce_results=True, so the output is already
-            # all-reduced.  Do NOT set the fusion flag — otherwise the next
-            # layer would all-reduce again, multiplying values by world_size.
+            # The dense MLP all-reduces its own output unless postprocess
+            # reduce-scatters it; it never leaves the sum to the next layer.
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +6/-4
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41198 - [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit

- 链接: https://github.com/sgl-project/sglang/pull/41198
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/step3p5.py`；关联提交 `b7f6d04a9af1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+50/-219，可读 patch 402 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit」；模型线: Step 3.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/step3p5.py`；技术摘要: 覆盖「[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit」；主要实现面是 `python/sglang/srt/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` modified +24/-41 (65 lines); hunks: -11,11 +11,7; -609,45 +605,32 @@ def forward(; symbols: forward, Step3p5Model，涉及 `forward, Step3p5Model`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` modified +24/-41 (65 lines); hunks: -11,11 +11,7; -609,45 +605,32 @@ def forward(; symbols: forward, Step3p5Model
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -11,11 +11,7 @@
-from sglang.srt.layers.communicator import (
-    LayerCommunicator,
-    LayerScatterModes,
-    UnreducedOutput,
-)
+from sglang.srt.layers.communicator import LayerCommunicator, LayerScatterModes
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +24/-41
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41437 - [Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit

- 链接: https://github.com/sgl-project/sglang/pull/41437
- 状态/时间: merged / 2026-09-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/step3p5.py`；关联提交 `55d2ee554635`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+31/-17，可读 patch 110 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit」；模型线: Step 3.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/step3p5.py`；技术摘要: 覆盖「[Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit」；主要实现面是 `python/sglang/srt/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` modified +5/-11 (16 lines); hunks: -572,6 +572,9 @@ def __init__(; -618,18 +621,9 @@ def forward(; symbols: __init__, forward, Step3p5Model，涉及 `__init__, forward, Step3p5Model`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` modified +5/-11 (16 lines); hunks: -572,6 +572,9 @@ def __init__(; -618,18 +621,9 @@ def forward(; symbols: __init__, forward, Step3p5Model
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -572,6 +572,9 @@ def __init__(
+            # The dense MLP all-reduces its own output unless postprocess
+            # reduce-scatters it; it never leaves the sum to the next layer.
+            allow_deferred_ffn_reduction=self.use_moe,
@@ -618,18 +621,9 @@ def forward(
-        # The dense MLP all-reduces its own output unless postprocess
-        # reduce-scatters it; it never leaves the sum to the next layer.
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +5/-11
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_last_layer_communicator.py`, `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41754 - [Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends

- 链接: https://github.com/sgl-project/sglang/pull/41754
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/step3p5.py`；关联提交 `9ee065e49a12`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+33/-19，可读 patch 135 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/step3p5.py`；技术摘要: 覆盖「[Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends」；主要实现面是 `python/sglang/srt/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` modified +33/-19 (52 lines); hunks: -4,9 +4,6; -32,6 +29,7; symbols: forward, get_moe_weights, forward_normal，涉及 `forward, get_moe_weights, forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` modified +33/-19 (52 lines); hunks: -4,9 +4,6; -32,6 +29,7; symbols: forward, get_moe_weights, forward_normal
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -4,9 +4,6 @@
-from sglang.srt.distributed import (
-    tensor_model_parallel_all_reduce,
-)
@@ -32,6 +29,7 @@
+    should_use_flashinfer_cutlass_moe_fp4_allgather,
@@ -50,7 +48,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +33/-19
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/step3p5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42302 - [Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1

- 链接: https://github.com/sgl-project/sglang/pull/42302
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/step3p5.py`；关联提交 `be20e7453cc8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+18/-8，可读 patch 62 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1」；模型线: Step 3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/step3p5.py`；技术摘要: 覆盖「[Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1」；主要实现面是 `python/sglang/srt/models/step3p5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/step3p5.py` modified +10/-2 (12 lines); hunks: -236,7 +236,13 @@ def forward_deepep(; -252,8 +258,10 @@ def forward_deepep(; symbols: forward_deepep，涉及 `forward_deepep`。
- 代码 diff 细节:
  - `python/sglang/srt/models/step3p5.py` modified +10/-2 (12 lines); hunks: -236,7 +236,13 @@ def forward_deepep(; -252,8 +258,10 @@ def forward_deepep(; symbols: forward_deepep
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/step3p5.py
@@ -236,7 +236,13 @@ def forward_deepep(
-            router_logits, _ = self.gate(hidden_states)
+            if self.need_fp32_gate:
+                router_logits = torch.matmul(
+                    hidden_states.to(torch.float32),
+                    self.gate.weight.t().to(torch.float32),
+                )
```

- 已读文件:
  - runtime: `python/sglang/srt/models/step3p5.py` modified +10/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/sarvam_moe.py`, `python/sglang/srt/models/step3p5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
