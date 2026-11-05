# sglang Nemotron Super 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3-Nano-Omni.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3-Nano.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3-Super.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` | [#33481](https://github.com/sgl-project/sglang/pull/33481), [#36186](https://github.com/sgl-project/sglang/pull/36186), [#44510](https://github.com/sgl-project/sglang/pull/44510) |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx` | [#44510](https://github.com/sgl-project/sglang/pull/44510) |
| `docs/src/snippets/autoregressive/nemotron3-nano-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/nemotron3-nano-omni-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/nemotron3-super-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/nemotron3-ultra-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx` | [#33481](https://github.com/sgl-project/sglang/pull/33481) |
| `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` | [#33481](https://github.com/sgl-project/sglang/pull/33481), [#34573](https://github.com/sgl-project/sglang/pull/34573) |
| `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx` | [#44510](https://github.com/sgl-project/sglang/pull/44510), [#44587](https://github.com/sgl-project/sglang/pull/44587) |
| `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` | [#44510](https://github.com/sgl-project/sglang/pull/44510), [#44587](https://github.com/sgl-project/sglang/pull/44587) |
| `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py` | [#45885](https://github.com/sgl-project/sglang/pull/45885) |
| `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py` | [#35599](https://github.com/sgl-project/sglang/pull/35599), [#43685](https://github.com/sgl-project/sglang/pull/43685), [#44750](https://github.com/sgl-project/sglang/pull/44750) |
| `python/sglang/srt/configs/jet_nemotron.py` | [#12448](https://github.com/sgl-project/sglang/pull/12448) |
| `python/sglang/srt/configs/nano_nemotron_vl.py` | [#12277](https://github.com/sgl-project/sglang/pull/12277), [#23568](https://github.com/sgl-project/sglang/pull/23568), [#23857](https://github.com/sgl-project/sglang/pull/23857), [#25023](https://github.com/sgl-project/sglang/pull/25023), [#35599](https://github.com/sgl-project/sglang/pull/35599), [#39798](https://github.com/sgl-project/sglang/pull/39798), [#44487](https://github.com/sgl-project/sglang/pull/44487) |
| `python/sglang/srt/configs/nemotron_h.py` | [#10909](https://github.com/sgl-project/sglang/pull/10909), [#12690](https://github.com/sgl-project/sglang/pull/12690), [#16227](https://github.com/sgl-project/sglang/pull/16227), [#19950](https://github.com/sgl-project/sglang/pull/19950), [#20458](https://github.com/sgl-project/sglang/pull/20458), [#24429](https://github.com/sgl-project/sglang/pull/24429) |
| `python/sglang/srt/models/jet_nemotron.py` | [#12448](https://github.com/sgl-project/sglang/pull/12448), [#42306](https://github.com/sgl-project/sglang/pull/42306) |
| `python/sglang/srt/models/nano_nemotron_vl.py` | [#12277](https://github.com/sgl-project/sglang/pull/12277), [#14051](https://github.com/sgl-project/sglang/pull/14051), [#23568](https://github.com/sgl-project/sglang/pull/23568), [#23857](https://github.com/sgl-project/sglang/pull/23857), [#25023](https://github.com/sgl-project/sglang/pull/25023), [#35599](https://github.com/sgl-project/sglang/pull/35599), [#39798](https://github.com/sgl-project/sglang/pull/39798), [#42933](https://github.com/sgl-project/sglang/pull/42933), [#43685](https://github.com/sgl-project/sglang/pull/43685), [#44518](https://github.com/sgl-project/sglang/pull/44518), [#44581](https://github.com/sgl-project/sglang/pull/44581) |
| `python/sglang/srt/models/nemotron3_embedding.py` | [#45885](https://github.com/sgl-project/sglang/pull/45885) |
| `python/sglang/srt/models/nemotron_h.py` | [#10909](https://github.com/sgl-project/sglang/pull/10909), [#11866](https://github.com/sgl-project/sglang/pull/11866), [#12015](https://github.com/sgl-project/sglang/pull/12015), [#12277](https://github.com/sgl-project/sglang/pull/12277), [#12690](https://github.com/sgl-project/sglang/pull/12690), [#16172](https://github.com/sgl-project/sglang/pull/16172), [#16227](https://github.com/sgl-project/sglang/pull/16227), [#16569](https://github.com/sgl-project/sglang/pull/16569), [#17013](https://github.com/sgl-project/sglang/pull/17013), [#18546](https://github.com/sgl-project/sglang/pull/18546), [#19903](https://github.com/sgl-project/sglang/pull/19903), [#20580](https://github.com/sgl-project/sglang/pull/20580), ... (35 total) |
| `python/sglang/srt/models/nemotron_h_mtp.py` | [#17013](https://github.com/sgl-project/sglang/pull/17013), [#19433](https://github.com/sgl-project/sglang/pull/19433), [#24429](https://github.com/sgl-project/sglang/pull/24429), [#24955](https://github.com/sgl-project/sglang/pull/24955), [#28346](https://github.com/sgl-project/sglang/pull/28346), [#33123](https://github.com/sgl-project/sglang/pull/33123), [#35599](https://github.com/sgl-project/sglang/pull/35599), [#40800](https://github.com/sgl-project/sglang/pull/40800), [#41430](https://github.com/sgl-project/sglang/pull/41430), [#43685](https://github.com/sgl-project/sglang/pull/43685) |
| `python/sglang/srt/models/nemotron_h_nvfp4_layout.py` | [#45082](https://github.com/sgl-project/sglang/pull/45082) |
| `python/sglang/srt/models/nemotron_h_utils.py` | [#24955](https://github.com/sgl-project/sglang/pull/24955), [#28102](https://github.com/sgl-project/sglang/pull/28102), [#28309](https://github.com/sgl-project/sglang/pull/28309), [#28346](https://github.com/sgl-project/sglang/pull/28346), [#40867](https://github.com/sgl-project/sglang/pull/40867), [#41430](https://github.com/sgl-project/sglang/pull/41430) |
| `python/sglang/srt/models/nemotron_nas.py` | [#9067](https://github.com/sgl-project/sglang/pull/9067), [#42308](https://github.com/sgl-project/sglang/pull/42308) |
| `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` | [#12277](https://github.com/sgl-project/sglang/pull/12277), [#14051](https://github.com/sgl-project/sglang/pull/14051), [#23568](https://github.com/sgl-project/sglang/pull/23568), [#23857](https://github.com/sgl-project/sglang/pull/23857), [#35599](https://github.com/sgl-project/sglang/pull/35599), [#42933](https://github.com/sgl-project/sglang/pull/42933), [#44184](https://github.com/sgl-project/sglang/pull/44184) |
| `test/manual/models/test_nvidia_nemotron_nano_v2.py` | 无直接 PR 号提交 |
| `test/manual/models/test_nvidia_nemotron_nano_v2_vl.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_nvidia_nemotron_3_nano.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_nvidia_nemotron_3_super_bf16_mtp.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models_large/test_nvidia_nemotron_3_super_nightly.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models_large/test_nvidia_nemotron_3_super_nvfp4.py` | [#43685](https://github.com/sgl-project/sglang/pull/43685) |
| `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py` | [#23594](https://github.com/sgl-project/sglang/pull/23594) |
| `test/registered/prefill_only/test_nemotron3_embedding.py` | [#45885](https://github.com/sgl-project/sglang/pull/45885) |
| `test/registered/unit/configs/test_nano_nemotron_vl_config.py` | [#35599](https://github.com/sgl-project/sglang/pull/35599), [#39798](https://github.com/sgl-project/sglang/pull/39798), [#44487](https://github.com/sgl-project/sglang/pull/44487) |
| `test/registered/unit/layer_boundary/test_nemotron_h_aux_capture.py` | 无直接 PR 号提交 |
| `test/registered/unit/layer_boundary/test_nemotron_h_stages.py` | 无直接 PR 号提交 |
| `test/registered/unit/models/test_nano_nemotron_vl.py` | [#35599](https://github.com/sgl-project/sglang/pull/35599), [#39798](https://github.com/sgl-project/sglang/pull/39798), [#42933](https://github.com/sgl-project/sglang/pull/42933), [#43685](https://github.com/sgl-project/sglang/pull/43685), [#44581](https://github.com/sgl-project/sglang/pull/44581) |
| `test/registered/unit/models/test_nemotron_h_mtp.py` | [#35599](https://github.com/sgl-project/sglang/pull/35599) |
| `test/registered/unit/models/test_nemotron_h_shared_add.py` | [#30430](https://github.com/sgl-project/sglang/pull/30430) |
| `test/registered/unit/models/test_nemotron_h_weight_loading.py` | [#24434](https://github.com/sgl-project/sglang/pull/24434), [#26522](https://github.com/sgl-project/sglang/pull/26522), [#30456](https://github.com/sgl-project/sglang/pull/30456), [#35599](https://github.com/sgl-project/sglang/pull/35599) |
| `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` | [#35599](https://github.com/sgl-project/sglang/pull/35599), [#42933](https://github.com/sgl-project/sglang/pull/42933), [#44184](https://github.com/sgl-project/sglang/pull/44184), [#44581](https://github.com/sgl-project/sglang/pull/44581) |
| `test/registered/xpu/llm_models/test_xpu_nemotron_3_nano_30b_a3b.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 61
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 61
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2025-08-17 | [#9067](https://github.com/sgl-project/sglang/pull/9067) | merged | model: support nvidia/Llama-3_3-Nemotron-Super-49B-v1 | `python/sglang/srt/models/nemotron_nas.py` |
| 2025-10-08 | [#10909](https://github.com/sgl-project/sglang/pull/10909) | merged | model: Support Hybrid Mamba2 NemotronHForCausalLM (nvidia/NVIDIA-Nemotron-Nano-9B-v2) | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py` |
| 2025-10-23 | [#11866](https://github.com/sgl-project/sglang/pull/11866) | merged | Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4 | `python/sglang/srt/models/nemotron_h.py` |
| 2025-10-23 | [#12015](https://github.com/sgl-project/sglang/pull/12015) | merged | Revert "Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4" | `python/sglang/srt/models/nemotron_h.py` |
| 2025-11-09 | [#12448](https://github.com/sgl-project/sglang/pull/12448) | merged | Add Jet-Nemotron | `python/sglang/srt/models/jet_nemotron.py`, `python/sglang/srt/configs/jet_nemotron.py` |
| 2025-11-21 | [#12690](https://github.com/sgl-project/sglang/pull/12690) | merged | Feat/nemotron nano v3 support | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py` |
| 2025-11-26 | [#12277](https://github.com/sgl-project/sglang/pull/12277) | merged | Support nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 (and nvidia/C-RADIOv2-H) | `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py` |
| 2025-12-31 | [#16172](https://github.com/sgl-project/sglang/pull/16172) | merged | [NemotronH] PP support | `python/sglang/srt/models/nemotron_h.py` |
| 2026-01-02 | [#16227](https://github.com/sgl-project/sglang/pull/16227) | merged | [NemotronH] Add latent MoE support | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py` |
| 2026-01-05 | [#14051](https://github.com/sgl-project/sglang/pull/14051) | merged | EVS Framework: Support NemotronH_Nano_VL_V2 | `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py` |
| 2026-01-14 | [#17013](https://github.com/sgl-project/sglang/pull/17013) | merged | Feat/support nemotron h mtp | `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-01-14 | [#16569](https://github.com/sgl-project/sglang/pull/16569) | merged | [NemotronH] Use ReplicatedLinear for fc1_latent_proj | `python/sglang/srt/models/nemotron_h.py` |
| 2026-02-21 | [#18546](https://github.com/sgl-project/sglang/pull/18546) | merged | [Quantization] Support config.json quantization_config format, fix exclude_modules matching, and fix KV cache scale loading for Nemotron | `python/sglang/srt/models/nemotron_h.py` |
| 2026-03-03 | [#19433](https://github.com/sgl-project/sglang/pull/19433) | merged | Fix/nemotron mtp quantaized | `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-03-07 | [#19950](https://github.com/sgl-project/sglang/pull/19950) | merged | Refactor NemotronHConfig to canonical layers_block_type and add MTP block-type support | `python/sglang/srt/configs/nemotron_h.py` |
| 2026-03-12 | [#19903](https://github.com/sgl-project/sglang/pull/19903) | merged | Enable Piecewise CUDA Graph for NemotronH Hybrid (Mamba+Attention) Models | `python/sglang/srt/models/nemotron_h.py` |
| 2026-03-15 | [#20458](https://github.com/sgl-project/sglang/pull/20458) | merged | fix: Nemotron chunk size alias | `python/sglang/srt/configs/nemotron_h.py` |
| 2026-03-17 | [#20580](https://github.com/sgl-project/sglang/pull/20580) | merged | [Model] Fix NemotronH OOM on unified-mem systems: stream weights | `python/sglang/srt/models/nemotron_h.py` |
| 2026-04-25 | [#23568](https://github.com/sgl-project/sglang/pull/23568) | merged | Parakeet nemotron encoder | `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py` |
| 2026-04-28 | [#23874](https://github.com/sgl-project/sglang/pull/23874) | merged | Fix failing `test_nvidia_nemotron_3_nano` by fixing `test_grouped_topk` | `python/sglang/srt/models/nemotron_h.py` |
| 2026-04-29 | [#23857](https://github.com/sgl-project/sglang/pull/23857) | merged | Nemotron-omni-v3-alias | `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py` |
| 2026-04-29 | [#21321](https://github.com/sgl-project/sglang/pull/21321) | merged | [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron) | `python/sglang/srt/models/nemotron_h.py` |
| 2026-04-30 | [#23594](https://github.com/sgl-project/sglang/pull/23594) | merged | LoRA support for qwen3.5 and nemotron3 | `python/sglang/srt/models/nemotron_h.py`, `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py` |
| 2026-05-08 | [#24434](https://github.com/sgl-project/sglang/pull/24434) | merged | [NemotronH] Fix expert scale weight loading | `test/registered/unit/models/test_nemotron_h_weight_loading.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-05-26 | [#25023](https://github.com/sgl-project/sglang/pull/25023) | merged | [NemotronH] V3 Omni wrapper: WeightsMapper + config round-trip | `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py` |
| 2026-05-27 | [#24429](https://github.com/sgl-project/sglang/pull/24429) | merged | Support NemotronHPuzzleForCausalLM | `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-05-28 | [#26522](https://github.com/sgl-project/sglang/pull/26522) | merged | [NemotronH] Fix weight-loading unit test broken by Puzzle support | `test/registered/unit/models/test_nemotron_h_weight_loading.py` |
| 2026-06-06 | [#26733](https://github.com/sgl-project/sglang/pull/26733) | merged | Nemotron perf changes | `python/sglang/srt/models/nemotron_h.py` |
| 2026-06-12 | [#24955](https://github.com/sgl-project/sglang/pull/24955) | merged | Support Nemotron DP attention and MTP | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-06-13 | [#28102](https://github.com/sgl-project/sglang/pull/28102) | merged | Fix DP attention + EP mode of Nemotron | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py` |
| 2026-06-19 | [#28346](https://github.com/sgl-project/sglang/pull/28346) | merged | Use Flashinfer allreduce fusion for MNNVL allreduce for Nemotron | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-07-13 | [#30968](https://github.com/sgl-project/sglang/pull/30968) | merged | [Bugfix] Fix Nemotron ForwardFlags across custom op boundary | `python/sglang/srt/models/nemotron_h.py` |
| 2026-07-16 | [#29692](https://github.com/sgl-project/sglang/pull/29692) | merged | Use fused A GEMM for `fc1_latent_proj` in NemotronH | `python/sglang/srt/models/nemotron_h.py` |
| 2026-07-16 | [#28309](https://github.com/sgl-project/sglang/pull/28309) | merged | Support Flashinfer one-sided A2A + CuteDSL MoE for Nemotron Ultra | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py` |
| 2026-07-16 | [#30456](https://github.com/sgl-project/sglang/pull/30456) | merged | [NemotronH] Load shared embed_tokens/lm_head in MTP draft weights | `test/registered/unit/models/test_nemotron_h_weight_loading.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-08-05 | [#33123](https://github.com/sgl-project/sglang/pull/33123) | merged | Fix broken Nemotron DP attention | `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-08-11 | [#33481](https://github.com/sgl-project/sglang/pull/33481) | merged | Add NVIDIA Nemotron 3.5 Lightning cookbook | `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` |
| 2026-08-12 | [#34573](https://github.com/sgl-project/sglang/pull/34573) | merged | docs(cookbook): add BF16 recipes to Nemotron 3.5 Lightning | `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` |
| 2026-08-19 | [#34561](https://github.com/sgl-project/sglang/pull/34561) | merged | [Fix] Fix Nemotron-H Mamba illegal memory access under DP attention with CUDA graph | `python/sglang/srt/models/nemotron_h.py` |
| 2026-08-25 | [#36186](https://github.com/sgl-project/sglang/pull/36186) | merged | [Model] Support Nemotron 3.5 Lightning speculative decoding | `python/sglang/srt/models/nemotron_h.py`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` |
| 2026-09-07 | [#30430](https://github.com/sgl-project/sglang/pull/30430) | merged | Fuse Nemotron latent MoE projection and shared add | `test/registered/unit/models/test_nemotron_h_shared_add.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-09-10 | [#35599](https://github.com/sgl-project/sglang/pull/35599) | merged | Support NemotronH_Omni_Reasoning_V3 in SGLang | `test/registered/unit/models/test_nemotron_h_mtp.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py` |
| 2026-09-23 | [#40800](https://github.com/sgl-project/sglang/pull/40800) | merged | [Fix] Reduce Nemotron MTP attention outputs once | `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-09-23 | [#40801](https://github.com/sgl-project/sglang/pull/40801) | merged | [Fix] Capture complete Nemotron auxiliary hidden states | `python/sglang/srt/models/nemotron_h.py` |
| 2026-09-23 | [#40867](https://github.com/sgl-project/sglang/pull/40867) | merged | [Refactor] Run Nemotron-H DP attention through the standard layer communicator | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py` |
| 2026-09-27 | [#41430](https://github.com/sgl-project/sglang/pull/41430) | merged | [Refactor] Nemotron-H: build each layer's boundaries from its stage and the previous one | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-10-03 | [#42306](https://github.com/sgl-project/sglang/pull/42306) | merged | [Fix] Jet-Nemotron build and Granite MoE hybrid final norm | `python/sglang/srt/models/jet_nemotron.py` |
| 2026-10-03 | [#42308](https://github.com/sgl-project/sglang/pull/42308) | merged | [Refactor] Build the Llama and Nemotron-NAS decoders from stage boundaries | `python/sglang/srt/models/nemotron_nas.py` |
| 2026-10-13 | [#42933](https://github.com/sgl-project/sglang/pull/42933) | merged | Fix EVS for NemotronH_Omni_Reasoning_V3 | `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` |
| 2026-10-13 | [#39798](https://github.com/sgl-project/sglang/pull/39798) | merged | [lora] Support LoRA for the NemotronH_Nano_VL_V2 model family | `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `python/sglang/srt/models/nano_nemotron_vl.py` |
| 2026-10-15 | [#43685](https://github.com/sgl-project/sglang/pull/43685) | merged | Support EPLB for Nemotron-H | `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h_mtp.py` |
| 2026-10-15 | [#44510](https://github.com/sgl-project/sglang/pull/44510) | merged | [Doc] cookbook: Add Nemotron 3.5 Super VL | `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx` |
| 2026-10-19 | [#44587](https://github.com/sgl-project/sglang/pull/44587) | merged | [Doc] nemotron-3.5-super: update H200 and Spark wizard recipes | `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` |
| 2026-10-19 | [#44518](https://github.com/sgl-project/sglang/pull/44518) | merged | [Feat] nemotron: Port Nemotron 3.5 Super serving changes | `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nano_nemotron_vl.py` |
| 2026-10-21 | [#44184](https://github.com/sgl-project/sglang/pull/44184) | merged | [Fix] nemotron_vl: Preserve tokenized prompts during media expansion | `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` |
| 2026-10-21 | [#45082](https://github.com/sgl-project/sglang/pull/45082) | merged | [Fix] nemotron: Correct weight-export failures and GEMV dispatch | `python/sglang/srt/models/nemotron_h_nvfp4_layout.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-10-22 | [#44581](https://github.com/sgl-project/sglang/pull/44581) | merged | [Fix] nemotron_vl: Pad visual spans using processor offsets | `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `test/registered/unit/models/test_nano_nemotron_vl.py` |
| 2026-10-26 | [#46551](https://github.com/sgl-project/sglang/pull/46551) | merged | [Refactor] nemotron_h: Read the prefill shared expert's output from the caller's holder | `python/sglang/srt/models/nemotron_h.py` |
| 2026-10-27 | [#44487](https://github.com/sgl-project/sglang/pull/44487) | merged | [Fix] nemotron: Preserve nested Puzzle configs | `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `python/sglang/srt/configs/nano_nemotron_vl.py` |
| 2026-10-30 | [#44750](https://github.com/sgl-project/sglang/pull/44750) | merged | [Fix] nemotron-h: Allow explicit CuTe DSL W4A16 MoE | `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py` |
| 2026-11-04 | [#45885](https://github.com/sgl-project/sglang/pull/45885) | merged | [Feat] nemotron3-embed: Support Nemotron-3-Embed embedding models | `python/sglang/srt/models/nemotron3_embedding.py`, `test/registered/prefill_only/test_nemotron3_embedding.py`, `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py` |

## 逐 PR diff 审计卡

### PR #9067 - model: support nvidia/Llama-3_3-Nemotron-Super-49B-v1

- 链接: https://github.com/sgl-project/sglang/pull/9067
- 状态/时间: merged / 2025-08-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_nas.py`；关联提交 `845d12a979fb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+465/-5，可读 patch 505 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「model: support nvidia/Llama-3_3-Nemotron-Super-49B-v1」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nemotron_nas.py`；技术摘要: 覆盖「model: support nvidia/Llama-3_3-Nemotron-Super-49B-v1」；主要实现面是 `python/sglang/srt/models/nemotron_nas.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_nas.py` added +435/-0 (435 lines); hunks: -0,0 +1,435; symbols: _ffn_mult_to_intermediate_size, _find_multiple, DeciLMDecoderLayer, __init__，涉及 `_ffn_mult_to_intermediate_size, _find_multiple, DeciLMDecoderLayer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_nas.py` added +435/-0 (435 lines); hunks: -0,0 +1,435; symbols: _ffn_mult_to_intermediate_size, _find_multiple, DeciLMDecoderLayer, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_nas.py
@@ -0,0 +1,435 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_nas.py` added +435/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/runners.py`, `test/srt/models/test_generation_models.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #10909 - model: Support Hybrid Mamba2 NemotronHForCausalLM (nvidia/NVIDIA-Nemotron-Nano-9B-v2)

- 链接: https://github.com/sgl-project/sglang/pull/10909
- 状态/时间: merged / 2025-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py`；关联提交 `d6837aea4d2c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 35 个文件，+3279/-853，可读 patch 4929 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「model: Support Hybrid Mamba2 NemotronHForCausalLM (nvidia/NVIDIA-Nemotron-Nano-9B-v2)」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py`；技术摘要: 覆盖「model: Support Hybrid Mamba2 NemotronHForCausalLM (nvidia/NVIDIA-Nemotron-Nano-9B-v2)」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` added +514/-0 (514 lines); hunks: -0,0 +1,514; symbols: NemotronHMLP, __init__, forward, NemotronHMLPDecoderLayer，涉及 `NemotronHMLP, __init__, forward`；`python/sglang/srt/configs/nemotron_h.py` added +286/-0 (286 lines); hunks: -0,0 +1,286; symbols: NemotronHConfig, to, __init__, mamba_layer_ids，涉及 `NemotronHConfig, to, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` added +514/-0 (514 lines); hunks: -0,0 +1,514; symbols: NemotronHMLP, __init__, forward, NemotronHMLPDecoderLayer
  - `python/sglang/srt/configs/nemotron_h.py` added +286/-0 (286 lines); hunks: -0,0 +1,286; symbols: NemotronHConfig, to, __init__, mamba_layer_ids
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -0,0 +1,514 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/configs/nemotron_h.py
@@ -0,0 +1,286 @@
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` added +514/-0; `python/sglang/srt/configs/nemotron_h.py` added +286/-0
- 验证与风险: diff 自带测试面 `test/srt/layers/attention/mamba/test_causal_conv1d.py`, `test/srt/layers/attention/mamba/test_mamba2_mixer.py`, `test/srt/layers/attention/mamba/test_mamba_ssm.py`, `test/srt/layers/attention/mamba/test_mamba_ssm_ssd.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #11866 - Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4

- 链接: https://github.com/sgl-project/sglang/pull/11866
- 状态/时间: merged / 2025-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `d6fee73d1f59`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+207/-127，可读 patch 628 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +19/-22 (41 lines); hunks: -48,6 +48,8; -155,6 +157,7 @@ def __init__(; symbols: __init__, forward, NemotronHForCausalLM, _init_model，涉及 `__init__, forward, NemotronHForCausalLM`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +19/-22 (41 lines); hunks: -48,6 +48,8; -155,6 +157,7 @@ def __init__(; symbols: __init__, forward, NemotronHForCausalLM, _init_model
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -48,6 +48,8 @@
+    replace_prefix,
+    replace_substrings,
@@ -155,6 +157,7 @@ def __init__(
+            prefix=f"{prefix}.mixer",
@@ -381,16 +384,19 @@ def forward(
+    stacked_params_mapping = [
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +19/-22
- 验证与风险: diff 自带测试面 `test/srt/layers/attention/mamba/test_causal_conv1d.py`, `test/srt/layers/attention/mamba/test_mamba2_mixer.py`, `test/srt/layers/attention/mamba/test_mamba_ssm.py`, `test/srt/layers/attention/mamba/test_mamba_ssm_ssd.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #12015 - Revert "Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4"

- 链接: https://github.com/sgl-project/sglang/pull/12015
- 状态/时间: merged / 2025-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `6c18addb6f53`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+127/-207，可读 patch 628 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4"」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Revert "Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4"」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +22/-19 (41 lines); hunks: -48,8 +48,6; -157,7 +155,6 @@ def __init__(; symbols: __init__, forward, NemotronHForCausalLM, _init_model，涉及 `__init__, forward, NemotronHForCausalLM`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +22/-19 (41 lines); hunks: -48,8 +48,6; -157,7 +155,6 @@ def __init__(; symbols: __init__, forward, NemotronHForCausalLM, _init_model
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -48,8 +48,6 @@
-    replace_prefix,
-    replace_substrings,
@@ -157,7 +155,6 @@ def __init__(
-            prefix=f"{prefix}.mixer",
@@ -384,19 +381,16 @@ def forward(
-    stacked_params_mapping = [
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +22/-19
- 验证与风险: diff 自带测试面 `test/srt/layers/attention/mamba/test_causal_conv1d.py`, `test/srt/layers/attention/mamba/test_mamba2_mixer.py`, `test/srt/layers/attention/mamba/test_mamba_ssm.py`, `test/srt/layers/attention/mamba/test_mamba_ssm_ssd.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #12448 - Add Jet-Nemotron

- 链接: https://github.com/sgl-project/sglang/pull/12448
- 状态/时间: merged / 2025-11-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/models/jet_nemotron.py`；关联提交 `3633f8b0cfef`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+678/-2，可读 patch 733 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add Jet-Nemotron」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/jet_nemotron.py`, `python/sglang/srt/configs/jet_nemotron.py`；技术摘要: 覆盖「Add Jet-Nemotron」；主要实现面是 `python/sglang/srt/models/jet_nemotron.py`, `python/sglang/srt/configs/jet_nemotron.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/jet_nemotron.py` added +596/-0 (596 lines); hunks: -0,0 +1,596; symbols: DynamicShortConvolutionKernelGenerator, __init__, forward, DynamicShortConvolution，涉及 `DynamicShortConvolutionKernelGenerator, __init__, forward`；`python/sglang/srt/configs/jet_nemotron.py` added +74/-0 (74 lines); hunks: -0,0 +1,74; symbols: JetBlockConfig, JetNemotronConfig, full_attention_layer_ids, linear_layer_ids，涉及 `JetBlockConfig, JetNemotronConfig, full_attention_layer_ids`。
- 代码 diff 细节:
  - `python/sglang/srt/models/jet_nemotron.py` added +596/-0 (596 lines); hunks: -0,0 +1,596; symbols: DynamicShortConvolutionKernelGenerator, __init__, forward, DynamicShortConvolution
  - `python/sglang/srt/configs/jet_nemotron.py` added +74/-0 (74 lines); hunks: -0,0 +1,74; symbols: JetBlockConfig, JetNemotronConfig, full_attention_layer_ids, linear_layer_ids
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/jet_nemotron.py
@@ -0,0 +1,596 @@
+from collections.abc import Iterable
+from typing import cast
+import einops
+import torch
+import torch.nn as nn
+from sglang.srt.configs.jet_nemotron import JetBlockConfig, JetNemotronConfig
diff -- python/sglang/srt/configs/jet_nemotron.py
@@ -0,0 +1,74 @@
+from dataclasses import dataclass
+from typing import Any
+from transformers.configuration_utils import PretrainedConfig
+from sglang.srt.configs.mamba_utils import Mamba2CacheParams, Mamba2StateShape
+@dataclass
+class JetBlockConfig:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/jet_nemotron.py` added +596/-0; `python/sglang/srt/configs/jet_nemotron.py` added +74/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/test_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #12690 - Feat/nemotron nano v3 support

- 链接: https://github.com/sgl-project/sglang/pull/12690
- 状态/时间: merged / 2025-11-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py`；关联提交 `1b48e1b97484`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+775/-67，可读 patch 1291 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Feat/nemotron nano v3 support」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py`；技术摘要: 覆盖「Feat/nemotron nano v3 support」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +259/-28 (287 lines); hunks: -22,8 +22,13; -34,9 +39,13; symbols: NemotronHMLP, __init__, forward, _get_or_create_alt_stream，涉及 `NemotronHMLP, __init__, forward`；`python/sglang/srt/configs/nemotron_h.py` modified +25/-6 (31 lines); hunks: -26,6 +26,7; -189,6 +190,15 @@ def __init__(; symbols: NemotronHConfig, __init__，涉及 `NemotronHConfig, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +259/-28 (287 lines); hunks: -22,8 +22,13; -34,9 +39,13; symbols: NemotronHMLP, __init__, forward, _get_or_create_alt_stream
  - `python/sglang/srt/configs/nemotron_h.py` modified +25/-6 (31 lines); hunks: -26,6 +26,7; -189,6 +190,15 @@ def __init__(; symbols: NemotronHConfig, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -22,8 +22,13 @@
-from sglang.srt.configs.nemotron_h import ATTENTION, MAMBA, MLP
-from sglang.srt.distributed import get_pp_group, get_tensor_model_parallel_world_size
+from sglang.srt.configs.nemotron_h import ATTENTION, MAMBA, MLP, MOE
+from sglang.srt.distributed import (
+    get_moe_ep_group,
+    get_pp_group,
diff -- python/sglang/srt/configs/nemotron_h.py
@@ -26,6 +26,7 @@
+MOE = "E"
@@ -189,6 +190,15 @@ def __init__(
+        n_routed_experts=8,
+        n_shared_experts=1,
+        moe_intermediate_size=7688,
+        moe_shared_expert_intermediate_size=7688,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +259/-28; `python/sglang/srt/configs/nemotron_h.py` modified +25/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=128,N=1856,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=128,N=1856,device_name=NVIDIA_L40S.json`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #12277 - Support nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 (and nvidia/C-RADIOv2-H)

- 链接: https://github.com/sgl-project/sglang/pull/12277
- 状态/时间: merged / 2025-11-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`；关联提交 `082b54c6890a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 17 个文件，+1334/-17，可读 patch 1528 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 (and nvidia/C-RADIOv2-H)」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`；技术摘要: 覆盖「Support nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 (and nvidia/C-RADIOv2-H)」；主要实现面是 `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nano_nemotron_vl.py` added +219/-0 (219 lines); hunks: -0,0 +1,219; symbols: NemotronH_Nano_VL_V2, __init__, pad_input_ids, pixel_shuffle，涉及 `NemotronH_Nano_VL_V2, __init__, pad_input_ids`；`python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` added +197/-0 (197 lines); hunks: -0,0 +1,197; symbols: NanoNemotronVLImageProcessor, __init__, preprocess_image, render_image，涉及 `NanoNemotronVLImageProcessor, __init__, preprocess_image`；`python/sglang/srt/configs/nano_nemotron_vl.py` added +114/-0 (114 lines); hunks: -0,0 +1,114; symbols: float_triplet, NemotronH_Nano_VL_V2_Config, __init__, create_radio_config，涉及 `float_triplet, NemotronH_Nano_VL_V2_Config, __init__`；`python/sglang/srt/models/nemotron_h.py` modified +3/-6 (9 lines); hunks: -542,9 +542,6 @@ def get_layer(idx: int, prefix: str):; -557,7 +554,7 @@ def forward(; symbols: get_layer, get_input_embeddings, forward, _init_model，涉及 `get_layer, get_input_embeddings, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nano_nemotron_vl.py` added +219/-0 (219 lines); hunks: -0,0 +1,219; symbols: NemotronH_Nano_VL_V2, __init__, pad_input_ids, pixel_shuffle
  - `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` added +197/-0 (197 lines); hunks: -0,0 +1,197; symbols: NanoNemotronVLImageProcessor, __init__, preprocess_image, render_image
  - `python/sglang/srt/configs/nano_nemotron_vl.py` added +114/-0 (114 lines); hunks: -0,0 +1,114; symbols: float_triplet, NemotronH_Nano_VL_V2_Config, __init__, create_radio_config
  - `python/sglang/srt/models/nemotron_h.py` modified +3/-6 (9 lines); hunks: -542,9 +542,6 @@ def get_layer(idx: int, prefix: str):; -557,7 +554,7 @@ def forward(; symbols: get_layer, get_input_embeddings, forward, _init_model
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -0,0 +1,219 @@
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/multimodal/processors/nano_nemotron_vl.py
@@ -0,0 +1,197 @@
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/configs/nano_nemotron_vl.py
@@ -0,0 +1,114 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nano_nemotron_vl.py` added +219/-0; `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` added +197/-0; `python/sglang/srt/configs/nano_nemotron_vl.py` added +114/-0; `python/sglang/srt/models/nemotron_h.py` modified +3/-6
- 验证与风险: diff 自带测试面 `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`, `test/srt/run_suite.py`, `test/srt/test_video_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #16172 - [NemotronH] PP support

- 链接: https://github.com/sgl-project/sglang/pull/16172
- 状态/时间: merged / 2025-12-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `47a660d5b925`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+94/-35，可读 patch 207 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NemotronH] PP support」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[NemotronH] PP support」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +88/-35 (123 lines); hunks: -48,6 +48,7; -65,7 +66,7; symbols: __init__, get_layer, forward，涉及 `__init__, get_layer, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +88/-35 (123 lines); hunks: -48,6 +48,7; -65,7 +66,7; symbols: __init__, get_layer, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -48,6 +48,7 @@
+from sglang.srt.layers.utils import PPMissingLayer, get_layer_id
@@ -65,7 +66,7 @@
-    make_layers_non_pp,
+    make_layers,
@@ -526,21 +527,32 @@ def __init__(
+        self.pp_group = get_pp_group()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +88/-35
- 验证与风险: diff 自带测试面 `test/srt/models/test_nvidia_nemotron_nano_v2.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #16227 - [NemotronH] Add latent MoE support

- 链接: https://github.com/sgl-project/sglang/pull/16227
- 状态/时间: merged / 2026-01-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py`；关联提交 `b0213323397c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 23 个文件，+2957/-2，可读 patch 3056 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NemotronH] Add latent MoE support」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py`；技术摘要: 覆盖「[NemotronH] Add latent MoE support」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/configs/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +32/-1 (33 lines); hunks: -138,6 +138,10 @@ def __init__(; -165,7 +169,7 @@ def __init__(; symbols: __init__, _forward_core, _forward_core_normal，涉及 `__init__, _forward_core, _forward_core_normal`；`python/sglang/srt/configs/nemotron_h.py` modified +2/-0 (2 lines); hunks: -194,6 +194,7 @@ def __init__(; -259,6 +260,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +32/-1 (33 lines); hunks: -138,6 +138,10 @@ def __init__(; -165,7 +169,7 @@ def __init__(; symbols: __init__, _forward_core, _forward_core_normal
  - `python/sglang/srt/configs/nemotron_h.py` modified +2/-0 (2 lines); hunks: -194,6 +194,7 @@ def __init__(; -259,6 +260,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -138,6 +138,10 @@ def __init__(
+        self.use_latent_moe = getattr(config, "moe_latent_size", None) is not None
+        self.moe_hidden_size = (
+            config.moe_latent_size if self.use_latent_moe else config.hidden_size
+        )
@@ -165,7 +169,7 @@ def __init__(
-            hidden_size=config.hidden_size,
diff -- python/sglang/srt/configs/nemotron_h.py
@@ -194,6 +194,7 @@ def __init__(
+        moe_latent_size=None,
@@ -259,6 +260,7 @@ def __init__(
+        self.moe_latent_size = moe_latent_size
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +32/-1; `python/sglang/srt/configs/nemotron_h.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1344,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1344,device_name=NVIDIA_H100_80GB_HBM3.json`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14051 - EVS Framework: Support NemotronH_Nano_VL_V2

- 链接: https://github.com/sgl-project/sglang/pull/14051
- 状态/时间: merged / 2026-01-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`；关联提交 `bebd625ba145`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+821/-56，可读 patch 1171 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「EVS Framework: Support NemotronH_Nano_VL_V2」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`；技术摘要: 覆盖「EVS Framework: Support NemotronH_Nano_VL_V2」；主要实现面是 `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +35/-22 (57 lines); hunks: -11,14 +11,16; -40,6 +42,9 @@ class NanoNemotronVLImageProcessor(BaseMultimodalProcessor):; symbols: NanoNemotronVLImageProcessor, __init__, preprocess_image, render_image，涉及 `NanoNemotronVLImageProcessor, __init__, preprocess_image`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +7/-2 (9 lines); hunks: -36,19 +36,24; symbols: NemotronH_Nano_VL_V2, create_evs_config, __init__，涉及 `NemotronH_Nano_VL_V2, create_evs_config, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +35/-22 (57 lines); hunks: -11,14 +11,16; -40,6 +42,9 @@ class NanoNemotronVLImageProcessor(BaseMultimodalProcessor):; symbols: NanoNemotronVLImageProcessor, __init__, preprocess_image, render_image
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +7/-2 (9 lines); hunks: -36,19 +36,24; symbols: NemotronH_Nano_VL_V2, create_evs_config, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/multimodal/processors/nano_nemotron_vl.py
@@ -11,14 +11,16 @@
+from math import sqrt
-from sglang.srt.managers.schedule_batch import Modality, MultimodalDataItem
+from sglang.srt.configs.nano_nemotron_vl import NemotronH_Nano_VL_V2_Config
+from sglang.srt.multimodal.evs import EVSProcessor
@@ -40,6 +42,9 @@ class NanoNemotronVLImageProcessor(BaseMultimodalProcessor):
+        self.evs = EVSProcessor(
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -36,19 +36,24 @@
+from sglang.srt.multimodal.evs import EVS, EVSConfig
-class NemotronH_Nano_VL_V2(nn.Module):
+class NemotronH_Nano_VL_V2(EVS):
+    @staticmethod
+    def create_evs_config(config: NemotronH_Nano_VL_V2_Config):
+        return EVSConfig(video_pruning_rate=config.video_pruning_rate)
```

- 已读文件:
  - runtime: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +35/-22; `python/sglang/srt/models/nano_nemotron_vl.py` modified +7/-2
- 验证与风险: diff 自带测试面 `python/sglang/test/test_utils.py`, `test/srt/run_suite.py`, `test/srt/test_evs.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17013 - Feat/support nemotron h mtp

- 链接: https://github.com/sgl-project/sglang/pull/17013
- 状态/时间: merged / 2026-01-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`；关联提交 `ba625c2d908a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+378/-1，可读 patch 408 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Feat/support nemotron h mtp」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Feat/support nemotron h mtp」；主要实现面是 `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h_mtp.py` added +340/-0 (340 lines); hunks: -0,0 +1,340; symbols: NemotronHMTPAttentionDecoderLayer, __init__, forward, NemotronHMTPMoEDecoderLayer，涉及 `NemotronHMTPAttentionDecoderLayer, __init__, forward`；`python/sglang/srt/models/nemotron_h.py` modified +28/-1 (29 lines); hunks: -728,7 +728,20 @@ def copy_inputs_before_cuda_graphs(self, input_buffers, **k...; -749,6 +762,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: copy_inputs_before_cuda_graphs, get_seqlen_agnostic_capture_inputs, load_weights, get_embed_and_head，涉及 `copy_inputs_before_cuda_graphs, get_seqlen_agnostic_capture_inputs, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h_mtp.py` added +340/-0 (340 lines); hunks: -0,0 +1,340; symbols: NemotronHMTPAttentionDecoderLayer, __init__, forward, NemotronHMTPMoEDecoderLayer
  - `python/sglang/srt/models/nemotron_h.py` modified +28/-1 (29 lines); hunks: -728,7 +728,20 @@ def copy_inputs_before_cuda_graphs(self, input_buffers, **k...; -749,6 +762,20 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: copy_inputs_before_cuda_graphs, get_seqlen_agnostic_capture_inputs, load_weights, get_embed_and_head
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -0,0 +1,340 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/nemotron_h.py
@@ -728,7 +728,20 @@ def copy_inputs_before_cuda_graphs(self, input_buffers, **kwargs):
-    def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> None:
+    def get_embed_and_head(self):
+        return self.model.embed_tokens.weight, self.lm_head.weight
+    def set_embed_and_head(self, embed, head):
+        del self.model.embed_tokens.weight
+        del self.lm_head.weight
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h_mtp.py` added +340/-0; `python/sglang/srt/models/nemotron_h.py` modified +28/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16569 - [NemotronH] Use ReplicatedLinear for fc1_latent_proj

- 链接: https://github.com/sgl-project/sglang/pull/16569
- 状态/时间: merged / 2026-01-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `72bacc88c8a0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-2，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NemotronH] Use ReplicatedLinear for fc1_latent_proj」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[NemotronH] Use ReplicatedLinear for fc1_latent_proj」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +1/-2 (3 lines); hunks: -191,12 +191,11 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +1/-2 (3 lines); hunks: -191,12 +191,11 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -191,12 +191,11 @@ def __init__(
-            self.fc1_latent_proj = ColumnParallelLinear(
+            self.fc1_latent_proj = ReplicatedLinear(
-                gather_output=True,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +1/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18546 - [Quantization] Support config.json quantization_config format, fix exclude_modules matching, and fix KV cache scale loading for Nemotron

- 链接: https://github.com/sgl-project/sglang/pull/18546
- 状态/时间: merged / 2026-02-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `33c33a7de9bb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+100/-71，可读 patch 251 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Quantization] Support config.json quantization_config format, fix exclude_modules matching, and fix KV cache scale loading for Nemotron」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Quantization] Support config.json quantization_config format, fix exclude_modules matching, and fix KV cache scale loading for Nemotron」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +7/-0 (7 lines); hunks: -61,6 +61,7; -640,6 +641,12 @@ class NemotronHForCausalLM(nn.Module):; symbols: NemotronHForCausalLM, __init__，涉及 `NemotronHForCausalLM, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +7/-0 (7 lines); hunks: -61,6 +61,7; -640,6 +641,12 @@ class NemotronHForCausalLM(nn.Module):; symbols: NemotronHForCausalLM, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -61,6 +61,7 @@
+from sglang.srt.models.utils import WeightsMapper
@@ -640,6 +641,12 @@ class NemotronHForCausalLM(nn.Module):
+    hf_to_sglang_mapper = WeightsMapper(
+        orig_to_new_prefix={
+            "backbone.": "model.",
+        }
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19433 - Fix/nemotron mtp quantaized

- 链接: https://github.com/sgl-project/sglang/pull/19433
- 状态/时间: merged / 2026-03-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h_mtp.py`；关联提交 `4c95953b7733`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+73/-3，可读 patch 117 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix/nemotron mtp quantaized」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「Fix/nemotron mtp quantaized」；主要实现面是 `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-1 (2 lines); hunks: -297,7 +297,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-1 (2 lines); hunks: -297,7 +297,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -297,7 +297,7 @@ def __init__(
-            prefix=add_prefix("model", prefix),
+            prefix=add_prefix("mtp", prefix),
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/registered/model_loading/test_modelopt_loader.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #19950 - Refactor NemotronHConfig to canonical layers_block_type and add MTP block-type support

- 链接: https://github.com/sgl-project/sglang/pull/19950
- 状态/时间: merged / 2026-03-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nemotron_h.py`；关联提交 `f8bbf56de7b2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+182/-17，可读 patch 281 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Refactor NemotronHConfig to canonical layers_block_type and add MTP block-type support」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/configs/nemotron_h.py`；技术摘要: 覆盖「Refactor NemotronHConfig to canonical layers_block_type and add MTP block-type support」；主要实现面是 `python/sglang/srt/configs/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/configs/nemotron_h.py` modified +182/-17 (199 lines); hunks: -15,7 +15,6; -31,6 +30,8; symbols: NemotronHConfig, _validate_layers_block_type, _resolve_layers_block_type，涉及 `NemotronHConfig, _validate_layers_block_type, _resolve_layers_block_type`。
- 代码 diff 细节:
  - `python/sglang/srt/configs/nemotron_h.py` modified +182/-17 (199 lines); hunks: -15,7 +15,6; -31,6 +30,8; symbols: NemotronHConfig, _validate_layers_block_type, _resolve_layers_block_type
- 关键代码摘录:

```diff
diff -- python/sglang/srt/configs/nemotron_h.py
@@ -15,7 +15,6 @@
-import regex as re
@@ -31,6 +30,8 @@
+DEFAULT_LAYERS_BLOCK_TYPE = ["mamba", "moe", "attention", "moe"]
+DEFAULT_MTP_LAYERS_BLOCK_TYPE = ["attention", "moe"]
@@ -53,13 +54,17 @@ class NemotronHConfig(PretrainedConfig):
-        num_hidden_layers (`int`, *optional*, defaults to 52):
```

- 已读文件:
  - runtime: `python/sglang/srt/configs/nemotron_h.py` modified +182/-17
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19903 - Enable Piecewise CUDA Graph for NemotronH Hybrid (Mamba+Attention) Models

- 链接: https://github.com/sgl-project/sglang/pull/19903
- 状态/时间: merged / 2026-03-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `25bd83033d09`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+91/-24，可读 patch 188 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable Piecewise CUDA Graph for NemotronH Hybrid (Mamba+Attention) Models」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Enable Piecewise CUDA Graph for NemotronH Hybrid (Mamba+Attention) Models」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +70/-18 (88 lines); hunks: -21,6 +21,11; -69,6 +74,7; symbols: _forward_core, __init__, _forward_mamba, forward，涉及 `_forward_core, __init__, _forward_mamba`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +70/-18 (88 lines); hunks: -21,6 +21,11; -69,6 +74,7; symbols: _forward_core, __init__, _forward_mamba, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -21,6 +21,11 @@
+from sglang.srt.compilation.compilation_config import register_split_op
+from sglang.srt.compilation.piecewise_context_manager import (
+    get_forward_context,
+    is_in_piecewise_cuda_graph,
+)
@@ -69,6 +74,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +70/-18
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20458 - fix: Nemotron chunk size alias

- 链接: https://github.com/sgl-project/sglang/pull/20458
- 状态/时间: merged / 2026-03-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nemotron_h.py`；关联提交 `1ac6a2646437`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+26/-1，可读 patch 55 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: Nemotron chunk size alias」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/configs/nemotron_h.py`；技术摘要: 覆盖「fix: Nemotron chunk size alias」；主要实现面是 `python/sglang/srt/configs/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/configs/nemotron_h.py` modified +26/-1 (27 lines); hunks: -32,6 +32,7; -213,6 +214,28 @@ def _resolve_mtp_layers_block_type(mtp_layers_block_type, k...; symbols: NemotronHConfig, _resolve_mtp_layers_block_type, _resolve_mamba_chunk_size, __init__，涉及 `NemotronHConfig, _resolve_mtp_layers_block_type, _resolve_mamba_chunk_size`。
- 代码 diff 细节:
  - `python/sglang/srt/configs/nemotron_h.py` modified +26/-1 (27 lines); hunks: -32,6 +32,7; -213,6 +214,28 @@ def _resolve_mtp_layers_block_type(mtp_layers_block_type, k...; symbols: NemotronHConfig, _resolve_mtp_layers_block_type, _resolve_mamba_chunk_size, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/configs/nemotron_h.py
@@ -32,6 +32,7 @@
+DEFAULT_MAMBA_CHUNK_SIZE = 256
@@ -213,6 +214,28 @@ def _resolve_mtp_layers_block_type(mtp_layers_block_type, kwargs) -> list[str]:
+    @staticmethod
+    def _resolve_mamba_chunk_size(mamba_chunk_size, kwargs) -> int:
+        """Resolve canonical mamba_chunk_size from new and legacy config fields."""
+        chunk_size = kwargs.pop("chunk_size", None)
```

- 已读文件:
  - runtime: `python/sglang/srt/configs/nemotron_h.py` modified +26/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #20580 - [Model] Fix NemotronH OOM on unified-mem systems: stream weights

- 链接: https://github.com/sgl-project/sglang/pull/20580
- 状态/时间: merged / 2026-03-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `466ff20e5148`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+7/-7，可读 patch 28 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Fix NemotronH OOM on unified-mem systems: stream weights」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Model] Fix NemotronH OOM on unified-mem systems: stream weights」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +7/-7 (14 lines); hunks: -774,12 +774,6 @@ def set_embed_and_head(self, embed, head):; -793,7 +787,13 @@ def load_weights(; symbols: set_embed_and_head, load_weights，涉及 `set_embed_and_head, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +7/-7 (14 lines); hunks: -774,12 +774,6 @@ def set_embed_and_head(self, embed, head):; -793,7 +787,13 @@ def load_weights(; symbols: set_embed_and_head, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -774,12 +774,6 @@ def set_embed_and_head(self, embed, head):
-        updated_weights = []
-        for name, loaded_weight in weights:
-            name = replace_prefix(name, self.remap_prefix)
-            name = replace_substrings(name, self.remap_substr)
-            updated_weights.append((name, loaded_weight))
@@ -793,7 +787,13 @@ def load_weights(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +7/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23568 - Parakeet nemotron encoder

- 链接: https://github.com/sgl-project/sglang/pull/23568
- 状态/时间: merged / 2026-04-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`；关联提交 `4a3fe2a0913c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+1289/-116，可读 patch 1817 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Parakeet nemotron encoder」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`；技术摘要: 覆盖「Parakeet nemotron encoder」；主要实现面是 `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +322/-36 (358 lines); hunks: -11,23 +11,39; -63,18 +79,62 @@ def __init__(self, hf_config, server_args, _image_processor,...; symbols: __init__, preprocess_image, render_image, render_image_dynamic，涉及 `__init__, preprocess_image, render_image`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +171/-20 (191 lines); hunks: -35,8 +35,10; -66,9 +68,13 @@ def __init__(; symbols: __init__, pad_input_ids, pixel_shuffle，涉及 `__init__, pad_input_ids, pixel_shuffle`；`python/sglang/srt/configs/nano_nemotron_vl.py` modified +38/-0 (38 lines); hunks: -38,6 +38,7 @@ def __init__(; -51,6 +52,9 @@ def __init__(; symbols: __init__, create_radio_config，涉及 `__init__, create_radio_config`。
- 代码 diff 细节:
  - `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +322/-36 (358 lines); hunks: -11,23 +11,39; -63,18 +79,62 @@ def __init__(self, hf_config, server_args, _image_processor,...; symbols: __init__, preprocess_image, render_image, render_image_dynamic
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +171/-20 (191 lines); hunks: -35,8 +35,10; -66,9 +68,13 @@ def __init__(; symbols: __init__, pad_input_ids, pixel_shuffle
  - `python/sglang/srt/configs/nano_nemotron_vl.py` modified +38/-0 (38 lines); hunks: -38,6 +38,7 @@ def __init__(; -51,6 +52,9 @@ def __init__(; symbols: __init__, create_radio_config
- 关键代码摘录:

```diff
diff -- python/sglang/srt/multimodal/processors/nano_nemotron_vl.py
@@ -11,23 +11,39 @@
+import logging
+import math
-from sglang.srt.managers.schedule_batch import MultimodalProcessorOutput
+from sglang.srt.managers.schedule_batch import (
+    Modality,
+    MultimodalDataItem,
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -35,8 +35,10 @@
+from sglang.srt.models.parakeet import ProjectedParakeet
+from sglang.srt.multimodal.evs.evs_module import VideoEVSDataItem
@@ -66,9 +68,13 @@ def __init__(
-        self.rmsnorm_hidden_size = vit_hidden_size * int(1 / self.downsample_ratio) ** 2
+        self.rmsnorm_hidden_size = (
+            vit_hidden_size * int(round(1 / self.downsample_ratio)) ** 2
diff -- python/sglang/srt/configs/nano_nemotron_vl.py
@@ -38,6 +38,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +322/-36; `python/sglang/srt/models/nano_nemotron_vl.py` modified +171/-20; `python/sglang/srt/configs/nano_nemotron_vl.py` modified +38/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/configs/parakeet.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23874 - Fix failing `test_nvidia_nemotron_3_nano` by fixing `test_grouped_topk`

- 链接: https://github.com/sgl-project/sglang/pull/23874
- 状态/时间: merged / 2026-04-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `ddcacaf1bd4e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+223/-19，可读 patch 282 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix failing `test_nvidia_nemotron_3_nano` by fixing `test_grouped_topk`」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Fix failing `test_nvidia_nemotron_3_nano` by fixing `test_grouped_topk`」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +2/-0 (2 lines); hunks: -923,6 +923,8 @@ def nemotron_mamba2_with_output(; symbols: nemotron_mamba2_with_output，涉及 `nemotron_mamba2_with_output`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +2/-0 (2 lines); hunks: -923,6 +923,8 @@ def nemotron_mamba2_with_output(; symbols: nemotron_mamba2_with_output
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -923,6 +923,8 @@ def nemotron_mamba2_with_output(
+    if output.shape[0] != num_actual_tokens:
+        output[num_actual_tokens:].zero_()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +2/-0
- 验证与风险: diff 自带测试面 `python/sglang/jit_kernel/tests/test_grouped_topk.py`, `test/registered/models/test_nvidia_nemotron_3_nano.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23857 - Nemotron-omni-v3-alias

- 链接: https://github.com/sgl-project/sglang/pull/23857
- 状态/时间: merged / 2026-04-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`；关联提交 `b437f6be48a1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+36/-6，可读 patch 111 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Nemotron-omni-v3-alias」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`；技术摘要: 覆盖「Nemotron-omni-v3-alias」；主要实现面是 `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +14/-4 (18 lines); hunks: -19,13 +19,19; -51,15 +57,19; symbols: NanoNemotronVLImageProcessor, __init__，涉及 `NanoNemotronVLImageProcessor, __init__`；`python/sglang/srt/configs/nano_nemotron_vl.py` modified +9/-0 (9 lines); hunks: -150,3 +150,12 @@ def create_radio_config(self):; symbols: create_radio_config, NemotronH_Nano_Omni_Reasoning_V3_Config, __init__，涉及 `create_radio_config, NemotronH_Nano_Omni_Reasoning_V3_Config, __init__`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +5/-1 (6 lines); hunks: -372,4 +372,8 @@ def is_sound_weights(name: str) -> bool:; symbols: is_sound_weights, NemotronH_Nano_Omni_Reasoning_V3，涉及 `is_sound_weights, NemotronH_Nano_Omni_Reasoning_V3`。
- 代码 diff 细节:
  - `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +14/-4 (18 lines); hunks: -19,13 +19,19; -51,15 +57,19; symbols: NanoNemotronVLImageProcessor, __init__
  - `python/sglang/srt/configs/nano_nemotron_vl.py` modified +9/-0 (9 lines); hunks: -150,3 +150,12 @@ def create_radio_config(self):; symbols: create_radio_config, NemotronH_Nano_Omni_Reasoning_V3_Config, __init__
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +5/-1 (6 lines); hunks: -372,4 +372,8 @@ def is_sound_weights(name: str) -> bool:; symbols: is_sound_weights, NemotronH_Nano_Omni_Reasoning_V3
- 关键代码摘录:

```diff
diff -- python/sglang/srt/multimodal/processors/nano_nemotron_vl.py
@@ -19,13 +19,19 @@
-from sglang.srt.configs.nano_nemotron_vl import NemotronH_Nano_VL_V2_Config
+from sglang.srt.configs.nano_nemotron_vl import (
+    NemotronH_Nano_Omni_Reasoning_V3_Config,
+    NemotronH_Nano_VL_V2_Config,
+)
-from sglang.srt.models.nano_nemotron_vl import NemotronH_Nano_VL_V2
diff -- python/sglang/srt/configs/nano_nemotron_vl.py
@@ -150,3 +150,12 @@ def create_radio_config(self):
+class NemotronH_Nano_Omni_Reasoning_V3_Config(NemotronH_Nano_VL_V2_Config):
+    model_type = "NemotronH_Nano_Omni_Reasoning_V3"
+    def __init__(self, *args, **kwargs):
+        # Explicit __init__ prevents PretrainedConfig.__init_subclass__ from
+        # replacing the parent's custom __init__ with a dataclass-generated one.
+        super().__init__(*args, **kwargs)
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -372,4 +372,8 @@ def is_sound_weights(name: str) -> bool:
```

- 已读文件:
  - runtime: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +14/-4; `python/sglang/srt/configs/nano_nemotron_vl.py` modified +9/-0; `python/sglang/srt/models/nano_nemotron_vl.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21321 - [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron)

- 链接: https://github.com/sgl-project/sglang/pull/21321
- 状态/时间: merged / 2026-04-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `8327270c7263`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+341/-53，可读 patch 758 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron)」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron)」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +2/-0 (2 lines); hunks: -51,6 +51,7; -190,6 +191,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +2/-0 (2 lines); hunks: -51,6 +51,7; -190,6 +191,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -51,6 +51,7 @@
+from sglang.srt.layers.moe.utils import RoutingMethodType
@@ -190,6 +191,7 @@ def __init__(
+            routing_method_type=RoutingMethodType.DeepSeekV3,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23594 - LoRA support for qwen3.5 and nemotron3

- 链接: https://github.com/sgl-project/sglang/pull/23594
- 状态/时间: merged / 2026-04-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py`；关联提交 `c8c1c9261d72`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 21 个文件，+1131/-127，可读 patch 1734 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「LoRA support for qwen3.5 and nemotron3」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py`；技术摘要: 覆盖「LoRA support for qwen3.5 and nemotron3」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +105/-0 (105 lines); hunks: -665,6 +665,17 @@ class NemotronHForCausalLM(nn.Module):; -748,6 +759,100 @@ def _init_model(; symbols: NemotronHForCausalLM, _init_model, get_input_embeddings, get_stacked_multiply，涉及 `NemotronHForCausalLM, _init_model, get_input_embeddings`；`test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py` added +154/-0 (154 lines); hunks: -0,0 +1,154; symbols: kl_v2, get_prompt_logprobs, TestLoRANemotron3Super120B_A12B_LogprobDiff, test_lora_nemotron_3_super_120b_a12b_logprob_accuracy，涉及 `kl_v2, get_prompt_logprobs, TestLoRANemotron3Super120B_A12B_LogprobDiff`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +105/-0 (105 lines); hunks: -665,6 +665,17 @@ class NemotronHForCausalLM(nn.Module):; -748,6 +759,100 @@ def _init_model(; symbols: NemotronHForCausalLM, _init_model, get_input_embeddings, get_stacked_multiply
  - `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py` added +154/-0 (154 lines); hunks: -0,0 +1,154; symbols: kl_v2, get_prompt_logprobs, TestLoRANemotron3Super120B_A12B_LogprobDiff, test_lora_nemotron_3_super_120b_a12b_logprob_accuracy
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -665,6 +665,17 @@ class NemotronHForCausalLM(nn.Module):
+    supported_lora_modules = [
+        "qkv_proj",
+        "o_proj",
+        "out_proj",
+        "in_proj",
+        "up_proj",
diff -- test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py
@@ -0,0 +1,154 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +105/-0
  - tests: `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py` added +154/-0
- 验证与风险: diff 自带测试面 `test/registered/lora/test_chunked_sgmv_backend.py`, `test/registered/lora/test_lora_nemotron_3_super_120b_a12b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_5_4b_logprob_diff.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #24434 - [NemotronH] Fix expert scale weight loading

- 链接: https://github.com/sgl-project/sglang/pull/24434
- 状态/时间: merged / 2026-05-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nemotron_h_weight_loading.py`；关联提交 `672f778512bc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+89/-0，可读 patch 97 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NemotronH] Fix expert scale weight loading」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_nemotron_h_weight_loading.py`, `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[NemotronH] Fix expert scale weight loading」；主要实现面是 `test/registered/unit/models/test_nemotron_h_weight_loading.py`, `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_nemotron_h_weight_loading.py` added +87/-0 (87 lines); hunks: -0,0 +1,87; symbols: _FakePPGroup, _FakeParam, __init__, weight_loader，涉及 `_FakePPGroup, _FakeParam, __init__`；`python/sglang/srt/models/nemotron_h.py` modified +2/-0 (2 lines); hunks: -972,6 +972,8 @@ def load_weights(; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_nemotron_h_weight_loading.py` added +87/-0 (87 lines); hunks: -0,0 +1,87; symbols: _FakePPGroup, _FakeParam, __init__, weight_loader
  - `python/sglang/srt/models/nemotron_h.py` modified +2/-0 (2 lines); hunks: -972,6 +972,8 @@ def load_weights(; symbols: load_weights
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_nemotron_h_weight_loading.py
@@ -0,0 +1,87 @@
+"""
+Unit tests for NemotronHForCausalLM.load_weights.
+Regression test for Nemotron-H expert scale checkpoint tensors that map to
+parameters absent from the current runtime model.
+"""
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/models/nemotron_h.py
@@ -972,6 +972,8 @@ def load_weights(
+                    if name_mapped not in params_dict:
+                        continue
```

- 已读文件:
  - tests: `test/registered/unit/models/test_nemotron_h_weight_loading.py` added +87/-0
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +2/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_nemotron_h_weight_loading.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25023 - [NemotronH] V3 Omni wrapper: WeightsMapper + config round-trip

- 链接: https://github.com/sgl-project/sglang/pull/25023
- 状态/时间: merged / 2026-05-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`；关联提交 `499eecce22ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+17/-0，可读 patch 38 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NemotronH] V3 Omni wrapper: WeightsMapper + config round-trip」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`；技术摘要: 覆盖「[NemotronH] V3 Omni wrapper: WeightsMapper + config round-trip」；主要实现面是 `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nano_nemotron_vl.py` modified +10/-0 (10 lines); hunks: -39,6 +39,7; -47,6 +48,15; symbols: NemotronH_Nano_VL_V2, when, create_evs_config，涉及 `NemotronH_Nano_VL_V2, when, create_evs_config`；`python/sglang/srt/configs/nano_nemotron_vl.py` modified +7/-0 (7 lines); hunks: -60,6 +60,13 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +10/-0 (10 lines); hunks: -39,6 +39,7; -47,6 +48,15; symbols: NemotronH_Nano_VL_V2, when, create_evs_config
  - `python/sglang/srt/configs/nano_nemotron_vl.py` modified +7/-0 (7 lines); hunks: -60,6 +60,13 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -39,6 +39,7 @@
+from sglang.srt.models.utils import WeightsMapper
@@ -47,6 +48,15 @@
+    # The loader reads `hf_to_sglang_mapper` off the outer model class when
+    # applying name rewrites to the quant config's `quantized_layers` keys;
+    # the inner NemotronHForCausalLM mapper is not consulted there.
+    hf_to_sglang_mapper = WeightsMapper(
diff -- python/sglang/srt/configs/nano_nemotron_vl.py
@@ -60,6 +60,13 @@ def __init__(
+        # Round-trip: `to_dict()` emits `raw_vision_config` (V2's storage
+        # name) but `from_dict()` rebuilds via this `vision_config` kwarg.
+        # Without this alias, the V3->V2 alias rebuild in `get_config` loses
+        # the vision config across the round-trip.
+        if vision_config is None:
+            vision_config = kwargs.pop("raw_vision_config", None)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nano_nemotron_vl.py` modified +10/-0; `python/sglang/srt/configs/nano_nemotron_vl.py` modified +7/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24429 - Support NemotronHPuzzleForCausalLM

- 链接: https://github.com/sgl-project/sglang/pull/24429
- 状态/时间: merged / 2026-05-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`；关联提交 `0abe6a85a51f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+74/-7，可读 patch 187 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support NemotronHPuzzleForCausalLM」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「Support NemotronHPuzzleForCausalLM」；主要实现面是 `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/configs/nemotron_h.py` modified +53/-0 (53 lines); hunks: -17,6 +17,9; -240,6 +243,7 @@ def _resolve_mamba_chunk_size(mamba_chunk_size, kwargs) -> int:; symbols: _resolve_mamba_chunk_size, __init__, _pattern_to_list, get_nemotron_h_config_for_layer，涉及 `_resolve_mamba_chunk_size, __init__, _pattern_to_list`；`python/sglang/srt/models/nemotron_h.py` modified +11/-4 (15 lines); hunks: -358,9 +358,10 @@ def __init__(; -510,6 +511,7 @@ def __init__(; symbols: __init__, load_weights，涉及 `__init__, load_weights`；`python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-0 (1 lines); hunks: -283,6 +283,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/configs/nemotron_h.py` modified +53/-0 (53 lines); hunks: -17,6 +17,9; -240,6 +243,7 @@ def _resolve_mamba_chunk_size(mamba_chunk_size, kwargs) -> int:; symbols: _resolve_mamba_chunk_size, __init__, _pattern_to_list, get_nemotron_h_config_for_layer
  - `python/sglang/srt/models/nemotron_h.py` modified +11/-4 (15 lines); hunks: -358,9 +358,10 @@ def __init__(; -510,6 +511,7 @@ def __init__(; symbols: __init__, load_weights
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-0 (1 lines); hunks: -283,6 +283,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/configs/nemotron_h.py
@@ -17,6 +17,9 @@
+import copy
+from typing import Any
@@ -240,6 +243,7 @@ def _resolve_mamba_chunk_size(mamba_chunk_size, kwargs) -> int:
+        *,
@@ -504,3 +508,52 @@ def _pattern_to_list(pattern: str) -> list[str]:
+    def get_nemotron_h_config_for_layer(self, layer_idx: int) -> "NemotronHConfig":
diff -- python/sglang/srt/models/nemotron_h.py
@@ -358,9 +358,10 @@ def __init__(
+        layer_config = config.get_nemotron_h_config_for_layer(layer_idx)
-            config,
+            layer_config,
@@ -510,6 +511,7 @@ def __init__(
+            sliding_window_size=config.sliding_window,
@@ -533,9 +535,10 @@ def __init__(
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -283,6 +283,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/configs/nemotron_h.py` modified +53/-0; `python/sglang/srt/models/nemotron_h.py` modified +11/-4; `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26522 - [NemotronH] Fix weight-loading unit test broken by Puzzle support

- 链接: https://github.com/sgl-project/sglang/pull/26522
- 状态/时间: merged / 2026-05-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/unit/models/test_nemotron_h_weight_loading.py`；关联提交 `68e5b4fdd66b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NemotronH] Fix weight-loading unit test broken by Puzzle support」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_nemotron_h_weight_loading.py`；技术摘要: 覆盖「[NemotronH] Fix weight-loading unit test broken by Puzzle support」；主要实现面是 `test/registered/unit/models/test_nemotron_h_weight_loading.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +1/-1 (2 lines); hunks: -35,7 +35,7 @@ def weight_loader(; symbols: weight_loader, TestNemotronHWeightLoading, _make_minimal_model，涉及 `weight_loader, TestNemotronHWeightLoading, _make_minimal_model`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +1/-1 (2 lines); hunks: -35,7 +35,7 @@ def weight_loader(; symbols: weight_loader, TestNemotronHWeightLoading, _make_minimal_model
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_nemotron_h_weight_loading.py
@@ -35,7 +35,7 @@ def weight_loader(
-        model.config = SimpleNamespace(n_routed_experts=2)
+        model.config = SimpleNamespace(n_routed_experts=2, max_n_routed_experts=2)
```

- 已读文件:
  - tests: `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_nemotron_h_weight_loading.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26733 - Nemotron perf changes

- 链接: https://github.com/sgl-project/sglang/pull/26733
- 状态/时间: merged / 2026-06-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `38ae22e08c73`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+297/-58，可读 patch 713 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Nemotron perf changes」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Nemotron perf changes」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +25/-25 (50 lines); hunks: -164,24 +164,13 @@ def __init__(; -195,6 +184,18 @@ def __init__(; symbols: __init__, _forward_core_normal, _forward_core_shared_routed_overlap，涉及 `__init__, _forward_core_normal, _forward_core_shared_routed_overlap`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +25/-25 (50 lines); hunks: -164,24 +164,13 @@ def __init__(; -195,6 +184,18 @@ def __init__(; symbols: __init__, _forward_core_normal, _forward_core_shared_routed_overlap
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -164,24 +164,13 @@ def __init__(
-            params_dtype=torch.float32,
-        self.topk = TopK(
-            top_k=config.num_experts_per_tok,
-            use_grouped_topk=True,
-            topk_group=config.topk_group,
-            num_expert_group=config.n_group,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +25/-25
- 验证与风险: diff 自带测试面 `python/sglang/jit_kernel/tests/test_activation.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #24955 - Support Nemotron DP attention and MTP

- 链接: https://github.com/sgl-project/sglang/pull/24955
- 状态/时间: merged / 2026-06-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h_utils.py`；关联提交 `6e0fa5afe1c6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+472/-95，可读 patch 1135 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support Nemotron DP attention and MTP」；模型线: Nemotron Super；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「Support Nemotron DP attention and MTP」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +139/-35 (174 lines); hunks: -42,6 +42,12; -76,6 +82,12; symbols: forward, NemotronHMLPDecoderLayer, NemotronHMLPLikeDecoderLayer，涉及 `forward, NemotronHMLPDecoderLayer, NemotronHMLPLikeDecoderLayer`；`python/sglang/srt/models/nemotron_h_utils.py` added +67/-0 (67 lines); hunks: -0,0 +1,67; symbols: is_attn_layer, get_real_num_tokens, pad_to_original_num_tokens, _build_layer_scatter_modes，涉及 `is_attn_layer, get_real_num_tokens, pad_to_original_num_tokens`；`python/sglang/srt/models/nemotron_h_mtp.py` modified +37/-3 (40 lines); hunks: -19,6 +19,13; -33,6 +40,7; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +139/-35 (174 lines); hunks: -42,6 +42,12; -76,6 +82,12; symbols: forward, NemotronHMLPDecoderLayer, NemotronHMLPLikeDecoderLayer
  - `python/sglang/srt/models/nemotron_h_utils.py` added +67/-0 (67 lines); hunks: -0,0 +1,67; symbols: is_attn_layer, get_real_num_tokens, pad_to_original_num_tokens, _build_layer_scatter_modes
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +37/-3 (40 lines); hunks: -19,6 +19,13; -33,6 +40,7; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -42,6 +42,12 @@
+from sglang.srt.layers.dp_attention import (
+    attn_tp_all_reduce,
+    get_attention_tp_rank,
+    get_attention_tp_size,
+    is_dp_attention_enabled,
+)
diff -- python/sglang/srt/models/nemotron_h_utils.py
@@ -0,0 +1,67 @@
+"""DP-attention helpers for the Nemotron-H model."""
+import torch
+from torch import nn
+from sglang.srt.configs.nemotron_h import ATTENTION, MAMBA
+from sglang.srt.layers.communicator import (
+    LayerCommunicator,
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -19,6 +19,13 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +139/-35; `python/sglang/srt/models/nemotron_h_utils.py` added +67/-0; `python/sglang/srt/models/nemotron_h_mtp.py` modified +37/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28102 - Fix DP attention + EP mode of Nemotron

- 链接: https://github.com/sgl-project/sglang/pull/28102
- 状态/时间: merged / 2026-06-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`；关联提交 `1a19f66acbf2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+27/-9，可读 patch 98 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix DP attention + EP mode of Nemotron」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`；技术摘要: 覆盖「Fix DP attention + EP mode of Nemotron」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +25/-8 (33 lines); hunks: -55,7 +55,10; -129,10 +132,10 @@ def __init__(; symbols: __init__, forward, _forward_core_shared_routed_overlap，涉及 `__init__, forward, _forward_core_shared_routed_overlap`；`python/sglang/srt/models/nemotron_h_utils.py` modified +2/-1 (3 lines); hunks: -57,11 +57,12 @@ def _build_layer_scatter_modes() -> LayerScatterModes:; symbols: _build_layer_scatter_modes, make_layer_communicator，涉及 `_build_layer_scatter_modes, make_layer_communicator`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +25/-8 (33 lines); hunks: -55,7 +55,10; -129,10 +132,10 @@ def __init__(; symbols: __init__, forward, _forward_core_shared_routed_overlap
  - `python/sglang/srt/models/nemotron_h_utils.py` modified +2/-1 (3 lines); hunks: -57,11 +57,12 @@ def _build_layer_scatter_modes() -> LayerScatterModes:; symbols: _build_layer_scatter_modes, make_layer_communicator
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -55,7 +55,10 @@
-from sglang.srt.layers.moe.utils import RoutingMethodType
+from sglang.srt.layers.moe.utils import (
+    RoutingMethodType,
+    should_skip_post_experts_all_reduce,
+)
@@ -129,10 +132,10 @@ def __init__(
diff -- python/sglang/srt/models/nemotron_h_utils.py
@@ -57,11 +57,12 @@ def _build_layer_scatter_modes() -> LayerScatterModes:
-    layer_norm: RMSNorm, *, for_attn: bool
+    layer_norm: RMSNorm, *, for_attn: bool, allow_reduce_scatter: bool = False
+        allow_reduce_scatter=allow_reduce_scatter,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +25/-8; `python/sglang/srt/models/nemotron_h_utils.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28346 - Use Flashinfer allreduce fusion for MNNVL allreduce for Nemotron

- 链接: https://github.com/sgl-project/sglang/pull/28346
- 状态/时间: merged / 2026-06-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h_utils.py`；关联提交 `ea407df4b023`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+111/-47，可读 patch 385 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Use Flashinfer allreduce fusion for MNNVL allreduce for Nemotron」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「Use Flashinfer allreduce fusion for MNNVL allreduce for Nemotron」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +76/-46 (122 lines); hunks: -18,7 +18,6; -85,6 +84,7; symbols: __init__, forward，涉及 `__init__, forward`；`python/sglang/srt/models/nemotron_h_utils.py` modified +32/-1 (33 lines); hunks: -4,10 +4,12; -57,12 +59,41 @@ def _build_layer_scatter_modes() -> LayerScatterModes:; symbols: _build_layer_scatter_modes, make_layer_communicator, input_norm_maybe_fuse_allreduce，涉及 `_build_layer_scatter_modes, make_layer_communicator, input_norm_maybe_fuse_allreduce`；`python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-0 (1 lines); hunks: -148,6 +148,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +76/-46 (122 lines); hunks: -18,7 +18,6; -85,6 +84,7; symbols: __init__, forward
  - `python/sglang/srt/models/nemotron_h_utils.py` modified +32/-1 (33 lines); hunks: -4,10 +4,12; -57,12 +59,41 @@ def _build_layer_scatter_modes() -> LayerScatterModes:; symbols: _build_layer_scatter_modes, make_layer_communicator, input_norm_maybe_fuse_allreduce
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-0 (1 lines); hunks: -148,6 +148,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -18,7 +18,6 @@
-from typing import Optional, Union
@@ -85,6 +84,7 @@
+    input_norm_maybe_fuse_allreduce,
@@ -108,7 +108,7 @@ def __init__(
-        quant_config: Optional[QuantizationConfig] = None,
+        quant_config: QuantizationConfig | None = None,
diff -- python/sglang/srt/models/nemotron_h_utils.py
@@ -4,10 +4,12 @@
+from sglang.srt.distributed import tensor_model_parallel_all_reduce
+    apply_flashinfer_allreduce_fusion,
@@ -57,12 +59,41 @@ def _build_layer_scatter_modes() -> LayerScatterModes:
-    layer_norm: RMSNorm, *, for_attn: bool, allow_reduce_scatter: bool = False
+    layer_norm: RMSNorm,
+    *,
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -148,6 +148,7 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +76/-46; `python/sglang/srt/models/nemotron_h_utils.py` modified +32/-1; `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h_utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30968 - [Bugfix] Fix Nemotron ForwardFlags across custom op boundary

- 链接: https://github.com/sgl-project/sglang/pull/30968
- 状态/时间: merged / 2026-07-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `cbcbef6811c6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-8，可读 patch 50 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Nemotron ForwardFlags across custom op boundary」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Bugfix] Fix Nemotron ForwardFlags across custom op boundary」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +11/-3 (14 lines); hunks: -550,11 +550,13 @@ def forward(; -1189,6 +1191,7 @@ def nemotron_mamba2_with_output(; symbols: forward, nemotron_mamba2_with_output，涉及 `forward, nemotron_mamba2_with_output`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +11/-3 (14 lines); hunks: -550,11 +550,13 @@ def forward(; -1189,6 +1191,7 @@ def nemotron_mamba2_with_output(; symbols: forward, nemotron_mamba2_with_output
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -550,11 +550,13 @@ def forward(
-                    hidden_states, output, self.layer_id
+                    hidden_states, output, self.layer_id, fuse_mlp_allreduce
-                nemotron_mamba2_with_output(hidden_states, output, self.layer_id)
+                nemotron_mamba2_with_output(
+                    hidden_states, output, self.layer_id, fuse_mlp_allreduce
+                )
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +11/-3
- 验证与风险: diff 自带测试面 `test/registered/models_e2e/test_nvidia_nemotron_3_nano.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29692 - Use fused A GEMM for `fc1_latent_proj` in NemotronH

- 链接: https://github.com/sgl-project/sglang/pull/29692
- 状态/时间: merged / 2026-07-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `0b04e9da83db`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+70/-38，可读 patch 191 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Use fused A GEMM for `fc1_latent_proj` in NemotronH」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Use fused A GEMM for `fc1_latent_proj` in NemotronH」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +20/-2 (22 lines); hunks: -99,6 +99,12; -245,6 +251,18 @@ def __init__(; symbols: NemotronHMLP, __init__, _apply_fc1_latent_proj, _forward_core，涉及 `NemotronHMLP, __init__, _apply_fc1_latent_proj`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +20/-2 (22 lines); hunks: -99,6 +99,12; -245,6 +251,18 @@ def __init__(; symbols: NemotronHMLP, __init__, _apply_fc1_latent_proj, _forward_core
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -99,6 +99,12 @@
+if _is_cuda:
+    from sglang.jit_kernel.fused_a_gemm import (
+        fused_a_gemm_weight_eligible,
+        linear_with_fused_a_gemm,
+    )
@@ -245,6 +251,18 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +20/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/jit_kernel/fused_a_gemm.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28309 - Support Flashinfer one-sided A2A + CuteDSL MoE for Nemotron Ultra

- 链接: https://github.com/sgl-project/sglang/pull/28309
- 状态/时间: merged / 2026-07-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`；关联提交 `edb2059139d4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+92/-33，可读 patch 320 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support Flashinfer one-sided A2A + CuteDSL MoE for Nemotron Ultra」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`；技术摘要: 覆盖「Support Flashinfer one-sided A2A + CuteDSL MoE for Nemotron Ultra」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +24/-8 (32 lines); hunks: -53,6 +53,7; -65,6 +66,7; symbols: __init__, _forward_core，涉及 `__init__, _forward_core`；`python/sglang/srt/models/nemotron_h_utils.py` modified +11/-4 (15 lines); hunks: -12,6 +12,7; -48,12 +49,17 @@ def pad_to_original_num_tokens(; symbols: pad_to_original_num_tokens, _build_layer_scatter_modes, make_layer_communicator，涉及 `pad_to_original_num_tokens, _build_layer_scatter_modes, make_layer_communicator`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +24/-8 (32 lines); hunks: -53,6 +53,7; -65,6 +66,7; symbols: __init__, _forward_core
  - `python/sglang/srt/models/nemotron_h_utils.py` modified +11/-4 (15 lines); hunks: -12,6 +12,7; -48,12 +49,17 @@ def pad_to_original_num_tokens(; symbols: pad_to_original_num_tokens, _build_layer_scatter_modes, make_layer_communicator
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -53,6 +53,7 @@
+    get_moe_a2a_backend,
@@ -65,6 +66,7 @@
+from sglang.srt.model_executor.runner import get_is_capture_mode
@@ -108,6 +110,8 @@ def __init__(
+        tp_rank: int | None = None,
+        tp_size: int | None = None,
diff -- python/sglang/srt/models/nemotron_h_utils.py
@@ -12,6 +12,7 @@
+from sglang.srt.layers.moe.utils import get_moe_a2a_backend
@@ -48,12 +49,17 @@ def pad_to_original_num_tokens(
-def _build_layer_scatter_modes() -> LayerScatterModes:
+def _build_layer_scatter_modes(is_sparse: bool = False) -> LayerScatterModes:
+    scatter_mlp = is_sparse and not get_moe_a2a_backend().is_none()
+    mlp_mode = ScatterMode.SCATTERED if scatter_mlp else ScatterMode.FULL
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +24/-8; `python/sglang/srt/models/nemotron_h_utils.py` modified +11/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30456 - [NemotronH] Load shared embed_tokens/lm_head in MTP draft weights

- 链接: https://github.com/sgl-project/sglang/pull/30456
- 状态/时间: merged / 2026-07-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nemotron_h_weight_loading.py`；关联提交 `1f34911de7be`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+63/-1，可读 patch 85 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NemotronH] Load shared embed_tokens/lm_head in MTP draft weights」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `test/registered/unit/models/test_nemotron_h_weight_loading.py`, `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[NemotronH] Load shared embed_tokens/lm_head in MTP draft weights」；主要实现面是 `test/registered/unit/models/test_nemotron_h_weight_loading.py`, `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +52/-0 (52 lines); hunks: -32,6 +32,17 @@ def weight_loader(; -82,6 +93,47 @@ def test_expert_weight_with_target_parameter_is_loaded(self):; symbols: weight_loader, _RecordingParam, __init__, TestNemotronHWeightLoading，涉及 `weight_loader, _RecordingParam, __init__`；`python/sglang/srt/models/nemotron_h.py` modified +11/-1 (12 lines); hunks: -1091,7 +1091,17 @@ def load_weights(; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +52/-0 (52 lines); hunks: -32,6 +32,17 @@ def weight_loader(; -82,6 +93,47 @@ def test_expert_weight_with_target_parameter_is_loaded(self):; symbols: weight_loader, _RecordingParam, __init__, TestNemotronHWeightLoading
  - `python/sglang/srt/models/nemotron_h.py` modified +11/-1 (12 lines); hunks: -1091,7 +1091,17 @@ def load_weights(; symbols: load_weights
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_nemotron_h_weight_loading.py
@@ -32,6 +32,17 @@ def weight_loader(
+class _RecordingParam:
+    """Param whose weight_loader matches the plain (non-expert) load path:
+    weight_loader(param, loaded_weight)."""
+    def __init__(self):
+        self.loaded_weight = None
+    def weight_loader(self, param, loaded_weight):
diff -- python/sglang/srt/models/nemotron_h.py
@@ -1091,7 +1091,17 @@ def load_weights(
-                if "mtp" not in name:
+                # Keep the MTP draft layers (mtp.layers.*) and the shared
+                # embed_tokens / lm_head weights. The remap above already
+                # rewrote "embeddings" -> "embed_tokens", so the shared draft
+                # weights must be whitelisted by their post-remap names; without
+                # this the draft loads no embedding / head and accepts zero
```

- 已读文件:
  - tests: `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +52/-0
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +11/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_nemotron_h_weight_loading.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33123 - Fix broken Nemotron DP attention

- 链接: https://github.com/sgl-project/sglang/pull/33123
- 状态/时间: merged / 2026-08-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h_mtp.py`；关联提交 `a14c870886bc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+74/-14，可读 patch 186 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix broken Nemotron DP attention」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「Fix broken Nemotron DP attention」；主要实现面是 `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h_mtp.py` modified +3/-4 (7 lines); hunks: -288,13 +288,14 @@ def get_input_embeddings(self, input_ids: torch.Tensor) ->...; -352,11 +353,9 @@ def forward(; symbols: get_input_embeddings, forward，涉及 `get_input_embeddings, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +3/-4 (7 lines); hunks: -288,13 +288,14 @@ def get_input_embeddings(self, input_ids: torch.Tensor) ->...; -352,11 +353,9 @@ def forward(; symbols: get_input_embeddings, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -288,13 +288,14 @@ def get_input_embeddings(self, input_ids: torch.Tensor) -> torch.Tensor:
-        hidden_states: torch.Tensor,
+        positions: torch.Tensor,
+        hidden_states = forward_batch.spec_info.hidden_states
@@ -352,11 +353,9 @@ def forward(
-        hidden_states = forward_batch.spec_info.hidden_states
-            hidden_states,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h_mtp.py` modified +3/-4
- 验证与风险: diff 自带测试面 `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33481 - Add NVIDIA Nemotron 3.5 Lightning cookbook

- 链接: https://github.com/sgl-project/sglang/pull/33481
- 状态/时间: merged / 2026-08-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`；关联提交 `3add7e19ffa1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+537/-1，可读 patch 555 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add NVIDIA Nemotron 3.5 Lightning cookbook」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`；技术摘要: 覆盖「Add NVIDIA Nemotron 3.5 Lightning cookbook」；主要实现面是 `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` added +355/-0 (355 lines); hunks: -0,0 +1,355；`docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx` added +18/-0 (18 lines); hunks: -0,0 +1,18；`docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` added +162/-0 (162 lines); hunks: -0,0 +1,162。
- 代码 diff 细节:
  - `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` added +355/-0 (355 lines); hunks: -0,0 +1,355
  - `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx` added +18/-0 (18 lines); hunks: -0,0 +1,18
  - `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` added +162/-0 (162 lines); hunks: -0,0 +1,162
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx
@@ -0,0 +1,355 @@
+// Single `export const config` literal — no spreads/calls/IIFE (Mintlify re-evals at hydration).
+//
+// `{{MODEL_NAME}}` resolves to `modelNames` below (HF repos under the nvidia org).
+export const config = {
+  modelName: "Nemotron 3.5 Lightning",
+  // Three validated single-GPU platforms, all at TP1/EP1.
diff -- docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx
@@ -0,0 +1,18 @@
+// One entry per cell `match`. Numbers pending — the card renders "pending"
+// until speed/accuracy data is filled in from a measured run.
+export const benchmarks = [
+  { match: { hw: "b200", variant: "default", quant: "nvfp4", strategy: "balanced", nodes: "single" } },
+  { match: { hw: "b200", variant: "default", quant: "nvfp4", strategy: "mtp",      nodes: "single" } },
+  { match: { hw: "b200", variant: "default", quant: "nvfp4", strategy: "dflash",   nodes: "single" } },
diff -- docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx
@@ -0,0 +1,162 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` added +355/-0; `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx` added +18/-0; `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` added +162/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #34573 - docs(cookbook): add BF16 recipes to Nemotron 3.5 Lightning

- 链接: https://github.com/sgl-project/sglang/pull/34573
- 状态/时间: merged / 2026-08-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`；关联提交 `f28bc5a6de37`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+233/-1，可读 patch 254 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「docs(cookbook): add BF16 recipes to Nemotron 3.5 Lightning」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`；技术摘要: 覆盖「docs(cookbook): add BF16 recipes to Nemotron 3.5 Lightning」；主要实现面是 `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` modified +233/-1 (234 lines); hunks: -10,7 +10,7 @@ export const config = {; -24,6 +24,7 @@ export const config = {。
- 代码 diff 细节:
  - `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` modified +233/-1 (234 lines); hunks: -10,7 +10,7 @@ export const config = {; -24,6 +24,7 @@ export const config = {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx
@@ -10,7 +10,7 @@ export const config = {
-  quantizations: [{ id: "nvfp4", label: "NVFP4" }],
+  quantizations: [{ id: "nvfp4", label: "NVFP4" }, { id: "bf16", label: "BF16" }],
@@ -24,6 +24,7 @@ export const config = {
+    "default|bf16": "nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16",
@@ -351,5 +352,236 @@ sgl-eval run gsm8k \\
+    // ==== NVIDIA B200 (SM100) + BF16, single GPU ====
```

- 已读文件:
  - docs: `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx` modified +233/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #34561 - [Fix] Fix Nemotron-H Mamba illegal memory access under DP attention with CUDA graph

- 链接: https://github.com/sgl-project/sglang/pull/34561
- 状态/时间: merged / 2026-08-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `a6bc0532c936`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+10/-3，可读 patch 27 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Fix Nemotron-H Mamba illegal memory access under DP attention with CUDA graph」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Fix] Fix Nemotron-H Mamba illegal memory access under DP attention with CUDA graph」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +10/-1 (11 lines); hunks: -563,7 +563,16 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +10/-1 (11 lines); hunks: -563,7 +563,16 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -563,7 +563,16 @@ def forward(
-            output = self._forward_mamba(hidden_states, forward_batch)
+            if is_in_breakable_cuda_graph():
+                output = torch.empty_like(hidden_states)
+                breakable_nemotron_mamba2_with_output(
+                    hidden_states, output, self.layer_id, False
+                )
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +10/-1
- 验证与风险: diff 自带测试面 `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36186 - [Model] Support Nemotron 3.5 Lightning speculative decoding

- 链接: https://github.com/sgl-project/sglang/pull/36186
- 状态/时间: merged / 2026-08-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `python/sglang/srt/models/nemotron_h.py`；关联提交 `41e7612dee44`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 18 个文件，+792/-122，可读 patch 1556 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Support Nemotron 3.5 Lightning speculative decoding」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`；技术摘要: 覆盖「[Model] Support Nemotron 3.5 Lightning speculative decoding」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +42/-1 (43 lines); hunks: -833,6 +833,7 @@ def get_layer(idx: int, prefix: str):; -853,7 +854,17 @@ def forward(; symbols: get_layer, forward, __init__，涉及 `get_layer, forward, __init__`；`docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` modified +1/-1 (2 lines); hunks: -19,7 +19,7 @@ For all methods and hardware platforms, see the [official SGLa...。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +42/-1 (43 lines); hunks: -833,6 +833,7 @@ def get_layer(idx: int, prefix: str):; -853,7 +854,17 @@ def forward(; symbols: get_layer, forward, __init__
  - `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` modified +1/-1 (2 lines); hunks: -19,7 +19,7 @@ For all methods and hardware platforms, see the [official SGLa...
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -833,6 +833,7 @@ def get_layer(idx: int, prefix: str):
+        self.layers_to_capture: set[int] = set()
@@ -853,7 +854,17 @@ def forward(
+        aux_hidden_states = []
+            if i in self.layers_to_capture:
+                if residual is not None and getattr(
+                    hidden_states, "_sglang_needs_allreduce_fusion", False
diff -- docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx
@@ -19,7 +19,7 @@ For all methods and hardware platforms, see the [official SGLang installation gu
-SGLANG_BUILD_RUST_EXTS=none uv pip install --prerelease=allow 'git+https://github.com/sgl-project/sglang.git@refs/pull/33554/head#subdirectory=python'
+SGLANG_BUILD_RUST_EXTS=none uv pip install --prerelease=allow 'git+https://github.com/sgl-project/sglang.git#subdirectory=python'
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +42/-1
  - docs: `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` modified +1/-1
- 验证与风险: diff 自带测试面 `python/sglang/test/kits/eval_accuracy_kit.py`, `test/registered/models_e2e/test_nvidia_nemotron_3_nano.py`, `test/registered/unit/test_model_overrides.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30430 - Fuse Nemotron latent MoE projection and shared add

- 链接: https://github.com/sgl-project/sglang/pull/30430
- 状态/时间: merged / 2026-09-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nemotron_h_shared_add.py`；关联提交 `214313ee796b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+430/-10，可读 patch 513 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fuse Nemotron latent MoE projection and shared add」；模型线: Nemotron Super；类别: 性能/后端优化；主要 diff: `test/registered/unit/models/test_nemotron_h_shared_add.py`, `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「Fuse Nemotron latent MoE projection and shared add」；主要实现面是 `test/registered/unit/models/test_nemotron_h_shared_add.py`, `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_nemotron_h_shared_add.py` added +127/-0 (127 lines); hunks: -0,0 +1,127; symbols: _DoubleMethod, apply, _FakeLoRABackend, run_lora_a_sgemm，涉及 `_DoubleMethod, apply, _FakeLoRABackend`；`python/sglang/srt/models/nemotron_h.py` modified +32/-3 (35 lines); hunks: -57,6 +57,7; -163,6 +164,17 @@ def _get_or_create_alt_stream(device_module):; symbols: _get_or_create_alt_stream, _latent_proj_fuses_shared_add, NemotronHMoE, __init__，涉及 `_get_or_create_alt_stream, _latent_proj_fuses_shared_add, NemotronHMoE`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_nemotron_h_shared_add.py` added +127/-0 (127 lines); hunks: -0,0 +1,127; symbols: _DoubleMethod, apply, _FakeLoRABackend, run_lora_a_sgemm
  - `python/sglang/srt/models/nemotron_h.py` modified +32/-3 (35 lines); hunks: -57,6 +57,7; -163,6 +164,17 @@ def _get_or_create_alt_stream(device_module):; symbols: _get_or_create_alt_stream, _latent_proj_fuses_shared_add, NemotronHMoE, __init__
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_nemotron_h_shared_add.py
@@ -0,0 +1,127 @@
+"""
+Unit tests for the NemotronHMoE latent-projection shared-expert add.
+The fused path calls the projection's quant method directly,
+not ``ReplicatedLinear.forward``.
+These cases pin the gate that decides when the substitution is safe.
+"""
diff -- python/sglang/srt/models/nemotron_h.py
@@ -57,6 +57,7 @@
+from sglang.srt.layers.quantization.unquant import UnquantizedLinearMethod
@@ -163,6 +164,17 @@ def _get_or_create_alt_stream(device_module):
+def _latent_proj_fuses_shared_add(projection: nn.Module) -> bool:
+    return (
+        # LoRA swaps a wrapper module over this attribute after init,
+        # and a subclass may override forward; exact type excludes both.
```

- 已读文件:
  - tests: `test/registered/unit/models/test_nemotron_h_shared_add.py` added +127/-0
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +32/-3
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_unquant_apply_with_addend.py`, `test/registered/unit/models/test_nemotron_h_shared_add.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #35599 - Support NemotronH_Omni_Reasoning_V3 in SGLang

- 链接: https://github.com/sgl-project/sglang/pull/35599
- 状态/时间: merged / 2026-09-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` 等 10 个文件；关联提交 `fae8cd84cbc5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 20 个文件，+1081/-63，可读 patch 1476 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support NemotronH_Omni_Reasoning_V3 in SGLang」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `test/registered/unit/models/test_nemotron_h_mtp.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`；技术摘要: 覆盖「Support NemotronH_Omni_Reasoning_V3 in SGLang」；主要实现面是 `test/registered/unit/models/test_nemotron_h_mtp.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_nemotron_h_mtp.py` added +226/-0 (226 lines); hunks: -0,0 +1,226; symbols: _RecordingLayer, __init__, forward, TestNemotronHMultiTokenPredictor，涉及 `_RecordingLayer, __init__, forward`；`test/registered/unit/models/test_nano_nemotron_vl.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: TestNemotronHOmniModel, test_existing_nano_model_keeps_ignoring_unrecognized_weights, test_model_registry_resolves_new_architecture, test_exposes_language_embed_and_head，涉及 `TestNemotronHOmniModel, test_existing_nano_model_keeps_ignoring_unrecognized_weights, test_model_registry_resolves_new_architecture`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +105/-26 (131 lines); hunks: -16,6 +16,7; -178,6 +179,18 @@ def pixel_shuffle(self, x: torch.Tensor, scale_factor: floa...; symbols: pixel_shuffle, _normalize_vision_features, _load_extra_weight, get_embed_and_head，涉及 `pixel_shuffle, _normalize_vision_features, _load_extra_weight`；`test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +72/-13 (85 lines); hunks: -1,20 +1,16; -43,9 +39,19 @@ def weight_loader(self, param, loaded_weight):; symbols: _FakePPGroup, weight_loader, TestNemotronHWeightLoading, _make_minimal_model，涉及 `_FakePPGroup, weight_loader, TestNemotronHWeightLoading`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_nemotron_h_mtp.py` added +226/-0 (226 lines); hunks: -0,0 +1,226; symbols: _RecordingLayer, __init__, forward, TestNemotronHMultiTokenPredictor
  - `test/registered/unit/models/test_nano_nemotron_vl.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: TestNemotronHOmniModel, test_existing_nano_model_keeps_ignoring_unrecognized_weights, test_model_registry_resolves_new_architecture, test_exposes_language_embed_and_head
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +105/-26 (131 lines); hunks: -16,6 +16,7; -178,6 +179,18 @@ def pixel_shuffle(self, x: torch.Tensor, scale_factor: floa...; symbols: pixel_shuffle, _normalize_vision_features, _load_extra_weight, get_embed_and_head
  - `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +72/-13 (85 lines); hunks: -1,20 +1,16; -43,9 +39,19 @@ def weight_loader(self, param, loaded_weight):; symbols: _FakePPGroup, weight_loader, TestNemotronHWeightLoading, _make_minimal_model
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +70/-3 (73 lines); hunks: -27,6 +27,7; -38,6 +39,7; symbols: forward, NemotronHForCausalLMMTP, __init__
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_nemotron_h_mtp.py
@@ -0,0 +1,226 @@
+"""Unit tests for Nemotron-H MTP model behavior."""
+import unittest
+from types import SimpleNamespace
+from unittest.mock import patch
+import torch
+import torch.nn as nn
diff -- test/registered/unit/models/test_nano_nemotron_vl.py
@@ -0,0 +1,182 @@
+"""Unit tests for native Nemotron-H Omni model integration."""
+import unittest
+from types import SimpleNamespace
+import torch
+import torch.nn as nn
+from sglang.srt.models.nano_nemotron_vl import (
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -16,6 +16,7 @@
```

- 已读文件:
  - tests: `test/registered/unit/models/test_nemotron_h_mtp.py` added +226/-0; `test/registered/unit/models/test_nano_nemotron_vl.py` added +182/-0; `test/registered/unit/models/test_nemotron_h_weight_loading.py` modified +72/-13; `test/registered/unit/configs/test_nano_nemotron_vl_config.py` added +51/-0; `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` added +24/-0
  - runtime: `python/sglang/srt/models/nano_nemotron_vl.py` modified +105/-26; `python/sglang/srt/models/nemotron_h_mtp.py` modified +70/-3; `python/sglang/srt/configs/nano_nemotron_vl.py` modified +21/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/configs/test_model_config.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40800 - [Fix] Reduce Nemotron MTP attention outputs once

- 链接: https://github.com/sgl-project/sglang/pull/40800
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h_mtp.py`；关联提交 `9ebe42238baf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+94/-16，可读 patch 139 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Reduce Nemotron MTP attention outputs once」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「[Fix] Reduce Nemotron MTP attention outputs once」；主要实现面是 `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-16 (17 lines); hunks: -18,10 +18,7; -37,7 +34,6; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-16 (17 lines); hunks: -18,10 +18,7; -37,7 +34,6; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -18,10 +18,7 @@
-from sglang.srt.layers.dp_attention import (
-    attn_tp_all_reduce,
-    is_dp_attention_enabled,
-)
+from sglang.srt.layers.dp_attention import is_dp_attention_enabled
@@ -37,7 +34,6 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h_mtp.py` modified +1/-16
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_nemotron_h_mtp_reduction.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40801 - [Fix] Capture complete Nemotron auxiliary hidden states

- 链接: https://github.com/sgl-project/sglang/pull/40801
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `379e8f916b7e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+145/-2，可读 patch 169 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Capture complete Nemotron auxiliary hidden states」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Fix] Capture complete Nemotron auxiliary hidden states」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +14/-2 (16 lines); hunks: -863,6 +863,18 @@ def get_layer(idx: int, prefix: str):; -891,7 +903,7 @@ def forward(; symbols: get_layer, _capture_hidden_states, forward，涉及 `get_layer, _capture_hidden_states, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +14/-2 (16 lines); hunks: -863,6 +863,18 @@ def get_layer(idx: int, prefix: str):; -891,7 +903,7 @@ def forward(; symbols: get_layer, _capture_hidden_states, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -863,6 +863,18 @@ def get_layer(idx: int, prefix: str):
+    def _capture_hidden_states(self, hidden_states, residual, boundary_idx):
+        if (
+            is_dp_attention_enabled()
+            and residual is not None
+            and boundary_idx > 0
+            and is_attn_layer(self.config.hybrid_override_pattern[boundary_idx - 1])
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +14/-2
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_nemotron_h_aux_capture.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40867 - [Refactor] Run Nemotron-H DP attention through the standard layer communicator

- 链接: https://github.com/sgl-project/sglang/pull/40867
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`；关联提交 `701cf7e47e68`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+318/-301，可读 patch 973 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Run Nemotron-H DP attention through the standard layer communicator」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`；技术摘要: 覆盖「[Refactor] Run Nemotron-H DP attention through the standard layer communicator」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +108/-189 (297 lines); hunks: -81,11 +81,9; -383,7 +381,24 @@ def forward(; symbols: forward, NemotronHMLPLikeDecoderLayer, _init_layer_communicator，涉及 `forward, NemotronHMLPLikeDecoderLayer, _init_layer_communicator`；`python/sglang/srt/models/nemotron_h_utils.py` modified +6/-55 (61 lines); hunks: -1,19 +1,15; -22,32 +18,9 @@ def is_attn_layer(layer_type: str) -> bool:; symbols: is_attn_layer, get_real_num_tokens, pad_to_original_num_tokens, feeds_mlp_layer，涉及 `is_attn_layer, get_real_num_tokens, pad_to_original_num_tokens`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +108/-189 (297 lines); hunks: -81,11 +81,9; -383,7 +381,24 @@ def forward(; symbols: forward, NemotronHMLPLikeDecoderLayer, _init_layer_communicator
  - `python/sglang/srt/models/nemotron_h_utils.py` modified +6/-55 (61 lines); hunks: -1,19 +1,15; -22,32 +18,9 @@ def is_attn_layer(layer_type: str) -> bool:; symbols: is_attn_layer, get_real_num_tokens, pad_to_original_num_tokens, feeds_mlp_layer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -81,11 +81,9 @@
-    get_real_num_tokens,
-    input_norm_maybe_fuse_allreduce,
+    feeds_mlp_layer,
-    pad_to_original_num_tokens,
@@ -383,7 +381,24 @@ def forward(
-    """Shared forward for the dense-MLP / MoE decoder layers."""
diff -- python/sglang/srt/models/nemotron_h_utils.py
@@ -1,19 +1,15 @@
-"""DP-attention helpers for the Nemotron-H model."""
+"""Layer-communication helpers for the Nemotron-H model."""
-import torch
-from sglang.srt.distributed import tensor_model_parallel_all_reduce
-    apply_flashinfer_allreduce_fusion,
-from sglang.srt.model_executor.forward_batch_info import ForwardBatch
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +108/-189; `python/sglang/srt/models/nemotron_h_utils.py` modified +6/-55
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/test_linear_attention_masked_idle_rank.py`, `test/registered/unit/model_executor/test_mlp_sync_hybrid_target_verify.py`, `test/registered/unit/models/test_nemotron_h_aux_capture.py`, `test/registered/unit/models/test_nemotron_h_mtp_reduction.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41430 - [Refactor] Nemotron-H: build each layer's boundaries from its stage and the previous one

- 链接: https://github.com/sgl-project/sglang/pull/41430
- 状态/时间: merged / 2026-09-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h_utils.py`；关联提交 `8c43c667cbb4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+560/-136，可读 patch 1021 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Nemotron-H: build each layer's boundaries from its stage and the previous one」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「[Refactor] Nemotron-H: build each layer's boundaries from its stage and the previous one」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +34/-86 (120 lines); hunks: -78,11 +78,7; -376,66 +372,28 @@ def forward(; symbols: forward, NemotronHMLPLikeDecoderLayer, _init_layer_communicator，涉及 `forward, NemotronHMLPLikeDecoderLayer, _init_layer_communicator`；`python/sglang/srt/models/nemotron_h_utils.py` modified +95/-15 (110 lines); hunks: -1,12 +1,24; -18,9 +30,75 @@ def is_attn_layer(layer_type: str) -> bool:; symbols: is_attn_layer, feeds_mlp_layer, _stage_kind, _stage_decl，涉及 `is_attn_layer, feeds_mlp_layer, _stage_kind`；`python/sglang/srt/models/nemotron_h_mtp.py` modified +0/-1 (1 lines); hunks: -141,7 +141,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +34/-86 (120 lines); hunks: -78,11 +78,7; -376,66 +372,28 @@ def forward(; symbols: forward, NemotronHMLPLikeDecoderLayer, _init_layer_communicator
  - `python/sglang/srt/models/nemotron_h_utils.py` modified +95/-15 (110 lines); hunks: -1,12 +1,24; -18,9 +30,75 @@ def is_attn_layer(layer_type: str) -> bool:; symbols: is_attn_layer, feeds_mlp_layer, _stage_kind, _stage_decl
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +0/-1 (1 lines); hunks: -141,7 +141,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -78,11 +78,7 @@
-from sglang.srt.models.nemotron_h_utils import (
-    feeds_mlp_layer,
-    is_attn_layer,
-    make_layer_communicator,
-)
+from sglang.srt.models.nemotron_h_utils import make_layer_communicator
diff -- python/sglang/srt/models/nemotron_h_utils.py
@@ -1,12 +1,24 @@
-from torch import nn
+from typing import Optional
-from sglang.srt.configs.nemotron_h import ATTENTION, MAMBA
+from sglang.srt.configs.nemotron_h import ATTENTION, MAMBA, MOE
+from sglang.srt.layers.boundary_layout import (
+    Layout,
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -141,7 +141,6 @@ def __init__(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +34/-86; `python/sglang/srt/models/nemotron_h_utils.py` modified +95/-15; `python/sglang/srt/models/nemotron_h_mtp.py` modified +0/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/test_communicator_ffn_exit.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py`, `test/registered/unit/models/test_nemotron_h_aux_capture.py`, `test/registered/unit/models/test_nemotron_h_mtp_reduction.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #42306 - [Fix] Jet-Nemotron build and Granite MoE hybrid final norm

- 链接: https://github.com/sgl-project/sglang/pull/42306
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/jet_nemotron.py`；关联提交 `2c739b225b41`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-6，可读 patch 90 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Jet-Nemotron build and Granite MoE hybrid final norm」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/jet_nemotron.py`；技术摘要: 覆盖「[Fix] Jet-Nemotron build and Granite MoE hybrid final norm」；主要实现面是 `python/sglang/srt/models/jet_nemotron.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/jet_nemotron.py` modified +13/-3 (16 lines); hunks: -32,6 +32,7; -286,7 +287,7 @@ def forward(; symbols: DynamicShortConvolutionKernelGenerator, forward, __init__，涉及 `DynamicShortConvolutionKernelGenerator, forward, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/jet_nemotron.py` modified +13/-3 (16 lines); hunks: -32,6 +32,7; -286,7 +287,7 @@ def forward(; symbols: DynamicShortConvolutionKernelGenerator, forward, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/jet_nemotron.py
@@ -32,6 +32,7 @@
+from sglang.srt.utils.hf_transformers_utils import get_rope_config
@@ -286,7 +287,7 @@ def forward(
-        conv_cache = layer_cache.conv
+        conv_cache = layer_cache.conv[0]
@@ -369,12 +370,13 @@ def __init__(
+        rope_theta, rope_scaling = get_rope_config(self.config)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/jet_nemotron.py` modified +13/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/models/granitemoehybrid.py`, `python/sglang/srt/models/jet_nemotron.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42308 - [Refactor] Build the Llama and Nemotron-NAS decoders from stage boundaries

- 链接: https://github.com/sgl-project/sglang/pull/42308
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_nas.py`；关联提交 `e4554fd5e5fc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+173/-98，可读 patch 540 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Build the Llama and Nemotron-NAS decoders from stage boundaries」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/nemotron_nas.py`；技术摘要: 覆盖「[Refactor] Build the Llama and Nemotron-NAS decoders from stage boundaries」；主要实现面是 `python/sglang/srt/models/nemotron_nas.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_nas.py` modified +68/-35 (103 lines); hunks: -23,6 +23,12; -57,6 +63,21 @@ def _find_multiple(n: int, k: int) -> int:; symbols: _find_multiple, _previous_stage, _has_stage, DeciLMDecoderLayer，涉及 `_find_multiple, _previous_stage, _has_stage`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_nas.py` modified +68/-35 (103 lines); hunks: -23,6 +23,12; -57,6 +63,21 @@ def _find_multiple(n: int, k: int) -> int:; symbols: _find_multiple, _previous_stage, _has_stage, DeciLMDecoderLayer
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_nas.py
@@ -23,6 +23,12 @@
+from sglang.srt.layers.layer_boundary import (
+    declare_attn,
+    declare_ffn,
+    make_stages,
+)
+from sglang.srt.layers.layer_boundary.residual import batch as residual_batch
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_nas.py` modified +68/-35
- 验证与风险: diff 自带测试面 `test/registered/unit/layer_boundary/test_declared_decoder_boundary.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #42933 - Fix EVS for NemotronH_Omni_Reasoning_V3

- 链接: https://github.com/sgl-project/sglang/pull/42933
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`；关联提交 `4b5b7271454f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+273/-45，可读 patch 397 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix EVS for NemotronH_Omni_Reasoning_V3」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`；技术摘要: 覆盖「Fix EVS for NemotronH_Omni_Reasoning_V3」；主要实现面是 `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_nano_nemotron_vl.py` modified +99/-0 (99 lines); hunks: -1,20 +1,119; symbols: _temporal_video_model, extract_video_feature_temporal, _video_item, TestNemotronHOmniVideo，涉及 `_temporal_video_model, extract_video_feature_temporal, _video_item`；`python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +52/-32 (84 lines); hunks: -59,6 +59,46; -189,8 +229,8 @@ def render_tubelet(; symbols: _create_visual_items, NanoNemotronVLImageProcessor, render_tubelet, process_mm_data_async，涉及 `_create_visual_items, NanoNemotronVLImageProcessor, render_tubelet`；`test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` added +64/-0 (64 lines); hunks: -0,0 +1,64; symbols: TestNanoNemotronVLProcessor, test_tubelet_label_matches_hf_reference, test_evs_video_next_to_dynamic_images_keeps_evs_metadata，涉及 `TestNanoNemotronVLProcessor, test_tubelet_label_matches_hf_reference, test_evs_video_next_to_dynamic_images_keeps_evs_metadata`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +14/-10 (24 lines); hunks: -147,13 +147,10 @@ def pad_input_ids(self, input_ids: array, mm_inputs: Multi...; -283,10 +280,17 @@ def get_video_feature(self, items: list[MultimodalDataItem]):; symbols: pad_input_ids, get_video_feature，涉及 `pad_input_ids, get_video_feature`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_nano_nemotron_vl.py` modified +99/-0 (99 lines); hunks: -1,20 +1,119; symbols: _temporal_video_model, extract_video_feature_temporal, _video_item, TestNemotronHOmniVideo
  - `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +52/-32 (84 lines); hunks: -59,6 +59,46; -189,8 +229,8 @@ def render_tubelet(; symbols: _create_visual_items, NanoNemotronVLImageProcessor, render_tubelet, process_mm_data_async
  - `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` added +64/-0 (64 lines); hunks: -0,0 +1,64; symbols: TestNanoNemotronVLProcessor, test_tubelet_label_matches_hf_reference, test_evs_video_next_to_dynamic_images_keeps_evs_metadata
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +14/-10 (24 lines); hunks: -147,13 +147,10 @@ def pad_input_ids(self, input_ids: array, mm_inputs: Multi...; -283,10 +280,17 @@ def get_video_feature(self, items: list[MultimodalDataItem]):; symbols: pad_input_ids, get_video_feature
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_nano_nemotron_vl.py
@@ -1,20 +1,119 @@
+import math
+from array import array
+from sglang.srt.managers.schedule_batch import (
+    Modality,
+    MultimodalDataItem,
+    MultimodalInputs,
diff -- python/sglang/srt/multimodal/processors/nano_nemotron_vl.py
@@ -59,6 +59,46 @@
+def _create_visual_items(
+    *,
+    create_data_items,
+    image_feature: torch.Tensor | list[torch.Tensor] | None,
+    image_offsets: list[tuple[int, int]],
+    num_tokens_per_image: list[int] | None,
diff -- test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py
@@ -0,0 +1,64 @@
```

- 已读文件:
  - tests: `test/registered/unit/models/test_nano_nemotron_vl.py` modified +99/-0; `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` added +64/-0
  - runtime: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +52/-32; `python/sglang/srt/models/nano_nemotron_vl.py` modified +14/-10
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_evs.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39798 - [lora] Support LoRA for the NemotronH_Nano_VL_V2 model family

- 链接: https://github.com/sgl-project/sglang/pull/39798
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`；关联提交 `2a8e9db3b09f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+286/-112，可读 patch 503 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[lora] Support LoRA for the NemotronH_Nano_VL_V2 model family」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `python/sglang/srt/models/nano_nemotron_vl.py`；技术摘要: 覆盖「[lora] Support LoRA for the NemotronH_Nano_VL_V2 model family」；主要实现面是 `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `python/sglang/srt/models/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_nano_nemotron_vl.py` modified +30/-0 (30 lines); hunks: -39,6 +39,36 @@ def test_model_registry_resolves_new_architecture(self):; symbols: test_model_registry_resolves_new_architecture, test_lora_scope_excludes_the_vision_tower, test_lora_shape_hooks_reach_the_language_model, test_vision_final_layernorm_is_loaded_and_applied，涉及 `test_model_registry_resolves_new_architecture, test_lora_scope_excludes_the_vision_tower, test_lora_shape_hooks_reach_the_language_model`；`test/registered/unit/configs/test_nano_nemotron_vl_config.py` modified +11/-1 (12 lines); hunks: -8,7 +8,7; -46,6 +46,16 @@ def test_normalizes_current_nemotron_h_layer_names(self):; symbols: TestNemotronHOmniConfig, test_normalizes_current_nemotron_h_layer_names, test_text_config_resolves_to_the_language_model_config，涉及 `TestNemotronHOmniConfig, test_normalizes_current_nemotron_h_layer_names, test_text_config_resolves_to_the_language_model_config`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +11/-0 (11 lines); hunks: -58,10 +58,21 @@ class NemotronH_Nano_VL_V2(EVS):; symbols: NemotronH_Nano_VL_V2, create_evs_config, should_apply_lora, get_hidden_dim，涉及 `NemotronH_Nano_VL_V2, create_evs_config, should_apply_lora`；`python/sglang/srt/configs/nano_nemotron_vl.py` modified +5/-2 (7 lines); hunks: -76,8 +76,6 @@ def __init__(; -88,6 +86,8 @@ def __init__(; symbols: __init__, get_text_config, create_radio_config，涉及 `__init__, get_text_config, create_radio_config`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_nano_nemotron_vl.py` modified +30/-0 (30 lines); hunks: -39,6 +39,36 @@ def test_model_registry_resolves_new_architecture(self):; symbols: test_model_registry_resolves_new_architecture, test_lora_scope_excludes_the_vision_tower, test_lora_shape_hooks_reach_the_language_model, test_vision_final_layernorm_is_loaded_and_applied
  - `test/registered/unit/configs/test_nano_nemotron_vl_config.py` modified +11/-1 (12 lines); hunks: -8,7 +8,7; -46,6 +46,16 @@ def test_normalizes_current_nemotron_h_layer_names(self):; symbols: TestNemotronHOmniConfig, test_normalizes_current_nemotron_h_layer_names, test_text_config_resolves_to_the_language_model_config
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +11/-0 (11 lines); hunks: -58,10 +58,21 @@ class NemotronH_Nano_VL_V2(EVS):; symbols: NemotronH_Nano_VL_V2, create_evs_config, should_apply_lora, get_hidden_dim
  - `python/sglang/srt/configs/nano_nemotron_vl.py` modified +5/-2 (7 lines); hunks: -76,8 +76,6 @@ def __init__(; -88,6 +86,8 @@ def __init__(; symbols: __init__, get_text_config, create_radio_config
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_nano_nemotron_vl.py
@@ -39,6 +39,36 @@ def test_model_registry_resolves_new_architecture(self):
+    def test_lora_scope_excludes_the_vision_tower(self):
+        """RADIO qkv_proj under a layers.<i>. path is outside the LoRA scope."""
+        model = object.__new__(NemotronH_Omni_Reasoning_V3)
+        nn.Module.__init__(model)
+        self.assertTrue(
+            model.should_apply_lora("language_model.model.layers.7.mixer.qkv_proj")
diff -- test/registered/unit/configs/test_nano_nemotron_vl_config.py
@@ -8,7 +8,7 @@
-register_cpu_ci(est_time=2, suite="base-a-test-cpu")
+register_cpu_ci(est_time=3, suite="base-a-test-cpu")
@@ -46,6 +46,16 @@ def test_normalizes_current_nemotron_h_layer_names(self):
+    def test_text_config_resolves_to_the_language_model_config(self):
+        """get_text_config() returns llm_config, which LoRAManager sizes from."""
+        config = NemotronH_Omni_Reasoning_V3_Config(
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -58,10 +58,21 @@ class NemotronH_Nano_VL_V2(EVS):
```

- 已读文件:
  - tests: `test/registered/unit/models/test_nano_nemotron_vl.py` modified +30/-0; `test/registered/unit/configs/test_nano_nemotron_vl_config.py` modified +11/-1
  - runtime: `python/sglang/srt/models/nano_nemotron_vl.py` modified +11/-0; `python/sglang/srt/configs/nano_nemotron_vl.py` modified +5/-2
- 验证与风险: diff 自带测试面 `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `test/registered/unit/lora/test_lora_manager_init_modules.py`, `test/registered/unit/lora/test_lora_manager_tied_lm_head.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43685 - Support EPLB for Nemotron-H

- 链接: https://github.com/sgl-project/sglang/pull/43685
- 状态/时间: merged / 2026-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `test/registered/e2e/models_large/test_nvidia_nemotron_3_super_nvfp4.py` 等 6 个文件；关联提交 `6fe5596ebb1b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+312/-20，可读 patch 587 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support EPLB for Nemotron-H」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h_mtp.py`；技术摘要: 覆盖「Support EPLB for Nemotron-H」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +87/-9 (96 lines); hunks: -26,6 +26,9; -50,6 +53,7; symbols: __init__, _apply_fc1_latent_proj, _forward_core, _forward_core_normal，涉及 `__init__, _apply_fc1_latent_proj, _forward_core`；`test/registered/unit/models/test_nano_nemotron_vl.py` modified +31/-0 (31 lines); hunks: -8,6 +8,8; -281,6 +283,35 @@ def load_sound_weights(weights):; symbols: load_sound_weights, test_expert_location_config_spans_full_hybrid_stack, test_routed_expert_weights_come_from_language_model，涉及 `load_sound_weights, test_expert_location_config_spans_full_hybrid_stack, test_routed_expert_weights_come_from_language_model`；`python/sglang/srt/models/nemotron_h_mtp.py` modified +9/-6 (15 lines); hunks: -18,6 +18,7; -137,6 +138,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +10/-0 (10 lines); hunks: -128,6 +128,16 @@ def __init__(; symbols: __init__, routed_experts_weights_of_layer, get_model_config_for_expert_location, pad_input_ids，涉及 `__init__, routed_experts_weights_of_layer, get_model_config_for_expert_location`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +87/-9 (96 lines); hunks: -26,6 +26,9; -50,6 +53,7; symbols: __init__, _apply_fc1_latent_proj, _forward_core, _forward_core_normal
  - `test/registered/unit/models/test_nano_nemotron_vl.py` modified +31/-0 (31 lines); hunks: -8,6 +8,8; -281,6 +283,35 @@ def load_sound_weights(weights):; symbols: load_sound_weights, test_expert_location_config_spans_full_hybrid_stack, test_routed_expert_weights_come_from_language_model
  - `python/sglang/srt/models/nemotron_h_mtp.py` modified +9/-6 (15 lines); hunks: -18,6 +18,7; -137,6 +138,7 @@ def __init__(; symbols: __init__, forward
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +10/-0 (10 lines); hunks: -128,6 +128,16 @@ def __init__(; symbols: __init__, routed_experts_weights_of_layer, get_model_config_for_expert_location, pad_input_ids
  - `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py` modified +51/-0 (51 lines); hunks: -54,6 +54,14 @@ def _nemotron_h_overrides(server_args: Any, hf_config: Any) -...; -76,6 +84,18 @@ def _nemotron_h_overrides(server_args: Any, hf_config: Any) -...; symbols: _nemotron_h_overrides, _validate_expert_remap
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -26,6 +26,9 @@
+from sglang.srt.eplb.expert_distribution import get_global_expert_distribution_recorder
+from sglang.srt.eplb.expert_location import ModelConfigForExpertLocation
+from sglang.srt.eplb.expert_location_dispatch import ExpertLocationDispatchInfo
@@ -50,6 +53,7 @@
+    filter_moe_weight_param_global_expert,
@@ -82,6 +86,7 @@
diff -- test/registered/unit/models/test_nano_nemotron_vl.py
@@ -8,6 +8,8 @@
+from sglang.srt.configs import NemotronHConfig
+from sglang.srt.configs.nemotron_h import MOE
@@ -281,6 +283,35 @@ def load_sound_weights(weights):
+    def test_expert_location_config_spans_full_hybrid_stack(self):
+        """The VL wrapper exposes the full-stack expert-location config for EPLB."""
+        pattern = "ME*E-E"
diff -- python/sglang/srt/models/nemotron_h_mtp.py
@@ -18,6 +18,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +87/-9; `python/sglang/srt/models/nemotron_h_mtp.py` modified +9/-6; `python/sglang/srt/models/nano_nemotron_vl.py` modified +10/-0; `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py` modified +51/-0
  - tests: `test/registered/unit/models/test_nano_nemotron_vl.py` modified +31/-0; `test/registered/e2e/models_large/test_nvidia_nemotron_3_super_nvfp4.py` modified +43/-5
- 验证与风险: diff 自带测试面 `test/registered/e2e/models_large/test_nvidia_nemotron_3_super_nvfp4.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/test_model_overrides.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44510 - [Doc] cookbook: Add Nemotron 3.5 Super VL

- 链接: https://github.com/sgl-project/sglang/pull/44510
- 状态/时间: merged / 2026-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`；关联提交 `05cbe241be8b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+537/-2，可读 patch 563 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: Add Nemotron 3.5 Super VL」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx`；技术摘要: 覆盖「[Doc] cookbook: Add Nemotron 3.5 Super VL」；主要实现面是 `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` added +328/-0 (328 lines); hunks: -0,0 +1,328；`docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx` added +113/-0 (113 lines); hunks: -0,0 +1,113；`docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx` added +94/-0 (94 lines); hunks: -0,0 +1,94；`docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` modified +0/-1 (1 lines); hunks: -1,7 +1,6。
- 代码 diff 细节:
  - `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` added +328/-0 (328 lines); hunks: -0,0 +1,328
  - `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx` added +113/-0 (113 lines); hunks: -0,0 +1,113
  - `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx` added +94/-0 (94 lines); hunks: -0,0 +1,94
  - `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` modified +0/-1 (1 lines); hunks: -1,7 +1,6
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx
@@ -0,0 +1,328 @@
+// Instantiated from the cookbook-add-model config template. The non-Spark
+// source recipes were exercised on dev @ 2c7511f6f7cf1cdf9ae568ad0fb25f291edb10da.
+// Public HF IDs and the planned Docker image still need verification.
+export const config = {
+  modelName: "Nemotron 3.5 Super VL",
+  supportedHardware: ["b200", "h200", "rtx-pro-6000", "dgx-spark"],
diff -- docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx
@@ -0,0 +1,113 @@
+// Text-only GSM8K scores from completed sgl-eval==0.1.2 runs.
+// Accuracy verification applies to these NGC-weight source runs, not to the
+// public Hugging Face checkpoint IDs or the planned cookbook Docker tag.
+export const benchmarks = [
+  {
+    match: { hw: "b200", variant: "default", quant: "nvfp4", strategy: "high-throughput", nodes: "single", mambaDtype: "bfloat16" },
diff -- docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx
@@ -0,0 +1,94 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` added +328/-0; `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx` added +113/-0; `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx` added +94/-0; `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx` modified +0/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx`, `docs/cookbook/autoregressive/intro.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #44587 - [Doc] nemotron-3.5-super: update H200 and Spark wizard recipes

- 链接: https://github.com/sgl-project/sglang/pull/44587
- 状态/时间: merged / 2026-10-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`；关联提交 `0dc6de2e74e9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+20/-23，可读 patch 110 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] nemotron-3.5-super: update H200 and Spark wizard recipes」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`；技术摘要: 覆盖「[Doc] nemotron-3.5-super: update H200 and Spark wizard recipes」；主要实现面是 `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx` modified +14/-14 (28 lines); hunks: -1,6 +1,6; -52,27 +52,27 @@ export const benchmarks = [；`docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` modified +6/-9 (15 lines); hunks: -1,6 +1,5; -185,7 +184,6 @@ export const config = {。
- 代码 diff 细节:
  - `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx` modified +14/-14 (28 lines); hunks: -1,6 +1,6; -52,27 +52,27 @@ export const benchmarks = [
  - `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` modified +6/-9 (15 lines); hunks: -1,6 +1,5; -185,7 +184,6 @@ export const config = {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx
@@ -1,6 +1,6 @@
-// Accuracy verification applies to these NGC-weight source runs, not to the
-// public Hugging Face checkpoint IDs or the planned cookbook Docker tag.
+// H200 rows use the public BF16 Hugging Face checkpoint and cookbook image.
+// Other rows use NGC checkpoints with the source revision shown below.
@@ -52,27 +52,27 @@ export const benchmarks = [
-    sglang_version: "dev @ 2c7511f6f7cf",
diff -- docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx
@@ -1,6 +1,5 @@
-// Instantiated from the cookbook-add-model config template. The non-Spark
-// source recipes were exercised on dev @ 2c7511f6f7cf1cdf9ae568ad0fb25f291edb10da.
-// Public HF IDs and the planned Docker image still need verification.
+// Instantiated from the cookbook-add-model config template. Benchmark entries
+// identify the checkpoint and runtime used for each score.
@@ -185,7 +184,6 @@ export const config = {
```

- 已读文件:
  - docs: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx` modified +14/-14; `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx` modified +6/-9
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #44518 - [Feat] nemotron: Port Nemotron 3.5 Super serving changes

- 链接: https://github.com/sgl-project/sglang/pull/44518
- 状态/时间: merged / 2026-10-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h.py`；关联提交 `7c9a78efbecf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 23 个文件，+1825/-58，可读 patch 2332 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] nemotron: Port Nemotron 3.5 Super serving changes」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nano_nemotron_vl.py`；技术摘要: 覆盖「[Feat] nemotron: Port Nemotron 3.5 Super serving changes」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +168/-3 (171 lines); hunks: -18,14 +18,15; -65,7 +66,11; symbols: _get_or_create_alt_stream, _prefill_shared_expert_pool, _PrefillSharedExpertCall, __init__，涉及 `_get_or_create_alt_stream, _prefill_shared_expert_pool, _PrefillSharedExpertCall`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +3/-0 (3 lines); hunks: -447,6 +447,9 @@ def __init__(self, config, quant_config=None, prefix: str =...; symbols: __init__, prepare_for_forward, lm_head，涉及 `__init__, prepare_for_forward, lm_head`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +168/-3 (171 lines); hunks: -18,14 +18,15; -65,7 +66,11; symbols: _get_or_create_alt_stream, _prefill_shared_expert_pool, _PrefillSharedExpertCall, __init__
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +3/-0 (3 lines); hunks: -447,6 +447,9 @@ def __init__(self, config, quant_config=None, prefix: str =...; symbols: __init__, prepare_for_forward, lm_head
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -18,14 +18,15 @@
-from functools import partial
+from functools import lru_cache, partial
+from sglang.srt.environ import envs
@@ -65,7 +66,11 @@
-from sglang.srt.model_executor.forward_batch_info import ForwardBatch, PPProxyTensors
+from sglang.srt.model_executor.forward_batch_info import (
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -447,6 +447,9 @@ def __init__(self, config, quant_config=None, prefix: str = ""):
+    def prepare_for_forward(self, forward_batch: ForwardBatch) -> None:
+        self.language_model.prepare_for_forward(forward_batch)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +168/-3; `python/sglang/srt/models/nano_nemotron_vl.py` modified +3/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_flashinfer_host_plan.py`, `test/registered/kernels/ops/moe/test_sm120_topk_gate_small_m.py`, `test/registered/unit/layers/moe/test_moe_runner_config_placement.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44184 - [Fix] nemotron_vl: Preserve tokenized prompts during media expansion

- 链接: https://github.com/sgl-project/sglang/pull/44184
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`；关联提交 `dbe0a9a7c9c8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+219/-10，可读 patch 317 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] nemotron_vl: Preserve tokenized prompts during media expansion」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`；技术摘要: 覆盖「[Fix] nemotron_vl: Preserve tokenized prompts during media expansion」；主要实现面是 `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` modified +119/-0 (119 lines); hunks: -1,6 +1,9; -16,6 +19,122; symbols: TestNanoNemotronVLProcessor, _tokenized_processor, test_tokenized_images_preserve_text_ids_and_budget, test_video_marker_cleanup_preserves_text_unknown_ids，涉及 `TestNanoNemotronVLProcessor, _tokenized_processor, test_tokenized_images_preserve_text_ids_and_budget`；`python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +100/-10 (110 lines); hunks: -13,6 +13,7; -258,11 +259,80 @@ def render_audio(self, *, num_tokens: int):; symbols: render_audio, _media_token_ids, _splice_media, process_mm_data_async，涉及 `render_audio, _media_token_ids, _splice_media`。
- 代码 diff 细节:
  - `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` modified +119/-0 (119 lines); hunks: -1,6 +1,9; -16,6 +19,122; symbols: TestNanoNemotronVLProcessor, _tokenized_processor, test_tokenized_images_preserve_text_ids_and_budget, test_video_marker_cleanup_preserves_text_unknown_ids
  - `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +100/-10 (110 lines); hunks: -13,6 +13,7; -258,11 +259,80 @@ def render_audio(self, *, num_tokens: int):; symbols: render_audio, _media_token_ids, _splice_media, process_mm_data_async
- 关键代码摘录:

```diff
diff -- test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py
@@ -1,6 +1,9 @@
+import asyncio
+from types import SimpleNamespace
+from unittest.mock import AsyncMock, Mock, patch
@@ -16,6 +19,122 @@
+    def _tokenized_processor(self):
+        processor = object.__new__(NanoNemotronVLImageProcessor)
diff -- python/sglang/srt/multimodal/processors/nano_nemotron_vl.py
@@ -13,6 +13,7 @@
+from collections import deque
@@ -258,11 +259,80 @@ def render_audio(self, *, num_tokens: int):
+    def _media_token_ids(self) -> dict[int, str]:
+        """Only placeholders represented by a single token can be spliced."""
+        candidates = {
+            self.mm_tokens.image_token_id: self.IMG_CONTEXT_TOKEN,
```

- 已读文件:
  - tests: `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` modified +119/-0
  - runtime: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` modified +100/-10
- 验证与风险: diff 自带测试面 `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45082 - [Fix] nemotron: Correct weight-export failures and GEMV dispatch

- 链接: https://github.com/sgl-project/sglang/pull/45082
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_nvfp4_layout.py`；关联提交 `5bf10d4c79a5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 16 个文件，+173/-105，可读 patch 531 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] nemotron: Correct weight-export failures and GEMV dispatch」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/nemotron_h_nvfp4_layout.py`, `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Fix] nemotron: Correct weight-export failures and GEMV dispatch」；主要实现面是 `python/sglang/srt/models/nemotron_h_nvfp4_layout.py`, `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h_nvfp4_layout.py` added +60/-0 (60 lines); hunks: -0,0 +1,60; symbols: Nvfp4LayoutCycle, __init__, prepare_workspace, ensure，涉及 `Nvfp4LayoutCycle, __init__, prepare_workspace`；`python/sglang/srt/models/nemotron_h.py` modified +21/-3 (24 lines); hunks: -89,7 +89,7; -226,6 +226,19 @@ def _latent_proj_fuses_shared_add(projection: nn.Module) ->...; symbols: _latent_proj_fuses_shared_add, _publishes_weight_storage, NemotronHMoE, __init__，涉及 `_latent_proj_fuses_shared_add, _publishes_weight_storage, NemotronHMoE`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h_nvfp4_layout.py` added +60/-0 (60 lines); hunks: -0,0 +1,60; symbols: Nvfp4LayoutCycle, __init__, prepare_workspace, ensure
  - `python/sglang/srt/models/nemotron_h.py` modified +21/-3 (24 lines); hunks: -89,7 +89,7; -226,6 +226,19 @@ def _latent_proj_fuses_shared_add(projection: nn.Module) ->...; symbols: _latent_proj_fuses_shared_add, _publishes_weight_storage, NemotronHMoE, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h_nvfp4_layout.py
@@ -0,0 +1,60 @@
+from __future__ import annotations
+import torch
+from sglang.kernels.ops.gemm.sm120_nvfp4_moe import _transpose_module
+class Nvfp4LayoutCycle:
+    """Own the two views of a fixed, serial set of [512,1024,1344] weights."""
+    def __init__(self, weights):
diff -- python/sglang/srt/models/nemotron_h.py
@@ -89,7 +89,7 @@
-from sglang.srt.runtime_context import get_exec, get_parallel, get_schedule
+from sglang.srt.runtime_context import get_exec, get_model, get_parallel, get_schedule
@@ -226,6 +226,19 @@ def _latent_proj_fuses_shared_add(projection: nn.Module) -> bool:
+def _publishes_weight_storage() -> bool:
+    # Transfer-engine seeds and ModelExpress instances publish parameter
+    # addresses for remote readers right after weight loading.
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h_nvfp4_layout.py` added +60/-0; `python/sglang/srt/models/nemotron_h.py` modified +21/-3
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_flashinfer_host_plan.py`, `test/registered/kernels/ops/moe/test_sm120_topk_gate_small_m.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44581 - [Fix] nemotron_vl: Pad visual spans using processor offsets

- 链接: https://github.com/sgl-project/sglang/pull/44581
- 状态/时间: merged / 2026-10-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nano_nemotron_vl.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`；关联提交 `e5db41b329ef`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+53/-8，可读 patch 116 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] nemotron_vl: Pad visual spans using processor offsets」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`；技术摘要: 覆盖「[Fix] nemotron_vl: Pad visual spans using processor offsets」；主要实现面是 `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` modified +41/-0 (41 lines); hunks: -2,11 +2,14; -135,6 +138,44 @@ def test_tokenized_image_count_checked_before_loading(self):; symbols: test_tokenized_image_count_checked_before_loading, test_visual_offsets_ignore_literal_boundaries_and_preserve_audio, test_tubelet_label_matches_hf_reference，涉及 `test_tokenized_image_count_checked_before_loading, test_visual_offsets_ignore_literal_boundaries_and_preserve_audio, test_tubelet_label_matches_hf_reference`；`python/sglang/srt/models/nano_nemotron_vl.py` modified +5/-6 (11 lines); hunks: -30,6 +30,7; -139,20 +140,18 @@ def get_model_config_for_expert_location(cls, config):; symbols: get_model_config_for_expert_location, pad_input_ids，涉及 `get_model_config_for_expert_location, pad_input_ids`；`test/registered/unit/models/test_nano_nemotron_vl.py` modified +7/-2 (9 lines); hunks: -99,15 +99,20 @@ def test_evs_prunes_temporal_tubelets_per_video(self):; symbols: test_evs_prunes_temporal_tubelets_per_video, test_evs_keeps_image_pad_values_for_redistribution，涉及 `test_evs_prunes_temporal_tubelets_per_video, test_evs_keeps_image_pad_values_for_redistribution`。
- 代码 diff 细节:
  - `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` modified +41/-0 (41 lines); hunks: -2,11 +2,14; -135,6 +138,44 @@ def test_tokenized_image_count_checked_before_loading(self):; symbols: test_tokenized_image_count_checked_before_loading, test_visual_offsets_ignore_literal_boundaries_and_preserve_audio, test_tubelet_label_matches_hf_reference
  - `python/sglang/srt/models/nano_nemotron_vl.py` modified +5/-6 (11 lines); hunks: -30,6 +30,7; -139,20 +140,18 @@ def get_model_config_for_expert_location(cls, config):; symbols: get_model_config_for_expert_location, pad_input_ids
  - `test/registered/unit/models/test_nano_nemotron_vl.py` modified +7/-2 (9 lines); hunks: -99,15 +99,20 @@ def test_evs_prunes_temporal_tubelets_per_video(self):; symbols: test_evs_prunes_temporal_tubelets_per_video, test_evs_keeps_image_pad_values_for_redistribution
- 关键代码摘录:

```diff
diff -- test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py
@@ -2,11 +2,14 @@
+from array import array
+from sglang.srt.managers.schedule_batch import Modality, MultimodalDataItem
+from sglang.srt.models.nano_nemotron_vl import NemotronH_Nano_VL_V2
@@ -135,6 +138,44 @@ def test_tokenized_image_count_checked_before_loading(self):
+    def test_visual_offsets_ignore_literal_boundaries_and_preserve_audio(self):
+        model = object.__new__(NemotronH_Nano_VL_V2)
diff -- python/sglang/srt/models/nano_nemotron_vl.py
@@ -30,6 +30,7 @@
+    pad_mm_tokens,
@@ -139,20 +140,18 @@ def get_model_config_for_expert_location(cls, config):
-        im_start_id: int = mm_inputs.im_start_id
-        im_end_id: int = mm_inputs.im_end_id
+            # Literal boundary tokens in text must not change which spans are images.
-            input_ids = pad_mm_token_pairs(
diff -- test/registered/unit/models/test_nano_nemotron_vl.py
@@ -99,15 +99,20 @@ def test_evs_prunes_temporal_tubelets_per_video(self):
```

- 已读文件:
  - tests: `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py` modified +41/-0; `test/registered/unit/models/test_nano_nemotron_vl.py` modified +7/-2
  - runtime: `python/sglang/srt/models/nano_nemotron_vl.py` modified +5/-6
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #46551 - [Refactor] nemotron_h: Read the prefill shared expert's output from the caller's holder

- 链接: https://github.com/sgl-project/sglang/pull/46551
- 状态/时间: merged / 2026-10-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/nemotron_h.py`；关联提交 `5aeb6dfdb648`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-9，可读 patch 50 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] nemotron_h: Read the prefill shared expert's output from the caller's holder」；模型线: Nemotron Super；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/nemotron_h.py`；技术摘要: 覆盖「[Refactor] nemotron_h: Read the prefill shared expert's output from the caller's holder」；主要实现面是 `python/sglang/srt/models/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron_h.py` modified +6/-9 (15 lines); hunks: -178,7 +178,7 @@ def __init__(self, stream):; -189,10 +189,9 @@ def launch(self, module, hidden_states):; symbols: __init__, launch, _capture_prefill_shared_expert，涉及 `__init__, launch, _capture_prefill_shared_expert`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron_h.py` modified +6/-9 (15 lines); hunks: -178,7 +178,7 @@ def __init__(self, stream):; -189,10 +189,9 @@ def launch(self, module, hidden_states):; symbols: __init__, launch, _capture_prefill_shared_expert
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron_h.py
@@ -178,7 +178,7 @@ def __init__(self, stream):
-    def launch(self, module, hidden_states):
+    def launch(self, module, hidden_states) -> None:
@@ -189,10 +189,9 @@ def launch(self, module, hidden_states):
-        return self.output
-def _capture_prefill_shared_expert(module, hidden_states, call):
+def _capture_prefill_shared_expert(module, hidden_states, call) -> None:
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron_h.py` modified +6/-9
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/nemotron_h.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #44487 - [Fix] nemotron: Preserve nested Puzzle configs

- 链接: https://github.com/sgl-project/sglang/pull/44487
- 状态/时间: merged / 2026-10-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/nano_nemotron_vl.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`；关联提交 `4549937519a5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+70/-2，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] nemotron: Preserve nested Puzzle configs」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`；技术摘要: 覆盖「[Fix] nemotron: Preserve nested Puzzle configs」；主要实现面是 `test/registered/unit/configs/test_nano_nemotron_vl_config.py`, `python/sglang/srt/configs/nano_nemotron_vl.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/configs/test_nano_nemotron_vl_config.py` modified +62/-0 (62 lines); hunks: -1,10 +1,14; -56,6 +60,64 @@ def test_text_config_resolves_to_the_language_model_config(se...; symbols: test_text_config_resolves_to_the_language_model_config, test_puzzle_layer_settings_survive_serialization, test_non_puzzle_configs_keep_existing_defaults，涉及 `test_text_config_resolves_to_the_language_model_config, test_puzzle_layer_settings_survive_serialization, test_non_puzzle_configs_keep_existing_defaults`；`python/sglang/srt/configs/nano_nemotron_vl.py` modified +8/-2 (10 lines); hunks: -17,7 +17,7; -78,7 +78,13 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `test/registered/unit/configs/test_nano_nemotron_vl_config.py` modified +62/-0 (62 lines); hunks: -1,10 +1,14; -56,6 +60,64 @@ def test_text_config_resolves_to_the_language_model_config(se...; symbols: test_text_config_resolves_to_the_language_model_config, test_puzzle_layer_settings_survive_serialization, test_non_puzzle_configs_keep_existing_defaults
  - `python/sglang/srt/configs/nano_nemotron_vl.py` modified +8/-2 (10 lines); hunks: -17,7 +17,7; -78,7 +78,13 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- test/registered/unit/configs/test_nano_nemotron_vl_config.py
@@ -1,10 +1,14 @@
+import json
+    NemotronH_Nano_Omni_Reasoning_V3_Config,
+    NemotronH_Nano_VL_V2_Config,
+from sglang.srt.configs.nemotron_h import NemotronHConfig, NemotronHPuzzleConfig
@@ -56,6 +60,64 @@ def test_text_config_resolves_to_the_language_model_config(self):
+    def test_puzzle_layer_settings_survive_serialization(self):
diff -- python/sglang/srt/configs/nano_nemotron_vl.py
@@ -17,7 +17,7 @@
-from sglang.srt.configs.nemotron_h import NemotronHConfig
+from sglang.srt.configs.nemotron_h import NemotronHConfig, NemotronHPuzzleConfig
@@ -78,7 +78,13 @@ def __init__(
-            self.llm_config = NemotronHConfig(**llm_config)
+            if llm_config.get("model_type") != "nemotron_h_puzzle":
+                self.llm_config = NemotronHConfig(**llm_config)
```

- 已读文件:
  - tests: `test/registered/unit/configs/test_nano_nemotron_vl_config.py` modified +62/-0
  - runtime: `python/sglang/srt/configs/nano_nemotron_vl.py` modified +8/-2
- 验证与风险: diff 自带测试面 `test/registered/unit/configs/test_nano_nemotron_vl_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44750 - [Fix] nemotron-h: Allow explicit CuTe DSL W4A16 MoE

- 链接: https://github.com/sgl-project/sglang/pull/44750
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`；关联提交 `5d4a6f499e02`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+67/-6，可读 patch 103 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] nemotron-h: Allow explicit CuTe DSL W4A16 MoE」；模型线: Nemotron Super；类别: 缺陷修复；主要 diff: `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`；技术摘要: 覆盖「[Fix] nemotron-h: Allow explicit CuTe DSL W4A16 MoE」；主要实现面是 `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py` modified +11/-2 (13 lines); hunks: -9,6 +9,7; -74,9 +75,17 @@ def _nemotron_h_overrides(server_args: Any, hf_config: Any) -...; symbols: _nemotron_h_overrides，涉及 `_nemotron_h_overrides`。
- 代码 diff 细节:
  - `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py` modified +11/-2 (13 lines); hunks: -9,6 +9,7; -74,9 +75,17 @@ def _nemotron_h_overrides(server_args: Any, hf_config: Any) -...; symbols: _nemotron_h_overrides
- 关键代码摘录:

```diff
diff -- python/sglang/srt/arg_groups/model_overrides/nemotron_h.py
@@ -9,6 +9,7 @@
+from sglang.srt.environ import envs
@@ -74,9 +75,17 @@ def _nemotron_h_overrides(server_args: Any, hf_config: Any) -> dict:
-        if cfg.moe_runner_backend not in ("auto", "marlin"):
+        # CuTe DSL supports BF16 activations with NVFP4 weights when opted in.
+        use_cutedsl_w4a16 = (
+            cfg.moe_runner_backend == "flashinfer_cutedsl"
```

- 已读文件:
  - runtime: `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py` modified +11/-2
- 验证与风险: diff 自带测试面 `test/registered/unit/test_model_overrides.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45885 - [Feat] nemotron3-embed: Support Nemotron-3-Embed embedding models

- 链接: https://github.com/sgl-project/sglang/pull/45885
- 状态/时间: merged / 2026-11-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py`, `python/sglang/srt/models/nemotron3_embedding.py`, `test/registered/prefill_only/test_nemotron3_embedding.py`；关联提交 `c6f1eef4c946`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+396/-2，可读 patch 553 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] nemotron3-embed: Support Nemotron-3-Embed embedding models」；模型线: Nemotron Super；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/nemotron3_embedding.py`, `test/registered/prefill_only/test_nemotron3_embedding.py`, `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py`；技术摘要: 覆盖「[Feat] nemotron3-embed: Support Nemotron-3-Embed embedding models」；主要实现面是 `python/sglang/srt/models/nemotron3_embedding.py`, `test/registered/prefill_only/test_nemotron3_embedding.py`, `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/nemotron3_embedding.py` added +65/-0 (65 lines); hunks: -0,0 +1,65; symbols: _FP32Pooler, forward, EmbeddingNemotron3Model, __init__，涉及 `_FP32Pooler, forward, EmbeddingNemotron3Model`；`test/registered/prefill_only/test_nemotron3_embedding.py` added +130/-0 (130 lines); hunks: -0,0 +1,130; symbols: TestNemotron3Embedding, setUpClass, tearDownClass, _check，涉及 `TestNemotron3Embedding, setUpClass, tearDownClass`；`python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py` added +19/-0 (19 lines); hunks: -0,0 +1,19; symbols: _embedding_nemotron3_overrides，涉及 `_embedding_nemotron3_overrides`。
- 代码 diff 细节:
  - `python/sglang/srt/models/nemotron3_embedding.py` added +65/-0 (65 lines); hunks: -0,0 +1,65; symbols: _FP32Pooler, forward, EmbeddingNemotron3Model, __init__
  - `test/registered/prefill_only/test_nemotron3_embedding.py` added +130/-0 (130 lines); hunks: -0,0 +1,130; symbols: TestNemotron3Embedding, setUpClass, tearDownClass, _check
  - `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py` added +19/-0 (19 lines); hunks: -0,0 +1,19; symbols: _embedding_nemotron3_overrides
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/nemotron3_embedding.py
@@ -0,0 +1,65 @@
+"""NVIDIA Nemotron-3-Embed: a bidirectional Ministral3 with normalized mean pooling."""
+from typing import Iterable, Optional, Tuple
+import torch
+from transformers import PretrainedConfig
+from sglang.srt.layers.pooler import Pooler, PoolingType
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
diff -- test/registered/prefill_only/test_nemotron3_embedding.py
@@ -0,0 +1,130 @@
+"""End-to-end check of Nemotron-3-Embed support against a Hugging Face reference.
+Builds a tiny random checkpoint with the same config shape as
+nvidia/Nemotron-3-Embed-1B (bare ``Ministral3Model``, ``is_causal=false``,
+``pooling=avg``) so the test does not download the real weights.
+"""
+import os
diff -- python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py
@@ -0,0 +1,19 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/nemotron3_embedding.py` added +65/-0; `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py` added +19/-0
  - tests: `test/registered/prefill_only/test_nemotron3_embedding.py` added +130/-0
- 验证与风险: diff 自带测试面 `test/registered/prefill_only/test_nemotron3_embedding.py`, `test/registered/unit/configs/test_embedding_model_spec.py`, `test/registered/unit/configs/test_model_config.py`, `test/registered/unit/test_model_overrides.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
