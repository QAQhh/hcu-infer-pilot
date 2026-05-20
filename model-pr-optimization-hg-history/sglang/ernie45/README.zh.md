# sglang ERNIE 4.5 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/ernie45_moe_vl.py` | `d1e95af28`, `07a24f1a3`, `1a19b3987` |
| `python/sglang/srt/models/ernie45_vl.py` | `82e7139c0`, `07a24f1a3`, `1a19b3987` |
| `python/sglang/srt/multimodal/processors/ernie45_vl.py` | `b835309f0`, `42f4b7276`, `0d23a461a`, `07a24f1a3`, `1a19b3987` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 7
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-25 | `b835309f0` | 调度/缓存/PD | Reland: compute M-RoPE positions for preprocessed VL inputs (#21244) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-19 | `42f4b7276` | 调度/缓存/PD | Revert "feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs" (#20956) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-18 | `0d23a461a` | 调度/缓存/PD | feat(mm)(grpc): compute M-RoPE positions for preprocessed VL inputs (#19973) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-04 | `82e7139c0` | 调度/缓存/PD | [VLM] Support cos sin cache for Ernie4.5-VL (#19743) | `python/sglang/srt/models/ernie45_vl.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-01-26 | `1a19b3987` | 性能/后端优化 | [Model] Add Ernie4.5 VL model support (#15679) | `docs/supported_models/multimodal_language_models.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py` |

## 逐 Commit 审计卡

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

### Commit `82e7139c0` - [VLM] Support cos sin cache for Ernie4.5-VL (#19743)

- 完整 hash: `82e7139c06a312986d3aa0af0faf0182631c1258`
- 时间/作者: 2026-03-04 / Yuan Luo
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/models/ernie45_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/ernie45_vl.py`
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

### Commit `1a19b3987` - [Model] Add Ernie4.5 VL model support (#15679)

- 完整 hash: `1a19b3987dca941483d7508cae842978d728c737`
- 时间/作者: 2026-01-26 / CSWYF3634076
- 自动分类: 性能/后端优化
- 主要文件: `docs/supported_models/multimodal_language_models.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/models/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/supported_models/multimodal_language_models.md`
  - other: `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/multimodal/processors/ernie45_vl.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/ernie45_vl.py`
  - runtime-perf: `python/sglang/srt/models/ernie45_moe_vl.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
