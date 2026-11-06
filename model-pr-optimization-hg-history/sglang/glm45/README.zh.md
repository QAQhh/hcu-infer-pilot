# sglang GLM-4.5 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| - | 无本地独有提交 |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 0
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| - | - | - | no local-only commit found | - |

## 逐 Commit 审计卡

### 本地提交检索结论

- 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；当前基线历史中没有保留的本地独有提交。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## v0.5.12_dev 到 release/20260825_v0.5.18 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-03
- 本章节提交数: 2（其中 merge 0）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/glm4_moe.py` | `1e2fec228`, `3604cec31` |
| `python/sglang/check_env.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/attn.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/elementwise.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/gemm.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/moe.py` | `1e2fec228` |
| `python/sglang/jit_kernel/fp8_blockwise_gemm.py` | `1e2fec228` |
| `python/sglang/jit_kernel/include/sgl_kernel/tensor.h` | `1e2fec228` |
| `python/sglang/jit_kernel/mxfp8.py` | `1e2fec228` |
| `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` | `1e2fec228` |
| `python/sglang/jit_kernel/trtllm_lora_temp/jit.py` | `1e2fec228` |
| `python/sglang/kernels/ops/layernorm/mhc.py` | `1e2fec228` |
| `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | `1e2fec228` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228` |
| `python/sglang/kernels/ops/speculative/cache_locs.py` | `1e2fec228` |
| `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py` | `1e2fec228` |
| `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py` | `1e2fec228` |
| `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` | `1e2fec228` |
| `python/sglang/srt/arg_groups/overrides.py` | `1e2fec228` |
| `python/sglang/srt/batch_overlap/single_batch_overlap.py` | `1e2fec228` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `1e2fec228` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` | `1e2fec228` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228` |
| `python/sglang/srt/environ.py` | `1e2fec228` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/aiter_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/index_buf_accessor.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/tilelang_kernel.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/triton_kernel.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsv4/metadata.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `1e2fec228` |
| ... | 另有 70 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-10-13 | `3604cec31` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): 修复 GLM W4A8 target 的 BF16 MTP 加载与 DeepEP 通信 (#520) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/glm4_moe.py` |

### 逐 Commit 审计卡

#### Commit `1e2fec228` - feat(hcu): port runtime and kernel rename

- 完整 hash: `1e2fec228a9a8b1e781c3592eff356eeb8b584ed`
- 时间/作者: 2026-07-20 / tianlinyang77
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/jit_kernel/dsv4/moe.py`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/mxfp8.py` 等 109 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/check_env.py`; `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/fp8_blockwise_gemm.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/mxfp8.py`; `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` 等 80 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `sgl-kernel/tests/test_moe_align.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `3604cec31` - fix(hcu): 修复 GLM W4A8 target 的 BF16 MTP 加载与 DeepEP 通信 (#520)

- 完整 hash: `3604cec316cca9c1b9fb8da2e5d1a5a7d59e92a2`
- 时间/作者: 2026-10-13 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/glm4_moe.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/models/glm4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
