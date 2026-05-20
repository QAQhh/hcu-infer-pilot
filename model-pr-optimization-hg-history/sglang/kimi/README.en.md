# sglang Kimi K2/K2.5/Linear/VL Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/configs/kimi_k25.py` | `479ab7a4e` |
| `python/sglang/srt/configs/kimi_linear.py` | no direct commit |
| `python/sglang/srt/configs/kimi_vl.py` | no direct commit |
| `python/sglang/srt/configs/kimi_vl_moonvit.py` | no direct commit |
| `python/sglang/srt/function_call/kimik2_detector.py` | `c562e0d13`, `677b66af8` |
| `python/sglang/srt/models/kimi_k25.py` | `01ccdb91b`, `24a27d532`, `1c456a0af`, `5f717913a`, `069d4c577`, `85f7a0aa3`, `86eb80007`, `4a3a787f1`, `5a7ae059e`, `071bf2ce0`, `7b8365931`, `d11ccc0a0`, ... (13 total) |
| `python/sglang/srt/models/kimi_linear.py` | `db995fba4`, `738ebfd33`, `d2885a909`, `bf5238835`, `37c33cc0a`, `d90c0837e`, `1e8db1829`, `0c8165ffb`, `176da1bbd`, `bcc6d84f9`, `e6b7c0494` |
| `python/sglang/srt/models/kimi_vl.py` | no direct commit |
| `python/sglang/srt/models/kimi_vl_moonvit.py` | `766d225fc`, `1c456a0af`, `5f717913a` |
| `python/sglang/srt/multimodal/processors/kimi_k25.py` | `07a24f1a3`, `479ab7a4e` |
| `python/sglang/srt/multimodal/processors/kimi_vl.py` | `07a24f1a3` |
| `test/manual/models/test_kimi_k2_models.py` | `56907cbcb` |
| `test/registered/8-gpu-models/test_kimi_k25.py` | `8c3ccef2d`, `011806c41` |
| `test/registered/amd/accuracy/mi30x/test_kimi_k25_eval_amd.py` | `d84d2063d` |
| `test/registered/amd/accuracy/mi30x/test_kimi_k2_eval_amd.py` | `6fd878b41` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k25_aiter_mla_eval_mi35x.py` | `1e2983c98` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k25_eval_mi35x.py` | `d84d2063d` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k25_mxfp4_eval_mi35x.py` | `1e2983c98` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k2_eval_mi35x.py` | `6fd878b41` |
| `test/registered/amd/test_kimi_k25_mxfp4.py` | `18dd5c972`, `1e2983c98` |
| `test/registered/amd/test_kimi_k2_instruct.py` | `52bca4287`, `738b1ac98` |
| `test/registered/ascend/vlm_models/test_npu_kimi_vl_a3b_instruct.py` | `895e56097` |
| `test/registered/function_call/test_kimik2_detector.py` | `814202704`, `cea79530f`, `c562e0d13` |
| `test/registered/models/test_kimi_linear_models.py` | `814202704`, `63cc97f4e` |
| `test/registered/models/test_kimi_linear_models_pcg.py` | `814202704`, `c64274c74`, `bf5238835` |
| `test/registered/stress/test_stress_kimi_k2.py` | no direct commit |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 71
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-30 | `2b0bed239` | 性能/后端优化 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |
| 2026-03-26 | `8c3ccef2d` | 缺陷修复 | Fix Kimi K2.5 dp attention+ spec decoding launch crash (#21391) | `python/sglang/srt/models/llama_eagle3.py`, `test/registered/8-gpu-models/test_kimi_k25.py` |
| 2026-03-26 | `01ccdb91b` | 缺陷修复 | [Fix] Add EPLB rebalance support for Kimi K2.5 (#21004) | `python/sglang/srt/models/kimi_k25.py` |
| 2026-03-23 | `27ac831a8` | 性能/后端优化 | docs: improve CI and testing documentation (#21202) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md` |
| 2026-03-23 | `814202704` | 性能/后端优化 | ci: unify PR test suite naming (#21187) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-22 | `766d225fc` | 性能/后端优化 | Add SGLang CUDA crash API logging inspired by FlashInfer (#20910) | `.claude/skills/debug-cuda-crash/SKILL.md`, `docs/references/environment_variables.md`, `python/sglang/jit_kernel/awq_marlin_repack.py` |
| 2026-03-20 | `104b10f70` | 性能/后端优化 | refactor: consolidate is_in_ci (jit_kernel, sgl-kernel benchmarks, tests) (#21009) | `.claude/skills/add-sgl-kernel/SKILL.md`, `benchmark/kernels/all_reduce/benchmark_torch_symm_mem.py`, `python/sglang/jit_kernel/benchmark/bench_awq_dequantize.py` |
| 2026-03-20 | `cea79530f` | 性能/后端优化 | ci: merge CPU default and stage-a-cpu-only suites (#20992) | `.github/workflows/pr-test.yml`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_executor.py`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_planner.py` |
| 2026-03-19 | `db995fba4` | 性能/后端优化 | perf(kimi_linear): replace einops rearrange with native torch ops in Kimi-Linear KDA path (#20396) | `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-03-20 | `c562e0d13` | 测试/文档/基准 | [feat] Enhance Kimi-K2/K2.5 function call and reasoning detection (#19552) | `python/sglang/srt/function_call/kimik2_detector.py`, `test/registered/function_call/test_kimik2_detector.py` |
| 2026-03-18 | `24a27d532` | 性能/后端优化 | vlm: support piecewise cuda graph for Kimi-K2.5 (#20747) | `python/sglang/srt/models/kimi_k25.py` |
| 2026-03-17 | `18dd5c972` | 性能/后端优化 | [AMD] Fix AMD CI : stage-c-large-8-gpu-amd-mi35x (#20521) | `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/amd/test_kimi_k25_mxfp4.py` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-03-15 | `1c456a0af` | 缺陷修复 | VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282) | `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py` |
| 2026-03-12 | `1e2983c98` | 性能/后端优化 | [AMD] Fix FP8 assertion failure in aiter MLA decode by falling back to self.k_scale (#19935) | `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/accuracy/mi35x/test_kimi_k25_aiter_mla_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_kimi_k25_mxfp4_eval_mi35x.py` |
| 2026-03-10 | `5f717913a` | 性能/后端优化 | support Kimi-K2.5-w4a8 on ascend | `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_vl_moonvit.py` |
| 2026-03-06 | `011806c41` | 模型支持/运行时入口 | [Nightly] Add Kimi K2.5 nightly test (base + Eagle3 MTP), replace Kimi K2 (#19802) | `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_kimi_k25.py` |
| 2026-03-07 | `069d4c577` | 缺陷修复 | Fix Kimi K2.5 PP layer range exposure for PD disaggregation (#19959) | `python/sglang/srt/models/kimi_k25.py` |
| 2026-03-04 | `738ebfd33` | 性能/后端优化 | KDA: fuse qkv conv and support stride for fused_sigmoid_gating_delta_rule_update_kernel (#19506) | `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` |
| 2026-03-04 | `85f7a0aa3` | 模型支持/运行时入口 | feat: support Kimi K2.5 for Eagle3 (#19689) | `python/sglang/srt/models/kimi_k25.py` |
| 2026-03-03 | `dbf1247fe` | 模型支持/运行时入口 | Add KimiK2Detector with tool interruption support (#19696) | `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/parser/test_reasoning_parser.py` |
| 2026-03-02 | `c64274c74` | 性能/后端优化 | Piecewise Cuda Graph set default (#16331) | `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-02-27 | `d2885a909` | 性能/后端优化 | [Qwen3-Next] Support gdn fused_rms_norm_gated (#19434) | `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-02-27 | `eef44ec91` | 性能/后端优化 | [NPU]kimi k2 thinking bugfix (#19387) | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` |
| 2026-02-27 | `a1ef8e2cc` | 性能/后端优化 | [AMD] optimize Kimi K2.5 fused_moe_triton performance by tuning (#19228) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py` |
| 2026-02-26 | `86eb80007` | 性能/后端优化 | [NPU] support Kimi-K2.5 on NPU (#19331) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/models/kimi_k25.py` |
| 2026-02-25 | `4a3a787f1` | 缺陷修复 | [Fix] Kimi K2.5 support pp (#18434) | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/kimi_k25.py` |
| 2026-02-21 | `677b66af8` | 缺陷修复 | fix KimiK2Detector regex patterns with re.DOTALL (#19120) | `python/sglang/srt/function_call/kimik2_detector.py` |
| 2026-02-18 | `5a7ae059e` | 模型支持/运行时入口 | Add DP ViT support for Kimi K2.5 (#18689) | `python/sglang/srt/models/kimi_k25.py` |
| 2026-02-17 | `bf5238835` | 性能/后端优化 | [PCG] support piecewise cuda graph for kimi-linear model (#18849) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-02-15 | `b992828ad` | 缺陷修复 | fix: fix bug on kimi2.5 with dp2 and tp4 (#18604) | `python/sglang/srt/layers/attention/trtllm_mla_backend.py` |
| 2026-02-11 | `dc1309fc7` | 通用实现调整 | Avoid kimi linear stream sync (#16186) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` |
| 2026-02-10 | `d84d2063d` | 缺陷修复 | [AMD] Fix Janus-Pro crash and add Kimi-K2.5 nightly test (#18269) | `.github/workflows/nightly-test-amd.yml`, `python/sglang/srt/models/deepseek_janus_pro.py`, `test/registered/amd/accuracy/mi30x/test_kimi_k25_eval_amd.py` |
| 2026-02-09 | `071bf2ce0` | 性能/后端优化 | [Kimi-K2.5] Fix missing `quant_config` in `KimiK25` (#18440) | `python/sglang/srt/models/kimi_k25.py` |
| 2026-02-08 | `7b8365931` | 性能/后端优化 | fix: fix NVFP4 Kimi-K2.5 weight mapping and exclude list (#18370) | `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/kimi_k25.py` |
| 2026-02-05 | `599c5f492` | 性能/后端优化 | fix kimi k2.5's moe gemm config init (#18064) | `python/sglang/srt/managers/scheduler.py` |
| 2026-02-04 | `6fd878b41` | 性能/后端优化 | [AMD] Add kimi mi35x nightly test, folder organization and several stability fixes (#17895) | `.github/workflows/nightly-test-amd.yml`, `python/sglang/test/nightly_utils.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py` |
| 2026-02-04 | `37c33cc0a` | 性能/后端优化 | fuse qkvbfg linear into one gemm and f_b g_b into batched gemm. (#17801) | `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-02-02 | `d11ccc0a0` | 缺陷修复 | fix: avoid double reduce in VLM dp attention (#17991) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/kimi_k25.py`, `test/registered/distributed/test_dp_attention.py` |
| 2026-02-01 | `56907cbcb` | 模型支持/运行时入口 | Move deleted 8-GPU tests to test/manual/ (#18060) | `test/manual/models/test_kimi_k2_models.py`, `test/manual/models/test_mistral_large3_basic.py` |
| 2026-01-31 | `a0bae4c34` | 性能/后端优化 | Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299) | `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py` |
| 2026-01-30 | `70db3398d` | 模型支持/运行时入口 | [NPU] enhance accuracy for model kimi-vl-a3b-instruct (#17480) | `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `test/registered/ascend/vlm_models/test_ascend_kimi_vl_a3b_instruct.py` |
| 2026-01-28 | `9409c4359` | 缺陷修复 | Fix flaky tool calls in the Kimi K2.5 model (#17914) | `python/sglang/srt/server_args.py` |
| 2026-01-28 | `3c34d2c3e` | 缺陷修复 | [FIX] kimi_k2 reasoning parser (#17901) | `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/parser/reasoning_parser.py` |
| 2026-01-28 | `f8636fbb2` | 性能/后端优化 | [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI (#17523) | `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` |
| 2026-01-28 | `52bca4287` | 性能/后端优化 | [AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites (#17633) | `.github/workflows/pr-test-amd.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/amd/test_deepseek_v32_basic.py` |
| 2026-01-27 | `d90c0837e` | 模型支持/运行时入口 | [hybrid-model] clean up and consolidate redundant fields in RadixLinearAttention (#17660) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-01-27 | `479ab7a4e` | 模型支持/运行时入口 | model: support Kimi-K2.5 (#17789) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/kimi_k25.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-01-26 | `738b1ac98` | 模型支持/运行时入口 | [AMD CI] Add moonshotai/Kimi-K2-Instruct-0905 testcases (#17656) | `.github/workflows/pr-test-amd.yml`, `test/registered/amd/test_kimi_k2_instruct.py` |
| 2026-01-26 | `1e8db1829` | 模型支持/运行时入口 | [Kimi-Linear] Remove duplicated code in kimi-linear (#17731) | `python/sglang/srt/models/kimi_linear.py` |
| 2026-01-25 | `2c1e2674c` | 性能/后端优化 | [misc] replace existing tool call code with new crate package (#17720) | `sgl-model-gateway/src/tool_parser/errors.rs`, `sgl-model-gateway/src/tool_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/mod.rs` |
| 2026-01-25 | `912349143` | 调度/缓存/PD | A few updates to the night tests (#17694) | `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-25 | `6af22f8db` | 模型支持/运行时入口 | use published reasoning parser crate (#17709) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/reasoning_parser/README.md` |
| 2026-01-24 | `0c8165ffb` | 模型支持/运行时入口 | [Kimi-Linear] Refactor Kimi-Linear to support RadixLinearAttention (#17506) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-01-24 | `176da1bbd` | 性能/后端优化 | Fix: mistake sigmoid in kda (#17508) | `python/sglang/srt/models/kimi_linear.py`, `test/registered/attention/test_kda_kernels.py` |
| 2026-01-22 | `5d299c25c` | 性能/后端优化 | [NPU] bugfix with Kimi-k2 and bge-reranker-v2 model (#17478) | `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `python/sglang/srt/layers/rotary_embedding.py` |
| 2026-01-21 | `bcc6d84f9` | 性能/后端优化 | Use fused_sigmoid_gating_delta_rule_update_kernel for KDA (#17108) | `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-01-20 | `e6b7c0494` | 模型支持/运行时入口 | [Kimi-Linear] Refactor kimi-linear gate calculation to avoid duplicated code (#17160) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-01-15 | `655d2c7c2` | 缺陷修复 | fix: adding matrix partitioning for h200 and b200 nightly tests (#17091) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-15 | `d1110e1c3` | 模型支持/运行时入口 | docs only add kimi k2 thinking and kimi linear (#15789) | `docs/supported_models/generative_models.md` |
| 2026-01-14 | `aa2b4f766` | 缺陷修复 | fix: renaming test file and job names + skip blocking llama4 nightly (#16971) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-07 | `63cc97f4e` | 调度/缓存/PD | ci: migrate 2-GPU tests to test/registered/ (#16529) | `.github/workflows/pr-test.yml`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-01-06 | `534976429` | 缺陷修复 | fix: kimi k2 thinking accuracy threshold change (#16585) | `test/registered/8-gpu-models/test_kimi_k2.py` |
| 2026-01-05 | `c80c0e0fc` | 缺陷修复 | fix: adding multi-threading for kimi weights loading in pr test (#16538) | `test/srt/models/test_kimi_k2_models.py` |
| 2026-01-04 | `f84487af5` | 性能/后端优化 | [model-gateway] : Rust integration tests for integration_mock replacement (#16441) | `.pre-commit-config.yaml`, `sgl-model-gateway/py_test/unit/__init__.py`, `sgl-model-gateway/tests/common/mock_mcp_server.rs` |
| 2026-01-05 | `12df16607` | 模型支持/运行时入口 | Tiny speed up kimi detokenizer by 10x (#16427) | `python/sglang/srt/environ.py`, `python/sglang/srt/utils/hf_transformers_utils.py`, `python/sglang/srt/utils/patch_tokenizer.py` |
| 2026-01-02 | `d8ac5eecf` | 性能/后端优化 | [model-gateway] bug fix on module name (#16332) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/benches/manual_policy_benchmark.rs`, `sgl-model-gateway/benches/request_processing.rs` |
| 2025-12-31 | `f35b5da52` | 性能/后端优化 | [CI] Append test variant name to markdown report header in nightly test (#16166) | `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py` |
| 2025-12-22 | `989d4b301` | 性能/后端优化 | [CI] Migrate nightly tests to test/registered/ (#15582) | `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py` |
| 2025-12-20 | `96740d698` | 性能/后端优化 | feature: revamp nightly tests with combined runner (#15324) | `.github/workflows/nightly-test-nvidia.yml`, `test/nightly/accuracy_test_runner.py`, `test/nightly/nightly_utils.py` |

## Per-Commit Audit Cards

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

### Commit `8c3ccef2d` - Fix Kimi K2.5 dp attention+ spec decoding launch crash (#21391)

- Full hash: `8c3ccef2d94e185159badc74dcbe07885ad21ff3`
- Date/author: 2026-03-26 / Qiaolin Yu
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/llama_eagle3.py`, `test/registered/8-gpu-models/test_kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/llama_eagle3.py`
  - tests: `test/registered/8-gpu-models/test_kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `01ccdb91b` - [Fix] Add EPLB rebalance support for Kimi K2.5 (#21004)

- Full hash: `01ccdb91b162cc399a5bf3a8db3fd43d457bb52b`
- Date/author: 2026-03-26 / MARATRIX
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `27ac831a8` - docs: improve CI and testing documentation (#21202)

- Full hash: `27ac831a84d061ad31743554da04c00afce100d3`
- Date/author: 2026-03-23 / Lianmin Zheng
- Auto category: 性能/后端优化
- Main files: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `README.md`, `docker/xpu.Dockerfile`, `docs/index.rst` 等 110 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`
  - docs-bench: `docs/index.rst`
  - other: `README.md`; `docker/xpu.Dockerfile`; `python/sglang/srt/utils/hf_transformers_utils.py`; `scripts/ci/amd/check_vram_clear.sh`; `scripts/ci/amd/ensure_vram_clear.sh`
  - runtime-model: `python/sglang/srt/configs/model_config.py`
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `python/sglang/srt/layers/quantization/fp8_kernel.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/mem_cache/hisparse_memory_pool.py`; `python/sglang/srt/mem_cache/storage/hf3fs/test_hf3fs_utils.py`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/test_add_constant.py`; `python/sglang/jit_kernel/tests/test_awq_dequantize.py`; `python/sglang/jit_kernel/tests/test_awq_marlin_moe_repack.py`; `python/sglang/jit_kernel/tests/test_awq_marlin_repack.py`; `python/sglang/jit_kernel/tests/test_clamp_position.py`; `python/sglang/jit_kernel/tests/test_concat_mla.py`; `python/sglang/jit_kernel/tests/test_cutedsl_gdn.py` 等 95 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `104b10f70` - refactor: consolidate is_in_ci (jit_kernel, sgl-kernel benchmarks, tests) (#21009)

- Full hash: `104b10f70af602a10fbcdc5aef2f6fba13da0eed`
- Date/author: 2026-03-20 / Lianmin Zheng
- Auto category: 性能/后端优化
- Main files: `.claude/skills/add-sgl-kernel/SKILL.md`, `benchmark/kernels/all_reduce/benchmark_torch_symm_mem.py`, `python/sglang/jit_kernel/benchmark/bench_awq_dequantize.py`, `python/sglang/jit_kernel/benchmark/bench_awq_marlin_moe_repack.py`, `python/sglang/jit_kernel/benchmark/bench_awq_marlin_repack.py`, `python/sglang/jit_kernel/benchmark/bench_concat_mla.py`, `python/sglang/jit_kernel/benchmark/bench_fused_add_rmsnorm.py`, `python/sglang/jit_kernel/benchmark/bench_fused_norm_scale_shift.py` 等 44 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/kernels/all_reduce/benchmark_torch_symm_mem.py`
  - runtime-perf: `.claude/skills/add-sgl-kernel/SKILL.md`; `python/sglang/jit_kernel/benchmark/bench_awq_dequantize.py`; `python/sglang/jit_kernel/benchmark/bench_awq_marlin_moe_repack.py`; `python/sglang/jit_kernel/benchmark/bench_awq_marlin_repack.py`; `python/sglang/jit_kernel/benchmark/bench_concat_mla.py`; `python/sglang/jit_kernel/benchmark/bench_fused_add_rmsnorm.py`; `python/sglang/jit_kernel/benchmark/bench_fused_norm_scale_shift.py`; `python/sglang/jit_kernel/benchmark/bench_gptq_marlin.py` 等 41 个文件
  - tests: `test/registered/language/test_srt_backend.py`; `test/registered/moe/test_hybrid_dp_ep_tp_mtp.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `cea79530f` - ci: merge CPU default and stage-a-cpu-only suites (#20992)

- Full hash: `cea79530f818b82d7d90c4832f88751e6deb2087`
- Date/author: 2026-03-20 / Lianmin Zheng
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test.yml`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_executor.py`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_planner.py`, `test/registered/debug_utils/comparator/aligner/reorderer/test_executor.py`, `test/registered/debug_utils/comparator/aligner/reorderer/test_planner.py`, `test/registered/debug_utils/comparator/aligner/test_axis_aligner.py`, `test/registered/debug_utils/comparator/aligner/token_aligner/test_aux_loader.py`, `test/registered/debug_utils/comparator/aligner/token_aligner/test_aux_plugins.py` 等 54 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test.yml`
  - tests: `test/registered/debug_utils/comparator/aligner/entrypoint/test_executor.py`; `test/registered/debug_utils/comparator/aligner/entrypoint/test_planner.py`; `test/registered/debug_utils/comparator/aligner/reorderer/test_executor.py`; `test/registered/debug_utils/comparator/aligner/reorderer/test_planner.py`; `test/registered/debug_utils/comparator/aligner/test_axis_aligner.py`; `test/registered/debug_utils/comparator/aligner/token_aligner/test_aux_loader.py`; `test/registered/debug_utils/comparator/aligner/token_aligner/test_aux_plugins.py`; `test/registered/debug_utils/comparator/aligner/token_aligner/test_concat_steps.py` 等 53 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `db995fba4` - perf(kimi_linear): replace einops rearrange with native torch ops in Kimi-Linear KDA path (#20396)

- Full hash: `db995fba4790c9010af1aeff6022569504706f17`
- Date/author: 2026-03-19 / Vedant V Jhaveri
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/models/kimi_linear.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kda_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c562e0d13` - [feat] Enhance Kimi-K2/K2.5 function call and reasoning detection (#19552)

- Full hash: `c562e0d13ba9c1513122ed583fabede207d8813a`
- Date/author: 2026-03-20 / AlfredYong
- Auto category: 测试/文档/基准
- Main files: `python/sglang/srt/function_call/kimik2_detector.py`, `test/registered/function_call/test_kimik2_detector.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/function_call/kimik2_detector.py`
  - tests: `test/registered/function_call/test_kimik2_detector.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `24a27d532` - vlm: support piecewise cuda graph for Kimi-K2.5 (#20747)

- Full hash: `24a27d532084dc47e37334a6bb131d3d9b681ffd`
- Date/author: 2026-03-18 / Yuhao Yang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `18dd5c972` - [AMD] Fix AMD CI : stage-c-large-8-gpu-amd-mi35x (#20521)

- Full hash: `18dd5c972d03942ded6fd9b608f8ed3f2325d603`
- Date/author: 2026-03-17 / YC Yen-Ching Tseng
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/amd/test_kimi_k25_mxfp4.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`
  - tests: `test/registered/amd/test_kimi_k25_mxfp4.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `1c456a0af` - VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282)

- Full hash: `1c456a0af540b5fd092a90d3af7627be973416a5`
- Date/author: 2026-03-15 / Yuhao Yang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/idefics2.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_vl_moonvit.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/conv.py`
  - runtime-model: `python/sglang/srt/models/clip.py`; `python/sglang/srt/models/dots_vlm_vit.py`; `python/sglang/srt/models/glm4v.py`; `python/sglang/srt/models/idefics2.py`; `python/sglang/srt/models/internvl.py`; `python/sglang/srt/models/kimi_k25.py`; `python/sglang/srt/models/kimi_vl_moonvit.py`; `python/sglang/srt/models/midashenglm.py` 等 16 个文件
  - tests: `test/unit/test_conv_layer.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1e2983c98` - [AMD] Fix FP8 assertion failure in aiter MLA decode by falling back to self.k_scale (#19935)

- Full hash: `1e2983c98ebd53c60df3581cc31627d75f24b811`
- Date/author: 2026-03-12 / jacky.cheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/accuracy/mi35x/test_kimi_k25_aiter_mla_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_kimi_k25_mxfp4_eval_mi35x.py`, `test/registered/amd/test_kimi_k25_mxfp4.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
  - tests: `test/registered/amd/accuracy/mi35x/test_kimi_k25_aiter_mla_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_kimi_k25_mxfp4_eval_mi35x.py`; `test/registered/amd/test_kimi_k25_mxfp4.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5f717913a` - support Kimi-K2.5-w4a8 on ascend

- Full hash: `5f717913a04d74e10ee5ab7a98a6a9d3e2e57953`
- Date/author: 2026-03-10 / khalilzhk
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_vl_moonvit.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`; `python/sglang/srt/models/kimi_vl_moonvit.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `011806c41` - [Nightly] Add Kimi K2.5 nightly test (base + Eagle3 MTP), replace Kimi K2 (#19802)

- Full hash: `011806c41999848f6625e8e31aca7c3a9686183d`
- Date/author: 2026-03-06 / Alison Shao
- Auto category: 模型支持/运行时入口
- Main files: `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_kimi_k25.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `069d4c577` - Fix Kimi K2.5 PP layer range exposure for PD disaggregation (#19959)

- Full hash: `069d4c577b39cc6fcd56f0ff138df7c8c793ea82`
- Date/author: 2026-03-07 / MARATRIX
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `738ebfd33` - KDA: fuse qkv conv and support stride for fused_sigmoid_gating_delta_rule_update_kernel (#19506)

- Full hash: `738ebfd3301c8317df3e946c2d14efe543260fe8`
- Date/author: 2026-03-04 / strgrb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/models/kimi_linear.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/mamba_utils.py`; `python/sglang/srt/models/kimi_linear.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/srt/layers/attention/linear/kda_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `85f7a0aa3` - feat: support Kimi K2.5 for Eagle3 (#19689)

- Full hash: `85f7a0aa3077e9bdec83ca9eb7f3687d3d51050b`
- Date/author: 2026-03-04 / yefei12
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `dbf1247fe` - Add KimiK2Detector with tool interruption support (#19696)

- Full hash: `dbf1247fe08ba390599e070db1174de0ae5a4d7d`
- Date/author: 2026-03-03 / Xinyuan Tong
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/parser/test_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/parser/reasoning_parser.py`
  - tests: `test/registered/parser/test_reasoning_parser.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `d2885a909` - [Qwen3-Next] Support gdn fused_rms_norm_gated (#19434)

- Full hash: `d2885a9094c3847769923322e51a85841a552662`
- Date/author: 2026-02-27 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`; `python/sglang/srt/layers/attention/fla/kda.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `eef44ec91` - [NPU]kimi k2 thinking bugfix (#19387)

- Full hash: `eef44ec916fe24119e68117b2deeea3b03e7a88f`
- Date/author: 2026-02-27 / KnightLTC
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a1ef8e2cc` - [AMD] optimize Kimi K2.5 fused_moe_triton performance by tuning  (#19228)

- Full hash: `a1ef8e2cc0976eeb0b2bacf265bed80c645a7ded`
- Date/author: 2026-02-27 / RoyWang
- Auto category: 性能/后端优化
- Main files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=384,N=128,device_name=,dtype=int4_w4a16.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=384,N=128,device_name=,dtype=int4_w4a16_down.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=384,N=128,device_name=,dtype=int4_w4a16.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_4_0/E=384,N=128,device_name=,dtype=int4_w4a16_down.json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `86eb80007` - [NPU] support Kimi-K2.5 on NPU (#19331)

- Full hash: `86eb80007e78b61bc8bf91ebe48aa8ee2eb19f01`
- Date/author: 2026-02-26 / khalilzhk
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
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

### Commit `677b66af8` - fix KimiK2Detector regex patterns with re.DOTALL (#19120)

- Full hash: `677b66af805d93f7a26e9cf96b7b243eb1beaee1`
- Date/author: 2026-02-21 / Xinyuan Tong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/function_call/kimik2_detector.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/function_call/kimik2_detector.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `5a7ae059e` - Add DP ViT support for Kimi K2.5 (#18689)

- Full hash: `5a7ae059e37f2c481462a2ad965467264718c461`
- Date/author: 2026-02-18 / Yuhao Yang
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `bf5238835` - [PCG] support piecewise cuda graph for kimi-linear model (#18849)

- Full hash: `bf523883545917d225cd5839d0ac8b0d715c5515`
- Date/author: 2026-02-17 / Minglei Zhu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py`, `test/registered/models/test_kimi_linear_models_pcg.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/radix_linear_attention.py`
  - tests: `test/registered/models/test_kimi_linear_models_pcg.py`
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

### Commit `b992828ad` - fix: fix bug on kimi2.5 with dp2 and tp4 (#18604)

- Full hash: `b992828ad272dbea38446b1b41c45fb78d049547`
- Date/author: 2026-02-15 / haowen-han
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `dc1309fc7` - Avoid kimi linear stream sync (#16186)

- Full hash: `dc1309fc7e4a1f338a13bd3f91a549ac766d6cc0`
- Date/author: 2026-02-11 / Yi Zhong
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d84d2063d` - [AMD] Fix Janus-Pro crash and add Kimi-K2.5 nightly test  (#18269)

- Full hash: `d84d2063d32a881842843bc0e991c01e725445b3`
- Date/author: 2026-02-10 / Michael
- Auto category: 缺陷修复
- Main files: `.github/workflows/nightly-test-amd.yml`, `python/sglang/srt/models/deepseek_janus_pro.py`, `test/registered/amd/accuracy/mi30x/test_kimi_k25_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_kimi_k25_eval_mi35x.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - runtime-model: `python/sglang/srt/models/deepseek_janus_pro.py`
  - tests: `test/registered/amd/accuracy/mi30x/test_kimi_k25_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_kimi_k25_eval_mi35x.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `071bf2ce0` - [Kimi-K2.5] Fix missing `quant_config` in `KimiK25` (#18440)

- Full hash: `071bf2ce094c6f45e6039bf5f858f271f8be9f0b`
- Date/author: 2026-02-09 / Mohammad Miadh Angkad
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `7b8365931` - fix: fix NVFP4 Kimi-K2.5 weight mapping and exclude list (#18370)

- Full hash: `7b836593108559f8db954375f0e64bb38637363e`
- Date/author: 2026-02-08 / Mohammad Miadh Angkad
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/kimi_k25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/modelopt_quant.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `599c5f492` - fix kimi k2.5's moe gemm config init (#18064)

- Full hash: `599c5f4922579742a0c65a4c2fb4503dd63f7ae3`
- Date/author: 2026-02-05 / yinghui
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/managers/scheduler.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
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

### Commit `37c33cc0a` - fuse qkvbfg linear into one gemm and f_b g_b into batched gemm. (#17801)

- Full hash: `37c33cc0aa6213fd4abcfb40c3e1d71dde484295`
- Date/author: 2026-02-04 / strgrb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/kimi_linear.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d11ccc0a0` - fix: avoid double reduce in VLM dp attention (#17991)

- Full hash: `d11ccc0a0aa86baa465072e1969b6fc9438cc04a`
- Date/author: 2026-02-02 / Yuhao Yang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/kimi_k25.py`, `test/registered/distributed/test_dp_attention.py`, `test/registered/distributed/test_dp_attention_large.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_k25.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
  - tests: `test/registered/distributed/test_dp_attention.py`; `test/registered/distributed/test_dp_attention_large.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `56907cbcb` - Move deleted 8-GPU tests to test/manual/ (#18060)

- Full hash: `56907cbcb190affa4dfa3473cbe7534622f2f8b1`
- Date/author: 2026-02-01 / Alison Shao
- Auto category: 模型支持/运行时入口
- Main files: `test/manual/models/test_kimi_k2_models.py`, `test/manual/models/test_mistral_large3_basic.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/manual/models/test_kimi_k2_models.py`; `test/manual/models/test_mistral_large3_basic.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `a0bae4c34` - Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299)

- Full hash: `a0bae4c34349d09b3ad71db71d4fc3f4f32f221e`
- Date/author: 2026-01-31 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py` 等 39 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v32_basic.py`; `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v3_basic.py`; `test/registered/8-gpu-models/test_deepseek_v3_mtp.py` 等 37 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `9409c4359` - Fix flaky tool calls in the Kimi K2.5 model (#17914)

- Full hash: `9409c43593f2d6d64595981abf216a15752b0875`
- Date/author: 2026-01-28 / Xinyuan Tong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `3c34d2c3e` - [FIX] kimi_k2 reasoning parser (#17901)

- Full hash: `3c34d2c3ebfe0d4dfc02353980ed50a350fa0324`
- Date/author: 2026-01-28 / Xinyuan Tong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/parser/reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/parser/reasoning_parser.py`
  - runtime-model: `python/sglang/srt/entrypoints/openai/serving_chat.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `52bca4287` - [AMD] CI - enable deepseekv3.2 on MI325-8gpu and merge perf/accuracy test suites into stage-b suites (#17633)

- Full hash: `52bca4287033a0e514d64e2a8798e45b132f9a4b`
- Date/author: 2026-01-28 / YC Tseng
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test-amd.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_kimi_k2_instruct.py`, `test/registered/attention/test_triton_sliding_window.py`, `test/registered/eval/test_eval_accuracy_large.py`, `test/registered/eval/test_moe_eval_accuracy_large.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-amd.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `test/registered/amd/test_deepseek_v32_basic.py`; `test/registered/amd/test_deepseek_v32_mtp.py`; `test/registered/amd/test_kimi_k2_instruct.py`; `test/registered/attention/test_triton_sliding_window.py`; `test/registered/eval/test_eval_accuracy_large.py`; `test/registered/eval/test_moe_eval_accuracy_large.py`; `test/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `d90c0837e` - [hybrid-model] clean up and consolidate redundant fields in RadixLinearAttention (#17660)

- Full hash: `d90c0837e5b812864a7570234b1a498740a01e85`
- Date/author: 2026-01-27 / Minglei Zhu
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/radix_linear_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `479ab7a4e` - model: support Kimi-K2.5 (#17789)

- Full hash: `479ab7a4e7e40d4227d892f9d3da871424a316bb`
- Date/author: 2026-01-27 / Yuhao Yang
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/kimi_k25.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/kimi_k25.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/kimi_k25.py`; `python/sglang/srt/parser/reasoning_parser.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/kimi_k25.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/models/kimi_k25.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `738b1ac98` - [AMD CI] Add moonshotai/Kimi-K2-Instruct-0905 testcases (#17656)

- Full hash: `738b1ac988c36c1c5d03cf86f0806bdfd115720c`
- Date/author: 2026-01-26 / sogalin
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/pr-test-amd.yml`, `test/registered/amd/test_kimi_k2_instruct.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-amd.yml`
  - tests: `test/registered/amd/test_kimi_k2_instruct.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `1e8db1829` - [Kimi-Linear] Remove duplicated code in kimi-linear (#17731)

- Full hash: `1e8db1829096392a7b2bebc8fd92b239495ec2cd`
- Date/author: 2026-01-26 / Yuan Luo
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/kimi_linear.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `2c1e2674c` - [misc] replace existing tool call code with new crate package (#17720)

- Full hash: `2c1e2674ccca62d9c6dda72dd4a8639bd1f571eb`
- Date/author: 2026-01-25 / Simo Lin
- Auto category: 性能/后端优化
- Main files: `sgl-model-gateway/src/tool_parser/errors.rs`, `sgl-model-gateway/src/tool_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/mod.rs`, `sgl-model-gateway/src/tool_parser/parsers/deepseek.rs`, `sgl-model-gateway/src/tool_parser/parsers/glm4_moe.rs`, `sgl-model-gateway/src/tool_parser/parsers/helpers.rs`, `sgl-model-gateway/src/tool_parser/parsers/json.rs`, `sgl-model-gateway/src/tool_parser/parsers/kimik2.rs` 等 39 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `sgl-model-gateway/src/tool_parser/errors.rs`; `sgl-model-gateway/src/tool_parser/factory.rs`; `sgl-model-gateway/src/tool_parser/mod.rs`; `sgl-model-gateway/src/tool_parser/parsers/deepseek.rs`; `sgl-model-gateway/src/tool_parser/parsers/helpers.rs`; `sgl-model-gateway/src/tool_parser/parsers/json.rs`; `sgl-model-gateway/src/tool_parser/parsers/kimik2.rs`; `sgl-model-gateway/src/tool_parser/parsers/llama.rs` 等 20 个文件
  - runtime-perf: `sgl-model-gateway/src/tool_parser/parsers/glm4_moe.rs`
  - tests: `sgl-model-gateway/tests/tool_parser/mod.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_deepseek.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_edge_cases.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_fallback.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_glm47_moe.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_glm4_moe.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_json.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_kimik2.rs` 等 18 个文件
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

### Commit `6af22f8db` - use published reasoning parser crate (#17709)

- Full hash: `6af22f8dbf4852d3aec9df7c20a7b8361c9b2ddf`
- Date/author: 2026-01-25 / Simo Lin
- Auto category: 模型支持/运行时入口
- Main files: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/reasoning_parser/README.md`, `sgl-model-gateway/src/reasoning_parser/factory.rs`, `sgl-model-gateway/src/reasoning_parser/mod.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/base.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/deepseek_r1.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/glm45.rs` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `sgl-model-gateway/Cargo.toml`; `sgl-model-gateway/src/lib.rs`; `sgl-model-gateway/src/reasoning_parser/README.md`; `sgl-model-gateway/src/reasoning_parser/factory.rs`; `sgl-model-gateway/src/reasoning_parser/mod.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/base.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/deepseek_r1.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/glm45.rs` 等 14 个文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `0c8165ffb` - [Kimi-Linear] Refactor Kimi-Linear to support RadixLinearAttention (#17506)

- Full hash: `0c8165ffbd1bc7e7d6c64da1687d1718e42f2f4a`
- Date/author: 2026-01-24 / Yuan Luo
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/radix_linear_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `176da1bbd` - Fix: mistake sigmoid in kda (#17508)

- Full hash: `176da1bbddbed865759d97942cf8038fdac16e82`
- Date/author: 2026-01-24 / strgrb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/kimi_linear.py`, `test/registered/attention/test_kda_kernels.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
  - tests: `test/registered/attention/test_kda_kernels.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `5d299c25c` - [NPU] bugfix with Kimi-k2 and bge-reranker-v2 model (#17478)

- Full hash: `5d299c25c04a9e28170659b7588afcc0b6f84599`
- Date/author: 2026-01-22 / chenxu214
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/bert.py`, `test/registered/ascend/embedding_models/test_ascend_bge_large_en_v1_5.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
  - runtime-model: `python/sglang/srt/models/bert.py`
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
  - tests: `test/registered/ascend/embedding_models/test_ascend_bge_large_en_v1_5.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bcc6d84f9` - Use fused_sigmoid_gating_delta_rule_update_kernel for KDA (#17108)

- Full hash: `bcc6d84f93fbfbbb64bf4c86356147acee042750`
- Date/author: 2026-01-21 / strgrb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/kimi_linear.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e6b7c0494` - [Kimi-Linear] Refactor kimi-linear gate calculation to avoid duplicated code (#17160)

- Full hash: `e6b7c04947eebc2239b7937ed7f509386d208f11`
- Date/author: 2026-01-20 / Yuan Luo
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/kimi_linear.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
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

### Commit `d1110e1c3` - docs only add kimi k2 thinking and kimi linear  (#15789)

- Full hash: `d1110e1c3e1a2f68cac4541261169545a6fc2547`
- Date/author: 2026-01-15 / Yi Zhong
- Auto category: 模型支持/运行时入口
- Main files: `docs/supported_models/generative_models.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/supported_models/generative_models.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

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

### Commit `63cc97f4e` - ci: migrate 2-GPU tests to test/registered/ (#16529)

- Full hash: `63cc97f4ef7a4641185a7e3655c75a5d039988c2`
- Date/author: 2026-01-07 / Alison Shao
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/pr-test.yml`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/model_loader/weight_utils.py`, `scripts/ci/slash_command_handler.py`, `test/registered/disaggregation/test_disaggregation_basic.py`, `test/registered/distributed/test_data_parallelism.py`, `test/registered/distributed/test_dp_attention.py`, `test/registered/distributed/test_load_weights_from_remote_instance.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test.yml`
  - other: `python/sglang/srt/model_loader/weight_utils.py`; `scripts/ci/slash_command_handler.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`
  - tests: `test/registered/disaggregation/test_disaggregation_basic.py`; `test/registered/distributed/test_data_parallelism.py`; `test/registered/distributed/test_dp_attention.py`; `test/registered/distributed/test_load_weights_from_remote_instance.py`; `test/registered/hicache/test_hicache_storage_3fs_backend.py`; `test/registered/hicache/test_hicache_storage_file_backend.py`; `test/registered/hicache/test_hicache_storage_mooncake_backend.py`; `test/registered/models/test_kimi_linear_models.py` 等 10 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `534976429` - fix: kimi k2 thinking accuracy threshold change (#16585)

- Full hash: `53497642985aa1184cfa63378612b6db10599782`
- Date/author: 2026-01-06 / Douglas Yang
- Auto category: 缺陷修复
- Main files: `test/registered/8-gpu-models/test_kimi_k2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/8-gpu-models/test_kimi_k2.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `c80c0e0fc` - fix: adding multi-threading for kimi weights loading in pr test (#16538)

- Full hash: `c80c0e0fc0d33e5e680e4dd0e32a6f3a17267471`
- Date/author: 2026-01-05 / Douglas Yang
- Auto category: 缺陷修复
- Main files: `test/srt/models/test_kimi_k2_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/srt/models/test_kimi_k2_models.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `f84487af5` - [model-gateway] : Rust integration tests for integration_mock replacement (#16441)

- Full hash: `f84487af591ba514b726a2daf72e438a41f417c0`
- Date/author: 2026-01-04 / Simo Lin
- Auto category: 性能/后端优化
- Main files: `.pre-commit-config.yaml`, `sgl-model-gateway/py_test/unit/__init__.py`, `sgl-model-gateway/tests/common/mock_mcp_server.rs`, `sgl-model-gateway/tests/common/mod.rs`, `sgl-model-gateway/tests/common/test_certs.rs`, `sgl-model-gateway/tests/common/test_config.rs`, `sgl-model-gateway/tests/common/tls_mock_worker.rs`, `sgl-model-gateway/tests/header_forwarding_test.rs` 等 48 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `.pre-commit-config.yaml`
  - tests: `sgl-model-gateway/py_test/unit/__init__.py`; `sgl-model-gateway/tests/common/mock_mcp_server.rs`; `sgl-model-gateway/tests/common/mod.rs`; `sgl-model-gateway/tests/common/test_certs.rs`; `sgl-model-gateway/tests/common/test_config.rs`; `sgl-model-gateway/tests/common/tls_mock_worker.rs`; `sgl-model-gateway/tests/header_forwarding_test.rs`; `sgl-model-gateway/tests/payload_size_test.rs` 等 47 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `12df16607` - Tiny speed up kimi detokenizer by 10x (#16427)

- Full hash: `12df16607b3d74f21caf62d68a9882abe3f1e901`
- Date/author: 2026-01-05 / fzyzcjy
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/utils/hf_transformers_utils.py`, `python/sglang/srt/utils/patch_tokenizer.py`, `test/srt/test_patch_tokenizer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/utils/hf_transformers_utils.py`; `python/sglang/srt/utils/patch_tokenizer.py`
  - tests: `test/srt/test_patch_tokenizer.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `d8ac5eecf` - [model-gateway] bug fix on module name (#16332)

- Full hash: `d8ac5eecf74e6edb9b5114980a9c71b1467c51ca`
- Date/author: 2026-01-02 / Chang Su
- Auto category: 性能/后端优化
- Main files: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/benches/manual_policy_benchmark.rs`, `sgl-model-gateway/benches/request_processing.rs`, `sgl-model-gateway/benches/router_registry_bench.rs`, `sgl-model-gateway/benches/tokenizer_benchmark.rs`, `sgl-model-gateway/benches/tool_parser_benchmark.rs`, `sgl-model-gateway/benches/tree_benchmark.rs`, `sgl-model-gateway/bindings/golang/src/client.rs` 等 66 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `sgl-model-gateway/tests/workflow_test.rs`
  - other: `sgl-model-gateway/Cargo.toml`; `sgl-model-gateway/benches/manual_policy_benchmark.rs`; `sgl-model-gateway/benches/request_processing.rs`; `sgl-model-gateway/benches/tokenizer_benchmark.rs`; `sgl-model-gateway/benches/tool_parser_benchmark.rs`; `sgl-model-gateway/benches/tree_benchmark.rs`; `sgl-model-gateway/bindings/golang/src/client.rs`; `sgl-model-gateway/bindings/golang/src/grpc_converter.rs` 等 19 个文件
  - runtime-model: `sgl-model-gateway/benches/router_registry_bench.rs`; `sgl-model-gateway/src/routers/grpc/harmony/mod.rs`
  - tests: `sgl-model-gateway/tests/api_endpoints_test.rs`; `sgl-model-gateway/tests/auth_integration_test.rs`; `sgl-model-gateway/tests/cache_aware_backward_compat_test.rs`; `sgl-model-gateway/tests/chat_template_format_detection.rs`; `sgl-model-gateway/tests/chat_template_integration.rs`; `sgl-model-gateway/tests/chat_template_loading.rs`; `sgl-model-gateway/tests/common/mod.rs`; `sgl-model-gateway/tests/common/test_app.rs` 等 44 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f35b5da52` - [CI] Append test variant name to markdown report header in nightly test (#16166)

- Full hash: `f35b5da521bffa72404f45ad4a9e85727f12456b`
- Date/author: 2025-12-31 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/test_utils.py`, `test/manual/nightly/test_deepseek_v31_perf.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/nightly_bench_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/test_utils.py`; `test/manual/nightly/test_deepseek_v31_perf.py`; `test/manual/nightly/test_deepseek_v32_perf.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `989d4b301` - [CI] Migrate nightly tests to test/registered/ (#15582)

- Full hash: `989d4b301293ea8eb243d7c320c5c457cb718629`
- Date/author: 2025-12-22 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/vlm_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/run_combined_tests.py` 等 64 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/ascend/__init__.py`; `python/sglang/test/ascend/gsm8k_ascend_mixin.py`; `python/sglang/test/ascend/vlm_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/run_combined_tests.py`; `test/registered/8-gpu-models/test_deepseek_v31.py` 等 63 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `96740d698` - feature: revamp nightly tests with combined runner (#15324)

- Full hash: `96740d6983711d85a66b1ca4ebd6b83b3a40106b`
- Date/author: 2025-12-20 / Douglas Yang
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `test/nightly/accuracy_test_runner.py`, `test/nightly/nightly_utils.py`, `test/nightly/performance_test_runner.py`, `test/nightly/run_combined_tests.py`, `test/nightly/test_deepseek_v31_perf.py`, `test/nightly/test_deepseek_v32_gpqa.py`, `test/nightly/test_deepseek_v32_nsabackend.py` 等 23 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/nightly/accuracy_test_runner.py`; `test/nightly/nightly_utils.py`; `test/nightly/performance_test_runner.py`; `test/nightly/run_combined_tests.py`; `test/nightly/test_deepseek_v31_perf.py`; `test/nightly/test_deepseek_v32_gpqa.py`; `test/nightly/test_deepseek_v32_nsabackend.py`; `test/nightly/test_deepseek_v32_perf.py` 等 22 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.
