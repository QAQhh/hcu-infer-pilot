# sglang MOSS-VL Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/arg_groups/model_overrides/moss_vl.py` | `ab43824b09`, `50bacb0280` |
| `python/sglang/srt/models/moss_vl.py` | `36b93840b5`, `ab43824b09`, `ee0f2375e5` |
| `python/sglang/srt/multimodal/processors/moss_vl.py` | `ee0f2375e5`, `50bacb0280`, `2d561a3ec2`, `dbe95efd88` |
| `test/registered/unit/models/test_moss_vl_processor.py` | `ee0f2375e5`, `50bacb0280` |

## Local Commit Coverage Summary

- Source worktree: `HYGON-AI/sglang-das`
- Generated date: 2026-11-05
- Commits in this document: 6
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-10-12 | `36b93840b5` | 性能/后端优化 | Sync/official main daily 20261009 (#500) | `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md` |
| 2026-09-29 | `ab43824b09` | 性能/后端优化 | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` |
| 2026-09-08 | `ee0f2375e5` | 性能/后端优化 | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` |
| 2026-09-01 | `50bacb0280` | 性能/后端优化 | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` |
| 2026-07-05 | `2d561a3ec2` | 性能/后端优化 | chore: add modification notices for DCU changes | `NOTICE`, `THIRD_PARTY_NOTICES.md`, `python/sglang/jit_kernel/deepseek_v4.py` |
| 2026-07-01 | `dbe95efd88` | 缺陷修复 | 修复IPC报错的问题 | `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/moss_vl.py`, `python/sglang/srt/multimodal/processors/transformers_auto.py` |

## Per-Commit Audit Cards

### Commit `36b93840b5` - Sync/official main daily 20261009 (#500)

- Full hash: `36b93840b54b8c41fe395e6f3e3f9a5463fe17ba`
- Date/author: 2026-10-12 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`, `.agents/skills/ci-test-audit/SKILL.md`, `.agents/skills/ci-test-audit/action-items.md`, `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/clean-startup-log/SKILL.md` 等 2736 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/check-maintenance/action.yml`; `.github/labeler.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 38 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/kernels/bench_block_verification.py`; `benchmark/kernels/fused_moe_triton/benchmark_sglang_fused_moe_triton.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/.mintignore`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-Math-V2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-OCR-2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-OCR.mdx` 等 154 个文件
  - other: `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`; `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`; `.agents/skills/ci-test-audit/SKILL.md`; `.agents/skills/ci-test-audit/action-items.md`; `.agents/skills/clean-startup-log/SKILL.md`; `.agents/skills/clean-startup-log/references/noise-sources.md`; `.agents/skills/compute-mamba-ratio/SKILL.md`; `.agents/skills/cookbook-add-model/SKILL.md` 等 475 个文件
  - runtime-model: `.agents/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.agents/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml` 等 351 个文件
  - runtime-perf: `.agents/skills/add-jit-kernel/SKILL.md`; `.agents/skills/add-sgl-kernel/SKILL.md`; `.agents/skills/debug-cuda-crash/SKILL.md`; `.agents/skills/debug-distributed-hang/SKILL.md`; `.agents/skills/kernel-organization/SKILL.md`; `.agents/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `.claude/rules/kernel-benchmark.md`; `.claude/skills/add-jit-kernel/SKILL.md` 等 705 个文件
  - tests: `.agents/skills/kl-consistency-test/SKILL.md`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/conftest.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/generator_testlib.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extract_functions.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extracts.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_imports.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_main_single_commit.py` 等 1013 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ab43824b09` - Sync/official main daily 20260928 (#452)

- Full hash: `ab43824b09055fc790bd5a9166a6a6182b1bccc3`
- Date/author: 2026-09-29 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/clean-startup-log/SKILL.md`, `.claude/skills/clean-startup-log/references/noise-sources.md`, `.claude/skills/cookbook-add-model/SKILL.md` 等 2576 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/MAINTAINER.md`; `.github/actions/check-pr-test-health/action.test.cjs`; `.github/actions/check-pr-test-health/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml` 等 38 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/disaggregation/bench_cached_prefix.py`; `benchmark/dllm/README.md`; `benchmark/gsm8k/README.md`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/io/bench_mm_token_padding.py`; `benchmark/kernels/all_gather/benchmark_mscclpp.py` 等 167 个文件
  - other: `.claude/rules/cookbook-first.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/clean-startup-log/SKILL.md`; `.claude/skills/clean-startup-log/references/noise-sources.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-review-pr/SKILL.md`; `.claude/skills/env-var-conventions/SKILL.md`; `.claude/skills/generate-profile/SKILL.md` 等 313 个文件
  - runtime-model: `.pre-commit-config.yaml`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/src/buckets_reorg.rs` 等 229 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `.claude/skills/kernel-organization/SKILL.md`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `python/sglang/kernels/README.md` 等 865 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/main.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/decode.rs`; `experimental/sgl-router/tests/component/policies/fused_score.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs` 等 964 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ee0f2375e5` - Sync/official main daily 20260907 (#328)

- Full hash: `ee0f2375e5fb285e4fb021a9831fa88018244679`
- Date/author: 2026-09-08 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py` 等 3141 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/_pr-test-rust-ext-build.yml`; `.github/workflows/_pr-test-simulator-cpu.yml` 等 43 个文件
  - docs-bench: `benchmark/asr/bench_sglang.py`; `benchmark/bench_linear_attention/bench_kda_flashinfer_mtp.py`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_client.py`; `benchmark/hf3fs/bench_storage.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/hicache/bench_mix.py`; `benchmark/hicache/bench_multiturn.py` 等 106 个文件
  - other: `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`; `.claude/skills/sglang-prod-incident-triage/scripts/incident_artifact_tool.py`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.git-blame-ignore-revs`; `.gitignore` 等 399 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/policy_select.rs`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml`; `experimental/sgl-router/sgl-kv-indexer/README.md` 等 310 个文件
  - runtime-perf: `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `3rdparty/amd/wheel/sgl-kernel/rocm_hipify.py`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `python/sglang/kernels/aot/benchmark/bench_amd_deterministic_allreduce.py` 等 575 个文件
  - tests: `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_add_imports.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_extract_symbols_to_new_module.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_assign.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_symbol.py`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs` 等 1708 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `50bacb0280` - Sync/official main daily 20260831 (#273)

- Full hash: `50bacb028023ba6d0155267a7c0f7841d5ec3fd7`
- Date/author: 2026-09-01 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/nightly-test-npu.yml` 等 1215 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-stage.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`; `.github/workflows/nightly-test-npu.yml`; `.github/workflows/pr-test-amd-extra.yml` 等 21 个文件
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/lean_kernel_sweep.py`; `benchmark/unified_memory/bench_peer_aware_eviction.py`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` 等 84 个文件
  - other: `.claude/skills/sglang-runtime-context/SKILL.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134`; `docker/kimi_k3/apply_deepep_k3_patch.sh`; `docker/kimi_k3/kimi_k3_cu12.Dockerfile`; `docker/kimi_k3/kimi_k3_cu13.Dockerfile`; `docker/npu.Dockerfile`; `python/pyproject.toml` 等 242 个文件
  - runtime-model: `python/sglang/benchmark/one_batch_server.py`; `python/sglang/launch_server.py`; `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/bailing_hybrid.py`; `python/sglang/srt/configs/embedding_model_spec.py`; `python/sglang/srt/configs/hybrid_arch.py`; `python/sglang/srt/configs/inkling.py`; `python/sglang/srt/configs/load_config.py` 等 88 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/cmake/flashmla.cmake`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`; `python/sglang/kernels/aot/csrc/cpu/extend.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 360 个文件
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`; `python/sglang/test/ascend/e2e/test_npu_multi_node_utils.py`; `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`; `python/sglang/test/ci/ci_utils.py`; `python/sglang/test/ci/fork_test_worker.py`; `python/sglang/test/config_publishers.py`; `python/sglang/test/gpt_oss_common.py` 等 420 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2d561a3ec2` - chore: add modification notices for DCU changes

- Full hash: `2d561a3ec23bdc4e0bfeebf73eea1fe638dc3e80`
- Date/author: 2026-07-05 / Lv Jiajia
- Auto category: 性能/后端优化
- Main files: `NOTICE`, `THIRD_PARTY_NOTICES.md`, `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/include/sgl_kernel/utils.h`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 250 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `NOTICE`; `THIRD_PARTY_NOTICES.md`; `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py` 等 23 个文件
  - runtime-model: `python/sglang/srt/model_executor/input_buffers.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/speculative/eagle_worker.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/jit_kernel/dsv4/compress.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/include/sgl_kernel/utils.h`; `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py` 等 68 个文件
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/few_shot_gsm8k.py`; `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_mmlu.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `sgl-kernel/tests/test_moe_align.py`; `sgl-kernel/tests/test_norm.py` 等 153 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `dbe95efd88` - 修复IPC报错的问题

- Full hash: `dbe95efd8883c2e73ed7041030b7afd3ab71e345`
- Date/author: 2026-07-01 / luoyao
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/moss_vl.py`, `python/sglang/srt/multimodal/processors/transformers_auto.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/moss_vl.py`; `python/sglang/srt/multimodal/processors/transformers_auto.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_START -->
## Local-only branch update from hg-full-base to main

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `hg-full-base`@`92b1d382c`, `main`@`5343b311c`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-05
- Commits in this section: 1 (merges: 0)
- Branch segments: `hg-full-base..main`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/multimodal/processors/base_processor.py` | `dbe95efd8` |
| `python/sglang/srt/multimodal/processors/moss_vl.py` | `dbe95efd8` |
| `python/sglang/srt/multimodal/processors/transformers_auto.py` | `dbe95efd8` |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-01 | `dbe95efd8` | `hg-full-base..main` | 缺陷修复 | 修复IPC报错的问题 | `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/moss_vl.py`, `python/sglang/srt/multimodal/processors/transformers_auto.py` |

### Per-Commit Audit Cards

#### Commit `dbe95efd8` - 修复IPC报错的问题

- Full hash: `dbe95efd8883c2e73ed7041030b7afd3ab71e345`
- Date/author: 2026-07-01 / luoyao
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/moss_vl.py`, `python/sglang/srt/multimodal/processors/transformers_auto.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/moss_vl.py`; `python/sglang/srt/multimodal/processors/transformers_auto.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_END -->
