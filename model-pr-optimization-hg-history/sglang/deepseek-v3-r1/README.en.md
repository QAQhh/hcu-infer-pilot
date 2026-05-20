# sglang DeepSeek V3/R1 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `docs/references/multi_node_deployment/rbg_pd/deepseekv32_pd.md` | no direct commit |
| `examples/chat_template/tool_chat_template_deepseekv3.jinja` | no direct commit |
| `examples/chat_template/tool_chat_template_deepseekv31.jinja` | no direct commit |
| `examples/chat_template/tool_chat_template_deepseekv32.jinja` | no direct commit |
| `python/sglang/jit_kernel/csrc/nsa/fused_store_index_cache.cuh` | `4e843f121` |
| `python/sglang/srt/function_call/deepseekv31_detector.py` | no direct commit |
| `python/sglang/srt/function_call/deepseekv32_detector.py` | `666caaf9c`, `6af0448cc` |
| `python/sglang/srt/function_call/deepseekv3_detector.py` | no direct commit |
| `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` | `9b2e5526f`, `b3718982a` |
| `python/sglang/srt/layers/attention/nsa/dequant_k_cache.py` | no direct commit |
| `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py` | `e9d6aefa9`, `17031120b`, `006bd44cf` |
| `python/sglang/srt/layers/attention/nsa/nsa_backend_mtp_precompute.py` | no direct commit |
| `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` | `1c83a2090`, `262fa654e`, `78557fe3d`, `c40804b20`, `47b08354a`, `552de7b75`, `2854c89b4`, `e9d6aefa9`, `649172879`, `17031120b`, `006bd44cf`, `17721b00f`, ... (14 total) |
| `python/sglang/srt/layers/attention/nsa/nsa_mtp_verification.py` | no direct commit |
| `python/sglang/srt/layers/attention/nsa/quant_k_cache.py` | no direct commit |
| `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py` | `87fb1eaa6`, `855d15adf` |
| `python/sglang/srt/layers/attention/nsa/transform_index.py` | no direct commit |
| `python/sglang/srt/layers/attention/nsa/triton_kernel.py` | `7e46aafeb` |
| `python/sglang/srt/layers/attention/nsa/utils.py` | `b7f7df7ee`, `6851613b9` |
| `python/sglang/srt/layers/attention/nsa_backend.py` | `47b08354a`, `552de7b75`, `2854c89b4`, `e9d6aefa9`, `4b5f63e1b`, `13f4f010d`, `17031120b`, `be63f982b`, `9ebffef1e`, `472eef407`, `80a6b3270`, `7e46aafeb`, ... (13 total) |
| `python/sglang/srt/layers/communicator_nsa_cp.py` | `3d312643b` |
| `python/sglang/srt/mem_cache/sparsity/algorithms/deepseek_nsa.py` | no direct commit |
| `python/sglang/srt/models/deepseek_common/__init__.py` | no direct commit |
| `python/sglang/srt/models/deepseek_common/attention_backend_handler.py` | `776709efe` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py` | `776709efe` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` | `776709efe` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` | `17721b00f`, `5172c3784` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` | `cd22aa27a`, `c64274c74`, `776709efe` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` | `cd22aa27a`, `776709efe` |
| `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` | `776709efe` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `47b08354a`, `e9d6aefa9`, `cd22aa27a`, `549fbcc86` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `47b08354a`, `766d225fc` |
| `python/sglang/srt/models/deepseek_v2.py` | `2854c89b4`, `79349e551`, `2b0bed239`, `e9d6aefa9`, `574572b21`, `85fe8c679`, `eea9e19c1`, `6b8a6545b`, `d1e95af28`, `944355c66`, `c5d2528bf`, `966ae87d0`, ... (26 total) |
| `test/manual/layers/attention/nsa/test_act_quant_triton.py` | no direct commit |
| `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py` | `006bd44cf` |
| `test/manual/layers/attention/nsa/test_index_buf_accessor.py` | `006bd44cf` |
| `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py` | no direct commit |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py` | no direct commit |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_ar_fusion_eval_mi35x.py` | `b5edab57f` |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` | no direct commit |
| `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_kv_fp8_eval_mi35x.py` | `b5edab57f` |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_ar_fusion_perf_mi35x.py` | `b5edab57f` |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_kv_fp8_perf_mi35x.py` | `b5edab57f` |
| `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_perf_mi35x.py` | no direct commit |
| `test/registered/amd/test_deepseek_r1_mxfp4_8gpu.py` | `67f02681c` |
| `test/registered/backends/test_deepseek_r1_fp8_trtllm_backend.py` | no direct commit |
| `test/registered/kernels/test_nsa_indexer.py` | `814202704`, `17031120b` |
| `test/registered/unit/mem_cache/test_nsa_pool_host_unit.py` | `814202704`, `c3483e8e9` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 80
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-05-09 | `1c83a2090` | 缺陷修复 | fix: 修复paged mqa logits融合算子被误覆盖的问题 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-04-30 | `262fa654e` | 调度/缓存/PD | 【GLM5】NSA indexer新增bf16路径 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-04-25 | `78557fe3d` | 通用实现调整 | 【GLM5】避免DCU路径加载TileLang和TVM依赖 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-04-23 | `c40804b20` | 性能/后端优化 | 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合 3. 融合get_logits_head_gate算子 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-04-16 | `47b08354a` | 缺陷修复 | 1. 修复mqa logits chunk bug 2.将FP8 MLA BMM权重在加载时转为BF16，避免forward中重复cast | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` |
| 2026-04-14 | `87fb1eaa6` | 性能/后端优化 | act_quant接入lightop算子，绕过tilealng | `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py` |
| 2026-04-14 | `552de7b75` | 性能/后端优化 | 1. 修改w8a8in8 marlin重排逻辑，解决精度问题 2. 融合cpy、layernorm、rope、split和D2D操作 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-03-31 | `79349e551` | 性能/后端优化 | 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` |
| 2026-03-30 | `2b0bed239` | 性能/后端优化 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |
| 2026-03-27 | `46e38112a` | 性能/后端优化 | Remove redundant DeepSeek V3 FP4 PCG test (#21485) | `test/registered/quant/test_deepseek_v3_fp4_4gpu.py` |
| 2026-03-26 | `4b5f63e1b` | 性能/后端优化 | FIX: (NSA) Compute topk_indices_offset when NSA prefill flashmla_sparse is used with FP8 KV cache (#20606) | `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-03-24 | `c4db64c16` | 性能/后端优化 | Add Lychee Doc Links Check to Local and CI (#19742) | `.github/linters/lychee-ci.toml`, `.github/linters/lychee.toml`, `.github/workflows/lint.yml` |
| 2026-03-24 | `855d15adf` | 性能/后端优化 | [AMD] Tilelang sparse fwd for dsv32 mi355/mi300 (#19945) | `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py` |
| 2026-03-24 | `649172879` | 性能/后端优化 | [Perf] Overlap NSA-CP key all-gather with query computation for DeepSeek-V3.2 (#20438) | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-03-23 | `ed316a26e` | 性能/后端优化 | Fix CP in-seq-split method for DeepSeek V32 and update related tests (#21192) | `python/sglang/srt/server_args.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py` |
| 2026-03-23 | `814202704` | 性能/后端优化 | ci: unify PR test suite naming (#21187) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-23 | `3d312643b` | 缺陷修复 | [BUGFIX] Fix CP residual size mismatch crash when tp_size == attn_cp_size (#21170) | `python/sglang/srt/layers/communicator_nsa_cp.py` |
| 2026-03-22 | `13f4f010d` | 性能/后端优化 | HiSparse for Sparse Attention (#20343) | `python/sglang/jit_kernel/csrc/hisparse.cuh`, `python/sglang/jit_kernel/hisparse.py`, `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-03-22 | `766d225fc` | 性能/后端优化 | Add SGLang CUDA crash API logging inspired by FlashInfer (#20910) | `.claude/skills/debug-cuda-crash/SKILL.md`, `docs/references/environment_variables.md`, `python/sglang/jit_kernel/awq_marlin_repack.py` |
| 2026-03-20 | `5f3393c04` | 缺陷修复 | Fix deepseek-v32-fp4 b200 ci (#21072) | `python/sglang/srt/utils/common.py` |
| 2026-03-20 | `a0a4dae67` | 性能/后端优化 | Revert "Fix DeepSeek V32 FP4 test" (#21003) | `python/sglang/test/test_utils.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py` |
| 2026-03-20 | `c82d20d48` | 性能/后端优化 | Fix DeepSeek V32 FP4 test (#20984) | `python/sglang/test/test_utils.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py` |
| 2026-03-19 | `c8f0122ac` | 性能/后端优化 | Fix gpu-fault issue when run deepseek-r1 and enable dp (#20841) | `python/sglang/srt/layers/attention/aiter_backend.py` |
| 2026-03-19 | `574572b21` | 缺陷修复 | [BugFix] bug fix for DeepSeek eagle3 in Attn-DP mode (#20492) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-19 | `85fe8c679` | 性能/后端优化 | [AMD] Use aiter_dsv3_router_gemm kernel if number of experts <= 256. (#18451) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-19 | `cd22aa27a` | 性能/后端优化 | [CPU] Add FP8 Bmm support (#9744) | `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_cpu.py` |
| 2026-03-18 | `eea9e19c1` | 缺陷修复 | fix lint introduced in #20708 (#20886) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-18 | `6b8a6545b` | 性能/后端优化 | Add Mistral Small 4 (Pixtral) support (#20708) | `benchmark/mmmu/bench_sglang.py`, `benchmark/mmmu/eval_utils.py`, `python/sglang/srt/configs/deepseek_ocr.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-18 | `944355c66` | 性能/后端优化 | [Bugfix] Fix model output corruption caused by EPLB rebalance (Eager and CUDA Graph modes) (#18213) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-17 | `c5d2528bf` | 性能/后端优化 | Revert "[AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars." (#20797) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-18 | `17031120b` | 性能/后端优化 | [DeepSeek v3.2][Bugfix] get_index_k_scale_buffer support cp (#18280) | `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-03-17 | `966ae87d0` | 模型支持/运行时入口 | [AMD] avoid correction_bias_dtype dtype convert (#20692) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-17 | `385a35bd1` | 性能/后端优化 | [AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars. (#20647) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-16 | `549fbcc86` | 调度/缓存/PD | [5/N] (Elastic EP) Use GPU P2P to exchange expert weights during EPLB as much as possible (#12068) | `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/eplb/expert_location_updater.py`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-03-15 | `c3483e8e9` | 性能/后端优化 | [CI] Move existing unit tests into unit directory (#20631) | `test/registered/unit/batch_invariant_ops/test_batch_invariant_ops.py`, `test/registered/unit/entrypoints/test_ssl_cert_refresher.py`, `test/registered/unit/function_call/test_function_call_parser.py` |
| 2026-03-14 | `39008955f` | 性能/后端优化 | Revert "[AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars." (#20602) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-14 | `0eea80bc0` | 性能/后端优化 | [AMD][MORI] Fix MTP crash with FP4/FP8 dispatch and add NEXTN dispatch env vars. (#20453) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-11 | `67f02681c` | 性能/后端优化 | [AMD] Support speculative decoding v2 for aiter backend on ROCm/HIP (#17450) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-03-11 | `2720ea266` | 缺陷修复 | [Typo] Fix H200 doc links pointing to H20 section in deepseek_v3.md (#20383) | `docs/basic_usage/deepseek_v3.md` |
| 2026-03-12 | `006bd44cf` | 性能/后端优化 | [deepseekv3.2] fix get_k_and_s_triton kenel for 128K seqlen case bug (#19319) | `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-03-11 | `7b44bc923` | 性能/后端优化 | Relax flaky B200 GSM8K accuracy thresholds (#20304) | `test/registered/quant/test_deepseek_v3_fp4_4gpu.py`, `test/registered/spec/eagle/test_eagle_infer_beta_dp_attention.py` |
| 2026-03-11 | `9991debde` | 性能/后端优化 | [Feature] Integrate Elastic NIXL-EP into SGLang (#19248) | `docs/advanced_features/expert_parallelism.md`, `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` |
| 2026-03-10 | `9b2e5526f` | 缺陷修复 | [NPU][Bug fix] context parallel bug fix (#19820) | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` |
| 2026-03-09 | `be63f982b` | 性能/后端优化 | [V32/GLM5] Control the threshold of applying dense attention with an environ (#20062) | `docs/references/environment_variables.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-03-08 | `17721b00f` | 缺陷修复 | [AMD] Fix Tensor Memory Aliasing (#19928) | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-03-06 | `50bbdcf8e` | 性能/后端优化 | Relax flaky test thresholds for MLA DeepSeek V3 and AutoRound (#20068) | `test/registered/mla/test_mla_deepseek_v3.py`, `test/registered/quant/test_autoround.py` |
| 2026-03-07 | `a0d085c16` | 性能/后端优化 | Adding correct path for module not found error while collecting test (#19778) | `test/manual/nightly/test_deepseek_v31_perf.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/manual/nightly/test_text_models_perf.py` |
| 2026-03-06 | `84aaa6979` | 性能/后端优化 | [AMD] Use bfloat16 for correction_bias in AITER FP8 path to avoid runtime dtype conversion for dsv3 (#19843) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-05 | `04e364d53` | 性能/后端优化 | [V32] Enhance deepseek v32 related tests (#19985) | `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py` |
| 2026-03-06 | `9ebffef1e` | 缺陷修复 | [FIX] NSA backend page_table overflow in speculative decoding target_verify (#19016) | `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-03-05 | `346a4131c` | 缺陷修复 | [Spec] Refactor NaN/OOB checks to async `maybe_detect_*` with env-var control (#19899) | `python/sglang/srt/environ.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_worker.py` |
| 2026-03-05 | `b5edab57f` | 性能/后端优化 | [AMD] CI - Add MI35x nightly/PR tests for kv-cache-fp8 and allreduce-fusion (DeepSeek) (#19834) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-05 | `472eef407` | 性能/后端优化 | fa4 cleanup (#19727) | `python/pyproject.toml`, `python/sglang/jit_kernel/flash_attention/cute/.flake8`, `python/sglang/jit_kernel/flash_attention/cute/AUTHORS` |
| 2026-03-05 | `1b76eb936` | 调度/缓存/PD | [Doc] Update version references and add automation (#18409) | `.github/workflows/release-branch-cut.yml`, `benchmark/deepseek_v3/README.md`, `docs/get_started/install.md` |
| 2026-03-04 | `5972f97f1` | 模型支持/运行时入口 | Remove naive rotary forward overriding. (#19263) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-03-03 | `b7f7df7ee` | 缺陷修复 | [NSA] Fix line-too-long lint in `can_nsa_prefill_cp_round_robin_split` (#19829) | `python/sglang/srt/layers/attention/nsa/utils.py` |
| 2026-03-04 | `6851613b9` | 缺陷修复 | [Bugfix] For cp: Fixed hang problem in prefix cache and kvcache support fp8 in-seq-split mode (#19656) | `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/server_args.py` |
| 2026-03-03 | `666caaf9c` | 调度/缓存/PD | [Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format. (#16091) | `python/sglang/srt/function_call/deepseekv32_detector.py`, `test/registered/function_call/test_function_call_parser.py` |
| 2026-03-03 | `6af0448cc` | 缺陷修复 | [Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON (#18174) | `python/sglang/srt/function_call/deepseekv32_detector.py` |
| 2026-03-02 | `fe9d85d93` | 性能/后端优化 | Fix CompressedTensorsMxInt4MoE abstract method and relax GPQA baseline (#19726) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-03-02 | `c64274c74` | 性能/后端优化 | Piecewise Cuda Graph set default (#16331) | `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-03-02 | `b3718982a` | 模型支持/运行时入口 | [Feature] add feature mla_ag_after_qlora for dsv3.2 (#19428) | `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-03-01 | `80a6b3270` | 性能/后端优化 | [Perf] Optimize NSA backend metadata under MTP (#19536) | `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/attention/utils.py` |
| 2026-02-27 | `776709efe` | 性能/后端优化 | [3/n] deepseek_v2.py Refactor: Migrate MLA forward method in deepseek_v2.py (#19122) | `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` |
| 2026-02-28 | `7e46aafeb` | 性能/后端优化 | [AMD] Enable cudagraph for aiter nsa backend and add aiter impl for nsa pr… (#18526) | `python/sglang/srt/layers/attention/nsa/triton_kernel.py`, `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-02-27 | `9496bbd7b` | 通用实现调整 | [AMD] Use `tilelang` as default NSA attention backend dispatch on AMD Instinct (#18319) | `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/server_args.py` |
| 2026-02-27 | `5172c3784` | 性能/后端优化 | [AMD] Use fused GEMM with FP8 cast for FP8 prefill (#19422) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-02-26 | `4e843f121` | 性能/后端优化 | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache (#19148) | `python/sglang/jit_kernel/csrc/nsa/fused_store_index_cache.cuh`, `python/sglang/jit_kernel/fused_store_index_cache.py`, `python/sglang/jit_kernel/utils.py` |
| 2026-02-25 | `cc1ca61c8` | 性能/后端优化 | fix: add --cuda-graph-max-bs to DSV3 FA3 FP8 KV cache test (#19307) | `test/registered/mla/test_mla_deepseek_v3.py` |
| 2026-02-25 | `60eeef737` | 性能/后端优化 | [AMD][with CI Fix] support two batch overlapping for mori ep (#19216) | `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations.py`, `python/sglang/srt/batch_overlap/operations_strategy.py` |
| 2026-02-25 | `a55f65883` | 模型支持/运行时入口 | [Misc] Normalize `--host` parameter to use plain hostname without scheme (#19309) | `benchmark/deepseek_v3/README.md`, `docs/developer_guide/evaluating_new_models.md`, `examples/runtime/multimodal/llama3_llava_server.py` |
| 2026-02-25 | `4a3a787f1` | 缺陷修复 | [Fix] Kimi K2.5 support pp (#18434) | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/kimi_k25.py` |
| 2026-02-25 | `b9cf1563d` | 性能/后端优化 | [ROCm] Optimize Deepseek R1 on MI300X (#18242) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-25 | `c193a52fa` | 模型支持/运行时入口 | [AMD] DSR1/V3 use fp8 bmm in MLA for MI300X (#18624) | `python/sglang/srt/models/deepseek_v2.py` |
| 2026-02-24 | `38f25e802` | 缺陷修复 | Fix/deepseek readme link (#19258) | `benchmark/deepseek_v3/README.md` |
| 2026-02-23 | `43f83525c` | 性能/后端优化 | Revert "[AMD] support two batch overlapping for mori ep #17953" (#19161) | `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` |

## Per-Commit Audit Cards

### Commit `1c83a2090` - fix: 修复paged mqa logits融合算子被误覆盖的问题

- Full hash: `1c83a209088dd514de09124279cb9ccdd2301928`
- Date/author: 2026-05-09 / maxiao
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `262fa654e` - 【GLM5】NSA indexer新增bf16路径

- Full hash: `262fa654e806f504f9a20f5b7438975bb719d891`
- Date/author: 2026-04-30 / maxiao1
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `78557fe3d` - 【GLM5】避免DCU路径加载TileLang和TVM依赖

- Full hash: `78557fe3d0893bb8173b1322ef08fe722accf2af`
- Date/author: 2026-04-25 / maxiao1
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c40804b20` - 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合  3. 融合get_logits_head_gate算子

- Full hash: `c40804b203877a1affe2cc3862fc26dc29b8efdd`
- Date/author: 2026-04-23 / maxiao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `87fb1eaa6` - act_quant接入lightop算子，绕过tilealng

- Full hash: `87fb1eaa697c69ff4d53c37170687b3788866df5`
- Date/author: 2026-04-14 / niuhb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `552de7b75` - 1. 修改w8a8in8 marlin重排逻辑，解决精度问题 2. 融合cpy、layernorm、rope、split和D2D操作

- Full hash: `552de7b759eb7c81ff39ae678e1d2f05024c7b2b`
- Date/author: 2026-04-14 / niuhb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`
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

### Commit `46e38112a` - Remove redundant DeepSeek V3 FP4 PCG test (#21485)

- Full hash: `46e38112a7b8cca693fb6d0f2e7da556e019f0ea`
- Date/author: 2026-03-27 / Mohammad Miadh Angkad
- Auto category: 性能/后端优化
- Main files: `test/registered/quant/test_deepseek_v3_fp4_4gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/quant/test_deepseek_v3_fp4_4gpu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `4b5f63e1b` - FIX: (NSA) Compute topk_indices_offset when NSA prefill flashmla_sparse is used with FP8 KV cache (#20606)

- Full hash: `4b5f63e1b8ba37f26d71caf2a6004e473db53675`
- Date/author: 2026-03-26 / Ho-Ren (Jack) Chuang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c4db64c16` - Add Lychee Doc Links Check to Local and CI (#19742)

- Full hash: `c4db64c16bba9cb549d510735a064272c87779fa`
- Date/author: 2026-03-24 / Jiaxin(Jackson) Deng
- Auto category: 性能/后端优化
- Main files: `.github/linters/lychee-ci.toml`, `.github/linters/lychee.toml`, `.github/workflows/lint.yml`, `.github/workflows/nightly-link-check.yml`, `.pre-commit-config.yaml`, `benchmark/blog_v0_2/README.md`, `docs/basic_usage/deepseek_v3.md`, `docs/basic_usage/gpt_oss.md` 等 20 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/linters/lychee-ci.toml`; `.github/linters/lychee.toml`; `.github/workflows/lint.yml`; `.github/workflows/nightly-link-check.yml`
  - docs-bench: `benchmark/blog_v0_2/README.md`; `docs/basic_usage/deepseek_v3.md`; `docs/basic_usage/gpt_oss.md`; `docs/developer_guide/contribution_guide.md`; `docs/developer_guide/setup_github_runner.md`; `docs/performance_dashboard/index.html`; `docs/platforms/ascend_contribution_guide.md`; `docs/platforms/ascend_npu.md` 等 15 个文件
  - runtime-model: `.pre-commit-config.yaml`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `855d15adf` - [AMD] Tilelang sparse fwd for dsv32 mi355/mi300 (#19945)

- Full hash: `855d15adf6571e90b07bb851bbab512def1d3413`
- Date/author: 2026-03-24 / Thomas Wang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `649172879` - [Perf] Overlap NSA-CP key all-gather with query computation for DeepSeek-V3.2 (#20438)

- Full hash: `649172879778646a8574525448734b95a55b6739`
- Date/author: 2026-03-24 / Baidu-AIAK
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ed316a26e` - Fix CP in-seq-split method for DeepSeek V32 and update related tests (#21192)

- Full hash: `ed316a26efa474190a18ee517cebffba46e4bcdf`
- Date/author: 2026-03-23 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/server_args.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`, `test/registered/cp/test_deepseek_v32_cp_single_node.py`, `test/registered/ep/test_deepep_large.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
  - tests: `test/manual/nightly/test_deepseek_v32_perf.py`; `test/registered/8-gpu-models/test_deepseek_v32_basic.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; `test/registered/cp/test_deepseek_v32_cp_single_node.py`; `test/registered/ep/test_deepep_large.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `814202704` - ci: unify PR test suite naming (#21187)

- Full hash: `814202704bf21525b5ae07029cb475da4c87f3b7`
- Date/author: 2026-03-23 / Lianmin Zheng
- Auto category: 性能/后端优化
- Main files: `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`, `scripts/ci/utils/slash_command_handler.py`, `test/README.md` 等 283 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/actions/wait-for-jobs/action.yml`; `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`; `test/README.md`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/attention/test_chunk_gated_delta_rule.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py` 等 278 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `3d312643b` - [BUGFIX] Fix CP residual size mismatch crash when tp_size == attn_cp_size  (#21170)

- Full hash: `3d312643b9f1035916c6a715b7f0a25b6e1fc484`
- Date/author: 2026-03-23 / yudian0504
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/communicator_nsa_cp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/communicator_nsa_cp.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `13f4f010d` - HiSparse for Sparse Attention (#20343)

- Full hash: `13f4f010d8ea7fbf628cd3b5313a73cac6c0285e`
- Date/author: 2026-03-22 / Zhiqiang Xie
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/csrc/hisparse.cuh`, `python/sglang/jit_kernel/hisparse.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py` 等 20 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/hisparse_coordinator.py`; `python/sglang/srt/managers/schedule_batch.py`
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/jit_kernel/csrc/hisparse.cuh`; `python/sglang/jit_kernel/hisparse.py`; `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_output_processor_mixin.py`; `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`; `python/sglang/srt/mem_cache/hisparse_memory_pool.py`; `python/sglang/srt/mem_cache/memory_pool.py` 等 14 个文件
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

### Commit `5f3393c04` - Fix deepseek-v32-fp4 b200 ci (#21072)

- Full hash: `5f3393c04cf0de2eb99f5624b8be1125b34f5baf`
- Date/author: 2026-03-20 / Baizhou Zhang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/utils/common.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/utils/common.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `a0a4dae67` - Revert "Fix DeepSeek V32 FP4 test" (#21003)

- Full hash: `a0a4dae67f5fdcb209cbbd7b6885a99b06406ac3`
- Date/author: 2026-03-20 / Lianmin Zheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/test_utils.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/test_utils.py`; `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`; `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `c82d20d48` - Fix DeepSeek V32 FP4 test (#20984)

- Full hash: `c82d20d48ecc643ab2a84a0961b8b71901eeffb1`
- Date/author: 2026-03-20 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/test_utils.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/test_utils.py`; `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`; `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `c8f0122ac` - Fix gpu-fault issue when run deepseek-r1 and enable dp (#20841)

- Full hash: `c8f0122acf481e8712491dcd6aebc0bd97df430c`
- Date/author: 2026-03-19 / kk
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
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

### Commit `17031120b` - [DeepSeek v3.2][Bugfix] get_index_k_scale_buffer support cp (#18280)

- Full hash: `17031120b8f68fb96ec22fec549d6c599a4e473e`
- Date/author: 2026-03-18 / Yongfei Xu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `test/registered/kernels/test_nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
  - tests: `test/registered/kernels/test_nsa_indexer.py`
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

### Commit `895e56097` - Add NPU basic function testcases (#19382)

- Full hash: `895e56097cc25f762373f462fd027bc39163eb0c`
- Date/author: 2026-03-16 / Sugar920
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`, `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py` 等 87 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/disaggregation_utils.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`; `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py`; `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py` 等 86 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `c3483e8e9` - [CI] Move existing unit tests into unit directory (#20631)

- Full hash: `c3483e8e97d399d5b796ef4af75a23934bd49b10`
- Date/author: 2026-03-15 / Ke Bao
- Auto category: 性能/后端优化
- Main files: `test/registered/unit/batch_invariant_ops/test_batch_invariant_ops.py`, `test/registered/unit/entrypoints/test_ssl_cert_refresher.py`, `test/registered/unit/function_call/test_function_call_parser.py`, `test/registered/unit/function_call/test_glm47_moe_detector.py`, `test/registered/unit/function_call/test_json_schema_constraint.py`, `test/registered/unit/function_call/test_parallel_tool_calls.py`, `test/registered/unit/function_call/test_unknown_tool_name.py`, `test/registered/unit/layers/test_conv_layer.py` 等 29 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/unit/batch_invariant_ops/test_batch_invariant_ops.py`; `test/registered/unit/entrypoints/test_ssl_cert_refresher.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/unit/function_call/test_glm47_moe_detector.py`; `test/registered/unit/function_call/test_json_schema_constraint.py`; `test/registered/unit/function_call/test_parallel_tool_calls.py`; `test/registered/unit/function_call/test_unknown_tool_name.py`; `test/registered/unit/layers/test_conv_layer.py` 等 29 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `67f02681c` - [AMD] Support speculative decoding v2 for aiter backend on ROCm/HIP (#17450)

- Full hash: `67f02681c9a3dd578c8d987f48796e17c1f98aa5`
- Date/author: 2026-03-11 / Hubert Lu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/amd/test_deepseek_r1_mxfp4_8gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
  - tests: `test/registered/amd/test_deepseek_r1_mxfp4_8gpu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2720ea266` - [Typo] Fix H200 doc links pointing to H20 section in deepseek_v3.md (#20383)

- Full hash: `2720ea2667dc8ae2129730326491f3c6e7364cdd`
- Date/author: 2026-03-11 / Mook
- Auto category: 缺陷修复
- Main files: `docs/basic_usage/deepseek_v3.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/basic_usage/deepseek_v3.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `006bd44cf` - [deepseekv3.2] fix get_k_and_s_triton kenel for 128K seqlen case bug (#19319)

- Full hash: `006bd44cf92064bdd32a96f150a1aa77c2eb7cde`
- Date/author: 2026-03-12 / BingjiaWang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py`, `test/manual/layers/attention/nsa/test_index_buf_accessor.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py`; `test/manual/layers/attention/nsa/test_index_buf_accessor.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7b44bc923` - Relax flaky B200 GSM8K accuracy thresholds (#20304)

- Full hash: `7b44bc923e9afd3cb0ed3727a4f2520924853b7f`
- Date/author: 2026-03-11 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `test/registered/quant/test_deepseek_v3_fp4_4gpu.py`, `test/registered/spec/eagle/test_eagle_infer_beta_dp_attention.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/quant/test_deepseek_v3_fp4_4gpu.py`; `test/registered/spec/eagle/test_eagle_infer_beta_dp_attention.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `be63f982b` - [V32/GLM5] Control the threshold of applying dense attention with an environ (#20062)

- Full hash: `be63f982b7b7f0451a3ccbb13f6fe2ecf6c39796`
- Date/author: 2026-03-09 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/server_args.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
  - tests: `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`; `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
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

### Commit `50bbdcf8e` - Relax flaky test thresholds for MLA DeepSeek V3 and AutoRound (#20068)

- Full hash: `50bbdcf8e97d837b9a532723f47f4444ce71bba0`
- Date/author: 2026-03-06 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `test/registered/mla/test_mla_deepseek_v3.py`, `test/registered/quant/test_autoround.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/mla/test_mla_deepseek_v3.py`; `test/registered/quant/test_autoround.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `04e364d53` - [V32] Enhance deepseek v32 related tests (#19985)

- Full hash: `04e364d538bb92e433ecc7479c1f303a8a1c6ddf`
- Date/author: 2026-03-05 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/8-gpu-models/test_deepseek_v32_basic.py`; `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`; `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `9ebffef1e` - [FIX] NSA backend page_table overflow in speculative decoding target_verify (#19016)

- Full hash: `9ebffef1ef956654e249ca21804d4a82b8ca1778`
- Date/author: 2026-03-06 / Xinyuan Tong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/nsa_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `346a4131c` - [Spec] Refactor NaN/OOB checks to async `maybe_detect_*` with env-var control (#19899)

- Full hash: `346a4131cfbac5fe2f42ba01d7c4062853e2ded5`
- Date/author: 2026-03-05 / kpham-sgl
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_worker.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `python/sglang/srt/speculative/spec_utils.py`, `python/sglang/srt/speculative/standalone_worker.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/speculative/spec_utils.py`
  - runtime-model: `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`; `python/sglang/srt/speculative/standalone_worker.py`; `python/sglang/srt/speculative/standalone_worker_v2.py`
  - tests: `python/sglang/test/server_fixtures/eagle_fixture.py`; `test/registered/spec/eagle/test_deepseek_v3_fp4_mtp_small.py`; `test/registered/spec/eagle/test_eagle_constrained_decoding.py`; `test/registered/spec/eagle/test_eagle_dp_attention.py`; `test/registered/spec/eagle/test_eagle_infer_beta.py`; `test/registered/spec/eagle/test_eagle_infer_beta_dp_attention.py`; `test/registered/spec/eagle/test_eagle_infer_beta_dp_attention_large.py`; `test/registered/spec/test_constrained_decoding_spec_reasoning.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b5edab57f` - [AMD] CI - Add MI35x nightly/PR tests for kv-cache-fp8 and allreduce-fusion (DeepSeek) (#19834)

- Full hash: `b5edab57f2ff7baa8ac5aeee149aab0dc59e61dd`
- Date/author: 2026-03-05 / YC Tseng
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_ar_fusion_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_kv_fp8_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_ar_fusion_perf_mi35x.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`; `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`
  - other: `scripts/ci/amd/amd_ci_start_container_disagg.sh`
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_ar_fusion_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_kv_fp8_eval_mi35x.py`; `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_ar_fusion_perf_mi35x.py`; `test/registered/amd/perf/mi35x/test_deepseek_r1_mxfp4_kv_fp8_perf_mi35x.py`; `test/registered/amd/test_deepseek_v3_basic_kv_fp8.py`; `test/registered/amd/test_deepseek_v3_mtp_kv_fp8.py`; `test/registered/ops/test_aiter_allreduce_fusion_amd.py`; `test/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `472eef407` - fa4 cleanup (#19727)

- Full hash: `472eef4071ed94cb809a95031612f51779d799ad`
- Date/author: 2026-03-05 / Rain Jiang
- Auto category: 性能/后端优化
- Main files: `python/pyproject.toml`, `python/sglang/jit_kernel/flash_attention/cute/.flake8`, `python/sglang/jit_kernel/flash_attention/cute/AUTHORS`, `python/sglang/jit_kernel/flash_attention/cute/LICENSE`, `python/sglang/jit_kernel/flash_attention/cute/README.md`, `python/sglang/jit_kernel/flash_attention/cute/__init__.py`, `python/sglang/jit_kernel/flash_attention/cute/ampere_helpers.py`, `python/sglang/jit_kernel/flash_attention/cute/barrier.py` 等 45 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/pyproject.toml`
  - runtime-perf: `python/sglang/jit_kernel/flash_attention/cute/.flake8`; `python/sglang/jit_kernel/flash_attention/cute/AUTHORS`; `python/sglang/jit_kernel/flash_attention/cute/LICENSE`; `python/sglang/jit_kernel/flash_attention/cute/README.md`; `python/sglang/jit_kernel/flash_attention/cute/__init__.py`; `python/sglang/jit_kernel/flash_attention/cute/ampere_helpers.py`; `python/sglang/jit_kernel/flash_attention/cute/barrier.py`; `python/sglang/jit_kernel/flash_attention/cute/benchmark.py` 等 43 个文件
  - tests: `sgl-kernel/tests/test_flash_attention_4.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1b76eb936` - [Doc] Update version references and add automation (#18409)

- Full hash: `1b76eb93618c5c4318c6c0f70783dd18dc315bc1`
- Date/author: 2026-03-05 / Mohammad Miadh Angkad
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/release-branch-cut.yml`, `benchmark/deepseek_v3/README.md`, `docs/get_started/install.md`, `docs/platforms/amd_gpu.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/release-branch-cut.yml`
  - docs-bench: `benchmark/deepseek_v3/README.md`; `docs/get_started/install.md`; `docs/platforms/amd_gpu.md`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `5972f97f1` - Remove naive rotary forward overriding. (#19263)

- Full hash: `5972f97f11c0886d6d6b1790bc2de6e3f228e682`
- Date/author: 2026-03-04 / Jue Wang
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b7f7df7ee` - [NSA] Fix line-too-long lint in `can_nsa_prefill_cp_round_robin_split` (#19829)

- Full hash: `b7f7df7ee6c2a47fdffb8275feffb24108eca73f`
- Date/author: 2026-03-03 / sglang-bot
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/nsa/utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6851613b9` - [Bugfix] For cp: Fixed hang problem in prefix cache and kvcache support fp8 in-seq-split mode (#19656)

- Full hash: `6851613b93e36a49c07a2583234bd9f08f67eef6`
- Date/author: 2026-03-04 / Baidu-AIAK
- Auto category: 缺陷修复
- Main files: `docs/basic_usage/deepseek_v32.md`, `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/basic_usage/deepseek_v32.md`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `666caaf9c` - [Tool Call] Stream DeepSeek-V3.2 function call parameters in JSON format. (#16091)

- Full hash: `666caaf9ce76ea157ac546a80d2c9c901c5c926c`
- Date/author: 2026-03-03 / Muqi Li
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/function_call/deepseekv32_detector.py`, `test/registered/function_call/test_function_call_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/function_call/deepseekv32_detector.py`
  - tests: `test/registered/function_call/test_function_call_parser.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `6af0448cc` - [Bugfix] Catch errors when DeepSeek-V3.2 generates malformed JSON (#18174)

- Full hash: `6af0448cc9bff5fbf13fe84b50276e399f620516`
- Date/author: 2026-03-03 / Muqi Li
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/function_call/deepseekv32_detector.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/function_call/deepseekv32_detector.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `fe9d85d93` - Fix CompressedTensorsMxInt4MoE abstract method and relax GPQA baseline (#19726)

- Full hash: `fe9d85d93cbd22283809317c61df6a9f5df35f90`
- Date/author: 2026-03-02 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`
  - tests: `test/registered/8-gpu-models/test_deepseek_v32.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `80a6b3270` - [Perf] Optimize NSA backend metadata under MTP (#19536)

- Full hash: `80a6b32703db7f0fe1ef69fa9b5e2154f3e51258`
- Date/author: 2026-03-01 / Brayden Zhong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/layers/attention/utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`; `python/sglang/srt/layers/attention/utils.py`
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

### Commit `7e46aafeb` - [AMD] Enable cudagraph for aiter nsa backend and add aiter impl for nsa pr… (#18526)

- Full hash: `7e46aafebb6dded04f6ba345a8e203049618704a`
- Date/author: 2026-02-28 / wufann
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/triton_kernel.py`, `python/sglang/srt/layers/attention/nsa_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/triton_kernel.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9496bbd7b` - [AMD] Use `tilelang` as default NSA attention backend dispatch on AMD Instinct (#18319)

- Full hash: `9496bbd7b11c7ce7ac96b339c7a1fb23d0406545`
- Date/author: 2026-02-27 / fxmarty-amd
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
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

### Commit `4e843f121` - [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache (#19148)

- Full hash: `4e843f12165705b036718ecce8cdfe9d4dce1691`
- Date/author: 2026-02-26 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/csrc/nsa/fused_store_index_cache.cuh`, `python/sglang/jit_kernel/fused_store_index_cache.py`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/nsa/fused_store_index_cache.cuh`; `python/sglang/jit_kernel/fused_store_index_cache.py`; `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `cc1ca61c8` - fix: add --cuda-graph-max-bs to DSV3 FA3 FP8 KV cache test (#19307)

- Full hash: `cc1ca61c81fb2133ab134fd4294d11828fa89a9e`
- Date/author: 2026-02-25 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `test/registered/mla/test_mla_deepseek_v3.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/mla/test_mla_deepseek_v3.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `a55f65883` - [Misc] Normalize `--host` parameter to use plain hostname without scheme (#19309)

- Full hash: `a55f6588350c754cfc7ff0a5a0f8b75a5fde6dfa`
- Date/author: 2026-02-25 / Julian Huang
- Auto category: 模型支持/运行时入口
- Main files: `benchmark/deepseek_v3/README.md`, `docs/developer_guide/evaluating_new_models.md`, `examples/runtime/multimodal/llama3_llava_server.py`, `examples/runtime/multimodal/pixtral_server.py`, `examples/runtime/multimodal/qwen_llava_server.py`, `python/sglang/test/few_shot_gsm8k.py`, `python/sglang/test/test_utils.py`, `python/sglang/utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/deepseek_v3/README.md`; `docs/developer_guide/evaluating_new_models.md`; `examples/runtime/multimodal/llama3_llava_server.py`; `examples/runtime/multimodal/pixtral_server.py`; `examples/runtime/multimodal/qwen_llava_server.py`
  - other: `python/sglang/utils.py`
  - tests: `python/sglang/test/few_shot_gsm8k.py`; `python/sglang/test/test_utils.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `38f25e802` - Fix/deepseek readme link (#19258)

- Full hash: `38f25e802d771efca521e194d7ea3aee2295443c`
- Date/author: 2026-02-24 / Alec Leng
- Auto category: 缺陷修复
- Main files: `benchmark/deepseek_v3/README.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/deepseek_v3/README.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

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
