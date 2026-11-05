# sglang DeepSeek V3.2 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/docs/references/multi_node_deployment/rbg_pd/deepseekv32_pd.mdx` | 无直接 PR 号提交 |
| `examples/chat_template/tool_chat_template_deepseekv32.jinja` | [#11063](https://github.com/sgl-project/sglang/pull/11063) |
| `python/sglang/kernels/jit/csrc/deepseek_v32/indexer_k.cuh` | 无直接 PR 号提交 |
| `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` | 无直接 PR 号提交 |
| `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` | [#14249](https://github.com/sgl-project/sglang/pull/14249), [#14353](https://github.com/sgl-project/sglang/pull/14353) |
| `python/sglang/srt/function_call/deepseekv32_detector.py` | [#14249](https://github.com/sgl-project/sglang/pull/14249), [#14573](https://github.com/sgl-project/sglang/pull/14573), [#14750](https://github.com/sgl-project/sglang/pull/14750), [#15278](https://github.com/sgl-project/sglang/pull/15278), [#16091](https://github.com/sgl-project/sglang/pull/16091), [#18174](https://github.com/sgl-project/sglang/pull/18174), [#25233](https://github.com/sgl-project/sglang/pull/25233) |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | [#13959](https://github.com/sgl-project/sglang/pull/13959), [#14541](https://github.com/sgl-project/sglang/pull/14541), [#14572](https://github.com/sgl-project/sglang/pull/14572), [#15381](https://github.com/sgl-project/sglang/pull/15381), [#17007](https://github.com/sgl-project/sglang/pull/17007), [#19428](https://github.com/sgl-project/sglang/pull/19428), [#23268](https://github.com/sgl-project/sglang/pull/23268), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_common/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/a8w8_blockscale_bpreshuffle_tuned_gemm.csv` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=2048-K=7168.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=7168-K=2048.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=8192-K=1536.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_tune.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_act.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_moe.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | [#18931](https://github.com/sgl-project/sglang/pull/18931), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | [#21405](https://github.com/sgl-project/sglang/pull/21405), [#21511](https://github.com/sgl-project/sglang/pull/21511), [#24125](https://github.com/sgl-project/sglang/pull/24125), [#24392](https://github.com/sgl-project/sglang/pull/24392), [#25821](https://github.com/sgl-project/sglang/pull/25821), [#31888](https://github.com/sgl-project/sglang/pull/31888) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/triton_qk_rmsnorm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | [#27705](https://github.com/sgl-project/sglang/pull/27705) |
| `python/sglang/srt/models/deepseek_common/moe_transport.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/utils.py` | [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `python/sglang/srt/models/deepseek_v2.py` | [#11061](https://github.com/sgl-project/sglang/pull/11061), [#11510](https://github.com/sgl-project/sglang/pull/11510), [#11892](https://github.com/sgl-project/sglang/pull/11892), [#12065](https://github.com/sgl-project/sglang/pull/12065), [#12094](https://github.com/sgl-project/sglang/pull/12094), [#12788](https://github.com/sgl-project/sglang/pull/12788), [#12816](https://github.com/sgl-project/sglang/pull/12816), [#12964](https://github.com/sgl-project/sglang/pull/12964), [#13459](https://github.com/sgl-project/sglang/pull/13459), [#13544](https://github.com/sgl-project/sglang/pull/13544), [#13959](https://github.com/sgl-project/sglang/pull/13959), [#14572](https://github.com/sgl-project/sglang/pull/14572), ... (25 total) |
| `test/manual/nightly/test_deepseek_v32_perf.py` | [#13646](https://github.com/sgl-project/sglang/pull/13646), [#21192](https://github.com/sgl-project/sglang/pull/21192), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/manual/quant/test_deepseek_v32_fp4_4gpu.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_dp_eval_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_eval_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_mtp_eval_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v32_tc_eval_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` | [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` | [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/perf/mi30x/test_deepseek_v32_basic_perf_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi30x/test_deepseek_v32_mtp_perf_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/test_deepseek_v32_basic.py` | [#16934](https://github.com/sgl-project/sglang/pull/16934), [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17432](https://github.com/sgl-project/sglang/pull/17432), [#17633](https://github.com/sgl-project/sglang/pull/17633), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/amd/test_deepseek_v32_mtp.py` | [#16934](https://github.com/sgl-project/sglang/pull/16934), [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17432](https://github.com/sgl-project/sglang/pull/17432), [#17633](https://github.com/sgl-project/sglang/pull/17633), [#25821](https://github.com/sgl-project/sglang/pull/25821) |
| `test/registered/e2e/models_large/test_deepseek_v32_indexcache.py` | 无直接 PR 号提交 |
| `test/registered/unit/function_call/test_deepseekv32_detector.py` | 无直接 PR 号提交 |
| `test/registered/unit/model_executor/test_compensated_mhc_update_guard.py` | 无直接 PR 号提交 |
| `test/registered/xpu/llm_models/test_xpu_deepseek_v2_lite_chat_fp8_gsm8k_eval.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 49
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 49
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #11063 - Add DeepSeek-V3.2 Tool Call Template

- 链接: https://github.com/sgl-project/sglang/pull/11063
- 状态/时间: merged / 2025-10-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv32.jinja`；关联提交 `85c1f7937781`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+100/-0，可读 patch 101 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add DeepSeek-V3.2 Tool Call Template」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `examples/chat_template/tool_chat_template_deepseekv32.jinja`；技术摘要: 覆盖「Add DeepSeek-V3.2 Tool Call Template」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv32.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/chat_template/tool_chat_template_deepseekv32.jinja` added +100/-0 (100 lines); hunks: -0,0 +1,100。
- 代码 diff 细节:
  - `examples/chat_template/tool_chat_template_deepseekv32.jinja` added +100/-0 (100 lines); hunks: -0,0 +1,100
- 关键代码摘录:

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

- 已读文件:
  - docs: `examples/chat_template/tool_chat_template_deepseekv32.jinja` added +100/-0
- 验证与风险: 该 PR 主要落在文档/示例 `examples/chat_template/tool_chat_template_deepseekv32.jinja`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #11061 - Support DeepSeek V3.2 Exp

- 链接: https://github.com/sgl-project/sglang/pull/11061
- 状态/时间: merged / 2025-10-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `efbc687c2817`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 29 个文件，+4542/-141，可读 patch 5365 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support DeepSeek V3.2 Exp」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Support DeepSeek V3.2 Exp」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +329/-17 (346 lines); hunks: -15,6 +15,7; -25,10 +26,16; symbols: AttnForwardMethod, handle_attention_ascend, _get_sum_extend_prefix_lens, _is_extend_without_speculative，涉及 `AttnForwardMethod, handle_attention_ascend, _get_sum_extend_prefix_lens`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +329/-17 (346 lines); hunks: -15,6 +15,7; -25,10 +26,16; symbols: AttnForwardMethod, handle_attention_ascend, _get_sum_extend_prefix_lens, _is_extend_without_speculative
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +329/-17
- 验证与风险: diff 自带测试面 `python/sglang/test/get_logits_ut.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #11510 - [Bugfix] Fix Qwen3/DSV3/DSV3.2 model support

- 链接: https://github.com/sgl-project/sglang/pull/11510
- 状态/时间: merged / 2025-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `3cceaa381ad3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+102/-33，可读 patch 359 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1357,6 +1357,7 @@ def forward_prepare(; symbols: forward_prepare，涉及 `forward_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1357,6 +1357,7 @@ def forward_prepare(; symbols: forward_prepare
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1357,6 +1357,7 @@ def forward_prepare(
+                inner_state = (*inner_state, None)  # add a position for topk_indices
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0
- 验证与风险: diff 自带测试面 `test/srt/ascend/test_ascend_deepep.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #12094 - Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4

- 链接: https://github.com/sgl-project/sglang/pull/12094
- 状态/时间: merged / 2025-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `9ff9fa7f95be`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+110/-22，可读 patch 231 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +65/-0 (65 lines); hunks: -224,6 +224,17 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1143,6 +1154,9 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__，涉及 `add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +65/-0 (65 lines); hunks: -224,6 +224,17 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1143,6 +1154,9 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +65/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #11892 - DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill

- 链接: https://github.com/sgl-project/sglang/pull/11892
- 状态/时间: merged / 2025-11-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `f235498eca7a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+188/-4，可读 patch 255 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +43/-2 (45 lines); hunks: -402,6 +402,34 @@ def handle_attention_aiter(attn, forward_batch):; -1478,8 +1506,21 @@ def forward_normal_prepare(; symbols: handle_attention_aiter, handle_attention_nsa, forward_normal_prepare，涉及 `handle_attention_aiter, handle_attention_nsa, forward_normal_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +43/-2 (45 lines); hunks: -402,6 +402,34 @@ def handle_attention_aiter(attn, forward_batch):; -1478,8 +1506,21 @@ def forward_normal_prepare(; symbols: handle_attention_aiter, handle_attention_nsa, forward_normal_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +43/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #12788 - [DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)

- 链接: https://github.com/sgl-project/sglang/pull/12788
- 状态/时间: merged / 2025-11-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `7257525ccea6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+53/-6，可读 patch 96 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -415,11 +415,14 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa，涉及 `handle_attention_nsa`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -415,11 +415,14 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #12816 - [Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative

- 链接: https://github.com/sgl-project/sglang/pull/12816
- 状态/时间: merged / 2025-11-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `bef37d6de86a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-18，可读 patch 112 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +6/-14 (20 lines); hunks: -308,14 +308,6 @@ def _get_sum_extend_prefix_lens(forward_batch):; -334,7 +326,7 @@ def _handle_attention_backend(; symbols: _get_sum_extend_prefix_lens, _is_extend_without_speculative, _support_mha_one_shot, _handle_attention_backend，涉及 `_get_sum_extend_prefix_lens, _is_extend_without_speculative, _support_mha_one_shot`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +6/-14 (20 lines); hunks: -308,14 +308,6 @@ def _get_sum_extend_prefix_lens(forward_batch):; -334,7 +326,7 @@ def _handle_attention_backend(; symbols: _get_sum_extend_prefix_lens, _is_extend_without_speculative, _support_mha_one_shot, _handle_attention_backend
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +6/-14
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #12065 - (1/n)support context parallel with deepseekv3.2-DSA

- 链接: https://github.com/sgl-project/sglang/pull/12065
- 状态/时间: merged / 2025-11-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `d368c7451a48`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 17 个文件，+1247/-54，可读 patch 1729 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「(1/n)support context parallel with deepseekv3.2-DSA」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「(1/n)support context parallel with deepseekv3.2-DSA」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +134/-32 (166 lines); hunks: -54,13 +54,23; -412,7 +422,9 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, __init__, forward，涉及 `handle_attention_nsa, __init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +134/-32 (166 lines); hunks: -54,13 +54,23; -412,7 +422,9 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +134/-32
- 验证与风险: diff 自带测试面 `test/srt/run_suite.py`, `test/srt/test_deepseek_v32_cp_single_node.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #12964 - [DeepseekV3.2] Deepseek fp8 support for MHA path

- 链接: https://github.com/sgl-project/sglang/pull/12964
- 状态/时间: merged / 2025-11-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `fa924410276d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+55/-9，可读 patch 114 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepseekV3.2] Deepseek fp8 support for MHA path」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepseekV3.2] Deepseek fp8 support for MHA path」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +46/-8 (54 lines); hunks: -53,6 +53,7; -418,8 +419,6 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, forward_normal_prepare, _get_mla_kv_buffer, _get_mla_kv_buffer_from_fp8，涉及 `handle_attention_nsa, forward_normal_prepare, _get_mla_kv_buffer`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +46/-8 (54 lines); hunks: -53,6 +53,7; -418,8 +419,6 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, forward_normal_prepare, _get_mla_kv_buffer, _get_mla_kv_buffer_from_fp8
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +46/-8
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13459 - [Deepseek V3.2] Change indexer weights_proj to fp32

- 链接: https://github.com/sgl-project/sglang/pull/13459
- 状态/时间: merged / 2025-11-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `7291c72e575d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+92/-124，可读 patch 345 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Deepseek V3.2] Change indexer weights_proj to fp32」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek V3.2] Change indexer weights_proj to fp32」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +0/-71 (71 lines); hunks: -239,17 +239,6 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1226,9 +1215,6 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__，涉及 `add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +0/-71 (71 lines); hunks: -239,17 +239,6 @@ def add_forward_absorb_core_attention_backend(backend_name):; -1226,9 +1215,6 @@ def __init__(; symbols: add_forward_absorb_core_attention_backend, is_nsa_indexer_wk_and_weights_proj_fused, AttnForwardMethod, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +0/-71
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13544 - [DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend

- 链接: https://github.com/sgl-project/sglang/pull/13544
- 状态/时间: merged / 2025-11-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `5eed5fc0b091`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+74/-78，可读 patch 342 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +5/-36 (41 lines); hunks: -417,43 +417,12 @@ def handle_attention_aiter(attn, forward_batch):; symbols: handle_attention_aiter, handle_attention_nsa，涉及 `handle_attention_aiter, handle_attention_nsa`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-36 (41 lines); hunks: -417,43 +417,12 @@ def handle_attention_aiter(attn, forward_batch):; symbols: handle_attention_aiter, handle_attention_nsa
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-36
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13646 - [DeepSeekV3.2] Enable pure TP & Partial DP Attention

- 链接: https://github.com/sgl-project/sglang/pull/13646
- 状态/时间: merged / 2025-11-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/manual/nightly/test_deepseek_v32_perf.py`；关联提交 `decb48965dd1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+286/-24，可读 patch 460 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeekV3.2] Enable pure TP & Partial DP Attention」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `test/manual/nightly/test_deepseek_v32_perf.py`, `test/nightly/test_deepseek_v32_perf.py`；技术摘要: 覆盖「[DeepSeekV3.2] Enable pure TP & Partial DP Attention」；主要实现面是 `test/manual/nightly/test_deepseek_v32_perf.py`, `test/nightly/test_deepseek_v32_perf.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/manual/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass，涉及 `setUpClass`；`test/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass，涉及 `setUpClass`。
- 代码 diff 细节:
  - `test/manual/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass
  - `test/nightly/test_deepseek_v32_perf.py` modified +25/-0 (25 lines); hunks: -25,6 +25,9 @@ def setUpClass(cls):; -35,6 +38,9 @@ def setUpClass(cls):; symbols: setUpClass
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/manual/nightly/test_deepseek_v32_perf.py` modified +25/-0; `test/nightly/test_deepseek_v32_perf.py` modified +25/-0
- 验证与风险: diff 自带测试面 `test/manual/nightly/test_deepseek_v32_perf.py`, `test/nightly/test_deepseek_v32_nsabackend.py`, `test/nightly/test_deepseek_v32_perf.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14249 - feat: DeepSeek new v3.2 encoding

- 链接: https://github.com/sgl-project/sglang/pull/14249
- 状态/时间: merged / 2025-12-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `7c38eca1e4a7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+1153/-89，可读 patch 1359 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: DeepSeek new v3.2 encoding」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「feat: DeepSeek new v3.2 encoding」；主要实现面是 `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` added +451/-0 (451 lines); hunks: -0,0 +1,451; symbols: to_json, tools_from_openai_format, tool_calls_from_openai_format, tool_calls_to_openai_format，涉及 `to_json, tools_from_openai_format, tool_calls_from_openai_format`；`python/sglang/srt/function_call/deepseekv32_detector.py` added +321/-0 (321 lines); hunks: -0,0 +1,321; symbols: DeepSeekV32Detector, __init__, has_tool_call, _parse_parameters_from_xml，涉及 `DeepSeekV32Detector, __init__, has_tool_call`。
- 代码 diff 细节:
  - `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` added +451/-0 (451 lines); hunks: -0,0 +1,451; symbols: to_json, tools_from_openai_format, tool_calls_from_openai_format, tool_calls_to_openai_format
  - `python/sglang/srt/function_call/deepseekv32_detector.py` added +321/-0 (321 lines); hunks: -0,0 +1,321; symbols: DeepSeekV32Detector, __init__, has_tool_call, _parse_parameters_from_xml
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` added +451/-0; `python/sglang/srt/function_call/deepseekv32_detector.py` added +321/-0
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`, `test/srt/openai_server/basic/test_serving_chat.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14573 - [Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode

- 链接: https://github.com/sgl-project/sglang/pull/14573
- 状态/时间: merged / 2025-12-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `b7b7524e9560`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+144/-7，可读 patch 165 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +2/-7 (9 lines); hunks: -241,13 +241,8 @@ def parse_streaming_increment(; symbols: parse_streaming_increment，涉及 `parse_streaming_increment`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +2/-7 (9 lines); hunks: -241,13 +241,8 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +2/-7
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14541 - [NPU]dsv3.2 cp for npu

- 链接: https://github.com/sgl-project/sglang/pull/14541
- 状态/时间: merged / 2025-12-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；关联提交 `388018a5bd41`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+281/-134，可读 patch 587 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]dsv3.2 cp for npu」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU]dsv3.2 cp for npu」；主要实现面是 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +9/-0 (9 lines); hunks: -311,8 +311,17 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu，涉及 `forward_dsa_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +9/-0 (9 lines); hunks: -311,8 +311,17 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +9/-0
- 验证与风险: diff 自带测试面 `test/srt/ascend/test_ascend_tp4_bf16.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14572 - [NPU] optimization for dsv3.2

- 链接: https://github.com/sgl-project/sglang/pull/14572
- 状态/时间: merged / 2025-12-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c05d3afb5d8b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+141/-68，可读 patch 393 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU] optimization for dsv3.2」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU] optimization for dsv3.2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +25/-4 (29 lines); hunks: -700,6 +700,7 @@ def __init__(; -738,7 +739,11 @@ def __init__(; symbols: __init__, forward_deepep, _post_combine_hook，涉及 `__init__, forward_deepep, _post_combine_hook`；`python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +34/-18 (52 lines); hunks: -273,39 +273,51 @@ def forward_dsa_prepare_npu(; -367,7 +379,11 @@ def forward_dsa_core_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu，涉及 `forward_dsa_prepare_npu, forward_dsa_core_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +25/-4 (29 lines); hunks: -700,6 +700,7 @@ def __init__(; -738,7 +739,11 @@ def __init__(; symbols: __init__, forward_deepep, _post_combine_hook
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +34/-18 (52 lines); hunks: -273,39 +273,51 @@ def forward_dsa_prepare_npu(; -367,7 +379,11 @@ def forward_dsa_core_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +25/-4; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +34/-18
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/hardware_backend/npu/moe/topk.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #15278 - feat: DeepSeek-V3.2 Streaming tool call output

- 链接: https://github.com/sgl-project/sglang/pull/15278
- 状态/时间: merged / 2025-12-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `41683536d394`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+111/-69，可读 patch 328 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: DeepSeek-V3.2 Streaming tool call output」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「feat: DeepSeek-V3.2 Streaming tool call output」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +95/-65 (160 lines); hunks: -1,7 +1,6; -11,6 +10,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml，涉及 `__init__, has_tool_call, _parse_parameters_from_xml`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +95/-65 (160 lines); hunks: -1,7 +1,6; -11,6 +10,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +95/-65
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14353 - feat(dsv32): better error handling for DeepSeek-v3.2 encoder

- 链接: https://github.com/sgl-project/sglang/pull/14353
- 状态/时间: merged / 2025-12-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`；关联提交 `216067c0cba2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+53/-32，可读 patch 197 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat(dsv32): better error handling for DeepSeek-v3.2 encoder」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`；技术摘要: 覆盖「feat(dsv32): better error handling for DeepSeek-v3.2 encoder」；主要实现面是 `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` modified +45/-32 (77 lines); hunks: -4,6 +4,11; -148,11 +153,12 @@ def find_last_user_index(messages: List[Dict[str, Any]]) -...; symbols: DS32EncodingError, find_last_user_index, render_message，涉及 `DS32EncodingError, find_last_user_index, render_message`。
- 代码 diff 细节:
  - `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` modified +45/-32 (77 lines); hunks: -4,6 +4,11; -148,11 +153,12 @@ def find_last_user_index(messages: List[Dict[str, Any]]) -...; symbols: DS32EncodingError, find_last_user_index, render_message
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py` modified +45/-32
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/entrypoints/openai/serving_base.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14901 - fix ds3.2 nsa backend prefill TBO

- 链接: https://github.com/sgl-project/sglang/pull/14901
- 状态/时间: merged / 2025-12-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `350fbbf4dc1e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+76/-2，可读 patch 148 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix ds3.2 nsa backend prefill TBO」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「fix ds3.2 nsa backend prefill TBO」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -66,6 +66,7; -421,7 +422,10 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, _get_mla_kv_buffer_from_fp8，涉及 `handle_attention_nsa, _get_mla_kv_buffer_from_fp8`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -66,6 +66,7; -421,7 +422,10 @@ def handle_attention_nsa(attn, forward_batch):; symbols: handle_attention_nsa, _get_mla_kv_buffer_from_fp8
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1
- 验证与风险: diff 自带测试面 `test/srt/ep/test_deepep_large.py`, `test/srt/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14750 - [Tool Call][DSV32] Streamline function call parameters

- 链接: https://github.com/sgl-project/sglang/pull/14750
- 状态/时间: merged / 2025-12-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `01bd0d3e8b8c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+60/-29，可读 patch 200 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Tool Call][DSV32] Streamline function call parameters」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Tool Call][DSV32] Streamline function call parameters」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +23/-15 (38 lines); hunks: -2,6 +2,8; -10,7 +12,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml, parse_streaming_increment，涉及 `__init__, has_tool_call, _parse_parameters_from_xml`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +23/-15 (38 lines); hunks: -2,6 +2,8; -10,7 +12,7; symbols: __init__, has_tool_call, _parse_parameters_from_xml, parse_streaming_increment
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +23/-15
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #13959 - [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache

- 链接: https://github.com/sgl-project/sglang/pull/13959
- 状态/时间: merged / 2026-01-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `0d244116d28a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+603/-264，可读 patch 1414 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +10/-16 (26 lines); hunks: -64,8 +64,8; -578,9 +578,7 @@ def forward(; symbols: forward, forward_absorb_prepare，涉及 `forward, forward_absorb_prepare`；`python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +5/-5 (10 lines); hunks: -10,7 +10,7; -192,12 +192,12 @@ def forward_mla_prepare_npu(; symbols: forward_mla_prepare_npu, forward_dsa_prepare_npu，涉及 `forward_mla_prepare_npu, forward_dsa_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +10/-16 (26 lines); hunks: -64,8 +64,8; -578,9 +578,7 @@ def forward(; symbols: forward, forward_absorb_prepare
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +5/-5 (10 lines); hunks: -10,7 +10,7; -192,12 +192,12 @@ def forward_mla_prepare_npu(; symbols: forward_mla_prepare_npu, forward_dsa_prepare_npu
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +10/-16; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +5/-5
- 验证与风险: diff 自带测试面 `test/manual/test_deepseek_v32_cp_single_node.py`, `test/srt/test_prefill_adder.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #16637 - [DSv32] Overlap indexer weights_proj during dual_stream decode

- 链接: https://github.com/sgl-project/sglang/pull/16637
- 状态/时间: merged / 2026-01-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `20abaee26cd8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+64/-22，可读 patch 134 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DSv32] Overlap indexer weights_proj during dual_stream decode」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DSv32] Overlap indexer weights_proj during dual_stream decode」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +34/-11 (45 lines); hunks: -1666,6 +1666,7 @@ def forward_absorb_prepare(; -1722,8 +1723,39 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare，涉及 `forward_absorb_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +34/-11 (45 lines); hunks: -1666,6 +1666,7 @@ def forward_absorb_prepare(; -1722,8 +1723,39 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +34/-11
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16841 - [AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant

- 链接: https://github.com/sgl-project/sglang/pull/16841
- 状态/时间: merged / 2026-01-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `afe285f7bd9a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+260/-81，可读 patch 587 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +58/-18 (76 lines); hunks: -1523,10 +1523,34 @@ def forward_normal_prepare(; -1703,31 +1727,47 @@ def forward_absorb_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare，涉及 `forward_normal_prepare, forward_absorb_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +58/-18 (76 lines); hunks: -1523,10 +1523,34 @@ def forward_normal_prepare(; -1703,31 +1727,47 @@ def forward_absorb_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +58/-18
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16934 - [AMD] Enable DeepseekV3.2 test for AMD CI

- 链接: https://github.com/sgl-project/sglang/pull/16934
- 状态/时间: merged / 2026-01-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；关联提交 `968c4f55b194`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+379/-1，可读 patch 403 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Enable DeepseekV3.2 test for AMD CI」；模型线: DeepSeek V3.2；类别: 文档/测试/CI；主要 diff: `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_deepseek_v32_basic.py`；技术摘要: 覆盖「[AMD] Enable DeepseekV3.2 test for AMD CI」；主要实现面是 `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_deepseek_v32_basic.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/test_deepseek_v32_mtp.py` added +213/-0 (213 lines); hunks: -0,0 +1,213; symbols: TestDeepseekV32DPMTP, setUpClass, tearDownClass, test_a_gsm8k，涉及 `TestDeepseekV32DPMTP, setUpClass, tearDownClass`；`test/registered/amd/test_deepseek_v32_basic.py` added +163/-0 (163 lines); hunks: -0,0 +1,163; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k，涉及 `TestDeepseekV32DP, setUpClass, tearDownClass`。
- 代码 diff 细节:
  - `test/registered/amd/test_deepseek_v32_mtp.py` added +213/-0 (213 lines); hunks: -0,0 +1,213; symbols: TestDeepseekV32DPMTP, setUpClass, tearDownClass, test_a_gsm8k
  - `test/registered/amd/test_deepseek_v32_basic.py` added +163/-0 (163 lines); hunks: -0,0 +1,163; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/test_deepseek_v32_mtp.py` added +213/-0; `test/registered/amd/test_deepseek_v32_basic.py` added +163/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17179 - [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests

- 链接: https://github.com/sgl-project/sglang/pull/17179
- 状态/时间: merged / 2026-01-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`, `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；关联提交 `a3addd6203ca`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 18 个文件，+1140/-99，可读 patch 1539 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`；技术摘要: 覆盖「[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_display_name, get_one_example，涉及 `ModelConfig, __post_init__, get_display_name`；`test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32MTPPerformance, setUpClass, test_bench_one_batch，涉及 `generate_simple_markdown_report, TestNightlyDeepseekV32MTPPerformance, setUpClass`；`test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` added +134/-0 (134 lines); hunks: -0,0 +1,134; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32BasicPerformance, setUpClass, test_bench_one_batch，涉及 `generate_simple_markdown_report, TestNightlyDeepseekV32BasicPerformance, setUpClass`；`test/registered/amd/test_deepseek_v32_basic.py` modified +1/-1 (2 lines); hunks: -16,7 +16,7; symbols: TestDeepseekV32DP，涉及 `TestDeepseekV32DP`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` added +251/-0 (251 lines); hunks: -0,0 +1,251; symbols: ModelConfig, __post_init__, get_display_name, get_one_example
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32MTPPerformance, setUpClass, test_bench_one_batch
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` added +134/-0 (134 lines); hunks: -0,0 +1,134; symbols: generate_simple_markdown_report, TestNightlyDeepseekV32BasicPerformance, setUpClass, test_bench_one_batch
  - `test/registered/amd/test_deepseek_v32_basic.py` modified +1/-1 (2 lines); hunks: -16,7 +16,7; symbols: TestDeepseekV32DP
  - `test/registered/amd/test_deepseek_v32_mtp.py` modified +1/-1 (2 lines); hunks: -18,7 +18,7; symbols: TestDeepseekV32DPMTP
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` added +251/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` added +146/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` added +134/-0; `test/registered/amd/test_deepseek_v32_basic.py` modified +1/-1; `test/registered/amd/test_deepseek_v32_mtp.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/test_vlms_mmmu_eval_amd.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17432 - [AMD] fix amd ci dpskv32

- 链接: https://github.com/sgl-project/sglang/pull/17432
- 状态/时间: merged / 2026-01-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；关联提交 `17807caf82c8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+16/-7，可读 patch 96 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] fix amd ci dpskv32」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；技术摘要: 覆盖「[AMD] fix amd ci dpskv32」；主要实现面是 `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/test_deepseek_v32_basic.py` modified +7/-2 (9 lines); hunks: -15,10 +15,16; -90,7 +96,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DP, setUpClass, test_bs_1_speed, TestDeepseekV32TP，涉及 `TestDeepseekV32DP, setUpClass, test_bs_1_speed`；`test/registered/amd/test_deepseek_v32_mtp.py` modified +2/-2 (4 lines); hunks: -21,6 +21,7; -116,7 +117,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DPMTP, setUpClass, test_bs_1_speed, TestDeepseekV32TPMTP，涉及 `TestDeepseekV32DPMTP, setUpClass, test_bs_1_speed`。
- 代码 diff 细节:
  - `test/registered/amd/test_deepseek_v32_basic.py` modified +7/-2 (9 lines); hunks: -15,10 +15,16; -90,7 +96,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DP, setUpClass, test_bs_1_speed, TestDeepseekV32TP
  - `test/registered/amd/test_deepseek_v32_mtp.py` modified +2/-2 (4 lines); hunks: -21,6 +21,7; -116,7 +117,6 @@ def test_bs_1_speed(self):; symbols: TestDeepseekV32DPMTP, setUpClass, test_bs_1_speed, TestDeepseekV32TPMTP
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/test_deepseek_v32_basic.py` modified +7/-2; `test/registered/amd/test_deepseek_v32_mtp.py` modified +2/-2
- 验证与风险: diff 自带测试面 `python/sglang/test/test_utils.py`, `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17007 - [NPU]bugfix: fix for dsv3.2 and dsvl2

- 链接: https://github.com/sgl-project/sglang/pull/17007
- 状态/时间: merged / 2026-01-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c0b5a180febe`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+129/-46，可读 patch 224 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]bugfix: fix for dsv3.2 and dsvl2」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU]bugfix: fix for dsv3.2 and dsvl2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1220,6 +1220,7 @@ def __init__(; symbols: __init__，涉及 `__init__`；`python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +80/-46 (126 lines); hunks: -64,36 +64,44 @@ def forward_mha_prepare_npu(; -288,10 +296,30 @@ def forward_dsa_prepare_npu(; symbols: forward_mha_prepare_npu, forward_dsa_prepare_npu，涉及 `forward_mha_prepare_npu, forward_dsa_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1220,6 +1220,7 @@ def __init__(; symbols: __init__
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +80/-46 (126 lines); hunks: -64,36 +64,44 @@ def forward_mha_prepare_npu(; -288,10 +296,30 @@ def forward_dsa_prepare_npu(; symbols: forward_mha_prepare_npu, forward_dsa_prepare_npu
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +80/-46
- 验证与风险: diff 自带测试面 `test/registered/ascend/llm_models/test_ascend_deepseek_v3_2_exp_w8a8.py`, `test/registered/ascend/vlm_models/test_ascend_deepseek_vl2.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #15381 - [NPU]DeepSeek-V3.2 support npu mlaprolog

- 链接: https://github.com/sgl-project/sglang/pull/15381
- 状态/时间: merged / 2026-01-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；关联提交 `b56366f8275a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+195/-61，可读 patch 364 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]DeepSeek-V3.2 support npu mlaprolog」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU]DeepSeek-V3.2 support npu mlaprolog」；主要实现面是 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +116/-55 (171 lines); hunks: -1,3 +1,4; -281,61 +282,25 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu, npu_mla_preprocess，涉及 `forward_dsa_prepare_npu, forward_dsa_core_npu, npu_mla_preprocess`。
- 代码 diff 细节:
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +116/-55 (171 lines); hunks: -1,3 +1,4; -281,61 +282,25 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu, forward_dsa_core_npu, npu_mla_preprocess
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +116/-55
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17633 - [AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites

- 链接: https://github.com/sgl-project/sglang/pull/17633
- 状态/时间: merged / 2026-01-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；关联提交 `52bca4287033`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+88/-230，可读 patch 490 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`；技术摘要: 覆盖「[AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites」；主要实现面是 `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/test_deepseek_v32_basic.py` modified +2/-6 (8 lines); hunks: -15,11 +15,7; -159,7 +155,7 @@ def test_bs_1_speed(self):; symbols: test_bs_1_speed，涉及 `test_bs_1_speed`；`test/registered/amd/test_deepseek_v32_mtp.py` modified +6/-1 (7 lines); hunks: -17,7 +17,12。
- 代码 diff 细节:
  - `test/registered/amd/test_deepseek_v32_basic.py` modified +2/-6 (8 lines); hunks: -15,11 +15,7; -159,7 +155,7 @@ def test_bs_1_speed(self):; symbols: test_bs_1_speed
  - `test/registered/amd/test_deepseek_v32_mtp.py` modified +6/-1 (7 lines); hunks: -17,7 +17,12
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/test_deepseek_v32_basic.py` modified +2/-6; `test/registered/amd/test_deepseek_v32_mtp.py` modified +6/-1
- 验证与风险: diff 自带测试面 `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_kimi_k2_instruct.py`, `test/registered/attention/test_triton_sliding_window.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17523 - [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI

- 链接: https://github.com/sgl-project/sglang/pull/17523
- 状态/时间: merged / 2026-01-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`；关联提交 `f8636fbb253a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 27 个文件，+1540/-43，可读 patch 1823 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`；技术摘要: 覆盖「[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: TestDeepseekV32TPMTP, setUpClass, tearDownClass, test_a_gsm8k，涉及 `TestDeepseekV32TPMTP, setUpClass, tearDownClass`；`test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` added +119/-0 (119 lines); hunks: -0,0 +1,119; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k，涉及 `TestDeepseekV32DP, setUpClass, tearDownClass`；`test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` modified +59/-3 (62 lines); hunks: -13,12 +13,17; -57,11 +62,58 @@ def generate_simple_markdown_report(results: List[BenchmarkR...; symbols: generate_simple_markdown_report, _run_benchmark_with_timeout, TestNightlyDeepseekV32MTPPerformance, setUpClass，涉及 `generate_simple_markdown_report, _run_benchmark_with_timeout, TestNightlyDeepseekV32MTPPerformance`；`test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -215,6 +215,9 @@ def test_deepseek_v32_accuracy(self):; symbols: test_deepseek_v32_accuracy，涉及 `test_deepseek_v32_accuracy`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` added +142/-0 (142 lines); hunks: -0,0 +1,142; symbols: TestDeepseekV32TPMTP, setUpClass, tearDownClass, test_a_gsm8k
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` added +119/-0 (119 lines); hunks: -0,0 +1,119; symbols: TestDeepseekV32DP, setUpClass, tearDownClass, test_a_gsm8k
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` modified +59/-3 (62 lines); hunks: -13,12 +13,17; -57,11 +62,58 @@ def generate_simple_markdown_report(results: List[BenchmarkR...; symbols: generate_simple_markdown_report, _run_benchmark_with_timeout, TestNightlyDeepseekV32MTPPerformance, setUpClass
  - `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -215,6 +215,9 @@ def test_deepseek_v32_accuracy(self):; symbols: test_deepseek_v32_accuracy
  - `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` modified +2/-0 (2 lines); hunks: -93,6 +93,8 @@ def setUpClass(cls):; symbols: setUpClass
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py` added +142/-0; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py` added +119/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py` modified +59/-3; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py` modified +3/-0; `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` modified +2/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #18297 - Deepseekv32 compatibility with transformers v5

- 链接: https://github.com/sgl-project/sglang/pull/18297
- 状态/时间: merged / 2026-02-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e8a2c133807c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+33/-19，可读 patch 131 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Deepseekv32 compatibility with transformers v5」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Deepseekv32 compatibility with transformers v5」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -1150,6 +1150,7 @@ def __init__(; -1162,6 +1163,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -1150,6 +1150,7 @@ def __init__(; -1162,6 +1163,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16907 - Fix model loading for DeepSeek-V3.2-AWQ

- 链接: https://github.com/sgl-project/sglang/pull/16907
- 状态/时间: merged / 2026-02-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `190fa8246fbc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-4，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix model loading for DeepSeek-V3.2-AWQ」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix model loading for DeepSeek-V3.2-AWQ」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +8/-4 (12 lines); hunks: -245,10 +245,14 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +8/-4 (12 lines); hunks: -245,10 +245,14 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +8/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18389 - Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4

- 链接: https://github.com/sgl-project/sglang/pull/18389
- 状态/时间: merged / 2026-02-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `0ffd0a3995e5`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+352/-183，可读 patch 914 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -1488,6 +1488,12 @@ def _fuse_rope_for_trtllm_mla(self, forward_batch: Forwar...; symbols: _fuse_rope_for_trtllm_mla，涉及 `_fuse_rope_for_trtllm_mla`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -1488,6 +1488,12 @@ def _fuse_rope_for_trtllm_mla(self, forward_batch: Forwar...; symbols: _fuse_rope_for_trtllm_mla
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1488,6 +1488,12 @@ def _fuse_rope_for_trtllm_mla(self, forward_batch: ForwardBatch) -> bool:
+        if self.current_attention_backend == "nsa":
+            return (
+                get_global_server_args().nsa_decode_backend == "trtllm"
+                or get_global_server_args().nsa_prefill_backend == "trtllm"
+            ) and forward_batch.attn_backend.kv_cache_dtype == torch.float8_e4m3fn
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0
- 验证与风险: diff 自带测试面 `test/registered/hicache/test_nsa_pool_host_unit.py`, `test/registered/kernels/test_nsa_indexer.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #18931 - Fix NSA FP8 KV cache path for both-trtllm MHA one-shot

- 链接: https://github.com/sgl-project/sglang/pull/18931
- 状态/时间: merged / 2026-02-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`；关联提交 `f23a23cc05fc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+8/-1，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix NSA FP8 KV cache path for both-trtllm MHA one-shot」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`；技术摘要: 覆盖「Fix NSA FP8 KV cache path for both-trtllm MHA one-shot」；主要实现面是 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +8/-1 (9 lines); hunks: -215,7 +215,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare，涉及 `forward_normal_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +8/-1 (9 lines); hunks: -215,7 +215,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +8/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19428 - [Feature] add feature mla_ag_after_qlora for dsv3.2

- 链接: https://github.com/sgl-project/sglang/pull/19428
- 状态/时间: merged / 2026-03-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `b3718982a1b4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+101/-9，可读 patch 316 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feature] add feature mla_ag_after_qlora for dsv3.2」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[Feature] add feature mla_ag_after_qlora for dsv3.2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +26/-3 (29 lines); hunks: -1301,13 +1301,15 @@ def forward(; -1318,6 +1320,7 @@ def forward_prepare(; symbols: forward, forward_prepare, __init__，涉及 `forward, forward_prepare, __init__`；`python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +35/-3 (38 lines); hunks: -4,21 +4,24; -28,6 +31,7 @@ def forward_mha_prepare_npu(; symbols: forward_mha_prepare_npu, forward_mla_prepare_npu, forward_dsa_prepare_npu，涉及 `forward_mha_prepare_npu, forward_mla_prepare_npu, forward_dsa_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +26/-3 (29 lines); hunks: -1301,13 +1301,15 @@ def forward(; -1318,6 +1320,7 @@ def forward_prepare(; symbols: forward, forward_prepare, __init__
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +35/-3 (38 lines); hunks: -4,21 +4,24; -28,6 +31,7 @@ def forward_mha_prepare_npu(; symbols: forward_mha_prepare_npu, forward_mla_prepare_npu, forward_dsa_prepare_npu
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +26/-3; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +35/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18174 - [Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON

- 链接: https://github.com/sgl-project/sglang/pull/18174
- 状态/时间: merged / 2026-03-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `6af0448cc9bf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-3，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +6/-3 (9 lines); hunks: -158,9 +158,12 @@ def _parse_parameters_from_xml(; symbols: _parse_parameters_from_xml，涉及 `_parse_parameters_from_xml`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +6/-3 (9 lines); hunks: -158,9 +158,12 @@ def _parse_parameters_from_xml(; symbols: _parse_parameters_from_xml
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +6/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv32_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #16091 - [Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format.

- 链接: https://github.com/sgl-project/sglang/pull/16091
- 状态/时间: merged / 2026-03-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `666caaf9ce76`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+31/-22，可读 patch 151 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format.」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format.」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +17/-21 (38 lines); hunks: -85,6 +85,7 @@ def __init__(self):; -93,27 +94,24 @@ def has_tool_call(self, text: str) -> bool:; symbols: __init__, has_tool_call, _parse_parameters_from_xml，涉及 `__init__, has_tool_call, _parse_parameters_from_xml`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +17/-21 (38 lines); hunks: -85,6 +85,7 @@ def __init__(self):; -93,27 +94,24 @@ def has_tool_call(self, text: str) -> bool:; symbols: __init__, has_tool_call, _parse_parameters_from_xml
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +17/-21
- 验证与风险: diff 自带测试面 `test/registered/function_call/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21192 - Fix CP in-seq-split method for DeepSeek V32 and update related tests

- 链接: https://github.com/sgl-project/sglang/pull/21192
- 状态/时间: merged / 2026-03-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/manual/nightly/test_deepseek_v32_perf.py`；关联提交 `ed316a26efa4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+162/-97，可读 patch 296 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix CP in-seq-split method for DeepSeek V32 and update related tests」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `test/manual/nightly/test_deepseek_v32_perf.py`；技术摘要: 覆盖「Fix CP in-seq-split method for DeepSeek V32 and update related tests」；主要实现面是 `test/manual/nightly/test_deepseek_v32_perf.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/manual/nightly/test_deepseek_v32_perf.py` modified +1/-1 (2 lines); hunks: -3,7 +3,7。
- 代码 diff 细节:
  - `test/manual/nightly/test_deepseek_v32_perf.py` modified +1/-1 (2 lines); hunks: -3,7 +3,7
- 关键代码摘录:

```diff
diff -- test/manual/nightly/test_deepseek_v32_perf.py
@@ -3,7 +3,7 @@
-DEEPSEEK_V32_MODEL_PATH = "deepseek-ai/DeepSeek-V3.2-Exp"
+DEEPSEEK_V32_MODEL_PATH = "deepseek-ai/DeepSeek-V3.2"
```

- 已读文件:
  - tests: `test/manual/nightly/test_deepseek_v32_perf.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #21511 - [AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend

- 链接: https://github.com/sgl-project/sglang/pull/21511
- 状态/时间: merged / 2026-04-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；关联提交 `7431db7392fe`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+517/-77，可读 patch 713 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「[AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend」；主要实现面是 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +79/-18 (97 lines); hunks: -292,9 +292,11 @@ def forward_absorb_prepare(; -332,24 +334,69 @@ def forward_absorb_core(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla, _skip_rope_for_nsa_tilelang_fused，涉及 `forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +79/-18 (97 lines); hunks: -292,9 +292,11 @@ def forward_absorb_prepare(; -332,24 +334,69 @@ def forward_absorb_core(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla, _skip_rope_for_nsa_tilelang_fused
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +79/-18
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21405 - Enable IndexCache for DeepSeek V3.2

- 链接: https://github.com/sgl-project/sglang/pull/21405
- 状态/时间: merged / 2026-04-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `5a3531641735`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+196/-20，可读 patch 358 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable IndexCache for DeepSeek V3.2」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「Enable IndexCache for DeepSeek V3.2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +51/-6 (57 lines); hunks: -1106,6 +1106,7 @@ def __init__(; -1175,6 +1176,8 @@ def __init__(; symbols: __init__, op_prepare, op_core，涉及 `__init__, op_prepare, op_core`；`python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +27/-13 (40 lines); hunks: -91,6 +91,7 @@ def forward_absorb_prepare(; -182,25 +183,31 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla，涉及 `forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +51/-6 (57 lines); hunks: -1106,6 +1106,7 @@ def __init__(; -1175,6 +1176,8 @@ def __init__(; symbols: __init__, op_prepare, op_core
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +27/-13 (40 lines); hunks: -91,6 +91,7 @@ def forward_absorb_prepare(; -182,25 +183,31 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, _fuse_rope_for_trtllm_mla
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +51/-6; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +27/-13
- 验证与风险: diff 自带测试面 `test/registered/8-gpu-models/test_deepseek_v32_indexcache.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #22914 - [Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel

- 链接: https://github.com/sgl-project/sglang/pull/22914
- 状态/时间: merged / 2026-04-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c304d0d64d30`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+148/-402，可读 patch 783 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +11/-7 (18 lines); hunks: -55,13 +55,9; -112,6 +108,12; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-7 (18 lines); hunks: -55,13 +55,9; -112,6 +108,12; symbols: forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23268 - 【NPU】【bugfix】accuracy fix when enable both nsa cp and prefixcache

- 链接: https://github.com/sgl-project/sglang/pull/23268
- 状态/时间: merged / 2026-04-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；关联提交 `b1e1fe8eee68`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+21/-5，可读 patch 40 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「【NPU】【bugfix】accuracy fix when enable both nsa cp and prefixcache」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「【NPU】【bugfix】accuracy fix when enable both nsa cp and prefixcache」；主要实现面是 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +3/-1 (4 lines); hunks: -359,7 +359,9 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu，涉及 `forward_dsa_prepare_npu`。
- 代码 diff 细节:
  - `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +3/-1 (4 lines); hunks: -359,7 +359,9 @@ def forward_dsa_prepare_npu(; symbols: forward_dsa_prepare_npu
- 关键代码摘录:

```diff
diff -- python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py
@@ -359,7 +359,9 @@ def forward_dsa_prepare_npu(
-            if fused_qkv_a_proj_out.shape[0] < 65535:
+            if fused_qkv_a_proj_out.shape[0] < 65535 and not nsa_use_prefill_cp(
+                forward_batch
+            ):
```

- 已读文件:
  - runtime: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` modified +3/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24392 - add indexer-topk capture (V3.2 NSA + infra)

- 链接: https://github.com/sgl-project/sglang/pull/24392
- 状态/时间: merged / 2026-05-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；关联提交 `47a416fc6272`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 19 个文件，+428/-18，可读 patch 785 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「add indexer-topk capture (V3.2 NSA + infra)」；模型线: DeepSeek V3.2；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「add indexer-topk capture (V3.2 NSA + infra)」；主要实现面是 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +11/-2 (13 lines); hunks: -6,6 +6,9; -205,7 +208,11 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare，涉及 `forward_absorb_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +11/-2 (13 lines); hunks: -6,6 +6,9; -205,7 +208,11 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +11/-2
- 验证与风险: diff 自带测试面 `test/registered/8-gpu-models/test_return_indexer_topk.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #24125 - [AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode

- 链接: https://github.com/sgl-project/sglang/pull/24125
- 状态/时间: merged / 2026-05-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；关联提交 `fc20f5b114f9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+60/-20，可读 patch 110 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode」；模型线: DeepSeek V3.2；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「[AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode」；主要实现面是 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +48/-18 (66 lines); hunks: -415,25 +415,55 @@ def forward_absorb_core(; symbols: forward_absorb_core，涉及 `forward_absorb_core`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +48/-18 (66 lines); hunks: -415,25 +415,55 @@ def forward_absorb_core(; symbols: forward_absorb_core
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +48/-18
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25233 - [Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers

- 链接: https://github.com/sgl-project/sglang/pull/25233
- 状态/时间: merged / 2026-05-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `7cb4669a049a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+115/-3，可读 patch 141 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers」；模型线: DeepSeek V3.2；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +115/-3 (118 lines); hunks: -1,10 +1,11; -14,8 +15,30; symbols: DeepSeekV32Detector, structure_info, get_structural_tag_name, get_structural_tag，涉及 `DeepSeekV32Detector, structure_info, get_structural_tag_name`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv32_detector.py` modified +115/-3 (118 lines); hunks: -1,10 +1,11; -14,8 +15,30; symbols: DeepSeekV32Detector, structure_info, get_structural_tag_name, get_structural_tag
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv32_detector.py` modified +115/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv32_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25821 - [Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename

- 链接: https://github.com/sgl-project/sglang/pull/25821
- 状态/时间: merged / 2026-05-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/utils.py` 等 14 个文件；关联提交 `8131641bc66e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 162 个文件，+11303/-10745，可读 patch 15980 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename」；模型线: DeepSeek V3.2；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename」；主要实现面是 `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/attention/nsa/utils.py` modified +9/-268 (277 lines); hunks: -1,269 +1,10; symbols: aiter_can_use_preshuffle_paged_mqa, compute_nsa_seqlens, is_nsa_enable_prefill_cp, is_nsa_prefill_cp_in_seq_split，涉及 `aiter_can_use_preshuffle_paged_mqa, compute_nsa_seqlens, is_nsa_enable_prefill_cp`；`python/sglang/srt/layers/attention/dsa/utils.py` added +271/-0 (271 lines); hunks: -0,0 +1,271; symbols: aiter_can_use_preshuffle_paged_mqa, compute_dsa_seqlens, is_dsa_enable_prefill_cp, is_dsa_prefill_cp_in_seq_split，涉及 `aiter_can_use_preshuffle_paged_mqa, compute_dsa_seqlens, is_dsa_enable_prefill_cp`；`python/sglang/srt/models/deepseek_v2.py` modified +37/-37 (74 lines); hunks: -40,10 +40,10; -59,19 +59,19; symbols: __init__, forward，涉及 `__init__, forward`；`python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +33/-26 (59 lines); hunks: -6,7 +6,7; -124,7 +124,6 @@ def fused_qk_rmsnorm_bf16(q, q_weight, q_eps, k, k_weight, k...; symbols: fused_qk_rmsnorm_bf16, DeepseekMLAForwardMixin, init_mla_forward, forward_absorb_prepare，涉及 `fused_qk_rmsnorm_bf16, DeepseekMLAForwardMixin, init_mla_forward`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/attention/nsa/utils.py` modified +9/-268 (277 lines); hunks: -1,269 +1,10; symbols: aiter_can_use_preshuffle_paged_mqa, compute_nsa_seqlens, is_nsa_enable_prefill_cp, is_nsa_prefill_cp_in_seq_split
  - `python/sglang/srt/layers/attention/dsa/utils.py` added +271/-0 (271 lines); hunks: -0,0 +1,271; symbols: aiter_can_use_preshuffle_paged_mqa, compute_dsa_seqlens, is_dsa_enable_prefill_cp, is_dsa_prefill_cp_in_seq_split
  - `python/sglang/srt/models/deepseek_v2.py` modified +37/-37 (74 lines); hunks: -40,10 +40,10; -59,19 +59,19; symbols: __init__, forward
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +33/-26 (59 lines); hunks: -6,7 +6,7; -124,7 +124,6 @@ def fused_qk_rmsnorm_bf16(q, q_weight, q_eps, k, k_weight, k...; symbols: fused_qk_rmsnorm_bf16, DeepseekMLAForwardMixin, init_mla_forward, forward_absorb_prepare
  - `python/sglang/srt/layers/utils/cp_utils.py` modified +20/-20 (40 lines); hunks: -66,17 +66,17 @@ def can_cp_split(seq_len: int, cp_size: int, forward_batch):; -88,18 +88,18 @@ def cp_split_and_rebuild_data(forward_batch, input_: torch.T...; symbols: can_cp_split, cp_split_and_rebuild_data, cp_split_and_rebuild_position, cp_all_gather_rerange_output
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/layers/attention/nsa/utils.py` modified +9/-268; `python/sglang/srt/layers/attention/dsa/utils.py` added +271/-0; `python/sglang/srt/models/deepseek_v2.py` modified +37/-37; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +33/-26; `python/sglang/srt/layers/utils/cp_utils.py` modified +20/-20; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +11/-11
- 验证与风险: diff 自带测试面 `python/sglang/jit_kernel/tests/test_fused_metadata_copy.py`, `python/sglang/jit_kernel/tests/test_fused_store_index_cache.py`, `python/sglang/jit_kernel/tests/test_set_mla_kv_buffer.py`, `python/sglang/test/nightly_utils.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #23351 - Support piecewise CUDA graph with NSA

- 链接: https://github.com/sgl-project/sglang/pull/23351
- 状态/时间: merged / 2026-05-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `cadfa2d025d3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+317/-58，可读 patch 682 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support piecewise CUDA graph with NSA」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Support piecewise CUDA graph with NSA」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1980,6 +1980,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -1980,6 +1980,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1980,6 +1980,7 @@ def forward(
+            and not torch.compiler.is_compiling()
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0
- 验证与风险: diff 自带测试面 `test/registered/piecewise_cuda_graph/test_pcg_glm5_fp4.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27705 - Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels

- 链接: https://github.com/sgl-project/sglang/pull/27705
- 状态/时间: merged / 2026-06-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`；关联提交 `073de150530a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 13 个文件，+1196/-69，可读 patch 1573 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`；技术摘要: 覆盖「Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels」；主要实现面是 `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +61/-0 (61 lines); hunks: -76,6 +76,52 @@ def _clone_if_runai_streamed_tensor(tensor: torch.Tensor) ->...; -147,6 +193,8 @@ def do_load_weights(; symbols: _clone_if_runai_streamed_tensor, _load_fused_indexer_wk, NextNEnabledConfig, do_load_weights，涉及 `_clone_if_runai_streamed_tensor, _load_fused_indexer_wk, NextNEnabledConfig`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +61/-0 (61 lines); hunks: -76,6 +76,52 @@ def _clone_if_runai_streamed_tensor(tensor: torch.Tensor) ->...; -147,6 +193,8 @@ def do_load_weights(; symbols: _clone_if_runai_streamed_tensor, _load_fused_indexer_wk, NextNEnabledConfig, do_load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +61/-0
- 验证与风险: diff 自带测试面 `test/registered/8-gpu-models/test_deepseek_v32_indexcache.py`, `test/registered/jit/test_dsv32_indexer_fusion.py`, `test/registered/models_e2e/test_dsa_glm5_dp_mtp.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31888 - [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations

- 链接: https://github.com/sgl-project/sglang/pull/31888
- 状态/时间: merged / 2026-07-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e4a40a71f84c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 30 个文件，+3837/-52，可读 patch 4635 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations」；模型线: DeepSeek V3.2；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +180/-18 (198 lines); hunks: -241,6 +241,9; -307,6 +310,7 @@ def forward(; symbols: forward, __init__, get_moe_weights, forward_normal_dual_stream，涉及 `forward, __init__, get_moe_weights`；`python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +174/-0 (174 lines); hunks: -6,6 +6,7; -52,6 +53,7; symbols: _make_mla_bmm_fusion_plan, _q8kv8_born_fp8_q_backend, forward_absorb_prepare，涉及 `_make_mla_bmm_fusion_plan, _q8kv8_born_fp8_q_backend, forward_absorb_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +180/-18 (198 lines); hunks: -241,6 +241,9; -307,6 +310,7 @@ def forward(; symbols: forward, __init__, get_moe_weights, forward_normal_dual_stream
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +174/-0 (174 lines); hunks: -6,6 +6,7; -52,6 +53,7; symbols: _make_mla_bmm_fusion_plan, _q8kv8_born_fp8_q_backend, forward_absorb_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +180/-18; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +174/-0
- 验证与风险: diff 自带测试面 `test/manual/test_moe_quant_once.py`, `test/registered/kernels/ops/attention/test_qprep_bf16_fp8_sm90.py`, `test/registered/kernels/ops/attention/test_sparse_mla_q8kv8_prefill_sm90.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
