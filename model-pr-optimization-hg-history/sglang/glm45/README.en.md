# sglang GLM-4.5 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `docs/basic_usage/glm45.md` | `3d72944fb` |
| `python/sglang/srt/function_call/glm4_moe_detector.py` | `8ef5b9052`, `bc8b526ed` |
| `python/sglang/srt/models/glm4_moe.py` | `646573e4e`, `d1e95af28`, `9991debde`, `1b659bcb0`, `398b81f78`, `2c2c4e446`, `fb683be6e`, `2ff0880a0`, `76b06bee0`, `d27f16f38`, `8e43980eb`, `bed301a5a` |
| `python/sglang/srt/models/glm4_moe_lite.py` | `9ac4dcada`, `fb683be6e`, `76b06bee0` |
| `python/sglang/srt/models/glm4_moe_nextn.py` | `fb683be6e` |
| `test/registered/moe/test_glm4_moe_models.py` | `814202704`, `146b5fcc8`, `ff0f370f8` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 26
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-27 | `646573e4e` | 性能/后端优化 | fix: use get_rope_config() to support models without rope_parameters (#21135) | `python/sglang/srt/models/baichuan.py`, `python/sglang/srt/models/deepseek.py`, `python/sglang/srt/models/ernie4.py` |
| 2026-03-23 | `814202704` | 性能/后端优化 | ci: unify PR test suite naming (#21187) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-11 | `9991debde` | 性能/后端优化 | [Feature] Integrate Elastic NIXL-EP into SGLang (#19248) | `docs/advanced_features/expert_parallelism.md`, `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` |
| 2026-03-02 | `da2a0240f` | 模型支持/运行时入口 | Add GLM45 tool interruption support (#17714) | `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/parser/test_reasoning_parser.py` |
| 2026-02-17 | `1b659bcb0` | 性能/后端优化 | Fix GLM-5 fused shared expert (#18804) | `python/sglang/srt/models/glm4_moe.py` |
| 2026-02-10 | `398b81f78` | 性能/后端优化 | Support GlmMoeDsaForCausalLM (#18521) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/server_args.py` |
| 2026-02-01 | `9ac4dcada` | 性能/后端优化 | [Tiny] Fix grammar in shared experts fusion log messages (#18043) | `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe_lite.py` |
| 2026-01-25 | `2c1e2674c` | 性能/后端优化 | [misc] replace existing tool call code with new crate package (#17720) | `sgl-model-gateway/src/tool_parser/errors.rs`, `sgl-model-gateway/src/tool_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/mod.rs` |
| 2026-01-25 | `6af22f8db` | 模型支持/运行时入口 | use published reasoning parser crate (#17709) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/reasoning_parser/README.md` |
| 2026-01-24 | `2c2c4e446` | 性能/后端优化 | [NVIDIA] Add flashinfer all-to-all MOE dispatcher (#14668) | `docs/advanced_features/expert_parallelism.md`, `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-01-24 | `fb683be6e` | 性能/后端优化 | Use attn tp group in embedding for more models (#17570) | `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py` |
| 2026-01-21 | `2ff0880a0` | 性能/后端优化 | [Fix] GLM 4.7 + NVFP4 + MTP (#17166) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-01-20 | `76b06bee0` | 性能/后端优化 | [New Model] GLM4.7-Flash (#17247) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-01-15 | `146b5fcc8` | 性能/后端优化 | [CI] Reorganize stage-b 1-GPU tests for 5090 compatibility (#16826) | `.github/workflows/pr-test.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py` |
| 2026-01-15 | `3d72944fb` | 模型支持/运行时入口 | [Doc] Add tip on how to use Spec V2 (#15455) | `docs/basic_usage/deepseek_v3.md`, `docs/basic_usage/glm45.md`, `docs/basic_usage/gpt_oss.md` |
| 2026-01-14 | `4346db5fa` | 性能/后端优化 | [Fix] Remove assertion for padding for NVFP4 weight scales to fix GLM 4.5 NVFP4 (#12497) | `python/sglang/srt/layers/quantization/modelopt_quant.py` |
| 2026-01-10 | `d27f16f38` | 性能/后端优化 | Fix EPLB + FP4 Quantization Compatibility Issue (#13715) | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-10 | `8ef5b9052` | 性能/后端优化 | Fix GLM-4.7 MoE Detector complex JSON Schema type parsing (#15753) | `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/utils.py` |
| 2026-01-04 | `f84487af5` | 性能/后端优化 | [model-gateway] : Rust integration tests for integration_mock replacement (#16441) | `.pre-commit-config.yaml`, `sgl-model-gateway/py_test/unit/__init__.py`, `sgl-model-gateway/tests/common/mock_mcp_server.rs` |
| 2026-01-04 | `ff0f370f8` | 性能/后端优化 | ci: migrate MoE tests to test/registered/moe/ (#16127) | `test/registered/moe/test_cutedsl_moe.py`, `test/registered/moe/test_fused_moe.py`, `test/registered/moe/test_glm4_moe_models.py` |
| 2026-01-02 | `d8ac5eecf` | 性能/后端优化 | [model-gateway] bug fix on module name (#16332) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/benches/manual_policy_benchmark.rs`, `sgl-model-gateway/benches/request_processing.rs` |
| 2025-12-31 | `bc8b526ed` | 性能/后端优化 | Fix: Handle empty func_name and None values in GLM MoE detectors (#15754) | `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `test/registered/function_call/test_function_call_parser.py` |
| 2025-12-28 | `8e43980eb` | 性能/后端优化 | [Feature] JIT Fused QK norm + qk norm clean up (#15835) | `python/sglang/jit_kernel/benchmark/bench_qknorm.py`, `python/sglang/jit_kernel/csrc/norm.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` |
| 2025-12-21 | `bed301a5a` | 性能/后端优化 | [Feature] Enable return routed experts (#12162) | `python/sglang/bench_serving.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/routed_experts_capturer.py` |
| 2025-12-21 | `26704c23c` | 性能/后端优化 | [model-gateway]: Tool parser for glm47 (#15520) | `sgl-model-gateway/README.md`, `sgl-model-gateway/benches/tool_parser_benchmark.rs`, `sgl-model-gateway/src/reasoning_parser/README.md` |

## Per-Commit Audit Cards

### Commit `646573e4e` - fix: use get_rope_config() to support models without rope_parameters (#21135)

- Full hash: `646573e4e8d10c2684e0563bc40915b4bef874f4`
- Date/author: 2026-03-27 / shuwenn
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/baichuan.py`, `python/sglang/srt/models/deepseek.py`, `python/sglang/srt/models/ernie4.py`, `python/sglang/srt/models/exaone.py`, `python/sglang/srt/models/glm4.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/grok.py`, `python/sglang/srt/models/hunyuan.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/deepseek.py`; `python/sglang/srt/models/ernie4.py`; `python/sglang/srt/models/exaone.py`; `python/sglang/srt/models/glm4.py`; `python/sglang/srt/models/grok.py`; `python/sglang/srt/models/hunyuan.py`; `python/sglang/srt/models/iquest_loopcoder.py` 等 16 个文件
  - runtime-perf: `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/xverse_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `814202704` - ci: unify PR test suite naming (#21187)

- Full hash: `814202704bf21525b5ae07029cb475da4c87f3b7`
- Date/author: 2026-03-23 / Lianmin Zheng
- Auto category: 性能/后端优化
- Main files: `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`, `scripts/ci/utils/slash_command_handler.py`, `test/README.md` 等 283 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/actions/wait-for-jobs/action.yml`; `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`; `test/README.md`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/attention/test_chunk_gated_delta_rule.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py` 等 278 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `9991debde` - [Feature] Integrate Elastic NIXL-EP into SGLang (#19248)

- Full hash: `9991debde37b0ea1ecca8e13f0aef24c6b498d17`
- Date/author: 2026-03-11 / Yoray Zack
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/expert_parallelism.md`, `docs/advanced_features/server_arguments.md`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/distributed/utils.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/eplb_algorithms/__init__.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/expert_parallelism.md`; `docs/advanced_features/server_arguments.md`
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/eplb_algorithms/__init__.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/distributed/utils.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/nixl.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/fp8.py` 等 9 个文件
  - tests: `test/manual/ep/test_nixl_ep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `da2a0240f` - Add GLM45 tool interruption support (#17714)

- Full hash: `da2a0240f7784fa8e4c7e978e4357a5908a4ee64`
- Date/author: 2026-03-02 / Leoyzen
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/parser/test_reasoning_parser.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/parser/reasoning_parser.py`
  - tests: `test/registered/parser/test_reasoning_parser.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `1b659bcb0` - Fix GLM-5 fused shared expert (#18804)

- Full hash: `1b659bcb088fd303ee472c0720eeb1a3797cffa1`
- Date/author: 2026-02-17 / Frank Minors
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/glm4_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/glm4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `398b81f78` - Support GlmMoeDsaForCausalLM (#18521)

- Full hash: `398b81f78c939469f60f3f54f6526df95f4cab31`
- Date/author: 2026-02-10 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/models/glm4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9ac4dcada` - [Tiny] Fix grammar in shared experts fusion log messages (#18043)

- Full hash: `9ac4dcada4bd77a18e6f3d3efcd1906f705b235d`
- Date/author: 2026-02-01 / Mohammad Miadh Angkad
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe_lite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/models/glm4_moe_lite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `6af22f8db` - use published reasoning parser crate (#17709)

- Full hash: `6af22f8dbf4852d3aec9df7c20a7b8361c9b2ddf`
- Date/author: 2026-01-25 / Simo Lin
- Auto category: 模型支持/运行时入口
- Main files: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/reasoning_parser/README.md`, `sgl-model-gateway/src/reasoning_parser/factory.rs`, `sgl-model-gateway/src/reasoning_parser/mod.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/base.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/deepseek_r1.rs`, `sgl-model-gateway/src/reasoning_parser/parsers/glm45.rs` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `sgl-model-gateway/Cargo.toml`; `sgl-model-gateway/src/lib.rs`; `sgl-model-gateway/src/reasoning_parser/README.md`; `sgl-model-gateway/src/reasoning_parser/factory.rs`; `sgl-model-gateway/src/reasoning_parser/mod.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/base.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/deepseek_r1.rs`; `sgl-model-gateway/src/reasoning_parser/parsers/glm45.rs` 等 14 个文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `2c2c4e446` - [NVIDIA] Add flashinfer all-to-all MOE dispatcher (#14668)

- Full hash: `2c2c4e446b99c529896b3377b24e1b48b6a52e61`
- Date/author: 2026-01-24 / Trevor Morris
- Auto category: 性能/后端优化
- Main files: `docs/advanced_features/expert_parallelism.md`, `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`, `python/sglang/srt/layers/moe/token_dispatcher/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/layers/moe/token_dispatcher/flashinfer_utils.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/advanced_features/expert_parallelism.md`; `docs/references/environment_variables.md`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/__init__.py`; `python/sglang/srt/layers/moe/token_dispatcher/base.py`; `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`; `python/sglang/srt/layers/moe/token_dispatcher/flashinfer_utils.py`; `python/sglang/srt/layers/moe/token_dispatcher/standard.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/modelopt_quant.py` 等 9 个文件
  - tests: `python/sglang/test/test_flashinfer_dispatcher.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fb683be6e` - Use attn tp group in embedding for more models (#17570)

- Full hash: `fb683be6eb7c6960f3d37ea91ca836c1b8e4120c`
- Date/author: 2026-01-24 / Ke Bao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py`, `python/sglang/srt/models/glm4.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/models/gpt_oss.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/falcon_h1.py`; `python/sglang/srt/models/glm4.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/llada2.py`; `python/sglang/srt/models/llama4.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/bailing_moe_nextn.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/glm4_moe_lite.py`; `python/sglang/srt/models/glm4_moe_nextn.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 10 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2ff0880a0` - [Fix] GLM 4.7 + NVFP4 + MTP (#17166)

- Full hash: `2ff0880a0ed1b81f0dc34e45fbccaa244cf80cf8`
- Date/author: 2026-01-21 / b8zhong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/common.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/model_loader/loader.py`; `python/sglang/srt/model_loader/weight_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/models/glm4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `76b06bee0` - [New Model] GLM4.7-Flash (#17247)

- Full hash: `76b06bee03e8d5e5fbd57dfbdbc80688705988ac`
- Date/author: 2026-01-20 / Qiaolin Yu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/glm4_moe_lite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `146b5fcc8` - [CI] Reorganize stage-b 1-GPU tests for 5090 compatibility (#16826)

- Full hash: `146b5fcc84101123baf743eb9480ad7ce60a0e92`
- Date/author: 2026-01-15 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_mamba_unittest.py`, `test/registered/attention/test_radix_attention.py`, `test/registered/attention/test_radix_cache_unit.py`, `test/registered/attention/test_swa_unittest.py`, `test/registered/attention/test_torch_native_attention_backend.py` 等 136 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/slash_command_handler.py`
  - tests: `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_mamba_unittest.py`; `test/registered/attention/test_radix_attention.py`; `test/registered/attention/test_radix_cache_unit.py`; `test/registered/attention/test_swa_unittest.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py`; `test/registered/attention/test_triton_attention_kernels.py` 等 134 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `3d72944fb` - [Doc] Add tip on how to use Spec V2 (#15455)

- Full hash: `3d72944fb89842672cf9d663228663e05096d8c6`
- Date/author: 2026-01-15 / b8zhong
- Auto category: 模型支持/运行时入口
- Main files: `docs/basic_usage/deepseek_v3.md`, `docs/basic_usage/glm45.md`, `docs/basic_usage/gpt_oss.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/basic_usage/deepseek_v3.md`; `docs/basic_usage/glm45.md`; `docs/basic_usage/gpt_oss.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `4346db5fa` - [Fix] Remove assertion for padding for NVFP4 weight scales to fix GLM 4.5 NVFP4 (#12497)

- Full hash: `4346db5fafee11513799ebb57ec3e6ad5d95f6e9`
- Date/author: 2026-01-14 / b8zhong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/modelopt_quant.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/modelopt_quant.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d27f16f38` - Fix EPLB + FP4 Quantization Compatibility Issue (#13715)

- Full hash: `d27f16f38a6f23e5a7c529c6f052ac11f28c4a97`
- Date/author: 2026-01-10 / Shifang Xu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/longcat_flash.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/gpt_oss.py`
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8ef5b9052` - Fix GLM-4.7 MoE Detector complex JSON Schema type parsing (#15753)

- Full hash: `8ef5b9052825c2624e3ac91852b16998f6f6ee3c`
- Date/author: 2026-01-10 / Leoyzen
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/utils.py`, `test/registered/function_call/test_glm47_moe_detector.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/function_call/utils.py`
  - runtime-perf: `python/sglang/srt/function_call/glm47_moe_detector.py`; `python/sglang/srt/function_call/glm4_moe_detector.py`
  - tests: `test/registered/function_call/test_glm47_moe_detector.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `ff0f370f8` - ci: migrate MoE tests to test/registered/moe/ (#16127)

- Full hash: `ff0f370f85319ca57f6a1572da0c1dfe22761cb3`
- Date/author: 2026-01-04 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `test/registered/moe/test_cutedsl_moe.py`, `test/registered/moe/test_fused_moe.py`, `test/registered/moe/test_glm4_moe_models.py`, `test/registered/moe/test_moe_ep.py`, `test/registered/moe/test_torch_compile_moe.py`, `test/registered/moe/test_triton_fused_moe.py`, `test/registered/moe/test_triton_moe_channel_fp8_kernel.py`, `test/srt/run_suite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/moe/test_cutedsl_moe.py`; `test/registered/moe/test_fused_moe.py`; `test/registered/moe/test_glm4_moe_models.py`; `test/registered/moe/test_moe_ep.py`; `test/registered/moe/test_torch_compile_moe.py`; `test/registered/moe/test_triton_fused_moe.py`; `test/registered/moe/test_triton_moe_channel_fp8_kernel.py`; `test/srt/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `bc8b526ed` - Fix: Handle empty func_name and None values in GLM MoE detectors (#15754)

- Full hash: `bc8b526edad7cb0b53658a6d230d4f4f5a1d1949`
- Date/author: 2025-12-31 / Leoyzen
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `test/registered/function_call/test_function_call_parser.py`, `test/registered/function_call/test_glm47_moe_detector.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/function_call/glm47_moe_detector.py`; `python/sglang/srt/function_call/glm4_moe_detector.py`
  - tests: `test/registered/function_call/test_function_call_parser.py`; `test/registered/function_call/test_glm47_moe_detector.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8e43980eb` - [Feature] JIT Fused QK norm + qk norm clean up (#15835)

- Full hash: `8e43980ebbc324cf2c32a8d248fe0f54f95c339d`
- Date/author: 2025-12-28 / DarkSharpness
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/benchmark/bench_qknorm.py`, `python/sglang/jit_kernel/csrc/norm.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`, `python/sglang/jit_kernel/norm.py`, `python/sglang/jit_kernel/tests/test_qknorm.py` 等 15 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/llada2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/utils.py`
  - runtime-perf: `python/sglang/jit_kernel/benchmark/bench_qknorm.py`; `python/sglang/jit_kernel/csrc/norm.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`; `python/sglang/jit_kernel/norm.py`; `python/sglang/jit_kernel/utils.py` 等 11 个文件
  - tests: `python/sglang/jit_kernel/tests/test_qknorm.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bed301a5a` - [Feature] Enable return routed experts (#12162)

- Full hash: `bed301a5acaa9577c9aa706468bdf242f6a43051`
- Date/author: 2025-12-21 / Junrong Lin
- Auto category: 性能/后端优化
- Main files: `python/sglang/bench_serving.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/routed_experts_capturer.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/schedule_batch.py` 等 27 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/bench_serving.py`; `python/sglang/srt/managers/detokenizer_manager.py`; `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/managers/multi_tokenizer_mixin.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-model: `python/sglang/srt/entrypoints/engine.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/ernie4.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/grok.py`; `python/sglang/srt/models/hunyuan.py` 等 10 个文件
  - runtime-perf: `python/sglang/srt/layers/moe/routed_experts_capturer.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_output_processor_mixin.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`
  - tests: `python/sglang/test/test_utils.py`; `test/srt/rl/test_return_routed_experts.py`; `test/srt/run_suite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `26704c23c` - [model-gateway]: Tool parser for glm47 (#15520)

- Full hash: `26704c23c056e426c6bc86ea1289e82b5fd37e59`
- Date/author: 2025-12-21 / Haoran Wang
- Auto category: 性能/后端优化
- Main files: `sgl-model-gateway/README.md`, `sgl-model-gateway/benches/tool_parser_benchmark.rs`, `sgl-model-gateway/src/reasoning_parser/README.md`, `sgl-model-gateway/src/reasoning_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/parsers/glm4_moe.rs`, `sgl-model-gateway/tests/tool_parser_glm47_moe.rs`, `sgl-model-gateway/tests/tool_parser_glm4_moe.rs`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `sgl-model-gateway/README.md`; `sgl-model-gateway/benches/tool_parser_benchmark.rs`; `sgl-model-gateway/src/reasoning_parser/README.md`; `sgl-model-gateway/src/reasoning_parser/factory.rs`; `sgl-model-gateway/src/tool_parser/factory.rs`
  - runtime-perf: `sgl-model-gateway/src/tool_parser/parsers/glm4_moe.rs`
  - tests: `sgl-model-gateway/tests/tool_parser_glm47_moe.rs`; `sgl-model-gateway/tests/tool_parser_glm4_moe.rs`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
