

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
# sglang 未归属具体模型的本地独有提交索引

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
- 本章节提交数: 122（其中 merge 113）
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `test/registered/unit/function_call/test_function_call_parser.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `test/registered/unit/managers/test_mm_process_config.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `test/registered/unit/model_loader/test_modelopt_loader.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `test/registered/unit/server_args/test_server_args.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `test/run_suite.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `.github/workflows/hcu-full-enabled.yml` | `c43b06722`, `b97d7df6e`, `b7bd14f19`, `b781224d4` |
| `.github/workflows/pr-test-hcu.yml` | `c43b06722`, `b97d7df6e`, `b7bd14f19`, `b781224d4` |
| `README.md` | `c43b06722`, `b97d7df6e`, `b781224d4`, `16d7caa10` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/distributed/parallel_state.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/environ.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/activation.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/layernorm.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/moe/mega_moe.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/moe/topk.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/quantization/fp8.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/model_loader/loader.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/models/deepseek_v2.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/models/deepseek_v4.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/models/minimax_m2.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/models/qwen3_5.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/server_args.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `python/sglang/srt/utils/common.py` | `b97d7df6e`, `b781224d4`, `ba31df0c0`, `16d7caa10` |
| `test/registered/attention/test_deterministic.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| `test/registered/lora/test_lora_openai_api.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| `test/registered/model_loading/test_external_models.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| `test/registered/openai_server/function_call/test_anthropic_tool_use.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| `test/registered/openai_server/validation/test_large_max_new_tokens.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| `test/registered/openai_server/validation/test_matched_stop.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| `test/registered/profiling/test_start_profile.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| `test/registered/radix_cache/test_radix_attention.py` | `c43b06722`, `b7bd14f19`, `b781224d4`, `16d7caa10` |
| ... | 另有 3798 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | `0fc998757` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C01 | 无直接文件变更/merge |
| 2026-06-23 | `571813832` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C02 | 无直接文件变更/merge |
| 2026-06-24 | `8303d60f7` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C03 | 无直接文件变更/merge |
| 2026-06-30 | `810624fbe` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C04 | 无直接文件变更/merge |
| 2026-06-30 | `08c1fd5a0` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C05 | 无直接文件变更/merge |
| 2026-07-01 | `16cff03a2` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C06 | 无直接文件变更/merge |
| 2026-07-02 | `593df5e14` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C07 | 无直接文件变更/merge |
| 2026-07-03 | `01f8caf22` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C08 | 无直接文件变更/merge |
| 2026-07-06 | `2ada58179` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C09 | 无直接文件变更/merge |
| 2026-07-07 | `5f232f552` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoint C10 | 无直接文件变更/merge |
| 2026-07-08 | `bae695b56` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main checkpoints C11-C13 | 无直接文件变更/merge |
| 2026-07-08 | `293fa64f0` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge commit '2ad00faae1f4f413330fbc1241dc2c79f44ac4d4' into sync/official-main-C14-C16-20260616 | 无直接文件变更/merge |
| 2026-07-09 | `15abf620c` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official SGLang C17-C19 into DCU bootstrap | 无直接文件变更/merge |
| 2026-07-09 | `76d14014a` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main bootstrap C01-C19 into main | 无直接文件变更/merge |
| 2026-07-09 | `d8f3057b3` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main catchup 20260623 into DCU main | 无直接文件变更/merge |
| 2026-07-13 | `b9cf8ac56` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main catchup 20260625 into DCU main | 无直接文件变更/merge |
| 2026-07-13 | `dcd4013b3` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official SGLang main through 2026-06-29 | 无直接文件变更/merge |
| 2026-07-13 | `c4de02791` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official SGLang main through 2026-07-03 | 无直接文件变更/merge |
| 2026-07-14 | `f96aaeb79` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main catch-up through 20260706 | 无直接文件变更/merge |
| 2026-07-14 | `6cd17f3e3` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official SGLang main through 2026-07-09 | 无直接文件变更/merge |
| 2026-07-14 | `1a2c734e5` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main catch-up through 20260710 | 无直接文件变更/merge |
| 2026-07-15 | `9ec22c5c9` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge sync/official-main-catchup-20260710 into main | 无直接文件变更/merge |
| 2026-07-15 | `7fa6d89c3` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main catch-up through 20260712 | 无直接文件变更/merge |
| 2026-07-15 | `4cc240b90` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main catch-up through 20260713 | 无直接文件变更/merge |
| 2026-07-15 | `21a4a455e` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge official main through v0.5.15.post1 equivalent | 无直接文件变更/merge |
| 2026-07-15 | `d67c7e44e` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 1 | 无直接文件变更/merge |
| 2026-07-15 | `d71a069b7` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 2 | 无直接文件变更/merge |
| 2026-07-15 | `0d3dbd7ab` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 3 | 无直接文件变更/merge |
| 2026-07-16 | `69315951c` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 4 | 无直接文件变更/merge |
| 2026-07-16 | `bdd8d46cc` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev step 5 | 无直接文件变更/merge |
| 2026-07-16 | `7df16485f` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): land v0.5.12_dev forward-port on main | 无直接文件变更/merge |
| 2026-07-20 | `c43b06722` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci(hcu): port v0.5.12 wheel staging gate | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 372 个文件 |
| 2026-07-21 | `2d509d387` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | Merge pull request #113 from HYGON-AI/v0.5.15.post1_dev_rye_megamoe_cp | 无直接文件变更/merge |
| 2026-07-22 | `e20e686c7` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge: sync v0.5.15.post1_dev into HCU port | 无直接文件变更/merge |
| 2026-07-22 | `f0d6741cc` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): forward-port v0.5.12_dev daily 20260722 | 无直接文件变更/merge |
| 2026-07-22 | `c32209f6d` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | Merge pull request #115 from HYGON-AI/v0.5.15_dev_lzg | 无直接文件变更/merge |
| 2026-07-22 | `1f3d470dc` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(dcu): integrate origin/v0.5.15.post1_dev PR#115 into forward-port 20260722 | 无直接文件变更/merge |
| 2026-07-23 | `599610198` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | merge: sync latest v0.5.15.post1_dev into HCU port | 无直接文件变更/merge |
| 2026-07-23 | `bee4b423f` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | Merge pull request #114 from HYGON-AI/hcu/v0.5.15.post1-port | 无直接文件变更/merge |
| 2026-07-29 | `d42b0a3bf` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(hcu): forward-port v0.5.12_dev daily 20260729 | 无直接文件变更/merge |
| 2026-07-29 | `cce4bdd61` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge pull request #148 from HYGON-AI/ci/align-workflows-v0515-0729 | 无直接文件变更/merge |
| 2026-08-03 | `d08093cb4` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | Merge pull request #158 from HYGON-AI/lvj-repox-patch-1 | 无直接文件变更/merge |
| 2026-08-03 | `b97d7df6e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | Forward port/v0.5.12 dev daily 20260729 (#146) | `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml` 等 184 个文件 |
| 2026-08-06 | `b91477f29` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | chore(hcu): anchor forward-port base to ac04c9cb (no content change) | 无直接文件变更/merge |
| 2026-08-06 | `4da105483` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | merge(hcu): forward-port v0.5.12_dev daily 20260806 (ac04c9cb..b1b81c18f) | 无直接文件变更/merge |
| 2026-08-06 | `34b6864a2` | `v0.5.12_dev..v0.5.15.post1_dev` | 通用实现调整 | Merge pull request #173 from HYGON-AI/forward-port/v0.5.12-dev-daily-20260806 | 无直接文件变更/merge |
| 2026-08-07 | `654ff007e` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | [BugFix] fix the lmslim and lightop calling issues regressions (#176) | 无直接文件变更/merge |
| 2026-08-07 | `b7bd14f19` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci(hcu): normalize HCU suite names | `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml` 等 199 个文件 |
| 2026-08-11 | `ad1fea5d7` | `v0.5.12_dev..v0.5.15.post1_dev` | 测试/文档/基准 | Merge pull request #177 from HYGON-AI/hcu/align-v0515-ci | 无直接文件变更/merge |
| 2026-08-12 | `856b425b8` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | Merge pull request #185 from HYGON-AI/v0.5.15.post1_dev_rye_dspark_bugfix | 无直接文件变更/merge |
| 2026-08-12 | `74e12e1e8` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | Merge pull request #189 from HYGON-AI/hcu/fix-ciupload-v0515 | 无直接文件变更/merge |
| 2026-08-13 | `97a1938e2` | `v0.5.12_dev..v0.5.15.post1_dev` | 缺陷修复 | Merge pull request #192 from HYGON-AI/rye_dspark_bugfix | 无直接文件变更/merge |
| 2026-07-21 | `4859ed3b8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge official main daily 20260721 | 无直接文件变更/merge |
| 2026-07-24 | `b781224d4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Rename DCU integration to HCU and sanitize runtime logs | `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml` 等 466 个文件 |
| 2026-07-24 | `cb01580d4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #124 from HYGON-AI/sanitize-hcu-runtime-log-audit-20260723 | 无直接文件变更/merge |
| 2026-07-27 | `49764eb37` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #131 from HYGON-AI/lvjia-repoguy-patch-1 | 无直接文件变更/merge |
| 2026-07-29 | `ba31df0c0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Sync/official main daily 20260728 (#136) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` 等 1924 个文件 |
| 2026-07-29 | `3bd903cb2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge pull request #147 from HYGON-AI/ci/align-workflows-main-0729 | 无直接文件变更/merge |
| 2026-08-04 | `8bb597e2c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'd703c086ff42655c602b85c9f0ac935215f8c4cc' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `2ceaca5ef` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '2d509d387218fb0e71ca4880cba8c56570316ab3' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `050d160da` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'f0d6741cc1fc14ad8d74a12777345d23ec8ed7fc' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `4315f50a0` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '1f3d470dc5ff3365a87ae317ea12ef341335fffe' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `9c451b2d2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '9fc04a7a2cebc525a96301d3e8e9515bb0a5b4b6' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `7ac99d59b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'c43b06722' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `1462076bb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '1e2fec228' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `de2659dc6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '358a33714' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `bb91d55c7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '416bbd9b9' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `515526331` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '81e3561ae' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `0792d89a9` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '811aa027d' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `235a6b991` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '15a656ea6' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `b2e118b59` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '9864c8451' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `a822ab35c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '9b86479ac' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `8bb3f9ecb` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'ac56ca009' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `d91d2c7d7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'bee4b423f68fa27792f5d8ed79eb9ecbb5e0f4e6' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `f628e2a98` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '7482123c3' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `128f5f73b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '0710e82a0' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `fc4bd96f4` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit '997e64560' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `19889fe0e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'cce4bdd61' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `e1ad3a989` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'e7106de94' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `9e305f571` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'd08093cb4' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `74d439192` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'de696eab9' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-04 | `9dda7e375` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge commit 'b97d7df6e' into forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-06 | `1672d9e47` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #170 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260804 | 无直接文件变更/merge |
| 2026-08-07 | `eda349619` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | chore(hcu): anchor daily sync base to official edc0e5489 (no content change) | 无直接文件变更/merge |
| 2026-08-10 | `80e01615e` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Sync/official main daily 20260807 | 无直接文件变更/merge |
| 2026-08-10 | `37b7742e7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Sync/official main 20260810 (v0.5.17) | 无直接文件变更/merge |
| 2026-08-10 | `6f86e904d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge pull request #179 from HYGON-AI/sync/official-main-20260810 | 无直接文件变更/merge |
| 2026-08-10 | `8f7a660e5` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge pull request #183 from HYGON-AI/sync/official-main-20260810 | 无直接文件变更/merge |
| 2026-08-12 | `5daa79af7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | merge(hcu): forward-port v0.5.15.post1_dev through 20260811 | 无直接文件变更/merge |
| 2026-08-12 | `9b76db90d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #184 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260811 | 无直接文件变更/merge |
| 2026-08-14 | `1c349c31f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | merge(hcu): forward-port v0.5.15.post1_dev through 20260813 | 无直接文件变更/merge |
| 2026-08-17 | `d95af36e1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #206 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260813 | 无直接文件变更/merge |
| 2026-08-17 | `9f4368f10` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | merge(hcu): backport official main through 20260817 (92b1d382c7) | 无直接文件变更/merge |
| 2026-08-17 | `d20a4750f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge pull request #208 from HYGON-AI/backport/official-main-20260817 | 无直接文件变更/merge |
| 2026-08-24 | `2e8f1408b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #214 from Crowder13/main | 无直接文件变更/merge |
| 2026-08-25 | `16d7caa10` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | sync(hcu): official main through 20260824 (c8e1ddc707) | `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md` 等 1857 个文件 |
| 2026-08-25 | `dd41b1f06` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge |
| 2026-08-25 | `97aa7a298` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #224 from dddddddxl/hcu/fork-pr-target | 无直接文件变更/merge |
| 2026-08-25 | `4eacd3c36` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge |
| 2026-08-25 | `8ba0c9376` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #226 from dddddddxl/hcu/allow-fork-checkout | 无直接文件变更/merge |
| 2026-08-25 | `7481b1f54` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge branch 'main' into sync/official-main-daily-20260824 | 无直接文件变更/merge |
| 2026-08-25 | `a3cfa2a97` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge pull request #222 from RyeYuan/sync/official-main-daily-20260824 | 无直接文件变更/merge |
| 2026-08-25 | `688659c15` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Merge pull request #228 from dddddddxl/hcu/dynamic-runner-ownership | 无直接文件变更/merge |
| 2026-08-26 | `89d8ac7b1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #233 from Crowder13/release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-26 | `700dd657d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge pull request #237 from HYGON-AI/zyh/test-release-workflow | 无直接文件变更/merge |
| 2026-08-26 | `5f2c97ef7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 测试/文档/基准 | Merge pull request #239 from dddddddxl/hcu/enable-v0518-ci | 无直接文件变更/merge |
| 2026-08-27 | `91856a154` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Merge pull request #245 from dddddddxl/hcu/fix-safe-directory-v0518 | 无直接文件变更/merge |
| 2026-08-27 | `d92a60a7f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #250 from aivictor0901-tech/release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `3cf589201` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #253 from aivictor0901-tech/release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `8a65f5ecd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge branch 'HYGON-AI:release/20260825_v0.5.18' into release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `b4b3aaee6` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge branch 'HYGON-AI:release/20260825_v0.5.18' into release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `52cddf2fa` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `45c5fad8d` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `1cac982c2` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `c16848ebe` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #251 from wufan-ToBeWater/release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-28 | `72dac21ce` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | [bugfix] torchaudio版本装的不对 (#257) | `docker/hcu.Dockerfile` |
| 2026-08-29 | `1b8d95c85` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #258 from aivictor0901-tech/release/20260825_v0.5.18 | 无直接文件变更/merge |
| 2026-08-31 | `2d4eb83cc` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Merge pull request #261 from xinleishang/fix/20260829_v0.5.18_hicache_pp | 无直接文件变更/merge |
| 2026-08-31 | `6378905dc` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 通用实现调整 | Merge pull request #270 from dddddddxl/hcu/remove-amd-pr-state-v0518 | 无直接文件变更/merge |
| 2026-08-31 | `84a65ccdd` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Merge pull request #271 from xingjinliang/fix/dismatch-shape-of-one-step-off-policy | 无直接文件变更/merge |
| 2026-09-02 | `f5a24dc84` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 模型支持/运行时入口 | [FEATURE]0.5.18镜像新增安装nixl (#283) | `docker/hcu.Dockerfile` |
| 2026-09-07 | `cd8f78f01` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): include MLA absorb q kernel in HIP build (#293) |  |

### 逐 Commit 审计卡

- 时间线列出全部 122 个提交；审计卡只保留最近的 80 个。

#### Commit `b97d7df6e` - Forward port/v0.5.12 dev daily 20260729 (#146)

- 完整 hash: `b97d7df6ee606d51c8a96b07b447b1a536a7e0af`
- 时间/作者: 2026-08-03 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-feishu-notify-preview.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `.github/workflows/quality-baseline-scan.yml`, `.github/workflows/release-pr-hcu.yml`, `README.md`, `README_DCU.md` 等 184 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/hcu-feishu-notify-preview.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`; `.github/workflows/quality-baseline-scan.yml`; `.github/workflows/release-pr-hcu.yml`
  - docs-bench: `docs/dcu-pr-ci-visual-guide.html`; `docs/hcu-pr-ci-visual-guide.html`; `docs/internal/dcu-main-conflict-ledger.md`
  - other: `README.md`; `README_DCU.md`; `THIRD_PARTY_NOTICES.md`; `python/sglang/check_env.py`; `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`; `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`; `python/sglang/multimodal_gen/runtime/loader/utils.py` 等 32 个文件
  - runtime-model: `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`; `python/sglang/multimodal_gen/configs/sample/ltx_2.py`; `python/sglang/multimodal_gen/configs/sample/sampling_params.py`; `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`; `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/multimodal_gen/runtime/server_args/server_args.py`; `python/sglang/srt/configs/model_config.py` 等 33 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/add_constant.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh` 等 101 个文件
  - tests: `python/sglang/multimodal_gen/test/server/test_server_common.py`; `python/sglang/multimodal_gen/test/server/test_server_utils.py`; `python/sglang/test/hcu_accuracy_report.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_server_guard.py`; `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py` 等 9 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `b91477f29` - chore(hcu): anchor forward-port base to ac04c9cb (no content change)

- 完整 hash: `b91477f2961992d12adb427475d633118cdc9fe3`
- 时间/作者: 2026-08-06 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `4da105483` - merge(hcu): forward-port v0.5.12_dev daily 20260806 (ac04c9cb..b1b81c18f)

- 完整 hash: `4da105483f725fb89c5689a4f299abb09f305571`
- 时间/作者: 2026-08-06 / RyeYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `34b6864a2` - Merge pull request #173 from HYGON-AI/forward-port/v0.5.12-dev-daily-20260806

- 完整 hash: `34b6864a208cb053f0dffaec4f54ea0df0d4788a`
- 时间/作者: 2026-08-06 / lizhigong
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `654ff007e` - [BugFix] fix the lmslim and lightop calling issues regressions (#176)

- 完整 hash: `654ff007ee5e1f60aee5b7a07a42fcac7a61ff93`
- 时间/作者: 2026-08-07 / YuanYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `b7bd14f19` - ci(hcu): normalize HCU suite names

- 完整 hash: `b7bd14f19898fe547e644590f0096bef715f0072`
- 时间/作者: 2026-08-07 / LvJIA-RG
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `README_HCU.md`, `scripts/ci/hcu/hcu_ci_pd.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_deterministic.py` 等 199 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - other: `README_HCU.md`; `scripts/ci/hcu/hcu_ci_pd.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_deterministic.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py`; `test/registered/attention/test_pack_paged_kv_to_varlen.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py` 等 194 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

#### Commit `ad1fea5d7` - Merge pull request #177 from HYGON-AI/hcu/align-v0515-ci

- 完整 hash: `ad1fea5d74f6264de5734bee8971bbade980343d`
- 时间/作者: 2026-08-11 / dingxinlong
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `856b425b8` - Merge pull request #185 from HYGON-AI/v0.5.15.post1_dev_rye_dspark_bugfix

- 完整 hash: `856b425b86102879467e89dc3912c76af654643c`
- 时间/作者: 2026-08-12 / YuanYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `74e12e1e8` - Merge pull request #189 from HYGON-AI/hcu/fix-ciupload-v0515

- 完整 hash: `74e12e1e8fbd5e38be975645f64355df8b671e57`
- 时间/作者: 2026-08-12 / lizhigong
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `97a1938e2` - Merge pull request #192 from HYGON-AI/rye_dspark_bugfix

- 完整 hash: `97a1938e2bd04cffd7f07570e7d91679034c4dbc`
- 时间/作者: 2026-08-13 / YuanYuan
- 分支更新段: `v0.5.12_dev..v0.5.15.post1_dev`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `4859ed3b8` - Merge official main daily 20260721

- 完整 hash: `4859ed3b833fd6c505d8740b7ef879b35cf0857f`
- 时间/作者: 2026-07-21 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `b781224d4` - Rename DCU integration to HCU and sanitize runtime logs

- 完整 hash: `b781224d4dae58889ba9bcc3efc0ff20fb424dc4`
- 时间/作者: 2026-07-24 / LvJIA-RG
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `.github/open-source-compliance.json`, `.github/workflows/dcu-full-enabled.yml`, `.github/workflows/dcu-manual-model-test.yml`, `.github/workflows/hcu-full-enabled.yml`, `.github/workflows/hcu-manual-model-test.yml`, `.github/workflows/labeler.yml`, `.github/workflows/lint-dcu.yml`, `.github/workflows/lint-hcu.yml` 等 466 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/open-source-compliance.json`; `.github/workflows/dcu-full-enabled.yml`; `.github/workflows/dcu-manual-model-test.yml`; `.github/workflows/hcu-full-enabled.yml`; `.github/workflows/hcu-manual-model-test.yml`; `.github/workflows/labeler.yml`; `.github/workflows/lint-dcu.yml`; `.github/workflows/lint-hcu.yml` 等 14 个文件
  - docs-bench: `docs/dcu-pr-ci-visual-guide.html`; `docs/hcu-pr-ci-visual-guide.html`
  - other: `NOTICE`; `README.md`; `README_DCU.md`; `README_HCU.md`; `THIRD_PARTY_NOTICES.md`; `python/sglang/check_env.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py` 等 33 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/pool_configurator.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/compress.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`; `python/sglang/kernels/ops/attention/dsa/tilelang_kernel.py` 等 77 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `python/sglang/test/ci/ci_register.py`; `python/sglang/test/dcu_cookbook_utils.py`; `python/sglang/test/dcu_utils.py`; `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_utils.py`; `python/sglang/test/simple_eval_mmmu_vlm.py`; `python/sglang/test/test_utils.py` 等 326 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `cb01580d4` - Merge pull request #124 from HYGON-AI/sanitize-hcu-runtime-log-audit-20260723

- 完整 hash: `cb01580d4618170ce8b9f3713b766508ca81782d`
- 时间/作者: 2026-07-24 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `49764eb37` - Merge pull request #131 from HYGON-AI/lvjia-repoguy-patch-1

- 完整 hash: `49764eb373aef40ab1809215717d7c2222cfc5d8`
- 时间/作者: 2026-07-27 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `ba31df0c0` - Sync/official main daily 20260728 (#136)

- 完整 hash: `ba31df0c0da941467ef94a6c114a375af39b488f`
- 时间/作者: 2026-07-29 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-review-pr/SKILL.md`, `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md` 等 1924 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/MAINTAINER.md`; `.github/labeler.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/diffusion-ci-gt-gen-npu.yml`; `.github/workflows/diffusion-ci-gt-gen.yml`; `.github/workflows/lint.yml` 等 28 个文件
  - docs-bench: `benchmark/bench_linear_attention/bench_cutedsl_kda_decode.py`; `benchmark/bench_linear_attention/bench_gdn_qkv_split.py`; `benchmark/hicache/bench_hicache_write_back.py`; `benchmark/hicache/perf.py`; `benchmark/kernels/all_reduce/benchmark_fused_ar_rms_quant_amd.py`; `benchmark/kernels/bench_fused_gate_sigmoid_mul_add.py`; `benchmark/kernels/bench_fused_sigmoid_mul.py`; `benchmark/kernels/deepseek/benchmark_cute_dsl_fp8_paged_mqa_logits.py` 等 47 个文件
  - other: `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`; `.claude/skills/cookbook-migrate-model/SKILL.md`; `.claude/skills/cookbook-review-pr/SKILL.md`; `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`; `3rdparty/amd/wheel/sglang/pyproject.toml`; `docker/Dockerfile`; `python/pyproject.toml` 等 159 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `python/sglang/multimodal_gen/runtime/models/dits/krea2.py`; `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`; `python/sglang/multimodal_gen/runtime/models/dits/sana_wm_components.py`; `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`; `python/sglang/multimodal_gen/runtime/models/vaes/hunyuanvae.py`; `python/sglang/srt/configs/load_config.py` 等 74 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `python/sglang/jit_kernel/.clang-format`; `python/sglang/jit_kernel/__init__.py`; `python/sglang/jit_kernel/__main__.py`; `python/sglang/jit_kernel/activation.py`; `python/sglang/jit_kernel/add_constant.py` 等 1037 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/deepseek_v4/__init__.py`; `python/sglang/jit_kernel/tests/deepseek_v4/common.py`; `python/sglang/jit_kernel/tests/kv_canary/__init__.py`; `python/sglang/jit_kernel/tests/kv_canary/_canary_helpers.py`; `python/sglang/jit_kernel/tests/kv_canary/_constants.py`; `python/sglang/jit_kernel/tests/kv_canary/_differential.py`; `python/sglang/jit_kernel/tests/kv_canary/_fixtures.py` 等 579 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `3bd903cb2` - Merge pull request #147 from HYGON-AI/ci/align-workflows-main-0729

- 完整 hash: `3bd903cb2346916401221961348f8ec8a736d1b1`
- 时间/作者: 2026-07-29 / dddddddxl
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `8bb597e2c` - Merge commit 'd703c086ff42655c602b85c9f0ac935215f8c4cc' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `8bb597e2c956c7758fab3907f35e60e10fde68b9`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `2ceaca5ef` - Merge commit '2d509d387218fb0e71ca4880cba8c56570316ab3' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `2ceaca5ef2cf2a735ca187a1655db3f7387b3346`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `050d160da` - Merge commit 'f0d6741cc1fc14ad8d74a12777345d23ec8ed7fc' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `050d160dafdfa4e406ca9afa988f5593f9d4b20e`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `4315f50a0` - Merge commit '1f3d470dc5ff3365a87ae317ea12ef341335fffe' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `4315f50a076ba0bc2d56ebdd0fcd4f7b96af4e8e`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `9c451b2d2` - Merge commit '9fc04a7a2cebc525a96301d3e8e9515bb0a5b4b6' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `9c451b2d26be1dc7eb84b3b5a5ff5b5ded6fa98f`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `7ac99d59b` - Merge commit 'c43b06722' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `7ac99d59b3ba889e0e6975e6e3576caf30d134af`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `1462076bb` - Merge commit '1e2fec228' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `1462076bbac783eda6f9c8e7352668f44dd0b8e0`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `de2659dc6` - Merge commit '358a33714' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `de2659dc628759ae256f67ce14ffb0eccf1b10aa`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `bb91d55c7` - Merge commit '416bbd9b9' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `bb91d55c7ab3b90cc09139d5f6c1b92301ee46fe`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `515526331` - Merge commit '81e3561ae' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `5155263318cf7b01fa78ed0606f330b9e76d7db4`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `0792d89a9` - Merge commit '811aa027d' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `0792d89a997bdc052b84469179e107928543c521`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `235a6b991` - Merge commit '15a656ea6' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `235a6b99156b98a95255264a42741465a0c534c5`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `b2e118b59` - Merge commit '9864c8451' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `b2e118b59a6f7a5762e70e821a430d3ff525894d`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `a822ab35c` - Merge commit '9b86479ac' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `a822ab35c92cc04fdbe4952d559d5fcff7471898`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `8bb3f9ecb` - Merge commit 'ac56ca009' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `8bb3f9ecbb788865a359428361afbb60833f303b`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `d91d2c7d7` - Merge commit 'bee4b423f68fa27792f5d8ed79eb9ecbb5e0f4e6' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `d91d2c7d72c8aa86fd871a978e82fc989663c03a`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `f628e2a98` - Merge commit '7482123c3' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `f628e2a9840d4dd0ef850f8fe8a193761b01b27a`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `128f5f73b` - Merge commit '0710e82a0' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `128f5f73b6ff1885819fe35889a076ab1cc57b41`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `fc4bd96f4` - Merge commit '997e64560' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `fc4bd96f4346ee32b05f9713b4c2e5aa3f3a584c`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `19889fe0e` - Merge commit 'cce4bdd61' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `19889fe0e241c5613ddcd3db6c82b2a11d01b36e`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `e1ad3a989` - Merge commit 'e7106de94' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `e1ad3a98986cfb1809b1ec5999e62029786d0cda`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `9e305f571` - Merge commit 'd08093cb4' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `9e305f5717087f05b2f415bd641e4c4d903dbdb3`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `74d439192` - Merge commit 'de696eab9' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `74d439192d38be421aecd837ae692785ca5bface`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `9dda7e375` - Merge commit 'b97d7df6e' into forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `9dda7e375e0a8a8815ebacafec60cb8015cd77c3`
- 时间/作者: 2026-08-04 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `1672d9e47` - Merge pull request #170 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260804

- 完整 hash: `1672d9e470a59c952e881dfebe9bae6ac914656e`
- 时间/作者: 2026-08-06 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `eda349619` - chore(hcu): anchor daily sync base to official edc0e5489 (no content change)

- 完整 hash: `eda349619bd4ca60246bea0a2623c4b494bd7ea9`
- 时间/作者: 2026-08-07 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `80e01615e` - Sync/official main daily 20260807

- 完整 hash: `80e01615e8ea05d69b290ee983490bf4f44c599e`
- 时间/作者: 2026-08-10 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `37b7742e7` - Sync/official main 20260810 (v0.5.17)

- 完整 hash: `37b7742e7e55116c01f8565fe578b2478c476560`
- 时间/作者: 2026-08-10 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `6f86e904d` - Merge pull request #179 from HYGON-AI/sync/official-main-20260810

- 完整 hash: `6f86e904d21870cf1f638e4713725ecca120f757`
- 时间/作者: 2026-08-10 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `8f7a660e5` - Merge pull request #183 from HYGON-AI/sync/official-main-20260810

- 完整 hash: `8f7a660e58527db05b130f5609d95b86885f84da`
- 时间/作者: 2026-08-10 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `5daa79af7` - merge(hcu): forward-port v0.5.15.post1_dev through 20260811

- 完整 hash: `5daa79af74da9583663ed20eb29779320ce7bece`
- 时间/作者: 2026-08-12 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `9b76db90d` - Merge pull request #184 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260811

- 完整 hash: `9b76db90d66ff3f0379f66a52b24102bf7fb264d`
- 时间/作者: 2026-08-12 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `1c349c31f` - merge(hcu): forward-port v0.5.15.post1_dev through 20260813

- 完整 hash: `1c349c31fc7f51c71c63d812b1213b3fe1f47edf`
- 时间/作者: 2026-08-14 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `d95af36e1` - Merge pull request #206 from HYGON-AI/forward-port/v0.5.15-post1-dev-20260813

- 完整 hash: `d95af36e1331aa3c7064eb837dd7103b6406b8a8`
- 时间/作者: 2026-08-17 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `9f4368f10` - merge(hcu): backport official main through 20260817 (92b1d382c7)

- 完整 hash: `9f4368f104fbf93f744eafef685ebe8f8a94ff3c`
- 时间/作者: 2026-08-17 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `d20a4750f` - Merge pull request #208 from HYGON-AI/backport/official-main-20260817

- 完整 hash: `d20a4750f11e581c0691752f3d6b7389312a6819`
- 时间/作者: 2026-08-17 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `2e8f1408b` - Merge pull request #214 from Crowder13/main

- 完整 hash: `2e8f1408b42432408dc0087dec9f8520204d5a75`
- 时间/作者: 2026-08-24 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `16d7caa10` - sync(hcu): official main through 20260824 (c8e1ddc707)

- 完整 hash: `16d7caa1065abd2af782f3afc35c3dc4da745cde`
- 时间/作者: 2026-08-25 / RyeYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: `.claude/rules/comment-style.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/references/diffusion-authoring.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/diffusion-page.mdx.tmpl` 等 1857 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/labeler.yml`; `.github/update_ci_permission.py`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 42 个文件
  - docs-bench: `benchmark/hicache/bench_buffer_mode.py`; `docs/cookbook/autoregressive/Baidu/PaddleOCR-VL.mdx`; `docs/cookbook/autoregressive/Baidu/Unlimited-OCR.mdx`; `docs/cookbook/autoregressive/DeepReinforce/Ornith-1.0.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-4.6V.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/Google/Gemma4.mdx` 等 115 个文件
  - other: `.claude/rules/comment-style.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-add-model/references/diffusion-authoring.md`; `.claude/skills/cookbook-add-model/templates/diffusion-page.mdx.tmpl`; `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`; `.claude/skills/sglang-runtime-context/SKILL.md` 等 288 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.claude/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/sgl-kv-indexer/.gitignore`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml` 等 257 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `python/sglang/kernel_api_logging.py`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/cpu/activation.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 453 个文件
  - tests: `experimental/sgl-router/sgl-kv-indexer/tests/common/id.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/common/net.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/memory_integration.rs`; `experimental/sgl-router/tests/component/policies/cache_aware_zmq.rs`; `experimental/sgl-router/tests/e2e/chat_completions/test_two_router_convergence.py`; `experimental/sgl-router/tests/e2e/infra/gateway.py` 等 702 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `dd41b1f06` - Merge branch 'main' into sync/official-main-daily-20260824

- 完整 hash: `dd41b1f06dee84cdb3a77eb2a4c3cdd64306bebc`
- 时间/作者: 2026-08-25 / YuanYuan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `97aa7a298` - Merge pull request #224 from dddddddxl/hcu/fork-pr-target

- 完整 hash: `97aa7a298a3274cddc7b19c55123fed05e112336`
- 时间/作者: 2026-08-25 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `4eacd3c36` - Merge branch 'main' into sync/official-main-daily-20260824

- 完整 hash: `4eacd3c36d9ee880fae87ea072e22fb5bf641b30`
- 时间/作者: 2026-08-25 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `8ba0c9376` - Merge pull request #226 from dddddddxl/hcu/allow-fork-checkout

- 完整 hash: `8ba0c9376f157769b4fd8bccb560af739b61d15b`
- 时间/作者: 2026-08-25 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `7481b1f54` - Merge branch 'main' into sync/official-main-daily-20260824

- 完整 hash: `7481b1f5430eb91025166a3f0a6a9e920ef8348a`
- 时间/作者: 2026-08-25 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `a3cfa2a97` - Merge pull request #222 from RyeYuan/sync/official-main-daily-20260824

- 完整 hash: `a3cfa2a979442d114187460e31d42f3fb4744441`
- 时间/作者: 2026-08-25 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `688659c15` - Merge pull request #228 from dddddddxl/hcu/dynamic-runner-ownership

- 完整 hash: `688659c15694195ee0c6fab18de26b60b313b82f`
- 时间/作者: 2026-08-25 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `89d8ac7b1` - Merge pull request #233 from Crowder13/release/20260825_v0.5.18

- 完整 hash: `89d8ac7b1d97151c0389e34cc9f4d097fce7ef99`
- 时间/作者: 2026-08-26 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `700dd657d` - Merge pull request #237 from HYGON-AI/zyh/test-release-workflow

- 完整 hash: `700dd657dce63efa2b6869e337a8522705b5acdd`
- 时间/作者: 2026-08-26 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `5f2c97ef7` - Merge pull request #239 from dddddddxl/hcu/enable-v0518-ci

- 完整 hash: `5f2c97ef71d6adce5c910a0a78054bb27dcdf3c0`
- 时间/作者: 2026-08-26 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 测试/文档/基准
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `91856a154` - Merge pull request #245 from dddddddxl/hcu/fix-safe-directory-v0518

- 完整 hash: `91856a15449b4aeaf8dbc6c6ed73681b86d03f1d`
- 时间/作者: 2026-08-27 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `d92a60a7f` - Merge pull request #250 from aivictor0901-tech/release/20260825_v0.5.18

- 完整 hash: `d92a60a7f0500b0d022aaeefaadb02f59c0e903f`
- 时间/作者: 2026-08-27 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `3cf589201` - Merge pull request #253 from aivictor0901-tech/release/20260825_v0.5.18

- 完整 hash: `3cf5892012c37f06edb9f1e495a2cbb2b872038c`
- 时间/作者: 2026-08-28 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `8a65f5ecd` - Merge branch 'HYGON-AI:release/20260825_v0.5.18' into release/20260825_v0.5.18

- 完整 hash: `8a65f5ecd8ec0ea9cac3add863bda1f18578d994`
- 时间/作者: 2026-08-28 / wufan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `b4b3aaee6` - Merge branch 'HYGON-AI:release/20260825_v0.5.18' into release/20260825_v0.5.18

- 完整 hash: `b4b3aaee6e8f6bfe75965f70d1382e0a49e6cf28`
- 时间/作者: 2026-08-28 / wufan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `52cddf2fa` - Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18

- 完整 hash: `52cddf2fa5a5f2a3a00b782f52af82b9659f87b4`
- 时间/作者: 2026-08-28 / wufan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `45c5fad8d` - Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18

- 完整 hash: `45c5fad8de90135528ff9e02e94a46f4f770774d`
- 时间/作者: 2026-08-28 / wufan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `1cac982c2` - Merge branch 'release/20260825_v0.5.18' of github.com:wufan-ToBeWater/sglang-das into release/20260825_v0.5.18

- 完整 hash: `1cac982c2125bee1bda17c1a8472302dd66e9b74`
- 时间/作者: 2026-08-28 / wufan
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `c16848ebe` - Merge pull request #251 from wufan-ToBeWater/release/20260825_v0.5.18

- 完整 hash: `c16848ebe82f2466525eb44f4ca369d948ad4301`
- 时间/作者: 2026-08-28 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `72dac21ce` - [bugfix] torchaudio版本装的不对 (#257)

- 完整 hash: `72dac21ce7211142fe7194f932a9cafdde7d6be6`
- 时间/作者: 2026-08-28 / Crowder13
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `1b8d95c85` - Merge pull request #258 from aivictor0901-tech/release/20260825_v0.5.18

- 完整 hash: `1b8d95c85b5a2442939ccc5abc0225b1a7e943f3`
- 时间/作者: 2026-08-29 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `2d4eb83cc` - Merge pull request #261 from xinleishang/fix/20260829_v0.5.18_hicache_pp

- 完整 hash: `2d4eb83cc759a3e318b287cb37efc64bf8f8099c`
- 时间/作者: 2026-08-31 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `6378905dc` - Merge pull request #270 from dddddddxl/hcu/remove-amd-pr-state-v0518

- 完整 hash: `6378905dc61607a8ad0f04db03b078379da14692`
- 时间/作者: 2026-08-31 / Lvjiajia
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `84a65ccdd` - Merge pull request #271 from xingjinliang/fix/dismatch-shape-of-one-step-off-policy

- 完整 hash: `84a65ccddc0ba1bc553012a5497bdc8b54069f79`
- 时间/作者: 2026-08-31 / lizhigong
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `f5a24dc84` - [FEATURE]0.5.18镜像新增安装nixl (#283)

- 完整 hash: `f5a24dc843be70821c51186c22c4211b7326646d`
- 时间/作者: 2026-09-02 / Crowder13
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 模型支持/运行时入口
- 主要文件: `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `cd8f78f01` - fix(hcu): include MLA absorb q kernel in HIP build (#293)

- 完整 hash: `cd8f78f01f9b6cc9f379e7393a369f378eab35c2`
- 时间/作者: 2026-09-07 / maxiaobetter
- 分支更新段: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- 自动分类: 性能/后端优化
- 主要文件: 未记录文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## release/20260825_v0.5.18 到 release_v0.5.18_deepseekv4 本地独有提交补充

### 覆盖说明

- 来源仓库: `HYGON-AI/sglang-das`；分支端点: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交；合并提交也保留。
- 生成日期: 2026-11-05
- 本章节提交数: 27（其中 merge 13）
- 分支更新段: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- 归类说明: 命中具体模型名、模型文件的提交进入对应模型桶（可同时进入多个）；其余运行时、后端、CI、测试提交进入 `shared`；仅有 merge 或无相关路径的提交进入 `unclassified`。改动文件数超过 150 的批量同步/重命名提交（如整合官方 main 的 squash 同步）也只进入 `unclassified`，其内容含上游代码，不能当作本地独有实现。自动归类，未逐条人工审阅 diff。

### 涉及文件

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/arg_groups/overrides.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/arg_groups/parallel_hook.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/disaggregation/decode.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/disaggregation/prefill.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/disaggregation/utils.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/entrypoints/http_server.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/entrypoints/openai/serving_chat.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/environ.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/attention/dsa/utils.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/attention/linear/kda_backend.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/dp_attention.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/moe/topk.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/managers/schedule_batch.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/managers/scheduler.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/model_executor/model_runner.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/models/deepseek_v2.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/models/deepseek_v4.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/speculative/eagle_worker_v2.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/utils/common.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/arg_groups/field_order.py` | `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/arg_groups/model_hook.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490` |
| `python/sglang/srt/arg_groups/pd_disaggregation_hook.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490` |
| `python/sglang/srt/arg_groups/pipeline.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/arg_groups/speculative_hook.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490` |
| `python/sglang/srt/configs/model_config.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490` |
| `python/sglang/srt/disaggregation/common/conn.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/disaggregation/nixl/conn.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/distributed/parallel_state.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/cp/utils.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/layernorm.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `6049c219e`, `ab43824b0`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/logits_processor.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `ab43824b0`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` | `50bacb028`, `ee0f2375e`, `ca25bc427`, `16229e94d`, `6049c219e`, `756ae5b4f`, `36b93840b`, `4975d6490`, `5f67ce01c` |
| ... | 另有 9137 个文件未列出 |

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-08-24 | `4a540f118` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge |
| 2026-08-24 | `7676961ba` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge |
| 2026-08-25 | `d445b357f` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge |
| 2026-08-26 | `ed9037191` | `release/20260825_v0.5.18..main` | 缺陷修复 | Merge pull request #238 from dddddddxl/hcu/fix-bash-shell-main | 无直接文件变更/merge |
| 2026-08-26 | `c832752c7` | `release/20260825_v0.5.18..main` | 通用实现调整 | Merge remote-tracking branch 'origin/main' into review/pr-230 | 无直接文件变更/merge |
| 2026-08-26 | `26c6e0fb3` | `release/20260825_v0.5.18..main` | 通用实现调整 | Merge pull request #230 from reverie-hub/hcu/sanitize-runtime | 无直接文件变更/merge |
| 2026-08-27 | `a15b56677` | `release/20260825_v0.5.18..main` | 通用实现调整 | Merge branch 'HYGON-AI:main' into main | 无直接文件变更/merge |
| 2026-08-27 | `fd402a780` | `release/20260825_v0.5.18..main` | 缺陷修复 | Merge pull request #246 from dddddddxl/hcu/fix-safe-directory-main | 无直接文件变更/merge |
| 2026-08-27 | `dc7b624e9` | `release/20260825_v0.5.18..main` | 通用实现调整 | Merge branch 'HYGON-AI:main' into main | 无直接文件变更/merge |
| 2026-08-28 | `13c60ec0d` | `release/20260825_v0.5.18..main` | 通用实现调整 | Merge pull request #254 from Crowder13/main | 无直接文件变更/merge |
| 2026-08-31 | `5cf052bd0` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Merge branch 'main' into feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge |
| 2026-08-31 | `20ee2b297` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Merge pull request #216 from Zhuwenbopro/feature/aiter-adaptation-zhuwenbo | 无直接文件变更/merge |
| 2026-08-31 | `cc6b7c948` | `release/20260825_v0.5.18..main` | 通用实现调整 | Merge pull request #269 from dddddddxl/hcu/remove-amd-pr-state-main | 无直接文件变更/merge |
| 2026-09-01 | `50bacb028` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/official main daily 20260831 (#273) | `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml` 等 1435 个文件 |
| 2026-09-03 | `d150cf2ac` | `release/20260825_v0.5.18..main` | 缺陷修复 | [BUGFIX]torchaudio使用hcu的版本 (#298) | `docker/hcu.Dockerfile` |
| 2026-09-07 | `df05aa9f9` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE] daily镜像里面加装ai-dynamo (#313) | `docker/hcu.Dockerfile` |
| 2026-09-08 | `ee0f2375e` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/official main daily 20260907 (#328) | `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` 等 3600 个文件 |
| 2026-09-14 | `ca25bc427` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/official main daily 20260914 (#362) | `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md` 等 1792 个文件 |
| 2026-09-20 | `16229e94d` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/official main daily 20260920 (#410) | `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md` 等 1583 个文件 |
| 2026-09-23 | `2f9a696ab` | `release/20260825_v0.5.18..main` | 测试/文档/基准 | [FEATURE] 基础镜像内置 shca 驱动 (#440) | `docker/hcu.Dockerfile` |
| 2026-09-28 | `6049c219e` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Glm5.3 flash (#427) | `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc` 等 196 个文件 |
| 2026-09-29 | `ab43824b0` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/official main daily 20260928 (#452) | `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md` 等 2902 个文件 |
| 2026-09-30 | `756ae5b4f` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/20260929 rye rel 2 main (#470) | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml` 等 313 个文件 |
| 2026-10-08 | `5cf6ed7f7` | `release/20260825_v0.5.18..main` | 性能/后端优化 | [BUGFIX]镜像增加安装megamoe (#479) | `docker/hcu.Dockerfile` |
| 2026-10-12 | `36b93840b` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/official main daily 20261009 (#500) | `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md` 等 3300 个文件 |
| 2026-10-20 | `4975d6490` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/official main daily 20261019 (#560) | `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md` 等 3006 个文件 |
| 2026-10-21 | `5f67ce01c` | `release/20260825_v0.5.18..main` | 性能/后端优化 | Sync/rel 2 main 20261021 dsv4 validated (#576) | `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore` 等 321 个文件 |

### 逐 Commit 审计卡

#### Commit `4a540f118` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- 完整 hash: `4a540f1186efe80fe46b6459c199f9d2f883974f`
- 时间/作者: 2026-08-24 / lizhigong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `7676961ba` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- 完整 hash: `7676961ba770d5327714e7220186a1943c25c594`
- 时间/作者: 2026-08-24 / lizhigong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `d445b357f` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- 完整 hash: `d445b357fd702592f289a6e72161901a72c69df0`
- 时间/作者: 2026-08-25 / lizhigong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `ed9037191` - Merge pull request #238 from dddddddxl/hcu/fix-bash-shell-main

- 完整 hash: `ed903719178b9f6592d9160aabedbd6d55679c12`
- 时间/作者: 2026-08-26 / Lvjiajia
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `c832752c7` - Merge remote-tracking branch 'origin/main' into review/pr-230

- 完整 hash: `c832752c72ec3fb573ca121d88e109940d621729`
- 时间/作者: 2026-08-26 / dddddddxl
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `26c6e0fb3` - Merge pull request #230 from reverie-hub/hcu/sanitize-runtime

- 完整 hash: `26c6e0fb3d9557be7c9f9a9a3b4ef48b1bbbb561`
- 时间/作者: 2026-08-26 / lizhigong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `a15b56677` - Merge branch 'HYGON-AI:main' into main

- 完整 hash: `a15b56677625f2f4c9906559376a97f70b86636e`
- 时间/作者: 2026-08-27 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `fd402a780` - Merge pull request #246 from dddddddxl/hcu/fix-safe-directory-main

- 完整 hash: `fd402a7803ec007123f6a201b8d27f73071b156a`
- 时间/作者: 2026-08-27 / Lvjiajia
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `dc7b624e9` - Merge branch 'HYGON-AI:main' into main

- 完整 hash: `dc7b624e97ff48076819a10c5a08f89f2a8dcc23`
- 时间/作者: 2026-08-27 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `13c60ec0d` - Merge pull request #254 from Crowder13/main

- 完整 hash: `13c60ec0d41c2880f2f4cd811f13a93cc9677684`
- 时间/作者: 2026-08-28 / lizhigong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `5cf052bd0` - Merge branch 'main' into feature/aiter-adaptation-zhuwenbo

- 完整 hash: `5cf052bd014a50378029315ef0654a2318badf1f`
- 时间/作者: 2026-08-31 / lizhigong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `20ee2b297` - Merge pull request #216 from Zhuwenbopro/feature/aiter-adaptation-zhuwenbo

- 完整 hash: `20ee2b297f01e602a640c9219d658c643b3c306c`
- 时间/作者: 2026-08-31 / lizhigong
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `cc6b7c948` - Merge pull request #269 from dddddddxl/hcu/remove-amd-pr-state-main

- 完整 hash: `cc6b7c9481e9696bdeea86a63f769ce835b03a4b`
- 时间/作者: 2026-08-31 / Lvjiajia
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 通用实现调整
- 主要文件: 无直接文件变更/merge
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 验证与风险: 合并提交本身没有直接文件 diff；实际内容以被合入分支上的提交为准。

#### Commit `50bacb028` - Sync/official main daily 20260831 (#273)

- 完整 hash: `50bacb028023ba6d0155267a7c0f7841d5ec3fd7`
- 时间/作者: 2026-09-01 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/nightly-test-npu.yml` 等 1435 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-stage.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`; `.github/workflows/nightly-test-npu.yml`; `.github/workflows/pr-test-amd-extra.yml` 等 21 个文件
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/lean_kernel_sweep.py`; `benchmark/unified_memory/bench_peer_aware_eviction.py`; `docs/cards/logos/ibm.png`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`; `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx` 等 100 个文件
  - other: `.claude/skills/sglang-runtime-context/SKILL.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134`; `docker/kimi_k3/apply_deepep_k3_patch.sh`; `docker/kimi_k3/kimi_k3_cu12.Dockerfile`; `docker/kimi_k3/kimi_k3_cu13.Dockerfile`; `docker/npu.Dockerfile`; `python/pyproject.toml` 等 299 个文件
  - runtime-model: `python/sglang/benchmark/one_batch_server.py`; `python/sglang/launch_server.py`; `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/configs/models/encoders/base.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan3d.py`; `python/sglang/multimodal_gen/configs/pipeline_configs/longcat_image.py` 等 133 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/cmake/flashmla.cmake`; `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce.cuh`; `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`; `python/sglang/kernels/aot/csrc/cpu/extend.cpp`; `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` 等 396 个文件
  - tests: `python/sglang/multimodal_gen/test/run_suite.py`; `python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py`; `python/sglang/multimodal_gen/test/server/ascend/perf_baselines_npu.json`; `python/sglang/multimodal_gen/test/server/ascend/test_glm_image_distributed.py`; `python/sglang/multimodal_gen/test/server/ascend/testcase_configs_npu.py`; `python/sglang/multimodal_gen/test/server/gpu_cases.py`; `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json`; `python/sglang/multimodal_gen/test/server/test_server_common.py` 等 486 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `d150cf2ac` - [BUGFIX]torchaudio使用hcu的版本 (#298)

- 完整 hash: `d150cf2acd16a9b416c399ab3662264684b3962b`
- 时间/作者: 2026-09-03 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 缺陷修复
- 主要文件: `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `df05aa9f9` - [FEATURE] daily镜像里面加装ai-dynamo (#313)

- 完整 hash: `df05aa9f9dac6b5fe4fd4ce3fd5ee86a35106b62`
- 时间/作者: 2026-09-07 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `ee0f2375e` - Sync/official main daily 20260907 (#328)

- 完整 hash: `ee0f2375e5fb285e4fb021a9831fa88018244679`
- 时间/作者: 2026-09-08 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`, `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`, `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py` 等 3600 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/_pr-test-rust-ext-build.yml`; `.github/workflows/_pr-test-simulator-cpu.yml` 等 43 个文件
  - docs-bench: `benchmark/asr/bench_sglang.py`; `benchmark/bench_linear_attention/bench_kda_flashinfer_mtp.py`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_client.py`; `benchmark/hf3fs/bench_storage.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/hicache/bench_mix.py`; `benchmark/hicache/bench_multiturn.py` 等 133 个文件
  - other: `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_proof_generator.py`; `.claude/skills/mechanical-refactor-verify/scripts/mechanical_refactor_reproduction_utils.py`; `.claude/skills/sglang-prod-incident-triage/scripts/incident_artifact_tool.py`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.git-blame-ignore-revs`; `.gitignore` 等 510 个文件
  - runtime-model: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.pre-commit-config.yaml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/policy_select.rs`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/sgl-kv-indexer/Cargo.toml`; `experimental/sgl-router/sgl-kv-indexer/README.md` 等 402 个文件
  - runtime-perf: `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `3rdparty/amd/wheel/sgl-kernel/rocm_hipify.py`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/policies/cache_aware_zmq.rs`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `python/sglang/kernels/aot/benchmark/bench_amd_deterministic_allreduce.py` 等 683 个文件
  - tests: `.claude/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_cli/cli_testlib.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_add_imports.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_extract_symbols_to_new_module.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_assign.py`; `.claude/skills/mechanical-refactor-verify/scripts/tests/reproduction_utils/test_move_symbol.py`; `experimental/sgl-router/sgl-kv-indexer/tests/common/kv.rs`; `experimental/sgl-router/sgl-kv-indexer/tests/grpc_contract.rs` 等 1829 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `ca25bc427` - Sync/official main daily 20260914 (#362)

- 完整 hash: `ca25bc4275b93e02a48a2f8158835f372fee3553`
- 时间/作者: 2026-09-14 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.claude/rules/unit-test-admission.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.codespellrc` 等 1792 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/FOLDER_README.md`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/workflows/_docker-build-and-publish.yml` 等 44 个文件
  - docs-bench: `benchmark/bench_linear_attention/bench_int8_checkpoint_reuse.py`; `benchmark/kernels/attention/bench_gdn_replayssm_decode.py`; `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/simulator/bench_runner.py`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx` 等 130 个文件
  - other: `.claude/rules/unit-test-admission.md`; `.claude/skills/cookbook-add-model/references/authoring-reference.md`; `.claude/skills/cookbook-migrate-model/SKILL.md`; `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.codespellrc`; `.gitleaksignore`; `3rdparty/amd/wheel/README.md` 等 284 个文件
  - runtime-model: `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/src/policies/buckets.rs`; `experimental/sgl-router/src/policies/mod.rs`; `experimental/sgl-router/src/proxy/mod.rs`; `experimental/sgl-router/src/proxy/sse.rs`; `experimental/sgl-router/src/server/metrics.rs`; `experimental/sgl-router/src/server/routes/chat.rs`; `python/sglang/launch_server.py` 等 148 个文件
  - runtime-perf: `3rdparty/amd/wheel/sgl-kernel/build_rocm.sh`; `3rdparty/amd/wheel/sgl-kernel/rename_wheels_rocm.sh`; `docker/patches/sgl-kernel-gfx1151.sh`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/cache_aware.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/Dockerfile` 等 412 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/proxy/bucket_routing.rs`; `experimental/sgl-router/tests/proxy/chat_routing.rs`; `python/sglang/kernels/aot/tests/test_awq_dequant.py`; `python/sglang/kernels/aot/tests/test_cutlass_mla.py`; `python/sglang/kernels/aot/tests/test_flash_attn_sparse.py`; `python/sglang/kernels/aot/tests/test_fused_qk_norm_rope.py` 等 774 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `16229e94d` - Sync/official main daily 20260920 (#410)

- 完整 hash: `16229e94d0a0a218875ab0db2133c12d9695abd1`
- 时间/作者: 2026-09-20 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/ci-test-audit/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 1583 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/workflows/_npu-single-node-test-stage.yml`; `.github/workflows/_pr-test-check-changes.yml`; `.github/workflows/amd-aiter-scout.yml`; `.github/workflows/amd-ci-job-monitor.yml`; `.github/workflows/bot-bump-sglang-version.yml`; `.github/workflows/ci-coverage-overview.yml` 等 26 个文件
  - docs-bench: `benchmark/agentic-rollout/README.md`; `benchmark/agentic-rollout/explore.py`; `benchmark/agentic-rollout/metrics.py`; `benchmark/agentic-rollout/plot.py`; `benchmark/agentic-rollout/simulate.py`; `benchmark/agentic-rollout/spec/README.md`; `benchmark/agentic-rollout/spec/evidence/feature-00-session-hicache-latency.md`; `benchmark/agentic-rollout/spec/feature-00-session-hicache-latency.md` 等 127 个文件
  - other: `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`; `.claude/skills/ci-test-audit/SKILL.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/sglang-runtime-context/SKILL.md`; `.gitignore`; `.gitleaksignore`; `docker/Dockerfile.cu134`; `docker/npu.Dockerfile` 等 217 个文件
  - runtime-model: `docker/sgl-router.Dockerfile`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/deny.toml`; `experimental/sgl-router/monitoring/README.md`; `experimental/sgl-router/monitoring/grafana-dashboard.json` 等 234 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `experimental/sgl-router/src/policies/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/cpu/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/cpu/bmm.cpp` 等 443 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `benchmark/agentic-rollout/tests/test_explore.py`; `benchmark/agentic-rollout/tests/test_simulate.py`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/bucket_domains.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs`; `experimental/sgl-router/tests/component/policies/kv_events_two_subscribers.rs`; `experimental/sgl-router/tests/component/policies/zmq_helpers.rs` 等 536 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `2f9a696ab` - [FEATURE] 基础镜像内置 shca 驱动 (#440)

- 完整 hash: `2f9a696abd7055f8cdc545b168b1bcd730cc6109`
- 时间/作者: 2026-09-23 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 测试/文档/基准
- 主要文件: `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `6049c219e` - Glm5.3 flash (#427)

- 完整 hash: `6049c219ec044420bbacce7eddfe7ae31e031625`
- 时间/作者: 2026-09-28 / leon.wang
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/kpool_write_plan.cu`, `python/sglang/kernels/aot/csrc/elementwise/topk.hip`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h`, `python/sglang/kernels/aot/python/sgl_kernel/__init__.py` 等 196 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/__init__.py`; `python/sglang/srt/arg_groups/fields/parallel.py`; `python/sglang/srt/arg_groups/fields/serving.py`; `python/sglang/srt/arg_groups/fields/spec.py`; `python/sglang/srt/arg_groups/model_hook.py`; `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`; `python/sglang/srt/arg_groups/overrides.py` 等 73 个文件
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/glm5_next.py`; `python/sglang/srt/configs/mamba_utils.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/disaggregation/encoder/server.py`; `python/sglang/srt/entrypoints/anthropic/serving.py`; `python/sglang/srt/entrypoints/engine.py`; `python/sglang/srt/entrypoints/http_server.py` 等 33 个文件
  - runtime-perf: `python/sglang/kernels/aot/CMakeLists.txt`; `python/sglang/kernels/aot/csrc/common_extension.cc`; `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/kpool_write_plan.cu`; `python/sglang/kernels/aot/csrc/elementwise/topk.hip`; `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/python/sgl_kernel/__init__.py` 等 88 个文件
  - tests: `test/manual/test_hcu_delta_rule_cuda.py`; `test/registered/quant/test_fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `ab43824b0` - Sync/official main daily 20260928 (#452)

- 完整 hash: `ab43824b09055fc790bd5a9166a6a6182b1bccc3`
- 时间/作者: 2026-09-29 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.claude/rules/cookbook-first.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/clean-startup-log/SKILL.md`, `.claude/skills/clean-startup-log/references/noise-sources.md`, `.claude/skills/cookbook-add-model/SKILL.md` 等 2902 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/MAINTAINER.md`; `.github/actions/check-pr-test-health/action.test.cjs`; `.github/actions/check-pr-test-health/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml` 等 42 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/disaggregation/bench_cached_prefix.py`; `benchmark/dllm/README.md`; `benchmark/dllm/bench_diffusion_gemma.py`; `benchmark/gsm8k/README.md`; `benchmark/gsm8k/bench_sglang.py`; `benchmark/hf3fs/bench_zerocopy.py`; `benchmark/io/bench_mm_token_padding.py` 等 209 个文件
  - other: `.claude/rules/cookbook-first.md`; `.claude/skills/ci-test-audit/action-items.md`; `.claude/skills/clean-startup-log/SKILL.md`; `.claude/skills/clean-startup-log/references/noise-sources.md`; `.claude/skills/cookbook-add-model/SKILL.md`; `.claude/skills/cookbook-review-pr/SKILL.md`; `.claude/skills/env-var-conventions/SKILL.md`; `.claude/skills/generate-profile/SKILL.md` 等 383 个文件
  - runtime-model: `.pre-commit-config.yaml`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/benches/tree_lookup.rs`; `experimental/sgl-router/monitoring/grafana-dashboard.json`; `experimental/sgl-router/src/buckets_reorg.rs` 等 312 个文件
  - runtime-perf: `.claude/skills/add-jit-kernel/SKILL.md`; `.claude/skills/add-sgl-kernel/SKILL.md`; `.claude/skills/kernel-organization/SKILL.md`; `docker/rocm-gfx1151.Dockerfile`; `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `python/sglang/kernels/README.md` 等 898 个文件
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/main.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/decode.rs`; `experimental/sgl-router/tests/component/policies/fused_score.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs` 等 1058 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `756ae5b4f` - Sync/20260929 rye rel 2 main (#470)

- 完整 hash: `756ae5b4fe26cf9ad666d46cda6c45b14b3abc60`
- 时间/作者: 2026-09-30 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/quality-gate.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `README_HCU.md`, `benchmark/eplb/README.md`, `benchmark/eplb/prepare_static_lp.py`, `benchmark/glm53/README.md`, `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py` 等 313 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/quality-gate.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/eplb/README.md`; `benchmark/eplb/prepare_static_lp.py`; `benchmark/glm53/README.md`; `benchmark/kernels/elementwise/benchmark_concat_mla_absorb_q_hcu.py`; `docs/internal/README_BF16_FLASHMLA.md`
  - other: `README_HCU.md`; `python/pyproject_hcu.toml`; `python/sglang/benchmark/datasets/generated_shared_prefix.py`; `python/sglang/benchmark/serving.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`; `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`; `python/sglang/srt/arg_groups/choices.py`; `python/sglang/srt/arg_groups/deepseek_v4_hook.py` 等 63 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`; `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`; `python/sglang/srt/configs/dspark.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py` 等 33 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/concat_mla_absorb_q_hcu.cu`; `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py`; `python/sglang/kernels/jit/csrc/deepseek_v4/common.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`; `python/sglang/kernels/jit/csrc/deepseek_v4/linear_bf16_fp32.cuh` 等 158 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_aime25.py`; `python/sglang/test/simple_eval_aime26.py`; `python/sglang/test/simple_eval_common.py`; `python/sglang/test/simple_eval_mmlu.py`; `test/hcu_humaneval_judge.py`; `test/manual/ep/test_kimi_k3_eplb.py`; `test/manual/layers/test_hy4_ihc_tilelang.py` 等 51 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `5cf6ed7f7` - [BUGFIX]镜像增加安装megamoe (#479)

- 完整 hash: `5cf6ed7f71fac8dab1983923c93e2d42074079c3`
- 时间/作者: 2026-10-08 / Crowder13
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `docker/hcu.Dockerfile`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - other: `docker/hcu.Dockerfile`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

#### Commit `36b93840b` - Sync/official main daily 20261009 (#500)

- 完整 hash: `36b93840b54b8c41fe395e6f3e3f9a5463fe17ba`
- 时间/作者: 2026-10-12 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-sgl-kernel/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`, `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`, `.agents/skills/ci-test-audit/SKILL.md`, `.agents/skills/ci-test-audit/action-items.md`, `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/clean-startup-log/SKILL.md` 等 3300 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.claude/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/check-maintenance/action.yml`; `.github/labeler.yml`; `.github/workflows/_npu-pr-test-stage.yml`; `.github/workflows/_npu-single-node-test-stage.yml` 等 38 个文件
  - docs-bench: `benchmark/deepseek_v3/README.md`; `benchmark/kernels/bench_block_verification.py`; `benchmark/kernels/fused_moe_triton/benchmark_sglang_fused_moe_triton.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/.mintignore`; `docs/cards/logos/gigachat.png`; `docs/cards/logos/iquestlab.png`; `docs/cards/logos/perplexity.png` 等 190 个文件
  - other: `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`; `.agents/skills/babysit-pr-to-pass-ci/agents/openai.yaml`; `.agents/skills/ci-test-audit/SKILL.md`; `.agents/skills/ci-test-audit/action-items.md`; `.agents/skills/clean-startup-log/SKILL.md`; `.agents/skills/clean-startup-log/references/noise-sources.md`; `.agents/skills/compute-mamba-ratio/SKILL.md`; `.agents/skills/cookbook-add-model/SKILL.md` 等 596 个文件
  - runtime-model: `.agents/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.agents/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`; `.agents/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`; `.claude/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`; `.claude/skills/llm-torch-profiler-analysis/scripts/probe_llm_server.py`; `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile` 等 470 个文件
  - runtime-perf: `.agents/skills/add-jit-kernel/SKILL.md`; `.agents/skills/add-sgl-kernel/SKILL.md`; `.agents/skills/debug-cuda-crash/SKILL.md`; `.agents/skills/debug-distributed-hang/SKILL.md`; `.agents/skills/kernel-organization/SKILL.md`; `.agents/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`; `.claude/rules/kernel-benchmark.md`; `.claude/skills/add-jit-kernel/SKILL.md` 等 816 个文件
  - tests: `.agents/skills/kl-consistency-test/SKILL.md`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/conftest.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/generator_testlib.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extract_functions.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_extracts.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_imports.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_infer_moves.py`; `.agents/skills/mechanical-refactor-verify/scripts/tests/proof_generator/test_main_single_commit.py` 等 1190 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `4975d6490` - Sync/official main daily 20261019 (#560)

- 完整 hash: `4975d6490ac2c71c2d88c8a86b96a6f7061050ab`
- 时间/作者: 2026-10-20 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/cookbook-add-model/SKILL.md`, `.agents/skills/generate-profile/SKILL.md`, `.agents/skills/processor-model-parity/SKILL.md`, `.agents/skills/write-sglang-test/SKILL.md`, `.claude/rules/prefer-sgl-eval.md`, `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS` 等 3006 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.agents/skills/ci-workflow-guide/SKILL.md`; `.github/CI_PERMISSIONS.json`; `.github/CODEOWNERS`; `.github/actions/download-rust-ext/action.yml`; `.github/actions/wait-for-jobs/action.yml`; `.github/labeler.yml`; `.github/pull_request_template.md`; `.github/scripts/pr-check-comment.cjs` 等 60 个文件
  - docs-bench: `benchmark/hicache/bench_host_memory_migration.py`; `benchmark/kernels/lora_csgmv/bench_csgmv_split_k.py`; `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`; `docs/cards/logos/cloudflare.png`; `docs/cards/logos/reflection.png`; `docs/cookbook/autoregressive/Cloudflare/clef.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`; `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx` 等 211 个文件
  - other: `.agents/skills/cookbook-add-model/SKILL.md`; `.agents/skills/generate-profile/SKILL.md`; `.agents/skills/processor-model-parity/SKILL.md`; `.claude/rules/prefer-sgl-eval.md`; `.gitignore`; `README.md`; `docker/Dockerfile`; `docker/Dockerfile.cu134` 等 521 个文件
  - runtime-model: `.pre-commit-config.yaml`; `docker/sgl-router.Dockerfile`; `experimental/sgl-router/ARCHITECTURE.md`; `experimental/sgl-router/Cargo.lock`; `experimental/sgl-router/Cargo.toml`; `experimental/sgl-router/POLICY_DESIGN.md`; `experimental/sgl-router/README.md`; `experimental/sgl-router/REFERENCE.md` 等 516 个文件
  - runtime-perf: `docker/rocm.Dockerfile`; `experimental/sgl-router/src/policies/scoring/prefix_cache.rs`; `experimental/sgl-router/src/policies_reorg/cache_aware.rs`; `experimental/sgl-router/src/server/routes/cache.rs`; `python/sglang/kernels/README.md`; `python/sglang/kernels/__init__.py`; `python/sglang/kernels/aot/benchmark/bench_dsv4_norm_rope.py`; `python/sglang/kernels/aot/benchmark/bench_flashmla_mega.py` 等 711 个文件
  - tests: `.agents/skills/write-sglang-test/SKILL.md`; `docs/scripts/tests/diffusion-builders.test.mjs`; `docs/scripts/tests/wan-animate-2-config.test.mjs`; `experimental/sgl-router/tests/component/discovery/static_urls.rs`; `experimental/sgl-router/tests/component/policies/cache_prefix_provider.rs`; `experimental/sgl-router/tests/component/policies/kv_events_hash_parity.rs`; `experimental/sgl-router/tests/component/policies/kv_events_peer_bootstrap.rs`; `experimental/sgl-router/tests/component/policies_reorg.rs` 等 987 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

#### Commit `5f67ce01c` - Sync/rel 2 main 20261021 dsv4 validated (#576)

- 完整 hash: `5f67ce01c3ec1894916d16627eaca4959fbe2d90`
- 时间/作者: 2026-10-21 / YuanYuan
- 分支更新段: `release/20260825_v0.5.18..main`
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-hcu.yml`, `.github/workflows/release-pypi-nightly-hcu.yml`, `.gitignore`, `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `benchmark/kernels/minimax_router_gemv.py`, `docs/internal/rel-2-main-20261020-release-updates.md`, `python/sglang/benchmark/serving.py` 等 321 个文件
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 涉及文件（按路径分组，未逐文件阅读）:
  - ci: `.github/workflows/pr-test-hcu.yml`; `.github/workflows/release-pypi-nightly-hcu.yml`
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`; `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`; `benchmark/kernels/minimax_router_gemv.py`; `docs/internal/rel-2-main-20261020-release-updates.md`
  - other: `.gitignore`; `python/sglang/benchmark/serving.py`; `python/sglang/multimodal_gen/envs.py`; `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`; `python/sglang/srt/arg_groups/field_order.py`; `python/sglang/srt/arg_groups/fields/exec_.py`; `python/sglang/srt/arg_groups/fields/memory.py`; `python/sglang/srt/arg_groups/fields/schedule.py` 等 56 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`; `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vit_utils.py`; `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`; `python/sglang/srt/model_executor/cpu_graph_runner.py`; `python/sglang/srt/model_executor/forward_batch_info.py` 等 26 个文件
  - runtime-perf: `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`; `python/sglang/kernels/aot/csrc/elementwise/activation.cu`; `python/sglang/kernels/aot/csrc/gemm/per_token_quant_fp8.cu`; `python/sglang/kernels/aot/csrc/sgl_diffusion/minimax_h3_rope.cu`; `python/sglang/kernels/aot/include/sgl_kernel_ops.h`; `python/sglang/kernels/aot/include/utils.h`; `python/sglang/kernels/aot/setup_hip.py`; `python/sglang/kernels/aot/setup_rocm.py` 等 131 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py`; `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `python/sglang/multimodal_gen/test/unit/test_wan_sla_layout.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`; `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_fp8_attn_gemm.py`; `python/sglang/test/few_shot_gsm8k.py`; `python/sglang/test/kits/linker_load_failure_kit.py`; `test/manual/hcu/test_kimi_k3_serial_sbo.py` 等 102 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
