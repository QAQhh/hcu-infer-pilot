# sglang Shared Framework Commits 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `.codespellrc` | 无直接提交 |
| `.coveragerc` | 无直接提交 |
| `.dockerignore` | 无直接提交 |
| `.github/CI_PERMISSIONS.json` | 无直接提交 |
| `.github/CODEOWNERS` | 无直接提交 |
| `.github/FOLDER_README.md` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/1-bug-report.yml` | 无直接提交 |
| `.github/ISSUE_TEMPLATE/2-feature-request.yml` | 无直接提交 |
| `.github/MAINTAINER.md` | 无直接提交 |
| `.github/actions/check-maintenance/action.yml` | `176c8e7b0` |
| `.github/actions/check-stage-health/action.yml` | `17f43d151` |
| `.github/actions/upload-cuda-coredumps/action.yml` | 无直接提交 |
| `.github/actions/wait-for-jobs/action.yml` | 无直接提交 |
| `.github/labeler.yml` | 无直接提交 |
| `.github/linters/lychee-ci.toml` | 无直接提交 |
| `.github/linters/lychee.toml` | 无直接提交 |
| `.github/pull_request_template.md` | 无直接提交 |
| `.github/update_ci_permission.py` | 无直接提交 |
| `.github/workflows/amd-aiter-scout.yml` | 无直接提交 |
| `.github/workflows/amd-ci-job-monitor.yml` | 无直接提交 |
| `.github/workflows/auto-tune.yml` | 无直接提交 |
| `.github/workflows/bot-bump-flashinfer-version.yml` | 无直接提交 |
| `.github/workflows/bot-bump-kernel-version-to-sglang.yml` | 无直接提交 |
| `.github/workflows/bot-bump-kernel-version.yml` | 无直接提交 |
| `.github/workflows/bot-bump-sglang-version.yml` | 无直接提交 |
| `.github/workflows/bot-cherry-pick.yml` | 无直接提交 |
| `.github/workflows/cancel-pr-workflow-on-merge.yml` | 无直接提交 |
| `.github/workflows/cancel-unfinished-pr-tests.yml` | 无直接提交 |
| `.github/workflows/ci-coverage-overview.yml` | 无直接提交 |
| `.github/workflows/ci-failure-monitor.yml` | 无直接提交 |
| `.github/workflows/close-inactive-issues.yml` | 无直接提交 |
| `.github/workflows/execute-notebook.yml` | 无直接提交 |
| `.github/workflows/labeler.yml` | 无直接提交 |
| `.github/workflows/lint.yml` | 无直接提交 |
| `.github/workflows/list-active-pr-runs.yml` | 无直接提交 |
| `.github/workflows/nightly-link-check.yml` | 无直接提交 |
| `.github/workflows/nightly-release-gateway.yml` | 无直接提交 |
| `.github/workflows/nightly-test-amd-rocm720.yml` | 无直接提交 |
| `.github/workflows/nightly-test-amd.yml` | 无直接提交 |
| `.github/workflows/nightly-test-intel.yml` | 无直接提交 |
| `.github/workflows/nightly-test-npu.yml` | `f289d173a` |
| `.github/workflows/nightly-test-nvidia.yml` | `176c8e7b0`, `bb2989368` |
| `.github/workflows/open-pr-copy-from-oss.yml` | 无直接提交 |
| `.github/workflows/open-pr-copy-to-oss.yml` | 无直接提交 |
| `.github/workflows/patch-docker-dev.yml` | 无直接提交 |
| `.github/workflows/pr-benchmark-rust.yml` | 无直接提交 |
| `.github/workflows/pr-gate.yml` | 无直接提交 |
| `.github/workflows/pr-test-amd-rocm720.yml` | `7ca015fe6` |
| `.github/workflows/pr-test-amd.yml` | `013fa5563`, `7ca015fe6` |
| `.github/workflows/pr-test-jit-kernel.yml` | `17f43d151`, `176c8e7b0`, `bb2989368` |
| `.github/workflows/pr-test-multimodal-gen.yml` | `17f43d151`, `176c8e7b0` |
| `.github/workflows/pr-test-npu.yml` | `8febc3650` |
| `.github/workflows/pr-test-rust.yml` | 无直接提交 |
| `.github/workflows/pr-test-sgl-kernel.yml` | `17f43d151`, `176c8e7b0` |
| `.github/workflows/pr-test-xeon.yml` | 无直接提交 |
| `.github/workflows/pr-test-xpu.yml` | 无直接提交 |
| `.github/workflows/pr-test.yml` | `17f43d151`, `7ca015fe6`, `176c8e7b0` |
| `.github/workflows/release-branch-cut.yml` | `17f43d151` |
| `.github/workflows/release-docker-amd-nightly.yml` | 无直接提交 |
| `.github/workflows/release-docker-amd-rocm720-nightly.yml` | 无直接提交 |
| `.github/workflows/release-docker-amd.yml` | 无直接提交 |
| `.github/workflows/release-docker-cu13-framework.yml` | 无直接提交 |
| `.github/workflows/release-docker-dev.yml` | 无直接提交 |
| `.github/workflows/release-docker-gateway.yml` | 无直接提交 |
| `.github/workflows/release-docker-npu-nightly.yml` | 无直接提交 |
| `.github/workflows/release-docker-npu.yml` | 无直接提交 |
| `.github/workflows/release-docker-xeon.yml` | 无直接提交 |
| `.github/workflows/release-docker.yml` | 无直接提交 |
| `.github/workflows/release-docs.yml` | 无直接提交 |
| `.github/workflows/release-pypi-gateway.yml` | 无直接提交 |
| `.github/workflows/release-pypi-nightly.yml` | 无直接提交 |
| `.github/workflows/release-pypi-pr.yml` | 无直接提交 |
| `.github/workflows/release-pypi.yml` | 无直接提交 |
| `.github/workflows/release-tag.yml` | 无直接提交 |
| `.github/workflows/release-whl-kernel.yml` | 无直接提交 |
| `.github/workflows/rerun-ut.yml` | `176c8e7b0` |
| `.github/workflows/retag-docker.yml` | 无直接提交 |
| `.github/workflows/runner-utilization.yml` | 无直接提交 |
| `.github/workflows/slash-command-handler.yml` | 无直接提交 |
| `.github/workflows/stress-test.yml` | 无直接提交 |
| ... | 2951 more files omitted from table; all were used for git tracing. |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 80
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-05-18 | `5a00fbb22` | 性能/后端优化 | 删除多余代码 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_profiler_mixin.py` |
| 2026-05-18 | `dea82e2bc` | 调度/缓存/PD | 去掉无关的代码及注释 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py` |
| 2026-05-18 | `ce4be7d18` | 性能/后端优化 | hicache功能适配 | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py` |
| 2026-05-09 | `55a72732c` | 性能/后端优化 | fix(dcu): 修复HiCache kernel路径访问host pointer导致的VMFault | `sgl-kernel/csrc/kvcacheio/transfer.cu` |
| 2026-05-06 | `5a811d1de` | 调度/缓存/PD | 修改transfer_kv_all_direct_pf_lf_H2D_dcu参数 | `python/sglang/srt/mem_cache/memory_pool_host.py` |
| 2026-04-18 | `ec7e2e859` | 性能/后端优化 | 提交本地修改的hicache | `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-05-18 | `9555bc282` | 性能/后端优化 | 修改launch_chunk_fwd_kernel_o算子传参 | `python/sglang/srt/layers/attention/fla/chunk_o.py` |
| 2026-05-18 | `162699fac` | 性能/后端优化 | [opt]fused_mamba_state_scatter_with_mask算子优化 | `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py` |
| 2026-05-18 | `d32a79c65` | 性能/后端优化 | 修改aiter prefill阶段的fla算子传参 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/fla/chunk_o.py` |
| 2026-05-16 | `4816b3f21` | 性能/后端优化 | [BUG FIX] add missing argument in aiter block fp8 moe | `python/sglang/srt/layers/quantization/fp8.py` |
| 2026-05-15 | `5daf25b16` | 性能/后端优化 | [feat]适配aiter moe fp8_w8a8 | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-05-14 | `0474160f8` | 性能/后端优化 | [BUG FIX] RadixAttention should not be skipped regardless of ignore list | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-05-13 | `bd06359df` | 性能/后端优化 | [fix]: SlimQuantW4A8Int8MarlinMoEMethod增加必要的形参 | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-05-14 | `7b06a6e59` | 缺陷修复 | 修复seq_lens前后不一致，导致开mtp时block_table索引计算有问题，进而导致临界状态传参错误造成vmfault的问题 | `python/sglang/srt/layers/attention/dcu_mla_backend.py` |
| 2026-05-14 | `87d24d36b` | 性能/后端优化 | [bugfix]fix aiter_chunk_gated_delta_rule_fwd_kernel_h_blockdim64函数传参错误，解决qw3.5-35b,qw3.6-35b的精度问题 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` |
| 2026-05-13 | `06751b190` | 性能/后端优化 | [feat]lightop不支持的moe size转到aiter进行支持 | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` |
| 2026-05-14 | `5d71e7e7a` | 性能/后端优化 | fix some error in initial version | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-05-13 | `1b7bdda04` | 性能/后端优化 | [feat]修改chunk_gated_delta_rule_fwd_kernel_h_blockdim64算子的import 路径从而适配新版本aiter | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` |
| 2026-05-12 | `423d7d102` | 缺陷修复 | [BUG FIX] eliminate trace bubbles in MTP graph reply stage by avoiding implicit conversion | `python/sglang/srt/layers/attention/triton_backend.py` |
| 2026-05-08 | `8401bfecf` | 通用实现调整 | 接入causal_conv1d_fn_dcu算子实现 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-05-08 | `2e6a7a94d` | 性能/后端优化 | 增加aiter的fused_sigmoid_gating_delta_rule_update算子实现 | `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` |
| 2026-05-07 | `3c1dba355` | 性能/后端优化 | 修复slimquant_w4a8中blaslt路径的量化算子调用与权重布局 | `python/sglang/srt/layers/quantization/slimquant_w4a8.py` |
| 2026-05-06 | `dfb359973` | 性能/后端优化 | 修改调用aiter的chunk_gated_delta_rule_fwd算子方法 | `python/sglang/srt/layers/attention/fla/chunk.py`, `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` |
| 2026-04-29 | `b80efea17` | 性能/后端优化 | 修改w4a8重排逻辑，适配deepgemm新包 | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/layers/quantization/w4a8_utils.py` |
| 2026-04-28 | `16df9541d` | 性能/后端优化 | fix(量化): 规范 W8A8 与 Marlin MoE 处理逻辑 | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` |
| 2026-04-24 | `f34ecd7de` | 性能/后端优化 | [BUG FIX] fix CUDA graph grid undercoverage in multi-layer EAGLE MTP draft extend | `python/sglang/srt/layers/attention/triton_backend.py` |
| 2026-04-22 | `c4c4c2148` | 性能/后端优化 | 修复fused_recurrent_gated_delta_rule_packed_decode报错问题 | `python/sglang/srt/layers/attention/fla/fused_recurrent.py` |
| 2026-04-22 | `39474e90b` | 性能/后端优化 | [feature] linear attn fused_recurrent_gated_delta_rule_packed_decode use aiter | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/fla/chunk.py`, `python/sglang/srt/layers/attention/fla/fused_recurrent.py` |
| 2026-04-22 | `c840dd8e7` | 性能/后端优化 | [FEAT] update triton extend fwd via aiter | `python/sglang/srt/layers/attention/triton_backend.py` |
| 2026-04-21 | `fe965ea9e` | 性能/后端优化 | [feature] linear attn chunk_gated_delta_rule_fwd_h use aiter | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/fla/chunk.py` |
| 2026-04-17 | `1221130a1` | 性能/后端优化 | add aiter moe w4a8 support | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-04-16 | `cd511513d` | 性能/后端优化 | [FEAT] enable fp8 shuffle weight for asm moe | `python/sglang/srt/layers/quantization/fp8.py` |
| 2026-04-16 | `a9965e61f` | 性能/后端优化 | adjust aiter_moe para order and w1_zp&w2_zp opt | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` |
| 2026-04-16 | `e2ae2a431` | 通用实现调整 | 修改 pyproject.toml 中的huggingface_hub版本 | `python/pyproject.toml` |
| 2026-04-16 | `82a13cc79` | 缺陷修复 | fix: 修改 pyproject.toml 中的依赖版本 | `python/pyproject.toml` |
| 2026-04-15 | `41d14b7c6` | 性能/后端优化 | [FEAT] support FP8 MoE via aiter ASM kernel | `python/sglang/srt/layers/quantization/fp8.py` |
| 2026-04-15 | `fdf368589` | 性能/后端优化 | fix: 修复bmz上flash_mla不支持fp8 | `python/sglang/srt/layers/attention/dcu_mla_backend.py` |
| 2026-04-15 | `07469199b` | 性能/后端优化 | dpsk fp8适配fuse_moe_fp8_w8a8 | `python/sglang/srt/layers/quantization/w8a8_fp8.py` |
| 2026-04-14 | `3a8cd31f5` | 性能/后端优化 | add aiter moe w4f16 support | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py` |
| 2026-04-14 | `7859b2885` | 性能/后端优化 | [BUG FIX] fix nn transpose error for fp8 blockwise linear | `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-04-09 | `aa77e2522` | 缺陷修复 | Bugfix:fix mm model attention interface | `python/sglang/srt/layers/attention/vision.py` |
| 2026-04-07 | `e91aa8029` | 性能/后端优化 | 接入causal_conv1d_update优化算子 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-04-07 | `518582021` | 性能/后端优化 | fix deepseek log cudagraph init meta data copy error in bmz when capture cudagraph. | `python/sglang/srt/layers/attention/dcu_mla_backend.py` |
| 2026-04-02 | `95a02a38d` | 调度/缓存/PD | Update README_DCU.md | `README_DCU.md` |
| 2026-04-02 | `80cbcce8e` | 调度/缓存/PD | Update README_DCU.md | `README_DCU.md` |
| 2026-04-02 | `71cd1e550` | 调度/缓存/PD | Update README_DCU.md | `README_DCU.md` |
| 2026-04-02 | `a510541b9` | 调度/缓存/PD | Update README_DCU.md | `README_DCU.md` |
| 2026-04-01 | `e32b8b387` | 性能/后端优化 | optimized code of layernorm | `python/sglang/srt/layers/layernorm.py` |
| 2026-04-01 | `c87293f3a` | 性能/后端优化 | 修复融合算子并验证精度. | `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` |
| 2026-04-01 | `4418f4abb` | 性能/后端优化 | 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现 | `python/sglang/srt/layers/layernorm.py` |
| 2026-04-01 | `790dbca3a` | 性能/后端优化 | Revert "适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现" | `python/sglang/srt/layers/layernorm.py` |
| 2026-04-01 | `ec19cdf61` | 性能/后端优化 | 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现 | `python/sglang/srt/layers/layernorm.py` |
| 2026-04-01 | `23329122c` | 性能/后端优化 | 适配lightop的gemma_fused_add_rmsnorm算子 | `python/sglang/srt/layers/layernorm.py` |
| 2026-03-27 | `9b0c470a6` | 缺陷修复 | fix(security): replace unsafe pickle.loads with SafeUnpickler for CVE-2026-3989 (#20904) | `docs/developer_guide/contribution_guide.md`, `python/sglang/srt/utils/common.py`, `scripts/playground/replay_request_dump.py` |
| 2026-03-26 | `192ba2c4e` | 调度/缓存/PD | [Security] 1/N: Bind ZMQ sockets to localhost to prevent unauthenticated remote access (#21435) | `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/utils/network.py` |
| 2026-03-27 | `2e65c27b2` | 调度/缓存/PD | Api add flush cache timeout (#21413) | `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-03-26 | `be0cca559` | 模型支持/运行时入口 | Use torch.addmm instead of separate mm and add_ calls for LoRA torch.native (#20562) | `python/sglang/srt/lora/backend/torch_backend.py`, `python/sglang/srt/lora/torch_ops/lora_ops.py` |
| 2026-03-26 | `e59ea4f6e` | 缺陷修复 | fix: torch-native LoRA for multi-adapter case (#20564) | `python/sglang/srt/lora/backend/torch_backend.py`, `test/manual/lora/test_torch_backend.py` |
| 2026-03-26 | `e5dd411f6` | 模型支持/运行时入口 | [CI] Add ci-workflow-guide skill and consolidate CI docs (#21429) | `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `test/README.md` |
| 2026-03-26 | `e5b765035` | 缺陷修复 | Fix UnboundLocalError when DetokenizerManager constructor fails (#21471) | `python/sglang/srt/managers/detokenizer_manager.py` |
| 2026-03-26 | `17f43d151` | 性能/后端优化 | [CI] Skip stage health check for release branch cut (#21488) | `.github/actions/check-stage-health/action.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test-multimodal-gen.yml` |
| 2026-03-26 | `8febc3650` | 调度/缓存/PD | [NPU] multimodal-gen-test-8-npu-a3,Cache pytorch dependency (#21470) | `.github/workflows/pr-test-npu.yml` |
| 2026-03-26 | `013fa5563` | 缺陷修复 | [AMD] CI - fix amd 4-GPU PR test (#21444) | `.github/workflows/pr-test-amd.yml` |
| 2026-03-26 | `f289d173a` | 测试/文档/基准 | [Deps] Bump xgrammar to 0.1.32 (#21032) | `.github/workflows/nightly-test-npu.yml`, `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml` |
| 2026-03-26 | `fd535942a` | 性能/后端优化 | [AMD]Integrate aiter's fused_topk for softmax scoring in topk function (#21421) | `python/sglang/srt/layers/moe/topk.py` |
| 2026-03-26 | `a30596415` | 调度/缓存/PD | [MLX] Add native MLX execution backend for Apple Silicon Mac (#20342) | `python/pyproject_other.toml`, `python/sglang/bench_one_batch.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py` |
| 2026-03-26 | `7ca015fe6` | 性能/后端优化 | [Diffusion] Refactor diffusion JIT kernel test layout and narrow CI triggers (#21385) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml` |
| 2026-03-25 | `79db3bec3` | 模型支持/运行时入口 | [CI] Add PID namespace and ps auxf diagnostics to killall.py (#21401) | `python/sglang/cli/killall.py` |
| 2026-03-25 | `176c8e7b0` | 性能/后端优化 | [CI] Simplify CI check actions and add maintenance gate to rerun-ut (#21455) | `.github/actions/check-maintenance/action.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test-jit-kernel.yml` |
| 2026-03-26 | `f14260840` | 模型支持/运行时入口 | [MUSA] apply_vocab_mask support musa device (#21296) | `python/sglang/srt/constrained/xgrammar_backend.py` |
| 2026-03-26 | `f420b9b4a` | 性能/后端优化 | [MUSA][Feature] Enable Piecewise CUDA Graph support for MUSA platform (#20758) | `python/sglang/srt/compilation/weak_ref_tensor.py`, `python/sglang/srt/server_args.py` |
| 2026-03-26 | `abf4f1a47` | 模型支持/运行时入口 | [MPS] Add StreamContext stub (#20782) | `python/sglang/_mps_stub.py` |
| 2026-03-26 | `02521420b` | 模型支持/运行时入口 | [MPS] Support sglang.check_env (#20753) | `python/sglang/check_env.py` |
| 2026-03-26 | `d9e96153d` | 调度/缓存/PD | [NPU] Support Hybrid KV Cache for Ascend backend (#18032) | `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-03-26 | `bb2989368` | 性能/后端优化 | [Fix] Try to fix nvcc compilation error (#21246) | `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `python/sglang/jit_kernel/all_reduce.py` |
| 2026-03-25 | `a34e9ed64` | 模型支持/运行时入口 | Add adjusted_filter_batch (#21260) | `python/sglang/srt/sampling/sampling_batch_info.py` |
| 2026-03-25 | `53c1d8e96` | 缺陷修复 | Fix customized_info offset truncation (#21262) | `python/sglang/srt/managers/scheduler_output_processor_mixin.py` |
| 2026-03-25 | `1100b9865` | 性能/后端优化 | Fix MxInt4 MoE returning wrong output variable (#21348) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py` |
| 2026-03-25 | `662635e7a` | 性能/后端优化 | fix(sgl-kernel): align wheel METADATA/WHEEL with +cu filename (#21437) | `sgl-kernel/rename_wheels.sh` |
| 2026-03-25 | `80389fec0` | 缺陷修复 | [AMD] Fix AMD CI: mark /sglang-checkout as git safe.directory in container (#21423) | `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh` |

## 逐 Commit 审计卡

### Commit `5a00fbb22` - 删除多余代码

- 完整 hash: `5a00fbb22ffdc69b5b13abecabd5a5f111fe328f`
- 时间/作者: 2026-05-18 / shangxl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_profiler_mixin.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/session_aware_cache.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_profiler_mixin.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/session_aware_cache.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py` 等 9 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `dea82e2bc` - 去掉无关的代码及注释

- 完整 hash: `dea82e2bc5991147fae3eec4c5b1589e88a00ae4`
- 时间/作者: 2026-05-18 / shangxl
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/radix_cache.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ce4be7d18` - hicache功能适配

- 完整 hash: `ce4be7d186e131497c0586a32ed18345a79f4a93`
- 时间/作者: 2026-05-18 / shangxl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/kvcacheio/transfer.cu`, `sgl-kernel/include/sgl_kernel_ops.h`, `sgl-kernel/python/sgl_kernel/kvcacheio.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/csrc/kvcacheio/transfer.cu`; `sgl-kernel/include/sgl_kernel_ops.h`; `sgl-kernel/python/sgl_kernel/kvcacheio.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `55a72732c` - fix(dcu): 修复HiCache kernel路径访问host pointer导致的VMFault

- 完整 hash: `55a72732c41836b8e672ce02a6af9ffcee0b5817`
- 时间/作者: 2026-05-09 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `sgl-kernel/csrc/kvcacheio/transfer.cu`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `sgl-kernel/csrc/kvcacheio/transfer.cu`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5a811d1de` - 修改transfer_kv_all_direct_pf_lf_H2D_dcu参数

- 完整 hash: `5a811d1ded746b54d5b8877d307d83aa0f5dc1f5`
- 时间/作者: 2026-05-06 / shangxl
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/mem_cache/memory_pool_host.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool_host.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ec7e2e859` - 提交本地修改的hicache

- 完整 hash: `ec7e2e8595a8bd4df2cc191ec3fcca11a9610bc0`
- 时间/作者: 2026-04-18 / niuhb
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_profiler_mixin.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`; `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_profiler_mixin.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/radix_cache.py` 等 14 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9555bc282` - 修改launch_chunk_fwd_kernel_o算子传参

- 完整 hash: `9555bc28286e08db74dce900900b5ccf86ca0715`
- 时间/作者: 2026-05-18 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_o.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_o.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `162699fac` - [opt]fused_mamba_state_scatter_with_mask算子优化

- 完整 hash: `162699fac22b3bb750671b4d537c63c3a8e95a56`
- 时间/作者: 2026-05-18 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d32a79c65` - 修改aiter prefill阶段的fla算子传参

- 完整 hash: `d32a79c65c752b8432983b083a82bf20c8ae7796`
- 时间/作者: 2026-05-18 / liucong8560
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/fla/chunk_o.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/attention/fla/chunk_o.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4816b3f21` - [BUG FIX] add missing argument in aiter block fp8 moe

- 完整 hash: `4816b3f21e57d9804bf01c25db48c28760976508`
- 时间/作者: 2026-05-16 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5daf25b16` - [feat]适配aiter moe fp8_w8a8

- 完整 hash: `5daf25b168a9182e660225f68d45f1d2b481d3b6`
- 时间/作者: 2026-05-15 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0474160f8` - [BUG FIX] RadixAttention should not be skipped regardless of ignore list

- 完整 hash: `0474160f8eaeab06e5e1d8affe352685d4ce8cdd`
- 时间/作者: 2026-05-14 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bd06359df` - [fix]: SlimQuantW4A8Int8MarlinMoEMethod增加必要的形参

- 完整 hash: `bd06359df6a612e029eb8c0f28dcf861d8e2b22f`
- 时间/作者: 2026-05-13 / wujl5
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7b06a6e59` - 修复seq_lens前后不一致，导致开mtp时block_table索引计算有问题，进而导致临界状态传参错误造成vmfault的问题

- 完整 hash: `7b06a6e593db9cead379d6d9542e4c29f6830a73`
- 时间/作者: 2026-05-14 / lipenghui
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `87d24d36b` - [bugfix]fix aiter_chunk_gated_delta_rule_fwd_kernel_h_blockdim64函数传参错误，解决qw3.5-35b,qw3.6-35b的精度问题

- 完整 hash: `87d24d36b9271ee6fd27fe640b203cff4bb0d8c3`
- 时间/作者: 2026-05-14 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `06751b190` - [feat]lightop不支持的moe  size转到aiter进行支持

- 完整 hash: `06751b1909d13c17500c59f5ae3621915e8704b5`
- 时间/作者: 2026-05-13 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5d71e7e7a` - fix some error in initial version

- 完整 hash: `5d71e7e7ab11e7b760fba5e33f1dbeff30b35ba8`
- 时间/作者: 2026-05-14 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1b7bdda04` - [feat]修改chunk_gated_delta_rule_fwd_kernel_h_blockdim64算子的import 路径从而适配新版本aiter

- 完整 hash: `1b7bdda04720df5a0ecd25964939f90e7417137d`
- 时间/作者: 2026-05-13 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `423d7d102` - [BUG FIX] eliminate trace bubbles in MTP graph reply stage by avoiding implicit conversion

- 完整 hash: `423d7d102b5cc7490cd0919a419ab111b02f8bf5`
- 时间/作者: 2026-05-12 / shiqiang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8401bfecf` - 接入causal_conv1d_fn_dcu算子实现

- 完整 hash: `8401bfecf28117841d8798e4bdc57c294b1434fe`
- 时间/作者: 2026-05-08 / liucong
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2e6a7a94d` - 增加aiter的fused_sigmoid_gating_delta_rule_update算子实现

- 完整 hash: `2e6a7a94d930dbcfa46bc3941cc8343ff8e66be6`
- 时间/作者: 2026-05-08 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3c1dba355` - 修复slimquant_w4a8中blaslt路径的量化算子调用与权重布局

- 完整 hash: `3c1dba35570e7261a6bf39a26837c7b8907c7b5f`
- 时间/作者: 2026-05-07 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `dfb359973` - 修改调用aiter的chunk_gated_delta_rule_fwd算子方法

- 完整 hash: `dfb359973e5195d09817137c2a1b4740195f8d7e`
- 时间/作者: 2026-05-06 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/chunk.py`, `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk.py`; `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b80efea17` - 修改w4a8重排逻辑，适配deepgemm新包

- 完整 hash: `b80efea17de96dc59b81b5ebf9f8d1fa1ad55501`
- 时间/作者: 2026-04-29 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/layers/quantization/w4a8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`; `python/sglang/srt/layers/quantization/w4a8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `16df9541d` - fix(量化): 规范 W8A8 与 Marlin MoE 处理逻辑

- 完整 hash: `16df9541d2c0d36afb21179d106f26462d495c0f`
- 时间/作者: 2026-04-28 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f34ecd7de` - [BUG FIX] fix CUDA graph grid undercoverage in multi-layer EAGLE MTP draft extend

- 完整 hash: `f34ecd7def554d51e627783eb8f5bc12ff100bf7`
- 时间/作者: 2026-04-24 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c4c4c2148` - 修复fused_recurrent_gated_delta_rule_packed_decode报错问题

- 完整 hash: `c4c4c21480969b39ffb91f96371fd02221e97e5d`
- 时间/作者: 2026-04-22 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `39474e90b` - [feature] linear attn  fused_recurrent_gated_delta_rule_packed_decode use aiter

- 完整 hash: `39474e90b867ded403cbbe45ededa91c777768a1`
- 时间/作者: 2026-04-22 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/fla/chunk.py`, `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk.py`; `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c840dd8e7` - [FEAT] update triton extend fwd via aiter

- 完整 hash: `c840dd8e7d57896eb3f0ecdb000896ed46337e5a`
- 时间/作者: 2026-04-22 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fe965ea9e` - [feature] linear attn chunk_gated_delta_rule_fwd_h  use aiter

- 完整 hash: `fe965ea9e4269aa499a63da2a7ce18d7e0bd6e74`
- 时间/作者: 2026-04-21 / fanwl
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/fla/chunk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1221130a1` - add aiter moe w4a8 support

- 完整 hash: `1221130a1d2e4a556e69f4a3253548f267c91488`
- 时间/作者: 2026-04-17 / niuhb
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cd511513d` - [FEAT] enable fp8 shuffle weight for asm moe

- 完整 hash: `cd511513d07880685d26dae94074300e8e2fa614`
- 时间/作者: 2026-04-16 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a9965e61f` - adjust aiter_moe para order and w1_zp&w2_zp opt

- 完整 hash: `a9965e61f23b6e0ecd1c0eae7e9af714493e087d`
- 时间/作者: 2026-04-16 / Jiafei Sun
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e2ae2a431` - 修改 pyproject.toml 中的huggingface_hub版本

- 完整 hash: `e2ae2a431eaf957158e09bd015820520c6075035`
- 时间/作者: 2026-04-16 / chenjunhu
- 自动分类: 通用实现调整
- 主要文件: `python/pyproject.toml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `82a13cc79` - fix: 修改 pyproject.toml 中的依赖版本

- 完整 hash: `82a13cc794379a49951777284f91d9c9fc2113df`
- 时间/作者: 2026-04-16 / chenjunhu
- 自动分类: 缺陷修复
- 主要文件: `python/pyproject.toml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `41d14b7c6` - [FEAT] support FP8 MoE via aiter ASM kernel

- 完整 hash: `41d14b7c6dcbc42f239ed7df51fea3892a6721ed`
- 时间/作者: 2026-04-15 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fdf368589` - fix: 修复bmz上flash_mla不支持fp8

- 完整 hash: `fdf368589c914b7e936ec23daa07dc0ef39bc45b`
- 时间/作者: 2026-04-15 / niuhb
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `07469199b` - dpsk fp8适配fuse_moe_fp8_w8a8

- 完整 hash: `07469199b6c8b461505b99d7342ebfc1507ceed2`
- 时间/作者: 2026-04-15 / lipenghui
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3a8cd31f5` - add aiter moe w4f16 support

- 完整 hash: `3a8cd31f5738e12beeda73023f9c621aa659aecb`
- 时间/作者: 2026-04-14 / Jiafei Sun
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7859b2885` - [BUG FIX] fix nn transpose error for fp8 blockwise linear

- 完整 hash: `7859b2885fa219e71138b17cdec1dc7830f072f6`
- 时间/作者: 2026-04-14 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `aa77e2522` - Bugfix:fix mm model attention interface

- 完整 hash: `aa77e25228c0a04b41b6c3b0dc9fa01f9ebba4f2`
- 时间/作者: 2026-04-09 / liuchy5
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/vision.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e91aa8029` - 接入causal_conv1d_update优化算子

- 完整 hash: `e91aa8029e5cbffb7c2fdd4c685bdc7cac1f3760`
- 时间/作者: 2026-04-07 / liucong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `518582021` - fix deepseek log cudagraph init meta data copy error in bmz when capture cudagraph.

- 完整 hash: `5185820211a43e8383652d726bb61ecbfce7f6bb`
- 时间/作者: 2026-04-07 / lizhigong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `95a02a38d` - Update README_DCU.md

- 完整 hash: `95a02a38db01435ac2cb0d060ca70e8e05ac1337`
- 时间/作者: 2026-04-02 / guobj
- 自动分类: 调度/缓存/PD
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `80cbcce8e` - Update README_DCU.md

- 完整 hash: `80cbcce8e796bc909fbec586c238f0f60dba5f13`
- 时间/作者: 2026-04-02 / guobj
- 自动分类: 调度/缓存/PD
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `71cd1e550` - Update README_DCU.md

- 完整 hash: `71cd1e550bb0622d8def4214bb9c19bc3738d742`
- 时间/作者: 2026-04-02 / guobj
- 自动分类: 调度/缓存/PD
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `a510541b9` - Update README_DCU.md

- 完整 hash: `a510541b99527e69358b2d407368227fa7156bd7`
- 时间/作者: 2026-04-02 / guobj
- 自动分类: 调度/缓存/PD
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `e32b8b387` - optimized code of layernorm

- 完整 hash: `e32b8b38726e52fee4876c66f99d216396d7a9b3`
- 时间/作者: 2026-04-01 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `c87293f3a` - 修复融合算子并验证精度.

- 完整 hash: `c87293f3a9d04f1472a3f2c46c58cd5daa8ebf61`
- 时间/作者: 2026-04-01 / linhai1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4418f4abb` - 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现

- 完整 hash: `4418f4abbbe437f4f9cb4e17c4969b8de85c6008`
- 时间/作者: 2026-04-01 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `790dbca3a` - Revert "适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现"

- 完整 hash: `790dbca3a21961c89de4dda2e51686760edb46d2`
- 时间/作者: 2026-04-01 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `ec19cdf61` - 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现

- 完整 hash: `ec19cdf617a1ab433e28a56a90dafa3d41778976`
- 时间/作者: 2026-04-01 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `23329122c` - 适配lightop的gemma_fused_add_rmsnorm算子

- 完整 hash: `23329122cee029aee84517aca9f64f59dae7c8bb`
- 时间/作者: 2026-04-01 / chenyue3
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `9b0c470a6` - fix(security): replace unsafe pickle.loads with SafeUnpickler for CVE-2026-3989 (#20904)

- 完整 hash: `9b0c470a6a13bedc860c6836f5d07b6c2f62e61a`
- 时间/作者: 2026-03-27 / zwang86
- 自动分类: 缺陷修复
- 主要文件: `docs/developer_guide/contribution_guide.md`, `python/sglang/srt/utils/common.py`, `scripts/playground/replay_request_dump.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/developer_guide/contribution_guide.md`
  - other: `python/sglang/srt/utils/common.py`; `scripts/playground/replay_request_dump.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `192ba2c4e` - [Security] 1/N: Bind ZMQ sockets to localhost to prevent unauthenticated remote access (#21435)

- 完整 hash: `192ba2c4e4daa408a8845521c10797395ef8c17e`
- 时间/作者: 2026-03-26 / Khoa Pham
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/utils/network.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/encode_receiver.py`; `python/sglang/srt/utils/network.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `2e65c27b2` - Api add flush cache timeout (#21413)

- 完整 hash: `2e65c27b29152cc99fac5589a89a79edbc975a81`
- 时间/作者: 2026-03-27 / SevenJ
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_communicator_mixin.py`, `test/registered/unit/managers/test_scheduler_flush_cache.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/managers/tokenizer_communicator_mixin.py`
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
  - tests: `test/registered/unit/managers/test_scheduler_flush_cache.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `be0cca559` - Use torch.addmm instead of separate mm and add_ calls for LoRA torch.native (#20562)

- 完整 hash: `be0cca5596f97c2eff6f5e7b4ba49f187e7a2e11`
- 时间/作者: 2026-03-26 / satyamk7054
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/lora/backend/torch_backend.py`, `python/sglang/srt/lora/torch_ops/lora_ops.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/lora/backend/torch_backend.py`; `python/sglang/srt/lora/torch_ops/lora_ops.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `e59ea4f6e` - fix: torch-native LoRA for multi-adapter case (#20564)

- 完整 hash: `e59ea4f6e9aacb50b54fb29b8396d22708b3df79`
- 时间/作者: 2026-03-26 / satyamk7054
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/lora/backend/torch_backend.py`, `test/manual/lora/test_torch_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/lora/backend/torch_backend.py`
  - tests: `test/manual/lora/test_torch_backend.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `e5dd411f6` - [CI] Add ci-workflow-guide skill and consolidate CI docs (#21429)

- 完整 hash: `e5dd411f64b5860e1fa5d36c1d781eb9bed0d647`
- 时间/作者: 2026-03-26 / Liangsheng Yin
- 自动分类: 模型支持/运行时入口
- 主要文件: `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `test/README.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `test/README.md`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `e5b765035` - Fix UnboundLocalError when DetokenizerManager constructor fails (#21471)

- 完整 hash: `e5b7650353234754a92116b9fd5478dd3bfffa13`
- 时间/作者: 2026-03-26 / Liangsheng Yin
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/detokenizer_manager.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/detokenizer_manager.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `17f43d151` - [CI] Skip stage health check for release branch cut (#21488)

- 完整 hash: `17f43d15187be710828a1ff6a4843fdddb0b1eb7`
- 时间/作者: 2026-03-26 / Liangsheng Yin
- 自动分类: 性能/后端优化
- 主要文件: `.github/actions/check-stage-health/action.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test-multimodal-gen.yml`, `.github/workflows/pr-test-sgl-kernel.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/release-branch-cut.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/actions/check-stage-health/action.yml`; `.github/workflows/pr-test-jit-kernel.yml`; `.github/workflows/pr-test-multimodal-gen.yml`; `.github/workflows/pr-test-sgl-kernel.yml`; `.github/workflows/pr-test.yml`; `.github/workflows/release-branch-cut.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `8febc3650` - [NPU] multimodal-gen-test-8-npu-a3,Cache pytorch dependency (#21470)

- 完整 hash: `8febc3650d0490db2ed3fcc471b6925028dc027c`
- 时间/作者: 2026-03-26 / monkeyLoveding
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/pr-test-npu.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-npu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `013fa5563` - [AMD] CI - fix amd 4-GPU PR test (#21444)

- 完整 hash: `013fa5563022f921e0e2f634a946cbcecbc082b2`
- 时间/作者: 2026-03-26 / YC Yen-Ching Tseng
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-amd.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-amd.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f289d173a` - [Deps] Bump xgrammar to 0.1.32 (#21032)

- 完整 hash: `f289d173aa6031a01c4300c14584fa48ffa6e36e`
- 时间/作者: 2026-03-26 / Anant Sharma
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-npu.yml`, `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - other: `3rdparty/amd/wheel/sglang/pyproject.toml`; `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `fd535942a` - [AMD]Integrate aiter's fused_topk for softmax scoring in topk function (#21421)

- 完整 hash: `fd535942acfe4fa63b46040bd26f411be04a2995`
- 时间/作者: 2026-03-26 / Chen, Zhentao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/topk.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a30596415` - [MLX] Add native MLX execution backend for Apple Silicon Mac (#20342)

- 完整 hash: `a3059641593b985387a6abbb70c19c4ddc53cf1e`
- 时间/作者: 2026-03-26 / R0CKSTAR
- 自动分类: 调度/缓存/PD
- 主要文件: `python/pyproject_other.toml`, `python/sglang/bench_one_batch.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/tensor_bridge.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject_other.toml`; `python/sglang/bench_one_batch.py`; `python/sglang/srt/hardware_backend/mlx/model_runner.py`; `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`; `python/sglang/srt/utils/tensor_bridge.py`
  - runtime-model: `python/sglang/srt/hardware_backend/mlx/tp_worker.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `7ca015fe6` - [Diffusion] Refactor diffusion JIT kernel test layout and narrow CI triggers (#21385)

- 完整 hash: `7ca015fe65e5369df8cc4936f48617dca269b1b2`
- 时间/作者: 2026-03-26 / Xiaoyu Zhang
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `test/README.md`, `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `test/README.md`; `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `79db3bec3` - [CI] Add PID namespace and ps auxf diagnostics to killall.py (#21401)

- 完整 hash: `79db3bec34a0fd0d70220841b0f16791b2191302`
- 时间/作者: 2026-03-25 / Liangsheng Yin
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/cli/killall.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/cli/killall.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `176c8e7b0` - [CI] Simplify CI check actions and add maintenance gate to rerun-ut (#21455)

- 完整 hash: `176c8e7b0e6eac5374738d8d01c0e7574f1d4348`
- 时间/作者: 2026-03-25 / Liangsheng Yin
- 自动分类: 性能/后端优化
- 主要文件: `.github/actions/check-maintenance/action.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test-multimodal-gen.yml`, `.github/workflows/pr-test-sgl-kernel.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/rerun-ut.yml`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/actions/check-maintenance/action.yml`; `.github/workflows/nightly-test-nvidia.yml`; `.github/workflows/pr-test-jit-kernel.yml`; `.github/workflows/pr-test-multimodal-gen.yml`; `.github/workflows/pr-test-sgl-kernel.yml`; `.github/workflows/pr-test.yml`; `.github/workflows/rerun-ut.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

### Commit `f14260840` - [MUSA] apply_vocab_mask support musa device (#21296)

- 完整 hash: `f142608408ed2a9b28aa649ce4c234bb1a2f30e1`
- 时间/作者: 2026-03-26 / ori
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/constrained/xgrammar_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/constrained/xgrammar_backend.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `f420b9b4a` - [MUSA][Feature] Enable Piecewise CUDA Graph support for MUSA platform (#20758)

- 完整 hash: `f420b9b4a58ec42106edd70c3dc022ab71b0ccf5`
- 时间/作者: 2026-03-26 / MARATRIX
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/compilation/weak_ref_tensor.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/compilation/weak_ref_tensor.py`
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `abf4f1a47` - [MPS] Add StreamContext stub (#20782)

- 完整 hash: `abf4f1a47a0769a3fb61d021fd59b797319caa2c`
- 时间/作者: 2026-03-26 / R0CKSTAR
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/_mps_stub.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/_mps_stub.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `02521420b` - [MPS] Support sglang.check_env (#20753)

- 完整 hash: `02521420b3ca353433d5e58c4e981af74b1e3483`
- 时间/作者: 2026-03-26 / R0CKSTAR
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/check_env.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/check_env.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `d9e96153d` - [NPU] Support Hybrid KV Cache for Ascend backend (#18032)

- 完整 hash: `d9e96153de8a1011c3eb4427af4b3c2e9823e4b2`
- 时间/作者: 2026-03-26 / gjsheu
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`; `python/sglang/srt/mem_cache/swa_memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bb2989368` - [Fix] Try to fix nvcc compilation error (#21246)

- 完整 hash: `bb298936891fb6390ee43e6f7ebf635b9954cc9b`
- 时间/作者: 2026-03-26 / DarkSharpness
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `python/sglang/jit_kernel/all_reduce.py`, `python/sglang/jit_kernel/include/sgl_kernel/distributed/custom_all_reduce.cuh`, `python/sglang/jit_kernel/tests/test_custom_all_reduce.py`, `test/README.md`, `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-nvidia.yml`; `.github/workflows/pr-test-jit-kernel.yml`
  - runtime-perf: `python/sglang/jit_kernel/all_reduce.py`; `python/sglang/jit_kernel/include/sgl_kernel/distributed/custom_all_reduce.cuh`
  - tests: `python/sglang/jit_kernel/tests/test_custom_all_reduce.py`; `test/README.md`; `test/run_suite.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a34e9ed64` - Add adjusted_filter_batch (#21260)

- 完整 hash: `a34e9ed64adeb7b9f3b3809390e33f1ee87a2080`
- 时间/作者: 2026-03-25 / Aurick Qiao
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/sampling/sampling_batch_info.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/sampling/sampling_batch_info.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `53c1d8e96` - Fix customized_info offset truncation (#21262)

- 完整 hash: `53c1d8e963888fee0c3330491be7204f82a7b64b`
- 时间/作者: 2026-03-25 / Aurick Qiao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler_output_processor_mixin.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler_output_processor_mixin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1100b9865` - Fix MxInt4 MoE returning wrong output variable (#21348)

- 完整 hash: `1100b9865c48219e74887a60274f6d7a134bbb60`
- 时间/作者: 2026-03-25 / Sam Shleifer
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `662635e7a` - fix(sgl-kernel): align wheel METADATA/WHEEL with +cu filename (#21437)

- 完整 hash: `662635e7a7674b7f83d1a64573c9378455d033e2`
- 时间/作者: 2026-03-25 / Yanda Cheng
- 自动分类: 性能/后端优化
- 主要文件: `sgl-kernel/rename_wheels.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `sgl-kernel/rename_wheels.sh`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `80389fec0` - [AMD] Fix AMD CI: mark /sglang-checkout as git safe.directory in container (#21423)

- 完整 hash: `80389fec004394db409e9d04aef263465a3b235c`
- 时间/作者: 2026-03-25 / Michael
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `scripts/ci/amd/amd_ci_start_container.sh`; `scripts/ci/amd/amd_ci_start_container_disagg.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。
