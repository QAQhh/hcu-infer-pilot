# vllm GLM-4.6/4.7 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `tests/reasoning/test_glm4_moe_reasoning_parser.py` | `d9ab1ad9d` |
| `tests/tool_parsers/test_glm4_moe_tool_parser.py` | `78c1f9e5c`, `fefce4980`, `ed586e772` |
| `vllm/model_executor/models/glm4_moe.py` | `0f6b9a199`, `110bbdd5c`, `f1a7696f7`, `df7041633`, `dcd80206b`, `1f33e38e8`, `482914849`, `4e67a8f61`, `8a7a41437`, `cf3eacfe5`, `e10c84e06`, `430dd4d9e`, ... (15 total) |
| `vllm/model_executor/models/glm4_moe_lite.py` | `df7041633`, `dcd80206b`, `71832ba71` |
| `vllm/model_executor/models/glm4_moe_lite_mtp.py` | `df7041633`, `dcd80206b`, `71832ba71` |
| `vllm/model_executor/models/glm4_moe_mtp.py` | `dc027d74e`, `df7041633`, `dcd80206b`, `71832ba71`, `600aaab8d`, `0dd63639b`, `d111bc53a`, `482914849`, `ab01cd14e`, `97d1c9930`, `d3ade61e4`, `e50c45467` |
| `vllm/reasoning/glm4_moe_reasoning_parser.py` | `0202971a4`, `0d4044edd`, `d9ab1ad9d`, `e261d37c9` |
| `vllm/tool_parsers/glm47_moe_tool_parser.py` | `8a7a41437` |
| `vllm/tool_parsers/glm4_moe_tool_parser.py` | `a52d1396a`, `fefce4980`, `02dbb933c`, `aa7e83605`, `2a1776b7a` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 40
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-16 | `0f6b9a199` | 性能/后端优化 | perf: GLM4.7增加MOE调用rmsQuant, fix: 修掉fused_moe向后传递None导致的报错 | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py` |
| 2026-03-06 | `110bbdd5c` | 性能/后端优化 | [perf]glm4_moe模型适配rmsquant和silu_quant融合算子 | `vllm/envs.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/layers/linear.py` |
| 2026-03-06 | `f1a7696f7` | 性能/后端优化 | [perf]添加Module支持split qkv+rmsnorm+rope+kvcache融合算子，GLM4_MOE完成适配 | `vllm/attention/layer.py`, `vllm/config/compilation.py`, `vllm/envs.py` |
| 2026-02-13 | `dc027d74e` | 性能/后端优化 | [feat]支持glm4_moe_mtp使用torch compile，实现mtp cudagraph模式 | `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-05 | `78c1f9e5c` | 性能/后端优化 | sync v0.15.1(tests) | `tests/compile/fullgraph/test_basic_correctness.py`, `tests/compile/test_config.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-23 | `586a57ad7` | 性能/后端优化 | fix: Add glm4_moe_lite to MLA detection (#32614) | `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/platforms/cuda.py`, `vllm/transformers_utils/model_arch_config_convertor.py` |
| 2026-01-19 | `71832ba71` | 性能/后端优化 | [GLM-4.7] GLM Model support for GLM-Lite (#31386) | `benchmarks/kernels/benchmark_moe.py`, `benchmarks/kernels/benchmark_moe_permute_unpermute.py`, `docs/features/tool_calling.md` |
| 2026-01-15 | `a52d1396a` | 性能/后端优化 | fix: avoid crash on zero-arg tool calls in glm4 parser (#32321) | `vllm/tool_parsers/glm4_moe_tool_parser.py` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-12 | `600aaab8d` | 性能/后端优化 | [Model] Remove incorrect `SupportsPP` from MTP models (#32150) | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-10 | `0dd63639b` | 性能/后端优化 | [MTP][GLM][Bugfix] Fixed .weight_scale loading logic that dropped MTP prediction accuracy with fp8+mtp (#32101) | `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-07 | `e5173d3ba` | 性能/后端优化 | [Bugfix] Remove the num_hidden_layers override for glm4_moe (#31745) | `vllm/config/speculative.py` |
| 2026-01-07 | `d111bc53a` | 性能/后端优化 | [Bugfix][MTP] Fix GLM4 MoE fp8 loading with MTP on (#31757) | `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-07 | `1f33e38e8` | 性能/后端优化 | [Model] Cleanup: Remove redundant manual definition of `make_empty_intermediate_tensors` in GLM-4-MoE (#31869) | `vllm/model_executor/models/glm4_moe.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `4e67a8f61` | 性能/后端优化 | [Bugfix] Fix GLM-4 MoE router logits dtype for data parallel chunking (#31055) | `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/glm4_moe.py` |
| 2026-01-06 | `0202971a4` | 性能/后端优化 | [Frontend] Support GLM-4.5 / GLM-4.7 with enable_thinking: false (#31788) | `vllm/reasoning/deepseek_v3_reasoning_parser.py`, `vllm/reasoning/glm4_moe_reasoning_parser.py`, `vllm/reasoning/holo2_reasoning_parser.py` |
| 2026-01-05 | `02dbb933c` | 性能/后端优化 | Fix GLM-4.6v flash tool calling in transformers 5.x (#31622) | `examples/tool_chat_template_glm4.jinja`, `vllm/tool_parsers/glm4_moe_tool_parser.py` |
| 2026-01-04 | `0d4044edd` | 性能/后端优化 | fix no think of GLM-4.5 / GLM-4.7 (#31449) | `vllm/reasoning/glm4_moe_reasoning_parser.py` |
| 2025-12-28 | `b9793e6a8` | 性能/后端优化 | Add Fused MoE Triton kernels for GLM-4.5-Air, GLM-4.5v, GLM-4.6v on 2x RTX Pro 6000 (#31407) | `vllm/model_executor/layers/fused_moe/configs/E=128,N=704,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Workstation_Edition,dtype=fp8_w8a8.json`, `vllm/model_executor/layers/fused_moe/configs/E=129,N=704,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Workstation_Edition,dtype=fp8_w8a8.json` |
| 2025-12-20 | `8a7a41437` | 性能/后端优化 | GLM-4.7 Tool Parser and Doc Update (#30876) | `docs/features/tool_calling.md`, `docs/models/supported_models.md`, `vllm/model_executor/models/glm4_moe.py` |
| 2025-12-18 | `aa7e83605` | 性能/后端优化 | [Bugfix] Fix Unicode issues in GLM-4 tool calling (#30920) | `vllm/tool_parsers/glm4_moe_tool_parser.py` |
| 2025-12-15 | `ed586e772` | 性能/后端优化 | [Refactor] [3/N] Move tool parser tests and run on CPU (#30693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/misc.yaml` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-04 | `e10c84e06` | 性能/后端优化 | Access `partial_rotary_factor` from `rope_parameters` (#29966) | `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/apertus.py` |
| 2025-12-02 | `653591d5e` | 性能/后端优化 | [Chore] Move tokenizer initialization methods (#29793) | `benchmarks/benchmark_prefix_caching.py`, `benchmarks/benchmark_serving_structured_output.py`, `tests/compile/test_dynamic_shapes_compilation.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-21 | `2092ce8c3` | 性能/后端优化 | Tool Call Parser logs should not contain user input / model output except on DEBUG (#29160) | `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/qwen3coder_tool_parser.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-17 | `ab01cd14e` | 性能/后端优化 | [BugFix] Fix glm4_moe_mtp load weights bug (#28805) | `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `d3ade61e4` | 性能/后端优化 | [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint. (#27597) | `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2025-11-08 | `d9ab1ad9d` | 性能/后端优化 | `reasoning_content` -> `reasoning` (#27752) | `docs/features/reasoning_outputs.md`, `docs/features/structured_outputs.md`, `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py` |
| 2025-11-05 | `e50c45467` | 性能/后端优化 | [BugFix] Support EP/DP + EPLB with MTP (#25311) | `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py` |
| 2025-11-05 | `e261d37c9` | 性能/后端优化 | [Refactor] Lazy-loaded reasoning_parser (#28092) | `docs/features/reasoning_outputs.md`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `vllm/engine/arg_utils.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |

## 逐 Commit 审计卡

### Commit `0f6b9a199` - perf: GLM4.7增加MOE调用rmsQuant, fix: 修掉fused_moe向后传递None导致的报错

- 完整 hash: `0f6b9a199ece04a6c916dc1aa93e2f138c5f908b`
- 时间/作者: 2026-03-16 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`, `vllm/model_executor/models/glm4_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/shared_fused_moe.py`; `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`; `vllm/model_executor/models/glm4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `110bbdd5c` - [perf]glm4_moe模型适配rmsquant和silu_quant融合算子

- 完整 hash: `110bbdd5c20236320d89773bb7c224a38e766171`
- 时间/作者: 2026-03-06 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/envs.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`, `vllm/model_executor/models/glm4_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/model_executor/layers/layernorm.py`; `vllm/model_executor/layers/linear.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`; `vllm/model_executor/models/glm4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f1a7696f7` - [perf]添加Module支持split qkv+rmsnorm+rope+kvcache融合算子，GLM4_MOE完成适配

- 完整 hash: `f1a7696f7fbe15a1a48840a1cd7840d705112b23`
- 时间/作者: 2026-03-06 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/layer.py`, `vllm/config/compilation.py`, `vllm/envs.py`, `vllm/model_executor/models/glm4_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/config/compilation.py`
  - runtime-perf: `vllm/attention/layer.py`; `vllm/model_executor/models/glm4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `dc027d74e` - [feat]支持glm4_moe_mtp使用torch compile，实现mtp cudagraph模式

- 完整 hash: `dc027d74eaaf040aab177827d48970174f73f4ec`
- 时间/作者: 2026-02-13 / 王敏
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/glm4_moe_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `78c1f9e5c` - sync v0.15.1(tests)

- 完整 hash: `78c1f9e5c138765b1f949f5b2cd2209f704a0e3b`
- 时间/作者: 2026-02-05 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `tests/compile/fullgraph/test_basic_correctness.py`, `tests/compile/test_config.py`, `tests/entrypoints/openai/test_chat_error.py`, `tests/entrypoints/openai/test_chat_template.py`, `tests/entrypoints/pooling/openai/test_embedding.py`, `tests/entrypoints/pooling/openai/test_score.py`, `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_cache.py` 等 35 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `tests/compile/fullgraph/test_basic_correctness.py`; `tests/compile/test_config.py`; `tests/entrypoints/openai/test_chat_error.py`; `tests/entrypoints/openai/test_chat_template.py`; `tests/entrypoints/pooling/openai/test_embedding.py`; `tests/entrypoints/pooling/openai/test_score.py`; `tests/kernels/attention/test_attention.py`; `tests/kernels/attention/test_cache.py` 等 35 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

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

### Commit `586a57ad7` - fix: Add glm4_moe_lite to MLA detection (#32614)

- 完整 hash: `586a57ad7ede5c5132a70d021fc48fe05b10f5c3`
- 时间/作者: 2026-01-23 / Markus / Mark
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/platforms/cuda.py`, `vllm/transformers_utils/model_arch_config_convertor.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/transformers_utils/model_arch_config_convertor.py`
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`; `vllm/platforms/cuda.py`; `vllm/v1/attention/backends/mla/flashinfer_mla.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `71832ba71` - [GLM-4.7] GLM Model support for GLM-Lite (#31386)

- 完整 hash: `71832ba71e77c01a1d249e014384522b46813749`
- 时间/作者: 2026-01-19 / Yuxuan Zhang
- 自动分类: 性能/后端优化
- 主要文件: `benchmarks/kernels/benchmark_moe.py`, `benchmarks/kernels/benchmark_moe_permute_unpermute.py`, `docs/features/tool_calling.md`, `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/glm4_moe_lite_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmarks/kernels/benchmark_moe.py`; `benchmarks/kernels/benchmark_moe_permute_unpermute.py`; `docs/features/tool_calling.md`
  - runtime-model: `vllm/config/speculative.py`; `vllm/model_executor/models/registry.py`
  - runtime-perf: `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py`; `vllm/model_executor/models/glm4_moe_mtp.py`
  - tests: `tests/models/registry.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a52d1396a` - fix: avoid crash on zero-arg tool calls in glm4 parser (#32321)

- 完整 hash: `a52d1396a7108d9bb8a7afdadb524d72c59fff5c`
- 时间/作者: 2026-01-15 / seeksky
- 自动分类: 性能/后端优化
- 主要文件: `vllm/tool_parsers/glm4_moe_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
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

### Commit `600aaab8d` - [Model] Remove incorrect `SupportsPP` from MTP models (#32150)

- 完整 hash: `600aaab8d626301f4dbfcd812ccf47b3e8d81ac9`
- 时间/作者: 2026-01-12 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`, `vllm/model_executor/models/longcat_flash_mtp.py`, `vllm/model_executor/models/openpangu_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/ernie_mtp.py`; `vllm/model_executor/models/openpangu_mtp.py`; `vllm/model_executor/models/qwen3_next_mtp.py`
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/longcat_flash_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0dd63639b` - [MTP][GLM][Bugfix] Fixed .weight_scale loading logic that dropped MTP prediction accuracy with fp8+mtp (#32101)

- 完整 hash: `0dd63639be24c67a0bccc9e3b0f0fd6ab039455d`
- 时间/作者: 2026-01-10 / Andy Liu
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/glm4_moe_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e5173d3ba` - [Bugfix] Remove the num_hidden_layers override for glm4_moe (#31745)

- 完整 hash: `e5173d3bac054edc1b556005d804a5acf94eaf15`
- 时间/作者: 2026-01-07 / Andy Liu
- 自动分类: 性能/后端优化
- 主要文件: `vllm/config/speculative.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/config/speculative.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d111bc53a` - [Bugfix][MTP] Fix GLM4 MoE fp8 loading with MTP on (#31757)

- 完整 hash: `d111bc53ad2fbb5f28671019d21f5f753436e46d`
- 时间/作者: 2026-01-07 / Andy Liu
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/glm4_moe_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1f33e38e8` - [Model] Cleanup: Remove redundant manual definition of `make_empty_intermediate_tensors` in GLM-4-MoE (#31869)

- 完整 hash: `1f33e38e81a1b29bb4261a5e4e1fa430198b251a`
- 时间/作者: 2026-01-07 / maang
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/glm4_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/models/glm4_moe.py`
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

### Commit `4e67a8f61` - [Bugfix] Fix GLM-4 MoE router logits dtype for data parallel chunking (#31055)

- 完整 hash: `4e67a8f616f4f202fd7a549978914f398a738d49`
- 时间/作者: 2026-01-06 / Yakine Tahtah
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/glm4_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/models/glm4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0202971a4` - [Frontend] Support GLM-4.5 / GLM-4.7 with enable_thinking: false (#31788)

- 完整 hash: `0202971a4842e129027b0931870112e45ee9ad65`
- 时间/作者: 2026-01-06 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `vllm/reasoning/deepseek_v3_reasoning_parser.py`, `vllm/reasoning/glm4_moe_reasoning_parser.py`, `vllm/reasoning/holo2_reasoning_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/holo2_reasoning_parser.py`
  - runtime-perf: `vllm/reasoning/glm4_moe_reasoning_parser.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `02dbb933c` - Fix GLM-4.6v flash tool calling in transformers 5.x (#31622)

- 完整 hash: `02dbb933cb28eb2b0f05dd491f20273d2f84e517`
- 时间/作者: 2026-01-05 / baonudesifeizhai
- 自动分类: 性能/后端优化
- 主要文件: `examples/tool_chat_template_glm4.jinja`, `vllm/tool_parsers/glm4_moe_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `examples/tool_chat_template_glm4.jinja`
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0d4044edd` - fix no think of GLM-4.5 / GLM-4.7 (#31449)

- 完整 hash: `0d4044edd85de30d7d4558aeea4d1e95c7c556d6`
- 时间/作者: 2026-01-04 / Yuxuan Zhang
- 自动分类: 性能/后端优化
- 主要文件: `vllm/reasoning/glm4_moe_reasoning_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/reasoning/glm4_moe_reasoning_parser.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b9793e6a8` - Add Fused MoE Triton kernels for GLM-4.5-Air, GLM-4.5v, GLM-4.6v on 2x RTX Pro 6000 (#31407)

- 完整 hash: `b9793e6a8c30bc42f35d2a1eac919284aea27f76`
- 时间/作者: 2025-12-28 / Mamy Ratsimbazafy
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/configs/E=128,N=704,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Workstation_Edition,dtype=fp8_w8a8.json`, `vllm/model_executor/layers/fused_moe/configs/E=129,N=704,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Workstation_Edition,dtype=fp8_w8a8.json`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=704,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Workstation_Edition,dtype=fp8_w8a8.json`; `vllm/model_executor/layers/fused_moe/configs/E=129,N=704,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Workstation_Edition,dtype=fp8_w8a8.json`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8a7a41437` - GLM-4.7 Tool Parser and Doc Update (#30876)

- 完整 hash: `8a7a414374909bc176cb165e8031e0e92948d07e`
- 时间/作者: 2025-12-20 / Yuxuan Zhang
- 自动分类: 性能/后端优化
- 主要文件: `docs/features/tool_calling.md`, `docs/models/supported_models.md`, `vllm/model_executor/models/glm4_moe.py`, `vllm/tool_parsers/__init__.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/tool_calling.md`; `docs/models/supported_models.md`
  - other: `vllm/tool_parsers/__init__.py`
  - runtime-perf: `vllm/model_executor/models/glm4_moe.py`; `vllm/tool_parsers/glm47_moe_tool_parser.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `aa7e83605` - [Bugfix] Fix Unicode issues in GLM-4 tool calling (#30920)

- 完整 hash: `aa7e8360559e639f201f08a4deee490af332b22c`
- 时间/作者: 2025-12-18 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `vllm/tool_parsers/glm4_moe_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/tool_parsers/glm4_moe_tool_parser.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `e10c84e06` - Access `partial_rotary_factor` from `rope_parameters` (#29966)

- 完整 hash: `e10c84e06af7264d5c0b3e7ec5604ada2eee7094`
- 时间/作者: 2025-12-04 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/falcon_h1.py`, `vllm/model_executor/models/glm.py` 等 21 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/falcon_h1.py`; `vllm/model_executor/models/glm.py`; `vllm/model_executor/models/glm4.py`; `vllm/model_executor/models/gpt_neox.py` 等 18 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/glm4_moe.py`
  - tests: `tests/kernels/core/test_mrope.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `2092ce8c3` - Tool Call Parser logs should not contain user input / model output except on DEBUG (#29160)

- 完整 hash: `2092ce8c39a4f01a93dcb32d3c92d05586507e7c`
- 时间/作者: 2025-11-21 / sfbemerk
- 自动分类: 性能/后端优化
- 主要文件: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`, `vllm/entrypoints/openai/tool_parsers/qwen3coder_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/qwen3coder_tool_parser.py`
  - runtime-perf: `vllm/entrypoints/openai/tool_parsers/glm4_moe_tool_parser.py`
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

### Commit `ab01cd14e` - [BugFix] Fix glm4_moe_mtp load weights bug (#28805)

- 完整 hash: `ab01cd14e5e2ef65549b459d0a2bf3a2540c9f3f`
- 时间/作者: 2025-11-17 / wuyaoxuehun
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/glm4_moe_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`
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

### Commit `d3ade61e4` - [Model] fix glm4_moe_mtp load weights with GLM-4.6 checkpoint. (#27597)

- 完整 hash: `d3ade61e429fcae40829587244ced9c553120703`
- 时间/作者: 2025-11-12 / wuyaoxuehun
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/glm4_moe_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d9ab1ad9d` - `reasoning_content` -> `reasoning` (#27752)

- 完整 hash: `d9ab1ad9d1be96885f4387a33a3a82233c009ce9`
- 时间/作者: 2025-11-08 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `docs/features/reasoning_outputs.md`, `docs/features/structured_outputs.md`, `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py`, `examples/online_serving/openai_chat_completion_with_reasoning.py`, `examples/online_serving/openai_chat_completion_with_reasoning_streaming.py`, `examples/online_serving/streamlit_openai_chatbot_webserver.py`, `examples/online_serving/structured_outputs/structured_outputs.py`, `tests/entrypoints/openai/test_chat_with_tool_reasoning.py` 等 46 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/reasoning_outputs.md`; `docs/features/structured_outputs.md`; `examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py`; `examples/online_serving/openai_chat_completion_with_reasoning.py`; `examples/online_serving/openai_chat_completion_with_reasoning_streaming.py`; `examples/online_serving/streamlit_openai_chatbot_webserver.py`; `examples/online_serving/structured_outputs/structured_outputs.py`
  - other: `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/basic_parsers.py`; `vllm/reasoning/deepseek_r1_reasoning_parser.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/ernie45_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/granite_reasoning_parser.py`; `vllm/reasoning/hunyuan_a13b_reasoning_parser.py` 等 15 个文件
  - runtime-model: `vllm/entrypoints/harmony_utils.py`; `vllm/entrypoints/openai/protocol.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/serving_responses.py`; `vllm/entrypoints/openai/tool_parsers/qwen3xml_tool_parser.py`
  - runtime-perf: `vllm/reasoning/glm4_moe_reasoning_parser.py`
  - tests: `tests/entrypoints/openai/test_chat_with_tool_reasoning.py`; `tests/entrypoints/openai/test_completion_with_function_calling.py`; `tests/entrypoints/openai/test_run_batch.py`; `tests/reasoning/test_base_thinking_reasoning_parser.py`; `tests/reasoning/test_deepseekr1_reasoning_parser.py`; `tests/reasoning/test_deepseekv3_reasoning_parser.py`; `tests/reasoning/test_ernie45_reasoning_parser.py`; `tests/reasoning/test_glm4_moe_reasoning_parser.py` 等 18 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e50c45467` - [BugFix] Support EP/DP + EPLB with MTP (#25311)

- 完整 hash: `e50c45467215f96068d95736b08d8a25f624e67d`
- 时间/作者: 2025-11-05 / Ilya Markov
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py`, `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/ernie45_moe.py` 等 27 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - other: `vllm/v1/spec_decode/medusa.py`
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`; `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llama4.py`; `vllm/model_executor/models/llama4_eagle.py` 等 17 个文件
  - runtime-perf: `vllm/distributed/eplb/eplb_state.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/qwen3_moe.py`; `vllm/model_executor/models/transformers/moe.py`
  - tests: `tests/distributed/test_eplb_spec_decode.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e261d37c9` - [Refactor] Lazy-loaded reasoning_parser (#28092)

- 完整 hash: `e261d37c9a5e88a6c86d32decf39f1fab7ca1f2c`
- 时间/作者: 2025-11-05 / Chauncey
- 自动分类: 性能/后端优化
- 主要文件: `docs/features/reasoning_outputs.md`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `vllm/engine/arg_utils.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/openai/run_batch.py`, `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/reasoning/__init__.py`, `vllm/reasoning/abs_reasoning_parsers.py` 等 21 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/reasoning_outputs.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/reasoning/__init__.py`; `vllm/reasoning/abs_reasoning_parsers.py`; `vllm/reasoning/deepseek_r1_reasoning_parser.py`; `vllm/reasoning/deepseek_v3_reasoning_parser.py`; `vllm/reasoning/ernie45_reasoning_parser.py`; `vllm/reasoning/gptoss_reasoning_parser.py`; `vllm/reasoning/granite_reasoning_parser.py` 等 15 个文件
  - runtime-model: `vllm/entrypoints/openai/api_server.py`; `vllm/entrypoints/openai/run_batch.py`; `vllm/entrypoints/openai/tool_parsers/__init__.py`
  - runtime-perf: `vllm/reasoning/glm4_moe_reasoning_parser.py`
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py`
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
