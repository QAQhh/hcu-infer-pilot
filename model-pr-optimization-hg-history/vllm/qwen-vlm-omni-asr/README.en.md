# vllm Qwen VLM/Omni/ASR Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `examples/offline_inference/qwen2_5_omni/README.md` | `da71d4441` |
| `examples/offline_inference/qwen2_5_omni/only_thinker.py` | `a698e8e7a`, `7e24e5d4d` |
| `examples/offline_inference/qwen3_omni/only_thinker.py` | `86a65417e`, `6ca2c91b9`, `7e24e5d4d` |
| `examples/pooling/score/template/qwen3_vl_reranker.jinja` | `eac3b96ec` |
| `examples/template_dse_qwen2_vl.jinja` | no direct commit |
| `tests/model_executor/test_qwen3_omni.py` | no direct commit |
| `tests/models/multimodal/generation/test_qwen2_5_vl.py` | no direct commit |
| `tests/models/multimodal/generation/test_qwen2_vl.py` | `aa3868ecf` |
| `tests/models/multimodal/pooling/test_dse_qwen2_vl.py` | no direct commit |
| `tests/models/multimodal/processing/test_qwen2_vl.py` | `f90319d5d`, `e83b7e379`, `27f4c2fd4` |
| `tests/models/multimodal/processing/test_qwen3_omni.py` | `657e9c0e1`, `97a01308e` |
| `vllm/model_executor/models/glmasr.py` | `df7041633`, `dcd80206b`, `e1a34c3a5`, `38bf2ffb2`, `9ea07b41d`, `2612ba928`, `2972a0547`, `974138751`, `d722e9e61` |
| `vllm/model_executor/models/glmasr_utils.py` | `37c9859fa`, `974138751`, `d722e9e61` |
| `vllm/model_executor/models/qwen2_5_omni_thinker.py` | `df7041633`, `dcd80206b`, `a698e8e7a`, `9ad7f89f5`, `4753f3bf6`, `9ea07b41d`, `657e9c0e1`, `da71d4441`, `6fe588765`, `87b4d1557`, `c46b932df`, `34a8559be`, ... (13 total) |
| `vllm/model_executor/models/qwen2_5_vl.py` | `dcd80206b`, `9ad7f89f5`, `04a9e064d`, `4753f3bf6`, `542a4059b`, `2612ba928`, `2972a0547`, `ce1eafd1a`, `8f8f469b1`, `ad8c07313`, `3bd9c4915`, `87b4d1557`, ... (18 total) |
| `vllm/model_executor/models/qwen2_audio.py` | `3a45ab97b`, `df7041633`, `dcd80206b`, `193069d12`, `9ea07b41d`, `657e9c0e1`, `dd424571c`, `c46b932df` |
| `vllm/model_executor/models/qwen2_vl.py` | `df7041633`, `dcd80206b`, `7e67df557`, `9ad7f89f5`, `4753f3bf6`, `9ea07b41d`, `542a4059b`, `2612ba928`, `2972a0547`, `ce1eafd1a`, `ad8c07313`, `3bd9c4915`, ... (22 total) |
| `vllm/model_executor/models/qwen3_asr.py` | `c50e6deea` |
| `vllm/model_executor/models/qwen3_omni_moe_thinker.py` | `df7041633`, `dcd80206b`, `6ca2c91b9`, `9ad7f89f5`, `193069d12`, `9ea07b41d`, `b8199f604`, `2612ba928`, `2c1a4f248`, `da71d4441`, `97a01308e`, `bb24592d1`, ... (19 total) |
| `vllm/model_executor/models/qwen3_vl.py` | `0bef83582`, `df7041633`, `dcd80206b`, `11b556878`, `7e67df557`, `9ad7f89f5`, `193069d12`, `04a9e064d`, `4753f3bf6`, `9ea07b41d`, `2612ba928`, `ce1eafd1a`, ... (27 total) |
| `vllm/model_executor/models/qwen3_vl_moe.py` | `0bef83582`, `df7041633`, `dcd80206b`, `9ad7f89f5`, `2b8a38b6d`, `7ab80a8e3`, `fda3f03eb`, `4753f3bf6`, `3f175f18a`, `87b4d1557` |
| `vllm/model_executor/models/qwen_vl.py` | `df7041633`, `dcd80206b`, `2b8a38b6d`, `976af2f31`, `9ea07b41d`, `5708297e4`, `c46b932df`, `fe3398fab` |
| `vllm/transformers_utils/configs/qwen3_asr.py` | `c50e6deea` |
| `vllm/transformers_utils/processors/qwen3_asr.py` | `c50e6deea` |

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
| 2026-03-17 | `3a45ab97b` | 性能/后端优化 | invoke flash_attn in the Qwen2AudioEncoder (transformers) | `vllm/model_executor/models/qwen2_audio.py` |
| 2026-03-06 | `7826240b0` | 模型支持/运行时入口 | Merge branch 'add-qwen3-asr' into 'v0.15.1-dev' |  |
| 2026-03-05 | `c50e6deea` | 模型支持/运行时入口 | add qwen3-asr | `vllm/model_executor/models/qwen3_asr.py`, `vllm/model_executor/models/registry.py`, `vllm/transformers_utils/configs/qwen3_asr.py` |
| 2026-03-02 | `c9733a54f` | 性能/后端优化 | Merge branch 'v0.15.1-dev-qwen3-vl-fused-rope' into 'v0.15.1-dev' |  |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-05 | `86a65417e` | 性能/后端优化 | sync v0.15.1 (ex tests&vllm) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/kernels/E=512,N=128,device_name=gfx936_80cu_nn.json`, `benchmarks/kernels/E=512,N=64,device_name=gfx936_80cu_nn.json` |
| 2026-01-29 | `1ed963d43` | 缺陷修复 | [Bugfix] Fix Qwen3-VL-Reranker load. (#33298) | `examples/pooling/score/vision_rerank_api_online.py`, `examples/pooling/score/vision_score_api_online.py`, `tests/entrypoints/pooling/classify/test_online_vision.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-26 | `6ca2c91b9` | 性能/后端优化 | [Model] Use mm_position to compute mrope positions for Qwen3-Omni (#33010) | `examples/offline_inference/qwen3_omni/only_thinker.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2026-01-26 | `11b556878` | 模型支持/运行时入口 | [Refactor] Use data parser for matching data items to multi-modal UUIDs (#32955) | `docs/features/multimodal_inputs.md`, `examples/pooling/plugin/prithvi_geospatial_mae_offline.py`, `tests/entrypoints/openai/test_vision_embeds.py` |
| 2026-01-25 | `a698e8e7a` | 模型支持/运行时入口 | [Model] Use mm_position to compute mrope positions for Qwen2.5-Omni (#32772) | `examples/offline_inference/qwen2_5_omni/only_thinker.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/v1/worker/gpu_model_runner.py` |
| 2026-01-25 | `7e67df557` | 缺陷修复 | [Bugfix] fix encoder cache hang in Qwen3VL (#32684) | `tests/models/multimodal/processing/test_tensor_schema.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/qwen3_vl.py` |
| 2026-01-24 | `9ad7f89f5` | 性能/后端优化 | [Models]: Make Multimodal config implicit in ViT implementation (#31972) | `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py` |
| 2026-01-23 | `37c9859fa` | 性能/后端优化 | [Refactor] Clean up unused variables & func (#32692) | `vllm/entrypoints/openai/engine/protocol.py`, `vllm/model_executor/layers/quantization/utils/petit_utils.py`, `vllm/model_executor/models/glmasr_utils.py` |
| 2026-01-22 | `2b8a38b6d` | 性能/后端优化 | [Model] Extend `collect_children` and `no_init_weights` contexts (#32757) | `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py` |
| 2026-01-20 | `7ab80a8e3` | 性能/后端优化 | Added qwen3 vision language moe support for speculative decoding (#32048) | `vllm/model_executor/models/qwen3_vl_moe.py`, `vllm/v1/spec_decode/eagle.py` |
| 2026-01-21 | `193069d12` | 性能/后端优化 | [5/N] Initialize MM components in context managers (Q-Z) (#32695) | `vllm/model_executor/models/qwen2_audio.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py` |
| 2026-01-21 | `04a9e064d` | 缺陷修复 | [Bugfix] fix the ima issue of qwen-vit (#32687) | `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen3_vl.py` |
| 2026-01-20 | `fda3f03eb` | 性能/后端优化 | [4/N] Initialize MM components in context managers (M-P) (#32663) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/interfaces.py` |
| 2026-01-20 | `e1a34c3a5` | 模型支持/运行时入口 | [2/N] Initialize MM components in context managers (E-H) (#32641) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/cohere2_vision.py` |
| 2026-01-20 | `4753f3bf6` | 性能/后端优化 | [Model] Use context managers for encoder- and LM-only mode (#32605) | `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/config/multimodal.py` |
| 2026-01-19 | `976af2f31` | 缺陷修复 | [BugFix] Fix embed_input_ids argument error of QwenVLForConditionalGeneration (#32462) | `vllm/model_executor/models/qwen_vl.py` |
| 2026-01-18 | `38bf2ffb2` | 缺陷修复 | [Bugfix] Fix GLM-ASR audio encoder RoPE dim (#32540) | `examples/offline_inference/audio_language.py`, `vllm/model_executor/models/glmasr.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-13 | `b8199f604` | 性能/后端优化 | [Model] Re-implement Qwen3Omni Audio Encoder (#32167) | `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2026-01-13 | `542a4059b` | 模型支持/运行时入口 | [Model] Use mm_position to compute mrope positions for Qwen2-VL/2.5-VL (#32126) | `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py` |
| 2026-01-11 | `8020a6040` | 缺陷修复 | [Bugfix] Fix Qwen3-VL-Reranker model loading for sequence classification (#32089) | `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/config.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-09 | `657e9c0e1` | 缺陷修复 | [Fix] Introduce audio channels spec (#31595) | `docs/features/multimodal_inputs.md`, `tests/models/multimodal/processing/test_qwen3_omni.py`, `tests/multimodal/test_audio.py` |
| 2026-01-08 | `2972a0547` | 模型支持/运行时入口 | [MM Encoder]: Make MMEncoderAttention's `scale` takes effect properly (#31950) | `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py` |
| 2026-01-08 | `eac3b96ec` | 模型支持/运行时入口 | [Models] Allow converting Qwen3-VL into Reranker model (#31890) | `docs/models/supported_models.md`, `examples/pooling/pooling/vision_language_pooling.py`, `examples/pooling/score/template/qwen3_vl_reranker.jinja` |
| 2026-01-07 | `8dd2419fa` | 模型支持/运行时入口 | [CI] Skip Qwen-VL in multimodal processing tests due to flaky external dependency (#31932) | `tests/models/multimodal/processing/test_common.py` |
| 2026-01-07 | `974138751` | 模型支持/运行时入口 | [Refactor] GLM-ASR Modeling (#31779) | `vllm/model_executor/models/glmasr.py`, `vllm/model_executor/models/glmasr_utils.py` |
| 2026-01-06 | `2c1a4f248` | 性能/后端优化 | [Bugfix]: avoid overriding audio/text kwargs (Qwen3-Omni) (#31790) | `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2026-01-06 | `da71d4441` | 性能/后端优化 | [Doc] Show that `use_audio_in_video` is supported in docs (#30837) | `docs/models/supported_models.md`, `examples/offline_inference/qwen2_5_omni/README.md`, `vllm/model_executor/models/qwen2_5_omni_thinker.py` |
| 2026-01-06 | `5708297e4` | 性能/后端优化 | [Misc][Model][Refactor] Pass the prefix into Linear layers (#31669) | `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/gpt_neox.py` |
| 2026-01-02 | `97a01308e` | 性能/后端优化 | Improve HF qwen3_omni: preserve audio_sample_rate in kwargs restructuring (#29255) | `tests/models/multimodal/processing/test_qwen3_omni.py`, `tests/multimodal/test_processing.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2025-12-31 | `d722e9e61` | 模型支持/运行时入口 | Add GLM-ASR multimodal support (#31436) | `docs/models/supported_models.md`, `examples/offline_inference/audio_language.py`, `tests/models/multimodal/processing/test_common.py` |
| 2025-12-26 | `ce1eafd1a` | 模型支持/运行时入口 | [Core] Initialize LoRA support for tower and connector in multi-modal models (#26674) | `docs/features/lora.md`, `tests/lora/conftest.py`, `tests/lora/test_lora_manager.py` |
| 2025-12-24 | `aa3868ecf` | 调度/缓存/PD | [Chore] Remove unused `noqa`s (#31263) | `tests/conftest.py`, `tests/entrypoints/openai/test_async_tokenization.py`, `tests/entrypoints/openai/test_chat.py` |
| 2025-12-24 | `bb24592d1` | 性能/后端优化 | [Qwen3-Omni] fixed _get_feat_extract_output_lengths function (#31007) | `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2025-12-24 | `dd424571c` | 缺陷修复 | [Bugfix] Enable `dynamic_dims` for different embeds shape (#31223) | `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/minicpmv.py`, `vllm/model_executor/models/qwen2_audio.py` |
| 2025-12-22 | `8f8f469b1` | 缺陷修复 | [BugFix] skip language model in Encoder (#30242) | `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/model_executor/model_loader/utils.py` |
| 2025-12-21 | `14c3e6ade` | 性能/后端优化 | [Misc] Fix spelling typos in model comments (#31117) | `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2025-12-19 | `058926d48` | 通用实现调整 | [XPU] allow custom workers (e.g. vllm-omni workers) to be used on XPU (#30935) | `vllm/platforms/xpu.py` |
| 2025-12-18 | `0db5439de` | 缺陷修复 | [Bugfix][torch2.10] Fix test_qwen2_5_vl_compilation with 2.10 RC (#30822) | `vllm/compilation/backends.py`, `vllm/compilation/caching.py`, `vllm/compilation/piecewise_backend.py` |
| 2025-12-18 | `6fe588765` | 模型支持/运行时入口 | [Chore] Remove v0 dead code for Qwen2.5-omni (#30883) | `vllm/model_executor/models/qwen2_5_omni_thinker.py` |
| 2025-12-16 | `16484d394` | 性能/后端优化 | [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475) | `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py` |
| 2025-12-16 | `ad8c07313` | 性能/后端优化 | [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873) | `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py` |
| 2025-12-16 | `f5f51e593` | 性能/后端优化 | [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475) | `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py` |
| 2025-12-16 | `3bd9c4915` | 性能/后端优化 | [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873) | `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py` |
| 2025-12-15 | `3f175f18a` | 性能/后端优化 | [Bugfix] Fix multimodal configuration for Qwen3VL MOE model (#30670) | `vllm/model_executor/models/qwen3_vl_moe.py` |
| 2025-12-15 | `87b4d1557` | 性能/后端优化 | [CustomOp][MM] Extract MMEncoderAttention as CustomOp and replace the backend of QwenVisionAttention with it. (#30125) | `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `vllm/attention/layer.py`, `vllm/attention/layers/mm_encoder_attention.py` |
| 2025-12-14 | `ae88aada3` | 模型支持/运行时入口 | [Feature]Add EVS (Efficient Video Sampling) Support for Qwen3-VL (#29752) | `vllm/model_executor/models/qwen3_vl.py` |
| 2025-12-14 | `48b8456ff` | 缺陷修复 | [Bugfix] Revert Qwen2-VL part of change in #28271 (#30542) | `vllm/model_executor/models/qwen2_vl.py` |
| 2025-12-14 | `3224ea991` | 模型支持/运行时入口 | [torch.compile] Add encoder tag for compilation (#30489) | `vllm/compilation/backends.py`, `vllm/compilation/piecewise_backend.py`, `vllm/model_executor/models/qwen2_5_vl.py` |
| 2025-12-12 | `f90319d5d` | 缺陷修复 | [Bugfix] Schedule failure due to wrong get_image_size_with_most_features (#29692) | `tests/models/multimodal/processing/test_gemma3.py`, `tests/models/multimodal/processing/test_qwen2_vl.py`, `vllm/model_executor/models/gemma3_mm.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-11 | `3a3b06ee7` | 缺陷修复 | [Misc] Improve error message for `is_multimodal` (#30483) | `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/phi3v.py`, `vllm/model_executor/models/qwen3_vl.py` |
| 2025-12-11 | `979f50efd` | 模型支持/运行时入口 | [Deprecation] Remove fallbacks for `embed_input_ids` and `embed_multimodal` (#30458) | `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/interfaces_base.py`, `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2025-12-11 | `7e24e5d4d` | 调度/缓存/PD | [Deprecation] Remove deprecated task, seed and MM settings (#30397) | `benchmarks/benchmark_ngram_proposer.py`, `examples/offline_inference/audio_language.py`, `examples/offline_inference/encoder_decoder_multimodal.py` |
| 2025-12-08 | `7b35011ad` | 测试/文档/基准 | Mark qwen2_5_vl as xfail (#30283) | `tests/compile/fullgraph/test_multimodal_compile.py` |
| 2025-12-08 | `bcb6f5947` | 性能/后端优化 | [Perf] Remove sync point in vit torch sdpa attn backend (#30232) | `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py` |
| 2025-12-07 | `e83b7e379` | 调度/缓存/PD | Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `27f4c2fd4` | 调度/缓存/PD | [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-06 | `671427efb` | 调度/缓存/PD | [Model] Move `multimodal_cpu_fields` definition to field config (#30181) | `tests/distributed/test_shm_storage.py`, `tests/multimodal/test_cache.py`, `tests/v1/test_serial_utils.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-05 | `6dcb07f67` | 模型支持/运行时入口 | support qwen3-vl handle requests with embeddings (#30037) | `docs/features/multimodal_inputs.md`, `vllm/model_executor/models/qwen3_vl.py` |
| 2025-12-05 | `b286a311c` | 调度/缓存/PD | [Chore] Deprecate `merge_by_field_config` arg (#30035) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_glm4_1v.py`, `tests/models/multimodal/processing/test_tensor_schema.py` |
| 2025-12-04 | `3f1b03739` | 性能/后端优化 | [ROCm] [Bugfix] `compute_attn_mask_seqlen` for qwen3 omni (#29974) | `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2025-12-02 | `6fc5841db` | 缺陷修复 | Fix some more Transformers nightly tests (#29872) | `examples/offline_inference/vision_language.py`, `examples/offline_inference/vision_language_multi_image.py`, `tests/models/registry.py` |
| 2025-12-02 | `34a8559be` | 调度/缓存/PD | [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py` |
| 2025-12-03 | `a2b053dc8` | 性能/后端优化 | feat(model): Add BitsAndBytes quantization support for Qwen3-Omni-MoE (#29896) | `vllm/model_executor/models/qwen3_omni_moe_thinker.py` |
| 2025-12-02 | `68ffbca7e` | 调度/缓存/PD | [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py` |
| 2025-11-29 | `fe3398fab` | 模型支持/运行时入口 | [Chore] Enable passing `tokenizer=None` into MM processor (#29724) | `tests/multimodal/test_processing.py`, `vllm/entrypoints/openai/serving_engine.py`, `vllm/inputs/preprocess.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-28 | `460d8bbf2` | 性能/后端优化 | Remove upstream fa checks (#29471) | `vllm/attention/layer.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/attention/utils/fa_utils.py` |
| 2025-11-28 | `b34e8775a` | 调度/缓存/PD | Revert "[CPU]Update CPU PyTorch to 2.9.0 (#29589)" (#29647) | `docker/Dockerfile.cpu`, `requirements/cpu-build.txt`, `requirements/cpu.txt` |
| 2025-11-28 | `37b15e97e` | 调度/缓存/PD | [Multimodal][Speculative Decoding]Eagle3 mm support, enablement on qwen3vl (#29594) | `tests/models/registry.py`, `tests/v1/e2e/test_spec_decode.py`, `vllm/model_executor/models/qwen3_vl.py` |

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

### Commit `3a45ab97b` - invoke flash_attn in the Qwen2AudioEncoder (transformers)

- Full hash: `3a45ab97bf2ae6f755b428b0298f5b98279d4378`
- Date/author: 2026-03-17 / caihl
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen2_audio.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen2_audio.py`
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

### Commit `a698e8e7a` - [Model] Use mm_position to compute mrope positions for Qwen2.5-Omni (#32772)

- Full hash: `a698e8e7ad4bd06c0197bd79c9c200bef71be189`
- Date/author: 2026-01-25 / Itay Etelis
- Auto category: 模型支持/运行时入口
- Main files: `examples/offline_inference/qwen2_5_omni/only_thinker.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/v1/worker/gpu_model_runner.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/offline_inference/qwen2_5_omni/only_thinker.py`
  - runtime-model: `vllm/model_executor/models/qwen2_5_omni_thinker.py`; `vllm/v1/worker/gpu_model_runner.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `37c9859fa` - [Refactor] Clean up unused variables & func (#32692)

- Full hash: `37c9859fab60bbc346be20a662387479eb0760de`
- Date/author: 2026-01-23 / Wentao Ye
- Auto category: 性能/后端优化
- Main files: `vllm/entrypoints/openai/engine/protocol.py`, `vllm/model_executor/layers/quantization/utils/petit_utils.py`, `vllm/model_executor/models/glmasr_utils.py`, `vllm/model_executor/models/phi4mm_audio.py`, `vllm/platforms/rocm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/entrypoints/openai/engine/protocol.py`; `vllm/model_executor/models/glmasr_utils.py`; `vllm/model_executor/models/phi4mm_audio.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/petit_utils.py`; `vllm/platforms/rocm.py`
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

### Commit `e1a34c3a5` - [2/N] Initialize MM components in context managers (E-H) (#32641)

- Full hash: `e1a34c3a5d9273431ee182253750d39b546d37a1`
- Date/author: 2026-01-20 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/cohere2_vision.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/fuyu.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/gemma3n_mm.py`, `vllm/model_executor/models/glm4_1v.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/cohere2_vision.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/fuyu.py`; `vllm/model_executor/models/gemma3_mm.py`; `vllm/model_executor/models/gemma3n_mm.py`; `vllm/model_executor/models/glm4_1v.py` 等 12 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `976af2f31` - [BugFix] Fix embed_input_ids argument error of QwenVLForConditionalGeneration (#32462)

- Full hash: `976af2f314d1c7d54e3707e325df2b5961c069a4`
- Date/author: 2026-01-19 / honglyua
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `38bf2ffb2` - [Bugfix] Fix GLM-ASR audio encoder RoPE dim (#32540)

- Full hash: `38bf2ffb21d54eb67a68d4ba82125922f4a4c7ad`
- Date/author: 2026-01-18 / Isotr0py
- Auto category: 缺陷修复
- Main files: `examples/offline_inference/audio_language.py`, `vllm/model_executor/models/glmasr.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/offline_inference/audio_language.py`
  - runtime-model: `vllm/model_executor/models/glmasr.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `542a4059b` - [Model] Use mm_position to compute mrope positions for Qwen2-VL/2.5-VL (#32126)

- Full hash: `542a4059b2bb0f790e82822c8b9cbcf8cde91adb`
- Date/author: 2026-01-13 / YunzhuLu
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `8020a6040` - [Bugfix] Fix Qwen3-VL-Reranker model loading for sequence classification (#32089)

- Full hash: `8020a60402597740c7fbd0beba1d5f253983f82f`
- Date/author: 2026-01-11 / RickyChen / 陳昭儒
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/config.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/config.py`
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

### Commit `2972a0547` - [MM Encoder]: Make MMEncoderAttention's `scale` takes effect properly  (#31950)

- Full hash: `2972a05473d64a21c7390a5676bbb07bd8d2c8da`
- Date/author: 2026-01-08 / Isotr0py
- Auto category: 模型支持/运行时入口
- Main files: `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glmasr.py`, `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/moonvit.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glmasr.py`; `vllm/model_executor/models/isaac.py`; `vllm/model_executor/models/moonvit.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_vl.py` 等 9 个文件
  - runtime-perf: `vllm/attention/layers/mm_encoder_attention.py`; `vllm/attention/ops/vit_attn_wrappers.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `8dd2419fa` - [CI] Skip Qwen-VL in multimodal processing tests due to flaky external dependency (#31932)

- Full hash: `8dd2419fa96488bc862ad60f7fc7ffffa39728e7`
- Date/author: 2026-01-07 / Andreas Karatzas
- Auto category: 模型支持/运行时入口
- Main files: `tests/models/multimodal/processing/test_common.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_common.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `974138751` - [Refactor] GLM-ASR Modeling (#31779)

- Full hash: `974138751bdb8e41743d0beac0ac4c5d89308c2f`
- Date/author: 2026-01-07 / Jared Wen
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/glmasr.py`, `vllm/model_executor/models/glmasr_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/glmasr.py`; `vllm/model_executor/models/glmasr_utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `2c1a4f248` - [Bugfix]: avoid overriding audio/text kwargs (Qwen3-Omni) (#31790)

- Full hash: `2c1a4f2488da2bb3c60dcbbb5df61a370e39ee27`
- Date/author: 2026-01-06 / Jzz1943
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
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

### Commit `d722e9e61` - Add GLM-ASR multimodal support  (#31436)

- Full hash: `d722e9e614f667ed9b6f951fdc284646bf3a572c`
- Date/author: 2025-12-31 / baonudesifeizhai
- Auto category: 模型支持/运行时入口
- Main files: `docs/models/supported_models.md`, `examples/offline_inference/audio_language.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/registry.py`, `vllm/model_executor/models/glmasr.py`, `vllm/model_executor/models/glmasr_utils.py`, `vllm/model_executor/models/registry.py`, `vllm/transformers_utils/config.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`; `examples/offline_inference/audio_language.py`
  - runtime-model: `vllm/model_executor/models/glmasr.py`; `vllm/model_executor/models/glmasr_utils.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/config.py`
  - tests: `tests/models/multimodal/processing/test_common.py`; `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `aa3868ecf` - [Chore] Remove unused `noqa`s (#31263)

- Full hash: `aa3868ecfe65036349412ce54fa5b07cb545d836`
- Date/author: 2025-12-24 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `tests/conftest.py`, `tests/entrypoints/openai/test_async_tokenization.py`, `tests/entrypoints/openai/test_chat.py`, `tests/entrypoints/openai/test_chat_with_tool_reasoning.py`, `tests/entrypoints/openai/test_completion_with_function_calling.py`, `tests/entrypoints/openai/test_default_mm_loras.py`, `tests/entrypoints/openai/test_enable_force_include_usage.py`, `tests/entrypoints/openai/test_messages.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/entrypoints/serve/elastic_ep/api_router.py`; `vllm/model_executor/model_loader/bitsandbytes_loader.py`; `vllm/model_executor/model_loader/runai_streamer_loader.py`; `vllm/v1/worker/ec_connector_model_runner_mixin.py`; `vllm/v1/worker/kv_connector_model_runner_mixin.py`
  - runtime-perf: `vllm/distributed/ec_transfer/ec_connector/example_connector.py`
  - tests: `tests/conftest.py`; `tests/entrypoints/openai/test_async_tokenization.py`; `tests/entrypoints/openai/test_chat.py`; `tests/entrypoints/openai/test_chat_with_tool_reasoning.py`; `tests/entrypoints/openai/test_completion_with_function_calling.py`; `tests/entrypoints/openai/test_default_mm_loras.py`; `tests/entrypoints/openai/test_enable_force_include_usage.py`; `tests/entrypoints/openai/test_messages.py` 等 11 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bb24592d1` - [Qwen3-Omni] fixed _get_feat_extract_output_lengths function (#31007)

- Full hash: `bb24592d139b48f036d46a4649a2a867fea67f3a`
- Date/author: 2025-12-24 / Xiong Wang
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `dd424571c` - [Bugfix] Enable `dynamic_dims` for different embeds shape (#31223)

- Full hash: `dd424571c8edaf7c68fe4ff400da8ef9f26a1e48`
- Date/author: 2025-12-24 / Cyrus Leung
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/minicpmv.py`, `vllm/model_executor/models/qwen2_audio.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/minicpmv.py`; `vllm/model_executor/models/qwen2_audio.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `8f8f469b1` - [BugFix] skip language model in Encoder (#30242)

- Full hash: `8f8f469b1b8c4ef44a0a8a5f0bc6ddf86acbc9db`
- Date/author: 2025-12-22 / dengyunyang
- Auto category: 缺陷修复
- Main files: `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/v1/worker/gpu_model_runner.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/online_serving/disaggregated_encoder/README.md`
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `14c3e6ade` - [Misc] Fix spelling typos in model comments (#31117)

- Full hash: `14c3e6ade3605852282ec895397e6403b609847a`
- Date/author: 2025-12-21 / Kevin McKay
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/config.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `058926d48` - [XPU] allow custom workers (e.g. vllm-omni workers) to be used on XPU (#30935)

- Full hash: `058926d48c2435496839ec8e7e3ee90683ea7791`
- Date/author: 2025-12-19 / Fanli Lin
- Auto category: 通用实现调整
- Main files: `vllm/platforms/xpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/platforms/xpu.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `0db5439de` - [Bugfix][torch2.10] Fix test_qwen2_5_vl_compilation with 2.10 RC (#30822)

- Full hash: `0db5439ded739731474009217a7515fd52c221c8`
- Date/author: 2025-12-18 / Lucas Kabela
- Auto category: 缺陷修复
- Main files: `vllm/compilation/backends.py`, `vllm/compilation/caching.py`, `vllm/compilation/piecewise_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/compilation/backends.py`; `vllm/compilation/caching.py`; `vllm/compilation/piecewise_backend.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `6fe588765` - [Chore] Remove v0 dead code for Qwen2.5-omni (#30883)

- Full hash: `6fe58876528751a808c0d25016d3c97b432b909f`
- Date/author: 2025-12-18 / Isotr0py
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/qwen2_5_omni_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen2_5_omni_thinker.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `16484d394` - [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475)

- Full hash: `16484d394c6046890635b7895edb4deca2f1b1b0`
- Date/author: 2025-12-16 / Roger Wang
- Auto category: 性能/后端优化
- Main files: `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py`, `tests/v1/ec_connector/unit/test_ec_example_connector.py`, `vllm/distributed/ec_transfer/ec_connector/example_connector.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/multimodal/inputs.py`, `vllm/multimodal/profiling.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/profiling.py`; `vllm/multimodal/registry.py`; `vllm/v1/request.py`
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/utils.py`
  - runtime-perf: `vllm/distributed/ec_transfer/ec_connector/example_connector.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/models/multimodal/processing/test_mllama4.py`; `tests/multimodal/test_utils.py`; `tests/v1/core/test_encoder_cache_manager.py`; `tests/v1/ec_connector/unit/test_ec_example_connector.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ad8c07313` - [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873)

- Full hash: `ad8c073131f52365ca9917b546f39185f39a49cb`
- Date/author: 2025-12-16 / Shanshan Shen
- Auto category: 性能/后端优化
- Main files: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`, `vllm/model_executor/layers/rotary_embedding/xdrope.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/layers/rotary_embedding/common.py`; `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`; `vllm/model_executor/layers/rotary_embedding/mrope.py`; `vllm/model_executor/layers/rotary_embedding/xdrope.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py` 等 13 个文件
  - tests: `tests/kernels/core/test_apply_rotary_emb.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f5f51e593` - [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475)

- Full hash: `f5f51e5931ffd99afe69696b60765b88d3eb13f2`
- Date/author: 2025-12-16 / Roger Wang
- Auto category: 性能/后端优化
- Main files: `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py`, `tests/v1/ec_connector/unit/test_ec_example_connector.py`, `vllm/distributed/ec_transfer/ec_connector/example_connector.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/multimodal/inputs.py`, `vllm/multimodal/profiling.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/profiling.py`; `vllm/multimodal/registry.py`; `vllm/v1/request.py`
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/utils.py`
  - runtime-perf: `vllm/distributed/ec_transfer/ec_connector/example_connector.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/models/multimodal/processing/test_mllama4.py`; `tests/multimodal/test_utils.py`; `tests/v1/core/test_encoder_cache_manager.py`; `tests/v1/ec_connector/unit/test_ec_example_connector.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `3bd9c4915` - [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873)

- Full hash: `3bd9c491583d45ae9f3f24b10e99626f502014b4`
- Date/author: 2025-12-16 / Shanshan Shen
- Auto category: 性能/后端优化
- Main files: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`, `vllm/model_executor/layers/rotary_embedding/xdrope.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/layers/rotary_embedding/common.py`; `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`; `vllm/model_executor/layers/rotary_embedding/mrope.py`; `vllm/model_executor/layers/rotary_embedding/xdrope.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py` 等 13 个文件
  - tests: `tests/kernels/core/test_apply_rotary_emb.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `3f175f18a` - [Bugfix] Fix multimodal configuration for Qwen3VL MOE model (#30670)

- Full hash: `3f175f18a2e5d430ffa17fcb96759a758cc3ec05`
- Date/author: 2025-12-15 / Max Hu
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_vl_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `87b4d1557` - [CustomOp][MM] Extract MMEncoderAttention as CustomOp and replace the backend of QwenVisionAttention with it. (#30125)

- Full hash: `87b4d1557dc83addf5dd8568862ee7a74882200a`
- Date/author: 2025-12-15 / Shanshan Shen
- Auto category: 性能/后端优化
- Main files: `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `vllm/attention/layer.py`, `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/keye.py` 等 24 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/platforms/interface.py`; `vllm/platforms/tpu.py`; `vllm/platforms/xpu.py`
  - runtime-model: `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/opencua.py`; `vllm/model_executor/models/ovis2_5.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 13 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/layers/mm_encoder_attention.py`; `vllm/attention/ops/vit_attn_wrappers.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/model_executor/models/qwen3_vl_moe.py`; `vllm/platforms/cuda.py`; `vllm/platforms/rocm.py`
  - tests: `tests/models/multimodal/generation/test_vit_backend_functionality.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ae88aada3` - [Feature]Add EVS (Efficient Video Sampling) Support for Qwen3-VL (#29752)

- Full hash: `ae88aada38eca50f6b7e3c9caf2ac410e76964c9`
- Date/author: 2025-12-14 / ZiTian Zhao
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `48b8456ff` - [Bugfix] Revert Qwen2-VL part of change in #28271 (#30542)

- Full hash: `48b8456ff9927f619ab9463106735b83d3035113`
- Date/author: 2025-12-14 / zifeitong
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen2_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen2_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `3224ea991` - [torch.compile] Add encoder tag for compilation (#30489)

- Full hash: `3224ea9915750cdd714d85c843264923ef4018cc`
- Date/author: 2025-12-14 / Ilya Markov
- Auto category: 模型支持/运行时入口
- Main files: `vllm/compilation/backends.py`, `vllm/compilation/piecewise_backend.py`, `vllm/model_executor/models/qwen2_5_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/compilation/backends.py`; `vllm/compilation/piecewise_backend.py`
  - runtime-model: `vllm/model_executor/models/qwen2_5_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f90319d5d` - [Bugfix] Schedule failure due to wrong get_image_size_with_most_features (#29692)

- Full hash: `f90319d5d14266769b65f0de28ff60b002a65fcc`
- Date/author: 2025-12-12 / Jaehwang Jung
- Auto category: 缺陷修复
- Main files: `tests/models/multimodal/processing/test_gemma3.py`, `tests/models/multimodal/processing/test_qwen2_vl.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/qwen2_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/gemma3_mm.py`; `vllm/model_executor/models/qwen2_vl.py`
  - tests: `tests/models/multimodal/processing/test_gemma3.py`; `tests/models/multimodal/processing/test_qwen2_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `cf3eacfe5` - Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389)

- Full hash: `cf3eacfe58fa9e745c2854782ada884a9f992cf7`
- Date/author: 2025-12-11 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `vllm/config/utils.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/afmoe.py` 等 83 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `benchmarks/kernels/benchmark_rope.py`
  - runtime-model: `vllm/config/utils.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/olmoe.py` 等 12 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `3a3b06ee7` - [Misc] Improve error message for `is_multimodal` (#30483)

- Full hash: `3a3b06ee706e6ff99b711b20a6c431b43e490dbc`
- Date/author: 2025-12-11 / Cyrus Leung
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/phi3v.py`, `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/phi3v.py`; `vllm/model_executor/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `979f50efd` - [Deprecation] Remove fallbacks for `embed_input_ids` and `embed_multimodal` (#30458)

- Full hash: `979f50efd04552654eca57c7e71e38160a7cbb5c`
- Date/author: 2025-12-11 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/interfaces_base.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`, `vllm/model_executor/models/phi3v.py`, `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/interfaces_base.py`; `vllm/model_executor/models/mistral_large_3_eagle.py`; `vllm/model_executor/models/phi3v.py`; `vllm/model_executor/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `7e24e5d4d` - [Deprecation] Remove deprecated task, seed and MM settings (#30397)

- Full hash: `7e24e5d4d65abbe5ffc7e653fdfd670c7e300944`
- Date/author: 2025-12-11 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `benchmarks/benchmark_ngram_proposer.py`, `examples/offline_inference/audio_language.py`, `examples/offline_inference/encoder_decoder_multimodal.py`, `examples/offline_inference/qwen2_5_omni/only_thinker.py`, `examples/offline_inference/qwen3_omni/only_thinker.py`, `examples/offline_inference/vision_language.py`, `examples/offline_inference/vision_language_multi_image.py`, `examples/pooling/plugin/prithvi_geospatial_mae_client.py` 等 16 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/benchmark_ngram_proposer.py`; `examples/offline_inference/audio_language.py`; `examples/offline_inference/encoder_decoder_multimodal.py`; `examples/offline_inference/qwen2_5_omni/only_thinker.py`; `examples/offline_inference/qwen3_omni/only_thinker.py`; `examples/offline_inference/vision_language.py`; `examples/offline_inference/vision_language_multi_image.py`; `examples/pooling/plugin/prithvi_geospatial_mae_client.py` 等 9 个文件
  - other: `vllm/engine/arg_utils.py`; `vllm/envs.py`
  - runtime-model: `vllm/config/model.py`; `vllm/entrypoints/llm.py`
  - tests: `tests/conftest.py`; `tests/test_config.py`; `tests/utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `7b35011ad` - Mark qwen2_5_vl as xfail (#30283)

- Full hash: `7b35011ad136748b3d18d069103feda9a239459f`
- Date/author: 2025-12-08 / Yanan Cao
- Auto category: 测试/文档/基准
- Main files: `tests/compile/fullgraph/test_multimodal_compile.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/compile/fullgraph/test_multimodal_compile.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `bcb6f5947` - [Perf] Remove sync point in vit torch sdpa attn backend (#30232)

- Full hash: `bcb6f5947f8acac22f5d1d5fc92a91b06fd57e77`
- Date/author: 2025-12-08 / Dazhi Jiang
- Auto category: 性能/后端优化
- Main files: `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen2_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/qwen2_vl.py`
  - runtime-perf: `vllm/attention/ops/vit_attn_wrappers.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e83b7e379` - Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199)

- Full hash: `e83b7e379c11bf136c1b96bc6a67b6d2207cfde4`
- Date/author: 2025-12-07 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py`, `tests/compile/test_fusion.py`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_pass_manager.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/distributed/test_kvlayout.py` 等 105 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/transcription.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/processor.py`; `vllm/v1/engine/async_llm.py` 等 12 个文件
  - runtime-model: `vllm/config/__init__.py`; `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/config/renderer.py`; `vllm/config/speculative.py`; `vllm/config/vllm.py`; `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py` 等 33 个文件
  - runtime-perf: `vllm/multimodal/cache.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/compile/distributed/test_sequence_parallelism.py`; `tests/compile/test_functionalization.py`; `tests/compile/test_fusion.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_pass_manager.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/distributed/test_kvlayout.py`; `tests/entrypoints/openai/test_chat_template.py` 等 56 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `27f4c2fd4` - [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)

- Full hash: `27f4c2fd46b99778d7ea19dfe7751fbaab615177`
- Date/author: 2025-12-07 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py`, `tests/compile/test_fusion.py`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_pass_manager.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/distributed/test_kvlayout.py` 等 105 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/transcription.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/processor.py`; `vllm/v1/engine/async_llm.py` 等 12 个文件
  - runtime-model: `vllm/config/__init__.py`; `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/config/renderer.py`; `vllm/config/speculative.py`; `vllm/config/vllm.py`; `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py` 等 33 个文件
  - runtime-perf: `vllm/multimodal/cache.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/compile/distributed/test_sequence_parallelism.py`; `tests/compile/test_functionalization.py`; `tests/compile/test_fusion.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_pass_manager.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/distributed/test_kvlayout.py`; `tests/entrypoints/openai/test_chat_template.py` 等 56 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `671427efb` - [Model] Move `multimodal_cpu_fields` definition to field config (#30181)

- Full hash: `671427efbf57d4e40370a336cf1d3a4d1fd8eb91`
- Date/author: 2025-12-06 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `tests/distributed/test_shm_storage.py`, `tests/multimodal/test_cache.py`, `tests/v1/test_serial_utils.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/hunyuan_vision.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/opencua.py`, `vllm/model_executor/models/qwen2_5_vl.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/utils.py`; `vllm/v1/serial_utils.py`
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/hunyuan_vision.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/opencua.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py` 等 9 个文件
  - tests: `tests/distributed/test_shm_storage.py`; `tests/multimodal/test_cache.py`; `tests/v1/test_serial_utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c46b932df` - [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170)

- Full hash: `c46b932df2b801ba0a6452e436268f086029d82b`
- Date/author: 2025-12-06 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/cohere2_vision.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/deepseek_vl2.py` 等 61 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/utils.py`
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/blip2.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/cohere2_vision.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/deepseek_vl2.py` 等 59 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6dcb07f67` - support qwen3-vl handle requests with embeddings (#30037)

- Full hash: `6dcb07f676ae473703b4ab69ef15d93f51d24ce8`
- Date/author: 2025-12-05 / Tao Yun
- Auto category: 模型支持/运行时入口
- Main files: `docs/features/multimodal_inputs.md`, `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/multimodal_inputs.md`
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b286a311c` - [Chore] Deprecate `merge_by_field_config` arg (#30035)

- Full hash: `b286a311c2bab639ce6edc998a9a67c0affc9cbf`
- Date/author: 2025-12-05 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_glm4_1v.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/multimodal/test_cache.py`, `tests/multimodal/test_inputs.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/lightonocr.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/utils.py`; `vllm/v1/serial_utils.py`
  - runtime-model: `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/lightonocr.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/opencua.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/paligemma.py`; `vllm/model_executor/models/qwen2_5_vl.py` 等 10 个文件
  - runtime-perf: `vllm/multimodal/cache.py`
  - tests: `tests/models/multimodal/processing/test_common.py`; `tests/models/multimodal/processing/test_glm4_1v.py`; `tests/models/multimodal/processing/test_tensor_schema.py`; `tests/multimodal/test_cache.py`; `tests/multimodal/test_inputs.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `3f1b03739` - [ROCm] [Bugfix] `compute_attn_mask_seqlen` for qwen3 omni (#29974)

- Full hash: `3f1b03739ae1422361446d3d23bed970bd549ebc`
- Date/author: 2025-12-04 / TJian
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6fc5841db` - Fix some more Transformers nightly tests (#29872)

- Full hash: `6fc5841db14efedae7e6a8d1abdde3516c6c35a1`
- Date/author: 2025-12-02 / Harry Mellor
- Auto category: 缺陷修复
- Main files: `examples/offline_inference/vision_language.py`, `examples/offline_inference/vision_language_multi_image.py`, `tests/models/registry.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/tokenizers/mistral.py`, `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/tarsier2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/offline_inference/vision_language.py`; `examples/offline_inference/vision_language_multi_image.py`
  - other: `vllm/tokenizers/mistral.py`
  - runtime-model: `vllm/model_executor/models/qwen2_vl.py`; `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/tarsier2.py`
  - tests: `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `34a8559be` - [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851)

- Full hash: `34a8559be7473e3ba34e9b9e13827e60651e3b41`
- Date/author: 2025-12-02 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py`, `vllm/entrypoints/renderer.py`, `vllm/entrypoints/score_utils.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/multimodal/processing.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/processing.py`; `vllm/transformers_utils/tokenizer.py`
  - runtime-model: `vllm/entrypoints/openai/speech_to_text.py`; `vllm/entrypoints/renderer.py`; `vllm/entrypoints/score_utils.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py`
  - tests: `tests/models/multimodal/processing/test_common.py`; `tests/models/multimodal/processing/test_llama4.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `a2b053dc8` - feat(model): Add BitsAndBytes quantization support for Qwen3-Omni-MoE (#29896)

- Full hash: `a2b053dc858db461d8d98cff37ee7c67ba21126b`
- Date/author: 2025-12-03 / Navanit Dubey
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `68ffbca7e` - [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851)

- Full hash: `68ffbca7e462cfa6a32b46dabc9a604c7c1b918d`
- Date/author: 2025-12-02 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py`, `vllm/entrypoints/renderer.py`, `vllm/entrypoints/score_utils.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/multimodal/processing.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/processing.py`; `vllm/transformers_utils/tokenizer.py`
  - runtime-model: `vllm/entrypoints/openai/speech_to_text.py`; `vllm/entrypoints/renderer.py`; `vllm/entrypoints/score_utils.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py`
  - tests: `tests/models/multimodal/processing/test_common.py`; `tests/models/multimodal/processing/test_llama4.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `fe3398fab` - [Chore] Enable passing `tokenizer=None` into MM processor (#29724)

- Full hash: `fe3398fab2b11f92b4ada209a85558710c446a36`
- Date/author: 2025-11-29 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `tests/multimodal/test_processing.py`, `vllm/entrypoints/openai/serving_engine.py`, `vllm/inputs/preprocess.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/qwen_vl.py`, `vllm/multimodal/processing.py`, `vllm/multimodal/registry.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`
  - runtime-model: `vllm/entrypoints/openai/serving_engine.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/model_executor/models/qwen_vl.py`
  - tests: `tests/multimodal/test_processing.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `34a984274` - [Misc] Refactor tokenizer interface (#29693)

- Full hash: `34a984274eae2f8fb9d1d6413abd08d7fcde741c`
- Date/author: 2025-11-29 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py`, `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_engine.py`, `tests/entrypoints/openai/tool_parsers/conftest.py`, `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py` 等 119 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/backend_request_func.py`; `docs/features/reasoning_outputs.md`; `docs/features/tool_calling.md`
  - other: `tools/pre_commit/check_pickle_imports.py`; `tools/pre_commit/mypy.py`; `vllm/benchmarks/datasets.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/logits_process.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py` 等 32 个文件
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_classification.py`; `vllm/entrypoints/openai/serving_completion.py`; `vllm/entrypoints/openai/serving_engine.py`; `vllm/entrypoints/openai/serving_responses.py`; `vllm/entrypoints/openai/serving_score.py` 等 44 个文件
  - runtime-perf: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/test_serving_engine.py`; `tests/entrypoints/openai/tool_parsers/conftest.py`; `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/utils.py` 等 37 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `460d8bbf2` - Remove upstream fa checks (#29471)

- Full hash: `460d8bbf2d19fc4757b3253050a0a18b61c136e3`
- Date/author: 2025-11-28 / Mingyuan Ma
- Auto category: 性能/后端优化
- Main files: `vllm/attention/layer.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/attention/utils/fa_utils.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/paddleocr_vl.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py` 等 9 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/ops/vit_attn_wrappers.py`; `vllm/attention/utils/fa_utils.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b34e8775a` - Revert "[CPU]Update CPU PyTorch to 2.9.0 (#29589)" (#29647)

- Full hash: `b34e8775a31c1a077a1a24f22ffbf048b2a979f6`
- Date/author: 2025-11-28 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `docker/Dockerfile.cpu`, `requirements/cpu-build.txt`, `requirements/cpu.txt`, `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `docker/Dockerfile.cpu`; `requirements/cpu-build.txt`; `requirements/cpu.txt`
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `37b15e97e` - [Multimodal][Speculative Decoding]Eagle3 mm support, enablement on qwen3vl (#29594)

- Full hash: `37b15e97e8443a7fd76f5aa95a78d5593f7241a4`
- Date/author: 2025-11-28 / EanWang211123
- Auto category: 调度/缓存/PD
- Main files: `tests/models/registry.py`, `tests/v1/e2e/test_spec_decode.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/registry.py`, `vllm/v1/spec_decode/eagle.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`; `vllm/model_executor/models/registry.py`
  - tests: `tests/models/registry.py`; `tests/v1/e2e/test_spec_decode.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
