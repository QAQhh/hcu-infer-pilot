# sglang DeepSeek V3.1 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `examples/chat_template/tool_chat_template_deepseekv31.jinja` | no direct commit |
| `python/sglang/srt/function_call/deepseekv31_detector.py` | `2667c857a` |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | `9b2e5526f`, `b3718982a`, `70db3398d`, `b56366f82`, `c0b5a180f`, `0d244116d` |
| `python/sglang/srt/models/deepseek_common/__init__.py` | `38dc5839d` |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | `776709efe`, `8b9e9357f`, `38dc5839d` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | `776709efe`, `8b9e9357f` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | `776709efe`, `8b9e9357f`, `38dc5839d` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | `17721b00f`, `5172c3784`, `f23a23cc0`, `76b06bee0`, `8b9e9357f` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | `cd22aa27a`, `c64274c74`, `776709efe` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | `cd22aa27a`, `776709efe` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | `776709efe` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `47b08354a`, `e9d6aefa9`, `cd22aa27a`, `549fbcc86`, `04efd03db`, `010c17a13`, `93433726e` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `47b08354a`, `766d225fc`, `d0d9cecd1`, `894928a95`, `93433726e`, `38dc5839d` |
| `python/sglang/srt/models/deepseek_v2.py` | `2854c89b4`, `79349e551`, `2b0bed239`, `e9d6aefa9`, `574572b21`, `85fe8c679`, `eea9e19c1`, `6b8a6545b`, `d1e95af28`, `944355c66`, `c5d2528bf`, `966ae87d0`, ... (50 total) |
| `test/manual/nightly/test_deepseek_v31_perf.py` | `a0d085c16`, `f35b5da52` |
| `test/registered/8-gpu-models/test_deepseek_v31.py` | `ae9586929`, `912349143`, `655d2c7c2`, `aa2b4f766`, `153c69f63`, `f35b5da52` |
| `test/registered/amd/accuracy/mi30x/test_deepseek_v31_eval_amd.py` | `6fd878b41` |
| `test/registered/amd/perf/mi30x/test_deepseek_v31_perf.py` | `6fd878b41` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 80
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-16 | `47b08354a` | 缺陷修复 | 1. 修复mqa logits chunk bug 2.将FP8 MLA BMM权重在加载时转为BF16，避免forward中重复cast | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-03-31 | `79349e551` | 性能/后端优化 | 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` |
| 2026-03-30 | `2b0bed239` | 性能/后端优化 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |
| 2026-03-22 | `766d225fc` | 性能/后端优化 | Add SGLang CUDA crash API logging inspired by FlashInfer (#20910) | `.claude/skills/debug-cuda-crash/SKILL.md`, `docs/references/environment_variables.md`, `python/sglang/jit_kernel/awq_marlin_repack.py` |
| 2026-03-19 | `574572b21` | 缺陷修复 | [BugFix] bug fix for DeepSeek eagle3 in Attn-DP mode (#20492) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-19 | `85fe8c679` | 性能/后端优化 | [AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256. (#18451) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-19 | `cd22aa27a` | 性能/后端优化 | [CPU] Add FP8 Bmm support (#9744) | `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` |
| 2026-03-18 | `eea9e19c1` | 缺陷修复 | fix lint introduced in #20708 (#20886) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-18 | `6b8a6545b` | 性能/后端优化 | Add Mistral Small 4 (Pixtral) support (#20708) | `benchmark/mmmu/bench_sglang.py`, `benchmark/mmmu/eval_utils.py`, `python/sglang/srt/configs/deepseek_ocr.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-18 | `944355c66` | 性能/后端优化 | [Bugfix] Fix model output corruption caused by EPLB rebalance (Eager and CUDA Graph modes) (#18213) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-17 | `c5d2528bf` | 性能/后端优化 | Revert "[AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars." (#20797) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-17 | `966ae87d0` | 模型支持/运行时入口 | [AMD] avoid correction_bias_dtype dtype convert (#20692) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-17 | `385a35bd1` | 性能/后端优化 | [AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars. (#20647) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-16 | `549fbcc86` | 调度/缓存/PD | [5/N] (Elastic EP) Use GPU P2P to exchange expert weights during EPLB as much as possible (#12068) | `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/eplb/expert_location_updater.py`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-03-14 | `39008955f` | 性能/后端优化 | Revert "[AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars." (#20602) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-14 | `0eea80bc0` | 性能/后端优化 | [AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars. (#20453) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-11 | `9991debde` | 性能/后端优化 | [Feature] Integrate Elastic NIXL-EP into SGLang (#19248) | `docs/advanced_features/expert_parallelism.md`, `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` |
| 2026-03-10 | `9b2e5526f` | 缺陷修复 | [NPU][Bug fix] context parallel bug fix (#19820) | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-03-08 | `17721b00f` | 缺陷修复 | [AMD] Fix Tensor Memory Aliasing (#19928) | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-03-07 | `a0d085c16` | 性能/后端优化 | Adding correct path for module not found error while collecting test (#19778) | `test/manual/nightly/test_deepseek_v31_perf.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/manual/nightly/test_text_models_perf.py` |
| 2026-03-06 | `84aaa6979` | 性能/后端优化 | [AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3 (#19843) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-04 | `5972f97f1` | 模型支持/运行时入口 | Remove naive rotary forward overriding. (#19263) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-02 | `c64274c74` | 性能/后端优化 | Piecewise Cuda Graph set default (#16331) | `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-03-02 | `b3718982a` | 模型支持/运行时入口 | [Feature] add feature mla_ag_after_qlora for dsv3.2 (#19428) | `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-02-27 | `776709efe` | 性能/后端优化 | [3/n] deepseek_v2.py Refactor: Migrate MLA forward method in deepseek_v2.py (#19122) | `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` |
| 2026-02-27 | `5172c3784` | 性能/后端优化 | [AMD] Use fused GEMM with FP8 cast for FP8 prefill (#19422) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-02-25 | `60eeef737` | 性能/后端优化 | [AMD][with CI Fix] support two batch overlapping for mori ep (#19216) | `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations.py`, `python/sglang/srt/batch_overlap/operations_strategy.py` |
| 2026-02-25 | `4a3a787f1` | 缺陷修复 | [Fix] Kimi K2.5 support pp (#18434) | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/kimi_k25.py` |
| 2026-02-25 | `b9cf1563d` | 性能/后端优化 | [ROCm] Optimize Deepseek R1 on MI300X (#18242) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-25 | `c193a52fa` | 模型支持/运行时入口 | [AMD] DSR1/V3 use fp8 bmm in MLA for MI300X (#18624) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-23 | `43f83525c` | 性能/后端优化 | Revert "[AMD] support two batch overlapping for mori ep #17953" (#19161) | `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` |
| 2026-02-21 | `fbb609848` | 性能/后端优化 | [AMD] support two batch overlapping for mori ep (#17953) | `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` |
| 2026-02-20 | `f23a23cc0` | 缺陷修复 | Fix NSA FP8 KV cache path for both-trtllm MHA one-shot (#18931) | `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-02-15 | `0ffd0a399` | 性能/后端优化 | Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 (#18389) | `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-02-15 | `190fa8246` | 缺陷修复 | Fix model loading for DeepSeek-V3.2-AWQ (#16907) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-14 | `ae9586929` | 性能/后端优化 | Enable SGLANG_ENABLE_SPEC_V2 for nightly speculative decoding tests (#18719) | `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py` |
| 2026-02-13 | `8b4c36496` | 性能/后端优化 | refactor context parallel state (#17213) | `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/distributed/parallel_state.py` |
| 2026-02-10 | `e8a2c1338` | 调度/缓存/PD | Deepseekv32 compatibility with transformers v5 (#18297) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-02-04 | `6fd878b41` | 性能/后端优化 | [AMD] Add kimi mi35x nightly test, folder organization and several stability fixes (#17895) | `.github/workflows/nightly-test-amd.yml`, `python/sglang/test/nightly_utils.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py` |
| 2026-02-01 | `9ac4dcada` | 性能/后端优化 | [Tiny] Fix grammar in shared experts fusion log messages (#18043) | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe_lite.py` |
| 2026-01-31 | `04efd03db` | 缺陷修复 | Fix OOM in DeepSeek weight loading by deferring dict(weights) materialization (#17744) | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-01-31 | `d0d9cecd1` | 缺陷修复 | Fix cuBLAS >=12.9 detection for cu12/cu13 package naming (#17766) | `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/utils/common.py` |
| 2026-01-30 | `70db3398d` | 模型支持/运行时入口 | [NPU] enhance accuracy for model kimi-vl-a3b-instruct (#17480) | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `test/registered/ascend/vlm_models/test_ascend_kimi_vl_a3b_instruct.py` |
| 2026-01-30 | `c35aa0238` | 性能/后端优化 | [CPU][INT4] Add INT4 kernels for CPU (#8226) | `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/unquant.py` |
| 2026-01-30 | `71e4d3b6b` | 性能/后端优化 | [Intel GPU] fix import error to run DeepSeek-V2-Lite model with BF16 on XPU (#10858) | `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py` |
| 2026-01-30 | `858dc80af` | 缺陷修复 | [Intel GPU] fix device in DeepseekScalingRotaryEmbedding to run DeepSeek-V2-Lite BF16 on XPU (#10021) | `python/sglang/srt/layers/rotary_embedding.py` |
| 2026-01-29 | `f1384f529` | 性能/后端优化 | Integration mori backend for EP a2a data communication (#17012) | `docs/advanced_features/expert_parallelism.md`, `docs/references/environment_variables.md`, `python/sglang/srt/layers/attention/utils.py` |
| 2026-01-28 | `f8636fbb2` | 性能/后端优化 | [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI (#17523) | `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` |
| 2026-01-26 | `b56366f82` | 性能/后端优化 | [NPU]DeepSeek-V3.2 support npu mlaprolog (#15381) | `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-01-25 | `912349143` | 调度/缓存/PD | A few updates to the night tests (#17694) | `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-24 | `2c2c4e446` | 性能/后端优化 | [NVIDIA] Add flashinfer all-to-all MOE dispatcher (#14668) | `docs/advanced_features/expert_parallelism.md`, `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-01-24 | `894928a95` | 模型支持/运行时入口 | Refactor: Extract DeepSeek common utilities into shared module (#16969) | `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-23 | `010c17a13` | 模型支持/运行时入口 | [Refactor] Algebraic data type for nextn config + some basic refactors (#17347) | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-01-23 | `c0b5a180f` | 缺陷修复 | [NPU]bugfix: fix for dsv3.2 and dsvl2 (#17007) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-21 | `6ea491e43` | 模型支持/运行时入口 | Overlap shared experts with deepep dispatch for single batch overlap on Blackwell (#17289) | `docs/references/environment_variables.md`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/environ.py` |
| 2026-01-20 | `d97066d20` | 模型支持/运行时入口 | Use attn_tp_group for all reduce in token embedding (#17403) | `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py`, `python/sglang/srt/models/deepseek_nextn.py` |
| 2026-01-20 | `76b06bee0` | 性能/后端优化 | [New Model] GLM4.7-Flash (#17247) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-01-19 | `a3addd620` | 性能/后端优化 | [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests (#17179) | `.github/workflows/nightly-test-amd.yml`, `scripts/ci/amd_ci_exec.sh`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` |
| 2026-01-18 | `93433726e` | 模型支持/运行时入口 | [Refactor] Split out deepseek v2 weight loader function into mixin (#16649) | `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_nextn.py` |
| 2026-01-17 | `8b9e9357f` | 模型支持/运行时入口 | [2/n] deepseek_v2.py Refactor: Migrate MHA forward method in deepseek_v2.py (#16817) | `python/sglang/srt/model_executor/forward_batch_deepseek_mha_mixin.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` |
| 2026-01-17 | `82a1b645b` | 性能/后端优化 | [DeepSeek V3.1/V3.2] Optimize fused moe configs for H20 & H20-3E based on swapab (#17133) | `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128]_down.json` |
| 2026-01-15 | `655d2c7c2` | 缺陷修复 | fix: adding matrix partitioning for h200 and b200 nightly tests (#17091) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-14 | `aa2b4f766` | 缺陷修复 | fix: renaming test file and job names + skip blocking llama4 nightly (#16971) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-13 | `b025cff44` | 性能/后端优化 | [AMD] Add AMD CI registration (1-gpu unit test) to nightly CI. (#16941) | `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` |
| 2026-01-13 | `afe285f7b` | 性能/后端优化 | [AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant (#16841) | `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py` |
| 2026-01-10 | `d27f16f38` | 性能/后端优化 | Fix EPLB + FP4 Quantization Compatibility Issue (#13715) | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-09 | `20abaee26` | 调度/缓存/PD | [DSv32] Overlap indexer weights_proj during dual_stream decode (#16637) | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-07 | `4935344fc` | 性能/后端优化 | [AMD] Fix aiter page-size handling, DeepSeek MLA tuple inputs, and HiCache/FA3 decode-backend override (#16531) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/server_args.py` |
| 2026-01-08 | `38dc5839d` | 模型支持/运行时入口 | [1/n]deepseek_v2.py Refactor: attention backend handlers and forward method definition (#16306) | `python/sglang/srt/models/deepseek_common/__init__.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` |
| 2026-01-07 | `153c69f63` | 模型支持/运行时入口 | [CI] Enable dpsk v31 test on nightly H200 (#16660) | `test/registered/8-gpu-models/test_deepseek_v31.py` |
| 2026-01-03 | `bb23a8fe7` | 性能/后端优化 | [Tiny]Remove progress bar for fp8 ue8m0 quant when unneeded (#16177) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-02 | `0d244116d` | 性能/后端优化 | [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache (#13959) | `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2025-12-31 | `2667c857a` | 缺陷修复 | Fix DeepSeekV31's structural tag trigger (#13394) | `python/sglang/srt/function_call/deepseekv31_detector.py` |
| 2025-12-31 | `f35b5da52` | 性能/后端优化 | [CI] Append test variant name to markdown report header in nightly test (#16166) | `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py` |
| 2025-12-30 | `5e20e7a60` | 性能/后端优化 | [AMD CI] Organize AMD nightly perf test files (#16114) | `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/test_deepseek_v31_perf.py`, `test/registered/amd/test_deepseek_v3_perf.py` |
| 2025-12-29 | `2ec6fa3c5` | 调度/缓存/PD | feat PD: add eagle3 support for DeepSeek V3 in EP mode (#14280) | `python/sglang/srt/models/deepseek_v2.py` |

## Per-Commit Audit Cards

### Commit `47b08354a` - 1. 修复mqa logits chunk bug 2.将FP8 MLA BMM权重在加载时转为BF16，避免forward中重复cast

- Full hash: `47b08354ad96b97bb18c738bac89349ee9cec5bc`
- Date/author: 2026-04-16 / niuhb
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2854c89b4` - 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化

- Full hash: `2854c89b4ee838989dea9b7e403840dfcf4d7116`
- Date/author: 2026-04-10 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `79349e551` - 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug

- Full hash: `79349e5510a7485abc9102a64f972c07d2f8790b`
- Date/author: 2026-03-31 / niuhb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/deepseek_v2.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/setup_hip.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/setup_hip.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2b0bed239` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- Full hash: `2b0bed23943bee2e93916979aabc272268a11a1c`
- Date/author: 2026-03-30 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e9d6aefa9` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- Full hash: `e9d6aefa947699a1edc971ecc2e3fdd2053f525f`
- Date/author: 2026-03-30 / lizhigong
- Auto category: 性能/后端优化
- Main files: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README_DCU.md`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py` 等 25 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/server_args.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `766d225fc` - Add SGLang CUDA crash API logging inspired by FlashInfer (#20910)

- Full hash: `766d225fccf01bdd41a35dc95300952b511454de`
- Date/author: 2026-03-22 / Xiaoyu Zhang
- Auto category: 性能/后端优化
- Main files: `.claude/skills/debug-cuda-crash/SKILL.md`, `docs/references/environment_variables.md`, `python/sglang/jit_kernel/awq_marlin_repack.py`, `python/sglang/jit_kernel/debug_utils.py`, `python/sglang/jit_kernel/flash_attention_v4.py`, `python/sglang/jit_kernel/fused_store_index_cache.py`, `python/sglang/jit_kernel/gptq_marlin.py`, `python/sglang/jit_kernel/gptq_marlin_repack.py` 等 34 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - other: `python/sglang/srt/layers/linear.py`; `python/sglang/srt/layers/utils/multi_platform.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/kimi_vl_moonvit.py`; `python/sglang/srt/models/minimax_m2.py`
  - runtime-perf: `.claude/skills/debug-cuda-crash/SKILL.md`; `python/sglang/jit_kernel/awq_marlin_repack.py`; `python/sglang/jit_kernel/debug_utils.py`; `python/sglang/jit_kernel/flash_attention_v4.py`; `python/sglang/jit_kernel/fused_store_index_cache.py`; `python/sglang/jit_kernel/gptq_marlin.py`; `python/sglang/jit_kernel/gptq_marlin_repack.py`; `python/sglang/jit_kernel/hicache.py` 等 27 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `574572b21` - [BugFix] bug fix for DeepSeek eagle3 in Attn-DP mode (#20492)

- Full hash: `574572b21bf7a26c66ca063cd52a08c225e6e964`
- Date/author: 2026-03-19 / khalilzhk
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `85fe8c679` - [AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256. (#18451)

- Full hash: `85fe8c6793a0b2bf8d5b2e98c88a8630515b0ac6`
- Date/author: 2026-03-19 / Matti Varjokallio
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `cd22aa27a` - [CPU] Add FP8 Bmm support (#9744)

- Full hash: `cd22aa27a941d10ecd3df1e2df69faa84454b443`
- Date/author: 2026-03-19 / blzheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/longcat_flash.py`, `python/sglang/srt/models/longcat_flash_nextn.py`, `sgl-kernel/csrc/cpu/bmm.cpp`, `sgl-kernel/csrc/cpu/gemm.h` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
  - runtime-perf: `python/sglang/srt/models/bailing_moe_linear.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `sgl-kernel/csrc/cpu/bmm.cpp`; `sgl-kernel/csrc/cpu/gemm.h`; `sgl-kernel/csrc/cpu/gemm_fp8.cpp` 等 10 个文件
  - tests: `test/srt/cpu/test_bmm.py`; `test/srt/cpu/test_qkv_proj_with_rope.py`; `test/srt/run_suite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `eea9e19c1` - fix lint introduced in #20708 (#20886)

- Full hash: `eea9e19c135524d4ba76328a00770bc68b5f89ad`
- Date/author: 2026-03-18 / Qiaolin Yu
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `6b8a6545b` - Add Mistral Small 4 (Pixtral) support (#20708)

- Full hash: `6b8a6545b231e175a9534ee50ed57fcd6d5b75e5`
- Date/author: 2026-03-18 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `benchmark/mmmu/bench_sglang.py`, `benchmark/mmmu/eval_utils.py`, `python/sglang/srt/configs/deepseek_ocr.py`, `python/sglang/srt/configs/deepseekvl2.py`, `python/sglang/srt/configs/janus_pro.py`, `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/mmmu/bench_sglang.py`; `benchmark/mmmu/eval_utils.py`
  - other: `python/sglang/srt/function_call/mistral_detector.py`; `python/sglang/srt/multimodal/processors/pixtral.py`; `python/sglang/srt/parser/reasoning_parser.py`; `python/sglang/srt/utils/hf_transformers_utils.py`; `python/sglang/srt/utils/mistral_utils.py`
  - runtime-model: `python/sglang/srt/configs/deepseek_ocr.py`; `python/sglang/srt/configs/deepseekvl2.py`; `python/sglang/srt/configs/janus_pro.py`; `python/sglang/srt/configs/jet_nemotron.py`; `python/sglang/srt/entrypoints/openai/protocol.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/mistral_large_3_eagle.py` 等 10 个文件
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d1e95af28` - Upgrade transformers==5.3.0 (#17784)

- Full hash: `d1e95af282068a751ee6a8b60a0ae2a90c464819`
- Date/author: 2026-03-18 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py` 等 88 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/layers/rotary_embedding/factory.py`; `python/sglang/srt/managers/tokenizer_manager.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/configs/internvl.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/arcee.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/commandr.py`; `python/sglang/srt/models/dbrx.py` 等 54 个文件
  - runtime-perf: `python/sglang/srt/models/afmoe.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/ernie45_moe_vl.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/granitemoe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 15 个文件
  - tests: `python/sglang/test/runners.py`; `test/registered/core/test_score_api.py`; `test/registered/quant/test_awq.py`; `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/vlm/test_vlm_input_format.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `944355c66` - [Bugfix] Fix model output corruption caused by EPLB rebalance (Eager and CUDA Graph modes) (#18213)

- Full hash: `944355c66ffa4b4738258fe44eb083aaf6a6536e`
- Date/author: 2026-03-18 / lviy
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c5d2528bf` - Revert "[AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars." (#20797)

- Full hash: `c5d2528bff98f4ba8c1289547cf626d2aa735395`
- Date/author: 2026-03-17 / Qiaolin Yu
- Auto category: 性能/后端优化
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/base.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `966ae87d0` - [AMD] avoid correction_bias_dtype dtype convert (#20692)

- Full hash: `966ae87d021f1a902240149937939082faef735c`
- Date/author: 2026-03-17 / AMD-yanfeiwang
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `385a35bd1` - [AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars. (#20647)

- Full hash: `385a35bd118d2e420be1fd6978c703d22a3bcc77`
- Date/author: 2026-03-17 / Duyi-Wang
- Auto category: 性能/后端优化
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/base.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `549fbcc86` - [5/N] (Elastic EP) Use GPU P2P to exchange expert weights during EPLB as much as possible (#12068)

- Full hash: `549fbcc864c24bc7d98b6ac33981967b79a67c3c`
- Date/author: 2026-03-16 / Xun Sun
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/eplb/expert_location_updater.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/elastic_ep/expert_backup_client.py`; `python/sglang/srt/eplb/expert_location_updater.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `39008955f` - Revert "[AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars." (#20602)

- Full hash: `39008955ffc52dc5da783640ca7ef5c148daa430`
- Date/author: 2026-03-14 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/base.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0eea80bc0` - [AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars. (#20453)

- Full hash: `0eea80bc001c991c9323ba7063f480fd4ae94c21`
- Date/author: 2026-03-14 / Duyi-Wang
- Auto category: 性能/后端优化
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/base.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9991debde` - [Feature] Integrate Elastic NIXL-EP into SGLang (#19248)

- Full hash: `9991debde37b0ea1ecca8e13f0aef24c6b498d17`
- Date/author: 2026-03-11 / Yoray Zack
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/expert_parallelism.md`, `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/distributed/utils.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/eplb_algorithms/__init__.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/expert_parallelism.md`; `docs/advanced_features/server_arguments.md`
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/eplb_algorithms/__init__.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/distributed/utils.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/nixl.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/fp8.py` 等 9 个文件
  - tests: `test/manual/ep/test_nixl_ep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9b2e5526f` - [NPU][Bug fix] context parallel bug fix (#19820)

- Full hash: `9b2e5526fb85d4eab71cd380f526b59f5719cc18`
- Date/author: 2026-03-10 / liupeng374
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `17721b00f` - [AMD] Fix Tensor Memory Aliasing  (#19928)

- Full hash: `17721b00fddfb85e21af80e0b23ef249d1bfe46a`
- Date/author: 2026-03-08 / Bingxu Chen
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a0d085c16` - Adding correct path for module not found error while collecting test (#19778)

- Full hash: `a0d085c16d5a267a3657c40d3b35b474ed548f81`
- Date/author: 2026-03-07 / shubham singhal
- Auto category: 性能/后端优化
- Main files: `test/manual/nightly/test_deepseek_v31_perf.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/manual/nightly/test_text_models_perf.py`, `test/manual/nightly/test_vlms_perf.py`, `test/manual/test_two_batch_overlap.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/manual/nightly/test_deepseek_v31_perf.py`; `test/manual/nightly/test_deepseek_v32_perf.py`; `test/manual/nightly/test_text_models_perf.py`; `test/manual/nightly/test_vlms_perf.py`; `test/manual/test_two_batch_overlap.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `84aaa6979` - [AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3 (#19843)

- Full hash: `84aaa69795f3588c0d384e034d060d4436d28672`
- Date/author: 2026-03-06 / inkcherry
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `5972f97f1` - Remove naive rotary forward overriding. (#19263)

- Full hash: `5972f97f11c0886d6d6b1790bc2de6e3f228e682`
- Date/author: 2026-03-04 / Jue Wang
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c64274c74` - Piecewise Cuda Graph set default (#16331)

- Full hash: `c64274c746f210497c45bd1600d2046faf7f4b10`
- Date/author: 2026-03-02 / Yuwei An
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/awq.py` 等 34 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/compilation/compile.py`; `python/sglang/srt/compilation/piecewise_context_manager.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/minicpm3.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/flashinfer_backend.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/qwen2_moe.py`
  - tests: `test/manual/nightly/test_vlms_piecewise_cuda_graph.py`; `test/manual/nightly/test_vlms_vit_cuda_graph.py`; `test/manual/piecewise_cudagraph/test_disaggregation_piecewise_cuda_graph.py`; `test/registered/mla/test_mla_deepseek_v3.py`; `test/registered/models/test_generation_models.py`; `test/registered/models/test_kimi_linear_models_pcg.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/piecewise_cuda_graph/test_piecewise_cuda_graph_2_gpu.py` 等 13 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b3718982a` - [Feature] add feature mla_ag_after_qlora for dsv3.2 (#19428)

- Full hash: `b3718982a1b41afcc58921c2933348bc23560604`
- Date/author: 2026-03-02 / JiaruiChang5268
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/layers/communicator.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `776709efe` - [3/n] deepseek_v2.py Refactor: Migrate MLA forward method in deepseek_v2.py (#19122)

- Full hash: `776709efe89390599302a244f6ab1626f02ba9ff`
- Date/author: 2026-02-27 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/srt/cpu/test_qkv_proj_with_rope.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py`
  - tests: `test/srt/cpu/test_qkv_proj_with_rope.py`; `test/srt/cpu/test_rope.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5172c3784` - [AMD] Use fused GEMM with FP8 cast for FP8 prefill (#19422)

- Full hash: `5172c378456fa9735ba6429a2ca7688d1152d256`
- Date/author: 2026-02-27 / Thomas Wang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `60eeef737` - [AMD][with CI Fix] support two batch overlapping for mori ep (#19216)

- Full hash: `60eeef73701a5e5d79b28bd4b9b6d552c576854f`
- Date/author: 2026-02-25 / billishyahao
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations.py`, `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/__init__.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/server_arguments.md`
  - other: `python/sglang/srt/batch_overlap/operations.py`; `python/sglang/srt/batch_overlap/operations_strategy.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`
  - tests: `python/sglang/test/bench_one_batch_server_internal.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4a3a787f1` - [Fix] Kimi K2.5 support pp (#18434)

- Full hash: `4a3a787f1e1ff3d1a5efd9eb0b7ffa00eb53d9a8`
- Date/author: 2026-02-25 / lw9527
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b9cf1563d` - [ROCm] Optimize Deepseek R1 on MI300X (#18242)

- Full hash: `b9cf1563de979458e5c831ccfe8f5bfd47a55d01`
- Date/author: 2026-02-25 / Chen, Zhentao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c193a52fa` - [AMD] DSR1/V3 use fp8 bmm in MLA for MI300X (#18624)

- Full hash: `c193a52fa263dbba15173830332a073020340fcd`
- Date/author: 2026-02-25 / Chen, Zhentao
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `43f83525c` - Revert "[AMD] support two batch overlapping for mori ep #17953" (#19161)

- Full hash: `43f83525c0a294a7a1d65e8ee46e1e73d1363000`
- Date/author: 2026-02-23 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/server_arguments.md`
  - other: `python/sglang/srt/batch_overlap/operations_strategy.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`
  - tests: `python/sglang/test/bench_one_batch_server_internal.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fbb609848` - [AMD] support two batch overlapping for mori ep (#17953)

- Full hash: `fbb60984872ee69d868b595f81c0155b15601de5`
- Date/author: 2026-02-21 / billishyahao
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/server_arguments.md`
  - other: `python/sglang/srt/batch_overlap/operations_strategy.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`
  - tests: `python/sglang/test/bench_one_batch_server_internal.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f23a23cc0` - Fix NSA FP8 KV cache path for both-trtllm MHA one-shot (#18931)

- Full hash: `f23a23cc05fca67d296426e4acb9ce69524f26e4`
- Date/author: 2026-02-20 / Mohammad Miadh Angkad
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0ffd0a399` - Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 (#18389)

- Full hash: `0ffd0a3995e537c2ec6f450cbb7d4b4db44550aa`
- Date/author: 2026-02-15 / Rain Jiang
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/layers/attention/utils.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/models/deepseek_v2.py` 等 10 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/server_arguments.md`; `docs/basic_usage/deepseek_v32.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/layers/attention/trtllm_mla_backend.py`; `python/sglang/srt/layers/attention/utils.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
  - tests: `test/registered/hicache/test_nsa_pool_host_unit.py`; `test/registered/kernels/test_nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `07a24f1a3` - update pre-commit config (#18860)

- Full hash: `07a24f1a3846c4186e82ffc2bc43990ba6c0babc`
- Date/author: 2026-02-16 / SoluMilken
- Auto category: 性能/后端优化
- Main files: `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py`, `benchmark/fla/benchmark_layernorm_gated.py`, `benchmark/tip_suggestion/bench_other.py`, `benchmark/tip_suggestion/bench_sglang.py`, `benchmark/tip_suggestion/lmql_funcs.py`, `examples/runtime/engine/save_remote_state.py` 等 100 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/lint.yml`
  - docs-bench: `benchmark/fla/benchmark_layernorm_gated.py`; `benchmark/tip_suggestion/bench_other.py`; `benchmark/tip_suggestion/bench_sglang.py`; `benchmark/tip_suggestion/lmql_funcs.py`; `examples/runtime/engine/save_remote_state.py`; `examples/runtime/engine/save_sharded_state.py`
  - other: `python/sglang/srt/compilation/weak_ref_tensor.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/function_call/base_format_detector.py`; `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/metrics/collector.py`; `python/sglang/srt/metrics/utils.py` 等 25 个文件
  - runtime-model: `.pre-commit-config.yaml`; `python/sglang/srt/checkpoint_engine/checkpoint_engine_worker.py`; `python/sglang/srt/configs/exaone.py`; `python/sglang/srt/configs/falcon_h1.py`; `python/sglang/srt/entrypoints/openai/serving_responses.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/deepseek_nextn.py` 等 34 个文件
  - runtime-perf: `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `python/sglang/jit_kernel/include/sgl_kernel/type.cuh`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/linear/seg_la.py`; `python/sglang/srt/layers/attention/wave_ops/prefill_attention.py`; `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py` 等 27 个文件
  - tests: `sgl-kernel/tests/test_per_token_group_quant_8bit.py`; `test/manual/test_vlm_accuracy.py`; `test/registered/attention/test_triton_sliding_window.py`; `test/registered/layers/test_fla_layernorm_guard.py`; `test/registered/quant/test_awq_dequant.py`; `test/srt/cpu/test_norm.py`; `test/srt/cpu/test_qwen3.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `190fa8246` - Fix model loading for DeepSeek-V3.2-AWQ (#16907)

- Full hash: `190fa8246fbc021034b8b2725ce30df11a96915e`
- Date/author: 2026-02-15 / Guangda Liu
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `ae9586929` - Enable SGLANG_ENABLE_SPEC_V2 for nightly speculative decoding tests (#18719)

- Full hash: `ae958692927509723ada6e33f368bdba148f1654`
- Date/author: 2026-02-14 / Kangyan-Zhou
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/test_utils.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py` 等 10 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/test_utils.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py` 等 10 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `8b4c36496` - refactor context parallel state  (#17213)

- Full hash: `8b4c364960e6cccecd72edcdf47f54d06f3623c4`
- Date/author: 2026-02-13 / dongjiyingdjy
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_nsa_cp.py` 等 27 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/server_arguments.md`; `docs/basic_usage/deepseek_v32.md`
  - other: `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/communicator_nsa_cp.py`; `python/sglang/srt/managers/data_parallel_controller.py`
  - runtime-model: `python/sglang/srt/entrypoints/engine.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker.py`; `python/sglang/srt/speculative/eagle_worker_v2.py` 等 13 个文件
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa/utils.py`; `python/sglang/srt/layers/dp_attention.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_dp_attn_mixin.py`; `python/sglang/srt/model_executor/cuda_graph_runner.py`
  - tests: `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/distributed/test_parallel_state.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e8a2c1338` - Deepseekv32 compatibility with transformers v5 (#18297)

- Full hash: `e8a2c133807cc25d872be19ab35110c79df77efd`
- Date/author: 2026-02-10 / Xinyuan Tong
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6fd878b41` - [AMD] Add kimi mi35x nightly test, folder organization and several stability fixes (#17895)

- Full hash: `6fd878b41df0153bd28f0185920e1b2d9dcc7480`
- Date/author: 2026-02-04 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd.yml`, `python/sglang/test/nightly_utils.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v31_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_dp_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_mtp_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_tc_eval_amd.py` 等 34 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - tests: `python/sglang/test/nightly_utils.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v31_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_dp_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_mtp_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_tc_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py` 等 33 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `9ac4dcada` - [Tiny] Fix grammar in shared experts fusion log messages (#18043)

- Full hash: `9ac4dcada4bd77a18e6f3d3efcd1906f705b235d`
- Date/author: 2026-02-01 / Mohammad Miadh Angkad
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe_lite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/models/glm4_moe_lite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `04efd03db` - Fix OOM in DeepSeek weight loading by deferring dict(weights) materialization (#17744)

- Full hash: `04efd03dbf0f40c2c847e2dcaba84faa8dfcb128`
- Date/author: 2026-01-31 / jeff
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d0d9cecd1` - Fix cuBLAS >=12.9 detection for cu12/cu13 package naming (#17766)

- Full hash: `d0d9cecd1b34ead4caf506e0481011603ac87bcc`
- Date/author: 2026-01-31 / Mohammad Miadh Angkad
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/utils/common.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/models/deepseek_common/utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `70db3398d` - [NPU] enhance accuracy for model kimi-vl-a3b-instruct (#17480)

- Full hash: `70db3398d196861a9acf0405440f3ffa71fd6607`
- Date/author: 2026-01-30 / McZyWu
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `test/registered/ascend/vlm_models/test_ascend_kimi_vl_a3b_instruct.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`
  - tests: `test/registered/ascend/vlm_models/test_ascend_kimi_vl_a3b_instruct.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c35aa0238` - [CPU][INT4] Add INT4 kernels for CPU  (#8226)

- Full hash: `c35aa0238c730e68810b422bcc91d2a0790538ea`
- Date/author: 2026-01-30 / jianan-gu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/models/deepseek_v2.py`, `sgl-kernel/csrc/cpu/gemm.h`, `sgl-kernel/csrc/cpu/gemm_int4.cpp`, `sgl-kernel/csrc/cpu/moe.cpp` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/amx_utils.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/unquant.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`; `sgl-kernel/csrc/cpu/gemm.h`; `sgl-kernel/csrc/cpu/gemm_int4.cpp`; `sgl-kernel/csrc/cpu/moe.cpp`; `sgl-kernel/csrc/cpu/moe_int4.cpp`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
  - tests: `test/srt/cpu/test_gemm.py`; `test/srt/cpu/test_moe.py`; `test/srt/cpu/test_shared_expert.py`; `test/srt/cpu/utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `71e4d3b6b` - [Intel GPU] fix import error to run DeepSeek-V2-Lite model with BF16 on XPU (#10858)

- Full hash: `71e4d3b6bc467c0c6a45f2beb9494c0209ebe374`
- Date/author: 2026-01-30 / Polisetty V R K Jyothendra Varma
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `858dc80af` - [Intel GPU] fix device in DeepseekScalingRotaryEmbedding to run DeepSeek-V2-Lite BF16 on XPU (#10021)

- Full hash: `858dc80aff167cc49ec8b0e08c21459a5217e171`
- Date/author: 2026-01-30 / Polisetty V R K Jyothendra Varma
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/rotary_embedding.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `f1384f529` - Integration mori backend for EP a2a data communication (#17012)

- Full hash: `f1384f5293ce11c659b39743592f466b14612375`
- Date/author: 2026-01-29 / kk
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/expert_parallelism.md`, `docs/references/environment_variables.md`, `python/sglang/srt/layers/attention/utils.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/rocm_moe_utils.py`, `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/expert_parallelism.md`; `docs/references/environment_variables.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/utils.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/rocm_moe_utils.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/managers/scheduler_metrics_mixin.py`
  - tests: `python/sglang/test/test_utils.py`; `test/srt/ep/test_moriep_small.py`; `test/srt/run_suite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f8636fbb2` - [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI (#17523)

- Full hash: `f8636fbb253a83d268ffa1636eac4e111966376c`
- Date/author: 2026-01-28 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py` 等 27 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok2_eval_mi35x.py` 等 26 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `b56366f82` - [NPU]DeepSeek-V3.2 support npu mlaprolog (#15381)

- Full hash: `b56366f8275a636218a9c32ed551c9543146ba31`
- Date/author: 2026-01-26 / lawtherWu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`; `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`; `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `912349143` - A few updates to the night tests (#17694)

- Full hash: `9123491430c9cc38b6796cbf3ad3ef07e948e8c9`
- Date/author: 2026-01-25 / Kangyan-Zhou
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/accuracy_test_runner.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `2c2c4e446` - [NVIDIA] Add flashinfer all-to-all MOE dispatcher (#14668)

- Full hash: `2c2c4e446b99c529896b3377b24e1b48b6a52e61`
- Date/author: 2026-01-24 / Trevor Morris
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/expert_parallelism.md`, `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`, `python/sglang/srt/layers/moe/token_dispatcher/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/layers/moe/token_dispatcher/flashinfer_utils.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/expert_parallelism.md`; `docs/references/environment_variables.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/base.py`; `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`; `python/sglang/srt/layers/moe/token_dispatcher/flashinfer_utils.py`; `python/sglang/srt/layers/moe/token_dispatcher/standard.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/modelopt_quant.py` 等 9 个文件
  - tests: `python/sglang/test/test_flashinfer_dispatcher.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `894928a95` - Refactor: Extract DeepSeek common utilities into shared module (#16969)

- Full hash: `894928a9512440974032ce49e058d8c2c169b1cf`
- Date/author: 2026-01-24 / Ananya
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `010c17a13` - [Refactor] Algebraic data type for nextn config + some basic refactors (#17347)

- Full hash: `010c17a133fa7443f83a18dfff1218e40dae335c`
- Date/author: 2026-01-23 / Jerry Ji
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c0b5a180f` - [NPU]bugfix: fix for dsv3.2 and dsvl2 (#17007)

- Full hash: `c0b5a180febef52bba4f1f3e974d364f6c96a10f`
- Date/author: 2026-01-23 / JiaruiChang5268
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/ascend/llm_models/test_ascend_deepseek_v3_2_exp_w8a8.py`, `test/registered/ascend/vlm_models/test_ascend_deepseek_vl2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`
  - tests: `test/registered/ascend/llm_models/test_ascend_deepseek_v3_2_exp_w8a8.py`; `test/registered/ascend/vlm_models/test_ascend_deepseek_vl2.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6ea491e43` - Overlap shared experts with deepep dispatch for single batch overlap on Blackwell (#17289)

- Full hash: `6ea491e4392d8cb4bcf38c21430eef594ed62eb6`
- Date/author: 2026-01-21 / Baizhou Zhang
- Auto category: 模型支持/运行时入口
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - other: `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d97066d20` - Use attn_tp_group for all reduce in token embedding (#17403)

- Full hash: `d97066d209b97f7a9808cf9c1dfa4bee4163c23b`
- Date/author: 2026-01-20 / Ke Bao
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/vocab_parallel_embedding.py`
  - runtime-model: `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/dp_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `76b06bee0` - [New Model] GLM4.7-Flash (#17247)

- Full hash: `76b06bee03e8d5e5fbd57dfbdbc80688705988ac`
- Date/author: 2026-01-20 / Qiaolin Yu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/glm4_moe_lite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a3addd620` - [AMD] Add DeepSeek-V3.2 and VLMs model in nightly tests (#17179)

- Full hash: `a3addd6203cab13d1b61e7df555722104d03591c`
- Date/author: 2026-01-19 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd.yml`, `scripts/ci/amd_ci_exec.sh`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/test_vlms_mmmu_eval_amd.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - other: `scripts/ci/amd_ci_exec.sh`
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`; `test/registered/amd/accuracy/test_gsm8k_eval_amd.py`; `test/registered/amd/accuracy/test_vlms_mmmu_eval_amd.py`; `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py`; `test/registered/amd/perf/mi35x/test_deepseek_v32_basic_perf_mi35x.py`; `test/registered/amd/perf/mi35x/test_deepseek_v32_mtp_perf_mi35x.py`; `test/registered/amd/perf/mi35x/test_grok1_int4_perf_mi35x.py` 等 16 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `93433726e` - [Refactor] Split out deepseek v2 weight loader function into mixin (#16649)

- Full hash: `93433726eb72d7e11d0ff692e6101955c99cafbc`
- Date/author: 2026-01-18 / Jerry Ji
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `8b9e9357f` - [2/n] deepseek_v2.py Refactor: Migrate MHA forward method in deepseek_v2.py (#16817)

- Full hash: `8b9e9357fe2850f17e4ca5a64d9387f2f02619d8`
- Date/author: 2026-01-17 / Baizhou Zhang
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/model_executor/forward_batch_deepseek_mha_mixin.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_deepseek_mha_mixin.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `82a1b645b` - [DeepSeek V3.1/V3.2] Optimize fused moe configs for H20 & H20-3E based on swapab (#17133)

- Full hash: `82a1b645bad31c3071220c1acd4171209c524013`
- Date/author: 2026-01-17 / Yongfei Xu
- Auto category: 性能/后端优化
- Main files: `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20-3e,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20-3e,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20-3e,dtype=fp8_w8a8,block_shape=[128, 128].json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=257,N=256,device_name=NVIDIA_H20-3e,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `655d2c7c2` - fix: adding matrix partitioning for h200 and b200 nightly tests (#17091)

- Full hash: `655d2c7c2aa42d7b097498a2c0d48cd697aeda61`
- Date/author: 2026-01-15 / Douglas Yang
- Auto category: 缺陷修复
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py`; `test/registered/8-gpu-models/test_minimax_m2.py` 等 10 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `aa2b4f766` - fix: renaming test file and job names + skip blocking llama4 nightly (#16971)

- Full hash: `aa2b4f76617929469acb3a7bbd6052e718d00ab3`
- Date/author: 2026-01-14 / Douglas Yang
- Auto category: 缺陷修复
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py`, `test/registered/8-gpu-models/test_minimax_m2.py` 等 10 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py`; `test/registered/8-gpu-models/test_minimax_m2.py`; `test/registered/8-gpu-models/test_mistral_large3.py` 等 9 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `b025cff44` - [AMD] Add AMD CI registration (1-gpu unit test) to nightly CI.  (#16941)

- Full hash: `b025cff441e187646b5bed6dbaf6152a1dd11522`
- Date/author: 2026-01-13 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_grok2_eval_mi35x.py`, `test/registered/amd/accuracy/test_deepseek_r1_eval_amd.py`, `test/registered/amd/accuracy/test_deepseek_v31_eval_amd.py` 等 39 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok2_eval_mi35x.py`; `test/registered/amd/accuracy/test_deepseek_r1_eval_amd.py`; `test/registered/amd/accuracy/test_deepseek_v31_eval_amd.py`; `test/registered/amd/accuracy/test_gpt_oss_eval_amd.py` 等 38 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `afe285f7b` - [AMD] enable CUDA graph for NSA backend and fix NSA FP8 fused RMSNorm group quant (#16841)

- Full hash: `afe285f7bd9a2f377b5fc50ed713f7cf9889edf8`
- Date/author: 2026-01-13 / Hubert Lu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`; `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d27f16f38` - Fix EPLB + FP4 Quantization Compatibility Issue (#13715)

- Full hash: `d27f16f38a6f23e5a7c529c6f052ac11f28c4a97`
- Date/author: 2026-01-10 / Shifang Xu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/longcat_flash.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/gpt_oss.py`
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `20abaee26` - [DSv32] Overlap indexer weights_proj during dual_stream decode (#16637)

- Full hash: `20abaee26cd8ac1387584775babf910c517c3388`
- Date/author: 2026-01-09 / Ziang Li
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4935344fc` - [AMD] Fix aiter page-size handling, DeepSeek MLA tuple inputs, and HiCache/FA3 decode-backend override (#16531)

- Full hash: `4935344fcd57ee515148aed23fcfc559300a4509`
- Date/author: 2026-01-07 / Hubert Lu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `38dc5839d` - [1/n]deepseek_v2.py Refactor: attention backend handlers and forward method definition (#16306)

- Full hash: `38dc5839dd8d185b419be9e5bb2d22c2908db979`
- Date/author: 2026-01-08 / Baizhou Zhang
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_common/__init__.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_common/__init__.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `153c69f63` - [CI] Enable dpsk v31 test on nightly H200 (#16660)

- Full hash: `153c69f63d6b03bae2a0ae64a7991e8a80c88807`
- Date/author: 2026-01-07 / Baizhou Zhang
- Auto category: 模型支持/运行时入口
- Main files: `test/registered/8-gpu-models/test_deepseek_v31.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/8-gpu-models/test_deepseek_v31.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `bb23a8fe7` - [Tiny]Remove progress bar for fp8 ue8m0 quant when unneeded (#16177)

- Full hash: `bb23a8fe7726b28b47cced41b4d59cea4738c5de`
- Date/author: 2026-01-03 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `0d244116d` - [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache (#13959)

- Full hash: `0d244116d28afd92c0f8491a0b5625d75b904e83`
- Date/author: 2026-01-02 / Yongfei Xu
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_nsa_cp.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/server_arguments.md`; `docs/basic_usage/deepseek_v32.md`
  - other: `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/communicator_nsa_cp.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-model: `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa/utils.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
  - tests: `test/manual/test_deepseek_v32_cp_single_node.py`; `test/srt/test_prefill_adder.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2667c857a` - Fix DeepSeekV31's structural tag trigger (#13394)

- Full hash: `2667c857a78faad7d95bb295b5ee821e80779cf8`
- Date/author: 2025-12-31 / Muqi Li
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/function_call/deepseekv31_detector.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/function_call/deepseekv31_detector.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `f35b5da52` - [CI] Append test variant name to markdown report header in nightly test (#16166)

- Full hash: `f35b5da521bffa72404f45ad4a9e85727f12456b`
- Date/author: 2025-12-31 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/test_utils.py`, `test/manual/nightly/test_deepseek_v31_perf.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/nightly_bench_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/test_utils.py`; `test/manual/nightly/test_deepseek_v31_perf.py`; `test/manual/nightly/test_deepseek_v32_perf.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `5e20e7a60` - [AMD CI] Organize AMD nightly perf test files (#16114)

- Full hash: `5e20e7a60d031e5c1e199dfced28fcd34d8563be`
- Date/author: 2025-12-30 / Bingxu Chen
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/test_deepseek_v31_perf.py`, `test/registered/amd/test_deepseek_v3_perf.py`, `test/registered/amd/test_grok_perf.py`, `test/srt/nightly/test_gsm8k_eval_amd.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/test_deepseek_v31_perf.py`; `test/registered/amd/test_deepseek_v3_perf.py`; `test/registered/amd/test_grok_perf.py`; `test/srt/nightly/test_gsm8k_eval_amd.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `2ec6fa3c5` - feat PD: add eagle3 support for DeepSeek V3 in EP mode (#14280)

- Full hash: `2ec6fa3c54a817a621a8da909aed15dfefe79157`
- Date/author: 2025-12-29 / Mike Qiu
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
