# sglang Shared Framework Commits Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `.codespellrc` | no direct commit |
| `.coveragerc` | no direct commit |
| `.dockerignore` | no direct commit |
| `.github/CI_PERMISSIONS.json` | no direct commit |
| `.github/CODEOWNERS` | no direct commit |
| `.github/FOLDER_README.md` | no direct commit |
| `.github/ISSUE_TEMPLATE/1-bug-report.yml` | no direct commit |
| `.github/ISSUE_TEMPLATE/2-feature-request.yml` | no direct commit |
| `.github/MAINTAINER.md` | no direct commit |
| `.github/actions/check-maintenance/action.yml` | `176c8e7b0` |
| `.github/actions/check-stage-health/action.yml` | `17f43d151` |
| `.github/actions/upload-cuda-coredumps/action.yml` | no direct commit |
| `.github/actions/wait-for-jobs/action.yml` | no direct commit |
| `.github/labeler.yml` | no direct commit |
| `.github/linters/lychee-ci.toml` | no direct commit |
| `.github/linters/lychee.toml` | no direct commit |
| `.github/pull_request_template.md` | no direct commit |
| `.github/update_ci_permission.py` | no direct commit |
| `.github/workflows/amd-aiter-scout.yml` | no direct commit |
| `.github/workflows/amd-ci-job-monitor.yml` | no direct commit |
| `.github/workflows/auto-tune.yml` | no direct commit |
| `.github/workflows/bot-bump-flashinfer-version.yml` | no direct commit |
| `.github/workflows/bot-bump-kernel-version-to-sglang.yml` | no direct commit |
| `.github/workflows/bot-bump-kernel-version.yml` | no direct commit |
| `.github/workflows/bot-bump-sglang-version.yml` | no direct commit |
| `.github/workflows/bot-cherry-pick.yml` | no direct commit |
| `.github/workflows/cancel-pr-workflow-on-merge.yml` | no direct commit |
| `.github/workflows/cancel-unfinished-pr-tests.yml` | no direct commit |
| `.github/workflows/ci-coverage-overview.yml` | no direct commit |
| `.github/workflows/ci-failure-monitor.yml` | no direct commit |
| `.github/workflows/close-inactive-issues.yml` | no direct commit |
| `.github/workflows/execute-notebook.yml` | no direct commit |
| `.github/workflows/labeler.yml` | no direct commit |
| `.github/workflows/lint.yml` | no direct commit |
| `.github/workflows/list-active-pr-runs.yml` | no direct commit |
| `.github/workflows/nightly-link-check.yml` | no direct commit |
| `.github/workflows/nightly-release-gateway.yml` | no direct commit |
| `.github/workflows/nightly-test-amd-rocm720.yml` | no direct commit |
| `.github/workflows/nightly-test-amd.yml` | no direct commit |
| `.github/workflows/nightly-test-intel.yml` | no direct commit |
| `.github/workflows/nightly-test-npu.yml` | `f289d173a` |
| `.github/workflows/nightly-test-nvidia.yml` | `176c8e7b0`, `bb2989368` |
| `.github/workflows/open-pr-copy-from-oss.yml` | no direct commit |
| `.github/workflows/open-pr-copy-to-oss.yml` | no direct commit |
| `.github/workflows/patch-docker-dev.yml` | no direct commit |
| `.github/workflows/pr-benchmark-rust.yml` | no direct commit |
| `.github/workflows/pr-gate.yml` | no direct commit |
| `.github/workflows/pr-test-amd-rocm720.yml` | `7ca015fe6` |
| `.github/workflows/pr-test-amd.yml` | `013fa5563`, `7ca015fe6` |
| `.github/workflows/pr-test-jit-kernel.yml` | `17f43d151`, `176c8e7b0`, `bb2989368` |
| `.github/workflows/pr-test-multimodal-gen.yml` | `17f43d151`, `176c8e7b0` |
| `.github/workflows/pr-test-npu.yml` | `8febc3650` |
| `.github/workflows/pr-test-rust.yml` | no direct commit |
| `.github/workflows/pr-test-sgl-kernel.yml` | `17f43d151`, `176c8e7b0` |
| `.github/workflows/pr-test-xeon.yml` | no direct commit |
| `.github/workflows/pr-test-xpu.yml` | no direct commit |
| `.github/workflows/pr-test.yml` | `17f43d151`, `7ca015fe6`, `176c8e7b0` |
| `.github/workflows/release-branch-cut.yml` | `17f43d151` |
| `.github/workflows/release-docker-amd-nightly.yml` | no direct commit |
| `.github/workflows/release-docker-amd-rocm720-nightly.yml` | no direct commit |
| `.github/workflows/release-docker-amd.yml` | no direct commit |
| `.github/workflows/release-docker-cu13-framework.yml` | no direct commit |
| `.github/workflows/release-docker-dev.yml` | no direct commit |
| `.github/workflows/release-docker-gateway.yml` | no direct commit |
| `.github/workflows/release-docker-npu-nightly.yml` | no direct commit |
| `.github/workflows/release-docker-npu.yml` | no direct commit |
| `.github/workflows/release-docker-xeon.yml` | no direct commit |
| `.github/workflows/release-docker.yml` | no direct commit |
| `.github/workflows/release-docs.yml` | no direct commit |
| `.github/workflows/release-pypi-gateway.yml` | no direct commit |
| `.github/workflows/release-pypi-nightly.yml` | no direct commit |
| `.github/workflows/release-pypi-pr.yml` | no direct commit |
| `.github/workflows/release-pypi.yml` | no direct commit |
| `.github/workflows/release-tag.yml` | no direct commit |
| `.github/workflows/release-whl-kernel.yml` | no direct commit |
| `.github/workflows/rerun-ut.yml` | `176c8e7b0` |
| `.github/workflows/retag-docker.yml` | no direct commit |
| `.github/workflows/runner-utilization.yml` | no direct commit |
| `.github/workflows/slash-command-handler.yml` | no direct commit |
| `.github/workflows/stress-test.yml` | no direct commit |
| ... | 2951 more files omitted from table; all were used for git tracing. |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 80
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
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

## Per-Commit Audit Cards

### Commit `5a00fbb22` - 删除多余代码

- Full hash: `5a00fbb22ffdc69b5b13abecabd5a5f111fe328f`
- Date/author: 2026-05-18 / shangxl
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_profiler_mixin.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/session_aware_cache.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_profiler_mixin.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/session_aware_cache.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py` 等 9 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `dea82e2bc` - 去掉无关的代码及注释

- Full hash: `dea82e2bc5991147fae3eec4c5b1589e88a00ae4`
- Date/author: 2026-05-18 / shangxl
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/radix_cache.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ce4be7d18` - hicache功能适配

- Full hash: `ce4be7d186e131497c0586a32ed18345a79f4a93`
- Date/author: 2026-05-18 / shangxl
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `sgl-kernel/csrc/common_extension_rocm.cc`, `sgl-kernel/csrc/kvcacheio/transfer.cu`, `sgl-kernel/include/sgl_kernel_ops.h`, `sgl-kernel/python/sgl_kernel/kvcacheio.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `sgl-kernel/csrc/common_extension_rocm.cc`; `sgl-kernel/csrc/kvcacheio/transfer.cu`; `sgl-kernel/include/sgl_kernel_ops.h`; `sgl-kernel/python/sgl_kernel/kvcacheio.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `55a72732c` - fix(dcu): 修复HiCache kernel路径访问host pointer导致的VMFault

- Full hash: `55a72732c41836b8e672ce02a6af9ffcee0b5817`
- Date/author: 2026-05-09 / maxiao1
- Auto category: 性能/后端优化
- Main files: `sgl-kernel/csrc/kvcacheio/transfer.cu`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `sgl-kernel/csrc/kvcacheio/transfer.cu`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5a811d1de` - 修改transfer_kv_all_direct_pf_lf_H2D_dcu参数

- Full hash: `5a811d1ded746b54d5b8877d307d83aa0f5dc1f5`
- Date/author: 2026-05-06 / shangxl
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/mem_cache/memory_pool_host.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool_host.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ec7e2e859` - 提交本地修改的hicache

- Full hash: `ec7e2e8595a8bd4df2cc191ec3fcca11a9610bc0`
- Date/author: 2026-04-18 / niuhb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_profiler_mixin.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/memory_pool_host.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`; `python/sglang/srt/managers/cache_controller.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_profiler_mixin.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hiradix_cache.py`; `python/sglang/srt/mem_cache/memory_pool_host.py`; `python/sglang/srt/mem_cache/radix_cache.py` 等 14 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9555bc282` - 修改launch_chunk_fwd_kernel_o算子传参

- Full hash: `9555bc28286e08db74dce900900b5ccf86ca0715`
- Date/author: 2026-05-18 / liucong8560
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk_o.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_o.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `162699fac` - [opt]fused_mamba_state_scatter_with_mask算子优化

- Full hash: `162699fac22b3bb750671b4d537c63c3a8e95a56`
- Date/author: 2026-05-18 / liucong8560
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d32a79c65` - 修改aiter prefill阶段的fla算子传参

- Full hash: `d32a79c65c752b8432983b083a82bf20c8ae7796`
- Date/author: 2026-05-18 / liucong8560
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/fla/chunk_o.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/attention/fla/chunk_o.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4816b3f21` - [BUG FIX] add missing argument in aiter block fp8 moe

- Full hash: `4816b3f21e57d9804bf01c25db48c28760976508`
- Date/author: 2026-05-16 / shiqiang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5daf25b16` - [feat]适配aiter moe fp8_w8a8

- Full hash: `5daf25b168a9182e660225f68d45f1d2b481d3b6`
- Date/author: 2026-05-15 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0474160f8` - [BUG FIX] RadixAttention should not be skipped regardless of ignore list

- Full hash: `0474160f8eaeab06e5e1d8affe352685d4ce8cdd`
- Date/author: 2026-05-14 / shiqiang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bd06359df` - [fix]: SlimQuantW4A8Int8MarlinMoEMethod增加必要的形参

- Full hash: `bd06359df6a612e029eb8c0f28dcf861d8e2b22f`
- Date/author: 2026-05-13 / wujl5
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7b06a6e59` - 修复seq_lens前后不一致，导致开mtp时block_table索引计算有问题，进而导致临界状态传参错误造成vmfault的问题

- Full hash: `7b06a6e593db9cead379d6d9542e4c29f6830a73`
- Date/author: 2026-05-14 / lipenghui
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `87d24d36b` - [bugfix]fix aiter_chunk_gated_delta_rule_fwd_kernel_h_blockdim64函数传参错误，解决qw3.5-35b,qw3.6-35b的精度问题

- Full hash: `87d24d36b9271ee6fd27fe640b203cff4bb0d8c3`
- Date/author: 2026-05-14 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `06751b190` - [feat]lightop不支持的moe  size转到aiter进行支持

- Full hash: `06751b1909d13c17500c59f5ae3621915e8704b5`
- Date/author: 2026-05-13 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5d71e7e7a` - fix some error in initial version

- Full hash: `5d71e7e7ab11e7b760fba5e33f1dbeff30b35ba8`
- Date/author: 2026-05-14 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_interface.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1b7bdda04` - [feat]修改chunk_gated_delta_rule_fwd_kernel_h_blockdim64算子的import 路径从而适配新版本aiter

- Full hash: `1b7bdda04720df5a0ecd25964939f90e7417137d`
- Date/author: 2026-05-13 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `423d7d102` - [BUG FIX] eliminate trace bubbles in MTP graph reply stage by avoiding implicit conversion

- Full hash: `423d7d102b5cc7490cd0919a419ab111b02f8bf5`
- Date/author: 2026-05-12 / shiqiang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `8401bfecf` - 接入causal_conv1d_fn_dcu算子实现

- Full hash: `8401bfecf28117841d8798e4bdc57c294b1434fe`
- Date/author: 2026-05-08 / liucong
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2e6a7a94d` - 增加aiter的fused_sigmoid_gating_delta_rule_update算子实现

- Full hash: `2e6a7a94d930dbcfa46bc3941cc8343ff8e66be6`
- Date/author: 2026-05-08 / liucong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `3c1dba355` - 修复slimquant_w4a8中blaslt路径的量化算子调用与权重布局

- Full hash: `3c1dba35570e7261a6bf39a26837c7b8907c7b5f`
- Date/author: 2026-05-07 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `dfb359973` - 修改调用aiter的chunk_gated_delta_rule_fwd算子方法

- Full hash: `dfb359973e5195d09817137c2a1b4740195f8d7e`
- Date/author: 2026-05-06 / liucong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/chunk.py`, `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk.py`; `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b80efea17` - 修改w4a8重排逻辑，适配deepgemm新包

- Full hash: `b80efea17de96dc59b81b5ebf9f8d1fa1ad55501`
- Date/author: 2026-04-29 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/layers/quantization/w4a8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`; `python/sglang/srt/layers/quantization/w4a8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `16df9541d` - fix(量化): 规范 W8A8 与 Marlin MoE 处理逻辑

- Full hash: `16df9541d2c0d36afb21179d106f26462d495c0f`
- Date/author: 2026-04-28 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f34ecd7de` - [BUG FIX] fix CUDA graph grid undercoverage in multi-layer EAGLE MTP draft extend

- Full hash: `f34ecd7def554d51e627783eb8f5bc12ff100bf7`
- Date/author: 2026-04-24 / ShiQiang Dai
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c4c4c2148` - 修复fused_recurrent_gated_delta_rule_packed_decode报错问题

- Full hash: `c4c4c21480969b39ffb91f96371fd02221e97e5d`
- Date/author: 2026-04-22 / liucong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `39474e90b` - [feature] linear attn  fused_recurrent_gated_delta_rule_packed_decode use aiter

- Full hash: `39474e90b867ded403cbbe45ededa91c777768a1`
- Date/author: 2026-04-22 / liucong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/fla/chunk.py`, `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk.py`; `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c840dd8e7` - [FEAT] update triton extend fwd via aiter

- Full hash: `c840dd8e7d57896eb3f0ecdb000896ed46337e5a`
- Date/author: 2026-04-22 / ShiQiang Dai
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fe965ea9e` - [feature] linear attn chunk_gated_delta_rule_fwd_h  use aiter

- Full hash: `fe965ea9e4269aa499a63da2a7ce18d7e0bd6e74`
- Date/author: 2026-04-21 / fanwl
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/fla/chunk.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/chunk.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1221130a1` - add aiter moe w4a8 support

- Full hash: `1221130a1d2e4a556e69f4a3253548f267c91488`
- Date/author: 2026-04-17 / niuhb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `cd511513d` - [FEAT] enable fp8 shuffle weight for asm moe

- Full hash: `cd511513d07880685d26dae94074300e8e2fa614`
- Date/author: 2026-04-16 / ShiQiang Dai
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a9965e61f` - adjust aiter_moe para order and w1_zp&w2_zp opt

- Full hash: `a9965e61f23b6e0ecd1c0eae7e9af714493e087d`
- Date/author: 2026-04-16 / Jiafei Sun
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e2ae2a431` - 修改 pyproject.toml 中的huggingface_hub版本

- Full hash: `e2ae2a431eaf957158e09bd015820520c6075035`
- Date/author: 2026-04-16 / chenjunhu
- Auto category: 通用实现调整
- Main files: `python/pyproject.toml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/pyproject.toml`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `82a13cc79` - fix: 修改 pyproject.toml 中的依赖版本

- Full hash: `82a13cc794379a49951777284f91d9c9fc2113df`
- Date/author: 2026-04-16 / chenjunhu
- Auto category: 缺陷修复
- Main files: `python/pyproject.toml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/pyproject.toml`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `41d14b7c6` - [FEAT] support FP8 MoE via aiter ASM kernel

- Full hash: `41d14b7c6dcbc42f239ed7df51fea3892a6721ed`
- Date/author: 2026-04-15 / ShiQiang Dai
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fdf368589` - fix: 修复bmz上flash_mla不支持fp8

- Full hash: `fdf368589c914b7e936ec23daa07dc0ef39bc45b`
- Date/author: 2026-04-15 / niuhb
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `07469199b` - dpsk fp8适配fuse_moe_fp8_w8a8

- Full hash: `07469199b6c8b461505b99d7342ebfc1507ceed2`
- Date/author: 2026-04-15 / lipenghui
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/w8a8_fp8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `3a8cd31f5` - add aiter moe w4f16 support

- Full hash: `3a8cd31f5738e12beeda73023f9c621aa659aecb`
- Date/author: 2026-04-14 / Jiafei Sun
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7859b2885` - [BUG FIX] fix nn transpose error for fp8 blockwise linear

- Full hash: `7859b2885fa219e71138b17cdec1dc7830f072f6`
- Date/author: 2026-04-14 / ShiQiang Dai
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `aa77e2522` - Bugfix:fix mm model attention interface

- Full hash: `aa77e25228c0a04b41b6c3b0dc9fa01f9ebba4f2`
- Date/author: 2026-04-09 / liuchy5
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/vision.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e91aa8029` - 接入causal_conv1d_update优化算子

- Full hash: `e91aa8029e5cbffb7c2fdd4c685bdc7cac1f3760`
- Date/author: 2026-04-07 / liucong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `518582021` - fix deepseek log cudagraph init meta data copy error in bmz when capture cudagraph.

- Full hash: `5185820211a43e8383652d726bb61ecbfce7f6bb`
- Date/author: 2026-04-07 / lizhigong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `95a02a38d` - Update README_DCU.md

- Full hash: `95a02a38db01435ac2cb0d060ca70e8e05ac1337`
- Date/author: 2026-04-02 / guobj
- Auto category: 调度/缓存/PD
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README_DCU.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `80cbcce8e` - Update README_DCU.md

- Full hash: `80cbcce8e796bc909fbec586c238f0f60dba5f13`
- Date/author: 2026-04-02 / guobj
- Auto category: 调度/缓存/PD
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README_DCU.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `71cd1e550` - Update README_DCU.md

- Full hash: `71cd1e550bb0622d8def4214bb9c19bc3738d742`
- Date/author: 2026-04-02 / guobj
- Auto category: 调度/缓存/PD
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README_DCU.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `a510541b9` - Update README_DCU.md

- Full hash: `a510541b99527e69358b2d407368227fa7156bd7`
- Date/author: 2026-04-02 / guobj
- Auto category: 调度/缓存/PD
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `README_DCU.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `e32b8b387` - optimized code of layernorm

- Full hash: `e32b8b38726e52fee4876c66f99d216396d7a9b3`
- Date/author: 2026-04-01 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `c87293f3a` - 修复融合算子并验证精度.

- Full hash: `c87293f3a9d04f1472a3f2c46c58cd5daa8ebf61`
- Date/author: 2026-04-01 / linhai1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4418f4abb` - 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现

- Full hash: `4418f4abbbe437f4f9cb4e17c4969b8de85c6008`
- Date/author: 2026-04-01 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `790dbca3a` - Revert "适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现"

- Full hash: `790dbca3a21961c89de4dda2e51686760edb46d2`
- Date/author: 2026-04-01 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `ec19cdf61` - 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现

- Full hash: `ec19cdf617a1ab433e28a56a90dafa3d41778976`
- Date/author: 2026-04-01 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `23329122c` - 适配lightop的gemma_fused_add_rmsnorm算子

- Full hash: `23329122cee029aee84517aca9f64f59dae7c8bb`
- Date/author: 2026-04-01 / chenyue3
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `9b0c470a6` - fix(security): replace unsafe pickle.loads with SafeUnpickler for CVE-2026-3989 (#20904)

- Full hash: `9b0c470a6a13bedc860c6836f5d07b6c2f62e61a`
- Date/author: 2026-03-27 / zwang86
- Auto category: 缺陷修复
- Main files: `docs/developer_guide/contribution_guide.md`, `python/sglang/srt/utils/common.py`, `scripts/playground/replay_request_dump.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/developer_guide/contribution_guide.md`
  - other: `python/sglang/srt/utils/common.py`; `scripts/playground/replay_request_dump.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `192ba2c4e` - [Security] 1/N: Bind ZMQ sockets to localhost to prevent unauthenticated remote access (#21435)

- Full hash: `192ba2c4e4daa408a8845521c10797395ef8c17e`
- Date/author: 2026-03-26 / Khoa Pham
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/utils/network.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/encode_receiver.py`; `python/sglang/srt/utils/network.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `2e65c27b2` - Api add flush cache timeout (#21413)

- Full hash: `2e65c27b29152cc99fac5589a89a79edbc975a81`
- Date/author: 2026-03-27 / SevenJ
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_communicator_mixin.py`, `test/registered/unit/managers/test_scheduler_flush_cache.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/managers/tokenizer_communicator_mixin.py`
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
  - tests: `test/registered/unit/managers/test_scheduler_flush_cache.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `be0cca559` - Use torch.addmm instead of separate mm and add_ calls for LoRA torch.native (#20562)

- Full hash: `be0cca5596f97c2eff6f5e7b4ba49f187e7a2e11`
- Date/author: 2026-03-26 / satyamk7054
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/lora/backend/torch_backend.py`, `python/sglang/srt/lora/torch_ops/lora_ops.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/lora/backend/torch_backend.py`; `python/sglang/srt/lora/torch_ops/lora_ops.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `e59ea4f6e` - fix: torch-native LoRA for multi-adapter case (#20564)

- Full hash: `e59ea4f6e9aacb50b54fb29b8396d22708b3df79`
- Date/author: 2026-03-26 / satyamk7054
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/lora/backend/torch_backend.py`, `test/manual/lora/test_torch_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/lora/backend/torch_backend.py`
  - tests: `test/manual/lora/test_torch_backend.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `e5dd411f6` - [CI] Add ci-workflow-guide skill and consolidate CI docs (#21429)

- Full hash: `e5dd411f64b5860e1fa5d36c1d781eb9bed0d647`
- Date/author: 2026-03-26 / Liangsheng Yin
- Auto category: 模型支持/运行时入口
- Main files: `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `test/README.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `test/README.md`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `e5b765035` - Fix UnboundLocalError when DetokenizerManager constructor fails (#21471)

- Full hash: `e5b7650353234754a92116b9fd5478dd3bfffa13`
- Date/author: 2026-03-26 / Liangsheng Yin
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/detokenizer_manager.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/detokenizer_manager.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `17f43d151` - [CI] Skip stage health check for release branch cut (#21488)

- Full hash: `17f43d15187be710828a1ff6a4843fdddb0b1eb7`
- Date/author: 2026-03-26 / Liangsheng Yin
- Auto category: 性能/后端优化
- Main files: `.github/actions/check-stage-health/action.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test-multimodal-gen.yml`, `.github/workflows/pr-test-sgl-kernel.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/release-branch-cut.yml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/actions/check-stage-health/action.yml`; `.github/workflows/pr-test-jit-kernel.yml`; `.github/workflows/pr-test-multimodal-gen.yml`; `.github/workflows/pr-test-sgl-kernel.yml`; `.github/workflows/pr-test.yml`; `.github/workflows/release-branch-cut.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `8febc3650` - [NPU] multimodal-gen-test-8-npu-a3,Cache pytorch dependency (#21470)

- Full hash: `8febc3650d0490db2ed3fcc471b6925028dc027c`
- Date/author: 2026-03-26 / monkeyLoveding
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/pr-test-npu.yml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-npu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `013fa5563` - [AMD] CI - fix amd 4-GPU PR test (#21444)

- Full hash: `013fa5563022f921e0e2f634a946cbcecbc082b2`
- Date/author: 2026-03-26 / YC Yen-Ching Tseng
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-amd.yml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-amd.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `f289d173a` - [Deps] Bump xgrammar to 0.1.32 (#21032)

- Full hash: `f289d173aa6031a01c4300c14584fa48ffa6e36e`
- Date/author: 2026-03-26 / Anant Sharma
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-npu.yml`, `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - other: `3rdparty/amd/wheel/sglang/pyproject.toml`; `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `fd535942a` - [AMD]Integrate aiter's fused_topk for softmax scoring in topk function (#21421)

- Full hash: `fd535942acfe4fa63b46040bd26f411be04a2995`
- Date/author: 2026-03-26 / Chen, Zhentao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/topk.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/topk.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a30596415` - [MLX] Add native MLX execution backend for Apple Silicon Mac (#20342)

- Full hash: `a3059641593b985387a6abbb70c19c4ddc53cf1e`
- Date/author: 2026-03-26 / R0CKSTAR
- Auto category: 调度/缓存/PD
- Main files: `python/pyproject_other.toml`, `python/sglang/bench_one_batch.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/tensor_bridge.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/pyproject_other.toml`; `python/sglang/bench_one_batch.py`; `python/sglang/srt/hardware_backend/mlx/model_runner.py`; `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`; `python/sglang/srt/utils/tensor_bridge.py`
  - runtime-model: `python/sglang/srt/hardware_backend/mlx/tp_worker.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `7ca015fe6` - [Diffusion] Refactor diffusion JIT kernel test layout and narrow CI triggers (#21385)

- Full hash: `7ca015fe65e5369df8cc4936f48617dca269b1b2`
- Date/author: 2026-03-26 / Xiaoyu Zhang
- Auto category: 性能/后端优化
- Main files: `.claude/skills/write-sglang-test/SKILL.md`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `test/README.md`, `test/run_suite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `test/README.md`; `test/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `79db3bec3` - [CI] Add PID namespace and ps auxf diagnostics to killall.py (#21401)

- Full hash: `79db3bec34a0fd0d70220841b0f16791b2191302`
- Date/author: 2026-03-25 / Liangsheng Yin
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/cli/killall.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/cli/killall.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `176c8e7b0` - [CI] Simplify CI check actions and add maintenance gate to rerun-ut (#21455)

- Full hash: `176c8e7b0e6eac5374738d8d01c0e7574f1d4348`
- Date/author: 2026-03-25 / Liangsheng Yin
- Auto category: 性能/后端优化
- Main files: `.github/actions/check-maintenance/action.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test-multimodal-gen.yml`, `.github/workflows/pr-test-sgl-kernel.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/rerun-ut.yml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/actions/check-maintenance/action.yml`; `.github/workflows/nightly-test-nvidia.yml`; `.github/workflows/pr-test-jit-kernel.yml`; `.github/workflows/pr-test-multimodal-gen.yml`; `.github/workflows/pr-test-sgl-kernel.yml`; `.github/workflows/pr-test.yml`; `.github/workflows/rerun-ut.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `f14260840` - [MUSA] apply_vocab_mask support musa device (#21296)

- Full hash: `f142608408ed2a9b28aa649ce4c234bb1a2f30e1`
- Date/author: 2026-03-26 / ori
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/constrained/xgrammar_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/constrained/xgrammar_backend.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `f420b9b4a` - [MUSA][Feature] Enable Piecewise CUDA Graph support for MUSA platform (#20758)

- Full hash: `f420b9b4a58ec42106edd70c3dc022ab71b0ccf5`
- Date/author: 2026-03-26 / MARATRIX
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/compilation/weak_ref_tensor.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/compilation/weak_ref_tensor.py`
  - runtime-model: `python/sglang/srt/server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `abf4f1a47` - [MPS] Add StreamContext stub (#20782)

- Full hash: `abf4f1a47a0769a3fb61d021fd59b797319caa2c`
- Date/author: 2026-03-26 / R0CKSTAR
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/_mps_stub.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/_mps_stub.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `02521420b` - [MPS] Support sglang.check_env (#20753)

- Full hash: `02521420b3ca353433d5e58c4e981af74b1e3483`
- Date/author: 2026-03-26 / R0CKSTAR
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/check_env.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/check_env.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `d9e96153d` - [NPU] Support Hybrid KV Cache for Ascend backend (#18032)

- Full hash: `d9e96153de8a1011c3eb4427af4b3c2e9823e4b2`
- Date/author: 2026-03-26 / gjsheu
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`; `python/sglang/srt/mem_cache/swa_memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bb2989368` - [Fix] Try to fix nvcc compilation error (#21246)

- Full hash: `bb298936891fb6390ee43e6f7ebf635b9954cc9b`
- Date/author: 2026-03-26 / DarkSharpness
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `python/sglang/jit_kernel/all_reduce.py`, `python/sglang/jit_kernel/include/sgl_kernel/distributed/custom_all_reduce.cuh`, `python/sglang/jit_kernel/tests/test_custom_all_reduce.py`, `test/README.md`, `test/run_suite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`; `.github/workflows/pr-test-jit-kernel.yml`
  - runtime-perf: `python/sglang/jit_kernel/all_reduce.py`; `python/sglang/jit_kernel/include/sgl_kernel/distributed/custom_all_reduce.cuh`
  - tests: `python/sglang/jit_kernel/tests/test_custom_all_reduce.py`; `test/README.md`; `test/run_suite.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a34e9ed64` - Add adjusted_filter_batch (#21260)

- Full hash: `a34e9ed64adeb7b9f3b3809390e33f1ee87a2080`
- Date/author: 2026-03-25 / Aurick Qiao
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/sampling/sampling_batch_info.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/sampling/sampling_batch_info.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `53c1d8e96` - Fix customized_info offset truncation (#21262)

- Full hash: `53c1d8e963888fee0c3330491be7204f82a7b64b`
- Date/author: 2026-03-25 / Aurick Qiao
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/scheduler_output_processor_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/managers/scheduler_output_processor_mixin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1100b9865` - Fix MxInt4 MoE returning wrong output variable (#21348)

- Full hash: `1100b9865c48219e74887a60274f6d7a134bbb60`
- Date/author: 2026-03-25 / Sam Shleifer
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `662635e7a` - fix(sgl-kernel): align wheel METADATA/WHEEL with +cu filename (#21437)

- Full hash: `662635e7a7674b7f83d1a64573c9378455d033e2`
- Date/author: 2026-03-25 / Yanda Cheng
- Auto category: 性能/后端优化
- Main files: `sgl-kernel/rename_wheels.sh`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `sgl-kernel/rename_wheels.sh`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `80389fec0` - [AMD] Fix AMD CI: mark /sglang-checkout as git safe.directory in container (#21423)

- Full hash: `80389fec004394db409e9d04aef263465a3b235c`
- Date/author: 2026-03-25 / Michael
- Auto category: 缺陷修复
- Main files: `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `scripts/ci/amd/amd_ci_start_container.sh`; `scripts/ci/amd/amd_ci_start_container_disagg.sh`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.
