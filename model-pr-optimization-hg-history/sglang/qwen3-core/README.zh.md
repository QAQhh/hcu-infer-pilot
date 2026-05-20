# sglang Qwen3 Core 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/qwen3.py` | `b63cd7645`, `e9d6aefa9`, `d1e95af28`, `365ca1edb`, `c64274c74` |
| `python/sglang/srt/models/qwen3_moe.py` | `466a1d6a4`, `e9d6aefa9`, `dac148167`, `bb737d7a8`, `46a76af97`, `d1e95af28`, `031d0a2aa`, `365ca1edb` |
| `test/registered/lora/test_lora_qwen3.py` | `814202704` |
| `test/srt/cpu/test_qwen3.py` | 无直接提交 |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 80
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
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

## 逐 Commit 审计卡

### Commit `9f67deca2` - 支持qwen3.5-awq模型

- 完整 hash: `9f67deca24b100410fe69d142a4ebca4fe26cc34`
- 时间/作者: 2026-05-07 / maxiao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/quantization/awq.py`, `python/sglang/srt/layers/quantization/moe_wna16.py`, `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/moe_wna16.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c1d308c60` - 修复qwen3.5-397b-fp8报错问题

- 完整 hash: `c1d308c602379d71d746bc50ed785c2bee05ba99`
- 时间/作者: 2026-04-29 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/index.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `32bd2422e` - 修复qwen3.5模型memory_Async问题

- 完整 hash: `32bd2422e7d17f0cee10413aad4a223ffb25dd74`
- 时间/作者: 2026-04-23 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/sampling/sampling_batch_info.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/sampling/sampling_batch_info.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `94a624b83` - 增加qwen3.5模型gammarms_rotary_embedding_fuse_with_kv_store融合算子

- 完整 hash: `94a624b8364de497a4a7ee4a6f9def06e18d90c9`
- 时间/作者: 2026-04-23 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `466a1d6a4` - 将qwen3_moe文件中的SGLANG_USE_FUSED_BAILING_RMS_ROTARY修改为SGLANG_USE_FUSED_RMS_ROTARY

- 完整 hash: `466a1d6a4caa1403fb6608748c3111ddc152cdf2`
- 时间/作者: 2026-04-21 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b8cd509f4` - [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能

- 完整 hash: `b8cd509f45f9a51adee404eb9104358653e869d1`
- 时间/作者: 2026-04-09 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `28dec61dd` - support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k

- 完整 hash: `28dec61dd674f482fe34b5251ff0cd050ca2184c`
- 时间/作者: 2026-04-02 / liucong
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b63cd7645` - 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY

- 完整 hash: `b63cd76459510fb534dde7d8df2ca438099aa881`
- 时间/作者: 2026-03-31 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/qwen3.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/models/bailing_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e9d6aefa9` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- 完整 hash: `e9d6aefa947699a1edc971ecc2e3fdd2053f525f`
- 时间/作者: 2026-03-30 / lizhigong
- 自动分类: 性能/后端优化
- 主要文件: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py` 等 25 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/server_args.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7738d2be5` - Revert "bugfix for weight loading for qwen3-next" (#21496)

- 完整 hash: `7738d2be519eff05e35727fc19b6662c8913eaf3`
- 时间/作者: 2026-03-26 / Baizhou Zhang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `fb90c9d29` - [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047)

- 完整 hash: `fb90c9d298eeeb15fde5de1c7676cfc3d9a4b6ee`
- 时间/作者: 2026-03-26 / Liangsheng Yin
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/test/kits/eval_accuracy_kit.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_mimo_models.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `0906e45ce` - bugfix for weight loading for qwen3-next (#21313)

- 完整 hash: `0906e45cec97abf3aa8ee9cf8962f6a5d36ed4f1`
- 时间/作者: 2026-03-26 / McZyWu
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f5c225eeb` - [CI] Fix TestQwen35WithHiCache (#21371)

- 完整 hash: `f5c225eeba3c6f027e5e7691784249d6a667026f`
- 时间/作者: 2026-03-25 / Baizhou Zhang
- 自动分类: 缺陷修复
- 主要文件: `test/registered/4-gpu-models/test_qwen35_hicache.py`, `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_qwen35_hicache.py`; `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `6b0f1e3b4` - Update skip condition for TestQwen35PPAccuracy (#21370)

- 完整 hash: `6b0f1e3b437dc6aabf933deab07c3a0daa137f7b`
- 时间/作者: 2026-03-25 / Shangming Cai
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/distributed/test_pp_single_node.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/distributed/test_pp_single_node.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `dac148167` - Enable the qwen3 test (#21195)

- 完整 hash: `dac148167c80c695b731cb45e8347f52af9b57be`
- 时间/作者: 2026-03-24 / Shunkangz
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`, `test/registered/4-gpu-models/test_qwen3_30b.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_30b.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0986bed8e` - [HiCache][HybridModel]: Support mamba state offloading & HybridCacheController (#20457)

- 完整 hash: `0986bed8e279ce67659e4e473300fc3c5c717d6a`
- 时间/作者: 2026-03-24 / hzh0425
- 自动分类: 缺陷修复
- 主要文件: `benchmark/hicache/bench_multiturn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hicache_storage.py` 等 13 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/hicache/bench_multiturn.py`
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`; `python/sglang/srt/mem_cache/hicache_storage.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`; `python/sglang/srt/mem_cache/mamba_radix_cache.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b4d3fb001` - [AMD] Add fused GemmaRMSNorm forward_hip to use aiter/vllm kernels for qwen3.5 (#21188)

- 完整 hash: `b4d3fb001d435a9792a1a3896f2384ea9061b67b`
- 时间/作者: 2026-03-24 / jacky.cheng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `5bdc07d97` - [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019)

- 完整 hash: `5bdc07d974f6cf236fa765a685453ea5e587a838`
- 时间/作者: 2026-03-23 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `814202704` - ci: unify PR test suite naming (#21187)

- 完整 hash: `814202704bf21525b5ae07029cb475da4c87f3b7`
- 时间/作者: 2026-03-23 / Lianmin Zheng
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`, `scripts/ci/utils/slash_command_handler.py`, `test/README.md` 等 283 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/actions/wait-for-jobs/action.yml`; `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`; `test/README.md`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/attention/test_chunk_gated_delta_rule.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py` 等 278 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `a094eb9c2` - Temporarily disable flaky qwen3 cp test in CI (#21178)

- 完整 hash: `a094eb9c21221245a007aaca183816789cb5dc49`
- 时间/作者: 2026-03-23 / Shangming Cai
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/4-gpu-models/test_qwen3_30b.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_qwen3_30b.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `bb737d7a8` - Support Qwen3 MoE context parallel (#18233)

- 完整 hash: `bb737d7a829bac8fb6386fb6f494e1b2403c598f`
- 时间/作者: 2026-03-22 / Shunkangz
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/communication_op.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/utils/cp_utils.py`, `python/sglang/srt/managers/schedule_batch.py` 等 19 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/layers/utils/cp_utils.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/utils.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/communication_op.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/flashinfer_comm_fusion.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`
  - tests: `python/sglang/test/attention/test_flashattn_backend.py`; `test/registered/4-gpu-models/test_qwen3_30b.py`; `test/registered/8-gpu-models/test_qwen3_235b.py`; `test/registered/unit/managers/test_prefill_adder.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `852e112eb` - [Qwen3.5] Fix broken pipeline parallelism layer splitting (#21070)

- 完整 hash: `852e112ebf0054b317e9f02aec97fcf533259cac`
- 时间/作者: 2026-03-21 / Alison Shao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
  - tests: `test/registered/distributed/test_pp_single_node.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3f883ebf2` - Fix test_qwen35_models (#21081)

- 完整 hash: `3f883ebf2e11fd1c56224bc9111deea1b8860a50`
- 时间/作者: 2026-03-21 / Qiaolin Yu
- 自动分类: 缺陷修复
- 主要文件: `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f97c09dac` - [AMD] Enable aiter unified attention for non-SWA models (Qwen3-VL) (#20897)

- 完整 hash: `f97c09dac16192d1578d05ecb340b4dca1923e0a`
- 时间/作者: 2026-03-21 / YC Yen-Ching Tseng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ec01ef909` - Fix torch.compile/dynamo crash with Qwen3 QK-norm in piecewise CUDA g… (#19818)

- 完整 hash: `ec01ef9092fbb8467504aa36649ce33bef7a6689`
- 时间/作者: 2026-03-20 / Jia Guo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/norm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/norm.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `46a76af97` - [Bugifx] qwen3 rope parameter compatibility (#20931)

- 完整 hash: `46a76af97becf0e3d61fd0fccd2f15571019645b`
- 时间/作者: 2026-03-20 / lviy
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d9794ef9f` - [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj (#19321)

- 完整 hash: `d9794ef9f7602e3a61ee6b337eda3d364aa3ea1d`
- 时间/作者: 2026-03-20 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `dc6aa26ce` - [CPU] Add mrope kernel for Qwen3-vl (#12531)

- 完整 hash: `dc6aa26ce9f9f3ea8fafde5a3846579d72b31e0b`
- 时间/作者: 2026-03-19 / blzheng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/rope.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`, `test/srt/cpu/test_rope.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding/mrope.py`
  - runtime-model: `python/sglang/srt/model_executor/cpu_graph_runner.py`
  - runtime-perf: `sgl-kernel/csrc/cpu/rope.cpp`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
  - tests: `test/srt/cpu/test_rope.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f85455ab2` - [Bugfix] fix qwen3vl hang when --mm-enable-dp-encoder is enable (#20759)

- 完整 hash: `f85455ab24d33a6fc0a25c80f8974a21bc87bc94`
- 时间/作者: 2026-03-19 / Ling Zhang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d1e95af28` - Upgrade transformers==5.3.0 (#17784)

- 完整 hash: `d1e95af282068a751ee6a8b60a0ae2a90c464819`
- 时间/作者: 2026-03-18 / Xinyuan Tong
- 自动分类: 性能/后端优化
- 主要文件: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py` 等 88 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/layers/rotary_embedding/factory.py`; `python/sglang/srt/managers/tokenizer_manager.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/configs/internvl.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/arcee.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/commandr.py`; `python/sglang/srt/models/dbrx.py` 等 54 个文件
  - runtime-perf: `python/sglang/srt/models/afmoe.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/ernie45_moe_vl.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/granitemoe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 15 个文件
  - tests: `python/sglang/test/runners.py`; `test/registered/core/test_score_api.py`; `test/registered/quant/test_awq.py`; `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/vlm/test_vlm_input_format.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `21c4fc633` - [DP encoder] Fix `pos_emb `layer TP issue when DP encoder enabled for Qwen3 VL (#20788)

- 完整 hash: `21c4fc6334d13cbc075504353b9abc3716cc069e`
- 时间/作者: 2026-03-18 / jianan-gu
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `0acc1d3c9` - fix: change qwen 3.5 linear attention a_log to fp32 (#19961)

- 完整 hash: `0acc1d3c9ad7e912d2ecfe245bc29c6486ada405`
- 时间/作者: 2026-03-18 / shiyu7
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `97d5386a2` - Use TRTLLM allreduce fusion for Qwen 3.5 (#19889)

- 完整 hash: `97d5386a211c83a21d2c977540fd453928f5e417`
- 时间/作者: 2026-03-18 / Brayden Zhong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4cc19862e` - [NVIDIA] Integrate FlashInfer decode kernel (Blackwell) for Qwen3.5 (#19150)

- 完整 hash: `4cc19862efded3a4aff44aafa8dcd87be8cff5c2`
- 时间/作者: 2026-03-17 / Kaixi Hou
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/accuracy_test_runner.py`, `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cfead25bb` - [Qwen3.5] mamba slice fix (Prefill TP != Decode TP & decode TP size>1) (#20655)

- 完整 hash: `cfead25bbf695b577fcb8ef6d5cb4ab63e2901f6`
- 时间/作者: 2026-03-17 / YAMY
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `210d0fbae` - Update ascend docs (#20674)

- 完整 hash: `210d0fbaef41bb18a83320e1fbe8f50c9d0c9ead`
- 时间/作者: 2026-03-17 / amote-i
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`; `docs/platforms/ascend_npu_support_features.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `895e56097` - Add NPU basic function testcases (#19382)

- 完整 hash: `895e56097cc25f762373f462fd027bc39163eb0c`
- 时间/作者: 2026-03-16 / Sugar920
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`, `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py` 等 87 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/disaggregation_utils.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`; `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py`; `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py` 等 86 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `7142a594f` - [CI]: Add CI For HiMambaRadixTree and qwen3.5 (#20540)

- 完整 hash: `7142a594f950053646793b590ac6f9aafe58416c`
- 时间/作者: 2026-03-15 / hzh0425
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test.yml`, `test/registered/4-gpu-models/test_qwen35_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `1c456a0af` - VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282)

- 完整 hash: `1c456a0af540b5fd092a90d3af7627be973416a5`
- 时间/作者: 2026-03-15 / Yuhao Yang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/idefics2.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_vl_moonvit.py` 等 18 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/conv.py`
  - runtime-model: `python/sglang/srt/models/clip.py`; `python/sglang/srt/models/dots_vlm_vit.py`; `python/sglang/srt/models/glm4v.py`; `python/sglang/srt/models/idefics2.py`; `python/sglang/srt/models/internvl.py`; `python/sglang/srt/models/kimi_k25.py`; `python/sglang/srt/models/kimi_vl_moonvit.py`; `python/sglang/srt/models/midashenglm.py` 等 16 个文件
  - tests: `test/unit/test_conv_layer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `6c5bf53a3` - [Doc] Clarify that --chat-template is required for Qwen3-Reranker (#20596)

- 完整 hash: `6c5bf53a36e1fd5e002d11dc72a151190aeac47c`
- 时间/作者: 2026-03-14 / Matt Van Horn
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/supported_models/retrieval_ranking/rerank_models.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/supported_models/retrieval_ranking/rerank_models.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `574dbe23b` - Add piecewise cuda graph for Qwen3-Next FP8 flashinfer_trtllm moe backend (#18184)

- 完整 hash: `574dbe23b25bb823601a55f76dd913fd3fbd9819`
- 时间/作者: 2026-03-15 / Xiaowei Wang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `22e67876d` - [Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker (#18185)

- 完整 hash: `22e67876d6aa6992bff89d5d91aef2c2c6b3d1bb`
- 时间/作者: 2026-03-14 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_omni_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_omni_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c95dc88f8` - [CI] migrate ascend-gptq from `test/srt` to `test/registered` (#19628)

- 完整 hash: `c95dc88f86e971a696ce3066389c0336e68f7691`
- 时间/作者: 2026-03-14 / SoluMilken
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/llm_models/test_ascend_qwen3_1_7b_gptq_int8.py`, `test/registered/ascend/llm_models/test_ascend_qwen3_30b.py`, `test/srt/ascend/test_ascend_gptq.py`, `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-npu.yml`
  - tests: `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/llm_models/test_ascend_qwen3_1_7b_gptq_int8.py`; `test/registered/ascend/llm_models/test_ascend_qwen3_30b.py`; `test/srt/ascend/test_ascend_gptq.py`; `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `9c8777c80` - [AMD][Qwen3.5] aiter a8w8 gemm configuration (#19826)

- 完整 hash: `9c8777c80f685fba2179a5341492bfdcf6077ad8`
- 时间/作者: 2026-03-13 / seungrokj
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `067353f67` - [Test] Refactor KL divergence and prefix cache branching to kits (#19715)

- 完整 hash: `067353f67b56ea6143d9cd77b87b32edde74b6ac`
- 时间/作者: 2026-03-12 / roikoren755
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/test/kits/kl_divergence_kit.py`, `python/sglang/test/kits/prefix_cache_branching_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/models/test_qwen3_next_models_fp4.py`, `test/registered/models/test_qwen3_next_models_pcg.py`, `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/kits/kl_divergence_kit.py`; `python/sglang/test/kits/prefix_cache_branching_kit.py`; `python/sglang/test/server_fixtures/default_fixture.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/models/test_qwen3_next_models_fp4.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `9b55a98a6` - perf(qwen3_5): replace einops rearrange with torch.flatten in GatedDe… (#20386)

- 完整 hash: `9b55a98a67059b30a2997f244221be1b0b4042c3`
- 时间/作者: 2026-03-11 / Vedant V Jhaveri
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ed42af99a` - [NPU] [Quantization] w4a4 MoE layer support (#18924)

- 完整 hash: `ed42af99a92fa6f69c5de7f05d023b5a673ddf6b`
- 时间/作者: 2026-03-11 / Артем Савкин
- 自动分类: 性能/后端优化
- 主要文件: `docs/platforms/ascend_npu_quantization.md`, `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/__init__.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_w4a4_int4_moe.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/llm_models/test_ascend_qwen3_30b_w4a4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_quantization.md`
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`; `python/sglang/srt/layers/quantization/modelslim/modelslim.py`; `python/sglang/srt/layers/quantization/modelslim/schemes/__init__.py`; `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_w4a4_int4_moe.py`
  - tests: `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/llm_models/test_ascend_qwen3_30b_w4a4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `031d0a2aa` - [Qwen-MOE] Fix memory duplication issues in case layers weights are re-assigned during weight loading (#18255)

- 完整 hash: `031d0a2aad444b61c3bbe04e67dda84677b2289d`
- 时间/作者: 2026-03-10 / fxmarty-amd
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`; `python/sglang/srt/models/qwen3_omni_moe.py`; `python/sglang/srt/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9884957c0` - [NPU] Bugfix  for qwen35 on NPU (#19756)

- 完整 hash: `9884957c07ce0a98fad34ea0055803594c459cb1`
- 时间/作者: 2026-03-10 / Hexq0210
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cabe171b6` - Fix qwen3.5 mtp eplb related issues (#19767)

- 完整 hash: `cabe171b6ce3b0d4fb25ff9c88d5743430efaca6`
- 时间/作者: 2026-03-09 / luoyuyan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_next_mtp.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fc543df28` - [NPU] qwen3_vl encoder support graph

- 完整 hash: `fc543df2899582729ef23cbcd9f9362393624222`
- 时间/作者: 2026-03-09 / cen121212
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7da590d4d` - [Qwen3.5] Support Qwen3.5 Pipeline Parallelism (#19670)

- 完整 hash: `7da590d4d069273644e2eed5fd67c597ba97b220`
- 时间/作者: 2026-03-07 / Yuan Luo
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen3_5.py`, `test/registered/distributed/test_pp_single_node.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
  - tests: `test/registered/distributed/test_pp_single_node.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ac453b253` - Add Qwen3.5-397B-A17B nightly test (8-GPU) (#19906)

- 完整 hash: `ac453b253f586b3d85d5eac2a3a38ee77826cbf1`
- 时间/作者: 2026-03-06 / Alison Shao
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/8-gpu-models/test_qwen35.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/8-gpu-models/test_qwen35.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f7de9375a` - [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775)

- 完整 hash: `f7de9375ace71f46882d095bb3fc23f706bad660`
- 时间/作者: 2026-03-06 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`; `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
  - tests: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9457c049e` - [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391)

- 完整 hash: `9457c049e19e1cfa75833ef4351ac5aa26941c2c`
- 时间/作者: 2026-03-04 / hlu1
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen35_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c6850ac30` - [AMD] Fix Qwen3-Coder-Next: Add missing k_scale/v_scale args to extend_attention_fwd in aiter_backend (#19736)

- 完整 hash: `c6850ac30cbea6e751575beb150818e757c710b2`
- 时间/作者: 2026-03-03 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `365ca1edb` - [NPU] bugs fix: fix a condition bug when using speculative inference on Qwen3 and Qwen3 moe  (#19532)

- 完整 hash: `365ca1edb5af06de8d76fd85fa882df2b0ad1654`
- 时间/作者: 2026-03-03 / shengzhaotian
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3.py`
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6b8e62f94` - [AMD] [Qwen 3.5 Day 0] Add Qwen 3.5 nightly accuracy tests (#19479)

- 完整 hash: `6b8e62f94fec4703048869ca3efbaf40e2928817`
- 时间/作者: 2026-03-02 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `docs/basic_usage/popular_model_usage.rst`, `docs/basic_usage/qwen3_5.md`, `docs/supported_models/text_generation/generative_models.md`, `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml`, `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - docs-bench: `docs/basic_usage/popular_model_usage.rst`; `docs/basic_usage/qwen3_5.md`; `docs/supported_models/text_generation/generative_models.md`
  - tests: `test/lm_eval_configs/Qwen3.5-397B-A17B.yaml`; `test/registered/amd/accuracy/mi30x/test_qwen35_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_qwen35_eval_mi35x.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3f9fc8b84` - [Qwen3.5] Fix missing `quant_config` in `Qwen3VL` (#19291)

- 完整 hash: `3f9fc8b848365a5797a44856854e3e6f00a60dd0`
- 时间/作者: 2026-03-03 / Mohammad Miadh Angkad
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c64274c74` - Piecewise Cuda Graph set default (#16331)

- 完整 hash: `c64274c746f210497c45bd1600d2046faf7f4b10`
- 时间/作者: 2026-03-02 / Yuwei An
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/awq.py` 等 34 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/compilation/compile.py`; `python/sglang/srt/compilation/piecewise_context_manager.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/minicpm3.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/flashinfer_backend.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/qwen2_moe.py`
  - tests: `test/manual/nightly/test_vlms_piecewise_cuda_graph.py`; `test/manual/nightly/test_vlms_vit_cuda_graph.py`; `test/manual/piecewise_cudagraph/test_disaggregation_piecewise_cuda_graph.py`; `test/registered/mla/test_mla_deepseek_v3.py`; `test/registered/models/test_generation_models.py`; `test/registered/models/test_kimi_linear_models_pcg.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/piecewise_cuda_graph/test_piecewise_cuda_graph_2_gpu.py` 等 13 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `468e3dc56` - [Qwen3.5] Set full attn_backend to trtllm_mha on SM100 by default when possible (#19030)

- 完整 hash: `468e3dc56beef6cf2d15284851f77a6390d7e97f`
- 时间/作者: 2026-03-02 / hlu1
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `98f47d817` - [AMD] Add Qwen3-Coder-Next accuracy and functionality test scripts for MI35x 8-GPU (#18608)

- 完整 hash: `98f47d817583a0a4a3654f12153d975712325e1b`
- 时间/作者: 2026-03-02 / jacky.cheng
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py`; `test/registered/amd/test_qwen3_coder_next_8gpu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `a2ea5941d` - [feat] Support nvfp4 quantized model of Qwen3-Next (#17627)

- 完整 hash: `a2ea5941d562faa5a9a20083ffc81dd0d9dd2d6a`
- 时间/作者: 2026-02-28 / Zheng Duan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_fp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - tests: `test/registered/models/test_qwen3_next_models_fp4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d2885a909` - [Qwen3-Next] Support gdn fused_rms_norm_gated (#19434)

- 完整 hash: `d2885a9094c3847769923322e51a85841a552662`
- 时间/作者: 2026-02-27 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`; `python/sglang/srt/layers/attention/fla/kda.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4f0f6cd9d` - Add torch.compile support for qwen3-next on CPU (#12444)

- 完整 hash: `4f0f6cd9d0259fb5081ecc565dad2bb47643e8fa`
- 时间/作者: 2026-02-27 / Cao E
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/cpu_graph_runner.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/intel_amx_backend.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d566816d8` - fix qwen3_vl visual module loading (#19333)

- 完整 hash: `d566816d838ce92d3ae044209f7d67eaa58ce74a`
- 时间/作者: 2026-02-27 / wingedge777
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `e4b708d3e` - [Spec V2] Support specV2 for mamba hybrid attention (#18808)

- 完整 hash: `e4b708d3e9dd90613a9707c5c3cd4e98cd8c4cd8`
- 时间/作者: 2026-02-27 / zhangheng
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/managers/scheduler_output_processor_mixin.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bdc1e46e5` - [Qwen3.5] Qwen3.5-27B inference repeat bug fix (#19411)

- 完整 hash: `bdc1e46e5ac93dd7ee2d53e5d8c2d3de7dc03f69`
- 时间/作者: 2026-02-26 / AlfredYong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b3202fe6d` - [PCG] fix piecewise cuda graph for Qwen3.5 (#19220)

- 完整 hash: `b3202fe6d072c6afdfd8a567977d84de17c1d50d`
- 时间/作者: 2026-02-25 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b2c46fc60` - [AMD] Support Qwen3-Coder-Next on AMD platform (#18355)

- 完整 hash: `b2c46fc60b14904857a37a02ceb633c898b23a63`
- 时间/作者: 2026-02-26 / jacky.cheng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `56891e46b` - [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339)

- 完整 hash: `56891e46bc1ac4f75e8e541b61810f777cda8209`
- 时间/作者: 2026-02-25 / Hexq0210
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d38c0e537` - fix(dense): fix Qwen3.5 dense model precision bug in TP_SIZE>1 (#19070)

- 完整 hash: `d38c0e537d95bfb78486c1185f68c90046ce0cc9`
- 时间/作者: 2026-02-25 / Zheng Li
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `307a2b73e` - [AMD] add testcases for Qwen3 235b Instruct 2507 models (#18805)

- 完整 hash: `307a2b73edd84e66128c92576fb5817535e370d2`
- 时间/作者: 2026-02-25 / mqhc2020
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/test_qwen3_instruct.py`, `test/registered/amd/test_qwen3_instruct_fp8.py`, `test/registered/amd/test_qwen3_instruct_mxfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/test_qwen3_instruct.py`; `test/registered/amd/test_qwen3_instruct_fp8.py`; `test/registered/amd/test_qwen3_instruct_mxfp4.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f75abb452` - [Fix][Qwen3.5] Fix KV cache slice transfer for GQA models with replicated KV heads (#19086)

- 完整 hash: `f75abb4521cfa5a58a9876b3d71c5788302f751d`
- 时间/作者: 2026-02-25 / YAMY
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d0bb14003` - [NPU] bugfix for model Qwen3-Coder-Next at weight shape transpose for npu. (#18700)

- 完整 hash: `d0bb140034894da4390f048d424be53ff76d8f2d`
- 时间/作者: 2026-02-25 / Hexq0210
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `73fe389dd` - [Qwen3.5] Raise Exception when radix_cache and extra_buffer are enabled at the same time (#19169)

- 完整 hash: `73fe389dd11472fcd41f401382c0763d4d1db664`
- 时间/作者: 2026-02-24 / YAMY
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `31c7dc9d9` - [VLM] Introduce FlashInfer CUDNN Prefill as ViT Backend (#19003)

- 完整 hash: `31c7dc9d990d47919435e5c1799d0d36e8b59eca`
- 时间/作者: 2026-02-24 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/server_args.py`, `test/manual/nightly/test_vlms_vit_flashinfer_cudnn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
  - tests: `test/manual/nightly/test_vlms_vit_flashinfer_cudnn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5995bfec6` - [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill (#18917)

- 完整 hash: `5995bfec6368faa48fd8ad159bf9805c15ebc217`
- 时间/作者: 2026-02-21 / YAMY
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `8541b1118` - [Fix][Qwen3.5] Pass max_mamba_cache_size to mamba pool in disaggregation decode path (#19002)

- 完整 hash: `8541b1118d6cb396fe9c8f580ea597996635f8fb`
- 时间/作者: 2026-02-19 / YAMY
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-perf: `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bba2fc49a` - [Qwen3.5] Enable nvfp4 checkpoint (#18937)

- 完整 hash: `bba2fc49a1700d82ac9f4f79bf6e05b120d424e7`
- 时间/作者: 2026-02-18 / hlu1
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
