# vllm GPT-OSS 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `tests/evals/gpt_oss/__init__.py` | 无直接提交 |
| `tests/evals/gpt_oss/conftest.py` | 无直接提交 |
| `tests/evals/gpt_oss/test_gpqa_correctness.py` | 无直接提交 |
| `tests/kernels/moe/test_gpt_oss_triton_kernels.py` | `3e41992fe`, `fd65015a1`, `a8b70304d` |
| `tests/models/quantization/test_gpt_oss_attn_quantization.py` | `5a1271d83` |
| `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` | `42135d689`, `3f72639d3`, `e7b68f4d6`, `a491b0911`, `3fd1fb0b6`, `745a3bae1`, `53d7f1f60` |
| `vllm/model_executor/models/gpt_oss.py` | `df7041633`, `dcd80206b`, `2612ba928`, `482914849`, `cf3eacfe5`, `5f5521bd5`, `430dd4d9e`, `1073ba68b`, `6eb745d9b`, `2fd893b4c`, `a8b70304d`, `8d259fad6`, ... (18 total) |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 53
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-02-01 | `f0d005864` | 缺陷修复 | [Fix] prefix cache hit rate == 0 bug with gpt-oss style models (#33524) | `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/kv_cache_coordinator.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-21 | `42135d689` | 性能/后端优化 | [MoE Refactor] Oracle Select FP8+NVFP4 Kernels In Priority (#32414) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py` |
| 2026-01-15 | `46f8a982b` | 性能/后端优化 | [ROCm][CI] Enable AITER Unified Attention On ROCm For gpt-oss Test (#32431) | `tests/entrypoints/openai/test_serving_chat.py` |
| 2026-01-14 | `d084e9fca` | 缺陷修复 | [MODEL] Fix handling of multiple channels for gpt-oss with speculative decoding (#26291) | `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/test_serving_chat_stream_harmony.py`, `vllm/entrypoints/openai/chat_completion/serving.py` |
| 2026-01-12 | `3f72639d3` | 性能/后端优化 | [FIX] Add NO_MUL activation support for modular kernel path (#31528) | `tests/kernels/moe/test_triton_moe_no_act_mul.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/cutlass_moe.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-09 | `f32c629eb` | 模型支持/运行时入口 | [Frontend][gpt-oss] Allow system message to overwrite model identity (#31737) | `tests/entrypoints/openai/test_response_api_with_harmony.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`, `vllm/entrypoints/openai/serving_responses.py` |
| 2026-01-09 | `e7b68f4d6` | 性能/后端优化 | [Bugfix] Fix Triton FusedMoE LoRA (#30585) | `pyproject.toml`, `tests/lora/test_gptoss_tp.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `a45673d2b` | 性能/后端优化 | [gpt-oss-20b] MoE configs for BW1000 TP=1&2 [gpt-oss-120b] MoE configs for BW1000 TP=8 | `vllm/model_executor/layers/fused_moe/configs/E=128,N=360,device_name=gfx936_80cu.json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=360,device_name=gfx936_80cu_nn.json`, `vllm/model_executor/layers/fused_moe/configs/E=32,N=1440,device_name=gfx936_80cu.json` |
| 2025-12-25 | `42826bbcc` | 模型支持/运行时入口 | [Doc] Add tool call parser documentation for GPT-OSS models (#31212) | `docs/features/tool_calling.md` |
| 2025-12-22 | `ab3a85fd6` | 性能/后端优化 | [ROCm][CI/Build] Fix triton version to one that has triton_kernels required for gpt-oss to run (#31159) | `docker/Dockerfile.rocm_base` |
| 2025-12-22 | `bd6d5a747` | 缺陷修复 | [gpt-oss] Fix harmony parser in streaming responses (#30205) | `vllm/entrypoints/openai/serving_chat.py` |
| 2025-12-21 | `3e92b2b7a` | 缺陷修复 | [BugFix]fix gpt-oss v1/completions response bug (#30608) | `tests/entrypoints/openai/test_response_api_with_harmony.py`, `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/serving_chat.py` |
| 2025-12-19 | `6a09612b2` | 缺陷修复 | [Bugfix] Fix tool_choice="none" being ignored by GPT-OSS/harmony models (#30867) | `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/serving_chat.py` |
| 2025-12-12 | `3e41992fe` | 性能/后端优化 | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 (#27532) | `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp` |
| 2025-12-11 | `8f8fda261` | 缺陷修复 | [Bugfix] Multiple fixes for gpt-oss Chat Completion prompting (#28729) | `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/utils.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-05 | `02a416919` | 性能/后端优化 | [Tests] Tool call tests for openai/gpt-oss-20b (#26237) | `requirements/rocm-test.txt`, `tests/entrypoints/openai/tool_parsers/test_openai_tool_parser.py` |
| 2025-11-29 | `a491b0911` | 性能/后端优化 | [LoRA] Support FusedMoE LoRA Triton kernel for mxfp4 (#29708) | `tests/kernels/moe/test_modular_oai_triton_moe.py`, `vllm/lora/layers/fused_moe.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` |
| 2025-11-28 | `3fd1fb0b6` | 性能/后端优化 | Revert "[LoRA] Support FusedMoE LoRA Triton kernel for mxfp4 (#28971)" (#29697) | `tests/kernels/moe/test_modular_oai_triton_moe.py`, `vllm/lora/layers/fused_moe.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` |
| 2025-11-28 | `5f5521bd5` | 缺陷修复 | Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights (#29506) | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-27 | `745a3bae1` | 性能/后端优化 | [LoRA] Support FusedMoE LoRA Triton kernel for mxfp4 (#28971) | `tests/kernels/moe/test_modular_oai_triton_moe.py`, `vllm/lora/layers/fused_moe.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-26 | `70d5953f8` | 性能/后端优化 | Revert "[Bugfix] Fix GPT-OSS AR+NORM fusion (#28841)" (#29483) | `.buildkite/test-pipeline.yaml`, `tests/compile/distributed/test_fusions_e2e.py`, `vllm/distributed/device_communicators/symm_mem.py` |
| 2025-11-25 | `53d7f1f60` | 性能/后端优化 | [Kernel] Use pre-allocated output buffer for triton kernel fused_experts (#29219) | `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` |
| 2025-11-25 | `6330f9477` | 性能/后端优化 | [Bugfix] Fix GPT-OSS AR+NORM fusion (#28841) | `.buildkite/test-pipeline.yaml`, `tests/compile/distributed/test_fusions_e2e.py`, `vllm/distributed/device_communicators/symm_mem.py` |
| 2025-11-24 | `71df2a57e` | 调度/缓存/PD | [Hybrid Allocator] Better layer padding strategy for gpt-oss eagle (#29303) | `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py` |
| 2025-11-24 | `84371daf7` | 测试/文档/基准 | [Tests] Verify gpt_oss package is installed in harmony tests (#29336) | `tests/entrypoints/openai/test_response_api_with_harmony.py` |
| 2025-11-24 | `1073ba68b` | 性能/后端优化 | [LoRA] Optimize 3D MoE logic (#29222) | `tests/lora/test_gptoss_tp.py`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/base.py` |
| 2025-11-21 | `fd65015a1` | 性能/后端优化 | [CI/Build] Only use supported types and features on ROCm in MoE kernel tests (#29149) | `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py` |
| 2025-11-20 | `3f5f36da3` | 性能/后端优化 | [ROCm] Fix for import when building with upstream triton for gfx1100 for gpt-oss serving (#29127) | `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py` |
| 2025-11-20 | `6eb745d9b` | 模型支持/运行时入口 | Add truncate arg to yarn to match openai implementation of gpt-oss (#28244) | `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py` |
| 2025-11-20 | `2fd893b4c` | 性能/后端优化 | [Feature] Prefill Context Parallel (PCP) basic support (#28718) | `tests/distributed/test_context_parallel.py`, `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/v1/worker/test_gpu_model_runner.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-18 | `d0a73620c` | 性能/后端优化 | [ROCm][Quantization] add apply_vllm_mapper in quark config for models like gpt-oss (#28638) | `vllm/model_executor/layers/quantization/quark/quark.py` |
| 2025-11-17 | `f8b19c0ff` | 性能/后端优化 | [Bugfix] Fix GPT-OSS on AMD after #28603 (#28816) | `.buildkite/test-amd.yaml`, `vllm/model_executor/layers/quantization/mxfp4.py` |
| 2025-11-16 | `8d259fad6` | 缺陷修复 | Fix gpt oss weight loading with EP + bf16 (#28765) | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-16 | `af02c4097` | 缺陷修复 | Fixed gpt-oss _load_weights_other() parameter position bug (#28715) | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `a543e678b` | 性能/后端优化 | [Bugfix] Fix SM100 gpt-oss regression due to faulty attn sink support (#28561) | `vllm/utils/flashinfer.py`, `vllm/v1/attention/backends/flashinfer.py` |
| 2025-11-12 | `a9d18b510` | 缺陷修复 | [Bugfix] Fix gpt_oss packed_modules_mapping (#28536) | `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-12 | `5a1271d83` | 性能/后端优化 | [Quantization] fix attention quantization of gpt_oss model (#27334) | `tests/models/quantization/test_gpt_oss_attn_quantization.py`, `vllm/model_executor/layers/quantization/mxfp4.py`, `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-09 | `404d7a9d1` | 性能/后端优化 | [Performance][gpt-oss] Revert gpt-oss max cudagraph size to 1024 (#28345) | `vllm/model_executor/models/config.py` |
| 2025-11-05 | `18b39828d` | 性能/后端优化 | [XPU] Add gpt-oss model support for Intel GPU (#27786) | `vllm/attention/utils/fa_utils.py`, `vllm/model_executor/layers/quantization/mxfp4.py`, `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-04 | `2d977a7a9` | 性能/后端优化 | [ROCm] gemm_a16w16 upstreaming (#26969) | `vllm/model_executor/layers/utils.py`, `vllm/model_executor/models/gpt_oss.py` |
| 2025-11-03 | `32257297d` | 测试/文档/基准 | [CI/Build] Remove the flaky gpt-oss lora test (#27966) | `tests/lora/test_gptoss_tp.py` |
| 2025-10-31 | `0384aa715` | 性能/后端优化 | [CI/Build] Add gpt-oss LoRA test (#27870) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `tests/lora/conftest.py` |
| 2025-10-30 | `e5e076cad` | 性能/后端优化 | [BugFix] Stopgap - Flashinfer Autotuner + GPT-OSS + DP/TP (#27762) | `vllm/model_executor/warmup/kernel_warmup.py` |
| 2025-10-29 | `ab2eb27b7` | 缺陷修复 | [Frontend] [gpt-oss] Mcp type bug (#27689) | `tests/entrypoints/openai/test_response_api_mcp_tools.py`, `tests/entrypoints/openai/test_serving_responses.py`, `tests/entrypoints/test_harmony_utils.py` |
| 2025-10-29 | `3c7fefdeb` | 缺陷修复 | [Frontend] [gpt-oss] Tool json call parsing error retry (#27675) | `vllm/entrypoints/context.py`, `vllm/entrypoints/harmony_utils.py`, `vllm/envs.py` |

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

### Commit `f0d005864` - [Fix] prefix cache hit rate == 0 bug with gpt-oss style models (#33524)

- 完整 hash: `f0d005864a78c0a91aceb16a9fecd8c06bfbceab`
- 时间/作者: 2026-02-01 / Yifan Qiao
- 自动分类: 缺陷修复
- 主要文件: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/kv_cache_coordinator.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/core/kv_cache_coordinator.py`
  - tests: `tests/v1/core/test_prefix_caching.py`
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

### Commit `46f8a982b` - [ROCm][CI] Enable AITER Unified Attention On ROCm For gpt-oss Test (#32431)

- 完整 hash: `46f8a982b191e3a3d3a1eccaf18b184c391ac2ac`
- 时间/作者: 2026-01-15 / Micah Williamson
- 自动分类: 性能/后端优化
- 主要文件: `tests/entrypoints/openai/test_serving_chat.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `tests/entrypoints/openai/test_serving_chat.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `d084e9fca` - [MODEL] Fix handling of multiple channels for gpt-oss with speculative decoding  (#26291)

- 完整 hash: `d084e9fca7d5d40cbb62eb5fe8ab5cbc6c769cf0`
- 时间/作者: 2026-01-14 / Aleksandr Samarin
- 自动分类: 缺陷修复
- 主要文件: `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/test_serving_chat_stream_harmony.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/chat_completion/stream_harmony.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/chat_completion/serving.py`; `vllm/entrypoints/openai/chat_completion/stream_harmony.py`
  - tests: `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/test_serving_chat_stream_harmony.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3f72639d3` - [FIX] Add NO_MUL activation support for modular kernel path (#31528)

- 完整 hash: `3f72639d36a15b348c3dfee211daa3da8140736f`
- 时间/作者: 2026-01-12 / danielafrimi
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/moe/test_triton_moe_no_act_mul.py`, `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/fallback.py`, `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py`, `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/fused_batched_moe.py` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/fallback.py`; `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py`; `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/fused_batched_moe.py`; `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py` 等 16 个文件
  - tests: `tests/kernels/moe/test_triton_moe_no_act_mul.py`
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

### Commit `f32c629eb` - [Frontend][gpt-oss] Allow system message to overwrite model identity (#31737)

- 完整 hash: `f32c629eb4cc2bbe85d321a6b382e30e33a32f7d`
- 时间/作者: 2026-01-09 / Andrew Xia
- 自动分类: 模型支持/运行时入口
- 主要文件: `tests/entrypoints/openai/test_response_api_with_harmony.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`, `vllm/entrypoints/openai/serving_responses.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/parser/harmony_utils.py`; `vllm/entrypoints/openai/serving_responses.py`
  - tests: `tests/entrypoints/openai/test_response_api_with_harmony.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `e7b68f4d6` - [Bugfix] Fix Triton FusedMoE LoRA (#30585)

- 完整 hash: `e7b68f4d6c7e4b71820994566b7317f24e613b2e`
- 时间/作者: 2026-01-09 / Xin Yang
- 自动分类: 性能/后端优化
- 主要文件: `pyproject.toml`, `tests/lora/test_gptoss_tp.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `pyproject.toml`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`
  - tests: `tests/lora/test_gptoss_tp.py`
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

### Commit `a45673d2b` - [gpt-oss-20b] MoE configs for BW1000 TP=1&2 [gpt-oss-120b] MoE configs for BW1000 TP=8

- 完整 hash: `a45673d2bc833596b4e40693b43797454e6320bd`
- 时间/作者: 2026-01-06 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/configs/E=128,N=360,device_name=gfx936_80cu.json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=360,device_name=gfx936_80cu_nn.json`, `vllm/model_executor/layers/fused_moe/configs/E=32,N=1440,device_name=gfx936_80cu.json`, `vllm/model_executor/layers/fused_moe/configs/E=32,N=1440,device_name=gfx936_80cu_nn.json`, `vllm/model_executor/layers/fused_moe/configs/E=32,N=2880,device_name=gfx936_80cu.json`, `vllm/model_executor/layers/fused_moe/configs/E=32,N=2880,device_name=gfx936_80cu_nn.json`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=360,device_name=gfx936_80cu.json`; `vllm/model_executor/layers/fused_moe/configs/E=128,N=360,device_name=gfx936_80cu_nn.json`; `vllm/model_executor/layers/fused_moe/configs/E=32,N=1440,device_name=gfx936_80cu.json`; `vllm/model_executor/layers/fused_moe/configs/E=32,N=1440,device_name=gfx936_80cu_nn.json`; `vllm/model_executor/layers/fused_moe/configs/E=32,N=2880,device_name=gfx936_80cu.json`; `vllm/model_executor/layers/fused_moe/configs/E=32,N=2880,device_name=gfx936_80cu_nn.json`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `42826bbcc` - [Doc] Add tool call parser documentation for GPT-OSS models (#31212)

- 完整 hash: `42826bbccd04d71d88e19f51a0d0b3d98f29d780`
- 时间/作者: 2025-12-25 / Amith KK
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/features/tool_calling.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/features/tool_calling.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `ab3a85fd6` - [ROCm][CI/Build] Fix triton version to one that has triton_kernels required for gpt-oss to run (#31159)

- 完整 hash: `ab3a85fd688dc2544edab3098fab8e2c8893a707`
- 时间/作者: 2025-12-22 / Gregory Shtrasberg
- 自动分类: 性能/后端优化
- 主要文件: `docker/Dockerfile.rocm_base`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `docker/Dockerfile.rocm_base`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bd6d5a747` - [gpt-oss] Fix harmony parser in streaming responses (#30205)

- 完整 hash: `bd6d5a7475aa26a85de5d63cfcae9a1151d7652f`
- 时间/作者: 2025-12-22 / AlonKejzman
- 自动分类: 缺陷修复
- 主要文件: `vllm/entrypoints/openai/serving_chat.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/serving_chat.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3e92b2b7a` - [BugFix]fix gpt-oss v1/completions response bug (#30608)

- 完整 hash: `3e92b2b7acaa61335ecd7bea5eeed50388739194`
- 时间/作者: 2025-12-21 / 汪志鹏
- 自动分类: 缺陷修复
- 主要文件: `tests/entrypoints/openai/test_response_api_with_harmony.py`, `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/serving_chat.py`, `vllm/tool_parsers/openai_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/tool_parsers/openai_tool_parser.py`
  - runtime-model: `vllm/entrypoints/openai/serving_chat.py`
  - tests: `tests/entrypoints/openai/test_response_api_with_harmony.py`; `tests/entrypoints/openai/test_serving_chat.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `6a09612b2` - [Bugfix] Fix tool_choice="none" being ignored by GPT-OSS/harmony models (#30867)

- 完整 hash: `6a09612b2e0e09d037a220ea8115632b8084e008`
- 时间/作者: 2025-12-19 / PlatinumGod
- 自动分类: 缺陷修复
- 主要文件: `tests/entrypoints/openai/test_serving_chat.py`, `vllm/entrypoints/openai/serving_chat.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/serving_chat.py`
  - tests: `tests/entrypoints/openai/test_serving_chat.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3e41992fe` - [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 (#27532)

- 完整 hash: `3e41992fecdc31ee60715bb350f18fec18ed6680`
- 时间/作者: 2025-12-12 / Lucas Wilkinson
- 自动分类: 性能/后端优化
- 主要文件: `csrc/cache.h`, `csrc/cache_kernels.cu`, `csrc/torch_bindings.cpp`, `tests/conftest.py`, `tests/kernels/moe/test_batched_deepgemm.py`, `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py`, `tests/kernels/moe/test_cutlass_moe.py` 等 30 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `csrc/torch_bindings.cpp`; `vllm/_custom_ops.py`; `vllm/envs.py`
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/gpu_worker.py`; `vllm/v1/worker/workspace.py`
  - runtime-perf: `csrc/cache.h`; `csrc/cache_kernels.cu`; `vllm/model_executor/layers/fused_moe/modular_kernel.py`; `vllm/v1/attention/backends/mla/flashmla_sparse.py`; `vllm/v1/attention/backends/mla/indexer.py`; `vllm/v1/attention/backends/utils.py`
  - tests: `tests/conftest.py`; `tests/kernels/moe/test_batched_deepgemm.py`; `tests/kernels/moe/test_batched_moe.py`; `tests/kernels/moe/test_block_fp8.py`; `tests/kernels/moe/test_cutlass_moe.py`; `tests/kernels/moe/test_deepep_deepgemm_moe.py`; `tests/kernels/moe/test_deepep_moe.py`; `tests/kernels/moe/test_deepgemm.py` 等 17 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8f8fda261` - [Bugfix] Multiple fixes for gpt-oss Chat Completion prompting (#28729)

- 完整 hash: `8f8fda261a620234fdeea338f44093d5d8072879`
- 时间/作者: 2025-12-11 / Ben Browning
- 自动分类: 缺陷修复
- 主要文件: `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/entrypoints/openai/test_serving_chat.py`, `tests/entrypoints/openai/utils.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`, `vllm/entrypoints/openai/serving_chat.py`, `vllm/entrypoints/openai/tool_parsers/openai_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/entrypoints/openai/parser/harmony_utils.py`; `vllm/entrypoints/openai/serving_chat.py`; `vllm/entrypoints/openai/tool_parsers/openai_tool_parser.py`
  - tests: `tests/entrypoints/openai/parser/test_harmony_utils.py`; `tests/entrypoints/openai/test_serving_chat.py`; `tests/entrypoints/openai/utils.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `02a416919` - [Tests] Tool call tests for openai/gpt-oss-20b (#26237)

- 完整 hash: `02a41691932683aa544b8a0139586f43e2f8b4bd`
- 时间/作者: 2025-12-05 / Deboleina
- 自动分类: 性能/后端优化
- 主要文件: `requirements/rocm-test.txt`, `tests/entrypoints/openai/tool_parsers/test_openai_tool_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `requirements/rocm-test.txt`
  - tests: `tests/entrypoints/openai/tool_parsers/test_openai_tool_parser.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a491b0911` - [LoRA] Support FusedMoE LoRA Triton kernel for mxfp4 (#29708)

- 完整 hash: `a491b0911bf9d9ed264ec3ad83bdd9e96c0324a6`
- 时间/作者: 2025-11-29 / Xin Yang
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/moe/test_modular_oai_triton_moe.py`, `vllm/lora/layers/fused_moe.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`, `vllm/model_executor/layers/quantization/mxfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/lora/layers/fused_moe.py`; `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`; `vllm/model_executor/layers/quantization/mxfp4.py`
  - tests: `tests/kernels/moe/test_modular_oai_triton_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3fd1fb0b6` - Revert "[LoRA] Support FusedMoE LoRA Triton kernel for mxfp4 (#28971)" (#29697)

- 完整 hash: `3fd1fb0b6016d1471853f5114fd97c74f1a8d29c`
- 时间/作者: 2025-11-28 / Huamin Li
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/moe/test_modular_oai_triton_moe.py`, `vllm/lora/layers/fused_moe.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`, `vllm/model_executor/layers/quantization/mxfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/lora/layers/fused_moe.py`; `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`; `vllm/model_executor/layers/quantization/mxfp4.py`
  - tests: `tests/kernels/moe/test_modular_oai_triton_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5f5521bd5` - Fix parameter order in GPT-OSS weight loading function for non-MXFP4 weights  (#29506)

- 完整 hash: `5f5521bd5d7d38d380640166294d97a839cf7ef9`
- 时间/作者: 2025-11-28 / Filipp Fisin
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/gpt_oss.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `745a3bae1` - [LoRA] Support FusedMoE LoRA Triton kernel for mxfp4 (#28971)

- 完整 hash: `745a3bae1aef2ff3aa70b3eab8624e4571698ba0`
- 时间/作者: 2025-11-27 / Xin Yang
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/moe/test_modular_oai_triton_moe.py`, `vllm/lora/layers/fused_moe.py`, `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`, `vllm/model_executor/layers/quantization/mxfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/lora/layers/fused_moe.py`; `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`; `vllm/model_executor/layers/quantization/mxfp4.py`
  - tests: `tests/kernels/moe/test_modular_oai_triton_moe.py`
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

### Commit `70d5953f8` - Revert "[Bugfix] Fix GPT-OSS AR+NORM fusion (#28841)" (#29483)

- 完整 hash: `70d5953f820ec528e2b6050a7969130009410d1e`
- 时间/作者: 2025-11-26 / Huamin Li
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/compile/distributed/test_fusions_e2e.py`, `vllm/distributed/device_communicators/symm_mem.py`, `vllm/model_executor/layers/fused_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/distributed/device_communicators/symm_mem.py`; `vllm/model_executor/layers/fused_moe/layer.py`
  - tests: `tests/compile/distributed/test_fusions_e2e.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `53d7f1f60` - [Kernel] Use pre-allocated output buffer for triton kernel fused_experts (#29219)

- 完整 hash: `53d7f1f601a12b8fa58aa0bffb7fc27d63d1eb5e`
- 时间/作者: 2025-11-25 / Xin Yang
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6330f9477` - [Bugfix] Fix GPT-OSS AR+NORM fusion (#28841)

- 完整 hash: `6330f9477db214477004df6546f86e3f14f8eab9`
- 时间/作者: 2025-11-25 / elvischenv
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/compile/distributed/test_fusions_e2e.py`, `vllm/distributed/device_communicators/symm_mem.py`, `vllm/model_executor/layers/fused_moe/layer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/distributed/device_communicators/symm_mem.py`; `vllm/model_executor/layers/fused_moe/layer.py`
  - tests: `tests/compile/distributed/test_fusions_e2e.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `71df2a57e` - [Hybrid Allocator] Better layer padding strategy for gpt-oss eagle (#29303)

- 完整 hash: `71df2a57effc15b5f67cdbf55f3d1e1b71f90e86`
- 时间/作者: 2025-11-24 / Chen Zhang
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/v1/core/kv_cache_utils.py`
  - tests: `tests/v1/core/test_kv_cache_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `84371daf7` - [Tests] Verify gpt_oss package is installed in harmony tests (#29336)

- 完整 hash: `84371daf75507c849a38a9a44b2fb2af89e96dd3`
- 时间/作者: 2025-11-24 / Nick Hill
- 自动分类: 测试/文档/基准
- 主要文件: `tests/entrypoints/openai/test_response_api_with_harmony.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `tests/entrypoints/openai/test_response_api_with_harmony.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `1073ba68b` - [LoRA] Optimize 3D MoE logic (#29222)

- 完整 hash: `1073ba68b0a741de6de0a7230795acba151084f2`
- 时间/作者: 2025-11-24 / Jee Jee Li
- 自动分类: 性能/后端优化
- 主要文件: `tests/lora/test_gptoss_tp.py`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/base.py`, `vllm/lora/layers/base_linear.py`, `vllm/lora/layers/column_parallel_linear.py`, `vllm/lora/layers/fused_moe.py`, `vllm/lora/layers/logits_processor.py`, `vllm/lora/layers/vocal_parallel_embedding.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/lora/layers/__init__.py`; `vllm/lora/layers/base.py`; `vllm/lora/layers/base_linear.py`; `vllm/lora/layers/column_parallel_linear.py`; `vllm/lora/layers/logits_processor.py`; `vllm/lora/layers/vocal_parallel_embedding.py`; `vllm/lora/models.py`; `vllm/lora/utils.py`
  - runtime-model: `vllm/model_executor/models/gpt_oss.py`
  - runtime-perf: `vllm/lora/layers/fused_moe.py`
  - tests: `tests/lora/test_gptoss_tp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fd65015a1` - [CI/Build] Only use supported types and features on ROCm in MoE kernel tests (#29149)

- 完整 hash: `fd65015a14be5f2ce663cd959dff6970285c54b4`
- 时间/作者: 2025-11-21 / rasmith
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`, `tests/kernels/moe/test_moe_permute_unpermute.py`, `tests/kernels/moe/test_silu_mul_fp8_quant_deep_gemm.py`, `tests/kernels/moe/test_triton_moe_ptpc_fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `tests/kernels/moe/test_batched_moe.py`; `tests/kernels/moe/test_block_fp8.py`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; `tests/kernels/moe/test_modular_kernel_combinations.py`; `tests/kernels/moe/test_moe_permute_unpermute.py`; `tests/kernels/moe/test_silu_mul_fp8_quant_deep_gemm.py`; `tests/kernels/moe/test_triton_moe_ptpc_fp8.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3f5f36da3` - [ROCm] Fix for import when building with upstream triton for gfx1100 for gpt-oss serving (#29127)

- 完整 hash: `3f5f36da3fefbae96960f60d41ccf8ac1155515e`
- 时间/作者: 2025-11-20 / Hongxia Yang
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6eb745d9b` - Add truncate arg to yarn to match openai implementation of gpt-oss (#28244)

- 完整 hash: `6eb745d9bdf5b69bb63f897b32465c62ecb9e14a`
- 时间/作者: 2025-11-20 / Anna Shors
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`, `vllm/model_executor/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/layers/rotary_embedding/common.py`; `vllm/model_executor/layers/rotary_embedding/yarn_scaling_rope.py`; `vllm/model_executor/models/gpt_oss.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `2fd893b4c` - [Feature] Prefill Context Parallel (PCP) basic support (#28718)

- 完整 hash: `2fd893b4cec0975a2a8430077fd9b4f294eb3561`
- 时间/作者: 2025-11-20 / Qiu
- 自动分类: 性能/后端优化
- 主要文件: `tests/distributed/test_context_parallel.py`, `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/attention/backends/abstract.py`, `vllm/attention/ops/common.py`, `vllm/config/parallel.py`, `vllm/config/vllm.py`, `vllm/distributed/parallel_state.py` 等 27 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/engine/arg_utils.py`; `vllm/v1/engine/core.py`; `vllm/v1/executor/multiproc_executor.py`
  - runtime-model: `vllm/config/parallel.py`; `vllm/config/vllm.py`; `vllm/model_executor/models/gpt_oss.py`; `vllm/v1/worker/block_table.py`; `vllm/v1/worker/gpu_input_batch.py`; `vllm/v1/worker/gpu_model_runner.py`; `vllm/v1/worker/gpu_worker.py`
  - runtime-perf: `vllm/attention/backends/abstract.py`; `vllm/attention/ops/common.py`; `vllm/distributed/parallel_state.py`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/v1/attention/backends/flash_attn.py`; `vllm/v1/attention/backends/mla/common.py`; `vllm/v1/attention/backends/utils.py` 等 14 个文件
  - tests: `tests/distributed/test_context_parallel.py`; `tests/kernels/moe/modular_kernel_tools/common.py`; `tests/v1/worker/test_gpu_model_runner.py`
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

### Commit `d0a73620c` - [ROCm][Quantization] add apply_vllm_mapper in quark config for models like gpt-oss (#28638)

- 完整 hash: `d0a73620cc85a840323d25b28772efac04c006e2`
- 时间/作者: 2025-11-18 / xuebwang-amd
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/quantization/quark/quark.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/quark.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f8b19c0ff` - [Bugfix] Fix GPT-OSS on AMD after #28603 (#28816)

- 完整 hash: `f8b19c0ffd65f7f6f01a0da4a39b6890f5db40cb`
- 时间/作者: 2025-11-17 / Zhewen Li
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `vllm/model_executor/layers/quantization/mxfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`
  - runtime-perf: `vllm/model_executor/layers/quantization/mxfp4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8d259fad6` - Fix gpt oss weight loading with EP + bf16 (#28765)

- 完整 hash: `8d259fad6cd5a93bef04d00640e132e84c0c9b20`
- 时间/作者: 2025-11-16 / Anna Shors
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/gpt_oss.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `af02c4097` - Fixed gpt-oss _load_weights_other() parameter position bug (#28715)

- 完整 hash: `af02c409702f2f41eb13471ce3224e3315e19d89`
- 时间/作者: 2025-11-16 / Dezhan
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/gpt_oss.py`
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

### Commit `a543e678b` - [Bugfix] Fix SM100 gpt-oss regression due to faulty attn sink support (#28561)

- 完整 hash: `a543e678b45a08c6bd98a4e5ebcc244679003659`
- 时间/作者: 2025-11-12 / Michael Goin
- 自动分类: 性能/后端优化
- 主要文件: `vllm/utils/flashinfer.py`, `vllm/v1/attention/backends/flashinfer.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/utils/flashinfer.py`; `vllm/v1/attention/backends/flashinfer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a9d18b510` - [Bugfix] Fix gpt_oss packed_modules_mapping (#28536)

- 完整 hash: `a9d18b51078d29f732e2811e91e8c002b1d1d0c4`
- 时间/作者: 2025-11-12 / Jee Jee Li
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/gpt_oss.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5a1271d83` - [Quantization] fix attention quantization of gpt_oss model (#27334)

- 完整 hash: `5a1271d83a65be5ed8dc3e4c990ed42074197db3`
- 时间/作者: 2025-11-12 / xuebwang-amd
- 自动分类: 性能/后端优化
- 主要文件: `tests/models/quantization/test_gpt_oss_attn_quantization.py`, `vllm/model_executor/layers/quantization/mxfp4.py`, `vllm/model_executor/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/gpt_oss.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/mxfp4.py`
  - tests: `tests/models/quantization/test_gpt_oss_attn_quantization.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `404d7a9d1` - [Performance][gpt-oss] Revert gpt-oss max cudagraph size to 1024 (#28345)

- 完整 hash: `404d7a9d1452d571c52fdcc6795ad18add57483c`
- 时间/作者: 2025-11-09 / Mohammad Miadh Angkad
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/config.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/config.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `18b39828d` - [XPU] Add gpt-oss model support for Intel GPU (#27786)

- 完整 hash: `18b39828d90413d05d770dfd2e2f48304f4ca0eb`
- 时间/作者: 2025-11-05 / Kunshang Ji
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/utils/fa_utils.py`, `vllm/model_executor/layers/quantization/mxfp4.py`, `vllm/model_executor/models/gpt_oss.py`, `vllm/v1/attention/backends/flash_attn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/gpt_oss.py`
  - runtime-perf: `vllm/attention/utils/fa_utils.py`; `vllm/model_executor/layers/quantization/mxfp4.py`; `vllm/v1/attention/backends/flash_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2d977a7a9` - [ROCm] gemm_a16w16 upstreaming (#26969)

- 完整 hash: `2d977a7a9ead3179fde9ed55d69393ef7b6cec47`
- 时间/作者: 2025-11-04 / Aleksandr Malyshev
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/utils.py`, `vllm/model_executor/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/utils.py`; `vllm/model_executor/models/gpt_oss.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `32257297d` - [CI/Build] Remove the flaky gpt-oss lora test (#27966)

- 完整 hash: `32257297dd4dcb996a0fb4641c2018289d20396b`
- 时间/作者: 2025-11-03 / Jee Jee Li
- 自动分类: 测试/文档/基准
- 主要文件: `tests/lora/test_gptoss_tp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `tests/lora/test_gptoss_tp.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `0384aa715` - [CI/Build] Add gpt-oss LoRA test (#27870)

- 完整 hash: `0384aa7150c4c9778efca041ffd1beb3ad2bd694`
- 时间/作者: 2025-10-31 / Jee Jee Li
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `tests/lora/conftest.py`, `tests/lora/test_deepseekv2_tp.py`, `tests/lora/test_gptoss.py`, `tests/lora/test_gptoss_tp.py`, `tests/lora/test_qwen3moe_tp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`
  - tests: `tests/lora/conftest.py`; `tests/lora/test_deepseekv2_tp.py`; `tests/lora/test_gptoss.py`; `tests/lora/test_gptoss_tp.py`; `tests/lora/test_qwen3moe_tp.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `e5e076cad` - [BugFix] Stopgap - Flashinfer Autotuner + GPT-OSS + DP/TP (#27762)

- 完整 hash: `e5e076cad7c1c922fa6d48049c45bead505f52a6`
- 时间/作者: 2025-10-30 / Varun Sundar Rabindranath
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/warmup/kernel_warmup.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `vllm/model_executor/warmup/kernel_warmup.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ab2eb27b7` - [Frontend] [gpt-oss] Mcp type bug (#27689)

- 完整 hash: `ab2eb27b74da0e6846749c11a68179d27a78d963`
- 时间/作者: 2025-10-29 / Alec S
- 自动分类: 缺陷修复
- 主要文件: `tests/entrypoints/openai/test_response_api_mcp_tools.py`, `tests/entrypoints/openai/test_serving_responses.py`, `tests/entrypoints/test_harmony_utils.py`, `tests/test_envs.py`, `vllm/entrypoints/harmony_utils.py`, `vllm/entrypoints/openai/serving_responses.py`, `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/entrypoints/harmony_utils.py`; `vllm/entrypoints/openai/serving_responses.py`
  - tests: `tests/entrypoints/openai/test_response_api_mcp_tools.py`; `tests/entrypoints/openai/test_serving_responses.py`; `tests/entrypoints/test_harmony_utils.py`; `tests/test_envs.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3c7fefdeb` - [Frontend] [gpt-oss] Tool json call parsing error retry (#27675)

- 完整 hash: `3c7fefdeba183e5c5e575f668b797549530f5a3d`
- 时间/作者: 2025-10-29 / Alec S
- 自动分类: 缺陷修复
- 主要文件: `vllm/entrypoints/context.py`, `vllm/entrypoints/harmony_utils.py`, `vllm/envs.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/envs.py`
  - runtime-model: `vllm/entrypoints/context.py`; `vllm/entrypoints/harmony_utils.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
