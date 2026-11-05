# sglang Shared Framework Commits 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| ... | 2951 more files omitted from table; all were used for git tracing. |

| - | 无本地独有提交 |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 53
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

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

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## v0.5.8_dev 到 v0.5.12_dev 本地独有提交补充

### 覆盖说明

- 来源索引: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- 来源工作树: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交。
- 本章节提交数: 68
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
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

### 逐 Commit 审计卡

#### Commit `155c1f634` - sglang dcu 0.5.9base patch->hash(5dd49e07)

- 完整 hash: `155c1f6345bab53c8b26616172893defdc051761`
- 时间/作者: 2026-02-27 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` 等 104 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3_moe.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/attention/lightop_concat.py`; `python/sglang/srt/layers/attention/nsa_backend.py` 等 64 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - other: `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py` 等 30 个文件
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `1dd77c2e6` - Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev'

- 完整 hash: `1dd77c2e6e865c3bef8bd225a65938a02c2d1f42`
- 时间/作者: 2026-02-27 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`, `requirements_dcu.txt`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `README_DCU.md`
  - other: `requirements_dcu.txt`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `356694d6b` - Merge branch 'cherry-pick-1dfc3015' into 'v0.5.9_dev'

- 完整 hash: `356694d6b92ad51a3306c8ac589425490a6f72c1`
- 时间/作者: 2026-02-27 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `403027fd8` - Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev'

- 完整 hash: `403027fd8458cae4cab8c18358f06b948955325b`
- 时间/作者: 2026-02-27 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `8a6520cd8` - Merge branch 'cherry-pick-3b73900b' into 'v0.5.9_dev'

- 完整 hash: `8a6520cd86730570c6f2ff26dc7a5bce4b527ac2`
- 时间/作者: 2026-02-27 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `c77a90449` - Debugging through TP parallel

- 完整 hash: `c77a904497e951351de67c53cb52ec7dad2ed6a1`
- 时间/作者: 2026-02-27 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `sgl-kernel/setup_hip.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `sgl-kernel/setup_hip.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `d62ea43c1` - Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev'

- 完整 hash: `d62ea43c13d89e9a3b372c6d54dac8ed8353a740`
- 时间/作者: 2026-02-27 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `a5c071e36` - Merge branch 'cherry-pick-fc0f9e89' into 'v0.5.9_dev'

- 完整 hash: `a5c071e366454178b06e6f18955d3c64966fd75b`
- 时间/作者: 2026-03-06 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `b3f4b0861` - Merge branch 'v0.5.8_dev_sxl' into 'v0.5.8_dev'

- 完整 hash: `b3f4b086156d31e528ac3720765535f687782127`
- 时间/作者: 2026-03-06 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/mem_cache/allocator.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 12 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/communicator.py`
  - other: `python/sglang/srt/mem_cache/allocator.py`; `python/sglang/srt/mem_cache/common.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/speculative/eagle_info.py`; `python/sglang/srt/speculative/eagle_info_v2.py`; `python/sglang/srt/speculative/spec_utils.py`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `b930b5645` - Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev'

- 完整 hash: `b930b5645eb1978f8867c6f0594138e6cedc09c2`
- 时间/作者: 2026-03-06 / liucong8560
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `5d7c6b671` - Merge branch 'v0.5.8_dev_mx' into 'v0.5.8_dev'

- 完整 hash: `5d7c6b67152f6c381210e9f3e0f62fba4db4ea7f`
- 时间/作者: 2026-03-07 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/unquant.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/layers/quantization/unquant.py`
  - other: `python/sglang/srt/batch_overlap/single_batch_overlap.py`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `686124d90` - 适配fuse_moe_fp8_w8a8

- 完整 hash: `686124d90a495d9337f99869cf20fdd7fdd556ba`
- 时间/作者: 2026-03-07 / liucong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `76c737ac7` - Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev'

- 完整 hash: `76c737ac7b7b3167d3c57f1ec08c88267f5c4961`
- 时间/作者: 2026-03-07 / liucong8560
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `8ba520fcc` - fix error when set dtype float16

- 完整 hash: `8ba520fcc8ce231449229252d52a83f2baede139`
- 时间/作者: 2026-03-07 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/quantization/unquant.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/unquant.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `c5a76ad9e` - Merge branch 'cherry-pick-a16f19db' into 'v0.5.9_dev'

- 完整 hash: `c5a76ad9ecdd9894da92d4751f2b596d339e3cd0`
- 时间/作者: 2026-03-07 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `e687d64ce` - Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev'

- 完整 hash: `e687d64ce991449877c284d1ddcedc7cb645c159`
- 时间/作者: 2026-03-07 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `37689613c` - 修复pd分离开启ttft优化首字偶发精度问题 & 修复pd分离decode卡住、精度问题

- 完整 hash: `37689613cf1056185ef795308cc6cb792c1b10ab`
- 时间/作者: 2026-03-11 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `3e822f7ad` - Merge branch 'v0.5.9_dev_pd' into 'v0.5.9_dev'

- 完整 hash: `3e822f7ad0003772608e0b7529e7d347d46d0704`
- 时间/作者: 2026-03-11 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `5db31f4b4` - Merge branch 'cherry-pick-214917d1' into 'v0.5.9_dev'

- 完整 hash: `5db31f4b4642449fdaf6d35a43db94ad24747f66`
- 时间/作者: 2026-03-13 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `8f3e9df94` - Merge branch 'cherry-pick-4d97fa3d-to-059' into 'v0.5.9_dev'

- 完整 hash: `8f3e9df94c6ec255a7e42f55a9b4e85957dc880b`
- 时间/作者: 2026-03-13 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `c64ac4481` - Merge branch 'cherry-pick-0955197e' into 'v0.5.9_dev'

- 完整 hash: `c64ac44818bc201872073f9b581daf3052a754ef`
- 时间/作者: 2026-03-13 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `e850c8d2c` - Merge branch 'v0.5.8_dev_yiqa' into 'v0.5.8_dev'

- 完整 hash: `e850c8d2c590ace3a477b2d4631684e55dc48ebe`
- 时间/作者: 2026-03-13 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `python/sglang/srt/layers/quantization/fp8_kernel.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_kernel.py`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `ee5b7ebb6` - Merge branch 'cherry-pick-e18f065f' into 'v0.5.8_dev'

- 完整 hash: `ee5b7ebb692396eab6b2be1360f0d56fe49c577f`
- 时间/作者: 2026-03-13 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `23fd42261` - Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev'

- 完整 hash: `23fd42261b8a7f5620becaa4bfe80abd651d812b`
- 时间/作者: 2026-03-16 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `c2f921462` - 修复bailing模型大ep无法启动

- 完整 hash: `c2f921462faaf92baecf22d1a23021472fe770b2`
- 时间/作者: 2026-03-16 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `b54acd50f` - Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev'

- 完整 hash: `b54acd50f88ff3dcb0c23f396c83fda0b1f5a462`
- 时间/作者: 2026-03-20 / liucong8560
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `fc5981e07` - bailing模型支持EP模式下开启rms+quant算子融合

- 完整 hash: `fc5981e071f99c0069ac3e6ede6e78b711aa0728`
- 时间/作者: 2026-03-20 / liucong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/bailing_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`
  - runtime-perf: `python/sglang/srt/layers/communicator.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `d34753123` - pd分离p端加上日志

- 完整 hash: `d347531234de2009c6e747b628aea6a4ce469a57`
- 时间/作者: 2026-03-22 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/prefill.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/prefill.py`
- 验证与风险: 涉及调度、缓存、PD 或 MTP 路径；需要验证 prefill/decode 时序、首 token 正确性、并发与长上下文稳定性。

#### Commit `3f30edf9a` - 修复059版本函数名字修改导致的报错

- 完整 hash: `3f30edf9aa05c86075746873066fd50f1e97877c`
- 时间/作者: 2026-03-23 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `79a11f9bb` - Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev'

- 完整 hash: `79a11f9bb063714ebeeeac7f20da617a7cdb26c6`
- 时间/作者: 2026-03-23 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `886fbccec` - Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev'

- 完整 hash: `886fbccec07147749c241985caf3f52ec4acb2fc`
- 时间/作者: 2026-03-23 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `e845e0ead` - Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb

- 完整 hash: `e845e0eadd2d5f636be783ac5a99d1d95d66f29a`
- 时间/作者: 2026-03-26 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_info_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashmla_backend.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`
  - other: `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `2b4435fa5` - fis bug

- 完整 hash: `2b4435fa5a79ae5d0c19e51094018860bd98e786`
- 时间/作者: 2026-03-27 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `48739c3ac` - Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb

- 完整 hash: `48739c3ac64be80745e51a8742523504bc8ef990`
- 时间/作者: 2026-03-30 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `b15505653` - update readme about dcu

- 完整 hash: `b15505653f0a936301786b2570a48209ff21dcd9`
- 时间/作者: 2026-03-30 / lizhigong
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `README_DCU.md`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `f9ea5254d` - add torch version hadamard_transform_optimized()

- 完整 hash: `f9ea5254d79e28a0583e39e01f64f4b546d37310`
- 时间/作者: 2026-03-30 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- 验证与风险: 涉及性能或后端路径；复用前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `70c416ca9` - fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1

- 完整 hash: `70c416ca947cc7ede81a25e216aed255f017ce93`
- 时间/作者: 2026-03-31 / chenyue3
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `c2ffad7df` - 修复开融合算子后传参逻辑

- 完整 hash: `c2ffad7df56d0befafbd449799ab156cbbbfcbcd`
- 时间/作者: 2026-04-01 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `c5eb17125` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- 完整 hash: `c5eb171255d709e18146bdd027308aa71ca71c8c`
- 时间/作者: 2026-03-30 / lizhigong
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py` 等 11 个文件
  - runtime-perf: `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/flashmla_backend.py` 等 69 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - docs-bench: `README_DCU.md`
  - other: `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` 等 32 个文件
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `f9d9b0204` - 解决PD分离报错问题

- 完整 hash: `f9d9b0204997baa59ff4e4af58ad29610109e81f`
- 时间/作者: 2026-03-30 / liucong
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/bailing_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/bailing_moe.py`
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/model_executor/forward_batch_info.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `77a4da53b` - fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1

- 完整 hash: `77a4da53b195948f368d09aca59eeff7a84445b0`
- 时间/作者: 2026-03-31 / chenyue3
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `236c37f41` - 修改环境变量SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING名称为SGLANG_USE_FUSED_RMS_ROTARY

- 完整 hash: `236c37f410e190d19d32aa6e85f312509ac87ea0`
- 时间/作者: 2026-04-01 / chenyue3
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `8edb7c965` - 修复融合算子并验证精度.

- 完整 hash: `8edb7c9650db08be27033956472ebb9247d2eb46`
- 时间/作者: 2026-04-01 / linhai1
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/dcu_mla_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `962c74637` - optimized code of layernorm

- 完整 hash: `962c746378e9db0345c1094fdc83c0610bb0fdbe`
- 时间/作者: 2026-04-01 / chenyue3
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 涉及性能或后端路径；复用前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f2dfc2ec8` - fix split_qkv_rms_rotary_embedding_fuse_with_kv_store_quant算子的使用bug，此bug影响QwQ-32B模型的性能优化

- 完整 hash: `f2dfc2ec8bf1efd51c494afa69dcf2261f47b0d8`
- 时间/作者: 2026-04-01 / chenyue3
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `5bb6dff38` - Update README_DCU.md

- 完整 hash: `5bb6dff38e0a5a5c40362517df95bdbdf53580b3`
- 时间/作者: 2026-04-02 / guobj
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `README_DCU.md`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `70c9a1a6d` - Update README_DCU.md

- 完整 hash: `70c9a1a6dbc01df5faca6eb7775be75e7c43ca2e`
- 时间/作者: 2026-04-02 / guobj
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `README_DCU.md`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `865ca25a7` - Update README_DCU.md

- 完整 hash: `865ca25a7b0b6b5ef7930828bdb57af7b8220ba5`
- 时间/作者: 2026-04-02 / guobj
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `README_DCU.md`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `8d278721f` - Update README_DCU.md

- 完整 hash: `8d278721f069861662a3a08d3a723fb6746152d1`
- 时间/作者: 2026-04-02 / guobj
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `README_DCU.md`
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `4dd71954e` - [bugfix]将使能QWQ-32B性能优化的环境变量SGLANG_USE_FUSED_RMS_ROTARY名称修改为SGLANG_USE_FUSED_SPLIT_QKV_RMS_ROTARY_EMBEDDING，解决因此引起的精度问题

- 完整 hash: `4dd71954e4540e047696b9b3d0d744e86611e654`
- 时间/作者: 2026-04-03 / chenyue3
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `50a63c96d` - fix deepseek log cudagraph init meta data copy error in bmz when capture cudagraph.

- 完整 hash: `50a63c96d8304e6f2ec23819b93680a70a4851ff`
- 时间/作者: 2026-04-07 / lizhigong
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/dcu_mla_backend.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `b4059342f` - 接入causal_conv1d_update优化算子

- 完整 hash: `b4059342f9fc93943d4ef95b81ebfb4ffb73c02c`
- 时间/作者: 2026-04-07 / liucong
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/gdn_backend.py`
- 验证与风险: 涉及调度、缓存、PD 或 MTP 路径；需要验证 prefill/decode 时序、首 token 正确性、并发与长上下文稳定性。

#### Commit `7104fdb72` - 解决FA报错问题

- 完整 hash: `7104fdb72e187f1a30ab158c32d7f4d0518afb10`
- 时间/作者: 2026-04-08 / liucong
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `22e5ac5b1` - Bugfix:fix mm model attention interface

- 完整 hash: `22e5ac5b196dddddbe227be61aa4cb0e75726a0e`
- 时间/作者: 2026-04-09 / liuchy5
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/vision.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `c200c7845` - sglang dcu 0.5.11 base hash(dfb35997)

- 完整 hash: `c200c78458e45487f5b7615d68c0fe4f15fc2b22`
- 时间/作者: 2026-05-06 / lizhigong
- 分支更新段: `v0.5.10_dev..v0.5.11_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py` 等 131 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py` 等 17 个文件
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/fla/chunk.py`; `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`; `python/sglang/srt/layers/attention/fla/fused_recurrent.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - docs-bench: `README_DCU.md`
  - other: `python/pyproject.toml`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py` 等 33 个文件
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `4d897133e` - Supplement merge

- 完整 hash: `4d897133e08212eaa77243fe8b9f4693bb75e0cf`
- 时间/作者: 2026-05-07 / lizhigong
- 分支更新段: `v0.5.10_dev..v0.5.11_dev`
- 自动分类: 通用实现调整
- 主要文件: `python/pyproject.toml`, `python/sglang/srt/model_executor/model_runner.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - other: `python/pyproject.toml`
- 验证与风险: 通用实现调整；需要结合命中文件判断是否影响目标模型的启动、加载或服务行为。

#### Commit `96a5c116a` - fix some error in initial version

- 完整 hash: `96a5c116a377cdafe911274f1eb87e154879557c`
- 时间/作者: 2026-05-07 / lizhigong
- 分支更新段: `v0.5.10_dev..v0.5.11_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`
  - other: `python/sglang/srt/distributed/parallel_state.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `a28aa5f97` - fix some errors when init server

- 完整 hash: `a28aa5f97c936c20bc4e5d77f0d993c606a1b5f0`
- 时间/作者: 2026-04-25 / lizhigong
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/qwen2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/qwen2.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/mxfp4.py`
  - other: `python/sglang/srt/managers/overlap_utils.py`; `python/sglang/srt/model_executor/forward_batch_info.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `eec3b3ff8` - fix for load model

- 完整 hash: `eec3b3ff89bba04cfd7eab0551a85b931b06fa51`
- 时间/作者: 2026-04-27 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: 无直接文件变更/merge
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `6ad2adb52` - [Feature] support rocm moe_fused_gate

- 完整 hash: `6ad2adb5276fb722d8cdfc1092fcdf40746d945e`
- 时间/作者: 2026-04-28 / Zhangzbb
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`, `python/sglang/jit_kernel/utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/add_constant.cuh`; `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`; `python/sglang/jit_kernel/utils.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `50b898285` - fix mhc with tile 0.1.9

- 完整 hash: `50b89828562e31f35fbb3e2a2083256b7dc044b6`
- 时间/作者: 2026-04-29 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/mhc.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/mhc.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `a44cec29b` - fix jit for moe_fused_gate

- 完整 hash: `a44cec29bc25886036fa3c237da7c7283beb78ff`
- 时间/作者: 2026-04-29 / wangaq
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `bb24fa6e1` - [Feature] support rocm moe_fused_gate

- 完整 hash: `bb24fa6e1c303972bfb5455d15f0a46591110552`
- 时间/作者: 2026-04-29 / Zhangzbb
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/warp.cuh`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `fd077165a` - fix the mtp issues of metadata loc size

- 完整 hash: `fd077165adfa5c1f81f6c77e5f290be1cbaea958`
- 时间/作者: 2026-05-14 / YuanYuan
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/speculative/eagle_worker_v2.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `c5dd815b3` - dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6)

- 完整 hash: `c5dd815b3c631b45afa6450eb74f16fee6902428`
- 时间/作者: 2026-05-18 / lizhigong
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 测试/文档/基线合入
- 主要文件: `README_DCU.md`, `python/pyproject.toml`, `python/sglang/bench_serving.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/ring_attention.py` 等 141 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=128,N=192,device_name=BW200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_0_0/E=160,N=320,device_name=BW200.json`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` 等 18 个文件
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/multimodal_gen/runtime/layers/ring_attention.py`; `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py` 等 85 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
  - docs-bench: `README_DCU.md`
  - other: `python/pyproject.toml`; `python/sglang/bench_serving.py`; `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/executors/pipeline_executor.py`; `python/sglang/multimodal_gen/runtime/utils/profiler.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py` 等 36 个文件
- 验证与风险: 基线、合并、测试或文档类提交；主要用于定位分支来源和验证入口，通常不直接作为性能 patch 依据。

#### Commit `411660d35` - feat(diffusion): add ROCm SLA attention backend

- 完整 hash: `411660d351f37b6a859dad55729a457078892e82`
- 时间/作者: 2026-05-21 / zhenggf
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/runtime/platforms/rocm.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`
  - other: `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`; `python/sglang/multimodal_gen/runtime/platforms/rocm.py`
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `f378b1a20` - [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0

- 完整 hash: `f378b1a208dbcd79520abdb38e075ad11d2f09d8`
- 时间/作者: 2026-05-22 / chenyue3
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/unquant.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/quantization/unquant.py`
- 验证与风险: 涉及性能或后端路径；复用前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `18b48e742` - moe-runner-backend支持lightop_moe_w8a8

- 完整 hash: `18b48e742b700bb2c06586c742a4abd480aaf317`
- 时间/作者: 2026-05-28 / yangyn1
- 分支更新段: `v0.5.11_dev..v0.5.12_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/lightop.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/lightop.py`; `python/sglang/srt/layers/moe/moe_runner/runner.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 281（其中 merge 0）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
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
| ... | 另有 305 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
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
| 2026-07-20 | `358a33714` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): keep Harbor build image path | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 |
| 2026-07-20 | `81e3561ae` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci(hcu): exclude two unstable PR tests | `.github/workflows/pr-test-hcu.yml` |
| 2026-07-20 | `811aa027d` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: replace HCU runtime text check with sensitive diff gate | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_hcu_runtime_text.py`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-20 | `15a656ea6` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | test(hcu): align v0.5.15 compatibility tests | `test/registered/hcu/openai_server/test_serving_chat_hcu.py`, `test/registered/hcu/unit/test_profile_merger_hcu.py`, `test/registered/unit/server_args/test_server_args.py` |
| 2026-07-21 | `9864c8451` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: use shared sensitive diff gate for HCU port | `.github/workflows/quality-gate.yml`, `scripts/ci/hcu/check_sensitive_diff_text.py` |
| 2026-07-21 | `ac56ca009` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: follow main sensitive diff workflow | `.github/workflows/quality-gate.yml` |
| 2026-07-22 | `9fc04a7a2` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] Disable the standalone-DCU MegaMoE ASM tail-reduce path by default to avoid vmfault | `python/sglang/srt/layers/moe/mega_moe.py` |
| 2026-07-24 | `7482123c3` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-27 | `0710e82a0` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow for new branch version | `.github/workflows/quality-gate.yml` |
| 2026-07-28 | `997e64560` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 4 个文件 |
| 2026-07-29 | `3b4327cd7` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(hcu): support current LightOp fp8 quant API | `python/sglang/srt/layers/linear.py` |
| 2026-07-29 | `e18e6b94b` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | docs(hcu): record daily forward-port 20260729 | `docs/internal/dcu-main-conflict-ledger.md` |
| 2026-07-29 | `111fea82f` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 36 个文件 |
| 2026-07-31 | `02968a96d` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore shared wheel staging root lost in forward-port | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 4 个文件 |
| 2026-07-31 | `39d691220` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore NETWORK_MODE default lost in forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-08-03 | `286612da4` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to use version v2.0.0 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `de696eab9` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to version 2.0.1 | `.github/workflows/quality-gate.yml` |
| 2026-08-03 | `015f6d49a` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: drop redundant module-scope sgl_kernel import in forward_batch_info | `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-08-06 | `f1c6f5631` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix(hcu): drop leftover source hunks that renaming and partial takes left behind | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` |
| 2026-08-06 | `8e2aba4bf` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: apply isort/black to forward-port diff | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8.py` 等 5 个文件 |
| 2026-08-06 | `f17440f19` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore original license headers dropped by the forward-port | `scripts/ci/hcu/hcu_ci_start_container.sh`, `test/run_suite.py` |
| 2026-08-06 | `b0f2bb3a8` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): restore network_mode matrix keys dropped by the forward-port | `.github/workflows/nightly-test-hcu.yml` |
| 2026-08-07 | `154a88c7b` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: apply isort/black to the lmslim->lightop migration | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` |
| 2026-08-07 | `b59995e42` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | fix(hcu): point PD smoke tests at a declared HCU suite | `test/registered/hcu/README.md`, `test/registered/hcu/disaggregation/test_pd_environment_hcu.py`, `test/registered/hcu/disaggregation/test_pd_hcu_utils.py` |
| 2026-08-07 | `92ce544fa` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci: align v0.5.15 workflow triggers | `.github/workflows/bot-bump-docs-version.yml`, `.github/workflows/release-docker-amd.yml`, `.github/workflows/release-docker-npu.yml` 等 7 个文件 |
| 2026-08-07 | `132b630bc` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci(hcu): harden server lifecycle and model mounts | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `python/sglang/test/hcu_cookbook_utils.py` 等 5 个文件 |
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
| 2026-08-12 | `fb7f11956` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | ci(hcu): adapt wheel jobs to CIUpload 0.3 | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 |
| 2026-08-13 | `54e3ed50f` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | [BugFix] fix the runtime errors in ep+dspark mode | `python/sglang/srt/speculative/dspark_components/dspark_draft.py` |
| 2026-08-13 | `18e167b73` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] fix the client inference None errors in temperature>0 with a torch implementation | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-13 | `5e2ba659e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: apply pre-commit fixes to the dspark bugfixes | `python/sglang/srt/speculative/dflash_utils.py` |
| 2026-08-31 | `93b801826` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` |
| 2026-09-21 | `c8ba30447` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-07-24 | `6c1786bc4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): prefer hcusmi for platform detection | `python/sglang/multimodal_gen/runtime/platforms/__init__.py` |
| 2026-07-27 | `93c56ce71` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Refactor quality gate workflow and job configurations | `.github/workflows/quality-gate.yml` |
| 2026-07-28 | `77939d9a5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci: use configured HCU release image | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-07-29 | `b2f0b830c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | ci: disable unused workflow triggers | `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/ci-coverage-overview.yml` 等 39 个文件 |
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
| 2026-08-13 | `ccfc91c5d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(attention): 保留 IFB/MTP 的 DSA effective forward mode | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/forward_batch_utils.py`, `python/sglang/srt/layers/attention/dsa/utils.py` 等 5 个文件 |
| 2026-08-13 | `75cc77fa2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): 修复 IFB/MTP FlashMLA padded rows | `python/sglang/srt/layers/attention/dsa/forward_batch_utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_forward_batch_utils.py` |
| 2026-08-13 | `902de5d3d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): 修复 HCU DSA FlashMLA metadata replay | `python/sglang/srt/layers/attention/dsa/flashmla_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_flashmla_backend.py` |
| 2026-08-13 | `18b106418` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | feat(attention): 恢复 HCU LightOp DSA indexer 路径 | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/paged_mqa_logits_backend.py`, `python/sglang/srt/server_args.py` 等 4 个文件 |
| 2026-08-13 | `0dd9ab211` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(attention): 按 head_dim 归一化 DSA indexer | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `test/registered/unit/layers/attention/dsa/test_hcu_indexer.py` |
| 2026-08-13 | `43f1a8b2a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(attention): 启用 HCU DSA MTP draft-extend CUDA graph | `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/spec/test_eagle_worker_v2_graph_support.py` |
| 2026-08-14 | `fa309a1e1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): drop the stale 0.5.12-era expert-count override in FusedMoE | `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-08-14 | `288ab2445` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: fix submit_nogds_read failed when use fastsafetensors load | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-08-14 | `1535858ca` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: refactor mxfp4 moe for activate 8 or 16 bit | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 4 个文件 |
| 2026-08-15 | `3190629e7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: correct blockshape is none when use aiter moe for channel w4a8 model | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-17 | `9bbf3799d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | docs(hcu): add the 20260817 official backport validation report | `docs/internal/backport-official-20260817-validation-report.md` |
| 2026-08-18 | `b0dc28040` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Hcu/fix main kernel build path (#207) | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/nightly-test-hcu.yml` 等 9 个文件 |
| 2026-08-18 | `e3a192d66` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: update kda default value and support boltops chunk delta rule | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py` 等 4 个文件 |
| 2026-08-19 | `ef56737fc` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: update w4a8 moe default backend | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-19 | `45d26d754` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(kernel): add HCU MLA query concat kernel | `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/concat_mla_absorb_q_hcu.cu` 等 7 个文件 |
| 2026-08-19 | `1653683bd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): port sparse page MQA with mask TopK to DSA | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_metadata.py` 等 5 个文件 |
| 2026-08-19 | `f475e6569` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(dsa): compact shared index-K cache | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/utils.py` 等 8 个文件 |
| 2026-08-19 | `a306b8023` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(hcu): port gfx936 INT8 DSA index cache | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/hcu_int8_index_k_cache.py` 等 7 个文件 |
| 2026-08-19 | `f41bb0f58` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(hcu): support INT8 DSA cache in Mooncake PD | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/utils.py` 等 8 个文件 |
| 2026-08-19 | `3d12a3ce1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): stabilize DSA MTP metadata replay | `python/sglang/kernels/jit/csrc/elementwise/fused_metadata_copy.cuh`, `python/sglang/kernels/ops/attention/fused_metadata_copy.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py` 等 4 个文件 |
| 2026-08-19 | `51e53affe` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): reuse DSA target verify graph metadata | `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py` |
| 2026-08-19 | `873465654` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): correct compact index cache handling | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` 等 10 个文件 |
| 2026-08-19 | `6a51f2a38` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): register SlimQuant W4A8 Marlin quantization | `python/sglang/srt/server_args.py` |
| 2026-08-19 | `afe5219d0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(scheduler): use parallel state for PD decode sync | `python/sglang/srt/managers/scheduler.py` |
| 2026-08-19 | `0d243f4f1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): restore async metadata copies and padded dispatch | `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/moe/test_topk_padded_region.py` |
| 2026-08-19 | `ed017ea38` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): use LayerSplit scratch for fused index writes | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/index_key_cache.py` 等 4 个文件 |
| 2026-08-20 | `62a07586d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat] 适配HCU FA3 | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 5 个文件 |
| 2026-08-20 | `fb7369fec` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix]删除无关文件 | `python/sglang/srt/layers/rotary_embedding/base.py.bak-20260806-145942` |
| 2026-08-20 | `b628d29e1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | [feature] 增加打镜像的ci, 0.5.15版本更新torch到2.11版本 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-20 | `11d08002b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` 等 4 个文件 |
| 2026-08-20 | `f6b66222a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | revert: 恢复 release-pr-hcu.yml 默认 torch 版本为 2.10.0 | `.github/workflows/release-pr-hcu.yml` |
| 2026-08-20 | `72d1d2a73` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix]solved other CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `27ce43c71` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix]solved CI Test errors | `python/sglang/srt/layers/attention/flashattention_interface.py` |
| 2026-08-20 | `37c5b30bb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: extract full DTK version for three-part versions | `.github/workflows/nightly-test-dcu.yml`, `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-dcu.yml` 等 4 个文件 |
| 2026-08-20 | `a6a8e0d5d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: read MXFP4 group_size from model config instead of hardcoding 32 | `python/sglang/srt/layers/quantization/mxfp4.py` |
| 2026-08-20 | `650a58304` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): skip padded tokens for legacy DeepGEMM MoE | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-20 | `b001a8d21` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): reduce TopK and DSA replay overhead | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` |
| 2026-08-20 | `dcbfd4230` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): avoid redundant padded weight mask | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-20 | `9e3dd4834` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): fuse DeepEP topk id cast | `python/sglang/srt/layers/moe/topk.py` |
| 2026-08-20 | `5aedbbcc9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): overlap LayerSplit index cache broadcast | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` 等 5 个文件 |
| 2026-08-24 | `261b8627f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): restore 29 environ declarations the sync auto-merge dropped | `docs/internal/dcu-main-conflict-ledger.md`, `docs/internal/sync-official-main-20260824-summary.md`, `python/sglang/srt/environ.py` |
| 2026-08-24 | `238c81b4c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 优化因数据拷贝导致的性能问题 | `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py`, `python/sglang/srt/hardware_backend/npu/moe/matmul.py` |
| 2026-08-24 | `6e2f11552` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): align speculative index cache lengths | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` |
| 2026-08-25 | `c40703e6b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(ci): clear the three Quality Gate blockers from the 20260824 sync | `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml` 等 5 个文件 |
| 2026-08-25 | `59213c7e4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Revert the hcu_rename_allowlist entry for -DCUDA_ENABLED | `scripts/ci/hcu/hcu_rename_allowlist.txt` |
| 2026-08-25 | `69c73a178` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | ci(hcu): support fork pull requests | `.github/workflows/lint-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `f2fc4e166` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | Update quality gate workflow to version 2.0.3 | `.github/workflows/quality-gate.yml` |
| 2026-08-25 | `3e6aaf09d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): allow fork checkout in target workflows | `.github/workflows/lint-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `6a4a61efb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | ci(hcu): detect runner workspace ownership | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-25 | `b921d697a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support contiguous and masked hipc kernel for deepep normal and low_latency mode | `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` 等 4 个文件 |
| 2026-08-25 | `7164456e7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: preserve target lightop int8 quantization | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` |
| 2026-08-26 | `8b50a269f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | bugfix router路径不对 | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `d5882c133` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | [feature] 发包流水支持手动触发,手动触发不上传pypi | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `038467e8b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix lightop moe align vimfault | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-26 | `6ba4328e9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): release 发包流水触发方式改为 push | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `93c930c6f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix aiter shuffle func not found | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-26 | `d8db8bb3e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): complete LayerSplit HiCache paths | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` 等 11 个文件 |
| 2026-08-26 | `5efbf9c3b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | debug: gateway 构建加日志排查 wheel 路径，临时只编 router | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `0669c1842` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(quantization): defer SlimQuant MoE backend resolution | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-26 | `63610c2ff` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): enable checks for release branches | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/quality-gate.yml` |
| 2026-08-26 | `d39c77a23` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): use bash for wheel build jobs | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-26 | `1db0108f3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [CI bugfix]工作目录没有清理导致权限变root (#240) | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-26 | `b57ecddf2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): fix W4A8 DeepEP accuracy with SwiGLU clamp | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `f292fa0e3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): trust wheel build workspaces | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-08-27 | `779f1bea2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix] CI打包版本更新为0.5.18 (#244) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-08-27 | `1679428e0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [FEAT][DSpark] 1. Support the p/d radix cache w/ DSpark by PR:https://github.com/sgl-project/sglang/pull/31097; 2. SGLANG_ENABLE_UNIFIED_RADIX_TREE=1 & SGLANG_ENABLE_UNIFIED_RADIX_TREE=1 & --disaggregation-decode-enable-radix-cache should be enable in D | `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` 等 14 个文件 |
| 2026-08-27 | `6721affc2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | [feature]适配hcu发包 | `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml` |
| 2026-08-27 | `dc1b54b42` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): tolerate deepgemm without contiguous HIPC kernel | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `b065e598a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): restore slimquant backend logger | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-27 | `962ab75e4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): default to compatible masked W4A8 kernel | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `253e326c3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(disagg): avoid duplicate KV transfer in worker | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-08-27 | `42185e316` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): apply SwiGLU clamp in contiguous W4A8 path | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-08-27 | `e769cde2e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | hcu ci: docker 镜像 daily 定时构建, router 改用 vendored openssl, 补装 flash_kda (#252) | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 |
| 2026-08-28 | `5f314b004` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dspark): transfer draft KV from PD prefill | `python/sglang/srt/speculative/dspark_components/dspark_disaggregation.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py` |
| 2026-08-28 | `31a159567` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: use the model's MoE topk for DeepEP RDMA buffer sizing | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-08-28 | `845f99085` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(spec): handle zero-token verify results | `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py` |
| 2026-08-28 | `c3846f222` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): consume INT8 DSA index cache directly | `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/hcu_int8_index_k_cache.py` |
| 2026-08-29 | `bf037e528` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hicache): synchronize L3 prefetch across PP ranks | `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hicache_storage.py` 等 11 个文件 |
| 2026-08-31 | `bf9245607` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` |
| 2026-09-01 | `685051c47` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix] removed the http warning info in the skip-warmup mode (#276) | `python/sglang/srt/entrypoints/http_server.py` |
| 2026-09-01 | `867eeada1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: gracefully handle unsupported KV cache schemes (#268) | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-09-01 | `8ae13700d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): port PD disaggregation accuracy fix to v0.5.18 release (#266) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` 等 5 个文件 |
| 2026-09-02 | `6614bebc7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): add BHSD KV-cache support while preserving legacy HCU FA (#282) | `docker/hcu.Dockerfile`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` 等 11 个文件 |
| 2026-09-02 | `4fea017b1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): sample linear MTP target verification (#280) | `python/sglang/srt/speculative/eagle_utils.py` |
| 2026-09-02 | `0e2a6e743` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Feat/bolt recompute w u (#278) | `python/sglang/kernels/ops/attention/fla/wy_fast.py` |
| 2026-09-02 | `556337109` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]:用lightop的gemm_w8a8_smooth代替triton实现，提升性能 (#279) | `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py` 等 4 个文件 |
| 2026-09-02 | `0ce4bc716` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [CI] Use v0.5.18 HCU image and update model paths (#287) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `README_HCU.md` 等 12 个文件 |
| 2026-09-02 | `3b678f293` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BUGFIX] HCU环境不需要依赖flashinfer (#289) | `python/pyproject_hcu.toml` |
| 2026-09-03 | `ab91a15c8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix] 1.fix the accuracy issue in Decode radix-cache enable due to… (#291) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/mem_cache/common.py` |
| 2026-09-03 | `2a1b589b3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): support BSHD multi-batch varlen attention and PD disaggregation (#288) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` |
| 2026-09-03 | `b0f501598` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] fix the bug that certain chat/completion in DSpark goes to C… (#294) | `python/sglang/kernels/ops/speculative/dspark/dspark_accept.py` |
| 2026-09-03 | `f656a2ed2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] fix the bug by removing old monkey patch of mhc (#296) | `python/sglang/kernels/ops/layernorm/mhc.py` |
| 2026-09-03 | `2b855b5be` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | ci(hcu): align llguidance and model asset paths (#300) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` |
| 2026-09-03 | `20c5f927f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [BugFix] Remove the dependency of prefill radix-cache with decode-pre… (#302) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py` 等 5 个文件 |
| 2026-09-04 | `9153913d6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(speculative): remove unsupported server args (#304) | `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2026-09-04 | `f35668e41` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [perf] add opt-in LightOp KV allocation kernel (#307) | `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/allocator/paged.py` |
| 2026-09-04 | `4c9d666cd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: fix deepep and dspark conflict (#306) | `python/sglang/srt/arg_groups/speculative_hook.py` |
| 2026-09-04 | `44b7bc846` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [BugFix] support the MegaMoE func in DSpark model (#309) | `python/sglang/srt/layers/moe/mega_moe.py` |
| 2026-09-07 | `3bc09034b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | feat(bench): add --gsp-input-ids to skip server tokenization (#315) | `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` |
| 2026-09-07 | `cdea7a5db` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): use available RMSNorm kernel op (#321) | `python/sglang/srt/layers/layernorm.py` |
| 2026-09-07 | `ba2dec637` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(fst): reclaim device cache after each weight batch (#322) | `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-09-08 | `056b21d82` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | opt: optimize situ_quant op form lightop lib (#324) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-08 | `47b97c0f7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): avoid gfx936 QSA LDS overflow (#326) | `python/sglang/srt/layers/attention/qsa/sparse_attn.py` |
| 2026-09-08 | `57beb6b4a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | ci(hcu): align PR wheel version with release 0.5.18 (#295) | `.github/workflows/release-pr-hcu.yml`, `README_HCU.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py` 等 9 个文件 |
| 2026-09-09 | `e6540308c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix bug: Refactor is_fp8_fnuz function for clarity | `python/sglang/kernels/ops/quantization/fp8_kernel.py` |
| 2026-09-09 | `b10bb8c6e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [FEAT] support the dspark megamoe-int4 by packing signed-int4 to int8 (#333) | `python/sglang/srt/layers/moe/hcu_int4_megamoe.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py` 等 5 个文件 |
| 2026-09-10 | `6d5931922` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | test(hcu): derive FP8 quant reference bounds from the output dtype (#337) | `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` |
| 2026-09-10 | `ebe9c77f2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | [FEATURE]同步编译python3.10和python3.12, 上传whl包后记录信息至dashub (#338) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-10 | `a494caa1e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): use AITER IPC collectives for DP TP-MoE (#340) | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/dp_attention.py` |
| 2026-09-10 | `4cdd9d36e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Release/20260825 v0.5.18 (#339) | `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py` |
| 2026-09-11 | `77ba00139` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: fix pd fake prefill mode and attn_tp_size bug (#345) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-09-12 | `fa95ae084` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix and opt: fix dspark eagle error and optimize attn tp comm from ai… (#342) | `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py` |
| 2026-09-12 | `647229c6e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): pin v0.5.18 image fallback and shared eval wheels (#348) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` |
| 2026-09-14 | `4a7532fef` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): keep DFLASH FP8 sliding attention on native FlashAttention (#356) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_native_swa.py`, `test/manual/test_hcu_native_swa.py` |
| 2026-09-14 | `74ee9054e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | ci(hcu): fix v0.5.18 PR runtime consistency (#363) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/sampling/test_pytorch_sampling_backend.py` |
| 2026-09-14 | `5077850b7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | support fabric aiter custom allreduce (#361) | `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py` 等 5 个文件 |
| 2026-09-14 | `72df69c80` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [BUGFIX]缺少token声明导致打包信息无法推送至Dashub (#366) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-15 | `86cdce034` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | ci(hcu): align v0.5.18 wheel builds with torch 2.11 (#368) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-09-15 | `45b20a85c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Fix ValueError: Add type annotations to fuse_situ_mul_quant_ep (#369) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-15 | `7c7da44a7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | ci(hcu): fix stale v0.5.18 PR test paths (#370) | `.github/workflows/pr-test-hcu.yml` |
| 2026-09-15 | `35d915ef2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | feat: support hy4 cp (#358) | `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/hunyuan_v4.py` |
| 2026-09-15 | `0f88700ac` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | feat(mem-cache): support direct L3 external linker cache without test file (#373) | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py` 等 31 个文件 |
| 2026-09-16 | `b80d0d1bb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [fix] 修复w8a8-fp8-v4pro精度问题 (#380) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-16 | `7df099eb6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(moe): 增加 EP 绝对均衡性能测试开关 (#383) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_balance.py`, `python/sglang/srt/layers/moe/hash_topk.py` 等 4 个文件 |
| 2026-09-16 | `2bb5e81e5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | feat(spec): 支持节点内 Draft LM-head 词表并行 (#385) | `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 6 个文件 |
| 2026-09-17 | `07214443b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(qsa): use FA sparse GQA for HIP chunk-prefill extend (#392) | `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` |
| 2026-09-17 | `2df70449a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | feat(layersplit): 支持单层 MTP Draft KV 分片与缓存复用 (#387) | `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` 等 10 个文件 |
| 2026-09-17 | `7db5ec177` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(lplb): 支持 HIP 静态 LP 副本概率分发 (#386) | `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `python/sglang/kernels/jit/csrc/lplb/dispatch_probability.cuh` 等 10 个文件 |
| 2026-09-17 | `c4ef6d3a4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): 修复 MQA 显存预算与 CP/MTP 索引补齐 (#382) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py` |
| 2026-09-17 | `eb4f0ad89` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]适配 w4a8-int8-megamoe (#394) | `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-09-20 | `16e9b3867` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): support BF16 KV for Qwen DFLASH2 attention (#405) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/manual/test_hcu_dflash_native_block16.py` |
| 2026-09-20 | `ccc15a6f3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(cache): integrate Mooncake ReadPlan and optimize page-wise loading for direct linker (#404) | `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` 等 6 个文件 |
| 2026-09-20 | `98ba405a2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(aiter): w13 权重 shuffle 改回 gemm2 布局，修复 w8a8 变体乱码 (#401) | `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-09-20 | `05c58e82f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(dsa): 修复 gfx938 72CU sparse MQA 路由与 HCU 判断 (#409) | `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/attention/dsa_backend.py` |
| 2026-09-22 | `50beda6a9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-09-23 | `31262cd68` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix deepep num_rdma_bytes count correct (#437) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-09-23 | `90f80c6bd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(moe): 增加 aiter moe_c 后端选定环境变量 (#415) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` |
| 2026-09-23 | `6c0330d8d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(w4a8): 修复 HIPC MoE scale 重复乘 16 与 HCU RoPE 启动越界 (#439) | `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` 等 4 个文件 |
| 2026-09-23 | `2f93be6c5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(kvcache): handle zero full iterations for asymmetric KV cache (#425) | `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh` |
| 2026-09-23 | `066a95af7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix lightop situ import regression bug and deepgemm w4a8 op interface change (#428) | `python/sglang/srt/layers/moe/ep_moe/layer.py` |
| 2026-09-30 | `6086af28d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | ci(hcu): migrate v0.5.18 workflows to organization runners (#465) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` 等 11 个文件 |
| 2026-09-30 | `1828115e0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix w4a16 moe asm error (#462) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py` |
| 2026-09-30 | `3854f7754` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | opt(kda): update kda verify decode op from boltops (#458) | `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` |
| 2026-09-30 | `e885e7223` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): restore ForwardBatch RMS quantization flag (#469) | `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_forward_batch_hcu_state.py` |
| 2026-10-08 | `cfa865d33` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix deepgemm masked fp8 api upstream (#472) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-10-08 | `b7e4eae12` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix: remove alt_stream overlap copy when writing KV cache (#478) | `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-10-08 | `7fa7729c1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(cache): harden Mooncake ReadPlan and PP direct-L3 cache loading (#482) | `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py` 等 27 个文件 |
| 2026-10-09 | `2cc1bcc28` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(deepgemm): 统一 INT8/FP8 权重重排与 FP8 masked GEMM 接口 (#484) | `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 6 个文件 |
| 2026-10-09 | `a06c34ef7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(ci): stage-b include 列表容忍分支差异的测试文件 (#485) | `.github/workflows/pr-test-hcu.yml` |
| 2026-10-09 | `6ca7a1bd6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(test): 修复 unified attention 单测 KV 索引构造 (#489) | `test/registered/attention/test_triton_attention_kernels.py` |
| 2026-10-09 | `1882acd8c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): restore DeepEP normal combine for HCU groupgemm (#491) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` |
| 2026-10-09 | `bfbff7f68` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): preserve INT8 MoE fallback and restore AITER W8A8 compatibility (#487) | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 7 个文件 |
| 2026-10-10 | `966f6da1b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): avoid double packing channel FP8 DeepGEMM weights (#497) | `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py` |
| 2026-10-10 | `e1eaf0829` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(moe): guard SBO setup for flat DeepEP dispatch (#501) | `python/sglang/srt/batch_overlap/single_batch_overlap.py` |
| 2026-10-10 | `f106c5360` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf(hcu): 优化小 batch W8A8 INT8 GEMM 的 Tiling 选择 (#502) | `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py` |
| 2026-10-12 | `49bb75c79` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(diffusion): upload all video outputs to cloud storage | `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py` |
| 2026-10-12 | `aebf1a9f4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): fix SlimQuant INT8 DeepEP routing and DeepGEMM weight packing (#514) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |
| 2026-10-13 | `018e5799a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Fix/hcu aiter moe inplace (#517) | `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/models/qwen2_moe.py` |
| 2026-10-13 | `71b2ee4ea` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf: add opt-in asynchronous prebuilt token H2D (#516) | `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/environ.py` 等 4 个文件 |
| 2026-10-13 | `9dd4e2e80` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [diffusion] attention: fix HCU Wan SLA and FA family admission (#519) | `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py` 等 7 个文件 |
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

### 逐 Commit 审计卡

- 时间线列出全部 281 个提交；审计卡只保留最近的 80 个。

#### Commit `9153913d6` - fix(speculative): remove unsupported server args (#304)

- 完整 hash: `9153913d619d31597b77c205453eadb5d2f355f1`
- 时间/作者: 2026-09-04 / Wenbo Zhu
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f35668e41` - [perf] add opt-in LightOp KV allocation kernel (#307)

- 完整 hash: `f35668e41c964583e7b0e0761f311c2893d31b9d`
- 时间/作者: 2026-09-04 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/allocator/paged.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/mem_cache/allocator/paged.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4c9d666cd` - fix: fix deepep and dspark conflict (#306)

- 完整 hash: `4c9d666cd36e3aafa5c584f7ff0188877460bb1d`
- 时间/作者: 2026-09-04 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/arg_groups/speculative_hook.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/speculative_hook.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `44b7bc846` - [BugFix] support the MegaMoE func in DSpark model (#309)

- 完整 hash: `44b7bc84619f5a87c239a586ef7fe10cdab0abf4`
- 时间/作者: 2026-09-04 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/mega_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `3bc09034b` - feat(bench): add --gsp-input-ids to skip server tokenization (#315)

- 完整 hash: `3bc09034bad8c7679d3eaaa3772669c6126ebcc5`
- 时间/作者: 2026-09-07 / chaoyujiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `cdea7a5db` - fix(hcu): use available RMSNorm kernel op (#321)

- 完整 hash: `cdea7a5dbb96b24f80d6330e53c06000ace56e65`
- 时间/作者: 2026-09-07 / Wenbo Zhu
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/layernorm.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/layernorm.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `ba2dec637` - fix(fst): reclaim device cache after each weight batch (#322)

- 完整 hash: `ba2dec637cc60db20a61f27f5ea04daa61db8e51`
- 时间/作者: 2026-09-07 / lzb16
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/model_loader/weight_utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/model_loader/weight_utils.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `056b21d82` - opt: optimize situ_quant op form lightop lib (#324)

- 完整 hash: `056b21d829f1408d184fc411e1155c7be9d5fa10`
- 时间/作者: 2026-09-08 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `47b97c0f7` - fix(hcu): avoid gfx936 QSA LDS overflow (#326)

- 完整 hash: `47b97c0f77e08a5b2287a5f6d0330dec5ccab090`
- 时间/作者: 2026-09-08 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `57beb6b4a` - ci(hcu): align PR wheel version with release 0.5.18 (#295)

- 完整 hash: `57beb6b4ae453725e0c02b58bb5b3d93d737aa4a`
- 时间/作者: 2026-09-08 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/release-pr-hcu.yml`, `README_HCU.md`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/server_args.py`, `requirements_hcu.txt`, `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
  - other: `README_HCU.md`; `python/sglang/srt/arg_groups/overrides.py`; `requirements_hcu.txt`; `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/hcu_ci_start_container.sh`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/kernels/ops/quantization/fp8_kernel.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `e6540308c` - fix bug: Refactor is_fp8_fnuz function for clarity

- 完整 hash: `e6540308c53b7099feb893050d56c1793a3962f1`
- 时间/作者: 2026-09-09 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/quantization/fp8_kernel.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/quantization/fp8_kernel.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b10bb8c6e` - [FEAT] support the dspark megamoe-int4 by packing signed-int4 to int8 (#333)

- 完整 hash: `b10bb8c6eb52cceb55647620d7e0e9e4e711dc3d`
- 时间/作者: 2026-09-09 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/hcu_int4_megamoe.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/mem_cache/common.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/hcu_int4_megamoe.py`; `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`; `python/sglang/srt/mem_cache/common.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `6d5931922` - test(hcu): derive FP8 quant reference bounds from the output dtype (#337)

- 完整 hash: `6d59319229dbc44db4ed7a13a1af8ffda67d14f2`
- 时间/作者: 2026-09-10 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `ebe9c77f2` - [FEATURE]同步编译python3.10和python3.12, 上传whl包后记录信息至dashub (#338)

- 完整 hash: `ebe9c77f2189d2e0982deb37a88a1f323dda191c`
- 时间/作者: 2026-09-10 / Crowder13
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a494caa1e` - perf(hcu): use AITER IPC collectives for DP TP-MoE (#340)

- 完整 hash: `a494caa1e7974a8ec960c526838f476fd93312c8`
- 时间/作者: 2026-09-10 / Yongqiang Duan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/dp_attention.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/dp_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4cdd9d36e` - Release/20260825 v0.5.18 (#339)

- 完整 hash: `4cdd9d36e79a61e736bc6712916a23617919fbfa`
- 时间/作者: 2026-09-10 / wufan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/npu_kernels/npu_quant_matmul_w8a8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `77ba00139` - fix: fix pd fake prefill mode and attn_tp_size bug (#345)

- 完整 hash: `77ba00139ac13b8a6bdb9ee15554cd9c18537fbc`
- 时间/作者: 2026-09-11 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `fa95ae084` - fix and opt: fix dspark eagle error and optimize attn tp comm from ai… (#342)

- 完整 hash: `fa95ae0846a943f9a740c56a3dee4d42279d4728`
- 时间/作者: 2026-09-12 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/dp_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `647229c6e` - ci(hcu): pin v0.5.18 image fallback and shared eval wheels (#348)

- 完整 hash: `647229c6e5adaf3f2dda3515671a48c45f58f825`
- 时间/作者: 2026-09-12 / dingxinlong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `4a7532fef` - fix(hcu): keep DFLASH FP8 sliding attention on native FlashAttention (#356)

- 完整 hash: `4a7532fefd86c6a5f0089a3b6b40eeb1f3ed2119`
- 时间/作者: 2026-09-14 / chenyuege
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/hcu_native_swa.py`, `test/manual/test_hcu_native_swa.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/hcu_native_swa.py`
  - tests: `test/manual/test_hcu_native_swa.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `74ee9054e` - ci(hcu): fix v0.5.18 PR runtime consistency (#363)

- 完整 hash: `74ee9054e84ccb9c33007e5726a93d16b248ea37`
- 时间/作者: 2026-09-14 / dingxinlong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/sampling/test_pytorch_sampling_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
  - tests: `test/registered/sampling/test_pytorch_sampling_backend.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `5077850b7` - support fabric aiter custom allreduce (#361)

- 完整 hash: `5077850b7b646483abe7bd2856ff79d5062ff335`
- 时间/作者: 2026-09-14 / jiafei96
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/hcu_cookbook_utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/bootstrap.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `72df69c80` - [BUGFIX]缺少token声明导致打包信息无法推送至Dashub (#366)

- 完整 hash: `72df69c8087c51d4ed237c219836a1d0df4d274e`
- 时间/作者: 2026-09-14 / Crowder13
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `86cdce034` - ci(hcu): align v0.5.18 wheel builds with torch 2.11 (#368)

- 完整 hash: `86cdce034cbf09a90b7a2a3328174d09634a660e`
- 时间/作者: 2026-09-15 / dingxinlong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `45b20a85c` - Fix ValueError: Add type annotations to fuse_situ_mul_quant_ep (#369)

- 完整 hash: `45b20a85cb28b0f3cbdb71c3d5ca233c8cb63901`
- 时间/作者: 2026-09-15 / Wenbo Zhu
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `7c7da44a7` - ci(hcu): fix stale v0.5.18 PR test paths (#370)

- 完整 hash: `7c7da44a797df5bb370a1789ab7f0aeef55b5530`
- 时间/作者: 2026-09-15 / dingxinlong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `35d915ef2` - feat: support hy4 cp (#358)

- 完整 hash: `35d915ef222de3b2839bb55c1afa9c99e3a24941`
- 时间/作者: 2026-09-15 / Fafap131
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/hunyuan_v4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/hunyuan_v4.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `0f88700ac` - feat(mem-cache): support direct L3 external linker cache without test file (#373)

- 完整 hash: `0f88700ac87668fe19d35f214773ea827a049a8c`
- 时间/作者: 2026-09-15 / xinleishang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` 等 31 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`
  - runtime-model: `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/base_spec_worker.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/base_prefix_cache.py`; `python/sglang/srt/mem_cache/hicache_storage.py`; `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`; `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`; `python/sglang/srt/mem_cache/kv_cache_builder.py`; `python/sglang/srt/mem_cache/kv_cache_configurator.py`; `python/sglang/srt/mem_cache/registry.py` 等 23 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b80d0d1bb` - [fix] 修复w8a8-fp8-v4pro精度问题 (#380)

- 完整 hash: `b80d0d1bb6a942853b242ecc38ef3be3db2575d2`
- 时间/作者: 2026-09-16 / yangyn
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `7df099eb6` - feat(moe): 增加 EP 绝对均衡性能测试开关 (#383)

- 完整 hash: `7df099eb6085eddb781531719bc2af24ff3cf204`
- 时间/作者: 2026-09-16 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_balance.py`, `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_balance.py`; `python/sglang/srt/layers/moe/hash_topk.py`; `python/sglang/srt/layers/moe/topk.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2bb5e81e5` - feat(spec): 支持节点内 Draft LM-head 词表并行 (#385)

- 完整 hash: `2bb5e81e5353c5bc40594d42bd80366b91af15bb`
- 时间/作者: 2026-09-16 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/draft_lm_head_vp.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/speculative/draft_lm_head_vp.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `07214443b` - feat(qsa): use FA sparse GQA for HIP chunk-prefill extend (#392)

- 完整 hash: `07214443be3c398eab3f874df214cbadf256ae03`
- 时间/作者: 2026-09-17 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2df70449a` - feat(layersplit): 支持单层 MTP Draft KV 分片与缓存复用 (#387)

- 完整 hash: `2df70449a7a99196cb2a9497c5f59e57dd556aca`
- 时间/作者: 2026-09-17 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/pool_host/dsa.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/models/deepseek_nextn.py` 等 10 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/cp/utils.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/speculative/base_spec_worker.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`; `python/sglang/srt/mem_cache/kv_cache_configurator.py`; `python/sglang/srt/mem_cache/pool_host/dsa.py`; `python/sglang/srt/mem_cache/pool_host/mla.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `7db5ec177` - feat(lplb): 支持 HIP 静态 LP 副本概率分发 (#386)

- 完整 hash: `7db5ec1771b90e54071f21394cb3df502af98880`
- 时间/作者: 2026-09-17 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `python/sglang/kernels/jit/csrc/lplb/dispatch_probability.cuh`, `python/sglang/kernels/jit/csrc/lplb/platform.cuh`, `python/sglang/kernels/ops/lplb/cuda_solver.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/lplb_solver.py` 等 10 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `benchmark/eplb/README.md`; `benchmark/eplb/prepare_static_lp.py`
  - other: `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/expert_location.py`; `python/sglang/srt/eplb/lplb_solver.py`
  - runtime-perf: `python/sglang/kernels/jit/csrc/lplb/dispatch_probability.cuh`; `python/sglang/kernels/jit/csrc/lplb/platform.cuh`; `python/sglang/kernels/ops/lplb/cuda_solver.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/model_executor/model_runner_components/moe_ep_setup.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `c4ef6d3a4` - fix(dsa): 修复 MQA 显存预算与 CP/MTP 索引补齐 (#382)

- 完整 hash: `c4ef6d3a48dfc0f79bf13871f3c4b028199a7c95`
- 时间/作者: 2026-09-17 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`; `python/sglang/srt/layers/attention/dsa_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `eb4f0ad89` - [feat]适配 w4a8-int8-megamoe (#394)

- 完整 hash: `eb4f0ad89390fc039a5943f241a5a7421bad2a1c`
- 时间/作者: 2026-09-17 / yangyn
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/mega_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `16e9b3867` - feat(hcu): support BF16 KV for Qwen DFLASH2 attention (#405)

- 完整 hash: `16e9b386740e30e4879c696db587db58a2eeeabf`
- 时间/作者: 2026-09-20 / chenyuege
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_interface.py`, `test/manual/test_hcu_dflash_native_block16.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`
  - tests: `test/manual/test_hcu_dflash_native_block16.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `ccc15a6f3` - feat(cache): integrate Mooncake ReadPlan and optimize page-wise loading for direct linker (#404)

- 完整 hash: `ccc15a6f3ff01d34f7b40441cbb7d29246e39003`
- 时间/作者: 2026-09-20 / leichuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_mooncake_direct_linker_read_plan.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`; `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`
  - tests: `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`; `test/registered/unit/mem_cache/test_mooncake_direct_linker_read_plan.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `98ba405a2` - fix(aiter): w13 权重 shuffle 改回 gemm2 布局，修复 w8a8 变体乱码 (#401)

- 完整 hash: `98ba405a238305be3bd2a483216aa5fb0bb2d47b`
- 时间/作者: 2026-09-20 / Wenbo Zhu
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `05c58e82f` - fix(dsa): 修复 gfx938 72CU sparse MQA 路由与 HCU 判断 (#409)

- 完整 hash: `05c58e82faab83b6bf906cfd70f2845eaee1df6c`
- 时间/作者: 2026-09-20 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`, `python/sglang/srt/layers/attention/dsa_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/hcu_sparse_mqa.py`; `python/sglang/srt/layers/attention/dsa_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `50beda6a9` - Update quality gate workflow to use stable version

- 完整 hash: `50beda6a90ba4dd7c85d667530c2614b13122fbf`
- 时间/作者: 2026-09-22 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `31262cd68` - fix: fix deepep num_rdma_bytes count correct (#437)

- 完整 hash: `31262cd68826a1f3bf8ef186dd692d2b3500b036`
- 时间/作者: 2026-09-23 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `90f80c6bd` - feat(moe): 增加 aiter moe_c 后端选定环境变量 (#415)

- 完整 hash: `90f80c6bd5a831f40c29ec8a32200174e749de9f`
- 时间/作者: 2026-09-23 / Wenbo Zhu
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `6c0330d8d` - fix(w4a8): 修复 HIPC MoE scale 重复乘 16 与 HCU RoPE 启动越界 (#439)

- 完整 hash: `6c0330d8d877d146412e65e5cf6bf717a3004dae`
- 时间/作者: 2026-09-23 / lipenghui
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/layers/rotary_embedding/base.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/rotary_embedding/base.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2f93be6c5` - fix(kvcache): handle zero full iterations for asymmetric KV cache (#425)

- 完整 hash: `2f93be6c5e0db8a54fa76d10eab1887e7fcfd145`
- 时间/作者: 2026-09-23 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `066a95af7` - fix: fix lightop situ import regression bug and deepgemm w4a8 op interface change (#428)

- 完整 hash: `066a95af77c479b644e4477afc42b39246f7f58a`
- 时间/作者: 2026-09-23 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `6086af28d` - ci(hcu): migrate v0.5.18 workflows to organization runners (#465)

- 完整 hash: `6086af28ddb97c1cc4c9cf22fadd2940a1100105`
- 时间/作者: 2026-09-30 / dingxinlong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-states.yml`, `.github/workflows/pr-test-hcu.yml` 等 11 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-states.yml`; `.github/workflows/pr-test-hcu.yml` 等 11 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `1828115e0` - fix w4a16 moe asm error (#462)

- 完整 hash: `1828115e08aba1659f71c5da67f761343e3553f4`
- 时间/作者: 2026-09-30 / jiafei96
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `3854f7754` - opt(kda): update kda verify decode op from boltops (#458)

- 完整 hash: `3854f77546c1a65ebc26d86ab84f2ebd96740cc5`
- 时间/作者: 2026-09-30 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kda_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `e885e7223` - fix(hcu): restore ForwardBatch RMS quantization flag (#469)

- 完整 hash: `e885e7223180a8ddc2c9aa753a4c884cfc9ba72c`
- 时间/作者: 2026-09-30 / wu ju
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_forward_batch_hcu_state.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`
  - tests: `test/registered/unit/model_executor/test_forward_batch_hcu_state.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `cfa865d33` - fix deepgemm masked fp8 api upstream (#472)

- 完整 hash: `cfa865d339c0d7191dd044e6980006be799a570a`
- 时间/作者: 2026-10-08 / chaoyujiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b7e4eae12` - fix: remove alt_stream overlap copy when writing KV cache (#478)

- 完整 hash: `b7e4eae1243fb6de06507484afaddbc1715ee054`
- 时间/作者: 2026-10-08 / Wenbo Zhu
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `7fa7729c1` - fix(cache): harden Mooncake ReadPlan and PP direct-L3 cache loading (#482)

- 完整 hash: `7fa7729c1d9a3007baf471184ca709aece7fdbed`
- 时间/作者: 2026-10-08 / leichuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` 等 27 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/managers/schedule_policy.py`; `python/sglang/srt/managers/tokenizer_manager.py`; `python/sglang/srt/observability/req_time_stats.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/managers/scheduler_components/request_receiver.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`; `python/sglang/srt/mem_cache/unified_cache/components/full_component.py`; `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`; `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`; `python/sglang/srt/mem_cache/unified_radix_cache.py`
  - tests: `test/registered/unit/disaggregation/test_bootstrap_failure_release.py`; `test/registered/unit/disaggregation/test_mooncake_final_chunk_poll.py`; `test/registered/unit/managers/test_scheduler_bg_prefetch_collectives.py`; `test/registered/unit/managers/test_scheduler_deferred_reqs.py`; `test/registered/unit/managers/test_scheduler_forward_ingress_fixes.py`; `test/registered/unit/managers/test_scheduler_prefetch_startup_consensus.py`; `test/registered/unit/mem_cache/test_load_back_construction_consensus.py`; `test/registered/unit/mem_cache/test_mooncake_direct_linker_prefetch_capability.py` 等 11 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2cc1bcc28` - fix(deepgemm): 统一 INT8/FP8 权重重排与 FP8 masked GEMM 接口 (#484)

- 完整 hash: `2cc1bcc28c5c4b6e129ae4ce3dadbe3fbc2796cf`
- 时间/作者: 2026-10-09 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `test/registered/openai_server/validation/test_request_length_validation.py`, `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
  - tests: `test/registered/openai_server/validation/test_request_length_validation.py`; `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `a06c34ef7` - fix(ci): stage-b include 列表容忍分支差异的测试文件 (#485)

- 完整 hash: `a06c34ef7511fbf767d1e8f8314546492d5efb0e`
- 时间/作者: 2026-10-09 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `6ca7a1bd6` - fix(test): 修复 unified attention 单测 KV 索引构造 (#489)

- 完整 hash: `6ca7a1bd6a1e7f4719171e4afeb257e4507d3061`
- 时间/作者: 2026-10-09 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/attention/test_triton_attention_kernels.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/attention/test_triton_attention_kernels.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `1882acd8c` - fix(moe): restore DeepEP normal combine for HCU groupgemm (#491)

- 完整 hash: `1882acd8c659b9071ad341741e7b5beef1c40ab0`
- 时间/作者: 2026-10-09 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `bfbff7f68` - fix(hcu): preserve INT8 MoE fallback and restore AITER W8A8 compatibility (#487)

- 完整 hash: `bfbff7f68e024ed71aaec1054c1bdf8ad6df7adf`
- 时间/作者: 2026-10-09 / WenQ7
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/utils/triton_load_watch.py`, `test/registered/unit/distributed/test_aiter_custom_all_reduce_config.py`, `test/registered/unit/layers/moe/test_aiter_w8a8_compat.py`, `test/registered/unit/utils/test_triton_load_watch.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/utils/triton_load_watch.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
  - tests: `test/registered/unit/distributed/test_aiter_custom_all_reduce_config.py`; `test/registered/unit/layers/moe/test_aiter_w8a8_compat.py`; `test/registered/unit/utils/test_triton_load_watch.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `966f6da1b` - fix(hcu): avoid double packing channel FP8 DeepGEMM weights (#497)

- 完整 hash: `966f6da1bcf76359bbbd3f6919f9da6f83ae905a`
- 时间/作者: 2026-10-10 / chaoyujiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `e1eaf0829` - fix(moe): guard SBO setup for flat DeepEP dispatch (#501)

- 完整 hash: `e1eaf08298435a45133f48366cd75d2ccfd03ecb`
- 时间/作者: 2026-10-10 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/batch_overlap/single_batch_overlap.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/batch_overlap/single_batch_overlap.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `f106c5360` - perf(hcu): 优化小 batch W8A8 INT8 GEMM 的 Tiling 选择 (#502)

- 完整 hash: `f106c53608df6269af7296265f9097e9a80abbd2`
- 时间/作者: 2026-10-10 / Yongqiang Duan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `49bb75c79` - fix(diffusion): upload all video outputs to cloud storage

- 完整 hash: `49bb75c791c10b2114c52c58c8d0433bd03e0856`
- 时间/作者: 2026-10-12 / zhangpc3
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `aebf1a9f4` - fix(hcu): fix SlimQuant INT8 DeepEP routing and DeepGEMM weight packing (#514)

- 完整 hash: `aebf1a9f41ad5fd1e00ac1570e6b9e6a8128b237`
- 时间/作者: 2026-10-12 / chaoyujiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `018e5799a` - Fix/hcu aiter moe inplace (#517)

- 完整 hash: `018e5799abb14aa90d05af042db8b273bebc5df9`
- 时间/作者: 2026-10-13 / Wenbo Zhu
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/models/qwen2_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/models/qwen2_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `71b2ee4ea` - perf: add opt-in asynchronous prebuilt token H2D (#516)

- 完整 hash: `71b2ee4ea67b6be712a5575ed1dd0950607fc6b5`
- 时间/作者: 2026-10-13 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/environ.py`, `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`; `python/sglang/srt/environ.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/verify_mla.py`
  - tests: `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `9dd4e2e80` - [diffusion] attention: fix HCU Wan SLA and FA family admission (#519)

- 完整 hash: `9dd4e2e80065ba556c1beb1ffd8b1f2e29bdb085`
- 时间/作者: 2026-10-13 / FrankXu0908
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`, `python/sglang/multimodal_gen/runtime/platforms/rocm.py`, `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`, `python/sglang/multimodal_gen/test/unit/test_wan_sla_layout.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`; `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`; `python/sglang/multimodal_gen/runtime/platforms/rocm.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py`; `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/test/unit/test_wan_sla_layout.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `40c9ec29b` - fix(scheduler): keep DP health probes on the generation path (#528)

- 完整 hash: `40c9ec29b31d5a160c8d83d56949c58e76cc6c26`
- 时间/作者: 2026-10-14 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `c2666f4b5` - [fix] 修复cp 逻辑：解决实际 token 不被整除时不走 cp 的问题 (#538)

- 完整 hash: `c2666f4b5c07e017ad9195c7435236517cda5f08`
- 时间/作者: 2026-10-15 / yangyn
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/dsa/utils.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/dsa/utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `6fe59ce1a` - ci: release-pypi-nightly-hcu 多版本编译 (dtk26.04/py3.10+3.12, dtk26.10/py3.12) [rel/20260825_v0.5.18] (#544)

- 完整 hash: `6fe59ce1ab68fb4ae69951502b621daa5cde0c95`
- 时间/作者: 2026-10-16 / Crowder13
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `0bb71f0c7` - [fix] 解决 w4a8 aiter moe 不支持 swiglu_limit 功能 (#550)

- 完整 hash: `0bb71f0c7fd7faeab15402d9a2d5f6759f623120`
- 时间/作者: 2026-10-16 / yangyn
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b9e0052e9` - fix(hcu): keep the w8a8 smooth asm fast path off on gfx928 (#555)

- 完整 hash: `b9e0052e9e35ae3aa58d73ed685ae6191d64fc24`
- 时间/作者: 2026-10-19 / GarrySnail
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `a031c979a` - [fix] 修复非 AITER 路径下 compressed-tensors W8A8 FP8 MoE 权重被错误补齐导致输出乱码 (#564)

- 完整 hash: `a031c979a4a848bb6905386808d771b5782125e1`
- 时间/作者: 2026-10-20 / liuzj512
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `030f6254f` - perf(attention): add paged split-KV support and opt-in DSpark V2 (#553)

- 完整 hash: `030f6254f2d9d4abe9e57543e3f38757d12ec4ba`
- 时间/作者: 2026-10-20 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/attention/verify_mla.py`; `python/sglang/srt/layers/attention/triton_backend.py`
  - tests: `test/registered/kernels/ops/attention/test_verify_mla_layout.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `19175a690` - [Feat] build: Add build wheel scripts (#569)

- 完整 hash: `19175a69044f2407fa371677a0a7d9be4e226bf2`
- 时间/作者: 2026-10-20 / XiaokunDing
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 模型支持/运行时入口
- 主要文件: `README_HCU.md`, `scripts/build_hcu_wheels.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `README_HCU.md`; `scripts/build_hcu_wheels.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `9f7bfb351` - fix(hcu): skip the w8a8 smooth asm fast path when M=0 (#573)

- 完整 hash: `9f7bfb351d8b2680399994cbade9e83d10972c93`
- 时间/作者: 2026-10-21 / Jane
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/quant_ops.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `464bebd64` - [Fix][v0.5.18] Backport reasoning token accounting fix from upstream #41460 (#579)

- 完整 hash: `464bebd6407de97376f3d00c682036b0494b7ab7`
- 时间/作者: 2026-10-22 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`
  - tests: `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `cbaf42c07` - Fix auxiliary HiCache load-back pending collisions (#591)

- 完整 hash: `cbaf42c071ebacf512215d320eae9c155b29e0e3`
- 时间/作者: 2026-10-26 / chaoyujiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`
  - tests: `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `1343bb07e` - [Fix] deepgemm: 修复 w8a8-fp8 旧版重排逻辑 (#608)

- 完整 hash: `1343bb07ef5f41dcea4dca531b794735203310eb`
- 时间/作者: 2026-10-28 / yangyn
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `448c57ad4` - [fix] 修复 w8a8_int8 量化时视觉层 qkv_proj 未命中忽略名单导致被错误量化 (#632)

- 完整 hash: `448c57ad4d4650d1a0a8ae43fdd416e254f1d4a8`
- 时间/作者: 2026-11-03 / liuzj512
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `c760e11b4` - fix: fix w4a8 int4 deepgemm hipc kernel interface mismatch (#638)

- 完整 hash: `c760e11b4e67898d95038c9ea87e5b83620df7ea`
- 时间/作者: 2026-11-03 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## release/20260825_v0.5.18 到 release_v0.5.18_deepseekv4 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 67（其中 merge 0）
- 分支更新段: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
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
| ... | 另有 81 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
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
| 2026-08-27 | `6b468d012` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 4 个文件 |
| 2026-08-28 | `68dcd498a` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致 | `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-08-28 | `bc990ebd5` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复) | `.github/workflows/release-whl-manual-hcu.yml` |
| 2026-08-31 | `3ca61517d` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci-remove-amd-status-from-pr-summaries | `.github/workflows/pr-states.yml` |
| 2026-08-31 | `e864c3028` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci: enable HCU PR tests for release branches (#272) | `.github/workflows/pr-test-hcu.yml` |
| 2026-09-01 | `8fa7122b3` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE]构建镜像之后触发模型测试 (#277) | `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml` |
| 2026-09-02 | `9d261478d` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [CI] Update HCU model asset paths on main (#285) | `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh` 等 10 个文件 |
| 2026-09-02 | `6fe7ce909` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): restore run suite file filters (#290) | `test/run_suite.py` |
| 2026-09-03 | `2828bde71` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | ci(hcu): align llguidance and model asset paths (#299) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh` |
| 2026-09-04 | `0457572a1` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308) | `.github/workflows/nightly-test-image-hcu.yml` |
| 2026-09-08 | `0af71f61b` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(ci): update HCU evaluation dependencies and asset paths (#325) | `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh` |
| 2026-09-14 | `b5108cc7f` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): use v0.5.18 image and restore eval dependencies (#347) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` 等 4 个文件 |
| 2026-09-14 | `516261baf` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): register sampling test and adjust MMLU threshold (#359) | `test/registered/sampling/test_pytorch_sampling_backend.py` |
| 2026-09-14 | `575cf4797` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): restore source mode for test-only PRs (#364) | `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py` |
| 2026-09-15 | `7c8272a3a` | `release/20260825_v0.5.18..main` | 缺陷修复 | [BUGFIX]更新AICC安装方式 (#367) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-15 | `ae14a99e5` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(ci): fix HCU wheel build target routing (#372) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` |
| 2026-09-15 | `5c03a8e22` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-16 | `adc1d69b2` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): align main wheel builds with 0.5.18 runtime (#379) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml` 等 6 个文件 |
| 2026-09-21 | `ae5c33991` | `release/20260825_v0.5.18..main` | 调度/缓存/PD | Update quality gate workflow to use stable version | `.github/workflows/quality-gate.yml` |
| 2026-09-21 | `cb932f5fb` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | feat(ci) compaity sgl-kernal main to v0.5.12 (#421) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-21 | `a981685e7` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix release-pr-hcu.yml build sglang (#423) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-22 | `b5ca753bc` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): run nightly against v0.5.18 and report its results (#432) | `.github/workflows/nightly-test-hcu.yml` |
| 2026-09-23 | `2871c8fdd` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438) | `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile` |
| 2026-09-23 | `7be1324cf` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | ci: report sglang nightly packages to DashHub (#424) | `.github/workflows/release-pypi-nightly-hcu.yml` |
| 2026-09-24 | `665b27d1f` | `release/20260825_v0.5.18..main` | 缺陷修复 | feat(ci) fix main build whl failed (#449) | `.github/workflows/release-pr-hcu.yml` |
| 2026-09-28 | `5e8269d55` | `release/20260825_v0.5.18..main` | 缺陷修复 | [BUGFIX]镜像DTK版本号不对 (#447) | `.github/workflows/release-docker-hcu.yml` |
| 2026-09-30 | `e05f146be` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | ci(hcu): migrate main workflows to organization runners (#463) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml` 等 12 个文件 |
| 2026-10-09 | `fb46d17ad` | `release/20260825_v0.5.18..main` | 性能/后端优化 | add optest process (#481) | `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-09 | `f0ee2a505` | `release/20260825_v0.5.18..main` | 缺陷修复 | FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473) | `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py` |
| 2026-10-10 | `4205397cb` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | add password-free download code (#499) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-10 | `3b0e4a073` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [Fix] Bound crash diagnostics and fatal shutdown on main (#498) | `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py` 等 6 个文件 |
| 2026-10-12 | `50b0d0051` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | Delegate HCU model deployment smoke CI to external controller (#503) | `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml` |
| 2026-10-12 | `f9b972b37` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | Use a clean checkout directory for the model smoke controller (#510) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `b6dd37e66` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | Run cookbook smoke tests for all cases by default | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-12 | `e295faff5` | `release/20260825_v0.5.18..main` | 性能/后端优化 | update ci name&&add optest log (#515) | `.github/workflows/nightly-test-operator-hcu.yml` |
| 2026-10-14 | `78c700ee0` | `release/20260825_v0.5.18..main` | 模型支持/运行时入口 | Add image input to cookbook deployment smoke workflow (#530) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-15 | `cc3758967` | `release/20260825_v0.5.18..main` | 通用实现调整 | Pass DashHub credential to deployment smoke controller (#534) | `.github/workflows/cookbook-deployment-smoke.yml` |
| 2026-10-15 | `fc095e059` | `release/20260825_v0.5.18..main` | 缺陷修复 | fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533) | `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py` 等 4 个文件 |
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
| 2026-10-23 | `962617b2d` | `release/20260825_v0.5.18..release/20261023_v0.5.18_welm` | 性能/后端优化 | WeLM v4.5 support on HCU (squash of yaoyupings/sglang-das v0.5.18_welm) | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/configs/model_config.py` 等 55 个文件 |
| 2026-10-20 | `eaa872862` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | fix: support API key with multiple tokenizer workers (#559) | `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/auth.py`, `test/registered/unit/entrypoints/test_http_server_auth_config.py` 等 5 个文件 |
| 2026-10-20 | `4c5ac2ee0` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | fix(disagg): defer cached-prefix sends during cache loads (#562) | `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `test/manual/hicache/test_pd_cached_prefix_load_ordering.py` |
| 2026-10-23 | `f0a0530ce` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | [Fix] grammar: 同步 Prefill CP 的 Grammar 请求准入与失败状态 (#589) | `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/constrained/test_grammar_manager.py` |
| 2026-10-30 | `c66f34363` | `release/20260825_v0.5.18..release_v0.5.18_deepseekv4` | 缺陷修复 | [Fix] TokenizerManager: 修复客户端断开后已下发请求未被终止的问题 (#628) | `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py` |

### 逐 Commit 审计卡

#### Commit `a96aed11f` - [feat] 适配aiter性能优化后的 sglang_fused_sigmoid_gating_delta_rule_update 算子

- 完整 hash: `a96aed11f05f65d18f5bd46446b4ca9b7ac82105`
- 时间/作者: 2026-08-21 / zhuwenbopro
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `d42ecf6fe` - Fix HCU detection and sanitized topology diagnostics

- 完整 hash: `d42ecf6fe9854d6127c167959fe7bec30439b73b`
- 时间/作者: 2026-08-21 / reverie-hub
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `scripts/ci/hcu/hcu_rename_allowlist.txt`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`; `scripts/ci/hcu/hcu_rename_allowlist.txt`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `fd4157047` - Refine HCU platform diagnostics and CLI help

- 完整 hash: `fd415704795411fa8fcbc7d7571c41dcb3d1c431`
- 时间/作者: 2026-08-24 / reverie-hub
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/platforms/__init__.py`
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `d1adf7b50` - [feature] manual compile ci

- 完整 hash: `d1adf7b503b20e64e07c38946a067ee90c428962`
- 时间/作者: 2026-08-25 / zhangyh15
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `94e9fa4b1` - ci: align manual HCU wheel workflow with nightly (drop chown/devpi upload)

- 完整 hash: `94e9fa4b1d10f14c6120bab4f5416caf6e318cd9`
- 时间/作者: 2026-08-25 / zhangyh15
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `990a1a798` - ci: disable scheduled gateway nightly release

- 完整 hash: `990a1a798d40ccea97ef91c16a9d8cd8f25957e2`
- 时间/作者: 2026-08-26 / dddddddxl
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-release-gateway.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-release-gateway.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `8dd5daf2f` - Refine HCU and AMD CLI help text

- 完整 hash: `8dd5daf2fa5555ab13751b159703124fd493a437`
- 时间/作者: 2026-08-26 / reverie-hub
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `python/sglang/srt/server_args.py`, `test/run_suite.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/server_args.py`
  - tests: `test/run_suite.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c94c3ca2c` - fix: gateway wheel is at workspace root target/wheels

- 完整 hash: `c94c3ca2c8341c501b46a32c750e32dfe8ce4e06`
- 时间/作者: 2026-08-26 / zhangyh15
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f6d701c52` - Fix stale HCU Stage B test paths

- 完整 hash: `f6d701c520529490926e3c350682b7fe7ca6f9d0`
- 时间/作者: 2026-08-26 / reverie-hub
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a2de3b8cf` - ci(hcu): use bash for wheel build jobs

- 完整 hash: `a2de3b8cffc365e5f813d2ddd6c7226abe29db90`
- 时间/作者: 2026-08-26 / dddddddxl
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `2866df994` - ci(hcu): trust wheel build workspaces

- 完整 hash: `2866df9948b40e81405fcf5947ef74b8f744c9a3`
- 时间/作者: 2026-08-27 / dddddddxl
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `7609d9af6` - [feature]适配hcu发包

- 完整 hash: `7609d9af69ac40ed6730564cde4934d5b3e4a540`
- 时间/作者: 2026-08-27 / zhangyh15
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`, `python/pyproject_hcu.toml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`; `python/pyproject_hcu.toml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `6b468d012` - [feature] hcu ci: docker 镜像加 daily 定时触发, router 编包改用 vendored openssl, 镜像补装 flash_kda

- 完整 hash: `6b468d012bcf693157cee193493842185165b93b`
- 时间/作者: 2026-08-27 / zhangyh15
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pr-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `68dcd498a` - [ci] hcu ci 文件与 release/20260825_v0.5.18 分支保持一致

- 完整 hash: `68dcd498aa7550a39e7f53b6588e19785efd5cae`
- 时间/作者: 2026-08-28 / zhangyh15
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `bc990ebd5` - [ci] 删除 release-whl-manual-hcu.yml (功能与 nightly/pr 编包重复)

- 完整 hash: `bc990ebd52e0ae2500dc3c0ab4eeba187e84965b`
- 时间/作者: 2026-08-28 / zhangyh15
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-whl-manual-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-whl-manual-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `3ca61517d` - ci-remove-amd-status-from-pr-summaries

- 完整 hash: `3ca61517d037e82ba19c981dd66ddaf0245e85cd`
- 时间/作者: 2026-08-31 / dddddddxl
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-states.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-states.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `e864c3028` - ci: enable HCU PR tests for release branches (#272)

- 完整 hash: `e864c302870000325162a5788883997cc850ade8`
- 时间/作者: 2026-08-31 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `8fa7122b3` - [FEATURE]构建镜像之后触发模型测试 (#277)

- 完整 hash: `8fa7122b3ace4a4de48372ee3c4c3346871281d7`
- 时间/作者: 2026-09-01 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/release-docker-hcu.yml`, `docker/image-citest-conf-hcu.yaml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
  - other: `docker/image-citest-conf-hcu.yaml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `9d261478d` - [CI] Update HCU model asset paths on main (#285)

- 完整 hash: `9d261478d6ace185f3e35a7211fc411b64d2057f`
- 时间/作者: 2026-09-02 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `README_HCU.md`, `python/sglang/test/hcu_cookbook_utils.py`, `scripts/ci/hcu/hcu_ci_exec.sh`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`, `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py` 等 10 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_exec.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`; `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py`; `test/registered/hcu/spec/test_ngram_speculative_decoding_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `6fe7ce909` - ci(hcu): restore run suite file filters (#290)

- 完整 hash: `6fe7ce9097c8e9f1b7dccefbe4834a7f928a78c2`
- 时间/作者: 2026-09-02 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `test/run_suite.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `2828bde71` - ci(hcu): align llguidance and model asset paths (#299)

- 完整 hash: `2828bde71da3f5f6314aa4022ae7e163dfc33ada`
- 时间/作者: 2026-09-03 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `0457572a1` - [FEATURE]CInotificate发送飞书通知时，把镜像数据推送到数据库 (#308)

- 完整 hash: `0457572a14edd55e05220726ff4a8af8b1931771`
- 时间/作者: 2026-09-04 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-image-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-image-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `0af71f61b` - fix(ci): update HCU evaluation dependencies and asset paths (#325)

- 完整 hash: `0af71f61b693c2bd2817a678e007660222db9bf3`
- 时间/作者: 2026-09-08 / tianly
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `scripts/ci/hcu/hcu_ci_exec.sh`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/hcu_ci_start_container.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `scripts/ci/hcu/hcu_ci_exec.sh`; `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/hcu_ci_start_container.sh`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `b5108cc7f` - ci(hcu): use v0.5.18 image and restore eval dependencies (#347)

- 完整 hash: `b5108cc7fea82d75da174f8f6681a843d43c462b`
- 时间/作者: 2026-09-14 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/utils/sgl_eval_ref.sh`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/utils/sgl_eval_ref.sh`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `516261baf` - ci(hcu): register sampling test and adjust MMLU threshold (#359)

- 完整 hash: `516261baf108e56bcb4a03dc7294a936e9656a2d`
- 时间/作者: 2026-09-14 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `test/registered/sampling/test_pytorch_sampling_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - tests: `test/registered/sampling/test_pytorch_sampling_backend.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `575cf4797` - ci(hcu): restore source mode for test-only PRs (#364)

- 完整 hash: `575cf47976761be9916048cfe2ca244b56d63fab`
- 时间/作者: 2026-09-14 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`
  - tests: `test/registered/hcu/openai_server/test_serving_chat_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `7c8272a3a` - [BUGFIX]更新AICC安装方式 (#367)

- 完整 hash: `7c8272a3a32d25391c8bc20e0c0678d3c9ac895d`
- 时间/作者: 2026-09-15 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `ae14a99e5` - fix(ci): fix HCU wheel build target routing (#372)

- 完整 hash: `ae14a99e502d0e5dbed8abf42e3b35eb8807c3c5`
- 时间/作者: 2026-09-15 / tianly
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `5c03a8e22` - [FEATURE]daily镜像将tag打入环境变量, dtk自动更新最新的blas (#376)

- 完整 hash: `5c03a8e22f8cfeef0f10cd909231862bd446cc30`
- 时间/作者: 2026-09-15 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `adc1d69b2` - ci(hcu): align main wheel builds with 0.5.18 runtime (#379)

- 完整 hash: `adc1d69b2a610fc000ca27e4b92c72e9c1b85044`
- 时间/作者: 2026-09-16 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`, `scripts/ci/hcu/hcu_ci_install_dependency.sh`, `scripts/ci/hcu/test_hcu_build_alignment.py`, `scripts/ci/hcu/test_hcu_wheel_version.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_install_dependency.sh`; `scripts/ci/hcu/test_hcu_build_alignment.py`; `scripts/ci/hcu/test_hcu_wheel_version.py`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `ae5c33991` - Update quality gate workflow to use stable version

- 完整 hash: `ae5c33991be7f0e277f71c4e853c10fc11cbe627`
- 时间/作者: 2026-09-21 / Lvjiajia
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/quality-gate.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/quality-gate.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `cb932f5fb` - feat(ci) compaity sgl-kernal main to v0.5.12 (#421)

- 完整 hash: `cb932f5fbd904a577093a262c6a101834a1ef994`
- 时间/作者: 2026-09-21 / 463975089
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a981685e7` - fix release-pr-hcu.yml build sglang (#423)

- 完整 hash: `a981685e7f137a9e0629cbdcad2ad7bdd42017b9`
- 时间/作者: 2026-09-21 / 463975089
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `b5ca753bc` - ci(hcu): run nightly against v0.5.18 and report its results (#432)

- 完整 hash: `b5ca753bc8e054ce99b4c01b0369eb89c6870dbb`
- 时间/作者: 2026-09-22 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/nightly-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `2871c8fdd` - ci(hcu): docker 镜像改从 dev 基础镜像内联安装 DTK 26.04.1-72cu-0911 (#438)

- 完整 hash: `2871c8fdd9594de894546b144d253c3dd88fd900`
- 时间/作者: 2026-09-23 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-docker-hcu.yml`, `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `7be1324cf` - ci: report sglang nightly packages to DashHub (#424)

- 完整 hash: `7be1324cf827dafe9f09ec3f86ade353801b5e1e`
- 时间/作者: 2026-09-23 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/release-pypi-nightly-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pypi-nightly-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `665b27d1f` - feat(ci) fix main build whl failed (#449)

- 完整 hash: `665b27d1fa35017a437b0aa0099a5f8aa33e5d9b`
- 时间/作者: 2026-09-24 / 463975089
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `5e8269d55` - [BUGFIX]镜像DTK版本号不对 (#447)

- 完整 hash: `5e8269d55a8cf4629cc39a3171169f4aa8b4d14b`
- 时间/作者: 2026-09-28 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `e05f146be` - ci(hcu): migrate main workflows to organization runners (#463)

- 完整 hash: `e05f146bed9ca80c72a18a4946fd6f838d8e7774`
- 时间/作者: 2026-09-30 / dingxinlong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-hcu.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/nightly-test-image-hcu.yml`, `.github/workflows/pr-states.yml` 等 12 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-hcu.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/nightly-test-image-hcu.yml`; `.github/workflows/pr-states.yml` 等 12 个文件
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `fb46d17ad` - add optest process (#481)

- 完整 hash: `fb46d17ad9f633aa7fee521484262b0c26de560d`
- 时间/作者: 2026-10-09 / Lee156
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f0ee2a505` - FIX(detokenizer): stream through genuine U+FFFD instead of holding until finish (#473)

- 完整 hash: `f0ee2a5059c2d6a167bee3d996bca004276b3138`
- 时间/作者: 2026-10-09 / JackPeng
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/detokenizer_manager.py`, `test/registered/unit/managers/test_detokenizer_incremental.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/managers/detokenizer_manager.py`
  - tests: `test/registered/unit/managers/test_detokenizer_incremental.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `4205397cb` - add password-free download code (#499)

- 完整 hash: `4205397cbcf8c60852fadd7306cea32f2541a19d`
- 时间/作者: 2026-10-10 / Lee156
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `3b0e4a073` - [Fix] Bound crash diagnostics and fatal shutdown on main (#498)

- 完整 hash: `3b0e4a07393778001dcd518d2b11de225e1be8c8`
- 时间/作者: 2026-10-10 / 王启宇
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`, `test/registered/unit/utils/test_bounded_fatal_shutdown.py`, `test/registered/unit/utils/test_bounded_pyspy.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `docs/docs/references/environment_variables.mdx`
  - other: `python/sglang/srt/managers/multi_tokenizer_mixin.py`; `python/sglang/srt/managers/tokenizer_manager.py`
  - runtime-perf: `python/sglang/srt/utils/cudacore_pyspy_dump_utils.py`
  - tests: `test/registered/unit/utils/test_bounded_fatal_shutdown.py`; `test/registered/unit/utils/test_bounded_pyspy.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `50b0d0051` - Delegate HCU model deployment smoke CI to external controller (#503)

- 完整 hash: `50b0d005189ee23cf3046b86dc44986c5e6b9345`
- 时间/作者: 2026-10-12 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f9b972b37` - Use a clean checkout directory for the model smoke controller (#510)

- 完整 hash: `f9b972b372f8695154301e2d7cee24195a963250`
- 时间/作者: 2026-10-12 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `b6dd37e66` - Run cookbook smoke tests for all cases by default

- 完整 hash: `b6dd37e66ad4f820a75614c8b0e6f54ffa67c796`
- 时间/作者: 2026-10-12 / gcy
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `e295faff5` - update ci name&&add optest log (#515)

- 完整 hash: `e295faff5dc889c97626f7bd25f6a8ca0a0f100c`
- 时间/作者: 2026-10-12 / Lee156
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `78c700ee0` - Add image input to cookbook deployment smoke workflow (#530)

- 完整 hash: `78c700ee0100f215268a3a802538881f281f29e2`
- 时间/作者: 2026-10-14 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `cc3758967` - Pass DashHub credential to deployment smoke controller (#534)

- 完整 hash: `cc3758967d74748204015a050182e5ad176c8a08`
- 时间/作者: 2026-10-15 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `fc095e059` - fix(bench): reuse --tokenize-prompt for generated shared-prefix token IDs (#533)

- 完整 hash: `fc095e059889d2fae91e86a5b3e5fa19eb8d7a34`
- 时间/作者: 2026-10-15 / chaoyujiang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/benchmark/datasets/common.py`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`
  - tests: `test/registered/bench_fn/test_benchmark_datasets_api.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `87b9d5c85` - Run cookbook deployment checks after HCU image publishing (#548)

- 完整 hash: `87b9d5c85eafab11fe18235718c1af37b348d784`
- 时间/作者: 2026-10-16 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `f89209aa8` - ci: pass package server to Cookbook model tests (#556)

- 完整 hash: `f89209aa84a4fd0619d0662f6adf6980740efc78`
- 时间/作者: 2026-10-19 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `a8543c813` - [CI] cookbook: Add BW1000 deployment smoke tests (#570)

- 完整 hash: `a8543c8131d429500411b8ba235b5411ddbabbd3`
- 时间/作者: 2026-10-20 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `6dac3481c` - [Fix] ci: Preserve model cases in DashHub operator reporting (#604)

- 完整 hash: `6dac3481cd73b48641f481b14858187d1936ee81`
- 时间/作者: 2026-10-28 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `098f31d69` - fix(ci) rebase pr-test-hcu.yml release-pr-hcu.yml (#612)

- 完整 hash: `098f31d695ce94169e6adf9ce55109beb532b326`
- 时间/作者: 2026-10-28 / 463975089
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pr-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pr-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `029b6e641` - [CI] model-ci: Pass history token for daily comparison report (#607)

- 完整 hash: `029b6e6418828280e22086449dfa174433d2788b`
- 时间/作者: 2026-10-28 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/cookbook-deployment-smoke.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/cookbook-deployment-smoke.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `fd98647ed` - [Fix] ci: Restore previous DashHub operator reporting (#614)

- 完整 hash: `fd98647ed1fc3d911926ea9d399b69934303c104`
- 时间/作者: 2026-10-28 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`, `.github/workflows/release-docker-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`; `.github/workflows/release-docker-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `25aa13e98` - fix(ci) rebase pr-test-hcu.yml (#617)

- 完整 hash: `25aa13e98fe76d262d87c0b798ec8a3215ffb703`
- 时间/作者: 2026-10-29 / 463975089
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `.github/workflows/pr-test-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `db479b030` - [CI] optest: Report outcome to DashHub (#619)

- 完整 hash: `db479b030f0975dbda241bf46fc4556a89a02365`
- 时间/作者: 2026-10-29 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `9fb319cc3` - [CI] optest: Require every enabled operator result (#622)

- 完整 hash: `9fb319cc33a15b624970b0f5e45020e2a573dc07`
- 时间/作者: 2026-10-29 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-operator-hcu.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-operator-hcu.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `471ab8254` - Add one-time DashHub recovery for run 41338132822 (#633)

- 完整 hash: `471ab8254520c958d3c614e768a29b10423f7cf2`
- 时间/作者: 2026-11-02 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/dashhub-recover-41338132822.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `594e1ae94` - [Chore] ci: Remove completed DashHub recovery workflow (#634)

- 完整 hash: `594e1ae94c6103dabed4152a4ebbcca6fb049aeb`
- 时间/作者: 2026-11-02 / guochenyang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `.github/workflows/dashhub-recover-41338132822.yml`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/dashhub-recover-41338132822.yml`
- 验证与风险: 主要影响 CI 或工程流程；性能分析中只作为构建、测试或依赖环境线索。

#### Commit `962617b2d` - WeLM v4.5 support on HCU (squash of yaoyupings/sglang-das v0.5.18_welm)

- 完整 hash: `962617b2d8f42175937aa79cfe36d14db4e02884`
- 时间/作者: 2026-10-23 / sunjf
- 分支更新段: `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/welm_dedup_decode.py`, `python/sglang/srt/layers/attention/welm_fa256_src/build.sh` 等 55 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/welm_oe_host.py`; `python/sglang/srt/layers/welm_oe_host_src/build.sh`; `python/sglang/srt/layers/welm_oe_host_src/export_oe.py`; `python/sglang/srt/layers/welm_oe_host_src/oe_host_gather.cpp`; `python/sglang/srt/layers/welmv4_fast_op.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/runner_utils/buffers.py`; `python/sglang/srt/models/welmv4.py`; `python/sglang/srt/models/welmv4_nextn.py`; `python/sglang/srt/models/welmv4_vlm.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_common.py` 等 10 个文件
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/welm_dedup_decode.py`; `python/sglang/srt/layers/attention/welm_fa256_src/build.sh`; `python/sglang/srt/layers/attention/welm_fa256_src/flags.txt`; `python/sglang/srt/layers/attention/welm_fa256_src/lflags.txt`; `python/sglang/srt/layers/attention/welm_fa256_src/welm_fa256.cpp` 等 31 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `eaa872862` - fix: support API key with multiple tokenizer workers (#559)

- 完整 hash: `eaa8728623fbab132f881e470e7715ff69ac9bff`
- 时间/作者: 2026-10-20 / zhengzhi
- 分支更新段: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/auth.py`, `test/registered/unit/entrypoints/test_http_server_auth_config.py`, `test/registered/unit/spec/test_ngram_corpus.py`, `test/registered/unit/utils/test_http_server_auth.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/utils/auth.py`
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`
  - tests: `test/registered/unit/entrypoints/test_http_server_auth_config.py`; `test/registered/unit/spec/test_ngram_corpus.py`; `test/registered/unit/utils/test_http_server_auth.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `4c5ac2ee0` - fix(disagg): defer cached-prefix sends during cache loads (#562)

- 完整 hash: `4c5ac2ee05e286d7f5c05cb789c60fdea4db0f58`
- 时间/作者: 2026-10-20 / 千纱都
- 分支更新段: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `test/manual/hicache/test_pd_cached_prefix_load_ordering.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/disaggregation/prefill.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
  - tests: `test/manual/hicache/test_pd_cached_prefix_load_ordering.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `f0a0530ce` - [Fix] grammar: 同步 Prefill CP 的 Grammar 请求准入与失败状态 (#589)

- 完整 hash: `f0a0530ce34fa7986c05c010146acb8ea0c20464`
- 时间/作者: 2026-10-23 / JingLee
- 分支更新段: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/constrained/test_grammar_manager.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/constrained/grammar_manager.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
  - tests: `test/registered/unit/constrained/test_grammar_manager.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `c66f34363` - [Fix] TokenizerManager: 修复客户端断开后已下发请求未被终止的问题 (#628)

- 完整 hash: `c66f3436365416bf3bb14c6e1b3665b669608573`
- 时间/作者: 2026-10-30 / zhengzhi
- 分支更新段: `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/managers/tokenizer_manager.py`
  - tests: `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
