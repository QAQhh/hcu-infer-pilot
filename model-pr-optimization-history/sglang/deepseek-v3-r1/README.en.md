# sglang DeepSeek V3/R1 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-R1.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_1.mdx` | no direct PR-number commit |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx` | no direct PR-number commit |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/deepseek_r1.mdx` | no direct PR-number commit |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/deepseek_r1.mdx` | no direct PR-number commit |
| `docs/docs/references/multi_node_deployment/rbg_pd/deepseekv32_pd.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/deepseek-r1-advanced-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/deepseek-r1-basic-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/deepseek-v3-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/deepseek-v31-deployment.jsx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/deepseek-v32-deployment.jsx` | no direct PR-number commit |
| `examples/chat_template/tool_chat_template_deepseekv3.jinja` | [#5908](https://github.com/sgl-project/sglang/pull/5908), [#9525](https://github.com/sgl-project/sglang/pull/9525), [#10209](https://github.com/sgl-project/sglang/pull/10209) |
| `examples/chat_template/tool_chat_template_deepseekv31.jinja` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#9895](https://github.com/sgl-project/sglang/pull/9895), [#14837](https://github.com/sgl-project/sglang/pull/14837) |
| `examples/chat_template/tool_chat_template_deepseekv32.jinja` | [#11063](https://github.com/sgl-project/sglang/pull/11063) |
| `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` | no direct PR-number commit |
| `python/sglang/srt/function_call/deepseekv31_detector.py` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#11589](https://github.com/sgl-project/sglang/pull/11589), [#13394](https://github.com/sgl-project/sglang/pull/13394) |
| `python/sglang/srt/function_call/deepseekv32_detector.py` | [#14573](https://github.com/sgl-project/sglang/pull/14573), [#14750](https://github.com/sgl-project/sglang/pull/14750), [#15278](https://github.com/sgl-project/sglang/pull/15278), [#16091](https://github.com/sgl-project/sglang/pull/16091), [#18174](https://github.com/sgl-project/sglang/pull/18174), [#25233](https://github.com/sgl-project/sglang/pull/25233) |
| `python/sglang/srt/function_call/deepseekv3_detector.py` | [#6655](https://github.com/sgl-project/sglang/pull/6655), [#7562](https://github.com/sgl-project/sglang/pull/7562), [#9525](https://github.com/sgl-project/sglang/pull/9525) |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | [#13959](https://github.com/sgl-project/sglang/pull/13959), [#14541](https://github.com/sgl-project/sglang/pull/14541), [#14572](https://github.com/sgl-project/sglang/pull/14572), [#15381](https://github.com/sgl-project/sglang/pull/15381), [#17007](https://github.com/sgl-project/sglang/pull/17007), [#19428](https://github.com/sgl-project/sglang/pull/19428) |
| `python/sglang/srt/models/deepseek_common/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/a8w8_blockscale_bpreshuffle_tuned_gemm.csv` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=2048-K=7168.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=7168-K=2048.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=8192-K=1536.json` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_tune.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_act.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_moe.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | [#22774](https://github.com/sgl-project/sglang/pull/22774) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | [#21405](https://github.com/sgl-project/sglang/pull/21405), [#22774](https://github.com/sgl-project/sglang/pull/22774), [#31619](https://github.com/sgl-project/sglang/pull/31619), [#31888](https://github.com/sgl-project/sglang/pull/31888) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | [#37762](https://github.com/sgl-project/sglang/pull/37762) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/triton_qk_rmsnorm.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | [#18461](https://github.com/sgl-project/sglang/pull/18461), [#22774](https://github.com/sgl-project/sglang/pull/22774) |
| `python/sglang/srt/models/deepseek_common/moe_transport.py` | no direct PR-number commit |
| `python/sglang/srt/models/deepseek_common/utils.py` | [#18461](https://github.com/sgl-project/sglang/pull/18461), [#22774](https://github.com/sgl-project/sglang/pull/22774), [#34693](https://github.com/sgl-project/sglang/pull/34693) |
| `python/sglang/srt/models/deepseek_v2.py` | [#2667](https://github.com/sgl-project/sglang/pull/2667), [#3237](https://github.com/sgl-project/sglang/pull/3237), [#3550](https://github.com/sgl-project/sglang/pull/3550), [#3582](https://github.com/sgl-project/sglang/pull/3582), [#3730](https://github.com/sgl-project/sglang/pull/3730), [#3785](https://github.com/sgl-project/sglang/pull/3785), [#3888](https://github.com/sgl-project/sglang/pull/3888), [#4836](https://github.com/sgl-project/sglang/pull/4836), [#4918](https://github.com/sgl-project/sglang/pull/4918), [#5571](https://github.com/sgl-project/sglang/pull/5571), [#5662](https://github.com/sgl-project/sglang/pull/5662), [#5707](https://github.com/sgl-project/sglang/pull/5707), ... (84 total) |
| `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` | [#17523](https://github.com/sgl-project/sglang/pull/17523) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_ar_fusion_eval_mi35x.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_kv_fp8_eval_mi35x.py` | no direct PR-number commit |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` | [#27188](https://github.com/sgl-project/sglang/pull/27188), [#27243](https://github.com/sgl-project/sglang/pull/27243) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` | [#27188](https://github.com/sgl-project/sglang/pull/27188), [#27243](https://github.com/sgl-project/sglang/pull/27243) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` | [#29290](https://github.com/sgl-project/sglang/pull/29290) |
| `test/registered/amd/accuracy/mi45x/test_deepseek_r1_0528_mxfp4_eval_mi45x.py` | no direct PR-number commit |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_ar_fusion_perf_mi35x.py` | no direct PR-number commit |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_kv_fp8_perf_mi35x.py` | no direct PR-number commit |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179) |
| `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` | [#26395](https://github.com/sgl-project/sglang/pull/26395) |
| `test/registered/unit/function_call/test_deepseekv32_detector.py` | no direct PR-number commit |
| `test/registered/unit/model_executor/test_compensated_mhc_update_guard.py` | no direct PR-number commit |
| `test/registered/xpu/llm_models/test_xpu_deepseek_v2_lite_chat_fp8_gsm8k_eval.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 110
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 110
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2024-12-30 | [#2667](https://github.com/sgl-project/sglang/pull/2667) | merged | AMD DeepSeek_V3 FP8 Numerical fix | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-02-14 | [#3550](https://github.com/sgl-project/sglang/pull/3550) | merged | feat: support flashinfer mla attention for deepseek v3 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-02-14 | [#3582](https://github.com/sgl-project/sglang/pull/3582) | merged | Support NextN (MTP) speculative decoding for DeepSeek-V3/R1 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-02-24 | [#3785](https://github.com/sgl-project/sglang/pull/3785) | merged | Refactor flashinfer logic for deepseek v3 and fix accuracy bug | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-02-24 | [#3730](https://github.com/sgl-project/sglang/pull/3730) | merged | Feature DeepSeek V3/R1 INT8 Quantization (block-wise) | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-02-25 | [#3237](https://github.com/sgl-project/sglang/pull/3237) | merged | [ROCm] Enable Fused MLA Triton kernel for DeepSeekV3 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-03-07 | [#3888](https://github.com/sgl-project/sglang/pull/3888) | merged | [Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise) | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-04-04 | [#4918](https://github.com/sgl-project/sglang/pull/4918) | merged | Add DeepSeek V3/R1 shared experts fusion | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-04-18 | [#4836](https://github.com/sgl-project/sglang/pull/4836) | merged | Introduce moe_dense_tp_size to fix dense layer errors in DeepSeek V3 + 4x8xH100 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-04-20 | [#5571](https://github.com/sgl-project/sglang/pull/5571) | merged | enable DeepSeek V3 shared_experts_fusion in sm90 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-04-24 | [#5707](https://github.com/sgl-project/sglang/pull/5707) | merged | [BugFix] Fix combination of MTP and `--n-share-experts-fusion`with R1 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-05-02 | [#5908](https://github.com/sgl-project/sglang/pull/5908) | merged | feat: Refactor DeepSeekV3 function call | `examples/chat_template/tool_chat_template_deepseekv3.jinja` |
| 2025-05-08 | [#6079](https://github.com/sgl-project/sglang/pull/6079) | merged | Clean logs for DeepSeek-V3 launching | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-05-08 | [#5662](https://github.com/sgl-project/sglang/pull/5662) | merged | [perf] dsv3 bmm fallback to bf16 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-05-28 | [#6655](https://github.com/sgl-project/sglang/pull/6655) | merged | fix(deepseekv3): Fix DeepSeekV3Detector tool_index assignment and multi-tool call streaming support | `python/sglang/srt/function_call/deepseekv3_detector.py` |
| 2025-05-29 | [#6265](https://github.com/sgl-project/sglang/pull/6265) | merged | [fix][RL] Fix DeepSeekV3ForCausalLM.post_load_weights for multiple update weight | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-06-08 | [#6853](https://github.com/sgl-project/sglang/pull/6853) | merged | [DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-06-14 | [#7181](https://github.com/sgl-project/sglang/pull/7181) | merged | [fix] fix dsv3 weight loader tqdm and simplify shared experts fusion | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-06-17 | [#7164](https://github.com/sgl-project/sglang/pull/7164) | merged | Fix Deepseek R1 0528 FP4 tensor name mismatch issue during weights loading. | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-06-17 | [#7286](https://github.com/sgl-project/sglang/pull/7286) | merged | fix: resolve b200 dsv3 mtp issue | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-06-20 | [#7371](https://github.com/sgl-project/sglang/pull/7371) | merged | Fix judgment condition for enabling Deepseek V3/R1 shared expert fusion optimization | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-06-23 | [#7481](https://github.com/sgl-project/sglang/pull/7481) | merged | [perf] slightly imporve DeepSeek-R1-FP4 TP8 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-06-24 | [#7376](https://github.com/sgl-project/sglang/pull/7376) | merged | Fix MTP with Deepseek R1 Fp4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-02 | [#7635](https://github.com/sgl-project/sglang/pull/7635) | merged | Apply dsv3_fused_a_gemm kernel | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-02 | [#7677](https://github.com/sgl-project/sglang/pull/7677) | merged | Apply dsv3 router gemm kernel for deepseek-r1 fp4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-03 | [#7735](https://github.com/sgl-project/sglang/pull/7735) | merged | fix awq and dsv3 fused gemm compatible | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-03 | [#7738](https://github.com/sgl-project/sglang/pull/7738) | merged | fix dsv3 fused proj check | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-03 | [#7750](https://github.com/sgl-project/sglang/pull/7750) | merged | [fix] fix dsv3_router_gemm filter | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-06 | [#7793](https://github.com/sgl-project/sglang/pull/7793) | merged | fix: disable dsv3_router_gemm in dsv3_nextn | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-07 | [#7762](https://github.com/sgl-project/sglang/pull/7762) | merged | feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-07-24 | [#7562](https://github.com/sgl-project/sglang/pull/7562) | merged | Fix incomplete tool call capture issue in streaming response of DeepSeek-V3 when enable MTP | `python/sglang/srt/function_call/deepseekv3_detector.py` |
| 2025-08-01 | [#8051](https://github.com/sgl-project/sglang/pull/8051) | merged | Update batch size limitation of dsv3_router_gemm kernel to 16 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-08-23 | [#9525](https://github.com/sgl-project/sglang/pull/9525) | merged | tool-call(dsv3): Improve deepseek-v3 chat template and tool_choice = `required` | `python/sglang/srt/function_call/deepseekv3_detector.py`, `examples/chat_template/tool_chat_template_deepseekv3.jinja` |
| 2025-08-27 | [#9446](https://github.com/sgl-project/sglang/pull/9446) | merged | Support DeepSeek-V3.1 tool call | `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-08-30 | [#9815](https://github.com/sgl-project/sglang/pull/9815) | merged | fix: dsv3 lite q_lora_rank none | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-02 | [#8118](https://github.com/sgl-project/sglang/pull/8118) | merged | [feat] Support tp mode for DeepSeek-R1-W4AFP8 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-03 | [#9895](https://github.com/sgl-project/sglang/pull/9895) | merged | Update tool_chat_template_deepseekv31.jinja | `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-09-03 | [#9671](https://github.com/sgl-project/sglang/pull/9671) | merged | Optimized deepseek-v3/r1 model performance on mxfp4 run | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-03 | [#9959](https://github.com/sgl-project/sglang/pull/9959) | merged | Revert "Optimized deepseek-v3/r1 model performance on mxfp4 run (#9671)" | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-04 | [#10008](https://github.com/sgl-project/sglang/pull/10008) | merged | Optimized deepseek-v3/r1 model performance on mxfp4 run | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-04 | [#8677](https://github.com/sgl-project/sglang/pull/8677) | merged | Fix accuracy drop of dsv3 run in dp enablement | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-06 | [#9834](https://github.com/sgl-project/sglang/pull/9834) | merged | perf: Avoid unnecessary data type conversions for DeepSeek-V3 on Blackwell | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-08 | [#10104](https://github.com/sgl-project/sglang/pull/10104) | merged | Fix run time error in dsv3-fp8 model on mi35x | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-09-09 | [#10209](https://github.com/sgl-project/sglang/pull/10209) | merged | tool-call(dsv3): Fixed a parse problem when there are multiple function definitions in tool_calls | `examples/chat_template/tool_chat_template_deepseekv3.jinja` |
| 2025-10-05 | [#11063](https://github.com/sgl-project/sglang/pull/11063) | merged | Add DeepSeek-V3.2 Tool Call Template | `examples/chat_template/tool_chat_template_deepseekv32.jinja` |
| 2025-10-06 | [#11061](https://github.com/sgl-project/sglang/pull/11061) | merged | Support DeepSeek V3.2 Exp | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-10-16 | [#11510](https://github.com/sgl-project/sglang/pull/11510) | merged | [Bugfix] Fix Qwen3/DSV3/DSV3.2 model support | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-10-29 | [#12095](https://github.com/sgl-project/sglang/pull/12095) | merged | [2/2] Deepseek deterministic: support deepseek v3 deterministic inference on 8 x H200 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-10-30 | [#12094](https://github.com/sgl-project/sglang/pull/12094) | merged | Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-06 | [#11892](https://github.com/sgl-project/sglang/pull/11892) | merged | DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-07 | [#12788](https://github.com/sgl-project/sglang/pull/12788) | merged | [DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100) | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-07 | [#12816](https://github.com/sgl-project/sglang/pull/12816) | merged | [Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-11 | [#12689](https://github.com/sgl-project/sglang/pull/12689) | merged | [ROCM] Optimized deepseek-r1 model with rmsnorm + fp8 quant fusion | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-14 | [#11589](https://github.com/sgl-project/sglang/pull/11589) | merged | [Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector | `python/sglang/srt/function_call/deepseekv31_detector.py` |
| 2025-11-17 | [#12065](https://github.com/sgl-project/sglang/pull/12065) | merged | (1/n)support context parallel with deepseekv3.2-DSA | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-18 | [#13264](https://github.com/sgl-project/sglang/pull/13264) | merged | [NVIDIA] Fix broken fp8 MoE of deepseek v3 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-20 | [#13617](https://github.com/sgl-project/sglang/pull/13617) | merged | [ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-20 | [#12964](https://github.com/sgl-project/sglang/pull/12964) | merged | [DeepseekV3.2] Deepseek fp8 support for MHA path | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-20 | [#13459](https://github.com/sgl-project/sglang/pull/13459) | merged | [Deepseek V3.2] Change indexer weights_proj to fp32 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-21 | [#13705](https://github.com/sgl-project/sglang/pull/13705) | merged | [AMD] Enable fused shared expert append and flatten quant for fp8 deepseekR1 model | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-25 | [#13544](https://github.com/sgl-project/sglang/pull/13544) | merged | [DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-11-26 | [#13954](https://github.com/sgl-project/sglang/pull/13954) | merged | Fix Deepseek v3.1 loading issue | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-06 | [#13115](https://github.com/sgl-project/sglang/pull/13115) | merged | support mtp with deepseek r1 nvfp4 model | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-08 | [#14573](https://github.com/sgl-project/sglang/pull/14573) | merged | [Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2025-12-10 | [#14837](https://github.com/sgl-project/sglang/pull/14837) | merged | [Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210) | `examples/chat_template/tool_chat_template_deepseekv31.jinja` |
| 2025-12-11 | [#14541](https://github.com/sgl-project/sglang/pull/14541) | merged | [NPU]dsv3.2 cp for npu | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2025-12-12 | [#14572](https://github.com/sgl-project/sglang/pull/14572) | merged | [NPU] optimization for dsv3.2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2025-12-16 | [#14975](https://github.com/sgl-project/sglang/pull/14975) | merged | [AMD] Support fused_rms_mxfp4_quant in the prefill stage for DeepSeek-R1-MXFP4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-18 | [#15278](https://github.com/sgl-project/sglang/pull/15278) | merged | feat: DeepSeek-V3.2 Streaming tool call output | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2025-12-21 | [#15531](https://github.com/sgl-project/sglang/pull/15531) | merged | Support piecewise cuda graph for dsv3 fp4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-26 | [#14750](https://github.com/sgl-project/sglang/pull/14750) | merged | [Tool Call][DSV32] Streamline function call parameters | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2025-12-29 | [#14280](https://github.com/sgl-project/sglang/pull/14280) | merged | feat PD: add eagle3 support for DeepSeek V3 in EP mode | `python/sglang/srt/models/deepseek_v2.py` |
| 2025-12-31 | [#13394](https://github.com/sgl-project/sglang/pull/13394) | merged | Fix DeepSeekV31's structural tag trigger | `python/sglang/srt/function_call/deepseekv31_detector.py` |
| 2026-01-02 | [#13959](https://github.com/sgl-project/sglang/pull/13959) | merged | [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-01-10 | [#16637](https://github.com/sgl-project/sglang/pull/16637) | merged | [DSv32] Overlap indexer weights_proj during dual_stream decode | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-20 | [#17179](https://github.com/sgl-project/sglang/pull/17179) | merged | [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests | `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` |
| 2026-01-23 | [#17007](https://github.com/sgl-project/sglang/pull/17007) | merged | [NPU]bugfix: fix for dsv3.2 and dsvl2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-01-26 | [#15381](https://github.com/sgl-project/sglang/pull/15381) | merged | [NPU]DeepSeek-V3.2 support npu mlaprolog | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-01-28 | [#17523](https://github.com/sgl-project/sglang/pull/17523) | merged | [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI | `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` |
| 2026-02-10 | [#18297](https://github.com/sgl-project/sglang/pull/18297) | merged | Deepseekv32 compatibility with transformers v5 | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-15 | [#16907](https://github.com/sgl-project/sglang/pull/16907) | merged | Fix model loading for DeepSeek-V3.2-AWQ | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-16 | [#18389](https://github.com/sgl-project/sglang/pull/18389) | merged | Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-24 | [#18624](https://github.com/sgl-project/sglang/pull/18624) | merged | [AMD] DSR1/V3 use fp8 bmm in MLA for MI300X | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-25 | [#18242](https://github.com/sgl-project/sglang/pull/18242) | merged | [ROCm] Optimize Deepseek R1 on MI300X | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-02 | [#19428](https://github.com/sgl-project/sglang/pull/19428) | merged | [Feature] add feature mla_ag_after_qlora for dsv3.2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-03-03 | [#18174](https://github.com/sgl-project/sglang/pull/18174) | merged | [Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-03-03 | [#16091](https://github.com/sgl-project/sglang/pull/16091) | merged | [Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format. | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-03-06 | [#19843](https://github.com/sgl-project/sglang/pull/19843) | merged | [AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3 | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-19 | [#18451](https://github.com/sgl-project/sglang/pull/18451) | merged | [AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256. | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-30 | [#18461](https://github.com/sgl-project/sglang/pull/18461) | merged | [Intel GPU] Enable DeepSeek R1 inference on XPU | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-04-04 | [#17707](https://github.com/sgl-project/sglang/pull/17707) | merged | Add dsv3 router gemm benchmark on blackwell | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-04-05 | [#21405](https://github.com/sgl-project/sglang/pull/21405) | merged | Enable IndexCache for DeepSeek V3.2 | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |
| 2026-04-24 | [#22774](https://github.com/sgl-project/sglang/pull/22774) | merged | [MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1) | `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-05-15 | [#25233](https://github.com/sgl-project/sglang/pull/25233) | merged | [Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-05-22 | [#25189](https://github.com/sgl-project/sglang/pull/25189) | merged | [perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-05-23 | [#25898](https://github.com/sgl-project/sglang/pull/25898) | merged | [AMD] Dsv4/pr1 fix run time issue | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-05-27 | [#26395](https://github.com/sgl-project/sglang/pull/26395) | merged | [AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x | `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` |
| 2026-06-03 | [#27188](https://github.com/sgl-project/sglang/pull/27188) | merged | [AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage | `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` |
| 2026-06-13 | [#27720](https://github.com/sgl-project/sglang/pull/27720) | merged | [DeepSeek V3] Defer moe finalize and fused it with main stream add | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-06-22 | [#27243](https://github.com/sgl-project/sglang/pull/27243) | merged | [AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests | `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` |
| 2026-06-26 | [#29142](https://github.com/sgl-project/sglang/pull/29142) | merged | [DeepSeek V3] Run routed experts on main stream in dual-stream MoE | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-06-26 | [#21531](https://github.com/sgl-project/sglang/pull/21531) | merged | [JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-06-26 | [#29452](https://github.com/sgl-project/sglang/pull/29452) | merged | Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE" | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-06-29 | [#29463](https://github.com/sgl-project/sglang/pull/29463) | merged | [DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-07-01 | [#29290](https://github.com/sgl-project/sglang/pull/29290) | merged | [AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI | `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` |
| 2026-07-18 | [#31619](https://github.com/sgl-project/sglang/pull/31619) | merged | [CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |
| 2026-07-30 | [#31888](https://github.com/sgl-project/sglang/pull/31888) | merged | [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` |
| 2026-09-01 | [#34693](https://github.com/sgl-project/sglang/pull/34693) | merged | [Kernel] Replace dsv3_router_gemm with the unified tiny GEMM | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/utils.py` |
| 2026-09-15 | [#38176](https://github.com/sgl-project/sglang/pull/38176) | merged | keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-09-21 | [#37762](https://github.com/sgl-project/sglang/pull/37762) | merged | [AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8 | `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` |

## Per-PR Diff Audit Cards

### PR #2667 - AMD DeepSeek_V3 FP8 Numerical fix

- Link: https://github.com/sgl-project/sglang/pull/2667
- Status/date: merged / 2024-12-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `c5210dfa3802`
- Diff scope read: GitHub Pull Request files API returned 1 files, +34/-7, 88 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "AMD DeepSeek_V3 FP8 Numerical fix"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "AMD DeepSeek_V3 FP8 Numerical fix"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +34/-7 (41 lines); hunks: -46,6 +46,7; -55,7 +56,9; symbols: forward_absorb, load_weights, DeepseekV3ForCausalLM, touching `forward_absorb, load_weights, DeepseekV3ForCausalLM`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +34/-7 (41 lines); hunks: -46,6 +46,7; -55,7 +56,9; symbols: forward_absorb, load_weights, DeepseekV3ForCausalLM
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -46,6 +46,7 @@
+    normalize_e4m3fn_to_e4m3fnuz,
@@ -55,7 +56,9 @@
-from sglang.srt.utils import is_flashinfer_available
+from sglang.srt.utils import is_flashinfer_available, is_hip
+is_hip_ = is_hip()
@@ -573,7 +576,13 @@ def forward_absorb(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +34/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #3550 - feat: support flashinfer mla attention for deepseek v3

- Link: https://github.com/sgl-project/sglang/pull/3550
- Status/date: merged / 2025-02-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `70f894b810c0`
- Diff scope read: GitHub Pull Request files API returned 12 files, +296/-132, 737 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: support flashinfer mla attention for deepseek v3"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "feat: support flashinfer mla attention for deepseek v3"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +13/-7 (20 lines); hunks: -510,14 +510,20 @@ def forward(; symbols: forward, forward_normal, touching `forward, forward_normal`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-7 (20 lines); hunks: -510,14 +510,20 @@ def forward(; symbols: forward, forward_normal
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -510,14 +510,20 @@ def forward(
-        # Use normal computation for prefill and use weight absorption for extend/decode
-        if (
-            forward_batch.forward_mode.is_extend()
-            and forward_batch.extend_prefix_lens.sum() == 0
-        ):
-            return self.forward_normal(positions, hidden_states, forward_batch)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-7
- Risk and verification: The diff ships test coverage in `test/srt/test_eagle_infer.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #3582 - Support NextN (MTP) speculative decoding for DeepSeek-V3/R1

- Link: https://github.com/sgl-project/sglang/pull/3582
- Status/date: merged / 2025-02-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `862dd76c7619`
- Diff scope read: GitHub Pull Request files API returned 7 files, +437/-7, 529 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support NextN (MTP) speculative decoding for DeepSeek-V3/R1"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Support NextN (MTP) speculative decoding for DeepSeek-V3/R1"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +4/-1 (5 lines); hunks: -519,6 +519,8 @@ def forward(; -680,6 +682,7 @@ def __init__(; symbols: forward, __init__, touching `forward, __init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +4/-1 (5 lines); hunks: -519,6 +519,8 @@ def forward(; -680,6 +682,7 @@ def __init__(; symbols: forward, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -519,6 +519,8 @@ def forward(
+                and not forward_batch.forward_mode.is_target_verify()
+                and not forward_batch.forward_mode.is_draft_extend()
@@ -680,6 +682,7 @@ def __init__(
+        is_nextn: bool = False,
@@ -731,7 +734,7 @@ def __init__(
-        if (
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +4/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #3785 - Refactor flashinfer logic for deepseek v3 and fix accuracy bug

- Link: https://github.com/sgl-project/sglang/pull/3785
- Status/date: merged / 2025-02-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `b110084654a1`
- Diff scope read: GitHub Pull Request files API returned 4 files, +565/-19, 635 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Refactor flashinfer logic for deepseek v3 and fix accuracy bug"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Refactor flashinfer logic for deepseek v3 and fix accuracy bug"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +19/-17 (36 lines); hunks: -510,25 +510,27 @@ def forward(; symbols: forward, no_absorb, forward_normal, touching `forward, no_absorb, forward_normal`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +19/-17 (36 lines); hunks: -510,25 +510,27 @@ def forward(; symbols: forward, no_absorb, forward_normal
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -510,25 +510,27 @@ def forward(
-        if global_server_args_dict["enable_flashinfer_mla"]:
-            if global_server_args_dict["disable_radix_cache"]:
-                if forward_batch.forward_mode.is_extend():
-                    return self.forward_normal(positions, hidden_states, forward_batch)
-                else:
-                    return self.forward_absorb(positions, hidden_states, forward_batch)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +19/-17
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/model_executor/model_runner.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #3730 - Feature DeepSeek V3/R1 INT8 Quantization (block-wise)

- Link: https://github.com/sgl-project/sglang/pull/3730
- Status/date: merged / 2025-02-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `1a6e97577acb`
- Diff scope read: GitHub Pull Request files API returned 9 files, +1092/-5, 1339 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Feature DeepSeek V3/R1 INT8 Quantization (block-wise)"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Feature DeepSeek V3/R1 INT8 Quantization (block-wise)"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +15/-0 (15 lines); hunks: -47,6 +47,9; -994,6 +997,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +15/-0 (15 lines); hunks: -47,6 +47,9; -994,6 +997,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -47,6 +47,9 @@
+from sglang.srt.layers.quantization.int8_utils import (
+    block_dequant as int8_block_dequant,
+)
@@ -994,6 +997,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+                if (
+                    hasattr(self.quant_config, "weight_block_size")
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +15/-0
- Risk and verification: The diff ships test coverage in `test/srt/run_suite.py`, `test/srt/test_block_int8.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #3237 - [ROCm] Enable Fused MLA Triton kernel for DeepSeekV3

- Link: https://github.com/sgl-project/sglang/pull/3237
- Status/date: merged / 2025-02-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `6ce9dbe82882`
- Diff scope read: GitHub Pull Request files API returned 3 files, +863/-1, 894 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm] Enable Fused MLA Triton kernel for DeepSeekV3"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[ROCm] Enable Fused MLA Triton kernel for DeepSeekV3"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +159/-1 (160 lines); hunks: -16,6 +16,7; -31,6 +32,9; symbols: no_absorb, forward_normal, forward_absorb, forward_absorb_fused_mla_rope, touching `no_absorb, forward_normal, forward_absorb`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +159/-1 (160 lines); hunks: -16,6 +16,7; -31,6 +32,9; symbols: no_absorb, forward_normal, forward_absorb, forward_absorb_fused_mla_rope
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -16,6 +16,7 @@
+import os
@@ -31,6 +32,9 @@
+from sglang.srt.layers.attention.triton_ops.rocm_mla_decode_rope import (
+    decode_attention_fwd_grouped_rope,
+)
@@ -533,7 +537,18 @@ def no_absorb() -> bool:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +159/-1
- Risk and verification: The diff ships test coverage in `test/srt/test_triton_attention_rocm_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #3888 - [Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)

- Link: https://github.com/sgl-project/sglang/pull/3888
- Status/date: merged / 2025-03-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `c7f254468fca`
- Diff scope read: GitHub Pull Request files API returned 5 files, +369/-21, 503 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +16/-12 (28 lines); hunks: -1202,18 +1202,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +16/-12 (28 lines); hunks: -1202,18 +1202,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1202,18 +1202,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-                if (
-                    hasattr(self.quant_config, "weight_block_size")
-                    and w.dtype == torch.int8
-                ):
-                    weight_block_size = self.quant_config.weight_block_size
-                    if weight_block_size is not None:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +16/-12
- Risk and verification: The diff ships test coverage in `test/srt/run_suite.py`, `test/srt/test_int8_kernel.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #4918 - Add DeepSeek V3/R1 shared experts fusion

- Link: https://github.com/sgl-project/sglang/pull/4918
- Status/date: merged / 2025-04-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `924ca7c92c86`
- Diff scope read: GitHub Pull Request files API returned 14 files, +536/-36, 939 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add DeepSeek V3/R1 shared experts fusion"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Add DeepSeek V3/R1 shared experts fusion"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +81/-5 (86 lines); hunks: -16,12 +16,14; -87,6 +89,8; symbols: DeepseekV2MLP, __init__, touching `DeepseekV2MLP, __init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +81/-5 (86 lines); hunks: -16,12 +16,14; -87,6 +89,8; symbols: DeepseekV2MLP, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -16,12 +16,14 @@
+import logging
+from tqdm import tqdm
@@ -87,6 +89,8 @@
+logger = logging.getLogger(__name__)
@@ -168,6 +172,12 @@ def __init__(
+        self.n_share_experts_fusion = (
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +81/-5
- Risk and verification: The diff ships test coverage in `sgl-kernel/tests/test_moe_align.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #4836 - Introduce moe_dense_tp_size to fix dense layer errors in DeepSeek V3 + 4x8xH100

- Link: https://github.com/sgl-project/sglang/pull/4836
- Status/date: merged / 2025-04-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `53dcf3887639`
- Diff scope read: GitHub Pull Request files API returned 4 files, +31/-1, 101 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Introduce moe_dense_tp_size to fix dense layer errors in DeepSeek V3 + 4x8xH100"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Introduce moe_dense_tp_size to fix dense layer errors in DeepSeek V3 + 4x8xH100"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +17/-1 (18 lines); hunks: -1066,12 +1066,18 @@ def __init__(; -1084,6 +1090,10 @@ def __init__(; symbols: __init__, _enable_moe_dense_fully_dp, _compute_info, touching `__init__, _enable_moe_dense_fully_dp, _compute_info`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +17/-1 (18 lines); hunks: -1066,12 +1066,18 @@ def __init__(; -1084,6 +1090,10 @@ def __init__(; symbols: __init__, _enable_moe_dense_fully_dp, _compute_info
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1066,12 +1066,18 @@ def __init__(
+            if self._enable_moe_dense_fully_dp():
+                mlp_tp_rank, mlp_tp_size = 0, 1
+            else:
+                mlp_tp_rank, mlp_tp_size = None, None
+                tp_rank=mlp_tp_rank,
+                tp_size=mlp_tp_size,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +17/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #5571 - enable DeepSeek V3 shared_experts_fusion in sm90

- Link: https://github.com/sgl-project/sglang/pull/5571
- Status/date: merged / 2025-04-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `d9dd529854f7`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-0, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "enable DeepSeek V3 shared_experts_fusion in sm90"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "enable DeepSeek V3 shared_experts_fusion in sm90"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +12/-0 (12 lines); hunks: -1427,6 +1427,18 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-0 (12 lines); hunks: -1427,6 +1427,18 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1427,6 +1427,18 @@ def __init__(
+        elif self.n_share_experts_fusion == 0:
+            if (
+                torch.cuda.get_device_capability("cuda") >= (9, 0)
+                and self.config.architectures[0] == "DeepseekV3ForCausalLM"
+                and self.config.n_routed_experts == 256
+                and (not global_server_args_dict["enable_deepep_moe"])
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #5707 - [BugFix] Fix combination of MTP and `--n-share-experts-fusion`with R1

- Link: https://github.com/sgl-project/sglang/pull/5707
- Status/date: merged / 2025-04-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `5d93a950eeeb`
- Diff scope read: GitHub Pull Request files API returned 2 files, +68/-15, 150 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix] Fix combination of MTP and `--n-share-experts-fusion`with R1"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[BugFix] Fix combination of MTP and `--n-share-experts-fusion`with R1"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +18/-14 (32 lines); hunks: -1431,11 +1431,27 @@ def __init__(; -1450,7 +1466,7 @@ def __init__(; symbols: __init__, determine_n_share_experts_fusion, get_input_embeddings, touching `__init__, determine_n_share_experts_fusion, get_input_embeddings`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +18/-14 (32 lines); hunks: -1431,11 +1431,27 @@ def __init__(; -1450,7 +1466,7 @@ def __init__(; symbols: __init__, determine_n_share_experts_fusion, get_input_embeddings
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1431,11 +1431,27 @@ def __init__(
+        self.determine_n_share_experts_fusion()
+        self.model = DeepseekV2Model(
+            config, quant_config, prefix=add_prefix("model", prefix)
+        )
+        self.lm_head = ParallelLMHead(
+            config.vocab_size,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +18/-14
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #5908 - feat: Refactor DeepSeekV3 function call

- Link: https://github.com/sgl-project/sglang/pull/5908
- Status/date: merged / 2025-05-02
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv3.jinja`; associated commits `170d1f218a4e`
- Diff scope read: GitHub Pull Request files API returned 3 files, +95/-29, 155 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: Refactor DeepSeekV3 function call"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `examples/chat_template/tool_chat_template_deepseekv3.jinja`; technical summary: Covers "feat: Refactor DeepSeekV3 function call"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv3.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/chat_template/tool_chat_template_deepseekv3.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91.
- Code diff details:
  - `examples/chat_template/tool_chat_template_deepseekv3.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- Key code excerpts:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv3.jinja
@@ -0,0 +1,91 @@
+{% if not add_generation_prompt is defined %}
+    {% set add_generation_prompt = false %}
+{% endif %}
+{% set ns = namespace(is_first=false, is_tool=false, is_output_first=true, system_prompt='', is_first_sp=true, is_last_user=false) %}
+{%- for message in messages %}
+    {%- if message['role'] == 'system' %}
```

- Reviewed files:
  - docs: `examples/chat_template/tool_chat_template_deepseekv3.jinja` added +91/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/openai_api/adapter.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #6079 - Clean logs for DeepSeek-V3 launching

- Link: https://github.com/sgl-project/sglang/pull/6079
- Status/date: merged / 2025-05-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `73600673bb1d`
- Diff scope read: GitHub Pull Request files API returned 7 files, +61/-39, 231 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Clean logs for DeepSeek-V3 launching"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Clean logs for DeepSeek-V3 launching"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -88,6 +88,7; -1487,8 +1488,9 @@ def determine_n_share_experts_fusion(; symbols: determine_n_share_experts_fusion, get_input_embeddings, touching `determine_n_share_experts_fusion, get_input_embeddings`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -88,6 +88,7; -1487,8 +1488,9 @@ def determine_n_share_experts_fusion(; symbols: determine_n_share_experts_fusion, get_input_embeddings
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -88,6 +88,7 @@
+    log_info_on_rank0,
@@ -1487,8 +1488,9 @@ def determine_n_share_experts_fusion(
-                logger.info(
-                    "Only Deepseek V3/R1 can use shared experts fusion optimization. Shared experts fusion optimization is disabled."
+                log_info_on_rank0(
+                    logger,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #5662 - [perf] dsv3 bmm fallback to bf16

- Link: https://github.com/sgl-project/sglang/pull/5662
- Status/date: merged / 2025-05-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `5e02330137a1`
- Diff scope read: GitHub Pull Request files API returned 2 files, +48/-3, 76 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[perf] dsv3 bmm fallback to bf16"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[perf] dsv3 bmm fallback to bf16"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +13/-3 (16 lines); hunks: -63,6 +63,7; -1589,13 +1590,22 @@ def post_load_weights(self, is_nextn=False):; symbols: post_load_weights, touching `post_load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-3 (16 lines); hunks: -63,6 +63,7; -1589,13 +1590,22 @@ def post_load_weights(self, is_nextn=False):; symbols: post_load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -63,6 +63,7 @@
+    block_quant_dequant,
@@ -1589,13 +1590,22 @@ def post_load_weights(self, is_nextn=False):
-                            and _ENABLE_JIT_DEEPGEMM
-                            block_scale = weight_scale
-                            use_deep_gemm_bmm = True
+                            if _ENABLE_JIT_DEEPGEMM and get_bool_env_var(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #6655 - fix(deepseekv3): Fix DeepSeekV3Detector tool_index assignment and multi-tool call streaming support

- Link: https://github.com/sgl-project/sglang/pull/6655
- Status/date: merged / 2025-05-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv3_detector.py`; associated commits `461a73028070`
- Diff scope read: GitHub Pull Request files API returned 1 files, +52/-4, 100 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(deepseekv3): Fix DeepSeekV3Detector tool_index assignment and multi-tool call streaming support"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv3_detector.py`; technical summary: Covers "fix(deepseekv3): Fix DeepSeekV3Detector tool_index assignment and multi-tool call streaming support"; the main implementation surface is `python/sglang/srt/function_call/deepseekv3_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +52/-4 (56 lines); hunks: -31,6 +31,7 @@ def __init__(self):; -75,7 +76,12 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment, touching `__init__, has_tool_call, parse_streaming_increment`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv3_detector.py` modified +52/-4 (56 lines); hunks: -31,6 +31,7 @@ def __init__(self):; -75,7 +76,12 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv3_detector.py
@@ -31,6 +31,7 @@ def __init__(self):
+        self.current_tool_id = -1
@@ -75,7 +76,12 @@ def parse_streaming_increment(
-        if self.bot_token not in current_text:
+        # Check if we have a tool call (either the start token or individual tool call)
+        has_tool_call = (
+            self.bot_token in current_text or "<｜tool▁call▁begin｜>" in current_text
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +52/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv3_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #6265 - [fix][RL] Fix DeepSeekV3ForCausalLM.post_load_weights for multiple update weight

- Link: https://github.com/sgl-project/sglang/pull/6265
- Status/date: merged / 2025-05-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `51cdd81f9720`
- Diff scope read: GitHub Pull Request files API returned 2 files, +47/-14, 114 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[fix][RL] Fix DeepSeekV3ForCausalLM.post_load_weights for multiple update weight"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[fix][RL] Fix DeepSeekV3ForCausalLM.post_load_weights for multiple update weight"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +39/-14 (53 lines); hunks: -92,6 +92,7; -1713,14 +1714,23 @@ def forward(; symbols: forward, post_load_weights, touching `forward, post_load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +39/-14 (53 lines); hunks: -92,6 +92,7; -1713,14 +1714,23 @@ def forward(; symbols: forward, post_load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -92,6 +92,7 @@
+    bind_or_assign,
@@ -1713,14 +1714,23 @@ def forward(
-    def post_load_weights(self, is_nextn=False):
+    def post_load_weights(self, is_nextn=False, weight_names=None):
-        layer_ids = (
-            range(self.config.num_hidden_layers)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +39/-14
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #6853 - [DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model

- Link: https://github.com/sgl-project/sglang/pull/6853
- Status/date: merged / 2025-06-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `c2c4f57f6311`
- Diff scope read: GitHub Pull Request files API returned 3 files, +386/-13, 506 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +33/-5 (38 lines); hunks: -1746,7 +1746,7 @@ def determine_num_fused_shared_experts(; -1926,6 +1926,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: determine_num_fused_shared_experts, get_input_embeddings, post_load_weights, load_weights, touching `determine_num_fused_shared_experts, get_input_embeddings, post_load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +33/-5 (38 lines); hunks: -1746,7 +1746,7 @@ def determine_num_fused_shared_experts(; -1926,6 +1926,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: determine_num_fused_shared_experts, get_input_embeddings, post_load_weights, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1746,7 +1746,7 @@ def determine_num_fused_shared_experts(
-                    "Deepseek V3/R1 with fp8 can use shared experts fusion optimization when SM version >=90. Shared experts fusion optimization is enabled.",
+                    "Deepseek V3/R1 with fp8/fp4 can use shared experts fusion optimization when SM version >=90. Shared experts fusion optimization is enabled.",
@@ -1926,6 +1926,7 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
@@ -1982,6 +1983,21 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+                elif self.quant_config.get_name() == "modelopt_fp4":
+                    suffix_list = [
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +33/-5
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7181 - [fix] fix dsv3 weight loader tqdm and simplify shared experts fusion

- Link: https://github.com/sgl-project/sglang/pull/7181
- Status/date: merged / 2025-06-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `ed54bf9d19f1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-96, 131 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[fix] fix dsv3 weight loader tqdm and simplify shared experts fusion"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[fix] fix dsv3 weight loader tqdm and simplify shared experts fusion"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +11/-96 (107 lines); hunks: -1033,7 +1033,7 @@ def forward_absorb_core(; -2008,101 +2008,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: forward_absorb_core, load_weights, touching `forward_absorb_core, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-96 (107 lines); hunks: -1033,7 +1033,7 @@ def forward_absorb_core(; -2008,101 +2008,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: forward_absorb_core, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1033,7 +1033,7 @@ def forward_absorb_core(
-            deep_gemm_grouped_gemm_nt_f8f8bf16_masked(
+            deep_gemm_wrapper.grouped_gemm_nt_f8f8bf16_masked(
@@ -2008,101 +2008,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
-        if self.num_fused_shared_experts > 0:
-            assert self.num_fused_shared_experts == 1
-            weights_list = list(weights)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-96
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7164 - Fix Deepseek R1 0528 FP4 tensor name mismatch issue during weights loading.

- Link: https://github.com/sgl-project/sglang/pull/7164
- Status/date: merged / 2025-06-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `8c16da334e93`
- Diff scope read: GitHub Pull Request files API returned 2 files, +10/-7, 45 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Deepseek R1 0528 FP4 tensor name mismatch issue during weights loading."; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix Deepseek R1 0528 FP4 tensor name mismatch issue during weights loading."; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +5/-6 (11 lines); hunks: -1919,6 +1919,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; -2151,12 +2153,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: post_load_weights, load_weights, touching `post_load_weights, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-6 (11 lines); hunks: -1919,6 +1919,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; -2151,12 +2153,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: post_load_weights, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1919,6 +1919,8 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
+            and hasattr(self.quant_config, "weight_block_size")
+            and self.quant_config.weight_block_size is not None
@@ -2151,12 +2153,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
-                            if any(scale in name for scale in ["k_scale", "v_scale"]):
-                                name = name.replace("_proj", "attn_mqa")
-                            else:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-6
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7286 - fix: resolve b200 dsv3 mtp issue

- Link: https://github.com/sgl-project/sglang/pull/7286
- Status/date: merged / 2025-06-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `4f204db57cf9`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-0, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: resolve b200 dsv3 mtp issue"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "fix: resolve b200 dsv3 mtp issue"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -1932,6 +1932,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights, _weight_requant_ue8m0, touching `post_load_weights, _weight_requant_ue8m0`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -1932,6 +1932,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights, _weight_requant_ue8m0
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1932,6 +1932,8 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
+        if self.config.architectures[0] == "DeepseekV3ForCausalLMNextN":
+            return
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7371 - Fix judgment condition for enabling Deepseek V3/R1 shared expert fusion optimization

- Link: https://github.com/sgl-project/sglang/pull/7371
- Status/date: merged / 2025-06-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `a06912ad8b35`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-3, 24 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix judgment condition for enabling Deepseek V3/R1 shared expert fusion optimization"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix judgment condition for enabling Deepseek V3/R1 shared expert fusion optimization"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -1731,12 +1731,12 @@ def determine_num_fused_shared_experts(; -2040,7 +2040,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights, touching `determine_num_fused_shared_experts, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -1731,12 +1731,12 @@ def determine_num_fused_shared_experts(; -2040,7 +2040,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1731,12 +1731,12 @@ def determine_num_fused_shared_experts(
-            or torch.cuda.get_device_capability("cuda") < (9, 0)
+            or torch.cuda.get_device_capability("cuda") < (8, 0)
-            disable_reason = "Only Deepseek V3/R1 on NV-platform with capability >= 90 can use shared experts fusion optimization."
+            disable_reason = "Only Deepseek V3/R1 on NV-platform with capability >= 80 can use shared experts fusion optimization."
@@ -2040,7 +2040,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
-            logger.info("Shared experts fusion optimization enabled.")
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7481 - [perf] slightly imporve DeepSeek-R1-FP4 TP8

- Link: https://github.com/sgl-project/sglang/pull/7481
- Status/date: merged / 2025-06-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `bdbb8d009ae1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +4/-2, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[perf] slightly imporve DeepSeek-R1-FP4 TP8"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[perf] slightly imporve DeepSeek-R1-FP4 TP8"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +4/-2 (6 lines); hunks: -362,12 +362,14 @@ def forward(; symbols: forward, forward_normal_dual_stream, touching `forward, forward_normal_dual_stream`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +4/-2 (6 lines); hunks: -362,12 +362,14 @@ def forward(; symbols: forward, forward_normal_dual_stream
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -362,12 +362,14 @@ def forward(
+        # router_logits: (num_tokens, n_experts)
+        router_logits = self.gate(hidden_states)
-            # router_logits: (num_tokens, n_experts)
-            router_logits = self.gate(hidden_states)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +4/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7376 - Fix MTP with Deepseek R1 Fp4

- Link: https://github.com/sgl-project/sglang/pull/7376
- Status/date: merged / 2025-06-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `15f34013432f`
- Diff scope read: GitHub Pull Request files API returned 3 files, +20/-1, 49 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix MTP with Deepseek R1 Fp4"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix MTP with Deepseek R1 Fp4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -2201,7 +2201,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -2232,6 +2232,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -2201,7 +2201,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -2232,6 +2232,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -2201,7 +2201,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
-                            if (
+                            if self.quant_config is not None and (
@@ -2232,6 +2232,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+                                    break
+                        if name not in params_dict:
+                            # modelopt ckpt contains not needed weights for MTP module:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7635 - Apply dsv3_fused_a_gemm kernel

- Link: https://github.com/sgl-project/sglang/pull/7635
- Status/date: merged / 2025-07-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `00aec6ad6c34`
- Diff scope read: GitHub Pull Request files API returned 1 files, +18/-2, 48 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Apply dsv3_fused_a_gemm kernel"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Apply dsv3_fused_a_gemm kernel"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +18/-2 (20 lines); hunks: -96,6 +96,7; -112,7 +113,7; symbols: __init__, forward_absorb_prepare, touching `__init__, forward_absorb_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +18/-2 (20 lines); hunks: -96,6 +96,7; -112,7 +113,7; symbols: __init__, forward_absorb_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -96,6 +96,7 @@
+    get_device_sm,
@@ -112,7 +113,7 @@
-    from sgl_kernel import awq_dequantize, bmm_fp8, merge_state_v2
+    from sgl_kernel import awq_dequantize, bmm_fp8, dsv3_fused_a_gemm, merge_state_v2
@@ -875,6 +876,15 @@ def __init__(
+        self.use_min_latency_fused_a_gemm = (
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +18/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7677 - Apply dsv3 router gemm kernel for deepseek-r1 fp4

- Link: https://github.com/sgl-project/sglang/pull/7677
- Status/date: merged / 2025-07-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `88f484ce4c73`
- Diff scope read: GitHub Pull Request files API returned 1 files, +21/-3, 47 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Apply dsv3 router gemm kernel for deepseek-r1 fp4"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Apply dsv3 router gemm kernel for deepseek-r1 fp4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +21/-3 (24 lines); hunks: -111,9 +111,16; -225,7 +232,18 @@ def forward(self, hidden_states):; symbols: forward, __init__, touching `forward, __init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +21/-3 (24 lines); hunks: -111,9 +111,16; -225,7 +232,18 @@ def forward(self, hidden_states):; symbols: forward, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -111,9 +111,16 @@
+_device_sm = get_device_sm()
-    from sgl_kernel import awq_dequantize, bmm_fp8, dsv3_fused_a_gemm, merge_state_v2
+    from sgl_kernel import (
+        awq_dequantize,
+        bmm_fp8,
+        dsv3_fused_a_gemm,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +21/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7735 - fix awq and dsv3 fused gemm compatible

- Link: https://github.com/sgl-project/sglang/pull/7735
- Status/date: merged / 2025-07-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `84f2e4a0f847`
- Diff scope read: GitHub Pull Request files API returned 1 files, +15/-2, 47 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix awq and dsv3 fused gemm compatible"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "fix awq and dsv3 fused gemm compatible"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +15/-2 (17 lines); hunks: -318,11 +318,17 @@ def __init__(; -876,8 +882,13 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +15/-2 (17 lines); hunks: -318,11 +318,17 @@ def __init__(; -876,8 +882,13 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -318,11 +318,17 @@ def __init__(
+            is_packed_weight = (
+                self.shared_experts.gate_up_proj.quant_method.quant_config.get_name()
+                in ["awq", "moe_wna16"]
+            )
-                self.shared_experts.gate_up_proj.weight.dtype == torch.int8
+                not is_packed_weight
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +15/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7738 - fix dsv3 fused proj check

- Link: https://github.com/sgl-project/sglang/pull/7738
- Status/date: merged / 2025-07-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `b58226510f7d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +15/-14, 61 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix dsv3 fused proj check"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "fix dsv3 fused proj check"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +15/-14 (29 lines); hunks: -336,10 +336,12 @@ def __init__(; -891,21 +893,20 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +15/-14 (29 lines); hunks: -336,10 +336,12 @@ def __init__(; -891,21 +893,20 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -336,10 +336,12 @@ def __init__(
-            is_packed_weight = (
-                self.shared_experts.gate_up_proj.quant_method.quant_config.get_name()
-                in ["awq", "moe_wna16"]
-            )
+            is_packed_weight = hasattr(
+                self.shared_experts.gate_up_proj.quant_method, "quant_config"
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +15/-14
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7750 - [fix] fix dsv3_router_gemm filter

- Link: https://github.com/sgl-project/sglang/pull/7750
- Status/date: merged / 2025-07-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `ac49dac00946`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[fix] fix dsv3_router_gemm filter"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[fix] fix dsv3_router_gemm filter"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -233,7 +233,8 @@ def forward(self, hidden_states):; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -233,7 +233,8 @@ def forward(self, hidden_states):; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -233,7 +233,8 @@ def forward(self, hidden_states):
-            hidden_states.shape[0] < 4
+            _is_cuda
+            and hidden_states.shape[0] < 4
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7793 - fix: disable dsv3_router_gemm in dsv3_nextn

- Link: https://github.com/sgl-project/sglang/pull/7793
- Status/date: merged / 2025-07-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `54411f6afa27`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-1, 49 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: disable dsv3_router_gemm in dsv3_nextn"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "fix: disable dsv3_router_gemm in dsv3_nextn"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +9/-1 (10 lines); hunks: -210,8 +210,10 @@ def __init__(; -233,8 +235,10 @@ def forward(self, hidden_states):; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +9/-1 (10 lines); hunks: -210,8 +210,10 @@ def __init__(; -233,8 +235,10 @@ def forward(self, hidden_states):; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -210,8 +210,10 @@ def __init__(
+        is_nextn: bool = False,
+        self.is_nextn = is_nextn
@@ -233,8 +235,10 @@ def forward(self, hidden_states):
+        # NOTE: For some unknown reason, router_gemm seems degrade accept length.
+            and not self.is_nextn
@@ -258,6 +262,7 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +9/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #7762 - feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode

- Link: https://github.com/sgl-project/sglang/pull/7762
- Status/date: merged / 2025-07-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `cb9d91ea8a71`
- Diff scope read: GitHub Pull Request files API returned 10 files, +1006/-9, 1203 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -2363,6 +2363,12 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -2363,6 +2363,12 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -2363,6 +2363,12 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+        if self.quant_config and self.quant_config.get_name() == "w4afp8":
+            expert_params_mapping += (
+                get_moe_impl_class().make_expert_input_scale_params_mapping(
+                    num_experts=self.config.n_routed_experts
+                )
+            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/test_cutlass_w4a8_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #7562 - Fix incomplete tool call capture issue in streaming response of DeepSeek-V3 when enable MTP

- Link: https://github.com/sgl-project/sglang/pull/7562
- Status/date: merged / 2025-07-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv3_detector.py`; associated commits `624a3b8d1f10`
- Diff scope read: GitHub Pull Request files API returned 2 files, +90/-1, 104 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix incomplete tool call capture issue in streaming response of DeepSeek-V3 when enable MTP"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv3_detector.py`; technical summary: Covers "Fix incomplete tool call capture issue in streaming response of DeepSeek-V3 when enable MTP"; the main implementation surface is `python/sglang/srt/function_call/deepseekv3_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -98,7 +98,7 @@ def parse_streaming_increment(; symbols: parse_streaming_increment, touching `parse_streaming_increment`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -98,7 +98,7 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv3_detector.py
@@ -98,7 +98,7 @@ def parse_streaming_increment(
-                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*)\n'''json\n(.*)",
+                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*)\n'''json\n(.*)\n'''.*",
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `test/srt/test_function_call_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #8051 - Update batch size limitation of dsv3_router_gemm kernel to 16

- Link: https://github.com/sgl-project/sglang/pull/8051
- Status/date: merged / 2025-08-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `e7e5a3050a64`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-2, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Update batch size limitation of dsv3_router_gemm kernel to 16"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Update batch size limitation of dsv3_router_gemm kernel to 16"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +1/-2 (3 lines); hunks: -248,8 +248,7 @@ def forward(self, hidden_states):; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-2 (3 lines); hunks: -248,8 +248,7 @@ def forward(self, hidden_states):; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -248,8 +248,7 @@ def forward(self, hidden_states):
-            and not self.is_nextn
-            and hidden_states.shape[0] < 4
+            and hidden_states.shape[0] <= 16
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9525 - tool-call(dsv3): Improve deepseek-v3 chat template and tool_choice = `required`

- Link: https://github.com/sgl-project/sglang/pull/9525
- Status/date: merged / 2025-08-23
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv3.jinja`, `python/sglang/srt/function_call/deepseekv3_detector.py`; associated commits `c9dd70fbde92`
- Diff scope read: GitHub Pull Request files API returned 2 files, +17/-17, 98 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "tool-call(dsv3): Improve deepseek-v3 chat template and tool_choice = `required`"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv3_detector.py`, `examples/chat_template/tool_chat_template_deepseekv3.jinja`; technical summary: Covers "tool-call(dsv3): Improve deepseek-v3 chat template and tool_choice = `required`"; the main implementation surface is `python/sglang/srt/function_call/deepseekv3_detector.py`, `examples/chat_template/tool_chat_template_deepseekv3.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -215,6 +215,6 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf, touching `build_ebnf`; `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +16/-16 (32 lines); hunks: -12,7 +12,7; -23,13 +23,13.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -215,6 +215,6 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf
  - `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +16/-16 (32 lines); hunks: -12,7 +12,7; -23,13 +23,13
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv3_detector.py
@@ -215,6 +215,6 @@ def build_ebnf(self, tools: List[Tool]):
-            call_rule_fmt='"<｜tool▁call▁begin｜>function<｜tool▁sep｜>{name}\\n'''json\\n" {arguments_rule} "\\n'''<｜tool▁call▁end｜>"',
+            call_rule_fmt='"<｜tool▁call▁begin｜>function<｜tool▁sep｜>{name}\\n'''json\\n"{arguments_rule}"\\n'''<｜tool▁call▁end｜>"',
diff -- examples/chat_template/tool_chat_template_deepseekv3.jinja
@@ -12,7 +12,7 @@
-{%- endfor %}
+{%- endfor -%}
@@ -23,13 +23,13 @@
-        {% set tool_ns.text = tool_ns.text + '- `' + tool['name'] + '`:\n'''json\n' + (tool | tojson) + '\n'''\n' %}
+        {% set tool_ns.text = tool_ns.text + '\n'''json\n' + (tool | tojson) + '\n'''\n' %}
-{{ bos_token }}
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1
  - docs: `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +16/-16
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv3_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9446 - Support DeepSeek-V3.1 tool call

- Link: https://github.com/sgl-project/sglang/pull/9446
- Status/date: merged / 2025-08-27
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv31.jinja`, `python/sglang/srt/function_call/deepseekv31_detector.py`; associated commits `b9683be6538e`
- Diff scope read: GitHub Pull Request files API returned 3 files, +315/-0, 331 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support DeepSeek-V3.1 tool call"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "Support DeepSeek-V3.1 tool call"; the main implementation surface is `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse, touching `DeepSeekV31Detector, __init__, has_tool_call`; `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -0,0 +1,222 @@
+import json
+import logging
+import re
+from typing import List
+from sglang.srt.entrypoints.openai.protocol import Tool
+from sglang.srt.function_call.base_format_detector import BaseFormatDetector
diff -- examples/chat_template/tool_chat_template_deepseekv31.jinja
@@ -0,0 +1,91 @@
+{% if not add_generation_prompt is defined %}
+  {% set add_generation_prompt = false %}
+{% endif %}
+{% if not thinking is defined %}
+  {% set thinking = false %}
+{% endif %}
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv31_detector.py`, `python/sglang/srt/function_call/function_call_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9815 - fix: dsv3 lite q_lora_rank none

- Link: https://github.com/sgl-project/sglang/pull/9815
- Status/date: merged / 2025-08-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `8abe8deae6cd`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-4, 31 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: dsv3 lite q_lora_rank none"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "fix: dsv3 lite q_lora_rank none"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +12/-4 (16 lines); hunks: -2414,18 +2414,26 @@ def _weight_requant_ue8m0(self, is_nextn=False):; symbols: _weight_requant_ue8m0, touching `_weight_requant_ue8m0`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-4 (16 lines); hunks: -2414,18 +2414,26 @@ def _weight_requant_ue8m0(self, is_nextn=False):; symbols: _weight_requant_ue8m0
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -2414,18 +2414,26 @@ def _weight_requant_ue8m0(self, is_nextn=False):
-            for module in [
-                layer.self_attn.fused_qkv_a_proj_with_mqa,
-                layer.self_attn.q_b_proj,
+            module_list = [
-            ]:
+            ]
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #8118 - [feat] Support tp mode for DeepSeek-R1-W4AFP8

- Link: https://github.com/sgl-project/sglang/pull/8118
- Status/date: merged / 2025-09-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `d4a938417d2c`
- Diff scope read: GitHub Pull Request files API returned 11 files, +291/-120, 710 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[feat] Support tp mode for DeepSeek-R1-W4AFP8"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[feat] Support tp mode for DeepSeek-R1-W4AFP8"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -2168,6 +2168,8 @@ def determine_num_fused_shared_experts(; -2471,6 +2473,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights, touching `determine_num_fused_shared_experts, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -2168,6 +2168,8 @@ def determine_num_fused_shared_experts(; -2471,6 +2473,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -2168,6 +2168,8 @@ def determine_num_fused_shared_experts(
+        elif self.quant_config.get_name() == "w4afp8":
+            disable_reason = "Deepseek V3/R1 W4AFP8 model uses different quant method for routed experts and shared experts."
@@ -2471,6 +2473,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]], is_nextn=Fal
+        # Params for special naming rules in mixed-precision models, for example:
+        # model.layers.xx.mlp.experts.xx.w1.input_scale. For details,
+        # see https://huggingface.co/Barrrrry/DeepSeek-R1-W4AFP8/blob/main.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-0
- Risk and verification: The diff ships test coverage in `python/sglang/test/test_cutlass_w4a8_moe.py`, `sgl-kernel/tests/test_cutlass_w4a8_moe_mm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #9895 - Update tool_chat_template_deepseekv31.jinja

- Link: https://github.com/sgl-project/sglang/pull/9895
- Status/date: merged / 2025-09-03
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv31.jinja`; associated commits `cc9a31c66226`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-3, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Update tool_chat_template_deepseekv31.jinja"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "Update tool_chat_template_deepseekv31.jinja"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13.
- Code diff details:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13
- Key code excerpts:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv31.jinja
@@ -43,13 +43,13 @@
-          {{'<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments'] + '<｜tool▁call▁end｜>'}}
+          {{'<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments']|tojson + '<｜tool▁call▁end｜>'}}
-          {{message['content'] + '<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>' + tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments'] + '<｜tool▁call▁end｜>'}}
+          {{message['content'] + '<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>' + tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments']|tojson + '<｜tool▁call▁end｜>'
-        {{'<｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments'] + '<｜tool▁call▁end｜>'}}
+        {{'<｜tool▁call▁begin｜>'+ tool['function']['name'] + '<｜tool▁sep｜>' + tool['function']['arguments']|tojson + '<｜tool▁call▁end｜>'}}
```

- Reviewed files:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3
- Risk and verification: This is mostly docs/examples in `examples/chat_template/tool_chat_template_deepseekv31.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #9671 - Optimized deepseek-v3/r1 model performance on mxfp4 run

- Link: https://github.com/sgl-project/sglang/pull/9671
- Status/date: merged / 2025-09-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `0dfd54d11d06`, `1b2ff4fb7f05`
- Diff scope read: GitHub Pull Request files API returned 7 files, +458/-62, 763 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Optimized deepseek-v3/r1 model performance on mxfp4 run"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Optimized deepseek-v3/r1 model performance on mxfp4 run"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +202/-27 (229 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__, touching `forward, __init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +202/-27 (229 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -112,6 +112,7 @@
+    is_gfx95_supported,
@@ -129,6 +130,22 @@
+_is_gfx95_supported = is_gfx95_supported()
+_use_aiter_gfx95 = _use_aiter and _is_gfx95_supported
+if _use_aiter_gfx95:
+    from sglang.srt.layers.quantization.quark.utils import quark_post_load_weights
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +202/-27
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9959 - Revert "Optimized deepseek-v3/r1 model performance on mxfp4 run (#9671)"

- Link: https://github.com/sgl-project/sglang/pull/9959
- Status/date: merged / 2025-09-03
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `1b2ff4fb7f05`
- Diff scope read: GitHub Pull Request files API returned 7 files, +62/-458, 763 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Revert "Optimized deepseek-v3/r1 model performance on mxfp4 run (#9671)""; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Revert "Optimized deepseek-v3/r1 model performance on mxfp4 run (#9671)""; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +27/-202 (229 lines); hunks: -112,7 +112,6; -130,22 +129,6; symbols: forward, __init__, touching `forward, __init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +27/-202 (229 lines); hunks: -112,7 +112,6; -130,22 +129,6; symbols: forward, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -112,7 +112,6 @@
-    is_gfx95_supported,
@@ -130,22 +129,6 @@
-_is_gfx95_supported = is_gfx95_supported()
-_use_aiter_gfx95 = _use_aiter and _is_gfx95_supported
-if _use_aiter_gfx95:
-    from sglang.srt.layers.quantization.quark.utils import quark_post_load_weights
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +27/-202
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10008 - Optimized deepseek-v3/r1 model performance on mxfp4 run

- Link: https://github.com/sgl-project/sglang/pull/10008
- Status/date: merged / 2025-09-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `e96973742c32`
- Diff scope read: GitHub Pull Request files API returned 8 files, +489/-67, 850 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Optimized deepseek-v3/r1 model performance on mxfp4 run"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Optimized deepseek-v3/r1 model performance on mxfp4 run"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +228/-32 (260 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__, touching `forward, __init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +228/-32 (260 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -112,6 +112,7 @@
+    is_gfx95_supported,
@@ -129,6 +130,22 @@
+_is_gfx95_supported = is_gfx95_supported()
+_use_aiter_gfx95 = _use_aiter and _is_gfx95_supported
+if _use_aiter_gfx95:
+    from sglang.srt.layers.quantization.quark.utils import quark_post_load_weights
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +228/-32
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #8677 - Fix accuracy drop of dsv3 run in dp enablement

- Link: https://github.com/sgl-project/sglang/pull/8677
- Status/date: merged / 2025-09-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `918e3d4c27c3`
- Diff scope read: GitHub Pull Request files API returned 2 files, +100/-69, 210 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix accuracy drop of dsv3 run in dp enablement"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix accuracy drop of dsv3 run in dp enablement"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +7/-1 (8 lines); hunks: -1077,7 +1077,13 @@ def _dispatch_mla_subtype():; symbols: _dispatch_mla_subtype, touching `_dispatch_mla_subtype`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +7/-1 (8 lines); hunks: -1077,7 +1077,13 @@ def _dispatch_mla_subtype():; symbols: _dispatch_mla_subtype
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1077,7 +1077,13 @@ def _dispatch_mla_subtype():
-                return AttnForwardMethod.MHA
+                if is_dp_attention_enabled():
+                    if sum(forward_batch.extend_prefix_lens_cpu) == 0:
+                        return AttnForwardMethod.MHA
+                    else:
+                        return AttnForwardMethod.MLA
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +7/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #9834 - perf: Avoid unnecessary data type conversions for DeepSeek-V3 on Blackwell

- Link: https://github.com/sgl-project/sglang/pull/9834
- Status/date: merged / 2025-09-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `012584ecd539`
- Diff scope read: GitHub Pull Request files API returned 2 files, +13/-4, 52 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "perf: Avoid unnecessary data type conversions for DeepSeek-V3 on Blackwell"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "perf: Avoid unnecessary data type conversions for DeepSeek-V3 on Blackwell"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +11/-3 (14 lines); hunks: -67,7 +67,10; -299,7 +302,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward, __init__, touching `forward, __init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-3 (14 lines); hunks: -67,7 +67,10; -299,7 +302,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -67,7 +67,10 @@
-from sglang.srt.layers.moe.fused_moe_triton.layer import FusedMoE
+from sglang.srt.layers.moe.fused_moe_triton.layer import (
+    FusedMoE,
+    _is_fp4_quantization_enabled,
+)
@@ -299,7 +302,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator: BumpAllocator = Non
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10104 - Fix run time error in dsv3-fp8 model on mi35x

- Link: https://github.com/sgl-project/sglang/pull/10104
- Status/date: merged / 2025-09-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `400d3b97aebc`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix run time error in dsv3-fp8 model on mi35x"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix run time error in dsv3-fp8 model on mi35x"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -249,7 +249,11 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -249,7 +249,11 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -249,7 +249,11 @@ def forward(
-        if gemm_output_zero_allocator != None and x.shape[0] <= 256:
+        if (
+            gemm_output_zero_allocator is not None
+            and x.shape[0] <= 256
+            and self.gate_up_proj.weight.dtype == torch.uint8
+        ):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10209 - tool-call(dsv3): Fixed a parse problem when there are multiple function definitions in tool_calls

- Link: https://github.com/sgl-project/sglang/pull/10209
- Status/date: merged / 2025-09-09
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv3.jinja`; associated commits `2cd94dd07eea`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "tool-call(dsv3): Fixed a parse problem when there are multiple function definitions in tool_calls"; model line: DeepSeek V3/R1; category: bug fix; main diff: `examples/chat_template/tool_chat_template_deepseekv3.jinja`; technical summary: Covers "tool-call(dsv3): Fixed a parse problem when there are multiple function definitions in tool_calls"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv3.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +1/-1 (2 lines); hunks: -55,7 +55,7.
- Code diff details:
  - `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +1/-1 (2 lines); hunks: -55,7 +55,7
- Key code excerpts:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv3.jinja
@@ -55,7 +55,7 @@
-                {{- '\n' + '<｜tool▁call▁begin｜>' + tool['type'] + '<｜tool▁sep｜>' + tool['function']['name'] + '\n' + ''''json' + '\n' + tool['function']['arguments'] + '\n' + ''''
+                {{- '\n' + '<｜tool▁call▁begin｜>' + tool['type'] + '<｜tool▁sep｜>' + tool['function']['name'] + '\n' + ''''json' + '\n' + tool['function']['arguments']|tojson + '\n'
```

- Reviewed files:
  - docs: `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +1/-1
- Risk and verification: This is mostly docs/examples in `examples/chat_template/tool_chat_template_deepseekv3.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #11063 - Add DeepSeek-V3.2 Tool Call Template

- Link: https://github.com/sgl-project/sglang/pull/11063
- Status/date: merged / 2025-10-05
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv32.jinja`; associated commits `85c1f7937781`
- Diff scope read: GitHub Pull Request files API returned 1 files, +100/-0, 101 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add DeepSeek-V3.2 Tool Call Template"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `examples/chat_template/tool_chat_template_deepseekv32.jinja`; technical summary: Covers "Add DeepSeek-V3.2 Tool Call Template"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv32.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "Support DeepSeek V3.2 Exp"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Support DeepSeek V3.2 Exp"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #12095 - [2/2] Deepseek deterministic: support deepseek v3 deterministic inference on 8 x H200

- Link: https://github.com/sgl-project/sglang/pull/12095
- Status/date: merged / 2025-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `e39628fd07b3`
- Diff scope read: GitHub Pull Request files API returned 3 files, +19/-0, 54 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[2/2] Deepseek deterministic: support deepseek v3 deterministic inference on 8 x H200"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[2/2] Deepseek deterministic: support deepseek v3 deterministic inference on 8 x H200"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +3/-0 (3 lines); hunks: -515,6 +515,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-0 (3 lines); hunks: -515,6 +515,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -515,6 +515,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator: BumpAllocator = Non
+        if get_global_server_args().enable_deterministic_inference:
+            return F.linear(hidden_states, self.weight, None)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-0
- Risk and verification: The diff ships test coverage in `test/srt/test_fused_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #12094 - Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4

- Link: https://github.com/sgl-project/sglang/pull/12094
- Status/date: merged / 2025-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `9ff9fa7f95be`
- Diff scope read: GitHub Pull Request files API returned 2 files, +110/-22, 231 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #12689 - [ROCM] Optimized deepseek-r1 model with rmsnorm + fp8 quant fusion

- Link: https://github.com/sgl-project/sglang/pull/12689
- Status/date: merged / 2025-11-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `4a78031a71dd`
- Diff scope read: GitHub Pull Request files API returned 6 files, +331/-22, 474 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCM] Optimized deepseek-r1 model with rmsnorm + fp8 quant fusion"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[ROCM] Optimized deepseek-r1 model with rmsnorm + fp8 quant fusion"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +117/-15 (132 lines); hunks: -153,6 +153,8; -1507,13 +1509,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare, forward_npu_sparse_prepare, touching `forward_normal_prepare, forward_absorb_prepare, forward_npu_sparse_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +117/-15 (132 lines); hunks: -153,6 +153,8; -1507,13 +1509,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare, forward_npu_sparse_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -153,6 +153,8 @@
+    from aiter.ops.triton.fused_fp8_quant import fused_rms_fp8_group_quant
@@ -1507,13 +1509,14 @@ def forward_normal_prepare(
-            q_lora = self.q_a_layernorm(q)
-            q = self.q_b_proj(q_lora)[0].view(
-                -1, self.num_local_heads, self.qk_head_dim
-            )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +117/-15
- Risk and verification: The diff ships test coverage in `test/srt/quant/test_fused_rms_fp8_group_quant.py`, `test/srt/run_suite.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #11589 - [Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector

- Link: https://github.com/sgl-project/sglang/pull/11589
- Status/date: merged / 2025-11-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv31_detector.py`; associated commits `fc5da1e80b78`
- Diff scope read: GitHub Pull Request files API returned 1 files, +4/-9, 34 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv31_detector.py`; technical summary: Covers "[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector"; the main implementation surface is `python/sglang/srt/function_call/deepseekv31_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment, touching `parse_streaming_increment`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -115,13 +115,14 @@ def parse_streaming_increment(
-                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*)<｜tool▁call▁end｜>",
+                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*?)(<｜tool▁call▁end｜>|$)",
+                is_tool_end = partial_match.group(3)
@@ -180,15 +181,9 @@ def parse_streaming_increment(
-                        tool_call_end_pattern = (
-                            r"<｜tool▁call▁begin｜>.*?<｜tool▁call▁end｜>"
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv31_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12065 - (1/n)support context parallel with deepseekv3.2-DSA

- Link: https://github.com/sgl-project/sglang/pull/12065
- Status/date: merged / 2025-11-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `d368c7451a48`
- Diff scope read: GitHub Pull Request files API returned 17 files, +1247/-54, 1729 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "(1/n)support context parallel with deepseekv3.2-DSA"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "(1/n)support context parallel with deepseekv3.2-DSA"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #13264 - [NVIDIA] Fix broken fp8 MoE of deepseek v3

- Link: https://github.com/sgl-project/sglang/pull/13264
- Status/date: merged / 2025-11-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `e389f91decda`
- Diff scope read: GitHub Pull Request files API returned 5 files, +117/-4, 171 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NVIDIA] Fix broken fp8 MoE of deepseek v3"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[NVIDIA] Fix broken fp8 MoE of deepseek v3"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -93,6 +93,7; -674,6 +675,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -93,6 +93,7; -674,6 +675,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -93,6 +93,7 @@
+from sglang.srt.layers.moe.utils import RoutingMethodType
@@ -674,6 +675,7 @@ def __init__(
+            routing_method_type=RoutingMethodType.DeepSeekV3,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0
- Risk and verification: The diff ships test coverage in `test/srt/run_suite.py`, `test/srt/test_deepseek_r1_fp8_trtllm_backend.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #13617 - [ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel

- Link: https://github.com/sgl-project/sglang/pull/13617
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `c8ede0e93c3a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +61/-15, 125 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +57/-14 (71 lines); hunks: -167,6 +167,9; -1813,10 +1816,25 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, forward_npu_sparse_prepare, _set_mla_kv_buffer, touching `forward_absorb_prepare, forward_absorb_core, forward_npu_sparse_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +57/-14 (71 lines); hunks: -167,6 +167,9; -1813,10 +1816,25 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, forward_npu_sparse_prepare, _set_mla_kv_buffer
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -167,6 +167,9 @@
+    from aiter.ops.triton.batched_gemm_a8w8_a_per_token_group_prequant_w_per_batched_tensor_quant import (
+        batched_gemm_a8w8_a_per_token_group_prequant_w_per_batched_tensor_quant,
+    )
@@ -1813,10 +1816,25 @@ def forward_absorb_prepare(
-                q_nope_out = torch.bmm(
-                    q_nope.to(torch.bfloat16).transpose(0, 1),
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +57/-14
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12964 - [DeepseekV3.2] Deepseek fp8 support for MHA path

- Link: https://github.com/sgl-project/sglang/pull/12964
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `fa924410276d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +55/-9, 114 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepseekV3.2] Deepseek fp8 support for MHA path"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepseekV3.2] Deepseek fp8 support for MHA path"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[Deepseek V3.2] Change indexer weights_proj to fp32"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Deepseek V3.2] Change indexer weights_proj to fp32"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #13705 - [AMD] Enable fused shared expert append and flatten quant for fp8 deepseekR1 model

- Link: https://github.com/sgl-project/sglang/pull/13705
- Status/date: merged / 2025-11-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `eff7df6d0a49`
- Diff scope read: GitHub Pull Request files API returned 3 files, +92/-26, 162 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Enable fused shared expert append and flatten quant for fp8 deepseekR1 model"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[AMD] Enable fused shared expert append and flatten quant for fp8 deepseekR1 model"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +10/-1 (11 lines); hunks: -168,10 +168,14; -2001,6 +2005,11 @@ def forward_absorb_core(; symbols: forward_absorb_core, touching `forward_absorb_core`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +10/-1 (11 lines); hunks: -168,10 +168,14; -2001,6 +2005,11 @@ def forward_absorb_core(; symbols: forward_absorb_core
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -168,10 +168,14 @@
-    from aiter.ops.triton.fused_fp8_quant import fused_rms_fp8_group_quant
+    from aiter.ops.triton.fused_fp8_quant import (
+        fused_flatten_fp8_group_quant,
+        fused_rms_fp8_group_quant,
+    )
@@ -2001,6 +2005,11 @@ def forward_absorb_core(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +10/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13544 - [DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend

- Link: https://github.com/sgl-project/sglang/pull/13544
- Status/date: merged / 2025-11-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `5eed5fc0b091`
- Diff scope read: GitHub Pull Request files API returned 2 files, +74/-78, 342 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #13954 - Fix Deepseek v3.1 loading issue

- Link: https://github.com/sgl-project/sglang/pull/13954
- Status/date: merged / 2025-11-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `13e5beeab499`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Deepseek v3.1 loading issue"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix Deepseek v3.1 loading issue"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights, touching `post_load_weights`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
-                        and self_attn.kv_b_proj.executed_weight_requant_ue8m0
+                        and weight_scale.format_ue8m0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13115 - support mtp with deepseek r1 nvfp4 model

- Link: https://github.com/sgl-project/sglang/pull/13115
- Status/date: merged / 2025-12-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `ea177372bd8c`
- Diff scope read: GitHub Pull Request files API returned 11 files, +123/-59, 459 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support mtp with deepseek r1 nvfp4 model"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "support mtp with deepseek r1 nvfp4 model"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -2502,7 +2502,9 @@ def forward_normal_chunked_kv_prepare(; symbols: forward_normal_chunked_kv_prepare, forward_normal_chunked_kv_core, touching `forward_normal_chunked_kv_prepare, forward_normal_chunked_kv_core`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -2502,7 +2502,9 @@ def forward_normal_chunked_kv_prepare(; symbols: forward_normal_chunked_kv_prepare, forward_normal_chunked_kv_core
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -2502,7 +2502,9 @@ def forward_normal_chunked_kv_prepare(
-        has_extend_prefix = any(forward_batch.extend_prefix_lens_cpu)
+        has_extend_prefix = forward_batch.extend_prefix_lens_cpu is not None and any(
+            forward_batch.extend_prefix_lens_cpu
+        )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #14573 - [Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode

- Link: https://github.com/sgl-project/sglang/pull/14573
- Status/date: merged / 2025-12-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `b7b7524e9560`
- Diff scope read: GitHub Pull Request files API returned 2 files, +144/-7, 165 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #14837 - [Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)

- Link: https://github.com/sgl-project/sglang/pull/14837
- Status/date: merged / 2025-12-10
- Trace source: `git log --name-only -- <model-files>` found it through `examples/chat_template/tool_chat_template_deepseekv31.jinja`; associated commits `ef1ab2302ab2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)"; the main implementation surface is `examples/chat_template/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11.
- Code diff details:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11
- Key code excerpts:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv31.jinja
@@ -19,7 +19,11 @@
-    {% set tool_ns.text = tool_ns.text + '\n### ' + tool.function.name + '\nDescription: ' + tool.function.description + '\n\nParameters: ' + (tool.function.parameters | tojson) +
+    {% if tool.function.description is not none %}
+      {% set tool_ns.text = tool_ns.text + '\n### ' + tool.function.name + '\nDescription: ' + tool.function.description + '\n\nParameters: ' + (tool.function.parameters | tojson)
+    {% else %}
+      {% set tool_ns.text = tool_ns.text + '\n### ' + tool.function.name + '\n\nParameters: ' + (tool.function.parameters | tojson) + '\n' %}
+    {% endif %}
```

- Reviewed files:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1
- Risk and verification: This is mostly docs/examples in `examples/chat_template/tool_chat_template_deepseekv31.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #14541 - [NPU]dsv3.2 cp for npu

- Link: https://github.com/sgl-project/sglang/pull/14541
- Status/date: merged / 2025-12-11
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; associated commits `388018a5bd41`
- Diff scope read: GitHub Pull Request files API returned 8 files, +281/-134, 587 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]dsv3.2 cp for npu"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU]dsv3.2 cp for npu"; the main implementation surface is `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[NPU] optimization for dsv3.2"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU] optimization for dsv3.2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #14975 - [AMD] Support fused_rms_mxfp4_quant in the prefill stage for DeepSeek-R1-MXFP4

- Link: https://github.com/sgl-project/sglang/pull/14975
- Status/date: merged / 2025-12-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `8ac350f335c6`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-1, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Support fused_rms_mxfp4_quant in the prefill stage for DeepSeek-R1-MXFP4"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[AMD] Support fused_rms_mxfp4_quant in the prefill stage for DeepSeek-R1-MXFP4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -1722,7 +1722,17 @@ def forward_normal_prepare(; symbols: forward_normal_prepare, touching `forward_normal_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -1722,7 +1722,17 @@ def forward_normal_prepare(; symbols: forward_normal_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1722,7 +1722,17 @@ def forward_normal_prepare(
+            elif _use_aiter_gfx95 and self.q_b_proj.weight.dtype == torch.uint8:
+                # MXFP4: fused RMSNorm + quant
+                q, _, _, _ = fused_rms_mxfp4_quant(
+                    q,
+                    self.q_a_layernorm.weight,
+                    self.q_a_layernorm.variance_epsilon,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15278 - feat: DeepSeek-V3.2 Streaming tool call output

- Link: https://github.com/sgl-project/sglang/pull/15278
- Status/date: merged / 2025-12-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `41683536d394`
- Diff scope read: GitHub Pull Request files API returned 2 files, +111/-69, 328 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat: DeepSeek-V3.2 Streaming tool call output"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "feat: DeepSeek-V3.2 Streaming tool call output"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #15531 - Support piecewise cuda graph for dsv3 fp4

- Link: https://github.com/sgl-project/sglang/pull/15531
- Status/date: merged / 2025-12-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `8fe3e3746832`
- Diff scope read: GitHub Pull Request files API returned 7 files, +148/-16, 261 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support piecewise cuda graph for dsv3 fp4"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Support piecewise cuda graph for dsv3 fp4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -20,6 +20,7; -400,6 +401,9 @@ def handle_attention_fa4(attn, forward_batch):; symbols: handle_attention_fa4, handle_attention_trtllm_mla, forward, touching `handle_attention_fa4, handle_attention_trtllm_mla, forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -20,6 +20,7; -400,6 +401,9 @@ def handle_attention_fa4(attn, forward_batch):; symbols: handle_attention_fa4, handle_attention_trtllm_mla, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -20,6 +20,7 @@
+from contextlib import nullcontext
@@ -400,6 +401,9 @@ def handle_attention_fa4(attn, forward_batch):
+    if is_in_piecewise_cuda_graph():
+        return AttnForwardMethod.MLA
@@ -3188,7 +3192,13 @@ def forward(
-            with get_global_expert_distribution_recorder().with_current_layer(i):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1
- Risk and verification: The diff ships test coverage in `test/srt/run_suite.py`, `test/srt/test_deepseek_v3_fp4_4gpu.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14750 - [Tool Call][DSV32] Streamline function call parameters

- Link: https://github.com/sgl-project/sglang/pull/14750
- Status/date: merged / 2025-12-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `01bd0d3e8b8c`
- Diff scope read: GitHub Pull Request files API returned 2 files, +60/-29, 200 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tool Call][DSV32] Streamline function call parameters"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Tool Call][DSV32] Streamline function call parameters"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #14280 - feat PD: add eagle3 support for DeepSeek V3 in EP mode

- Link: https://github.com/sgl-project/sglang/pull/14280
- Status/date: merged / 2025-12-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `2ec6fa3c54a8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-1, 34 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "feat PD: add eagle3 support for DeepSeek V3 in EP mode"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "feat PD: add eagle3 support for DeepSeek V3 in EP mode"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +12/-1 (13 lines); hunks: -46,6 +46,7; -3117,6 +3118,10 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-1 (13 lines); hunks: -46,6 +46,7; -3117,6 +3118,10 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -46,6 +46,7 @@
+    tensor_model_parallel_all_gather,
@@ -3117,6 +3118,10 @@ def __init__(
+        if get_moe_a2a_backend().is_deepep() or get_moe_a2a_backend().is_mooncake():
+            self.enable_a2a_moe = True
+        else:
+            self.enable_a2a_moe = False
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13394 - Fix DeepSeekV31's structural tag trigger

- Link: https://github.com/sgl-project/sglang/pull/13394
- Status/date: merged / 2025-12-31
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv31_detector.py`; associated commits `2667c857a78f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 7 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix DeepSeekV31's structural tag trigger"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv31_detector.py`; technical summary: Covers "Fix DeepSeekV31's structural tag trigger"; the main implementation surface is `python/sglang/srt/function_call/deepseekv31_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info, touching `structure_info`.
- Code diff details:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info
- Key code excerpts:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:
-            trigger="<｜tool▁call▁begin｜>" + name + "<｜tool▁sep｜>",
+            trigger="<｜tool▁call▁begin｜>",
```

- Reviewed files:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/function_call/deepseekv31_detector.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13959 - [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache

- Link: https://github.com/sgl-project/sglang/pull/13959
- Status/date: merged / 2026-01-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `0d244116d28a`
- Diff scope read: GitHub Pull Request files API returned 14 files, +603/-264, 1414 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[DSv32] Overlap indexer weights_proj during dual_stream decode"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DSv32] Overlap indexer weights_proj during dual_stream decode"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #17179 - [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests

- Link: https://github.com/sgl-project/sglang/pull/17179
- Status/date: merged / 2026-01-20
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`; associated commits `a3addd6203ca`
- Diff scope read: GitHub Pull Request files API returned 18 files, +1140/-99, 1539 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`; technical summary: Covers "[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +5/-30 (35 lines); hunks: -1,7 +1,7; -32,9 +32,9; symbols: get_mxfp4_models, touching `get_mxfp4_models`; `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` modified +13/-3 (16 lines); hunks: -30,7 +30,10; -43,7 +46,14 @@ def generate_simple_markdown_report(results: List[BenchmarkRe...; symbols: generate_simple_markdown_report, setUpClass, touching `generate_simple_markdown_report, setUpClass`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +5/-30 (35 lines); hunks: -1,7 +1,7; -32,9 +32,9; symbols: get_mxfp4_models
  - `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` modified +13/-3 (16 lines); hunks: -30,7 +30,10; -43,7 +46,14 @@ def generate_simple_markdown_report(results: List[BenchmarkRe...; symbols: generate_simple_markdown_report, setUpClass
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py
@@ -1,7 +1,7 @@
-Tests DeepSeek-R1-MXFP4 quantized model with multiple configurations
-(basic, MTP, DP, TC) using few-shot completion benchmark on MI35x.
+Tests DeepSeek-R1-MXFP4 quantized model with basic configuration
+using few-shot completion benchmark on MI35x.
@@ -32,9 +32,9 @@
-# Register for AMD CI - MI35x DeepSeek-R1-MXFP4 accuracy tests (~120 min)
diff -- test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py
@@ -30,7 +30,10 @@
-    """Generate a simplified markdown report without traces and cost columns."""
+    """Generate a simplified markdown report without traces and cost columns.
+    Skips the first result if it's a warmup run (duplicate batch_size).
+    """
@@ -43,7 +46,14 @@ def generate_simple_markdown_report(results: List[BenchmarkResult]) -> str:
-    for result in results:
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +5/-30; `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` modified +13/-3
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/test_vlms_mmmu_eval_amd.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #17007 - [NPU]bugfix: fix for dsv3.2 and dsvl2

- Link: https://github.com/sgl-project/sglang/pull/17007
- Status/date: merged / 2026-01-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `c0b5a180febe`
- Diff scope read: GitHub Pull Request files API returned 5 files, +129/-46, 224 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[NPU]bugfix: fix for dsv3.2 and dsvl2"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU]bugfix: fix for dsv3.2 and dsvl2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[NPU]DeepSeek-V3.2 support npu mlaprolog"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[NPU]DeepSeek-V3.2 support npu mlaprolog"; the main implementation surface is `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #17523 - [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI

- Link: https://github.com/sgl-project/sglang/pull/17523
- Status/date: merged / 2026-01-28
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`; associated commits `f8636fbb253a`
- Diff scope read: GitHub Pull Request files API returned 27 files, +1540/-43, 1823 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`; technical summary: Covers "[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -214,6 +214,9 @@ def test_deepseek_r1_accuracy(self):; symbols: test_deepseek_r1_accuracy, touching `test_deepseek_r1_accuracy`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -239,6 +239,9 @@ def test_deepseek_r1_mxfp4_accuracy(self):; symbols: test_deepseek_r1_mxfp4_accuracy, touching `test_deepseek_r1_mxfp4_accuracy`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -214,6 +214,9 @@ def test_deepseek_r1_accuracy(self):; symbols: test_deepseek_r1_accuracy
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -239,6 +239,9 @@ def test_deepseek_r1_mxfp4_accuracy(self):; symbols: test_deepseek_r1_mxfp4_accuracy
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py
@@ -214,6 +214,9 @@ def test_deepseek_r1_accuracy(self):
+                        print(
+                            f"  accuracy={acc:.3f} threshold={config.accuracy_threshold} {status}"
+                        )
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py
@@ -239,6 +239,9 @@ def test_deepseek_r1_mxfp4_accuracy(self):
+                        print(
+                            f"  accuracy={acc:.3f} threshold={config.accuracy_threshold} {status}"
+                        )
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` modified +3/-0; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +3/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #18297 - Deepseekv32 compatibility with transformers v5

- Link: https://github.com/sgl-project/sglang/pull/18297
- Status/date: merged / 2026-02-10
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `e8a2c133807c`
- Diff scope read: GitHub Pull Request files API returned 5 files, +33/-19, 131 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Deepseekv32 compatibility with transformers v5"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Deepseekv32 compatibility with transformers v5"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "Fix model loading for DeepSeek-V3.2-AWQ"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Fix model loading for DeepSeek-V3.2-AWQ"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #18624 - [AMD] DSR1/V3 use fp8 bmm in MLA for MI300X

- Link: https://github.com/sgl-project/sglang/pull/18624
- Status/date: merged / 2026-02-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `c193a52fa263`
- Diff scope read: GitHub Pull Request files API returned 1 files, +13/-9, 67 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] DSR1/V3 use fp8 bmm in MLA for MI300X"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[AMD] DSR1/V3 use fp8 bmm in MLA for MI300X"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +13/-9 (22 lines); hunks: -119,6 +119,7; -158,11 +159,11; symbols: forward, forward_absorb_prepare, forward_absorb_core, touching `forward, forward_absorb_prepare, forward_absorb_core`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-9 (22 lines); hunks: -119,6 +119,7; -158,11 +159,11; symbols: forward, forward_absorb_prepare, forward_absorb_core
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -119,6 +119,7 @@
+from sglang.srt.model_executor.cuda_graph_runner import get_is_capture_mode
@@ -158,11 +159,11 @@
-if _use_aiter_gfx95:
+if _use_aiter:
+if _use_aiter_gfx95:
@@ -564,8 +565,6 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-9
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18242 - [ROCm] Optimize Deepseek R1 on MI300X

- Link: https://github.com/sgl-project/sglang/pull/18242
- Status/date: merged / 2026-02-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `b9cf1563de97`
- Diff scope read: GitHub Pull Request files API returned 3 files, +7/-2, 44 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm] Optimize Deepseek R1 on MI300X"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[ROCm] Optimize Deepseek R1 on MI300X"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -180,6 +180,9; -1724,7 +1727,7 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, touching `forward_absorb_prepare, forward_absorb_core`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -180,6 +180,9; -1724,7 +1727,7 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -180,6 +180,9 @@
+if _use_aiter:
+    from sglang.srt.layers.rocm_linear_utils import fused_qk_rope_cat_and_cache_mla
@@ -1724,7 +1727,7 @@ def forward_absorb_prepare(
-            and (not _use_aiter or not _is_gfx95_supported or self.use_nsa)
+            and (not _use_aiter or not _is_hip or self.use_nsa)
@@ -1780,7 +1783,7 @@ def forward_absorb_core(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #19428 - [Feature] add feature mla_ag_after_qlora for dsv3.2

- Link: https://github.com/sgl-project/sglang/pull/19428
- Status/date: merged / 2026-03-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `b3718982a1b4`
- Diff scope read: GitHub Pull Request files API returned 5 files, +101/-9, 316 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] add feature mla_ag_after_qlora for dsv3.2"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; technical summary: Covers "[Feature] add feature mla_ag_after_qlora for dsv3.2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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
- Motivation: Title: "[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format."; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format."; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #19843 - [AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3

- Link: https://github.com/sgl-project/sglang/pull/19843
- Status/date: merged / 2026-03-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `84aaa69795f3`
- Diff scope read: GitHub Pull Request files API returned 1 files, +12/-7, 26 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +12/-7 (19 lines); hunks: -271,13 +271,18 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-7 (19 lines); hunks: -271,13 +271,18 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -271,13 +271,18 @@ def __init__(
-            correction_bias_dtype = (
-                torch.bfloat16
-                if quant_config is not None
-                and quant_config.get_name() == "modelopt_fp4"
-                and get_moe_runner_backend().is_flashinfer_trtllm()
-                else torch.float32
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18451 - [AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256.

- Link: https://github.com/sgl-project/sglang/pull/18451
- Status/date: merged / 2026-03-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `85fe8c6793a0`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256."; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256."; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -325,7 +325,11 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -325,7 +325,11 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -325,7 +325,11 @@ def forward(
-            elif _use_aiter_gfx95 and hidden_states.shape[0] <= 256:
+            elif (
+                _use_aiter_gfx95
+                and hidden_states.shape[0] <= 256
+                and self.weight.shape[0] <= 256
+            ):
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18461 - [Intel GPU] Enable DeepSeek R1 inference on XPU

- Link: https://github.com/sgl-project/sglang/pull/18461
- Status/date: merged / 2026-03-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `f0303fd07eb0`
- Diff scope read: GitHub Pull Request files API returned 6 files, +46/-28, 245 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Intel GPU] Enable DeepSeek R1 inference on XPU"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[Intel GPU] Enable DeepSeek R1 inference on XPU"; the main implementation surface is `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +2/-1 (3 lines); hunks: -50,6 +50,7; -497,7 +498,7 @@ def post_load_weights(; symbols: post_load_weights, touching `post_load_weights`; `python/sglang/srt/models/deepseek_common/utils.py` modified +2/-0 (2 lines); hunks: -31,6 +31,7; -40,6 +41,7; `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -137,6 +137,7; -677,6 +678,7 @@ def _post_combine_hook(; symbols: _post_combine_hook, touching `_post_combine_hook`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +2/-1 (3 lines); hunks: -50,6 +50,7; -497,7 +498,7 @@ def post_load_weights(; symbols: post_load_weights
  - `python/sglang/srt/models/deepseek_common/utils.py` modified +2/-0 (2 lines); hunks: -31,6 +31,7; -40,6 +41,7
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -137,6 +137,7; -677,6 +678,7 @@ def _post_combine_hook(; symbols: _post_combine_hook
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py
@@ -50,6 +50,7 @@
+    _is_xpu,
@@ -497,7 +498,7 @@ def post_load_weights(
-                        _is_cuda
+                        (_is_cuda or _is_xpu)
diff -- python/sglang/srt/models/deepseek_common/utils.py
@@ -31,6 +31,7 @@
+    is_xpu,
@@ -40,6 +41,7 @@
+_is_xpu = is_xpu()
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -137,6 +137,7 @@
+    _is_xpu,
@@ -677,6 +678,7 @@ def _post_combine_hook(
+            and not _is_xpu
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +2/-1; `python/sglang/srt/models/deepseek_common/utils.py` modified +2/-0; `python/sglang/srt/models/deepseek_v2.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/token_dispatcher/standard.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17707 - Add dsv3 router gemm benchmark on blackwell

- Link: https://github.com/sgl-project/sglang/pull/17707
- Status/date: merged / 2026-04-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `9fa12d605af2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +284/-4, 310 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add dsv3 router gemm benchmark on blackwell"; model line: DeepSeek V3/R1; category: docs/tests/CI; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Add dsv3 router gemm benchmark on blackwell"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +34/-4 (38 lines); hunks: -165,7 +165,10; -324,11 +327,20 @@ def forward(; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm, touching `forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +34/-4 (38 lines); hunks: -165,7 +165,10; -324,11 +327,20 @@ def forward(; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -165,7 +165,10 @@
+    from flashinfer.gemm import mm_M1_16_K7168_N256 as _raw_dsv3_router_gemm
+    from sglang.srt.utils.custom_op import register_custom_op
@@ -324,11 +327,20 @@ def forward(
+                if _device_sm >= 100 and self.weight.shape[0] == 256:
+                    # router gemm output float32
+                    logits = torch.empty(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +34/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21405 - Enable IndexCache for DeepSeek V3.2

- Link: https://github.com/sgl-project/sglang/pull/21405
- Status/date: merged / 2026-04-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `5a3531641735`
- Diff scope read: GitHub Pull Request files API returned 4 files, +196/-20, 358 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Enable IndexCache for DeepSeek V3.2"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "Enable IndexCache for DeepSeek V3.2"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #22774 - [MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1)

- Link: https://github.com/sgl-project/sglang/pull/22774
- Status/date: merged / 2026-04-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `b35213be11c7`
- Diff scope read: GitHub Pull Request files API returned 27 files, +184/-44, 795 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1)"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; technical summary: Covers "[MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1)"; the main implementation surface is `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py` modified +14/-3 (17 lines); hunks: -1,6 +1,6; -14,10 +14,12; symbols: execute, deep_gemm_execution_hook, _deep_gemm_execution_hook, touching `execute, deep_gemm_execution_hook, _deep_gemm_execution_hook`; `python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -141,6 +141,7; -182,6 +183,8; symbols: forward_normal_dual_stream, _post_combine_hook, __init__, determine_num_fused_shared_experts, touching `forward_normal_dual_stream, _post_combine_hook, __init__`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +10/-1 (11 lines); hunks: -49,6 +49,7; -498,7 +499,7 @@ def post_load_weights(; symbols: post_load_weights, touching `post_load_weights`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +6/-0 (6 lines); hunks: -21,6 +21,7; -553,6 +554,11 @@ def forward_absorb_core(; symbols: forward_absorb_core, touching `forward_absorb_core`.
- Code diff details:
  - `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py` modified +14/-3 (17 lines); hunks: -1,6 +1,6; -14,10 +14,12; symbols: execute, deep_gemm_execution_hook, _deep_gemm_execution_hook
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -141,6 +141,7; -182,6 +183,8; symbols: forward_normal_dual_stream, _post_combine_hook, __init__, determine_num_fused_shared_experts
  - `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +10/-1 (11 lines); hunks: -49,6 +49,7; -498,7 +499,7 @@ def post_load_weights(; symbols: post_load_weights
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +6/-0 (6 lines); hunks: -21,6 +21,7; -553,6 +554,11 @@ def forward_absorb_core(; symbols: forward_absorb_core
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +2/-1 (3 lines); hunks: -13,6 +13,7; -491,7 +492,7 @@ def _concat_and_cast_mha_k(; symbols: _concat_and_cast_mha_k
- Key code excerpts:

```diff
diff -- python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py
@@ -1,6 +1,6 @@
-from contextlib import contextmanager
+from contextlib import contextmanager, nullcontext
@@ -14,10 +14,12 @@
-from sglang.srt.utils import ceil_div, get_available_gpu_memory
+from sglang.srt.utils import ceil_div, get_available_gpu_memory, is_musa
+_is_musa = is_musa()
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -141,6 +141,7 @@
+    _is_musa,
@@ -182,6 +183,8 @@
+elif _is_musa:
+    from sgl_kernel import dsv3_fused_a_gemm, dsv3_router_gemm
@@ -640,7 +643,9 @@ def forward_normal_dual_stream(
-            if not _is_cuda or isinstance(self.experts.quant_method, KTEPWrapperMethod):
diff -- python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py
@@ -49,6 +49,7 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py` modified +14/-3; `python/sglang/srt/models/deepseek_v2.py` modified +13/-4; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +10/-1; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +6/-0; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +2/-1; `python/sglang/srt/layers/quantization/fp8_utils.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25233 - [Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers

- Link: https://github.com/sgl-project/sglang/pull/25233
- Status/date: merged / 2026-05-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/function_call/deepseekv32_detector.py`; associated commits `7cb4669a049a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +115/-3, 141 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/function_call/deepseekv32_detector.py`; technical summary: Covers "[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers"; the main implementation surface is `python/sglang/srt/function_call/deepseekv32_detector.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #25189 - [perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths

- Link: https://github.com/sgl-project/sglang/pull/25189
- Status/date: merged / 2026-05-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `2df9e8b4b331`
- Diff scope read: GitHub Pull Request files API returned 2 files, +3/-14, 45 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -403,6 +403,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -403,6 +403,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -403,6 +403,7 @@ def forward(
+                    # TODO: will check the dtype to be bf16
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25898 - [AMD] Dsv4/pr1 fix run time issue

- Link: https://github.com/sgl-project/sglang/pull/25898
- Status/date: merged / 2026-05-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `af8f66940e9b`
- Diff scope read: GitHub Pull Request files API returned 32 files, +2523/-129, 3203 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Dsv4/pr1 fix run time issue"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[AMD] Dsv4/pr1 fix run time issue"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +39/-1 (40 lines); hunks: -255,6 +255,11 @@ def __init__(; -316,8 +321,41 @@ def forward(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +39/-1 (40 lines); hunks: -255,6 +255,11 @@ def __init__(; -316,8 +321,41 @@ def forward(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -255,6 +255,11 @@ def __init__(
+        self.use_fused_clamp_act_mul = (
+            _is_hip and envs.SGLANG_OPT_USE_FUSED_CLAMP_ACT_MUL.get()
+        )
+        self._fused_clamp_fp8_checked = False
+        self._fused_clamp_use_fp8 = False
@@ -316,8 +321,41 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +39/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/jit_kernel/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26395 - [AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x

- Link: https://github.com/sgl-project/sglang/pull/26395
- Status/date: merged / 2026-05-27
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`; associated commits `bf5bc234310b`
- Diff scope read: GitHub Pull Request files API returned 1 files, +171/-0, 172 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`; technical summary: Covers "[AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x"; the main implementation surface is `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` added +171/-0 (171 lines); hunks: -0,0 +1,171; symbols: TestDeepSeekR1HiCacheMI35x, setUpClass, tearDownClass, test_gsm8k, touching `TestDeepSeekR1HiCacheMI35x, setUpClass, tearDownClass`.
- Code diff details:
  - `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` added +171/-0 (171 lines); hunks: -0,0 +1,171; symbols: TestDeepSeekR1HiCacheMI35x, setUpClass, tearDownClass, test_gsm8k
- Key code excerpts:

```diff
diff -- test/registered/amd/test_deepseek_r1_hicache_mi35x.py
@@ -0,0 +1,171 @@
+"""MI35x DeepSeek-R1-0528 FP8 HiCache PR Test (8-GPU)
+Regression guard: launches DeepSeek-R1-0528 (native FP8, MLA, aiter attention
+backend) on MI35x with the full L1+L2+L3 HiCache hierarchy wired up
+(``--enable-hierarchical-cache --hicache-storage-backend file``), then runs
+GSM8K few-shot completion and asserts the accuracy still matches the
+established threshold. The goal is to catch regressions where HiCache
```

- Reviewed files:
  - tests: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` added +171/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27188 - [AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage

- Link: https://github.com/sgl-project/sglang/pull/27188
- Status/date: merged / 2026-06-03
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`; associated commits `cfb7fb4fad03`
- Diff scope read: GitHub Pull Request files API returned 6 files, +518/-1, 619 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage"; model line: DeepSeek V3/R1; category: bug fix; main diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`; technical summary: Covers "[AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value, touching `get_model_path, get_one_example, get_few_shot_examples`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value, touching `get_model_path, get_one_example, get_few_shot_examples`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py
@@ -0,0 +1,185 @@
+"""MI35x DeepSeek-R1-MXFP4 TP=2 GSM8K AITER MLA regression.
+DeepSeek-R1 has 128 attention heads, so TP=2 gives 64 heads per rank. This
+covers the AITER persistent MLA decode metadata path that previously crashed
+with GPU memory access faults.
+Registry: nightly-amd-2-gpu-mi35x-deepseek-r1-mxfp4-tp2 suite
+"""
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py
@@ -0,0 +1,184 @@
+"""MI35x DeepSeek-R1-MXFP4 TP=4 GSM8K AITER MLA regression.
+DeepSeek-R1 has 128 attention heads, so TP=4 gives 32 heads per rank. This
+covers the AITER persistent MLA decode metadata path for the nhead=32 case.
+Registry: nightly-amd-8-gpu-mi35x-deepseek-r1-mxfp4-tp4 suite
+"""
+import ast
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` added +185/-0; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` added +184/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`, `test/run_suite.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27720 - [DeepSeek V3] Defer moe finalize and fused it with main stream add

- Link: https://github.com/sgl-project/sglang/pull/27720
- Status/date: merged / 2026-06-13
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `d1a39b0c74ed`
- Diff scope read: GitHub Pull Request files API returned 7 files, +743/-36, 865 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek V3] Defer moe finalize and fused it with main stream add"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepSeek V3] Defer moe finalize and fused it with main stream add"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +28/-7 (35 lines); hunks: -905,7 +905,18 @@ def forward_normal_dual_stream(; -916,12 +927,22 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream, touching `forward_normal_dual_stream`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +28/-7 (35 lines); hunks: -905,7 +905,18 @@ def forward_normal_dual_stream(; -916,12 +927,22 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -905,7 +905,18 @@ def forward_normal_dual_stream(
-            final_hidden_states = self.experts(hidden_states, topk_output)
+            deferred_finalize = (
+                shared_output is not None
+                and not self._shared_expert_tp1
+                and topk_output.format == TopKOutputFormat.BYPASSED
+                and self.experts.supports_deferred_finalize
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +28/-7
- Risk and verification: Runtime changes concentrate in `python/sglang/jit_kernel/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/jit_kernel/csrc/moe/tvm_ffi_utils.h`, `python/sglang/jit_kernel/moe_finalize_fuse_shared.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27243 - [AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests

- Link: https://github.com/sgl-project/sglang/pull/27243
- Status/date: merged / 2026-06-22
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`; associated commits `e2540188ce8b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +4/-36, 92 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`; technical summary: Covers "[AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` modified +2/-18 (20 lines); hunks: -9,11 +9,6; -39,21 +34,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP2MI35x, touching `get_model_path, get_one_example, few_shot_gsm8k`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` modified +2/-18 (20 lines); hunks: -8,11 +8,6; -38,21 +33,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP4MI35x, touching `get_model_path, get_one_example, few_shot_gsm8k`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` modified +2/-18 (20 lines); hunks: -9,11 +9,6; -39,21 +34,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP2MI35x
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` modified +2/-18 (20 lines); hunks: -8,11 +8,6; -38,21 +33,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP4MI35x
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py
@@ -9,11 +9,6 @@
-# Set HF cache for MI35x.
-os.environ.setdefault("HF_HOME", "/data2/models/huggingface")
-os.environ.setdefault("HF_HUB_CACHE", "/data2/models/huggingface/hub")
@@ -39,21 +34,10 @@
-DEEPSEEK_R1_MXFP4_LOCAL_PATH = "/data2/models/amd-DeepSeek-R1-MXFP4-Preview"
-DEEPSEEK_R1_MXFP4_HF_MODEL_ID = "amd/DeepSeek-R1-MXFP4-Preview"
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py
@@ -8,11 +8,6 @@
-# Set HF cache for MI35x.
-os.environ.setdefault("HF_HOME", "/data2/models/huggingface")
-os.environ.setdefault("HF_HUB_CACHE", "/data2/models/huggingface/hub")
@@ -38,21 +33,10 @@
-DEEPSEEK_R1_MXFP4_LOCAL_PATH = "/data2/models/amd-DeepSeek-R1-MXFP4-Preview"
-DEEPSEEK_R1_MXFP4_HF_MODEL_ID = "amd/DeepSeek-R1-MXFP4-Preview"
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` modified +2/-18; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` modified +2/-18
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29142 - [DeepSeek V3] Run routed experts on main stream in dual-stream MoE

- Link: https://github.com/sgl-project/sglang/pull/29142
- Status/date: merged / 2026-06-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `999199f9ff4b`
- Diff scope read: GitHub Pull Request files API returned 1 files, +48/-46, 108 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +48/-46 (94 lines); hunks: -936,59 +936,61 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream, touching `forward_normal_dual_stream`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +48/-46 (94 lines); hunks: -936,59 +936,61 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -936,59 +936,61 @@ def forward_normal_dual_stream(
-        shared_output = self._forward_shared_experts(
-            hidden_states, gemm_output_zero_allocator
-        )
+        # router_logits: (num_tokens, n_experts)
+        router_logits = self.gate(hidden_states, gemm_output_zero_allocator)
+        if use_flashinfer_trtllm_bypass:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +48/-46
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21531 - [JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel

- Link: https://github.com/sgl-project/sglang/pull/21531
- Status/date: merged / 2026-06-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `714011a40fc3`
- Diff scope read: GitHub Pull Request files API returned 12 files, +395/-252, 722 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +10/-37 (47 lines); hunks: -196,8 +196,11; -208,7 +211,7; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm, dsv2_flashinfer_moe_dual_stream_graph, touching `forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +10/-37 (47 lines); hunks: -196,8 +196,11; -208,7 +211,7; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm, dsv2_flashinfer_moe_dual_stream_graph
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -196,8 +196,11 @@
-    from flashinfer.gemm import mm_M1_16_K7168_N256 as _raw_dsv3_router_gemm
-    from sgl_kernel import dsv3_fused_a_gemm, dsv3_router_gemm
+    from sgl_kernel import dsv3_fused_a_gemm
+    from sglang.jit_kernel.dsv3_router_gemm import (
+        dsv3_router_gemm as _jit_dsv3_router_gemm,
+    )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +10/-37
- Risk and verification: The diff ships test coverage in `sgl-kernel/tests/test_dsv3_router_gemm.py`, `test/registered/jit/benchmark/bench_dsv3_router_gemm.py`, `test/registered/jit/test_dsv3_router_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29452 - Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE"

- Link: https://github.com/sgl-project/sglang/pull/29452
- Status/date: merged / 2026-06-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `7b02eab7a688`
- Diff scope read: GitHub Pull Request files API returned 1 files, +46/-48, 108 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE""; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE""; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +46/-48 (94 lines); hunks: -927,61 +927,59 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream, touching `forward_normal_dual_stream`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +46/-48 (94 lines); hunks: -927,61 +927,59 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -927,61 +927,59 @@ def forward_normal_dual_stream(
+        shared_output = self._forward_shared_experts(
+            hidden_states, gemm_output_zero_allocator
+        )
-        # router_logits: (num_tokens, n_experts)
-        router_logits = self.gate(hidden_states, gemm_output_zero_allocator)
-        if use_flashinfer_trtllm_bypass:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +46/-48
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #29463 - [DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE

- Link: https://github.com/sgl-project/sglang/pull/29463
- Status/date: merged / 2026-06-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `6bdecb8206b8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +49/-46, 111 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "[DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +49/-46 (95 lines); hunks: -925,61 +925,64 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream, touching `forward_normal_dual_stream`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +49/-46 (95 lines); hunks: -925,61 +925,64 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -925,61 +925,64 @@ def forward_normal_dual_stream(
+        # Note(kpham-sgl): launch the shared expert BEFORE the routed call.
+        # The routed deep_gemm pre-permute calls `dispose_tensor` which
+        # `set_()`s `hidden_states` to empty (host-side); any later kernel
+        # launch consuming `hidden_states` then captures `data_ptr() == 0`
+        # into the decode CUDA graph and replays from null.
-        shared_output = self._forward_shared_experts(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +49/-46
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #29290 - [AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI

- Link: https://github.com/sgl-project/sglang/pull/29290
- Status/date: merged / 2026-07-01
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`; associated commits `548f505cc54a`
- Diff scope read: GitHub Pull Request files API returned 3 files, +226/-2, 243 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`; technical summary: Covers "[AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI"; the main implementation surface is `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` added +202/-0 (202 lines); hunks: -0,0 +1,202; symbols: get_one_example, get_few_shot_examples, get_answer_value, run_gsm8k_benchmark, touching `get_one_example, get_few_shot_examples, get_answer_value`.
- Code diff details:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` added +202/-0 (202 lines); hunks: -0,0 +1,202; symbols: get_one_example, get_few_shot_examples, get_answer_value, run_gsm8k_benchmark
- Key code excerpts:

```diff
diff -- test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py
@@ -0,0 +1,202 @@
+"""MI35x DeepSeek-R1-MXFP4 TP=4 EAGLE GSM8K regression.
+This mirrors the production-style TP=4 launch recipe with EAGLE speculative
+decoding, overlap plan stream, FP8 KV cache, long context, and full GSM8K
+client pressure enabled.
+Registry: nightly-amd-8-gpu-mi35x-deepseek-r1-mxfp4-tp4 suite
+"""
```

- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` added +202/-0
- Risk and verification: The diff ships test coverage in `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31619 - [CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy

- Link: https://github.com/sgl-project/sglang/pull/31619
- Status/date: merged / 2026-07-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `7a896215e765`
- Diff scope read: GitHub Pull Request files API returned 7 files, +123/-76, 309 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "[CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +9/-7 (16 lines); hunks: -77,6 +77,7; -2546,9 +2547,13 @@ def forward(; symbols: forward, touching `forward`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +8/-2 (10 lines); hunks: -19,6 +19,7; -565,8 +566,13 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, touching `forward_absorb_prepare`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +9/-7 (16 lines); hunks: -77,6 +77,7; -2546,9 +2547,13 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +8/-2 (10 lines); hunks: -19,6 +19,7; -565,8 +566,13 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -77,6 +77,7 @@
+from sglang.srt.layers.cp.utils import is_cp_v2_active
@@ -2546,9 +2547,13 @@ def forward(
-        if dsa_use_prefill_cp(
-            forward_batch, self.dsa_enable_prefill_cp
-        ) or mla_use_prefill_cp(forward_batch, self.mla_enable_prefill_cp):
+        # CP-v2 shards/gathers at the eager-runner boundary instead.
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py
@@ -19,6 +19,7 @@
+from sglang.srt.layers.cp.utils import is_cp_v2_active
@@ -565,8 +566,13 @@ def forward_absorb_prepare(
-        if (dsa_prefill_cp or mla_prefill_cp) and not defer_kv_gather_until_after_rope:
-            # support allgather+rerrange
+        if (
+            (dsa_prefill_cp or mla_prefill_cp)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +9/-7; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +8/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/layers/cp/zigzag.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31888 - [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations

- Link: https://github.com/sgl-project/sglang/pull/31888
- Status/date: merged / 2026-07-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `e4a40a71f84c`
- Diff scope read: GitHub Pull Request files API returned 30 files, +3837/-52, 4635 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; technical summary: Covers "[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
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

### PR #34693 - [Kernel] Replace dsv3_router_gemm with the unified tiny GEMM

- Link: https://github.com/sgl-project/sglang/pull/34693
- Status/date: merged / 2026-09-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`; associated commits `cb6dd58fbeca`
- Diff scope read: GitHub Pull Request files API returned 15 files, +446/-638, 1409 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Replace dsv3_router_gemm with the unified tiny GEMM"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/utils.py`; technical summary: Covers "[Kernel] Replace dsv3_router_gemm with the unified tiny GEMM"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +13/-13 (26 lines); hunks: -179,7 +179,6; -195,6 +194,7; symbols: __init__, forward, touching `__init__, forward`; `python/sglang/srt/models/deepseek_common/utils.py` modified +17/-0 (17 lines); hunks: -180,3 +180,20 @@ def _get_llama_4_scaling(; symbols: _get_llama_4_scaling, tiny_router_gemm_max_tokens, touching `_get_llama_4_scaling, tiny_router_gemm_max_tokens`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-13 (26 lines); hunks: -179,7 +179,6; -195,6 +194,7; symbols: __init__, forward
  - `python/sglang/srt/models/deepseek_common/utils.py` modified +17/-0 (17 lines); hunks: -180,3 +180,20 @@ def _get_llama_4_scaling(; symbols: _get_llama_4_scaling, tiny_router_gemm_max_tokens
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -179,7 +179,6 @@
-    _device_sm,
@@ -195,6 +194,7 @@
+    tiny_router_gemm_max_tokens,
@@ -229,9 +229,7 @@
-    from sglang.kernels.ops.gemm.dsv3_router_gemm import (
-        dsv3_router_gemm as dsv3_router_gemm,
diff -- python/sglang/srt/models/deepseek_common/utils.py
@@ -180,3 +180,20 @@ def _get_llama_4_scaling(
+def tiny_router_gemm_max_tokens(
+    *, num_experts: int, hidden_size: int, weight_dtype: torch.dtype
+) -> int:
+    """Rows up to which the tiny GEMM beats cuBLAS for the router, -1 when the
+    shape or the device rules it out. Doubles as the kernel's compile-time
+    max_m, so keep it as tight as the measurements allow.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-13; `python/sglang/srt/models/deepseek_common/utils.py` modified +17/-0
- Risk and verification: The diff ships test coverage in `test/registered/kernels/benchmark/gemm/bench_dsv3_router_gemm.py`, `test/registered/kernels/benchmark/gemm/bench_tiny_gemm.py`, `test/registered/kernels/ops/gemm/test_dsv3_router_gemm.py`, `test/registered/kernels/ops/gemm/test_tiny_gemm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #38176 - keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4)

- Link: https://github.com/sgl-project/sglang/pull/38176
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_v2.py`; associated commits `4f52c9948bc8`
- Diff scope read: GitHub Pull Request files API returned 2 files, +29/-15, 117 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4)"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `python/sglang/srt/models/deepseek_v2.py`; technical summary: Covers "keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4)"; the main implementation surface is `python/sglang/srt/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -518,7 +518,9 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -518,7 +518,9 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -518,7 +518,9 @@ def forward(
-            return F.linear(hidden_states, self.weight, None)
+            if _is_cuda or _is_hip:
+                return torch.mm(hidden_states, self.weight.t(), out_dtype=torch.float32)
+            return F.linear(hidden_states.float(), self.weight.float(), None)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37762 - [AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8

- Link: https://github.com/sgl-project/sglang/pull/37762
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`; associated commits `632919e49865`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8"; model line: DeepSeek V3/R1; category: bug fix; main diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`; technical summary: Covers "[AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8"; the main implementation surface is `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` modified +1/-0 (1 lines); hunks: -348,6 +348,7 @@ def _fused_rope_cat_and_cache(; symbols: _fused_rope_cat_and_cache, touching `_fused_rope_cat_and_cache`.
- Code diff details:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` modified +1/-0 (1 lines); hunks: -348,6 +348,7 @@ def _fused_rope_cat_and_cache(; symbols: _fused_rope_cat_and_cache
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py
@@ -348,6 +348,7 @@ def _fused_rope_cat_and_cache(
+        and q_nope_out.shape[-2] == 12
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
