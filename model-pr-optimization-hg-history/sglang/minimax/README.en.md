# sglang MiniMax M2 Series Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `docs/basic_usage/minimax_m2.md` | `403195d59`, `5c64a20da` |
| `python/sglang/srt/function_call/minimax_m2.py` | `5c64a20da` |
| `python/sglang/srt/models/minimax_m2.py` | `18944a9d3`, `1b4933d45`, `766d225fc`, `a3196d08b`, `df1d046de`, `d1e95af28`, `c64274c74`, `2d183c4e6`, `079fc8f3c`, `486c7de39`, `d17b9e639` |
| `test/registered/8-gpu-models/test_minimax_m25.py` | `1aa6ab41d` |
| `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py` | `403195d59` |
| `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py` | `403195d59` |
| `test/registered/ascend/llm_models/test_ascend_minimax_m2.py` | `4641e5a3d` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 27
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-23 | `18944a9d3` | 模型支持/运行时入口 | support MiniMax M2.5 PP | `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-24 | `1b4933d45` | 性能/后端优化 | [NPU][ModelSlim] adapt w2 quant layer for Minimax2.5 (#20905) | `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-23 | `4641e5a3d` | 性能/后端优化 | [NPU] enhance accuracy for model minimaxm2 from 16.5% to 95.5% (#17695) | `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/llm_models/test_ascend_minimax_m2.py` |
| 2026-03-22 | `766d225fc` | 性能/后端优化 | Add SGLang CUDA crash API logging inspired by FlashInfer (#20910) | `.claude/skills/debug-cuda-crash/SKILL.md`, `docs/references/environment_variables.md`, `python/sglang/jit_kernel/awq_marlin_repack.py` |
| 2026-03-18 | `a3196d08b` | 缺陷修复 | [MiniMax M2] Fix KV cache scale loading (#20870) | `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-18 | `df1d046de` | 模型支持/运行时入口 | Add packed_modules_mapping for MiniMax-M2 (#19995) | `python/sglang/srt/models/minimax_m2.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-07 | `1aa6ab41d` | 模型支持/运行时入口 | [Nightly] Replace MiniMax-M2 with MiniMax-M2.5 (#20083) | `test/registered/8-gpu-models/test_minimax_m25.py` |
| 2026-03-02 | `c64274c74` | 性能/后端优化 | Piecewise Cuda Graph set default (#16331) | `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-03-02 | `2d183c4e6` | 模型支持/运行时入口 | [Feat] add PP Support for minimax-m2 series (#19577) | `python/sglang/srt/models/minimax_m2.py` |
| 2026-02-27 | `403195d59` | 性能/后端优化 | [AMD] [MiniMax-M2.5 Day 0] Add MiniMax-M2.5 nightly accuracy test (#19443) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `docs/basic_usage/minimax_m2.md` |
| 2026-02-15 | `ad1bdb93d` | 性能/后端优化 | perf: add minimax-2.5 fused_moe tuning config for h20 (#18833) | `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=384,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json` |
| 2026-02-15 | `922fbc21e` | 性能/后端优化 | [Perf] Tune MiniMax M2 fused moe kernel on H100 GPU (#18851) | `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=384,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128, 128].json` |
| 2026-02-05 | `079fc8f3c` | 性能/后端优化 | [piecewise graph]: support MiniMax-M2 (#18217) | `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/minimax_m2.py` |
| 2026-02-01 | `486c7de39` | 性能/后端优化 | Optimizing all_reduce in RMSNormTP in minimax_m2 (#16483) | `python/sglang/srt/models/minimax_m2.py` |
| 2026-01-25 | `2c1e2674c` | 性能/后端优化 | [misc] replace existing tool call code with new crate package (#17720) | `sgl-model-gateway/src/tool_parser/errors.rs`, `sgl-model-gateway/src/tool_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/mod.rs` |
| 2026-01-25 | `912349143` | 调度/缓存/PD | A few updates to the night tests (#17694) | `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-25 | `6af22f8db` | 模型支持/运行时入口 | use published reasoning parser crate (#17709) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/reasoning_parser/README.md` |
| 2026-01-15 | `655d2c7c2` | 缺陷修复 | fix: adding matrix partitioning for h200 and b200 nightly tests (#17091) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-14 | `aa2b4f766` | 缺陷修复 | fix: renaming test file and job names + skip blocking llama4 nightly (#16971) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-04 | `f84487af5` | 性能/后端优化 | [model-gateway] : Rust integration tests for integration_mock replacement (#16441) | `.pre-commit-config.yaml`, `sgl-model-gateway/py_test/unit/__init__.py`, `sgl-model-gateway/tests/common/mock_mcp_server.rs` |
| 2026-01-02 | `d8ac5eecf` | 性能/后端优化 | [model-gateway] bug fix on module name (#16332) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/benches/manual_policy_benchmark.rs`, `sgl-model-gateway/benches/request_processing.rs` |
| 2025-12-31 | `d17b9e639` | 模型支持/运行时入口 | Fusing RMSNormTP in minimax_m2 (#14416) | `python/sglang/srt/models/minimax_m2.py` |
| 2025-12-31 | `f35b5da52` | 性能/后端优化 | [CI] Append test variant name to markdown report header in nightly test (#16166) | `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py` |
| 2025-12-24 | `5c64a20da` | 调度/缓存/PD | Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs (#15538) | `docs/basic_usage/minimax_m2.md`, `docs/basic_usage/popular_model_usage.rst`, `docs/supported_models/generative_models.md` |
| 2025-12-22 | `989d4b301` | 性能/后端优化 | [CI] Migrate nightly tests to test/registered/ (#15582) | `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py` |
| 2025-12-20 | `96740d698` | 性能/后端优化 | feature: revamp nightly tests with combined runner (#15324) | `.github/workflows/nightly-test-nvidia.yml`, `test/nightly/accuracy_test_runner.py`, `test/nightly/nightly_utils.py` |

## Per-Commit Audit Cards

### Commit `18944a9d3` - support MiniMax M2.5 PP

- Full hash: `18944a9d392690db20f30c060b33d18e8bf9062c`
- Date/author: 2026-04-23 / guizhh
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `1b4933d45` - [NPU][ModelSlim] adapt w2 quant layer for Minimax2.5 (#20905)

- Full hash: `1b4933d45d9384feede20e4cf4fc6c5df2c7e04e`
- Date/author: 2026-03-24 / shadowxz109
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4641e5a3d` - [NPU] enhance accuracy for model minimaxm2 from 16.5% to 95.5% (#17695)

- Full hash: `4641e5a3d2bbeaaa1988528fde4f2e4571e2016d`
- Date/author: 2026-03-23 / McZyWu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/llm_models/test_ascend_minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/moe/topk.py`
  - tests: `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/llm_models/test_ascend_minimax_m2.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `766d225fc` - Add SGLang CUDA crash API logging inspired by FlashInfer (#20910)

- Full hash: `766d225fccf01bdd41a35dc95300952b511454de`
- Date/author: 2026-03-22 / Xiaoyu Zhang
- Auto category: 性能/后端优化
- Main files: `.claude/skills/debug-cuda-crash/SKILL.md`, `docs/references/environment_variables.md`, `python/sglang/jit_kernel/awq_marlin_repack.py`, `python/sglang/jit_kernel/debug_utils.py`, `python/sglang/jit_kernel/flash_attention_v4.py`, `python/sglang/jit_kernel/fused_store_index_cache.py`, `python/sglang/jit_kernel/gptq_marlin.py`, `python/sglang/jit_kernel/gptq_marlin_repack.py` 等 34 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - other: `python/sglang/srt/layers/linear.py`; `python/sglang/srt/layers/utils/multi_platform.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/kimi_vl_moonvit.py`; `python/sglang/srt/models/minimax_m2.py`
  - runtime-perf: `.claude/skills/debug-cuda-crash/SKILL.md`; `python/sglang/jit_kernel/awq_marlin_repack.py`; `python/sglang/jit_kernel/debug_utils.py`; `python/sglang/jit_kernel/flash_attention_v4.py`; `python/sglang/jit_kernel/fused_store_index_cache.py`; `python/sglang/jit_kernel/gptq_marlin.py`; `python/sglang/jit_kernel/gptq_marlin_repack.py`; `python/sglang/jit_kernel/hicache.py` 等 27 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a3196d08b` - [MiniMax M2] Fix KV cache scale loading (#20870)

- Full hash: `a3196d08b8f6de3017cb2ea059a7025ee4504c9d`
- Date/author: 2026-03-18 / Chad Voegele
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `df1d046de` - Add packed_modules_mapping for MiniMax-M2 (#19995)

- Full hash: `df1d046de2a1ac47ef4f1c99b37b3e59feff95e1`
- Date/author: 2026-03-18 / Trevor Morris
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `1aa6ab41d` - [Nightly] Replace MiniMax-M2 with MiniMax-M2.5 (#20083)

- Full hash: `1aa6ab41deb56c2889c7739ad91bec37c9941c60`
- Date/author: 2026-03-07 / Alison Shao
- Auto category: 模型支持/运行时入口
- Main files: `test/registered/8-gpu-models/test_minimax_m25.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/8-gpu-models/test_minimax_m25.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `c64274c74` - Piecewise Cuda Graph set default (#16331)

- Full hash: `c64274c746f210497c45bd1600d2046faf7f4b10`
- Date/author: 2026-03-02 / Yuwei An
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/awq.py` 等 34 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/compilation/compile.py`; `python/sglang/srt/compilation/piecewise_context_manager.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/minicpm3.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/flashinfer_backend.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/qwen2_moe.py`
  - tests: `test/manual/nightly/test_vlms_piecewise_cuda_graph.py`; `test/manual/nightly/test_vlms_vit_cuda_graph.py`; `test/manual/piecewise_cudagraph/test_disaggregation_piecewise_cuda_graph.py`; `test/registered/mla/test_mla_deepseek_v3.py`; `test/registered/models/test_generation_models.py`; `test/registered/models/test_kimi_linear_models_pcg.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/piecewise_cuda_graph/test_piecewise_cuda_graph_2_gpu.py` 等 13 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2d183c4e6` - [Feat] add PP Support for minimax-m2 series (#19577)

- Full hash: `2d183c4e6d32b2463feaec7dee9c6646f104555e`
- Date/author: 2026-03-02 / 0xNullPath
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `403195d59` - [AMD] [MiniMax-M2.5 Day 0] Add MiniMax-M2.5 nightly accuracy test (#19443)

- Full hash: `403195d59de0db4fe37d0b730e9cf6c2a9d9749c`
- Date/author: 2026-02-27 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `docs/basic_usage/minimax_m2.md`, `docs/supported_models/text_generation/generative_models.md`, `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - docs-bench: `docs/basic_usage/minimax_m2.md`; `docs/supported_models/text_generation/generative_models.md`
  - tests: `test/registered/amd/accuracy/mi30x/test_minimax_m25_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_minimax_m25_eval_mi35x.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `ad1bdb93d` - perf: add minimax-2.5 fused_moe tuning config for h20 (#18833)

- Full hash: `ad1bdb93df029bb0c6ce145cfca8a0bc62d925d2`
- Date/author: 2026-02-15 / zhangxiaolei123456
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=384,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=384,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `922fbc21e` - [Perf] Tune MiniMax M2 fused moe kernel on H100 GPU (#18851)

- Full hash: `922fbc21e25dd0b609834e98ceb9e07a62b66928`
- Date/author: 2026-02-15 / jackey hua
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=384,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128, 128].json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=384,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128, 128].json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `079fc8f3c` - [piecewise graph]: support MiniMax-M2 (#18217)

- Full hash: `079fc8f3c591a43316d98fae6f108ce03d0eeeb3`
- Date/author: 2026-02-05 / zhangheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_kernel.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `486c7de39` - Optimizing all_reduce in RMSNormTP in minimax_m2 (#16483)

- Full hash: `486c7de39f5c6ec8d651c5c0c662e940fccb63e0`
- Date/author: 2026-02-01 / Roger Young
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `2c1e2674c` - [misc] replace existing tool call code with new crate package (#17720)

- Full hash: `2c1e2674ccca62d9c6dda72dd4a8639bd1f571eb`
- Date/author: 2026-01-25 / Simo Lin
- Auto category: 性能/后端优化
- Main files: `sgl-model-gateway/src/tool_parser/errors.rs`, `sgl-model-gateway/src/tool_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/mod.rs`, `sgl-model-gateway/src/tool_parser/parsers/deepseek.rs`, `sgl-model-gateway/src/tool_parser/parsers/glm4_moe.rs`, `sgl-model-gateway/src/tool_parser/parsers/helpers.rs`, `sgl-model-gateway/src/tool_parser/parsers/json.rs`, `sgl-model-gateway/src/tool_parser/parsers/kimik2.rs` 等 39 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `sgl-model-gateway/src/tool_parser/errors.rs`; `sgl-model-gateway/src/tool_parser/factory.rs`; `sgl-model-gateway/src/tool_parser/mod.rs`; `sgl-model-gateway/src/tool_parser/parsers/deepseek.rs`; `sgl-model-gateway/src/tool_parser/parsers/helpers.rs`; `sgl-model-gateway/src/tool_parser/parsers/json.rs`; `sgl-model-gateway/src/tool_parser/parsers/kimik2.rs`; `sgl-model-gateway/src/tool_parser/parsers/llama.rs` 等 20 个文件
  - runtime-perf: `sgl-model-gateway/src/tool_parser/parsers/glm4_moe.rs`
  - tests: `sgl-model-gateway/tests/tool_parser/mod.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_deepseek.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_edge_cases.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_fallback.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_glm47_moe.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_glm4_moe.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_json.rs`; `sgl-model-gateway/tests/tool_parser/tool_parser_kimik2.rs` 等 18 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `912349143` - A few updates to the night tests (#17694)

- Full hash: `9123491430c9cc38b6796cbf3ad3ef07e948e8c9`
- Date/author: 2026-01-25 / Kangyan-Zhou
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/accuracy_test_runner.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `6af22f8db` - use published reasoning parser crate (#17709)

- Full hash: `6af22f8dbf4852d3aec9df7c20a7b8361c9b2ddf`
- Date/author: 2026-01-25 / Simo Lin
- Auto category: 模型支持/运行时入口
- Main files: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/reasoning_parser/README.md`, `sgl-model-gateway/src/reasoning_parser/factory.rs`, `sgl-model-gateway/src/reasoning_parser/mod.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/base.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/deepseek_r1.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/glm45.rs` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `sgl-model-gateway/Cargo.toml`; `sgl-model-gateway/src/lib.rs`; `sgl-model-gateway/src/reasoning_parser/README.md`; `sgl-model-gateway/src/reasoning_parser/factory.rs`; `sgl-model-gateway/src/reasoning_parser/mod.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/base.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/deepseek_r1.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/glm45.rs` 等 14 个文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `655d2c7c2` - fix: adding matrix partitioning for h200 and b200 nightly tests (#17091)

- Full hash: `655d2c7c2aa42d7b097498a2c0d48cd697aeda61`
- Date/author: 2026-01-15 / Douglas Yang
- Auto category: 缺陷修复
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py`; `test/registered/8-gpu-models/test_minimax_m2.py` 等 10 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `aa2b4f766` - fix: renaming test file and job names + skip blocking llama4 nightly (#16971)

- Full hash: `aa2b4f76617929469acb3a7bbd6052e718d00ab3`
- Date/author: 2026-01-14 / Douglas Yang
- Auto category: 缺陷修复
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_glm_46.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py`, `test/registered/8-gpu-models/test_kimi_k2.py`, `test/registered/8-gpu-models/test_llama4.py`, `test/registered/8-gpu-models/test_minimax_m2.py` 等 10 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_glm_46.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py`; `test/registered/8-gpu-models/test_kimi_k2.py`; `test/registered/8-gpu-models/test_llama4.py`; `test/registered/8-gpu-models/test_minimax_m2.py`; `test/registered/8-gpu-models/test_mistral_large3.py` 等 9 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `f84487af5` - [model-gateway] : Rust integration tests for integration_mock replacement (#16441)

- Full hash: `f84487af591ba514b726a2daf72e438a41f417c0`
- Date/author: 2026-01-04 / Simo Lin
- Auto category: 性能/后端优化
- Main files: `.pre-commit-config.yaml`, `sgl-model-gateway/py_test/unit/__init__.py`, `sgl-model-gateway/tests/common/mock_mcp_server.rs`, `sgl-model-gateway/tests/common/mod.rs`, `sgl-model-gateway/tests/common/test_certs.rs`, `sgl-model-gateway/tests/common/test_config.rs`, `sgl-model-gateway/tests/common/tls_mock_worker.rs`, `sgl-model-gateway/tests/header_forwarding_test.rs` 等 48 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `.pre-commit-config.yaml`
  - tests: `sgl-model-gateway/py_test/unit/__init__.py`; `sgl-model-gateway/tests/common/mock_mcp_server.rs`; `sgl-model-gateway/tests/common/mod.rs`; `sgl-model-gateway/tests/common/test_certs.rs`; `sgl-model-gateway/tests/common/test_config.rs`; `sgl-model-gateway/tests/common/tls_mock_worker.rs`; `sgl-model-gateway/tests/header_forwarding_test.rs`; `sgl-model-gateway/tests/payload_size_test.rs` 等 47 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d8ac5eecf` - [model-gateway] bug fix on module name (#16332)

- Full hash: `d8ac5eecf74e6edb9b5114980a9c71b1467c51ca`
- Date/author: 2026-01-02 / Chang Su
- Auto category: 性能/后端优化
- Main files: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/benches/manual_policy_benchmark.rs`, `sgl-model-gateway/benches/request_processing.rs`, `sgl-model-gateway/benches/router_registry_bench.rs`, `sgl-model-gateway/benches/tokenizer_benchmark.rs`, `sgl-model-gateway/benches/tool_parser_benchmark.rs`, `sgl-model-gateway/benches/tree_benchmark.rs`, `sgl-model-gateway/bindings/golang/src/client.rs` 等 66 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `sgl-model-gateway/tests/workflow_test.rs`
  - other: `sgl-model-gateway/Cargo.toml`; `sgl-model-gateway/benches/manual_policy_benchmark.rs`; `sgl-model-gateway/benches/request_processing.rs`; `sgl-model-gateway/benches/tokenizer_benchmark.rs`; `sgl-model-gateway/benches/tool_parser_benchmark.rs`; `sgl-model-gateway/benches/tree_benchmark.rs`; `sgl-model-gateway/bindings/golang/src/client.rs`; `sgl-model-gateway/bindings/golang/src/grpc_converter.rs` 等 19 个文件
  - runtime-model: `sgl-model-gateway/benches/router_registry_bench.rs`; `sgl-model-gateway/src/routers/grpc/harmony/mod.rs`
  - tests: `sgl-model-gateway/tests/api_endpoints_test.rs`; `sgl-model-gateway/tests/auth_integration_test.rs`; `sgl-model-gateway/tests/cache_aware_backward_compat_test.rs`; `sgl-model-gateway/tests/chat_template_format_detection.rs`; `sgl-model-gateway/tests/chat_template_integration.rs`; `sgl-model-gateway/tests/chat_template_loading.rs`; `sgl-model-gateway/tests/common/mod.rs`; `sgl-model-gateway/tests/common/test_app.rs` 等 44 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d17b9e639` - Fusing RMSNormTP in minimax_m2 (#14416)

- Full hash: `d17b9e639224f013265070de848c09f7e9f4bc71`
- Date/author: 2025-12-31 / Roger Young
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f35b5da52` - [CI] Append test variant name to markdown report header in nightly test (#16166)

- Full hash: `f35b5da521bffa72404f45ad4a9e85727f12456b`
- Date/author: 2025-12-31 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/test_utils.py`, `test/manual/nightly/test_deepseek_v31_perf.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/nightly_bench_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/test_utils.py`; `test/manual/nightly/test_deepseek_v31_perf.py`; `test/manual/nightly/test_deepseek_v32_perf.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `5c64a20da` - Update MiniMax-M2 ToolCall and add MiniMax-M2.1 in Docs (#15538)

- Full hash: `5c64a20da7dd15ca743f453c73b8d6d955a09493`
- Date/author: 2025-12-24 / Roger Young
- Auto category: 调度/缓存/PD
- Main files: `docs/basic_usage/minimax_m2.md`, `docs/basic_usage/popular_model_usage.rst`, `docs/supported_models/generative_models.md`, `python/sglang/srt/function_call/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/basic_usage/minimax_m2.md`; `docs/basic_usage/popular_model_usage.rst`; `docs/supported_models/generative_models.md`
  - other: `python/sglang/srt/function_call/minimax_m2.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `989d4b301` - [CI] Migrate nightly tests to test/registered/ (#15582)

- Full hash: `989d4b301293ea8eb243d7c320c5c457cb718629`
- Date/author: 2025-12-22 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/vlm_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/run_combined_tests.py` 等 64 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/ascend/__init__.py`; `python/sglang/test/ascend/gsm8k_ascend_mixin.py`; `python/sglang/test/ascend/vlm_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/run_combined_tests.py`; `test/registered/8-gpu-models/test_deepseek_v31.py` 等 63 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `96740d698` - feature: revamp nightly tests with combined runner (#15324)

- Full hash: `96740d6983711d85a66b1ca4ebd6b83b3a40106b`
- Date/author: 2025-12-20 / Douglas Yang
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `test/nightly/accuracy_test_runner.py`, `test/nightly/nightly_utils.py`, `test/nightly/performance_test_runner.py`, `test/nightly/run_combined_tests.py`, `test/nightly/test_deepseek_v31_perf.py`, `test/nightly/test_deepseek_v32_gpqa.py`, `test/nightly/test_deepseek_v32_nsabackend.py` 等 23 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/nightly/accuracy_test_runner.py`; `test/nightly/nightly_utils.py`; `test/nightly/performance_test_runner.py`; `test/nightly/run_combined_tests.py`; `test/nightly/test_deepseek_v31_perf.py`; `test/nightly/test_deepseek_v32_gpqa.py`; `test/nightly/test_deepseek_v32_nsabackend.py`; `test/nightly/test_deepseek_v32_perf.py` 等 22 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.
