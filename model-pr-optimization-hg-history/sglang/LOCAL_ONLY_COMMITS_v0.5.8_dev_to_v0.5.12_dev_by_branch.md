# SGLang v0.5.8_dev..v0.5.12_dev 分支更新本地独有提交索引

## 范围与口径

- 本地仓库: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 目标分支: `v0.5.8_dev`, `v0.5.9_dev`, `v0.5.10_dev`, `v0.5.11_dev`, `v0.5.12_dev`
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`, `v0.5.9_dev..v0.5.10_dev`, `v0.5.10_dev..v0.5.11_dev`, `v0.5.11_dev..v0.5.12_dev`
- 官方仓库: `https://github.com/sgl-project/sglang.git`
- 官方 refs: 已 fetch 到本地 `refs/remotes/github-official/*`
- 筛选方法: 每个分支更新段内，本地 commit hash 不可从官方 GitHub refs 到达，即记录为本地 fork 独有提交。
- 说明: 合并提交也保留；如果合并提交没有直接文件 diff，`主要涉及` 标记为 `无直接文件变更/merge`。

## 数量汇总

| 分支更新段 | 范围内提交数 | 本地独有提交数 |
| --- | ---: | ---: |
| `v0.5.8_dev..v0.5.9_dev` | 817 | 46 |
| `v0.5.9_dev..v0.5.10_dev` | 1456 | 26 |
| `v0.5.10_dev..v0.5.11_dev` | 937 | 4 |
| `v0.5.11_dev..v0.5.12_dev` | 515 | 30 |
| 合计 | 3725 | 106 |

## 重复检查

- 已对所有本地独有提交计算 `git patch-id --stable`。
- 发现 1 组完全相同 patch-id: `968d82d7f` 与 `b4a02fae7`，均为 `support mimo-v2-flash-int4 with triton attn`，分别出现在相邻分支更新段中。索引中均保留，并在备注列标记。
- 其他提交未发现完全相同 patch-id；标题相近的 LightOp、MHC、DeepSeek-V4 JIT、PD 修复属于连续补丁，内容不同。

## 提交索引

### `v0.5.8_dev..v0.5.9_dev`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 2026-02-27 | `155c1f634` | lizhigong | sglang dcu 0.5.9base patch->hash(5dd49e07) | python/sglang/bench_serving.py; python/sglang/srt/batch_overlap/single_batch_overlap.py; python/sglang/srt/batch_overlap/two_batch_overlap.py; ... 共 104 个文件 |  |
| 2026-02-27 | `1dd77c2e6` | lizhigong | Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev' | README_DCU.md; requirements_dcu.txt |  |
| 2026-02-27 | `356694d6b` | lizhigong | Merge branch 'cherry-pick-1dfc3015' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-02-27 | `403027fd8` | lizhigong | Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-02-27 | `8a6520cd8` | lizhigong | Merge branch 'cherry-pick-3b73900b' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-02-27 | `c77a90449` | lizhigong | Debugging through TP parallel | python/sglang/srt/layers/attention/flashattention_backend.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; sgl-kernel/setup_hip.py |  |
| 2026-02-27 | `d62ea43c1` | lizhigong | Merge branch 'v0.5.8_dev_niuhb' into 'v0.5.8_dev' | python/sglang/srt/layers/moe/token_dispatcher/deepep.py |  |
| 2026-03-06 | `4c7028bf2` | liucong | qwen系列模型算子融合 | python/sglang/srt/distributed/parallel_state.py; python/sglang/srt/environ.py; python/sglang/srt/layers/activation.py; ... 共 9 个文件 |  |
| 2026-03-06 | `a5c071e36` | lizhigong | Merge branch 'cherry-pick-fc0f9e89' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-06 | `b3f4b0861` | lizhigong | Merge branch 'v0.5.8_dev_sxl' into 'v0.5.8_dev' | python/sglang/srt/layers/attention/base_attn_backend.py; python/sglang/srt/layers/attention/dcu_mla_backend.py; python/sglang/srt/layers/attention/flashmla_backend.py; ... 共 12 个文件 |  |
| 2026-03-06 | `b930b5645` | liucong8560 | Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-07 | `5d7c6b671` | lizhigong | Merge branch 'v0.5.8_dev_mx' into 'v0.5.8_dev' | python/sglang/srt/batch_overlap/single_batch_overlap.py; python/sglang/srt/layers/moe/ep_moe/layer.py; python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py; ... 共 5 个文件 |  |
| 2026-03-07 | `686124d90` | liucong | 适配fuse_moe_fp8_w8a8 | python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py |  |
| 2026-03-07 | `76c737ac7` | liucong8560 | Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-07 | `8ba520fcc` | lizhigong | fix error when set dtype float16 | python/sglang/srt/layers/quantization/unquant.py |  |
| 2026-03-07 | `c5a76ad9e` | lizhigong | Merge branch 'cherry-pick-a16f19db' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-07 | `e687d64ce` | lizhigong | Merge branch 'v0.5.9_dev_lzg' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-11 | `37689613c` | maxiao1 | 修复pd分离开启ttft优化首字偶发精度问题 & 修复pd分离decode卡住、精度问题 | python/sglang/srt/disaggregation/decode.py; python/sglang/srt/disaggregation/mooncake/conn.py |  |
| 2026-03-11 | `3e822f7ad` | lizhigong | Merge branch 'v0.5.9_dev_pd' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-13 | `446841129` | niuhb | 支持qwen3-next在fa3后端时打开radix cache | python/sglang/srt/server_args.py |  |
| 2026-03-13 | `5db31f4b4` | lizhigong | Merge branch 'cherry-pick-214917d1' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-13 | `8f3e9df94` | maxiao1 | Merge branch 'cherry-pick-4d97fa3d-to-059' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-13 | `c64ac4481` | lizhigong | Merge branch 'cherry-pick-0955197e' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-13 | `e850c8d2c` | lizhigong | Merge branch 'v0.5.8_dev_yiqa' into 'v0.5.8_dev' | python/sglang/srt/layers/quantization/fp8_kernel.py |  |
| 2026-03-13 | `ee5b7ebb6` | lizhigong | Merge branch 'cherry-pick-e18f065f' into 'v0.5.8_dev' | python/sglang/srt/layers/attention/flashattention_interface.py |  |
| 2026-03-16 | `23fd42261` | maxiao1 | Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-16 | `c2f921462` | niuhb | 修复bailing模型大ep无法启动 | python/sglang/srt/layers/moe/ep_moe/layer.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py; ... 共 4 个文件 |  |
| 2026-03-18 | `c6c74dbdc` | niuhb | GLM5 Test | python/sglang/srt/disaggregation/decode.py; python/sglang/srt/layers/attention/flashmla_backend.py; python/sglang/srt/layers/attention/nsa/index_buf_accessor.py; ... 共 16 个文件 |  |
| 2026-03-20 | `b54acd50f` | liucong8560 | Merge branch 'v0.5.9_dev_liucong' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-20 | `fc5981e07` | liucong | bailing模型支持EP模式下开启rms+quant算子融合 | python/sglang/srt/layers/communicator.py; python/sglang/srt/models/bailing_moe.py |  |
| 2026-03-22 | `d34753123` | niuhb | pd分离p端加上日志 | python/sglang/srt/disaggregation/prefill.py |  |
| 2026-03-23 | `3f30edf9a` | maxiao1 | 修复059版本函数名字修改导致的报错 | python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py |  |
| 2026-03-23 | `79a11f9bb` | maxiao1 | Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-23 | `886fbccec` | maxiao1 | Merge branch 'v0.5.9_dev_mx' into 'v0.5.9_dev' | 无直接文件变更/merge |  |
| 2026-03-26 | `5f51de15a` | niuhb | GLM-5 adaptation | python/sglang/srt/layers/attention/nsa/nsa_indexer.py; python/sglang/srt/layers/attention/nsa_backend.py; python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py; ... 共 6 个文件 |  |
| 2026-03-26 | `e845e0ead` | niuhb | Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb | python/sglang/srt/layers/attention/flashmla_backend.py; python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; ... 共 7 个文件 |  |
| 2026-03-27 | `2b4435fa5` | niuhb | fis bug | python/sglang/srt/layers/attention/nsa/nsa_indexer.py |  |
| 2026-03-27 | `40a938509` | niuhb |  add prefill flashmla_sparse kv_cache fp8 for GLM-5 | python/sglang/srt/layers/attention/nsa_backend.py; sgl-kernel/setup_rocm.py |  |
| 2026-03-30 | `00db89c86` | maxiao1 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py; ... 共 5 个文件 |  |
| 2026-03-30 | `48739c3ac` | niuhb | Merge remote-tracking branch 'origin/v0.5.9_dev' into v0.5.9_dev_niuhb | 无直接文件变更/merge |  |
| 2026-03-30 | `511c78385` | niuhb | GLM5 MTP adapt | python/sglang/srt/layers/attention/nsa_backend.py |  |
| 2026-03-30 | `b15505653` | lizhigong | update readme about dcu | README_DCU.md |  |
| 2026-03-30 | `f9ea5254d` | niuhb | add torch version hadamard_transform_optimized() | python/sglang/srt/layers/attention/nsa/nsa_indexer.py |  |
| 2026-03-31 | `70c416ca9` | chenyue3 | fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1 | python/sglang/srt/models/qwen2.py |  |
| 2026-04-01 | `c2ffad7df` | niuhb | 修复开融合算子后传参逻辑 | python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py |  |
| 2026-04-03 | `968d82d7f` | shiqiang | support mimo-v2-flash-int4 with triton attn | python/sglang/srt/layers/attention/triton_backend.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py; ... 共 4 个文件 | 重复 patch-id: 与 v0.5.9_dev..v0.5.10_dev 的 b4a02fae7 相同 |

### `v0.5.9_dev..v0.5.10_dev`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 2026-03-30 | `7bfdade34` | maxiao1 | 适配kimik2.5；适配mimax2.5；修复 DeepSeek 架构下 routed_scaling_factor 仅在 moe_sum 中生效的逻辑；triton fused_moe接入lightop moe_align；修复函数传参bug | python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe_marlin.py; ... 共 5 个文件 |  |
| 2026-03-30 | `c5eb17125` | lizhigong | sglang dcu 0.5.10rc0 base bash(48739c3a) | README_DCU.md; python/sglang/bench_serving.py; python/sglang/srt/batch_overlap/single_batch_overlap.py; ... 共 114 个文件 |  |
| 2026-03-30 | `f9d9b0204` | liucong | 解决PD分离报错问题 | python/sglang/srt/disaggregation/decode.py; python/sglang/srt/disaggregation/prefill.py; python/sglang/srt/managers/overlap_utils.py; ... 共 7 个文件 |  |
| 2026-03-31 | `2befcb806` | liucong8560 | 修改SGLANG_USE_FUSED_BAILING_RMS_ROTARY环境变量为SGLANG_USE_FUSED_RMS_ROTARY | python/sglang/srt/environ.py; python/sglang/srt/layers/attention/flashattention_backend.py; python/sglang/srt/models/bailing_moe.py; ... 共 4 个文件 |  |
| 2026-03-31 | `77a4da53b` | chenyue3 | fuse rotary_embedding of QwQ-32B by setting export SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING=1 | python/sglang/srt/models/qwen2.py |  |
| 2026-03-31 | `b4de83009` | niuhb | 1. 修复pd分离报错问题 2. 修复跑dpsk代码bug 3. 修复customm allreduce bug 4. 修复sgl-kernel bug | python/sglang/srt/disaggregation/decode.py; python/sglang/srt/disaggregation/prefill.py; python/sglang/srt/distributed/device_communicators/custom_all_reduce.py; ... 共 7 个文件 |  |
| 2026-04-01 | `1ae23c9a5` | chenyue3 | 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现 | python/sglang/srt/layers/layernorm.py |  |
| 2026-04-01 | `236c37f41` | chenyue3 | 修改环境变量SGLANG_USE_FUSED_QWEN_RMS_ROTARY_EMBEDDING名称为SGLANG_USE_FUSED_RMS_ROTARY | python/sglang/srt/models/qwen2.py |  |
| 2026-04-01 | `3d2b0f024` | chenyue3 | 适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现 | python/sglang/srt/layers/layernorm.py |  |
| 2026-04-01 | `3d8bf1aa2` | chenyue3 | 适配lightop的gemma_fused_add_rmsnorm算子 | python/sglang/srt/layers/layernorm.py |  |
| 2026-04-01 | `8edb7c965` | linhai1 | 修复融合算子并验证精度. | python/sglang/srt/layers/attention/dcu_mla_backend.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py |  |
| 2026-04-01 | `962c74637` | chenyue3 | optimized code of layernorm | python/sglang/srt/layers/layernorm.py |  |
| 2026-04-01 | `f2dfc2ec8` | chenyue3 | fix split_qkv_rms_rotary_embedding_fuse_with_kv_store_quant算子的使用bug，此bug影响QwQ-32B模型的性能优化 | python/sglang/srt/models/qwen2.py |  |
| 2026-04-01 | `f4c2ac84a` | chenyue3 | Revert "适配lightop的gemma_fused_add_rmsnorm算子,并保留社区实现" | python/sglang/srt/layers/layernorm.py |  |
| 2026-04-02 | `44081352b` | liucong | support qwen3.5-397b with MTP and deliver a model_dump method by using MODEL_DUMP env, but acc is about 0.02 of gsm8k | python/sglang/srt/model_executor/model_runner.py; python/sglang/srt/speculative/eagle_info_v2.py |  |
| 2026-04-02 | `5bb6dff38` | guobj | Update README_DCU.md | README_DCU.md |  |
| 2026-04-02 | `70c9a1a6d` | guobj | Update README_DCU.md | README_DCU.md |  |
| 2026-04-02 | `865ca25a7` | guobj | Update README_DCU.md | README_DCU.md |  |
| 2026-04-02 | `8d278721f` | guobj | Update README_DCU.md | README_DCU.md |  |
| 2026-04-03 | `4dd71954e` | chenyue3 | [bugfix]将使能QWQ-32B性能优化的环境变量SGLANG_USE_FUSED_RMS_ROTARY名称修改为SGLANG_USE_FUSED_SPLIT_QKV_RMS_ROTARY_EMBEDDING，解决因此引起的精度问题 | python/sglang/srt/models/qwen2.py |  |
| 2026-04-03 | `b4a02fae7` | shiqiang | support mimo-v2-flash-int4 with triton attn | python/sglang/srt/layers/attention/triton_backend.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py; ... 共 4 个文件 | 重复 patch-id: 与 v0.5.8_dev..v0.5.9_dev 的 968d82d7 相同 |
| 2026-04-07 | `50a63c96d` | lizhigong | fix deepseek log cudagraph init meta data copy error in bmz when capture cudagraph. | python/sglang/srt/layers/attention/dcu_mla_backend.py |  |
| 2026-04-07 | `b4059342f` | liucong | 接入causal_conv1d_update优化算子 | python/sglang/srt/layers/attention/linear/gdn_backend.py |  |
| 2026-04-08 | `7104fdb72` | liucong | 解决FA报错问题 | python/sglang/srt/layers/attention/flashattention_backend.py |  |
| 2026-04-09 | `22e5ac5b1` | liuchy5 | Bugfix:fix mm model attention interface | python/sglang/srt/layers/attention/vision.py |  |
| 2026-04-09 | `f6730ce49` | chenyue3 | [Feature]将hipblaslt_w8a8_block_fp8_linear中的per_token_group_quant_fp8量化极修改为lmslim的实现，以提升Qwen3.5-35B-A3B-FP8的性能 | python/sglang/srt/layers/quantization/fp8_utils.py |  |

### `v0.5.10_dev..v0.5.11_dev`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 2026-05-06 | `c200c7845` | lizhigong | sglang dcu 0.5.11 base hash(dfb35997) | README_DCU.md; python/pyproject.toml; python/sglang/bench_serving.py; ... 共 131 个文件 |  |
| 2026-05-07 | `4d897133e` | lizhigong | Supplement merge | python/pyproject.toml; python/sglang/srt/model_executor/model_runner.py |  |
| 2026-05-07 | `96a5c116a` | lizhigong | fix some error in initial version | python/sglang/srt/distributed/parallel_state.py; python/sglang/srt/layers/attention/flashattention_interface.py; python/sglang/srt/layers/quantization/fp8_kernel.py |  |
| 2026-05-09 | `fe8d278ca` | lizhigong | debugging qwen3.5 model | python/sglang/srt/layers/attention/flashattention_backend.py; python/sglang/srt/layers/linear.py; python/sglang/srt/layers/moe/fused_moe_triton/layer.py; ... 共 6 个文件 |  |

### `v0.5.11_dev..v0.5.12_dev`

| 日期 | Commit | 作者 | 概要 | 主要涉及 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 2026-04-25 | `a28aa5f97` | lizhigong | fix some errors when init server | python/sglang/srt/configs/model_config.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; python/sglang/srt/layers/quantization/fp8.py; ... 共 8 个文件 |  |
| 2026-04-27 | `eec3b3ff8` | wangaq | fix for load model | 无直接文件变更/merge |  |
| 2026-04-28 | `14671daae` | wangaq | patch for deepseekv4 | python/sglang/jit_kernel/csrc/deepseek_v4/rope.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh; python/sglang/jit_kernel/include/sgl_kernel/tensor.h; ... 共 11 个文件 |  |
| 2026-04-28 | `24f89924a` | wangaq | Ignore error exceptions and allow the service to start. | python/sglang/jit_kernel/deepseek_v4.py; python/sglang/srt/layers/attention/dsv4/indexer.py; python/sglang/srt/layers/attention/nsa/nsa_indexer.py; ... 共 7 个文件 |  |
| 2026-04-28 | `6ad2adb52` | Zhangzbb | [Feature] support rocm moe_fused_gate | python/sglang/jit_kernel/csrc/add_constant.cuh; python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh; python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh; ... 共 6 个文件 |  |
| 2026-04-28 | `bc0809390` | wangaq | fix jit for compress_forward | python/sglang/jit_kernel/csrc/deepseek_v4/c128.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/c4.cuh; python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh; ... 共 4 个文件 |  |
| 2026-04-28 | `dbd0d5c1d` | wangaq | fix jit for compress_fused_norm_rope_inplace | python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh; python/sglang/srt/layers/attention/dsv4/compressor.py |  |
| 2026-04-29 | `50b898285` | wangaq | fix mhc with tile 0.1.9 | python/sglang/srt/layers/mhc.py |  |
| 2026-04-29 | `66bb0d501` | YuanYuan | [compile fix] rename all '__grid_constant__' with global SGL_GRID_CONSTANT to avoid compiling issues | python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/hash_topk.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh; ... 共 16 个文件 |  |
| 2026-04-29 | `6f3103454` | lipenghui | 修复CompressorPrefillPlan中使用jit kernel编译deepseek_v4/common.cuh时报错的问题 | python/sglang/jit_kernel/deepseek_v4.py; python/sglang/jit_kernel/include/sgl_kernel/utils.h |  |
| 2026-04-29 | `a44cec29b` | wangaq | fix jit for moe_fused_gate | python/sglang/jit_kernel/include/sgl_kernel/warp.cuh |  |
| 2026-04-29 | `bb24fa6e1` | Zhangzbb | [Feature] support rocm moe_fused_gate | python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh; python/sglang/jit_kernel/include/sgl_kernel/warp.cuh |  |
| 2026-04-29 | `cf0af79d2` | wangaq | fix topk_transform_512 jit | python/sglang/jit_kernel/csrc/deepseek_v4/topk.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh; python/sglang/srt/layers/attention/dsv4/metadata.py; ... 共 6 个文件 |  |
| 2026-04-30 | `51f4fe3e1` | flyingdown | fix mhc | python/sglang/srt/layers/mhc.py; python/sglang/srt/models/deepseek_v4.py |  |
| 2026-04-30 | `53c8956fd` | yuanyuan | [compile fix] replace cuda_fp8 with hip/hip_fp8 to avoid jit compile errors | python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh; ... 共 4 个文件 |  |
| 2026-04-30 | `83e281dc0` | wangaq | first version for fp8 block | python/sglang/jit_kernel/deepseek_v4.py; python/sglang/srt/managers/tp_worker.py; python/sglang/srt/models/deepseek_v4.py |  |
| 2026-05-06 | `0c411213f` | flyingdown | 删除deepgemm meta | python/sglang/srt/layers/attention/deepseek_v4_backend.py; python/sglang/srt/layers/attention/nsa/nsa_indexer.py; python/sglang/srt/model_executor/model_runner.py |  |
| 2026-05-07 | `070988441` | flyingdown | support fp8 channel-wise load weight | python/sglang/srt/models/deepseek_v4.py |  |
| 2026-05-08 | `ba7aa00c9` | wangaq | fix bug | python/sglang/srt/models/deepseek_v2.py |  |
| 2026-05-09 | `0dbd5074d` | lj1999 | 接入lightop的Marlin MOE W8A8算子 | python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py; python/sglang/srt/models/deepseek_v4.py |  |
| 2026-05-09 | `452e413c1` | yuanyuan | [bug fix] fix the dpsk-v4 mtp start issue, but multi-request input is failed still | python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope.cuh; python/sglang/srt/layers/moe/ep_moe/layer.py |  |
| 2026-05-09 | `7ecb521af` | wangaq | 1. add aiter moe; 2. split attn for prefill/decode | python/sglang/srt/environ.py; python/sglang/srt/layers/attention/deepseek_v4_backend.py; python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py; ... 共 4 个文件 |  |
| 2026-05-14 | `fd077165a` | YuanYuan | fix the mtp issues of metadata loc size | python/sglang/srt/speculative/eagle_worker_v2.py; python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py |  |
| 2026-05-18 | `43efcafdc` | lizhigong | fix init error when use qwen 3.5 | python/sglang/srt/distributed/parallel_state.py; python/sglang/srt/layers/attention/flashattention_backend.py; python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py; ... 共 7 个文件 |  |
| 2026-05-18 | `c5dd815b3` | lizhigong | dcu 0.5.12 base merge (5daf25b168a9182e660225f68d45f1d2b481d3b6) | README_DCU.md; python/pyproject.toml; python/sglang/bench_serving.py; ... 共 141 个文件 |  |
| 2026-05-20 | `139c5c455` | lizhigong | backup dcu deepseek v4 debug state | python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py; python/sglang/srt/environ.py; python/sglang/srt/layers/mhc.py |  |
| 2026-05-21 | `411660d35` | zhenggf | feat(diffusion): add ROCm SLA attention backend | python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py; python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py; python/sglang/multimodal_gen/runtime/loader/fsdp_load.py; ... 共 6 个文件 |  |
| 2026-05-21 | `b306ccfe4` | lizhigong | 适配deepseekv4 | python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh; python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh; ... 共 19 个文件 |  |
| 2026-05-22 | `f378b1a20` | chenyue3 | [feat]增加aiter w16a16 moe的支持，使能方式为export SGLANG_ROCM_USE_AITER_MOE=1 && export SGLANG_USE_MARLIN_W16A16_MOE=0 | python/sglang/srt/layers/quantization/unquant.py |  |
| 2026-05-28 | `18b48e742` | yangyn1 | moe-runner-backend支持lightop_moe_w8a8 | python/sglang/srt/layers/moe/moe_runner/lightop.py; python/sglang/srt/layers/moe/moe_runner/runner.py; python/sglang/srt/layers/moe/utils.py; ... 共 5 个文件 |  |

## 查询提示

- LightOp/MoE: `00db89c86`, `7bfdade34`, `0dbd5074d`, `7ecb521af`, `f378b1a20`, `18b48e742`
- DeepSeek-V4/DCU JIT: `14671daae`, `24f89924a`, `bc0809390`, `dbd0d5c1d`, `66bb0d501`, `6f3103454`, `cf0af79d2`, `53c8956fd`, `83e281dc0`, `b306ccfe4`
- Qwen/QwQ/GLM/Bailing 模型路径: `4c7028bf2`, `446841129`, `5f51de15a`, `70c416ca9`, `2befcb806`, `77a4da53b`, `44081352b`, `43efcafdc`
- PD/MTP/speculative: `37689613c`, `f9d9b0204`, `b4de83009`, `452e413c1`, `fd077165a`
- multimodal/diffusion ROCm: `411660d35`
