# sglang Shared Framework Commits Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| ... | 2951 more files omitted from table; all were used for git tracing. |

| - | no local-only commit |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 53
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

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

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## Local-only dev branch update from v0.5.8_dev to v0.5.12_dev

### Coverage Note

- Source index: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- Source worktree: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs.
- Commits in this section: 68
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-02-27 | `155c1f634` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | sglang dcu 0.5.9base patch->hash(5dd49e07) | `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` 等 104 个文件 |
| 2026-02-27 | `1dd77c2e6` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev' | `README_DCU.md`, `requirements_dcu.txt` |
| 2026-02-27 | `356694d6b` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-1dfc3015' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-02-27 | `403027fd8` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-02-27 | `8a6520cd8` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-3b73900b' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-02-27 | `c77a90449` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | Debugging through TP parallel | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `sgl-kernel/setup_hip.py` |
| 2026-02-27 | `d62ea43c1` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev' | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-03-06 | `a5c071e36` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-fc0f9e89' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-06 | `b3f4b0861` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.8_dev_sxl' into 'v0.5.8_dev' | `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py` 等 12 个文件 |
| 2026-03-06 | `b930b5645` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-07 | `5d7c6b671` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.8_dev_mx' into 'v0.5.8_dev' | `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` 等 5 个文件 |
| 2026-03-07 | `686124d90` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | 适配fuse_moe_fp8_w8a8 | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-03-07 | `76c737ac7` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-07 | `8ba520fcc` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | fix error when set dtype float16 | `python/sglang/srt/layers/quantization/unquant.py` |
| 2026-03-07 | `c5a76ad9e` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-a16f19db' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-07 | `e687d64ce` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-11 | `37689613c` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 修复pd分离开启ttft优化首字偶发精度问题 & 修复pd分离decode卡住、精度问题 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-03-11 | `3e822f7ad` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_pd' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-13 | `5db31f4b4` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-214917d1' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-13 | `8f3e9df94` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-4d97fa3d-to-059' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-13 | `c64ac4481` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-0955197e' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-13 | `e850c8d2c` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.8_dev_yiqa' into 'v0.5.8_dev' | `python/sglang/srt/layers/quantization/fp8_kernel.py` |
| 2026-03-13 | `ee5b7ebb6` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'cherry-pick-e18f065f' into 'v0.5.8_dev' | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-03-16 | `23fd42261` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-16 | `c2f921462` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 修复bailing模型大ep无法启动 | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` 等 4 个文件 |
| 2026-03-20 | `b54acd50f` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-20 | `fc5981e07` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | bailing模型支持EP模式下开启rms+quant算子融合 | `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/bailing_moe.py` |
| 2026-03-22 | `d34753123` | `v0.5.8_dev..v0.5.9_dev` | 调度/缓存/PD | pd分离p端加上日志 | `python/sglang/srt/disaggregation/prefill.py` |
| 2026-03-23 | `3f30edf9a` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 修复059版本函数名字修改导致的报错 | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-03-23 | `79a11f9bb` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-23 | `886fbccec` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev' | 无直接文件变更/merge |
| 2026-03-26 | `e845e0ead` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb | `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` 等 7 个文件 |
| 2026-03-27 | `2b4435fa5` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | fis bug | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-03-30 | `48739c3ac` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb | 无直接文件变更/merge |
| 2026-03-30 | `b15505653` | `v0.5.8_dev..v0.5.9_dev` | 测试/文档/基线合入 | update readme about dcu | `README_DCU.md` |
| 2026-03-30 | `f9ea5254d` | `v0.5.8_dev..v0.5.9_dev` | 性能/后端优化 | add torch version hadamard_transform_optimized() | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-03-31 | `70c416ca9` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1 | `python/sglang/srt/models/qwen2.py` |
| 2026-04-01 | `c2ffad7df` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 修复开融合算子后传参逻辑 | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` |
| 2026-03-30 | `c5eb17125` | `v0.5.9_dev..v0.5.10_dev` | 测试/文档/基线合入 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` 等 114 个文件 |
| 2026-03-30 | `f9d9b0204` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 解决PD分离报错问题 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/overlap_utils.py` 等 7 个文件 |
| 2026-03-31 | `77a4da53b` | `v0.5.9_dev..v0.5.10_dev` | 模型支持/运行时入口 | fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1 | `python/sglang/srt/models/qwen2.py` |
| 2026-04-01 | `236c37f41` | `v0.5.9_dev..v0.5.10_dev` | 模型支持/运行时入口 | 修改环境变量SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING名称为SGLANG_USE_FUSED_RMS_ROTARY | `python/sglang/srt/models/qwen2.py` |
| 2026-04-01 | `8edb7c965` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 修复融合算子并验证精度. | `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` |
| 2026-04-01 | `962c74637` | `v0.5.9_dev..v0.5.10_dev` | 性能/后端优化 | optimized code of layernorm | `python/sglang/srt/layers/layernorm.py` |
| 2026-04-01 | `f2dfc2ec8` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | fix split_qkv_rms_rotary_embedding_fuse_with_kv_store_quant算子的使用bug，此bug影响QwQ-32B模型的性能优化 | `python/sglang/srt/models/qwen2.py` |
| 2026-04-02 | `5bb6dff38` | `v0.5.9_dev..v0.5.10_dev` | 测试/文档/基线合入 | Update README_DCU.md | `README_DCU.md` |
| 2026-04-02 | `70c9a1a6d` | `v0.5.9_dev..v0.5.10_dev` | 测试/文档/基线合入 | Update README_DCU.md | `README_DCU.md` |
| 2026-04-02 | `865ca25a7` | `v0.5.9_dev..v0.5.10_dev` | 测试/文档/基线合入 | Update README_DCU.md | `README_DCU.md` |
| 2026-04-02 | `8d278721f` | `v0.5.9_dev..v0.5.10_dev` | 测试/文档/基线合入 | Update README_DCU.md | `README_DCU.md` |
| 2026-04-03 | `4dd71954e` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | [bugfix]将使能QWQ-32B性能优化的环境变量SGLANG_USE_FUSED_RMS_ROTARY名称修改为SGLANG_USE_FUSED_SPLIT_QKV_RMS_ROTARY_EMBEDDING，解决因此引起的精度问题 | `python/sglang/srt/models/qwen2.py` |
| 2026-04-07 | `50a63c96d` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | fix deepseek log cudagraph init meta data copy error in bmz when capture cudagraph. | `python/sglang/srt/layers/attention/dcu_mla_backend.py` |
| 2026-04-07 | `b4059342f` | `v0.5.9_dev..v0.5.10_dev` | 调度/缓存/PD | 接入causal_conv1d_update优化算子 | `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-04-08 | `7104fdb72` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 解决FA报错问题 | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-04-09 | `22e5ac5b1` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | Bugfix:fix mm model attention interface | `python/sglang/srt/layers/attention/vision.py` |
| 2026-05-06 | `c200c7845` | `v0.5.10_dev..v0.5.11_dev` | 测试/文档/基线合入 | sglang dcu 0.5.11 base hash(dfb35997) | `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py` 等 131 个文件 |
| 2026-05-07 | `4d897133e` | `v0.5.10_dev..v0.5.11_dev` | 通用实现调整 | Supplement merge | `python/pyproject.toml`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-05-07 | `96a5c116a` | `v0.5.10_dev..v0.5.11_dev` | 缺陷修复 | fix some error in initial version | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py` |
| 2026-04-25 | `a28aa5f97` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix some errors when init server | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8.py` 等 8 个文件 |
| 2026-04-27 | `eec3b3ff8` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix for load model | 无直接文件变更/merge |
| 2026-04-28 | `6ad2adb52` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh` 等 6 个文件 |
| 2026-04-29 | `50b898285` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix mhc with tile 0.1.9 | `python/sglang/srt/layers/mhc.py` |
| 2026-04-29 | `a44cec29b` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix jit for moe_fused_gate | `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` |
| 2026-04-29 | `bb24fa6e1` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | [Feature] support rocm moe_fused_gate | `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh` |
| 2026-05-14 | `fd077165a` | `v0.5.11_dev..v0.5.12_dev` | 缺陷修复 | fix the mtp issues of metadata loc size | `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-05-18 | `c5dd815b3` | `v0.5.11_dev..v0.5.12_dev` | 测试/文档/基线合入 | dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6) | `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py` 等 141 个文件 |
| 2026-05-21 | `411660d35` | `v0.5.11_dev..v0.5.12_dev` | 模型支持/运行时入口 | feat(diffusion): add ROCm SLA attention backend | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py` 等 6 个文件 |
| 2026-05-22 | `f378b1a20` | `v0.5.11_dev..v0.5.12_dev` | 性能/后端优化 | [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0 | `python/sglang/srt/layers/quantization/unquant.py` |
| 2026-05-28 | `18b48e742` | `v0.5.11_dev..v0.5.12_dev` | 性能/后端优化 | moe-runner-backend支持lightop_moe_w8a8 | `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py` 等 5 个文件 |

### Per-Commit Audit Cards

#### Commit `155c1f634` - sglang dcu 0.5.9base patch->hash(5dd49e07)

- Full hash: `155c1f6345bab53c8b26616172893defdc051761`
- Date/author: 2026-02-27 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` 等 104 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3_moe.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/attention/lightop_concat.py`; `python/sglang/srt/layers/attention/nsa_backend.py` 等 64 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - other: `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py` 等 30 个文件
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `1dd77c2e6` - Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev'

- Full hash: `1dd77c2e6e865c3bef8bd225a65938a02c2d1f42`
- Date/author: 2026-02-27 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`, `requirements_dcu.txt`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `README_DCU.md`
  - other: `requirements_dcu.txt`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `356694d6b` - Merge branch 'cherry-pick-1dfc3015' into 'v0.5.9_dev'

- Full hash: `356694d6b92ad51a3306c8ac589425490a6f72c1`
- Date/author: 2026-02-27 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `403027fd8` - Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev'

- Full hash: `403027fd8458cae4cab8c18358f06b948955325b`
- Date/author: 2026-02-27 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `8a6520cd8` - Merge branch 'cherry-pick-3b73900b' into 'v0.5.9_dev'

- Full hash: `8a6520cd86730570c6f2ff26dc7a5bce4b527ac2`
- Date/author: 2026-02-27 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `c77a90449` - Debugging through TP parallel

- Full hash: `c77a904497e951351de67c53cb52ec7dad2ed6a1`
- Date/author: 2026-02-27 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `sgl-kernel/setup_hip.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `sgl-kernel/setup_hip.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `d62ea43c1` - Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev'

- Full hash: `d62ea43c13d89e9a3b372c6d54dac8ed8353a740`
- Date/author: 2026-02-27 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `a5c071e36` - Merge branch 'cherry-pick-fc0f9e89' into 'v0.5.9_dev'

- Full hash: `a5c071e366454178b06e6f18955d3c64966fd75b`
- Date/author: 2026-03-06 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `b3f4b0861` - Merge branch 'v0.5.8_dev_sxl' into 'v0.5.8_dev'

- Full hash: `b3f4b086156d31e528ac3720765535f687782127`
- Date/author: 2026-03-06 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/mem_cache/allocator.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 12 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/communicator.py`
  - other: `python/sglang/srt/mem_cache/allocator.py`; `python/sglang/srt/mem_cache/common.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/speculative/eagle_info.py`; `python/sglang/srt/speculative/eagle_info_v2.py`; `python/sglang/srt/speculative/spec_utils.py`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `b930b5645` - Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev'

- Full hash: `b930b5645eb1978f8867c6f0594138e6cedc09c2`
- Date/author: 2026-03-06 / liucong8560
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `5d7c6b671` - Merge branch 'v0.5.8_dev_mx' into 'v0.5.8_dev'

- Full hash: `5d7c6b67152f6c381210e9f3e0f62fba4db4ea7f`
- Date/author: 2026-03-07 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/unquant.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/layers/quantization/unquant.py`
  - other: `python/sglang/srt/batch_overlap/single_batch_overlap.py`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `686124d90` - 适配fuse_moe_fp8_w8a8

- Full hash: `686124d90a495d9337f99869cf20fdd7fdd556ba`
- Date/author: 2026-03-07 / liucong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `76c737ac7` - Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev'

- Full hash: `76c737ac7b7b3167d3c57f1ec08c88267f5c4961`
- Date/author: 2026-03-07 / liucong8560
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `8ba520fcc` - fix error when set dtype float16

- Full hash: `8ba520fcc8ce231449229252d52a83f2baede139`
- Date/author: 2026-03-07 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/quantization/unquant.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/unquant.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `c5a76ad9e` - Merge branch 'cherry-pick-a16f19db' into 'v0.5.9_dev'

- Full hash: `c5a76ad9ecdd9894da92d4751f2b596d339e3cd0`
- Date/author: 2026-03-07 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `e687d64ce` - Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev'

- Full hash: `e687d64ce991449877c284d1ddcedc7cb645c159`
- Date/author: 2026-03-07 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `37689613c` - 修复pd分离开启ttft优化首字偶发精度问题 & 修复pd分离decode卡住、精度问题

- Full hash: `37689613cf1056185ef795308cc6cb792c1b10ab`
- Date/author: 2026-03-11 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `3e822f7ad` - Merge branch 'v0.5.9_dev_pd' into 'v0.5.9_dev'

- Full hash: `3e822f7ad0003772608e0b7529e7d347d46d0704`
- Date/author: 2026-03-11 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `5db31f4b4` - Merge branch 'cherry-pick-214917d1' into 'v0.5.9_dev'

- Full hash: `5db31f4b4642449fdaf6d35a43db94ad24747f66`
- Date/author: 2026-03-13 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `8f3e9df94` - Merge branch 'cherry-pick-4d97fa3d-to-059' into 'v0.5.9_dev'

- Full hash: `8f3e9df94c6ec255a7e42f55a9b4e85957dc880b`
- Date/author: 2026-03-13 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `c64ac4481` - Merge branch 'cherry-pick-0955197e' into 'v0.5.9_dev'

- Full hash: `c64ac44818bc201872073f9b581daf3052a754ef`
- Date/author: 2026-03-13 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `e850c8d2c` - Merge branch 'v0.5.8_dev_yiqa' into 'v0.5.8_dev'

- Full hash: `e850c8d2c590ace3a477b2d4631684e55dc48ebe`
- Date/author: 2026-03-13 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `python/sglang/srt/layers/quantization/fp8_kernel.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_kernel.py`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `ee5b7ebb6` - Merge branch 'cherry-pick-e18f065f' into 'v0.5.8_dev'

- Full hash: `ee5b7ebb692396eab6b2be1360f0d56fe49c577f`
- Date/author: 2026-03-13 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `python/sglang/srt/layers/attention/flashattention_interface.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `23fd42261` - Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev'

- Full hash: `23fd42261b8a7f5620becaa4bfe80abd651d812b`
- Date/author: 2026-03-16 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `c2f921462` - 修复bailing模型大ep无法启动

- Full hash: `c2f921462faaf92baecf22d1a23021472fe770b2`
- Date/author: 2026-03-16 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `b54acd50f` - Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev'

- Full hash: `b54acd50f88ff3dcb0c23f396c83fda0b1f5a462`
- Date/author: 2026-03-20 / liucong8560
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `fc5981e07` - bailing模型支持EP模式下开启rms+quant算子融合

- Full hash: `fc5981e071f99c0069ac3e6ede6e78b711aa0728`
- Date/author: 2026-03-20 / liucong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/bailing_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`
  - runtime-perf: `python/sglang/srt/layers/communicator.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `d34753123` - pd分离p端加上日志

- Full hash: `d347531234de2009c6e747b628aea6a4ce469a57`
- Date/author: 2026-03-22 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/prefill.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/prefill.py`
- Risk and verification: Touches scheduling, cache, PD, or MTP paths; verify prefill/decode ordering, first-token correctness, concurrency, and long-context stability.

#### Commit `3f30edf9a` - 修复059版本函数名字修改导致的报错

- Full hash: `3f30edf9aa05c86075746873066fd50f1e97877c`
- Date/author: 2026-03-23 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `79a11f9bb` - Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev'

- Full hash: `79a11f9bb063714ebeeeac7f20da617a7cdb26c6`
- Date/author: 2026-03-23 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `886fbccec` - Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev'

- Full hash: `886fbccec07147749c241985caf3f52ec4acb2fc`
- Date/author: 2026-03-23 / maxiao1
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `e845e0ead` - Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb

- Full hash: `e845e0eadd2d5f636be783ac5a99d1d95d66f29a`
- Date/author: 2026-03-26 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
  - other: `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `2b4435fa5` - fis bug

- Full hash: `2b4435fa5a79ae5d0c19e51094018860bd98e786`
- Date/author: 2026-03-27 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `48739c3ac` - Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb

- Full hash: `48739c3ac64be80745e51a8742523504bc8ef990`
- Date/author: 2026-03-30 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `b15505653` - update readme about dcu

- Full hash: `b15505653f0a936301786b2570a48209ff21dcd9`
- Date/author: 2026-03-30 / lizhigong
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `README_DCU.md`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `f9ea5254d` - add torch version hadamard_transform_optimized()

- Full hash: `f9ea5254d79e28a0583e39e01f64f4b546d37310`
- Date/author: 2026-03-30 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate with prefill/decode traces, end-to-end throughput, and correctness smoke tests before reusing.

#### Commit `70c416ca9` - fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1

- Full hash: `70c416ca947cc7ede81a25e216aed255f017ce93`
- Date/author: 2026-03-31 / chenyue3
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/qwen2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `c2ffad7df` - 修复开融合算子后传参逻辑

- Full hash: `c2ffad7df56d0befafbd449799ab156cbbbfcbcd`
- Date/author: 2026-04-01 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `c5eb17125` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- Full hash: `c5eb171255d709e18146bdd027308aa71ca71c8c`
- Date/author: 2026-03-30 / lizhigong
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py` 等 11 个文件
  - runtime-perf: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/flashmla_backend.py` 等 69 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - docs-bench: `README_DCU.md`
  - other: `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` 等 32 个文件
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `f9d9b0204` - 解决PD分离报错问题

- Full hash: `f9d9b0204997baa59ff4e4af58ad29610109e81f`
- Date/author: 2026-03-30 / liucong
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/bailing_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/model_executor/forward_batch_info.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `77a4da53b` - fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1

- Full hash: `77a4da53b195948f368d09aca59eeff7a84445b0`
- Date/author: 2026-03-31 / chenyue3
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/qwen2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `236c37f41` - 修改环境变量SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING名称为SGLANG_USE_FUSED_RMS_ROTARY

- Full hash: `236c37f410e190d19d32aa6e85f312509ac87ea0`
- Date/author: 2026-04-01 / chenyue3
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/qwen2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `8edb7c965` - 修复融合算子并验证精度.

- Full hash: `8edb7c9650db08be27033956472ebb9247d2eb46`
- Date/author: 2026-04-01 / linhai1
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `962c74637` - optimized code of layernorm

- Full hash: `962c746378e9db0345c1094fdc83c0610bb0fdbe`
- Date/author: 2026-04-01 / chenyue3
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: Touches performance or backend paths; validate with prefill/decode traces, end-to-end throughput, and correctness smoke tests before reusing.

#### Commit `f2dfc2ec8` - fix split_qkv_rms_rotary_embedding_fuse_with_kv_store_quant算子的使用bug，此bug影响QwQ-32B模型的性能优化

- Full hash: `f2dfc2ec8bf1efd51c494afa69dcf2261f47b0d8`
- Date/author: 2026-04-01 / chenyue3
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `5bb6dff38` - Update README_DCU.md

- Full hash: `5bb6dff38e0a5a5c40362517df95bdbdf53580b3`
- Date/author: 2026-04-02 / guobj
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `README_DCU.md`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `70c9a1a6d` - Update README_DCU.md

- Full hash: `70c9a1a6dbc01df5faca6eb7775be75e7c43ca2e`
- Date/author: 2026-04-02 / guobj
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `README_DCU.md`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `865ca25a7` - Update README_DCU.md

- Full hash: `865ca25a7b0b6b5ef7930828bdb57af7b8220ba5`
- Date/author: 2026-04-02 / guobj
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `README_DCU.md`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `8d278721f` - Update README_DCU.md

- Full hash: `8d278721f069861662a3a08d3a723fb6746152d1`
- Date/author: 2026-04-02 / guobj
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `README_DCU.md`
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `4dd71954e` - [bugfix]将使能QWQ-32B性能优化的环境变量SGLANG_USE_FUSED_RMS_ROTARY名称修改为SGLANG_USE_FUSED_SPLIT_QKV_RMS_ROTARY_EMBEDDING，解决因此引起的精度问题

- Full hash: `4dd71954e4540e047696b9b3d0d744e86611e654`
- Date/author: 2026-04-03 / chenyue3
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `50a63c96d` - fix deepseek log cudagraph init meta data copy error in bmz when capture cudagraph.

- Full hash: `50a63c96d8304e6f2ec23819b93680a70a4851ff`
- Date/author: 2026-04-07 / lizhigong
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `b4059342f` - 接入causal_conv1d_update优化算子

- Full hash: `b4059342f9fc93943d4ef95b81ebfb4ffb73c02c`
- Date/author: 2026-04-07 / liucong
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- Risk and verification: Touches scheduling, cache, PD, or MTP paths; verify prefill/decode ordering, first-token correctness, concurrency, and long-context stability.

#### Commit `7104fdb72` - 解决FA报错问题

- Full hash: `7104fdb72e187f1a30ab158c32d7f4d0518afb10`
- Date/author: 2026-04-08 / liucong
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `22e5ac5b1` - Bugfix:fix mm model attention interface

- Full hash: `22e5ac5b196dddddbe227be61aa4cb0e75726a0e`
- Date/author: 2026-04-09 / liuchy5
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/vision.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `c200c7845` - sglang dcu 0.5.11 base hash(dfb35997)

- Full hash: `c200c78458e45487f5b7615d68c0fe4f15fc2b22`
- Date/author: 2026-05-06 / lizhigong
- Branch update: `v0.5.10_dev..v0.5.11_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py` 等 131 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py` 等 17 个文件
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/fla/chunk.py`; `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/attention/fla/fused_recurrent.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - docs-bench: `README_DCU.md`
  - other: `python/pyproject.toml`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py` 等 33 个文件
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `4d897133e` - Supplement merge

- Full hash: `4d897133e08212eaa77243fe8b9f4693bb75e0cf`
- Date/author: 2026-05-07 / lizhigong
- Branch update: `v0.5.10_dev..v0.5.11_dev`
- Auto category: 通用实现调整
- Main files: `python/pyproject.toml`, `python/sglang/srt/model_executor/model_runner.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - other: `python/pyproject.toml`
- Risk and verification: General implementation change; inspect matched files to decide whether it affects target model startup, loading, or serving behavior.

#### Commit `96a5c116a` - fix some error in initial version

- Full hash: `96a5c116a377cdafe911274f1eb87e154879557c`
- Date/author: 2026-05-07 / lizhigong
- Branch update: `v0.5.10_dev..v0.5.11_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`
  - other: `python/sglang/srt/distributed/parallel_state.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `a28aa5f97` - fix some errors when init server

- Full hash: `a28aa5f97c936c20bc4e5d77f0d993c606a1b5f0`
- Date/author: 2026-04-25 / lizhigong
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/qwen2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/qwen2.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/mxfp4.py`
  - other: `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/model_executor/forward_batch_info.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `eec3b3ff8` - fix for load model

- Full hash: `eec3b3ff89bba04cfd7eab0551a85b931b06fa51`
- Date/author: 2026-04-27 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: 无直接文件变更/merge
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: 无直接文件变更/merge
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `6ad2adb52` - [Feature] support rocm moe_fused_gate

- Full hash: `6ad2adb5276fb722d8cdfc1092fcdf40746d945e`
- Date/author: 2026-04-28 / Zhangzbb
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`, `python/sglang/jit_kernel/utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/add_constant.cuh`; `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`; `python/sglang/jit_kernel/utils.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `50b898285` - fix mhc with tile 0.1.9

- Full hash: `50b89828562e31f35fbb3e2a2083256b7dc044b6`
- Date/author: 2026-04-29 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/mhc.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/mhc.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `a44cec29b` - fix jit for moe_fused_gate

- Full hash: `a44cec29bc25886036fa3c237da7c7283beb78ff`
- Date/author: 2026-04-29 / wangaq
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `bb24fa6e1` - [Feature] support rocm moe_fused_gate

- Full hash: `bb24fa6e1c303972bfb5455d15f0a46591110552`
- Date/author: 2026-04-29 / Zhangzbb
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `fd077165a` - fix the mtp issues of metadata loc size

- Full hash: `fd077165adfa5c1f81f6c77e5f290be1cbaea958`
- Date/author: 2026-05-14 / YuanYuan
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/speculative/eagle_worker_v2.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- Risk and verification: Bug-fix commit; validate the trigger condition, accuracy regression, and exceptional path before reusing it.

#### Commit `c5dd815b3` - dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6)

- Full hash: `c5dd815b3c631b45afa6450eb74f16fee6902428`
- Date/author: 2026-05-18 / lizhigong
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 测试/文档/基线合入
- Main files: `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py` 等 141 个文件
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` 等 18 个文件
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`; `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py` 等 85 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - docs-bench: `README_DCU.md`
  - other: `python/pyproject.toml`; `python/sglang/bench_serving.py`; `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/executors/pipeline_executor.py`; `python/sglang/multimodal_gen/runtime/utils/profiler.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py` 等 36 个文件
- Risk and verification: Baseline, merge, test, or docs commit; useful for branch provenance and validation entry points, but usually not direct performance-patch evidence.

#### Commit `411660d35` - feat(diffusion): add ROCm SLA attention backend

- Full hash: `411660d351f37b6a859dad55729a457078892e82`
- Date/author: 2026-05-21 / zhenggf
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/runtime/platforms/rocm.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`
  - other: `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`; `python/sglang/multimodal_gen/runtime/platforms/rocm.py`
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `f378b1a20` - [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0

- Full hash: `f378b1a208dbcd79520abdb38e075ad11d2f09d8`
- Date/author: 2026-05-22 / chenyue3
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/unquant.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/unquant.py`
- Risk and verification: Touches performance or backend paths; validate with prefill/decode traces, end-to-end throughput, and correctness smoke tests before reusing.

#### Commit `18b48e742` - moe-runner-backend支持lightop_moe_w8a8

- Full hash: `18b48e742b700bb2c06586c742a4abd480aaf317`
- Date/author: 2026-05-28 / yangyn1
- Branch update: `v0.5.11_dev..v0.5.12_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/lightop.py`; `python/sglang/srt/layers/moe/moe_runner/runner.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`
- Risk and verification: Touches performance or backend paths; validate with prefill/decode traces, end-to-end throughput, and correctness smoke tests before reusing.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 281 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `docs/internal/dcu-main-conflict-ledger.md` | `5d83cfe85`, `0536e102c`, `523756bde`, `93cf8edc4`, `ff440b897`, `e6d4b3378`, `00063277c`, `88bb5176c`, `a1ed918ae`, `bfaf180d1`, `b6db54a9a`, `1cea713a7`, ... (36 total) |
| `.github/workflows/release-pypi-nightly-hcu.yml` | `358a33714`, `997e64560`, `fb7f11956`, `77939d9a5`, `b0dc28040`, `37c5b30bb`, `8b50a269f`, `d5882c133`, `6ba4328e9`, `5efbf9c3b`, `d39c77a23`, `1db0108f3`, ... (19 total) |
| `.github/workflows/release-pr-hcu.yml` | `358a33714`, `997e64560`, `02968a96d`, `fb7f11956`, `77939d9a5`, `b0dc28040`, `b628d29e1`, `f6b66222a`, `69c73a178`, `3e6aaf09d`, `6a4a61efb`, `d39c77a23`, ... (17 total) |
| `python/sglang/srt/server_args.py` | `cba9e72cc`, `a7931170f`, `6e2576a74`, `832ed3b14`, `18b106418`, `a306b8023`, `f41bb0f58`, `873465654`, `6a51f2a38`, `c40703e6b`, `1679428e0`, `57beb6b4a`, ... (17 total) |
| `.github/workflows/nightly-test-hcu.yml` | `358a33714`, `997e64560`, `02968a96d`, `b0f2bb3a8`, `1a5ce1750`, `fb7f11956`, `b0dc28040`, `6a4a61efb`, `d39c77a23`, `f292fa0e3`, `0ce4bc716`, `647229c6e`, ... (14 total) |
| `.github/workflows/quality-gate.yml` | `811aa027d`, `9864c8451`, `ac56ca009`, `0710e82a0`, `286612da4`, `de696eab9`, `93b801826`, `c8ba30447`, `93c56ce71`, `4d3aaf6af`, `e6c410259`, `f2fc4e166`, ... (14 total) |
| `python/sglang/srt/environ.py` | `45d26d754`, `1653683bd`, `a306b8023`, `261b8627f`, `1679428e0`, `f35668e41`, `a494caa1e`, `0f88700ac`, `7df099eb6`, `7db5ec177`, `c4ef6d3a4`, `90f80c6bd`, ... (14 total) |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `b921d697a`, `038467e8b`, `b57ecddf2`, `dc1b54b42`, `962ab75e4`, `42185e316`, `056b21d82`, `45b20a85c`, `b80d0d1bb`, `6c0330d8d`, `066a95af7`, `cfa865d33`, ... (14 total) |
| `.github/workflows/pr-test-hcu.yml` | `81e3561ae`, `02968a96d`, `dc5cd7089`, `b0dc28040`, `69c73a178`, `63610c2ff`, `0ce4bc716`, `647229c6e`, `74ee9054e`, `7c7da44a7`, `6086af28d`, `a06c34ef7` |
| `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` | `ccfc91c5d`, `18b106418`, `0dd9ab211`, `1653683bd`, `a306b8023`, `873465654`, `ed017ea38`, `5aedbbcc9`, `6e2f11552`, `c3846f222`, `c4ef6d3a4` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `0d55c3dcc`, `c11fc7982`, `3190629e7`, `ef56737fc`, `b921d697a`, `93c930c6f`, `0669c1842`, `b065e598a`, `b10bb8c6e`, `eb4f0ad89`, `6c0330d8d` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `143df0a3e`, `ccfc91c5d`, `75cc77fa2`, `902de5d3d`, `3d12a3ce1`, `51e53affe`, `b001a8d21`, `35d915ef2`, `c4ef6d3a4`, `05c58e82f` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` | `ccbb65acb`, `2083c069f`, `4a6fbed98`, `b36730b41`, `cfa865d33`, `2cc1bcc28`, `966f6da1b`, `018e5799a`, `a031c979a`, `1343bb07e` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `083d1d8b9`, `f475e6569`, `a306b8023`, `f41bb0f58`, `873465654`, `ed017ea38`, `d8db8bb3e`, `6614bebc7`, `b7e4eae12` |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `62a07586d`, `11d08002b`, `72d1d2a73`, `27ce43c71`, `6614bebc7`, `2a1b589b3`, `4a7532fef`, `16e9b3867` |
| `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | `154a88c7b`, `a0cc11498`, `9287931ed`, `39dc297c2`, `c11fc7982`, `1535858ca`, `7164456e7` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `f41bb0f58`, `873465654`, `d8db8bb3e`, `253e326c3`, `8ae13700d`, `6614bebc7`, `7fa7729c1` |
| `python/sglang/srt/disaggregation/prefill.py` | `d8db8bb3e`, `1679428e0`, `8ae13700d`, `6614bebc7`, `20c5f927f`, `0f88700ac`, `7fa7729c1` |
| `python/sglang/srt/layers/moe/topk.py` | `0d243f4f1`, `650a58304`, `b001a8d21`, `dcbfd4230`, `9e3dd4834`, `7df099eb6`, `7db5ec177` |
| `python/sglang/srt/managers/scheduler.py` | `afe5219d0`, `bf037e528`, `8ae13700d`, `77ba00139`, `0f88700ac`, `7fa7729c1`, `40c9ec29b` |
| `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` | `f475e6569`, `a306b8023`, `873465654`, `ed017ea38`, `5aedbbcc9`, `d8db8bb3e`, `2df70449a` |
| `.github/workflows/lint-hcu.yml` | `358a33714`, `997e64560`, `77939d9a5`, `69c73a178`, `3e6aaf09d`, `6086af28d` |
| `python/sglang/srt/disaggregation/decode.py` | `d8db8bb3e`, `1679428e0`, `8ae13700d`, `6614bebc7`, `ab91a15c8`, `77ba00139` |
| `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` | `c0e8edd74`, `b921d697a`, `31a159567`, `31262cd68`, `1882acd8c`, `aebf1a9f4` |
| `.github/workflows/hcu-full-enabled.yml` | `02968a96d`, `132b630bc`, `4c7a264e5`, `b0dc28040`, `6086af28d` |
| `.github/workflows/release-docker-hcu.yml` | `b628d29e1`, `37c5b30bb`, `1db0108f3`, `e769cde2e`, `6086af28d` |
| `docker/hcu.Dockerfile` | `b628d29e1`, `1db0108f3`, `6721affc2`, `e769cde2e`, `6614bebc7` |
| `docs/internal/dcu-main-migration-plan.md` | `5d83cfe85`, `0536e102c`, `e3aa204a0`, `dc1323ba4`, `339dfe433` |
| `python/sglang/srt/disaggregation/common/conn.py` | `f475e6569`, `f41bb0f58`, `873465654`, `6614bebc7`, `20c5f927f` |
| `python/sglang/srt/layers/attention/dsa/hcu_int8_index_k_cache.py` | `a306b8023`, `f41bb0f58`, `873465654`, `d8db8bb3e`, `c3846f222` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `fa6b75971`, `62a07586d`, `11d08002b`, `6614bebc7`, `9153913d6` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `ccbb65acb`, `4a6fbed98`, `1535858ca`, `bfbff7f68`, `0bb71f0c7` |
| `python/sglang/srt/managers/schedule_batch.py` | `3910b3f9d`, `1679428e0`, `20c5f927f`, `0f88700ac`, `7fa7729c1` |
| `python/sglang/srt/mem_cache/unified_radix_cache.py` | `1679428e0`, `bf037e528`, `20c5f927f`, `0f88700ac`, `7fa7729c1` |
| `.github/workflows/hcu-manual-model-test.yml` | `132b630bc`, `4c7a264e5`, `b0dc28040`, `6086af28d` |
| `README_HCU.md` | `50736ebe7`, `0ce4bc716`, `57beb6b4a`, `19175a690` |
| `python/sglang/srt/disaggregation/utils.py` | `f475e6569`, `f41bb0f58`, `d8db8bb3e`, `0f88700ac` |
| `python/sglang/srt/layers/moe/mega_moe.py` | `9fc04a7a2`, `44b7bc846`, `b10bb8c6e`, `eb4f0ad89` |
| `python/sglang/srt/layers/moe/moe_runner/aiter.py` | `8e2aba4bf`, `98ba405a2`, `90f80c6bd`, `bfbff7f68` |
| `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` | `f1c6f5631`, `f106c5360`, `b9e0052e9`, `9f7bfb351` |
| ... | 305 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | `5d83cfe85` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` |
| 2026-06-22 | `0536e102c` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | [SGlang Open] Created an internal main branch from v0.5.12_dev-d4c6831a107a and some docs | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md`, `scripts/code_sync/dcu_main_migration.py` |
| 2026-06-24 | `523756bde` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | [docs(dcu)] log C01/C02 conflict ledger update | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-30 | `93cf8edc4` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-06-30 | `3910b3f9d` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(scheduler): restore DCU empty-prefix location | `python/sglang/srt/managers/schedule_batch.py` |
| 2026-06-30 | `ff440b897` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record C04 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-01 | `e6d4b3378` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-03 | `00063277c` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C07 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-06 | `88bb5176c` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C08 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-06 | `fa6b75971` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] Deliver the remaining _is_dcu branch when flashattention_backend has changed | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_ops/metadata.py` |
| 2026-07-06 | `a1ed918ae` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C09 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `bfaf180d1` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C10 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `b6db54a9a` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C11~C13 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `1cea713a7` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record C14-C16 validation block | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-08 | `b452d6bd6` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record C14-C16 functional validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `01a6f1b94` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C14~C16 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `cee45bc55` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record C17-C19 validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-09 | `4b0fcbd07` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | [Addition] deliver one validation doc of C17~C19 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `cba9e72cc` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] skip some uncompatibal env setup in hip for DCU | `python/sglang/srt/server_args.py` |
| 2026-07-13 | `48489724d` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record 20260623 catch-up runtime status | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `8c797abd6` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Record 20260629 DCU runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-13 | `d8ed552da` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | docs(dcu): add 20260629 conflict review | `docs/internal/dcu-main-catchup-20260629-conflict-review.md` |
| 2026-07-13 | `516a35c40` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record 20260703 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `e3aa204a0` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): require catch-up conflict reviews | `docs/internal/dcu-main-catchup-20260706-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-migration-plan.md` |
| 2026-07-14 | `412d0ef9f` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | docs(dcu): add 20260709 conflict review | `docs/internal/dcu-main-catchup-20260709-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `c0e8edd74` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(dcu): initialize DeepEP dispatch dtype state | `docs/internal/dcu-main-conflict-ledger.md`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-07-14 | `9d7fbb017` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | docs: add 20260710 conflict review | `docs/internal/dcu-main-catchup-20260710-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `24894692e` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix: use runtime attention TP size in model warmup | `python/sglang/srt/model_executor/model_runner.py` |
| 2026-07-14 | `6630db3cf` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs: record 20260710 pure-TP validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `3d77308ea` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs: mark 20260710 catch-up validated | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-14 | `3e335fce8` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs: correct 20260710 endpoint subject | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `baa08af59` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | docs(dcu): add 20260712 conflict review | `docs/internal/dcu-main-catchup-20260712-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `44f81e8f7` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record 20260712 runtime gate status | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `0b30b7c9d` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record 20260712 runtime validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `324181561` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | docs(dcu): add 20260713 conflict review | `docs/internal/dcu-main-catchup-20260713-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `20633db57` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | docs(dcu): add 20260714 conflict review | `docs/internal/dcu-main-catchup-20260714-conflict-review.md`, `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `f67cdf69b` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record 20260714 runtime blocker | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-15 | `49a10aec8` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): record 20260714 owner validation | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-16 | `dc1323ba4` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): finalize v0.5.12_dev forward-port | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md` |
| 2026-07-16 | `339dfe433` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(dcu): define v0.5.15.post1 release workflow | `docs/internal/dcu-main-forward-port-v0.5.12-dev-plan-20260715.md`, `docs/internal/dcu-main-migration-plan.md`, `docs/internal/dcu-v0.5.15-post1-dev-plan.md` |
| 2026-07-20 | `358a33714` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): keep Harbor build image path | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` and 4 files in total |
| 2026-07-20 | `81e3561ae` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci(hcu): exclude two unstable PR tests | `.github/workflows/pr-test-hcu.yml` |
| 2026-07-20 | `811aa027d` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: replace HCU runtime text check with sensitive diff gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-20 | `15a656ea6` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | test(hcu): align v0.5.15 compatibility tests | `test/registered/hcu/openai_server/test_serving_chat_hcu.py`, `test/registered/hcu/unit/test_profile_merger_hcu.py`, `test/registered/unit/server_args/test_server_args.py` |
| 2026-07-21 | `9864c8451` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: use shared sensitive diff gate for HCU port | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-21 | `ac56ca009` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: follow main sensitive diff workflow | `.github/workflows/quality-gate.yml` |
| 2026-07-22 | `9fc04a7a2` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] Disable the standalone-DCU MegaMoE ASM tail-reduce path by default to avoid vmfault | `python/sglang/srt/layers/moe/mega_moe.py` |
| 2026-07-24 | `7482123c3` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-27 | `0710e82a0` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow for new branch version | `.github/workflows/quality-gate.yml` |
| 2026-07-28 | `997e64560` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` and 4 files in total |
| 2026-07-29 | `3b4327cd7` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(hcu): support current LightOp fp8 quant API | `python/sglang/srt/layers/linear.py` |
| 2026-07-29 | `e18e6b94b` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(hcu): record daily forward-port 20260729 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-29 | `111fea82f` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` and 36 files in total |
| 2026-07-31 | `02968a96d` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore shared wheel staging root lost in forward-port | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` and 4 files in total |
| 2026-07-31 | `39d691220` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore NETWORK_MODE default lost in forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-08-03 | `286612da4` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `de696eab9` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `015f6d49a` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: drop redundant module-scope sgl_kernel import in forward_batch_info | `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-08-06 | `f1c6f5631` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(hcu): drop leftover source hunks that renaming and partial takes left behind | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-06 | `8e2aba4bf` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: apply isort/black to forward-port diff | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` and 5 files in total |
| 2026-08-06 | `f17440f19` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore original license headers dropped by the forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh`, `test/run_suite.py` |
| 2026-08-06 | `b0f2bb3a8` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore network_mode matrix keys dropped by the forward-port | `.github/workflows/nightly-test-hcu.yml` |
| 2026-08-07 | `154a88c7b` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: apply isort/black to the lmslim->lightop migration | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-08-07 | `b59995e42` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): point PD smoke tests at a declared HCU suite | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` |
| 2026-08-07 | `92ce544fa` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: align v0.5.15 workflow triggers | `.github/workflows/bot-bump-docs-version.yml`, `.github/workflows/release-docker-amd.yml`, `.github/workflows/release-docker-npu.yml` and 7 files in total |
| 2026-08-07 | `132b630bc` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci(hcu): harden server lifecycle and model mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` and 5 files in total |
| 2026-08-07 | `4c7a264e5` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci(hcu): align model assets and selected-ref kernel | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` |
| 2026-08-07 | `1a5ce1750` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci(hcu): publish reasoning results to shared storage | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_publish_reasoning_code.py`, `scripts/ci/hcu/test_hcu_ci_publish_reasoning_code.py` |
| 2026-08-07 | `50736ebe7` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci(hcu): keep migration changes scoped | `README_HCU.md` |
| 2026-08-07 | `dc5cd7089` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: finalize v0.5.15 workflow policy | `.github/workflows/ci-auto-bisect.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/slash-command-handler.yml` |
| 2026-08-07 | `ecf4756ce` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | test(hcu): isolate server guard unit test | `scripts/ci/hcu/test_hcu_server_guard.py` |
| 2026-08-07 | `76ced479e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | test(hcu): use v0.5.15 FP8 kernel path | `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` |
| 2026-08-07 | `3fbc8ae9e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | test(hcu): align numerical references with v0.5.15 | `test/registered/hcu/kernels/test_attention_reference_hcu.py`, `test/registered/hcu/kernels/test_int8_w8a8_reference_hcu.py` |
| 2026-08-07 | `3de1323a9` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | ci(hcu): normalize rebased PD suite names | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` |
| 2026-08-11 | `ccbb65acb` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [HCU][DSpark] Fix DP EP MoE fallback routing | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-12 | `2083c069f` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: apply pre-commit fixes to the EP MoE fallback change | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-12 | `fb7f11956` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci(hcu): adapt wheel jobs to CIUpload 0.3 | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` and 4 files in total |
| 2026-08-13 | `54e3ed50f` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | [BugFix] fix the runtime errors in ep+dspark mode | `python/sglang/srt/speculative/dspark_components/dspark_draft.py` |
| 2026-08-13 | `18e167b73` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] fix the client inference None errors in temperature>0 with a torch implementation | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-13 | `5e2ba659e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: apply pre-commit fixes to the dspark bugfixes | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-31 | `93b801826` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` |
| 2026-09-21 | `c8ba30447` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `6c1786bc4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-27 | `93c56ce71` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Refactor quality gate workflow and job configurations | `.github/workflows/quality-gate.yml` |
| 2026-07-28 | `77939d9a5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-07-29 | `b2f0b830c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` and 39 files in total |
| 2026-07-31 | `a0cc11498` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] fix the mxfp4 triton accuracy issues | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` |
| 2026-08-03 | `4d3aaf6af` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | Update quality gate workflow for versioning and concurrency | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `e6c410259` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` |
| 2026-08-04 | `083d1d8b9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): restore DeepGEMM PD helper and current cache API | `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-08-04 | `e8298ba90` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): restore DP decode protocol constants | `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-04 | `8160ebe53` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): retain PD decode adapter callbacks | `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-04 | `a7931170f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | sytnx fix | `python/sglang/srt/server_args.py` |
| 2026-08-07 | `6e2576a74` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: route hcu_mla prefill through the chunked prefix cache path | `python/sglang/srt/server_args.py` |
| 2026-08-10 | `e3a9d595c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [HCU][DSpark] Fix sampling parameter updates after graph capture | `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py` |
| 2026-08-10 | `4a6fbed98` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [HCU][DSpark] Add standalone Triton fallback for missing AITER MoE config | `python/sglang/srt/layers/moe/hcu_dspark_aiter_moe_fallback.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-08-10 | `5fd89c728` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [BugFix] fix the inference tensor graph replay issues in MTP mode | `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` |
| 2026-08-10 | `b36730b41` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix lint: apply pre-commit fixes to the mHC EAGLE changes | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/speculative/eagle_worker_common.py` |
| 2026-08-11 | `4a004a87b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: route KDA packed decode to the HCU operator kernel | `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` |
| 2026-08-12 | `7d3e54a20` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support aiter gdn fwd op | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/kda_hcu.py` |
| 2026-08-12 | `9287931ed` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support triton moe wfp4 afp8 tc | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` |
| 2026-08-13 | `39dc297c2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: optimize Triton MXFP4 W4A8 scaling | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` |
| 2026-08-13 | `0d55c3dcc` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: remove debug info | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-13 | `c11fc7982` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: add INT4 MoE W4A8 int8 tensor-core path for slimquant HCU | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-13 | `83ab58f2e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(quant): 修复 HCU W8A8 hipBLASLt 权重布局 | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_w8a8_int8_hcu_layout.py` |
| 2026-08-13 | `832ed3b14` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(moe): 增加 locality-fair static dispatch 策略 | `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/eplb/test_compute_logical_to_rank_dispatch_physical_map.py` |
| 2026-08-13 | `143df0a3e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): 恢复 HCU DSA FlashMLA backend 路由 | `python/sglang/srt/layers/attention/dsa/flashmla_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_flashmla_backend.py` |
| 2026-08-13 | `ccfc91c5d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(attention): 保留 IFB/MTP 的 DSA effective forward mode | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/forward_batch_utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py` and 5 files in total |
| 2026-08-13 | `75cc77fa2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): 修复 IFB/MTP FlashMLA padded rows | `python/sglang/srt/layers/attention/dsa/forward_batch_utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_forward_batch_utils.py` |
| 2026-08-13 | `902de5d3d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): 修复 HCU DSA FlashMLA metadata replay | `python/sglang/srt/layers/attention/dsa/flashmla_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_flashmla_backend.py` |
| 2026-08-13 | `18b106418` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | feat(attention): 恢复 HCU LightOp DSA indexer 路径 | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/paged_mqa_logits_backend.py`, `python/sglang/srt/server_args.py` and 4 files in total |
| 2026-08-13 | `0dd9ab211` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(attention): 按 head_dim 归一化 DSA indexer | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `test/registered/unit/layers/attention/dsa/test_hcu_indexer.py` |
| 2026-08-13 | `43f1a8b2a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): 启用 HCU DSA MTP draft-extend CUDA graph | `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/spec/test_eagle_worker_v2_graph_support.py` |
| 2026-08-14 | `fa309a1e1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-08-14 | `288ab2445` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: fix submit_nogds_read failed when use fastsafetensors load | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-08-14 | `1535858ca` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: refactor mxfp4 moe for activate 8 or 16 bit | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` and 4 files in total |
| 2026-08-15 | `3190629e7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: correct blockshape is none when use aiter moe for channel w4a8 model | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-17 | `9bbf3799d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | docs(hcu): add the 20260817 official backport validation report | `docs/internal/backport-official-20260817-validation-report.md` |
| 2026-08-18 | `b0dc28040` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Hcu/fix main kernel build path (#207) | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` and 9 files in total |
| 2026-08-18 | `e3a192d66` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: update kda default value and support boltops chunk delta rule | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py` and 4 files in total |
| 2026-08-19 | `ef56737fc` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: update w4a8 moe default backend | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-19 | `45d26d754` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(kernel): add HCU MLA query concat kernel | `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/concat_mla_absorb_q_hcu.cu` and 7 files in total |
| 2026-08-19 | `1653683bd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): port sparse page MQA with mask TopK to DSA | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_metadata.py` and 5 files in total |
| 2026-08-19 | `f475e6569` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(dsa): compact shared index-K cache | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/utils.py` and 8 files in total |
| 2026-08-19 | `a306b8023` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(hcu): port gfx936 INT8 DSA index cache | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/hcu_int8_index_k_cache.py` and 7 files in total |
| 2026-08-19 | `f41bb0f58` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(hcu): support INT8 DSA cache in Mooncake PD | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/utils.py` and 8 files in total |
| 2026-08-19 | `3d12a3ce1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): stabilize DSA MTP metadata replay | `python/sglang/kernels/jit/csrc/elementwise/fused_metadata_copy.cuh`, `python/sglang/kernels/ops/attention/fused_metadata_copy.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py` and 4 files in total |
| 2026-08-19 | `51e53affe` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): reuse DSA target verify graph metadata | `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py` |
| 2026-08-19 | `873465654` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): correct compact index cache handling | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` and 10 files in total |
| 2026-08-19 | `6a51f2a38` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): register SlimQuant W4A8 Marlin quantization | `python/sglang/srt/server_args.py` |
| 2026-08-19 | `afe5219d0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(scheduler): use parallel state for PD decode sync | `python/sglang/srt/managers/scheduler.py` |
| 2026-08-19 | `0d243f4f1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): restore async metadata copies and padded dispatch | `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/moe/test_topk_padded_region.py` |
| 2026-08-19 | `ed017ea38` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): use LayerSplit scratch for fused index writes | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/index_key_cache.py` and 4 files in total |
| 2026-08-20 | `62a07586d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat] 适配HCU FA3 | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` and 5 files in total |
| 2026-08-20 | `fb7369fec` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix]删除无关文件 | `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942` |
| 2026-08-20 | `b628d29e1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | [feature] 增加打镜像的ci, 0.5.15版本更新torch到2.11版本 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-20 | `11d08002b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` and 4 files in total |
| 2026-08-20 | `f6b66222a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | revert: 恢复 release-pr-hcu.yml 默认 torch 版本为 2.10.0 | `.github/workflows/release-pr-hcu.yml` |
| 2026-08-20 | `72d1d2a73` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix]solved other CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `27ce43c71` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `37c5b30bb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: extract full DTK version for three-part versions | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` and 4 files in total |
| 2026-08-20 | `a6a8e0d5d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: read MXFP4 group_size from model config instead of hardcoding 32 | `python/sglang/srt/layers/quantization/mxfp4.py` |
| 2026-08-20 | `650a58304` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): skip padded tokens for legacy DeepGEMM MoE | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-20 | `b001a8d21` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): reduce TopK and DSA replay overhead | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` |
| 2026-08-20 | `dcbfd4230` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): avoid redundant padded weight mask | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-20 | `9e3dd4834` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): fuse DeepEP topk id cast | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-20 | `5aedbbcc9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): overlap LayerSplit index cache broadcast | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` and 5 files in total |
| 2026-08-24 | `261b8627f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): restore 29 environ declarations the sync auto-merge dropped | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py` |
| 2026-08-24 | `238c81b4c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 优化因数据拷贝导致的性能问题 | `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py`, `python/sglang/srt/hardware_backend/npu/moe/matmul.py` |
| 2026-08-24 | `6e2f11552` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): align speculative index cache lengths | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` |
| 2026-08-25 | `c40703e6b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(ci): clear the three Quality Gate blockers from the 20260824 sync | `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml` and 5 files in total |
| 2026-08-25 | `59213c7e4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED | `scripts/ci/hcu/hcu_rename_allowlist.txt` |
| 2026-08-25 | `69c73a178` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | ci(hcu): support fork pull requests | `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `f2fc4e166` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` |
| 2026-08-25 | `3e6aaf09d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): allow fork checkout in target workflows | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `6a4a61efb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | ci(hcu): detect runner workspace ownership | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `b921d697a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support contiguous and masked hipc kernel for deepep normal and low_latency mode | `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` and 4 files in total |
| 2026-08-25 | `7164456e7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: preserve target lightop int8 quantization | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` |
| 2026-08-26 | `8b50a269f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | bugfix router路径不对 | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `d5882c133` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | [feature] 发包流水支持手动触发,手动触发不上传pypi | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `038467e8b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix lightop moe align vimfault | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-26 | `6ba4328e9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): release 发包流水触发方式改为 push | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `93c930c6f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix aiter shuffle func not found | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-26 | `d8db8bb3e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): complete LayerSplit HiCache paths | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` and 11 files in total |
| 2026-08-26 | `5efbf9c3b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | debug: gateway 构建加日志排查 wheel 路径，临时只编 router | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `0669c1842` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(quantization): defer SlimQuant MoE backend resolution | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-26 | `63610c2ff` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): enable checks for release branches | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/quality-gate.yml` |
| 2026-08-26 | `d39c77a23` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): use bash for wheel build jobs | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `1db0108f3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [CI bugfix]工作目录没有清理导致权限变root (#240) | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-26 | `b57ecddf2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): fix W4A8 DeepEP accuracy with SwiGLU clamp | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `f292fa0e3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): trust wheel build workspaces | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-27 | `779f1bea2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix] CI打包版本更新为0.5.18 (#244) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-27 | `1679428e0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [FEAT][DSpark] 1. Support the p/d radix cache w/ DSpark by PR:https://github.com/sgl-project/sglang/pull/31097; 2. SGLANG_ENABLE_UNIFIED_RADIX_TREE=1 & SGLANG_ENABLE_UNIFIED_RADIX_TREE=1 & --disaggregation-decode-enable-radix-cache should be enable in D | `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` and 14 files in total |
| 2026-08-27 | `6721affc2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | [feature]适配hcu发包 | `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml` |
| 2026-08-27 | `dc1b54b42` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): tolerate deepgemm without contiguous HIPC kernel | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `b065e598a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): restore slimquant backend logger | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-27 | `962ab75e4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): default to compatible masked W4A8 kernel | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `253e326c3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(disagg): avoid duplicate KV transfer in worker | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-08-27 | `42185e316` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): apply SwiGLU clamp in contiguous W4A8 path | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `e769cde2e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | hcu ci: docker 镜像 daily 定时构建, router 改用 vendored openssl, 补装 flash_kda (#252) | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` and 4 files in total |
| 2026-08-28 | `5f314b004` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dspark): transfer draft KV from PD prefill | `python/sglang/srt/speculative/dspark_components/dspark_disaggregation.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py` |
| 2026-08-28 | `31a159567` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: use the model's MoE topk for DeepEP RDMA buffer sizing | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-08-28 | `845f99085` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(spec): handle zero-token verify results | `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py` |
| 2026-08-28 | `c3846f222` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): consume INT8 DSA index cache directly | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/hcu_int8_index_k_cache.py` |
| 2026-08-29 | `bf037e528` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hicache): synchronize L3 prefetch across PP ranks | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hicache_storage.py` and 11 files in total |
| 2026-08-31 | `bf9245607` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` |
| 2026-09-01 | `685051c47` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix] removed the http warning info in the skip-warmup mode (#276) | `python/sglang/srt/entrypoints/http_server.py` |
| 2026-09-01 | `867eeada1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: gracefully handle unsupported KV cache schemes (#268) | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-09-01 | `8ae13700d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): port PD disaggregation accuracy fix to v0.5.18 release (#266) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` and 5 files in total |
| 2026-09-02 | `6614bebc7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): add BHSD KV-cache support while preserving legacy HCU FA (#282) | `docker/hcu.Dockerfile`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` and 11 files in total |
| 2026-09-02 | `4fea017b1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): sample linear MTP target verification (#280) | `python/sglang/srt/speculative/eagle_utils.py` |
| 2026-09-02 | `0e2a6e743` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Feat/bolt recompute w u (#278) | `python/sglang/kernels/ops/attention/fla/wy_fast.py` |
| 2026-09-02 | `556337109` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]:用lightop的gemm_w8a8_smooth代替triton实现，提升性能 (#279) | `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py` and 4 files in total |
| 2026-09-02 | `0ce4bc716` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [CI] Use v0.5.18 HCU image and update model paths (#287) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `README_HCU.md` and 12 files in total |
| 2026-09-02 | `3b678f293` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BUGFIX] HCU环境不需要依赖flashinfer (#289) | `python/pyproject_hcu.toml` |
| 2026-09-03 | `ab91a15c8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix] 1.fix the accuracy issue in Decode radix-cache enable due to… (#291) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/mem_cache/common.py` |
| 2026-09-03 | `2a1b589b3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): support BSHD multi-batch varlen attention and PD disaggregation (#288) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` |
| 2026-09-03 | `b0f501598` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] fix the bug that certain chat/completion in DSpark goes to C… (#294) | `python/sglang/kernels/ops/speculative/dspark/dspark_accept.py` |
| 2026-09-03 | `f656a2ed2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] fix the bug by removing old monkey patch of mhc (#296) | `python/sglang/kernels/ops/layernorm/mhc.py` |
| 2026-09-03 | `2b855b5be` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | ci(hcu): align llguidance and model asset paths (#300) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` |
| 2026-09-03 | `20c5f927f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [BugFix] Remove the dependency of prefill radix-cache with decode-pre… (#302) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py` and 5 files in total |
| 2026-09-04 | `9153913d6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(speculative): remove unsupported server args (#304) | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-09-04 | `f35668e41` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [perf] add opt-in LightOp KV allocation kernel (#307) | `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/allocator/paged.py` |
| 2026-09-04 | `4c9d666cd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: fix deepep and dspark conflict (#306) | `python/sglang/srt/arg_groups/speculative_hook.py` |
| 2026-09-04 | `44b7bc846` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] support the MegaMoE func in DSpark model (#309) | `python/sglang/srt/layers/moe/mega_moe.py` |
| 2026-09-07 | `3bc09034b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | feat(bench): add --gsp-input-ids to skip server tokenization (#315) | `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` |
| 2026-09-07 | `cdea7a5db` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): use available RMSNorm kernel op (#321) | `python/sglang/srt/layers/layernorm.py` |
| 2026-09-07 | `ba2dec637` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(fst): reclaim device cache after each weight batch (#322) | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-09-08 | `056b21d82` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | opt: optimize situ_quant op form lightop lib (#324) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-08 | `47b97c0f7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): avoid gfx936 QSA LDS overflow (#326) | `python/sglang/srt/layers/attention/qsa/sparse_attn.py` |
| 2026-09-08 | `57beb6b4a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | ci(hcu): align PR wheel version with release 0.5.18 (#295) | `.github/workflows/release-pr-hcu.yml`, `README_HCU.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py` and 9 files in total |
| 2026-09-09 | `e6540308c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix bug: Refactor is_fp8_fnuz function for clarity | `python/sglang/kernels/ops/quantization/fp8_kernel.py` |
| 2026-09-09 | `b10bb8c6e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [FEAT] support the dspark megamoe-int4 by packing signed-int4 to int8 (#333) | `python/sglang/srt/layers/moe/hcu_int4_megamoe.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py` and 5 files in total |
| 2026-09-10 | `6d5931922` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | test(hcu): derive FP8 quant reference bounds from the output dtype (#337) | `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` |
| 2026-09-10 | `ebe9c77f2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | [FEATURE]同步编译python3.10和python3.12, 上传whl包后记录信息至dashub (#338) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-10 | `a494caa1e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): use AITER IPC collectives for DP TP-MoE (#340) | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/dp_attention.py` |
| 2026-09-10 | `4cdd9d36e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Release/20260825 v0.5.18 (#339) | `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py` |
| 2026-09-11 | `77ba00139` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: fix pd fake prefill mode and attn_tp_size bug (#345) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-09-12 | `fa95ae084` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix and opt: fix dspark eagle error and optimize attn tp comm from ai… (#342) | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py` |
| 2026-09-12 | `647229c6e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): pin v0.5.18 image fallback and shared eval wheels (#348) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` |
| 2026-09-14 | `4a7532fef` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): keep DFLASH FP8 sliding attention on native FlashAttention (#356) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_native_swa.py`, `test/manual/test_hcu_native_swa.py` |
| 2026-09-14 | `74ee9054e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | ci(hcu): fix v0.5.18 PR runtime consistency (#363) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/sampling/test_pytorch_sampling_backend.py` |
| 2026-09-14 | `5077850b7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | support fabric aiter custom allreduce (#361) | `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py` and 5 files in total |
| 2026-09-14 | `72df69c80` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [BUGFIX]缺少token声明导致打包信息无法推送至Dashub (#366) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-15 | `86cdce034` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): align v0.5.18 wheel builds with torch 2.11 (#368) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-09-15 | `45b20a85c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Fix ValueError: Add type annotations to fuse_situ_mul_quant_ep (#369) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-15 | `7c7da44a7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | ci(hcu): fix stale v0.5.18 PR test paths (#370) | `.github/workflows/pr-test-hcu.yml` |
| 2026-09-15 | `35d915ef2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | feat: support hy4 cp (#358) | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/hunyuan_v4.py` |
| 2026-09-15 | `0f88700ac` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | feat(mem-cache): support direct L3 external linker cache without test file (#373) | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py` and 31 files in total |
| 2026-09-16 | `b80d0d1bb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix] 修复w8a8-fp8-v4pro精度问题 (#380) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-16 | `7df099eb6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(moe): 增加 EP 绝对均衡性能测试开关 (#383) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_balance.py`, `python/sglang/srt/layers/moe/hash_topk.py` and 4 files in total |
| 2026-09-16 | `2bb5e81e5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | feat(spec): 支持节点内 Draft LM-head 词表并行 (#385) | `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/forward_batch_info.py` and 6 files in total |
| 2026-09-17 | `07214443b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(qsa): use FA sparse GQA for HIP chunk-prefill extend (#392) | `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` |
| 2026-09-17 | `2df70449a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(layersplit): 支持单层 MTP Draft KV 分片与缓存复用 (#387) | `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` and 10 files in total |
| 2026-09-17 | `7db5ec177` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(lplb): 支持 HIP 静态 LP 副本概率分发 (#386) | `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `python/sglang/kernels/jit/csrc/lplb/dispatch_probability.cuh` and 10 files in total |
| 2026-09-17 | `c4ef6d3a4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): 修复 MQA 显存预算与 CP/MTP 索引补齐 (#382) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py` |
| 2026-09-17 | `eb4f0ad89` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]适配 w4a8-int8-megamoe (#394) | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-09-20 | `16e9b3867` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): support BF16 KV for Qwen DFLASH2 attention (#405) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/manual/test_hcu_dflash_native_block16.py` |
| 2026-09-20 | `ccc15a6f3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(cache): integrate Mooncake ReadPlan and optimize page-wise loading for direct linker (#404) | `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` and 6 files in total |
| 2026-09-20 | `98ba405a2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(aiter): w13 权重 shuffle 改回 gemm2 布局，修复 w8a8 变体乱码 (#401) | `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-09-20 | `05c58e82f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): 修复 gfx938 72CU sparse MQA 路由与 HCU 判断 (#409) | `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/attention/dsa_backend.py` |
| 2026-09-22 | `50beda6a9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-09-23 | `31262cd68` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix deepep num_rdma_bytes count correct (#437) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-09-23 | `90f80c6bd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(moe): 增加 aiter moe_c 后端选定环境变量 (#415) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-09-23 | `6c0330d8d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(w4a8): 修复 HIPC MoE scale 重复乘 16 与 HCU RoPE 启动越界 (#439) | `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` and 4 files in total |
| 2026-09-23 | `2f93be6c5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(kvcache): handle zero full iterations for asymmetric KV cache (#425) | `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh` |
| 2026-09-23 | `066a95af7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix lightop situ import regression bug and deepgemm w4a8 op interface change (#428) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-30 | `6086af28d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | ci(hcu): migrate v0.5.18 workflows to organization runners (#465) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` and 11 files in total |
| 2026-09-30 | `1828115e0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix w4a16 moe asm error (#462) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` |
| 2026-09-30 | `3854f7754` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | opt(kda): update kda verify decode op from boltops (#458) | `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` |
| 2026-09-30 | `e885e7223` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): restore ForwardBatch RMS quantization flag (#469) | `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_forward_batch_hcu_state.py` |
| 2026-10-08 | `cfa865d33` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix deepgemm masked fp8 api upstream (#472) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-10-08 | `b7e4eae12` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: remove alt_stream overlap copy when writing KV cache (#478) | `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-10-08 | `7fa7729c1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(cache): harden Mooncake ReadPlan and PP direct-L3 cache loading (#482) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py` and 27 files in total |
| 2026-10-09 | `2cc1bcc28` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(deepgemm): 统一 INT8/FP8 权重重排与 FP8 masked GEMM 接口 (#484) | `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` and 6 files in total |
| 2026-10-09 | `a06c34ef7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(ci): stage-b include 列表容忍分支差异的测试文件 (#485) | `.github/workflows/pr-test-hcu.yml` |
| 2026-10-09 | `6ca7a1bd6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(test): 修复 unified attention 单测 KV 索引构造 (#489) | `test/registered/attention/test_triton_attention_kernels.py` |
| 2026-10-09 | `1882acd8c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): restore DeepEP normal combine for HCU groupgemm (#491) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-10-09 | `bfbff7f68` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): preserve INT8 MoE fallback and restore AITER W8A8 compatibility (#487) | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` and 7 files in total |
| 2026-10-10 | `966f6da1b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): avoid double packing channel FP8 DeepGEMM weights (#497) | `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-10-10 | `e1eaf0829` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): guard SBO setup for flat DeepEP dispatch (#501) | `python/sglang/srt/batch_overlap/single_batch_overlap.py` |
| 2026-10-10 | `f106c5360` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): 优化小 batch W8A8 INT8 GEMM 的 Tiling 选择 (#502) | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` |
| 2026-10-12 | `49bb75c79` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(diffusion): upload all video outputs to cloud storage | `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py` |
| 2026-10-12 | `aebf1a9f4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): fix SlimQuant INT8 DeepEP routing and DeepGEMM weight packing (#514) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-10-13 | `018e5799a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Fix/hcu aiter moe inplace (#517) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/models/qwen2_moe.py` |
| 2026-10-13 | `71b2ee4ea` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf: add opt-in asynchronous prebuilt token H2D (#516) | `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/environ.py` and 4 files in total |
| 2026-10-13 | `9dd4e2e80` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [diffusion] attention: fix HCU Wan SLA and FA family admission (#519) | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py` and 7 files in total |
| 2026-10-14 | `40c9ec29b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(scheduler): keep DP health probes on the generation path (#528) | `python/sglang/srt/managers/scheduler.py` |
| 2026-10-15 | `c2666f4b5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [fix] 修复cp 逻辑：解决实际 token 不被整除时不走 cp 的问题 (#538) | `python/sglang/srt/layers/attention/dsa/utils.py` |
| 2026-10-16 | `6fe59ce1a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci: release-pypi-nightly-hcu 多版本编译 (dtk26.04/py3.10+3.12, dtk26.10/py3.12) [rel/20260825_v0.5.18] (#544) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-10-16 | `0bb71f0c7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix] 解决 w4a8 aiter moe 不支持 swiglu_limit 功能 (#550) | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-10-19 | `b9e0052e9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): keep the w8a8 smooth asm fast path off on gfx928 (#555) | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` |
| 2026-10-20 | `a031c979a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix] 修复非 AITER 路径下 compressed-tensors W8A8 FP8 MoE 权重被错误补齐导致输出乱码 (#564) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-10-20 | `030f6254f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(attention): add paged split-KV support and opt-in DSpark V2 (#553) | `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/kernels/ops/attention/test_verify_mla_layout.py` |
| 2026-10-20 | `19175a690` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | [Feat] build: Add build wheel scripts (#569) | `README_HCU.md`, `scripts/build_hcu_wheels.sh` |
| 2026-10-21 | `9f7bfb351` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): skip the w8a8 smooth asm fast path when M=0 (#573) | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` |
| 2026-10-22 | `464bebd64` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [Fix][v0.5.18] Backport reasoning token accounting fix from upstream #41460 (#579) | `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py` |
| 2026-10-26 | `cbaf42c07` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Fix auxiliary HiCache load-back pending collisions (#591) | `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py` |
| 2026-10-28 | `1343bb07e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Fix] deepgemm: 修复 w8a8-fp8 旧版重排逻辑 (#608) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-11-03 | `448c57ad4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix] 修复 w8a8_int8 量化时视觉层 qkv_proj 未命中忽略名单导致被错误量化 (#632) | `python/sglang/srt/layers/quantization/w8a8_int8.py` |
| 2026-11-03 | `c760e11b4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix w4a8 int4 deepgemm hipc kernel interface mismatch (#638) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |

### Per-Commit Audit Cards

- The timeline lists all 281 commits; audit cards cover only the most recent 80.

#### Commit `9153913d6` - fix(speculative): remove unsupported server args (#304)

- Full hash: `9153913d619d31597b77c205453eadb5d2f355f1`
- Date/author: 2026-09-04 / Wenbo Zhu
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f35668e41` - [perf] add opt-in LightOp KV allocation kernel (#307)

- Full hash: `f35668e41c964583e7b0e0761f311c2893d31b9d`
- Date/author: 2026-09-04 / JingLee
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/allocator/paged.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/mem_cache/allocator/paged.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `4c9d666cd` - fix: fix deepep and dspark conflict (#306)

- Full hash: `4c9d666cd36e3aafa5c584f7ff0188877460bb1d`
- Date/author: 2026-09-04 / daishiqiang123
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/arg_groups/speculative_hook.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/arg_groups/speculative_hook.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `44b7bc846` - [BugFix] support the MegaMoE func in DSpark model (#309)

- Full hash: `44b7bc84619f5a87c239a586ef7fe10cdab0abf4`
- Date/author: 2026-09-04 / YuanYuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/mega_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `3bc09034b` - feat(bench): add --gsp-input-ids to skip server tokenization (#315)

- Full hash: `3bc09034bad8c7679d3eaaa3772669c6126ebcc5`
- Date/author: 2026-09-07 / chaoyujiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `cdea7a5db` - fix(hcu): use available RMSNorm kernel op (#321)

- Full hash: `cdea7a5dbb96b24f80d6330e53c06000ace56e65`
- Date/author: 2026-09-07 / Wenbo Zhu
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/layernorm.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/layernorm.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `ba2dec637` - fix(fst): reclaim device cache after each weight batch (#322)

- Full hash: `ba2dec637cc60db20a61f27f5ea04daa61db8e51`
- Date/author: 2026-09-07 / lzb16
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/model_loader/weight_utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/model_loader/weight_utils.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `056b21d82` - opt: optimize situ_quant op form lightop lib (#324)

- Full hash: `056b21d829f1408d184fc411e1155c7be9d5fa10`
- Date/author: 2026-09-08 / daishiqiang123
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `47b97c0f7` - fix(hcu): avoid gfx936 QSA LDS overflow (#326)

- Full hash: `47b97c0f77e08a5b2287a5f6d0330dec5ccab090`
- Date/author: 2026-09-08 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `57beb6b4a` - ci(hcu): align PR wheel version with release 0.5.18 (#295)

- Full hash: `57beb6b4ae453725e0c02b58bb5b3d93d737aa4a`
- Date/author: 2026-09-08 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/release-pr-hcu.yml`, `README_HCU.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/server_args.py`, `requirements_hcu.txt`, `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` 等 9 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pr-hcu.yml`
  - other: `README_HCU.md`; `python/sglang/srt/arg_groups/overrides.py`; `requirements_hcu.txt`; `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/hcu_ci_start_container.sh`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/kernels/ops/quantization/fp8_kernel.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `e6540308c` - fix bug: Refactor is_fp8_fnuz function for clarity

- Full hash: `e6540308c53b7099feb893050d56c1793a3962f1`
- Date/author: 2026-09-09 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/quantization/fp8_kernel.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/quantization/fp8_kernel.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b10bb8c6e` - [FEAT] support the dspark megamoe-int4 by packing signed-int4 to int8 (#333)

- Full hash: `b10bb8c6eb52cceb55647620d7e0e9e4e711dc3d`
- Date/author: 2026-09-09 / YuanYuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/hcu_int4_megamoe.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/mem_cache/common.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/hcu_int4_megamoe.py`; `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`; `python/sglang/srt/mem_cache/common.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `6d5931922` - test(hcu): derive FP8 quant reference bounds from the output dtype (#337)

- Full hash: `6d59319229dbc44db4ed7a13a1af8ffda67d14f2`
- Date/author: 2026-09-10 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `ebe9c77f2` - [FEATURE]同步编译python3.10和python3.12, 上传whl包后记录信息至dashub (#338)

- Full hash: `ebe9c77f2189d2e0982deb37a88a1f323dda191c`
- Date/author: 2026-09-10 / Crowder13
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 通用实现调整
- Main files: `.github/workflows/release-pypi-nightly-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `a494caa1e` - perf(hcu): use AITER IPC collectives for DP TP-MoE (#340)

- Full hash: `a494caa1e7974a8ec960c526838f476fd93312c8`
- Date/author: 2026-09-10 / Yongqiang Duan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/dp_attention.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/dp_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `4cdd9d36e` - Release/20260825 v0.5.18 (#339)

- Full hash: `4cdd9d36e79a61e736bc6712916a23617919fbfa`
- Date/author: 2026-09-10 / wufan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `77ba00139` - fix: fix pd fake prefill mode and attn_tp_size bug (#345)

- Full hash: `77ba00139ac13b8a6bdb9ee15554cd9c18537fbc`
- Date/author: 2026-09-11 / daishiqiang123
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `fa95ae084` - fix and opt: fix dspark eagle error and optimize attn tp comm from ai… (#342)

- Full hash: `fa95ae0846a943f9a740c56a3dee4d42279d4728`
- Date/author: 2026-09-12 / daishiqiang123
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/dp_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `647229c6e` - ci(hcu): pin v0.5.18 image fallback and shared eval wheels (#348)

- Full hash: `647229c6e5adaf3f2dda3515671a48c45f58f825`
- Date/author: 2026-09-12 / dingxinlong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `4a7532fef` - fix(hcu): keep DFLASH FP8 sliding attention on native FlashAttention (#356)

- Full hash: `4a7532fefd86c6a5f0089a3b6b40eeb1f3ed2119`
- Date/author: 2026-09-14 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_native_swa.py`, `test/manual/test_hcu_native_swa.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/hcu_native_swa.py`
  - tests: `test/manual/test_hcu_native_swa.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `74ee9054e` - ci(hcu): fix v0.5.18 PR runtime consistency (#363)

- Full hash: `74ee9054e84ccb9c33007e5726a93d16b248ea37`
- Date/author: 2026-09-14 / dingxinlong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/sampling/test_pytorch_sampling_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
  - tests: `test/registered/sampling/test_pytorch_sampling_backend.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `5077850b7` - support fabric aiter custom allreduce (#361)

- Full hash: `5077850b7b646483abe7bd2856ff79d5062ff335`
- Date/author: 2026-09-14 / jiafei96
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/hcu_cookbook_utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/bootstrap.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `72df69c80` - [BUGFIX]缺少token声明导致打包信息无法推送至Dashub (#366)

- Full hash: `72df69c8087c51d4ed237c219836a1d0df4d274e`
- Date/author: 2026-09-14 / Crowder13
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `.github/workflows/release-pypi-nightly-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `86cdce034` - ci(hcu): align v0.5.18 wheel builds with torch 2.11 (#368)

- Full hash: `86cdce034cbf09a90b7a2a3328174d09634a660e`
- Date/author: 2026-09-15 / dingxinlong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `45b20a85c` - Fix ValueError: Add type annotations to fuse_situ_mul_quant_ep (#369)

- Full hash: `45b20a85cb28b0f3cbdb71c3d5ca233c8cb63901`
- Date/author: 2026-09-15 / Wenbo Zhu
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `7c7da44a7` - ci(hcu): fix stale v0.5.18 PR test paths (#370)

- Full hash: `7c7da44a797df5bb370a1789ab7f0aeef55b5530`
- Date/author: 2026-09-15 / dingxinlong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `35d915ef2` - feat: support hy4 cp (#358)

- Full hash: `35d915ef222de3b2839bb55c1afa9c99e3a24941`
- Date/author: 2026-09-15 / Fafap131
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/hunyuan_v4.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/hunyuan_v4.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `0f88700ac` - feat(mem-cache): support direct L3 external linker cache without test file (#373)

- Full hash: `0f88700ac87668fe19d35f214773ea827a049a8c`
- Date/author: 2026-09-15 / xinleishang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` 等 31 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-model: `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/base_spec_worker.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hicache_storage.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`; `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`; `python/sglang/srt/mem_cache/kv_cache_builder.py`; `python/sglang/srt/mem_cache/kv_cache_configurator.py`; `python/sglang/srt/mem_cache/registry.py` 等 23 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b80d0d1bb` - [fix] 修复w8a8-fp8-v4pro精度问题 (#380)

- Full hash: `b80d0d1bb6a942853b242ecc38ef3be3db2575d2`
- Date/author: 2026-09-16 / yangyn
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `7df099eb6` - feat(moe): 增加 EP 绝对均衡性能测试开关 (#383)

- Full hash: `7df099eb6085eddb781531719bc2af24ff3cf204`
- Date/author: 2026-09-16 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_balance.py`, `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_balance.py`; `python/sglang/srt/layers/moe/hash_topk.py`; `python/sglang/srt/layers/moe/topk.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2bb5e81e5` - feat(spec): 支持节点内 Draft LM-head 词表并行 (#385)

- Full hash: `2bb5e81e5353c5bc40594d42bd80366b91af15bb`
- Date/author: 2026-09-16 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/draft_lm_head_vp.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/speculative/draft_lm_head_vp.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `07214443b` - feat(qsa): use FA sparse GQA for HIP chunk-prefill extend (#392)

- Full hash: `07214443be3c398eab3f874df214cbadf256ae03`
- Date/author: 2026-09-17 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2df70449a` - feat(layersplit): 支持单层 MTP Draft KV 分片与缓存复用 (#387)

- Full hash: `2df70449a7a99196cb2a9497c5f59e57dd556aca`
- Date/author: 2026-09-17 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/pool_host/dsa.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/models/deepseek_nextn.py` 等 10 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/cp/utils.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/speculative/base_spec_worker.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`; `python/sglang/srt/mem_cache/kv_cache_configurator.py`; `python/sglang/srt/mem_cache/pool_host/dsa.py`; `python/sglang/srt/mem_cache/pool_host/mla.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `7db5ec177` - feat(lplb): 支持 HIP 静态 LP 副本概率分发 (#386)

- Full hash: `7db5ec1771b90e54071f21394cb3df502af98880`
- Date/author: 2026-09-17 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `python/sglang/kernels/jit/csrc/lplb/dispatch_probability.cuh`, `python/sglang/kernels/jit/csrc/lplb/platform.cuh`, `python/sglang/kernels/ops/lplb/cuda_solver.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/lplb_solver.py` 等 10 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - docs-bench: `benchmark/eplb/README.md`; `benchmark/eplb/prepare_static_lp.py`
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/expert_location.py`; `python/sglang/srt/eplb/lplb_solver.py`
  - runtime-perf: `python/sglang/kernels/jit/csrc/lplb/dispatch_probability.cuh`; `python/sglang/kernels/jit/csrc/lplb/platform.cuh`; `python/sglang/kernels/ops/lplb/cuda_solver.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/model_executor/model_runner_components/moe_ep_setup.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `c4ef6d3a4` - fix(dsa): 修复 MQA 显存预算与 CP/MTP 索引补齐 (#382)

- Full hash: `c4ef6d3a48dfc0f79bf13871f3c4b028199a7c95`
- Date/author: 2026-09-17 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`; `python/sglang/srt/layers/attention/dsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `eb4f0ad89` - [feat]适配 w4a8-int8-megamoe (#394)

- Full hash: `eb4f0ad89390fc039a5943f241a5a7421bad2a1c`
- Date/author: 2026-09-17 / yangyn
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `16e9b3867` - feat(hcu): support BF16 KV for Qwen DFLASH2 attention (#405)

- Full hash: `16e9b386740e30e4879c696db587db58a2eeeabf`
- Date/author: 2026-09-20 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/manual/test_hcu_dflash_native_block16.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
  - tests: `test/manual/test_hcu_dflash_native_block16.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `ccc15a6f3` - feat(cache): integrate Mooncake ReadPlan and optimize page-wise loading for direct linker (#404)

- Full hash: `ccc15a6f3ff01d34f7b40441cbb7d29246e39003`
- Date/author: 2026-09-20 / leichuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_mooncake_direct_linker_read_plan.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`; `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`
  - tests: `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`; `test/registered/unit/mem_cache/test_mooncake_direct_linker_read_plan.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `98ba405a2` - fix(aiter): w13 权重 shuffle 改回 gemm2 布局，修复 w8a8 变体乱码 (#401)

- Full hash: `98ba405a238305be3bd2a483216aa5fb0bb2d47b`
- Date/author: 2026-09-20 / Wenbo Zhu
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `05c58e82f` - fix(dsa): 修复 gfx938 72CU sparse MQA 路由与 HCU 判断 (#409)

- Full hash: `05c58e82faab83b6bf906cfd70f2845eaee1df6c`
- Date/author: 2026-09-20 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/attention/dsa_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`; `python/sglang/srt/layers/attention/dsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `50beda6a9` - Update quality gate workflow to use stable version

- Full hash: `50beda6a90ba4dd7c85d667530c2614b13122fbf`
- Date/author: 2026-09-22 / Lvjiajia
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/quality-gate.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/quality-gate.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `31262cd68` - fix: fix deepep num_rdma_bytes count correct (#437)

- Full hash: `31262cd68826a1f3bf8ef186dd692d2b3500b036`
- Date/author: 2026-09-23 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `90f80c6bd` - feat(moe): 增加 aiter moe_c 后端选定环境变量 (#415)

- Full hash: `90f80c6bd5a831f40c29ec8a32200174e749de9f`
- Date/author: 2026-09-23 / Wenbo Zhu
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `6c0330d8d` - fix(w4a8): 修复 HIPC MoE scale 重复乘 16 与 HCU RoPE 启动越界 (#439)

- Full hash: `6c0330d8d877d146412e65e5cf6bf717a3004dae`
- Date/author: 2026-09-23 / lipenghui
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/layers/rotary_embedding/base.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/rotary_embedding/base.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2f93be6c5` - fix(kvcache): handle zero full iterations for asymmetric KV cache (#425)

- Full hash: `2f93be6c5e0db8a54fa76d10eab1887e7fcfd145`
- Date/author: 2026-09-23 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `066a95af7` - fix: fix lightop situ import regression bug and deepgemm w4a8 op interface change (#428)

- Full hash: `066a95af77c479b644e4477afc42b39246f7f58a`
- Date/author: 2026-09-23 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `6086af28d` - ci(hcu): migrate v0.5.18 workflows to organization runners (#465)

- Full hash: `6086af28ddb97c1cc4c9cf22fadd2940a1100105`
- Date/author: 2026-09-30 / dingxinlong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-states.yml`, `.github/workflows/pr-test-hcu.yml` 等 11 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-states.yml`; `.github/workflows/pr-test-hcu.yml` 等 11 个文件
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `1828115e0` - fix w4a16 moe asm error (#462)

- Full hash: `1828115e08aba1659f71c5da67f761343e3553f4`
- Date/author: 2026-09-30 / jiafei96
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `3854f7754` - opt(kda): update kda verify decode op from boltops (#458)

- Full hash: `3854f77546c1a65ebc26d86ab84f2ebd96740cc5`
- Date/author: 2026-09-30 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kda_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `e885e7223` - fix(hcu): restore ForwardBatch RMS quantization flag (#469)

- Full hash: `e885e7223180a8ddc2c9aa753a4c884cfc9ba72c`
- Date/author: 2026-09-30 / wu ju
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_forward_batch_hcu_state.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`
  - tests: `test/registered/unit/model_executor/test_forward_batch_hcu_state.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `cfa865d33` - fix deepgemm masked fp8 api upstream (#472)

- Full hash: `cfa865d339c0d7191dd044e6980006be799a570a`
- Date/author: 2026-10-08 / chaoyujiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b7e4eae12` - fix: remove alt_stream overlap copy when writing KV cache (#478)

- Full hash: `b7e4eae1243fb6de06507484afaddbc1715ee054`
- Date/author: 2026-10-08 / Wenbo Zhu
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/mem_cache/memory_pool.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `7fa7729c1` - fix(cache): harden Mooncake ReadPlan and PP direct-L3 cache loading (#482)

- Full hash: `7fa7729c1d9a3007baf471184ca709aece7fdbed`
- Date/author: 2026-10-08 / leichuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` 等 27 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`; `python/sglang/srt/managers/tokenizer_manager.py`; `python/sglang/srt/observability/req_time_stats.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_components/request_receiver.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`; `python/sglang/srt/mem_cache/unified_cache/components/full_component.py`; `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`; `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`; `python/sglang/srt/mem_cache/unified_radix_cache.py`
  - tests: `test/registered/unit/disaggregation/test_bootstrap_failure_release.py`; `test/registered/unit/disaggregation/test_mooncake_final_chunk_poll.py`; `test/registered/unit/managers/test_scheduler_bg_prefetch_collectives.py`; `test/registered/unit/managers/test_scheduler_deferred_reqs.py`; `test/registered/unit/managers/test_scheduler_forward_ingress_fixes.py`; `test/registered/unit/managers/test_scheduler_prefetch_startup_consensus.py`; `test/registered/unit/mem_cache/test_load_back_construction_consensus.py`; `test/registered/unit/mem_cache/test_mooncake_direct_linker_prefetch_capability.py` 等 11 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2cc1bcc28` - fix(deepgemm): 统一 INT8/FP8 权重重排与 FP8 masked GEMM 接口 (#484)

- Full hash: `2cc1bcc28c5c4b6e129ae4ce3dadbe3fbc2796cf`
- Date/author: 2026-10-09 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `test/registered/openai_server/validation/test_request_length_validation.py`, `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
  - tests: `test/registered/openai_server/validation/test_request_length_validation.py`; `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `a06c34ef7` - fix(ci): stage-b include 列表容忍分支差异的测试文件 (#485)

- Full hash: `a06c34ef7511fbf767d1e8f8314546492d5efb0e`
- Date/author: 2026-10-09 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `6ca7a1bd6` - fix(test): 修复 unified attention 单测 KV 索引构造 (#489)

- Full hash: `6ca7a1bd6a1e7f4719171e4afeb257e4507d3061`
- Date/author: 2026-10-09 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `test/registered/attention/test_triton_attention_kernels.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `test/registered/attention/test_triton_attention_kernels.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `1882acd8c` - fix(moe): restore DeepEP normal combine for HCU groupgemm (#491)

- Full hash: `1882acd8c659b9071ad341741e7b5beef1c40ab0`
- Date/author: 2026-10-09 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `bfbff7f68` - fix(hcu): preserve INT8 MoE fallback and restore AITER W8A8 compatibility (#487)

- Full hash: `bfbff7f68e024ed71aaec1054c1bdf8ad6df7adf`
- Date/author: 2026-10-09 / WenQ7
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/utils/triton_load_watch.py`, `test/registered/unit/distributed/test_aiter_custom_all_reduce_config.py`, `test/registered/unit/layers/moe/test_aiter_w8a8_compat.py`, `test/registered/unit/utils/test_triton_load_watch.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/utils/triton_load_watch.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
  - tests: `test/registered/unit/distributed/test_aiter_custom_all_reduce_config.py`; `test/registered/unit/layers/moe/test_aiter_w8a8_compat.py`; `test/registered/unit/utils/test_triton_load_watch.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `966f6da1b` - fix(hcu): avoid double packing channel FP8 DeepGEMM weights (#497)

- Full hash: `966f6da1bcf76359bbbd3f6919f9da6f83ae905a`
- Date/author: 2026-10-10 / chaoyujiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `e1eaf0829` - fix(moe): guard SBO setup for flat DeepEP dispatch (#501)

- Full hash: `e1eaf08298435a45133f48366cd75d2ccfd03ecb`
- Date/author: 2026-10-10 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/batch_overlap/single_batch_overlap.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/batch_overlap/single_batch_overlap.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `f106c5360` - perf(hcu): 优化小 batch W8A8 INT8 GEMM 的 Tiling 选择 (#502)

- Full hash: `f106c53608df6269af7296265f9097e9a80abbd2`
- Date/author: 2026-10-10 / Yongqiang Duan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `49bb75c79` - fix(diffusion): upload all video outputs to cloud storage

- Full hash: `49bb75c791c10b2114c52c58c8d0433bd03e0856`
- Date/author: 2026-10-12 / zhangpc3
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `aebf1a9f4` - fix(hcu): fix SlimQuant INT8 DeepEP routing and DeepGEMM weight packing (#514)

- Full hash: `aebf1a9f41ad5fd1e00ac1570e6b9e6a8128b237`
- Date/author: 2026-10-12 / chaoyujiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `018e5799a` - Fix/hcu aiter moe inplace (#517)

- Full hash: `018e5799abb14aa90d05af042db8b273bebc5df9`
- Date/author: 2026-10-13 / Wenbo Zhu
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/models/qwen2_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/models/qwen2_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `71b2ee4ea` - perf: add opt-in asynchronous prebuilt token H2D (#516)

- Full hash: `71b2ee4ea67b6be712a5575ed1dd0950607fc6b5`
- Date/author: 2026-10-13 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/environ.py`, `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`; `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/verify_mla.py`
  - tests: `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `9dd4e2e80` - [diffusion] attention: fix HCU Wan SLA and FA family admission (#519)

- Full hash: `9dd4e2e80065ba556c1beb1ffd8b1f2e29bdb085`
- Date/author: 2026-10-13 / FrankXu0908
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`, `python/sglang/multimodal_gen/runtime/platforms/rocm.py`, `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/test/unit/test_wan_sla_layout.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`; `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`; `python/sglang/multimodal_gen/runtime/platforms/rocm.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py`; `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/test/unit/test_wan_sla_layout.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `40c9ec29b` - fix(scheduler): keep DP health probes on the generation path (#528)

- Full hash: `40c9ec29b31d5a160c8d83d56949c58e76cc6c26`
- Date/author: 2026-10-14 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/scheduler.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `c2666f4b5` - [fix] 修复cp 逻辑：解决实际 token 不被整除时不走 cp 的问题 (#538)

- Full hash: `c2666f4b5c07e017ad9195c7435236517cda5f08`
- Date/author: 2026-10-15 / yangyn
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/dsa/utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `6fe59ce1a` - ci: release-pypi-nightly-hcu 多版本编译 (dtk26.04/py3.10+3.12, dtk26.10/py3.12) [rel/20260825_v0.5.18] (#544)

- Full hash: `6fe59ce1ab68fb4ae69951502b621daa5cde0c95`
- Date/author: 2026-10-16 / Crowder13
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-pypi-nightly-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `0bb71f0c7` - [fix] 解决 w4a8 aiter moe 不支持 swiglu_limit 功能 (#550)

- Full hash: `0bb71f0c7fd7faeab15402d9a2d5f6759f623120`
- Date/author: 2026-10-16 / yangyn
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b9e0052e9` - fix(hcu): keep the w8a8 smooth asm fast path off on gfx928 (#555)

- Full hash: `b9e0052e9e35ae3aa58d73ed685ae6191d64fc24`
- Date/author: 2026-10-19 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `a031c979a` - [fix] 修复非 AITER 路径下 compressed-tensors W8A8 FP8 MoE 权重被错误补齐导致输出乱码 (#564)

- Full hash: `a031c979a4a848bb6905386808d771b5782125e1`
- Date/author: 2026-10-20 / liuzj512
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `030f6254f` - perf(attention): add paged split-KV support and opt-in DSpark V2 (#553)

- Full hash: `030f6254f2d9d4abe9e57543e3f38757d12ec4ba`
- Date/author: 2026-10-20 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/attention/verify_mla.py`; `python/sglang/srt/layers/attention/triton_backend.py`
  - tests: `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `19175a690` - [Feat] build: Add build wheel scripts (#569)

- Full hash: `19175a69044f2407fa371677a0a7d9be4e226bf2`
- Date/author: 2026-10-20 / XiaokunDing
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 模型支持/运行时入口
- Main files: `README_HCU.md`, `scripts/build_hcu_wheels.sh`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `README_HCU.md`; `scripts/build_hcu_wheels.sh`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `9f7bfb351` - fix(hcu): skip the w8a8 smooth asm fast path when M=0 (#573)

- Full hash: `9f7bfb351d8b2680399994cbade9e83d10972c93`
- Date/author: 2026-10-21 / Jane
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `464bebd64` - [Fix][v0.5.18] Backport reasoning token accounting fix from upstream #41460 (#579)

- Full hash: `464bebd6407de97376f3d00c682036b0494b7ab7`
- Date/author: 2026-10-22 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`
  - tests: `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `cbaf42c07` - Fix auxiliary HiCache load-back pending collisions (#591)

- Full hash: `cbaf42c071ebacf512215d320eae9c155b29e0e3`
- Date/author: 2026-10-26 / chaoyujiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`
  - tests: `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `1343bb07e` - [Fix] deepgemm: 修复 w8a8-fp8 旧版重排逻辑 (#608)

- Full hash: `1343bb07ef5f41dcea4dca531b794735203310eb`
- Date/author: 2026-10-28 / yangyn
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `448c57ad4` - [fix] 修复 w8a8_int8 量化时视觉层 qkv_proj 未命中忽略名单导致被错误量化 (#632)

- Full hash: `448c57ad4d4650d1a0a8ae43fdd416e254f1d4a8`
- Date/author: 2026-11-03 / liuzj512
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/w8a8_int8.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/w8a8_int8.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `c760e11b4` - fix: fix w4a8 int4 deepgemm hipc kernel interface mismatch (#638)

- Full hash: `c760e11b4e67898d95038c9ea87e5b83620df7ea`
- Date/author: 2026-11-03 / daishiqiang
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## Local-only branch update from release/20260825_v0.5.18 to release_v0.5.18_deepseekv4

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-05
- Commits in this section: 67 (merges: 0)
- Branch segments: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `.github/workflows/release-docker-hcu.yml` | `6b468d012`, `68dcd498a`, `8fa7122b3`, `7c8272a3a`, `5c03a8e22`, `2871c8fdd`, `5e8269d55`, `e05f146be`, `fb46d17ad`, `50b0d0051`, `87b9d5c85`, `6dac3481c`, ... (13 total) |
| `.github/workflows/release-pr-hcu.yml` | `a2de3b8cf`, `2866df994`, `6b468d012`, `ae14a99e5`, `adc1d69b2`, `cb932f5fb`, `a981685e7`, `665b27d1f`, `e05f146be`, `098f31d69` |
| `.github/workflows/cookbook-deployment-smoke.yml` | `50b0d0051`, `f9b972b37`, `b6dd37e66`, `78c700ee0`, `cc3758967`, `87b9d5c85`, `f89209aa8`, `a8543c813`, `029b6e641` |
| `.github/workflows/pr-test-hcu.yml` | `f6d701c52`, `e864c3028`, `b5108cc7f`, `575cf4797`, `ae14a99e5`, `adc1d69b2`, `e05f146be`, `098f31d69`, `25aa13e98` |
| `.github/workflows/nightly-test-hcu.yml` | `a2de3b8cf`, `2866df994`, `b5108cc7f`, `adc1d69b2`, `b5ca753bc`, `e05f146be`, `50b0d0051` |
| `.github/workflows/nightly-test-operator-hcu.yml` | `fb46d17ad`, `4205397cb`, `e295faff5`, `6dac3481c`, `fd98647ed`, `db479b030`, `9fb319cc3` |
| `.github/workflows/release-pypi-nightly-hcu.yml` | `a2de3b8cf`, `7609d9af6`, `6b468d012`, `68dcd498a`, `7be1324cf`, `e05f146be` |
| `docker/hcu.Dockerfile` | `7609d9af6`, `6b468d012`, `68dcd498a`, `7c8272a3a`, `5c03a8e22`, `2871c8fdd` |
| `.github/workflows/release-whl-manual-hcu.yml` | `d1adf7b50`, `94e9fa4b1`, `c94c3ca2c`, `bc990ebd5` |
| `scripts/ci/hcu/hcu_ci_install_dependency.sh` | `2828bde71`, `0af71f61b`, `575cf4797`, `adc1d69b2` |
| `.github/workflows/nightly-test-image-hcu.yml` | `8fa7122b3`, `0457572a1`, `e05f146be` |
| `python/sglang/srt/managers/scheduler.py` | `962617b2d`, `4c5ac2ee0`, `f0a0530ce` |
| `python/sglang/srt/server_args.py` | `fd4157047`, `8dd5daf2f`, `962617b2d` |
| `scripts/ci/hcu/hcu_ci_exec.sh` | `9d261478d`, `2828bde71`, `0af71f61b` |
| `.github/workflows/dashhub-recover-41338132822.yml` | `471ab8254`, `594e1ae94` |
| `.github/workflows/pr-states.yml` | `3ca61517d`, `e05f146be` |
| `python/sglang/multimodal_gen/runtime/platforms/__init__.py` | `d42ecf6fe`, `fd4157047` |
| `python/sglang/srt/managers/tokenizer_manager.py` | `3b0e4a073`, `c66f34363` |
| `test/run_suite.py` | `8dd5daf2f`, `6fe7ce909` |
| `.github/workflows/hcu-feishu-notify-preview.yml` | `e05f146be` |
| `.github/workflows/hcu-full-enabled.yml` | `e05f146be` |
| `.github/workflows/hcu-manual-model-test.yml` | `e05f146be` |
| `.github/workflows/labeler.yml` | `e05f146be` |
| `.github/workflows/lint-hcu.yml` | `e05f146be` |
| `.github/workflows/nightly-release-gateway.yml` | `990a1a798` |
| `.github/workflows/quality-gate.yml` | `ae5c33991` |
| `README_HCU.md` | `9d261478d` |
| `docker/image-citest-conf-hcu.yaml` | `8fa7122b3` |
| `docs/docs/references/environment_variables.mdx` | `3b0e4a073` |
| `python/pyproject_hcu.toml` | `7609d9af6` |
| `python/sglang/benchmark/datasets/common.py` | `fc095e059` |
| `python/sglang/benchmark/datasets/generated_shared_prefix.py` | `fc095e059` |
| `python/sglang/benchmark/serving.py` | `fc095e059` |
| `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | `962617b2d` |
| `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py` | `962617b2d` |
| `python/sglang/srt/configs/model_config.py` | `962617b2d` |
| `python/sglang/srt/constrained/grammar_manager.py` | `f0a0530ce` |
| `python/sglang/srt/disaggregation/prefill.py` | `4c5ac2ee0` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` | `d42ecf6fe` |
| `python/sglang/srt/entrypoints/http_server.py` | `eaa872862` |
| ... | 81 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | `a96aed11f` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子 | `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py` |
| 2026-08-21 | `d42ecf6fe` | `release/20260825_v0.5.18..main` | 缺陷修复 | Fix HCU detection and sanitized topology diagnostics | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt` |
| 2026-08-24 | `fd4157047` | `release/20260825_v0.5.18..main` | 通用实现调整 | Refine HCU platform diagnostics and CLI help | `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/server_args.py` |
| 2026-08-25 | `d1adf7b50` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [feature] manual compile ci | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-25 | `94e9fa4b1` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload) | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-26 | `990a1a798` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci: disable scheduled gateway nightly release | `.github/workflows/nightly-release-gateway.yml` |
| 2026-08-26 | `8dd5daf2f` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | Refine HCU and AMD CLI help text | `python/sglang/srt/server_args.py`, `test/run_suite.py` |
| 2026-08-26 | `c94c3ca2c` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix: gateway wheel is at workspace root target/wheels | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-26 | `f6d701c52` | `release/20260825_v0.5.18..main` | 缺陷修复 | Fix stale HCU Stage B test paths | `.github/workflows/pr-test-hcu.yml` |
| 2026-08-26 | `a2de3b8cf` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): use bash for wheel build jobs | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-27 | `2866df994` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): trust wheel build workspaces | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-27 | `7609d9af6` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | [feature]适配hcu发包 | `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml` |
| 2026-08-27 | `6b468d012` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` and 4 files in total |
| 2026-08-28 | `68dcd498a` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-28 | `bc990ebd5` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复) | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-31 | `3ca61517d` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` |
| 2026-08-31 | `e864c3028` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci: enable HCU PR tests for release branches (#272) | `.github/workflows/pr-test-hcu.yml` |
| 2026-09-01 | `8fa7122b3` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE]构建镜像之后触发模型测试 (#277) | `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml` |
| 2026-09-02 | `9d261478d` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [CI] Update HCU model asset paths on main (#285) | `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh` and 10 files in total |
| 2026-09-02 | `6fe7ce909` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): restore run suite file filters (#290) | `test/run_suite.py` |
| 2026-09-03 | `2828bde71` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | ci(hcu): align llguidance and model asset paths (#299) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` |
| 2026-09-04 | `0457572a1` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308) | `.github/workflows/nightly-test-image-hcu.yml` |
| 2026-09-08 | `0af71f61b` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(ci): update HCU evaluation dependencies and asset paths (#325) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-09-14 | `b5108cc7f` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): use v0.5.18 image and restore eval dependencies (#347) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` and 4 files in total |
| 2026-09-14 | `516261baf` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): register sampling test and adjust MMLU threshold (#359) | `test/registered/sampling/test_pytorch_sampling_backend.py` |
| 2026-09-14 | `575cf4797` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): restore source mode for test-only PRs (#364) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` |
| 2026-09-15 | `7c8272a3a` | `release/20260825_v0.5.18..main` | 缺陷修复 | [BUGFIX]更新AICC安装方式 (#367) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-15 | `ae14a99e5` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(ci): fix HCU wheel build target routing (#372) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-09-15 | `5c03a8e22` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-16 | `adc1d69b2` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): align main wheel builds with 0.5.18 runtime (#379) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` and 6 files in total |
| 2026-09-21 | `ae5c33991` | `release/20260825_v0.5.18..main` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-09-21 | `cb932f5fb` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | feat(ci) compaity sgl-kernal main to v0.5.12 (#421) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-21 | `a981685e7` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix release-pr-hcu.yml build sglang (#423) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-22 | `b5ca753bc` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): run nightly against v0.5.18 and report its results (#432) | `.github/workflows/nightly-test-hcu.yml` |
| 2026-09-23 | `2871c8fdd` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-23 | `7be1324cf` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci: report sglang nightly packages to DashHub (#424) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-24 | `665b27d1f` | `release/20260825_v0.5.18..main` | 缺陷修复 | feat(ci) fix main build whl failed (#449) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-28 | `5e8269d55` | `release/20260825_v0.5.18..main` | 缺陷修复 | [BUGFIX]镜像DTK版本号不对 (#447) | `.github/workflows/release-docker-hcu.yml` |
| 2026-09-30 | `e05f146be` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | ci(hcu): migrate main workflows to organization runners (#463) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` and 12 files in total |
| 2026-10-09 | `fb46d17ad` | `release/20260825_v0.5.18..main` | 性能/后端优化 | add optest process (#481) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-09 | `f0ee2a505` | `release/20260825_v0.5.18..main` | 缺陷修复 | FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473) | `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py` |
| 2026-10-10 | `4205397cb` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | add password-free download code (#499) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-10 | `3b0e4a073` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [Fix] Bound crash diagnostics and fatal shutdown on main (#498) | `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py` and 6 files in total |
| 2026-10-12 | `50b0d0051` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | Delegate HCU model deployment smoke CI to external controller (#503) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-12 | `f9b972b37` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | Use a clean checkout directory for the model smoke controller (#510) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `b6dd37e66` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | Run cookbook smoke tests for all cases by default | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `e295faff5` | `release/20260825_v0.5.18..main` | 性能/后端优化 | update ci name&&add optest log (#515) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-14 | `78c700ee0` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | Add image input to cookbook deployment smoke workflow (#530) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-15 | `cc3758967` | `release/20260825_v0.5.18..main` | 通用实现调整 | Pass DashHub credential to deployment smoke controller (#534) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-15 | `fc095e059` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533) | `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` and 4 files in total |
| 2026-10-16 | `87b9d5c85` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | Run cookbook deployment checks after HCU image publishing (#548) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-19 | `f89209aa8` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | ci: pass package server to Cookbook model tests (#556) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-20 | `a8543c813` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | [CI] cookbook: Add BW1000 deployment smoke tests (#570) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-28 | `6dac3481c` | `release/20260825_v0.5.18..main` | 缺陷修复 | [Fix] ci: Preserve model cases in DashHub operator reporting (#604) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-28 | `098f31d69` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-10-28 | `029b6e641` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | [CI] model-ci: Pass history token for daily comparison report (#607) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-28 | `fd98647ed` | `release/20260825_v0.5.18..main` | 缺陷修复 | [Fix] ci: Restore previous DashHub operator reporting (#614) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-29 | `25aa13e98` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(ci) rebase pr-test-hcu.yml (#617) | `.github/workflows/pr-test-hcu.yml` |
| 2026-10-29 | `db479b030` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [CI] optest: Report outcome to DashHub (#619) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-29 | `9fb319cc3` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [CI] optest: Require every enabled operator result (#622) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-11-02 | `471ab8254` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | Add one-time DashHub recovery for run 41338132822 (#633) | `.github/workflows/dashhub-recover-41338132822.yml` |
| 2026-11-02 | `594e1ae94` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [Chore] ci: Remove completed DashHub recovery workflow (#634) | `.github/workflows/dashhub-recover-41338132822.yml` |
| 2026-10-23 | `962617b2d` | `release/20260825_v0.5.18..release/20261023_v0.5.18_welm` | 性能/后端优化 | WeLM v4.5 support on HCU (squash of yaoyupings/sglang-das v0.5.18_welm) | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/configs/model_config.py` and 55 files in total |
| 2026-10-20 | `eaa872862` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | fix: support API key with multiple tokenizer workers (#559) | `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/auth.py`, `test/registered/unit/entrypoints/test_http_server_auth_config.py` and 5 files in total |
| 2026-10-20 | `4c5ac2ee0` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | fix(disagg): defer cached-prefix sends during cache loads (#562) | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `test/manual/hicache/test_pd_cached_prefix_load_ordering.py` |
| 2026-10-23 | `f0a0530ce` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | [Fix] grammar: 同步 Prefill CP 的 Grammar 请求准入与失败状态 (#589) | `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/constrained/test_grammar_manager.py` |
| 2026-10-30 | `c66f34363` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | [Fix] TokenizerManager: 修复客户端断开后已下发请求未被终止的问题 (#628) | `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py` |

### Per-Commit Audit Cards

#### Commit `a96aed11f` - [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子

- Full hash: `a96aed11f05f65d18f5bd46446b4ca9b7ac82105`
- Date/author: 2026-08-21 / zhuwenbopro
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `d42ecf6fe` - Fix HCU detection and sanitized topology diagnostics

- Full hash: `d42ecf6fe9854d6127c167959fe7bec30439b73b`
- Date/author: 2026-08-21 / reverie-hub
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`; `scripts/ci/hcu/hcu_rename_allowlist.txt`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `fd4157047` - Refine HCU platform diagnostics and CLI help

- Full hash: `fd415704795411fa8fcbc7d7571c41dcb3d1c431`
- Date/author: 2026-08-24 / reverie-hub
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 通用实现调整
- Main files: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`
  - runtime-model: `python/sglang/srt/server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `d1adf7b50` - [feature] manual compile ci

- Full hash: `d1adf7b503b20e64e07c38946a067ee90c428962`
- Date/author: 2026-08-25 / zhangyh15
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-whl-manual-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `94e9fa4b1` - ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload)

- Full hash: `94e9fa4b1d10f14c6120bab4f5416caf6e318cd9`
- Date/author: 2026-08-25 / zhangyh15
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-whl-manual-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `990a1a798` - ci: disable scheduled gateway nightly release

- Full hash: `990a1a798d40ccea97ef91c16a9d8cd8f25957e2`
- Date/author: 2026-08-26 / dddddddxl
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-release-gateway.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-release-gateway.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `8dd5daf2f` - Refine HCU and AMD CLI help text

- Full hash: `8dd5daf2fa5555ab13751b159703124fd493a437`
- Date/author: 2026-08-26 / reverie-hub
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `python/sglang/srt/server_args.py`, `test/run_suite.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/server_args.py`
  - tests: `test/run_suite.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `c94c3ca2c` - fix: gateway wheel is at workspace root target/wheels

- Full hash: `c94c3ca2c8341c501b46a32c750e32dfe8ce4e06`
- Date/author: 2026-08-26 / zhangyh15
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/release-whl-manual-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `f6d701c52` - Fix stale HCU Stage B test paths

- Full hash: `f6d701c520529490926e3c350682b7fe7ca6f9d0`
- Date/author: 2026-08-26 / reverie-hub
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `a2de3b8cf` - ci(hcu): use bash for wheel build jobs

- Full hash: `a2de3b8cffc365e5f813d2ddd6c7226abe29db90`
- Date/author: 2026-08-26 / dddddddxl
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `2866df994` - ci(hcu): trust wheel build workspaces

- Full hash: `2866df9948b40e81405fcf5947ef74b8f744c9a3`
- Date/author: 2026-08-27 / dddddddxl
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `7609d9af6` - [feature]适配hcu发包

- Full hash: `7609d9af69ac40ed6730564cde4934d5b3e4a540`
- Date/author: 2026-08-27 / zhangyh15
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`; `python/pyproject_hcu.toml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `6b468d012` - [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda

- Full hash: `6b468d012bcf693157cee193493842185165b93b`
- Date/author: 2026-08-27 / zhangyh15
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `68dcd498a` - [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致

- Full hash: `68dcd498aa7550a39e7f53b6588e19785efd5cae`
- Date/author: 2026-08-28 / zhangyh15
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `bc990ebd5` - [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复)

- Full hash: `bc990ebd52e0ae2500dc3c0ab4eeba187e84965b`
- Date/author: 2026-08-28 / zhangyh15
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-whl-manual-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `3ca61517d` - ci-remove-amd-status-from-pr-summaries

- Full hash: `3ca61517d037e82ba19c981dd66ddaf0245e85cd`
- Date/author: 2026-08-31 / dddddddxl
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/pr-states.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-states.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `e864c3028` - ci: enable HCU PR tests for release branches (#272)

- Full hash: `e864c302870000325162a5788883997cc850ade8`
- Date/author: 2026-08-31 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/pr-test-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `8fa7122b3` - [FEATURE]构建镜像之后触发模型测试 (#277)

- Full hash: `8fa7122b3ace4a4de48372ee3c4c3346871281d7`
- Date/author: 2026-09-01 / Crowder13
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
  - other: `docker/image-citest-conf-hcu.yaml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `9d261478d` - [CI] Update HCU model asset paths on main (#285)

- Full hash: `9d261478d6ace185f3e35a7211fc411b64d2057f`
- Date/author: 2026-09-02 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`, `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py` 等 10 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_exec.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`; `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py`; `test/registered/hcu/spec/test_ngram_speculative_decoding_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `6fe7ce909` - ci(hcu): restore run suite file filters (#290)

- Full hash: `6fe7ce9097c8e9f1b7dccefbe4834a7f928a78c2`
- Date/author: 2026-09-02 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `test/run_suite.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `test/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `2828bde71` - ci(hcu): align llguidance and model asset paths (#299)

- Full hash: `2828bde71da3f5f6314aa4022ae7e163dfc33ada`
- Date/author: 2026-09-03 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `0457572a1` - [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308)

- Full hash: `0457572a14edd55e05220726ff4a8af8b1931771`
- Date/author: 2026-09-04 / Crowder13
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-image-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-image-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `0af71f61b` - fix(ci): update HCU evaluation dependencies and asset paths (#325)

- Full hash: `0af71f61b693c2bd2817a678e007660222db9bf3`
- Date/author: 2026-09-08 / tianly
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/hcu_ci_start_container.sh`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

#### Commit `b5108cc7f` - ci(hcu): use v0.5.18 image and restore eval dependencies (#347)

- Full hash: `b5108cc7fea82d75da174f8f6681a843d43c462b`
- Date/author: 2026-09-14 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/utils/sgl_eval_ref.sh`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/utils/sgl_eval_ref.sh`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `516261baf` - ci(hcu): register sampling test and adjust MMLU threshold (#359)

- Full hash: `516261baf108e56bcb4a03dc7294a936e9656a2d`
- Date/author: 2026-09-14 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `test/registered/sampling/test_pytorch_sampling_backend.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `test/registered/sampling/test_pytorch_sampling_backend.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `575cf4797` - ci(hcu): restore source mode for test-only PRs (#364)

- Full hash: `575cf47976761be9916048cfe2ca244b56d63fab`
- Date/author: 2026-09-14 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
  - tests: `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `7c8272a3a` - [BUGFIX]更新AICC安装方式 (#367)

- Full hash: `7c8272a3a32d25391c8bc20e0c0678d3c9ac895d`
- Date/author: 2026-09-15 / Crowder13
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `ae14a99e5` - fix(ci): fix HCU wheel build target routing (#372)

- Full hash: `ae14a99e502d0e5dbed8abf42e3b35eb8807c3c5`
- Date/author: 2026-09-15 / tianly
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `5c03a8e22` - [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376)

- Full hash: `5c03a8e22f8cfeef0f10cd909231862bd446cc30`
- Date/author: 2026-09-15 / Crowder13
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `adc1d69b2` - ci(hcu): align main wheel builds with 0.5.18 runtime (#379)

- Full hash: `adc1d69b2a610fc000ca27e4b92c72e9c1b85044`
- Date/author: 2026-09-16 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/test_hcu_build_alignment.py`, `scripts/ci/hcu/test_hcu_wheel_version.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/test_hcu_build_alignment.py`; `scripts/ci/hcu/test_hcu_wheel_version.py`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `ae5c33991` - Update quality gate workflow to use stable version

- Full hash: `ae5c33991be7f0e277f71c4e853c10fc11cbe627`
- Date/author: 2026-09-21 / Lvjiajia
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/quality-gate.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/quality-gate.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `cb932f5fb` - feat(ci) compaity sgl-kernal main to v0.5.12 (#421)

- Full hash: `cb932f5fbd904a577093a262c6a101834a1ef994`
- Date/author: 2026-09-21 / 463975089
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-pr-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pr-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `a981685e7` - fix release-pr-hcu.yml build sglang (#423)

- Full hash: `a981685e7f137a9e0629cbdcad2ad7bdd42017b9`
- Date/author: 2026-09-21 / 463975089
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/release-pr-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pr-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `b5ca753bc` - ci(hcu): run nightly against v0.5.18 and report its results (#432)

- Full hash: `b5ca753bc8e054ce99b4c01b0369eb89c6870dbb`
- Date/author: 2026-09-22 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/nightly-test-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `2871c8fdd` - ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438)

- Full hash: `2871c8fdd9594de894546b144d253c3dd88fd900`
- Date/author: 2026-09-23 / Crowder13
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `7be1324cf` - ci: report sglang nightly packages to DashHub (#424)

- Full hash: `7be1324cf827dafe9f09ec3f86ade353801b5e1e`
- Date/author: 2026-09-23 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/release-pypi-nightly-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `665b27d1f` - feat(ci) fix main build whl failed (#449)

- Full hash: `665b27d1fa35017a437b0aa0099a5f8aa33e5d9b`
- Date/author: 2026-09-24 / 463975089
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/release-pr-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-pr-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `5e8269d55` - [BUGFIX]镜像DTK版本号不对 (#447)

- Full hash: `5e8269d55a8cf4629cc39a3171169f4aa8b4d14b`
- Date/author: 2026-09-28 / Crowder13
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/release-docker-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/release-docker-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `e05f146be` - ci(hcu): migrate main workflows to organization runners (#463)

- Full hash: `e05f146bed9ca80c72a18a4946fd6f838d8e7774`
- Date/author: 2026-09-30 / dingxinlong
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/pr-states.yml` 等 12 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/pr-states.yml` 等 12 个文件
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `fb46d17ad` - add optest process (#481)

- Full hash: `fb46d17ad9f633aa7fee521484262b0c26de560d`
- Date/author: 2026-10-09 / Lee156
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `f0ee2a505` - FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473)

- Full hash: `f0ee2a5059c2d6a167bee3d996bca004276b3138`
- Date/author: 2026-10-09 / JackPeng
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/managers/detokenizer_manager.py`
  - tests: `test/registered/unit/managers/test_detokenizer_incremental.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `4205397cb` - add password-free download code (#499)

- Full hash: `4205397cbcf8c60852fadd7306cea32f2541a19d`
- Date/author: 2026-10-10 / Lee156
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/nightly-test-operator-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `3b0e4a073` - [Fix] Bound crash diagnostics and fatal shutdown on main (#498)

- Full hash: `3b0e4a07393778001dcd518d2b11de225e1be8c8`
- Date/author: 2026-10-10 / 王启宇
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`, `test/registered/unit/utils/test_bounded_fatal_shutdown.py`, `test/registered/unit/utils/test_bounded_pyspy.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - docs-bench: `docs/docs/references/environment_variables.mdx`
  - other: `python/sglang/srt/managers/multi_tokenizer_mixin.py`; `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-perf: `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`
  - tests: `test/registered/unit/utils/test_bounded_fatal_shutdown.py`; `test/registered/unit/utils/test_bounded_pyspy.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `50b0d0051` - Delegate HCU model deployment smoke CI to external controller (#503)

- Full hash: `50b0d005189ee23cf3046b86dc44986c5e6b9345`
- Date/author: 2026-10-12 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `f9b972b37` - Use a clean checkout directory for the model smoke controller (#510)

- Full hash: `f9b972b372f8695154301e2d7cee24195a963250`
- Date/author: 2026-10-12 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `b6dd37e66` - Run cookbook smoke tests for all cases by default

- Full hash: `b6dd37e66ad4f820a75614c8b0e6f54ffa67c796`
- Date/author: 2026-10-12 / gcy
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `e295faff5` - update ci name&&add optest log (#515)

- Full hash: `e295faff5dc889c97626f7bd25f6a8ca0a0f100c`
- Date/author: 2026-10-12 / Lee156
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-operator-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `78c700ee0` - Add image input to cookbook deployment smoke workflow (#530)

- Full hash: `78c700ee0100f215268a3a802538881f281f29e2`
- Date/author: 2026-10-14 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `cc3758967` - Pass DashHub credential to deployment smoke controller (#534)

- Full hash: `cc3758967d74748204015a050182e5ad176c8a08`
- Date/author: 2026-10-15 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 通用实现调整
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `fc095e059` - fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533)

- Full hash: `fc095e059889d2fae91e86a5b3e5fa19eb8d7a34`
- Date/author: 2026-10-15 / chaoyujiang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/benchmark/datasets/common.py`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`
  - tests: `test/registered/bench_fn/test_benchmark_datasets_api.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `87b9d5c85` - Run cookbook deployment checks after HCU image publishing (#548)

- Full hash: `87b9d5c85eafab11fe18235718c1af37b348d784`
- Date/author: 2026-10-16 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/release-docker-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `f89209aa8` - ci: pass package server to Cookbook model tests (#556)

- Full hash: `f89209aa84a4fd0619d0662f6adf6980740efc78`
- Date/author: 2026-10-19 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `a8543c813` - [CI] cookbook: Add BW1000 deployment smoke tests (#570)

- Full hash: `a8543c8131d429500411b8ba235b5411ddbabbd3`
- Date/author: 2026-10-20 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `6dac3481c` - [Fix] ci: Preserve model cases in DashHub operator reporting (#604)

- Full hash: `6dac3481cd73b48641f481b14858187d1936ee81`
- Date/author: 2026-10-28 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `098f31d69` - fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612)

- Full hash: `098f31d695ce94169e6adf9ce55109beb532b326`
- Date/author: 2026-10-28 / 463975089
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `029b6e641` - [CI] model-ci: Pass history token for daily comparison report (#607)

- Full hash: `029b6e6418828280e22086449dfa174433d2788b`
- Date/author: 2026-10-28 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/cookbook-deployment-smoke.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `fd98647ed` - [Fix] ci: Restore previous DashHub operator reporting (#614)

- Full hash: `fd98647ed1fc3d911926ea9d399b69934303c104`
- Date/author: 2026-10-28 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `25aa13e98` - fix(ci) rebase pr-test-hcu.yml (#617)

- Full hash: `25aa13e98fe76d262d87c0b798ec8a3215ffb703`
- Date/author: 2026-10-29 / 463975089
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 缺陷修复
- Main files: `.github/workflows/pr-test-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/pr-test-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `db479b030` - [CI] optest: Report outcome to DashHub (#619)

- Full hash: `db479b030f0975dbda241bf46fc4556a89a02365`
- Date/author: 2026-10-29 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-operator-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `9fb319cc3` - [CI] optest: Require every enabled operator result (#622)

- Full hash: `9fb319cc33a15b624970b0f5e45020e2a573dc07`
- Date/author: 2026-10-29 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-operator-hcu.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `471ab8254` - Add one-time DashHub recovery for run 41338132822 (#633)

- Full hash: `471ab8254520c958d3c614e768a29b10423f7cf2`
- Date/author: 2026-11-02 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/dashhub-recover-41338132822.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `594e1ae94` - [Chore] ci: Remove completed DashHub recovery workflow (#634)

- Full hash: `594e1ae94c6103dabed4152a4ebbcca6fb049aeb`
- Date/author: 2026-11-02 / guochenyang
- Branch update: `release/20260825_v0.5.18..main`
- Auto category: 测试/文档/基准
- Main files: `.github/workflows/dashhub-recover-41338132822.yml`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

#### Commit `962617b2d` - WeLM v4.5 support on HCU (squash of yaoyupings/sglang-das v0.5.18_welm)

- Full hash: `962617b2d8f42175937aa79cfe36d14db4e02884`
- Date/author: 2026-10-23 / sunjf
- Branch update: `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/welm_dedup_decode.py`, `python/sglang/srt/layers/attention/welm_fa256_src/build.sh` 等 55 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/welm_oe_host.py`; `python/sglang/srt/layers/welm_oe_host_src/build.sh`; `python/sglang/srt/layers/welm_oe_host_src/export_oe.py`; `python/sglang/srt/layers/welm_oe_host_src/oe_host_gather.cpp`; `python/sglang/srt/layers/welmv4_fast_op.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/runner_utils/buffers.py`; `python/sglang/srt/models/welmv4.py`; `python/sglang/srt/models/welmv4_nextn.py`; `python/sglang/srt/models/welmv4_vlm.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_common.py` 等 10 个文件
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/welm_dedup_decode.py`; `python/sglang/srt/layers/attention/welm_fa256_src/build.sh`; `python/sglang/srt/layers/attention/welm_fa256_src/flags.txt`; `python/sglang/srt/layers/attention/welm_fa256_src/lflags.txt`; `python/sglang/srt/layers/attention/welm_fa256_src/welm_fa256.cpp` 等 31 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `eaa872862` - fix: support API key with multiple tokenizer workers (#559)

- Full hash: `eaa8728623fbab132f881e470e7715ff69ac9bff`
- Date/author: 2026-10-20 / zhengzhi
- Branch update: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/auth.py`, `test/registered/unit/entrypoints/test_http_server_auth_config.py`, `test/registered/unit/spec/test_ngram_corpus.py`, `test/registered/unit/utils/test_http_server_auth.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/utils/auth.py`
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`
  - tests: `test/registered/unit/entrypoints/test_http_server_auth_config.py`; `test/registered/unit/spec/test_ngram_corpus.py`; `test/registered/unit/utils/test_http_server_auth.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `4c5ac2ee0` - fix(disagg): defer cached-prefix sends during cache loads (#562)

- Full hash: `4c5ac2ee05e286d7f5c05cb789c60fdea4db0f58`
- Date/author: 2026-10-20 / 千纱都
- Branch update: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `test/manual/hicache/test_pd_cached_prefix_load_ordering.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/prefill.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
  - tests: `test/manual/hicache/test_pd_cached_prefix_load_ordering.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f0a0530ce` - [Fix] grammar: 同步 Prefill CP 的 Grammar 请求准入与失败状态 (#589)

- Full hash: `f0a0530ce34fa7986c05c010146acb8ea0c20464`
- Date/author: 2026-10-23 / JingLee
- Branch update: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/constrained/test_grammar_manager.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/constrained/grammar_manager.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
  - tests: `test/registered/unit/constrained/test_grammar_manager.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `c66f34363` - [Fix] TokenizerManager: 修复客户端断开后已下发请求未被终止的问题 (#628)

- Full hash: `c66f3436365416bf3bb14c6e1b3665b669608573`
- Date/author: 2026-10-30 / zhengzhi
- Branch update: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/managers/tokenizer_manager.py`
  - tests: `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
