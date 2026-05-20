# vllm Mixtral Quark INT4/FP8 MoE Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `docs/features/quantization/quark.md` | `d20180733`, `7ed27f3cb`, `2bb4435cb`, `05576df85` |
| `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-fi-cutlass.yaml` | `31c29257c` |
| `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-triton.yaml` | `31c29257c` |
| `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-fi-cutlass.yaml` | `d3e477c01` |
| `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-triton.yaml` | `d3e477c01` |
| `tests/lora/test_mixtral.py` | `6b2b9fd93` |
| `tests/quantization/untest_quark.py` | no direct commit |
| `vllm/model_executor/layers/quantization/quark/__init__.py` | no direct commit |
| `vllm/model_executor/layers/quantization/quark/quark.py` | `0c738b58b`, `fc1d8be3d`, `d0a73620c`, `0b2549899`, `05576df85` |
| `vllm/model_executor/layers/quantization/quark/quark_moe.py` | `dc917cceb`, `327a02d8d`, `e74698c27`, `5dcd7ef1f`, `9152a30d8`, `54c892438`, `0c738b58b`, `00e5cbb96`, `c6df05ebb`, `8f066146c`, `f080a8351`, `b06b9470c`, ... (13 total) |
| `vllm/model_executor/layers/quantization/quark/schemes/__init__.py` | no direct commit |
| `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py` | `9b67338b7`, `b89275d01`, `04a797cd0`, `b7f1f490a`, `f080a8351` |
| `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py` | no direct commit |
| `vllm/model_executor/layers/quantization/quark/schemes/quark_w8a8_fp8.py` | `148117ea2` |
| `vllm/model_executor/layers/quantization/quark/schemes/quark_w8a8_int8.py` | `148117ea2` |
| `vllm/model_executor/layers/quantization/quark/utils.py` | `8c11001ba` |
| `vllm/model_executor/models/mixtral.py` | `df7041633`, `dcd80206b`, `482914849`, `cf3eacfe5`, `39e63dec7`, `430dd4d9e`, `9875be643`, `a8b70304d`, `97d1c9930`, `e50c45467` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 43
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-22 | `dc917cceb` | 性能/后端优化 | [MoE Refactor] Move `select_experts` from `FusedMoEQuantMethod` -> `FusedMoE` (#31996) | `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py` |
| 2026-01-21 | `9b67338b7` | 性能/后端优化 | [Bugfix] Suppress log on non-ROCm platform (#32703) | `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py` |
| 2026-01-20 | `148117ea2` | 性能/后端优化 | [Refactor] Make FP8 Linear Ops use kernel abstraction (#27814) | `.buildkite/lm-eval-harness/configs/models-small-rocm.txt`, `tests/compile/distributed/test_fusion_all_reduce.py`, `tests/compile/distributed/test_sequence_parallelism.py` |
| 2026-01-18 | `327a02d8d` | 性能/后端优化 | [MoE Refactor] Separate Router into OO Classes (#30623) | `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py` |
| 2026-01-15 | `31c29257c` | 性能/后端优化 | [MoE Refactor][17/N] Apply Refactor to Bf16 (#31827) | `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml` |
| 2026-01-15 | `8c11001ba` | 性能/后端优化 | [ROCM] DSfp4 mla projection gemms weight dynamic quantization (#32238) | `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py` |
| 2026-01-15 | `b89275d01` | 性能/后端优化 | [ROCm] Improve error handling while loading quantized model on gfx120… (#31715) | `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py` |
| 2026-01-08 | `e74698c27` | 性能/后端优化 | [Misc][Refactor] Add FusedMoERouter object (#30519) | `tests/test_routing_simulator.py`, `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py` |
| 2026-01-07 | `5dcd7ef1f` | 性能/后端优化 | [MoE Refactor][15/N] Apply Refactor to Fp8 (#31415) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `d3e477c01` | 性能/后端优化 | [MoE Refactor] Add Temporary Integration Tests - H100/B200 (#31759) | `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml` |
| 2025-12-29 | `9152a30d8` | 性能/后端优化 | [MoE Refactor][12/N] Marlin Fp8 MoE Pure Function (#31499) | `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py` |
| 2025-12-24 | `d20180733` | 性能/后端优化 | [Chore] Bump `lm-eval` version (#31264) | `.buildkite/lm-eval-harness/run-lm-eval-chartqa-vllm-vlm-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-gsm-hf-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-gsm-vllm-baseline.sh` |
| 2025-12-24 | `b41aeb346` | 性能/后端优化 | [Bugfix][ROCm] Fix load issue on deepseek quark quantization when shared expert enabled (#31261) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-20 | `54c892438` | 性能/后端优化 | [MoE Refactor][5/N] Isolate zero expert to LongCatFlash (#28891) | `tests/test_routing_simulator.py`, `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py` |
| 2025-12-17 | `0c738b58b` | 性能/后端优化 | [Quantization] Support Quark int4-fp8 w4a8 for MoE (#30071) | `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-11 | `5a87d8b9b` | 性能/后端优化 | [Deprecation] Remove deprecated plugin and compilation fields for v0.13 release (#30396) | `docs/design/plugin_system.md`, `tests/compile/test_config.py`, `tests/kernels/moe/test_ocp_mx_moe.py` |
| 2025-12-10 | `06462392e` | 性能/后端优化 | [bugfix][quantization] fix quark qwen3 kv_cache quantization (#30308) | `vllm/model_executor/models/qwen3_moe.py` |
| 2025-12-09 | `00e5cbb96` | 性能/后端优化 | [MoE][Refactor] Remove most arguments to FusedMoEMethodBase.apply (#29066) | `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py` |
| 2025-12-08 | `c6df05ebb` | 性能/后端优化 | [ROCm] [Fused Moe EP] Use binary expert mask for aiter fused moe kernel (#29773) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py` |
| 2025-11-29 | `04a797cd0` | 性能/后端优化 | [Doc]: fixing typos in various files. (#29717) | `vllm/distributed/device_communicators/pynccl_allocator.py`, `vllm/distributed/parallel_state.py`, `vllm/entrypoints/openai/serving_models.py` |
| 2025-11-29 | `39e63dec7` | 性能/后端优化 | [LoRA] Cleanup LoRA unused code (#29611) | `examples/offline_inference/multilora_inference.py`, `tests/entrypoints/conftest.py`, `tests/entrypoints/openai/test_basic.py` |
| 2025-11-27 | `fc1d8be3d` | 性能/后端优化 | [Attention] Update attention imports (#29540) | `tests/v1/attention/test_rocm_attention_backends_selection.py`, `tests/v1/kv_connector/unit/test_backwards_compatibility.py`, `vllm/attention/backends/abstract.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-24 | `8f066146c` | 性能/后端优化 | [MoE][Refactor] Make select_experts a non-static method (#29067) | `tests/kernels/moe/test_flashinfer.py`, `tests/test_routing_simulator.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py` |
| 2025-11-21 | `b7f1f490a` | 性能/后端优化 | Upstream triton fp4 weight preshuffle (#28888) | `vllm/_aiter_ops.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py` |
| 2025-11-21 | `9875be643` | 性能/后端优化 | [LoRA][2/2]Remove LoRA extra vocab (#28545) | `tests/lora/conftest.py`, `tests/lora/test_layers.py`, `tests/lora/test_llama_tp.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-19 | `7ed27f3cb` | 性能/后端优化 | [Doc]: fix typos in various files (#28945) | `docs/design/moe_kernel_features.md`, `docs/design/plugin_system.md`, `docs/features/quantization/quark.md` |
| 2025-11-18 | `d0a73620c` | 性能/后端优化 | [ROCm][Quantization] add apply_vllm_mapper in quark config for models like gpt-oss (#28638) | `vllm/model_executor/layers/quantization/quark/quark.py` |
| 2025-11-15 | `2bb4435cb` | 性能/后端优化 | [Doc]: fix typos in various files (#28567) | `docs/design/moe_kernel_features.md`, `docs/features/quantization/quark.md`, `vllm/compilation/compiler_interface.py` |
| 2025-11-14 | `0b2549899` | 性能/后端优化 | [Misc] add ignore mapper for quark quantization (#28275) | `vllm/model_executor/layers/quantization/quark/quark.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-11 | `9f0247cfa` | 性能/后端优化 | `VLLM_USE_TRITON_FLASH_ATTN` V0 variable deprecation (#27611) | `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `tests/kernels/test_triton_flash_attention.py`, `tests/models/language/pooling/test_classification.py` |
| 2025-11-12 | `05576df85` | 性能/后端优化 | [ROCm][Quantization] extend AMD Quark to support mixed-precision quantized model (#24239) | `docs/features/quantization/quark.md`, `tests/quantization/test_mixed_precision.py`, `vllm/model_executor/layers/quantization/quark/quark.py` |
| 2025-11-10 | `f080a8351` | 性能/后端优化 | [RFC][ROCm][AITER] Keep all AITER kernels in `_aiter_ops` class like `_custom_ops` and `_ipex_ops` (#24490) | `docs/design/moe_kernel_features.md`, `tests/kernels/moe/test_moe.py`, `tests/model_executor/test_enabled_custom_ops.py` |
| 2025-11-10 | `b06b9470c` | 性能/后端优化 | [Rocm][fused_moe][fp4] view weight to torch.float4_e2m1fn_x2 when running aiter fused moe for fp4 model (#27474) | `vllm/model_executor/layers/quantization/quark/quark_moe.py` |
| 2025-11-09 | `6b2b9fd93` | 模型支持/运行时入口 | [CI] lora/test_mixtral.py : Add additional expected outputs due to flakiness (#28322) | `tests/lora/test_mixtral.py` |
| 2025-11-05 | `e50c45467` | 性能/后端优化 | [BugFix] Support EP/DP + EPLB with MTP (#25311) | `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py` |
| 2025-11-04 | `938772af0` | 性能/后端优化 | [Kernels] Isolate modular kernel code from FusedMoEMethodBase subclasses. (#27123) | `vllm/distributed/device_communicators/base_device_communicator.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py` |

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

### Commit `dc917cceb` - [MoE Refactor] Move `select_experts` from `FusedMoEQuantMethod` -> `FusedMoE` (#31996)

- Full hash: `dc917cceb877dfd13f98c538c4c96158047d98bd`
- Date/author: 2026-01-22 / bnellnm
- Auto category: 性能/后端优化
- Main files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/router/base_router.py`, `vllm/model_executor/layers/fused_moe/router/custom_routing_router.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py` 等 22 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`; `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`; `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/router/base_router.py`; `vllm/model_executor/layers/fused_moe/router/custom_routing_router.py`; `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`; `vllm/model_executor/layers/fused_moe/router/router_factory.py` 等 21 个文件
  - tests: `tests/kernels/moe/test_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9b67338b7` - [Bugfix] Suppress log on non-ROCm platform (#32703)

- Full hash: `9b67338b78f33dca5726191cead98ed913a96f4a`
- Date/author: 2026-01-21 / TJian
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `148117ea2` - [Refactor] Make FP8 Linear Ops use kernel abstraction (#27814)

- Full hash: `148117ea2e689cd43df4be6892671a17cdae5833`
- Date/author: 2026-01-20 / vllmellm
- Auto category: 性能/后端优化
- Main files: `.buildkite/lm-eval-harness/configs/models-small-rocm.txt`, `tests/compile/distributed/test_fusion_all_reduce.py`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py`, `tests/compile/test_fusion.py`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_silu_mul_quant_fusion.py`, `tests/kernels/quantization/test_scaled_mm_kernel_selection.py` 等 30 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/lm-eval-harness/configs/models-small-rocm.txt`
  - other: `vllm/_aiter_ops.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`; `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `vllm/model_executor/layers/quantization/fbgemm_fp8.py`; `vllm/model_executor/layers/quantization/fp8.py`; `vllm/model_executor/layers/quantization/kernels/scaled_mm/ScaledMMLinearKernel.py`; `vllm/model_executor/layers/quantization/kernels/scaled_mm/__init__.py`; `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`; `vllm/model_executor/layers/quantization/kernels/scaled_mm/cpu.py` 等 19 个文件
  - tests: `tests/compile/distributed/test_fusion_all_reduce.py`; `tests/compile/distributed/test_sequence_parallelism.py`; `tests/compile/test_functionalization.py`; `tests/compile/test_fusion.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_silu_mul_quant_fusion.py`; `tests/kernels/quantization/test_scaled_mm_kernel_selection.py`; `tests/quantization/test_compressed_tensors.py` 等 9 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `31c29257c` - [MoE Refactor][17/N] Apply Refactor to Bf16 (#31827)

- Full hash: `31c29257c852c429a655dd35a1c373ccd46f97da`
- Date/author: 2026-01-15 / Yongye Zhu
- Auto category: 性能/后端优化
- Main files: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-triton.yaml` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-BF16-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-BF16-triton.yaml` 等 10 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8c11001ba` - [ROCM] DSfp4 mla projection gemms weight dynamic quantization (#32238)

- Full hash: `8c11001ba2110134df3c3aecc63f2559ad1f5996`
- Date/author: 2026-01-15 / Aleksandr Malyshev
- Auto category: 性能/后端优化
- Main files: `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/quantization/quark/utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/_aiter_ops.py`; `vllm/envs.py`
  - runtime-perf: `vllm/model_executor/layers/attention/mla_attention.py`; `vllm/model_executor/layers/quantization/quark/utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b89275d01` - [ROCm] Improve error handling while loading quantized model on gfx120… (#31715)

- Full hash: `b89275d018796170acbb91b8bcddbc8b8213025e`
- Date/author: 2026-01-15 / brian033
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e74698c27` - [Misc][Refactor] Add FusedMoERouter object (#30519)

- Full hash: `e74698c27ad5a66bb0f1b131a9e5582a0fbf00d1`
- Date/author: 2026-01-08 / bnellnm
- Auto category: 性能/后端优化
- Main files: `tests/test_routing_simulator.py`, `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`, `vllm/model_executor/layers/fused_moe/fused_moe_router.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/quantization/awq_marlin.py` 等 20 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/__init__.py`; `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`; `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`; `vllm/model_executor/layers/fused_moe/fused_moe_router.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/model_executor/layers/quantization/awq_marlin.py`; `vllm/model_executor/layers/quantization/bitsandbytes.py` 等 19 个文件
  - tests: `tests/test_routing_simulator.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5dcd7ef1f` - [MoE Refactor][15/N] Apply Refactor to Fp8 (#31415)

- Full hash: `5dcd7ef1f219068e6b6be5b614bc43978f028651`
- Date/author: 2026-01-07 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`, `benchmarks/kernels/benchmark_moe.py`, `docs/design/moe_kernel_features.md`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ht.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml` 等 38 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`; `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`; `benchmarks/kernels/benchmark_moe.py`; `docs/design/moe_kernel_features.md`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/__init__.py`; `vllm/model_executor/layers/fused_moe/cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/fallback.py`; `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`; `vllm/model_executor/layers/fused_moe/oracle/__init__.py`; `vllm/model_executor/layers/fused_moe/oracle/fp8.py`; `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/triton_deep_gemm_moe.py` 等 16 个文件
  - tests: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ht.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ht.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-CT-fi-cutlass.yaml` 等 17 个文件
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

### Commit `d3e477c01` - [MoE Refactor] Add Temporary Integration Tests - H100/B200 (#31759)

- Full hash: `d3e477c01342f800790b170b8fa799b467621358`
- Date/author: 2026-01-06 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-marlin.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-fi-cutlass.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-triton.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml` 等 30 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - tests: `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-trtllm.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-marlin.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Mixtral-8x7B-Fp8-AutoFp8-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-cutlass.yaml` 等 29 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `9152a30d8` - [MoE Refactor][12/N] Marlin Fp8 MoE Pure Function (#31499)

- Full hash: `9152a30d8f6f85cbc5505fafb6f6682d4e189884`
- Date/author: 2025-12-29 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils_fp8.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/fp8.py`; `vllm/model_executor/layers/quantization/quark/quark_moe.py`; `vllm/model_executor/layers/quantization/utils/marlin_utils_fp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d20180733` - [Chore] Bump `lm-eval` version (#31264)

- Full hash: `d201807339697c6c8206ae08d2cdccfc25cb1ce1`
- Date/author: 2025-12-24 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `.buildkite/lm-eval-harness/run-lm-eval-chartqa-vllm-vlm-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-gsm-hf-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-gsm-vllm-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-mmlupro-vllm-baseline.sh`, `.buildkite/scripts/hardware_ci/run-tpu-v1-test-part2.sh`, `.buildkite/scripts/hardware_ci/run-tpu-v1-test.sh`, `docs/features/quantization/fp8.md`, `docs/features/quantization/int4.md` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/lm-eval-harness/run-lm-eval-chartqa-vllm-vlm-baseline.sh`; `.buildkite/lm-eval-harness/run-lm-eval-gsm-hf-baseline.sh`; `.buildkite/lm-eval-harness/run-lm-eval-gsm-vllm-baseline.sh`; `.buildkite/lm-eval-harness/run-lm-eval-mmlupro-vllm-baseline.sh`; `.buildkite/scripts/hardware_ci/run-tpu-v1-test-part2.sh`; `.buildkite/scripts/hardware_ci/run-tpu-v1-test.sh`
  - docs-bench: `docs/features/quantization/fp8.md`; `docs/features/quantization/int4.md`; `docs/features/quantization/int8.md`; `docs/features/quantization/quark.md`
  - other: `requirements/nightly_torch_test.txt`; `requirements/test.in`; `requirements/test.txt`
  - runtime-perf: `requirements/rocm-test.txt`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b41aeb346` - [Bugfix][ROCm] Fix load issue on deepseek quark quantization when shared expert enabled (#31261)

- Full hash: `b41aeb3468fecb33b7934fc7ca5406bdba84dace`
- Date/author: 2025-12-24 / Pleaplusone
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/deepseek_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `54c892438` - [MoE Refactor][5/N] Isolate zero expert to LongCatFlash (#28891)

- Full hash: `54c892438479c0a8aec9a10b8db570034af92443`
- Date/author: 2025-12-20 / baonudesifeizhai
- Auto category: 性能/后端优化
- Main files: `tests/test_routing_simulator.py`, `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/fused_moe/zero_expert_fused_moe.py`, `vllm/model_executor/layers/quantization/awq_marlin.py`, `vllm/model_executor/layers/quantization/bitsandbytes.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/__init__.py`; `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/model_executor/layers/fused_moe/zero_expert_fused_moe.py`; `vllm/model_executor/layers/quantization/awq_marlin.py`; `vllm/model_executor/layers/quantization/bitsandbytes.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py` 等 18 个文件
  - tests: `tests/test_routing_simulator.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0c738b58b` - [Quantization] Support Quark int4-fp8 w4a8 for MoE (#30071)

- Full hash: `0c738b58bc0e5a5bf2448c95fc2014b83127a4d5`
- Date/author: 2025-12-17 / Bowen Bao
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/quark.py`; `vllm/model_executor/layers/quantization/quark/quark_moe.py`
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

### Commit `5a87d8b9b` - [Deprecation] Remove deprecated plugin and compilation fields for v0.13 release (#30396)

- Full hash: `5a87d8b9b1f357a65a9b73773178ae17fd7cd9c8`
- Date/author: 2025-12-11 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `docs/design/plugin_system.md`, `tests/compile/test_config.py`, `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/quantization/test_quark.py`, `tests/test_config.py`, `vllm/attention/backends/registry.py`, `vllm/attention/selector.py`, `vllm/config/compilation.py` 等 10 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/design/plugin_system.md`
  - other: `vllm/engine/arg_utils.py`
  - runtime-model: `vllm/config/compilation.py`; `vllm/config/vllm.py`
  - runtime-perf: `vllm/attention/backends/registry.py`; `vllm/attention/selector.py`
  - tests: `tests/compile/test_config.py`; `tests/kernels/moe/test_ocp_mx_moe.py`; `tests/quantization/test_quark.py`; `tests/test_config.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `06462392e` - [bugfix][quantization] fix quark qwen3 kv_cache quantization (#30308)

- Full hash: `06462392e40f9ae1bf87290c4cec10533fdd3205`
- Date/author: 2025-12-10 / haoyangli-amd
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `00e5cbb96` - [MoE][Refactor] Remove most arguments to FusedMoEMethodBase.apply (#29066)

- Full hash: `00e5cbb96789fd9d083b4015cdcff318e4de3808`
- Date/author: 2025-12-09 / bnellnm
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/quantization/awq_marlin.py`, `vllm/model_executor/layers/quantization/bitsandbytes.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/__init__.py`; `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`; `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/model_executor/layers/quantization/awq_marlin.py`; `vllm/model_executor/layers/quantization/bitsandbytes.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py` 等 18 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c6df05ebb` - [ROCm] [Fused Moe EP] Use binary expert mask for aiter fused moe kernel (#29773)

- Full hash: `c6df05ebb49901510890aea7c7411a17a38c0a8f`
- Date/author: 2025-12-08 / Zhiwei
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/quantization/quark/quark_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `04a797cd0` - [Doc]: fixing typos in various files. (#29717)

- Full hash: `04a797cd0e94567ee2b158a0246d6112a197fdc5`
- Date/author: 2025-11-29 / Didier Durand
- Auto category: 性能/后端优化
- Main files: `vllm/distributed/device_communicators/pynccl_allocator.py`, `vllm/distributed/parallel_state.py`, `vllm/entrypoints/openai/serving_models.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`, `vllm/transformers_utils/repo_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/transformers_utils/repo_utils.py`
  - runtime-model: `vllm/entrypoints/openai/serving_models.py`
  - runtime-perf: `vllm/distributed/device_communicators/pynccl_allocator.py`; `vllm/distributed/parallel_state.py`; `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`
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

### Commit `fc1d8be3d` - [Attention] Update attention imports (#29540)

- Full hash: `fc1d8be3dc97e33ade7fb578451006bb044a5e60`
- Date/author: 2025-11-27 / Matthew Bonanni
- Auto category: 性能/后端优化
- Main files: `tests/v1/attention/test_rocm_attention_backends_selection.py`, `tests/v1/kv_connector/unit/test_backwards_compatibility.py`, `vllm/attention/backends/abstract.py`, `vllm/attention/layers/chunked_local_attention.py`, `vllm/config/model.py`, `vllm/config/multimodal.py`, `vllm/distributed/kv_transfer/kv_connector/v1/base.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py` 等 38 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/forward_context.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/tpu.py`; `vllm/platforms/xpu.py`; `vllm/v1/kv_offload/spec.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/v1/worker/utils.py`
  - runtime-perf: `vllm/attention/backends/abstract.py`; `vllm/attention/layers/chunked_local_attention.py`; `vllm/distributed/kv_transfer/kv_connector/v1/base.py`; `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/vllm_v1_adapter.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py` 等 25 个文件
  - tests: `tests/v1/attention/test_rocm_attention_backends_selection.py`; `tests/v1/kv_connector/unit/test_backwards_compatibility.py`
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

### Commit `8f066146c` - [MoE][Refactor] Make select_experts a non-static method (#29067)

- Full hash: `8f066146c395dfadb86914c88d9a0f3173f8fa39`
- Date/author: 2025-11-24 / bnellnm
- Auto category: 性能/后端优化
- Main files: `tests/kernels/moe/test_flashinfer.py`, `tests/test_routing_simulator.py`, `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/quantization/awq_marlin.py`, `vllm/model_executor/layers/quantization/bitsandbytes.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`; `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`; `vllm/model_executor/layers/quantization/awq_marlin.py`; `vllm/model_executor/layers/quantization/bitsandbytes.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/experts_int8.py` 等 16 个文件
  - tests: `tests/kernels/moe/test_flashinfer.py`; `tests/test_routing_simulator.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b7f1f490a` - Upstream triton fp4 weight preshuffle (#28888)

- Full hash: `b7f1f490a61c99d0b371e39aefbe5546cba231a9`
- Date/author: 2025-11-21 / Aleksandr Malyshev
- Auto category: 性能/后端优化
- Main files: `vllm/_aiter_ops.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/_aiter_ops.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9875be643` - [LoRA][2/2]Remove LoRA extra vocab  (#28545)

- Full hash: `9875be6431872b513a8554c518e48ad79eba4656`
- Date/author: 2025-11-21 / Jee Jee Li
- Auto category: 性能/后端优化
- Main files: `tests/lora/conftest.py`, `tests/lora/test_layers.py`, `tests/lora/test_llama_tp.py`, `tests/lora/test_lora_functions.py`, `tests/lora/test_lora_manager.py`, `tests/lora/test_worker.py`, `tests/lora/utils.py`, `vllm/config/lora.py` 等 28 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/engine/arg_utils.py`; `vllm/lora/layers/base.py`; `vllm/lora/layers/base_linear.py`; `vllm/lora/layers/column_parallel_linear.py`; `vllm/lora/layers/logits_processor.py`; `vllm/lora/layers/vocal_parallel_embedding.py`; `vllm/lora/lora_weights.py`; `vllm/lora/models.py` 等 13 个文件
  - runtime-model: `vllm/config/lora.py`; `vllm/lora/worker_manager.py`; `vllm/model_executor/models/granite.py`; `vllm/model_executor/models/llama.py`; `vllm/model_executor/models/mixtral.py`; `vllm/model_executor/models/teleflm.py`; `vllm/v1/worker/tpu_model_runner.py`
  - runtime-perf: `vllm/lora/layers/fused_moe.py`
  - tests: `tests/lora/conftest.py`; `tests/lora/test_layers.py`; `tests/lora/test_llama_tp.py`; `tests/lora/test_lora_functions.py`; `tests/lora/test_lora_manager.py`; `tests/lora/test_worker.py`; `tests/lora/utils.py`
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

### Commit `7ed27f3cb` - [Doc]: fix typos in various files (#28945)

- Full hash: `7ed27f3cb55e3f64614300ec7acde1b382a48541`
- Date/author: 2025-11-19 / Didier Durand
- Auto category: 性能/后端优化
- Main files: `docs/design/moe_kernel_features.md`, `docs/design/plugin_system.md`, `docs/features/quantization/quark.md`, `examples/online_serving/prometheus_grafana/README.md`, `vllm/engine/arg_utils.py`, `vllm/envs.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/design/moe_kernel_features.md`; `docs/design/plugin_system.md`; `docs/features/quantization/quark.md`; `examples/online_serving/prometheus_grafana/README.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/envs.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `d0a73620c` - [ROCm][Quantization] add apply_vllm_mapper in quark config for models like gpt-oss (#28638)

- Full hash: `d0a73620cc85a840323d25b28772efac04c006e2`
- Date/author: 2025-11-18 / xuebwang-amd
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/quark/quark.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/quark.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2bb4435cb` - [Doc]: fix typos in various files (#28567)

- Full hash: `2bb4435cb7e2e2317b0f20803347690fb38fe6b4`
- Date/author: 2025-11-15 / Didier Durand
- Auto category: 性能/后端优化
- Main files: `docs/design/moe_kernel_features.md`, `docs/features/quantization/quark.md`, `vllm/compilation/compiler_interface.py`, `vllm/compilation/decorators.py`, `vllm/v1/worker/gpu_model_runner.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/design/moe_kernel_features.md`; `docs/features/quantization/quark.md`
  - other: `vllm/compilation/compiler_interface.py`; `vllm/compilation/decorators.py`
  - runtime-model: `vllm/v1/worker/gpu_model_runner.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `0b2549899` - [Misc] add ignore mapper for quark quantization (#28275)

- Full hash: `0b25498990f01ea2553c02731d6e2ce2d550156a`
- Date/author: 2025-11-14 / haoyangli-amd
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/quark/quark.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/quark.py`
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

### Commit `9f0247cfa` - `VLLM_USE_TRITON_FLASH_ATTN` V0 variable deprecation (#27611)

- Full hash: `9f0247cfa40a52356aa7860c163c062eb086d266`
- Date/author: 2025-11-11 / Andreas Karatzas
- Auto category: 性能/后端优化
- Main files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `tests/kernels/test_triton_flash_attention.py`, `tests/models/language/pooling/test_classification.py`, `tests/models/language/pooling/test_embedding.py`, `tests/models/language/pooling/test_mm_classifier_conversion.py`, `tests/models/language/pooling/test_reward.py`, `tests/models/multimodal/generation/test_common.py`, `tests/models/multimodal/generation/test_phi4_multimodal.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/hardware_ci/run-amd-test.sh`
  - other: `vllm/envs.py`; `vllm/usage/usage_lib.py`
  - runtime-perf: `vllm/attention/ops/triton_flash_attention.py`; `vllm/platforms/rocm.py`; `vllm/v1/attention/backends/mla/triton_mla.py`
  - tests: `tests/kernels/test_triton_flash_attention.py`; `tests/models/language/pooling/test_classification.py`; `tests/models/language/pooling/test_embedding.py`; `tests/models/language/pooling/test_mm_classifier_conversion.py`; `tests/models/language/pooling/test_reward.py`; `tests/models/multimodal/generation/test_common.py`; `tests/models/multimodal/generation/test_phi4_multimodal.py`; `tests/models/multimodal/generation/test_phi4mm.py` 等 9 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `05576df85` - [ROCm][Quantization] extend AMD Quark to support mixed-precision quantized model (#24239)

- Full hash: `05576df85c5274ee3045d90b0779d4adeecc09b9`
- Date/author: 2025-11-12 / xuebwang-amd
- Auto category: 性能/后端优化
- Main files: `docs/features/quantization/quark.md`, `tests/quantization/test_mixed_precision.py`, `vllm/model_executor/layers/quantization/quark/quark.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/features/quantization/quark.md`
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/quark.py`
  - tests: `tests/quantization/test_mixed_precision.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f080a8351` - [RFC][ROCm][AITER] Keep all AITER kernels in `_aiter_ops` class like `_custom_ops` and `_ipex_ops` (#24490)

- Full hash: `f080a83511511a9c0a222451a752a1623aec095d`
- Date/author: 2025-11-10 / vllmellm
- Auto category: 性能/后端优化
- Main files: `docs/design/moe_kernel_features.md`, `tests/kernels/moe/test_moe.py`, `tests/model_executor/test_enabled_custom_ops.py`, `vllm/_aiter_ops.py`, `vllm/attention/ops/rocm_aiter_mla.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py` 等 25 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/design/moe_kernel_features.md`
  - other: `vllm/_aiter_ops.py`; `vllm/envs.py`
  - runtime-model: `vllm/model_executor/layers/layernorm.py`; `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`; `vllm/model_executor/models/deepseek_v2.py`
  - runtime-perf: `vllm/attention/ops/rocm_aiter_mla.py`; `vllm/model_executor/layers/fused_moe/fused_moe.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`; `vllm/model_executor/layers/quantization/fp8.py`; `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py` 等 16 个文件
  - tests: `tests/kernels/moe/test_moe.py`; `tests/model_executor/test_enabled_custom_ops.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b06b9470c` - [Rocm][fused_moe][fp4] view weight to torch.float4_e2m1fn_x2 when running aiter fused moe for fp4 model (#27474)

- Full hash: `b06b9470ca881f89feea72e4d89b20c213f360d4`
- Date/author: 2025-11-10 / zejunchen-zejun
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/quantization/quark/quark_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/quantization/quark/quark_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6b2b9fd93` - [CI] lora/test_mixtral.py : Add additional expected outputs due to flakiness (#28322)

- Full hash: `6b2b9fd934af2bf59f749aa04ac739fd9c7d29f7`
- Date/author: 2025-11-09 / Varun Sundar Rabindranath
- Auto category: 模型支持/运行时入口
- Main files: `tests/lora/test_mixtral.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/lora/test_mixtral.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `938772af0` - [Kernels] Isolate modular kernel code from FusedMoEMethodBase subclasses. (#27123)

- Full hash: `938772af03ce01590c7e92b0d3fd0a5bdc899d19`
- Date/author: 2025-11-04 / bnellnm
- Auto category: 性能/后端优化
- Main files: `vllm/distributed/device_communicators/base_device_communicator.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py`, `vllm/model_executor/layers/quantization/awq_marlin.py`, `vllm/model_executor/layers/quantization/bitsandbytes.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/experts_int8.py`, `vllm/model_executor/layers/quantization/fp8.py` 等 16 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/warmup/deep_gemm_warmup.py`
  - runtime-perf: `vllm/distributed/device_communicators/base_device_communicator.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/fused_moe/modular_kernel.py`; `vllm/model_executor/layers/quantization/awq_marlin.py`; `vllm/model_executor/layers/quantization/bitsandbytes.py`; `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`; `vllm/model_executor/layers/quantization/experts_int8.py`; `vllm/model_executor/layers/quantization/fp8.py` 等 15 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
