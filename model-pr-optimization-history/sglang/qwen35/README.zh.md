# sglang Qwen3.5 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` | [#32945](https://github.com/sgl-project/sglang/pull/32945), [#34357](https://github.com/sgl-project/sglang/pull/34357), [#35194](https://github.com/sgl-project/sglang/pull/35194), [#36245](https://github.com/sgl-project/sglang/pull/36245), [#38374](https://github.com/sgl-project/sglang/pull/38374), [#39104](https://github.com/sgl-project/sglang/pull/39104), [#39358](https://github.com/sgl-project/sglang/pull/39358), [#39572](https://github.com/sgl-project/sglang/pull/39572), [#41849](https://github.com/sgl-project/sglang/pull/41849), [#43083](https://github.com/sgl-project/sglang/pull/43083), [#46017](https://github.com/sgl-project/sglang/pull/46017), [#46032](https://github.com/sgl-project/sglang/pull/46032), ... (13 total) |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/qwen3_5_397b.mdx` | 无直接 PR 号提交 |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/qwen3_5_397b.mdx` | 无直接 PR 号提交 |
| `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` | [#43083](https://github.com/sgl-project/sglang/pull/43083), [#44712](https://github.com/sgl-project/sglang/pull/44712) |
| `docs/src/snippets/autoregressive/qwen35-deployment.jsx` | [#32945](https://github.com/sgl-project/sglang/pull/32945), [#34357](https://github.com/sgl-project/sglang/pull/34357), [#35445](https://github.com/sgl-project/sglang/pull/35445), [#36245](https://github.com/sgl-project/sglang/pull/36245), [#37360](https://github.com/sgl-project/sglang/pull/37360), [#38374](https://github.com/sgl-project/sglang/pull/38374), [#39104](https://github.com/sgl-project/sglang/pull/39104), [#39358](https://github.com/sgl-project/sglang/pull/39358), [#39572](https://github.com/sgl-project/sglang/pull/39572), [#40770](https://github.com/sgl-project/sglang/pull/40770), [#41849](https://github.com/sgl-project/sglang/pull/41849), [#46017](https://github.com/sgl-project/sglang/pull/46017), ... (13 total) |
| `python/sglang/srt/arg_groups/model_overrides/qwen3_5.py` | 无直接 PR 号提交 |
| `python/sglang/srt/configs/qwen3_5.py` | [#18489](https://github.com/sgl-project/sglang/pull/18489) |
| `python/sglang/srt/models/qwen3_5.py` | [#18489](https://github.com/sgl-project/sglang/pull/18489), [#18538](https://github.com/sgl-project/sglang/pull/18538), [#18544](https://github.com/sgl-project/sglang/pull/18544), [#18937](https://github.com/sgl-project/sglang/pull/18937), [#19070](https://github.com/sgl-project/sglang/pull/19070), [#19220](https://github.com/sgl-project/sglang/pull/19220), [#19411](https://github.com/sgl-project/sglang/pull/19411), [#19484](https://github.com/sgl-project/sglang/pull/19484), [#19670](https://github.com/sgl-project/sglang/pull/19670), [#19767](https://github.com/sgl-project/sglang/pull/19767), [#20386](https://github.com/sgl-project/sglang/pull/20386), [#20736](https://github.com/sgl-project/sglang/pull/20736), ... (50 total) |
| `python/sglang/srt/models/qwen3_5_mtp.py` | [#18489](https://github.com/sgl-project/sglang/pull/18489), [#18538](https://github.com/sgl-project/sglang/pull/18538), [#18926](https://github.com/sgl-project/sglang/pull/18926), [#18937](https://github.com/sgl-project/sglang/pull/18937), [#19391](https://github.com/sgl-project/sglang/pull/19391), [#19767](https://github.com/sgl-project/sglang/pull/19767), [#20918](https://github.com/sgl-project/sglang/pull/20918), [#23146](https://github.com/sgl-project/sglang/pull/23146), [#23331](https://github.com/sgl-project/sglang/pull/23331), [#35719](https://github.com/sgl-project/sglang/pull/35719), [#37471](https://github.com/sgl-project/sglang/pull/37471), [#38878](https://github.com/sgl-project/sglang/pull/38878), ... (13 total) |
| `python/sglang/srt/models/qwen3_5_text.py` | [#32401](https://github.com/sgl-project/sglang/pull/32401), [#34771](https://github.com/sgl-project/sglang/pull/34771), [#42002](https://github.com/sgl-project/sglang/pull/42002) |
| `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml` | 无直接 PR 号提交 |
| `test/manual/4-gpu-models/test_qwen35_fp4_triton.py` | 无直接 PR 号提交 |
| `test/manual/4-gpu-models/test_qwen35_models_archived.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py` | [#21669](https://github.com/sgl-project/sglang/pull/21669) |
| `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py` | [#21669](https://github.com/sgl-project/sglang/pull/21669) |
| `test/registered/amd/accuracy/mi35x/test_qwen35_mxfp4_eval_mi35x.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py` | [#21669](https://github.com/sgl-project/sglang/pull/21669) |
| `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py` | [#24651](https://github.com/sgl-project/sglang/pull/24651) |
| `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py` | [#21669](https://github.com/sgl-project/sglang/pull/21669) |
| `test/registered/amd/test_qwen35_gdn_online_mxfp4.py` | [#43839](https://github.com/sgl-project/sglang/pull/43839) |
| `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py` | [#39902](https://github.com/sgl-project/sglang/pull/39902) |
| `test/registered/amd/test_qwen35_gdn_packed_in_proj.py` | [#39902](https://github.com/sgl-project/sglang/pull/39902) |
| `test/registered/amd/test_qwen35_moe_softmax_topk.py` | [#39986](https://github.com/sgl-project/sglang/pull/39986) |
| `test/registered/attention/test_qwen35_deterministic.py` | [#27869](https://github.com/sgl-project/sglang/pull/27869) |
| `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py` | [#33922](https://github.com/sgl-project/sglang/pull/33922) |
| `test/registered/e2e/models/test_qwen35_9b_nvfp4_kv_cache_sm100.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_qwen35_fp4_mtp.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models_large/test_qwen35.py` | 无直接 PR 号提交 |
| `test/registered/hicache/test_qwen35_hicache.py` | [#34560](https://github.com/sgl-project/sglang/pull/34560) |
| `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py` | [#23594](https://github.com/sgl-project/sglang/pull/23594) |
| `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py` | [#23594](https://github.com/sgl-project/sglang/pull/23594) |
| `test/registered/npu/accuracy/qwen3_5_9b/test_npu_qwen3_5_9b_bf16_1p_gsm8k.py` | 无直接 PR 号提交 |
| `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` | [#39047](https://github.com/sgl-project/sglang/pull/39047) |
| `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py` | [#31220](https://github.com/sgl-project/sglang/pull/31220) |
| `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py` | [#39064](https://github.com/sgl-project/sglang/pull/39064) |
| `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py` | [#23062](https://github.com/sgl-project/sglang/pull/23062) |
| `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py` | [#29753](https://github.com/sgl-project/sglang/pull/29753), [#37471](https://github.com/sgl-project/sglang/pull/37471) |
| `test/registered/xpu/llm_models/test_xpu_qwen3_5_35b_a3b.py` | 无直接 PR 号提交 |
| `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py` | [#33354](https://github.com/sgl-project/sglang/pull/33354) |

## PR 覆盖总览

- git 追溯 PR 数: 85
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 85
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-09 | [#18489](https://github.com/sgl-project/sglang/pull/18489) | merged | [MODEL] Adding Support for Qwen3.5 Models | `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/configs/qwen3_5.py` |
| 2026-02-12 | [#18538](https://github.com/sgl-project/sglang/pull/18538) | merged | [Qwen3_5] Refactor `Qwen3_5ForCausalLMMTP` class implementation | `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-12 | [#18544](https://github.com/sgl-project/sglang/pull/18544) | merged | [Ascend]Support qwen3.5 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-18 | [#18926](https://github.com/sgl-project/sglang/pull/18926) | merged | feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation | `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-02-19 | [#18937](https://github.com/sgl-project/sglang/pull/18937) | merged | [Qwen3.5] Enable nvfp4 checkpoint | `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-02-25 | [#19070](https://github.com/sgl-project/sglang/pull/19070) | merged | fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-26 | [#19220](https://github.com/sgl-project/sglang/pull/19220) | merged | [PCG] fix piecewise cuda graph for Qwen3.5 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-26 | [#19411](https://github.com/sgl-project/sglang/pull/19411) | merged | [Qwen3.5] Qwen3.5-27B inference repeat bug fix | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-04 | [#19391](https://github.com/sgl-project/sglang/pull/19391) | merged | [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 | `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-03-07 | [#19670](https://github.com/sgl-project/sglang/pull/19670) | merged | [Qwen3.5] Support Qwen3.5 Pipeline Parallelism | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-09 | [#19767](https://github.com/sgl-project/sglang/pull/19767) | merged | Fix qwen3.5 mtp eplb related issues | `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-03-12 | [#20386](https://github.com/sgl-project/sglang/pull/20386) | merged | perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe… | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-21 | [#21070](https://github.com/sgl-project/sglang/pull/21070) | merged | [Qwen3.5] Fix broken pipeline parallelism layer splitting | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-23 | [#21019](https://github.com/sgl-project/sglang/pull/21019) | merged | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-30 | [#21448](https://github.com/sgl-project/sglang/pull/21448) | merged | [Fix] Fix Qwen3.5 MoE model loading and Mamba cache sharding in PP mode | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-30 | [#21234](https://github.com/sgl-project/sglang/pull/21234) | merged | [AMD] Support AMD MXFP4 Qwen3.5-397B-A17B model | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-01 | [#21347](https://github.com/sgl-project/sglang/pull/21347) | merged | [Bugfix] Fix PP tied embeddings weight loading for qwen3.5 4B dense model | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-07 | [#21669](https://github.com/sgl-project/sglang/pull/21669) | merged | [AMD] Add Qwen3.5-397B FP8 nightly perf benchmarks for MI30x and MI35x | `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py` |
| 2026-04-08 | [#21692](https://github.com/sgl-project/sglang/pull/21692) | merged | [Bugfix] [NPU] Qwen3.5 with quantization fix | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-15 | [#20736](https://github.com/sgl-project/sglang/pull/20736) | merged | [AMD] Enable share expert fusion with router experts for Qwen3.5 BF16 & FP8 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-26 | [#19484](https://github.com/sgl-project/sglang/pull/19484) | merged | [CPU] Add Qwen3.5 model optimization for CPU | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-27 | [#20918](https://github.com/sgl-project/sglang/pull/20918) | merged | [NPU] Support MTP for Qwen3.5 | `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-04-28 | [#23471](https://github.com/sgl-project/sglang/pull/23471) | merged | [Fix] NVFP4 qwen3.5 quant error fix by add packed_modules_mapping | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-29 | [#23815](https://github.com/sgl-project/sglang/pull/23815) | merged | [NPU] Fix DeepEP LL dispatch BF16 flag and skip triton kernel on NPU for Qwen3.5 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-30 | [#23594](https://github.com/sgl-project/sglang/pull/23594) | merged | LoRA support for qwen3.5 and nemotron3 | `python/sglang/srt/models/qwen3_5.py`, `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py` |
| 2026-04-30 | [#23062](https://github.com/sgl-project/sglang/pull/23062) | merged | [bugfix]fix(qwen3_5): broadcast per-tensor scale in _make_packed_weight_loader for FP8 models | `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-05-05 | [#23146](https://github.com/sgl-project/sglang/pull/23146) | merged | [AMD] Enable EAGLE speculative decoding for Qwen3.5 FP8 and MXFP4 models with aiter's unified attention | `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-05-19 | [#23331](https://github.com/sgl-project/sglang/pull/23331) | merged | [BugFix] Resolve adaptive speculative decoding conflicts for Qwen3.5 (hybrid GDN) | `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-05-20 | [#23925](https://github.com/sgl-project/sglang/pull/23925) | merged | [NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next | `python/sglang/srt/models/qwen3_5.py` |
| 2026-06-05 | [#25885](https://github.com/sgl-project/sglang/pull/25885) | merged | [AMD] Support alt stream for Qwen3.5 on AMD platform | `python/sglang/srt/models/qwen3_5.py` |
| 2026-06-10 | [#27656](https://github.com/sgl-project/sglang/pull/27656) | merged | [AMD][Perf] Fuse QK RMSNorm + gate extraction Triton kernel for Qwen3.5 on HIP | `python/sglang/srt/models/qwen3_5.py` |
| 2026-06-13 | [#26924](https://github.com/sgl-project/sglang/pull/26924) | merged | [4/N] Qwen3.5Opt: Overlap mamba verify update with draft extend | `python/sglang/srt/models/qwen3_5.py` |
| 2026-06-14 | [#27869](https://github.com/sgl-project/sglang/pull/27869) | merged | Fix Qwen3.5 deterministic batch-invariant logprobs | `test/registered/attention/test_qwen35_deterministic.py` |
| 2026-06-15 | [#27868](https://github.com/sgl-project/sglang/pull/27868) | merged | fix(qwen3.5): keep CUDA dual-stream overlap (regressed by #25885) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-06-24 | [#27870](https://github.com/sgl-project/sglang/pull/27870) | merged | [qwen3.5][XPU]Add XPU support for set_embed_and_head and fused QK RMSNorm kernel | `python/sglang/srt/models/qwen3_5.py` |
| 2026-06-25 | [#28320](https://github.com/sgl-project/sglang/pull/28320) | merged | Fused QK GemmaRMSNorm + RoPE + gate kernel for Qwen3.5 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-15 | [#31171](https://github.com/sgl-project/sglang/pull/31171) | merged | [CPU] add fused input proj for qwen3.5 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-17 | [#31174](https://github.com/sgl-project/sglang/pull/31174) | merged | fix: Qwen3.5-35B-A3B-AWQ w2_weight KeyError and related params for CPU | `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-22 | [#24651](https://github.com/sgl-project/sglang/pull/24651) | merged | [AMD] Add fused all-reduce RMSNorm per-group quant for Qwen3.5 FP8 | `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py` |
| 2026-07-28 | [#32401](https://github.com/sgl-project/sglang/pull/32401) | merged | [Model] Support standalone text-only Qwen3.5 checkpoints | `python/sglang/srt/models/qwen3_5_text.py` |
| 2026-07-29 | [#32022](https://github.com/sgl-project/sglang/pull/32022) | merged | fix(qwen3.5): restrict MoE weights to local PP layers | `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-30 | [#31220](https://github.com/sgl-project/sglang/pull/31220) | merged | Qwen3.5-MoE: support modelopt_fp4 checkpoints that quantize attention (+ load baked FP8 KV scales) | `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-08-07 | [#32945](https://github.com/sgl-project/sglang/pull/32945) | merged | Qwen3.5 NVFP4 V2 | `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx` |
| 2026-08-09 | [#22867](https://github.com/sgl-project/sglang/pull/22867) | merged | [feat] Add language_model_only parameter support for Qwen35 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-08-11 | [#34357](https://github.com/sgl-project/sglang/pull/34357) | merged | Update Qwen3.5 B200 NVFP4 MTP config | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-08-13 | [#34421](https://github.com/sgl-project/sglang/pull/34421) | merged | [AMD][Perf] Fuse GatedDeltaNet QKVZBA split/reshape/cat into a single Triton kernel for Qwen3.5-architecture MoE on HIP | `python/sglang/srt/models/qwen3_5.py` |
| 2026-08-14 | [#34560](https://github.com/sgl-project/sglang/pull/34560) | merged | [Fix] Fix Qwen3.5 MTP startup with HiCache | `test/registered/hicache/test_qwen35_hicache.py` |
| 2026-08-15 | [#34771](https://github.com/sgl-project/sglang/pull/34771) | merged | [Spec] Wire DFLASH aux-hidden capture into the Qwen3.5 text-only wrapper | `python/sglang/srt/models/qwen3_5_text.py` |
| 2026-08-16 | [#34474](https://github.com/sgl-project/sglang/pull/34474) | merged | [AMD] Qwen3.5: guard attn layers against empty DP-attention batch | `python/sglang/srt/models/qwen3_5.py` |
| 2026-08-18 | [#35194](https://github.com/sgl-project/sglang/pull/35194) | merged | Update Qwen3.5 H200 FP8 for AgentX HiCache MTP | `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-08-19 | [#35445](https://github.com/sgl-project/sglang/pull/35445) | merged | [AMD] cookbook: serve Qwen3.5 MXFP4 on MI355X with an fp8_e4m3 KV cache | `docs/src/snippets/autoregressive/qwen35-deployment.jsx` |
| 2026-08-24 | [#33354](https://github.com/sgl-project/sglang/pull/33354) | merged | [XPU] Use a fused GDN kernel from sgl-kernel for Qwen3.5 | `python/sglang/srt/models/qwen3_5.py`, `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py` |
| 2026-08-24 | [#35719](https://github.com/sgl-project/sglang/pull/35719) | merged | [AMD] Fix Qwen3.5 MTP dropping fused shared-expert weights | `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-08-25 | [#36245](https://github.com/sgl-project/sglang/pull/36245) | merged | [AMD] cookbook: add HiCache host-DRAM KV tier for Qwen3.5 MXFP4 on MI355X | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-08-28 | [#35341](https://github.com/sgl-project/sglang/pull/35341) | merged | [AMD][Fix] Qwen3.5: make empty-batch guard tuple-aware on fused AR+quant path | `python/sglang/srt/models/qwen3_5.py` |
| 2026-08-30 | [#34446](https://github.com/sgl-project/sglang/pull/34446) | merged | [rotary] Fix the fused Qwen3.5 RoPE kernel discarding mrope height and width | `python/sglang/srt/models/qwen3_5.py` |
| 2026-09-01 | [#37360](https://github.com/sgl-project/sglang/pull/37360) | merged | docs(cookbook): enable FlashInfer GDN for Qwen3.5 B200 | `docs/src/snippets/autoregressive/qwen35-deployment.jsx` |
| 2026-09-02 | [#37471](https://github.com/sgl-project/sglang/pull/37471) | merged | [Bugfix] Load Qwen3.5 MTP embedding under PP | `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-09-04 | [#36267](https://github.com/sgl-project/sglang/pull/36267) | merged | [Performance] Optimize Qwen3.5 GDN prefill projection layouts | `python/sglang/srt/models/qwen3_5.py` |
| 2026-09-08 | [#38374](https://github.com/sgl-project/sglang/pull/38374) | merged | docs(cookbook): Qwen3.5 FP8 on B200/B300 — trtllm-gen MoE + symm mem | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-09-10 | [#33922](https://github.com/sgl-project/sglang/pull/33922) | merged | Fix Qwen3.5 GDN multi-item scoring | `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py` |
| 2026-09-12 | [#39104](https://github.com/sgl-project/sglang/pull/39104) | merged | [AMD] Update MI355X MXFP4 HiCache defaults and quick-reduce quantization for Qwen3.5 cookbook | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-09-14 | [#39358](https://github.com/sgl-project/sglang/pull/39358) | merged | [AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-09-14 | [#39047](https://github.com/sgl-project/sglang/pull/39047) | merged | [NPU] Remove temperature/top_p from Qwen3.5-397B-A17B perf test | `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` |
| 2026-09-16 | [#39572](https://github.com/sgl-project/sglang/pull/39572) | merged | [AMD] Align Qwen3.5 MI355X HiCache cookbook with kernel / page_first | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-09-17 | [#38878](https://github.com/sgl-project/sglang/pull/38878) | merged | [AMD] Load fused shared experts for Qwen4-Exp and Qwen3.5 MTP | `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-09-21 | [#39986](https://github.com/sgl-project/sglang/pull/39986) | merged | [AMD] Use Triton softmax routing for Qwen3.5 on gfx950 | `test/registered/amd/test_qwen35_moe_softmax_topk.py` |
| 2026-09-22 | [#39902](https://github.com/sgl-project/sglang/pull/39902) | merged | [AMD] Pack Qwen3.5 GDN input projections on ROCm | `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_packed_in_proj.py`, `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py` |
| 2026-09-22 | [#40770](https://github.com/sgl-project/sglang/pull/40770) | merged | Add GB200/GB300 hardware to Qwen3.5 | `docs/src/snippets/autoregressive/qwen35-deployment.jsx` |
| 2026-09-23 | [#35958](https://github.com/sgl-project/sglang/pull/35958) | merged | [npu] decoding procedure optimization on qwen3.5/3.6 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-09-25 | [#41198](https://github.com/sgl-project/sglang/pull/41198) | merged | [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit | `python/sglang/srt/models/qwen3_5.py` |
| 2026-09-25 | [#39064](https://github.com/sgl-project/sglang/pull/39064) | merged | [ROCm][Bugfix] Keep quantization for mixed Quark Qwen3.5 MTP checkpoints | `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-09-30 | [#41849](https://github.com/sgl-project/sglang/pull/41849) | merged | [Docs] Add MI355X FP8 agentic recipe to the Qwen3.5 cookbook | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-09-30 | [#41154](https://github.com/sgl-project/sglang/pull/41154) | merged | fix(spec): enable Qwen3.5 EAGLE3 capture and streaming overlap | `python/sglang/srt/models/qwen3_5.py` |
| 2026-10-02 | [#42002](https://github.com/sgl-project/sglang/pull/42002) | merged | [Spec] Fix Qwen3.5 text model EAGLE3/DFLASH aux-layer capture | `python/sglang/srt/models/qwen3_5_text.py` |
| 2026-10-08 | [#41134](https://github.com/sgl-project/sglang/pull/41134) | merged | [AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-10-09 | [#43083](https://github.com/sgl-project/sglang/pull/43083) | merged | [Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1 | `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-10-11 | [#43037](https://github.com/sgl-project/sglang/pull/43037) | merged | [Spec] Allow Qwen3.5 backends to opt into packed target verification | `python/sglang/srt/models/qwen3_5.py` |
| 2026-10-15 | [#29753](https://github.com/sgl-project/sglang/pull/29753) | merged | [NPU] [Bugfix] Fix rope sin cos pre-calculation for Qwen3.5 during Pipeline Parallelism | `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-10-16 | [#44712](https://github.com/sgl-project/sglang/pull/44712) | merged | [Doc] cookbook: Refresh SemiAnalysis AgentX launches for Qwen3.5 and DeepSeek-V4.1-Flash GB300 | `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` |
| 2026-10-21 | [#32745](https://github.com/sgl-project/sglang/pull/32745) | merged | [Fix] [NPU] qwen3.5: Fix dense serving on Ascend 950 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-10-23 | [#46017](https://github.com/sgl-project/sglang/pull/46017) | merged | [Doc] cookbook: Qwen3.5 MI355X FP8 agentic uses HiCache write_through on the v0.5.22 image | `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx` |
| 2026-10-23 | [#46032](https://github.com/sgl-project/sglang/pull/46032) | merged | [Doc] cookbook: Qwen3.5 MI355X FP8 agentic adds scheduler/tokenizer tuning from the InferenceX recipe | `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |
| 2026-10-27 | [#43839](https://github.com/sgl-project/sglang/pull/43839) | merged | [Perf] [AMD] qwen3_5: Quantize the BF16 GDN projections to MXFP4 online | `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_online_mxfp4.py` |
| 2026-10-28 | [#46757](https://github.com/sgl-project/sglang/pull/46757) | merged | [Doc] [AMD] cookbook: Add the Qwen3.5 MI355X FP8 agentic recipe covering the GPU-resident and HiCache bands | `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` |

## 逐 PR diff 审计卡

### PR #18489 - [MODEL] Adding Support for Qwen3.5 Models

- 链接: https://github.com/sgl-project/sglang/pull/18489
- 状态/时间: merged / 2026-02-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/qwen3_5.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `27c447653d9c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 17 个文件，+1923/-9，可读 patch 2159 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MODEL] Adding Support for Qwen3.5 Models」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/configs/qwen3_5.py`；技术摘要: 覆盖「[MODEL] Adding Support for Qwen3.5 Models」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/configs/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` added +1310/-0 (1310 lines); hunks: -0,0 +1,1310; symbols: Qwen3_5GatedDeltaNet, __init__, fix_query_key_value_ordering, forward，涉及 `Qwen3_5GatedDeltaNet, __init__, fix_query_key_value_ordering`；`python/sglang/srt/models/qwen3_5_mtp.py` added +415/-0 (415 lines); hunks: -0,0 +1,415; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward，涉及 `Qwen3_5MultiTokenPredictor, __init__, embed_input_ids`；`python/sglang/srt/configs/qwen3_5.py` added +113/-0 (113 lines); hunks: -0,0 +1,113; symbols: Qwen3_5VisionConfig, Qwen3_5TextConfig, __init__, Qwen3_5Config，涉及 `Qwen3_5VisionConfig, Qwen3_5TextConfig, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` added +1310/-0 (1310 lines); hunks: -0,0 +1,1310; symbols: Qwen3_5GatedDeltaNet, __init__, fix_query_key_value_ordering, forward
  - `python/sglang/srt/models/qwen3_5_mtp.py` added +415/-0 (415 lines); hunks: -0,0 +1,415; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward
  - `python/sglang/srt/configs/qwen3_5.py` added +113/-0 (113 lines); hunks: -0,0 +1,113; symbols: Qwen3_5VisionConfig, Qwen3_5TextConfig, __init__, Qwen3_5Config
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -0,0 +1,1310 @@
+# Copyright 2025 Qwen Team
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -0,0 +1,415 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/configs/qwen3_5.py
@@ -0,0 +1,113 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` added +1310/-0; `python/sglang/srt/models/qwen3_5_mtp.py` added +415/-0; `python/sglang/srt/configs/qwen3_5.py` added +113/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18538 - [Qwen3_5] Refactor `Qwen3_5ForCausalLMMTP` class implementation

- 链接: https://github.com/sgl-project/sglang/pull/18538
- 状态/时间: merged / 2026-02-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `4ed2548427a0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+62/-118，可读 patch 275 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3_5] Refactor `Qwen3_5ForCausalLMMTP` class implementation」；模型线: Qwen3.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Qwen3_5] Refactor `Qwen3_5ForCausalLMMTP` class implementation」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +44/-112 (156 lines); hunks: -24,114 +24,15; -140,7 +41,7 @@ def __init__(; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward，涉及 `Qwen3_5MultiTokenPredictor, __init__, embed_input_ids`；`python/sglang/srt/models/qwen3_5.py` modified +18/-6 (24 lines); hunks: -330,6 +330,9 @@ def __init__(; -338,15 +341,18 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +44/-112 (156 lines); hunks: -24,114 +24,15; -140,7 +41,7 @@ def __init__(; symbols: Qwen3_5MultiTokenPredictor, __init__, embed_input_ids, forward
  - `python/sglang/srt/models/qwen3_5.py` modified +18/-6 (24 lines); hunks: -330,6 +330,9 @@ def __init__(; -338,15 +341,18 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -24,114 +24,15 @@
-from sglang.srt.layers.vocab_parallel_embedding import (
-    ParallelLMHead,
-    VocabParallelEmbedding,
-)
+from sglang.srt.layers.vocab_parallel_embedding import ParallelLMHead
-from sglang.srt.models.qwen3_5 import Qwen3_5AttentionDecoderLayer
diff -- python/sglang/srt/models/qwen3_5.py
@@ -330,6 +330,9 @@ def __init__(
+            is_layer_sparse = True
+            is_previous_layer_sparse = True
+            is_next_layer_sparse = True
@@ -338,15 +341,18 @@ def __init__(
+            is_layer_sparse = False
+            is_previous_layer_sparse = False
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +44/-112; `python/sglang/srt/models/qwen3_5.py` modified +18/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18544 - [Ascend]Support qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/18544
- 状态/时间: merged / 2026-02-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `1edc69be0854`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+23/-4，可读 patch 75 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Ascend]Support qwen3.5」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Ascend]Support qwen3.5」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +12/-2 (14 lines); hunks: -34,6 +34,7; -328,15 +329,15 @@ def __init__(; symbols: __init__, load_fused_expert_weights, get_model_config_for_expert_location，涉及 `__init__, load_fused_expert_weights, get_model_config_for_expert_location`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +12/-2 (14 lines); hunks: -34,6 +34,7; -328,15 +329,15 @@ def __init__(; symbols: __init__, load_fused_expert_weights, get_model_config_for_expert_location
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -34,6 +34,7 @@
+from sglang.srt.eplb.expert_location import ModelConfigForExpertLocation
@@ -328,15 +329,15 @@ def __init__(
-                prefix=add_prefix("mlp", prefix.replace(".self_attn", "")),
+                prefix=add_prefix("mlp", prefix.replace(".linear_attn", "")),
-                prefix=add_prefix("mlp", prefix.replace(".self_attn", "")),
+                prefix=add_prefix("mlp", prefix.replace(".linear_attn", "")),
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +12/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18926 - feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation

- 链接: https://github.com/sgl-project/sglang/pull/18926
- 状态/时间: merged / 2026-02-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `fa5698d79164`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+57/-12，可读 patch 131 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +1/-6 (7 lines); hunks: -64,7 +64,7 @@ def __init__(; -214,16 +214,11 @@ def load_fused_expert_weights(; symbols: __init__, load_fused_expert_weights，涉及 `__init__, load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +1/-6 (7 lines); hunks: -64,7 +64,7 @@ def __init__(; -214,16 +214,11 @@ def load_fused_expert_weights(; symbols: __init__, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -64,7 +64,7 @@ def __init__(
-            prefix=add_prefix("model", prefix),
+            prefix=add_prefix("mtp", prefix),
@@ -214,16 +214,11 @@ def load_fused_expert_weights(
-            # Some checkpoints use model.language_model.mtp.* prefix
-            if "language_model" in name:
-                name = name.replace(r"model.language_model.", r"model.")
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +1/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18937 - [Qwen3.5] Enable nvfp4 checkpoint

- 链接: https://github.com/sgl-project/sglang/pull/18937
- 状态/时间: merged / 2026-02-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `bba2fc49a170`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+26/-8，可读 patch 98 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3.5] Enable nvfp4 checkpoint」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[Qwen3.5] Enable nvfp4 checkpoint」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +19/-7 (26 lines); hunks: -318,8 +318,14 @@ def __init__(; -458,13 +464,19 @@ def __init__(; symbols: __init__, load_weights, load_fused_expert_weights，涉及 `__init__, load_weights, load_fused_expert_weights`；`python/sglang/srt/models/qwen3_5_mtp.py` modified +4/-0 (4 lines); hunks: -48,6 +48,10 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +19/-7 (26 lines); hunks: -318,8 +318,14 @@ def __init__(; -458,13 +464,19 @@ def __init__(; symbols: __init__, load_weights, load_fused_expert_weights
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +4/-0 (4 lines); hunks: -48,6 +48,10 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -318,8 +318,14 @@ def __init__(
+        linear_attn_quant_config = (
+            None
+            if quant_config and quant_config.get_name() == "modelopt_fp4"
+            else quant_config
+        )
-            config, layer_id, quant_config, alt_stream, prefix
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -48,6 +48,10 @@ def __init__(
+        # The MTP model is unquantized in the nvfp4 checkpoint.
+        if quant_config and quant_config.get_name() == "modelopt_fp4":
+            quant_config = None
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +19/-7; `python/sglang/srt/models/qwen3_5_mtp.py` modified +4/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19070 - fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1

- 链接: https://github.com/sgl-project/sglang/pull/19070
- 状态/时间: merged / 2026-02-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `d38c0e537d95`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+32/-6，可读 patch 56 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +32/-6 (38 lines); hunks: -400,11 +400,24 @@ def forward(; -633,11 +646,24 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +32/-6 (38 lines); hunks: -400,11 +400,24 @@ def forward(; -633,11 +646,24 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -400,11 +400,24 @@ def forward(
-        hidden_states = self.mlp(hidden_states, forward_batch, use_reduce_scatter)
-        hidden_states, residual = self.layer_communicator.postprocess_layer(
-            hidden_states, residual, forward_batch
+        should_allreduce_fusion = (
+            self.layer_communicator.should_fuse_mlp_allreduce_with_next_layer(
+                forward_batch
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +32/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19220 - [PCG] fix piecewise cuda graph for Qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/19220
- 状态/时间: merged / 2026-02-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `b3202fe6d072`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+9/-46，可读 patch 115 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[PCG] fix piecewise cuda graph for Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[PCG] fix piecewise cuda graph for Qwen3.5」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +1/-21 (22 lines); hunks: -22,9 +22,6; -72,7 +69,6; symbols: forward, _forward，涉及 `forward, _forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +1/-21 (22 lines); hunks: -22,9 +22,6; -72,7 +69,6; symbols: forward, _forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -22,9 +22,6 @@
-# Model Executor
-from sglang.srt.compilation.piecewise_context_manager import get_forward_context
@@ -72,7 +69,6 @@
-from sglang.srt.models.qwen3_next import gdn_with_output
@@ -253,22 +249,6 @@ def forward(
-    ):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +1/-21
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19411 - [Qwen3.5] Qwen3.5-27B inference repeat bug fix

- 链接: https://github.com/sgl-project/sglang/pull/19411
- 状态/时间: merged / 2026-02-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `bdc1e46e5ac9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-0，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3.5] Qwen3.5-27B inference repeat bug fix」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Qwen3.5] Qwen3.5-27B inference repeat bug fix」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +2/-0 (2 lines); hunks: -352,6 +352,7 @@ def __init__(; -542,6 +543,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +2/-0 (2 lines); hunks: -352,6 +352,7 @@ def __init__(; -542,6 +543,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -352,6 +352,7 @@ def __init__(
+            is_last_layer=(layer_id == config.num_hidden_layers - 1),
@@ -542,6 +543,7 @@ def __init__(
+            is_last_layer=(layer_id == config.num_hidden_layers - 1),
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19391 - [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4

- 链接: https://github.com/sgl-project/sglang/pull/19391
- 状态/时间: merged / 2026-03-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `9457c049e19e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+252/-16，可读 patch 332 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +1/-1 (2 lines); hunks: -111,7 +111,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +1/-1 (2 lines); hunks: -111,7 +111,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -111,7 +111,7 @@ def forward(
-            and not forward_batch.forward_mode.is_draft_extend()
+            and not forward_batch.forward_mode.is_draft_extend(include_v2=True)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/registered/4-gpu-models/test_qwen35_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #19670 - [Qwen3.5] Support Qwen3.5 Pipeline Parallelism

- 链接: https://github.com/sgl-project/sglang/pull/19670
- 状态/时间: merged / 2026-03-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `7da590d4d069`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+114/-13，可读 patch 194 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3.5] Support Qwen3.5 Pipeline Parallelism」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Qwen3.5] Support Qwen3.5 Pipeline Parallelism」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +60/-13 (73 lines); hunks: -30,7 +30,7; -59,6 +59,7; symbols: __init__, get_layer, get_input_embeddings，涉及 `__init__, get_layer, get_input_embeddings`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +60/-13 (73 lines); hunks: -30,7 +30,7; -59,6 +59,7; symbols: __init__, get_layer, get_input_embeddings
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -30,7 +30,7 @@
-from sglang.srt.distributed import get_pp_group
+from sglang.srt.distributed import get_pp_group, get_pp_indices
@@ -59,6 +59,7 @@
+from sglang.srt.layers.utils import PPMissingLayer
@@ -680,6 +681,8 @@ def __init__(
+        else:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +60/-13
- 验证与风险: diff 自带测试面 `test/registered/distributed/test_pp_single_node.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #19767 - Fix qwen3.5 mtp eplb related issues

- 链接: https://github.com/sgl-project/sglang/pull/19767
- 状态/时间: merged / 2026-03-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `cabe171b6ce3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+79/-16，可读 patch 272 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix qwen3.5 mtp eplb related issues」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「Fix qwen3.5 mtp eplb related issues」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +34/-1 (35 lines); hunks: -72,7 +72,14; -294,6 +301,7 @@ def __init__(; symbols: __init__，涉及 `__init__`；`python/sglang/srt/models/qwen3_5_mtp.py` modified +19/-6 (25 lines); hunks: -22,6 +22,8; -69,6 +71,7 @@ def __init__(; symbols: __init__, get_model_config_for_expert_location, get_embed_and_head, forward，涉及 `__init__, get_model_config_for_expert_location, get_embed_and_head`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +34/-1 (35 lines); hunks: -72,7 +72,14; -294,6 +301,7 @@ def __init__(; symbols: __init__
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +19/-6 (25 lines); hunks: -22,6 +22,8; -69,6 +71,7 @@ def __init__(; symbols: __init__, get_model_config_for_expert_location, get_embed_and_head, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -72,7 +72,14 @@
-from sglang.srt.utils import add_prefix, is_cuda, is_npu, make_layers, set_weight_attrs
+from sglang.srt.utils import (
+    LazyValue,
+    add_prefix,
+    is_cuda,
+    is_npu,
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -22,6 +22,8 @@
+from sglang.srt.eplb.expert_distribution import get_global_expert_distribution_recorder
+from sglang.srt.eplb.expert_location import ModelConfigForExpertLocation
@@ -69,6 +71,7 @@ def __init__(
+            is_nextn=True,
@@ -84,6 +87,15 @@ def __init__(
+    @classmethod
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +34/-1; `python/sglang/srt/models/qwen3_5_mtp.py` modified +19/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20386 - perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe…

- 链接: https://github.com/sgl-project/sglang/pull/20386
- 状态/时间: merged / 2026-03-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `9b55a98a6705`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-2，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe…」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe…」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +1/-2 (3 lines); hunks: -20,7 +20,6; -287,7 +286,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +1/-2 (3 lines); hunks: -20,7 +20,6; -287,7 +286,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -20,7 +20,6 @@
-from einops import rearrange
@@ -287,7 +286,7 @@ def forward(
-        core_attn_out = rearrange(core_attn_out, "... h d -> ... (h d)")
+        core_attn_out = core_attn_out.flatten(-2)  # ... h d -> ... (h d)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +1/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21070 - [Qwen3.5] Fix broken pipeline parallelism layer splitting

- 链接: https://github.com/sgl-project/sglang/pull/21070
- 状态/时间: merged / 2026-03-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `852e112ebf00`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+15/-20，可读 patch 94 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3.5] Fix broken pipeline parallelism layer splitting」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Qwen3.5] Fix broken pipeline parallelism layer splitting」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +8/-15 (23 lines); hunks: -29,7 +29,7; -721,25 +721,14 @@ def get_layer(idx: int, prefix: str):; symbols: get_layer, load_fused_expert_weights，涉及 `get_layer, load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +8/-15 (23 lines); hunks: -29,7 +29,7; -721,25 +721,14 @@ def get_layer(idx: int, prefix: str):; symbols: get_layer, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -29,7 +29,7 @@
-from sglang.srt.distributed import get_pp_group, get_pp_indices
+from sglang.srt.distributed import get_pp_group
@@ -721,25 +721,14 @@ def get_layer(idx: int, prefix: str):
-        self.layers = make_layers(
+        self.layers, self._start_layer, self._end_layer = make_layers(
+            pp_rank=self.pp_group.rank_in_group,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +8/-15
- 验证与风险: diff 自带测试面 `test/registered/distributed/test_pp_single_node.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21019 - [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel

- 链接: https://github.com/sgl-project/sglang/pull/21019
- 状态/时间: merged / 2026-03-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `5bdc07d974f6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+597/-202，可读 patch 953 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +285/-65 (350 lines); hunks: -20,6 +20,11; -54,6 +59,10; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +285/-65 (350 lines); hunks: -20,6 +20,11; -54,6 +59,10; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -20,6 +20,11 @@
+import triton
+from sglang.jit_kernel.triton.gdn_fused_proj import (
+    fused_qkvzba_split_reshape_cat_contiguous,
+)
@@ -54,6 +59,10 @@
+from sglang.srt.layers.parameter import (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +285/-65
- 验证与风险: runtime 路径改动集中在 `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21448 - [Fix] Fix Qwen3.5 MoE model loading and Mamba cache sharding in PP mode

- 链接: https://github.com/sgl-project/sglang/pull/21448
- 状态/时间: merged / 2026-03-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `9b4dd274787c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+78/-8，可读 patch 262 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Fix Qwen3.5 MoE model loading and Mamba cache sharding in PP mode」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Fix] Fix Qwen3.5 MoE model loading and Mamba cache sharding in PP mode」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +31/-1 (32 lines); hunks: -67,7 +67,7; -1038,6 +1038,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights, load_fused_expert_weights，涉及 `load_weights, load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +31/-1 (32 lines); hunks: -67,7 +67,7; -1038,6 +1038,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -67,7 +67,7 @@
-from sglang.srt.layers.utils import PPMissingLayer
+from sglang.srt.layers.utils import PPMissingLayer, get_layer_id
@@ -1038,6 +1038,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+            layer_id = get_layer_id(name)
+            if (
+                layer_id is not None
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +31/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/mem_cache/test_mamba_unittest.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21234 - [AMD] Support AMD MXFP4 Qwen3.5-397B-A17B model

- 链接: https://github.com/sgl-project/sglang/pull/21234
- 状态/时间: merged / 2026-03-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `e6071e60c097`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+18/-0，可读 patch 53 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Support AMD MXFP4 Qwen3.5-397B-A17B model」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD] Support AMD MXFP4 Qwen3.5-397B-A17B model」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +18/-0 (18 lines); hunks: -88,6 +88,7; -98,6 +99,7; symbols: forward, Qwen3_5ForCausalLM, __init__, load_fused_expert_weights，涉及 `forward, Qwen3_5ForCausalLM, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +18/-0 (18 lines); hunks: -88,6 +88,7; -98,6 +99,7; symbols: forward, Qwen3_5ForCausalLM, __init__, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -88,6 +88,7 @@
+    is_gfx95_supported,
@@ -98,6 +99,7 @@
+_is_gfx95 = is_gfx95_supported()
@@ -879,6 +881,14 @@ def forward(
+    if _is_gfx95:
+        packed_modules_mapping = {
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +18/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21347 - [Bugfix] Fix PP tied embeddings weight loading for qwen3.5 4B dense model

- 链接: https://github.com/sgl-project/sglang/pull/21347
- 状态/时间: merged / 2026-04-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `2861596fc683`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+22/-0，可读 patch 36 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix PP tied embeddings weight loading for qwen3.5 4B dense model」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] Fix PP tied embeddings weight loading for qwen3.5 4B dense model」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +22/-0 (22 lines); hunks: -1384,6 +1384,17 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; -1549,6 +1560,17 @@ def load_fused_expert_weights(; symbols: load_weights, load_fused_expert_weights，涉及 `load_weights, load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +22/-0 (22 lines); hunks: -1384,6 +1384,17 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; -1549,6 +1560,17 @@ def load_fused_expert_weights(; symbols: load_weights, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -1384,6 +1384,17 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+            if (
+                self.config.tie_word_embeddings
+                and self.pp_group.is_last_rank
+                and "model.embed_tokens.weight" in name
+            ):
+                if "lm_head.weight" in params_dict:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +22/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21669 - [AMD] Add Qwen3.5-397B FP8 nightly perf benchmarks for MI30x and MI35x

- 链接: https://github.com/sgl-project/sglang/pull/21669
- 状态/时间: merged / 2026-04-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py`；关联提交 `ba78f6e0efb9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+408/-8，可读 patch 538 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add Qwen3.5-397B FP8 nightly perf benchmarks for MI30x and MI35x」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`；技术摘要: 覆盖「[AMD] Add Qwen3.5-397B FP8 nightly perf benchmarks for MI30x and MI35x」；主要实现面是 `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py` added +139/-0 (139 lines); hunks: -0,0 +1,139; symbols: generate_simple_markdown_report, TestNightlyQwen35Fp8Performance, setUpClass, test_bench_qwen35_fp8，涉及 `generate_simple_markdown_report, TestNightlyQwen35Fp8Performance, setUpClass`；`test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py` added +139/-0 (139 lines); hunks: -0,0 +1,139; symbols: generate_simple_markdown_report, TestQwen35Fp8PerfMI35x, setUpClass, test_qwen35_fp8_perf，涉及 `generate_simple_markdown_report, TestQwen35Fp8PerfMI35x, setUpClass`；`test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py` modified +42/-1 (43 lines); hunks: -8,14 +8,20; -38,7 +44,7 @@ def setUpClass(cls):; symbols: setUpClass, tearDownClass, test_lm_eval，涉及 `setUpClass, tearDownClass, test_lm_eval`；`test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py` modified +36/-3 (39 lines); hunks: -8,16 +8,21; -40,12 +45,12 @@ def setUpClass(cls):; symbols: setUpClass, test_lm_eval，涉及 `setUpClass, test_lm_eval`。
- 代码 diff 细节:
  - `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py` added +139/-0 (139 lines); hunks: -0,0 +1,139; symbols: generate_simple_markdown_report, TestNightlyQwen35Fp8Performance, setUpClass, test_bench_qwen35_fp8
  - `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py` added +139/-0 (139 lines); hunks: -0,0 +1,139; symbols: generate_simple_markdown_report, TestQwen35Fp8PerfMI35x, setUpClass, test_qwen35_fp8_perf
  - `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py` modified +42/-1 (43 lines); hunks: -8,14 +8,20; -38,7 +44,7 @@ def setUpClass(cls):; symbols: setUpClass, tearDownClass, test_lm_eval
  - `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py` modified +36/-3 (39 lines); hunks: -8,16 +8,21; -40,12 +45,12 @@ def setUpClass(cls):; symbols: setUpClass, test_lm_eval
- 关键代码摘录:

```diff
diff -- test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py
@@ -0,0 +1,139 @@
+"""Nightly performance benchmark for Qwen3.5-397B-A17B FP8.
+Tests Qwen3.5-397B-A17B-FP8 (MoE, Hybrid Attention with Gated Delta Networks)
+on 8 GPUs with triton attention backend.
+Model path can be configured via environment variable:
+- QWEN35_FP8_MODEL_PATH: Path to Qwen3.5-FP8 model
+  (default: Qwen/Qwen3.5-397B-A17B-FP8)
diff -- test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py
@@ -0,0 +1,139 @@
+"""MI35x Nightly performance benchmark for Qwen3.5-397B-A17B FP8.
+Tests Qwen3.5-397B-A17B-FP8 (MoE, Hybrid Attention with Gated Delta Networks)
+on 8 GPUs with triton attention backend.
+Registry: nightly-perf-8-gpu-mi35x-qwen35-fp8 suite
+"""
+import os
diff -- test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py
@@ -8,14 +8,20 @@
```

- 已读文件:
  - tests: `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py` added +139/-0; `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py` added +139/-0; `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py` modified +42/-1; `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py` modified +36/-3
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_qwen35_fp8_perf_amd.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_perf_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21692 - [Bugfix] [NPU] Qwen3.5 with quantization fix

- 链接: https://github.com/sgl-project/sglang/pull/21692
- 状态/时间: merged / 2026-04-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `cd373667cdfa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+29/-42，可读 patch 147 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] [NPU] Qwen3.5 with quantization fix」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Bugfix] [NPU] Qwen3.5 with quantization fix」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +3/-3 (6 lines); hunks: -881,7 +881,7 @@ def forward(; -1310,7 +1310,7 @@ def load_fused_expert_weights(; symbols: forward, Qwen3_5ForCausalLM, load_fused_expert_weights, Qwen3_5ForConditionalGeneration，涉及 `forward, Qwen3_5ForCausalLM, load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +3/-3 (6 lines); hunks: -881,7 +881,7 @@ def forward(; -1310,7 +1310,7 @@ def load_fused_expert_weights(; symbols: forward, Qwen3_5ForCausalLM, load_fused_expert_weights, Qwen3_5ForConditionalGeneration
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -881,7 +881,7 @@ def forward(
-    if _is_gfx95:
+    if _is_gfx95 or _is_npu:
@@ -1310,7 +1310,7 @@ def load_fused_expert_weights(
-    if _is_gfx95:
+    if _is_gfx95 or _is_npu:
@@ -1447,7 +1447,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +3/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20736 - [AMD] Enable share expert fusion with router experts for Qwen3.5 BF16 & FP8

- 链接: https://github.com/sgl-project/sglang/pull/20736
- 状态/时间: merged / 2026-04-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `ea05ea5abed1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+218/-8，可读 patch 383 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Enable share expert fusion with router experts for Qwen3.5 BF16 & FP8」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD] Enable share expert fusion with router experts for Qwen3.5 BF16 & FP8」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +110/-3 (113 lines); hunks: -86,9 +86,11; -100,6 +102,8; symbols: __init__, _get_num_fused_shared_experts, get_embed_and_head，涉及 `__init__, _get_num_fused_shared_experts, get_embed_and_head`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +110/-3 (113 lines); hunks: -86,9 +86,11; -100,6 +102,8; symbols: __init__, _get_num_fused_shared_experts, get_embed_and_head
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -86,9 +86,11 @@
+    get_bool_env_var,
+    is_hip,
@@ -100,6 +102,8 @@
+_is_hip = is_hip()
+_use_aiter = get_bool_env_var("SGLANG_USE_AITER") and _is_hip
@@ -528,6 +532,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +110/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19484 - [CPU] Add Qwen3.5 model optimization for CPU

- 链接: https://github.com/sgl-project/sglang/pull/19484
- 状态/时间: merged / 2026-04-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `10fd0faccd85`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 20 个文件，+768/-209，可读 patch 1454 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CPU] Add Qwen3.5 model optimization for CPU」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[CPU] Add Qwen3.5 model optimization for CPU」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +37/-4 (41 lines); hunks: -124,8 +124,16 @@ def __init__(; -321,7 +329,20 @@ def weight_loader(param, loaded_weight, loaded_shard_id=None):; symbols: __init__, weight_loader, forward, load_weights，涉及 `__init__, weight_loader, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +37/-4 (41 lines); hunks: -124,8 +124,16 @@ def __init__(; -321,7 +329,20 @@ def weight_loader(param, loaded_weight, loaded_shard_id=None):; symbols: __init__, weight_loader, forward, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -124,8 +124,16 @@ def __init__(
-        self.num_v_heads = config.linear_num_value_heads
-        self.num_k_heads = config.linear_num_key_heads
+        self.num_v_heads = (
+            config.linear_num_value_heads
+            if not _is_cpu
+            else config.linear_num_value_heads_cpu
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +37/-4
- 验证与风险: diff 自带测试面 `test/srt/cpu/test_mamba.py`, `test/srt/cpu/test_qwen3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #20918 - [NPU] Support MTP for Qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/20918
- 状态/时间: merged / 2026-04-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `32c3513816b0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+809/-10，可读 patch 963 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Support MTP for Qwen3.5」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[NPU] Support MTP for Qwen3.5」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +23/-1 (24 lines); hunks: -15,13 +15,15; -31,7 +33,8; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +23/-1 (24 lines); hunks: -15,13 +15,15; -31,7 +33,8; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -15,13 +15,15 @@
+from contextlib import ExitStack
+from sglang.srt.environ import envs
@@ -31,7 +33,8 @@
-from sglang.srt.utils import add_prefix
+from sglang.srt.server_args import get_global_server_args
+from sglang.srt.utils import add_prefix, is_npu
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +23/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23471 - [Fix] NVFP4 qwen3.5 quant error fix by add packed_modules_mapping

- 链接: https://github.com/sgl-project/sglang/pull/23471
- 状态/时间: merged / 2026-04-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `9814cc89ce03`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-13，可读 patch 45 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] NVFP4 qwen3.5 quant error fix by add packed_modules_mapping」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Fix] NVFP4 qwen3.5 quant error fix by add packed_modules_mapping」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +11/-13 (24 lines); hunks: -900,13 +900,12 @@ def forward(; -1345,9 +1344,9 @@ def load_fused_expert_weights(; symbols: forward, Qwen3_5ForCausalLM, __init__, load_fused_expert_weights，涉及 `forward, Qwen3_5ForCausalLM, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +11/-13 (24 lines); hunks: -900,13 +900,12 @@ def forward(; -1345,9 +1344,9 @@ def load_fused_expert_weights(; symbols: forward, Qwen3_5ForCausalLM, __init__, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -900,13 +900,12 @@ def forward(
-    if _is_gfx95 or _is_npu:
-        packed_modules_mapping = {
-            "qkv_proj": ["q_proj", "k_proj", "v_proj"],
-            "gate_up_proj": ["gate_proj", "up_proj"],
-            "in_proj_qkvz": ["in_proj_qkv", "in_proj_z"],
-            "in_proj_ba": ["in_proj_b", "in_proj_a"],
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +11/-13
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23815 - [NPU] Fix DeepEP LL dispatch BF16 flag and skip triton kernel on NPU for Qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/23815
- 状态/时间: merged / 2026-04-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `08699bb1b2d3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+12/-2，可读 patch 37 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Fix DeepEP LL dispatch BF16 flag and skip triton kernel on NPU for Qwen3.5」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[NPU] Fix DeepEP LL dispatch BF16 flag and skip triton kernel on NPU for Qwen3.5」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +7/-1 (8 lines); hunks: -464,7 +464,11 @@ def forward(; -488,6 +492,8 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +7/-1 (8 lines); hunks: -464,7 +464,11 @@ def forward(; -488,6 +492,8 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -464,7 +464,11 @@ def forward(
-        if self.num_v_heads // self.num_k_heads in [1, 2, 4] and not _is_cpu:
+        if (
+            self.num_v_heads // self.num_k_heads in [1, 2, 4]
+            and not _is_cpu
+            and not _is_npu
+        ):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +7/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23594 - LoRA support for qwen3.5 and nemotron3

- 链接: https://github.com/sgl-project/sglang/pull/23594
- 状态/时间: merged / 2026-04-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py`；关联提交 `c8c1c9261d72`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 21 个文件，+1131/-127，可读 patch 1734 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「LoRA support for qwen3.5 and nemotron3」；模型线: Qwen3.5；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py`；技术摘要: 覆盖「LoRA support for qwen3.5 and nemotron3」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +76/-0 (76 lines); hunks: -945,6 +945,65 @@ class Qwen3_5ForCausalLM(nn.Module):; -1386,6 +1445,8 @@ class Qwen3_5ForConditionalGeneration(Qwen3VLForConditiona...; symbols: Qwen3_5ForCausalLM, get_hidden_dim, __init__, Qwen3_5ForConditionalGeneration，涉及 `Qwen3_5ForCausalLM, get_hidden_dim, __init__`；`test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: kl_v2, get_prompt_logprobs, TestLoRAQwen3_5_35B_A3B_LogprobDiff, test_lora_qwen3_5_35b_a3b_logprob_accuracy，涉及 `kl_v2, get_prompt_logprobs, TestLoRAQwen3_5_35B_A3B_LogprobDiff`；`test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: kl_v2, get_prompt_logprobs, TestLoRAQwen3_5_4BLogprobDiff, test_lora_qwen3_5_4b_logprob_accuracy，涉及 `kl_v2, get_prompt_logprobs, TestLoRAQwen3_5_4BLogprobDiff`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +76/-0 (76 lines); hunks: -945,6 +945,65 @@ class Qwen3_5ForCausalLM(nn.Module):; -1386,6 +1445,8 @@ class Qwen3_5ForConditionalGeneration(Qwen3VLForConditiona...; symbols: Qwen3_5ForCausalLM, get_hidden_dim, __init__, Qwen3_5ForConditionalGeneration
  - `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: kl_v2, get_prompt_logprobs, TestLoRAQwen3_5_35B_A3B_LogprobDiff, test_lora_qwen3_5_35b_a3b_logprob_accuracy
  - `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: kl_v2, get_prompt_logprobs, TestLoRAQwen3_5_4BLogprobDiff, test_lora_qwen3_5_4b_logprob_accuracy
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -945,6 +945,65 @@ class Qwen3_5ForCausalLM(nn.Module):
+    supported_lora_modules = [
+        "qkv_proj",
+        "o_proj",
+        "out_proj",
+        "in_proj_qkvz",
+        "gate_up_proj",
diff -- test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py
@@ -0,0 +1,157 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py
@@ -0,0 +1,146 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +76/-0
  - tests: `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py` added +157/-0; `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py` added +146/-0
- 验证与风险: diff 自带测试面 `test/registered/lora/test_chunked_sgmv_backend.py`, `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23062 - [bugfix]fix(qwen3_5): broadcast per-tensor scale in _make_packed_weight_loader for FP8 models

- 链接: https://github.com/sgl-project/sglang/pull/23062
- 状态/时间: merged / 2026-04-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py`；关联提交 `936c9c235596`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+220/-7，可读 patch 235 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[bugfix]fix(qwen3_5): broadcast per-tensor scale in _make_packed_weight_loader for FP8 models」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py`, `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[bugfix]fix(qwen3_5): broadcast per-tensor scale in _make_packed_weight_loader for FP8 models」；主要实现面是 `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py`, `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py` added +216/-0 (216 lines); hunks: -0,0 +1,216; symbols: _make_mock_module, _make_per_tensor_scale_param, TestMakePackedWeightLoader, test_scalar_weight_broadcast，涉及 `_make_mock_module, _make_per_tensor_scale_param, TestMakePackedWeightLoader`；`python/sglang/srt/models/qwen3_5.py` modified +4/-7 (11 lines); hunks: -320,13 +320,10 @@ def weight_loader(param, loaded_weight, loaded_shard_id=No...; symbols: weight_loader，涉及 `weight_loader`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py` added +216/-0 (216 lines); hunks: -0,0 +1,216; symbols: _make_mock_module, _make_per_tensor_scale_param, TestMakePackedWeightLoader, test_scalar_weight_broadcast
  - `python/sglang/srt/models/qwen3_5.py` modified +4/-7 (11 lines); hunks: -320,13 +320,10 @@ def weight_loader(param, loaded_weight, loaded_shard_id=No...; symbols: weight_loader
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_qwen3_5_packed_weight_loader.py
@@ -0,0 +1,216 @@
+"""
+Unit tests for Qwen3_5GatedDeltaNet._make_packed_weight_loader.
+Validates that per-tensor FP8 scales (scalar or single-element tensors)
+are broadcast to every logical shard, while normal multi-element weights
+are split correctly.
+Regression test for https://github.com/sgl-project/sglang/issues/23051
diff -- python/sglang/srt/models/qwen3_5.py
@@ -320,13 +320,10 @@ def weight_loader(param, loaded_weight, loaded_shard_id=None):
-                if len(loaded_weight.shape) == 0:
-                    # Scalar only makes sense for a single logical shard.
-                    assert len(split_sizes) == 1 and split_sizes[0] == 1, (
-                        f"Unexpected scalar for tuple shard load: "
-                        f"{loaded_shard_id=}, {split_sizes=}"
-                    )
```

- 已读文件:
  - tests: `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py` added +216/-0
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +4/-7
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_qwen3_5_packed_weight_loader.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23146 - [AMD] Enable EAGLE speculative decoding for Qwen3.5 FP8 and MXFP4 models with aiter's unified attention

- 链接: https://github.com/sgl-project/sglang/pull/23146
- 状态/时间: merged / 2026-05-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `c2db19ffa40e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+588/-148，可读 patch 964 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Enable EAGLE speculative decoding for Qwen3.5 FP8 and MXFP4 models with aiter's unified attention」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[AMD] Enable EAGLE speculative decoding for Qwen3.5 FP8 and MXFP4 models with aiter's unified attention」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +12/-0 (12 lines); hunks: -62,6 +62,18 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +12/-0 (12 lines); hunks: -62,6 +62,18 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -62,6 +62,18 @@ def __init__(
+        # Quark-quantized Qwen3.5 MXFP4 checkpoints ship the MTP module in
+        # bf16; every `mtp.*` layer appears under the quantization exclude
+        # list. Detect that and skip quantization here so linear/MoE weight
+        # loaders allocate bf16 shapes (see sgl-project/sglang#23113).
+        if quant_config and quant_config.get_name() == "quark":
+            exclude_layers = getattr(quant_config, "exclude_layers", [])
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +12/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/triton_ops/aiter_unified_attention.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23331 - [BugFix] Resolve adaptive speculative decoding conflicts for Qwen3.5 (hybrid GDN)

- 链接: https://github.com/sgl-project/sglang/pull/23331
- 状态/时间: merged / 2026-05-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `b9c2bf717ba4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+156/-68，可读 patch 444 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix] Resolve adaptive speculative decoding conflicts for Qwen3.5 (hybrid GDN)」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[BugFix] Resolve adaptive speculative decoding conflicts for Qwen3.5 (hybrid GDN)」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +4/-0 (4 lines); hunks: -14,6 +14,7; -51,6 +52,9 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +4/-0 (4 lines); hunks: -14,6 +14,7; -51,6 +52,9 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -14,6 +14,7 @@
+import copy
@@ -51,6 +52,9 @@ def __init__(
+        # Deep-copy so MTP mutations below don't leak into the target's config.
+        config = copy.deepcopy(config)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +4/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/spec/test_adaptive_spec_params.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23925 - [NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next

- 链接: https://github.com/sgl-project/sglang/pull/23925
- 状态/时间: merged / 2026-05-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `55ba03db6a46`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+194/-19，可读 patch 284 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +52/-8 (60 lines); hunks: -109,6 +109,11; -841,15 +846,8 @@ def _apply_qk_norm(; symbols: Qwen3_5GatedDeltaNet, __init__, _apply_qk_norm, self_attention，涉及 `Qwen3_5GatedDeltaNet, __init__, _apply_qk_norm`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +52/-8 (60 lines); hunks: -109,6 +109,11; -841,15 +846,8 @@ def _apply_qk_norm(; symbols: Qwen3_5GatedDeltaNet, __init__, _apply_qk_norm, self_attention
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -109,6 +109,11 @@
+if _is_npu:
+    from sgl_kernel_npu.norm.split_qkv_rmsnorm_rope import (
+        split_qkvgate_gemma_rmsnorm_rope,
+    )
@@ -841,15 +846,8 @@ def _apply_qk_norm(
-    def self_attention(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +52/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25885 - [AMD] Support alt stream for Qwen3.5 on AMD platform

- 链接: https://github.com/sgl-project/sglang/pull/25885
- 状态/时间: merged / 2026-06-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `7f919edf006b`, `d5899b95c4d5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+26/-7，可读 patch 90 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Support alt stream for Qwen3.5 on AMD platform」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD] Support alt stream for Qwen3.5 on AMD platform」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +26/-7 (33 lines); hunks: -105,10 +105,24; -445,6 +459,7 @@ def _forward_input_proj(self, hidden_states: torch.Tensor):; symbols: _disable_shared_experts_fusion, _forward_input_proj, __init__, _apply_qk_norm，涉及 `_disable_shared_experts_fusion, _forward_input_proj, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +26/-7 (33 lines); hunks: -105,10 +105,24; -445,6 +459,7 @@ def _forward_input_proj(self, hidden_states: torch.Tensor):; symbols: _disable_shared_experts_fusion, _forward_input_proj, __init__, _apply_qk_norm
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -105,10 +105,24 @@
+_hip_use_alt_stream = get_bool_env_var("SGLANG_ALT_STREAM") and _is_hip
+_gdn_use_alt_stream = (
+    get_bool_env_var("SGLANG_GDN_QKVZ_BA_ALT_STREAM", "False") and _hip_use_alt_stream
+)
+_qknorm_use_alt_stream = (
+    get_bool_env_var("SGLANG_QK_NORM_ALT_STREAM", "False") and _hip_use_alt_stream
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +26/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27656 - [AMD][Perf] Fuse QK RMSNorm + gate extraction Triton kernel for Qwen3.5 on HIP

- 链接: https://github.com/sgl-project/sglang/pull/27656
- 状态/时间: merged / 2026-06-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `0da18f8d916e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+315/-7，可读 patch 371 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Perf] Fuse QK RMSNorm + gate extraction Triton kernel for Qwen3.5 on HIP」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD][Perf] Fuse QK RMSNorm + gate extraction Triton kernel for Qwen3.5 on HIP」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +37/-3 (40 lines); hunks: -79,7 +79,10; -884,6 +887,33 @@ def forward_prepare_native(self, positions, hidden_states):; symbols: forward_prepare_native, forward_prepare_hip, forward_prepare_npu, self_attention，涉及 `forward_prepare_native, forward_prepare_hip, forward_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +37/-3 (40 lines); hunks: -79,7 +79,10; -884,6 +887,33 @@ def forward_prepare_native(self, positions, hidden_states):; symbols: forward_prepare_native, forward_prepare_hip, forward_prepare_npu, self_attention
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -79,7 +79,10 @@
-from sglang.srt.models.utils import fused_qk_gemma_rmsnorm
+from sglang.srt.models.utils import (
+    fused_qk_gemma_rmsnorm,
+    fused_qk_gemma_rmsnorm_with_gate,
+)
@@ -884,6 +887,33 @@ def forward_prepare_native(self, positions, hidden_states):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +37/-3
- 验证与风险: diff 自带测试面 `python/sglang/jit_kernel/tests/test_fused_qk_gemma_rmsnorm_gate.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26924 - [4/N] Qwen3.5Opt: Overlap mamba verify update with draft extend

- 链接: https://github.com/sgl-project/sglang/pull/26924
- 状态/时间: merged / 2026-06-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `aea0e308537a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+534/-16，可读 patch 647 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[4/N] Qwen3.5Opt: Overlap mamba verify update with draft extend」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[4/N] Qwen3.5Opt: Overlap mamba verify update with draft extend」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +3/-10 (13 lines); hunks: -47,6 +47,7; -883,7 +884,7 @@ def forward_prepare_native(self, positions, hidden_states):; symbols: forward_prepare_native, self_attention，涉及 `forward_prepare_native, self_attention`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +3/-10 (13 lines); hunks: -47,6 +47,7; -883,7 +884,7 @@ def forward_prepare_native(self, positions, hidden_states):; symbols: forward_prepare_native, self_attention
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -47,6 +47,7 @@
+from sglang.srt.layers.elementwise import fused_sigmoid_mul
@@ -883,7 +884,7 @@ def forward_prepare_native(self, positions, hidden_states):
-            gate = gate.reshape(*orig_shape, -1)
+            # gate stays as 3D strided view; fused_sigmoid_mul handles it directly
@@ -970,15 +971,7 @@ def self_attention(
-            if _is_hip:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +3/-10
- 验证与风险: diff 自带测试面 `test/manual/layers/test_fused_gate_sigmoid_mul_add.py`, `test/manual/layers/test_fused_sigmoid_mul.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27869 - Fix Qwen3.5 deterministic batch-invariant logprobs

- 链接: https://github.com/sgl-project/sglang/pull/27869
- 状态/时间: merged / 2026-06-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/attention/test_qwen35_deterministic.py`；关联提交 `171037c3e73d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+56/-5，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Qwen3.5 deterministic batch-invariant logprobs」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `test/registered/attention/test_qwen35_deterministic.py`；技术摘要: 覆盖「Fix Qwen3.5 deterministic batch-invariant logprobs」；主要实现面是 `test/registered/attention/test_qwen35_deterministic.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/attention/test_qwen35_deterministic.py` added +44/-0 (44 lines); hunks: -0,0 +1,44; symbols: TestQwen35Fa3Deterministic, get_model, get_server_args，涉及 `TestQwen35Fa3Deterministic, get_model, get_server_args`。
- 代码 diff 细节:
  - `test/registered/attention/test_qwen35_deterministic.py` added +44/-0 (44 lines); hunks: -0,0 +1,44; symbols: TestQwen35Fa3Deterministic, get_model, get_server_args
- 关键代码摘录:

```diff
diff -- test/registered/attention/test_qwen35_deterministic.py
@@ -0,0 +1,44 @@
+"""
+Usage:
+cd test/srt
+python3 -m unittest test_qwen35_deterministic.TestQwen35Fa3Deterministic
+"""
+import unittest
```

- 已读文件:
  - tests: `test/registered/attention/test_qwen35_deterministic.py` added +44/-0
- 验证与风险: diff 自带测试面 `test/registered/attention/test_qwen35_deterministic.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27868 - fix(qwen3.5): keep CUDA dual-stream overlap (regressed by #25885)

- 链接: https://github.com/sgl-project/sglang/pull/27868
- 状态/时间: merged / 2026-06-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `d5899b95c4d5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-4，可读 patch 39 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(qwen3.5): keep CUDA dual-stream overlap (regressed by #25885)」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「fix(qwen3.5): keep CUDA dual-stream overlap (regressed by #25885)」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +12/-4 (16 lines); hunks: -119,10 +119,10; -594,7 +594,11 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +12/-4 (16 lines); hunks: -119,10 +119,10; -594,7 +594,11 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -119,10 +119,10 @@
-_gdn_use_alt_stream = (
+_gdn_use_alt_stream = _is_cuda or (
-_qknorm_use_alt_stream = (
+_qknorm_use_alt_stream = _is_cuda or (
@@ -594,7 +594,11 @@ def __init__(
-                alt_stream=(alt_stream if _disable_shared_experts_fusion() else None),
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +12/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27870 - [qwen3.5][XPU]Add XPU support for set_embed_and_head and fused QK RMSNorm kernel

- 链接: https://github.com/sgl-project/sglang/pull/27870
- 状态/时间: merged / 2026-06-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `bf231f01a3b3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+18/-8，可读 patch 75 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[qwen3.5][XPU]Add XPU support for set_embed_and_head and fused QK RMSNorm kernel」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[qwen3.5][XPU]Add XPU support for set_embed_and_head and fused QK RMSNorm kernel」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +18/-8 (26 lines); hunks: -105,6 +105,7; -116,6 +117,7; symbols: _apply_qk_norm, forward_prepare_native, forward_prepare_hip, forward_prepare_fused_gate，涉及 `_apply_qk_norm, forward_prepare_native, forward_prepare_hip`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +18/-8 (26 lines); hunks: -105,6 +105,7; -116,6 +117,7; symbols: _apply_qk_norm, forward_prepare_native, forward_prepare_hip, forward_prepare_fused_gate
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -105,6 +105,7 @@
+    is_xpu,
@@ -116,6 +117,7 @@
+_is_xpu = is_xpu()
@@ -867,7 +869,7 @@ def _apply_qk_norm(
-        elif _is_hip:
+        elif _is_hip or _is_xpu:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +18/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28320 - Fused QK GemmaRMSNorm + RoPE + gate kernel for Qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/28320
- 状态/时间: merged / 2026-06-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `4a8200565e1c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+244/-7，可读 patch 292 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fused QK GemmaRMSNorm + RoPE + gate kernel for Qwen3.5」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「Fused QK GemmaRMSNorm + RoPE + gate kernel for Qwen3.5」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +40/-1 (41 lines); hunks: -137,6 +137,11 @@ def _disable_shared_experts_fusion() -> bool:; -887,6 +892,35 @@ def _apply_qk_norm(; symbols: _disable_shared_experts_fusion, _apply_qk_norm, forward_prepare_cuda_fused, forward_prepare_native，涉及 `_disable_shared_experts_fusion, _apply_qk_norm, forward_prepare_cuda_fused`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +40/-1 (41 lines); hunks: -137,6 +137,11 @@ def _disable_shared_experts_fusion() -> bool:; -887,6 +892,35 @@ def _apply_qk_norm(; symbols: _disable_shared_experts_fusion, _apply_qk_norm, forward_prepare_cuda_fused, forward_prepare_native
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -137,6 +137,11 @@ def _disable_shared_experts_fusion() -> bool:
+if _is_cuda:
+    from sglang.srt.layers.fused_qk_rmsnorm_rope_gate import (
+        fused_qk_gemma_rmsnorm_rope_gate,
+    )
@@ -887,6 +892,35 @@ def _apply_qk_norm(
+    def forward_prepare_cuda_fused(self, positions, hidden_states):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +40/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31171 - [CPU] add fused input proj for qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/31171
- 状态/时间: merged / 2026-07-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `41e0b4b3695e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+238/-94，可读 patch 471 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CPU] add fused input proj for qwen3.5」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[CPU] add fused input proj for qwen3.5」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +33/-18 (51 lines); hunks: -112,6 +112,7; -152,6 +153,9 @@ def _disable_shared_experts_fusion() -> bool:; symbols: _disable_shared_experts_fusion, __init__, _forward_input_proj, forward，涉及 `_disable_shared_experts_fusion, __init__, _forward_input_proj`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +33/-18 (51 lines); hunks: -112,6 +112,7; -152,6 +153,9 @@ def _disable_shared_experts_fusion() -> bool:; symbols: _disable_shared_experts_fusion, __init__, _forward_input_proj, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -112,6 +112,7 @@
+    use_intel_amx_backend,
@@ -152,6 +153,9 @@ def _disable_shared_experts_fusion() -> bool:
+    fused_qkvzba_split_reshape_cat_contiguous = (
+        torch.ops.sgl_kernel.fused_qkvzba_split_reshape_cat_contiguous_cpu
+    )
@@ -233,6 +237,17 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +33/-18
- 验证与风险: diff 自带测试面 `test/registered/cpu/test_qwen3.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31174 - fix: Qwen3.5-35B-A3B-AWQ w2_weight KeyError and related params for CPU

- 链接: https://github.com/sgl-project/sglang/pull/31174
- 状态/时间: merged / 2026-07-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `302c3b97d2d0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+3/-1，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: Qwen3.5-35B-A3B-AWQ w2_weight KeyError and related params for CPU」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「fix: Qwen3.5-35B-A3B-AWQ w2_weight KeyError and related params for CPU」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +1/-1 (2 lines); hunks: -301,7 +301,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +1/-1 (2 lines); hunks: -301,7 +301,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -301,7 +301,7 @@ def __init__(
-            dtype=config.torch_dtype,
+            dtype=torch.get_default_dtype(),
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/awq/awq.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24651 - [AMD] Add fused all-reduce RMSNorm per-group quant for Qwen3.5 FP8

- 链接: https://github.com/sgl-project/sglang/pull/24651
- 状态/时间: merged / 2026-07-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py`；关联提交 `e8e765b9d657`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+1192/-8，可读 patch 1376 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add fused all-reduce RMSNorm per-group quant for Qwen3.5 FP8」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py`；技术摘要: 覆盖「[AMD] Add fused all-reduce RMSNorm per-group quant for Qwen3.5 FP8」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +115/-0 (115 lines); hunks: -157,6 +157,56 @@ def _disable_shared_experts_fusion() -> bool:; -490,6 +540,14 @@ def fix_query_key_value_ordering(; symbols: _disable_shared_experts_fusion, _enable_qwen35_fused_ar_quant, _linear_accepts_fp8_tuple, _select_fused_ar_input_for_linear，涉及 `_disable_shared_experts_fusion, _enable_qwen35_fused_ar_quant, _linear_accepts_fp8_tuple`；`test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py` added +234/-0 (234 lines); hunks: -0,0 +1,234; symbols: FusionVariant, _base_url_with_port_offset, get_fusion_variants, _parse_gsm8k_metrics，涉及 `FusionVariant, _base_url_with_port_offset, get_fusion_variants`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +115/-0 (115 lines); hunks: -157,6 +157,56 @@ def _disable_shared_experts_fusion() -> bool:; -490,6 +540,14 @@ def fix_query_key_value_ordering(; symbols: _disable_shared_experts_fusion, _enable_qwen35_fused_ar_quant, _linear_accepts_fp8_tuple, _select_fused_ar_input_for_linear
  - `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py` added +234/-0 (234 lines); hunks: -0,0 +1,234; symbols: FusionVariant, _base_url_with_port_offset, get_fusion_variants, _parse_gsm8k_metrics
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -157,6 +157,56 @@ def _disable_shared_experts_fusion() -> bool:
+@lru_cache(maxsize=1)
+def _enable_qwen35_fused_ar_quant() -> bool:
+    """Gate the fused AR+RMSNorm+per-group-FP8-quant path for Qwen3.5.
+    The single-kernel backend is ROCm/aiter/gfx95-only. The model gate stays
+    tied to ROCm/aiter so non-gfx95 HIP can keep the existing 2-kernel fallback
+    behavior for tuple handoff when this branch is used. It replaces the
diff -- test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py
@@ -0,0 +1,234 @@
+"""MI35x PR-CI accuracy coverage for Qwen3.5-FP8 aiter AR-fusion.
+PR-specific fused AR+RMSNorm+per-group-quant accuracy check. The file runs in
+the 8-GPU MI35x stage-c suite and launches two TP4 servers in parallel:
+* GPUs 0-3: fused AR+RMSNorm+per-group FP8 quant enabled.
+* GPUs 4-7: same launch with SGLANG_DISABLE_FUSED_AR_QUANT=1 fallback.
+Each server runs GSM8K and reports accuracy, invalid rate, latency, and output
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +115/-0
  - tests: `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py` added +234/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #32401 - [Model] Support standalone text-only Qwen3.5 checkpoints

- 链接: https://github.com/sgl-project/sglang/pull/32401
- 状态/时间: merged / 2026-07-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_text.py`；关联提交 `fc8b328f5cb5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+222/-1，可读 patch 259 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Support standalone text-only Qwen3.5 checkpoints」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_5_text.py`；技术摘要: 覆盖「[Model] Support standalone text-only Qwen3.5 checkpoints」；主要实现面是 `python/sglang/srt/models/qwen3_5_text.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_text.py` added +208/-0 (208 lines); hunks: -0,0 +1,208; symbols: Qwen3_5ForCausalLM, __init__, start_layer, end_layer，涉及 `Qwen3_5ForCausalLM, __init__, start_layer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_text.py` added +208/-0 (208 lines); hunks: -0,0 +1,208; symbols: Qwen3_5ForCausalLM, __init__, start_layer, end_layer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_text.py
@@ -0,0 +1,208 @@
+# Copyright 2025 Qwen Team
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_text.py` added +208/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_5_text.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #32022 - fix(qwen3.5): restrict MoE weights to local PP layers

- 链接: https://github.com/sgl-project/sglang/pull/32022
- 状态/时间: merged / 2026-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `e4f7f7b3807b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-3，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(qwen3.5): restrict MoE weights to local PP layers」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「fix(qwen3.5): restrict MoE weights to local PP layers」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +3/-3 (6 lines); hunks: -2288,9 +2288,9 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights，涉及 `load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +3/-3 (6 lines); hunks: -2288,9 +2288,9 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -2288,9 +2288,9 @@ def load_fused_expert_weights(
-                layer_id: layer.mlp.get_moe_weights()
-                for layer_id, layer in enumerate(self.model.layers)
-                if isinstance(layer.mlp, Qwen2MoeSparseMoeBlock)
+                layer_id: self.model.layers[layer_id].mlp.get_moe_weights()
+                for layer_id in range(self.model.start_layer, self.model.end_layer)
+                if isinstance(self.model.layers[layer_id].mlp, Qwen2MoeSparseMoeBlock)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +3/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31220 - Qwen3.5-MoE: support modelopt_fp4 checkpoints that quantize attention (+ load baked FP8 KV scales)

- 链接: https://github.com/sgl-project/sglang/pull/31220
- 状态/时间: merged / 2026-07-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py`；关联提交 `c4af6cf26397`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+177/-14，可读 patch 269 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Qwen3.5-MoE: support modelopt_fp4 checkpoints that quantize attention (+ load baked FP8 KV scales)」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py`, `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「Qwen3.5-MoE: support modelopt_fp4 checkpoints that quantize attention (+ load baked FP8 KV scales)」；主要实现面是 `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py`, `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: TestModelOptFp4AttentionExclusion, test_moe_only_checkpoint_excludes_attention, test_uniform_w4a4_checkpoint_quantizes_attention, TestRadixAttentionKvScaleRegistration，涉及 `TestModelOptFp4AttentionExclusion, test_moe_only_checkpoint_excludes_attention, test_uniform_w4a4_checkpoint_quantizes_attention`；`python/sglang/srt/models/qwen3_5.py` modified +20/-14 (34 lines); hunks: -87,6 +87,7; -700,13 +701,8 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: TestModelOptFp4AttentionExclusion, test_moe_only_checkpoint_excludes_attention, test_uniform_w4a4_checkpoint_quantizes_attention, TestRadixAttentionKvScaleRegistration
  - `python/sglang/srt/models/qwen3_5.py` modified +20/-14 (34 lines); hunks: -87,6 +87,7; -700,13 +701,8 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_qwen3_5_modelopt_fp4.py
@@ -0,0 +1,157 @@
+"""Unit tests for modelopt_fp4 checkpoints that quantize Qwen3.5 attention.
+Covers three things:
+  1. ModelOptFp4Config.is_layer_excluded() decides per prefix whether attention is
+     quantized or kept in BF16.
+  2. RadixAttention registers k_scale/v_scale when built with a quant_config that
+     declares kv_cache_quant_algo; without them, baked KV scales have nowhere to
diff -- python/sglang/srt/models/qwen3_5.py
@@ -87,6 +87,7 @@
+    WeightsMapper,
@@ -700,13 +701,8 @@ def __init__(
-        linear_attn_quant_config = (
-            None
-            if quant_config and quant_config.get_name() == "modelopt_fp4"
-            else quant_config
```

- 已读文件:
  - tests: `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py` added +157/-0
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +20/-14
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #32945 - Qwen3.5 NVFP4 V2

- 链接: https://github.com/sgl-project/sglang/pull/32945
- 状态/时间: merged / 2026-08-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `115cd7bde1b5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-4，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Qwen3.5 NVFP4 V2」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；技术摘要: 覆盖「Qwen3.5 NVFP4 V2」；主要实现面是 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-2 (4 lines); hunks: -42,7 +42,7 @@ Qwen3.5 features a Gated Delta Networks combined with sparse M...; -156,7 +156,7 @@ This section provides deployment configurations optimized fo...；`docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +2/-2 (4 lines); hunks: -318,10 +318,10 @@ export const Qwen35Deployment = () => {。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-2 (4 lines); hunks: -42,7 +42,7 @@ Qwen3.5 features a Gated Delta Networks combined with sparse M...; -156,7 +156,7 @@ This section provides deployment configurations optimized fo...
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +2/-2 (4 lines); hunks: -318,10 +318,10 @@ export const Qwen35Deployment = () => {
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -42,7 +42,7 @@ Qwen3.5 features a Gated Delta Networks combined with sparse Mixture-of-Experts
-      <td style={{padding: "9px 12px", backgroundColor: "rgba(255,255,255,0.05)"}}>NVIDIA NVFP4: [nvidia/Qwen3.5-397B-A17B-NVFP4](https://huggingface.co/nvidia/Qwen3.5-397B-A17B-N
+      <td style={{padding: "9px 12px", backgroundColor: "rgba(255,255,255,0.05)"}}>NVIDIA NVFP4: [nvidia/Qwen3.5-397B-A17B-NVFP4-V2](https://huggingface.co/nvidia/Qwen3.5-397B-A17
@@ -156,7 +156,7 @@ This section provides deployment configurations optimized for different hardware
-    - **FP4**: The FP4 quantized model requires ~250GB for weights, cutting memory by almost 4x. NVFP4 ([nvidia/Qwen3.5-397B-A17B-NVFP4](https://huggingface.co/nvidia/Qwen3.5-397B
+    - **FP4**: The FP4 quantized model requires ~250GB for weights, cutting memory by almost 4x. NVFP4 ([nvidia/Qwen3.5-397B-A17B-NVFP4-V2](https://huggingface.co/nvidia/Qwen3.5-3
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -318,10 +318,10 @@ export const Qwen35Deployment = () => {
-      // AMD MI355X uses the MXFP4 checkpoint; Blackwell uses NVFP4.
+      // AMD MI355X uses the MXFP4 checkpoint; Blackwell uses NVFP4-V2.
-        : 'nvidia/Qwen3.5-397B-A17B-NVFP4';
+        : 'nvidia/Qwen3.5-397B-A17B-NVFP4-V2';
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-2; `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +2/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #22867 - [feat] Add language_model_only parameter support for Qwen35

- 链接: https://github.com/sgl-project/sglang/pull/22867
- 状态/时间: merged / 2026-08-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `bfeb9a8af29c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+118/-47，可读 patch 266 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[feat] Add language_model_only parameter support for Qwen35」；模型线: Qwen3.5；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[feat] Add language_model_only parameter support for Qwen35」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +13/-4 (17 lines); hunks: -1786,9 +1786,13 @@ def __init__(; -1944,9 +1948,14 @@ def __init__(; symbols: __init__, get_hidden_dim，涉及 `__init__, get_hidden_dim`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +13/-4 (17 lines); hunks: -1786,9 +1786,13 @@ def __init__(; -1944,9 +1948,14 @@ def __init__(; symbols: __init__, get_hidden_dim
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -1786,9 +1786,13 @@ def __init__(
-        self.is_mrope_enabled = "mrope_section" in rope_config
+        self.is_mrope_enabled = (
+            not self.language_model_only and "mrope_section" in rope_config
+        )
-        self.deepstack_visual_indexes = self.visual.deepstack_visual_indexes
+        self.deepstack_visual_indexes = (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +13/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34357 - Update Qwen3.5 B200 NVFP4 MTP config

- 链接: https://github.com/sgl-project/sglang/pull/34357
- 状态/时间: merged / 2026-08-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `857910bd35e2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+8/-3，可读 patch 39 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update Qwen3.5 B200 NVFP4 MTP config」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「Update Qwen3.5 B200 NVFP4 MTP config」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +6/-1 (7 lines); hunks: -20,7 +20,7 @@ export const Qwen35Deployment = () => {; -315,6 +315,11 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-2 (4 lines); hunks: -157,7 +157,7 @@ This section provides deployment configurations optimized fo...; -191,7 +191,7 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +6/-1 (7 lines); hunks: -20,7 +20,7 @@ export const Qwen35Deployment = () => {; -315,6 +315,11 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-2 (4 lines); hunks: -157,7 +157,7 @@ This section provides deployment configurations optimized fo...; -191,7 +191,7 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -20,7 +20,7 @@ export const Qwen35Deployment = () => {
-  // FP4 (397B only): NVFP4 on Blackwell B200/B300 tp=4; AMD MXFP4 on MI355X tp=2
+  // FP4 (397B only): NVFP4 on Blackwell B200 tp=4 (tp=2 ep=2 w/ MTP) / B300 tp=4; AMD MXFP4 on MI355X tp=2
@@ -315,6 +315,11 @@ export const Qwen35Deployment = () => {
+    // 397B B200 NVFP4 with MTP: tp=2 with expert parallelism 2 (TEP2) beats
+    // tp=4 across the concurrency sweep.
+    if (model === '397b' && hardware === 'b200' && quantization === 'fp4' && speculative === 'enabled') {
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -157,7 +157,7 @@ This section provides deployment configurations optimized for different hardware
-        - **B200 (183GB)** runs with tp=4. (NVFP4)
+        - **B200 (183GB)** runs with tp=4 (tp=2 with expert parallelism 2 when MTP is enabled). (NVFP4)
@@ -191,7 +191,7 @@ This section provides deployment configurations optimized for different hardware
-      <td style={{padding: "9px 12px", backgroundColor: "rgba(255,255,255,0.02)"}}>4</td>
+      <td style={{padding: "9px 12px", backgroundColor: "rgba(255,255,255,0.02)"}}>4 / 2 + EP2 (MTP)</td>
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +6/-1; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #34421 - [AMD][Perf] Fuse GatedDeltaNet QKVZBA split/reshape/cat into a single Triton kernel for Qwen3.5-architecture MoE on HIP

- 链接: https://github.com/sgl-project/sglang/pull/34421
- 状态/时间: merged / 2026-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `b7f87a2513c2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+27/-2，可读 patch 64 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Perf] Fuse GatedDeltaNet QKVZBA split/reshape/cat into a single Triton kernel for Qwen3.5-architecture MoE on HIP」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD][Perf] Fuse GatedDeltaNet QKVZBA split/reshape/cat into a single Triton kernel for Qwen3.5-architecture MoE on HIP」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +11/-1 (12 lines); hunks: -136,6 +136,13; -636,7 +643,10 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +11/-1 (12 lines); hunks: -136,6 +136,13; -636,7 +643,10 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -136,6 +136,13 @@
+# Head-group ratios (num_v_heads // num_k_heads) served by the fused
+# split/reshape/cat Triton kernel. On AMD/aiter the ratio-8 layout is also
+# covered by the fused kernel, which removes the two `.contiguous()` copies
+# plus the `torch.cat` of the unfused fallback. Other backends keep the
+# original tuple so their control flow is unchanged.
+_GDN_FUSED_QKVZBA_RATIOS = (1, 2, 4, 8) if _use_aiter else (1, 2, 4)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +11/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34560 - [Fix] Fix Qwen3.5 MTP startup with HiCache

- 链接: https://github.com/sgl-project/sglang/pull/34560
- 状态/时间: merged / 2026-08-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/hicache/test_qwen35_hicache.py`；关联提交 `41cd5a718942`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+56/-3，可读 patch 108 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Fix Qwen3.5 MTP startup with HiCache」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `test/registered/hicache/test_qwen35_hicache.py`；技术摘要: 覆盖「[Fix] Fix Qwen3.5 MTP startup with HiCache」；主要实现面是 `test/registered/hicache/test_qwen35_hicache.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/hicache/test_qwen35_hicache.py` modified +8/-0 (8 lines); hunks: -57,6 +57,14 @@ def setUpClass(cls):; symbols: setUpClass，涉及 `setUpClass`。
- 代码 diff 细节:
  - `test/registered/hicache/test_qwen35_hicache.py` modified +8/-0 (8 lines); hunks: -57,6 +57,14 @@ def setUpClass(cls):; symbols: setUpClass
- 关键代码摘录:

```diff
diff -- test/registered/hicache/test_qwen35_hicache.py
@@ -57,6 +57,14 @@ def setUpClass(cls):
+                "--speculative-algorithm",
+                "NEXTN",
+                "--speculative-num-steps",
+                "3",
+                "--speculative-eagle-topk",
+                "1",
```

- 已读文件:
  - tests: `test/registered/hicache/test_qwen35_hicache.py` modified +8/-0
- 验证与风险: diff 自带测试面 `test/registered/hicache/test_qwen35_hicache.py`, `test/registered/unit/configs/test_model_config.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #34771 - [Spec] Wire DFLASH aux-hidden capture into the Qwen3.5 text-only wrapper

- 链接: https://github.com/sgl-project/sglang/pull/34771
- 状态/时间: merged / 2026-08-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_text.py`；关联提交 `a5ba081fbb8f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-0，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec] Wire DFLASH aux-hidden capture into the Qwen3.5 text-only wrapper」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5_text.py`；技术摘要: 覆盖「[Spec] Wire DFLASH aux-hidden capture into the Qwen3.5 text-only wrapper」；主要实现面是 `python/sglang/srt/models/qwen3_5_text.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_text.py` modified +10/-0 (10 lines); hunks: -118,6 +118,16 @@ def set_embed_and_head(self, embed, head):; symbols: set_embed_and_head, set_dflash_layers_to_capture, forward，涉及 `set_embed_and_head, set_dflash_layers_to_capture, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_text.py` modified +10/-0 (10 lines); hunks: -118,6 +118,16 @@ def set_embed_and_head(self, embed, head):; symbols: set_embed_and_head, set_dflash_layers_to_capture, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_text.py
@@ -118,6 +118,16 @@ def set_embed_and_head(self, embed, head):
+    def set_dflash_layers_to_capture(self, layers_to_capture: list[int]):
+        if not self.pp_group.is_last_rank:
+            return
+        if layers_to_capture is None:
+            raise ValueError(
+                "DFLASH requires explicit layer ids for aux hidden capture."
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_text.py` modified +10/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5_text.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34474 - [AMD] Qwen3.5: guard attn layers against empty DP-attention batch

- 链接: https://github.com/sgl-project/sglang/pull/34474
- 状态/时间: merged / 2026-08-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `24ab8f9ed9f7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-3，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Qwen3.5: guard attn layers against empty DP-attention batch」；模型线: Qwen3.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD] Qwen3.5: guard attn layers against empty DP-attention batch」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +6/-3 (9 lines); hunks: -683,7 +683,10 @@ def forward(; -790,7 +793,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +6/-3 (9 lines); hunks: -683,7 +683,10 @@ def forward(; -790,7 +793,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -683,7 +683,10 @@ def forward(
-        core_attn_out = core_attn_out.reshape(*core_attn_out.shape[:-2], -1)
+        core_attn_out = core_attn_out.reshape(
+            *core_attn_out.shape[:-2],
+            core_attn_out.shape[-2] * core_attn_out.shape[-1],
+        )
@@ -790,7 +793,7 @@ def forward(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +6/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35194 - Update Qwen3.5 H200 FP8 for AgentX HiCache MTP

- 链接: https://github.com/sgl-project/sglang/pull/35194
- 状态/时间: merged / 2026-08-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；关联提交 `91144797c517`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+39/-0，可读 patch 46 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update Qwen3.5 H200 FP8 for AgentX HiCache MTP」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「Update Qwen3.5 H200 FP8 for AgentX HiCache MTP」；主要实现面是 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +39/-0 (39 lines); hunks: -989,6 +989,45 @@ Max ITL (ms): 1220.68。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +39/-0 (39 lines); hunks: -989,6 +989,45 @@ Max ITL (ms): 1220.68
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -989,6 +989,45 @@ Max ITL (ms):                            1220.68
+#### 5.2.3 Agentic Long-Context with HiCache DRAM Offload (H200 FP8, MTP)
+For agentic workloads, here is how to enable HiCache and MTP.
+Container image (pinned for reproducibility):
+`lmsysorg/sglang:nightly-dev-cu13-20260815-a5ba081f`.
+Server Launch Command:
+'''bash Command
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +39/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #35445 - [AMD] cookbook: serve Qwen3.5 MXFP4 on MI355X with an fp8_e4m3 KV cache

- 链接: https://github.com/sgl-project/sglang/pull/35445
- 状态/时间: merged / 2026-08-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `574274660f78`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] cookbook: serve Qwen3.5 MXFP4 on MI355X with an fp8_e4m3 KV cache」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；技术摘要: 覆盖「[AMD] cookbook: serve Qwen3.5 MXFP4 on MI355X with an fp8_e4m3 KV cache」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +1/-0 (1 lines); hunks: -480,6 +480,7 @@ export const Qwen35Deployment = () => {。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +1/-0 (1 lines); hunks: -480,6 +480,7 @@ export const Qwen35Deployment = () => {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -480,6 +480,7 @@ export const Qwen35Deployment = () => {
+        cmd += ' \\\n  --kv-cache-dtype fp8_e4m3';
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +1/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #33354 - [XPU] Use a fused GDN kernel from sgl-kernel for Qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/33354
- 状态/时间: merged / 2026-08-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py`；关联提交 `5b5b29d4e2a6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+307/-3，可读 patch 409 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[XPU] Use a fused GDN kernel from sgl-kernel for Qwen3.5」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py`；技术摘要: 覆盖「[XPU] Use a fused GDN kernel from sgl-kernel for Qwen3.5」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +45/-0 (45 lines); hunks: -136,6 +136,7; -659,6 +660,40 @@ def _forward_input_proj_fused_quant_amd(self, hidden_states):; symbols: _forward_input_proj_fused_quant_amd, _forward_xpu, forward，涉及 `_forward_input_proj_fused_quant_amd, _forward_xpu, forward`；`test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py` modified +23/-3 (26 lines); hunks: -1,6 +1,8; -18,9 +20,9; symbols: TestQwen3_5_9BXPU, Qwen3_5_9BXPUBase, TestQwen3_5_9BXPUDefault, TestQwen3_5_9BXPUFusedGDN，涉及 `TestQwen3_5_9BXPU, Qwen3_5_9BXPUBase, TestQwen3_5_9BXPUDefault`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +45/-0 (45 lines); hunks: -136,6 +136,7; -659,6 +660,40 @@ def _forward_input_proj_fused_quant_amd(self, hidden_states):; symbols: _forward_input_proj_fused_quant_amd, _forward_xpu, forward
  - `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py` modified +23/-3 (26 lines); hunks: -1,6 +1,8; -18,9 +20,9; symbols: TestQwen3_5_9BXPU, Qwen3_5_9BXPUBase, TestQwen3_5_9BXPUDefault, TestQwen3_5_9BXPUFusedGDN
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -136,6 +136,7 @@
+_is_xpu = is_xpu()
@@ -659,6 +660,40 @@ def _forward_input_proj_fused_quant_amd(self, hidden_states):
+    def _forward_xpu(
+        self,
+        backend: object,
+        projected_states_qkvz: torch.Tensor,
diff -- test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py
@@ -1,6 +1,8 @@
-Scored by ``simple_eval_gsm8k.GSM8KEval``.
+Scored by ``simple_eval_gsm8k.GSM8KEval``. Covers both the opt-in fused GDN
+SYCL kernel path (``--linear-attn-backend intel_xpu``) and the default Triton
+GDN path (``triton``, unchanged from other platforms).
@@ -18,9 +20,9 @@
-class TestQwen3_5_9BXPU(SimpleEvalGSM8KXPUMixin, CustomTestCase):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +45/-0
  - tests: `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py` modified +23/-3
- 验证与风险: diff 自带测试面 `test/registered/xpu/llm_models/test_xpu_qwen3_5_9b.py`, `test/registered/xpu/test_intel_xpu_linear_attn_dispatch.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35719 - [AMD] Fix Qwen3.5 MTP dropping fused shared-expert weights

- 链接: https://github.com/sgl-project/sglang/pull/35719
- 状态/时间: merged / 2026-08-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `0d5b5ae6202c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+24/-2，可读 patch 55 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix Qwen3.5 MTP dropping fused shared-expert weights」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[AMD] Fix Qwen3.5 MTP dropping fused shared-expert weights」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +24/-2 (26 lines); hunks: -39,10 +39,13; -244,12 +247,20 @@ def load_weights(; symbols: _mtp_quant_config, load_weights, load_fused_expert_weights，涉及 `_mtp_quant_config, load_weights, load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +24/-2 (26 lines); hunks: -39,10 +39,13; -244,12 +247,20 @@ def load_weights(; symbols: _mtp_quant_config, load_weights, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -39,10 +39,13 @@
-from sglang.srt.utils import add_prefix, is_npu
+from sglang.srt.utils import add_prefix, get_bool_env_var, is_hip, is_npu
+_is_hip = is_hip()
+_use_aiter = get_bool_env_var("SGLANG_USE_AITER") and _is_hip
@@ -244,12 +247,20 @@ def load_weights(
+        # A fused shared expert lives in routed slot `num_experts`.
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +24/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #36245 - [AMD] cookbook: add HiCache host-DRAM KV tier for Qwen3.5 MXFP4 on MI355X

- 链接: https://github.com/sgl-project/sglang/pull/36245
- 状态/时间: merged / 2026-08-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `9eee990ce15d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+26/-3，可读 patch 64 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] cookbook: add HiCache host-DRAM KV tier for Qwen3.5 MXFP4 on MI355X」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[AMD] cookbook: add HiCache host-DRAM KV tier for Qwen3.5 MXFP4 on MI355X」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +24/-2 (26 lines); hunks: -110,6 +110,17 @@ export const Qwen35Deployment = () => {; -296,7 +307,7 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-1 (3 lines); hunks: -128,6 +128,7 @@ This section provides deployment configurations optimized fo...; -225,7 +226,7 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +24/-2 (26 lines); hunks: -110,6 +110,17 @@ export const Qwen35Deployment = () => {; -296,7 +307,7 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-1 (3 lines); hunks: -128,6 +128,7 @@ This section provides deployment configurations optimized fo...; -225,7 +226,7 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -110,6 +110,17 @@ export const Qwen35Deployment = () => {
+    kvOffload: {
+      name: 'kvOffload',
+      title: 'KV Cache Offloading',
+      // HiCache adds a host-DRAM tier below the device KV cache. Only wired up
+      // for the MI355X MXFP4 recipe, which is the arm it is tuned on.
+      condition: (values) => values.hardware === 'mi355x' && values.quantization === 'fp4',
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -128,6 +128,7 @@ This section provides deployment configurations optimized for different hardware
+- **KV cache offloading (MXFP4 on MI355X):** Selecting **Host DRAM (HiCache)** adds a host-memory tier below the device KV cache, which lets long-context agentic workloads keep mo
@@ -225,7 +226,7 @@ This section provides deployment configurations optimized for different hardware
-**FP8 KV Cache**: `--kv-cache-dtype fp8_e4m3` quantizes the KV cache to FP8 at runtime. Since these FP8 model checkpoints do not include pre-calibrated KV cache scaling factors, S
+**FP8 KV Cache**: `--kv-cache-dtype fp8_e4m3` quantizes the KV cache to FP8 at runtime. Since these FP8 model checkpoints do not include pre-calibrated KV cache scaling factors, S
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +24/-2; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +2/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #35341 - [AMD][Fix] Qwen3.5: make empty-batch guard tuple-aware on fused AR+quant path

- 链接: https://github.com/sgl-project/sglang/pull/35341
- 状态/时间: merged / 2026-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `0c7d017dbbaa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-2，可读 patch 22 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Fix] Qwen3.5: make empty-batch guard tuple-aware on fused AR+quant path」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD][Fix] Qwen3.5: make empty-batch guard tuple-aware on fused AR+quant path」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +6/-2 (8 lines); hunks: -891,7 +891,9 @@ def forward(; -1295,7 +1297,9 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +6/-2 (8 lines); hunks: -891,7 +891,9 @@ def forward(; -1295,7 +1297,9 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -891,7 +891,9 @@ def forward(
-        if not forward_batch.forward_mode.is_idle() and hidden_states.shape[0] > 0:
+        # fused AR+quant hands down a (fp8, scale) / (bf16, fp8, scale) tuple
+        hs = hidden_states[0] if isinstance(hidden_states, tuple) else hidden_states
+        if not forward_batch.forward_mode.is_idle() and hs.shape[0] > 0:
@@ -1295,7 +1297,9 @@ def forward(
-        if not forward_batch.forward_mode.is_idle() and hidden_states.shape[0] > 0:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +6/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34446 - [rotary] Fix the fused Qwen3.5 RoPE kernel discarding mrope height and width

- 链接: https://github.com/sgl-project/sglang/pull/34446
- 状态/时间: merged / 2026-08-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `e635577431cb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+373/-37，可读 patch 518 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[rotary] Fix the fused Qwen3.5 RoPE kernel discarding mrope height and width」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[rotary] Fix the fused Qwen3.5 RoPE kernel discarding mrope height and width」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +1/-0 (1 lines); hunks: -1151,6 +1151,7 @@ def forward_prepare_cuda_fused(self, positions, hidden_sta...; symbols: forward_prepare_cuda_fused，涉及 `forward_prepare_cuda_fused`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +1/-0 (1 lines); hunks: -1151,6 +1151,7 @@ def forward_prepare_cuda_fused(self, positions, hidden_sta...; symbols: forward_prepare_cuda_fused
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -1151,6 +1151,7 @@ def forward_prepare_cuda_fused(self, positions, hidden_states):
+            mrope_axis_map=(self.rotary_emb.axis_map if positions.dim() == 2 else None),
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_fused_qk_rmsnorm_rope_gate.py`, `test/registered/rotary/test_mrope_axis_map.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37360 - docs(cookbook): enable FlashInfer GDN for Qwen3.5 B200

- 链接: https://github.com/sgl-project/sglang/pull/37360
- 状态/时间: merged / 2026-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `3315356cc043`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+9/-0，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「docs(cookbook): enable FlashInfer GDN for Qwen3.5 B200」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；技术摘要: 覆盖「docs(cookbook): enable FlashInfer GDN for Qwen3.5 B200」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +9/-0 (9 lines); hunks: -438,6 +438,15 @@ export const Qwen35Deployment = () => {。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +9/-0 (9 lines); hunks: -438,6 +438,15 @@ export const Qwen35Deployment = () => {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -438,6 +438,15 @@ export const Qwen35Deployment = () => {
+    // B200 NVFP4 with MTP runs TP2/EP2 (set above). Keep Triton as the base
+    // linear-attention backend while routing GDN decode and prefill through
+    // FlashInfer.
+    if (model === '397b' && hardware === 'b200' && quantization === 'fp4' && speculative === 'enabled') {
+      cmd += ` \\\n  --linear-attn-backend triton`;
+      cmd += ` \\\n  --linear-attn-decode-backend flashinfer`;
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +9/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #37471 - [Bugfix] Load Qwen3.5 MTP embedding under PP

- 链接: https://github.com/sgl-project/sglang/pull/37471
- 状态/时间: merged / 2026-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`, `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`；关联提交 `982aa8acfcfd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+52/-0，可读 patch 82 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Load Qwen3.5 MTP embedding under PP」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[Bugfix] Load Qwen3.5 MTP embedding under PP」；主要实现面是 `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`, `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py` modified +35/-0 (35 lines); hunks: -1,15 +1,30; -64,6 +79,26 @@ def test_get_num_fused_shared_experts_returns_zero_without_lo...; symbols: TestQwen3_5PipelineParallel, _make_mtp_weight_loader_stub, _get_num_fused_shared_experts, test_get_num_fused_shared_experts_returns_zero_without_local_fusion，涉及 `TestQwen3_5PipelineParallel, _make_mtp_weight_loader_stub, _get_num_fused_shared_experts`；`python/sglang/srt/models/qwen3_5_mtp.py` modified +17/-0 (17 lines); hunks: -323,6 +323,23 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights，涉及 `load_fused_expert_weights`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py` modified +35/-0 (35 lines); hunks: -1,15 +1,30; -64,6 +79,26 @@ def test_get_num_fused_shared_experts_returns_zero_without_lo...; symbols: TestQwen3_5PipelineParallel, _make_mtp_weight_loader_stub, _get_num_fused_shared_experts, test_get_num_fused_shared_experts_returns_zero_without_local_fusion
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +17/-0 (17 lines); hunks: -323,6 +323,23 @@ def load_fused_expert_weights(; symbols: load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_qwen3_5_pipeline_parallel.py
@@ -1,15 +1,30 @@
+import torch
+from sglang.srt.models.qwen3_5_mtp import Qwen3_5ForCausalLMMTP
+    @staticmethod
+    def _make_mtp_weight_loader_stub():
+        model = Qwen3_5ForCausalLMMTP.__new__(Qwen3_5ForCausalLMMTP)
+        torch.nn.Module.__init__(model)
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -323,6 +323,23 @@ def load_fused_expert_weights(
+            # The last-stage MTP draft cannot share the target embedding on PP0.
+            # Load the checkpoint embedding into its retained local copy instead
+            # of leaving the torch.empty() allocation uninitialized.
+            if name in (
+                "model.embed_tokens.weight",
+                "model.language_model.embed_tokens.weight",
```

- 已读文件:
  - tests: `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py` modified +35/-0
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +17/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36267 - [Performance] Optimize Qwen3.5 GDN prefill projection layouts

- 链接: https://github.com/sgl-project/sglang/pull/36267
- 状态/时间: merged / 2026-09-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `07199fa220cc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+386/-17，可读 patch 525 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Performance] Optimize Qwen3.5 GDN prefill projection layouts」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Performance] Optimize Qwen3.5 GDN prefill projection layouts」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +18/-4 (22 lines); hunks: -27,6 +27,7; -780,6 +781,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +18/-4 (22 lines); hunks: -27,6 +27,7; -780,6 +781,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -27,6 +27,7 @@
+    qwen3_5_gdn_prefill_projection_views,
@@ -780,6 +781,7 @@ def forward(
+        use_strided_prefill_z = False
@@ -803,7 +805,15 @@ def forward(
-            mixed_qkv, z, b, a = fused_qkvzba_split_reshape_cat_contiguous(
+            use_strided_prefill_z = (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +18/-4
- 验证与风险: diff 自带测试面 `test/registered/attention/test_gdn_prefill_layout.py`, `test/registered/unit/layers/attention/test_gdn_flashinfer_alignment.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38374 - docs(cookbook): Qwen3.5 FP8 on B200/B300 — trtllm-gen MoE + symm mem

- 链接: https://github.com/sgl-project/sglang/pull/38374
- 状态/时间: merged / 2026-09-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `f4bbf12423b8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+16/-3，可读 patch 47 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「docs(cookbook): Qwen3.5 FP8 on B200/B300 — trtllm-gen MoE + symm mem」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「docs(cookbook): Qwen3.5 FP8 on B200/B300 — trtllm-gen MoE + symm mem」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +13/-2 (15 lines); hunks: -410,8 +410,9 @@ export const Qwen35Deployment = () => {; -455,6 +456,16 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-1 (4 lines); hunks: -126,7 +126,7 @@ This section provides deployment configurations optimized fo...; -139,6 +139,8 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +13/-2 (15 lines); hunks: -410,8 +410,9 @@ export const Qwen35Deployment = () => {; -455,6 +456,16 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-1 (4 lines); hunks: -126,7 +126,7 @@ This section provides deployment configurations optimized fo...; -139,6 +139,8 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -410,8 +410,9 @@ export const Qwen35Deployment = () => {
-    // Enable NCCL symmetric memory for H100 FP8 deployments.
-    if (hardware === 'h100' && quantization === 'fp8' && hwConfig.tp > 1) {
+    // Enable NCCL symmetric memory for H100 and Blackwell FP8 deployments.
+    const symmMemFp8Hw = ['h100', 'b200', 'b300'];
+    if (symmMemFp8Hw.includes(hardware) && quantization === 'fp8' && hwConfig.tp > 1) {
@@ -455,6 +456,16 @@ export const Qwen35Deployment = () => {
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -126,7 +126,7 @@ This section provides deployment configurations optimized for different hardware
-- **H100 FP8:** Add `--enable-symm-mem` to enable NCCL symmetric memory for faster collectives and better performance under multi-GPU settings.
+- **H100 / B200 / B300 FP8:** Add `--enable-symm-mem` to enable NCCL symmetric memory for faster collectives and better performance under multi-GPU settings. It only helps when tp
@@ -139,6 +139,8 @@ This section provides deployment configurations optimized for different hardware
+- **B200 / B300 (FP8 MoE)**: Add `--moe-runner-backend flashinfer_trtllm` to route the fused MoE through the trtllm-gen kernels on Blackwell. This is not picked up automatically —
+- **B200 / B300 (FP8)**: Add `--linear-attn-prefill-backend flashinfer` to run GDN (linear attention) prefill on the FlashInfer CuTe-DSL kernel. SGLang auto-selects it only inside
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +13/-2; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #33922 - Fix Qwen3.5 GDN multi-item scoring

- 链接: https://github.com/sgl-project/sglang/pull/33922
- 状态/时间: merged / 2026-09-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py`；关联提交 `03e4c06589e3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+845/-30，可读 patch 1180 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Qwen3.5 GDN multi-item scoring」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py`；技术摘要: 覆盖「Fix Qwen3.5 GDN multi-item scoring」；主要实现面是 `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py` added +133/-0 (133 lines); hunks: -0,0 +1,133; symbols: TestQwen35GDNMultiItemScoring, setUpClass, tearDownClass, _score，涉及 `TestQwen35GDNMultiItemScoring, setUpClass, tearDownClass`。
- 代码 diff 细节:
  - `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py` added +133/-0 (133 lines); hunks: -0,0 +1,133; symbols: TestQwen35GDNMultiItemScoring, setUpClass, tearDownClass, _score
- 关键代码摘录:

```diff
diff -- test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py
@@ -0,0 +1,133 @@
+"""End-to-end MIS coverage for the hybrid Qwen3.5 GDN architecture."""
+import asyncio
+import os
+import unittest
+import torch
+from transformers import AutoTokenizer
```

- 已读文件:
  - tests: `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py` added +133/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/kits/attention_unittest/attention_methods/gdn_attention.py`, `test/registered/attention/test_chunk_gated_delta_rule.py`, `test/registered/attention/unittests/gdn/test_triton.py`, `test/registered/e2e/gdn/test_qwen35_gdn_multi_item_scoring.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39104 - [AMD] Update MI355X MXFP4 HiCache defaults and quick-reduce quantization for Qwen3.5 cookbook

- 链接: https://github.com/sgl-project/sglang/pull/39104
- 状态/时间: merged / 2026-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `7bc4eb374033`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+9/-9，可读 patch 60 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Update MI355X MXFP4 HiCache defaults and quick-reduce quantization for Qwen3.5 cookbook」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[AMD] Update MI355X MXFP4 HiCache defaults and quick-reduce quantization for Qwen3.5 cookbook」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +6/-6 (12 lines); hunks: -470,16 +470,16 @@ export const Qwen35Deployment = () => {; -506,7 +506,7 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3 (6 lines); hunks: -106,7 +106,7 @@ docker pull lmsysorg/sglang:latest; -127,8 +127,8 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +6/-6 (12 lines); hunks: -470,16 +470,16 @@ export const Qwen35Deployment = () => {; -506,7 +506,7 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3 (6 lines); hunks: -106,7 +106,7 @@ docker pull lmsysorg/sglang:latest; -127,8 +127,8 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -470,16 +470,16 @@ export const Qwen35Deployment = () => {
-    // except the MXFP4 MI355X recipe, which uses ROCm INT8 quantized quick
-    // all-reduce (ROCM_QUICK_REDUCE_QUANTIZATION=INT8) instead.
+    // except the MXFP4 MI355X recipe, which uses ROCm INT4 quantized quick
+    // all-reduce (ROCM_QUICK_REDUCE_QUANTIZATION=INT4) instead.
-        amdEnv += "ROCM_QUICK_REDUCE_QUANTIZATION=INT8 \\\n";
+        amdEnv += "ROCM_QUICK_REDUCE_QUANTIZATION=INT4 \\\n";
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -106,7 +106,7 @@ docker pull lmsysorg/sglang:latest
-docker pull lmsysorg/sglang-rocm:v0.5.15.post1-rocm720-mi35x-20260715
+docker pull lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260911
@@ -127,8 +127,8 @@ This section provides deployment configurations optimized for different hardware
-- **AMD GPUs (MI300X / MI325X / MI355X):** Use `SGLANG_USE_AITER=1` and `SGLANG_USE_AITER_UNIFIED_ATTN=1` with `--attention-backend aiter`, which requires `--page-size 16` and can
-- **KV cache offloading (MXFP4 on MI355X):** Selecting **Host DRAM (HiCache)** adds a host-memory tier below the device KV cache, which lets long-context agentic workloads keep mo
+- **AMD GPUs (MI300X / MI325X / MI355X):** Use `SGLANG_USE_AITER=1` and `SGLANG_USE_AITER_UNIFIED_ATTN=1` with `--attention-backend aiter`, which requires `--page-size 16` and can
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +6/-6; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39358 - [AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct

- 链接: https://github.com/sgl-project/sglang/pull/39358
- 状态/时间: merged / 2026-09-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `2f5cc8e33e97`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+7/-7，可读 patch 50 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +4/-4 (8 lines); hunks: -334,9 +334,9 @@ export const Qwen35Deployment = () => {; -517,8 +517,8 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3 (6 lines); hunks: -42,7 +42,7 @@ Qwen3.5 features a Gated Delta Networks combined with sparse M...; -128,7 +128,7 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +4/-4 (8 lines); hunks: -334,9 +334,9 @@ export const Qwen35Deployment = () => {; -517,8 +517,8 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3 (6 lines); hunks: -42,7 +42,7 @@ Qwen3.5 features a Gated Delta Networks combined with sparse M...; -128,7 +128,7 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -334,9 +334,9 @@ export const Qwen35Deployment = () => {
-      // AMD MI355X uses the MXFP4 checkpoint; Blackwell uses NVFP4-V2.
+      // AMD MI355X uses MXFP4-AttnFP8-V2 (MXFP4 MoE, FP8 attention); Blackwell uses NVFP4-V2.
-        ? 'amd/Qwen3.5-397B-A17B-MXFP4'
+        ? 'amd/Qwen3.5-397B-A17B-MXFP4-AttnFP8-V2'
@@ -517,8 +517,8 @@ export const Qwen35Deployment = () => {
-          cmd += ' \\\n  --hicache-io-backend kernel';
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -42,7 +42,7 @@ Qwen3.5 features a Gated Delta Networks combined with sparse Mixture-of-Experts
-      <td style={{padding: "9px 12px", backgroundColor: "rgba(255,255,255,0.05)"}}>NVIDIA NVFP4: [nvidia/Qwen3.5-397B-A17B-NVFP4-V2](https://huggingface.co/nvidia/Qwen3.5-397B-A17
+      <td style={{padding: "9px 12px", backgroundColor: "rgba(255,255,255,0.05)"}}>NVIDIA NVFP4: [nvidia/Qwen3.5-397B-A17B-NVFP4-V2](https://huggingface.co/nvidia/Qwen3.5-397B-A17
@@ -128,7 +128,7 @@ This section provides deployment configurations optimized for different hardware
-- **KV cache offloading (MXFP4 on MI355X):** Selecting **Host DRAM (HiCache)** adds a host-memory tier below the device KV cache, which lets long-context agentic workloads keep mo
+- **KV cache offloading (MXFP4 on MI355X):** Selecting **Host DRAM (HiCache)** adds a host-memory tier below the device KV cache, which lets long-context agentic workloads keep mo
@@ -159,7 +159,7 @@ This section provides deployment configurations optimized for different hardware
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +4/-4; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39047 - [NPU] Remove temperature/top_p from Qwen3.5-397B-A17B perf test

- 链接: https://github.com/sgl-project/sglang/pull/39047
- 状态/时间: merged / 2026-09-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py`；关联提交 `d5f1c593c160`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-2，可读 patch 12 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Remove temperature/top_p from Qwen3.5-397B-A17B perf test」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py`；技术摘要: 覆盖「[NPU] Remove temperature/top_p from Qwen3.5-397B-A17B perf test」；主要实现面是 `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` modified +3/-2 (5 lines); hunks: -125,8 +125,9 @@ class TestNPUQwen3_5_397B_A17B_3K5_1K5_50ms(TestNpuPerforman...; symbols: TestNPUQwen3_5_397B_A17B_3K5_1K5_50ms, test_npu_qwen3_5_397b_a17b_3k5_1k5，涉及 `TestNPUQwen3_5_397B_A17B_3K5_1K5_50ms, test_npu_qwen3_5_397b_a17b_3k5_1k5`。
- 代码 diff 细节:
  - `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` modified +3/-2 (5 lines); hunks: -125,8 +125,9 @@ class TestNPUQwen3_5_397B_A17B_3K5_1K5_50ms(TestNpuPerforman...; symbols: TestNPUQwen3_5_397B_A17B_3K5_1K5_50ms, test_npu_qwen3_5_397b_a17b_3k5_1k5
- 关键代码摘录:

```diff
diff -- test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
@@ -125,8 +125,9 @@ class TestNPUQwen3_5_397B_A17B_3K5_1K5_50ms(TestNpuPerformanceTestCaseBase):
-    temperature = 0.6
-    top_p = 0.95
+    # Disabled to work around DTS2026091033366; re-enable after the fix.
+    # temperature = 0.6
+    # top_p = 0.95
```

- 已读文件:
  - tests: `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` modified +3/-2
- 验证与风险: diff 自带测试面 `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39572 - [AMD] Align Qwen3.5 MI355X HiCache cookbook with kernel / page_first

- 链接: https://github.com/sgl-project/sglang/pull/39572
- 状态/时间: merged / 2026-09-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `a9bb4d7d4561`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+3/-3，可读 patch 20 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Align Qwen3.5 MI355X HiCache cookbook with kernel / page_first」；模型线: Qwen3.5；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[AMD] Align Qwen3.5 MI355X HiCache cookbook with kernel / page_first」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +2/-2 (4 lines); hunks: -517,8 +517,8 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +1/-1 (2 lines); hunks: -128,7 +128,7 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +2/-2 (4 lines); hunks: -517,8 +517,8 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +1/-1 (2 lines); hunks: -128,7 +128,7 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -517,8 +517,8 @@ export const Qwen35Deployment = () => {
-          cmd += ' \\\n  --hicache-io-backend direct';
-          cmd += ' \\\n  --hicache-mem-layout page_first_direct';
+          cmd += ' \\\n  --hicache-io-backend kernel';
+          cmd += ' \\\n  --hicache-mem-layout page_first';
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -128,7 +128,7 @@ This section provides deployment configurations optimized for different hardware
-- **KV cache offloading (MXFP4 on MI355X):** Selecting **Host DRAM (HiCache)** adds a host-memory tier below the device KV cache, which lets long-context agentic workloads keep mo
+- **KV cache offloading (MXFP4 on MI355X):** Selecting **Host DRAM (HiCache)** adds a host-memory tier below the device KV cache, which lets long-context agentic workloads keep mo
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +2/-2; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #38878 - [AMD] Load fused shared experts for Qwen4-Exp and Qwen3.5 MTP

- 链接: https://github.com/sgl-project/sglang/pull/38878
- 状态/时间: merged / 2026-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`；关联提交 `11c35b8433e8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+37/-10，可读 patch 96 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Load fused shared experts for Qwen4-Exp and Qwen3.5 MTP」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[AMD] Load fused shared experts for Qwen4-Exp and Qwen3.5 MTP」；主要实现面是 `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_mtp.py` modified +13/-8 (21 lines); hunks: -291,8 +291,9 @@ def load_weights(; -368,13 +369,17 @@ def load_fused_expert_weights(; symbols: load_weights, load_fused_expert_weights，涉及 `load_weights, load_fused_expert_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +13/-8 (21 lines); hunks: -291,8 +291,9 @@ def load_weights(; -368,13 +369,17 @@ def load_fused_expert_weights(; symbols: load_weights, load_fused_expert_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -291,8 +291,9 @@ def load_weights(
-        # fused experts: experts.w13_weight / experts.w2_weight
-        is_fused_expert = False
+        # Fused checkpoint tensors: experts.gate_up_proj / experts.down_proj.
+        # The checkpoint interleaves these with separate shared-expert tensors,
+        # so picking one mapping must not affect the next weight.
@@ -368,13 +369,17 @@ def load_fused_expert_weights(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +13/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen4_exp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #39986 - [AMD] Use Triton softmax routing for Qwen3.5 on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/39986
- 状态/时间: merged / 2026-09-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/test_qwen35_moe_softmax_topk.py`；关联提交 `90b3f8544ca2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+163/-2，可读 patch 201 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Use Triton softmax routing for Qwen3.5 on gfx950」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `test/registered/amd/test_qwen35_moe_softmax_topk.py`；技术摘要: 覆盖「[AMD] Use Triton softmax routing for Qwen3.5 on gfx950」；主要实现面是 `test/registered/amd/test_qwen35_moe_softmax_topk.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/test_qwen35_moe_softmax_topk.py` added +127/-0 (127 lines); hunks: -0,0 +1,127; symbols: TestQwen35MoeSoftmaxTopK, test_triton_dispatch_matches_aiter, test_dispatch_envelope_is_narrow，涉及 `TestQwen35MoeSoftmaxTopK, test_triton_dispatch_matches_aiter, test_dispatch_envelope_is_narrow`。
- 代码 diff 细节:
  - `test/registered/amd/test_qwen35_moe_softmax_topk.py` added +127/-0 (127 lines); hunks: -0,0 +1,127; symbols: TestQwen35MoeSoftmaxTopK, test_triton_dispatch_matches_aiter, test_dispatch_envelope_is_narrow
- 关键代码摘录:

```diff
diff -- test/registered/amd/test_qwen35_moe_softmax_topk.py
@@ -0,0 +1,127 @@
+"""ROCm coverage for the decode-sized Qwen3.5 MoE softmax router."""
+import unittest
+from unittest.mock import patch
+import torch
+from sglang.srt.layers.moe import topk as topk_module
+from sglang.srt.utils import is_gfx95_supported
```

- 已读文件:
  - tests: `test/registered/amd/test_qwen35_moe_softmax_topk.py` added +127/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/test_qwen35_moe_softmax_topk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39902 - [AMD] Pack Qwen3.5 GDN input projections on ROCm

- 链接: https://github.com/sgl-project/sglang/pull/39902
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py`, `test/registered/amd/test_qwen35_gdn_packed_in_proj.py`；关联提交 `6412ad8c6481`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+573/-5，可读 patch 639 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Pack Qwen3.5 GDN input projections on ROCm」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_packed_in_proj.py`, `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py`；技术摘要: 覆盖「[AMD] Pack Qwen3.5 GDN input projections on ROCm」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_packed_in_proj.py`, `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +151/-5 (156 lines); hunks: -133,8 +133,12; -394,6 +398,10 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, finalize_fused_in_proj, _finalize_fused_fp8_in_proj，涉及 `__init__, fix_query_key_value_ordering, finalize_fused_in_proj`；`test/registered/amd/test_qwen35_gdn_packed_in_proj.py` added +214/-0 (214 lines); hunks: -0,0 +1,214; symbols: _Linear, __init__, forward, _GDN，涉及 `_Linear, __init__, forward`；`test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: _FP8Linear, __init__, forward, TestQwen35GDNPackedFP8InProj，涉及 `_FP8Linear, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +151/-5 (156 lines); hunks: -133,8 +133,12; -394,6 +398,10 @@ def __init__(; symbols: __init__, fix_query_key_value_ordering, finalize_fused_in_proj, _finalize_fused_fp8_in_proj
  - `test/registered/amd/test_qwen35_gdn_packed_in_proj.py` added +214/-0 (214 lines); hunks: -0,0 +1,214; symbols: _Linear, __init__, forward, _GDN
  - `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: _FP8Linear, __init__, forward, TestQwen35GDNPackedFP8InProj
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -133,8 +133,12 @@
+# qwen4_exp shares these classes, but the ROCm packed path is Qwen3.5-only.
+_QWEN3_5_ROCM_PACKED_MODEL_TYPES = ("qwen3_5_text", "qwen3_5_moe_text")
+if _use_aiter:
+    from aiter.tuned_gemm import tgemm
@@ -394,6 +398,10 @@ def __init__(
+        self._fused_in_proj_ba_width = 0
diff -- test/registered/amd/test_qwen35_gdn_packed_in_proj.py
@@ -0,0 +1,214 @@
+"""Packed BF16 GDN input projection for Qwen3.5 decode on ROCm.
+``finalize_fused_in_proj`` stacks ``in_proj_qkvz`` and ``in_proj_ba`` into one
+weight and re-points the module weights at row views of it; on ROCm
+``_forward_input_proj`` then runs one aiter GEMM for verify-sized batches and
+splits the result. Guards: the views alias the packed buffer and keep their
+values, and the packed and separate paths agree on both sides of the token gate.
diff -- test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py
@@ -0,0 +1,142 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +151/-5
  - tests: `test/registered/amd/test_qwen35_gdn_packed_in_proj.py` added +214/-0; `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py` added +142/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py`, `test/registered/amd/test_qwen35_gdn_packed_in_proj.py`, `test/registered/unit/model_executor/test_derived_weight_cache.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40770 - Add GB200/GB300 hardware to Qwen3.5

- 链接: https://github.com/sgl-project/sglang/pull/40770
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `d72629e4bade`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+49/-8，可读 patch 167 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add GB200/GB300 hardware to Qwen3.5」；模型线: Qwen3.5；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；技术摘要: 覆盖「Add GB200/GB300 hardware to Qwen3.5」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +49/-8 (57 lines); hunks: -8,16 +8,16 @@ export const Qwen35Deployment = () => {; -62,6 +62,8 @@ export const Qwen35Deployment = () => {。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +49/-8 (57 lines); hunks: -8,16 +8,16 @@ export const Qwen35Deployment = () => {; -62,6 +62,8 @@ export const Qwen35Deployment = () => {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -8,16 +8,16 @@ export const Qwen35Deployment = () => {
-  //   397B-A17B: H100 tp=16 (2 nodes), H200 tp=8, B200 tp=8, B300 tp=8, MI300X tp=8, MI325X tp=4, MI355X tp=4
-  //   122B-A10B: H100 tp=4,  H200 tp=4, B200 tp=2, B300 tp=2, MI300X tp=2, MI325X tp=1, MI355X tp=1
-  //   35B-A3B:   H100 tp=1 (tp=2 w/ MTP), H200 tp=1, B200 tp=1, B300 tp=1, MI300X tp=1, MI325X tp=1, MI355X tp=1
+  //   397B-A17B: H100 tp=16 (2 nodes), H200 tp=8, B200 tp=8, B300 tp=8, GB200 tp=8 (2 nodes, 4 GPUs/node), GB300 tp=8 (2 nodes, 4 GPUs/node), MI300X tp=8, MI325X tp=4, MI355X tp=
+  //   122B-A10B: H100 tp=4,  H200 tp=4, B200 tp=2, B300 tp=2, GB200 tp=2, GB300 tp=2, MI300X tp=2, MI325X tp=1, MI355X tp=1
+  //   35B-A3B:   H100 tp=1 (tp=2 w/ MTP), H200 tp=1, B200 tp=1, B300 tp=1, GB200 tp=1, GB300 tp=1, MI300X tp=1, MI325X tp=1, MI355X tp=1
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +49/-8
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #35958 - [npu] decoding procedure optimization on qwen3.5/3.6

- 链接: https://github.com/sgl-project/sglang/pull/35958
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `d4dcce12d4fc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+27/-13，可读 patch 106 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[npu] decoding procedure optimization on qwen3.5/3.6」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[npu] decoding procedure optimization on qwen3.5/3.6」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +11/-2 (13 lines); hunks: -245,6 +245,15 @@ def fused_sigmoid_mul(x, gate, inplace=True):; -984,7 +993,7 @@ def forward(; symbols: fused_sigmoid_mul, _enable_qwen35_fused_ar_quant, forward, self_attention，涉及 `fused_sigmoid_mul, _enable_qwen35_fused_ar_quant, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +11/-2 (13 lines); hunks: -245,6 +245,15 @@ def fused_sigmoid_mul(x, gate, inplace=True):; -984,7 +993,7 @@ def forward(; symbols: fused_sigmoid_mul, _enable_qwen35_fused_ar_quant, forward, self_attention
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -245,6 +245,15 @@ def fused_sigmoid_mul(x, gate, inplace=True):
+if _is_npu:
+    from sgl_kernel_npu.activation.fused_sigmoid_mul import (
+        fused_sigmoid_mul as npu_fused_sigmoid_mul,
+    )
+    # NPU uses the Ascend-tuned implementation; other backends keep the
+    # original Triton kernel.
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +11/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41198 - [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit

- 链接: https://github.com/sgl-project/sglang/pull/41198
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `b7f6d04a9af1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+50/-219，可读 patch 402 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit」；模型线: Qwen3.5；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +6/-93 (99 lines); hunks: -46,7 +46,6; -108,7 +107,6; symbols: _select_fused_ar_input_for_linear, _finish_mlp_output, forward, Qwen3_5AttentionDecoderLayer，涉及 `_select_fused_ar_input_for_linear, _finish_mlp_output, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +6/-93 (99 lines); hunks: -46,7 +46,6; -108,7 +107,6; symbols: _select_fused_ar_input_for_linear, _finish_mlp_output, forward, Qwen3_5AttentionDecoderLayer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -46,7 +46,6 @@
-    UnreducedOutput,
@@ -108,7 +107,6 @@
-    get_forward,
@@ -307,19 +305,6 @@ def _select_fused_ar_input_for_linear(hidden_states, linear: nn.Module):
-def _finish_mlp_output(hidden_states, *, expect_deferred: bool):
-    from sglang.srt.layers.moe.cutedsl_ar_fusion import MoeFinalizeHandoff
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +6/-93
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39064 - [ROCm][Bugfix] Keep quantization for mixed Quark Qwen3.5 MTP checkpoints

- 链接: https://github.com/sgl-project/sglang/pull/39064
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_mtp.py`, `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py`；关联提交 `0154f72b48d5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+130/-9，可读 patch 153 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Bugfix] Keep quantization for mixed Quark Qwen3.5 MTP checkpoints」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py`, `python/sglang/srt/models/qwen3_5_mtp.py`；技术摘要: 覆盖「[ROCm][Bugfix] Keep quantization for mixed Quark Qwen3.5 MTP checkpoints」；主要实现面是 `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py`, `python/sglang/srt/models/qwen3_5_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py` added +107/-0 (107 lines); hunks: -0,0 +1,107; symbols: _FakeQuantConfig, __init__, get_name, TestQwen3_5MTPQuantConfig，涉及 `_FakeQuantConfig, __init__, get_name`；`python/sglang/srt/models/qwen3_5_mtp.py` modified +23/-9 (32 lines); hunks: -69,21 +69,35 @@ def _mtp_quant_config(quant_config):; symbols: _mtp_quant_config, Qwen3_5ForCausalLMMTP, and, shared_experts_fusion_disable_reason，涉及 `_mtp_quant_config, Qwen3_5ForCausalLMMTP, and`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py` added +107/-0 (107 lines); hunks: -0,0 +1,107; symbols: _FakeQuantConfig, __init__, get_name, TestQwen3_5MTPQuantConfig
  - `python/sglang/srt/models/qwen3_5_mtp.py` modified +23/-9 (32 lines); hunks: -69,21 +69,35 @@ def _mtp_quant_config(quant_config):; symbols: _mtp_quant_config, Qwen3_5ForCausalLMMTP, and, shared_experts_fusion_disable_reason
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_qwen3_5_mtp_quant_config.py
@@ -0,0 +1,107 @@
+import unittest
+from sglang.srt.layers.quantization.quark.utils import should_ignore_layer
+from sglang.srt.models.qwen3_5 import Qwen3_5ForCausalLM
+from sglang.srt.models.qwen3_5_mtp import Qwen3_5ForCausalLMMTP, _mtp_quant_config
+from sglang.test.ci.ci_register import register_cpu_ci
+from sglang.test.test_utils import CustomTestCase
diff -- python/sglang/srt/models/qwen3_5_mtp.py
@@ -69,21 +69,35 @@ def _mtp_quant_config(quant_config):
-    # Quark-quantized Qwen3.5 MXFP4 checkpoints ship the MTP module in bf16;
-    # every `mtp.*` layer appears under the quantization exclude list. Detect
-    # that and skip quantization here so linear/MoE weight loaders allocate
-    # bf16 shapes (see sgl-project/sglang#23113).
+    # Some Quark-quantized Qwen3.5 MXFP4 checkpoints ship the MTP module
+    # entirely in bf16, listing every `mtp.*` layer under the quantization
```

- 已读文件:
  - tests: `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py` added +107/-0
  - runtime: `python/sglang/srt/models/qwen3_5_mtp.py` modified +23/-9
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41849 - [Docs] Add MI355X FP8 agentic recipe to the Qwen3.5 cookbook

- 链接: https://github.com/sgl-project/sglang/pull/41849
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `47dcde70f40e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+30/-7，可读 patch 92 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Add MI355X FP8 agentic recipe to the Qwen3.5 cookbook」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[Docs] Add MI355X FP8 agentic recipe to the Qwen3.5 cookbook」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +26/-4 (30 lines); hunks: -15,7 +15,7 @@ export const Qwen35Deployment = () => {; -117,9 +117,12 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +4/-3 (7 lines); hunks: -106,7 +106,7 @@ docker pull lmsysorg/sglang:latest; -127,6 +127,7 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +26/-4 (30 lines); hunks: -15,7 +15,7 @@ export const Qwen35Deployment = () => {; -117,9 +117,12 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +4/-3 (7 lines); hunks: -106,7 +106,7 @@ docker pull lmsysorg/sglang:latest; -127,6 +127,7 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -15,7 +15,7 @@ export const Qwen35Deployment = () => {
-  //   397B-A17B: H100 tp=8, H200 tp=8 ep=8, B200 tp=4, B300 tp=4, GB200 tp=4, GB300 tp=4, MI300X tp=4, MI325X tp=2, MI355X tp=2
+  //   397B-A17B: H100 tp=8, H200 tp=8 ep=8, B200 tp=4, B300 tp=4, GB200 tp=4, GB300 tp=4, MI300X tp=4, MI325X tp=2, MI355X tp=2 (tp=4 with HiCache, the long-context agentic recip
@@ -117,9 +117,12 @@ export const Qwen35Deployment = () => {
-      // HiCache adds a host-DRAM tier below the device KV cache. Only wired up
-      // for the MI355X MXFP4 recipe, which is the arm it is tuned on.
-      condition: (values) => values.hardware === 'mi355x' && values.quantization === 'fp4',
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -106,7 +106,7 @@ docker pull lmsysorg/sglang:latest
-docker pull lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260911
+docker pull lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260927
@@ -127,6 +127,7 @@ This section provides deployment configurations optimized for different hardware
+- **KV cache offloading (397B FP8 on MI355X):** A separate recipe from the MXFP4 one above, for long-context agentic serving of the FP8 checkpoint. Selecting **Host DRAM (HiCache)
@@ -219,14 +220,14 @@ This section provides deployment configurations optimized for different hardware
-      <td style={{padding: "9px 12px", backgroundColor: "rgba(255,255,255,0.05)"}}>2</td>
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +26/-4; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +4/-3
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #41154 - fix(spec): enable Qwen3.5 EAGLE3 capture and streaming overlap

- 链接: https://github.com/sgl-project/sglang/pull/41154
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `f050ab194ab5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+90/-19，可读 patch 233 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(spec): enable Qwen3.5 EAGLE3 capture and streaming overlap」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「fix(spec): enable Qwen3.5 EAGLE3 capture and streaming overlap」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +5/-0 (5 lines); hunks: -1770,6 +1770,11 @@ def set_dflash_layers_to_capture(self, layers_to_capture:...; symbols: set_dflash_layers_to_capture, set_eagle3_layers_to_capture, start_layer，涉及 `set_dflash_layers_to_capture, set_eagle3_layers_to_capture, start_layer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +5/-0 (5 lines); hunks: -1770,6 +1770,11 @@ def set_dflash_layers_to_capture(self, layers_to_capture:...; symbols: set_dflash_layers_to_capture, set_eagle3_layers_to_capture, start_layer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -1770,6 +1770,11 @@ def set_dflash_layers_to_capture(self, layers_to_capture: list[int]):
+    def set_eagle3_layers_to_capture(self, layers_to_capture: list[int]):
+        self.layers_to_capture = layers_to_capture
+        for layer_id in self.layers_to_capture:
+            setattr(self.layers[layer_id], "_is_layer_to_capture", True)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +5/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42002 - [Spec] Fix Qwen3.5 text model EAGLE3/DFLASH aux-layer capture

- 链接: https://github.com/sgl-project/sglang/pull/42002
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5_text.py`；关联提交 `0098b9d29d5b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-10，可读 patch 35 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec] Fix Qwen3.5 text model EAGLE3/DFLASH aux-layer capture」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5_text.py`；技术摘要: 覆盖「[Spec] Fix Qwen3.5 text model EAGLE3/DFLASH aux-layer capture」；主要实现面是 `python/sglang/srt/models/qwen3_5_text.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5_text.py` modified +11/-10 (21 lines); hunks: -127,6 +127,17 @@ def set_dflash_layers_to_capture(self, layer_ids: list[int]...; -146,16 +157,6 @@ def set_embed_and_head(self, embed, head):; symbols: set_dflash_layers_to_capture, set_eagle3_layers_to_capture, get_embed_and_head, set_embed_and_head，涉及 `set_dflash_layers_to_capture, set_eagle3_layers_to_capture, get_embed_and_head`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5_text.py` modified +11/-10 (21 lines); hunks: -127,6 +127,17 @@ def set_dflash_layers_to_capture(self, layer_ids: list[int]...; -146,16 +157,6 @@ def set_embed_and_head(self, embed, head):; symbols: set_dflash_layers_to_capture, set_eagle3_layers_to_capture, get_embed_and_head, set_embed_and_head
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5_text.py
@@ -127,6 +127,17 @@ def set_dflash_layers_to_capture(self, layer_ids: list[int]) -> None:
+    def set_eagle3_layers_to_capture(self, layer_ids: Optional[list[int]] = None):
+        if not self.pp_group.is_last_rank:
+            return
+        self.capture_aux_hidden_states = True
+        if layer_ids is None:
+            num_layers = len(self.model.layers)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5_text.py` modified +11/-10
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5_text.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41134 - [AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/41134
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `33883a5fa3c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+607/-12，可读 patch 793 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +40/-1 (41 lines); hunks: -26,6 +26,7; -120,6 +121,7; symbols: _linear_accepts_fp8_tuple, _fp8_tuple_input, _select_fused_ar_input_for_linear, forward，涉及 `_linear_accepts_fp8_tuple, _fp8_tuple_input, _select_fused_ar_input_for_linear`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +40/-1 (41 lines); hunks: -26,6 +26,7; -120,6 +121,7; symbols: _linear_accepts_fp8_tuple, _fp8_tuple_input, _select_fused_ar_input_for_linear, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -26,6 +26,7 @@
+from sglang.kernels.ops.attention.fla.layernorm_gated import _layer_norm_fwd
@@ -120,6 +121,7 @@
+    get_forward,
@@ -157,6 +159,11 @@
+    from sglang.kernels.ops.gemm.smallm_fp8_gfx950 import (
+        smallm_fp8_gemm_config,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +40/-1
- 验证与风险: diff 自带测试面 `test/registered/amd/test_smallm_fp8_proj_gfx950.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43083 - [Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1

- 链接: https://github.com/sgl-project/sglang/pull/43083
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`；关联提交 `1fc6b8962c02`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+14703/-1042，可读 patch 5223 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1」；主要实现面是 `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` added +12051/-0 (12051 lines)；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +15/-38 (53 lines); hunks: -232,6 +232,21 @@ This section provides deployment configurations optimized f...; -1023,44 +1038,6 @@ Max ITL (ms): 1220.68。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` added +12051/-0 (12051 lines)
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +15/-38 (53 lines); hunks: -232,6 +232,21 @@ This section provides deployment configurations optimized f...; -1023,44 +1038,6 @@ Max ITL (ms): 1220.68
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -232,6 +232,21 @@ This section provides deployment configurations optimized for different hardware
+<a id="agentic-long-context-deployment" />
+### 3.3 Agentic Long-Context Deployment
+Agentic workloads, such as coding agents and other multi-turn, tool-using assistants, send long prompts whose prefixes grow and repeat from turn to turn. Serving them well depends
+- **Router.** Each configuration was submitted behind one front door: Dynamo (`dynamo.frontend` with `dynamo.sglang` workers) or SGLang (`sglang.launch_server`, behind `sglang_rou
+- **KV offload.** Choose among these KV cache offloading mechanisms: none (GPU KV only), HiCache (host DRAM), or a Mooncake store attached through the external linker. The Mooncak
+- **Container image.** Run the commands inside the image listed for each configuration. Several are SGLang nightly images, so flag names follow that image.
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` added +12051/-0; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +15/-38
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/_agentx.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #43037 - [Spec] Allow Qwen3.5 backends to opt into packed target verification

- 链接: https://github.com/sgl-project/sglang/pull/43037
- 状态/时间: merged / 2026-10-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `5678b71b6cca`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-6，可读 patch 41 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Spec] Allow Qwen3.5 backends to opt into packed target verification」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Spec] Allow Qwen3.5 backends to opt into packed target verification」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +12/-6 (18 lines); hunks: -976,16 +976,23 @@ def forward(; -1033,11 +1040,10 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +12/-6 (18 lines); hunks: -976,16 +976,23 @@ def forward(; -1033,11 +1040,10 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -976,16 +976,23 @@ def forward(
-        use_fused_decode_proj_conv = (
+        packed_verify = False
+        if forward_batch.forward_mode.is_target_verify():
+            from sglang.srt.model_executor.forward_context import get_attn_backend
+            backend = get_attn_backend()
+            backend = getattr(backend, "linear_attn_backend", backend)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +12/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #29753 - [NPU] [Bugfix] Fix rope sin cos pre-calculation for Qwen3.5 during Pipeline Parallelism

- 链接: https://github.com/sgl-project/sglang/pull/29753
- 状态/时间: merged / 2026-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`；关联提交 `fa66e7d816d7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+99/-3，可读 patch 154 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] [Bugfix] Fix rope sin cos pre-calculation for Qwen3.5 during Pipeline Parallelism」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`, `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[NPU] [Bugfix] Fix rope sin cos pre-calculation for Qwen3.5 during Pipeline Parallelism」；主要实现面是 `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`, `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py` modified +64/-1 (65 lines); hunks: -1,10 +1,17; -99,6 +106,62 @@ def test_mtp_loads_text_target_embedding_for_last_pp_stage(s...; symbols: test_mtp_loads_text_target_embedding_for_last_pp_stage, test_rope_refresh_at_first_attention_layer_of_each_pp_stage, test_rope_refresh_for_draft_ignores_target_pp_split，涉及 `test_mtp_loads_text_target_embedding_for_last_pp_stage, test_rope_refresh_at_first_attention_layer_of_each_pp_stage, test_rope_refresh_for_draft_ignores_target_pp_split`；`python/sglang/srt/models/qwen3_5.py` modified +30/-2 (32 lines); hunks: -45,6 +45,7; -1227,6 +1228,31 @@ def forward(; symbols: forward, _refreshes_rope_cos_sin, Qwen3_5AttentionDecoderLayer, __init__，涉及 `forward, _refreshes_rope_cos_sin, Qwen3_5AttentionDecoderLayer`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py` modified +64/-1 (65 lines); hunks: -1,10 +1,17; -99,6 +106,62 @@ def test_mtp_loads_text_target_embedding_for_last_pp_stage(s...; symbols: test_mtp_loads_text_target_embedding_for_last_pp_stage, test_rope_refresh_at_first_attention_layer_of_each_pp_stage, test_rope_refresh_for_draft_ignores_target_pp_split
  - `python/sglang/srt/models/qwen3_5.py` modified +30/-2 (32 lines); hunks: -45,6 +45,7; -1227,6 +1228,31 @@ def forward(; symbols: forward, _refreshes_rope_cos_sin, Qwen3_5AttentionDecoderLayer, __init__
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_qwen3_5_pipeline_parallel.py
@@ -1,10 +1,17 @@
+import os
+from unittest.mock import patch
+from sglang.srt.configs.qwen3_5 import Qwen3_5TextConfig
+from sglang.srt.distributed import get_pp_indices
-from sglang.srt.models.qwen3_5 import Qwen3_5MoeForConditionalGeneration
+from sglang.srt.models.qwen3_5 import (
diff -- python/sglang/srt/models/qwen3_5.py
@@ -45,6 +45,7 @@
+from sglang.srt.distributed import get_pp_indices
@@ -1227,6 +1228,31 @@ def forward(
+def _refreshes_rope_cos_sin(
+    config: Qwen3_5TextConfig, layer_id: int, is_nextn: bool
+) -> bool:
+    """rotary_emb is shared by all layers, so its per-forward cos/sin is refreshed
```

- 已读文件:
  - tests: `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py` modified +64/-1
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +30/-2
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44712 - [Doc] cookbook: Refresh SemiAnalysis AgentX launches for Qwen3.5 and DeepSeek-V4.1-Flash GB300

- 链接: https://github.com/sgl-project/sglang/pull/44712
- 状态/时间: merged / 2026-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`；关联提交 `5e240a200dd0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+827/-1423，可读 patch 3401 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: Refresh SemiAnalysis AgentX launches for Qwen3.5 and DeepSeek-V4.1-Flash GB300」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`；技术摘要: 覆盖「[Doc] cookbook: Refresh SemiAnalysis AgentX launches for Qwen3.5 and DeepSeek-V4.1-Flash GB300」；主要实现面是 `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` modified +564/-1131 (1695 lines); hunks: -1,37 +1,22; -177,13 +162,13 @@ export const agentx = {。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` modified +564/-1131 (1695 lines); hunks: -1,37 +1,22; -177,13 +162,13 @@ export const agentx = {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/agentx/Qwen/qwen3.5.jsx
@@ -1,37 +1,22 @@
-// (SemiAnalysisAI/InferenceX main@c08eb51d3bd5 plus open PRs #4094, #4111, #4112, #4141, #4146), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@12dbddac599f plus open PRs #4033, #4162), with SA-specific settings removed.
- "generatedOn": "2026-10-15",
+ "generatedOn": "2026-10-16",
-  "main": "c08eb51d3bd536ae3aac8d9b1843b363411611ff",
+  "main": "12dbddac599f461400aa6a5542d29bc6e40a497c",
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` modified +564/-1131
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #32745 - [Fix] [NPU] qwen3.5: Fix dense serving on Ascend 950

- 链接: https://github.com/sgl-project/sglang/pull/32745
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`；关联提交 `844d2b5decf6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+501/-29，可读 patch 662 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [NPU] qwen3.5: Fix dense serving on Ascend 950」；模型线: Qwen3.5；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/qwen3_5.py`；技术摘要: 覆盖「[Fix] [NPU] qwen3.5: Fix dense serving on Ascend 950」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +31/-5 (36 lines); hunks: -347,6 +347,9 @@ def _select_fused_ar_input_for_linear(hidden_states, linear:...; -1538,6 +1541,31 @@ def forward_prepare_fused_gate(self, positions, hidden_st...; symbols: _select_fused_ar_input_for_linear, forward_prepare_fused_gate, forward_prepare_npu_prefill, forward_prepare_npu，涉及 `_select_fused_ar_input_for_linear, forward_prepare_fused_gate, forward_prepare_npu_prefill`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +31/-5 (36 lines); hunks: -347,6 +347,9 @@ def _select_fused_ar_input_for_linear(hidden_states, linear:...; -1538,6 +1541,31 @@ def forward_prepare_fused_gate(self, positions, hidden_st...; symbols: _select_fused_ar_input_for_linear, forward_prepare_fused_gate, forward_prepare_npu_prefill, forward_prepare_npu
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -347,6 +347,9 @@ def _select_fused_ar_input_for_linear(hidden_states, linear: nn.Module):
+    from sgl_kernel_npu.norm.split_qkv_rmsnorm_mrope import (
+        triton_split_qkv_rmsnorm_mrope,
+    )
@@ -1538,6 +1541,31 @@ def forward_prepare_fused_gate(self, positions, hidden_states):
+    def forward_prepare_npu_prefill(self, positions, hidden_states):
+        rotary_emb = self.rotary_emb
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +31/-5
- 验证与风险: diff 自带测试面 `test/registered/rotary/test_mrope_axis_map.py`, `test/registered/unit/layers/quantization/test_modelslim_mxfp8.py`, `test/registered/unit/npu/test_npu_gemma_rmsnorm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #46017 - [Doc] cookbook: Qwen3.5 MI355X FP8 agentic uses HiCache write_through on the v0.5.22 image

- 链接: https://github.com/sgl-project/sglang/pull/46017
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `69f830756e59`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-4，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: Qwen3.5 MI355X FP8 agentic uses HiCache write_through on the v0.5.22 image」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；技术摘要: 覆盖「[Doc] cookbook: Qwen3.5 MI355X FP8 agentic uses HiCache write_through on the v0.5.22 image」；主要实现面是 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3 (6 lines); hunks: -103,10 +103,10 @@ uv pip install --prerelease=allow 'git+https://github.com/...; -127,7 +127,7 @@ This section provides deployment configurations optimized fo...；`docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +1/-1 (2 lines); hunks: -578,7 +578,7 @@ export const Qwen35Deployment = () => {。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3 (6 lines); hunks: -103,10 +103,10 @@ uv pip install --prerelease=allow 'git+https://github.com/...; -127,7 +127,7 @@ This section provides deployment configurations optimized fo...
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +1/-1 (2 lines); hunks: -578,7 +578,7 @@ export const Qwen35Deployment = () => {
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -103,10 +103,10 @@ uv pip install --prerelease=allow 'git+https://github.com/sgl-project/sglang.git
-docker pull lmsysorg/sglang-rocm:v0.5.15.post1-rocm720-mi30x-20260715
+docker pull lmsysorg/sglang-rocm:v0.5.22-rocm720-mi30x-20261020
-docker pull lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260927
+docker pull lmsysorg/sglang-rocm:v0.5.22-rocm720-mi35x-20261020
@@ -127,7 +127,7 @@ This section provides deployment configurations optimized for different hardware
-- **KV cache offloading (397B FP8 on MI355X):** A separate recipe from the MXFP4 one above, for long-context agentic serving of the FP8 checkpoint. Selecting **Host DRAM (HiCache)
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -578,7 +578,7 @@ export const Qwen35Deployment = () => {
-      cmd += ' \\\n  --hicache-write-policy write_through_selective';
+      cmd += ' \\\n  --hicache-write-policy write_through';
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +3/-3; `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #46032 - [Doc] cookbook: Qwen3.5 MI355X FP8 agentic adds scheduler/tokenizer tuning from the InferenceX recipe

- 链接: https://github.com/sgl-project/sglang/pull/46032
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；关联提交 `f967418a35cf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+9/-1，可读 patch 24 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: Qwen3.5 MI355X FP8 agentic adds scheduler/tokenizer tuning from the InferenceX recipe」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[Doc] cookbook: Qwen3.5 MI355X FP8 agentic adds scheduler/tokenizer tuning from the InferenceX recipe」；主要实现面是 `docs/src/snippets/autoregressive/qwen35-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +8/-0 (8 lines); hunks: -582,6 +582,14 @@ export const Qwen35Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +1/-1 (2 lines); hunks: -127,7 +127,7 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +8/-0 (8 lines); hunks: -582,6 +582,14 @@ export const Qwen35Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +1/-1 (2 lines); hunks: -127,7 +127,7 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen35-deployment.jsx
@@ -582,6 +582,14 @@ export const Qwen35Deployment = () => {
+      // Scheduler / tokenizer tuning from the same recipe: larger prefill chunks,
+      // coarser scheduler polling and token streaming, and parallel tokenization
+      // so 256k-token warmups stay within client timeouts.
+      cmd += ' \\\n  --chunked-prefill-size 16384';
+      cmd += ' \\\n  --max-prefill-tokens 16384';
+      cmd += ' \\\n  --scheduler-recv-interval 60';
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -127,7 +127,7 @@ This section provides deployment configurations optimized for different hardware
-- **KV cache offloading (397B FP8 on MI355X):** A separate recipe from the MXFP4 one above, for long-context agentic serving of the FP8 checkpoint. Selecting **Host DRAM (HiCache)
+- **KV cache offloading (397B FP8 on MI355X):** A separate recipe from the MXFP4 one above, for long-context agentic serving of the FP8 checkpoint. Selecting **Host DRAM (HiCache)
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen35-deployment.jsx` modified +8/-0; `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #43839 - [Perf] [AMD] qwen3_5: Quantize the BF16 GDN projections to MXFP4 online

- 链接: https://github.com/sgl-project/sglang/pull/43839
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_online_mxfp4.py`；关联提交 `3145c7ae6650`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+187/-1，可读 patch 249 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [AMD] qwen3_5: Quantize the BF16 GDN projections to MXFP4 online」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_online_mxfp4.py`；技术摘要: 覆盖「[Perf] [AMD] qwen3_5: Quantize the BF16 GDN projections to MXFP4 online」；主要实现面是 `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_online_mxfp4.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/qwen3_5.py` modified +32/-0 (32 lines); hunks: -184,6 +184,11; -528,6 +533,22 @@ def __init__(; symbols: __init__, _override_weight_loader, get_input_embeddings, prepare_before_cuda_graph_capture，涉及 `__init__, _override_weight_loader, get_input_embeddings`；`test/registered/amd/test_qwen35_gdn_online_mxfp4.py` added +62/-0 (62 lines); hunks: -0,0 +1,62; symbols: TestQwen35GdnOnlineMxfp4, test_matches_dequantized_reference，涉及 `TestQwen35GdnOnlineMxfp4, test_matches_dequantized_reference`。
- 代码 diff 细节:
  - `python/sglang/srt/models/qwen3_5.py` modified +32/-0 (32 lines); hunks: -184,6 +184,11; -528,6 +533,22 @@ def __init__(; symbols: __init__, _override_weight_loader, get_input_embeddings, prepare_before_cuda_graph_capture
  - `test/registered/amd/test_qwen35_gdn_online_mxfp4.py` added +62/-0 (62 lines); hunks: -0,0 +1,62; symbols: TestQwen35GdnOnlineMxfp4, test_matches_dequantized_reference
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/qwen3_5.py
@@ -184,6 +184,11 @@
+_gdn_online_mxfp4 = (
+    ("in_proj_qkvz", "out_proj")
+    if envs.SGLANG_ROCM_GDN_ONLINE_MXFP4.get() and _use_aiter and _is_gfx95
+    else ()
+)
@@ -528,6 +533,22 @@ def __init__(
diff -- test/registered/amd/test_qwen35_gdn_online_mxfp4.py
@@ -0,0 +1,62 @@
+"""ROCm coverage for the online MXFP4 Qwen3.5/3.8 GDN projections."""
+import itertools
+import unittest
+import torch
+from sglang.srt.utils import is_gfx95_supported
+from sglang.test.ci.ci_register import register_amd_ci
```

- 已读文件:
  - runtime: `python/sglang/srt/models/qwen3_5.py` modified +32/-0
  - tests: `test/registered/amd/test_qwen35_gdn_online_mxfp4.py` added +62/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/test_qwen35_gdn_online_mxfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #46757 - [Doc] [AMD] cookbook: Add the Qwen3.5 MI355X FP8 agentic recipe covering the GPU-resident and HiCache bands

- 链接: https://github.com/sgl-project/sglang/pull/46757
- 状态/时间: merged / 2026-10-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；关联提交 `45252c64ca85`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+81/-2，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] [AMD] cookbook: Add the Qwen3.5 MI355X FP8 agentic recipe covering the GPU-resident and HiCache bands」；模型线: Qwen3.5；类别: 性能/后端优化；主要 diff: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；技术摘要: 覆盖「[Doc] [AMD] cookbook: Add the Qwen3.5 MI355X FP8 agentic recipe covering the GPU-resident and HiCache bands」；主要实现面是 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +81/-2 (83 lines); hunks: -127,7 +127,7 @@ This section provides deployment configurations optimized fo...; -227,7 +227,7 @@ This section provides deployment configurations optimized fo...。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +81/-2 (83 lines); hunks: -127,7 +127,7 @@ This section provides deployment configurations optimized fo...; -227,7 +227,7 @@ This section provides deployment configurations optimized fo...
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx
@@ -127,7 +127,7 @@ This section provides deployment configurations optimized for different hardware
-- **KV cache offloading (397B FP8 on MI355X):** A separate recipe from the MXFP4 one above, for long-context agentic serving of the FP8 checkpoint. Selecting **Host DRAM (HiCache)
+- **KV cache offloading (397B FP8 on MI355X):** A separate recipe from the MXFP4 one above, for long-context agentic serving of the FP8 checkpoint. Selecting **Host DRAM (HiCache)
@@ -227,7 +227,7 @@ This section provides deployment configurations optimized for different hardware
-**FP8 KV Cache**: `--kv-cache-dtype fp8_e4m3` quantizes the KV cache to FP8 at runtime. Since these FP8 model checkpoints do not include pre-calibrated KV cache scaling factors, S
+**FP8 KV Cache**: `--kv-cache-dtype fp8_e4m3` quantizes the KV cache to FP8 at runtime. Since these FP8 model checkpoints do not include pre-calibrated KV cache scaling factors, S
@@ -247,6 +247,85 @@ import { agentx } from "/src/snippets/agentx/Qwen/qwen3.5.jsx";
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx` modified +81/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
