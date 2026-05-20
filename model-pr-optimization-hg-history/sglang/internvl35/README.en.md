# sglang InternVL 3.5 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/configs/internvl.py` | `d1e95af28` |
| `python/sglang/srt/models/internvl.py` | `1c456a0af`, `f0c208959`, `feae615b1`, `94bcc19bc`, `b9af8d2eb` |
| `python/sglang/srt/multimodal/internvl_utils.py` | no direct commit |
| `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py` | `07a24f1a3`, `feae615b1` |
| `python/sglang/srt/multimodal/processors/internvl.py` | `745840743`, `4a757990a`, `f0c208959`, `539924037`, `5f3eb377e`, `94bcc19bc` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 12
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
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

## Per-Commit Audit Cards

### Commit `4052b5322` - fix scheduler for non-cuda devices and disable piecewise cuda graph f… (#19992)

- Full hash: `4052b53227f6d234862a45d36b3214fa7ca02784`
- Date/author: 2026-03-18 / Juan Muneton
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/srt/server_args.py`, `test/srt/run_suite.py`, `test/srt/xpu/test_internvl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test-xpu.yml`
  - runtime-model: `python/sglang/srt/server_args.py`
  - tests: `test/srt/run_suite.py`; `test/srt/xpu/test_internvl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d1e95af28` - Upgrade transformers==5.3.0 (#17784)

- Full hash: `d1e95af282068a751ee6a8b60a0ae2a90c464819`
- Date/author: 2026-03-18 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/configs/internvl.py`, `python/sglang/srt/configs/model_config.py` 等 88 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/layers/rotary_embedding/factory.py`; `python/sglang/srt/managers/tokenizer_manager.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/configs/internvl.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/apertus.py`; `python/sglang/srt/models/arcee.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/commandr.py`; `python/sglang/srt/models/dbrx.py` 等 54 个文件
  - runtime-perf: `python/sglang/srt/models/afmoe.py`; `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/ernie45_moe_vl.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/granitemoe.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 15 个文件
  - tests: `python/sglang/test/runners.py`; `test/registered/core/test_score_api.py`; `test/registered/quant/test_awq.py`; `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/vlm/test_vlm_input_format.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1c456a0af` - VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282)

- Full hash: `1c456a0af540b5fd092a90d3af7627be973416a5`
- Date/author: 2026-03-15 / Yuhao Yang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/idefics2.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_vl_moonvit.py` 等 18 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/conv.py`
  - runtime-model: `python/sglang/srt/models/clip.py`; `python/sglang/srt/models/dots_vlm_vit.py`; `python/sglang/srt/models/glm4v.py`; `python/sglang/srt/models/idefics2.py`; `python/sglang/srt/models/internvl.py`; `python/sglang/srt/models/kimi_k25.py`; `python/sglang/srt/models/kimi_vl_moonvit.py`; `python/sglang/srt/models/midashenglm.py` 等 16 个文件
  - tests: `test/unit/test_conv_layer.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `745840743` - Fix InternVL and vision attention for non-CUDA backends (e.g. XPU) (#19997)

- Full hash: `7458407437cae93f221c529e7e43da54e5a0a233`
- Date/author: 2026-03-14 / Juan Muneton
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/internvl.py`, `python/sglang/srt/server_args.py`, `test/srt/run_suite.py`, `test/srt/xpu/test_internvl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`; `python/sglang/srt/managers/scheduler.py`
  - tests: `test/srt/run_suite.py`; `test/srt/xpu/test_internvl.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4a757990a` - [VLM] Replace decord with torchcodec for video decoding (#20055)

- Full hash: `4a757990a1d37c00a3b6ce9432d18b46d9ea2595`
- Date/author: 2026-03-09 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `examples/runtime/multimodal/llava_onevision_server.py`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml`, `python/pyproject_xpu.toml`, `python/sglang/check_env.py`, `python/sglang/srt/multimodal/processors/base_processor.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `examples/runtime/multimodal/llava_onevision_server.py`
  - other: `python/pyproject.toml`; `python/pyproject_cpu.toml`; `python/pyproject_npu.toml`; `python/pyproject_other.toml`; `python/pyproject_xpu.toml`; `python/sglang/check_env.py`; `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/internvl.py` 等 12 个文件
  - runtime-perf: `scripts/ci/cuda/ci_install_dependency.sh`
  - tests: `python/sglang/test/vlm_utils.py`; `test/registered/vlm/test_video_utils.py`; `test/registered/vlm/test_vision_chunked_prefill.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f0c208959` - [vlm][internVL] Support processor and embedding inputs for InternVL (#19127)

- Full hash: `f0c208959794abcd603c6495e6829b2ff6a06a46`
- Date/author: 2026-02-26 / Ken J
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/internvl.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/internvl.py`, `test/registered/vlm/test_vlm_input_format.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/internvl.py`
  - runtime-model: `python/sglang/srt/models/internvl.py`
  - tests: `test/registered/vlm/test_vlm_input_format.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `07a24f1a3` - update pre-commit config (#18860)

- Full hash: `07a24f1a3846c4186e82ffc2bc43990ba6c0babc`
- Date/author: 2026-02-16 / SoluMilken
- Auto category: 性能/后端优化
- Main files: `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py`, `benchmark/fla/benchmark_layernorm_gated.py`, `benchmark/tip_suggestion/bench_other.py`, `benchmark/tip_suggestion/bench_sglang.py`, `benchmark/tip_suggestion/lmql_funcs.py`, `examples/runtime/engine/save_remote_state.py` 等 100 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/lint.yml`
  - docs-bench: `benchmark/fla/benchmark_layernorm_gated.py`; `benchmark/tip_suggestion/bench_other.py`; `benchmark/tip_suggestion/bench_sglang.py`; `benchmark/tip_suggestion/lmql_funcs.py`; `examples/runtime/engine/save_remote_state.py`; `examples/runtime/engine/save_sharded_state.py`
  - other: `python/sglang/srt/compilation/weak_ref_tensor.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/function_call/base_format_detector.py`; `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`; `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/metrics/collector.py`; `python/sglang/srt/metrics/utils.py` 等 25 个文件
  - runtime-model: `.pre-commit-config.yaml`; `python/sglang/srt/checkpoint_engine/checkpoint_engine_worker.py`; `python/sglang/srt/configs/exaone.py`; `python/sglang/srt/configs/falcon_h1.py`; `python/sglang/srt/entrypoints/openai/serving_responses.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/models/baichuan.py`; `python/sglang/srt/models/deepseek_nextn.py` 等 34 个文件
  - runtime-perf: `3rdparty/amd/tuning/benchmark_moe_rocm.py`; `python/sglang/jit_kernel/include/sgl_kernel/type.cuh`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/linear/seg_la.py`; `python/sglang/srt/layers/attention/wave_ops/prefill_attention.py`; `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py` 等 27 个文件
  - tests: `sgl-kernel/tests/test_per_token_group_quant_8bit.py`; `test/manual/test_vlm_accuracy.py`; `test/registered/attention/test_triton_sliding_window.py`; `test/registered/layers/test_fla_layernorm_guard.py`; `test/registered/quant/test_awq_dequant.py`; `test/srt/cpu/test_norm.py`; `test/srt/cpu/test_qwen3.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `539924037` - fix(processor): support InternS1 text_config in InternVL processor (#17040)

- Full hash: `539924037fbc6b64a75c554ed338cb8c5abe5343`
- Date/author: 2026-01-26 / Mahdi-CV
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/multimodal/processors/internvl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `feae615b1` - [VLM] Support ViT CUDA Graph for InternVL (#16732)

- Full hash: `feae615b1146ec7869c203ddf7e997c3a3a59f6e`
- Date/author: 2026-01-14 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/internvl.py`, `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/internvl.py`; `python/sglang/srt/models/qwen2_5_vl.py`
  - runtime-perf: `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5f3eb377e` - [VLM] Support request level max_dynamic_patch for OpenAI request (#16268)

- Full hash: `5f3eb377e0e8bd101c10928c4f73eb36228e6f43`
- Date/author: 2026-01-04 / Yuan Luo
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/multimodal/processors/internvl.py`, `python/sglang/srt/parser/jinja_template_utils.py`, `python/sglang/srt/utils/common.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/io_struct.py`; `python/sglang/srt/multimodal/processors/internvl.py`; `python/sglang/srt/parser/jinja_template_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/entrypoints/openai/protocol.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `94bcc19bc` - [VLM] Support Video for InternVL3_5  (#15942)

- Full hash: `94bcc19bcef66b0db31b7366cfd9f09d38d5cb06`
- Date/author: 2025-12-30 / Yuan Luo
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/internvl.py`, `python/sglang/srt/multimodal/processors/internvl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/internvl.py`
  - runtime-model: `python/sglang/srt/models/internvl.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b9af8d2eb` - [VLM] Support apply qk norm in multi cuda streams (#15720)

- Full hash: `b9af8d2eb9f0486c1578dcdbb1ded9b6350bc641`
- Date/author: 2025-12-25 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/internvl.py`, `python/sglang/srt/utils/multi_stream_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/utils/multi_stream_utils.py`
  - runtime-model: `python/sglang/srt/models/internvl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
