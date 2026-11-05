# sglang Mixtral Quark INT4/FP8 MoE 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `python/sglang/srt/layers/quantization/quark/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/layers/quantization/quark/quark.py` | [#10485](https://github.com/sgl-project/sglang/pull/10485), [#13147](https://github.com/sgl-project/sglang/pull/13147), [#18005](https://github.com/sgl-project/sglang/pull/18005), [#18182](https://github.com/sgl-project/sglang/pull/18182), [#18252](https://github.com/sgl-project/sglang/pull/18252), [#25467](https://github.com/sgl-project/sglang/pull/25467), [#25694](https://github.com/sgl-project/sglang/pull/25694), [#27057](https://github.com/sgl-project/sglang/pull/27057), [#27204](https://github.com/sgl-project/sglang/pull/27204), [#28213](https://github.com/sgl-project/sglang/pull/28213), [#28291](https://github.com/sgl-project/sglang/pull/28291), [#31054](https://github.com/sgl-project/sglang/pull/31054), ... (19 total) |
| `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` | [#10485](https://github.com/sgl-project/sglang/pull/10485), [#18252](https://github.com/sgl-project/sglang/pull/18252), [#27204](https://github.com/sgl-project/sglang/pull/27204) |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py` | [#18252](https://github.com/sgl-project/sglang/pull/18252) |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` | [#10485](https://github.com/sgl-project/sglang/pull/10485), [#18005](https://github.com/sgl-project/sglang/pull/18005), [#18182](https://github.com/sgl-project/sglang/pull/18182), [#18252](https://github.com/sgl-project/sglang/pull/18252), [#19422](https://github.com/sgl-project/sglang/pull/19422), [#28213](https://github.com/sgl-project/sglang/pull/28213), [#28291](https://github.com/sgl-project/sglang/pull/28291), [#39598](https://github.com/sgl-project/sglang/pull/39598) |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` | [#18005](https://github.com/sgl-project/sglang/pull/18005), [#18182](https://github.com/sgl-project/sglang/pull/18182), [#18252](https://github.com/sgl-project/sglang/pull/18252), [#18684](https://github.com/sgl-project/sglang/pull/18684), [#21040](https://github.com/sgl-project/sglang/pull/21040), [#21067](https://github.com/sgl-project/sglang/pull/21067), [#21097](https://github.com/sgl-project/sglang/pull/21097), [#23585](https://github.com/sgl-project/sglang/pull/23585), [#23597](https://github.com/sgl-project/sglang/pull/23597), [#23760](https://github.com/sgl-project/sglang/pull/23760), [#28213](https://github.com/sgl-project/sglang/pull/28213), [#28291](https://github.com/sgl-project/sglang/pull/28291), ... (24 total) |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` | [#27204](https://github.com/sgl-project/sglang/pull/27204), [#37367](https://github.com/sgl-project/sglang/pull/37367), [#45365](https://github.com/sgl-project/sglang/pull/45365) |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` | [#10485](https://github.com/sgl-project/sglang/pull/10485), [#18252](https://github.com/sgl-project/sglang/pull/18252), [#28734](https://github.com/sgl-project/sglang/pull/28734), [#29630](https://github.com/sgl-project/sglang/pull/29630), [#37564](https://github.com/sgl-project/sglang/pull/37564), [#40811](https://github.com/sgl-project/sglang/pull/40811), [#41134](https://github.com/sgl-project/sglang/pull/41134) |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | [#18252](https://github.com/sgl-project/sglang/pull/18252), [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30786](https://github.com/sgl-project/sglang/pull/30786), [#39155](https://github.com/sgl-project/sglang/pull/39155) |
| `python/sglang/srt/layers/quantization/quark/utils.py` | [#10485](https://github.com/sgl-project/sglang/pull/10485), [#18182](https://github.com/sgl-project/sglang/pull/18182), [#25467](https://github.com/sgl-project/sglang/pull/25467), [#28213](https://github.com/sgl-project/sglang/pull/28213), [#28291](https://github.com/sgl-project/sglang/pull/28291), [#39317](https://github.com/sgl-project/sglang/pull/39317) |
| `python/sglang/srt/layers/quantization/quark/weights.py` | [#27204](https://github.com/sgl-project/sglang/pull/27204) |
| `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` | [#7392](https://github.com/sgl-project/sglang/pull/7392), [#23597](https://github.com/sgl-project/sglang/pull/23597), [#23760](https://github.com/sgl-project/sglang/pull/23760), [#41807](https://github.com/sgl-project/sglang/pull/41807) |
| `python/sglang/srt/models/mixtral.py` | [#460](https://github.com/sgl-project/sglang/pull/460), [#1081](https://github.com/sgl-project/sglang/pull/1081), [#1290](https://github.com/sgl-project/sglang/pull/1290), [#1418](https://github.com/sgl-project/sglang/pull/1418), [#1835](https://github.com/sgl-project/sglang/pull/1835), [#2156](https://github.com/sgl-project/sglang/pull/2156), [#2163](https://github.com/sgl-project/sglang/pull/2163), [#2300](https://github.com/sgl-project/sglang/pull/2300), [#2371](https://github.com/sgl-project/sglang/pull/2371), [#2563](https://github.com/sgl-project/sglang/pull/2563), [#6223](https://github.com/sgl-project/sglang/pull/6223), [#7966](https://github.com/sgl-project/sglang/pull/7966), ... (19 total) |
| `python/sglang/srt/models/mixtral_quant.py` | [#460](https://github.com/sgl-project/sglang/pull/460), [#1081](https://github.com/sgl-project/sglang/pull/1081) |
| `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` | [#38546](https://github.com/sgl-project/sglang/pull/38546), [#41464](https://github.com/sgl-project/sglang/pull/41464) |
| `test/registered/e2e/quantization/test_quark_mxfp4.py` | [#41980](https://github.com/sgl-project/sglang/pull/41980) |
| `test/registered/unit/layers/quantization/test_quark_config.py` | [#25694](https://github.com/sgl-project/sglang/pull/25694), [#31054](https://github.com/sgl-project/sglang/pull/31054), [#38546](https://github.com/sgl-project/sglang/pull/38546), [#41899](https://github.com/sgl-project/sglang/pull/41899), [#45332](https://github.com/sgl-project/sglang/pull/45332), [#46800](https://github.com/sgl-project/sglang/pull/46800) |
| `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py` | [#39598](https://github.com/sgl-project/sglang/pull/39598) |
| `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py` | [#41899](https://github.com/sgl-project/sglang/pull/41899) |
| `test/registered/unit/layers/quantization/test_quark_utils.py` | [#37254](https://github.com/sgl-project/sglang/pull/37254), [#39317](https://github.com/sgl-project/sglang/pull/39317) |
| `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py` | [#34540](https://github.com/sgl-project/sglang/pull/34540), [#45802](https://github.com/sgl-project/sglang/pull/45802) |
| `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py` | [#47408](https://github.com/sgl-project/sglang/pull/47408) |
| `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py` | [#40811](https://github.com/sgl-project/sglang/pull/40811) |
| `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py` | [#28734](https://github.com/sgl-project/sglang/pull/28734) |
| `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py` | [#40776](https://github.com/sgl-project/sglang/pull/40776) |

## PR 覆盖总览

- git 追溯 PR 数: 68
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 68
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2024-05-21 | [#460](https://github.com/sgl-project/sglang/pull/460) | merged | port fp8 mixtral | `python/sglang/srt/models/mixtral_quant.py`, `python/sglang/srt/models/mixtral.py` |
| 2024-08-13 | [#1081](https://github.com/sgl-project/sglang/pull/1081) | merged | Update the mixtral to use the better FusedMoE layer | `python/sglang/srt/models/mixtral.py`, `python/sglang/srt/models/mixtral_quant.py` |
| 2024-09-01 | [#1290](https://github.com/sgl-project/sglang/pull/1290) | merged | fix: resolve fp8 for mixtral | `python/sglang/srt/models/mixtral.py` |
| 2024-09-14 | [#1418](https://github.com/sgl-project/sglang/pull/1418) | merged | Add torchao quant for mixtral and qwen_moe | `python/sglang/srt/models/mixtral.py` |
| 2024-10-29 | [#1835](https://github.com/sgl-project/sglang/pull/1835) | merged | [FP8 KV Cache, Mixtral] Avoid KeyError at loading pre-quantized FP8 m… | `python/sglang/srt/models/mixtral.py` |
| 2024-11-24 | [#2156](https://github.com/sgl-project/sglang/pull/2156) | merged | feat: update other MoE models deps | `python/sglang/srt/models/mixtral.py` |
| 2024-11-24 | [#2163](https://github.com/sgl-project/sglang/pull/2163) | merged | Rename triton_fused_moe -> fused_moe_triton | `python/sglang/srt/models/mixtral.py` |
| 2024-12-03 | [#2300](https://github.com/sgl-project/sglang/pull/2300) | merged | Fix gptq for moe layers | `python/sglang/srt/models/mixtral.py` |
| 2024-12-06 | [#2371](https://github.com/sgl-project/sglang/pull/2371) | merged | MoE Expert Parallel | `python/sglang/srt/models/mixtral.py` |
| 2024-12-23 | [#2563](https://github.com/sgl-project/sglang/pull/2563) | merged | Reorg moe code | `python/sglang/srt/models/mixtral.py` |
| 2025-05-12 | [#6223](https://github.com/sgl-project/sglang/pull/6223) | merged | [PP] Fix init_memory_pool desync & add PP for mixtral | `python/sglang/srt/models/mixtral.py` |
| 2025-07-19 | [#7966](https://github.com/sgl-project/sglang/pull/7966) | merged | [1/N] MoE Refactor: refactor `select_experts` | `python/sglang/srt/models/mixtral.py` |
| 2025-07-29 | [#8448](https://github.com/sgl-project/sglang/pull/8448) | merged | Support EPLB in FusedMoE | `python/sglang/srt/models/mixtral.py` |
| 2025-08-01 | [#8658](https://github.com/sgl-project/sglang/pull/8658) | merged | [5/N] MoE Refactor: Update MoE parallelism arguments | `python/sglang/srt/models/mixtral.py` |
| 2025-08-15 | [#8849](https://github.com/sgl-project/sglang/pull/8849) | merged | [6/N] MoE Refactor: Cleanup MoE-related configs | `python/sglang/srt/models/mixtral.py` |
| 2025-10-08 | [#11211](https://github.com/sgl-project/sglang/pull/11211) | merged | [8/N] MoE Refactor: deprecate `EPMoE` | `python/sglang/srt/models/mixtral.py` |
| 2025-11-13 | [#10485](https://github.com/sgl-project/sglang/pull/10485) | merged | [Quantization] Support Quark Dense + MoE FP8 & FP8 PTPC | `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2025-11-20 | [#13667](https://github.com/sgl-project/sglang/pull/13667) | merged | [Piecewise CUDA Graph] Fix recompile issue for Mixtral and Grok2 | `python/sglang/srt/models/mixtral.py` |
| 2025-12-09 | [#13147](https://github.com/sgl-project/sglang/pull/13147) | merged | Aiter fp8 kv cache | `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-01-14 | [#7392](https://github.com/sgl-project/sglang/pull/7392) | merged | [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm | `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` |
| 2026-02-18 | [#18252](https://github.com/sgl-project/sglang/pull/18252) | merged | [4/N] Quantization Refactor: Quark MoE schemes | `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-02-26 | [#19422](https://github.com/sgl-project/sglang/pull/19422) | merged | [AMD] Use fused GEMM with FP8 cast for FP8 prefill | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` |
| 2026-03-20 | [#18684](https://github.com/sgl-project/sglang/pull/18684) | merged | [AMD] Add MoE weights and scales padding | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-03-21 | [#21067](https://github.com/sgl-project/sglang/pull/21067) | merged | Revert "[AMD] Add MoE weights and scales padding" | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-03-25 | [#21040](https://github.com/sgl-project/sglang/pull/21040) | merged | [AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype. | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-04-13 | [#21097](https://github.com/sgl-project/sglang/pull/21097) | merged | [AMD] Add MoE weights and scales padding | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-04-24 | [#23585](https://github.com/sgl-project/sglang/pull/23585) | merged | Move expert_mask_gpu from FusedMoE layer to StandardDispatcher | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-05-01 | [#23597](https://github.com/sgl-project/sglang/pull/23597) | merged | [MoE] Add Aiter MoE runner backend and purge aiter.fused_moe from quant methods | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` |
| 2026-05-17 | [#23760](https://github.com/sgl-project/sglang/pull/23760) | merged | [MoE] Unify DeepEPMoE+MoriEPMoE through AITER MoeRunner pre/post-permute | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` |
| 2026-06-03 | [#18005](https://github.com/sgl-project/sglang/pull/18005) | merged | [AMD][MXFP4] Online MXFP4 quantization 1/N - dense and MOE models w. original BF16 weight | `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` |
| 2026-06-13 | [#27057](https://github.com/sgl-project/sglang/pull/27057) | merged | [AMD] move shared expert check function to quark | `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-06-13 | [#18182](https://github.com/sgl-project/sglang/pull/18182) | merged | [AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-06-14 | [#28213](https://github.com/sgl-project/sglang/pull/28213) | merged | Revert "[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs" | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-06-30 | [#27204](https://github.com/sgl-project/sglang/pull/27204) | merged | [AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8 | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/weights.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-07-09 | [#25467](https://github.com/sgl-project/sglang/pull/25467) | merged | [Quantization] Update error message strings with correct framework name in Quark/compressed-tensors | `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`, `python/sglang/srt/layers/quantization/quark/utils.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-07-09 | [#25694](https://github.com/sgl-project/sglang/pull/25694) | merged | [Quantization][Bugfix]: Join multi-arg RuntimeError in Quark _check_scheme_supported | `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-07-14 | [#30786](https://github.com/sgl-project/sglang/pull/30786) | merged | [Kernel] Migrate scattered MoE kernels to sglang.kernels (RFC #29630, Phase 2.5, 2/7) | `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` |
| 2026-07-21 | [#28291](https://github.com/sgl-project/sglang/pull/28291) | merged | [AMD][MXFP4] Reland "Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs" | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-08-01 | [#33090](https://github.com/sgl-project/sglang/pull/33090) | merged | [AMD][Fix] Restore aiter-padded MoE weight dims for serialized checkpoints | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-08-18 | [#35200](https://github.com/sgl-project/sglang/pull/35200) | merged | [AMD] Fix Quark Shared Experts Fusion Gate after load-time-override Removal | `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-08-24 | [#36124](https://github.com/sgl-project/sglang/pull/36124) | merged | [AMD] Quark shared-experts gate: recognise a trailing MTP layer | `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-09-12 | [#37254](https://github.com/sgl-project/sglang/pull/37254) | merged | [AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj | `test/registered/unit/layers/quantization/test_quark_utils.py` |
| 2026-09-13 | [#37564](https://github.com/sgl-project/sglang/pull/37564) | merged | [AMD][Fix] Fix aiter bpreshuffle GEMM for output sizes it cannot dispatch for qwen3.5 mxfp-attn-fp8-v2 TP4 | `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` |
| 2026-09-16 | [#39155](https://github.com/sgl-project/sglang/pull/39155) | merged | [AMD] GLM-5.2 NextN: cast draft fused MoE to per-channel FP8 | `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` |
| 2026-09-22 | [#38546](https://github.com/sgl-project/sglang/pull/38546) | merged | [AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950 | `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-09-22 | [#39317](https://github.com/sgl-project/sglang/pull/39317) | merged | [AMD] [GLM-5.3-Flash Day 0] Honor fused and per-expert names in quark `exclude` | `test/registered/unit/layers/quantization/test_quark_utils.py`, `python/sglang/srt/layers/quantization/quark/utils.py` |
| 2026-09-29 | [#41464](https://github.com/sgl-project/sglang/pull/41464) | merged | [AMD] Fix GLM-5.3 quark MoE MI35x test runner config | `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` |
| 2026-09-29 | [#28734](https://github.com/sgl-project/sglang/pull/28734) | merged | [AMD] Fix Load and Inference of MLA models with Quark PTPC FP8 attention on ROCm | `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` |
| 2026-09-29 | [#40980](https://github.com/sgl-project/sglang/pull/40980) | merged | [Fix] MoE: require TopK layer_id to ensure routed expert captures | `python/sglang/srt/models/mixtral.py` |
| 2026-09-30 | [#41807](https://github.com/sgl-project/sglang/pull/41807) | merged | [Fix] Shard MoE WNA16 and Quark INT4-FP8 weights by the MoE placement | `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` |
| 2026-10-01 | [#40811](https://github.com/sgl-project/sglang/pull/40811) | merged | [AMD][Quark] Serve the Kimi-K3 MXFP4 checkpoint on ROCm | `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` |
| 2026-10-03 | [#41870](https://github.com/sgl-project/sglang/pull/41870) | merged | [AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4 | `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-10-07 | [#34540](https://github.com/sgl-project/sglang/pull/34540) | merged | [AMD] Fix Quark W4A4 MXFP4 MoE clamped-SwiGLU on the AITER path | `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-10-08 | [#41134](https://github.com/sgl-project/sglang/pull/41134) | merged | [AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950 | `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` |
| 2026-10-09 | [#31054](https://github.com/sgl-project/sglang/pull/31054) | merged | [AMD] Support Quark DeepSeek-V4-MXFP4 checkpoints on the DSV4 stack, enabling shared-expert fusion and MTP | `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-10-12 | [#41980](https://github.com/sgl-project/sglang/pull/41980) | merged | [AMD] Recalibrate test_quark_mxfp4 GSM8K thresholds to observed MI355X noise | `test/registered/e2e/quantization/test_quark_mxfp4.py` |
| 2026-10-20 | [#45365](https://github.com/sgl-project/sglang/pull/45365) | merged | [Fix] [AMD] gpt-oss: support EP for gfx1250 W4A8 MXFP4 MoE | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` |
| 2026-10-20 | [#44993](https://github.com/sgl-project/sglang/pull/44993) | merged | [Refactor] moe: Derive layer contracts from the selected quant method | `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/mixtral.py` |
| 2026-10-21 | [#39598](https://github.com/sgl-project/sglang/pull/39598) | merged | [Perf] [AMD] quark: Add opt-in AITER ASM FP4 GEMM for Quark dense linear | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py` |
| 2026-10-23 | [#40776](https://github.com/sgl-project/sglang/pull/40776) | merged | [Fix] [AMD] Quark: fix Quark block-FP8 loading in DeepSeek loader | `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py` |
| 2026-10-26 | [#41899](https://github.com/sgl-project/sglang/pull/41899) | merged | [Perf] [AMD] quark/Qwen3.8: Quantize the BF16 shared expert of Quark MXFP4 checkpoints to MXFP4 while loading for shared-expert fusion | `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-10-29 | [#45802](https://github.com/sgl-project/sglang/pull/45802) | merged | [Fix] [AMD] quark: Skip no-copy loads after MXFP4 quantization | `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-10-29 | [#41389](https://github.com/sgl-project/sglang/pull/41389) | merged | [Feat] [AMD] Quark: Run Quark MXFP4 MoE as W4A16 via triton_kernels on RDNA (gfx1151) | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-10-30 | [#46800](https://github.com/sgl-project/sglang/pull/46800) | merged | [Fix] [AMD] quark: Keep MXFP8 shared experts out of the MXFP4 fused slot on dense-first models | `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py` |
| 2026-10-31 | [#47408](https://github.com/sgl-project/sglang/pull/47408) | merged | [Fix] [AMD] quark: Fix the EP>1 crash in the Quark MXFP4 W4A16 MoE path and restrict it to gfx1151 | `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-10-31 | [#37367](https://github.com/sgl-project/sglang/pull/37367) | merged | [Perf] [AMD] moe: Resolve MoRI dispatch from the AITER activation contract | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` |
| 2026-11-02 | [#45332](https://github.com/sgl-project/sglang/pull/45332) | merged | [Fix] [AMD] quark: Load MXFP4 MoE checkpoints on gfx95 and gfx1250 without SGLANG_USE_AITER | `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |
| 2026-11-02 | [#41639](https://github.com/sgl-project/sglang/pull/41639) | merged | [Feat] [AMD] moe: Add native GLM MXFP4 Triton Gluon backend | `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` |

## 逐 PR diff 审计卡

### PR #460 - port fp8 mixtral

- 链接: https://github.com/sgl-project/sglang/pull/460
- 状态/时间: merged / 2024-05-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`, `python/sglang/srt/models/mixtral_quant.py`；关联提交 `0fafc5606b0d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+636/-121，可读 patch 921 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「port fp8 mixtral」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/mixtral_quant.py`, `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「port fp8 mixtral」；主要实现面是 `python/sglang/srt/models/mixtral_quant.py`, `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral_quant.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: MixtralMLP, __init__, forward, MixtralMoE，涉及 `MixtralMLP, __init__, forward`；`python/sglang/srt/models/mixtral.py` modified +240/-101 (341 lines); hunks: -1,5 +1,5; -8,131 +8,226; symbols: MixtralMLP, __init__, forward, MixtralMoE，涉及 `MixtralMLP, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral_quant.py` added +371/-0 (371 lines); hunks: -0,0 +1,371; symbols: MixtralMLP, __init__, forward, MixtralMoE
  - `python/sglang/srt/models/mixtral.py` modified +240/-101 (341 lines); hunks: -1,5 +1,5; -8,131 +8,226; symbols: MixtralMLP, __init__, forward, MixtralMoE
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral_quant.py
@@ -0,0 +1,371 @@
+# Adapted from
+# https://github.com/vllm-project/vllm/blob/c7f2cf2b7f67bce5842fedfdba508440fe257375/vllm/model_executor/models/mixtral_quant.py#L1
+"""Inference-only Mixtral model."""
+from typing import Iterable, Optional, Tuple
+import numpy as np
+import torch
diff -- python/sglang/srt/models/mixtral.py
@@ -1,5 +1,5 @@
-# https://github.com/vllm-project/vllm/blob/c7f2cf2b7f67bce5842fedfdba508440fe257375/vllm/model_executor/models/mixtral_quant.py#L1
+# https://github.com/vllm-project/vllm/blob/c7f2cf2b7f67bce5842fedfdba508440fe257375/vllm/model_executor/models/mixtral.py#L1
@@ -8,131 +8,226 @@
+from vllm import _custom_ops as ops
+from vllm.model_executor.layers.fused_moe import fused_moe
+from vllm.model_executor.layers.quantization.fp8 import Fp8Config
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral_quant.py` added +371/-0; `python/sglang/srt/models/mixtral.py` modified +240/-101
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/managers/router/model_rpc.py`, `python/sglang/srt/managers/router/model_runner.py`, `python/sglang/srt/models/mixtral.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #1081 - Update the mixtral to use the better FusedMoE layer

- 链接: https://github.com/sgl-project/sglang/pull/1081
- 状态/时间: merged / 2024-08-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`, `python/sglang/srt/models/mixtral_quant.py`；关联提交 `ad3e4f16199a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+57/-258，可读 patch 515 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update the mixtral to use the better FusedMoE layer」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/mixtral.py`, `python/sglang/srt/models/mixtral_quant.py`；技术摘要: 覆盖「Update the mixtral to use the better FusedMoE layer」；主要实现面是 `python/sglang/srt/models/mixtral.py`, `python/sglang/srt/models/mixtral_quant.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +55/-253 (308 lines); hunks: -18,34 +18,25; -69,216 +60,44 @@ def __init__(; symbols: __init__, weight_loader, process_weights_after_loading, forward，涉及 `__init__, weight_loader, process_weights_after_loading`；`python/sglang/srt/models/mixtral_quant.py` modified +0/-3 (3 lines); hunks: -160,7 +160,6 @@ def __init__(; -183,7 +182,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +55/-253 (308 lines); hunks: -18,34 +18,25; -69,216 +60,44 @@ def __init__(; symbols: __init__, weight_loader, process_weights_after_loading, forward
  - `python/sglang/srt/models/mixtral_quant.py` modified +0/-3 (3 lines); hunks: -160,7 +160,6 @@ def __init__(; -183,7 +182,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -18,34 +18,25 @@
-import numpy as np
-import torch.nn.functional as F
-from vllm import _custom_ops as ops
-from vllm.distributed import (
-    get_tensor_model_parallel_rank,
-    get_tensor_model_parallel_world_size,
diff -- python/sglang/srt/models/mixtral_quant.py
@@ -160,7 +160,6 @@ def __init__(
-        sliding_window: Optional[int] = None,
@@ -183,7 +182,6 @@ def __init__(
-        self.sliding_window = sliding_window
@@ -246,7 +244,6 @@ def __init__(
-            sliding_window=config.sliding_window,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +55/-253; `python/sglang/srt/models/mixtral_quant.py` modified +0/-3
- 验证与风险: diff 自带测试面 `test/srt/test_moe_serving_throughput.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #1290 - fix: resolve fp8 for mixtral

- 链接: https://github.com/sgl-project/sglang/pull/1290
- 状态/时间: merged / 2024-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `9b0805242eea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: resolve fp8 for mixtral」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「fix: resolve fp8 for mixtral」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +1/-1 (2 lines); hunks: -362,7 +362,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +1/-1 (2 lines); hunks: -362,7 +362,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -362,7 +362,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-                        weight_name,
+                        name,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/mixtral.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #1418 - Add torchao quant for mixtral and qwen_moe

- 链接: https://github.com/sgl-project/sglang/pull/1418
- 状态/时间: merged / 2024-09-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `30b404ce72b5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+50/-20，可读 patch 138 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add torchao quant for mixtral and qwen_moe」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「Add torchao quant for mixtral and qwen_moe」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +5/-0 (5 lines); hunks: -41,6 +41,8; -296,6 +298,7 @@ def __init__(; symbols: __init__, load_weights，涉及 `__init__, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +5/-0 (5 lines); hunks: -41,6 +41,8; -296,6 +298,7 @@ def __init__(; symbols: __init__, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -41,6 +41,8 @@
+from sglang.srt.layers.torchao_utils import apply_torchao_config_
+from sglang.srt.managers.schedule_batch import global_server_args_dict
@@ -296,6 +298,7 @@ def __init__(
+        self.torchao_config = global_server_args_dict["torchao_config"]
@@ -376,5 +379,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+        apply_torchao_config_(self, params_dict, set(["proj.weight"]))
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +5/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/torchao_utils.py`, `python/sglang/srt/models/llama.py`, `python/sglang/srt/models/mixtral.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #1835 - [FP8 KV Cache, Mixtral] Avoid KeyError at loading pre-quantized FP8 m…

- 链接: https://github.com/sgl-project/sglang/pull/1835
- 状态/时间: merged / 2024-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `54dd3ea12277`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-0，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[FP8 KV Cache, Mixtral] Avoid KeyError at loading pre-quantized FP8 m…」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[FP8 KV Cache, Mixtral] Avoid KeyError at loading pre-quantized FP8 m…」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +3/-0 (3 lines); hunks: -369,6 +369,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +3/-0 (3 lines); hunks: -369,6 +369,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -369,6 +369,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+                    # Skip loading kv_scale from ckpts towards new design.
+                    if name.endswith(".kv_scale") and name not in params_dict:
+                        continue
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/mixtral.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #2156 - feat: update other MoE models deps

- 链接: https://github.com/sgl-project/sglang/pull/2156
- 状态/时间: merged / 2024-11-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `e3938b2f9c96`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+28/-14，可读 patch 162 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: update other MoE models deps」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「feat: update other MoE models deps」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +1/-1 (2 lines); hunks: -22,7 +22,6; -36,6 +35,7。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +1/-1 (2 lines); hunks: -22,7 +22,6; -36,6 +35,7
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -22,7 +22,6 @@
-from vllm.model_executor.layers.fused_moe import FusedMoE
@@ -36,6 +35,7 @@
+from sglang.srt.layers.triton_fused_moe import FusedMoE
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/fused_moe/layer.py`, `python/sglang/srt/layers/triton_fused_moe/fused_moe.py`, `python/sglang/srt/layers/triton_fused_moe/layer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #2163 - Rename triton_fused_moe -> fused_moe_triton

- 链接: https://github.com/sgl-project/sglang/pull/2163
- 状态/时间: merged / 2024-11-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `be0124bda09d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 76 个文件，+19/-19，可读 patch 199 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Rename triton_fused_moe -> fused_moe_triton」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「Rename triton_fused_moe -> fused_moe_triton」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +1/-1 (2 lines); hunks: -25,6 +25,7; -35,7 +36,6。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +1/-1 (2 lines); hunks: -25,6 +25,7; -35,7 +36,6
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -25,6 +25,7 @@
+from sglang.srt.layers.fused_moe_triton import FusedMoE
@@ -35,7 +36,6 @@
-from sglang.srt.layers.triton_fused_moe import FusedMoE
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/fused_moe/__init__.py`, `python/sglang/srt/layers/fused_moe_grok/__init__.py`, `python/sglang/srt/layers/fused_moe_grok/configs/E=8,N=4096,device_name=AMD_Instinct_MI300X,dtype=float8.json`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #2300 - Fix gptq for moe layers

- 链接: https://github.com/sgl-project/sglang/pull/2300
- 状态/时间: merged / 2024-12-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `1228f7ca69e6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+44/-2，可读 patch 78 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix gptq for moe layers」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「Fix gptq for moe layers」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +10/-2 (12 lines); hunks: -339,7 +339,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; -353,6 +355,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +10/-2 (12 lines); hunks: -339,7 +339,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Te...; -353,6 +355,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -339,7 +339,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-                if name.endswith(".bias") and name not in params_dict:
+                if (
+                    name.endswith(".bias") or name.endswith("_bias")
+                ) and name not in params_dict:
@@ -353,6 +355,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+                    if (
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +10/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/models/mixtral.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #2371 - MoE Expert Parallel

- 链接: https://github.com/sgl-project/sglang/pull/2371
- 状态/时间: merged / 2024-12-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `3d32e4a32c4c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+1172/-8，可读 patch 1320 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「MoE Expert Parallel」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「MoE Expert Parallel」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +13/-5 (18 lines); hunks: -21,9 +21,13; -38,6 +42,7; symbols: __init__, forward, load_weights，涉及 `__init__, forward, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +13/-5 (18 lines); hunks: -21,9 +21,13; -38,6 +42,7; symbols: __init__, forward, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -21,9 +21,13 @@
-from vllm.distributed import get_tensor_model_parallel_world_size
+from vllm.distributed import (
+    get_tensor_model_parallel_world_size,
+    tensor_model_parallel_all_reduce,
+)
+from sglang.srt.layers.ep_moe.layer import EPMoE
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +13/-5
- 验证与风险: diff 自带测试面 `test/srt/test_moe_ep.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #2563 - Reorg moe code

- 链接: https://github.com/sgl-project/sglang/pull/2563
- 状态/时间: merged / 2024-12-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `e835a50021e0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 88 个文件，+338/-344，可读 patch 1108 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Reorg moe code」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「Reorg moe code」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +2/-2 (4 lines); hunks: -27,15 +27,15。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +2/-2 (4 lines); hunks: -27,15 +27,15
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -27,15 +27,15 @@
-from sglang.srt.layers.ep_moe.layer import EPMoE
-from sglang.srt.layers.fused_moe_triton import FusedMoE
+from sglang.srt.layers.moe.ep_moe.layer import EPMoE
+from sglang.srt.layers.moe.fused_moe_triton import FusedMoE
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +2/-2
- 验证与风险: diff 自带测试面 `test/srt/test_fused_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #6223 - [PP] Fix init_memory_pool desync & add PP for mixtral

- 链接: https://github.com/sgl-project/sglang/pull/6223
- 状态/时间: merged / 2025-05-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `bad7c26fdc7f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+179/-47，可读 patch 391 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[PP] Fix init_memory_pool desync & add PP for mixtral」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[PP] Fix init_memory_pool desync & add PP for mixtral」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +98/-34 (132 lines); hunks: -16,13 +16,15; -38,14 +40,17; symbols: MixtralMoE, __init__, forward，涉及 `MixtralMoE, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +98/-34 (132 lines); hunks: -16,13 +16,15; -38,14 +40,17; symbols: MixtralMoE, __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -16,13 +16,15 @@
-from typing import Iterable, Optional, Tuple
+import logging
+from typing import Iterable, Optional, Tuple, Union
+    get_pp_group,
@@ -38,14 +40,17 @@
+from sglang.srt.layers.utils import PPMissingLayer, get_layer_id
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +98/-34
- 验证与风险: diff 自带测试面 `test/srt/test_bench_serving.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #7966 - [1/N] MoE Refactor: refactor `select_experts`

- 链接: https://github.com/sgl-project/sglang/pull/7966
- 状态/时间: merged / 2025-07-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `15ad6c908670`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 39 个文件，+557/-872，可读 patch 2848 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[1/N] MoE Refactor: refactor `select_experts`」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[1/N] MoE Refactor: refactor `select_experts`」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +9/-2 (11 lines); hunks: -37,6 +37,7; -86,14 +87,19 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +9/-2 (11 lines); hunks: -37,6 +37,7; -86,14 +87,19 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -37,6 +37,7 @@
+from sglang.srt.layers.moe.topk import TopK
@@ -86,14 +87,19 @@ def __init__(
+        self.topk = TopK(
+            top_k=top_k,
+            renormalize=True,
+        )
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +9/-2
- 验证与风险: diff 自带测试面 `python/sglang/test/test_block_fp8.py`, `python/sglang/test/test_block_fp8_ep.py`, `python/sglang/test/test_cutlass_w4a8_moe.py`, `python/sglang/test/test_fp4_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #8448 - Support EPLB in FusedMoE

- 链接: https://github.com/sgl-project/sglang/pull/8448
- 状态/时间: merged / 2025-07-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `9effeb5bddf2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+107/-11，可读 patch 407 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support EPLB in FusedMoE」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「Support EPLB in FusedMoE」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +3/-0 (3 lines); hunks: -69,6 +69,7 @@ def __init__(; -97,6 +98,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +3/-0 (3 lines); hunks: -69,6 +69,7 @@ def __init__(; -97,6 +98,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -69,6 +69,7 @@ def __init__(
+        layer_id: int,
@@ -97,6 +98,7 @@ def __init__(
+            layer_id=layer_id,
@@ -226,6 +228,7 @@ def __init__(
+            layer_id=layer_id,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/expert_location_dispatch.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #8658 - [5/N] MoE Refactor: Update MoE parallelism arguments

- 链接: https://github.com/sgl-project/sglang/pull/8658
- 状态/时间: merged / 2025-08-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `6c88f6c8d908`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 38 个文件，+342/-299，可读 patch 1748 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[5/N] MoE Refactor: Update MoE parallelism arguments」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[5/N] MoE Refactor: Update MoE parallelism arguments」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +3/-3 (6 lines); hunks: -24,6 +24,7; -94,7 +95,7 @@ def __init__(; symbols: __init__, load_weights，涉及 `__init__, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +3/-3 (6 lines); hunks: -24,6 +24,7; -94,7 +95,7 @@ def __init__(; symbols: __init__, load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -24,6 +24,7 @@
+    get_moe_expert_parallel_world_size,
@@ -94,7 +95,7 @@ def __init__(
-        MoEImpl = EPMoE if global_server_args_dict["enable_ep_moe"] else FusedMoE
+        MoEImpl = EPMoE if get_moe_expert_parallel_world_size() > 1 else FusedMoE
@@ -398,8 +399,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-        MoEImpl = EPMoE if global_server_args_dict["enable_ep_moe"] else FusedMoE
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +3/-3
- 验证与风险: diff 自带测试面 `python/sglang/test/runners.py`, `test/srt/test_deepep_large.py`, `test/srt/test_deepep_small.py`, `test/srt/test_eplb.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #8849 - [6/N] MoE Refactor: Cleanup MoE-related configs

- 链接: https://github.com/sgl-project/sglang/pull/8849
- 状态/时间: merged / 2025-08-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `295895120df4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 69 个文件，+958/-1039，可读 patch 4640 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[6/N] MoE Refactor: Cleanup MoE-related configs」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[6/N] MoE Refactor: Cleanup MoE-related configs」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +0/-2 (2 lines); hunks: -47,7 +47,6; -104,7 +103,6 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +0/-2 (2 lines); hunks: -47,7 +47,6; -104,7 +103,6 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -47,7 +47,6 @@
-from sglang.srt.managers.schedule_batch import global_server_args_dict
@@ -104,7 +103,6 @@ def __init__(
-            tp_size=tp_size,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +0/-2
- 验证与风险: diff 自带测试面 `python/sglang/test/test_block_fp8.py`, `python/sglang/test/test_block_fp8_ep.py`, `python/sglang/test/test_cutlass_w4a8_moe.py`, `python/sglang/test/test_fp4_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #11211 - [8/N] MoE Refactor: deprecate `EPMoE`

- 链接: https://github.com/sgl-project/sglang/pull/11211
- 状态/时间: merged / 2025-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `3c06b673aff9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 19 个文件，+496/-1778，可读 patch 2897 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[8/N] MoE Refactor: deprecate `EPMoE`」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[8/N] MoE Refactor: deprecate `EPMoE`」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +1/-3 (4 lines); hunks: -36,7 +36,6; -94,8 +93,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +1/-3 (4 lines); hunks: -36,7 +36,6; -94,8 +93,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -36,7 +36,6 @@
-from sglang.srt.layers.moe.ep_moe.layer import EPMoE
@@ -94,8 +93,7 @@ def __init__(
-        MoEImpl = EPMoE if get_moe_expert_parallel_world_size() > 1 else FusedMoE
-        self.experts = MoEImpl(
+        self.experts = FusedMoE(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +1/-3
- 验证与风险: diff 自带测试面 `python/sglang/test/test_block_fp8_ep.py`, `python/sglang/test/test_cutlass_w4a8_moe.py`, `test/srt/ep/test_moe_ep.py`, `test/srt/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #10485 - [Quantization] Support Quark Dense + MoE FP8 & FP8 PTPC

- 链接: https://github.com/sgl-project/sglang/pull/10485
- 状态/时间: merged / 2025-11-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；关联提交 `67e9d287eea0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+666/-243，可读 patch 1041 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Quantization] Support Quark Dense + MoE FP8 & FP8 PTPC」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[Quantization] Support Quark Dense + MoE FP8 & FP8 PTPC」；主要实现面是 `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/fp8_utils.py` modified +116/-220 (336 lines); hunks: -604,158 +604,16 @@ def apply_fp8_linear(; -783,87 +641,125 @@ def apply_fp8_linear(; symbols: apply_fp8_linear, can_auto_enable_marlin_fp8，涉及 `apply_fp8_linear, can_auto_enable_marlin_fp8`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: QuarkW8A8Fp8, __init__, get_min_capability, process_weights_after_loading，涉及 `QuarkW8A8Fp8, __init__, get_min_capability`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +42/-1 (43 lines); hunks: -14,7 +14,11; -173,6 +177,37 @@ def _check_scheme_supported(self, min_capability: int, erro...; symbols: _check_scheme_supported, _is_fp8_w8a8, _is_mx_fp4, _get_scheme_from_config，涉及 `_check_scheme_supported, _is_fp8_w8a8, _is_mx_fp4`；`python/sglang/srt/layers/quantization/__init__.py` modified +3/-11 (14 lines); hunks: -35,6 +35,7 @@ def override_quantization_method(self, *args, **kwargs):; -65,23 +66,14 @@ def override_quantization_method(self, *args, **kwargs):; symbols: override_quantization_method，涉及 `override_quantization_method`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/fp8_utils.py` modified +116/-220 (336 lines); hunks: -604,158 +604,16 @@ def apply_fp8_linear(; -783,87 +641,125 @@ def apply_fp8_linear(; symbols: apply_fp8_linear, can_auto_enable_marlin_fp8
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: QuarkW8A8Fp8, __init__, get_min_capability, process_weights_after_loading
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +42/-1 (43 lines); hunks: -14,7 +14,11; -173,6 +177,37 @@ def _check_scheme_supported(self, min_capability: int, erro...; symbols: _check_scheme_supported, _is_fp8_w8a8, _is_mx_fp4, _get_scheme_from_config
  - `python/sglang/srt/layers/quantization/__init__.py` modified +3/-11 (14 lines); hunks: -35,6 +35,7 @@ def override_quantization_method(self, *args, **kwargs):; -65,23 +66,14 @@ def override_quantization_method(self, *args, **kwargs):; symbols: override_quantization_method
  - `python/sglang/srt/layers/quantization/quark/utils.py` modified +11/-1 (12 lines); hunks: -6,7 +6,17; symbols: raise_aiter_import_error
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/fp8_utils.py
@@ -604,158 +604,16 @@ def apply_fp8_linear(
-        # cutlass_scaled_mm supports per tensor/channel W and per tensor/token A
-        # for sgl-kernel fp8_scaled_mm, it support per channel W now
+        # Maybe apply padding to output, see comment in __init__
+        num_token_padding = output_padding
-            qinput, x_scale = scaled_fp8_quant(
-                input_2d,
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py
@@ -0,0 +1,186 @@
+# SPDX-License-Identifier: Apache-2.0
+from typing import Any, Callable, Optional, cast
+import torch
+from torch.nn import Parameter
+from sglang.srt.layers.parameter import (
+    ChannelQuantScaleParameter,
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -14,7 +14,11 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/fp8_utils.py` modified +116/-220; `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` added +186/-0; `python/sglang/srt/layers/quantization/quark/quark.py` modified +42/-1; `python/sglang/srt/layers/quantization/__init__.py` modified +3/-11; `python/sglang/srt/layers/quantization/quark/utils.py` modified +11/-1; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +8/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13667 - [Piecewise CUDA Graph] Fix recompile issue for Mixtral and Grok2

- 链接: https://github.com/sgl-project/sglang/pull/13667
- 状态/时间: merged / 2025-11-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `b5344b31b8f1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+24/-160，可读 patch 315 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Piecewise CUDA Graph] Fix recompile issue for Mixtral and Grok2」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[Piecewise CUDA Graph] Fix recompile issue for Mixtral and Grok2」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +1/-0 (1 lines); hunks: -353,6 +353,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +1/-0 (1 lines); hunks: -353,6 +353,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -353,6 +353,7 @@ def __init__(
+    @torch.no_grad()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/grok.py`, `python/sglang/srt/models/mixtral.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13147 - Aiter fp8 kv cache

- 链接: https://github.com/sgl-project/sglang/pull/13147
- 状态/时间: merged / 2025-12-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`；关联提交 `c106b54b57d8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+594/-96，可读 patch 1032 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Aiter fp8 kv cache」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「Aiter fp8 kv cache」；主要实现面是 `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/quark.py` modified +2/-0 (2 lines); hunks: -71,6 +71,8 @@ def get_quant_method(; symbols: get_quant_method，涉及 `get_quant_method`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +2/-0 (2 lines); hunks: -71,6 +71,8 @@ def get_quant_method(; symbols: get_quant_method
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -71,6 +71,8 @@ def get_quant_method(
+            elif isinstance(layer, RadixAttention):
+                return QuarkKVCacheMethod(self)
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7392 - [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm

- 链接: https://github.com/sgl-project/sglang/pull/7392
- 状态/时间: merged / 2026-01-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；关联提交 `5af84c8af554`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+615/-15，可读 patch 759 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；技术摘要: 覆盖「[AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm」；主要实现面是 `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` added +443/-0 (443 lines); hunks: -0,0 +1,443; symbols: tqdm_reset_no_print, QuarkInt4Fp8Config, for, __init__，涉及 `tqdm_reset_no_print, QuarkInt4Fp8Config, for`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` added +443/-0 (443 lines); hunks: -0,0 +1,443; symbols: tqdm_reset_no_print, QuarkInt4Fp8Config, for, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark_int4fp8_moe.py
@@ -0,0 +1,443 @@
+import logging
+from typing import TYPE_CHECKING, Any, Dict, List, Optional
+import torch
+from tqdm import tqdm
+from tqdm.std import EMA
+from sglang.srt.distributed import get_tensor_model_parallel_rank
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` added +443/-0
- 验证与风险: diff 自带测试面 `test/srt/run_suite.py`, `test/srt/test_int4fp8_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #18252 - [4/N] Quantization Refactor: Quark MoE schemes

- 链接: https://github.com/sgl-project/sglang/pull/18252
- 状态/时间: merged / 2026-02-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` 等 7 个文件；关联提交 `150ed881be2c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+396/-243，可读 patch 835 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[4/N] Quantization Refactor: Quark MoE schemes」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[4/N] Quantization Refactor: Quark MoE schemes」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` renamed +5/-221 (226 lines); hunks: -9,248 +9,32; -479,7 +263,7 @@ def create_moe_runner(; symbols: QuarkMoEMethod, __init__, get_moe_method, QuarkW4A4MXFp4MoEMethod，涉及 `QuarkMoEMethod, __init__, get_moe_method`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` added +213/-0 (213 lines); hunks: -0,0 +1,213; symbols: QuarkW4A4MXFp4MoE, __init__, get_min_capability, create_weights，涉及 `QuarkW4A4MXFp4MoE, __init__, get_min_capability`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +96/-10 (106 lines); hunks: -2,29 +2,36; -77,7 +84,7 @@ def get_quant_method(; symbols: get_quant_method, _find_matched_config, _get_scheme_from_config，涉及 `get_quant_method, _find_matched_config, _get_scheme_from_config`；`python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py` modified +65/-4 (69 lines); hunks: -1,14 +1,20; -30,6 +36,14 @@ def create_weights(self, *args, **kwargs):; symbols: QuarkScheme, QuarkLinearScheme, used, create_weights，涉及 `QuarkScheme, QuarkLinearScheme, used`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` renamed +5/-221 (226 lines); hunks: -9,248 +9,32; -479,7 +263,7 @@ def create_moe_runner(; symbols: QuarkMoEMethod, __init__, get_moe_method, QuarkW4A4MXFp4MoEMethod
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` added +213/-0 (213 lines); hunks: -0,0 +1,213; symbols: QuarkW4A4MXFp4MoE, __init__, get_min_capability, create_weights
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +96/-10 (106 lines); hunks: -2,29 +2,36; -77,7 +84,7 @@ def get_quant_method(; symbols: get_quant_method, _find_matched_config, _get_scheme_from_config
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py` modified +65/-4 (69 lines); hunks: -1,14 +1,20; -30,6 +36,14 @@ def create_weights(self, *args, **kwargs):; symbols: QuarkScheme, QuarkLinearScheme, used, create_weights
  - `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` modified +11/-2 (13 lines); hunks: -1,7 +1,16
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py
@@ -9,248 +9,32 @@
-from sglang.srt.layers.quantization.base_config import FusedMoEMethodBase
+from sglang.srt.layers.quantization.quark.schemes import QuarkMoEScheme
-from sglang.srt.utils import (
-    get_bool_env_var,
-    is_gfx95_supported,
-    is_hip,
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -0,0 +1,213 @@
+# SPDX-License-Identifier: Apache-2.0
+from __future__ import annotations
+import logging
+from typing import TYPE_CHECKING, Any
+import torch
+from sglang.srt.layers.moe import MoeRunnerConfig
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -2,29 +2,36 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` renamed +5/-221; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` added +213/-0; `python/sglang/srt/layers/quantization/quark/quark.py` modified +96/-10; `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py` modified +65/-4; `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` modified +11/-2; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19422 - [AMD] Use fused GEMM with FP8 cast for FP8 prefill

- 链接: https://github.com/sgl-project/sglang/pull/19422
- 状态/时间: merged / 2026-02-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`；关联提交 `5172c378456f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+73/-20，可读 patch 194 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Use fused GEMM with FP8 cast for FP8 prefill」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`；技术摘要: 覆盖「[AMD] Use fused GEMM with FP8 cast for FP8 prefill」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +30/-5 (35 lines); hunks: -10,6 +10,9; -87,20 +90,29 @@ def apply_weights(; symbols: apply_weights，涉及 `apply_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +30/-5 (35 lines); hunks: -10,6 +10,9; -87,20 +90,29 @@ def apply_weights(; symbols: apply_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py
@@ -10,6 +10,9 @@
+    from aiter.ops.triton.gemm.fused.fused_gemm_afp4wfp4_split_cat import (
+        fused_gemm_afp4wfp4_split_cat,
+    )
@@ -87,20 +90,29 @@ def apply_weights(
+        fused_gemm_split_cat = False
-            ], "For tuple input, only (x, x_s) or (x, x_s, y) formats are accepted"
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +30/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18684 - [AMD] Add MoE weights and scales padding

- 链接: https://github.com/sgl-project/sglang/pull/18684
- 状态/时间: merged / 2026-03-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `941945371314`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+131/-36，可读 patch 388 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add MoE weights and scales padding」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[AMD] Add MoE weights and scales padding」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +23/-5 (28 lines); hunks: -8,6 +8,7; -73,10 +74,20 @@ def create_weights(; symbols: create_weights，涉及 `create_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +23/-5 (28 lines); hunks: -8,6 +8,7; -73,10 +74,20 @@ def create_weights(; symbols: create_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -8,6 +8,7 @@
+from sglang.srt.layers.moe.utils import get_moe_weight_sizes
@@ -73,10 +74,20 @@ def create_weights(
+        w13_up_dim, w2_down_dim, weight_padded = get_moe_weight_sizes(
+            intermediate_size_per_partition,
+            is_aiter_moe=True,
+            is_concat=True,
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +23/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21067 - Revert "[AMD] Add MoE weights and scales padding"

- 链接: https://github.com/sgl-project/sglang/pull/21067
- 状态/时间: merged / 2026-03-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `048d90e1651a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+36/-131，可读 patch 388 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[AMD] Add MoE weights and scales padding"」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「Revert "[AMD] Add MoE weights and scales padding"」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +5/-23 (28 lines); hunks: -8,7 +8,6; -74,20 +73,10 @@ def create_weights(; symbols: create_weights，涉及 `create_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +5/-23 (28 lines); hunks: -8,7 +8,6; -74,20 +73,10 @@ def create_weights(; symbols: create_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -8,7 +8,6 @@
-from sglang.srt.layers.moe.utils import get_moe_weight_sizes
@@ -74,20 +73,10 @@ def create_weights(
-        w13_up_dim, w2_down_dim, weight_padded = get_moe_weight_sizes(
-            intermediate_size_per_partition,
-            is_aiter_moe=True,
-            is_concat=True,
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +5/-23
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21040 - [AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype.

- 链接: https://github.com/sgl-project/sglang/pull/21040
- 状态/时间: merged / 2026-03-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `61a902ce88ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+90/-54，可读 patch 331 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype.」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype.」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +4/-0 (4 lines); hunks: -160,6 +160,10 @@ def process_weights_after_loading(self, layer: torch.nn.Mod...; symbols: process_weights_after_loading, create_moe_runner，涉及 `process_weights_after_loading, create_moe_runner`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +4/-0 (4 lines); hunks: -160,6 +160,10 @@ def process_weights_after_loading(self, layer: torch.nn.Mod...; symbols: process_weights_after_loading, create_moe_runner
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -160,6 +160,10 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
+        if hasattr(layer, "dispatcher"):
+            # Weights are stored as torch.uint8 but semantically MXFP4
+            layer.dispatcher.set_quant_config({"weight_dtype": torch.float4_e2m1fn_x2})
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +4/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/test_moriep_small.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21097 - [AMD] Add MoE weights and scales padding

- 链接: https://github.com/sgl-project/sglang/pull/21097
- 状态/时间: merged / 2026-04-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `f4f9e6818916`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+153/-46，可读 patch 432 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add MoE weights and scales padding」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[AMD] Add MoE weights and scales padding」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +20/-5 (25 lines); hunks: -8,6 +8,7; -73,10 +74,20 @@ def create_weights(; symbols: create_weights，涉及 `create_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +20/-5 (25 lines); hunks: -8,6 +8,7; -73,10 +74,20 @@ def create_weights(; symbols: create_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -8,6 +8,7 @@
+from sglang.srt.layers.moe.utils import get_moe_weight_sizes
@@ -73,10 +74,20 @@ def create_weights(
+        w13_up_dim, w2_down_dim, weight_padded = get_moe_weight_sizes(
+            intermediate_size_per_partition,
+            is_aiter_moe=_use_aiter,
+            is_concat=True,
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +20/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23585 - Move expert_mask_gpu from FusedMoE layer to StandardDispatcher

- 链接: https://github.com/sgl-project/sglang/pull/23585
- 状态/时间: merged / 2026-04-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `000a2525e196`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+25/-25，可读 patch 124 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Move expert_mask_gpu from FusedMoE layer to StandardDispatcher」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「Move expert_mask_gpu from FusedMoE layer to StandardDispatcher」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +1/-1 (2 lines); hunks: -227,6 +227,6 @@ def apply_weights(; symbols: apply_weights，涉及 `apply_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +1/-1 (2 lines); hunks: -227,6 +227,6 @@ def apply_weights(; symbols: apply_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -227,6 +227,6 @@ def apply_weights(
-            expert_mask=layer.expert_mask_gpu,
+            expert_mask=layer.dispatcher.expert_mask_gpu,
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py`, `python/sglang/srt/layers/quantization/fp8.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23597 - [MoE] Add Aiter MoE runner backend and purge aiter.fused_moe from quant methods

- 链接: https://github.com/sgl-project/sglang/pull/23597
- 状态/时间: merged / 2026-05-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；关联提交 `108bfd8b6a0d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+316/-251，可读 patch 873 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MoE] Add Aiter MoE runner backend and purge aiter.fused_moe from quant methods」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；技术摘要: 覆盖「[MoE] Add Aiter MoE runner backend and purge aiter.fused_moe from quant methods」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +25/-29 (54 lines); hunks: -7,7 +7,7; -32,8 +32,6; symbols: process_weights_after_loading, create_moe_runner, apply_weights，涉及 `process_weights_after_loading, create_moe_runner, apply_weights`；`python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +25/-22 (47 lines); hunks: -11,7 +11,7; -27,8 +27,6; symbols: process_weights_after_loading, create_moe_runner, apply，涉及 `process_weights_after_loading, create_moe_runner, apply`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +25/-29 (54 lines); hunks: -7,7 +7,7; -32,8 +32,6; symbols: process_weights_after_loading, create_moe_runner, apply_weights
  - `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +25/-22 (47 lines); hunks: -11,7 +11,7; -27,8 +27,6; symbols: process_weights_after_loading, create_moe_runner, apply
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -7,7 +7,7 @@
-from sglang.srt.layers.moe import MoeRunnerConfig
+from sglang.srt.layers.moe import MoeRunner, MoeRunnerBackend, MoeRunnerConfig
@@ -32,8 +32,6 @@
-    from aiter import ActivationType, QuantType
-    from aiter.fused_moe import fused_moe
@@ -182,24 +180,31 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
diff -- python/sglang/srt/layers/quantization/quark_int4fp8_moe.py
@@ -11,7 +11,7 @@
-from sglang.srt.layers.moe import MoeRunnerConfig
+from sglang.srt.layers.moe import MoeRunner, MoeRunnerBackend, MoeRunnerConfig
@@ -27,8 +27,6 @@
-    from aiter import ActivationType, QuantType
-    from aiter.fused_moe import fused_moe
@@ -405,39 +403,44 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +25/-29; `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +25/-22
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23760 - [MoE] Unify DeepEPMoE+MoriEPMoE through AITER MoeRunner pre/post-permute

- 链接: https://github.com/sgl-project/sglang/pull/23760
- 状态/时间: merged / 2026-05-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；关联提交 `be3c425788db`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+398/-330，可读 patch 954 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MoE] Unify DeepEPMoE+MoriEPMoE through AITER MoeRunner pre/post-permute」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；技术摘要: 覆盖「[MoE] Unify DeepEPMoE+MoriEPMoE through AITER MoeRunner pre/post-permute」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +1/-1 (2 lines); hunks: -187,7 +187,7 @@ def create_moe_runner(; symbols: create_moe_runner，涉及 `create_moe_runner`；`python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +1/-1 (2 lines); hunks: -410,7 +410,7 @@ def create_moe_runner(; symbols: create_moe_runner，涉及 `create_moe_runner`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +1/-1 (2 lines); hunks: -187,7 +187,7 @@ def create_moe_runner(; symbols: create_moe_runner
  - `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +1/-1 (2 lines); hunks: -410,7 +410,7 @@ def create_moe_runner(; symbols: create_moe_runner
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -187,7 +187,7 @@ def create_moe_runner(
-        if moe_runner_backend.is_auto() and get_moe_a2a_backend().is_none():
+        if moe_runner_backend.is_auto() and get_moe_a2a_backend().supports_aiter():
diff -- python/sglang/srt/layers/quantization/quark_int4fp8_moe.py
@@ -410,7 +410,7 @@ def create_moe_runner(
-        if moe_runner_backend.is_auto() and get_moe_a2a_backend().is_none():
+        if moe_runner_backend.is_auto() and get_moe_a2a_backend().supports_aiter():
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +1/-1; `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18005 - [AMD][MXFP4] Online MXFP4 quantization 1/N - dense and MOE models w. original BF16 weight

- 链接: https://github.com/sgl-project/sglang/pull/18005
- 状态/时间: merged / 2026-06-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `293816ab14af`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+509/-26，可读 patch 877 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][MXFP4] Online MXFP4 quantization 1/N - dense and MOE models w. original BF16 weight」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`；技术摘要: 覆盖「[AMD][MXFP4] Online MXFP4 quantization 1/N - dense and MOE models w. original BF16 weight」；主要实现面是 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/quark.py` modified +103/-3 (106 lines); hunks: -29,6 +29,8; -40,21 +42,47 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers, get_linear_method，涉及 `QuarkConfig, __init__, quantized_layers`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +77/-10 (87 lines); hunks: -16,6 +16,7; -35,14 +36,25; symbols: QuarkW4A4MXFp4MoE, __init__, get_min_capability，涉及 `QuarkW4A4MXFp4MoE, __init__, get_min_capability`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +68/-6 (74 lines); hunks: -1,12 +1,14; -19,26 +21,43; symbols: QuarkW4A4MXFP4, __init__, get_min_capability, process_weights_after_loading，涉及 `QuarkW4A4MXFP4, __init__, get_min_capability`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +103/-3 (106 lines); hunks: -29,6 +29,8; -40,21 +42,47 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers, get_linear_method
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +77/-10 (87 lines); hunks: -16,6 +16,7; -35,14 +36,25; symbols: QuarkW4A4MXFp4MoE, __init__, get_min_capability
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +68/-6 (74 lines); hunks: -1,12 +1,14; -19,26 +21,43; symbols: QuarkW4A4MXFP4, __init__, get_min_capability, process_weights_after_loading
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -29,6 +29,8 @@
+    from transformers import PretrainedConfig
@@ -40,21 +42,47 @@ class QuarkConfig(QuantizationConfig):
-        quant_config: dict[str, Any],
+        quant_config: Optional[dict[str, Any]] = None,
+        hf_config: "PretrainedConfig | None" = None,
+        is_prequantized: bool = False,
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -16,6 +16,7 @@
+from sglang.srt.utils.common import mxfp_supported
@@ -35,14 +36,25 @@
+if _is_hip:
+    from aiter.ops.triton.quant import dynamic_mxfp4_quant
+else:
+    dynamic_mxfp4_quant = None
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py
@@ -1,12 +1,14 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +103/-3; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +77/-10; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +68/-6
- 验证与风险: diff 自带测试面 `test/registered/quant/test_quark_mxfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27057 - [AMD] move shared expert check function to quark

- 链接: https://github.com/sgl-project/sglang/pull/27057
- 状态/时间: merged / 2026-06-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`；关联提交 `f288283c07a4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+74/-11，可读 patch 131 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] move shared expert check function to quark」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD] move shared expert check function to quark」；主要实现面是 `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/quark.py` modified +44/-0 (44 lines); hunks: -37,6 +37,18; -492,6 +504,38 @@ def get_moe_scheme(; symbols: QuarkConfig, get_moe_scheme, get_scaled_act_names, can_fuse_shared_expert，涉及 `QuarkConfig, get_moe_scheme, get_scaled_act_names`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +44/-0 (44 lines); hunks: -37,6 +37,18; -492,6 +504,38 @@ def get_moe_scheme(; symbols: QuarkConfig, get_moe_scheme, get_scaled_act_names, can_fuse_shared_expert
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -37,6 +37,18 @@
+_MOE_SHARED_EXPERT_QUANT_LAYER0_BASES: tuple[str, ...] = (
+    "model.layers.0",
+    "model.language_model.layers.0",
+)
+_SHARED_EXPERT_BODY_PROJ_SUFFIXES: tuple[str, ...] = (
+    "gate_proj",
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +44/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18182 - [AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs

- 链接: https://github.com/sgl-project/sglang/pull/18182
- 状态/时间: merged / 2026-06-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；关联提交 `3f4a338212b2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+1042/-130，可读 patch 1694 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +374/-28 (402 lines); hunks: -3,12 +3,20; -51,10 +59,12 @@ def __init__(; symbols: __init__, create_weights, get_online_weight_loader，涉及 `__init__, create_weights, get_online_weight_loader`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +214/-33 (247 lines); hunks: -1,11 +1,19; -162,12 +170,14 @@ def __init__(; symbols: __init__, create_weights, get_online_mxfp4_weight_loader, online_mxfp4_weight_loader，涉及 `__init__, create_weights, get_online_mxfp4_weight_loader`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +61/-11 (72 lines); hunks: -14,6 +14,7; -54,13 +55,14 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers，涉及 `QuarkConfig, __init__, quantized_layers`；`python/sglang/srt/layers/quantization/quark/utils.py` modified +4/-0 (4 lines); hunks: -210,5 +210,9 @@ def quark_post_load_weights(self_attn: nn.Module, w: torch.T...; symbols: quark_post_load_weights，涉及 `quark_post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +374/-28 (402 lines); hunks: -3,12 +3,20; -51,10 +59,12 @@ def __init__(; symbols: __init__, create_weights, get_online_weight_loader
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +214/-33 (247 lines); hunks: -1,11 +1,19; -162,12 +170,14 @@ def __init__(; symbols: __init__, create_weights, get_online_mxfp4_weight_loader, online_mxfp4_weight_loader
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +61/-11 (72 lines); hunks: -14,6 +14,7; -54,13 +55,14 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers
  - `python/sglang/srt/layers/quantization/quark/utils.py` modified +4/-0 (4 lines); hunks: -210,5 +210,9 @@ def quark_post_load_weights(self_attn: nn.Module, w: torch.T...; symbols: quark_post_load_weights
  - `python/sglang/srt/layers/quantization/fp8_utils.py` modified +2/-0 (2 lines); hunks: -1216,6 +1216,8 @@ def block_quant_dequant(; symbols: block_quant_dequant
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -3,12 +3,20 @@
+import threading
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
+from sglang.srt.layers.quantization.dequantization import (
+    copy_missing_attrs,
+    dequantize_fp8,
+)
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py
@@ -1,11 +1,19 @@
+import threading
+from sglang.srt.layers.quantization import QuantizationConfig
+from sglang.srt.layers.quantization.dequantization import (
+    copy_missing_attrs,
+    dequantize_fp8,
+)
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -14,6 +14,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +374/-28; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +214/-33; `python/sglang/srt/layers/quantization/quark/quark.py` modified +61/-11; `python/sglang/srt/layers/quantization/quark/utils.py` modified +4/-0; `python/sglang/srt/layers/quantization/fp8_utils.py` modified +2/-0; `python/sglang/srt/model_loader/utils.py` modified +15/-1
- 验证与风险: diff 自带测试面 `test/registered/quant/test_quark_mxfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #28213 - Revert "[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs"

- 链接: https://github.com/sgl-project/sglang/pull/28213
- 状态/时间: merged / 2026-06-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；关联提交 `f18d38d04084`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+130/-1042，可读 patch 1694 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs"」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「Revert "[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs"」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +28/-374 (402 lines); hunks: -3,20 +3,12; -59,12 +51,10 @@ def __init__(; symbols: __init__, create_weights, get_online_weight_loader，涉及 `__init__, create_weights, get_online_weight_loader`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +33/-214 (247 lines); hunks: -1,19 +1,11; -170,14 +162,12 @@ def __init__(; symbols: __init__, create_weights, get_online_mxfp4_weight_loader, online_mxfp4_weight_loader，涉及 `__init__, create_weights, get_online_mxfp4_weight_loader`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +11/-61 (72 lines); hunks: -14,7 +14,6; -55,14 +54,13 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers，涉及 `QuarkConfig, __init__, quantized_layers`；`python/sglang/srt/layers/quantization/quark/utils.py` modified +0/-4 (4 lines); hunks: -210,9 +210,5 @@ def quark_post_load_weights(self_attn: nn.Module, w: torch.T...; symbols: quark_post_load_weights，涉及 `quark_post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +28/-374 (402 lines); hunks: -3,20 +3,12; -59,12 +51,10 @@ def __init__(; symbols: __init__, create_weights, get_online_weight_loader
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +33/-214 (247 lines); hunks: -1,19 +1,11; -170,14 +162,12 @@ def __init__(; symbols: __init__, create_weights, get_online_mxfp4_weight_loader, online_mxfp4_weight_loader
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +11/-61 (72 lines); hunks: -14,7 +14,6; -55,14 +54,13 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers
  - `python/sglang/srt/layers/quantization/quark/utils.py` modified +0/-4 (4 lines); hunks: -210,9 +210,5 @@ def quark_post_load_weights(self_attn: nn.Module, w: torch.T...; symbols: quark_post_load_weights
  - `python/sglang/srt/layers/quantization/fp8_utils.py` modified +0/-2 (2 lines); hunks: -1216,8 +1216,6 @@ def block_quant_dequant(; symbols: block_quant_dequant
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -3,20 +3,12 @@
-import threading
-from sglang.srt.layers.quantization.base_config import QuantizationConfig
-from sglang.srt.layers.quantization.dequantization import (
-    copy_missing_attrs,
-    dequantize_fp8,
-)
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py
@@ -1,19 +1,11 @@
-import threading
-from sglang.srt.layers.quantization import QuantizationConfig
-from sglang.srt.layers.quantization.dequantization import (
-    copy_missing_attrs,
-    dequantize_fp8,
-)
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -14,7 +14,6 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +28/-374; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +33/-214; `python/sglang/srt/layers/quantization/quark/quark.py` modified +11/-61; `python/sglang/srt/layers/quantization/quark/utils.py` modified +0/-4; `python/sglang/srt/layers/quantization/fp8_utils.py` modified +0/-2; `python/sglang/srt/model_loader/utils.py` modified +1/-15
- 验证与风险: diff 自带测试面 `test/registered/quant/test_quark_mxfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27204 - [AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8

- 链接: https://github.com/sgl-project/sglang/pull/27204
- 状态/时间: merged / 2026-06-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/weights.py`；关联提交 `a5e6dd37677f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+948/-3，可读 patch 998 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/weights.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/weights.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` added +407/-0 (407 lines); hunks: -0,0 +1,407; symbols: QuarkW4A8MXFp4MoE, __init__, get_min_capability, create_weights，涉及 `QuarkW4A8MXFp4MoE, __init__, get_min_capability`；`python/sglang/srt/layers/quantization/quark/weights.py` added +248/-0 (248 lines); hunks: -0,0 +1,248; symbols: load_gptoss_weight_quark, _load_gptoss_quark_expert_weights，涉及 `load_gptoss_weight_quark, _load_gptoss_quark_expert_weights`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +26/-0 (26 lines); hunks: -20,6 +20,7; -385,6 +386,28 @@ def _is_mx_fp4(; symbols: _is_mx_fp4, _is_mx_w4a8, _find_matched_config, get_moe_scheme，涉及 `_is_mx_fp4, _is_mx_w4a8, _find_matched_config`；`python/sglang/srt/layers/quantization/quark/schemes/__init__.py` modified +2/-0 (2 lines); hunks: -3,6 +3,7; -12,5 +13,6。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` added +407/-0 (407 lines); hunks: -0,0 +1,407; symbols: QuarkW4A8MXFp4MoE, __init__, get_min_capability, create_weights
  - `python/sglang/srt/layers/quantization/quark/weights.py` added +248/-0 (248 lines); hunks: -0,0 +1,248; symbols: load_gptoss_weight_quark, _load_gptoss_quark_expert_weights
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +26/-0 (26 lines); hunks: -20,6 +20,7; -385,6 +386,28 @@ def _is_mx_fp4(; symbols: _is_mx_fp4, _is_mx_w4a8, _find_matched_config, get_moe_scheme
  - `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` modified +2/-0 (2 lines); hunks: -3,6 +3,7; -12,5 +13,6
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py
@@ -0,0 +1,407 @@
+# SPDX-License-Identifier: Apache-2.0
+from __future__ import annotations
+import logging
+from dataclasses import replace
+from typing import TYPE_CHECKING, Any
+import torch
diff -- python/sglang/srt/layers/quantization/quark/weights.py
@@ -0,0 +1,248 @@
+# SPDX-License-Identifier: Apache-2.0
+import math
+import re
+import torch
+from sglang.srt.distributed import (
+    get_moe_expert_parallel_rank,
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -20,6 +20,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` added +407/-0; `python/sglang/srt/layers/quantization/quark/weights.py` added +248/-0; `python/sglang/srt/layers/quantization/quark/quark.py` modified +26/-0; `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` modified +2/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_gpt_oss_w4a8_mxfp4_eval_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25467 - [Quantization] Update error message strings with correct framework name in Quark/compressed-tensors

- 链接: https://github.com/sgl-project/sglang/pull/25467
- 状态/时间: merged / 2026-07-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；关联提交 `966350408eba`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+5/-5，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Quantization] Update error message strings with correct framework name in Quark/compressed-tensors」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`, `python/sglang/srt/layers/quantization/quark/utils.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[Quantization] Update error message strings with correct framework name in Quark/compressed-tensors」；主要实现面是 `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`, `python/sglang/srt/layers/quantization/quark/utils.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/compressed_tensors/utils.py` modified +2/-2 (4 lines); hunks: -59,8 +59,8 @@ def should_ignore_layer(; symbols: should_ignore_layer，涉及 `should_ignore_layer`；`python/sglang/srt/layers/quantization/quark/utils.py` modified +2/-2 (4 lines); hunks: -72,8 +72,8 @@ def should_ignore_layer(; symbols: should_ignore_layer，涉及 `should_ignore_layer`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +1/-1 (2 lines); hunks: -407,7 +407,7 @@ def _find_matched_config(; symbols: _find_matched_config，涉及 `_find_matched_config`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/compressed_tensors/utils.py` modified +2/-2 (4 lines); hunks: -59,8 +59,8 @@ def should_ignore_layer(; symbols: should_ignore_layer
  - `python/sglang/srt/layers/quantization/quark/utils.py` modified +2/-2 (4 lines); hunks: -72,8 +72,8 @@ def should_ignore_layer(; symbols: should_ignore_layer
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +1/-1 (2 lines); hunks: -407,7 +407,7 @@ def _find_matched_config(; symbols: _find_matched_config
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/compressed_tensors/utils.py
@@ -59,8 +59,8 @@ def should_ignore_layer(
-                    f"Found a different quantization schemes for "
-                    f"{shard_proj_names} in {layer_name}. vLLM "
+                    f"Found different quantization schemes for "
+                    f"{shard_proj_names} in {layer_name}. SGLang "
diff -- python/sglang/srt/layers/quantization/quark/utils.py
@@ -72,8 +72,8 @@ def should_ignore_layer(
-                    f"Found a different quantization schemes for "
-                    f"{shard_proj_names} in {layer_name}. vLLM "
+                    f"Found different quantization schemes for "
+                    f"{shard_proj_names} in {layer_name}. SGLang "
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -407,7 +407,7 @@ def _find_matched_config(
-                    f"{shard_proj_names} in {layer_name}. vLLM "
+                    f"{shard_proj_names} in {layer_name}. SGLang "
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/compressed_tensors/utils.py` modified +2/-2; `python/sglang/srt/layers/quantization/quark/utils.py` modified +2/-2; `python/sglang/srt/layers/quantization/quark/quark.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25694 - [Quantization][Bugfix]: Join multi-arg RuntimeError in Quark _check_scheme_supported

- 链接: https://github.com/sgl-project/sglang/pull/25694
- 状态/时间: merged / 2026-07-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `test/registered/unit/layers/quantization/test_quark_config.py`；关联提交 `40a522203c53`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+92/-3，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Quantization][Bugfix]: Join multi-arg RuntimeError in Quark _check_scheme_supported」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[Quantization][Bugfix]: Join multi-arg RuntimeError in Quark _check_scheme_supported」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_config.py` added +87/-0 (87 lines); hunks: -0,0 +1,87; symbols: _bare_config, TestCheckSchemeSupportedError, test_error_is_single_argument, test_error_message_renders_as_sentence，涉及 `_bare_config, TestCheckSchemeSupportedError, test_error_is_single_argument`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +5/-3 (8 lines); hunks: -294,10 +294,12 @@ def _check_scheme_supported(self, min_capability: int, err...; symbols: _check_scheme_supported，涉及 `_check_scheme_supported`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_config.py` added +87/-0 (87 lines); hunks: -0,0 +1,87; symbols: _bare_config, TestCheckSchemeSupportedError, test_error_is_single_argument, test_error_message_renders_as_sentence
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +5/-3 (8 lines); hunks: -294,10 +294,12 @@ def _check_scheme_supported(self, min_capability: int, err...; symbols: _check_scheme_supported
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_config.py
@@ -0,0 +1,87 @@
+"""Unit tests for QuarkConfig — CPU-only, no model loading."""
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=5, suite="base-a-test-cpu")
+import unittest
+from unittest.mock import patch
+from sglang.srt.layers.quantization.quark.quark import QuarkConfig
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -294,10 +294,12 @@ def _check_scheme_supported(self, min_capability: int, error: bool = True) -> bo
+                # Pass a single joined message; RuntimeError stringifies
+                # multiple positional args as a tuple repr.
-                    "Quantization scheme is not supported for ",
-                    f"the current GPU. Min capability: {min_capability}. ",
-                    f"Current capability: {capability}.",
+                    "Quantization scheme is not supported for "
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_config.py` added +87/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +5/-3
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #30786 - [Kernel] Migrate scattered MoE kernels to sglang.kernels (RFC #29630, Phase 2.5, 2/7)

- 链接: https://github.com/sgl-project/sglang/pull/30786
- 状态/时间: merged / 2026-07-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`；关联提交 `ee464fedc63e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 31 个文件，+480/-475，可读 patch 1267 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Migrate scattered MoE kernels to sglang.kernels (RFC #29630, Phase 2.5, 2/7)」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`；技术摘要: 覆盖「[Kernel] Migrate scattered MoE kernels to sglang.kernels (RFC #29630, Phase 2.5, 2/7)」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` modified +1/-1 (2 lines); hunks: -31,7 +31,7; symbols: QuarkW8A8FP8MoE，涉及 `QuarkW8A8FP8MoE`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` modified +1/-1 (2 lines); hunks: -31,7 +31,7; symbols: QuarkW8A8FP8MoE
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py
@@ -31,7 +31,7 @@
-    from sglang.srt.layers.moe.rocm_moe_utils import rocm_fused_experts_tkw1
+    from sglang.kernels.ops.moe.rocm_moe_utils import rocm_fused_experts_tkw1
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` modified +1/-1
- 验证与风险: diff 自带测试面 `python/sglang/jit_kernel/tests/test_minimax_m3_mxfp8.py`, `test/registered/jit/benchmark/bench_post_reorder_deepgemm.py`, `test/registered/jit/minimax/test_minimax_quant_scatter.py`, `test/registered/jit/test_post_reorder_deepgemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #28291 - [AMD][MXFP4] Reland "Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs"

- 链接: https://github.com/sgl-project/sglang/pull/28291
- 状态/时间: merged / 2026-07-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；关联提交 `dcd9014f1503`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+1054/-131，可读 patch 1729 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][MXFP4] Reland "Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs"」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD][MXFP4] Reland "Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs"」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +375/-28 (403 lines); hunks: -3,12 +3,20; -51,10 +59,12 @@ def __init__(; symbols: __init__, create_weights, get_online_weight_loader，涉及 `__init__, create_weights, get_online_weight_loader`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +214/-33 (247 lines); hunks: -1,11 +1,19; -162,12 +170,14 @@ def __init__(; symbols: __init__, create_weights, get_online_mxfp4_weight_loader, online_mxfp4_weight_loader，涉及 `__init__, create_weights, get_online_mxfp4_weight_loader`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +83/-15 (98 lines); hunks: -14,6 +14,7; -55,13 +56,14 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers, log_online_quantization，涉及 `QuarkConfig, __init__, quantized_layers`；`python/sglang/srt/layers/quantization/quark/utils.py` modified +4/-0 (4 lines); hunks: -206,5 +206,9 @@ def quark_post_load_weights(self_attn: nn.Module, w: torch.T...; symbols: quark_post_load_weights，涉及 `quark_post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +375/-28 (403 lines); hunks: -3,12 +3,20; -51,10 +59,12 @@ def __init__(; symbols: __init__, create_weights, get_online_weight_loader
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +214/-33 (247 lines); hunks: -1,11 +1,19; -162,12 +170,14 @@ def __init__(; symbols: __init__, create_weights, get_online_mxfp4_weight_loader, online_mxfp4_weight_loader
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +83/-15 (98 lines); hunks: -14,6 +14,7; -55,13 +56,14 @@ class QuarkConfig(QuantizationConfig):; symbols: QuarkConfig, __init__, quantized_layers, log_online_quantization
  - `python/sglang/srt/layers/quantization/quark/utils.py` modified +4/-0 (4 lines); hunks: -206,5 +206,9 @@ def quark_post_load_weights(self_attn: nn.Module, w: torch.T...; symbols: quark_post_load_weights
  - `python/sglang/srt/layers/quantization/fp8_utils.py` modified +2/-0 (2 lines); hunks: -1378,6 +1378,8 @@ def block_quant_dequant(; symbols: block_quant_dequant
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -3,12 +3,20 @@
+import threading
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
+from sglang.srt.layers.quantization.dequantization import (
+    copy_missing_attrs,
+    dequantize_fp8,
+)
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py
@@ -1,11 +1,19 @@
+import threading
+from sglang.srt.layers.quantization import QuantizationConfig
+from sglang.srt.layers.quantization.dequantization import (
+    copy_missing_attrs,
+    dequantize_fp8,
+)
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -14,6 +14,7 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +375/-28; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +214/-33; `python/sglang/srt/layers/quantization/quark/quark.py` modified +83/-15; `python/sglang/srt/layers/quantization/quark/utils.py` modified +4/-0; `python/sglang/srt/layers/quantization/fp8_utils.py` modified +2/-0; `python/sglang/srt/model_loader/utils.py` modified +15/-1
- 验证与风险: diff 自带测试面 `test/registered/quant/test_quark_mxfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33090 - [AMD][Fix] Restore aiter-padded MoE weight dims for serialized checkpoints

- 链接: https://github.com/sgl-project/sglang/pull/33090
- 状态/时间: merged / 2026-08-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `0d186f49be34`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-2，可读 patch 29 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Fix] Restore aiter-padded MoE weight dims for serialized checkpoints」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[AMD][Fix] Restore aiter-padded MoE weight dims for serialized checkpoints」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +11/-2 (13 lines); hunks: -196,9 +196,18 @@ def create_weights(; -217,7 +226,7 @@ def create_weights(; symbols: create_weights，涉及 `create_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +11/-2 (13 lines); hunks: -196,9 +196,18 @@ def create_weights(; -217,7 +226,7 @@ def create_weights(; symbols: create_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -196,9 +196,18 @@ def create_weights(
+        # Serialized MXFP4 must keep the aiter-aligned dims from
+        # get_moe_weight_sizes(): w13_weight_scale / w2_weight_scale below are
+        # still sized off w13_up_dim / w2_down_dim, and `weight_padded` is
+        # advertised to the loader, so allocating the raw (unpadded) dims here
+        # desyncs the weights from their scales.
-            2 * intermediate_size_per_partition,
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +11/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35200 - [AMD] Fix Quark Shared Experts Fusion Gate after load-time-override Removal

- 链接: https://github.com/sgl-project/sglang/pull/35200
- 状态/时间: merged / 2026-08-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`；关联提交 `ea27e3ddab12`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+70/-23，可读 patch 149 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix Quark Shared Experts Fusion Gate after load-time-override Removal」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD] Fix Quark Shared Experts Fusion Gate after load-time-override Removal」；主要实现面是 `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/quark.py` modified +0/-23 (23 lines); hunks: -336,29 +336,6 @@ def __init__(; symbols: __init__, _maybe_disable_shared_experts_fusion, quantized_layers，涉及 `__init__, _maybe_disable_shared_experts_fusion, quantized_layers`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +0/-23 (23 lines); hunks: -336,29 +336,6 @@ def __init__(; symbols: __init__, _maybe_disable_shared_experts_fusion, quantized_layers
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -336,29 +336,6 @@ def __init__(
-        self._maybe_disable_shared_experts_fusion()
-    def _maybe_disable_shared_experts_fusion(self) -> None:
-        """Turn off shared-expert fusion when the producer keeps shared experts
-        in a higher precision than the routed experts.
-        """
-        if self.can_fuse_shared_expert():
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +0/-23
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_deepseek_v4_shared_expert_fusion.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36124 - [AMD] Quark shared-experts gate: recognise a trailing MTP layer

- 链接: https://github.com/sgl-project/sglang/pull/36124
- 状态/时间: merged / 2026-08-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`；关联提交 `7bbd0ddeb5f3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+35/-1，可读 patch 62 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Quark shared-experts gate: recognise a trailing MTP layer」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD] Quark shared-experts gate: recognise a trailing MTP layer」；主要实现面是 `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/quark.py` modified +35/-1 (36 lines); hunks: -322,6 +322,14 @@ def __init__(; -555,6 +563,10 @@ def from_config(cls, config: dict[str, Any]) -> "QuarkConfig":; symbols: __init__, from_config, get_moe_scheme, get_scaled_act_names，涉及 `__init__, from_config, get_moe_scheme`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +35/-1 (36 lines); hunks: -322,6 +322,14 @@ def __init__(; -555,6 +563,10 @@ def from_config(cls, config: dict[str, Any]) -> "QuarkConfig":; symbols: __init__, from_config, get_moe_scheme, get_scaled_act_names
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -322,6 +322,14 @@ def __init__(
+        # Both are consumed by _is_draft_layer(), which has to tell an appended
+        # MTP/NextN draft layer from a target-model one. "No draft stack" is
+        # spelled None as often as it is spelled absent -- ModelConfig defaults
+        # the same field to None -- so coerce rather than let range() raise.
+        self.num_hidden_layers = getattr(hf_config, "num_hidden_layers", None)
+        self.num_nextn_predict_layers = int(
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +35/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/quark/quark.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37254 - [AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj

- 链接: https://github.com/sgl-project/sglang/pull/37254
- 状态/时间: merged / 2026-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/unit/layers/quantization/test_quark_utils.py`；关联提交 `7c195b915162`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+54/-3，可读 patch 81 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_utils.py`；技术摘要: 覆盖「[AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_utils.py` modified +50/-1 (51 lines); hunks: -8,10 +8,59; symbols: TestShouldIgnoreLayer, test_minimax_dsa_index_qkv_ignored, test_all_shards_agree_still_works, test_no_shards_ignored，涉及 `TestShouldIgnoreLayer, test_minimax_dsa_index_qkv_ignored, test_all_shards_agree_still_works`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_utils.py` modified +50/-1 (51 lines); hunks: -8,10 +8,59; symbols: TestShouldIgnoreLayer, test_minimax_dsa_index_qkv_ignored, test_all_shards_agree_still_works, test_no_shards_ignored
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_utils.py
@@ -8,10 +8,59 @@
-from sglang.srt.layers.quantization.quark.utils import e8m0_to_f32
+from sglang.srt.layers.quantization.quark.utils import (
+    e8m0_to_f32,
+    should_ignore_layer,
+)
+class TestShouldIgnoreLayer(CustomTestCase):
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_utils.py` modified +50/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37564 - [AMD][Fix] Fix aiter bpreshuffle GEMM for output sizes it cannot dispatch for qwen3.5 mxfp-attn-fp8-v2 TP4

- 链接: https://github.com/sgl-project/sglang/pull/37564
- 状态/时间: merged / 2026-09-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`；关联提交 `d6fabb74b45d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-4，可读 patch 73 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Fix] Fix aiter bpreshuffle GEMM for output sizes it cannot dispatch for qwen3.5 mxfp-attn-fp8-v2 TP4」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`；技术摘要: 覆盖「[AMD][Fix] Fix aiter bpreshuffle GEMM for output sizes it cannot dispatch for qwen3.5 mxfp-attn-fp8-v2 TP4」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +2/-1 (3 lines); hunks: -15,6 +15,7; -95,7 +96,7 @@ def process_weights_after_loading(self, layer) -> None:; symbols: process_weights_after_loading，涉及 `process_weights_after_loading`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +2/-1 (3 lines); hunks: -15,6 +15,7; -95,7 +96,7 @@ def process_weights_after_loading(self, layer) -> None:; symbols: process_weights_after_loading
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py
@@ -15,6 +15,7 @@
+    use_aiter_bpreshuffle_gemm,
@@ -95,7 +96,7 @@ def process_weights_after_loading(self, layer) -> None:
-            if _use_aiter:
+            if use_aiter_bpreshuffle_gemm(weight.shape[0]):
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #39155 - [AMD] GLM-5.2 NextN: cast draft fused MoE to per-channel FP8

- 链接: https://github.com/sgl-project/sglang/pull/39155
- 状态/时间: merged / 2026-09-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`；关联提交 `f920be4b0973`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+326/-51，可读 patch 475 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] GLM-5.2 NextN: cast draft fused MoE to per-channel FP8」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`；技术摘要: 覆盖「[AMD] GLM-5.2 NextN: cast draft fused MoE to per-channel FP8」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` modified +51/-43 (94 lines); hunks: -13,7 +13,7; -31,8 +31,6; symbols: QuarkW8A8FP8MoE, __init__, process_weights_after_loading, create_moe_runner，涉及 `QuarkW8A8FP8MoE, __init__, process_weights_after_loading`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` modified +51/-43 (94 lines); hunks: -13,7 +13,7; -31,8 +31,6; symbols: QuarkW8A8FP8MoE, __init__, process_weights_after_loading, create_moe_runner
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py
@@ -13,7 +13,7 @@
-from sglang.srt.utils import get_bool_env_var, is_hip, set_weight_attrs
+from sglang.srt.utils import get_bool_env_var, is_hip, print_info_once, set_weight_attrs
@@ -31,8 +31,6 @@
-    from sglang.kernels.ops.moe.rocm_moe_utils import rocm_fused_experts_tkw1
@@ -238,74 +236,84 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
-        if (
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` modified +51/-43
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_glm_nextn_moe_ptpc.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38546 - [AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/38546
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`, `test/registered/unit/layers/quantization/test_quark_config.py`；关联提交 `b44e2486824e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+756/-15，可读 patch 994 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_config.py` modified +185/-1 (186 lines); hunks: -1,21 +1,35; -207,5 +221,175 @@ def test_already_regex_entries_pass_through_and_match(self):; symbols: test_already_regex_entries_pass_through_and_match, TestQuarkPerLayerBlockFp8, _build_bare_config, test_model_mapper_rewrites_explicit_layer_config，涉及 `test_already_regex_entries_pass_through_and_match, TestQuarkPerLayerBlockFp8, _build_bare_config`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +56/-3 (59 lines); hunks: -15,7 +15,11; -375,6 +379,46 @@ def apply_weight_name_mapper(self, hf_to_sglang_mapper):; symbols: apply_weight_name_mapper, _get_block_fp8_config, get_quant_method，涉及 `apply_weight_name_mapper, _get_block_fp8_config, get_quant_method`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +24/-4 (28 lines); hunks: -38,12 +38,12; -202,6 +202,8 @@ def create_weights(; symbols: create_weights, _quantize_w2_online, process_weights_after_loading, create_moe_runner，涉及 `create_weights, _quantize_w2_online, process_weights_after_loading`；`test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` added +397/-0 (397 lines); hunks: -0,0 +1,397; symbols: TestGLM53FlashQuarkMoE, setUpClass, _make_mxfp4_bank, _quantize_fp8_weight，涉及 `TestGLM53FlashQuarkMoE, setUpClass, _make_mxfp4_bank`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_config.py` modified +185/-1 (186 lines); hunks: -1,21 +1,35; -207,5 +221,175 @@ def test_already_regex_entries_pass_through_and_match(self):; symbols: test_already_regex_entries_pass_through_and_match, TestQuarkPerLayerBlockFp8, _build_bare_config, test_model_mapper_rewrites_explicit_layer_config
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +56/-3 (59 lines); hunks: -15,7 +15,11; -375,6 +379,46 @@ def apply_weight_name_mapper(self, hf_to_sglang_mapper):; symbols: apply_weight_name_mapper, _get_block_fp8_config, get_quant_method
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +24/-4 (28 lines); hunks: -38,12 +38,12; -202,6 +202,8 @@ def create_weights(; symbols: create_weights, _quantize_w2_online, process_weights_after_loading, create_moe_runner
  - `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` added +397/-0 (397 lines); hunks: -0,0 +1,397; symbols: TestGLM53FlashQuarkMoE, setUpClass, _make_mxfp4_bank, _quantize_fp8_weight
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_config.py
@@ -1,21 +1,35 @@
-"""Unit tests for QuarkConfig — CPU-only, no model loading."""
+"""Unit tests for QuarkConfig and its MoE scheme — CPU-only, no model loading."""
+import sys
+import types
+from copy import deepcopy
+from types import SimpleNamespace
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -15,7 +15,11 @@
-from sglang.srt.layers.quantization.fp8 import Fp8Config, Fp8LinearMethod
+from sglang.srt.layers.quantization.fp8 import (
+    Fp8Config,
+    Fp8LinearMethod,
+    Fp8MoEMethod,
+)
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -38,12 +38,12 @@
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_config.py` modified +185/-1; `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` added +397/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +56/-3; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +24/-4
- 验证与风险: diff 自带测试面 `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`, `test/registered/unit/layers/quantization/test_fp8_moe_runner_ownership.py`, `test/registered/unit/layers/quantization/test_quark_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39317 - [AMD] [GLM-5.3-Flash Day 0] Honor fused and per-expert names in quark `exclude`

- 链接: https://github.com/sgl-project/sglang/pull/39317
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/utils.py`, `test/registered/unit/layers/quantization/test_quark_utils.py`；关联提交 `e1daf68304ea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+56/-5，可读 patch 82 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [GLM-5.3-Flash Day 0] Honor fused and per-expert names in quark `exclude`」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `test/registered/unit/layers/quantization/test_quark_utils.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；技术摘要: 覆盖「[AMD] [GLM-5.3-Flash Day 0] Honor fused and per-expert names in quark `exclude`」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_utils.py`, `python/sglang/srt/layers/quantization/quark/utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_utils.py` modified +41/-0 (41 lines); hunks: -115,5 +115,46 @@ def test_cuda_parity(self):; symbols: test_cuda_parity, TestShouldIgnoreLayerFusedNames, test_directly_excluded_fused_qkv_is_ignored, test_per_expert_excludes_ignore_the_fused_moe_module，涉及 `test_cuda_parity, TestShouldIgnoreLayerFusedNames, test_directly_excluded_fused_qkv_is_ignored`；`python/sglang/srt/layers/quantization/quark/utils.py` modified +15/-5 (20 lines); hunks: -55,6 +55,19 @@ def should_ignore_layer(; -87,12 +100,9 @@ def should_ignore_layer(; symbols: should_ignore_layer，涉及 `should_ignore_layer`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_utils.py` modified +41/-0 (41 lines); hunks: -115,5 +115,46 @@ def test_cuda_parity(self):; symbols: test_cuda_parity, TestShouldIgnoreLayerFusedNames, test_directly_excluded_fused_qkv_is_ignored, test_per_expert_excludes_ignore_the_fused_moe_module
  - `python/sglang/srt/layers/quantization/quark/utils.py` modified +15/-5 (20 lines); hunks: -55,6 +55,19 @@ def should_ignore_layer(; -87,12 +100,9 @@ def should_ignore_layer(; symbols: should_ignore_layer
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_utils.py
@@ -115,5 +115,46 @@ def test_cuda_parity(self):
+QKV_MAPPING = {"qkv_proj": ["q_proj", "k_proj", "v_proj"]}
+class TestShouldIgnoreLayerFusedNames(CustomTestCase):
+    """An `exclude` entry naming an already-fused module, or naming experts
+    individually, must exclude the fused module SGLang builds; otherwise an
+    MXFP4-packed parameter is allocated for a BF16 tensor and loading aborts."""
+    # ---- Bug-catchers: must FAIL on unfixed code ---------------------------
diff -- python/sglang/srt/layers/quantization/quark/utils.py
@@ -55,6 +55,19 @@ def should_ignore_layer(
+    # a fused module can be excluded under its fused name, so match it before expanding
+    if check_equal_or_regex_match(layer_name=layer_name, targets=ignore):
+        return True
+    # excludes may name experts individually, so an excluded expert excludes the module
+    if layer_name.endswith(".experts"):
+        expert_prefix = layer_name + "."
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_utils.py` modified +41/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/utils.py` modified +15/-5
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41464 - [AMD] Fix GLM-5.3 quark MoE MI35x test runner config

- 链接: https://github.com/sgl-project/sglang/pull/41464
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`；关联提交 `05817a40c98a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-0，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix GLM-5.3 quark MoE MI35x test runner config」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`；技术摘要: 覆盖「[AMD] Fix GLM-5.3 quark MoE MI35x test runner config」；主要实现面是 `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` modified +2/-0 (2 lines); hunks: -49,7 +49,9 @@ def setUpClass(cls):; symbols: setUpClass，涉及 `setUpClass`。
- 代码 diff 细节:
  - `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` modified +2/-0 (2 lines); hunks: -49,7 +49,9 @@ def setUpClass(cls):; symbols: setUpClass
- 关键代码摘录:

```diff
diff -- test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py
@@ -49,7 +49,9 @@ def setUpClass(cls):
+                is_gated=True,
+                gemm1_beta=None,
```

- 已读文件:
  - tests: `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` modified +2/-0
- 验证与风险: diff 自带测试面 `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #28734 - [AMD] Fix Load and Inference of MLA models with Quark PTPC FP8 attention on ROCm

- 链接: https://github.com/sgl-project/sglang/pull/28734
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py`；关联提交 `875dd41e6f5c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+99/-3，可读 patch 139 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix Load and Inference of MLA models with Quark PTPC FP8 attention on ROCm」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`；技术摘要: 覆盖「[AMD] Fix Load and Inference of MLA models with Quark PTPC FP8 attention on ROCm」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py` added +65/-0 (65 lines); hunks: -0,0 +1,65; symbols: TestChannelQuantToTensorQuantBroadcast, test_2d_weight_1d_scale_broadcasts_per_output_channel, test_mismatched_n_k_would_fail_without_unsqueeze, test_scale_already_matching_rank_is_unchanged，涉及 `TestChannelQuantToTensorQuantBroadcast, test_2d_weight_1d_scale_broadcasts_per_output_channel, test_mismatched_n_k_would_fail_without_unsqueeze`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +8/-1 (9 lines); hunks: -174,7 +174,14 @@ def apply_weights(; symbols: apply_weights，涉及 `apply_weights`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py` added +65/-0 (65 lines); hunks: -0,0 +1,65; symbols: TestChannelQuantToTensorQuantBroadcast, test_2d_weight_1d_scale_broadcasts_per_output_channel, test_mismatched_n_k_would_fail_without_unsqueeze, test_scale_already_matching_rank_is_unchanged
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +8/-1 (9 lines); hunks: -174,7 +174,14 @@ def apply_weights(; symbols: apply_weights
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py
@@ -0,0 +1,65 @@
+"""CPU-only regression tests for the Quark PTPC-FP8 (W8A8 FP8) MLA attention fix.
+These guard the hardware-independent pieces of the fix that enables loading and
+running MLA models (e.g. GlmMoeDsaForCausalLM) with Quark-quantized PTPC FP8
+attention on ROCm/gfx95.
+"""
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py
@@ -174,7 +174,14 @@ def apply_weights(
+        # Activations must be a plain bf16 tensor: per-channel FP8 (weight_scale
+        # [N, 1]) is gated off the aiter fused RMSNorm+quant kernel upstream by
+        # _is_block_scale_fp8, so the per-token quant happens in apply_fp8_linear.
+        assert not isinstance(x, tuple), (
+            "quark W8A8 FP8 linear received a pre-quantized tuple; a fused "
+            "RMSNorm+quant producer was not gated off by _is_block_scale_fp8 "
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py` added +65/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +8/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40980 - [Fix] MoE: require TopK layer_id to ensure routed expert captures

- 链接: https://github.com/sgl-project/sglang/pull/40980
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/mixtral.py`；关联提交 `3d4953839c39`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 23 个文件，+34/-2，可读 patch 267 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] MoE: require TopK layer_id to ensure routed expert captures」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[Fix] MoE: require TopK layer_id to ensure routed expert captures」；主要实现面是 `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/mixtral.py` modified +1/-0 (1 lines); hunks: -90,6 +90,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/mixtral.py` modified +1/-0 (1 lines); hunks: -90,6 +90,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/mixtral.py
@@ -90,6 +90,7 @@ def __init__(
+            layer_id=layer_id,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/mixtral.py` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/moe/test_triton_fused_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41807 - [Fix] Shard MoE WNA16 and Quark INT4-FP8 weights by the MoE placement

- 链接: https://github.com/sgl-project/sglang/pull/41807
- 状态/时间: merged / 2026-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；关联提交 `e2899899331f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+148/-12，可读 patch 209 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Shard MoE WNA16 and Quark INT4-FP8 weights by the MoE placement」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`；技术摘要: 覆盖「[Fix] Shard MoE WNA16 and Quark INT4-FP8 weights by the MoE placement」；主要实现面是 `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +2/-4 (6 lines); hunks: -138,8 +138,6 @@ def __init__(self, quant_config):; -170,12 +168,12 @@ def online_int4_fp8_weight_loader(; symbols: __init__, online_int4_fp8_weight_loader，涉及 `__init__, online_int4_fp8_weight_loader`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +2/-4 (6 lines); hunks: -138,8 +138,6 @@ def __init__(self, quant_config):; -170,12 +168,12 @@ def online_int4_fp8_weight_loader(; symbols: __init__, online_int4_fp8_weight_loader
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark_int4fp8_moe.py
@@ -138,8 +138,6 @@ def __init__(self, quant_config):
-        self.tp_rank = get_parallel().tp_rank
@@ -170,12 +168,12 @@ def online_int4_fp8_weight_loader(
-                        shard_dim, shard_size * self.tp_rank, shard_size
+                        shard_dim, shard_size * layer.moe_tp_rank, shard_size
-                        shard_dim, shard_size * self.tp_rank, shard_size
+                        shard_dim, shard_size * layer.moe_tp_rank, shard_size
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` modified +2/-4
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_moe_wna16_ep_shard.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40811 - [AMD][Quark] Serve the Kimi-K3 MXFP4 checkpoint on ROCm

- 链接: https://github.com/sgl-project/sglang/pull/40811
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py`；关联提交 `6af651ea0cb4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+402/-11，可读 patch 546 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][Quark] Serve the Kimi-K3 MXFP4 checkpoint on ROCm」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`；技术摘要: 覆盖「[AMD][Quark] Serve the Kimi-K3 MXFP4 checkpoint on ROCm」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py` added +115/-0 (115 lines); hunks: -0,0 +1,115; symbols: _per_channel_scheme, _quantized_layer, TestNarrowOutputPartitionFp8, setUp，涉及 `_per_channel_scheme, _quantized_layer, TestNarrowOutputPartitionFp8`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +64/-2 (66 lines); hunks: -17,6 +17,9; -44,8 +47,15; symbols: create_weights, _quantize_w2_online, _shuffle_gu_interleaved, process_weights_after_loading，涉及 `create_weights, _quantize_w2_online, _shuffle_gu_interleaved`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +20/-0 (20 lines); hunks: -94,6 +94,21 @@ def process_weights_after_loading(self, layer) -> None:; -182,6 +197,11 @@ def apply_weights(; symbols: process_weights_after_loading, apply_weights，涉及 `process_weights_after_loading, apply_weights`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py` added +115/-0 (115 lines); hunks: -0,0 +1,115; symbols: _per_channel_scheme, _quantized_layer, TestNarrowOutputPartitionFp8, setUp
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +64/-2 (66 lines); hunks: -17,6 +17,9; -44,8 +47,15; symbols: create_weights, _quantize_w2_online, _shuffle_gu_interleaved, process_weights_after_loading
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +20/-0 (20 lines); hunks: -94,6 +94,21 @@ def process_weights_after_loading(self, layer) -> None:; -182,6 +197,11 @@ def apply_weights(; symbols: process_weights_after_loading, apply_weights
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py
@@ -0,0 +1,115 @@
+"""Unit tests for srt/layers/quantization/quark/schemes/quark_w8a8_fp8 on ROCm."""
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=10, suite="base-a-test-cpu")
+import unittest
+from types import SimpleNamespace
+from unittest.mock import patch
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -17,6 +17,9 @@
+from sglang.srt.layers.quantization.mxfp4 import (
+    _aiter_situ_uses_gu_interleaved_weights,
+)
@@ -44,8 +47,15 @@
+_aiter_k3_opt = _use_aiter and get_bool_env_var("SGLANG_AITER_K3_OPT")
-    from aiter.ops.shuffle import moe_shuffle_scale, moe_shuffle_weight, shuffle_weight
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py
@@ -94,6 +94,21 @@ def process_weights_after_loading(self, layer) -> None:
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py` added +115/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +64/-2; `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +20/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/kda_flydsl/test_kimi_k3_kda_decode.py`, `test/registered/unit/layers/quantization/test_quark_w8a8_fp8.py`, `test/registered/unit/models/test_kimi_k3_rocm_quant.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41870 - [AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4

- 链接: https://github.com/sgl-project/sglang/pull/41870
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`；关联提交 `af1bef3eaf72`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+245/-7，可读 patch 353 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4」；主要实现面是 `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/quark.py` modified +9/-0 (9 lines); hunks: -419,6 +419,15 @@ def _get_block_fp8_config(; symbols: _get_block_fp8_config, is_linear_unquantized, get_quant_method，涉及 `_get_block_fp8_config, is_linear_unquantized, get_quant_method`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +9/-0 (9 lines); hunks: -419,6 +419,15 @@ def _get_block_fp8_config(; symbols: _get_block_fp8_config, is_linear_unquantized, get_quant_method
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -419,6 +419,15 @@ def _get_block_fp8_config(
+    def is_linear_unquantized(self, prefix: str) -> bool:
+        # get_quant_method registers every non-excluded prefix as an
+        # online-quantized layer, so answer from the exclude list instead.
+        return self.excluded_fp8_config is None and should_ignore_layer(
+            prefix,
+            ignore=self.exclude_layers,
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +9/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_glm5_next_bfg_fusion.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #34540 - [AMD] Fix Quark W4A4 MXFP4 MoE clamped-SwiGLU on the AITER path

- 链接: https://github.com/sgl-project/sglang/pull/34540
- 状态/时间: merged / 2026-10-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`；关联提交 `c0df52be2d96`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+144/-1，可读 patch 160 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix Quark W4A4 MXFP4 MoE clamped-SwiGLU on the AITER path」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[AMD] Fix Quark W4A4 MXFP4 MoE clamped-SwiGLU on the AITER path」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py` added +138/-0 (138 lines); hunks: -0,0 +1,138; symbols: _make_scheme, _force_aiter_runner, fake_moe_runner, _fake_layer，涉及 `_make_scheme, _force_aiter_runner, fake_moe_runner`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +6/-1 (7 lines); hunks: -980,6 +980,7 @@ def apply_weights(; -1015,7 +1016,11 @@ def apply_weights(; symbols: apply_weights，涉及 `apply_weights`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py` added +138/-0 (138 lines); hunks: -0,0 +1,138; symbols: _make_scheme, _force_aiter_runner, fake_moe_runner, _fake_layer
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +6/-1 (7 lines); hunks: -980,6 +980,7 @@ def apply_weights(; -1015,7 +1016,11 @@ def apply_weights(; symbols: apply_weights
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py
@@ -0,0 +1,138 @@
+"""Unit tests for the Quark W4A4 MXFP4 MoE clamped-SwiGLU plumbing.
+CPU-only, no model loading and no aiter/ROCm dependency: they exercise the
+pure-Python control flow in ``QuarkW4A4MXFp4MoE.create_moe_runner`` and
+``apply_weights`` that decides whether the AITER MoE runner is driven on the
+clamped-SwiGLU path (``activation="swiglu"`` + ``swiglu_limit``) or the plain
+SiLU path. See the regression these guard against: clamped-SwiGLU MXFP4
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -980,6 +980,7 @@ def apply_weights(
+            aiter_swiglu_oai_limit,
@@ -1015,7 +1016,11 @@ def apply_weights(
-            swiglu_limit=self.moe_runner_config.swiglu_limit or 0.0,
+            swiglu_limit=(
+                aiter_swiglu_oai_limit(self.moe_runner_config)
+                or self.moe_runner_config.swiglu_limit
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py` added +138/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +6/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41134 - [AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/41134
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`；关联提交 `33883a5fa3c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+607/-12，可读 patch 793 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`；技术摘要: 覆盖「[AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +15/-1 (16 lines); hunks: -29,6 +29,8; -192,6 +194,18 @@ def apply_weights(; symbols: QuarkW8A8Fp8, __init__, apply_weights，涉及 `QuarkW8A8Fp8, __init__, apply_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +15/-1 (16 lines); hunks: -29,6 +29,8; -192,6 +194,18 @@ def apply_weights(; symbols: QuarkW8A8Fp8, __init__, apply_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py
@@ -29,6 +29,8 @@
+    from sglang.kernels.ops.gemm.smallm_fp8_gfx950 import smallm_fp8_gemm_enabled
@@ -192,6 +194,18 @@ def apply_weights(
+        # The one exception is the per-token (fp8, scale [M, 1]) pair that the
+        # Qwen3.5 SGLANG_ROCM_SMALLM_FP8_PROJ producers send on gfx950.
+        input_scale = layer.input_scale
+        if isinstance(x, tuple) and _use_aiter and smallm_fp8_gemm_enabled():
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` modified +15/-1
- 验证与风险: diff 自带测试面 `test/registered/amd/test_smallm_fp8_proj_gfx950.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31054 - [AMD] Support Quark DeepSeek-V4-MXFP4 checkpoints on the DSV4 stack, enabling shared-expert fusion and MTP

- 链接: https://github.com/sgl-project/sglang/pull/31054
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_config.py`；关联提交 `3c1703d2ffdd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+266/-7，可读 patch 367 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Support Quark DeepSeek-V4-MXFP4 checkpoints on the DSV4 stack, enabling shared-expert fusion and MTP」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[AMD] Support Quark DeepSeek-V4-MXFP4 checkpoints on the DSV4 stack, enabling shared-expert fusion and MTP」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_config.py` modified +149/-0 (149 lines); hunks: -399,6 +399,85 @@ def test_unmatched_layer_still_uses_global_quark_config(self):; -459,5 +538,75 @@ def test_apply_forwards_clamp_separated_layout_and_padding(...; symbols: test_unmatched_layer_still_uses_global_quark_config, TestDeepseekV4QuarkMapping, _config_for, test_only_draft_vetoes_fusion_on_fp8_mtp_shared_experts，涉及 `test_unmatched_layer_still_uses_global_quark_config, TestDeepseekV4QuarkMapping, _config_for`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +40/-0 (40 lines); hunks: -59,6 +59,42; -220,6 +256,10 @@ def create_weights(; symbols: _pad_tp_chunks, _rank_chunk_padding_loader, loader, create_weights，涉及 `_pad_tp_chunks, _rank_chunk_padding_loader, loader`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +28/-7 (35 lines); hunks: -282,6 +282,10 @@ def _build_excluded_fp8_config(config: Dict[str, Any]) -> O...; -381,9 +385,15 @@ def apply_weight_name_mapper(self, hf_to_sglang_mapper):; symbols: _build_excluded_fp8_config, apply_weight_name_mapper, can_fuse_shared_expert，涉及 `_build_excluded_fp8_config, apply_weight_name_mapper, can_fuse_shared_expert`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_config.py` modified +149/-0 (149 lines); hunks: -399,6 +399,85 @@ def test_unmatched_layer_still_uses_global_quark_config(self):; -459,5 +538,75 @@ def test_apply_forwards_clamp_separated_layout_and_padding(...; symbols: test_unmatched_layer_still_uses_global_quark_config, TestDeepseekV4QuarkMapping, _config_for, test_only_draft_vetoes_fusion_on_fp8_mtp_shared_experts
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +40/-0 (40 lines); hunks: -59,6 +59,42; -220,6 +256,10 @@ def create_weights(; symbols: _pad_tp_chunks, _rank_chunk_padding_loader, loader, create_weights
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +28/-7 (35 lines); hunks: -282,6 +282,10 @@ def _build_excluded_fp8_config(config: Dict[str, Any]) -> O...; -381,9 +385,15 @@ def apply_weight_name_mapper(self, hf_to_sglang_mapper):; symbols: _build_excluded_fp8_config, apply_weight_name_mapper, can_fuse_shared_expert
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_config.py
@@ -399,6 +399,85 @@ def test_unmatched_layer_still_uses_global_quark_config(self):
+class TestDeepseekV4QuarkMapping(CustomTestCase):
+    """amd/DeepSeek-V4-*-MXFP4 layout: MXFP4 experts everywhere, but the MTP
+    block keeps FP8-block shared experts; specs are keyed by checkpoint names."""
+    _HF_CONFIG = SimpleNamespace(quantization_config={"quant_method": "quark"})
+    _FP8 = TestQuarkPerLayerBlockFp8._BLOCK_FP8_CONFIG
+    _MXFP4 = {
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -59,6 +59,42 @@
+def _pad_tp_chunks(
+    loaded_weight: torch.Tensor, *, dim: int, tp_size: int, padded: int
+) -> torch.Tensor:
+    """Zero-pad each of the tp_size equal chunks of loaded_weight along dim to padded."""
+    real = loaded_weight.shape[dim] // tp_size
+    if real == padded:
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -282,6 +282,10 @@ def _build_excluded_fp8_config(config: Dict[str, Any]) -> Optional["Fp8Config"]:
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_config.py` modified +149/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +40/-0; `python/sglang/srt/layers/quantization/quark/quark.py` modified +28/-7
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41980 - [AMD] Recalibrate test_quark_mxfp4 GSM8K thresholds to observed MI355X noise

- 链接: https://github.com/sgl-project/sglang/pull/41980
- 状态/时间: merged / 2026-10-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/quantization/test_quark_mxfp4.py`；关联提交 `7224fce1b5e4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-4，可读 patch 23 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Recalibrate test_quark_mxfp4 GSM8K thresholds to observed MI355X noise」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `test/registered/e2e/quantization/test_quark_mxfp4.py`；技术摘要: 覆盖「[AMD] Recalibrate test_quark_mxfp4 GSM8K thresholds to observed MI355X noise」；主要实现面是 `test/registered/e2e/quantization/test_quark_mxfp4.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/quantization/test_quark_mxfp4.py` modified +5/-4 (9 lines); hunks: -220,9 +220,9 @@ class TestNVFP4ToMXFP4MOETP1(TestOnlineQuantizationMemoryLoad):; -286,7 +286,8 @@ def test_peak_memory(self):; symbols: TestNVFP4ToMXFP4MOETP1, test_gsm8k, test_peak_memory，涉及 `TestNVFP4ToMXFP4MOETP1, test_gsm8k, test_peak_memory`。
- 代码 diff 细节:
  - `test/registered/e2e/quantization/test_quark_mxfp4.py` modified +5/-4 (9 lines); hunks: -220,9 +220,9 @@ class TestNVFP4ToMXFP4MOETP1(TestOnlineQuantizationMemoryLoad):; -286,7 +286,8 @@ def test_peak_memory(self):; symbols: TestNVFP4ToMXFP4MOETP1, test_gsm8k, test_peak_memory
- 关键代码摘录:

```diff
diff -- test/registered/e2e/quantization/test_quark_mxfp4.py
@@ -220,9 +220,9 @@ class TestNVFP4ToMXFP4MOETP1(TestOnlineQuantizationMemoryLoad):
-        # Requantized NVFP4 -> MXFP4 observed accuracy: ~0.88
-        # (BF16 Qwen/Qwen3-30B-A3B reference: ~0.94).
-        self._test_gsm8k(accuracy_threshold=0.85)
+        # Requantized NVFP4 -> MXFP4 observed accuracy on MI355X CI: median
+        # 0.862, min 0.798 over 40 runs (BF16 Qwen/Qwen3-30B-A3B reference: ~0.94).
+        self._test_gsm8k(accuracy_threshold=0.78)
```

- 已读文件:
  - tests: `test/registered/e2e/quantization/test_quark_mxfp4.py` modified +5/-4
- 验证与风险: diff 自带测试面 `test/registered/e2e/quantization/test_quark_mxfp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45365 - [Fix] [AMD] gpt-oss: support EP for gfx1250 W4A8 MXFP4 MoE

- 链接: https://github.com/sgl-project/sglang/pull/45365
- 状态/时间: merged / 2026-10-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`；关联提交 `89860fbd2e3c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+123/-8，可读 patch 197 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [AMD] gpt-oss: support EP for gfx1250 W4A8 MXFP4 MoE」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`；技术摘要: 覆盖「[Fix] [AMD] gpt-oss: support EP for gfx1250 W4A8 MXFP4 MoE」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` modified +17/-0 (17 lines); hunks: -261,9 +261,24 @@ def _process_weights_gfx1250(self, layer: torch.nn.Module)...; -458,6 +473,8 @@ def apply_weights(; symbols: _process_weights_gfx1250, apply_weights，涉及 `_process_weights_gfx1250, apply_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` modified +17/-0 (17 lines); hunks: -261,9 +261,24 @@ def _process_weights_gfx1250(self, layer: torch.nn.Module)...; -458,6 +473,8 @@ def apply_weights(; symbols: _process_weights_gfx1250, apply_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py
@@ -261,9 +261,24 @@ def _process_weights_gfx1250(self, layer: torch.nn.Module) -> None:
+            build_ep_expert_map,
+        self.ep_expert_map = None
+        self.num_local_experts = layer.w13_weight.shape[0]
+        if getattr(layer, "moe_ep_size", 1) > 1:
+            if getattr(layer, "num_fused_shared_experts", 0):
+                raise NotImplementedError(
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` modified +17/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/aiter_mxfp4_w4a8_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #44993 - [Refactor] moe: Derive layer contracts from the selected quant method

- 链接: https://github.com/sgl-project/sglang/pull/44993
- 状态/时间: merged / 2026-10-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/mixtral.py`；关联提交 `4f8f06faf3ac`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 95 个文件，+2599/-372，可读 patch 4583 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] moe: Derive layer contracts from the selected quant method」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 模型实现调整；主要 diff: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/mixtral.py`；技术摘要: 覆盖「[Refactor] moe: Derive layer contracts from the selected quant method」；主要实现面是 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/mixtral.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/quark.py` modified +3/-0 (3 lines); hunks: -1180,6 +1180,9 @@ def create_moe_runner(; symbols: create_moe_runner, get_moe_runner_backend, apply，涉及 `create_moe_runner, get_moe_runner_backend, apply`；`python/sglang/srt/models/mixtral.py` modified +1/-0 (1 lines); hunks: -107,6 +107,7 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +3/-0 (3 lines); hunks: -1180,6 +1180,9 @@ def create_moe_runner(; symbols: create_moe_runner, get_moe_runner_backend, apply
  - `python/sglang/srt/models/mixtral.py` modified +1/-0 (1 lines); hunks: -107,6 +107,7 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -1180,6 +1180,9 @@ def create_moe_runner(
+    def get_moe_runner_backend(self, layer):
+        return layer.scheme.get_moe_runner_backend(layer)
diff -- python/sglang/srt/models/mixtral.py
@@ -107,6 +107,7 @@ def __init__(
+        self.topk.bind_runner_backend(self.experts.runner_backend)
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +3/-0; `python/sglang/srt/models/mixtral.py` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/test_fp8_moe_triton_runner_with_aiter.py`, `test/registered/cuda_graph/breakable/test_deepseek_dual_stream_outputs.py`, `test/registered/unit/layers/moe/test_flashinfer_dispatcher.py`, `test/registered/unit/layers/moe/test_fused_shared_expert_scaling.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39598 - [Perf] [AMD] quark: Add opt-in AITER ASM FP4 GEMM for Quark dense linear

- 链接: https://github.com/sgl-project/sglang/pull/39598
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py`；关联提交 `6e98c84c601a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+328/-0，可读 patch 378 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [AMD] quark: Add opt-in AITER ASM FP4 GEMM for Quark dense linear」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py`；技术摘要: 覆盖「[Perf] [AMD] quark: Add opt-in AITER ASM FP4 GEMM for Quark dense linear」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +204/-0 (204 lines); hunks: -6,6 +6,7; -29,6 +30,82; symbols: _asm_fp4_scale_swizzle_supported, _swizzle_asm_fp4_scale, _shuffle_asm_fp4_act_scale, _asm_fp4_prequantized_input，涉及 `_asm_fp4_scale_swizzle_supported, _swizzle_asm_fp4_scale, _shuffle_asm_fp4_act_scale`；`test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py` added +121/-0 (121 lines); hunks: -0,0 +1,121; symbols: TestQuarkMxfp4AsmScaleLayout, test_supported_shape, test_rejects_unsupported_shapes, test_swizzle_matches_aiter_tile_permutation，涉及 `TestQuarkMxfp4AsmScaleLayout, test_supported_shape, test_rejects_unsupported_shapes`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +204/-0 (204 lines); hunks: -6,6 +6,7; -29,6 +30,82; symbols: _asm_fp4_scale_swizzle_supported, _swizzle_asm_fp4_scale, _shuffle_asm_fp4_act_scale, _asm_fp4_prequantized_input
  - `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py` added +121/-0 (121 lines); hunks: -0,0 +1,121; symbols: TestQuarkMxfp4AsmScaleLayout, test_supported_shape, test_rejects_unsupported_shapes, test_swizzle_matches_aiter_tile_permutation
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py
@@ -6,6 +6,7 @@
+from sglang.srt.environ import envs
@@ -29,6 +30,82 @@
+_ASM_FP4_SCALE_ROW_MULTIPLE = 32
+_ASM_FP4_SCALE_COL_MULTIPLE = 8
+# Workaround: gemm_a4w4's untuned ASM heuristic returns wrong rows 1..M-1 for
+# N <= 128 at 2 <= M <= 64 (measured on ROCm/aiter@e7d2453f2, MI355X).
diff -- test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py
@@ -0,0 +1,121 @@
+"""CPU-only tests for Quark MXFP4 AITER ASM layout helpers."""
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=5, suite="base-a-test-cpu")
+import unittest
+from unittest import mock
+import torch
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` modified +204/-0
  - tests: `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py` added +121/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40776 - [Fix] [AMD] Quark: fix Quark block-FP8 loading in DeepSeek loader

- 链接: https://github.com/sgl-project/sglang/pull/40776
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py`；关联提交 `9d7ad308bdbb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+232/-17，可读 patch 299 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [AMD] Quark: fix Quark block-FP8 loading in DeepSeek loader」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py`；技术摘要: 覆盖「[Fix] [AMD] Quark: fix Quark block-FP8 loading in DeepSeek loader」；主要实现面是 `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py` added +187/-0 (187 lines); hunks: -0,0 +1,187; symbols: _FakeParam, __init__, weight_loader, _FakeDeepseekLoader，涉及 `_FakeParam, __init__, weight_loader`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py` added +187/-0 (187 lines); hunks: -0,0 +1,187; symbols: _FakeParam, __init__, weight_loader, _FakeDeepseekLoader
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py
@@ -0,0 +1,187 @@
+"""Regression tests for Quark block-FP8 weights in the DeepSeek loader."""
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=5, suite="base-a-test-cpu")
+import unittest
+from types import SimpleNamespace
+from unittest.mock import patch
```

- 已读文件:
  - tests: `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py` added +187/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41899 - [Perf] [AMD] quark/Qwen3.8: Quantize the BF16 shared expert of Quark MXFP4 checkpoints to MXFP4 while loading for shared-expert fusion

- 链接: https://github.com/sgl-project/sglang/pull/41899
- 状态/时间: merged / 2026-10-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py`；关联提交 `0cd2a63b3634`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+1470/-19，可读 patch 1710 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [AMD] quark/Qwen3.8: Quantize the BF16 shared expert of Quark MXFP4 checkpoints to MXFP4 while loading for shared-expert fusion」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[Perf] [AMD] quark/Qwen3.8: Quantize the BF16 shared expert of Quark MXFP4 checkpoints to MXFP4 while loading for shared-expert fusion」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_config.py` modified +546/-3 (549 lines); hunks: -2,20 +2,24; -474,7 +478,7 @@ class TestQuarkMxfp4MoEAiterQuantInfo(CustomTestCase):; symbols: TestQuarkMxfp4MoEAiterQuantInfo, test_apply_forwards_clamp_separated_layout_and_padding, test_unpadded_weights_pass_through_unchanged, TestSharedExpertOnlineMxfp4Gate，涉及 `TestQuarkMxfp4MoEAiterQuantInfo, test_apply_forwards_clamp_separated_layout_and_padding, test_unpadded_weights_pass_through_unchanged`；`test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py` added +474/-0 (474 lines); hunks: -0,0 +1,474; symbols: _fake_packed, _StubScheme, __init__, quantize_shared_expert，涉及 `_fake_packed, _StubScheme, __init__`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +211/-7 (218 lines); hunks: -7,6 +7,7; -37,7 +38,12; symbols: _build_excluded_fp8_config, QuarkConfig, __init__, get_quant_method，涉及 `_build_excluded_fp8_config, QuarkConfig, __init__`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +52/-0 (52 lines); hunks: -130,11 +130,13 @@ def __init__(; -160,6 +162,16 @@ def __init__(; symbols: __init__, get_min_capability, create_weights, online_mxfp4_moe_weight_loader，涉及 `__init__, get_min_capability, create_weights`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_config.py` modified +546/-3 (549 lines); hunks: -2,20 +2,24; -474,7 +478,7 @@ class TestQuarkMxfp4MoEAiterQuantInfo(CustomTestCase):; symbols: TestQuarkMxfp4MoEAiterQuantInfo, test_apply_forwards_clamp_separated_layout_and_padding, test_unpadded_weights_pass_through_unchanged, TestSharedExpertOnlineMxfp4Gate
  - `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py` added +474/-0 (474 lines); hunks: -0,0 +1,474; symbols: _fake_packed, _StubScheme, __init__, quantize_shared_expert
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +211/-7 (218 lines); hunks: -7,6 +7,7; -37,7 +38,12; symbols: _build_excluded_fp8_config, QuarkConfig, __init__, get_quant_method
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +52/-0 (52 lines); hunks: -130,11 +130,13 @@ def __init__(; -160,6 +162,16 @@ def __init__(; symbols: __init__, get_min_capability, create_weights, online_mxfp4_moe_weight_loader
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_config.py
@@ -2,20 +2,24 @@
-register_cpu_ci(est_time=12, suite="base-a-test-cpu")
+register_cpu_ci(est_time=18, suite="base-a-test-cpu")
+from contextlib import contextmanager
-from unittest.mock import patch
+from unittest.mock import MagicMock, patch
+from sglang.srt.environ import envs
diff -- test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py
@@ -0,0 +1,474 @@
+"""Unit tests for the load-time shared-expert MXFP4 conversion — CPU-only, no model loading."""
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=8, suite="base-a-test-cpu")
+import unittest
+from types import SimpleNamespace
+import torch
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -7,6 +7,7 @@
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_config.py` modified +546/-3; `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py` added +474/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +211/-7; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +52/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_qwen38_mxfp4_eval_mi35x.py`, `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/layers/quantization/test_quark_shared_expert_online_mxfp4_loader.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45802 - [Fix] [AMD] quark: Skip no-copy loads after MXFP4 quantization

- 链接: https://github.com/sgl-project/sglang/pull/45802
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`；关联提交 `de6c211a4905`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+53/-11，可读 patch 91 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [AMD] quark: Skip no-copy loads after MXFP4 quantization」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[Fix] [AMD] quark: Skip no-copy loads after MXFP4 quantization」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py` modified +50/-11 (61 lines); hunks: -1,17 +1,8; -21,6 +12,7; symbols: test_apply_weights_defaults_swiglu_limit_zero_without_clamp, TestOnlineWeightLoader, test_nonlocal_w13_after_quantization, test_nonlocal_w2_after_quantization，涉及 `test_apply_weights_defaults_swiglu_limit_zero_without_clamp, TestOnlineWeightLoader, test_nonlocal_w13_after_quantization`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +3/-0 (3 lines); hunks: -651,6 +651,9 @@ def online_mxfp4_moe_weight_loader(; symbols: online_mxfp4_moe_weight_loader，涉及 `online_mxfp4_moe_weight_loader`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py` modified +50/-11 (61 lines); hunks: -1,17 +1,8; -21,6 +12,7; symbols: test_apply_weights_defaults_swiglu_limit_zero_without_clamp, TestOnlineWeightLoader, test_nonlocal_w13_after_quantization, test_nonlocal_w2_after_quantization
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +3/-0 (3 lines); hunks: -651,6 +651,9 @@ def online_mxfp4_moe_weight_loader(; symbols: online_mxfp4_moe_weight_loader
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py
@@ -1,17 +1,8 @@
-"""Unit tests for the Quark W4A4 MXFP4 MoE clamped-SwiGLU plumbing.
-CPU-only, no model loading and no aiter/ROCm dependency: they exercise the
-pure-Python control flow in ``QuarkW4A4MXFp4MoE.create_moe_runner`` and
-``apply_weights`` that decides whether the AITER MoE runner is driven on the
-clamped-SwiGLU path (``activation="swiglu"`` + ``swiglu_limit``) or the plain
-SiLU path. See the regression these guard against: clamped-SwiGLU MXFP4
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -651,6 +651,9 @@ def online_mxfp4_moe_weight_loader(
+            if copy_numel_counter.copied_numel == 0:
+                return
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py` modified +50/-11
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +3/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41389 - [Feat] [AMD] Quark: Run Quark MXFP4 MoE as W4A16 via triton_kernels on RDNA (gfx1151)

- 链接: https://github.com/sgl-project/sglang/pull/41389
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `2c6b95e035e8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+109/-1，可读 patch 149 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] [AMD] Quark: Run Quark MXFP4 MoE as W4A16 via triton_kernels on RDNA (gfx1151)」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[Feat] [AMD] Quark: Run Quark MXFP4 MoE as W4A16 via triton_kernels on RDNA (gfx1151)」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +109/-1 (110 lines); hunks: -122,6 +122,19 @@ def loader(param, loaded_weight, weight_name, shard_id, exp...; -247,7 +260,7 @@ def create_weights(; symbols: loader, QuarkW4A4MXFp4MoE, __init__, create_weights，涉及 `loader, QuarkW4A4MXFp4MoE, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +109/-1 (110 lines); hunks: -122,6 +122,19 @@ def loader(param, loaded_weight, weight_name, shard_id, exp...; -247,7 +260,7 @@ def create_weights(; symbols: loader, QuarkW4A4MXFp4MoE, __init__, create_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -122,6 +122,19 @@ def loader(param, loaded_weight, weight_name, shard_id, expert_id, *args, **kw):
+# HIP GPUs without FP4 hardware or an AITER FP4 MoE kernel (e.g. gfx1151 / Strix
+# Halo) cannot run the AITER path: its scales are laid out for gfx950 and its
+# kernels produce garbage there. Run the MoE as W4A16 instead: keep the packed
+# MXFP4 weights and upcast them inside triton_kernels' matmul, with bf16
+# activations. SGLANG_QUARK_MXFP4_MOE_W4A16=0 opts out.
+_use_triton_w4a16 = (
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +109/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46800 - [Fix] [AMD] quark: Keep MXFP8 shared experts out of the MXFP4 fused slot on dense-first models

- 链接: https://github.com/sgl-project/sglang/pull/46800
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/quark.py`, `test/registered/unit/layers/quantization/test_quark_config.py`；关联提交 `16a3bf3d9db7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+245/-7，可读 patch 324 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [AMD] quark: Keep MXFP8 shared experts out of the MXFP4 fused slot on dense-first models」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`；技术摘要: 覆盖「[Fix] [AMD] quark: Keep MXFP8 shared experts out of the MXFP4 fused slot on dense-first models」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_config.py` modified +94/-0 (94 lines); hunks: -633,6 +633,100 @@ def test_unpadded_weights_pass_through_unchanged(self):; symbols: test_unpadded_weights_pass_through_unchanged, TestSharedExpertFusionGateDenseLeadingLayers, _config, test_shared_expert_in_another_format_blocks_fusion，涉及 `test_unpadded_weights_pass_through_unchanged, TestSharedExpertFusionGateDenseLeadingLayers, _config`；`python/sglang/srt/layers/quantization/quark/quark.py` modified +30/-6 (36 lines); hunks: -299,6 +299,10 @@ def _build_excluded_fp8_config(config: Dict[str, Any]) -> O...; -1276,14 +1280,17 @@ def can_fuse_shared_expert(self) -> bool:; symbols: _build_excluded_fp8_config, can_fuse_shared_expert, _named_moe_layers, QuarkLinearMethod，涉及 `_build_excluded_fp8_config, can_fuse_shared_expert, _named_moe_layers`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_config.py` modified +94/-0 (94 lines); hunks: -633,6 +633,100 @@ def test_unpadded_weights_pass_through_unchanged(self):; symbols: test_unpadded_weights_pass_through_unchanged, TestSharedExpertFusionGateDenseLeadingLayers, _config, test_shared_expert_in_another_format_blocks_fusion
  - `python/sglang/srt/layers/quantization/quark/quark.py` modified +30/-6 (36 lines); hunks: -299,6 +299,10 @@ def _build_excluded_fp8_config(config: Dict[str, Any]) -> O...; -1276,14 +1280,17 @@ def can_fuse_shared_expert(self) -> bool:; symbols: _build_excluded_fp8_config, can_fuse_shared_expert, _named_moe_layers, QuarkLinearMethod
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_config.py
@@ -633,6 +633,100 @@ def test_unpadded_weights_pass_through_unchanged(self):
+_MXFP8_LINEAR_SPEC = {
+    "weight": {
+        "dtype": "fp8_e4m3",
+        "qscheme": "per_block",
+        "block_size": [1, 32],
+        "is_dynamic": False,
diff -- python/sglang/srt/layers/quantization/quark/quark.py
@@ -299,6 +299,10 @@ def _build_excluded_fp8_config(config: Dict[str, Any]) -> Optional["Fp8Config"]:
+_NAMED_MOE_LAYER = re.compile(
+    r"((?:.+\.)?layers\.\d+)\.mlp\.(?:experts|shared_experts?)(?:\..+)?"
+)
@@ -1276,14 +1280,17 @@ def can_fuse_shared_expert(self) -> bool:
-        # Compare routed vs shared specs at layer 0 and the draft block (stub module
-        # needed by _find_matched_config; an unmatched name -> ValueError -> cannot fuse).
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_config.py` modified +94/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/quark.py` modified +30/-6
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #47408 - [Fix] [AMD] quark: Fix the EP>1 crash in the Quark MXFP4 W4A16 MoE path and restrict it to gfx1151

- 链接: https://github.com/sgl-project/sglang/pull/47408
- 状态/时间: merged / 2026-10-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py`；关联提交 `fb3396260545`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+209/-14，可读 patch 268 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [AMD] quark: Fix the EP>1 crash in the Quark MXFP4 W4A16 MoE path and restrict it to gfx1151」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[Fix] [AMD] quark: Fix the EP>1 crash in the Quark MXFP4 W4A16 MoE path and restrict it to gfx1151」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py` added +168/-0 (168 lines); hunks: -0,0 +1,168; symbols: _random_weights, u8, _build_rank, _run，涉及 `_random_weights, u8, _build_rank`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +38/-14 (52 lines); hunks: -8,6 +8,7; -122,17 +123,13 @@ def loader(param, loaded_weight, weight_name, shard_id, ex...; symbols: loader, _process_weights_triton_w4a16, _apply_triton_w4a16，涉及 `loader, _process_weights_triton_w4a16, _apply_triton_w4a16`。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py` added +168/-0 (168 lines); hunks: -0,0 +1,168; symbols: _random_weights, u8, _build_rank, _run
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +38/-14 (52 lines); hunks: -8,6 +8,7; -122,17 +123,13 @@ def loader(param, loaded_weight, weight_name, shard_id, ex...; symbols: loader, _process_weights_triton_w4a16, _apply_triton_w4a16
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py
@@ -0,0 +1,168 @@
+"""Quark MXFP4 MoE W4A16 (triton_kernels) path on gfx1151.
+The path must only replace the AITER path on gfx1151; other AMD GPUs keep AITER.
+With EP > 1 the dispatcher maps experts owned by other ranks to -1; the W4A16
+path must drop those slots instead of indexing with -1 (a GPU memory fault).
+"""
+import importlib
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -8,6 +8,7 @@
+from sglang.srt.environ import envs
@@ -122,17 +123,13 @@ def loader(param, loaded_weight, weight_name, shard_id, expert_id, *args, **kw):
-# HIP GPUs without FP4 hardware or an AITER FP4 MoE kernel (e.g. gfx1151 / Strix
-# Halo) cannot run the AITER path: its scales are laid out for gfx950 and its
-# kernels produce garbage there. Run the MoE as W4A16 instead: keep the packed
-# MXFP4 weights and upcast them inside triton_kernels' matmul, with bf16
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py` added +168/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +38/-14
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37367 - [Perf] [AMD] moe: Resolve MoRI dispatch from the AITER activation contract

- 链接: https://github.com/sgl-project/sglang/pull/37367
- 状态/时间: merged / 2026-10-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`；关联提交 `ef4f3f1151f1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+252/-17，可读 patch 368 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] [AMD] moe: Resolve MoRI dispatch from the AITER activation contract」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`；技术摘要: 覆盖「[Perf] [AMD] moe: Resolve MoRI dispatch from the AITER activation contract」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +19/-2 (21 lines); hunks: -975,6 +975,11 @@ def _shuffle_gu_interleaved(self, layer: torch.nn.Module) -...; -1008,7 +1013,12 @@ def process_weights_after_loading(self, layer: torch.nn.M...; symbols: _shuffle_gu_interleaved, process_weights_after_loading, create_moe_runner，涉及 `_shuffle_gu_interleaved, process_weights_after_loading, create_moe_runner`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` modified +10/-1 (11 lines); hunks: -407,8 +407,17 @@ def process_weights_after_loading(self, layer: torch.nn.Mod...; symbols: process_weights_after_loading, create_moe_runner，涉及 `process_weights_after_loading, create_moe_runner`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +19/-2 (21 lines); hunks: -975,6 +975,11 @@ def _shuffle_gu_interleaved(self, layer: torch.nn.Module) -...; -1008,7 +1013,12 @@ def process_weights_after_loading(self, layer: torch.nn.M...; symbols: _shuffle_gu_interleaved, process_weights_after_loading, create_moe_runner
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` modified +10/-1 (11 lines); hunks: -407,8 +407,17 @@ def process_weights_after_loading(self, layer: torch.nn.Mod...; symbols: process_weights_after_loading, create_moe_runner
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -975,6 +975,11 @@ def _shuffle_gu_interleaved(self, layer: torch.nn.Module) -> None:
+        from sglang.srt.layers.moe.moe_runner.aiter import AiterQuantType
+        from sglang.srt.layers.moe.token_dispatcher.base import (
+            build_dispatcher_quant_config,
+        )
@@ -1008,7 +1013,12 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
-                    {"weight_dtype": torch.float4_e2m1fn_x2}
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py
@@ -407,8 +407,17 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
+            from sglang.srt.layers.moe.moe_runner.aiter import AiterQuantType
+            from sglang.srt.layers.moe.token_dispatcher.base import (
+                build_dispatcher_quant_config,
+            )
-            layer.dispatcher.set_quant_config({"weight_dtype": torch.float4_e2m1fn_x2})
+            layer.dispatcher.set_quant_config(
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +19/-2; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py` modified +10/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/token_dispatcher/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #45332 - [Fix] [AMD] quark: Load MXFP4 MoE checkpoints on gfx95 and gfx1250 without SGLANG_USE_AITER

- 链接: https://github.com/sgl-project/sglang/pull/45332
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_config.py`；关联提交 `e0c7992d0d48`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+74/-1，可读 patch 97 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [AMD] quark: Load MXFP4 MoE checkpoints on gfx95 and gfx1250 without SGLANG_USE_AITER」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 缺陷修复；主要 diff: `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[Fix] [AMD] quark: Load MXFP4 MoE checkpoints on gfx95 and gfx1250 without SGLANG_USE_AITER」；主要实现面是 `test/registered/unit/layers/quantization/test_quark_config.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/layers/quantization/test_quark_config.py` modified +69/-0 (69 lines); hunks: -4,6 +4,8; -457,6 +459,73 @@ def test_fused_wqkv_a_takes_the_wq_a_block_fp8_spec(self):; symbols: test_fused_wqkv_a_takes_the_wq_a_block_fp8_spec, _stub, _fake_aiter_shuffle_modules, TestQuarkMxfp4MoEShuffleImports，涉及 `test_fused_wqkv_a_takes_the_wq_a_block_fp8_spec, _stub, _fake_aiter_shuffle_modules`；`python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +5/-1 (6 lines); hunks: -44,8 +44,12。
- 代码 diff 细节:
  - `test/registered/unit/layers/quantization/test_quark_config.py` modified +69/-0 (69 lines); hunks: -4,6 +4,8; -457,6 +459,73 @@ def test_fused_wqkv_a_takes_the_wq_a_block_fp8_spec(self):; symbols: test_fused_wqkv_a_takes_the_wq_a_block_fp8_spec, _stub, _fake_aiter_shuffle_modules, TestQuarkMxfp4MoEShuffleImports
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +5/-1 (6 lines); hunks: -44,8 +44,12
- 关键代码摘录:

```diff
diff -- test/registered/unit/layers/quantization/test_quark_config.py
@@ -4,6 +4,8 @@
+import importlib
+import os
@@ -457,6 +459,73 @@ def test_fused_wqkv_a_takes_the_wq_a_block_fp8_spec(self):
+def _stub(*args, **kwargs):
+    return None
+def _fake_aiter_shuffle_modules():
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -44,8 +44,12 @@
-_use_aiter = get_bool_env_var("SGLANG_USE_AITER") and _is_hip
+# This scheme runs only on the AITER runner, so on the arches AITER has an MXFP4
+# MoE layout for, that layout is bound whatever SGLANG_USE_AITER says.
+_use_aiter = _is_hip and (
+    get_bool_env_var("SGLANG_USE_AITER") or _is_gfx95 or is_gfx1250_supported()
+)
```

- 已读文件:
  - tests: `test/registered/unit/layers/quantization/test_quark_config.py` modified +69/-0
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +5/-1
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41639 - [Feat] [AMD] moe: Add native GLM MXFP4 Triton Gluon backend

- 链接: https://github.com/sgl-project/sglang/pull/41639
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；关联提交 `f6127bf96ead`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 26 个文件，+7546/-14，可读 patch 7709 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] [AMD] moe: Add native GLM MXFP4 Triton Gluon backend」；模型线: Mixtral Quark INT4/FP8 MoE；类别: 性能/后端优化；主要 diff: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`；技术摘要: 覆盖「[Feat] [AMD] moe: Add native GLM MXFP4 Triton Gluon backend」；主要实现面是 `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +16/-3 (19 lines); hunks: -975,9 +975,10 @@ def process_weights_after_loading(self, layer: torch.nn.Mod...; -1057,6 +1058,10 @@ def process_weights_after_loading(self, layer: torch.nn.M...; symbols: process_weights_after_loading, create_moe_runner，涉及 `process_weights_after_loading, create_moe_runner`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +16/-3 (19 lines); hunks: -975,9 +975,10 @@ def process_weights_after_loading(self, layer: torch.nn.Mod...; -1057,6 +1058,10 @@ def process_weights_after_loading(self, layer: torch.nn.M...; symbols: process_weights_after_loading, create_moe_runner
- 关键代码摘录:

```diff
diff -- python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py
@@ -975,9 +975,10 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
-        if not getattr(self, "_owns_moe_runner", False):
+        if not getattr(self, "_owns_moe_weight_layout", False):
-                "Quark MXFP4 weight preshuffling requires an owned AITER runner."
+                "Quark MXFP4 weight preshuffling requires a backend that owns "
+                "the resulting weight layout."
@@ -1057,6 +1058,10 @@ def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
```

- 已读文件:
  - runtime: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` modified +16/-3
- 验证与风险: diff 自带测试面 `python/sglang/test/kernels/gluon_moe_reference.py`, `test/registered/kernels/ops/moe/test_gluon_moe_gfx950.py`, `test/registered/unit/models/test_gluon_moe_backend.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
