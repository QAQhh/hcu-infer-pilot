# sglang Mistral Small 4 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/function_call/mistral_detector.py` | `6b8a6545b` |
| `python/sglang/srt/models/ministral3.py` | `d1e95af28` |
| `python/sglang/srt/models/mistral.py` | no direct commit |
| `python/sglang/srt/models/mistral_large_3.py` | no direct commit |
| `python/sglang/srt/models/mistral_large_3_eagle.py` | `6b8a6545b` |
| `python/sglang/srt/utils/mistral_utils.py` | `6b8a6545b` |
| `test/manual/models/test_mistral_large3_basic.py` | `56907cbcb` |
| `test/registered/8-gpu-models/test_mistral_large3.py` | `e14fd4acc`, `350190487`, `ae9586929`, `99fab2ce6`, `912349143`, `655d2c7c2`, `aa2b4f766`, `f35b5da52`, `989d4b301`, `96740d698` |
| `test/registered/ascend/llm_models/test_npu_mistral_7b.py` | `895e56097` |
| `test/registered/ascend/vlm_models/test_npu_mistral_small_3_1_24b_instruct_2503.py` | `895e56097` |
| `test/registered/models/test_ministral3_models.py` | `fb90c9d29`, `814202704`, `a0bae4c34` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 25
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-26 | `fb90c9d29` | 性能/后端优化 | [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047) | `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py` |
| 2026-03-23 | `814202704` | 性能/后端优化 | ci: unify PR test suite naming (#21187) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-18 | `6b8a6545b` | 性能/后端优化 | Add Mistral Small 4 (Pixtral) support (#20708) | `benchmark/mmmu/bench_sglang.py`, `benchmark/mmmu/eval_utils.py`, `python/sglang/srt/configs/deepseek_ocr.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-02-25 | `e14fd4acc` | 缺陷修复 | Fix nightly Mistral-Large-3 NVFP4 accuracy threshold (#19402) | `test/registered/8-gpu-models/test_mistral_large3.py` |
| 2026-02-26 | `350190487` | 性能/后端优化 | Flashinfer MOE FP8 support for Mistral Large 3. (#15422) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/utils.py`, `test/registered/8-gpu-models/test_mistral_large3.py` |
| 2026-02-16 | `7e41ac6c8` | 测试/文档/基准 | Skip flaky test_tool_choice_required_non_streaming for Mistral (#18889) | `test/registered/openai_server/function_call/test_tool_choice.py` |
| 2026-02-14 | `ae9586929` | 性能/后端优化 | Enable SGLANG_ENABLE_SPEC_V2 for nightly speculative decoding tests (#18719) | `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py` |
| 2026-02-03 | `99fab2ce6` | 性能/后端优化 | [Bugfix] Fix Mistral Large 3 NVFP4 TRTLLM MoE (#18065) | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `test/registered/8-gpu-models/test_mistral_large3.py` |
| 2026-02-03 | `c781db0f6` | 调度/缓存/PD | [NPU] update nightly tests (#17952) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-02-01 | `56907cbcb` | 模型支持/运行时入口 | Move deleted 8-GPU tests to test/manual/ (#18060) | `test/manual/models/test_kimi_k2_models.py`, `test/manual/models/test_mistral_large3_basic.py` |
| 2026-01-31 | `a0bae4c34` | 性能/后端优化 | Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299) | `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py` |
| 2026-01-25 | `2c1e2674c` | 性能/后端优化 | [misc] replace existing tool call code with new crate package (#17720) | `sgl-model-gateway/src/tool_parser/errors.rs`, `sgl-model-gateway/src/tool_parser/factory.rs`, `sgl-model-gateway/src/tool_parser/mod.rs` |
| 2026-01-25 | `912349143` | 调度/缓存/PD | A few updates to the night tests (#17694) | `python/sglang/test/accuracy_test_runner.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-15 | `655d2c7c2` | 缺陷修复 | fix: adding matrix partitioning for h200 and b200 nightly tests (#17091) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-14 | `aa2b4f766` | 缺陷修复 | fix: renaming test file and job names + skip blocking llama4 nightly (#16971) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` |
| 2026-01-04 | `f84487af5` | 性能/后端优化 | [model-gateway] : Rust integration tests for integration_mock replacement (#16441) | `.pre-commit-config.yaml`, `sgl-model-gateway/py_test/unit/__init__.py`, `sgl-model-gateway/tests/common/mock_mcp_server.rs` |
| 2026-01-02 | `d8ac5eecf` | 性能/后端优化 | [model-gateway] bug fix on module name (#16332) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/benches/manual_policy_benchmark.rs`, `sgl-model-gateway/benches/request_processing.rs` |
| 2025-12-31 | `f35b5da52` | 性能/后端优化 | [CI] Append test variant name to markdown report header in nightly test (#16166) | `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py` |
| 2025-12-28 | `5969be2f0` | 缺陷修复 | Apply fixture-kit mode to MMMUVLMMixin (#15615) | `python/sglang/srt/environ.py`, `python/sglang/test/kits/mmmu_vlm_kit.py`, `python/sglang/test/server_fixtures/mmmu_fixture.py` |
| 2025-12-24 | `bd572360f` | 模型支持/运行时入口 | Tiny apply gsm8k mixin to ngram test (#15606) | `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/spec/test_ngram_speculative_decoding.py`, `test/srt/models/test_ministral3_models.py` |
| 2025-12-22 | `989d4b301` | 性能/后端优化 | [CI] Migrate nightly tests to test/registered/ (#15582) | `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py` |
| 2025-12-22 | `beae3f961` | 缺陷修复 | Adapt fixture-kit to gsm8k mixin (#15599) | `python/sglang/test/gsm8k_mixin.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `python/sglang/test/kits/mmmu_vlm_kit.py` |
| 2025-12-20 | `96740d698` | 性能/后端优化 | feature: revamp nightly tests with combined runner (#15324) | `.github/workflows/nightly-test-nvidia.yml`, `test/nightly/accuracy_test_runner.py`, `test/nightly/nightly_utils.py` |

## Per-Commit Audit Cards

### Commit `fb90c9d29` - [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047)

- Full hash: `fb90c9d298eeeb15fde5de1c7676cfc3d9a4b6ee`
- Date/author: 2026-03-26 / Liangsheng Yin
- Auto category: 性能/后端优化
- Main files: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/test/kits/eval_accuracy_kit.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_mimo_models.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `6b8a6545b` - Add Mistral Small 4 (Pixtral) support (#20708)

- Full hash: `6b8a6545b231e175a9534ee50ed57fcd6d5b75e5`
- Date/author: 2026-03-18 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `benchmark/mmmu/bench_sglang.py`, `benchmark/mmmu/eval_utils.py`, `python/sglang/srt/configs/deepseek_ocr.py`, `python/sglang/srt/configs/deepseekvl2.py`, `python/sglang/srt/configs/janus_pro.py`, `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/mmmu/bench_sglang.py`; `benchmark/mmmu/eval_utils.py`
  - other: `python/sglang/srt/function_call/mistral_detector.py`; `python/sglang/srt/multimodal/processors/pixtral.py`; `python/sglang/srt/parser/reasoning_parser.py`; `python/sglang/srt/utils/hf_transformers_utils.py`; `python/sglang/srt/utils/mistral_utils.py`
  - runtime-model: `python/sglang/srt/configs/deepseek_ocr.py`; `python/sglang/srt/configs/deepseekvl2.py`; `python/sglang/srt/configs/janus_pro.py`; `python/sglang/srt/configs/jet_nemotron.py`; `python/sglang/srt/entrypoints/openai/protocol.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/mistral_large_3_eagle.py` 等 10 个文件
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
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

### Commit `895e56097` - Add NPU basic function testcases (#19382)

- Full hash: `895e56097cc25f762373f462fd027bc39163eb0c`
- Date/author: 2026-03-16 / Sugar920
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`, `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py` 等 87 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/disaggregation_utils.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`; `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py`; `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py` 等 86 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `e14fd4acc` - Fix nightly Mistral-Large-3 NVFP4 accuracy threshold (#19402)

- Full hash: `e14fd4accb43cc551dc7cb08a69ef2c2e74c4922`
- Date/author: 2026-02-25 / Alison Shao
- Auto category: 缺陷修复
- Main files: `test/registered/8-gpu-models/test_mistral_large3.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/8-gpu-models/test_mistral_large3.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `350190487` - Flashinfer MOE FP8 support for Mistral Large 3. (#15422)

- Full hash: `350190487be4a4b0a173c05e51136c57ee137a28`
- Date/author: 2026-02-26 / Daniel Cámpora
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/utils.py`, `test/registered/8-gpu-models/test_mistral_large3.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/utils.py`
  - tests: `test/registered/8-gpu-models/test_mistral_large3.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7e41ac6c8` - Skip flaky test_tool_choice_required_non_streaming for Mistral (#18889)

- Full hash: `7e41ac6c8db6496820f8c9f404db67f1973fd121`
- Date/author: 2026-02-16 / Alison Shao
- Auto category: 测试/文档/基准
- Main files: `test/registered/openai_server/function_call/test_tool_choice.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/registered/openai_server/function_call/test_tool_choice.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `ae9586929` - Enable SGLANG_ENABLE_SPEC_V2 for nightly speculative decoding tests (#18719)

- Full hash: `ae958692927509723ada6e33f368bdba148f1654`
- Date/author: 2026-02-14 / Kangyan-Zhou
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/test_utils.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`, `test/registered/8-gpu-models/test_glm_46_fp8.py` 等 10 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/test_utils.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py`; `test/registered/8-gpu-models/test_deepseek_v32_cp_single_node.py`; `test/registered/8-gpu-models/test_glm_46_fp8.py` 等 10 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `99fab2ce6` - [Bugfix] Fix Mistral Large 3 NVFP4 TRTLLM MoE (#18065)

- Full hash: `99fab2ce673eeae87736cee44844777a3c9ae304`
- Date/author: 2026-02-03 / elvischenv
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`, `test/registered/8-gpu-models/test_mistral_large3.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
  - tests: `test/registered/8-gpu-models/test_mistral_large3.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c781db0f6` - [NPU] update nightly tests (#17952)

- Full hash: `c781db0f6c236e357a0652a962fdf7d3f528d752`
- Date/author: 2026-02-03 / Sugar920
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `python/sglang/test/ascend/vlm_utils.py`, `test/registered/ascend/basic_function/interface/test_ascend_enable_thinking.py`, `test/registered/ascend/basic_function/parameter/test_ascend_log_level.py`, `test/registered/ascend/basic_function/parameter/test_ascend_no_chunked_prefill.py`, `test/registered/ascend/basic_function/parameter/test_ascend_no_overlap_scheduler.py` 等 52 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/gsm8k_ascend_mixin.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `python/sglang/test/ascend/vlm_utils.py`; `test/registered/ascend/basic_function/interface/test_ascend_enable_thinking.py`; `test/registered/ascend/basic_function/parameter/test_ascend_log_level.py`; `test/registered/ascend/basic_function/parameter/test_ascend_no_chunked_prefill.py`; `test/registered/ascend/basic_function/parameter/test_ascend_no_overlap_scheduler.py`; `test/registered/ascend/basic_function/parameter/test_ascend_original_logprobs.py` 等 51 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `56907cbcb` - Move deleted 8-GPU tests to test/manual/ (#18060)

- Full hash: `56907cbcb190affa4dfa3473cbe7534622f2f8b1`
- Date/author: 2026-02-01 / Alison Shao
- Auto category: 模型支持/运行时入口
- Main files: `test/manual/models/test_kimi_k2_models.py`, `test/manual/models/test_mistral_large3_basic.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/manual/models/test_kimi_k2_models.py`; `test/manual/models/test_mistral_large3_basic.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `a0bae4c34` - Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299)

- Full hash: `a0bae4c34349d09b3ad71db71d4fc3f4f32f221e`
- Date/author: 2026-01-31 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py` 等 39 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v32_basic.py`; `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v3_basic.py`; `test/registered/8-gpu-models/test_deepseek_v3_mtp.py` 等 37 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `f35b5da52` - [CI] Append test variant name to markdown report header in nightly test (#16166)

- Full hash: `f35b5da521bffa72404f45ad4a9e85727f12456b`
- Date/author: 2025-12-31 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/test_utils.py`, `test/manual/nightly/test_deepseek_v31_perf.py`, `test/manual/nightly/test_deepseek_v32_perf.py`, `test/registered/8-gpu-models/test_deepseek_v31.py`, `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/nightly_bench_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/test_utils.py`; `test/manual/nightly/test_deepseek_v31_perf.py`; `test/manual/nightly/test_deepseek_v32_perf.py`; `test/registered/8-gpu-models/test_deepseek_v31.py`; `test/registered/8-gpu-models/test_deepseek_v32.py` 等 14 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `5969be2f0` - Apply fixture-kit mode to MMMUVLMMixin (#15615)

- Full hash: `5969be2f06c9642c6c8583d48cbd4f363a594824`
- Date/author: 2025-12-28 / lif
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/environ.py`, `python/sglang/test/kits/mmmu_vlm_kit.py`, `python/sglang/test/server_fixtures/mmmu_fixture.py`, `test/srt/models/test_ministral3_models.py`, `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`, `test/srt/models/test_vlm_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`
  - tests: `python/sglang/test/kits/mmmu_vlm_kit.py`; `python/sglang/test/server_fixtures/mmmu_fixture.py`; `test/srt/models/test_ministral3_models.py`; `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/srt/models/test_vlm_models.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `bd572360f` - Tiny apply gsm8k mixin to ngram test (#15606)

- Full hash: `bd572360f315095e69fbdce52b3029e26b8de3b2`
- Date/author: 2025-12-24 / Liangsheng Yin
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/spec/test_ngram_speculative_decoding.py`, `test/srt/models/test_ministral3_models.py`, `test/srt/models/test_nvidia_nemotron_nano_v2.py`, `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`, `test/srt/run_suite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/spec/test_ngram_speculative_decoding.py`; `test/srt/models/test_ministral3_models.py`; `test/srt/models/test_nvidia_nemotron_nano_v2.py`; `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/srt/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

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

### Commit `beae3f961` - Adapt fixture-kit to gsm8k mixin (#15599)

- Full hash: `beae3f961cd517a03ca92ccbca1a030d4f549026`
- Date/author: 2025-12-22 / Liangsheng Yin
- Auto category: 缺陷修复
- Main files: `python/sglang/test/gsm8k_mixin.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `python/sglang/test/kits/mmmu_vlm_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `test/srt/models/test_ministral3_models.py`, `test/srt/models/test_nvidia_nemotron_nano_v2.py`, `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`, `test/srt/models/test_vlm_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/gsm8k_mixin.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `python/sglang/test/kits/mmmu_vlm_kit.py`; `python/sglang/test/server_fixtures/default_fixture.py`; `test/srt/models/test_ministral3_models.py`; `test/srt/models/test_nvidia_nemotron_nano_v2.py`; `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/srt/models/test_vlm_models.py`
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
