# sglang Kimi K2/K2.5/Linear/VL Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `docs/cookbook/autoregressive/Moonshotai/Kimi-K2.5.mdx` | `36b93840b5` |
| `docs/cookbook/autoregressive/Moonshotai/Kimi-K2.6.mdx` | `36b93840b5`, `ee0f2375e5`, `50bacb0280` |
| `docs/cookbook/autoregressive/Moonshotai/Kimi-K2.7-Code.mdx` | `4975d6490a`, `36b93840b5`, `ab43824b09`, `50bacb0280` |
| `docs/cookbook/autoregressive/Moonshotai/Kimi-K2.mdx` | `36b93840b5`, `ab43824b09` |
| `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx` | `4975d6490a`, `36b93840b5`, `ab43824b09`, `16229e94d0`, `ca25bc4275`, `ee0f2375e5`, `50bacb0280`, `16d7caa106` |
| `docs/cookbook/autoregressive/Moonshotai/Kimi-Linear.mdx` | `ab43824b09` |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/kimi_k2_6.mdx` | `36b93840b5`, `ab43824b09`, `16229e94d0`, `ca25bc4275`, `50bacb0280` |
| `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/kimi_k2_6.mdx` | `4975d6490a`, `16229e94d0`, `ca25bc4275` |
| `docs/src/snippets/_kimi_k3_mamba_ratio_calculator.jsx` | `36b93840b5`, `ab43824b09`, `16d7caa106` |
| `docs/src/snippets/autoregressive/kimi-k2-deployment.jsx` | `36b93840b5` |
| `docs/src/snippets/autoregressive/kimi-k25-deployment.jsx` | `36b93840b5` |
| `docs/src/snippets/autoregressive/kimi-k26-deployment.jsx` | `36b93840b5` |
| `docs/src/snippets/autoregressive/kimi-k27-code-deployment.jsx` | `4975d6490a`, `36b93840b5`, `50bacb0280` |
| `docs/src/snippets/autoregressive/kimi-linear-deployment.jsx` | no direct commit |
| `docs/src/snippets/configs/moonshotai/kimi-k3-benchmarks.jsx` | `ca25bc4275`, `ee0f2375e5` |
| `docs/src/snippets/configs/moonshotai/kimi-k3.jsx` | `4975d6490a`, `36b93840b5`, `ab43824b09`, `16229e94d0`, `ca25bc4275`, `ee0f2375e5`, `16d7caa106` |
| `examples/runtime/kimi_k3/benchmark_kimi_k3_5090.py` | `50bacb0280` |
| `python/sglang/kernels/jit/csrc/kimi_k3/attn_res/fused_tma.cuh` | `50bacb0280` |
| `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh` | `756ae5b4fe`, `ca25bc4275`, `50bacb0280` |
| `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh` | `756ae5b4fe`, `50bacb0280` |
| `python/sglang/kernels/jit/csrc/kimi_k3/comm/sp_collective.cuh` | `50bacb0280` |
| `python/sglang/kernels/jit/csrc/kimi_k3/mla_output_gate.cuh` | no direct commit |
| `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh` | `756ae5b4fe`, `16229e94d0` |
| `python/sglang/kernels/jit/csrc/lora/trtllm_lora_temp/kimi_k2_moe_fused_gate.cuh` | `36b93840b5` |
| `python/sglang/kernels/ops/attention/kda_flydsl/kernels/kimi_k3_kda_decode_fb.py` | `4975d6490a`, `36b93840b5`, `ab43824b09` |
| `python/sglang/kernels/ops/attention/kda_flydsl/kimi_k3_kda_decode.py` | `4975d6490a`, `ab43824b09` |
| `python/sglang/kernels/ops/gemm/kimi_k3.py` | `ab43824b09` |
| `python/sglang/kernels/ops/lora/moe/trtllm_lora_temp/kimi_k2_moe_fused_gate.py` | `36b93840b5` |
| `python/sglang/srt/arg_groups/kimi_k3_hook.py` | `50bacb0280`, `16d7caa106` |
| `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py` | `ab43824b09`, `ca25bc4275`, `50bacb0280` |
| `python/sglang/srt/configs/kimi_k25.py` | no direct commit |
| `python/sglang/srt/configs/kimi_k3.py` | no direct commit |
| `python/sglang/srt/configs/kimi_linear.py` | `ab43824b09` |
| `python/sglang/srt/configs/kimi_vl.py` | no direct commit |
| `python/sglang/srt/configs/kimi_vl_moonvit.py` | no direct commit |
| `python/sglang/srt/function_call/kimik2_detector.py` | `ab43824b09`, `ee0f2375e5`, `50bacb0280` |
| `python/sglang/srt/function_call/kimik3_detector.py` | `16d7caa106` |
| `python/sglang/srt/function_call/kimik3_format.py` | no direct commit |
| `python/sglang/srt/function_call/kimik3_structural_tag.py` | `ee0f2375e5` |
| `python/sglang/srt/model_loader/expert_pack/kimi_ggml.py` | `50bacb0280` |
| `python/sglang/srt/model_loader/expert_pack/prepare_kimi_manifest.py` | `50bacb0280` |
| `python/sglang/srt/model_loader/expert_pack/prepare_kimi_pack.py` | `50bacb0280` |
| `python/sglang/srt/model_loader/kimi_k3_gguf.py` | `ee0f2375e5`, `50bacb0280` |
| `python/sglang/srt/models/kimi_k25.py` | `4975d6490a`, `ab43824b09`, `ee0f2375e5`, `50bacb0280` |
| `python/sglang/srt/models/kimi_k25_eagle3.py` | `36b93840b5`, `16229e94d0` |
| `python/sglang/srt/models/kimi_k3.py` | `5f67ce01c3`, `4975d6490a`, `36b93840b5`, `756ae5b4fe`, `ab43824b09`, `16229e94d0`, `ca25bc4275`, `ee0f2375e5`, `50bacb0280`, `16d7caa106` |
| `python/sglang/srt/models/kimi_k3_rocm_quant.py` | `36b93840b5` |
| `python/sglang/srt/models/kimi_k3_vl.py` | `36b93840b5` |
| `python/sglang/srt/models/kimi_linear.py` | `4975d6490a`, `36b93840b5`, `ab43824b09`, `16229e94d0`, `ee0f2375e5`, `50bacb0280`, `16d7caa106`, `ba31df0c0d` |
| `python/sglang/srt/models/kimi_vl.py` | `4975d6490a`, `ab43824b09`, `ee0f2375e5` |
| `python/sglang/srt/models/kimi_vl_moonvit.py` | `36b93840b5`, `ee0f2375e5` |
| `python/sglang/srt/multimodal/kimi_k3_image_processing.py` | no direct commit |
| `python/sglang/srt/multimodal/kimi_k3_vit_cuda_graph_runner.py` | `16d7caa106` |
| `python/sglang/srt/multimodal/media_artifacts/kimi_k3.py` | no direct commit |
| `python/sglang/srt/multimodal/processors/kimi_common.py` | `4975d6490a` |
| `python/sglang/srt/multimodal/processors/kimi_k25.py` | `4975d6490a`, `16229e94d0`, `ee0f2375e5` |
| `python/sglang/srt/multimodal/processors/kimi_k3.py` | `4975d6490a`, `ee0f2375e5` |
| `python/sglang/srt/multimodal/processors/kimi_vl.py` | `50bacb0280` |
| `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/1p1d-mtp.yaml` | `36b93840b5` |
| `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/1p1d.yaml` | no direct commit |
| `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/2p1d-ep16-mtp-mxfp4.yaml` | `4975d6490a`, `ca25bc4275` |
| `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/2p1d-ep16-mxfp4.yaml` | `4975d6490a`, `ca25bc4275` |
| `test/manual/ep/test_kimi_k3_eplb.py` | `756ae5b4fe` |
| `test/manual/hcu/test_kimi_k3_serial_sbo.py` | `5f67ce01c3` |
| `test/manual/hicache/test_npu_kimi_k3_hicache.py` | `36b93840b5`, `16229e94d0` |
| `test/manual/models/test_kimi_k2_models.py` | `ab43824b09`, `ee0f2375e5` |
| `test/registered/amd/accuracy/mi30x/test_kimi_k25_eval_amd.py` | `ab43824b09` |
| `test/registered/amd/accuracy/mi30x/test_kimi_k26_eval_amd.py` | `ab43824b09` |
| `test/registered/amd/accuracy/mi30x/test_kimi_k2_eval_amd.py` | `ab43824b09` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k25_aiter_mla_eval_mi35x.py` | `ab43824b09`, `ee0f2375e5` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k25_eval_mi35x.py` | `ab43824b09` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k25_mxfp4_eval_mi35x.py` | `ab43824b09`, `ee0f2375e5` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k26_eval_mi35x.py` | `ab43824b09` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k27_code_mxfp4_eval_mi35x.py` | `ab43824b09`, `ee0f2375e5` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k2_eval_mi35x.py` | `ab43824b09` |
| `test/registered/amd/accuracy/mi35x/test_kimi_k3_eval_mi35x.py` | `ab43824b09`, `16d7caa106` |
| `test/registered/amd/perf/mi30x/test_kimi_k26_perf_amd.py` | no direct commit |
| `test/registered/amd/perf/mi35x/test_kimi_k26_perf_mi35x.py` | no direct commit |
| `test/registered/amd/perf/mi35x/test_kimi_k3_perf_mi35x.py` | `16d7caa106` |
| `test/registered/amd/test_kimi_k25_mxfp4.py` | `ab43824b09`, `ee0f2375e5` |
| ... | 46 more files omitted from table; all were used for git tracing. |

## Local Commit Coverage Summary

- Source worktree: `HYGON-AI/sglang-das`
- Generated date: 2026-11-05
- Commits in this document: 30
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-10-21 | `5f67ce01c3` | 性能/后端优化 | Sync/rel 2 main 20261021 dsv4 validated (#576) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore` |
| 2026-10-20 | `4975d6490a` | 性能/后端优化 | Sync/official main daily 20261019 (#560) | `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md` |
| 2026-10-12 | `36b93840b5` | 性能/后端优化 | Sync/official main daily 20261009 (#500) | `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md` |
| 2026-09-30 | `756ae5b4fe` | 性能/后端优化 | Sync/20260929 rye rel 2 main (#470) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-29 | `ab43824b09` | 性能/后端优化 | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` |
| 2026-09-20 | `16229e94d0` | 性能/后端优化 | Sync/official main daily 20260920 (#410) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md` |
| 2026-09-14 | `ca25bc4275` | 性能/后端优化 | Sync/official main daily 20260914 (#362) | `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` |
| 2026-09-08 | `ee0f2375e5` | 性能/后端优化 | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` |
| 2026-09-01 | `50bacb0280` | 性能/后端优化 | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` |
| 2026-08-25 | `16d7caa106` | 性能/后端优化 | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` |
| 2026-08-07 | `2b4271498f` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-08-07 | `b7bd14f198` | 性能/后端优化 | ci(hcu): normalize HCU suite names | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` |
| 2026-08-01 | `ca730a059a` | 通用实现调整 | Merge pull request #157 from HYGON-AI/v0.5.12_dev_kimi27 |  |
| 2026-07-31 | `f7161d452e` | 通用实现调整 | Merge branch 'v0.5.12_dev' of https://github.com/HYGON-AI/sglang-das into v0.5.12_dev_kimi27 |  |
| 2026-07-29 | `ba31df0c0d` | 性能/后端优化 | Sync/official main daily 20260728 (#136) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` |
| 2026-07-24 | `b781224d4d` | 性能/后端优化 | Rename DCU integration to HCU and sanitize runtime logs | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` |
| 2026-07-22 | `aa2309e220` | 性能/后端优化 | chore(compliance): add HYGON headers and provenance | `README.md`, `THIRD_PARTY_NOTICES.md`, `python/sglang/check_env.py` |
| 2026-07-22 | `af89ecd853` | 性能/后端优化 | test: remove unstable MiMo HCU coverage and restore EAGLE | `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-07-22 | `549cacab35` | 测试/文档/基准 | ci(hcu): isolate accuracy servers and share results | `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_server_guard.py` |
| 2026-07-21 | `b4604b61fa` | 性能/后端优化 | ci(hcu): notify Feishu with accuracy results | `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_accuracy_report.py`, `python/sglang/test/hcu_cookbook_utils.py` |
| 2026-07-16 | `0769f832d5` | 测试/文档/基准 | test: tighten HCU accuracy thresholds | `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_common.py` |
| 2026-07-20 | `c43b06722a` | 性能/后端优化 | ci(hcu): port v0.5.12 wheel staging gate | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` |
| 2026-07-17 | `7c22d53e3d` | 缺陷修复 | ci(hcu): use local model assets and fix mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` |
| 2026-07-15 | `7f8f5cd28e` | 测试/文档/基准 | test: tune HCU text accuracy coverage | `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` |
| 2026-07-13 | `f38f1a5d21` | 性能/后端优化 | test: sync HCU registrations with current main | `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py` |
| 2026-07-10 | `d2480f3eb5` | 通用实现调整 | Merge pull request #85 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.7 |  |
| 2026-07-05 | `1e967ec11d` | 性能/后端优化 | chore: add Apache headers for DCU files | `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py` |
| 2026-06-29 | `6fb7d6ec37` | 通用实现调整 | Merge pull request #52 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.6-marlin |  |
| 2026-06-29 | `e23638045b` | 性能/后端优化 | 为kimi-k2.6适配marlin moe | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-06-26 | `54f44d298f` | 性能/后端优化 | test: add DCU cookbook nightly model coverage | `python/sglang/test/dcu_cookbook_utils.py`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py` |

## Per-Commit Audit Cards

### Commit `5f67ce01c3` - Sync/rel 2 main 20261021 dsv4 validated (#576)

- Full hash: `5f67ce01c3ec1894916d16627eaca4959fbe2d90`
- Date/author: 2026-10-21 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore`, `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py`, `docs/internal/rel-2-main-20261020-release-updates.md`, `python/sglang/benchmark/serving.py` 等 307 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/minimax_router_gemv.py`; `docs/internal/rel-2-main-20261020-release-updates.md`
  - other: `.gitignore`; `python/sglang/benchmark/serving.py`; `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/exec_.py`; `python/sglang/srt/arg_groups/fields/memory.py`; `python/sglang/srt/arg_groups/fields/schedule.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/arg_groups/parallel_hook.py` 等 54 个文件
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`; `python/sglang/srt/model_executor/cpu_graph_runner.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/model_runner_components/misc_utils.py` 等 23 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/activation.cu`; `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/include/utils.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh` 等 125 个文件
  - tests: `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`; `python/sglang/test/few_shot_gsm8k.py`; `python/sglang/test/kits/linker_load_failure_kit.py`; `test/manual/hcu/test_kimi_k3_serial_sbo.py`; `test/registered/attention/test_triton_attention_kernels.py`; `test/registered/attention/test_verify_shared_kv.py`; `test/registered/cp/test_cp_strategy_unit.py` 等 99 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4975d6490a` - Sync/official main daily 20261019 (#560)

- Full hash: `4975d6490ac2c71c2d88c8a86b96a6f7061050ab`
- Date/author: 2026-10-20 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md`, `.agents/skills/processor-model-parity/SKILL.md`, `.agents/skills/write-sglang-test/SKILL.md`, `.claude/rules/prefer-sgl-eval.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 2248 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/pull_request_template.md`; `.github/scripts/pr-check-comment.cjs` 等 54 个文件
  - docs-bench: `benchmark/hicache/bench_host_memory_migration.py`; `benchmark/kernels/lora_csgmv/bench_csgmv_split_k.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/cookbook/autoregressive/Cloudflare/clef.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`; `docs/cookbook/autoregressive/IFM/Jais-3.mdx` 等 155 个文件
  - other: `.agents/skills/cookbook-add-model/SKILL.md`; `.agents/skills/generate-profile/SKILL.md`; `.agents/skills/processor-model-parity/SKILL.md`; `.claude/rules/prefer-sgl-eval.md`; `.gitignore`; `README.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134` 等 336 个文件
  - runtime-model: `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/ARCHITECTURE.md`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/REFERENCE.md` 等 335 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/README.md`; `python/sglang/kernels/__init__.py`; `python/sglang/kernels/aot/benchmark/bench_dsv4_norm_rope.py`; `python/sglang/kernels/aot/benchmark/bench_flashmla_mega.py` 等 574 个文件
  - tests: `.agents/skills/write-sglang-test/SKILL.md`; `docs/scripts/tests/wan-animate-2-config.test.mjs`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_peer_bootstrap.rs`; `experimental/sgl-router/tests/component/policies_reorg.rs`; `experimental/sgl-router/tests/component/policies_reorg_admission.rs` 等 794 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `756ae5b4fe` - Sync/20260929 rye rel 2 main (#470)

- Full hash: `756ae5b4fe26cf9ad666d46cda6c45b14b3abc60`
- Date/author: 2026-09-30 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `README_HCU.md`, `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `benchmark/glm53/README.md`, `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py` 等 308 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/quality-gate.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/eplb/README.md`; `benchmark/eplb/prepare_static_lp.py`; `benchmark/glm53/README.md`; `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py`; `docs/internal/README_BF16_FLASHMLA.md`
  - other: `README_HCU.md`; `python/pyproject_hcu.toml`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`; `python/sglang/srt/arg_groups/choices.py`; `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/disagg.py` 等 61 个文件
  - runtime-model: `python/sglang/srt/configs/dspark.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/pool_configurator.py` 等 30 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/concat_mla_absorb_q_hcu.cu`; `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh` 等 158 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_aime25.py`; `python/sglang/test/simple_eval_aime26.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py`; `test/hcu_humaneval_judge.py`; `test/manual/ep/test_kimi_k3_eplb.py`; `test/manual/layers/test_hy4_ihc_tilelang.py` 等 51 个文件
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

### Commit `16229e94d0` - Sync/official main daily 20260920 (#410)

- Full hash: `16229e94d0a0a218875ab0db2133c12d9695abd1`
- Date/author: 2026-09-20 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 1391 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/amd-aiter-scout.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/bot-bump-sglang-version.yml`; `.github/workflows/ci-coverage-overview.yml` 等 26 个文件
  - docs-bench: `benchmark/agentic-rollout/README.md`; `benchmark/agentic-rollout/explore.py`; `benchmark/agentic-rollout/metrics.py`; `benchmark/agentic-rollout/plot.py`; `benchmark/agentic-rollout/simulate.py`; `benchmark/agentic-rollout/spec/README.md`; `benchmark/agentic-rollout/spec/evidence/feature-00-session-hicache-latency.md`; `benchmark/agentic-rollout/spec/feature-00-session-hicache-latency.md` 等 100 个文件
  - other: `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`; `.claude/skills/ci-test-audit/SKILL.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.gitignore`; `.gitleaksignore`; `docker/Dockerfile.cu134`; `docker/npu.Dockerfile` 等 177 个文件
  - runtime-model: `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/deny.toml`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json` 等 205 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/cpu/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/cpu/bmm.cpp` 等 417 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `benchmark/agentic-rollout/tests/test_explore.py`; `benchmark/agentic-rollout/tests/test_simulate.py`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs`; `experimental/sgl-router/tests/component/policies/kv_events_two_subscribers.rs`; `experimental/sgl-router/tests/component/policies/zmq_helpers.rs` 等 466 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ca25bc4275` - Sync/official main daily 20260914 (#362)

- Full hash: `ca25bc4275b93e02a48a2f8158835f372fee3553`
- Date/author: 2026-09-14 / YuanYuan
- Auto category: 性能/后端优化
- Main files: `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.codespellrc` 等 1457 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/workflows/_docker-build-and-publish.yml` 等 43 个文件
  - docs-bench: `benchmark/bench_linear_attention/bench_int8_checkpoint_reuse.py`; `benchmark/kernels/attention/bench_gdn_replayssm_decode.py`; `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/simulator/bench_runner.py`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx` 等 112 个文件
  - other: `.claude/rules/unit-test-admission.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-migrate-model/SKILL.md`; `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.codespellrc`; `.gitleaksignore`; `3rdparty/amd/wheel/README.md` 等 194 个文件
  - runtime-model: `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/src/policies/buckets.rs`; `experimental/sgl-router/src/policies/mod.rs`; `experimental/sgl-router/src/proxy/mod.rs`; `experimental/sgl-router/src/proxy/sse.rs`; `experimental/sgl-router/src/server/metrics.rs`; `experimental/sgl-router/src/server/routes/chat.rs`; `python/sglang/launch_server.py` 等 85 个文件
  - runtime-perf: `3rdparty/amd/wheel/sgl-kernel/build_rocm.sh`; `3rdparty/amd/wheel/sgl-kernel/rename_wheels_rocm.sh`; `docker/patches/sgl-kernel-gfx1151.sh`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/Dockerfile` 等 357 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/proxy/bucket_routing.rs`; `experimental/sgl-router/tests/proxy/chat_routing.rs`; `python/sglang/kernels/aot/tests/test_awq_dequant.py`; `python/sglang/kernels/aot/tests/test_cutlass_mla.py`; `python/sglang/kernels/aot/tests/test_flash_attn_sparse.py`; `python/sglang/kernels/aot/tests/test_fused_qk_norm_rope.py` 等 666 个文件
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

### Commit `16d7caa106` - sync(hcu): official main through 20260824 (c8e1ddc707)

- Full hash: `16d7caa1065abd2af782f3afc35c3dc4da745cde`
- Date/author: 2026-08-25 / RyeYuan
- Auto category: 性能/后端优化
- Main files: `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`, `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`, `.claude/skills/sglang-runtime-context/SKILL.md` 等 1308 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/labeler.yml`; `.github/update_ci_permission.py`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 41 个文件
  - docs-bench: `benchmark/hicache/bench_buffer_mode.py`; `docs/cookbook/autoregressive/Baidu/PaddleOCR-VL.mdx`; `docs/cookbook/autoregressive/Baidu/Unlimited-OCR.mdx`; `docs/cookbook/autoregressive/DeepReinforce/Ornith-1.0.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-4.6V.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/Google/Gemma4.mdx` 等 79 个文件
  - other: `.claude/rules/comment-style.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `3rdparty/amd/wheel/sglang/pyproject.toml`; `README.md` 等 183 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/sgl-kv-indexer/.gitignore`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml`; `experimental/sgl-router/sgl-kv-indexer/README.md` 等 190 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `python/sglang/kernel_api_logging.py`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/cpu/activation.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 271 个文件
  - tests: `experimental/sgl-router/sgl-kv-indexer/tests/common/id.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/net.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/memory_integration.rs`; `experimental/sgl-router/tests/component/policies/cache_aware_zmq.rs`; `experimental/sgl-router/tests/e2e/chat_completions/test_two_router_convergence.py`; `experimental/sgl-router/tests/e2e/infra/gateway.py` 等 544 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2b4271498f` - ci(hcu): publish nine-model accuracy results

- Full hash: `2b4271498f3d9031d0080accfa4dea9eccd10a59`
- Date/author: 2026-08-07 / LvJIA-RG
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `b7bd14f198` - ci(hcu): normalize HCU suite names

- Full hash: `b7bd14f19898fe547e644590f0096bef715f0072`
- Date/author: 2026-08-07 / LvJIA-RG
- Auto category: 性能/后端优化
- Main files: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `README_HCU.md`, `scripts/ci/hcu/hcu_ci_pd.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_deterministic.py` 等 199 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_pd.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_deterministic.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py`; `test/registered/attention/test_pack_paged_kv_to_varlen.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py` 等 194 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `ca730a059a` - Merge pull request #157 from HYGON-AI/v0.5.12_dev_kimi27

- Full hash: `ca730a059a041cb4e0b4567157eebbc19ca6cb12`
- Date/author: 2026-08-01 / lizhigong
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `f7161d452e` - Merge branch 'v0.5.12_dev' of https://github.com/HYGON-AI/sglang-das into v0.5.12_dev_kimi27

- Full hash: `f7161d452e42a2ef802576a3c0270e6813eb413a`
- Date/author: 2026-07-31 / liucong
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `ba31df0c0d` - Sync/official main daily 20260728 (#136)

- Full hash: `ba31df0c0da941467ef94a6c114a375af39b488f`
- Date/author: 2026-07-29 / RyeYuan
- Auto category: 性能/后端优化
- Main files: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-review-pr/SKILL.md`, `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md` 等 1780 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/MAINTAINER.md`; `.github/labeler.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/lint.yml`; `.github/workflows/nightly-test-amd-miles-rocm700.yml`; `.github/workflows/nightly-test-amd-miles-rocm720.yml` 等 26 个文件
  - docs-bench: `benchmark/bench_linear_attention/bench_cutedsl_kda_decode.py`; `benchmark/bench_linear_attention/bench_gdn_qkv_split.py`; `benchmark/hicache/bench_hicache_write_back.py`; `benchmark/hicache/perf.py`; `benchmark/kernels/all_reduce/benchmark_fused_ar_rms_quant_amd.py`; `benchmark/kernels/bench_fused_gate_sigmoid_mul_add.py`; `benchmark/kernels/bench_fused_sigmoid_mul.py`; `benchmark/kernels/deepseek/benchmark_cute_dsl_fp8_paged_mqa_logits.py` 等 47 个文件
  - other: `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`; `.claude/skills/cookbook-migrate-model/SKILL.md`; `.claude/skills/cookbook-review-pr/SKILL.md`; `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`; `3rdparty/amd/wheel/sglang/pyproject.toml`; `docker/Dockerfile`; `python/pyproject.toml` 等 146 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `python/sglang/srt/configs/load_config.py`; `python/sglang/srt/configs/mamba_utils.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/disaggregation/encode_server.py`; `python/sglang/srt/entrypoints/engine.py`; `python/sglang/srt/entrypoints/http_server.py` 等 69 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `python/sglang/jit_kernel/.clang-format`; `python/sglang/jit_kernel/__init__.py`; `python/sglang/jit_kernel/__main__.py`; `python/sglang/jit_kernel/activation.py`; `python/sglang/jit_kernel/add_constant.py` 等 965 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/deepseek_v4/__init__.py`; `python/sglang/jit_kernel/tests/deepseek_v4/common.py`; `python/sglang/jit_kernel/tests/kv_canary/__init__.py`; `python/sglang/jit_kernel/tests/kv_canary/_canary_helpers.py`; `python/sglang/jit_kernel/tests/kv_canary/_constants.py`; `python/sglang/jit_kernel/tests/kv_canary/_differential.py`; `python/sglang/jit_kernel/tests/kv_canary/_fixtures.py` 等 527 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b781224d4d` - Rename DCU integration to HCU and sanitize runtime logs

- Full hash: `b781224d4dae58889ba9bcc3efc0ff20fb424dc4`
- Date/author: 2026-07-24 / LvJIA-RG
- Auto category: 性能/后端优化
- Main files: `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-dcu.yml`, `.github/workflows/lint-hcu.yml` 等 464 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/open-source-compliance.json`; `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/dcu-manual-model-test.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-dcu.yml`; `.github/workflows/lint-hcu.yml` 等 14 个文件
  - docs-bench: `docs/dcu-pr-ci-visual-guide.html`; `docs/hcu-pr-ci-visual-guide.html`
  - other: `NOTICE`; `README.md`; `README_DCU.md`; `README_HCU.md`; `THIRD_PARTY_NOTICES.md`; `python/sglang/check_env.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py` 等 33 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/compress.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`; `python/sglang/kernels/ops/attention/dsa/tilelang_kernel.py` 等 76 个文件
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py` 等 325 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `aa2309e220` - chore(compliance): add HYGON headers and provenance

- Full hash: `aa2309e220d9a0df4325928ff969a214c7806e03`
- Date/author: 2026-07-22 / Lv Jiajia
- Auto category: 性能/后端优化
- Main files: `README.md`, `THIRD_PARTY_NOTICES.md`, `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh` 等 151 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README.md`; `THIRD_PARTY_NOTICES.md`; `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py` 等 22 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py` 等 24 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/add_constant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh` 等 82 个文件
  - tests: `python/sglang/test/hcu_server_guard.py`; `python/sglang/test/simple_eval_common.py`; `test/manual/ep/test_eplb.py`; `test/manual/test_expert_distribution.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py` 等 23 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `af89ecd853` - test: remove unstable MiMo HCU coverage and restore EAGLE

- Full hash: `af89ecd853eb34c8a872893720ea94cc47a8031f`
- Date/author: 2026-07-22 / LvJIA-RG
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py`, `test/registered/hcu/large_models/bw1100/test_kimi_cookbook_8gpu_server_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/speculative/multi_layer_eagle_utils.py`; `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_kimi_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_kimi_mimo_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/perf/bw1100/test_kimi_cookbook_8gpu_serving_perf_hcu.py`; `test/registered/hcu/perf/bw1100/test_kimi_mimo_cookbook_8gpu_serving_perf_hcu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `549cacab35` - ci(hcu): isolate accuracy servers and share results

- Full hash: `549cacab35632a7e0fda17a54a87791aa3ce4fcf`
- Date/author: 2026-07-22 / tianlinyang77
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_server_guard.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/hcu_ci_publish_accuracy.py`, `scripts/ci/hcu/hcu_ci_start_container.sh`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_server_guard.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/hcu_ci_publish_accuracy.py`; `scripts/ci/hcu/hcu_ci_start_container.sh`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - runtime-model: `scripts/ci/hcu/test_hcu_server_guard.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_server_guard.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b4604b61fa` - ci(hcu): notify Feishu with accuracy results

- Full hash: `b4604b61fae504fa0ece17ca7dd1937af33c38e6`
- Date/author: 2026-07-21 / tianlinyang77
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_accuracy_report.py`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `python/sglang/test/hcu_accuracy_report.py`; `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py` 等 10 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `0769f832d5` - test: tighten HCU accuracy thresholds

- Full hash: `0769f832d57dc395a330d6fe0fd73fc87b009ed1`
- Date/author: 2026-07-16 / dddddddxl
- Auto category: 测试/文档/基准
- Main files: `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_common.py`, `python/sglang/test/simple_eval_mmlu.py`, `python/sglang/test/simple_eval_mmmu_vlm.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `c43b06722a` - ci(hcu): port v0.5.12 wheel staging gate

- Full hash: `c43b06722a405fe04e5b38bdc332250b9816e349`
- Date/author: 2026-07-20 / tianlinyang77
- Auto category: 性能/后端优化
- Main files: `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-dcu.yml`, `.github/workflows/lint-hcu.yml` 等 372 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/open-source-compliance.json`; `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/dcu-manual-model-test.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-dcu.yml`; `.github/workflows/lint-hcu.yml` 等 18 个文件
  - other: `README.md`; `README_HCU.md`; `requirements_dcu.txt`; `requirements_hcu.txt`; `scripts/ci/dcu/check_hcu_runtime_text.py`; `scripts/ci/dcu/dcu_ci_cleanup_container.sh`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh` 等 20 个文件
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/hcu_mla_backend.py`
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `scripts/ci/dcu/tests/test_check_hcu_runtime_text.py` 等 332 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7c22d53e3d` - ci(hcu): use local model assets and fix mounts

- Full hash: `7c22d53e3db82a121fb92b3336ea817f83942021`
- Date/author: 2026-07-17 / DCU CI Bot
- Auto category: 缺陷修复
- Main files: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/nightly-test-hcu.yml`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm51_int8_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm5_cookbook_8gpu_server_hcu.py` 等 11 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `7f8f5cd28e` - test: tune HCU text accuracy coverage

- Full hash: `7f8f5cd28ee90a038e1268a4147504ece5e81cc9`
- Date/author: 2026-07-15 / dddddddxl
- Auto category: 测试/文档/基准
- Main files: `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `f38f1a5d21` - test: sync HCU registrations with current main

- Full hash: `f38f1a5d2113838d01fc4e51151e49d9a164a50e`
- Date/author: 2026-07-13 / DCU CI Bot
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_utils.py`, `python/sglang/test/simple_eval_mmmu_vlm.py`, `python/sglang/test/test_utils.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` 等 322 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` 等 322 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `d2480f3eb5` - Merge pull request #85 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.7

- Full hash: `d2480f3eb50a2f5d63c7a25bb9db2c7057c0cb64`
- Date/author: 2026-07-10 / lizhigong
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `1e967ec11d` - chore: add Apache headers for DCU files

- Full hash: `1e967ec11d7417188930e2c7183b63ebe3e5f55a`
- Date/author: 2026-07-05 / Lv Jiajia
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/lightop_concat.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 118 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/profile/prof.py`; `scripts/ci/dcu/dcu_ci_cleanup_container.sh`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`; `scripts/ci/dcu/verify_dcu_registration.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`; `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`; `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/lightop_concat.py`; `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` 等 16 个文件
  - tests: `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_local_attn.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_page_size.py`; `test/registered/core/test_score_api.py` 等 96 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6fb7d6ec37` - Merge pull request #52 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.6-marlin

- Full hash: `6fb7d6ec37bd5c86304d99fdb9a0478054186480`
- Date/author: 2026-06-29 / lizhigong
- Auto category: 通用实现调整
- Main files: 未记录文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - 未记录文件
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `e23638045b` - 为kimi-k2.6适配marlin moe

- Full hash: `e23638045bc3c4956b0eac7594230766882e572d`
- Date/author: 2026-06-29 / wufan3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/model_loader/weight_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/model_loader/weight_utils.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `54f44d298f` - test: add DCU cookbook nightly model coverage

- Full hash: `54f44d298fa4b21c3907e2d585e383b3bc02201d`
- Date/author: 2026-06-26 / DCU CI Bot
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/dcu_cookbook_utils.py`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_gsm8k_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`, `test/registered/dcu/large_models/bw1100/test_deepseek_v32_cookbook_8gpu_server_dcu.py` 等 24 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `scripts/ci/dcu/dcu_ci_start_container.sh`
  - tests: `python/sglang/test/dcu_cookbook_utils.py`; `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_gsm8k_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`; `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`; `test/registered/dcu/large_models/bw1100/test_deepseek_v32_cookbook_8gpu_server_dcu.py`; `test/registered/dcu/large_models/bw1100/test_glm51_cookbook_8gpu_server_dcu.py` 等 23 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_START -->
## Local-only branch update from hg-full-base to main

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `hg-full-base`@`92b1d382c`, `main`@`5343b311c`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-05
- Commits in this section: 14 (merges: 4)
- Branch segments: `hg-full-base..main`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/test/hcu_cookbook_utils.py` | `7f8f5cd28`, `0769f832d`, `7c22d53e3`, `b4604b61f`, `549cacab3`, `af89ecd85` |
| `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` | `7f8f5cd28`, `0769f832d`, `7c22d53e3`, `b4604b61f`, `549cacab3`, `2b4271498` |
| `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py` | `0769f832d`, `7c22d53e3`, `b4604b61f`, `549cacab3`, `2b4271498` |
| `.github/workflows/nightly-test-hcu.yml` | `7c22d53e3`, `b4604b61f`, `549cacab3`, `2b4271498` |
| `scripts/ci/hcu/hcu_ci_notify_feishu.py` | `b4604b61f`, `549cacab3`, `af89ecd85`, `2b4271498` |
| `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` | `b4604b61f`, `549cacab3`, `af89ecd85`, `2b4271498` |
| `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py` | `0769f832d`, `7c22d53e3`, `549cacab3`, `2b4271498` |
| `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py` | `7f8f5cd28`, `b4604b61f`, `2b4271498` |
| `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py` | `7c22d53e3`, `b4604b61f`, `2b4271498` |
| `python/sglang/test/dcu_cookbook_utils.py` | `54f44d298`, `1e967ec11` |
| `scripts/ci/dcu/dcu_ci_start_container.sh` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/accuracy/bw1100/test_gsm8k_eval_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/large_models/bw1100/test_deepseek_v32_cookbook_8gpu_server_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/large_models/bw1100/test_glm51_cookbook_8gpu_server_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/large_models/bw1100/test_kimi_mimo_cookbook_8gpu_server_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/large_models/bw1100/test_minimax_m25_cookbook_8gpu_server_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/large_models/bw1100/test_qwen3_cookbook_4gpu_server_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/perf/bw1100/test_deepseek_v32_cookbook_8gpu_serving_perf_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/perf/bw1100/test_glm51_cookbook_8gpu_serving_perf_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/perf/bw1100/test_kimi_mimo_cookbook_8gpu_serving_perf_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/perf/bw1100/test_minimax_m25_cookbook_8gpu_serving_perf_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/perf/bw1100/test_qwen3_cookbook_4gpu_serving_perf_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/quant_opt/bw1100/test_deepseek_v32_cookbook_quant_opt_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/quant_opt/bw1100/test_minimax_m25_cookbook_quant_opt_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/quant_opt/bw1100/test_qwen3_w8a8_cookbook_opt_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/quant_opt/bw1100/test_vlm_cookbook_quant_opt_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/vlm/bw1100/test_cookbook_mmmu_eval_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/dcu/vlm/bw1100/test_cookbook_vlm_server_dcu.py` | `54f44d298`, `1e967ec11` |
| `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py` | `b4604b61f`, `2b4271498` |
| `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py` | `b4604b61f`, `af89ecd85` |
| `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py` | `b4604b61f`, `2b4271498` |
| `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py` | `b4604b61f`, `2b4271498` |
| `.github/workflows/hcu-full-enabled.yml` | `7c22d53e3` |
| `.github/workflows/hcu-manual-model-test.yml` | `7c22d53e3` |
| `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py` | `1e967ec11` |
| `python/sglang/multimodal_gen/runtime/layers/ring_attention.py` | `1e967ec11` |
| ... | 123 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-06-26 | `54f44d298` | `hg-full-base..main` | 性能/后端优化 | test: add DCU cookbook nightly model coverage | `python/sglang/test/dcu_cookbook_utils.py`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py` and 24 files in total |
| 2026-06-29 | `e23638045` | `hg-full-base..main` | 性能/后端优化 | 为kimi-k2.6适配marlin moe | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-06-29 | `6fb7d6ec3` | `hg-full-base..main` | 通用实现调整 | Merge pull request #52 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.6-marlin | no direct file change / merge |
| 2026-07-05 | `1e967ec11` | `hg-full-base..main` | 性能/后端优化 | chore: add Apache headers for DCU files | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` and 121 files in total |
| 2026-07-10 | `d2480f3eb` | `hg-full-base..main` | 通用实现调整 | Merge pull request #85 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.7 | no direct file change / merge |
| 2026-07-15 | `7f8f5cd28` | `hg-full-base..main` | 测试/文档/基准 | test: tune HCU text accuracy coverage | `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` |
| 2026-07-16 | `0769f832d` | `hg-full-base..main` | 测试/文档/基准 | test: tighten HCU accuracy thresholds | `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_common.py` and 11 files in total |
| 2026-07-17 | `7c22d53e3` | `hg-full-base..main` | 缺陷修复 | ci(hcu): use local model assets and fix mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` and 14 files in total |
| 2026-07-21 | `b4604b61f` | `hg-full-base..main` | 性能/后端优化 | ci(hcu): notify Feishu with accuracy results | `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_accuracy_report.py`, `python/sglang/test/hcu_cookbook_utils.py` and 13 files in total |
| 2026-07-22 | `549cacab3` | `hg-full-base..main` | 测试/文档/基准 | ci(hcu): isolate accuracy servers and share results | `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_server_guard.py` and 11 files in total |
| 2026-07-22 | `af89ecd85` | `hg-full-base..main` | 性能/后端优化 | test: remove unstable MiMo HCU coverage and restore EAGLE | `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` and 11 files in total |
| 2026-07-31 | `f7161d452` | `hg-full-base..main` | 通用实现调整 | Merge branch 'v0.5.12_dev' of https://github.com/HYGON-AI/sglang-das into v0.5.12_dev_kimi27 | no direct file change / merge |
| 2026-08-01 | `ca730a059` | `hg-full-base..main` | 通用实现调整 | Merge pull request #157 from HYGON-AI/v0.5.12_dev_kimi27 | no direct file change / merge |
| 2026-08-07 | `2b4271498` | `hg-full-base..main` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` and 11 files in total |

### Per-Commit Audit Cards

#### Commit `54f44d298` - test: add DCU cookbook nightly model coverage

- Full hash: `54f44d298fa4b21c3907e2d585e383b3bc02201d`
- Date/author: 2026-06-26 / DCU CI Bot
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `python/sglang/test/dcu_cookbook_utils.py`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_gsm8k_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`, `test/registered/dcu/large_models/bw1100/test_deepseek_v32_cookbook_8gpu_server_dcu.py` 等 24 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `scripts/ci/dcu/dcu_ci_start_container.sh`
  - tests: `python/sglang/test/dcu_cookbook_utils.py`; `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_gsm8k_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`; `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`; `test/registered/dcu/large_models/bw1100/test_deepseek_v32_cookbook_8gpu_server_dcu.py`; `test/registered/dcu/large_models/bw1100/test_glm51_cookbook_8gpu_server_dcu.py` 等 23 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `e23638045` - 为kimi-k2.6适配marlin moe

- Full hash: `e23638045bc3c4956b0eac7594230766882e572d`
- Date/author: 2026-06-29 / wufan3
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/model_loader/weight_utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/model_loader/weight_utils.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `6fb7d6ec3` - Merge pull request #52 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.6-marlin

- Full hash: `6fb7d6ec37bd5c86304d99fdb9a0478054186480`
- Date/author: 2026-06-29 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `1e967ec11` - chore: add Apache headers for DCU files

- Full hash: `1e967ec11d7417188930e2c7183b63ebe3e5f55a`
- Date/author: 2026-07-05 / Lv Jiajia
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`, `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 121 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/profile/prof.py`; `scripts/ci/dcu/dcu_ci_cleanup_container.sh`; `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_install_dependency.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`; `scripts/ci/dcu/verify_dcu_registration.py`
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`; `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`; `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/lightop_concat.py` 等 18 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_local_attn.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_page_size.py` 等 97 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `d2480f3eb` - Merge pull request #85 from HYGON-AI/v0.5.12_dev_wufan_kimi-k2.7

- Full hash: `d2480f3eb50a2f5d63c7a25bb9db2c7057c0cb64`
- Date/author: 2026-07-10 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `7f8f5cd28` - test: tune HCU text accuracy coverage

- Full hash: `7f8f5cd28ee90a038e1268a4147504ece5e81cc9`
- Date/author: 2026-07-15 / dddddddxl
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `0769f832d` - test: tighten HCU accuracy thresholds

- Full hash: `0769f832d57dc395a330d6fe0fd73fc87b009ed1`
- Date/author: 2026-07-16 / dddddddxl
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_common.py`, `python/sglang/test/simple_eval_mmlu.py`, `python/sglang/test/simple_eval_mmmu_vlm.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `7c22d53e3` - ci(hcu): use local model assets and fix mounts

- Full hash: `7c22d53e3db82a121fb92b3336ea817f83942021`
- Date/author: 2026-07-17 / DCU CI Bot
- Branch update: `hg-full-base..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 14 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/nightly-test-hcu.yml`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm51_int8_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm5_cookbook_8gpu_server_hcu.py` 等 11 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `b4604b61f` - ci(hcu): notify Feishu with accuracy results

- Full hash: `b4604b61fae504fa0ece17ca7dd1937af33c38e6`
- Date/author: 2026-07-21 / tianlinyang77
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_accuracy_report.py`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py` 等 13 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `python/sglang/test/hcu_accuracy_report.py`; `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py` 等 10 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `549cacab3` - ci(hcu): isolate accuracy servers and share results

- Full hash: `549cacab35632a7e0fda17a54a87791aa3ce4fcf`
- Date/author: 2026-07-22 / tianlinyang77
- Branch update: `hg-full-base..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_server_guard.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/hcu_ci_publish_accuracy.py`, `scripts/ci/hcu/hcu_ci_start_container.sh`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_server_guard.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/hcu_ci_publish_accuracy.py`; `scripts/ci/hcu/hcu_ci_start_container.sh`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - runtime-model: `scripts/ci/hcu/test_hcu_server_guard.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_server_guard.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `af89ecd85` - test: remove unstable MiMo HCU coverage and restore EAGLE

- Full hash: `af89ecd853eb34c8a872893720ea94cc47a8031f`
- Date/author: 2026-07-22 / LvJIA-RG
- Branch update: `hg-full-base..main`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py`, `test/registered/hcu/large_models/bw1100/test_kimi_cookbook_8gpu_server_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/speculative/multi_layer_eagle_utils.py`; `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_kimi_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_kimi_mimo_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/perf/bw1100/test_kimi_cookbook_8gpu_serving_perf_hcu.py`; `test/registered/hcu/perf/bw1100/test_kimi_mimo_cookbook_8gpu_serving_perf_hcu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f7161d452` - Merge branch 'v0.5.12_dev' of https://github.com/HYGON-AI/sglang-das into v0.5.12_dev_kimi27

- Full hash: `f7161d452e42a2ef802576a3c0270e6813eb413a`
- Date/author: 2026-07-31 / liucong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `ca730a059` - Merge pull request #157 from HYGON-AI/v0.5.12_dev_kimi27

- Full hash: `ca730a059a041cb4e0b4567157eebbc19ca6cb12`
- Date/author: 2026-08-01 / lizhigong
- Branch update: `hg-full-base..main`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `2b4271498` - ci(hcu): publish nine-model accuracy results

- Full hash: `2b4271498f3d9031d0080accfa4dea9eccd10a59`
- Date/author: 2026-08-07 / LvJIA-RG
- Branch update: `hg-full-base..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_END -->
