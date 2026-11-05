# sglang ERNIE 4.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` | [#42303](https://github.com/sgl-project/sglang/pull/42303) |
| `python/sglang/srt/models/ernie45_moe_vl.py` | [#42303](https://github.com/sgl-project/sglang/pull/42303), [#42304](https://github.com/sgl-project/sglang/pull/42304) |
| `python/sglang/srt/models/ernie45_vl.py` | 无直接 PR 号提交 |
| `python/sglang/srt/multimodal/processors/ernie45_vl.py` | 无直接 PR 号提交 |
| `test/manual/models/test_ernie45_vl_visual_mask.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 2
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 2
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-03 | [#42303](https://github.com/sgl-project/sglang/pull/42303) | merged | [Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues | `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` |
| 2026-10-03 | [#42304](https://github.com/sgl-project/sglang/pull/42304) | merged | [Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries | `python/sglang/srt/models/ernie45_moe_vl.py` |

## 逐 PR diff 审计卡

### PR #42303 - [Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues

- 链接: https://github.com/sgl-project/sglang/pull/42303
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`, `python/sglang/srt/models/ernie45_moe_vl.py`；关联提交 `f89ead192f3c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+65/-10，可读 patch 168 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues」；模型线: ERNIE 4.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`；技术摘要: 覆盖「[Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues」；主要实现面是 `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/ernie45_moe_vl.py` modified +0/-2 (2 lines); hunks: -25,7 +25,6; -479,7 +478,6 @@ def __init__(; symbols: __init__，涉及 `__init__`；`python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` added +19/-0 (19 lines); hunks: -0,0 +1,19; symbols: _ernie45_vl_overrides，涉及 `_ernie45_vl_overrides`。
- 代码 diff 细节:
  - `python/sglang/srt/models/ernie45_moe_vl.py` modified +0/-2 (2 lines); hunks: -25,7 +25,6; -479,7 +478,6 @@ def __init__(; symbols: __init__
  - `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` added +19/-0 (19 lines); hunks: -0,0 +1,19; symbols: _ernie45_vl_overrides
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/ernie45_moe_vl.py
@@ -25,7 +25,6 @@
-from sglang.srt.layers.dp_attention import is_dp_attention_enabled
@@ -479,7 +478,6 @@ def __init__(
-                enable_tp=not is_dp_attention_enabled(),
diff -- python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py
@@ -0,0 +1,19 @@
+"""Config-time override declarations for ernie45_vl."""
+from typing import Any
+from sglang.srt.arg_groups.model_override_base import (
+    _register_for,
+    resolving_view,
+)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/ernie45_moe_vl.py` modified +0/-2; `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py` added +19/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42304 - [Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries

- 链接: https://github.com/sgl-project/sglang/pull/42304
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/ernie45_moe_vl.py`；关联提交 `2fa17a64671b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+126/-100，可读 patch 403 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries」；模型线: ERNIE 4.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/ernie45_moe_vl.py`；技术摘要: 覆盖「[Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries」；主要实现面是 `python/sglang/srt/models/ernie45_moe_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/ernie45_moe_vl.py` modified +66/-58 (124 lines); hunks: -16,15 +16,18; -107,6 +110,7 @@ def __init__(; symbols: __init__, forward, _is_moe_layer, Ernie4_5_VLMoeDecoderLayer，涉及 `__init__, forward, _is_moe_layer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/ernie45_moe_vl.py` modified +66/-58 (124 lines); hunks: -16,15 +16,18; -107,6 +110,7 @@ def __init__(; symbols: __init__, forward, _is_moe_layer, Ernie4_5_VLMoeDecoderLayer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/ernie45_moe_vl.py
@@ -16,15 +16,18 @@
-from typing import Any, Dict, Optional, Tuple, Union
+from typing import Any, Dict, Optional, Union
-from sglang.srt.distributed import (
-    tensor_model_parallel_all_reduce,
+from sglang.srt.layers.layer_boundary import (
+    declare_attn,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/ernie45_moe_vl.py` modified +66/-58
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/models/exaone_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
