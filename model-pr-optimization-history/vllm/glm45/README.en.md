# vllm GLM-4.5 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/reasoning/test_glm4_moe_reasoning_parser.py` | no direct PR-number commit |
| `tests/tool_parsers/test_glm4_moe_tool_parser.py` | [#39601](https://github.com/vllm-project/vllm/pull/39601) |
| `vllm/model_executor/models/glm4_moe.py` | [#21435](https://github.com/vllm-project/vllm/pull/21435), [#22143](https://github.com/vllm-project/vllm/pull/22143), [#22203](https://github.com/vllm-project/vllm/pull/22203), [#22460](https://github.com/vllm-project/vllm/pull/22460), [#22520](https://github.com/vllm-project/vllm/pull/22520), [#22832](https://github.com/vllm-project/vllm/pull/22832), [#24849](https://github.com/vllm-project/vllm/pull/24849), [#25830](https://github.com/vllm-project/vllm/pull/25830), [#41755](https://github.com/vllm-project/vllm/pull/41755), [#44313](https://github.com/vllm-project/vllm/pull/44313) |
| `vllm/model_executor/models/glm4_moe_lite.py` | no direct PR-number commit |
| `vllm/model_executor/models/glm4_moe_lite_mtp.py` | [#62234](https://github.com/vllm-project/vllm/pull/62234) |
| `vllm/model_executor/models/glm4_moe_mtp.py` | [#27597](https://github.com/vllm-project/vllm/pull/27597), [#28805](https://github.com/vllm-project/vllm/pull/28805), [#44313](https://github.com/vllm-project/vllm/pull/44313), [#62234](https://github.com/vllm-project/vllm/pull/62234) |

## PR Coverage Summary

- Git-traced PRs: 14
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 14

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
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

## Per-PR Diff Audit Cards

### PR #62234 - [Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden.

- Link: https://github.com/vllm-project/vllm/pull/62234
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`; associated commits `62966a7e00c4`
- Diff scope read: GitHub Pull Request files API returned 9 files, +166/-14, 282 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden."; model line: GLM-4.5; category: bug fix; main diff: `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`; technical summary: Covers "[Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden."; the main implementation surface is `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe_lite_mtp.py` modified +7/-5 (12 lines); hunks: -156,8 +156,12 @@ def forward(; -214,9 +218,7 @@ def compute_logits(; symbols: forward, Glm4MoeLiteMultiTokenPredictor, compute_logits, touching `forward, Glm4MoeLiteMultiTokenPredictor, compute_logits`; `vllm/model_executor/models/glm4_moe_mtp.py` modified +7/-5 (12 lines); hunks: -127,8 +127,12 @@ def forward(; -188,9 +192,7 @@ def compute_logits(; symbols: forward, Glm4MoeMultiTokenPredictor, compute_logits, touching `forward, Glm4MoeMultiTokenPredictor, compute_logits`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe_lite_mtp.py` modified +7/-5 (12 lines); hunks: -156,8 +156,12 @@ def forward(; -214,9 +218,7 @@ def compute_logits(; symbols: forward, Glm4MoeLiteMultiTokenPredictor, compute_logits
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +7/-5 (12 lines); hunks: -127,8 +127,12 @@ def forward(; -188,9 +192,7 @@ def compute_logits(; symbols: forward, Glm4MoeMultiTokenPredictor, compute_logits
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe_lite_mtp.py` modified +7/-5; `vllm/model_executor/models/glm4_moe_mtp.py` modified +7/-5
- Risk and verification: The diff ships test coverage in `tests/v1/e2e/spec_decode/mtp/glm/__init__.py`, `tests/v1/e2e/spec_decode/mtp/glm/test_mtp.py`, `tests/v1/spec_decode/test_llm_base_proposer_sampling.py`, `tests/v1/spec_decode/test_mtp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #44313 - [ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7

- Link: https://github.com/vllm-project/vllm/pull/44313
- Status/date: merged / 2026-06-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`; associated commits `c7ca0bccae66`
- Diff scope read: GitHub Pull Request files API returned 2 files, +254/-105, 482 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7"; model line: GLM-4.5; category: performance/backend optimization; main diff: `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`; technical summary: Covers "[ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +138/-63 (201 lines); hunks: -32,6 +32,7; -168,7 +169,16 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`; `vllm/model_executor/models/glm4_moe_mtp.py` modified +116/-42 (158 lines); hunks: -24,12 +24,14; -239,6 +241,10 @@ def compute_logits(; symbols: compute_logits, load_weights, touching `compute_logits, load_weights`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +138/-63 (201 lines); hunks: -32,6 +32,7; -168,7 +169,16 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +116/-42 (158 lines); hunks: -24,12 +24,14; -239,6 +241,10 @@ def compute_logits(; symbols: compute_logits, load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +138/-63; `vllm/model_executor/models/glm4_moe_mtp.py` modified +116/-42
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #39601 - [Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format

- Link: https://github.com/vllm-project/vllm/pull/39601
- Status/date: merged / 2026-05-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_glm4_moe_tool_parser.py`; associated commits `050611a3dd19`
- Diff scope read: GitHub Pull Request files API returned 2 files, +135/-25, 214 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format"; model line: GLM-4.5; category: bug fix; main diff: `tests/tool_parsers/test_glm4_moe_tool_parser.py`; technical summary: Covers "[Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format"; the main implementation surface is `tests/tool_parsers/test_glm4_moe_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +120/-0 (120 lines); hunks: -5,6 +5,7; -1363,3 +1364,122 @@ def test_stream_interval_content_between_tool_calls(; symbols: test_stream_interval_content_between_tool_calls, function_tools, glm4_moe_parser_function_tools, mock_request_function_tools, touching `test_stream_interval_content_between_tool_calls, function_tools, glm4_moe_parser_function_tools`.
- Code diff details:
  - `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +120/-0 (120 lines); hunks: -5,6 +5,7; -1363,3 +1364,122 @@ def test_stream_interval_content_between_tool_calls(; symbols: test_stream_interval_content_between_tool_calls, function_tools, glm4_moe_parser_function_tools, mock_request_function_tools
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_glm4_moe_tool_parser.py` modified +120/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_glm4_moe_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41755 - [Bugfix] Fix GLM4-MoE weight loading for NVFP4 quantized checkpoints

- Link: https://github.com/vllm-project/vllm/pull/41755
- Status/date: merged / 2026-05-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `75f0d516c43c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +10/-2, 27 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix GLM4-MoE weight loading for NVFP4 quantized checkpoints"; model line: GLM-4.5; category: bug fix; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "[Bugfix] Fix GLM4-MoE weight loading for NVFP4 quantized checkpoints"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +10/-2 (12 lines); hunks: -506,16 +506,24 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +10/-2 (12 lines); hunks: -506,16 +506,24 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +10/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28805 - [BugFix] Fix glm4_moe_mtp load weights bug

- Link: https://github.com/vllm-project/vllm/pull/28805
- Status/date: merged / 2025-11-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe_mtp.py`; associated commits `ab01cd14e5e2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-4, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix] Fix glm4_moe_mtp load weights bug"; model line: GLM-4.5; category: bug fix; main diff: `vllm/model_executor/models/glm4_moe_mtp.py`; technical summary: Covers "[BugFix] Fix glm4_moe_mtp load weights bug"; the main implementation surface is `vllm/model_executor/models/glm4_moe_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe_mtp.py` modified +3/-4 (7 lines); hunks: -256,13 +256,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +3/-4 (7 lines); hunks: -256,13 +256,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe_mtp.py` modified +3/-4
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27597 - [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint.

- Link: https://github.com/vllm-project/vllm/pull/27597
- Status/date: merged / 2025-11-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe_mtp.py`; associated commits `d3ade61e429f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-4, 23 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint."; model line: GLM-4.5; category: bug fix; main diff: `vllm/model_executor/models/glm4_moe_mtp.py`; technical summary: Covers "[Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint."; the main implementation surface is `vllm/model_executor/models/glm4_moe_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4 (15 lines); hunks: -256,11 +256,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe_mtp.py` modified +11/-4
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25830 - Update GLM-4.5 Doc transformers version

- Link: https://github.com/vllm-project/vllm/pull/25830
- Status/date: merged / 2025-09-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `b1ded114b976`
- Diff scope read: GitHub Pull Request files API returned 4 files, +7/-5, 40 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Update GLM-4.5 Doc transformers version"; model line: GLM-4.5; category: docs/tests/CI; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "Update GLM-4.5 Doc transformers version"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -21,7 +21,7.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +1/-1 (2 lines); hunks: -21,7 +21,7
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -21,7 +21,7 @@
-"""Inference-only GLM-4.5 model compatible with HuggingFace weights."""
+"""Inference-only GLM-4.5, GLM-4.6 model compatible with HuggingFace weights."""
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #24849 - [Model] Apply SharedFusedMoE to glm4_moe.

- Link: https://github.com/vllm-project/vllm/pull/24849
- Status/date: merged / 2025-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `c15309a730fa`
- Diff scope read: GitHub Pull Request files API returned 1 files, +55/-30, 114 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Apply SharedFusedMoE to glm4_moe."; model line: GLM-4.5; category: performance/backend optimization; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "[Model] Apply SharedFusedMoE to glm4_moe."; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +55/-30 (85 lines); hunks: -46,6 +46,7; -146,25 +147,6 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +55/-30 (85 lines); hunks: -46,6 +46,7; -146,25 +147,6 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +55/-30
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22832 - [Model] Modify the gate implementation of glm4_moe

- Link: https://github.com/vllm-project/vllm/pull/22832
- Status/date: merged / 2025-08-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `92ff41abea13`
- Diff scope read: GitHub Pull Request files API returned 2 files, +11/-11, 50 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Modify the gate implementation of glm4_moe"; model line: GLM-4.5; category: model implementation change; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "[Model] Modify the gate implementation of glm4_moe"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +10/-10 (20 lines); hunks: -41,7 +41,6; -118,14 +117,15 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +10/-10 (20 lines); hunks: -41,7 +41,6; -118,14 +117,15 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +10/-10
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22520 - GLM-4.5V with new class name at transformers

- Link: https://github.com/vllm-project/vllm/pull/22520
- Status/date: merged / 2025-08-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `a6022e6fbcbd`
- Diff scope read: GitHub Pull Request files API returned 5 files, +13/-6, 61 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "GLM-4.5V with new class name at transformers"; model line: GLM-4.5; category: model implementation change; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "GLM-4.5V with new class name at transformers"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +7/-1 (8 lines); hunks: -372,7 +372,13 @@ def forward(; symbols: forward, Glm4MoeModel, __init__, touching `forward, Glm4MoeModel, __init__`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +7/-1 (8 lines); hunks: -372,7 +372,13 @@ def forward(; symbols: forward, Glm4MoeModel, __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +7/-1
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22460 - not tie_word_embeddings for glm-4.5 and glm-4.5v

- Link: https://github.com/vllm-project/vllm/pull/22460
- Status/date: merged / 2025-08-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `c152e2a8a0f4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-2, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "not tie_word_embeddings for glm-4.5 and glm-4.5v"; model line: GLM-4.5; category: model implementation change; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "not tie_word_embeddings for glm-4.5 and glm-4.5v"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +0/-2 (2 lines); hunks: -601,8 +601,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +0/-2 (2 lines); hunks: -601,8 +601,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -601,8 +601,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-        if self.config.tie_word_embeddings:
-            self.lm_head.weight = self.model.embed_tokens.weight
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +0/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22203 - self.gate dtype update for GLM-4.5

- Link: https://github.com/vllm-project/vllm/pull/22203
- Status/date: merged / 2025-08-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `6fa41e0c32f3`
- Diff scope read: GitHub Pull Request files API returned 3 files, +4/-3, 35 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "self.gate dtype update for GLM-4.5"; model line: GLM-4.5; category: model implementation change; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "self.gate dtype update for GLM-4.5"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -123,6 +123,7 @@ def __init__(; -180,7 +181,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +2/-1 (3 lines); hunks: -123,6 +123,7 @@ def __init__(; -180,7 +181,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -123,6 +123,7 @@ def __init__(
+                                     params_dtype=torch.float32,
@@ -180,7 +181,7 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
-        router_logits, _ = self.gate(hidden_states)
+        router_logits, _ = self.gate(hidden_states.to(dtype=torch.float32))
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +2/-1
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22143 - fuse fp32 for GLM-4.5 e_score_correction_bias

- Link: https://github.com/vllm-project/vllm/pull/22143
- Status/date: merged / 2025-08-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `d3c18c9cb0b6`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-3, 12 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fuse fp32 for GLM-4.5 e_score_correction_bias"; model line: GLM-4.5; category: performance/backend optimization; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "fuse fp32 for GLM-4.5 e_score_correction_bias"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +2/-3 (5 lines); hunks: -125,9 +125,8 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +2/-3 (5 lines); hunks: -125,9 +125,8 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -125,9 +125,8 @@ def __init__(
-        # noaux_tc is not set in transformers new config now
-        self.gate.e_score_correction_bias = (nn.Parameter(
-            torch.empty(config.n_routed_experts)))
+        self.gate.e_score_correction_bias = nn.Parameter(
+            torch.empty(config.n_routed_experts, dtype=torch.float32))
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +2/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/glm4_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21435 - remove GLM-4 quantization wrong Code

- Link: https://github.com/vllm-project/vllm/pull/21435
- Status/date: merged / 2025-07-24
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/glm4_moe.py`; associated commits `85bda9e7d053`
- Diff scope read: GitHub Pull Request files API returned 3 files, +2/-3, 26 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "remove GLM-4 quantization wrong Code"; model line: GLM-4.5; category: bug fix; main diff: `vllm/model_executor/models/glm4_moe.py`; technical summary: Covers "remove GLM-4 quantization wrong Code"; the main implementation surface is `vllm/model_executor/models/glm4_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/glm4_moe.py` modified +0/-1 (1 lines); hunks: -390,7 +390,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/glm4_moe.py` modified +0/-1 (1 lines); hunks: -390,7 +390,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/glm4_moe.py
@@ -390,7 +390,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                quant_config=quant_config,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/glm4_moe.py` modified +0/-1
- Risk and verification: Runtime changes concentrate in `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`, `vllm/model_executor/models/glm4_moe.py`, `vllm/reasoning/glm4_moe_reasoning_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
