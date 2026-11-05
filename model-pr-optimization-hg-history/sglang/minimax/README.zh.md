# sglang MiniMax M2 Series 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/minimax_m2.py` | `18944a9d3` |

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
| 2026-04-23 | `18944a9d3` | 模型支持/运行时入口 | support MiniMax M2.5 PP | `python/sglang/srt/models/minimax_m2.py` |

## 逐 Commit 审计卡

### Commit `18944a9d3` - support MiniMax M2.5 PP

- 完整 hash: `18944a9d392690db20f30c060b33d18e8bf9062c`
- 时间/作者: 2026-04-23 / guizhh
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/minimax_m2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/minimax_m2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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
- 本章节提交数: 21（其中 merge 3）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
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
| ... | 另有 332 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` 等 109 个文件 |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` 等 91 个文件 |
| 2026-08-07 | `4d9f46783` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | [BugFix] fix the lmslim and lightop calling issues regressions | `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py` 等 6 个文件 |
| 2026-08-07 | `2b4271498` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | ci(hcu): publish nine-model accuracy results | `.github/workflows/nightly-test-hcu.yml`, `scripts/ci/hcu/hcu_ci_notify_feishu.py`, `scripts/ci/hcu/test_hcu_ci_notify_feishu.py` 等 11 个文件 |
| 2026-08-10 | `d76d3f185` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | Adapt MiniMax-H3 for v0.5.15 | `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py` 等 84 个文件 |
| 2026-08-10 | `abe7d784d` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | Merge pull request #182 from HYGON-AI/sglang_minimax-h3-adapt | 无直接文件变更/merge |
| 2026-08-20 | `12c25ba52` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [fix][minimax-h3]: fix HCU QK-Norm fallback and backend resolution | `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` |
| 2026-08-20 | `56a4faa68` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [fix][minimax-h3]: default HCU component attention backends | `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py` |
| 2026-08-24 | `0d49fbb93` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #215 from s1mplezpc/zhangpc3_minimax_h3_dev | 无直接文件变更/merge |
| 2026-08-25 | `e04856c1d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(minimax-h3): allow HCU full-loop denoise | `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` |
| 2026-08-25 | `ce113101c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(minimax-h3): avoid sharing refined prompts with CacheDiT | `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` |
| 2026-08-26 | `530d6363b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #231 from s1mplezpc/0518-minimaxh3-dev | 无直接文件变更/merge |
| 2026-09-20 | `c496509fb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(mmgen): declare MiniMax H3 request extensions in the OpenAPI document (#399) | `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py` 等 4 个文件 |
| 2026-09-23 | `2df2a10f8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(mmgen): align MiniMax H3 OpenAPI contract (#426) | `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py` |
| 2026-09-30 | `8effe1350` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(minimax-m3): optimize prefill and decode on HCU gfx938 (#453) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py` 等 140 个文件 |
| 2026-10-14 | `5f31aec46` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(aiter): avoid duplicate MoE weights outside MiniMax-M3 (#526) | `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/models/minimax_m3.py` 等 6 个文件 |
| 2026-10-14 | `0ac3b2f83` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(MiniMax-H3): support MiniMax-H3 channel-wise INT8/FP8 inference on HCU (#532) | `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h` 等 9 个文件 |
| 2026-10-21 | `cda280cdf` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Fix] moe: Restrict DeepEPMoE runner delegation to MiniMax-M3 (#577) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py` 等 4 个文件 |
| 2026-10-23 | `a12acccb2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(minimax-h3): avoid full-video clone in VAE postprocessing (#583) | `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py` |
| 2026-10-31 | `5c859fcfd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Fix] minimax-h3: prevent repeated-request OOM and fix row-quantization dispatch (#629) | `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` 等 6 个文件 |
| 2026-11-03 | `729879dce` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Fix] quantization: 修复 INT4/INT8 混合量化模型加载 (#631) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py` |

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

#### Commit `123e9539e` - fix lint: satisfy pre-commit on the forward-port diff

- 完整 hash: `123e9539ea23dde2f1a12b0374c1375bbfb10989`
- 时间/作者: 2026-07-31 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py` 等 91 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py` 等 14 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py` 等 19 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py` 等 56 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_mmlu.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4d9f46783` - [BugFix] fix the lmslim and lightop calling issues regressions

- 完整 hash: `4d9f467839a30162175d1cfc7e0d0f11862fcffd`
- 时间/作者: 2026-08-07 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/fused_moe_int8_marlin_for_minimax_m2.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/layers/quantization/w8a8_int8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

#### Commit `d76d3f185` - Adapt MiniMax-H3 for v0.5.15

- 完整 hash: `d76d3f185d95025e63aad11ee3f65abe4b78f37e`
- 时间/作者: 2026-08-10 / yuchenyang
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py`, `python/sglang/kernels/ops/diffusion/triton/indexed_modulation.py`, `python/sglang/kernels/ops/diffusion/triton/scale_shift.py`, `python/sglang/kernels/ops/layernorm/norm.py`, `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/configs/models/encoders/minimax_h3_qwen3vl.py` 等 84 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`; `python/sglang/multimodal_gen/runtime/pipelines/minimax_h3_pipeline.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/decoding.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/__init__.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/canvas.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/condition_noise.py` 等 35 个文件
  - runtime-model: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/configs/models/encoders/minimax_h3_qwen3vl.py`; `python/sglang/multimodal_gen/configs/models/vaes/minimax_h3_audio.py`; `python/sglang/multimodal_gen/configs/models/vaes/minimax_h3_contract.py`; `python/sglang/multimodal_gen/configs/models/vaes/minimax_h3_video.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`; `python/sglang/multimodal_gen/configs/sample/minimax_h3.py` 等 28 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`; `python/sglang/kernels/ops/activation/activation.py`; `python/sglang/kernels/ops/diffusion/qknorm_rope.py`; `python/sglang/kernels/ops/diffusion/triton/indexed_modulation.py`; `python/sglang/kernels/ops/diffusion/triton/scale_shift.py`; `python/sglang/kernels/ops/layernorm/norm.py`; `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py` 等 15 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_minimax_h3_admission.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_denoise_loop.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_media.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_packed_sequence.py`; `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vae_parallel_modes.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `abe7d784d` - Merge pull request #182 from HYGON-AI/sglang_minimax-h3-adapt

- 完整 hash: `abe7d784d82c304000ad760af13356f2d74f56fd`
- 时间/作者: 2026-08-10 / lizhigong
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `12c25ba52` - [fix][minimax-h3]: fix HCU QK-Norm fallback and backend resolution

- 完整 hash: `12c25ba52859ab130655399e9c1750879bee7d7e`
- 时间/作者: 2026-08-20 / zhangpc3
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `56a4faa68` - [fix][minimax-h3]: default HCU component attention backends

- 完整 hash: `56a4faa68a55f3ab300d32156f6860578dc10503`
- 时间/作者: 2026-08-20 / zhangpc3
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`
  - tests: `python/sglang/multimodal_gen/test/unit/test_server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `0d49fbb93` - Merge pull request #215 from s1mplezpc/zhangpc3_minimax_h3_dev

- 完整 hash: `0d49fbb937fbed3909361ae2f4cb9996177d321a`
- 时间/作者: 2026-08-24 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `e04856c1d` - fix(minimax-h3): allow HCU full-loop denoise

- 完整 hash: `e04856c1d4613fcfbc39aa0ed88bc5d3ad5153d7`
- 时间/作者: 2026-08-25 / Codex
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `ce113101c` - fix(minimax-h3): avoid sharing refined prompts with CacheDiT

- 完整 hash: `ce113101ca7d946ccd9ef0a1db8c1d876b7c7c19`
- 时间/作者: 2026-08-25 / zhangpc3
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `530d6363b` - Merge pull request #231 from s1mplezpc/0518-minimaxh3-dev

- 完整 hash: `530d6363b30262d10286610938a45e8219306784`
- 时间/作者: 2026-08-26 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `c496509fb` - fix(mmgen): declare MiniMax H3 request extensions in the OpenAPI document (#399)

- 完整 hash: `c496509fbbf73b0acb7875652cf640791a778294`
- 时间/作者: 2026-09-20 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`, `python/sglang/srt/function_call/function_call_parser.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`; `python/sglang/srt/function_call/function_call_parser.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `2df2a10f8` - fix(mmgen): align MiniMax H3 OpenAPI contract (#426)

- 完整 hash: `2df2a10f818a0bf88a2a0b6ac97a3dd919b608f6`
- 时间/作者: 2026-09-23 / Phy
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `8effe1350` - feat(minimax-m3): optimize prefill and decode on HCU gfx938 (#453)

- 完整 hash: `8effe13508725f3c871dceb5dfbfbbfc6f959a89`
- 时间/作者: 2026-09-30 / WenQ7
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py`, `python/sglang/benchmark/serving.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/activation.cu`, `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`, `python/sglang/kernels/aot/include/utils.h` 等 140 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/minimax_router_gemv.py`
  - other: `python/sglang/benchmark/serving.py`; `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/eplb/eplb_manager.py`; `python/sglang/srt/eplb/expert_distribution.py`; `python/sglang/srt/eplb/expert_location_dispatch.py`; `python/sglang/srt/eplb/load_aware_dispatch.py`; `python/sglang/srt/eplb/lplb_solver.py` 等 19 个文件
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`; `python/sglang/srt/model_executor/cpu_graph_runner.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/runner/eager_runner.py`; `python/sglang/srt/models/llama_eagle3.py` 等 14 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/activation.cu`; `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`; `python/sglang/kernels/aot/include/utils.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`; `python/sglang/kernels/jit/csrc/moe/moe_topk_sigmoid.cuh` 等 65 个文件
  - tests: `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`; `test/registered/attention/test_verify_shared_kv.py`; `test/registered/cp/test_cp_strategy_unit.py`; `test/registered/kernels/ops/attention/test_minimax_prefill_grouped_union.py`; `test/registered/kernels/ops/attention/test_verify_mla_split_policy.py`; `test/registered/kernels/ops/kvcache/test_scaled_fp8_kv_store.py`; `test/registered/kernels/ops/speculative/test_draft_extend_kv_metadata.py` 等 39 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `5f31aec46` - fix(aiter): avoid duplicate MoE weights outside MiniMax-M3 (#526)

- 完整 hash: `5f31aec46b5e557fc00e891e8d91bcdb2e4c6b3b`
- 时间/作者: 2026-10-14 / WenQ7
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/unit/layers/moe/test_aiter_runner.py`, `test/registered/unit/layers/moe/test_aiter_weight_layout.py`, `test/registered/unit/models/test_minimax_m3_eplb.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/minimax_m3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/aiter.py`; `python/sglang/srt/layers/moe/moe_runner/base.py`
  - tests: `test/registered/unit/layers/moe/test_aiter_runner.py`; `test/registered/unit/layers/moe/test_aiter_weight_layout.py`; `test/registered/unit/models/test_minimax_m3_eplb.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `0ac3b2f83` - feat(MiniMax-H3): support MiniMax-H3 channel-wise INT8/FP8 inference on HCU (#532)

- 完整 hash: `0ac3b2f83eb8c7a57f534810c035dc0feb973cd3`
- 时间/作者: 2026-10-14 / s1mplezpc
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h`, `python/sglang/kernels/aot/setup_hip.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` 等 9 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vit_utils.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `cda280cdf` - [Fix] moe: Restrict DeepEPMoE runner delegation to MiniMax-M3 (#577)

- 完整 hash: `cda280cdf5a9a968536cb3ae8b5fdb7a4c586d05`
- 时间/作者: 2026-10-21 / WenQ7
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`, `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-model: `python/sglang/srt/models/minimax_m3.py`
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`
  - tests: `test/registered/unit/layers/moe/test_hcu_deepgemm_runner.py`; `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `a12acccb2` - fix(minimax-h3): avoid full-video clone in VAE postprocessing (#583)

- 完整 hash: `a12acccb2237d008407061130053e6135701a05b`
- 时间/作者: 2026-10-23 / s1mplezpc
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

#### Commit `5c859fcfd` - [Fix] minimax-h3: prevent repeated-request OOM and fix row-quantization dispatch (#629)

- 完整 hash: `5c859fcfdba2ff1089f223612ec292b8365a1b47`
- 时间/作者: 2026-10-31 / s1mplezpc
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`
  - runtime-perf: `python/sglang/multimodal_gen/runtime/layers/quantization/minimax_h3_quant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `729879dce` - [Fix] quantization: 修复 INT4/INT8 混合量化模型加载 (#631)

- 完整 hash: `729879dce06763c0ed7b15c5edca084a69557507`
- 时间/作者: 2026-11-03 / Songge
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`, `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py`
  - tests: `test/registered/unit/models/test_minimax_m3_hcu_moe_routing.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## release/20260825_v0.5.18 到 release_v0.5.18_deepseekv4 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 0（其中 merge 0）
- 分支更新段: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

- 该分支更新段内没有归入本桶的本地独有提交。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
