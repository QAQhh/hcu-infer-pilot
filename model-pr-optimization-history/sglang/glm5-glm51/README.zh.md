# sglang GLM-5/5.1 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/GLM/GLM-5.1.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` | [#31554](https://github.com/sgl-project/sglang/pull/31554), [#34379](https://github.com/sgl-project/sglang/pull/34379), [#35368](https://github.com/sgl-project/sglang/pull/35368), [#36440](https://github.com/sgl-project/sglang/pull/36440), [#39106](https://github.com/sgl-project/sglang/pull/39106), [#39230](https://github.com/sgl-project/sglang/pull/39230), [#39406](https://github.com/sgl-project/sglang/pull/39406), [#40148](https://github.com/sgl-project/sglang/pull/40148), [#40570](https://github.com/sgl-project/sglang/pull/40570), [#41597](https://github.com/sgl-project/sglang/pull/41597), [#42167](https://github.com/sgl-project/sglang/pull/42167), [#42278](https://github.com/sgl-project/sglang/pull/42278), ... (16 total) |
| `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` | [#36440](https://github.com/sgl-project/sglang/pull/36440), [#36519](https://github.com/sgl-project/sglang/pull/36519), [#36544](https://github.com/sgl-project/sglang/pull/36544), [#36608](https://github.com/sgl-project/sglang/pull/36608), [#36660](https://github.com/sgl-project/sglang/pull/36660), [#36719](https://github.com/sgl-project/sglang/pull/36719), [#36740](https://github.com/sgl-project/sglang/pull/36740), [#37109](https://github.com/sgl-project/sglang/pull/37109), [#37380](https://github.com/sgl-project/sglang/pull/37380), [#38522](https://github.com/sgl-project/sglang/pull/38522), [#39213](https://github.com/sgl-project/sglang/pull/39213), [#39273](https://github.com/sgl-project/sglang/pull/39273), ... (20 total) |
| `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` | [#36827](https://github.com/sgl-project/sglang/pull/36827), [#37392](https://github.com/sgl-project/sglang/pull/37392), [#40497](https://github.com/sgl-project/sglang/pull/40497), [#45513](https://github.com/sgl-project/sglang/pull/45513), [#46825](https://github.com/sgl-project/sglang/pull/46825) |
| `docs/cookbook/autoregressive/GLM/GLM-5.mdx` | 无直接 PR 号提交 |
| `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` | [#42726](https://github.com/sgl-project/sglang/pull/42726), [#43083](https://github.com/sgl-project/sglang/pull/43083), [#43799](https://github.com/sgl-project/sglang/pull/43799), [#43983](https://github.com/sgl-project/sglang/pull/43983), [#44065](https://github.com/sgl-project/sglang/pull/44065), [#45513](https://github.com/sgl-project/sglang/pull/45513) |
| `docs/src/snippets/agentx/zai-org/glm-5.3.jsx` | [#45513](https://github.com/sgl-project/sglang/pull/45513) |
| `docs/src/snippets/autoregressive/glm-5-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/glm-51-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx` | [#31554](https://github.com/sgl-project/sglang/pull/31554) |
| `docs/src/snippets/configs/zai-org/glm-5.2.jsx` | [#33935](https://github.com/sgl-project/sglang/pull/33935), [#34379](https://github.com/sgl-project/sglang/pull/34379), [#39106](https://github.com/sgl-project/sglang/pull/39106), [#39230](https://github.com/sgl-project/sglang/pull/39230), [#39406](https://github.com/sgl-project/sglang/pull/39406), [#40148](https://github.com/sgl-project/sglang/pull/40148), [#40570](https://github.com/sgl-project/sglang/pull/40570), [#41109](https://github.com/sgl-project/sglang/pull/41109), [#42109](https://github.com/sgl-project/sglang/pull/42109), [#42167](https://github.com/sgl-project/sglang/pull/42167), [#42613](https://github.com/sgl-project/sglang/pull/42613), [#45642](https://github.com/sgl-project/sglang/pull/45642), ... (13 total) |
| `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx` | [#36827](https://github.com/sgl-project/sglang/pull/36827) |
| `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` | [#36440](https://github.com/sgl-project/sglang/pull/36440), [#36513](https://github.com/sgl-project/sglang/pull/36513), [#36519](https://github.com/sgl-project/sglang/pull/36519), [#36544](https://github.com/sgl-project/sglang/pull/36544), [#36608](https://github.com/sgl-project/sglang/pull/36608), [#36660](https://github.com/sgl-project/sglang/pull/36660), [#37109](https://github.com/sgl-project/sglang/pull/37109), [#37380](https://github.com/sgl-project/sglang/pull/37380), [#37412](https://github.com/sgl-project/sglang/pull/37412), [#37576](https://github.com/sgl-project/sglang/pull/37576), [#39213](https://github.com/sgl-project/sglang/pull/39213), [#40036](https://github.com/sgl-project/sglang/pull/40036), ... (15 total) |
| `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` | [#36440](https://github.com/sgl-project/sglang/pull/36440), [#36513](https://github.com/sgl-project/sglang/pull/36513), [#36519](https://github.com/sgl-project/sglang/pull/36519), [#36544](https://github.com/sgl-project/sglang/pull/36544), [#36608](https://github.com/sgl-project/sglang/pull/36608), [#36660](https://github.com/sgl-project/sglang/pull/36660), [#36740](https://github.com/sgl-project/sglang/pull/36740), [#37109](https://github.com/sgl-project/sglang/pull/37109), [#37380](https://github.com/sgl-project/sglang/pull/37380), [#37412](https://github.com/sgl-project/sglang/pull/37412), [#37576](https://github.com/sgl-project/sglang/pull/37576), [#38522](https://github.com/sgl-project/sglang/pull/38522), ... (21 total) |
| `docs/src/snippets/configs/zai-org/glm-5.3.jsx` | [#36827](https://github.com/sgl-project/sglang/pull/36827), [#36950](https://github.com/sgl-project/sglang/pull/36950), [#37392](https://github.com/sgl-project/sglang/pull/37392), [#40497](https://github.com/sgl-project/sglang/pull/40497) |
| `python/sglang/srt/arg_groups/glm5_next_hook.py` | [#42905](https://github.com/sgl-project/sglang/pull/42905) |
| `python/sglang/srt/configs/glm5_next.py` | [#36507](https://github.com/sgl-project/sglang/pull/36507), [#42044](https://github.com/sgl-project/sglang/pull/42044), [#44093](https://github.com/sgl-project/sglang/pull/44093), [#44098](https://github.com/sgl-project/sglang/pull/44098) |
| `python/sglang/srt/models/glm5_next.py` | [#36507](https://github.com/sgl-project/sglang/pull/36507), [#38546](https://github.com/sgl-project/sglang/pull/38546), [#38621](https://github.com/sgl-project/sglang/pull/38621), [#39200](https://github.com/sgl-project/sglang/pull/39200), [#39273](https://github.com/sgl-project/sglang/pull/39273), [#39688](https://github.com/sgl-project/sglang/pull/39688), [#39720](https://github.com/sgl-project/sglang/pull/39720), [#40466](https://github.com/sgl-project/sglang/pull/40466), [#41161](https://github.com/sgl-project/sglang/pull/41161), [#41198](https://github.com/sgl-project/sglang/pull/41198), [#41870](https://github.com/sgl-project/sglang/pull/41870), [#42044](https://github.com/sgl-project/sglang/pull/42044), ... (13 total) |
| `python/sglang/srt/models/glm5_next_nextn.py` | [#36507](https://github.com/sgl-project/sglang/pull/36507), [#39779](https://github.com/sgl-project/sglang/pull/39779), [#42044](https://github.com/sgl-project/sglang/pull/42044) |
| `python/sglang/srt/parser/glm53_chat_template.py` | [#45154](https://github.com/sgl-project/sglang/pull/45154) |
| `python/sglang/test/glm53_flash_common.py` | [#44892](https://github.com/sgl-project/sglang/pull/44892) |
| `scripts/ci/slurm/recipes/mi355x-fp4/glm51/1k1k/1p1d-dp8ep8-mtp.yaml` | 无直接 PR 号提交 |
| `scripts/ci/slurm/recipes/mi355x-fp4/glm51/1k1k/1p1d-dp8ep8.yaml` | 无直接 PR 号提交 |
| `scripts/ci/slurm/recipes/mi355x-fp4/glm51/1k1k/1p1d-mtp.yaml` | 无直接 PR 号提交 |
| `scripts/ci/slurm/recipes/mi355x-fp4/glm51/1k1k/1p1d.yaml` | 无直接 PR 号提交 |
| `scripts/ci/slurm/recipes/mi355x-fp4/glm51/1k1k/2p1d-ep16-mtp.yaml` | 无直接 PR 号提交 |
| `scripts/ci/slurm/recipes/mi355x-fp4/glm51/1k1k/2p1d-ep16.yaml` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py` | [#22336](https://github.com/sgl-project/sglang/pull/22336) |
| `test/registered/amd/accuracy/mi30x/test_glm51_hisparse_eval_mi30x.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py` | [#41602](https://github.com/sgl-project/sglang/pull/41602) |
| `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` | [#18911](https://github.com/sgl-project/sglang/pull/18911), [#21710](https://github.com/sgl-project/sglang/pull/21710) |
| `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py` | [#22336](https://github.com/sgl-project/sglang/pull/22336) |
| `test/registered/amd/accuracy/mi35x/test_glm51_hisparse_eval_mi35x.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py` | [#26396](https://github.com/sgl-project/sglang/pull/26396) |
| `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py` | [#32570](https://github.com/sgl-project/sglang/pull/32570) |
| `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py` | [#41602](https://github.com/sgl-project/sglang/pull/41602) |
| `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py` | [#36903](https://github.com/sgl-project/sglang/pull/36903) |
| `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` | [#18911](https://github.com/sgl-project/sglang/pull/18911), [#21710](https://github.com/sgl-project/sglang/pull/21710) |
| `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py` | [#21773](https://github.com/sgl-project/sglang/pull/21773) |
| `test/registered/amd/perf/mi30x/test_glm51_perf_amd.py` | [#22336](https://github.com/sgl-project/sglang/pull/22336) |
| `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py` | [#21710](https://github.com/sgl-project/sglang/pull/21710) |
| `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py` | [#22336](https://github.com/sgl-project/sglang/pull/22336) |
| `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py` | [#32570](https://github.com/sgl-project/sglang/pull/32570) |
| `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py` | [#21773](https://github.com/sgl-project/sglang/pull/21773) |
| `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py` | [#21710](https://github.com/sgl-project/sglang/pull/21710) |
| `test/registered/dcp/test_glm53_dcp2.py` | [#43735](https://github.com/sgl-project/sglang/pull/43735) |
| `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py` | [#43774](https://github.com/sgl-project/sglang/pull/43774) |
| `test/registered/e2e/models/test_dsa_glm52_dp_mtp.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_dsa_glm52_hisparse.py` | [#44192](https://github.com/sgl-project/sglang/pull/44192), [#44256](https://github.com/sgl-project/sglang/pull/44256), [#44303](https://github.com/sgl-project/sglang/pull/44303), [#44597](https://github.com/sgl-project/sglang/pull/44597) |
| `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py` | [#38725](https://github.com/sgl-project/sglang/pull/38725) |
| `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` | [#38725](https://github.com/sgl-project/sglang/pull/38725), [#39816](https://github.com/sgl-project/sglang/pull/39816) |
| `test/registered/e2e/models/test_dsa_glm52_pd_kv_shard_hicache.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py` | [#41207](https://github.com/sgl-project/sglang/pull/41207) |
| `test/registered/e2e/models/test_dsa_glm52_tp_mtp.py` | 无直接 PR 号提交 |
| `test/registered/e2e/models/test_glm53_flash_b200.py` | [#40862](https://github.com/sgl-project/sglang/pull/40862), [#42845](https://github.com/sgl-project/sglang/pull/42845), [#43774](https://github.com/sgl-project/sglang/pull/43774), [#43975](https://github.com/sgl-project/sglang/pull/43975) |
| `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py` | [#44892](https://github.com/sgl-project/sglang/pull/44892) |
| `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py` | [#44892](https://github.com/sgl-project/sglang/pull/44892) |
| `test/registered/e2e/models_large/test_glm52_fp8.py` | 无直接 PR 号提交 |
| `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` | [#38546](https://github.com/sgl-project/sglang/pull/38546), [#41464](https://github.com/sgl-project/sglang/pull/41464) |
| `test/registered/gb300/test_glm52_nvfp4.py` | 无直接 PR 号提交 |
| `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py` | [#41161](https://github.com/sgl-project/sglang/pull/41161) |
| `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py` | [#36459](https://github.com/sgl-project/sglang/pull/36459) |
| `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py` | [#38775](https://github.com/sgl-project/sglang/pull/38775) |
| `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py` | [#47611](https://github.com/sgl-project/sglang/pull/47611) |
| `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py` | [#47611](https://github.com/sgl-project/sglang/pull/47611) |
| `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | [#38775](https://github.com/sgl-project/sglang/pull/38775) |
| `test/registered/npu/performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms.py` | 无直接 PR 号提交 |
| `test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_glm52.py` | 无直接 PR 号提交 |
| `test/registered/radix_cache/unified_radix_tree/linker/test_unified_cache_linker_kl_glm52.py` | 无直接 PR 号提交 |
| `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py` | [#36281](https://github.com/sgl-project/sglang/pull/36281) |
| `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm53_bcg.py` | 无直接 PR 号提交 |
| `test/registered/unit/layer_boundary/test_glm5_next_dflash_capture.py` | 无直接 PR 号提交 |
| `test/registered/unit/models/test_glm5_next_bfg_fusion.py` | [#39688](https://github.com/sgl-project/sglang/pull/39688), [#41870](https://github.com/sgl-project/sglang/pull/41870) |
| `test/registered/unit/models/test_glm5_next_modelopt.py` | [#38621](https://github.com/sgl-project/sglang/pull/38621), [#39273](https://github.com/sgl-project/sglang/pull/39273), [#39779](https://github.com/sgl-project/sglang/pull/39779) |
| `test/registered/unit/parser/test_glm53_chat_template.py` | [#45154](https://github.com/sgl-project/sglang/pull/45154) |

## PR 覆盖总览

- git 追溯 PR 数: 93
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 93
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-25 | [#18911](https://github.com/sgl-project/sglang/pull/18911) | merged | [AMD] [GLM-5 Day 0] Add GLM-5 nightly test | `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` |
| 2026-04-08 | [#21710](https://github.com/sgl-project/sglang/pull/21710) | merged | [AMD] Add GLM-5-FP8 nightly performance benchmarks for MI30x and MI35x | `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` |
| 2026-04-09 | [#22336](https://github.com/sgl-project/sglang/pull/22336) | merged | [AMD] Add GLM-5.1-FP8 nightly accuracy and performance benchmarks for MI30x and MI35x | `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py`, `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py` |
| 2026-04-15 | [#21773](https://github.com/sgl-project/sglang/pull/21773) | merged | [AMD][CI] Add GLM-5-MXFP4 accuracy and perf nightly tests for MI35x | `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py` |
| 2026-05-27 | [#26396](https://github.com/sgl-project/sglang/pull/26396) | merged | [AMD] [CI] Add GLM-5.1 MXFP4 TP2 accuracy gate | `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py` |
| 2026-08-07 | [#33935](https://github.com/sgl-project/sglang/pull/33935) | merged | Clean GLM-5.2 NVFP4 cookbook | `docs/src/snippets/configs/zai-org/glm-5.2.jsx` |
| 2026-08-12 | [#34379](https://github.com/sgl-project/sglang/pull/34379) | merged | [AMD] GLM 5.2 MXFP4 SGLANG COOKBOOK | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-08-14 | [#31554](https://github.com/sgl-project/sglang/pull/31554) | merged | [Docs] Fill GLM-5.2 H200 FP8 speed cells (low-latency, balanced); fix MTP notation | `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-08-20 | [#32570](https://github.com/sgl-project/sglang/pull/32570) | merged | [AMD] Add GLM-5.2 MI35x nightly accuracy and perf benchmark | `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py` |
| 2026-08-26 | [#36281](https://github.com/sgl-project/sglang/pull/36281) | merged | [Unified Cache]: add glm5.2 per commit ci | `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py` |
| 2026-08-26 | [#36440](https://github.com/sgl-project/sglang/pull/36440) | merged | Add GLM-5.3-Flash cookbook | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-08-26 | [#36513](https://github.com/sgl-project/sglang/pull/36513) | merged | GLM-5.3-Flash cookbook: FP8 KV + TRT-LLM benchmark cards and Blackwell default | `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` |
| 2026-08-26 | [#36519](https://github.com/sgl-project/sglang/pull/36519) | merged | GLM-5.3-Flash cookbook: default Blackwell recipes to FP8 KV + TRT-LLM DSA | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-08-27 | [#36608](https://github.com/sgl-project/sglang/pull/36608) | merged | [AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-08-27 | [#36660](https://github.com/sgl-project/sglang/pull/36660) | merged | cookbook: fix GLM-5.3-Flash speculative flag, size Hopper memory, record GSM8K | `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-08-27 | [#36719](https://github.com/sgl-project/sglang/pull/36719) | merged | [Docs] GLM-5.3-Flash: point at compute-mamba-ratio for the KDA/KV pool split | `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-08-27 | [#36544](https://github.com/sgl-project/sglang/pull/36544) | merged | GLM-5.3-Flash cookbook: HiCache for LL, fusion-flag drop, EAGLE, default-cell numbers, DCP4 overlay | `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-08-27 | [#36740](https://github.com/sgl-project/sglang/pull/36740) | merged | cookbook: add a Speculative card to the GLM-5.3-Flash playground | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-08-28 | [#36827](https://github.com/sgl-project/sglang/pull/36827) | merged | [Docs] Add GLM-5.3 cookbook | `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` |
| 2026-08-29 | [#36950](https://github.com/sgl-project/sglang/pull/36950) | merged | [Docs] Restore the AIME25 label so GLM-5.3 FP8 and BF16 scores render again | `docs/src/snippets/configs/zai-org/glm-5.3.jsx` |
| 2026-08-31 | [#36459](https://github.com/sgl-project/sglang/pull/36459) | merged | [NPU] Fix evalscope accuracy parsing and add glm5_1 aime26 request timeout | `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py` |
| 2026-09-01 | [#37109](https://github.com/sgl-project/sglang/pull/37109) | merged | [Docs] Add NVFP4 section to GLM-5.3-Flash cookbook | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-09-01 | [#37380](https://github.com/sgl-project/sglang/pull/37380) | merged | Revert "[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)" | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-09-01 | [#37392](https://github.com/sgl-project/sglang/pull/37392) | merged | [Cookbook] Add the DFlash2 speculative option to GLM-5.3 | `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` |
| 2026-09-01 | [#37412](https://github.com/sgl-project/sglang/pull/37412) | merged | [Docs] GLM-5.3-Flash cookbook: add NVFP4 FP8+TRT-LLM benchmark rows (follow-up to #37109) | `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` |
| 2026-09-02 | [#35368](https://github.com/sgl-project/sglang/pull/35368) | merged | Update GLM-5.2 NVFP4 B200/B300 for AgentX HiCache | `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-09-03 | [#37576](https://github.com/sgl-project/sglang/pull/37576) | merged | [Docs] GLM-5.3-Flash cookbook: drop stale EP caveat, add B300/H100/B200 FP8 speed data | `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` |
| 2026-09-06 | [#36507](https://github.com/sgl-project/sglang/pull/36507) | merged | GLM-5.3-Flash support | `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py` |
| 2026-09-09 | [#38725](https://github.com/sgl-project/sglang/pull/38725) | merged | Relax GSM8K thresholds for the GLM-5.2 DSA-MTP variants | `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` |
| 2026-09-09 | [#38621](https://github.com/sgl-project/sglang/pull/38621) | merged | [Model] Support GLM-5.3 Flash NVFP4 loading | `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next.py` |
| 2026-09-10 | [#38522](https://github.com/sgl-project/sglang/pull/38522) | merged | Add Opt-In for GLM-5.3 Flash breakable prefill CUDA graphs | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-09-10 | [#38775](https://github.com/sgl-project/sglang/pull/38775) | merged | [NPU] Set DEEPEP_HYBRID_DEPLOYMENT for new DeepEP tests; switch glm5_2 to w8a8; tune nightly timeouts | `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py` |
| 2026-09-11 | [#39106](https://github.com/sgl-project/sglang/pull/39106) | merged | [AMD] Use the triton DSA backend for GLM-5.2 MXFP4 on MI355X | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-09-12 | [#39213](https://github.com/sgl-project/sglang/pull/39213) | merged | [Docs] GLM-5.3-Flash cookbook: fixed MTP 5/1/6, EP1 + flashinfer_trtllm on Blackwell | `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-09-12 | [#39230](https://github.com/sgl-project/sglang/pull/39230) | merged | [AMD] Document GLM-5.2 MXFP4 recipe update on MI355X | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-09-14 | [#39406](https://github.com/sgl-project/sglang/pull/39406) | merged | [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916 | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-09-16 | [#39720](https://github.com/sgl-project/sglang/pull/39720) | merged | [Fix] Fix GLM5 mHC PP forward | `python/sglang/srt/models/glm5_next.py` |
| 2026-09-17 | [#40036](https://github.com/sgl-project/sglang/pull/40036) | merged | [Docs] GLM-5.3-Flash cookbook: temporarily remove the DCP option | `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-09-18 | [#40148](https://github.com/sgl-project/sglang/pull/40148) | merged | [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916, use HIP Top-K | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-09-20 | [#39688](https://github.com/sgl-project/sglang/pull/39688) | merged | Fuse GLM-5.3-Flash KDA projections and prefill metadata | `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_bfg_fusion.py` |
| 2026-09-20 | [#39200](https://github.com/sgl-project/sglang/pull/39200) | merged | [Perf] Fuse the glm5_next mHC attn->MLP boundary | `python/sglang/srt/models/glm5_next.py` |
| 2026-09-21 | [#40570](https://github.com/sgl-project/sglang/pull/40570) | merged | [AMD] Enable HiCache for GLM-5.2 MI355X throughput recipe | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-09-22 | [#38546](https://github.com/sgl-project/sglang/pull/38546) | merged | [AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950 | `python/sglang/srt/models/glm5_next.py`, `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` |
| 2026-09-22 | [#40497](https://github.com/sgl-project/sglang/pull/40497) | merged | [Docs] GLM-5.3/5.3-Flash cookbooks: enable reasoning/tool-call parsers by default via auto | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-09-22 | [#39779](https://github.com/sgl-project/sglang/pull/39779) | merged | [AMD] [GLM-5.3-Flash Day 0] Load the MXFP4 MTP draft layer | `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next_nextn.py` |
| 2026-09-23 | [#40466](https://github.com/sgl-project/sglang/pull/40466) | merged | [deepep_v2] support GLM-5.3-Flash (Glm5NextForConditionalGeneration) | `python/sglang/srt/models/glm5_next.py` |
| 2026-09-23 | [#40862](https://github.com/sgl-project/sglang/pull/40862) | merged | [CI] Update GLM-5.3-Flash H200/B200 test args | `test/registered/e2e/models/test_glm53_flash_b200.py` |
| 2026-09-24 | [#39816](https://github.com/sgl-project/sglang/pull/39816) | merged | Refactor the Cute-DSL AR fusion to support DeepseekV2 archs (GLM-5.3, etc.) | `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` |
| 2026-09-24 | [#41109](https://github.com/sgl-project/sglang/pull/41109) | merged | [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260923 daily | `docs/src/snippets/configs/zai-org/glm-5.2.jsx` |
| 2026-09-25 | [#41207](https://github.com/sgl-project/sglang/pull/41207) | merged | [CI] Move GLM-5.2 layer-split test to extra-b-test-8-gpu-b300 | `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py` |
| 2026-09-25 | [#41198](https://github.com/sgl-project/sglang/pull/41198) | merged | [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit | `python/sglang/srt/models/glm5_next.py` |
| 2026-09-28 | [#36903](https://github.com/sgl-project/sglang/pull/36903) | merged | [AMD] Add GLM-5.3-Flash MI35x nightly test | `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py` |
| 2026-09-28 | [#41161](https://github.com/sgl-project/sglang/pull/41161) | merged | [AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950 | `python/sglang/srt/models/glm5_next.py`, `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py` |
| 2026-09-28 | [#41597](https://github.com/sgl-project/sglang/pull/41597) | merged | [Docs][AMD] Update GLM-5.2 MI355X daily image | `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-09-29 | [#41464](https://github.com/sgl-project/sglang/pull/41464) | merged | [AMD] Fix GLM-5.3 quark MoE MI35x test runner config | `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` |
| 2026-09-29 | [#41602](https://github.com/sgl-project/sglang/pull/41602) | merged | [AMD] Add GLM-5.3 MI30x and MI35x nightly accuracy tests | `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py` |
| 2026-10-01 | [#41986](https://github.com/sgl-project/sglang/pull/41986) | merged | [Docs] Add NVIDIA NVFP4 checkpoint to GLM-5.3-Flash cookbook | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-10-01 | [#39273](https://github.com/sgl-project/sglang/pull/39273) | merged | [AMD] [GLM-5.3-Flash] Enable FP8 and MXFP4 serving on gfx950 | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next.py` |
| 2026-10-02 | [#42109](https://github.com/sgl-project/sglang/pull/42109) | merged | [Docs] GLM-5.2 GB300 NVFP4: add env vars from InferenceX AgentX recipe | `docs/src/snippets/configs/zai-org/glm-5.2.jsx` |
| 2026-10-02 | [#42278](https://github.com/sgl-project/sglang/pull/42278) | merged | [Docs][AMD] Update GLM-5.2 MI355X daily image to 20260930 | `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-10-03 | [#41870](https://github.com/sgl-project/sglang/pull/41870) | merged | [AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4 | `test/registered/unit/models/test_glm5_next_bfg_fusion.py`, `python/sglang/srt/models/glm5_next.py` |
| 2026-10-06 | [#42167](https://github.com/sgl-project/sglang/pull/42167) | merged | [Docs] GLM-5.2: move GB300 AgentX recipe to the agentic HiCache section and drop no-op settings | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-10-06 | [#42613](https://github.com/sgl-project/sglang/pull/42613) | merged | docs(cookbook): enable Top-K v2 for GLM-5.2 MI355X MTP | `docs/src/snippets/configs/zai-org/glm-5.2.jsx` |
| 2026-10-06 | [#42693](https://github.com/sgl-project/sglang/pull/42693) | merged | [GLM-5.3-Flash] Autotune MoE kernels at prefill sizes | `python/sglang/srt/models/glm5_next.py` |
| 2026-10-07 | [#42905](https://github.com/sgl-project/sglang/pull/42905) | merged | [KDA] Default GLM-5-Next spec verify to the CuTe DSL KDA kernel | `python/sglang/srt/arg_groups/glm5_next_hook.py` |
| 2026-10-07 | [#43015](https://github.com/sgl-project/sglang/pull/43015) | merged | [Docs] GLM-5.3-Flash: measured MI355X MXFP4 agentic recipe | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-10-08 | [#42726](https://github.com/sgl-project/sglang/pull/42726) | merged | [Docs] Cookbook: interactive SemiAnalysis InferenceX AgentX launches for GLM-5.2, DeepSeek-V4 and DeepSeek-V4.1 | `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-10-09 | [#42044](https://github.com/sgl-project/sglang/pull/42044) | merged | [CP] GLM-5.3-Flash Prefill CP implemented on layer boundaries | `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py`, `python/sglang/srt/configs/glm5_next.py` |
| 2026-10-09 | [#43083](https://github.com/sgl-project/sglang/pull/43083) | merged | [Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1 | `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` |
| 2026-10-09 | [#42845](https://github.com/sgl-project/sglang/pull/42845) | merged | [GLM-5.3-Flash] Enable breakable prefill CUDA graph by default | `test/registered/e2e/models/test_glm53_flash_b200.py` |
| 2026-10-12 | [#43802](https://github.com/sgl-project/sglang/pull/43802) | merged | [Docs] Update GLM-5.3-Flash playground: B300 default, CP8, EP and PD | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-10-12 | [#43799](https://github.com/sgl-project/sglang/pull/43799) | merged | [Docs] Cookbook: refresh SemiAnalysis AgentX launches (GLM-5.2 B300, DeepSeek-V4.1 GB300) | `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` |
| 2026-10-13 | [#43983](https://github.com/sgl-project/sglang/pull/43983) | merged | [Docs] Cookbook: refresh SemiAnalysis AgentX launches (DeepSeek-V4.1 GB200/GB300, GLM-5.2 FP8 B300) | `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` |
| 2026-10-13 | [#43975](https://github.com/sgl-project/sglang/pull/43975) | merged | [CI] Use sgl-eval for GLM-5.3-Flash GSM8K tests | `test/registered/e2e/models/test_glm53_flash_b200.py` |
| 2026-10-13 | [#41790](https://github.com/sgl-project/sglang/pull/41790) | merged | [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.3-Flash with BF16 KV Cache | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-10-13 | [#43735](https://github.com/sgl-project/sglang/pull/43735) | merged | [DCP] Decode context parallelism for DSA (GLM-5.2 / GLM-5.3) with MTP | `test/registered/dcp/test_glm53_dcp2.py` |
| 2026-10-14 | [#44098](https://github.com/sgl-project/sglang/pull/44098) | merged | [GLM-5.3-Flash] Drop the NextN layer from the KDA state pool | `python/sglang/srt/configs/glm5_next.py` |
| 2026-10-14 | [#44192](https://github.com/sgl-project/sglang/pull/44192) | merged | [CI] glm5.2: Temporarily disable PD HiSparse+MTP B300 test | `test/registered/e2e/models/test_dsa_glm52_hisparse.py` |
| 2026-10-14 | [#44065](https://github.com/sgl-project/sglang/pull/44065) | merged | [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main (GLM-5.2 NVFP4 B300 agg TP4, Dynamo frontend counts) | `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` |
| 2026-10-14 | [#44256](https://github.com/sgl-project/sglang/pull/44256) | merged | [Fix] glm5.2: Align PD HiSparse prefill KV layout | `test/registered/e2e/models/test_dsa_glm52_hisparse.py` |
| 2026-10-14 | [#44303](https://github.com/sgl-project/sglang/pull/44303) | merged | [Fix] glm5.2: Align HiSparse warmup backends and move test to nightly | `test/registered/e2e/models/test_dsa_glm52_hisparse.py` |
| 2026-10-15 | [#44093](https://github.com/sgl-project/sglang/pull/44093) | merged | [Fix] glm5_next: Correct num_experts_per_tok default to 8 | `python/sglang/srt/configs/glm5_next.py` |
| 2026-10-17 | [#44597](https://github.com/sgl-project/sglang/pull/44597) | merged | [CI] glm5.2: Keep EOS in HiSparse needle test output | `test/registered/e2e/models/test_dsa_glm52_hisparse.py` |
| 2026-10-18 | [#44892](https://github.com/sgl-project/sglang/pull/44892) | merged | [Fix] [H200] ci: Split GLM-5.3-Flash serving recipes into separate tests | `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py`, `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py`, `python/sglang/test/glm53_flash_common.py` |
| 2026-10-20 | [#45154](https://github.com/sgl-project/sglang/pull/45154) | merged | [Feat] glm-5.3: Render GLM-5.3 and GLM-5.3-Flash chat prompts with a Python chat template | `test/registered/unit/parser/test_glm53_chat_template.py`, `python/sglang/srt/parser/glm53_chat_template.py` |
| 2026-10-21 | [#45326](https://github.com/sgl-project/sglang/pull/45326) | merged | [Doc] cookbook: add TPU7x recipe for GLM-5.3-Flash | `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` |
| 2026-10-21 | [#45513](https://github.com/sgl-project/sglang/pull/45513) | merged | [Doc] cookbook: Add GLM-5.3 AgentX section and refresh with eight open InferenceX PRs | `docs/src/snippets/agentx/zai-org/glm-5.3.jsx`, `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` |
| 2026-10-23 | [#43774](https://github.com/sgl-project/sglang/pull/43774) | merged | [Feat] glm5.3flash: Support padded CP BCG and prefix replay with PD/DFlash2 | `test/registered/e2e/models/test_glm53_flash_b200.py`, `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py` |
| 2026-10-26 | [#45642](https://github.com/sgl-project/sglang/pull/45642) | merged | [Doc] [NPU] cookbook: add A3 deployment scenarios to GLM-5.2 | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-10-29 | [#46825](https://github.com/sgl-project/sglang/pull/46825) | merged | [Doc] [AMD] cookbook: Add GLM-5.3 MI355X AgentX recipe | `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` |
| 2026-10-30 | [#47331](https://github.com/sgl-project/sglang/pull/47331) | merged | [Doc] [AMD] cookbook: Add DCP4 to the GLM-5.2 MI355X MXFP4 high-throughput recipe | `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-10-31 | [#47615](https://github.com/sgl-project/sglang/pull/47615) | merged | [Doc] [AMD] cookbook: Add GLM-5.2 MI355X AgentX recipe | `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` |
| 2026-11-02 | [#47611](https://github.com/sgl-project/sglang/pull/47611) | merged | [Test] [Ascend] npu: Add GLM-5.2 2P2D gpqa cases and unify evalscope retry loop | `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py` |

## 逐 PR diff 审计卡

### PR #18911 - [AMD] [GLM-5 Day 0] Add GLM-5 nightly test

- 链接: https://github.com/sgl-project/sglang/pull/18911
- 状态/时间: merged / 2026-02-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`；关联提交 `23adb50751d5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+635/-1，可读 patch 725 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [GLM-5 Day 0] Add GLM-5 nightly test」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`；技术摘要: 覆盖「[AMD] [GLM-5 Day 0] Add GLM-5 nightly test」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples，涉及 `ModelConfig, get_display_name, get_one_example`；`test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` added +244/-0 (244 lines); hunks: -0,0 +1,244; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples，涉及 `ModelConfig, get_display_name, get_one_example`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples
  - `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` added +244/-0 (244 lines); hunks: -0,0 +1,244; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples
- 关键代码摘录:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py
@@ -0,0 +1,249 @@
+"""MI35x GLM-5 GSM8K Completion Evaluation Test (8-GPU)
+Tests GLM-5 with NSA attention backend using few-shot completion
+benchmark on MI35x.
+Registry: nightly-amd-8-gpu-mi35x-glm5 suite
+"""
+import ast
diff -- test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py
@@ -0,0 +1,244 @@
+"""AMD GLM-5 GSM8K Completion Evaluation Test (8-GPU)
+Tests GLM-5 with NSA attention backend using few-shot completion
+benchmark on MI325/MI300X.
+Registry: nightly-amd-accuracy-8-gpu-glm5 suite
+"""
+import ast
```

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` added +249/-0; `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` added +244/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21710 - [AMD] Add GLM-5-FP8 nightly performance benchmarks for MI30x and MI35x

- 链接: https://github.com/sgl-project/sglang/pull/21710
- 状态/时间: merged / 2026-04-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py`, `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py`；关联提交 `db60a620dbf1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+345/-5，可读 patch 448 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add GLM-5-FP8 nightly performance benchmarks for MI30x and MI35x」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`；技术摘要: 覆盖「[AMD] Add GLM-5-FP8 nightly performance benchmarks for MI30x and MI35x」；主要实现面是 `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: generate_simple_markdown_report, TestGLM5PerfMI35x, setUpClass, test_glm5_perf，涉及 `generate_simple_markdown_report, TestGLM5PerfMI35x, setUpClass`；`test/registered/amd/perf/mi30x/test_glm5_perf_amd.py` added +140/-0 (140 lines); hunks: -0,0 +1,140; symbols: generate_simple_markdown_report, TestNightlyGLM5Performance, setUpClass, test_bench_glm5，涉及 `generate_simple_markdown_report, TestNightlyGLM5Performance, setUpClass`；`test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` modified +6/-2 (8 lines); hunks: -59,13 +59,17 @@ def get_display_name(self) -> str:; -77,7 +81,7 @@ def get_display_name(self) -> str:; symbols: get_display_name，涉及 `get_display_name`；`test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` modified +6/-2 (8 lines); hunks: -64,13 +64,17 @@ def get_display_name(self) -> str:; -82,7 +86,7 @@ def get_display_name(self) -> str:; symbols: get_display_name，涉及 `get_display_name`。
- 代码 diff 细节:
  - `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: generate_simple_markdown_report, TestGLM5PerfMI35x, setUpClass, test_glm5_perf
  - `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py` added +140/-0 (140 lines); hunks: -0,0 +1,140; symbols: generate_simple_markdown_report, TestNightlyGLM5Performance, setUpClass, test_bench_glm5
  - `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` modified +6/-2 (8 lines); hunks: -59,13 +59,17 @@ def get_display_name(self) -> str:; -77,7 +81,7 @@ def get_display_name(self) -> str:; symbols: get_display_name
  - `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` modified +6/-2 (8 lines); hunks: -64,13 +64,17 @@ def get_display_name(self) -> str:; -82,7 +86,7 @@ def get_display_name(self) -> str:; symbols: get_display_name
- 关键代码摘录:

```diff
diff -- test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py
@@ -0,0 +1,143 @@
+"""MI35x Nightly performance benchmark for GLM-5.
+Tests GLM-5 with NSA attention backend using bench_one_batch on 8 GPUs.
+Registry: nightly-perf-8-gpu-mi35x-glm5 suite
+"""
+import os
+os.environ.setdefault("HF_HOME", "/data2/models/huggingface")
diff -- test/registered/amd/perf/mi30x/test_glm5_perf_amd.py
@@ -0,0 +1,140 @@
+"""Nightly performance benchmark for GLM-5 on MI30x.
+Tests GLM-5 with NSA attention backend using bench_one_batch on 8 GPUs.
+Model paths can be configured via environment variables:
+- GLM5_MODEL_PATH: Path to GLM-5 model (default: zai-org/GLM-5-FP8)
+Example usage:
+    python -m pytest test_glm5_perf_amd.py -v
diff -- test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py
@@ -59,13 +59,17 @@ def get_display_name(self) -> str:
```

- 已读文件:
  - tests: `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py` added +143/-0; `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py` added +140/-0; `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` modified +6/-2; `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` modified +6/-2
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py`, `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22336 - [AMD] Add GLM-5.1-FP8 nightly accuracy and performance benchmarks for MI30x and MI35x

- 链接: https://github.com/sgl-project/sglang/pull/22336
- 状态/时间: merged / 2026-04-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_glm51_perf_amd.py`, `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py`；关联提交 `ef6bfc1197ab`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+918/-25，可读 patch 1064 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add GLM-5.1-FP8 nightly accuracy and performance benchmarks for MI30x and MI35x」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py`, `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py`；技术摘要: 覆盖「[AMD] Add GLM-5.1-FP8 nightly accuracy and performance benchmarks for MI30x and MI35x」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py`, `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py` added +242/-0 (242 lines); hunks: -0,0 +1,242; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples，涉及 `ModelConfig, get_display_name, get_one_example`；`test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py` added +238/-0 (238 lines); hunks: -0,0 +1,238; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples，涉及 `ModelConfig, get_display_name, get_one_example`；`test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestGLM51PerfMI35x, setUpClass, test_glm51_perf，涉及 `generate_simple_markdown_report, TestGLM51PerfMI35x, setUpClass`；`test/registered/amd/perf/mi30x/test_glm51_perf_amd.py` added +138/-0 (138 lines); hunks: -0,0 +1,138; symbols: generate_simple_markdown_report, TestNightlyGLM51Performance, setUpClass, test_bench_glm51，涉及 `generate_simple_markdown_report, TestNightlyGLM51Performance, setUpClass`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py` added +242/-0 (242 lines); hunks: -0,0 +1,242; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples
  - `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py` added +238/-0 (238 lines); hunks: -0,0 +1,238; symbols: ModelConfig, get_display_name, get_one_example, get_few_shot_examples
  - `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestGLM51PerfMI35x, setUpClass, test_glm51_perf
  - `test/registered/amd/perf/mi30x/test_glm51_perf_amd.py` added +138/-0 (138 lines); hunks: -0,0 +1,138; symbols: generate_simple_markdown_report, TestNightlyGLM51Performance, setUpClass, test_bench_glm51
- 关键代码摘录:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py
@@ -0,0 +1,242 @@
+"""MI35x GLM-5.1 GSM8K Completion Evaluation Test (8-GPU)
+Tests GLM-5.1-FP8 with NSA attention backend using few-shot
+completion benchmark on MI35x.
+Registry: nightly-amd-8-gpu-mi35x-glm51 suite
+"""
+import ast
diff -- test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py
@@ -0,0 +1,238 @@
+"""AMD GLM-5.1 GSM8K Completion Evaluation Test (8-GPU)
+Tests GLM-5.1-FP8 with NSA attention backend using few-shot
+completion benchmark on MI325/MI300X.
+Registry: nightly-amd-accuracy-8-gpu-glm51 suite
+"""
+import ast
diff -- test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py
@@ -0,0 +1,146 @@
```

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py` added +242/-0; `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py` added +238/-0; `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py` added +146/-0; `test/registered/amd/perf/mi30x/test_glm51_perf_amd.py` added +138/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi30x/test_glm51_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_glm51_perf_amd.py`, `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21773 - [AMD][CI] Add GLM-5-MXFP4 accuracy and perf nightly tests for MI35x

- 链接: https://github.com/sgl-project/sglang/pull/21773
- 状态/时间: merged / 2026-04-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py`；关联提交 `39c6bf730c41`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+528/-130，可读 patch 821 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD][CI] Add GLM-5-MXFP4 accuracy and perf nightly tests for MI35x」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py`；技术摘要: 覆盖「[AMD][CI] Add GLM-5-MXFP4 accuracy and perf nightly tests for MI35x」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: get_model_path, ModelConfig, __post_init__, get_display_name，涉及 `get_model_path, ModelConfig, __post_init__`；`test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py` added +187/-0 (187 lines); hunks: -0,0 +1,187; symbols: generate_simple_markdown_report, get_model_path, TestGLM5MXFP4PerfMI35x, setUpClass，涉及 `generate_simple_markdown_report, get_model_path, TestGLM5MXFP4PerfMI35x`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: get_model_path, ModelConfig, __post_init__, get_display_name
  - `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py` added +187/-0 (187 lines); hunks: -0,0 +1,187; symbols: generate_simple_markdown_report, get_model_path, TestGLM5MXFP4PerfMI35x, setUpClass
- 关键代码摘录:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py
@@ -0,0 +1,281 @@
+"""MI35x GLM-5-MXFP4 GSM8K Completion Evaluation Test (8-GPU)
+Tests the AMD Quark MXFP4-quantized GLM-5 model using few-shot
+completion benchmark on MI35x.
+Model: amd/GLM-5-MXFP4 (MOE-only MXFP4 quantization of zai-org/GLM-5)
+Reference: https://huggingface.co/amd/GLM-5-MXFP4
+Registry: nightly-amd-8-gpu-mi35x-glm5-mxfp4 suite
diff -- test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py
@@ -0,0 +1,187 @@
+"""MI35x Nightly performance benchmark for GLM-5-MXFP4 model.
+Benchmarks the AMD Quark MXFP4-quantized GLM-5 model on MI35x with 8 GPUs.
+Model: amd/GLM-5-MXFP4 (MOE-only MXFP4 quantization of zai-org/GLM-5)
+Reference: https://huggingface.co/amd/GLM-5-MXFP4
+Registry: nightly-perf-8-gpu-mi35x-glm5-mxfp4 suite
+"""
```

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py` added +281/-0; `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py` added +187/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_glm5_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm5_mxfp4_perf_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26396 - [AMD] [CI] Add GLM-5.1 MXFP4 TP2 accuracy gate

- 链接: https://github.com/sgl-project/sglang/pull/26396
- 状态/时间: merged / 2026-05-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py`；关联提交 `d44584e8d8b2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+144/-0，可读 patch 145 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [CI] Add GLM-5.1 MXFP4 TP2 accuracy gate」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py`；技术摘要: 覆盖「[AMD] [CI] Add GLM-5.1 MXFP4 TP2 accuracy gate」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py` added +144/-0 (144 lines); hunks: -0,0 +1,144; symbols: _raise_nofile_limit, _get_model_path, TestGLM51MXFP4TP2GSM8KMI35x, setUpClass，涉及 `_raise_nofile_limit, _get_model_path, TestGLM51MXFP4TP2GSM8KMI35x`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py` added +144/-0 (144 lines); hunks: -0,0 +1,144; symbols: _raise_nofile_limit, _get_model_path, TestGLM51MXFP4TP2GSM8KMI35x, setUpClass
- 关键代码摘录:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py
@@ -0,0 +1,144 @@
+"""MI355X GLM-5.1-MXFP4 TP=2 GSM8K accuracy gate.
+This is a PR Test (AMD) regression test for the GLM-5.1-MXFP4 TP=2
+accuracy drop seen on MI355X/gfx950 when aiter selected a bad BF16 GEMM path.
+Registry: stage-c-test-large-8-gpu-amd-mi35x suite
+"""
+import os
```

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py` added +144/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #33935 - Clean GLM-5.2 NVFP4 cookbook

- 链接: https://github.com/sgl-project/sglang/pull/33935
- 状态/时间: merged / 2026-08-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `0c3a76fa0a5b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+0/-4，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Clean GLM-5.2 NVFP4 cookbook」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「Clean GLM-5.2 NVFP4 cookbook」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +0/-4 (4 lines); hunks: -763,8 +763,6 @@ sgl-eval run aime25 \\; -830,8 +828,6 @@ sgl-eval run aime25 \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +0/-4 (4 lines); hunks: -763,8 +763,6 @@ sgl-eval run aime25 \\; -830,8 +828,6 @@ sgl-eval run aime25 \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -763,8 +763,6 @@ sgl-eval run aime25 \\
-        "--kv-cache-dtype fp8_e4m3",
-        "--bf16-gemm-backend cutedsl",
@@ -830,8 +828,6 @@ sgl-eval run aime25 \\
-        "--kv-cache-dtype fp8_e4m3",
-        "--bf16-gemm-backend cutedsl",
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +0/-4
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #34379 - [AMD] GLM 5.2 MXFP4 SGLANG COOKBOOK

- 链接: https://github.com/sgl-project/sglang/pull/34379
- 状态/时间: merged / 2026-08-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `b5d1453ed26b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+1266/-1153，可读 patch 2446 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] GLM 5.2 MXFP4 SGLANG COOKBOOK」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[AMD] GLM 5.2 MXFP4 SGLANG COOKBOOK」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +1258/-1151 (2409 lines); hunks: -1,1151 +1,1258; symbols: kernels，涉及 `kernels`；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +8/-2 (10 lines); hunks: -70,7 +70,7 @@ import { Playground } from "/src/snippets/_playground.jsx";; -96,12 +96,17 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +1258/-1151 (2409 lines); hunks: -1,1151 +1,1258; symbols: kernels
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +8/-2 (10 lines); hunks: -70,7 +70,7 @@ import { Playground } from "/src/snippets/_playground.jsx";; -96,12 +96,17 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -1,1151 +1,1258 @@
-// Single `export const config` literal — no spreads/calls/IIFE (Mintlify re-evals at hydration).
-// Cells are denormalized: no `--nnodes`/`--node-rank`/`--dist-init-addr`/`--host`/`--port` literals — engine injects them.
-export const config = {
-  modelName: "GLM-5.2",
-  supportedHardware: [
-    "h200", "b200", "gb300", "b300",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -70,7 +70,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-**GLM-5.2** is Z.ai's flagship Mixture-of-Experts model built on **DeepSeek Sparse Attention (DSA)**: a lightning indexer selects a sparse set of key tokens per query (top-2048),
+**GLM-5.2** is Z.ai's flagship Mixture-of-Experts model built on **DeepSeek Sparse Attention (DSA)**: a lightning indexer selects a sparse set of key tokens per query (top-2048),
@@ -96,12 +96,17 @@ import { Playground } from "/src/snippets/_playground.jsx";
+    <tr>
+      <td style={{padding: "9px 12px"}}><strong><a href="https://huggingface.co/amd/GLM-5.2-MXFP4">GLM-5.2-MXFP4</a></strong></td>
+      <td style={{padding: "9px 12px"}}>MoE · DSA · 256 experts (top-8) · MTP · MXFP4</td>
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +1258/-1151; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +8/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #31554 - [Docs] Fill GLM-5.2 H200 FP8 speed cells (low-latency, balanced); fix MTP notation

- 链接: https://github.com/sgl-project/sglang/pull/31554
- 状态/时间: merged / 2026-08-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`；关联提交 `22dde1dd5b56`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+36/-5，可读 patch 55 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Fill GLM-5.2 H200 FP8 speed cells (low-latency, balanced); fix MTP notation」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Docs] Fill GLM-5.2 H200 FP8 speed cells (low-latency, balanced); fix MTP notation」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx` modified +35/-4 (39 lines); hunks: -3,10 +3,41；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -57,7 +57,7 @@ import { benchmarks } from "/src/snippets/configs/zai-org/glm-...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx` modified +35/-4 (39 lines); hunks: -3,10 +3,41
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -57,7 +57,7 @@ import { benchmarks } from "/src/snippets/configs/zai-org/glm-...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx
@@ -3,10 +3,41 @@
-  // ---- H200 + FP8 ----  (serve recipe in glm-5.2.jsx; benchmark pending re-measurement)
-  { match: { hw: "h200", variant: "default", quant: "fp8", strategy: "low-latency", nodes: "single" } },
-  { match: { hw: "h200", variant: "default", quant: "fp8", strategy: "balanced", nodes: "single" } },
-  { match: { hw: "h200", variant: "default", quant: "fp8", strategy: "high-throughput", nodes: "single" } },
+  // ---- H200 + FP8 ----  (8-GPU single node; serve recipe in glm-5.2.jsx; real weights,
+  // --random-range-ratio 1.0, flush-cache every run)
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -57,7 +57,7 @@ import { benchmarks } from "/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx
-  Speed numbers are measured with `--random-range-ratio 1.0`, `--flush-cache`, on `main @ 09ca4fc`. Spec cells pin the EAGLE acceptance length via the serve env `SGLANG_SIMULATE_A
+  Speed numbers are measured with `--random-range-ratio 1.0`, `--flush-cache`, on `main @ 09ca4fc` (H200 FP8 cells: `v0.5.14 @ 49e384ce`). Spec cells pin the EAGLE acceptance leng
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx` modified +35/-4; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #32570 - [AMD] Add GLM-5.2 MI35x nightly accuracy and perf benchmark

- 链接: https://github.com/sgl-project/sglang/pull/32570
- 状态/时间: merged / 2026-08-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py`；关联提交 `02b93e7e01cd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+231/-10，可读 patch 300 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add GLM-5.2 MI35x nightly accuracy and perf benchmark」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py`；技术摘要: 覆盖「[AMD] Add GLM-5.2 MI35x nightly accuracy and perf benchmark」；主要实现面是 `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py` added +106/-0 (106 lines); hunks: -0,0 +1,106; symbols: TestGLM52FP8PerfMI35x, setUpClass, test_glm52_fp8_perf，涉及 `TestGLM52FP8PerfMI35x, setUpClass, test_glm52_fp8_perf`；`test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py` added +103/-0 (103 lines); hunks: -0,0 +1,103; symbols: TestGLM52FP8EvalMI35x, test_glm_52_fp8，涉及 `TestGLM52FP8EvalMI35x, test_glm_52_fp8`。
- 代码 diff 细节:
  - `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py` added +106/-0 (106 lines); hunks: -0,0 +1,106; symbols: TestGLM52FP8PerfMI35x, setUpClass, test_glm52_fp8_perf
  - `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py` added +103/-0 (103 lines); hunks: -0,0 +1,103; symbols: TestGLM52FP8EvalMI35x, test_glm_52_fp8
- 关键代码摘录:

```diff
diff -- test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py
@@ -0,0 +1,106 @@
+"""MI35x nightly performance benchmark for GLM-5.2-FP8 (8-GPU).
+Benchmarks zai-org/GLM-5.2-FP8 at TP8 with the cookbook's MI355X / FP8 /
+low-latency / single-node server configuration. At 8K-input / 1K-output,
+batch 1 and 16 are the concurrency points the cookbook publishes, so drift from
+the recipe shows up directly; 8 and 64 extend the sweep to keep the batch range
+the retired GLM-5.1 MI35x benchmark used to cover.
diff -- test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py
@@ -0,0 +1,103 @@
+"""MI35x GLM-5.2-FP8 GSM8K Accuracy Evaluation Test (8-GPU)
+Tests zai-org/GLM-5.2-FP8 with the DSA tilelang backend on MI35x (gfx950).
+Server arguments track the GLM-5.2 cookbook's MI355X / FP8 / low-latency /
+single-node cell: TP8, DSA tilelang prefill+decode, 131072 chunked prefill,
+0.80 static memory fraction, and a 20-minute watchdog for weight loading.
+That cell ships as `verified: true` with published benchmarks, but nothing in
```

- 已读文件:
  - tests: `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py` added +106/-0; `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py` added +103/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py`, `test/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36281 - [Unified Cache]: add glm5.2 per commit ci

- 链接: https://github.com/sgl-project/sglang/pull/36281
- 状态/时间: merged / 2026-08-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py`；关联提交 `bec624827235`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+207/-263，可读 patch 501 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Unified Cache]: add glm5.2 per commit ci」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py`；技术摘要: 覆盖「[Unified Cache]: add glm5.2 per commit ci」；主要实现面是 `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py` added +85/-0 (85 lines); hunks: -0,0 +1,85; symbols: TestGLM5UnifiedRadixCacheL3Accuracy, setUpClass, tearDownClass，涉及 `TestGLM5UnifiedRadixCacheL3Accuracy, setUpClass, tearDownClass`。
- 代码 diff 细节:
  - `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py` added +85/-0 (85 lines); hunks: -0,0 +1,85; symbols: TestGLM5UnifiedRadixCacheL3Accuracy, setUpClass, tearDownClass
- 关键代码摘录:

```diff
diff -- test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py
@@ -0,0 +1,85 @@
+"""UnifiedRadixTree + HiCache accuracy tests for GLM-5.2.
+Runs GLM-5.2-FP8 with HiCache L3 (file backend) under UnifiedRadixTree,
+verifying accuracy stays stable across a cache flush.
+"""
+import os
+import shutil
```

- 已读文件:
  - tests: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py` added +85/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/kits/unified_radix_cache_kit.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36440 - Add GLM-5.3-Flash cookbook

- 链接: https://github.com/sgl-project/sglang/pull/36440
- 状态/时间: merged / 2026-08-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `dfc40e0efe10`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+850/-4，可读 patch 890 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add GLM-5.3-Flash cookbook」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「Add GLM-5.3-Flash cookbook」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` added +502/-0 (502 lines); hunks: -0,0 +1,502；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` added +80/-0 (80 lines); hunks: -0,0 +1,80；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` added +250/-0 (250 lines); hunks: -0,0 +1,250；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +0/-1 (1 lines); hunks: -1,7 +1,6。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` added +502/-0 (502 lines); hunks: -0,0 +1,502
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` added +80/-0 (80 lines); hunks: -0,0 +1,80
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` added +250/-0 (250 lines); hunks: -0,0 +1,250
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +0/-1 (1 lines); hunks: -1,7 +1,6
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -0,0 +1,502 @@
+export const config = {
+  modelName: "GLM-5.3-Flash",
+  supportedHardware: ["gb300", "h100", "h200", "b200", "b300", "gb200"],
+  matchDims: [
+    {
+      id: "strategy",
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -0,0 +1,80 @@
+export const benchmarks = [
+  {
+    match: { hw: "gb300", strategy: "low-latency" },
+    sglang_version: "f13cb6f6a7",
+    latencyPercentile: "Mean",
+    speed: [
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -0,0 +1,250 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` added +502/-0; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` added +80/-0; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` added +250/-0; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +0/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/docs.json`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36513 - GLM-5.3-Flash cookbook: FP8 KV + TRT-LLM benchmark cards and Blackwell default

- 链接: https://github.com/sgl-project/sglang/pull/36513
- 状态/时间: merged / 2026-08-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `f8cc1f9525c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+84/-4，可读 patch 123 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-5.3-Flash cookbook: FP8 KV + TRT-LLM benchmark cards and Blackwell default」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；技术摘要: 覆盖「GLM-5.3-Flash cookbook: FP8 KV + TRT-LLM benchmark cards and Blackwell default」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +66/-0 (66 lines); hunks: -21,6 +21,27 @@ export const benchmarks = [; -67,6 +88,51 @@ export const benchmarks = [；`docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +10/-2 (12 lines); hunks: -239,7 +239,11 @@ sgl-eval run gsm8k \\; -264,7 +268,11 @@ sgl-eval run gsm8k \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +66/-0 (66 lines); hunks: -21,6 +21,27 @@ export const benchmarks = [; -67,6 +88,51 @@ export const benchmarks = [
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +10/-2 (12 lines); hunks: -239,7 +239,11 @@ sgl-eval run gsm8k \\; -264,7 +268,11 @@ sgl-eval run gsm8k \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -21,6 +21,27 @@ export const benchmarks = [
+  {
+    match: { hw: "gb300", strategy: "low-latency", kvDsaPair: "fp8-trtllm" },
+    sglang_version: "f13cb6f6a7",
+    latencyPercentile: "Mean",
+    speed: [
+      {
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -239,7 +239,11 @@ sgl-eval run gsm8k \\
-      verificationStatus: (s) => config.isRecommendedSelection(s) ? "verified" : "unverified",
+      verificationStatus: (s) =>
+        config.isRecommendedSelection(s) ||
+        (s.kvDsaPair === "fp8-trtllm" && s.mmTransport === "auto" && s.hicache === "off")
+          ? "verified"
+          : "unverified",
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +66/-0; `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +10/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36519 - GLM-5.3-Flash cookbook: default Blackwell recipes to FP8 KV + TRT-LLM DSA

- 链接: https://github.com/sgl-project/sglang/pull/36519
- 状态/时间: merged / 2026-08-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `e27a7fac772b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+74/-53，可读 patch 335 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-5.3-Flash cookbook: default Blackwell recipes to FP8 KV + TRT-LLM DSA」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「GLM-5.3-Flash cookbook: default Blackwell recipes to FP8 KV + TRT-LLM DSA」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +60/-41 (101 lines); hunks: -15,8 +15,9 @@ export const config = {; -26,18 +27,8 @@ export const config = {；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +10/-9 (19 lines); hunks: -12,14 +12,14 @@ export const benchmarks = [; -34,13 +34,13 @@ export const benchmarks = [；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-3 (6 lines); hunks: -25,7 +25,7 @@ Choose your hardware, then choose the operating point that mat...; -65,7 +65,7 @@ GLM-5.3-Flash is a natively multimodal Mixture-of-Experts mode...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +60/-41 (101 lines); hunks: -15,8 +15,9 @@ export const config = {; -26,18 +27,8 @@ export const config = {
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +10/-9 (19 lines); hunks: -12,14 +12,14 @@ export const benchmarks = [; -34,13 +34,13 @@ export const benchmarks = [
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-3 (6 lines); hunks: -25,7 +25,7 @@ Choose your hardware, then choose the operating point that mat...; -65,7 +65,7 @@ GLM-5.3-Flash is a natively multimodal Mixture-of-Experts mode...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -15,8 +15,9 @@ export const config = {
+    const pairing = ["h100", "h200"].includes(s.hw) ? "bf16-tilelang" : "fp8-trtllm";
-      s.kvDsaPair === "bf16-tilelang" &&
+      s.kvDsaPair === pairing &&
@@ -26,18 +27,8 @@ export const config = {
-      default: "bf16-tilelang",
+      default: "fp8-trtllm",
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -12,14 +12,14 @@ export const benchmarks = [
-        ttft_ms: 589.2,
+        ttft_ms: 599.91,
-        tokens_per_sec_per_gpu: 2277.46,
+        tokens_per_sec_per_gpu: 2266.08,
-      "Measured on 4x GB300 (TP4/EP4) with the final weights (zai-org/GLM-5.3-Flash, c5b82b63e37b) at the rc2 cut (f13cb6f6a7), adaptive MTP 5/1/6 with SGLANG_SIMULATE_ACC_LEN=3 (
+      "Measured on 4x GB300 (TP4/EP4) with the final weights (zai-org/GLM-5.3-Flash, c5b82b63e37b) at the rc2 cut (f13cb6f6a7), adaptive MTP 5/1/6 with SGLANG_SIMULATE_ACC_LEN=3 (
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -25,7 +25,7 @@ Choose your hardware, then choose the operating point that matches your workload
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +60/-41; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +10/-9; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-3
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36608 - [AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X

- 链接: https://github.com/sgl-project/sglang/pull/36608
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `0f7b5b8b2a67`, `6c72b49a5796`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+112/-12，可读 patch 223 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +90/-7 (97 lines); hunks: -1,21 +1,32; -32,8 +43,8 @@ export const config = {；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +15/-0 (15 lines); hunks: -144,4 +144,19 @@ export const benchmarks = [；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +7/-5 (12 lines); hunks: -1,6 +1,6; -10,7 +10,7 @@ tag: NEW。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +90/-7 (97 lines); hunks: -1,21 +1,32; -32,8 +43,8 @@ export const config = {
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +15/-0 (15 lines); hunks: -144,4 +144,19 @@ export const benchmarks = [
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +7/-5 (12 lines); hunks: -1,6 +1,6; -10,7 +10,7 @@ tag: NEW
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -1,21 +1,32 @@
-  supportedHardware: ["gb300", "h100", "h200", "b200", "b300", "gb200"],
+  supportedHardware: [
+    "gb300", "h100", "h200", "b200", "b300", "gb200",
+    "mi300x", "mi325x", "mi355x",
+  ],
-        { id: "low-latency", label: "Low Latency", subtitle: "Adaptive MTP 5/1/6" },
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -144,4 +144,19 @@ export const benchmarks = [
+  {
+    match: { hw: "mi300x", strategy: "high-throughput" },
+    sglang_version: "9e692c9216",
+    accuracy: { gsm8k_pct: 97.35 },
+    notes:
+      "Accuracy-only validation on 8x MI300X (gfx942, TP8) with zai-org/GLM-5.3-Flash revision 3f1971b7b5f7a528c9c4ef6212c8785298a8c24a, SGLang PR #36607 head 9e692c9216c3b5e5c443
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -1,6 +1,6 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +90/-7; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +15/-0; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +7/-5
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36660 - cookbook: fix GLM-5.3-Flash speculative flag, size Hopper memory, record GSM8K

- 链接: https://github.com/sgl-project/sglang/pull/36660
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `636a6f7dbad2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+92/-26，可读 patch 243 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「cookbook: fix GLM-5.3-Flash speculative flag, size Hopper memory, record GSM8K」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「cookbook: fix GLM-5.3-Flash speculative flag, size Hopper memory, record GSM8K」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +56/-8 (64 lines); hunks: -134,14 +134,62 @@ export const benchmarks = [；`docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +34/-16 (50 lines); hunks: -277,7 +277,7 @@ sgl-eval run gsm8k \\; -317,20 +317,23 @@ sgl-eval run gsm8k \\；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +2/-2 (4 lines); hunks: -88,7 +88,7 @@ The deployment recipes use the checkpoint's generation configu...; -168,7 +168,7 @@ sglang serve \。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +56/-8 (64 lines); hunks: -134,14 +134,62 @@ export const benchmarks = [
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +34/-16 (50 lines); hunks: -277,7 +277,7 @@ sgl-eval run gsm8k \\; -317,20 +317,23 @@ sgl-eval run gsm8k \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +2/-2 (4 lines); hunks: -88,7 +88,7 @@ The deployment recipes use the checkpoint's generation configu...; -168,7 +168,7 @@ sglang serve \
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -134,14 +134,62 @@ export const benchmarks = [
-  { match: { hw: "h100", strategy: "low-latency" } },
-  { match: { hw: "h100", strategy: "high-throughput" } },
-  { match: { hw: "h200", strategy: "low-latency" } },
-  { match: { hw: "h200", strategy: "high-throughput" } },
-  { match: { hw: "b200", strategy: "low-latency" } },
-  { match: { hw: "b200", strategy: "high-throughput" } },
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -277,7 +277,7 @@ sgl-eval run gsm8k \\
-        "--speculative-algorithm NEXTN",
+        "--speculative-algorithm EAGLE",
@@ -317,20 +317,23 @@ sgl-eval run gsm8k \\
-      verified: false,
-      verificationStatus: (s) => config.isRecommendedSelection(s) ? "in-progress" : "unverified",
+      verified: true,
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -88,7 +88,7 @@ The deployment recipes use the checkpoint's generation configuration. Override s
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +56/-8; `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +34/-16; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +2/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36719 - [Docs] GLM-5.3-Flash: point at compute-mamba-ratio for the KDA/KV pool split

- 链接: https://github.com/sgl-project/sglang/pull/36719
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；关联提交 `46a544e0a067`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-0，可读 patch 11 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.3-Flash: point at compute-mamba-ratio for the KDA/KV pool split」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] GLM-5.3-Flash: point at compute-mamba-ratio for the KDA/KV pool split」；主要实现面是 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +4/-0 (4 lines); hunks: -35,6 +35,10 @@ import { benchmarks } from "/src/snippets/configs/zai-org/glm...。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +4/-0 (4 lines); hunks: -35,6 +35,10 @@ import { benchmarks } from "/src/snippets/configs/zai-org/glm...
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -35,6 +35,10 @@ import { benchmarks } from "/src/snippets/configs/zai-org/glm-5.3-flash-benchmar
+<Note>
+Generated commands leave `--mamba-full-memory-ratio` at its `0.9` default, which is a generic starting point rather than a workload-tuned split: too low starves the KDA state pool
+</Note>
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +4/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36544 - GLM-5.3-Flash cookbook: HiCache for LL, fusion-flag drop, EAGLE, default-cell numbers, DCP4 overlay

- 链接: https://github.com/sgl-project/sglang/pull/36544
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `d1f14431fdf0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+102/-53，可读 patch 382 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-5.3-Flash cookbook: HiCache for LL, fusion-flag drop, EAGLE, default-cell numbers, DCP4 overlay」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「GLM-5.3-Flash cookbook: HiCache for LL, fusion-flag drop, EAGLE, default-cell numbers, DCP4 overlay」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +74/-32 (106 lines); hunks: -1,7 +1,7; -12,18 +12,18 @@ export const benchmarks = [；`docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +22/-19 (41 lines); hunks: -30,7 +30,8 @@ export const config = {; -90,8 +91,6 @@ export const config = {；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-2 (8 lines); hunks: -88,7 +88,7 @@ The deployment recipes use the checkpoint's generation configu...; -102,10 +102,14 @@ Keep the checkpoint's KDA lower-bound setting unchanged. I...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +74/-32 (106 lines); hunks: -1,7 +1,7; -12,18 +12,18 @@ export const benchmarks = [
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +22/-19 (41 lines); hunks: -30,7 +30,8 @@ export const config = {; -90,8 +91,6 @@ export const config = {
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-2 (8 lines); hunks: -88,7 +88,7 @@ The deployment recipes use the checkpoint's generation configu...; -102,10 +102,14 @@ Keep the checkpoint's KDA lower-bound setting unchanged. I...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -1,7 +1,7 @@
-    sglang_version: "f13cb6f6a7",
+    sglang_version: "d6ab04bdf1",
@@ -12,18 +12,18 @@ export const benchmarks = [
-        ttft_ms: 599.91,
-        tpot_ms: 6.48,
-        tokens_per_sec_per_gpu: 2266.08,
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -30,7 +30,8 @@ export const config = {
-      s.hicache === "off"
+      s.hicache === "off" &&
+      s.dcp === "off"
@@ -90,8 +91,6 @@ export const config = {
-          disabled: (s) => s.strategy === "low-latency",
-          disableReason: "HiCache with MTP speculative decoding crashes at startup in the current build (DSA draft pool lacks full_kv_pool); use it with High Throughput only.",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -88,7 +88,7 @@ The deployment recipes use the checkpoint's generation configuration. Override s
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +74/-32; `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +22/-19; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36740 - cookbook: add a Speculative card to the GLM-5.3-Flash playground

- 链接: https://github.com/sgl-project/sglang/pull/36740
- 状态/时间: merged / 2026-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `6ccfeb59bcbc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+103/-2，可读 patch 168 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「cookbook: add a Speculative card to the GLM-5.3-Flash playground」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「cookbook: add a Speculative card to the GLM-5.3-Flash playground」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +66/-0 (66 lines); hunks: -267,6 +267,72 @@ sgl-eval run gsm8k \\；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +11/-1 (12 lines); hunks: -41,7 +41,7 @@ Generated commands leave `--mamba-full-memory-ratio` at its `0...; -96,6 +96,16 @@ Start with **Low Latency** for chat and agent workloads. Adap...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +66/-0 (66 lines); hunks: -267,6 +267,72 @@ sgl-eval run gsm8k \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +11/-1 (12 lines); hunks: -41,7 +41,7 @@ Generated commands leave `--mamba-full-memory-ratio` at its `0...; -96,6 +96,16 @@ Start with **Low Latency** for chat and agent workloads. Adap...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -267,6 +267,72 @@ sgl-eval run gsm8k \\
+    // ----- Card: "Speculative" -----
+    // The Deploy panel only picks speculation through the Strategy dim (Low
+    // Latency = the checkpoint's adaptive MTP head, High Throughput = off).
+    // This card is the finer control, and it adds the one algorithm no cell
+    // ships: DFlash2, whose draft is a separate checkpoint.
+    //
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -41,7 +41,7 @@ Generated commands leave `--mamba-full-memory-ratio` at its `0.9` default, which
-Use the Playground for lower-level tuning such as attention parallelism, MoE communication, and reasoning or tool parsers. It inherits every selection from the deployment panel an
+Use the Playground for lower-level tuning such as attention parallelism, MoE communication, speculative decoding, and reasoning or tool parsers. It inherits every selection from t
@@ -96,6 +96,16 @@ Start with **Low Latency** for chat and agent workloads. Adaptive MTP changes th
+### Change the speculative algorithm
+The **Speculative** card in the Playground changes the algorithm without leaving the selected strategy:
+- **EAGLE / Adaptive MTP 5-1-6** is exactly what Low Latency serves, so a Low Latency base starts on this chip. Pick it from a High Throughput base to keep that recipe's other set
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +66/-0; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +11/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36827 - [Docs] Add GLM-5.3 cookbook

- 链接: https://github.com/sgl-project/sglang/pull/36827
- 状态/时间: merged / 2026-08-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`；关联提交 `395c2258c374`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+1509/-0，可读 patch 1519 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Add GLM-5.3 cookbook」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`；技术摘要: 覆盖「[Docs] Add GLM-5.3 cookbook」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3.jsx` added +1028/-0 (1028 lines); hunks: -0,0 +1,1028；`docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx` added +221/-0 (221 lines); hunks: -0,0 +1,221；`docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` added +259/-0 (259 lines); hunks: -0,0 +1,259。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3.jsx` added +1028/-0 (1028 lines); hunks: -0,0 +1,1028
  - `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx` added +221/-0 (221 lines); hunks: -0,0 +1,221
  - `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` added +259/-0 (259 lines); hunks: -0,0 +1,259
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3.jsx
@@ -0,0 +1,1028 @@
+// Single `export const config` literal — no spreads/calls/IIFE (Mintlify re-evals at hydration).
+// Cells are denormalized: no `--nnodes`/`--node-rank`/`--dist-init-addr`/`--host`/`--port` literals — engine injects them.
+export const config = {
+  modelName: "GLM-5.3",
+  supportedHardware: [
+    "h200", "b200", "gb300", "b300",
diff -- docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx
@@ -0,0 +1,221 @@
+// GLM-5.3 benchmark placeholders, keyed by the same `match` tuple as glm-5.3.jsx cells.
+// Bare match stubs render as pending until speed and accuracy measurements are available.
+export const benchmarks = [
+  // NVIDIA FP8, single node.
+  {
+    match: { hw: "h200",  variant: "default", quant: "fp8", strategy: "low-latency",     nodes: "single" },
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3.mdx
@@ -0,0 +1,259 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3.jsx` added +1028/-0; `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx` added +221/-0; `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` added +259/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/docs.json`, `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36950 - [Docs] Restore the AIME25 label so GLM-5.3 FP8 and BF16 scores render again

- 链接: https://github.com/sgl-project/sglang/pull/36950
- 状态/时间: merged / 2026-08-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.3.jsx`；关联提交 `8a4c517a6007`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+9/-0，可读 patch 23 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Restore the AIME25 label so GLM-5.3 FP8 and BF16 scores render again」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3.jsx`；技术摘要: 覆盖「[Docs] Restore the AIME25 label so GLM-5.3 FP8 and BF16 scores render again」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +9/-0 (9 lines); hunks: -68,6 +68,14 @@ sgl-eval run gsm8k \\; -79,6 +87,7 @@ sgl-eval run aime26 \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +9/-0 (9 lines); hunks: -68,6 +68,14 @@ sgl-eval run gsm8k \\; -79,6 +87,7 @@ sgl-eval run aime26 \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3.jsx
@@ -68,6 +68,14 @@ sgl-eval run gsm8k \\
+  --model {{MODEL_NAME}} --api-key <api-key> \\
+  --n-repeats 16 --max-tokens 64000 \\
+  --temperature 1.0 --top-p 0.95 --thinking \\
+  --out-dir /sgl-workspace/logs \\
+  --base-url http://{{CURL_HOST}}:{{CURL_PORT}}/v1`,
+      aime25_pct:
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +9/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/zai-org/glm-5.3.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36459 - [NPU] Fix evalscope accuracy parsing and add glm5_1 aime26 request timeout

- 链接: https://github.com/sgl-project/sglang/pull/36459
- 状态/时间: merged / 2026-08-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py`；关联提交 `63b2adbeac38`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+12/-67，可读 patch 130 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Fix evalscope accuracy parsing and add glm5_1 aime26 request timeout」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py`；技术摘要: 覆盖「[NPU] Fix evalscope accuracy parsing and add glm5_1 aime26 request timeout」；主要实现面是 `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7。
- 代码 diff 细节:
  - `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py` modified +1/-1 (2 lines); hunks: -159,7 +159,7
- 关键代码摘录:

```diff
diff -- test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py
@@ -159,7 +159,7 @@
-    "router_args": ["--policy", "round_robin"],
+    "router_args": ["--policy", "round_robin", "--request-timeout-secs", 7200],
```

- 已读文件:
  - tests: `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py` modified +1/-1
- 验证与风险: diff 自带测试面 `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py`, `test/registered/npu/accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py`, `test/registered/npu/performance/kimi_k2_6/test_npu_kimi_k2_6_w4a8_16p_in64k_out1k_100ms.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37109 - [Docs] Add NVFP4 section to GLM-5.3-Flash cookbook

- 链接: https://github.com/sgl-project/sglang/pull/37109
- 状态/时间: merged / 2026-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `442c7c1e2997`, `60548501bb13`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+324/-20，可读 patch 520 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Add NVFP4 section to GLM-5.3-Flash cookbook」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] Add NVFP4 section to GLM-5.3-Flash cookbook」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +244/-15 (259 lines); hunks: -21,6 +21,19 @@ export const config = {; -123,6 +136,7 @@ export const config = {；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +80/-4 (84 lines); hunks: -22,7 +22,7 @@ export const benchmarks = [; -43,7 +43,7 @@ export const benchmarks = [；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +0/-1 (1 lines); hunks: -184,7 +184,6 @@ sglang serve \。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +244/-15 (259 lines); hunks: -21,6 +21,19 @@ export const config = {; -123,6 +136,7 @@ export const config = {
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +80/-4 (84 lines); hunks: -22,7 +22,7 @@ export const benchmarks = [; -43,7 +43,7 @@ export const benchmarks = [
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +0/-1 (1 lines); hunks: -184,7 +184,6 @@ sglang serve \
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -21,6 +21,19 @@ export const config = {
+    {
+      id: "quant",
+      title: "Quantization",
+      options: [
+        { id: "fp8", label: "FP8" },
+        {
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -22,7 +22,7 @@ export const benchmarks = [
-    match: { hw: "gb300", strategy: "low-latency", kvDsaPair: "fp8-trtllm" },
+    match: { hw: "gb300", strategy: "low-latency", kvDsaPair: "fp8-trtllm", quant: "fp8" },
@@ -43,7 +43,7 @@ export const benchmarks = [
-    match: { hw: "gb300", strategy: "low-latency", kvDsaPair: "fp8-trtllm", dcp: "4" },
+    match: { hw: "gb300", strategy: "low-latency", kvDsaPair: "fp8-trtllm", dcp: "4", quant: "fp8" },
@@ -64,7 +64,7 @@ export const benchmarks = [
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -184,7 +184,6 @@ sglang serve \
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +244/-15; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +80/-4; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +0/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #37380 - Revert "[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)"

- 链接: https://github.com/sgl-project/sglang/pull/37380
- 状态/时间: merged / 2026-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `6c72b49a5796`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+14/-122，可读 patch 263 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)"」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「Revert "[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)"」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +8/-99 (107 lines); hunks: -1,23 +1,14; -30,16 +21,14 @@ export const config = {；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +0/-15 (15 lines); hunks: -310,19 +310,4 @@ export const benchmarks = [；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-8 (14 lines); hunks: -1,6 +1,6; -10,7 +10,7 @@ tag: NEW。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +8/-99 (107 lines); hunks: -1,23 +1,14; -30,16 +21,14 @@ export const config = {
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +0/-15 (15 lines); hunks: -310,19 +310,4 @@ export const benchmarks = [
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-8 (14 lines); hunks: -1,6 +1,6; -10,7 +10,7 @@ tag: NEW
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -1,23 +1,14 @@
-  supportedHardware: [
-    "gb300", "h100", "h200", "b200", "b300", "gb200",
-    "mi300x", "mi325x", "mi355x",
-  ],
+  supportedHardware: ["gb300", "h100", "h200", "b200", "b300", "gb200"],
-        {
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -310,19 +310,4 @@ export const benchmarks = [
-  {
-    match: { hw: "mi300x", strategy: "high-throughput" },
-    sglang_version: "9e692c9216",
-    accuracy: { gsm8k_pct: 97.35 },
-    notes:
-      "Accuracy-only validation on 8x MI300X (gfx942, TP8) with zai-org/GLM-5.3-Flash revision 3f1971b7b5f7a528c9c4ef6212c8785298a8c24a, SGLang PR #36607 head 9e692c9216c3b5e5c443
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -1,6 +1,6 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +8/-99; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +0/-15; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-8
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #37392 - [Cookbook] Add the DFlash2 speculative option to GLM-5.3

- 链接: https://github.com/sgl-project/sglang/pull/37392
- 状态/时间: merged / 2026-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`；关联提交 `dc1ae02684d4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+22/-1，可读 patch 44 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Cookbook] Add the DFlash2 speculative option to GLM-5.3」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`；技术摘要: 覆盖「[Cookbook] Add the DFlash2 speculative option to GLM-5.3」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +21/-1 (22 lines); hunks: -169,7 +169,8 @@ sgl-eval run aime25 \\; -184,6 +185,25 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +1/-0 (1 lines); hunks: -103,6 +103,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +21/-1 (22 lines); hunks: -169,7 +169,8 @@ sgl-eval run aime25 \\; -184,6 +185,25 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +1/-0 (1 lines); hunks: -103,6 +103,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3.jsx
@@ -169,7 +169,8 @@ sgl-eval run aime25 \\
-    // DSA indexer topk across draft steps (topk==1 only).
+    // DSA indexer topk across draft steps (topk==1 only). DFlash2 is the one
+    // algorithm no Deploy cell ships: its draft is a separate checkpoint.
@@ -184,6 +185,25 @@ sgl-eval run aime25 \\
+        { id: "dflash", label: "DFlash2 (block diffusion)",
+          // Block-wise draft from a separate checkpoint, not the in-checkpoint
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3.mdx
@@ -103,6 +103,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
+- **DFlash2 (block-diffusion draft).** The **Speculative** card in the [Playground above](#playground) also offers **DFlash2**, which replaces the in-checkpoint MTP layer with the
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +21/-1; `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +1/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #37412 - [Docs] GLM-5.3-Flash cookbook: add NVFP4 FP8+TRT-LLM benchmark rows (follow-up to #37109)

- 链接: https://github.com/sgl-project/sglang/pull/37412
- 状态/时间: merged / 2026-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `442c7c1e2997`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+95/-11，可读 patch 176 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.3-Flash cookbook: add NVFP4 FP8+TRT-LLM benchmark rows (follow-up to #37109)」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；技术摘要: 覆盖「[Docs] GLM-5.3-Flash cookbook: add NVFP4 FP8+TRT-LLM benchmark rows (follow-up to #37109)」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +91/-3 (94 lines); hunks: -181,6 +181,18 @@ export const benchmarks = [; -196,7 +208,7 @@ export const benchmarks = [；`docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +4/-8 (12 lines); hunks: -451,8 +451,10 @@ sgl-eval run gsm8k \\; -462,7 +464,6 @@ sgl-eval run gsm8k \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +91/-3 (94 lines); hunks: -181,6 +181,18 @@ export const benchmarks = [; -196,7 +208,7 @@ export const benchmarks = [
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +4/-8 (12 lines); hunks: -451,8 +451,10 @@ sgl-eval run gsm8k \\; -462,7 +464,6 @@ sgl-eval run gsm8k \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -181,6 +181,18 @@ export const benchmarks = [
+      {
+        workload: {
+          dataset: "random",
+          isl: 1024,
+          osl: 256,
+          max_concurrency: 1,
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -451,8 +451,10 @@ sgl-eval run gsm8k \\
-    // cell's parallelism (gb200 TP4/EP4, b200/b300 TP8/EP8). Not measured on
-    // this hardware, so every cell here reports unverified.
+    // cell's TP size (gb200 TP4, b200/b300 TP8). Not measured on this
+    // hardware, so every cell here reports unverified. All NVFP4 cells are
+    // TP-only: --ep-size crashes for this checkpoint on the stock image (the
+    // shared-expert NVFP4 weight arrives 1-D under EP).
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +91/-3; `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +4/-8
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #35368 - Update GLM-5.2 NVFP4 B200/B300 for AgentX HiCache

- 链接: https://github.com/sgl-project/sglang/pull/35368
- 状态/时间: merged / 2026-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；关联提交 `9c70d22721d3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+30/-0，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update GLM-5.2 NVFP4 B200/B300 for AgentX HiCache」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「Update GLM-5.2 NVFP4 B200/B300 for AgentX HiCache」；主要实现面是 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +30/-0 (30 lines); hunks: -269,3 +269,33 @@ When deploying with PD Disaggregation, the prefill node can...。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +30/-0 (30 lines); hunks: -269,3 +269,33 @@ When deploying with PD Disaggregation, the prefill node can...
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -269,3 +269,33 @@ When deploying with PD Disaggregation, the prefill node can choose to enable [La
+### 3.6 Agentic Long-Context with HiCache DRAM Offload (NVFP4, MTP)
+**B300 (TP8):**
+'''bash Command
+python3 -m sglang.launch_server \
+  --model-path nvidia/GLM-5.2-NVFP4 \
+  --trust-remote-code \
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +30/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #37576 - [Docs] GLM-5.3-Flash cookbook: drop stale EP caveat, add B300/H100/B200 FP8 speed data

- 链接: https://github.com/sgl-project/sglang/pull/37576
- 状态/时间: merged / 2026-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `3421d4375b31`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+154/-53，可读 patch 397 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.3-Flash cookbook: drop stale EP caveat, add B300/H100/B200 FP8 speed data」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；技术摘要: 覆盖「[Docs] GLM-5.3-Flash cookbook: drop stale EP caveat, add B300/H100/B200 FP8 speed data」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +151/-46 (197 lines); hunks: -4,6 +4,18 @@ export const benchmarks = [; -19,13 +31,25 @@ export const benchmarks = [；`docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +3/-7 (10 lines); hunks: -386,10 +386,8 @@ sgl-eval run gsm8k \\; -452,9 +450,7 @@ sgl-eval run gsm8k \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +151/-46 (197 lines); hunks: -4,6 +4,18 @@ export const benchmarks = [; -19,13 +31,25 @@ export const benchmarks = [
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +3/-7 (10 lines); hunks: -386,10 +386,8 @@ sgl-eval run gsm8k \\; -452,9 +450,7 @@ sgl-eval run gsm8k \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -4,6 +4,18 @@ export const benchmarks = [
+      {
+        workload: {
+          dataset: "random",
+          isl: 1024,
+          osl: 256,
+          max_concurrency: 1,
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -386,10 +386,8 @@ sgl-eval run gsm8k \\
-    // 4x GB300 on the stock image with both KV/DSA pairings: the speed rows
-    // were measured with BF16 KV + TileLang DSA, while FP8 KV + TRT-LLM DSA
-    // passed smoke, a 200-example GSM8K check, a 600-request soak, and the
-    // TB2.1 run without separate speed measurements.
+    // 4x GB300 and 4x B300 with both KV/DSA pairings; the benchmark rows
+    // carry measured speed for both pairings on the current release image.
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +151/-46; `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +3/-7
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #36507 - GLM-5.3-Flash support

- 链接: https://github.com/sgl-project/sglang/pull/36507
- 状态/时间: merged / 2026-09-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py`；关联提交 `97c6978369ac`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 103 个文件，+7740/-558，可读 patch 10897 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「GLM-5.3-Flash support」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py`；技术摘要: 覆盖「GLM-5.3-Flash support」；主要实现面是 `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` added +1630/-0 (1630 lines); hunks: -0,0 +1,1630; symbols: swiglu_clamped, Glm5NextVisionMLP, __init__, forward，涉及 `swiglu_clamped, Glm5NextVisionMLP, __init__`；`python/sglang/srt/configs/glm5_next.py` added +341/-0 (341 lines); hunks: -0,0 +1,341; symbols: Glm5NextTextConfig, __init__, is_kda_layer, linear_layer_ids，涉及 `Glm5NextTextConfig, __init__, is_kda_layer`；`python/sglang/srt/models/glm5_next_nextn.py` added +80/-0 (80 lines); hunks: -0,0 +1,80; symbols: Glm5NextForConditionalGenerationNextN, get_hf_to_sglang_mapper, _resolve_nextn_quant_config, __init__，涉及 `Glm5NextForConditionalGenerationNextN, get_hf_to_sglang_mapper, _resolve_nextn_quant_config`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` added +1630/-0 (1630 lines); hunks: -0,0 +1,1630; symbols: swiglu_clamped, Glm5NextVisionMLP, __init__, forward
  - `python/sglang/srt/configs/glm5_next.py` added +341/-0 (341 lines); hunks: -0,0 +1,341; symbols: Glm5NextTextConfig, __init__, is_kda_layer, linear_layer_ids
  - `python/sglang/srt/models/glm5_next_nextn.py` added +80/-0 (80 lines); hunks: -0,0 +1,80; symbols: Glm5NextForConditionalGenerationNextN, get_hf_to_sglang_mapper, _resolve_nextn_quant_config, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -0,0 +1,1630 @@
+import logging
+from contextlib import nullcontext
+from functools import partial
+from typing import Any, Dict, Iterable, List, Optional, Tuple, Union
+import torch
+from torch import nn
diff -- python/sglang/srt/configs/glm5_next.py
@@ -0,0 +1,341 @@
+from typing import List, Optional, Union
+from transformers.configuration_utils import PretrainedConfig
+from transformers.models.glm_ocr.configuration_glm_ocr import GlmOcrVisionConfig
+from sglang.srt.configs.mamba_utils import KimiLinearCacheParams, KimiLinearStateShape
+from sglang.srt.runtime_context import get_parallel
+_GLM5_NEXT_TOP_LEVEL_CONFIG_KEYS = (
diff -- python/sglang/srt/models/glm5_next_nextn.py
@@ -0,0 +1,80 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` added +1630/-0; `python/sglang/srt/configs/glm5_next.py` added +341/-0; `python/sglang/srt/models/glm5_next_nextn.py` added +80/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_dsa_indexer.py`, `test/registered/kernels/ops/attention/test_fused_verify_triton_gdn.py`, `test/registered/kernels/test_lean_attention.py`, `test/registered/models_e2e/test_glm53_flash_b200.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38725 - Relax GSM8K thresholds for the GLM-5.2 DSA-MTP variants

- 链接: https://github.com/sgl-project/sglang/pull/38725
- 状态/时间: merged / 2026-09-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`；关联提交 `95a88bfd69d3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+5/-2，可读 patch 28 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Relax GSM8K thresholds for the GLM-5.2 DSA-MTP variants」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`；技术摘要: 覆盖「Relax GSM8K thresholds for the GLM-5.2 DSA-MTP variants」；主要实现面是 `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py` modified +1/-0 (1 lines); hunks: -24,6 +24,7 @@ class TestGLM52NVFP4DPMTP(; symbols: TestGLM52NVFP4DPMTP，涉及 `TestGLM52NVFP4DPMTP`；`test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` modified +1/-0 (1 lines); hunks: -22,6 +22,7 @@ class TestGLM52NVFP4TPMTP(; symbols: TestGLM52NVFP4TPMTP，涉及 `TestGLM52NVFP4TPMTP`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py` modified +1/-0 (1 lines); hunks: -24,6 +24,7 @@ class TestGLM52NVFP4DPMTP(; symbols: TestGLM52NVFP4DPMTP
  - `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` modified +1/-0 (1 lines); hunks: -22,6 +22,7 @@ class TestGLM52NVFP4TPMTP(; symbols: TestGLM52NVFP4TPMTP
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py
@@ -24,6 +24,7 @@ class TestGLM52NVFP4DPMTP(
+    gsm8k_accuracy_thres = 0.92
diff -- test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py
@@ -22,6 +22,7 @@ class TestGLM52NVFP4TPMTP(
+    gsm8k_accuracy_thres = 0.92
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py` modified +1/-0; `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` modified +1/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/server_fixtures/dsa_mtp_fixture.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38621 - [Model] Support GLM-5.3 Flash NVFP4 loading

- 链接: https://github.com/sgl-project/sglang/pull/38621
- 状态/时间: merged / 2026-09-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_modelopt.py`；关联提交 `96d91ef9266d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+123/-0，可读 patch 145 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Support GLM-5.3 Flash NVFP4 loading」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[Model] Support GLM-5.3 Flash NVFP4 loading」；主要实现面是 `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_glm5_next_modelopt.py` added +104/-0 (104 lines); hunks: -0,0 +1,104; symbols: TestGlm5NextModelOpt, _config, _hf_config, test_checkpoint_exclusions_match_sglang_module_names，涉及 `TestGlm5NextModelOpt, _config, _hf_config`；`python/sglang/srt/models/glm5_next.py` modified +19/-0 (19 lines); hunks: -94,6 +94,7; -1077,6 +1078,13 @@ def forward(; symbols: forward, Glm5NextForConditionalGeneration, shared_experts_fusion_disable_reason，涉及 `forward, Glm5NextForConditionalGeneration, shared_experts_fusion_disable_reason`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_glm5_next_modelopt.py` added +104/-0 (104 lines); hunks: -0,0 +1,104; symbols: TestGlm5NextModelOpt, _config, _hf_config, test_checkpoint_exclusions_match_sglang_module_names
  - `python/sglang/srt/models/glm5_next.py` modified +19/-0 (19 lines); hunks: -94,6 +94,7; -1077,6 +1078,13 @@ def forward(; symbols: forward, Glm5NextForConditionalGeneration, shared_experts_fusion_disable_reason
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_glm5_next_modelopt.py
@@ -0,0 +1,104 @@
+import unittest
+from types import SimpleNamespace
+from unittest.mock import patch
+from sglang.srt.layers.quantization.modelopt_quant import ModelOptFp4Config
+from sglang.srt.models import glm5_next
+from sglang.srt.models.glm5_next import Glm5NextForConditionalGeneration
diff -- python/sglang/srt/models/glm5_next.py
@@ -94,6 +94,7 @@
+from sglang.srt.models.utils import WeightsMapper
@@ -1077,6 +1078,13 @@ def forward(
+    hf_to_sglang_mapper = WeightsMapper(
+        orig_to_new_substr={
+            "model.language_model.": "model.",
+            "model.visual": "visual",
```

- 已读文件:
  - tests: `test/registered/unit/models/test_glm5_next_modelopt.py` added +104/-0
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +19/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_glm5_next_modelopt.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38522 - Add Opt-In for GLM-5.3 Flash breakable prefill CUDA graphs

- 链接: https://github.com/sgl-project/sglang/pull/38522
- 状态/时间: merged / 2026-09-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `0084030179bf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+219/-10，可读 patch 429 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add Opt-In for GLM-5.3 Flash breakable prefill CUDA graphs」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「Add Opt-In for GLM-5.3 Flash breakable prefill CUDA graphs」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +29/-2 (31 lines); hunks: -33,6 +33,7 @@ export const config = {; -68,6 +69,20 @@ export const config = {；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-1 (4 lines); hunks: -27,7 +27,9 @@ Choose your hardware, then choose the operating point that mat...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +29/-2 (31 lines); hunks: -33,6 +33,7 @@ export const config = {; -68,6 +69,20 @@ export const config = {
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-1 (4 lines); hunks: -27,7 +27,9 @@ Choose your hardware, then choose the operating point that mat...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -33,6 +33,7 @@ export const config = {
+      s.bcg === "off" &&
@@ -68,6 +69,20 @@ export const config = {
+    {
+      id: "bcg",
+      title: "Breakable Cuda Graph",
+      default: "off",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -27,7 +27,9 @@ Choose your hardware, then choose the operating point that matches your workload
-The recommended selection is only a starting point. The same panel also lets you override the KV/DSA pairing, multimodal feature transport, and HiCache tiers. Changing an option t
+The recommended selection is only a starting point. The same panel also lets you override the KV/DSA pairing, multimodal feature transport, Breakable Cuda Graph, and HiCache tiers
+**Breakable Cuda Graph** defaults to **Off**. Select **On** to add `--cuda-graph-backend-prefill breakable` to the generated command. This requires a build that includes [PR #3852
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +29/-2; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/configs/model_config.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #38775 - [NPU] Set DEEPEP_HYBRID_DEPLOYMENT for new DeepEP tests; switch glm5_2 to w8a8; tune nightly timeouts

- 链接: https://github.com/sgl-project/sglang/pull/38775
- 状态/时间: merged / 2026-09-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py`；关联提交 `92dffebe16f5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+37/-31，可读 patch 179 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] Set DEEPEP_HYBRID_DEPLOYMENT for new DeepEP tests; switch glm5_2 to w8a8; tune nightly timeouts」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py`；技术摘要: 覆盖「[NPU] Set DEEPEP_HYBRID_DEPLOYMENT for new DeepEP tests; switch glm5_2 to w8a8; tune nightly timeouts」；主要实现面是 `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py` renamed +13/-13 (26 lines); hunks: -6,7 +6,7; -17,7 +17,7; symbols: TestNPUGLM_5_2_W4A8_16P_GPQA, TestNPUGLM_5_2_W8A8_16P_GPQA, test_npu_glm_5_2_w4a8_16p_gpqa, test_npu_glm_5_2_w8a8_16p_gpqa，涉及 `TestNPUGLM_5_2_W4A8_16P_GPQA, TestNPUGLM_5_2_W8A8_16P_GPQA, test_npu_glm_5_2_w4a8_16p_gpqa`；`test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py` modified +1/-0 (1 lines); hunks: -19,6 +19,7。
- 代码 diff 细节:
  - `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py` renamed +13/-13 (26 lines); hunks: -6,7 +6,7; -17,7 +17,7; symbols: TestNPUGLM_5_2_W4A8_16P_GPQA, TestNPUGLM_5_2_W8A8_16P_GPQA, test_npu_glm_5_2_w4a8_16p_gpqa, test_npu_glm_5_2_w8a8_16p_gpqa
  - `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py` modified +1/-0 (1 lines); hunks: -19,6 +19,7
- 关键代码摘录:

```diff
diff -- test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py
@@ -6,7 +6,7 @@
-    GLM_5_2_W4A8_MODEL_PATH,
+    GLM_5_2_W8A8_MODEL_PATH,
@@ -17,7 +17,7 @@
-GLM_5_2_W4A8_16P_TWO_NODE_ENVS = {
+GLM_5_2_W8A8_16P_TWO_NODE_ENVS = {
@@ -34,7 +34,7 @@
diff -- test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py
@@ -19,6 +19,7 @@
+    "DEEPEP_HYBRID_DEPLOYMENT": "1",
```

- 已读文件:
  - tests: `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py` renamed +13/-13; `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py` modified +1/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py`, `test/registered/npu/accuracy/kimi_k2_6/test_npu_kimi_k2_6_w4a8_16p_in64k_out1k_100ms_aime25.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39106 - [AMD] Use the triton DSA backend for GLM-5.2 MXFP4 on MI355X

- 链接: https://github.com/sgl-project/sglang/pull/39106
- 状态/时间: merged / 2026-09-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `d7c284b894e9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+12/-9，可读 patch 63 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Use the triton DSA backend for GLM-5.2 MXFP4 on MI355X」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[AMD] Use the triton DSA backend for GLM-5.2 MXFP4 on MI355X」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +11/-8 (19 lines); hunks: -1011,6 +1011,9 @@ sgl-eval run aime25 \\; -1021,8 +1024,8 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -118,7 +118,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +11/-8 (19 lines); hunks: -1011,6 +1011,9 @@ sgl-eval run aime25 \\; -1021,8 +1024,8 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -118,7 +118,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -1011,6 +1011,9 @@ sgl-eval run aime25 \\
+    // DSA backend: triton (SGLang's ROCm default). At TP4 this shape hits the
+    // gfx950 FP8 sparse-MLA tuning; the TP8 FP8/BF16 cells above stay on
+    // tilelang, where their published numbers were measured.
@@ -1021,8 +1024,8 @@ sgl-eval run aime25 \\
-        "--dsa-prefill-backend tilelang",
-        "--dsa-decode-backend tilelang",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -118,7 +118,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-- **MI355X MXFP4 (gfx950-only).** AMD publishes a Quark-quantized **`amd/GLM-5.2-MXFP4`** build for MI355X. It needs `--trust-remote-code` (Quark's custom quant config) and runs a
+- **MI355X MXFP4 (gfx950-only).** AMD publishes a Quark-quantized **`amd/GLM-5.2-MXFP4`** build for MI355X. It needs `--trust-remote-code` (Quark's custom quant config) and runs a
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +11/-8; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39213 - [Docs] GLM-5.3-Flash cookbook: fixed MTP 5/1/6, EP1 + flashinfer_trtllm on Blackwell

- 链接: https://github.com/sgl-project/sglang/pull/39213
- 状态/时间: merged / 2026-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `b5a2aebc7ecc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+111/-73，可读 patch 584 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.3-Flash cookbook: fixed MTP 5/1/6, EP1 + flashinfer_trtllm on Blackwell」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] GLM-5.3-Flash cookbook: fixed MTP 5/1/6, EP1 + flashinfer_trtllm on Blackwell」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +71/-13 (84 lines); hunks: -1,4 +1,5; -35,37 +36,86 @@ export const benchmarks = [；`docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +32/-51 (83 lines); hunks: -8,7 +8,7 @@ export const config = {; -130,9 +130,9 @@ export const config = {；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +8/-9 (17 lines); hunks: -22,7 +22,7 @@ The deployment panel can render a complete `docker run` comman...; -94,15 +94,15 @@ The deployment recipes use the checkpoint's generation confi...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +71/-13 (84 lines); hunks: -1,4 +1,5; -35,37 +36,86 @@ export const benchmarks = [
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +32/-51 (83 lines); hunks: -8,7 +8,7 @@ export const config = {; -130,9 +130,9 @@ export const config = {
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +8/-9 (17 lines); hunks: -22,7 +22,7 @@ The deployment panel can render a complete `docker run` comman...; -94,15 +94,15 @@ The deployment recipes use the checkpoint's generation confi...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -1,4 +1,5 @@
+  // TODO: speed measured on the earlier TP4/EP4 deep_gemm command with adaptive MTP; re-measure on the current recipe.
@@ -35,37 +36,86 @@ export const benchmarks = [
-    sglang_version: "d6ab04bdf1",
+    sglang_version: "b3dc0388ed",
-          isl: 1024,
-          osl: 256,
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -8,7 +8,7 @@ export const config = {
-        { id: "low-latency", label: "Low Latency", subtitle: "Adaptive MTP 5/1/6" },
+        { id: "low-latency", label: "Low Latency", subtitle: "MTP 5/1/6" },
@@ -130,9 +130,9 @@ export const config = {
-          disableReason: "DCP is validated only on 4x GB300 TP4/EP4 for now.",
+          disableReason: "DCP is validated only on 4x GB300 for now.",
-          hints: ["Measured on 4x GB300 with both KV/DSA pairings, adaptive MTP 5/1/6, full decode graph."],
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -22,7 +22,7 @@ The deployment panel can render a complete `docker run` command for the selected
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +71/-13; `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +32/-51; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +8/-9
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39230 - [AMD] Document GLM-5.2 MXFP4 recipe update on MI355X

- 链接: https://github.com/sgl-project/sglang/pull/39230
- 状态/时间: merged / 2026-09-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `288627e4006a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+23/-12，可读 patch 83 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Document GLM-5.2 MXFP4 recipe update on MI355X」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[AMD] Document GLM-5.2 MXFP4 recipe update on MI355X」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +22/-11 (33 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -178,8 +178,12 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +22/-11 (33 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -178,8 +178,12 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -97,7 +97,7 @@ sgl-eval run aime25 \\
-    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.16-rocm720-mi35x-20260728",
+    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260910",
@@ -178,8 +178,12 @@ sgl-eval run aime25 \\
-          disable: { hw: ["mi355x", "mi325x", "mi300x"] },
-          disableReason: "MTP/EAGLE speculative decoding is not yet validated on AMD ROCm (MI300X/MI325X/MI355X): the gfx950 spec-decode draft kernel is not yet validated and at -
+          disable: [
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-- **MTP / EAGLE speculative decoding** is disabled for AMD in the Deploy panel. The block-FP8 accuracy bug that previously degraded it is now fixed (see note above), but MTP on gf
+- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260910`. Choose **Lo
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +22/-11; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39406 - [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916

- 链接: https://github.com/sgl-project/sglang/pull/39406
- 状态/时间: merged / 2026-09-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `242d8a70c05b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+7/-7，可读 patch 60 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +6/-6 (12 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -1019,7 +1019,7 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +6/-6 (12 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -1019,7 +1019,7 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -97,7 +97,7 @@ sgl-eval run aime25 \\
-    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260910",
+    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260913",
@@ -1019,7 +1019,7 @@ sgl-eval run aime25 \\
-      env: [],
+      env: ["SGLANG_OPT_USE_TOPK_V2=true"],
@@ -1042,7 +1042,7 @@ sgl-eval run aime25 \\
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260910`. Choose **Lo
+- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260913`. Choose **Lo
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +6/-6; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39720 - [Fix] Fix GLM5 mHC PP forward

- 链接: https://github.com/sgl-project/sglang/pull/39720
- 状态/时间: merged / 2026-09-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`；关联提交 `9c8d4641ff64`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-1，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] Fix GLM5 mHC PP forward」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[Fix] Fix GLM5 mHC PP forward」；主要实现面是 `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +4/-1 (5 lines); hunks: -981,7 +981,8 @@ def forward(; -1059,6 +1060,8 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +4/-1 (5 lines); hunks: -981,7 +981,8 @@ def forward(; -1059,6 +1060,8 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -981,7 +981,8 @@ def forward(
-            residual = pp_proxy_tensors["residual"]
+            # mHC carries its residual streams in hidden_states across PP stages.
+            residual = None if self.config.mhc else pp_proxy_tensors["residual"]
@@ -1059,6 +1060,8 @@ def forward(
+            if self.config.mhc:
+                return PPProxyTensors({"hidden_states": hidden_states})
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm5_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #40036 - [Docs] GLM-5.3-Flash cookbook: temporarily remove the DCP option

- 链接: https://github.com/sgl-project/sglang/pull/40036
- 状态/时间: merged / 2026-09-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `b98a2d1096f6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+6/-74，可读 patch 136 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.3-Flash cookbook: temporarily remove the DCP option」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] GLM-5.3-Flash cookbook: temporarily remove the DCP option」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +0/-44 (44 lines); hunks: -115,50 +115,6 @@ export const benchmarks = [；`docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +6/-26 (32 lines); hunks: -33,8 +33,7 @@ export const config = {; -120,22 +119,6 @@ export const config = {；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +0/-4 (4 lines); hunks: -120,10 +120,6 @@ Keep the checkpoint's KDA lower-bound setting unchanged. In...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +0/-44 (44 lines); hunks: -115,50 +115,6 @@ export const benchmarks = [
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +6/-26 (32 lines); hunks: -33,8 +33,7 @@ export const config = {; -120,22 +119,6 @@ export const config = {
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +0/-4 (4 lines); hunks: -120,10 +120,6 @@ Keep the checkpoint's KDA lower-bound setting unchanged. In...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -115,50 +115,6 @@ export const benchmarks = [
-  // TODO: speed measured on the earlier TP4/EP4 deep_gemm command with adaptive MTP; re-measure on the current recipe.
-  {
-    match: { hw: "gb300", strategy: "low-latency", kvDsaPair: "fp8-trtllm", dcp: "4", quant: "fp8" },
-    sglang_version: "d6ab04bdf1",
-    latencyPercentile: "Mean",
-    speed: [
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -33,8 +33,7 @@ export const config = {
-      s.bcg === "off" &&
-      s.dcp === "off"
+      s.bcg === "off"
@@ -120,22 +119,6 @@ export const config = {
-    {
-      id: "dcp",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -120,10 +120,6 @@ Keep the checkpoint's KDA lower-bound setting unchanged. In particular, do not o
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +0/-44; `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +6/-26; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +0/-4
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #40148 - [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916, use HIP Top-K

- 链接: https://github.com/sgl-project/sglang/pull/40148
- 状态/时间: merged / 2026-09-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `45938a24ae41`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+6/-6，可读 patch 54 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916, use HIP Top-K」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916, use HIP Top-K」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +5/-5 (10 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -1019,7 +1019,7 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +5/-5 (10 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -1019,7 +1019,7 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -97,7 +97,7 @@ sgl-eval run aime25 \\
-    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260913",
+    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260916",
@@ -1019,7 +1019,7 @@ sgl-eval run aime25 \\
-      env: ["SGLANG_OPT_USE_TOPK_V2=true"],
+      env: [],
@@ -1042,7 +1042,7 @@ sgl-eval run aime25 \\
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260913`. Choose **Lo
+- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260916`. Choose **Lo
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +5/-5; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39688 - Fuse GLM-5.3-Flash KDA projections and prefill metadata

- 链接: https://github.com/sgl-project/sglang/pull/39688
- 状态/时间: merged / 2026-09-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_bfg_fusion.py`；关联提交 `c8eb54c41da1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+1027/-87，可读 patch 1507 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fuse GLM-5.3-Flash KDA projections and prefill metadata」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_bfg_fusion.py`；技术摘要: 覆盖「Fuse GLM-5.3-Flash KDA projections and prefill metadata」；主要实现面是 `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_bfg_fusion.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +149/-62 (211 lines); hunks: -36,6 +36,7; -49,6 +50,7; symbols: __init__, Glm5NextLinearAttention, _can_fuse_proj，涉及 `__init__, Glm5NextLinearAttention, _can_fuse_proj`；`test/registered/unit/models/test_glm5_next_bfg_fusion.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: MockQuantizedLinearMethod, apply, MockFp8Config, __init__，涉及 `MockQuantizedLinearMethod, apply, MockFp8Config`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +149/-62 (211 lines); hunks: -36,6 +36,7; -49,6 +50,7; symbols: __init__, Glm5NextLinearAttention, _can_fuse_proj
  - `test/registered/unit/models/test_glm5_next_bfg_fusion.py` added +182/-0 (182 lines); hunks: -0,0 +1,182; symbols: MockQuantizedLinearMethod, apply, MockFp8Config, __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -36,6 +36,7 @@
+    LinearBase,
@@ -49,6 +50,7 @@
+from sglang.srt.layers.quantization.unquant import UnquantizedLinearMethod
@@ -99,7 +101,13 @@
-from sglang.srt.runtime_context import get_forward, get_mm, get_parallel, get_spec
+from sglang.srt.runtime_context import (
diff -- test/registered/unit/models/test_glm5_next_bfg_fusion.py
@@ -0,0 +1,182 @@
+import unittest
+from types import SimpleNamespace
+from unittest.mock import patch
+import torch
+import torch.nn.functional as F
+from sglang.srt.layers.quantization.unquant import UnquantizedLinearMethod
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +149/-62
  - tests: `test/registered/unit/models/test_glm5_next_bfg_fusion.py` added +182/-0
- 验证与风险: diff 自带测试面 `test/registered/kernel/attention/test_kda_gate_beta_cumsum.py`, `test/registered/unit/layers/test_mamba2_track_ssm_indices.py`, `test/registered/unit/layers/test_mamba_prefill_track_metadata.py`, `test/registered/unit/models/test_glm5_next_bfg_fusion.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39200 - [Perf] Fuse the glm5_next mHC attn->MLP boundary

- 链接: https://github.com/sgl-project/sglang/pull/39200
- 状态/时间: merged / 2026-09-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`；关联提交 `2fa6b94e3440`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+162/-3，可读 patch 256 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] Fuse the glm5_next mHC attn->MLP boundary」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[Perf] Fuse the glm5_next mHC attn->MLP boundary」；主要实现面是 `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +61/-1 (62 lines); hunks: -75,6 +75,10; -117,6 +121,15; symbols: swiglu_clamped, __init__, _hc_pre, hc_ffn_pre，涉及 `swiglu_clamped, __init__, _hc_pre`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +61/-1 (62 lines); hunks: -75,6 +75,10; -117,6 +121,15; symbols: swiglu_clamped, __init__, _hc_pre, hc_ffn_pre
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -75,6 +75,10 @@
+from sglang.srt.models.deepseek_common.amd.deepseek_v4_fused_mhc import (
+    apply_mhc_post_pre_boundary,
+    is_cross_layer_mhc_fusion_enabled,
+)
@@ -117,6 +121,15 @@
+# Matches DeepSeek-V4's _MHC_POST_MULT_VALUE; the fused and unfused boundaries
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +61/-1
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/layernorm/test_mhc_kernels.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40570 - [AMD] Enable HiCache for GLM-5.2 MI355X throughput recipe

- 链接: https://github.com/sgl-project/sglang/pull/40570
- 状态/时间: merged / 2026-09-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `66f19f5c468f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+5/-3，可读 patch 36 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Enable HiCache for GLM-5.2 MI355X throughput recipe」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[AMD] Enable HiCache for GLM-5.2 MI355X throughput recipe」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +4/-2 (6 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -1011,7 +1011,7 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +4/-2 (6 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\; -1011,7 +1011,7 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -97,7 +97,7 @@ sgl-eval run aime25 \\
-    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260916",
+    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260920",
@@ -1011,7 +1011,7 @@ sgl-eval run aime25 \\
-    // newer image (v0.5.19, see dockerImages["mi355x|mxfp4"]) than the FP8/BF16
+    // newer image (v0.5.20, see dockerImages["mi355x|mxfp4"]) than the FP8/BF16
@@ -1075,6 +1075,8 @@ sgl-eval run aime25 \\
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.19-rocm720-mi35x-20260916`. Choose **Lo
+- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260920`. Choose **Lo
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +4/-2; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #38546 - [AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/38546
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`, `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`；关联提交 `b44e2486824e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+756/-15，可读 patch 994 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`, `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`；技术摘要: 覆盖「[AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950」；主要实现面是 `python/sglang/srt/models/glm5_next.py`, `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +17/-3 (20 lines); hunks: -1233,11 +1233,13 @@ def forward(; -1570,6 +1572,14 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: forward, Glm5NextForConditionalGeneration, load_weights, maybe_map_fp8_block_scale_name，涉及 `forward, Glm5NextForConditionalGeneration, load_weights`；`test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` added +397/-0 (397 lines); hunks: -0,0 +1,397; symbols: TestGLM53FlashQuarkMoE, setUpClass, _make_mxfp4_bank, _quantize_fp8_weight，涉及 `TestGLM53FlashQuarkMoE, setUpClass, _make_mxfp4_bank`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +17/-3 (20 lines); hunks: -1233,11 +1233,13 @@ def forward(; -1570,6 +1572,14 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: forward, Glm5NextForConditionalGeneration, load_weights, maybe_map_fp8_block_scale_name
  - `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` added +397/-0 (397 lines); hunks: -0,0 +1,397; symbols: TestGLM53FlashQuarkMoE, setUpClass, _make_mxfp4_bank, _quantize_fp8_weight
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -1233,11 +1233,13 @@ def forward(
-            "model.language_model.": "model.",
-        }
+        },
+        orig_to_new_prefix={
+            "model.language_model.": "model.",
+        },
diff -- test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py
@@ -0,0 +1,397 @@
+"""Isolated gfx950 numerical tests for GLM-5.3-Flash Quark MoE."""
+import unittest
+from types import SimpleNamespace
+import torch
+import torch.nn.functional as F
+from aiter.ops.flydsl.moe_common import GateMode
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +17/-3
  - tests: `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py` added +397/-0
- 验证与风险: diff 自带测试面 `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`, `test/registered/unit/layers/quantization/test_fp8_moe_runner_ownership.py`, `test/registered/unit/layers/quantization/test_quark_config.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40497 - [Docs] GLM-5.3/5.3-Flash cookbooks: enable reasoning/tool-call parsers by default via auto

- 链接: https://github.com/sgl-project/sglang/pull/40497
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`；关联提交 `a0781f271462`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+83/-74，可读 patch 409 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.3/5.3-Flash cookbooks: enable reasoning/tool-call parsers by default via auto」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] GLM-5.3/5.3-Flash cookbooks: enable reasoning/tool-call parsers by default via auto」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +38/-56 (94 lines); hunks: -119,6 +119,32 @@ export const config = {; -174,15 +200,16 @@ sgl-eval run gsm8k \\；`docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +36/-9 (45 lines); hunks: -96,15 +96,45 @@ sgl-eval run aime25 \\; -162,8 +192,8 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +5/-5 (10 lines); hunks: -10,10 +10,10 @@ tag: NEW; -104,7 +104,7 @@ The **Speculative** card in the Playground changes the algor...；`docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +4/-4 (8 lines); hunks: -103,7 +103,7 @@ import { Playground } from "/src/snippets/_playground.jsx";; -117,7 +117,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +38/-56 (94 lines); hunks: -119,6 +119,32 @@ export const config = {; -174,15 +200,16 @@ sgl-eval run gsm8k \\
  - `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +36/-9 (45 lines); hunks: -96,15 +96,45 @@ sgl-eval run aime25 \\; -162,8 +192,8 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +5/-5 (10 lines); hunks: -10,10 +10,10 @@ tag: NEW; -104,7 +104,7 @@ The **Speculative** card in the Playground changes the algor...
  - `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +4/-4 (8 lines); hunks: -103,7 +103,7 @@ import { Playground } from "/src/snippets/_playground.jsx";; -117,7 +117,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -119,6 +119,32 @@ export const config = {
+    // Parser flags live in one overlay dim so every generated command gets
+    // them without per-cell duplication; the Parsers card toggles derive
+    // on/off from the composed flags. `auto` needs the GLM-5.3 template
+    // detection (v0.5.20+).
+    {
+      id: "parsers",
diff -- docs/src/snippets/configs/zai-org/glm-5.3.jsx
@@ -96,15 +96,45 @@ sgl-eval run aime25 \\
-    mi355x: "lmsysorg/sglang-rocm:v0.5.13.post1-rocm720-mi35x-20260618",
-    mi325x: "lmsysorg/sglang-rocm:v0.5.13.post1-rocm700-mi30x-20260616",
-    mi300x: "lmsysorg/sglang-rocm:v0.5.13.post1-rocm700-mi30x-20260616",
+    // >= v0.5.20 so `--*-parser auto` detects GLM-5.3 (#38297); the rocm700
+    // line stopped at v0.5.19, so mi30x moves to the rocm720 build.
+    mi355x: "lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260920",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -10,10 +10,10 @@ tag: NEW
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +38/-56; `docs/src/snippets/configs/zai-org/glm-5.3.jsx` modified +36/-9; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +5/-5; `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +4/-4
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39779 - [AMD] [GLM-5.3-Flash Day 0] Load the MXFP4 MTP draft layer

- 链接: https://github.com/sgl-project/sglang/pull/39779
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next_nextn.py`, `test/registered/unit/models/test_glm5_next_modelopt.py`；关联提交 `c19dc43cc732`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+147/-4，可读 patch 193 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [GLM-5.3-Flash Day 0] Load the MXFP4 MTP draft layer」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next_nextn.py`；技术摘要: 覆盖「[AMD] [GLM-5.3-Flash Day 0] Load the MXFP4 MTP draft layer」；主要实现面是 `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next_nextn.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_glm5_next_modelopt.py` modified +18/-0 (18 lines); hunks: -5,6 +5,7; -99,6 +100,23 @@ def test_radixark_uniform_fp4_shared_experts_keep_fusion(self):; symbols: test_radixark_uniform_fp4_shared_experts_keep_fusion, test_nextn_mapper_routes_checkpoint_names_to_runtime_modules，涉及 `test_radixark_uniform_fp4_shared_experts_keep_fusion, test_nextn_mapper_routes_checkpoint_names_to_runtime_modules`；`python/sglang/srt/models/glm5_next_nextn.py` modified +12/-4 (16 lines); hunks: -25,10 +25,18 @@ class Glm5NextForConditionalGenerationNextN(DeepseekV3ForCau...; symbols: Glm5NextForConditionalGenerationNextN, get_hf_to_sglang_mapper, _resolve_nextn_quant_config，涉及 `Glm5NextForConditionalGenerationNextN, get_hf_to_sglang_mapper, _resolve_nextn_quant_config`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_glm5_next_modelopt.py` modified +18/-0 (18 lines); hunks: -5,6 +5,7; -99,6 +100,23 @@ def test_radixark_uniform_fp4_shared_experts_keep_fusion(self):; symbols: test_radixark_uniform_fp4_shared_experts_keep_fusion, test_nextn_mapper_routes_checkpoint_names_to_runtime_modules
  - `python/sglang/srt/models/glm5_next_nextn.py` modified +12/-4 (16 lines); hunks: -25,10 +25,18 @@ class Glm5NextForConditionalGenerationNextN(DeepseekV3ForCau...; symbols: Glm5NextForConditionalGenerationNextN, get_hf_to_sglang_mapper, _resolve_nextn_quant_config
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_glm5_next_modelopt.py
@@ -5,6 +5,7 @@
+from sglang.srt.models.glm5_next_nextn import Glm5NextForConditionalGenerationNextN
@@ -99,6 +100,23 @@ def test_radixark_uniform_fp4_shared_experts_keep_fusion(self):
+    def test_nextn_mapper_routes_checkpoint_names_to_runtime_modules(self):
+        """Draft quant lookups miss unless checkpoint names reach NextN module paths."""
+        mapper = Glm5NextForConditionalGenerationNextN.get_hf_to_sglang_mapper(
+            self._hf_config()
diff -- python/sglang/srt/models/glm5_next_nextn.py
@@ -25,10 +25,18 @@ class Glm5NextForConditionalGenerationNextN(DeepseekV3ForCausalLMNextN):
-        return WeightsMapper(
-            orig_to_new_substr={
-                f"model.layers.{text_config.num_hidden_layers}": "model.decoder",
-            },
+        n = text_config.num_hidden_layers
+        # lookups arrive as checkpoint and normalized names, so every rule has both forms
```

- 已读文件:
  - tests: `test/registered/unit/models/test_glm5_next_modelopt.py` modified +18/-0
  - runtime: `python/sglang/srt/models/glm5_next_nextn.py` modified +12/-4
- 验证与风险: diff 自带测试面 `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/models/test_glm5_next_modelopt.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #40466 - [deepep_v2] support GLM-5.3-Flash (Glm5NextForConditionalGeneration)

- 链接: https://github.com/sgl-project/sglang/pull/40466
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`；关联提交 `28be39f72e7d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+6/-1，可读 patch 21 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[deepep_v2] support GLM-5.3-Flash (Glm5NextForConditionalGeneration)」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[deepep_v2] support GLM-5.3-Flash (Glm5NextForConditionalGeneration)」；主要实现面是 `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +5/-1 (6 lines); hunks: -1093,7 +1093,11 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +5/-1 (6 lines); hunks: -1093,7 +1093,11 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -1093,7 +1093,11 @@ def __init__(
-        if get_moe_a2a_backend().is_deepep() or get_moe_a2a_backend().is_mooncake():
+        if (
+            get_moe_a2a_backend().is_deepep()
+            or get_moe_a2a_backend().is_mooncake()
+            or get_moe_a2a_backend().is_deepep_v2()
+        ):
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/moe_model_registry.py`, `python/sglang/srt/models/glm5_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #40862 - [CI] Update GLM-5.3-Flash H200/B200 test args

- 链接: https://github.com/sgl-project/sglang/pull/40862
- 状态/时间: merged / 2026-09-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_glm53_flash_b200.py`；关联提交 `86cb4a0f9796`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+8/-18，可读 patch 97 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Update GLM-5.3-Flash H200/B200 test args」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/e2e/models/test_glm53_flash_b200.py`；技术摘要: 覆盖「[CI] Update GLM-5.3-Flash H200/B200 test args」；主要实现面是 `test/registered/e2e/models/test_glm53_flash_b200.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +5/-10 (15 lines); hunks: -1,7 +1,7; -29,20 +29,18; symbols: TestGLM53FlashB200LowLatency, TestGLM53FlashB200HighThroughput，涉及 `TestGLM53FlashB200LowLatency, TestGLM53FlashB200HighThroughput`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_glm53_flash_b200.py` modified +5/-10 (15 lines); hunks: -1,7 +1,7; -29,20 +29,18; symbols: TestGLM53FlashB200LowLatency, TestGLM53FlashB200HighThroughput
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_glm53_flash_b200.py
@@ -1,7 +1,7 @@
-Runs the Low Latency, DFlash2, and High Throughput TP4/EP4 recipes on four
-B200 GPUs. All recipes must retain GSM8K accuracy; the Low Latency recipe also
+Runs the Low Latency, DFlash2, and High Throughput TP4 recipes on four B200
+GPUs. All recipes must retain GSM8K accuracy; the Low Latency recipe also
@@ -29,20 +29,18 @@
-    "--ep-size",
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +5/-10
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_glm53_flash_b200.py`, `test/registered/e2e/models/test_glm53_flash_h200.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #39816 - Refactor the Cute-DSL AR fusion to support DeepseekV2 archs (GLM-5.3, etc.)

- 链接: https://github.com/sgl-project/sglang/pull/39816
- 状态/时间: merged / 2026-09-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`；关联提交 `3177d10ca6f7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 20 个文件，+1327/-855，可读 patch 2658 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Refactor the Cute-DSL AR fusion to support DeepseekV2 archs (GLM-5.3, etc.)」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`；技术摘要: 覆盖「Refactor the Cute-DSL AR fusion to support DeepseekV2 archs (GLM-5.3, etc.)」；主要实现面是 `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` modified +2/-0 (2 lines); hunks: -28,6 +28,8 @@ class TestGLM52NVFP4TPMTP(; symbols: TestGLM52NVFP4TPMTP，涉及 `TestGLM52NVFP4TPMTP`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` modified +2/-0 (2 lines); hunks: -28,6 +28,8 @@ class TestGLM52NVFP4TPMTP(; symbols: TestGLM52NVFP4TPMTP
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py
@@ -28,6 +28,8 @@ class TestGLM52NVFP4TPMTP(
+        "--flashinfer-allreduce-fusion-backend",
+        "cutedsl",
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py` modified +2/-0
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`, `test/registered/unit/layers/moe/test_cutedsl_ar_fusion.py`, `test/registered/unit/layers/moe/test_qwen35_flashinfer_fusion.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41109 - [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260923 daily

- 链接: https://github.com/sgl-project/sglang/pull/41109
- 状态/时间: merged / 2026-09-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `6a14b801417a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] GLM-5.2 MI355X MXFP4: bump image to 20260923 daily」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「[AMD] GLM-5.2 MI355X MXFP4: bump image to 20260923 daily」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +1/-1 (2 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +1/-1 (2 lines); hunks: -97,7 +97,7 @@ sgl-eval run aime25 \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -97,7 +97,7 @@ sgl-eval run aime25 \\
-    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260920",
+    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260923",
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #41207 - [CI] Move GLM-5.2 layer-split test to extra-b-test-8-gpu-b300

- 链接: https://github.com/sgl-project/sglang/pull/41207
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py`；关联提交 `3fc7a669bfe3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Move GLM-5.2 layer-split test to extra-b-test-8-gpu-b300」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py`；技术摘要: 覆盖「[CI] Move GLM-5.2 layer-split test to extra-b-test-8-gpu-b300」；主要实现面是 `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py` modified +1/-1 (2 lines); hunks: -20,7 +20,7。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py` modified +1/-1 (2 lines); hunks: -20,7 +20,7
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py
@@ -20,7 +20,7 @@
-register_cuda_ci(est_time=898, stage="base-c", runner_config="8-gpu-b300")
+register_cuda_ci(est_time=898, stage="extra-b", runner_config="8-gpu-b300")
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41198 - [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit

- 链接: https://github.com/sgl-project/sglang/pull/41198
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`；关联提交 `b7f6d04a9af1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+50/-219，可读 patch 402 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit」；模型线: GLM-5/5.1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit」；主要实现面是 `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +4/-29 (33 lines); hunks: -28,7 +28,6; -109,7 +108,6; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +4/-29 (33 lines); hunks: -28,7 +28,6; -109,7 +108,6; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -28,7 +28,6 @@
-    UnreducedOutput,
@@ -109,7 +108,6 @@
-    get_forward,
@@ -953,16 +951,6 @@ def forward(
-        should_allreduce_fusion = (
-            self.layer_communicator.should_fuse_mlp_allreduce_with_next_layer(
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +4/-29
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36903 - [AMD] Add GLM-5.3-Flash MI35x nightly test

- 链接: https://github.com/sgl-project/sglang/pull/36903
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py`；关联提交 `25de80780a9e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+178/-25，可读 patch 256 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add GLM-5.3-Flash MI35x nightly test」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py`；技术摘要: 覆盖「[AMD] Add GLM-5.3-Flash MI35x nightly test」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: TestGLM53FlashEvalMI35x, test_glm_53_flash，涉及 `TestGLM53FlashEvalMI35x, test_glm_53_flash`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: TestGLM53FlashEvalMI35x, test_glm_53_flash
- 关键代码摘录:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py
@@ -0,0 +1,165 @@
+"""MI35x GLM-5.3-Flash GSM8K Accuracy Evaluation Test (8-GPU)
+Tests zai-org/GLM-5.3-Flash on MI35x (gfx950) with the AMD FP8 recipe from the
+GLM-5.3-Flash cookbook refresh (#36712): TP8 + EP8, BF16 KV cache, TileLang DSA
+prefill+decode, Triton linear attention, AITER MoE runner, SGLANG_USE_AITER=1,
+full decode graphs at batch sizes 1 and 32.
+GLM-5.3-Flash is the first GLM checkpoint whose 45 text layers mix three
```

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py` added +165/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py`, `test/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41161 - [AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/41161
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`, `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py`；关联提交 `fa443412c558`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+556/-14，可读 patch 645 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`, `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py`；技术摘要: 覆盖「[AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950」；主要实现面是 `python/sglang/srt/models/glm5_next.py`, `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +70/-9 (79 lines); hunks: -53,6 +53,7; -1338,6 +1339,8 @@ def shared_experts_fusion_disable_reason(cls, hf_config, q...; symbols: shared_experts_fusion_disable_reason, determine_num_fused_shared_experts，涉及 `shared_experts_fusion_disable_reason, determine_num_fused_shared_experts`；`test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py` added +265/-0 (265 lines); hunks: -0,0 +1,265; symbols: TestGlm53SharedExpertFusion, _quantize_weight, _make_weights, _fmoe，涉及 `TestGlm53SharedExpertFusion, _quantize_weight, _make_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +70/-9 (79 lines); hunks: -53,6 +53,7; -1338,6 +1339,8 @@ def shared_experts_fusion_disable_reason(cls, hf_config, q...; symbols: shared_experts_fusion_disable_reason, determine_num_fused_shared_experts
  - `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py` added +265/-0 (265 lines); hunks: -0,0 +1,265; symbols: TestGlm53SharedExpertFusion, _quantize_weight, _make_weights, _fmoe
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -53,6 +53,7 @@
+from sglang.srt.layers.quantization.utils import is_layer_skipped
@@ -1338,6 +1339,8 @@ def shared_experts_fusion_disable_reason(cls, hf_config, quant_config):
+        if getattr(text_config, "n_shared_experts", None) != 1:
+            return "Shared experts fusion requires exactly one shared expert."
@@ -1349,20 +1352,78 @@ def shared_experts_fusion_disable_reason(cls, hf_config, quant_config):
-        if not _is_cuda:
diff -- test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py
@@ -0,0 +1,265 @@
+"""gfx950 component checks for GLM-5.3 shared-expert AITER fusion."""
+import unittest
+import aiter
+import torch
+import torch.nn.functional as F
+from aiter import dtypes, pertoken_quant
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +70/-9
  - tests: `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py` added +265/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py`, `test/registered/unit/layers/moe/test_fused_shared_expert_scaling.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41597 - [Docs][AMD] Update GLM-5.2 MI355X daily image

- 链接: https://github.com/sgl-project/sglang/pull/41597
- 状态/时间: merged / 2026-09-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；关联提交 `26d7539799ec`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs][AMD] Update GLM-5.2 MI355X daily image」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Docs][AMD] Update GLM-5.2 MI355X daily image」；主要实现面是 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260920`. Choose **Lo
+- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260924`. Choose **Lo
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #41464 - [AMD] Fix GLM-5.3 quark MoE MI35x test runner config

- 链接: https://github.com/sgl-project/sglang/pull/41464
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`；关联提交 `05817a40c98a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-0，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix GLM-5.3 quark MoE MI35x test runner config」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`；技术摘要: 覆盖「[AMD] Fix GLM-5.3 quark MoE MI35x test runner config」；主要实现面是 `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #41602 - [AMD] Add GLM-5.3 MI30x and MI35x nightly accuracy tests

- 链接: https://github.com/sgl-project/sglang/pull/41602
- 状态/时间: merged / 2026-09-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py`, `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py`；关联提交 `5828cd49276a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+329/-67，可读 patch 489 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add GLM-5.3 MI30x and MI35x nightly accuracy tests」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py`；技术摘要: 覆盖「[AMD] Add GLM-5.3 MI30x and MI35x nightly accuracy tests」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: of, TestGLM53EvalMI35x, test_glm_53，涉及 `of, TestGLM53EvalMI35x, test_glm_53`；`test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: TestGLM53EvalMI30x, test_glm_53，涉及 `TestGLM53EvalMI30x, test_glm_53`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: of, TestGLM53EvalMI35x, test_glm_53
  - `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: TestGLM53EvalMI30x, test_glm_53
- 关键代码摘录:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py
@@ -0,0 +1,151 @@
+"""MI35x GLM-5.3 GSM8K Accuracy Evaluation Test (8-GPU)
+Tests zai-org/GLM-5.3 (FP8) on MI35x (gfx950) with the GLM-5.3 cookbook's
+MI355X / FP8 / low-latency / single-node cell: TP8, DSA tilelang prefill+decode,
+131072 chunked prefill, 0.80 static memory fraction, and a 20-minute watchdog
+for weight loading. No MTP: the cookbook disables speculative decoding on AMD.
+The day-0 dashboard (https://rocm.github.io/sglang-ci/day0/) lists MI355X FP8 as
diff -- test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py
@@ -0,0 +1,142 @@
+"""MI30x GLM-5.3 GSM8K Accuracy Evaluation Test (8-GPU)
+Tests zai-org/GLM-5.3 (FP8) on MI30x (gfx942) with the GLM-5.3 cookbook's
+MI300X / FP8 / low-latency / single-node cell: TP8, DSA tilelang prefill+decode,
+131072 chunked prefill, 0.80 static memory fraction, and a 20-minute watchdog
+for weight loading. The MI325X cell uses the same flags. Same eval and
+threshold as the gfx950 gate in test_glm53_eval_mi35x.py.
```

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py` added +151/-0; `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py` added +142/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py`, `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py`, `test/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41986 - [Docs] Add NVIDIA NVFP4 checkpoint to GLM-5.3-Flash cookbook

- 链接: https://github.com/sgl-project/sglang/pull/41986
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `40e1bb0f3667`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+258/-227，可读 patch 648 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Add NVIDIA NVFP4 checkpoint to GLM-5.3-Flash cookbook」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] Add NVIDIA NVFP4 checkpoint to GLM-5.3-Flash cookbook」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +227/-66 (293 lines); hunks: -19,7 +19,13 @@ export const config = {; -150,6 +156,7 @@ export const config = {；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +30/-160 (190 lines); hunks: -210,166 +210,6 @@ export const benchmarks = [; -509,12 +349,42 @@ export const benchmarks = [；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +1/-1 (2 lines); hunks: -71,7 +71,7 @@ GLM-5.3-Flash is a natively multimodal Mixture-of-Experts mode...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +227/-66 (293 lines); hunks: -19,7 +19,13 @@ export const config = {; -150,6 +156,7 @@ export const config = {
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +30/-160 (190 lines); hunks: -210,166 +210,6 @@ export const benchmarks = [; -509,12 +349,42 @@ export const benchmarks = [
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +1/-1 (2 lines); hunks: -71,7 +71,7 @@ GLM-5.3-Flash is a natively multimodal Mixture-of-Experts mode...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -19,7 +19,13 @@ export const config = {
-          label: "NVFP4",
+          label: "NVFP4 (RDXA)",
+          disabled: (s) => !["gb300", "gb200", "b200", "b300"].includes(s.hw),
+          disableReason: "The NVFP4 W4A4 kernels are Blackwell-only; Hopper cannot serve this checkpoint.",
+        },
+        {
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -210,166 +210,6 @@ export const benchmarks = [
-  {
-    match: { hw: "gb300", strategy: "low-latency", quant: "nvfp4", kvDsaPair: "bf16-tilelang" },
-    sglang_version: "fe236ea6c3",
-    latencyPercentile: "Mean",
-    speed: [
-      {
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -71,7 +71,7 @@ GLM-5.3-Flash is a natively multimodal Mixture-of-Experts model built around a h
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +227/-66; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +30/-160; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #39273 - [AMD] [GLM-5.3-Flash] Enable FP8 and MXFP4 serving on gfx950

- 链接: https://github.com/sgl-project/sglang/pull/39273
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_modelopt.py`；关联提交 `f17f7705a5a6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 34 个文件，+1045/-115，可读 patch 1966 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [GLM-5.3-Flash] Enable FP8 and MXFP4 serving on gfx950」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[AMD] [GLM-5.3-Flash] Enable FP8 and MXFP4 serving on gfx950」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `test/registered/unit/models/test_glm5_next_modelopt.py`, `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +159/-7 (166 lines); hunks: -1,7 +1,7; -17,6 +17,12 @@ export const config = {；`test/registered/unit/models/test_glm5_next_modelopt.py` modified +43/-2 (45 lines); hunks: -1,6 +1,8; -10,7 +12,7; symbols: test_nextn_mapper_routes_checkpoint_names_to_runtime_modules, TestGlm5NextNextNScaleLoading, _load, _param，涉及 `test_nextn_mapper_routes_checkpoint_names_to_runtime_modules, TestGlm5NextNextNScaleLoading, _load`；`python/sglang/srt/models/glm5_next.py` modified +9/-3 (12 lines); hunks: -25,6 +25,7; -317,11 +318,14 @@ def __init__(; symbols: __init__, load_weights, maybe_map_fp8_block_scale_name，涉及 `__init__, load_weights, maybe_map_fp8_block_scale_name`；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +13/-11 (24 lines); hunks: -1,6 +1,6; -16,7 +16,9 @@ Use an SGLang build that includes GLM-5.3-Flash support (v0.5....。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +159/-7 (166 lines); hunks: -1,7 +1,7; -17,6 +17,12 @@ export const config = {
  - `test/registered/unit/models/test_glm5_next_modelopt.py` modified +43/-2 (45 lines); hunks: -1,6 +1,8; -10,7 +12,7; symbols: test_nextn_mapper_routes_checkpoint_names_to_runtime_modules, TestGlm5NextNextNScaleLoading, _load, _param
  - `python/sglang/srt/models/glm5_next.py` modified +9/-3 (12 lines); hunks: -25,6 +25,7; -317,11 +318,14 @@ def __init__(; symbols: __init__, load_weights, maybe_map_fp8_block_scale_name
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +13/-11 (24 lines); hunks: -1,6 +1,6; -16,7 +16,9 @@ Use an SGLang build that includes GLM-5.3-Flash support (v0.5....
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -1,7 +1,7 @@
-  supportedHardware: ["gb300", "h100", "h200", "b200", "b300", "gb200"],
+  supportedHardware: ["gb300", "h100", "h200", "b200", "b300", "gb200", "mi355x"],
@@ -17,6 +17,12 @@ export const config = {
+        {
+          id: "mxfp4",
+          label: "MXFP4",
diff -- test/registered/unit/models/test_glm5_next_modelopt.py
@@ -1,6 +1,8 @@
-from unittest.mock import patch
+from unittest.mock import Mock, patch
+import torch
@@ -10,7 +12,7 @@
-register_cpu_ci(est_time=5, suite="base-a-test-cpu")
+register_cpu_ci(est_time=6, suite="base-a-test-cpu")
diff -- python/sglang/srt/models/glm5_next.py
@@ -25,6 +25,7 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +159/-7; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +13/-11
  - tests: `test/registered/unit/models/test_glm5_next_modelopt.py` modified +43/-2
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +9/-3
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_fused_kda_conv_recurrent_verify.py`, `test/registered/kernels/ops/attention/test_kpool_topk_transform_fused.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/layers/attention/test_dsa_mqa_logits_chunking.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #42109 - [Docs] GLM-5.2 GB300 NVFP4: add env vars from InferenceX AgentX recipe

- 链接: https://github.com/sgl-project/sglang/pull/42109
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `8acd36b56bfa`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+41/-7，可读 patch 78 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.2 GB300 NVFP4: add env vars from InferenceX AgentX recipe」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「[Docs] GLM-5.2 GB300 NVFP4: add env vars from InferenceX AgentX recipe」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +41/-7 (48 lines); hunks: -817,28 +817,55 @@ sgl-eval run aime25 \\; -860,7 +887,14 @@ sgl-eval run aime25 \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +41/-7 (48 lines); hunks: -817,28 +817,55 @@ sgl-eval run aime25 \\; -860,7 +887,14 @@ sgl-eval run aime25 \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -817,28 +817,55 @@ sgl-eval run aime25 \\
-      env: [],
+      env: [
+        "SGLANG_DISABLE_TP_MEMORY_INBALANCE_CHECK=1",
+        "SGLANG_ENABLE_THINKING=1",
+        "SGLANG_ENABLE_UNIFIED_RADIX_TREE=1",
+        "SGLANG_HICACHE_DEBUG_LOG=1",
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +41/-7
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #42278 - [Docs][AMD] Update GLM-5.2 MI355X daily image to 20260930

- 链接: https://github.com/sgl-project/sglang/pull/42278
- 状态/时间: merged / 2026-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；关联提交 `cbe070b6bfce`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs][AMD] Update GLM-5.2 MI355X daily image to 20260930」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Docs][AMD] Update GLM-5.2 MI355X daily image to 20260930」；主要实现面是 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -124,7 +124,7 @@ import { Playground } from "/src/snippets/_playground.jsx";
-- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260924`. Choose **Lo
+- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260930`. Choose **Lo
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #41870 - [AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4

- 链接: https://github.com/sgl-project/sglang/pull/41870
- 状态/时间: merged / 2026-10-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_bfg_fusion.py`；关联提交 `af1bef3eaf72`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+245/-7，可读 patch 353 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/unit/models/test_glm5_next_bfg_fusion.py`, `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4」；主要实现面是 `test/registered/unit/models/test_glm5_next_bfg_fusion.py`, `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/models/test_glm5_next_bfg_fusion.py` modified +65/-0 (65 lines); hunks: -5,6 +5,7; -30,6 +31,8 @@ class MockFp8Config:; symbols: MockFp8Config, __init__, get_name, get_quant_method，涉及 `MockFp8Config, __init__, get_name`；`python/sglang/srt/models/glm5_next.py` modified +51/-7 (58 lines); hunks: -40,7 +40,6; -54,7 +53,6; symbols: _can_fuse_proj, shared_experts_fusion_disable_reason, _quark_mxfp4_shared_fusion_disable_reason，涉及 `_can_fuse_proj, shared_experts_fusion_disable_reason, _quark_mxfp4_shared_fusion_disable_reason`。
- 代码 diff 细节:
  - `test/registered/unit/models/test_glm5_next_bfg_fusion.py` modified +65/-0 (65 lines); hunks: -5,6 +5,7; -30,6 +31,8 @@ class MockFp8Config:; symbols: MockFp8Config, __init__, get_name, get_quant_method
  - `python/sglang/srt/models/glm5_next.py` modified +51/-7 (58 lines); hunks: -40,7 +40,6; -54,7 +53,6; symbols: _can_fuse_proj, shared_experts_fusion_disable_reason, _quark_mxfp4_shared_fusion_disable_reason
- 关键代码摘录:

```diff
diff -- test/registered/unit/models/test_glm5_next_bfg_fusion.py
@@ -5,6 +5,7 @@
+from sglang.srt.layers.quantization.base_config import QuantizationConfig
@@ -30,6 +31,8 @@ class MockFp8Config:
+    is_linear_unquantized = QuantizationConfig.is_linear_unquantized
@@ -44,6 +47,35 @@ def get_quant_method(self, layer, prefix):
+def quark_mxfp4_config(excluded):
+    """A Quark MXFP4 export that keeps `excluded` in BF16, named as the HF
diff -- python/sglang/srt/models/glm5_next.py
@@ -40,7 +40,6 @@
-    LinearBase,
@@ -54,7 +53,6 @@
-from sglang.srt.layers.quantization.unquant import UnquantizedLinearMethod
@@ -359,10 +357,10 @@ def _can_fuse_proj(
+            "quark",
-        probe = LinearBase(1, 1)
```

- 已读文件:
  - tests: `test/registered/unit/models/test_glm5_next_bfg_fusion.py` modified +65/-0
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +51/-7
- 验证与风险: diff 自带测试面 `test/registered/unit/models/test_glm5_next_bfg_fusion.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #42167 - [Docs] GLM-5.2: move GB300 AgentX recipe to the agentic HiCache section and drop no-op settings

- 链接: https://github.com/sgl-project/sglang/pull/42167
- 状态/时间: merged / 2026-10-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `f2f0be731cdc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+78/-41，可读 patch 153 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.2: move GB300 AgentX recipe to the agentic HiCache section and drop no-op settings」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Docs] GLM-5.2: move GB300 AgentX recipe to the agentic HiCache section and drop no-op settings」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +7/-41 (48 lines); hunks: -817,55 +817,28 @@ sgl-eval run aime25 \\; -887,14 +860,7 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +71/-0 (71 lines); hunks: -303,3 +303,74 @@ python3 -m sglang.launch_server \。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +7/-41 (48 lines); hunks: -817,55 +817,28 @@ sgl-eval run aime25 \\; -887,14 +860,7 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +71/-0 (71 lines); hunks: -303,3 +303,74 @@ python3 -m sglang.launch_server \
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -817,55 +817,28 @@ sgl-eval run aime25 \\
-      env: [
-        "SGLANG_DISABLE_TP_MEMORY_INBALANCE_CHECK=1",
-        "SGLANG_ENABLE_THINKING=1",
-        "SGLANG_ENABLE_UNIFIED_RADIX_TREE=1",
-        "SGLANG_HICACHE_DEBUG_LOG=1",
-        "SGLANG_HICACHE_DEBUG_SAMPLE_RATE=16384",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -303,3 +303,74 @@ python3 -m sglang.launch_server \
+**GB300 (TP4, single node):** one 4-GPU GB300 node serves the whole model. All three commands offload KV cache to host DRAM with `--hicache-size 135` (GB of host memory per rank,
+Low-latency (TP4, MTP 5-1-6, up to 16 concurrent requests):
+'''bash Command
+sglang serve \
+  --model-path nvidia/GLM-5.2-NVFP4 \
+  --trust-remote-code \
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +7/-41; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +71/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #42613 - docs(cookbook): enable Top-K v2 for GLM-5.2 MI355X MTP

- 链接: https://github.com/sgl-project/sglang/pull/42613
- 状态/时间: merged / 2026-10-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `c76faa1ff290`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-3，可读 patch 25 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「docs(cookbook): enable Top-K v2 for GLM-5.2 MI355X MTP」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「docs(cookbook): enable Top-K v2 for GLM-5.2 MI355X MTP」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +4/-3 (7 lines); hunks: -1034,12 +1034,13 @@ sgl-eval run aime25 \\; -1082,7 +1083,7 @@ sgl-eval run aime25 \\。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +4/-3 (7 lines); hunks: -1034,12 +1034,13 @@ sgl-eval run aime25 \\; -1082,7 +1083,7 @@ sgl-eval run aime25 \\
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -1034,12 +1034,13 @@ sgl-eval run aime25 \\
-    // DSA backend: triton (SGLang's ROCm default).
+    // DSA backend: triton (SGLang's ROCm default). Five-step MTP cells select
+    // the top-k v2 indexer kernel, matching InferenceX PR #3724.
-      env: [],
+      env: ["SGLANG_OPT_USE_TOPK_V2=1"],
@@ -1082,7 +1083,7 @@ sgl-eval run aime25 \\
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +4/-3
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #42693 - [GLM-5.3-Flash] Autotune MoE kernels at prefill sizes

- 链接: https://github.com/sgl-project/sglang/pull/42693
- 状态/时间: merged / 2026-10-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/glm5_next.py`；关联提交 `fcbbefa82a78`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+32/-0，可读 patch 53 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-5.3-Flash] Autotune MoE kernels at prefill sizes」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`；技术摘要: 覆盖「[GLM-5.3-Flash] Autotune MoE kernels at prefill sizes」；主要实现面是 `python/sglang/srt/models/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +32/-0 (32 lines); hunks: -26,6 +26,7; -51,6 +52,7; symbols: determine_num_fused_shared_experts, wants_prefill_autotune, autotune_prefill_kernels, set_eagle3_layers_to_capture，涉及 `determine_num_fused_shared_experts, wants_prefill_autotune, autotune_prefill_kernels`。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +32/-0 (32 lines); hunks: -26,6 +26,7; -51,6 +52,7; symbols: determine_num_fused_shared_experts, wants_prefill_autotune, autotune_prefill_kernels, set_eagle3_layers_to_capture
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -26,6 +26,7 @@
+from sglang.srt.layers.dp_attention import is_dp_attention_enabled
@@ -51,6 +52,7 @@
+    get_moe_runner_backend,
@@ -1457,6 +1459,36 @@ def determine_num_fused_shared_experts(self):
+    def wants_prefill_autotune(self) -> bool:
+        backend = get_moe_runner_backend()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +32/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/glm5_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42905 - [KDA] Default GLM-5-Next spec verify to the CuTe DSL KDA kernel

- 链接: https://github.com/sgl-project/sglang/pull/42905
- 状态/时间: merged / 2026-10-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/arg_groups/glm5_next_hook.py`；关联提交 `f47d89564dc2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+43/-0，可读 patch 51 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[KDA] Default GLM-5-Next spec verify to the CuTe DSL KDA kernel」；模型线: GLM-5/5.1；类别: 模型实现调整；主要 diff: `python/sglang/srt/arg_groups/glm5_next_hook.py`；技术摘要: 覆盖「[KDA] Default GLM-5-Next spec verify to the CuTe DSL KDA kernel」；主要实现面是 `python/sglang/srt/arg_groups/glm5_next_hook.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/arg_groups/glm5_next_hook.py` added +36/-0 (36 lines); hunks: -0,0 +1,36; symbols: apply_glm5_next_spec_backend_defaults，涉及 `apply_glm5_next_spec_backend_defaults`。
- 代码 diff 细节:
  - `python/sglang/srt/arg_groups/glm5_next_hook.py` added +36/-0 (36 lines); hunks: -0,0 +1,36; symbols: apply_glm5_next_spec_backend_defaults
- 关键代码摘录:

```diff
diff -- python/sglang/srt/arg_groups/glm5_next_hook.py
@@ -0,0 +1,36 @@
+from __future__ import annotations
+import logging
+from typing import TYPE_CHECKING
+from sglang.srt.arg_groups.overrides import (
+    declare_resolution,
+    resolving_view,
```

- 已读文件:
  - runtime: `python/sglang/srt/arg_groups/glm5_next_hook.py` added +36/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/arg_groups/glm5_next_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #43015 - [Docs] GLM-5.3-Flash: measured MI355X MXFP4 agentic recipe

- 链接: https://github.com/sgl-project/sglang/pull/43015
- 状态/时间: merged / 2026-10-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `79ef49cb6bf9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+11/-10，可读 patch 59 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] GLM-5.3-Flash: measured MI355X MXFP4 agentic recipe」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] GLM-5.3-Flash: measured MI355X MXFP4 agentic recipe」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +8/-9 (17 lines); hunks: -136,12 +136,11 @@ export const config = {; -394,9 +393,9 @@ sgl-eval run gsm8k \\；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-1 (4 lines); hunks: -29,7 +29,7 @@ Choose your hardware, then choose the operating point that mat...; -126,6 +126,8 @@ On Blackwell, the recipes default to an FP8 KV cache with TR...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +8/-9 (17 lines); hunks: -136,12 +136,11 @@ export const config = {; -394,9 +393,9 @@ sgl-eval run gsm8k \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-1 (4 lines); hunks: -29,7 +29,7 @@ Choose your hardware, then choose the operating point that mat...; -126,6 +126,8 @@ On Blackwell, the recipes default to an FP8 KV cache with TR...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -136,12 +136,11 @@ export const config = {
-            ? ["--enable-hierarchical-cache", "--hicache-ratio 0.50",
-              "--hicache-write-policy write_through", "--hicache-io-backend direct",
-              "--hicache-mem-layout page_first_direct"]
+            ? ["--enable-hierarchical-cache", "--hicache-size 180",
+              "--hicache-write-policy write_through"]
-            ? ["Host cache matches the measured 0.50-ratio, write-through MI355X recipe; check available RAM."]
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -29,7 +29,7 @@ Choose your hardware, then choose the operating point that matches your workload
-The recommended selection is only a starting point. The same panel also lets you override the KV/DSA pairing, multimodal feature transport, Breakable Cuda Graph, and HiCache tiers
+The recommended selection is only a starting point. The same panel also lets you override the KV/DSA pairing, multimodal feature transport, Breakable Cuda Graph, and HiCache tiers
@@ -126,6 +126,8 @@ On Blackwell, the recipes default to an FP8 KV cache with TRT-LLM DSA: on GB300
+For agentic MXFP4 serving on MI355X, select **Low Latency** with **L1 + L2**. The host tier uses `--hicache-size 180` (about 190 GB of host memory per rank once the KDA state and
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +8/-9; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +3/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #42726 - [Docs] Cookbook: interactive SemiAnalysis InferenceX AgentX launches for GLM-5.2, DeepSeek-V4 and DeepSeek-V4.1

- 链接: https://github.com/sgl-project/sglang/pull/42726
- 状态/时间: merged / 2026-10-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；关联提交 `7b6b6ee25eed`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+16341/-255，可读 patch 1160 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Cookbook: interactive SemiAnalysis InferenceX AgentX launches for GLM-5.2, DeepSeek-V4 and DeepSeek-V4.1」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Docs] Cookbook: interactive SemiAnalysis InferenceX AgentX launches for GLM-5.2, DeepSeek-V4 and DeepSeek-V4.1」；主要实现面是 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` added +5061/-0 (5061 lines)；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +14/-102 (116 lines); hunks: -49,7 +49,7 @@ import { Deployment } from "/src/snippets/_deployment.jsx";; -67,6 +67,19 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` added +5061/-0 (5061 lines)
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +14/-102 (116 lines); hunks: -49,7 +49,7 @@ import { Deployment } from "/src/snippets/_deployment.jsx";; -67,6 +67,19 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -49,7 +49,7 @@ import { Deployment } from "/src/snippets/_deployment.jsx";
-<Deployment config={config} benchmarks={benchmarks} />
+<Deployment config={config} benchmarks={benchmarks} agenticLink="agentic-long-context-deployment" />
@@ -67,6 +67,19 @@ import { Playground } from "/src/snippets/_playground.jsx";
+## Agentic Long-Context Deployment
+Agentic workloads, such as coding agents and other multi-turn, tool-using assistants, send long prompts whose prefixes grow and repeat from turn to turn. Serving them well depends
+- **Router.** Each configuration was submitted behind one front door: Dynamo (`dynamo.frontend` with `dynamo.sglang` workers) or SGLang (`sglang.launch_server`, behind `sglang_rou
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` added +5061/-0; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +14/-102
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #42044 - [CP] GLM-5.3-Flash Prefill CP implemented on layer boundaries

- 链接: https://github.com/sgl-project/sglang/pull/42044
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py`；关联提交 `33bffcd490f8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 21 个文件，+590/-96，可读 patch 1151 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CP] GLM-5.3-Flash Prefill CP implemented on layer boundaries」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py`, `python/sglang/srt/configs/glm5_next.py`；技术摘要: 覆盖「[CP] GLM-5.3-Flash Prefill CP implemented on layer boundaries」；主要实现面是 `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/glm5_next_nextn.py`, `python/sglang/srt/configs/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/glm5_next.py` modified +85/-23 (108 lines); hunks: -30,6 +30,7; -68,6 +69,7; symbols: __init__，涉及 `__init__`；`python/sglang/srt/models/glm5_next_nextn.py` modified +9/-0 (9 lines); hunks: -22,6 +22,15; symbols: Glm5NextForConditionalGenerationNextN, prepare_cp_inputs, get_hf_to_sglang_mapper，涉及 `Glm5NextForConditionalGenerationNextN, prepare_cp_inputs, get_hf_to_sglang_mapper`；`python/sglang/srt/configs/glm5_next.py` modified +3/-2 (5 lines); hunks: -4,7 +4,6; -262,8 +261,10 @@ def full_attention_layer_ids(self):; symbols: full_attention_layer_ids, mamba2_cache_params，涉及 `full_attention_layer_ids, mamba2_cache_params`；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +33/-2 (35 lines); hunks: -130,7 +130,7 @@ For agentic MXFP4 serving on MI355X, select **Low Latency**...; -202,7 +202,38 @@ This topology served image requests and videos up to 238,08...。
- 代码 diff 细节:
  - `python/sglang/srt/models/glm5_next.py` modified +85/-23 (108 lines); hunks: -30,6 +30,7; -68,6 +69,7; symbols: __init__
  - `python/sglang/srt/models/glm5_next_nextn.py` modified +9/-0 (9 lines); hunks: -22,6 +22,15; symbols: Glm5NextForConditionalGenerationNextN, prepare_cp_inputs, get_hf_to_sglang_mapper
  - `python/sglang/srt/configs/glm5_next.py` modified +3/-2 (5 lines); hunks: -4,7 +4,6; -262,8 +261,10 @@ def full_attention_layer_ids(self):; symbols: full_attention_layer_ids, mamba2_cache_params
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +33/-2 (35 lines); hunks: -130,7 +130,7 @@ For agentic MXFP4 serving on MI355X, select **Low Latency**...; -202,7 +202,38 @@ This topology served image requests and videos up to 238,08...
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/glm5_next.py
@@ -30,6 +30,7 @@
+    SumGroup,
@@ -68,6 +69,7 @@
+    prepare_mm_inputs,
@@ -395,7 +397,13 @@ def __init__(
-        head_shard_size = get_parallel().attn_tp_size
+        from sglang.srt.runtime_context import (
diff -- python/sglang/srt/models/glm5_next_nextn.py
@@ -22,6 +22,15 @@
+    def prepare_cp_inputs(self, forward_batch, **kwargs):
+        # The worker has rotated the target's multimodal embeddings per request.
+        # Fill each appended token while indices still address full sequences,
+        # then let the runner shard embeddings and target states together.
+        input_embeds = self.model.embed_input_ids(
+            forward_batch.input_ids, forward_batch
diff -- python/sglang/srt/configs/glm5_next.py
@@ -4,7 +4,6 @@
```

- 已读文件:
  - runtime: `python/sglang/srt/models/glm5_next.py` modified +85/-23; `python/sglang/srt/models/glm5_next_nextn.py` modified +9/-0; `python/sglang/srt/configs/glm5_next.py` modified +3/-2
  - docs: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +33/-2
- 验证与风险: diff 自带测试面 `test/registered/cp/test_cp_strategy_unit.py`, `test/registered/cp/test_glm53_flash_cp.py`, `test/registered/unit/layer_boundary/test_declared_decoder_boundary.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43083 - [Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1

- 链接: https://github.com/sgl-project/sglang/pull/43083
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；关联提交 `1fc6b8962c02`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+14703/-1042，可读 patch 5223 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「[Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1」；主要实现面是 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +424/-162 (586 lines); hunks: -1,37 +1,57; -232,10 +252,10 @@ export const agentx = {。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +424/-162 (586 lines); hunks: -1,37 +1,57; -232,10 +252,10 @@ export const agentx = {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/agentx/zai-org/glm-5.2.jsx
@@ -1,37 +1,57 @@
-// (SemiAnalysisAI/InferenceX main@0259609ce99d plus open PRs #3187, #3598, #3631, #3659, #3745), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@ceb50ba21208 plus open PRs #2978, #3606, #3701, #3744, #3782, #3816, #3817, #3836, #3840), with SA-specific settings removed.
- "generatedOn": "2026-10-06",
+ "generatedOn": "2026-10-08",
-  "main": "0259609ce99d0f4f7bd7180c3b3436e4f0334a46",
+  "main": "ceb50ba212080174e0563d2be1db9b0d654ab2ef",
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +424/-162
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/_agentx.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #42845 - [GLM-5.3-Flash] Enable breakable prefill CUDA graph by default

- 链接: https://github.com/sgl-project/sglang/pull/42845
- 状态/时间: merged / 2026-10-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_glm53_flash_b200.py`；关联提交 `72eab59bf639`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+6/-35，可读 patch 83 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-5.3-Flash] Enable breakable prefill CUDA graph by default」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/e2e/models/test_glm53_flash_b200.py`；技术摘要: 覆盖「[GLM-5.3-Flash] Enable breakable prefill CUDA graph by default」；主要实现面是 `test/registered/e2e/models/test_glm53_flash_b200.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +0/-2 (2 lines); hunks: -107,8 +107,6 @@ class TestGLM53FlashB200HighThroughput(; symbols: TestGLM53FlashB200HighThroughput，涉及 `TestGLM53FlashB200HighThroughput`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_glm53_flash_b200.py` modified +0/-2 (2 lines); hunks: -107,8 +107,6 @@ class TestGLM53FlashB200HighThroughput(; symbols: TestGLM53FlashB200HighThroughput
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_glm53_flash_b200.py
@@ -107,8 +107,6 @@ class TestGLM53FlashB200HighThroughput(
-        "--cuda-graph-backend-prefill",
-        "breakable",
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +0/-2
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_glm53_flash_b200.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43802 - [Docs] Update GLM-5.3-Flash playground: B300 default, CP8, EP and PD

- 链接: https://github.com/sgl-project/sglang/pull/43802
- 状态/时间: merged / 2026-10-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `450837e770ce`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+92/-32，可读 patch 245 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Update GLM-5.3-Flash playground: B300 default, CP8, EP and PD」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Docs] Update GLM-5.3-Flash playground: B300 default, CP8, EP and PD」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +56/-26 (82 lines); hunks: -1,7 +1,7; -270,7 +270,16 @@ sgl-eval run gsm8k \\；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-2 (8 lines); hunks: -22,7 +22,7 @@ For MI355X, follow the [AMD GPU installation guide](/docs/hard...; -45,7 +45,7 @@ Generated commands leave `--mamba-full-memory-ratio` at its `0...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +56/-26 (82 lines); hunks: -1,7 +1,7; -270,7 +270,16 @@ sgl-eval run gsm8k \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-2 (8 lines); hunks: -22,7 +22,7 @@ For MI355X, follow the [AMD GPU installation guide](/docs/hard...; -45,7 +45,7 @@ Generated commands leave `--mamba-full-memory-ratio` at its `0...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -1,7 +1,7 @@
-  supportedHardware: ["gb300", "h100", "h200", "b200", "b300", "gb200", "mi355x"],
+  supportedHardware: ["b300", "gb300", "h100", "h200", "b200", "gb200", "mi355x"],
@@ -270,7 +270,16 @@ sgl-eval run gsm8k \\
-        { id: "cp", label: "CP", values: [null, 1, 2, 4] },
+        {
+          id: "cp", label: "CP",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -22,7 +22,7 @@ For MI355X, follow the [AMD GPU installation guide](/docs/hardware-platforms/amd
-Choose your hardware, then choose the operating point that matches your workload:
+The cookbook opens on **B300**. Choose your hardware, then choose the operating point that matches your workload:
@@ -45,7 +45,7 @@ Generated commands leave `--mamba-full-memory-ratio` at its `0.9` default, which
-Use the Playground for lower-level tuning such as attention parallelism, MoE communication, speculative decoding, and reasoning or tool parsers. It inherits every selection from t
+Use the Playground for lower-level tuning such as attention parallelism, MoE communication, PD disaggregation, speculative decoding, and reasoning or tool parsers. It inherits eve
@@ -206,6 +206,8 @@ Install `torchcodec` for video and see the [encoder disaggregation guide](/docs/
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +56/-26; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +6/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #43799 - [Docs] Cookbook: refresh SemiAnalysis AgentX launches (GLM-5.2 B300, DeepSeek-V4.1 GB300)

- 链接: https://github.com/sgl-project/sglang/pull/43799
- 状态/时间: merged / 2026-10-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；关联提交 `b0c84d45189a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+1624/-590，可读 patch 3227 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Cookbook: refresh SemiAnalysis AgentX launches (GLM-5.2 B300, DeepSeek-V4.1 GB300)」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「[Docs] Cookbook: refresh SemiAnalysis AgentX launches (GLM-5.2 B300, DeepSeek-V4.1 GB300)」；主要实现面是 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +223/-136 (359 lines); hunks: -1,28 +1,28; -34,23 +34,18 @@ export const agentx = {。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +223/-136 (359 lines); hunks: -1,28 +1,28; -34,23 +34,18 @@ export const agentx = {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/agentx/zai-org/glm-5.2.jsx
@@ -1,28 +1,28 @@
-// (SemiAnalysisAI/InferenceX main@ceb50ba21208 plus open PRs #2978, #3606, #3701, #3744, #3782, #3816, #3817, #3836, #3840), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@4f00011e81e6 plus open PRs #2978, #3606, #3701, #3817, #3836, #3859, #3860, #3890), with SA-specific settings removed.
- "generatedOn": "2026-10-08",
+ "generatedOn": "2026-10-12",
-  "main": "ceb50ba212080174e0563d2be1db9b0d654ab2ef",
+  "main": "4f00011e81e6d9eb9bda5c0f6870b58d2254f40b",
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +223/-136
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #43983 - [Docs] Cookbook: refresh SemiAnalysis AgentX launches (DeepSeek-V4.1 GB200/GB300, GLM-5.2 FP8 B300)

- 链接: https://github.com/sgl-project/sglang/pull/43983
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；关联提交 `dbad07a06fbe`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+451/-845，可读 patch 2033 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Docs] Cookbook: refresh SemiAnalysis AgentX launches (DeepSeek-V4.1 GB200/GB300, GLM-5.2 FP8 B300)」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「[Docs] Cookbook: refresh SemiAnalysis AgentX launches (DeepSeek-V4.1 GB200/GB300, GLM-5.2 FP8 B300)」；主要实现面是 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +111/-43 (154 lines); hunks: -1,52 +1,47; -2513,10 +2508,10 @@ export const agentx = {。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +111/-43 (154 lines); hunks: -1,52 +1,47; -2513,10 +2508,10 @@ export const agentx = {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/agentx/zai-org/glm-5.2.jsx
@@ -1,52 +1,47 @@
-// (SemiAnalysisAI/InferenceX main@4f00011e81e6 plus open PRs #2978, #3606, #3701, #3817, #3836, #3859, #3860, #3890), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@029d019d1b4b plus open PRs #2978, #3606, #3817, #3836, #3859, #3860, #3927), with SA-specific settings removed.
-  "main": "4f00011e81e6d9eb9bda5c0f6870b58d2254f40b",
+  "main": "029d019d1b4bb89717ca8db137e6000d8e6bf583",
-   "2978": {
-    "run": "https://github.com/SemiAnalysisAI/InferenceX/actions/runs/34548026742",
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +111/-43
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #43975 - [CI] Use sgl-eval for GLM-5.3-Flash GSM8K tests

- 链接: https://github.com/sgl-project/sglang/pull/43975
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_glm53_flash_b200.py`；关联提交 `195cb7afb49f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+45/-22，可读 patch 130 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Use sgl-eval for GLM-5.3-Flash GSM8K tests」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/e2e/models/test_glm53_flash_b200.py`；技术摘要: 覆盖「[CI] Use sgl-eval for GLM-5.3-Flash GSM8K tests」；主要实现面是 `test/registered/e2e/models/test_glm53_flash_b200.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +24/-12 (36 lines); hunks: -75,12 +75,14 @@ class TestGLM53FlashB200LowLatency(; -100,9 +102,14 @@ class TestGLM53FlashB200HighThroughput(; symbols: TestGLM53FlashB200LowLatency, TestGLM53FlashB200HighThroughput, TestGLM53FlashB200DFlash2，涉及 `TestGLM53FlashB200LowLatency, TestGLM53FlashB200HighThroughput, TestGLM53FlashB200DFlash2`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_glm53_flash_b200.py` modified +24/-12 (36 lines); hunks: -75,12 +75,14 @@ class TestGLM53FlashB200LowLatency(; -100,9 +102,14 @@ class TestGLM53FlashB200HighThroughput(; symbols: TestGLM53FlashB200LowLatency, TestGLM53FlashB200HighThroughput, TestGLM53FlashB200DFlash2
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_glm53_flash_b200.py
@@ -75,12 +75,14 @@ class TestGLM53FlashB200LowLatency(
-    gsm8k_score_threshold = 0.93
-    # Match the established DSA+MTP accuracy workload. The generic 200-question,
-    # 5-shot defaults leave a single question worth 0.5 percentage points and
-    # make this tight quality floor unnecessarily sensitive to kernel numerics.
-    gsm8k_num_examples = 500
-    gsm8k_num_shots = 20
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +24/-12
- 验证与风险: diff 自带测试面 `python/sglang/test/kits/eval_accuracy_kit.py`, `test/registered/e2e/models/test_glm53_flash_b200.py`, `test/registered/e2e/models/test_glm53_flash_h200.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41790 - [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.3-Flash with BF16 KV Cache

- 链接: https://github.com/sgl-project/sglang/pull/41790
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `5100f8d11d1d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+752/-63，可读 patch 1013 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.3-Flash with BF16 KV Cache」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.3-Flash with BF16 KV Cache」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +22/-2 (24 lines); hunks: -91,6 +91,22 @@ export const config = {; -927,7 +943,9 @@ sgl-eval run gsm8k \\；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +6/-0 (6 lines); hunks: -265,6 +265,12 @@ export const benchmarks = [；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +2/-0 (2 lines); hunks: -122,6 +122,8 @@ Keep the checkpoint's KDA lower-bound setting unchanged. In...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +22/-2 (24 lines); hunks: -91,6 +91,22 @@ export const config = {; -927,7 +943,9 @@ sgl-eval run gsm8k \\
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +6/-0 (6 lines); hunks: -265,6 +265,12 @@ export const benchmarks = [
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +2/-0 (2 lines); hunks: -122,6 +122,8 @@ Keep the checkpoint's KDA lower-bound setting unchanged. In...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -91,6 +91,22 @@ export const config = {
+        // Order matters: a disabled pick is re-seated onto the first enabled
+        // option, so this entry must stay after BF16 + TileLang to keep the
+        // Hopper default unchanged.
+        {
+          id: "bf16-q8-prefill",
+          label: "BF16 + Q8 sparse prefill",
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -265,6 +265,12 @@ export const benchmarks = [
+  // BF16 + Q8 sparse prefill has only a relative A/B so far; these empty entries outrank the hw + strategy rows above.
+  // A defaultAccuracy added to glm-5.3-flash.jsx would show on them as if it were measured.
+  { match: { hw: "h200", strategy: "low-latency", kvDsaPair: "bf16-q8-prefill" } },
+  { match: { hw: "h200", strategy: "high-throughput", kvDsaPair: "bf16-q8-prefill" } },
+  { match: { hw: "h100", strategy: "low-latency", kvDsaPair: "bf16-q8-prefill" } },
+  { match: { hw: "h100", strategy: "high-throughput", kvDsaPair: "bf16-q8-prefill" } },
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -122,6 +122,8 @@ Keep the checkpoint's KDA lower-bound setting unchanged. In particular, do not o
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +22/-2; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +6/-0; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +2/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/ops/attention/test_q8kv8_dsa_nope_bf16_prefill.py`, `test/registered/unit/layers/attention/test_dsa_q8kv8_bf16_prefill_routing.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43735 - [DCP] Decode context parallelism for DSA (GLM-5.2 / GLM-5.3) with MTP

- 链接: https://github.com/sgl-project/sglang/pull/43735
- 状态/时间: merged / 2026-10-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/dcp/test_glm53_dcp2.py`；关联提交 `8bf145d11903`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 26 个文件，+565/-88，可读 patch 1241 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DCP] Decode context parallelism for DSA (GLM-5.2 / GLM-5.3) with MTP」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/dcp/test_glm53_dcp2.py`；技术摘要: 覆盖「[DCP] Decode context parallelism for DSA (GLM-5.2 / GLM-5.3) with MTP」；主要实现面是 `test/registered/dcp/test_glm53_dcp2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/dcp/test_glm53_dcp2.py` added +22/-0 (22 lines); hunks: -0,0 +1,22; symbols: TestGLM53NVFP4DCP2MTP，涉及 `TestGLM53NVFP4DCP2MTP`。
- 代码 diff 细节:
  - `test/registered/dcp/test_glm53_dcp2.py` added +22/-0 (22 lines); hunks: -0,0 +1,22; symbols: TestGLM53NVFP4DCP2MTP
- 关键代码摘录:

```diff
diff -- test/registered/dcp/test_glm53_dcp2.py
@@ -0,0 +1,22 @@
+import unittest
+from sglang.test.ci.ci_register import register_cuda_ci
+from sglang.test.kits.eval_accuracy_kit import GSM8KMixin
+from sglang.test.server_fixtures.dsa_mtp_fixture import (
+    DsaMtpEvalConfigDefaults,
+    DsaMtpServerBase,
```

- 已读文件:
  - tests: `test/registered/dcp/test_glm53_dcp2.py` added +22/-0
- 验证与风险: diff 自带测试面 `test/registered/dcp/test_dsa_dcp_attention.py`, `test/registered/dcp/test_glm53_dcp2.py`, `test/registered/hicache/test_dsa_host_release.py`, `test/registered/kernels/ops/attention/test_dcp_lse_combine.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44098 - [GLM-5.3-Flash] Drop the NextN layer from the KDA state pool

- 链接: https://github.com/sgl-project/sglang/pull/44098
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/glm5_next.py`；关联提交 `7f0434e4af02`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+3/-11，可读 patch 32 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[GLM-5.3-Flash] Drop the NextN layer from the KDA state pool」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/configs/glm5_next.py`；技术摘要: 覆盖「[GLM-5.3-Flash] Drop the NextN layer from the KDA state pool」；主要实现面是 `python/sglang/srt/configs/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/configs/glm5_next.py` modified +0/-5 (5 lines); hunks: -250,11 +250,6 @@ def is_kda_layer(self, layer_idx: int):; symbols: is_kda_layer, linear_layer_ids, nextn_layer_ids, full_attention_layer_ids，涉及 `is_kda_layer, linear_layer_ids, nextn_layer_ids`。
- 代码 diff 细节:
  - `python/sglang/srt/configs/glm5_next.py` modified +0/-5 (5 lines); hunks: -250,11 +250,6 @@ def is_kda_layer(self, layer_idx: int):; symbols: is_kda_layer, linear_layer_ids, nextn_layer_ids, full_attention_layer_ids
- 关键代码摘录:

```diff
diff -- python/sglang/srt/configs/glm5_next.py
@@ -250,11 +250,6 @@ def is_kda_layer(self, layer_idx: int):
-    @property
-    def nextn_layer_ids(self):
-        num_nextn_layers = self.num_nextn_predict_layers or 0
-        return [self.num_hidden_layers + i for i in range(num_nextn_layers)]
```

- 已读文件:
  - runtime: `python/sglang/srt/configs/glm5_next.py` modified +0/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #44192 - [CI] glm5.2: Temporarily disable PD HiSparse+MTP B300 test

- 链接: https://github.com/sgl-project/sglang/pull/44192
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；关联提交 `ff8d964cf5b6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-1，可读 patch 20 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] glm5.2: Temporarily disable PD HiSparse+MTP B300 test」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；技术摘要: 覆盖「[CI] glm5.2: Temporarily disable PD HiSparse+MTP B300 test」；主要实现面是 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +8/-1 (9 lines); hunks: -10,11 +10,18; symbols: TestGLM52PDHiSparseSpec，涉及 `TestGLM52PDHiSparseSpec`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +8/-1 (9 lines); hunks: -10,11 +10,18; symbols: TestGLM52PDHiSparseSpec
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_dsa_glm52_hisparse.py
@@ -10,11 +10,18 @@
-register_cuda_ci(est_time=700, stage="extra-b", runner_config="8-gpu-b300")
+register_cuda_ci(
+    est_time=700,
+    stage="extra-b",
+    runner_config="8-gpu-b300",
+    disabled="Temporarily disabled: NaN in EAGLE verify target logits on B300.",
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +8/-1
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44065 - [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main (GLM-5.2 NVFP4 B300 agg TP4, Dynamo frontend counts)

- 链接: https://github.com/sgl-project/sglang/pull/44065
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；关联提交 `721953c6f640`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+1177/-3524，可读 patch 6663 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main (GLM-5.2 NVFP4 B300 agg TP4, Dynamo frontend counts)」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`；技术摘要: 覆盖「[Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main (GLM-5.2 NVFP4 B300 agg TP4, Dynamo frontend counts)」；主要实现面是 `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +607/-206 (813 lines); hunks: -1,47 +1,22; -158,57 +133,49 @@ export const agentx = {。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +607/-206 (813 lines); hunks: -1,47 +1,22; -158,57 +133,49 @@ export const agentx = {
- 关键代码摘录:

```diff
diff -- docs/src/snippets/agentx/zai-org/glm-5.2.jsx
@@ -1,47 +1,22 @@
-// (SemiAnalysisAI/InferenceX main@029d019d1b4b plus open PRs #2978, #3606, #3817, #3836, #3859, #3860, #3927), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@01e3b46aea55 plus open PRs #3927, #3953), with SA-specific settings removed.
- "generatedOn": "2026-10-12",
+ "generatedOn": "2026-10-13",
-  "main": "029d019d1b4bb89717ca8db137e6000d8e6bf583",
+  "main": "01e3b46aea55f1840b5a430efafc2112de01b68b",
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +607/-206
- 验证与风险: 该 PR 主要落在文档/示例 `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #44256 - [Fix] glm5.2: Align PD HiSparse prefill KV layout

- 链接: https://github.com/sgl-project/sglang/pull/44256
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；关联提交 `7b53a134016c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-4，可读 patch 29 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] glm5.2: Align PD HiSparse prefill KV layout」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；技术摘要: 覆盖「[Fix] glm5.2: Align PD HiSparse prefill KV layout」；主要实现面是 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +6/-4 (10 lines); hunks: -14,14 +14,11; -53,7 +50,12 @@ class TestGLM52PDHiSparseSpec(PDDisaggregationServerBase, GSM...; symbols: TestGLM52PDHiSparseSpec，涉及 `TestGLM52PDHiSparseSpec`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +6/-4 (10 lines); hunks: -14,14 +14,11; -53,7 +50,12 @@ class TestGLM52PDHiSparseSpec(PDDisaggregationServerBase, GSM...; symbols: TestGLM52PDHiSparseSpec
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_dsa_glm52_hisparse.py
@@ -14,14 +14,11 @@
-    disabled="Temporarily disabled: NaN in EAGLE verify target logits on B300.",
-# Also skip selective reruns, which bypass the registry's disabled marker.
-@unittest.skip("Temporarily disabled: NaN in EAGLE verify target logits on B300")
@@ -53,7 +50,12 @@ class TestGLM52PDHiSparseSpec(PDDisaggregationServerBase, GSM8KMixin):
-    extra_prefill_args = common_args
+    # PD transfers KV bytes without converting layouts. Match FlashMLA decode's
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +6/-4
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44303 - [Fix] glm5.2: Align HiSparse warmup backends and move test to nightly

- 链接: https://github.com/sgl-project/sglang/pull/44303
- 状态/时间: merged / 2026-10-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；关联提交 `b67785153a55`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-3，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] glm5.2: Align HiSparse warmup backends and move test to nightly」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；技术摘要: 覆盖「[Fix] glm5.2: Align HiSparse warmup backends and move test to nightly」；主要实现面是 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +6/-3 (9 lines); hunks: -12,8 +12,8; -22,7 +22,7; symbols: TestGLM52PDHiSparseSpec，涉及 `TestGLM52PDHiSparseSpec`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +6/-3 (9 lines); hunks: -12,8 +12,8; -22,7 +22,7; symbols: TestGLM52PDHiSparseSpec
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_dsa_glm52_hisparse.py
@@ -12,8 +12,8 @@
-    stage="extra-b",
-    runner_config="8-gpu-b300",
+    stage="nightly",
+    runner_config="8-gpu-b200",
@@ -22,7 +22,7 @@
-    # Match the existing GLM-5.2 PD test: NVFP4 fits TP4 + TP4 on eight B300s.
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +6/-3
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44093 - [Fix] glm5_next: Correct num_experts_per_tok default to 8

- 链接: https://github.com/sgl-project/sglang/pull/44093
- 状态/时间: merged / 2026-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/configs/glm5_next.py`；关联提交 `c4870d98cfef`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] glm5_next: Correct num_experts_per_tok default to 8」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `python/sglang/srt/configs/glm5_next.py`；技术摘要: 覆盖「[Fix] glm5_next: Correct num_experts_per_tok default to 8」；主要实现面是 `python/sglang/srt/configs/glm5_next.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/configs/glm5_next.py` modified +1/-1 (2 lines); hunks: -104,7 +104,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/configs/glm5_next.py` modified +1/-1 (2 lines); hunks: -104,7 +104,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/configs/glm5_next.py
@@ -104,7 +104,7 @@ def __init__(
-        num_experts_per_tok: int = 7,
+        num_experts_per_tok: int = 8,
```

- 已读文件:
  - runtime: `python/sglang/srt/configs/glm5_next.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/glm5_next.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #44597 - [CI] glm5.2: Keep EOS in HiSparse needle test output

- 链接: https://github.com/sgl-project/sglang/pull/44597
- 状态/时间: merged / 2026-10-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；关联提交 `4fc86f73c224`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] glm5.2: Keep EOS in HiSparse needle test output」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；技术摘要: 覆盖「[CI] glm5.2: Keep EOS in HiSparse needle test output」；主要实现面是 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +1/-0 (1 lines); hunks: -147,6 +147,7 @@ def _test_long_context_spec_swap(self, temperature):; symbols: _test_long_context_spec_swap，涉及 `_test_long_context_spec_swap`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +1/-0 (1 lines); hunks: -147,6 +147,7 @@ def _test_long_context_spec_swap(self, temperature):; symbols: _test_long_context_spec_swap
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_dsa_glm52_hisparse.py
@@ -147,6 +147,7 @@ def _test_long_context_spec_swap(self, temperature):
+                    "skip_special_tokens": False,
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_dsa_glm52_hisparse.py` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/e2e/models/test_dsa_glm52_hisparse.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #44892 - [Fix] [H200] ci: Split GLM-5.3-Flash serving recipes into separate tests

- 链接: https://github.com/sgl-project/sglang/pull/44892
- 状态/时间: merged / 2026-10-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/test/glm53_flash_common.py`, `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py`, `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py`；关联提交 `8dee3f6bdb29`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+132/-121，可读 patch 257 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] [H200] ci: Split GLM-5.3-Flash serving recipes into separate tests」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py`, `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py`, `python/sglang/test/glm53_flash_common.py`；技术摘要: 覆盖「[Fix] [H200] ci: Split GLM-5.3-Flash serving recipes into separate tests」；主要实现面是 `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py`, `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py`, `python/sglang/test/glm53_flash_common.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py` added +42/-0 (42 lines); hunks: -0,0 +1,42; symbols: TestGLM53FlashH200LowLatency，涉及 `TestGLM53FlashH200LowLatency`；`test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py` added +33/-0 (33 lines); hunks: -0,0 +1,33; symbols: TestGLM53FlashH200HighThroughput，涉及 `TestGLM53FlashH200HighThroughput`；`python/sglang/test/glm53_flash_common.py` added +57/-0 (57 lines); hunks: -0,0 +1,57; symbols: _stop_server, _GLM53FlashH200Base, setUpClass, tearDownClass，涉及 `_stop_server, _GLM53FlashH200Base, setUpClass`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py` added +42/-0 (42 lines); hunks: -0,0 +1,42; symbols: TestGLM53FlashH200LowLatency
  - `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py` added +33/-0 (33 lines); hunks: -0,0 +1,33; symbols: TestGLM53FlashH200HighThroughput
  - `python/sglang/test/glm53_flash_common.py` added +57/-0 (57 lines); hunks: -0,0 +1,57; symbols: _stop_server, _GLM53FlashH200Base, setUpClass, tearDownClass
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_glm53_flash_h200_low_latency.py
@@ -0,0 +1,42 @@
+"""H200 per-commit coverage for the GLM-5.3-Flash low latency recipe."""
+import unittest
+from sglang.test.ci.ci_register import register_cuda_ci
+from sglang.test.glm53_flash_common import COMMON_SERVER_ARGS, _GLM53FlashH200Base
+from sglang.test.kits.eval_accuracy_kit import GSM8KMixin
+from sglang.test.kits.spec_decoding_kit import SpecDecodingMixin
diff -- test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py
@@ -0,0 +1,33 @@
+"""H200 per-commit coverage for the GLM-5.3-Flash high throughput recipe."""
+import unittest
+from sglang.test.ci.ci_register import register_cuda_ci
+from sglang.test.glm53_flash_common import COMMON_SERVER_ARGS, _GLM53FlashH200Base
+from sglang.test.kits.eval_accuracy_kit import GSM8KMixin
+register_cuda_ci(est_time=1200, stage="extra-b", runner_config="8-gpu-h200")
diff -- python/sglang/test/glm53_flash_common.py
@@ -0,0 +1,57 @@
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py` added +42/-0; `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py` added +33/-0; `python/sglang/test/glm53_flash_common.py` added +57/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/glm53_flash_common.py`, `test/registered/e2e/models/test_glm53_flash_h200.py`, `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py`, `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45154 - [Feat] glm-5.3: Render GLM-5.3 and GLM-5.3-Flash chat prompts with a Python chat template

- 链接: https://github.com/sgl-project/sglang/pull/45154
- 状态/时间: merged / 2026-10-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/parser/glm53_chat_template.py`, `test/registered/unit/parser/test_glm53_chat_template.py`；关联提交 `ca473ef3e437`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+1438/-6，可读 patch 1554 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] glm-5.3: Render GLM-5.3 and GLM-5.3-Flash chat prompts with a Python chat template」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `test/registered/unit/parser/test_glm53_chat_template.py`, `python/sglang/srt/parser/glm53_chat_template.py`；技术摘要: 覆盖「[Feat] glm-5.3: Render GLM-5.3 and GLM-5.3-Flash chat prompts with a Python chat template」；主要实现面是 `test/registered/unit/parser/test_glm53_chat_template.py`, `python/sglang/srt/parser/glm53_chat_template.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/unit/parser/test_glm53_chat_template.py` added +645/-0 (645 lines); hunks: -0,0 +1,645; symbols: _render, _glm53_like_template, _hf_config, _tiny_tokenizer，涉及 `_render, _glm53_like_template, _hf_config`；`python/sglang/srt/parser/glm53_chat_template.py` added +438/-0 (438 lines); hunks: -0,0 +1,438; symbols: _get, _first, _string, _is_iterable，涉及 `_get, _first, _string`。
- 代码 diff 细节:
  - `test/registered/unit/parser/test_glm53_chat_template.py` added +645/-0 (645 lines); hunks: -0,0 +1,645; symbols: _render, _glm53_like_template, _hf_config, _tiny_tokenizer
  - `python/sglang/srt/parser/glm53_chat_template.py` added +438/-0 (438 lines); hunks: -0,0 +1,438; symbols: _get, _first, _string, _is_iterable
- 关键代码摘录:

```diff
diff -- test/registered/unit/parser/test_glm53_chat_template.py
@@ -0,0 +1,645 @@
+"""GLM-5.3 / GLM-5.3-Flash Python chat templates.
+The expected prompts below were rendered with the checkpoints' chat_template.jinja.
+Set SGLANG_TEST_GLM53_CHECKPOINT / SGLANG_TEST_GLM53_FLASH_CHECKPOINT to model
+directories to also compare against their Jinja templates directly.
+"""
+import inspect
diff -- python/sglang/srt/parser/glm53_chat_template.py
@@ -0,0 +1,438 @@
+# Adapted from the GLM-5.3 / GLM-5.3-Flash reference chat_template.py by Z.ai.
+"""Python version of the GLM-5.3 and GLM-5.3-Flash chat templates.
+The two templates are the same apart from the multimodal block, so a single
+renderer serves both. The output is byte-identical to the Jinja templates.
+Where a template fails on malformed input, the renderer fails at the same
+point, raising ``ValueError`` for Jinja's ``UndefinedError`` and the very
```

- 已读文件:
  - tests: `test/registered/unit/parser/test_glm53_chat_template.py` added +645/-0
  - runtime: `python/sglang/srt/parser/glm53_chat_template.py` added +438/-0
- 验证与风险: diff 自带测试面 `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/entrypoints/openai/utils.py`, `test/registered/unit/parser/test_glm53_chat_template.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45326 - [Doc] cookbook: add TPU7x recipe for GLM-5.3-Flash

- 链接: https://github.com/sgl-project/sglang/pull/45326
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；关联提交 `c1c287a42928`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+155/-17，可读 patch 334 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: add TPU7x recipe for GLM-5.3-Flash」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`；技术摘要: 覆盖「[Doc] cookbook: add TPU7x recipe for GLM-5.3-Flash」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +118/-15 (133 lines); hunks: -1,15 +1,24; -41,6 +50,7 @@ export const config = {；`docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +21/-0 (21 lines); hunks: -210,6 +210,27 @@ export const benchmarks = [；`docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +16/-2 (18 lines); hunks: -1,6 +1,6; -20,14 +20,24 @@ For the listed NVIDIA hardware, the deployment panel can ren...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +118/-15 (133 lines); hunks: -1,15 +1,24; -41,6 +50,7 @@ export const config = {
  - `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +21/-0 (21 lines); hunks: -210,6 +210,27 @@ export const benchmarks = [
  - `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +16/-2 (18 lines); hunks: -1,6 +1,6; -20,14 +20,24 @@ For the listed NVIDIA hardware, the deployment panel can ren...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx
@@ -1,15 +1,24 @@
-  supportedHardware: ["b300", "gb300", "h100", "h200", "b200", "gb200", "mi355x"],
+  supportedHardware: ["b300", "gb300", "h100", "h200", "b200", "gb200", "mi355x", "tpu7x"],
+  // One TPU7x (Ironwood) host: 4 chips, 8 TensorCores, served by sglang-torchtpu.
+  hardware: [{ id: "tpu7x", label: "TPU7x", vram: "192GB", vendor: "tpu" }],
-        { id: "high-throughput", label: "High Throughput", subtitle: "Spec decode off" },
+        {
diff -- docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx
@@ -210,6 +210,27 @@ export const benchmarks = [
+  {
+    match: { hw: "tpu7x", strategy: "low-latency", quant: "fp8" },
+    sglang_version: "sglang-torchtpu 46a6f50291",
+    latencyPercentile: "P50",
+    speed: [
+      {
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx
@@ -1,6 +1,6 @@
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` modified +118/-15; `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx` modified +21/-0; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` modified +16/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #45513 - [Doc] cookbook: Add GLM-5.3 AgentX section and refresh with eight open InferenceX PRs

- 链接: https://github.com/sgl-project/sglang/pull/45513
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `docs/src/snippets/agentx/zai-org/glm-5.3.jsx`；关联提交 `1689cb2d5262`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+2698/-1040，可读 patch 1739 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: Add GLM-5.3 AgentX section and refresh with eight open InferenceX PRs」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/agentx/zai-org/glm-5.3.jsx`, `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`；技术摘要: 覆盖「[Doc] cookbook: Add GLM-5.3 AgentX section and refresh with eight open InferenceX PRs」；主要实现面是 `docs/src/snippets/agentx/zai-org/glm-5.3.jsx`, `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/agentx/zai-org/glm-5.3.jsx` added +450/-0 (450 lines); hunks: -0,0 +1,450；`docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +71/-49 (120 lines); hunks: -1,37 +1,52; -226,18 +241,20 @@ export const agentx = {；`docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +14/-1 (15 lines); hunks: -50,7 +50,7 @@ import { Deployment } from "/src/snippets/_deployment.jsx";; -64,6 +64,19 @@ import { Playground } from "/src/snippets/_playground.jsx";。
- 代码 diff 细节:
  - `docs/src/snippets/agentx/zai-org/glm-5.3.jsx` added +450/-0 (450 lines); hunks: -0,0 +1,450
  - `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +71/-49 (120 lines); hunks: -1,37 +1,52; -226,18 +241,20 @@ export const agentx = {
  - `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +14/-1 (15 lines); hunks: -50,7 +50,7 @@ import { Deployment } from "/src/snippets/_deployment.jsx";; -64,6 +64,19 @@ import { Playground } from "/src/snippets/_playground.jsx";
- 关键代码摘录:

```diff
diff -- docs/src/snippets/agentx/zai-org/glm-5.3.jsx
@@ -0,0 +1,450 @@
+// GENERATED by the sa-infx-cookbook sync scripts — do not edit by hand.
+// Launch commands mirrored from SemiAnalysis InferenceX AgentX submissions
+// (SemiAnalysisAI/InferenceX main@6046414d2d1a plus open PRs #3930, #4333, #4341, #4342, #4343, #4344, #4346, #4350), with SA-specific settings removed.
+export const agentx = {
+ "model": "GLM-5.3",
+ "generatedOn": "2026-10-20",
diff -- docs/src/snippets/agentx/zai-org/glm-5.2.jsx
@@ -1,37 +1,52 @@
-// (SemiAnalysisAI/InferenceX main@660b5a8dbda9 plus open PRs #3817, #4300, #4327, #4333, #4334), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@6046414d2d1a plus open PRs #3930, #4333, #4341, #4342, #4343, #4344, #4346, #4350), with SA-specific settings removed.
- "generatedOn": "2026-10-19",
+ "generatedOn": "2026-10-20",
-  "main": "660b5a8dbda948f1042f1f11da354b2d2a39e169",
+  "main": "6046414d2d1ad2fb17aa857f01fd3146f429b4fc",
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3.mdx
@@ -50,7 +50,7 @@ import { Deployment } from "/src/snippets/_deployment.jsx";
```

- 已读文件:
  - docs: `docs/src/snippets/agentx/zai-org/glm-5.3.jsx` added +450/-0; `docs/src/snippets/agentx/zai-org/glm-5.2.jsx` modified +71/-49; `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +14/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #43774 - [Feat] glm5.3flash: Support padded CP BCG and prefix replay with PD/DFlash2

- 链接: https://github.com/sgl-project/sglang/pull/43774
- 状态/时间: merged / 2026-10-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py`, `test/registered/e2e/models/test_glm53_flash_b200.py`；关联提交 `ea226cf78267`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 17 个文件，+398/-195，可读 patch 821 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] glm5.3flash: Support padded CP BCG and prefix replay with PD/DFlash2」；模型线: GLM-5/5.1；类别: 缺陷修复；主要 diff: `test/registered/e2e/models/test_glm53_flash_b200.py`, `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py`；技术摘要: 覆盖「[Feat] glm5.3flash: Support padded CP BCG and prefix replay with PD/DFlash2」；主要实现面是 `test/registered/e2e/models/test_glm53_flash_b200.py`, `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +1/-25 (26 lines); hunks: -1,6 +1,6; -22,7 +22,6; symbols: TestGLM53FlashB200HighThroughput, TestGLM53FlashB200DFlash2，涉及 `TestGLM53FlashB200HighThroughput, TestGLM53FlashB200DFlash2`；`test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py` added +223/-0 (223 lines); hunks: -0,0 +1,223; symbols: TestGlm53CpBcgDflashPD, setUpClass, launch_lb, _prompt，涉及 `TestGlm53CpBcgDflashPD, setUpClass, launch_lb`。
- 代码 diff 细节:
  - `test/registered/e2e/models/test_glm53_flash_b200.py` modified +1/-25 (26 lines); hunks: -1,6 +1,6; -22,7 +22,6; symbols: TestGLM53FlashB200HighThroughput, TestGLM53FlashB200DFlash2
  - `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py` added +223/-0 (223 lines); hunks: -0,0 +1,223; symbols: TestGlm53CpBcgDflashPD, setUpClass, launch_lb, _prompt
- 关键代码摘录:

```diff
diff -- test/registered/e2e/models/test_glm53_flash_b200.py
@@ -1,6 +1,6 @@
-Runs the Low Latency, DFlash2, and High Throughput TP4 recipes on four B200
+Runs the Low Latency and High Throughput TP4 recipes on four B200
@@ -22,7 +22,6 @@
-DFLASH2_DRAFT_MODEL_PATH = "incoai/GLM-5.3-Flash-DFlash2"
@@ -118,28 +117,5 @@ class TestGLM53FlashB200HighThroughput(
-class TestGLM53FlashB200DFlash2(
diff -- test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py
@@ -0,0 +1,223 @@
+"""GLM CP4/BCG prefill -> TP4 DFlash2 decode, with padding and cached prefixes."""
+import unittest
+import requests
+from transformers import AutoTokenizer
+from sglang.test.ci.ci_register import register_cuda_ci
+from sglang.test.kits.eval_accuracy_kit import GSM8KMixin
```

- 已读文件:
  - tests: `test/registered/e2e/models/test_glm53_flash_b200.py` modified +1/-25; `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py` added +223/-0
- 验证与风险: diff 自带测试面 `test/registered/cp/test_cp_strategy_unit.py`, `test/registered/cp/test_glm53_flash_cp.py`, `test/registered/e2e/disaggregation/test_glm53_cp_bcg_dflash.py`, `test/registered/e2e/models/test_glm53_flash_b200.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45642 - [Doc] [NPU] cookbook: add A3 deployment scenarios to GLM-5.2

- 链接: https://github.com/sgl-project/sglang/pull/45642
- 状态/时间: merged / 2026-10-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `d1bbcbdc0db5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+17/-4，可读 patch 51 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] [NPU] cookbook: add A3 deployment scenarios to GLM-5.2」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Doc] [NPU] cookbook: add A3 deployment scenarios to GLM-5.2」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +2/-2 (4 lines); hunks: -101,7 +101,7 @@ sgl-eval run aime25 \\; -291,7 +291,7 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +15/-2 (17 lines); hunks: -49,10 +49,10 @@ Use a Linux host with the Ascend driver and a compatible CAN...; -188,6 +188,19 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5....。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +2/-2 (4 lines); hunks: -101,7 +101,7 @@ sgl-eval run aime25 \\; -291,7 +291,7 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +15/-2 (17 lines); hunks: -49,10 +49,10 @@ Use a Linux host with the Ascend driver and a compatible CAN...; -188,6 +188,19 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5....
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -101,7 +101,7 @@ sgl-eval run aime25 \\
-    a3: "quay.io/ascend/sglang:cann9.0.0-a3-v0.5.16",
+    a3: "quay.io/ascend/sglang:v0.5.22-cann9.1.0-a3",
@@ -291,7 +291,7 @@ sgl-eval run aime25 \\
-      commands: { python: router.command, docker: `docker run --network host --rm ${s.hw === "a5" ? "<your-compatible-950pr-dt-series-image>" : "quay.io/ascend/sglang:cann9.0.0-a3
+      commands: { python: router.command, docker: `docker run --network host --rm ${s.hw === "a5" ? "<your-compatible-950pr-dt-series-image>" : "quay.io/ascend/sglang:v0.5.22-cann
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -49,10 +49,10 @@ Use a Linux host with the Ascend driver and a compatible CANN / TorchNPU environ
-docker pull quay.io/ascend/sglang:cann9.0.0-a3-v0.5.16
+docker pull quay.io/ascend/sglang:v0.5.22-cann9.1.0-a3
-Run the following setup before copying the generated command (CANN 9.0.0). CPU tuning requires host privileges.
+Run the following setup before copying the generated command (CANN 9.1.0). CPU tuning requires host privileges.
@@ -188,6 +188,19 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.2.jsx";
+- **Ascend NPU (A3 Series) topology.** One A3 node is 8 cards x 2 dies = **16 devices**, so every A3 recipe runs `--tp-size 16` per node. **Single Node** is PD mixed on one node;
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +2/-2; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +15/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #46825 - [Doc] [AMD] cookbook: Add GLM-5.3 MI355X AgentX recipe

- 链接: https://github.com/sgl-project/sglang/pull/46825
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`；关联提交 `f854e3df13cd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+64/-1，可读 patch 79 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] [AMD] cookbook: Add GLM-5.3 MI355X AgentX recipe」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`；技术摘要: 覆盖「[Doc] [AMD] cookbook: Add GLM-5.3 MI355X AgentX recipe」；主要实现面是 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +64/-1 (65 lines); hunks: -131,6 +131,69 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5....; -178,7 +241,7 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.3...。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +64/-1 (65 lines); hunks: -131,6 +131,69 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5....; -178,7 +241,7 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.3...
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/GLM/GLM-5.3.mdx
@@ -131,6 +131,69 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.3.jsx";
+### MI355X deployment measured with SemiAnalysis InferenceX
+MXFP4 checkpoint with EAGLE MTP on MI355X, benchmarked in [SemiAnalysis InferenceX](https://inferencex.semianalysis.com/) ([InferenceX #4593](https://github.com/SemiAnalysisAI/Inf
+- **Container image.** `lmsysorg/sglang-rocm:v0.5.22-rocm10-mi35x-20261025` (`sha256:bb3370918fb7fc4adce40d4192e61ad7dbccbc8159e2f6063318120d0bc0e949`, the image tested in Inferen
+- **Batch limits.** Set `--max-running-requests` and `--cuda-graph-max-bs-decode` to twice the concurrency. The commands below use concurrency 10 for TP4·EP4 and 4 for TP8·EP1.
+- **HiCache.** `--hicache-size` is the host tier in GB per rank, so 180 GB needs about 720 GB of host memory across the four ranks.
+'''bash TP4·EP4 (concurrency 4–16)
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` modified +64/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #47331 - [Doc] [AMD] cookbook: Add DCP4 to the GLM-5.2 MI355X MXFP4 high-throughput recipe

- 链接: https://github.com/sgl-project/sglang/pull/47331
- 状态/时间: merged / 2026-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；关联提交 `56280587141d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+7/-7，可读 patch 49 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] [AMD] cookbook: Add DCP4 to the GLM-5.2 MI355X MXFP4 high-throughput recipe」；模型线: GLM-5/5.1；类别: 性能/后端优化；主要 diff: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Doc] [AMD] cookbook: Add DCP4 to the GLM-5.2 MI355X MXFP4 high-throughput recipe」；主要实现面是 `docs/src/snippets/configs/zai-org/glm-5.2.jsx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +6/-6 (12 lines); hunks: -107,7 +107,7 @@ sgl-eval run aime25 \\; -1269,9 +1269,9 @@ sgl-eval run aime25 \\；`docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -186,7 +186,7 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.2...。
- 代码 diff 细节:
  - `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +6/-6 (12 lines); hunks: -107,7 +107,7 @@ sgl-eval run aime25 \\; -1269,9 +1269,9 @@ sgl-eval run aime25 \\
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1 (2 lines); hunks: -186,7 +186,7 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.2...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/configs/zai-org/glm-5.2.jsx
@@ -107,7 +107,7 @@ sgl-eval run aime25 \\
-    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260923",
+    "mi355x|mxfp4": "lmsysorg/sglang-rocm:v0.5.22-rocm720-mi35x-20261028",
@@ -1269,9 +1269,9 @@ sgl-eval run aime25 \\
-    // newer image (v0.5.20, see dockerImages["mi355x|mxfp4"]) than the FP8/BF16
-    // mi355x cells. Low-Latency uses validated TP8/EP1; High-Throughput uses
-    // validated TP4/EP4. Both use five-step MTP from InferenceX PR #2900.
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -186,7 +186,7 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.2.jsx";
-- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.20-rocm720-mi35x-20260930`. Choose **Lo
+- **MTP / EAGLE speculative decoding on AMD.** Five-step MTP is validated for `amd/GLM-5.2-MXFP4` on MI355X with `lmsysorg/sglang-rocm:v0.5.22-rocm720-mi35x-20261028`. Choose **Lo
```

- 已读文件:
  - docs: `docs/src/snippets/configs/zai-org/glm-5.2.jsx` modified +6/-6; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #47615 - [Doc] [AMD] cookbook: Add GLM-5.2 MI355X AgentX recipe

- 链接: https://github.com/sgl-project/sglang/pull/47615
- 状态/时间: merged / 2026-10-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；关联提交 `2e80af28577d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+90/-0，可读 patch 97 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] [AMD] cookbook: Add GLM-5.2 MI355X AgentX recipe」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；技术摘要: 覆盖「[Doc] [AMD] cookbook: Add GLM-5.2 MI355X AgentX recipe」；主要实现面是 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +90/-0 (90 lines); hunks: -129,6 +129,96 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5....。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +90/-0 (90 lines); hunks: -129,6 +129,96 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5....
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/GLM/GLM-5.2.mdx
@@ -129,6 +129,96 @@ import { agentx } from "/src/snippets/agentx/zai-org/glm-5.2.jsx";
+### MI355X deployment measured with SemiAnalysis InferenceX
+MXFP4 checkpoint with EAGLE MTP on MI355X, benchmarked in [SemiAnalysis InferenceX](https://inferencex.semianalysis.com/) ([InferenceX #4064](https://github.com/SemiAnalysisAI/Inf
+Image: `lmsysorg/sglang-rocm:v0.5.22-rocm720-mi35x-20261028` (`sha256:2456fff6cfaffb822026d089a0629a4859c84d2448864ffd6d5fa4f945ef2c86`). Set `--max-running-requests` to twice the
+These commands match the InferenceX runs; the Deploy panel cells above are general-purpose starting points.
+'''bash TP8·EP1 (concurrency 1–4)
+SGLANG_OPT_USE_TOPK_V2=true \
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx` modified +90/-0
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #47611 - [Test] [Ascend] npu: Add GLM-5.2 2P2D gpqa cases and unify evalscope retry loop

- 链接: https://github.com/sgl-project/sglang/pull/47611
- 状态/时间: merged / 2026-11-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py`；关联提交 `e1e0f4ab8cc3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+554/-102，可读 patch 711 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Test] [Ascend] npu: Add GLM-5.2 2P2D gpqa cases and unify evalscope retry loop」；模型线: GLM-5/5.1；类别: 文档/测试/CI；主要 diff: `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py`；技术摘要: 覆盖「[Test] [Ascend] npu: Add GLM-5.2 2P2D gpqa cases and unify evalscope retry loop」；主要实现面是 `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py` added +239/-0 (239 lines); hunks: -0,0 +1,239; symbols: TestNPUGLM5_2_W8A8_2P2D_PCP_GPQA, test_npu_glm_5_2_w8a8_2p2d_pcp_gpqa，涉及 `TestNPUGLM5_2_W8A8_2P2D_PCP_GPQA, test_npu_glm_5_2_w8a8_2p2d_pcp_gpqa`；`test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py` added +230/-0 (230 lines); hunks: -0,0 +1,230; symbols: TestNPUGLM5_2_W8A8_2P2D_DCP_GPQA, test_npu_glm_5_2_w8a8_2p2d_dcp_gpqa，涉及 `TestNPUGLM5_2_W8A8_2P2D_DCP_GPQA, test_npu_glm_5_2_w8a8_2p2d_dcp_gpqa`。
- 代码 diff 细节:
  - `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py` added +239/-0 (239 lines); hunks: -0,0 +1,239; symbols: TestNPUGLM5_2_W8A8_2P2D_PCP_GPQA, test_npu_glm_5_2_w8a8_2p2d_pcp_gpqa
  - `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py` added +230/-0 (230 lines); hunks: -0,0 +1,230; symbols: TestNPUGLM5_2_W8A8_2P2D_DCP_GPQA, test_npu_glm_5_2_w8a8_2p2d_dcp_gpqa
- 关键代码摘录:

```diff
diff -- test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py
@@ -0,0 +1,239 @@
+import unittest
+from sglang.test.ascend.e2e.test_npu_accuracy_utils import (
+    TestNpuAccuracyMultiNodePdSepTestCaseBase,
+)
+from sglang.test.ascend.e2e.test_npu_multi_node_utils import NIC_NAME
+from sglang.test.ascend.e2e.test_npu_performance_utils import (
diff -- test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py
@@ -0,0 +1,230 @@
+import unittest
+from sglang.test.ascend.e2e.test_npu_accuracy_utils import (
+    TestNpuAccuracyMultiNodePdSepTestCaseBase,
+)
+from sglang.test.ascend.e2e.test_npu_multi_node_utils import NIC_NAME
+from sglang.test.ascend.e2e.test_npu_performance_utils import (
```

- 已读文件:
  - tests: `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py` added +239/-0; `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py` added +230/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
