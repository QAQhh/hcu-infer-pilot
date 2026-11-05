# sglang DeepSeek V3.2 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/docs/references/multi_node_deployment/rbg_pd/deepseekv32_pd.mdx` | no direct PR-number commit |
| `examples/chat_template/tool_chat_template_deepseekv32.jinja` | [#11063](https://github.com/sgl-project/sglang/pull/11063) |
| `python/sglang/kernels/jit/csrc/deepseek_v32/indexer_k.cuh` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` | no direct PR-number commit |
| `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` | [#14249](https://github.com/sgl-project/sglang/pull/14249), [#14353](https://github.com/sgl-project/sglang/pull/14353) |
| `python/sglang/srt/function_call/deepseekv32_detector.py` | [#14249](https://github.com/sgl-project/sglang/pull/14249), [#14573](https://github.com/sgl-project/sglang/pull/14573), [#14750](https://github.com/sgl-project/sglang/pull/14750), [#15278](https://github.com/sgl-project/sglang/pull/15278), [#16091](https://github.com/sgl-project/sglang/pull/16091), [#18174](https://github.com/sgl-project/sglang/pull/18174), [#25233](https://github.com/sgl-project/sglang/pull/25233) |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | [#13959](https://github.com/sgl-project/sglang/pull/13959), [#14541](https://github.com/sgl-project/sglang/pull/14541), [#14572](https://github.com/sgl-project/sglang/pull/14572), [#15381](https://github.com/sgl-project/sglang/pull/15381), [#17007](https://github.com/sgl-project/sglang/pull/17007), [#19428](https://github.com/sgl-project/sglang/pull/19428), [#23268](https://github.com/sgl-project/sglang/pull/23268), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_common/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/a8w8_blockscale_bpreshuffle_tuned_gemm.csv` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=2048-K=7168.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=7168-K=2048.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=8192-K=1536.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_tune.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_act.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_moe.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | [#18931](https://github.com/sgl-project/sglang/pull/18931), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | [#21405](https://github.com/sgl-project/sglang/pull/21405), [#21511](https://github.com/sgl-project/sglang/pull/21511), [#24125](https://github.com/sgl-project/sglang/pull/24125), [#24392](https://github.com/sgl-project/sglang/pull/24392), [#25821](https://github.com/sgl-project/sglang/pull/25821), [#31888](https://github.com/sgl-project/sglang/pull/31888) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/triton_qk_rmsnorm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | [#27705](https://github.com/sgl-project/sglang/pull/27705) |
| `python/sglang/srt/models/deepseek_common/moe_transport.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/utils.py` | [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_v2.py` | [#11061](https://github.com/sgl-project/sglang/pull/11061), [#11510](https://github.com/sgl-project/sglang/pull/11510), [#11892](https://github.com/sgl-project/sglang/pull/11892), [#12065](https://github.com/sgl-project/sglang/pull/12065), [#12094](https://github.com/sgl-project/sglang/pull/12094), [#12788](https://github.com/sgl-project/sglang/pull/12788), [#12816](https://github.com/sgl-project/sglang/pull/12816), [#12964](https://github.com/sgl-project/sglang/pull/12964), [#13459](https://github.com/sgl-project/sglang/pull/13459), [#13544](https://github.com/sgl-project/sglang/pull/13544), [#13959](https://github.com/sgl-project/sglang/pull/13959), [#14572](https://github.com/sgl-project/sglang/pull/14572), ... (25 total) |
| `test/manual/nightly/test_deepseek_v32_perf.py` | [#13646](https://github.com/sgl-project/sglang/pull/13646), [#21192](https://github.com/sgl-project/sglang/pull/21192), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/manual/quant/test_deepseek_v32_fp4_4gpu.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_dp_eval_amd.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_eval_amd.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_mtp_eval_amd.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_tc_eval_amd.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` | [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` | [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/perf/mi30x/test_deepseek_v32_basic_perf_amd.py` | no direct PR-number commit |
| `test/registered/amd/perf/mi30x/test_deepseek_v32_mtp_perf_amd.py` | no direct PR-number commit |
| `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/test_deepseek_v32_basic.py` | [#16934](https://github.com/sgl-project/sglang/pull/16934), [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17432](https://github.com/sgl-project/sglang/pull/17432), [#17633](https://github.com/sgl-project/sglang/pull/17633), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/test_deepseek_v32_mtp.py` | [#16934](https://github.com/sgl-project/sglang/pull/16934), [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17432](https://github.com/sgl-project/sglang/pull/17432), [#17633](https://github.com/sgl-project/sglang/pull/17633), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/e2e/models_large/test_deepseek_v32_indexcache.py` | no direct PR-number commit |
| `test/registered/unit/function_call/test_deepseekv32_detector.py` | no direct PR-number commit |
| `test/registered/unit/model_executor/test_compensated_mhc_update_guard.py` | no direct PR-number commit |
| `test/registered/xpu/llm_models/test_xpu_deepseek_v2_lite_chat_fp8_gsm8k_eval.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 49
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 49
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2025-10-05 | [#11063](https://github.com/sgl-project/sglang/pull/11063) | merged | Add DeepSeek-V3.2 Tool Call Template | `examples/chat_template/tool_chat_template_deepseekv32.jinja` |
| 2025-10-06 | [#11061](https://github.com/sgl-project/sglang/pull/11061) | merged | Support DeepSeek V3.2 Exp | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-10-16 | [#11510](https://github.com/sgl-project/sglang/pull/11510) | merged | [Bugfix] Fix Qwen3/DSV3/DSV3.2 model support | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-10-30 | [#12094](https://github.com/sgl-project/sglang/pull/12094) | merged | Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-06 | [#11892](https://github.com/sgl-project/sglang/pull/11892) | merged | DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-07 | [#12788](https://github.com/sgl-project/sglang/pull/12788) | merged | [DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100) | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-07 | [#12816](https://github.com/sgl-project/sglang/pull/12816) | merged | [Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-17 | [#12065](https://github.com/sgl-project/sglang/pull/12065) | merged | (1/n)support context parallel with deepseekv3.2-DSA | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-20 | [#12964](https://github.com/sgl-project/sglang/pull/12964) | merged | [DeepseekV3.2] Deepseek fp8 support for MHA path | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-20 | [#13459](https://github.com/sgl-project/sglang/pull/13459) | merged | [Deepseek V3.2] Change indexer weights_proj to fp32 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-25 | [#13544](https://github.com/sgl-project/sglang/pull/13544) | merged | [DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-30 | [#13646](https://github.com/sgl-project/sglang/pull/13646) | merged | [DeepSeekV3.2] Enable pure TP & Partial DP Attention | `test/manual/nightly/test_deepseek_v32_perf.py`, `test/nightly/test_deepseek_v32_perf.py` |
| 2025-12-02 | [#14249](https://github.com/sgl-project/sglang/pull/14249) | merged | feat: DeepSeek new v3.2 encoding | `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2025-12-08 | [#14573](https://github.com/sgl-project/sglang/pull/14573) | merged | [Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2025-12-11 | [#14541](https://github.com/sgl-project/sglang/pull/14541) | merged | [NPU]dsv3.2 cp for npu | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2025-12-12 | [#14572](https://github.com/sgl-project/sglang/pull/14572) | merged | [NPU] optimization for dsv3.2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2025-12-18 | [#15278](https://github.com/sgl-project/sglang/pull/15278) | merged | feat: DeepSeek-V3.2 Streaming tool call output | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2025-12-19 | [#14353](https://github.com/sgl-project/sglang/pull/14353) | merged | feat(dsv32): better error handling for DeepSeek-v3.2 encoder | `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` |
| 2025-12-21 | [#14901](https://github.com/sgl-project/sglang/pull/14901) | merged | fix ds3.2 nsa backend prefill TBO | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-26 | [#14750](https://github.com/sgl-project/sglang/pull/14750) | merged | [Tool Call][DSV32] Streamline function call parameters | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-01-02 | [#13959](https://github.com/sgl-project/sglang/pull/13959) | merged | [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-01-10 | [#16637](https://github.com/sgl-project/sglang/pull/16637) | merged | [DSv32] Overlap indexer weights_proj during dual_stream decode | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-14 | [#16841](https://github.com/sgl-project/sglang/pull/16841) | merged | [AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-16 | [#16934](https://github.com/sgl-project/sglang/pull/16934) | merged | [AMD] Enable DeepseekV3.2 test for AMD CI | `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_deepseek_v32_basic.py` |
| 2026-01-20 | [#17179](https://github.com/sgl-project/sglang/pull/17179) | merged | [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests | `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` |
| 2026-01-22 | [#17432](https://github.com/sgl-project/sglang/pull/17432) | merged | [AMD] fix amd ci dpskv32 | `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py` |
| 2026-01-23 | [#17007](https://github.com/sgl-project/sglang/pull/17007) | merged | [NPU]bugfix: fix for dsv3.2 and dsvl2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-01-26 | [#15381](https://github.com/sgl-project/sglang/pull/15381) | merged | [NPU]DeepSeek-V3.2 support npu mlaprolog | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-01-28 | [#17633](https://github.com/sgl-project/sglang/pull/17633) | merged | [AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites | `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py` |
| 2026-01-28 | [#17523](https://github.com/sgl-project/sglang/pull/17523) | merged | [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI | `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` |
| 2026-02-10 | [#18297](https://github.com/sgl-project/sglang/pull/18297) | merged | Deepseekv32 compatibility with transformers v5 | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-15 | [#16907](https://github.com/sgl-project/sglang/pull/16907) | merged | Fix model loading for DeepSeek-V3.2-AWQ | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-16 | [#18389](https://github.com/sgl-project/sglang/pull/18389) | merged | Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-20 | [#18931](https://github.com/sgl-project/sglang/pull/18931) | merged | Fix NSA FP8 KV cache path for both-trtllm MHA one-shot | `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-03-02 | [#19428](https://github.com/sgl-project/sglang/pull/19428) | merged | [Feature] add feature mla_ag_after_qlora for dsv3.2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-03-03 | [#18174](https://github.com/sgl-project/sglang/pull/18174) | merged | [Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-03-03 | [#16091](https://github.com/sgl-project/sglang/pull/16091) | merged | [Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format. | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-03-23 | [#21192](https://github.com/sgl-project/sglang/pull/21192) | merged | Fix CP in-seq-split method for DeepSeek V32 and update related tests | `test/manual/nightly/test_deepseek_v32_perf.py` |
| 2026-04-03 | [#21511](https://github.com/sgl-project/sglang/pull/21511) | merged | [AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend | `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |
| 2026-04-05 | [#21405](https://github.com/sgl-project/sglang/pull/21405) | merged | Enable IndexCache for DeepSeek V3.2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |
| 2026-04-20 | [#22914](https://github.com/sgl-project/sglang/pull/22914) | merged | [Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-04-28 | [#23268](https://github.com/sgl-project/sglang/pull/23268) | merged | 【NPU】【bugfix】accuracy fix when enable both nsa cp and prefixcache | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-05-05 | [#24392](https://github.com/sgl-project/sglang/pull/24392) | merged | add indexer-topk capture (V3.2 NSA + infra) | `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |
| 2026-05-13 | [#24125](https://github.com/sgl-project/sglang/pull/24125) | merged | [AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode | `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |
| 2026-05-15 | [#25233](https://github.com/sgl-project/sglang/pull/25233) | merged | [Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-05-20 | [#25821](https://github.com/sgl-project/sglang/pull/25821) | merged | [Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename | `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-05-22 | [#23351](https://github.com/sgl-project/sglang/pull/23351) | merged | Support piecewise CUDA graph with NSA | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-06-27 | [#27705](https://github.com/sgl-project/sglang/pull/27705) | merged | Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-07-30 | [#31888](https://github.com/sgl-project/sglang/pull/31888) | merged | [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |

## Per-PR Diff Audit Cards

### PR #11063 - Add DeepSeek-V3.2 Tool Call Template

- Link: https://github.com/sgl-project/sglang/pull/11063
- Status/date: merged / 2025-10-05
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv32.jinja`; associated commits `85c1f7937781`
- Diff scope read: GitHub Pull Request files API returned 1 files, +100/-0, 101 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add DeepSeek-V3.2 Tool Call Template"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `examples/chat_template/tool_chat_template_deepseekv32.jinja`; technical summary: Covers "Add DeepSeek-V3.2 Tool Call Template"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv32.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/chat_template/tool_chat_template_deepseekv32.jinja` added +100/-0 (100 lines); hunks: -0,0 +1,100.
- Code diff details:
  - `examples/chat_template/tool_chat_template_deepseekv32.jinja` added +100/-0 (100 lines); hunks: -0,0 +1,100
- Key code excerpts:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv32.jinja
@@ -0,0 +1,100 @@
+{% if not add_generation_prompt is defined %}
+  {% set add_generation_prompt = false %}
+{% endif %}
+{% if not thinking is defined %}
+  {% set thinking = false %}
+{% endif %}
```

- Reviewed files:
  - docs: `examples/chat_template/tool_chat_template_deepseekv32.jinja` added +100/-0
- Risk and verification: This is mostly docs/examples in `examples/chat_template/tool_chat_template_deepseekv32.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #11061 - Support DeepSeek V3.2 Exp

- Link: https://github.com/sgl-project/sglang/pull/11061
- Status/date: merged / 2025-10-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `efbc687c2817`
- Diff scope read: GitHub Pull Request files API returned 29 files, +4542/-141, 5365 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support DeepSeek V3.2 Exp"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Support DeepSeek V3.2 Exp"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +329/-17 (346 lines); hunks: -15,6 +15,7; -25,10 +26,16; symbols: AttnForwardMethod, handle_attention_ascend, _get_sum_extend_prefix_lens, _is_extend_without_speculative, touching `AttnForwardMethod, handle_attention_ascend, _get_sum_extend_prefix_lens`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +329/-17 (346 lines); hunks: -15,6 +15,7; -25,10 +26,16; symbols: AttnForwardMethod, handle_attention_ascend, _get_sum_extend_prefix_lens, _is_extend_without_speculative
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -15,6 +15,7 @@
+from __future__ import annotations
@@ -25,10 +26,16 @@
-from tqdm import tqdm
+from sglang.srt.configs.model_config import (
+    get_nsa_index_head_dim,
+    get_nsa_index_n_heads,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +329/-17
- Risk and verification: The diff ships test coverage in `python/sglang/test/get_logits_ut.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #11510 - [Bugfix] Fix Qwen3/DSV3/DSV3.2 model support

- Link: https://github.com/sgl-project/sglang/pull/11510
- Status/date: merged / 2025-10-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `3cceaa381ad3`
- Diff scope read: GitHub Pull Request files API returned 12 files, +102/-33, 359 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1357,6 +1357,7 @@ def forward_prepare(; symbols: forward_prepare, touching `forward_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1357,6 +1357,7 @@ def forward_prepare(; symbols: forward_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1357,6 +1357,7 @@ def forward_prepare(
+                inner_state = (*inner_state, None)  # add a position for topk_indices
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `test/srt/ascend/test_ascend_deepep.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #12094 - Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4

- Link: https://github.com/sgl-project/sglang/pull/12094
- Status/date: merged / 2025-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `9ff9fa7f95be`
- Diff scope read: GitHub Pull Request files API returned 2 files, +110/-22, 231 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +65/-0 (65 lines); hunks: -224,6 +224,17 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1143,6 +1154,9 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__, touching `add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +65/-0 (65 lines); hunks: -224,6 +224,17 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1143,6 +1154,9 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -224,6 +224,17 @@ def add_forward_absorb_core_attention_backend(backend_name):
+def is_nsa_indexer_wk_and_weights_proj_fused(config, quant_config):
+    """
+    NSA Indexer wk and weights_proj can be fused in FP4 model because they are both in BF16
+    """
+    return (
+        is_deepseek_nsa(config)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +65/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11892 - DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill

- Link: https://github.com/sgl-project/sglang/pull/11892
- Status/date: merged / 2025-11-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `f235498eca7a`
- Diff scope read: GitHub Pull Request files API returned 3 files, +188/-4, 255 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +43/-2 (45 lines); hunks: -402,6 +402,34 @@ def handle_attention_aiter(attn, forward_batch):; -1478,8 +1506,21 @@ def forward_normal_prepare(; symbols: handle_attention_aiter, handle_attention_nsa, forward_normal_prepare, touching `handle_attention_aiter, handle_attention_nsa, forward_normal_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +43/-2 (45 lines); hunks: -402,6 +402,34 @@ def handle_attention_aiter(attn, forward_batch):; -1478,8 +1506,21 @@ def forward_normal_prepare(; symbols: handle_attention_aiter, handle_attention_nsa, forward_normal_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -402,6 +402,34 @@ def handle_attention_aiter(attn, forward_batch):
+    """
+    Select MHA or MLA based on sequence length for optimal performance.
+    - Decode: MLA (avoids per-token decompression)
+    - Prefill <= 2048: MHA (topk ineffective, MHA has lower FLOPs)
+    - Prefill > 2048: MLA (topk filtering reduces computation significantly)
+    TODO: B200 (SM100) MHA path is temporarily disabled due to FA4 gpqa accuracy issues.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +43/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12788 - [DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)

- Link: https://github.com/sgl-project/sglang/pull/12788
- Status/date: merged / 2025-11-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `7257525ccea6`
- Diff scope read: GitHub Pull Request files API returned 2 files, +53/-6, 96 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -415,11 +415,14 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, touching `handle_attention_nsa`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -415,11 +415,14 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -415,11 +415,14 @@ def handle_attention_nsa(attn, forward_batch):
-        # B200 (SM100) is temporarily disabled for MHA due to FA4 accuracy issues
-        # Currently only H200 (SM90) with FA3 is allowed to use MHA path
-        is_hopper = _device_sm == 90
+        # MHA path enabled for both H200 (SM90, FA3) and B200 (SM100, TRTLLm ragged)
+        # B200 uses trtllm_ragged_attention_deepseek kernel instead of FA4
+        supports_mha = _device_sm in [90, 100]
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12816 - [Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative

- Link: https://github.com/sgl-project/sglang/pull/12816
- Status/date: merged / 2025-11-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `bef37d6de86a`
- Diff scope read: GitHub Pull Request files API returned 3 files, +20/-18, 112 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +6/-14 (20 lines); hunks: -308,14 +308,6 @@ def _get_sum_extend_prefix_lens(forward_batch):; -334,7 +326,7 @@ def _handle_attention_backend(; symbols: _get_sum_extend_prefix_lens, _is_extend_without_speculative, _support_mha_one_shot, _handle_attention_backend, touching `_get_sum_extend_prefix_lens, _is_extend_without_speculative, _support_mha_one_shot`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +6/-14 (20 lines); hunks: -308,14 +308,6 @@ def _get_sum_extend_prefix_lens(forward_batch):; -334,7 +326,7 @@ def _handle_attention_backend(; symbols: _get_sum_extend_prefix_lens, _is_extend_without_speculative, _support_mha_one_shot, _handle_attention_backend
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -308,14 +308,6 @@ def _get_sum_extend_prefix_lens(forward_batch):
-def _is_extend_without_speculative(forward_batch):
-    return (
-        forward_batch.forward_mode.is_extend()
-        and not forward_batch.forward_mode.is_target_verify()
-        and not forward_batch.forward_mode.is_draft_extend()
-    )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +6/-14
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12065 - (1/n)support context parallel with deepseekv3.2-DSA

- Link: https://github.com/sgl-project/sglang/pull/12065
- Status/date: merged / 2025-11-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `d368c7451a48`
- Diff scope read: GitHub Pull Request files API returned 17 files, +1247/-54, 1729 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "(1/n)support context parallel with deepseekv3.2-DSA"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "(1/n)support context parallel with deepseekv3.2-DSA"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +134/-32 (166 lines); hunks: -54,13 +54,23; -412,7 +422,9 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, __init__, forward, touching `handle_attention_nsa, __init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +134/-32 (166 lines); hunks: -54,13 +54,23; -412,7 +422,9 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -54,13 +54,23 @@
+from sglang.srt.layers.attention.nsa.utils import (
+    can_cp_split,
+    cp_all_gather_rerange_output,
+    cp_split_and_rebuild_data,
+    cp_split_and_rebuild_position,
+    enable_prefill_cp,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +134/-32
- Risk and verification: The diff ships test coverage in `test/srt/run_suite.py`, `test/srt/test_deepseek_v32_cp_single_node.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #12964 - [DeepseekV3.2] Deepseek fp8 support for MHA path

- Link: https://github.com/sgl-project/sglang/pull/12964
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `fa924410276d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +55/-9, 114 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepseekV3.2] Deepseek fp8 support for MHA path"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepseekV3.2] Deepseek fp8 support for MHA path"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +46/-8 (54 lines); hunks: -53,6 +53,7; -418,8 +419,6 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, forward_normal_prepare, _get_mla_kv_buffer, _get_mla_kv_buffer_from_fp8, touching `handle_attention_nsa, forward_normal_prepare, _get_mla_kv_buffer`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +46/-8 (54 lines); hunks: -53,6 +53,7; -418,8 +419,6 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, forward_normal_prepare, _get_mla_kv_buffer, _get_mla_kv_buffer_from_fp8
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -53,6 +53,7 @@
+from sglang.srt.layers.attention.nsa.dequant_k_cache import dequantize_k_cache_paged
@@ -418,8 +419,6 @@ def handle_attention_nsa(attn, forward_batch):
-    TODO: B200 (SM100) MHA path is temporarily disabled due to FA4 gpqa accuracy issues.
@@ -434,10 +433,17 @@ def handle_attention_nsa(attn, forward_batch):
-        # Check if kvcache dtype is bfloat16
-        kv_dtype_is_bf16 = forward_batch.token_to_kv_pool.dtype == torch.bfloat16
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +46/-8
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13459 - [Deepseek V3.2] Change indexer weights_proj to fp32

- Link: https://github.com/sgl-project/sglang/pull/13459
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `7291c72e575d`
- Diff scope read: GitHub Pull Request files API returned 3 files, +92/-124, 345 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Deepseek V3.2] Change indexer weights_proj to fp32"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Deepseek V3.2] Change indexer weights_proj to fp32"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +0/-71 (71 lines); hunks: -239,17 +239,6 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1226,9 +1215,6 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__, touching `add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +0/-71 (71 lines); hunks: -239,17 +239,6 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1226,9 +1215,6 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -239,17 +239,6 @@ def add_forward_absorb_core_attention_backend(backend_name):
-def is_nsa_indexer_wk_and_weights_proj_fused(config, quant_config):
-    """
-    NSA Indexer wk and weights_proj can be fused in FP4 model because they are both in BF16
-    """
-    return (
-        is_deepseek_nsa(config)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +0/-71
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13544 - [DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend

- Link: https://github.com/sgl-project/sglang/pull/13544
- Status/date: merged / 2025-11-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `5eed5fc0b091`
- Diff scope read: GitHub Pull Request files API returned 2 files, +74/-78, 342 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +5/-36 (41 lines); hunks: -417,43 +417,12 @@ def handle_attention_aiter(attn, forward_batch):; symbols: handle_attention_aiter, handle_attention_nsa, touching `handle_attention_aiter, handle_attention_nsa`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-36 (41 lines); hunks: -417,43 +417,12 @@ def handle_attention_aiter(attn, forward_batch):; symbols: handle_attention_aiter, handle_attention_nsa
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -417,43 +417,12 @@ def handle_attention_aiter(attn, forward_batch):
-    Select MHA or MLA based on sequence length for optimal performance.
-    - Decode: MLA (avoids per-token decompression)
-    - Prefill <= 2048: MHA (topk ineffective, MHA has lower FLOPs)
-    - Prefill > 2048: MLA (topk filtering reduces computation significantly)
+    Dispatch logic is centralized in NativeSparseAttnBackend.set_nsa_prefill_impl and executed
+    in init_forward_metadata. Read the decision from backend.use_mha.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-36
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13646 - [DeepSeekV3.2] Enable pure TP & Partial DP Attention

- Link: https://github.com/sgl-project/sglang/pull/13646
- Status/date: merged / 2025-11-30
- Trace source: `git log --name-only -- <model-files>` found it through `test/manual/nightly/test_deepseek_v32_perf.py`; associated commits `decb48965dd1`
- Diff scope read: GitHub Pull Request files API returned 7 files, +286/-24, 460 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeekV3.2] Enable pure TP & Partial DP Attention"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `test/manual/nightly/test_deepseek_v32_perf.py`, `test/nightly/test_deepseek_v32_perf.py`; technical summary: Covers "[DeepSeekV3.2] Enable pure TP & Partial DP Attention"; the main implementation surface is `test/manual/nightly/test_deepseek_v32_perf.py`, `test/nightly/test_deepseek_v32_perf.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/manual/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass, touching `setUpClass`; `test/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass, touching `setUpClass`.
- Code diff details:
  - `test/manual/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass
  - `test/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass
- Key code excerpts:

```diff
diff -- test/manual/nightly/test_deepseek_v32_perf.py
@@ -25,6 +25,9 @@ def setUpClass(cls):
+                    "--dp",
+                    "8",
+                    "--enable-dp-attention",
@@ -35,6 +38,9 @@ def setUpClass(cls):
+                    "--dp",
+                    "8",
diff -- test/nightly/test_deepseek_v32_perf.py
@@ -25,6 +25,9 @@ def setUpClass(cls):
+                    "--dp",
+                    "8",
+                    "--enable-dp-attention",
@@ -35,6 +38,9 @@ def setUpClass(cls):
+                    "--dp",
+                    "8",
```

- Reviewed files:
  - tests: `test/manual/nightly/test_deepseek_v32_perf.py` modified +25/-0; `test/nightly/test_deepseek_v32_perf.py` modified +25/-0
- Risk and verification: The diff ships test coverage in `test/manual/nightly/test_deepseek_v32_perf.py`, `test/nightly/test_deepseek_v32_nsabackend.py`, `test/nightly/test_deepseek_v32_perf.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14249 - feat: DeepSeek new v3.2 encoding

- Link: https://github.com/sgl-project/sglang/pull/14249
- Status/date: merged / 2025-12-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `7c38eca1e4a7`
- Diff scope read: GitHub Pull Request files API returned 6 files, +1153/-89, 1359 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: DeepSeek new v3.2 encoding"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "feat: DeepSeek new v3.2 encoding"; the main implementation surface is `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` added +451/-0 (451 lines); hunks: -0,0 +1,451; symbols: to_json, tools_from_openai_format, tool_calls_from_openai_format, tool_calls_to_openai_format, touching `to_json, tools_from_openai_format, tool_calls_from_openai_format`; `python/sglang/srt/function_call/deepseekv32_detector.py` added +321/-0 (321 lines); hunks: -0,0 +1,321; symbols: DeepSeekV32Detector, __init__, has_tool_call, _parse_parameters_from_xml, touching `DeepSeekV32Detector, __init__, has_tool_call`.
- Code diff details:
  - `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` added +451/-0 (451 lines); hunks: -0,0 +1,451; symbols: to_json, tools_from_openai_format, tool_calls_from_openai_format, tool_calls_to_openai_format
  - `python/sglang/srt/function_call/deepseekv32_detector.py` added +321/-0 (321 lines); hunks: -0,0 +1,321; symbols: DeepSeekV32Detector, __init__, has_tool_call, _parse_parameters_from_xml
- Key code excerpts:

```diff
diff -- python/sglang/srt/entrypoints/openai/encoding_dsv32.py
@@ -0,0 +1,451 @@
+# Adapted from https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/encoding/encoding_dsv32.py
+import copy
+import json
+import re
+from typing import Any, Dict, List, Optional, Tuple, Union
+TOOLS_SYSTEM_TEMPLATE = """## Tools
diff -- python/sglang/srt/function_call/deepseekv32_detector.py
@@ -0,0 +1,321 @@
+import json
+import logging
+import re
+from typing import List
+from sglang.srt.entrypoints.openai.protocol import Tool
+from sglang.srt.function_call.base_format_detector import BaseFormatDetector
```

- Reviewed files:
  - runtime: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` added +451/-0; `python/sglang/srt/function_call/deepseekv32_detector.py` added +321/-0
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`, `test/srt/openai_server/basic/test_serving_chat.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14573 - [Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode

- Link: https://github.com/sgl-project/sglang/pull/14573
- Status/date: merged / 2025-12-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `b7b7524e9560`
- Diff scope read: GitHub Pull Request files API returned 2 files, +144/-7, 165 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +2/-7 (9 lines); hunks: -241,13 +241,8 @@ def parse_streaming_increment(; symbols: parse_streaming_increment, touching `parse_streaming_increment`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +2/-7 (9 lines); hunks: -241,13 +241,8 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv32_detector.py
@@ -241,13 +241,8 @@ def parse_streaming_increment(
-                    # Check if invoke_content is empty or whitespace only
-                    # If so, skip this tool call entirely (it's likely incomplete or malformed)
-                    if not invoke_content.strip():
-                        # Remove the incomplete tool call from buffer
-                        self._buffer = current_text[invoke_match.end() :]
-                        current_text = self._buffer
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +2/-7
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14541 - [NPU]dsv3.2 cp for npu

- Link: https://github.com/sgl-project/sglang/pull/14541
- Status/date: merged / 2025-12-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; associated commits `388018a5bd41`
- Diff scope read: GitHub Pull Request files API returned 8 files, +281/-134, 587 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]dsv3.2 cp for npu"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU]dsv3.2 cp for npu"; the main implementation surface is `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +9/-0 (9 lines); hunks: -311,8 +311,17 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu, touching `forward_dsa_prepare_npu`.
- Code diff details:
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +9/-0 (9 lines); hunks: -311,8 +311,17 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu
- Key code excerpts:

```diff
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -311,8 +311,17 @@ def forward_dsa_prepare_npu(
+        if enable_prefill_cp(forward_batch, m.nsa_enable_prefill_cp):
+            positions = cp_split_and_rebuild_position(forward_batch, positions)
+        if enable_prefill_cp(forward_batch, m.nsa_enable_prefill_cp):
+            # support allgather+rerrange
+            k_nope, k_pe = m.rebuild_cp_kv_cache(
+                latent_cache, forward_batch, k_nope, k_pe
```

- Reviewed files:
  - runtime: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +9/-0
- Risk and verification: The diff ships test coverage in `test/srt/ascend/test_ascend_tp4_bf16.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14572 - [NPU] optimization for dsv3.2

- Link: https://github.com/sgl-project/sglang/pull/14572
- Status/date: merged / 2025-12-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `c05d3afb5d8b`
- Diff scope read: GitHub Pull Request files API returned 11 files, +141/-68, 393 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU] optimization for dsv3.2"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU] optimization for dsv3.2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +25/-4 (29 lines); hunks: -700,6 +700,7 @@ def __init__(; -738,7 +739,11 @@ def __init__(; symbols: __init__, forward_deepep, _post_combine_hook, touching `__init__, forward_deepep, _post_combine_hook`; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +34/-18 (52 lines); hunks: -273,39 +273,51 @@ def forward_dsa_prepare_npu(; -367,7 +379,11 @@ def forward_dsa_core_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu, touching `forward_dsa_prepare_npu, forward_dsa_core_npu`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +25/-4 (29 lines); hunks: -700,6 +700,7 @@ def __init__(; -738,7 +739,11 @@ def __init__(; symbols: __init__, forward_deepep, _post_combine_hook
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +34/-18 (52 lines); hunks: -273,39 +273,51 @@ def forward_dsa_prepare_npu(; -367,7 +379,11 @@ def forward_dsa_core_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -700,6 +700,7 @@ def __init__(
+                    or get_moe_a2a_backend().is_ascend_fuseep()
@@ -738,7 +739,11 @@ def __init__(
-        if get_moe_a2a_backend().is_deepep() or get_moe_a2a_backend().is_mooncake():
+        if (
+            get_moe_a2a_backend().is_deepep()
+            or get_moe_a2a_backend().is_mooncake()
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -273,39 +273,51 @@ def forward_dsa_prepare_npu(
-        (
-            q_pe,
-            k_pe,
-            q_nope_out,
-            k_nope,
-            forward_batch,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +25/-4; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +34/-18
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/hardware_backend/npu/moe/topk.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15278 - feat: DeepSeek-V3.2 Streaming tool call output

- Link: https://github.com/sgl-project/sglang/pull/15278
- Status/date: merged / 2025-12-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `41683536d394`
- Diff scope read: GitHub Pull Request files API returned 2 files, +111/-69, 328 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: DeepSeek-V3.2 Streaming tool call output"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "feat: DeepSeek-V3.2 Streaming tool call output"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +95/-65 (160 lines); hunks: -1,7 +1,6; -11,6 +10,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml, touching `__init__, has_tool_call, _parse_parameters_from_xml`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +95/-65 (160 lines); hunks: -1,7 +1,6; -11,6 +10,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv32_detector.py
@@ -1,7 +1,6 @@
-from typing import List
@@ -11,6 +10,7 @@
+from sglang.srt.function_call.utils import _find_common_prefix
@@ -71,17 +71,26 @@ def __init__(self):
-        self.invoke_begin_regex = r'<｜DSML｜invoke\s+name="([^"]+)"\s*>'
-        self._last_arguments = ""
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +95/-65
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14353 - feat(dsv32): better error handling for DeepSeek-v3.2 encoder

- Link: https://github.com/sgl-project/sglang/pull/14353
- Status/date: merged / 2025-12-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`; associated commits `216067c0cba2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +53/-32, 197 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat(dsv32): better error handling for DeepSeek-v3.2 encoder"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`; technical summary: Covers "feat(dsv32): better error handling for DeepSeek-v3.2 encoder"; the main implementation surface is `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` modified +45/-32 (77 lines); hunks: -4,6 +4,11; -148,11 +153,12 @@ def find_last_user_index(messages: List[Dict[str, Any]]) -...; symbols: DS32EncodingError, find_last_user_index, render_message, touching `DS32EncodingError, find_last_user_index, render_message`.
- Code diff details:
  - `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` modified +45/-32 (77 lines); hunks: -4,6 +4,11; -148,11 +153,12 @@ def find_last_user_index(messages: List[Dict[str, Any]]) -...; symbols: DS32EncodingError, find_last_user_index, render_message
- Key code excerpts:

```diff
diff -- python/sglang/srt/entrypoints/openai/encoding_dsv32.py
@@ -4,6 +4,11 @@
+class DS32EncodingError(Exception):
+    pass
@@ -148,11 +153,12 @@ def find_last_user_index(messages: List[Dict[str, Any]]) -> int:
-    assert 0 <= index < len(messages)
-    assert thinking_mode in [
-        "chat",
```

- Reviewed files:
  - runtime: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` modified +45/-32
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/entrypoints/openai/serving_base.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14901 - fix ds3.2 nsa backend prefill TBO

- Link: https://github.com/sgl-project/sglang/pull/14901
- Status/date: merged / 2025-12-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `350fbbf4dc1e`
- Diff scope read: GitHub Pull Request files API returned 5 files, +76/-2, 148 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix ds3.2 nsa backend prefill TBO"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "fix ds3.2 nsa backend prefill TBO"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -66,6 +66,7; -421,7 +422,10 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, _get_mla_kv_buffer_from_fp8, touching `handle_attention_nsa, _get_mla_kv_buffer_from_fp8`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -66,6 +66,7; -421,7 +422,10 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, _get_mla_kv_buffer_from_fp8
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -66,6 +66,7 @@
+from sglang.srt.layers.attention.tbo_backend import TboAttnBackend
@@ -421,7 +422,10 @@ def handle_attention_nsa(attn, forward_batch):
+    if isinstance(backend, TboAttnBackend):  # if enable tbo, get primary backend
+        backend = backend.primary
@@ -2665,7 +2669,10 @@ def _get_mla_kv_buffer_from_fp8(
-        kv_indices = forward_batch.attn_backend.forward_metadata.page_table_1_flattened
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1
- Risk and verification: The diff ships test coverage in `test/srt/ep/test_deepep_large.py`, `test/srt/run_suite.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14750 - [Tool Call][DSV32] Streamline function call parameters

- Link: https://github.com/sgl-project/sglang/pull/14750
- Status/date: merged / 2025-12-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `01bd0d3e8b8c`
- Diff scope read: GitHub Pull Request files API returned 2 files, +60/-29, 200 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tool Call][DSV32] Streamline function call parameters"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Tool Call][DSV32] Streamline function call parameters"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +23/-15 (38 lines); hunks: -2,6 +2,8; -10,7 +12,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml, parse_streaming_increment, touching `__init__, has_tool_call, _parse_parameters_from_xml`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +23/-15 (38 lines); hunks: -2,6 +2,8; -10,7 +12,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml, parse_streaming_increment
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv32_detector.py
@@ -2,6 +2,8 @@
+from partial_json_parser.core.options import Allow
@@ -10,7 +12,7 @@
-from sglang.srt.function_call.utils import _find_common_prefix
+from sglang.srt.function_call.utils import _find_common_prefix, _partial_json_loads
@@ -82,11 +84,12 @@ def __init__(self):
+        self.prefix_parameter_end_call = ["</", "｜DSML｜", "parameter"]
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +23/-15
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #13959 - [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache

- Link: https://github.com/sgl-project/sglang/pull/13959
- Status/date: merged / 2026-01-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `0d244116d28a`
- Diff scope read: GitHub Pull Request files API returned 14 files, +603/-264, 1414 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +10/-16 (26 lines); hunks: -64,8 +64,8; -578,9 +578,7 @@ def forward(; symbols: forward, forward_absorb_prepare, touching `forward, forward_absorb_prepare`; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +5/-5 (10 lines); hunks: -10,7 +10,7; -192,12 +192,12 @@ def forward_mla_prepare_npu(; symbols: forward_mla_prepare_npu, forward_dsa_prepare_npu, touching `forward_mla_prepare_npu, forward_dsa_prepare_npu`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +10/-16 (26 lines); hunks: -64,8 +64,8; -578,9 +578,7 @@ def forward(; symbols: forward, forward_absorb_prepare
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +5/-5 (10 lines); hunks: -10,7 +10,7; -192,12 +192,12 @@ def forward_mla_prepare_npu(; symbols: forward_mla_prepare_npu, forward_dsa_prepare_npu
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -64,8 +64,8 @@
-    enable_prefill_cp,
+    nsa_use_prefill_cp,
@@ -578,9 +578,7 @@ def forward(
-        if forward_batch is not None and enable_prefill_cp(
-            forward_batch, self.nsa_enable_prefill_cp
-        ):
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -10,7 +10,7 @@
-    enable_prefill_cp,
+    nsa_use_prefill_cp,
@@ -192,12 +192,12 @@ def forward_mla_prepare_npu(
-        if enable_prefill_cp(forward_batch, m.nsa_enable_prefill_cp):
+        if nsa_use_prefill_cp(forward_batch, m.nsa_enable_prefill_cp):
-        if enable_prefill_cp(forward_batch, m.nsa_enable_prefill_cp):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +10/-16; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +5/-5
- Risk and verification: The diff ships test coverage in `test/manual/test_deepseek_v32_cp_single_node.py`, `test/srt/test_prefill_adder.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #16637 - [DSv32] Overlap indexer weights_proj during dual_stream decode

- Link: https://github.com/sgl-project/sglang/pull/16637
- Status/date: merged / 2026-01-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `20abaee26cd8`
- Diff scope read: GitHub Pull Request files API returned 2 files, +64/-22, 134 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSv32] Overlap indexer weights_proj during dual_stream decode"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DSv32] Overlap indexer weights_proj during dual_stream decode"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +34/-11 (45 lines); hunks: -1666,6 +1666,7 @@ def forward_absorb_prepare(; -1722,8 +1723,39 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, touching `forward_absorb_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +34/-11 (45 lines); hunks: -1666,6 +1666,7 @@ def forward_absorb_prepare(; -1722,8 +1723,39 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1666,6 +1666,7 @@ def forward_absorb_prepare(
+        topk_indices = None
@@ -1722,8 +1723,39 @@ def forward_absorb_prepare(
-            k_nope = k_nope.unsqueeze(1)
-            q = self.q_b_proj(q)[0].view(-1, self.num_local_heads, self.qk_head_dim)
+            # overlap q_b_proj and indexer during decode
+            if (
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +34/-11
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16841 - [AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant

- Link: https://github.com/sgl-project/sglang/pull/16841
- Status/date: merged / 2026-01-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `afe285f7bd9a`
- Diff scope read: GitHub Pull Request files API returned 7 files, +260/-81, 587 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +58/-18 (76 lines); hunks: -1523,10 +1523,34 @@ def forward_normal_prepare(; -1703,31 +1727,47 @@ def forward_absorb_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare, touching `forward_normal_prepare, forward_absorb_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +58/-18 (76 lines); hunks: -1523,10 +1523,34 @@ def forward_normal_prepare(; -1703,31 +1727,47 @@ def forward_absorb_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1523,10 +1523,34 @@ def forward_normal_prepare(
-                q_lora = self.q_a_layernorm(q)
-                q = self.q_b_proj(q_lora)[0].view(
-                    -1, self.num_local_heads, self.qk_head_dim
-                )
+                # NSA requires unquantized q_lora for the indexer. When q_b_proj is FP8
+                # on gfx95, we can still use fused RMSNorm+FP8 quant, but MUST request
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +58/-18
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16934 - [AMD] Enable DeepseekV3.2 test for AMD CI

- Link: https://github.com/sgl-project/sglang/pull/16934
- Status/date: merged / 2026-01-16
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; associated commits `968c4f55b194`
- Diff scope read: GitHub Pull Request files API returned 4 files, +379/-1, 403 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Enable DeepseekV3.2 test for AMD CI"; model line: DeepSeek V3.2; category: docs/tests/CI; main diff: `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_deepseek_v32_basic.py`; technical summary: Covers "[AMD] Enable DeepseekV3.2 test for AMD CI"; the main implementation surface is `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_deepseek_v32_basic.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/test_deepseek_v32_mtp.py` added +213/-0 (213 lines); hunks: -0,0 +1,213; symbols: TestDeepseekV32DPMTP, setUpClass, tearDownClass, test_a_gsm8k, touching `TestDeepseekV32DPMTP, setUpClass, tearDownClass`; `test/registered/amd/test_deepseek_v32_basic.py` added +163/-0 (163 lines); hunks: -0,0 +1,163; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k, touching `TestDeepseekV32DP, setUpClass, tearDownClass`.
- Code diff details:
  - `test/registered/amd/test_deepseek_v32_mtp.py` added +213/-0 (213 lines); hunks: -0,0 +1,213; symbols: TestDeepseekV32DPMTP, setUpClass, tearDownClass, test_a_gsm8k
  - `test/registered/amd/test_deepseek_v32_basic.py` added +163/-0 (163 lines); hunks: -0,0 +1,163; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k
- Key code excerpts:

```diff
diff -- test/registered/amd/test_deepseek_v32_mtp.py
@@ -0,0 +1,213 @@
+import unittest
+from types import SimpleNamespace
+import requests
+from sglang.srt.utils import kill_process_tree
+from sglang.test.ci.ci_register import register_amd_ci
+from sglang.test.few_shot_gsm8k import run_eval as run_eval_few_shot_gsm8k
diff -- test/registered/amd/test_deepseek_v32_basic.py
@@ -0,0 +1,163 @@
+import unittest
+from types import SimpleNamespace
+from sglang.srt.utils import kill_process_tree
+from sglang.test.ci.ci_register import register_amd_ci
+from sglang.test.few_shot_gsm8k import run_eval as run_eval_few_shot_gsm8k
+from sglang.test.send_one import BenchArgs, send_one_prompt
```

- Reviewed files:
  - tests: `test/registered/amd/test_deepseek_v32_mtp.py` added +213/-0; `test/registered/amd/test_deepseek_v32_basic.py` added +163/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #17179 - [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests

- Link: https://github.com/sgl-project/sglang/pull/17179
- Status/date: merged / 2026-01-20
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`, `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; associated commits `a3addd6203ca`
- Diff scope read: GitHub Pull Request files API returned 18 files, +1140/-99, 1539 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`; technical summary: Covers "[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_display_name, get_one_example, touching `ModelConfig, __post_init__, get_display_name`; `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32MTPPerformance, setUpClass, test_bench_one_batch, touching `generate_simple_markdown_report, TestNightlyDeepseekV32MTPPerformance, setUpClass`; `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` added +134/-0 (134 lines); hunks: -0,0 +1,134; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32BasicPerformance, setUpClass, test_bench_one_batch, touching `generate_simple_markdown_report, TestNightlyDeepseekV32BasicPerformance, setUpClass`; `test/registered/amd/test_deepseek_v32_basic.py` modified +1/-1 (2 lines); hunks: -16,7 +16,7; symbols: TestDeepseekV32DP, touching `TestDeepseekV32DP`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_display_name, get_one_example
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32MTPPerformance, setUpClass, test_bench_one_batch
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` added +134/-0 (134 lines); hunks: -0,0 +1,134; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32BasicPerformance, setUpClass, test_bench_one_batch
  - `test/registered/amd/test_deepseek_v32_basic.py` modified +1/-1 (2 lines); hunks: -16,7 +16,7; symbols: TestDeepseekV32DP
  - `test/registered/amd/test_deepseek_v32_mtp.py` modified +1/-1 (2 lines); hunks: -18,7 +18,7; symbols: TestDeepseekV32DPMTP
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py
@@ -0,0 +1,251 @@
+"""MI35x DeepSeek-V3.2 GSM8K Completion Evaluation Test (8-GPU)
+Tests DeepSeek-V3.2 with basic configuration using few-shot completion
+benchmark on MI35x.
+Registry: nightly-amd-accuracy-8-gpu-mi35x-deepseek-v32 suite
+"""
+import ast
diff -- test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py
@@ -0,0 +1,146 @@
+"""MI35x Nightly performance benchmark for DeepSeek-V3.2 model (MTP variant).
+This test benchmarks the DeepSeek-V3.2 model with MTP (EAGLE speculative decoding)
+configuration on 8 GPUs.
+The model path can be configured via DEEPSEEK_V32_MODEL_PATH environment variable.
+Registry: nightly-perf-8-gpu-mi35x-deepseek-v32-mtp suite
+Example usage:
diff -- test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py
@@ -0,0 +1,134 @@
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` added +251/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` added +146/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` added +134/-0; `test/registered/amd/test_deepseek_v32_basic.py` modified +1/-1; `test/registered/amd/test_deepseek_v32_mtp.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/test_vlms_mmmu_eval_amd.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #17432 - [AMD] fix amd ci dpskv32

- Link: https://github.com/sgl-project/sglang/pull/17432
- Status/date: merged / 2026-01-22
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; associated commits `17807caf82c8`
- Diff scope read: GitHub Pull Request files API returned 5 files, +16/-7, 96 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] fix amd ci dpskv32"; model line: DeepSeek V3.2; category: bug fix; main diff: `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; technical summary: Covers "[AMD] fix amd ci dpskv32"; the main implementation surface is `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/test_deepseek_v32_basic.py` modified +7/-2 (9 lines); hunks: -15,10 +15,16; -90,7 +96,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DP, setUpClass, test_bs_1_speed, TestDeepseekV32TP, touching `TestDeepseekV32DP, setUpClass, test_bs_1_speed`; `test/registered/amd/test_deepseek_v32_mtp.py` modified +2/-2 (4 lines); hunks: -21,6 +21,7; -116,7 +117,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DPMTP, setUpClass, test_bs_1_speed, TestDeepseekV32TPMTP, touching `TestDeepseekV32DPMTP, setUpClass, test_bs_1_speed`.
- Code diff details:
  - `test/registered/amd/test_deepseek_v32_basic.py` modified +7/-2 (9 lines); hunks: -15,10 +15,16; -90,7 +96,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DP, setUpClass, test_bs_1_speed, TestDeepseekV32TP
  - `test/registered/amd/test_deepseek_v32_mtp.py` modified +2/-2 (4 lines); hunks: -21,6 +21,7; -116,7 +117,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DPMTP, setUpClass, test_bs_1_speed, TestDeepseekV32TPMTP
- Key code excerpts:

```diff
diff -- test/registered/amd/test_deepseek_v32_basic.py
@@ -15,10 +15,16 @@
-register_amd_ci(est_time=3600, suite="stage-c-test-large-8-gpu-amd-mi35x")
+register_amd_ci(
+    est_time=3600,
+    suite="stage-c-test-large-8-gpu-amd-mi35x",
+    disabled="move to nightly for saving time",
+)
diff -- test/registered/amd/test_deepseek_v32_mtp.py
@@ -21,6 +21,7 @@
+@unittest.skipIf(is_in_amd_ci(), "Skip DP test for AMD CI, run TP only.")
@@ -116,7 +117,6 @@ def test_bs_1_speed(self):
-@unittest.skipIf(is_in_amd_ci(), "To reduce the CI execution time for AMD.")
@@ -204,7 +204,7 @@ def test_bs_1_speed(self):
-                self.assertGreater(speed, 60)
+                self.assertGreater(speed, 55)
```

- Reviewed files:
  - tests: `test/registered/amd/test_deepseek_v32_basic.py` modified +7/-2; `test/registered/amd/test_deepseek_v32_mtp.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `python/sglang/test/test_utils.py`, `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #17007 - [NPU]bugfix: fix for dsv3.2 and dsvl2

- Link: https://github.com/sgl-project/sglang/pull/17007
- Status/date: merged / 2026-01-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `c0b5a180febe`
- Diff scope read: GitHub Pull Request files API returned 5 files, +129/-46, 224 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]bugfix: fix for dsv3.2 and dsvl2"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU]bugfix: fix for dsv3.2 and dsvl2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1220,6 +1220,7 @@ def __init__(; symbols: __init__, touching `__init__`; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +80/-46 (126 lines); hunks: -64,36 +64,44 @@ def forward_mha_prepare_npu(; -288,10 +296,30 @@ def forward_dsa_prepare_npu(; symbols: forward_mha_prepare_npu, forward_dsa_prepare_npu, touching `forward_mha_prepare_npu, forward_dsa_prepare_npu`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1220,6 +1220,7 @@ def __init__(; symbols: __init__
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +80/-46 (126 lines); hunks: -64,36 +64,44 @@ def forward_mha_prepare_npu(; -288,10 +296,30 @@ def forward_dsa_prepare_npu(; symbols: forward_mha_prepare_npu, forward_dsa_prepare_npu
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1220,6 +1220,7 @@ def __init__(
+        self.use_deepseek_yarn_rope = rope_scaling is not None
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -64,36 +64,44 @@ def forward_mha_prepare_npu(
-    B, S = q.shape[0], 1
-    cos, sin = m.rotary_emb.get_cos_sin_cache(
-        positions, hidden_states.dtype, offsets=None
-    )
-    q_pe = torch_npu.npu_interleave_rope(
-        q_pe.reshape(B, -1, S, m.qk_rope_head_dim),
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +80/-46
- Risk and verification: The diff ships test coverage in `test/registered/ascend/llm_models/test_ascend_deepseek_v3_2_exp_w8a8.py`, `test/registered/ascend/vlm_models/test_ascend_deepseek_vl2.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #15381 - [NPU]DeepSeek-V3.2 support npu mlaprolog

- Link: https://github.com/sgl-project/sglang/pull/15381
- Status/date: merged / 2026-01-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; associated commits `b56366f8275a`
- Diff scope read: GitHub Pull Request files API returned 5 files, +195/-61, 364 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]DeepSeek-V3.2 support npu mlaprolog"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU]DeepSeek-V3.2 support npu mlaprolog"; the main implementation surface is `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +116/-55 (171 lines); hunks: -1,3 +1,4; -281,61 +282,25 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu, npu_mla_preprocess, touching `forward_dsa_prepare_npu, forward_dsa_core_npu, npu_mla_preprocess`.
- Code diff details:
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +116/-55 (171 lines); hunks: -1,3 +1,4; -281,61 +282,25 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu, npu_mla_preprocess
- Key code excerpts:

```diff
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -1,3 +1,4 @@
+import re
@@ -281,61 +282,25 @@ def forward_dsa_prepare_npu(
+    dynamic_scale = None
-        if not hasattr(m, "mla_preprocess"):
-            m.mla_preprocess = NPUFusedMLAPreprocess(
-                m.fused_qkv_a_proj_with_mqa,
```

- Reviewed files:
  - runtime: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +116/-55
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17633 - [AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites

- Link: https://github.com/sgl-project/sglang/pull/17633
- Status/date: merged / 2026-01-28
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; associated commits `52bca4287033`
- Diff scope read: GitHub Pull Request files API returned 9 files, +88/-230, 490 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`; technical summary: Covers "[AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites"; the main implementation surface is `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/test_deepseek_v32_basic.py` modified +2/-6 (8 lines); hunks: -15,11 +15,7; -159,7 +155,7 @@ def test_bs_1_speed(self):; symbols: test_bs_1_speed, touching `test_bs_1_speed`; `test/registered/amd/test_deepseek_v32_mtp.py` modified +6/-1 (7 lines); hunks: -17,7 +17,12.
- Code diff details:
  - `test/registered/amd/test_deepseek_v32_basic.py` modified +2/-6 (8 lines); hunks: -15,11 +15,7; -159,7 +155,7 @@ def test_bs_1_speed(self):; symbols: test_bs_1_speed
  - `test/registered/amd/test_deepseek_v32_mtp.py` modified +6/-1 (7 lines); hunks: -17,7 +17,12
- Key code excerpts:

```diff
diff -- test/registered/amd/test_deepseek_v32_basic.py
@@ -15,11 +15,7 @@
-register_amd_ci(
-    est_time=3600,
-    suite="stage-c-test-large-8-gpu-amd-mi35x",
-    disabled="move to nightly for saving time",
-)
+register_amd_ci(est_time=1800, suite="stage-c-test-large-8-gpu-amd")
diff -- test/registered/amd/test_deepseek_v32_mtp.py
@@ -17,7 +17,12 @@
-register_amd_ci(est_time=3600, suite="stage-c-test-large-8-gpu-amd-mi35x")
+register_amd_ci(
+    est_time=3600,
+    suite="stage-c-test-large-8-gpu-amd-mi35x",
+    disabled="move to nightly for saving time",
+)
```

- Reviewed files:
  - tests: `test/registered/amd/test_deepseek_v32_basic.py` modified +2/-6; `test/registered/amd/test_deepseek_v32_mtp.py` modified +6/-1
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_kimi_k2_instruct.py`, `test/registered/attention/test_triton_sliding_window.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #17523 - [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI

- Link: https://github.com/sgl-project/sglang/pull/17523
- Status/date: merged / 2026-01-28
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`; associated commits `f8636fbb253a`
- Diff scope read: GitHub Pull Request files API returned 27 files, +1540/-43, 1823 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`; technical summary: Covers "[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: TestDeepseekV32TPMTP, setUpClass, tearDownClass, test_a_gsm8k, touching `TestDeepseekV32TPMTP, setUpClass, tearDownClass`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` added +119/-0 (119 lines); hunks: -0,0 +1,119; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k, touching `TestDeepseekV32DP, setUpClass, tearDownClass`; `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` modified +59/-3 (62 lines); hunks: -13,12 +13,17; -57,11 +62,58 @@ def generate_simple_markdown_report(results: List[BenchmarkR...; symbols: generate_simple_markdown_report, _run_benchmark_with_timeout, TestNightlyDeepseekV32MTPPerformance, setUpClass, touching `generate_simple_markdown_report, _run_benchmark_with_timeout, TestNightlyDeepseekV32MTPPerformance`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -215,6 +215,9 @@ def test_deepseek_v32_accuracy(self):; symbols: test_deepseek_v32_accuracy, touching `test_deepseek_v32_accuracy`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: TestDeepseekV32TPMTP, setUpClass, tearDownClass, test_a_gsm8k
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` added +119/-0 (119 lines); hunks: -0,0 +1,119; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` modified +59/-3 (62 lines); hunks: -13,12 +13,17; -57,11 +62,58 @@ def generate_simple_markdown_report(results: List[BenchmarkR...; symbols: generate_simple_markdown_report, _run_benchmark_with_timeout, TestNightlyDeepseekV32MTPPerformance, setUpClass
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -215,6 +215,9 @@ def test_deepseek_v32_accuracy(self):; symbols: test_deepseek_v32_accuracy
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` modified +2/-0 (2 lines); hunks: -93,6 +93,8 @@ def setUpClass(cls):; symbols: setUpClass
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py
@@ -0,0 +1,142 @@
+"""MI35x DeepSeek-V3.2 TP+MTP GSM8K Accuracy Evaluation Test (8-GPU)
+Tests DeepSeek-V3.2 with TP=8 + MTP (EAGLE speculative decoding) using few-shot
+completion benchmark on MI35x.
+Registry: nightly-amd-accuracy-8-gpu-mi35x-deepseek-v32-mtp suite
+"""
+import os
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py
@@ -0,0 +1,119 @@
+"""MI35x DeepSeek-V3.2 DP GSM8K Accuracy Evaluation Test (8-GPU)
+Tests DeepSeek-V3.2 with DP=8 + TP=8 + dp-attention using few-shot
+completion benchmark on MI35x.
+Registry: nightly-amd-accuracy-8-gpu-mi35x-deepseek-v32-dp suite
+"""
+import os
diff -- test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py
@@ -13,12 +13,17 @@
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` added +142/-0; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` added +119/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` modified +59/-3; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` modified +3/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` modified +2/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #18297 - Deepseekv32 compatibility with transformers v5

- Link: https://github.com/sgl-project/sglang/pull/18297
- Status/date: merged / 2026-02-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `e8a2c133807c`
- Diff scope read: GitHub Pull Request files API returned 5 files, +33/-19, 131 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Deepseekv32 compatibility with transformers v5"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Deepseekv32 compatibility with transformers v5"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -1150,6 +1150,7 @@ def __init__(; -1162,6 +1163,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -1150,6 +1150,7 @@ def __init__(; -1162,6 +1163,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1150,6 +1150,7 @@ def __init__(
+            is_neox_style = not getattr(config, "indexer_rope_interleave", False)
@@ -1162,6 +1163,7 @@ def __init__(
+                is_neox_style=is_neox_style,
@@ -1191,13 +1193,14 @@ def __init__(
+            is_neox_style = not getattr(config, "rope_interleave", True)
-                is_neox_style=False,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16907 - Fix model loading for DeepSeek-V3.2-AWQ

- Link: https://github.com/sgl-project/sglang/pull/16907
- Status/date: merged / 2026-02-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `190fa8246fbc`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-4, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix model loading for DeepSeek-V3.2-AWQ"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix model loading for DeepSeek-V3.2-AWQ"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +8/-4 (12 lines); hunks: -245,10 +245,14 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +8/-4 (12 lines); hunks: -245,10 +245,14 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -245,10 +245,14 @@ def __init__(
-        if not hasattr(self.gate_up_proj, "weight"):
-            self.gate_up_proj.weight = getattr(self.gate_up_proj, "weight_packed")
-        if not hasattr(self.down_proj, "weight"):
-            self.down_proj.weight = getattr(self.down_proj, "weight_packed")
+        if not hasattr(self.gate_up_proj, "weight") and hasattr(
+            self.gate_up_proj, "weight_packed"
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +8/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18389 - Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4

- Link: https://github.com/sgl-project/sglang/pull/18389
- Status/date: merged / 2026-02-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `0ffd0a3995e5`
- Diff scope read: GitHub Pull Request files API returned 10 files, +352/-183, 914 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -1488,6 +1488,12 @@ def _fuse_rope_for_trtllm_mla(self, forward_batch: Forwar...; symbols: _fuse_rope_for_trtllm_mla, touching `_fuse_rope_for_trtllm_mla`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -1488,6 +1488,12 @@ def _fuse_rope_for_trtllm_mla(self, forward_batch: Forwar...; symbols: _fuse_rope_for_trtllm_mla
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1488,6 +1488,12 @@ def _fuse_rope_for_trtllm_mla(self, forward_batch: ForwardBatch) -> bool:
+        if self.current_attention_backend == "nsa":
+            return (
+                get_global_server_args().nsa_decode_backend == "trtllm"
+                or get_global_server_args().nsa_prefill_backend == "trtllm"
+            ) and forward_batch.attn_backend.kv_cache_dtype == torch.float8_e4m3fn
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0
- Risk and verification: The diff ships test coverage in `test/registered/hicache/test_nsa_pool_host_unit.py`, `test/registered/kernels/test_nsa_indexer.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #18931 - Fix NSA FP8 KV cache path for both-trtllm MHA one-shot

- Link: https://github.com/sgl-project/sglang/pull/18931
- Status/date: merged / 2026-02-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`; associated commits `f23a23cc05fc`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-1, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix NSA FP8 KV cache path for both-trtllm MHA one-shot"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`; technical summary: Covers "Fix NSA FP8 KV cache path for both-trtllm MHA one-shot"; the main implementation surface is `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +8/-1 (9 lines); hunks: -215,7 +215,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare, touching `forward_normal_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +8/-1 (9 lines); hunks: -215,7 +215,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py
@@ -215,7 +215,14 @@ def forward_normal_prepare(
-            if self.use_nsa and self.kv_cache_dtype == "fp8_e4m3":
+            if (
+                self.use_nsa
+                and self.kv_cache_dtype == "fp8_e4m3"
+                and (
+                    not get_global_server_args().nsa_decode_backend == "trtllm"
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +8/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #19428 - [Feature] add feature mla_ag_after_qlora for dsv3.2

- Link: https://github.com/sgl-project/sglang/pull/19428
- Status/date: merged / 2026-03-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `b3718982a1b4`
- Diff scope read: GitHub Pull Request files API returned 5 files, +101/-9, 316 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] add feature mla_ag_after_qlora for dsv3.2"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[Feature] add feature mla_ag_after_qlora for dsv3.2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +26/-3 (29 lines); hunks: -1301,13 +1301,15 @@ def forward(; -1318,6 +1320,7 @@ def forward_prepare(; symbols: forward, forward_prepare, __init__, touching `forward, forward_prepare, __init__`; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +35/-3 (38 lines); hunks: -4,21 +4,24; -28,6 +31,7 @@ def forward_mha_prepare_npu(; symbols: forward_mha_prepare_npu, forward_mla_prepare_npu, forward_dsa_prepare_npu, touching `forward_mha_prepare_npu, forward_mla_prepare_npu, forward_dsa_prepare_npu`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +26/-3 (29 lines); hunks: -1301,13 +1301,15 @@ def forward(; -1318,6 +1320,7 @@ def forward_prepare(; symbols: forward, forward_prepare, __init__
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +35/-3 (38 lines); hunks: -4,21 +4,24; -28,6 +31,7 @@ def forward_mha_prepare_npu(; symbols: forward_mha_prepare_npu, forward_mla_prepare_npu, forward_dsa_prepare_npu
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1301,13 +1301,15 @@ def forward(
+        layer_scatter_modes: LayerScatterModes = None,
+            layer_scatter_modes=layer_scatter_modes,
@@ -1318,6 +1320,7 @@ def forward_prepare(
+        layer_scatter_modes: LayerScatterModes = None,
@@ -1370,15 +1373,30 @@ def forward_prepare(
-                self, positions, hidden_states, forward_batch, zero_allocator
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -4,21 +4,24 @@
+from sglang.srt.environ import envs
+from sglang.srt.layers.attention.nsa.nsa_indexer import scattered_to_tp_attn_full
-from sglang.srt.layers.communicator import get_attn_tp_context
+from sglang.srt.layers.communicator import ScatterMode, get_attn_tp_context
+_use_ag_after_qlora = envs.SGLANG_USE_AG_AFTER_QLORA.get()
@@ -28,6 +31,7 @@ def forward_mha_prepare_npu(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +26/-3; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +35/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18174 - [Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON

- Link: https://github.com/sgl-project/sglang/pull/18174
- Status/date: merged / 2026-03-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `6af0448cc9bf`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-3, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +6/-3 (9 lines); hunks: -158,9 +158,12 @@ def _parse_parameters_from_xml(; symbols: _parse_parameters_from_xml, touching `_parse_parameters_from_xml`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +6/-3 (9 lines); hunks: -158,9 +158,12 @@ def _parse_parameters_from_xml(; symbols: _parse_parameters_from_xml
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv32_detector.py
@@ -158,9 +158,12 @@ def _parse_parameters_from_xml(
-                    parameters[param_name] = _partial_json_loads(
-                        param_value, Allow.ALL
-                    )[0]
+                    try:
+                        parameters[param_name] = _partial_json_loads(
+                            param_value, Allow.ALL
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +6/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv32_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16091 - [Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format.

- Link: https://github.com/sgl-project/sglang/pull/16091
- Status/date: merged / 2026-03-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `666caaf9ce76`
- Diff scope read: GitHub Pull Request files API returned 2 files, +31/-22, 151 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format."; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format."; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +17/-21 (38 lines); hunks: -85,6 +85,7 @@ def __init__(self):; -93,27 +94,24 @@ def has_tool_call(self, text: str) -> bool:; symbols: __init__, has_tool_call, _parse_parameters_from_xml, touching `__init__, has_tool_call, _parse_parameters_from_xml`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +17/-21 (38 lines); hunks: -85,6 +85,7 @@ def __init__(self):; -93,27 +94,24 @@ def has_tool_call(self, text: str) -> bool:; symbols: __init__, has_tool_call, _parse_parameters_from_xml
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv32_detector.py
@@ -85,6 +85,7 @@ def __init__(self):
+        self.prefix_invoke_end_call = ["</", "｜DSML｜", "inv", "oke"]
@@ -93,27 +94,24 @@ def has_tool_call(self, text: str) -> bool:
-    ) -> dict:
+    ) -> str:
-        Parse parameters from either XML-like format or JSON format to dict.
+        Parse parameters from either XML-like format or JSON format to str.
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +17/-21
- Risk and verification: The diff ships test coverage in `test/registered/function_call/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #21192 - Fix CP in-seq-split method for DeepSeek V32 and update related tests

- Link: https://github.com/sgl-project/sglang/pull/21192
- Status/date: merged / 2026-03-23
- Trace source: `git log --name-only -- <model-files>` found it through `test/manual/nightly/test_deepseek_v32_perf.py`; associated commits `ed316a26efa4`
- Diff scope read: GitHub Pull Request files API returned 7 files, +162/-97, 296 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix CP in-seq-split method for DeepSeek V32 and update related tests"; model line: DeepSeek V3.2; category: bug fix; main diff: `test/manual/nightly/test_deepseek_v32_perf.py`; technical summary: Covers "Fix CP in-seq-split method for DeepSeek V32 and update related tests"; the main implementation surface is `test/manual/nightly/test_deepseek_v32_perf.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/manual/nightly/test_deepseek_v32_perf.py` modified +1/-1 (2 lines); hunks: -3,7 +3,7.
- Code diff details:
  - `test/manual/nightly/test_deepseek_v32_perf.py` modified +1/-1 (2 lines); hunks: -3,7 +3,7
- Key code excerpts:

```diff
diff -- test/manual/nightly/test_deepseek_v32_perf.py
@@ -3,7 +3,7 @@
-DEEPSEEK_V32_MODEL_PATH = "deepseek-ai/DeepSeek-V3.2-Exp"
+DEEPSEEK_V32_MODEL_PATH = "deepseek-ai/DeepSeek-V3.2"
```

- Reviewed files:
  - tests: `test/manual/nightly/test_deepseek_v32_perf.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #21511 - [AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend

- Link: https://github.com/sgl-project/sglang/pull/21511
- Status/date: merged / 2026-04-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; associated commits `7431db7392fe`
- Diff scope read: GitHub Pull Request files API returned 6 files, +517/-77, 713 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "[AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend"; the main implementation surface is `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +79/-18 (97 lines); hunks: -292,9 +292,11 @@ def forward_absorb_prepare(; -332,24 +334,69 @@ def forward_absorb_core(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla, _skip_rope_for_nsa_tilelang_fused, touching `forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +79/-18 (97 lines); hunks: -292,9 +292,11 @@ def forward_absorb_prepare(; -332,24 +334,69 @@ def forward_absorb_core(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla, _skip_rope_for_nsa_tilelang_fused
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py
@@ -292,9 +292,11 @@ def forward_absorb_prepare(
+        skip_rope_for_nsa_tilelang_fused = self._skip_rope_for_nsa_tilelang_fused()
+            and (not skip_rope_for_nsa_tilelang_fused)
@@ -332,24 +334,69 @@ def forward_absorb_core(
-            extra_args = {}
-            if self._fuse_rope_for_trtllm_mla(forward_batch):
-                extra_args = {
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +79/-18
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21405 - Enable IndexCache for DeepSeek V3.2

- Link: https://github.com/sgl-project/sglang/pull/21405
- Status/date: merged / 2026-04-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `5a3531641735`
- Diff scope read: GitHub Pull Request files API returned 4 files, +196/-20, 358 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Enable IndexCache for DeepSeek V3.2"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "Enable IndexCache for DeepSeek V3.2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +51/-6 (57 lines); hunks: -1106,6 +1106,7 @@ def __init__(; -1175,6 +1176,8 @@ def __init__(; symbols: __init__, op_prepare, op_core, touching `__init__, op_prepare, op_core`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +27/-13 (40 lines); hunks: -91,6 +91,7 @@ def forward_absorb_prepare(; -182,25 +183,31 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla, touching `forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +51/-6 (57 lines); hunks: -1106,6 +1106,7 @@ def __init__(; -1175,6 +1176,8 @@ def __init__(; symbols: __init__, op_prepare, op_core
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +27/-13 (40 lines); hunks: -91,6 +91,7 @@ def forward_absorb_prepare(; -182,25 +183,31 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1106,6 +1106,7 @@ def __init__(
+        is_nextn: bool = False,
@@ -1175,6 +1176,8 @@ def __init__(
+        self.skip_topk = None
+        self.next_skip_topk = None
@@ -1195,6 +1198,26 @@ def __init__(
+            # Refer: https://arxiv.org/abs/2603.12201 for more details.
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py
@@ -91,6 +91,7 @@ def forward_absorb_prepare(
+        prev_topk_indices: Optional[torch.Tensor] = None,
@@ -182,25 +183,31 @@ def forward_absorb_prepare(
-                topk_indices = self.indexer(
-                    x=hidden_states,
-                    q_lora=q_lora,
-                    positions=positions,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +51/-6; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +27/-13
- Risk and verification: The diff ships test coverage in `test/registered/8-gpu-models/test_deepseek_v32_indexcache.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22914 - [Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel

- Link: https://github.com/sgl-project/sglang/pull/22914
- Status/date: merged / 2026-04-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `c304d0d64d30`
- Diff scope read: GitHub Pull Request files API returned 8 files, +148/-402, 783 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +11/-7 (18 lines); hunks: -55,13 +55,9; -112,6 +108,12; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-7 (18 lines); hunks: -55,13 +55,9; -112,6 +108,12; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -55,13 +55,9 @@
-    can_cp_split,
-    cp_all_gather_rerange_output,
-    cp_split_and_rebuild_data,
-    cp_split_and_rebuild_position,
+    can_nsa_cp_split,
-    prepare_input_dp_with_cp_dsa,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23268 - 【NPU】【bugfix】accuracy fix when enable both nsa cp and prefixcache

- Link: https://github.com/sgl-project/sglang/pull/23268
- Status/date: merged / 2026-04-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; associated commits `b1e1fe8eee68`
- Diff scope read: GitHub Pull Request files API returned 2 files, +21/-5, 40 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "【NPU】【bugfix】accuracy fix when enable both nsa cp and prefixcache"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "【NPU】【bugfix】accuracy fix when enable both nsa cp and prefixcache"; the main implementation surface is `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +3/-1 (4 lines); hunks: -359,7 +359,9 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu, touching `forward_dsa_prepare_npu`.
- Code diff details:
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +3/-1 (4 lines); hunks: -359,7 +359,9 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu
- Key code excerpts:

```diff
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -359,7 +359,9 @@ def forward_dsa_prepare_npu(
-            if fused_qkv_a_proj_out.shape[0] < 65535:
+            if fused_qkv_a_proj_out.shape[0] < 65535 and not nsa_use_prefill_cp(
+                forward_batch
+            ):
```

- Reviewed files:
  - runtime: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +3/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24392 - add indexer-topk capture (V3.2 NSA + infra)

- Link: https://github.com/sgl-project/sglang/pull/24392
- Status/date: merged / 2026-05-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; associated commits `47a416fc6272`
- Diff scope read: GitHub Pull Request files API returned 19 files, +428/-18, 785 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "add indexer-topk capture (V3.2 NSA + infra)"; model line: DeepSeek V3.2; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "add indexer-topk capture (V3.2 NSA + infra)"; the main implementation surface is `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +11/-2 (13 lines); hunks: -6,6 +6,9; -205,7 +208,11 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, touching `forward_absorb_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +11/-2 (13 lines); hunks: -6,6 +6,9; -205,7 +208,11 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py
@@ -6,6 +6,9 @@
+from sglang.srt.layers.attention.indexer_topk_capturer import (
+    maybe_capture_indexer_topk,
+)
@@ -205,7 +208,11 @@ def forward_absorb_prepare(
-                    topk_indices = prev_topk_indices
+                    # skip_topk reuses prev layer's indices; mirror into this
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +11/-2
- Risk and verification: The diff ships test coverage in `test/registered/8-gpu-models/test_return_indexer_topk.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #24125 - [AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode

- Link: https://github.com/sgl-project/sglang/pull/24125
- Status/date: merged / 2026-05-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; associated commits `fc20f5b114f9`
- Diff scope read: GitHub Pull Request files API returned 2 files, +60/-20, 110 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode"; model line: DeepSeek V3.2; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "[AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode"; the main implementation surface is `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +48/-18 (66 lines); hunks: -415,25 +415,55 @@ def forward_absorb_core(; symbols: forward_absorb_core, touching `forward_absorb_core`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +48/-18 (66 lines); hunks: -415,25 +415,55 @@ def forward_absorb_core(; symbols: forward_absorb_core
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py
@@ -415,25 +415,55 @@ def forward_absorb_core(
-                q_nope_fused = q_cat[..., : self.kv_lora_rank]
-                q_pe_fused = q_cat[..., self.kv_lora_rank :]
-                if llama_4_scaling is not None:
-                    q_nope_fused *= llama_4_scaling
-                attn_output = self.attn_mqa(
-                    q_nope_fused,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +48/-18
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25233 - [Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers

- Link: https://github.com/sgl-project/sglang/pull/25233
- Status/date: merged / 2026-05-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `7cb4669a049a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +115/-3, 141 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers"; model line: DeepSeek V3.2; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +115/-3 (118 lines); hunks: -1,10 +1,11; -14,8 +15,30; symbols: DeepSeekV32Detector, structure_info, get_structural_tag_name, get_structural_tag, touching `DeepSeekV32Detector, structure_info, get_structural_tag_name`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +115/-3 (118 lines); hunks: -1,10 +1,11; -14,8 +15,30; symbols: DeepSeekV32Detector, structure_info, get_structural_tag_name, get_structural_tag
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv32_detector.py
@@ -1,10 +1,11 @@
+from typing import List, Literal, Optional, Union
-from sglang.srt.entrypoints.openai.protocol import Tool
+from sglang.srt.entrypoints.openai.protocol import Tool, ToolChoice
@@ -14,8 +15,30 @@
+try:
+    from xgrammar import StructuralTag
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +115/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv32_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25821 - [Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename

- Link: https://github.com/sgl-project/sglang/pull/25821
- Status/date: merged / 2026-05-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/utils.py` and 14 files; associated commits `8131641bc66e`
- Diff scope read: GitHub Pull Request files API returned 162 files, +11303/-10745, 15980 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename"; model line: DeepSeek V3.2; category: docs/tests/CI; main diff: `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename"; the main implementation surface is `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/attention/nsa/utils.py` modified +9/-268 (277 lines); hunks: -1,269 +1,10; symbols: aiter_can_use_preshuffle_paged_mqa, compute_nsa_seqlens, is_nsa_enable_prefill_cp, is_nsa_prefill_cp_in_seq_split, touching `aiter_can_use_preshuffle_paged_mqa, compute_nsa_seqlens, is_nsa_enable_prefill_cp`; `python/sglang/srt/layers/attention/dsa/utils.py` added +271/-0 (271 lines); hunks: -0,0 +1,271; symbols: aiter_can_use_preshuffle_paged_mqa, compute_dsa_seqlens, is_dsa_enable_prefill_cp, is_dsa_prefill_cp_in_seq_split, touching `aiter_can_use_preshuffle_paged_mqa, compute_dsa_seqlens, is_dsa_enable_prefill_cp`; `python/sglang/srt/models/deepseek_v2.py` modified +37/-37 (74 lines); hunks: -40,10 +40,10; -59,19 +59,19; symbols: __init__, forward, touching `__init__, forward`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +33/-26 (59 lines); hunks: -6,7 +6,7; -124,7 +124,6 @@ def fused_qk_rmsnorm_bf16(q, q_weight, q_eps, k, k_weight, k...; symbols: fused_qk_rmsnorm_bf16, DeepseekMLAForwardMixin, init_mla_forward, forward_absorb_prepare, touching `fused_qk_rmsnorm_bf16, DeepseekMLAForwardMixin, init_mla_forward`.
- Code diff details:
  - `python/sglang/srt/layers/attention/nsa/utils.py` modified +9/-268 (277 lines); hunks: -1,269 +1,10; symbols: aiter_can_use_preshuffle_paged_mqa, compute_nsa_seqlens, is_nsa_enable_prefill_cp, is_nsa_prefill_cp_in_seq_split
  - `python/sglang/srt/layers/attention/dsa/utils.py` added +271/-0 (271 lines); hunks: -0,0 +1,271; symbols: aiter_can_use_preshuffle_paged_mqa, compute_dsa_seqlens, is_dsa_enable_prefill_cp, is_dsa_prefill_cp_in_seq_split
  - `python/sglang/srt/models/deepseek_v2.py` modified +37/-37 (74 lines); hunks: -40,10 +40,10; -59,19 +59,19; symbols: __init__, forward
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +33/-26 (59 lines); hunks: -6,7 +6,7; -124,7 +124,6 @@ def fused_qk_rmsnorm_bf16(q, q_weight, q_eps, k, k_weight, k...; symbols: fused_qk_rmsnorm_bf16, DeepseekMLAForwardMixin, init_mla_forward, forward_absorb_prepare
  - `python/sglang/srt/layers/utils/cp_utils.py` modified +20/-20 (40 lines); hunks: -66,17 +66,17 @@ def can_cp_split(seq_len: int, cp_size: int, forward_batch):; -88,18 +88,18 @@ def cp_split_and_rebuild_data(forward_batch, input_: torch.T...; symbols: can_cp_split, cp_split_and_rebuild_data, cp_split_and_rebuild_position, cp_all_gather_rerange_output
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/attention/nsa/utils.py
@@ -1,269 +1,10 @@
-from functools import lru_cache
-from typing import TYPE_CHECKING, List, Tuple, Union
-import torch
-import triton
-import triton.language as tl
-from sglang.srt.layers.dp_attention import (
diff -- python/sglang/srt/layers/attention/dsa/utils.py
@@ -0,0 +1,271 @@
+from functools import lru_cache
+from typing import TYPE_CHECKING, List, Tuple, Union
+import torch
+import triton
+import triton.language as tl
+from sglang.srt.environ import envs
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -40,10 +40,10 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/attention/nsa/utils.py` modified +9/-268; `python/sglang/srt/layers/attention/dsa/utils.py` added +271/-0; `python/sglang/srt/models/deepseek_v2.py` modified +37/-37; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +33/-26; `python/sglang/srt/layers/utils/cp_utils.py` modified +20/-20; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +11/-11
- Risk and verification: The diff ships test coverage in `python/sglang/jit_kernel/tests/test_fused_metadata_copy.py`, `python/sglang/jit_kernel/tests/test_fused_store_index_cache.py`, `python/sglang/jit_kernel/tests/test_set_mla_kv_buffer.py`, `python/sglang/test/nightly_utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #23351 - Support piecewise CUDA graph with NSA

- Link: https://github.com/sgl-project/sglang/pull/23351
- Status/date: merged / 2026-05-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `cadfa2d025d3`
- Diff scope read: GitHub Pull Request files API returned 12 files, +317/-58, 682 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support piecewise CUDA graph with NSA"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Support piecewise CUDA graph with NSA"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1980,6 +1980,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1980,6 +1980,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1980,6 +1980,7 @@ def forward(
+            and not torch.compiler.is_compiling()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `test/registered/piecewise_cuda_graph/test_pcg_glm5_fp4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27705 - Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels

- Link: https://github.com/sgl-project/sglang/pull/27705
- Status/date: merged / 2026-06-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; associated commits `073de150530a`
- Diff scope read: GitHub Pull Request files API returned 13 files, +1196/-69, 1573 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; technical summary: Covers "Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels"; the main implementation surface is `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +61/-0 (61 lines); hunks: -76,6 +76,52 @@ def _clone_if_runai_streamed_tensor(tensor: torch.Tensor) ->...; -147,6 +193,8 @@ def do_load_weights(; symbols: _clone_if_runai_streamed_tensor, _load_fused_indexer_wk, NextNEnabledConfig, do_load_weights, touching `_clone_if_runai_streamed_tensor, _load_fused_indexer_wk, NextNEnabledConfig`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +61/-0 (61 lines); hunks: -76,6 +76,52 @@ def _clone_if_runai_streamed_tensor(tensor: torch.Tensor) ->...; -147,6 +193,8 @@ def do_load_weights(; symbols: _clone_if_runai_streamed_tensor, _load_fused_indexer_wk, NextNEnabledConfig, do_load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py
@@ -76,6 +76,52 @@ def _clone_if_runai_streamed_tensor(tensor: torch.Tensor) -> torch.Tensor:
+def _load_fused_indexer_wk(
+    name: str,
+    loaded_weight: torch.Tensor,
+    params_dict: Dict[str, torch.Tensor],
+    pending: Dict[str, Dict[str, torch.Tensor]],
+    quant_config: Optional[QuantizationConfig],
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +61/-0
- Risk and verification: The diff ships test coverage in `test/registered/8-gpu-models/test_deepseek_v32_indexcache.py`, `test/registered/jit/test_dsv32_indexer_fusion.py`, `test/registered/models_e2e/test_dsa_glm5_dp_mtp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31888 - [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations

- Link: https://github.com/sgl-project/sglang/pull/31888
- Status/date: merged / 2026-07-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `e4a40a71f84c`
- Diff scope read: GitHub Pull Request files API returned 30 files, +3837/-52, 4635 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations"; model line: DeepSeek V3.2; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +180/-18 (198 lines); hunks: -241,6 +241,9; -307,6 +310,7 @@ def forward(; symbols: forward, __init__, get_moe_weights, forward_normal_dual_stream, touching `forward, __init__, get_moe_weights`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +174/-0 (174 lines); hunks: -6,6 +6,7; -52,6 +53,7; symbols: _make_mla_bmm_fusion_plan, _q8kv8_born_fp8_q_backend, forward_absorb_prepare, touching `_make_mla_bmm_fusion_plan, _q8kv8_born_fp8_q_backend, forward_absorb_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +180/-18 (198 lines); hunks: -241,6 +241,9; -307,6 +310,7 @@ def forward(; symbols: forward, __init__, get_moe_weights, forward_normal_dual_stream
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +174/-0 (174 lines); hunks: -6,6 +6,7; -52,6 +53,7; symbols: _make_mla_bmm_fusion_plan, _q8kv8_born_fp8_q_backend, forward_absorb_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -241,6 +241,9 @@
+# One-time SGLANG_OPT_MOE_QUANT_ONCE engagement log (see _moe_quant_once_enabled).
+_moe_quant_once_logged = False
@@ -307,6 +310,7 @@ def forward(
+        gateup_pre_quant: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
@@ -336,17 +340,24 @@ def forward(
-        if (
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py
@@ -6,6 +6,7 @@
+from sglang.kernels.ops.kvcache.cache_ops import absorbed_bmm_concat_cast_q_fp8
@@ -52,6 +53,7 @@
+    get_tc_piecewise_forward_context,
@@ -75,6 +77,8 @@
+_ENABLE_DSA_Q8KV8_BORN_FP8_Q = envs.SGLANG_ENABLE_DSA_Q8KV8_BORN_FP8_Q.get()
+_ENABLE_DSA_Q8KV8_QPREP_OVERLAP = envs.SGLANG_ENABLE_DSA_Q8KV8_QPREP_OVERLAP.get()
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +180/-18; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +174/-0
- Risk and verification: The diff ships test coverage in `test/manual/test_moe_quant_once.py`, `test/registered/kernels/ops/attention/test_qprep_bf16_fp8_sm90.py`, `test/registered/kernels/ops/attention/test_sparse_mla_q8kv8_prefill_sm90.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
