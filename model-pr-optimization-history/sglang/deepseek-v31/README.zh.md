# sglang DeepSeek V3.1 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `examples/chat_template/tool_chat_template_deepseekv31.jinja` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#9895](https://github.com/sgl-project/sglang/pull/9895), [#14837](https://github.com/sgl-project/sglang/pull/14837) |
| `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/deepseekv31_detector.py` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#11589](https://github.com/sgl-project/sglang/pull/11589), [#13394](https://github.com/sgl-project/sglang/pull/13394) |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/a8w8_blockscale_bpreshuffle_tuned_gemm.csv` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=2048-K=7168.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=7168-K=2048.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=8192-K=1536.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_tune.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_act.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_moe.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/triton_qk_rmsnorm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/moe_transport.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/utils.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_v2.py` | [#13954](https://github.com/sgl-project/sglang/pull/13954) |
| `test/manual/nightly/test_deepseek_v31_perf.py` | 无直接 PR 号提交 |
| `test/manual/test_deepseek_v31.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v31_eval_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi30x/test_deepseek_v31_perf.py` | 无直接 PR 号提交 |
| `test/registered/xpu/llm_models/test_xpu_deepseek_v2_lite_chat_fp8_gsm8k_eval.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 6
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 6
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2025-08-27 | [#9446](https://github.com/sgl-project/sglang/pull/9446) | merged | Support DeepSeek-V3.1 tool call | `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-09-03 | [#9895](https://github.com/sgl-project/sglang/pull/9895) | merged | Update tool_chat_template_deepseekv31.jinja | `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-11-14 | [#11589](https://github.com/sgl-project/sglang/pull/11589) | merged | [Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector | `python/sglang/srt/function_call/deepseekv31_detector.py` |
| 2025-11-26 | [#13954](https://github.com/sgl-project/sglang/pull/13954) | merged | Fix Deepseek v3.1 loading issue | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-10 | [#14837](https://github.com/sgl-project/sglang/pull/14837) | merged | [Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210) | `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-12-31 | [#13394](https://github.com/sgl-project/sglang/pull/13394) | merged | Fix DeepSeekV31's structural tag trigger | `python/sglang/srt/function_call/deepseekv31_detector.py` |

## 逐 PR diff 审计卡

### PR #9446 - Support DeepSeek-V3.1 tool call

- 链接: https://github.com/sgl-project/sglang/pull/9446
- 状态/时间: merged / 2025-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv31.jinja`, `python/sglang/srt/function_call/deepseekv31_detector.py`；关联提交 `b9683be6538e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+315/-0，可读 patch 331 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support DeepSeek-V3.1 tool call」；模型线: DeepSeek V3.1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「Support DeepSeek-V3.1 tool call」；主要实现面是 `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse，涉及 `DeepSeekV31Detector, __init__, has_tool_call`；`examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv31_detector.py`, `python/sglang/srt/function_call/function_call_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9895 - Update tool_chat_template_deepseekv31.jinja

- 链接: https://github.com/sgl-project/sglang/pull/9895
- 状态/时间: merged / 2025-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；关联提交 `cc9a31c66226`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-3，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update tool_chat_template_deepseekv31.jinja」；模型线: DeepSeek V3.1；类别: 模型实现调整；主要 diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「Update tool_chat_template_deepseekv31.jinja」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13。
- 代码 diff 细节:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13
- 关键代码摘录:

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

- 已读文件:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3
- 验证与风险: 该 PR 主要落在文档/示例 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #11589 - [Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector

- 链接: https://github.com/sgl-project/sglang/pull/11589
- 状态/时间: merged / 2025-11-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv31_detector.py`；关联提交 `fc5da1e80b78`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-9，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector」；模型线: DeepSeek V3.1；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv31_detector.py`；技术摘要: 覆盖「[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector」；主要实现面是 `python/sglang/srt/function_call/deepseekv31_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment，涉及 `parse_streaming_increment`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv31_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13954 - Fix Deepseek v3.1 loading issue

- 链接: https://github.com/sgl-project/sglang/pull/13954
- 状态/时间: merged / 2025-11-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `13e5beeab499`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Deepseek v3.1 loading issue」；模型线: DeepSeek V3.1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix Deepseek v3.1 loading issue」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights，涉及 `post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
-                        and self_attn.kv_b_proj.executed_weight_requant_ue8m0
+                        and weight_scale.format_ue8m0
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14837 - [Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)

- 链接: https://github.com/sgl-project/sglang/pull/14837
- 状态/时间: merged / 2025-12-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；关联提交 `ef1ab2302ab2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)」；模型线: DeepSeek V3.1；类别: 模型实现调整；主要 diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11。
- 代码 diff 细节:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11
- 关键代码摘录:

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

- 已读文件:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1
- 验证与风险: 该 PR 主要落在文档/示例 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #13394 - Fix DeepSeekV31's structural tag trigger

- 链接: https://github.com/sgl-project/sglang/pull/13394
- 状态/时间: merged / 2025-12-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv31_detector.py`；关联提交 `2667c857a78f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 7 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix DeepSeekV31's structural tag trigger」；模型线: DeepSeek V3.1；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv31_detector.py`；技术摘要: 覆盖「Fix DeepSeekV31's structural tag trigger」；主要实现面是 `python/sglang/srt/function_call/deepseekv31_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info，涉及 `structure_info`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:
-            trigger="<｜tool▁call▁begin｜>" + name + "<｜tool▁sep｜>",
+            trigger="<｜tool▁call▁begin｜>",
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv31_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
