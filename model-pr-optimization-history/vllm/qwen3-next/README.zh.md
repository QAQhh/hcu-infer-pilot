# vllm Qwen3 Next 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `vllm/model_executor/models/qwen3_next.py` | [#24526](https://github.com/vllm-project/vllm/pull/24526), [#24709](https://github.com/vllm-project/vllm/pull/24709), [#24957](https://github.com/vllm-project/vllm/pull/24957), [#24960](https://github.com/vllm-project/vllm/pull/24960), [#25079](https://github.com/vllm-project/vllm/pull/25079), [#25243](https://github.com/vllm-project/vllm/pull/25243), [#25268](https://github.com/vllm-project/vllm/pull/25268), [#26437](https://github.com/vllm-project/vllm/pull/26437), [#27030](https://github.com/vllm-project/vllm/pull/27030), [#27578](https://github.com/vllm-project/vllm/pull/27578), [#28202](https://github.com/vllm-project/vllm/pull/28202), [#28267](https://github.com/vllm-project/vllm/pull/28267), ... (23 total) |
| `vllm/model_executor/models/qwen3_next_mtp.py` | [#24526](https://github.com/vllm-project/vllm/pull/24526), [#25079](https://github.com/vllm-project/vllm/pull/25079), [#39280](https://github.com/vllm-project/vllm/pull/39280), [#62111](https://github.com/vllm-project/vllm/pull/62111) |

## PR 覆盖总览

- git 追溯 PR 数: 24
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 24

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-30 | [#62111](https://github.com/vllm-project/vllm/pull/62111) | merged | [Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next | `vllm/model_executor/models/qwen3_next_mtp.py` |
| 2026-05-08 | [#39280](https://github.com/vllm-project/vllm/pull/39280) | merged | [ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next | `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py` |
| 2026-04-08 | [#39181](https://github.com/vllm-project/vllm/pull/39181) | merged | [Bugfix]Fix EP precision for Qwen3.5, Qwen3-Next | `vllm/model_executor/models/qwen3_next.py` |
| 2026-03-18 | [#37427](https://github.com/vllm-project/vllm/pull/37427) | merged | [Bugfix] Fix ROCm crash in qwen3_next multi-stream events (#36795) | `vllm/model_executor/models/qwen3_next.py` |
| 2026-03-18 | [#36795](https://github.com/vllm-project/vllm/pull/36795) | merged | [Perf] Enable dual stream execution of input projection for Qwen3 | `vllm/model_executor/models/qwen3_next.py` |
| 2026-03-10 | [#36242](https://github.com/vllm-project/vllm/pull/36242) | merged | [Bugfix] Fix Qwen3-Next in_proj_ba weight sharding with TP > 1 | `vllm/model_executor/models/qwen3_next.py` |
| 2026-03-09 | [#35777](https://github.com/vllm-project/vllm/pull/35777) | merged | [Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next | `vllm/model_executor/models/qwen3_next.py` |
| 2026-02-18 | [#34697](https://github.com/vllm-project/vllm/pull/34697) | merged | [Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion | `vllm/model_executor/models/qwen3_next.py` |
| 2026-02-13 | [#34489](https://github.com/vllm-project/vllm/pull/34489) | merged | [Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5 | `vllm/model_executor/models/qwen3_next.py` |
| 2026-01-08 | [#31719](https://github.com/vllm-project/vllm/pull/31719) | merged | [Misc] Support qwen3-next lora | `vllm/model_executor/models/qwen3_next.py` |
| 2025-12-13 | [#30433](https://github.com/vllm-project/vllm/pull/30433) | merged | [Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\} | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-19 | [#28960](https://github.com/vllm-project/vllm/pull/28960) | merged | [Bugfix] Fix typo in Qwen3 Next model executor | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-11 | [#28202](https://github.com/vllm-project/vllm/pull/28202) | merged | [Bugfix] fix qwen3-next crash | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-09 | [#28267](https://github.com/vllm-project/vllm/pull/28267) | merged | [Misc] Add some comments in qwen3-next | `vllm/model_executor/models/qwen3_next.py` |
| 2025-10-29 | [#27578](https://github.com/vllm-project/vllm/pull/27578) | merged | [perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next | `vllm/model_executor/models/qwen3_next.py` |
| 2025-10-17 | [#27030](https://github.com/vllm-project/vllm/pull/27030) | merged | [Bugfix][Qwen] fixes the weights dtype in qwen3_next: it is actually a bfloat16 | `vllm/model_executor/models/qwen3_next.py` |
| 2025-10-16 | [#26437](https://github.com/vllm-project/vllm/pull/26437) | merged | [PERF] Qwen3-next MTP speedup (change bool mask indexing to index_select / index_copy to reduce d2h) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-09-20 | [#25268](https://github.com/vllm-project/vllm/pull/25268) | merged | [BUGFIX] GPTQ quantization compatibility for Qwen3 Next MOE models (AutoGPTQ and AutoRound-GPTQ) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-09-19 | [#25243](https://github.com/vllm-project/vllm/pull/25243) | merged | [Qwen] Remove cuda hard-code in qwen3 next | `vllm/model_executor/models/qwen3_next.py` |
| 2025-09-18 | [#25079](https://github.com/vllm-project/vllm/pull/25079) | merged | [Qwen] Add fp8 checkpoint support for qwen3-next. | `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py` |
| 2025-09-18 | [#24960](https://github.com/vllm-project/vllm/pull/24960) | merged | [Bugfix][Qwen3-Next] add prefixes to shared_expert in qwen3-next and mlp in qwen2moe to successfully load ignored params in quantized models | `vllm/model_executor/models/qwen3_next.py` |
| 2025-09-17 | [#24957](https://github.com/vllm-project/vllm/pull/24957) | merged | [Bugfix][Qwen3-Next] fixes the varlen issue in qwen3-next's MTP implementation. | `vllm/model_executor/models/qwen3_next.py` |
| 2025-09-12 | [#24709](https://github.com/vllm-project/vllm/pull/24709) | merged | [BugFix] Fix Qwen3-Next PP | `vllm/model_executor/models/qwen3_next.py` |
| 2025-09-11 | [#24526](https://github.com/vllm-project/vllm/pull/24526) | merged | Add the support for the qwen3 next model (a hybrid attention model). | `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`, `vllm/transformers_utils/configs/qwen3_next.py` |

## 逐 PR diff 审计卡

### PR #62111 - [Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next

- 链接: https://github.com/vllm-project/vllm/pull/62111
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next_mtp.py`；关联提交 `dd5f5eebd7a0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+222/-16，可读 patch 388 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next_mtp.py`；技术摘要: 覆盖「[Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next」；主要实现面是 `vllm/model_executor/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4 (23 lines); hunks: -41,7 +41,17; -171,7 +181,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights, Qwen3NextMTP，涉及 `should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4 (23 lines); hunks: -41,7 +41,17; -171,7 +181,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights, Qwen3NextMTP
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next_mtp.py
@@ -41,7 +41,17 @@
-@support_torch_compile
+def should_torch_compile_mtp_drafter(vllm_config: VllmConfig) -> bool:
+    """`enable_if` for MTP drafters that pick their module by `spec_step_idx`.
+    The drafter is compiled once with guards dropped, so a compiled
+    multi-module drafter would reuse the first-traced module for every step.
+    """
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4
- 验证与风险: diff 自带测试面 `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/test_qwen3_5_mtp_config.py`, `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39280 - [ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next

- 链接: https://github.com/vllm-project/vllm/pull/39280
- 状态/时间: merged / 2026-05-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`；关联提交 `2c6b59b80771`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+359/-10，可读 patch 573 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`；技术摘要: 覆盖「[ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +26/-4 (30 lines); hunks: -8,6 +8,7; -135,7 +136,12 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/model_executor/models/qwen3_next_mtp.py` modified +14/-1 (15 lines); hunks: -7,6 +7,7; -147,20 +148,32 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +26/-4 (30 lines); hunks: -8,6 +8,7; -135,7 +136,12 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__, forward
  - `vllm/model_executor/models/qwen3_next_mtp.py` modified +14/-1 (15 lines); hunks: -7,6 +7,7; -147,20 +148,32 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -8,6 +8,7 @@
+from vllm._aiter_ops import rocm_aiter_ops
@@ -135,7 +136,12 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):
-        if config.shared_expert_intermediate_size > 0:
+        if (
+            rocm_aiter_ops.is_fusion_moe_shared_experts_enabled()
+            or config.shared_expert_intermediate_size <= 0
diff -- vllm/model_executor/models/qwen3_next_mtp.py
@@ -7,6 +7,7 @@
+from vllm._aiter_ops import rocm_aiter_ops
@@ -147,20 +148,32 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+        is_fse = rocm_aiter_ops.is_fusion_moe_shared_experts_enabled()
+        num_experts = self.config.num_experts
+        if is_fse:
+            num_experts += 1
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +26/-4; `vllm/model_executor/models/qwen3_next_mtp.py` modified +14/-1
- 验证与风险: runtime 路径改动集中在 `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #39181 - [Bugfix]Fix EP precision for Qwen3.5, Qwen3-Next

- 链接: https://github.com/vllm-project/vllm/pull/39181
- 状态/时间: merged / 2026-04-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `f3c7941ec8d3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-0，可读 patch 32 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix]Fix EP precision for Qwen3.5, Qwen3-Next」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix]Fix EP precision for Qwen3.5, Qwen3-Next」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -140,6 +140,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -140,6 +140,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -140,6 +140,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):
+                is_sequence_parallel=self.is_sequence_parallel,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen2_moe.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37427 - [Bugfix] Fix ROCm crash in qwen3_next multi-stream events (#36795)

- 链接: https://github.com/vllm-project/vllm/pull/37427
- 状态/时间: merged / 2026-03-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `a913b612d8a8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix ROCm crash in qwen3_next multi-stream events (#36795)」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix] Fix ROCm crash in qwen3_next multi-stream events (#36795)」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -426,7 +426,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -426,7 +426,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -426,7 +426,7 @@ def __init__(
-            if current_platform.is_cuda()
+            if current_platform.is_cuda_alike()
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #36795 - [Perf] Enable dual stream execution of input projection for Qwen3

- 链接: https://github.com/vllm-project/vllm/pull/36795
- 状态/时间: merged / 2026-03-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `a913b612d8a8`, `f1740006e47d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+115/-5，可读 patch 174 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Enable dual stream execution of input projection for Qwen3」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Perf] Enable dual stream execution of input projection for Qwen3」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +61/-3 (64 lines); hunks: -82,7 +82,11; -419,6 +423,12 @@ def __init__(; symbols: __init__, forward, _warmup_prefill_kernels, _forward_in_proj，涉及 `__init__, forward, _warmup_prefill_kernels`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +61/-3 (64 lines); hunks: -82,7 +82,11; -419,6 +423,12 @@ def __init__(; symbols: __init__, forward, _warmup_prefill_kernels, _forward_in_proj
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -82,7 +82,11 @@
-from vllm.utils.torch_utils import direct_register_custom_op
+from vllm.utils.multi_stream_utils import maybe_execute_in_parallel
+from vllm.utils.torch_utils import (
+    aux_stream,
+    direct_register_custom_op,
+)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +61/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`, `vllm/utils/multi_stream_utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #36242 - [Bugfix] Fix Qwen3-Next in_proj_ba weight sharding with TP > 1

- 链接: https://github.com/vllm-project/vllm/pull/36242
- 状态/时间: merged / 2026-03-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `4e95ec111cd1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+45/-6，可读 patch 72 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Qwen3-Next in_proj_ba weight sharding with TP > 1」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix] Fix Qwen3-Next in_proj_ba weight sharding with TP > 1」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +27/-6 (33 lines); hunks: -412,12 +412,11 @@ def __init__(; -497,6 +496,28 @@ def create_qkvz_proj(; symbols: __init__, create_qkvz_proj, create_ba_proj, fix_query_key_value_ordering，涉及 `__init__, create_qkvz_proj, create_ba_proj`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +27/-6 (33 lines); hunks: -412,12 +412,11 @@ def __init__(; -497,6 +496,28 @@ def create_qkvz_proj(; symbols: __init__, create_qkvz_proj, create_ba_proj, fix_query_key_value_ordering
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -412,12 +412,11 @@ def __init__(
-        # # in_proj_ba is defined as MergedColumnParallelLinear for
-        # compatibility with Qwen3_5.
-        self.in_proj_ba = MergedColumnParallelLinear(
-            input_size=self.hidden_size,
-            output_sizes=[self.num_v_heads] * 2,
-            bias=False,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +27/-6
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35777 - [Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next

- 链接: https://github.com/vllm-project/vllm/pull/35777
- 状态/时间: merged / 2026-03-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `dc6b57846686`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+509/-31，可读 patch 585 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +32/-31 (63 lines); hunks: -34,7 +34,7; -731,41 +731,40 @@ def _forward_core(; symbols: _forward_core，涉及 `_forward_core`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +32/-31 (63 lines); hunks: -34,7 +34,7; -731,41 +731,40 @@ def _forward_core(; symbols: _forward_core
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -34,7 +34,7 @@
-    fused_recurrent_gated_delta_rule,
+    fused_sigmoid_gating_delta_rule_update,
@@ -731,41 +731,40 @@ def _forward_core(
-        g, beta = fused_gdn_gating(self.A_log, a, b, self.dt_bias)
-        if spec_sequence_masks is not None:
-            if attn_metadata.num_prefills == 0 and attn_metadata.num_decodes == 0:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +32/-31
- 验证与风险: diff 自带测试面 `tests/kernels/test_fused_sigmoid_gating_delta_rule.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #34697 - [Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion

- 链接: https://github.com/vllm-project/vllm/pull/34697
- 状态/时间: merged / 2026-02-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `c0bd8b13da36`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+102/-192，可读 patch 477 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +27/-10 (37 lines); hunks: -44,6 +44,7; -406,19 +407,19 @@ def __init__(; symbols: __init__, create_qkvz_proj, fix_query_key_value_ordering，涉及 `__init__, create_qkvz_proj, fix_query_key_value_ordering`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +27/-10 (37 lines); hunks: -44,6 +44,7; -406,19 +407,19 @@ def __init__(; symbols: __init__, create_qkvz_proj, fix_query_key_value_ordering
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -44,6 +44,7 @@
+    MergedColumnParallelLinear,
@@ -406,19 +407,19 @@ def __init__(
-        self.projection_size_qkvz = self.key_dim * 2 + self.value_dim * 2
-        self.projection_size_ba = self.num_v_heads * 2
-        self.in_proj_qkvz = ColumnParallelLinear(
-            input_size=self.hidden_size,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +27/-10
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34489 - [Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/34489
- 状态/时间: merged / 2026-02-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `eea3024f43e0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+42/-6，可读 patch 91 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +6/-2 (8 lines); hunks: -341,7 +341,9 @@ def mamba_type(self) -> str:; -1372,7 +1374,9 @@ def get_mamba_state_dtype_from_config(; symbols: mamba_type, get_state_dtype, get_state_shape, get_mamba_state_dtype_from_config，涉及 `mamba_type, get_state_dtype, get_state_shape`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +6/-2 (8 lines); hunks: -341,7 +341,9 @@ def mamba_type(self) -> str:; -1372,7 +1374,9 @@ def get_mamba_state_dtype_from_config(; symbols: mamba_type, get_state_dtype, get_state_shape, get_mamba_state_dtype_from_config
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -341,7 +341,9 @@ def mamba_type(self) -> str:
-            self.model_config.dtype, self.cache_config.mamba_cache_dtype
+            self.model_config.dtype,
+            self.cache_config.mamba_cache_dtype,
+            self.cache_config.mamba_ssm_cache_dtype,
@@ -1372,7 +1374,9 @@ def get_mamba_state_dtype_from_config(
-            vllm_config.model_config.dtype, vllm_config.cache_config.mamba_cache_dtype
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +6/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31719 - [Misc] Support qwen3-next lora

- 链接: https://github.com/vllm-project/vllm/pull/31719
- 状态/时间: merged / 2026-01-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `96fcd3c267a0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-1，可读 patch 15 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Misc] Support qwen3-next lora」；模型线: Qwen3 Next；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Misc] Support qwen3-next lora」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +7/-1 (8 lines); hunks: -145,7 +145,13 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +7/-1 (8 lines); hunks: -145,7 +145,13 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -145,7 +145,13 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):
-        self.shared_expert_gate = torch.nn.Linear(config.hidden_size, 1, bias=False)
+        self.shared_expert_gate = ReplicatedLinear(
+            config.hidden_size,
+            1,
+            bias=False,
+            quant_config=None,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +7/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30433 - [Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\}

- 链接: https://github.com/vllm-project/vllm/pull/30433
- 状态/时间: merged / 2025-12-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `ace34e378320`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-0，可读 patch 21 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\}」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\}」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -1093,6 +1093,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -1109,6 +1111,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -1093,6 +1093,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -1109,6 +1111,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -1093,6 +1093,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                    if name not in params_dict:
+                        continue
@@ -1109,6 +1111,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                    if name not in params_dict:
+                        logger.warning_once(
+                            f"Parameter {name} not found in params_dict, skip loading"
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28960 - [Bugfix] Fix typo in Qwen3 Next model executor

- 链接: https://github.com/vllm-project/vllm/pull/28960
- 状态/时间: merged / 2025-11-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `73ff872db0d4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix typo in Qwen3 Next model executor」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix] Fix typo in Qwen3 Next model executor」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -1154,8 +1154,8 @@ def set_moe_parameters(self):; symbols: set_moe_parameters，涉及 `set_moe_parameters`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -1154,8 +1154,8 @@ def set_moe_parameters(self):; symbols: set_moe_parameters
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -1154,8 +1154,8 @@ def set_moe_parameters(self):
-            if example_moe is None:
-                raise RuntimeError("No Qwen3Next layer found in the model.layers.")
+        if example_moe is None:
+            raise RuntimeError("No Qwen3Next layer found in the model.layers.")
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28202 - [Bugfix] fix qwen3-next crash

- 链接: https://github.com/vllm-project/vllm/pull/28202
- 状态/时间: merged / 2025-11-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `f0359fffa434`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] fix qwen3-next crash」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix] fix qwen3-next crash」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -585,7 +585,7 @@ def _forward_core(; symbols: _forward_core，涉及 `_forward_core`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -585,7 +585,7 @@ def _forward_core(; symbols: _forward_core
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -585,7 +585,7 @@ def _forward_core(
-                    : attn_metadata.num_decodes
+                    : attn_metadata.num_actual_tokens
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28267 - [Misc] Add some comments in qwen3-next

- 链接: https://github.com/vllm-project/vllm/pull/28267
- 状态/时间: merged / 2025-11-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `7ae5a5fb1115`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-0，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Misc] Add some comments in qwen3-next」；模型线: Qwen3 Next；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Misc] Add some comments in qwen3-next」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +2/-0 (2 lines); hunks: -462,6 +462,8 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +2/-0 (2 lines); hunks: -462,6 +462,8 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -462,6 +462,8 @@ def forward(
+        # Note: we should not use torch.empty here like other attention backends,
+        # see discussions in https://github.com/vllm-project/vllm/pull/28182
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27578 - [perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next

- 链接: https://github.com/vllm-project/vllm/pull/27578
- 状态/时间: merged / 2025-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `8df98c2161e2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-5，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +12/-5 (17 lines); hunks: -159,6 +159,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; -181,11 +182,17 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Te...; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +12/-5 (17 lines); hunks: -159,6 +159,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; -181,11 +182,17 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Te...; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -159,6 +159,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):
+            gate=self.gate,
@@ -181,11 +182,17 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
-        # router_logits: (num_tokens, n_experts)
-        router_logits, _ = self.gate(hidden_states)
-        final_hidden_states = self.experts(
-            hidden_states=hidden_states, router_logits=router_logits
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +12/-5
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27030 - [Bugfix][Qwen] fixes the weights dtype in qwen3_next: it is actually a bfloat16

- 链接: https://github.com/vllm-project/vllm/pull/27030
- 状态/时间: merged / 2025-10-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `bde9e2272a28`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-1，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Qwen] fixes the weights dtype in qwen3_next: it is actually a bfloat16」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix][Qwen] fixes the weights dtype in qwen3_next: it is actually a bfloat16」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +0/-1 (1 lines); hunks: -325,7 +325,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +0/-1 (1 lines); hunks: -325,7 +325,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -325,7 +325,6 @@ def __init__(
-                dtype=torch.float32,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +0/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26437 - [PERF] Qwen3-next MTP speedup (change bool mask indexing to index_select / index_copy to reduce d2h)

- 链接: https://github.com/vllm-project/vllm/pull/26437
- 状态/时间: merged / 2025-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `785d8b6410c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+56/-36，可读 patch 203 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[PERF] Qwen3-next MTP speedup (change bool mask indexing to index_select / index_copy to reduce d2h)」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[PERF] Qwen3-next MTP speedup (change bool mask indexing to index_select / index_copy to reduce d2h)」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +12/-12 (24 lines); hunks: -423,7 +423,7 @@ def rearrange_mixed_qkv(self, mixed_qkv):; -455,16 +455,15 @@ def _forward(; symbols: rearrange_mixed_qkv, forward, _forward，涉及 `rearrange_mixed_qkv, forward, _forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +12/-12 (24 lines); hunks: -423,7 +423,7 @@ def rearrange_mixed_qkv(self, mixed_qkv):; -455,16 +455,15 @@ def _forward(; symbols: rearrange_mixed_qkv, forward, _forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -423,7 +423,7 @@ def rearrange_mixed_qkv(self, mixed_qkv):
-        return query, key, value
+        return query.contiguous(), key.contiguous(), value.contiguous()
@@ -455,16 +455,15 @@ def _forward(
-        spec_token_masks = attn_metadata.spec_token_masks
+        spec_token_indx = attn_metadata.spec_token_indx
+        non_spec_token_indx = attn_metadata.non_spec_token_indx
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +12/-12
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fla/ops/utils.py`, `vllm/model_executor/models/qwen3_next.py`, `vllm/v1/attention/backends/gdn_attn.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25268 - [BUGFIX] GPTQ quantization compatibility for Qwen3 Next MOE models (AutoGPTQ and AutoRound-GPTQ)

- 链接: https://github.com/vllm-project/vllm/pull/25268
- 状态/时间: merged / 2025-09-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `36429096171f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-3，可读 patch 15 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BUGFIX] GPTQ quantization compatibility for Qwen3 Next MOE models (AutoGPTQ and AutoRound-GPTQ)」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[BUGFIX] GPTQ quantization compatibility for Qwen3 Next MOE models (AutoGPTQ and AutoRound-GPTQ)」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +5/-3 (8 lines); hunks: -148,9 +148,11 @@ def __init__(; symbols: __init__, _maybe_ignore_quant_config，涉及 `__init__, _maybe_ignore_quant_config`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +5/-3 (8 lines); hunks: -148,9 +148,11 @@ def __init__(; symbols: __init__, _maybe_ignore_quant_config
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -148,9 +148,11 @@ def __init__(
-        # seems to avoid gate quantization.
-        # See: https://huggingface.co/Qwen/Qwen3-30B-A3B-GPTQ-Int4
-        if isinstance(quant_config, (GPTQConfig, GPTQMarlinConfig)):
+        # seems to avoid gate quantization while AutoRound does.
+        if isinstance(
+                quant_config,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +5/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25243 - [Qwen] Remove cuda hard-code in qwen3 next

- 链接: https://github.com/vllm-project/vllm/pull/25243
- 状态/时间: merged / 2025-09-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `838d7116ba59`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen] Remove cuda hard-code in qwen3 next」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Qwen] Remove cuda hard-code in qwen3 next」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -306,7 +306,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -306,7 +306,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -306,7 +306,7 @@ def __init__(
-            device=torch.cuda.current_device(),
+            device=current_platform.current_device(),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25079 - [Qwen] Add fp8 checkpoint support for qwen3-next.

- 链接: https://github.com/vllm-project/vllm/pull/25079
- 状态/时间: merged / 2025-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`；关联提交 `ef7eefe17a7d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+22/-21，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen] Add fp8 checkpoint support for qwen3-next.」；模型线: Qwen3 Next；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`；技术摘要: 覆盖「[Qwen] Add fp8 checkpoint support for qwen3-next.」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +17/-18 (35 lines); hunks: -30,7 +30,6; -254,12 +253,20 @@ def __init__(; symbols: __init__, _forward, load_weights, Qwen3NextForCausalLM，涉及 `__init__, _forward, load_weights`；`vllm/model_executor/models/qwen3_next_mtp.py` modified +5/-3 (8 lines); hunks: -63,7 +63,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; -72,7 +74,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +17/-18 (35 lines); hunks: -30,7 +30,6; -254,12 +253,20 @@ def __init__(; symbols: __init__, _forward, load_weights, Qwen3NextForCausalLM
  - `vllm/model_executor/models/qwen3_next_mtp.py` modified +5/-3 (8 lines); hunks: -63,7 +63,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; -72,7 +74,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -30,7 +30,6 @@
-                                               MergedColumnParallelLinear,
@@ -254,12 +253,20 @@ def __init__(
-        self.in_proj = MergedColumnParallelLinear(
+        self.in_proj_qkvz = ColumnParallelLinear(
-            output_sizes=[self.projection_size_qkvz, self.projection_size_ba],
+            output_size=self.projection_size_qkvz,
diff -- vllm/model_executor/models/qwen3_next_mtp.py
@@ -63,7 +63,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                                       return_bias=False)
+                                       return_bias=False,
+                                       quant_config=quant_config,
+                                       prefix=f'{prefix}.fc')
@@ -72,7 +74,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                prefix=f'{prefix}.layers.{self.mtp_start_layer_idx + idx}',
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +17/-18; `vllm/model_executor/models/qwen3_next_mtp.py` modified +5/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24960 - [Bugfix][Qwen3-Next] add prefixes to shared_expert in qwen3-next and mlp in qwen2moe to successfully load ignored params in quantized models

- 链接: https://github.com/vllm-project/vllm/pull/24960
- 状态/时间: merged / 2025-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `027d37df389b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+26/-23，可读 patch 101 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Qwen3-Next] add prefixes to shared_expert in qwen3-next and mlp in qwen2moe to successfully load ignored params in quantized models」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix][Qwen3-Next] add prefixes to shared_expert in qwen3-next and mlp in qwen2moe to successfully load ignored params in quantized models」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -138,6 +138,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -138,6 +138,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -138,6 +138,7 @@ def __init__(
+                prefix=f"{prefix}.shared_expert",
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen2_moe.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24957 - [Bugfix][Qwen3-Next] fixes the varlen issue in qwen3-next's MTP implementation.

- 链接: https://github.com/vllm-project/vllm/pull/24957
- 状态/时间: merged / 2025-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `dd6a910aac65`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+139/-34，可读 patch 385 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Qwen3-Next] fixes the varlen issue in qwen3-next's MTP implementation.」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[Bugfix][Qwen3-Next] fixes the varlen issue in qwen3-next's MTP implementation.」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +3/-7 (10 lines); hunks: -417,9 +417,7 @@ def _forward(; -458,9 +456,6 @@ def _forward(; symbols: _forward，涉及 `_forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +3/-7 (10 lines); hunks: -417,9 +417,7 @@ def _forward(; -458,9 +456,6 @@ def _forward(; symbols: _forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -417,9 +417,7 @@ def _forward(
-        num_actual_tokens = (attn_metadata.num_prefill_tokens +
-                             attn_metadata.num_decode_tokens +
-                             attn_metadata.num_spec_decode_tokens)
+        num_actual_tokens = attn_metadata.num_actual_tokens
@@ -458,9 +456,6 @@ def _forward(
-            mixed_qkv_spec = mixed_qkv_spec.view(
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +3/-7
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/ops/causal_conv1d.py`, `vllm/model_executor/models/qwen3_next.py`, `vllm/v1/attention/backends/gdn_attn.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24709 - [BugFix] Fix Qwen3-Next PP

- 链接: https://github.com/vllm-project/vllm/pull/24709
- 状态/时间: merged / 2025-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`；关联提交 `f592b3174b39`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-3，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix] Fix Qwen3-Next PP」；模型线: Qwen3 Next；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_next.py`；技术摘要: 覆盖「[BugFix] Fix Qwen3-Next PP」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` modified +7/-3 (10 lines); hunks: -2,6 +2,7; -917,8 +918,11 @@ def get_layer(prefix: str):; symbols: get_layer, get_input_embeddings, forward，涉及 `get_layer, get_input_embeddings, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` modified +7/-3 (10 lines); hunks: -2,6 +2,7; -917,8 +918,11 @@ def get_layer(prefix: str):; symbols: get_layer, get_input_embeddings, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -2,6 +2,7 @@
+from itertools import islice
@@ -917,8 +918,11 @@ def get_layer(prefix: str):
-        self.norm = Qwen3NextRMSNorm(config.hidden_size,
-                                     eps=config.rms_norm_eps)
+        if get_pp_group().is_last_rank:
+            self.norm = Qwen3NextRMSNorm(config.hidden_size,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +7/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24526 - Add the support for the qwen3 next model (a hybrid attention model).

- 链接: https://github.com/vllm-project/vllm/pull/24526
- 状态/时间: merged / 2025-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`；关联提交 `e93f4cc9e374`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 29 个文件，+2476/-61，可读 patch 3045 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add the support for the qwen3 next model (a hybrid attention model).」；模型线: Qwen3 Next；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`, `vllm/transformers_utils/configs/qwen3_next.py`；技术摘要: 覆盖「Add the support for the qwen3 next model (a hybrid attention model).」；主要实现面是 `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`, `vllm/transformers_utils/configs/qwen3_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_next.py` added +1294/-0 (1294 lines); hunks: -0,0 +1,1294; symbols: Qwen3NextSparseMoeBlock, __init__, _maybe_ignore_quant_config, forward，涉及 `Qwen3NextSparseMoeBlock, __init__, _maybe_ignore_quant_config`；`vllm/model_executor/models/qwen3_next_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: Qwen3NextMultiTokenPredictor, __init__, get_input_embeddings, forward，涉及 `Qwen3NextMultiTokenPredictor, __init__, get_input_embeddings`；`vllm/transformers_utils/configs/qwen3_next.py` added +275/-0 (275 lines); hunks: -0,0 +1,275; symbols: Qwen3NextConfig, to, __init__，涉及 `Qwen3NextConfig, to, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_next.py` added +1294/-0 (1294 lines); hunks: -0,0 +1,1294; symbols: Qwen3NextSparseMoeBlock, __init__, _maybe_ignore_quant_config, forward
  - `vllm/model_executor/models/qwen3_next_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: Qwen3NextMultiTokenPredictor, __init__, get_input_embeddings, forward
  - `vllm/transformers_utils/configs/qwen3_next.py` added +275/-0 (275 lines); hunks: -0,0 +1,275; symbols: Qwen3NextConfig, to, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -0,0 +1,1294 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only Qwen3Next model."""
+from collections.abc import Iterable
+from typing import Optional
+import torch
diff -- vllm/model_executor/models/qwen3_next_mtp.py
@@ -0,0 +1,285 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only Qwen3Next MTP model."""
+from collections.abc import Iterable
+from typing import Optional
+import torch
diff -- vllm/transformers_utils/configs/qwen3_next.py
@@ -0,0 +1,275 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_next.py` added +1294/-0; `vllm/model_executor/models/qwen3_next_mtp.py` added +285/-0; `vllm/transformers_utils/configs/qwen3_next.py` added +275/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
