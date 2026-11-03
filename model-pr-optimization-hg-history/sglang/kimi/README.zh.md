# sglang Kimi K2/K2.5/Linear/VL 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| - | 无本地独有提交 |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 1
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-30 | `2b0bed239` | 性能/后端优化 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` |

## 逐 Commit 审计卡

### Commit `2b0bed239` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- 完整 hash: `2b0bed23943bee2e93916979aabc272268a11a1c`
- 时间/作者: 2026-03-30 / maxiao1
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## v0.5.8_dev 到 v0.5.12_dev 本地独有提交补充

### 覆盖说明

- 来源索引: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- 来源工作树: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交。
- 本章节提交数: 2
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-03-30 | `00db89c86` | `v0.5.8_dev..v0.5.9_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |
| 2026-03-30 | `7bfdade34` | `v0.5.9_dev..v0.5.10_dev` | 缺陷修复 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 5 个文件 |

### 逐 Commit 审计卡

#### Commit `00db89c86` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- 完整 hash: `00db89c86ed93c08a883ffa6b708babf8e89743c`
- 时间/作者: 2026-03-30 / maxiao1
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

#### Commit `7bfdade34` - 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug

- 完整 hash: `7bfdade34395bd4ae7c723b64de68a990820d0b2`
- 时间/作者: 2026-03-30 / maxiao1
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/models/deepseek_v2.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 缺陷修复类提交；复用时优先验证触发条件、精度回归和异常路径。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 25（其中 merge 2）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
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
| ... | 另有 70 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-08-07 | `2b4271498` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` 等 11 个文件 |
| 2026-07-30 | `785804bfb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix triton moe path but accuracy fail | `python/sglang/kernels/ops/kimi_k3/__init__.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/mxfp4.py` |
| 2026-08-06 | `a6ce82576` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support flash kda, hcu triton kda and hcu triton attn residual | `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/kda.py` 等 8 个文件 |
| 2026-08-07 | `12ba645c7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support WFP4A16 hipc moe for kimi-k3 | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-08-11 | `8084b5cac` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | merge: fix kimi-k3 merge conflict | `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-08-11 | `9c60fd0fd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: fix situ activation jit error | `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh` 等 4 个文件 |
| 2026-08-13 | `00468ade3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | perf: route K3 attention-residual aggregation to the HCU kernel on large batches | `python/sglang/srt/layers/attn_residual.py` |
| 2026-08-13 | `38eea340e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: correct Kimi-K3 INT4 MoE accuracy via slimquant quant Triton W4A16 path | `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/server_args.py` |
| 2026-08-15 | `68d20891f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: refactor kimi k3 int4 moe for activate 8 or 16 bit | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` 等 4 个文件 |
| 2026-08-18 | `38cdca36f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat: support w4a8 hipc moe for k3 int4_w4a16 model | `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` |
| 2026-08-19 | `c4212e944` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 适配kimi-k3-w4a8-huawei | `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py`, `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py` 等 17 个文件 |
| 2026-08-20 | `6de39e28a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | refactor(hcu): replace vendored KDA kernels with boltops | `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py` 等 8 个文件 |
| 2026-08-25 | `88f910e94` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix: preserve release fuse_swiglu with source Kimi MoE | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` |
| 2026-08-26 | `5c6fb2e29` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #236 from daishiqiang123/20260825_v0.5.18_kimi_k3 | 无直接文件变更/merge |
| 2026-08-27 | `561186ca9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | kimi-k3 dspark support (#249) | `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py` 等 4 个文件 |
| 2026-08-27 | `2ec9f04ae` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]: use aiter moe for kimi-k3-w4a8-huawei | `python/sglang/srt/layers/quantization/modelslim/aiter_w4a8.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py` |
| 2026-08-29 | `ea6b50308` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Merge pull request #260 from daishiqiang123/0.5.18_kimi_deepep_fix | 无直接文件变更/merge |
| 2026-09-01 | `ddbbccde8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(dsv4): support PP/DSpark and CP-aware sparse prefill on HCU (#274) | `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 32 个文件 |
| 2026-09-20 | `4c219c5f3` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | opt: opt dense moe ag and nonzero bubble (#406) | `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/srt/environ.py` 等 5 个文件 |
| 2026-09-20 | `8eb6acd22` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(moe): support EPLB for Kimi K3 with DSpark bug fix (#411) | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py` 等 5 个文件 |
| 2026-10-12 | `c9a84fca9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Perf][HCU] Optimize Kimi K3 decode fusions 20261010 (#507) | `.gitignore`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py` 等 17 个文件 |
| 2026-10-15 | `5b6302252` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): keep packed FP8 Q on the old MLA path for Kimi K3 (#537) | `python/sglang/srt/layers/attention/hcu_mla_backend.py` |
| 2026-10-16 | `ae065131d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(kimi-k3): add opt-in serial shared-expert overlap for DeepEP (#540) | `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/k3_sbo_gemm.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` 等 6 个文件 |
| 2026-10-16 | `da90edf06` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(k3): fix aiter ar shape mismatch and some entries accept rate=1 (#546) | `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/logits_processor.py` |
| 2026-10-23 | `e7fb26db7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(acc): fix k3-int4 tp16 acc wrong (#587) | `python/sglang/srt/models/kimi_k3.py` |

### 逐 Commit 审计卡

#### Commit `2b4271498` - ci(hcu): publish nine-model accuracy results

- 完整 hash: `2b4271498f3d9031d0080accfa4dea9eccd10a59`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`, `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`, `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py` 等 11 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `scripts/ci/hcu/hcu_ci_notify_feishu.py`; `scripts/ci/hcu/test_hcu_ci_notify_feishu.py`
  - tests: `test/registered/hcu/accuracy/bw1100/test_cookbook_text_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_deepseek_v32_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_glm51_int8_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_gsm8k_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_kimi_k26_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_minimax_m25_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_mmlu_eval_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_qwen35_eval_hcu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `785804bfb` - fix triton moe path but accuracy fail

- 完整 hash: `785804bfb994a0afb14e936b163be40803190d28`
- 时间/作者: 2026-07-30 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/kimi_k3/__init__.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/mxfp4.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/kimi_k3/__init__.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/mxfp4.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `a6ce82576` - feat: support flash kda, hcu triton kda and hcu triton attn residual

- 完整 hash: `a6ce82576e49f7456af4b83d1bae95625e26bb89`
- 时间/作者: 2026-08-06 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/kernels/ops/attention/fla/kda_hcu.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/attn_residual.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/attn_residual.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/chunk_intra.py`; `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`; `python/sglang/kernels/ops/attention/fla/kda.py`; `python/sglang/kernels/ops/attention/fla/kda_hcu.py`; `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`; `python/sglang/srt/layers/attention/linear/kda_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `12ba645c7` - feat: support WFP4A16 hipc moe for kimi-k3

- 完整 hash: `12ba645c77fd34eb18379b2bd7dc503f25a3b4e9`
- 时间/作者: 2026-08-07 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `8084b5cac` - merge: fix kimi-k3 merge conflict

- 完整 hash: `8084b5cacf215104abd62eb2e5e548a0f019302a`
- 时间/作者: 2026-08-11 / zhaosong1
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `9c60fd0fd` - fix: fix situ activation jit error

- 完整 hash: `9c60fd0fdffdc9fa0ad89e7ecf0bf046482a4d62`
- 时间/作者: 2026-08-11 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh`, `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`; `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`; `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh`; `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `00468ade3` - perf: route K3 attention-residual aggregation to the HCU kernel on large batches

- 完整 hash: `00468ade31979fcdedd2b1586b62219ad7c26dfc`
- 时间/作者: 2026-08-13 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attn_residual.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/attn_residual.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `38eea340e` - fix: correct Kimi-K3 INT4 MoE accuracy via slimquant quant Triton W4A16 path

- 完整 hash: `38eea340e42d537d77f6d3a6f651de46e04b5ad5`
- 时间/作者: 2026-08-13 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `68d20891f` - fix: refactor kimi k3 int4 moe for activate 8 or 16 bit

- 完整 hash: `68d20891ff89194d21c6197b47a60a2d3e8b2f4d`
- 时间/作者: 2026-08-15 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `38cdca36f` - feat: support w4a8 hipc moe for k3 int4_w4a16 model

- 完整 hash: `38cdca36fe2c8fb27b4ae5475fe99e9a65f12faa`
- 时间/作者: 2026-08-18 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `c4212e944` - 适配kimi-k3-w4a8-huawei

- 完整 hash: `c4212e94422f5cbe6d1519398ce7003b913a2f25`
- 时间/作者: 2026-08-19 / WuFan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/npu_kernels/__init__.py`, `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py`, `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py`, `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py`, `python/sglang/kernels/npu_kernels/npu_moe_finalize_routing_triton.py`, `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py`, `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py`, `python/sglang/srt/hardware_backend/npu/moe/activation.py` 等 17 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/kernels/npu_kernels/__init__.py`; `python/sglang/kernels/npu_kernels/npu_dequant_swiglu_quant_triton.py`; `python/sglang/kernels/npu_kernels/npu_dynamic_quant_triton.py`; `python/sglang/kernels/npu_kernels/npu_grouped_matmul_triton.py`; `python/sglang/kernels/npu_kernels/npu_moe_finalize_routing_triton.py`; `python/sglang/kernels/npu_kernels/npu_moe_init_routing_v2_triton.py`; `python/sglang/kernels/npu_kernels/npu_quant_matmul_triton.py`; `python/sglang/srt/hardware_backend/npu/moe/activation.py` 等 16 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `6de39e28a` - refactor(hcu): replace vendored KDA kernels with boltops

- 完整 hash: `6de39e28a3e6cc03cfb88f71d1c3382dafe34427`
- 时间/作者: 2026-08-20 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/kernels/ops/attention/fla/kda_hcu.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`, `python/sglang/srt/layers/attn_residual.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/attn_residual.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`; `python/sglang/kernels/ops/attention/fla/chunk_intra.py`; `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`; `python/sglang/kernels/ops/attention/fla/kda.py`; `python/sglang/kernels/ops/attention/fla/kda_hcu.py`; `python/sglang/kernels/ops/kimi_k3/attn_res_hcu.py`; `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `88f910e94` - fix: preserve release fuse_swiglu with source Kimi MoE

- 完整 hash: `88f910e94553c50210cd42e4a278c6afbba41b6c`
- 时间/作者: 2026-08-25 / shiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `5c6fb2e29` - Merge pull request #236 from daishiqiang123/20260825_v0.5.18_kimi_k3

- 完整 hash: `5c6fb2e29f5211aac83ad24378771464baec4ac2`
- 时间/作者: 2026-08-26 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `561186ca9` - kimi-k3 dspark support (#249)

- 完整 hash: `561186ca93c8630038574e78654e2a517cb8f8e7`
- 时间/作者: 2026-08-27 / jiafei96
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/layers/attention/hcu_mla_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/attention/decode_attention.py`; `python/sglang/kernels/ops/attention/extend_attention.py`; `python/sglang/srt/layers/attention/hcu_mla_backend.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2ec9f04ae` - [feat]: use aiter moe for kimi-k3-w4a8-huawei

- 完整 hash: `2ec9f04ae224b3d5a39bab76c17f7b11772a5f6e`
- 时间/作者: 2026-08-27 / WuFan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/modelslim/aiter_w4a8.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/quantization/modelslim/aiter_w4a8.py`; `python/sglang/srt/layers/quantization/modelslim/modelslim.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `ea6b50308` - Merge pull request #260 from daishiqiang123/0.5.18_kimi_deepep_fix

- 完整 hash: `ea6b50308e972d67bfbce1fb1eed9bbb019c38d5`
- 时间/作者: 2026-08-29 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `ddbbccde8` - feat(dsv4): support PP/DSpark and CP-aware sparse prefill on HCU (#274)

- 完整 hash: `ddbbccde8cc167817faf2f643dfd79c6f4f9e6e6`
- 时间/作者: 2026-09-01 / JingLee
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` 等 32 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/nixl/conn.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/managers/utils.py`; `python/sglang/srt/speculative/dspark_components/dspark_kv_inject.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner_components/layer_setup.py`; `python/sglang/srt/model_executor/runner_utils/buffers.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/deepseek_v4_dspark.py`; `python/sglang/srt/models/dspark.py`; `python/sglang/srt/models/kimi_k3.py`; `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/server_args.py` 等 10 个文件
  - runtime-perf: `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py`; `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`; `python/sglang/srt/managers/scheduler_pp_mixin.py`; `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`; `python/sglang/srt/mem_cache/dsa_cache_layer_split.py` 等 11 个文件
  - tests: `test/registered/unit/disaggregation/test_disaggregation_wire.py`; `test/registered/unit/disaggregation/test_pp_pd_consensus.py`; `test/registered/unit/spec/test_dspark_pp_context.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4c219c5f3` - opt: opt dense moe ag and nonzero bubble (#406)

- 完整 hash: `4c219c5f307b655b42b198737229c391f5988900`
- 时间/作者: 2026-09-20 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/kimi_k3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/kernels/ops/kvcache/__init__.py`; `python/sglang/kernels/ops/kvcache/cache_move.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `8eb6acd22` - feat(moe): support EPLB for Kimi K3 with DSpark bug fix (#411)

- 完整 hash: `8eb6acd22bca671c36219947cd25df4be1ef8ef2`
- 时间/作者: 2026-09-20 / daishiqiang123
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `test/manual/ep/test_kimi_k3_eplb.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/speculative/dspark_components/dspark_verify.py`
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/kimi_k3.py`; `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`
  - tests: `test/manual/ep/test_kimi_k3_eplb.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `c9a84fca9` - [Perf][HCU] Optimize Kimi K3 decode fusions 20261010 (#507)

- 完整 hash: `c9a84fca9624adb32d1848a05298a39ca6f0409f`
- 时间/作者: 2026-10-12 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `.gitignore`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py`, `python/sglang/kernels/ops/kimi_k3/csrc/mla_post_hip.cu`, `python/sglang/kernels/ops/kimi_k3/mla_post_hip.py`, `python/sglang/kernels/ops/mamba/csrc/mamba_state_indices_hip.cu`, `python/sglang/kernels/ops/mamba/mamba_state_indices.py`, `python/sglang/kernels/ops/mamba/mamba_state_indices_hip.py` 等 17 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `.gitignore`; `python/sglang/srt/layers/attn_residual.py`; `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py`; `python/sglang/kernels/ops/kimi_k3/csrc/mla_post_hip.cu`; `python/sglang/kernels/ops/kimi_k3/mla_post_hip.py`; `python/sglang/kernels/ops/mamba/csrc/mamba_state_indices_hip.cu`; `python/sglang/kernels/ops/mamba/mamba_state_indices.py`; `python/sglang/kernels/ops/mamba/mamba_state_indices_hip.py`; `python/sglang/srt/distributed/parallel_state.py` 等 12 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `5b6302252` - fix(hcu): keep packed FP8 Q on the old MLA path for Kimi K3 (#537)

- 完整 hash: `5b630225295b1bc1e510cfb5fd25e8f9521acef8`
- 时间/作者: 2026-10-15 / lipenghui
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/hcu_mla_backend.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/attention/hcu_mla_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `ae065131d` - feat(kimi-k3): add opt-in serial shared-expert overlap for DeepEP (#540)

- 完整 hash: `ae065131d82c45bf7135761091fb77b718c5df66`
- 时间/作者: 2026-10-16 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/k3_sbo_gemm.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/kimi_k3.py`, `test/manual/hcu/test_kimi_k3_serial_sbo.py`, `test/registered/unit/models/test_kimi_k3_serial_sbo.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/layers/k3_sbo_gemm.py`
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`
  - tests: `test/manual/hcu/test_kimi_k3_serial_sbo.py`; `test/registered/unit/models/test_kimi_k3_serial_sbo.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `da90edf06` - fix(k3): fix aiter ar shape mismatch and some entries accept rate=1 (#546)

- 完整 hash: `da90edf068c9a574c3a9e3e7ad69229440edfa01`
- 时间/作者: 2026-10-16 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/logits_processor.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/layers/logits_processor.py`
  - runtime-perf: `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `e7fb26db7` - fix(acc): fix k3-int4 tp16 acc wrong (#587)

- 完整 hash: `e7fb26db710c97fd1e445eef9df3a7ca71b26ccf`
- 时间/作者: 2026-10-23 / daishiqiang
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/kimi_k3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/kimi_k3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
