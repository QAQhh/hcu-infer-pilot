# vllm Qwen3 Next Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `vllm/model_executor/models/qwen3_next.py` | [#24526](https://github.com/vllm-project/vllm/pull/24526), [#24709](https://github.com/vllm-project/vllm/pull/24709), [#24957](https://github.com/vllm-project/vllm/pull/24957), [#24960](https://github.com/vllm-project/vllm/pull/24960), [#25079](https://github.com/vllm-project/vllm/pull/25079), [#25243](https://github.com/vllm-project/vllm/pull/25243), [#25268](https://github.com/vllm-project/vllm/pull/25268), [#26437](https://github.com/vllm-project/vllm/pull/26437), [#27030](https://github.com/vllm-project/vllm/pull/27030), [#27578](https://github.com/vllm-project/vllm/pull/27578), [#28202](https://github.com/vllm-project/vllm/pull/28202), [#28267](https://github.com/vllm-project/vllm/pull/28267), ... (23 total) |
| `vllm/model_executor/models/qwen3_next_mtp.py` | [#24526](https://github.com/vllm-project/vllm/pull/24526), [#25079](https://github.com/vllm-project/vllm/pull/25079), [#39280](https://github.com/vllm-project/vllm/pull/39280), [#62111](https://github.com/vllm-project/vllm/pull/62111) |

## PR Coverage Summary

- Git-traced PRs: 24
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 24

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
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

## Per-PR Diff Audit Cards

### PR #62111 - [Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next

- Link: https://github.com/vllm-project/vllm/pull/62111
- Status/date: merged / 2026-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next_mtp.py`; associated commits `dd5f5eebd7a0`
- Diff scope read: GitHub Pull Request files API returned 9 files, +222/-16, 388 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next_mtp.py`; technical summary: Covers "[Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next"; the main implementation surface is `vllm/model_executor/models/qwen3_next_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4 (23 lines); hunks: -41,7 +41,17; -171,7 +181,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights, Qwen3NextMTP, touching `should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4 (23 lines); hunks: -41,7 +41,17; -171,7 +181,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights, Qwen3NextMTP
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4
- Risk and verification: The diff ships test coverage in `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/test_qwen3_5_mtp_config.py`, `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39280 - [ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next

- Link: https://github.com/vllm-project/vllm/pull/39280
- Status/date: merged / 2026-05-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`; associated commits `2c6b59b80771`
- Diff scope read: GitHub Pull Request files API returned 8 files, +359/-10, 573 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`; technical summary: Covers "[ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +26/-4 (30 lines); hunks: -8,6 +8,7; -135,7 +136,12 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__, forward, touching `__init__, forward`; `vllm/model_executor/models/qwen3_next_mtp.py` modified +14/-1 (15 lines); hunks: -7,6 +7,7; -147,20 +148,32 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +26/-4 (30 lines); hunks: -8,6 +8,7; -135,7 +136,12 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__, forward
  - `vllm/model_executor/models/qwen3_next_mtp.py` modified +14/-1 (15 lines); hunks: -7,6 +7,7; -147,20 +148,32 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +26/-4; `vllm/model_executor/models/qwen3_next_mtp.py` modified +14/-1
- Risk and verification: Runtime changes concentrate in `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #39181 - [Bugfix]Fix EP precision for Qwen3.5, Qwen3-Next

- Link: https://github.com/vllm-project/vllm/pull/39181
- Status/date: merged / 2026-04-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `f3c7941ec8d3`
- Diff scope read: GitHub Pull Request files API returned 2 files, +4/-0, 32 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix]Fix EP precision for Qwen3.5, Qwen3-Next"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix]Fix EP precision for Qwen3.5, Qwen3-Next"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -140,6 +140,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -140,6 +140,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -140,6 +140,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):
+                is_sequence_parallel=self.is_sequence_parallel,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen2_moe.py`, `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37427 - [Bugfix] Fix ROCm crash in qwen3_next multi-stream events (#36795)

- Link: https://github.com/vllm-project/vllm/pull/37427
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `a913b612d8a8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix ROCm crash in qwen3_next multi-stream events (#36795)"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix] Fix ROCm crash in qwen3_next multi-stream events (#36795)"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -426,7 +426,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -426,7 +426,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -426,7 +426,7 @@ def __init__(
-            if current_platform.is_cuda()
+            if current_platform.is_cuda_alike()
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36795 - [Perf] Enable dual stream execution of input projection for Qwen3

- Link: https://github.com/vllm-project/vllm/pull/36795
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `a913b612d8a8`, `f1740006e47d`
- Diff scope read: GitHub Pull Request files API returned 3 files, +115/-5, 174 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Enable dual stream execution of input projection for Qwen3"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Perf] Enable dual stream execution of input projection for Qwen3"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +61/-3 (64 lines); hunks: -82,7 +82,11; -419,6 +423,12 @@ def __init__(; symbols: __init__, forward, _warmup_prefill_kernels, _forward_in_proj, touching `__init__, forward, _warmup_prefill_kernels`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +61/-3 (64 lines); hunks: -82,7 +82,11; -419,6 +423,12 @@ def __init__(; symbols: __init__, forward, _warmup_prefill_kernels, _forward_in_proj
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +61/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`, `vllm/utils/multi_stream_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36242 - [Bugfix] Fix Qwen3-Next in_proj_ba weight sharding with TP > 1

- Link: https://github.com/vllm-project/vllm/pull/36242
- Status/date: merged / 2026-03-10
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `4e95ec111cd1`
- Diff scope read: GitHub Pull Request files API returned 2 files, +45/-6, 72 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Qwen3-Next in_proj_ba weight sharding with TP > 1"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix] Fix Qwen3-Next in_proj_ba weight sharding with TP > 1"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +27/-6 (33 lines); hunks: -412,12 +412,11 @@ def __init__(; -497,6 +496,28 @@ def create_qkvz_proj(; symbols: __init__, create_qkvz_proj, create_ba_proj, fix_query_key_value_ordering, touching `__init__, create_qkvz_proj, create_ba_proj`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +27/-6 (33 lines); hunks: -412,12 +412,11 @@ def __init__(; -497,6 +496,28 @@ def create_qkvz_proj(; symbols: __init__, create_qkvz_proj, create_ba_proj, fix_query_key_value_ordering
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +27/-6
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #35777 - [Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next

- Link: https://github.com/vllm-project/vllm/pull/35777
- Status/date: merged / 2026-03-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `dc6b57846686`
- Diff scope read: GitHub Pull Request files API returned 4 files, +509/-31, 585 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +32/-31 (63 lines); hunks: -34,7 +34,7; -731,41 +731,40 @@ def _forward_core(; symbols: _forward_core, touching `_forward_core`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +32/-31 (63 lines); hunks: -34,7 +34,7; -731,41 +731,40 @@ def _forward_core(; symbols: _forward_core
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +32/-31
- Risk and verification: The diff ships test coverage in `tests/kernels/test_fused_sigmoid_gating_delta_rule.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #34697 - [Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion

- Link: https://github.com/vllm-project/vllm/pull/34697
- Status/date: merged / 2026-02-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `c0bd8b13da36`
- Diff scope read: GitHub Pull Request files API returned 3 files, +102/-192, 477 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +27/-10 (37 lines); hunks: -44,6 +44,7; -406,19 +407,19 @@ def __init__(; symbols: __init__, create_qkvz_proj, fix_query_key_value_ordering, touching `__init__, create_qkvz_proj, fix_query_key_value_ordering`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +27/-10 (37 lines); hunks: -44,6 +44,7; -406,19 +407,19 @@ def __init__(; symbols: __init__, create_qkvz_proj, fix_query_key_value_ordering
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +27/-10
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34489 - [Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5

- Link: https://github.com/vllm-project/vllm/pull/34489
- Status/date: merged / 2026-02-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `eea3024f43e0`
- Diff scope read: GitHub Pull Request files API returned 4 files, +42/-6, 91 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +6/-2 (8 lines); hunks: -341,7 +341,9 @@ def mamba_type(self) -> str:; -1372,7 +1374,9 @@ def get_mamba_state_dtype_from_config(; symbols: mamba_type, get_state_dtype, get_state_shape, get_mamba_state_dtype_from_config, touching `mamba_type, get_state_dtype, get_state_shape`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +6/-2 (8 lines); hunks: -341,7 +341,9 @@ def mamba_type(self) -> str:; -1372,7 +1374,9 @@ def get_mamba_state_dtype_from_config(; symbols: mamba_type, get_state_dtype, get_state_shape, get_mamba_state_dtype_from_config
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +6/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31719 - [Misc] Support qwen3-next lora

- Link: https://github.com/vllm-project/vllm/pull/31719
- Status/date: merged / 2026-01-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `96fcd3c267a0`
- Diff scope read: GitHub Pull Request files API returned 1 files, +7/-1, 15 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Misc] Support qwen3-next lora"; model line: Qwen3 Next; category: model support/runtime entry; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Misc] Support qwen3-next lora"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +7/-1 (8 lines); hunks: -145,7 +145,13 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +7/-1 (8 lines); hunks: -145,7 +145,13 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +7/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #30433 - [Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\}

- Link: https://github.com/vllm-project/vllm/pull/30433
- Status/date: merged / 2025-12-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `ace34e378320`
- Diff scope read: GitHub Pull Request files API returned 1 files, +7/-0, 21 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\}"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\}"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -1093,6 +1093,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -1109,6 +1111,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +7/-0 (7 lines); hunks: -1093,6 +1093,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -1109,6 +1111,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +7/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28960 - [Bugfix] Fix typo in Qwen3 Next model executor

- Link: https://github.com/vllm-project/vllm/pull/28960
- Status/date: merged / 2025-11-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `73ff872db0d4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 11 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix typo in Qwen3 Next model executor"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix] Fix typo in Qwen3 Next model executor"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -1154,8 +1154,8 @@ def set_moe_parameters(self):; symbols: set_moe_parameters, touching `set_moe_parameters`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +2/-2 (4 lines); hunks: -1154,8 +1154,8 @@ def set_moe_parameters(self):; symbols: set_moe_parameters
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -1154,8 +1154,8 @@ def set_moe_parameters(self):
-            if example_moe is None:
-                raise RuntimeError("No Qwen3Next layer found in the model.layers.")
+        if example_moe is None:
+            raise RuntimeError("No Qwen3Next layer found in the model.layers.")
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28202 - [Bugfix] fix qwen3-next crash

- Link: https://github.com/vllm-project/vllm/pull/28202
- Status/date: merged / 2025-11-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `f0359fffa434`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] fix qwen3-next crash"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix] fix qwen3-next crash"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -585,7 +585,7 @@ def _forward_core(; symbols: _forward_core, touching `_forward_core`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -585,7 +585,7 @@ def _forward_core(; symbols: _forward_core
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -585,7 +585,7 @@ def _forward_core(
-                    : attn_metadata.num_decodes
+                    : attn_metadata.num_actual_tokens
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28267 - [Misc] Add some comments in qwen3-next

- Link: https://github.com/vllm-project/vllm/pull/28267
- Status/date: merged / 2025-11-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `7ae5a5fb1115`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-0, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Misc] Add some comments in qwen3-next"; model line: Qwen3 Next; category: model support/runtime entry; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Misc] Add some comments in qwen3-next"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +2/-0 (2 lines); hunks: -462,6 +462,8 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +2/-0 (2 lines); hunks: -462,6 +462,8 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -462,6 +462,8 @@ def forward(
+        # Note: we should not use torch.empty here like other attention backends,
+        # see discussions in https://github.com/vllm-project/vllm/pull/28182
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27578 - [perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next

- Link: https://github.com/vllm-project/vllm/pull/27578
- Status/date: merged / 2025-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `8df98c2161e2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-5, 31 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +12/-5 (17 lines); hunks: -159,6 +159,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; -181,11 +182,17 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Te...; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +12/-5 (17 lines); hunks: -159,6 +159,7 @@ def __init__(self, vllm_config: VllmConfig, prefix: str = ""):; -181,11 +182,17 @@ def forward(self, hidden_states: torch.Tensor) -> torch.Te...; symbols: __init__, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +12/-5
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27030 - [Bugfix][Qwen] fixes the weights dtype in qwen3_next: it is actually a bfloat16

- Link: https://github.com/vllm-project/vllm/pull/27030
- Status/date: merged / 2025-10-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `bde9e2272a28`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-1, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Qwen] fixes the weights dtype in qwen3_next: it is actually a bfloat16"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix][Qwen] fixes the weights dtype in qwen3_next: it is actually a bfloat16"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +0/-1 (1 lines); hunks: -325,7 +325,6 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +0/-1 (1 lines); hunks: -325,7 +325,6 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -325,7 +325,6 @@ def __init__(
-                dtype=torch.float32,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +0/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26437 - [PERF] Qwen3-next MTP speedup (change bool mask indexing to index_select / index_copy to reduce d2h)

- Link: https://github.com/vllm-project/vllm/pull/26437
- Status/date: merged / 2025-10-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `785d8b6410c3`
- Diff scope read: GitHub Pull Request files API returned 3 files, +56/-36, 203 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[PERF] Qwen3-next MTP speedup (change bool mask indexing to index_select / index_copy to reduce d2h)"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[PERF] Qwen3-next MTP speedup (change bool mask indexing to index_select / index_copy to reduce d2h)"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +12/-12 (24 lines); hunks: -423,7 +423,7 @@ def rearrange_mixed_qkv(self, mixed_qkv):; -455,16 +455,15 @@ def _forward(; symbols: rearrange_mixed_qkv, forward, _forward, touching `rearrange_mixed_qkv, forward, _forward`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +12/-12 (24 lines); hunks: -423,7 +423,7 @@ def rearrange_mixed_qkv(self, mixed_qkv):; -455,16 +455,15 @@ def _forward(; symbols: rearrange_mixed_qkv, forward, _forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +12/-12
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/fla/ops/utils.py`, `vllm/model_executor/models/qwen3_next.py`, `vllm/v1/attention/backends/gdn_attn.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25268 - [BUGFIX] GPTQ quantization compatibility for Qwen3 Next MOE models (AutoGPTQ and AutoRound-GPTQ)

- Link: https://github.com/vllm-project/vllm/pull/25268
- Status/date: merged / 2025-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `36429096171f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-3, 15 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BUGFIX] GPTQ quantization compatibility for Qwen3 Next MOE models (AutoGPTQ and AutoRound-GPTQ)"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[BUGFIX] GPTQ quantization compatibility for Qwen3 Next MOE models (AutoGPTQ and AutoRound-GPTQ)"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +5/-3 (8 lines); hunks: -148,9 +148,11 @@ def __init__(; symbols: __init__, _maybe_ignore_quant_config, touching `__init__, _maybe_ignore_quant_config`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +5/-3 (8 lines); hunks: -148,9 +148,11 @@ def __init__(; symbols: __init__, _maybe_ignore_quant_config
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +5/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25243 - [Qwen] Remove cuda hard-code in qwen3 next

- Link: https://github.com/vllm-project/vllm/pull/25243
- Status/date: merged / 2025-09-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `838d7116ba59`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Qwen] Remove cuda hard-code in qwen3 next"; model line: Qwen3 Next; category: performance/backend optimization; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Qwen] Remove cuda hard-code in qwen3 next"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -306,7 +306,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-1 (2 lines); hunks: -306,7 +306,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -306,7 +306,7 @@ def __init__(
-            device=torch.cuda.current_device(),
+            device=current_platform.current_device(),
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25079 - [Qwen] Add fp8 checkpoint support for qwen3-next.

- Link: https://github.com/vllm-project/vllm/pull/25079
- Status/date: merged / 2025-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`; associated commits `ef7eefe17a7d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +22/-21, 104 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Qwen] Add fp8 checkpoint support for qwen3-next."; model line: Qwen3 Next; category: performance/backend optimization; main diff: `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`; technical summary: Covers "[Qwen] Add fp8 checkpoint support for qwen3-next."; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +17/-18 (35 lines); hunks: -30,7 +30,6; -254,12 +253,20 @@ def __init__(; symbols: __init__, _forward, load_weights, Qwen3NextForCausalLM, touching `__init__, _forward, load_weights`; `vllm/model_executor/models/qwen3_next_mtp.py` modified +5/-3 (8 lines); hunks: -63,7 +63,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; -72,7 +74,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +17/-18 (35 lines); hunks: -30,7 +30,6; -254,12 +253,20 @@ def __init__(; symbols: __init__, _forward, load_weights, Qwen3NextForCausalLM
  - `vllm/model_executor/models/qwen3_next_mtp.py` modified +5/-3 (8 lines); hunks: -63,7 +63,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; -72,7 +74,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +17/-18; `vllm/model_executor/models/qwen3_next_mtp.py` modified +5/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24960 - [Bugfix][Qwen3-Next] add prefixes to shared_expert in qwen3-next and mlp in qwen2moe to successfully load ignored params in quantized models

- Link: https://github.com/vllm-project/vllm/pull/24960
- Status/date: merged / 2025-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `027d37df389b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +26/-23, 101 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Qwen3-Next] add prefixes to shared_expert in qwen3-next and mlp in qwen2moe to successfully load ignored params in quantized models"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix][Qwen3-Next] add prefixes to shared_expert in qwen3-next and mlp in qwen2moe to successfully load ignored params in quantized models"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -138,6 +138,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +1/-0 (1 lines); hunks: -138,6 +138,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/qwen3_next.py
@@ -138,6 +138,7 @@ def __init__(
+                prefix=f"{prefix}.shared_expert",
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen2_moe.py`, `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24957 - [Bugfix][Qwen3-Next] fixes the varlen issue in qwen3-next's MTP implementation.

- Link: https://github.com/vllm-project/vllm/pull/24957
- Status/date: merged / 2025-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `dd6a910aac65`
- Diff scope read: GitHub Pull Request files API returned 3 files, +139/-34, 385 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Qwen3-Next] fixes the varlen issue in qwen3-next's MTP implementation."; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[Bugfix][Qwen3-Next] fixes the varlen issue in qwen3-next's MTP implementation."; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +3/-7 (10 lines); hunks: -417,9 +417,7 @@ def _forward(; -458,9 +456,6 @@ def _forward(; symbols: _forward, touching `_forward`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +3/-7 (10 lines); hunks: -417,9 +417,7 @@ def _forward(; -458,9 +456,6 @@ def _forward(; symbols: _forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +3/-7
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/mamba/ops/causal_conv1d.py`, `vllm/model_executor/models/qwen3_next.py`, `vllm/v1/attention/backends/gdn_attn.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24709 - [BugFix] Fix Qwen3-Next PP

- Link: https://github.com/vllm-project/vllm/pull/24709
- Status/date: merged / 2025-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`; associated commits `f592b3174b39`
- Diff scope read: GitHub Pull Request files API returned 1 files, +7/-3, 31 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix] Fix Qwen3-Next PP"; model line: Qwen3 Next; category: bug fix; main diff: `vllm/model_executor/models/qwen3_next.py`; technical summary: Covers "[BugFix] Fix Qwen3-Next PP"; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` modified +7/-3 (10 lines); hunks: -2,6 +2,7; -917,8 +918,11 @@ def get_layer(prefix: str):; symbols: get_layer, get_input_embeddings, forward, touching `get_layer, get_input_embeddings, forward`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` modified +7/-3 (10 lines); hunks: -2,6 +2,7; -917,8 +918,11 @@ def get_layer(prefix: str):; symbols: get_layer, get_input_embeddings, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` modified +7/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/qwen3_next.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24526 - Add the support for the qwen3 next model (a hybrid attention model).

- Link: https://github.com/vllm-project/vllm/pull/24526
- Status/date: merged / 2025-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`; associated commits `e93f4cc9e374`
- Diff scope read: GitHub Pull Request files API returned 29 files, +2476/-61, 3045 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add the support for the qwen3 next model (a hybrid attention model)."; model line: Qwen3 Next; category: model support/runtime entry; main diff: `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`, `vllm/transformers_utils/configs/qwen3_next.py`; technical summary: Covers "Add the support for the qwen3 next model (a hybrid attention model)."; the main implementation surface is `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`, `vllm/transformers_utils/configs/qwen3_next.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/qwen3_next.py` added +1294/-0 (1294 lines); hunks: -0,0 +1,1294; symbols: Qwen3NextSparseMoeBlock, __init__, _maybe_ignore_quant_config, forward, touching `Qwen3NextSparseMoeBlock, __init__, _maybe_ignore_quant_config`; `vllm/model_executor/models/qwen3_next_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: Qwen3NextMultiTokenPredictor, __init__, get_input_embeddings, forward, touching `Qwen3NextMultiTokenPredictor, __init__, get_input_embeddings`; `vllm/transformers_utils/configs/qwen3_next.py` added +275/-0 (275 lines); hunks: -0,0 +1,275; symbols: Qwen3NextConfig, to, __init__, touching `Qwen3NextConfig, to, __init__`.
- Code diff details:
  - `vllm/model_executor/models/qwen3_next.py` added +1294/-0 (1294 lines); hunks: -0,0 +1,1294; symbols: Qwen3NextSparseMoeBlock, __init__, _maybe_ignore_quant_config, forward
  - `vllm/model_executor/models/qwen3_next_mtp.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: Qwen3NextMultiTokenPredictor, __init__, get_input_embeddings, forward
  - `vllm/transformers_utils/configs/qwen3_next.py` added +275/-0 (275 lines); hunks: -0,0 +1,275; symbols: Qwen3NextConfig, to, __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/qwen3_next.py` added +1294/-0; `vllm/model_executor/models/qwen3_next_mtp.py` added +285/-0; `vllm/transformers_utils/configs/qwen3_next.py` added +275/-0
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
