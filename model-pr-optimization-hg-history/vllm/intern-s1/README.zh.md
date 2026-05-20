# vllm Intern-S1 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `examples/tool_chat_template_internlm2_tool.jinja` | 无直接提交 |
| `vllm/model_executor/models/internlm2.py` | `df7041633`, `dcd80206b`, `2b8a38b6d`, `583a90e00`, `c8ed39b9d`, `cf3eacfe5`, `430dd4d9e`, `a8b70304d`, `97d1c9930`, `9d1c47470` |
| `vllm/model_executor/models/internlm2_ve.py` | `df7041633`, `dcd80206b`, `a8b70304d` |
| `vllm/model_executor/models/interns1.py` | `df7041633`, `dcd80206b`, `fda3f03eb`, `7f1bcd18f`, `9ea07b41d`, `e83b7e379`, `27f4c2fd4`, `c46b932df`, `97d1c9930` |
| `vllm/model_executor/models/interns1_vit.py` | `2612ba928`, `700a5ad6c`, `e4bb2684b` |
| `vllm/tool_parsers/internlm2_tool_parser.py` | `fefce4980`, `2a1776b7a` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 23
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-22 | `2b8a38b6d` | 性能/后端优化 | [Model] Extend `collect_children` and `no_init_weights` contexts (#32757) | `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py` |
| 2026-01-20 | `fda3f03eb` | 性能/后端优化 | [4/N] Initialize MM components in context managers (M-P) (#32663) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/interfaces.py` |
| 2026-01-20 | `7f1bcd18f` | 模型支持/运行时入口 | [3/N] Initialize MM components in context managers (I-L) (#32650) | `vllm/model_executor/models/interns1.py`, `vllm/model_executor/models/internvl.py`, `vllm/model_executor/models/isaac.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-10 | `583a90e00` | 模型支持/运行时入口 | [Refactor] Separate sequence and token pooling types (#32026) | `tests/model_executor/test_model_load_with_params.py`, `tests/models/language/pooling/test_embedding.py`, `tests/models/language/pooling/test_mm_classifier_conversion.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-09 | `c8ed39b9d` | 模型支持/运行时入口 | [Model] Reorganize pooling layers (#31973) | `.github/CODEOWNERS`, `tests/model_executor/test_model_load_with_params.py`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py` |
| 2025-12-19 | `700a5ad6c` | 性能/后端优化 | [MM Encoder]: Migrate legacy ViT `MultiHeadAttention` to new `MMEncoderAttention` interface (#30684) | `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_mha_attn.py`, `tests/v1/tpu/test_mha_attn.py` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `e83b7e379` | 调度/缓存/PD | Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `27f4c2fd4` | 调度/缓存/PD | [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-19 | `e4bb2684b` | 模型支持/运行时入口 | [Models] Replace all `nn.Conv2d` with vLLM's Conv2dLayer (#28842) | `vllm/model_executor/layers/conv.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/blip.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `9d1c47470` | 性能/后端优化 | [LoRA][1/N]Remove LoRA extra vocab (#28382) | `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |

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

### Commit `2b8a38b6d` - [Model] Extend `collect_children` and `no_init_weights` contexts (#32757)

- 完整 hash: `2b8a38b6d6be4f6e09cc20381c7027e7c35cb6c9`
- 时间/作者: 2026-01-22 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/bagel.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/glm4v.py`, `vllm/model_executor/models/idefics3.py` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/utils/collection_utils.py`
  - runtime-model: `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/gemma3_mm.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/idefics3.py`; `vllm/model_executor/models/interfaces.py` 等 17 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
  - tests: `tests/utils_/test_collection_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fda3f03eb` - [4/N] Initialize MM components in context managers (M-P) (#32663)

- 完整 hash: `fda3f03eb28c3b0daf73394219b8ad73adfc53e8`
- 时间/作者: 2026-01-20 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/interns1.py`, `vllm/model_executor/models/internvl.py`, `vllm/model_executor/models/midashenglm.py`, `vllm/model_executor/models/minicpmo.py`, `vllm/model_executor/models/minicpmv.py` 等 24 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/interns1.py`; `vllm/model_executor/models/internvl.py`; `vllm/model_executor/models/midashenglm.py`; `vllm/model_executor/models/minicpmo.py`; `vllm/model_executor/models/minicpmv.py` 等 23 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
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

### Commit `583a90e00` - [Refactor] Separate sequence and token pooling types (#32026)

- 完整 hash: `583a90e0055f3fa1fc464b2dd62ea26a7d389ae1`
- 时间/作者: 2026-01-10 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `tests/model_executor/test_model_load_with_params.py`, `tests/models/language/pooling/test_embedding.py`, `tests/models/language/pooling/test_mm_classifier_conversion.py`, `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/mteb_score_utils.py`, `tests/models/language/pooling_mteb_test/test_baai.py`, `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py`, `tests/models/language/pooling_mteb_test/test_cross_encoder.py` 等 42 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/pooling_params.py`; `vllm/tasks.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/pooler.py`; `vllm/entrypoints/llm.py`; `vllm/model_executor/layers/pooler/seqwise/methods.py`; `vllm/model_executor/layers/pooler/seqwise/poolers.py`; `vllm/model_executor/layers/pooler/tokwise/methods.py`; `vllm/model_executor/layers/pooler/tokwise/poolers.py`; `vllm/model_executor/models/bert.py` 等 20 个文件
  - tests: `tests/model_executor/test_model_load_with_params.py`; `tests/models/language/pooling/test_embedding.py`; `tests/models/language/pooling/test_mm_classifier_conversion.py`; `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`; `tests/models/language/pooling_mteb_test/mteb_score_utils.py`; `tests/models/language/pooling_mteb_test/test_baai.py`; `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py`; `tests/models/language/pooling_mteb_test/test_cross_encoder.py` 等 20 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `c8ed39b9d` - [Model] Reorganize pooling layers (#31973)

- 完整 hash: `c8ed39b9dd8efad4bed9547c52df7999c1735114`
- 时间/作者: 2026-01-09 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/CODEOWNERS`, `tests/model_executor/test_model_load_with_params.py`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/config/pooler.py`, `vllm/model_executor/layers/pooler.py`, `vllm/model_executor/layers/pooler/__init__.py`, `vllm/model_executor/layers/pooler/abstract.py`, `vllm/model_executor/layers/pooler/activations.py` 等 34 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/CODEOWNERS`
  - other: `vllm/v1/outputs.py`
  - runtime-model: `vllm/config/pooler.py`; `vllm/model_executor/layers/pooler.py`; `vllm/model_executor/layers/pooler/__init__.py`; `vllm/model_executor/layers/pooler/abstract.py`; `vllm/model_executor/layers/pooler/activations.py`; `vllm/model_executor/layers/pooler/common.py`; `vllm/model_executor/layers/pooler/seqwise/__init__.py`; `vllm/model_executor/layers/pooler/seqwise/heads.py` 等 30 个文件
  - tests: `tests/model_executor/test_model_load_with_params.py`; `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `700a5ad6c` - [MM Encoder]: Migrate legacy ViT `MultiHeadAttention` to new `MMEncoderAttention` interface (#30684)

- 完整 hash: `700a5ad6c616358f42db7d9b55e8bc9caa140ca5`
- 时间/作者: 2025-12-19 / Isotr0py
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_mha_attn.py`, `tests/v1/tpu/test_mha_attn.py`, `vllm/attention/layer.py`, `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/blip.py` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/aimv2.py`; `vllm/model_executor/models/blip.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/hunyuan_vision.py`; `vllm/model_executor/models/idefics2_vision_model.py`; `vllm/model_executor/models/intern_vit.py` 等 14 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/layers/mm_encoder_attention.py`; `vllm/attention/ops/vit_attn_wrappers.py`
  - tests: `tests/kernels/attention/test_attention.py`; `tests/kernels/attention/test_mha_attn.py`; `tests/v1/tpu/test_mha_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `cf3eacfe5` - Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389)

- 完整 hash: `cf3eacfe58fa9e745c2854782ada884a9f992cf7`
- 时间/作者: 2025-12-11 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `vllm/config/utils.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/afmoe.py` 等 83 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `benchmarks/kernels/benchmark_rope.py`
  - runtime-model: `vllm/config/utils.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/olmoe.py` 等 12 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e83b7e379` - Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199)

- 完整 hash: `e83b7e379c11bf136c1b96bc6a67b6d2207cfde4`
- 时间/作者: 2025-12-07 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py`, `tests/compile/test_fusion.py`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_pass_manager.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/distributed/test_kvlayout.py` 等 105 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/transcription.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/processor.py`; `vllm/v1/engine/async_llm.py` 等 12 个文件
  - runtime-model: `vllm/config/__init__.py`; `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/config/renderer.py`; `vllm/config/speculative.py`; `vllm/config/vllm.py`; `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py` 等 33 个文件
  - runtime-perf: `vllm/multimodal/cache.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/compile/distributed/test_sequence_parallelism.py`; `tests/compile/test_functionalization.py`; `tests/compile/test_fusion.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_pass_manager.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/distributed/test_kvlayout.py`; `tests/entrypoints/openai/test_chat_template.py` 等 56 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `27f4c2fd4` - [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)

- 完整 hash: `27f4c2fd46b99778d7ea19dfe7751fbaab615177`
- 时间/作者: 2025-12-07 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py`, `tests/compile/test_fusion.py`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_pass_manager.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/distributed/test_kvlayout.py` 等 105 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/transcription.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/processor.py`; `vllm/v1/engine/async_llm.py` 等 12 个文件
  - runtime-model: `vllm/config/__init__.py`; `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/config/renderer.py`; `vllm/config/speculative.py`; `vllm/config/vllm.py`; `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py` 等 33 个文件
  - runtime-perf: `vllm/multimodal/cache.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/compile/distributed/test_sequence_parallelism.py`; `tests/compile/test_functionalization.py`; `tests/compile/test_fusion.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_pass_manager.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/distributed/test_kvlayout.py`; `tests/entrypoints/openai/test_chat_template.py` 等 56 个文件
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

### Commit `430dd4d9e` - [Attention] Remove imports from `vllm/attention/__init__.py` (#29342)

- 完整 hash: `430dd4d9eb7e342e28012351df06d93892f86741`
- 时间/作者: 2025-11-26 / Matthew Bonanni
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/kernels/utils.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_utils.py`, `vllm/attention/__init__.py`, `vllm/attention/backends/abstract.py` 等 96 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`
  - other: `vllm/compilation/fusion_attn.py`; `vllm/compilation/qk_norm_rope_fusion.py`; `vllm/v1/kv_offload/cpu.py`; `vllm/v1/kv_offload/spec.py`
  - runtime-model: `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bloom.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/attention/__init__.py`; `vllm/attention/backends/abstract.py`; `vllm/attention/layer.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py` 等 20 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/kernels/utils.py`; `tests/v1/worker/test_gpu_model_runner.py`; `tests/v1/worker/test_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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
