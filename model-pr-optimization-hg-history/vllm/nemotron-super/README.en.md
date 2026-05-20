# vllm Nemotron Super Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `examples/pooling/score/template/nemotron-rerank.jinja` | `23daef548` |
| `tests/models/language/pooling_mteb_test/test_nemotron.py` | `583a90e00`, `911d38ed9`, `1ff67df18`, `23daef548` |
| `tests/models/multimodal/generation/test_nemotron_parse.py` | `ee2129182` |
| `tests/models/multimodal/processing/test_nemotron_vl.py` | `e83b7e379`, `27f4c2fd4` |
| `vllm/model_executor/models/nano_nemotron_vl.py` | `df7041633`, `dcd80206b`, `5206e5e28`, `2b8a38b6d`, `27ca95b3c`, `fda3f03eb`, `cd3ac5b79`, `9ea07b41d`, `ee2129182`, `e83b7e379`, `27f4c2fd4`, `c46b932df`, ... (19 total) |
| `vllm/model_executor/models/nemotron.py` | `df7041633`, `dcd80206b`, `cf3eacfe5`, `e10c84e06`, `39e63dec7`, `430dd4d9e`, `a8b70304d`, `97d1c9930`, `9d1c47470` |
| `vllm/model_executor/models/nemotron_h.py` | `df7041633`, `dcd80206b`, `5206e5e28`, `44f08af3a`, `aa7f37ccf`, `bf184a662`, `482914849`, `28c94770a`, `108a2728f`, `fcd5306f6`, `39e63dec7`, `1395461f5`, ... (16 total) |
| `vllm/model_executor/models/nemotron_nas.py` | `df7041633`, `dcd80206b`, `44f08af3a`, `2612ba928`, `f5db6385a`, `cf3eacfe5`, `e10c84e06`, `39e63dec7`, `430dd4d9e`, `a8b70304d`, `97d1c9930`, `9d1c47470` |
| `vllm/model_executor/models/nemotron_parse.py` | `df7041633`, `eec3546bb`, `dcd80206b`, `fda3f03eb`, `9ea07b41d`, `eb28e8068`, `2612ba928`, `ee2129182` |
| `vllm/model_executor/models/nemotron_vl.py` | `df7041633`, `dcd80206b`, `fda3f03eb`, `e83b7e379`, `27f4c2fd4`, `c46b932df`, `34a984274`, `97d1c9930` |
| `vllm/transformers_utils/configs/nemotron.py` | `e10c84e06`, `a8b70304d` |
| `vllm/transformers_utils/configs/nemotron_h.py` | `fcd5306f6` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 48
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-29 | `eec3546bb` | 模型支持/运行时入口 | [Misc][Build] Lazy load cv2 in nemotron_parse.py (#33189) | `vllm/model_executor/models/nemotron_parse.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-24 | `5206e5e28` | 性能/后端优化 | [V1][Hybrid] Mamba Prefix Caching with align mode (#30877) | `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py` |
| 2026-01-22 | `44f08af3a` | 性能/后端优化 | Add llmcompressor fp8 kv-cache quant (per-tensor and per-attn_head) (#30141) | `csrc/cache_kernels.cu`, `docs/features/quantization/quantized_kvcache.md`, `tests/kernels/attention/test_cache.py` |
| 2026-01-22 | `2b8a38b6d` | 性能/后端优化 | [Model] Extend `collect_children` and `no_init_weights` contexts (#32757) | `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py` |
| 2026-01-21 | `27ca95b3c` | 缺陷修复 | [Bugfix] Fix Nemotron-Nano-v2-vlm static resolution (#32682) | `vllm/model_executor/models/nano_nemotron_vl.py` |
| 2026-01-20 | `fda3f03eb` | 性能/后端优化 | [4/N] Initialize MM components in context managers (M-P) (#32663) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/interfaces.py` |
| 2026-01-19 | `cd3ac5b79` | 模型支持/运行时入口 | support dynamic resolution image encoding for Nemotron Nano VL (#32121) | `vllm/model_executor/models/intern_vit.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/radio.py` |
| 2026-01-19 | `aa7f37ccf` | 性能/后端优化 | Add support for LoRA adapters in Nemotron-H models (#30802) | `tests/lora/test_layers.py`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/column_parallel_linear.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-13 | `eb28e8068` | 模型支持/运行时入口 | [Refactor] Remove `get_encoder_dummy_data` (#32241) | `vllm/model_executor/models/nemotron_parse.py`, `vllm/model_executor/models/whisper.py`, `vllm/multimodal/processing.py` |
| 2026-01-10 | `583a90e00` | 模型支持/运行时入口 | [Refactor] Separate sequence and token pooling types (#32026) | `tests/model_executor/test_model_load_with_params.py`, `tests/models/language/pooling/test_embedding.py`, `tests/models/language/pooling/test_mm_classifier_conversion.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-08 | `b8112c1d8` | 性能/后端优化 | [Bugfix] Fix vllm serve failure with Nemotron Nano V3 FP8 (#31960) | `vllm/model_executor/layers/quantization/utils/fp8_utils.py` |
| 2026-01-07 | `bf184a662` | 性能/后端优化 | Enable quantized attention in NemotronH models (#31898) | `vllm/model_executor/model_loader/weight_utils.py`, `vllm/model_executor/models/nemotron_h.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `e5d427e93` | 性能/后端优化 | [ROCm][CI] Pinning timm lib version to fix ImportError in Multi-Modal Tests (Nemotron) (#31835) | `requirements/rocm-test.txt` |
| 2026-01-06 | `28c94770a` | 模型支持/运行时入口 | [NemotronH] Use ReplicatedLinear for fc1_latent_proj (#31807) | `vllm/model_executor/models/nemotron_h.py` |
| 2026-01-05 | `ee2129182` | 模型支持/运行时入口 | [Model] Nemotron Parse 1.1 Support (#30864) | `requirements/test.in`, `requirements/test.txt`, `tests/conftest.py` |
| 2026-01-05 | `911d38ed9` | 模型支持/运行时入口 | [Model] Let more models to support the score template. (#31335) | `docs/models/supported_models.md`, `examples/pooling/score/convert_model_to_seq_cls.py`, `examples/pooling/score/offline_reranker.py` |
| 2025-12-31 | `108a2728f` | 模型支持/运行时入口 | Add get_expert_mapping to NemotronHModel (for LoRA support) (#31539) | `vllm/model_executor/models/nemotron_h.py` |
| 2025-12-24 | `1ff67df18` | 模型支持/运行时入口 | [CI] Reorganization pooling_mteb_test (#31265) | `tests/entrypoints/pooling/embed/test_correctness_mteb.py`, `tests/entrypoints/pooling/score/test_correctness_mteb.py`, `tests/entrypoints/pooling/score/test_utils.py` |
| 2025-12-23 | `23daef548` | 模型支持/运行时入口 | [Frontend] Support using chat template as custom score template for reranking models (#30550) | `docs/models/supported_models.md`, `docs/serving/openai_compatible_server.md`, `examples/pooling/score/offline_using_template.py` |
| 2025-12-17 | `f5db6385a` | 缺陷修复 | Fix nemotron_nas intermediate_size computation (#30795) | `vllm/model_executor/models/nemotron_nas.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-08 | `fcd5306f6` | 性能/后端优化 | Add latent MoE support (#30203) | `vllm/model_executor/models/nemotron_h.py`, `vllm/transformers_utils/configs/nemotron_h.py` |
| 2025-12-07 | `e83b7e379` | 调度/缓存/PD | Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `27f4c2fd4` | 调度/缓存/PD | [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-05 | `6038b1b04` | 调度/缓存/PD | [Frontend][Model] Add 'float16' to possible mamba cache dtype values, override mamba SSM cache dtype value for NemotronH (#29978) | `vllm/config/cache.py`, `vllm/model_executor/models/config.py`, `vllm/utils/torch_utils.py` |
| 2025-12-04 | `e10c84e06` | 性能/后端优化 | Access `partial_rotary_factor` from `rope_parameters` (#29966) | `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/apertus.py` |
| 2025-12-05 | `b286a311c` | 调度/缓存/PD | [Chore] Deprecate `merge_by_field_config` arg (#30035) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_glm4_1v.py`, `tests/models/multimodal/processing/test_tensor_schema.py` |
| 2025-12-02 | `34a8559be` | 调度/缓存/PD | [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py` |
| 2025-12-02 | `68ffbca7e` | 调度/缓存/PD | [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py` |
| 2025-12-02 | `653591d5e` | 性能/后端优化 | [Chore] Move tokenizer initialization methods (#29793) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-29 | `39e63dec7` | 性能/后端优化 | [LoRA] Cleanup LoRA unused code (#29611) | `examples/offline_inference/multilora_inference.py`, `tests/entrypoints/conftest.py`, `tests/entrypoints/openai/test_basic.py` |
| 2025-11-28 | `fae694306` | 缺陷修复 | [Doc]: fixing typos in multiple files. (#29685) | `vllm/compilation/sequence_parallelism.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/stablelm.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-19 | `1395461f5` | 性能/后端优化 | [Hybrid][torch.compile] Refactor mamba2 forward to avoid obscuring linear projections under custom op (#28587) | `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/falcon_h1.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `9d1c47470` | 性能/后端优化 | [LoRA][1/N]Remove LoRA extra vocab (#28382) | `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py` |
| 2025-11-06 | `ffb08379d` | 通用实现调整 | [Chore] Remove Nemotron-Nano-VL config copy (#28126) | `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/nemotron_vl.py` |
| 2025-11-05 | `e50c45467` | 性能/后端优化 | [BugFix] Support EP/DP + EPLB with MTP (#25311) | `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py` |
| 2025-11-04 | `e4ee65867` | 性能/后端优化 | [Model] add optimal triton fused moe configs for NemotronH MoE (#27967) | `benchmarks/kernels/benchmark_moe.py`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=1856,device_name=NVIDIA_H100_80GB_HBM3.json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=1856,device_name=NVIDIA_L40S.json` |
| 2025-11-04 | `77f8001f5` | 缺陷修复 | [Model][Bugfix] fix pipeline parallelism support for NemotronH (#27968) | `vllm/model_executor/models/nemotron_h.py` |

## Per-Commit Audit Cards

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

### Commit `eec3546bb` - [Misc][Build] Lazy load cv2 in nemotron_parse.py (#33189)

- Full hash: `eec3546bba747a90ac174c8f262f6045ab6c840f`
- Date/author: 2026-01-29 / Kiersten Stokes
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/nemotron_parse.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/nemotron_parse.py`
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

### Commit `44f08af3a` - Add llmcompressor fp8 kv-cache quant (per-tensor and per-attn_head) (#30141)

- Full hash: `44f08af3a75edcd64e525ac619ebb3b52b99a9c5`
- Date/author: 2026-01-22 / Eldar Kurtić
- Auto category: 性能/后端优化
- Main files: `csrc/cache_kernels.cu`, `docs/features/quantization/quantized_kvcache.md`, `tests/kernels/attention/test_cache.py`, `tests/quantization/test_compressed_tensors.py`, `vllm/attention/layer.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/input_quant_fp8.py`, `vllm/model_executor/layers/quantization/utils/quant_utils.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/quantization/quantized_kvcache.md`
  - runtime-model: `vllm/model_executor/model_loader/weight_utils.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/llama.py`; `vllm/model_executor/models/llama_eagle.py`; `vllm/model_executor/models/llama_eagle3.py`; `vllm/model_executor/models/nemotron_h.py`; `vllm/model_executor/models/nemotron_nas.py`
  - runtime-perf: `csrc/cache_kernels.cu`; `vllm/attention/layer.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`; `vllm/model_executor/layers/quantization/input_quant_fp8.py`; `vllm/model_executor/layers/quantization/utils/quant_utils.py`; `vllm/v1/attention/backend.py`; `vllm/v1/attention/backends/flash_attn.py`
  - tests: `tests/kernels/attention/test_cache.py`; `tests/quantization/test_compressed_tensors.py`
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

### Commit `27ca95b3c` - [Bugfix] Fix Nemotron-Nano-v2-vlm static resolution (#32682)

- Full hash: `27ca95b3c9e6e32ac02508e729c01865800fd036`
- Date/author: 2026-01-21 / Netanel Haber
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/nano_nemotron_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/nano_nemotron_vl.py`
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

### Commit `cd3ac5b79` - support dynamic resolution image encoding for Nemotron Nano VL (#32121)

- Full hash: `cd3ac5b79703b350c7b66053dcec56300b33deb0`
- Date/author: 2026-01-19 / Netanel Haber
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/intern_vit.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/radio.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/intern_vit.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/radio.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `aa7f37ccf` - Add support for LoRA adapters in Nemotron-H models (#30802)

- Full hash: `aa7f37ccfa168d40c89d1a104a870757666fcb56`
- Date/author: 2026-01-19 / danisereb
- Auto category: 性能/后端优化
- Main files: `tests/lora/test_layers.py`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/column_parallel_linear.py`, `vllm/lora/layers/fused_moe.py`, `vllm/lora/lora_weights.py`, `vllm/lora/model_manager.py`, `vllm/lora/utils.py`, `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py` 等 10 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/lora/layers/__init__.py`; `vllm/lora/layers/column_parallel_linear.py`; `vllm/lora/lora_weights.py`; `vllm/lora/model_manager.py`; `vllm/lora/utils.py`
  - runtime-model: `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/nemotron_h.py`
  - runtime-perf: `vllm/lora/layers/fused_moe.py`; `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`
  - tests: `tests/lora/test_layers.py`
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

### Commit `eb28e8068` - [Refactor] Remove `get_encoder_dummy_data` (#32241)

- Full hash: `eb28e8068dd870283f1a4fe8251ed9254d6f477e`
- Date/author: 2026-01-13 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/nemotron_parse.py`, `vllm/model_executor/models/whisper.py`, `vllm/multimodal/processing.py`, `vllm/multimodal/profiling.py`, `vllm/multimodal/registry.py`, `vllm/v1/engine/input_processor.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/processing.py`; `vllm/multimodal/profiling.py`; `vllm/multimodal/registry.py`; `vllm/v1/engine/input_processor.py`
  - runtime-model: `vllm/model_executor/models/nemotron_parse.py`; `vllm/model_executor/models/whisper.py`
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

### Commit `b8112c1d8` - [Bugfix] Fix vllm serve failure with Nemotron Nano V3 FP8 (#31960)

- Full hash: `b8112c1d85442b060e37df90e9db343cbc7b000c`
- Date/author: 2026-01-08 / danisereb
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/utils/fp8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bf184a662` - Enable quantized attention in NemotronH models (#31898)

- Full hash: `bf184a66218beae5355c1e9784074c21b896fe0f`
- Date/author: 2026-01-07 / roikoren755
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/model_loader/weight_utils.py`, `vllm/model_executor/models/nemotron_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/model_loader/weight_utils.py`; `vllm/model_executor/models/nemotron_h.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `e5d427e93` - [ROCm][CI] Pinning timm lib version to fix ImportError in Multi-Modal Tests (Nemotron) (#31835)

- Full hash: `e5d427e93af5861e22c2b7b3ce88af0028fc41e3`
- Date/author: 2026-01-06 / Andreas Karatzas
- Auto category: 性能/后端优化
- Main files: `requirements/rocm-test.txt`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `requirements/rocm-test.txt`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `28c94770a` - [NemotronH] Use ReplicatedLinear for fc1_latent_proj (#31807)

- Full hash: `28c94770adfcb9cfbc78a3221f915bfc830c6582`
- Date/author: 2026-01-06 / roikoren755
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/nemotron_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/nemotron_h.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `ee2129182` - [Model] Nemotron Parse 1.1 Support (#30864)

- Full hash: `ee212918250ab5aa33a2968c027d71ffd6048ae4`
- Date/author: 2026-01-05 / amitz-nv
- Auto category: 模型支持/运行时入口
- Main files: `requirements/test.in`, `requirements/test.txt`, `tests/conftest.py`, `tests/models/multimodal/generation/test_nemotron_parse.py`, `tests/models/multimodal/pooling/test_radio.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/registry.py`, `vllm/assets/image.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `requirements/test.in`; `requirements/test.txt`; `vllm/assets/image.py`
  - runtime-model: `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/nemotron_parse.py`; `vllm/model_executor/models/radio.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/configs/radio.py`
  - tests: `tests/conftest.py`; `tests/models/multimodal/generation/test_nemotron_parse.py`; `tests/models/multimodal/pooling/test_radio.py`; `tests/models/multimodal/processing/test_common.py`; `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `108a2728f` - Add get_expert_mapping to NemotronHModel (for LoRA support) (#31539)

- Full hash: `108a2728f74da693c3007094063a6ee357243a5e`
- Date/author: 2025-12-31 / danisereb
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/nemotron_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/nemotron_h.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1ff67df18` - [CI] Reorganization pooling_mteb_test (#31265)

- Full hash: `1ff67df1826a2e6d2d9be684151604c46f04947d`
- Date/author: 2025-12-24 / wang.yuqi
- Auto category: 模型支持/运行时入口
- Main files: `tests/entrypoints/pooling/embed/test_correctness_mteb.py`, `tests/entrypoints/pooling/score/test_correctness_mteb.py`, `tests/entrypoints/pooling/score/test_utils.py`, `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/mteb_score_utils.py`, `tests/models/language/pooling_mteb_test/test_baai.py`, `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py`, `tests/models/language/pooling_mteb_test/test_cross_encoder.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/entrypoints/pooling/embed/test_correctness_mteb.py`; `tests/entrypoints/pooling/score/test_correctness_mteb.py`; `tests/entrypoints/pooling/score/test_utils.py`; `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`; `tests/models/language/pooling_mteb_test/mteb_score_utils.py`; `tests/models/language/pooling_mteb_test/test_baai.py`; `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py`; `tests/models/language/pooling_mteb_test/test_cross_encoder.py` 等 18 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `23daef548` - [Frontend] Support using chat template as custom score template for reranking models (#30550)

- Full hash: `23daef548dd1b33ba6ecb00c8c65e69f17102d13`
- Date/author: 2025-12-23 / Jakub Zakrzewski
- Auto category: 模型支持/运行时入口
- Main files: `docs/models/supported_models.md`, `docs/serving/openai_compatible_server.md`, `examples/pooling/score/offline_using_template.py`, `examples/pooling/score/online_using_template.py`, `examples/pooling/score/template/nemotron-rerank.jinja`, `tests/entrypoints/pooling/score/test_utils.py`, `tests/models/language/pooling_mteb_test/mteb_utils.py`, `tests/models/language/pooling_mteb_test/test_nemotron.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`; `docs/serving/openai_compatible_server.md`; `examples/pooling/score/offline_using_template.py`; `examples/pooling/score/online_using_template.py`; `examples/pooling/score/template/nemotron-rerank.jinja`
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/run_batch.py`; `vllm/entrypoints/pooling/score/serving.py`; `vllm/entrypoints/score_utils.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/llama.py` 等 9 个文件
  - tests: `tests/entrypoints/pooling/score/test_utils.py`; `tests/models/language/pooling_mteb_test/mteb_utils.py`; `tests/models/language/pooling_mteb_test/test_nemotron.py`; `tests/models/registry.py`; `tests/models/utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f5db6385a` - Fix nemotron_nas intermediate_size computation (#30795)

- Full hash: `f5db6385a19b04e76b5834618305485753e75544`
- Date/author: 2025-12-17 / Grzegorz K. Karch
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/nemotron_nas.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/nemotron_nas.py`
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

### Commit `fcd5306f6` - Add latent MoE support (#30203)

- Full hash: `fcd5306f65876f72122d7e5852b6000738498d7e`
- Date/author: 2025-12-08 / shaharmor98
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/nemotron_h.py`, `vllm/transformers_utils/configs/nemotron_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/nemotron_h.py`; `vllm/transformers_utils/configs/nemotron_h.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `6038b1b04` - [Frontend][Model] Add 'float16' to possible mamba cache dtype values, override mamba SSM cache dtype value for NemotronH (#29978)

- Full hash: `6038b1b04b7ee1b716a75591040fd3ecaa596a3d`
- Date/author: 2025-12-05 / amitz-nv
- Auto category: 调度/缓存/PD
- Main files: `vllm/config/cache.py`, `vllm/model_executor/models/config.py`, `vllm/utils/torch_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/utils/torch_utils.py`
  - runtime-model: `vllm/model_executor/models/config.py`
  - runtime-perf: `vllm/config/cache.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e10c84e06` - Access `partial_rotary_factor` from `rope_parameters` (#29966)

- Full hash: `e10c84e06af7264d5c0b3e7ec5604ada2eee7094`
- Date/author: 2025-12-04 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/falcon_h1.py`, `vllm/model_executor/models/glm.py` 等 21 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/falcon_h1.py`; `vllm/model_executor/models/glm.py`; `vllm/model_executor/models/glm4.py`; `vllm/model_executor/models/gpt_neox.py` 等 18 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/glm4_moe.py`
  - tests: `tests/kernels/core/test_mrope.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `653591d5e` - [Chore] Move tokenizer initialization methods (#29793)

- Full hash: `653591d5e73b34ffd9186c61e964474bcc4b7c80`
- Date/author: 2025-12-02 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_lora_resolvers.py`, `tests/entrypoints/openai/test_return_token_ids.py`, `tests/entrypoints/openai/test_return_tokens_as_ids.py`, `tests/entrypoints/openai/test_serving_chat.py` 等 51 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/benchmark_prefix_caching.py`; `benchmarks/benchmark_serving_structured_output.py`
  - other: `vllm/benchmarks/serve.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/__init__.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/tokenizer.py`; `vllm/v1/engine/async_llm.py`; `vllm/v1/engine/llm_engine.py`; `vllm/v1/structured_output/__init__.py`
  - runtime-model: `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/deepseek_vl2.py`; `vllm/model_executor/models/granite_speech.py`; `vllm/model_executor/models/gritlm.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/pixtral.py`; `vllm/model_executor/models/voxtral.py` 等 9 个文件
  - tests: `tests/compile/test_dynamic_shapes_compilation.py`; `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_lora_resolvers.py`; `tests/entrypoints/openai/test_return_token_ids.py`; `tests/entrypoints/openai/test_return_tokens_as_ids.py`; `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/test_token_in_token_out.py`; `tests/entrypoints/openai/test_tokenization.py` 等 32 个文件
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

### Commit `39e63dec7` - [LoRA] Cleanup LoRA unused code (#29611)

- Full hash: `39e63dec7c751a28d5a577caf16439e08a878c92`
- Date/author: 2025-11-29 / Jee Jee Li
- Auto category: 性能/后端优化
- Main files: `examples/offline_inference/multilora_inference.py`, `tests/entrypoints/conftest.py`, `tests/entrypoints/openai/test_basic.py`, `tests/entrypoints/openai/test_chat.py`, `tests/entrypoints/openai/test_chunked_prompt.py`, `tests/entrypoints/openai/test_lora_adapters.py`, `tests/entrypoints/openai/test_models.py`, `tests/entrypoints/openai/test_orca_metrics.py` 等 46 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/offline_inference/multilora_inference.py`
  - other: `vllm/lora/models.py`
  - runtime-model: `vllm/lora/worker_manager.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/exaone.py`; `vllm/model_executor/models/exaone4.py`; `vllm/model_executor/models/falcon_h1.py`; `vllm/model_executor/models/granite.py`; `vllm/model_executor/models/interfaces.py` 等 21 个文件
  - runtime-perf: `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/phimoe.py`
  - tests: `tests/entrypoints/conftest.py`; `tests/entrypoints/openai/test_basic.py`; `tests/entrypoints/openai/test_chat.py`; `tests/entrypoints/openai/test_chunked_prompt.py`; `tests/entrypoints/openai/test_lora_adapters.py`; `tests/entrypoints/openai/test_models.py`; `tests/entrypoints/openai/test_orca_metrics.py`; `tests/entrypoints/openai/test_return_tokens_as_ids.py` 等 18 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fae694306` - [Doc]: fixing typos in multiple files. (#29685)

- Full hash: `fae6943068e05fb90705ccb5c08bbd04d771048f`
- Date/author: 2025-11-28 / Didier Durand
- Auto category: 缺陷修复
- Main files: `vllm/compilation/sequence_parallelism.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/stablelm.py`, `vllm/utils/gc_utils.py`, `vllm/v1/spec_decode/ngram_proposer.py`, `vllm/v1/worker/ec_connector_model_runner_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/compilation/sequence_parallelism.py`; `vllm/utils/gc_utils.py`; `vllm/v1/spec_decode/ngram_proposer.py`
  - runtime-model: `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/stablelm.py`; `vllm/v1/worker/ec_connector_model_runner_mixin.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `430dd4d9e` - [Attention] Remove imports from `vllm/attention/__init__.py` (#29342)

- Full hash: `430dd4d9eb7e342e28012351df06d93892f86741`
- Date/author: 2025-11-26 / Matthew Bonanni
- Auto category: 性能/后端优化
- Main files: `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/kernels/utils.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_utils.py`, `vllm/attention/__init__.py`, `vllm/attention/backends/abstract.py` 等 96 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/basic.md`
  - other: `vllm/compilation/fusion_attn.py`; `vllm/compilation/qk_norm_rope_fusion.py`; `vllm/v1/kv_offload/cpu.py`; `vllm/v1/kv_offload/spec.py`
  - runtime-model: `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bloom.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/attention/__init__.py`; `vllm/attention/backends/abstract.py`; `vllm/attention/layer.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py` 等 20 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/kernels/utils.py`; `tests/v1/worker/test_gpu_model_runner.py`; `tests/v1/worker/test_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a8b70304d` - Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542)

- Full hash: `a8b70304d68497ac1c432a2ff343e9bfb516c227`
- Date/author: 2025-11-19 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/language/pooling/test_nomic_max_model_len.py` 等 104 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `examples/offline_inference/context_extension.py`
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py` 等 78 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 17 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; `tests/models/language/pooling/test_nomic_max_model_len.py`; `tests/test_config.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1395461f5` - [Hybrid][torch.compile] Refactor mamba2 forward to avoid obscuring linear projections under custom op (#28587)

- Full hash: `1395461f5fb76145433c1dc8a3b7262ee3799bf8`
- Date/author: 2025-11-19 / tomeras91
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/falcon_h1.py`, `vllm/model_executor/models/granitemoehybrid.py`, `vllm/model_executor/models/mamba2.py`, `vllm/model_executor/models/nemotron_h.py`, `vllm/model_executor/models/zamba2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/falcon_h1.py`; `vllm/model_executor/models/mamba2.py`; `vllm/model_executor/models/nemotron_h.py`; `vllm/model_executor/models/zamba2.py`
  - runtime-perf: `vllm/model_executor/models/granitemoehybrid.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `97d1c9930` - Rename clashing method names for vLLM model protocol (#27583)

- Full hash: `97d1c99302df6f7eadc0d0b32ec174db69cb4421`
- Date/author: 2025-11-13 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/baichuan.py` 等 164 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/basic.md`; `docs/contributing/model/multimodal.md`
  - other: `vllm/multimodal/processing.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/bert.py` 等 144 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 16 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9d1c47470` - [LoRA][1/N]Remove LoRA extra vocab (#28382)

- Full hash: `9d1c47470430ba31c02946aa1fd01aadf6e18b91`
- Date/author: 2025-11-12 / Jee Jee Li
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/baichuan.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/chameleon.py` 等 65 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 58 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/longcat_flash.py`; `vllm/model_executor/models/phimoe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ffb08379d` - [Chore] Remove Nemotron-Nano-VL config copy (#28126)

- Full hash: `ffb08379d8870a1a81ba82b72797f196838d0c86`
- Date/author: 2025-11-06 / Isotr0py
- Auto category: 通用实现调整
- Main files: `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/nemotron_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/nemotron_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `e50c45467` - [BugFix] Support EP/DP + EPLB with MTP (#25311)

- Full hash: `e50c45467215f96068d95736b08d8a25f624e67d`
- Date/author: 2025-11-05 / Ilya Markov
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py`, `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/ernie45_moe.py` 等 27 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - other: `vllm/v1/spec_decode/medusa.py`
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`; `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llama4.py`; `vllm/model_executor/models/llama4_eagle.py` 等 17 个文件
  - runtime-perf: `vllm/distributed/eplb/eplb_state.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/qwen3_moe.py`; `vllm/model_executor/models/transformers/moe.py`
  - tests: `tests/distributed/test_eplb_spec_decode.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e4ee65867` - [Model] add optimal triton fused moe configs for NemotronH MoE (#27967)

- Full hash: `e4ee6586721cd9e09ac50207cb5e754d7a4a773e`
- Date/author: 2025-11-04 / tomeras91
- Auto category: 性能/后端优化
- Main files: `benchmarks/kernels/benchmark_moe.py`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=1856,device_name=NVIDIA_H100_80GB_HBM3.json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=1856,device_name=NVIDIA_L40S.json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=928,device_name=NVIDIA_H100_80GB_HBM3.json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=928,device_name=NVIDIA_L40S.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/kernels/benchmark_moe.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=1856,device_name=NVIDIA_H100_80GB_HBM3.json`; `vllm/model_executor/layers/fused_moe/configs/E=128,N=1856,device_name=NVIDIA_L40S.json`; `vllm/model_executor/layers/fused_moe/configs/E=128,N=928,device_name=NVIDIA_H100_80GB_HBM3.json`; `vllm/model_executor/layers/fused_moe/configs/E=128,N=928,device_name=NVIDIA_L40S.json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `77f8001f5` - [Model][Bugfix] fix pipeline parallelism support for NemotronH (#27968)

- Full hash: `77f8001f533021ece46779f5b7e69edc1d3b514f`
- Date/author: 2025-11-04 / tomeras91
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/nemotron_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/nemotron_h.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
