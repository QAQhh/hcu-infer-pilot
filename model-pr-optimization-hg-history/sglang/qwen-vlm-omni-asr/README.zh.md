# sglang Qwen VLM/Omni/ASR 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3-Nano-Omni.mdx` | `ab43824b09`, `16d7caa106` |
| `docs/cookbook/omni/FishAudio/S2-Pro.mdx` | 无直接提交 |
| `docs/cookbook/omni/intro.mdx` | 无直接提交 |
| `docs/src/snippets/autoregressive/nemotron3-nano-omni-deployment.jsx` | 无直接提交 |
| `examples/chat_template/qwen3_vl_reranker.jinja` | 无直接提交 |
| `examples/runtime/qwen3_vl_reranker.py` | `ee0f2375e5` |
| `python/sglang/srt/arg_groups/model_overrides/qwen3_vl.py` | `ab43824b09`, `ca25bc4275`, `50bacb0280` |
| `python/sglang/srt/configs/qwen3_asr.py` | `ee0f2375e5` |
| `python/sglang/srt/configs/qwen3_omni.py` | `36b93840b5`, `ee0f2375e5` |
| `python/sglang/srt/configs/qwen3_vl.py` | `16229e94d0` |
| `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py` | `16d7caa106` |
| `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py` | `16d7caa106` |
| `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` | 无直接提交 |
| `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` | `4975d6490a` |
| `python/sglang/srt/models/dots3_common/dots_omni_audio.py` | `ee0f2375e5`, `16d7caa106` |
| `python/sglang/srt/models/dots3_common/dots_omni_towers.py` | `16d7caa106` |
| `python/sglang/srt/models/dots3_common/dots_omni_vision.py` | `16d7caa106` |
| `python/sglang/srt/models/glmasr.py` | `4975d6490a`, `ab43824b09`, `16d7caa106` |
| `python/sglang/srt/models/muse_spark_omni.py` | `4975d6490a` |
| `python/sglang/srt/models/qwen2_5_vl.py` | `4975d6490a`, `36b93840b5`, `ab43824b09`, `16229e94d0`, `ee0f2375e5`, `50bacb0280`, `16d7caa106`, `b97d7df6ee`, `aa2309e220`, `e5a4e379b0` |
| `python/sglang/srt/models/qwen2_audio.py` | `4975d6490a`, `ab43824b09` |
| `python/sglang/srt/models/qwen2_vl.py` | `4975d6490a`, `ab43824b09`, `ee0f2375e5` |
| `python/sglang/srt/models/qwen3_asr.py` | `4975d6490a`, `ab43824b09` |
| `python/sglang/srt/models/qwen3_omni_moe.py` | `ee0f2375e5` |
| `python/sglang/srt/models/qwen3_vl.py` | `4975d6490a`, `36b93840b5`, `ab43824b09`, `16229e94d0`, `ca25bc4275`, `ee0f2375e5`, `50bacb0280`, `7b3548f974`, `16d7caa106`, `b97d7df6ee`, `123e9539ea`, `aa2309e220`, ... (13 total) |
| `python/sglang/srt/models/qwen3_vl_moe.py` | `36b93840b5`, `ab43824b09`, `50bacb0280` |
| `python/sglang/srt/multimodal/processors/dots_note_omni.py` | `16d7caa106` |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/__init__.py` | `16d7caa106` |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/flatten_runner.py` | `16d7caa106` |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/preprocess.py` | `16d7caa106` |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/v2core.py` | `16d7caa106` |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/video_qa_flattener.py` | `16d7caa106` |
| `python/sglang/srt/multimodal/processors/glmasr.py` | `50bacb0280`, `16d7caa106` |
| `python/sglang/srt/multimodal/processors/muse_spark_omni.py` | `4975d6490a` |
| `python/sglang/srt/multimodal/processors/qwen3_asr.py` | `ee0f2375e5`, `50bacb0280` |
| `python/sglang/srt/multimodal/processors/qwen_vl.py` | `4975d6490a`, `16229e94d0`, `ca25bc4275`, `ee0f2375e5` |
| `python/sglang/test/external_models/custom_qwen2_vl.py` | 无直接提交 |
| `test/manual/models/test_qwen3_asr.py` | `ee0f2375e5` |
| `test/registered/hcu/vlm_models/bw1100/test_qwen2_vl_2b_server_hcu.py` | `b781224d4d`, `c43b06722a`, `f38f1a5d21` |
| `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py` | `ee0f2375e5` |
| `test/registered/npu/accuracy/qwen3_omni_30b_a3b_thinking/test_npu_qwen3_omni_30b_a3b_thinking_1p_mmmu.py` | `ca25bc4275`, `16d7caa106` |
| `test/registered/npu/accuracy/qwen3_vl_30b_a3b/test_npu_qwen3_vl_30b_a3b_bf16_2p_gsm8k.py` | `ee0f2375e5`, `16d7caa106` |
| `test/registered/npu/accuracy/qwen3_vl_30b_a3b_thinking/test_npu_qwen3_vl_30b_a3b_thinking_1p_mmmu.py` | `ee0f2375e5`, `50bacb0280`, `16d7caa106` |
| `test/registered/npu/accuracy/qwen3_vl_8b/test_npu_qwen3_vl_8b_bf16_2p_gsm8k.py` | `ca25bc4275`, `ee0f2375e5`, `16d7caa106` |
| `test/registered/npu/accuracy/qwen3_vl_8b_thinking/test_npu_qwen3_vl_8b_thinking_1p_mmmu.py` | `ee0f2375e5`, `50bacb0280`, `16d7caa106` |
| `test/registered/npu/vlm_models/test_npu_qwen2_5_vl_3b_instruct.py` | `16d7caa106` |
| `test/registered/npu/vlm_models/test_npu_qwen2_5_vl_72b_instruct.py` | `16d7caa106` |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_235b_a22b_instruct.py` | `16d7caa106` |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_30b_a3b_instruct.py` | `16d7caa106` |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_4b_instruct.py` | 无直接提交 |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_8b_instruct.py` | `16d7caa106` |
| `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` | `4975d6490a`, `ca25bc4275`, `ee0f2375e5` |
| `test/registered/unit/multimodal/test_dots_note_omni.py` | `ee0f2375e5`, `16d7caa106` |

## 本地提交覆盖总览

- 来源工作树: `HYGON-AI/sglang-das`
- 生成日期: 2026-11-05
- 文档提交数: 20
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-20 | `4975d6490a` | 性能/后端优化 | Sync/official main daily 20261019 (#560) | `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md` |
| 2026-10-12 | `36b93840b5` | 性能/后端优化 | Sync/official main daily 20261009 (#500) | `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md` |
| 2026-09-29 | `ab43824b09` | 性能/后端优化 | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` |
| 2026-09-20 | `16229e94d0` | 性能/后端优化 | Sync/official main daily 20260920 (#410) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md` |
| 2026-09-14 | `ca25bc4275` | 性能/后端优化 | Sync/official main daily 20260914 (#362) | `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` |
| 2026-09-08 | `ee0f2375e5` | 性能/后端优化 | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` |
| 2026-09-01 | `50bacb0280` | 性能/后端优化 | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` |
| 2026-08-25 | `7b3548f974` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` |
| 2026-08-25 | `16d7caa106` | 性能/后端优化 | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` |
| 2026-08-03 | `b97d7df6ee` | 性能/后端优化 | Forward port/v0.5.12 dev daily 20260729 (#146) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml` |
| 2026-07-31 | `123e9539ea` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` |
| 2026-07-24 | `b781224d4d` | 性能/后端优化 | Rename DCU integration to HCU and sanitize runtime logs | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` |
| 2026-07-22 | `aa2309e220` | 性能/后端优化 | chore(compliance): add HYGON headers and provenance | `README.md`, `THIRD_PARTY_NOTICES.md`, `python/sglang/check_env.py` |
| 2026-07-20 | `c43b06722a` | 性能/后端优化 | ci(hcu): port v0.5.12 wheel staging gate | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` |
| 2026-07-17 | `e5a4e379b0` | 缺陷修复 | Fix Qwen2.5-VL FA3 cu_seqlens | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2026-07-13 | `f38f1a5d21` | 性能/后端优化 | test: sync HCU registrations with current main | `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py` |
| 2026-07-05 | `1e967ec11d` | 性能/后端优化 | chore: add Apache headers for DCU files | `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py` |
| 2026-06-27 | `db4a263167` | 性能/后端优化 | test: use local DCU model paths for smoke tests | `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py` |
| 2026-06-25 | `a21b0b6ef2` | 性能/后端优化 | test: preserve local DCU AI smoke and accuracy cases | `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`, `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py` |
| 2026-05-18 | `c5dd815b3c` | 性能/后端优化 | dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6) | `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py` |

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

### Commit `36b93840b5` - Sync/official main daily 20261009 (#500)

- 完整 hash: `36b93840b54b8c41fe395e6f3e3f9a5463fe17ba`
- 时间/作者: 2026-10-12 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`, `.agents/skills/ci-test-audit/SKILL.md`, `.agents/skills/ci-test-audit/action-items.md`, `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/clean-startup-log/SKILL.md` 等 2736 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/check-maintenance/action.yml`; `.github/labeler.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 38 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/kernels/bench_block_verification.py`; `benchmark/kernels/fused_moe_triton/benchmark_sglang_fused_moe_triton.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/.mintignore`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-Math-V2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-OCR-2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-OCR.mdx` 等 154 个文件
  - other: `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`; `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`; `.agents/skills/ci-test-audit/SKILL.md`; `.agents/skills/ci-test-audit/action-items.md`; `.agents/skills/clean-startup-log/SKILL.md`; `.agents/skills/clean-startup-log/references/noise-sources.md`; `.agents/skills/compute-mamba-ratio/SKILL.md`; `.agents/skills/cookbook-add-model/SKILL.md` 等 475 个文件
  - runtime-model: `.agents/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.agents/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml` 等 351 个文件
  - runtime-perf: `.agents/skills/add-jit-kernel/SKILL.md`; `.agents/skills/add-sgl-kernel/SKILL.md`; `.agents/skills/debug-cuda-crash/SKILL.md`; `.agents/skills/debug-distributed-hang/SKILL.md`; `.agents/skills/kernel-organization/SKILL.md`; `.agents/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `.claude/rules/kernel-benchmark.md`; `.claude/skills/add-jit-kernel/SKILL.md` 等 705 个文件
  - tests: `.agents/skills/kl-consistency-test/SKILL.md`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/conftest.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/generator_testlib.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extract_functions.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extracts.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_imports.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_main_single_commit.py` 等 1013 个文件
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

### Commit `7b3548f974` - fix lint: apply pre-commit fixes across the 20260824 sync diff

- 完整 hash: `7b3548f97409d83b7e7dde4c3ad71e2f30955267`
- 时间/作者: 2026-08-25 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/utils.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/attention_registry.py` 等 46 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/hardware_backend/npu/utils.py`; `python/sglang/srt/sampling/sampling_batch_info.py`; `python/sglang/srt/speculative/draft_utils.py`; `python/sglang/srt/speculative/eagle_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`; `python/sglang/kernels/ops/moe/ep_moe_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 22 个文件
  - tests: `test/registered/hicache/test_hicache_storage_3fs_backend.py`; `test/registered/openai_server/validation/test_matched_stop.py`; `test/registered/pp/test_pp_single_node.py`; `test/registered/profiling/test_start_profile.py`; `test/registered/unit/entrypoints/openai/test_serving_embedding.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/unit/function_call/test_json_schema_constraint.py`; `test/registered/unit/mem_cache/test_radix_cache_unit.py` 等 12 个文件
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

### Commit `b97d7df6ee` - Forward port/v0.5.12 dev daily 20260729 (#146)

- 完整 hash: `b97d7df6ee606d51c8a96b07b447b1a536a7e0af`
- 时间/作者: 2026-08-03 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/quality-baseline-scan.yml`, `.github/workflows/release-pr-hcu.yml`, `README.md`, `README_DCU.md` 等 166 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/quality-baseline-scan.yml`; `.github/workflows/release-pr-hcu.yml`
  - docs-bench: `docs/dcu-pr-ci-visual-guide.html`; `docs/hcu-pr-ci-visual-guide.html`; `docs/internal/dcu-main-conflict-ledger.md`
  - other: `README.md`; `README_DCU.md`; `THIRD_PARTY_NOTICES.md`; `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/decode.py` 等 27 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py` 等 26 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/add_constant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh` 等 97 个文件
  - tests: `python/sglang/test/hcu_accuracy_report.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_server_guard.py`; `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `123e9539ea` - fix lint: satisfy pre-commit on the forward-port diff

- 完整 hash: `123e9539ea23dde2f1a12b0374c1375bbfb10989`
- 时间/作者: 2026-07-31 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` 等 88 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py` 等 18 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 54 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_mmlu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b781224d4d` - Rename DCU integration to HCU and sanitize runtime logs

- 完整 hash: `b781224d4dae58889ba9bcc3efc0ff20fb424dc4`
- 时间/作者: 2026-07-24 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-dcu.yml`, `.github/workflows/lint-hcu.yml` 等 464 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/open-source-compliance.json`; `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/dcu-manual-model-test.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-dcu.yml`; `.github/workflows/lint-hcu.yml` 等 14 个文件
  - docs-bench: `docs/dcu-pr-ci-visual-guide.html`; `docs/hcu-pr-ci-visual-guide.html`
  - other: `NOTICE`; `README.md`; `README_DCU.md`; `README_HCU.md`; `THIRD_PARTY_NOTICES.md`; `python/sglang/check_env.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py` 等 33 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/compress.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`; `python/sglang/kernels/ops/attention/dsa/tilelang_kernel.py` 等 76 个文件
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py` 等 325 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `aa2309e220` - chore(compliance): add HYGON headers and provenance

- 完整 hash: `aa2309e220d9a0df4325928ff969a214c7806e03`
- 时间/作者: 2026-07-22 / Lv Jiajia
- 自动分类: 性能/后端优化
- 主要文件: `README.md`, `THIRD_PARTY_NOTICES.md`, `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh` 等 151 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README.md`; `THIRD_PARTY_NOTICES.md`; `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py` 等 22 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py` 等 24 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/add_constant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh` 等 82 个文件
  - tests: `python/sglang/test/hcu_server_guard.py`; `python/sglang/test/simple_eval_common.py`; `test/manual/ep/test_eplb.py`; `test/manual/test_expert_distribution.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py` 等 23 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c43b06722a` - ci(hcu): port v0.5.12 wheel staging gate

- 完整 hash: `c43b06722a405fe04e5b38bdc332250b9816e349`
- 时间/作者: 2026-07-20 / tianlinyang77
- 自动分类: 性能/后端优化
- 主要文件: `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-dcu.yml`, `.github/workflows/lint-hcu.yml` 等 372 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/open-source-compliance.json`; `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/dcu-manual-model-test.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-dcu.yml`; `.github/workflows/lint-hcu.yml` 等 18 个文件
  - other: `README.md`; `README_HCU.md`; `requirements_dcu.txt`; `requirements_hcu.txt`; `scripts/ci/dcu/check_hcu_runtime_text.py`; `scripts/ci/dcu/dcu_ci_cleanup_container.sh`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh` 等 20 个文件
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/hcu_mla_backend.py`
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py` 等 332 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e5a4e379b0` - Fix Qwen2.5-VL FA3 cu_seqlens

- 完整 hash: `e5a4e379b023eaa0b475098641bcfabeec8a90c5`
- 时间/作者: 2026-07-17 / liucong8560
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen2_5_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2_5_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f38f1a5d21` - test: sync HCU registrations with current main

- 完整 hash: `f38f1a5d2113838d01fc4e51151e49d9a164a50e`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_utils.py`, `python/sglang/test/simple_eval_mmmu_vlm.py`, `python/sglang/test/test_utils.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` 等 322 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` 等 322 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `1e967ec11d` - chore: add Apache headers for DCU files

- 完整 hash: `1e967ec11d7417188930e2c7183b63ebe3e5f55a`
- 时间/作者: 2026-07-05 / Lv Jiajia
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/lightop_concat.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 118 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/profile/prof.py`; `scripts/ci/dcu/dcu_ci_cleanup_container.sh`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`; `scripts/ci/dcu/verify_dcu_registration.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`; `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`; `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/lightop_concat.py`; `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 16 个文件
  - tests: `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_local_attn.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_page_size.py`; `test/registered/core/test_score_api.py` 等 96 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `db4a263167` - test: use local DCU model paths for smoke tests

- 完整 hash: `db4a2631679173d94d8ef07bee785c40587e3401`
- 时间/作者: 2026-06-27 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`; `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`; `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `a21b0b6ef2` - test: preserve local DCU AI smoke and accuracy cases

- 完整 hash: `a21b0b6ef2e40ddb4ee4c8a97cc5e5e78cd917a4`
- 时间/作者: 2026-06-25 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`, `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`, `test/registered/dcu/core/test_deterministic_fa3_dcu.py`, `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py`, `test/registered/dcu/lora/bw1100/test_qwen3_lora_server_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/quant/test_torchao_smoke_dcu.py` 等 10 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`; `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`; `test/registered/dcu/core/test_deterministic_fa3_dcu.py`; `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py`; `test/registered/dcu/lora/bw1100/test_qwen3_lora_server_dcu.py`; `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`; `test/registered/dcu/quant/test_torchao_smoke_dcu.py` 等 10 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `c5dd815b3c` - dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6)

- 完整 hash: `c5dd815b3c631b45afa6450eb74f16fee6902428`
- 时间/作者: 2026-05-18 / lizhigong
- 自动分类: 性能/后端优化
- 主要文件: `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 133 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`; `python/pyproject.toml`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py` 等 25 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/minimax_m2.py` 等 15 个文件
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` 等 92 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_START -->
## hg-full-base 到 main 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `hg-full-base`@`92b1d382c`, `main`@`5343b311c`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 7（其中 merge 0）
- 分支更新段: `hg-full-base..main`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/distributed/parallel_state.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/environ.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/lightop_concat.py` | `c5dd815b3`, `1e967ec11`, `123e9539e` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` | `c5dd815b3`, `1e967ec11`, `123e9539e` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8.py` | `c5dd815b3`, `1e967ec11`, `123e9539e` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `c5dd815b3`, `1e967ec11`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w4a8_utils.py` | `c5dd815b3`, `1e967ec11`, `123e9539e` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/model_executor/model_runner.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_v2.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/qwen3_5.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/qwen3_vl.py` | `c5dd815b3`, `123e9539e`, `7b3548f97` |
| `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py` | `a21b0b6ef`, `db4a26316`, `1e967ec11` |
| `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py` | `a21b0b6ef`, `db4a26316`, `1e967ec11` |
| `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/multimodal_gen/runtime/layers/ring_attention.py` | `c5dd815b3`, `1e967ec11` |
| `python/sglang/multimodal_gen/runtime/layers/usp.py` | `c5dd815b3`, `7b3548f97` |
| `python/sglang/srt/batch_overlap/two_batch_overlap.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `c5dd815b3`, `7b3548f97` |
| `python/sglang/srt/layers/attention/base_attn_backend.py` | `c5dd815b3`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dcu_mla_backend.py` | `c5dd815b3`, `1e967ec11` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/fused_recurrent.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/index.py` | `c5dd815b3`, `123e9539e` |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `c5dd815b3`, `1e967ec11` |
| `python/sglang/srt/layers/attention/linear/gdn_backend.py` | `c5dd815b3`, `7b3548f97` |
| `python/sglang/srt/layers/attention/triton_backend.py` | `c5dd815b3`, `7b3548f97` |
| `python/sglang/srt/layers/attention/vision.py` | `c5dd815b3`, `7b3548f97` |
| `python/sglang/srt/layers/attention/xpu_backend.py` | `c5dd815b3`, `7b3548f97` |
| `python/sglang/srt/layers/communicator.py` | `c5dd815b3`, `123e9539e` |
| ... | 另有 270 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-05-18 | `c5dd815b3` | `hg-full-base..main` | 性能/后端优化 | dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6) | `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py` 等 141 个文件 |
| 2026-06-25 | `a21b0b6ef` | `hg-full-base..main` | 性能/后端优化 | test: preserve local DCU AI smoke and accuracy cases | `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`, `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py` 等 10 个文件 |
| 2026-06-27 | `db4a26316` | `hg-full-base..main` | 性能/后端优化 | test: use local DCU model paths for smoke tests | `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py` |
| 2026-07-05 | `1e967ec11` | `hg-full-base..main` | 性能/后端优化 | chore: add Apache headers for DCU files | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` 等 121 个文件 |
| 2026-07-17 | `e5a4e379b` | `hg-full-base..main` | 缺陷修复 | Fix Qwen2.5-VL FA3 cu_seqlens | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2026-07-31 | `123e9539e` | `hg-full-base..main` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-08-25 | `7b3548f97` | `hg-full-base..main` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` 等 48 个文件 |

### 逐 Commit 审计卡

#### Commit `c5dd815b3` - dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6)

- 完整 hash: `c5dd815b3c631b45afa6450eb74f16fee6902428`
- 时间/作者: 2026-05-18 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py` 等 141 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `README_DCU.md`; `python/pyproject.toml`; `python/sglang/bench_serving.py`; `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/executors/pipeline_executor.py`; `python/sglang/multimodal_gen/runtime/utils/profiler.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py` 等 29 个文件
  - runtime-model: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py` 等 16 个文件
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py` 等 95 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `a21b0b6ef` - test: preserve local DCU AI smoke and accuracy cases

- 完整 hash: `a21b0b6ef2e40ddb4ee4c8a97cc5e5e78cd917a4`
- 时间/作者: 2026-06-25 / LvJIA-RG
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`, `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`, `test/registered/dcu/core/test_deterministic_fa3_dcu.py`, `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py`, `test/registered/dcu/lora/bw1100/test_qwen3_lora_server_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/quant/test_torchao_smoke_dcu.py` 等 10 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`; `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py`; `test/registered/dcu/core/test_deterministic_fa3_dcu.py`; `test/registered/dcu/hicache/test_hicache_storage_file_backend_dcu.py`; `test/registered/dcu/lora/bw1100/test_qwen3_lora_server_dcu.py`; `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`; `test/registered/dcu/quant/test_torchao_smoke_dcu.py` 等 10 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `db4a26316` - test: use local DCU model paths for smoke tests

- 完整 hash: `db4a2631679173d94d8ef07bee785c40587e3401`
- 时间/作者: 2026-06-27 / DCU CI Bot
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`; `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`; `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `1e967ec11` - chore: add Apache headers for DCU files

- 完整 hash: `1e967ec11d7417188930e2c7183b63ebe3e5f55a`
- 时间/作者: 2026-07-05 / Lv Jiajia
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`, `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 121 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/profile/prof.py`; `scripts/ci/dcu/dcu_ci_cleanup_container.sh`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`; `scripts/ci/dcu/verify_dcu_registration.py`
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`; `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`; `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/lightop_concat.py` 等 18 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_local_attn.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_page_size.py` 等 97 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `e5a4e379b` - Fix Qwen2.5-VL FA3 cu_seqlens

- 完整 hash: `e5a4e379b023eaa0b475098641bcfabeec8a90c5`
- 时间/作者: 2026-07-17 / liucong8560
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen2_5_vl.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/qwen2_5_vl.py`
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

#### Commit `7b3548f97` - fix lint: apply pre-commit fixes across the 20260824 sync diff

- 完整 hash: `7b3548f97409d83b7e7dde4c3ad71e2f30955267`
- 时间/作者: 2026-08-25 / RyeYuan
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/utils.py` 等 48 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/hardware_backend/npu/utils.py`; `python/sglang/srt/sampling/sampling_batch_info.py`; `python/sglang/srt/speculative/draft_utils.py`; `python/sglang/srt/speculative/eagle_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`; `python/sglang/kernels/ops/moe/ep_moe_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 22 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_server_args.py`; `test/registered/hicache/test_hicache_storage_3fs_backend.py`; `test/registered/openai_server/validation/test_matched_stop.py`; `test/registered/pp/test_pp_single_node.py`; `test/registered/profiling/test_start_profile.py`; `test/registered/unit/entrypoints/openai/test_serving_embedding.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/unit/function_call/test_json_schema_constraint.py` 等 13 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_END -->
