# sglang Hunyuan3 Preview 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx` | `ab43824b09`, `50bacb0280` |
| `docs/cookbook/autoregressive/Tencent/Hy3.mdx` | `50bacb0280`, `16d7caa106` |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx` | `4975d6490a`, `ab43824b09`, `16229e94d0`, `ca25bc4275` |
| `docs/src/snippets/autoregressive/hunyuan3-preview-deployment.jsx` | 无直接提交 |
| `docs/src/snippets/configs/tencent/hy3-benchmarks.jsx` | 无直接提交 |
| `docs/src/snippets/configs/tencent/hy3.jsx` | `ee0f2375e5` |
| `python/sglang/srt/function_call/hunyuan_detector.py` | `ee0f2375e5`, `50bacb0280` |
| `test/registered/unit/function_call/test_hunyuan_detector.py` | `4975d6490a`, `ee0f2375e5` |

## 本地提交覆盖总览

- 来源工作树: `HYGON-AI/sglang-das`
- 生成日期: 2026-11-05
- 文档提交数: 7
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-20 | `4975d6490a` | 性能/后端优化 | Sync/official main daily 20261019 (#560) | `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md` |
| 2026-09-29 | `ab43824b09` | 性能/后端优化 | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` |
| 2026-09-20 | `16229e94d0` | 性能/后端优化 | Sync/official main daily 20260920 (#410) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md` |
| 2026-09-14 | `ca25bc4275` | 性能/后端优化 | Sync/official main daily 20260914 (#362) | `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` |
| 2026-09-08 | `ee0f2375e5` | 性能/后端优化 | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` |
| 2026-09-01 | `50bacb0280` | 性能/后端优化 | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` |
| 2026-08-25 | `16d7caa106` | 性能/后端优化 | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` |

## 逐 Commit 审计卡

### Commit `4975d6490a` - Sync/official main daily 20261019 (#560)

- 完整 hash: `4975d6490ac2c71c2d88c8a86b96a6f7061050ab`
- 时间/作者: 2026-10-20 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md`, `.agents/skills/processor-model-parity/SKILL.md`, `.agents/skills/write-sglang-test/SKILL.md`, `.claude/rules/prefer-sgl-eval.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 2248 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/pull_request_template.md`; `.github/scripts/pr-check-comment.cjs` 等 54 个文件
  - docs-bench: `benchmark/hicache/bench_host_memory_migration.py`; `benchmark/kernels/lora_csgmv/bench_csgmv_split_k.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/cookbook/autoregressive/Cloudflare/clef.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`; `docs/cookbook/autoregressive/IFM/Jais-3.mdx` 等 155 个文件
  - other: `.agents/skills/cookbook-add-model/SKILL.md`; `.agents/skills/generate-profile/SKILL.md`; `.agents/skills/processor-model-parity/SKILL.md`; `.claude/rules/prefer-sgl-eval.md`; `.gitignore`; `README.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134` 等 336 个文件
  - runtime-model: `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/ARCHITECTURE.md`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/REFERENCE.md` 等 335 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/README.md`; `python/sglang/kernels/__init__.py`; `python/sglang/kernels/aot/benchmark/bench_dsv4_norm_rope.py`; `python/sglang/kernels/aot/benchmark/bench_flashmla_mega.py` 等 574 个文件
  - tests: `.agents/skills/write-sglang-test/SKILL.md`; `docs/scripts/tests/wan-animate-2-config.test.mjs`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_peer_bootstrap.rs`; `experimental/sgl-router/tests/component/policies_reorg.rs`; `experimental/sgl-router/tests/component/policies_reorg_admission.rs` 等 794 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ab43824b09` - Sync/official main daily 20260928 (#452)

- 完整 hash: `ab43824b09055fc790bd5a9166a6a6182b1bccc3`
- 时间/作者: 2026-09-29 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/clean-startup-log/SKILL.md`, `.claude/skills/clean-startup-log/references/noise-sources.md`, `.claude/skills/cookbook-add-model/SKILL.md` 等 2576 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/MAINTAINER.md`; `.github/actions/check-pr-test-health/action.test.cjs`; `.github/actions/check-pr-test-health/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml` 等 38 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/disaggregation/bench_cached_prefix.py`; `benchmark/dllm/README.md`; `benchmark/gsm8k/README.md`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/io/bench_mm_token_padding.py`; `benchmark/kernels/all_gather/benchmark_mscclpp.py` 等 167 个文件
  - other: `.claude/rules/cookbook-first.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/clean-startup-log/SKILL.md`; `.claude/skills/clean-startup-log/references/noise-sources.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-review-pr/SKILL.md`; `.claude/skills/env-var-conventions/SKILL.md`; `.claude/skills/generate-profile/SKILL.md` 等 313 个文件
  - runtime-model: `.pre-commit-config.yaml`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/src/buckets_reorg.rs` 等 229 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `.claude/skills/kernel-organization/SKILL.md`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `python/sglang/kernels/README.md` 等 865 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/main.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/decode.rs`; `experimental/sgl-router/tests/component/policies/fused_score.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs` 等 964 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `16229e94d0` - Sync/official main daily 20260920 (#410)

- 完整 hash: `16229e94d0a0a218875ab0db2133c12d9695abd1`
- 时间/作者: 2026-09-20 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 1391 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/amd-aiter-scout.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/bot-bump-sglang-version.yml`; `.github/workflows/ci-coverage-overview.yml` 等 26 个文件
  - docs-bench: `benchmark/agentic-rollout/README.md`; `benchmark/agentic-rollout/explore.py`; `benchmark/agentic-rollout/metrics.py`; `benchmark/agentic-rollout/plot.py`; `benchmark/agentic-rollout/simulate.py`; `benchmark/agentic-rollout/spec/README.md`; `benchmark/agentic-rollout/spec/evidence/feature-00-session-hicache-latency.md`; `benchmark/agentic-rollout/spec/feature-00-session-hicache-latency.md` 等 100 个文件
  - other: `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`; `.claude/skills/ci-test-audit/SKILL.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.gitignore`; `.gitleaksignore`; `docker/Dockerfile.cu134`; `docker/npu.Dockerfile` 等 177 个文件
  - runtime-model: `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/deny.toml`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json` 等 205 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/cpu/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/cpu/bmm.cpp` 等 417 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `benchmark/agentic-rollout/tests/test_explore.py`; `benchmark/agentic-rollout/tests/test_simulate.py`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs`; `experimental/sgl-router/tests/component/policies/kv_events_two_subscribers.rs`; `experimental/sgl-router/tests/component/policies/zmq_helpers.rs` 等 466 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ca25bc4275` - Sync/official main daily 20260914 (#362)

- 完整 hash: `ca25bc4275b93e02a48a2f8158835f372fee3553`
- 时间/作者: 2026-09-14 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.codespellrc` 等 1457 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/workflows/_docker-build-and-publish.yml` 等 43 个文件
  - docs-bench: `benchmark/bench_linear_attention/bench_int8_checkpoint_reuse.py`; `benchmark/kernels/attention/bench_gdn_replayssm_decode.py`; `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/simulator/bench_runner.py`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx` 等 112 个文件
  - other: `.claude/rules/unit-test-admission.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-migrate-model/SKILL.md`; `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.codespellrc`; `.gitleaksignore`; `3rdparty/amd/wheel/README.md` 等 194 个文件
  - runtime-model: `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/src/policies/buckets.rs`; `experimental/sgl-router/src/policies/mod.rs`; `experimental/sgl-router/src/proxy/mod.rs`; `experimental/sgl-router/src/proxy/sse.rs`; `experimental/sgl-router/src/server/metrics.rs`; `experimental/sgl-router/src/server/routes/chat.rs`; `python/sglang/launch_server.py` 等 85 个文件
  - runtime-perf: `3rdparty/amd/wheel/sgl-kernel/build_rocm.sh`; `3rdparty/amd/wheel/sgl-kernel/rename_wheels_rocm.sh`; `docker/patches/sgl-kernel-gfx1151.sh`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/Dockerfile` 等 357 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/proxy/bucket_routing.rs`; `experimental/sgl-router/tests/proxy/chat_routing.rs`; `python/sglang/kernels/aot/tests/test_awq_dequant.py`; `python/sglang/kernels/aot/tests/test_cutlass_mla.py`; `python/sglang/kernels/aot/tests/test_flash_attn_sparse.py`; `python/sglang/kernels/aot/tests/test_fused_qk_norm_rope.py` 等 666 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ee0f2375e5` - Sync/official main daily 20260907 (#328)

- 完整 hash: `ee0f2375e5fb285e4fb021a9831fa88018244679`
- 时间/作者: 2026-09-08 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py` 等 3141 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/_pr-test-rust-ext-build.yml`; `.github/workflows/_pr-test-simulator-cpu.yml` 等 43 个文件
  - docs-bench: `benchmark/asr/bench_sglang.py`; `benchmark/bench_linear_attention/bench_kda_flashinfer_mtp.py`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_client.py`; `benchmark/hf3fs/bench_storage.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/hicache/bench_mix.py`; `benchmark/hicache/bench_multiturn.py` 等 106 个文件
  - other: `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`; `.claude/skills/sglang-prod-incident-triage/scripts/incident_artifact_tool.py`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.git-blame-ignore-revs`; `.gitignore` 等 399 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/policy_select.rs`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml`; `experimental/sgl-router/sgl-kv-indexer/README.md` 等 310 个文件
  - runtime-perf: `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `3rdparty/amd/wheel/sgl-kernel/rocm_hipify.py`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `python/sglang/kernels/aot/benchmark/bench_amd_deterministic_allreduce.py` 等 575 个文件
  - tests: `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_add_imports.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_extract_symbols_to_new_module.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_assign.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_symbol.py`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs` 等 1708 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `50bacb0280` - Sync/official main daily 20260831 (#273)

- 完整 hash: `50bacb028023ba6d0155267a7c0f7841d5ec3fd7`
- 时间/作者: 2026-09-01 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/nightly-test-npu.yml` 等 1215 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-stage.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`; `.github/workflows/nightly-test-npu.yml`; `.github/workflows/pr-test-amd-extra.yml` 等 21 个文件
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/lean_kernel_sweep.py`; `benchmark/unified_memory/bench_peer_aware_eviction.py`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` 等 84 个文件
  - other: `.claude/skills/sglang-runtime-context/SKILL.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134`; `docker/kimi_k3/apply_deepep_k3_patch.sh`; `docker/kimi_k3/kimi_k3_cu12.Dockerfile`; `docker/kimi_k3/kimi_k3_cu13.Dockerfile`; `docker/npu.Dockerfile`; `python/pyproject.toml` 等 242 个文件
  - runtime-model: `python/sglang/benchmark/one_batch_server.py`; `python/sglang/launch_server.py`; `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/bailing_hybrid.py`; `python/sglang/srt/configs/embedding_model_spec.py`; `python/sglang/srt/configs/hybrid_arch.py`; `python/sglang/srt/configs/inkling.py`; `python/sglang/srt/configs/load_config.py` 等 88 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/cmake/flashmla.cmake`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`; `python/sglang/kernels/aot/csrc/cpu/extend.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 360 个文件
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`; `python/sglang/test/ascend/e2e/test_npu_multi_node_utils.py`; `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`; `python/sglang/test/ci/ci_utils.py`; `python/sglang/test/ci/fork_test_worker.py`; `python/sglang/test/config_publishers.py`; `python/sglang/test/gpt_oss_common.py` 等 420 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `16d7caa106` - sync(hcu): official main through 20260824 (c8e1ddc707)

- 完整 hash: `16d7caa1065abd2af782f3afc35c3dc4da745cde`
- 时间/作者: 2026-08-25 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`, `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`, `.claude/skills/sglang-runtime-context/SKILL.md` 等 1308 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/labeler.yml`; `.github/update_ci_permission.py`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 41 个文件
  - docs-bench: `benchmark/hicache/bench_buffer_mode.py`; `docs/cookbook/autoregressive/Baidu/PaddleOCR-VL.mdx`; `docs/cookbook/autoregressive/Baidu/Unlimited-OCR.mdx`; `docs/cookbook/autoregressive/DeepReinforce/Ornith-1.0.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-4.6V.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/Google/Gemma4.mdx` 等 79 个文件
  - other: `.claude/rules/comment-style.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `3rdparty/amd/wheel/sglang/pyproject.toml`; `README.md` 等 183 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/sgl-kv-indexer/.gitignore`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml`; `experimental/sgl-router/sgl-kv-indexer/README.md` 等 190 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `python/sglang/kernel_api_logging.py`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/cpu/activation.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 271 个文件
  - tests: `experimental/sgl-router/sgl-kv-indexer/tests/common/id.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/net.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/memory_integration.rs`; `experimental/sgl-router/tests/component/policies/cache_aware_zmq.rs`; `experimental/sgl-router/tests/e2e/chat_completions/test_two_router_convergence.py`; `experimental/sgl-router/tests/e2e/infra/gateway.py` 等 544 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_START -->
## hg-full-base 到 main 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `hg-full-base`@`92b1d382c`, `main`@`5343b311c`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 25（其中 merge 0）
- 分支更新段: `hg-full-base..main`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/hunyuan_v3.py` | `6ae083114`, `237b7de51`, `62a23f050`, `d32fa4686`, `56b6eebcc`, `c0b27a966`, `fffe84acb`, `3b0e1b709`, `92c15b3d8`, `02858213c`, `baf11236a`, `5eb556f88`, ... (24 total) |
| `python/sglang/srt/layers/moe/topk.py` | `4fb3f0939`, `0d61dcb98`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/distributed/parallel_state.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/layernorm.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `6ae083114`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/bailing_moe.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v4.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/hunyuan_v3_nextn.py` | `6844a8693`, `fffe84acb`, `baf11236a`, `5eb556f88`, `123e9539e` |
| `python/sglang/srt/models/mimo_v2.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/minimax_m2.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen2.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen3.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen3_5.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen3_moe.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/moe/mega_moe.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `4fb3f0939`, `1e2fec228`, `38c750157`, `123e9539e` |
| `python/sglang/srt/environ.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/metadata.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f` |
| `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` | `4fb3f0939`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py` | `4fb3f0939`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/quantization/fp8.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/moe_wna16.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_fp8.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_int8.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/model_executor/model_runner.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v2.py` | `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| ... | 另有 135 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-03 | `6ae083114` | `hg-full-base..main` | 性能/后端优化 | add topk fused op | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-06-03 | `237b7de51` | `hg-full-base..main` | 性能/后端优化 | [feat]: 添加rms_rotary_embedding_fuse_with_kv_store融合算子 | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-06-16 | `62a23f050` | `hg-full-base..main` | 模型支持/运行时入口 | [feat]: HY3 support PP | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-06-16 | `d32fa4686` | `hg-full-base..main` | 模型支持/运行时入口 | [feat]: HY3 support PP | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-06-16 | `56b6eebcc` | `hg-full-base..main` | 模型支持/运行时入口 | [feat]: HY3 support PP | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-06-25 | `6844a8693` | `hg-full-base..main` | 模型支持/运行时入口 | feat: hy3 mtp support dp attention | `python/sglang/srt/models/hunyuan_v3_nextn.py` |
| 2026-06-30 | `c0b27a966` | `hg-full-base..main` | 调度/缓存/PD | [feat]: 支持pd分离下hunyuanv3 p节点ep8跑通. | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-06 | `fffe84acb` | `hg-full-base..main` | 模型支持/运行时入口 | feat: support EPLB for hunyuan_v3 and hunyuan_v3_nextn | `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py` |
| 2026-07-06 | `3b0e1b709` | `hg-full-base..main` | 缺陷修复 | [bug fix] hunyuanv3精度异常解决 | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-06 | `92c15b3d8` | `hg-full-base..main` | 缺陷修复 | [bug fix] hunyuanv3精度异常解决 | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-07 | `02858213c` | `hg-full-base..main` | 缺陷修复 | style: fix pre-commit formatting | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` 等 4 个文件 |
| 2026-07-08 | `baf11236a` | `hg-full-base..main` | 缺陷修复 | style: fix pre-commit formatting for hunyuan_v3 and hunyuan_v3_nextn | `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py` |
| 2026-07-08 | `5eb556f88` | `hg-full-base..main` | 模型支持/运行时入口 | [feature]:hunyuan_v3 EPLB support with redundant experts | `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py` |
| 2026-07-09 | `fcc3e6e18` | `hg-full-base..main` | 模型支持/运行时入口 | resolve conflict: merge PP support with EPLB changes on hunyuan_v3.py | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-09 | `5fdffaac3` | `hg-full-base..main` | 模型支持/运行时入口 | Revert "resolve conflict: merge PP support with EPLB changes on hunyuan_v3.py" | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-09 | `fba577896` | `hg-full-base..main` | 模型支持/运行时入口 | Revert "[feat]: HY3 support PP" | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-13 | `4fb3f0939` | `hg-full-base..main` | 性能/后端优化 | runtime: migrate current main DCU interfaces to HCU | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` 等 80 个文件 |
| 2026-07-14 | `0d61dcb98` | `hg-full-base..main` | 性能/后端优化 | fix(eplb): fix static/dynamic EPLB accuracy and layer broadcast bug in expert dump | `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-16 | `8e5e785ea` | `hg-full-base..main` | 缺陷修复 | style: fix pre-commit formatting in hunyuan_v3.py | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-20 | `1e2fec228` | `hg-full-base..main` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-07-22 | `73c7e6c8f` | `hg-full-base..main` | 性能/后端优化 | [feat]:迁移lightop调用方式到新的接口. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 38 个文件 |
| 2026-07-27 | `38c750157` | `hg-full-base..main` | 性能/后端优化 | fix：修复接口改动. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 21 个文件 |
| 2026-07-29 | `24201e257` | `hg-full-base..main` | 性能/后端优化 | fix(hy3): apply router_scaling_factor when not fused into topk | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-30 | `716cb09f8` | `hg-full-base..main` | 性能/后端优化 | fix(hy3): always post-multiply rsf when not fused into topk | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-07-31 | `123e9539e` | `hg-full-base..main` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |

### 逐 Commit 审计卡

#### Commit `6ae083114` - add topk fused op

- 完整 hash: `6ae0831145c2f896e59657f5bbf96e6624f10115`
- 时间/作者: 2026-06-03 / wujl5
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `237b7de51` - [feat]: 添加rms_rotary_embedding_fuse_with_kv_store融合算子

- 完整 hash: `237b7de518fb1297823d0de4181e3d85cd6f959a`
- 时间/作者: 2026-06-03 / LuoYao
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `62a23f050` - [feat]: HY3 support PP

- 完整 hash: `62a23f050dededc6028928b9600d31f307fe72a6`
- 时间/作者: 2026-06-16 / wujl5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `d32fa4686` - [feat]: HY3 support PP

- 完整 hash: `d32fa4686df8c5dc88437f2baaea2af8e3d4b190`
- 时间/作者: 2026-06-16 / wujl5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `56b6eebcc` - [feat]: HY3 support PP

- 完整 hash: `56b6eebcc0edc6c758b499f3733d3000b7987e88`
- 时间/作者: 2026-06-16 / wujl5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `6844a8693` - feat: hy3 mtp support dp attention

- 完整 hash: `6844a86938e1a037dad606df79f4ce3a293d65ae`
- 时间/作者: 2026-06-25 / janeeyreliu
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c0b27a966` - [feat]: 支持pd分离下hunyuanv3 p节点ep8跑通.

- 完整 hash: `c0b27a9668b5130b0d37aa9d9b271ee2864a3a1b`
- 时间/作者: 2026-06-30 / LuoYao
- 分支更新段: `hg-full-base..main`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `fffe84acb` - feat: support EPLB for hunyuan_v3 and hunyuan_v3_nextn

- 完整 hash: `fffe84acbfd8a7e77acf084d6b4268e0beaee2c4`
- 时间/作者: 2026-07-06 / liuchy5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `3b0e1b709` - [bug fix] hunyuanv3精度异常解决

- 完整 hash: `3b0e1b7096a2ae4f956ea614ba47b7b16041a397`
- 时间/作者: 2026-07-06 / luoyao
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `92c15b3d8` - [bug fix] hunyuanv3精度异常解决

- 完整 hash: `92c15b3d80868770f27d4a2060c4b5fcc9528432`
- 时间/作者: 2026-07-06 / luoyao
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `02858213c` - style: fix pre-commit formatting

- 完整 hash: `02858213c9623635bc74628fc9890fef789fb5b6`
- 时间/作者: 2026-07-07 / LuoYao
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `baf11236a` - style: fix pre-commit formatting for hunyuan_v3 and hunyuan_v3_nextn

- 完整 hash: `baf11236a9c594f669bdf6706906fb29a5578507`
- 时间/作者: 2026-07-08 / liuchy5
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `5eb556f88` - [feature]:hunyuan_v3 EPLB support with redundant experts

- 完整 hash: `5eb556f88bf2a431ccf0832a42ed69d75a1671c0`
- 时间/作者: 2026-07-08 / liuchy5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/hunyuan_v3_nextn.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `fcc3e6e18` - resolve conflict: merge PP support with EPLB changes on hunyuan_v3.py

- 完整 hash: `fcc3e6e1890f7e0c2d476258cc2ec1878ae4c5e9`
- 时间/作者: 2026-07-09 / liuchy5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `5fdffaac3` - Revert "resolve conflict: merge PP support with EPLB changes on hunyuan_v3.py"

- 完整 hash: `5fdffaac3808992e8f4070fb4879274d3db5fbd8`
- 时间/作者: 2026-07-09 / liuchy5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `fba577896` - Revert "[feat]: HY3 support PP"

- 完整 hash: `fba577896ec4cf89a01752393ae4c9f6e12ae2be`
- 时间/作者: 2026-07-09 / liuchy5
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `4fb3f0939` - runtime: migrate current main DCU interfaces to HCU

- 完整 hash: `4fb3f09391ef791a7dd3811b0c610d6b89ae8ea0`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py` 等 80 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/layers/mhc.py`; `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/model_loader/loader.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py`; `python/sglang/srt/models/minimax_m2.py` 等 13 个文件
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`; `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py` 等 52 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `0d61dcb98` - fix(eplb): fix static/dynamic EPLB accuracy and layer broadcast bug in expert dump

- 完整 hash: `0d61dcb9883887194a05612e4e982b020f686575`
- 时间/作者: 2026-07-14 / janeeyreliu
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `8e5e785ea` - style: fix pre-commit formatting in hunyuan_v3.py

- 完整 hash: `8e5e785ea7a9829fea82d93c04f024048ad5b617`
- 时间/作者: 2026-07-16 / liuchy5
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `1e2fec228` - feat(hcu): port runtime and kernel rename

- 完整 hash: `1e2fec228a9a8b1e781c3592eff356eeb8b584ed`
- 时间/作者: 2026-07-20 / tianlinyang77
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/jit_kernel/dsv4/moe.py`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/mxfp8.py` 等 109 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/check_env.py`; `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/fp8_blockwise_gemm.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/mxfp8.py`; `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` 等 80 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `sgl-kernel/tests/test_moe_align.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `73c7e6c8f` - [feat]:迁移lightop调用方式到新的接口.

- 完整 hash: `73c7e6c8f50ff20c1093426c6adf88744ef9c202`
- 时间/作者: 2026-07-22 / luoyao
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/attention/dsv4/quant_k_cache.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py` 等 38 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_5.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/attention/dsv4/metadata.py`; `python/sglang/srt/layers/attention/dsv4/quant_k_cache.py`; `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/flashattention_backend.py` 等 26 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `38c750157` - fix：修复接口改动.

- 完整 hash: `38c750157fb1485c24cc9135e71c923a6054ee66`
- 时间/作者: 2026-07-27 / luoyao
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/moe/mega_moe.py` 等 21 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_5.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`; `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`; `python/sglang/srt/layers/moe/topk.py` 等 12 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `24201e257` - fix(hy3): apply router_scaling_factor when not fused into topk

- 完整 hash: `24201e257197ee700d251b216689d572d501116c`
- 时间/作者: 2026-07-29 / yht183
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `716cb09f8` - fix(hy3): always post-multiply rsf when not fused into topk

- 完整 hash: `716cb09f806321a81fe130118c69a3a6ef932280`
- 时间/作者: 2026-07-30 / yht183
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/hunyuan_v3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `123e9539e` - fix lint: satisfy pre-commit on the forward-port diff

- 完整 hash: `123e9539ea23dde2f1a12b0374c1375bbfb10989`
- 时间/作者: 2026-07-31 / RyeYuan
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py` 等 91 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py` 等 14 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py` 等 19 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py` 等 56 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_mmlu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_END -->
