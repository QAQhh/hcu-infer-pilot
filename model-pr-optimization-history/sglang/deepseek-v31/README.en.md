# sglang DeepSeek V3.1 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `examples/chat_template/tool_chat_template_deepseekv31.jinja` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#9895](https://github.com/sgl-project/sglang/pull/9895), [#14837](https://github.com/sgl-project/sglang/pull/14837) |
| `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` | no direct PR-number commit |
| `python/sglang/srt/function_call/deepseekv31_detector.py` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#11589](https://github.com/sgl-project/sglang/pull/11589), [#13394](https://github.com/sgl-project/sglang/pull/13394) |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/a8w8_blockscale_bpreshuffle_tuned_gemm.csv` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=2048-K=7168.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=7168-K=2048.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=8192-K=1536.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_tune.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_act.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_moe.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/triton_qk_rmsnorm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/moe_transport.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/utils.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_v2.py` | [#13954](https://github.com/sgl-project/sglang/pull/13954) |
| `test/manual/nightly/test_deepseek_v31_perf.py` | no direct PR-number commit |
| `test/manual/test_deepseek_v31.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v31_eval_amd.py` | no direct PR-number commit |
| `test/registered/amd/perf/mi30x/test_deepseek_v31_perf.py` | no direct PR-number commit |
| `test/registered/xpu/llm_models/test_xpu_deepseek_v2_lite_chat_fp8_gsm8k_eval.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 6
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 6
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-08-27 | [#9446](https://github.com/sgl-project/sglang/pull/9446) | merged | Support DeepSeek-V3.1 tool call | `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-09-03 | [#9895](https://github.com/sgl-project/sglang/pull/9895) | merged | Update tool_chat_template_deepseekv31.jinja | `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-11-14 | [#11589](https://github.com/sgl-project/sglang/pull/11589) | merged | [Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector | `python/sglang/srt/function_call/deepseekv31_detector.py` |
| 2025-11-26 | [#13954](https://github.com/sgl-project/sglang/pull/13954) | merged | Fix Deepseek v3.1 loading issue | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-10 | [#14837](https://github.com/sgl-project/sglang/pull/14837) | merged | [Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210) | `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-12-31 | [#13394](https://github.com/sgl-project/sglang/pull/13394) | merged | Fix DeepSeekV31's structural tag trigger | `python/sglang/srt/function_call/deepseekv31_detector.py` |

## Per-PR Diff Audit Cards

### PR #9446 - Support DeepSeek-V3.1 tool call

- Link: https://github.com/sgl-project/sglang/pull/9446
- Status/date: merged / 2025-08-27
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv31.jinja`, `python/sglang/srt/function_call/deepseekv31_detector.py`; associated commits `b9683be6538e`
- Diff scope read: GitHub Pull Request files API returned 3 files, +315/-0, 331 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support DeepSeek-V3.1 tool call"; model line: DeepSeek V3.1; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "Support DeepSeek-V3.1 tool call"; the main implementation surface is `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse, touching `DeepSeekV31Detector, __init__, has_tool_call`; `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -0,0 +1,222 @@
+import json
+import logging
+import re
+from typing import List
+from sglang.srt.entrypoints.openai.protocol import Tool
+from sglang.srt.function_call.base_format_detector import BaseFormatDetector
diff -- examples/chat_template/tool_chat_template_deepseekv31.jinja
@@ -0,0 +1,91 @@
+{% if not add_generation_prompt is defined %}
+  {% set add_generation_prompt = false %}
+{% endif %}
+{% if not thinking is defined %}
+  {% set thinking = false %}
+{% endif %}
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv31_detector.py`, `python/sglang/srt/function_call/function_call_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9895 - Update tool_chat_template_deepseekv31.jinja

- Link: https://github.com/sgl-project/sglang/pull/9895
- Status/date: merged / 2025-09-03
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv31.jinja`; associated commits `cc9a31c66226`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-3, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Update tool_chat_template_deepseekv31.jinja"; model line: DeepSeek V3.1; category: model implementation change; main diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "Update tool_chat_template_deepseekv31.jinja"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13.
- Code diff details:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13
- Key code excerpts:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv31.jinja
@@ -43,13 +43,13 @@
-          {{'<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments'] + '<｜tool▁call▁end｜>'}}
+          {{'<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments']|tojson + '<｜tool▁call▁end｜>'}}
-          {{message['content'] + '<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>' + tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments'] + '<｜tool▁call▁end｜>'}}
+          {{message['content'] + '<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>' + tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments']|tojson + '<｜tool▁call▁end｜>'
-        {{'<｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments'] + '<｜tool▁call▁end｜>'}}
+        {{'<｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments']|tojson + '<｜tool▁call▁end｜>'}}
```

- Reviewed files:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3
- Risk and verification: This is mostly docs/examples in `examples/chat_template/tool_chat_template_deepseekv31.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #11589 - [Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector

- Link: https://github.com/sgl-project/sglang/pull/11589
- Status/date: merged / 2025-11-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv31_detector.py`; associated commits `fc5da1e80b78`
- Diff scope read: GitHub Pull Request files API returned 1 files, +4/-9, 34 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector"; model line: DeepSeek V3.1; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv31_detector.py`; technical summary: Covers "[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector"; the main implementation surface is `python/sglang/srt/function_call/deepseekv31_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment, touching `parse_streaming_increment`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -115,13 +115,14 @@ def parse_streaming_increment(
-                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*)<｜tool▁call▁end｜>",
+                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*?)(<｜tool▁call▁end｜>|$)",
+                is_tool_end = partial_match.group(3)
@@ -180,15 +181,9 @@ def parse_streaming_increment(
-                        tool_call_end_pattern = (
-                            r"<｜tool▁call▁begin｜>.*?<｜tool▁call▁end｜>"
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv31_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13954 - Fix Deepseek v3.1 loading issue

- Link: https://github.com/sgl-project/sglang/pull/13954
- Status/date: merged / 2025-11-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `13e5beeab499`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Deepseek v3.1 loading issue"; model line: DeepSeek V3.1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix Deepseek v3.1 loading issue"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights, touching `post_load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
-                        and self_attn.kv_b_proj.executed_weight_requant_ue8m0
+                        and weight_scale.format_ue8m0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14837 - [Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)

- Link: https://github.com/sgl-project/sglang/pull/14837
- Status/date: merged / 2025-12-10
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv31.jinja`; associated commits `ef1ab2302ab2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)"; model line: DeepSeek V3.1; category: model implementation change; main diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11.
- Code diff details:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11
- Key code excerpts:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv31.jinja
@@ -19,7 +19,11 @@
-    {% set tool_ns.text = tool_ns.text + '\n### ' + tool.function.name + '\nDescription: ' + tool.function.description + '\n\nParameters: ' + (tool.function.parameters | tojson) +
+    {% if tool.function.description is not none %}
+      {% set tool_ns.text = tool_ns.text + '\n### ' + tool.function.name + '\nDescription: ' + tool.function.description + '\n\nParameters: ' + (tool.function.parameters | tojson)
+    {% else %}
+      {% set tool_ns.text = tool_ns.text + '\n### ' + tool.function.name + '\n\nParameters: ' + (tool.function.parameters | tojson) + '\n' %}
+    {% endif %}
```

- Reviewed files:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1
- Risk and verification: This is mostly docs/examples in `examples/chat_template/tool_chat_template_deepseekv31.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #13394 - Fix DeepSeekV31's structural tag trigger

- Link: https://github.com/sgl-project/sglang/pull/13394
- Status/date: merged / 2025-12-31
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv31_detector.py`; associated commits `2667c857a78f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 7 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix DeepSeekV31's structural tag trigger"; model line: DeepSeek V3.1; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv31_detector.py`; technical summary: Covers "Fix DeepSeekV31's structural tag trigger"; the main implementation surface is `python/sglang/srt/function_call/deepseekv31_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info, touching `structure_info`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:
-            trigger="<｜tool▁call▁begin｜>" + name + "<｜tool▁sep｜>",
+            trigger="<｜tool▁call▁begin｜>",
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv31_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
