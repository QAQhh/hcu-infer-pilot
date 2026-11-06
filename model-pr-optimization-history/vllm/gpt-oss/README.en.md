# vllm GPT-OSS Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/evals/gpt_oss/README.md` | no direct PR-number commit |
| `tests/evals/gpt_oss/__init__.py` | [#24920](https://github.com/vllm-project/vllm/pull/24920) |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-baseline.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-bf16-cutlass.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-bf16-trtllm.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-humming-mxfp4-mxfp8.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-marlin.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` | [#36179](https://github.com/vllm-project/vllm/pull/36179) |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-quark-mxfp4-bf16-aiter.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-quark-mxfp4-bf16-triton.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-quark-mxfp4-fp8-triton.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-sm120.yaml` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` | [#48703](https://github.com/vllm-project/vllm/pull/48703) |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` | [#48703](https://github.com/vllm-project/vllm/pull/48703) |
| `tests/evals/gpt_oss/configs/models-b200.txt` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/models-gfx942.txt` | [#36179](https://github.com/vllm-project/vllm/pull/36179) |
| `tests/evals/gpt_oss/configs/models-gfx950.txt` | [#36179](https://github.com/vllm-project/vllm/pull/36179), [#38292](https://github.com/vllm-project/vllm/pull/38292) |
| `tests/evals/gpt_oss/configs/models-h100.txt` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/models-spark.txt` | no direct PR-number commit |
| `tests/evals/gpt_oss/configs/models-xpu.txt` | [#48703](https://github.com/vllm-project/vllm/pull/48703) |
| `tests/evals/gpt_oss/conftest.py` | [#24920](https://github.com/vllm-project/vllm/pull/24920) |
| `tests/evals/gpt_oss/run_gpqa_eval.py` | no direct PR-number commit |
| `tests/evals/gpt_oss/test_gpqa_correctness.py` | [#24920](https://github.com/vllm-project/vllm/pull/24920), [#26030](https://github.com/vllm-project/vllm/pull/26030) |
| `tests/evals/gsm8k/configs/humming/gpt-oss-20b-humming-act-fp8.yaml` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/humming/gpt-oss-20b-humming.yaml` | no direct PR-number commit |
| `tests/kernels/moe/test_gpt_oss_triton_kernels.py` | [#22421](https://github.com/vllm-project/vllm/pull/22421), [#29008](https://github.com/vllm-project/vllm/pull/29008), [#37683](https://github.com/vllm-project/vllm/pull/37683), [#39007](https://github.com/vllm-project/vllm/pull/39007), [#45457](https://github.com/vllm-project/vllm/pull/45457), [#55934](https://github.com/vllm-project/vllm/pull/55934) |
| `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` | [#52209](https://github.com/vllm-project/vllm/pull/52209) |
| `tests/models/quantization/test_gpt_oss.py` | [#29008](https://github.com/vllm-project/vllm/pull/29008), [#35806](https://github.com/vllm-project/vllm/pull/35806), [#35887](https://github.com/vllm-project/vllm/pull/35887), [#36174](https://github.com/vllm-project/vllm/pull/36174), [#43571](https://github.com/vllm-project/vllm/pull/43571) |
| `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` | [#39007](https://github.com/vllm-project/vllm/pull/39007), [#43135](https://github.com/vllm-project/vllm/pull/43135), [#45457](https://github.com/vllm-project/vllm/pull/45457), [#55934](https://github.com/vllm-project/vllm/pull/55934) |
| `vllm/model_executor/models/gpt_oss.py` | [#22327](https://github.com/vllm-project/vllm/pull/22327), [#22401](https://github.com/vllm-project/vllm/pull/22401), [#22508](https://github.com/vllm-project/vllm/pull/22508), [#22538](https://github.com/vllm-project/vllm/pull/22538), [#22678](https://github.com/vllm-project/vllm/pull/22678), [#22948](https://github.com/vllm-project/vllm/pull/22948), [#22951](https://github.com/vllm-project/vllm/pull/22951), [#23613](https://github.com/vllm-project/vllm/pull/23613), [#23680](https://github.com/vllm-project/vllm/pull/23680), [#23815](https://github.com/vllm-project/vllm/pull/23815), [#24032](https://github.com/vllm-project/vllm/pull/24032), [#25246](https://github.com/vllm-project/vllm/pull/25246), ... (30 total) |

## PR Coverage Summary

- Git-traced PRs: 45
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 45

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-10-14 | [#61257](https://github.com/vllm-project/vllm/pull/61257) | merged | [Model Runner V2] Enable batch-sharded sampling for GPT-OSS | `vllm/model_executor/models/gpt_oss.py` |
| 2026-09-17 | [#55934](https://github.com/vllm-project/vllm/pull/55934) | merged | [ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4) | `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py` |
| 2026-08-29 | [#45457](https://github.com/vllm-project/vllm/pull/45457) | merged | [Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward | `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py` |
| 2026-08-23 | [#52209](https://github.com/vllm-project/vllm/pull/52209) | merged | Add routed expert loading for gpt-oss | `vllm/model_executor/models/gpt_oss.py`, `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` |
| 2026-07-29 | [#48703](https://github.com/vllm-project/vllm/pull/48703) | merged | [XPU] [UT] [CI] add xpu config to run gpt-oss accuracy in ut and ci | `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt` |
| 2026-06-23 | [#45818](https://github.com/vllm-project/vllm/pull/45818) | merged | [Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r… | `vllm/model_executor/models/gpt_oss.py` |
| 2026-06-23 | [#46441](https://github.com/vllm-project/vllm/pull/46441) | merged | fix gpt_oss pp>1 with ep | `vllm/model_executor/models/gpt_oss.py` |
| 2026-06-11 | [#45067](https://github.com/vllm-project/vllm/pull/45067) | merged | [Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor | `vllm/model_executor/models/gpt_oss.py` |
| 2026-05-30 | [#43571](https://github.com/vllm-project/vllm/pull/43571) | merged | [BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py | `tests/models/quantization/test_gpt_oss.py` |
| 2026-05-20 | [#43135](https://github.com/vllm-project/vllm/pull/43135) | merged | [Perf][gpt-oss] Downgrade triton_kernels to v3.5.1 | `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` |
| 2026-04-14 | [#39007](https://github.com/vllm-project/vllm/pull/39007) | merged | [MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/ | `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py` |
| 2026-04-02 | [#38292](https://github.com/vllm-project/vllm/pull/38292) | merged | [CI][ROCm] Add gpt-oss w4a8 in CI | `tests/evals/gpt_oss/configs/models-gfx950.txt` |
| 2026-04-02 | [#38778](https://github.com/vllm-project/vllm/pull/38778) | merged | Revert "[Kernel] Add gpt-oss Router GEMM kernel (#37205)" | `vllm/model_executor/models/gpt_oss.py` |
| 2026-03-20 | [#37683](https://github.com/vllm-project/vllm/pull/37683) | merged | [Perf] Eliminate redundant SparseMatrix creation in gpt_oss_triton_kernels | `tests/kernels/moe/test_gpt_oss_triton_kernels.py` |
| 2026-03-18 | [#37205](https://github.com/vllm-project/vllm/pull/37205) | merged | [Kernel] Add gpt-oss Router GEMM kernel | `vllm/model_executor/models/gpt_oss.py` |
| 2026-03-10 | [#36179](https://github.com/vllm-project/vllm/pull/36179) | merged | [ROCm][CI] Fix ROCm GPT-OSS Eval test group | `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt` |
| 2026-03-07 | [#36174](https://github.com/vllm-project/vllm/pull/36174) | merged | [ROCm][CI] Enable AITER for failing `test_gpt_oss` test case on MI355 | `tests/models/quantization/test_gpt_oss.py` |
| 2026-03-03 | [#35887](https://github.com/vllm-project/vllm/pull/35887) | merged | [ROCm][CI] Fix TP size issue for `test_gpt_oss` | `tests/models/quantization/test_gpt_oss.py` |
| 2026-03-03 | [#35806](https://github.com/vllm-project/vllm/pull/35806) | merged | [ROCm][CI] Fix Assertion Logic For `test_gpt_oss` | `tests/models/quantization/test_gpt_oss.py` |
| 2026-02-27 | [#35404](https://github.com/vllm-project/vllm/pull/35404) | merged | [Bugfix][Model] Fix gpt-oss batch invariance | `vllm/model_executor/models/gpt_oss.py` |
| 2026-02-11 | [#34337](https://github.com/vllm-project/vllm/pull/34337) | merged | [GPT-OSS] Remove unnecessary contiguous | `vllm/model_executor/models/gpt_oss.py` |
| 2026-02-10 | [#29008](https://github.com/vllm-project/vllm/pull/29008) | merged | [ROCm][Quantization] GPT_OSS in amd-quark format model loading and emulations | `vllm/model_executor/models/gpt_oss.py`, `tests/models/quantization/test_gpt_oss.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py` |
| 2026-01-28 | [#30976](https://github.com/vllm-project/vllm/pull/30976) | merged | Use aiter triton fused_add_rmsnorm_pad for gpt-oss | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-28 | [#29506](https://github.com/vllm-project/vllm/pull/29506) | merged | Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-20 | [#28244](https://github.com/vllm-project/vllm/pull/28244) | merged | Add truncate arg to yarn to match openai implementation of gpt-oss | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-16 | [#28765](https://github.com/vllm-project/vllm/pull/28765) | merged | Fix gpt oss weight loading with EP + bf16 | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-16 | [#28715](https://github.com/vllm-project/vllm/pull/28715) | merged | Fixed gpt-oss _load_weights_other() parameter position bug | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-12 | [#28536](https://github.com/vllm-project/vllm/pull/28536) | merged | [Bugfix] Fix gpt_oss packed_modules_mapping | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-11 | [#27334](https://github.com/vllm-project/vllm/pull/27334) | merged | [Quantization] fix attention quantization of gpt_oss model | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-05 | [#27786](https://github.com/vllm-project/vllm/pull/27786) | merged | [XPU] Add gpt-oss model support for Intel GPU | `vllm/model_executor/models/gpt_oss.py` |
| 2025-10-21 | [#24032](https://github.com/vllm-project/vllm/pull/24032) | merged | [BugFix] GPT-OSS Attention DP + MoE TP weight loading issue | `vllm/model_executor/models/gpt_oss.py` |
| 2025-10-01 | [#26030](https://github.com/vllm-project/vllm/pull/26030) | merged | [CI] Tweaks to GPT-OSS Eval (Blackwell) for stability | `tests/evals/gpt_oss/test_gpqa_correctness.py` |
| 2025-09-22 | [#25246](https://github.com/vllm-project/vllm/pull/25246) | merged | Enable Eagle3 speculative decoding for GPT-OSS model | `vllm/model_executor/models/gpt_oss.py` |
| 2025-09-17 | [#24920](https://github.com/vllm-project/vllm/pull/24920) | merged | [CI] GPT-OSS GPQA eval test for Blackwell | `tests/evals/gpt_oss/test_gpqa_correctness.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/__init__.py` |
| 2025-08-28 | [#23815](https://github.com/vllm-project/vllm/pull/23815) | merged | [Model] [gpt-oss] fix gpt-oss pp support | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-28 | [#23680](https://github.com/vllm-project/vllm/pull/23680) | merged | [Model] Add PP support and VLM backbone compatability for GPT-OSS | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-27 | [#23613](https://github.com/vllm-project/vllm/pull/23613) | merged | [Bugfix][gpt-oss] passing the cache config in gpt-oss | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-17 | [#22951](https://github.com/vllm-project/vllm/pull/22951) | merged | [Kernel] Add cuda kernel for gpt_oss activation | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-15 | [#22948](https://github.com/vllm-project/vllm/pull/22948) | merged | Revert "[Kernel] Add cuda kernel for gpt_oss activation" | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-15 | [#22538](https://github.com/vllm-project/vllm/pull/22538) | merged | [Kernel] Add cuda kernel for gpt_oss activation | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-13 | [#22678](https://github.com/vllm-project/vllm/pull/22678) | merged | Force TRTLLM attention for gpt-oss on SM100 | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-10 | [#22508](https://github.com/vllm-project/vllm/pull/22508) | merged | [oss] Init gpt-oss bf16 support | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-08 | [#22421](https://github.com/vllm-project/vllm/pull/22421) | merged | [gpt-oss] triton kernel mxfp4 | `tests/kernels/moe/test_gpt_oss_triton_kernels.py` |
| 2025-08-07 | [#22401](https://github.com/vllm-project/vllm/pull/22401) | merged | [gpt-oss] fix model config with hf_config | `vllm/model_executor/models/gpt_oss.py` |
| 2025-08-06 | [#22327](https://github.com/vllm-project/vllm/pull/22327) | merged | Add GPT-OSS model code and config [1/N] | `vllm/model_executor/models/gpt_oss.py` |

## Per-PR Diff Audit Cards

### PR #61257 - [Model Runner V2] Enable batch-sharded sampling for GPT-OSS

- Link: https://github.com/vllm-project/vllm/pull/61257
- Status/date: merged / 2026-10-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `2c74fd1873e3`
- Diff scope read: GitHub Pull Request files API returned 2 files, +118/-37, 215 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model Runner V2] Enable batch-sharded sampling for GPT-OSS"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Model Runner V2] Enable batch-sharded sampling for GPT-OSS"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -1482,6 +1482,9 @@ def compute_logits(self, hidden_states: torch.Tensor) -> t...; symbols: compute_logits, compute_logits_local, load_weights, touching `compute_logits, compute_logits_local, load_weights`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -1482,6 +1482,9 @@ def compute_logits(self, hidden_states: torch.Tensor) -> t...; symbols: compute_logits, compute_logits_local, load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -1482,6 +1482,9 @@ def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
+    def compute_logits_local(self, hidden_states: torch.Tensor) -> torch.Tensor:
+        return self.logits_processor(self.lm_head, hidden_states, skip_gather=True)
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +3/-0
- Risk and verification: The diff ships test coverage in `tests/v1/e2e/general/test_sharded_sampling.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55934 - [ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4)

- Link: https://github.com/vllm-project/vllm/pull/55934
- Status/date: merged / 2026-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`; associated commits `3e267bae70d8`
- Diff scope read: GitHub Pull Request files API returned 9 files, +270/-147, 718 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4)"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; technical summary: Covers "[ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4)"; the main implementation surface is `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +176/-38 (214 lines); hunks: -26,7 +26,7; -441,48 +441,59 @@ def _sort_tokens_pow2(expt_scal, expt_indx, n_expts_tot, b...; symbols: _sort_tokens_pow2, RoutingData, __init__, pack_bitmatrix, touching `_sort_tokens_pow2, RoutingData, __init__`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-2 (3 lines); hunks: -384,9 +384,8 @@ def test_routing_data_from_sparse_topk_parity(n_tokens, n_ex...; symbols: test_routing_data_from_sparse_topk_parity, touching `test_routing_data_from_sparse_topk_parity`.
- Code diff details:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +176/-38 (214 lines); hunks: -26,7 +26,7; -441,48 +441,59 @@ def _sort_tokens_pow2(expt_scal, expt_indx, n_expts_tot, b...; symbols: _sort_tokens_pow2, RoutingData, __init__, pack_bitmatrix
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-2 (3 lines); hunks: -384,9 +384,8 @@ def test_routing_data_from_sparse_topk_parity(n_tokens, n_ex...; symbols: test_routing_data_from_sparse_topk_parity
- Key code excerpts:

```diff
diff -- vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py
@@ -26,7 +26,7 @@
-from vllm.utils.import_utils import has_triton_kernels
+from vllm.utils.import_utils import get_triton_kernels_version, has_triton_kernels
@@ -441,48 +441,59 @@ def _sort_tokens_pow2(expt_scal, expt_indx, n_expts_tot, bitmatrix):
-# Two API generations of triton_kernels are supported:
-#   - v3.5.1 (the version bundled with vLLM): exposes `routing()` and
-#     `routing_from_bitmatrix()` in triton_kernels.routing; the `Bitmatrix`
diff -- tests/kernels/moe/test_gpt_oss_triton_kernels.py
@@ -384,9 +384,8 @@ def test_routing_data_from_sparse_topk_parity(n_tokens, n_experts, topk):
-    use_legacy_triton_kernels = gptoss_moe.use_legacy_triton_kernels
-    if use_legacy_triton_kernels:
+    if gptoss_moe.triton_kernels_version == "3.5.1":
```

- Reviewed files:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +176/-38
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45457 - [Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward

- Link: https://github.com/vllm-project/vllm/pull/45457
- Status/date: merged / 2026-08-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`; associated commits `129087ddab2b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +102/-15, 158 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; technical summary: Covers "[Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward"; the main implementation surface is `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +45/-14 (59 lines); hunks: -578,13 +578,14 @@ def triton_kernel_moe_forward(; -597,11 +598,23 @@ def triton_kernel_moe_forward(; symbols: triton_kernel_moe_forward, make_routing_data, routing_data_from_sparse_topk, touching `triton_kernel_moe_forward, make_routing_data, routing_data_from_sparse_topk`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +57/-1 (58 lines); hunks: -1,6 +1,6; -371,3 +371,59 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_routing_data_from_sparse_topk_parity, assert_equivalent, touching `test_unit_shuffle, test_routing_data_from_sparse_topk_parity, assert_equivalent`.
- Code diff details:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +45/-14 (59 lines); hunks: -578,13 +578,14 @@ def triton_kernel_moe_forward(; -597,11 +598,23 @@ def triton_kernel_moe_forward(; symbols: triton_kernel_moe_forward, make_routing_data, routing_data_from_sparse_topk
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +57/-1 (58 lines); hunks: -1,6 +1,6; -371,3 +371,59 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_routing_data_from_sparse_topk_parity, assert_equivalent
- Key code excerpts:

```diff
diff -- vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py
@@ -578,13 +578,14 @@ def triton_kernel_moe_forward(
+        is_sparse_topk = not isinstance(topk_result, tuple)
-        if isinstance(topk_result, tuple):
-            topk_weights, topk_ids_raw, _ = topk_result
-        else:
+        if is_sparse_topk:
+        else:
diff -- tests/kernels/moe/test_gpt_oss_triton_kernels.py
@@ -1,6 +1,6 @@
-from dataclasses import dataclass, fields
+from dataclasses import dataclass, fields, is_dataclass
@@ -371,3 +371,59 @@ def test_unit_shuffle():
+@pytest.mark.parametrize("n_tokens", [1, 33, 512])
+@pytest.mark.parametrize("n_experts,topk", [(32, 4), (128, 4)])
+def test_routing_data_from_sparse_topk_parity(n_tokens, n_experts, topk):
```

- Reviewed files:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +45/-14
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +57/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #52209 - Add routed expert loading for gpt-oss

- Link: https://github.com/vllm-project/vllm/pull/52209
- Status/date: merged / 2026-08-23
- Trace source: `git log --name-only -- <model-files>` found it through `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`, `vllm/model_executor/models/gpt_oss.py`; associated commits `b26039b09fc9`
- Diff scope read: GitHub Pull Request files API returned 4 files, +370/-3, 446 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add routed expert loading for gpt-oss"; model line: GPT-OSS; category: docs/tests/CI; main diff: `vllm/model_executor/models/gpt_oss.py`, `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`; technical summary: Covers "Add routed expert loading for gpt-oss"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`, `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +197/-0 (197 lines); hunks: -25,6 +25,7; -68,6 +69,15; symbols: OAIAttention, forward, GptOssRoutedExperts, _narrow_for_rank, touching `OAIAttention, forward, GptOssRoutedExperts`; `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: _TestExperts, __init__, _map_global_expert_id_to_local_expert_id, _load, touching `_TestExperts, __init__, _map_global_expert_id_to_local_expert_id`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +197/-0 (197 lines); hunks: -25,6 +25,7; -68,6 +69,15; symbols: OAIAttention, forward, GptOssRoutedExperts, _narrow_for_rank
  - `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: _TestExperts, __init__, _map_global_expert_id_to_local_expert_id, _load
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -25,6 +25,7 @@
+from vllm.model_executor.layers.fused_moe.routed_experts import RoutedExperts
@@ -68,6 +69,15 @@
+_GPT_OSS_STREAMED_EXPERT_SUFFIX_TO_SHARD = {
+    "w13_weight": "gpt_oss_w13",
+    "w2_weight": "gpt_oss_w2",
+    "w13_bias": "gpt_oss_w13",
diff -- tests/model_executor/model_loader/test_gpt_oss_weight_loading.py
@@ -0,0 +1,152 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from types import SimpleNamespace
+import pytest
+import torch
+from vllm.model_executor.models.gpt_oss import (
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +197/-0
  - tests: `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` added +152/-0
- Risk and verification: The diff ships test coverage in `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`, `tests/model_executor/model_loader/test_reload.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #48703 - [XPU] [UT] [CI] add xpu config to run gpt-oss accuracy in ut and ci

- Link: https://github.com/vllm-project/vllm/pull/48703
- Status/date: merged / 2026-07-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`; associated commits `7de49bab7e91`
- Diff scope read: GitHub Pull Request files API returned 4 files, +38/-0, 48 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[XPU] [UT] [CI] add xpu config to run gpt-oss accuracy in ut and ci"; model line: GPT-OSS; category: performance/backend optimization; main diff: `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`; technical summary: Covers "[XPU] [UT] [CI] add xpu config to run gpt-oss accuracy in ut and ci"; the main implementation surface is `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6; `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` added +5/-0 (5 lines); hunks: -0,0 +1,5; `tests/evals/gpt_oss/configs/models-xpu.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3.
- Code diff details:
  - `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` added +5/-0 (5 lines); hunks: -0,0 +1,5
  - `tests/evals/gpt_oss/configs/models-xpu.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3
- Key code excerpts:

```diff
diff -- tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml
@@ -0,0 +1,6 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+model_name: openai/gpt-oss-20b
+metric_threshold: 0.568
+reasoning_effort: low
+server_args: "--attention-backend TRITON_ATTN"
diff -- tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml
@@ -0,0 +1,5 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+model_name: openai/gpt-oss-20b
+metric_threshold: 0.568
+reasoning_effort: low
diff -- tests/evals/gpt_oss/configs/models-xpu.txt
@@ -0,0 +1,3 @@
+# Intel XPU model configurations for GPQA evaluation
```

- Reviewed files:
  - tests: `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` added +6/-0; `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` added +5/-0; `tests/evals/gpt_oss/configs/models-xpu.txt` added +3/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45818 - [Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r…

- Link: https://github.com/vllm-project/vllm/pull/45818
- Status/date: merged / 2026-06-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `f4d5f73ffa40`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r…"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r…"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -979,7 +979,11 @@ def _load_weights_other(; symbols: _load_weights_other, touching `_load_weights_other`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -979,7 +979,11 @@ def _load_weights_other(; symbols: _load_weights_other
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -979,7 +979,11 @@ def _load_weights_other(
-        for name, weight in weights:
+        # Use centralized weight remapping for MoE expert parameters.
+        # The FusedMoE refactor moved expert params under
+        # `mlp.experts.routed_experts.*`; this remaps checkpoint names so
+        # MoE weight/bias keys resolve against params_dict.
+        for name, weight in remap_moe_expert_weights(weights, params_dict):
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #46441 - fix gpt_oss pp>1 with ep

- Link: https://github.com/vllm-project/vllm/pull/46441
- Status/date: merged / 2026-06-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `901a3b091cf1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix gpt_oss pp>1 with ep"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "fix gpt_oss pp>1 with ep"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1078,7 +1078,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1078,7 +1078,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -1078,7 +1078,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-        ep_rank = get_ep_group().rank
+        ep_rank = get_ep_group().rank_in_group
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #45067 - [Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor

- Link: https://github.com/vllm-project/vllm/pull/45067
- Status/date: merged / 2026-06-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `7920ccb97c2d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +7/-0, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +7/-0 (7 lines); hunks: -635,6 +635,13 @@ def _get_moe_weight_dtype(layer_id: int = 0) -> str | None:; symbols: _get_moe_weight_dtype, touching `_get_moe_weight_dtype`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +7/-0 (7 lines); hunks: -635,6 +635,13 @@ def _get_moe_weight_dtype(layer_id: int = 0) -> str | None:; symbols: _get_moe_weight_dtype
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -635,6 +635,13 @@ def _get_moe_weight_dtype(layer_id: int = 0) -> str | None:
+                # The MoE refactor (#41184) moved expert params under
+                # `mlp.experts.routed_experts.*`; remap the legacy checkpoint
+                # name so keys like w2_bias resolve against params_dict.
+                fused_name = fused_name.replace(
+                    ".mlp.experts.", ".mlp.experts.routed_experts."
+                )
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +7/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #43571 - [BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py

- Link: https://github.com/vllm-project/vllm/pull/43571
- Status/date: merged / 2026-05-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_gpt_oss.py`; associated commits `e9499996df89`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-1, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py"; model line: GPT-OSS; category: bug fix; main diff: `tests/models/quantization/test_gpt_oss.py`; technical summary: Covers "[BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py"; the main implementation surface is `tests/models/quantization/test_gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -22,7 +22,14; symbols: on_gfx950, touching `on_gfx950`.
- Code diff details:
  - `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -22,7 +22,14; symbols: on_gfx950
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_gpt_oss.py
@@ -22,7 +22,14 @@
-from vllm.platforms.rocm import on_gfx950
+if current_platform.is_rocm():
+    from vllm.platforms.rocm import on_gfx950
+else:
+    def on_gfx950() -> bool:
+        return False
```

- Reviewed files:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +8/-1
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_gpt_oss.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #43135 - [Perf][gpt-oss] Downgrade triton_kernels to v3.5.1

- Link: https://github.com/vllm-project/vllm/pull/43135
- Status/date: merged / 2026-05-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`; associated commits `5774aad9c5b6`
- Diff scope read: GitHub Pull Request files API returned 3 files, +73/-57, 204 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][gpt-oss] Downgrade triton_kernels to v3.5.1"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`; technical summary: Covers "[Perf][gpt-oss] Downgrade triton_kernels to v3.5.1"; the main implementation surface is `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +57/-32 (89 lines); hunks: -209,6 +209,16 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitmat...; -233,11 +243,10 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitma...; symbols: _make_bitmatrix_metadata_pow2_safe, triton_kernel_moe_forward, touching `_make_bitmatrix_metadata_pow2_safe, triton_kernel_moe_forward`.
- Code diff details:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +57/-32 (89 lines); hunks: -209,6 +209,16 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitmat...; -233,11 +243,10 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitma...; symbols: _make_bitmatrix_metadata_pow2_safe, triton_kernel_moe_forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py
@@ -209,6 +209,16 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitmatrix):
+# Two API generations of triton_kernels are supported:
+#   - v3.5.1 (the version bundled with vLLM): exposes `routing()` and
+#     `routing_from_bitmatrix()` in triton_kernels.routing; the `Bitmatrix`
+#     constructor takes a `scratchpad` argument.
+#   - v3.6.0+: removes the `routing` module in favor of a `SparseMatrix`
+#     based path, and adds a `dtype=BIT` kwarg to `Bitmatrix`. Used only
```

- Reviewed files:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +57/-32
- Risk and verification: The diff ships test coverage in `tests/kernels/quantization/test_mxfp4_triton_ep.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39007 - [MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/

- Link: https://github.com/vllm-project/vllm/pull/39007
- Status/date: merged / 2026-04-14
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`; associated commits `1a9353bb02e6`
- Diff scope read: GitHub Pull Request files API returned 8 files, +16/-12, 100 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; technical summary: Covers "[MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/"; the main implementation surface is `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` renamed +0/-0 (0 lines); `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-1 (2 lines); hunks: -25,7 +25,7.
- Code diff details:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` renamed +0/-0 (0 lines)
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-1 (2 lines); hunks: -25,7 +25,7
- Key code excerpts:

```diff
diff -- tests/kernels/moe/test_gpt_oss_triton_kernels.py
@@ -25,7 +25,7 @@
-from vllm.model_executor.layers.fused_moe.gpt_oss_triton_kernels_moe import (
+from vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe import (
```

- Reviewed files:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` renamed +0/-0
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/kernels/moe/test_modular_oai_triton_moe.py`, `tests/kernels/quantization/test_mxfp4_triton_ep.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #38292 - [CI][ROCm] Add gpt-oss w4a8 in CI

- Link: https://github.com/vllm-project/vllm/pull/38292
- Status/date: merged / 2026-04-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gpt_oss/configs/models-gfx950.txt`; associated commits `82a006beebf0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +10/-1, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI][ROCm] Add gpt-oss w4a8 in CI"; model line: GPT-OSS; category: docs/tests/CI; main diff: `tests/evals/gpt_oss/configs/models-gfx950.txt`; technical summary: Covers "[CI][ROCm] Add gpt-oss w4a8 in CI"; the main implementation surface is `tests/evals/gpt_oss/configs/models-gfx950.txt`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gpt_oss/configs/models-gfx950.txt` modified +2/-1 (3 lines); hunks: -1,3 +1,4.
- Code diff details:
  - `tests/evals/gpt_oss/configs/models-gfx950.txt` modified +2/-1 (3 lines); hunks: -1,3 +1,4
- Key code excerpts:

```diff
diff -- tests/evals/gpt_oss/configs/models-gfx950.txt
@@ -1,3 +1,4 @@
-gpt-oss-20b-rocm-baseline.yaml
+gpt-oss-20b-rocm-baseline.yaml
+gpt-oss-20b-rocm-mxfp4-fp8.yaml
```

- Reviewed files:
  - tests: `tests/evals/gpt_oss/configs/models-gfx950.txt` modified +2/-1
- Risk and verification: The diff ships test coverage in `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-mxfp4-fp8.yaml`, `tests/evals/gpt_oss/configs/models-gfx950.txt`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #38778 - Revert "[Kernel] Add gpt-oss Router GEMM kernel (#37205)"

- Link: https://github.com/vllm-project/vllm/pull/38778
- Status/date: merged / 2026-04-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `9bd723110689`
- Diff scope read: GitHub Pull Request files API returned 13 files, +12/-875, 1027 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Revert "[Kernel] Add gpt-oss Router GEMM kernel (#37205)""; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Revert "[Kernel] Add gpt-oss Router GEMM kernel (#37205)""; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -20,11 +20,12; -174,11 +175,13 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -20,11 +20,12; -174,11 +175,13 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -20,11 +20,12 @@
-from vllm.model_executor.layers.fused_moe import FusedMoE, GateLinear
+from vllm.model_executor.layers.fused_moe import FusedMoE
+    ReplicatedLinear,
@@ -174,11 +175,13 @@ def __init__(
-        self.router = GateLinear(
+        self.router = ReplicatedLinear(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +6/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_router_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37683 - [Perf] Eliminate redundant SparseMatrix creation in gpt_oss_triton_kernels

- Link: https://github.com/vllm-project/vllm/pull/37683
- Status/date: merged / 2026-03-20
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; associated commits `d0532bf38da5`
- Diff scope read: GitHub Pull Request files API returned 2 files, +73/-4, 108 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Eliminate redundant SparseMatrix creation in gpt_oss_triton_kernels"; model line: GPT-OSS; category: performance/backend optimization; main diff: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; technical summary: Covers "[Perf] Eliminate redundant SparseMatrix creation in gpt_oss_triton_kernels"; the main implementation surface is `tests/kernels/moe/test_gpt_oss_triton_kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +44/-0 (44 lines); hunks: -21,12 +21,16; -355,3 +359,43 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_legacy_routing, touching `test_unit_shuffle, test_legacy_routing`.
- Code diff details:
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +44/-0 (44 lines); hunks: -21,12 +21,16; -355,3 +359,43 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_legacy_routing
- Key code excerpts:

```diff
diff -- tests/kernels/moe/test_gpt_oss_triton_kernels.py
@@ -21,12 +21,16 @@
+from triton_kernels.topk import topk as topk_fn
+    legacy_routing,
+    make_routing_data,
+from vllm.utils.torch_utils import set_random_seed
@@ -355,3 +359,43 @@ def test_unit_shuffle():
+@pytest.mark.parametrize("num_tokens", [2, 8, 64])
```

- Reviewed files:
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +44/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37205 - [Kernel] Add gpt-oss Router GEMM kernel

- Link: https://github.com/vllm-project/vllm/pull/37205
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `9bd723110689`, `b1169d7be8ad`
- Diff scope read: GitHub Pull Request files API returned 13 files, +875/-13, 1035 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Add gpt-oss Router GEMM kernel"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Kernel] Add gpt-oss Router GEMM kernel"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +3/-7 (10 lines); hunks: -20,12 +20,11; -175,13 +174,11 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +3/-7 (10 lines); hunks: -20,12 +20,11; -175,13 +174,11 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -20,12 +20,11 @@
-from vllm.model_executor.layers.fused_moe import FusedMoE
+from vllm.model_executor.layers.fused_moe import FusedMoE, GateLinear
-    ReplicatedLinear,
@@ -175,13 +174,11 @@ def __init__(
-        self.router = ReplicatedLinear(
+        self.router = GateLinear(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +3/-7
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_router_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36179 - [ROCm][CI] Fix ROCm GPT-OSS Eval test group

- Link: https://github.com/vllm-project/vllm/pull/36179
- Status/date: merged / 2026-03-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`; associated commits `179547d62c73`
- Diff scope read: GitHub Pull Request files API returned 4 files, +16/-4, 40 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI] Fix ROCm GPT-OSS Eval test group"; model line: GPT-OSS; category: bug fix; main diff: `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`; technical summary: Covers "[ROCm][CI] Fix ROCm GPT-OSS Eval test group"; the main implementation surface is `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6; `tests/evals/gpt_oss/configs/models-gfx942.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3; `tests/evals/gpt_oss/configs/models-gfx950.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3.
- Code diff details:
  - `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `tests/evals/gpt_oss/configs/models-gfx942.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3
  - `tests/evals/gpt_oss/configs/models-gfx950.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3
- Key code excerpts:

```diff
diff -- tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml
@@ -0,0 +1,6 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+model_name: openai/gpt-oss-20b
+metric_threshold: 0.568
+reasoning_effort: low
+server_args: "--attention-backend ROCM_AITER_UNIFIED_ATTN"
diff -- tests/evals/gpt_oss/configs/models-gfx942.txt
@@ -0,0 +1,3 @@
+# GFX942 model configurations for GPQA evaluation
+# Tests different environment variable combinations
+gpt-oss-20b-rocm-baseline.yaml
diff -- tests/evals/gpt_oss/configs/models-gfx950.txt
@@ -0,0 +1,3 @@
+# GFX950 model configurations for GPQA evaluation
+# Tests different environment variable combinations
+gpt-oss-20b-rocm-baseline.yaml
```

- Reviewed files:
  - tests: `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` added +6/-0; `tests/evals/gpt_oss/configs/models-gfx942.txt` added +3/-0; `tests/evals/gpt_oss/configs/models-gfx950.txt` added +3/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36174 - [ROCm][CI] Enable AITER for failing `test_gpt_oss` test case on MI355

- Link: https://github.com/vllm-project/vllm/pull/36174
- Status/date: merged / 2026-03-07
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_gpt_oss.py`; associated commits `fc4657756ff0`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-1, 27 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI] Enable AITER for failing `test_gpt_oss` test case on MI355"; model line: GPT-OSS; category: performance/backend optimization; main diff: `tests/models/quantization/test_gpt_oss.py`; technical summary: Covers "[ROCm][CI] Enable AITER for failing `test_gpt_oss` test case on MI355"; the main implementation surface is `tests/models/quantization/test_gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -21,6 +21,7; -83,11 +84,17 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization, touching `get_model_args, test_gpt_oss_attention_quantization`.
- Code diff details:
  - `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -21,6 +21,7; -83,11 +84,17 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_gpt_oss.py
@@ -21,6 +21,7 @@
+from vllm.platforms.rocm import on_gfx950
@@ -83,11 +84,17 @@ def get_model_args(self, tp_size: int):
-    model_name: str, tp_size: int, expected_accuracy: float
+    model_name: str,
+    tp_size: int,
+    expected_accuracy: float,
```

- Reviewed files:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +8/-1
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_gpt_oss.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #35887 - [ROCm][CI] Fix TP size issue for `test_gpt_oss`

- Link: https://github.com/vllm-project/vllm/pull/35887
- Status/date: merged / 2026-03-03
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_gpt_oss.py`; associated commits `e7213003cbf6`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-0, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI] Fix TP size issue for `test_gpt_oss`"; model line: GPT-OSS; category: bug fix; main diff: `tests/models/quantization/test_gpt_oss.py`; technical summary: Covers "[ROCm][CI] Fix TP size issue for `test_gpt_oss`"; the main implementation surface is `tests/models/quantization/test_gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_gpt_oss.py` modified +5/-0 (5 lines); hunks: -21,6 +21,8; -83,6 +85,9 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization, touching `get_model_args, test_gpt_oss_attention_quantization`.
- Code diff details:
  - `tests/models/quantization/test_gpt_oss.py` modified +5/-0 (5 lines); hunks: -21,6 +21,8; -83,6 +85,9 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_gpt_oss.py
@@ -21,6 +21,8 @@
+from vllm.utils.torch_utils import cuda_device_count_stateless
@@ -83,6 +85,9 @@ def get_model_args(self, tp_size: int):
+    if tp_size > cuda_device_count_stateless():
+        pytest.skip("Not enough GPUs to run this test case")
```

- Reviewed files:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +5/-0
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_gpt_oss.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #35806 - [ROCm][CI] Fix Assertion Logic For `test_gpt_oss`

- Link: https://github.com/vllm-project/vllm/pull/35806
- Status/date: merged / 2026-03-03
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/quantization/test_gpt_oss.py`; associated commits `8b9e8b74541e`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-5, 22 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI] Fix Assertion Logic For `test_gpt_oss`"; model line: GPT-OSS; category: bug fix; main diff: `tests/models/quantization/test_gpt_oss.py`; technical summary: Covers "[ROCm][CI] Fix Assertion Logic For `test_gpt_oss`"; the main implementation surface is `tests/models/quantization/test_gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/quantization/test_gpt_oss.py` modified +5/-5 (10 lines); hunks: -12,8 +12,8; -104,7 +104,7 @@ def test_gpt_oss_attention_quantization(; symbols: test_gpt_oss_attention_quantization, touching `test_gpt_oss_attention_quantization`.
- Code diff details:
  - `tests/models/quantization/test_gpt_oss.py` modified +5/-5 (10 lines); hunks: -12,8 +12,8; -104,7 +104,7 @@ def test_gpt_oss_attention_quantization(; symbols: test_gpt_oss_attention_quantization
- Key code excerpts:

```diff
diff -- tests/models/quantization/test_gpt_oss.py
@@ -12,8 +12,8 @@
-import importlib
+import importlib.util
@@ -104,7 +104,7 @@ def test_gpt_oss_attention_quantization(
-    assert (
-        measured_accuracy - rtol < expected_accuracy
-        and measured_accuracy + rtol > expected_accuracy
```

- Reviewed files:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +5/-5
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_gpt_oss.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #35404 - [Bugfix][Model] Fix gpt-oss batch invariance

- Link: https://github.com/vllm-project/vllm/pull/35404
- Status/date: merged / 2026-02-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `1f3dbd95fd13`
- Diff scope read: GitHub Pull Request files API returned 2 files, +14/-8, 50 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] Fix gpt-oss batch invariance"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Bugfix][Model] Fix gpt-oss batch invariance"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +13/-2 (15 lines); hunks: -23,7 +23,11; -165,7 +169,14 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +13/-2 (15 lines); hunks: -23,7 +23,11; -165,7 +169,14 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -23,7 +23,11 @@
-from vllm.model_executor.layers.linear import QKVParallelLinear, RowParallelLinear
+from vllm.model_executor.layers.linear import (
+    QKVParallelLinear,
+    ReplicatedLinear,
+    RowParallelLinear,
+)
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +13/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34337 - [GPT-OSS] Remove unnecessary contiguous

- Link: https://github.com/vllm-project/vllm/pull/34337
- Status/date: merged / 2026-02-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `83e26c834ef1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-1, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GPT-OSS] Remove unnecessary contiguous"; model line: GPT-OSS; category: model implementation change; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[GPT-OSS] Remove unnecessary contiguous"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +0/-1 (1 lines); hunks: -140,7 +140,6 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +0/-1 (1 lines); hunks: -140,7 +140,6 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -140,7 +140,6 @@ def forward(
-        v = v.contiguous()
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +0/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #29008 - [ROCm][Quantization] GPT_OSS in amd-quark format model loading and emulations

- Link: https://github.com/vllm-project/vllm/pull/29008
- Status/date: merged / 2026-02-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/quantization/test_gpt_oss.py`, `vllm/model_executor/models/gpt_oss.py`; associated commits `b129136c7a73`
- Diff scope read: GitHub Pull Request files API returned 13 files, +1094/-213, 1860 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Quantization] GPT_OSS in amd-quark format model loading and emulations"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/models/gpt_oss.py`, `tests/models/quantization/test_gpt_oss.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; technical summary: Covers "[ROCm][Quantization] GPT_OSS in amd-quark format model loading and emulations"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`, `tests/models/quantization/test_gpt_oss.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +491/-18 (509 lines); hunks: -1,6 +1,7; -25,13 +26,17; symbols: __init__, forward, get_expert_mapping, _load_weights_mxfp4, touching `__init__, forward, get_expert_mapping`; `tests/models/quantization/test_gpt_oss.py` added +110/-0 (110 lines); hunks: -0,0 +1,110; symbols: has_huggingface_access, ModelCase, EvaluationConfig, get_model_args, touching `has_huggingface_access, ModelCase, EvaluationConfig`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +13/-7 (20 lines); hunks: -22,7 +22,7; -298,12 +298,18 @@ def test_equiv(num_token, a_dtype, w_dtype, tp, workspace_...; symbols: test_equiv, touching `test_equiv`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +491/-18 (509 lines); hunks: -1,6 +1,7; -25,13 +26,17; symbols: __init__, forward, get_expert_mapping, _load_weights_mxfp4
  - `tests/models/quantization/test_gpt_oss.py` added +110/-0 (110 lines); hunks: -0,0 +1,110; symbols: has_huggingface_access, ModelCase, EvaluationConfig, get_model_args
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +13/-7 (20 lines); hunks: -22,7 +22,7; -298,12 +298,18 @@ def test_equiv(num_token, a_dtype, w_dtype, tp, workspace_...; symbols: test_equiv
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -1,6 +1,7 @@
-from collections.abc import Iterable
+import typing
+from collections.abc import Callable, Iterable
@@ -25,13 +26,17 @@
+from vllm.model_executor.layers.quantization.utils.ocp_mx_utils import OCP_MX_BLOCK_SIZE
-from vllm.model_executor.model_loader.weight_utils import default_weight_loader
diff -- tests/models/quantization/test_gpt_oss.py
@@ -0,0 +1,110 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""
+End-to-end accuracy test for GPT-OSS model quantization.
+Config:
+    Task:   gsm8k_platinum
diff -- tests/kernels/moe/test_gpt_oss_triton_kernels.py
@@ -22,7 +22,7 @@
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +491/-18
  - tests: `tests/models/quantization/test_gpt_oss.py` added +110/-0; `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +13/-7
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/quantization/test_gpt_oss.py`, `tests/models/quantization/test_gpt_oss_attn_quantization.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30976 - Use aiter triton fused_add_rmsnorm_pad for gpt-oss

- Link: https://github.com/vllm-project/vllm/pull/30976
- Status/date: merged / 2026-01-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `59bcc5b6f2e6`
- Diff scope read: GitHub Pull Request files API returned 9 files, +327/-11, 489 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Use aiter triton fused_add_rmsnorm_pad for gpt-oss"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Use aiter triton fused_add_rmsnorm_pad for gpt-oss"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -187,7 +187,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -187,7 +187,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -187,7 +187,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:
-        x = self.experts(hidden_states=x, router_logits=g)
+        x = self.experts(hidden_states=x, router_logits=g)[:, : self.hidden_size]
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/compile/test_fuse_act_padding.py`, `tests/compile/test_fusion.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29506 - Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights

- Link: https://github.com/vllm-project/vllm/pull/29506
- Status/date: merged / 2025-11-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `5f5521bd5d7d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -647,8 +647,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -647,8 +647,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -647,8 +647,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-                ep_rank_start,
+                ep_rank_start,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28244 - Add truncate arg to yarn to match openai implementation of gpt-oss

- Link: https://github.com/vllm-project/vllm/pull/28244
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `6eb745d9bdf5`
- Diff scope read: GitHub Pull Request files API returned 4 files, +12/-7, 60 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add truncate arg to yarn to match openai implementation of gpt-oss"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Add truncate arg to yarn to match openai implementation of gpt-oss"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-0 (1 lines); hunks: -78,6 +78,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-0 (1 lines); hunks: -78,6 +78,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -78,6 +78,7 @@ def __init__(
+                "truncate": config.rope_parameters.get("truncate", True),
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28765 - Fix gpt oss weight loading with EP + bf16

- Link: https://github.com/vllm-project/vllm/pull/28765
- Status/date: merged / 2025-11-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `8d259fad6cd5`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix gpt oss weight loading with EP + bf16"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Fix gpt oss weight loading with EP + bf16"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -494,8 +494,8 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other, touching `_load_weights_mxfp4, _load_weights_other`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -494,8 +494,8 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -494,8 +494,8 @@ def _load_weights_mxfp4(
-        ep_rank_start: int,
+        ep_rank_start: int,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28715 - Fixed gpt-oss _load_weights_other() parameter position bug

- Link: https://github.com/vllm-project/vllm/pull/28715
- Status/date: merged / 2025-11-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `af02c409702f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fixed gpt-oss _load_weights_other() parameter position bug"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Fixed gpt-oss _load_weights_other() parameter position bug"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -641,8 +641,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -641,8 +641,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -641,8 +641,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-                ep_rank_end,
+                ep_rank_end,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28536 - [Bugfix] Fix gpt_oss packed_modules_mapping

- Link: https://github.com/vllm-project/vllm/pull/28536
- Status/date: merged / 2025-11-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `a9d18b51078d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-5, 31 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix gpt_oss packed_modules_mapping"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Bugfix] Fix gpt_oss packed_modules_mapping"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +5/-5 (10 lines); hunks: -92,7 +92,7 @@ def __init__(; -129,7 +129,7 @@ def __init__(; symbols: __init__, forward, _load_weights_other, load_weights, touching `__init__, forward, _load_weights_other`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +5/-5 (10 lines); hunks: -92,7 +92,7 @@ def __init__(; -129,7 +129,7 @@ def __init__(; symbols: __init__, forward, _load_weights_other, load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -92,7 +92,7 @@ def __init__(
-        self.qkv = QKVParallelLinear(
+        self.qkv_proj = QKVParallelLinear(
@@ -129,7 +129,7 @@ def __init__(
-        qkv, _ = self.qkv(hidden_states)
+        qkv, _ = self.qkv_proj(hidden_states)
@@ -606,9 +606,9 @@ def _load_weights_other(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +5/-5
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27334 - [Quantization] fix attention quantization of gpt_oss model

- Link: https://github.com/vllm-project/vllm/pull/27334
- Status/date: merged / 2025-11-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `5a1271d83a65`
- Diff scope read: GitHub Pull Request files API returned 3 files, +101/-4, 154 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Quantization] fix attention quantization of gpt_oss model"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Quantization] fix attention quantization of gpt_oss model"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +8/-2 (10 lines); hunks: -198,6 +198,7 @@ class TransformerBlock(torch.nn.Module):; -207,7 +208,10 @@ def __init__(; symbols: TransformerBlock, __init__, touching `TransformerBlock, __init__`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +8/-2 (10 lines); hunks: -198,6 +198,7 @@ class TransformerBlock(torch.nn.Module):; -207,7 +208,10 @@ def __init__(; symbols: TransformerBlock, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -198,6 +198,7 @@ class TransformerBlock(torch.nn.Module):
+        quant_config: QuantizationConfig,
@@ -207,7 +208,10 @@ def __init__(
-            config, prefix=f"{prefix}.attn", cache_config=cache_config
+            config,
+            prefix=f"{prefix}.attn",
+            quant_config=quant_config,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +8/-2
- Risk and verification: The diff ships test coverage in `tests/models/quantization/test_gpt_oss_attn_quantization.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27786 - [XPU] Add gpt-oss model support for Intel GPU

- Link: https://github.com/vllm-project/vllm/pull/27786
- Status/date: merged / 2025-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `18b39828d904`
- Diff scope read: GitHub Pull Request files API returned 4 files, +101/-6, 160 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[XPU] Add gpt-oss model support for Intel GPU"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[XPU] Add gpt-oss model support for Intel GPU"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +0/-3 (3 lines); hunks: -329,9 +329,6 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, touching `_load_weights_mxfp4`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +0/-3 (3 lines); hunks: -329,9 +329,6 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -329,9 +329,6 @@ def _load_weights_mxfp4(
-            # FIXME(woosuk): Remove this after testing.
-            weight = weight.cuda()
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +0/-3
- Risk and verification: Runtime changes concentrate in `vllm/attention/utils/fa_utils.py`, `vllm/model_executor/layers/quantization/mxfp4.py`, `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24032 - [BugFix] GPT-OSS Attention DP + MoE TP weight loading issue

- Link: https://github.com/vllm-project/vllm/pull/24032
- Status/date: merged / 2025-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `aef368aa0857`
- Diff scope read: GitHub Pull Request files API returned 2 files, +30/-13, 89 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix] GPT-OSS Attention DP + MoE TP weight loading issue"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[BugFix] GPT-OSS Attention DP + MoE TP weight loading issue"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +16/-4 (20 lines); hunks: -11,13 +11,15; -305,8 +307,13 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other, touching `_load_weights_mxfp4, _load_weights_other`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +16/-4 (20 lines); hunks: -11,13 +11,15; -305,8 +307,13 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -11,13 +11,15 @@
+    get_dp_group,
+from vllm.model_executor.layers.fused_moe.config import FusedMoEParallelConfig
@@ -305,8 +307,13 @@ def _load_weights_mxfp4(
-        tp_rank = get_tensor_model_parallel_rank()
-        tp_size = get_tensor_model_parallel_world_size()
+        # In MoE, we need to flatten the tensor parallel size across the data
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +16/-4
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26030 - [CI] Tweaks to GPT-OSS Eval (Blackwell) for stability

- Link: https://github.com/vllm-project/vllm/pull/26030
- Status/date: merged / 2025-10-01
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gpt_oss/test_gpqa_correctness.py`; associated commits `ee04c0cd04cf`
- Diff scope read: GitHub Pull Request files API returned 2 files, +3/-4, 28 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Tweaks to GPT-OSS Eval (Blackwell) for stability"; model line: GPT-OSS; category: docs/tests/CI; main diff: `tests/evals/gpt_oss/test_gpqa_correctness.py`; technical summary: Covers "[CI] Tweaks to GPT-OSS Eval (Blackwell) for stability"; the main implementation surface is `tests/evals/gpt_oss/test_gpqa_correctness.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gpt_oss/test_gpqa_correctness.py` modified +2/-3 (5 lines); hunks: -26,7 +26,8 @@ def run_gpqa_eval(model_name: str, base_url: str) -> float:; -72,8 +73,6 @@ def test_gpqa_correctness(request):; symbols: run_gpqa_eval, test_gpqa_correctness, touching `run_gpqa_eval, test_gpqa_correctness`.
- Code diff details:
  - `tests/evals/gpt_oss/test_gpqa_correctness.py` modified +2/-3 (5 lines); hunks: -26,7 +26,8 @@ def run_gpqa_eval(model_name: str, base_url: str) -> float:; -72,8 +73,6 @@ def test_gpqa_correctness(request):; symbols: run_gpqa_eval, test_gpqa_correctness
- Key code excerpts:

```diff
diff -- tests/evals/gpt_oss/test_gpqa_correctness.py
@@ -26,7 +26,8 @@ def run_gpqa_eval(model_name: str, base_url: str) -> float:
-        model_name, "--reasoning-effort", "low", "--base-url", base_url
+        model_name, "--reasoning-effort", "low", "--base-url", base_url,
+        "--n-threads", "200"
@@ -72,8 +73,6 @@ def test_gpqa_correctness(request):
-        "--max-model-len",
-        "32768",
```

- Reviewed files:
  - tests: `tests/evals/gpt_oss/test_gpqa_correctness.py` modified +2/-3
- Risk and verification: The diff ships test coverage in `tests/evals/gpt_oss/test_gpqa_correctness.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #25246 - Enable Eagle3 speculative decoding for GPT-OSS model

- Link: https://github.com/vllm-project/vllm/pull/25246
- Status/date: merged / 2025-09-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `21467f9a1c62`
- Diff scope read: GitHub Pull Request files API returned 3 files, +41/-12, 111 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Enable Eagle3 speculative decoding for GPT-OSS model"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Enable Eagle3 speculative decoding for GPT-OSS model"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +17/-2 (19 lines); hunks: -28,7 +28,7; -239,6 +239,7 @@ def __init__(; symbols: __init__, get_input_embeddings, forward, _load_weights_mxfp4, touching `__init__, get_input_embeddings, forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +17/-2 (19 lines); hunks: -28,7 +28,7; -239,6 +239,7 @@ def __init__(; symbols: __init__, get_input_embeddings, forward, _load_weights_mxfp4
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -28,7 +28,7 @@
-from .interfaces import SupportsPP
+from .interfaces import SupportsEagle3, SupportsPP
@@ -239,6 +239,7 @@ def __init__(
+        self.aux_hidden_state_layers = tuple[int, ...]()
@@ -262,15 +263,22 @@ def forward(
+        aux_hidden_states = []
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +17/-2
- Risk and verification: Runtime changes concentrate in `vllm/config/speculative.py`, `vllm/model_executor/models/gpt_oss.py`, `vllm/v1/spec_decode/eagle.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24920 - [CI] GPT-OSS GPQA eval test for Blackwell

- Link: https://github.com/vllm-project/vllm/pull/24920
- Status/date: merged / 2025-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gpt_oss/__init__.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/test_gpqa_correctness.py`; associated commits `493b10f8bf38`
- Diff scope read: GitHub Pull Request files API returned 4 files, +136/-0, 147 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] GPT-OSS GPQA eval test for Blackwell"; model line: GPT-OSS; category: docs/tests/CI; main diff: `tests/evals/gpt_oss/test_gpqa_correctness.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/__init__.py`; technical summary: Covers "[CI] GPT-OSS GPQA eval test for Blackwell"; the main implementation surface is `tests/evals/gpt_oss/test_gpqa_correctness.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/__init__.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gpt_oss/test_gpqa_correctness.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: run_gpqa_eval, test_gpqa_correctness, touching `run_gpqa_eval, test_gpqa_correctness`; `tests/evals/gpt_oss/conftest.py` added +18/-0 (18 lines); hunks: -0,0 +1,18; symbols: pytest_addoption, touching `pytest_addoption`; `tests/evals/gpt_oss/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2.
- Code diff details:
  - `tests/evals/gpt_oss/test_gpqa_correctness.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: run_gpqa_eval, test_gpqa_correctness
  - `tests/evals/gpt_oss/conftest.py` added +18/-0 (18 lines); hunks: -0,0 +1,18; symbols: pytest_addoption
  - `tests/evals/gpt_oss/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- Key code excerpts:

```diff
diff -- tests/evals/gpt_oss/test_gpqa_correctness.py
@@ -0,0 +1,102 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""
+GPQA evaluation using vLLM server and GPT-OSS evaluation package.
+Usage:
+pytest -s -v tests/evals/gpt_oss/test_gpqa_correctness.py \
diff -- tests/evals/gpt_oss/conftest.py
@@ -0,0 +1,18 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""
+Pytest configuration for GPT-OSS evaluation tests.
+"""
+def pytest_addoption(parser):
diff -- tests/evals/gpt_oss/__init__.py
@@ -0,0 +1,2 @@
```

- Reviewed files:
  - tests: `tests/evals/gpt_oss/test_gpqa_correctness.py` added +102/-0; `tests/evals/gpt_oss/conftest.py` added +18/-0; `tests/evals/gpt_oss/__init__.py` added +2/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gpt_oss/__init__.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/test_gpqa_correctness.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #23815 - [Model] [gpt-oss] fix gpt-oss pp support

- Link: https://github.com/vllm-project/vllm/pull/23815
- Status/date: merged / 2025-08-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `bfab219648fd`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-3, 12 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] [gpt-oss] fix gpt-oss pp support"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Model] [gpt-oss] fix gpt-oss pp support"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +2/-3 (5 lines); hunks: -668,9 +668,8 @@ def forward(self,; symbols: forward, compute_logits, touching `forward, compute_logits`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +2/-3 (5 lines); hunks: -668,9 +668,8 @@ def forward(self,; symbols: forward, compute_logits
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -668,9 +668,8 @@ def forward(self,
-        assert intermediate_tensors is None
-        assert inputs_embeds is None
-        return self.model(input_ids, positions)
+        return self.model(input_ids, positions, intermediate_tensors,
+                          inputs_embeds)
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +2/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23680 - [Model] Add PP support and VLM backbone compatability for GPT-OSS

- Link: https://github.com/vllm-project/vllm/pull/23680
- Status/date: merged / 2025-08-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `c5d004aaaf3b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +87/-34, 232 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Add PP support and VLM backbone compatability for GPT-OSS"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Model] Add PP support and VLM backbone compatability for GPT-OSS"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +86/-33 (119 lines); hunks: -11,7 +11,8; -27,7 +28,10; symbols: __init__, forward, MLPBlock, touching `__init__, forward, MLPBlock`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +86/-33 (119 lines); hunks: -11,7 +11,8; -27,7 +28,10; symbols: __init__, forward, MLPBlock
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -11,7 +11,8 @@
-from vllm.distributed import (get_ep_group, get_tensor_model_parallel_rank,
+from vllm.distributed import (get_ep_group, get_pp_group,
+                              get_tensor_model_parallel_rank,
@@ -27,7 +28,10 @@
+from .interfaces import SupportsPP
+                    is_pp_missing_parameter,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +86/-33
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23613 - [Bugfix][gpt-oss] passing the cache config in gpt-oss

- Link: https://github.com/vllm-project/vllm/pull/23613
- Status/date: merged / 2025-08-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `fecbb7c78298`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-1, 33 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][gpt-oss] passing the cache config in gpt-oss"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Bugfix][gpt-oss] passing the cache config in gpt-oss"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +6/-1 (7 lines); hunks: -174,12 +174,15 @@ class TransformerBlock(torch.nn.Module):; -203,6 +206,7 @@ def __init__(; symbols: TransformerBlock, __init__, touching `TransformerBlock, __init__`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +6/-1 (7 lines); hunks: -174,12 +174,15 @@ class TransformerBlock(torch.nn.Module):; -203,6 +206,7 @@ def __init__(; symbols: TransformerBlock, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -174,12 +174,15 @@ class TransformerBlock(torch.nn.Module):
+        cache_config: CacheConfig,
-        self.attn = OAIAttention(config, prefix=f"{prefix}.attn")
+        self.attn = OAIAttention(config,
+                                 prefix=f"{prefix}.attn",
+                                 cache_config=cache_config)
@@ -203,6 +206,7 @@ def __init__(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +6/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22951 - [Kernel] Add cuda kernel for gpt_oss activation

- Link: https://github.com/vllm-project/vllm/pull/22951
- Status/date: merged / 2025-08-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `4d4061b6e73d`
- Diff scope read: GitHub Pull Request files API returned 9 files, +157/-42, 330 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Add cuda kernel for gpt_oss activation"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Kernel] Add cuda kernel for gpt_oss activation"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -159,7 +159,7 @@ def __init__(
-                                activation="swiglu_oai")
+                                activation="swigluoai")
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/core/test_activation.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22948 - Revert "[Kernel] Add cuda kernel for gpt_oss activation"

- Link: https://github.com/vllm-project/vllm/pull/22948
- Status/date: merged / 2025-08-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `f1f0d2fab8a1`
- Diff scope read: GitHub Pull Request files API returned 8 files, +24/-150, 290 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Revert "[Kernel] Add cuda kernel for gpt_oss activation""; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Revert "[Kernel] Add cuda kernel for gpt_oss activation""; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -159,7 +159,7 @@ def __init__(
-                                activation="swigluoai")
+                                activation="swiglu_oai")
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/core/test_activation.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22538 - [Kernel] Add cuda kernel for gpt_oss activation

- Link: https://github.com/vllm-project/vllm/pull/22538
- Status/date: merged / 2025-08-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `81f4b9648117`
- Diff scope read: GitHub Pull Request files API returned 8 files, +150/-24, 290 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Add cuda kernel for gpt_oss activation"; model line: GPT-OSS; category: performance/backend optimization; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[Kernel] Add cuda kernel for gpt_oss activation"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -159,7 +159,7 @@ def __init__(
-                                activation="swiglu_oai")
+                                activation="swigluoai")
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/core/test_activation.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22678 - Force TRTLLM attention for gpt-oss on SM100

- Link: https://github.com/vllm-project/vllm/pull/22678
- Status/date: merged / 2025-08-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `c6b928798e96`
- Diff scope read: GitHub Pull Request files API returned 4 files, +20/-9, 96 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Force TRTLLM attention for gpt-oss on SM100"; model line: GPT-OSS; category: model implementation change; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Force TRTLLM attention for gpt-oss on SM100"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +1/-4 (5 lines); hunks: -8,7 +8,6; -70,11 +69,9 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-4 (5 lines); hunks: -8,7 +8,6; -70,11 +69,9 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -8,7 +8,6 @@
-from vllm import envs
@@ -70,11 +69,9 @@ def __init__(
-        attention_sink_dtype = (torch.float32 if envs.VLLM_USE_TRTLLM_ATTENTION
-                                else torch.bfloat16)
-                        dtype=attention_sink_dtype,
+                        dtype=torch.bfloat16,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-4
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`, `vllm/utils/flashinfer.py`, `vllm/v1/attention/backends/flashinfer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22508 - [oss] Init gpt-oss bf16 support

- Link: https://github.com/vllm-project/vllm/pull/22508
- Status/date: merged / 2025-08-10
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `0c5254b82acc`
- Diff scope read: GitHub Pull Request files API returned 4 files, +342/-125, 726 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[oss] Init gpt-oss bf16 support"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[oss] Init gpt-oss bf16 support"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +149/-3 (152 lines); hunks: -160,7 +160,9 @@ def __init__(; -262,8 +264,8 @@ def compute_logits(self, hidden_states: torch.Tensor,; symbols: __init__, forward, compute_logits, load_weights, touching `__init__, forward, compute_logits`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +149/-3 (152 lines); hunks: -160,7 +160,9 @@ def __init__(; -262,8 +264,8 @@ def compute_logits(self, hidden_states: torch.Tensor,; symbols: __init__, forward, compute_logits, load_weights
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -160,7 +160,9 @@ def __init__(
-                                apply_router_weight_on_input=False)
+                                apply_router_weight_on_input=False,
+                                has_bias=True,
+                                activation="swiglu_oai")
@@ -262,8 +264,8 @@ def compute_logits(self, hidden_states: torch.Tensor,
-    def load_weights(self, weights: Iterable[tuple[str,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +149/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22421 - [gpt-oss] triton kernel mxfp4

- Link: https://github.com/vllm-project/vllm/pull/22421
- Status/date: merged / 2025-08-08
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; associated commits `e789cad6b8b5`
- Diff scope read: GitHub Pull Request files API returned 8 files, +755/-9, 859 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[gpt-oss] triton kernel mxfp4"; model line: GPT-OSS; category: performance/backend optimization; main diff: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; technical summary: Covers "[gpt-oss] triton kernel mxfp4"; the main implementation surface is `tests/kernels/moe/test_gpt_oss_triton_kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` added +375/-0 (375 lines); hunks: -0,0 +1,375; symbols: deshuffle, init_compute_data, ModelConfig, swiglu, touching `deshuffle, init_compute_data, ModelConfig`.
- Code diff details:
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` added +375/-0 (375 lines); hunks: -0,0 +1,375; symbols: deshuffle, init_compute_data, ModelConfig, swiglu
- Key code excerpts:

```diff
diff -- tests/kernels/moe/test_gpt_oss_triton_kernels.py
@@ -0,0 +1,375 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from dataclasses import dataclass, fields
+import pytest
+import torch
+import torch.nn.functional as F
```

- Reviewed files:
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` added +375/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22401 - [gpt-oss] fix model config with hf_config

- Link: https://github.com/vllm-project/vllm/pull/22401
- Status/date: merged / 2025-08-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `5c7cc33f4daf`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-3, 21 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[gpt-oss] fix model config with hf_config"; model line: GPT-OSS; category: bug fix; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "[gpt-oss] fix model config with hf_config"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` modified +3/-3 (6 lines); hunks: -61,9 +61,9 @@ def __init__(; -154,7 +154,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` modified +3/-3 (6 lines); hunks: -61,9 +61,9 @@ def __init__(; -154,7 +154,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -61,9 +61,9 @@ def __init__(
-                config.rope_ntk_beta,
+                config.rope_scaling["beta_fast"],
-                config.rope_ntk_alpha,
+                config.rope_scaling["beta_slow"],
@@ -154,7 +154,7 @@ def __init__(
-                                top_k=config.num_experts_per_token,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +3/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/gpt_oss.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22327 - Add GPT-OSS model code and config [1/N]

- Link: https://github.com/vllm-project/vllm/pull/22327
- Status/date: merged / 2025-08-06
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/gpt_oss.py`; associated commits `de98252f497b`
- Diff scope read: GitHub Pull Request files API returned 4 files, +503/-0, 530 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add GPT-OSS model code and config [1/N]"; model line: GPT-OSS; category: model support/runtime entry; main diff: `vllm/model_executor/models/gpt_oss.py`; technical summary: Covers "Add GPT-OSS model code and config [1/N]"; the main implementation surface is `vllm/model_executor/models/gpt_oss.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/gpt_oss.py` added +472/-0 (472 lines); hunks: -0,0 +1,472; symbols: OAIAttention, __init__, forward, MLPBlock, touching `OAIAttention, __init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/gpt_oss.py` added +472/-0 (472 lines); hunks: -0,0 +1,472; symbols: OAIAttention, __init__, forward, MLPBlock
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -0,0 +1,472 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Iterable
+from typing import Optional
+import torch
+import torch.distributed as dist
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/gpt_oss.py` added +472/-0
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
