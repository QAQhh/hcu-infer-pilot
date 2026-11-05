# sglang Qwen3 Coder Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/Qwen/Qwen3-Coder-Next.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/Qwen/Qwen3-Coder.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/qwen3-coder-480b-a35b-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/qwen3-coder-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/qwen3-coder-next-deployment.jsx` | no direct PR-number commit |
| `python/sglang/srt/function_call/qwen3_coder_detector.py` | [#8371](https://github.com/sgl-project/sglang/pull/8371), [#16744](https://github.com/sgl-project/sglang/pull/16744), [#30832](https://github.com/sgl-project/sglang/pull/30832), [#44124](https://github.com/sgl-project/sglang/pull/44124) |
| `python/sglang/srt/models/qwen3.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` | [#18608](https://github.com/sgl-project/sglang/pull/18608) |
| `test/registered/amd/test_qwen3_coder_next_8gpu.py` | [#18608](https://github.com/sgl-project/sglang/pull/18608) |
| `test/registered/cpu/test_qwen3.py` | no direct PR-number commit |
| `test/registered/lora/test_lora_qwen3.py` | no direct PR-number commit |
| `test/registered/npu/llm_models/test_npu_qwen3_coder_480b_a35b.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 5
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 5
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-08-08 | [#8371](https://github.com/sgl-project/sglang/pull/8371) | merged | Update qwen3_coder_detector.py for streaming | `python/sglang/srt/function_call/qwen3_coder_detector.py` |
| 2026-01-19 | [#16744](https://github.com/sgl-project/sglang/pull/16744) | merged | support new qwen3_coder_detector | `python/sglang/srt/function_call/qwen3_coder_detector.py` |
| 2026-03-02 | [#18608](https://github.com/sgl-project/sglang/pull/18608) | merged | [AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU | `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py` |
| 2026-07-22 | [#30832](https://github.com/sgl-project/sglang/pull/30832) | merged | Add 'anyOf' schema support for qwen3_coder tool call parser | `python/sglang/srt/function_call/qwen3_coder_detector.py` |
| 2026-10-27 | [#44124](https://github.com/sgl-project/sglang/pull/44124) | merged | [Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions | `python/sglang/srt/function_call/qwen3_coder_detector.py` |

## Per-PR Diff Audit Cards

### PR #8371 - Update qwen3_coder_detector.py for streaming

- Link: https://github.com/sgl-project/sglang/pull/8371
- Status/date: merged / 2025-08-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/qwen3_coder_detector.py`; associated commits `b3359dc9bf5b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +348/-67, 510 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Update qwen3_coder_detector.py for streaming"; model line: Qwen3 Coder; category: model implementation change; main diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`; technical summary: Covers "Update qwen3_coder_detector.py for streaming"; the main implementation surface is `python/sglang/srt/function_call/qwen3_coder_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +219/-9 (228 lines); hunks: -57,6 +57,15 @@ def __init__(self):; -70,23 +79,224 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment, _parse_and_stream_parameters, touching `__init__, has_tool_call, parse_streaming_increment`.
- Code diff details:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +219/-9 (228 lines); hunks: -57,6 +57,15 @@ def __init__(self):; -70,23 +79,224 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment, _parse_and_stream_parameters
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/qwen3_coder_detector.py
@@ -57,6 +57,15 @@ def __init__(self):
+        # Streaming state variables
+        self._current_function_name: str = ""
+        self._current_parameters: Dict[str, Any] = {}
+        self._streamed_parameters: Dict[str, str] = (
+            {}
+        )  # Track what parameter content we've streamed
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +219/-9
- Risk and verification: The diff ships test coverage in `test/srt/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #16744 - support new qwen3_coder_detector

- Link: https://github.com/sgl-project/sglang/pull/16744
- Status/date: merged / 2026-01-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/qwen3_coder_detector.py`; associated commits `858a4d659b3e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +637/-667, 1493 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support new qwen3_coder_detector"; model line: Qwen3 Coder; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`; technical summary: Covers "support new qwen3_coder_detector"; the main implementation surface is `python/sglang/srt/function_call/qwen3_coder_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +392/-271 (663 lines); hunks: -1,12 +1,10; -17,334 +15,457; symbols: _safe_val, Qwen3CoderDetector, __init__, already, touching `_safe_val, Qwen3CoderDetector, __init__`.
- Code diff details:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +392/-271 (663 lines); hunks: -1,12 +1,10; -17,334 +15,457; symbols: _safe_val, Qwen3CoderDetector, __init__, already
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/qwen3_coder_detector.py
@@ -1,12 +1,10 @@
-import html
-from typing import Any, Dict, List, Tuple
+from typing import Any, List, Optional
-from sglang.srt.environ import envs
@@ -17,334 +15,457 @@
-def _safe_val(raw: str) -> Any:
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +392/-271
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #18608 - [AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU

- Link: https://github.com/sgl-project/sglang/pull/18608
- Status/date: merged / 2026-03-02
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`; associated commits `98f47d817583`
- Diff scope read: GitHub Pull Request files API returned 2 files, +486/-0, 488 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU"; model line: Qwen3 Coder; category: docs/tests/CI; main diff: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`; technical summary: Covers "[AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` added +302/-0 (302 lines); hunks: -0,0 +1,302; symbols: get_model_path, ModelConfig, __post_init__, get_display_name, touching `get_model_path, ModelConfig, __post_init__`; `test/registered/amd/test_qwen3_coder_next_8gpu.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: TestQwen3CoderNext, setUpClass, tearDownClass, test_a_gsm8k, touching `TestQwen3CoderNext, setUpClass, tearDownClass`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` added +302/-0 (302 lines); hunks: -0,0 +1,302; symbols: get_model_path, ModelConfig, __post_init__, get_display_name
  - `test/registered/amd/test_qwen3_coder_next_8gpu.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: TestQwen3CoderNext, setUpClass, tearDownClass, test_a_gsm8k
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py
@@ -0,0 +1,302 @@
+"""MI35x Qwen3-Coder-Next GSM8K Completion Evaluation Test (8-GPU)
+Tests Qwen3-Coder-Next model with basic and MTP configurations
+using few-shot completion benchmark on MI35x.
+Registry: nightly-amd-8-gpu-mi35x-qwen3-coder-next suite
+"""
+import ast
diff -- test/registered/amd/test_qwen3_coder_next_8gpu.py
@@ -0,0 +1,184 @@
+"""MI35x Qwen3-Coder-Next Functionality Test (8-GPU)
+Tests Qwen3-Coder-Next model with basic configuration
+on MI35x. Covers GSM8K accuracy and BS=1 decode speed.
+Server args match run_qwen3-coder-next_spec.sh.
+Registry: stage-c-test-large-8-gpu-amd-mi35x-qwen3-coder-next suite
+"""
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` added +302/-0; `test/registered/amd/test_qwen3_coder_next_8gpu.py` added +184/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30832 - Add 'anyOf' schema support for qwen3_coder tool call parser

- Link: https://github.com/sgl-project/sglang/pull/30832
- Status/date: merged / 2026-07-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/qwen3_coder_detector.py`; associated commits `c20c48b8fd94`
- Diff scope read: GitHub Pull Request files API returned 3 files, +159/-7, 215 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add 'anyOf' schema support for qwen3_coder tool call parser"; model line: Qwen3 Coder; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`; technical summary: Covers "Add 'anyOf' schema support for qwen3_coder tool call parser"; the main implementation surface is `python/sglang/srt/function_call/qwen3_coder_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +9/-7 (16 lines); hunks: -11,6 +11,7; -86,6 +87,13 @@ def _get_arguments_config(; symbols: _get_arguments_config, _get_param_type, _convert_param_value, touching `_get_arguments_config, _get_param_type, _convert_param_value`.
- Code diff details:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +9/-7 (16 lines); hunks: -11,6 +11,7; -86,6 +87,13 @@ def _get_arguments_config(; symbols: _get_arguments_config, _get_param_type, _convert_param_value
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/qwen3_coder_detector.py
@@ -11,6 +11,7 @@
+from sglang.srt.function_call.utils import infer_type_from_json_schema
@@ -86,6 +87,13 @@ def _get_arguments_config(
+    def _get_param_type(self, param_schema: Any) -> str:
+        """Infer the parser conversion type from a JSON schema parameter."""
+        inferred_type = infer_type_from_json_schema(param_schema)
+        if inferred_type is None:
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +9/-7
- Risk and verification: The diff ships test coverage in `test/registered/unit/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #44124 - [Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions

- Link: https://github.com/sgl-project/sglang/pull/44124
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/qwen3_coder_detector.py`; associated commits `9d45fdda46d5`
- Diff scope read: GitHub Pull Request files API returned 2 files, +240/-13, 336 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions"; model line: Qwen3 Coder; category: bug fix; main diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`; technical summary: Covers "[Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions"; the main implementation surface is `python/sglang/srt/function_call/qwen3_coder_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +58/-13 (71 lines); hunks: -1,8 +1,12; -63,10 +67,10 @@ def has_tool_call(self, text: str) -> bool:; symbols: has_tool_call, _get_arguments_config, _get_param_type, touching `has_tool_call, _get_arguments_config, _get_param_type`.
- Code diff details:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +58/-13 (71 lines); hunks: -1,8 +1,12; -63,10 +67,10 @@ def has_tool_call(self, text: str) -> bool:; symbols: has_tool_call, _get_arguments_config, _get_param_type
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/qwen3_coder_detector.py
@@ -1,8 +1,12 @@
+import math
+from jsonschema import Draft202012Validator
+from referencing import Registry
@@ -63,10 +67,10 @@ def has_tool_call(self, text: str) -> bool:
-    ) -> dict:
-        """Extract argument configuration for a function."""
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +58/-13
- Risk and verification: The diff ships test coverage in `test/registered/unit/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
