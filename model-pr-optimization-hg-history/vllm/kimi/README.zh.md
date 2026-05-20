# vllm Kimi K2/K2.5/Linear/VL 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `tests/tool_parsers/test_kimi_k2_tool_parser.py` | `fefce4980`, `358bfd315`, `ed586e772` |
| `vllm/model_executor/models/kimi_k25.py` | `5042815ab`, `b539f988e` |
| `vllm/model_executor/models/kimi_k25_vit.py` | `5042815ab`, `b539f988e` |
| `vllm/model_executor/models/kimi_linear.py` | `df7041633`, `dcd80206b`, `5206e5e28`, `482914849`, `a8b70304d`, `97d1c9930`, `bc306fe5e`, `e5ef4dfc1`, `4e68cc9b6` |
| `vllm/model_executor/models/kimi_vl.py` | `df7041633`, `dcd80206b`, `9ad7f89f5`, `7f1bcd18f`, `9ea07b41d`, `482914849`, `7101e0851`, `c46b932df`, `97d1c9930`, `9d1c47470`, `c7991269d`, `43ecd0a90` |
| `vllm/model_executor/models/moonvit.py` | `9ad7f89f5`, `2612ba928`, `2972a0547`, `7101e0851`, `3cfa63ad9`, `e4bb2684b`, `879a06579` |
| `vllm/reasoning/kimi_k2_reasoning_parser.py` | `5042815ab`, `b539f988e` |
| `vllm/tool_parsers/kimi_k2_tool_parser.py` | `899a2db47`, `2d7053438`, `fefce4980`, `358bfd315`, `2a1776b7a` |
| `vllm/transformers_utils/configs/kimi_k25.py` | `5042815ab`, `b539f988e` |
| `vllm/transformers_utils/configs/kimi_linear.py` | `a8b70304d`, `4e68cc9b6` |
| `vllm/transformers_utils/configs/kimi_vl.py` | `43ecd0a90` |
| `vllm/transformers_utils/configs/moonvit.py` | 无直接提交 |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 40
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-05 | `899a2db47` | 性能/后端优化 | sync v0.15.1(ex fused_moe&models) | `vllm/_custom_ops.py`, `vllm/compilation/decorators.py`, `vllm/config/compilation.py` |
| 2026-01-26 | `5042815ab` | 模型支持/运行时入口 | [Models] Kimi-K2.5 (#33131) | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/entrypoints/chat_utils.py` |
| 2026-01-26 | `b539f988e` | 模型支持/运行时入口 | [Models] Kimi-K2.5 (#33131) | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/entrypoints/chat_utils.py` |
| 2026-01-27 | `2d7053438` | 缺陷修复 | fix: preserve native tool call ID in multi-turn tool calling (#32768) | `tests/entrypoints/openai/test_chat_error.py`, `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-24 | `9ad7f89f5` | 性能/后端优化 | [Models]: Make Multimodal config implicit in ViT implementation (#31972) | `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py` |
| 2026-01-24 | `5206e5e28` | 性能/后端优化 | [V1][Hybrid] Mamba Prefix Caching with align mode (#30877) | `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py` |
| 2026-01-20 | `7f1bcd18f` | 模型支持/运行时入口 | [3/N] Initialize MM components in context managers (I-L) (#32650) | `vllm/model_executor/models/interns1.py`, `vllm/model_executor/models/internvl.py`, `vllm/model_executor/models/isaac.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-08 | `2972a0547` | 模型支持/运行时入口 | [MM Encoder]: Make MMEncoderAttention's `scale` takes effect properly (#31950) | `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `7101e0851` | 模型支持/运行时入口 | [Models]: Use `MMEncoderAttention` for MoonViT (#31738) | `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/moonvit.py` |
| 2025-12-30 | `358bfd315` | 缺陷修复 | fix: update kimi k2 tool parser logic (#31207) | `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py` |
| 2025-12-15 | `ed586e772` | 性能/后端优化 | [Refactor] [3/N] Move tool parser tests and run on CPU (#30693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-05 | `e3fbb6f15` | 缺陷修复 | fix#30092 Kimi-Linear model loading failure with missing indexer_rotary_emb (#30093) | `vllm/model_executor/layers/mla.py` |
| 2025-12-02 | `653591d5e` | 性能/后端优化 | [Chore] Move tokenizer initialization methods (#29793) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py` |
| 2025-12-01 | `fa8804ad9` | 缺陷修复 | [responsesAPI][4] fix responseOutputItem Kimi K2 thinking bug (#29555) | `tests/entrypoints/test_responses_utils.py`, `vllm/entrypoints/responses_utils.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-25 | `3cfa63ad9` | 缺陷修复 | [XPU]fix Kimi-VL-A3B-thinking on xpu (#29309) | `vllm/model_executor/models/moonvit.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-19 | `e4bb2684b` | 模型支持/运行时入口 | [Models] Replace all `nn.Conv2d` with vLLM's Conv2dLayer (#28842) | `vllm/model_executor/layers/conv.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/blip.py` |
| 2025-11-18 | `b6e04390d` | 缺陷修复 | [Bugfix] Fix Kimi-K2 tool parser concatenated tool calls parsing (#28831) | `tests/tool_use/test_kimi_k2_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/kimi_k2_tool_parser.py` |
| 2025-11-16 | `6f3741924` | 缺陷修复 | [Bugfix][Model] Prevent special token leakage in KimiK2ToolParser streaming mode (#28543) | `tests/tool_use/test_kimi_k2_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/kimi_k2_tool_parser.py` |
| 2025-11-13 | `fa183e927` | 缺陷修复 | [Bugfix] fix kimi-linear crash (#28445) | `vllm/model_executor/layers/kda.py` |
| 2025-11-12 | `7e082bc14` | 性能/后端优化 | Support DeepEP for Kimi-k2-thinking through enabling gemm selection for compressed-tensor marlin wna16 (#28574) | `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `9d1c47470` | 性能/后端优化 | [LoRA][1/N]Remove LoRA extra vocab (#28382) | `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py` |
| 2025-11-11 | `c7991269d` | 缺陷修复 | [BugFix] 'DeepseekV2Config' object has no attribute 'use_mla'` (#28387) | `vllm/model_executor/models/kimi_vl.py` |
| 2025-11-06 | `43ecd0a90` | 模型支持/运行时入口 | [Chore] Clean up deepseek v2/v3 config copy (#28055) | `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/kimi_vl.py` |
| 2025-11-05 | `0606bea2b` | 模型支持/运行时入口 | add kimi reasoning parser (#28128) | `vllm/reasoning/__init__.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |
| 2025-11-01 | `879a06579` | 模型支持/运行时入口 | [CI/Build] Bump transformers version (#27528) | `requirements/common.txt`, `requirements/nightly_torch_test.txt`, `requirements/test.in` |
| 2025-11-01 | `bc306fe5e` | 缺陷修复 | fix incorrect type annotation in KimiMLP (#27885) | `vllm/model_executor/models/kimi_linear.py` |
| 2025-10-31 | `e5ef4dfc1` | 性能/后端优化 | [Kimi-Linear] Correct prefixes and add compatibility to AWQ quants (#27834) | `vllm/model_executor/models/kimi_linear.py` |
| 2025-10-30 | `4e68cc9b6` | 模型支持/运行时入口 | [Model] Introduce Kimi Linear to vLLM (#27809) | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/compilation.py` |

## 逐 Commit 审计卡

### Commit `df7041633` - sync v0.15.1 (models)

- 完整 hash: `df7041633878cacfcd677cef5efc907705de6c98`
- 时间/作者: 2026-02-06 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/bagel.py` 等 169 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 147 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `899a2db47` - sync v0.15.1(ex fused_moe&models)

- 完整 hash: `899a2db4715963a4dfde80e69d71a57cf0c97f28`
- 时间/作者: 2026-02-05 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/_custom_ops.py`, `vllm/compilation/decorators.py`, `vllm/config/compilation.py`, `vllm/config/speculative.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/distributed/device_communicators/base_device_communicator.py`, `vllm/distributed/device_communicators/cpu_communicator.py`, `vllm/distributed/device_communicators/cuda_communicator.py` 等 72 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/_custom_ops.py`; `vllm/compilation/decorators.py`; `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/logging_utils/__init__.py`; `vllm/logging_utils/access_log_filter.py`; `vllm/plugins/lora_resolvers/filesystem_resolver.py` 等 15 个文件
  - runtime-model: `vllm/config/compilation.py`; `vllm/config/speculative.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/completion/serving.py`; `vllm/entrypoints/openai/engine/protocol.py` 等 29 个文件
  - runtime-perf: `vllm/distributed/device_communicators/all2all.py`; `vllm/distributed/device_communicators/base_device_communicator.py`; `vllm/distributed/device_communicators/cpu_communicator.py`; `vllm/distributed/device_communicators/cuda_communicator.py`; `vllm/distributed/device_communicators/mnnvl_compat.py`; `vllm/distributed/device_communicators/xpu_communicator.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/distributed/parallel_state.py` 等 28 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5042815ab` - [Models] Kimi-K2.5 (#33131)

- 完整 hash: `5042815ab6eb96596730e2853beef6cdfe0a3996`
- 时间/作者: 2026-01-26 / Roger Wang
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/entrypoints/chat_utils.py`, `vllm/envs.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/registry.py`, `vllm/multimodal/inputs.py` 等 16 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/envs.py`; `vllm/multimodal/inputs.py`; `vllm/multimodal/parse.py`; `vllm/multimodal/video.py`; `vllm/reasoning/__init__.py`; `vllm/reasoning/kimi_k2_reasoning_parser.py`; `vllm/renderers/hf.py`
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/model_executor/models/kimi_k25.py`; `vllm/model_executor/models/kimi_k25_vit.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/kimi_k25.py`
  - tests: `tests/models/registry.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b539f988e` - [Models] Kimi-K2.5 (#33131)

- 完整 hash: `b539f988e1eeffe1c39bebbeaba892dc529eefaf`
- 时间/作者: 2026-01-26 / Roger Wang
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/entrypoints/chat_utils.py`, `vllm/envs.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/registry.py`, `vllm/multimodal/inputs.py` 等 16 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/envs.py`; `vllm/multimodal/inputs.py`; `vllm/multimodal/parse.py`; `vllm/multimodal/video.py`; `vllm/reasoning/__init__.py`; `vllm/reasoning/kimi_k2_reasoning_parser.py`; `vllm/renderers/hf.py`
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/model_executor/models/kimi_k25.py`; `vllm/model_executor/models/kimi_k25_vit.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/kimi_k25.py`
  - tests: `tests/models/registry.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `2d7053438` - fix: preserve native tool call ID in multi-turn tool calling (#32768)

- 完整 hash: `2d7053438a112e2be55cf6d2bde9deb8a169d0a4`
- 时间/作者: 2026-01-27 / wangln19
- 自动分类: 缺陷修复
- 主要文件: `tests/entrypoints/openai/test_chat_error.py`, `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/engine/protocol.py`, `vllm/entrypoints/openai/engine/serving.py`, `vllm/entrypoints/openai/responses/serving.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tool_parsers/kimi_k2_tool_parser.py`
  - runtime-model: `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/engine/protocol.py`; `vllm/entrypoints/openai/engine/serving.py`; `vllm/entrypoints/openai/responses/serving.py`
  - tests: `tests/entrypoints/openai/test_chat_error.py`; `tests/entrypoints/openai/test_serving_chat.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `dcd80206b` - [Chore] Update type annotation of `input_ids` in model forward (#33063)

- 完整 hash: `dcd80206b7a9143c81f7f2808e84914f8e38ce95`
- 时间/作者: 2026-01-26 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py` 等 164 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 140 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
  - tests: `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9ad7f89f5` - [Models]: Make Multimodal config implicit in ViT implementation (#31972)

- 完整 hash: `9ad7f89f55b7046d0498608eb85b94b2dc5c2666`
- 时间/作者: 2026-01-24 / Isotr0py
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/eagle2_5_vl.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py` 等 38 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/eagle2_5_vl.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/hunyuan_vision.py` 等 35 个文件
  - runtime-perf: `vllm/model_executor/layers/attention/mm_encoder_attention.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/model_executor/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5206e5e28` - [V1][Hybrid] Mamba Prefix Caching with align mode (#30877)

- 完整 hash: `5206e5e28c25dcc43d3a2373b591a0cdf9792f5d`
- 时间/作者: 2026-01-24 / Harry Huang
- 自动分类: 性能/后端优化
- 主要文件: `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py`, `vllm/config/vllm.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py` 等 42 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/engine/arg_utils.py`; `vllm/v1/core/block_pool.py`
  - runtime-model: `vllm/config/vllm.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/mamba_mixer.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/mamba_utils.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/falcon_h1.py` 等 26 个文件
  - runtime-perf: `vllm/config/cache.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/v1/attention/backends/gdn_attn.py`; `vllm/v1/attention/backends/linear_attn.py`; `vllm/v1/attention/backends/mamba_attn.py`; `vllm/v1/attention/backends/utils.py`; `vllm/v1/core/kv_cache_coordinator.py` 等 12 个文件
  - tests: `tests/v1/core/test_single_type_kv_cache_manager.py`; `tests/v1/e2e/test_mamba_prefix_cache.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7f1bcd18f` - [3/N] Initialize MM components in context managers (I-L) (#32650)

- 完整 hash: `7f1bcd18ffd9313a72e1d72c55a3d44f4fbb6157`
- 时间/作者: 2026-01-20 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/interns1.py`, `vllm/model_executor/models/internvl.py`, `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/kanana_v.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/lfm2_vl.py`, `vllm/model_executor/models/llava_next.py` 等 10 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/interns1.py`; `vllm/model_executor/models/internvl.py`; `vllm/model_executor/models/isaac.py`; `vllm/model_executor/models/kanana_v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/kimi_vl.py`; `vllm/model_executor/models/lfm2_vl.py`; `vllm/model_executor/models/llava_next.py` 等 10 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9ea07b41d` - [1/N] Reorganize multimodal processing code (#32327)

- 完整 hash: `9ea07b41da169f727a2eb7302adec4c724319522`
- 时间/作者: 2026-01-14 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md`, `tests/multimodal/test_processing.py`, `vllm/benchmarks/mm_processor.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py` 等 76 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/api/README.md`; `docs/contributing/model/multimodal.md`; `docs/design/mm_processing.md`
  - other: `vllm/benchmarks/mm_processor.py`; `vllm/multimodal/inputs.py`; `vllm/multimodal/processing/__init__.py`; `vllm/multimodal/processing/context.py`; `vllm/multimodal/processing/dummy_inputs.py`; `vllm/multimodal/processing/processor.py`; `vllm/multimodal/registry.py`; `vllm/v1/engine/input_processor.py`
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/blip2.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/cohere2_vision.py` 等 62 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/multimodal/cache.py`
  - tests: `tests/multimodal/test_processing.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fefce4980` - [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240)

- 完整 hash: `fefce49807a52fc94678e336fc5d1f3b7ebe2daf`
- 时间/作者: 2026-01-13 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_completion_error.py`, `tests/entrypoints/openai/test_gptoss_structural_tags_integration.py`, `tests/entrypoints/openai/test_lora_resolvers.py`, `tests/entrypoints/openai/test_protocol.py` 等 128 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/basic_parsers.py`; `vllm/reasoning/deepseek_r1_reasoning_parser.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/ernie45_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/granite_reasoning_parser.py`; `vllm/reasoning/holo2_reasoning_parser.py` 等 45 个文件
  - runtime-model: `vllm/entrypoints/anthropic/serving_messages.py`; `vllm/entrypoints/context.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/chat_completion/__init__.py`; `vllm/entrypoints/openai/chat_completion/api_router.py`; `vllm/entrypoints/openai/chat_completion/protocol.py`; `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/chat_completion/stream_harmony.py` 等 43 个文件
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/responses/test_errors.py`; `tests/entrypoints/openai/responses/test_function_call_parsing.py`; `tests/entrypoints/openai/test_chat_error.py`; `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_completion_error.py`; `tests/entrypoints/openai/test_gptoss_structural_tags_integration.py`; `tests/entrypoints/openai/test_lora_resolvers.py`; `tests/entrypoints/openai/test_protocol.py` 等 39 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2612ba928` - [1/N][Attention] Restructure attention: move files (#31916)

- 完整 hash: `2612ba9285d828f3179801334b6d2db0046b9b6c`
- 时间/作者: 2026-01-09 / Matthew Bonanni
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml`, `.github/CODEOWNERS`, `.github/mergify.yml`, `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`, `docs/contributing/model/basic.md`, `docs/design/custom_op.md` 等 195 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/kernels.yaml`; `.github/CODEOWNERS`; `.github/mergify.yml`
  - docs-bench: `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`; `docs/contributing/model/basic.md`; `docs/design/custom_op.md`; `docs/design/plugin_system.md`; `examples/offline_inference/basic/embed.py`; `examples/offline_inference/basic/score.py`
  - other: `tools/pre_commit/mypy.py`; `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/xpu.py`; `vllm/v1/kv_offload/cpu.py` 等 10 个文件
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/layers/batch_invariant.py`; `vllm/model_executor/layers/kda.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/short_conv.py` 等 66 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/ops/__init__.py`; `vllm/config/attention.py`; `vllm/distributed/kv_transfer/kv_connector/utils.py`; `vllm/distributed/kv_transfer/kv_connector/v1/base.py`; `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py` 等 73 个文件
  - tests: `tests/compile/fullgraph/test_full_cudagraph.py`; `tests/compile/fullgraph/test_full_graph.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/config/test_multimodal_config.py`; `tests/engine/test_arg_utils.py`; `tests/kernels/attention/test_aiter_flash_attn.py`; `tests/kernels/attention/test_attention.py` 等 35 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2972a0547` - [MM Encoder]: Make MMEncoderAttention's `scale` takes effect properly  (#31950)

- 完整 hash: `2972a05473d64a21c7390a5676bbb07bd8d2c8da`
- 时间/作者: 2026-01-08 / Isotr0py
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glmasr.py`, `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/moonvit.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glmasr.py`; `vllm/model_executor/models/isaac.py`; `vllm/model_executor/models/moonvit.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_vl.py` 等 9 个文件
  - runtime-perf: `vllm/attention/layers/mm_encoder_attention.py`; `vllm/attention/ops/vit_attn_wrappers.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `482914849` - [BugFix] LoRA: Support loading base_layer of experts (#31104)

- 完整 hash: `482914849cf9ce61d3e0dffaa35096bb34de58f5`
- 时间/作者: 2026-01-07 / ℍ𝕠𝕝𝕝𝕠𝕨 𝕄𝕒𝕟
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/dots1.py`, `vllm/model_executor/models/ernie45_moe.py` 等 35 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/dots1.py`; `vllm/model_executor/models/gpt_oss.py`; `vllm/model_executor/models/grok1.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/jamba.py` 等 19 个文件
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py` 等 16 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7101e0851` - [Models]: Use `MMEncoderAttention` for MoonViT (#31738)

- 完整 hash: `7101e0851f73b8157145cf04835a87dc0837d450`
- 时间/作者: 2026-01-06 / Isotr0py
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/kimi_vl.py`, `vllm/model_executor/models/moonvit.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/kimi_vl.py`; `vllm/model_executor/models/moonvit.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `358bfd315` - fix: update kimi k2 tool parser logic (#31207)

- 完整 hash: `358bfd315cad6956f0921a4e8a9c4baa053abafc`
- 时间/作者: 2025-12-30 / wangln19
- 自动分类: 缺陷修复
- 主要文件: `tests/tool_parsers/test_kimi_k2_tool_parser.py`, `vllm/tool_parsers/kimi_k2_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tool_parsers/kimi_k2_tool_parser.py`
  - tests: `tests/tool_parsers/test_kimi_k2_tool_parser.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `ed586e772` - [Refactor] [3/N] Move tool parser tests and run on CPU (#30693)

- 完整 hash: `ed586e7724fdf91b391abcf6f3e473be641ff5d6`
- 时间/作者: 2025-12-15 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/tool_use.yaml`, `tests/tool_parsers/__init__.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_ernie45_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py` 等 16 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/misc.yaml`; `.buildkite/test_areas/tool_use.yaml`
  - tests: `tests/tool_parsers/__init__.py`; `tests/tool_parsers/test_deepseekv31_tool_parser.py`; `tests/tool_parsers/test_ernie45_moe_tool_parser.py`; `tests/tool_parsers/test_glm4_moe_tool_parser.py`; `tests/tool_parsers/test_jamba_tool_parser.py`; `tests/tool_parsers/test_kimi_k2_tool_parser.py`; `tests/tool_parsers/test_minimax_tool_parser.py`; `tests/tool_parsers/test_mistral_tool_parser.py` 等 12 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `2a1776b7a` - [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675)

- 完整 hash: `2a1776b7ac4fae7c50c694edeafc1b14270e4350`
- 时间/作者: 2025-12-15 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_hunyuan_a13b_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`, `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py` 等 61 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/tool_calling.md`
  - other: `vllm/tool_parsers/__init__.py`; `vllm/tool_parsers/abstract_tool_parser.py`; `vllm/tool_parsers/deepseekv31_tool_parser.py`; `vllm/tool_parsers/deepseekv32_tool_parser.py`; `vllm/tool_parsers/deepseekv3_tool_parser.py`; `vllm/tool_parsers/ernie45_tool_parser.py`; `vllm/tool_parsers/gigachat3_tool_parser.py`; `vllm/tool_parsers/granite_20b_fc_tool_parser.py` 等 30 个文件
  - runtime-model: `vllm/entrypoints/context.py`; `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/parser/responses_parser.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_engine.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_hunyuan_a13b_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_pythonic_tool_parser.py` 等 22 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c46b932df` - [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170)

- 完整 hash: `c46b932df2b801ba0a6452e436268f086029d82b`
- 时间/作者: 2025-12-06 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/cohere2_vision.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/deepseek_vl2.py` 等 61 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/utils.py`
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/blip2.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/cohere2_vision.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/deepseek_vl2.py` 等 59 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e3fbb6f15` - fix#30092 Kimi-Linear model loading failure with missing indexer_rotary_emb (#30093)

- 完整 hash: `e3fbb6f152fe721506f22b3d8d2ec70c10229569`
- 时间/作者: 2025-12-05 / Dongjie Zou
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/mla.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/mla.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `653591d5e` - [Chore] Move tokenizer initialization methods (#29793)

- 完整 hash: `653591d5e73b34ffd9186c61e964474bcc4b7c80`
- 时间/作者: 2025-12-02 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/openai/test_lora_resolvers.py`, `tests/entrypoints/openai/test_return_token_ids.py`, `tests/entrypoints/openai/test_return_tokens_as_ids.py`, `tests/entrypoints/openai/test_serving_chat.py` 等 51 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmarks/benchmark_prefix_caching.py`; `benchmarks/benchmark_serving_structured_output.py`
  - other: `vllm/benchmarks/serve.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/__init__.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/tokenizer.py`; `vllm/v1/engine/async_llm.py`; `vllm/v1/engine/llm_engine.py`; `vllm/v1/structured_output/__init__.py`
  - runtime-model: `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/deepseek_vl2.py`; `vllm/model_executor/models/granite_speech.py`; `vllm/model_executor/models/gritlm.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/pixtral.py`; `vllm/model_executor/models/voxtral.py` 等 9 个文件
  - tests: `tests/compile/test_dynamic_shapes_compilation.py`; `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/openai/test_lora_resolvers.py`; `tests/entrypoints/openai/test_return_token_ids.py`; `tests/entrypoints/openai/test_return_tokens_as_ids.py`; `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/test_token_in_token_out.py`; `tests/entrypoints/openai/test_tokenization.py` 等 32 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `fa8804ad9` - [responsesAPI][4] fix responseOutputItem Kimi K2 thinking bug (#29555)

- 完整 hash: `fa8804ad9c3f21dad3143418c7d9f40190f609ae`
- 时间/作者: 2025-12-01 / Andrew Xia
- 自动分类: 缺陷修复
- 主要文件: `tests/entrypoints/test_responses_utils.py`, `vllm/entrypoints/responses_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/responses_utils.py`
  - tests: `tests/entrypoints/test_responses_utils.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `34a984274` - [Misc] Refactor tokenizer interface (#29693)

- 完整 hash: `34a984274eae2f8fb9d1d6413abd08d7fcde741c`
- 时间/作者: 2025-11-29 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py`, `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_engine.py`, `tests/entrypoints/openai/tool_parsers/conftest.py`, `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py` 等 119 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/backend_request_func.py`; `docs/features/reasoning_outputs.md`; `docs/features/tool_calling.md`
  - other: `tools/pre_commit/check_pickle_imports.py`; `tools/pre_commit/mypy.py`; `vllm/benchmarks/datasets.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/logits_process.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py` 等 32 个文件
  - runtime-model: `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_classification.py`; `vllm/entrypoints/openai/serving_completion.py`; `vllm/entrypoints/openai/serving_engine.py`; `vllm/entrypoints/openai/serving_responses.py`; `vllm/entrypoints/openai/serving_score.py` 等 44 个文件
  - runtime-perf: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/entrypoints/openai/test_serving_engine.py`; `tests/entrypoints/openai/tool_parsers/conftest.py`; `tests/entrypoints/openai/tool_parsers/test_hermes_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama3_json_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_olmo3_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/test_pythonic_tool_parser.py`; `tests/entrypoints/openai/tool_parsers/utils.py` 等 37 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3cfa63ad9` - [XPU]fix Kimi-VL-A3B-thinking on xpu (#29309)

- 完整 hash: `3cfa63ad991665b2440155cd29352342024072fd`
- 时间/作者: 2025-11-25 / Yan Ma
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/moonvit.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/moonvit.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `a8b70304d` - Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542)

- 完整 hash: `a8b70304d68497ac1c432a2ff343e9bfb516c227`
- 时间/作者: 2025-11-19 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/language/pooling/test_nomic_max_model_len.py` 等 104 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `examples/offline_inference/context_extension.py`
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py` 等 78 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 17 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; `tests/models/language/pooling/test_nomic_max_model_len.py`; `tests/test_config.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e4bb2684b` - [Models] Replace all `nn.Conv2d` with vLLM's Conv2dLayer (#28842)

- 完整 hash: `e4bb2684bcea12f72a36a6c48292f79534af849a`
- 时间/作者: 2025-11-19 / Isotr0py
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/layers/conv.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/blip.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/conv.py`; `vllm/model_executor/models/aimv2.py`; `vllm/model_executor/models/blip.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glm4v.py` 等 20 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b6e04390d` - [Bugfix] Fix Kimi-K2 tool parser concatenated tool calls parsing (#28831)

- 完整 hash: `b6e04390d3ea5ebc79ac70d1b76d638c56fa8ce2`
- 时间/作者: 2025-11-18 / Benjamin Bartels
- 自动分类: 缺陷修复
- 主要文件: `tests/tool_use/test_kimi_k2_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/kimi_k2_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/kimi_k2_tool_parser.py`
  - tests: `tests/tool_use/test_kimi_k2_tool_parser.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `6f3741924` - [Bugfix][Model] Prevent special token leakage in KimiK2ToolParser streaming mode (#28543)

- 完整 hash: `6f374192442381b37a6a6ba29045c74a8ee2486d`
- 时间/作者: 2025-11-16 / Jay Caldwell
- 自动分类: 缺陷修复
- 主要文件: `tests/tool_use/test_kimi_k2_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/kimi_k2_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/kimi_k2_tool_parser.py`
  - tests: `tests/tool_use/test_kimi_k2_tool_parser.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `fa183e927` - [Bugfix] fix kimi-linear crash (#28445)

- 完整 hash: `fa183e92713456dec682088a362dd9908100cc03`
- 时间/作者: 2025-11-13 / Jiangyun Zhu
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/kda.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/kda.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `7e082bc14` - Support DeepEP for Kimi-k2-thinking through enabling gemm selection for compressed-tensor marlin wna16 (#28574)

- 完整 hash: `7e082bc14e431af0311186dd18d4f4da7a757f3a`
- 时间/作者: 2025-11-12 / Lucia Fang
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `97d1c9930` - Rename clashing method names for vLLM model protocol (#27583)

- 完整 hash: `97d1c99302df6f7eadc0d0b32ec174db69cb4421`
- 时间/作者: 2025-11-13 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/baichuan.py` 等 164 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`; `docs/contributing/model/multimodal.md`
  - other: `vllm/multimodal/processing.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/bert.py` 等 144 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 16 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9d1c47470` - [LoRA][1/N]Remove LoRA extra vocab (#28382)

- 完整 hash: `9d1c47470430ba31c02946aa1fd01aadf6e18b91`
- 时间/作者: 2025-11-12 / Jee Jee Li
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/baichuan.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/chameleon.py` 等 65 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 58 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/longcat_flash.py`; `vllm/model_executor/models/phimoe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c7991269d` - [BugFix] 'DeepseekV2Config' object has no attribute 'use_mla'`  (#28387)

- 完整 hash: `c7991269dd8fe86096a3eee5040e855801ae9665`
- 时间/作者: 2025-11-11 / Fanli Lin
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/kimi_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/kimi_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `43ecd0a90` - [Chore] Clean up deepseek v2/v3 config copy (#28055)

- 完整 hash: `43ecd0a900e45e0c594bb428f18b8f2b14434391`
- 时间/作者: 2025-11-06 / Isotr0py
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/kimi_vl.py`, `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/deepseek_v3.py`, `vllm/transformers_utils/configs/deepseek_vl2.py`, `vllm/transformers_utils/configs/eagle.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/kimi_vl.py`; `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/__init__.py`; `vllm/transformers_utils/configs/deepseek_v3.py`; `vllm/transformers_utils/configs/deepseek_vl2.py`; `vllm/transformers_utils/configs/eagle.py` 等 9 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `0606bea2b` - add kimi reasoning parser (#28128)

- 完整 hash: `0606bea2b63f6b5d49e5d04b4561f2e606cc7c45`
- 时间/作者: 2025-11-05 / bigmoyan
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/reasoning/__init__.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/reasoning/__init__.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c02fccdbd` - [Refactor] Lazy import tool_parser (#27974)

- 完整 hash: `c02fccdbd2794fe016ebd738e3a8b8c8d78eb78c`
- 时间/作者: 2025-11-04 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py`, `tests/tool_use/test_glm4_moe_tool_parser.py`, `tests/tool_use/test_jamba_tool_parser.py`, `tests/tool_use/test_kimi_k2_tool_parser.py`, `tests/tool_use/test_minimax_tool_parser.py`, `tests/tool_use/test_openai_tool_parser.py` 等 40 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/tool_calling.md`
  - runtime-model: `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/cli_args.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`; `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/deepseekv31_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/deepseekv3_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/ernie45_tool_parser.py`; `vllm/entrypoints/openai/tool_parsers/granite_20b_fc_tool_parser.py` 等 29 个文件
  - runtime-perf: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`
  - tests: `tests/tool_use/test_deepseekv31_tool_parser.py`; `tests/tool_use/test_ernie45_moe_tool_parser.py`; `tests/tool_use/test_glm4_moe_tool_parser.py`; `tests/tool_use/test_jamba_tool_parser.py`; `tests/tool_use/test_kimi_k2_tool_parser.py`; `tests/tool_use/test_minimax_tool_parser.py`; `tests/tool_use/test_openai_tool_parser.py`; `tests/tool_use/test_seed_oss_tool_parser.py` 等 9 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `879a06579` - [CI/Build] Bump transformers version (#27528)

- 完整 hash: `879a06579ea8a057c250e9b6cc4e632dabd87d2e`
- 时间/作者: 2025-11-01 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `requirements/common.txt`, `requirements/nightly_torch_test.txt`, `requirements/test.in`, `requirements/test.txt`, `tests/models/multimodal/generation/test_maverick.py`, `tests/models/registry.py`, `tests/models/test_transformers.py`, `vllm/model_executor/models/moonvit.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `requirements/common.txt`; `requirements/nightly_torch_test.txt`; `requirements/test.in`; `requirements/test.txt`
  - runtime-model: `vllm/model_executor/models/moonvit.py`; `vllm/model_executor/models/qwen2_vl.py`
  - tests: `tests/models/multimodal/generation/test_maverick.py`; `tests/models/registry.py`; `tests/models/test_transformers.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `bc306fe5e` - fix incorrect type annotation in KimiMLP (#27885)

- 完整 hash: `bc306fe5e97823e2a2e989725bd5e39a897a43a6`
- 时间/作者: 2025-11-01 / ZiTian Zhao
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/kimi_linear.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/kimi_linear.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `e5ef4dfc1` - [Kimi-Linear] Correct prefixes and add compatibility to AWQ quants (#27834)

- 完整 hash: `e5ef4dfc11abfc44494963b85ced1c79d1d5efea`
- 时间/作者: 2025-10-31 / toncao
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/kimi_linear.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/kimi_linear.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `4e68cc9b6` - [Model] Introduce Kimi Linear to vLLM (#27809)

- 完整 hash: `4e68cc9b6aa2b9cfe8d799c2b1cd156a01bca438`
- 时间/作者: 2025-10-30 / Zhiyuan Li
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/compilation.py`, `vllm/config/model.py`, `vllm/model_executor/layers/fla/ops/kda.py`, `vllm/model_executor/layers/kda.py`, `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/layers/mla.py` 等 15 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/models/supported_models.md`
  - runtime-model: `vllm/config/compilation.py`; `vllm/config/model.py`; `vllm/model_executor/layers/fla/ops/kda.py`; `vllm/model_executor/layers/kda.py`; `vllm/model_executor/layers/mamba/mamba_utils.py`; `vllm/model_executor/layers/mla.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/kimi_linear.py` 等 13 个文件
  - tests: `tests/models/registry.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
