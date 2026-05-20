# vllm Mistral Small 4 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `examples/offline_inference/mistral-small.py` | no direct commit |
| `examples/tool_chat_template_mistral.jinja` | no direct commit |
| `examples/tool_chat_template_mistral3.jinja` | no direct commit |
| `examples/tool_chat_template_mistral_parallel.jinja` | no direct commit |
| `tests/models/fixtures/mistral_small_3_chat.json` | no direct commit |
| `tests/models/language/generation/test_mistral.py` | `2a1776b7a`, `64251f48d`, `6a6108511`, `1b1e35aaf`, `34a984274`, `57430fc95` |
| `tests/reasoning/test_mistral_reasoning_parser.py` | `64251f48d`, `aa3c250c4`, `34a984274`, `d9ab1ad9d` |
| `tests/renderers/test_mistral.py` | `d117a4d1a` |
| `tests/tokenizers_/test_mistral.py` | `d8c6210ee`, `2afcec4de`, `34a984274` |
| `tests/tool_parsers/test_mistral_tool_parser.py` | `fefce4980`, `38c361f99`, `ed586e772` |
| `tests/tool_use/mistral/__init__.py` | no direct commit |
| `tests/tool_use/mistral/conftest.py` | no direct commit |
| `tests/tool_use/mistral/test_mistral_tool_calls.py` | no direct commit |
| `tests/tool_use/mistral/utils.py` | no direct commit |
| `vllm/model_executor/models/mistral.py` | `df7041633`, `d56afd45f`, `3f3f89529`, `1579c9b5f` |
| `vllm/model_executor/models/mistral3.py` | `df7041633`, `dcd80206b`, `9ad7f89f5`, `4753f3bf6`, `2f03035a6`, `9ea07b41d`, `5576227bc`, `c46b932df`, `97d1c9930` |
| `vllm/model_executor/models/mistral_large_3.py` | `d8c6210ee` |
| `vllm/model_executor/models/mistral_large_3_eagle.py` | `5708297e4`, `979f50efd`, `d8c6210ee` |
| `vllm/reasoning/mistral_reasoning_parser.py` | `7ef587375`, `9312a6c03`, `fefce4980`, `8c084de59`, `64251f48d`, `aa3c250c4`, `34a984274`, `e261d37c9` |
| `vllm/renderers/mistral.py` | `d117a4d1a` |
| `vllm/tokenizers/mistral.py` | `fefce4980`, `644482487`, `48e744976`, `39cefbdf1`, `40a046cd8`, `6fc5841db`, `d8c6210ee`, `f0a28bf66`, `2afcec4de`, `34a984274` |
| `vllm/tool_parsers/mistral_tool_parser.py` | `fefce4980`, `38c361f99`, `2a1776b7a` |
| `vllm/transformers_utils/configs/mistral.py` | `3f3f89529`, `3faa8bee5`, `d8c6210ee`, `d1cf8214e`, `57430fc95`, `434f3d3eb`, `a8b70304d`, `7a8375f8a` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 56
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-05 | `899a2db47` | 性能/后端优化 | sync v0.15.1(ex fused_moe&models) | `vllm/_custom_ops.py`, `vllm/compilation/decorators.py`, `vllm/config/compilation.py` |
| 2026-01-26 | `d56afd45f` | 模型支持/运行时入口 | Remove unused logic in `models/mistral.py` (#33095) | `vllm/model_executor/models/mistral.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-24 | `9ad7f89f5` | 性能/后端优化 | [Models]: Make Multimodal config implicit in ViT implementation (#31972) | `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py` |
| 2026-01-23 | `3f3f89529` | 模型支持/运行时入口 | [Voxtral] Add new streaming arch (#32861) | `tests/models/multimodal/generation/test_voxtral_streaming.py`, `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/mistral.py` |
| 2026-01-22 | `7ef587375` | 性能/后端优化 | [CI] Fix mypy for `vllm/v1/structured_output` (#32722) | `tools/pre_commit/mypy.py`, `vllm/reasoning/abs_reasoning_parsers.py`, `vllm/reasoning/basic_parsers.py` |
| 2026-01-22 | `d117a4d1a` | 模型支持/运行时入口 | [Frontend] Introduce Renderer for processing chat messages (using `ModelConfig`) (#30200) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2026-01-22 | `1579c9b5f` | 模型支持/运行时入口 | [Llama.py -> mistral.py] Extract mistral-only relevant code into separate file (#32780) | `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/mistral.py`, `vllm/model_executor/models/registry.py` |
| 2026-01-21 | `f23fb5a7c` | 缺陷修复 | [Bugfix] Support HF sharded weights for Mistral3/Pixtral models (#32673) | `vllm/model_executor/models/pixtral.py` |
| 2026-01-20 | `4753f3bf6` | 性能/后端优化 | [Model] Use context managers for encoder- and LM-only mode (#32605) | `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/config/multimodal.py` |
| 2026-01-18 | `2f03035a6` | 性能/后端优化 | "refactor: refactor_repeated_interfaces" (#32486) | `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/pplx_prepare_finalize.py`, `vllm/model_executor/layers/quantization/fp_quant.py` |
| 2026-01-16 | `037a6487a` | 模型支持/运行时入口 | apply _validate_input to MistralTokenizer token-id chat prompts (#32448) | `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/engine/serving.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-14 | `9312a6c03` | 模型支持/运行时入口 | [Refactor] [8/N] to simplify the vLLM openai responsesapi_serving architecture (#32260) | `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_protocol.py`, `tests/entrypoints/openai/test_serving_responses.py` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-08 | `5576227bc` | 模型支持/运行时入口 | [Model] Standardize common vision encoders (#31947) | `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/deepseek_ocr.py` |
| 2026-01-07 | `309a8f66e` | 缺陷修复 | [Bugfix] Handle mistral tokenizer in get_hf_processor (#31817) | `vllm/multimodal/processing.py` |
| 2026-01-06 | `644482487` | 模型支持/运行时入口 | [Misc] Implement `TokenizerLike.convert_tokens_to_ids` (#31796) | `vllm/tokenizers/deepseek_v32.py`, `vllm/tokenizers/mistral.py`, `vllm/tokenizers/protocol.py` |
| 2026-01-06 | `5708297e4` | 性能/后端优化 | [Misc][Model][Refactor] Pass the prefix into Linear layers (#31669) | `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/gpt_neox.py` |
| 2025-12-26 | `48e744976` | 模型支持/运行时入口 | [Mistral common] Ensure all functions are imported from the top & only use public methods (#31138) | `requirements/common.txt`, `requirements/nightly_torch_test.txt`, `requirements/test.in` |
| 2025-12-23 | `38c361f99` | 缺陷修复 | Fix edge case Mistral tool parser (#30724) | `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py` |
| 2025-12-23 | `3faa8bee5` | 模型支持/运行时入口 | adapt voxtral (#31095) | `tests/models/multimodal/generation/test_voxtral.py`, `tests/models/registry.py`, `vllm/config/model.py` |
| 2025-12-21 | `8c084de59` | 缺陷修复 | [Misc] Fix spelling typos in comments (#31114) | `.buildkite/scripts/generate-nightly-index.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `vllm/reasoning/mistral_reasoning_parser.py` |
| 2025-12-15 | `ed586e772` | 性能/后端优化 | [Refactor] [3/N] Move tool parser tests and run on CPU (#30693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-13 | `39cefbdf1` | 调度/缓存/PD | [Refactor] `TokenizerRegistry` only uses lazy imports (#30609) | `tests/test_inputs.py`, `tests/tokenizers_/test_basic.py`, `tests/tokenizers_/test_registry.py` |
| 2025-12-13 | `e5db3e277` | 缺陷修复 | [CI/Build] Fix broken mm processor test Mistral-3-large (#30597) | `tests/models/multimodal/processing/test_tensor_schema.py` |
| 2025-12-13 | `64251f48d` | 模型支持/运行时入口 | [Chore] Adjust tokenizer import to avoid circular imports (#30601) | `benchmarks/backend_request_func.py`, `tests/entrypoints/openai/test_serving_engine.py`, `tests/entrypoints/test_chat_utils.py` |
| 2025-12-11 | `aa3c250c4` | 模型支持/运行时入口 | [IMPROVEMENT] Change MistralReasoningParser behavior (#30391) | `tests/reasoning/test_mistral_reasoning_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py` |
| 2025-12-11 | `979f50efd` | 模型支持/运行时入口 | [Deprecation] Remove fallbacks for `embed_input_ids` and `embed_multimodal` (#30458) | `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/interfaces_base.py`, `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2025-12-09 | `5c213d289` | 缺陷修复 | [BUGFIX] Mistral tool call parser v11+ (#30332) | `tests/tool_use/test_mistral_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-05 | `40a046cd8` | 缺陷修复 | [Bugfix]: Fix `TokenizerLike` interface (#30009) | `vllm/benchmarks/datasets.py`, `vllm/benchmarks/serve.py`, `vllm/benchmarks/throughput.py` |
| 2025-12-03 | `dd5d1ef78` | 缺陷修复 | [Bugfix] Mistral tool parser streaming update (#19425) | `requirements/common.txt`, `tests/tool_use/test_mistral_tool_parser.py`, `tests/tool_use/utils.py` |
| 2025-12-02 | `6a6108511` | 缺陷修复 | [BUGFIX] Fix regex pattern for Mistral Tool Call (#29918) | `tests/models/language/generation/test_mistral.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py` |
| 2025-12-02 | `1b1e35aaf` | 缺陷修复 | [BUGFIX] Fix regex pattern for Mistral Tool Call (#29918) | `tests/models/language/generation/test_mistral.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py` |
| 2025-12-02 | `6fc5841db` | 缺陷修复 | Fix some more Transformers nightly tests (#29872) | `examples/offline_inference/vision_language.py`, `examples/offline_inference/vision_language_multi_image.py`, `tests/models/registry.py` |
| 2025-12-02 | `d8c6210ee` | 性能/后端优化 | Add Mistral Large 3 and Ministral 3 (#29757) | `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/tokenizers_/test_mistral.py` |
| 2025-12-01 | `f0a28bf66` | 模型支持/运行时入口 | [Misc] Unify tokenizer registration (#29767) | `tests/entrypoints/openai/test_tokenization.py`, `tests/entrypoints/pooling/embed/test_online.py`, `tests/entrypoints/pooling/pooling/test_online.py` |
| 2025-11-30 | `2afcec4de` | 调度/缓存/PD | [Misc] Update `TokenizerLike` interface and move `get_cached_tokenizer` (#29730) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `docs/design/huggingface_integration.md` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-28 | `fecae12cd` | 调度/缓存/PD | Remove `all_special_tokens_extended` from tokenizer code (#29686) | `tests/tokenization/test_cached_tokenizer.py`, `tests/tokenization/test_mistral_tokenizer.py`, `tests/tokenization/test_tokenizer_registry.py` |
| 2025-11-28 | `b2c1d294f` | 缺陷修复 | [BUGFIX] MistralTokenizer._call__ adds an invalid EOS token (#29607) | `tests/tokenization/test_mistral_tokenizer.py`, `vllm/transformers_utils/tokenizers/mistral.py` |
| 2025-11-23 | `d1cf8214e` | 缺陷修复 | [Bugfix] Use HF config fields as fallback when loading Mistral config (#29239) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `vllm/transformers_utils/config.py` |
| 2025-11-21 | `57430fc95` | 性能/后端优化 | Default model load/config/tokenizer to `mistral` format if relevant files exist (#28659) | `docs/features/tool_calling.md`, `tests/models/language/generation/test_mistral.py`, `tests/models/multimodal/test_mapping.py` |
| 2025-11-21 | `434f3d3eb` | 缺陷修复 | Fix mistral config (#29172) | `vllm/transformers_utils/configs/mistral.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-14 | `085424808` | 性能/后端优化 | Remove audio optional dependency for mistral-common (#28722) | `docs/contributing/model/transcription.md`, `docs/models/supported_models.md`, `examples/offline_inference/audio_language.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-08 | `d9ab1ad9d` | 性能/后端优化 | `reasoning_content` -> `reasoning` (#27752) | `docs/features/reasoning_outputs.md`, `docs/features/structured_outputs.md`, `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py` |
| 2025-11-06 | `7a8375f8a` | 模型支持/运行时入口 | Add llama 4 scaling support (#28145) | `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`, `vllm/model_executor/models/llama.py` |
| 2025-11-06 | `a404e2c0f` | 模型支持/运行时入口 | Patch Mistral Tokenizer (#28146) | `tests/tokenization/test_mistral_tokenizer.py`, `vllm/transformers_utils/tokenizers/mistral.py` |
| 2025-11-05 | `e261d37c9` | 性能/后端优化 | [Refactor] Lazy-loaded reasoning_parser (#28092) | `docs/features/reasoning_outputs.md`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `vllm/engine/arg_utils.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |
| 2025-11-02 | `73444b7b5` | 性能/后端优化 | Performance fix MistralTokenizer: cache special ids and tokens (#27925) | `vllm/transformers_utils/tokenizers/mistral.py` |

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

### Commit `899a2db47` - sync v0.15.1(ex fused_moe&models)

- Full hash: `899a2db4715963a4dfde80e69d71a57cf0c97f28`
- Date/author: 2026-02-05 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/_custom_ops.py`, `vllm/compilation/decorators.py`, `vllm/config/compilation.py`, `vllm/config/speculative.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/distributed/device_communicators/base_device_communicator.py`, `vllm/distributed/device_communicators/cpu_communicator.py`, `vllm/distributed/device_communicators/cuda_communicator.py` 等 72 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/_custom_ops.py`; `vllm/compilation/decorators.py`; `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/logging_utils/__init__.py`; `vllm/logging_utils/access_log_filter.py`; `vllm/plugins/lora_resolvers/filesystem_resolver.py` 等 15 个文件
  - runtime-model: `vllm/config/compilation.py`; `vllm/config/speculative.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/completion/serving.py`; `vllm/entrypoints/openai/engine/protocol.py` 等 29 个文件
  - runtime-perf: `vllm/distributed/device_communicators/all2all.py`; `vllm/distributed/device_communicators/base_device_communicator.py`; `vllm/distributed/device_communicators/cpu_communicator.py`; `vllm/distributed/device_communicators/cuda_communicator.py`; `vllm/distributed/device_communicators/mnnvl_compat.py`; `vllm/distributed/device_communicators/xpu_communicator.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/distributed/parallel_state.py` 等 28 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d56afd45f` - Remove unused logic in `models/mistral.py` (#33095)

- Full hash: `d56afd45fd4efee581129c401613be356b95350d`
- Date/author: 2026-01-26 / Andy Lo
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/mistral.py`
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

### Commit `3f3f89529` - [Voxtral] Add new streaming arch (#32861)

- Full hash: `3f3f89529dc3fbaa5bf22c86d9f0833b49dc76ea`
- Date/author: 2026-01-23 / Patrick von Platen
- Auto category: 模型支持/运行时入口
- Main files: `tests/models/multimodal/generation/test_voxtral_streaming.py`, `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/mistral.py`, `vllm/model_executor/models/voxtral.py`, `vllm/model_executor/models/voxtral_streaming.py`, `vllm/model_executor/models/whisper.py`, `vllm/model_executor/models/whisper_causal.py`, `vllm/model_executor/models/whisper_utils.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/llama.py`; `vllm/model_executor/models/mistral.py`; `vllm/model_executor/models/voxtral.py`; `vllm/model_executor/models/voxtral_streaming.py`; `vllm/model_executor/models/whisper.py`; `vllm/model_executor/models/whisper_causal.py`; `vllm/model_executor/models/whisper_utils.py`; `vllm/transformers_utils/configs/mistral.py`
  - tests: `tests/models/multimodal/generation/test_voxtral_streaming.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `d117a4d1a` - [Frontend] Introduce Renderer for processing chat messages (using `ModelConfig`) (#30200)

- Full hash: `d117a4d1a915c7acf124563f9b337de5c0aa2c2f`
- Date/author: 2026-01-22 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml`, `docs/features/reasoning_outputs.md`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/test_serving_engine.py`, `tests/entrypoints/openai/test_serving_models.py` 等 48 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/misc.yaml`
  - docs-bench: `docs/features/reasoning_outputs.md`
  - other: `tools/pre_commit/mypy.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/renderers/__init__.py`; `vllm/renderers/deepseek_v32.py`; `vllm/renderers/grok2.py`; `vllm/renderers/hf.py`; `vllm/renderers/mistral.py` 等 14 个文件
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/completion/serving.py`; `vllm/entrypoints/openai/engine/serving.py`; `vllm/entrypoints/openai/models/serving.py`; `vllm/entrypoints/openai/responses/context.py` 等 17 个文件
  - tests: `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/test_serving_engine.py`; `tests/entrypoints/openai/test_serving_models.py`; `tests/entrypoints/openai/test_serving_responses.py`; `tests/entrypoints/pooling/score/test_utils.py`; `tests/entrypoints/test_chat_utils.py`; `tests/renderers/__init__.py` 等 13 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1579c9b5f` - [Llama.py -> mistral.py] Extract mistral-only relevant code into separate file (#32780)

- Full hash: `1579c9b5fd0f6f213be3bbc55c88b1d215245ed6`
- Date/author: 2026-01-22 / Patrick von Platen
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/mistral.py`, `vllm/model_executor/models/registry.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/llama.py`; `vllm/model_executor/models/mistral.py`; `vllm/model_executor/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f23fb5a7c` - [Bugfix] Support HF sharded weights for Mistral3/Pixtral models (#32673)

- Full hash: `f23fb5a7c1b61350c5c40ca1115d3bf8cf2b8cc9`
- Date/author: 2026-01-21 / RickyChen / 陳昭儒
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/pixtral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/pixtral.py`
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

### Commit `2f03035a6` - "refactor: refactor_repeated_interfaces" (#32486)

- Full hash: `2f03035a618f03c412b8a540606c7b1816839390`
- Date/author: 2026-01-18 / tjp_zju
- Auto category: 性能/后端优化
- Main files: `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/pplx_prepare_finalize.py`, `vllm/model_executor/layers/quantization/fp_quant.py`, `vllm/model_executor/layers/quantization/qutlass_utils.py`, `vllm/model_executor/model_loader/bitsandbytes_loader.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/llava.py`, `vllm/model_executor/models/mistral3.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/_custom_ops.py`
  - runtime-model: `vllm/model_executor/model_loader/bitsandbytes_loader.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/llava.py`; `vllm/model_executor/models/mistral3.py`; `vllm/model_executor/models/tarsier.py`; `vllm/model_executor/models/utils.py`; `vllm/model_executor/warmup/deep_gemm_warmup.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/pplx_prepare_finalize.py`; `vllm/model_executor/layers/quantization/fp_quant.py`; `vllm/model_executor/layers/quantization/qutlass_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `037a6487a` - apply _validate_input to MistralTokenizer token-id chat prompts (#32448)

- Full hash: `037a6487af3429bb3f3e1adfe3e2f5e5e95aa420`
- Date/author: 2026-01-16 / vanshil shah
- Auto category: 模型支持/运行时入口
- Main files: `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/engine/serving.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/entrypoints/openai/engine/serving.py`
  - tests: `tests/entrypoints/openai/test_serving_chat.py`
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

### Commit `5576227bc` - [Model] Standardize common vision encoders (#31947)

- Full hash: `5576227bc132996d9e4ca279a8a8cf9e7b8a8ca4`
- Date/author: 2026-01-08 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/hyperclovax_vision.py`, `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/lightonocr.py`, `vllm/model_executor/models/llava.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/hyperclovax_vision.py`; `vllm/model_executor/models/isaac.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/lightonocr.py`; `vllm/model_executor/models/llava.py` 等 19 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `309a8f66e` - [Bugfix] Handle mistral tokenizer in get_hf_processor (#31817)

- Full hash: `309a8f66ee0daec7dbee5030dac1bcfcfad7b3ec`
- Date/author: 2026-01-07 / Cyrus Leung
- Auto category: 缺陷修复
- Main files: `vllm/multimodal/processing.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/multimodal/processing.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `644482487` - [Misc] Implement `TokenizerLike.convert_tokens_to_ids` (#31796)

- Full hash: `6444824873711eeeb68ded97cad79394bd051ed1`
- Date/author: 2026-01-06 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/tokenizers/deepseek_v32.py`, `vllm/tokenizers/mistral.py`, `vllm/tokenizers/protocol.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tokenizers/deepseek_v32.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/protocol.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

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

### Commit `48e744976` - [Mistral common] Ensure all functions are imported from the top & only use public methods (#31138)

- Full hash: `48e744976cf4deb889998ff82813efdf34c21589`
- Date/author: 2025-12-26 / Patrick von Platen
- Auto category: 模型支持/运行时入口
- Main files: `requirements/common.txt`, `requirements/nightly_torch_test.txt`, `requirements/test.in`, `requirements/test.txt`, `vllm/tokenizers/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `requirements/common.txt`; `requirements/nightly_torch_test.txt`; `requirements/test.in`; `requirements/test.txt`; `vllm/tokenizers/mistral.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `38c361f99` - Fix edge case Mistral tool parser (#30724)

- Full hash: `38c361f99dffcf2b83725e81a1b5ed949eef43ab`
- Date/author: 2025-12-23 / Joachim Studnia
- Auto category: 缺陷修复
- Main files: `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tool_parsers/mistral_tool_parser.py`
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `3faa8bee5` - adapt voxtral (#31095)

- Full hash: `3faa8bee57982d08cae5adf733f92e27708f15ce`
- Date/author: 2025-12-23 / Patrick von Platen
- Auto category: 模型支持/运行时入口
- Main files: `tests/models/multimodal/generation/test_voxtral.py`, `tests/models/registry.py`, `vllm/config/model.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/registry.py`, `vllm/model_executor/models/voxtral.py`, `vllm/model_executor/models/voxtral_streaming.py`, `vllm/model_executor/models/whisper.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/registry.py`; `vllm/model_executor/models/voxtral.py`; `vllm/model_executor/models/voxtral_streaming.py`; `vllm/model_executor/models/whisper.py`; `vllm/model_executor/models/whisper_utils.py`; `vllm/transformers_utils/configs/mistral.py` 等 9 个文件
  - runtime-perf: `vllm/v1/attention/backends/utils.py`
  - tests: `tests/models/multimodal/generation/test_voxtral.py`; `tests/models/registry.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8c084de59` - [Misc] Fix spelling typos in comments (#31114)

- Full hash: `8c084de59d45a511aebe4005f49d9a81abceff3e`
- Date/author: 2025-12-21 / Kevin McKay
- Auto category: 缺陷修复
- Main files: `.buildkite/scripts/generate-nightly-index.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `vllm/reasoning/mistral_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/generate-nightly-index.py`
  - other: `vllm/reasoning/mistral_reasoning_parser.py`
  - tests: `tests/models/multimodal/processing/test_tensor_schema.py`
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

### Commit `39cefbdf1` - [Refactor] `TokenizerRegistry` only uses lazy imports (#30609)

- Full hash: `39cefbdf17e2e906e0eae3e82bd601f66137deb4`
- Date/author: 2025-12-13 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `tests/test_inputs.py`, `tests/tokenizers_/test_basic.py`, `tests/tokenizers_/test_registry.py`, `vllm/entrypoints/chat_utils.py`, `vllm/tokenizers/__init__.py`, `vllm/tokenizers/deepseekv32.py`, `vllm/tokenizers/hf.py`, `vllm/tokenizers/mistral.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/tokenizers/__init__.py`; `vllm/tokenizers/deepseekv32.py`; `vllm/tokenizers/hf.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/protocol.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/tokenizer.py`; `vllm/v1/engine/async_llm.py` 等 10 个文件
  - runtime-model: `vllm/entrypoints/chat_utils.py`
  - tests: `tests/test_inputs.py`; `tests/tokenizers_/test_basic.py`; `tests/tokenizers_/test_registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `e5db3e277` - [CI/Build] Fix broken mm processor test Mistral-3-large (#30597)

- Full hash: `e5db3e2774fd16394f8a96a608263ff2416385c8`
- Date/author: 2025-12-13 / Isotr0py
- Auto category: 缺陷修复
- Main files: `tests/models/multimodal/processing/test_tensor_schema.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_tensor_schema.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `64251f48d` - [Chore] Adjust tokenizer import to avoid circular imports (#30601)

- Full hash: `64251f48df0ed16fb67f12ece26ab6c7ea730e74`
- Date/author: 2025-12-13 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `benchmarks/backend_request_func.py`, `tests/entrypoints/openai/test_serving_engine.py`, `tests/entrypoints/test_chat_utils.py`, `tests/models/language/generation/test_mistral.py`, `tests/models/multimodal/generation/test_voxtral.py`, `tests/models/multimodal/processing/test_common.py`, `tests/reasoning/test_mistral_reasoning_parser.py`, `tests/reasoning/utils.py` 等 23 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/backend_request_func.py`
  - other: `vllm/reasoning/mistral_reasoning_parser.py`; `vllm/v1/engine/input_processor.py`; `vllm/v1/structured_output/backend_xgrammar.py`
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/serving_engine.py`; `vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/jamba_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`; `vllm/entrypoints/pooling/score/serving.py`; `vllm/entrypoints/utils.py` 等 10 个文件
  - tests: `tests/entrypoints/openai/test_serving_engine.py`; `tests/entrypoints/test_chat_utils.py`; `tests/models/language/generation/test_mistral.py`; `tests/models/multimodal/generation/test_voxtral.py`; `tests/models/multimodal/processing/test_common.py`; `tests/reasoning/test_mistral_reasoning_parser.py`; `tests/reasoning/utils.py`; `tests/tokenizers_/test_detokenize.py` 等 9 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `aa3c250c4` - [IMPROVEMENT] Change MistralReasoningParser behavior (#30391)

- Full hash: `aa3c250c487e843b229a58d9978b02707b71109c`
- Date/author: 2025-12-11 / Julien Denize
- Auto category: 模型支持/运行时入口
- Main files: `tests/reasoning/test_mistral_reasoning_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/reasoning/mistral_reasoning_parser.py`
  - tests: `tests/reasoning/test_mistral_reasoning_parser.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `979f50efd` - [Deprecation] Remove fallbacks for `embed_input_ids` and `embed_multimodal` (#30458)

- Full hash: `979f50efd04552654eca57c7e71e38160a7cbb5c`
- Date/author: 2025-12-11 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/interfaces_base.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`, `vllm/model_executor/models/phi3v.py`, `vllm/model_executor/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/interfaces_base.py`; `vllm/model_executor/models/mistral_large_3_eagle.py`; `vllm/model_executor/models/phi3v.py`; `vllm/model_executor/models/qwen3_vl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `5c213d289` - [BUGFIX] Mistral tool call parser v11+ (#30332)

- Full hash: `5c213d2899f5a2d439c8d771a0abc156a5412a2b`
- Date/author: 2025-12-09 / Julien Denize
- Auto category: 缺陷修复
- Main files: `tests/tool_use/test_mistral_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
  - tests: `tests/tool_use/test_mistral_tool_parser.py`
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

### Commit `40a046cd8` - [Bugfix]: Fix `TokenizerLike` interface (#30009)

- Full hash: `40a046cd82af87e65d3be9db8bd27a4be65f1b00`
- Date/author: 2025-12-05 / Rohan Potdar
- Auto category: 缺陷修复
- Main files: `vllm/benchmarks/datasets.py`, `vllm/benchmarks/serve.py`, `vllm/benchmarks/throughput.py`, `vllm/config/model.py`, `vllm/tokenizers/deepseekv32.py`, `vllm/tokenizers/mistral.py`, `vllm/tokenizers/protocol.py`, `vllm/tokenizers/registry.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/benchmarks/datasets.py`; `vllm/benchmarks/serve.py`; `vllm/benchmarks/throughput.py`; `vllm/tokenizers/deepseekv32.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/protocol.py`; `vllm/tokenizers/registry.py`
  - runtime-model: `vllm/config/model.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `dd5d1ef78` - [Bugfix] Mistral tool parser streaming update (#19425)

- Full hash: `dd5d1ef780b5b73b9817e5dc8fe9b3e98a399e20`
- Date/author: 2025-12-03 / avigny
- Auto category: 缺陷修复
- Main files: `requirements/common.txt`, `tests/tool_use/test_mistral_tool_parser.py`, `tests/tool_use/utils.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `requirements/common.txt`
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
  - tests: `tests/tool_use/test_mistral_tool_parser.py`; `tests/tool_use/utils.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `6a6108511` - [BUGFIX] Fix regex pattern for Mistral Tool Call (#29918)

- Full hash: `6a6108511f251c2b8278a84e4266504c55e1f037`
- Date/author: 2025-12-02 / Julien Denize
- Auto category: 缺陷修复
- Main files: `tests/models/language/generation/test_mistral.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
  - tests: `tests/models/language/generation/test_mistral.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1b1e35aaf` - [BUGFIX] Fix regex pattern for Mistral Tool Call (#29918)

- Full hash: `1b1e35aaf9d9561e1b5bf5b8e08b03565188e537`
- Date/author: 2025-12-02 / Julien Denize
- Auto category: 缺陷修复
- Main files: `tests/models/language/generation/test_mistral.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`
  - tests: `tests/models/language/generation/test_mistral.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `d8c6210ee` - Add Mistral Large 3 and Ministral 3 (#29757)

- Full hash: `d8c6210eeaa7f3b474e50cf74926f77a8dc79adf`
- Date/author: 2025-12-02 / Julien Denize
- Auto category: 性能/后端优化
- Main files: `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/tokenizers_/test_mistral.py`, `vllm/config/speculative.py`, `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8.json`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py` 等 16 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/tokenizers/mistral.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/speculative.py`; `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`; `vllm/model_executor/layers/mla.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/mistral_large_3.py`; `vllm/model_executor/models/mistral_large_3_eagle.py`; `vllm/model_executor/models/registry.py` 等 10 个文件
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8.json`
  - tests: `tests/models/registry.py`; `tests/tokenizers_/test_mistral.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f0a28bf66` - [Misc] Unify tokenizer registration (#29767)

- Full hash: `f0a28bf6610602a4f064ac59e1449f5acdf04c7a`
- Date/author: 2025-12-01 / Cyrus Leung
- Auto category: 模型支持/运行时入口
- Main files: `tests/entrypoints/openai/test_tokenization.py`, `tests/entrypoints/pooling/embed/test_online.py`, `tests/entrypoints/pooling/pooling/test_online.py`, `tests/models/registry.py`, `tests/tokenizers_/test_registry.py`, `tests/v1/entrypoints/llm/test_struct_output_generate.py`, `vllm/config/model.py`, `vllm/engine/arg_utils.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/engine/arg_utils.py`; `vllm/tokenizers/__init__.py`; `vllm/tokenizers/hf.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/tokenizer.py`
  - runtime-model: `vllm/config/model.py`; `vllm/entrypoints/llm.py`
  - tests: `tests/entrypoints/openai/test_tokenization.py`; `tests/entrypoints/pooling/embed/test_online.py`; `tests/entrypoints/pooling/pooling/test_online.py`; `tests/models/registry.py`; `tests/tokenizers_/test_registry.py`; `tests/v1/entrypoints/llm/test_struct_output_generate.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `2afcec4de` - [Misc] Update `TokenizerLike` interface and move `get_cached_tokenizer` (#29730)

- Full hash: `2afcec4decbbd64cf8da20d49281f828dd136c27`
- Date/author: 2025-11-30 / Cyrus Leung
- Auto category: 调度/缓存/PD
- Main files: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `docs/design/huggingface_integration.md`, `tests/tokenizers_/test_hf.py`, `tests/tokenizers_/test_mistral.py`, `tests/tokenizers_/test_registry.py`, `tools/pre_commit/check_pickle_imports.py`, `vllm/entrypoints/llm.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`
  - docs-bench: `docs/design/huggingface_integration.md`
  - other: `tools/pre_commit/check_pickle_imports.py`; `vllm/tokenizers/__init__.py`; `vllm/tokenizers/hf.py`; `vllm/tokenizers/mistral.py`; `vllm/tokenizers/protocol.py`; `vllm/transformers_utils/tokenizer.py`; `vllm/v1/engine/detokenizer.py`
  - runtime-model: `vllm/entrypoints/llm.py`; `vllm/entrypoints/score_utils.py`
  - tests: `tests/tokenizers_/test_hf.py`; `tests/tokenizers_/test_mistral.py`; `tests/tokenizers_/test_registry.py`
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

### Commit `fecae12cd` - Remove `all_special_tokens_extended` from tokenizer code (#29686)

- Full hash: `fecae12cd7deb969dcbba37fda9d2d234697a944`
- Date/author: 2025-11-28 / Harry Mellor
- Auto category: 调度/缓存/PD
- Main files: `tests/tokenization/test_cached_tokenizer.py`, `tests/tokenization/test_mistral_tokenizer.py`, `tests/tokenization/test_tokenizer_registry.py`, `vllm/transformers_utils/tokenizer.py`, `vllm/transformers_utils/tokenizer_base.py`, `vllm/transformers_utils/tokenizers/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/transformers_utils/tokenizer.py`; `vllm/transformers_utils/tokenizer_base.py`; `vllm/transformers_utils/tokenizers/mistral.py`
  - tests: `tests/tokenization/test_cached_tokenizer.py`; `tests/tokenization/test_mistral_tokenizer.py`; `tests/tokenization/test_tokenizer_registry.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `b2c1d294f` - [BUGFIX] MistralTokenizer._call__ adds an invalid EOS token (#29607)

- Full hash: `b2c1d294faca96643dbc2413d604ca160f458f0d`
- Date/author: 2025-11-28 / Julien Denize
- Auto category: 缺陷修复
- Main files: `tests/tokenization/test_mistral_tokenizer.py`, `vllm/transformers_utils/tokenizers/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/transformers_utils/tokenizers/mistral.py`
  - tests: `tests/tokenization/test_mistral_tokenizer.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `d1cf8214e` - [Bugfix] Use HF config fields as fallback when loading Mistral config (#29239)

- Full hash: `d1cf8214e523ce664797b3f65a26ffdc6e81f032`
- Date/author: 2025-11-23 / Cyrus Leung
- Auto category: 缺陷修复
- Main files: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`
  - runtime-model: `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/mistral.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `57430fc95` - Default model load/config/tokenizer to `mistral` format if relevant files exist (#28659)

- Full hash: `57430fc95c8a94a7c68b3d525e3b8823b0f2433f`
- Date/author: 2025-11-21 / Julien Denize
- Auto category: 性能/后端优化
- Main files: `docs/features/tool_calling.md`, `tests/models/language/generation/test_mistral.py`, `tests/models/multimodal/test_mapping.py`, `tests/models/quantization/test_bitsandbytes.py`, `tests/tool_use/utils.py`, `tests/transformers_utils/test_config.py`, `tests/transformers_utils/test_utils.py`, `tests/v1/entrypoints/llm/test_struct_output_generate.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/tool_calling.md`
  - other: `vllm/transformers_utils/tokenizer.py`; `vllm/v1/engine/processor.py`
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/model_loader/__init__.py`; `vllm/model_executor/model_loader/default_loader.py`; `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/mistral.py`
  - tests: `tests/models/language/generation/test_mistral.py`; `tests/models/multimodal/test_mapping.py`; `tests/models/quantization/test_bitsandbytes.py`; `tests/tool_use/utils.py`; `tests/transformers_utils/test_config.py`; `tests/transformers_utils/test_utils.py`; `tests/v1/entrypoints/llm/test_struct_output_generate.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `434f3d3eb` - Fix mistral config (#29172)

- Full hash: `434f3d3eb869606af221f0307e16548c1f99da20`
- Date/author: 2025-11-21 / Julien Denize
- Auto category: 缺陷修复
- Main files: `vllm/transformers_utils/configs/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/transformers_utils/configs/mistral.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `085424808` - Remove audio optional dependency for mistral-common (#28722)

- Full hash: `085424808ef705efbf59e7b18bc010f53d9d7f75`
- Date/author: 2025-11-14 / Julien Denize
- Auto category: 性能/后端优化
- Main files: `docs/contributing/model/transcription.md`, `docs/models/supported_models.md`, `examples/offline_inference/audio_language.py`, `requirements/common.txt`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/transcription.md`; `docs/models/supported_models.md`; `examples/offline_inference/audio_language.py`
  - other: `requirements/common.txt`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

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

### Commit `7a8375f8a` - Add llama 4 scaling support (#28145)

- Full hash: `7a8375f8a0cd37ee7e3d2be8498b5ae543694179`
- Date/author: 2025-11-06 / Julien Denize
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`, `vllm/model_executor/models/llama.py`, `vllm/transformers_utils/configs/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`; `vllm/model_executor/models/llama.py`; `vllm/transformers_utils/configs/mistral.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `a404e2c0f` - Patch Mistral Tokenizer (#28146)

- Full hash: `a404e2c0f1bf100d28453a5a2ab7bd2a29d9aa31`
- Date/author: 2025-11-06 / Julien Denize
- Auto category: 模型支持/运行时入口
- Main files: `tests/tokenization/test_mistral_tokenizer.py`, `vllm/transformers_utils/tokenizers/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/transformers_utils/tokenizers/mistral.py`
  - tests: `tests/tokenization/test_mistral_tokenizer.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `73444b7b5` - Performance fix MistralTokenizer: cache special ids and tokens (#27925)

- Full hash: `73444b7b5623f5bc569277c8c7dc809843312d11`
- Date/author: 2025-11-02 / Julien Denize
- Auto category: 性能/后端优化
- Main files: `vllm/transformers_utils/tokenizers/mistral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/transformers_utils/tokenizers/mistral.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.
