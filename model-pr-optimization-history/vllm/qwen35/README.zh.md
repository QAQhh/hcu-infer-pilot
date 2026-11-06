# vllm Qwen3.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `examples/pooling/score/colqwen3_5_rerank_online.py` | [#36887](https://github.com/vllm-project/vllm/pull/36887), [#46108](https://github.com/vllm-project/vllm/pull/46108) |
| `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` | [#38083](https://github.com/vllm-project/vllm/pull/38083), [#45002](https://github.com/vllm-project/vllm/pull/45002), [#51293](https://github.com/vllm-project/vllm/pull/51293) |
| `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml` | [#38083](https://github.com/vllm-project/vllm/pull/38083) |
| `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml` | [#46520](https://github.com/vllm-project/vllm/pull/46520) |
| `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-EMU-TP2.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` | [#44700](https://github.com/vllm-project/vllm/pull/44700), [#49881](https://github.com/vllm-project/vllm/pull/49881), [#52007](https://github.com/vllm-project/vllm/pull/52007) |
| `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` | [#38083](https://github.com/vllm-project/vllm/pull/38083), [#38632](https://github.com/vllm-project/vllm/pull/38632), [#52007](https://github.com/vllm-project/vllm/pull/52007) |
| `tests/evals/gsm8k/configs/Qwen3.5-4B-Octave-k3v3-compact.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/Qwen3.5-4B-Octave-k3v3.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/Qwen3.5-4B-Octave-k3v4.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/Qwen3.5-4B-watermark.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-35B-A3B-FP8-humming-act-fp8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-35B-A3B-FP8-humming.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-35B-A3B-experts-int8-humming-act-int8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-35B-A3B-experts-int8-humming.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-35B-A3B-int6wc-hadamard-humming-act-int8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-35B-A3B-int6wc-hadamard-humming.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-4B-quantized.w4a16-humming-act-fp8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-4B-quantized.w4a16-humming-act-int8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-4B-quantized.w4a16-humming.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-9B-int6wc-hadamard-humming-act-int8.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/humming/Qwen3.5-9B-int6wc-hadamard-humming.yaml` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` | [#38083](https://github.com/vllm-project/vllm/pull/38083), [#44700](https://github.com/vllm-project/vllm/pull/44700) |
| `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` | [#38155](https://github.com/vllm-project/vllm/pull/38155), [#38664](https://github.com/vllm-project/vllm/pull/38664) |
| `tests/evals/mrcr/configs/Qwen3.5-4B.yaml` | 无直接 PR 号提交 |
| `tests/lora/test_qwen35_densemodel_lora.py` | [#37816](https://github.com/vllm-project/vllm/pull/37816) |
| `tests/model_executor/test_qwen3_5_quantization.py` | 无直接 PR 号提交 |
| `tests/models/multimodal/pooling/test_colqwen3_5.py` | [#36887](https://github.com/vllm-project/vllm/pull/36887), [#46108](https://github.com/vllm-project/vllm/pull/46108), [#49372](https://github.com/vllm-project/vllm/pull/49372) |
| `tests/models/qwen3_5/__init__.py` | [#64509](https://github.com/vllm-project/vllm/pull/64509) |
| `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py` | [#64723](https://github.com/vllm-project/vllm/pull/64723) |
| `tests/models/qwen3_5/test_gdn_ba_overlap.py` | 无直接 PR 号提交 |
| `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` | [#64509](https://github.com/vllm-project/vllm/pull/64509) |
| `tests/models/test_qwen3_5.py` | [#51012](https://github.com/vllm-project/vllm/pull/51012) |
| `tests/models/test_qwen3_5_mtp_config.py` | [#50734](https://github.com/vllm-project/vllm/pull/50734), [#55369](https://github.com/vllm-project/vllm/pull/55369), [#62111](https://github.com/vllm-project/vllm/pull/62111) |
| `tests/v1/e2e/spec_decode/mtp/qwen3_5/__init__.py` | 无直接 PR 号提交 |
| `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py` | [#62111](https://github.com/vllm-project/vllm/pull/62111) |
| `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_rejected_placeholders.py` | 无直接 PR 号提交 |
| `vllm/model_executor/models/colqwen3_5.py` | [#36887](https://github.com/vllm-project/vllm/pull/36887), [#46108](https://github.com/vllm-project/vllm/pull/46108), [#54847](https://github.com/vllm-project/vllm/pull/54847) |
| `vllm/model_executor/models/qwen3_5.py` | [#34110](https://github.com/vllm-project/vllm/pull/34110), [#34198](https://github.com/vllm-project/vllm/pull/34198), [#34200](https://github.com/vllm-project/vllm/pull/34200), [#34313](https://github.com/vllm-project/vllm/pull/34313), [#34489](https://github.com/vllm-project/vllm/pull/34489), [#34492](https://github.com/vllm-project/vllm/pull/34492), [#34512](https://github.com/vllm-project/vllm/pull/34512), [#34683](https://github.com/vllm-project/vllm/pull/34683), [#34697](https://github.com/vllm-project/vllm/pull/34697), [#34719](https://github.com/vllm-project/vllm/pull/34719), [#34723](https://github.com/vllm-project/vllm/pull/34723), [#35617](https://github.com/vllm-project/vllm/pull/35617), ... (30 total) |
| `vllm/model_executor/models/qwen3_5_mtp.py` | [#34110](https://github.com/vllm-project/vllm/pull/34110), [#34512](https://github.com/vllm-project/vllm/pull/34512), [#35581](https://github.com/vllm-project/vllm/pull/35581), [#37114](https://github.com/vllm-project/vllm/pull/37114), [#38832](https://github.com/vllm-project/vllm/pull/38832), [#42716](https://github.com/vllm-project/vllm/pull/42716), [#45002](https://github.com/vllm-project/vllm/pull/45002), [#48816](https://github.com/vllm-project/vllm/pull/48816), [#62111](https://github.com/vllm-project/vllm/pull/62111) |
| `vllm/models/qwen3_5/__init__.py` | [#51012](https://github.com/vllm-project/vllm/pull/51012) |
| `vllm/models/qwen3_5/nvidia/__init__.py` | [#51012](https://github.com/vllm-project/vllm/pull/51012) |
| `vllm/models/qwen3_5/nvidia/model.py` | [#51012](https://github.com/vllm-project/vllm/pull/51012), [#64425](https://github.com/vllm-project/vllm/pull/64425), [#64509](https://github.com/vllm-project/vllm/pull/64509), [#64723](https://github.com/vllm-project/vllm/pull/64723) |
| `vllm/models/qwen3_5/nvidia/mtp.py` | [#51012](https://github.com/vllm-project/vllm/pull/51012), [#62111](https://github.com/vllm-project/vllm/pull/62111) |
| `vllm/models/qwen3_5/nvidia/ops/__init__.py` | [#51012](https://github.com/vllm-project/vllm/pull/51012) |
| `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py` | [#64723](https://github.com/vllm-project/vllm/pull/64723) |
| `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` | [#51012](https://github.com/vllm-project/vllm/pull/51012), [#64509](https://github.com/vllm-project/vllm/pull/64509) |
| `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` | [#64509](https://github.com/vllm-project/vllm/pull/64509) |

## PR 覆盖总览

- git 追溯 PR 数: 54
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 54

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-11-03 | [#64723](https://github.com/vllm-project/vllm/pull/64723) | merged | [Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant | `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py` |
| 2026-10-30 | [#62111](https://github.com/vllm-project/vllm/pull/62111) | merged | [Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next | `tests/models/test_qwen3_5_mtp_config.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py` |
| 2026-10-30 | [#64509](https://github.com/vllm-project/vllm/pull/64509) | merged | [Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant | `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` |
| 2026-10-29 | [#64425](https://github.com/vllm-project/vllm/pull/64425) | merged | [Perf] Qwen3.5 GDN: overlap in_proj_ba with in_proj_qkvz on the aux stream | `vllm/models/qwen3_5/nvidia/model.py` |
| 2026-10-29 | [#51012](https://github.com/vllm-project/vllm/pull/51012) | merged | [Models] Deprecate `torch.compile` for Qwen3.5 models | `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/mtp.py`, `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` |
| 2026-10-10 | [#59853](https://github.com/vllm-project/vllm/pull/59853) | merged | [Model] Drop the 4x M-RoPE cache headroom for Qwen3-VL, Qwen3.5 and Qwen3.8 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-09-29 | [#51289](https://github.com/vllm-project/vllm/pull/51289) | merged | [Model] Extend device-side mm normalization to Qwen3VL/Qwen3.5/Qwen4Next | `vllm/model_executor/models/qwen3_5.py` |
| 2026-09-07 | [#55369](https://github.com/vllm-project/vllm/pull/55369) | merged | [Bugfix][Spec Decode] Resolve n_predict from text_config for Qwen3.5 multimodal MTP | `tests/models/test_qwen3_5_mtp_config.py` |
| 2026-09-02 | [#54847](https://github.com/vllm-project/vllm/pull/54847) | merged | [Bugfix] Fix ColQwen3.5 pooler projector initialization | `vllm/model_executor/models/colqwen3_5.py` |
| 2026-08-19 | [#48850](https://github.com/vllm-project/vllm/pull/48850) | merged | [Bugfix][LoRA] Add embedding_modules for Qwen3.5 CausalLM | `vllm/model_executor/models/qwen3_5.py` |
| 2026-08-12 | [#52007](https://github.com/vllm-project/vllm/pull/52007) | merged | [CI Bug] Fix ci qwen3.5 | `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` |
| 2026-08-10 | [#50734](https://github.com/vllm-project/vllm/pull/50734) | merged | [Bugfix][Model] Fix Qwen3.5 MTP for text-only checkpoints | `tests/models/test_qwen3_5_mtp_config.py` |
| 2026-08-07 | [#51293](https://github.com/vllm-project/vllm/pull/51293) | merged | [CI] Re-enable FI autotune in GSM8K config for Qwen3.5-35B-A3B | `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` |
| 2026-08-06 | [#50355](https://github.com/vllm-project/vllm/pull/50355) | merged | [Model] Fix weight prefix mapping for native Qwen3.5 text-only checkp… | `vllm/model_executor/models/qwen3_5.py` |
| 2026-07-29 | [#50210](https://github.com/vllm-project/vllm/pull/50210) | merged | [Model] Support Qwen3.5 text-only dense and MoE models | `vllm/model_executor/models/qwen3_5.py` |
| 2026-07-28 | [#49881](https://github.com/vllm-project/vllm/pull/49881) | merged | [CI] Increase Qwen3.5 MTP GSM8K generation length | `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` |
| 2026-07-27 | [#48912](https://github.com/vllm-project/vllm/pull/48912) | merged | [Model] Enable EVS for Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-07-26 | [#49372](https://github.com/vllm-project/vllm/pull/49372) | merged | [Bugfix] Respect declared attention contract for ColQwen3.5 retrievers | `tests/models/multimodal/pooling/test_colqwen3_5.py` |
| 2026-07-23 | [#48816](https://github.com/vllm-project/vllm/pull/48816) | merged | Fix GPTQ quantized Qwen3.5 MTP weight loading with spec decode | `vllm/model_executor/models/qwen3_5_mtp.py` |
| 2026-06-23 | [#44434](https://github.com/vllm-project/vllm/pull/44434) | merged | [ROCm][Bugfix][Perf] enable shared expert fusion for Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-06-23 | [#46520](https://github.com/vllm-project/vllm/pull/46520) | merged | [ROCm][CI] Shard LM Eval Qwen3-5 Models (B200-MI355) in AMD CI | `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml` |
| 2026-06-22 | [#46108](https://github.com/vllm-project/vllm/pull/46108) | merged | [Model] ColQwen3.5: fix retrieval correctness (bias + bidirectional) | `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/models/colqwen3_5.py`, `examples/pooling/score/colqwen3_5_rerank_online.py` |
| 2026-06-09 | [#45002](https://github.com/vllm-project/vllm/pull/45002) | merged | [Bugfix] fix qwen3.5 ep weight loading | `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` |
| 2026-06-06 | [#44700](https://github.com/vllm-project/vllm/pull/44700) | merged | [PERF] [Qwen3.5] Split mixed prefill+decode batches: route decodes to the recurrent kernel | `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` |
| 2026-05-17 | [#42716](https://github.com/vllm-project/vllm/pull/42716) | merged | Fix Weight loading for Qwen3.5-MTP and Qwen3-VL using runai_streamer | `vllm/model_executor/models/qwen3_5_mtp.py` |
| 2026-05-14 | [#42521](https://github.com/vllm-project/vllm/pull/42521) | merged | [Fix] Weight loading for qwen3_5 using runai_streamer | `vllm/model_executor/models/qwen3_5.py` |
| 2026-05-13 | [#42151](https://github.com/vllm-project/vllm/pull/42151) | merged | [MM][Perf][CG] Support ViT full CUDA graph for Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-05-10 | [#37912](https://github.com/vllm-project/vllm/pull/37912) | merged | [Bugfix] Fuse Qwen3.5 in_qkvz_proj forwarding with LoRA enabled | `vllm/model_executor/models/qwen3_5.py` |
| 2026-04-21 | [#37114](https://github.com/vllm-project/vllm/pull/37114) | merged | [Bugfix] LoRA: extend expert base_layer loading to Qwen3.5 and Step3.x | `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py` |
| 2026-04-03 | [#38927](https://github.com/vllm-project/vllm/pull/38927) | merged | [Bugfix][LoRA] Fix missing in_proj_z in Qwen3_5ForConditionalGenerati… | `vllm/model_executor/models/qwen3_5.py` |
| 2026-04-03 | [#38664](https://github.com/vllm-project/vllm/pull/38664) | merged | [CI][ROCm] Add Qwen3.5-35B-A3B-MXFP4 model eval into CI | `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` |
| 2026-04-03 | [#38832](https://github.com/vllm-project/vllm/pull/38832) | merged | [Bugfix] Fix NVFP4+MTP crash: force unquantized mtp.fc for Qwen3.5 | `vllm/model_executor/models/qwen3_5_mtp.py` |
| 2026-03-31 | [#38632](https://github.com/vllm-project/vllm/pull/38632) | merged | [CI] fix LM Eval Qwen3.5 Models (B200) | `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` |
| 2026-03-27 | [#37975](https://github.com/vllm-project/vllm/pull/37975) | merged | [Model] Extract GatedDeltaNetAttention into shared layer for Qwen3Next and Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-03-26 | [#38155](https://github.com/vllm-project/vllm/pull/38155) | merged | [ROCm][CI] Add LM Eval Qwen3.5 Models test for MI355 | `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` |
| 2026-03-26 | [#38083](https://github.com/vllm-project/vllm/pull/38083) | merged | [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell | `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml` |
| 2026-03-23 | [#37816](https://github.com/vllm-project/vllm/pull/37816) | merged | [CI/Build][LoRA] Update Qwen35 LoRA testing | `tests/lora/test_qwen35_densemodel_lora.py` |
| 2026-03-20 | [#36976](https://github.com/vllm-project/vllm/pull/36976) | merged | [Bugfix][LoRA] Fix Qwen35 LoRA | `vllm/model_executor/models/qwen3_5.py` |
| 2026-03-19 | [#37448](https://github.com/vllm-project/vllm/pull/37448) | merged | Fix AttributeError in Qwen3.5 GDN layers with quantized models | `vllm/model_executor/models/qwen3_5.py` |
| 2026-03-17 | [#36887](https://github.com/vllm-project/vllm/pull/36887) | merged | [Model] Add ColQwen3.5 4.5B support | `vllm/model_executor/models/colqwen3_5.py`, `tests/models/multimodal/pooling/test_colqwen3_5.py`, `examples/pooling/score/colqwen3_5_rerank_online.py` |
| 2026-03-11 | [#36658](https://github.com/vllm-project/vllm/pull/36658) | merged | Add: Eagle3 support for Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-03-01 | [#35617](https://github.com/vllm-project/vllm/pull/35617) | merged | [Bugfix][Model] Fix Qwen3.5/Qwen3Next ignoring --dtype flag on older GPUs | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-28 | [#35581](https://github.com/vllm-project/vllm/pull/35581) | merged | Fix Qwen3_5MTP packed_modules_mapping for gate_up_proj | `vllm/model_executor/models/qwen3_5_mtp.py` |
| 2026-02-19 | [#34719](https://github.com/vllm-project/vllm/pull/34719) | merged | [Bugfix] Qwen3.5 kv-scale weight remapping | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-18 | [#34697](https://github.com/vllm-project/vllm/pull/34697) | merged | [Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-18 | [#34723](https://github.com/vllm-project/vllm/pull/34723) | merged | [Bugfix] Fix prefix creation for Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-17 | [#34683](https://github.com/vllm-project/vllm/pull/34683) | merged | Revert "[Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj" | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-16 | [#34492](https://github.com/vllm-project/vllm/pull/34492) | merged | [Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-13 | [#34512](https://github.com/vllm-project/vllm/pull/34512) | merged | [Misc] Port Qwen3.5 Configs | `vllm/transformers_utils/configs/qwen3_5.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py` |
| 2026-02-13 | [#34489](https://github.com/vllm-project/vllm/pull/34489) | merged | [Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-11 | [#34313](https://github.com/vllm-project/vllm/pull/34313) | merged | [Bugfix] Fix weight naming in Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-10 | [#34200](https://github.com/vllm-project/vllm/pull/34200) | merged | [Bugfix] Fix mamba cache dtype for Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-10 | [#34198](https://github.com/vllm-project/vllm/pull/34198) | merged | [Bugfix] Adopt `ChunkGatedDeltaRule` for Qwen3.5 | `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-09 | [#34110](https://github.com/vllm-project/vllm/pull/34110) | merged | [MODEL] Adding Support for Qwen3.5 Models | `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py` |

## 逐 PR diff 审计卡

### PR #64723 - [Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant

- 链接: https://github.com/vllm-project/vllm/pull/64723
- 状态/时间: merged / 2026-11-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`；关联提交 `523991fec066`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+424/-46，可读 patch 547 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`；技术摘要: 覆盖「[Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant」；主要实现面是 `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: _worker, make_linear, run_one, test_forward_fused，涉及 `_worker, make_linear, run_one`；`vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: _get_workspace, fused_allreduce_gemma_rms_norm_quant，涉及 `_get_workspace, fused_allreduce_gemma_rms_norm_quant`；`vllm/models/qwen3_5/nvidia/model.py` modified +69/-46 (115 lines); hunks: -125,6 +125,7; -179,13 +180,21 @@ class Qwen3_5RMSNorm(nn.Module):; symbols: Qwen3_5RMSNorm, __init__, forward，涉及 `Qwen3_5RMSNorm, __init__, forward`。
- 代码 diff 细节:
  - `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: _worker, make_linear, run_one, test_forward_fused
  - `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py` added +167/-0 (167 lines); hunks: -0,0 +1,167; symbols: _get_workspace, fused_allreduce_gemma_rms_norm_quant
  - `vllm/models/qwen3_5/nvidia/model.py` modified +69/-46 (115 lines); hunks: -125,6 +125,7; -179,13 +180,21 @@ class Qwen3_5RMSNorm(nn.Module):; symbols: Qwen3_5RMSNorm, __init__, forward
- 关键代码摘录:

```diff
diff -- tests/models/qwen3_5/test_fused_allreduce_norm_quant.py
@@ -0,0 +1,186 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""TP2: ``Qwen3_5RMSNorm.forward_fused`` vs the unfused chain it replaces,
+(all-reduce +) Gemma norm, then scaled_fp8_quant / scaled_fp4_quant, for real
+ModelOpt static FP8 and NVFP4 consumers.
+All cases run in one 2-rank spawn; spawning per case re-imports vLLM and
diff -- vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py
@@ -0,0 +1,167 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""TP all-reduce + residual add + Gemma RMSNorm + consumer input quant.
+Calls FlashInfer's ``kARResidualRMSNormOut{FP8,FP4}Quant`` patterns directly
+(no torch.compile custom op). The kernel writes the bf16 normed activation
+(GDN's ``in_proj_ba`` reads it) next to the static FP8 / NVFP4 codes; its
diff -- vllm/models/qwen3_5/nvidia/model.py
@@ -125,6 +125,7 @@
```

- 已读文件:
  - tests: `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py` added +186/-0
  - runtime: `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py` added +167/-0; `vllm/models/qwen3_5/nvidia/model.py` modified +69/-46
- 验证与风险: diff 自带测试面 `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #62111 - [Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next

- 链接: https://github.com/vllm-project/vllm/pull/62111
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/test_qwen3_5_mtp_config.py`, `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/models/qwen3_5/nvidia/mtp.py`；关联提交 `dd5f5eebd7a0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+222/-16，可读 patch 388 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/models/test_qwen3_5_mtp_config.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`；技术摘要: 覆盖「[Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next」；主要实现面是 `tests/models/test_qwen3_5_mtp_config.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/test_qwen3_5_mtp_config.py` modified +64/-1 (65 lines); hunks: -2,11 +2,18; -119,3 +126,59 @@ def test_mtp_override_downloads_real_hf_hub_configs(; symbols: test_mtp_override_downloads_real_hf_hub_configs, test_mtp_num_hidden_layers_selects_multi_module_mtp，涉及 `test_mtp_override_downloads_real_hf_hub_configs, test_mtp_num_hidden_layers_selects_multi_module_mtp`；`vllm/model_executor/models/qwen3_5_mtp.py` modified +22/-4 (26 lines); hunks: -28,6 +28,9; -59,7 +62,8; symbols: Qwen3_5MultiTokenPredictor, load_weights, Qwen3_5MTP, forward，涉及 `Qwen3_5MultiTokenPredictor, load_weights, Qwen3_5MTP`；`vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4 (23 lines); hunks: -41,7 +41,17; -171,7 +181,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights, Qwen3NextMTP，涉及 `should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights`；`vllm/models/qwen3_5/nvidia/mtp.py` modified +15/-2 (17 lines); hunks: -255,10 +255,15 @@ def forward( # type: ignore[override]; -269,6 +274,14 @@ def compute_logits(; symbols: forward, compute_logits, get_top_tokens, is_unused_checkpoint_weight，涉及 `forward, compute_logits, get_top_tokens`。
- 代码 diff 细节:
  - `tests/models/test_qwen3_5_mtp_config.py` modified +64/-1 (65 lines); hunks: -2,11 +2,18; -119,3 +126,59 @@ def test_mtp_override_downloads_real_hf_hub_configs(; symbols: test_mtp_override_downloads_real_hf_hub_configs, test_mtp_num_hidden_layers_selects_multi_module_mtp
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +22/-4 (26 lines); hunks: -28,6 +28,9; -59,7 +62,8; symbols: Qwen3_5MultiTokenPredictor, load_weights, Qwen3_5MTP, forward
  - `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4 (23 lines); hunks: -41,7 +41,17; -171,7 +181,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: should_torch_compile_mtp_drafter, Qwen3NextMultiTokenPredictor, load_weights, Qwen3NextMTP
  - `vllm/models/qwen3_5/nvidia/mtp.py` modified +15/-2 (17 lines); hunks: -255,10 +255,15 @@ def forward( # type: ignore[override]; -269,6 +274,14 @@ def compute_logits(; symbols: forward, compute_logits, get_top_tokens, is_unused_checkpoint_weight
  - `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py` modified +76/-0 (76 lines); hunks: -1,20 +1,96; symbols: _add_random_mtp_module, test_mtp_draft_steps_use_their_own_module
- 关键代码摘录:

```diff
diff -- tests/models/test_qwen3_5_mtp_config.py
@@ -2,11 +2,18 @@
+from pathlib import Path
-from transformers import AutoConfig, PreTrainedConfig
+from transformers import (
+    AutoConfig,
+    PreTrainedConfig,
+    Qwen3_5Config,
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -28,6 +28,9 @@
+from vllm.model_executor.models.qwen3_next_mtp import (
+    should_torch_compile_mtp_drafter,
+)
@@ -59,7 +62,8 @@
-    }
+    },
diff -- vllm/model_executor/models/qwen3_next_mtp.py
@@ -41,7 +41,17 @@
```

- 已读文件:
  - tests: `tests/models/test_qwen3_5_mtp_config.py` modified +64/-1; `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py` modified +76/-0
  - runtime: `vllm/model_executor/models/qwen3_5_mtp.py` modified +22/-4; `vllm/model_executor/models/qwen3_next_mtp.py` modified +19/-4; `vllm/models/qwen3_5/nvidia/mtp.py` modified +15/-2
- 验证与风险: diff 自带测试面 `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/test_qwen3_5_mtp_config.py`, `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64509 - [Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant

- 链接: https://github.com/vllm-project/vllm/pull/64509
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/qwen3_5/__init__.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py`, `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py`；关联提交 `6c19299fca37`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+668/-34，可读 patch 994 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`；技术摘要: 覆盖「[Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant」；主要实现面是 `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` added +216/-0 (216 lines); hunks: -0,0 +1,216; symbols: _rcp_approx_ftz, _cvt_e2m1x2, _gemma_add_rms_norm_quant_kernel, gemma_add_rms_norm_quant，涉及 `_rcp_approx_ftz, _cvt_e2m1x2, _gemma_add_rms_norm_quant_kernel`；`vllm/models/qwen3_5/nvidia/model.py` modified +125/-18 (143 lines); hunks: -50,6 +50,11; -60,6 +65,14; symbols: _norm_quant_key, _fused_gdn_gated_rms_norm_quant, Qwen3_5RMSNorm, forward，涉及 `_norm_quant_key, _fused_gdn_gated_rms_norm_quant, Qwen3_5RMSNorm`；`tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _fp8_codes, _fp4_codes, _swizzled_sf_rows, test_gemma_add_rms_norm_quant_matches_chain，涉及 `_fp8_codes, _fp4_codes, _swizzled_sf_rows`；`vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` modified +15/-0 (15 lines); hunks: -14,6 +14,7 @@ def _fused_gdn_gated_rms_norm_kernel(; -24,6 +25,7 @@ def _fused_gdn_gated_rms_norm_kernel(; symbols: _fused_gdn_gated_rms_norm_kernel, fused_gdn_gated_rms_norm，涉及 `_fused_gdn_gated_rms_norm_kernel, fused_gdn_gated_rms_norm`。
- 代码 diff 细节:
  - `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` added +216/-0 (216 lines); hunks: -0,0 +1,216; symbols: _rcp_approx_ftz, _cvt_e2m1x2, _gemma_add_rms_norm_quant_kernel, gemma_add_rms_norm_quant
  - `vllm/models/qwen3_5/nvidia/model.py` modified +125/-18 (143 lines); hunks: -50,6 +50,11; -60,6 +65,14; symbols: _norm_quant_key, _fused_gdn_gated_rms_norm_quant, Qwen3_5RMSNorm, forward
  - `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` added +109/-0 (109 lines); hunks: -0,0 +1,109; symbols: _fp8_codes, _fp4_codes, _swizzled_sf_rows, test_gemma_add_rms_norm_quant_matches_chain
  - `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` modified +15/-0 (15 lines); hunks: -14,6 +14,7 @@ def _fused_gdn_gated_rms_norm_kernel(; -24,6 +25,7 @@ def _fused_gdn_gated_rms_norm_kernel(; symbols: _fused_gdn_gated_rms_norm_kernel, fused_gdn_gated_rms_norm
  - `tests/models/qwen3_5/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- 关键代码摘录:

```diff
diff -- vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py
@@ -0,0 +1,216 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Gemma (1 + w) add-RMSNorm fused with the consumer linear's input quant.
+Replaces ``gemma_fused_add_rmsnorm`` followed by a standalone static FP8
+(``scaled_fp8_quant``) or NVFP4 (``scaled_fp4_quant``) kernel. The quantized
+values are computed from the bf16-rounded normed activation with the same
diff -- vllm/models/qwen3_5/nvidia/model.py
@@ -50,6 +50,11 @@
+from vllm.model_executor.layers.fusion.quant_activation import (
+    QuantizedActivation,
+    get_input_quant_key,
+)
+from vllm.model_executor.layers.linear import LinearBase
@@ -60,6 +65,14 @@
diff -- tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py
@@ -0,0 +1,109 @@
```

- 已读文件:
  - runtime: `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` added +216/-0; `vllm/models/qwen3_5/nvidia/model.py` modified +125/-18; `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` modified +15/-0
  - tests: `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py` added +109/-0; `tests/models/qwen3_5/__init__.py` added +2/-0
- 验证与风险: diff 自带测试面 `tests/kernels/core/test_fused_sigmoid_gate_mul.py`, `tests/kernels/mamba/test_gdn_output_projection.py`, `tests/models/qwen3_5/__init__.py`, `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #64425 - [Perf] Qwen3.5 GDN: overlap in_proj_ba with in_proj_qkvz on the aux stream

- 链接: https://github.com/vllm-project/vllm/pull/64425
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/models/qwen3_5/nvidia/model.py`；关联提交 `914d61fc538a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+45/-2，可读 patch 114 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Qwen3.5 GDN: overlap in_proj_ba with in_proj_qkvz on the aux stream」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `vllm/models/qwen3_5/nvidia/model.py`；技术摘要: 覆盖「[Perf] Qwen3.5 GDN: overlap in_proj_ba with in_proj_qkvz on the aux stream」；主要实现面是 `vllm/models/qwen3_5/nvidia/model.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/qwen3_5/nvidia/model.py` modified +2/-0 (2 lines); hunks: -190,6 +190,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/models/qwen3_5/nvidia/model.py` modified +2/-0 (2 lines); hunks: -190,6 +190,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/models/qwen3_5/nvidia/model.py
@@ -190,6 +190,8 @@ def __init__(
+                # This path runs outside torch.compile, as the overlap requires.
+                overlap_ba_proj=True,
```

- 已读文件:
  - runtime: `vllm/models/qwen3_5/nvidia/model.py` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/kernels/mamba/test_gdn_fused_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51012 - [Models] Deprecate `torch.compile` for Qwen3.5 models

- 链接: https://github.com/vllm-project/vllm/pull/51012
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/test_qwen3_5.py`, `vllm/models/qwen3_5/__init__.py`, `vllm/models/qwen3_5/nvidia/__init__.py`, `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/mtp.py` 等 7 个文件；关联提交 `d6fbd9478249`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 29 个文件，+2029/-21，可读 patch 2322 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Models] Deprecate `torch.compile` for Qwen3.5 models」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/mtp.py`, `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py`；技术摘要: 覆盖「[Models] Deprecate `torch.compile` for Qwen3.5 models」；主要实现面是 `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/mtp.py`, `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/models/qwen3_5/nvidia/model.py` added +939/-0 (939 lines); hunks: -0,0 +1,939; symbols: Qwen3_5RMSNorm, __init__, forward, Qwen3_5DecoderLayer，涉及 `Qwen3_5RMSNorm, __init__, forward`；`vllm/models/qwen3_5/nvidia/mtp.py` added +295/-0 (295 lines); hunks: -0,0 +1,295; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward，涉及 `Qwen3_5MultiTokenPredictor, __init__, embed_input_ids`；`vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` added +123/-0 (123 lines); hunks: -0,0 +1,123; symbols: _fused_gdn_gated_rms_norm_kernel, fused_gdn_gated_rms_norm，涉及 `_fused_gdn_gated_rms_norm_kernel, fused_gdn_gated_rms_norm`；`vllm/models/qwen3_5/__init__.py` added +48/-0 (48 lines); hunks: -0,0 +1,48。
- 代码 diff 细节:
  - `vllm/models/qwen3_5/nvidia/model.py` added +939/-0 (939 lines); hunks: -0,0 +1,939; symbols: Qwen3_5RMSNorm, __init__, forward, Qwen3_5DecoderLayer
  - `vllm/models/qwen3_5/nvidia/mtp.py` added +295/-0 (295 lines); hunks: -0,0 +1,295; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward
  - `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` added +123/-0 (123 lines); hunks: -0,0 +1,123; symbols: _fused_gdn_gated_rms_norm_kernel, fused_gdn_gated_rms_norm
  - `vllm/models/qwen3_5/__init__.py` added +48/-0 (48 lines); hunks: -0,0 +1,48
  - `tests/models/test_qwen3_5.py` added +47/-0 (47 lines); hunks: -0,0 +1,47; symbols: test_qwen3_5_models_use_platform_specific_implementation, test_qwen3_5_nvidia_models_do_not_use_torch_compile_wrapper, test_qwen3_5_legacy_models_keep_torch_compile_wrapper
- 关键代码摘录:

```diff
diff -- vllm/models/qwen3_5/nvidia/model.py
@@ -0,0 +1,939 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Copyright 2025 The vLLM team.
+# Copyright 2025 The Qwen Team.
+# Copyright 2025 The HuggingFace Inc. team.
+# All rights reserved.
diff -- vllm/models/qwen3_5/nvidia/mtp.py
@@ -0,0 +1,295 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only Qwen3_5 MTP model."""
+from collections.abc import Iterable
+import torch
+from torch import nn
diff -- vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py
@@ -0,0 +1,123 @@
```

- 已读文件:
  - runtime: `vllm/models/qwen3_5/nvidia/model.py` added +939/-0; `vllm/models/qwen3_5/nvidia/mtp.py` added +295/-0; `vllm/models/qwen3_5/nvidia/ops/fused_gdn_gated_norm.py` added +123/-0; `vllm/models/qwen3_5/__init__.py` added +48/-0; `vllm/models/qwen3_5/nvidia/__init__.py` added +2/-0; `vllm/models/qwen3_5/nvidia/ops/__init__.py` added +2/-0
  - tests: `tests/models/test_qwen3_5.py` added +47/-0
- 验证与风险: diff 自带测试面 `.buildkite/hardware_tests/cpu.yaml`, `tests/conftest.py`, `tests/kernels/core/test_fused_pre_fc_norms.py`, `tests/kernels/core/test_fused_sigmoid_gate_mul.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59853 - [Model] Drop the 4x M-RoPE cache headroom for Qwen3-VL, Qwen3.5 and Qwen3.8

- 链接: https://github.com/vllm-project/vllm/pull/59853
- 状态/时间: merged / 2026-10-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `a98247ab4db6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+56/-6，可读 patch 275 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Drop the 4x M-RoPE cache headroom for Qwen3-VL, Qwen3.5 and Qwen3.8」；模型线: Qwen3.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Model] Drop the 4x M-RoPE cache headroom for Qwen3-VL, Qwen3.5 and Qwen3.8」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +2/-0 (2 lines); hunks: -91,6 +91,7; -161,6 +162,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +2/-0 (2 lines); hunks: -91,6 +91,7; -161,6 +162,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -91,6 +91,7 @@
+    mrope_positions_factor,
@@ -161,6 +162,7 @@ def __init__(
+                mrope_positions_factor=mrope_positions_factor(vllm_config),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `vllm/config/model.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #51289 - [Model] Extend device-side mm normalization to Qwen3VL/Qwen3.5/Qwen4Next

- 链接: https://github.com/vllm-project/vllm/pull/51289
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `491f44adfa42`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+87/-25，可读 patch 321 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Extend device-side mm normalization to Qwen3VL/Qwen3.5/Qwen4Next」；模型线: Qwen3.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Model] Extend device-side mm normalization to Qwen3VL/Qwen3.5/Qwen4Next」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +3/-0 (3 lines); hunks: -39,6 +39,7; -517,6 +518,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +3/-0 (3 lines); hunks: -39,6 +39,7; -517,6 +518,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -39,6 +39,7 @@
+from vllm.model_executor.layers.fusion.mm_input_norm import build_mm_input_norm
@@ -517,6 +518,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
+                input_norm=build_mm_input_norm(self.model_config),
@@ -739,6 +741,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
+                input_norm=build_mm_input_norm(self.model_config),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +3/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation_ppl_test/ppl_utils.py`, `tests/models/multimodal/generation_ppl_test/test_qwen.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #55369 - [Bugfix][Spec Decode] Resolve n_predict from text_config for Qwen3.5 multimodal MTP

- 链接: https://github.com/vllm-project/vllm/pull/55369
- 状态/时间: merged / 2026-09-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/test_qwen3_5_mtp_config.py`；关联提交 `b339d75a410e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+101/-9，可读 patch 145 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Spec Decode] Resolve n_predict from text_config for Qwen3.5 multimodal MTP」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/models/test_qwen3_5_mtp_config.py`；技术摘要: 覆盖「[Bugfix][Spec Decode] Resolve n_predict from text_config for Qwen3.5 multimodal MTP」；主要实现面是 `tests/models/test_qwen3_5_mtp_config.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/test_qwen3_5_mtp_config.py` modified +96/-8 (104 lines); hunks: -1,19 +1,45; -26,8 +52,70 @@ def _mtp_config(model_type: str) -> PretrainedConfig:; symbols: _mtp_config, _multimodal_wrapper_mtp_config, test_mtp_override_recognizes_text_only_types，涉及 `_mtp_config, _multimodal_wrapper_mtp_config, test_mtp_override_recognizes_text_only_types`。
- 代码 diff 细节:
  - `tests/models/test_qwen3_5_mtp_config.py` modified +96/-8 (104 lines); hunks: -1,19 +1,45; -26,8 +52,70 @@ def _mtp_config(model_type: str) -> PretrainedConfig:; symbols: _mtp_config, _multimodal_wrapper_mtp_config, test_mtp_override_recognizes_text_only_types
- 关键代码摘录:

```diff
diff -- tests/models/test_qwen3_5_mtp_config.py
@@ -1,19 +1,45 @@
-"""CPU-only tests for Qwen3.5 text-only MTP speculative decoding."""
+"""CPU-only tests for Qwen3.5 MTP speculative decoding config overrides."""
+from typing import Any
-from transformers import PretrainedConfig
+from transformers import AutoConfig, PretrainedConfig
+_CHECKPOINTS = {
```

- 已读文件:
  - tests: `tests/models/test_qwen3_5_mtp_config.py` modified +96/-8
- 验证与风险: diff 自带测试面 `tests/models/test_qwen3_5_mtp_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #54847 - [Bugfix] Fix ColQwen3.5 pooler projector initialization

- 链接: https://github.com/vllm-project/vllm/pull/54847
- 状态/时间: merged / 2026-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/colqwen3_5.py`；关联提交 `dbf1a044eacd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-17，可读 patch 64 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix ColQwen3.5 pooler projector initialization」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/colqwen3_5.py`；技术摘要: 覆盖「[Bugfix] Fix ColQwen3.5 pooler projector initialization」；主要实现面是 `vllm/model_executor/models/colqwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/colqwen3_5.py` modified +10/-17 (27 lines); hunks: -121,13 +121,13 @@ class ColQwen3_5Model(; -187,7 +187,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: ColQwen3_5Model, __init__, forward, load_weights，涉及 `ColQwen3_5Model, __init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/colqwen3_5.py` modified +10/-17 (27 lines); hunks: -121,13 +121,13 @@ class ColQwen3_5Model(; -187,7 +187,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: ColQwen3_5Model, __init__, forward, load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/colqwen3_5.py
@@ -121,13 +121,13 @@ class ColQwen3_5Model(
-    The model produces per-token embeddings by:
+    The model produces L2-normalized per-token embeddings by:
-    2. Projecting hidden states through a linear layer (hidden_size -> embed_dim)
-    3. L2 normalization is handled by the pooler via PoolerNormalize
+    2. Projection and L2-normalization via the pooler (TokenEmbeddingPoolerHead)
-        custom_text_proj: Linear projection from hidden_size to embed_dim
```

- 已读文件:
  - runtime: `vllm/model_executor/models/colqwen3_5.py` modified +10/-17
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/colqwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #48850 - [Bugfix][LoRA] Add embedding_modules for Qwen3.5 CausalLM

- 链接: https://github.com/vllm-project/vllm/pull/48850
- 状态/时间: merged / 2026-08-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `5a4c8d99242e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-0，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][LoRA] Add embedding_modules for Qwen3.5 CausalLM」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix][LoRA] Add embedding_modules for Qwen3.5 CausalLM」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +5/-0 (5 lines); hunks: -309,6 +309,11 @@ class Qwen3_5ForCausalLMBase(; symbols: Qwen3_5ForCausalLMBase，涉及 `Qwen3_5ForCausalLMBase`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +5/-0 (5 lines); hunks: -309,6 +309,11 @@ class Qwen3_5ForCausalLMBase(; symbols: Qwen3_5ForCausalLMBase
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -309,6 +309,11 @@ class Qwen3_5ForCausalLMBase(
+    # Maps PEFT embed/lm_head LoRA targets onto vLLM embedding wrappers.
+    embedding_modules = {
+        "embed_tokens": "input_embeddings",
+        "lm_head": "output_embeddings",
+    }
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +5/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #52007 - [CI Bug] Fix ci qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/52007
- 状态/时间: merged / 2026-08-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`；关联提交 `0fb168e6ee54`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+2/-2，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI Bug] Fix ci qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`；技术摘要: 覆盖「[CI Bug] Fix ci qwen3.5」；主要实现面是 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` modified +1/-1 (2 lines); hunks: -8,6 +8,6 @@ server_args: >-；`tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` modified +1/-1 (2 lines); hunks: -7,4 +7,4 @@ server_args: >-。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` modified +1/-1 (2 lines); hunks: -8,6 +8,6 @@ server_args: >-
  - `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` modified +1/-1 (2 lines); hunks: -7,4 +7,4 @@ server_args: >-
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml
@@ -8,6 +8,6 @@ server_args: >-
-  --max-num-seqs 384
+  --max-num-seqs 256
diff -- tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml
@@ -7,4 +7,4 @@ server_args: >-
-  --max-num-seqs 512
+  --max-num-seqs 256
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` modified +1/-1; `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50734 - [Bugfix][Model] Fix Qwen3.5 MTP for text-only checkpoints

- 链接: https://github.com/vllm-project/vllm/pull/50734
- 状态/时间: merged / 2026-08-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/test_qwen3_5_mtp_config.py`；关联提交 `900d09f91a1f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+55/-7，可读 patch 77 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] Fix Qwen3.5 MTP for text-only checkpoints」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/models/test_qwen3_5_mtp_config.py`；技术摘要: 覆盖「[Bugfix][Model] Fix Qwen3.5 MTP for text-only checkpoints」；主要实现面是 `tests/models/test_qwen3_5_mtp_config.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/test_qwen3_5_mtp_config.py` added +33/-0 (33 lines); hunks: -0,0 +1,33; symbols: _mtp_config, test_mtp_override_recognizes_text_only_types，涉及 `_mtp_config, test_mtp_override_recognizes_text_only_types`。
- 代码 diff 细节:
  - `tests/models/test_qwen3_5_mtp_config.py` added +33/-0 (33 lines); hunks: -0,0 +1,33; symbols: _mtp_config, test_mtp_override_recognizes_text_only_types
- 关键代码摘录:

```diff
diff -- tests/models/test_qwen3_5_mtp_config.py
@@ -0,0 +1,33 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""CPU-only tests for Qwen3.5 text-only MTP speculative decoding."""
+import pytest
+from transformers import PretrainedConfig
+from vllm.config.speculative import SpeculativeConfig
```

- 已读文件:
  - tests: `tests/models/test_qwen3_5_mtp_config.py` added +33/-0
- 验证与风险: diff 自带测试面 `tests/models/test_qwen3_5_mtp_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51293 - [CI] Re-enable FI autotune in GSM8K config for Qwen3.5-35B-A3B

- 链接: https://github.com/vllm-project/vllm/pull/51293
- 状态/时间: merged / 2026-08-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`；关联提交 `5ac2684976ee`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-1，可读 patch 6 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Re-enable FI autotune in GSM8K config for Qwen3.5-35B-A3B」；模型线: Qwen3.5；类别: 文档/测试/CI；主要 diff: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`；技术摘要: 覆盖「[CI] Re-enable FI autotune in GSM8K config for Qwen3.5-35B-A3B」；主要实现面是 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +0/-1 (1 lines); hunks: -7,4 +7,3 @@ server_args: >-。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +0/-1 (1 lines); hunks: -7,4 +7,3 @@ server_args: >-
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml
@@ -7,4 +7,3 @@ server_args: >-
-  --no-enable-flashinfer-autotune
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +0/-1
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50355 - [Model] Fix weight prefix mapping for native Qwen3.5 text-only checkp…

- 链接: https://github.com/vllm-project/vllm/pull/50355
- 状态/时间: merged / 2026-08-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `febea17f6aa9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+13/-2，可读 patch 36 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Fix weight prefix mapping for native Qwen3.5 text-only checkp…」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Model] Fix weight prefix mapping for native Qwen3.5 text-only checkp…」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +8/-1 (9 lines); hunks: -303,6 +303,13 @@ class Qwen3_5ForCausalLMBase(; -416,7 +423,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: Qwen3_5ForCausalLMBase, __init__, load_weights, Qwen3_5ForCausalLM，涉及 `Qwen3_5ForCausalLMBase, __init__, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +8/-1 (9 lines); hunks: -303,6 +303,13 @@ class Qwen3_5ForCausalLMBase(; -416,7 +423,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: Qwen3_5ForCausalLMBase, __init__, load_weights, Qwen3_5ForCausalLM
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -303,6 +303,13 @@ class Qwen3_5ForCausalLMBase(
+    # Some community text-only checkpoints keep the extraneous
+    # `model.language_model.` prefix inherited from the VL training stack.
+    # Strip it so both prefixed and clean checkpoints load correctly.
+    hf_to_vllm_mapper = WeightsMapper(
+        orig_to_new_prefix={"model.language_model.": "model."},
+    )
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +8/-1
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #50210 - [Model] Support Qwen3.5 text-only dense and MoE models

- 链接: https://github.com/vllm-project/vllm/pull/50210
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `ad5d29db702c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+62/-0，可读 patch 113 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Support Qwen3.5 text-only dense and MoE models」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Model] Support Qwen3.5 text-only dense and MoE models」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +40/-0 (40 lines); hunks: -282,6 +282,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; -361,6 +362,45 @@ def forward(; symbols: load_weights, Qwen3_5ForCausalLMBase, forward, get_mamba_state_dtype_from_config，涉及 `load_weights, Qwen3_5ForCausalLMBase, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +40/-0 (40 lines); hunks: -282,6 +282,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; -361,6 +362,45 @@ def forward(; symbols: load_weights, Qwen3_5ForCausalLMBase, forward, get_mamba_state_dtype_from_config
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -282,6 +282,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+    IsHybrid,
@@ -361,6 +362,45 @@ def forward(
+    @classmethod
+    def get_mamba_state_dtype_from_config(
+        cls,
+        vllm_config: "VllmConfig",
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +40/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #49881 - [CI] Increase Qwen3.5 MTP GSM8K generation length

- 链接: https://github.com/vllm-project/vllm/pull/49881
- 状态/时间: merged / 2026-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`；关联提交 `25ace8fe5df0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Increase Qwen3.5 MTP GSM8K generation length」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`；技术摘要: 覆盖「[CI] Increase Qwen3.5 MTP GSM8K generation length」；主要实现面是 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` modified +2/-1 (3 lines); hunks: -3,8 +3,9 @@ accuracy_threshold: 0.88。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` modified +2/-1 (3 lines); hunks: -3,8 +3,9 @@ accuracy_threshold: 0.88
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml
@@ -3,8 +3,9 @@ accuracy_threshold: 0.88
+max_tokens: 12000
-  --max-model-len 4096
+  --max-model-len 16384
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #48912 - [Model] Enable EVS for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/48912
- 状态/时间: merged / 2026-07-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `dbccc5ae328d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+32/-12，可读 patch 79 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Enable EVS for Qwen3.5」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Model] Enable EVS for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +32/-12 (44 lines); hunks: -53,6 +53,7; -397,8 +398,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, Qwen3_5ForConditionalGeneration, embed_input_ids, recompute_mrope_positions，涉及 `__init__, Qwen3_5ForConditionalGeneration, embed_input_ids`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +32/-12 (44 lines); hunks: -53,6 +53,7; -397,8 +398,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, Qwen3_5ForConditionalGeneration, embed_input_ids, recompute_mrope_positions
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -53,6 +53,7 @@
+from vllm.tokenizers.registry import cached_tokenizer_from_config
@@ -397,8 +398,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-    # Qwen3.5 does not support multimodal pruning (EVS).
-    supports_multimodal_pruning = False
+    supports_multimodal_pruning = True
@@ -416,8 +416,21 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +32/-12
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #49372 - [Bugfix] Respect declared attention contract for ColQwen3.5 retrievers

- 链接: https://github.com/vllm-project/vllm/pull/49372
- 状态/时间: merged / 2026-07-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/models/multimodal/pooling/test_colqwen3_5.py`；关联提交 `1240c74c0a47`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+135/-16，可读 patch 180 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Respect declared attention contract for ColQwen3.5 retrievers」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/models/multimodal/pooling/test_colqwen3_5.py`；技术摘要: 覆盖「[Bugfix] Respect declared attention contract for ColQwen3.5 retrievers」；主要实现面是 `tests/models/multimodal/pooling/test_colqwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/pooling/test_colqwen3_5.py` modified +103/-8 (111 lines); hunks: -7,6 +7,8; -154,19 +156,112 @@ def test_colqwen3_5_relevance_ordering(; symbols: test_colqwen3_5_relevance_ordering, test_colqwen3_5_config_enables_bidirectional_attention, test_colqwen3_5_config_applies_declared_attention_contract, test_colqwen3_5_config_rejects_invalid_attention_contract，涉及 `test_colqwen3_5_relevance_ordering, test_colqwen3_5_config_enables_bidirectional_attention, test_colqwen3_5_config_applies_declared_attention_contract`。
- 代码 diff 细节:
  - `tests/models/multimodal/pooling/test_colqwen3_5.py` modified +103/-8 (111 lines); hunks: -7,6 +7,8; -154,19 +156,112 @@ def test_colqwen3_5_relevance_ordering(; symbols: test_colqwen3_5_relevance_ordering, test_colqwen3_5_config_enables_bidirectional_attention, test_colqwen3_5_config_applies_declared_attention_contract, test_colqwen3_5_config_rejects_invalid_attention_contract
- 关键代码摘录:

```diff
diff -- tests/models/multimodal/pooling/test_colqwen3_5.py
@@ -7,6 +7,8 @@
+from types import SimpleNamespace
@@ -154,19 +156,112 @@ def test_colqwen3_5_relevance_ordering(
-def test_colqwen3_5_config_enables_bidirectional_attention() -> None:
-    """ColQwen3.5 retrieval must be served BIDIRECTIONAL (is_causal=False) so the
-    full_attention layers build with AttentionType.ENCODER_ONLY. This guards the
-    silent-causal regression (no GPU / model load needed)."""
```

- 已读文件:
  - tests: `tests/models/multimodal/pooling/test_colqwen3_5.py` modified +103/-8
- 验证与风险: diff 自带测试面 `tests/models/multimodal/pooling/test_colqwen3_5.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #48816 - Fix GPTQ quantized Qwen3.5 MTP weight loading with spec decode

- 链接: https://github.com/vllm-project/vllm/pull/48816
- 状态/时间: merged / 2026-07-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `c8db00b16cc1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-2，可读 patch 38 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix GPTQ quantized Qwen3.5 MTP weight loading with spec decode」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5_mtp.py`；技术摘要: 覆盖「Fix GPTQ quantized Qwen3.5 MTP weight loading with spec decode」；主要实现面是 `vllm/model_executor/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5_mtp.py` modified +12/-2 (14 lines); hunks: -103,6 +103,16 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; -111,11 +121,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +12/-2 (14 lines); hunks: -103,6 +103,16 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; -111,11 +121,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -103,6 +103,16 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
+        # GPTQ: quantized checkpoints may exclude MTP from quantization via
+        # quantization_config.dynamic with "-:pattern" entries. When detected,
+        # disable quantization for MTP layers so they use unquantized params.
+        original_quant = vllm_config.quant_config
+        if quant_config and quant_config.get_name() not in ("modelopt_fp4",):
+            hf_qc = getattr(model_config.hf_config, "quantization_config", None)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5_mtp.py` modified +12/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #44434 - [ROCm][Bugfix][Perf] enable shared expert fusion for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/44434
- 状态/时间: merged / 2026-06-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `80e511772f3e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+48/-4，可读 patch 87 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix][Perf] enable shared expert fusion for Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[ROCm][Bugfix][Perf] enable shared expert fusion for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +19/-0 (19 lines); hunks: -30,6 +30,7; -314,6 +315,15 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +19/-0 (19 lines); hunks: -30,6 +30,7; -314,6 +315,15 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -30,6 +30,7 @@
+from vllm._aiter_ops import rocm_aiter_ops
@@ -314,6 +315,15 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+        from vllm.config import get_current_vllm_config
+        from .qwen3_next import _is_shared_expert_fse_compatible
+        is_fse = (
+            rocm_aiter_ops.is_fusion_moe_shared_experts_enabled()
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +19/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46520 - [ROCm][CI] Shard LM Eval Qwen3-5 Models (B200-MI355) in AMD CI

- 链接: https://github.com/vllm-project/vllm/pull/46520
- 状态/时间: merged / 2026-06-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`；关联提交 `b28103e1ca8b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+5/-3，可读 patch 33 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Shard LM Eval Qwen3-5 Models (B200-MI355) in AMD CI」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`；技术摘要: 覆盖「[ROCm][CI] Shard LM Eval Qwen3-5 Models (B200-MI355) in AMD CI」；主要实现面是 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml` modified +1/-0 (1 lines); hunks: -3,6 +3,7 @@ accuracy_threshold: 0.89。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml` modified +1/-0 (1 lines); hunks: -3,6 +3,7 @@ accuracy_threshold: 0.89
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml
@@ -3,6 +3,7 @@ accuracy_threshold: 0.89
+startup_max_wait_seconds: 3600
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #46108 - [Model] ColQwen3.5: fix retrieval correctness (bias + bidirectional)

- 链接: https://github.com/vllm-project/vllm/pull/46108
- 状态/时间: merged / 2026-06-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/pooling/score/colqwen3_5_rerank_online.py`, `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/models/colqwen3_5.py`；关联提交 `3c8e49596c3f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+79/-5，可读 patch 167 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] ColQwen3.5: fix retrieval correctness (bias + bidirectional)」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/models/colqwen3_5.py`, `examples/pooling/score/colqwen3_5_rerank_online.py`；技术摘要: 覆盖「[Model] ColQwen3.5: fix retrieval correctness (bias + bidirectional)」；主要实现面是 `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/models/colqwen3_5.py`, `examples/pooling/score/colqwen3_5_rerank_online.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/models/multimodal/pooling/test_colqwen3_5.py` modified +18/-0 (18 lines); hunks: -152,3 +152,21 @@ def test_colqwen3_5_relevance_ordering(; symbols: test_colqwen3_5_relevance_ordering, test_colqwen3_5_config_enables_bidirectional_attention，涉及 `test_colqwen3_5_relevance_ordering, test_colqwen3_5_config_enables_bidirectional_attention`；`vllm/model_executor/models/colqwen3_5.py` modified +9/-1 (10 lines); hunks: -15,6 +15,7; -166,12 +167,19 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`；`examples/pooling/score/colqwen3_5_rerank_online.py` modified +17/-1 (18 lines); hunks: -7,11 +7,27。
- 代码 diff 细节:
  - `tests/models/multimodal/pooling/test_colqwen3_5.py` modified +18/-0 (18 lines); hunks: -152,3 +152,21 @@ def test_colqwen3_5_relevance_ordering(; symbols: test_colqwen3_5_relevance_ordering, test_colqwen3_5_config_enables_bidirectional_attention
  - `vllm/model_executor/models/colqwen3_5.py` modified +9/-1 (10 lines); hunks: -15,6 +15,7; -166,12 +167,19 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
  - `examples/pooling/score/colqwen3_5_rerank_online.py` modified +17/-1 (18 lines); hunks: -7,11 +7,27
- 关键代码摘录:

```diff
diff -- tests/models/multimodal/pooling/test_colqwen3_5.py
@@ -152,3 +152,21 @@ def test_colqwen3_5_relevance_ordering(
+def test_colqwen3_5_config_enables_bidirectional_attention() -> None:
+    """ColQwen3.5 retrieval must be served BIDIRECTIONAL (is_causal=False) so the
+    full_attention layers build with AttentionType.ENCODER_ONLY. This guards the
+    silent-causal regression (no GPU / model load needed)."""
+    from types import SimpleNamespace
+    from vllm.model_executor.models.config import (
diff -- vllm/model_executor/models/colqwen3_5.py
@@ -15,6 +15,7 @@
+- vultr/VultronRetrieverPrime-Qwen3.5-8B
@@ -166,12 +167,19 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
+        # ColPali defines `custom_text_proj = nn.Linear(hidden, dim)`, i.e.
+        # bias=True by default, and the trained ColQwen3.5 checkpoints ship a
+        # `custom_text_proj.bias`. Construct with a bias and zero-initialize it:
+        # a (legacy) bias-less checkpoint then behaves identically to bias=False,
diff -- examples/pooling/score/colqwen3_5_rerank_online.py
@@ -7,11 +7,27 @@
```

- 已读文件:
  - tests: `tests/models/multimodal/pooling/test_colqwen3_5.py` modified +18/-0
  - runtime: `vllm/model_executor/models/colqwen3_5.py` modified +9/-1
  - docs: `examples/pooling/score/colqwen3_5_rerank_online.py` modified +17/-1
- 验证与风险: diff 自带测试面 `tests/models/multimodal/pooling/test_colqwen3_5.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45002 - [Bugfix] fix qwen3.5 ep weight loading

- 链接: https://github.com/vllm-project/vllm/pull/45002
- 状态/时间: merged / 2026-06-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `ca4cfd873163`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+32/-14，可读 patch 72 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] fix qwen3.5 ep weight loading」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`；技术摘要: 覆盖「[Bugfix] fix qwen3.5 ep weight loading」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +17/-7 (24 lines); hunks: -36,6 +36,9; -294,13 +297,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`；`vllm/model_executor/models/qwen3_5_mtp.py` modified +14/-7 (21 lines); hunks: -209,13 +209,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights，涉及 `load_weights`；`tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +1/-0 (1 lines); hunks: -7,3 +7,4 @@ server_args: >-。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +17/-7 (24 lines); hunks: -36,6 +36,9; -294,13 +297,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +14/-7 (21 lines); hunks: -209,13 +209,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: load_weights
  - `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +1/-0 (1 lines); hunks: -7,3 +7,4 @@ server_args: >-
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -36,6 +36,9 @@
+from vllm.model_executor.layers.fused_moe import (
+    fused_moe_make_expert_params_mapping,
+)
@@ -294,13 +297,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-        base_layer = (
-            "base_layer." if any(".base_layer." in name for name in params_dict) else ""
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -209,13 +209,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
-        base_layer = (
-            "base_layer." if any(".base_layer." in name for name in params_dict) else ""
-        )
-        fused_expert_params_mapping = [
-            (f"experts.{base_layer}w13_weight", "experts.gate_up_proj", 0, "w1"),
-            (f"experts.{base_layer}w2_weight", "experts.down_proj", 0, "w2"),
diff -- tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml
@@ -7,3 +7,4 @@ server_args: >-
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +17/-7; `vllm/model_executor/models/qwen3_5_mtp.py` modified +14/-7
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44700 - [PERF] [Qwen3.5] Split mixed prefill+decode batches: route decodes to the recurrent kernel

- 链接: https://github.com/vllm-project/vllm/pull/44700
- 状态/时间: merged / 2026-06-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt`；关联提交 `fa27d4e9cf3c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+426/-31，可读 patch 625 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[PERF] [Qwen3.5] Split mixed prefill+decode batches: route decodes to the recurrent kernel」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt`；技术摘要: 覆盖「[PERF] [Qwen3.5] Split mixed prefill+decode batches: route decodes to the recurrent kernel」；主要实现面是 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` added +12/-0 (12 lines); hunks: -0,0 +1,12；`tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` modified +2/-1 (3 lines); hunks: -1,3 +1,4。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` added +12/-0 (12 lines); hunks: -0,0 +1,12
  - `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` modified +2/-1 (3 lines); hunks: -1,3 +1,4
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml
@@ -0,0 +1,12 @@
+model_name: "nvidia/Qwen3.5-397B-A17B-NVFP4"
+accuracy_threshold: 0.88
+tolerance: 0.03
+num_questions: 1319
+num_fewshot: 5
+server_args: >-
diff -- tests/evals/gsm8k/configs/models-qwen35-blackwell.txt
@@ -1,3 +1,4 @@
-Qwen3.5-397B-A17B-NVFP4-DEP2.yaml
+Qwen3.5-397B-A17B-NVFP4-DEP2.yaml
+Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml` added +12/-0; `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` modified +2/-1
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt`, `tests/kernels/mamba/test_gdn_forward_core_split.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #42716 - Fix Weight loading for Qwen3.5-MTP and Qwen3-VL using runai_streamer

- 链接: https://github.com/vllm-project/vllm/pull/42716
- 状态/时间: merged / 2026-05-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `a94189295b8b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-4，可读 patch 22 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Weight loading for Qwen3.5-MTP and Qwen3-VL using runai_streamer」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5_mtp.py`；技术摘要: 覆盖「Fix Weight loading for Qwen3.5-MTP and Qwen3-VL using runai_streamer」；主要实现面是 `vllm/model_executor/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5_mtp.py` modified +2/-2 (4 lines); hunks: -175,8 +175,8 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights，涉及 `load_fused_expert_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +2/-2 (4 lines); hunks: -175,8 +175,8 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -175,8 +175,8 @@ def load_fused_expert_weights(
-                shard_id,
-                expert_id,
+                shard_id=shard_id,
+                expert_id=expert_id,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5_mtp.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_vl_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42521 - [Fix] Weight loading for qwen3_5 using runai_streamer

- 链接: https://github.com/vllm-project/vllm/pull/42521
- 状态/时间: merged / 2026-05-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `ca60a4e84f9a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Weight loading for qwen3_5 using runai_streamer」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Fix] Weight loading for qwen3_5 using runai_streamer」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +2/-2 (4 lines); hunks: -262,8 +262,8 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights，涉及 `load_fused_expert_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +2/-2 (4 lines); hunks: -262,8 +262,8 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -262,8 +262,8 @@ def load_fused_expert_weights(
-                shard_id,
-                expert_id,
+                shard_id=shard_id,
+                expert_id=expert_id,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42151 - [MM][Perf][CG] Support ViT full CUDA graph for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/42151
- 状态/时间: merged / 2026-05-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `92def124bcb7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+112/-5，可读 patch 187 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MM][Perf][CG] Support ViT full CUDA graph for Qwen3.5」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[MM][Perf][CG] Support ViT full CUDA graph for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +2/-0 (2 lines); hunks: -565,6 +565,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; -778,6 +779,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +2/-0 (2 lines); hunks: -565,6 +565,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; -778,6 +779,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -565,6 +565,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
+        self.model_config = vllm_config.model_config
@@ -778,6 +779,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
+        self.model_config = vllm_config.model_config
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/generation/test_vit_cudagraph.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37912 - [Bugfix] Fuse Qwen3.5 in_qkvz_proj forwarding with LoRA enabled

- 链接: https://github.com/vllm-project/vllm/pull/37912
- 状态/时间: merged / 2026-05-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `48698b1b9b30`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+84/-111，可读 patch 341 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fuse Qwen3.5 in_qkvz_proj forwarding with LoRA enabled」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Fuse Qwen3.5 in_qkvz_proj forwarding with LoRA enabled」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +4/-43 (47 lines); hunks: -138,7 +138,6 @@ def __init__(; -217,7 +216,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, load_fused_expert_weights, load_weights，涉及 `__init__, load_fused_expert_weights, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +4/-43 (47 lines); hunks: -138,7 +138,6 @@ def __init__(; -217,7 +216,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, load_fused_expert_weights, load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -138,7 +138,6 @@ def __init__(
-                create_in_proj_qkvz=vllm_config.lora_config is None,
@@ -217,7 +216,6 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-        self.enable_lora = vllm_config.lora_config is not None
@@ -276,6 +274,9 @@ def load_fused_expert_weights(
+            # GDN
+            ("in_proj_qkvz", "in_proj_qkv", (0, 1, 2)),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +4/-43
- 验证与风险: runtime 路径改动集中在 `vllm/lora/layers/column_parallel_linear.py`, `vllm/lora/model_manager.py`, `vllm/model_executor/layers/mamba/gdn_linear_attn.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37114 - [Bugfix] LoRA: extend expert base_layer loading to Qwen3.5 and Step3.x

- 链接: https://github.com/vllm-project/vllm/pull/37114
- 状态/时间: merged / 2026-04-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `908a713488db`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+34/-16，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] LoRA: extend expert base_layer loading to Qwen3.5 and Step3.x」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[Bugfix] LoRA: extend expert base_layer loading to Qwen3.5 and Step3.x」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +5/-2 (7 lines); hunks: -306,9 +306,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`；`vllm/model_executor/models/qwen3_5_mtp.py` modified +5/-2 (7 lines); hunks: -207,9 +207,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +5/-2 (7 lines); hunks: -306,9 +306,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +5/-2 (7 lines); hunks: -207,9 +207,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -306,9 +306,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+        base_layer = (
+            "base_layer." if any(".base_layer." in name for name in params_dict) else ""
+        )
-            ("experts.w13_weight", "experts.gate_up_proj", 0, "w1"),
-            ("experts.w2_weight", "experts.down_proj", 0, "w2"),
+            (f"experts.{base_layer}w13_weight", "experts.gate_up_proj", 0, "w1"),
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -207,9 +207,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+        base_layer = (
+            "base_layer." if any(".base_layer." in name for name in params_dict) else ""
+        )
-            ("experts.w13_weight", "experts.gate_up_proj", 0, "w1"),
-            ("experts.w2_weight", "experts.down_proj", 0, "w2"),
+            (f"experts.{base_layer}w13_weight", "experts.gate_up_proj", 0, "w1"),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +5/-2; `vllm/model_executor/models/qwen3_5_mtp.py` modified +5/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_vl_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #38927 - [Bugfix][LoRA] Fix missing in_proj_z in Qwen3_5ForConditionalGenerati…

- 链接: https://github.com/vllm-project/vllm/pull/38927
- 状态/时间: merged / 2026-04-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `81994e1d0ea6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][LoRA] Fix missing in_proj_z in Qwen3_5ForConditionalGenerati…」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix][LoRA] Fix missing in_proj_z in Qwen3_5ForConditionalGenerati…」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +1/-0 (1 lines); hunks: -620,6 +620,7 @@ def update_packed_mapping(self, enable_lora: bool):; symbols: update_packed_mapping, embed_input_ids，涉及 `update_packed_mapping, embed_input_ids`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +1/-0 (1 lines); hunks: -620,6 +620,7 @@ def update_packed_mapping(self, enable_lora: bool):; symbols: update_packed_mapping, embed_input_ids
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -620,6 +620,7 @@ def update_packed_mapping(self, enable_lora: bool):
+            self.packed_modules_mapping["in_proj_z"] = ["in_proj_z"]
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #38664 - [CI][ROCm] Add Qwen3.5-35B-A3B-MXFP4 model eval into CI

- 链接: https://github.com/vllm-project/vllm/pull/38664
- 状态/时间: merged / 2026-04-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`；关联提交 `201d2ea5bfb9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+9/-0，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][ROCm] Add Qwen3.5-35B-A3B-MXFP4 model eval into CI」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`；技术摘要: 覆盖「[CI][ROCm] Add Qwen3.5-35B-A3B-MXFP4 model eval into CI」；主要实现面是 `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` modified +1/-0 (1 lines); hunks: -1 +1,2。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` modified +1/-0 (1 lines); hunks: -1 +1,2
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/models-qwen35-mi355.txt
@@ -1 +1,2 @@
+Qwen3.5-35B-A3B-MXFP4-TP2.yaml
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-TP2.yaml`, `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38832 - [Bugfix] Fix NVFP4+MTP crash: force unquantized mtp.fc for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/38832
- 状态/时间: merged / 2026-04-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `771913e4a024`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-1，可读 patch 24 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix NVFP4+MTP crash: force unquantized mtp.fc for Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[Bugfix] Fix NVFP4+MTP crash: force unquantized mtp.fc for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5_mtp.py` modified +10/-1 (11 lines); hunks: -75,13 +75,22 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +10/-1 (11 lines); hunks: -75,13 +75,22 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -75,13 +75,22 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
+        # Workaround: mtp.fc is stored as BF16 in NVFP4 checkpoints but is
+        # missing from hf_quant_config.json exclude_modules. Force unquantized.
+        # Ref: https://github.com/vllm-project/vllm/pull/38650
+        # Ref: https://github.com/NVIDIA/Model-Optimizer/pull/1124
+        fc_quant = (
+            None
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5_mtp.py` modified +10/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #38632 - [CI] fix LM Eval Qwen3.5 Models (B200)

- 链接: https://github.com/vllm-project/vllm/pull/38632
- 状态/时间: merged / 2026-03-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`；关联提交 `ea7bfde6e40d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 5 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] fix LM Eval Qwen3.5 Models (B200)」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`；技术摘要: 覆盖「[CI] fix LM Eval Qwen3.5 Models (B200)」；主要实现面是 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` modified +1/-0 (1 lines); hunks: -7,3 +7,4 @@ server_args: >-。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` modified +1/-0 (1 lines); hunks: -7,3 +7,4 @@ server_args: >-
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml
@@ -7,3 +7,4 @@ server_args: >-
+  --max-num-seqs 512
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` modified +1/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37975 - [Model] Extract GatedDeltaNetAttention into shared layer for Qwen3Next and Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/37975
- 状态/时间: merged / 2026-03-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `a8eab8f30dda`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+1053/-1126，可读 patch 2304 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Extract GatedDeltaNetAttention into shared layer for Qwen3Next and Qwen3.5」；模型线: Qwen3.5；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Model] Extract GatedDeltaNetAttention into shared layer for Qwen3Next and Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +4/-151 (155 lines); hunks: -28,7 +28,6; -40,18 +39,14; symbols: get_hf_config, Qwen3_5GatedDeltaNet, fix_query_key_value_ordering, __init__，涉及 `get_hf_config, Qwen3_5GatedDeltaNet, fix_query_key_value_ordering`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +4/-151 (155 lines); hunks: -28,7 +28,6; -40,18 +39,14; symbols: get_hf_config, Qwen3_5GatedDeltaNet, fix_query_key_value_ordering, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -28,7 +28,6 @@
-from einops import rearrange
@@ -40,18 +39,14 @@
-from vllm.model_executor.layers.linear import (
-    ColumnParallelLinear,
-    MergedColumnParallelLinear,
-)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +4/-151
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/gdn_linear_attn.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #38155 - [ROCm][CI] Add LM Eval Qwen3.5 Models test for MI355

- 链接: https://github.com/vllm-project/vllm/pull/38155
- 状态/时间: merged / 2026-03-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`；关联提交 `9c3ae04bfe65`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+25/-0，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Add LM Eval Qwen3.5 Models test for MI355」；模型线: Qwen3.5；类别: 文档/测试/CI；主要 diff: `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`；技术摘要: 覆盖「[ROCm][CI] Add LM Eval Qwen3.5 Models test for MI355」；主要实现面是 `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` added +1/-0 (1 lines); hunks: -0,0 +1。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` added +1/-0 (1 lines); hunks: -0,0 +1
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/models-qwen35-mi355.txt
@@ -0,0 +1 @@
+Qwen3.5-35B-A3B-DEP2.yaml
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` added +1/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/models-qwen35-mi355.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38083 - [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell

- 链接: https://github.com/vllm-project/vllm/pull/38083
- 状态/时间: merged / 2026-03-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt`；关联提交 `52069012fe53`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+69/-11，可读 patch 177 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml`；技术摘要: 覆盖「[Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell」；主要实现面是 `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` added +9/-0 (9 lines); hunks: -0,0 +1,9；`tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +2/-1 (3 lines); hunks: -1,5 +1,6；`tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml` modified +2/-1 (3 lines); hunks: -1,5 +1,6；`tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` modified +2/-0 (2 lines); hunks: -1 +1,3。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` added +9/-0 (9 lines); hunks: -0,0 +1,9
  - `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +2/-1 (3 lines); hunks: -1,5 +1,6
  - `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml` modified +2/-1 (3 lines); hunks: -1,5 +1,6
  - `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` modified +2/-0 (2 lines); hunks: -1 +1,3
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml
@@ -0,0 +1,9 @@
+model_name: "nvidia/Qwen3.5-397B-A17B-NVFP4"
+accuracy_threshold: 0.88
+tolerance: 0.03
+num_questions: 1319
+num_fewshot: 5
+server_args: >-
diff -- tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml
@@ -1,5 +1,6 @@
-accuracy_threshold: 0.86
+accuracy_threshold: 0.84
+tolerance: 0.03
diff -- tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml
@@ -1,5 +1,6 @@
-accuracy_threshold: 0.86
+accuracy_threshold: 0.79
+tolerance: 0.03
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml` added +9/-0; `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml` modified +2/-1; `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml` modified +2/-1; `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt` modified +2/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-FP8-DEP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37816 - [CI/Build][LoRA] Update Qwen35 LoRA testing

- 链接: https://github.com/vllm-project/vllm/pull/37816
- 状态/时间: merged / 2026-03-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/lora/test_qwen35_densemodel_lora.py`；关联提交 `1f0d21064137`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+369/-135，可读 patch 529 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI/Build][LoRA] Update Qwen35 LoRA testing」；模型线: Qwen3.5；类别: 文档/测试/CI；主要 diff: `tests/lora/test_qwen35_densemodel_lora.py`；技术摘要: 覆盖「[CI/Build][LoRA] Update Qwen35 LoRA testing」；主要实现面是 `tests/lora/test_qwen35_densemodel_lora.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/lora/test_qwen35_densemodel_lora.py` added +361/-0 (361 lines); hunks: -0,0 +1,361; symbols: _assert_exact_outputs, _assert_prefix_outputs, _run_text_lora_sample, _run_vl_lora_sample，涉及 `_assert_exact_outputs, _assert_prefix_outputs, _run_text_lora_sample`。
- 代码 diff 细节:
  - `tests/lora/test_qwen35_densemodel_lora.py` added +361/-0 (361 lines); hunks: -0,0 +1,361; symbols: _assert_exact_outputs, _assert_prefix_outputs, _run_text_lora_sample, _run_vl_lora_sample
- 关键代码摘录:

```diff
diff -- tests/lora/test_qwen35_densemodel_lora.py
@@ -0,0 +1,361 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from transformers import AutoTokenizer
+import vllm
+import vllm.config
+from vllm.assets.image import ImageAsset
```

- 已读文件:
  - tests: `tests/lora/test_qwen35_densemodel_lora.py` added +361/-0
- 验证与风险: diff 自带测试面 `tests/lora/conftest.py`, `tests/lora/test_qwen35_densemodel_lora.py`, `tests/lora/test_qwen35_densemoel_lora.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36976 - [Bugfix][LoRA] Fix Qwen35 LoRA

- 链接: https://github.com/vllm-project/vllm/pull/36976
- 状态/时间: merged / 2026-03-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `8fbe3f303fbf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+257/-46，可读 patch 464 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][LoRA] Fix Qwen35 LoRA」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix][LoRA] Fix Qwen35 LoRA」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +100/-23 (123 lines); hunks: -32,17 +32,18; -130,6 +131,40 @@ def fix_query_key_value_ordering(; symbols: fix_query_key_value_ordering, __init__, create_qkvz_proj, forward，涉及 `fix_query_key_value_ordering, __init__, create_qkvz_proj`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +100/-23 (123 lines); hunks: -32,17 +32,18; -130,6 +131,40 @@ def fix_query_key_value_ordering(; symbols: fix_query_key_value_ordering, __init__, create_qkvz_proj, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -32,17 +32,18 @@
-from vllm.config import (
-    VllmConfig,
-)
+from vllm.config import VllmConfig
-from vllm.model_executor.layers.linear import MergedColumnParallelLinear
+from vllm.model_executor.layers.linear import (
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +100/-23
- 验证与风险: diff 自带测试面 `tests/lora/conftest.py`, `tests/lora/test_qwen35_densemoel_lora.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37448 - Fix AttributeError in Qwen3.5 GDN layers with quantized models

- 链接: https://github.com/vllm-project/vllm/pull/37448
- 状态/时间: merged / 2026-03-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `4120a05ff1d0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-4，可读 patch 22 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix AttributeError in Qwen3.5 GDN layers with quantized models」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「Fix AttributeError in Qwen3.5 GDN layers with quantized models」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +2/-2 (4 lines); hunks: -182,8 +182,8 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +2/-2 (4 lines); hunks: -182,8 +182,8 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -182,8 +182,8 @@ def forward(
-            self.in_proj_qkvz.weight.shape[0],
-            self.in_proj_ba.weight.shape[0],
+            sum(self.in_proj_qkvz.output_sizes) // self.tp_size,
+            sum(self.in_proj_ba.output_sizes) // self.tp_size,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #36887 - [Model] Add ColQwen3.5 4.5B support

- 链接: https://github.com/vllm-project/vllm/pull/36887
- 状态/时间: merged / 2026-03-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/pooling/score/colqwen3_5_rerank_online.py`, `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/models/colqwen3_5.py`；关联提交 `c0745a851a4f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+579/-0，可读 patch 619 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add ColQwen3.5 4.5B support」；模型线: Qwen3.5；类别: 文档/测试/CI；主要 diff: `vllm/model_executor/models/colqwen3_5.py`, `tests/models/multimodal/pooling/test_colqwen3_5.py`, `examples/pooling/score/colqwen3_5_rerank_online.py`；技术摘要: 覆盖「[Model] Add ColQwen3.5 4.5B support」；主要实现面是 `vllm/model_executor/models/colqwen3_5.py`, `tests/models/multimodal/pooling/test_colqwen3_5.py`, `examples/pooling/score/colqwen3_5_rerank_online.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/colqwen3_5.py` added +246/-0 (246 lines); hunks: -0,0 +1,246; symbols: ColQwen3_5ProcessingInfo, get_hf_config, get_hf_processor, _supports_video，涉及 `ColQwen3_5ProcessingInfo, get_hf_config, get_hf_processor`；`tests/models/multimodal/pooling/test_colqwen3_5.py` added +154/-0 (154 lines); hunks: -0,0 +1,154; symbols: _run_token_embed_test, _run_late_interaction_test, _run_relevance_test, test_colqwen3_5_token_embed，涉及 `_run_token_embed_test, _run_late_interaction_test, _run_relevance_test`；`examples/pooling/score/colqwen3_5_rerank_online.py` added +130/-0 (130 lines); hunks: -0,0 +1,130; symbols: rerank_text, score_text, score_text_top_n, main，涉及 `rerank_text, score_text, score_text_top_n`。
- 代码 diff 细节:
  - `vllm/model_executor/models/colqwen3_5.py` added +246/-0 (246 lines); hunks: -0,0 +1,246; symbols: ColQwen3_5ProcessingInfo, get_hf_config, get_hf_processor, _supports_video
  - `tests/models/multimodal/pooling/test_colqwen3_5.py` added +154/-0 (154 lines); hunks: -0,0 +1,154; symbols: _run_token_embed_test, _run_late_interaction_test, _run_relevance_test, test_colqwen3_5_token_embed
  - `examples/pooling/score/colqwen3_5_rerank_online.py` added +130/-0 (130 lines); hunks: -0,0 +1,130; symbols: rerank_text, score_text, score_text_top_n, main
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/colqwen3_5.py
@@ -0,0 +1,246 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""
+ColQwen3.5 late interaction model for multi-modal retrieval and reranking.
+ColQwen3.5 extends Qwen3.5 with a ColBERT-style late interaction head,
+producing per-token embeddings for both text and image inputs. It uses
diff -- tests/models/multimodal/pooling/test_colqwen3_5.py
@@ -0,0 +1,154 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Tests for ColQwen3.5 late interaction model for multi-modal retrieval.
+ColQwen3.5 is a multi-vector retrieval model based on Qwen3.5 backbone with
+ColBERT-style late interaction scoring (MaxSim). It produces per-token
+embeddings for both text and image inputs.
diff -- examples/pooling/score/colqwen3_5_rerank_online.py
@@ -0,0 +1,130 @@
```

- 已读文件:
  - runtime: `vllm/model_executor/models/colqwen3_5.py` added +246/-0
  - tests: `tests/models/multimodal/pooling/test_colqwen3_5.py` added +154/-0
  - docs: `examples/pooling/score/colqwen3_5_rerank_online.py` added +130/-0
- 验证与风险: diff 自带测试面 `tests/models/multimodal/pooling/test_colqwen3_5.py`, `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36658 - Add: Eagle3 support for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/36658
- 状态/时间: merged / 2026-03-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `9d07a3d6e472`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+25/-2，可读 patch 83 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add: Eagle3 support for Qwen3.5」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「Add: Eagle3 support for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +11/-0 (11 lines); hunks: -75,6 +75,7; -353,6 +354,8 @@ def get_layer(prefix: str):; symbols: get_layer, load_fused_expert_weights, load_weights, Qwen3_5ForCausalLMBase，涉及 `get_layer, load_fused_expert_weights, load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +11/-0 (11 lines); hunks: -75,6 +75,7; -353,6 +354,8 @@ def get_layer(prefix: str):; symbols: get_layer, load_fused_expert_weights, load_weights, Qwen3_5ForCausalLMBase
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -75,6 +75,7 @@
+    SupportsEagle3,
@@ -353,6 +354,8 @@ def get_layer(prefix: str):
+        self.aux_hidden_state_layers: tuple[int, ...] = ()
@@ -536,6 +539,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+    SupportsEagle3,
@@ -592,6 +596,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +11/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35617 - [Bugfix][Model] Fix Qwen3.5/Qwen3Next ignoring --dtype flag on older GPUs

- 链接: https://github.com/vllm-project/vllm/pull/35617
- 状态/时间: merged / 2026-03-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `afd089f231d7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+0/-5，可读 patch 40 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Model] Fix Qwen3.5/Qwen3Next ignoring --dtype flag on older GPUs」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix][Model] Fix Qwen3.5/Qwen3Next ignoring --dtype flag on older GPUs」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +0/-2 (2 lines); hunks: -274,15 +274,13 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +0/-2 (2 lines); hunks: -274,15 +274,13 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -274,15 +274,13 @@ def __init__(
-                    dtype=config.dtype,
-                    dtype=config.dtype,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +0/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35581 - Fix Qwen3_5MTP packed_modules_mapping for gate_up_proj

- 链接: https://github.com/vllm-project/vllm/pull/35581
- 状态/时间: merged / 2026-02-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `63d7972f13d1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Qwen3_5MTP packed_modules_mapping for gate_up_proj」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5_mtp.py`；技术摘要: 覆盖「Fix Qwen3_5MTP packed_modules_mapping for gate_up_proj」；主要实现面是 `vllm/model_executor/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5_mtp.py` modified +1/-1 (2 lines); hunks: -339,7 +339,7 @@ class Qwen3_5MTP(nn.Module, SupportsMultiModal):; symbols: Qwen3_5MTP, __init__，涉及 `Qwen3_5MTP, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +1/-1 (2 lines); hunks: -339,7 +339,7 @@ class Qwen3_5MTP(nn.Module, SupportsMultiModal):; symbols: Qwen3_5MTP, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -339,7 +339,7 @@ class Qwen3_5MTP(nn.Module, SupportsMultiModal):
-        "gate_up_proj": ["up_proj", "down_proj"],
+        "gate_up_proj": ["gate_proj", "up_proj"],
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5_mtp.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34719 - [Bugfix] Qwen3.5 kv-scale weight remapping

- 链接: https://github.com/vllm-project/vllm/pull/34719
- 状态/时间: merged / 2026-02-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `6fff24f30fe2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-0，可读 patch 21 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Qwen3.5 kv-scale weight remapping」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Qwen3.5 kv-scale weight remapping」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +7/-0 (7 lines); hunks: -57,6 +57,7; -397,6 +398,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +7/-0 (7 lines); hunks: -57,6 +57,7; -397,6 +398,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -57,6 +57,7 @@
+    maybe_remap_kv_scale_name,
@@ -397,6 +398,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+            # Remapping the name of FP8 kv-scale.
+            if name.endswith("scale"):
+                name = maybe_remap_kv_scale_name(name, params_dict)
+                if name is None:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34697 - [Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion

- 链接: https://github.com/vllm-project/vllm/pull/34697
- 状态/时间: merged / 2026-02-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `c0bd8b13da36`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+102/-192，可读 patch 477 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Redo Qwen3.5/Qwen3-Next GDN projector fusion」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +43/-170 (213 lines); hunks: -30,36 +30,20; -73,11 +57,8; symbols: get_hf_config, Qwen3_5GatedDeltaNet, __init__, fix_query_key_value_ordering，涉及 `get_hf_config, Qwen3_5GatedDeltaNet, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +43/-170 (213 lines); hunks: -30,36 +30,20; -73,11 +57,8; symbols: get_hf_config, Qwen3_5GatedDeltaNet, __init__, fix_query_key_value_ordering
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -30,36 +30,20 @@
-from transformers.activations import ACT2FN
-    CacheConfig,
-    ModelConfig,
-    SpeculativeConfig,
-    get_current_vllm_config,
-    divide,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +43/-170
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34723 - [Bugfix] Fix prefix creation for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/34723
- 状态/时间: merged / 2026-02-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `909b14719725`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-5，可读 patch 32 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix prefix creation for Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Fix prefix creation for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +6/-5 (11 lines); hunks: -542,9 +542,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; -620,7 +621,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int, st...; symbols: __init__, get_expert_mapping, Qwen3_5ForConditionalGeneration，涉及 `__init__, get_expert_mapping, Qwen3_5ForConditionalGeneration`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +6/-5 (11 lines); hunks: -542,9 +542,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; -620,7 +621,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int, st...; symbols: __init__, get_expert_mapping, Qwen3_5ForConditionalGeneration
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -542,9 +542,10 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-        self.model = Qwen3_5Model(
-            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
-        )
+        # Deal with the case where the prefix is already "language_model" since
+        # Qwen/Qwen3.5-397B-A17B has naming like: model.language_model.layers.0
+        model_prefix = prefix if "model" in prefix else "model"
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +6/-5
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34683 - Revert "[Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj"

- 链接: https://github.com/vllm-project/vllm/pull/34683
- 状态/时间: merged / 2026-02-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `1d65283e95f4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+182/-87，可读 patch 402 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj"」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「Revert "[Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj"」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +166/-32 (198 lines); hunks: -30,20 +30,36; -57,8 +73,11; symbols: get_hf_config, Qwen3_5GatedDeltaNet, fix_query_key_value_ordering, __init__，涉及 `get_hf_config, Qwen3_5GatedDeltaNet, fix_query_key_value_ordering`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +166/-32 (198 lines); hunks: -30,20 +30,36; -57,8 +73,11; symbols: get_hf_config, Qwen3_5GatedDeltaNet, fix_query_key_value_ordering, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -30,20 +30,36 @@
+from transformers.activations import ACT2FN
+    CacheConfig,
+    ModelConfig,
+    SpeculativeConfig,
+    get_current_vllm_config,
+    divide,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +166/-32
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34492 - [Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj

- 链接: https://github.com/vllm-project/vllm/pull/34492
- 状态/时间: merged / 2026-02-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `3bb4e4311c6d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+87/-182，可读 patch 404 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Models] Fuse Qwen3.5 GDN's qkvz_proj and ba_proj」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +32/-166 (198 lines); hunks: -30,36 +30,20; -73,11 +57,8; symbols: get_hf_config, Qwen3_5GatedDeltaNet, __init__, fix_query_key_value_ordering，涉及 `get_hf_config, Qwen3_5GatedDeltaNet, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +32/-166 (198 lines); hunks: -30,36 +30,20; -73,11 +57,8; symbols: get_hf_config, Qwen3_5GatedDeltaNet, __init__, fix_query_key_value_ordering
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -30,36 +30,20 @@
-from transformers.activations import ACT2FN
-    CacheConfig,
-    ModelConfig,
-    SpeculativeConfig,
-    get_current_vllm_config,
-    divide,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +32/-166
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34512 - [Misc] Port Qwen3.5 Configs

- 链接: https://github.com/vllm-project/vllm/pull/34512
- 状态/时间: merged / 2026-02-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `5885e330efea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+410/-12，可读 patch 473 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Misc] Port Qwen3.5 Configs」；模型线: Qwen3.5；类别: 模型实现调整；主要 diff: `vllm/transformers_utils/configs/qwen3_5.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[Misc] Port Qwen3.5 Configs」；主要实现面是 `vllm/transformers_utils/configs/qwen3_5.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/transformers_utils/configs/qwen3_5.py` added +189/-0 (189 lines); hunks: -0,0 +1,189; symbols: Qwen3_5TextConfig, __init__, Qwen3_5VisionConfig, Qwen3_5Config，涉及 `Qwen3_5TextConfig, __init__, Qwen3_5VisionConfig`；`vllm/model_executor/models/qwen3_5.py` modified +8/-8 (16 lines); hunks: -31,14 +31,6; -87,6 +79,14；`vllm/model_executor/models/qwen3_5_mtp.py` modified +2/-4 (6 lines); hunks: -7,10 +7,6; -27,6 +23,8。
- 代码 diff 细节:
  - `vllm/transformers_utils/configs/qwen3_5.py` added +189/-0 (189 lines); hunks: -0,0 +1,189; symbols: Qwen3_5TextConfig, __init__, Qwen3_5VisionConfig, Qwen3_5Config
  - `vllm/model_executor/models/qwen3_5.py` modified +8/-8 (16 lines); hunks: -31,14 +31,6; -87,6 +79,14
  - `vllm/model_executor/models/qwen3_5_mtp.py` modified +2/-4 (6 lines); hunks: -7,10 +7,6; -27,6 +23,8
- 关键代码摘录:

```diff
diff -- vllm/transformers_utils/configs/qwen3_5.py
@@ -0,0 +1,189 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Copyright 2025 The Qwen Team and The HuggingFace Inc. team.
+# All rights reserved.
+#
+# Licensed under the Apache License, Version 2.0 (the "License");
diff -- vllm/model_executor/models/qwen3_5.py
@@ -31,14 +31,6 @@
-from transformers.models.qwen3_5.configuration_qwen3_5 import (
-    Qwen3_5Config,
-    Qwen3_5TextConfig,
-)
-from transformers.models.qwen3_5_moe.configuration_qwen3_5_moe import (
-    Qwen3_5MoeConfig,
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -7,10 +7,6 @@
```

- 已读文件:
  - runtime: `vllm/transformers_utils/configs/qwen3_5.py` added +189/-0; `vllm/model_executor/models/qwen3_5.py` modified +8/-8; `vllm/model_executor/models/qwen3_5_mtp.py` modified +2/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/transformers_utils/config.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34489 - [Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/34489
- 状态/时间: merged / 2026-02-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `eea3024f43e0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+42/-6，可读 patch 91 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Fix mamba state dtype setting for Qwen3-Next and Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +3/-2 (5 lines); hunks: -870,9 +870,10 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config，涉及 `get_mamba_state_dtype_from_config`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +3/-2 (5 lines); hunks: -870,9 +870,10 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -870,9 +870,10 @@ def get_mamba_state_dtype_from_config(
-        mamba_ssm_dtype = vllm_config.model_config.hf_text_config.mamba_ssm_dtype
-            vllm_config.model_config.dtype, mamba_ssm_dtype
+            vllm_config.model_config.dtype,
+            vllm_config.cache_config.mamba_cache_dtype,
+            vllm_config.cache_config.mamba_ssm_cache_dtype,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +3/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34313 - [Bugfix] Fix weight naming in Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/34313
- 状态/时间: merged / 2026-02-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `0b20469c627e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix weight naming in Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Fix weight naming in Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +1/-1 (2 lines); hunks: -206,7 +206,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +1/-1 (2 lines); hunks: -206,7 +206,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -206,7 +206,7 @@ def __init__(
-            prefix=f"{prefix}.in_proj_ba",
+            prefix=f"{prefix}.in_proj_b",
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34200 - [Bugfix] Fix mamba cache dtype for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/34200
- 状态/时间: merged / 2026-02-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `9615575afc0d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix mamba cache dtype for Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Fix mamba cache dtype for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +2/-1 (3 lines); hunks: -867,8 +867,9 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config，涉及 `get_mamba_state_dtype_from_config`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +2/-1 (3 lines); hunks: -867,8 +867,9 @@ def get_mamba_state_dtype_from_config(; symbols: get_mamba_state_dtype_from_config
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -867,8 +867,9 @@ def get_mamba_state_dtype_from_config(
+        mamba_ssm_dtype = vllm_config.model_config.hf_text_config.mamba_ssm_dtype
-            vllm_config.model_config.dtype, vllm_config.cache_config.mamba_cache_dtype
+            vllm_config.model_config.dtype, mamba_ssm_dtype
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34198 - [Bugfix] Adopt `ChunkGatedDeltaRule` for Qwen3.5

- 链接: https://github.com/vllm-project/vllm/pull/34198
- 状态/时间: merged / 2026-02-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`；关联提交 `047a457fa4af`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-0，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Adopt `ChunkGatedDeltaRule` for Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Adopt `ChunkGatedDeltaRule` for Qwen3.5」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` modified +3/-0 (3 lines); hunks: -99,6 +99,7; -268,6 +269,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` modified +3/-0 (3 lines); hunks: -99,6 +99,7; -268,6 +269,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -99,6 +99,7 @@
+    ChunkGatedDeltaRule,
@@ -268,6 +269,8 @@ def __init__(
+        self.chunk_gated_delta_rule = ChunkGatedDeltaRule()
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34110 - [MODEL] Adding Support for Qwen3.5 Models

- 链接: https://github.com/vllm-project/vllm/pull/34110
- 状态/时间: merged / 2026-02-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`；关联提交 `9562912cead1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+1501/-9，可读 patch 1631 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MODEL] Adding Support for Qwen3.5 Models」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[MODEL] Adding Support for Qwen3.5 Models」；主要实现面是 `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/qwen3_5.py` added +993/-0 (993 lines); hunks: -0,0 +1,993; symbols: Qwen3_5ProcessingInfo, get_hf_config, Qwen3_5MoeProcessingInfo, Qwen3_5GatedDeltaNet，涉及 `Qwen3_5ProcessingInfo, get_hf_config, Qwen3_5MoeProcessingInfo`；`vllm/model_executor/models/qwen3_5_mtp.py` added +447/-0 (447 lines); hunks: -0,0 +1,447; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward，涉及 `Qwen3_5MultiTokenPredictor, __init__, embed_input_ids`。
- 代码 diff 细节:
  - `vllm/model_executor/models/qwen3_5.py` added +993/-0 (993 lines); hunks: -0,0 +1,993; symbols: Qwen3_5ProcessingInfo, get_hf_config, Qwen3_5MoeProcessingInfo, Qwen3_5GatedDeltaNet
  - `vllm/model_executor/models/qwen3_5_mtp.py` added +447/-0 (447 lines); hunks: -0,0 +1,447; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/qwen3_5.py
@@ -0,0 +1,993 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Copyright 2025 The vLLM team.
+# Copyright 2025 The Qwen Team.
+# Copyright 2025 The HuggingFace Inc. team.
+# All rights reserved.
diff -- vllm/model_executor/models/qwen3_5_mtp.py
@@ -0,0 +1,447 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Inference-only Qwen3_5 MTP model."""
+import typing
+from collections.abc import Callable, Iterable
+import torch
```

- 已读文件:
  - runtime: `vllm/model_executor/models/qwen3_5.py` added +993/-0; `vllm/model_executor/models/qwen3_5_mtp.py` added +447/-0
- 验证与风险: diff 自带测试面 `tests/models/registry.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
