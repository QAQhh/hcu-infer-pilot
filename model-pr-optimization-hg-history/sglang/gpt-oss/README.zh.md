# sglang GPT-OSS 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `benchmark/gpt_oss/README.md` | 无直接提交 |
| `docs/basic_usage/gpt_oss.md` | `c4db64c16`, `de6a03260`, `3d72944fb` |
| `python/sglang/srt/function_call/gpt_oss_detector.py` | 无直接提交 |
| `python/sglang/srt/models/gpt_oss.py` | `bbe25b241`, `d1e95af28`, `d8d0208c6`, `2bd836348`, `fb683be6e`, `61abff66c`, `733de6be3`, `d27f16f38`, `bed301a5a` |
| `python/sglang/test/gpt_oss_common.py` | `20554a0a4`, `0c474273c` |
| `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` | `8290171f5`, `a0bae4c34` |
| `test/registered/8-gpu-models/test_gpt_oss_120b.py` | `c8da307d7` |
| `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py` | `88010e960`, `20554a0a4`, `6fd878b41` |
| `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` | `20554a0a4`, `6fd878b41`, `f8636fbb2`, `b025cff44` |
| `test/registered/core/test_gpt_oss_1gpu.py` | `814202704`, `146b5fcc8`, `cc25f9df5`, `4e999404c`, `0c474273c` |
| `test/registered/core/test_gpt_oss_sm120.py` | `814202704`, `8cdb7e1fd` |
| `test/registered/models/test_gpt_oss_models_pcg.py` | `814202704`, `152560d1b` |
| `test/registered/perf/test_gpt_oss_4gpu_perf.py` | `989d4b301` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 45
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-25 | `bbe25b241` | 性能/后端优化 | Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+ (#20755) | `python/sglang/srt/models/gpt_oss.py` |
| 2026-03-24 | `c4db64c16` | 性能/后端优化 | Add Lychee Doc Links Check to Local and CI (#19742) | `.github/linters/lychee-ci.toml`, `.github/linters/lychee.toml`, `.github/workflows/lint.yml` |
| 2026-03-23 | `814202704` | 性能/后端优化 | ci: unify PR test suite naming (#21187) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-21 | `3f0ba021f` | 性能/后端优化 | [AMD] Improve openai/gpt-oss performance (#21020) | `python/sglang/srt/layers/attention/aiter_backend.py` |
| 2026-03-19 | `126cd5cfa` | 性能/后端优化 | gpt-oss decode performance optimization (#20392) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/utils.py`, `python/sglang/srt/layers/quantization/unquant.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-07 | `8cdb7e1fd` | 模型支持/运行时入口 | [CI] Add GPT-OSS test for SM120 (#20056) | `test/registered/core/test_gpt_oss_sm120.py` |
| 2026-03-07 | `759700c80` | 性能/后端优化 | Fix SM120 `triton_kernels` MXFP4 `block_k` for GPT-OSS (#20040) | `python/sglang/srt/layers/quantization/mxfp4.py` |
| 2026-03-03 | `9305f0e58` | 性能/后端优化 | Support `triton_kernels` for GPT-OSS on SM120 (#19718) | `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/server_args.py` |
| 2026-03-02 | `15af26d1e` | 性能/后端优化 | Add aiter attention support in prefill-attention-backend of gpt-oss (#18282) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/server_args.py` |
| 2026-02-28 | `35ef38c61` | 通用实现调整 | Remove gpt-oss hybrid swa gate for trtllm_mha (#19079) | `python/sglang/srt/server_args.py` |
| 2026-02-24 | `152560d1b` | 模型支持/运行时入口 | [PCG] add pcg CI test for gpt-oss model (#18961) | `test/registered/models/test_gpt_oss_models_pcg.py` |
| 2026-02-21 | `d8d0208c6` | 性能/后端优化 | [Feature] rewrite rope kernel; remove flashinfer dependencies (#18844) | `python/sglang/jit_kernel/benchmark/bench_rope.py`, `python/sglang/jit_kernel/csrc/elementwise/rope.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh` |
| 2026-02-20 | `4bffd3a23` | 性能/后端优化 | [GPT-OSS] support fp8 online quantization for gpt-oss bf16 (#18988) | `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/server_args.py` |
| 2026-02-16 | `8290171f5` | 模型支持/运行时入口 | [CI] Remove `--mem-fraction-static 0.93` from gpt-oss test (#18869) | `test/registered/4-gpu-models/test_gpt_oss_4gpu.py` |
| 2026-02-15 | `88010e960` | 性能/后端优化 | [AMD] Fix nightly 1-GPU test failures and bench_serving regression (#18761) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `python/sglang/bench_serving.py` |
| 2026-02-12 | `20554a0a4` | 性能/后端优化 | [AMD] rocm 7.2 image release, PR test, Nightly Test (#17799) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml` |
| 2026-02-11 | `2bd836348` | 性能/后端优化 | [PCG] GPT OSS Triton Kernel Support (#18405) | `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-02-04 | `de6a03260` | 缺陷修复 | [docs] fix misspellings & typos (#18276) | `docs/advanced_features/dp_for_multi_modal_encoder.md`, `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v3.md` |
| 2026-02-04 | `6fd878b41` | 性能/后端优化 | [AMD] Add kimi mi35x nightly test, folder organization and several stability fixes (#17895) | `.github/workflows/nightly-test-amd.yml`, `python/sglang/test/nightly_utils.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py` |
| 2026-02-02 | `c8da307d7` | 模型支持/运行时入口 | feature: adding gpt-oss 120b nightly test (#18134) | `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_gpt_oss_120b.py` |
| 2026-01-31 | `a0bae4c34` | 性能/后端优化 | Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299) | `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py` |
| 2026-01-31 | `38d275a9f` | 性能/后端优化 | [BugFix] fix gpt-oss accuracy issue when enabling piecewise cuda graph (#18013) | `python/sglang/srt/managers/schedule_batch.py` |
| 2026-01-29 | `ef1c51275` | 性能/后端优化 | Add aiter bias moe support in gpt-oss mxfp4 model (#17735) | `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/server_args.py` |
| 2026-01-28 | `f8636fbb2` | 性能/后端优化 | [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI (#17523) | `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` |
| 2026-01-26 | `6c0f9b482` | 模型支持/运行时入口 | Add test_gpt_oss_4gpu.py to B200 test suite (#17743) | `test/srt/run_suite.py` |
| 2026-01-24 | `fb683be6e` | 性能/后端优化 | Use attn tp group in embedding for more models (#17570) | `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py` |
| 2026-01-22 | `2b2f31738` | 性能/后端优化 | fix gpt-oss launch failure with piecewise cuda graph (#17532) |  |
| 2026-01-22 | `61abff66c` | 缺陷修复 | [NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py (#17553) | `python/sglang/srt/models/gpt_oss.py` |
| 2026-01-21 | `9be2a3a9a` | 测试/文档/基准 | Remove test_gpt_oss_4gpu.py from __not_in_ci__ (keep in per-commit-4-gpu) (#17534) | `test/srt/run_suite.py` |
| 2026-01-21 | `85d9af51d` | 测试/文档/基准 | Temporarily disable flaky test_gpt_oss_4gpu.py on B200 (#17528) | `test/srt/run_suite.py` |
| 2026-01-22 | `d725487dc` | 通用实现调整 | Disable swa memory for gpt-oss with spec (#17517) | `python/sglang/srt/server_args.py` |
| 2026-01-19 | `733de6be3` | 性能/后端优化 | [NPU]Support GPT-OSS for NPU (#14197) | `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/gpt_oss.py` |
| 2026-01-18 | `e499258e9` | 调度/缓存/PD | Use swa radix cache and memory pool for gpt-oss model (#17261) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/utils.py`, `python/sglang/srt/server_args.py` |
| 2026-01-15 | `146b5fcc8` | 性能/后端优化 | [CI] Reorganize stage-b 1-GPU tests for 5090 compatibility (#16826) | `.github/workflows/pr-test.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py` |
| 2026-01-15 | `3d72944fb` | 模型支持/运行时入口 | [Doc] Add tip on how to use Spec V2 (#15455) | `docs/basic_usage/deepseek_v3.md`, `docs/basic_usage/glm45.md`, `docs/basic_usage/gpt_oss.md` |
| 2026-01-13 | `b025cff44` | 性能/后端优化 | [AMD] Add AMD CI registration (1-gpu unit test) to nightly CI. (#16941) | `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py` |
| 2026-01-10 | `cc25f9df5` | 性能/后端优化 | Update est_time for stage-b-test-small-1-gpu tests (#16835) | `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_deterministic.py` |
| 2026-01-10 | `a2c2c09d7` | 性能/后端优化 | [BugFix] fix gpt-oss-120b launch failure with --enable-piecewise-cuda-graph (#16757) | `python/sglang/srt/layers/quantization/mxfp4.py` |
| 2026-01-10 | `d27f16f38` | 性能/后端优化 | Fix EPLB + FP4 Quantization Compatibility Issue (#13715) | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/deepseek_v2.py` |
| 2026-01-09 | `4e999404c` | 性能/后端优化 | [AMD] Fix CI - unit-test-backend-1-gpu-amd-mi35x and unit-test-backend-2-gpu-amd, stage-b-test-small-1-gpu-amd (#16675) | `.github/workflows/pr-test-amd.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py` |
| 2026-01-07 | `0c474273c` | 缺陷修复 | Fix gpt_oss_common import path and migrate core tests (#16426) | `python/sglang/test/gpt_oss_common.py`, `test/registered/core/test_deterministic.py`, `test/registered/core/test_gpt_oss_1gpu.py` |
| 2025-12-30 | `3dfff6ae3` | 性能/后端优化 | Eagle: GPT-OSS Eagle v2 support (#14920) | `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py` |
| 2025-12-22 | `989d4b301` | 性能/后端优化 | [CI] Migrate nightly tests to test/registered/ (#15582) | `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py` |
| 2025-12-21 | `bed301a5a` | 性能/后端优化 | [Feature] Enable return routed experts (#12162) | `python/sglang/bench_serving.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/routed_experts_capturer.py` |

## 逐 Commit 审计卡

### Commit `bbe25b241` - Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+ (#20755)

- 完整 hash: `bbe25b24126d456965577c159557f97036556e9f`
- 时间/作者: 2026-03-25 / Mohammad Miadh Angkad
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/gpt_oss.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c4db64c16` - Add Lychee Doc Links Check to Local and CI (#19742)

- 完整 hash: `c4db64c16bba9cb549d510735a064272c87779fa`
- 时间/作者: 2026-03-24 / Jiaxin(Jackson) Deng
- 自动分类: 性能/后端优化
- 主要文件: `.github/linters/lychee-ci.toml`, `.github/linters/lychee.toml`, `.github/workflows/lint.yml`, `.github/workflows/nightly-link-check.yml`, `.pre-commit-config.yaml`, `benchmark/blog_v0_2/README.md`, `docs/basic_usage/deepseek_v3.md`, `docs/basic_usage/gpt_oss.md` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/linters/lychee-ci.toml`; `.github/linters/lychee.toml`; `.github/workflows/lint.yml`; `.github/workflows/nightly-link-check.yml`
  - docs-bench: `benchmark/blog_v0_2/README.md`; `docs/basic_usage/deepseek_v3.md`; `docs/basic_usage/gpt_oss.md`; `docs/developer_guide/contribution_guide.md`; `docs/developer_guide/setup_github_runner.md`; `docs/performance_dashboard/index.html`; `docs/platforms/ascend_contribution_guide.md`; `docs/platforms/ascend_npu.md` 等 15 个文件
  - runtime-model: `.pre-commit-config.yaml`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `814202704` - ci: unify PR test suite naming (#21187)

- 完整 hash: `814202704bf21525b5ae07029cb475da4c87f3b7`
- 时间/作者: 2026-03-23 / Lianmin Zheng
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`, `scripts/ci/utils/slash_command_handler.py`, `test/README.md` 等 283 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/actions/wait-for-jobs/action.yml`; `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`; `test/README.md`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/attention/test_chunk_gated_delta_rule.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py` 等 278 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3f0ba021f` - [AMD] Improve openai/gpt-oss performance (#21020)

- 完整 hash: `3f0ba021fc7e8363c0e878faae4e6db8bfc4141c`
- 时间/作者: 2026-03-21 / kk
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `126cd5cfa` - gpt-oss decode performance optimization (#20392)

- 完整 hash: `126cd5cfae7afbc9c7efb2b00dd52807ff17b842`
- 时间/作者: 2026-03-19 / kk
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/utils.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/utils.py`; `python/sglang/srt/layers/quantization/unquant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d1e95af28` - Upgrade transformers==5.3.0 (#17784)

- 完整 hash: `d1e95af282068a751ee6a8b60a0ae2a90c464819`
- 时间/作者: 2026-03-18 / Xinyuan Tong
- 自动分类: 性能/后端优化
- 主要文件: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py` 等 88 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/layers/rotary_embedding/factory.py`; `python/sglang/srt/managers/tokenizer_manager.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/configs/internvl.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/arcee.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/commandr.py`; `python/sglang/srt/models/dbrx.py` 等 54 个文件
  - runtime-perf: `python/sglang/srt/models/afmoe.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/ernie45_moe_vl.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/granitemoe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 15 个文件
  - tests: `python/sglang/test/runners.py`; `test/registered/core/test_score_api.py`; `test/registered/quant/test_awq.py`; `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/vlm/test_vlm_input_format.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8cdb7e1fd` - [CI] Add GPT-OSS test for SM120 (#20056)

- 完整 hash: `8cdb7e1fd453003474009f4fc041a61930a8ce89`
- 时间/作者: 2026-03-07 / Mohammad Miadh Angkad
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/core/test_gpt_oss_sm120.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/core/test_gpt_oss_sm120.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `759700c80` - Fix SM120 `triton_kernels` MXFP4 `block_k` for GPT-OSS (#20040)

- 完整 hash: `759700c80856cbbef5dccb110860d8b12ecbd180`
- 时间/作者: 2026-03-07 / Mohammad Miadh Angkad
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/mxfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/mxfp4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9305f0e58` - Support `triton_kernels` for GPT-OSS on SM120 (#19718)

- 完整 hash: `9305f0e58dca327bbb3dbd7622405e64d31d4449`
- 时间/作者: 2026-03-03 / Brayden Zhong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/mxfp4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `15af26d1e` - Add aiter attention support in prefill-attention-backend of gpt-oss (#18282)

- 完整 hash: `15af26d1e89932ccac62c3aa3db21562f85ce6ac`
- 时间/作者: 2026-03-02 / kk
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `35ef38c61` - Remove gpt-oss hybrid swa gate for trtllm_mha (#19079)

- 完整 hash: `35ef38c61b2de3ce905836f18cfffd80e56c0a00`
- 时间/作者: 2026-02-28 / Mohammad Miadh Angkad
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `152560d1b` - [PCG] add pcg CI test for gpt-oss model (#18961)

- 完整 hash: `152560d1b9ac26ef45a01fadc6d7b23cfe2d3c22`
- 时间/作者: 2026-02-24 / Kaiqi Jin
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/models/test_gpt_oss_models_pcg.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/models/test_gpt_oss_models_pcg.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `d8d0208c6` - [Feature] rewrite rope kernel; remove flashinfer dependencies (#18844)

- 完整 hash: `d8d0208c6381312e56f7baf72441803509b605bf`
- 时间/作者: 2026-02-21 / DarkSharpness
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/benchmark/bench_rope.py`, `python/sglang/jit_kernel/csrc/elementwise/rope.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/rope.py`, `python/sglang/jit_kernel/tests/test_rope.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/llada2.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
  - runtime-model: `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/llada2.py`; `python/sglang/srt/models/utils.py`
  - runtime-perf: `python/sglang/jit_kernel/benchmark/bench_rope.py`; `python/sglang/jit_kernel/csrc/elementwise/rope.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/rope.py`
  - tests: `python/sglang/jit_kernel/tests/test_rope.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4bffd3a23` - [GPT-OSS] support fp8 online quantization for gpt-oss bf16 (#18988)

- 完整 hash: `4bffd3a2323a332506ce16f0fbd2ce7e96db2204`
- 时间/作者: 2026-02-20 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8290171f5` - [CI] Remove `--mem-fraction-static 0.93` from gpt-oss test (#18869)

- 完整 hash: `8290171f5247061d48ca6545d2e298599db0359c`
- 时间/作者: 2026-02-16 / Mohammad Miadh Angkad
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `88010e960` - [AMD] Fix nightly 1-GPU test failures and bench_serving regression (#18761)

- 完整 hash: `88010e9601bccca6f816984b34f7373ec80778ac`
- 时间/作者: 2026-02-15 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `python/sglang/bench_serving.py`, `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py`, `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - other: `python/sglang/bench_serving.py`
  - tests: `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py`; `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `20554a0a4` - [AMD] rocm 7.2 image release, PR test, Nightly Test (#17799)

- 完整 hash: `20554a0a4fb686dd00ffc83f7e45f12b14210fa6`
- 时间/作者: 2026-02-12 / YC Tseng
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/release-docker-amd-rocm720-nightly-preview.yml`, `docker/rocm720.Dockerfile`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/release-docker-amd-rocm720-nightly-preview.yml`
  - other: `python/sglang/srt/layers/layernorm.py`; `scripts/ci/amd/amd_ci_install_dependency.sh`; `scripts/ci/amd/amd_ci_start_container.sh`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `docker/rocm720.Dockerfile`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`; `python/sglang/srt/layers/quantization/unquant.py`
  - tests: `python/sglang/test/gpt_oss_common.py`; `python/sglang/test/nightly_utils.py`; `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_gsm8k_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_vlms_mmmu_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py` 等 12 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2bd836348` - [PCG] GPT OSS Triton Kernel Support (#18405)

- 完整 hash: `2bd8363486e4c0cf1bc9f09e8e97073588a9684e`
- 时间/作者: 2026-02-11 / Yuwei An
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/compilation/piecewise_context_manager.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `de6a03260` - [docs] fix misspellings & typos (#18276)

- 完整 hash: `de6a03260f59fd33a9eeb8f67e7e6e2cf235a70f`
- 时间/作者: 2026-02-04 / rinbaro
- 自动分类: 缺陷修复
- 主要文件: `docs/advanced_features/dp_for_multi_modal_encoder.md`, `docs/advanced_features/server_arguments.md`, `docs/basic_usage/deepseek_v3.md`, `docs/basic_usage/glmv.md`, `docs/basic_usage/gpt_oss.md`, `docs/basic_usage/sampling_params.md`, `docs/developer_guide/bench_serving.md`, `docs/developer_guide/benchmark_and_profiling.md` 等 18 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/advanced_features/dp_for_multi_modal_encoder.md`; `docs/advanced_features/server_arguments.md`; `docs/basic_usage/deepseek_v3.md`; `docs/basic_usage/glmv.md`; `docs/basic_usage/gpt_oss.md`; `docs/basic_usage/sampling_params.md`; `docs/developer_guide/bench_serving.md`; `docs/developer_guide/benchmark_and_profiling.md` 等 18 个文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `6fd878b41` - [AMD] Add kimi mi35x nightly test, folder organization and several stability fixes (#17895)

- 完整 hash: `6fd878b41df0153bd28f0185920e1b2d9dcc7480`
- 时间/作者: 2026-02-04 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd.yml`, `python/sglang/test/nightly_utils.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v31_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_dp_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_mtp_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_deepseek_v32_tc_eval_amd.py` 等 34 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - tests: `python/sglang/test/nightly_utils.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_r1_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v31_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_dp_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_mtp_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_deepseek_v32_tc_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_gpt_oss_eval_amd.py` 等 33 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `c8da307d7` - feature: adding gpt-oss 120b nightly test (#18134)

- 完整 hash: `c8da307d7e6353fdcfdf6ca1ecb1cec854411230`
- 时间/作者: 2026-02-02 / Douglas Yang
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/8-gpu-models/test_gpt_oss_120b.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `test/registered/8-gpu-models/test_gpt_oss_120b.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `a0bae4c34` - Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299)

- 完整 hash: `a0bae4c34349d09b3ad71db71d4fc3f4f32f221e`
- 时间/作者: 2026-01-31 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py` 等 39 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v32_basic.py`; `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v3_basic.py`; `test/registered/8-gpu-models/test_deepseek_v3_mtp.py` 等 37 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `38d275a9f` - [BugFix] fix gpt-oss accuracy issue when enabling piecewise cuda graph (#18013)

- 完整 hash: `38d275a9fd7c42353839b88ce83359444fb3cb6c`
- 时间/作者: 2026-01-31 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/managers/schedule_batch.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/schedule_batch.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `ef1c51275` - Add aiter bias moe support in gpt-oss mxfp4 model (#17735)

- 完整 hash: `ef1c5127545ed9ee26c9d3ba0f55ce370c4c247d`
- 时间/作者: 2026-01-29 / kk
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/mxfp4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f8636fbb2` - [AMD] Add Kimi-K2, DeepSeek-V3.2 tests to nightly CI (#17523)

- 完整 hash: `f8636fbb253a83d268ffa1636eac4e111966376c`
- 时间/作者: 2026-01-28 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py` 等 27 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_dp_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_v32_mtp_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok2_eval_mi35x.py` 等 26 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `6c0f9b482` - Add test_gpt_oss_4gpu.py to B200 test suite (#17743)

- 完整 hash: `6c0f9b4824acce6ed6394baf00606839b3216750`
- 时间/作者: 2026-01-26 / Alison Shao
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `fb683be6e` - Use attn tp group in embedding for more models (#17570)

- 完整 hash: `fb683be6eb7c6960f3d37ea91ca836c1b8e4120c`
- 时间/作者: 2026-01-24 / Ke Bao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py`, `python/sglang/srt/models/glm4.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/models/gpt_oss.py` 等 19 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/falcon_h1.py`; `python/sglang/srt/models/glm4.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/llada2.py`; `python/sglang/srt/models/llama4.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/bailing_moe_nextn.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/glm4_moe_lite.py`; `python/sglang/srt/models/glm4_moe_nextn.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 10 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2b2f31738` - fix gpt-oss launch failure with piecewise cuda graph (#17532)

- 完整 hash: `2b2f317383a451d8ec944bea3ee1da659b4421c6`
- 时间/作者: 2026-01-22 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - 未记录文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `61abff66c` - [NPU] [Bug Fix] Fix typo in npu device check in gpt_oss.py (#17553)

- 完整 hash: `61abff66c150b559517f25a769f4740e23bbdefa`
- 时间/作者: 2026-01-22 / Chandrakant Khandelwal
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/gpt_oss.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/gpt_oss.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9be2a3a9a` - Remove test_gpt_oss_4gpu.py from __not_in_ci__ (keep in per-commit-4-gpu) (#17534)

- 完整 hash: `9be2a3a9a332978641b6af29004d14c21d271d7f`
- 时间/作者: 2026-01-21 / Alison Shao
- 自动分类: 测试/文档/基准
- 主要文件: `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `85d9af51d` - Temporarily disable flaky test_gpt_oss_4gpu.py on B200 (#17528)

- 完整 hash: `85d9af51da7e898748743f3d105e299b9e6d16ec`
- 时间/作者: 2026-01-21 / Alison Shao
- 自动分类: 测试/文档/基准
- 主要文件: `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `d725487dc` - Disable swa memory for gpt-oss with spec (#17517)

- 完整 hash: `d725487dc8eaa56eaef39d248d46b2cc1c678b27`
- 时间/作者: 2026-01-22 / Ke Bao
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `733de6be3` - [NPU]Support GPT-OSS for NPU (#14197)

- 完整 hash: `733de6be31e20242421ea5cbc2a66582711d33f0`
- 时间/作者: 2026-01-19 / Todobe
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`; `python/sglang/srt/layers/quantization/unquant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e499258e9` - Use swa radix cache and memory pool for gpt-oss model (#17261)

- 完整 hash: `e499258e97ec45a92e631a455bf1cd4000409c10`
- 时间/作者: 2026-01-18 / Ke Bao
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/utils.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/utils.py`; `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `146b5fcc8` - [CI] Reorganize stage-b 1-GPU tests for 5090 compatibility (#16826)

- 完整 hash: `146b5fcc84101123baf743eb9480ad7ce60a0e92`
- 时间/作者: 2026-01-15 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_mamba_unittest.py`, `test/registered/attention/test_radix_attention.py`, `test/registered/attention/test_radix_cache_unit.py`, `test/registered/attention/test_swa_unittest.py`, `test/registered/attention/test_torch_native_attention_backend.py` 等 136 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/slash_command_handler.py`
  - tests: `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_mamba_unittest.py`; `test/registered/attention/test_radix_attention.py`; `test/registered/attention/test_radix_cache_unit.py`; `test/registered/attention/test_swa_unittest.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py`; `test/registered/attention/test_triton_attention_kernels.py` 等 134 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3d72944fb` - [Doc] Add tip on how to use Spec V2 (#15455)

- 完整 hash: `3d72944fb89842672cf9d663228663e05096d8c6`
- 时间/作者: 2026-01-15 / b8zhong
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/basic_usage/deepseek_v3.md`, `docs/basic_usage/glm45.md`, `docs/basic_usage/gpt_oss.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/basic_usage/deepseek_v3.md`; `docs/basic_usage/glm45.md`; `docs/basic_usage/gpt_oss.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b025cff44` - [AMD] Add AMD CI registration (1-gpu unit test) to nightly CI.  (#16941)

- 完整 hash: `b025cff441e187646b5bed6dbaf6152a1dd11522`
- 时间/作者: 2026-01-13 / Michael
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_grok2_eval_mi35x.py`, `test/registered/amd/accuracy/test_deepseek_r1_eval_amd.py`, `test/registered/amd/accuracy/test_deepseek_v31_eval_amd.py` 等 39 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok1_int4_eval_mi35x.py`; `test/registered/amd/accuracy/mi35x/test_grok2_eval_mi35x.py`; `test/registered/amd/accuracy/test_deepseek_r1_eval_amd.py`; `test/registered/amd/accuracy/test_deepseek_v31_eval_amd.py`; `test/registered/amd/accuracy/test_gpt_oss_eval_amd.py` 等 38 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `cc25f9df5` - Update est_time for stage-b-test-small-1-gpu tests (#16835)

- 完整 hash: `cc25f9df50e1578dd4313004f2f15a501b4c8337`
- 时间/作者: 2026-01-10 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_deterministic.py`, `test/registered/core/test_gpt_oss_1gpu.py`, `test/registered/cuda_graph/test_piecewise_cuda_graph_small_1_gpu.py`, `test/registered/dllm/test_llada2_mini.py`, `test/registered/hicache/test_hicache_variants.py`, `test/registered/lora/test_lora_update.py` 等 24 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_deterministic.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/cuda_graph/test_piecewise_cuda_graph_small_1_gpu.py`; `test/registered/dllm/test_llada2_mini.py`; `test/registered/hicache/test_hicache_variants.py`; `test/registered/lora/test_lora_update.py` 等 24 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `a2c2c09d7` - [BugFix] fix gpt-oss-120b launch failure with --enable-piecewise-cuda-graph (#16757)

- 完整 hash: `a2c2c09d7d2e146235a9f985b20375f6efa66c98`
- 时间/作者: 2026-01-10 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/mxfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/mxfp4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d27f16f38` - Fix EPLB + FP4 Quantization Compatibility Issue (#13715)

- 完整 hash: `d27f16f38a6f23e5a7c529c6f052ac11f28c4a97`
- 时间/作者: 2026-01-10 / Shifang Xu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/longcat_flash.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/gpt_oss.py`
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4e999404c` - [AMD] Fix CI - unit-test-backend-1-gpu-amd-mi35x and unit-test-backend-2-gpu-amd, stage-b-test-small-1-gpu-amd (#16675)

- 完整 hash: `4e999404c3361a64a2147988380270cfb4fd394c`
- 时间/作者: 2026-01-09 / YC Tseng
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-amd.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_radix_attention.py`, `test/registered/attention/test_swa_unittest.py`, `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/attention/test_triton_attention_backend.py`, `test/registered/attention/test_triton_attention_kernels.py` 等 60 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-amd.yml`
  - other: `scripts/ci/slash_command_handler.py`
  - tests: `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_radix_attention.py`; `test/registered/attention/test_swa_unittest.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py`; `test/registered/attention/test_triton_attention_kernels.py`; `test/registered/attention/test_triton_sliding_window.py`; `test/registered/backends/test_torch_compile.py` 等 58 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `0c474273c` - Fix gpt_oss_common import path and migrate core tests (#16426)

- 完整 hash: `0c474273c514e048ea4dc3477e74c8fd085dd2db`
- 时间/作者: 2026-01-07 / Alison Shao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/test/gpt_oss_common.py`, `test/registered/core/test_deterministic.py`, `test/registered/core/test_gpt_oss_1gpu.py`, `test/registered/core/test_hidden_states.py`, `test/registered/core/test_input_embeddings.py`, `test/registered/core/test_io_struct.py`, `test/registered/core/test_model_hooks.py`, `test/registered/core/test_page_size.py` 等 15 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/gpt_oss_common.py`; `test/registered/core/test_deterministic.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_hidden_states.py`; `test/registered/core/test_input_embeddings.py`; `test/registered/core/test_io_struct.py`; `test/registered/core/test_model_hooks.py`; `test/registered/core/test_page_size.py` 等 15 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3dfff6ae3` - Eagle: GPT-OSS Eagle v2 support (#14920)

- 完整 hash: `3dfff6ae3c338f0a56816bd254e8d3292f8e1e1b`
- 时间/作者: 2025-12-30 / Izzy Putterman
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/speculative/eagle_worker.py`
  - runtime-perf: `python/sglang/srt/model_executor/cuda_graph_runner.py`; `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `989d4b301` - [CI] Migrate nightly tests to test/registered/ (#15582)

- 完整 hash: `989d4b301293ea8eb243d7c320c5c457cb718629`
- 时间/作者: 2025-12-22 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/vlm_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/run_combined_tests.py` 等 64 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/ascend/__init__.py`; `python/sglang/test/ascend/gsm8k_ascend_mixin.py`; `python/sglang/test/ascend/vlm_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/run_combined_tests.py`; `test/registered/8-gpu-models/test_deepseek_v31.py` 等 63 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `bed301a5a` - [Feature] Enable return routed experts (#12162)

- 完整 hash: `bed301a5acaa9577c9aa706468bdf242f6a43051`
- 时间/作者: 2025-12-21 / Junrong Lin
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/bench_serving.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/routed_experts_capturer.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/schedule_batch.py` 等 27 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/bench_serving.py`; `python/sglang/srt/managers/detokenizer_manager.py`; `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/managers/multi_tokenizer_mixin.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-model: `python/sglang/srt/entrypoints/engine.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/ernie4.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/grok.py`; `python/sglang/srt/models/hunyuan.py` 等 10 个文件
  - runtime-perf: `python/sglang/srt/layers/moe/routed_experts_capturer.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_output_processor_mixin.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`
  - tests: `python/sglang/test/test_utils.py`; `test/srt/rl/test_return_routed_experts.py`; `test/srt/run_suite.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
