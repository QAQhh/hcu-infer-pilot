# sglang GLM VLM/OCR Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/glm4v.py` | `1c456a0af`, `97a2a9be0`, `7106f6c8e`, `25fa2ac29` |
| `python/sglang/srt/models/glm4v_moe.py` | `fcaad42b0`, `f15b3338c`, `c330b687a` |
| `python/sglang/srt/models/glm_ocr.py` | `fcaad42b0`, `f15b3338c`, `c330b687a`, `7106f6c8e` |
| `python/sglang/srt/models/glm_ocr_nextn.py` | `7106f6c8e` |
| `python/sglang/srt/multimodal/processors/glm4v.py` | `b835309f0`, `42f4b7276`, `0d23a461a`, `206accd15`, `07a24f1a3`, `7106f6c8e` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 13
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-03-25 | `b835309f0` | 调度/缓存/PD | Reland: compute M-RoPE positions for preprocessed VL inputs (#21244) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-24 | `fcaad42b0` | 性能/后端优化 | [Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix (#21134) | `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py` |
| 2026-03-19 | `42f4b7276` | 调度/缓存/PD | Revert "feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs" (#20956) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-18 | `0d23a461a` | 调度/缓存/PD | feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs (#19973) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-18 | `f15b3338c` | 性能/后端优化 | Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr" (#20740) | `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py` |
| 2026-03-15 | `1c456a0af` | 缺陷修复 | VLM: add Conv2dLayer/Conv3dLayer to fix PyTorch 2.9.1 CuDNN Conv3d (#20282) | `python/sglang/srt/layers/conv.py`, `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/dots_vlm_vit.py` |
| 2026-03-14 | `c330b687a` | 性能/后端优化 | [Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr (#20463) | `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py` |
| 2026-03-08 | `97a2a9be0` | 性能/后端优化 | [VLM] Replace conv3d proj with linear for GLM4V (#20033) | `python/sglang/srt/models/glm4v.py`, `test/registered/vlm/test_patch_embed_perf.py` |
| 2026-02-16 | `206accd15` | 缺陷修复 | Fix GLM-4V processor registration when glm_ocr is unavailable (#18885) | `python/sglang/srt/multimodal/processors/glm4v.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-02-01 | `4ea4f2a20` | 性能/后端优化 | [VLM] Optimize get_rope_index for GLM4v (#17420) | `benchmark/bench_rope/benchmark_rope_index.py`, `python/sglang/srt/layers/rotary_embedding.py` |
| 2026-01-27 | `7106f6c8e` | 模型支持/运行时入口 | [GLM-OCR] Support GLM-OCR Model (#17582) | `docs/supported_models/multimodal_language_models.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/vision.py` |
| 2026-01-04 | `25fa2ac29` | 性能/后端优化 | Convert cu_seqlens to CPU for npu_flash_attention_unpad operator (#15434) | `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py` |

## Per-Commit Audit Cards

### Commit `b835309f0` - Reland: compute M-RoPE positions for preprocessed VL inputs (#21244)

- Full hash: `b835309f0c5c8499bb03dd317b8f11bb085e54dd`
- Date/author: 2026-03-25 / Simo Lin
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/glm4v.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/ernie45_vl.py`; `python/sglang/srt/multimodal/processors/glm4v.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fcaad42b0` - [Bug Fix] GLM-V / GLM-OCR: field detection for transformers 5.x and MTP omission fix (#21134)

- Full hash: `fcaad42b0038adbeb76b5807f47ed5d369f5d71a`
- Date/author: 2026-03-24 / Yuxuan Zhang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/model_loader/weight_utils.py`
  - runtime-model: `python/sglang/srt/models/glm_ocr.py`
  - runtime-perf: `python/sglang/srt/models/glm4v_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `42f4b7276` - Revert "feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs" (#20956)

- Full hash: `42f4b7276c3b5888dec4807ce26df8a5e87e54cc`
- Date/author: 2026-03-19 / Baizhou Zhang
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/glm4v.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/ernie45_vl.py`; `python/sglang/srt/multimodal/processors/glm4v.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0d23a461a` - feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs (#19973)

- Full hash: `0d23a461a04a8c5e94d3d8a6250a0275d9678921`
- Date/author: 2026-03-18 / Chang Su
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/glm4v.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/base_processor.py`; `python/sglang/srt/multimodal/processors/ernie45_vl.py`; `python/sglang/srt/multimodal/processors/glm4v.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f15b3338c` - Revert "[Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr" (#20740)

- Full hash: `f15b3338c9f3c6a4a93c652cb2b0295510fc68e5`
- Date/author: 2026-03-18 / Mick
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/glm_ocr.py`
  - runtime-perf: `python/sglang/srt/models/glm4v_moe.py`
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

### Commit `c330b687a` - [Bugfix] Fix GLM-4.6V vision regression in glm4v_moe and glm_ocr (#20463)

- Full hash: `c330b687a116be3738120f430ddbb096ca9543a3`
- Date/author: 2026-03-14 / Xinyuan Tong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/glm4v_moe.py`, `python/sglang/srt/models/glm_ocr.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/glm_ocr.py`
  - runtime-perf: `python/sglang/srt/models/glm4v_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `97a2a9be0` - [VLM] Replace conv3d proj with linear for GLM4V (#20033)

- Full hash: `97a2a9be0f45a64f1d2e469456377361329011eb`
- Date/author: 2026-03-08 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/glm4v.py`, `test/registered/vlm/test_patch_embed_perf.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/glm4v.py`
  - tests: `test/registered/vlm/test_patch_embed_perf.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `206accd15` - Fix GLM-4V processor registration when glm_ocr is unavailable (#18885)

- Full hash: `206accd15de341e10be68ae6139a3cdfb610eac3`
- Date/author: 2026-02-16 / Alison Shao
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/multimodal/processors/glm4v.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/multimodal/processors/glm4v.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

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

### Commit `4ea4f2a20` - [VLM] Optimize get_rope_index for GLM4v (#17420)

- Full hash: `4ea4f2a20c4b7d6d78220ac5e1c80aa1d288c9fb`
- Date/author: 2026-02-01 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `benchmark/bench_rope/benchmark_rope_index.py`, `python/sglang/srt/layers/rotary_embedding.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/bench_rope/benchmark_rope_index.py`
  - other: `python/sglang/srt/layers/rotary_embedding.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `7106f6c8e` - [GLM-OCR] Support GLM-OCR Model (#17582)

- Full hash: `7106f6c8e1509cd57abeafd5d50cb1beaffbc63c`
- Date/author: 2026-01-27 / Yuxuan Zhang
- Auto category: 模型支持/运行时入口
- Main files: `docs/supported_models/multimodal_language_models.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/glm4.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/glm_ocr.py`, `python/sglang/srt/models/glm_ocr_nextn.py`, `python/sglang/srt/multimodal/processors/glm4v.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/supported_models/multimodal_language_models.md`
  - other: `python/sglang/srt/multimodal/processors/glm4v.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/glm4.py`; `python/sglang/srt/models/glm4v.py`; `python/sglang/srt/models/glm_ocr.py`; `python/sglang/srt/models/glm_ocr_nextn.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `25fa2ac29` - Convert cu_seqlens to CPU for npu_flash_attention_unpad operator (#15434)

- Full hash: `25fa2ac2904fe61f2471d805907f45773a7645e9`
- Date/author: 2026-01-04 / fy
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/dots_vlm_vit.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/idefics2.py`, `python/sglang/srt/models/paddleocr_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen3_omni_moe.py` 等 9 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/dots_vlm_vit.py`; `python/sglang/srt/models/glm4v.py`; `python/sglang/srt/models/idefics2.py`; `python/sglang/srt/models/paddleocr_vl.py`; `python/sglang/srt/models/qwen2_5_vl.py`; `python/sglang/srt/models/qwen2_vl.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/vision.py`; `python/sglang/srt/models/qwen3_omni_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
