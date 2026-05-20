# vllm Llama 4 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `examples/tool_chat_template_llama4_json.jinja` | 无直接提交 |
| `examples/tool_chat_template_llama4_pythonic.jinja` | 无直接提交 |
| `tests/entrypoints/openai/tool_parsers/test_llama4_pythonic_tool_parser.py` | `fefce4980`, `2a1776b7a`, `34a984274` |
| `tests/models/multimodal/processing/test_llama4.py` | `e83b7e379`, `27f4c2fd4`, `34a8559be`, `68ffbca7e` |
| `tests/models/multimodal/processing/test_mllama4.py` | `90db5b31e`, `252c01101`, `16484d394`, `f5f51e593`, `e83b7e379`, `27f4c2fd4` |
| `vllm/model_executor/layers/rotary_embedding/llama4_vision_rope.py` | `ea6d067a2`, `b798e39f9` |
| `vllm/model_executor/models/llama4.py` | `1fb648bf1`, `2612ba928`, `482914849`, `cf3eacfe5`, `430dd4d9e`, `dc45efc8e`, `a8b70304d`, `e50c45467` |
| `vllm/model_executor/models/llama4_eagle.py` | `962d70381`, `93c8672ce`, `e439c784f`, `97d1c9930`, `e50c45467` |
| `vllm/model_executor/models/mllama4.py` | `df7041633`, `dcd80206b`, `2b8a38b6d`, `4753f3bf6`, `9ea07b41d`, `ea6d067a2`, `2612ba928`, `482914849`, `700a5ad6c`, `cf3eacfe5`, `c46b932df`, `a8b70304d`, ... (15 total) |
| `vllm/tool_parsers/llama4_pythonic_tool_parser.py` | `fefce4980`, `2a1776b7a` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 47
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-23 | `1fb648bf1` | 性能/后端优化 | [Bugfix] Fix FP8 MoE EP Weight Loading for ModelOpt Llama4 (#32886) | `vllm/model_executor/models/llama4.py` |
| 2026-01-22 | `2b8a38b6d` | 性能/后端优化 | [Model] Extend `collect_children` and `no_init_weights` contexts (#32757) | `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py` |
| 2026-01-21 | `42135d689` | 性能/后端优化 | [MoE Refactor] Oracle Select FP8+NVFP4 Kernels In Priority (#32414) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py` |
| 2026-01-20 | `4753f3bf6` | 性能/后端优化 | [Model] Use context managers for encoder- and LM-only mode (#32605) | `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/config/multimodal.py` |
| 2026-01-15 | `31c29257c` | 性能/后端优化 | [MoE Refactor][17/N] Apply Refactor to Bf16 (#31827) | `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-14 | `90db5b31e` | 模型支持/运行时入口 | [Refactor] Move top-level dummy data generation to registry (#32310) | `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_processing.py`, `vllm/multimodal/processing.py` |
| 2026-01-13 | `252c01101` | 模型支持/运行时入口 | [Refactor] Remove `MultiModalProfiler` (#32254) | `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_processing.py`, `vllm/multimodal/profiling.py` |
| 2026-01-13 | `fefce4980` | 性能/后端优化 | [Refactor] [6/N] to simplify the vLLM openai chat_completion serving architecture (#32240) | `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/test_chat_error.py` |
| 2026-01-09 | `ea6d067a2` | 模型支持/运行时入口 | [Misc][LLaMa4] Compile LLaMa Vision Encoder (#30709) | `tests/compile/fullgraph/test_multimodal_compile.py`, `vllm/config/compilation.py`, `vllm/model_executor/layers/attention/mm_encoder_attention.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-07 | `5dcd7ef1f` | 性能/后端优化 | [MoE Refactor][15/N] Apply Refactor to Fp8 (#31415) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `d3e477c01` | 性能/后端优化 | [MoE Refactor] Add Temporary Integration Tests - H100/B200 (#31759) | `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml` |
| 2025-12-19 | `700a5ad6c` | 性能/后端优化 | [MM Encoder]: Migrate legacy ViT `MultiHeadAttention` to new `MMEncoderAttention` interface (#30684) | `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_mha_attn.py`, `tests/v1/tpu/test_mha_attn.py` |
| 2025-12-16 | `16484d394` | 性能/后端优化 | [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475) | `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py` |
| 2025-12-16 | `f5f51e593` | 性能/后端优化 | [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475) | `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py` |
| 2025-12-15 | `2a1776b7a` | 性能/后端优化 | [Refactor] [2/N] Move tool parsers into the vLLM main directory (#30675) | `docs/features/tool_calling.md`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/tool_parsers/test_gigachat3_tool_parser.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `e83b7e379` | 调度/缓存/PD | Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `27f4c2fd4` | 调度/缓存/PD | [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-05 | `962d70381` | 缺陷修复 | [Bugfix][llama4_eagle] Fix missing 'lm_head' attribute (#29926) | `tests/v1/e2e/test_spec_decode.py`, `vllm/model_executor/models/llama4_eagle.py` |
| 2025-12-04 | `bcf43ab1f` | 性能/后端优化 | [CI/Build][AMD] Add Llama4 Maverick FP8 to AMD CI (#28695) | `.buildkite/lm-eval-harness/configs/Meta-Llama-4-Maverick-17B-128E-Instruct-FP8.yaml`, `.buildkite/lm-eval-harness/configs/models-large-rocm.txt`, `.buildkite/lm-eval-harness/test_lm_eval_correctness.py` |
| 2025-12-02 | `9057fc2f1` | 缺陷修复 | [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-02 | `5e5646e20` | 缺陷修复 | [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-02 | `34a8559be` | 调度/缓存/PD | [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py` |
| 2025-12-02 | `68ffbca7e` | 调度/缓存/PD | [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py` |
| 2025-11-29 | `34a984274` | 性能/后端优化 | [Misc] Refactor tokenizer interface (#29693) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `benchmarks/backend_request_func.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-20 | `ed6ae1e36` | 性能/后端优化 | [AITER] [ROCm] Fix crash when loading llama4 model with old aiter version installed, fallback to forward_native implementation (#29124) | `vllm/v1/sample/ops/topk_topp_sampler.py` |
| 2025-11-20 | `93c8672ce` | 缺陷修复 | [Bugfix] Fix spec decode memory regression after #28549 (#28819) | `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/llama4_eagle.py`, `vllm/model_executor/models/llama_eagle.py` |
| 2025-11-20 | `dc45efc8e` | 缺陷修复 | [BugFix] Fix Llama4 Pipeline Parallelism Assert Error (#28577) | `vllm/model_executor/models/llama4.py` |
| 2025-11-19 | `61728cd1d` | 性能/后端优化 | Re-enable FlashInfer for Llama4 on Blackwell in e2e fusion tests (#28966) | `.buildkite/test-pipeline.yaml`, `tests/compile/distributed/test_fusions_e2e.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-17 | `3380ed5e1` | 模型支持/运行时入口 | [Doc] Add llama4 LoRA tag (#28825) | `docs/models/supported_models.md` |
| 2025-11-15 | `e439c784f` | 调度/缓存/PD | Add support for Eagle with separate lm-head and embed_tokens layers (#28549) | `tests/v1/spec_decode/test_eagle.py`, `tests/v1/spec_decode/test_mtp.py`, `vllm/model_executor/models/deepseek_eagle.py` |
| 2025-11-15 | `1ec978c20` | 性能/后端优化 | [Kernel][Moe Configs] llama4 maverick fp8 moe config tp8 on mi325 (#28709) | `vllm/model_executor/layers/fused_moe/configs/E=128,N=1024,device_name=AMD_Instinct_MI325X,dtype=fp8_w8a8.json` |
| 2025-11-14 | `964d65dee` | 模型支持/运行时入口 | LLaMA4 LoRA Adapter Enablement (#28602) | `vllm/model_executor/models/mllama4.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-06 | `7a8375f8a` | 模型支持/运行时入口 | Add llama 4 scaling support (#28145) | `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`, `vllm/model_executor/models/llama.py` |
| 2025-11-05 | `e50c45467` | 性能/后端优化 | [BugFix] Support EP/DP + EPLB with MTP (#25311) | `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py` |
| 2025-11-05 | `6e97eccf5` | 性能/后端优化 | [XPU] Enable custom routing functions in IPEX for Llama4 (#28004) | `vllm/model_executor/layers/fused_moe/layer.py` |
| 2025-11-04 | `c02fccdbd` | 性能/后端优化 | [Refactor] Lazy import tool_parser (#27974) | `docs/features/tool_calling.md`, `tests/tool_use/test_deepseekv31_tool_parser.py`, `tests/tool_use/test_ernie45_moe_tool_parser.py` |
| 2025-10-30 | `b798e39f9` | 缺陷修复 | [XPU][bugfix] fix rope for llama4 and deepseek (#25145) | `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`, `vllm/model_executor/layers/rotary_embedding/llama4_vision_rope.py` |

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

### Commit `1fb648bf1` - [Bugfix] Fix FP8 MoE EP Weight Loading for ModelOpt Llama4 (#32886)

- 完整 hash: `1fb648bf107e9c24e7f99671c77406d126506d7a`
- 时间/作者: 2026-01-23 / baonudesifeizhai
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/llama4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/llama4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `42135d689` - [MoE Refactor] Oracle Select FP8+NVFP4 Kernels In Priority (#32414)

- 完整 hash: `42135d689830c0e764d925b6454bc68ba6c6cab4`
- 时间/作者: 2026-01-21 / Robert Shaw
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`, `benchmarks/kernels/benchmark_moe.py`, `docs/design/moe_kernel_features.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_silu_mul_quant_fusion.py` 等 82 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`; `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`; `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`; `benchmarks/kernels/benchmark_moe.py`; `docs/design/moe_kernel_features.md`
  - other: `vllm/compilation/fusion.py`; `vllm/compilation/fusion_attn.py`; `vllm/compilation/matcher_utils.py`
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`; `vllm/model_executor/warmup/deep_gemm_warmup.py`
  - runtime-perf: `tools/vllm-rocm/pin_rocm_dependencies.py`; `vllm/compilation/activation_quant_fusion.py`; `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/fallback.py`; `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py` 等 38 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_silu_mul_quant_fusion.py`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-trtllm.yaml` 等 33 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4753f3bf6` - [Model] Use context managers for encoder- and LM-only mode (#32605)

- 完整 hash: `4753f3bf69a2b975361afa7c49e8d948047613f6`
- 时间/作者: 2026-01-20 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `examples/online_serving/disaggregated_encoder/README.md`, `vllm/config/model.py`, `vllm/config/multimodal.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/llava.py` 等 21 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `examples/online_serving/disaggregated_encoder/README.md`
  - other: `vllm/engine/arg_utils.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llava.py`; `vllm/model_executor/models/mistral3.py`; `vllm/model_executor/models/mllama4.py` 等 18 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `31c29257c` - [MoE Refactor][17/N] Apply Refactor to Bf16 (#31827)

- 完整 hash: `31c29257c852c429a655dd35a1c373ccd46f97da`
- 时间/作者: 2026-01-15 / Yongye Zhu
- 自动分类: 性能/后端优化
- 主要文件: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-triton.yaml` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-triton.yaml` 等 10 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `90db5b31e` - [Refactor] Move top-level dummy data generation to registry (#32310)

- 完整 hash: `90db5b31e4eeb8fc8bfb3260791bf795fda4f633`
- 时间/作者: 2026-01-14 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_processing.py`, `vllm/multimodal/processing.py`, `vllm/multimodal/profiling.py`, `vllm/multimodal/registry.py`, `vllm/v1/worker/gpu_model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/processing.py`; `vllm/multimodal/profiling.py`; `vllm/multimodal/registry.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
  - tests: `tests/models/multimodal/processing/test_mllama4.py`; `tests/multimodal/test_processing.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `252c01101` - [Refactor] Remove `MultiModalProfiler` (#32254)

- 完整 hash: `252c011012658490c2e970c5bc739a84bf5759c0`
- 时间/作者: 2026-01-13 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_processing.py`, `vllm/multimodal/profiling.py`, `vllm/multimodal/registry.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/profiling.py`; `vllm/multimodal/registry.py`
  - tests: `tests/models/multimodal/processing/test_mllama4.py`; `tests/multimodal/test_processing.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

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

### Commit `ea6d067a2` - [Misc][LLaMa4] Compile LLaMa Vision Encoder (#30709)

- 完整 hash: `ea6d067a2aebc32976f4ebfc0ab2546fbaa91c42`
- 时间/作者: 2026-01-09 / Lucas Kabela
- 自动分类: 模型支持/运行时入口
- 主要文件: `tests/compile/fullgraph/test_multimodal_compile.py`, `vllm/config/compilation.py`, `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/layers/rotary_embedding/llama4_vision_rope.py`, `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/mllama4.py`, `vllm/v1/attention/ops/vit_attn_wrappers.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/config/compilation.py`; `vllm/model_executor/layers/rotary_embedding/llama4_vision_rope.py`; `vllm/model_executor/models/llama.py`; `vllm/model_executor/models/mllama4.py`
  - runtime-perf: `vllm/model_executor/layers/attention/mm_encoder_attention.py`; `vllm/v1/attention/ops/vit_attn_wrappers.py`
  - tests: `tests/compile/fullgraph/test_multimodal_compile.py`
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

### Commit `5dcd7ef1f` - [MoE Refactor][15/N] Apply Refactor to Fp8 (#31415)

- 完整 hash: `5dcd7ef1f219068e6b6be5b614bc43978f028651`
- 时间/作者: 2026-01-07 / Robert Shaw
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`, `benchmarks/kernels/benchmark_moe.py`, `docs/design/moe_kernel_features.md`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ht.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml` 等 38 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`; `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`; `benchmarks/kernels/benchmark_moe.py`; `docs/design/moe_kernel_features.md`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/__init__.py`; `vllm/model_executor/layers/fused_moe/cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/fallback.py`; `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`; `vllm/model_executor/layers/fused_moe/oracle/__init__.py`; `vllm/model_executor/layers/fused_moe/oracle/fp8.py`; `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/triton_deep_gemm_moe.py` 等 16 个文件
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ht.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ht.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-CT-fi-cutlass.yaml` 等 17 个文件
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

### Commit `d3e477c01` - [MoE Refactor] Add Temporary Integration Tests - H100/B200 (#31759)

- 完整 hash: `d3e477c01342f800790b170b8fa799b467621358`
- 时间/作者: 2026-01-06 / Robert Shaw
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-marlin.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml` 等 30 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - tests: `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-marlin.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-cutlass.yaml` 等 29 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

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

### Commit `16484d394` - [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475)

- 完整 hash: `16484d394c6046890635b7895edb4deca2f1b1b0`
- 时间/作者: 2025-12-16 / Roger Wang
- 自动分类: 性能/后端优化
- 主要文件: `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py`, `tests/v1/ec_connector/unit/test_ec_example_connector.py`, `vllm/distributed/ec_transfer/ec_connector/example_connector.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/multimodal/inputs.py`, `vllm/multimodal/profiling.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/profiling.py`; `vllm/multimodal/registry.py`; `vllm/v1/request.py`
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/utils.py`
  - runtime-perf: `vllm/distributed/ec_transfer/ec_connector/example_connector.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/models/multimodal/processing/test_mllama4.py`; `tests/multimodal/test_utils.py`; `tests/v1/core/test_encoder_cache_manager.py`; `tests/v1/ec_connector/unit/test_ec_example_connector.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f5f51e593` - [Core][MM] Optimize encoder cache manager by operating with embeddings only (#30475)

- 完整 hash: `f5f51e5931ffd99afe69696b60765b88d3eb13f2`
- 时间/作者: 2025-12-16 / Roger Wang
- 自动分类: 性能/后端优化
- 主要文件: `tests/models/multimodal/processing/test_mllama4.py`, `tests/multimodal/test_utils.py`, `tests/v1/core/test_encoder_cache_manager.py`, `tests/v1/ec_connector/unit/test_ec_example_connector.py`, `vllm/distributed/ec_transfer/ec_connector/example_connector.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/multimodal/inputs.py`, `vllm/multimodal/profiling.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/profiling.py`; `vllm/multimodal/registry.py`; `vllm/v1/request.py`
  - runtime-model: `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/utils.py`
  - runtime-perf: `vllm/distributed/ec_transfer/ec_connector/example_connector.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/models/multimodal/processing/test_mllama4.py`; `tests/multimodal/test_utils.py`; `tests/v1/core/test_encoder_cache_manager.py`; `tests/v1/ec_connector/unit/test_ec_example_connector.py`
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

### Commit `962d70381` - [Bugfix][llama4_eagle] Fix missing 'lm_head' attribute (#29926)

- 完整 hash: `962d703818c038b6ea2ae18eab8061a6f2fb8f65`
- 时间/作者: 2025-12-05 / Divakar Verma
- 自动分类: 缺陷修复
- 主要文件: `tests/v1/e2e/test_spec_decode.py`, `vllm/model_executor/models/llama4_eagle.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/llama4_eagle.py`
  - tests: `tests/v1/e2e/test_spec_decode.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `bcf43ab1f` - [CI/Build][AMD] Add Llama4 Maverick FP8 to AMD CI (#28695)

- 完整 hash: `bcf43ab1f380208ea33769c49d116ea83f915080`
- 时间/作者: 2025-12-04 / Zhewen Li
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/lm-eval-harness/configs/Meta-Llama-4-Maverick-17B-128E-Instruct-FP8.yaml`, `.buildkite/lm-eval-harness/configs/models-large-rocm.txt`, `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`, `.buildkite/test-amd.yaml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/lm-eval-harness/configs/Meta-Llama-4-Maverick-17B-128E-Instruct-FP8.yaml`; `.buildkite/lm-eval-harness/configs/models-large-rocm.txt`; `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`; `.buildkite/test-amd.yaml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `9057fc2f1` - [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908)

- 完整 hash: `9057fc2f1b2701c2f33223c1b4b4d4036f2dc998`
- 时间/作者: 2025-12-02 / Julien Denize
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5e5646e20` - [BUGFIX] llama_4_scaling wrongly passed to DeepseekAttention (#29908)

- 完整 hash: `5e5646e2064f925f97ff533aa688a43834e9ff96`
- 时间/作者: 2025-12-02 / Julien Denize
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `34a8559be` - [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851)

- 完整 hash: `34a8559be7473e3ba34e9b9e13827e60651e3b41`
- 时间/作者: 2025-12-02 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py`, `vllm/entrypoints/renderer.py`, `vllm/entrypoints/score_utils.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/multimodal/processing.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/processing.py`; `vllm/transformers_utils/tokenizer.py`
  - runtime-model: `vllm/entrypoints/openai/speech_to_text.py`; `vllm/entrypoints/renderer.py`; `vllm/entrypoints/score_utils.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py`
  - tests: `tests/models/multimodal/processing/test_common.py`; `tests/models/multimodal/processing/test_llama4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `68ffbca7e` - [Chore] Use `tokenizer.encode` and `tokenizer.decode` directly (#29851)

- 完整 hash: `68ffbca7e462cfa6a32b46dabc9a604c7c1b918d`
- 时间/作者: 2025-12-02 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llama4.py`, `vllm/entrypoints/openai/speech_to_text.py`, `vllm/entrypoints/renderer.py`, `vllm/entrypoints/score_utils.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/multimodal/processing.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/processing.py`; `vllm/transformers_utils/tokenizer.py`
  - runtime-model: `vllm/entrypoints/openai/speech_to_text.py`; `vllm/entrypoints/renderer.py`; `vllm/entrypoints/score_utils.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py`
  - tests: `tests/models/multimodal/processing/test_common.py`; `tests/models/multimodal/processing/test_llama4.py`
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

### Commit `ed6ae1e36` - [AITER] [ROCm] Fix crash when loading llama4 model with old aiter version installed, fallback to forward_native implementation (#29124)

- 完整 hash: `ed6ae1e36a03bed4a29287163e051a7772b1d8b1`
- 时间/作者: 2025-11-20 / Xiao Li
- 自动分类: 性能/后端优化
- 主要文件: `vllm/v1/sample/ops/topk_topp_sampler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/sample/ops/topk_topp_sampler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `93c8672ce` - [Bugfix] Fix spec decode memory regression after #28549 (#28819)

- 完整 hash: `93c8672ceb06f6e9c282a96fcd85a7ce41293693`
- 时间/作者: 2025-11-20 / Zhewen Li
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/llama4_eagle.py`, `vllm/model_executor/models/llama_eagle.py`, `vllm/v1/spec_decode/eagle.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/llama4_eagle.py`; `vllm/model_executor/models/llama_eagle.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `dc45efc8e` - [BugFix] Fix Llama4 Pipeline Parallelism Assert Error (#28577)

- 完整 hash: `dc45efc8ef7fc1e2571331eaf4671e1652e2a865`
- 时间/作者: 2025-11-20 / Dezhan
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/llama4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/llama4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `61728cd1d` - Re-enable FlashInfer for Llama4 on Blackwell in e2e fusion tests (#28966)

- 完整 hash: `61728cd1dfb03cbbfa03924f2a2cda311cfc13ac`
- 时间/作者: 2025-11-19 / Copilot
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/compile/distributed/test_fusions_e2e.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - tests: `tests/compile/distributed/test_fusions_e2e.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

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

### Commit `3380ed5e1` - [Doc] Add llama4 LoRA tag (#28825)

- 完整 hash: `3380ed5e115613bb0029164754ffea99f328e065`
- 时间/作者: 2025-11-17 / Jee Jee Li
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/models/supported_models.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/models/supported_models.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `e439c784f` - Add support for Eagle with separate lm-head and embed_tokens layers (#28549)

- 完整 hash: `e439c784fa318dbc23c04b0730bee0fccf46481d`
- 时间/作者: 2025-11-15 / Eldar Kurtić
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/v1/spec_decode/test_eagle.py`, `tests/v1/spec_decode/test_mtp.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/llama4_eagle.py`, `vllm/model_executor/models/llama_eagle.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llama.py`; `vllm/model_executor/models/llama4_eagle.py`; `vllm/model_executor/models/llama_eagle.py`; `vllm/model_executor/models/llama_eagle3.py`; `vllm/model_executor/models/minicpm_eagle.py` 等 9 个文件
  - tests: `tests/v1/spec_decode/test_eagle.py`; `tests/v1/spec_decode/test_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `1ec978c20` - [Kernel][Moe Configs] llama4 maverick fp8 moe config tp8 on mi325 (#28709)

- 完整 hash: `1ec978c209391286d4cee968426900e9a4d256a5`
- 时间/作者: 2025-11-15 / Zhewen Li
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/configs/E=128,N=1024,device_name=AMD_Instinct_MI325X,dtype=fp8_w8a8.json`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=1024,device_name=AMD_Instinct_MI325X,dtype=fp8_w8a8.json`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `964d65dee` - LLaMA4 LoRA Adapter Enablement (#28602)

- 完整 hash: `964d65deedb9ae0480fecdb2e726ba16d63409d7`
- 时间/作者: 2025-11-14 / Fardin Hoque
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/mllama4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/mllama4.py`
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

### Commit `7a8375f8a` - Add llama 4 scaling support (#28145)

- 完整 hash: `7a8375f8a0cd37ee7e3d2be8498b5ae543694179`
- 时间/作者: 2025-11-06 / Julien Denize
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`, `vllm/model_executor/models/llama.py`, `vllm/transformers_utils/configs/mistral.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`; `vllm/model_executor/models/llama.py`; `vllm/transformers_utils/configs/mistral.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `6e97eccf5` - [XPU] Enable custom routing functions in IPEX for Llama4 (#28004)

- 完整 hash: `6e97eccf5dd5036e26d63141d2bc1a9ea17a2cc8`
- 时间/作者: 2025-11-05 / Frost Mitchell
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`
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

### Commit `b798e39f9` - [XPU][bugfix] fix rope for llama4 and deepseek (#25145)

- 完整 hash: `b798e39f931ad42354e0223de3d49e24523b79af`
- 时间/作者: 2025-10-30 / Yan Ma
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`, `vllm/model_executor/layers/rotary_embedding/llama4_vision_rope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`; `vllm/model_executor/layers/rotary_embedding/llama4_vision_rope.py`; `vllm/model_executor/layers/rotary_embedding/mrope.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
