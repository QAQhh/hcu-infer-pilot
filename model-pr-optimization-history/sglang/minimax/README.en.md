# sglang MiniMax M2 Series Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx` | [#40120](https://github.com/sgl-project/sglang/pull/40120) |
| `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.7.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` | [#45924](https://github.com/sgl-project/sglang/pull/45924), [#46506](https://github.com/sgl-project/sglang/pull/46506), [#46546](https://github.com/sgl-project/sglang/pull/46546), [#47844](https://github.com/sgl-project/sglang/pull/47844) |
| `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` | [#31446](https://github.com/sgl-project/sglang/pull/31446), [#45924](https://github.com/sgl-project/sglang/pull/45924), [#47187](https://github.com/sgl-project/sglang/pull/47187) |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/minimax_m2_5.mdx` | no direct PR-number commit |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/minimax_m2_5.mdx` | no direct PR-number commit |
| `docs/scripts/tests/minimax-m25-deployment.test.mjs` | [#40120](https://github.com/sgl-project/sglang/pull/40120) |
| `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` | [#46506](https://github.com/sgl-project/sglang/pull/46506), [#46547](https://github.com/sgl-project/sglang/pull/46547), [#47303](https://github.com/sgl-project/sglang/pull/47303), [#47623](https://github.com/sgl-project/sglang/pull/47623), [#47699](https://github.com/sgl-project/sglang/pull/47699), [#47791](https://github.com/sgl-project/sglang/pull/47791), [#48070](https://github.com/sgl-project/sglang/pull/48070) |
| `docs/src/snippets/autoregressive/minimax-m2-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx` | [#40120](https://github.com/sgl-project/sglang/pull/40120) |
| `docs/src/snippets/autoregressive/minimax-m27-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx` | [#35839](https://github.com/sgl-project/sglang/pull/35839), [#47587](https://github.com/sgl-project/sglang/pull/47587) |
| `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx` | [#47187](https://github.com/sgl-project/sglang/pull/47187) |
| `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` | [#45924](https://github.com/sgl-project/sglang/pull/45924), [#46546](https://github.com/sgl-project/sglang/pull/46546), [#47844](https://github.com/sgl-project/sglang/pull/47844) |
| `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx` | [#47187](https://github.com/sgl-project/sglang/pull/47187) |
| `python/sglang/kernels/jit/csrc/minimax/fused_gemma_qknorm_rope.cuh` | [#29630](https://github.com/sgl-project/sglang/pull/29630) |
| `python/sglang/kernels/jit/csrc/minimax/fused_store_kv_index.cuh` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#46135](https://github.com/sgl-project/sglang/pull/46135) |
| `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#36560](https://github.com/sgl-project/sglang/pull/36560), [#38615](https://github.com/sgl-project/sglang/pull/38615), [#45174](https://github.com/sgl-project/sglang/pull/45174) |
| `python/sglang/kernels/jit/csrc/minimax/msa_v1/attn/dequant.cuh` | no direct PR-number commit |
| `python/sglang/kernels/jit/csrc/minimax/nvfp4_store_kv_index.cuh` | no direct PR-number commit |
| `python/sglang/kernels/jit/csrc/minimax/per_token_quant_ue8m0.cuh` | [#29630](https://github.com/sgl-project/sglang/pull/29630) |
| `python/sglang/kernels/ops/activation/minimax_m3_swiglu.py` | no direct PR-number commit |
| `python/sglang/kernels/ops/attention/minimax_decode_topk.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#36560](https://github.com/sgl-project/sglang/pull/36560), [#38615](https://github.com/sgl-project/sglang/pull/38615) |
| `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#36549](https://github.com/sgl-project/sglang/pull/36549), [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_qknorm_rope.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630) |
| `python/sglang/kernels/ops/attention/minimax_sparse/__init__.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793) |
| `python/sglang/kernels/ops/attention/minimax_sparse/common/index.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793) |
| `python/sglang/kernels/ops/attention/minimax_sparse/common/nvfp4.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/common/nvfp4_gfx950.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/common/out_quant_gfx950.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/common/tile_ptr.py` | [#46135](https://github.com/sgl-project/sglang/pull/46135) |
| `python/sglang/kernels/ops/attention/minimax_sparse/common/utils.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793), [#30971](https://github.com/sgl-project/sglang/pull/30971) |
| `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#36527](https://github.com/sgl-project/sglang/pull/36527), [#36560](https://github.com/sgl-project/sglang/pull/36560), [#38615](https://github.com/sgl-project/sglang/pull/38615), [#42772](https://github.com/sgl-project/sglang/pull/42772), [#46135](https://github.com/sgl-project/sglang/pull/46135), [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py` | [#41488](https://github.com/sgl-project/sglang/pull/41488), [#42614](https://github.com/sgl-project/sglang/pull/42614) |
| `python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#31446](https://github.com/sgl-project/sglang/pull/31446), [#38841](https://github.com/sgl-project/sglang/pull/38841), [#46135](https://github.com/sgl-project/sglang/pull/46135), [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/decode/verify_topk_gfx950.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/decode/verify_topk_idx.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#36546](https://github.com/sgl-project/sglang/pull/36546), [#46135](https://github.com/sgl-project/sglang/pull/46135), [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/prefill/gluon_prefill.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/prefill/gluon_prefill_pair_gfx950.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/prefill/index_topk_gfx950.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/prefill/nvfp4_prefill.py` | [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#31446](https://github.com/sgl-project/sglang/pull/31446), [#36546](https://github.com/sgl-project/sglang/pull/36546), [#46135](https://github.com/sgl-project/sglang/pull/46135) |
| `python/sglang/kernels/ops/kvcache/minimax_store_kv_index.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#46135](https://github.com/sgl-project/sglang/pull/46135) |
| `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py` | [#29630](https://github.com/sgl-project/sglang/pull/29630), [#46691](https://github.com/sgl-project/sglang/pull/46691) |
| `python/sglang/kernels/ops/moe/minimax_quant_ue8m0.py` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/minimax_m2.py` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py` | [#45925](https://github.com/sgl-project/sglang/pull/45925), [#46868](https://github.com/sgl-project/sglang/pull/46868) |
| `python/sglang/srt/configs/minimax_vl.py` | [#28715](https://github.com/sgl-project/sglang/pull/28715), [#46140](https://github.com/sgl-project/sglang/pull/46140) |
| `python/sglang/srt/disaggregation/minimax.py` | [#45925](https://github.com/sgl-project/sglang/pull/45925) |
| `python/sglang/srt/function_call/minimax_m2.py` | [#12129](https://github.com/sgl-project/sglang/pull/12129), [#15538](https://github.com/sgl-project/sglang/pull/15538) |
| `python/sglang/srt/function_call/minimax_m3.py` | [#28715](https://github.com/sgl-project/sglang/pull/28715), [#46133](https://github.com/sgl-project/sglang/pull/46133) |
| `python/sglang/srt/hardware_backend/npu/modules/minimax_m3_processor.py` | [#32941](https://github.com/sgl-project/sglang/pull/32941) |
| `python/sglang/srt/layers/attention/minimax_sparse_backend.py` | [#28715](https://github.com/sgl-project/sglang/pull/28715), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#31446](https://github.com/sgl-project/sglang/pull/31446), [#32941](https://github.com/sgl-project/sglang/pull/32941), [#36527](https://github.com/sgl-project/sglang/pull/36527), [#36546](https://github.com/sgl-project/sglang/pull/36546), [#41488](https://github.com/sgl-project/sglang/pull/41488), [#41497](https://github.com/sgl-project/sglang/pull/41497), [#42614](https://github.com/sgl-project/sglang/pull/42614), [#46868](https://github.com/sgl-project/sglang/pull/46868) |
| `python/sglang/srt/layers/attention/minimax_sparse_nvfp4_backend.py` | no direct PR-number commit |
| `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` | [#41488](https://github.com/sgl-project/sglang/pull/41488), [#42614](https://github.com/sgl-project/sglang/pull/42614) |
| `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` | [#28712](https://github.com/sgl-project/sglang/pull/28712), [#29250](https://github.com/sgl-project/sglang/pull/29250), [#29630](https://github.com/sgl-project/sglang/pull/29630), [#30793](https://github.com/sgl-project/sglang/pull/30793), [#30971](https://github.com/sgl-project/sglang/pull/30971), [#31446](https://github.com/sgl-project/sglang/pull/31446), [#36527](https://github.com/sgl-project/sglang/pull/36527), [#36546](https://github.com/sgl-project/sglang/pull/36546), [#38841](https://github.com/sgl-project/sglang/pull/38841), [#41488](https://github.com/sgl-project/sglang/pull/41488), [#42614](https://github.com/sgl-project/sglang/pull/42614), [#46690](https://github.com/sgl-project/sglang/pull/46690) |
| `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` | [#28712](https://github.com/sgl-project/sglang/pull/28712), [#29250](https://github.com/sgl-project/sglang/pull/29250), [#30971](https://github.com/sgl-project/sglang/pull/30971) |
| `python/sglang/srt/layers/attention/minimax_sparse_ops/msa_plan.py` | no direct PR-number commit |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json` | [#28712](https://github.com/sgl-project/sglang/pull/28712) |
| `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py` | [#46140](https://github.com/sgl-project/sglang/pull/46140) |
| `python/sglang/srt/mem_cache/minimax_m3_nvfp4_pool.py` | no direct PR-number commit |
| `python/sglang/srt/mem_cache/pool_host/minimax_m3_nvfp4.py` | [#45925](https://github.com/sgl-project/sglang/pull/45925) |
| `python/sglang/srt/models/dspark_minimax.py` | [#45925](https://github.com/sgl-project/sglang/pull/45925) |
| `python/sglang/srt/models/minimax_m2.py` | [#12129](https://github.com/sgl-project/sglang/pull/12129), [#12798](https://github.com/sgl-project/sglang/pull/12798), [#13297](https://github.com/sgl-project/sglang/pull/13297), [#13659](https://github.com/sgl-project/sglang/pull/13659), [#13892](https://github.com/sgl-project/sglang/pull/13892), [#14047](https://github.com/sgl-project/sglang/pull/14047), [#14416](https://github.com/sgl-project/sglang/pull/14416), [#16483](https://github.com/sgl-project/sglang/pull/16483), [#18217](https://github.com/sgl-project/sglang/pull/18217), [#19577](https://github.com/sgl-project/sglang/pull/19577), [#19995](https://github.com/sgl-project/sglang/pull/19995), [#20067](https://github.com/sgl-project/sglang/pull/20067), ... (24 total) |
| `python/sglang/srt/models/minimax_m3.py` | [#28715](https://github.com/sgl-project/sglang/pull/28715), [#29630](https://github.com/sgl-project/sglang/pull/29630), [#31989](https://github.com/sgl-project/sglang/pull/31989), [#32099](https://github.com/sgl-project/sglang/pull/32099), [#32941](https://github.com/sgl-project/sglang/pull/32941), [#33962](https://github.com/sgl-project/sglang/pull/33962), [#34542](https://github.com/sgl-project/sglang/pull/34542), [#35357](https://github.com/sgl-project/sglang/pull/35357), [#36557](https://github.com/sgl-project/sglang/pull/36557), [#36576](https://github.com/sgl-project/sglang/pull/36576), [#37254](https://github.com/sgl-project/sglang/pull/37254), [#38841](https://github.com/sgl-project/sglang/pull/38841), ... (14 total) |
| `python/sglang/srt/models/minimax_m3_vl.py` | [#28715](https://github.com/sgl-project/sglang/pull/28715), [#31989](https://github.com/sgl-project/sglang/pull/31989), [#32941](https://github.com/sgl-project/sglang/pull/32941), [#36576](https://github.com/sgl-project/sglang/pull/36576), [#37254](https://github.com/sgl-project/sglang/pull/37254), [#45925](https://github.com/sgl-project/sglang/pull/45925) |
| `python/sglang/srt/models/minimax_vl_common.py` | [#28715](https://github.com/sgl-project/sglang/pull/28715), [#45925](https://github.com/sgl-project/sglang/pull/45925) |
| `python/sglang/srt/multimodal/processors/minimax_m31_media.py` | [#45925](https://github.com/sgl-project/sglang/pull/45925) |
| `python/sglang/srt/multimodal/processors/minimax_m3_vl.py` | [#28715](https://github.com/sgl-project/sglang/pull/28715), [#45925](https://github.com/sgl-project/sglang/pull/45925) |
| `python/sglang/test/kernels/minimax_h3_vae.py` | [#45179](https://github.com/sgl-project/sglang/pull/45179) |
| `test/manual/kernels/attention/test_minimax_msa_fp8_parity.py` | no direct PR-number commit |
| `test/manual/minimax_m3/test_npu_memory_pool.py` | [#32941](https://github.com/sgl-project/sglang/pull/32941) |
| `test/manual/minimax_m3/test_npu_topk.py` | [#32941](https://github.com/sgl-project/sglang/pull/32941) |
| `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py` | [#19443](https://github.com/sgl-project/sglang/pull/19443) |
| `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` | [#22722](https://github.com/sgl-project/sglang/pull/22722), [#34241](https://github.com/sgl-project/sglang/pull/34241) |
| `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py` | [#19443](https://github.com/sgl-project/sglang/pull/19443) |
| `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py` | [#27126](https://github.com/sgl-project/sglang/pull/27126) |
| ... | 53 more files omitted from table; all were used for git tracing. |

## PR Coverage Summary

- Git-traced PRs: 85
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 85
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-10-26 | [#12129](https://github.com/sgl-project/sglang/pull/12129) | merged | Support MiniMax M2 model | `python/sglang/srt/models/minimax_m2.py`, `python/sglang/srt/function_call/minimax_m2.py` |
| 2025-11-08 | [#12798](https://github.com/sgl-project/sglang/pull/12798) | merged | Support capturing aux_hidden_states for minimax m2. | `python/sglang/srt/models/minimax_m2.py` |
| 2025-11-15 | [#13297](https://github.com/sgl-project/sglang/pull/13297) | merged | Fix: add missing get_embed_and_head in MiniMax M2 for Eagle3 | `python/sglang/srt/models/minimax_m2.py` |
| 2025-11-20 | [#13659](https://github.com/sgl-project/sglang/pull/13659) | merged | Super tiny remove unused MiniMaxM2MLP class | `python/sglang/srt/models/minimax_m2.py` |
| 2025-11-26 | [#13892](https://github.com/sgl-project/sglang/pull/13892) | merged | fix: correct usage of minimax-m2 deepep moe forward | `python/sglang/srt/models/minimax_m2.py` |
| 2025-12-02 | [#14047](https://github.com/sgl-project/sglang/pull/14047) | merged | Optimize topk sigmoid in minimax_m2 | `python/sglang/srt/models/minimax_m2.py` |
| 2025-12-23 | [#15538](https://github.com/sgl-project/sglang/pull/15538) | merged | Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs | `python/sglang/srt/function_call/minimax_m2.py` |
| 2025-12-30 | [#14416](https://github.com/sgl-project/sglang/pull/14416) | merged | Fusing RMSNormTP in minimax_m2 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-02-01 | [#16483](https://github.com/sgl-project/sglang/pull/16483) | merged | Optimizing all_reduce in RMSNormTP in minimax_m2 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-02-05 | [#18217](https://github.com/sgl-project/sglang/pull/18217) | merged | [piecewise graph]: support MiniMax-M2 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-02-27 | [#19443](https://github.com/sgl-project/sglang/pull/19443) | merged | [AMD] [MiniMax-M2.5 Day 0] Add MiniMax-M2.5 nightly accuracy test | `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py` |
| 2026-03-02 | [#19577](https://github.com/sgl-project/sglang/pull/19577) | merged | [Feat] add PP Support for minimax-m2 series | `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-18 | [#19995](https://github.com/sgl-project/sglang/pull/19995) | merged | Add packed_modules_mapping for MiniMax-M2 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-18 | [#20870](https://github.com/sgl-project/sglang/pull/20870) | merged | [MiniMax M2] Fix KV cache scale loading | `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-24 | [#20905](https://github.com/sgl-project/sglang/pull/20905) | merged | [NPU][ModelSlim] adapt w2 quant layer for Minimax2.5 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-31 | [#21241](https://github.com/sgl-project/sglang/pull/21241) | merged | [bugfix] Fix rope theta config for MiniMax after transformers v5 update | `python/sglang/srt/models/minimax_m2.py` |
| 2026-04-03 | [#21524](https://github.com/sgl-project/sglang/pull/21524) | merged | [AMD] Add MiniMax-M2.5 nightly perf benchmarks for MI30x and MI35x | `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py` |
| 2026-04-07 | [#20919](https://github.com/sgl-project/sglang/pull/20919) | merged | [NPU] Support dp-attention for MiniMax2.5 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-04-10 | [#20967](https://github.com/sgl-project/sglang/pull/20967) | merged | 【BugFix】fix the bug of minimax_m2.5 model that causes repeated outputs when using tp16 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-04-10 | [#20067](https://github.com/sgl-project/sglang/pull/20067) | merged | MiniMax-M2.5 - Support dp attention, dp reduce scatter, FP4 all gather, AR fusion in prepare_attn | `python/sglang/srt/models/minimax_m2.py` |
| 2026-04-13 | [#20673](https://github.com/sgl-project/sglang/pull/20673) | merged | [Feature][JIT Kernel] Fused TP QK norm For Minimax | `python/sglang/srt/models/minimax_m2.py` |
| 2026-04-14 | [#22722](https://github.com/sgl-project/sglang/pull/22722) | merged | [AMD] Add MiniMax-M2.7 accuracy and performance nightly tests | `python/sglang/srt/models/minimax_m2.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` |
| 2026-04-30 | [#23190](https://github.com/sgl-project/sglang/pull/23190) | merged | [NPU] add split_qkv_tp_rmsnorm_rope ops for minimax2 & fix eagle3 hidden states capture in dp attn mode | `python/sglang/srt/models/minimax_m2.py` |
| 2026-05-28 | [#25061](https://github.com/sgl-project/sglang/pull/25061) | merged | Fix MiniMax-M2.7 on CPU | `python/sglang/srt/models/minimax_m2.py` |
| 2026-06-04 | [#27126](https://github.com/sgl-project/sglang/pull/27126) | merged | [AMD] Add MiniMax-M2.5 TP=4 nightly accuracy test for MI355X | `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py` |
| 2026-06-22 | [#28712](https://github.com/sgl-project/sglang/pull/28712) | merged | [minimax-m3] Split 1/4: sparse attention ops + JIT kernels + config foundation | `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json` |
| 2026-06-26 | [#29250](https://github.com/sgl-project/sglang/pull/29250) | merged | Fix MiniMax MSA fallback when fmha plan is unavailable | `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` |
| 2026-06-27 | [#28713](https://github.com/sgl-project/sglang/pull/28713) | merged | [minimax-m3] Split 2/4: mem-cache / HiCache / sparse KV pool | `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` |
| 2026-06-28 | [#28714](https://github.com/sgl-project/sglang/pull/28714) | merged | [minimax-m3] Split 3/4: disagg K-only index-K transfer | `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py` |
| 2026-07-11 | [#28715](https://github.com/sgl-project/sglang/pull/28715) | merged | [minimax-m3] Split 4/4: model + VL + glue + function-call + fp8 quant + generic infra | `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_vl_common.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py` |
| 2026-07-15 | [#30793](https://github.com/sgl-project/sglang/pull/30793) | merged | [Kernel] Migrate linear-attention, MiniMax-sparse and diffusion kernels to sglang.kernels (RFC #29630, Phase 2.5, 6/7) | `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/__init__.py` |
| 2026-07-26 | [#30613](https://github.com/sgl-project/sglang/pull/30613) | merged | [AMD] Nightly Test Coverage - Minimax-M3-MXFP8 Accuracy Test | `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` |
| 2026-07-30 | [#31989](https://github.com/sgl-project/sglang/pull/31989) | merged | feat: Support nvidia/MiniMax-M3-NVFP4 | `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py` |
| 2026-08-01 | [#30971](https://github.com/sgl-project/sglang/pull/30971) | merged | [minimax-m3] fp8 attention GEMMs on SM100 (fp8_e4m3 KV + trtllm_mha) | `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` |
| 2026-08-04 | [#33402](https://github.com/sgl-project/sglang/pull/33402) | merged | [AMD] Enable block-fp8 + quick INT4 all-reduce in MiniMax-M3 MI35x nightly Test | `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` |
| 2026-08-10 | [#33962](https://github.com/sgl-project/sglang/pull/33962) | merged | enable TRT-LLM for MiniMax M3 by preserving SwiGLU params | `python/sglang/srt/models/minimax_m3.py` |
| 2026-08-13 | [#32941](https://github.com/sgl-project/sglang/pull/32941) | merged | [minimax m3][npu]Adaptation of Minimax M3(w8a8) for NPU platforms [1/2] | `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py` |
| 2026-08-13 | [#31956](https://github.com/sgl-project/sglang/pull/31956) | merged | Optimize MiniMax-M2.7 on CPU | `python/sglang/srt/models/minimax_m2.py` |
| 2026-08-14 | [#34542](https://github.com/sgl-project/sglang/pull/34542) | merged | [MiniMax-M3] Overlap shared and routed experts | `python/sglang/srt/models/minimax_m3.py` |
| 2026-08-18 | [#32099](https://github.com/sgl-project/sglang/pull/32099) | merged | [AMD] MiniMax-M3 : Fuse QKV+index proj for block-fp8 | `python/sglang/srt/models/minimax_m3.py` |
| 2026-08-25 | [#36142](https://github.com/sgl-project/sglang/pull/36142) | merged | [AMD][CI] Add MiniMax-M3-MXFP8 MI35x nightly perf benchmark | `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py` |
| 2026-08-28 | [#35290](https://github.com/sgl-project/sglang/pull/35290) | merged | [XPU] Lazily import tvm_ffi-dependent all_reduce kernel in minimax_m2 | `python/sglang/srt/models/minimax_m2.py` |
| 2026-09-08 | [#36527](https://github.com/sgl-project/sglang/pull/36527) | merged | MiniMax-M3: share the sparse index top-k across layers and reuse the decode top-k buffer | `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` |
| 2026-09-08 | [#36557](https://github.com/sgl-project/sglang/pull/36557) | merged | MiniMax-M3: Triton split-K router GEMV with in-kernel fixup | `python/sglang/srt/models/minimax_m3.py` |
| 2026-09-12 | [#37254](https://github.com/sgl-project/sglang/pull/37254) | merged | [AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj | `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py` |
| 2026-09-17 | [#36576](https://github.com/sgl-project/sglang/pull/36576) | merged | MiniMax-M3: allow shared-experts fusion on ROCm gfx942 and newer | `python/sglang/srt/models/minimax_m3_vl.py`, `python/sglang/srt/models/minimax_m3.py` |
| 2026-09-22 | [#31446](https://github.com/sgl-project/sglang/pull/31446) | merged | [HiSparse] Add MHA hisparse support for MiniMax M3 | `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` |
| 2026-09-23 | [#36546](https://github.com/sgl-project/sglang/pull/36546) | merged | MiniMax-M3: run the sparse prefill main attention through AITER Gluon paged attention | `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` |
| 2026-09-23 | [#36560](https://github.com/sgl-project/sglang/pull/36560) | merged | MiniMax-M3: wave64 histogram-select decode top-k, and raise kMaxNumBlocks for CUDA graphs | `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` |
| 2026-09-24 | [#36549](https://github.com/sgl-project/sglang/pull/36549) | merged | MiniMax-M3: allocate the lightning-indexer K cache in fp8 on gfx95 | `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` |
| 2026-09-25 | [#41198](https://github.com/sgl-project/sglang/pull/41198) | merged | [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit | `python/sglang/srt/models/minimax_m3.py` |
| 2026-10-01 | [#41497](https://github.com/sgl-project/sglang/pull/41497) | merged | [AMD] Fix MiniMax-M3 EAGLE3 verification on ROCm | `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `test/registered/amd/test_minimax_rocm_verify.py` |
| 2026-10-02 | [#41488](https://github.com/sgl-project/sglang/pull/41488) | merged | [AMD] Add opt-in MiniMax-M3 TP4 indexer context partitioning | `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` |
| 2026-10-04 | [#41707](https://github.com/sgl-project/sglang/pull/41707) | merged | [AMD] Use AITER ASM prefill for MiniMax-M3 HD128 attention | `test/registered/amd/test_minimax_hd128_asm_prefill.py` |
| 2026-10-04 | [#35357](https://github.com/sgl-project/sglang/pull/35357) | merged | [AMD] MiniMax-M3: fuse sparse QK norm, RoPE and cache writes with AITER | `python/sglang/srt/models/minimax_m3.py` |
| 2026-10-08 | [#38615](https://github.com/sgl-project/sglang/pull/38615) | merged | [MiniMax-M3] Instantiate the decode block top-k in register buckets | `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py` |
| 2026-10-08 | [#38841](https://github.com/sgl-project/sglang/pull/38841) | merged | [MiniMax-M3] Decode: paged K/V tile loads and a tiny GEMM for the router projection | `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py` |
| 2026-10-09 | [#42772](https://github.com/sgl-project/sglang/pull/42772) | merged | [AMD] Keep MiniMax decode-score tile at 128 tokens off gfx950 | `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` |
| 2026-10-09 | [#43259](https://github.com/sgl-project/sglang/pull/43259) | merged | [AMD] Run the MiniMax indexer CP test on MI35X, not MI300 | `test/registered/amd/test_minimax_indexer_cp.py` |
| 2026-10-09 | [#42614](https://github.com/sgl-project/sglang/pull/42614) | merged | [AMD] MiniMax-M3 indexer CP: packed scoring for EAGLE verify rows | `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` |
| 2026-10-21 | [#40120](https://github.com/sgl-project/sglang/pull/40120) | merged | [Doc] [NPU] cookbook: add tested A2 deployment and A3 reference for MiniMax-M2.5 | `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx`, `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx`, `docs/scripts/tests/minimax-m25-deployment.test.mjs` |
| 2026-10-22 | [#34241](https://github.com/sgl-project/sglang/pull/34241) | merged | [Fix] [AMD] test: Recalibrate MiniMax-M2.7 GSM8K threshold 0.93->0.91 for MI300 runners | `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` |
| 2026-10-23 | [#45924](https://github.com/sgl-project/sglang/pull/45924) | merged | [Doc] Cookbook: add MiniMax-M3.1 | `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` |
| 2026-10-24 | [#45179](https://github.com/sgl-project/sglang/pull/45179) | merged | [Perf] diffusion/minimax-h3: Batch the video VAE decoder tiles and fuse the output chain | `python/sglang/test/kernels/minimax_h3_vae.py` |
| 2026-10-24 | [#46133](https://github.com/sgl-project/sglang/pull/46133) | merged | [Fix] minimax-m3: Type nested tool-call arguments and count self-opened reasoning | `test/registered/unit/function_call/test_minimax_m3_detector.py`, `python/sglang/srt/function_call/minimax_m3.py` |
| 2026-10-25 | [#46135](https://github.com/sgl-project/sglang/pull/46135) | merged | [Perf] minimax-sparse: Speed up MiniMax-M3 sparse attention on Hopper | `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` |
| 2026-10-25 | [#46140](https://github.com/sgl-project/sglang/pull/46140) | merged | [Feat] quantization: Add the MiniMax-M3.1 NVFP4 MoE method | `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py`, `python/sglang/srt/configs/minimax_vl.py`, `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py` |
| 2026-10-26 | [#46506](https://github.com/sgl-project/sglang/pull/46506) | merged | [Doc] cookbook: Add MiniMax-M3.1-Flash AgentX launches and refresh with nine InferenceX PRs | `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` |
| 2026-10-26 | [#46546](https://github.com/sgl-project/sglang/pull/46546) | merged | [Doc] cookbook: MiniMax-M3.1 GB200 recipes and B200 Low-Latency (MonoKernel) | `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` |
| 2026-10-26 | [#46547](https://github.com/sgl-project/sglang/pull/46547) | merged | [Doc] cookbook: Refresh SemiAnalysis AgentX launches with MiniMax-M3.1-Flash B200 / GB200 HiCache points | `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` |
| 2026-10-26 | [#45925](https://github.com/sgl-project/sglang/pull/45925) | merged | [Feat] minimax: Support MiniMax-M3.1-Flash | `python/sglang/srt/multimodal/processors/minimax_m3_vl.py`, `test/registered/unit/multimodal/test_minimax_m31_processor.py`, `test/registered/unit/models/test_minimax_m31_model.py` |
| 2026-10-29 | [#46868](https://github.com/sgl-project/sglang/pull/46868) | merged | [Feat] minimax-m3.1: Support DSpark on Hopper | `test/registered/unit/models/test_minimax_m31_model.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py` |
| 2026-10-29 | [#47303](https://github.com/sgl-project/sglang/pull/47303) | merged | [Doc] cookbook: Add MiniMax-M3.1-Flash B300 TP2 SPF AgentX points | `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` |
| 2026-10-30 | [#46627](https://github.com/sgl-project/sglang/pull/46627) | merged | [Test] minimax-m3.1: Add nightly e2e tests on H200 and B300 | `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py`, `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` |
| 2026-10-31 | [#45174](https://github.com/sgl-project/sglang/pull/45174) | merged | [Fix] Minimax-M3: Deterministic tie-breaking in the CUDA radix decode top-k | `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` |
| 2026-10-31 | [#47623](https://github.com/sgl-project/sglang/pull/47623) | merged | [Doc] cookbook: Update MiniMax-M3.1-Flash AgentX launches | `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` |
| 2026-11-01 | [#47699](https://github.com/sgl-project/sglang/pull/47699) | merged | [Doc] cookbook: Add MiniMax-M3.1-Flash GB300 PD AgentX points | `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` |
| 2026-11-01 | [#47789](https://github.com/sgl-project/sglang/pull/47789) | merged | [CI] nightly: Disable the MiniMax-M3.1-Flash H200 test while it times out | `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` |
| 2026-11-01 | [#46690](https://github.com/sgl-project/sglang/pull/46690) | merged | [Feat] [AMD] minimax: gfx950 sparse attention, NVFP4 KV and DSpark verify kernels | `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py` |
| 2026-11-01 | [#46691](https://github.com/sgl-project/sglang/pull/46691) | merged | [Feat] [AMD] minimax: gfx950 MoE, router GEMV, block-fp8 GEMM and fp8 producer kernels | `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py`, `test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py` |
| 2026-11-02 | [#47791](https://github.com/sgl-project/sglang/pull/47791) | merged | [Doc] cookbook: Sync MiniMax-M3.1-Flash GB300 AgentX points | `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` |
| 2026-11-02 | [#47675](https://github.com/sgl-project/sglang/pull/47675) | merged | [Refactor] memory-pool: Build MiniMax K-only index host pools from buffer info | `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py` |
| 2026-11-02 | [#47844](https://github.com/sgl-project/sglang/pull/47844) | merged | [Doc] [AMD] cookbook: Verify MiniMax-M3.1-Flash High-Throughput on MI355X | `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` |
| 2026-11-03 | [#48070](https://github.com/sgl-project/sglang/pull/48070) | merged | [Doc] cookbook: Add MiniMax-M3.1-Flash GB300 MonoKernel and DEP16 AgentX points | `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` |
| 2026-11-05 | [#47187](https://github.com/sgl-project/sglang/pull/47187) | merged | [Doc] minimax-m3: Route GB300 decode to trtllm_mha in the cookbook recipe (prefill stays fa4) | `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` |

## Per-PR Diff Audit Cards

### PR #12129 - Support MiniMax M2 model

- Link: https://github.com/sgl-project/sglang/pull/12129
- Status/date: merged / 2025-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/minimax_m2.py`, `python/sglang/srt/models/minimax_m2.py`; associated commits `7ebc28f5d657`
- Diff scope read: GitHub Pull Request files API returned 5 files, +1320/-1, 1365 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support MiniMax M2 model"; model line: MiniMax M2 Series; category: model support/runtime entry; main diff: `python/sglang/srt/models/minimax_m2.py`, `python/sglang/srt/function_call/minimax_m2.py`; technical summary: Covers "Support MiniMax M2 model"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`, `python/sglang/srt/function_call/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` added +922/-0 (922 lines); hunks: -0,0 +1,922; symbols: MiniMaxM2RMSNormTP, __init__, weight_loader, forward, touching `MiniMaxM2RMSNormTP, __init__, weight_loader`; `python/sglang/srt/function_call/minimax_m2.py` added +367/-0 (367 lines); hunks: -0,0 +1,367; symbols: _safe_val, MinimaxM2Detector, __init__, has_tool_call, touching `_safe_val, MinimaxM2Detector, __init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` added +922/-0 (922 lines); hunks: -0,0 +1,922; symbols: MiniMaxM2RMSNormTP, __init__, weight_loader, forward
  - `python/sglang/srt/function_call/minimax_m2.py` added +367/-0 (367 lines); hunks: -0,0 +1,367; symbols: _safe_val, MinimaxM2Detector, __init__, has_tool_call
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -0,0 +1,922 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/function_call/minimax_m2.py
@@ -0,0 +1,367 @@
+import ast
+import html
+import json
+import logging
+import re
+from typing import Any, Dict, List, Tuple
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` added +922/-0; `python/sglang/srt/function_call/minimax_m2.py` added +367/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/function_call/minimax_m2.py`, `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12798 - Support capturing aux_hidden_states for minimax m2.

- Link: https://github.com/sgl-project/sglang/pull/12798
- Status/date: merged / 2025-11-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `f1a9c72de3c1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +34/-3, 90 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support capturing aux_hidden_states for minimax m2."; model line: MiniMax M2 Series; category: model support/runtime entry; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Support capturing aux_hidden_states for minimax m2."; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +34/-3 (37 lines); hunks: -706,6 +706,9 @@ def layer_fn(idx, prefix: str) -> nn.Module:; -716,7 +719,7 @@ def forward(; symbols: layer_fn, get_input_embeddings, forward, touching `layer_fn, get_input_embeddings, forward`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +34/-3 (37 lines); hunks: -706,6 +706,9 @@ def layer_fn(idx, prefix: str) -> nn.Module:; -716,7 +719,7 @@ def forward(; symbols: layer_fn, get_input_embeddings, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -706,6 +706,9 @@ def layer_fn(idx, prefix: str) -> nn.Module:
+        # For EAGLE3 support
+        self.layers_to_capture = []
@@ -716,7 +719,7 @@ def forward(
-    ) -> Union[torch.Tensor, PPProxyTensors]:
+    ) -> Union[torch.Tensor, PPProxyTensors, Tuple[torch.Tensor, list[torch.Tensor]]]:
@@ -728,6 +731,7 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +34/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13297 - Fix: add missing get_embed_and_head in MiniMax M2 for Eagle3

- Link: https://github.com/sgl-project/sglang/pull/13297
- Status/date: merged / 2025-11-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `b051d76dabb8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-0, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix: add missing get_embed_and_head in MiniMax M2 for Eagle3"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Fix: add missing get_embed_and_head in MiniMax M2 for Eagle3"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +3/-0 (3 lines); hunks: -821,6 +821,9 @@ def set_eagle3_layers_to_capture(self, layer_ids: Optional[l...; symbols: set_eagle3_layers_to_capture, get_embed_and_head, forward, touching `set_eagle3_layers_to_capture, get_embed_and_head, forward`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +3/-0 (3 lines); hunks: -821,6 +821,9 @@ def set_eagle3_layers_to_capture(self, layer_ids: Optional[l...; symbols: set_eagle3_layers_to_capture, get_embed_and_head, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -821,6 +821,9 @@ def set_eagle3_layers_to_capture(self, layer_ids: Optional[list[int]] = None):
+    def get_embed_and_head(self):
+        return self.model.embed_tokens.weight, self.lm_head.weight
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13659 - Super tiny remove unused MiniMaxM2MLP class

- Link: https://github.com/sgl-project/sglang/pull/13659
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `3f1cfd87b6fd`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-36, 57 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Super tiny remove unused MiniMaxM2MLP class"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Super tiny remove unused MiniMaxM2MLP class"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +0/-36 (36 lines); hunks: -31,15 +31,13; -127,40 +125,6 @@ def forward(; symbols: forward, MiniMaxM2MLP, __init__, MiniMaxM2MoE, touching `forward, MiniMaxM2MLP, __init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +0/-36 (36 lines); hunks: -31,15 +31,13; -127,40 +125,6 @@ def forward(; symbols: forward, MiniMaxM2MLP, __init__, MiniMaxM2MoE
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -31,15 +31,13 @@
-from sglang.srt.layers.activation import SiluAndMul
-    MergedColumnParallelLinear,
@@ -127,40 +125,6 @@ def forward(
-class MiniMaxM2MLP(nn.Module):
-    def __init__(
-        self,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +0/-36
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13892 - fix: correct usage of minimax-m2 deepep moe forward

- Link: https://github.com/sgl-project/sglang/pull/13892
- Status/date: merged / 2025-11-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `e0e8a9963043`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-7, 26 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: correct usage of minimax-m2 deepep moe forward"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "fix: correct usage of minimax-m2 deepep moe forward"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +3/-7 (10 lines); hunks: -222,7 +222,7 @@ def forward_deepep(; -231,14 +231,10 @@ def forward_deepep(; symbols: forward_deepep, touching `forward_deepep`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +3/-7 (10 lines); hunks: -222,7 +222,7 @@ def forward_deepep(; -231,14 +231,10 @@ def forward_deepep(; symbols: forward_deepep
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -222,7 +222,7 @@ def forward_deepep(
-            topk_weights, topk_idx, _ = self.topk(
+            topk_output = self.topk(
@@ -231,14 +231,10 @@ def forward_deepep(
-            topk_weights, topk_idx, _ = self.topk.empty_topk_output(
-                hidden_states.shape[0], self.top_k
-            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +3/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14047 - Optimize topk sigmoid in minimax_m2

- Link: https://github.com/sgl-project/sglang/pull/14047
- Status/date: merged / 2025-12-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `3dabd609fb03`
- Diff scope read: GitHub Pull Request files API returned 2 files, +38/-13, 149 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Optimize topk sigmoid in minimax_m2"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Optimize topk sigmoid in minimax_m2"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +0/-3 (3 lines); hunks: -167,9 +167,6 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +0/-3 (3 lines); hunks: -167,9 +167,6 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -167,9 +167,6 @@ def __init__(
-            use_grouped_topk=True,  # TODO: Use "grouped top-k" flag only for hardcoded sigmoid scoring
-            num_expert_group=1,
-            topk_group=1,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +0/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15538 - Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs

- Link: https://github.com/sgl-project/sglang/pull/15538
- Status/date: merged / 2025-12-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/minimax_m2.py`; associated commits `5c64a20da7dd`
- Diff scope read: GitHub Pull Request files API returned 4 files, +254/-19, 345 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `python/sglang/srt/function_call/minimax_m2.py`; technical summary: Covers "Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs"; the main implementation surface is `python/sglang/srt/function_call/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/minimax_m2.py` modified +185/-17 (202 lines); hunks: -1,5 +1,3; -16,17 +14,6; symbols: _safe_val, MinimaxM2Detector, detect_and_parse, _convert_param_value, touching `_safe_val, MinimaxM2Detector, detect_and_parse`.
- Code diff details:
  - `python/sglang/srt/function_call/minimax_m2.py` modified +185/-17 (202 lines); hunks: -1,5 +1,3; -16,17 +14,6; symbols: _safe_val, MinimaxM2Detector, detect_and_parse, _convert_param_value
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/minimax_m2.py
@@ -1,5 +1,3 @@
-import ast
-import html
@@ -16,17 +14,6 @@
-def _safe_val(raw: str) -> Any:
-    raw = html.unescape(raw.strip())
-    try:
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/minimax_m2.py` modified +185/-17
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14416 - Fusing RMSNormTP in minimax_m2

- Link: https://github.com/sgl-project/sglang/pull/14416
- Status/date: merged / 2025-12-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `d17b9e639224`
- Diff scope read: GitHub Pull Request files API returned 1 files, +189/-2, 219 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fusing RMSNormTP in minimax_m2"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Fusing RMSNormTP in minimax_m2"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +189/-2 (191 lines); hunks: -19,6 +19,8; -73,6 +75,164; symbols: rmsnorm_sumsq_kernel_serial, rmsnorm_apply_kernel_serial, rms_sumsq_serial, rms_apply_serial, touching `rmsnorm_sumsq_kernel_serial, rmsnorm_apply_kernel_serial, rms_sumsq_serial`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +189/-2 (191 lines); hunks: -19,6 +19,8; -73,6 +75,164; symbols: rmsnorm_sumsq_kernel_serial, rmsnorm_apply_kernel_serial, rms_sumsq_serial, rms_apply_serial
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -19,6 +19,8 @@
+import triton
+import triton.language as tl
@@ -73,6 +75,164 @@
+@triton.jit
+def rmsnorm_sumsq_kernel_serial(
+    x1_ptr,  # T* [B, D]
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +189/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16483 - Optimizing all_reduce in RMSNormTP in minimax_m2

- Link: https://github.com/sgl-project/sglang/pull/16483
- Status/date: merged / 2026-02-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `486c7de39f5c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-2, 24 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Optimizing all_reduce in RMSNormTP in minimax_m2"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Optimizing all_reduce in RMSNormTP in minimax_m2"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +8/-2 (10 lines); hunks: -166,7 +166,14 @@ def rms_sumsq_serial(x1: torch.Tensor, x2: torch.Tensor) ->...; -285,7 +292,6 @@ def forward(; symbols: rms_sumsq_serial, forward, forward_qk, touching `rms_sumsq_serial, forward, forward_qk`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +8/-2 (10 lines); hunks: -166,7 +166,14 @@ def rms_sumsq_serial(x1: torch.Tensor, x2: torch.Tensor) ->...; -285,7 +292,6 @@ def forward(; symbols: rms_sumsq_serial, forward, forward_qk
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -166,7 +166,14 @@ def rms_sumsq_serial(x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
-    sum_sq = torch.empty(B + B2, device=x1.device, dtype=torch.float32)
+    # We found that custom all-reduce `sglang::cross_device_reduce_1stage`
+    # is much faster than the nccl all-reduce in torch.
+    # However, `should_custom_ar` checks if the reduced buffer is 16-byte aligned.
+    # RMSNormTP reduces a [B, 2] fp32 tensor, so we pad the total element count to
+    # satisfy the alignment requirement.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +8/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18217 - [piecewise graph]: support MiniMax-M2

- Link: https://github.com/sgl-project/sglang/pull/18217
- Status/date: merged / 2026-02-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `079fc8f3c591`
- Diff scope read: GitHub Pull Request files API returned 2 files, +28/-7, 70 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[piecewise graph]: support MiniMax-M2"; model line: MiniMax M2 Series; category: model support/runtime entry; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[piecewise graph]: support MiniMax-M2"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +23/-7 (30 lines); hunks: -16,6 +16,7; -442,9 +443,14 @@ def op_select_experts(self, state):; symbols: op_select_experts, op_dispatch_a, op_dispatch_b, forward, touching `op_select_experts, op_dispatch_a, op_dispatch_b`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +23/-7 (30 lines); hunks: -16,6 +16,7; -442,9 +443,14 @@ def op_select_experts(self, state):; symbols: op_select_experts, op_dispatch_a, op_dispatch_b, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -16,6 +16,7 @@
+from contextlib import nullcontext
@@ -442,9 +443,14 @@ def op_select_experts(self, state):
-            with get_global_expert_distribution_recorder().with_current_layer(
-                self.layer_id
-            ):
+            ctx = (
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +23/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #19443 - [AMD] [MiniMax-M2.5 Day 0] Add MiniMax-M2.5 nightly accuracy test

- Link: https://github.com/sgl-project/sglang/pull/19443
- Status/date: merged / 2026-02-27
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py`; associated commits `403195d59de0`
- Diff scope read: GitHub Pull Request files API returned 6 files, +653/-4, 766 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] [MiniMax-M2.5 Day 0] Add MiniMax-M2.5 nightly accuracy test"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py`; technical summary: Covers "[AMD] [MiniMax-M2.5 Day 0] Add MiniMax-M2.5 nightly accuracy test"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: ModelConfig, __post_init__, get_display_name, get_one_example, touching `ModelConfig, __post_init__, get_display_name`; `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py` added +245/-0 (245 lines); hunks: -0,0 +1,245; symbols: ModelConfig, __post_init__, get_display_name, get_one_example, touching `ModelConfig, __post_init__, get_display_name`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: ModelConfig, __post_init__, get_display_name, get_one_example
  - `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py` added +245/-0 (245 lines); hunks: -0,0 +1,245; symbols: ModelConfig, __post_init__, get_display_name, get_one_example
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py
@@ -0,0 +1,249 @@
+"""MI35x MiniMax-M2.5 GSM8K Completion Evaluation Test (8-GPU)
+Tests MiniMax-M2.5 with TP=8 + EP=8 configuration using few-shot completion
+benchmark on MI35x.
+Registry: nightly-amd-8-gpu-mi35x-minimax-m25 suite
+"""
+import ast
diff -- test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py
@@ -0,0 +1,245 @@
+"""AMD MiniMax-M2.5 GSM8K Completion Evaluation Test (8-GPU)
+Tests MiniMax-M2.5 with TP=8 + EP=8 configuration using few-shot completion
+benchmark on MI325/MI300X.
+Registry: nightly-amd-accuracy-8-gpu-minimax-m25 suite
+"""
+import ast
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py` added +249/-0; `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py` added +245/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #19577 - [Feat] add PP Support for minimax-m2 series

- Link: https://github.com/sgl-project/sglang/pull/19577
- Status/date: merged / 2026-03-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `2d183c4e6d32`
- Diff scope read: GitHub Pull Request files API returned 1 files, +35/-7, 97 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] add PP Support for minimax-m2 series"; model line: MiniMax M2 Series; category: model support/runtime entry; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[Feat] add PP Support for minimax-m2 series"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +35/-7 (42 lines); hunks: -54,7 +54,7; -967,6 +967,7 @@ def __init__(; symbols: __init__, forward, load_weights, touching `__init__, forward, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +35/-7 (42 lines); hunks: -54,7 +54,7; -967,6 +967,7 @@ def __init__(; symbols: __init__, forward, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -54,7 +54,7 @@
-from sglang.srt.layers.utils import PPMissingLayer
+from sglang.srt.layers.utils import PPMissingLayer, get_layer_id
@@ -967,6 +967,7 @@ def __init__(
+        self.pp_group = get_pp_group()
@@ -999,17 +1000,26 @@ def forward(
+        pp_proxy_tensors: Optional[PPProxyTensors] = None,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +35/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #19995 - Add packed_modules_mapping for MiniMax-M2

- Link: https://github.com/sgl-project/sglang/pull/19995
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `df1d046de2a1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-0, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add packed_modules_mapping for MiniMax-M2"; model line: MiniMax M2 Series; category: model support/runtime entry; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Add packed_modules_mapping for MiniMax-M2"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +12/-0 (12 lines); hunks: -941,6 +941,18 @@ def forward(; symbols: forward, MiniMaxM2ForCausalLM, __init__, touching `forward, MiniMaxM2ForCausalLM, __init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +12/-0 (12 lines); hunks: -941,6 +941,18 @@ def forward(; symbols: forward, MiniMaxM2ForCausalLM, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -941,6 +941,18 @@ def forward(
+    packed_modules_mapping = {
+        "qkv_proj": [
+            "q_proj",
+            "k_proj",
+            "v_proj",
+        ],
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +12/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20870 - [MiniMax M2] Fix KV cache scale loading

- Link: https://github.com/sgl-project/sglang/pull/20870
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `a3196d08b8f6`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-0, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MiniMax M2] Fix KV cache scale loading"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[MiniMax M2] Fix KV cache scale loading"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +8/-0 (8 lines); hunks: -1063,10 +1063,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +8/-0 (8 lines); hunks: -1063,10 +1063,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -1063,10 +1063,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+            _is_kv_scale = name.endswith(".k_scale") or name.endswith(".v_scale")
+                # Skip kv cache scales - maybe_remap_kv_scale_name expects the
+                # original checkpoint name (e.g. self_attn.k_proj.k_scale) to
+                # remap it to self_attn.attn.k_scale. Renaming k_proj -> qkv_proj
+                # here would break that pattern match.
+                if _is_kv_scale:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +8/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20905 - [NPU][ModelSlim] adapt w2 quant layer for Minimax2.5

- Link: https://github.com/sgl-project/sglang/pull/20905
- Status/date: merged / 2026-03-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `1b4933d45d93`
- Diff scope read: GitHub Pull Request files API returned 2 files, +22/-30, 67 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU][ModelSlim] adapt w2 quant layer for Minimax2.5"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[NPU][ModelSlim] adapt w2 quant layer for Minimax2.5"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +1/-1 (2 lines); hunks: -713,7 +713,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +1/-1 (2 lines); hunks: -713,7 +713,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -713,7 +713,7 @@ def __init__(
-            prefix=add_prefix("mlp", prefix),
+            prefix=add_prefix("block_sparse_moe", prefix),
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21241 - [bugfix] Fix rope theta config for MiniMax after transformers v5 update

- Link: https://github.com/sgl-project/sglang/pull/21241
- Status/date: merged / 2026-03-31
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `b91f78d255d8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-3, 32 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[bugfix] Fix rope theta config for MiniMax after transformers v5 update"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[bugfix] Fix rope theta config for MiniMax after transformers v5 update"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +3/-3 (6 lines); hunks: -73,6 +73,7; -570,7 +571,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +3/-3 (6 lines); hunks: -73,6 +73,7; -570,7 +571,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -73,6 +73,7 @@
+from sglang.srt.utils.hf_transformers_utils import get_rope_config
@@ -570,7 +571,7 @@ def __init__(
-        self.rope_theta = config.rope_theta
+        self.rope_theta, self.rope_scaling = get_rope_config(config)
@@ -600,13 +601,12 @@ def __init__(
-        rope_scaling = getattr(config, "rope_scaling", None)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +3/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21524 - [AMD] Add MiniMax-M2.5 nightly perf benchmarks for MI30x and MI35x

- Link: https://github.com/sgl-project/sglang/pull/21524
- Status/date: merged / 2026-04-03
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py`, `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py`; associated commits `d07d0a15ceb8`
- Diff scope read: GitHub Pull Request files API returned 4 files, +338/-4, 400 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add MiniMax-M2.5 nightly perf benchmarks for MI30x and MI35x"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py`; technical summary: Covers "[AMD] Add MiniMax-M2.5 nightly perf benchmarks for MI30x and MI35x"; the main implementation surface is `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py`, `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyMiniMaxM25PerformanceMI35x, setUpClass, test_bench_minimax_m25, touching `generate_simple_markdown_report, TestNightlyMiniMaxM25PerformanceMI35x, setUpClass`; `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py` added +140/-0 (140 lines); hunks: -0,0 +1,140; symbols: generate_simple_markdown_report, TestNightlyMiniMaxM25Performance, setUpClass, test_bench_minimax_m25, touching `generate_simple_markdown_report, TestNightlyMiniMaxM25Performance, setUpClass`.
- Code diff details:
  - `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyMiniMaxM25PerformanceMI35x, setUpClass, test_bench_minimax_m25
  - `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py` added +140/-0 (140 lines); hunks: -0,0 +1,140; symbols: generate_simple_markdown_report, TestNightlyMiniMaxM25Performance, setUpClass, test_bench_minimax_m25
- Key code excerpts:

```diff
diff -- test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py
@@ -0,0 +1,146 @@
+"""MI35x Nightly performance benchmark for MiniMax-M2.5 (8-GPU).
+This test benchmarks MiniMax-M2.5 with TP=8 + EP=8 configuration on MI35x.
+The model path can be configured via MINIMAX_M25_MODEL_PATH environment variable.
+Registry: nightly-perf-8-gpu-mi35x-minimax-m25 suite
+Example usage:
+    python -m pytest test_minimax_m25_perf_mi35x.py -v
diff -- test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py
@@ -0,0 +1,140 @@
+"""Nightly performance benchmark for MiniMax-M2.5 on MI325/MI300X (8-GPU).
+This test benchmarks MiniMax-M2.5 with TP=8 + EP=8 configuration.
+The model path can be configured via MINIMAX_M25_MODEL_PATH environment variable.
+Registry: nightly-perf-8-gpu-minimax-m25 suite
+Example usage:
+    python -m pytest test_minimax_m25_perf_amd.py -v
```

- Reviewed files:
  - tests: `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py` added +146/-0; `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py` added +140/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/perf/mi30x/test_minimax_m25_perf_amd.py`, `test/registered/amd/perf/mi35x/test_minimax_m25_perf_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #20919 - [NPU] Support dp-attention for MiniMax2.5

- Link: https://github.com/sgl-project/sglang/pull/20919
- Status/date: merged / 2026-04-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `ae38b24cc358`
- Diff scope read: GitHub Pull Request files API returned 2 files, +104/-40, 298 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] Support dp-attention for MiniMax2.5"; model line: MiniMax M2 Series; category: model support/runtime entry; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[NPU] Support dp-attention for MiniMax2.5"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +82/-39 (121 lines); hunks: -30,7 +30,6; -41,6 +40,12; symbols: MiniMaxM2RMSNormTP, __init__, weight_loader, forward, touching `MiniMaxM2RMSNormTP, __init__, weight_loader`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +82/-39 (121 lines); hunks: -30,7 +30,6; -41,6 +40,12; symbols: MiniMaxM2RMSNormTP, __init__, weight_loader, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -30,7 +30,6 @@
-    get_tensor_model_parallel_rank,
@@ -41,6 +40,12 @@
+from sglang.srt.layers.dp_attention import (
+    attn_tp_all_reduce,
+    get_attention_tp_rank,
+    get_attention_tp_size,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +82/-39
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20967 - 【BugFix】fix the bug of minimax_m2.5 model that causes repeated outputs when using tp16

- Link: https://github.com/sgl-project/sglang/pull/20967
- Status/date: merged / 2026-04-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `84194c25c1cd`
- Diff scope read: GitHub Pull Request files API returned 1 files, +34/-10, 73 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "【BugFix】fix the bug of minimax_m2.5 model that causes repeated outputs when using tp16"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "【BugFix】fix the bug of minimax_m2.5 model that causes repeated outputs when using tp16"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +34/-10 (44 lines); hunks: -253,27 +253,47 @@ def rms_apply_serial(; -641,10 +661,14 @@ def __init__(; symbols: rms_apply_serial, MiniMaxM2RMSNormTP, __init__, weight_loader, touching `rms_apply_serial, MiniMaxM2RMSNormTP, __init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +34/-10 (44 lines); hunks: -253,27 +253,47 @@ def rms_apply_serial(; -641,10 +661,14 @@ def __init__(; symbols: rms_apply_serial, MiniMaxM2RMSNormTP, __init__, weight_loader
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -253,27 +253,47 @@ def rms_apply_serial(
-    def __init__(self, hidden_size: int, eps: float = 1e-6) -> None:
+    def __init__(self, hidden_size: int, num_heads: int, eps: float = 1e-6) -> None:
+        # Align with QKVParallelLinear pattern
+        if self.attn_tp_size >= num_heads:
+            assert (
+                self.attn_tp_size % num_heads == 0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +34/-10
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20067 - MiniMax-M2.5 - Support dp attention, dp reduce scatter, FP4 all gather, AR fusion in prepare_attn

- Link: https://github.com/sgl-project/sglang/pull/20067
- Status/date: merged / 2026-04-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `7dbd0dd9f01a`
- Diff scope read: GitHub Pull Request files API returned 3 files, +39/-6, 106 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "MiniMax-M2.5 - Support dp attention, dp reduce scatter, FP4 all gather, AR fusion in prepare_attn"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "MiniMax-M2.5 - Support dp attention, dp reduce scatter, FP4 all gather, AR fusion in prepare_attn"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +25/-6 (31 lines); hunks: -53,10 +53,13; -417,12 +420,20 @@ def forward_normal(; symbols: forward_normal, forward_prepare, forward_core, __init__, touching `forward_normal, forward_prepare, forward_core`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +25/-6 (31 lines); hunks: -53,10 +53,13; -417,12 +420,20 @@ def forward_normal(; symbols: forward_normal, forward_prepare, forward_core, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -53,10 +53,13 @@
+from sglang.srt.layers.moe import (
+    get_moe_a2a_backend,
+    should_use_flashinfer_cutlass_moe_fp4_allgather,
+)
-from sglang.srt.layers.moe.utils import get_moe_a2a_backend
@@ -417,12 +420,20 @@ def forward_normal(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +25/-6
- Risk and verification: The diff ships test coverage in `test/registered/8-gpu-models/test_minimax_m25.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #20673 - [Feature][JIT Kernel] Fused TP QK norm For Minimax

- Link: https://github.com/sgl-project/sglang/pull/20673
- Status/date: merged / 2026-04-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `314d6ecf0880`
- Diff scope read: GitHub Pull Request files API returned 11 files, +923/-82, 1277 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature][JIT Kernel] Fused TP QK norm For Minimax"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[Feature][JIT Kernel] Fused TP QK norm For Minimax"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +113/-21 (134 lines); hunks: -17,17 +17,23; -42,6 +48,7; symbols: forward, fused_tp_qknorm, MiniMaxM2QKRMSNorm, __init__, touching `forward, fused_tp_qknorm, MiniMaxM2QKRMSNorm`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +113/-21 (134 lines); hunks: -17,17 +17,23; -42,6 +48,7; symbols: forward, fused_tp_qknorm, MiniMaxM2QKRMSNorm, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -17,17 +17,23 @@
-from typing import Iterable, Optional, Set, Tuple, Union
+from functools import lru_cache
+from typing import Any, Dict, Iterable, Optional, Set, Tuple, Union
+from sglang.jit_kernel.all_reduce import (
+    fused_parallel_qknorm,
+    get_fused_parallel_qknorm_max_occupancy,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +113/-21
- Risk and verification: The diff ships test coverage in `python/sglang/jit_kernel/tests/test_custom_all_reduce.py`, `python/sglang/jit_kernel/tests/test_tp_qknorm.py`, `python/sglang/jit_kernel/tests/utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22722 - [AMD] Add MiniMax-M2.7 accuracy and performance nightly tests

- Link: https://github.com/sgl-project/sglang/pull/22722
- Status/date: merged / 2026-04-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`, `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_minimax_m27_perf_amd.py`, `test/registered/amd/perf/mi35x/test_minimax_m27_perf_mi35x.py`; associated commits `eab045b2b74e`
- Diff scope read: GitHub Pull Request files API returned 7 files, +805/-113, 1069 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add MiniMax-M2.7 accuracy and performance nightly tests"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m2.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`; technical summary: Covers "[AMD] Add MiniMax-M2.7 accuracy and performance nightly tests"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py`, `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +7/-1 (8 lines); hunks: -33,7 +33,6; -81,9 +80,16; `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: ModelConfig, __post_init__, get_display_name, get_one_example, touching `ModelConfig, __post_init__, get_display_name`; `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` added +245/-0 (245 lines); hunks: -0,0 +1,245; symbols: ModelConfig, __post_init__, get_display_name, get_one_example, touching `ModelConfig, __post_init__, get_display_name`; `test/registered/amd/perf/mi35x/test_minimax_m27_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyMiniMaxM27PerformanceMI35x, setUpClass, test_bench_minimax_m27, touching `generate_simple_markdown_report, TestNightlyMiniMaxM27PerformanceMI35x, setUpClass`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +7/-1 (8 lines); hunks: -33,7 +33,6; -81,9 +80,16
  - `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: ModelConfig, __post_init__, get_display_name, get_one_example
  - `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` added +245/-0 (245 lines); hunks: -0,0 +1,245; symbols: ModelConfig, __post_init__, get_display_name, get_one_example
  - `test/registered/amd/perf/mi35x/test_minimax_m27_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyMiniMaxM27PerformanceMI35x, setUpClass, test_bench_minimax_m27
  - `test/registered/amd/perf/mi30x/test_minimax_m27_perf_amd.py` added +140/-0 (140 lines); hunks: -0,0 +1,140; symbols: generate_simple_markdown_report, TestNightlyMiniMaxM27Performance, setUpClass, test_bench_minimax_m27
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -33,7 +33,6 @@
-    get_bool_env_var,
@@ -81,9 +80,16 @@
+# get_bool_env_var is defined in sglang.srt.utils.common, not sglang.srt.distributed.
+# Importing from the wrong module causes this file to fail import, which prevents the
+# native MiniMaxM2ForCausalLM from registering in ModelRegistry. The fallback to the
+# transformers wrapper then crashes on config.rope_parameters (transformers v5 issue).
diff -- test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py
@@ -0,0 +1,249 @@
+"""MI35x MiniMax-M2.7 GSM8K Completion Evaluation Test (8-GPU)
+Tests MiniMax-M2.7 with TP=8 + EP=8 configuration using few-shot completion
+benchmark on MI35x.
+Registry: nightly-amd-8-gpu-mi35x-minimax-m27 suite
+"""
+import ast
diff -- test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py
@@ -0,0 +1,245 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +7/-1
  - tests: `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py` added +249/-0; `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` added +245/-0; `test/registered/amd/perf/mi35x/test_minimax_m27_perf_mi35x.py` added +146/-0; `test/registered/amd/perf/mi30x/test_minimax_m27_perf_amd.py` added +140/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m27_eval_mi35x.py`, `test/registered/amd/perf/mi30x/test_minimax_m27_perf_amd.py`, `test/registered/amd/perf/mi35x/test_minimax_m27_perf_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #23190 - [NPU] add split_qkv_tp_rmsnorm_rope ops for minimax2 & fix eagle3 hidden states capture in dp attn mode

- Link: https://github.com/sgl-project/sglang/pull/23190
- Status/date: merged / 2026-04-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `3553fd032251`
- Diff scope read: GitHub Pull Request files API returned 1 files, +66/-10, 133 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] add split_qkv_tp_rmsnorm_rope ops for minimax2 & fix eagle3 hidden states capture in dp attn mode"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[NPU] add split_qkv_tp_rmsnorm_rope ops for minimax2 & fix eagle3 hidden states capture in dp attn mode"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +66/-10 (76 lines); hunks: -18,7 +18,7; -93,13 +93,18; symbols: forward_prepare, forward_prepare_npu, forward_core, forward, touching `forward_prepare, forward_prepare_npu, forward_core`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +66/-10 (76 lines); hunks: -18,7 +18,7; -93,13 +93,18; symbols: forward_prepare, forward_prepare_npu, forward_core, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -18,7 +18,7 @@
-from typing import Any, Dict, Iterable, Optional, Set, Tuple, Union
+from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union
@@ -93,13 +93,18 @@
+    is_npu,
+_is_npu = is_npu()
+if _is_npu:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +66/-10
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25061 - Fix MiniMax-M2.7 on CPU

- Link: https://github.com/sgl-project/sglang/pull/25061
- Status/date: merged / 2026-05-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `714fdd972342`
- Diff scope read: GitHub Pull Request files API returned 3 files, +50/-6, 138 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix MiniMax-M2.7 on CPU"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Fix MiniMax-M2.7 on CPU"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +27/-0 (27 lines); hunks: -78,6 +78,7; -89,8 +90,10; symbols: weight_loader, __init__, _forward_fused, _forward_cpu, touching `weight_loader, __init__, _forward_fused`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +27/-0 (27 lines); hunks: -78,6 +78,7; -89,8 +90,10; symbols: weight_loader, __init__, _forward_fused, _forward_cpu
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -78,6 +78,7 @@
+    narrow_padded_param_and_loaded_weight,
@@ -89,8 +90,10 @@
+    cpu_has_amx_support,
+    is_cpu,
@@ -100,6 +103,8 @@
+_is_cpu = is_cpu()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +27/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27126 - [AMD] Add MiniMax-M2.5 TP=4 nightly accuracy test for MI355X

- Link: https://github.com/sgl-project/sglang/pull/27126
- Status/date: merged / 2026-06-04
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py`; associated commits `6dcd78a37ff8`
- Diff scope read: GitHub Pull Request files API returned 3 files, +339/-0, 382 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add MiniMax-M2.5 TP=4 nightly accuracy test for MI355X"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py`; technical summary: Covers "[AMD] Add MiniMax-M2.5 TP=4 nightly accuracy test for MI355X"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py` added +255/-0 (255 lines); hunks: -0,0 +1,255; symbols: ModelConfig, __post_init__, get_display_name, get_one_example, touching `ModelConfig, __post_init__, get_display_name`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py` added +255/-0 (255 lines); hunks: -0,0 +1,255; symbols: ModelConfig, __post_init__, get_display_name, get_one_example
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py
@@ -0,0 +1,255 @@
+"""MI35x MiniMax-M2.5 GSM8K Completion Evaluation Test (4-GPU, TP=4)
+Tests MiniMax-M2.5 with TP=4 + EP=1 configuration using few-shot completion
+benchmark on MI35x. This configuration uses unified attention with FP8 KV cache.
+Registry: nightly-amd-4-gpu-mi35x-minimax-m25-tp4 suite
+"""
+import os
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py` added +255/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #28712 - [minimax-m3] Split 1/4: sparse attention ops + JIT kernels + config foundation

- Link: https://github.com/sgl-project/sglang/pull/28712
- Status/date: merged / 2026-06-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json`; associated commits `7c23d2255a1f`
- Diff scope read: GitHub Pull Request files API returned 51 files, +11157/-33, 11466 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[minimax-m3] Split 1/4: sparse attention ops + JIT kernels + config foundation"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json`; technical summary: Covers "[minimax-m3] Split 1/4: sparse attention ops + JIT kernels + config foundation"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` added +353/-0 (353 lines); hunks: -0,0 +1,353; symbols: msa_available, _build_page_table, msa_sparse_prefill_main, build_msa_decode_meta, touching `msa_available, _build_page_table, msa_sparse_prefill_main`; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` added +234/-0 (234 lines); hunks: -0,0 +1,234; symbols: minimax_sparse_prefill, minimax_sparse_decode, touching `minimax_sparse_prefill, minimax_sparse_decode`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json` added +70/-0 (70 lines); hunks: -0,0 +1,70.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` added +353/-0 (353 lines); hunks: -0,0 +1,353; symbols: msa_available, _build_page_table, msa_sparse_prefill_main, build_msa_decode_meta
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` added +234/-0 (234 lines); hunks: -0,0 +1,234; symbols: minimax_sparse_prefill, minimax_sparse_decode
  - `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json` added +70/-0 (70 lines); hunks: -0,0 +1,70
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py
@@ -0,0 +1,353 @@
+# MSA (fmha_sm100) drop-in for the MiniMax-M3 main sparse-attention step.
+#
+# Replaces only step 3 of MiniMax sparse prefill/decode. The lightning indexer
+# (steps 1-2) is unchanged and still produces `topk_idx`.
+# NVIDIA Blackwell (SM100/sm_103) only; callers gate on `msa_available()`.
+from __future__ import annotations
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -0,0 +1,234 @@
+# Copyright 2025 XunhaoLai. All rights reserved.
+from typing import Callable, List, Optional, Tuple
+import torch
+from .common.index import topk_index_reduce
+from .common.utils import get_cu_seqblocks
+from .decode.flash_with_topk_idx import flash_decode_with_topk_idx
diff -- python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json
@@ -0,0 +1,70 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` added +353/-0; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` added +234/-0; `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/minimax_m3_gfx950_mxfp8_compact_moe.json` added +70/-0
- Risk and verification: The diff ships test coverage in `python/sglang/jit_kernel/tests/test_minimax_m3_mxfp8.py`, `python/sglang/jit_kernel/tests/test_minimax_m3_rmsnorm.py`, `python/sglang/jit_kernel/tests/test_moe_topk_sigmoid.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29250 - Fix MiniMax MSA fallback when fmha plan is unavailable

- Link: https://github.com/sgl-project/sglang/pull/29250
- Status/date: merged / 2026-06-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`; associated commits `852467888948`
- Diff scope read: GitHub Pull Request files API returned 2 files, +115/-46, 280 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix MiniMax MSA fallback when fmha plan is unavailable"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`; technical summary: Covers "Fix MiniMax MSA fallback when fmha plan is unavailable"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +79/-28 (107 lines); hunks: -1,5 +1,6; -11,6 +12,20; symbols: _warn_msa_fallback, minimax_sparse_prefill, minimax_sparse_decode, touching `_warn_msa_fallback, minimax_sparse_prefill, minimax_sparse_decode`; `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` modified +36/-18 (54 lines); hunks: -12,9 +12,34; -24,10 +49,9 @@ def msa_available() -> bool:; symbols: MSAUnavailableError, _load_fmha_sm100, _run_fmha_sm100_plan, msa_available, touching `MSAUnavailableError, _load_fmha_sm100, _run_fmha_sm100_plan`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +79/-28 (107 lines); hunks: -1,5 +1,6; -11,6 +12,20; symbols: _warn_msa_fallback, minimax_sparse_prefill, minimax_sparse_decode
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` modified +36/-18 (54 lines); hunks: -12,9 +12,34; -24,10 +49,9 @@ def msa_available() -> bool:; symbols: MSAUnavailableError, _load_fmha_sm100, _run_fmha_sm100_plan, msa_available
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -1,5 +1,6 @@
+import logging
@@ -11,6 +12,20 @@
+logger = logging.getLogger(__name__)
+_msa_fallback_warned = False
+def _warn_msa_fallback(err: Exception) -> None:
+    global _msa_fallback_warned
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py
@@ -12,9 +12,34 @@
+class MSAUnavailableError(RuntimeError):
+    """Raised when fmha_sm100 cannot serve the MiniMax MSA path."""
+@functools.lru_cache(maxsize=1)
+def _load_fmha_sm100():
+    try:
+        from fmha_sm100 import fmha_sm100, fmha_sm100_plan
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +79/-28; `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` modified +36/-18
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28713 - [minimax-m3] Split 2/4: mem-cache / HiCache / sparse KV pool

- Link: https://github.com/sgl-project/sglang/pull/28713
- Status/date: merged / 2026-06-27
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py`; associated commits `592f6c849bf9`
- Diff scope read: GitHub Pull Request files API returned 10 files, +1715/-39, 1991 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[minimax-m3] Split 2/4: mem-cache / HiCache / sparse KV pool"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py`; technical summary: Covers "[minimax-m3] Split 2/4: mem-cache / HiCache / sparse KV pool"; the main implementation surface is `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py` added +410/-0 (410 lines); hunks: -0,0 +1,410; symbols: _cuda_major, _FakeLayerTransferCounter, __init__, wait_until, touching `_cuda_major, _FakeLayerTransferCounter, __init__`; `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` added +58/-0 (58 lines); hunks: -0,0 +1,58; symbols: _make_k_only_pool, TestMiniMaxSparsePoolPD, test_contiguous_buf_infos_main_only, test_index_k_state_buf_infos, touching `_make_k_only_pool, TestMiniMaxSparsePoolPD, test_contiguous_buf_infos_main_only`.
- Code diff details:
  - `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py` added +410/-0 (410 lines); hunks: -0,0 +1,410; symbols: _cuda_major, _FakeLayerTransferCounter, __init__, wait_until
  - `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` added +58/-0 (58 lines); hunks: -0,0 +1,58; symbols: _make_k_only_pool, TestMiniMaxSparsePoolPD, test_contiguous_buf_infos_main_only, test_index_k_state_buf_infos
- Key code excerpts:

```diff
diff -- test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py
@@ -0,0 +1,410 @@
+import unittest
+import psutil
+import torch
+from sglang.srt.mem_cache.hicache_storage import PoolHitPolicy, PoolName
+from sglang.srt.mem_cache.hiradix_cache import HiRadixCache
+from sglang.srt.mem_cache.hybrid_cache.hybrid_cache_controller import (
diff -- test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py
@@ -0,0 +1,58 @@
+import unittest
+import torch
+from sglang.srt.mem_cache.memory_pool import MiniMaxSparseKVPool
+from sglang.test.ci.ci_register import register_cpu_ci
+register_cpu_ci(est_time=5, suite="base-a-test-cpu")
+def _make_k_only_pool(start_layer: int = 0) -> MiniMaxSparseKVPool:
```

- Reviewed files:
  - tests: `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py` added +410/-0; `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` added +58/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py`, `test/registered/unit/mem_cache/test_unified_radix_hicache_dispatch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #28714 - [minimax-m3] Split 3/4: disagg K-only index-K transfer

- Link: https://github.com/sgl-project/sglang/pull/28714
- Status/date: merged / 2026-06-28
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py`; associated commits `ddc389cf09fc`
- Diff scope read: GitHub Pull Request files API returned 7 files, +173/-5, 263 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[minimax-m3] Split 3/4: disagg K-only index-K transfer"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py`; technical summary: Covers "[minimax-m3] Split 3/4: disagg K-only index-K transfer"; the main implementation surface is `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py` added +74/-0 (74 lines); hunks: -0,0 +1,74; symbols: _make_k_only_pool, _make_kv_pool, TestMiniMaxSparseDisaggStateKvArgs, test_setup_state_kv_args_single_minimax_component, touching `_make_k_only_pool, _make_kv_pool, TestMiniMaxSparseDisaggStateKvArgs`.
- Code diff details:
  - `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py` added +74/-0 (74 lines); hunks: -0,0 +1,74; symbols: _make_k_only_pool, _make_kv_pool, TestMiniMaxSparseDisaggStateKvArgs, test_setup_state_kv_args_single_minimax_component
- Key code excerpts:

```diff
diff -- test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py
@@ -0,0 +1,74 @@
+import unittest
+import torch
+from sglang.srt.disaggregation.base.conn import KVArgs, StateType
+from sglang.srt.disaggregation.utils import setup_state_kv_args
+from sglang.srt.mem_cache.memory_pool import MiniMaxSparseKVPool
+from sglang.test.ci.ci_register import register_cpu_ci
```

- Reviewed files:
  - tests: `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py` added +74/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #28715 - [minimax-m3] Split 4/4: model + VL + glue + function-call + fp8 quant + generic infra

- Link: https://github.com/sgl-project/sglang/pull/28715
- Status/date: merged / 2026-07-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/minimax_vl.py`, `python/sglang/srt/function_call/minimax_m3.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py` and 8 files; associated commits `0663ebc783e6`
- Diff scope read: GitHub Pull Request files API returned 46 files, +7486/-483, 9190 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[minimax-m3] Split 4/4: model + VL + glue + function-call + fp8 quant + generic infra"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_vl_common.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`; technical summary: Covers "[minimax-m3] Split 4/4: model + VL + glue + function-call + fp8 quant + generic infra"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_vl_common.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` added +1690/-0 (1690 lines); hunks: -0,0 +1,1690; symbols: MultiHeadRMSNorm, __init__, weight_loader, forward, touching `MultiHeadRMSNorm, __init__, weight_loader`; `python/sglang/srt/models/minimax_vl_common.py` added +882/-0 (882 lines); hunks: -0,0 +1,882; symbols: CLIPVisionConfig, from_dict, MiniMaxVLMultiModalProjector, __init__, touching `CLIPVisionConfig, from_dict, MiniMaxVLMultiModalProjector`; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` added +602/-0 (602 lines); hunks: -0,0 +1,602; symbols: MiniMaxSparseAttnBackend, __init__, init_forward_metadata_out_graph, _prepare_msa_decode_meta, touching `MiniMaxSparseAttnBackend, __init__, init_forward_metadata_out_graph`; `python/sglang/srt/function_call/minimax_m3.py` added +542/-0 (542 lines); hunks: -0,0 +1,542; symbols: MinimaxM3Detector, __init__, _normalize_tag_spacing, _flushable_prefix_length, touching `MinimaxM3Detector, __init__, _normalize_tag_spacing`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` added +1690/-0 (1690 lines); hunks: -0,0 +1,1690; symbols: MultiHeadRMSNorm, __init__, weight_loader, forward
  - `python/sglang/srt/models/minimax_vl_common.py` added +882/-0 (882 lines); hunks: -0,0 +1,882; symbols: CLIPVisionConfig, from_dict, MiniMaxVLMultiModalProjector, __init__
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` added +602/-0 (602 lines); hunks: -0,0 +1,602; symbols: MiniMaxSparseAttnBackend, __init__, init_forward_metadata_out_graph, _prepare_msa_decode_meta
  - `python/sglang/srt/function_call/minimax_m3.py` added +542/-0 (542 lines); hunks: -0,0 +1,542; symbols: MinimaxM3Detector, __init__, _normalize_tag_spacing, _flushable_prefix_length
  - `test/registered/unit/function_call/test_minimax_m3_detector.py` added +539/-0 (539 lines); hunks: -0,0 +1,539; symbols: _make_tools, _wire, _segments, _collect_streamed_tool_calls
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -0,0 +1,1690 @@
+# Copyright 2023-2024 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/models/minimax_vl_common.py
@@ -0,0 +1,882 @@
+# SPDX-License-Identifier: Apache-2.0
+import logging
+from dataclasses import dataclass, fields
+from typing import List, Optional, Tuple
+import numpy as np
+import torch
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -0,0 +1,602 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` added +1690/-0; `python/sglang/srt/models/minimax_vl_common.py` added +882/-0; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` added +602/-0; `python/sglang/srt/function_call/minimax_m3.py` added +542/-0; `python/sglang/srt/models/minimax_m3_vl.py` added +372/-0; `python/sglang/srt/multimodal/processors/minimax_m3_vl.py` added +283/-0
  - tests: `test/registered/unit/function_call/test_minimax_m3_detector.py` added +539/-0
- Risk and verification: The diff ships test coverage in `test/registered/attention/test_trtllm_mha_graph_metadata.py`, `test/registered/jit/benchmark/bench_per_token_group_quant_8bit.py`, `test/registered/jit/benchmark/bench_post_reorder_deepgemm.py`, `test/registered/jit/minimax/test_minimax_fused_qkv_index_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30793 - [Kernel] Migrate linear-attention, MiniMax-sparse and diffusion kernels to sglang.kernels (RFC #29630, Phase 2.5, 6/7)

- Link: https://github.com/sgl-project/sglang/pull/30793
- Status/date: merged / 2026-07-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_sparse/__init__.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/index.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/utils.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` and 8 files; associated commits `c00131ebaaeb`
- Diff scope read: GitHub Pull Request files API returned 44 files, +238/-168, 621 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Migrate linear-attention, MiniMax-sparse and diffusion kernels to sglang.kernels (RFC #29630, Phase 2.5, 6/7)"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/__init__.py`; technical summary: Covers "[Kernel] Migrate linear-attention, MiniMax-sparse and diffusion kernels to sglang.kernels (RFC #29630, Phase 2.5, 6/7)"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/__init__.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +14/-6 (20 lines); hunks: -5,12 +5,20; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py` modified +2/-2 (4 lines); hunks: -3,10 +3,10; `python/sglang/kernels/ops/attention/__init__.py` modified +26/-0 (26 lines); hunks: -43,6 +43,32; `python/sglang/kernels/ops/attention/linear/__init__.py` added +1/-0 (1 lines); hunks: -0,0 +1.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +14/-6 (20 lines); hunks: -5,12 +5,20
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py` modified +2/-2 (4 lines); hunks: -3,10 +3,10
  - `python/sglang/kernels/ops/attention/__init__.py` modified +26/-0 (26 lines); hunks: -43,6 +43,32
  - `python/sglang/kernels/ops/attention/linear/__init__.py` added +1/-0 (1 lines); hunks: -0,0 +1
  - `python/sglang/kernels/ops/attention/minimax_sparse/__init__.py` added +1/-0 (1 lines); hunks: -0,0 +1
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -5,12 +5,20 @@
-from .common.index import topk_index_reduce
-from .common.utils import get_cu_seqblocks
-from .decode.flash_with_topk_idx import flash_decode_with_topk_idx
-from .decode.topk_sparse import flash_decode_with_gqa_share_sparse
-from .prefill.flash_with_topk_idx import flash_prefill_with_topk_index
-from .prefill.topk_sparse import flash_prefill_with_gqa_share_sparse
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py
@@ -3,10 +3,10 @@
-from sglang.srt.environ import envs
-from sglang.srt.layers.attention.minimax_sparse_ops.decode.flash_with_topk_idx import (
+from sglang.kernels.ops.attention.minimax_sparse.decode.flash_with_topk_idx import (
+from sglang.srt.environ import envs
diff -- python/sglang/kernels/ops/attention/__init__.py
@@ -43,6 +43,32 @@
+# Linear-attention / MiniMax-sparse / diffusion kernels migrated in Phase 2.5
+# (RFC #29630); registered for inventory.
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +14/-6; `python/sglang/kernels/ops/attention/__init__.py` modified +26/-0; `python/sglang/kernels/ops/attention/linear/__init__.py` added +1/-0; `python/sglang/kernels/ops/attention/minimax_sparse/__init__.py` added +1/-0; `python/sglang/kernels/ops/attention/linear/gdn_blackwell/__init__.py` renamed +0/-0; `python/sglang/kernels/ops/attention/linear/kda_blackwell/__init__.py` renamed +0/-0
  - tests: `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_sparse_gqa.py`, `test/registered/attention/test_gdn_prefill_cutedsl.py`, `test/registered/attention/test_kda_prefill_cutedsl.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30613 - [AMD] Nightly Test Coverage - Minimax-M3-MXFP8 Accuracy Test

- Link: https://github.com/sgl-project/sglang/pull/30613
- Status/date: merged / 2026-07-26
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`; associated commits `1d0cd2e473e4`
- Diff scope read: GitHub Pull Request files API returned 3 files, +351/-0, 394 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Nightly Test Coverage - Minimax-M3-MXFP8 Accuracy Test"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`; technical summary: Covers "[AMD] Nightly Test Coverage - Minimax-M3-MXFP8 Accuracy Test"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` added +267/-0 (267 lines); hunks: -0,0 +1,267; symbols: ModelConfig, __post_init__, get_display_name, get_answer_value, touching `ModelConfig, __post_init__, get_display_name`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` added +267/-0 (267 lines); hunks: -0,0 +1,267; symbols: ModelConfig, __post_init__, get_display_name, get_answer_value
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py
@@ -0,0 +1,267 @@
+"""MI35x MiniMax-M3 MXFP8 GSM8K Chat+Thinking Evaluation Test (4-GPU, TP=4)
+Tests MiniMax-M3 (MXFP8 checkpoint) with TP=4 on MI35x. MI35x (gfx950 / CDNA4)
+has hardware MX-scaled matmul, so the MXFP8 MoE weights are served natively;
+you still pass `--quantization mxfp8`. Serves with the aiter attention backend,
+fp8 (e4m3) KV cache, and radix cache disabled — validated accuracy-neutral vs
+the bf16-KV / triton-attn baseline (0.972 vs 0.970 on GSM8K chat+thinking).
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` added +267/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31989 - feat: Support nvidia/MiniMax-M3-NVFP4

- Link: https://github.com/sgl-project/sglang/pull/31989
- Status/date: merged / 2026-07-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`; associated commits `a6221d776fe1`
- Diff scope read: GitHub Pull Request files API returned 6 files, +156/-16, 340 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: Support nvidia/MiniMax-M3-NVFP4"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`; technical summary: Covers "feat: Support nvidia/MiniMax-M3-NVFP4"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +18/-0 (18 lines); hunks: -79,6 +79,7; -1418,6 +1419,15 @@ def forward(; symbols: forward, MiniMaxM3SparseForCausalLM, __init__, determine_num_fused_shared_experts, touching `forward, MiniMaxM3SparseForCausalLM, __init__`; `python/sglang/srt/models/minimax_m3_vl.py` modified +18/-0 (18 lines); hunks: -42,6 +42,7; -54,6 +55,15; symbols: MiniMaxM3SparseForConditionalGeneration, __init__, _determine_num_fused_shared_experts, touching `MiniMaxM3SparseForConditionalGeneration, __init__, _determine_num_fused_shared_experts`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +18/-0 (18 lines); hunks: -79,6 +79,7; -1418,6 +1419,15 @@ def forward(; symbols: forward, MiniMaxM3SparseForCausalLM, __init__, determine_num_fused_shared_experts
  - `python/sglang/srt/models/minimax_m3_vl.py` modified +18/-0 (18 lines); hunks: -42,6 +42,7; -54,6 +55,15; symbols: MiniMaxM3SparseForConditionalGeneration, __init__, _determine_num_fused_shared_experts
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -79,6 +79,7 @@
+from sglang.srt.models.utils import WeightsMapper
@@ -1418,6 +1419,15 @@ def forward(
+    hf_to_sglang_mapper = WeightsMapper(
+        orig_to_new_substr={".block_sparse_moe.": ".mlp."}
+    )
+    packed_modules_mapping = {
diff -- python/sglang/srt/models/minimax_m3_vl.py
@@ -42,6 +42,7 @@
+from sglang.srt.models.utils import WeightsMapper
@@ -54,6 +55,15 @@
+    hf_to_sglang_mapper = WeightsMapper(
+        orig_to_new_substr={".block_sparse_moe.": ".mlp."}
+    )
+    packed_modules_mapping = {
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +18/-0; `python/sglang/srt/models/minimax_m3_vl.py` modified +18/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/model_loader/test_modelopt_loader.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30971 - [minimax-m3] fp8 attention GEMMs on SM100 (fp8_e4m3 KV + trtllm_mha)

- Link: https://github.com/sgl-project/sglang/pull/30971
- Status/date: merged / 2026-08-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/utils.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` and 10 files; associated commits `bae8eb8d6caa`
- Diff scope read: GitHub Pull Request files API returned 23 files, +1768/-147, 2889 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[minimax-m3] fp8 attention GEMMs on SM100 (fp8_e4m3 KV + trtllm_mha)"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`; technical summary: Covers "[minimax-m3] fp8 attention GEMMs on SM100 (fp8_e4m3 KV + trtllm_mha)"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` modified +129/-42 (171 lines); hunks: -3,6 +3,14; -11,11 +19,32; symbols: MSAUnavailableError, _check_msa_dtypes, _load_fmha_sm100, msa_sparse_prefill_main, touching `MSAUnavailableError, _check_msa_dtypes, _load_fmha_sm100`; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +73/-9 (82 lines); hunks: -18,19 +18,34; -72,19 +87,26 @@ def __init__(self, runner: ModelRunner):; symbols: _quant_q_fp8, MiniMaxSparseAttnBackend, __init__, touching `_quant_q_fp8, MiniMaxSparseAttnBackend, __init__`; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +36/-0 (36 lines); hunks: -67,6 +67,12 @@ def minimax_sparse_prefill(; -106,6 +112,9 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill, touching `minimax_sparse_prefill`; `python/sglang/kernels/ops/attention/minimax_sparse/common/utils.py` modified +73/-17 (90 lines); hunks: -10,11 +10,14; -25,26 +28,56; symbols: check_sparse_kv_fp8, sparse_out_dtype, unit_scale, _bitonic_merge, touching `check_sparse_kv_fp8, sparse_out_dtype, unit_scale`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` modified +129/-42 (171 lines); hunks: -3,6 +3,14; -11,11 +19,32; symbols: MSAUnavailableError, _check_msa_dtypes, _load_fmha_sm100, msa_sparse_prefill_main
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +73/-9 (82 lines); hunks: -18,19 +18,34; -72,19 +87,26 @@ def __init__(self, runner: ModelRunner):; symbols: _quant_q_fp8, MiniMaxSparseAttnBackend, __init__
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +36/-0 (36 lines); hunks: -67,6 +67,12 @@ def minimax_sparse_prefill(; -106,6 +112,9 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill
  - `python/sglang/kernels/ops/attention/minimax_sparse/common/utils.py` modified +73/-17 (90 lines); hunks: -10,11 +10,14; -25,26 +28,56; symbols: check_sparse_kv_fp8, sparse_out_dtype, unit_scale, _bitonic_merge
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +56/-12 (68 lines); hunks: -8,7 +8,14; -53,6 +60,8 @@ def _decode_score_kernel(; symbols: _decode_score_kernel, _decode_score_attn_kernel
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py
@@ -3,6 +3,14 @@
+#
+# Dtypes: bf16 end-to-end, or uniform fp8_e4m3fn Q/K/V under fp8 attn-GEMM mode
+# (output bf16). fmha_sm100 selects its kernel variant from q.dtype alone and
+# casts k/v pointers to the same element type, so mixed bf16-q/fp8-KV is NOT
+# possible on the cutlass path and e5m2 would silently dispatch the e4m3
+# kernel — `_check_msa_dtypes` enforces uniformity here. The fp8 kernel
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -18,19 +18,34 @@
+from sglang.srt.server_args import m3_fp8_attn_gemm_enabled
+def _quant_q_fp8(q: torch.Tensor, q_scale: Optional[float]) -> torch.Tensor:
+    # Same convention as the KV pools: the fp8 tensor stores value/scale and
+    # the attention kernels multiply the logits back by the scale (None = unit).
+    if q_scale is not None:
+        q = q / q_scale
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -67,6 +67,12 @@ def minimax_sparse_prefill(
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py` modified +129/-42; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +73/-9; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +36/-0; `python/sglang/kernels/ops/attention/minimax_sparse/common/utils.py` modified +73/-17; `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +56/-12; `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +54/-7
- Risk and verification: The diff ships test coverage in `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_msa_fp8_parity.py`, `test/registered/attention/unittests/dense/test_trtllm_mha.py`, `test/registered/unit/test_model_overrides.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #33402 - [AMD] Enable block-fp8 + quick INT4 all-reduce in MiniMax-M3 MI35x nightly Test

- Link: https://github.com/sgl-project/sglang/pull/33402
- Status/date: merged / 2026-08-04
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`; associated commits `eaf5c29cc5a1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +15/-1, 35 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Enable block-fp8 + quick INT4 all-reduce in MiniMax-M3 MI35x nightly Test"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`; technical summary: Covers "[AMD] Enable block-fp8 + quick INT4 all-reduce in MiniMax-M3 MI35x nightly Test"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` modified +15/-1 (16 lines); hunks: -72,12 +72,17 @@ def get_display_name(self) -> str:; -102,6 +107,15 @@ def get_display_name(self) -> str:; symbols: get_display_name, touching `get_display_name`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` modified +15/-1 (16 lines); hunks: -72,12 +72,17 @@ def get_display_name(self) -> str:; -102,6 +107,15 @@ def get_display_name(self) -> str:; symbols: get_display_name
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py
@@ -72,12 +72,17 @@ def get_display_name(self) -> str:
+    # MXFP8 + aiter attn + fp8 KV, with the block-fp8 linear path (PR #32036)
+    # and custom/quick INT4 all-reduce (PR #32230) opted in. Both are opt-in
+    # via env: on gfx950 block convert is not automatic
+    # (mxfp8_block_convert_required() is False), and the M3 overrides otherwise
+    # force --disable-custom-all-reduce.
-        variant="TP4+MXFP8+aiterAttn+fp8KV",
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py` modified +15/-1
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #33962 - enable TRT-LLM for MiniMax M3 by preserving SwiGLU params

- Link: https://github.com/sgl-project/sglang/pull/33962
- Status/date: merged / 2026-08-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`; associated commits `e226bb711c25`
- Diff scope read: GitHub Pull Request files API returned 8 files, +68/-2, 195 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "enable TRT-LLM for MiniMax M3 by preserving SwiGLU params"; model line: MiniMax M2 Series; category: model support/runtime entry; main diff: `python/sglang/srt/models/minimax_m3.py`; technical summary: Covers "enable TRT-LLM for MiniMax M3 by preserving SwiGLU params"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +1/-0 (1 lines); hunks: -323,6 +323,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +1/-0 (1 lines); hunks: -323,6 +323,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -323,6 +323,7 @@ def __init__(
+            gemm1_beta=1.0,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #32941 - [minimax m3][npu]Adaptation of Minimax M3(w8a8) for NPU platforms [1/2]

- Link: https://github.com/sgl-project/sglang/pull/32941
- Status/date: merged / 2026-08-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/minimax_m3_processor.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`, `test/manual/minimax_m3/test_npu_memory_pool.py` and 6 files; associated commits `bca8ed4afc03`
- Diff scope read: GitHub Pull Request files API returned 18 files, +2316/-177, 2962 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[minimax m3][npu]Adaptation of Minimax M3(w8a8) for NPU platforms [1/2]"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`; technical summary: Covers "[minimax m3][npu]Adaptation of Minimax M3(w8a8) for NPU platforms [1/2]"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +1201/-141 (1342 lines); hunks: -1,7 +1,9; -11,21 +13,87; symbols: _native_indexer_enabled, _native_attn_enabled, _kv_cache_to_bnsd, _idx_cache_to_bnsd, touching `_native_indexer_enabled, _native_attn_enabled, _kv_cache_to_bnsd`; `python/sglang/srt/models/minimax_m3.py` modified +115/-17 (132 lines); hunks: -42,7 +42,9; -89,13 +91,15; symbols: build_minimax_fused_qkv_index, MiniMaxM3MLP, _swigluoai_fused, __init__, touching `build_minimax_fused_qkv_index, MiniMaxM3MLP, _swigluoai_fused`; `python/sglang/srt/models/minimax_m3_vl.py` modified +41/-0 (41 lines); hunks: -135,6 +135,9 @@ def __init__(; -197,6 +200,36 @@ def get_video_feature(self, items: List[MultimodalDataItem]...; symbols: __init__, shared_experts_fusion_disable_reason, get_video_feature, get_input_embeddings, touching `__init__, shared_experts_fusion_disable_reason, get_video_feature`; `python/sglang/srt/hardware_backend/npu/modules/minimax_m3_processor.py` added +301/-0 (301 lines); hunks: -0,0 +1,301; symbols: _round_by_factor, _ceil_by_factor, _floor_by_factor, _smart_resize, touching `_round_by_factor, _ceil_by_factor, _floor_by_factor`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +1201/-141 (1342 lines); hunks: -1,7 +1,9; -11,21 +13,87; symbols: _native_indexer_enabled, _native_attn_enabled, _kv_cache_to_bnsd, _idx_cache_to_bnsd
  - `python/sglang/srt/models/minimax_m3.py` modified +115/-17 (132 lines); hunks: -42,7 +42,9; -89,13 +91,15; symbols: build_minimax_fused_qkv_index, MiniMaxM3MLP, _swigluoai_fused, __init__
  - `python/sglang/srt/models/minimax_m3_vl.py` modified +41/-0 (41 lines); hunks: -135,6 +135,9 @@ def __init__(; -197,6 +200,36 @@ def get_video_feature(self, items: List[MultimodalDataItem]...; symbols: __init__, shared_experts_fusion_disable_reason, get_video_feature, get_input_embeddings
  - `python/sglang/srt/hardware_backend/npu/modules/minimax_m3_processor.py` added +301/-0 (301 lines); hunks: -0,0 +1,301; symbols: _round_by_factor, _ceil_by_factor, _floor_by_factor, _smart_resize
  - `test/manual/minimax_m3/test_npu_topk.py` added +193/-0 (193 lines); hunks: -0,0 +1,193; symbols: _install_fake_modules, l1_norm, Recorder, on_select_experts
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -1,7 +1,9 @@
-from typing import TYPE_CHECKING, Optional
+import os
+from types import SimpleNamespace
+from typing import TYPE_CHECKING, Optional, Tuple
@@ -11,21 +13,87 @@
+from sglang.srt.environ import envs
diff -- python/sglang/srt/models/minimax_m3.py
@@ -42,7 +42,9 @@
-from sglang.srt.layers.dp_attention import is_dp_attention_enabled
+from sglang.srt.layers.dp_attention import (
+    is_dp_attention_enabled,
+)
@@ -89,13 +91,15 @@
+    is_npu,
diff -- python/sglang/srt/models/minimax_m3_vl.py
@@ -135,6 +135,9 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +1201/-141; `python/sglang/srt/models/minimax_m3.py` modified +115/-17; `python/sglang/srt/models/minimax_m3_vl.py` modified +41/-0; `python/sglang/srt/hardware_backend/npu/modules/minimax_m3_processor.py` added +301/-0
  - tests: `test/manual/minimax_m3/test_npu_topk.py` added +193/-0; `test/manual/minimax_m3/test_npu_memory_pool.py` added +176/-0
- Risk and verification: The diff ships test coverage in `test/manual/minimax_m3/test_npu_memory_pool.py`, `test/manual/minimax_m3/test_npu_topk.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31956 - Optimize MiniMax-M2.7 on CPU

- Link: https://github.com/sgl-project/sglang/pull/31956
- Status/date: merged / 2026-08-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `3f6ef01322ca`
- Diff scope read: GitHub Pull Request files API returned 8 files, +687/-72, 979 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Optimize MiniMax-M2.7 on CPU"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "Optimize MiniMax-M2.7 on CPU"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +20/-4 (24 lines); hunks: -482,10 +482,26 @@ def _forward_fused(self, q: torch.Tensor, k: torch.Tensor):; symbols: _forward_fused, _forward_cpu, MiniMaxM2MoE, touching `_forward_fused, _forward_cpu, MiniMaxM2MoE`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +20/-4 (24 lines); hunks: -482,10 +482,26 @@ def _forward_fused(self, q: torch.Tensor, k: torch.Tensor):; symbols: _forward_fused, _forward_cpu, MiniMaxM2MoE
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -482,10 +482,26 @@ def _forward_fused(self, q: torch.Tensor, k: torch.Tensor):
-        # TODO: add c++ kernel for cpu
-        q = self._q_norm(q.contiguous())
-        k = self._k_norm(k.contiguous())
-        return q, k
+        if self._world_size > 1:
+            sum_sq = torch.ops.sgl_kernel.fused_qk_rmsnorm_sumsq_cpu(q, k)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +20/-4
- Risk and verification: The diff ships test coverage in `test/registered/cpu/test_norm.py`, `test/registered/cpu/test_topk.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #34542 - [MiniMax-M3] Overlap shared and routed experts

- Link: https://github.com/sgl-project/sglang/pull/34542
- Status/date: merged / 2026-08-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`; associated commits `c939307e8aaa`
- Diff scope read: GitHub Pull Request files API returned 1 files, +29/-6, 102 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MiniMax-M3] Overlap shared and routed experts"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/models/minimax_m3.py`; technical summary: Covers "[MiniMax-M3] Overlap shared and routed experts"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +29/-6 (35 lines); hunks: -79,13 +79,14; -312,10 +313,12 @@ def __init__(; symbols: __init__, forward_normal, _forward_router_experts, forward_deepep, touching `__init__, forward_normal, _forward_router_experts`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +29/-6 (35 lines); hunks: -79,13 +79,14; -312,10 +313,12 @@ def __init__(; symbols: __init__, forward_normal, _forward_router_experts, forward_deepep
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -79,13 +79,14 @@
+from sglang.srt.model_executor.runner import get_is_capture_mode
-from sglang.srt.runtime_context import get_exec, get_parallel
+from sglang.srt.runtime_context import get_exec, get_parallel, get_stream
@@ -312,10 +313,12 @@ def __init__(
+        alt_stream: Optional[torch.cuda.Stream] = None,
+        self.alt_stream = alt_stream
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +29/-6
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #32099 - [AMD] MiniMax-M3 : Fuse QKV+index proj for block-fp8

- Link: https://github.com/sgl-project/sglang/pull/32099
- Status/date: merged / 2026-08-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`; associated commits `f7101b0ae626`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-8, 34 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] MiniMax-M3 : Fuse QKV+index proj for block-fp8"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m3.py`; technical summary: Covers "[AMD] MiniMax-M3 : Fuse QKV+index proj for block-fp8"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +12/-8 (20 lines); hunks: -194,9 +194,18 @@ def __init__(; -819,11 +828,6 @@ def maybe_build_fused_qkv_index(self) -> None:; symbols: __init__, forward, maybe_build_fused_qkv_index, touching `__init__, forward, maybe_build_fused_qkv_index`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +12/-8 (20 lines); hunks: -194,9 +194,18 @@ def __init__(; -819,11 +828,6 @@ def maybe_build_fused_qkv_index(self) -> None:; symbols: __init__, forward, maybe_build_fused_qkv_index
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -194,9 +194,18 @@ def __init__(
-            # Must derive the backend scale layout here: the loader skips this
-            # module (see ``_qm``), so it won't run process_weights_after_loading.
-            quant_method._process_mxfp8_linear_weight_scale(self)
+            # The loader skips this module (see ``_qm``), so run the weight
+            # post-process here instead of process_weights_after_loading.
+            if getattr(quant_method, "convert_mxfp8_to_block", False):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +12/-8
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36142 - [AMD][CI] Add MiniMax-M3-MXFP8 MI35x nightly perf benchmark

- Link: https://github.com/sgl-project/sglang/pull/36142
- Status/date: merged / 2026-08-25
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py`; associated commits `6569125e3ad9`
- Diff scope read: GitHub Pull Request files API returned 2 files, +164/-47, 261 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD][CI] Add MiniMax-M3-MXFP8 MI35x nightly perf benchmark"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py`; technical summary: Covers "[AMD][CI] Add MiniMax-M3-MXFP8 MI35x nightly perf benchmark"; the main implementation surface is `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: TestNightlyMiniMaxM3PerformanceMI35x, setUpClass, test_bench_minimax_m3, touching `TestNightlyMiniMaxM3PerformanceMI35x, setUpClass, test_bench_minimax_m3`.
- Code diff details:
  - `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: TestNightlyMiniMaxM3PerformanceMI35x, setUpClass, test_bench_minimax_m3
- Key code excerpts:

```diff
diff -- test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py
@@ -0,0 +1,151 @@
+"""MI35x nightly performance benchmark for MiniMax-M3-MXFP8 (4-GPU, TP=4).
+Benchmarks MiniMaxAI/MiniMax-M3-MXFP8 with the same TP=4 recipe the MI35x
+accuracy test validated (aiter attention, fp8 e4m3 KV, block-fp8 linear path,
+quick INT4 all-reduce), so a throughput regression cannot be confused with a
+configuration difference. MI35x (gfx950 / CDNA4) has hardware MX-scaled matmul,
+so the MXFP8 MoE weights are served natively.
```

- Reviewed files:
  - tests: `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py` added +151/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #35290 - [XPU] Lazily import tvm_ffi-dependent all_reduce kernel in minimax_m2

- Link: https://github.com/sgl-project/sglang/pull/35290
- Status/date: merged / 2026-08-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m2.py`; associated commits `9cee0a31d1a7`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-4, 33 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[XPU] Lazily import tvm_ffi-dependent all_reduce kernel in minimax_m2"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/models/minimax_m2.py`; technical summary: Covers "[XPU] Lazily import tvm_ffi-dependent all_reduce kernel in minimax_m2"; the main implementation surface is `python/sglang/srt/models/minimax_m2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m2.py` modified +8/-4 (12 lines); hunks: -27,10 +27,6; -103,6 +99,7.
- Code diff details:
  - `python/sglang/srt/models/minimax_m2.py` modified +8/-4 (12 lines); hunks: -27,10 +27,6; -103,6 +99,7
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m2.py
@@ -27,10 +27,6 @@
-from sglang.kernels.ops.communication.all_reduce import (
-    fused_parallel_qknorm,
-    get_fused_parallel_qknorm_max_occupancy,
-)
@@ -103,6 +99,7 @@
+    is_xpu,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m2.py` modified +8/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/minimax_m2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36527 - MiniMax-M3: share the sparse index top-k across layers and reuse the decode top-k buffer

- Link: https://github.com/sgl-project/sglang/pull/36527
- Status/date: merged / 2026-09-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`; associated commits `a25bbca8edfa`
- Diff scope read: GitHub Pull Request files API returned 4 files, +318/-88, 571 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "MiniMax-M3: share the sparse index top-k across layers and reuse the decode top-k buffer"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`; technical summary: Covers "MiniMax-M3: share the sparse index top-k across layers and reuse the decode top-k buffer"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +109/-61 (170 lines); hunks: -73,9 +73,18 @@ def minimax_sparse_prefill(; -88,42 +97,52 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill, minimax_sparse_decode, touching `minimax_sparse_prefill, minimax_sparse_decode`; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +154/-15 (169 lines); hunks: -19,14 +19,15; -147,6 +148,12 @@ def __init__(self, runner: ModelRunner):; symbols: __init__, init_forward_metadata_out_graph, forward_extend, touching `__init__, init_forward_metadata_out_graph, forward_extend`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +47/-12 (59 lines); hunks: -18,29 +18,63; -228,6 +262,7 @@ def _decode_score_kernel(; symbols: _prune_decode_configs, _decode_score_block_n, _decode_score_kernel, _decode_score_attn_kernel, touching `_prune_decode_configs, _decode_score_block_n, _decode_score_kernel`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +109/-61 (170 lines); hunks: -73,9 +73,18 @@ def minimax_sparse_prefill(; -88,42 +97,52 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill, minimax_sparse_decode
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +154/-15 (169 lines); hunks: -19,14 +19,15; -147,6 +148,12 @@ def __init__(self, runner: ModelRunner):; symbols: __init__, init_forward_metadata_out_graph, forward_extend
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +47/-12 (59 lines); hunks: -18,29 +18,63; -228,6 +262,7 @@ def _decode_score_kernel(; symbols: _prune_decode_configs, _decode_score_block_n, _decode_score_kernel, _decode_score_attn_kernel
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -73,9 +73,18 @@ def minimax_sparse_prefill(
+    cached_topk_idx: Optional[torch.Tensor] = None,
+    return_topk_idx: bool = False,
+    Index cache: when ``cached_topk_idx`` is given, skip Step 1
+    (the flash-index attention + top-k selection) and reuse the provided top-k
+    indices for Step 3's sparse attention. When ``return_topk_idx`` is True, the
+    reduced top-k tensor is returned as a third element so the caller can cache
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -19,14 +19,15 @@
+from sglang.srt.layers.moe.utils import is_tbo_enabled
-from sglang.srt.utils import is_npu
+from sglang.srt.utils import is_gfx95_supported, is_hip, is_npu
@@ -147,6 +148,12 @@ def __init__(self, runner: ModelRunner):
+        # (owning ForwardBatch, cu_seqlens, seq_lens, prefix_lens, cu_seqblocks_q,
+        # max_seqblock_q, all_seqblock_q). The owner is part of the key because one
diff -- python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py
@@ -18,29 +18,63 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +109/-61; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +154/-15; `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +47/-12
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36557 - MiniMax-M3: Triton split-K router GEMV with in-kernel fixup

- Link: https://github.com/sgl-project/sglang/pull/36557
- Status/date: merged / 2026-09-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`; associated commits `5177a3ec0854`
- Diff scope read: GitHub Pull Request files API returned 2 files, +189/-0, 213 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "MiniMax-M3: Triton split-K router GEMV with in-kernel fixup"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m3.py`; technical summary: Covers "MiniMax-M3: Triton split-K router GEMV with in-kernel fixup"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +14/-0 (14 lines); hunks: -91,6 +91,7; -101,8 +102,17; symbols: forward_deepep, _compute_router_logits, touching `forward_deepep, _compute_router_logits`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +14/-0 (14 lines); hunks: -91,6 +91,7; -101,8 +102,17; symbols: forward_deepep, _compute_router_logits
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -91,6 +91,7 @@
+    is_gfx95_supported,
@@ -101,8 +102,17 @@
+_is_gfx95_supported = _is_hip and is_gfx95_supported()
+if _is_gfx95_supported:
+    from sglang.kernels.ops.gemm.router_gemv import (
+        router_gemv,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +14/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/ops/gemm/router_gemv.py`, `python/sglang/srt/models/minimax_m3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37254 - [AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj

- Link: https://github.com/sgl-project/sglang/pull/37254
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`; associated commits `7c195b915162`
- Diff scope read: GitHub Pull Request files API returned 3 files, +54/-3, 81 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`; technical summary: Covers "[AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +2/-1 (3 lines); hunks: -1559,7 +1559,8 @@ class MiniMaxM3SparseForCausalLM(nn.Module):; symbols: MiniMaxM3SparseForCausalLM, touching `MiniMaxM3SparseForCausalLM`; `python/sglang/srt/models/minimax_m3_vl.py` modified +2/-1 (3 lines); hunks: -63,7 +63,8 @@ class MiniMaxM3SparseForConditionalGeneration(nn.Module):; symbols: MiniMaxM3SparseForConditionalGeneration, touching `MiniMaxM3SparseForConditionalGeneration`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +2/-1 (3 lines); hunks: -1559,7 +1559,8 @@ class MiniMaxM3SparseForCausalLM(nn.Module):; symbols: MiniMaxM3SparseForCausalLM
  - `python/sglang/srt/models/minimax_m3_vl.py` modified +2/-1 (3 lines); hunks: -63,7 +63,8 @@ class MiniMaxM3SparseForConditionalGeneration(nn.Module):; symbols: MiniMaxM3SparseForConditionalGeneration
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -1559,7 +1559,8 @@ class MiniMaxM3SparseForCausalLM(nn.Module):
-        "index_qkv_proj": ["index_q_proj", "index_k_proj", "index_v_proj"],
+        # no index_v_proj in the M3 checkpoint
+        "index_qkv_proj": ["index_q_proj", "index_k_proj"],
diff -- python/sglang/srt/models/minimax_m3_vl.py
@@ -63,7 +63,8 @@ class MiniMaxM3SparseForConditionalGeneration(nn.Module):
-        "index_qkv_proj": ["index_q_proj", "index_k_proj", "index_v_proj"],
+        # no index_v_proj in the M3 checkpoint
+        "index_qkv_proj": ["index_q_proj", "index_k_proj"],
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +2/-1; `python/sglang/srt/models/minimax_m3_vl.py` modified +2/-1
- Risk and verification: The diff ships test coverage in `test/registered/unit/layers/quantization/test_quark_utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36576 - MiniMax-M3: allow shared-experts fusion on ROCm gfx942 and newer

- Link: https://github.com/sgl-project/sglang/pull/36576
- Status/date: merged / 2026-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`; associated commits `241a5b982373`
- Diff scope read: GitHub Pull Request files API returned 3 files, +21/-7, 67 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "MiniMax-M3: allow shared-experts fusion on ROCm gfx942 and newer"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/models/minimax_m3_vl.py`, `python/sglang/srt/models/minimax_m3.py`; technical summary: Covers "MiniMax-M3: allow shared-experts fusion on ROCm gfx942 and newer"; the main implementation surface is `python/sglang/srt/models/minimax_m3_vl.py`, `python/sglang/srt/models/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3_vl.py` modified +15/-4 (19 lines); hunks: -47,13 +47,22; -152,10 +161,12 @@ def shared_experts_fusion_disable_reason(cls, hf_config, q...; symbols: shared_experts_fusion_disable_reason, touching `shared_experts_fusion_disable_reason`; `python/sglang/srt/models/minimax_m3.py` modified +4/-2 (6 lines); hunks: -1612,10 +1612,12 @@ def shared_experts_fusion_disable_reason(cls, hf_config,...; symbols: shared_experts_fusion_disable_reason, touching `shared_experts_fusion_disable_reason`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3_vl.py` modified +15/-4 (19 lines); hunks: -47,13 +47,22; -152,10 +161,12 @@ def shared_experts_fusion_disable_reason(cls, hf_config, q...; symbols: shared_experts_fusion_disable_reason
  - `python/sglang/srt/models/minimax_m3.py` modified +4/-2 (6 lines); hunks: -1612,10 +1612,12 @@ def shared_experts_fusion_disable_reason(cls, hf_config,...; symbols: shared_experts_fusion_disable_reason
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3_vl.py
@@ -47,13 +47,22 @@
-from sglang.srt.utils import add_prefix, get_device_sm, is_cuda, log_info_on_rank0
+from sglang.srt.utils import (
+    add_prefix,
+    get_device_sm,
+    is_cuda,
+    is_gfx95_supported,
diff -- python/sglang/srt/models/minimax_m3.py
@@ -1612,10 +1612,12 @@ def shared_experts_fusion_disable_reason(cls, hf_config, quant_config):
-        if not _is_cuda:
-            return "Shared experts fusion currently requires CUDA devices."
+        if not (_is_cuda or _is_hip):
+            return "Shared experts fusion currently requires CUDA or ROCm devices."
+        if _is_hip and not _is_gfx95_supported:
+            return "Shared experts fusion on ROCm is validated on gfx950 only."
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3_vl.py` modified +15/-4; `python/sglang/srt/models/minimax_m3.py` modified +4/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31446 - [HiSparse] Add MHA hisparse support for MiniMax M3

- Link: https://github.com/sgl-project/sglang/pull/31446
- Status/date: merged / 2026-09-22
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` and 7 files; associated commits `04c0913434c4`
- Diff scope read: GitHub Pull Request files API returned 27 files, +1017/-118, 2089 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[HiSparse] Add MHA hisparse support for MiniMax M3"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py`; technical summary: Covers "[HiSparse] Add MHA hisparse support for MiniMax M3"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +44/-0 (44 lines); hunks: -116,6 +116,7 @@ def __init__(self, runner: ModelRunner):; -176,6 +177,18 @@ def __init__(self, runner: ModelRunner):; symbols: __init__, touching `__init__`; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +11/-2 (13 lines); hunks: -75,6 +75,7 @@ def minimax_sparse_prefill(; -146,7 +147,7 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill, minimax_sparse_decode, touching `minimax_sparse_prefill, minimax_sparse_decode`; `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` modified +58/-2 (60 lines); hunks: -1,14 +1,23; -26,10 +35,11 @@ def _make_k_only_pool(start_layer: int = 0) -> MiniMaxSparse...; symbols: _make_k_only_pool, TestMiniMaxSparsePoolPD, touching `_make_k_only_pool, TestMiniMaxSparsePoolPD`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +27/-6 (33 lines); hunks: -23,6 +23,7; -43,6 +44,7 @@ def _gqa_share_sparse_decode_kernel(; symbols: _gqa_share_sparse_decode_kernel, flash_decode_with_gqa_share_sparse, touching `_gqa_share_sparse_decode_kernel, flash_decode_with_gqa_share_sparse`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +44/-0 (44 lines); hunks: -116,6 +116,7 @@ def __init__(self, runner: ModelRunner):; -176,6 +177,18 @@ def __init__(self, runner: ModelRunner):; symbols: __init__
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +11/-2 (13 lines); hunks: -75,6 +75,7 @@ def minimax_sparse_prefill(; -146,7 +147,7 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill, minimax_sparse_decode
  - `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` modified +58/-2 (60 lines); hunks: -1,14 +1,23; -26,10 +35,11 @@ def _make_k_only_pool(start_layer: int = 0) -> MiniMaxSparse...; symbols: _make_k_only_pool, TestMiniMaxSparsePoolPD
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +27/-6 (33 lines); hunks: -23,6 +23,7; -43,6 +44,7 @@ def _gqa_share_sparse_decode_kernel(; symbols: _gqa_share_sparse_decode_kernel, flash_decode_with_gqa_share_sparse
  - `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` modified +11/-0 (11 lines); hunks: -28,6 +28,7; -55,6 +56,7 @@ def _gqa_share_sparse_fwd_kernel(; symbols: _gqa_share_sparse_fwd_kernel, flash_prefill_with_gqa_share_sparse
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -116,6 +116,7 @@ def __init__(self, runner: ModelRunner):
+        self.hisparse_coordinator = runner.hisparse_coordinator
@@ -176,6 +177,18 @@ def __init__(self, runner: ModelRunner):
+        if self.hisparse_coordinator is not None:
+            selected_tokens = self.topk_blocks * self.block_size_k
+            assert selected_tokens <= self.hisparse_coordinator.device_buffer_size, (
+                f"MiniMax M3 selects {selected_tokens} sparse-attention tokens, "
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -75,6 +75,7 @@ def minimax_sparse_prefill(
+    loc_mapping: Optional[torch.Tensor] = None,
@@ -146,7 +147,7 @@ def minimax_sparse_prefill(
-    if use_msa and sink is None:
+    if use_msa and sink is None and loc_mapping is None:
@@ -188,6 +189,7 @@ def minimax_sparse_prefill(
+                loc_mapping=loc_mapping,
diff -- test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py
@@ -1,14 +1,23 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +44/-0; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +11/-2; `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +27/-6; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` modified +11/-0
  - tests: `test/registered/unit/mem_cache/test_minimax_sparse_pool_pd_unit.py` modified +58/-2; `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py` modified +8/-3
  - docs: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` modified +1/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/kvcache/test_hisparse.py`, `test/registered/unit/disaggregation/test_minimax_sparse_disagg_state_kv_args.py`, `test/registered/unit/disaggregation/test_mooncake_transfer_batching.py`, `test/registered/unit/mem_cache/test_hisparse_allocator.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36546 - MiniMax-M3: run the sparse prefill main attention through AITER Gluon paged attention

- Link: https://github.com/sgl-project/sglang/pull/36546
- Status/date: merged / 2026-09-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`; associated commits `4fa2c9c1de7b`
- Diff scope read: GitHub Pull Request files API returned 6 files, +966/-122, 1244 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "MiniMax-M3: run the sparse prefill main attention through AITER Gluon paged attention"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py`; technical summary: Covers "MiniMax-M3: run the sparse prefill main attention through AITER Gluon paged attention"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +72/-5 (77 lines); hunks: -19,9 +19,14; -35,6 +40,18 @@ def _warn_msa_fallback(err: Exception) -> None:; symbols: _warn_msa_fallback, _warn_gluon_fallback, minimax_sparse_prefill, touching `_warn_msa_fallback, _warn_gluon_fallback, minimax_sparse_prefill`; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +2/-0 (2 lines); hunks: -1570,6 +1570,7 @@ def forward_extend(; -1579,6 +1580,7 @@ def forward_extend(; symbols: forward_extend, touching `forward_extend`; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` modified +230/-45 (275 lines); hunks: -6,6 +6,8; -16,6 +18,9; symbols: _topk_index_kernel, _index_block_score_only_kernel, flash_prefill_with_topk_index, touching `_topk_index_kernel, _index_block_score_only_kernel, flash_prefill_with_topk_index`; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` modified +167/-72 (239 lines); hunks: -6,6 +6,8; -15,6 +17,11; symbols: _sparse_subk, _gqa_share_sparse_fwd_kernel, flash_prefill_with_gqa_share_sparse, touching `_sparse_subk, _gqa_share_sparse_fwd_kernel, flash_prefill_with_gqa_share_sparse`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +72/-5 (77 lines); hunks: -19,9 +19,14; -35,6 +40,18 @@ def _warn_msa_fallback(err: Exception) -> None:; symbols: _warn_msa_fallback, _warn_gluon_fallback, minimax_sparse_prefill
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +2/-0 (2 lines); hunks: -1570,6 +1570,7 @@ def forward_extend(; -1579,6 +1580,7 @@ def forward_extend(; symbols: forward_extend
  - `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` modified +230/-45 (275 lines); hunks: -6,6 +6,8; -16,6 +18,9; symbols: _topk_index_kernel, _index_block_score_only_kernel, flash_prefill_with_topk_index
  - `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` modified +167/-72 (239 lines); hunks: -6,6 +6,8; -15,6 +17,11; symbols: _sparse_subk, _gqa_share_sparse_fwd_kernel, flash_prefill_with_gqa_share_sparse
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -19,9 +19,14 @@
+from sglang.srt.environ import envs
+from sglang.srt.utils import is_gfx95_supported, is_hip
+_use_aiter_gfx95 = envs.SGLANG_USE_AITER.get() and is_hip() and is_gfx95_supported()
+_gluon_fallback_warned = False
@@ -35,6 +40,18 @@ def _warn_msa_fallback(err: Exception) -> None:
+def _warn_gluon_fallback(msg: str) -> None:
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -1570,6 +1570,7 @@ def forward_extend(
+                seq_lens_cpu=forward_batch.seq_lens_cpu,
@@ -1579,6 +1580,7 @@ def forward_extend(
+                page_size=self.page_size,
diff -- python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py
@@ -6,6 +6,8 @@
+from sglang.srt.utils import is_gfx95_supported
@@ -16,6 +18,9 @@
+# gfx950 MI350X: per-page wins at <=2 pages/block, loses at >=8
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +72/-5; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +2/-0; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` modified +230/-45; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` modified +167/-72
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py`, `python/sglang/srt/environ.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36560 - MiniMax-M3: wave64 histogram-select decode top-k, and raise kMaxNumBlocks for CUDA graphs

- Link: https://github.com/sgl-project/sglang/pull/36560
- Status/date: merged / 2026-09-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`; associated commits `f2a1366584e1`
- Diff scope read: GitHub Pull Request files API returned 4 files, +378/-18, 548 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "MiniMax-M3: wave64 histogram-select decode top-k, and raise kMaxNumBlocks for CUDA graphs"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`; technical summary: Covers "MiniMax-M3: wave64 histogram-select decode top-k, and raise kMaxNumBlocks for CUDA graphs"; the main implementation surface is `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +362/-16 (378 lines); hunks: -29,17 +29,34 @@ namespace sglang {; -50,14 +67,268 @@ struct TopKTrait {; `python/sglang/kernels/ops/attention/minimax_decode_topk.py` modified +9/-0 (9 lines); hunks: -29,6 +29,9; -59,6 +62,9 @@ def minimax_decode_topk(; symbols: _jit_module, minimax_decode_topk, minimax_decode_topk_page_table, touching `_jit_module, minimax_decode_topk, minimax_decode_topk_page_table`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +4/-1 (5 lines); hunks: -18,6 +18,9; -896,7 +899,7 @@ def flash_decode_with_topk_idx(; symbols: _prune_decode_configs, flash_decode_with_topk_idx, touching `_prune_decode_configs, flash_decode_with_topk_idx`; `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +3/-1 (4 lines); hunks: -64,7 +64,9 @@ def _check_contract(out, seq_lens, block_size, topk, S):; symbols: _check_contract, test_decode_topk_distinct, touching `_check_contract, test_decode_topk_distinct`.
- Code diff details:
  - `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +362/-16 (378 lines); hunks: -29,17 +29,34 @@ namespace sglang {; -50,14 +67,268 @@ struct TopKTrait {
  - `python/sglang/kernels/ops/attention/minimax_decode_topk.py` modified +9/-0 (9 lines); hunks: -29,6 +29,9; -59,6 +62,9 @@ def minimax_decode_topk(; symbols: _jit_module, minimax_decode_topk, minimax_decode_topk_page_table
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +4/-1 (5 lines); hunks: -18,6 +18,9; -896,7 +899,7 @@ def flash_decode_with_topk_idx(; symbols: _prune_decode_configs, flash_decode_with_topk_idx
  - `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +3/-1 (4 lines); hunks: -64,7 +64,9 @@ def _check_contract(out, seq_lens, block_size, topk, S):; symbols: _check_contract, test_decode_topk_distinct
- Key code excerpts:

```diff
diff -- python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh
@@ -29,17 +29,34 @@ namespace sglang {
-struct TopKTrait {
+//
+// On ROCm every regime is replaced by rocm_hist_select over a packed
+// (score, ~id) u64 total order: one coarse histogram round (256 bins for
+// n <= 1024, else 2048), 11-bit refine rounds while > kRocmCap candidates
+// remain, then a wave-0 bitonic-sort finish.
diff -- python/sglang/kernels/ops/attention/minimax_decode_topk.py
@@ -29,6 +29,9 @@
+# Must match TopKTrait::kMaxNumBlocks in minimax_decode_topk.cuh.
+_MAX_NUM_BLOCKS = 16384 if torch.version.hip else 4096
@@ -59,6 +62,9 @@ def minimax_decode_topk(
+    assert max_seqblock <= _MAX_NUM_BLOCKS, (
+        f"max_seqblock={max_seqblock} exceeds kMaxNumBlocks={_MAX_NUM_BLOCKS}"
+    )
diff -- python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py
@@ -18,6 +18,9 @@
```

- Reviewed files:
  - runtime: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +362/-16; `python/sglang/kernels/ops/attention/minimax_decode_topk.py` modified +9/-0; `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +4/-1
  - tests: `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +3/-1
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36549 - MiniMax-M3: allocate the lightning-indexer K cache in fp8 on gfx95

- Link: https://github.com/sgl-project/sglang/pull/36549
- Status/date: merged / 2026-09-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`; associated commits `ec75d3d30f02`
- Diff scope read: GitHub Pull Request files API returned 5 files, +46/-11, 134 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "MiniMax-M3: allocate the lightning-indexer K cache in fp8 on gfx95"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`; technical summary: Covers "MiniMax-M3: allocate the lightning-indexer K cache in fp8 on gfx95"; the main implementation surface is `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` modified +6/-1 (7 lines); hunks: -556,7 +556,12 @@ def _sparse_qk_index_gemma_rmsnorm_rope_cache_kernel(; symbols: _sparse_qk_index_gemma_rmsnorm_rope_cache_kernel, sparse_qk_index_gemma_rmsnorm_rope_cache, touching `_sparse_qk_index_gemma_rmsnorm_rope_cache_kernel, sparse_qk_index_gemma_rmsnorm_rope_cache`.
- Code diff details:
  - `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` modified +6/-1 (7 lines); hunks: -556,7 +556,12 @@ def _sparse_qk_index_gemma_rmsnorm_rope_cache_kernel(; symbols: _sparse_qk_index_gemma_rmsnorm_rope_cache_kernel, sparse_qk_index_gemma_rmsnorm_rope_cache
- Key code excerpts:

```diff
diff -- python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py
@@ -556,7 +556,12 @@ def _sparse_qk_index_gemma_rmsnorm_rope_cache_kernel(
-    tl.store(idx_cache_base, out_typed, mask=mask & is_idx_k)
+    # cast fp32 straight to the cache dtype (fp8 on gfx95) to avoid rounding twice via bf16
+    tl.store(
+        idx_cache_base,
+        out.to(idx_k_cache_ptr.dtype.element_ty),
+        mask=mask & is_idx_k,
```

- Reviewed files:
  - runtime: `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` modified +6/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41198 - [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit

- Link: https://github.com/sgl-project/sglang/pull/41198
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`; associated commits `b7f6d04a9af1`
- Diff scope read: GitHub Pull Request files API returned 6 files, +50/-219, 402 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/models/minimax_m3.py`; technical summary: Covers "[Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +9/-31 (40 lines); hunks: -39,7 +39,6; -1395,36 +1394,15 @@ def forward(; symbols: forward, MiniMaxM3Model, touching `forward, MiniMaxM3Model`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +9/-31 (40 lines); hunks: -39,7 +39,6; -1395,36 +1394,15 @@ def forward(; symbols: forward, MiniMaxM3Model
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -39,7 +39,6 @@
-    UnreducedOutput,
@@ -1395,36 +1394,15 @@ def forward(
-        should_allreduce_fusion = (
-            self.layer_communicator.should_fuse_mlp_allreduce_with_next_layer(
-                forward_batch
-            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +9/-31
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41497 - [AMD] Fix MiniMax-M3 EAGLE3 verification on ROCm

- Link: https://github.com/sgl-project/sglang/pull/41497
- Status/date: merged / 2026-10-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `test/registered/amd/test_minimax_rocm_verify.py`; associated commits `0148d9a2fd0f`
- Diff scope read: GitHub Pull Request files API returned 2 files, +186/-2, 253 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Fix MiniMax-M3 EAGLE3 verification on ROCm"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `test/registered/amd/test_minimax_rocm_verify.py`; technical summary: Covers "[AMD] Fix MiniMax-M3 EAGLE3 verification on ROCm"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `test/registered/amd/test_minimax_rocm_verify.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +59/-2 (61 lines); hunks: -1,5 +1,6; -115,6 +116,7 @@ class MiniMaxSparseAttnBackend(AttentionBackend):; symbols: MiniMaxSparseAttnBackend, __init__, init_forward_metadata_out_graph, touching `MiniMaxSparseAttnBackend, __init__, init_forward_metadata_out_graph`; `test/registered/amd/test_minimax_rocm_verify.py` added +127/-0 (127 lines); hunks: -0,0 +1,127; symbols: TestMiniMaxROCmVerify, setUp, decode, run_verify, touching `TestMiniMaxROCmVerify, setUp, decode`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +59/-2 (61 lines); hunks: -1,5 +1,6; -115,6 +116,7 @@ class MiniMaxSparseAttnBackend(AttentionBackend):; symbols: MiniMaxSparseAttnBackend, __init__, init_forward_metadata_out_graph
  - `test/registered/amd/test_minimax_rocm_verify.py` added +127/-0 (127 lines); hunks: -0,0 +1,127; symbols: TestMiniMaxROCmVerify, setUp, decode, run_verify
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -1,5 +1,6 @@
+import copy
@@ -115,6 +116,7 @@ class MiniMaxSparseAttnBackend(AttentionBackend):
+        self.is_hip = is_hip()
@@ -159,6 +161,7 @@ def __init__(self, runner: ModelRunner):
+        self._linear_verify_meta: Optional[SimpleNamespace] = None
@@ -274,6 +277,12 @@ def __init__(self, runner: ModelRunner):
diff -- test/registered/amd/test_minimax_rocm_verify.py
@@ -0,0 +1,127 @@
+"""Causal verify metadata and routing with no ordinary prefill metadata."""
+import unittest
+from types import SimpleNamespace
+import torch
+from sglang.test.ci.ci_register import register_amd_ci
+register_amd_ci(est_time=15, suite="stage-b-test-1-gpu-small-amd")
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +59/-2
  - tests: `test/registered/amd/test_minimax_rocm_verify.py` added +127/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_minimax_rocm_verify.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41488 - [AMD] Add opt-in MiniMax-M3 TP4 indexer context partitioning

- Link: https://github.com/sgl-project/sglang/pull/41488
- Status/date: merged / 2026-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/amd/test_minimax_indexer_cp.py` and 6 files; associated commits `b69a5f296ae7`
- Diff scope read: GitHub Pull Request files API returned 7 files, +686/-0, 725 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add opt-in MiniMax-M3 TP4 indexer context partitioning"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`; technical summary: Covers "[AMD] Add opt-in MiniMax-M3 TP4 indexer context partitioning"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` added +201/-0 (201 lines); hunks: -0,0 +1,201; symbols: unsupported_reason, draft_is_chain_layout, make_indexer_cp, MiniMaxIndexerCP, touching `unsupported_reason, draft_is_chain_layout, make_indexer_cp`; `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: TestMiniMaxIndexerCPGate, test_only_validated_draft_layouts_enable_cp, touching `TestMiniMaxIndexerCPGate, test_only_validated_draft_layouts_enable_cp`; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +26/-0 (26 lines); hunks: -326,6 +326,7 @@ def minimax_sparse_decode(; -338,6 +339,31 @@ def minimax_sparse_decode(; symbols: minimax_sparse_decode, touching `minimax_sparse_decode`; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +7/-0 (7 lines); hunks: -339,6 +339,12 @@ def __init__(self, runner: ModelRunner):; -1836,6 +1842,7 @@ def hisparse_swap_in_fn(topk_idx):; symbols: __init__, hisparse_swap_in_fn, touching `__init__, hisparse_swap_in_fn`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` added +201/-0 (201 lines); hunks: -0,0 +1,201; symbols: unsupported_reason, draft_is_chain_layout, make_indexer_cp, MiniMaxIndexerCP
  - `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: TestMiniMaxIndexerCPGate, test_only_validated_draft_layouts_enable_cp
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +26/-0 (26 lines); hunks: -326,6 +326,7 @@ def minimax_sparse_decode(; -338,6 +339,31 @@ def minimax_sparse_decode(; symbols: minimax_sparse_decode
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +7/-0 (7 lines); hunks: -339,6 +339,12 @@ def __init__(self, runner: ModelRunner):; -1836,6 +1842,7 @@ def hisparse_swap_in_fn(topk_idx):; symbols: __init__, hisparse_swap_in_fn
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py` added +270/-0 (270 lines); hunks: -0,0 +1,270; symbols: _score_shard, _pack, _local_candidates, _merge_candidates
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py
@@ -0,0 +1,201 @@
+"""Opt-in, decode-only context partitioning of MiniMax's replicated index K.
+This first implementation gathers the existing post-RoPE index queries rather
+than changing checkpoint loading or fused projections. Both gathers go through
+SGLang's communicator so AITER registration and graph capture remain owned by
+the runtime. Communication cost must be included in performance comparisons.
+"""
diff -- test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py
@@ -0,0 +1,61 @@
+import unittest
+from sglang.srt.layers.attention.minimax_sparse_ops.indexer_cp import (
+    draft_is_chain_layout,
+    unsupported_reason,
+)
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -326,6 +326,7 @@ def minimax_sparse_decode(
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` added +201/-0; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +26/-0; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +7/-0; `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py` added +270/-0
  - tests: `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py` added +61/-0; `test/registered/amd/test_minimax_indexer_cp.py` added +118/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_minimax_indexer_cp.py`, `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41707 - [AMD] Use AITER ASM prefill for MiniMax-M3 HD128 attention

- Link: https://github.com/sgl-project/sglang/pull/41707
- Status/date: merged / 2026-10-04
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/test_minimax_hd128_asm_prefill.py`; associated commits `71dc292b9702`
- Diff scope read: GitHub Pull Request files API returned 3 files, +211/-0, 226 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Use AITER ASM prefill for MiniMax-M3 HD128 attention"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `test/registered/amd/test_minimax_hd128_asm_prefill.py`; technical summary: Covers "[AMD] Use AITER ASM prefill for MiniMax-M3 HD128 attention"; the main implementation surface is `test/registered/amd/test_minimax_hd128_asm_prefill.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/test_minimax_hd128_asm_prefill.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: TestMiniMaxHD128AsmPrefill, setUpClass, exercise, test_first_chunk_reads_fp8_pool, touching `TestMiniMaxHD128AsmPrefill, setUpClass, exercise`.
- Code diff details:
  - `test/registered/amd/test_minimax_hd128_asm_prefill.py` added +157/-0 (157 lines); hunks: -0,0 +1,157; symbols: TestMiniMaxHD128AsmPrefill, setUpClass, exercise, test_first_chunk_reads_fp8_pool
- Key code excerpts:

```diff
diff -- test/registered/amd/test_minimax_hd128_asm_prefill.py
@@ -0,0 +1,157 @@
+"""Exercise the SGLang HD128 route with quantized KV and non-unit scales."""
+import os
+import unittest
+from types import SimpleNamespace
+from unittest.mock import patch
+import torch
```

- Reviewed files:
  - tests: `test/registered/amd/test_minimax_hd128_asm_prefill.py` added +157/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_minimax_hd128_asm_prefill.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #35357 - [AMD] MiniMax-M3: fuse sparse QK norm, RoPE and cache writes with AITER

- Link: https://github.com/sgl-project/sglang/pull/35357
- Status/date: merged / 2026-10-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/minimax_m3.py`; associated commits `ff219e159e65`
- Diff scope read: GitHub Pull Request files API returned 2 files, +192/-0, 227 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] MiniMax-M3: fuse sparse QK norm, RoPE and cache writes with AITER"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/models/minimax_m3.py`; technical summary: Covers "[AMD] MiniMax-M3: fuse sparse QK norm, RoPE and cache writes with AITER"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +188/-0 (188 lines); hunks: -150,6 +150,17; -794,6 +805,23 @@ def __init__(; symbols: __init__, _can_use_rocm_qk_norm_rope, _get_sparse_kv_pool, _get_aiter_cos_sin_cache, touching `__init__, _can_use_rocm_qk_norm_rope, _get_sparse_kv_pool`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +188/-0 (188 lines); hunks: -150,6 +150,17; -794,6 +805,23 @@ def __init__(; symbols: __init__, _can_use_rocm_qk_norm_rope, _get_sparse_kv_pool, _get_aiter_cos_sin_cache
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -150,6 +150,17 @@
+_aiter = None
+_has_aiter_fused_qknorm = False
+if _is_hip and envs.SGLANG_USE_AITER.get():
+    try:
+        import aiter as _aiter
+        _has_aiter_fused_qknorm = hasattr(_aiter, "fused_qknorm_idxrqknorm")
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +188/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/environ.py`, `python/sglang/srt/models/minimax_m3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #38615 - [MiniMax-M3] Instantiate the decode block top-k in register buckets

- Link: https://github.com/sgl-project/sglang/pull/38615
- Status/date: merged / 2026-10-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py`; associated commits `6e6ccb26f265`
- Diff scope read: GitHub Pull Request files API returned 5 files, +155/-47, 329 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MiniMax-M3] Instantiate the decode block top-k in register buckets"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py`; technical summary: Covers "[MiniMax-M3] Instantiate the decode block top-k in register buckets"; the main implementation surface is `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +88/-38 (126 lines); hunks: -42,10 +42,11 @@ struct TopKTraitImpl {; -301,6 +302,9 @@ struct TopKTraitImpl {; `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +52/-4 (56 lines); hunks: -9,7 +9,10; -64,9 +67,7 @@ def _check_contract(out, seq_lens, block_size, topk, S):; symbols: _check_contract, test_decode_topk_distinct, test_decode_topk_small_num_blocks, test_decode_topk_register_buckets, touching `_check_contract, test_decode_topk_distinct, test_decode_topk_small_num_blocks`; `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py` modified +11/-2 (13 lines); hunks: -57,7 +57,7 @@ def _effective_kv_from_selection(ti, seq_lens, block):; -119,7 +119,16 @@ def test_fused_page_table_matches_custom(bs, seq_len, nqh):; symbols: _effective_kv_from_selection, test_fused_page_table_matches_custom, test_dp_flattened_page_table, touching `_effective_kv_from_selection, test_fused_page_table_matches_custom, test_dp_flattened_page_table`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +3/-2 (5 lines); hunks: -18,8 +18,9; symbols: _prune_decode_configs, touching `_prune_decode_configs`.
- Code diff details:
  - `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +88/-38 (126 lines); hunks: -42,10 +42,11 @@ struct TopKTraitImpl {; -301,6 +302,9 @@ struct TopKTraitImpl {
  - `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +52/-4 (56 lines); hunks: -9,7 +9,10; -64,9 +67,7 @@ def _check_contract(out, seq_lens, block_size, topk, S):; symbols: _check_contract, test_decode_topk_distinct, test_decode_topk_small_num_blocks, test_decode_topk_register_buckets
  - `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py` modified +11/-2 (13 lines); hunks: -57,7 +57,7 @@ def _effective_kv_from_selection(ti, seq_lens, block):; -119,7 +119,16 @@ def test_fused_page_table_matches_custom(bs, seq_len, nqh):; symbols: _effective_kv_from_selection, test_fused_page_table_matches_custom, test_dp_flattened_page_table
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +3/-2 (5 lines); hunks: -18,8 +18,9; symbols: _prune_decode_configs
  - `python/sglang/kernels/ops/attention/minimax_decode_topk.py` modified +1/-1 (2 lines); hunks: -30,7 +30,7
- Key code excerpts:

```diff
diff -- python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh
@@ -42,10 +42,11 @@ struct TopKTraitImpl {
-#ifdef USE_ROCM
-#else
-  static constexpr uint32_t kMaxNumBlocks = 4096;  // block topk
+#ifndef USE_ROCM
+  // Smallest register bucket for the multi-element radix path; the launchers
+  // instantiate larger ones on demand up to kMaxNumBlocks.
diff -- test/registered/kernels/ops/attention/test_minimax_decode_topk.py
@@ -9,7 +9,10 @@
-from sglang.kernels.ops.attention.minimax_decode_topk import minimax_decode_topk
+from sglang.kernels.ops.attention.minimax_decode_topk import (
+    _jit_module,
+    minimax_decode_topk,
+)
@@ -64,9 +67,7 @@ def _check_contract(out, seq_lens, block_size, topk, S):
diff -- test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py
@@ -57,7 +57,7 @@ def _effective_kv_from_selection(ti, seq_lens, block):
```

- Reviewed files:
  - runtime: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +88/-38; `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +3/-2; `python/sglang/kernels/ops/attention/minimax_decode_topk.py` modified +1/-1
  - tests: `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +52/-4; `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py` modified +11/-2
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk_page_table.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #38841 - [MiniMax-M3] Decode: paged K/V tile loads and a tiny GEMM for the router projection

- Link: https://github.com/sgl-project/sglang/pull/38841
- Status/date: merged / 2026-10-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py`; associated commits `11b1fb21de1c`
- Diff scope read: GitHub Pull Request files API returned 4 files, +168/-1, 253 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MiniMax-M3] Decode: paged K/V tile loads and a tiny GEMM for the router projection"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py`; technical summary: Covers "[MiniMax-M3] Decode: paged K/V tile loads and a tiny GEMM for the router projection"; the main implementation surface is `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/minimax_m3.py` modified +24/-0 (24 lines); hunks: -88,6 +88,7; -117,6 +118,12; symbols: __init__, _compute_router_logits, touching `__init__, _compute_router_logits`; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0 (2 lines); hunks: -428,6 +428,7 @@ def minimax_sparse_decode(; -445,6 +446,7 @@ def minimax_sparse_decode(; symbols: minimax_sparse_decode, touching `minimax_sparse_decode`; `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: _inputs, _decode, test_paged_tile_matches_slot_gather, test_hisparse_slots_override_paged_tile, touching `_inputs, _decode, test_paged_tile_matches_slot_gather`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +16/-1 (17 lines); hunks: -88,6 +88,7 @@ def _gqa_share_sparse_decode_kernel(; -184,13 +185,22 @@ def _gqa_share_sparse_decode_kernel(; symbols: _gqa_share_sparse_decode_kernel, flash_decode_with_gqa_share_sparse, touching `_gqa_share_sparse_decode_kernel, flash_decode_with_gqa_share_sparse`.
- Code diff details:
  - `python/sglang/srt/models/minimax_m3.py` modified +24/-0 (24 lines); hunks: -88,6 +88,7; -117,6 +118,12; symbols: __init__, _compute_router_logits
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0 (2 lines); hunks: -428,6 +428,7 @@ def minimax_sparse_decode(; -445,6 +446,7 @@ def minimax_sparse_decode(; symbols: minimax_sparse_decode
  - `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: _inputs, _decode, test_paged_tile_matches_slot_gather, test_hisparse_slots_override_paged_tile
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +16/-1 (17 lines); hunks: -88,6 +88,7 @@ def _gqa_share_sparse_decode_kernel(; -184,13 +185,22 @@ def _gqa_share_sparse_decode_kernel(; symbols: _gqa_share_sparse_decode_kernel, flash_decode_with_gqa_share_sparse
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/minimax_m3.py
@@ -88,6 +88,7 @@
+from sglang.srt.models.deepseek_common.utils import tiny_router_gemm_max_tokens
@@ -117,6 +118,12 @@
+# Import-time CUDA kernels would block processor imports on CPU CI.
+if _is_cuda:
+    from sglang.kernels.ops.gemm.tiny_gemm import tiny_gemm_bf16
+else:
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -428,6 +428,7 @@ def minimax_sparse_decode(
+                    page_size=page_size,
@@ -445,6 +446,7 @@ def minimax_sparse_decode(
+                page_size=page_size,
diff -- test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py
@@ -0,0 +1,126 @@
+"""MiniMax-M3 sparse decode: a block inside one page loads from its first slot.
+These cases pin that this matches the slot gather on the allocator's page layout,
+that pages smaller than a block keep the gather, and that HiSparse slots win.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/minimax_m3.py` modified +24/-0; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0; `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +16/-1
  - tests: `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py` added +126/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #42772 - [AMD] Keep MiniMax decode-score tile at 128 tokens off gfx950

- Link: https://github.com/sgl-project/sglang/pull/42772
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`; associated commits `51f7ea84c794`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-3, 22 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Keep MiniMax decode-score tile at 128 tokens off gfx950"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`; technical summary: Covers "[AMD] Keep MiniMax decode-score tile at 128 tokens off gfx950"; the main implementation surface is `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +5/-3 (8 lines); hunks: -7,7 +7,7; -38,8 +38,10 @@ def _prune_decode_configs(configs, named_args, **kwargs):; symbols: _prune_decode_configs, _decode_score_block_n, touching `_prune_decode_configs, _decode_score_block_n`.
- Code diff details:
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +5/-3 (8 lines); hunks: -7,7 +7,7; -38,8 +38,10 @@ def _prune_decode_configs(configs, named_args, **kwargs):; symbols: _prune_decode_configs, _decode_score_block_n
- Key code excerpts:

```diff
diff -- python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py
@@ -7,7 +7,7 @@
-from sglang.srt.utils import is_xpu
+from sglang.srt.utils import is_gfx95_supported, is_xpu
@@ -38,8 +38,10 @@ def _prune_decode_configs(configs, named_args, **kwargs):
-    # gfx950 pick: 512 for tiny batches (few CTAs), else 128.
-    return max(512 if args["batch_size"] <= 4 else 128, args["block_size"])
+    # gfx950 pick: 512 for tiny batches (few CTAs), else 128. A 512-token bf16
```

- Reviewed files:
  - runtime: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +5/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #43259 - [AMD] Run the MiniMax indexer CP test on MI35X, not MI300

- Link: https://github.com/sgl-project/sglang/pull/43259
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/test_minimax_indexer_cp.py`; associated commits `70e82f7b731f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Run the MiniMax indexer CP test on MI35X, not MI300"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `test/registered/amd/test_minimax_indexer_cp.py`; technical summary: Covers "[AMD] Run the MiniMax indexer CP test on MI35X, not MI300"; the main implementation surface is `test/registered/amd/test_minimax_indexer_cp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/test_minimax_indexer_cp.py` modified +1/-1 (2 lines); hunks: -6,7 +6,7.
- Code diff details:
  - `test/registered/amd/test_minimax_indexer_cp.py` modified +1/-1 (2 lines); hunks: -6,7 +6,7
- Key code excerpts:

```diff
diff -- test/registered/amd/test_minimax_indexer_cp.py
@@ -6,7 +6,7 @@
-register_amd_ci(est_time=20, suite="stage-b-test-1-gpu-small-amd")
+register_amd_ci(est_time=20, suite="stage-b-test-1-gpu-small-amd-mi35x")
```

- Reviewed files:
  - tests: `test/registered/amd/test_minimax_indexer_cp.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_minimax_indexer_cp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #42614 - [AMD] MiniMax-M3 indexer CP: packed scoring for EAGLE verify rows

- Link: https://github.com/sgl-project/sglang/pull/42614
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `test/registered/amd/test_minimax_indexer_cp.py`; associated commits `6d8ddaf1d786`
- Diff scope read: GitHub Pull Request files API returned 5 files, +211/-7, 335 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] MiniMax-M3 indexer CP: packed scoring for EAGLE verify rows"; model line: MiniMax M2 Series; category: model implementation change; main diff: `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`; technical summary: Covers "[AMD] MiniMax-M3 indexer CP: packed scoring for EAGLE verify rows"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +6/-0 (6 lines); hunks: -1843,6 +1843,12 @@ def hisparse_swap_in_fn(topk_idx):; symbols: hisparse_swap_in_fn, touching `hisparse_swap_in_fn`; `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` modified +2/-0 (2 lines); hunks: -162,6 +162,7 @@ def __call__(; -189,6 +190,7 @@ def __call__(; symbols: __call__, touching `__call__`; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0 (2 lines); hunks: -327,6 +327,7 @@ def minimax_sparse_decode(; -362,6 +363,7 @@ def minimax_sparse_decode(; symbols: minimax_sparse_decode, touching `minimax_sparse_decode`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py` modified +142/-1 (143 lines); hunks: -9,6 +9,9; -92,6 +95,102 @@ def _score_shard(; symbols: _score_shard, _score_shard_packed, _pack, score_local_blocks, touching `_score_shard, _score_shard_packed, _pack`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +6/-0 (6 lines); hunks: -1843,6 +1843,12 @@ def hisparse_swap_in_fn(topk_idx):; symbols: hisparse_swap_in_fn
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` modified +2/-0 (2 lines); hunks: -162,6 +162,7 @@ def __call__(; -189,6 +190,7 @@ def __call__(; symbols: __call__
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0 (2 lines); hunks: -327,6 +327,7 @@ def minimax_sparse_decode(; -362,6 +363,7 @@ def minimax_sparse_decode(; symbols: minimax_sparse_decode
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py` modified +142/-1 (143 lines); hunks: -9,6 +9,9; -92,6 +95,102 @@ def _score_shard(; symbols: _score_shard, _score_shard_packed, _pack, score_local_blocks
  - `test/registered/amd/test_minimax_indexer_cp.py` modified +59/-6 (65 lines); hunks: -4,30 +4,46; -54,7 +70,7 @@ def _native_topk(q_head, cache, table, slots, lengths, max_len...; symbols: _inputs, _verify_rows, _native_topk, _cp_topk
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -1843,6 +1843,12 @@ def hisparse_swap_in_fn(topk_idx):
+                # the verify funnel lays out each request's draft rows consecutively
+                packed_queries=(
+                    self.speculative_num_draft_tokens
+                    if forward_batch.forward_mode.is_target_verify()
+                    else 1
+                ),
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py
@@ -162,6 +162,7 @@ def __call__(
+        packed_queries=1,
@@ -189,6 +190,7 @@ def __call__(
+            packed_queries=packed_queries,
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -327,6 +327,7 @@ def minimax_sparse_decode(
+    packed_queries: int = 1,  # consecutive rows sharing one request (EAGLE verify)
@@ -362,6 +363,7 @@ def minimax_sparse_decode(
+            packed_queries=packed_queries,
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +6/-0; `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` modified +2/-0; `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0; `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py` modified +142/-1
  - tests: `test/registered/amd/test_minimax_indexer_cp.py` modified +59/-6
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_minimax_indexer_cp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #40120 - [Doc] [NPU] cookbook: add tested A2 deployment and A3 reference for MiniMax-M2.5

- Link: https://github.com/sgl-project/sglang/pull/40120
- Status/date: merged / 2026-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx`, `docs/scripts/tests/minimax-m25-deployment.test.mjs`, `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx`; associated commits `cdbd47842269`
- Diff scope read: GitHub Pull Request files API returned 5 files, +967/-116, 1276 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] [NPU] cookbook: add tested A2 deployment and A3 reference for MiniMax-M2.5"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx`, `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx`, `docs/scripts/tests/minimax-m25-deployment.test.mjs`; technical summary: Covers "[Doc] [NPU] cookbook: add tested A2 deployment and A3 reference for MiniMax-M2.5"; the main implementation surface is `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx`, `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx`, `docs/scripts/tests/minimax-m25-deployment.test.mjs`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx` modified +473/-5 (478 lines); hunks: -1,5 +1,6; -23,7 +24,7 @@ For more details, please refer to the [official MiniMax-M2.5 a...; `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx` modified +336/-101 (437 lines); hunks: -1,5 +1,10; -12,13 +17,22 @@ export const MiniMaxM25Deployment = () => {; `docs/scripts/tests/minimax-m25-deployment.test.mjs` added +156/-0 (156 lines); hunks: -0,0 +1,156.
- Code diff details:
  - `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx` modified +473/-5 (478 lines); hunks: -1,5 +1,6; -23,7 +24,7 @@ For more details, please refer to the [official MiniMax-M2.5 a...
  - `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx` modified +336/-101 (437 lines); hunks: -1,5 +1,10; -12,13 +17,22 @@ export const MiniMaxM25Deployment = () => {
  - `docs/scripts/tests/minimax-m25-deployment.test.mjs` added +156/-0 (156 lines); hunks: -0,0 +1,156
- Key code excerpts:

```diff
diff -- docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx
@@ -1,5 +1,6 @@
+description: "Deploy MiniMax-M2.5 with SGLang on NVIDIA, AMD, or Ascend A2, with an Ascend A3 reference configuration."
@@ -23,7 +24,7 @@ For more details, please refer to the [official MiniMax-M2.5 announcement](https
-Please refer to the [official SGLang installation guide](../../../docs/get-started/install) for installation instructions.
+Please refer to the [official SGLang installation guide](/docs/get-started/install) for installation instructions.
@@ -35,19 +36,75 @@ docker pull lmsysorg/sglang:v0.5.9-rocm720-mi30x
+### Ascend A2 prerequisites (smoke tested)
diff -- docs/src/snippets/autoregressive/minimax-m25-deployment.jsx
@@ -1,5 +1,10 @@
+  const isAscend = (values) => values.hardware === 'a2' || values.hardware === 'a3';
+  const parserItems = (values) => [
+    { id: 'disabled', label: 'Disabled', default: true, disabled: isAscend(values) },
+    { id: 'enabled', label: 'Enabled', default: false, disabled: isAscend(values) }
+  ];
@@ -12,13 +17,22 @@ export const MiniMaxM25Deployment = () => {
diff -- docs/scripts/tests/minimax-m25-deployment.test.mjs
@@ -0,0 +1,156 @@
```

- Reviewed files:
  - docs: `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx` modified +473/-5; `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx` modified +336/-101
  - tests: `docs/scripts/tests/minimax-m25-deployment.test.mjs` added +156/-0
- Risk and verification: The diff ships test coverage in `docs/scripts/tests/diffusion-builders.test.mjs`, `docs/scripts/tests/minimax-m25-deployment.test.mjs`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #34241 - [Fix] [AMD] test: Recalibrate MiniMax-M2.7 GSM8K threshold 0.93->0.91 for MI300 runners

- Link: https://github.com/sgl-project/sglang/pull/34241
- Status/date: merged / 2026-10-22
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`; associated commits `1c967f5043e2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] [AMD] test: Recalibrate MiniMax-M2.7 GSM8K threshold 0.93->0.91 for MI300 runners"; model line: MiniMax M2 Series; category: bug fix; main diff: `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`; technical summary: Covers "[Fix] [AMD] test: Recalibrate MiniMax-M2.7 GSM8K threshold 0.93->0.91 for MI300 runners"; the main implementation surface is `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` modified +2/-1 (3 lines); hunks: -64,7 +64,8 @@ def get_display_name(self) -> str:; symbols: get_display_name, touching `get_display_name`.
- Code diff details:
  - `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` modified +2/-1 (3 lines); hunks: -64,7 +64,8 @@ def get_display_name(self) -> str:; symbols: get_display_name
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py
@@ -64,7 +64,8 @@ def get_display_name(self) -> str:
-        accuracy_threshold=0.93,
+        # MI300: mean 0.9216 over 10x full GSM8K (exact CI config); 0.93 never passes.
+        accuracy_threshold=0.91,
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py` modified +2/-1
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45924 - [Doc] Cookbook: add MiniMax-M3.1

- Link: https://github.com/sgl-project/sglang/pull/45924
- Status/date: merged / 2026-10-23
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`; associated commits `f36ee5de93e9`
- Diff scope read: GitHub Pull Request files API returned 6 files, +1196/-2, 1235 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] Cookbook: add MiniMax-M3.1"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`; technical summary: Covers "[Doc] Cookbook: add MiniMax-M3.1"; the main implementation surface is `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` added +727/-0 (727 lines); hunks: -0,0 +1,727; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` added +460/-0 (460 lines); hunks: -0,0 +1,460; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` modified +0/-1 (1 lines); hunks: -1,7 +1,6.
- Code diff details:
  - `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` added +727/-0 (727 lines); hunks: -0,0 +1,727
  - `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` added +460/-0 (460 lines); hunks: -0,0 +1,460
  - `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` modified +0/-1 (1 lines); hunks: -1,7 +1,6
- Key code excerpts:

```diff
diff -- docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx
@@ -0,0 +1,727 @@
+// MiniMax-M3.1 cookbook config. Consumed by _deployment.jsx + _playground.jsx;
+// see _deployment.jsx header for the field contract.
+export const config = (() => {
+// Shown under every Blackwell command; details in the Configuration Tips section.
+const BLACKWELL_NOTE =
+  "First launch JIT-compiles the MSA kernels (needs `FMHA_SM100_ALLOW_JIT=1`) and expects CUDA toolkit >= 13.4; "
diff -- docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx
@@ -0,0 +1,460 @@
+---
+title: MiniMax-M3.1
+description: "Deploy MiniMax-M3.1-Flash with SGLang — the static-NVFP4 build of MiniMax's sparse-attention Mixture-of-Experts reasoning model, with its bundled DSpark draft or Rad
+tag: NEW
+---
+## Deployment
diff -- docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx
@@ -1,7 +1,6 @@
```

- Reviewed files:
  - docs: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` added +727/-0; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` added +460/-0; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` modified +0/-1
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs/cookbook/autoregressive/intro.mdx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #45179 - [Perf] diffusion/minimax-h3: Batch the video VAE decoder tiles and fuse the output chain

- Link: https://github.com/sgl-project/sglang/pull/45179
- Status/date: merged / 2026-10-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/test/kernels/minimax_h3_vae.py`; associated commits `0498ab7b6ee2`
- Diff scope read: GitHub Pull Request files API returned 24 files, +1807/-121, 2323 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] diffusion/minimax-h3: Batch the video VAE decoder tiles and fuse the output chain"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/test/kernels/minimax_h3_vae.py`; technical summary: Covers "[Perf] diffusion/minimax-h3: Batch the video VAE decoder tiles and fuse the output chain"; the main implementation surface is `python/sglang/test/kernels/minimax_h3_vae.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/test/kernels/minimax_h3_vae.py` added +77/-0 (77 lines); hunks: -0,0 +1,77; symbols: _h3_tiny_vae, _h3_install_gate, touching `_h3_tiny_vae, _h3_install_gate`.
- Code diff details:
  - `python/sglang/test/kernels/minimax_h3_vae.py` added +77/-0 (77 lines); hunks: -0,0 +1,77; symbols: _h3_tiny_vae, _h3_install_gate
- Key code excerpts:

```diff
diff -- python/sglang/test/kernels/minimax_h3_vae.py
@@ -0,0 +1,77 @@
+# SPDX-License-Identifier: Apache-2.0
+"""Shared MiniMax-H3 VAE fixtures for CPU and CUDA integration tests."""
+from unittest.mock import patch
+import torch
+from sglang.multimodal_gen.runtime.models.vaes.fast_path_gate import (
+    VaeFastPathGate,
```

- Reviewed files:
  - tests: `python/sglang/test/kernels/minimax_h3_vae.py` added +77/-0
- Risk and verification: The diff ships test coverage in `python/sglang/multimodal_gen/test/unit/test_minimax_h3_admission.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vae_fast_path.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vdn.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46133 - [Fix] minimax-m3: Type nested tool-call arguments and count self-opened reasoning

- Link: https://github.com/sgl-project/sglang/pull/46133
- Status/date: merged / 2026-10-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/minimax_m3.py`, `test/registered/unit/function_call/test_minimax_m3_detector.py`; associated commits `d0f517168dff`
- Diff scope read: GitHub Pull Request files API returned 19 files, +991/-39, 1450 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] minimax-m3: Type nested tool-call arguments and count self-opened reasoning"; model line: MiniMax M2 Series; category: bug fix; main diff: `test/registered/unit/function_call/test_minimax_m3_detector.py`, `python/sglang/srt/function_call/minimax_m3.py`; technical summary: Covers "[Fix] minimax-m3: Type nested tool-call arguments and count self-opened reasoning"; the main implementation surface is `test/registered/unit/function_call/test_minimax_m3_detector.py`, `python/sglang/srt/function_call/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/function_call/test_minimax_m3_detector.py` modified +312/-0 (312 lines); hunks: -2,6 +2,7; -582,5 +583,316 @@ def test_detect_and_parse(self):; symbols: test_detect_and_parse, TestMinimaxM3SchemaLessContainers, setUp, _fetch, touching `test_detect_and_parse, TestMinimaxM3SchemaLessContainers, setUp`; `python/sglang/srt/function_call/minimax_m3.py` modified +84/-8 (92 lines); hunks: -24,6 +24,7; -84,6 +85,10 @@ def detect_and_parse(self, text: str, tools: List[Tool]) -> S...; symbols: MinimaxM3Detector, detect_and_parse, parses_without_tools, supports_structural_tag, touching `MinimaxM3Detector, detect_and_parse, parses_without_tools`.
- Code diff details:
  - `test/registered/unit/function_call/test_minimax_m3_detector.py` modified +312/-0 (312 lines); hunks: -2,6 +2,7; -582,5 +583,316 @@ def test_detect_and_parse(self):; symbols: test_detect_and_parse, TestMinimaxM3SchemaLessContainers, setUp, _fetch
  - `python/sglang/srt/function_call/minimax_m3.py` modified +84/-8 (92 lines); hunks: -24,6 +24,7; -84,6 +85,10 @@ def detect_and_parse(self, text: str, tools: List[Tool]) -> S...; symbols: MinimaxM3Detector, detect_and_parse, parses_without_tools, supports_structural_tag
- Key code excerpts:

```diff
diff -- test/registered/unit/function_call/test_minimax_m3_detector.py
@@ -2,6 +2,7 @@
+from sglang.srt.function_call.function_call_parser import FunctionCallParser
@@ -582,5 +583,316 @@ def test_detect_and_parse(self):
+class TestMinimaxM3SchemaLessContainers(CustomTestCase):
+    """Members of a bare {"type": "object"} have no schema to type them by."""
+    def setUp(self):
+        self.tools = [
diff -- python/sglang/srt/function_call/minimax_m3.py
@@ -24,6 +24,7 @@
+UNTYPED_LITERALS = {"true": True, "false": False, "null": None}
@@ -84,6 +85,10 @@ def detect_and_parse(self, text: str, tools: List[Tool]) -> StreamingParseResult
+    @classmethod
+    def parses_without_tools(cls) -> bool:
+        return True
@@ -136,7 +141,18 @@ def _parse_block(self, block: str, tools: List[Tool]) -> List[ToolCallItem]:
```

- Reviewed files:
  - tests: `test/registered/unit/function_call/test_minimax_m3_detector.py` modified +312/-0
  - runtime: `python/sglang/srt/function_call/minimax_m3.py` modified +84/-8
- Risk and verification: The diff ships test coverage in `test/registered/unit/configs/test_model_config.py`, `test/registered/unit/entrypoints/openai/test_protocol.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/function_call/test_minimax_m3_detector.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46135 - [Perf] minimax-sparse: Speed up MiniMax-M3 sparse attention on Hopper

- Link: https://github.com/sgl-project/sglang/pull/46135
- Status/date: merged / 2026-10-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/jit/csrc/minimax/fused_store_kv_index.cuh`, `python/sglang/kernels/ops/attention/minimax_sparse/common/tile_ptr.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` and 7 files; associated commits `db7b66c1b6a7`
- Diff scope read: GitHub Pull Request files API returned 8 files, +685/-281, 1342 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] minimax-sparse: Speed up MiniMax-M3 sparse attention on Hopper"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py`; technical summary: Covers "[Perf] minimax-sparse: Speed up MiniMax-M3 sparse attention on Hopper"; the main implementation surface is `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +265/-74 (339 lines); hunks: -7,8 +7,10; -151,24 +153,31 @@ def _decode_score_kernel(; symbols: _decode_score_kernel, _decode_score_paged_kernel, _decode_score_attn_kernel, touching `_decode_score_kernel, _decode_score_paged_kernel, _decode_score_attn_kernel`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +164/-109 (273 lines); hunks: -6,36 +6,30; -94,8 +88,11 @@ def _gqa_share_sparse_decode_kernel(; symbols: _gqa_share_sparse_decode_kernel, _gqa_share_sparse_decode_kernel_impl, touching `_gqa_share_sparse_decode_kernel, _gqa_share_sparse_decode_kernel_impl`; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` modified +58/-33 (91 lines); hunks: -8,6 +8,7; -151,24 +152,31 @@ def _flash_attn_fwd_with_block_score_kernel(; symbols: _flash_attn_fwd_with_block_score_kernel, _index_block_score_only_kernel, touching `_flash_attn_fwd_with_block_score_kernel, _index_block_score_only_kernel`; `python/sglang/kernels/ops/attention/minimax_sparse/common/tile_ptr.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: tile_ptrs_1d, tile_ptrs_2d, tile_ptrs_3d, touching `tile_ptrs_1d, tile_ptrs_2d, tile_ptrs_3d`.
- Code diff details:
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +265/-74 (339 lines); hunks: -7,8 +7,10; -151,24 +153,31 @@ def _decode_score_kernel(; symbols: _decode_score_kernel, _decode_score_paged_kernel, _decode_score_attn_kernel
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +164/-109 (273 lines); hunks: -6,36 +6,30; -94,8 +88,11 @@ def _gqa_share_sparse_decode_kernel(; symbols: _gqa_share_sparse_decode_kernel, _gqa_share_sparse_decode_kernel_impl
  - `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` modified +58/-33 (91 lines); hunks: -8,6 +8,7; -151,24 +152,31 @@ def _flash_attn_fwd_with_block_score_kernel(; symbols: _flash_attn_fwd_with_block_score_kernel, _index_block_score_only_kernel
  - `python/sglang/kernels/ops/attention/minimax_sparse/common/tile_ptr.py` added +81/-0 (81 lines); hunks: -0,0 +1,81; symbols: tile_ptrs_1d, tile_ptrs_2d, tile_ptrs_3d
  - `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` modified +38/-26 (64 lines); hunks: -8,6 +8,7; -156,17 +157,18 @@ def _gqa_share_sparse_fwd_kernel(; symbols: _gqa_share_sparse_fwd_kernel
- Key code excerpts:

```diff
diff -- python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py
@@ -7,8 +7,10 @@
+from sglang.srt.runtime_context import get_platform
+from ..common.tile_ptr import tile_ptrs_1d, tile_ptrs_2d
@@ -151,24 +153,31 @@ def _decode_score_kernel(
-    q_ptrs = tl.make_block_ptr(
-        base=q_ptr + pid_b * stride_q_b + pid_h * stride_q_h,
-        shape=(gqa_group_size, head_dim),
diff -- python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py
@@ -6,36 +6,30 @@
+from sglang.srt.runtime_context import get_platform
+from ..common.tile_ptr import tile_ptrs_1d, tile_ptrs_2d
+_SPARSE_DECODE_HEURISTICS = {
+    "BLOCK_SIZE_H": lambda args: max(
+        16, triton.next_power_of_2(args["gqa_group_size"])
+    ),
diff -- python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py
@@ -8,6 +8,7 @@
```

- Reviewed files:
  - runtime: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` modified +265/-74; `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` modified +164/-109; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py` modified +58/-33; `python/sglang/kernels/ops/attention/minimax_sparse/common/tile_ptr.py` added +81/-0; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py` modified +38/-26; `python/sglang/kernels/jit/csrc/minimax/fused_store_kv_index.cuh` modified +38/-14
- Risk and verification: Runtime changes concentrate in `python/sglang/kernels/jit/csrc/minimax/fused_store_kv_index.cuh`, `python/sglang/kernels/ops/attention/minimax_sparse/common/tile_ptr.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #46140 - [Feat] quantization: Add the MiniMax-M3.1 NVFP4 MoE method

- Link: https://github.com/sgl-project/sglang/pull/46140
- Status/date: merged / 2026-10-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/minimax_vl.py`, `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py`, `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py`; associated commits `a99c7d050fae`
- Diff scope read: GitHub Pull Request files API returned 15 files, +773/-15, 1008 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] quantization: Add the MiniMax-M3.1 NVFP4 MoE method"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py`, `python/sglang/srt/configs/minimax_vl.py`, `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py`; technical summary: Covers "[Feat] quantization: Add the MiniMax-M3.1 NVFP4 MoE method"; the main implementation surface is `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py`, `python/sglang/srt/configs/minimax_vl.py`, `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py` added +380/-0 (380 lines); hunks: -0,0 +1,380; symbols: MiniMaxM3Nvfp4Config, __init__, get_min_capability, get_name, touching `MiniMaxM3Nvfp4Config, __init__, get_min_capability`; `python/sglang/srt/configs/minimax_vl.py` modified +51/-0 (51 lines); hunks: -1,5 +1,6; -58,3 +59,53 @@ def __init__(; symbols: __init__, MiniMaxM3VLConfig, configure_minimax_m3_dspark, touching `__init__, MiniMaxM3VLConfig, configure_minimax_m3_dspark`; `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py` added +236/-0 (236 lines); hunks: -0,0 +1,236; symbols: _quantize, _fake_quant_per_token, _swigluoai, _build_layer, touching `_quantize, _fake_quant_per_token, _swigluoai`.
- Code diff details:
  - `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py` added +380/-0 (380 lines); hunks: -0,0 +1,380; symbols: MiniMaxM3Nvfp4Config, __init__, get_min_capability, get_name
  - `python/sglang/srt/configs/minimax_vl.py` modified +51/-0 (51 lines); hunks: -1,5 +1,6; -58,3 +59,53 @@ def __init__(; symbols: __init__, MiniMaxM3VLConfig, configure_minimax_m3_dspark
  - `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py` added +236/-0 (236 lines); hunks: -0,0 +1,236; symbols: _quantize, _fake_quant_per_token, _swigluoai, _build_layer
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py
@@ -0,0 +1,380 @@
+# SPDX-License-Identifier: Apache-2.0
+from __future__ import annotations
+import logging
+from typing import Any
+import torch
+from sglang.srt.layers.moe.utils import get_moe_a2a_backend, get_moe_runner_backend
diff -- python/sglang/srt/configs/minimax_vl.py
@@ -1,5 +1,6 @@
+import copy
@@ -58,3 +59,53 @@ def __init__(
+def configure_minimax_m3_dspark(config):
+    """Translate an M3.1 DSpark draft checkpoint to the public draft config contract."""
+    text = copy.deepcopy(getattr(config, "text_config", config))
+    if isinstance(text, dict):
diff -- test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py
@@ -0,0 +1,236 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/quantization/minimax_m3_nvfp4.py` added +380/-0; `python/sglang/srt/configs/minimax_vl.py` modified +51/-0
  - tests: `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py` added +236/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/moe/test_minimax_m31_nvfp4_trtllm_moe.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46506 - [Doc] cookbook: Add MiniMax-M3.1-Flash AgentX launches and refresh with nine InferenceX PRs

- Link: https://github.com/sgl-project/sglang/pull/46506
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; associated commits `3f29ad11451c`
- Diff scope read: GitHub Pull Request files API returned 10 files, +4026/-887, 6689 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Add MiniMax-M3.1-Flash AgentX launches and refresh with nine InferenceX PRs"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`; technical summary: Covers "[Doc] cookbook: Add MiniMax-M3.1-Flash AgentX launches and refresh with nine InferenceX PRs"; the main implementation surface is `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` added +2599/-0 (2599 lines); hunks: -0,0 +1,2599; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +14/-1 (15 lines); hunks: -70,7 +70,7 @@ Pick your hardware + recipe to generate the launch command. Th...; -80,6 +80,19 @@ import { Playground } from "/src/snippets/_playground.jsx";.
- Code diff details:
  - `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` added +2599/-0 (2599 lines); hunks: -0,0 +1,2599
  - `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +14/-1 (15 lines); hunks: -70,7 +70,7 @@ Pick your hardware + recipe to generate the launch command. Th...; -80,6 +80,19 @@ import { Playground } from "/src/snippets/_playground.jsx";
- Key code excerpts:

```diff
diff -- docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx
@@ -0,0 +1,2599 @@
+// GENERATED by the sa-infx-cookbook sync scripts — do not edit by hand.
+// Launch commands mirrored from SemiAnalysis InferenceX AgentX submissions
+// (SemiAnalysisAI/InferenceX main@1c3e892a8493 plus open PRs #4333, #4346, #4417, #4434, #4455, #4490, #4491, #4492, #4524), with SA-specific settings removed.
+export const agentx = {
+ "model": "MiniMax-M3.1-Flash",
+ "generatedOn": "2026-10-25",
diff -- docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx
@@ -70,7 +70,7 @@ Pick your hardware + recipe to generate the launch command. The serving strategi
-<Deployment config={config} />
+<Deployment config={config} agenticLink="agentic-long-context-deployment" />
@@ -80,6 +80,19 @@ import { Playground } from "/src/snippets/_playground.jsx";
+## Agentic Long-Context Deployment
+Agentic workloads, such as coding agents and other multi-turn, tool-using assistants, send long prompts whose prefixes grow and repeat from turn to turn. Serving them well depends
+- **Router.** Each configuration was submitted behind one front door: Dynamo (`dynamo.frontend` with `dynamo.sglang` workers) or SGLang (`sglang.launch_server`, behind `sglang_rou
```

- Reviewed files:
  - docs: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` added +2599/-0; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +14/-1
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #46546 - [Doc] cookbook: MiniMax-M3.1 GB200 recipes and B200 Low-Latency (MonoKernel)

- Link: https://github.com/sgl-project/sglang/pull/46546
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`; associated commits `e1c4b273afd9`
- Diff scope read: GitHub Pull Request files API returned 2 files, +131/-12, 235 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: MiniMax-M3.1 GB200 recipes and B200 Low-Latency (MonoKernel)"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`; technical summary: Covers "[Doc] cookbook: MiniMax-M3.1 GB200 recipes and B200 Low-Latency (MonoKernel)"; the main implementation surface is `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` modified +128/-9 (137 lines); hunks: -24,14 +24,15 @@ const DFLASH2_FLAGS = [; -43,7 +44,7 @@ const MONOKERNEL_NOTE =; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +3/-3 (6 lines); hunks: -63,7 +63,7 @@ For how to launch the image, see [Install → Method 3: Using Do...; -118,7 +118,7 @@ import { agentx } from "/src/snippets/agentx/MiniMaxAI/minim....
- Code diff details:
  - `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` modified +128/-9 (137 lines); hunks: -24,14 +24,15 @@ const DFLASH2_FLAGS = [; -43,7 +44,7 @@ const MONOKERNEL_NOTE =
  - `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +3/-3 (6 lines); hunks: -63,7 +63,7 @@ For how to launch the image, see [Install → Method 3: Using Do...; -118,7 +118,7 @@ import { agentx } from "/src/snippets/agentx/MiniMaxAI/minim...
- Key code excerpts:

```diff
diff -- docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx
@@ -24,14 +24,15 @@ const DFLASH2_FLAGS = [
-const BLACKWELL_HW = ["b300", "gb300", "b200"];
+const BLACKWELL_HW = ["b300", "gb300", "b200", "gb200"];
-// The plugin declares sm_100 and sm_103 at TP4 only;
-// only B300 has been measured, so GB300 / B200 get no cell yet.
+// The plugin declares sm_100 and sm_103 at TP4 only. B300 is measured; the GB300,
+// B200 and GB200 cells run the same command (final verification of B200 and GB200
diff -- docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx
@@ -63,7 +63,7 @@ For how to launch the image, see [Install → Method 3: Using Docker](../../../d
-- **Low-Latency** — fastest responses with a few users at once. On B300 it serves one request at a time through the MSA-V1 MonoKernel; on AMD it is a TP4 recipe for up to about 32
+- **Low-Latency** — fastest responses with a few users at once. On B300, GB300, B200 and GB200 it serves one request at a time through the MSA-V1 MonoKernel; on AMD it is a TP4 re
@@ -118,7 +118,7 @@ import { agentx } from "/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx";
-The B300 **Low-Latency** recipe serves batch-size-1 decode through the MSA-V1 MonoKernel plugin with `--monokernel-backend msa`. The plugin supports Blackwell sm_100 and sm_103 (B
+The B300 **Low-Latency** recipe serves batch-size-1 decode through the MSA-V1 MonoKernel plugin with `--monokernel-backend msa`. The plugin supports Blackwell sm_100 and sm_103 (B
@@ -129,7 +129,7 @@ The B300 **Low-Latency** recipe serves batch-size-1 decode through the MSA-V1 Mo
```

- Reviewed files:
  - docs: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` modified +128/-9; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +3/-3
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #46547 - [Doc] cookbook: Refresh SemiAnalysis AgentX launches with MiniMax-M3.1-Flash B200 / GB200 HiCache points

- Link: https://github.com/sgl-project/sglang/pull/46547
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; associated commits `d42e1ee7e10a`
- Diff scope read: GitHub Pull Request files API returned 8 files, +273/-147, 743 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Refresh SemiAnalysis AgentX launches with MiniMax-M3.1-Flash B200 / GB200 HiCache points"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; technical summary: Covers "[Doc] cookbook: Refresh SemiAnalysis AgentX launches with MiniMax-M3.1-Flash B200 / GB200 HiCache points"; the main implementation surface is `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +197/-40 (237 lines); hunks: -1,31 +1,26; -34,9 +29,9 @@ export const agentx = {.
- Code diff details:
  - `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +197/-40 (237 lines); hunks: -1,31 +1,26; -34,9 +29,9 @@ export const agentx = {
- Key code excerpts:

```diff
diff -- docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx
@@ -1,31 +1,26 @@
-// (SemiAnalysisAI/InferenceX main@1c3e892a8493 plus open PRs #4333, #4346, #4417, #4434, #4455, #4490, #4491, #4492, #4524), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@65a6dd197872 plus open PRs #4333, #4346, #4417, #4434, #4455, #4490, #4491, #4524), with SA-specific settings removed.
- "generatedOn": "2026-10-25",
+ "generatedOn": "2026-10-26",
-  "main": "1c3e892a8493ae4bc6b25bc688ccd6d6916742c3",
+  "main": "65a6dd1978720f65099fea8c4d5ac5eddfdfd8d7",
```

- Reviewed files:
  - docs: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +197/-40
- Risk and verification: This is mostly docs/examples in `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #45925 - [Feat] minimax: Support MiniMax-M3.1-Flash

- Link: https://github.com/sgl-project/sglang/pull/45925
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py`, `python/sglang/srt/disaggregation/minimax.py`, `python/sglang/srt/mem_cache/pool_host/minimax_m3_nvfp4.py`, `python/sglang/srt/models/dspark_minimax.py`, `python/sglang/srt/models/minimax_m3.py` and 16 files; associated commits `a9bf8c76a011`
- Diff scope read: GitHub Pull Request files API returned 63 files, +6257/-324, 8046 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] minimax: Support MiniMax-M3.1-Flash"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/multimodal/processors/minimax_m3_vl.py`, `test/registered/unit/multimodal/test_minimax_m31_processor.py`, `test/registered/unit/models/test_minimax_m31_model.py`; technical summary: Covers "[Feat] minimax: Support MiniMax-M3.1-Flash"; the main implementation surface is `python/sglang/srt/multimodal/processors/minimax_m3_vl.py`, `test/registered/unit/multimodal/test_minimax_m31_processor.py`, `test/registered/unit/models/test_minimax_m31_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/minimax_m3_vl.py` modified +637/-101 (738 lines); hunks: -2,68 +2,160; -119,6 +211,31 @@ async def get_video_tensor(; symbols: _compute_aligned_size, get_hw_multiple_of, _check_max_long_side_pixel, _check_video_fps, touching `_compute_aligned_size, get_hw_multiple_of, _check_max_long_side_pixel`; `test/registered/unit/multimodal/test_minimax_m31_processor.py` added +557/-0 (557 lines); hunks: -0,0 +1,557; symbols: _image, FakeDecoder, __init__, __len__, touching `_image, FakeDecoder, __init__`; `test/registered/unit/models/test_minimax_m31_model.py` added +484/-0 (484 lines); hunks: -0,0 +1,484; symbols: draft_config, server_args, packed_moe_hf, TestMiniMaxM31ConfigResolution, touching `draft_config, server_args, packed_moe_hf`; `python/sglang/srt/models/dspark_minimax.py` added +326/-0 (326 lines); hunks: -0,0 +1,326; symbols: DSparkMiniMaxAttention, __init__, kv_proj_only, apply_k_norm, touching `DSparkMiniMaxAttention, __init__, kv_proj_only`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/minimax_m3_vl.py` modified +637/-101 (738 lines); hunks: -2,68 +2,160; -119,6 +211,31 @@ async def get_video_tensor(; symbols: _compute_aligned_size, get_hw_multiple_of, _check_max_long_side_pixel, _check_video_fps
  - `test/registered/unit/multimodal/test_minimax_m31_processor.py` added +557/-0 (557 lines); hunks: -0,0 +1,557; symbols: _image, FakeDecoder, __init__, __len__
  - `test/registered/unit/models/test_minimax_m31_model.py` added +484/-0 (484 lines); hunks: -0,0 +1,484; symbols: draft_config, server_args, packed_moe_hf, TestMiniMaxM31ConfigResolution
  - `python/sglang/srt/models/dspark_minimax.py` added +326/-0 (326 lines); hunks: -0,0 +1,326; symbols: DSparkMiniMaxAttention, __init__, kv_proj_only, apply_k_norm
  - `python/sglang/srt/models/minimax_m3.py` modified +278/-26 (304 lines); hunks: -33,9 +33,11; -50,6 +52,7; symbols: __init__, ebias_weight_loader
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/minimax_m3_vl.py
@@ -2,68 +2,160 @@
+import itertools
-import re
-from typing import Dict, List, Optional, Tuple, Union
+from functools import cached_property
+from typing import Any, Dict, List, Optional, Tuple
+import torchvision.transforms.v2.functional as tvF
diff -- test/registered/unit/multimodal/test_minimax_m31_processor.py
@@ -0,0 +1,557 @@
+"""M3.1 media resize, per-request limits, and token expansion."""
+import asyncio
+import unittest
+from types import SimpleNamespace
+from unittest.mock import AsyncMock, Mock, patch
+import numpy as np
diff -- test/registered/unit/models/test_minimax_m31_model.py
@@ -0,0 +1,484 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/minimax_m3_vl.py` modified +637/-101; `python/sglang/srt/models/dspark_minimax.py` added +326/-0; `python/sglang/srt/models/minimax_m3.py` modified +278/-26; `python/sglang/srt/multimodal/processors/minimax_m31_media.py` added +82/-0; `python/sglang/srt/models/minimax_vl_common.py` modified +44/-13; `python/sglang/srt/models/minimax_m3_vl.py` modified +52/-2
  - tests: `test/registered/unit/multimodal/test_minimax_m31_processor.py` added +557/-0; `test/registered/unit/models/test_minimax_m31_model.py` added +484/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/kvcache/test_minimax_m31_hicache.py`, `test/registered/kernels/ops/speculative/test_dspark_fused_kv_write.py`, `test/registered/spec/dspark/test_dspark_dp_tier.py`, `test/registered/spec/dspark/test_dspark_draft_path_default.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46868 - [Feat] minimax-m3.1: Support DSpark on Hopper

- Link: https://github.com/sgl-project/sglang/pull/46868
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `test/registered/amd/test_minimax_rocm_verify.py`, `test/registered/unit/models/test_minimax_m31_model.py`; associated commits `b142fcde837e`
- Diff scope read: GitHub Pull Request files API returned 6 files, +44/-14, 184 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] minimax-m3.1: Support DSpark on Hopper"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `test/registered/unit/models/test_minimax_m31_model.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py`; technical summary: Covers "[Feat] minimax-m3.1: Support DSpark on Hopper"; the main implementation surface is `test/registered/unit/models/test_minimax_m31_model.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/models/test_minimax_m31_model.py` modified +18/-2 (20 lines); hunks: -85,6 +85,7 @@ def server_args(**kwargs):; -104,6 +105,7 @@ def packed_moe_hf(**quant_overrides):; symbols: server_args, packed_moe_hf, TestMiniMaxM31ConfigResolution, test_nvfp4_defaults_on_blackwell_and_portable_fallback, touching `server_args, packed_moe_hf, TestMiniMaxM31ConfigResolution`; `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +10/-7 (17 lines); hunks: -305,6 +305,9 @@ def __init__(self, runner: ModelRunner):; -425,7 +428,7 @@ def init_forward_metadata_out_graph(; symbols: __init__, init_forward_metadata_out_graph, _prepare_msa_decode_meta, touching `__init__, init_forward_metadata_out_graph, _prepare_msa_decode_meta`; `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py` modified +12/-3 (15 lines); hunks: -64,8 +64,8 @@ def _minimax_m3_overrides(server_args: Any, hf_config: Any) ->...; -78,12 +78,21 @@ def _minimax_m3_overrides(server_args: Any, hf_config: Any)...; symbols: _minimax_m3_overrides, touching `_minimax_m3_overrides`; `test/registered/amd/test_minimax_rocm_verify.py` modified +2/-2 (4 lines); hunks: -19,7 +19,7 @@ def setUp(self):; -41,7 +41,7 @@ def decode(q, k, v, layer, batch, save_kv_cache, **kwargs):; symbols: setUp, decode, run_verify, touching `setUp, decode, run_verify`.
- Code diff details:
  - `test/registered/unit/models/test_minimax_m31_model.py` modified +18/-2 (20 lines); hunks: -85,6 +85,7 @@ def server_args(**kwargs):; -104,6 +105,7 @@ def packed_moe_hf(**quant_overrides):; symbols: server_args, packed_moe_hf, TestMiniMaxM31ConfigResolution, test_nvfp4_defaults_on_blackwell_and_portable_fallback
  - `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +10/-7 (17 lines); hunks: -305,6 +305,9 @@ def __init__(self, runner: ModelRunner):; -425,7 +428,7 @@ def init_forward_metadata_out_graph(; symbols: __init__, init_forward_metadata_out_graph, _prepare_msa_decode_meta
  - `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py` modified +12/-3 (15 lines); hunks: -64,8 +64,8 @@ def _minimax_m3_overrides(server_args: Any, hf_config: Any) ->...; -78,12 +78,21 @@ def _minimax_m3_overrides(server_args: Any, hf_config: Any)...; symbols: _minimax_m3_overrides
  - `test/registered/amd/test_minimax_rocm_verify.py` modified +2/-2 (4 lines); hunks: -19,7 +19,7 @@ def setUp(self):; -41,7 +41,7 @@ def decode(q, k, v, layer, batch, save_kv_cache, **kwargs):; symbols: setUp, decode, run_verify
- Key code excerpts:

```diff
diff -- test/registered/unit/models/test_minimax_m31_model.py
@@ -85,6 +85,7 @@ def server_args(**kwargs):
+        speculative_draft_model_quantization=None,
@@ -104,6 +105,7 @@ def packed_moe_hf(**quant_overrides):
+        portable = base | dict(moe_runner_backend="marlin", attention_backend="fa3")
@@ -122,10 +124,17 @@ def test_nvfp4_defaults_on_blackwell_and_portable_fallback(self):
+            (False, None, portable),
+            # The draft's MXFP8 projections load as block-FP8 like the target's.
diff -- python/sglang/srt/layers/attention/minimax_sparse_backend.py
@@ -305,6 +305,9 @@ def __init__(self, runner: ModelRunner):
+        # Without NPU kernels or the MSA decode plan, a TARGET_VERIFY step runs the
+        # capture-safe decode kernels with one causal query per draft row.
+        self._linear_verify = not self.is_npu and not self._use_msa_decode
@@ -425,7 +428,7 @@ def init_forward_metadata_out_graph(
-            or (self.is_hip and forward_batch.forward_mode.is_target_verify())
+            or (self._linear_verify and forward_batch.forward_mode.is_target_verify())
diff -- python/sglang/srt/arg_groups/model_overrides/minimax_m3.py
@@ -64,8 +64,8 @@ def _minimax_m3_overrides(server_args: Any, hf_config: Any) -> dict:
```

- Reviewed files:
  - tests: `test/registered/unit/models/test_minimax_m31_model.py` modified +18/-2; `test/registered/amd/test_minimax_rocm_verify.py` modified +2/-2
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_backend.py` modified +10/-7; `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py` modified +12/-3
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_minimax_rocm_verify.py`, `test/registered/unit/models/test_minimax_m31_model.py`, `test/registered/unit/test_model_overrides.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #47303 - [Doc] cookbook: Add MiniMax-M3.1-Flash B300 TP2 SPF AgentX points

- Link: https://github.com/sgl-project/sglang/pull/47303
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; associated commits `d21312495642`
- Diff scope read: GitHub Pull Request files API returned 1 files, +331/-4, 376 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Add MiniMax-M3.1-Flash B300 TP2 SPF AgentX points"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; technical summary: Covers "[Doc] cookbook: Add MiniMax-M3.1-Flash B300 TP2 SPF AgentX points"; the main implementation surface is `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +331/-4 (335 lines); hunks: -1,13 +1,18; -2339,6 +2344,328 @@ export const agentx = {.
- Code diff details:
  - `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +331/-4 (335 lines); hunks: -1,13 +1,18; -2339,6 +2344,328 @@ export const agentx = {
- Key code excerpts:

```diff
diff -- docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx
@@ -1,13 +1,18 @@
-// (SemiAnalysisAI/InferenceX main@70a7601777e6 plus open PRs #4333, #4524, #4556, #4595, #4603, #4627), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@70a7601777e6 plus open PRs #4333, #4524, #4556, #4595, #4603, #4627, #4647), with SA-specific settings removed.
+   "4647": {
+    "run": "https://github.com/SemiAnalysisAI/InferenceX/actions/runs/40895671658",
+    "sha": "b623efbb700ba428206bda393658559d3c7dc631",
+    "status": "verified-pr"
```

- Reviewed files:
  - docs: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +331/-4
- Risk and verification: This is mostly docs/examples in `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #46627 - [Test] minimax-m3.1: Add nightly e2e tests on H200 and B300

- Link: https://github.com/sgl-project/sglang/pull/46627
- Status/date: merged / 2026-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py`, `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`; associated commits `0d01c3c12976`
- Diff scope read: GitHub Pull Request files API returned 3 files, +219/-0, 235 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Test] minimax-m3.1: Add nightly e2e tests on H200 and B300"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py`, `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`; technical summary: Covers "[Test] minimax-m3.1: Add nightly e2e tests on H200 and B300"; the main implementation surface is `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py`, `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: TestMiniMaxM31FlashGB300, setUpClass, tearDownClass, _storage_hit_tokens, touching `TestMiniMaxM31FlashGB300, setUpClass, tearDownClass`; `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` added +52/-0 (52 lines); hunks: -0,0 +1,52; symbols: TestMiniMaxM31FlashH200, touching `TestMiniMaxM31FlashH200`.
- Code diff details:
  - `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: TestMiniMaxM31FlashGB300, setUpClass, tearDownClass, _storage_hit_tokens
  - `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` added +52/-0 (52 lines); hunks: -0,0 +1,52; symbols: TestMiniMaxM31FlashH200
- Key code excerpts:

```diff
diff -- test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py
@@ -0,0 +1,126 @@
+"""MiniMax-M3.1-Flash on GB300 with the B300 balanced recipe, DSpark and HiCache.
+Covers the Blackwell path: MSA sparse attention, the TRT-LLM NVFP4 MoE, the
+bundled DSpark draft, and HiCache moving the NVFP4 page rows (packed KV, block
+scales, index K and draft KV) between GPU, host and file storage.
+"""
+import re
diff -- test/registered/e2e/models_large/test_minimax_m31_flash_h200.py
@@ -0,0 +1,52 @@
+"""MiniMax-M3.1-Flash on the H200 balanced recipe with DSpark.
+Hopper serves the NVFP4 experts through Marlin W4A16, runs the sparse attention
+without the Blackwell MSA kernels, and verifies DSpark drafts as per-row decode
+queries, so this recipe needs no extra install on the CI runner.
+"""
+import unittest
```

- Reviewed files:
  - tests: `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py` added +126/-0; `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` added +52/-0
- Risk and verification: The diff ships test coverage in `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py`, `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45174 - [Fix] Minimax-M3: Deterministic tie-breaking in the CUDA radix decode top-k

- Link: https://github.com/sgl-project/sglang/pull/45174
- Status/date: merged / 2026-10-31
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`; associated commits `006ad251695d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +69/-11, 137 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Minimax-M3: Deterministic tie-breaking in the CUDA radix decode top-k"; model line: MiniMax M2 Series; category: bug fix; main diff: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`; technical summary: Covers "[Fix] Minimax-M3: Deterministic tie-breaking in the CUDA radix decode top-k"; the main implementation surface is `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +46/-11 (57 lines); hunks: -62,7 +62,6 @@ struct TopKTraitImpl {; -372,6 +371,20 @@ struct TopKTraitImpl {; `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +23/-0 (23 lines); hunks: -118,6 +118,29 @@ def test_decode_topk_adversarial(kind):; symbols: test_decode_topk_adversarial, test_decode_topk_ties_pick_lowest_ids, test_decode_topk_small_num_blocks, touching `test_decode_topk_adversarial, test_decode_topk_ties_pick_lowest_ids, test_decode_topk_small_num_blocks`.
- Code diff details:
  - `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +46/-11 (57 lines); hunks: -62,7 +62,6 @@ struct TopKTraitImpl {; -372,6 +371,20 @@ struct TopKTraitImpl {
  - `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +23/-0 (23 lines); hunks: -118,6 +118,29 @@ def test_decode_topk_adversarial(kind):; symbols: test_decode_topk_adversarial, test_decode_topk_ties_pick_lowest_ids, test_decode_topk_small_num_blocks
- Key code excerpts:

```diff
diff -- python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh
@@ -62,7 +62,6 @@ struct TopKTraitImpl {
-    alignas(128) uint32_t counter_final;
@@ -372,6 +371,20 @@ struct TopKTraitImpl {
+    // Number of threads with a lower tx whose `flag` is set; called by the whole
+    // CTA. Final-round ties are exactly equal scores; ranking them by block id
+    // makes the selection deterministic (lower id wins, as in the small path).
+    const auto block_rank = [&](bool flag) -> uint32_t {
diff -- test/registered/kernels/ops/attention/test_minimax_decode_topk.py
@@ -118,6 +118,29 @@ def test_decode_topk_adversarial(kind):
+@pytest.mark.parametrize("nb", [300, 512, 2000, 3000, 9000])
+@pytest.mark.parametrize("levels", [2, 4, 1])
+def test_decode_topk_ties_pick_lowest_ids(nb, levels):
+    """Exactly equal scores are broken by block id (lower id wins), the same rule as
+    the small-row path, so repeated calls select the same blocks: one-element-per-
+    thread rows (nb <= 512) and register-bucket rows (nb > 512)."""
```

- Reviewed files:
  - runtime: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh` modified +46/-11
  - tests: `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` modified +23/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #47623 - [Doc] cookbook: Update MiniMax-M3.1-Flash AgentX launches

- Link: https://github.com/sgl-project/sglang/pull/47623
- Status/date: merged / 2026-10-31
- Trace source: `git log --name-only -- <model-files>` found it through `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; associated commits `7adb930d630f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +901/-1, 922 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Update MiniMax-M3.1-Flash AgentX launches"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; technical summary: Covers "[Doc] cookbook: Update MiniMax-M3.1-Flash AgentX launches"; the main implementation surface is `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +901/-1 (902 lines); hunks: -1,13 +1,23; -3538,6 +3548,896 @@ export const agentx = {.
- Code diff details:
  - `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +901/-1 (902 lines); hunks: -1,13 +1,23; -3538,6 +3548,896 @@ export const agentx = {
- Key code excerpts:

```diff
diff -- docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx
@@ -1,13 +1,23 @@
-// (SemiAnalysisAI/InferenceX main@ea8b34394a60 plus open PRs #4333, #4454, #4595, #4603, #4670), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@ea8b34394a60 plus open PRs #4333, #4454, #4595, #4603, #4670, #4675, #4676), with SA-specific settings removed.
+   "4676": {
+    "run": "https://github.com/SemiAnalysisAI/InferenceX/actions/runs/41054395691",
+    "sha": "51c91c3cfd2ad631fdb3fa9dd8a2c8d94f000194",
+    "status": "verified-pr"
```

- Reviewed files:
  - docs: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +901/-1
- Risk and verification: This is mostly docs/examples in `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #47699 - [Doc] cookbook: Add MiniMax-M3.1-Flash GB300 PD AgentX points

- Link: https://github.com/sgl-project/sglang/pull/47699
- Status/date: merged / 2026-11-01
- Trace source: `git log --name-only -- <model-files>` found it through `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; associated commits `592754fc5eb5`
- Diff scope read: GitHub Pull Request files API returned 1 files, +748/-1, 769 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Add MiniMax-M3.1-Flash GB300 PD AgentX points"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; technical summary: Covers "[Doc] cookbook: Add MiniMax-M3.1-Flash GB300 PD AgentX points"; the main implementation surface is `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +748/-1 (749 lines); hunks: -1,13 +1,18; -4438,6 +4443,748 @@ export const agentx = {.
- Code diff details:
  - `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +748/-1 (749 lines); hunks: -1,13 +1,18; -4438,6 +4443,748 @@ export const agentx = {
- Key code excerpts:

```diff
diff -- docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx
@@ -1,13 +1,18 @@
-// (SemiAnalysisAI/InferenceX main@ea8b34394a60 plus open PRs #4333, #4454, #4595, #4603, #4670, #4675, #4676), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@ea8b34394a60 plus open PRs #4333, #4454, #4595, #4603, #4670, #4675, #4676, #4686), with SA-specific settings removed.
+   "4686": {
+    "run": "https://github.com/SemiAnalysisAI/InferenceX/actions/runs/41185040680",
+    "sha": "8e3b3f1814224377d3a0c915f4441bed6640eb21",
+    "status": "verified-pr"
```

- Reviewed files:
  - docs: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +748/-1
- Risk and verification: This is mostly docs/examples in `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #47789 - [CI] nightly: Disable the MiniMax-M3.1-Flash H200 test while it times out

- Link: https://github.com/sgl-project/sglang/pull/47789
- Status/date: merged / 2026-11-01
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`; associated commits `cdc2f7d1b21d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-1, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] nightly: Disable the MiniMax-M3.1-Flash H200 test while it times out"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`; technical summary: Covers "[CI] nightly: Disable the MiniMax-M3.1-Flash H200 test while it times out"; the main implementation surface is `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` modified +6/-1 (7 lines); hunks: -11,7 +11,12; symbols: TestMiniMaxM31FlashH200, touching `TestMiniMaxM31FlashH200`.
- Code diff details:
  - `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` modified +6/-1 (7 lines); hunks: -11,7 +11,12; symbols: TestMiniMaxM31FlashH200
- Key code excerpts:

```diff
diff -- test/registered/e2e/models_large/test_minimax_m31_flash_h200.py
@@ -11,7 +11,12 @@
-register_cuda_ci(est_time=960, stage="nightly", runner_config="8-gpu-h200")
+register_cuda_ci(
+    est_time=960,
+    stage="nightly",
+    runner_config="8-gpu-h200",
+    disabled="times out on every nightly run; disabled while under investigation",
```

- Reviewed files:
  - tests: `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py` modified +6/-1
- Risk and verification: The diff ships test coverage in `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46690 - [Feat] [AMD] minimax: gfx950 sparse attention, NVFP4 KV and DSpark verify kernels

- Link: https://github.com/sgl-project/sglang/pull/46690
- Status/date: merged / 2026-11-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/nvfp4.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/nvfp4_gfx950.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/out_quant_gfx950.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` and 19 files; associated commits `03f90543787c`
- Diff scope read: GitHub Pull Request files API returned 25 files, +6495/-225, 7354 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] [AMD] minimax: gfx950 sparse attention, NVFP4 KV and DSpark verify kernels"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py`; technical summary: Covers "[Feat] [AMD] minimax: gfx950 sparse attention, NVFP4 KV and DSpark verify kernels"; the main implementation surface is `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0 (2 lines); hunks: -209,6 +209,8 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill, touching `minimax_sparse_prefill`; `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` modified +829/-29 (858 lines); hunks: -1,12 +1,40; -369,6 +397,463 @@ def sparse_qk_index_gemma_rmsnorm_rope(; symbols: _scale_cast_to_cache, _cache_inv_scale, _qk_gemma_rmsnorm_rope_kernel, sparse_qk_index_gemma_rmsnorm_rope, touching `_scale_cast_to_cache, _cache_inv_scale, _qk_gemma_rmsnorm_rope_kernel`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py` added +803/-0 (803 lines); hunks: -0,0 +1,803; symbols: _dim_layout, _idx, _k_dword_to_f16, _v_dwords_to_f16, touching `_dim_layout, _idx, _k_dword_to_f16`; `python/sglang/kernels/ops/attention/minimax_sparse/decode/verify_topk_gfx950.py` added +715/-0 (715 lines); hunks: -0,0 +1,715; symbols: _ordered, _key, _add, _split_plan, touching `_ordered, _key, _add`.
- Code diff details:
  - `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0 (2 lines); hunks: -209,6 +209,8 @@ def minimax_sparse_prefill(; symbols: minimax_sparse_prefill
  - `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` modified +829/-29 (858 lines); hunks: -1,12 +1,40; -369,6 +397,463 @@ def sparse_qk_index_gemma_rmsnorm_rope(; symbols: _scale_cast_to_cache, _cache_inv_scale, _qk_gemma_rmsnorm_rope_kernel, sparse_qk_index_gemma_rmsnorm_rope
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py` added +803/-0 (803 lines); hunks: -0,0 +1,803; symbols: _dim_layout, _idx, _k_dword_to_f16, _v_dwords_to_f16
  - `python/sglang/kernels/ops/attention/minimax_sparse/decode/verify_topk_gfx950.py` added +715/-0 (715 lines); hunks: -0,0 +1,715; symbols: _ordered, _key, _add, _split_plan
  - `python/sglang/kernels/ops/attention/minimax_sparse/prefill/index_topk_gfx950.py` added +632/-0 (632 lines); hunks: -0,0 +1,632; symbols: _min_with_idx, _row_offset, _load_k_block, _stage_k_block
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py
@@ -209,6 +209,8 @@ def minimax_sparse_prefill(
+                    k_scale=k_scale,
+                    v_scale=v_scale,
diff -- python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py
@@ -1,12 +1,40 @@
-from typing import Tuple
+from typing import Optional, Tuple, Union
+import numpy as np
+from sglang.kernels.ops.attention.minimax_sparse.common.nvfp4 import (
+    Nvfp4Cache,
+    nvfp4_f32_to_e2m1,
diff -- python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py
@@ -0,0 +1,803 @@
+"""Sparse decode over the packed NVFP4 (MSA-v1) K/V cache for gfx950, in Gluon.
+One program per (row, top-k chunk, kv head) with 4 warps; warp w owns tokens 32w..32w+31
+of every selected block and keeps its own online softmax, merged across warps at the end,
+so the block loop has no LDS traffic and no barrier. K and V go from global memory
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` modified +2/-0; `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py` modified +829/-29; `python/sglang/kernels/ops/attention/minimax_sparse/decode/nvfp4_decode_gfx950.py` added +803/-0; `python/sglang/kernels/ops/attention/minimax_sparse/decode/verify_topk_gfx950.py` added +715/-0; `python/sglang/kernels/ops/attention/minimax_sparse/prefill/index_topk_gfx950.py` added +632/-0; `python/sglang/kernels/ops/attention/minimax_sparse/decode/verify_topk_idx.py` added +492/-0
  - tests: `test/registered/kernels/ops/attention/test_minimax_gfx950_prefill.py` added +526/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/quant_ref_utils.py`, `test/registered/attention/test_verify_shared_kv.py`, `test/registered/kernels/ops/attention/test_minimax_gfx950_prefill.py`, `test/registered/kernels/ops/attention/test_minimax_m3_qk_norm_rope.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #46691 - [Feat] [AMD] minimax: gfx950 MoE, router GEMV, block-fp8 GEMM and fp8 producer kernels

- Link: https://github.com/sgl-project/sglang/pull/46691
- Status/date: merged / 2026-11-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py`, `test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py`; associated commits `e37c1fb020ac`
- Diff scope read: GitHub Pull Request files API returned 23 files, +3843/-65, 4325 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] [AMD] minimax: gfx950 MoE, router GEMV, block-fp8 GEMM and fp8 producer kernels"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py`, `test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py`; technical summary: Covers "[Feat] [AMD] minimax: gfx950 MoE, router GEMV, block-fp8 GEMM and fp8 producer kernels"; the main implementation surface is `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py`, `test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py` modified +250/-0 (250 lines); hunks: -10,10 +10,17; -86,6 +93,172 @@ def _gemma_fused_add_rmsnorm_kernel(; symbols: _gemma_fused_add_rmsnorm_kernel, _gemma_add_rmsnorm_fp8_kernel, _gemma_add_rmsnorm_fp8_4rows_kernel, _num_warps, touching `_gemma_fused_add_rmsnorm_kernel, _gemma_add_rmsnorm_fp8_kernel, _gemma_add_rmsnorm_fp8_4rows_kernel`; `test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py` modified +144/-1 (145 lines); hunks: -4,7 +4,7; -15,15 +15,24; symbols: _gemma_rmsnorm_ref, test_gemma_fused_add_rmsnorm_matches_reference, _bits, _norm_then_quant, touching `_gemma_rmsnorm_ref, test_gemma_fused_add_rmsnorm_matches_reference, _bits`.
- Code diff details:
  - `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py` modified +250/-0 (250 lines); hunks: -10,10 +10,17; -86,6 +93,172 @@ def _gemma_fused_add_rmsnorm_kernel(; symbols: _gemma_fused_add_rmsnorm_kernel, _gemma_add_rmsnorm_fp8_kernel, _gemma_add_rmsnorm_fp8_4rows_kernel, _num_warps
  - `test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py` modified +144/-1 (145 lines); hunks: -4,7 +4,7; -15,15 +15,24; symbols: _gemma_rmsnorm_ref, test_gemma_fused_add_rmsnorm_matches_reference, _bits, _norm_then_quant
- Key code excerpts:

```diff
diff -- python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py
@@ -10,10 +10,17 @@
+from typing import Optional
+from sglang.kernels.ops.quantization.aiter_fp8_quant_triton import (
+    fp8_group_quant,
+    fp8_per_token_quant,
+)
@@ -86,6 +93,172 @@ def _gemma_fused_add_rmsnorm_kernel(
diff -- test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py
@@ -4,7 +4,7 @@
-from sglang.srt.utils import is_hip
+from sglang.srt.utils import is_gfx95_supported, is_hip
@@ -15,15 +15,24 @@
+    _FOUR_ROWS_MIN_ROWS,
+    gemma_add_rmsnorm_fp8,
+# the fp8 producer cases need gfx95; the MI300 kernel job runs the others
```

- Reviewed files:
  - runtime: `python/sglang/kernels/ops/layernorm/minimax_m3_rmsnorm.py` modified +250/-0
  - tests: `test/registered/kernels/ops/layernorm/test_minimax_m3_rmsnorm.py` modified +144/-1
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_aiter_moe_addend.py`, `test/registered/amd/test_m31_router_gfx950.py`, `test/registered/amd/test_moe_sort_quant_large.py`, `test/registered/amd/test_moe_sorting_small.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #47791 - [Doc] cookbook: Sync MiniMax-M3.1-Flash GB300 AgentX points

- Link: https://github.com/sgl-project/sglang/pull/47791
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; associated commits `2b38f4a6edc4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +831/-463, 1436 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Sync MiniMax-M3.1-Flash GB300 AgentX points"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; technical summary: Covers "[Doc] cookbook: Sync MiniMax-M3.1-Flash GB300 AgentX points"; the main implementation surface is `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +831/-463 (1294 lines); hunks: -1,16 +1,16; -4463,50 +4463,31 @@ export const agentx = {.
- Code diff details:
  - `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +831/-463 (1294 lines); hunks: -1,16 +1,16; -4463,50 +4463,31 @@ export const agentx = {
- Key code excerpts:

```diff
diff -- docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx
@@ -1,16 +1,16 @@
-// (SemiAnalysisAI/InferenceX main@ea8b34394a60 plus open PRs #4333, #4454, #4595, #4603, #4670, #4675, #4676, #4686), with SA-specific settings removed.
+// (SemiAnalysisAI/InferenceX main@ea8b34394a60 plus open PRs #4333, #4454, #4595, #4603, #4670, #4675, #4676, #4698), with SA-specific settings removed.
-   "4686": {
-    "run": "https://github.com/SemiAnalysisAI/InferenceX/actions/runs/41185040680",
-    "sha": "8e3b3f1814224377d3a0c915f4441bed6640eb21",
+   "4698": {
```

- Reviewed files:
  - docs: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +831/-463
- Risk and verification: This is mostly docs/examples in `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #47675 - [Refactor] memory-pool: Build MiniMax K-only index host pools from buffer info

- Link: https://github.com/sgl-project/sglang/pull/47675
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`; associated commits `a7c9c3cad0e6`
- Diff scope read: GitHub Pull Request files API returned 9 files, +336/-97, 742 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] memory-pool: Build MiniMax K-only index host pools from buffer info"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`; technical summary: Covers "[Refactor] memory-pool: Build MiniMax K-only index host pools from buffer info"; the main implementation surface is `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py` modified +133/-62 (195 lines); hunks: -1,20 +1,18; -59,7 +57,56 @@ def _make_cpu_minimax_sparse_pool(start_layer: int = 4) -> Mi...; symbols: _make_cpu_minimax_sparse_pool, TestMiniMaxSparseHiCacheIntegration, test_k_only_page_axes_keep_token_addresses, test_index_k_waits_for_full_local_layer, touching `_make_cpu_minimax_sparse_pool, TestMiniMaxSparseHiCacheIntegration, test_k_only_page_axes_keep_token_addresses`.
- Code diff details:
  - `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py` modified +133/-62 (195 lines); hunks: -1,20 +1,18; -59,7 +57,56 @@ def _make_cpu_minimax_sparse_pool(start_layer: int = 4) -> Mi...; symbols: _make_cpu_minimax_sparse_pool, TestMiniMaxSparseHiCacheIntegration, test_k_only_page_axes_keep_token_addresses, test_index_k_waits_for_full_local_layer
- Key code excerpts:

```diff
diff -- test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py
@@ -1,20 +1,18 @@
+from unittest.mock import patch
-from sglang.srt.mem_cache.memory_pool import MiniMaxSparseKVPool
+from sglang.srt.mem_cache.memory_pool import MHATokenToKOnlyPool, MiniMaxSparseKVPool
-from sglang.srt.mem_cache.pool_host.common import (
-    ALLOC_MEMORY_FUNCS,
-    alloc_with_pin_memory,
```

- Reviewed files:
  - tests: `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py` modified +133/-62
- Risk and verification: The diff ships test coverage in `test/registered/hicache/test_k_only_host_release.py`, `test/registered/unit/mem_cache/test_hicache_host_register.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #47844 - [Doc] [AMD] cookbook: Verify MiniMax-M3.1-Flash High-Throughput on MI355X

- Link: https://github.com/sgl-project/sglang/pull/47844
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`; associated commits `3e884832882a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +8/-4, 42 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] [AMD] cookbook: Verify MiniMax-M3.1-Flash High-Throughput on MI355X"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`; technical summary: Covers "[Doc] [AMD] cookbook: Verify MiniMax-M3.1-Flash High-Throughput on MI355X"; the main implementation surface is `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` modified +7/-3 (10 lines); hunks: -801,10 +801,13 @@ const cfg = {; -813,7 +816,6 @@ const cfg = {; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +1/-1 (2 lines); hunks: -146,7 +146,7 @@ The B300 **Low-Latency** recipe serves batch-size-1 decode t....
- Code diff details:
  - `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` modified +7/-3 (10 lines); hunks: -801,10 +801,13 @@ const cfg = {; -813,7 +816,6 @@ const cfg = {
  - `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +1/-1 (2 lines); hunks: -146,7 +146,7 @@ The B300 **Low-Latency** recipe serves batch-size-1 decode t...
- Key code excerpts:

```diff
diff -- docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx
@@ -801,10 +801,13 @@ const cfg = {
+    // AgentX at 48 and 64 sessions on MI355X: GSM8K 96.59 at 64. Registered pageable host
+    // pools fault at the first HiCache write, so HSA_USERPTR_FOR_PAGED_MEM=0 allocates them
+    // with hipHostMalloc (#42553); 180 GB per rank fits two servers per host.
-      warn: AMD_HICACHE_NOTE,
-      env: ["SGLANG_USE_AITER=1"],
+      verified: true,
diff -- docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx
@@ -146,7 +146,7 @@ The B300 **Low-Latency** recipe serves batch-size-1 decode through the MSA-V1 Mo
-- The High-Throughput recipe was measured on MI350X. MI355X runs the same command but has not been measured with it.
+- **High-Throughput on MI355X** sets `--hicache-size 180 --hicache-write-policy write_back` and `HSA_USERPTR_FOR_PAGED_MEM=0`, and keeps the default bf16 draft KV cache. The envir
```

- Reviewed files:
  - docs: `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx` modified +7/-3; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx` modified +1/-1
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #48070 - [Doc] cookbook: Add MiniMax-M3.1-Flash GB300 MonoKernel and DEP16 AgentX points

- Link: https://github.com/sgl-project/sglang/pull/48070
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; associated commits `c68083d53c54`
- Diff scope read: GitHub Pull Request files API returned 1 files, +127/-14, 229 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Add MiniMax-M3.1-Flash GB300 MonoKernel and DEP16 AgentX points"; model line: MiniMax M2 Series; category: performance/backend optimization; main diff: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; technical summary: Covers "[Doc] cookbook: Add MiniMax-M3.1-Flash GB300 MonoKernel and DEP16 AgentX points"; the main implementation surface is `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +127/-14 (141 lines); hunks: -8,6 +8,11 @@ export const agentx = {; -247,7 +252,7 @@ export const agentx = {.
- Code diff details:
  - `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +127/-14 (141 lines); hunks: -8,6 +8,11 @@ export const agentx = {; -247,7 +252,7 @@ export const agentx = {
- Key code excerpts:

```diff
diff -- docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx
@@ -8,6 +8,11 @@ export const agentx = {
+   "4750": {
+    "run": "https://github.com/SemiAnalysisAI/InferenceX/actions/runs/41528865560",
+    "sha": "6528aa7c4341e9027ed152fa280fa22f32363b1f",
+    "status": "verified-pr"
+   },
@@ -247,7 +252,7 @@ export const agentx = {
```

- Reviewed files:
  - docs: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx` modified +127/-14
- Risk and verification: This is mostly docs/examples in `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #47187 - [Doc] minimax-m3: Route GB300 decode to trtllm_mha in the cookbook recipe (prefill stays fa4)

- Link: https://github.com/sgl-project/sglang/pull/47187
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`; associated commits `77b6e593e40f`
- Diff scope read: GitHub Pull Request files API returned 3 files, +73/-112, 304 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] minimax-m3: Route GB300 decode to trtllm_mha in the cookbook recipe (prefill stays fa4)"; model line: MiniMax M2 Series; category: docs/tests/CI; main diff: `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`; technical summary: Covers "[Doc] minimax-m3: Route GB300 decode to trtllm_mha in the cookbook recipe (prefill stays fa4)"; the main implementation surface is `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx` modified +40/-50 (90 lines); hunks: -1,81 +1,71; `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx` modified +18/-17 (35 lines); hunks: -92,16 +92,14 @@ sgl-eval run mmmu_pro \\; -199,10 +197,9 @@ sgl-eval run mmmu_pro \\; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` modified +15/-45 (60 lines); hunks: -19,29 +19,25 @@ For all methods and hardware platforms, see the [official SG...; -75,7 +71,7 @@ Key characteristics as served by SGLang:.
- Code diff details:
  - `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx` modified +40/-50 (90 lines); hunks: -1,81 +1,71
  - `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx` modified +18/-17 (35 lines); hunks: -92,16 +92,14 @@ sgl-eval run mmmu_pro \\; -199,10 +197,9 @@ sgl-eval run mmmu_pro \\
  - `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` modified +15/-45 (60 lines); hunks: -19,29 +19,25 @@ For all methods and hardware platforms, see the [official SG...; -75,7 +71,7 @@ Key characteristics as served by SGLang:
- Key code excerpts:

```diff
diff -- docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx
@@ -1,81 +1,71 @@
-// SPEED — bench_serving --flush-cache, random isl2048/osl256, max_concurrency 64,
-// CUDA graph on. B200 (tp8, MXFP8, MSA fmha_sm100 path; re-measured 2026-06-15
-// with piecewise CUDA graph default-on) and H200 (tp8, bf16, built-in Triton
-// sparse) are measured on PR #27944 — warm steady-state from a 3-run sweep (the
-// B200 3-run is identical; the H200 cold-start first run, ~2x slower, is
-// excluded). B300 / GB300
diff -- docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx
@@ -92,16 +92,14 @@ sgl-eval run mmmu_pro \\
-    // M3-specific dev images (multi-arch amd64+arm64). cu13 carries the sm_103
-    // (B300/GB300) + Grace arm64 builds; cu12 is the final Hopper/CUDA-12 build
-    // (that lane is retired, so it no longer rebuilds); dev-minimax-m3 is the
-    // rolling default. M3 model support is not yet in a tagged release, so
-    // :latest cannot serve it.
-    b200: "lmsysorg/sglang:dev-minimax-m3",
diff -- docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx
@@ -19,29 +19,25 @@ For all methods and hardware platforms, see the [official SGLang installation gu
```

- Reviewed files:
  - docs: `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx` modified +40/-50; `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx` modified +18/-17; `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` modified +15/-45
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
