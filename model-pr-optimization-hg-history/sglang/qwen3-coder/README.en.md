# sglang Qwen3 Coder Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/function_call/qwen3_coder_detector.py` | no direct commit |
| `python/sglang/srt/models/qwen3.py` | `b63cd7645`, `e9d6aefa9`, `d1e95af28`, `365ca1edb`, `c64274c74` |
| `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` | `98f47d817` |
| `test/registered/amd/test_qwen3_coder_next_8gpu.py` | `98f47d817` |
| `test/registered/ascend/llm_models/test_npu_qwen3_coder_480b_a35b.py` | `895e56097` |
| `test/registered/lora/test_lora_qwen3.py` | `814202704` |
| `test/srt/cpu/test_qwen3.py` | no direct commit |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 80
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-05-07 | `9f67deca2` | 性能/后端优化 | 支持qwen3.5-awq模型 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py` |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `94a624b83` | 性能/后端优化 | 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子 | `python/sglang/srt/models/qwen3_5.py` |
| 2026-04-21 | `466a1d6a4` | 性能/后端优化 | 将qwen3_moe文件中的SGLANG_USE_FUSED_BAILING_RMS_ROTARY修改为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-04-09 | `b8cd509f4` | 性能/后端优化 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-04-02 | `28dec61dd` | 模型支持/运行时入口 | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py` |
| 2026-03-31 | `b63cd7645` | 性能/后端优化 | 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py` |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |
| 2026-03-26 | `7738d2be5` | 缺陷修复 | Revert "bugfix for weight loading for qwen3-next" (#21496) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-26 | `fb90c9d29` | 性能/后端优化 | [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047) | `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py` |
| 2026-03-26 | `0906e45ce` | 缺陷修复 | bugfix for weight loading for qwen3-next (#21313) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-25 | `f5c225eeb` | 缺陷修复 | [CI] Fix TestQwen35WithHiCache (#21371) | `test/registered/4-gpu-models/test_qwen35_hicache.py`, `test/registered/4-gpu-models/test_qwen35_models.py` |
| 2026-03-25 | `6b0f1e3b4` | 调度/缓存/PD | Update skip condition for TestQwen35PPAccuracy (#21370) | `test/registered/distributed/test_pp_single_node.py` |
| 2026-03-24 | `dac148167` | 性能/后端优化 | Enable the qwen3 test (#21195) | `python/sglang/srt/models/qwen3_moe.py`, `test/registered/4-gpu-models/test_qwen3_30b.py` |
| 2026-03-24 | `0986bed8e` | 缺陷修复 | [HiCache][HybridModel]: Support mamba state offloading & HybridCacheController (#20457) | `benchmark/hicache/bench_multiturn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py` |
| 2026-03-24 | `b4d3fb001` | 性能/后端优化 | [AMD] Add fused GemmaRMSNorm forward_hip to use aiter/vllm kernels for qwen3.5 (#21188) | `python/sglang/srt/layers/layernorm.py` |
| 2026-03-23 | `5bdc07d97` | 性能/后端优化 | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019) | `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-23 | `814202704` | 性能/后端优化 | ci: unify PR test suite naming (#21187) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-23 | `a094eb9c2` | 模型支持/运行时入口 | Temporarily disable flaky qwen3 cp test in CI (#21178) | `test/registered/4-gpu-models/test_qwen3_30b.py` |
| 2026-03-22 | `bb737d7a8` | 性能/后端优化 | Support Qwen3 MoE context parallel (#18233) | `python/sglang/srt/distributed/communication_op.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-03-21 | `852e112eb` | 缺陷修复 | [Qwen3.5] Fix broken pipeline parallelism layer splitting (#21070) | `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py` |
| 2026-03-21 | `3f883ebf2` | 缺陷修复 | Fix test_qwen35_models (#21081) | `test/registered/4-gpu-models/test_qwen35_models.py` |
| 2026-03-21 | `f97c09dac` | 性能/后端优化 | [AMD] Enable aiter unified attention for non-SWA models (Qwen3-VL) (#20897) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/server_args.py` |
| 2026-03-20 | `ec01ef909` | 性能/后端优化 | Fix torch.compile/dynamo crash with Qwen3 QK-norm in piecewise CUDA g… (#19818) | `python/sglang/jit_kernel/norm.py` |
| 2026-03-20 | `46a76af97` | 性能/后端优化 | [Bugifx] qwen3 rope parameter compatibility (#20931) | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-03-20 | `d9794ef9f` | 性能/后端优化 | [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj (#19321) | `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-19 | `dc6aa26ce` | 性能/后端优化 | [CPU] Add mrope kernel for Qwen3-vl (#12531) | `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/rope.cpp` |
| 2026-03-19 | `f85455ab2` | 缺陷修复 | [Bugfix] fix qwen3vl hang when --mm-enable-dp-encoder is enable (#20759) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-18 | `21c4fc633` | 缺陷修复 | [DP encoder] Fix `pos_emb `layer TP issue when DP encoder enabled for Qwen3 VL (#20788) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-18 | `0acc1d3c9` | 缺陷修复 | fix: change qwen 3.5 linear attention a_log to fp32 (#19961) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-18 | `97d5386a2` | 性能/后端优化 | Use TRTLLM allreduce fusion for Qwen 3.5 (#19889) | `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-17 | `4cc19862e` | 性能/后端优化 | [NVIDIA] Integrate FlashInfer decode kernel (Blackwell) for Qwen3.5 (#19150) | `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/server_args.py` |
| 2026-03-17 | `cfead25bb` | 缺陷修复 | [Qwen3.5] mamba slice fix (Prefill TP != Decode TP & decode TP size>1) (#20655) | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-03-17 | `210d0fbae` | 调度/缓存/PD | Update ascend docs (#20674) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-03-15 | `7142a594f` | 模型支持/运行时入口 | [CI]: Add CI For HiMambaRadixTree and qwen3.5 (#20540) | `.github/workflows/pr-test.yml`, `test/registered/4-gpu-models/test_qwen35_models.py` |
| 2026-03-15 | `1c456a0af` | 缺陷修复 | VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282) | `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py` |
| 2026-03-14 | `6c5bf53a3` | 模型支持/运行时入口 | [Doc] Clarify that --chat-template is required for Qwen3-Reranker (#20596) | `docs/supported_models/retrieval_ranking/rerank_models.md` |
| 2026-03-15 | `574dbe23b` | 性能/后端优化 | Add piecewise cuda graph for Qwen3-Next FP8 flashinfer_trtllm moe backend (#18184) | `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` |
| 2026-03-14 | `22e67876d` | 性能/后端优化 | [Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker (#18185) | `python/sglang/srt/models/qwen3_omni_moe.py` |
| 2026-03-14 | `c95dc88f8` | 模型支持/运行时入口 | [CI] migrate ascend-gptq from `test/srt` to `test/registered` (#19628) | `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/llm_models/test_ascend_qwen3_1_7b_gptq_int8.py` |
| 2026-03-13 | `9c8777c80` | 性能/后端优化 | [AMD][Qwen3.5] aiter a8w8 gemm configuration (#19826) | `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-03-12 | `067353f67` | 缺陷修复 | [Test] Refactor KL divergence and prefix cache branching to kits (#19715) | `python/sglang/test/kits/kl_divergence_kit.py`, `python/sglang/test/kits/prefix_cache_branching_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py` |
| 2026-03-11 | `9b55a98a6` | 性能/后端优化 | perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe… (#20386) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-03-11 | `ed42af99a` | 性能/后端优化 | [NPU] [Quantization] w4a4 MoE layer support (#18924) | `docs/platforms/ascend_npu_quantization.md`, `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py` |
| 2026-03-10 | `031d0a2aa` | 性能/后端优化 | [Qwen-MOE] Fix memory duplication issues in case layers weights are re-assigned during weight loading (#18255) | `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl_moe.py` |
| 2026-03-10 | `9884957c0` | 缺陷修复 | [NPU] Bugfix for qwen35 on NPU (#19756) | `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-03-09 | `cabe171b6` | 性能/后端优化 | Fix qwen3.5 mtp eplb related issues (#19767) | `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-03-09 | `fc543df28` | 模型支持/运行时入口 | [NPU] qwen3_vl encoder support graph | `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-07 | `7da590d4d` | 模型支持/运行时入口 | [Qwen3.5] Support Qwen3.5 Pipeline Parallelism (#19670) | `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py` |
| 2026-03-06 | `ac453b253` | 模型支持/运行时入口 | Add Qwen3.5-397B-A17B nightly test (8-GPU) (#19906) | `test/registered/8-gpu-models/test_qwen35.py` |
| 2026-03-06 | `f7de9375a` | 性能/后端优化 | [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775) | `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-03-04 | `9457c049e` | 调度/缓存/PD | [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-03-03 | `c6850ac30` | 性能/后端优化 | [AMD] Fix Qwen3-Coder-Next: Add missing k_scale/v_scale args to extend_attention_fwd in aiter_backend (#19736) | `python/sglang/srt/layers/attention/aiter_backend.py` |
| 2026-03-03 | `365ca1edb` | 性能/后端优化 | [NPU] bugs fix: fix a condition bug when using speculative inference on Qwen3 and Qwen3 moe (#19532) | `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py` |
| 2026-03-02 | `6b8e62f94` | 性能/后端优化 | [AMD] [Qwen 3.5 Day 0] Add Qwen 3.5 nightly accuracy tests (#19479) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `docs/basic_usage/popular_model_usage.rst` |
| 2026-03-03 | `3f9fc8b84` | 性能/后端优化 | [Qwen3.5] Fix missing `quant_config` in `Qwen3VL` (#19291) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-02 | `c64274c74` | 性能/后端优化 | Piecewise Cuda Graph set default (#16331) | `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-03-02 | `468e3dc56` | 通用实现调整 | [Qwen3.5] Set full attn_backend to trtllm_mha on SM100 by default when possible (#19030) | `python/sglang/srt/server_args.py` |
| 2026-03-02 | `98f47d817` | 模型支持/运行时入口 | [AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU (#18608) | `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py` |
| 2026-02-28 | `a2ea5941d` | 性能/后端优化 | [feat] Support nvfp4 quantized model of Qwen3-Next (#17627) | `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_fp4.py` |
| 2026-02-27 | `d2885a909` | 性能/后端优化 | [Qwen3-Next] Support gdn fused_rms_norm_gated (#19434) | `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-02-27 | `4f0f6cd9d` | 性能/后端优化 | Add torch.compile support for qwen3-next on CPU (#12444) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-02-27 | `d566816d8` | 缺陷修复 | fix qwen3_vl visual module loading (#19333) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-02-27 | `e4b708d3e` | 调度/缓存/PD | [Spec V2] Support specV2 for mamba hybrid attention (#18808) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py` |
| 2026-02-26 | `bdc1e46e5` | 缺陷修复 | [Qwen3.5] Qwen3.5-27B inference repeat bug fix (#19411) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-25 | `b3202fe6d` | 性能/后端优化 | [PCG] fix piecewise cuda graph for Qwen3.5 (#19220) | `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-26 | `b2c46fc60` | 性能/后端优化 | [AMD] Support Qwen3-Coder-Next on AMD platform (#18355) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-25 | `56891e46b` | 模型支持/运行时入口 | [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md` |
| 2026-02-25 | `d38c0e537` | 缺陷修复 | fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1 (#19070) | `python/sglang/srt/models/qwen3_5.py` |
| 2026-02-25 | `307a2b73e` | 性能/后端优化 | [AMD] add testcases for Qwen3 235b Instruct 2507 models (#18805) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/test_qwen3_instruct.py` |
| 2026-02-25 | `f75abb452` | 缺陷修复 | [Fix][Qwen3.5] Fix KV cache slice transfer for GQA models with replicated KV heads (#19086) | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-02-25 | `d0bb14003` | 性能/后端优化 | [NPU] bugfix for model Qwen3-Coder-Next at weight shape transpose for npu. (#18700) | `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` |
| 2026-02-24 | `73fe389dd` | 调度/缓存/PD | [Qwen3.5] Raise Exception when radix_cache and extra_buffer are enabled at the same time (#19169) | `python/sglang/srt/server_args.py` |
| 2026-02-24 | `31c7dc9d9` | 性能/后端优化 | [VLM] Introduce FlashInfer CUDNN Prefill as ViT Backend (#19003) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/server_args.py` |
| 2026-02-21 | `5995bfec6` | 性能/后端优化 | [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill (#18917) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-19 | `8541b1118` | 缺陷修复 | [Fix][Qwen3.5] Pass max_mamba_cache_size to mamba pool in disaggregation decode path (#19002) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-02-18 | `bba2fc49a` | 模型支持/运行时入口 | [Qwen3.5] Enable nvfp4 checkpoint (#18937) | `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |

## Per-Commit Audit Cards

### Commit `9f67deca2` - 支持qwen3.5-awq模型

- Full hash: `9f67deca24b100410fe69d142a4ebca4fe26cc34`
- Date/author: 2026-05-07 / maxiao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py`, `python/sglang/srt/utils/common.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/moe_wna16.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c1d308c60` - 修复qwen3.5-397b-fp8报错问题

- Full hash: `c1d308c602379d71d746bc50ed785c2bee05ba99`
- Date/author: 2026-04-29 / liucong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/index.py`; `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `32bd2422e` - 修复qwen3.5模型memory_Async问题

- Full hash: `32bd2422e7d17f0cee10413aad4a223ffb25dd74`
- Date/author: 2026-04-23 / liucong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/sampling/sampling_batch_info.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/sampling/sampling_batch_info.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `94a624b83` - 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子

- Full hash: `94a624b8364de497a4a7ee4a6f9def06e18d90c9`
- Date/author: 2026-04-23 / liucong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_5.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `466a1d6a4` - 将qwen3_moe文件中的SGLANG_USE_FUSED_BAILING_RMS_ROTARY修改为SGLANG_USE_FUSED_RMS_ROTARY

- Full hash: `466a1d6a4caa1403fb6608748c3111ddc152cdf2`
- Date/author: 2026-04-21 / liucong8560
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b8cd509f4` - [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能

- Full hash: `b8cd509f45f9a51adee404eb9104358653e869d1`
- Date/author: 2026-04-09 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `28dec61dd` - support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k

- Full hash: `28dec61dd674f482fe34b5251ff0cd050ca2184c`
- Date/author: 2026-04-02 / liucong
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b63cd7645` - 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY

- Full hash: `b63cd76459510fb534dde7d8df2ca438099aa881`
- Date/author: 2026-03-31 / liucong8560
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/qwen3.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/models/bailing_moe.py`
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

### Commit `7738d2be5` - Revert "bugfix for weight loading for qwen3-next" (#21496)

- Full hash: `7738d2be519eff05e35727fc19b6662c8913eaf3`
- Date/author: 2026-03-26 / Baizhou Zhang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `fb90c9d29` - [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047)

- Full hash: `fb90c9d298eeeb15fde5de1c7676cfc3d9a4b6ee`
- Date/author: 2026-03-26 / Liangsheng Yin
- Auto category: 性能/后端优化
- Main files: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/test/kits/eval_accuracy_kit.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_mimo_models.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `0906e45ce` - bugfix for weight loading for qwen3-next (#21313)

- Full hash: `0906e45cec97abf3aa8ee9cf8962f6a5d36ed4f1`
- Date/author: 2026-03-26 / McZyWu
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f5c225eeb` - [CI] Fix TestQwen35WithHiCache (#21371)

- Full hash: `f5c225eeba3c6f027e5e7691784249d6a667026f`
- Date/author: 2026-03-25 / Baizhou Zhang
- Auto category: 缺陷修复
- Main files: `test/registered/4-gpu-models/test_qwen35_hicache.py`, `test/registered/4-gpu-models/test_qwen35_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/4-gpu-models/test_qwen35_hicache.py`; `test/registered/4-gpu-models/test_qwen35_models.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `6b0f1e3b4` - Update skip condition for TestQwen35PPAccuracy (#21370)

- Full hash: `6b0f1e3b437dc6aabf933deab07c3a0daa137f7b`
- Date/author: 2026-03-25 / Shangming Cai
- Auto category: 调度/缓存/PD
- Main files: `test/registered/distributed/test_pp_single_node.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/distributed/test_pp_single_node.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `dac148167` - Enable the qwen3 test (#21195)

- Full hash: `dac148167c80c695b731cb45e8347f52af9b57be`
- Date/author: 2026-03-24 / Shunkangz
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_moe.py`, `test/registered/4-gpu-models/test_qwen3_30b.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_30b.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0986bed8e` - [HiCache][HybridModel]: Support mamba state offloading & HybridCacheController (#20457)

- Full hash: `0986bed8e279ce67659e4e473300fc3c5c717d6a`
- Date/author: 2026-03-24 / hzh0425
- Auto category: 缺陷修复
- Main files: `benchmark/hicache/bench_multiturn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hicache_storage.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/hicache/bench_multiturn.py`
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`; `python/sglang/srt/mem_cache/hicache_storage.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`; `python/sglang/srt/mem_cache/mamba_radix_cache.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b4d3fb001` - [AMD] Add fused GemmaRMSNorm forward_hip to use aiter/vllm kernels for qwen3.5 (#21188)

- Full hash: `b4d3fb001d435a9792a1a3896f2384ea9061b67b`
- Date/author: 2026-03-24 / jacky.cheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `5bdc07d97` - [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019)

- Full hash: `5bdc07d974f6cf236fa765a685453ea5e587a838`
- Date/author: 2026-03-23 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`
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

### Commit `a094eb9c2` - Temporarily disable flaky qwen3 cp test in CI (#21178)

- Full hash: `a094eb9c21221245a007aaca183816789cb5dc49`
- Date/author: 2026-03-23 / Shangming Cai
- Auto category: 模型支持/运行时入口
- Main files: `test/registered/4-gpu-models/test_qwen3_30b.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/4-gpu-models/test_qwen3_30b.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `bb737d7a8` - Support Qwen3 MoE context parallel (#18233)

- Full hash: `bb737d7a829bac8fb6386fb6f494e1b2403c598f`
- Date/author: 2026-03-22 / Shunkangz
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/distributed/communication_op.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/utils/cp_utils.py`, `python/sglang/srt/managers/schedule_batch.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/layers/utils/cp_utils.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/utils.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/communication_op.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/flashinfer_comm_fusion.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`
  - tests: `python/sglang/test/attention/test_flashattn_backend.py`; `test/registered/4-gpu-models/test_qwen3_30b.py`; `test/registered/8-gpu-models/test_qwen3_235b.py`; `test/registered/unit/managers/test_prefill_adder.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `852e112eb` - [Qwen3.5] Fix broken pipeline parallelism layer splitting (#21070)

- Full hash: `852e112ebf0054b317e9f02aec97fcf533259cac`
- Date/author: 2026-03-21 / Alison Shao
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
  - tests: `test/registered/distributed/test_pp_single_node.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `3f883ebf2` - Fix test_qwen35_models (#21081)

- Full hash: `3f883ebf2e11fd1c56224bc9111deea1b8860a50`
- Date/author: 2026-03-21 / Qiaolin Yu
- Auto category: 缺陷修复
- Main files: `test/registered/4-gpu-models/test_qwen35_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `f97c09dac` - [AMD] Enable aiter unified attention for non-SWA models (Qwen3-VL) (#20897)

- Full hash: `f97c09dac16192d1578d05ecb340b4dca1923e0a`
- Date/author: 2026-03-21 / YC Yen-Ching Tseng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ec01ef909` - Fix torch.compile/dynamo crash with Qwen3 QK-norm in piecewise CUDA g… (#19818)

- Full hash: `ec01ef9092fbb8467504aa36649ce33bef7a6689`
- Date/author: 2026-03-20 / Jia Guo
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/norm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/norm.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `46a76af97` - [Bugifx] qwen3 rope parameter compatibility (#20931)

- Full hash: `46a76af97becf0e3d61fd0fccd2f15571019645b`
- Date/author: 2026-03-20 / lviy
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d9794ef9f` - [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj (#19321)

- Full hash: `d9794ef9f7602e3a61ee6b337eda3d364aa3ea1d`
- Date/author: 2026-03-20 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `dc6aa26ce` - [CPU] Add mrope kernel for Qwen3-vl (#12531)

- Full hash: `dc6aa26ce9f9f3ea8fafde5a3846579d72b31e0b`
- Date/author: 2026-03-19 / blzheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/rope.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`, `test/srt/cpu/test_rope.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/rotary_embedding/mrope.py`
  - runtime-model: `python/sglang/srt/model_executor/cpu_graph_runner.py`
  - runtime-perf: `sgl-kernel/csrc/cpu/rope.cpp`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
  - tests: `test/srt/cpu/test_rope.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f85455ab2` - [Bugfix] fix qwen3vl hang when --mm-enable-dp-encoder is enable (#20759)

- Full hash: `f85455ab24d33a6fc0a25c80f8974a21bc87bc94`
- Date/author: 2026-03-19 / Ling Zhang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `21c4fc633` - [DP encoder] Fix `pos_emb `layer TP issue when DP encoder enabled for Qwen3 VL (#20788)

- Full hash: `21c4fc6334d13cbc075504353b9abc3716cc069e`
- Date/author: 2026-03-18 / jianan-gu
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `0acc1d3c9` - fix: change qwen 3.5 linear attention a_log to fp32 (#19961)

- Full hash: `0acc1d3c9ad7e912d2ecfe245bc29c6486ada405`
- Date/author: 2026-03-18 / shiyu7
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_5.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `97d5386a2` - Use TRTLLM allreduce fusion for Qwen 3.5 (#19889)

- Full hash: `97d5386a211c83a21d2c977540fd453928f5e417`
- Date/author: 2026-03-18 / Brayden Zhong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/layernorm.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4cc19862e` - [NVIDIA] Integrate FlashInfer decode kernel (Blackwell) for Qwen3.5 (#19150)

- Full hash: `4cc19862efded3a4aff44aafa8dcd87be8cff5c2`
- Date/author: 2026-03-17 / Kaixi Hou
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/accuracy_test_runner.py`, `test/registered/4-gpu-models/test_qwen35_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `test/registered/4-gpu-models/test_qwen35_models.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `cfead25bb` - [Qwen3.5] mamba slice fix (Prefill TP != Decode TP & decode TP size>1) (#20655)

- Full hash: `cfead25bbf695b577fcb8ef6d5cb4ab63e2901f6`
- Date/author: 2026-03-17 / YAMY
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/mooncake/conn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `210d0fbae` - Update ascend docs (#20674)

- Full hash: `210d0fbaef41bb18a83320e1fbe8f50c9d0c9ead`
- Date/author: 2026-03-17 / amote-i
- Auto category: 调度/缓存/PD
- Main files: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`; `docs/platforms/ascend_npu_support_features.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

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

### Commit `7142a594f` - [CI]: Add CI For HiMambaRadixTree and qwen3.5 (#20540)

- Full hash: `7142a594f950053646793b590ac6f9aafe58416c`
- Date/author: 2026-03-15 / hzh0425
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/pr-test.yml`, `test/registered/4-gpu-models/test_qwen35_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test.yml`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
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

### Commit `6c5bf53a3` - [Doc] Clarify that --chat-template is required for Qwen3-Reranker (#20596)

- Full hash: `6c5bf53a36e1fd5e002d11dc72a151190aeac47c`
- Date/author: 2026-03-14 / Matt Van Horn
- Auto category: 模型支持/运行时入口
- Main files: `docs/supported_models/retrieval_ranking/rerank_models.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/supported_models/retrieval_ranking/rerank_models.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `574dbe23b` - Add piecewise cuda graph for Qwen3-Next FP8 flashinfer_trtllm moe backend (#18184)

- Full hash: `574dbe23b25bb823601a55f76dd913fd3fbd9819`
- Date/author: 2026-03-15 / Xiaowei Wang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `22e67876d` - [Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker (#18185)

- Full hash: `22e67876d6aa6992bff89d5d91aef2c2c6b3d1bb`
- Date/author: 2026-03-14 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_omni_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/qwen3_omni_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c95dc88f8` - [CI] migrate ascend-gptq from `test/srt` to `test/registered` (#19628)

- Full hash: `c95dc88f86e971a696ce3066389c0336e68f7691`
- Date/author: 2026-03-14 / SoluMilken
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/llm_models/test_ascend_qwen3_1_7b_gptq_int8.py`, `test/registered/ascend/llm_models/test_ascend_qwen3_30b.py`, `test/srt/ascend/test_ascend_gptq.py`, `test/srt/run_suite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-npu.yml`
  - tests: `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/llm_models/test_ascend_qwen3_1_7b_gptq_int8.py`; `test/registered/ascend/llm_models/test_ascend_qwen3_30b.py`; `test/srt/ascend/test_ascend_gptq.py`; `test/srt/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `9c8777c80` - [AMD][Qwen3.5] aiter a8w8 gemm configuration (#19826)

- Full hash: `9c8777c80f685fba2179a5341492bfdcf6077ad8`
- Date/author: 2026-03-13 / seungrokj
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `067353f67` - [Test] Refactor KL divergence and prefix cache branching to kits (#19715)

- Full hash: `067353f67b56ea6143d9cd77b87b32edde74b6ac`
- Date/author: 2026-03-12 / roikoren755
- Auto category: 缺陷修复
- Main files: `python/sglang/test/kits/kl_divergence_kit.py`, `python/sglang/test/kits/prefix_cache_branching_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/models/test_qwen3_next_models_fp4.py`, `test/registered/models/test_qwen3_next_models_pcg.py`, `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/kits/kl_divergence_kit.py`; `python/sglang/test/kits/prefix_cache_branching_kit.py`; `python/sglang/test/server_fixtures/default_fixture.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/models/test_qwen3_next_models_fp4.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `9b55a98a6` - perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe… (#20386)

- Full hash: `9b55a98a67059b30a2997f244221be1b0b4042c3`
- Date/author: 2026-03-11 / Vedant V Jhaveri
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_5.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `ed42af99a` - [NPU] [Quantization] w4a4 MoE layer support (#18924)

- Full hash: `ed42af99a92fa6f69c5de7f05d023b5a673ddf6b`
- Date/author: 2026-03-11 / Артем Савкин
- Auto category: 性能/后端优化
- Main files: `docs/platforms/ascend_npu_quantization.md`, `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/__init__.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_w4a4_int4_moe.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/llm_models/test_ascend_qwen3_30b_w4a4.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_quantization.md`
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`; `python/sglang/srt/layers/quantization/modelslim/modelslim.py`; `python/sglang/srt/layers/quantization/modelslim/schemes/__init__.py`; `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_w4a4_int4_moe.py`
  - tests: `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/llm_models/test_ascend_qwen3_30b_w4a4.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `031d0a2aa` - [Qwen-MOE] Fix memory duplication issues in case layers weights are re-assigned during weight loading (#18255)

- Full hash: `031d0a2aad444b61c3bbe04e67dda84677b2289d`
- Date/author: 2026-03-10 / fxmarty-amd
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`; `python/sglang/srt/models/qwen3_omni_moe.py`; `python/sglang/srt/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9884957c0` - [NPU] Bugfix  for qwen35 on NPU (#19756)

- Full hash: `9884957c07ce0a98fad34ea0055803594c459cb1`
- Date/author: 2026-03-10 / Hexq0210
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `cabe171b6` - Fix qwen3.5 mtp eplb related issues (#19767)

- Full hash: `cabe171b6ce3b0d4fb25ff9c88d5743430efaca6`
- Date/author: 2026-03-09 / luoyuyan
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_next_mtp.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fc543df28` - [NPU] qwen3_vl encoder support graph

- Full hash: `fc543df2899582729ef23cbcd9f9362393624222`
- Date/author: 2026-03-09 / cen121212
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7da590d4d` - [Qwen3.5] Support Qwen3.5 Pipeline Parallelism (#19670)

- Full hash: `7da590d4d069273644e2eed5fd67c597ba97b220`
- Date/author: 2026-03-07 / Yuan Luo
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
  - tests: `test/registered/distributed/test_pp_single_node.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `ac453b253` - Add Qwen3.5-397B-A17B nightly test (8-GPU) (#19906)

- Full hash: `ac453b253f586b3d85d5eac2a3a38ee77826cbf1`
- Date/author: 2026-03-06 / Alison Shao
- Auto category: 模型支持/运行时入口
- Main files: `test/registered/8-gpu-models/test_qwen35.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/8-gpu-models/test_qwen35.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `f7de9375a` - [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775)

- Full hash: `f7de9375ace71f46882d095bb3fc23f706bad660`
- Date/author: 2026-03-06 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`; `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
  - tests: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9457c049e` - [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391)

- Full hash: `9457c049e19e1cfa75833ef4351ac5aa26941c2c`
- Date/author: 2026-03-04 / hlu1
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen35_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c6850ac30` - [AMD] Fix Qwen3-Coder-Next: Add missing k_scale/v_scale args to extend_attention_fwd in aiter_backend (#19736)

- Full hash: `c6850ac30cbea6e751575beb150818e757c710b2`
- Date/author: 2026-03-03 / Michael
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `365ca1edb` - [NPU] bugs fix: fix a condition bug when using speculative inference on Qwen3 and Qwen3 moe  (#19532)

- Full hash: `365ca1edb5af06de8d76fd85fa882df2b0ad1654`
- Date/author: 2026-03-03 / shengzhaotian
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6b8e62f94` - [AMD] [Qwen 3.5 Day 0] Add Qwen 3.5 nightly accuracy tests (#19479)

- Full hash: `6b8e62f94fec4703048869ca3efbaf40e2928817`
- Date/author: 2026-03-02 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `docs/basic_usage/popular_model_usage.rst`, `docs/basic_usage/qwen3_5.md`, `docs/supported_models/text_generation/generative_models.md`, `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml`, `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - docs-bench: `docs/basic_usage/popular_model_usage.rst`; `docs/basic_usage/qwen3_5.md`; `docs/supported_models/text_generation/generative_models.md`
  - tests: `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml`; `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `3f9fc8b84` - [Qwen3.5] Fix missing `quant_config` in `Qwen3VL` (#19291)

- Full hash: `3f9fc8b848365a5797a44856854e3e6f00a60dd0`
- Date/author: 2026-03-03 / Mohammad Miadh Angkad
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
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

### Commit `468e3dc56` - [Qwen3.5] Set full attn_backend to trtllm_mha on SM100 by default when possible (#19030)

- Full hash: `468e3dc56beef6cf2d15284851f77a6390d7e97f`
- Date/author: 2026-03-02 / hlu1
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `98f47d817` - [AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU (#18608)

- Full hash: `98f47d817583a0a4a3654f12153d975712325e1b`
- Date/author: 2026-03-02 / jacky.cheng
- Auto category: 模型支持/运行时入口
- Main files: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`; `test/registered/amd/test_qwen3_coder_next_8gpu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `a2ea5941d` - [feat] Support nvfp4 quantized model of Qwen3-Next (#17627)

- Full hash: `a2ea5941d562faa5a9a20083ffc81dd0d9dd2d6a`
- Date/author: 2026-02-28 / Zheng Duan
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_fp4.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - tests: `test/registered/models/test_qwen3_next_models_fp4.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `4f0f6cd9d` - Add torch.compile support for qwen3-next on CPU (#12444)

- Full hash: `4f0f6cd9d0259fb5081ecc565dad2bb47643e8fa`
- Date/author: 2026-02-27 / Cao E
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/cpu_graph_runner.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/intel_amx_backend.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d566816d8` - fix qwen3_vl visual module loading (#19333)

- Full hash: `d566816d838ce92d3ae044209f7d67eaa58ce74a`
- Date/author: 2026-02-27 / wingedge777
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `e4b708d3e` - [Spec V2] Support specV2 for mamba hybrid attention (#18808)

- Full hash: `e4b708d3e9dd90613a9707c5c3cd4e98cd8c4cd8`
- Date/author: 2026-02-27 / zhangheng
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/managers/scheduler_output_processor_mixin.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bdc1e46e5` - [Qwen3.5] Qwen3.5-27B inference repeat bug fix (#19411)

- Full hash: `bdc1e46e5ac93dd7ee2d53e5d8c2d3de7dc03f69`
- Date/author: 2026-02-26 / AlfredYong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_5.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b3202fe6d` - [PCG] fix piecewise cuda graph for Qwen3.5 (#19220)

- Full hash: `b3202fe6d072c6afdfd8a567977d84de17c1d50d`
- Date/author: 2026-02-25 / Minglei Zhu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b2c46fc60` - [AMD] Support Qwen3-Coder-Next on AMD platform (#18355)

- Full hash: `b2c46fc60b14904857a37a02ceb633c898b23a63`
- Date/author: 2026-02-26 / jacky.cheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `56891e46b` - [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339)

- Full hash: `56891e46bc1ac4f75e8e541b61810f777cda8209`
- Date/author: 2026-02-25 / Hexq0210
- Auto category: 模型支持/运行时入口
- Main files: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `d38c0e537` - fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1 (#19070)

- Full hash: `d38c0e537d95bfb78486c1185f68c90046ce0cc9`
- Date/author: 2026-02-25 / Zheng Li
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_5.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `307a2b73e` - [AMD] add testcases for Qwen3 235b Instruct 2507 models (#18805)

- Full hash: `307a2b73edd84e66128c92576fb5817535e370d2`
- Date/author: 2026-02-25 / mqhc2020
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/test_qwen3_instruct.py`, `test/registered/amd/test_qwen3_instruct_fp8.py`, `test/registered/amd/test_qwen3_instruct_mxfp4.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/test_qwen3_instruct.py`; `test/registered/amd/test_qwen3_instruct_fp8.py`; `test/registered/amd/test_qwen3_instruct_mxfp4.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `f75abb452` - [Fix][Qwen3.5] Fix KV cache slice transfer for GQA models with replicated KV heads (#19086)

- Full hash: `f75abb4521cfa5a58a9876b3d71c5788302f751d`
- Date/author: 2026-02-25 / YAMY
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `d0bb14003` - [NPU] bugfix for model Qwen3-Coder-Next at weight shape transpose for npu. (#18700)

- Full hash: `d0bb140034894da4390f048d424be53ff76d8f2d`
- Date/author: 2026-02-25 / Hexq0210
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `73fe389dd` - [Qwen3.5] Raise Exception when radix_cache and extra_buffer are enabled at the same time (#19169)

- Full hash: `73fe389dd11472fcd41f401382c0763d4d1db664`
- Date/author: 2026-02-24 / YAMY
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `31c7dc9d9` - [VLM] Introduce FlashInfer CUDNN Prefill as ViT Backend (#19003)

- Full hash: `31c7dc9d990d47919435e5c1799d0d36e8b59eca`
- Date/author: 2026-02-24 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/server_args.py`, `test/manual/nightly/test_vlms_vit_flashinfer_cudnn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
  - tests: `test/manual/nightly/test_vlms_vit_flashinfer_cudnn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5995bfec6` - [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill (#18917)

- Full hash: `5995bfec6368faa48fd8ad159bf9805c15ebc217`
- Date/author: 2026-02-21 / YAMY
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `8541b1118` - [Fix][Qwen3.5] Pass max_mamba_cache_size to mamba pool in disaggregation decode path (#19002)

- Full hash: `8541b1118d6cb396fe9c8f580ea597996635f8fb`
- Date/author: 2026-02-19 / YAMY
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-perf: `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bba2fc49a` - [Qwen3.5] Enable nvfp4 checkpoint (#18937)

- Full hash: `bba2fc49a1700d82ac9f4f79bf6e05b120d424e7`
- Date/author: 2026-02-18 / hlu1
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
