# vllm Qwen3 Core Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `vllm/model_executor/models/qwen3.py` | `ef79626da`, `04d429f6b`, `02b0d6bac`, `e807ec39b`, `df7041633`, `dcd80206b`, `2612ba928` |
| `vllm/model_executor/models/qwen3_moe.py` | `dec8b9446`, `ef79626da`, `02b0d6bac`, `9ae319b34`, `1e2fe58f6`, `df7041633`, `dcd80206b`, `8edaf3857`, `42135d689`, `f06d1125d`, `482914849`, `874d2aaa5` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 80
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-05-20 | `0bef83582` | 性能/后端优化 | fix: use getattr for tie_word_embeddings in qwen3_vl models | `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl_moe.py` |
| 2026-04-18 | `0885aa256` | 性能/后端优化 | [feature][Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity #38479 | `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k3v4nc.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k8v4.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-t3nc.yaml` |
| 2026-03-23 | `be03cbe82` | 缺陷修复 | [BugFix] 合入官方pr，修复Qwen3/Qwen3.5 tool calling 不能正确调用工具的bug (github #36774) | `vllm/tool_parsers/qwen3coder_tool_parser.py` |
| 2026-03-27 | `dec8b9446` | 性能/后端优化 | fix(qwen3 moe): 修正 fused RMS RoPE 的 epsilon 参数传递顺序 | `vllm/model_executor/models/qwen3_moe.py` |
| 2026-03-19 | `dfb597c86` | 性能/后端优化 | Merge branch 'gy-015-qwen3py-fused_mrope' into 'v0.15.1-dev' |  |
| 2026-03-18 | `ef79626da` | 性能/后端优化 | 修改VLLM_USE_FUSED_RMS_ROPE的不同路径 | `vllm/model_executor/models/qwen3.py`, `vllm/model_executor/models/qwen3_moe.py` |
| 2026-03-18 | `04d429f6b` | 性能/后端优化 | qwen3.py合入fused_morpe | `vllm/_custom_ops.py`, `vllm/model_executor/models/qwen3.py` |
| 2026-03-18 | `1e7e69d9f` | 缺陷修复 | fix prompt_is_reasoning_end_arr not define | `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py` |
| 2026-03-16 | `b5ca585e7` | 通用实现调整 | Merge branch 'v0.15.1-dev-qwen3.5' into 'v0.15.1-dev' |  |
| 2026-03-16 | `9c122e36b` | 缺陷修复 | Fix Qwen3/Qwen3.5 Reasoning Parser (#34779) | `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py` |
| 2026-03-06 | `7826240b0` | 模型支持/运行时入口 | Merge branch 'add-qwen3-asr' into 'v0.15.1-dev' |  |
| 2026-03-05 | `c50e6deea` | 模型支持/运行时入口 | add qwen3-asr | `vllm/model_executor/models/qwen3_asr.py`, `vllm/model_executor/models/registry.py`, `vllm/transformers_utils/configs/qwen3_asr.py` |
| 2026-03-02 | `c9733a54f` | 性能/后端优化 | Merge branch 'v0.15.1-dev-qwen3-vl-fused-rope' into 'v0.15.1-dev' |  |
| 2026-03-02 | `02b0d6bac` | 性能/后端优化 | fix(qwen3): 修复VL场景fused RoPE分支条件，并更正qwen3_moe中rms_mrope参数顺序 | `vllm/model_executor/models/qwen3.py`, `vllm/model_executor/models/qwen3_moe.py` |
| 2026-02-28 | `b5e8d01eb` | 缺陷修复 | 修复qwen3.5的使用dtype为fp16的picecwise的推理模式 | `vllm/model_executor/layers/layernorm.py` |
| 2026-02-21 | `9ae319b34` | 性能/后端优化 | feat(moe): 增加 Qwen3 路由 logits 的环境变量可控采集能力 新增 router_capture 工具，用于按 num_tokens/rank 过滤并落盘 MoE router logits 在 Qwen3MoeSparseMoeBlock 中接入采集调用，并在 torch.compile 场景下自动跳过 补充 VLLM_MOE_ROUTER_CAPTURE* 环境变量 | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/router_capture.py`, `vllm/model_executor/models/qwen3_moe.py` |
| 2026-02-24 | `35006c0f1` | 通用实现调整 | Merge branch '0.15.1-dev-qwen3_5' into 'v0.15.1-dev' |  |
| 2026-02-16 | `4dc838d3e` | 性能/后端优化 | add qwen3_5 | `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py` |
| 2026-02-16 | `843c1822d` | 调度/缓存/PD | Add qwen3_5 | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py` |
| 2026-02-11 | `1e2fe58f6` | 性能/后端优化 | feat(moe): 补齐 v0.15 中 Marlin W16A16 MoE 端到端接入 | `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py` |
| 2026-02-10 | `8cdc3a30b` | 缺陷修复 | fix qwen3-next nn layout | `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/qwen3_next.py` |
| 2026-02-10 | `440222e9d` | 性能/后端优化 | fix qwen3-next run error | `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py` |
| 2026-02-06 | `e807ec39b` | 性能/后端优化 | perf(qwen3): 融合 q/k RMSNorm + RoPE set fp8_e4m3 only supported on nmz and support q&kvcache fp8 set VLLM_PCIE_USE_CUSTOM_ALLREDUCE=1 | `CMakeLists.txt`, `csrc/ops.h`, `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh` |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-05 | `86a65417e` | 性能/后端优化 | sync v0.15.1 (ex tests&vllm) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/kernels/E=512,N=128,device_name=gfx936_80cu_nn.json`, `benchmarks/kernels/E=512,N=64,device_name=gfx936_80cu_nn.json` |
| 2026-02-04 | `263f45a4f` | 性能/后端优化 | update VLLM_USE_OPT_RESHAPE_AND_CACHE to support bf16 and qwen3-dense | `vllm/model_executor/model_loader/utils.py`, `vllm/v1/attention/backends/flash_attn.py` |
| 2026-01-29 | `1ed963d43` | 缺陷修复 | [Bugfix] Fix Qwen3-VL-Reranker load. (#33298) | `examples/pooling/score/vision_rerank_api_online.py`, `examples/pooling/score/vision_score_api_online.py`, `tests/entrypoints/pooling/classify/test_online_vision.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-26 | `6ca2c91b9` | 性能/后端优化 | [Model] Use mm_position to compute mrope positions for Qwen3-Omni (#33010) | `examples/offline_inference/qwen3_omni/only_thinker.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2026-01-26 | `11b556878` | 模型支持/运行时入口 | [Refactor] Use data parser for matching data items to multi-modal UUIDs (#32955) | `docs/features/multimodal_inputs.md`, `examples/pooling/plugin/prithvi_geospatial_mae_offline.py`, `tests/entrypoints/openai/test_vision_embeds.py` |
| 2026-01-26 | `254db42ed` | 性能/后端优化 | [Tests] Remove Duplicates (#33032) | `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutlass-dp-ep.yaml`, `tests/evals/gsm8k/configs/moe-refactor/config-b200.txt` |
| 2026-01-25 | `7e67df557` | 缺陷修复 | [Bugfix] fix encoder cache hang in Qwen3VL (#32684) | `tests/models/multimodal/processing/test_tensor_schema.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/qwen3_vl.py` |
| 2026-01-24 | `9ad7f89f5` | 性能/后端优化 | [Models]: Make Multimodal config implicit in ViT implementation (#31972) | `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py` |
| 2026-01-24 | `8edaf3857` | 性能/后端优化 | [Models] Add `SharedFusedMoE` support to Qwen3MoE (#32082) | `vllm/model_executor/models/qwen3_moe.py` |
| 2026-01-24 | `5206e5e28` | 性能/后端优化 | [V1][Hybrid] Mamba Prefix Caching with align mode (#30877) | `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py` |
| 2026-01-22 | `2b8a38b6d` | 性能/后端优化 | [Model] Extend `collect_children` and `no_init_weights` contexts (#32757) | `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py` |
| 2026-01-21 | `42135d689` | 性能/后端优化 | [MoE Refactor] Oracle Select FP8+NVFP4 Kernels In Priority (#32414) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py` |
| 2026-01-20 | `7ab80a8e3` | 性能/后端优化 | Added qwen3 vision language moe support for speculative decoding (#32048) | `vllm/model_executor/models/qwen3_vl_moe.py`, `vllm/v1/spec_decode/eagle.py` |
| 2026-01-21 | `193069d12` | 性能/后端优化 | [5/N] Initialize MM components in context managers (Q-Z) (#32695) | `vllm/model_executor/models/qwen2_audio.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py` |
| 2026-01-21 | `04a9e064d` | 缺陷修复 | [Bugfix] fix the ima issue of qwen-vit (#32687) | `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen3_vl.py` |
| 2026-01-20 | `fda3f03eb` | 性能/后端优化 | [4/N] Initialize MM components in context managers (M-P) (#32663) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/interfaces.py` |
| 2026-01-20 | `4753f3bf6` | 性能/后端优化 | [Model] Use context managers for encoder- and LM-only mode (#32605) | `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/config/multimodal.py` |
| 2026-01-19 | `735033171` | 性能/后端优化 | [BugFix] Fix TRT-LLM NVFP4 DP/EP (#32349) | `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-trtllm.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `vllm/model_executor/layers/fused_moe/layer.py` |
| 2026-01-19 | `c88860d75` | 模型支持/运行时入口 | [Frontend] Score entrypoint support data_1 & data_2 and queries & documents as inputs (#32577) | `docs/serving/openai_compatible_server.md`, `examples/offline_inference/basic/score.py`, `examples/offline_inference/openai_batch/README.md` |
| 2026-01-16 | `b84c426a8` | 性能/后端优化 | [ROCm][CI] Skip Qwen3-30B-A3B-MXFP4A16 Eval Test On Non-CUDA Platforms (#32460) | `tests/evals/gsm8k/test_gsm8k_correctness.py` |
| 2026-01-16 | `f06d1125d` | 性能/后端优化 | Switch default w8a8 gemm impl to blaslt. fix _forward_encoder_attention remove medusa set VLLM_PCIE_USE_CUSTOM_ALLREDUCE=1 | `examples/medusa/README.md`, `examples/medusa/medusa_benchmark_throughput.py`, `examples/medusa/medusa_weight_converter.py` |
| 2026-01-15 | `1b5727520` | 性能/后端优化 | [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336) | `vllm/v1/attention/backends/rocm_attn.py` |
| 2026-01-15 | `31c29257c` | 性能/后端优化 | [MoE Refactor][17/N] Apply Refactor to Bf16 (#31827) | `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml` |
| 2026-01-15 | `361dfdc9d` | 性能/后端优化 | [Quant] Support MXFP4 W4A16 for compressed-tensors MoE models (#32285) | `tests/evals/gsm8k/configs/Qwen3-30B-A3B-MXFP4A16.yaml`, `tests/evals/gsm8k/configs/models-small.txt`, `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py` |
| 2026-01-15 | `e27078ea8` | 性能/后端优化 | [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336) | `vllm/v1/attention/backends/rocm_attn.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-13 | `b8199f604` | 性能/后端优化 | [Model] Re-implement Qwen3Omni Audio Encoder (#32167) | `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2026-01-14 | `9312a6c03` | 模型支持/运行时入口 | [Refactor] [8/N] to simplify the vLLM openai responsesapi_serving architecture (#32260) | `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_protocol.py`, `tests/entrypoints/openai/test_serving_responses.py` |
| 2026-01-13 | `6fa6e7ef0` | 性能/后端优化 | [ROCm][CI] Disable Async Scheduling For Qwen3-Next-80B-A3B-Instruct MTP Async EPLB Accuracy Test (#32275) | `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-13 | `9f430c94b` | 缺陷修复 | [BUGFIX] Add missed remaping of the names of fp8 kv-scale (#32199) | `vllm/model_executor/models/qwen3_next.py` |
| 2026-01-12 | `e68b0dad8` | 调度/缓存/PD | doc: Update model name for Qwen3-Coder in documentation (#32185) | `docs/features/tool_calling.md` |
| 2026-01-12 | `600aaab8d` | 性能/后端优化 | [Model] Remove incorrect `SupportsPP` from MTP models (#32150) | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-11 | `8020a6040` | 缺陷修复 | [Bugfix] Fix Qwen3-VL-Reranker model loading for sequence classification (#32089) | `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/config.py` |
| 2026-01-10 | `583a90e00` | 模型支持/运行时入口 | [Refactor] Separate sequence and token pooling types (#32026) | `tests/model_executor/test_model_load_with_params.py`, `tests/models/language/pooling/test_embedding.py`, `tests/models/language/pooling/test_mm_classifier_conversion.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-09 | `657e9c0e1` | 缺陷修复 | [Fix] Introduce audio channels spec (#31595) | `docs/features/multimodal_inputs.md`, `tests/models/multimodal/processing/test_qwen3_omni.py`, `tests/multimodal/test_audio.py` |
| 2026-01-09 | `1a19e9cd8` | 性能/后端优化 | [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten (#31380) | `tests/kernels/attention/test_prefix_prefill.py`, `vllm/attention/ops/chunked_prefill_paged_decode.py`, `vllm/attention/ops/prefix_prefill.py` |
| 2026-01-08 | `0fa8dd24d` | 性能/后端优化 | [Bugfix] Fix Typo from NVFP4 Refactor (#31977) | `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-CT-fi-cutedsl-deepep-ll.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutedsl-deepep-ll.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutlass.yaml` |
| 2026-01-08 | `96fcd3c26` | 模型支持/运行时入口 | [Misc] Support qwen3-next lora (#31719) | `vllm/model_executor/models/qwen3_next.py` |
| 2026-01-08 | `eac3b96ec` | 模型支持/运行时入口 | [Models] Allow converting Qwen3-VL into Reranker model (#31890) | `docs/models/supported_models.md`, `examples/pooling/pooling/vision_language_pooling.py`, `examples/pooling/score/template/qwen3_vl_reranker.jinja` |
| 2026-01-07 | `5dcd7ef1f` | 性能/后端优化 | [MoE Refactor][15/N] Apply Refactor to Fp8 (#31415) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `22dffca98` | 性能/后端优化 | [PERF] Speed-up of GDN attention decode part (Qwen3-Next) (#31722) | `vllm/model_executor/layers/fla/ops/fused_recurrent.py` |
| 2026-01-06 | `d3e477c01` | 性能/后端优化 | [MoE Refactor] Add Temporary Integration Tests - H100/B200 (#31759) | `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml` |
| 2026-01-06 | `2c1a4f248` | 性能/后端优化 | [Bugfix]: avoid overriding audio/text kwargs (Qwen3-Omni) (#31790) | `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2026-01-06 | `874d2aaa5` | 性能/后端优化 | [feat] 支持 mRoPE 的 fused RMSNorm+RoPE 路径，并修正 torch.compile 动态维度标注 实现了用于优化张量计算的 rms_mrope_fuse 和 rms_mrope_fuse_fake 方法 更新了 forward：在满足条件时走新的 M-RoPE 融合路径 增强了 Qwen3MoeModel 对动态参数维度的支持，以适配该功能 | `vllm/model_executor/models/qwen3_moe.py` |
| 2026-01-06 | `da71d4441` | 性能/后端优化 | [Doc] Show that `use_audio_in_video` is supported in docs (#30837) | `docs/models/supported_models.md`, `examples/offline_inference/qwen2_5_omni/README.md`, `vllm/model_executor/models/qwen2_5_omni_thinker.py` |
| 2026-01-06 | `d8a13c8df` | 性能/后端优化 | [Qwen3-480B] MoE configs for BW1000 TP=8(nn) & 16(nn) & 32(tn) | `vllm/model_executor/layers/fused_moe/configs/E=160,N=160,device_name=gfx936_80cu_nn.json`, `vllm/model_executor/layers/fused_moe/configs/E=160,N=320,device_name=gfx936_80cu_nn.json`, `vllm/model_executor/layers/fused_moe/configs/E=160,N=80,device_name=gfx936_80cu.json` |
| 2026-01-06 | `8f16b5920` | 性能/后端优化 | [Qwen3-30B] MoE configs for BW1000 TP=2 (bs390) | `vllm/model_executor/layers/fused_moe/configs/E=128,N=384,device_name=gfx936_80cu_nn.json` |
| 2026-01-06 | `5708297e4` | 性能/后端优化 | [Misc][Model][Refactor] Pass the prefix into Linear layers (#31669) | `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/gpt_neox.py` |
| 2026-01-05 | `911d38ed9` | 模型支持/运行时入口 | [Model] Let more models to support the score template. (#31335) | `docs/models/supported_models.md`, `examples/pooling/score/convert_model_to_seq_cls.py`, `examples/pooling/score/offline_reranker.py` |
| 2026-01-02 | `97a01308e` | 性能/后端优化 | Improve HF qwen3_omni: preserve audio_sample_rate in kwargs restructuring (#29255) | `tests/models/multimodal/processing/test_qwen3_omni.py`, `tests/multimodal/test_processing.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2025-12-29 | `0b6b70105` | 性能/后端优化 | [Model] Add tuned triton fused_moe configs for Qwen3Moe on B200 (#31448) | `vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=NVIDIA_B200.json` |
| 2025-12-26 | `ce1eafd1a` | 模型支持/运行时入口 | [Core] Initialize LoRA support for tower and connector in multi-modal models (#26674) | `docs/features/lora.md`, `tests/lora/conftest.py`, `tests/lora/test_lora_manager.py` |

## Per-Commit Audit Cards

### Commit `0bef83582` - fix: use getattr for tie_word_embeddings in qwen3_vl models

- Full hash: `0bef83582f6432e306df15afb7cd741ee6cd469b`
- Date/author: 2026-05-20 / guanyu1
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0885aa256` - [feature][Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity #38479

- Full hash: `0885aa25646d55d270b6a518d36861de2bec90d1`
- Date/author: 2026-04-18 / wanglong3
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k3v4nc.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k8v4.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-t3nc.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-t4nc.yaml`, `tests/evals/gsm8k/configs/models-turboquant.txt`, `tests/quantization/test_turboquant.py`, `tests/quantization/untest_fp8.py`, `tools/num_stages_sweep.sh` 等 27 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `tools/num_stages_sweep.sh`; `tools/run_single_bench.sh`; `vllm/engine/arg_utils.py`; `vllm/platforms/xpu.py`; `vllm/utils/torch_utils.py`
  - runtime-perf: `vllm/attention/layer.py`; `vllm/config/attention.py`; `vllm/config/cache.py`; `vllm/model_executor/layers/quantization/turboquant/__init__.py`; `vllm/model_executor/layers/quantization/turboquant/centroids.py`; `vllm/model_executor/layers/quantization/turboquant/config.py`; `vllm/model_executor/layers/quantization/turboquant/quantizer.py`; `vllm/platforms/cuda.py` 等 15 个文件
  - tests: `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k3v4nc.yaml`; `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k8v4.yaml`; `tests/evals/gsm8k/configs/Qwen3-4B-TQ-t3nc.yaml`; `tests/evals/gsm8k/configs/Qwen3-4B-TQ-t4nc.yaml`; `tests/evals/gsm8k/configs/models-turboquant.txt`; `tests/quantization/test_turboquant.py`; `tests/quantization/untest_fp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `be03cbe82` - [BugFix] 合入官方pr，修复Qwen3/Qwen3.5 tool calling 不能正确调用工具的bug (github #36774)

- Full hash: `be03cbe824b2af6999dbbc3c92f6cbe270cb0116`
- Date/author: 2026-03-23 / jujil
- Auto category: 缺陷修复
- Main files: `vllm/tool_parsers/qwen3coder_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tool_parsers/qwen3coder_tool_parser.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `dec8b9446` - fix(qwen3 moe): 修正 fused RMS RoPE 的 epsilon 参数传递顺序

- Full hash: `dec8b94466abeaad4c9c5be4929221c4e59b4049`
- Date/author: 2026-03-27 / laibao
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `dfb597c86` - Merge branch 'gy-015-qwen3py-fused_mrope' into 'v0.15.1-dev'

- Full hash: `dfb597c869a4554bbc763d38f29d149106c672f0`
- Date/author: 2026-03-19 / wangmin6
- Auto category: 性能/后端优化
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `ef79626da` - 修改VLLM_USE_FUSED_RMS_ROPE的不同路径

- Full hash: `ef79626daf3016224cb2d9ab9e80440ff7606854`
- Date/author: 2026-03-18 / guanyu1
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3.py`, `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `04d429f6b` - qwen3.py合入fused_morpe

- Full hash: `04d429f6b52f0e4c421dfb4a232135f9c2261761`
- Date/author: 2026-03-18 / guanyu1
- Auto category: 性能/后端优化
- Main files: `vllm/_custom_ops.py`, `vllm/model_executor/models/qwen3.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/models/qwen3.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1e7e69d9f` - fix prompt_is_reasoning_end_arr not define

- Full hash: `1e7e69d9f54c83f0931bf3af0b69cb5fe5621c80`
- Date/author: 2026-03-18 / renzhc
- Auto category: 缺陷修复
- Main files: `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/qwen3_reasoning_parser.py`
  - runtime-model: `vllm/entrypoints/openai/chat_completion/serving.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b5ca585e7` - Merge branch 'v0.15.1-dev-qwen3.5' into 'v0.15.1-dev'

- Full hash: `b5ca585e76a7fd8ac9211db1c6f7618f42b914ec`
- Date/author: 2026-03-16 / zhangqha
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `9c122e36b` - Fix Qwen3/Qwen3.5 Reasoning Parser  (#34779)

- Full hash: `9c122e36b5d6e6a2a333cc9bdecf9ca0cc147abe`
- Date/author: 2026-03-16 / jujil
- Auto category: 缺陷修复
- Main files: `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/reasoning/qwen3_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/qwen3_reasoning_parser.py`
  - runtime-model: `vllm/entrypoints/openai/chat_completion/serving.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `7826240b0` - Merge branch 'add-qwen3-asr' into 'v0.15.1-dev'

- Full hash: `7826240b0e8e4d6aadb5a413e736f4a7f369c8ce`
- Date/author: 2026-03-06 / zhangqha
- Auto category: 模型支持/运行时入口
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `c50e6deea` - add qwen3-asr

- Full hash: `c50e6deeaf9ae0f43c6aa5986f389a98f3730456`
- Date/author: 2026-03-05 / “weishb”
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/qwen3_asr.py`, `vllm/model_executor/models/registry.py`, `vllm/transformers_utils/configs/qwen3_asr.py`, `vllm/transformers_utils/processors/__init__.py`, `vllm/transformers_utils/processors/qwen3_asr.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/transformers_utils/processors/__init__.py`; `vllm/transformers_utils/processors/qwen3_asr.py`
  - runtime-model: `vllm/model_executor/models/qwen3_asr.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/configs/qwen3_asr.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c9733a54f` - Merge branch 'v0.15.1-dev-qwen3-vl-fused-rope' into 'v0.15.1-dev'

- Full hash: `c9733a54f53df5eaaec725b7366c8dab168aae1d`
- Date/author: 2026-03-02 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `02b0d6bac` - fix(qwen3): 修复VL场景fused RoPE分支条件，并更正qwen3_moe中rms_mrope参数顺序

- Full hash: `02b0d6bacabc817391a2cc2aba76878190bb287b`
- Date/author: 2026-03-02 / laibao
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3.py`, `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b5e8d01eb` - 修复qwen3.5的使用dtype为fp16的picecwise的推理模式

- Full hash: `b5e8d01ebde8ea1a2d82d014d62a96a9e5fd1e2a`
- Date/author: 2026-02-28 / yangql1
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/layernorm.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `9ae319b34` - feat(moe): 增加 Qwen3 路由 logits 的环境变量可控采集能力 新增 router_capture 工具，用于按 num_tokens/rank 过滤并落盘 MoE router logits 在 Qwen3MoeSparseMoeBlock 中接入采集调用，并在 torch.compile 场景下自动跳过 补充 VLLM_MOE_ROUTER_CAPTURE* 环境变量

- Full hash: `9ae319b340022ba4bd44c4403ed758e2282b8eed`
- Date/author: 2026-02-21 / laibao
- Auto category: 性能/后端优化
- Main files: `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/router_capture.py`, `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/envs.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/router_capture.py`; `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `35006c0f1` - Merge branch '0.15.1-dev-qwen3_5' into 'v0.15.1-dev'

- Full hash: `35006c0f17ed9d6210875c9b51d106920f1a16c8`
- Date/author: 2026-02-24 / zhuwenwen
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `4dc838d3e` - add qwen3_5

- Full hash: `4dc838d3e0bfb95155155f658a227d1958ca371c`
- Date/author: 2026-02-16 / Rayyyyy
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/qwen3_5.py`, `vllm/transformers_utils/configs/qwen3_5_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_utils.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/qwen3_5.py`; `vllm/model_executor/models/qwen3_5_mtp.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/qwen3_5.py`
  - runtime-perf: `vllm/transformers_utils/configs/qwen3_5_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `843c1822d` - Add qwen3_5

- Full hash: `843c1822de92edd962da42bbc490512a60aadbd5`
- Date/author: 2026-02-16 / Rayyyyy
- Auto category: 调度/缓存/PD
- Main files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/speculative.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/models/qwen3_5.py`; `vllm/model_executor/models/qwen3_5_mtp.py`; `vllm/model_executor/models/qwen3_next.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/model_arch_config_convertor.py`
  - tests: `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1e2fe58f6` -  feat(moe): 补齐 v0.15 中 Marlin W16A16 MoE 端到端接入

- Full hash: `1e2fe58f638d4678835242fffc307f6839e0be47`
- Date/author: 2026-02-11 / laibao
- Auto category: 性能/后端优化
- Main files: `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/envs.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8cdc3a30b` - fix qwen3-next nn layout

- Full hash: `8cdc3a30b21b06a793c896ced997436b8f1cb255`
- Date/author: 2026-02-10 / zhuwenwen
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `440222e9d` - fix qwen3-next run error

- Full hash: `440222e9d56246e140274c7a9eb9a9df13756ddf`
- Date/author: 2026-02-10 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e807ec39b` - perf(qwen3): 融合 q/k RMSNorm + RoPE set fp8_e4m3 only supported on nmz and support q&kvcache fp8 set VLLM_PCIE_USE_CUSTOM_ALLREDUCE=1

- Full hash: `e807ec39bf4295c5357833b97c382cd66a24ee1b`
- Date/author: 2026-02-06 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `CMakeLists.txt`, `csrc/ops.h`, `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh`, `csrc/quantization/w8a8/fp8/common.cuh`, `csrc/torch_bindings.cpp`, `vllm/envs.py`, `vllm/model_executor/models/qwen3.py`, `vllm/v1/attention/backends/flash_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `CMakeLists.txt`; `csrc/ops.h`; `csrc/torch_bindings.cpp`; `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/qwen3.py`
  - runtime-perf: `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh`; `csrc/quantization/w8a8/fp8/common.cuh`; `vllm/v1/attention/backends/flash_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `df7041633` - sync v0.15.1 (models)

- Full hash: `df7041633878cacfcd677cef5efc907705de6c98`
- Date/author: 2026-02-06 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/bagel.py` 等 169 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 147 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `86a65417e` - sync v0.15.1 (ex tests&vllm)

- Full hash: `86a65417e3df9d4a327de745631cb8a336a3cd79`
- Date/author: 2026-02-05 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `benchmarks/benchmark_prefix_caching.py`, `benchmarks/kernels/E=512,N=128,device_name=gfx936_80cu_nn.json`, `benchmarks/kernels/E=512,N=64,device_name=gfx936_80cu_nn.json`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`, `benchmarks/kernels/benchmark_moe_permute_unpermute.py`, `benchmarks/kernels/benchmark_paged_attention.py`, `csrc/cache.h`, `csrc/cache_kernels.cu` 等 24 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/benchmark_prefix_caching.py`; `benchmarks/kernels/E=512,N=128,device_name=gfx936_80cu_nn.json`; `benchmarks/kernels/E=512,N=64,device_name=gfx936_80cu_nn.json`; `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`; `benchmarks/kernels/benchmark_moe_permute_unpermute.py`; `benchmarks/kernels/benchmark_paged_attention.py`; `docs/configuration/optimization.md`; `docs/contributing/model/basic.md` 等 15 个文件
  - other: `csrc/cpu/torch_bindings.cpp`; `csrc/torch_bindings.cpp`; `pyproject.toml`; `setup.py`; `vllm/_custom_ops.py`
  - runtime-perf: `csrc/cache.h`; `csrc/cache_kernels.cu`; `csrc/cpu/cache.cpp`; `csrc/cpu/dnnl_kernels.cpp`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `263f45a4f` - update VLLM_USE_OPT_RESHAPE_AND_CACHE to support bf16 and qwen3-dense

- Full hash: `263f45a4f9d9d2383ba12482836968b66c2c4569`
- Date/author: 2026-02-04 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/model_loader/utils.py`, `vllm/v1/attention/backends/flash_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/model_loader/utils.py`
  - runtime-perf: `vllm/v1/attention/backends/flash_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1ed963d43` - [Bugfix] Fix Qwen3-VL-Reranker load. (#33298)

- Full hash: `1ed963d43a3511cb9d6360ec9b97a0a0cced7281`
- Date/author: 2026-01-29 / wang.yuqi
- Auto category: 缺陷修复
- Main files: `examples/pooling/score/vision_rerank_api_online.py`, `examples/pooling/score/vision_score_api_online.py`, `tests/entrypoints/pooling/classify/test_online_vision.py`, `tests/entrypoints/pooling/score/test_online_score_vision.py`, `tests/entrypoints/test_utils.py`, `vllm/model_executor/models/adapters.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/pooling/score/vision_rerank_api_online.py`; `examples/pooling/score/vision_score_api_online.py`
  - runtime-model: `vllm/model_executor/models/adapters.py`
  - tests: `tests/entrypoints/pooling/classify/test_online_vision.py`; `tests/entrypoints/pooling/score/test_online_score_vision.py`; `tests/entrypoints/test_utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `dcd80206b` - [Chore] Update type annotation of `input_ids` in model forward (#33063)

- Full hash: `dcd80206b7a9143c81f7f2808e84914f8e38ce95`
- Date/author: 2026-01-26 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py` 等 164 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/basic.md`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 140 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
  - tests: `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6ca2c91b9` - [Model] Use mm_position to compute mrope positions for Qwen3-Omni (#33010)

- Full hash: `6ca2c91b9663466b61ab14d804ef3f6fe7c80827`
- Date/author: 2026-01-26 / Itay Etelis
- Auto category: 性能/后端优化
- Main files: `examples/offline_inference/qwen3_omni/only_thinker.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/offline_inference/qwen3_omni/only_thinker.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `11b556878` - [Refactor] Use data parser for matching data items to multi-modal UUIDs (#32955)

- Full hash: `11b556878b958043e9c026919d4cba0236c85143`
- Date/author: 2026-01-26 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `docs/features/multimodal_inputs.md`, `examples/pooling/plugin/prithvi_geospatial_mae_offline.py`, `tests/entrypoints/openai/test_vision_embeds.py`, `tests/entrypoints/test_chat_utils.py`, `tests/models/multimodal/pooling/test_prithvi_mae.py`, `tests/plugins/prithvi_io_processor_plugin/prithvi_io_processor/prithvi_processor.py`, `tests/v1/engine/test_process_multi_modal_uuids.py`, `vllm/entrypoints/chat_utils.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/multimodal_inputs.md`; `examples/pooling/plugin/prithvi_geospatial_mae_offline.py`
  - other: `vllm/utils/__init__.py`; `vllm/v1/engine/input_processor.py`
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/pooling/score/utils.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/model_executor/models/terratorch.py`
  - tests: `tests/entrypoints/openai/test_vision_embeds.py`; `tests/entrypoints/test_chat_utils.py`; `tests/models/multimodal/pooling/test_prithvi_mae.py`; `tests/plugins/prithvi_io_processor_plugin/prithvi_io_processor/prithvi_processor.py`; `tests/v1/engine/test_process_multi_modal_uuids.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `254db42ed` - [Tests] Remove Duplicates (#33032)

- Full hash: `254db42ede6beb7d3191f50084594c0ce791ce40`
- Date/author: 2026-01-26 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutlass-dp-ep.yaml`, `tests/evals/gsm8k/configs/moe-refactor/config-b200.txt`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutlass-dp-ep.yaml`; `tests/evals/gsm8k/configs/moe-refactor/config-b200.txt`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `7e67df557` - [Bugfix] fix encoder cache hang in Qwen3VL (#32684)

- Full hash: `7e67df5570e2afc6a92833096898689c91244fb6`
- Date/author: 2026-01-25 / JJJYmmm
- Auto category: 缺陷修复
- Main files: `tests/models/multimodal/processing/test_tensor_schema.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py`
  - tests: `tests/models/multimodal/processing/test_tensor_schema.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `9ad7f89f5` - [Models]: Make Multimodal config implicit in ViT implementation (#31972)

- Full hash: `9ad7f89f55b7046d0498608eb85b94b2dc5c2666`
- Date/author: 2026-01-24 / Isotr0py
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/eagle2_5_vl.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py` 等 38 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/eagle2_5_vl.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/hunyuan_vision.py` 等 35 个文件
  - runtime-perf: `vllm/model_executor/layers/attention/mm_encoder_attention.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/model_executor/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8edaf3857` - [Models] Add `SharedFusedMoE` support to Qwen3MoE (#32082)

- Full hash: `8edaf3857027c75382672ade255f7cb531f96844`
- Date/author: 2026-01-24 / Isotr0py
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5206e5e28` - [V1][Hybrid] Mamba Prefix Caching with align mode (#30877)

- Full hash: `5206e5e28c25dcc43d3a2373b591a0cdf9792f5d`
- Date/author: 2026-01-24 / Harry Huang
- Auto category: 性能/后端优化
- Main files: `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py`, `vllm/config/vllm.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py` 等 42 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/engine/arg_utils.py`; `vllm/v1/core/block_pool.py`
  - runtime-model: `vllm/config/vllm.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/mamba_mixer.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/mamba_utils.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/falcon_h1.py` 等 26 个文件
  - runtime-perf: `vllm/config/cache.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/v1/attention/backends/gdn_attn.py`; `vllm/v1/attention/backends/linear_attn.py`; `vllm/v1/attention/backends/mamba_attn.py`; `vllm/v1/attention/backends/utils.py`; `vllm/v1/core/kv_cache_coordinator.py` 等 12 个文件
  - tests: `tests/v1/core/test_single_type_kv_cache_manager.py`; `tests/v1/e2e/test_mamba_prefix_cache.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2b8a38b6d` - [Model] Extend `collect_children` and `no_init_weights` contexts (#32757)

- Full hash: `2b8a38b6d6be4f6e09cc20381c7027e7c35cb6c9`
- Date/author: 2026-01-22 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/bagel.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/glm4v.py`, `vllm/model_executor/models/idefics3.py` 等 20 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/utils/collection_utils.py`
  - runtime-model: `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/gemma3_mm.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/idefics3.py`; `vllm/model_executor/models/interfaces.py` 等 17 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
  - tests: `tests/utils_/test_collection_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `42135d689` - [MoE Refactor] Oracle Select FP8+NVFP4 Kernels In Priority (#32414)

- Full hash: `42135d689830c0e764d925b6454bc68ba6c6cab4`
- Date/author: 2026-01-21 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`, `benchmarks/kernels/benchmark_moe.py`, `docs/design/moe_kernel_features.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_silu_mul_quant_fusion.py` 等 82 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`; `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`; `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`; `benchmarks/kernels/benchmark_moe.py`; `docs/design/moe_kernel_features.md`
  - other: `vllm/compilation/fusion.py`; `vllm/compilation/fusion_attn.py`; `vllm/compilation/matcher_utils.py`
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`; `vllm/model_executor/warmup/deep_gemm_warmup.py`
  - runtime-perf: `tools/vllm-rocm/pin_rocm_dependencies.py`; `vllm/compilation/activation_quant_fusion.py`; `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/fallback.py`; `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py` 等 38 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_silu_mul_quant_fusion.py`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-trtllm.yaml` 等 33 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7ab80a8e3` - Added qwen3 vision language moe support for speculative decoding (#32048)

- Full hash: `7ab80a8e37ac62f73e09fdc9ba7f69dd09cda2a8`
- Date/author: 2026-01-20 / shanjiaz
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_vl_moe.py`, `vllm/v1/spec_decode/eagle.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `193069d12` - [5/N] Initialize MM components in context managers (Q-Z) (#32695)

- Full hash: `193069d129414f8f70218f8fb88fb92c75f17ce5`
- Date/author: 2026-01-21 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen2_audio.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/radio.py`, `vllm/model_executor/models/siglip.py`, `vllm/model_executor/models/skyworkr1v.py`, `vllm/model_executor/models/tarsier.py`, `vllm/model_executor/models/ultravox.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen2_audio.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/model_executor/models/radio.py`; `vllm/model_executor/models/siglip.py`; `vllm/model_executor/models/skyworkr1v.py`; `vllm/model_executor/models/tarsier.py`; `vllm/model_executor/models/ultravox.py`; `vllm/model_executor/models/voxtral.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `04a9e064d` - [Bugfix] fix the ima issue of qwen-vit (#32687)

- Full hash: `04a9e064db4dcf57519f1333796ba7face46248b`
- Date/author: 2026-01-21 / JJJYmmm
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `fda3f03eb` - [4/N] Initialize MM components in context managers (M-P) (#32663)

- Full hash: `fda3f03eb28c3b0daf73394219b8ad73adfc53e8`
- Date/author: 2026-01-20 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/interns1.py`, `vllm/model_executor/models/internvl.py`, `vllm/model_executor/models/midashenglm.py`, `vllm/model_executor/models/minicpmo.py`, `vllm/model_executor/models/minicpmv.py` 等 24 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/interns1.py`; `vllm/model_executor/models/internvl.py`; `vllm/model_executor/models/midashenglm.py`; `vllm/model_executor/models/minicpmo.py`; `vllm/model_executor/models/minicpmv.py` 等 23 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4753f3bf6` - [Model] Use context managers for encoder- and LM-only mode (#32605)

- Full hash: `4753f3bf69a2b975361afa7c49e8d948047613f6`
- Date/author: 2026-01-20 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/config/multimodal.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/llava.py` 等 21 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/online_serving/disaggregated_encoder/README.md`
  - other: `vllm/engine/arg_utils.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llava.py`; `vllm/model_executor/models/mistral3.py`; `vllm/model_executor/models/mllama4.py` 等 18 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `735033171` - [BugFix] Fix TRT-LLM NVFP4 DP/EP (#32349)

- Full hash: `73503317188e4b6430ab2857d98546b5b432cb43`
- Date/author: 2026-01-19 / jiahanc
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-trtllm.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/modelopt.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/quantization/modelopt.py`
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-trtllm.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c88860d75` - [Frontend] Score entrypoint support data_1 & data_2 and queries & documents as inputs (#32577)

- Full hash: `c88860d759715affaf2285afb953cc791c0a5a38`
- Date/author: 2026-01-19 / wang.yuqi
- Auto category: 模型支持/运行时入口
- Main files: `docs/serving/openai_compatible_server.md`, `examples/offline_inference/basic/score.py`, `examples/offline_inference/openai_batch/README.md`, `examples/pooling/score/cohere_rerank_client.py`, `examples/pooling/score/qwen3_reranker_online.py`, `examples/pooling/score/score_api_online.py`, `examples/pooling/score/vision_rerank_api_online.py`, `examples/pooling/score/vision_score_api_online.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/serving/openai_compatible_server.md`; `examples/offline_inference/basic/score.py`; `examples/offline_inference/openai_batch/README.md`; `examples/pooling/score/cohere_rerank_client.py`; `examples/pooling/score/qwen3_reranker_online.py`; `examples/pooling/score/score_api_online.py`; `examples/pooling/score/vision_rerank_api_online.py`; `examples/pooling/score/vision_score_api_online.py`
  - runtime-model: `vllm/entrypoints/openai/engine/serving.py`; `vllm/entrypoints/openai/run_batch.py`; `vllm/entrypoints/pooling/score/protocol.py`; `vllm/entrypoints/pooling/score/serving.py`
  - tests: `tests/entrypoints/openai/test_run_batch.py`; `tests/entrypoints/pooling/classify/test_online.py`; `tests/entrypoints/pooling/score/test_offline.py`; `tests/entrypoints/pooling/score/test_online_score.py`; `tests/models/language/pooling_mteb_test/mteb_score_utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b84c426a8` - [ROCm][CI] Skip Qwen3-30B-A3B-MXFP4A16 Eval Test On Non-CUDA Platforms (#32460)

- Full hash: `b84c426a8c48c25db6a4a1a14860e845347db1c1`
- Date/author: 2026-01-16 / Micah Williamson
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/test_gsm8k_correctness.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/evals/gsm8k/test_gsm8k_correctness.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `f06d1125d` - Switch default w8a8 gemm impl to blaslt. fix _forward_encoder_attention remove medusa set VLLM_PCIE_USE_CUSTOM_ALLREDUCE=1

- Full hash: `f06d1125d9c8fde5075f4841ae4e0978a08095c9`
- Date/author: 2026-01-16 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `examples/medusa/README.md`, `examples/medusa/medusa_benchmark_throughput.py`, `examples/medusa/medusa_weight_converter.py`, `vllm/envs.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `vllm/model_executor/models/falcon.py`, `vllm/model_executor/models/glm4.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/medusa/README.md`; `examples/medusa/medusa_benchmark_throughput.py`; `examples/medusa/medusa_weight_converter.py`
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/falcon.py`; `vllm/model_executor/models/glm4.py`; `vllm/model_executor/models/telechat2.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`; `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `vllm/model_executor/models/qwen3_moe.py`; `vllm/platforms/rocm.py`; `vllm/v1/attention/backends/flash_attn.py`; `vllm/v1/attention/backends/mla/test_concat.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1b5727520` - [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336)

- Full hash: `1b5727520749e533b532a8cfa76ad855447f9980`
- Date/author: 2026-01-15 / vllmellm
- Auto category: 性能/后端优化
- Main files: `vllm/v1/attention/backends/rocm_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/v1/attention/backends/rocm_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `31c29257c` - [MoE Refactor][17/N] Apply Refactor to Bf16 (#31827)

- Full hash: `31c29257c852c429a655dd35a1c373ccd46f97da`
- Date/author: 2026-01-15 / Yongye Zhu
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-triton.yaml` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-triton.yaml` 等 10 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `361dfdc9d` - [Quant] Support MXFP4 W4A16 for compressed-tensors MoE models  (#32285)

- Full hash: `361dfdc9d81ef16f00cf9f51dc104b55e382ee61`
- Date/author: 2026-01-15 / Dipika Sikka
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/configs/Qwen3-30B-A3B-MXFP4A16.yaml`, `tests/evals/gsm8k/configs/models-small.txt`, `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
  - tests: `tests/evals/gsm8k/configs/Qwen3-30B-A3B-MXFP4A16.yaml`; `tests/evals/gsm8k/configs/models-small.txt`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e27078ea8` - [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336)

- Full hash: `e27078ea807cf5655c6be3b59608e55c1682756d`
- Date/author: 2026-01-15 / vllmellm
- Auto category: 性能/后端优化
- Main files: `vllm/v1/attention/backends/rocm_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/v1/attention/backends/rocm_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9ea07b41d` - [1/N] Reorganize multimodal processing code (#32327)

- Full hash: `9ea07b41da169f727a2eb7302adec4c724319522`
- Date/author: 2026-01-14 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md`, `tests/multimodal/test_processing.py`, `vllm/benchmarks/mm_processor.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py` 等 76 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/api/README.md`; `docs/contributing/model/multimodal.md`; `docs/design/mm_processing.md`
  - other: `vllm/benchmarks/mm_processor.py`; `vllm/multimodal/inputs.py`; `vllm/multimodal/processing/__init__.py`; `vllm/multimodal/processing/context.py`; `vllm/multimodal/processing/dummy_inputs.py`; `vllm/multimodal/processing/processor.py`; `vllm/multimodal/registry.py`; `vllm/v1/engine/input_processor.py`
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/blip2.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/cohere2_vision.py` 等 62 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/multimodal/cache.py`
  - tests: `tests/multimodal/test_processing.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b8199f604` - [Model] Re-implement Qwen3Omni Audio Encoder (#32167)

- Full hash: `b8199f604931012c433e018980aac22d44ad30b5`
- Date/author: 2026-01-13 / Roger Wang
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9312a6c03` - [Refactor] [8/N] to simplify the vLLM openai responsesapi_serving architecture (#32260)

- Full hash: `9312a6c03a87e100fdfc2679900221f9c6489a63`
- Date/author: 2026-01-14 / Chauncey
- Auto category: 模型支持/运行时入口
- Main files: `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_protocol.py`, `tests/entrypoints/openai/test_serving_responses.py`, `vllm/entrypoints/context.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/openai/engine/protocol.py`, `vllm/entrypoints/openai/engine/serving.py`, `vllm/entrypoints/openai/parser/harmony_utils.py` 等 21 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/basic_parsers.py`; `vllm/reasoning/minimax_m2_reasoning_parser.py`; `vllm/reasoning/mistral_reasoning_parser.py`; `vllm/reasoning/olmo3_reasoning_parser.py`; `vllm/reasoning/qwen3_reasoning_parser.py`; `vllm/tool_parsers/abstract_tool_parser.py`
  - runtime-model: `vllm/entrypoints/context.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/engine/protocol.py`; `vllm/entrypoints/openai/engine/serving.py`; `vllm/entrypoints/openai/parser/harmony_utils.py`; `vllm/entrypoints/openai/parser/responses_parser.py`; `vllm/entrypoints/openai/responses/__init__.py`; `vllm/entrypoints/openai/responses/api_router.py` 等 11 个文件
  - tests: `tests/entrypoints/openai/responses/test_function_call_parsing.py`; `tests/entrypoints/openai/test_protocol.py`; `tests/entrypoints/openai/test_serving_responses.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `6fa6e7ef0` - [ROCm][CI] Disable Async Scheduling For Qwen3-Next-80B-A3B-Instruct MTP Async EPLB Accuracy Test (#32275)

- Full hash: `6fa6e7ef0c9b485e8a684211e96691731aad6faa`
- Date/author: 2026-01-13 / Micah Williamson
- Auto category: 性能/后端优化
- Main files: `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `fefce4980` - [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240)

- Full hash: `fefce49807a52fc94678e336fc5d1f3b7ebe2daf`
- Date/author: 2026-01-13 / Chauncey
- Auto category: 性能/后端优化
- Main files: `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_completion_error.py`, `tests/entrypoints/openai/test_gptoss_structural_tags_integration.py`, `tests/entrypoints/openai/test_lora_resolvers.py`, `tests/entrypoints/openai/test_protocol.py` 等 128 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/basic_parsers.py`; `vllm/reasoning/deepseek_r1_reasoning_parser.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/ernie45_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/granite_reasoning_parser.py`; `vllm/reasoning/holo2_reasoning_parser.py` 等 45 个文件
  - runtime-model: `vllm/entrypoints/anthropic/serving_messages.py`; `vllm/entrypoints/context.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/chat_completion/__init__.py`; `vllm/entrypoints/openai/chat_completion/api_router.py`; `vllm/entrypoints/openai/chat_completion/protocol.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/chat_completion/stream_harmony.py` 等 43 个文件
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/responses/test_errors.py`; `tests/entrypoints/openai/responses/test_function_call_parsing.py`; `tests/entrypoints/openai/test_chat_error.py`; `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_completion_error.py`; `tests/entrypoints/openai/test_gptoss_structural_tags_integration.py`; `tests/entrypoints/openai/test_lora_resolvers.py`; `tests/entrypoints/openai/test_protocol.py` 等 39 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9f430c94b` - [BUGFIX] Add missed remaping of the names of fp8 kv-scale (#32199)

- Full hash: `9f430c94bd0b5cf5a697ddeefd4507ae078bb0ed`
- Date/author: 2026-01-13 / Vadim Gimpelson
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `e68b0dad8` - doc: Update model name for Qwen3-Coder in documentation (#32185)

- Full hash: `e68b0dad8b4070e3ae24603c12f53b6c659ba6f9`
- Date/author: 2026-01-12 / Andy Zhang
- Auto category: 调度/缓存/PD
- Main files: `docs/features/tool_calling.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/tool_calling.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `600aaab8d` - [Model] Remove incorrect `SupportsPP` from MTP models (#32150)

- Full hash: `600aaab8d626301f4dbfcd812ccf47b3e8d81ac9`
- Date/author: 2026-01-12 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`, `vllm/model_executor/models/longcat_flash_mtp.py`, `vllm/model_executor/models/openpangu_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/ernie_mtp.py`; `vllm/model_executor/models/openpangu_mtp.py`; `vllm/model_executor/models/qwen3_next_mtp.py`
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/longcat_flash_mtp.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8020a6040` - [Bugfix] Fix Qwen3-VL-Reranker model loading for sequence classification (#32089)

- Full hash: `8020a60402597740c7fbd0beba1d5f253983f82f`
- Date/author: 2026-01-11 / RickyChen / 陳昭儒
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/config.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/config.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `583a90e00` - [Refactor] Separate sequence and token pooling types (#32026)

- Full hash: `583a90e0055f3fa1fc464b2dd62ea26a7d389ae1`
- Date/author: 2026-01-10 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `tests/model_executor/test_model_load_with_params.py`, `tests/models/language/pooling/test_embedding.py`, `tests/models/language/pooling/test_mm_classifier_conversion.py`, `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/mteb_score_utils.py`, `tests/models/language/pooling_mteb_test/test_baai.py`, `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py`, `tests/models/language/pooling_mteb_test/test_cross_encoder.py` 等 42 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/pooling_params.py`; `vllm/tasks.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/pooler.py`; `vllm/entrypoints/llm.py`; `vllm/model_executor/layers/pooler/seqwise/methods.py`; `vllm/model_executor/layers/pooler/seqwise/poolers.py`; `vllm/model_executor/layers/pooler/tokwise/methods.py`; `vllm/model_executor/layers/pooler/tokwise/poolers.py`; `vllm/model_executor/models/bert.py` 等 20 个文件
  - tests: `tests/model_executor/test_model_load_with_params.py`; `tests/models/language/pooling/test_embedding.py`; `tests/models/language/pooling/test_mm_classifier_conversion.py`; `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`; `tests/models/language/pooling_mteb_test/mteb_score_utils.py`; `tests/models/language/pooling_mteb_test/test_baai.py`; `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py`; `tests/models/language/pooling_mteb_test/test_cross_encoder.py` 等 20 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `2612ba928` - [1/N][Attention] Restructure attention: move files (#31916)

- Full hash: `2612ba9285d828f3179801334b6d2db0046b9b6c`
- Date/author: 2026-01-09 / Matthew Bonanni
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml`, `.github/CODEOWNERS`, `.github/mergify.yml`, `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`, `docs/contributing/model/basic.md`, `docs/design/custom_op.md` 等 195 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/kernels.yaml`; `.github/CODEOWNERS`; `.github/mergify.yml`
  - docs-bench: `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`; `docs/contributing/model/basic.md`; `docs/design/custom_op.md`; `docs/design/plugin_system.md`; `examples/offline_inference/basic/embed.py`; `examples/offline_inference/basic/score.py`
  - other: `tools/pre_commit/mypy.py`; `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/xpu.py`; `vllm/v1/kv_offload/cpu.py` 等 10 个文件
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/layers/batch_invariant.py`; `vllm/model_executor/layers/kda.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/short_conv.py` 等 66 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/ops/__init__.py`; `vllm/config/attention.py`; `vllm/distributed/kv_transfer/kv_connector/utils.py`; `vllm/distributed/kv_transfer/kv_connector/v1/base.py`; `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py` 等 73 个文件
  - tests: `tests/compile/fullgraph/test_full_cudagraph.py`; `tests/compile/fullgraph/test_full_graph.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/config/test_multimodal_config.py`; `tests/engine/test_arg_utils.py`; `tests/kernels/attention/test_aiter_flash_attn.py`; `tests/kernels/attention/test_attention.py` 等 35 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `657e9c0e1` - [Fix] Introduce audio channels spec (#31595)

- Full hash: `657e9c0e183d4bdb157b07db987644d2d9d36245`
- Date/author: 2026-01-09 / Jeremy Teboul
- Auto category: 缺陷修复
- Main files: `docs/features/multimodal_inputs.md`, `tests/models/multimodal/processing/test_qwen3_omni.py`, `tests/multimodal/test_audio.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/model_executor/models/qwen2_audio.py`, `vllm/model_executor/models/ultravox.py`, `vllm/model_executor/models/whisper.py`, `vllm/multimodal/audio.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/multimodal_inputs.md`
  - other: `vllm/multimodal/audio.py`; `vllm/multimodal/parse.py`
  - runtime-model: `vllm/model_executor/models/qwen2_5_omni_thinker.py`; `vllm/model_executor/models/qwen2_audio.py`; `vllm/model_executor/models/ultravox.py`; `vllm/model_executor/models/whisper.py`
  - tests: `tests/models/multimodal/processing/test_qwen3_omni.py`; `tests/multimodal/test_audio.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1a19e9cd8` - [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten (#31380)

- Full hash: `1a19e9cd87b6bb091fc9c530e6446601db52b58e`
- Date/author: 2026-01-09 / vllmellm
- Auto category: 性能/后端优化
- Main files: `tests/kernels/attention/test_prefix_prefill.py`, `vllm/attention/ops/chunked_prefill_paged_decode.py`, `vllm/attention/ops/prefix_prefill.py`, `vllm/attention/ops/triton_reshape_and_cache_flash.py`, `vllm/v1/attention/backends/rocm_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/attention/ops/chunked_prefill_paged_decode.py`; `vllm/attention/ops/prefix_prefill.py`; `vllm/attention/ops/triton_reshape_and_cache_flash.py`; `vllm/v1/attention/backends/rocm_attn.py`
  - tests: `tests/kernels/attention/test_prefix_prefill.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0fa8dd24d` - [Bugfix] Fix Typo from NVFP4 Refactor (#31977)

- Full hash: `0fa8dd24d281f71c0b0f6fb5b6033ca30d97f932`
- Date/author: 2026-01-08 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-CT-fi-cutedsl-deepep-ll.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutedsl-deepep-ll.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/configs/moe-refactor/config-test.txt`, `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-CT-fi-cutedsl-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutedsl-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`; `tests/evals/gsm8k/configs/moe-refactor/config-test.txt`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `96fcd3c26` - [Misc] Support qwen3-next lora (#31719)

- Full hash: `96fcd3c267a0b16e3f94abd59e05cb3708a67db8`
- Date/author: 2026-01-08 / BingjiaWang
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `eac3b96ec` - [Models] Allow converting Qwen3-VL into Reranker model (#31890)

- Full hash: `eac3b96ec04d07a987823504671650a0bcad5a10`
- Date/author: 2026-01-08 / Isotr0py
- Auto category: 模型支持/运行时入口
- Main files: `docs/models/supported_models.md`, `examples/pooling/pooling/vision_language_pooling.py`, `examples/pooling/score/template/qwen3_vl_reranker.jinja`, `examples/pooling/score/vision_language_reranker.py`, `tests/models/registry.py`, `vllm/entrypoints/score_utils.py`, `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/config.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`; `examples/pooling/pooling/vision_language_pooling.py`; `examples/pooling/score/template/qwen3_vl_reranker.jinja`; `examples/pooling/score/vision_language_reranker.py`
  - runtime-model: `vllm/entrypoints/score_utils.py`; `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/config.py`
  - tests: `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `5dcd7ef1f` - [MoE Refactor][15/N] Apply Refactor to Fp8 (#31415)

- Full hash: `5dcd7ef1f219068e6b6be5b614bc43978f028651`
- Date/author: 2026-01-07 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`, `benchmarks/kernels/benchmark_moe.py`, `docs/design/moe_kernel_features.md`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ht.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml` 等 38 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`; `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`; `benchmarks/kernels/benchmark_moe.py`; `docs/design/moe_kernel_features.md`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/__init__.py`; `vllm/model_executor/layers/fused_moe/cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/fallback.py`; `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`; `vllm/model_executor/layers/fused_moe/oracle/__init__.py`; `vllm/model_executor/layers/fused_moe/oracle/fp8.py`; `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/triton_deep_gemm_moe.py` 等 16 个文件
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ht.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ht.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-CT-fi-cutlass.yaml` 等 17 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `482914849` - [BugFix] LoRA: Support loading base_layer of experts (#31104)

- Full hash: `482914849cf9ce61d3e0dffaa35096bb34de58f5`
- Date/author: 2026-01-07 / ℍ𝕠𝕝𝕝𝕠𝕨 𝕄𝕒𝕟
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/dots1.py`, `vllm/model_executor/models/ernie45_moe.py` 等 35 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/dots1.py`; `vllm/model_executor/models/gpt_oss.py`; `vllm/model_executor/models/grok1.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/jamba.py` 等 19 个文件
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py` 等 16 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `22dffca98` - [PERF] Speed-up of GDN attention decode part (Qwen3-Next) (#31722)

- Full hash: `22dffca9822987f0e912bfd9635e94bbdd05def3`
- Date/author: 2026-01-06 / Vadim Gimpelson
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fla/ops/fused_recurrent.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/fla/ops/fused_recurrent.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d3e477c01` - [MoE Refactor] Add Temporary Integration Tests - H100/B200 (#31759)

- Full hash: `d3e477c01342f800790b170b8fa799b467621358`
- Date/author: 2026-01-06 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-marlin.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml` 等 30 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - tests: `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-marlin.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-cutlass.yaml` 等 29 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `2c1a4f248` - [Bugfix]: avoid overriding audio/text kwargs (Qwen3-Omni) (#31790)

- Full hash: `2c1a4f2488da2bb3c60dcbbb5df61a370e39ee27`
- Date/author: 2026-01-06 / Jzz1943
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `874d2aaa5` - [feat] 支持 mRoPE 的 fused RMSNorm+RoPE 路径，并修正 torch.compile 动态维度标注 实现了用于优化张量计算的 rms_mrope_fuse 和 rms_mrope_fuse_fake 方法 更新了 forward：在满足条件时走新的 M-RoPE 融合路径 增强了 Qwen3MoeModel 对动态参数维度的支持，以适配该功能

- Full hash: `874d2aaa5060e46a33e9d09b30925e909da758bf`
- Date/author: 2026-01-06 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `da71d4441` - [Doc] Show that `use_audio_in_video` is supported in docs (#30837)

- Full hash: `da71d444107dbec33b597faebece6b816fab64eb`
- Date/author: 2026-01-06 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `docs/models/supported_models.md`, `examples/offline_inference/qwen2_5_omni/README.md`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`; `examples/offline_inference/qwen2_5_omni/README.md`
  - runtime-model: `vllm/model_executor/models/qwen2_5_omni_thinker.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d8a13c8df` - [Qwen3-480B] MoE configs for BW1000 TP=8(nn) & 16(nn) & 32(tn)

- Full hash: `d8a13c8dfecc0cce70ff9df408a0250852965d2f`
- Date/author: 2026-01-06 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/configs/E=160,N=160,device_name=gfx936_80cu_nn.json`, `vllm/model_executor/layers/fused_moe/configs/E=160,N=320,device_name=gfx936_80cu_nn.json`, `vllm/model_executor/layers/fused_moe/configs/E=160,N=80,device_name=gfx936_80cu.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=160,N=160,device_name=gfx936_80cu_nn.json`; `vllm/model_executor/layers/fused_moe/configs/E=160,N=320,device_name=gfx936_80cu_nn.json`; `vllm/model_executor/layers/fused_moe/configs/E=160,N=80,device_name=gfx936_80cu.json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8f16b5920` - [Qwen3-30B] MoE configs for BW1000 TP=2 (bs390)

- Full hash: `8f16b59202d88d16189d518407323cf313e4e583`
- Date/author: 2026-01-06 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/configs/E=128,N=384,device_name=gfx936_80cu_nn.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=384,device_name=gfx936_80cu_nn.json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5708297e4` - [Misc][Model][Refactor] Pass the prefix into Linear layers (#31669)

- Full hash: `5708297e4e7f27c4d06d6e4f62d75c3d2d1fc674`
- Date/author: 2026-01-06 / Wang Kunpeng
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/gpt_neox.py`, `vllm/model_executor/models/hunyuan_v1.py`, `vllm/model_executor/models/jamba.py`, `vllm/model_executor/models/jina_vl.py`, `vllm/model_executor/models/minicpm.py`, `vllm/model_executor/models/minicpm_eagle.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_mixer.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/gpt_neox.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/jamba.py`; `vllm/model_executor/models/jina_vl.py`; `vllm/model_executor/models/minicpm.py`; `vllm/model_executor/models/minicpm_eagle.py` 等 15 个文件
  - runtime-perf: `vllm/model_executor/models/olmoe.py`; `vllm/model_executor/models/phimoe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `911d38ed9` - [Model] Let more models to support the score template. (#31335)

- Full hash: `911d38ed99e1d191d3654f42fbeee97736092da8`
- Date/author: 2026-01-05 / wang.yuqi
- Auto category: 模型支持/运行时入口
- Main files: `docs/models/supported_models.md`, `examples/pooling/score/convert_model_to_seq_cls.py`, `examples/pooling/score/offline_reranker.py`, `examples/pooling/score/offline_using_template.py`, `examples/pooling/score/online_using_template.py`, `examples/pooling/score/qwen3_reranker_offline.py`, `examples/pooling/score/qwen3_reranker_online.py`, `examples/pooling/score/template/bge-reranker-v2-gemma.jinja` 等 23 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`; `examples/pooling/score/convert_model_to_seq_cls.py`; `examples/pooling/score/offline_reranker.py`; `examples/pooling/score/offline_using_template.py`; `examples/pooling/score/online_using_template.py`; `examples/pooling/score/qwen3_reranker_offline.py`; `examples/pooling/score/qwen3_reranker_online.py`; `examples/pooling/score/template/bge-reranker-v2-gemma.jinja` 等 12 个文件
  - runtime-model: `vllm/model_executor/models/config.py`
  - tests: `tests/conftest.py`; `tests/models/language/pooling_mteb_test/mteb_score_utils.py`; `tests/models/language/pooling_mteb_test/test_baai.py`; `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py`; `tests/models/language/pooling_mteb_test/test_cross_encoder.py`; `tests/models/language/pooling_mteb_test/test_gte.py`; `tests/models/language/pooling_mteb_test/test_jina.py`; `tests/models/language/pooling_mteb_test/test_mxbai_rerank.py` 等 10 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `97a01308e` - Improve HF qwen3_omni: preserve audio_sample_rate in kwargs restructuring (#29255)

- Full hash: `97a01308e9ceef351c5ae36bbc9f59b0a03f808b`
- Date/author: 2026-01-02 / jeremyteboul
- Auto category: 性能/后端优化
- Main files: `tests/models/multimodal/processing/test_qwen3_omni.py`, `tests/multimodal/test_processing.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
  - tests: `tests/models/multimodal/processing/test_qwen3_omni.py`; `tests/multimodal/test_processing.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0b6b70105` - [Model] Add tuned triton fused_moe configs for Qwen3Moe on B200 (#31448)

- Full hash: `0b6b7010508f85c3b54c49e35c1341031eb3b9c8`
- Date/author: 2025-12-29 / Jzz1943
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=NVIDIA_B200.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=NVIDIA_B200.json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ce1eafd1a` - [Core] Initialize LoRA support for tower and connector in multi-modal models (#26674)

- Full hash: `ce1eafd1a56bd5a4eb1ee743933a5e96e63d2116`
- Date/author: 2025-12-26 / Jee Jee Li
- Auto category: 模型支持/运行时入口
- Main files: `docs/features/lora.md`, `tests/lora/conftest.py`, `tests/lora/test_lora_manager.py`, `tests/lora/test_qwenvl.py`, `vllm/config/lora.py`, `vllm/engine/arg_utils.py`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/base_linear.py` 等 20 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/lora.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/lora/layers/__init__.py`; `vllm/lora/layers/base_linear.py`; `vllm/lora/layers/utils.py`; `vllm/lora/model_manager.py`; `vllm/v1/engine/input_processor.py`
  - runtime-model: `vllm/config/lora.py`; `vllm/lora/worker_manager.py`; `vllm/model_executor/models/idefics3.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py` 等 10 个文件
  - tests: `tests/lora/conftest.py`; `tests/lora/test_lora_manager.py`; `tests/lora/test_qwenvl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
