

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
# sglang Local-only Commits Without a Specific Model Bucket

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
