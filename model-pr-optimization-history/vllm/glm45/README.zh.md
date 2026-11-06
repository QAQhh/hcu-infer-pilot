# vllm GLM-4.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/reasoning/test_glm4_moe_reasoning_parser.py` | 无直接 PR 号提交 |
| `tests/tool_parsers/test_glm4_moe_tool_parser.py` | [#39601](https://github.com/vllm-project/vllm/pull/39601) |
| `vllm/model_executor/models/glm4_moe.py` | [#21435](https://github.com/vllm-project/vllm/pull/21435), [#22143](https://github.com/vllm-project/vllm/pull/22143), [#22203](https://github.com/vllm-project/vllm/pull/22203), [#22460](https://github.com/vllm-project/vllm/pull/22460), [#22520](https://github.com/vllm-project/vllm/pull/22520), [#22832](https://github.com/vllm-project/vllm/pull/22832), [#24849](https://github.com/vllm-project/vllm/pull/24849), [#25830](https://github.com/vllm-project/vllm/pull/25830), [#41755](https://github.com/vllm-project/vllm/pull/41755), [#44313](https://github.com/vllm-project/vllm/pull/44313) |
| `vllm/model_executor/models/glm4_moe_lite.py` | 无直接 PR 号提交 |
| `vllm/model_executor/models/glm4_moe_lite_mtp.py` | [#62234](https://github.com/vllm-project/vllm/pull/62234) |
| `vllm/model_executor/models/glm4_moe_mtp.py` | [#27597](https://github.com/vllm-project/vllm/pull/27597), [#28805](https://github.com/vllm-project/vllm/pull/28805), [#44313](https://github.com/vllm-project/vllm/pull/44313), [#62234](https://github.com/vllm-project/vllm/pull/62234) |

## PR 覆盖总览

- git 追溯 PR 数: 14
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 14

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-11-04 | [#62234](https://github.com/vllm-project/vllm/pull/62234) | merged | [Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden. | `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-06-28 | [#44313](https://github.com/vllm-project/vllm/pull/44313) | merged | [ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7 | `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-05-21 | [#39601](https://github.com/vllm-project/vllm/pull/39601) | merged | [Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format | `tests/tool_parsers/test_glm4_moe_tool_parser.py` |
| 2026-05-07 | [#41755](https://github.com/vllm-project/vllm/pull/41755) | merged | [Bugfix] Fix GLM4-MoE weight loading for NVFP4 quantized checkpoints | `vllm/model_executor/models/glm4_moe.py` |
| 2025-11-17 | [#28805](https://github.com/vllm-project/vllm/pull/28805) | merged | [BugFix] Fix glm4_moe_mtp load weights bug | `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2025-11-12 | [#27597](https://github.com/vllm-project/vllm/pull/27597) | merged | [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint. | `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2025-09-28 | [#25830](https://github.com/vllm-project/vllm/pull/25830) | merged | Update GLM-4.5 Doc transformers version | `vllm/model_executor/models/glm4_moe.py` |
| 2025-09-17 | [#24849](https://github.com/vllm-project/vllm/pull/24849) | merged | [Model] Apply SharedFusedMoE to glm4_moe. | `vllm/model_executor/models/glm4_moe.py` |
| 2025-08-14 | [#22832](https://github.com/vllm-project/vllm/pull/22832) | merged | [Model] Modify the gate implementation of glm4_moe | `vllm/model_executor/models/glm4_moe.py` |
| 2025-08-09 | [#22520](https://github.com/vllm-project/vllm/pull/22520) | merged | GLM-4.5V with new class name at transformers | `vllm/model_executor/models/glm4_moe.py` |
| 2025-08-08 | [#22460](https://github.com/vllm-project/vllm/pull/22460) | merged | not tie_word_embeddings for glm-4.5 and glm-4.5v | `vllm/model_executor/models/glm4_moe.py` |
| 2025-08-05 | [#22203](https://github.com/vllm-project/vllm/pull/22203) | merged | self.gate dtype update for GLM-4.5 | `vllm/model_executor/models/glm4_moe.py` |
| 2025-08-03 | [#22143](https://github.com/vllm-project/vllm/pull/22143) | merged | fuse fp32 for GLM-4.5 e_score_correction_bias | `vllm/model_executor/models/glm4_moe.py` |
| 2025-07-24 | [#21435](https://github.com/vllm-project/vllm/pull/21435) | merged | remove GLM-4 quantization wrong Code | `vllm/model_executor/models/glm4_moe.py` |

## 逐 PR diff 审计卡

### PR #62234 - [Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.

- 链接: https://github.com/vllm-project/vllm/pull/62234
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`；关联提交 `62966a7e00c4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+166/-14，可读 patch 282 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`；技术摘要: 覆盖「[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.」；主要实现面是 `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe_lite_mtp.py` modified +7/-5 (12 lines); hunks: -156,8 +156,12 @@ def forward(; -214,9 +218,7 @@ def compute_logits(; symbols: forward, Glm4MoeLiteMultiTokenPredictor, compute_logits，涉及 `forward, Glm4MoeLiteMultiTokenPredictor, compute_logits`；`vllm/model_executor/models/glm4_moe_mtp.py` modified +7/-5 (12 lines); hunks: -127,8 +127,12 @@ def forward(; -188,9 +192,7 @@ def compute_logits(; symbols: forward, Glm4MoeMultiTokenPredictor, compute_logits，涉及 `forward, Glm4MoeMultiTokenPredictor, compute_logits`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe_lite_mtp.py` modified +7/-5 (12 lines); hunks: -156,8 +156,12 @@ def forward(; -214,9 +218,7 @@ def compute_logits(; symbols: forward, Glm4MoeLiteMultiTokenPredictor, compute_logits
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +7/-5 (12 lines); hunks: -127,8 +127,12 @@ def forward(; -188,9 +192,7 @@ def compute_logits(; symbols: forward, Glm4MoeMultiTokenPredictor, compute_logits
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe_lite_mtp.py
@@ -156,8 +156,12 @@ def forward(
-        hidden_states = residual + hidden_states
-        return hidden_states
+        # Apply the final norm once (fused add+norm) and recycle the
+        # post-final-norm hidden into the next draft step; compute_logits uses
+        # it directly. Matches the GLM MTP recycle contract from #47448 and
+        # vllm/models/glm5next/common/mtp.py.
diff -- vllm/model_executor/models/glm4_moe_mtp.py
@@ -127,8 +127,12 @@ def forward(
-        hidden_states = residual + hidden_states
-        return hidden_states
+        # Apply the final norm once (fused add+norm) and recycle the
+        # post-final-norm hidden into the next draft step; compute_logits uses
+        # it directly. Matches the GLM MTP recycle contract from #47448 and
+        # vllm/models/glm5next/common/mtp.py.
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe_lite_mtp.py` modified +7/-5; `vllm/model_executor/models/glm4_moe_mtp.py` modified +7/-5
- 验证与风险: diff 自带测试面 `tests/v1/e2e/spec_decode/mtp/glm/__init__.py`, `tests/v1/e2e/spec_decode/mtp/glm/test_mtp.py`, `tests/v1/spec_decode/test_llm_base_proposer_sampling.py`, `tests/v1/spec_decode/test_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44313 - [ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7

- 链接: https://github.com/vllm-project/vllm/pull/44313
- 状态/时间: merged / 2026-06-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`；关联提交 `c7ca0bccae66`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+254/-105，可读 patch 482 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7」；模型线: GLM-4.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`；技术摘要: 覆盖「[ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +138/-63 (201 lines); hunks: -32,6 +32,7; -168,7 +169,16 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/model_executor/models/glm4_moe_mtp.py` modified +116/-42 (158 lines); hunks: -24,12 +24,14; -239,6 +241,10 @@ def compute_logits(; symbols: compute_logits, load_weights，涉及 `compute_logits, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +138/-63 (201 lines); hunks: -32,6 +32,7; -168,7 +169,16 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +116/-42 (158 lines); hunks: -24,12 +24,14; -239,6 +241,10 @@ def compute_logits(; symbols: compute_logits, load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -32,6 +32,7 @@
+from vllm._aiter_ops import rocm_aiter_ops
@@ -168,7 +169,16 @@ def __init__(
-        if config.n_shared_experts is not None:
+        # AITER fused shared-expert (FSE) gate; mirrors the deepseek_v2.py
+        # pattern (see Glm4MoE / FusedMoE wiring there).
+        self.is_rocm_aiter_moe_enabled = rocm_aiter_ops.is_fused_moe_enabled()
diff -- vllm/model_executor/models/glm4_moe_mtp.py
@@ -24,12 +24,14 @@
-from collections.abc import Iterable
+import typing
+from collections.abc import Callable, Iterable
+from vllm._aiter_ops import rocm_aiter_ops
@@ -239,6 +241,10 @@ def compute_logits(
+        # FSE weight loading mirrors glm4_moe.py / deepseek_mtp.py.
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +138/-63; `vllm/model_executor/models/glm4_moe_mtp.py` modified +116/-42
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #39601 - [Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format

- 链接: https://github.com/vllm-project/vllm/pull/39601
- 状态/时间: merged / 2026-05-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_glm4_moe_tool_parser.py`；关联提交 `050611a3dd19`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+135/-25，可读 patch 214 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_glm4_moe_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format」；主要实现面是 `tests/tool_parsers/test_glm4_moe_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +120/-0 (120 lines); hunks: -5,6 +5,7; -1363,3 +1364,122 @@ def test_stream_interval_content_between_tool_calls(; symbols: test_stream_interval_content_between_tool_calls, function_tools, glm4_moe_parser_function_tools, mock_request_function_tools，涉及 `test_stream_interval_content_between_tool_calls, function_tools, glm4_moe_parser_function_tools`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +120/-0 (120 lines); hunks: -5,6 +5,7; -1363,3 +1364,122 @@ def test_stream_interval_content_between_tool_calls(; symbols: test_stream_interval_content_between_tool_calls, function_tools, glm4_moe_parser_function_tools, mock_request_function_tools
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_glm4_moe_tool_parser.py
@@ -5,6 +5,7 @@
+from openai.types.responses import FunctionTool
@@ -1363,3 +1364,122 @@ def test_stream_interval_content_between_tool_calls(
+# ── FunctionTool (Responses API) tests ──────────────────────────────
+@pytest.fixture
+def function_tools():
+    return [
```

- 已读文件:
  - tests: `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +120/-0
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_glm4_moe_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41755 - [Bugfix] Fix GLM4-MoE weight loading for NVFP4 quantized checkpoints

- 链接: https://github.com/vllm-project/vllm/pull/41755
- 状态/时间: merged / 2026-05-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `75f0d516c43c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-2，可读 patch 27 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix GLM4-MoE weight loading for NVFP4 quantized checkpoints」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「[Bugfix] Fix GLM4-MoE weight loading for NVFP4 quantized checkpoints」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +10/-2 (12 lines); hunks: -506,16 +506,24 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +10/-2 (12 lines); hunks: -506,16 +506,24 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -506,16 +506,24 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                name = maybe_remap_kv_scale_name(name, params_dict)
+                if name is None:
+                    continue
-                weight_loader = param.weight_loader
-                weight_loader(param, loaded_weight, shard_id)
+                weight_loader = getattr(param, "weight_loader", default_weight_loader)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +10/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28805 - [BugFix] Fix glm4_moe_mtp load weights bug

- 链接: https://github.com/vllm-project/vllm/pull/28805
- 状态/时间: merged / 2025-11-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe_mtp.py`；关联提交 `ab01cd14e5e2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-4，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix] Fix glm4_moe_mtp load weights bug」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_moe_mtp.py`；技术摘要: 覆盖「[BugFix] Fix glm4_moe_mtp load weights bug」；主要实现面是 `vllm/model_executor/models/glm4_moe_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe_mtp.py` modified +3/-4 (7 lines); hunks: -256,13 +256,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +3/-4 (7 lines); hunks: -256,13 +256,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe_mtp.py
@@ -256,13 +256,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-        spec_layer = self.model.mtp_start_layer_idx
-                name = f"model.layers.{spec_layer}.shard_head.head.weight"
+                spec_layer = self.model.mtp_start_layer_idx
+                name = f"model.layers.{spec_layer}.shared_head.head.weight"
-                # This name is same with local model, rewriting is not needed.
-                pass
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe_mtp.py` modified +3/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27597 - [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.

- 链接: https://github.com/vllm-project/vllm/pull/27597
- 状态/时间: merged / 2025-11-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe_mtp.py`；关联提交 `d3ade61e429f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-4，可读 patch 23 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_moe_mtp.py`；技术摘要: 覆盖「[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.」；主要实现面是 `vllm/model_executor/models/glm4_moe_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe_mtp.py
@@ -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+        spec_layer = self.model.mtp_start_layer_idx
-            spec_layer = get_spec_layer_idx_from_weight_name(self.config, name)
-            if spec_layer is None:
-                continue
-            name = self._rewrite_spec_layer_name(spec_layer, name)
+            if name == "lm_head.weight":
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25830 - Update GLM-4.5 Doc transformers version

- 链接: https://github.com/vllm-project/vllm/pull/25830
- 状态/时间: merged / 2025-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `b1ded114b976`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+7/-5，可读 patch 40 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update GLM-4.5 Doc transformers version」；模型线: GLM-4.5；类别: 文档/测试/CI；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「Update GLM-4.5 Doc transformers version」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -21,7 +21,7。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -21,7 +21,7
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -21,7 +21,7 @@
-"""Inference-only GLM-4.5 model compatible with HuggingFace weights."""
+"""Inference-only GLM-4.5, GLM-4.6 model compatible with HuggingFace weights."""
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #24849 - [Model] Apply SharedFusedMoE to glm4_moe.

- 链接: https://github.com/vllm-project/vllm/pull/24849
- 状态/时间: merged / 2025-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `c15309a730fa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+55/-30，可读 patch 114 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Apply SharedFusedMoE to glm4_moe.」；模型线: GLM-4.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「[Model] Apply SharedFusedMoE to glm4_moe.」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +55/-30 (85 lines); hunks: -46,6 +46,7; -146,25 +147,6 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +55/-30 (85 lines); hunks: -46,6 +46,7; -146,25 +147,6 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -46,6 +46,7 @@
+from vllm.model_executor.layers.shared_fused_moe import SharedFusedMoE
@@ -146,25 +147,6 @@ def __init__(
-        self.experts = FusedMoE(
-            num_experts=config.n_routed_experts,
-            top_k=config.num_experts_per_tok,
-            hidden_size=config.hidden_size,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +55/-30
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22832 - [Model] Modify the gate implementation of glm4_moe

- 链接: https://github.com/vllm-project/vllm/pull/22832
- 状态/时间: merged / 2025-08-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `92ff41abea13`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-11，可读 patch 50 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Modify the gate implementation of glm4_moe」；模型线: GLM-4.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「[Model] Modify the gate implementation of glm4_moe」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +10/-10 (20 lines); hunks: -41,7 +41,6; -118,14 +117,15 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +10/-10 (20 lines); hunks: -41,7 +41,6; -118,14 +117,15 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -41,7 +41,6 @@
-                                               ReplicatedLinear,
@@ -118,14 +117,15 @@ def __init__(
-        self.gate = ReplicatedLinear(config.hidden_size,
-                                     config.n_routed_experts,
-                                     bias=False,
-                                     quant_config=None,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +10/-10
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22520 - GLM-4.5V with new class name at transformers

- 链接: https://github.com/vllm-project/vllm/pull/22520
- 状态/时间: merged / 2025-08-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `a6022e6fbcbd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+13/-6，可读 patch 61 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-4.5V with new class name at transformers」；模型线: GLM-4.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「GLM-4.5V with new class name at transformers」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +7/-1 (8 lines); hunks: -372,7 +372,13 @@ def forward(; symbols: forward, Glm4MoeModel, __init__，涉及 `forward, Glm4MoeModel, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +7/-1 (8 lines); hunks: -372,7 +372,13 @@ def forward(; symbols: forward, Glm4MoeModel, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -372,7 +372,13 @@ def forward(
-@support_torch_compile
+@support_torch_compile(
+    dynamic_arg_dims={
+        "input_ids": 0,
+        "positions": -1,
+        "intermediate_tensors": 0,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +7/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22460 - not tie_word_embeddings for glm-4.5 and glm-4.5v

- 链接: https://github.com/vllm-project/vllm/pull/22460
- 状态/时间: merged / 2025-08-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `c152e2a8a0f4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-2，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「not tie_word_embeddings for glm-4.5 and glm-4.5v」；模型线: GLM-4.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「not tie_word_embeddings for glm-4.5 and glm-4.5v」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +0/-2 (2 lines); hunks: -601,8 +601,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +0/-2 (2 lines); hunks: -601,8 +601,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -601,8 +601,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-        if self.config.tie_word_embeddings:
-            self.lm_head.weight = self.model.embed_tokens.weight
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +0/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22203 - self.gate dtype update for GLM-4.5

- 链接: https://github.com/vllm-project/vllm/pull/22203
- 状态/时间: merged / 2025-08-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `6fa41e0c32f3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+4/-3，可读 patch 35 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「self.gate dtype update for GLM-4.5」；模型线: GLM-4.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「self.gate dtype update for GLM-4.5」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -123,6 +123,7 @@ def __init__(; -180,7 +181,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -123,6 +123,7 @@ def __init__(; -180,7 +181,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -123,6 +123,7 @@ def __init__(
+                                     params_dtype=torch.float32,
@@ -180,7 +181,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
-        router_logits, _ = self.gate(hidden_states)
+        router_logits, _ = self.gate(hidden_states.to(dtype=torch.float32))
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22143 - fuse fp32 for GLM-4.5 e_score_correction_bias

- 链接: https://github.com/vllm-project/vllm/pull/22143
- 状态/时间: merged / 2025-08-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `d3c18c9cb0b6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-3，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fuse fp32 for GLM-4.5 e_score_correction_bias」；模型线: GLM-4.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「fuse fp32 for GLM-4.5 e_score_correction_bias」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +2/-3 (5 lines); hunks: -125,9 +125,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +2/-3 (5 lines); hunks: -125,9 +125,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -125,9 +125,8 @@ def __init__(
-        # noaux_tc is not set in transformers new config now
-        self.gate.e_score_correction_bias = (nn.Parameter(
-            torch.empty(config.n_routed_experts)))
+        self.gate.e_score_correction_bias = nn.Parameter(
+            torch.empty(config.n_routed_experts, dtype=torch.float32))
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +2/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/glm4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21435 - remove GLM-4 quantization wrong Code

- 链接: https://github.com/vllm-project/vllm/pull/21435
- 状态/时间: merged / 2025-07-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/glm4_moe.py`；关联提交 `85bda9e7d053`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+2/-3，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「remove GLM-4 quantization wrong Code」；模型线: GLM-4.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/glm4_moe.py`；技术摘要: 覆盖「remove GLM-4 quantization wrong Code」；主要实现面是 `vllm/model_executor/models/glm4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/glm4_moe.py` modified +0/-1 (1 lines); hunks: -390,7 +390,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/glm4_moe.py` modified +0/-1 (1 lines); hunks: -390,7 +390,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -390,7 +390,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                quant_config=quant_config,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +0/-1
- 验证与风险: runtime 路径改动集中在 `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py`, `vllm/reasoning/glm4_moe_reasoning_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
