# sglang Mixtral Quark INT4/FP8 MoE Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/layers/quantization/quark/__init__.py` | no direct commit |
| `python/sglang/srt/layers/quantization/quark/quark.py` | `f0d78f2e2`, `150ed881b`, `0d49b13fd` |
| `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` | `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py` | `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` | `e9d6aefa9`, `5172c3784`, `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` | `61a902ce8`, `048d90e16`, `941945371`, `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` | `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | `e9d6aefa9`, `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/utils.py` | `8d2892330` |
| `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` | `e9d6aefa9`, `5af84c8af` |
| `python/sglang/srt/models/mixtral.py` | `d1e95af28` |
| `python/sglang/srt/models/mixtral_quant.py` | `d1e95af28`, `20282f566` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 12
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |
| 2026-03-25 | `61a902ce8` | 性能/后端优化 | [AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype. (#21040) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/layers/quantization/fp8.py` |
| 2026-03-20 | `048d90e16` | 性能/后端优化 | Revert "[AMD] Add MoE weights and scales padding" (#21067) | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-21 | `941945371` | 性能/后端优化 | [AMD] Add MoE weights and scales padding (#18684) | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-02 | `20282f566` | 性能/后端优化 | [fix typo] expert_indicies -> expert_indices (#19627) | `python/sglang/srt/models/mixtral_quant.py` |
| 2026-02-27 | `f0d78f2e2` | 性能/后端优化 | [AMD] Fix weight load shape mismatch for amd dsr1 0528 mxfp4 (#19425) | `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/deepseek_nextn.py` |
| 2026-02-27 | `5172c3784` | 性能/后端优化 | [AMD] Use fused GEMM with FP8 cast for FP8 prefill (#19422) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-02-18 | `150ed881b` | 性能/后端优化 | [4/N] Quantization Refactor: Quark MoE schemes (#18252) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` |
| 2026-02-11 | `8d2892330` | 性能/后端优化 | chore: fix some typos (#18577) | `python/sglang/srt/layers/attention/double_sparsity_backend.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/int8_kernel.py` |
| 2026-01-21 | `0d49b13fd` | 性能/后端优化 | Fix circular import in quantization modules (#17372) | `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/auto_round.py`, `python/sglang/srt/layers/quantization/petit.py` |
| 2026-01-14 | `5af84c8af` | 性能/后端优化 | [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm (#7392) | `docs/advanced_features/quantization.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/int4fp8_utils.py` |

## Per-Commit Audit Cards

### Commit `e9d6aefa9` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- Full hash: `e9d6aefa947699a1edc971ecc2e3fdd2053f525f`
- Date/author: 2026-03-30 / lizhigong
- Auto category: 性能/后端优化
- Main files: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README_DCU.md`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py` 等 25 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/server_args.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `61a902ce8` - [AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype. (#21040)

- Full hash: `61a902ce88ea278ccc1dad0b5d7437a67724d868`
- Date/author: 2026-03-25 / Duyi-Wang
- Auto category: 性能/后端优化
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/amd/test_moriep_small.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`
  - tests: `test/registered/amd/test_moriep_small.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `048d90e16` - Revert "[AMD] Add MoE weights and scales padding" (#21067)

- Full hash: `048d90e1651a3842253ce5291162a4840e9ee5cc`
- Date/author: 2026-03-20 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/model_executor/model_runner.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `941945371` - [AMD] Add MoE weights and scales padding (#18684)

- Full hash: `9419453713146b1be0c21e6d328f435f1db95da6`
- Date/author: 2026-03-21 / mqhc2020
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/model_executor/model_runner.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d1e95af28` - Upgrade transformers==5.3.0 (#17784)

- Full hash: `d1e95af282068a751ee6a8b60a0ae2a90c464819`
- Date/author: 2026-03-18 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py` 等 88 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/layers/rotary_embedding/factory.py`; `python/sglang/srt/managers/tokenizer_manager.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/configs/internvl.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/arcee.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/commandr.py`; `python/sglang/srt/models/dbrx.py` 等 54 个文件
  - runtime-perf: `python/sglang/srt/models/afmoe.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/ernie45_moe_vl.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/granitemoe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 15 个文件
  - tests: `python/sglang/test/runners.py`; `test/registered/core/test_score_api.py`; `test/registered/quant/test_awq.py`; `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/vlm/test_vlm_input_format.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `20282f566` - [fix typo] expert_indicies -> expert_indices (#19627)

- Full hash: `20282f5664cbf762860db79e34b034b211e83cc0`
- Date/author: 2026-03-02 / SoluMilken
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/mixtral_quant.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/mixtral_quant.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f0d78f2e2` - [AMD] Fix weight load shape mismatch for amd dsr1 0528 mxfp4 (#19425)

- Full hash: `f0d78f2e201aa7a2f21d291e20cf0154ee868a21`
- Date/author: 2026-02-27 / billishyahao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/deepseek_nextn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_nextn.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/quark/quark.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5172c3784` - [AMD] Use fused GEMM with FP8 cast for FP8 prefill (#19422)

- Full hash: `5172c378456fa9735ba6429a2ca7688d1152d256`
- Date/author: 2026-02-27 / Thomas Wang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `150ed881b` - [4/N] Quantization Refactor: Quark MoE schemes (#18252)

- Full hash: `150ed881be2cf9a9e64b636226b3c6189d341a7d`
- Date/author: 2026-02-18 / Tamir Baydasov
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/quark/quark.py`; `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8d2892330` - chore: fix some typos (#18577)

- Full hash: `8d2892330c05e4a0d0ee3085b25c035bfed07dcf`
- Date/author: 2026-02-11 / cutetocute
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/double_sparsity_backend.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/int8_kernel.py`, `python/sglang/srt/layers/quantization/quark/utils.py`, `python/sglang/srt/managers/io_struct.py`, `test/registered/rl/test_multi_instance_release_memory_occupation.py`, `test/registered/utils/test_bench_typebaseddispatcher.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/io_struct.py`
  - runtime-perf: `python/sglang/srt/layers/attention/double_sparsity_backend.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`; `python/sglang/srt/layers/quantization/int8_kernel.py`; `python/sglang/srt/layers/quantization/quark/utils.py`
  - tests: `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/utils/test_bench_typebaseddispatcher.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0d49b13fd` - Fix circular import in quantization modules (#17372)

- Full hash: `0d49b13fdd7d96712efee7fbaf246c2e3a965304`
- Date/author: 2026-01-21 / Sam Shleifer
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/auto_round.py`, `python/sglang/srt/layers/quantization/petit.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/w4afp8.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/auto_round.py`; `python/sglang/srt/layers/quantization/petit.py`; `python/sglang/srt/layers/quantization/quark/quark.py`; `python/sglang/srt/layers/quantization/w4afp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5af84c8af` - [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm (#7392)

- Full hash: `5af84c8af554fa0e6fb55890b39b97f155275372`
- Date/author: 2026-01-14 / fxmarty-amd
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/quantization.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/int4fp8_utils.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`, `python/sglang/srt/model_loader/utils.py`, `python/sglang/srt/model_loader/weight_utils.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/quantization.md`
  - other: `python/sglang/srt/layers/int4fp8_utils.py`; `python/sglang/srt/layers/linear.py`; `python/sglang/srt/model_loader/utils.py`; `python/sglang/srt/model_loader/weight_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/__init__.py`; `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`
  - tests: `test/srt/run_suite.py`; `test/srt/test_int4fp8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
