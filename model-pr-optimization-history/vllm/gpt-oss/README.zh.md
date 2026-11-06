# vllm GPT-OSS 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `tests/evals/gpt_oss/README.md` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/__init__.py` | [#24920](https://github.com/vllm-project/vllm/pull/24920) |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-baseline.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-bf16-cutlass.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-bf16-trtllm.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-humming-mxfp4-mxfp8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-marlin.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` | [#36179](https://github.com/vllm-project/vllm/pull/36179) |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-quark-mxfp4-bf16-aiter.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-quark-mxfp4-bf16-triton.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-quark-mxfp4-fp8-triton.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-sm120.yaml` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` | [#48703](https://github.com/vllm-project/vllm/pull/48703) |
| `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` | [#48703](https://github.com/vllm-project/vllm/pull/48703) |
| `tests/evals/gpt_oss/configs/models-b200.txt` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/models-gfx942.txt` | [#36179](https://github.com/vllm-project/vllm/pull/36179) |
| `tests/evals/gpt_oss/configs/models-gfx950.txt` | [#36179](https://github.com/vllm-project/vllm/pull/36179), [#38292](https://github.com/vllm-project/vllm/pull/38292) |
| `tests/evals/gpt_oss/configs/models-h100.txt` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/models-spark.txt` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/configs/models-xpu.txt` | [#48703](https://github.com/vllm-project/vllm/pull/48703) |
| `tests/evals/gpt_oss/conftest.py` | [#24920](https://github.com/vllm-project/vllm/pull/24920) |
| `tests/evals/gpt_oss/run_gpqa_eval.py` | 无直接 PR 号提交 |
| `tests/evals/gpt_oss/test_gpqa_correctness.py` | [#24920](https://github.com/vllm-project/vllm/pull/24920), [#26030](https://github.com/vllm-project/vllm/pull/26030) |
| `tests/evals/gsm8k/configs/humming/gpt-oss-20b-humming-act-fp8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/gpt-oss-20b-humming.yaml` | 无直接 PR 号提交 |
| `tests/kernels/moe/test_gpt_oss_triton_kernels.py` | [#22421](https://github.com/vllm-project/vllm/pull/22421), [#29008](https://github.com/vllm-project/vllm/pull/29008), [#37683](https://github.com/vllm-project/vllm/pull/37683), [#39007](https://github.com/vllm-project/vllm/pull/39007), [#45457](https://github.com/vllm-project/vllm/pull/45457), [#55934](https://github.com/vllm-project/vllm/pull/55934) |
| `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` | [#52209](https://github.com/vllm-project/vllm/pull/52209) |
| `tests/models/quantization/test_gpt_oss.py` | [#29008](https://github.com/vllm-project/vllm/pull/29008), [#35806](https://github.com/vllm-project/vllm/pull/35806), [#35887](https://github.com/vllm-project/vllm/pull/35887), [#36174](https://github.com/vllm-project/vllm/pull/36174), [#43571](https://github.com/vllm-project/vllm/pull/43571) |
| `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` | [#39007](https://github.com/vllm-project/vllm/pull/39007), [#43135](https://github.com/vllm-project/vllm/pull/43135), [#45457](https://github.com/vllm-project/vllm/pull/45457), [#55934](https://github.com/vllm-project/vllm/pull/55934) |
| `vllm/model_executor/models/gpt_oss.py` | [#22327](https://github.com/vllm-project/vllm/pull/22327), [#22401](https://github.com/vllm-project/vllm/pull/22401), [#22508](https://github.com/vllm-project/vllm/pull/22508), [#22538](https://github.com/vllm-project/vllm/pull/22538), [#22678](https://github.com/vllm-project/vllm/pull/22678), [#22948](https://github.com/vllm-project/vllm/pull/22948), [#22951](https://github.com/vllm-project/vllm/pull/22951), [#23613](https://github.com/vllm-project/vllm/pull/23613), [#23680](https://github.com/vllm-project/vllm/pull/23680), [#23815](https://github.com/vllm-project/vllm/pull/23815), [#24032](https://github.com/vllm-project/vllm/pull/24032), [#25246](https://github.com/vllm-project/vllm/pull/25246), ... (30 total) |

## PR 覆盖总览

- git 追溯 PR 数: 45
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 45

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #61257 - [Model Runner V2] Enable batch-sharded sampling for GPT-OSS

- 链接: https://github.com/vllm-project/vllm/pull/61257
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `2c74fd1873e3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+118/-37，可读 patch 215 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model Runner V2] Enable batch-sharded sampling for GPT-OSS」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Model Runner V2] Enable batch-sharded sampling for GPT-OSS」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -1482,6 +1482,9 @@ def compute_logits(self, hidden_states: torch.Tensor) -> t...; symbols: compute_logits, compute_logits_local, load_weights，涉及 `compute_logits, compute_logits_local, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +3/-0 (3 lines); hunks: -1482,6 +1482,9 @@ def compute_logits(self, hidden_states: torch.Tensor) -> t...; symbols: compute_logits, compute_logits_local, load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -1482,6 +1482,9 @@ def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
+    def compute_logits_local(self, hidden_states: torch.Tensor) -> torch.Tensor:
+        return self.logits_processor(self.lm_head, hidden_states, skip_gather=True)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/v1/e2e/general/test_sharded_sampling.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55934 - [ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4)

- 链接: https://github.com/vllm-project/vllm/pull/55934
- 状态/时间: merged / 2026-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`；关联提交 `3e267bae70d8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+270/-147，可读 patch 718 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4)」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；技术摘要: 覆盖「[ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4)」；主要实现面是 `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +176/-38 (214 lines); hunks: -26,7 +26,7; -441,48 +441,59 @@ def _sort_tokens_pow2(expt_scal, expt_indx, n_expts_tot, b...; symbols: _sort_tokens_pow2, RoutingData, __init__, pack_bitmatrix，涉及 `_sort_tokens_pow2, RoutingData, __init__`；`tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-2 (3 lines); hunks: -384,9 +384,8 @@ def test_routing_data_from_sparse_topk_parity(n_tokens, n_ex...; symbols: test_routing_data_from_sparse_topk_parity，涉及 `test_routing_data_from_sparse_topk_parity`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +176/-38 (214 lines); hunks: -26,7 +26,7; -441,48 +441,59 @@ def _sort_tokens_pow2(expt_scal, expt_indx, n_expts_tot, b...; symbols: _sort_tokens_pow2, RoutingData, __init__, pack_bitmatrix
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-2 (3 lines); hunks: -384,9 +384,8 @@ def test_routing_data_from_sparse_topk_parity(n_tokens, n_ex...; symbols: test_routing_data_from_sparse_topk_parity
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +176/-38
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-2
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45457 - [Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward

- 链接: https://github.com/vllm-project/vllm/pull/45457
- 状态/时间: merged / 2026-08-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`；关联提交 `129087ddab2b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+102/-15，可读 patch 158 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；技术摘要: 覆盖「[Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward」；主要实现面是 `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +45/-14 (59 lines); hunks: -578,13 +578,14 @@ def triton_kernel_moe_forward(; -597,11 +598,23 @@ def triton_kernel_moe_forward(; symbols: triton_kernel_moe_forward, make_routing_data, routing_data_from_sparse_topk，涉及 `triton_kernel_moe_forward, make_routing_data, routing_data_from_sparse_topk`；`tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +57/-1 (58 lines); hunks: -1,6 +1,6; -371,3 +371,59 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_routing_data_from_sparse_topk_parity, assert_equivalent，涉及 `test_unit_shuffle, test_routing_data_from_sparse_topk_parity, assert_equivalent`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +45/-14 (59 lines); hunks: -578,13 +578,14 @@ def triton_kernel_moe_forward(; -597,11 +598,23 @@ def triton_kernel_moe_forward(; symbols: triton_kernel_moe_forward, make_routing_data, routing_data_from_sparse_topk
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +57/-1 (58 lines); hunks: -1,6 +1,6; -371,3 +371,59 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_routing_data_from_sparse_topk_parity, assert_equivalent
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +45/-14
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +57/-1
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #52209 - Add routed expert loading for gpt-oss

- 链接: https://github.com/vllm-project/vllm/pull/52209
- 状态/时间: merged / 2026-08-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`, `vllm/model_executor/models/gpt_oss.py`；关联提交 `b26039b09fc9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+370/-3，可读 patch 446 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add routed expert loading for gpt-oss」；模型线: GPT-OSS；类别: 文档/测试/CI；主要 diff: `vllm/model_executor/models/gpt_oss.py`, `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`；技术摘要: 覆盖「Add routed expert loading for gpt-oss」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`, `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +197/-0 (197 lines); hunks: -25,6 +25,7; -68,6 +69,15; symbols: OAIAttention, forward, GptOssRoutedExperts, _narrow_for_rank，涉及 `OAIAttention, forward, GptOssRoutedExperts`；`tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: _TestExperts, __init__, _map_global_expert_id_to_local_expert_id, _load，涉及 `_TestExperts, __init__, _map_global_expert_id_to_local_expert_id`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +197/-0 (197 lines); hunks: -25,6 +25,7; -68,6 +69,15; symbols: OAIAttention, forward, GptOssRoutedExperts, _narrow_for_rank
  - `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` added +152/-0 (152 lines); hunks: -0,0 +1,152; symbols: _TestExperts, __init__, _map_global_expert_id_to_local_expert_id, _load
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +197/-0
  - tests: `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py` added +152/-0
- 验证与风险: diff 自带测试面 `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`, `tests/model_executor/model_loader/test_reload.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #48703 - [XPU] [UT] [CI] add xpu config to run gpt-oss accuracy in ut and ci

- 链接: https://github.com/vllm-project/vllm/pull/48703
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`；关联提交 `7de49bab7e91`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+38/-0，可读 patch 48 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU] [UT] [CI] add xpu config to run gpt-oss accuracy in ut and ci」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`；技术摘要: 覆盖「[XPU] [UT] [CI] add xpu config to run gpt-oss accuracy in ut and ci」；主要实现面是 `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6；`tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` added +5/-0 (5 lines); hunks: -0,0 +1,5；`tests/evals/gpt_oss/configs/models-xpu.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3。
- 代码 diff 细节:
  - `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` added +5/-0 (5 lines); hunks: -0,0 +1,5
  - `tests/evals/gpt_oss/configs/models-xpu.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml` added +6/-0; `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml` added +5/-0; `tests/evals/gpt_oss/configs/models-xpu.txt` added +3/-0
- 验证与风险: diff 自带测试面 `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45818 - [Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r…

- 链接: https://github.com/vllm-project/vllm/pull/45818
- 状态/时间: merged / 2026-06-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `f4d5f73ffa40`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r…」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r…」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -979,7 +979,11 @@ def _load_weights_other(; symbols: _load_weights_other，涉及 `_load_weights_other`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +5/-1 (6 lines); hunks: -979,7 +979,11 @@ def _load_weights_other(; symbols: _load_weights_other
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46441 - fix gpt_oss pp>1 with ep

- 链接: https://github.com/vllm-project/vllm/pull/46441
- 状态/时间: merged / 2026-06-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `901a3b091cf1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix gpt_oss pp>1 with ep」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「fix gpt_oss pp>1 with ep」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1078,7 +1078,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -1078,7 +1078,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -1078,7 +1078,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-        ep_rank = get_ep_group().rank
+        ep_rank = get_ep_group().rank_in_group
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #45067 - [Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor

- 链接: https://github.com/vllm-project/vllm/pull/45067
- 状态/时间: merged / 2026-06-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `7920ccb97c2d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-0，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +7/-0 (7 lines); hunks: -635,6 +635,13 @@ def _get_moe_weight_dtype(layer_id: int = 0) -> str | None:; symbols: _get_moe_weight_dtype，涉及 `_get_moe_weight_dtype`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +7/-0 (7 lines); hunks: -635,6 +635,13 @@ def _get_moe_weight_dtype(layer_id: int = 0) -> str | None:; symbols: _get_moe_weight_dtype
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #43571 - [BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py

- 链接: https://github.com/vllm-project/vllm/pull/43571
- 状态/时间: merged / 2026-05-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_gpt_oss.py`；关联提交 `e9499996df89`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-1，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `tests/models/quantization/test_gpt_oss.py`；技术摘要: 覆盖「[BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py」；主要实现面是 `tests/models/quantization/test_gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -22,7 +22,14; symbols: on_gfx950，涉及 `on_gfx950`。
- 代码 diff 细节:
  - `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -22,7 +22,14; symbols: on_gfx950
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +8/-1
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_gpt_oss.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43135 - [Perf][gpt-oss] Downgrade triton_kernels to v3.5.1

- 链接: https://github.com/vllm-project/vllm/pull/43135
- 状态/时间: merged / 2026-05-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`；关联提交 `5774aad9c5b6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+73/-57，可读 patch 204 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][gpt-oss] Downgrade triton_kernels to v3.5.1」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`；技术摘要: 覆盖「[Perf][gpt-oss] Downgrade triton_kernels to v3.5.1」；主要实现面是 `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +57/-32 (89 lines); hunks: -209,6 +209,16 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitmat...; -233,11 +243,10 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitma...; symbols: _make_bitmatrix_metadata_pow2_safe, triton_kernel_moe_forward，涉及 `_make_bitmatrix_metadata_pow2_safe, triton_kernel_moe_forward`。
- 代码 diff 细节:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +57/-32 (89 lines); hunks: -209,6 +209,16 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitmat...; -233,11 +243,10 @@ def _make_bitmatrix_metadata_pow2_safe(nonzero_indx, bitma...; symbols: _make_bitmatrix_metadata_pow2_safe, triton_kernel_moe_forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` modified +57/-32
- 验证与风险: diff 自带测试面 `tests/kernels/quantization/test_mxfp4_triton_ep.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39007 - [MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/

- 链接: https://github.com/vllm-project/vllm/pull/39007
- 状态/时间: merged / 2026-04-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`；关联提交 `1a9353bb02e6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+16/-12，可读 patch 100 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；技术摘要: 覆盖「[MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/」；主要实现面是 `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` renamed +0/-0 (0 lines)；`tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-1 (2 lines); hunks: -25,7 +25,7。
- 代码 diff 细节:
  - `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` renamed +0/-0 (0 lines)
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-1 (2 lines); hunks: -25,7 +25,7
- 关键代码摘录:

```diff
diff -- tests/kernels/moe/test_gpt_oss_triton_kernels.py
@@ -25,7 +25,7 @@
-from vllm.model_executor.layers.fused_moe.gpt_oss_triton_kernels_moe import (
+from vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe import (
```

- 已读文件:
  - runtime: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` renamed +0/-0
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/kernels/moe/test_modular_oai_triton_moe.py`, `tests/kernels/quantization/test_mxfp4_triton_ep.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38292 - [CI][ROCm] Add gpt-oss w4a8 in CI

- 链接: https://github.com/vllm-project/vllm/pull/38292
- 状态/时间: merged / 2026-04-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gpt_oss/configs/models-gfx950.txt`；关联提交 `82a006beebf0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+10/-1，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][ROCm] Add gpt-oss w4a8 in CI」；模型线: GPT-OSS；类别: 文档/测试/CI；主要 diff: `tests/evals/gpt_oss/configs/models-gfx950.txt`；技术摘要: 覆盖「[CI][ROCm] Add gpt-oss w4a8 in CI」；主要实现面是 `tests/evals/gpt_oss/configs/models-gfx950.txt`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gpt_oss/configs/models-gfx950.txt` modified +2/-1 (3 lines); hunks: -1,3 +1,4。
- 代码 diff 细节:
  - `tests/evals/gpt_oss/configs/models-gfx950.txt` modified +2/-1 (3 lines); hunks: -1,3 +1,4
- 关键代码摘录:

```diff
diff -- tests/evals/gpt_oss/configs/models-gfx950.txt
@@ -1,3 +1,4 @@
-gpt-oss-20b-rocm-baseline.yaml
+gpt-oss-20b-rocm-baseline.yaml
+gpt-oss-20b-rocm-mxfp4-fp8.yaml
```

- 已读文件:
  - tests: `tests/evals/gpt_oss/configs/models-gfx950.txt` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-mxfp4-fp8.yaml`, `tests/evals/gpt_oss/configs/models-gfx950.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38778 - Revert "[Kernel] Add gpt-oss Router GEMM kernel (#37205)"

- 链接: https://github.com/vllm-project/vllm/pull/38778
- 状态/时间: merged / 2026-04-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `9bd723110689`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+12/-875，可读 patch 1027 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[Kernel] Add gpt-oss Router GEMM kernel (#37205)"」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Revert "[Kernel] Add gpt-oss Router GEMM kernel (#37205)"」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -20,11 +20,12; -174,11 +175,13 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +6/-3 (9 lines); hunks: -20,11 +20,12; -174,11 +175,13 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +6/-3
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_router_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37683 - [Perf] Eliminate redundant SparseMatrix creation in gpt_oss_triton_kernels

- 链接: https://github.com/vllm-project/vllm/pull/37683
- 状态/时间: merged / 2026-03-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；关联提交 `d0532bf38da5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+73/-4，可读 patch 108 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Eliminate redundant SparseMatrix creation in gpt_oss_triton_kernels」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；技术摘要: 覆盖「[Perf] Eliminate redundant SparseMatrix creation in gpt_oss_triton_kernels」；主要实现面是 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +44/-0 (44 lines); hunks: -21,12 +21,16; -355,3 +359,43 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_legacy_routing，涉及 `test_unit_shuffle, test_legacy_routing`。
- 代码 diff 细节:
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +44/-0 (44 lines); hunks: -21,12 +21,16; -355,3 +359,43 @@ def test_unit_shuffle():; symbols: test_unit_shuffle, test_legacy_routing
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +44/-0
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37205 - [Kernel] Add gpt-oss Router GEMM kernel

- 链接: https://github.com/vllm-project/vllm/pull/37205
- 状态/时间: merged / 2026-03-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `9bd723110689`, `b1169d7be8ad`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+875/-13，可读 patch 1035 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Add gpt-oss Router GEMM kernel」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Kernel] Add gpt-oss Router GEMM kernel」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +3/-7 (10 lines); hunks: -20,12 +20,11; -175,13 +174,11 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +3/-7 (10 lines); hunks: -20,12 +20,11; -175,13 +174,11 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +3/-7
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_router_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36179 - [ROCm][CI] Fix ROCm GPT-OSS Eval test group

- 链接: https://github.com/vllm-project/vllm/pull/36179
- 状态/时间: merged / 2026-03-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`；关联提交 `179547d62c73`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+16/-4，可读 patch 40 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Fix ROCm GPT-OSS Eval test group」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`；技术摘要: 覆盖「[ROCm][CI] Fix ROCm GPT-OSS Eval test group」；主要实现面是 `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6；`tests/evals/gpt_oss/configs/models-gfx942.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3；`tests/evals/gpt_oss/configs/models-gfx950.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3。
- 代码 diff 细节:
  - `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` added +6/-0 (6 lines); hunks: -0,0 +1,6
  - `tests/evals/gpt_oss/configs/models-gfx942.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3
  - `tests/evals/gpt_oss/configs/models-gfx950.txt` added +3/-0 (3 lines); hunks: -0,0 +1,3
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml` added +6/-0; `tests/evals/gpt_oss/configs/models-gfx942.txt` added +3/-0; `tests/evals/gpt_oss/configs/models-gfx950.txt` added +3/-0
- 验证与风险: diff 自带测试面 `tests/evals/gpt_oss/configs/gpt-oss-20b-rocm-baseline.yaml`, `tests/evals/gpt_oss/configs/models-gfx942.txt`, `tests/evals/gpt_oss/configs/models-gfx950.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36174 - [ROCm][CI] Enable AITER for failing `test_gpt_oss` test case on MI355

- 链接: https://github.com/vllm-project/vllm/pull/36174
- 状态/时间: merged / 2026-03-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_gpt_oss.py`；关联提交 `fc4657756ff0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-1，可读 patch 27 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Enable AITER for failing `test_gpt_oss` test case on MI355」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `tests/models/quantization/test_gpt_oss.py`；技术摘要: 覆盖「[ROCm][CI] Enable AITER for failing `test_gpt_oss` test case on MI355」；主要实现面是 `tests/models/quantization/test_gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -21,6 +21,7; -83,11 +84,17 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization，涉及 `get_model_args, test_gpt_oss_attention_quantization`。
- 代码 diff 细节:
  - `tests/models/quantization/test_gpt_oss.py` modified +8/-1 (9 lines); hunks: -21,6 +21,7; -83,11 +84,17 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +8/-1
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_gpt_oss.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35887 - [ROCm][CI] Fix TP size issue for `test_gpt_oss`

- 链接: https://github.com/vllm-project/vllm/pull/35887
- 状态/时间: merged / 2026-03-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_gpt_oss.py`；关联提交 `e7213003cbf6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-0，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Fix TP size issue for `test_gpt_oss`」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `tests/models/quantization/test_gpt_oss.py`；技术摘要: 覆盖「[ROCm][CI] Fix TP size issue for `test_gpt_oss`」；主要实现面是 `tests/models/quantization/test_gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_gpt_oss.py` modified +5/-0 (5 lines); hunks: -21,6 +21,8; -83,6 +85,9 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization，涉及 `get_model_args, test_gpt_oss_attention_quantization`。
- 代码 diff 细节:
  - `tests/models/quantization/test_gpt_oss.py` modified +5/-0 (5 lines); hunks: -21,6 +21,8; -83,6 +85,9 @@ def get_model_args(self, tp_size: int):; symbols: get_model_args, test_gpt_oss_attention_quantization
- 关键代码摘录:

```diff
diff -- tests/models/quantization/test_gpt_oss.py
@@ -21,6 +21,8 @@
+from vllm.utils.torch_utils import cuda_device_count_stateless
@@ -83,6 +85,9 @@ def get_model_args(self, tp_size: int):
+    if tp_size > cuda_device_count_stateless():
+        pytest.skip("Not enough GPUs to run this test case")
```

- 已读文件:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +5/-0
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_gpt_oss.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35806 - [ROCm][CI] Fix Assertion Logic For `test_gpt_oss`

- 链接: https://github.com/vllm-project/vllm/pull/35806
- 状态/时间: merged / 2026-03-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/quantization/test_gpt_oss.py`；关联提交 `8b9e8b74541e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-5，可读 patch 22 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Fix Assertion Logic For `test_gpt_oss`」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `tests/models/quantization/test_gpt_oss.py`；技术摘要: 覆盖「[ROCm][CI] Fix Assertion Logic For `test_gpt_oss`」；主要实现面是 `tests/models/quantization/test_gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/quantization/test_gpt_oss.py` modified +5/-5 (10 lines); hunks: -12,8 +12,8; -104,7 +104,7 @@ def test_gpt_oss_attention_quantization(; symbols: test_gpt_oss_attention_quantization，涉及 `test_gpt_oss_attention_quantization`。
- 代码 diff 细节:
  - `tests/models/quantization/test_gpt_oss.py` modified +5/-5 (10 lines); hunks: -12,8 +12,8; -104,7 +104,7 @@ def test_gpt_oss_attention_quantization(; symbols: test_gpt_oss_attention_quantization
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/models/quantization/test_gpt_oss.py` modified +5/-5
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_gpt_oss.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35404 - [Bugfix][Model] Fix gpt-oss batch invariance

- 链接: https://github.com/vllm-project/vllm/pull/35404
- 状态/时间: merged / 2026-02-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `1f3dbd95fd13`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+14/-8，可读 patch 50 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] Fix gpt-oss batch invariance」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Bugfix][Model] Fix gpt-oss batch invariance」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +13/-2 (15 lines); hunks: -23,7 +23,11; -165,7 +169,14 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +13/-2 (15 lines); hunks: -23,7 +23,11; -165,7 +169,14 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +13/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34337 - [GPT-OSS] Remove unnecessary contiguous

- 链接: https://github.com/vllm-project/vllm/pull/34337
- 状态/时间: merged / 2026-02-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `83e26c834ef1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-1，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GPT-OSS] Remove unnecessary contiguous」；模型线: GPT-OSS；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[GPT-OSS] Remove unnecessary contiguous」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +0/-1 (1 lines); hunks: -140,7 +140,6 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +0/-1 (1 lines); hunks: -140,7 +140,6 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -140,7 +140,6 @@ def forward(
-        v = v.contiguous()
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +0/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #29008 - [ROCm][Quantization] GPT_OSS in amd-quark format model loading and emulations

- 链接: https://github.com/vllm-project/vllm/pull/29008
- 状态/时间: merged / 2026-02-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/quantization/test_gpt_oss.py`, `vllm/model_executor/models/gpt_oss.py`；关联提交 `b129136c7a73`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+1094/-213，可读 patch 1860 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Quantization] GPT_OSS in amd-quark format model loading and emulations」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/gpt_oss.py`, `tests/models/quantization/test_gpt_oss.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；技术摘要: 覆盖「[ROCm][Quantization] GPT_OSS in amd-quark format model loading and emulations」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`, `tests/models/quantization/test_gpt_oss.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +491/-18 (509 lines); hunks: -1,6 +1,7; -25,13 +26,17; symbols: __init__, forward, get_expert_mapping, _load_weights_mxfp4，涉及 `__init__, forward, get_expert_mapping`；`tests/models/quantization/test_gpt_oss.py` added +110/-0 (110 lines); hunks: -0,0 +1,110; symbols: has_huggingface_access, ModelCase, EvaluationConfig, get_model_args，涉及 `has_huggingface_access, ModelCase, EvaluationConfig`；`tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +13/-7 (20 lines); hunks: -22,7 +22,7; -298,12 +298,18 @@ def test_equiv(num_token, a_dtype, w_dtype, tp, workspace_...; symbols: test_equiv，涉及 `test_equiv`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +491/-18 (509 lines); hunks: -1,6 +1,7; -25,13 +26,17; symbols: __init__, forward, get_expert_mapping, _load_weights_mxfp4
  - `tests/models/quantization/test_gpt_oss.py` added +110/-0 (110 lines); hunks: -0,0 +1,110; symbols: has_huggingface_access, ModelCase, EvaluationConfig, get_model_args
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +13/-7 (20 lines); hunks: -22,7 +22,7; -298,12 +298,18 @@ def test_equiv(num_token, a_dtype, w_dtype, tp, workspace_...; symbols: test_equiv
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +491/-18
  - tests: `tests/models/quantization/test_gpt_oss.py` added +110/-0; `tests/kernels/moe/test_gpt_oss_triton_kernels.py` modified +13/-7
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/quantization/test_gpt_oss.py`, `tests/models/quantization/test_gpt_oss_attn_quantization.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30976 - Use aiter triton fused_add_rmsnorm_pad for gpt-oss

- 链接: https://github.com/vllm-project/vllm/pull/30976
- 状态/时间: merged / 2026-01-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `59bcc5b6f2e6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+327/-11，可读 patch 489 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Use aiter triton fused_add_rmsnorm_pad for gpt-oss」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Use aiter triton fused_add_rmsnorm_pad for gpt-oss」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -187,7 +187,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -187,7 +187,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -187,7 +187,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:
-        x = self.experts(hidden_states=x, router_logits=g)
+        x = self.experts(hidden_states=x, router_logits=g)[:, : self.hidden_size]
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/compile/test_fuse_act_padding.py`, `tests/compile/test_fusion.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29506 - Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights

- 链接: https://github.com/vllm-project/vllm/pull/29506
- 状态/时间: merged / 2025-11-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `5f5521bd5d7d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -647,8 +647,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -647,8 +647,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -647,8 +647,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-                ep_rank_start,
+                ep_rank_start,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28244 - Add truncate arg to yarn to match openai implementation of gpt-oss

- 链接: https://github.com/vllm-project/vllm/pull/28244
- 状态/时间: merged / 2025-11-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `6eb745d9bdf5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+12/-7，可读 patch 60 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add truncate arg to yarn to match openai implementation of gpt-oss」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Add truncate arg to yarn to match openai implementation of gpt-oss」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-0 (1 lines); hunks: -78,6 +78,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-0 (1 lines); hunks: -78,6 +78,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -78,6 +78,7 @@ def __init__(
+                "truncate": config.rope_parameters.get("truncate", True),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28765 - Fix gpt oss weight loading with EP + bf16

- 链接: https://github.com/vllm-project/vllm/pull/28765
- 状态/时间: merged / 2025-11-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `8d259fad6cd5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix gpt oss weight loading with EP + bf16」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Fix gpt oss weight loading with EP + bf16」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -494,8 +494,8 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other，涉及 `_load_weights_mxfp4, _load_weights_other`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -494,8 +494,8 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -494,8 +494,8 @@ def _load_weights_mxfp4(
-        ep_rank_start: int,
+        ep_rank_start: int,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28715 - Fixed gpt-oss _load_weights_other() parameter position bug

- 链接: https://github.com/vllm-project/vllm/pull/28715
- 状态/时间: merged / 2025-11-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `af02c409702f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fixed gpt-oss _load_weights_other() parameter position bug」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Fixed gpt-oss _load_weights_other() parameter position bug」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -641,8 +641,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -641,8 +641,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -641,8 +641,8 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-                ep_rank_end,
+                ep_rank_end,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28536 - [Bugfix] Fix gpt_oss packed_modules_mapping

- 链接: https://github.com/vllm-project/vllm/pull/28536
- 状态/时间: merged / 2025-11-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `a9d18b51078d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-5，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix gpt_oss packed_modules_mapping」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Bugfix] Fix gpt_oss packed_modules_mapping」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +5/-5 (10 lines); hunks: -92,7 +92,7 @@ def __init__(; -129,7 +129,7 @@ def __init__(; symbols: __init__, forward, _load_weights_other, load_weights，涉及 `__init__, forward, _load_weights_other`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +5/-5 (10 lines); hunks: -92,7 +92,7 @@ def __init__(; -129,7 +129,7 @@ def __init__(; symbols: __init__, forward, _load_weights_other, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +5/-5
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27334 - [Quantization] fix attention quantization of gpt_oss model

- 链接: https://github.com/vllm-project/vllm/pull/27334
- 状态/时间: merged / 2025-11-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `5a1271d83a65`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+101/-4，可读 patch 154 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Quantization] fix attention quantization of gpt_oss model」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Quantization] fix attention quantization of gpt_oss model」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +8/-2 (10 lines); hunks: -198,6 +198,7 @@ class TransformerBlock(torch.nn.Module):; -207,7 +208,10 @@ def __init__(; symbols: TransformerBlock, __init__，涉及 `TransformerBlock, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +8/-2 (10 lines); hunks: -198,6 +198,7 @@ class TransformerBlock(torch.nn.Module):; -207,7 +208,10 @@ def __init__(; symbols: TransformerBlock, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +8/-2
- 验证与风险: diff 自带测试面 `tests/models/quantization/test_gpt_oss_attn_quantization.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27786 - [XPU] Add gpt-oss model support for Intel GPU

- 链接: https://github.com/vllm-project/vllm/pull/27786
- 状态/时间: merged / 2025-11-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `18b39828d904`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+101/-6，可读 patch 160 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU] Add gpt-oss model support for Intel GPU」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[XPU] Add gpt-oss model support for Intel GPU」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +0/-3 (3 lines); hunks: -329,9 +329,6 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4，涉及 `_load_weights_mxfp4`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +0/-3 (3 lines); hunks: -329,9 +329,6 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -329,9 +329,6 @@ def _load_weights_mxfp4(
-            # FIXME(woosuk): Remove this after testing.
-            weight = weight.cuda()
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +0/-3
- 验证与风险: runtime 路径改动集中在 `vllm/attention/utils/fa_utils.py`, `vllm/model_executor/layers/quantization/mxfp4.py`, `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24032 - [BugFix] GPT-OSS Attention DP + MoE TP weight loading issue

- 链接: https://github.com/vllm-project/vllm/pull/24032
- 状态/时间: merged / 2025-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `aef368aa0857`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+30/-13，可读 patch 89 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix] GPT-OSS Attention DP + MoE TP weight loading issue」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[BugFix] GPT-OSS Attention DP + MoE TP weight loading issue」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +16/-4 (20 lines); hunks: -11,13 +11,15; -305,8 +307,13 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other，涉及 `_load_weights_mxfp4, _load_weights_other`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +16/-4 (20 lines); hunks: -11,13 +11,15; -305,8 +307,13 @@ def _load_weights_mxfp4(; symbols: _load_weights_mxfp4, _load_weights_other
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +16/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26030 - [CI] Tweaks to GPT-OSS Eval (Blackwell) for stability

- 链接: https://github.com/vllm-project/vllm/pull/26030
- 状态/时间: merged / 2025-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gpt_oss/test_gpqa_correctness.py`；关联提交 `ee04c0cd04cf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+3/-4，可读 patch 28 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Tweaks to GPT-OSS Eval (Blackwell) for stability」；模型线: GPT-OSS；类别: 文档/测试/CI；主要 diff: `tests/evals/gpt_oss/test_gpqa_correctness.py`；技术摘要: 覆盖「[CI] Tweaks to GPT-OSS Eval (Blackwell) for stability」；主要实现面是 `tests/evals/gpt_oss/test_gpqa_correctness.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gpt_oss/test_gpqa_correctness.py` modified +2/-3 (5 lines); hunks: -26,7 +26,8 @@ def run_gpqa_eval(model_name: str, base_url: str) -> float:; -72,8 +73,6 @@ def test_gpqa_correctness(request):; symbols: run_gpqa_eval, test_gpqa_correctness，涉及 `run_gpqa_eval, test_gpqa_correctness`。
- 代码 diff 细节:
  - `tests/evals/gpt_oss/test_gpqa_correctness.py` modified +2/-3 (5 lines); hunks: -26,7 +26,8 @@ def run_gpqa_eval(model_name: str, base_url: str) -> float:; -72,8 +73,6 @@ def test_gpqa_correctness(request):; symbols: run_gpqa_eval, test_gpqa_correctness
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/evals/gpt_oss/test_gpqa_correctness.py` modified +2/-3
- 验证与风险: diff 自带测试面 `tests/evals/gpt_oss/test_gpqa_correctness.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25246 - Enable Eagle3 speculative decoding for GPT-OSS model

- 链接: https://github.com/vllm-project/vllm/pull/25246
- 状态/时间: merged / 2025-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `21467f9a1c62`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+41/-12，可读 patch 111 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable Eagle3 speculative decoding for GPT-OSS model」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Enable Eagle3 speculative decoding for GPT-OSS model」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +17/-2 (19 lines); hunks: -28,7 +28,7; -239,6 +239,7 @@ def __init__(; symbols: __init__, get_input_embeddings, forward, _load_weights_mxfp4，涉及 `__init__, get_input_embeddings, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +17/-2 (19 lines); hunks: -28,7 +28,7; -239,6 +239,7 @@ def __init__(; symbols: __init__, get_input_embeddings, forward, _load_weights_mxfp4
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +17/-2
- 验证与风险: runtime 路径改动集中在 `vllm/config/speculative.py`, `vllm/model_executor/models/gpt_oss.py`, `vllm/v1/spec_decode/eagle.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24920 - [CI] GPT-OSS GPQA eval test for Blackwell

- 链接: https://github.com/vllm-project/vllm/pull/24920
- 状态/时间: merged / 2025-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gpt_oss/__init__.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/test_gpqa_correctness.py`；关联提交 `493b10f8bf38`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+136/-0，可读 patch 147 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] GPT-OSS GPQA eval test for Blackwell」；模型线: GPT-OSS；类别: 文档/测试/CI；主要 diff: `tests/evals/gpt_oss/test_gpqa_correctness.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/__init__.py`；技术摘要: 覆盖「[CI] GPT-OSS GPQA eval test for Blackwell」；主要实现面是 `tests/evals/gpt_oss/test_gpqa_correctness.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/__init__.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gpt_oss/test_gpqa_correctness.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: run_gpqa_eval, test_gpqa_correctness，涉及 `run_gpqa_eval, test_gpqa_correctness`；`tests/evals/gpt_oss/conftest.py` added +18/-0 (18 lines); hunks: -0,0 +1,18; symbols: pytest_addoption，涉及 `pytest_addoption`；`tests/evals/gpt_oss/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2。
- 代码 diff 细节:
  - `tests/evals/gpt_oss/test_gpqa_correctness.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: run_gpqa_eval, test_gpqa_correctness
  - `tests/evals/gpt_oss/conftest.py` added +18/-0 (18 lines); hunks: -0,0 +1,18; symbols: pytest_addoption
  - `tests/evals/gpt_oss/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/evals/gpt_oss/test_gpqa_correctness.py` added +102/-0; `tests/evals/gpt_oss/conftest.py` added +18/-0; `tests/evals/gpt_oss/__init__.py` added +2/-0
- 验证与风险: diff 自带测试面 `tests/evals/gpt_oss/__init__.py`, `tests/evals/gpt_oss/conftest.py`, `tests/evals/gpt_oss/test_gpqa_correctness.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23815 - [Model] [gpt-oss] fix gpt-oss pp support

- 链接: https://github.com/vllm-project/vllm/pull/23815
- 状态/时间: merged / 2025-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `bfab219648fd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-3，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] [gpt-oss] fix gpt-oss pp support」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Model] [gpt-oss] fix gpt-oss pp support」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +2/-3 (5 lines); hunks: -668,9 +668,8 @@ def forward(self,; symbols: forward, compute_logits，涉及 `forward, compute_logits`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +2/-3 (5 lines); hunks: -668,9 +668,8 @@ def forward(self,; symbols: forward, compute_logits
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -668,9 +668,8 @@ def forward(self,
-        assert intermediate_tensors is None
-        assert inputs_embeds is None
-        return self.model(input_ids, positions)
+        return self.model(input_ids, positions, intermediate_tensors,
+                          inputs_embeds)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +2/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23680 - [Model] Add PP support and VLM backbone compatability for GPT-OSS

- 链接: https://github.com/vllm-project/vllm/pull/23680
- 状态/时间: merged / 2025-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `c5d004aaaf3b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+87/-34，可读 patch 232 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add PP support and VLM backbone compatability for GPT-OSS」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Model] Add PP support and VLM backbone compatability for GPT-OSS」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +86/-33 (119 lines); hunks: -11,7 +11,8; -27,7 +28,10; symbols: __init__, forward, MLPBlock，涉及 `__init__, forward, MLPBlock`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +86/-33 (119 lines); hunks: -11,7 +11,8; -27,7 +28,10; symbols: __init__, forward, MLPBlock
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +86/-33
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23613 - [Bugfix][gpt-oss] passing the cache config in gpt-oss

- 链接: https://github.com/vllm-project/vllm/pull/23613
- 状态/时间: merged / 2025-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `fecbb7c78298`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-1，可读 patch 33 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][gpt-oss] passing the cache config in gpt-oss」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Bugfix][gpt-oss] passing the cache config in gpt-oss」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +6/-1 (7 lines); hunks: -174,12 +174,15 @@ class TransformerBlock(torch.nn.Module):; -203,6 +206,7 @@ def __init__(; symbols: TransformerBlock, __init__，涉及 `TransformerBlock, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +6/-1 (7 lines); hunks: -174,12 +174,15 @@ class TransformerBlock(torch.nn.Module):; -203,6 +206,7 @@ def __init__(; symbols: TransformerBlock, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +6/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22951 - [Kernel] Add cuda kernel for gpt_oss activation

- 链接: https://github.com/vllm-project/vllm/pull/22951
- 状态/时间: merged / 2025-08-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `4d4061b6e73d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+157/-42，可读 patch 330 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Add cuda kernel for gpt_oss activation」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Kernel] Add cuda kernel for gpt_oss activation」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -159,7 +159,7 @@ def __init__(
-                                activation="swiglu_oai")
+                                activation="swigluoai")
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_activation.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22948 - Revert "[Kernel] Add cuda kernel for gpt_oss activation"

- 链接: https://github.com/vllm-project/vllm/pull/22948
- 状态/时间: merged / 2025-08-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `f1f0d2fab8a1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+24/-150，可读 patch 290 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[Kernel] Add cuda kernel for gpt_oss activation"」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Revert "[Kernel] Add cuda kernel for gpt_oss activation"」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -159,7 +159,7 @@ def __init__(
-                                activation="swigluoai")
+                                activation="swiglu_oai")
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_activation.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22538 - [Kernel] Add cuda kernel for gpt_oss activation

- 链接: https://github.com/vllm-project/vllm/pull/22538
- 状态/时间: merged / 2025-08-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `81f4b9648117`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+150/-24，可读 patch 290 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Add cuda kernel for gpt_oss activation」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[Kernel] Add cuda kernel for gpt_oss activation」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/gpt_oss.py
@@ -159,7 +159,7 @@ def __init__(
-                                activation="swiglu_oai")
+                                activation="swigluoai")
```

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_activation.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22678 - Force TRTLLM attention for gpt-oss on SM100

- 链接: https://github.com/vllm-project/vllm/pull/22678
- 状态/时间: merged / 2025-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `c6b928798e96`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+20/-9，可读 patch 96 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Force TRTLLM attention for gpt-oss on SM100」；模型线: GPT-OSS；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Force TRTLLM attention for gpt-oss on SM100」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +1/-4 (5 lines); hunks: -8,7 +8,6; -70,11 +69,9 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +1/-4 (5 lines); hunks: -8,7 +8,6; -70,11 +69,9 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +1/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`, `vllm/utils/flashinfer.py`, `vllm/v1/attention/backends/flashinfer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22508 - [oss] Init gpt-oss bf16 support

- 链接: https://github.com/vllm-project/vllm/pull/22508
- 状态/时间: merged / 2025-08-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `0c5254b82acc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+342/-125，可读 patch 726 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[oss] Init gpt-oss bf16 support」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[oss] Init gpt-oss bf16 support」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +149/-3 (152 lines); hunks: -160,7 +160,9 @@ def __init__(; -262,8 +264,8 @@ def compute_logits(self, hidden_states: torch.Tensor,; symbols: __init__, forward, compute_logits, load_weights，涉及 `__init__, forward, compute_logits`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +149/-3 (152 lines); hunks: -160,7 +160,9 @@ def __init__(; -262,8 +264,8 @@ def compute_logits(self, hidden_states: torch.Tensor,; symbols: __init__, forward, compute_logits, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +149/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22421 - [gpt-oss] triton kernel mxfp4

- 链接: https://github.com/vllm-project/vllm/pull/22421
- 状态/时间: merged / 2025-08-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；关联提交 `e789cad6b8b5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+755/-9，可读 patch 859 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[gpt-oss] triton kernel mxfp4」；模型线: GPT-OSS；类别: 性能/后端优化；主要 diff: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；技术摘要: 覆盖「[gpt-oss] triton kernel mxfp4」；主要实现面是 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` added +375/-0 (375 lines); hunks: -0,0 +1,375; symbols: deshuffle, init_compute_data, ModelConfig, swiglu，涉及 `deshuffle, init_compute_data, ModelConfig`。
- 代码 diff 细节:
  - `tests/kernels/moe/test_gpt_oss_triton_kernels.py` added +375/-0 (375 lines); hunks: -0,0 +1,375; symbols: deshuffle, init_compute_data, ModelConfig, swiglu
- 关键代码摘录:

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

- 已读文件:
  - tests: `tests/kernels/moe/test_gpt_oss_triton_kernels.py` added +375/-0
- 验证与风险: diff 自带测试面 `tests/kernels/moe/test_gpt_oss_triton_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22401 - [gpt-oss] fix model config with hf_config

- 链接: https://github.com/vllm-project/vllm/pull/22401
- 状态/时间: merged / 2025-08-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `5c7cc33f4daf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-3，可读 patch 21 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[gpt-oss] fix model config with hf_config」；模型线: GPT-OSS；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「[gpt-oss] fix model config with hf_config」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` modified +3/-3 (6 lines); hunks: -61,9 +61,9 @@ def __init__(; -154,7 +154,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` modified +3/-3 (6 lines); hunks: -61,9 +61,9 @@ def __init__(; -154,7 +154,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` modified +3/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/gpt_oss.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #22327 - Add GPT-OSS model code and config [1/N]

- 链接: https://github.com/vllm-project/vllm/pull/22327
- 状态/时间: merged / 2025-08-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/gpt_oss.py`；关联提交 `de98252f497b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+503/-0，可读 patch 530 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add GPT-OSS model code and config [1/N]」；模型线: GPT-OSS；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/gpt_oss.py`；技术摘要: 覆盖「Add GPT-OSS model code and config [1/N]」；主要实现面是 `vllm/model_executor/models/gpt_oss.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/gpt_oss.py` added +472/-0 (472 lines); hunks: -0,0 +1,472; symbols: OAIAttention, __init__, forward, MLPBlock，涉及 `OAIAttention, __init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/gpt_oss.py` added +472/-0 (472 lines); hunks: -0,0 +1,472; symbols: OAIAttention, __init__, forward, MLPBlock
- 关键代码摘录:

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

- 已读文件:
  - runtime: `vllm/model_executor/models/gpt_oss.py` added +472/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
