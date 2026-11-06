# sglang Mistral Small 4 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/Mistral/Devstral-2.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/Mistral/Ministral-3.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/Mistral/Mistral-Large-4.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/Mistral/Mistral-Medium-3.5.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/Mistral/Mistral-Small-4.mdx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/ministral-3-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/mistral-medium-3-5-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/mistral-small-4-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/configs/mistralai/mistral-large-4-benchmarks.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/configs/mistralai/mistral-large-4.jsx` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/mistral_detector.py` | [#6597](https://github.com/sgl-project/sglang/pull/6597), [#14921](https://github.com/sgl-project/sglang/pull/14921), [#20708](https://github.com/sgl-project/sglang/pull/20708) |
| `python/sglang/srt/models/ministral3.py` | [#14251](https://github.com/sgl-project/sglang/pull/14251), [#29111](https://github.com/sgl-project/sglang/pull/29111) |
| `python/sglang/srt/models/mistral.py` | [#108](https://github.com/sgl-project/sglang/pull/108), [#5099](https://github.com/sgl-project/sglang/pull/5099), [#39185](https://github.com/sgl-project/sglang/pull/39185), [#45656](https://github.com/sgl-project/sglang/pull/45656) |
| `python/sglang/srt/models/mistral_eagle.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/mistral_large_3.py` | [#14213](https://github.com/sgl-project/sglang/pull/14213), [#14466](https://github.com/sgl-project/sglang/pull/14466), [#14485](https://github.com/sgl-project/sglang/pull/14485) |
| `python/sglang/srt/models/mistral_large_3_eagle.py` | [#14466](https://github.com/sgl-project/sglang/pull/14466), [#14485](https://github.com/sgl-project/sglang/pull/14485), [#20708](https://github.com/sgl-project/sglang/pull/20708), [#33785](https://github.com/sgl-project/sglang/pull/33785) |
| `python/sglang/srt/utils/hf_transformers/mistral_utils.py` | [#30396](https://github.com/sgl-project/sglang/pull/30396), [#35215](https://github.com/sgl-project/sglang/pull/35215), [#35915](https://github.com/sgl-project/sglang/pull/35915) |
| `test/manual/models/test_mistral_large3_basic.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models_large/test_mistral_large3.py` | 无直接 PR 号提交 |
| `test/registered/npu/vlm_models/test_npu_mistral_small_3_1_24b_instruct_2503.py` | 无直接 PR 号提交 |
| `test/registered/unit/constrained/test_mistral_common_xgrammar.py` | [#35215](https://github.com/sgl-project/sglang/pull/35215) |
| `test/registered/unit/function_call/test_mistral_detector.py` | [#21399](https://github.com/sgl-project/sglang/pull/21399) |
| `test/registered/unit/models/test_mistral3_vision_feature.py` | [#39185](https://github.com/sgl-project/sglang/pull/39185), [#45656](https://github.com/sgl-project/sglang/pull/45656) |
| `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` | [#35915](https://github.com/sgl-project/sglang/pull/35915) |

## PR 覆盖总览

- git 追溯 PR 数: 17
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 17
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2024-01-26 | [#108](https://github.com/sgl-project/sglang/pull/108) | merged | Fix Mistral model loading | `python/sglang/srt/models/mistral.py` |
| 2025-05-17 | [#5099](https://github.com/sgl-project/sglang/pull/5099) | merged | model(vlm): mistral 3.1 | `python/sglang/srt/models/mistral.py` |
| 2025-05-26 | [#6597](https://github.com/sgl-project/sglang/pull/6597) | merged | feat: Improve Mistral and Qwen25 function call parsing | `python/sglang/srt/function_call/mistral_detector.py` |
| 2025-12-04 | [#14213](https://github.com/sgl-project/sglang/pull/14213) | merged | Add Mistral Large 3 support. | `python/sglang/srt/models/mistral_large_3.py` |
| 2025-12-04 | [#14251](https://github.com/sgl-project/sglang/pull/14251) | merged | ministral3 | `python/sglang/srt/models/ministral3.py` |
| 2025-12-05 | [#14466](https://github.com/sgl-project/sglang/pull/14466) | merged | Add Mistral Large 3 Eagle Support | `python/sglang/srt/models/mistral_large_3_eagle.py`, `python/sglang/srt/models/mistral_large_3.py` |
| 2025-12-12 | [#14921](https://github.com/sgl-project/sglang/pull/14921) | merged | update mistral detector | `python/sglang/srt/function_call/mistral_detector.py` |
| 2025-12-13 | [#14485](https://github.com/sgl-project/sglang/pull/14485) | merged | Mistral Large 3 NVFP4 support | `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py` |
| 2026-03-18 | [#20708](https://github.com/sgl-project/sglang/pull/20708) | merged | Add Mistral Small 4 (Pixtral) support | `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py` |
| 2026-04-06 | [#21399](https://github.com/sgl-project/sglang/pull/21399) | merged | [CI] Add unit tests for function_call detectors (hermes, llama32, mistral) | `test/registered/unit/function_call/test_mistral_detector.py` |
| 2026-06-25 | [#29111](https://github.com/sgl-project/sglang/pull/29111) | merged | [Bugfix] Fix Ministral3 init argument forwarding | `python/sglang/srt/models/ministral3.py` |
| 2026-07-09 | [#30396](https://github.com/sgl-project/sglang/pull/30396) | merged | Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral) | `python/sglang/srt/utils/hf_transformers/mistral_utils.py` |
| 2026-08-06 | [#33785](https://github.com/sgl-project/sglang/pull/33785) | merged | Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__ | `python/sglang/srt/models/mistral_large_3_eagle.py` |
| 2026-08-19 | [#35215](https://github.com/sgl-project/sglang/pull/35215) | merged | [Constrained] Support MistralCommon tokenizers in the XGrammar backend | `test/registered/unit/constrained/test_mistral_common_xgrammar.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py` |
| 2026-08-24 | [#35915](https://github.com/sgl-project/sglang/pull/35915) | merged | [OpenAI] Drop empty assistant turns for mistral_common tokenizers | `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py` |
| 2026-09-18 | [#39185](https://github.com/sgl-project/sglang/pull/39185) | merged | Fix Mistral3 retaining every vision-tower layer to read one | `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py` |
| 2026-10-23 | [#45656](https://github.com/sgl-project/sglang/pull/45656) | merged | [Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it | `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py` |

## 逐 PR diff 审计卡

### PR #108 - Fix Mistral model loading

- 链接: https://github.com/sgl-project/sglang/pull/108
- 状态/时间: merged / 2024-01-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral.py`；关联提交 `cd6872334e9e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-0，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Mistral model loading」；模型线: Mistral Small 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mistral.py`；技术摘要: 覆盖「Fix Mistral model loading」；主要实现面是 `python/sglang/srt/models/mistral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mistral.py` added +10/-0 (10 lines); hunks: -0,0 +1,10; symbols: MistralForCausalLM, __init__，涉及 `MistralForCausalLM, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mistral.py` added +10/-0 (10 lines); hunks: -0,0 +1,10; symbols: MistralForCausalLM, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mistral.py
@@ -0,0 +1,10 @@
+"""Inference-only Mistral model."""
+from sglang.srt.models.llama2 import LlamaForCausalLM
+class MistralForCausalLM(LlamaForCausalLM):
+    def __init__(self, *args, **kwargs):
+        super().__init__(*args, **kwargs)
+EntryClass = MistralForCausalLM
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mistral.py` added +10/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/mistral.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #5099 - model(vlm): mistral 3.1

- 链接: https://github.com/sgl-project/sglang/pull/5099
- 状态/时间: merged / 2025-05-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral.py`；关联提交 `64825b839521`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+152/-21，可读 patch 272 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「model(vlm): mistral 3.1」；模型线: Mistral Small 4；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mistral.py`；技术摘要: 覆盖「model(vlm): mistral 3.1」；主要实现面是 `python/sglang/srt/models/mistral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mistral.py` modified +71/-1 (72 lines); hunks: -13,11 +13,81; symbols: MistralForCausalLM, [REDACTED_MISTRAL_API_KEY], __init__, get_image_feature，涉及 `MistralForCausalLM, [REDACTED_MISTRAL_API_KEY], __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mistral.py` modified +71/-1 (72 lines); hunks: -13,11 +13,81; symbols: MistralForCausalLM, [REDACTED_MISTRAL_API_KEY], __init__, get_image_feature
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mistral.py
@@ -13,11 +13,81 @@
+from typing import List, Union
+import torch
+from transformers.models.mistral3.modeling_mistral3 import Mistral3MultiModalProjector
+from sglang.srt.managers.schedule_batch import MultimodalDataItem
-EntryClass = MistralForCausalLM
+class [REDACTED_MISTRAL_API_KEY]:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mistral.py` modified +71/-1
- 验证与风险: diff 自带测试面 `test/srt/test_vision_openai_server.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #6597 - feat: Improve Mistral and Qwen25 function call parsing

- 链接: https://github.com/sgl-project/sglang/pull/6597
- 状态/时间: merged / 2025-05-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/mistral_detector.py`；关联提交 `16f69b1f65c6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+318/-61，可读 patch 529 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: Improve Mistral and Qwen25 function call parsing」；模型线: Mistral Small 4；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/mistral_detector.py`；技术摘要: 覆盖「feat: Improve Mistral and Qwen25 function call parsing」；主要实现面是 `python/sglang/srt/function_call/mistral_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/mistral_detector.py` modified +72/-26 (98 lines); hunks: -1,4 +1,5; -11,12 +12,14; symbols: MistralDetector, __init__, has_tool_call, _clean_text，涉及 `MistralDetector, __init__, has_tool_call`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/mistral_detector.py` modified +72/-26 (98 lines); hunks: -1,4 +1,5; -11,12 +12,14; symbols: MistralDetector, __init__, has_tool_call, _clean_text
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/mistral_detector.py
@@ -1,4 +1,5 @@
+import logging
@@ -11,12 +12,14 @@
+logger = logging.getLogger(__name__)
-      [TOOL_CALLS] [{"name":"xxx", "arguments":{...}}]
+      [TOOL_CALLS] [{"name":"func1", "arguments":{...}}, {"name":"func2", "arguments":{...}}]
@@ -32,21 +35,6 @@ def has_tool_call(self, text: str) -> bool:
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/mistral_detector.py` modified +72/-26
- 验证与风险: diff 自带测试面 `test/srt/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14213 - Add Mistral Large 3 support.

- 链接: https://github.com/sgl-project/sglang/pull/14213
- 状态/时间: merged / 2025-12-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral_large_3.py`；关联提交 `842807843671`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 16 个文件，+1400/-120，可读 patch 2012 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add Mistral Large 3 support.」；模型线: Mistral Small 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/mistral_large_3.py`；技术摘要: 覆盖「Add Mistral Large 3 support.」；主要实现面是 `python/sglang/srt/models/mistral_large_3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mistral_large_3.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: MistralLarge3ForCausalLM, load_weights, _iterable_remap_mistral_to_ds，涉及 `MistralLarge3ForCausalLM, load_weights, _iterable_remap_mistral_to_ds`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mistral_large_3.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: MistralLarge3ForCausalLM, load_weights, _iterable_remap_mistral_to_ds
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mistral_large_3.py
@@ -0,0 +1,81 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Iterable
+import regex as re
+import torch
+from sglang.srt.models.deepseek_v2 import DeepseekV3ForCausalLM
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mistral_large_3.py` added +81/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14251 - ministral3

- 链接: https://github.com/sgl-project/sglang/pull/14251
- 状态/时间: merged / 2025-12-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/ministral3.py`；关联提交 `6d37e7088337`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+245/-26，可读 patch 405 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「ministral3」；模型线: Mistral Small 4；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/ministral3.py`；技术摘要: 覆盖「ministral3」；主要实现面是 `python/sglang/srt/models/ministral3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/ministral3.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: _get_llama_4_attn_scale, Ministral3Attention, __init__, forward，涉及 `_get_llama_4_attn_scale, Ministral3Attention, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/ministral3.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: _get_llama_4_attn_scale, Ministral3Attention, __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/ministral3.py
@@ -0,0 +1,157 @@
+from typing import Any, Dict, Optional
+import torch
+from transformers import PretrainedConfig
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
+from sglang.srt.model_executor.forward_batch_info import ForwardBatch
+from sglang.srt.models.llama import (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/ministral3.py` added +157/-0
- 验证与风险: diff 自带测试面 `test/srt/models/test_ministral3_models.py`, `test/srt/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14466 - Add Mistral Large 3 Eagle Support

- 链接: https://github.com/sgl-project/sglang/pull/14466
- 状态/时间: merged / 2025-12-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`；关联提交 `205f041e9619`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+313/-62，可读 patch 550 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add Mistral Large 3 Eagle Support」；模型线: Mistral Small 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/mistral_large_3_eagle.py`, `python/sglang/srt/models/mistral_large_3.py`；技术摘要: 覆盖「Add Mistral Large 3 Eagle Support」；主要实现面是 `python/sglang/srt/models/mistral_large_3_eagle.py`, `python/sglang/srt/models/mistral_large_3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mistral_large_3_eagle.py` added +105/-0 (105 lines); hunks: -0,0 +1,105; symbols: MistralLarge3Model, __init__, forward, MistralLarge3ForCausalLMEagle，涉及 `MistralLarge3Model, __init__, forward`；`python/sglang/srt/models/mistral_large_3.py` modified +0/-3 (3 lines); hunks: -72,9 +72,6 @@ def _iterable_remap_mistral_to_ds(; symbols: _iterable_remap_mistral_to_ds，涉及 `_iterable_remap_mistral_to_ds`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mistral_large_3_eagle.py` added +105/-0 (105 lines); hunks: -0,0 +1,105; symbols: MistralLarge3Model, __init__, forward, MistralLarge3ForCausalLMEagle
  - `python/sglang/srt/models/mistral_large_3.py` modified +0/-3 (3 lines); hunks: -72,9 +72,6 @@ def _iterable_remap_mistral_to_ds(; symbols: _iterable_remap_mistral_to_ds
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -0,0 +1,105 @@
+from typing import Optional
+import torch
+from torch import nn
+from transformers import PretrainedConfig
+from python.sglang.srt.layers.attention.nsa.utils import is_nsa_enable_prefill_cp
+from sglang.srt.distributed import get_pp_group
diff -- python/sglang/srt/models/mistral_large_3.py
@@ -72,9 +72,6 @@ def _iterable_remap_mistral_to_ds(
-            if name.endswith(".weight_scale") and ".experts." not in name:
-                name = re.sub(r"\.weight_scale$", ".weight_scale_inv", name)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mistral_large_3_eagle.py` added +105/-0; `python/sglang/srt/models/mistral_large_3.py` modified +0/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14921 - update mistral detector

- 链接: https://github.com/sgl-project/sglang/pull/14921
- 状态/时间: merged / 2025-12-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/mistral_detector.py`；关联提交 `fd1ebbb0d614`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+274/-34，可读 patch 361 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「update mistral detector」；模型线: Mistral Small 4；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/mistral_detector.py`；技术摘要: 覆盖「update mistral detector」；主要实现面是 `python/sglang/srt/function_call/mistral_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/mistral_detector.py` modified +240/-34 (274 lines); hunks: -1,47 +1,49; -51,31 +53,235 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: MistralDetector, __init__, has_tool_call, detect_and_parse，涉及 `MistralDetector, __init__, has_tool_call`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/mistral_detector.py` modified +240/-34 (274 lines); hunks: -1,47 +1,49; -51,31 +53,235 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: MistralDetector, __init__, has_tool_call, detect_and_parse
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/mistral_detector.py
@@ -1,47 +1,49 @@
-import re
-from typing import List
+from typing import Any, List, Optional, Tuple
+    ToolCallItem,
+from sglang.srt.function_call.utils import _is_complete_json
-    Detector for Mistral model function call format.
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/mistral_detector.py` modified +240/-34
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14485 - Mistral Large 3 NVFP4 support

- 链接: https://github.com/sgl-project/sglang/pull/14485
- 状态/时间: merged / 2025-12-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`；关联提交 `f6031adf0875`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+502/-36，可读 patch 707 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Mistral Large 3 NVFP4 support」；模型线: Mistral Small 4；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`；技术摘要: 覆盖「Mistral Large 3 NVFP4 support」；主要实现面是 `python/sglang/srt/models/mistral_large_3.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mistral_large_3.py` modified +1/-1 (2 lines); hunks: -1,5 +1,5；`python/sglang/srt/models/mistral_large_3_eagle.py` modified +2/-0 (2 lines); hunks: -1,3 +1,5。
- 代码 diff 细节:
  - `python/sglang/srt/models/mistral_large_3.py` modified +1/-1 (2 lines); hunks: -1,5 +1,5
  - `python/sglang/srt/models/mistral_large_3_eagle.py` modified +2/-0 (2 lines); hunks: -1,3 +1,5
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mistral_large_3.py
@@ -1,5 +1,5 @@
+# Adapted from https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mistral_large_3.py
-# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -1,3 +1,5 @@
+# Adapted from https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mistral_large_3_eagle.py
+# SPDX-License-Identifier: Apache-2.0
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mistral_large_3.py` modified +1/-1; `python/sglang/srt/models/mistral_large_3_eagle.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20708 - Add Mistral Small 4 (Pixtral) support

- 链接: https://github.com/sgl-project/sglang/pull/20708
- 状态/时间: merged / 2026-03-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`；关联提交 `6b8a6545b231`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 18 个文件，+360/-124，可读 patch 868 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add Mistral Small 4 (Pixtral) support」；模型线: Mistral Small 4；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`；技术摘要: 覆盖「Add Mistral Small 4 (Pixtral) support」；主要实现面是 `python/sglang/srt/function_call/mistral_detector.py`, `python/sglang/srt/models/mistral_large_3_eagle.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/mistral_detector.py` modified +17/-9 (26 lines); hunks: -90,19 +90,27 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: detect_and_parse, parse_streaming_increment，涉及 `detect_and_parse, parse_streaming_increment`；`python/sglang/srt/models/mistral_large_3_eagle.py` modified +11/-3 (14 lines); hunks: -18,7 +18,10; -99,9 +102,14 @@ def __init__(; symbols: MistralLarge3Model, MistralLarge3EagleModel, __init__，涉及 `MistralLarge3Model, MistralLarge3EagleModel, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/mistral_detector.py` modified +17/-9 (26 lines); hunks: -90,19 +90,27 @@ def detect_and_parse(self, text: str, tools: List[Tool]) ->...; symbols: detect_and_parse, parse_streaming_increment
  - `python/sglang/srt/models/mistral_large_3_eagle.py` modified +11/-3 (14 lines); hunks: -18,7 +18,10; -99,9 +102,14 @@ def __init__(; symbols: MistralLarge3Model, MistralLarge3EagleModel, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/mistral_detector.py
@@ -90,19 +90,27 @@ def detect_and_parse(self, text: str, tools: List[Tool]) -> StreamingParseResult
-        parsed = self._try_parse_compact_args_format(tool_part)
-        if not parsed:
+        # Loop to extract all consecutive compact tool calls.
+        all_calls: list = []
+        remaining = tool_part
+        while remaining:
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -18,7 +18,10 @@
-class MistralLarge3Model(DeepseekV2Model):
+class MistralLarge3EagleModel(DeepseekV2Model):
+    """EAGLE draft model with an fc layer that fuses token embeddings and
+    target-model hidden states before passing through transformer layers."""
@@ -99,9 +102,14 @@ def __init__(
-        config.quant_config = quant_config
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/mistral_detector.py` modified +17/-9; `python/sglang/srt/models/mistral_large_3_eagle.py` modified +11/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/deepseek_ocr.py`, `python/sglang/srt/configs/deepseekvl2.py`, `python/sglang/srt/configs/janus_pro.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21399 - [CI] Add unit tests for function_call detectors (hermes, llama32, mistral)

- 链接: https://github.com/sgl-project/sglang/pull/21399
- 状态/时间: merged / 2026-04-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/unit/function_call/test_mistral_detector.py`；关联提交 `30f5b8760851`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+595/-0，可读 patch 598 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Add unit tests for function_call detectors (hermes, llama32, mistral)」；模型线: Mistral Small 4；类别: 文档/测试/CI；主要 diff: `test/registered/unit/function_call/test_mistral_detector.py`；技术摘要: 覆盖「[CI] Add unit tests for function_call detectors (hermes, llama32, mistral)」；主要实现面是 `test/registered/unit/function_call/test_mistral_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/function_call/test_mistral_detector.py` added +224/-0 (224 lines); hunks: -0,0 +1,224; symbols: TestMistralDetector, setUp, test_has_tool_call_json_array_format, test_has_tool_call_compact_format，涉及 `TestMistralDetector, setUp, test_has_tool_call_json_array_format`。
- 代码 diff 细节:
  - `test/registered/unit/function_call/test_mistral_detector.py` added +224/-0 (224 lines); hunks: -0,0 +1,224; symbols: TestMistralDetector, setUp, test_has_tool_call_json_array_format, test_has_tool_call_compact_format
- 关键代码摘录:

```diff
diff -- test/registered/unit/function_call/test_mistral_detector.py
@@ -0,0 +1,224 @@
+"""Unit tests for MistralDetector — no server, no model loading."""
+import json
+from sglang.srt.entrypoints.openai.protocol import Function, Tool
+from sglang.srt.function_call.mistral_detector import MistralDetector
+from sglang.test.ci.ci_register import register_cpu_ci
+from sglang.test.test_utils import CustomTestCase
```

- 已读文件:
  - tests: `test/registered/unit/function_call/test_mistral_detector.py` added +224/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/function_call/test_hermes_detector.py`, `test/registered/unit/function_call/test_llama32_detector.py`, `test/registered/unit/function_call/test_mistral_detector.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29111 - [Bugfix] Fix Ministral3 init argument forwarding

- 链接: https://github.com/sgl-project/sglang/pull/29111
- 状态/时间: merged / 2026-06-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/ministral3.py`；关联提交 `ddda4f90288b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+37/-17，可读 patch 99 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Ministral3 init argument forwarding」；模型线: Mistral Small 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/ministral3.py`；技术摘要: 覆盖「[Bugfix] Fix Ministral3 init argument forwarding」；主要实现面是 `python/sglang/srt/models/ministral3.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/ministral3.py` modified +37/-17 (54 lines); hunks: -31,6 +31,7 @@ def __init__(; -40,18 +41,19 @@ def __init__(; symbols: __init__, forward, Ministral3DecoderLayer，涉及 `__init__, forward, Ministral3DecoderLayer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/ministral3.py` modified +37/-17 (54 lines); hunks: -31,6 +31,7 @@ def __init__(; -40,18 +41,19 @@ def __init__(; symbols: __init__, forward, Ministral3DecoderLayer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/ministral3.py
@@ -31,6 +31,7 @@ def __init__(
+        start_layer: int = 0,
@@ -40,18 +41,19 @@ def __init__(
-            config,
-            hidden_size,
-            num_heads,
-            num_kv_heads,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/ministral3.py` modified +37/-17
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/ministral3.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30396 - Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral)

- 链接: https://github.com/sgl-project/sglang/pull/30396
- 状态/时间: merged / 2026-07-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/utils/hf_transformers/mistral_utils.py`；关联提交 `7132af28de0b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+138/-12，可读 patch 190 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral)」；模型线: Mistral Small 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/utils/hf_transformers/mistral_utils.py`；技术摘要: 覆盖「Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral)」；主要实现面是 `python/sglang/srt/utils/hf_transformers/mistral_utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +34/-1 (35 lines); hunks: -11,7 +11,12; -430,6 +435,34 @@ def wrap_as_pixtral(processor, config):; symbols: adapt_config_dict, wrap_as_pixtral, is_bare_tekken_checkpoint, retry_without_mistral_common_kwargs，涉及 `adapt_config_dict, wrap_as_pixtral, is_bare_tekken_checkpoint`。
- 代码 diff 细节:
  - `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +34/-1 (35 lines); hunks: -11,7 +11,12; -430,6 +435,34 @@ def wrap_as_pixtral(processor, config):; symbols: adapt_config_dict, wrap_as_pixtral, is_bare_tekken_checkpoint, retry_without_mistral_common_kwargs
- 关键代码摘录:

```diff
diff -- python/sglang/srt/utils/hf_transformers/mistral_utils.py
@@ -11,7 +11,12 @@
-from .common import _ensure_sub_configs, download_from_hf
+from .common import (
+    _cached_file_exists,
+    _ensure_sub_configs,
+    _remote_file_exists,
+    download_from_hf,
```

- 已读文件:
  - runtime: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +34/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/tokenizer/test_tekken_tokenizer_routing.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33785 - Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__

- 链接: https://github.com/sgl-project/sglang/pull/33785
- 状态/时间: merged / 2026-08-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral_large_3_eagle.py`；关联提交 `dd7e4c91e2e1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+25/-54，可读 patch 118 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__」；模型线: Mistral Small 4；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mistral_large_3_eagle.py`；技术摘要: 覆盖「Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__」；主要实现面是 `python/sglang/srt/models/mistral_large_3_eagle.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mistral_large_3_eagle.py` modified +6/-46 (52 lines); hunks: -4,19 +4,12; -31,50 +24,17 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mistral_large_3_eagle.py` modified +6/-46 (52 lines); hunks: -4,19 +4,12; -31,50 +24,17 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mistral_large_3_eagle.py
@@ -4,19 +4,12 @@
-from torch import nn
-from sglang.srt.configs.model_config import is_deepseek_dsa
-from sglang.srt.distributed import get_pp_group
-from sglang.srt.layers.attention.dsa.utils import is_dsa_enable_prefill_cp
-from sglang.srt.layers.layernorm import RMSNorm
-from sglang.srt.layers.utils.cp_utils import is_prefill_context_parallel_enabled
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mistral_large_3_eagle.py` modified +6/-46
- 验证与风险: diff 自带测试面 `test/registered/8-gpu-models/test_mistral_large3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35215 - [Constrained] Support MistralCommon tokenizers in the XGrammar backend

- 链接: https://github.com/sgl-project/sglang/pull/35215
- 状态/时间: merged / 2026-08-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `test/registered/unit/constrained/test_mistral_common_xgrammar.py`；关联提交 `3391ab3712bb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+168/-1，可读 patch 189 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Constrained] Support MistralCommon tokenizers in the XGrammar backend」；模型线: Mistral Small 4；类别: 文档/测试/CI；主要 diff: `test/registered/unit/constrained/test_mistral_common_xgrammar.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`；技术摘要: 覆盖「[Constrained] Support MistralCommon tokenizers in the XGrammar backend」；主要实现面是 `test/registered/unit/constrained/test_mistral_common_xgrammar.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/constrained/test_mistral_common_xgrammar.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: _StubTekkenizer, __init__, id_to_piece, id_to_byte_piece，涉及 `_StubTekkenizer, __init__, id_to_piece`；`python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +43/-0 (43 lines); hunks: -634,4 +634,47 @@ def _safe_apply_chat_template(messages, **kwargs):; symbols: _safe_apply_chat_template, init_xgrammar，涉及 `_safe_apply_chat_template, init_xgrammar`。
- 代码 diff 细节:
  - `test/registered/unit/constrained/test_mistral_common_xgrammar.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: _StubTekkenizer, __init__, id_to_piece, id_to_byte_piece
  - `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +43/-0 (43 lines); hunks: -634,4 +634,47 @@ def _safe_apply_chat_template(messages, **kwargs):; symbols: _safe_apply_chat_template, init_xgrammar
- 关键代码摘录:

```diff
diff -- test/registered/unit/constrained/test_mistral_common_xgrammar.py
@@ -0,0 +1,112 @@
+import sys
+import pytest
+from sglang.srt.utils.hf_transformers.mistral_utils import (
+    patch_mistral_common_tokenizer,
+)
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/utils/hf_transformers/mistral_utils.py
@@ -634,4 +634,47 @@ def _safe_apply_chat_template(messages, **kwargs):
+    def init_xgrammar():
+        from xgrammar import TokenizerInfo
+        tekken = getattr(
+            getattr(tokenizer.tokenizer, "instruct_tokenizer", None), "tokenizer", None
+        )
+        if tekken is None or not hasattr(tekken, "id_to_byte_piece"):
```

- 已读文件:
  - tests: `test/registered/unit/constrained/test_mistral_common_xgrammar.py` added +112/-0
  - runtime: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +43/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/constrained/test_mistral_common_xgrammar.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35915 - [OpenAI] Drop empty assistant turns for mistral_common tokenizers

- 链接: https://github.com/sgl-project/sglang/pull/35915
- 状态/时间: merged / 2026-08-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`；关联提交 `0c1e9bda5773`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+125/-0，可读 patch 136 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[OpenAI] Drop empty assistant turns for mistral_common tokenizers」；模型线: Mistral Small 4；类别: 文档/测试/CI；主要 diff: `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`；技术摘要: 覆盖「[OpenAI] Drop empty assistant turns for mistral_common tokenizers」；主要实现面是 `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` added +86/-0 (86 lines); hunks: -0,0 +1,86; symbols: _user, _assistant, _MistralCommonStub, name，涉及 `_user, _assistant, _MistralCommonStub`；`python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +39/-0 (39 lines); hunks: -628,9 +628,48 @@ def _adapt_placeholder_messages_for_mistral_common(messages):; symbols: _adapt_placeholder_messages_for_mistral_common, _assistant_content_is_empty, _drop_empty_assistant_messages, _safe_apply_chat_template，涉及 `_adapt_placeholder_messages_for_mistral_common, _assistant_content_is_empty, _drop_empty_assistant_messages`。
- 代码 diff 细节:
  - `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` added +86/-0 (86 lines); hunks: -0,0 +1,86; symbols: _user, _assistant, _MistralCommonStub, name
  - `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +39/-0 (39 lines); hunks: -628,9 +628,48 @@ def _adapt_placeholder_messages_for_mistral_common(messages):; symbols: _adapt_placeholder_messages_for_mistral_common, _assistant_content_is_empty, _drop_empty_assistant_messages, _safe_apply_chat_template
- 关键代码摘录:

```diff
diff -- test/registered/unit/tokenizer/test_mistral_empty_assistant.py
@@ -0,0 +1,86 @@
+import unittest
+from sglang.srt.utils.hf_transformers.mistral_utils import (
+    patch_mistral_common_tokenizer,
+)
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=3, suite="base-a-test-cpu")
diff -- python/sglang/srt/utils/hf_transformers/mistral_utils.py
@@ -628,9 +628,48 @@ def _adapt_placeholder_messages_for_mistral_common(messages):
+    def _assistant_content_is_empty(content):
+        if content is None:
+            return True
+        if isinstance(content, str):
+            return not content.strip()
+        if isinstance(content, list):
```

- 已读文件:
  - tests: `test/registered/unit/tokenizer/test_mistral_empty_assistant.py` added +86/-0
  - runtime: `python/sglang/srt/utils/hf_transformers/mistral_utils.py` modified +39/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39185 - Fix Mistral3 retaining every vision-tower layer to read one

- 链接: https://github.com/sgl-project/sglang/pull/39185
- 状态/时间: merged / 2026-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral.py`, `test/registered/unit/models/test_mistral3_vision_feature.py`；关联提交 `2394b231c226`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+133/-12，可读 patch 168 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Mistral3 retaining every vision-tower layer to read one」；模型线: Mistral Small 4；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`；技术摘要: 覆盖「Fix Mistral3 retaining every vision-tower layer to read one」；主要实现面是 `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_mistral3_vision_feature.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: RecordingTower, __init__, __call__, _model，涉及 `RecordingTower, __init__, __call__`；`python/sglang/srt/models/mistral.py` modified +12/-6 (18 lines); hunks: -115,16 +115,22 @@ def get_image_feature(self, items: List[MultimodalDataItem...; symbols: get_image_feature，涉及 `get_image_feature`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_mistral3_vision_feature.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: RecordingTower, __init__, __call__, _model
  - `python/sglang/srt/models/mistral.py` modified +12/-6 (18 lines); hunks: -115,16 +115,22 @@ def get_image_feature(self, items: List[MultimodalDataItem...; symbols: get_image_feature
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_mistral3_vision_feature.py
@@ -0,0 +1,109 @@
+"""Pixtral adaptors should not ask the vision tower for every layer to read one.
+The tower materialises one hidden-state tensor per layer when hidden states are
+requested, ~49x the tensor the model actually consumes. These tests pin that the
+final-layer case takes the cheap path and that both paths agree, for each
+adaptor that reads the Pixtral tower this way.
+"""
diff -- python/sglang/srt/models/mistral.py
@@ -115,16 +115,22 @@ def get_image_feature(self, items: List[MultimodalDataItem]) -> torch.Tensor:
+        # Requesting hidden states materialises one tensor per layer (~1.8 GiB per
+        # 1540px image); the plain forward returns the same tensor as the last entry.
+        last_layer_only = self.vision_feature_layer == -1
-            image_outputs = self.vision_tower(
-                pixel_values, image_sizes, output_hidden_states=True
-            )
```

- 已读文件:
  - tests: `test/registered/unit/models/test_mistral3_vision_feature.py` added +109/-0
  - runtime: `python/sglang/srt/models/mistral.py` modified +12/-6
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_mistral3_vision_feature.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45656 - [Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it

- 链接: https://github.com/sgl-project/sglang/pull/45656
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mistral.py`, `test/registered/unit/models/test_mistral3_vision_feature.py`；关联提交 `4542fc8f598e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+125/-27，可读 patch 223 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it」；模型线: Mistral Small 4；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`；技术摘要: 覆盖「[Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it」；主要实现面是 `test/registered/unit/models/test_mistral3_vision_feature.py`, `python/sglang/srt/models/mistral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_mistral3_vision_feature.py` modified +107/-1 (108 lines); hunks: -6,6 +6,8; -15,7 +17,7; symbols: test_features_are_concatenated_per_item, _bare_mistral3, RecordingLoader, __init__，涉及 `test_features_are_concatenated_per_item, _bare_mistral3, RecordingLoader`；`python/sglang/srt/models/mistral.py` modified +15/-25 (40 lines); hunks: -15,14 +15,17; -88,22 +91,18 @@ def _remap_mistral_to_llama(; symbols: _remap_mistral_to_llama, [REDACTED_MISTRAL_API_KEY], __init__，涉及 `_remap_mistral_to_llama, [REDACTED_MISTRAL_API_KEY], __init__`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_mistral3_vision_feature.py` modified +107/-1 (108 lines); hunks: -6,6 +6,8; -15,7 +17,7; symbols: test_features_are_concatenated_per_item, _bare_mistral3, RecordingLoader, __init__
  - `python/sglang/srt/models/mistral.py` modified +15/-25 (40 lines); hunks: -15,14 +15,17; -88,22 +91,18 @@ def _remap_mistral_to_llama(; symbols: _remap_mistral_to_llama, [REDACTED_MISTRAL_API_KEY], __init__
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_mistral3_vision_feature.py
@@ -6,6 +6,8 @@
+import subprocess
+import sys
@@ -15,7 +17,7 @@
-register_cpu_ci(est_time=10, suite="base-a-test-cpu")
+register_cpu_ci(est_time=40, suite="base-a-test-cpu")
@@ -105,5 +107,109 @@ def test_features_are_concatenated_per_item(self):
diff -- python/sglang/srt/models/mistral.py
@@ -15,14 +15,17 @@
-from typing import List
+from typing import List, Optional
+from transformers import LlavaConfig
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
+from sglang.srt.models.llava import LlavaForConditionalGeneration
@@ -88,22 +91,18 @@ def _remap_mistral_to_llama(
```

- 已读文件:
  - tests: `test/registered/unit/models/test_mistral3_vision_feature.py` modified +107/-1
  - runtime: `python/sglang/srt/models/mistral.py` modified +15/-25
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_mistral3_vision_feature.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
