# sglang Qwen3 Coder 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `docs/cookbook/autoregressive/Qwen/Qwen3-Coder-Next.mdx` | `ab43824b09` |
| `docs/cookbook/autoregressive/Qwen/Qwen3-Coder.mdx` | `36b93840b5`, `ab43824b09` |
| `docs/src/snippets/autoregressive/qwen3-coder-480b-a35b-deployment.jsx` | 无直接提交 |
| `docs/src/snippets/autoregressive/qwen3-coder-deployment.jsx` | `36b93840b5` |
| `docs/src/snippets/autoregressive/qwen3-coder-next-deployment.jsx` | 无直接提交 |
| `python/sglang/srt/function_call/qwen3_coder_detector.py` | `50bacb0280`, `ba31df0c0d` |
| `python/sglang/srt/models/qwen3.py` | `4975d6490a`, `36b93840b5`, `ab43824b09`, `16229e94d0`, `b97d7df6ee`, `123e9539ea`, `38c750157f`, `b781224d4d`, `73c7e6c8f5`, `1e2fec228a`, `4fb3f09391`, `2d561a3ec2`, ... (13 total) |
| `test/registered/amd/accuracy/mi35x/test_qwen3_coder_next_eval_mi35x.py` | `ee0f2375e5` |
| `test/registered/amd/test_qwen3_coder_next_8gpu.py` | `ab43824b09`, `ee0f2375e5` |
| `test/registered/cpu/test_qwen3.py` | `ee0f2375e5`, `16d7caa106` |
| `test/registered/lora/test_lora_qwen3.py` | `b781224d4d`, `aa2309e220`, `c43b06722a`, `f38f1a5d21`, `4d9dc66182`, `cc279bcf67`, `f08ff0baba`, `90205d601e` |
| `test/registered/npu/llm_models/test_npu_qwen3_coder_480b_a35b.py` | `16d7caa106` |

## 本地提交覆盖总览

- 来源工作树: `HYGON-AI/sglang-das`
- 生成日期: 2026-11-05
- 文档提交数: 66
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-21 | `5f67ce01c3` | 性能/后端优化 | Sync/rel 2 main 20261021 dsv4 validated (#576) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore` |
| 2026-10-20 | `4975d6490a` | 性能/后端优化 | Sync/official main daily 20261019 (#560) | `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md` |
| 2026-10-12 | `36b93840b5` | 性能/后端优化 | Sync/official main daily 20261009 (#500) | `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md` |
| 2026-09-30 | `756ae5b4fe` | 性能/后端优化 | Sync/20260929 rye rel 2 main (#470) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-29 | `ab43824b09` | 性能/后端优化 | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` |
| 2026-09-23 | `9cd15042af` | 模型支持/运行时入口 | feat(citest): 更新镜像测试用例, 适配 0.5.18 (Qwen3.8 / DeepSeek-V4) (#433) | `docker/image-citest-conf-hcu.yaml` |
| 2026-09-20 | `16229e94d0` | 性能/后端优化 | Sync/official main daily 20260920 (#410) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md` |
| 2026-09-14 | `ca25bc4275` | 性能/后端优化 | Sync/official main daily 20260914 (#362) | `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` |
| 2026-09-08 | `ee0f2375e5` | 性能/后端优化 | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` |
| 2026-09-01 | `50bacb0280` | 性能/后端优化 | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` |
| 2026-08-25 | `7b3548f974` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` |
| 2026-08-25 | `16d7caa106` | 性能/后端优化 | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` |
| 2026-08-20 | `9ca1b25f7f` | 通用实现调整 | Merge pull request #210 from HYGON-AI/main_dev_qwen3.8 |  |
| 2026-08-18 | `b0dc28040e` | 性能/后端优化 | Hcu/fix main kernel build path (#207) | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` |
| 2026-08-07 | `b86a8dc74f` | 调度/缓存/PD | test(hcu): bound backend smoke test setup | `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py` |
| 2026-08-07 | `2b4271498f` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` |
| 2026-08-07 | `b7bd14f198` | 性能/后端优化 | ci(hcu): normalize HCU suite names | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` |
| 2026-08-06 | `5d0386fd4c` | 性能/后端优化 | ci(hcu): expand functional and numerical coverage | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py` |
| 2026-08-06 | `e473881969` | 性能/后端优化 | ci: migrate legacy CUDA suite= registrations to stage=/runner_config= | `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_local_attn.py` |
| 2026-08-06 | `799aaa455b` | 通用实现调整 | Merge pull request #168 from HYGON-AI/v0.5.12_dev_qwen3.5_eplb |  |
| 2026-08-03 | `b97d7df6ee` | 性能/后端优化 | Forward port/v0.5.12 dev daily 20260729 (#146) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml` |
| 2026-07-31 | `f6603bbe5b` | 性能/后端优化 | [fix] Fixed accuracy issue caused by aiter‑moe in Qwen3.6‑35B‑A3B‑W8A8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-07-31 | `123e9539ea` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` |
| 2026-07-29 | `956b155384` | 通用实现调整 | Merge pull request #145 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b |  |
| 2026-07-29 | `25ffedc227` | 性能/后端优化 | fix(hcu): repair forward-port compatibility gaps | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` |
| 2026-07-29 | `ba31df0c0d` | 性能/后端优化 | Sync/official main daily 20260728 (#136) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` |
| 2026-07-28 | `b5a1e87297` | 通用实现调整 | Merge pull request #133 from HYGON-AI/v0.5.12_dev_qwen3_coder |  |
| 2026-07-28 | `0e24597391` | 性能/后端优化 | fix: pass quant_config to Qwen3Moe gate router, fix qwen3-coder accuracy issue | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-07-27 | `38c750157f` | 性能/后端优化 | fix：修复接口改动. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` |
| 2026-07-24 | `b781224d4d` | 性能/后端优化 | Rename DCU integration to HCU and sanitize runtime logs | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` |
| 2026-07-23 | `540368a7d3` | 通用实现调整 | Merge pull request #123 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b |  |
| 2026-07-22 | `aa2309e220` | 性能/后端优化 | chore(compliance): add HYGON headers and provenance | `README.md`, `THIRD_PARTY_NOTICES.md`, `python/sglang/check_env.py` |
| 2026-07-22 | `73c7e6c8f5` | 性能/后端优化 | [feat]:迁移lightop调用方式到新的接口. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` |
| 2026-07-22 | `6e5326678d` | 缺陷修复 | fix(dcu): use runtime server args in Qwen3.5 paths | `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-21 | `b4604b61fa` | 性能/后端优化 | ci(hcu): notify Feishu with accuracy results | `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_accuracy_report.py`, `python/sglang/test/hcu_cookbook_utils.py` |
| 2026-07-21 | `9b86479ac4` | 模型支持/运行时入口 | test(hcu): add MATH-500 and HumanEval nightly coverage | `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md` |
| 2026-07-21 | `5dd9ba2f2c` | 通用实现调整 | Merge pull request #108 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b |  |
| 2026-07-20 | `248bfe3471` | 通用实现调整 | Merge pull request #106 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b |  |
| 2026-07-20 | `1e2fec228a` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` |
| 2026-07-20 | `c43b06722a` | 性能/后端优化 | ci(hcu): port v0.5.12 wheel staging gate | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` |
| 2026-07-17 | `7c22d53e3d` | 缺陷修复 | ci(hcu): use local model assets and fix mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` |
| 2026-07-17 | `592b9a4e56` | 性能/后端优化 | test: add HCU coverage for GLM-5 MiMo and Qwen3.5 | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py` |
| 2026-07-14 | `88f43c7e14` | 模型支持/运行时入口 | test: add Qwen3.6 HCU smoke and accuracy coverage | `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/large_models/bw1100/test_qwen36_cookbook_2gpu_server_hcu.py` |
| 2026-07-13 | `1c70e76d5e` | 性能/后端优化 | test: use verified local HCU model paths | `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py`, `test/registered/hcu/lora/bw1100/test_qwen3_lora_server_hcu.py`, `test/registered/hcu/moe/bw1100/test_qwen3_30b_moe_instruct_hcu.py` |
| 2026-07-13 | `bb9bb4b2dd` | 性能/后端优化 | ci: rename HCU PR stage suites | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `docs/hcu-pr-ci-visual-guide.html` |
| 2026-07-13 | `4fb3f09391` | 性能/后端优化 | runtime: migrate current main DCU interfaces to HCU | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py` |
| 2026-07-13 | `f38f1a5d21` | 性能/后端优化 | test: sync HCU registrations with current main | `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py` |
| 2026-07-10 | `0334ae99b9` | 缺陷修复 | Merge pull request #86 from HYGON-AI/v0.5.12_dev_fix_qwen3.5_397b |  |
| 2026-07-09 | `dd0492dbf4` | 调度/缓存/PD | [PD]解决qwen3.5-397b在pd分离场景下的精度问题 | `python/sglang/srt/disaggregation/common/conn.py` |
| 2026-07-05 | `2d561a3ec2` | 性能/后端优化 | chore: add modification notices for DCU changes | `NOTICE`, `THIRD_PARTY_NOTICES.md`, `python/sglang/jit_kernel/deepseek_v4.py` |
| 2026-07-05 | `1e967ec11d` | 性能/后端优化 | chore: add Apache headers for DCU files | `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/debug_flash_mla_adapter.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py` |
| 2026-07-01 | `1a4b4404eb` | 缺陷修复 | 修复qwen3.5-397b PD分离不支持的问题 | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-06-29 | `75e928284a` | 性能/后端优化 | Register DCU tests in categorized nightly suites | `test/registered/constrained_decoding/test_constrained_decoding.py`, `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/embedding/bw1100/test_gte_qwen2_embedding_dcu.py` |
| 2026-06-27 | `db4a263167` | 性能/后端优化 | test: use local DCU model paths for smoke tests | `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py` |
| 2026-06-26 | `54f44d298f` | 性能/后端优化 | test: add DCU cookbook nightly model coverage | `python/sglang/test/dcu_cookbook_utils.py`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py` |
| 2026-06-25 | `a21b0b6ef2` | 性能/后端优化 | test: preserve local DCU AI smoke and accuracy cases | `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmmu_eval_dcu.py`, `test/registered/dcu/backends/test_torch_compile_smoke_dcu.py` |
| 2026-06-23 | `51abf3148c` | 模型支持/运行时入口 | test: add DCU AI smoke cases to PR required | `.github/workflows/pr-test-dcu.yml`, `test/registered/dcu/openai_server/test_function_calling_dcu.py`, `test/registered/dcu/openai_server/test_hidden_states_base_dcu.py` |
| 2026-06-16 | `e49d0d2fbb` | 缺陷修复 | [bugfix]修复sglang0.5.12官方bug,解决因此引起的Qwen3-30B-A3B-Instruct-2507精度问题 | `python/sglang/srt/models/utils.py` |
| 2026-06-12 | `5a231f0b59` | 模型支持/运行时入口 | test: add DCU disabled smoke candidates | `test/registered/dcu/4-gpu-models/test_qwen3_next_80b_server_dcu.py`, `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/core/test_score_api_dcu.py` |
| 2026-06-11 | `4d9dc66182` | 性能/后端优化 | ci: reduce DCU CI mainline intrusion | `.github/workflows/pr-gate.yml`, `.github/workflows/release-whl-dcu.yml`, `python/sglang/__init__.py` |
| 2026-06-05 | `cc279bcf67` | 性能/后端优化 | ci: rename DCU BW1000 tests to BW1100 | `.github/workflows/pr-test-dcu.yml`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py` |
| 2026-06-05 | `f08ff0baba` | 性能/后端优化 | ci: disable failed DCU full-enabled tests | `.github/workflows/pr-test-dcu.yml`, `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/attention/test_triton_attention_backend.py` |
| 2026-06-04 | `f57339642b` | 性能/后端优化 | ci: keep DCU test defaults official-friendly | `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh` |
| 2026-05-26 | `f8dc6e03e4` | 性能/后端优化 | 支持Qwen3.5-397b-channel-fp8 EP8并行方案 | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-05-29 | `90205d601e` | 性能/后端优化 | test: sync validated DCU registered cases | `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py` |
| 2026-05-18 | `c5dd815b3c` | 性能/后端优化 | dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6) | `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py` |

## 逐 Commit 审计卡

### Commit `5f67ce01c3` - Sync/rel 2 main 20261021 dsv4 validated (#576)

- 完整 hash: `5f67ce01c3ec1894916d16627eaca4959fbe2d90`
- 时间/作者: 2026-10-21 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore`, `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py`, `docs/internal/rel-2-main-20261020-release-updates.md`, `python/sglang/benchmark/serving.py` 等 307 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/minimax_router_gemv.py`; `docs/internal/rel-2-main-20261020-release-updates.md`
  - other: `.gitignore`; `python/sglang/benchmark/serving.py`; `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/exec_.py`; `python/sglang/srt/arg_groups/fields/memory.py`; `python/sglang/srt/arg_groups/fields/schedule.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/arg_groups/parallel_hook.py` 等 54 个文件
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`; `python/sglang/srt/model_executor/cpu_graph_runner.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/model_runner_components/misc_utils.py` 等 23 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/activation.cu`; `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/include/utils.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh` 等 125 个文件
  - tests: `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`; `python/sglang/test/few_shot_gsm8k.py`; `python/sglang/test/kits/linker_load_failure_kit.py`; `test/manual/hcu/test_kimi_k3_serial_sbo.py`; `test/registered/attention/test_triton_attention_kernels.py`; `test/registered/attention/test_verify_shared_kv.py`; `test/registered/cp/test_cp_strategy_unit.py` 等 99 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `756ae5b4fe` - Sync/20260929 rye rel 2 main (#470)

- 完整 hash: `756ae5b4fe26cf9ad666d46cda6c45b14b3abc60`
- 时间/作者: 2026-09-30 / YuanYuan
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `README_HCU.md`, `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `benchmark/glm53/README.md`, `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py` 等 308 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/quality-gate.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/eplb/README.md`; `benchmark/eplb/prepare_static_lp.py`; `benchmark/glm53/README.md`; `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py`; `docs/internal/README_BF16_FLASHMLA.md`
  - other: `README_HCU.md`; `python/pyproject_hcu.toml`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`; `python/sglang/srt/arg_groups/choices.py`; `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/disagg.py` 等 61 个文件
  - runtime-model: `python/sglang/srt/configs/dspark.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/pool_configurator.py` 等 30 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/concat_mla_absorb_q_hcu.cu`; `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh` 等 158 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_aime25.py`; `python/sglang/test/simple_eval_aime26.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py`; `test/hcu_humaneval_judge.py`; `test/manual/ep/test_kimi_k3_eplb.py`; `test/manual/layers/test_hy4_ihc_tilelang.py` 等 51 个文件
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

### Commit `9cd15042af` - feat(citest): 更新镜像测试用例, 适配 0.5.18 (Qwen3.8 / DeepSeek-V4) (#433)

- 完整 hash: `9cd15042af60905ef088d409908e41e330fbf345`
- 时间/作者: 2026-09-23 / Crowder13
- 自动分类: 模型支持/运行时入口
- 主要文件: `docker/image-citest-conf-hcu.yaml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `docker/image-citest-conf-hcu.yaml`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `9ca1b25f7f` - Merge pull request #210 from HYGON-AI/main_dev_qwen3.8

- 完整 hash: `9ca1b25f7f912a086d4a5c6a4706a3b373eae0be`
- 时间/作者: 2026-08-20 / lizhigong
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b0dc28040e` - Hcu/fix main kernel build path (#207)

- 完整 hash: `b0dc28040e611a27ea29979496c301395e3c10ed`
- 时间/作者: 2026-08-18 / dingxinlong
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh`, `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_build_shared_wheels.sh`
  - tests: `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py`; `test/registered/hcu/reranker/bw1100/test_qwen3_reranker_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `b86a8dc74f` - test(hcu): bound backend smoke test setup

- 完整 hash: `b86a8dc74ff9d3a2f535122c85966923e04f5037`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 调度/缓存/PD
- 主要文件: `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `2b4271498f` - ci(hcu): publish nine-model accuracy results

- 完整 hash: `2b4271498f3d9031d0080accfa4dea9eccd10a59`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `b7bd14f198` - ci(hcu): normalize HCU suite names

- 完整 hash: `b7bd14f19898fe547e644590f0096bef715f0072`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `README_HCU.md`, `scripts/ci/hcu/hcu_ci_pd.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_deterministic.py` 等 199 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_pd.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_deterministic.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py`; `test/registered/attention/test_pack_paged_kv_to_varlen.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py` 等 194 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `5d0386fd4c` - ci(hcu): expand functional and numerical coverage

- 完整 hash: `5d0386fd4cfda35ce75a6519dd6008fac8d2dcc9`
- 时间/作者: 2026-08-06 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`, `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py`, `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py`, `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`, `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py` 等 16 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - tests: `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`; `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py`; `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py`; `test/registered/hcu/infra/test_hcu_server_guard_failures_hcu.py`; `test/registered/hcu/kernels/test_attention_reference_hcu.py` 等 14 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `e473881969` - ci: migrate legacy CUDA suite= registrations to stage=/runner_config=

- 完整 hash: `e473881969aef386533c0fb29ce8fd036a733560`
- 时间/作者: 2026-08-06 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_local_attn.py`, `test/registered/core/test_gpt_oss_1gpu.py`, `test/registered/core/test_page_size.py`, `test/registered/core/test_score_api.py`, `test/registered/disaggregation/test_dp_attention_large.py`, `test/registered/embedding/test_embedding_models.py` 等 44 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_local_attn.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_page_size.py`; `test/registered/core/test_score_api.py`; `test/registered/disaggregation/test_dp_attention_large.py`; `test/registered/embedding/test_embedding_models.py` 等 44 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `799aaa455b` - Merge pull request #168 from HYGON-AI/v0.5.12_dev_qwen3.5_eplb

- 完整 hash: `799aaa455bca9002d7bbde91967039854ef2a8b9`
- 时间/作者: 2026-08-06 / lizhigong
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `f6603bbe5b` - [fix] Fixed accuracy issue caused by aiter‑moe in Qwen3.6‑35B‑A3B‑W8A8

- 完整 hash: `f6603bbe5b71b96153bcab4d3e9e3ec345dd5ae5`
- 时间/作者: 2026-07-31 / chenyuege
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
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

### Commit `956b155384` - Merge pull request #145 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `956b155384fa2b369a673c5985acbce08dd2b55e`
- 时间/作者: 2026-07-29 / lizhigong
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `25ffedc227` - fix(hcu): repair forward-port compatibility gaps

- 完整 hash: `25ffedc2276699992e11eec0bddc867a8862663b`
- 时间/作者: 2026-07-29 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/w8a8_fp8.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/internal/dcu-main-conflict-ledger.md`
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/layers/quantization/w8a8_fp8.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` 等 9 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ba31df0c0d` - Sync/official main daily 20260728 (#136)

- 完整 hash: `ba31df0c0da941467ef94a6c114a375af39b488f`
- 时间/作者: 2026-07-29 / RyeYuan
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-review-pr/SKILL.md`, `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md` 等 1780 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/MAINTAINER.md`; `.github/labeler.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/lint.yml`; `.github/workflows/nightly-test-amd-miles-rocm700.yml`; `.github/workflows/nightly-test-amd-miles-rocm720.yml` 等 26 个文件
  - docs-bench: `benchmark/bench_linear_attention/bench_cutedsl_kda_decode.py`; `benchmark/bench_linear_attention/bench_gdn_qkv_split.py`; `benchmark/hicache/bench_hicache_write_back.py`; `benchmark/hicache/perf.py`; `benchmark/kernels/all_reduce/benchmark_fused_ar_rms_quant_amd.py`; `benchmark/kernels/bench_fused_gate_sigmoid_mul_add.py`; `benchmark/kernels/bench_fused_sigmoid_mul.py`; `benchmark/kernels/deepseek/benchmark_cute_dsl_fp8_paged_mqa_logits.py` 等 47 个文件
  - other: `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`; `.claude/skills/cookbook-migrate-model/SKILL.md`; `.claude/skills/cookbook-review-pr/SKILL.md`; `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`; `3rdparty/amd/wheel/sglang/pyproject.toml`; `docker/Dockerfile`; `python/pyproject.toml` 等 146 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `python/sglang/srt/configs/load_config.py`; `python/sglang/srt/configs/mamba_utils.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/disaggregation/encode_server.py`; `python/sglang/srt/entrypoints/engine.py`; `python/sglang/srt/entrypoints/http_server.py` 等 69 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `python/sglang/jit_kernel/.clang-format`; `python/sglang/jit_kernel/__init__.py`; `python/sglang/jit_kernel/__main__.py`; `python/sglang/jit_kernel/activation.py`; `python/sglang/jit_kernel/add_constant.py` 等 965 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/deepseek_v4/__init__.py`; `python/sglang/jit_kernel/tests/deepseek_v4/common.py`; `python/sglang/jit_kernel/tests/kv_canary/__init__.py`; `python/sglang/jit_kernel/tests/kv_canary/_canary_helpers.py`; `python/sglang/jit_kernel/tests/kv_canary/_constants.py`; `python/sglang/jit_kernel/tests/kv_canary/_differential.py`; `python/sglang/jit_kernel/tests/kv_canary/_fixtures.py` 等 527 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b5a1e87297` - Merge pull request #133 from HYGON-AI/v0.5.12_dev_qwen3_coder

- 完整 hash: `b5a1e872971a0776ca3902cf54be2dcca359edec`
- 时间/作者: 2026-07-28 / lizhigong
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `0e24597391` - fix: pass quant_config to Qwen3Moe gate router, fix qwen3-coder accuracy issue

- 完整 hash: `0e24597391f450ae8a4a6f388a41e73db4bd9efd`
- 时间/作者: 2026-07-28 / JaneEyreliu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `38c750157f` - fix：修复接口改动.

- 完整 hash: `38c750157fb1485c24cc9135e71c923a6054ee66`
- 时间/作者: 2026-07-27 / luoyao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/moe/mega_moe.py` 等 21 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_5.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`; `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`; `python/sglang/srt/layers/moe/topk.py` 等 12 个文件
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

### Commit `540368a7d3` - Merge pull request #123 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `540368a7d3608d778f57d430e8a71fb22d9a6268`
- 时间/作者: 2026-07-23 / lizhigong
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `73c7e6c8f5` - [feat]:迁移lightop调用方式到新的接口.

- 完整 hash: `73c7e6c8f50ff20c1093426c6adf88744ef9c202`
- 时间/作者: 2026-07-22 / luoyao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/attention/dsv4/quant_k_cache.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py` 等 38 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_5.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py`; `python/sglang/srt/layers/attention/dsv4/metadata.py`; `python/sglang/srt/layers/attention/dsv4/quant_k_cache.py`; `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/flashattention_backend.py` 等 26 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6e5326678d` - fix(dcu): use runtime server args in Qwen3.5 paths

- 完整 hash: `6e5326678d6dcac6c8ab88be605b9318b8d0cd70`
- 时间/作者: 2026-07-22 / lizhigong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/communicator.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b4604b61fa` - ci(hcu): notify Feishu with accuracy results

- 完整 hash: `b4604b61fae504fa0ece17ca7dd1937af33c38e6`
- 时间/作者: 2026-07-21 / tianlinyang77
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_accuracy_report.py`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py` 等 13 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `python/sglang/test/hcu_accuracy_report.py`; `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py` 等 10 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `9b86479ac4` - test(hcu): add MATH-500 and HumanEval nightly coverage

- 完整 hash: `9b86479ac4f933649d4f777d1ffb92bfbfc375ab`
- 时间/作者: 2026-07-21 / tianlinyang77
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_reasoning_code_utils.py`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`, `test/hcu_humaneval_judge.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `.gitignore`; `THIRD_PARTY_NOTICES.md`; `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_reasoning_code_utils.py`; `test/hcu_humaneval_judge.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen35_397b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen36_35b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_30b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_32b_hcu.py`; `test/run_suite.py` 等 9 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `5dd9ba2f2c` - Merge pull request #108 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `5dd9ba2f2c48e98aa0f244a665bb67cde7141699`
- 时间/作者: 2026-07-21 / lizhigong
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `248bfe3471` - Merge pull request #106 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `248bfe3471b17cd0dfb6578091eeb39d85b6ff6b`
- 时间/作者: 2026-07-20 / lizhigong
- 自动分类: 通用实现调整
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `1e2fec228a` - feat(hcu): port runtime and kernel rename

- 完整 hash: `1e2fec228a9a8b1e781c3592eff356eeb8b584ed`
- 时间/作者: 2026-07-20 / tianlinyang77
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/jit_kernel/dsv4/moe.py`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/mxfp8.py` 等 106 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/check_env.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/managers/overlap_utils.py` 等 12 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/fp8_blockwise_gemm.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/mxfp8.py`; `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` 等 79 个文件
  - tests: `sgl-kernel/tests/test_moe_align.py`
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

### Commit `7c22d53e3d` - ci(hcu): use local model assets and fix mounts

- 完整 hash: `7c22d53e3db82a121fb92b3336ea817f83942021`
- 时间/作者: 2026-07-17 / DCU CI Bot
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml`, `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/nightly-test-hcu.yml`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm51_int8_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm5_cookbook_8gpu_server_hcu.py` 等 11 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `592b9a4e56` - test: add HCU coverage for GLM-5 MiMo and Qwen3.5

- 完整 hash: `592b9a4e56d3e7625db2ef03657b2a36f5345acb`
- 时间/作者: 2026-07-17 / LvJIA-RG
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`
  - other: `python/sglang/srt/speculative/multi_layer_eagle_utils.py`
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm51_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm5_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_qwen35_cookbook_4gpu_server_hcu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `88f43c7e14` - test: add Qwen3.6 HCU smoke and accuracy coverage

- 完整 hash: `88f43c7e147be3dd41ad3ef5394e312fceaf770e`
- 时间/作者: 2026-07-14 / dddddddxl
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/large_models/bw1100/test_qwen36_cookbook_2gpu_server_hcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_qwen36_cookbook_2gpu_server_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `1c70e76d5e` - test: use verified local HCU model paths

- 完整 hash: `1c70e76d5e1b044d327974b7ad1abde44651c5ec`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py`, `test/registered/hcu/lora/bw1100/test_qwen3_lora_server_hcu.py`, `test/registered/hcu/moe/bw1100/test_qwen3_30b_moe_instruct_hcu.py`, `test/registered/hcu/moe/bw1100/test_qwen3_30b_moe_server_hcu.py`, `test/registered/hcu/reranker/bw1100/test_qwen3_reranker_hcu.py`, `test/registered/hcu/spec/eagle/bw1100/test_qwen3_30b_eagle_dp_smoke_hcu.py`, `test/registered/hcu/srt/bw1100/test_qwen25_0p5b_server_hcu.py`, `test/registered/hcu/srt/bw1100/test_qwen25_1p5b_server_hcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/hcu/embedding/bw1100/test_gte_qwen2_embedding_hcu.py`; `test/registered/hcu/lora/bw1100/test_qwen3_lora_server_hcu.py`; `test/registered/hcu/moe/bw1100/test_qwen3_30b_moe_instruct_hcu.py`; `test/registered/hcu/moe/bw1100/test_qwen3_30b_moe_server_hcu.py`; `test/registered/hcu/reranker/bw1100/test_qwen3_reranker_hcu.py`; `test/registered/hcu/spec/eagle/bw1100/test_qwen3_30b_eagle_dp_smoke_hcu.py`; `test/registered/hcu/srt/bw1100/test_qwen25_0p5b_server_hcu.py`; `test/registered/hcu/srt/bw1100/test_qwen25_1p5b_server_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `bb9bb4b2dd` - ci: rename HCU PR stage suites

- 完整 hash: `bb9bb4b2dd757dfd72da13bc1d02deabf1dc7749`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/pr-test-hcu.yml`, `docs/hcu-pr-ci-visual-guide.html`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_hybrid_attn_backend.py`, `test/registered/attention/test_pack_paged_kv_to_varlen.py`, `test/registered/attention/test_torch_native_attention_backend.py` 等 157 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/pr-test-hcu.yml`
  - docs-bench: `docs/hcu-pr-ci-visual-guide.html`
  - tests: `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py`; `test/registered/attention/test_pack_paged_kv_to_varlen.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_kernels.py`; `test/registered/attention/test_triton_sliding_window.py`; `test/registered/backends/test_torch_compile.py` 等 154 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `4fb3f09391` - runtime: migrate current main DCU interfaces to HCU

- 完整 hash: `4fb3f09391ef791a7dd3811b0c610d6b89ae8ea0`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/attention_registry.py` 等 78 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/layers/mhc.py`; `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/model_loader/loader.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py`; `python/sglang/srt/models/minimax_m2.py` 等 13 个文件
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/compressor.py`; `python/sglang/srt/layers/attention/dsv4/indexer.py` 等 51 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f38f1a5d21` - test: sync HCU registrations with current main

- 完整 hash: `f38f1a5d2113838d01fc4e51151e49d9a164a50e`
- 时间/作者: 2026-07-13 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/test/ci/ci_register.py`, `python/sglang/test/dcu_cookbook_utils.py`, `python/sglang/test/dcu_utils.py`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_utils.py`, `python/sglang/test/simple_eval_mmmu_vlm.py`, `python/sglang/test/test_utils.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` 等 322 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` 等 322 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `0334ae99b9` - Merge pull request #86 from HYGON-AI/v0.5.12_dev_fix_qwen3.5_397b

- 完整 hash: `0334ae99b93c45fc6c0bdb75f30f89150a4bc611`
- 时间/作者: 2026-07-10 / lizhigong
- 自动分类: 缺陷修复
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `dd0492dbf4` - [PD]解决qwen3.5-397b在pd分离场景下的精度问题

- 完整 hash: `dd0492dbf471fd1ec0941337ae8e0d9c15ae75ca`
- 时间/作者: 2026-07-09 / luoyao
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/common/conn.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `2d561a3ec2` - chore: add modification notices for DCU changes

- 完整 hash: `2d561a3ec23bdc4e0bfeebf73eea1fe638dc3e80`
- 时间/作者: 2026-07-05 / Lv Jiajia
- 自动分类: 性能/后端优化
- 主要文件: `NOTICE`, `THIRD_PARTY_NOTICES.md`, `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/include/sgl_kernel/utils.h`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 250 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `NOTICE`; `THIRD_PARTY_NOTICES.md`; `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py` 等 23 个文件
  - runtime-model: `python/sglang/srt/model_executor/input_buffers.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/speculative/eagle_worker.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/jit_kernel/deepseek_v4.py`; `python/sglang/jit_kernel/dsv4/compress.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/include/sgl_kernel/utils.h`; `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py` 等 68 个文件
  - tests: `python/sglang/test/ci/ci_register.py`; `python/sglang/test/few_shot_gsm8k.py`; `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_mmlu.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py`; `sgl-kernel/tests/test_moe_align.py`; `sgl-kernel/tests/test_norm.py` 等 153 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `1a4b4404eb` - 修复qwen3.5-397b PD分离不支持的问题

- 完整 hash: `1a4b4404eb6b47db05c2cc2f0cd4d798389f9bf6`
- 时间/作者: 2026-07-01 / liucong8560
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `75e928284a` - Register DCU tests in categorized nightly suites

- 完整 hash: `75e928284a54ea765f0823bf468896e54cf8776a`
- 时间/作者: 2026-06-29 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/constrained_decoding/test_constrained_decoding.py`, `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`, `test/registered/dcu/embedding/bw1100/test_gte_qwen2_embedding_dcu.py`, `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`, `test/registered/dcu/interface/test_dcu_stage_b_flow_1.py`, `test/registered/dcu/lora/bw1100/test_qwen3_lora_server_dcu.py`, `test/registered/dcu/models/test_reward_models_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py` 等 28 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/constrained_decoding/test_constrained_decoding.py`; `test/registered/dcu/core/bw1100/test_hidden_states_dcu.py`; `test/registered/dcu/embedding/bw1100/test_gte_qwen2_embedding_dcu.py`; `test/registered/dcu/interface/test_dcu_stage_b_flow_0.py`; `test/registered/dcu/interface/test_dcu_stage_b_flow_1.py`; `test/registered/dcu/lora/bw1100/test_qwen3_lora_server_dcu.py`; `test/registered/dcu/models/test_reward_models_dcu.py`; `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py` 等 28 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `db4a263167` - test: use local DCU model paths for smoke tests

- 完整 hash: `db4a2631679173d94d8ef07bee785c40587e3401`
- 时间/作者: 2026-06-27 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`; `test/registered/dcu/moe/bw1100/test_qwen3_30b_moe_smoke_dcu.py`; `test/registered/dcu/vlm_models/bw1100/test_qwen2_vl_2b_server_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `54f44d298f` - test: add DCU cookbook nightly model coverage

- 完整 hash: `54f44d298fa4b21c3907e2d585e383b3bc02201d`
- 时间/作者: 2026-06-26 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/test/dcu_cookbook_utils.py`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_gsm8k_eval_dcu.py`, `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`, `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`, `test/registered/dcu/large_models/bw1100/test_deepseek_v32_cookbook_8gpu_server_dcu.py` 等 24 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_start_container.sh`
  - tests: `python/sglang/test/dcu_cookbook_utils.py`; `test/registered/dcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_cookbook_text_mmlu_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_gsm8k_eval_dcu.py`; `test/registered/dcu/accuracy/bw1100/test_mmlu_eval_dcu.py`; `test/registered/dcu/kernels/test_sgl_kernel_supported_dcu.py`; `test/registered/dcu/large_models/bw1100/test_deepseek_v32_cookbook_8gpu_server_dcu.py`; `test/registered/dcu/large_models/bw1100/test_glm51_cookbook_8gpu_server_dcu.py` 等 23 个文件
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

### Commit `51abf3148c` - test: add DCU AI smoke cases to PR required

- 完整 hash: `51abf3148cb5741b4df29ac2d3a3075095d5ac28`
- 时间/作者: 2026-06-23 / DCU CI Bot
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `test/registered/dcu/openai_server/test_function_calling_dcu.py`, `test/registered/dcu/openai_server/test_hidden_states_base_dcu.py`, `test/registered/dcu/openai_server/test_protocol_dcu.py`, `test/registered/dcu/openai_server/test_serving_chat_dcu.py`, `test/registered/dcu/openai_server/test_tool_choice_dcu.py`, `test/registered/dcu/reranker/bw1100/test_qwen3_reranker_dcu.py`, `test/registered/dcu/rotary/test_mrope_smoke_dcu.py` 等 13 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - tests: `test/registered/dcu/openai_server/test_function_calling_dcu.py`; `test/registered/dcu/openai_server/test_hidden_states_base_dcu.py`; `test/registered/dcu/openai_server/test_protocol_dcu.py`; `test/registered/dcu/openai_server/test_serving_chat_dcu.py`; `test/registered/dcu/openai_server/test_tool_choice_dcu.py`; `test/registered/dcu/reranker/bw1100/test_qwen3_reranker_dcu.py`; `test/registered/dcu/rotary/test_mrope_smoke_dcu.py`; `test/registered/dcu/spec/test_build_eagle_tree_dcu.py` 等 12 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `e49d0d2fbb` - [bugfix]修复sglang0.5.12官方bug,解决因此引起的Qwen3-30B-A3B-Instruct-2507精度问题

- 完整 hash: `e49d0d2fbb11d5d278eff9fced9156286313d054`
- 时间/作者: 2026-06-16 / chenyuege
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/utils.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5a231f0b59` - test: add DCU disabled smoke candidates

- 完整 hash: `5a231f0b591bfff1407351c40f1ae7de937285da`
- 时间/作者: 2026-06-12 / LvJIA-RG
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/dcu/4-gpu-models/test_qwen3_next_80b_server_dcu.py`, `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`, `test/registered/dcu/core/test_score_api_dcu.py`, `test/registered/dcu/layers/test_mamba2_mixer_dcu.py`, `test/registered/dcu/models/test_reward_models_dcu.py`, `test/registered/dcu/spec/test_ngram_speculative_decoding_dcu.py`, `test/registered/dcu/vlm_models/bw1100/test_qwen25_vl_input_format_dcu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/dcu/4-gpu-models/test_qwen3_next_80b_server_dcu.py`; `test/registered/dcu/attention/test_fa3_text_smoke_dcu.py`; `test/registered/dcu/core/test_score_api_dcu.py`; `test/registered/dcu/layers/test_mamba2_mixer_dcu.py`; `test/registered/dcu/models/test_reward_models_dcu.py`; `test/registered/dcu/spec/test_ngram_speculative_decoding_dcu.py`; `test/registered/dcu/vlm_models/bw1100/test_qwen25_vl_input_format_dcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `4d9dc66182` - ci: reduce DCU CI mainline intrusion

- 完整 hash: `4d9dc66182e7afc0827207ecf93f7f31cd884677`
- 时间/作者: 2026-06-11 / DCU CI Bot
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-gate.yml`, `.github/workflows/release-whl-dcu.yml`, `python/sglang/__init__.py`, `python/sglang/lang/api.py`, `python/sglang/srt/models/qwen2.py`, `python/sglang/test/ci/ci_utils.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py` 等 151 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-gate.yml`; `.github/workflows/release-whl-dcu.yml`
  - other: `python/sglang/__init__.py`; `python/sglang/lang/api.py`
  - runtime-model: `python/sglang/srt/models/qwen2.py`
  - tests: `python/sglang/test/ci/ci_utils.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/amd/disaggregation/test_disaggregation_pp.py`; `test/registered/amd/test_deepseek_v32_basic.py`; `test/registered/amd/test_deepseek_v32_mtp.py`; `test/registered/amd/test_deepseek_v3_basic.py`; `test/registered/amd/test_deepseek_v3_mtp.py` 等 146 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `cc279bcf67` - ci: rename DCU BW1000 tests to BW1100

- 完整 hash: `cc279bcf6722c46e4f7fde54befec031f3618719`
- 时间/作者: 2026-06-05 / tly123
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py`, `test/registered/amd/disaggregation/test_disaggregation_pp.py`, `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_deepseek_v3_basic.py`, `test/registered/amd/test_deepseek_v3_mtp.py` 等 165 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - tests: `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/amd/disaggregation/test_disaggregation_pp.py`; `test/registered/amd/test_deepseek_v32_basic.py`; `test/registered/amd/test_deepseek_v32_mtp.py`; `test/registered/amd/test_deepseek_v3_basic.py`; `test/registered/amd/test_deepseek_v3_mtp.py`; `test/registered/attention/test_fa3.py` 等 164 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f08ff0baba` - ci: disable failed DCU full-enabled tests

- 完整 hash: `f08ff0babadbe873c1832572efb520b233fd2158`
- 时间/作者: 2026-06-05 / dddddddxl
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/attention/test_triton_attention_backend.py`, `test/registered/bench_fn/test_bench_serving_functionality.py`, `test/registered/core/test_page_size.py`, `test/registered/core/test_request_queue_validation.py`, `test/registered/core/test_srt_endpoint.py`, `test/registered/core/test_srt_engine.py` 等 49 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - tests: `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py`; `test/registered/bench_fn/test_bench_serving_functionality.py`; `test/registered/core/test_page_size.py`; `test/registered/core/test_request_queue_validation.py`; `test/registered/core/test_srt_endpoint.py`; `test/registered/core/test_srt_engine.py`; `test/registered/dcu/moe/bw1000/test_qwen3_30b_moe_instruct_dcu.py` 等 48 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f57339642b` - ci: keep DCU test defaults official-friendly

- 完整 hash: `f57339642b6c3c7846b4e068be0b434ddd10cdce`
- 时间/作者: 2026-06-04 / tly123
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/test/test_utils.py`, `scripts/ci/dcu/dcu_ci_exec.sh`, `scripts/ci/dcu/dcu_ci_start_container.sh`, `test/registered/dcu/accuracy/bw1000/test_mmlu_eval_dcu.py`, `test/registered/dcu/accuracy/bw1000/test_mmmu_eval_dcu.py`, `test/registered/dcu/embedding/bw1000/test_gte_qwen2_embedding_dcu.py`, `test/registered/dcu/moe/bw1000/test_qwen3_30b_moe_instruct_dcu.py`, `test/registered/dcu/moe/bw1000/test_qwen3_30b_moe_server_dcu.py` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/dcu/dcu_ci_exec.sh`; `scripts/ci/dcu/dcu_ci_start_container.sh`
  - tests: `python/sglang/test/test_utils.py`; `test/registered/dcu/accuracy/bw1000/test_mmlu_eval_dcu.py`; `test/registered/dcu/accuracy/bw1000/test_mmmu_eval_dcu.py`; `test/registered/dcu/embedding/bw1000/test_gte_qwen2_embedding_dcu.py`; `test/registered/dcu/moe/bw1000/test_qwen3_30b_moe_instruct_dcu.py`; `test/registered/dcu/moe/bw1000/test_qwen3_30b_moe_server_dcu.py`; `test/registered/dcu/reranker/bw1000/test_qwen3_reranker_dcu.py`; `test/registered/dcu/srt/bw1000/test_qwen25_0p5b_server_dcu.py` 等 15 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `f8dc6e03e4` - 支持Qwen3.5-397b-channel-fp8 EP8并行方案

- 完整 hash: `f8dc6e03e4e0ddeed638be295f353cb42dbf3a47`
- 时间/作者: 2026-05-26 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `90205d601e` - test: sync validated DCU registered cases

- 完整 hash: `90205d601e2d23e4cb8ae50a52fe60e9158087c0`
- 时间/作者: 2026-05-29 / tly123
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py`, `test/registered/amd/disaggregation/test_disaggregation_pp.py`, `test/registered/amd/test_deepseek_v32_basic.py`, `test/registered/amd/test_deepseek_v32_mtp.py`, `test/registered/amd/test_deepseek_v3_basic.py`, `test/registered/amd/test_deepseek_v3_mtp.py` 等 202 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/amd/disaggregation/test_disaggregation_pp.py`; `test/registered/amd/test_deepseek_v32_basic.py`; `test/registered/amd/test_deepseek_v32_mtp.py`; `test/registered/amd/test_deepseek_v3_basic.py`; `test/registered/amd/test_deepseek_v3_mtp.py` 等 202 个文件
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
- 本章节提交数: 25（其中 merge 8）
- 分支更新段: `hg-full-base..main`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/mem_cache/memory_pool.py` | `c5dd815b3`, `1a4b4404e`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen3_5.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `6e5326678`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen3_moe.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `0e2459739`, `123e9539e` |
| `python/sglang/srt/distributed/parallel_state.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/layernorm.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `c5dd815b3`, `f8dc6e03e`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/moe/topk.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/bailing_moe.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/minimax_m2.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen2.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/qwen3.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v4.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/hunyuan_v3.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/models/mimo_v2.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157`, `123e9539e` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `c5dd815b3`, `1a4b4404e`, `4fb3f0939`, `1e2fec228` |
| `python/sglang/srt/environ.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `73c7e6c8f` |
| `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` | `c5dd815b3`, `4fb3f0939`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py` | `c5dd815b3`, `4fb3f0939`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/communicator.py` | `c5dd815b3`, `6e5326678`, `73c7e6c8f`, `123e9539e` |
| `python/sglang/srt/layers/moe/mega_moe.py` | `4fb3f0939`, `1e2fec228`, `73c7e6c8f`, `38c750157` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `c5dd815b3`, `f8dc6e03e`, `4fb3f0939`, `1e2fec228` |
| `python/sglang/srt/layers/quantization/fp8.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/moe_wna16.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_fp8.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_int8.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/model_executor/model_runner.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `c5dd815b3`, `4fb3f0939`, `1e2fec228`, `123e9539e` |
| ... | 另有 243 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-05-18 | `c5dd815b3` | `hg-full-base..main` | 性能/后端优化 | dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6) | `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py` 等 141 个文件 |
| 2026-05-26 | `f8dc6e03e` | `hg-full-base..main` | 性能/后端优化 | 支持Qwen3.5-397b-channel-fp8 EP8并行方案 | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-06-05 | `f08ff0bab` | `hg-full-base..main` | 性能/后端优化 | ci: disable failed DCU full-enabled tests | `.github/workflows/pr-test-dcu.yml`, `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/attention/test_triton_attention_backend.py` 等 49 个文件 |
| 2026-06-16 | `e49d0d2fb` | `hg-full-base..main` | 缺陷修复 | [bugfix]修复sglang0.5.12官方bug,解决因此引起的Qwen3-30B-A3B-Instruct-2507精度问题 | `python/sglang/srt/models/utils.py` |
| 2026-07-01 | `1a4b4404e` | `hg-full-base..main` | 缺陷修复 | 修复qwen3.5-397b PD分离不支持的问题 | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-07-09 | `dd0492dbf` | `hg-full-base..main` | 调度/缓存/PD | [PD]解决qwen3.5-397b在pd分离场景下的精度问题 | `python/sglang/srt/disaggregation/common/conn.py` |
| 2026-07-10 | `0334ae99b` | `hg-full-base..main` | 缺陷修复 | Merge pull request #86 from HYGON-AI/v0.5.12_dev_fix_qwen3.5_397b | 无直接文件变更/merge |
| 2026-07-13 | `4fb3f0939` | `hg-full-base..main` | 性能/后端优化 | runtime: migrate current main DCU interfaces to HCU | `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` 等 80 个文件 |
| 2026-07-14 | `88f43c7e1` | `hg-full-base..main` | 模型支持/运行时入口 | test: add Qwen3.6 HCU smoke and accuracy coverage | `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/large_models/bw1100/test_qwen36_cookbook_2gpu_server_hcu.py` |
| 2026-07-17 | `592b9a4e5` | `hg-full-base..main` | 性能/后端优化 | test: add HCU coverage for GLM-5 MiMo and Qwen3.5 | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py` 等 12 个文件 |
| 2026-07-20 | `1e2fec228` | `hg-full-base..main` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-07-20 | `248bfe347` | `hg-full-base..main` | 通用实现调整 | Merge pull request #106 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge |
| 2026-07-21 | `5dd9ba2f2` | `hg-full-base..main` | 通用实现调整 | Merge pull request #108 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge |
| 2026-07-22 | `6e5326678` | `hg-full-base..main` | 缺陷修复 | fix(dcu): use runtime server args in Qwen3.5 paths | `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py` |
| 2026-07-22 | `73c7e6c8f` | `hg-full-base..main` | 性能/后端优化 | [feat]:迁移lightop调用方式到新的接口. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 38 个文件 |
| 2026-07-23 | `540368a7d` | `hg-full-base..main` | 通用实现调整 | Merge pull request #123 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge |
| 2026-07-27 | `38c750157` | `hg-full-base..main` | 性能/后端优化 | fix：修复接口改动. | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 21 个文件 |
| 2026-07-28 | `0e2459739` | `hg-full-base..main` | 性能/后端优化 | fix: pass quant_config to Qwen3Moe gate router, fix qwen3-coder accuracy issue | `python/sglang/srt/models/qwen3_moe.py` |
| 2026-07-28 | `b5a1e8729` | `hg-full-base..main` | 通用实现调整 | Merge pull request #133 from HYGON-AI/v0.5.12_dev_qwen3_coder | 无直接文件变更/merge |
| 2026-07-29 | `956b15538` | `hg-full-base..main` | 通用实现调整 | Merge pull request #145 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b | 无直接文件变更/merge |
| 2026-07-31 | `123e9539e` | `hg-full-base..main` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-07-31 | `f6603bbe5` | `hg-full-base..main` | 性能/后端优化 | [fix] Fixed accuracy issue caused by aiter‑moe in Qwen3.6‑35B‑A3B‑W8A8 | `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-08-06 | `799aaa455` | `hg-full-base..main` | 通用实现调整 | Merge pull request #168 from HYGON-AI/v0.5.12_dev_qwen3.5_eplb | 无直接文件变更/merge |
| 2026-08-20 | `9ca1b25f7` | `hg-full-base..main` | 通用实现调整 | Merge pull request #210 from HYGON-AI/main_dev_qwen3.8 | 无直接文件变更/merge |
| 2026-09-23 | `9cd15042a` | `hg-full-base..main` | 模型支持/运行时入口 | feat(citest): 更新镜像测试用例, 适配 0.5.18 (Qwen3.8 / DeepSeek-V4) (#433) | `docker/image-citest-conf-hcu.yaml` |

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

#### Commit `f8dc6e03e` - 支持Qwen3.5-397b-channel-fp8 EP8并行方案

- 完整 hash: `f8dc6e03e4e0ddeed638be295f353cb42dbf3a47`
- 时间/作者: 2026-05-26 / liucong8560
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f08ff0bab` - ci: disable failed DCU full-enabled tests

- 完整 hash: `f08ff0babadbe873c1832572efb520b233fd2158`
- 时间/作者: 2026-06-05 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-dcu.yml`, `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/attention/test_triton_attention_backend.py`, `test/registered/bench_fn/test_bench_serving_functionality.py`, `test/registered/core/test_page_size.py`, `test/registered/core/test_request_queue_validation.py`, `test/registered/core/test_srt_endpoint.py`, `test/registered/core/test_srt_engine.py` 等 49 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-dcu.yml`
  - tests: `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py`; `test/registered/bench_fn/test_bench_serving_functionality.py`; `test/registered/core/test_page_size.py`; `test/registered/core/test_request_queue_validation.py`; `test/registered/core/test_srt_endpoint.py`; `test/registered/core/test_srt_engine.py`; `test/registered/dcu/moe/bw1000/test_qwen3_30b_moe_instruct_dcu.py` 等 48 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `e49d0d2fb` - [bugfix]修复sglang0.5.12官方bug,解决因此引起的Qwen3-30B-A3B-Instruct-2507精度问题

- 完整 hash: `e49d0d2fbb11d5d278eff9fced9156286313d054`
- 时间/作者: 2026-06-16 / chenyuege
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/utils.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `1a4b4404e` - 修复qwen3.5-397b PD分离不支持的问题

- 完整 hash: `1a4b4404eb6b47db05c2cc2f0cd4d798389f9bf6`
- 时间/作者: 2026-07-01 / liucong8560
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `dd0492dbf` - [PD]解决qwen3.5-397b在pd分离场景下的精度问题

- 完整 hash: `dd0492dbf471fd1ec0941337ae8e0d9c15ae75ca`
- 时间/作者: 2026-07-09 / luoyao
- 分支更新段: `hg-full-base..main`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/common/conn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/common/conn.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `0334ae99b` - Merge pull request #86 from HYGON-AI/v0.5.12_dev_fix_qwen3.5_397b

- 完整 hash: `0334ae99b93c45fc6c0bdb75f30f89150a4bc611`
- 时间/作者: 2026-07-10 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

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

#### Commit `88f43c7e1` - test: add Qwen3.6 HCU smoke and accuracy coverage

- 完整 hash: `88f43c7e147be3dd41ad3ef5394e312fceaf770e`
- 时间/作者: 2026-07-14 / dddddddxl
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/large_models/bw1100/test_qwen36_cookbook_2gpu_server_hcu.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_qwen36_cookbook_2gpu_server_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `592b9a4e5` - test: add HCU coverage for GLM-5 MiMo and Qwen3.5

- 完整 hash: `592b9a4e56d3e7625db2ef03657b2a36f5345acb`
- 时间/作者: 2026-07-17 / LvJIA-RG
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `python/sglang/test/hcu_cookbook_utils.py`, `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py` 等 12 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`
  - other: `python/sglang/srt/speculative/multi_layer_eagle_utils.py`
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_glm5_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mimo_v2_flash_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm51_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_glm5_cookbook_8gpu_server_hcu.py`; `test/registered/hcu/large_models/bw1100/test_qwen35_cookbook_4gpu_server_hcu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

#### Commit `248bfe347` - Merge pull request #106 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `248bfe3471b17cd0dfb6578091eeb39d85b6ff6b`
- 时间/作者: 2026-07-20 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `5dd9ba2f2` - Merge pull request #108 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `5dd9ba2f2c48e98aa0f244a665bb67cde7141699`
- 时间/作者: 2026-07-21 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `6e5326678` - fix(dcu): use runtime server args in Qwen3.5 paths

- 完整 hash: `6e5326678d6dcac6c8ab88be605b9318b8d0cd70`
- 时间/作者: 2026-07-22 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/qwen3_5.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/communicator.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

#### Commit `540368a7d` - Merge pull request #123 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `540368a7d3608d778f57d430e8a71fb22d9a6268`
- 时间/作者: 2026-07-23 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

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

#### Commit `0e2459739` - fix: pass quant_config to Qwen3Moe gate router, fix qwen3-coder accuracy issue

- 完整 hash: `0e24597391f450ae8a4a6f388a41e73db4bd9efd`
- 时间/作者: 2026-07-28 / JaneEyreliu
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b5a1e8729` - Merge pull request #133 from HYGON-AI/v0.5.12_dev_qwen3_coder

- 完整 hash: `b5a1e872971a0776ca3902cf54be2dcca359edec`
- 时间/作者: 2026-07-28 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `956b15538` - Merge pull request #145 from HYGON-AI/v0.5.12_dev_yaoht_qwen3.5_397b

- 完整 hash: `956b155384fa2b369a673c5985acbce08dd2b55e`
- 时间/作者: 2026-07-29 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

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

#### Commit `f6603bbe5` - [fix] Fixed accuracy issue caused by aiter‑moe in Qwen3.6‑35B‑A3B‑W8A8

- 完整 hash: `f6603bbe5b71b96153bcab4d3e9e3ec345dd5ae5`
- 时间/作者: 2026-07-31 / chenyuege
- 分支更新段: `hg-full-base..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `799aaa455` - Merge pull request #168 from HYGON-AI/v0.5.12_dev_qwen3.5_eplb

- 完整 hash: `799aaa455bca9002d7bbde91967039854ef2a8b9`
- 时间/作者: 2026-08-06 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `9ca1b25f7` - Merge pull request #210 from HYGON-AI/main_dev_qwen3.8

- 完整 hash: `9ca1b25f7f912a086d4a5c6a4706a3b373eae0be`
- 时间/作者: 2026-08-20 / lizhigong
- 分支更新段: `hg-full-base..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `9cd15042a` - feat(citest): 更新镜像测试用例, 适配 0.5.18 (Qwen3.8 / DeepSeek-V4) (#433)

- 完整 hash: `9cd15042af60905ef088d409908e41e330fbf345`
- 时间/作者: 2026-09-23 / Crowder13
- 分支更新段: `hg-full-base..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `docker/image-citest-conf-hcu.yaml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `docker/image-citest-conf-hcu.yaml`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

<!-- LOCAL_ONLY_FULL_MAIN_TO_20261105_END -->
