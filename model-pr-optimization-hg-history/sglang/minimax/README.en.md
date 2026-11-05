# sglang MiniMax M2 Series Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/minimax_m2.py` | `18944a9d3` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 1
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-23 | `18944a9d3` | 模型支持/运行时入口 | support MiniMax M2.5 PP | `python/sglang/srt/models/minimax_m2.py` |

## Per-Commit Audit Cards

### Commit `18944a9d3` - support MiniMax M2.5 PP

- Full hash: `18944a9d392690db20f30c060b33d18e8bf9062c`
- Date/author: 2026-04-23 / guizhh
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/minimax_m2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## Local-only dev branch update from v0.5.8_dev to v0.5.12_dev

### Coverage Note

- Source index: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- Source worktree: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs.
- Commits in this section: 2
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-03-30 | `00db89c86` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |
| 2026-03-30 | `7bfdade34` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |

### Per-Commit Audit Cards

#### Commit `00db89c86` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- Full hash: `00db89c86ed93c08a883ffa6b708babf8e89743c`
- Date/author: 2026-03-30 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `7bfdade34` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- Full hash: `7bfdade34395bd4ae7c723b64de68a990820d0b2`
- Date/author: 2026-03-30 / maxiao1
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 21 (merges: 3)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `1e2fec228`, `123e9539e`, `8effe1350`, `cda280cdf`, `729879dce` |
| `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` | `d76d3f185`, `12c25ba52`, `0ac3b2f83`, `5c859fcfd` |
| `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` | `d76d3f185`, `e04856c1d`, `ce113101c`, `5c859fcfd` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `1e2fec228`, `123e9539e`, `4d9f46783`, `8effe1350` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py` | `d76d3f185`, `c496509fb`, `2df2a10f8` |
| `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py` | `d76d3f185`, `a12acccb2`, `5c859fcfd` |
| `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py` | `d76d3f185`, `a12acccb2`, `5c859fcfd` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/layernorm.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/moe/moe_runner/aiter.py` | `1e2fec228`, `8effe1350`, `5f31aec46` |
| `python/sglang/srt/layers/moe/topk.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | `1e2fec228`, `123e9539e`, `4d9f46783` |
| `python/sglang/srt/layers/quantization/w8a8_int8.py` | `1e2fec228`, `123e9539e`, `4d9f46783` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/model_executor/model_runner.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/models/minimax_m3.py` | `8effe1350`, `5f31aec46`, `cda280cdf` |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `8effe1350` |
| `python/sglang/srt/utils/common.py` | `1e2fec228`, `d76d3f185`, `8effe1350` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/aot/csrc/common_extension_rocm.cc` | `8effe1350`, `0ac3b2f83` |
| `python/sglang/kernels/aot/setup_hip.py` | `8effe1350`, `0ac3b2f83` |
| `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | `1e2fec228`, `4d9f46783` |
| `python/sglang/kernels/ops/speculative/cache_locs.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py` | `c496509fb`, `2df2a10f8` |
| `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py` | `123e9539e`, `d76d3f185` |
| `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py` | `0ac3b2f83`, `5c859fcfd` |
| `python/sglang/multimodal_gen/runtime/layers/usp.py` | `d76d3f185`, `5c859fcfd` |
| `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vit_utils.py` | `d76d3f185`, `0ac3b2f83` |
| `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py` | `d76d3f185`, `a12acccb2` |
| `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py` | `d76d3f185`, `c496509fb` |
| `python/sglang/multimodal_gen/runtime/server_args/server_args.py` | `d76d3f185`, `56a4faa68` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `1e2fec228`, `8effe1350` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
| ... | 332 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` and 109 files in total |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` and 91 files in total |
| 2026-08-07 | `4d9f46783` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] fix the lmslim and lightop calling issues regressions | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` and 6 files in total |
| 2026-08-07 | `2b4271498` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` and 11 files in total |
| 2026-08-10 | `d76d3f185` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | Adapt MiniMax-H3 for v0.5.15 | `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py` and 84 files in total |
| 2026-08-10 | `abe7d784d` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | Merge pull request #182 from HYGON-AI/sglang_minimax-h3-adapt | no direct file change / merge |
| 2026-08-20 | `12c25ba52` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [fix][minimax-h3]: fix HCU QK-Norm fallback and backend resolution | `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` |
| 2026-08-20 | `56a4faa68` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [fix][minimax-h3]: default HCU component attention backends | `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py` |
| 2026-08-24 | `0d49fbb93` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #215 from s1mplezpc/zhangpc3_minimax_h3_dev | no direct file change / merge |
| 2026-08-25 | `e04856c1d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(minimax-h3): allow HCU full-loop denoise | `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` |
| 2026-08-25 | `ce113101c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(minimax-h3): avoid sharing refined prompts with CacheDiT | `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` |
| 2026-08-26 | `530d6363b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #231 from s1mplezpc/0518-minimaxh3-dev | no direct file change / merge |
| 2026-09-20 | `c496509fb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(mmgen): declare MiniMax H3 request extensions in the OpenAPI document (#399) | `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py` and 4 files in total |
| 2026-09-23 | `2df2a10f8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(mmgen): align MiniMax H3 OpenAPI contract (#426) | `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py` |
| 2026-09-30 | `8effe1350` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(minimax-m3): optimize prefill and decode on HCU gfx938 (#453) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py` and 140 files in total |
| 2026-10-14 | `5f31aec46` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(aiter): avoid duplicate MoE weights outside MiniMax-M3 (#526) | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/models/minimax_m3.py` and 6 files in total |
| 2026-10-14 | `0ac3b2f83` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(MiniMax-H3): support MiniMax-H3 channel-wise INT8/FP8 inference on HCU (#532) | `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h` and 9 files in total |
| 2026-10-21 | `cda280cdf` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Fix] moe: Restrict DeepEPMoE runner delegation to MiniMax-M3 (#577) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py` and 4 files in total |
| 2026-10-23 | `a12acccb2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(minimax-h3): avoid full-video clone in VAE postprocessing (#583) | `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py` |
| 2026-10-31 | `5c859fcfd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Fix] minimax-h3: prevent repeated-request OOM and fix row-quantization dispatch (#629) | `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` and 6 files in total |
| 2026-11-03 | `729879dce` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Fix] quantization: 修复 INT4/INT8 混合量化模型加载 (#631) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py` |

### Per-Commit Audit Cards

#### Commit `1e2fec228` - feat(hcu): port runtime and kernel rename

- Full hash: `1e2fec228a9a8b1e781c3592eff356eeb8b584ed`
- Date/author: 2026-07-20 / tianlinyang77
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/jit_kernel/dsv4/moe.py`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/mxfp8.py` 等 109 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/check_env.py`; `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/fp8_blockwise_gemm.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/mxfp8.py`; `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` 等 80 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `sgl-kernel/tests/test_moe_align.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `123e9539e` - fix lint: satisfy pre-commit on the forward-port diff

- Full hash: `123e9539ea23dde2f1a12b0374c1375bbfb10989`
- Date/author: 2026-07-31 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py` 等 91 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py` 等 14 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py` 等 19 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py` 等 56 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_mmlu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `4d9f46783` - [BugFix] fix the lmslim and lightop calling issues regressions

- Full hash: `4d9f467839a30162175d1cfc7e0d0f11862fcffd`
- Date/author: 2026-08-07 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2b4271498` - ci(hcu): publish nine-model accuracy results

- Full hash: `2b4271498f3d9031d0080accfa4dea9eccd10a59`
- Date/author: 2026-08-07 / LvJIA-RG
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `d76d3f185` - Adapt MiniMax-H3 for v0.5.15

- Full hash: `d76d3f185d95025e63aad11ee3f65abe4b78f37e`
- Date/author: 2026-08-10 / yuchenyang
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py`, `python/sglang/kernels/ops/diffusion/triton/indexed_modulation.py`, `python/sglang/kernels/ops/diffusion/triton/scale_shift.py`, `python/sglang/kernels/ops/layernorm/norm.py`, `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/configs/models/encoders/minimax_h3_qwen3vl.py` 等 84 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`; `python/sglang/multimodal_gen/runtime/pipelines/minimax_h3_pipeline.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/decoding.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/__init__.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/canvas.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/condition_noise.py` 等 35 个文件
  - runtime-model: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/configs/models/encoders/minimax_h3_qwen3vl.py`; `python/sglang/multimodal_gen/configs/models/vaes/minimax_h3_audio.py`; `python/sglang/multimodal_gen/configs/models/vaes/minimax_h3_contract.py`; `python/sglang/multimodal_gen/configs/models/vaes/minimax_h3_video.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`; `python/sglang/multimodal_gen/configs/sample/minimax_h3.py` 等 28 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`; `python/sglang/kernels/ops/activation/activation.py`; `python/sglang/kernels/ops/diffusion/qknorm_rope.py`; `python/sglang/kernels/ops/diffusion/triton/indexed_modulation.py`; `python/sglang/kernels/ops/diffusion/triton/scale_shift.py`; `python/sglang/kernels/ops/layernorm/norm.py`; `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py` 等 15 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_minimax_h3_admission.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_denoise_loop.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_media.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_packed_sequence.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vae_parallel_modes.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `abe7d784d` - Merge pull request #182 from HYGON-AI/sglang_minimax-h3-adapt

- Full hash: `abe7d784d82c304000ad760af13356f2d74f56fd`
- Date/author: 2026-08-10 / lizhigong
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `12c25ba52` - [fix][minimax-h3]: fix HCU QK-Norm fallback and backend resolution

- Full hash: `12c25ba52859ab130655399e9c1750879bee7d7e`
- Date/author: 2026-08-20 / zhangpc3
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `56a4faa68` - [fix][minimax-h3]: default HCU component attention backends

- Full hash: `56a4faa68a55f3ab300d32156f6860578dc10503`
- Date/author: 2026-08-20 / zhangpc3
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `0d49fbb93` - Merge pull request #215 from s1mplezpc/zhangpc3_minimax_h3_dev

- Full hash: `0d49fbb937fbed3909361ae2f4cb9996177d321a`
- Date/author: 2026-08-24 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `e04856c1d` - fix(minimax-h3): allow HCU full-loop denoise

- Full hash: `e04856c1d4613fcfbc39aa0ed88bc5d3ad5153d7`
- Date/author: 2026-08-25 / Codex
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `ce113101c` - fix(minimax-h3): avoid sharing refined prompts with CacheDiT

- Full hash: `ce113101ca7d946ccd9ef0a1db8c1d876b7c7c19`
- Date/author: 2026-08-25 / zhangpc3
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `530d6363b` - Merge pull request #231 from s1mplezpc/0518-minimaxh3-dev

- Full hash: `530d6363b30262d10286610938a45e8219306784`
- Date/author: 2026-08-26 / YuanYuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `c496509fb` - fix(mmgen): declare MiniMax H3 request extensions in the OpenAPI document (#399)

- Full hash: `c496509fbbf73b0acb7875652cf640791a778294`
- Date/author: 2026-09-20 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`, `python/sglang/srt/function_call/function_call_parser.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`; `python/sglang/srt/function_call/function_call_parser.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `2df2a10f8` - fix(mmgen): align MiniMax H3 OpenAPI contract (#426)

- Full hash: `2df2a10f818a0bf88a2a0b6ac97a3dd919b608f6`
- Date/author: 2026-09-23 / Phy
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `8effe1350` - feat(minimax-m3): optimize prefill and decode on HCU gfx938 (#453)

- Full hash: `8effe13508725f3c871dceb5dfbfbbfc6f959a89`
- Date/author: 2026-09-30 / WenQ7
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py`, `python/sglang/benchmark/serving.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/activation.cu`, `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`, `python/sglang/kernels/aot/include/utils.h` 等 140 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/minimax_router_gemv.py`
  - other: `python/sglang/benchmark/serving.py`; `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/eplb_manager.py`; `python/sglang/srt/eplb/expert_distribution.py`; `python/sglang/srt/eplb/expert_location_dispatch.py`; `python/sglang/srt/eplb/load_aware_dispatch.py`; `python/sglang/srt/eplb/lplb_solver.py` 等 19 个文件
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`; `python/sglang/srt/model_executor/cpu_graph_runner.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/runner/eager_runner.py`; `python/sglang/srt/models/llama_eagle3.py` 等 14 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/activation.cu`; `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`; `python/sglang/kernels/aot/include/utils.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`; `python/sglang/kernels/jit/csrc/moe/moe_topk_sigmoid.cuh` 等 65 个文件
  - tests: `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`; `test/registered/attention/test_verify_shared_kv.py`; `test/registered/cp/test_cp_strategy_unit.py`; `test/registered/kernels/ops/attention/test_minimax_prefill_grouped_union.py`; `test/registered/kernels/ops/attention/test_verify_mla_split_policy.py`; `test/registered/kernels/ops/kvcache/test_scaled_fp8_kv_store.py`; `test/registered/kernels/ops/speculative/test_draft_extend_kv_metadata.py` 等 39 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `5f31aec46` - fix(aiter): avoid duplicate MoE weights outside MiniMax-M3 (#526)

- Full hash: `5f31aec46b5e557fc00e891e8d91bcdb2e4c6b3b`
- Date/author: 2026-10-14 / WenQ7
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/unit/layers/moe/test_aiter_runner.py`, `test/registered/unit/layers/moe/test_aiter_weight_layout.py`, `test/registered/unit/models/test_minimax_m3_eplb.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/minimax_m3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/moe/moe_runner/base.py`
  - tests: `test/registered/unit/layers/moe/test_aiter_runner.py`; `test/registered/unit/layers/moe/test_aiter_weight_layout.py`; `test/registered/unit/models/test_minimax_m3_eplb.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `0ac3b2f83` - feat(MiniMax-H3): support MiniMax-H3 channel-wise INT8/FP8 inference on HCU (#532)

- Full hash: `0ac3b2f83eb8c7a57f534810c035dc0feb973cd3`
- Date/author: 2026-10-14 / s1mplezpc
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h`, `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` 等 9 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vit_utils.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `cda280cdf` - [Fix] moe: Restrict DeepEPMoE runner delegation to MiniMax-M3 (#577)

- Full hash: `cda280cdf5a9a968536cb3ae8b5fdb7a4c586d05`
- Date/author: 2026-10-21 / WenQ7
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`, `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/minimax_m3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
  - tests: `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`; `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `a12acccb2` - fix(minimax-h3): avoid full-video clone in VAE postprocessing (#583)

- Full hash: `a12acccb2237d008407061130053e6135701a05b`
- Date/author: 2026-10-23 / s1mplezpc
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `5c859fcfd` - [Fix] minimax-h3: prevent repeated-request OOM and fix row-quantization dispatch (#629)

- Full hash: `5c859fcfdba2ff1089f223612ec292b8365a1b47`
- Date/author: 2026-10-31 / s1mplezpc
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `729879dce` - [Fix] quantization: 修复 INT4/INT8 混合量化模型加载 (#631)

- Full hash: `729879dce06763c0ed7b15c5edca084a69557507`
- Date/author: 2026-11-03 / Songge
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
  - tests: `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## Local-only branch update from release/20260825_v0.5.18 to release_v0.5.18_deepseekv4

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-05
- Commits in this section: 0 (merges: 0)
- Branch segments: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

- No local-only commit in these branch segments belongs to this bucket.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
