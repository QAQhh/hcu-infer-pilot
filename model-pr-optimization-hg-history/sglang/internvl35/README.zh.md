# sglang InternVL 3.5 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/configs/internvl.py` | `d1e95af28` |
| `python/sglang/srt/models/internvl.py` | `1c456a0af`, `f0c208959`, `feae615b1`, `94bcc19bc`, `b9af8d2eb` |
| `python/sglang/srt/multimodal/internvl_utils.py` | 无直接提交 |
| `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py` | `07a24f1a3`, `feae615b1` |
| `python/sglang/srt/multimodal/processors/internvl.py` | `745840743`, `4a757990a`, `f0c208959`, `539924037`, `5f3eb377e`, `94bcc19bc` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 12
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-18 | `4052b5322` | 性能/后端优化 | fix scheduler for non-cuda devices and disable piecewise cuda graph f… (#19992) | `.github/workflows/pr-test-xpu.yml`, `python/sglang/srt/server_args.py`, `test/srt/run_suite.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-15 | `1c456a0af` | 缺陷修复 | VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282) | `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py` |
| 2026-03-14 | `745840743` | 性能/后端优化 | Fix InternVL and vision attention for non-CUDA backends (e.g. XPU) (#19997) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/internvl.py` |
| 2026-03-09 | `4a757990a` | 性能/后端优化 | [VLM] Replace decord with torchcodec for video decoding (#20055) | `examples/runtime/multimodal/llava_onevision_server.py`, `python/pyproject.toml`, `python/pyproject_cpu.toml` |
| 2026-02-26 | `f0c208959` | 模型支持/运行时入口 | [vlm][internVL] Support processor and embedding inputs for InternVL (#19127) | `python/sglang/srt/models/internvl.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/internvl.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-01-26 | `539924037` | 缺陷修复 | fix(processor): support InternS1 text_config in InternVL processor (#17040) | `python/sglang/srt/multimodal/processors/internvl.py` |
| 2026-01-14 | `feae615b1` | 性能/后端优化 | [VLM] Support ViT CUDA Graph for InternVL (#16732) | `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py` |
| 2026-01-04 | `5f3eb377e` | 模型支持/运行时入口 | [VLM] Support request level max_dynamic_patch for OpenAI request (#16268) | `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/io_struct.py` |
| 2025-12-30 | `94bcc19bc` | 模型支持/运行时入口 | [VLM] Support Video for InternVL3_5 (#15942) | `python/sglang/srt/models/internvl.py`, `python/sglang/srt/multimodal/processors/internvl.py` |
| 2025-12-25 | `b9af8d2eb` | 性能/后端优化 | [VLM] Support apply qk norm in multi cuda streams (#15720) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/utils/multi_stream_utils.py` |

## 逐 Commit 审计卡

### Commit `4052b5322` - fix scheduler for non-cuda devices and disable piecewise cuda graph f… (#19992)

- 完整 hash: `4052b53227f6d234862a45d36b3214fa7ca02784`
- 时间/作者: 2026-03-18 / Juan Muneton
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test-xpu.yml`, `python/sglang/srt/server_args.py`, `test/srt/run_suite.py`, `test/srt/xpu/test_internvl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-xpu.yml`
  - runtime-model: `python/sglang/srt/server_args.py`
  - tests: `test/srt/run_suite.py`; `test/srt/xpu/test_internvl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d1e95af28` - Upgrade transformers==5.3.0 (#17784)

- 完整 hash: `d1e95af282068a751ee6a8b60a0ae2a90c464819`
- 时间/作者: 2026-03-18 / Xinyuan Tong
- 自动分类: 性能/后端优化
- 主要文件: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py` 等 88 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/layers/rotary_embedding/factory.py`; `python/sglang/srt/managers/tokenizer_manager.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/configs/internvl.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/arcee.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/commandr.py`; `python/sglang/srt/models/dbrx.py` 等 54 个文件
  - runtime-perf: `python/sglang/srt/models/afmoe.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/ernie45_moe_vl.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/granitemoe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 15 个文件
  - tests: `python/sglang/test/runners.py`; `test/registered/core/test_score_api.py`; `test/registered/quant/test_awq.py`; `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/vlm/test_vlm_input_format.py`
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

### Commit `745840743` - Fix InternVL and vision attention for non-CUDA backends (e.g. XPU) (#19997)

- 完整 hash: `7458407437cae93f221c529e7e43da54e5a0a233`
- 时间/作者: 2026-03-14 / Juan Muneton
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/internvl.py`, `python/sglang/srt/server_args.py`, `test/srt/run_suite.py`, `test/srt/xpu/test_internvl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`; `python/sglang/srt/managers/scheduler.py`
  - tests: `test/srt/run_suite.py`; `test/srt/xpu/test_internvl.py`
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

### Commit `f0c208959` - [vlm][internVL] Support processor and embedding inputs for InternVL (#19127)

- 完整 hash: `f0c208959794abcd603c6495e6829b2ff6a06a46`
- 时间/作者: 2026-02-26 / Ken J
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/internvl.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/internvl.py`, `test/registered/vlm/test_vlm_input_format.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/internvl.py`
  - runtime-model: `python/sglang/srt/models/internvl.py`
  - tests: `test/registered/vlm/test_vlm_input_format.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `539924037` - fix(processor): support InternS1 text_config in InternVL processor (#17040)

- 完整 hash: `539924037fbc6b64a75c554ed338cb8c5abe5343`
- 时间/作者: 2026-01-26 / Mahdi-CV
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/multimodal/processors/internvl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

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

### Commit `5f3eb377e` - [VLM] Support request level max_dynamic_patch for OpenAI request (#16268)

- 完整 hash: `5f3eb377e0e8bd101c10928c4f73eb36228e6f43`
- 时间/作者: 2026-01-04 / Yuan Luo
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/multimodal/processors/internvl.py`, `python/sglang/srt/parser/jinja_template_utils.py`, `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/multimodal/processors/internvl.py`; `python/sglang/srt/parser/jinja_template_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/entrypoints/openai/protocol.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `94bcc19bc` - [VLM] Support Video for InternVL3_5  (#15942)

- 完整 hash: `94bcc19bcef66b0db31b7366cfd9f09d38d5cb06`
- 时间/作者: 2025-12-30 / Yuan Luo
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/internvl.py`, `python/sglang/srt/multimodal/processors/internvl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
  - runtime-model: `python/sglang/srt/models/internvl.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b9af8d2eb` - [VLM] Support apply qk norm in multi cuda streams (#15720)

- 完整 hash: `b9af8d2eb9f0486c1578dcdbb1ded9b6350bc641`
- 时间/作者: 2025-12-25 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/utils/multi_stream_utils.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/utils/multi_stream_utils.py`
  - runtime-model: `python/sglang/srt/models/internvl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
