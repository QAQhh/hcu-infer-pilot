# sglang Kimi K2/K2.5/Linear/VL Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| - | no local-only commit |

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
| 2026-03-30 | `2b0bed239` | 性能/后端优化 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |

## Per-Commit Audit Cards

### Commit `2b0bed239` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- Full hash: `2b0bed23943bee2e93916979aabc272268a11a1c`
- Date/author: 2026-03-30 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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
- Commits in this section: 25 (merges: 2)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/kimi_k3.py` | `c4212e944`, `ddbbccde8`, `4c219c5f3`, `8eb6acd22`, `c9a84fca9`, `ae065131d`, `e7fb26db7` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `785804bfb`, `12ba645c7`, `68d20891f`, `38cdca36f`, `88f910e94` |
| `python/sglang/srt/layers/attn_residual.py` | `a6ce82576`, `00468ade3`, `6de39e28a`, `c9a84fca9` |
| `python/sglang/kernels/ops/attention/fla/fused_recurrent.py` | `a6ce82576`, `8084b5cac`, `6de39e28a` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `38eea340e`, `68d20891f`, `38cdca36f` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `561186ca9`, `ddbbccde8`, `4c219c5f3` |
| `python/sglang/kernels/ops/attention/fla/chunk_intra.py` | `a6ce82576`, `6de39e28a` |
| `python/sglang/kernels/ops/attention/fla/kda.py` | `a6ce82576`, `6de39e28a` |
| `python/sglang/kernels/ops/attention/fla/kda_hcu.py` | `a6ce82576`, `6de39e28a` |
| `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py` | `a6ce82576`, `6de39e28a` |
| `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | `68d20891f`, `88f910e94` |
| `python/sglang/srt/distributed/parallel_state.py` | `ddbbccde8`, `c9a84fca9` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `8084b5cac`, `9c60fd0fd` |
| `python/sglang/srt/layers/attention/hcu_mla_backend.py` | `561186ca9`, `5b6302252` |
| `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py` | `a6ce82576`, `da90edf06` |
| `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` | `6de39e28a`, `c9a84fca9` |
| `python/sglang/srt/server_args.py` | `38eea340e`, `ddbbccde8` |
| `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py` | `ddbbccde8`, `8eb6acd22` |
| `.github/workflows/nightly-test-hcu.yml` | `2b4271498` |
| `.gitignore` | `c9a84fca9` |
| `python/sglang/kernels/aot/setup_hip.py` | `ddbbccde8` |
| `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh` | `9c60fd0fd` |
| `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh` | `9c60fd0fd` |
| `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh` | `9c60fd0fd` |
| `python/sglang/kernels/npu_kernels/__init__.py` | `c4212e944` |
| `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py` | `c4212e944` |
| `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py` | `c4212e944` |
| `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py` | `c4212e944` |
| `python/sglang/kernels/npu_kernels/npu_moe_finalize_routing_triton.py` | `c4212e944` |
| `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py` | `c4212e944` |
| `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py` | `c4212e944` |
| `python/sglang/kernels/ops/attention/decode_attention.py` | `561186ca9` |
| `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py` | `ddbbccde8` |
| `python/sglang/kernels/ops/attention/extend_attention.py` | `561186ca9` |
| `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py` | `6de39e28a` |
| `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py` | `c9a84fca9` |
| `python/sglang/kernels/ops/kimi_k3/__init__.py` | `785804bfb` |
| `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py` | `c9a84fca9` |
| `python/sglang/kernels/ops/kimi_k3/csrc/mla_post_hip.cu` | `c9a84fca9` |
| `python/sglang/kernels/ops/kimi_k3/mla_post_hip.py` | `c9a84fca9` |
| ... | 70 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-08-07 | `2b4271498` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` and 11 files in total |
| 2026-07-30 | `785804bfb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix triton moe path but accuracy fail | `python/sglang/kernels/ops/kimi_k3/__init__.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/mxfp4.py` |
| 2026-08-06 | `a6ce82576` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support flash kda, hcu triton kda and hcu triton attn residual | `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/kda.py` and 8 files in total |
| 2026-08-07 | `12ba645c7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support WFP4A16 hipc moe for kimi-k3 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-08-11 | `8084b5cac` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | merge: fix kimi-k3 merge conflict | `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-08-11 | `9c60fd0fd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix situ activation jit error | `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh` and 4 files in total |
| 2026-08-13 | `00468ade3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf: route K3 attention-residual aggregation to the HCU kernel on large batches | `python/sglang/srt/layers/attn_residual.py` |
| 2026-08-13 | `38eea340e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: correct Kimi-K3 INT4 MoE accuracy via slimquant quant Triton W4A16 path | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/server_args.py` |
| 2026-08-15 | `68d20891f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: refactor kimi k3 int4 moe for activate 8 or 16 bit | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` and 4 files in total |
| 2026-08-18 | `38cdca36f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support w4a8 hipc moe for k3 int4_w4a16 model | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-19 | `c4212e944` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 适配kimi-k3-w4a8-huawei | `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py`, `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py` and 17 files in total |
| 2026-08-20 | `6de39e28a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | refactor(hcu): replace vendored KDA kernels with boltops | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py` and 8 files in total |
| 2026-08-25 | `88f910e94` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: preserve release fuse_swiglu with source Kimi MoE | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-08-26 | `5c6fb2e29` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #236 from daishiqiang123/20260825_v0.5.18_kimi_k3 | no direct file change / merge |
| 2026-08-27 | `561186ca9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | kimi-k3 dspark support (#249) | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py` and 4 files in total |
| 2026-08-27 | `2ec9f04ae` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]: use aiter moe for kimi-k3-w4a8-huawei | `python/sglang/srt/layers/quantization/modelslim/aiter_w4a8.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py` |
| 2026-08-29 | `ea6b50308` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Merge pull request #260 from daishiqiang123/0.5.18_kimi_deepep_fix | no direct file change / merge |
| 2026-09-01 | `ddbbccde8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(dsv4): support PP/DSpark and CP-aware sparse prefill on HCU (#274) | `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` and 32 files in total |
| 2026-09-20 | `4c219c5f3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | opt: opt dense moe ag and nonzero bubble (#406) | `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/srt/environ.py` and 5 files in total |
| 2026-09-20 | `8eb6acd22` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(moe): support EPLB for Kimi K3 with DSpark bug fix (#411) | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py` and 5 files in total |
| 2026-10-12 | `c9a84fca9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Perf][HCU] Optimize Kimi K3 decode fusions 20261010 (#507) | `.gitignore`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py` and 17 files in total |
| 2026-10-15 | `5b6302252` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): keep packed FP8 Q on the old MLA path for Kimi K3 (#537) | `python/sglang/srt/layers/attention/hcu_mla_backend.py` |
| 2026-10-16 | `ae065131d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(kimi-k3): add opt-in serial shared-expert overlap for DeepEP (#540) | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/k3_sbo_gemm.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` and 6 files in total |
| 2026-10-16 | `da90edf06` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(k3): fix aiter ar shape mismatch and some entries accept rate=1 (#546) | `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/logits_processor.py` |
| 2026-10-23 | `e7fb26db7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(acc): fix k3-int4 tp16 acc wrong (#587) | `python/sglang/srt/models/kimi_k3.py` |

### Per-Commit Audit Cards

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

#### Commit `785804bfb` - fix triton moe path but accuracy fail

- Full hash: `785804bfb994a0afb14e936b163be40803190d28`
- Date/author: 2026-07-30 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/kimi_k3/__init__.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/mxfp4.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/kimi_k3/__init__.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/mxfp4.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `a6ce82576` - feat: support flash kda, hcu triton kda and hcu triton attn residual

- Full hash: `a6ce82576e49f7456af4b83d1bae95625e26bb89`
- Date/author: 2026-08-06 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/kernels/ops/attention/fla/kda_hcu.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/attn_residual.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/attn_residual.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/chunk_intra.py`; `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`; `python/sglang/kernels/ops/attention/fla/kda.py`; `python/sglang/kernels/ops/attention/fla/kda_hcu.py`; `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`; `python/sglang/srt/layers/attention/linear/kda_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `12ba645c7` - feat: support WFP4A16 hipc moe for kimi-k3

- Full hash: `12ba645c77fd34eb18379b2bd7dc503f25a3b4e9`
- Date/author: 2026-08-07 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `8084b5cac` - merge: fix kimi-k3 merge conflict

- Full hash: `8084b5cacf215104abd62eb2e5e548a0f019302a`
- Date/author: 2026-08-11 / zhaosong1
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `9c60fd0fd` - fix: fix situ activation jit error

- Full hash: `9c60fd0fdffdc9fa0ad89e7ecf0bf046482a4d62`
- Date/author: 2026-08-11 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh`, `python/sglang/srt/layers/attention/flashattention_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`; `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`; `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh`; `python/sglang/srt/layers/attention/flashattention_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `00468ade3` - perf: route K3 attention-residual aggregation to the HCU kernel on large batches

- Full hash: `00468ade31979fcdedd2b1586b62219ad7c26dfc`
- Date/author: 2026-08-13 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attn_residual.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/attn_residual.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `38eea340e` - fix: correct Kimi-K3 INT4 MoE accuracy via slimquant quant Triton W4A16 path

- Full hash: `38eea340e42d537d77f6d3a6f651de46e04b5ad5`
- Date/author: 2026-08-13 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `68d20891f` - fix: refactor kimi k3 int4 moe for activate 8 or 16 bit

- Full hash: `68d20891ff89194d21c6197b47a60a2d3e8b2f4d`
- Date/author: 2026-08-15 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `38cdca36f` - feat: support w4a8 hipc moe for k3 int4_w4a16 model

- Full hash: `38cdca36fe2c8fb27b4ae5475fe99e9a65f12faa`
- Date/author: 2026-08-18 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `c4212e944` - 适配kimi-k3-w4a8-huawei

- Full hash: `c4212e94422f5cbe6d1519398ce7003b913a2f25`
- Date/author: 2026-08-19 / WuFan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py`, `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py`, `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_moe_finalize_routing_triton.py`, `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py`, `python/sglang/srt/hardware_backend/npu/moe/activation.py` 等 17 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/kernels/npu_kernels/__init__.py`; `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py`; `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py`; `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py`; `python/sglang/kernels/npu_kernels/npu_moe_finalize_routing_triton.py`; `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py`; `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py`; `python/sglang/srt/hardware_backend/npu/moe/activation.py` 等 16 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `6de39e28a` - refactor(hcu): replace vendored KDA kernels with boltops

- Full hash: `6de39e28a3e6cc03cfb88f71d1c3382dafe34427`
- Date/author: 2026-08-20 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/kernels/ops/attention/fla/kda_hcu.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`, `python/sglang/srt/layers/attn_residual.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/attn_residual.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`; `python/sglang/kernels/ops/attention/fla/chunk_intra.py`; `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`; `python/sglang/kernels/ops/attention/fla/kda.py`; `python/sglang/kernels/ops/attention/fla/kda_hcu.py`; `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`; `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `88f910e94` - fix: preserve release fuse_swiglu with source Kimi MoE

- Full hash: `88f910e94553c50210cd42e4a278c6afbba41b6c`
- Date/author: 2026-08-25 / shiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `5c6fb2e29` - Merge pull request #236 from daishiqiang123/20260825_v0.5.18_kimi_k3

- Full hash: `5c6fb2e29f5211aac83ad24378771464baec4ac2`
- Date/author: 2026-08-26 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `561186ca9` - kimi-k3 dspark support (#249)

- Full hash: `561186ca93c8630038574e78654e2a517cb8f8e7`
- Date/author: 2026-08-27 / jiafei96
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/attention/decode_attention.py`; `python/sglang/kernels/ops/attention/extend_attention.py`; `python/sglang/srt/layers/attention/hcu_mla_backend.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2ec9f04ae` - [feat]: use aiter moe for kimi-k3-w4a8-huawei

- Full hash: `2ec9f04ae224b3d5a39bab76c17f7b11772a5f6e`
- Date/author: 2026-08-27 / WuFan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/modelslim/aiter_w4a8.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/modelslim/aiter_w4a8.py`; `python/sglang/srt/layers/quantization/modelslim/modelslim.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `ea6b50308` - Merge pull request #260 from daishiqiang123/0.5.18_kimi_deepep_fix

- Full hash: `ea6b50308e972d67bfbce1fb1eed9bbb019c38d5`
- Date/author: 2026-08-29 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `ddbbccde8` - feat(dsv4): support PP/DSpark and CP-aware sparse prefill on HCU (#274)

- Full hash: `ddbbccde8cc167817faf2f643dfd79c6f4f9e6e6`
- Date/author: 2026-09-01 / JingLee
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` 等 32 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/nixl/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/managers/utils.py`; `python/sglang/srt/speculative/dspark_components/dspark_kv_inject.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner_components/layer_setup.py`; `python/sglang/srt/model_executor/runner_utils/buffers.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/deepseek_v4_dspark.py`; `python/sglang/srt/models/dspark.py`; `python/sglang/srt/models/kimi_k3.py`; `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/server_args.py` 等 10 个文件
  - runtime-perf: `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`; `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` 等 11 个文件
  - tests: `test/registered/unit/disaggregation/test_disaggregation_wire.py`; `test/registered/unit/disaggregation/test_pp_pd_consensus.py`; `test/registered/unit/spec/test_dspark_pp_context.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `4c219c5f3` - opt: opt dense moe ag and nonzero bubble (#406)

- Full hash: `4c219c5f307b655b42b198737229c391f5988900`
- Date/author: 2026-09-20 / daishiqiang123
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/kimi_k3.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/kernels/ops/kvcache/__init__.py`; `python/sglang/kernels/ops/kvcache/cache_move.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `8eb6acd22` - feat(moe): support EPLB for Kimi K3 with DSpark bug fix (#411)

- Full hash: `8eb6acd22bca671c36219947cd25df4be1ef8ef2`
- Date/author: 2026-09-20 / daishiqiang123
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `test/manual/ep/test_kimi_k3_eplb.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/speculative/dspark_components/dspark_verify.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/kimi_k3.py`; `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`
  - tests: `test/manual/ep/test_kimi_k3_eplb.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `c9a84fca9` - [Perf][HCU] Optimize Kimi K3 decode fusions 20261010 (#507)

- Full hash: `c9a84fca9624adb32d1848a05298a39ca6f0409f`
- Date/author: 2026-10-12 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `.gitignore`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py`, `python/sglang/kernels/ops/kimi_k3/csrc/mla_post_hip.cu`, `python/sglang/kernels/ops/kimi_k3/mla_post_hip.py`, `python/sglang/kernels/ops/mamba/csrc/mamba_state_indices_hip.cu`, `python/sglang/kernels/ops/mamba/mamba_state_indices.py`, `python/sglang/kernels/ops/mamba/mamba_state_indices_hip.py` 等 17 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `.gitignore`; `python/sglang/srt/layers/attn_residual.py`; `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py`; `python/sglang/kernels/ops/kimi_k3/csrc/mla_post_hip.cu`; `python/sglang/kernels/ops/kimi_k3/mla_post_hip.py`; `python/sglang/kernels/ops/mamba/csrc/mamba_state_indices_hip.cu`; `python/sglang/kernels/ops/mamba/mamba_state_indices.py`; `python/sglang/kernels/ops/mamba/mamba_state_indices_hip.py`; `python/sglang/srt/distributed/parallel_state.py` 等 12 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `5b6302252` - fix(hcu): keep packed FP8 Q on the old MLA path for Kimi K3 (#537)

- Full hash: `5b630225295b1bc1e510cfb5fd25e8f9521acef8`
- Date/author: 2026-10-15 / lipenghui
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/hcu_mla_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/hcu_mla_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `ae065131d` - feat(kimi-k3): add opt-in serial shared-expert overlap for DeepEP (#540)

- Full hash: `ae065131d82c45bf7135761091fb77b718c5df66`
- Date/author: 2026-10-16 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/k3_sbo_gemm.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/kimi_k3.py`, `test/manual/hcu/test_kimi_k3_serial_sbo.py`, `test/registered/unit/models/test_kimi_k3_serial_sbo.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/layers/k3_sbo_gemm.py`
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
  - tests: `test/manual/hcu/test_kimi_k3_serial_sbo.py`; `test/registered/unit/models/test_kimi_k3_serial_sbo.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `da90edf06` - fix(k3): fix aiter ar shape mismatch and some entries accept rate=1 (#546)

- Full hash: `da90edf068c9a574c3a9e3e7ad69229440edfa01`
- Date/author: 2026-10-16 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/logits_processor.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/logits_processor.py`
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `e7fb26db7` - fix(acc): fix k3-int4 tp16 acc wrong (#587)

- Full hash: `e7fb26db710c97fd1e445eef9df3a7ca71b26ccf`
- Date/author: 2026-10-23 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/kimi_k3.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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
