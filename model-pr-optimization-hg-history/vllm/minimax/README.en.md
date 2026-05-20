# vllm MiniMax M2 Series Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `examples/tool_chat_template_minimax_m1.jinja` | no direct commit |
| `tests/models/multimodal/processing/test_minimax_vl_01.py` | `e83b7e379`, `27f4c2fd4` |
| `tests/reasoning/test_minimax_m2_append_reasoning_parser.py` | `6299628d3` |
| `tests/reasoning/test_minimax_m2_reasoning_parser.py` | `6299628d3` |
| `tests/tool_parsers/test_minimax_tool_parser.py` | `fefce4980`, `ed586e772` |
| `tests/tool_use/test_minimax_m2_tool_parser.py` | `20fda4315` |
| `vllm/model_executor/models/minimax_m2.py` | `89a8f88b2`, `df7041633`, `7d98f09b1`, `dcd80206b`, `bc0d291bf`, `63227accf`, `482914849`, `5bc664110`, `cf3eacfe5`, `d017bceb0`, `430dd4d9e`, `a8b70304d`, ... (15 total) |
| `vllm/model_executor/models/minimax_text_01.py` | `df7041633`, `dcd80206b`, `5206e5e28`, `2612ba928`, `0790f0769`, `cf3eacfe5`, `430dd4d9e`, `a8b70304d`, `97d1c9930`, `9d1c47470` |
| `vllm/model_executor/models/minimax_vl_01.py` | `df7041633`, `dcd80206b`, `9ad7f89f5`, `fda3f03eb`, `5576227bc`, `c46b932df`, `97d1c9930` |
| `vllm/reasoning/minimax_m2_reasoning_parser.py` | `7ef587375`, `9312a6c03`, `fefce4980`, `6299628d3`, `34a984274`, `7636d4366`, `d9ab1ad9d`, `e261d37c9` |
| `vllm/tool_parsers/minimax_m2_tool_parser.py` | `19b251fe3`, `fefce4980`, `c02a2705f`, `20fda4315`, `2a1776b7a` |
| `vllm/tool_parsers/minimax_tool_parser.py` | `fefce4980`, `2a1776b7a` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 43
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-28 | `89a8f88b2` | 性能/后端优化 | feat: Support rms+quant fusion in minimax_m2 series model. | `vllm/model_executor/models/minimax_m2.py` |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-03 | `7d98f09b1` | 性能/后端优化 | cherry pick | `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-24 | `bc0d291bf` | 缺陷修复 | feat: Complete LoRA support for MiniMaxM2 Fixes #32736 (#32763) | `docs/models/supported_models.md`, `vllm/model_executor/models/minimax_m2.py` |
| 2026-01-24 | `9ad7f89f5` | 性能/后端优化 | [Models]: Make Multimodal config implicit in ViT implementation (#31972) | `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py` |
| 2026-01-24 | `5206e5e28` | 性能/后端优化 | [V1][Hybrid] Mamba Prefix Caching with align mode (#30877) | `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py` |
| 2026-01-22 | `7ef587375` | 性能/后端优化 | [CI] Fix mypy for `vllm/v1/structured_output` (#32722) | `tools/pre_commit/mypy.py`, `vllm/reasoning/abs_reasoning_parsers.py`, `vllm/reasoning/basic_parsers.py` |
| 2026-01-21 | `63227accf` | 性能/后端优化 | [Kernel] Add topk_sigmoid kernel (#31246) | `benchmarks/kernels/benchmark_fused_topk.py`, `csrc/moe/moe_ops.h`, `csrc/moe/topk_softmax_kernels.cu` |
| 2026-01-20 | `fda3f03eb` | 性能/后端优化 | [4/N] Initialize MM components in context managers (M-P) (#32663) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/interfaces.py` |
| 2026-01-14 | `19b251fe3` | 性能/后端优化 | Fix optional parameter parsing in MiniMax M2 tool parser #32278 (#32342) | `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2026-01-14 | `9312a6c03` | 模型支持/运行时入口 | [Refactor] [8/N] to simplify the vLLM openai responsesapi_serving architecture (#32260) | `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_protocol.py`, `tests/entrypoints/openai/test_serving_responses.py` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-08 | `5576227bc` | 模型支持/运行时入口 | [Model] Standardize common vision encoders (#31947) | `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/deepseek_ocr.py` |
| 2026-01-07 | `0790f0769` | 性能/后端优化 | [Misc] Improve error messages for unsupported types and parameters (#30593) | `benchmarks/cutlass_benchmarks/sparse_benchmarks.py`, `vllm/attention/ops/chunked_prefill_paged_decode.py`, `vllm/config/lora.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2025-12-30 | `5bc664110` | 性能/后端优化 | Optimize QKNorm for MiniMax-M2/M2.1 (#31493) | `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/models/minimax_m2.py` |
| 2025-12-22 | `c02a2705f` | 调度/缓存/PD | Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs (#31083) | `docs/models/supported_models.md`, `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2025-12-17 | `20fda4315` | 缺陷修复 | [Bugfix][Frontend] Prevent IndexError in MiniMax M2 tool parser during streaming extraction (#30555) | `tests/tool_use/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py` |
| 2025-12-15 | `ed586e772` | 性能/后端优化 | [Refactor] [3/N] Move tool parser tests and run on CPU (#30693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-11 | `6299628d3` | 缺陷修复 | [bugfix] fix MiniMaxM2ReasoningParser streaming output not separating reasoning_content. (#29882) | `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`, `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py` |
| 2025-12-10 | `d017bceb0` | 缺陷修复 | [BugFix] Fix minimax m2 model rotary_dim (#30384) | `vllm/model_executor/models/minimax_m2.py` |
| 2025-12-07 | `e83b7e379` | 调度/缓存/PD | Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `27f4c2fd4` | 调度/缓存/PD | [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-02 | `653591d5e` | 性能/后端优化 | [Chore] Move tokenizer initialization methods (#29793) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-17 | `f4776ec3d` | 通用实现调整 | Merge branch 'minimax_m2' into 'v0.11.0-dev' |  |
| 2025-11-17 | `7636d4366` | 模型支持/运行时入口 | Add minimax_m2 | `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py`, `vllm/model_executor/models/minimax_m2.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `9d1c47470` | 性能/后端优化 | [LoRA][1/N]Remove LoRA extra vocab (#28382) | `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py` |
| 2025-11-08 | `d9ab1ad9d` | 性能/后端优化 | `reasoning_content` -> `reasoning` (#27752) | `docs/features/reasoning_outputs.md`, `docs/features/structured_outputs.md`, `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py` |
| 2025-11-06 | `0370679ce` | 性能/后端优化 | [Kernel][Model] Tune fused_moe Triton configs for MiniMax-M2 on H100 (#28200) | `vllm/model_executor/layers/fused_moe/configs/E=256,N=384,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json` |
| 2025-11-05 | `b57789b62` | 缺陷修复 | Fix excessive logging noise by reducing the log level of the MinimaxM2ToolParser import success message (#27635) | `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py` |
| 2025-11-05 | `e261d37c9` | 性能/后端优化 | [Refactor] Lazy-loaded reasoning_parser (#28092) | `docs/features/reasoning_outputs.md`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `vllm/engine/arg_utils.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |
| 2025-10-31 | `5e8862e9e` | 调度/缓存/PD | [Feature] Pydantic validation for scheduler.py and structured_outputs.py (#26519) | `vllm/config/scheduler.py`, `vllm/config/structured_outputs.py`, `vllm/engine/arg_utils.py` |
| 2025-10-29 | `d6704dd09` | 缺陷修复 | Fix MiniMax-M2 rmsnorm precision and remove useless code (#27627) | `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/models/minimax_m2.py` |

## Per-Commit Audit Cards

### Commit `89a8f88b2` - feat: Support rms+quant fusion in minimax_m2 series model.

- Full hash: `89a8f88b22d490f8ccbbe18344a3d28c1d419a6d`
- Date/author: 2026-03-28 / wanglong3
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `7d98f09b1` - cherry pick

- Full hash: `7d98f09b1cc06ba485d8c79e1f2f5b0062e2e2f6`
- Date/author: 2026-02-03 / Michael Goin
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/minimax_m2.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`; `vllm/model_executor/layers/fused_moe/oracle/fp8.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/fp8.py`
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

### Commit `bc0d291bf` - feat: Complete LoRA support for MiniMaxM2 Fixes #32736 (#32763)

- Full hash: `bc0d291bfebf0979dbd6e8486de40aa95eb57490`
- Date/author: 2026-01-24 / david guan
- Auto category: 缺陷修复
- Main files: `docs/models/supported_models.md`, `vllm/model_executor/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`
  - runtime-model: `vllm/model_executor/models/minimax_m2.py`
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

### Commit `7ef587375` - [CI] Fix mypy for `vllm/v1/structured_output` (#32722)

- Full hash: `7ef587375280b475719c37463ca37f2ceb38e54e`
- Date/author: 2026-01-22 / Wentao Ye
- Auto category: 性能/后端优化
- Main files: `tools/pre_commit/mypy.py`, `vllm/reasoning/abs_reasoning_parsers.py`, `vllm/reasoning/basic_parsers.py`, `vllm/reasoning/deepseek_v3_reasoning_parser.py`, `vllm/reasoning/gptoss_reasoning_parser.py`, `vllm/reasoning/holo2_reasoning_parser.py`, `vllm/reasoning/hunyuan_a13b_reasoning_parser.py`, `vllm/reasoning/identity_reasoning_parser.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `tools/pre_commit/mypy.py`; `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/basic_parsers.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/holo2_reasoning_parser.py`; `vllm/reasoning/hunyuan_a13b_reasoning_parser.py`; `vllm/reasoning/identity_reasoning_parser.py` 等 15 个文件
  - runtime-perf: `vllm/v1/attention/backends/fa_utils.py`; `vllm/v1/attention/backends/mla/aiter_triton_mla.py`; `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `63227accf` - [Kernel] Add topk_sigmoid kernel (#31246)

- Full hash: `63227accf5af941215e5a7fd48c305a15e2c8814`
- Date/author: 2026-01-21 / Xin Yang
- Auto category: 性能/后端优化
- Main files: `benchmarks/kernels/benchmark_fused_topk.py`, `csrc/moe/moe_ops.h`, `csrc/moe/topk_softmax_kernels.cu`, `csrc/moe/torch_bindings.cpp`, `tests/kernels/moe/test_fused_topk.py`, `tests/model_executor/test_enabled_custom_ops.py`, `vllm/_aiter_ops.py`, `vllm/_custom_ops.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/kernels/benchmark_fused_topk.py`
  - other: `vllm/_aiter_ops.py`; `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/models/minimax_m2.py`
  - runtime-perf: `csrc/moe/moe_ops.h`; `csrc/moe/topk_softmax_kernels.cu`; `csrc/moe/torch_bindings.cpp`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`; `vllm/model_executor/layers/fused_moe/router/fused_topk_router.py`; `vllm/model_executor/layers/fused_moe/router/router_factory.py`
  - tests: `tests/kernels/moe/test_fused_topk.py`; `tests/model_executor/test_enabled_custom_ops.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `19b251fe3` - Fix optional parameter parsing in MiniMax M2 tool parser #32278 (#32342)

- Full hash: `19b251fe3d26ec9c8df6cb633af9dd196cc6ae18`
- Date/author: 2026-01-14 / baonudesifeizhai
- Auto category: 性能/后端优化
- Main files: `vllm/tool_parsers/minimax_m2_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tool_parsers/minimax_m2_tool_parser.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

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

### Commit `5576227bc` - [Model] Standardize common vision encoders (#31947)

- Full hash: `5576227bc132996d9e4ca279a8a8cf9e7b8a8ca4`
- Date/author: 2026-01-08 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/hyperclovax_vision.py`, `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/lightonocr.py`, `vllm/model_executor/models/llava.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/hyperclovax_vision.py`; `vllm/model_executor/models/isaac.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/lightonocr.py`; `vllm/model_executor/models/llava.py` 等 19 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `5bc664110` - Optimize QKNorm for MiniMax-M2/M2.1 (#31493)

- Full hash: `5bc664110f120adf789560b2ecfdb19a1cc72ee0`
- Date/author: 2025-12-30 / Roger Young
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c02a2705f` - Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs (#31083)

- Full hash: `c02a2705f9ceeb00b5d32453621f997b2ceafbea`
- Date/author: 2025-12-22 / Roger Young
- Auto category: 调度/缓存/PD
- Main files: `docs/models/supported_models.md`, `vllm/tool_parsers/minimax_m2_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/tool_parsers/minimax_m2_tool_parser.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `20fda4315` - [Bugfix][Frontend] Prevent IndexError in MiniMax M2 tool parser during streaming extraction (#30555)

- Full hash: `20fda431515d19a883cc962d3a1fa727f225e82d`
- Date/author: 2025-12-17 / Robin
- Auto category: 缺陷修复
- Main files: `tests/tool_use/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tool_parsers/minimax_m2_tool_parser.py`
  - tests: `tests/tool_use/test_minimax_m2_tool_parser.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `6299628d3` - [bugfix] fix MiniMaxM2ReasoningParser streaming output not separating reasoning_content. (#29882)

- Full hash: `6299628d326f429eba78736acb44e76749b281f5`
- Date/author: 2025-12-11 / Rei.
- Auto category: 缺陷修复
- Main files: `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`, `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/minimax_m2_reasoning_parser.py`
  - tests: `tests/reasoning/test_minimax_m2_append_reasoning_parser.py`; `tests/reasoning/test_minimax_m2_reasoning_parser.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `d017bceb0` - [BugFix] Fix minimax m2 model rotary_dim (#30384)

- Full hash: `d017bceb08eaac7bae2c499124ece737fb4fb22b`
- Date/author: 2025-12-10 / Roger Young
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/minimax_m2.py`
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

### Commit `f4776ec3d` - Merge branch 'minimax_m2' into 'v0.11.0-dev'

- Full hash: `f4776ec3dbd4fd3b3dc10ffffaf5b3df09bce232`
- Date/author: 2025-11-17 / zhuwenwen
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `7636d4366` - Add minimax_m2

- Full hash: `7636d4366cad7c0d6ac9baaefe70edae0a2272f7`
- Date/author: 2025-11-17 / chenych1
- Auto category: 模型支持/运行时入口
- Main files: `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py`, `vllm/model_executor/models/minimax_m2.py`, `vllm/model_executor/models/registry.py`, `vllm/reasoning/__init__.py`, `vllm/reasoning/minimax_m2_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/__init__.py`; `vllm/reasoning/minimax_m2_reasoning_parser.py`
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/__init__.py`; `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py`; `vllm/model_executor/models/minimax_m2.py`; `vllm/model_executor/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `0370679ce` - [Kernel][Model] Tune fused_moe Triton configs for MiniMax-M2 on H100 (#28200)

- Full hash: `0370679ce9fc5245953002e387ee9a86ea562b97`
- Date/author: 2025-11-06 / Eric Yue
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=384,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=256,N=384,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b57789b62` - Fix excessive logging noise by reducing the log level of the MinimaxM2ToolParser import success message (#27635)

- Full hash: `b57789b62b1f7451b0df099ebc9ac6358510cabb`
- Date/author: 2025-11-05 / Eric Yue
- Auto category: 缺陷修复
- Main files: `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `5e8862e9e` - [Feature] Pydantic validation for scheduler.py and structured_outputs.py (#26519)

- Full hash: `5e8862e9e0f5c81d81a1ee46248cc281edc42596`
- Date/author: 2025-10-31 / Vinay R Damodaran
- Auto category: 调度/缓存/PD
- Main files: `vllm/config/scheduler.py`, `vllm/config/structured_outputs.py`, `vllm/engine/arg_utils.py`, `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/engine/arg_utils.py`
  - runtime-model: `vllm/config/structured_outputs.py`; `vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py`
  - runtime-perf: `vllm/config/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d6704dd09` - Fix MiniMax-M2 rmsnorm precision and remove useless code (#27627)

- Full hash: `d6704dd099b71a9881613dee74b440d78594fa8f`
- Date/author: 2025-10-29 / Roger Young
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
