# vllm ERNIE 4.5 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `tests/reasoning/test_ernie45_reasoning_parser.py` | `d9ab1ad9d` |
| `tests/tool_parsers/test_ernie45_moe_tool_parser.py` | `fefce4980`, `ed586e772` |
| `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py` | `ad8c07313`, `3bd9c4915` |
| `vllm/model_executor/models/ernie45.py` | `40b69e33e` |
| `vllm/model_executor/models/ernie45_moe.py` | `df7041633`, `dcd80206b`, `327a02d8d`, `482914849`, `cf3eacfe5`, `430dd4d9e`, `a8b70304d`, `97d1c9930`, `e50c45467` |
| `vllm/model_executor/models/ernie45_vl.py` | `df7041633`, `dcd80206b`, `9ad7f89f5`, `e1a34c3a5`, `9ea07b41d`, `2612ba928`, `2972a0547`, `0790f0769`, `2d6001f49`, `ad8c07313`, `3bd9c4915`, `87b4d1557`, ... (21 total) |
| `vllm/model_executor/models/ernie45_vl_moe.py` | `df7041633`, `dcd80206b`, `327a02d8d`, `482914849`, `430dd4d9e`, `a8b70304d`, `97d1c9930` |
| `vllm/model_executor/models/ernie_mtp.py` | `df7041633`, `dcd80206b`, `600aaab8d`, `97d1c9930` |
| `vllm/reasoning/ernie45_reasoning_parser.py` | `fefce4980`, `d9ab1ad9d`, `e261d37c9`, `43a6acfb7` |
| `vllm/tool_parsers/ernie45_tool_parser.py` | `fefce4980`, `2a1776b7a` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 39
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-24 | `9ad7f89f5` | 性能/后端优化 | [Models]: Make Multimodal config implicit in ViT implementation (#31972) | `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py` |
| 2026-01-20 | `e1a34c3a5` | 模型支持/运行时入口 | [2/N] Initialize MM components in context managers (E-H) (#32641) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/cohere2_vision.py` |
| 2026-01-18 | `327a02d8d` | 性能/后端优化 | [MoE Refactor] Separate Router into OO Classes (#30623) | `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-12 | `600aaab8d` | 性能/后端优化 | [Model] Remove incorrect `SupportsPP` from MTP models (#32150) | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-08 | `2972a0547` | 模型支持/运行时入口 | [MM Encoder]: Make MMEncoderAttention's `scale` takes effect properly (#31950) | `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py` |
| 2026-01-07 | `0790f0769` | 性能/后端优化 | [Misc] Improve error messages for unsupported types and parameters (#30593) | `benchmarks/cutlass_benchmarks/sparse_benchmarks.py`, `vllm/attention/ops/chunked_prefill_paged_decode.py`, `vllm/config/lora.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2025-12-25 | `2d6001f49` | 模型支持/运行时入口 | [Model][Ernie4.5-VL] Support video metadata for timestamp rendering (#31274) | `tests/models/multimodal/processing/test_common.py`, `vllm/model_executor/models/ernie45_vl.py` |
| 2025-12-16 | `ad8c07313` | 性能/后端优化 | [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873) | `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py` |
| 2025-12-16 | `3bd9c4915` | 性能/后端优化 | [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873) | `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py` |
| 2025-12-15 | `ed586e772` | 性能/后端优化 | [Refactor] [3/N] Move tool parser tests and run on CPU (#30693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-15 | `87b4d1557` | 性能/后端优化 | [CustomOp][MM] Extract MMEncoderAttention as CustomOp and replace the backend of QwenVisionAttention with it. (#30125) | `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `vllm/attention/layer.py`, `vllm/attention/layers/mm_encoder_attention.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-08 | `bcb6f5947` | 性能/后端优化 | [Perf] Remove sync point in vit torch sdpa attn backend (#30232) | `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-02 | `653591d5e` | 性能/后端优化 | [Chore] Move tokenizer initialization methods (#29793) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py` |
| 2025-11-29 | `fa59fe417` | 性能/后端优化 | [Chore] Move `detokenizer_utils` to `vllm/tokenizers` (#29727) | `tests/tool_use/test_ernie45_moe_tool_parser.py`, `tests/tool_use/test_jamba_tool_parser.py`, `tests/tool_use/test_qwen3coder_tool_parser.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-28 | `460d8bbf2` | 性能/后端优化 | Remove upstream fa checks (#29471) | `vllm/attention/layer.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/attention/utils/fa_utils.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-23 | `0ff70821c` | 性能/后端优化 | [Core] Deprecate `xformers` (#29262) | `docker/Dockerfile.nightly_torch`, `docs/contributing/ci/update_pytorch_version.md`, `docs/getting_started/quickstart.md` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-11 | `afffd3cc8` | 性能/后端优化 | [Model] Pass `mm_features` directly into `get_mrope_input_positions` (#28399) | `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py` |
| 2025-11-11 | `b30dfa03c` | 性能/后端优化 | [Attention] Refactor CUDA attention backend selection logic (#24794) | `.buildkite/test-pipeline.yaml`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_fusions_e2e.py` |
| 2025-11-11 | `d0e186c16` | 性能/后端优化 | [V0 Deprecation] Remove unused `context_len` and `seq_len` from M-RoPE (#28395) | `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py` |
| 2025-11-10 | `912744d06` | 性能/后端优化 | [Fix] optimize visual token mask with caching and multi-token support (#28374) | `vllm/model_executor/models/ernie45_vl.py` |
| 2025-11-08 | `d9ab1ad9d` | 性能/后端优化 | `reasoning_content` -> `reasoning` (#27752) | `docs/features/reasoning_outputs.md`, `docs/features/structured_outputs.md`, `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py` |
| 2025-11-05 | `e50c45467` | 性能/后端优化 | [BugFix] Support EP/DP + EPLB with MTP (#25311) | `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py` |
| 2025-11-05 | `e261d37c9` | 性能/后端优化 | [Refactor] Lazy-loaded reasoning_parser (#28092) | `docs/features/reasoning_outputs.md`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `vllm/engine/arg_utils.py` |
| 2025-11-04 | `43a6acfb7` | 缺陷修复 | [Model] fix ernie45 reasoning_parser (#27973) | `vllm/reasoning/ernie45_reasoning_parser.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |
| 2025-11-03 | `40b69e33e` | 模型支持/运行时入口 | [Model] Add PaddleOCR-VL Model Support (#27758) | `docs/models/supported_models.md`, `examples/offline_inference/vision_language.py`, `examples/offline_inference/vision_language_multi_image.py` |

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

### Commit `e1a34c3a5` - [2/N] Initialize MM components in context managers (E-H) (#32641)

- Full hash: `e1a34c3a5d9273431ee182253750d39b546d37a1`
- Date/author: 2026-01-20 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/cohere2_vision.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/fuyu.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/gemma3n_mm.py`, `vllm/model_executor/models/glm4_1v.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/cohere2_vision.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/fuyu.py`; `vllm/model_executor/models/gemma3_mm.py`; `vllm/model_executor/models/gemma3n_mm.py`; `vllm/model_executor/models/glm4_1v.py` 等 12 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `327a02d8d` - [MoE Refactor] Separate Router into OO Classes (#30623)

- Full hash: `327a02d8db86e57f2488779b0c1b133da5f03fb5`
- Date/author: 2026-01-18 / bnellnm
- Auto category: 性能/后端优化
- Main files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py`, `tests/kernels/moe/test_cutlass_moe.py`, `tests/kernels/moe/test_flashinfer_moe.py`, `tests/kernels/moe/test_grouped_topk.py`, `tests/kernels/moe/test_moe.py`, `tests/kernels/moe/test_moe_permute_unpermute.py` 等 45 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/distributed/eplb/eplb_state.py`; `vllm/model_executor/layers/fused_moe/__init__.py`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`; `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/router/__init__.py` 等 32 个文件
  - tests: `tests/kernels/moe/modular_kernel_tools/common.py`; `tests/kernels/moe/test_batched_moe.py`; `tests/kernels/moe/test_block_fp8.py`; `tests/kernels/moe/test_cutlass_moe.py`; `tests/kernels/moe/test_flashinfer_moe.py`; `tests/kernels/moe/test_grouped_topk.py`; `tests/kernels/moe/test_moe.py`; `tests/kernels/moe/test_moe_permute_unpermute.py` 等 13 个文件
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

### Commit `0790f0769` - [Misc] Improve error messages for unsupported types and parameters (#30593)

- Full hash: `0790f07695c72fe203e95f6d8c8ff15c8003e754`
- Date/author: 2026-01-07 / BlankR
- Auto category: 性能/后端优化
- Main files: `benchmarks/cutlass_benchmarks/sparse_benchmarks.py`, `vllm/attention/ops/chunked_prefill_paged_decode.py`, `vllm/config/lora.py`, `vllm/distributed/device_communicators/pynccl_wrapper.py`, `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/vllm_v1_adapter.py`, `vllm/model_executor/layers/quantization/auto_round.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`, `vllm/model_executor/layers/quantization/mxfp4.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/cutlass_benchmarks/sparse_benchmarks.py`
  - runtime-model: `vllm/config/lora.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/granite_speech.py`; `vllm/model_executor/models/minimax_text_01.py`
  - runtime-perf: `vllm/attention/ops/chunked_prefill_paged_decode.py`; `vllm/distributed/device_communicators/pynccl_wrapper.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/vllm_v1_adapter.py`; `vllm/model_executor/layers/quantization/auto_round.py`; `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`; `vllm/model_executor/layers/quantization/mxfp4.py`
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

### Commit `2d6001f49` - [Model][Ernie4.5-VL] Support video metadata for timestamp rendering (#31274)

- Full hash: `2d6001f491bc29223dd3f8150688daeaded275ee`
- Date/author: 2025-12-25 / SongHe
- Auto category: 模型支持/运行时入口
- Main files: `tests/models/multimodal/processing/test_common.py`, `vllm/model_executor/models/ernie45_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`
  - tests: `tests/models/multimodal/processing/test_common.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `ed586e772` - [Refactor] [3/N] Move tool parser tests and run on CPU (#30693)

- Full hash: `ed586e7724fdf91b391abcf6f3e473be641ff5d6`
- Date/author: 2025-12-15 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/tool_use.yaml`, `tests/tool_parsers/__init__.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_ernie45_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py` 等 16 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/misc.yaml`; `.buildkite/test_areas/tool_use.yaml`
  - tests: `tests/tool_parsers/__init__.py`; `tests/tool_parsers/test_deepseekv31_tool_parser.py`; `tests/tool_parsers/test_ernie45_moe_tool_parser.py`; `tests/tool_parsers/test_glm4_moe_tool_parser.py`; `tests/tool_parsers/test_jamba_tool_parser.py`; `tests/tool_parsers/test_kimi_k2_tool_parser.py`; `tests/tool_parsers/test_minimax_tool_parser.py`; `tests/tool_parsers/test_mistral_tool_parser.py` 等 12 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `2a1776b7a` - [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675)

- Full hash: `2a1776b7ac4fae7c50c694edeafc1b14270e4350`
- Date/author: 2025-12-15 / Chauncey
- Auto category: 性能/后端优化
- Main files: `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_hunyuan_a13b_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py` 等 61 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/tool_calling.md`
  - other: `vllm/tool_parsers/__init__.py`; `vllm/tool_parsers/abstract_tool_parser.py`; `vllm/tool_parsers/deepseekv31_tool_parser.py`; `vllm/tool_parsers/deepseekv32_tool_parser.py`; `vllm/tool_parsers/deepseekv3_tool_parser.py`; `vllm/tool_parsers/ernie45_tool_parser.py`; `vllm/tool_parsers/gigachat3_tool_parser.py`; `vllm/tool_parsers/granite_20b_fc_tool_parser.py` 等 30 个文件
  - runtime-model: `vllm/entrypoints/context.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/parser/responses_parser.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_engine.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_hunyuan_a13b_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_pythonic_tool_parser.py` 等 22 个文件
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

### Commit `fa59fe417` - [Chore] Move `detokenizer_utils` to `vllm/tokenizers` (#29727)

- Full hash: `fa59fe417f509641fed102dfa2e3b8a63f224241`
- Date/author: 2025-11-29 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `tests/tool_use/test_ernie45_moe_tool_parser.py`, `tests/tool_use/test_jamba_tool_parser.py`, `tests/tool_use/test_qwen3coder_tool_parser.py`, `tests/tool_use/test_seed_oss_tool_parser.py`, `tests/tool_use/test_xlam_tool_parser.py`, `tests/utils_/test_argparse_utils.py`, `vllm/tokenizers/detokenizer_utils.py`, `vllm/v1/engine/detokenizer.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tokenizers/detokenizer_utils.py`; `vllm/v1/engine/detokenizer.py`; `vllm/v1/engine/logprobs.py`
  - tests: `tests/tool_use/test_ernie45_moe_tool_parser.py`; `tests/tool_use/test_jamba_tool_parser.py`; `tests/tool_use/test_qwen3coder_tool_parser.py`; `tests/tool_use/test_seed_oss_tool_parser.py`; `tests/tool_use/test_xlam_tool_parser.py`; `tests/utils_/test_argparse_utils.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `0ff70821c` - [Core] Deprecate `xformers` (#29262)

- Full hash: `0ff70821c9b0b991197fa7f3264bf9dd78b8d4b3`
- Date/author: 2025-11-23 / Roger Wang
- Auto category: 性能/后端优化
- Main files: `docker/Dockerfile.nightly_torch`, `docs/contributing/ci/update_pytorch_version.md`, `docs/getting_started/quickstart.md`, `examples/online_serving/openai_embedding_long_text/service.sh`, `requirements/cuda.txt`, `tests/basic_correctness/test_basic_correctness.py`, `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_attention_selector.py` 等 31 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/ci/update_pytorch_version.md`; `docs/getting_started/quickstart.md`; `examples/online_serving/openai_embedding_long_text/service.sh`
  - other: `docker/Dockerfile.nightly_torch`; `vllm/envs.py`; `vllm/utils/__init__.py`
  - runtime-model: `vllm/config/multimodal.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/pixtral.py`; `vllm/model_executor/models/qwen2_5_vl.py` 等 10 个文件
  - runtime-perf: `requirements/cuda.txt`; `vllm/attention/backends/registry.py`; `vllm/attention/layer.py`; `vllm/attention/ops/vit_attn_wrappers.py`; `vllm/attention/selector.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/platforms/cuda.py`; `vllm/v1/attention/backends/xformers.py`
  - tests: `tests/basic_correctness/test_basic_correctness.py`; `tests/kernels/attention/test_attention.py`; `tests/kernels/attention/test_attention_selector.py`; `tests/kernels/attention/test_mha_attn.py`; `tests/kernels/utils.py`; `tests/lora/test_minicpmv_tp.py`; `tests/lora/test_qwen2vl.py`
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

### Commit `afffd3cc8` - [Model] Pass `mm_features` directly into `get_mrope_input_positions` (#28399)

- Full hash: `afffd3cc8a99ce1cf0f6f1687852e5519d725a3b`
- Date/author: 2025-11-11 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/keye_vl1_5.py`, `vllm/model_executor/models/paddleocr_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/inputs.py`
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/keye_vl1_5.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 13 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b30dfa03c` - [Attention] Refactor CUDA attention backend selection logic (#24794)

- Full hash: `b30dfa03c564ce51c56bf2dd16283f074253c27c`
- Date/author: 2025-11-11 / Matthew Bonanni
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_fusions_e2e.py`, `tests/config/test_multimodal_config.py`, `tests/kernels/attention/test_attention_selector.py`, `tests/kernels/attention/test_mha_attn.py`, `tests/models/test_initialization.py`, `tests/v1/attention/test_attention_backends.py` 等 61 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - other: `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/tpu.py`; `vllm/platforms/xpu.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/ovis2_5.py`; `vllm/model_executor/models/paddleocr_vl.py` 等 14 个文件
  - runtime-perf: `vllm/attention/backends/abstract.py`; `vllm/attention/backends/registry.py`; `vllm/attention/layer.py`; `vllm/attention/selector.py`; `vllm/config/cache.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/platforms/cuda.py` 等 26 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_fusions_e2e.py`; `tests/config/test_multimodal_config.py`; `tests/kernels/attention/test_attention_selector.py`; `tests/kernels/attention/test_mha_attn.py`; `tests/models/test_initialization.py`; `tests/v1/attention/test_attention_backends.py`; `tests/v1/attention/test_mla_backends.py` 等 13 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d0e186c16` - [V0 Deprecation] Remove unused `context_len` and `seq_len` from M-RoPE (#28395)

- Full hash: `d0e186c16f0d62af8c128e2dc7c94cde1387ac02`
- Date/author: 2025-11-11 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/keye_vl1_5.py`, `vllm/model_executor/models/paddleocr_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/keye_vl1_5.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 12 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `912744d06` - [Fix] optimize visual token mask with caching and multi-token support (#28374)

- Full hash: `912744d0668405f2e70f5d1de785ad513abf7b13`
- Date/author: 2025-11-10 / Ferrebo
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/ernie45_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d9ab1ad9d` - `reasoning_content` -> `reasoning` (#27752)

- Full hash: `d9ab1ad9d1be96885f4387a33a3a82233c009ce9`
- Date/author: 2025-11-08 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `docs/features/reasoning_outputs.md`, `docs/features/structured_outputs.md`, `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py`, `examples/online_serving/openai_chat_completion_with_reasoning.py`, `examples/online_serving/openai_chat_completion_with_reasoning_streaming.py`, `examples/online_serving/streamlit_openai_chatbot_webserver.py`, `examples/online_serving/structured_outputs/structured_outputs.py`, `tests/entrypoints/openai/test_chat_with_tool_reasoning.py` 等 46 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/reasoning_outputs.md`; `docs/features/structured_outputs.md`; `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py`; `examples/online_serving/openai_chat_completion_with_reasoning.py`; `examples/online_serving/openai_chat_completion_with_reasoning_streaming.py`; `examples/online_serving/streamlit_openai_chatbot_webserver.py`; `examples/online_serving/structured_outputs/structured_outputs.py`
  - other: `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/basic_parsers.py`; `vllm/reasoning/deepseek_r1_reasoning_parser.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/ernie45_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/granite_reasoning_parser.py`; `vllm/reasoning/hunyuan_a13b_reasoning_parser.py` 等 15 个文件
  - runtime-model: `vllm/entrypoints/harmony_utils.py`; `vllm/entrypoints/openai/protocol.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_responses.py`; `vllm/entrypoints/openai/tool_parsers/qwen3xml_tool_parser.py`
  - runtime-perf: `vllm/reasoning/glm4_moe_reasoning_parser.py`
  - tests: `tests/entrypoints/openai/test_chat_with_tool_reasoning.py`; `tests/entrypoints/openai/test_completion_with_function_calling.py`; `tests/entrypoints/openai/test_run_batch.py`; `tests/reasoning/test_base_thinking_reasoning_parser.py`; `tests/reasoning/test_deepseekr1_reasoning_parser.py`; `tests/reasoning/test_deepseekv3_reasoning_parser.py`; `tests/reasoning/test_ernie45_reasoning_parser.py`; `tests/reasoning/test_glm4_moe_reasoning_parser.py` 等 18 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `e261d37c9` - [Refactor] Lazy-loaded reasoning_parser (#28092)

- Full hash: `e261d37c9a5e88a6c86d32decf39f1fab7ca1f2c`
- Date/author: 2025-11-05 / Chauncey
- Auto category: 性能/后端优化
- Main files: `docs/features/reasoning_outputs.md`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `vllm/engine/arg_utils.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/openai/run_batch.py`, `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/reasoning/__init__.py`, `vllm/reasoning/abs_reasoning_parsers.py` 等 21 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/reasoning_outputs.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/reasoning/__init__.py`; `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/deepseek_r1_reasoning_parser.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/ernie45_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/granite_reasoning_parser.py` 等 15 个文件
  - runtime-model: `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/run_batch.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`
  - runtime-perf: `vllm/reasoning/glm4_moe_reasoning_parser.py`
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `43a6acfb7` - [Model] fix ernie45 reasoning_parser (#27973)

- Full hash: `43a6acfb7de8c7ad839d41bc2109fafe692b77ba`
- Date/author: 2025-11-04 / CSWYF3634076
- Auto category: 缺陷修复
- Main files: `vllm/reasoning/ernie45_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/ernie45_reasoning_parser.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `c02fccdbd` - [Refactor] Lazy import tool_parser (#27974)

- Full hash: `c02fccdbd2794fe016ebd738e3a8b8c8d78eb78c`
- Date/author: 2025-11-04 / Chauncey
- Auto category: 性能/后端优化
- Main files: `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py`, `tests/tool_use/test_glm4_moe_tool_parser.py`, `tests/tool_use/test_jamba_tool_parser.py`, `tests/tool_use/test_kimi_k2_tool_parser.py`, `tests/tool_use/test_minimax_tool_parser.py`, `tests/tool_use/test_openai_tool_parser.py` 等 40 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/tool_calling.md`
  - runtime-model: `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`; `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/deepseekv31_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/deepseekv3_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/ernie45_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/granite_20b_fc_tool_parser.py` 等 29 个文件
  - runtime-perf: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/tool_use/test_deepseekv31_tool_parser.py`; `tests/tool_use/test_ernie45_moe_tool_parser.py`; `tests/tool_use/test_glm4_moe_tool_parser.py`; `tests/tool_use/test_jamba_tool_parser.py`; `tests/tool_use/test_kimi_k2_tool_parser.py`; `tests/tool_use/test_minimax_tool_parser.py`; `tests/tool_use/test_openai_tool_parser.py`; `tests/tool_use/test_seed_oss_tool_parser.py` 等 9 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `40b69e33e` - [Model] Add PaddleOCR-VL Model Support  (#27758)

- Full hash: `40b69e33e796efdc75e774a1c38cc73397ea6e17`
- Date/author: 2025-11-03 / zhang-prog
- Auto category: 模型支持/运行时入口
- Main files: `docs/models/supported_models.md`, `examples/offline_inference/vision_language.py`, `examples/offline_inference/vision_language_multi_image.py`, `tests/models/registry.py`, `vllm/model_executor/models/ernie45.py`, `vllm/model_executor/models/paddleocr_vl.py`, `vllm/model_executor/models/registry.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`; `examples/offline_inference/vision_language.py`; `examples/offline_inference/vision_language_multi_image.py`
  - runtime-model: `vllm/model_executor/models/ernie45.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/registry.py`
  - tests: `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
