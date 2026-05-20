# sglang Qwen VLM/Omni/ASR 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `docs/basic_usage/qwen3_vl.md` | 无直接提交 |
| `examples/chat_template/qwen3_vl_reranker.jinja` | `de94d793a` |
| `examples/runtime/qwen3_vl_reranker.py` | `de94d793a` |
| `python/sglang/srt/configs/qwen3_omni.py` | 无直接提交 |
| `python/sglang/srt/configs/qwen3_vl.py` | 无直接提交 |
| `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` | `55e6acf83` |
| `python/sglang/srt/models/glmasr.py` | `f3ba71166`, `82f1d6157` |
| `python/sglang/srt/models/qwen2_5_vl.py` | `677e446e5`, `07a24f1a3`, `feae615b1`, `25fa2ac29`, `9a414b164`, `cd3289c7a`, `828dec1c7` |
| `python/sglang/srt/models/qwen2_audio.py` | `07a24f1a3` |
| `python/sglang/srt/models/qwen2_vl.py` | `1c456a0af`, `07a24f1a3`, `25fa2ac29` |
| `python/sglang/srt/models/qwen3_omni_moe.py` | `22e67876d`, `031d0a2aa`, `07a24f1a3`, `25fa2ac29` |
| `python/sglang/srt/models/qwen3_vl.py` | `c1d308c60`, `32bd2422e`, `f85455ab2`, `21c4fc633`, `1c456a0af`, `fc543df28`, `3f9fc8b84`, `d566816d8`, `b3202fe6d`, `31c7dc9d9`, `fa5698d79`, `07a24f1a3`, ... (22 total) |
| `python/sglang/srt/models/qwen3_vl_moe.py` | `031d0a2aa`, `07a24f1a3`, `3e7ecb78a`, `725498634` |
| `python/sglang/srt/multimodal/processors/glmasr.py` | `f3ba71166`, `82f1d6157` |
| `python/sglang/srt/multimodal/processors/qwen_vl.py` | `b835309f0`, `42f4b7276`, `0d23a461a`, `135af6dc9`, `4a757990a`, `07a24f1a3`, `27c447653` |
| `python/sglang/test/external_models/custom_qwen2_vl.py` | `e46f79431` |
| `test/manual/lora/test_lora_qwen3_vl.py` | `9e263c216` |
| `test/registered/ascend/vlm_models/test_npu_qwen2_5_vl_3b_instruct.py` | `895e56097` |
| `test/registered/ascend/vlm_models/test_npu_qwen2_5_vl_72b_instruct.py` | `895e56097` |
| `test/registered/ascend/vlm_models/test_npu_qwen3_vl_235b_a22b_instruct.py` | `895e56097` |
| `test/registered/ascend/vlm_models/test_npu_qwen3_vl_30b_a3b_instruct.py` | `895e56097` |
| `test/registered/ascend/vlm_models/test_npu_qwen3_vl_4b_instruct.py` | `895e56097` |
| `test/registered/ascend/vlm_models/test_npu_qwen3_vl_8b_instruct.py` | `895e56097` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 50
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-03-25 | `b835309f0` | 调度/缓存/PD | Reland: compute M-RoPE positions for preprocessed VL inputs (#21244) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-21 | `f97c09dac` | 性能/后端优化 | [AMD] Enable aiter unified attention for non-SWA models (Qwen3-VL) (#20897) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/server_args.py` |
| 2026-03-19 | `42f4b7276` | 调度/缓存/PD | Revert "feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs" (#20956) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-19 | `dc6aa26ce` | 性能/后端优化 | [CPU] Add mrope kernel for Qwen3-vl (#12531) | `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/rope.cpp` |
| 2026-03-19 | `f85455ab2` | 缺陷修复 | [Bugfix] fix qwen3vl hang when --mm-enable-dp-encoder is enable (#20759) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-18 | `0d23a461a` | 调度/缓存/PD | feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs (#19973) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-18 | `21c4fc633` | 缺陷修复 | [DP encoder] Fix `pos_emb `layer TP issue when DP encoder enabled for Qwen3 VL (#20788) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-03-16 | `135af6dc9` | 调度/缓存/PD | [EPD][VLM] support video/audio input (#17824) | `python/sglang/srt/disaggregation/encode_grpc_server.py`, `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py` |
| 2026-03-15 | `1c456a0af` | 缺陷修复 | VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282) | `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py` |
| 2026-03-14 | `22e67876d` | 性能/后端优化 | [Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker (#18185) | `python/sglang/srt/models/qwen3_omni_moe.py` |
| 2026-03-12 | `677e446e5` | 模型支持/运行时入口 | [NPU] Convert cu_window_seqlens to CPU for npu_flush_attention_unpad operator (#20328) | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2026-03-11 | `55e6acf83` | 模型支持/运行时入口 | [NPU][QwenVL] Support qwen image preprocess on npu (#20189) | `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`, `python/sglang/srt/multimodal/processors/base_processor.py` |
| 2026-03-10 | `031d0a2aa` | 性能/后端优化 | [Qwen-MOE] Fix memory duplication issues in case layers weights are re-assigned during weight loading (#18255) | `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl_moe.py` |
| 2026-03-09 | `4a757990a` | 性能/后端优化 | [VLM] Replace decord with torchcodec for video decoding (#20055) | `examples/runtime/multimodal/llava_onevision_server.py`, `python/pyproject.toml`, `python/pyproject_cpu.toml` |
| 2026-03-09 | `fc543df28` | 模型支持/运行时入口 | [NPU] qwen3_vl encoder support graph | `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-03 | `3f9fc8b84` | 性能/后端优化 | [Qwen3.5] Fix missing `quant_config` in `Qwen3VL` (#19291) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-02-27 | `d566816d8` | 缺陷修复 | fix qwen3_vl visual module loading (#19333) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-02-25 | `b3202fe6d` | 性能/后端优化 | [PCG] fix piecewise cuda graph for Qwen3.5 (#19220) | `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-24 | `31c7dc9d9` | 性能/后端优化 | [VLM] Introduce FlashInfer CUDNN Prefill as ViT Backend (#19003) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/server_args.py` |
| 2026-02-18 | `fa5698d79` | 性能/后端优化 | feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation (#18926) | `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-02-10 | `27c447653` | 性能/后端优化 | model: support Qwen3.5 (#18489) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-02-07 | `c850a8a41` | 调度/缓存/PD | [Docs] Add Falcon H1, Hunyuan-Large, Qwen3-Omni support and update Diffusion usage (#17888) | `docs/index.rst`, `docs/platforms/ascend_npu_support.rst`, `docs/platforms/mindspore_backend.md` |
| 2026-02-06 | `6a4b81e2d` | 性能/后端优化 | Refactor(qwen3-vl) optimize position encoding interpolation (#16781) | `python/sglang/srt/models/qwen3_vl.py`, `test/srt/test_embed_interpolate_unittest.py` |
| 2026-02-05 | `3e7ecb78a` | 性能/后端优化 | model: support interns1-pro (#18145) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/interns1pro.py` |
| 2026-02-03 | `c781db0f6` | 调度/缓存/PD | [NPU] update nightly tests (#17952) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-02-02 | `522e13b4d` | 缺陷修复 | fix: correct weight loading prefix mapping for Qwen3-VL (#18024) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-01-30 | `0c5a81acb` | 缺陷修复 | [BUGFIX] Fix dp size > 1 for qwen3 vl model (#17624) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-01-26 | `6756cf18c` | 缺陷修复 | remove multimodal as this is completely dead code (#17750) | `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/multimodal/error.rs` |
| 2026-01-24 | `fb683be6e` | 性能/后端优化 | Use attn tp group in embedding for more models (#17570) | `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py` |
| 2026-01-22 | `0c2993eed` | 性能/后端优化 | Optimize Qwen3-VL video memory usage (#16366) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-01-15 | `de94d793a` | 模型支持/运行时入口 | feat: support qwen3(-VL) rerank scoring&chat template (#16403) | `docs/supported_models/rerank_models.md`, `examples/chat_template/qwen3_reranker.jinja`, `examples/chat_template/qwen3_vl_reranker.jinja` |
| 2026-01-14 | `feae615b1` | 性能/后端优化 | [VLM] Support ViT CUDA Graph for InternVL (#16732) | `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py` |
| 2026-01-08 | `e46f79431` | 性能/后端优化 | Fix external_models import path and migrate model loading tests (#16458) | `.github/workflows/pr-test.yml`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/test/external_models/custom_qwen2_vl.py` |
| 2026-01-06 | `ce694b2b9` | 缺陷修复 | Fix the problem where Qwen3VL raises an "object has no attribute 'mod… (#15677) | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-01-04 | `25fa2ac29` | 性能/后端优化 | Convert cu_seqlens to CPU for npu_flash_attention_unpad operator (#15434) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py` |
| 2026-01-03 | `9a414b164` | 性能/后端优化 | [Performance] Optimze the performance of Qwen25VL (#15640) | `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen2_5_vl.py` |
| 2026-01-01 | `725498634` | 性能/后端优化 | [VLM] feat: true on policy for vlm + fsdp (#14636) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/layernorm.py` |
| 2025-12-31 | `25b48564c` | 缺陷修复 | [NPU][Bugfix] fix Qwen3-VL-30B-A3B-Instruct accuracy loss (#15597) | `python/sglang/srt/layers/rotary_embedding.py` |
| 2025-12-30 | `1048803c1` | 模型支持/运行时入口 | Reworked fast_pos_embed_interpolate() using torch (#10959) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/server_args.py` |
| 2025-12-30 | `9e263c216` | 性能/后端优化 | [LoRA] Torch native backend: rework implementation and updated tests (#15187) | `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/backend/torch_backend.py`, `python/sglang/srt/lora/torch_ops/__init__.py` |
| 2025-12-27 | `cd3289c7a` | 缺陷修复 | [BugFix][VLM] Correct weight loading with tie_word_embeddings == False (#15398) | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-12-26 | `f3ba71166` | 缺陷修复 | fix: change class name of GLM-ASR (#15772) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/base_processor.py` |
| 2025-12-23 | `e254cdf32` | 性能/后端优化 | [CI] Remove pcg-omni-ci (#15656) | `test/registered/cuda_graph/test_piecewise_cuda_graph_2_gpu.py` |
| 2025-12-22 | `989d4b301` | 性能/后端优化 | [CI] Migrate nightly tests to test/registered/ (#15582) | `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py` |
| 2025-12-23 | `82f1d6157` | 模型支持/运行时入口 | [GLM-ASR] GLM-ASR Support (#15570) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/base_processor.py` |
| 2025-12-22 | `828dec1c7` | 模型支持/运行时入口 | [VLM] Tiny: Unify VLM environment variables (#15572) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen2_5_vl.py` |

## 逐 Commit 审计卡

### Commit `c1d308c60` - 修复qwen3.5-397b-fp8报错问题

- 完整 hash: `c1d308c602379d71d746bc50ed785c2bee05ba99`
- 时间/作者: 2026-04-29 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/index.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `32bd2422e` - 修复qwen3.5模型memory_Async问题

- 完整 hash: `32bd2422e7d17f0cee10413aad4a223ffb25dd74`
- 时间/作者: 2026-04-23 / liucong
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/sampling/sampling_batch_info.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/sampling/sampling_batch_info.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b835309f0` - Reland: compute M-RoPE positions for preprocessed VL inputs (#21244)

- 完整 hash: `b835309f0c5c8499bb03dd317b8f11bb085e54dd`
- 时间/作者: 2026-03-25 / Simo Lin
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/glm4v.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/ernie45_vl.py`; `python/sglang/srt/multimodal/processors/glm4v.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f97c09dac` - [AMD] Enable aiter unified attention for non-SWA models (Qwen3-VL) (#20897)

- 完整 hash: `f97c09dac16192d1578d05ecb340b4dca1923e0a`
- 时间/作者: 2026-03-21 / YC Yen-Ching Tseng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `42f4b7276` - Revert "feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs" (#20956)

- 完整 hash: `42f4b7276c3b5888dec4807ce26df8a5e87e54cc`
- 时间/作者: 2026-03-19 / Baizhou Zhang
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/glm4v.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/ernie45_vl.py`; `python/sglang/srt/multimodal/processors/glm4v.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `dc6aa26ce` - [CPU] Add mrope kernel for Qwen3-vl (#12531)

- 完整 hash: `dc6aa26ce9f9f3ea8fafde5a3846579d72b31e0b`
- 时间/作者: 2026-03-19 / blzheng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/rope.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`, `test/srt/cpu/test_rope.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding/mrope.py`
  - runtime-model: `python/sglang/srt/model_executor/cpu_graph_runner.py`
  - runtime-perf: `sgl-kernel/csrc/cpu/rope.cpp`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
  - tests: `test/srt/cpu/test_rope.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f85455ab2` - [Bugfix] fix qwen3vl hang when --mm-enable-dp-encoder is enable (#20759)

- 完整 hash: `f85455ab24d33a6fc0a25c80f8974a21bc87bc94`
- 时间/作者: 2026-03-19 / Ling Zhang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `0d23a461a` - feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs (#19973)

- 完整 hash: `0d23a461a04a8c5e94d3d8a6250a0275d9678921`
- 时间/作者: 2026-03-18 / Chang Su
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/glm4v.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/ernie45_vl.py`; `python/sglang/srt/multimodal/processors/glm4v.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `21c4fc633` - [DP encoder] Fix `pos_emb `layer TP issue when DP encoder enabled for Qwen3 VL (#20788)

- 完整 hash: `21c4fc6334d13cbc075504353b9abc3716cc069e`
- 时间/作者: 2026-03-18 / jianan-gu
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `895e56097` - Add NPU basic function testcases (#19382)

- 完整 hash: `895e56097cc25f762373f462fd027bc39163eb0c`
- 时间/作者: 2026-03-16 / Sugar920
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`, `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py` 等 87 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/disaggregation_utils.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`; `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py`; `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py` 等 86 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `135af6dc9` - [EPD][VLM] support video/audio input (#17824)

- 完整 hash: `135af6dc92aadbb226d111e4add0a757060fc10f`
- 时间/作者: 2026-03-16 / Zheng Wengang
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/encode_grpc_server.py`, `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/embedding_cache_controller.py`, `python/sglang/srt/multimodal/processors/base_processor.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/encode_receiver.py`; `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/managers/mm_utils.py`; `python/sglang/srt/managers/tokenizer_manager.py`; `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/qwen_audio.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`
  - runtime-model: `python/sglang/srt/disaggregation/encode_grpc_server.py`; `python/sglang/srt/disaggregation/encode_server.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/mem_cache/storage/mooncake_store/embedding_cache_controller.py`
  - tests: `test/registered/distributed/test_epd_disaggregation.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `1c456a0af` - VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282)

- 完整 hash: `1c456a0af540b5fd092a90d3af7627be973416a5`
- 时间/作者: 2026-03-15 / Yuhao Yang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/idefics2.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_vl_moonvit.py` 等 18 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/conv.py`
  - runtime-model: `python/sglang/srt/models/clip.py`; `python/sglang/srt/models/dots_vlm_vit.py`; `python/sglang/srt/models/glm4v.py`; `python/sglang/srt/models/idefics2.py`; `python/sglang/srt/models/internvl.py`; `python/sglang/srt/models/kimi_k25.py`; `python/sglang/srt/models/kimi_vl_moonvit.py`; `python/sglang/srt/models/midashenglm.py` 等 16 个文件
  - tests: `test/unit/test_conv_layer.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `22e67876d` - [Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker (#18185)

- 完整 hash: `22e67876d6aa6992bff89d5d91aef2c2c6b3d1bb`
- 时间/作者: 2026-03-14 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_omni_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_omni_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `677e446e5` - [NPU] Convert cu_window_seqlens to CPU for npu_flush_attention_unpad operator (#20328)

- 完整 hash: `677e446e51ca77ffbfbb2d8c0f7d42b0be411940`
- 时间/作者: 2026-03-12 / fy
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen2_5_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2_5_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `55e6acf83` - [NPU][QwenVL] Support qwen image preprocess on npu (#20189)

- 完整 hash: `55e6acf8347873f41e0ca90401170592a3ef2e57`
- 时间/作者: 2026-03-11 / Kurkur
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`, `python/sglang/srt/multimodal/processors/base_processor.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`; `python/sglang/srt/multimodal/processors/base_processor.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `031d0a2aa` - [Qwen-MOE] Fix memory duplication issues in case layers weights are re-assigned during weight loading (#18255)

- 完整 hash: `031d0a2aad444b61c3bbe04e67dda84677b2289d`
- 时间/作者: 2026-03-10 / fxmarty-amd
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/qwen3_moe.py`; `python/sglang/srt/models/qwen3_omni_moe.py`; `python/sglang/srt/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4a757990a` - [VLM] Replace decord with torchcodec for video decoding (#20055)

- 完整 hash: `4a757990a1d37c00a3b6ce9432d18b46d9ea2595`
- 时间/作者: 2026-03-09 / Xinyuan Tong
- 自动分类: 性能/后端优化
- 主要文件: `examples/runtime/multimodal/llava_onevision_server.py`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/multimodal/processors/base_processor.py` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `examples/runtime/multimodal/llava_onevision_server.py`
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/internvl.py` 等 12 个文件
  - runtime-perf: `scripts/ci/cuda/ci_install_dependency.sh`
  - tests: `python/sglang/test/vlm_utils.py`; `test/registered/vlm/test_video_utils.py`; `test/registered/vlm/test_vision_chunked_prefill.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fc543df28` - [NPU] qwen3_vl encoder support graph

- 完整 hash: `fc543df2899582729ef23cbcd9f9362393624222`
- 时间/作者: 2026-03-09 / cen121212
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3f9fc8b84` - [Qwen3.5] Fix missing `quant_config` in `Qwen3VL` (#19291)

- 完整 hash: `3f9fc8b848365a5797a44856854e3e6f00a60dd0`
- 时间/作者: 2026-03-03 / Mohammad Miadh Angkad
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d566816d8` - fix qwen3_vl visual module loading (#19333)

- 完整 hash: `d566816d838ce92d3ae044209f7d67eaa58ce74a`
- 时间/作者: 2026-02-27 / wingedge777
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b3202fe6d` - [PCG] fix piecewise cuda graph for Qwen3.5 (#19220)

- 完整 hash: `b3202fe6d072c6afdfd8a567977d84de17c1d50d`
- 时间/作者: 2026-02-25 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `31c7dc9d9` - [VLM] Introduce FlashInfer CUDNN Prefill as ViT Backend (#19003)

- 完整 hash: `31c7dc9d990d47919435e5c1799d0d36e8b59eca`
- 时间/作者: 2026-02-24 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/server_args.py`, `test/manual/nightly/test_vlms_vit_flashinfer_cudnn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
  - tests: `test/manual/nightly/test_vlms_vit_flashinfer_cudnn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fa5698d79` - feat: [Qwen3.5] Support block-wise FP8 quantization and model adaptation (#18926)

- 完整 hash: `fa5698d7916497288af8fe5a5b57bc4ee7e6fb37`
- 时间/作者: 2026-02-18 / Zheng Li
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `07a24f1a3` - update pre-commit config (#18860)

- 完整 hash: `07a24f1a3846c4186e82ffc2bc43990ba6c0babc`
- 时间/作者: 2026-02-16 / SoluMilken
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py`, `benchmark/fla/benchmark_layernorm_gated.py`, `benchmark/tip_suggestion/bench_other.py`, `benchmark/tip_suggestion/bench_sglang.py`, `benchmark/tip_suggestion/lmql_funcs.py`, `examples/runtime/engine/save_remote_state.py` 等 100 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/lint.yml`
  - docs-bench: `benchmark/fla/benchmark_layernorm_gated.py`; `benchmark/tip_suggestion/bench_other.py`; `benchmark/tip_suggestion/bench_sglang.py`; `benchmark/tip_suggestion/lmql_funcs.py`; `examples/runtime/engine/save_remote_state.py`; `examples/runtime/engine/save_sharded_state.py`
  - other: `python/sglang/srt/compilation/weak_ref_tensor.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/function_call/base_format_detector.py`; `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/metrics/collector.py`; `python/sglang/srt/metrics/utils.py` 等 25 个文件
  - runtime-model: `.pre-commit-config.yaml`; `python/sglang/srt/checkpoint_engine/checkpoint_engine_worker.py`; `python/sglang/srt/configs/exaone.py`; `python/sglang/srt/configs/falcon_h1.py`; `python/sglang/srt/entrypoints/openai/serving_responses.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/deepseek_nextn.py` 等 34 个文件
  - runtime-perf: `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `python/sglang/jit_kernel/include/sgl_kernel/type.cuh`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/linear/seg_la.py`; `python/sglang/srt/layers/attention/wave_ops/prefill_attention.py`; `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py` 等 27 个文件
  - tests: `sgl-kernel/tests/test_per_token_group_quant_8bit.py`; `test/manual/test_vlm_accuracy.py`; `test/registered/attention/test_triton_sliding_window.py`; `test/registered/layers/test_fla_layernorm_guard.py`; `test/registered/quant/test_awq_dequant.py`; `test/srt/cpu/test_norm.py`; `test/srt/cpu/test_qwen3.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `27c447653` - model: support Qwen3.5 (#18489)

- 完整 hash: `27c447653d9cf0f63aea1c190b931be4875cbf86`
- 时间/作者: 2026-02-10 / Zheng Li
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_5.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`
  - other: `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/managers/mm_utils.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`; `python/sglang/srt/utils/common.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py` 等 10 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c850a8a41` - [Docs] Add Falcon H1, Hunyuan-Large, Qwen3-Omni support and update Diffusion usage (#17888)

- 完整 hash: `c850a8a41af2d2f973a7cb033eef9ba9cacc0ca3`
- 时间/作者: 2026-02-07 / Rishit Shivam
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/index.rst`, `docs/platforms/ascend_npu_support.rst`, `docs/platforms/mindspore_backend.md`, `docs/supported_models/extending/index.rst`, `docs/supported_models/extending/modelscope.md`, `docs/supported_models/extending/support_new_models.md`, `docs/supported_models/extending/transformers_fallback.md`, `docs/supported_models/image_generation/index.rst` 等 18 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/index.rst`; `docs/platforms/ascend_npu_support.rst`; `docs/platforms/mindspore_backend.md`; `docs/supported_models/extending/index.rst`; `docs/supported_models/extending/modelscope.md`; `docs/supported_models/extending/support_new_models.md`; `docs/supported_models/extending/transformers_fallback.md`; `docs/supported_models/image_generation/index.rst` 等 18 个文件
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `6a4b81e2d` - Refactor(qwen3-vl) optimize position encoding interpolation (#16781)

- 完整 hash: `6a4b81e2d9fc0da998d296b86fbacc7e1594988d`
- 时间/作者: 2026-02-06 / aaaandychen
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`, `test/srt/test_embed_interpolate_unittest.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
  - tests: `test/srt/test_embed_interpolate_unittest.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3e7ecb78a` - model: support interns1-pro (#18145)

- 完整 hash: `3e7ecb78a60f8e1d889cfe25c88006577783d903`
- 时间/作者: 2026-02-05 / RunningLeon
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/interns1pro.py`, `python/sglang/srt/models/qwen3_vl_moe.py`, `python/sglang/srt/multimodal/processors/interns1pro.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/multimodal/processors/interns1pro.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/interns1pro.py`
  - runtime-perf: `python/sglang/srt/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c781db0f6` - [NPU] update nightly tests (#17952)

- 完整 hash: `c781db0f6c236e357a0652a962fdf7d3f528d752`
- 时间/作者: 2026-02-03 / Sugar920
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `python/sglang/test/ascend/vlm_utils.py`, `test/registered/ascend/basic_function/interface/test_ascend_enable_thinking.py`, `test/registered/ascend/basic_function/parameter/test_ascend_log_level.py`, `test/registered/ascend/basic_function/parameter/test_ascend_no_chunked_prefill.py`, `test/registered/ascend/basic_function/parameter/test_ascend_no_overlap_scheduler.py` 等 52 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/gsm8k_ascend_mixin.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `python/sglang/test/ascend/vlm_utils.py`; `test/registered/ascend/basic_function/interface/test_ascend_enable_thinking.py`; `test/registered/ascend/basic_function/parameter/test_ascend_log_level.py`; `test/registered/ascend/basic_function/parameter/test_ascend_no_chunked_prefill.py`; `test/registered/ascend/basic_function/parameter/test_ascend_no_overlap_scheduler.py`; `test/registered/ascend/basic_function/parameter/test_ascend_original_logprobs.py` 等 51 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `522e13b4d` - fix: correct weight loading prefix mapping for Qwen3-VL (#18024)

- 完整 hash: `522e13b4d2c1de1cfb44ecbbca374ec8f312de52`
- 时间/作者: 2026-02-02 / Xiaoming Liu
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `0c5a81acb` - [BUGFIX] Fix dp size > 1 for qwen3 vl model (#17624)

- 完整 hash: `0c5a81acb85b963f533cc85024736724a1182884`
- 时间/作者: 2026-01-30 / Zheng Li
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/mm_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/linear.py`; `python/sglang/srt/multimodal/mm_utils.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6756cf18c` - remove multimodal as this is completely dead code (#17750)

- 完整 hash: `6756cf18c61dde7eb855ccecd002ba5cde1ab610`
- 时间/作者: 2026-01-26 / Simo Lin
- 自动分类: 缺陷修复
- 主要文件: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/src/lib.rs`, `sgl-model-gateway/src/multimodal/error.rs`, `sgl-model-gateway/src/multimodal/media.rs`, `sgl-model-gateway/src/multimodal/mod.rs`, `sgl-model-gateway/src/multimodal/registry.rs`, `sgl-model-gateway/src/multimodal/tracker.rs`, `sgl-model-gateway/src/multimodal/types.rs` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `sgl-model-gateway/Cargo.toml`; `sgl-model-gateway/src/lib.rs`; `sgl-model-gateway/src/multimodal/error.rs`; `sgl-model-gateway/src/multimodal/media.rs`; `sgl-model-gateway/src/multimodal/mod.rs`; `sgl-model-gateway/src/multimodal/registry.rs`; `sgl-model-gateway/src/multimodal/tracker.rs`; `sgl-model-gateway/src/multimodal/types.rs` 等 20 个文件
  - runtime-model: `sgl-model-gateway/src/multimodal/vision/preprocessor_config.rs`
  - tests: `sgl-model-gateway/tests/multimodal/mod.rs`; `sgl-model-gateway/tests/multimodal/multimodal_tracker_test.rs`; `sgl-model-gateway/tests/multimodal/vision_golden_tests.rs`; `sgl-model-gateway/tests/multimodal_tests.rs`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `fb683be6e` - Use attn tp group in embedding for more models (#17570)

- 完整 hash: `fb683be6eb7c6960f3d37ea91ca836c1b8e4120c`
- 时间/作者: 2026-01-24 / Ke Bao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py`, `python/sglang/srt/models/glm4.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/models/gpt_oss.py` 等 19 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/falcon_h1.py`; `python/sglang/srt/models/glm4.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/llada2.py`; `python/sglang/srt/models/llama4.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/bailing_moe_nextn.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/glm4_moe_lite.py`; `python/sglang/srt/models/glm4_moe_nextn.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 10 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0c2993eed` - Optimize Qwen3-VL video memory usage (#16366)

- 完整 hash: `0c2993eed03a39f8b927a9c40b440b848408fd3c`
- 时间/作者: 2026-01-22 / cen121212
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `de94d793a` - feat: support qwen3(-VL) rerank scoring&chat template (#16403)

- 完整 hash: `de94d793ad258e85a254be2e158dd4d37f846c19`
- 时间/作者: 2026-01-15 / shuwenn
- 自动分类: 模型支持/运行时入口
- 主要文件: `docs/supported_models/rerank_models.md`, `examples/chat_template/qwen3_reranker.jinja`, `examples/chat_template/qwen3_vl_reranker.jinja`, `examples/runtime/qwen3_vl_reranker.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_rerank.py`, `python/sglang/srt/managers/tokenizer_manager_multiitem_mixin.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/supported_models/rerank_models.md`; `examples/chat_template/qwen3_reranker.jinja`; `examples/chat_template/qwen3_vl_reranker.jinja`; `examples/runtime/qwen3_vl_reranker.py`
  - other: `python/sglang/srt/managers/tokenizer_manager_multiitem_mixin.py`
  - runtime-model: `python/sglang/srt/entrypoints/http_server.py`; `python/sglang/srt/entrypoints/openai/protocol.py`; `python/sglang/srt/entrypoints/openai/serving_rerank.py`
  - tests: `test/registered/openai_server/basic/test_serving_rerank.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `feae615b1` - [VLM] Support ViT CUDA Graph for InternVL (#16732)

- 完整 hash: `feae615b1146ec7869c203ddf7e997c3a3a59f6e`
- 时间/作者: 2026-01-14 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/internvl.py`; `python/sglang/srt/models/qwen2_5_vl.py`
  - runtime-perf: `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e46f79431` - Fix external_models import path and migrate model loading tests (#16458)

- 完整 hash: `e46f79431b809aca979f105cb6034684f9ff9b53`
- 时间/作者: 2026-01-08 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test.yml`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/test/external_models/custom_qwen2_vl.py`, `test/registered/model_loading/test_external_models.py`, `test/registered/model_loading/test_modelopt_export.py`, `test/registered/model_loading/test_modelopt_loader.py`, `test/registered/model_loading/test_utils_update_weights.py`, `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`
  - tests: `python/sglang/test/external_models/custom_qwen2_vl.py`; `test/registered/model_loading/test_external_models.py`; `test/registered/model_loading/test_modelopt_export.py`; `test/registered/model_loading/test_modelopt_loader.py`; `test/registered/model_loading/test_utils_update_weights.py`; `test/srt/run_suite.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ce694b2b9` - Fix the problem where Qwen3VL raises an "object has no attribute 'mod… (#15677)

- 完整 hash: `ce694b2b9e0ab07aaffdd777d3370e096ed8b0f3`
- 时间/作者: 2026-01-06 / ShirakSyouya
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `25fa2ac29` - Convert cu_seqlens to CPU for npu_flash_attention_unpad operator (#15434)

- 完整 hash: `25fa2ac2904fe61f2471d805907f45773a7645e9`
- 时间/作者: 2026-01-04 / fy
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/idefics2.py`, `python/sglang/srt/models/paddleocr_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen3_omni_moe.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/dots_vlm_vit.py`; `python/sglang/srt/models/glm4v.py`; `python/sglang/srt/models/idefics2.py`; `python/sglang/srt/models/paddleocr_vl.py`; `python/sglang/srt/models/qwen2_5_vl.py`; `python/sglang/srt/models/qwen2_vl.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`; `python/sglang/srt/models/qwen3_omni_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9a414b164` - [Performance] Optimze the performance of Qwen25VL (#15640)

- 完整 hash: `9a414b164c5eb538a6b3677e5f3d9dcd27ee9f3d`
- 时间/作者: 2026-01-03 / Siyuan Chen
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen2_5_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen2_5_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `725498634` - [VLM] feat: true on policy for vlm + fsdp (#14636)

- 完整 hash: `7254986342f707435ebb00fa06268107ee3a4386`
- 时间/作者: 2026-01-01 / Nan Jiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3.py`, `python/sglang/srt/models/qwen3_moe.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/multimodal/processors/base_processor.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_vl.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`; `python/sglang/srt/models/qwen2_moe.py`; `python/sglang/srt/models/qwen3_moe.py`; `python/sglang/srt/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `25b48564c` - [NPU][Bugfix] fix Qwen3-VL-30B-A3B-Instruct accuracy loss (#15597)

- 完整 hash: `25b48564c38184e90026058c07f253a849f38e9e`
- 时间/作者: 2025-12-31 / cen121212
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/rotary_embedding.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/rotary_embedding.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `1048803c1` - Reworked fast_pos_embed_interpolate() using torch (#10959)

- 完整 hash: `1048803c1fc502079046b0fd28ecef8213cda430`
- 时间/作者: 2025-12-30 / Vitaly Tuzov
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/multi_stream_utils.py`, `test/srt/run_suite.py`, `test/srt/test_embed_interpolate_unittest.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/utils/multi_stream_utils.py`
  - runtime-model: `python/sglang/srt/models/qwen3_vl.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
  - tests: `test/srt/run_suite.py`; `test/srt/test_embed_interpolate_unittest.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9e263c216` - [LoRA] Torch native backend: rework implementation and updated tests (#15187)

- 完整 hash: `9e263c2162bec6721e6e9f8dd27ace97a3e9874f`
- 时间/作者: 2025-12-30 / Vladimir Serov
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/backend/torch_backend.py`, `python/sglang/srt/lora/torch_ops/__init__.py`, `python/sglang/srt/lora/torch_ops/lora_ops.py`, `python/sglang/srt/lora/utils.py`, `python/sglang/test/lora_utils.py`, `test/manual/lora/test_chunked_sgmv_backend.py`, `test/manual/lora/test_lora_cuda_graph.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/lora/backend/chunked_backend.py`; `python/sglang/srt/lora/backend/torch_backend.py`; `python/sglang/srt/lora/torch_ops/__init__.py`; `python/sglang/srt/lora/torch_ops/lora_ops.py`; `python/sglang/srt/lora/utils.py`
  - tests: `python/sglang/test/lora_utils.py`; `test/manual/lora/test_chunked_sgmv_backend.py`; `test/manual/lora/test_lora_cuda_graph.py`; `test/manual/lora/test_lora_ops.py`; `test/manual/lora/test_lora_qwen3_vl.py`; `test/manual/lora/test_lora_spec_decoding.py`; `test/manual/lora/test_torch_backend.py`; `test/manual/test_lora_ops.py` 等 9 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `cd3289c7a` - [BugFix][VLM] Correct weight loading with tie_word_embeddings == False (#15398)

- 完整 hash: `cd3289c7a46efdad6e01ad30a86d04f1767a5937`
- 时间/作者: 2025-12-27 / Zheng Wengang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen2_5_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen2_5_vl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f3ba71166` - fix: change class name of GLM-ASR (#15772)

- 完整 hash: `f3ba711662622dffde8d3cb7e464cfd5e5188765`
- 时间/作者: 2025-12-26 / Yuxuan Zhang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/glmasr.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/glmasr.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/glmasr.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `e254cdf32` - [CI] Remove pcg-omni-ci (#15656)

- 完整 hash: `e254cdf326849e893a8129b53d969e2aa45f88c4`
- 时间/作者: 2025-12-23 / Yuwei An
- 自动分类: 性能/后端优化
- 主要文件: `test/registered/cuda_graph/test_piecewise_cuda_graph_2_gpu.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/cuda_graph/test_piecewise_cuda_graph_2_gpu.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `989d4b301` - [CI] Migrate nightly tests to test/registered/ (#15582)

- 完整 hash: `989d4b301293ea8eb243d7c320c5c457cb718629`
- 时间/作者: 2025-12-22 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/vlm_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/run_combined_tests.py` 等 64 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/ascend/__init__.py`; `python/sglang/test/ascend/gsm8k_ascend_mixin.py`; `python/sglang/test/ascend/vlm_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/run_combined_tests.py`; `test/registered/8-gpu-models/test_deepseek_v31.py` 等 63 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `82f1d6157` - [GLM-ASR] GLM-ASR Support  (#15570)

- 完整 hash: `82f1d6157f8ed36a8eb758e7090331f817351f01`
- 时间/作者: 2025-12-23 / Yuxuan Zhang
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/glmasr.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/glmasr.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/glmasr.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `828dec1c7` - [VLM] Tiny: Unify VLM environment variables (#15572)

- 完整 hash: `828dec1c7c305f0311344ab1acf8f513bc486978`
- 时间/作者: 2025-12-22 / Yuan Luo
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/qwen2_5_vl.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
