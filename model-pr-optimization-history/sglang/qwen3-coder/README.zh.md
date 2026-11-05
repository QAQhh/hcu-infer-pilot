# sglang Qwen3 Coder 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/Qwen/Qwen3-Coder-Next.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/Qwen/Qwen3-Coder.mdx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/qwen3-coder-480b-a35b-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/qwen3-coder-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/qwen3-coder-next-deployment.jsx` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/qwen3_coder_detector.py` | [#8371](https://github.com/sgl-project/sglang/pull/8371), [#16744](https://github.com/sgl-project/sglang/pull/16744), [#30832](https://github.com/sgl-project/sglang/pull/30832), [#44124](https://github.com/sgl-project/sglang/pull/44124) |
| `python/sglang/srt/models/qwen3.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` | [#18608](https://github.com/sgl-project/sglang/pull/18608) |
| `test/registered/amd/test_qwen3_coder_next_8gpu.py` | [#18608](https://github.com/sgl-project/sglang/pull/18608) |
| `test/registered/cpu/test_qwen3.py` | 无直接 PR 号提交 |
| `test/registered/lora/test_lora_qwen3.py` | 无直接 PR 号提交 |
| `test/registered/npu/llm_models/test_npu_qwen3_coder_480b_a35b.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 5
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 5
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2025-08-08 | [#8371](https://github.com/sgl-project/sglang/pull/8371) | merged | Update qwen3_coder_detector.py for streaming | `python/sglang/srt/function_call/qwen3_coder_detector.py` |
| 2026-01-19 | [#16744](https://github.com/sgl-project/sglang/pull/16744) | merged | support new qwen3_coder_detector | `python/sglang/srt/function_call/qwen3_coder_detector.py` |
| 2026-03-02 | [#18608](https://github.com/sgl-project/sglang/pull/18608) | merged | [AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU | `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py` |
| 2026-07-22 | [#30832](https://github.com/sgl-project/sglang/pull/30832) | merged | Add 'anyOf' schema support for qwen3_coder tool call parser | `python/sglang/srt/function_call/qwen3_coder_detector.py` |
| 2026-10-27 | [#44124](https://github.com/sgl-project/sglang/pull/44124) | merged | [Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions | `python/sglang/srt/function_call/qwen3_coder_detector.py` |

## 逐 PR diff 审计卡

### PR #8371 - Update qwen3_coder_detector.py for streaming

- 链接: https://github.com/sgl-project/sglang/pull/8371
- 状态/时间: merged / 2025-08-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/qwen3_coder_detector.py`；关联提交 `b3359dc9bf5b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+348/-67，可读 patch 510 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update qwen3_coder_detector.py for streaming」；模型线: Qwen3 Coder；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`；技术摘要: 覆盖「Update qwen3_coder_detector.py for streaming」；主要实现面是 `python/sglang/srt/function_call/qwen3_coder_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +219/-9 (228 lines); hunks: -57,6 +57,15 @@ def __init__(self):; -70,23 +79,224 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment, _parse_and_stream_parameters，涉及 `__init__, has_tool_call, parse_streaming_increment`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +219/-9 (228 lines); hunks: -57,6 +57,15 @@ def __init__(self):; -70,23 +79,224 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment, _parse_and_stream_parameters
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +219/-9
- 验证与风险: diff 自带测试面 `test/srt/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #16744 - support new qwen3_coder_detector

- 链接: https://github.com/sgl-project/sglang/pull/16744
- 状态/时间: merged / 2026-01-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/qwen3_coder_detector.py`；关联提交 `858a4d659b3e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+637/-667，可读 patch 1493 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support new qwen3_coder_detector」；模型线: Qwen3 Coder；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`；技术摘要: 覆盖「support new qwen3_coder_detector」；主要实现面是 `python/sglang/srt/function_call/qwen3_coder_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +392/-271 (663 lines); hunks: -1,12 +1,10; -17,334 +15,457; symbols: _safe_val, Qwen3CoderDetector, __init__, already，涉及 `_safe_val, Qwen3CoderDetector, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +392/-271 (663 lines); hunks: -1,12 +1,10; -17,334 +15,457; symbols: _safe_val, Qwen3CoderDetector, __init__, already
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +392/-271
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #18608 - [AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU

- 链接: https://github.com/sgl-project/sglang/pull/18608
- 状态/时间: merged / 2026-03-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`；关联提交 `98f47d817583`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+486/-0，可读 patch 488 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU」；模型线: Qwen3 Coder；类别: 文档/测试/CI；主要 diff: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`；技术摘要: 覆盖「[AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` added +302/-0 (302 lines); hunks: -0,0 +1,302; symbols: get_model_path, ModelConfig, __post_init__, get_display_name，涉及 `get_model_path, ModelConfig, __post_init__`；`test/registered/amd/test_qwen3_coder_next_8gpu.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: TestQwen3CoderNext, setUpClass, tearDownClass, test_a_gsm8k，涉及 `TestQwen3CoderNext, setUpClass, tearDownClass`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` added +302/-0 (302 lines); hunks: -0,0 +1,302; symbols: get_model_path, ModelConfig, __post_init__, get_display_name
  - `test/registered/amd/test_qwen3_coder_next_8gpu.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: TestQwen3CoderNext, setUpClass, tearDownClass, test_a_gsm8k
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` added +302/-0; `test/registered/amd/test_qwen3_coder_next_8gpu.py` added +184/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30832 - Add 'anyOf' schema support for qwen3_coder tool call parser

- 链接: https://github.com/sgl-project/sglang/pull/30832
- 状态/时间: merged / 2026-07-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/qwen3_coder_detector.py`；关联提交 `c20c48b8fd94`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+159/-7，可读 patch 215 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add 'anyOf' schema support for qwen3_coder tool call parser」；模型线: Qwen3 Coder；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`；技术摘要: 覆盖「Add 'anyOf' schema support for qwen3_coder tool call parser」；主要实现面是 `python/sglang/srt/function_call/qwen3_coder_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +9/-7 (16 lines); hunks: -11,6 +11,7; -86,6 +87,13 @@ def _get_arguments_config(; symbols: _get_arguments_config, _get_param_type, _convert_param_value，涉及 `_get_arguments_config, _get_param_type, _convert_param_value`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +9/-7 (16 lines); hunks: -11,6 +11,7; -86,6 +87,13 @@ def _get_arguments_config(; symbols: _get_arguments_config, _get_param_type, _convert_param_value
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +9/-7
- 验证与风险: diff 自带测试面 `test/registered/unit/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44124 - [Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions

- 链接: https://github.com/sgl-project/sglang/pull/44124
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/qwen3_coder_detector.py`；关联提交 `9d45fdda46d5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+240/-13，可读 patch 336 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions」；模型线: Qwen3 Coder；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/qwen3_coder_detector.py`；技术摘要: 覆盖「[Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions」；主要实现面是 `python/sglang/srt/function_call/qwen3_coder_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +58/-13 (71 lines); hunks: -1,8 +1,12; -63,10 +67,10 @@ def has_tool_call(self, text: str) -> bool:; symbols: has_tool_call, _get_arguments_config, _get_param_type，涉及 `has_tool_call, _get_arguments_config, _get_param_type`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +58/-13 (71 lines); hunks: -1,8 +1,12; -63,10 +67,10 @@ def has_tool_call(self, text: str) -> bool:; symbols: has_tool_call, _get_arguments_config, _get_param_type
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/qwen3_coder_detector.py` modified +58/-13
- 验证与风险: diff 自带测试面 `test/registered/unit/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
