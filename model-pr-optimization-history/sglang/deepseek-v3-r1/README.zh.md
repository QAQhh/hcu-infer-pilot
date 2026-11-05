# sglang DeepSeek V3/R1 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-R1.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_1.mdx` | 无直接 PR 号提交 |
| `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx` | 无直接 PR 号提交 |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/deepseek_r1.mdx` | 无直接 PR 号提交 |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/deepseek_r1.mdx` | 无直接 PR 号提交 |
| `docs/docs/references/multi_node_deployment/rbg_pd/deepseekv32_pd.mdx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/deepseek-r1-advanced-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/deepseek-r1-basic-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/deepseek-v3-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/deepseek-v31-deployment.jsx` | 无直接 PR 号提交 |
| `docs/src/snippets/autoregressive/deepseek-v32-deployment.jsx` | 无直接 PR 号提交 |
| `examples/chat_template/tool_chat_template_deepseekv3.jinja` | [#5908](https://github.com/sgl-project/sglang/pull/5908), [#9525](https://github.com/sgl-project/sglang/pull/9525), [#10209](https://github.com/sgl-project/sglang/pull/10209) |
| `examples/chat_template/tool_chat_template_deepseekv31.jinja` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#9895](https://github.com/sgl-project/sglang/pull/9895), [#14837](https://github.com/sgl-project/sglang/pull/14837) |
| `examples/chat_template/tool_chat_template_deepseekv32.jinja` | [#11063](https://github.com/sgl-project/sglang/pull/11063) |
| `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` | 无直接 PR 号提交 |
| `python/sglang/srt/function_call/deepseekv31_detector.py` | [#9446](https://github.com/sgl-project/sglang/pull/9446), [#11589](https://github.com/sgl-project/sglang/pull/11589), [#13394](https://github.com/sgl-project/sglang/pull/13394) |
| `python/sglang/srt/function_call/deepseekv32_detector.py` | [#14573](https://github.com/sgl-project/sglang/pull/14573), [#14750](https://github.com/sgl-project/sglang/pull/14750), [#15278](https://github.com/sgl-project/sglang/pull/15278), [#16091](https://github.com/sgl-project/sglang/pull/16091), [#18174](https://github.com/sgl-project/sglang/pull/18174), [#25233](https://github.com/sgl-project/sglang/pull/25233) |
| `python/sglang/srt/function_call/deepseekv3_detector.py` | [#6655](https://github.com/sgl-project/sglang/pull/6655), [#7562](https://github.com/sgl-project/sglang/pull/7562), [#9525](https://github.com/sgl-project/sglang/pull/9525) |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | [#13959](https://github.com/sgl-project/sglang/pull/13959), [#14541](https://github.com/sgl-project/sglang/pull/14541), [#14572](https://github.com/sgl-project/sglang/pull/14572), [#15381](https://github.com/sgl-project/sglang/pull/15381), [#17007](https://github.com/sgl-project/sglang/pull/17007), [#19428](https://github.com/sgl-project/sglang/pull/19428) |
| `python/sglang/srt/models/deepseek_common/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/a8w8_blockscale_bpreshuffle_tuned_gemm.csv` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=2048-K=7168.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=7168-K=2048.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=8192-K=1536.json` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/aiter_intree_tune.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_act.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_moe.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | [#22774](https://github.com/sgl-project/sglang/pull/22774) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | [#21405](https://github.com/sgl-project/sglang/pull/21405), [#22774](https://github.com/sgl-project/sglang/pull/22774), [#31619](https://github.com/sgl-project/sglang/pull/31619), [#31888](https://github.com/sgl-project/sglang/pull/31888) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` | [#37762](https://github.com/sgl-project/sglang/pull/37762) |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/triton_qk_rmsnorm.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | [#18461](https://github.com/sgl-project/sglang/pull/18461), [#22774](https://github.com/sgl-project/sglang/pull/22774) |
| `python/sglang/srt/models/deepseek_common/moe_transport.py` | 无直接 PR 号提交 |
| `python/sglang/srt/models/deepseek_common/utils.py` | [#18461](https://github.com/sgl-project/sglang/pull/18461), [#22774](https://github.com/sgl-project/sglang/pull/22774), [#34693](https://github.com/sgl-project/sglang/pull/34693) |
| `python/sglang/srt/models/deepseek_v2.py` | [#2667](https://github.com/sgl-project/sglang/pull/2667), [#3237](https://github.com/sgl-project/sglang/pull/3237), [#3550](https://github.com/sgl-project/sglang/pull/3550), [#3582](https://github.com/sgl-project/sglang/pull/3582), [#3730](https://github.com/sgl-project/sglang/pull/3730), [#3785](https://github.com/sgl-project/sglang/pull/3785), [#3888](https://github.com/sgl-project/sglang/pull/3888), [#4836](https://github.com/sgl-project/sglang/pull/4836), [#4918](https://github.com/sgl-project/sglang/pull/4918), [#5571](https://github.com/sgl-project/sglang/pull/5571), [#5662](https://github.com/sgl-project/sglang/pull/5662), [#5707](https://github.com/sgl-project/sglang/pull/5707), ... (84 total) |
| `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` | [#17523](https://github.com/sgl-project/sglang/pull/17523) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_ar_fusion_eval_mi35x.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179), [#17523](https://github.com/sgl-project/sglang/pull/17523) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_kv_fp8_eval_mi35x.py` | 无直接 PR 号提交 |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` | [#27188](https://github.com/sgl-project/sglang/pull/27188), [#27243](https://github.com/sgl-project/sglang/pull/27243) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` | [#27188](https://github.com/sgl-project/sglang/pull/27188), [#27243](https://github.com/sgl-project/sglang/pull/27243) |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` | [#29290](https://github.com/sgl-project/sglang/pull/29290) |
| `test/registered/amd/accuracy/mi45x/test_deepseek_r1_0528_mxfp4_eval_mi45x.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_ar_fusion_perf_mi35x.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_kv_fp8_perf_mi35x.py` | 无直接 PR 号提交 |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` | [#17179](https://github.com/sgl-project/sglang/pull/17179) |
| `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` | [#26395](https://github.com/sgl-project/sglang/pull/26395) |
| `test/registered/unit/function_call/test_deepseekv32_detector.py` | 无直接 PR 号提交 |
| `test/registered/unit/model_executor/test_compensated_mhc_update_guard.py` | 无直接 PR 号提交 |
| `test/registered/xpu/llm_models/test_xpu_deepseek_v2_lite_chat_fp8_gsm8k_eval.py` | 无直接 PR 号提交 |

## PR 覆盖总览

- git 追溯 PR 数: 110
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 110
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
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

## 逐 PR diff 审计卡

### PR #2667 - AMD DeepSeek_V3 FP8 Numerical fix

- 链接: https://github.com/sgl-project/sglang/pull/2667
- 状态/时间: merged / 2024-12-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c5210dfa3802`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+34/-7，可读 patch 88 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「AMD DeepSeek_V3 FP8 Numerical fix」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「AMD DeepSeek_V3 FP8 Numerical fix」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +34/-7 (41 lines); hunks: -46,6 +46,7; -55,7 +56,9; symbols: forward_absorb, load_weights, DeepseekV3ForCausalLM，涉及 `forward_absorb, load_weights, DeepseekV3ForCausalLM`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +34/-7 (41 lines); hunks: -46,6 +46,7; -55,7 +56,9; symbols: forward_absorb, load_weights, DeepseekV3ForCausalLM
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +34/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #3550 - feat: support flashinfer mla attention for deepseek v3

- 链接: https://github.com/sgl-project/sglang/pull/3550
- 状态/时间: merged / 2025-02-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `70f894b810c0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+296/-132，可读 patch 737 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: support flashinfer mla attention for deepseek v3」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「feat: support flashinfer mla attention for deepseek v3」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +13/-7 (20 lines); hunks: -510,14 +510,20 @@ def forward(; symbols: forward, forward_normal，涉及 `forward, forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-7 (20 lines); hunks: -510,14 +510,20 @@ def forward(; symbols: forward, forward_normal
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-7
- 验证与风险: diff 自带测试面 `test/srt/test_eagle_infer.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #3582 - Support NextN (MTP) speculative decoding for DeepSeek-V3/R1

- 链接: https://github.com/sgl-project/sglang/pull/3582
- 状态/时间: merged / 2025-02-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `862dd76c7619`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+437/-7，可读 patch 529 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support NextN (MTP) speculative decoding for DeepSeek-V3/R1」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Support NextN (MTP) speculative decoding for DeepSeek-V3/R1」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +4/-1 (5 lines); hunks: -519,6 +519,8 @@ def forward(; -680,6 +682,7 @@ def __init__(; symbols: forward, __init__，涉及 `forward, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +4/-1 (5 lines); hunks: -519,6 +519,8 @@ def forward(; -680,6 +682,7 @@ def __init__(; symbols: forward, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +4/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #3785 - Refactor flashinfer logic for deepseek v3 and fix accuracy bug

- 链接: https://github.com/sgl-project/sglang/pull/3785
- 状态/时间: merged / 2025-02-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `b110084654a1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+565/-19，可读 patch 635 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Refactor flashinfer logic for deepseek v3 and fix accuracy bug」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Refactor flashinfer logic for deepseek v3 and fix accuracy bug」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +19/-17 (36 lines); hunks: -510,25 +510,27 @@ def forward(; symbols: forward, no_absorb, forward_normal，涉及 `forward, no_absorb, forward_normal`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +19/-17 (36 lines); hunks: -510,25 +510,27 @@ def forward(; symbols: forward, no_absorb, forward_normal
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +19/-17
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/model_executor/model_runner.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #3730 - Feature DeepSeek V3/R1 INT8 Quantization (block-wise)

- 链接: https://github.com/sgl-project/sglang/pull/3730
- 状态/时间: merged / 2025-02-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `1a6e97577acb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+1092/-5，可读 patch 1339 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Feature DeepSeek V3/R1 INT8 Quantization (block-wise)」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Feature DeepSeek V3/R1 INT8 Quantization (block-wise)」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +15/-0 (15 lines); hunks: -47,6 +47,9; -994,6 +997,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +15/-0 (15 lines); hunks: -47,6 +47,9; -994,6 +997,18 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +15/-0
- 验证与风险: diff 自带测试面 `test/srt/run_suite.py`, `test/srt/test_block_int8.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #3237 - [ROCm] Enable Fused MLA Triton kernel for DeepSeekV3

- 链接: https://github.com/sgl-project/sglang/pull/3237
- 状态/时间: merged / 2025-02-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `6ce9dbe82882`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+863/-1，可读 patch 894 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm] Enable Fused MLA Triton kernel for DeepSeekV3」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCm] Enable Fused MLA Triton kernel for DeepSeekV3」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +159/-1 (160 lines); hunks: -16,6 +16,7; -31,6 +32,9; symbols: no_absorb, forward_normal, forward_absorb, forward_absorb_fused_mla_rope，涉及 `no_absorb, forward_normal, forward_absorb`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +159/-1 (160 lines); hunks: -16,6 +16,7; -31,6 +32,9; symbols: no_absorb, forward_normal, forward_absorb, forward_absorb_fused_mla_rope
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +159/-1
- 验证与风险: diff 自带测试面 `test/srt/test_triton_attention_rocm_mla.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #3888 - [Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)

- 链接: https://github.com/sgl-project/sglang/pull/3888
- 状态/时间: merged / 2025-03-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c7f254468fca`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+369/-21，可读 patch 503 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +16/-12 (28 lines); hunks: -1202,18 +1202,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +16/-12 (28 lines); hunks: -1202,18 +1202,22 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +16/-12
- 验证与风险: diff 自带测试面 `test/srt/run_suite.py`, `test/srt/test_int8_kernel.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #4918 - Add DeepSeek V3/R1 shared experts fusion

- 链接: https://github.com/sgl-project/sglang/pull/4918
- 状态/时间: merged / 2025-04-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `924ca7c92c86`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+536/-36，可读 patch 939 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add DeepSeek V3/R1 shared experts fusion」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Add DeepSeek V3/R1 shared experts fusion」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +81/-5 (86 lines); hunks: -16,12 +16,14; -87,6 +89,8; symbols: DeepseekV2MLP, __init__，涉及 `DeepseekV2MLP, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +81/-5 (86 lines); hunks: -16,12 +16,14; -87,6 +89,8; symbols: DeepseekV2MLP, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +81/-5
- 验证与风险: diff 自带测试面 `sgl-kernel/tests/test_moe_align.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #4836 - Introduce moe_dense_tp_size to fix dense layer errors in DeepSeek V3 + 4x8xH100

- 链接: https://github.com/sgl-project/sglang/pull/4836
- 状态/时间: merged / 2025-04-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `53dcf3887639`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+31/-1，可读 patch 101 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Introduce moe_dense_tp_size to fix dense layer errors in DeepSeek V3 + 4x8xH100」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Introduce moe_dense_tp_size to fix dense layer errors in DeepSeek V3 + 4x8xH100」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +17/-1 (18 lines); hunks: -1066,12 +1066,18 @@ def __init__(; -1084,6 +1090,10 @@ def __init__(; symbols: __init__, _enable_moe_dense_fully_dp, _compute_info，涉及 `__init__, _enable_moe_dense_fully_dp, _compute_info`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +17/-1 (18 lines); hunks: -1066,12 +1066,18 @@ def __init__(; -1084,6 +1090,10 @@ def __init__(; symbols: __init__, _enable_moe_dense_fully_dp, _compute_info
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +17/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #5571 - enable DeepSeek V3 shared_experts_fusion in sm90

- 链接: https://github.com/sgl-project/sglang/pull/5571
- 状态/时间: merged / 2025-04-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `d9dd529854f7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-0，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「enable DeepSeek V3 shared_experts_fusion in sm90」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「enable DeepSeek V3 shared_experts_fusion in sm90」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +12/-0 (12 lines); hunks: -1427,6 +1427,18 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-0 (12 lines); hunks: -1427,6 +1427,18 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #5707 - [BugFix] Fix combination of MTP and `--n-share-experts-fusion`with R1

- 链接: https://github.com/sgl-project/sglang/pull/5707
- 状态/时间: merged / 2025-04-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `5d93a950eeeb`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+68/-15，可读 patch 150 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[BugFix] Fix combination of MTP and `--n-share-experts-fusion`with R1」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[BugFix] Fix combination of MTP and `--n-share-experts-fusion`with R1」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +18/-14 (32 lines); hunks: -1431,11 +1431,27 @@ def __init__(; -1450,7 +1466,7 @@ def __init__(; symbols: __init__, determine_n_share_experts_fusion, get_input_embeddings，涉及 `__init__, determine_n_share_experts_fusion, get_input_embeddings`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +18/-14 (32 lines); hunks: -1431,11 +1431,27 @@ def __init__(; -1450,7 +1466,7 @@ def __init__(; symbols: __init__, determine_n_share_experts_fusion, get_input_embeddings
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +18/-14
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #5908 - feat: Refactor DeepSeekV3 function call

- 链接: https://github.com/sgl-project/sglang/pull/5908
- 状态/时间: merged / 2025-05-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv3.jinja`；关联提交 `170d1f218a4e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+95/-29，可读 patch 155 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: Refactor DeepSeekV3 function call」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `examples/chat_template/tool_chat_template_deepseekv3.jinja`；技术摘要: 覆盖「feat: Refactor DeepSeekV3 function call」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv3.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/chat_template/tool_chat_template_deepseekv3.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91。
- 代码 diff 细节:
  - `examples/chat_template/tool_chat_template_deepseekv3.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- 关键代码摘录:

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

- 已读文件:
  - docs: `examples/chat_template/tool_chat_template_deepseekv3.jinja` added +91/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/openai_api/adapter.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6079 - Clean logs for DeepSeek-V3 launching

- 链接: https://github.com/sgl-project/sglang/pull/6079
- 状态/时间: merged / 2025-05-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `73600673bb1d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+61/-39，可读 patch 231 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Clean logs for DeepSeek-V3 launching」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Clean logs for DeepSeek-V3 launching」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -88,6 +88,7; -1487,8 +1488,9 @@ def determine_n_share_experts_fusion(; symbols: determine_n_share_experts_fusion, get_input_embeddings，涉及 `determine_n_share_experts_fusion, get_input_embeddings`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +7/-4 (11 lines); hunks: -88,6 +88,7; -1487,8 +1488,9 @@ def determine_n_share_experts_fusion(; symbols: determine_n_share_experts_fusion, get_input_embeddings
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +7/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #5662 - [perf] dsv3 bmm fallback to bf16

- 链接: https://github.com/sgl-project/sglang/pull/5662
- 状态/时间: merged / 2025-05-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `5e02330137a1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+48/-3，可读 patch 76 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[perf] dsv3 bmm fallback to bf16」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[perf] dsv3 bmm fallback to bf16」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +13/-3 (16 lines); hunks: -63,6 +63,7; -1589,13 +1590,22 @@ def post_load_weights(self, is_nextn=False):; symbols: post_load_weights，涉及 `post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-3 (16 lines); hunks: -63,6 +63,7; -1589,13 +1590,22 @@ def post_load_weights(self, is_nextn=False):; symbols: post_load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6655 - fix(deepseekv3): Fix DeepSeekV3Detector tool_index assignment and multi-tool call streaming support

- 链接: https://github.com/sgl-project/sglang/pull/6655
- 状态/时间: merged / 2025-05-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv3_detector.py`；关联提交 `461a73028070`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+52/-4，可读 patch 100 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix(deepseekv3): Fix DeepSeekV3Detector tool_index assignment and multi-tool call streaming support」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv3_detector.py`；技术摘要: 覆盖「fix(deepseekv3): Fix DeepSeekV3Detector tool_index assignment and multi-tool call streaming support」；主要实现面是 `python/sglang/srt/function_call/deepseekv3_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +52/-4 (56 lines); hunks: -31,6 +31,7 @@ def __init__(self):; -75,7 +76,12 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment，涉及 `__init__, has_tool_call, parse_streaming_increment`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv3_detector.py` modified +52/-4 (56 lines); hunks: -31,6 +31,7 @@ def __init__(self):; -75,7 +76,12 @@ def parse_streaming_increment(; symbols: __init__, has_tool_call, parse_streaming_increment
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +52/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv3_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6265 - [fix][RL] Fix DeepSeekV3ForCausalLM.post_load_weights for multiple update weight

- 链接: https://github.com/sgl-project/sglang/pull/6265
- 状态/时间: merged / 2025-05-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `51cdd81f9720`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+47/-14，可读 patch 114 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[fix][RL] Fix DeepSeekV3ForCausalLM.post_load_weights for multiple update weight」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[fix][RL] Fix DeepSeekV3ForCausalLM.post_load_weights for multiple update weight」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +39/-14 (53 lines); hunks: -92,6 +92,7; -1713,14 +1714,23 @@ def forward(; symbols: forward, post_load_weights，涉及 `forward, post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +39/-14 (53 lines); hunks: -92,6 +92,7; -1713,14 +1714,23 @@ def forward(; symbols: forward, post_load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +39/-14
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #6853 - [DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model

- 链接: https://github.com/sgl-project/sglang/pull/6853
- 状态/时间: merged / 2025-06-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c2c4f57f6311`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+386/-13，可读 patch 506 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +33/-5 (38 lines); hunks: -1746,7 +1746,7 @@ def determine_num_fused_shared_experts(; -1926,6 +1926,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: determine_num_fused_shared_experts, get_input_embeddings, post_load_weights, load_weights，涉及 `determine_num_fused_shared_experts, get_input_embeddings, post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +33/-5 (38 lines); hunks: -1746,7 +1746,7 @@ def determine_num_fused_shared_experts(; -1926,6 +1926,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: determine_num_fused_shared_experts, get_input_embeddings, post_load_weights, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +33/-5
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7181 - [fix] fix dsv3 weight loader tqdm and simplify shared experts fusion

- 链接: https://github.com/sgl-project/sglang/pull/7181
- 状态/时间: merged / 2025-06-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `ed54bf9d19f1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-96，可读 patch 131 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[fix] fix dsv3 weight loader tqdm and simplify shared experts fusion」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[fix] fix dsv3 weight loader tqdm and simplify shared experts fusion」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +11/-96 (107 lines); hunks: -1033,7 +1033,7 @@ def forward_absorb_core(; -2008,101 +2008,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: forward_absorb_core, load_weights，涉及 `forward_absorb_core, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-96 (107 lines); hunks: -1033,7 +1033,7 @@ def forward_absorb_core(; -2008,101 +2008,6 @@ def load_weights(self, weights: Iterable[Tuple[str, torc...; symbols: forward_absorb_core, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-96
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7164 - Fix Deepseek R1 0528 FP4 tensor name mismatch issue during weights loading.

- 链接: https://github.com/sgl-project/sglang/pull/7164
- 状态/时间: merged / 2025-06-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `8c16da334e93`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+10/-7，可读 patch 45 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Deepseek R1 0528 FP4 tensor name mismatch issue during weights loading.」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix Deepseek R1 0528 FP4 tensor name mismatch issue during weights loading.」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +5/-6 (11 lines); hunks: -1919,6 +1919,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; -2151,12 +2153,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: post_load_weights, load_weights，涉及 `post_load_weights, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-6 (11 lines); hunks: -1919,6 +1919,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; -2151,12 +2153,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: post_load_weights, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-6
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7286 - fix: resolve b200 dsv3 mtp issue

- 链接: https://github.com/sgl-project/sglang/pull/7286
- 状态/时间: merged / 2025-06-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `4f204db57cf9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-0，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: resolve b200 dsv3 mtp issue」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「fix: resolve b200 dsv3 mtp issue」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -1932,6 +1932,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights, _weight_requant_ue8m0，涉及 `post_load_weights, _weight_requant_ue8m0`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -1932,6 +1932,8 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights, _weight_requant_ue8m0
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -1932,6 +1932,8 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
+        if self.config.architectures[0] == "DeepseekV3ForCausalLMNextN":
+            return
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7371 - Fix judgment condition for enabling Deepseek V3/R1 shared expert fusion optimization

- 链接: https://github.com/sgl-project/sglang/pull/7371
- 状态/时间: merged / 2025-06-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `a06912ad8b35`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-3，可读 patch 24 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix judgment condition for enabling Deepseek V3/R1 shared expert fusion optimization」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix judgment condition for enabling Deepseek V3/R1 shared expert fusion optimization」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -1731,12 +1731,12 @@ def determine_num_fused_shared_experts(; -2040,7 +2040,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights，涉及 `determine_num_fused_shared_experts, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -1731,12 +1731,12 @@ def determine_num_fused_shared_experts(; -2040,7 +2040,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7481 - [perf] slightly imporve DeepSeek-R1-FP4 TP8

- 链接: https://github.com/sgl-project/sglang/pull/7481
- 状态/时间: merged / 2025-06-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `bdbb8d009ae1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-2，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[perf] slightly imporve DeepSeek-R1-FP4 TP8」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[perf] slightly imporve DeepSeek-R1-FP4 TP8」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +4/-2 (6 lines); hunks: -362,12 +362,14 @@ def forward(; symbols: forward, forward_normal_dual_stream，涉及 `forward, forward_normal_dual_stream`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +4/-2 (6 lines); hunks: -362,12 +362,14 @@ def forward(; symbols: forward, forward_normal_dual_stream
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -362,12 +362,14 @@ def forward(
+        # router_logits: (num_tokens, n_experts)
+        router_logits = self.gate(hidden_states)
-            # router_logits: (num_tokens, n_experts)
-            router_logits = self.gate(hidden_states)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +4/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7376 - Fix MTP with Deepseek R1 Fp4

- 链接: https://github.com/sgl-project/sglang/pull/7376
- 状态/时间: merged / 2025-06-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `15f34013432f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+20/-1，可读 patch 49 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix MTP with Deepseek R1 Fp4」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix MTP with Deepseek R1 Fp4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -2201,7 +2201,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -2232,6 +2232,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +8/-1 (9 lines); hunks: -2201,7 +2201,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; -2232,6 +2232,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +8/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7635 - Apply dsv3_fused_a_gemm kernel

- 链接: https://github.com/sgl-project/sglang/pull/7635
- 状态/时间: merged / 2025-07-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `00aec6ad6c34`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+18/-2，可读 patch 48 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Apply dsv3_fused_a_gemm kernel」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Apply dsv3_fused_a_gemm kernel」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +18/-2 (20 lines); hunks: -96,6 +96,7; -112,7 +113,7; symbols: __init__, forward_absorb_prepare，涉及 `__init__, forward_absorb_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +18/-2 (20 lines); hunks: -96,6 +96,7; -112,7 +113,7; symbols: __init__, forward_absorb_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +18/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7677 - Apply dsv3 router gemm kernel for deepseek-r1 fp4

- 链接: https://github.com/sgl-project/sglang/pull/7677
- 状态/时间: merged / 2025-07-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `88f484ce4c73`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+21/-3，可读 patch 47 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Apply dsv3 router gemm kernel for deepseek-r1 fp4」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Apply dsv3 router gemm kernel for deepseek-r1 fp4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +21/-3 (24 lines); hunks: -111,9 +111,16; -225,7 +232,18 @@ def forward(self, hidden_states):; symbols: forward, __init__，涉及 `forward, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +21/-3 (24 lines); hunks: -111,9 +111,16; -225,7 +232,18 @@ def forward(self, hidden_states):; symbols: forward, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +21/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7735 - fix awq and dsv3 fused gemm compatible

- 链接: https://github.com/sgl-project/sglang/pull/7735
- 状态/时间: merged / 2025-07-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `84f2e4a0f847`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+15/-2，可读 patch 47 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix awq and dsv3 fused gemm compatible」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「fix awq and dsv3 fused gemm compatible」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +15/-2 (17 lines); hunks: -318,11 +318,17 @@ def __init__(; -876,8 +882,13 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +15/-2 (17 lines); hunks: -318,11 +318,17 @@ def __init__(; -876,8 +882,13 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +15/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7738 - fix dsv3 fused proj check

- 链接: https://github.com/sgl-project/sglang/pull/7738
- 状态/时间: merged / 2025-07-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `b58226510f7d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+15/-14，可读 patch 61 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix dsv3 fused proj check」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「fix dsv3 fused proj check」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +15/-14 (29 lines); hunks: -336,10 +336,12 @@ def __init__(; -891,21 +893,20 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +15/-14 (29 lines); hunks: -336,10 +336,12 @@ def __init__(; -891,21 +893,20 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +15/-14
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7750 - [fix] fix dsv3_router_gemm filter

- 链接: https://github.com/sgl-project/sglang/pull/7750
- 状态/时间: merged / 2025-07-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `ac49dac00946`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[fix] fix dsv3_router_gemm filter」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[fix] fix dsv3_router_gemm filter」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -233,7 +233,8 @@ def forward(self, hidden_states):; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -233,7 +233,8 @@ def forward(self, hidden_states):; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -233,7 +233,8 @@ def forward(self, hidden_states):
-            hidden_states.shape[0] < 4
+            _is_cuda
+            and hidden_states.shape[0] < 4
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7793 - fix: disable dsv3_router_gemm in dsv3_nextn

- 链接: https://github.com/sgl-project/sglang/pull/7793
- 状态/时间: merged / 2025-07-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `54411f6afa27`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+9/-1，可读 patch 49 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: disable dsv3_router_gemm in dsv3_nextn」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「fix: disable dsv3_router_gemm in dsv3_nextn」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +9/-1 (10 lines); hunks: -210,8 +210,10 @@ def __init__(; -233,8 +235,10 @@ def forward(self, hidden_states):; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +9/-1 (10 lines); hunks: -210,8 +210,10 @@ def __init__(; -233,8 +235,10 @@ def forward(self, hidden_states):; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +9/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #7762 - feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode

- 链接: https://github.com/sgl-project/sglang/pull/7762
- 状态/时间: merged / 2025-07-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `cb9d91ea8a71`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 10 个文件，+1006/-9，可读 patch 1203 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -2363,6 +2363,12 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +6/-0 (6 lines); hunks: -2363,6 +2363,12 @@ def load_weights(self, weights: Iterable[Tuple[str, torch...; symbols: load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +6/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/test_cutlass_w4a8_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #7562 - Fix incomplete tool call capture issue in streaming response of DeepSeek-V3 when enable MTP

- 链接: https://github.com/sgl-project/sglang/pull/7562
- 状态/时间: merged / 2025-07-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv3_detector.py`；关联提交 `624a3b8d1f10`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+90/-1，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix incomplete tool call capture issue in streaming response of DeepSeek-V3 when enable MTP」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv3_detector.py`；技术摘要: 覆盖「Fix incomplete tool call capture issue in streaming response of DeepSeek-V3 when enable MTP」；主要实现面是 `python/sglang/srt/function_call/deepseekv3_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -98,7 +98,7 @@ def parse_streaming_increment(; symbols: parse_streaming_increment，涉及 `parse_streaming_increment`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -98,7 +98,7 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/deepseekv3_detector.py
@@ -98,7 +98,7 @@ def parse_streaming_increment(
-                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*)\n'''json\n(.*)",
+                pattern=r"<｜tool▁call▁begin｜>(.*)<｜tool▁sep｜>(.*)\n'''json\n(.*)\n'''.*",
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1
- 验证与风险: diff 自带测试面 `test/srt/test_function_call_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #8051 - Update batch size limitation of dsv3_router_gemm kernel to 16

- 链接: https://github.com/sgl-project/sglang/pull/8051
- 状态/时间: merged / 2025-08-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e7e5a3050a64`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-2，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update batch size limitation of dsv3_router_gemm kernel to 16」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Update batch size limitation of dsv3_router_gemm kernel to 16」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +1/-2 (3 lines); hunks: -248,8 +248,7 @@ def forward(self, hidden_states):; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-2 (3 lines); hunks: -248,8 +248,7 @@ def forward(self, hidden_states):; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -248,8 +248,7 @@ def forward(self, hidden_states):
-            and not self.is_nextn
-            and hidden_states.shape[0] < 4
+            and hidden_states.shape[0] <= 16
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9525 - tool-call(dsv3): Improve deepseek-v3 chat template and tool_choice = `required`

- 链接: https://github.com/sgl-project/sglang/pull/9525
- 状态/时间: merged / 2025-08-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv3.jinja`, `python/sglang/srt/function_call/deepseekv3_detector.py`；关联提交 `c9dd70fbde92`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+17/-17，可读 patch 98 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「tool-call(dsv3): Improve deepseek-v3 chat template and tool_choice = `required`」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv3_detector.py`, `examples/chat_template/tool_chat_template_deepseekv3.jinja`；技术摘要: 覆盖「tool-call(dsv3): Improve deepseek-v3 chat template and tool_choice = `required`」；主要实现面是 `python/sglang/srt/function_call/deepseekv3_detector.py`, `examples/chat_template/tool_chat_template_deepseekv3.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -215,6 +215,6 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf，涉及 `build_ebnf`；`examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +16/-16 (32 lines); hunks: -12,7 +12,7; -23,13 +23,13。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1 (2 lines); hunks: -215,6 +215,6 @@ def build_ebnf(self, tools: List[Tool]):; symbols: build_ebnf
  - `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +16/-16 (32 lines); hunks: -12,7 +12,7; -23,13 +23,13
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv3_detector.py` modified +1/-1
  - docs: `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +16/-16
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv3_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9446 - Support DeepSeek-V3.1 tool call

- 链接: https://github.com/sgl-project/sglang/pull/9446
- 状态/时间: merged / 2025-08-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv31.jinja`, `python/sglang/srt/function_call/deepseekv31_detector.py`；关联提交 `b9683be6538e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+315/-0，可读 patch 331 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support DeepSeek-V3.1 tool call」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「Support DeepSeek-V3.1 tool call」；主要实现面是 `python/sglang/srt/function_call/deepseekv31_detector.py`, `examples/chat_template/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse，涉及 `DeepSeekV31Detector, __init__, has_tool_call`；`examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0 (222 lines); hunks: -0,0 +1,222; symbols: DeepSeekV31Detector, __init__, has_tool_call, detect_and_parse
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` added +222/-0
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` added +91/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv31_detector.py`, `python/sglang/srt/function_call/function_call_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9815 - fix: dsv3 lite q_lora_rank none

- 链接: https://github.com/sgl-project/sglang/pull/9815
- 状态/时间: merged / 2025-08-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `8abe8deae6cd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-4，可读 patch 31 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「fix: dsv3 lite q_lora_rank none」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「fix: dsv3 lite q_lora_rank none」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +12/-4 (16 lines); hunks: -2414,18 +2414,26 @@ def _weight_requant_ue8m0(self, is_nextn=False):; symbols: _weight_requant_ue8m0，涉及 `_weight_requant_ue8m0`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-4 (16 lines); hunks: -2414,18 +2414,26 @@ def _weight_requant_ue8m0(self, is_nextn=False):; symbols: _weight_requant_ue8m0
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #8118 - [feat] Support tp mode for DeepSeek-R1-W4AFP8

- 链接: https://github.com/sgl-project/sglang/pull/8118
- 状态/时间: merged / 2025-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `d4a938417d2c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+291/-120，可读 patch 710 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[feat] Support tp mode for DeepSeek-R1-W4AFP8」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[feat] Support tp mode for DeepSeek-R1-W4AFP8」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -2168,6 +2168,8 @@ def determine_num_fused_shared_experts(; -2471,6 +2473,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights，涉及 `determine_num_fused_shared_experts, load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -2168,6 +2168,8 @@ def determine_num_fused_shared_experts(; -2471,6 +2473,9 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: determine_num_fused_shared_experts, load_weights
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-0
- 验证与风险: diff 自带测试面 `python/sglang/test/test_cutlass_w4a8_moe.py`, `sgl-kernel/tests/test_cutlass_w4a8_moe_mm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #9895 - Update tool_chat_template_deepseekv31.jinja

- 链接: https://github.com/sgl-project/sglang/pull/9895
- 状态/时间: merged / 2025-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；关联提交 `cc9a31c66226`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+3/-3，可读 patch 17 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Update tool_chat_template_deepseekv31.jinja」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「Update tool_chat_template_deepseekv31.jinja」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13。
- 代码 diff 细节:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3 (6 lines); hunks: -43,13 +43,13
- 关键代码摘录:

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

- 已读文件:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +3/-3
- 验证与风险: 该 PR 主要落在文档/示例 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #9671 - Optimized deepseek-v3/r1 model performance on mxfp4 run

- 链接: https://github.com/sgl-project/sglang/pull/9671
- 状态/时间: merged / 2025-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `0dfd54d11d06`, `1b2ff4fb7f05`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+458/-62，可读 patch 763 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Optimized deepseek-v3/r1 model performance on mxfp4 run」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Optimized deepseek-v3/r1 model performance on mxfp4 run」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +202/-27 (229 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__，涉及 `forward, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +202/-27 (229 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +202/-27
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9959 - Revert "Optimized deepseek-v3/r1 model performance on mxfp4 run (#9671)"

- 链接: https://github.com/sgl-project/sglang/pull/9959
- 状态/时间: merged / 2025-09-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `1b2ff4fb7f05`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+62/-458，可读 patch 763 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "Optimized deepseek-v3/r1 model performance on mxfp4 run (#9671)"」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Revert "Optimized deepseek-v3/r1 model performance on mxfp4 run (#9671)"」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +27/-202 (229 lines); hunks: -112,7 +112,6; -130,22 +129,6; symbols: forward, __init__，涉及 `forward, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +27/-202 (229 lines); hunks: -112,7 +112,6; -130,22 +129,6; symbols: forward, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +27/-202
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10008 - Optimized deepseek-v3/r1 model performance on mxfp4 run

- 链接: https://github.com/sgl-project/sglang/pull/10008
- 状态/时间: merged / 2025-09-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e96973742c32`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+489/-67，可读 patch 850 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Optimized deepseek-v3/r1 model performance on mxfp4 run」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Optimized deepseek-v3/r1 model performance on mxfp4 run」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +228/-32 (260 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__，涉及 `forward, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +228/-32 (260 lines); hunks: -112,6 +112,7; -129,6 +130,22; symbols: forward, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +228/-32
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #8677 - Fix accuracy drop of dsv3 run in dp enablement

- 链接: https://github.com/sgl-project/sglang/pull/8677
- 状态/时间: merged / 2025-09-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `918e3d4c27c3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+100/-69，可读 patch 210 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix accuracy drop of dsv3 run in dp enablement」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix accuracy drop of dsv3 run in dp enablement」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +7/-1 (8 lines); hunks: -1077,7 +1077,13 @@ def _dispatch_mla_subtype():; symbols: _dispatch_mla_subtype，涉及 `_dispatch_mla_subtype`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +7/-1 (8 lines); hunks: -1077,7 +1077,13 @@ def _dispatch_mla_subtype():; symbols: _dispatch_mla_subtype
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +7/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #9834 - perf: Avoid unnecessary data type conversions for DeepSeek-V3 on Blackwell

- 链接: https://github.com/sgl-project/sglang/pull/9834
- 状态/时间: merged / 2025-09-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `012584ecd539`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+13/-4，可读 patch 52 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「perf: Avoid unnecessary data type conversions for DeepSeek-V3 on Blackwell」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「perf: Avoid unnecessary data type conversions for DeepSeek-V3 on Blackwell」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +11/-3 (14 lines); hunks: -67,7 +67,10; -299,7 +302,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward, __init__，涉及 `forward, __init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-3 (14 lines); hunks: -67,7 +67,10; -299,7 +302,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward, __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-3
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10104 - Fix run time error in dsv3-fp8 model on mi35x

- 链接: https://github.com/sgl-project/sglang/pull/10104
- 状态/时间: merged / 2025-09-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `400d3b97aebc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix run time error in dsv3-fp8 model on mi35x」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix run time error in dsv3-fp8 model on mi35x」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -249,7 +249,11 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -249,7 +249,11 @@ def forward(; symbols: forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #10209 - tool-call(dsv3): Fixed a parse problem when there are multiple function definitions in tool_calls

- 链接: https://github.com/sgl-project/sglang/pull/10209
- 状态/时间: merged / 2025-09-09
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv3.jinja`；关联提交 `2cd94dd07eea`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「tool-call(dsv3): Fixed a parse problem when there are multiple function definitions in tool_calls」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `examples/chat_template/tool_chat_template_deepseekv3.jinja`；技术摘要: 覆盖「tool-call(dsv3): Fixed a parse problem when there are multiple function definitions in tool_calls」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv3.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +1/-1 (2 lines); hunks: -55,7 +55,7。
- 代码 diff 细节:
  - `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +1/-1 (2 lines); hunks: -55,7 +55,7
- 关键代码摘录:

```diff
diff -- examples/chat_template/tool_chat_template_deepseekv3.jinja
@@ -55,7 +55,7 @@
-                {{- '\n' + '<｜tool▁call▁begin｜>' + tool['type'] + '<｜tool▁sep｜>' + tool['function']['name'] + '\n' + ''''json' + '\n' + tool['function']['arguments'] + '\n' + ''''
+                {{- '\n' + '<｜tool▁call▁begin｜>' + tool['type'] + '<｜tool▁sep｜>' + tool['function']['name'] + '\n' + ''''json' + '\n' + tool['function']['arguments']|tojson + '\n'
```

- 已读文件:
  - docs: `examples/chat_template/tool_chat_template_deepseekv3.jinja` modified +1/-1
- 验证与风险: 该 PR 主要落在文档/示例 `examples/chat_template/tool_chat_template_deepseekv3.jinja`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #11063 - Add DeepSeek-V3.2 Tool Call Template

- 链接: https://github.com/sgl-project/sglang/pull/11063
- 状态/时间: merged / 2025-10-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv32.jinja`；关联提交 `85c1f7937781`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+100/-0，可读 patch 101 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add DeepSeek-V3.2 Tool Call Template」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `examples/chat_template/tool_chat_template_deepseekv32.jinja`；技术摘要: 覆盖「Add DeepSeek-V3.2 Tool Call Template」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv32.jinja`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「Support DeepSeek V3.2 Exp」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Support DeepSeek V3.2 Exp」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Bugfix] Fix Qwen3/DSV3/DSV3.2 model support」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #12095 - [2/2] Deepseek deterministic: support deepseek v3 deterministic inference on 8 x H200

- 链接: https://github.com/sgl-project/sglang/pull/12095
- 状态/时间: merged / 2025-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e39628fd07b3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+19/-0，可读 patch 54 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[2/2] Deepseek deterministic: support deepseek v3 deterministic inference on 8 x H200」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[2/2] Deepseek deterministic: support deepseek v3 deterministic inference on 8 x H200」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +3/-0 (3 lines); hunks: -515,6 +515,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-0 (3 lines); hunks: -515,6 +515,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator:...; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -515,6 +515,9 @@ def forward(self, hidden_states, gemm_output_zero_allocator: BumpAllocator = Non
+        if get_global_server_args().enable_deterministic_inference:
+            return F.linear(hidden_states, self.weight, None)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-0
- 验证与风险: diff 自带测试面 `test/srt/test_fused_moe.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #12094 - Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4

- 链接: https://github.com/sgl-project/sglang/pull/12094
- 状态/时间: merged / 2025-10-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `9ff9fa7f95be`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+110/-22，可读 patch 231 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fuse wk and weight_proj in Indexer for DeepSeekV3.2-FP4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100)」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #12689 - [ROCM] Optimized deepseek-r1 model with rmsnorm + fp8 quant fusion

- 链接: https://github.com/sgl-project/sglang/pull/12689
- 状态/时间: merged / 2025-11-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `4a78031a71dd`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+331/-22，可读 patch 474 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCM] Optimized deepseek-r1 model with rmsnorm + fp8 quant fusion」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCM] Optimized deepseek-r1 model with rmsnorm + fp8 quant fusion」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +117/-15 (132 lines); hunks: -153,6 +153,8; -1507,13 +1509,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare, forward_npu_sparse_prepare，涉及 `forward_normal_prepare, forward_absorb_prepare, forward_npu_sparse_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +117/-15 (132 lines); hunks: -153,6 +153,8; -1507,13 +1509,14 @@ def forward_normal_prepare(; symbols: forward_normal_prepare, forward_absorb_prepare, forward_npu_sparse_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +117/-15
- 验证与风险: diff 自带测试面 `test/srt/quant/test_fused_rms_fp8_group_quant.py`, `test/srt/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #11589 - [Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector

- 链接: https://github.com/sgl-project/sglang/pull/11589
- 状态/时间: merged / 2025-11-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv31_detector.py`；关联提交 `fc5da1e80b78`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+4/-9，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv31_detector.py`；技术摘要: 覆盖「[Tool Call] Steamline function arguments when tool_choice="auto" for deepseekv31_detector」；主要实现面是 `python/sglang/srt/function_call/deepseekv31_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment，涉及 `parse_streaming_increment`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9 (13 lines); hunks: -115,13 +115,14 @@ def parse_streaming_increment(; -180,15 +181,9 @@ def parse_streaming_increment(; symbols: parse_streaming_increment
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +4/-9
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv31_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #12065 - (1/n)support context parallel with deepseekv3.2-DSA

- 链接: https://github.com/sgl-project/sglang/pull/12065
- 状态/时间: merged / 2025-11-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `d368c7451a48`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 17 个文件，+1247/-54，可读 patch 1729 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「(1/n)support context parallel with deepseekv3.2-DSA」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「(1/n)support context parallel with deepseekv3.2-DSA」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #13264 - [NVIDIA] Fix broken fp8 MoE of deepseek v3

- 链接: https://github.com/sgl-project/sglang/pull/13264
- 状态/时间: merged / 2025-11-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e389f91decda`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+117/-4，可读 patch 171 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NVIDIA] Fix broken fp8 MoE of deepseek v3」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[NVIDIA] Fix broken fp8 MoE of deepseek v3」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -93,6 +93,7; -674,6 +675,7 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -93,6 +93,7; -674,6 +675,7 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -93,6 +93,7 @@
+from sglang.srt.layers.moe.utils import RoutingMethodType
@@ -674,6 +675,7 @@ def __init__(
+            routing_method_type=RoutingMethodType.DeepSeekV3,
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +2/-0
- 验证与风险: diff 自带测试面 `test/srt/run_suite.py`, `test/srt/test_deepseek_r1_fp8_trtllm_backend.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #13617 - [ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel

- 链接: https://github.com/sgl-project/sglang/pull/13617
- 状态/时间: merged / 2025-11-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c8ede0e93c3a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+61/-15，可读 patch 125 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +57/-14 (71 lines); hunks: -167,6 +167,9; -1813,10 +1816,25 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, forward_npu_sparse_prepare, _set_mla_kv_buffer，涉及 `forward_absorb_prepare, forward_absorb_core, forward_npu_sparse_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +57/-14 (71 lines); hunks: -167,6 +167,9; -1813,10 +1816,25 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core, forward_npu_sparse_prepare, _set_mla_kv_buffer
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +57/-14
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #12964 - [DeepseekV3.2] Deepseek fp8 support for MHA path

- 链接: https://github.com/sgl-project/sglang/pull/12964
- 状态/时间: merged / 2025-11-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `fa924410276d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+55/-9，可读 patch 114 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepseekV3.2] Deepseek fp8 support for MHA path」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepseekV3.2] Deepseek fp8 support for MHA path」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[Deepseek V3.2] Change indexer weights_proj to fp32」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek V3.2] Change indexer weights_proj to fp32」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #13705 - [AMD] Enable fused shared expert append and flatten quant for fp8 deepseekR1 model

- 链接: https://github.com/sgl-project/sglang/pull/13705
- 状态/时间: merged / 2025-11-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `eff7df6d0a49`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+92/-26，可读 patch 162 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Enable fused shared expert append and flatten quant for fp8 deepseekR1 model」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[AMD] Enable fused shared expert append and flatten quant for fp8 deepseekR1 model」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +10/-1 (11 lines); hunks: -168,10 +168,14; -2001,6 +2005,11 @@ def forward_absorb_core(; symbols: forward_absorb_core，涉及 `forward_absorb_core`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +10/-1 (11 lines); hunks: -168,10 +168,14; -2001,6 +2005,11 @@ def forward_absorb_core(; symbols: forward_absorb_core
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +10/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13544 - [DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend

- 链接: https://github.com/sgl-project/sglang/pull/13544
- 状态/时间: merged / 2025-11-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `5eed5fc0b091`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+74/-78，可读 patch 342 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #13954 - Fix Deepseek v3.1 loading issue

- 链接: https://github.com/sgl-project/sglang/pull/13954
- 状态/时间: merged / 2025-11-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `13e5beeab499`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 9 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix Deepseek v3.1 loading issue」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix Deepseek v3.1 loading issue」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights，涉及 `post_load_weights`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-1 (2 lines); hunks: -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=N...; symbols: post_load_weights
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -3568,7 +3568,7 @@ def post_load_weights(self, is_nextn=False, weight_names=None):
-                        and self_attn.kv_b_proj.executed_weight_requant_ue8m0
+                        and weight_scale.format_ue8m0
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13115 - support mtp with deepseek r1 nvfp4 model

- 链接: https://github.com/sgl-project/sglang/pull/13115
- 状态/时间: merged / 2025-12-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `ea177372bd8c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+123/-59，可读 patch 459 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「support mtp with deepseek r1 nvfp4 model」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「support mtp with deepseek r1 nvfp4 model」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -2502,7 +2502,9 @@ def forward_normal_chunked_kv_prepare(; symbols: forward_normal_chunked_kv_prepare, forward_normal_chunked_kv_core，涉及 `forward_normal_chunked_kv_prepare, forward_normal_chunked_kv_core`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -2502,7 +2502,9 @@ def forward_normal_chunked_kv_prepare(; symbols: forward_normal_chunked_kv_prepare, forward_normal_chunked_kv_core
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -2502,7 +2502,9 @@ def forward_normal_chunked_kv_prepare(
-        has_extend_prefix = any(forward_batch.extend_prefix_lens_cpu)
+        has_extend_prefix = forward_batch.extend_prefix_lens_cpu is not None and any(
+            forward_batch.extend_prefix_lens_cpu
+        )
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #14573 - [Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode

- 链接: https://github.com/sgl-project/sglang/pull/14573
- 状态/时间: merged / 2025-12-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `b7b7524e9560`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+144/-7，可读 patch 165 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Tool Call] Fix DeepSeekV32Detector skipping functions with no params in streaming mode」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #14837 - [Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)

- 链接: https://github.com/sgl-project/sglang/pull/14837
- 状态/时间: merged / 2025-12-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；关联提交 `ef1ab2302ab2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `examples/chat_template/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「[Auto Sync] Update tool_chat_template_deepseekv31.jinja (20251210)」；主要实现面是 `examples/chat_template/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11。
- 代码 diff 细节:
  - `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1 (6 lines); hunks: -19,7 +19,11
- 关键代码摘录:

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

- 已读文件:
  - docs: `examples/chat_template/tool_chat_template_deepseekv31.jinja` modified +5/-1
- 验证与风险: 该 PR 主要落在文档/示例 `examples/chat_template/tool_chat_template_deepseekv31.jinja`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #14541 - [NPU]dsv3.2 cp for npu

- 链接: https://github.com/sgl-project/sglang/pull/14541
- 状态/时间: merged / 2025-12-11
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；关联提交 `388018a5bd41`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+281/-134，可读 patch 587 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]dsv3.2 cp for npu」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU]dsv3.2 cp for npu」；主要实现面是 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[NPU] optimization for dsv3.2」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU] optimization for dsv3.2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #14975 - [AMD] Support fused_rms_mxfp4_quant in the prefill stage for DeepSeek-R1-MXFP4

- 链接: https://github.com/sgl-project/sglang/pull/14975
- 状态/时间: merged / 2025-12-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `8ac350f335c6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-1，可读 patch 19 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Support fused_rms_mxfp4_quant in the prefill stage for DeepSeek-R1-MXFP4」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[AMD] Support fused_rms_mxfp4_quant in the prefill stage for DeepSeek-R1-MXFP4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -1722,7 +1722,17 @@ def forward_normal_prepare(; symbols: forward_normal_prepare，涉及 `forward_normal_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -1722,7 +1722,17 @@ def forward_normal_prepare(; symbols: forward_normal_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #15278 - feat: DeepSeek-V3.2 Streaming tool call output

- 链接: https://github.com/sgl-project/sglang/pull/15278
- 状态/时间: merged / 2025-12-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `41683536d394`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+111/-69，可读 patch 328 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat: DeepSeek-V3.2 Streaming tool call output」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「feat: DeepSeek-V3.2 Streaming tool call output」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #15531 - Support piecewise cuda graph for dsv3 fp4

- 链接: https://github.com/sgl-project/sglang/pull/15531
- 状态/时间: merged / 2025-12-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `8fe3e3746832`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+148/-16，可读 patch 261 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support piecewise cuda graph for dsv3 fp4」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Support piecewise cuda graph for dsv3 fp4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -20,6 +20,7; -400,6 +401,9 @@ def handle_attention_fa4(attn, forward_batch):; symbols: handle_attention_fa4, handle_attention_trtllm_mla, forward，涉及 `handle_attention_fa4, handle_attention_trtllm_mla, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +11/-1 (12 lines); hunks: -20,6 +20,7; -400,6 +401,9 @@ def handle_attention_fa4(attn, forward_batch):; symbols: handle_attention_fa4, handle_attention_trtllm_mla, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +11/-1
- 验证与风险: diff 自带测试面 `test/srt/run_suite.py`, `test/srt/test_deepseek_v3_fp4_4gpu.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #14750 - [Tool Call][DSV32] Streamline function call parameters

- 链接: https://github.com/sgl-project/sglang/pull/14750
- 状态/时间: merged / 2025-12-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `01bd0d3e8b8c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+60/-29，可读 patch 200 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Tool Call][DSV32] Streamline function call parameters」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Tool Call][DSV32] Streamline function call parameters」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #14280 - feat PD: add eagle3 support for DeepSeek V3 in EP mode

- 链接: https://github.com/sgl-project/sglang/pull/14280
- 状态/时间: merged / 2025-12-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `2ec6fa3c54a8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-1，可读 patch 34 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「feat PD: add eagle3 support for DeepSeek V3 in EP mode」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「feat PD: add eagle3 support for DeepSeek V3 in EP mode」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +12/-1 (13 lines); hunks: -46,6 +46,7; -3117,6 +3118,10 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-1 (13 lines); hunks: -46,6 +46,7; -3117,6 +3118,10 @@ def __init__(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13394 - Fix DeepSeekV31's structural tag trigger

- 链接: https://github.com/sgl-project/sglang/pull/13394
- 状态/时间: merged / 2025-12-31
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv31_detector.py`；关联提交 `2667c857a78f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-1，可读 patch 7 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Fix DeepSeekV31's structural tag trigger」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv31_detector.py`；技术摘要: 覆盖「Fix DeepSeekV31's structural tag trigger」；主要实现面是 `python/sglang/srt/function_call/deepseekv31_detector.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info，涉及 `structure_info`。
- 代码 diff 细节:
  - `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1 (2 lines); hunks: -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:; symbols: structure_info
- 关键代码摘录:

```diff
diff -- python/sglang/srt/function_call/deepseekv31_detector.py
@@ -202,5 +202,5 @@ def structure_info(self) -> _GetInfoFunc:
-            trigger="<｜tool▁call▁begin｜>" + name + "<｜tool▁sep｜>",
+            trigger="<｜tool▁call▁begin｜>",
```

- 已读文件:
  - runtime: `python/sglang/srt/function_call/deepseekv31_detector.py` modified +1/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/function_call/deepseekv31_detector.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13959 - [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache

- 链接: https://github.com/sgl-project/sglang/pull/13959
- 状态/时间: merged / 2026-01-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `0d244116d28a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 14 个文件，+603/-264，可读 patch 1414 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[DSv32] Overlap indexer weights_proj during dual_stream decode」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DSv32] Overlap indexer weights_proj during dual_stream decode」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #17179 - [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests

- 链接: https://github.com/sgl-project/sglang/pull/17179
- 状态/时间: merged / 2026-01-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`；关联提交 `a3addd6203ca`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 18 个文件，+1140/-99，可读 patch 1539 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`；技术摘要: 覆盖「[AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +5/-30 (35 lines); hunks: -1,7 +1,7; -32,9 +32,9; symbols: get_mxfp4_models，涉及 `get_mxfp4_models`；`test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` modified +13/-3 (16 lines); hunks: -30,7 +30,10; -43,7 +46,14 @@ def generate_simple_markdown_report(results: List[BenchmarkRe...; symbols: generate_simple_markdown_report, setUpClass，涉及 `generate_simple_markdown_report, setUpClass`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +5/-30 (35 lines); hunks: -1,7 +1,7; -32,9 +32,9; symbols: get_mxfp4_models
  - `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` modified +13/-3 (16 lines); hunks: -30,7 +30,10; -43,7 +46,14 @@ def generate_simple_markdown_report(results: List[BenchmarkRe...; symbols: generate_simple_markdown_report, setUpClass
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +5/-30; `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` modified +13/-3
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/test_vlms_mmmu_eval_amd.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #17007 - [NPU]bugfix: fix for dsv3.2 and dsvl2

- 链接: https://github.com/sgl-project/sglang/pull/17007
- 状态/时间: merged / 2026-01-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c0b5a180febe`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+129/-46，可读 patch 224 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[NPU]bugfix: fix for dsv3.2 and dsvl2」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU]bugfix: fix for dsv3.2 and dsvl2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[NPU]DeepSeek-V3.2 support npu mlaprolog」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[NPU]DeepSeek-V3.2 support npu mlaprolog」；主要实现面是 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #17523 - [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI

- 链接: https://github.com/sgl-project/sglang/pull/17523
- 状态/时间: merged / 2026-01-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`；关联提交 `f8636fbb253a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 27 个文件，+1540/-43，可读 patch 1823 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`；技术摘要: 覆盖「[AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -214,6 +214,9 @@ def test_deepseek_r1_accuracy(self):; symbols: test_deepseek_r1_accuracy，涉及 `test_deepseek_r1_accuracy`；`test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -239,6 +239,9 @@ def test_deepseek_r1_mxfp4_accuracy(self):; symbols: test_deepseek_r1_mxfp4_accuracy，涉及 `test_deepseek_r1_mxfp4_accuracy`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -214,6 +214,9 @@ def test_deepseek_r1_accuracy(self):; symbols: test_deepseek_r1_accuracy
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +3/-0 (3 lines); hunks: -239,6 +239,9 @@ def test_deepseek_r1_mxfp4_accuracy(self):; symbols: test_deepseek_r1_mxfp4_accuracy
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` modified +3/-0; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` modified +3/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #18297 - Deepseekv32 compatibility with transformers v5

- 链接: https://github.com/sgl-project/sglang/pull/18297
- 状态/时间: merged / 2026-02-10
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e8a2c133807c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+33/-19，可读 patch 131 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Deepseekv32 compatibility with transformers v5」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Deepseekv32 compatibility with transformers v5」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「Fix model loading for DeepSeek-V3.2-AWQ」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Fix model loading for DeepSeek-V3.2-AWQ」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #18624 - [AMD] DSR1/V3 use fp8 bmm in MLA for MI300X

- 链接: https://github.com/sgl-project/sglang/pull/18624
- 状态/时间: merged / 2026-02-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `c193a52fa263`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+13/-9，可读 patch 67 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] DSR1/V3 use fp8 bmm in MLA for MI300X」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[AMD] DSR1/V3 use fp8 bmm in MLA for MI300X」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +13/-9 (22 lines); hunks: -119,6 +119,7; -158,11 +159,11; symbols: forward, forward_absorb_prepare, forward_absorb_core，涉及 `forward, forward_absorb_prepare, forward_absorb_core`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-9 (22 lines); hunks: -119,6 +119,7; -158,11 +159,11; symbols: forward, forward_absorb_prepare, forward_absorb_core
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-9
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18242 - [ROCm] Optimize Deepseek R1 on MI300X

- 链接: https://github.com/sgl-project/sglang/pull/18242
- 状态/时间: merged / 2026-02-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `b9cf1563de97`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+7/-2，可读 patch 44 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm] Optimize Deepseek R1 on MI300X」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCm] Optimize Deepseek R1 on MI300X」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -180,6 +180,9; -1724,7 +1727,7 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core，涉及 `forward_absorb_prepare, forward_absorb_core`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -180,6 +180,9; -1724,7 +1727,7 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare, forward_absorb_core
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #19428 - [Feature] add feature mla_ag_after_qlora for dsv3.2

- 链接: https://github.com/sgl-project/sglang/pull/19428
- 状态/时间: merged / 2026-03-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `b3718982a1b4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+101/-9，可读 patch 316 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feature] add feature mla_ag_after_qlora for dsv3.2」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`；技术摘要: 覆盖「[Feature] add feature mla_ag_after_qlora for dsv3.2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
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
- 动机: 标题「[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format.」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format.」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #19843 - [AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3

- 链接: https://github.com/sgl-project/sglang/pull/19843
- 状态/时间: merged / 2026-03-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `84aaa69795f3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+12/-7，可读 patch 26 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +12/-7 (19 lines); hunks: -271,13 +271,18 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +12/-7 (19 lines); hunks: -271,13 +271,18 @@ def __init__(; symbols: __init__
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +12/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18451 - [AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256.

- 链接: https://github.com/sgl-project/sglang/pull/18451
- 状态/时间: merged / 2026-03-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `85fe8c6793a0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256.」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256.」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -325,7 +325,11 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -325,7 +325,11 @@ def forward(; symbols: forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #18461 - [Intel GPU] Enable DeepSeek R1 inference on XPU

- 链接: https://github.com/sgl-project/sglang/pull/18461
- 状态/时间: merged / 2026-03-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `f0303fd07eb0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+46/-28，可读 patch 245 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Intel GPU] Enable DeepSeek R1 inference on XPU」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[Intel GPU] Enable DeepSeek R1 inference on XPU」；主要实现面是 `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +2/-1 (3 lines); hunks: -50,6 +50,7; -497,7 +498,7 @@ def post_load_weights(; symbols: post_load_weights，涉及 `post_load_weights`；`python/sglang/srt/models/deepseek_common/utils.py` modified +2/-0 (2 lines); hunks: -31,6 +31,7; -40,6 +41,7；`python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -137,6 +137,7; -677,6 +678,7 @@ def _post_combine_hook(; symbols: _post_combine_hook，涉及 `_post_combine_hook`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +2/-1 (3 lines); hunks: -50,6 +50,7; -497,7 +498,7 @@ def post_load_weights(; symbols: post_load_weights
  - `python/sglang/srt/models/deepseek_common/utils.py` modified +2/-0 (2 lines); hunks: -31,6 +31,7; -40,6 +41,7
  - `python/sglang/srt/models/deepseek_v2.py` modified +2/-0 (2 lines); hunks: -137,6 +137,7; -677,6 +678,7 @@ def _post_combine_hook(; symbols: _post_combine_hook
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +2/-1; `python/sglang/srt/models/deepseek_common/utils.py` modified +2/-0; `python/sglang/srt/models/deepseek_v2.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/token_dispatcher/standard.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17707 - Add dsv3 router gemm benchmark on blackwell

- 链接: https://github.com/sgl-project/sglang/pull/17707
- 状态/时间: merged / 2026-04-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `9fa12d605af2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+284/-4，可读 patch 310 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add dsv3 router gemm benchmark on blackwell」；模型线: DeepSeek V3/R1；类别: 文档/测试/CI；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Add dsv3 router gemm benchmark on blackwell」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +34/-4 (38 lines); hunks: -165,7 +165,10; -324,11 +327,20 @@ def forward(; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm，涉及 `forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +34/-4 (38 lines); hunks: -165,7 +165,10; -324,11 +327,20 @@ def forward(; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +34/-4
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21405 - Enable IndexCache for DeepSeek V3.2

- 链接: https://github.com/sgl-project/sglang/pull/21405
- 状态/时间: merged / 2026-04-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `5a3531641735`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+196/-20，可读 patch 358 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Enable IndexCache for DeepSeek V3.2」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「Enable IndexCache for DeepSeek V3.2」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #22774 - [MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1)

- 链接: https://github.com/sgl-project/sglang/pull/22774
- 状态/时间: merged / 2026-04-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `b35213be11c7`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 27 个文件，+184/-44，可读 patch 795 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1)」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`；技术摘要: 覆盖「[MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1)」；主要实现面是 `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py` modified +14/-3 (17 lines); hunks: -1,6 +1,6; -14,10 +14,12; symbols: execute, deep_gemm_execution_hook, _deep_gemm_execution_hook，涉及 `execute, deep_gemm_execution_hook, _deep_gemm_execution_hook`；`python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -141,6 +141,7; -182,6 +183,8; symbols: forward_normal_dual_stream, _post_combine_hook, __init__, determine_num_fused_shared_experts，涉及 `forward_normal_dual_stream, _post_combine_hook, __init__`；`python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +10/-1 (11 lines); hunks: -49,6 +49,7; -498,7 +499,7 @@ def post_load_weights(; symbols: post_load_weights，涉及 `post_load_weights`；`python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +6/-0 (6 lines); hunks: -21,6 +21,7; -553,6 +554,11 @@ def forward_absorb_core(; symbols: forward_absorb_core，涉及 `forward_absorb_core`。
- 代码 diff 细节:
  - `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py` modified +14/-3 (17 lines); hunks: -1,6 +1,6; -14,10 +14,12; symbols: execute, deep_gemm_execution_hook, _deep_gemm_execution_hook
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-4 (17 lines); hunks: -141,6 +141,7; -182,6 +183,8; symbols: forward_normal_dual_stream, _post_combine_hook, __init__, determine_num_fused_shared_experts
  - `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +10/-1 (11 lines); hunks: -49,6 +49,7; -498,7 +499,7 @@ def post_load_weights(; symbols: post_load_weights
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +6/-0 (6 lines); hunks: -21,6 +21,7; -553,6 +554,11 @@ def forward_absorb_core(; symbols: forward_absorb_core
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +2/-1 (3 lines); hunks: -13,6 +13,7; -491,7 +492,7 @@ def _concat_and_cast_mha_k(; symbols: _concat_and_cast_mha_k
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py` modified +14/-3; `python/sglang/srt/models/deepseek_v2.py` modified +13/-4; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` modified +10/-1; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +6/-0; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` modified +2/-1; `python/sglang/srt/layers/quantization/fp8_utils.py` modified +2/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25233 - [Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers

- 链接: https://github.com/sgl-project/sglang/pull/25233
- 状态/时间: merged / 2026-05-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/function_call/deepseekv32_detector.py`；关联提交 `7cb4669a049a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+115/-3，可读 patch 141 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/function_call/deepseekv32_detector.py`；技术摘要: 覆盖「[Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers」；主要实现面是 `python/sglang/srt/function_call/deepseekv32_detector.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #25189 - [perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths

- 链接: https://github.com/sgl-project/sglang/pull/25189
- 状态/时间: merged / 2026-05-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `2df9e8b4b331`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+3/-14，可读 patch 45 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -403,6 +403,7 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +1/-0 (1 lines); hunks: -403,6 +403,7 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -403,6 +403,7 @@ def forward(
+                    # TODO: will check the dtype to be bf16
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25898 - [AMD] Dsv4/pr1 fix run time issue

- 链接: https://github.com/sgl-project/sglang/pull/25898
- 状态/时间: merged / 2026-05-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `af8f66940e9b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 32 个文件，+2523/-129，可读 patch 3203 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Dsv4/pr1 fix run time issue」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[AMD] Dsv4/pr1 fix run time issue」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +39/-1 (40 lines); hunks: -255,6 +255,11 @@ def __init__(; -316,8 +321,41 @@ def forward(; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +39/-1 (40 lines); hunks: -255,6 +255,11 @@ def __init__(; -316,8 +321,41 @@ def forward(; symbols: __init__, forward
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +39/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/jit_kernel/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26395 - [AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x

- 链接: https://github.com/sgl-project/sglang/pull/26395
- 状态/时间: merged / 2026-05-27
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`；关联提交 `bf5bc234310b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+171/-0，可读 patch 172 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`；技术摘要: 覆盖「[AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x」；主要实现面是 `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` added +171/-0 (171 lines); hunks: -0,0 +1,171; symbols: TestDeepSeekR1HiCacheMI35x, setUpClass, tearDownClass, test_gsm8k，涉及 `TestDeepSeekR1HiCacheMI35x, setUpClass, tearDownClass`。
- 代码 diff 细节:
  - `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` added +171/-0 (171 lines); hunks: -0,0 +1,171; symbols: TestDeepSeekR1HiCacheMI35x, setUpClass, tearDownClass, test_gsm8k
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py` added +171/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27188 - [AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage

- 链接: https://github.com/sgl-project/sglang/pull/27188
- 状态/时间: merged / 2026-06-03
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`；关联提交 `cfb7fb4fad03`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+518/-1，可读 patch 619 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`；技术摘要: 覆盖「[AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value，涉及 `get_model_path, get_one_example, get_few_shot_examples`；`test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value，涉及 `get_model_path, get_one_example, get_few_shot_examples`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` added +185/-0 (185 lines); hunks: -0,0 +1,185; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` added +184/-0 (184 lines); hunks: -0,0 +1,184; symbols: get_model_path, get_one_example, get_few_shot_examples, get_answer_value
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` added +185/-0; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` added +184/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`, `test/run_suite.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27720 - [DeepSeek V3] Defer moe finalize and fused it with main stream add

- 链接: https://github.com/sgl-project/sglang/pull/27720
- 状态/时间: merged / 2026-06-13
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `d1a39b0c74ed`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+743/-36，可读 patch 865 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek V3] Defer moe finalize and fused it with main stream add」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeek V3] Defer moe finalize and fused it with main stream add」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +28/-7 (35 lines); hunks: -905,7 +905,18 @@ def forward_normal_dual_stream(; -916,12 +927,22 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream，涉及 `forward_normal_dual_stream`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +28/-7 (35 lines); hunks: -905,7 +905,18 @@ def forward_normal_dual_stream(; -916,12 +927,22 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +28/-7
- 验证与风险: runtime 路径改动集中在 `python/sglang/jit_kernel/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/jit_kernel/csrc/moe/tvm_ffi_utils.h`, `python/sglang/jit_kernel/moe_finalize_fuse_shared.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27243 - [AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests

- 链接: https://github.com/sgl-project/sglang/pull/27243
- 状态/时间: merged / 2026-06-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`；关联提交 `e2540188ce8b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+4/-36，可读 patch 92 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`；技术摘要: 覆盖「[AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` modified +2/-18 (20 lines); hunks: -9,11 +9,6; -39,21 +34,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP2MI35x，涉及 `get_model_path, get_one_example, few_shot_gsm8k`；`test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` modified +2/-18 (20 lines); hunks: -8,11 +8,6; -38,21 +33,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP4MI35x，涉及 `get_model_path, get_one_example, few_shot_gsm8k`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` modified +2/-18 (20 lines); hunks: -9,11 +9,6; -39,21 +34,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP2MI35x
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` modified +2/-18 (20 lines); hunks: -8,11 +8,6; -38,21 +33,10; symbols: get_model_path, get_one_example, few_shot_gsm8k, TestDeepSeekR1MXFP4TP4MI35x
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` modified +2/-18; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py` modified +2/-18
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29142 - [DeepSeek V3] Run routed experts on main stream in dual-stream MoE

- 链接: https://github.com/sgl-project/sglang/pull/29142
- 状态/时间: merged / 2026-06-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `999199f9ff4b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+48/-46，可读 patch 108 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek V3] Run routed experts on main stream in dual-stream MoE」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeek V3] Run routed experts on main stream in dual-stream MoE」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +48/-46 (94 lines); hunks: -936,59 +936,61 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream，涉及 `forward_normal_dual_stream`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +48/-46 (94 lines); hunks: -936,59 +936,61 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +48/-46
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #21531 - [JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel

- 链接: https://github.com/sgl-project/sglang/pull/21531
- 状态/时间: merged / 2026-06-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `714011a40fc3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 12 个文件，+395/-252，可读 patch 722 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +10/-37 (47 lines); hunks: -196,8 +196,11; -208,7 +211,7; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm, dsv2_flashinfer_moe_dual_stream_graph，涉及 `forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +10/-37 (47 lines); hunks: -196,8 +196,11; -208,7 +211,7; symbols: forward, DeepseekV32ForCausalLM, flashinfer_dsv3_router_gemm, dsv2_flashinfer_moe_dual_stream_graph
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +10/-37
- 验证与风险: diff 自带测试面 `sgl-kernel/tests/test_dsv3_router_gemm.py`, `test/registered/jit/benchmark/bench_dsv3_router_gemm.py`, `test/registered/jit/test_dsv3_router_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29452 - Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE"

- 链接: https://github.com/sgl-project/sglang/pull/29452
- 状态/时间: merged / 2026-06-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `7b02eab7a688`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+46/-48，可读 patch 108 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE"」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE"」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +46/-48 (94 lines); hunks: -927,61 +927,59 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream，涉及 `forward_normal_dual_stream`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +46/-48 (94 lines); hunks: -927,61 +927,59 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +46/-48
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #29463 - [DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE

- 链接: https://github.com/sgl-project/sglang/pull/29463
- 状态/时间: merged / 2026-06-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `6bdecb8206b8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+49/-46，可读 patch 111 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +49/-46 (95 lines); hunks: -925,61 +925,64 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream，涉及 `forward_normal_dual_stream`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +49/-46 (95 lines); hunks: -925,61 +925,64 @@ def forward_normal_dual_stream(; symbols: forward_normal_dual_stream
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +49/-46
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #29290 - [AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI

- 链接: https://github.com/sgl-project/sglang/pull/29290
- 状态/时间: merged / 2026-07-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`；关联提交 `548f505cc54a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+226/-2，可读 patch 243 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`；技术摘要: 覆盖「[AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI」；主要实现面是 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` added +202/-0 (202 lines); hunks: -0,0 +1,202; symbols: get_one_example, get_few_shot_examples, get_answer_value, run_gsm8k_benchmark，涉及 `get_one_example, get_few_shot_examples, get_answer_value`。
- 代码 diff 细节:
  - `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` added +202/-0 (202 lines); hunks: -0,0 +1,202; symbols: get_one_example, get_few_shot_examples, get_answer_value, run_gsm8k_benchmark
- 关键代码摘录:

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

- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py` added +202/-0
- 验证与风险: diff 自带测试面 `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31619 - [CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy

- 链接: https://github.com/sgl-project/sglang/pull/31619
- 状态/时间: merged / 2026-07-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `7a896215e765`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+123/-76，可读 patch 309 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「[CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +9/-7 (16 lines); hunks: -77,6 +77,7; -2546,9 +2547,13 @@ def forward(; symbols: forward，涉及 `forward`；`python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +8/-2 (10 lines); hunks: -19,6 +19,7; -565,8 +566,13 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare，涉及 `forward_absorb_prepare`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +9/-7 (16 lines); hunks: -77,6 +77,7; -2546,9 +2547,13 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +8/-2 (10 lines); hunks: -19,6 +19,7; -565,8 +566,13 @@ def forward_absorb_prepare(; symbols: forward_absorb_prepare
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +9/-7; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` modified +8/-2
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/layers/cp/zigzag.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31888 - [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations

- 链接: https://github.com/sgl-project/sglang/pull/31888
- 状态/时间: merged / 2026-07-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `e4a40a71f84c`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 30 个文件，+3837/-52，可读 patch 4635 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`；技术摘要: 覆盖「[DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`。下方保留文件级证据、代码摘录和验证风险。
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

### PR #34693 - [Kernel] Replace dsv3_router_gemm with the unified tiny GEMM

- 链接: https://github.com/sgl-project/sglang/pull/34693
- 状态/时间: merged / 2026-09-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`；关联提交 `cb6dd58fbeca`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+446/-638，可读 patch 1409 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Kernel] Replace dsv3_router_gemm with the unified tiny GEMM」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/utils.py`；技术摘要: 覆盖「[Kernel] Replace dsv3_router_gemm with the unified tiny GEMM」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_common/utils.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +13/-13 (26 lines); hunks: -179,7 +179,6; -195,6 +194,7; symbols: __init__, forward，涉及 `__init__, forward`；`python/sglang/srt/models/deepseek_common/utils.py` modified +17/-0 (17 lines); hunks: -180,3 +180,20 @@ def _get_llama_4_scaling(; symbols: _get_llama_4_scaling, tiny_router_gemm_max_tokens，涉及 `_get_llama_4_scaling, tiny_router_gemm_max_tokens`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +13/-13 (26 lines); hunks: -179,7 +179,6; -195,6 +194,7; symbols: __init__, forward
  - `python/sglang/srt/models/deepseek_common/utils.py` modified +17/-0 (17 lines); hunks: -180,3 +180,20 @@ def _get_llama_4_scaling(; symbols: _get_llama_4_scaling, tiny_router_gemm_max_tokens
- 关键代码摘录:

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

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +13/-13; `python/sglang/srt/models/deepseek_common/utils.py` modified +17/-0
- 验证与风险: diff 自带测试面 `test/registered/kernels/benchmark/gemm/bench_dsv3_router_gemm.py`, `test/registered/kernels/benchmark/gemm/bench_tiny_gemm.py`, `test/registered/kernels/ops/gemm/test_dsv3_router_gemm.py`, `test/registered/kernels/ops/gemm/test_tiny_gemm.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38176 - keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4)

- 链接: https://github.com/sgl-project/sglang/pull/38176
- 状态/时间: merged / 2026-09-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_v2.py`；关联提交 `4f52c9948bc8`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+29/-15，可读 patch 117 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4)」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `python/sglang/srt/models/deepseek_v2.py`；技术摘要: 覆盖「keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4)」；主要实现面是 `python/sglang/srt/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -518,7 +518,9 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_v2.py` modified +3/-1 (4 lines); hunks: -518,7 +518,9 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_v2.py
@@ -518,7 +518,9 @@ def forward(
-            return F.linear(hidden_states, self.weight, None)
+            if _is_cuda or _is_hip:
+                return torch.mm(hidden_states, self.weight.t(), out_dtype=torch.float32)
+            return F.linear(hidden_states.float(), self.weight.float(), None)
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_v2.py` modified +3/-1
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #37762 - [AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8

- 链接: https://github.com/sgl-project/sglang/pull/37762
- 状态/时间: merged / 2026-09-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`；关联提交 `632919e49865`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+1/-0，可读 patch 8 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`；技术摘要: 覆盖「[AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8」；主要实现面是 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` modified +1/-0 (1 lines); hunks: -348,6 +348,7 @@ def _fused_rope_cat_and_cache(; symbols: _fused_rope_cat_and_cache，涉及 `_fused_rope_cat_and_cache`。
- 代码 diff 细节:
  - `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` modified +1/-0 (1 lines); hunks: -348,6 +348,7 @@ def _fused_rope_cat_and_cache(; symbols: _fused_rope_cat_and_cache
- 关键代码摘录:

```diff
diff -- python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py
@@ -348,6 +348,7 @@ def _fused_rope_cat_and_cache(
+        and q_nope_out.shape[-2] == 12
```

- 已读文件:
  - runtime: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` modified +1/-0
- 验证与风险: runtime 路径改动集中在 `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
