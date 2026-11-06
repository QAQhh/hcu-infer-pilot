# vllm ERNIE 4.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/model_executor/test_ernie45_vl_mrope.py` | [#39753](https://github.com/vllm-project/vllm/pull/39753) |
| `tests/reasoning/test_ernie45_reasoning_parser.py` | [#25027](https://github.com/vllm-project/vllm/pull/25027) |
| `tests/tool_parsers/test_ernie45_moe_tool_parser.py` | 无直接 PR 号提交 |
| `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py` | 无直接 PR 号提交 |
| `vllm/model_executor/models/ernie45.py` | [#21735](https://github.com/vllm-project/vllm/pull/21735) |
| `vllm/model_executor/models/ernie45_moe.py` | [#25936](https://github.com/vllm-project/vllm/pull/25936), [#26684](https://github.com/vllm-project/vllm/pull/26684), [#27316](https://github.com/vllm-project/vllm/pull/27316) |
| `vllm/model_executor/models/ernie45_vl.py` | [#39753](https://github.com/vllm-project/vllm/pull/39753), [#45254](https://github.com/vllm-project/vllm/pull/45254), [#51461](https://github.com/vllm-project/vllm/pull/51461) |
| `vllm/model_executor/models/ernie45_vl_moe.py` | [#25936](https://github.com/vllm-project/vllm/pull/25936), [#26885](https://github.com/vllm-project/vllm/pull/26885) |
| `vllm/model_executor/models/ernie_mtp.py` | 无直接 PR 号提交 |
| `vllm/reasoning/ernie45_reasoning_parser.py` | [#25027](https://github.com/vllm-project/vllm/pull/25027), [#27973](https://github.com/vllm-project/vllm/pull/27973), [#46255](https://github.com/vllm-project/vllm/pull/46255) |
| `vllm/tool_parsers/ernie45_tool_parser.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 11
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 11

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-08-11 | [#51461](https://github.com/vllm-project/vllm/pull/51461) | merged | [MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs | `vllm/model_executor/models/ernie45_vl.py` |
| 2026-08-06 | [#45254](https://github.com/vllm-project/vllm/pull/45254) | merged | [MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference | `vllm/model_executor/models/ernie45_vl.py` |
| 2026-07-01 | [#46255](https://github.com/vllm-project/vllm/pull/46255) | merged | fix(reasoning): guard rfind in ernie45 streaming branch | `vllm/reasoning/ernie45_reasoning_parser.py` |
| 2026-04-14 | [#39753](https://github.com/vllm-project/vllm/pull/39753) | merged | [Model] Use mm_features for Ernie-4.5 VL M-RoPE | `vllm/model_executor/models/ernie45_vl.py`, `tests/model_executor/test_ernie45_vl_mrope.py` |
| 2025-11-04 | [#27973](https://github.com/vllm-project/vllm/pull/27973) | merged | [Model] fix ernie45 reasoning_parser | `vllm/reasoning/ernie45_reasoning_parser.py` |
| 2025-10-27 | [#27316](https://github.com/vllm-project/vllm/pull/27316) | merged | [Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple | `vllm/model_executor/models/ernie45_moe.py` |
| 2025-10-16 | [#26885](https://github.com/vllm-project/vllm/pull/26885) | merged | [Model][Bugfix] fix ernie45 vl run failed from shared experts optimization | `vllm/model_executor/models/ernie45_vl_moe.py` |
| 2025-10-14 | [#26684](https://github.com/vllm-project/vllm/pull/26684) | merged | [Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code | `vllm/model_executor/models/ernie45_moe.py` |
| 2025-10-13 | [#25027](https://github.com/vllm-project/vllm/pull/25027) | merged | [Model] Add reasoning_parser and tool_parser for Ernie45 thinking | `vllm/reasoning/ernie45_reasoning_parser.py`, `tests/reasoning/test_ernie45_reasoning_parser.py` |
| 2025-09-30 | [#25936](https://github.com/vllm-project/vllm/pull/25936) | merged | [Bugfix][Model]fix ernie45 moe gate&bias dtype to float32 | `vllm/model_executor/models/ernie45_vl_moe.py`, `vllm/model_executor/models/ernie45_moe.py` |
| 2025-07-28 | [#21735](https://github.com/vllm-project/vllm/pull/21735) | merged | [`Ernie 4.5`] Name Change for Base 0.3B Model | `vllm/model_executor/models/ernie45.py` |

## 逐 PR diff 审计卡

### PR #51461 - [MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs

- 链接: https://github.com/vllm-project/vllm/pull/51461
- 状态/时间: merged / 2026-08-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/ernie45_vl.py`；关联提交 `b2506d62aec7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-1，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/ernie45_vl.py`；技术摘要: 覆盖「[MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs」；主要实现面是 `vllm/model_executor/models/ernie45_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45_vl.py` modified +3/-1 (4 lines); hunks: -1721,7 +1721,7 @@ def encoder_eager_forward(; -1731,6 +1731,8 @@ def postprocess_encoder_output(; symbols: encoder_eager_forward, postprocess_encoder_output，涉及 `encoder_eager_forward, postprocess_encoder_output`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45_vl.py` modified +3/-1 (4 lines); hunks: -1721,7 +1721,7 @@ def encoder_eager_forward(; -1731,6 +1731,8 @@ def postprocess_encoder_output(; symbols: encoder_eager_forward, postprocess_encoder_output
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45_vl.py
@@ -1721,7 +1721,7 @@ def encoder_eager_forward(
-        output: torch.Tensor,
+        outputs: dict[str, torch.Tensor],
@@ -1731,6 +1731,8 @@ def postprocess_encoder_output(
+        # Ernie only uses the single "default" encoder path.
+        output = outputs["default"]
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45_vl.py` modified +3/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/ernie45_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #45254 - [MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference

- 链接: https://github.com/vllm-project/vllm/pull/45254
- 状态/时间: merged / 2026-08-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/ernie45_vl.py`；关联提交 `777b01d1a86e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+289/-13，可读 patch 374 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference」；模型线: ERNIE 4.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/ernie45_vl.py`；技术摘要: 覆盖「[MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference」；主要实现面是 `vllm/model_executor/models/ernie45_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45_vl.py` modified +260/-13 (273 lines); hunks: -77,12 +77,18; -453,13 +459,43 @@ def compute_attn_mask_seqlen(self, cu_seqlens: torch.Tenso...; symbols: compute_attn_mask_seqlen, forward, prepare_encoder_metadata，涉及 `compute_attn_mask_seqlen, forward, prepare_encoder_metadata`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45_vl.py` modified +260/-13 (273 lines); hunks: -77,12 +77,18; -453,13 +459,43 @@ def compute_attn_mask_seqlen(self, cu_seqlens: torch.Tenso...; symbols: compute_attn_mask_seqlen, forward, prepare_encoder_metadata
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45_vl.py
@@ -77,12 +77,18 @@
+    SupportsEncoderCudaGraph,
-from .utils import AutoWeightsLoader, WeightsMapper, maybe_prefix
+from .utils import (
+    AutoWeightsLoader,
+    WeightsMapper,
+    maybe_prefix,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45_vl.py` modified +260/-13
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation/test_vit_cudagraph.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #46255 - fix(reasoning): guard rfind in ernie45 streaming branch

- 链接: https://github.com/vllm-project/vllm/pull/46255
- 状态/时间: merged / 2026-07-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/reasoning/ernie45_reasoning_parser.py`；关联提交 `9294dd27eb9c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(reasoning): guard rfind in ernie45 streaming branch」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `vllm/reasoning/ernie45_reasoning_parser.py`；技术摘要: 覆盖「fix(reasoning): guard rfind in ernie45 streaming branch」；主要实现面是 `vllm/reasoning/ernie45_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-1 (3 lines); hunks: -114,7 +114,8 @@ def extract_reasoning_streaming(; symbols: extract_reasoning_streaming，涉及 `extract_reasoning_streaming`。
- 代码 diff 细节:
  - `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-1 (3 lines); hunks: -114,7 +114,8 @@ def extract_reasoning_streaming(; symbols: extract_reasoning_streaming
- 关键代码摘录:

```diff
diff -- vllm/reasoning/ernie45_reasoning_parser.py
@@ -114,7 +114,8 @@ def extract_reasoning_streaming(
-                content = content[:response_end_idx]
+                if response_end_idx != -1:
+                    content = content[:response_end_idx]
```

- 已读文件:
  - runtime: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/reasoning/ernie45_reasoning_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #39753 - [Model] Use mm_features for Ernie-4.5 VL M-RoPE

- 链接: https://github.com/vllm-project/vllm/pull/39753
- 状态/时间: merged / 2026-04-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/model_executor/test_ernie45_vl_mrope.py`, `vllm/model_executor/models/ernie45_vl.py`；关联提交 `0008729abfbd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+196/-123，可读 patch 339 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Use mm_features for Ernie-4.5 VL M-RoPE」；模型线: ERNIE 4.5；类别: 文档/测试/CI；主要 diff: `vllm/model_executor/models/ernie45_vl.py`, `tests/model_executor/test_ernie45_vl_mrope.py`；技术摘要: 覆盖「[Model] Use mm_features for Ernie-4.5 VL M-RoPE」；主要实现面是 `vllm/model_executor/models/ernie45_vl.py`, `tests/model_executor/test_ernie45_vl_mrope.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45_vl.py` modified +53/-123 (176 lines); hunks: -23,9 +23,8; -1401,131 +1400,62 @@ def get_mrope_input_positions(; symbols: get_mrope_input_positions, iter_mm_grid_thw, _parse_and_validate_image_input，涉及 `get_mrope_input_positions, iter_mm_grid_thw, _parse_and_validate_image_input`；`tests/model_executor/test_ernie45_vl_mrope.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: _force_cpu_default_device, DummyConfig, make_model, make_mm_feature，涉及 `_force_cpu_default_device, DummyConfig, make_model`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45_vl.py` modified +53/-123 (176 lines); hunks: -23,9 +23,8; -1401,131 +1400,62 @@ def get_mrope_input_positions(; symbols: get_mrope_input_positions, iter_mm_grid_thw, _parse_and_validate_image_input
  - `tests/model_executor/test_ernie45_vl_mrope.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: _force_cpu_default_device, DummyConfig, make_model, make_mm_feature
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45_vl.py
@@ -23,9 +23,8 @@
-import itertools
-from collections.abc import Callable, Iterable, Mapping, Sequence
+from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
@@ -1401,131 +1400,62 @@ def get_mrope_input_positions(
-        kwargs = MultiModalFeatureSpec.gather_kwargs(
-            mm_features,
diff -- tests/model_executor/test_ernie45_vl_mrope.py
@@ -0,0 +1,143 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from dataclasses import dataclass
+import pytest
+import torch
+from vllm.model_executor.models.ernie45_vl import (
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45_vl.py` modified +53/-123
  - tests: `tests/model_executor/test_ernie45_vl_mrope.py` added +143/-0
- 验证与风险: diff 自带测试面 `tests/model_executor/test_ernie45_vl_mrope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27973 - [Model] fix ernie45 reasoning_parser

- 链接: https://github.com/vllm-project/vllm/pull/27973
- 状态/时间: merged / 2025-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/reasoning/ernie45_reasoning_parser.py`；关联提交 `43a6acfb7de8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] fix ernie45 reasoning_parser」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `vllm/reasoning/ernie45_reasoning_parser.py`；技术摘要: 覆盖「[Model] fix ernie45 reasoning_parser」；主要实现面是 `vllm/reasoning/ernie45_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-2 (4 lines); hunks: -36,8 +36,8 @@ def end_token(self) -> str:; symbols: end_token, __init__，涉及 `end_token, __init__`。
- 代码 diff 细节:
  - `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-2 (4 lines); hunks: -36,8 +36,8 @@ def end_token(self) -> str:; symbols: end_token, __init__
- 关键代码摘录:

```diff
diff -- vllm/reasoning/ernie45_reasoning_parser.py
@@ -36,8 +36,8 @@ def end_token(self) -> str:
-    def __init__(self, tokenizer: PreTrainedTokenizerBase):
-        super().__init__(tokenizer)
+    def __init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
+        super().__init__(tokenizer, *args, **kwargs)
```

- 已读文件:
  - runtime: `vllm/reasoning/ernie45_reasoning_parser.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/reasoning/ernie45_reasoning_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27316 - [Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple

- 链接: https://github.com/vllm-project/vllm/pull/27316
- 状态/时间: merged / 2025-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/ernie45_moe.py`；关联提交 `63b22e0dbb90`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-0，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/ernie45_moe.py`；技术摘要: 覆盖「[Model][Bugfix] fix ernie45 moe 300B SharedFusedMoE output tuple」；主要实现面是 `vllm/model_executor/models/ernie45_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45_moe.py` modified +2/-0 (2 lines); hunks: -215,6 +215,8 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45_moe.py` modified +2/-0 (2 lines); hunks: -215,6 +215,8 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45_moe.py
@@ -215,6 +215,8 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
+        else:
+            final_hidden_states = final_hidden_states[1]
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45_moe.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/ernie45_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26885 - [Model][Bugfix] fix ernie45 vl run failed from shared experts optimization

- 链接: https://github.com/vllm-project/vllm/pull/26885
- 状态/时间: merged / 2025-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/ernie45_vl_moe.py`；关联提交 `e51928793e10`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+22/-5，可读 patch 55 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][Bugfix] fix ernie45 vl run failed from shared experts optimization」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/ernie45_vl_moe.py`；技术摘要: 覆盖「[Model][Bugfix] fix ernie45 vl run failed from shared experts optimization」；主要实现面是 `vllm/model_executor/models/ernie45_vl_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45_vl_moe.py` modified +22/-5 (27 lines); hunks: -341,7 +341,10 @@ def forward(; -353,16 +356,26 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45_vl_moe.py` modified +22/-5 (27 lines); hunks: -341,7 +341,10 @@ def forward(; -353,16 +356,26 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45_vl_moe.py
@@ -341,7 +341,10 @@ def forward(
-            final_hidden_states = torch.zeros_like(hidden_states)
+            final_experts_hidden_states = torch.zeros_like(hidden_states)
+            final_shared_ouput = (
+                torch.zeros_like(hidden_states) if self.has_shared_experts else None
+            )
@@ -353,16 +356,26 @@ def forward(
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45_vl_moe.py` modified +22/-5
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/ernie45_vl_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26684 - [Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code

- 链接: https://github.com/vllm-project/vllm/pull/26684
- 状态/时间: merged / 2025-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/ernie45_moe.py`；关联提交 `01ad27faff35`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+22/-12，可读 patch 71 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/ernie45_moe.py`；技术摘要: 覆盖「[Model][Bugfix]fix ernie45 load failed due to ernie45 eplb code」；主要实现面是 `vllm/model_executor/models/ernie45_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45_moe.py` modified +22/-12 (34 lines); hunks: -23,7 +23,8; -139,10 +140,10 @@ def __init__(; symbols: __init__, load_weights，涉及 `__init__, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45_moe.py` modified +22/-12 (34 lines); hunks: -23,7 +23,8; -139,10 +140,10 @@ def __init__(; symbols: __init__, load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45_moe.py
@@ -23,7 +23,8 @@
-from collections.abc import Iterable
+import typing
+from collections.abc import Callable, Iterable
@@ -139,10 +140,10 @@ def __init__(
-        parallel_config = vllm_config.parallel_config
+        eplb_config = vllm_config.parallel_config.eplb_config
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45_moe.py` modified +22/-12
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/ernie45_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25027 - [Model] Add reasoning_parser and tool_parser for Ernie45 thinking

- 链接: https://github.com/vllm-project/vllm/pull/25027
- 状态/时间: merged / 2025-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_ernie45_reasoning_parser.py`, `vllm/reasoning/ernie45_reasoning_parser.py`；关联提交 `782505ed8eb4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+870/-0，可读 patch 909 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add reasoning_parser and tool_parser for Ernie45 thinking」；模型线: ERNIE 4.5；类别: 文档/测试/CI；主要 diff: `vllm/reasoning/ernie45_reasoning_parser.py`, `tests/reasoning/test_ernie45_reasoning_parser.py`；技术摘要: 覆盖「[Model] Add reasoning_parser and tool_parser for Ernie45 thinking」；主要实现面是 `vllm/reasoning/ernie45_reasoning_parser.py`, `tests/reasoning/test_ernie45_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/reasoning/ernie45_reasoning_parser.py` added +169/-0 (169 lines); hunks: -0,0 +1,169; symbols: Ernie45ReasoningParser, start_token, end_token, __init__，涉及 `Ernie45ReasoningParser, start_token, end_token`；`tests/reasoning/test_ernie45_reasoning_parser.py` added +124/-0 (124 lines); hunks: -0,0 +1,124; symbols: ernie45_tokenizer, test_reasoning，涉及 `ernie45_tokenizer, test_reasoning`。
- 代码 diff 细节:
  - `vllm/reasoning/ernie45_reasoning_parser.py` added +169/-0 (169 lines); hunks: -0,0 +1,169; symbols: Ernie45ReasoningParser, start_token, end_token, __init__
  - `tests/reasoning/test_ernie45_reasoning_parser.py` added +124/-0 (124 lines); hunks: -0,0 +1,124; symbols: ernie45_tokenizer, test_reasoning
- 关键代码摘录:

```diff
diff -- vllm/reasoning/ernie45_reasoning_parser.py
@@ -0,0 +1,169 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Sequence
+from transformers import PreTrainedTokenizerBase
+from vllm.entrypoints.openai.protocol import ChatCompletionRequest, DeltaMessage
+from vllm.logger import init_logger
diff -- tests/reasoning/test_ernie45_reasoning_parser.py
@@ -0,0 +1,124 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from transformers import AutoTokenizer
+from tests.reasoning.utils import run_reasoning_extraction
+from vllm.reasoning import ReasoningParser, ReasoningParserManager
```

- 已读文件:
  - runtime: `vllm/reasoning/ernie45_reasoning_parser.py` added +169/-0
  - tests: `tests/reasoning/test_ernie45_reasoning_parser.py` added +124/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_ernie45_reasoning_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25936 - [Bugfix][Model]fix ernie45 moe gate&bias dtype to float32

- 链接: https://github.com/vllm-project/vllm/pull/25936
- 状态/时间: merged / 2025-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/ernie45_moe.py`, `vllm/model_executor/models/ernie45_vl_moe.py`；关联提交 `ef6e0e7132ec`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+13/-7，可读 patch 83 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model]fix ernie45 moe gate&bias dtype to float32」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/ernie45_vl_moe.py`, `vllm/model_executor/models/ernie45_moe.py`；技术摘要: 覆盖「[Bugfix][Model]fix ernie45 moe gate&bias dtype to float32」；主要实现面是 `vllm/model_executor/models/ernie45_vl_moe.py`, `vllm/model_executor/models/ernie45_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45_vl_moe.py` modified +10/-5 (15 lines); hunks: -199,7 +199,7 @@ def __init__(; -209,6 +209,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/model_executor/models/ernie45_moe.py` modified +3/-2 (5 lines); hunks: -120,11 +120,12 @@ def __init__(; -157,7 +158,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45_vl_moe.py` modified +10/-5 (15 lines); hunks: -199,7 +199,7 @@ def __init__(; -209,6 +209,7 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/ernie45_moe.py` modified +3/-2 (5 lines); hunks: -120,11 +120,12 @@ def __init__(; -157,7 +158,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45_vl_moe.py
@@ -199,7 +199,7 @@ def __init__(
-            torch.empty(2, config.moe_num_experts[0]))
+            torch.empty(2, config.moe_num_experts[0], dtype=torch.float32))
@@ -209,6 +209,7 @@ def __init__(
+                params_dtype=torch.float32,
@@ -238,6 +239,7 @@ def __init__(
+                params_dtype=torch.float32,
diff -- vllm/model_executor/models/ernie45_moe.py
@@ -120,11 +120,12 @@ def __init__(
+                                     params_dtype=torch.float32,
-            torch.empty(config.moe_num_experts))
+            torch.empty(config.moe_num_experts, dtype=torch.float32))
@@ -157,7 +158,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
-        router_logits, _ = self.gate(hidden_states)
+        router_logits, _ = self.gate(hidden_states.to(dtype=torch.float32))
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45_vl_moe.py` modified +10/-5; `vllm/model_executor/models/ernie45_moe.py` modified +3/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/ernie45_moe.py`, `vllm/model_executor/models/ernie45_vl_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21735 - [`Ernie 4.5`] Name Change for Base 0.3B Model

- 链接: https://github.com/vllm-project/vllm/pull/21735
- 状态/时间: merged / 2025-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/ernie45.py`；关联提交 `656c24f1b5d8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+8/-8，可读 patch 51 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[`Ernie 4.5`] Name Change for Base 0.3B Model」；模型线: ERNIE 4.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/ernie45.py`；技术摘要: 覆盖「[`Ernie 4.5`] Name Change for Base 0.3B Model」；主要实现面是 `vllm/model_executor/models/ernie45.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/ernie45.py` modified +1/-1 (2 lines); hunks: -28,7 +28,7; symbols: Ernie4_5_ForCausalLM, Ernie4_5ForCausalLM, __init__，涉及 `Ernie4_5_ForCausalLM, Ernie4_5ForCausalLM, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/ernie45.py` modified +1/-1 (2 lines); hunks: -28,7 +28,7; symbols: Ernie4_5_ForCausalLM, Ernie4_5ForCausalLM, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/ernie45.py
@@ -28,7 +28,7 @@
-class Ernie4_5_ForCausalLM(LlamaForCausalLM):
+class Ernie4_5ForCausalLM(LlamaForCausalLM):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/ernie45.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
