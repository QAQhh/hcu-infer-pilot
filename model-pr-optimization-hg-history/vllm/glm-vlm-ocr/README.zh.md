# vllm GLM VLM/OCR 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `tests/models/multimodal/processing/test_glm4_1v.py` | `e83b7e379`, `27f4c2fd4`, `b286a311c` |
| `vllm/model_executor/models/glm4_1v.py` | `df7041633`, `bb17e8f11`, `dcd80206b`, `9ad7f89f5`, `e1a34c3a5`, `9ea07b41d`, `2612ba928`, `2972a0547`, `63baa28cf`, `c7c3415a0`, `ad8c07313`, `3bd9c4915`, ... (33 total) |
| `vllm/model_executor/models/glm4v.py` | `df7041633`, `dcd80206b`, `2b8a38b6d`, `9ea07b41d`, `2612ba928`, `700a5ad6c`, `c46b932df`, `e4bb2684b`, `97d1c9930`, `afffd3cc8`, `d0e186c16` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- 生成日期: 2026-05-20
- 文档提交数: 38
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-26 | `bb17e8f11` | 调度/缓存/PD | [GLM-OCR] GLM-OCR with MTP Support (#33005) | `docs/models/supported_models.md`, `examples/offline_inference/vision_language.py`, `tests/models/multimodal/generation/test_common.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-24 | `9ad7f89f5` | 性能/后端优化 | [Models]: Make Multimodal config implicit in ViT implementation (#31972) | `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py` |
| 2026-01-22 | `2b8a38b6d` | 性能/后端优化 | [Model] Extend `collect_children` and `no_init_weights` contexts (#32757) | `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py` |
| 2026-01-20 | `e1a34c3a5` | 模型支持/运行时入口 | [2/N] Initialize MM components in context managers (E-H) (#32641) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/cohere2_vision.py` |
| 2026-01-14 | `9ea07b41d` | 性能/后端优化 | [1/N] Reorganize multimodal processing code (#32327) | `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-08 | `2972a0547` | 模型支持/运行时入口 | [MM Encoder]: Make MMEncoderAttention's `scale` takes effect properly (#31950) | `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py` |
| 2026-01-08 | `63baa28cf` | 模型支持/运行时入口 | [Model] Enable LoRA support for tower and connector in GLM4-V (#31652) | `vllm/model_executor/models/glm4_1v.py` |
| 2026-01-06 | `c7c3415a0` | 模型支持/运行时入口 | 适配glm4_1v量化模型 | `vllm/model_executor/models/glm4_1v.py` |
| 2025-12-19 | `700a5ad6c` | 性能/后端优化 | [MM Encoder]: Migrate legacy ViT `MultiHeadAttention` to new `MMEncoderAttention` interface (#30684) | `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_mha_attn.py`, `tests/v1/tpu/test_mha_attn.py` |
| 2025-12-16 | `ad8c07313` | 性能/后端优化 | [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873) | `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py` |
| 2025-12-16 | `3bd9c4915` | 性能/后端优化 | [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873) | `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py` |
| 2025-12-15 | `87b4d1557` | 性能/后端优化 | [CustomOp][MM] Extract MMEncoderAttention as CustomOp and replace the backend of QwenVisionAttention with it. (#30125) | `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `vllm/attention/layer.py`, `vllm/attention/layers/mm_encoder_attention.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-11 | `36c9ce255` | 模型支持/运行时入口 | Ensure minimum frames for GLM 4.6V compatibility (#30285) | `vllm/model_executor/models/glm4_1v.py` |
| 2025-12-08 | `bcb6f5947` | 性能/后端优化 | [Perf] Remove sync point in vit torch sdpa attn backend (#30232) | `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py` |
| 2025-12-07 | `e83b7e379` | 调度/缓存/PD | Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-07 | `27f4c2fd4` | 调度/缓存/PD | [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145) | `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py` |
| 2025-12-06 | `671427efb` | 调度/缓存/PD | [Model] Move `multimodal_cpu_fields` definition to field config (#30181) | `tests/distributed/test_shm_storage.py`, `tests/multimodal/test_cache.py`, `tests/v1/test_serial_utils.py` |
| 2025-12-06 | `c46b932df` | 性能/后端优化 | [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170) | `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py` |
| 2025-12-05 | `b286a311c` | 调度/缓存/PD | [Chore] Deprecate `merge_by_field_config` arg (#30035) | `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_glm4_1v.py`, `tests/models/multimodal/processing/test_tensor_schema.py` |
| 2025-11-29 | `fe3398fab` | 模型支持/运行时入口 | [Chore] Enable passing `tokenizer=None` into MM processor (#29724) | `tests/multimodal/test_processing.py`, `vllm/entrypoints/openai/serving_engine.py`, `vllm/inputs/preprocess.py` |
| 2025-11-28 | `460d8bbf2` | 性能/后端优化 | Remove upstream fa checks (#29471) | `vllm/attention/layer.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/attention/utils/fa_utils.py` |
| 2025-11-23 | `0ff70821c` | 性能/后端优化 | [Core] Deprecate `xformers` (#29262) | `docker/Dockerfile.nightly_torch`, `docs/contributing/ci/update_pytorch_version.md`, `docs/getting_started/quickstart.md` |
| 2025-11-20 | `0c80efd94` | 模型支持/运行时入口 | GLM-V video segmentation solution adjustment (#28941) | `vllm/model_executor/models/glm4_1v.py` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-19 | `3d4e7d34b` | 性能/后端优化 | [Model][QwenVL] Simplify cos/sin rotary embedding indexing (#28962) | `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py` |
| 2025-11-19 | `e4bb2684b` | 模型支持/运行时入口 | [Models] Replace all `nn.Conv2d` with vLLM's Conv2dLayer (#28842) | `vllm/model_executor/layers/conv.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/blip.py` |
| 2025-11-18 | `b9489f51e` | 性能/后端优化 | [Model][Perf] Use cos and sin cache in QwenVL (#28798) | `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen2_5_vl.py` |
| 2025-11-14 | `41b92f7d3` | 性能/后端优化 | [Model][MM] Extract conv layer as CustomOp (#28455) | `vllm/model_executor/layers/conv.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/glm4_1v.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-11 | `afffd3cc8` | 性能/后端优化 | [Model] Pass `mm_features` directly into `get_mrope_input_positions` (#28399) | `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py` |
| 2025-11-11 | `b30dfa03c` | 性能/后端优化 | [Attention] Refactor CUDA attention backend selection logic (#24794) | `.buildkite/test-pipeline.yaml`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_fusions_e2e.py` |
| 2025-11-11 | `d0e186c16` | 性能/后端优化 | [V0 Deprecation] Remove unused `context_len` and `seq_len` from M-RoPE (#28395) | `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py` |
| 2025-11-04 | `b13a44754` | 性能/后端优化 | [Bugfix][ROCm] Fix ViT rotary embeddings for torch.compile compatibility on ROCm (#27748) | `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/models/glm4_1v.py` |
| 2025-11-01 | `7e06c40e6` | 缺陷修复 | [Bugfix] Fix broken MRoPE for GLM-4.1V/GLM-4.5V (#27860) | `vllm/model_executor/models/glm4_1v.py` |

## 逐 Commit 审计卡

### Commit `df7041633` - sync v0.15.1 (models)

- 完整 hash: `df7041633878cacfcd677cef5efc907705de6c98`
- 时间/作者: 2026-02-06 / zhuwenwen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/bagel.py` 等 169 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 147 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bb17e8f11` - [GLM-OCR] GLM-OCR with MTP Support (#33005)

- 完整 hash: `bb17e8f11c3835fbb930c1669c069d950bec110a`
- 时间/作者: 2026-01-26 / Yuxuan Zhang
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/models/supported_models.md`, `examples/offline_inference/vision_language.py`, `tests/models/multimodal/generation/test_common.py`, `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/glm4.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/models/supported_models.md`; `examples/offline_inference/vision_language.py`
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/speculative.py`; `vllm/model_executor/models/glm4.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glm_ocr.py`; `vllm/model_executor/models/glm_ocr_mtp.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/model_arch_config_convertor.py`
  - tests: `tests/models/multimodal/generation/test_common.py`; `tests/models/multimodal/generation/test_vit_backend_functionality.py`; `tests/models/multimodal/processing/test_common.py`; `tests/models/registry.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `dcd80206b` - [Chore] Update type annotation of `input_ids` in model forward (#33063)

- 完整 hash: `dcd80206b7a9143c81f7f2808e84914f8e38ce95`
- 时间/作者: 2026-01-26 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py` 等 164 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 140 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
  - tests: `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9ad7f89f5` - [Models]: Make Multimodal config implicit in ViT implementation (#31972)

- 完整 hash: `9ad7f89f55b7046d0498608eb85b94b2dc5c2666`
- 时间/作者: 2026-01-24 / Isotr0py
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/eagle2_5_vl.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py` 等 38 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/eagle2_5_vl.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/hunyuan_vision.py` 等 35 个文件
  - runtime-perf: `vllm/model_executor/layers/attention/mm_encoder_attention.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/model_executor/models/qwen3_vl_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2b8a38b6d` - [Model] Extend `collect_children` and `no_init_weights` contexts (#32757)

- 完整 hash: `2b8a38b6d6be4f6e09cc20381c7027e7c35cb6c9`
- 时间/作者: 2026-01-22 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `tests/utils_/test_collection_utils.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/adapters.py`, `vllm/model_executor/models/bagel.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/glm4v.py`, `vllm/model_executor/models/idefics3.py` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/utils/collection_utils.py`
  - runtime-model: `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/adapters.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/gemma3_mm.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/idefics3.py`; `vllm/model_executor/models/interfaces.py` 等 17 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_vl_moe.py`
  - tests: `tests/utils_/test_collection_utils.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e1a34c3a5` - [2/N] Initialize MM components in context managers (E-H) (#32641)

- 完整 hash: `e1a34c3a5d9273431ee182253750d39b546d37a1`
- 时间/作者: 2026-01-20 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/cohere2_vision.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/fuyu.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/gemma3n_mm.py`, `vllm/model_executor/models/glm4_1v.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/cohere2_vision.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/fuyu.py`; `vllm/model_executor/models/gemma3_mm.py`; `vllm/model_executor/models/gemma3n_mm.py`; `vllm/model_executor/models/glm4_1v.py` 等 12 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `9ea07b41d` - [1/N] Reorganize multimodal processing code (#32327)

- 完整 hash: `9ea07b41da169f727a2eb7302adec4c724319522`
- 时间/作者: 2026-01-14 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `docs/api/README.md`, `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md`, `tests/multimodal/test_processing.py`, `vllm/benchmarks/mm_processor.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py` 等 76 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/api/README.md`; `docs/contributing/model/multimodal.md`; `docs/design/mm_processing.md`
  - other: `vllm/benchmarks/mm_processor.py`; `vllm/multimodal/inputs.py`; `vllm/multimodal/processing/__init__.py`; `vllm/multimodal/processing/context.py`; `vllm/multimodal/processing/dummy_inputs.py`; `vllm/multimodal/processing/processor.py`; `vllm/multimodal/registry.py`; `vllm/v1/engine/input_processor.py`
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/blip2.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/cohere2_vision.py` 等 62 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/multimodal/cache.py`
  - tests: `tests/multimodal/test_processing.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2612ba928` - [1/N][Attention] Restructure attention: move files (#31916)

- 完整 hash: `2612ba9285d828f3179801334b6d2db0046b9b6c`
- 时间/作者: 2026-01-09 / Matthew Bonanni
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml`, `.github/CODEOWNERS`, `.github/mergify.yml`, `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`, `docs/contributing/model/basic.md`, `docs/design/custom_op.md` 等 195 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/kernels.yaml`; `.github/CODEOWNERS`; `.github/mergify.yml`
  - docs-bench: `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`; `docs/contributing/model/basic.md`; `docs/design/custom_op.md`; `docs/design/plugin_system.md`; `examples/offline_inference/basic/embed.py`; `examples/offline_inference/basic/score.py`
  - other: `tools/pre_commit/mypy.py`; `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/xpu.py`; `vllm/v1/kv_offload/cpu.py` 等 10 个文件
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/layers/batch_invariant.py`; `vllm/model_executor/layers/kda.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/short_conv.py` 等 66 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/ops/__init__.py`; `vllm/config/attention.py`; `vllm/distributed/kv_transfer/kv_connector/utils.py`; `vllm/distributed/kv_transfer/kv_connector/v1/base.py`; `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py` 等 73 个文件
  - tests: `tests/compile/fullgraph/test_full_cudagraph.py`; `tests/compile/fullgraph/test_full_graph.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/config/test_multimodal_config.py`; `tests/engine/test_arg_utils.py`; `tests/kernels/attention/test_aiter_flash_attn.py`; `tests/kernels/attention/test_attention.py` 等 35 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `2972a0547` - [MM Encoder]: Make MMEncoderAttention's `scale` takes effect properly  (#31950)

- 完整 hash: `2972a05473d64a21c7390a5676bbb07bd8d2c8da`
- 时间/作者: 2026-01-08 / Isotr0py
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glmasr.py`, `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/moonvit.py` 等 11 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glmasr.py`; `vllm/model_executor/models/isaac.py`; `vllm/model_executor/models/moonvit.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_vl.py` 等 9 个文件
  - runtime-perf: `vllm/attention/layers/mm_encoder_attention.py`; `vllm/attention/ops/vit_attn_wrappers.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `63baa28cf` - [Model] Enable LoRA support for tower and connector in GLM4-V (#31652)

- 完整 hash: `63baa28cf5a95788f0a9237721b9d569bce39148`
- 时间/作者: 2026-01-08 / Zyyeric
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/glm4_1v.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c7c3415a0` - 适配glm4_1v量化模型

- 完整 hash: `c7c3415a00b1afa683053ad6c04a5e01e99bc25b`
- 时间/作者: 2026-01-06 / zhuwenwen
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/glm4_1v.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `700a5ad6c` - [MM Encoder]: Migrate legacy ViT `MultiHeadAttention` to new `MMEncoderAttention` interface (#30684)

- 完整 hash: `700a5ad6c616358f42db7d9b55e8bc9caa140ca5`
- 时间/作者: 2025-12-19 / Isotr0py
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_mha_attn.py`, `tests/v1/tpu/test_mha_attn.py`, `vllm/attention/layer.py`, `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/blip.py` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/aimv2.py`; `vllm/model_executor/models/blip.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/hunyuan_vision.py`; `vllm/model_executor/models/idefics2_vision_model.py`; `vllm/model_executor/models/intern_vit.py` 等 14 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/layers/mm_encoder_attention.py`; `vllm/attention/ops/vit_attn_wrappers.py`
  - tests: `tests/kernels/attention/test_attention.py`; `tests/kernels/attention/test_mha_attn.py`; `tests/v1/tpu/test_mha_attn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ad8c07313` - [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873)

- 完整 hash: `ad8c073131f52365ca9917b546f39185f39a49cb`
- 时间/作者: 2025-12-16 / Shanshan Shen
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`, `vllm/model_executor/layers/rotary_embedding/xdrope.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/layers/rotary_embedding/common.py`; `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`; `vllm/model_executor/layers/rotary_embedding/mrope.py`; `vllm/model_executor/layers/rotary_embedding/xdrope.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py` 等 13 个文件
  - tests: `tests/kernels/core/test_apply_rotary_emb.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3bd9c4915` - [CustomOp] Extract ApplyRotaryEmb as CustomOp and unify the dispatch logic (#29873)

- 完整 hash: `3bd9c491583d45ae9f3f24b10e99626f502014b4`
- 时间/作者: 2025-12-16 / Shanshan Shen
- 自动分类: 性能/后端优化
- 主要文件: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`, `vllm/model_executor/layers/rotary_embedding/xdrope.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/layers/rotary_embedding/common.py`; `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`; `vllm/model_executor/layers/rotary_embedding/mrope.py`; `vllm/model_executor/layers/rotary_embedding/xdrope.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py` 等 13 个文件
  - tests: `tests/kernels/core/test_apply_rotary_emb.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `87b4d1557` - [CustomOp][MM] Extract MMEncoderAttention as CustomOp and replace the backend of QwenVisionAttention with it. (#30125)

- 完整 hash: `87b4d1557dc83addf5dd8568862ee7a74882200a`
- 时间/作者: 2025-12-15 / Shanshan Shen
- 自动分类: 性能/后端优化
- 主要文件: `tests/models/multimodal/generation/test_vit_backend_functionality.py`, `vllm/attention/layer.py`, `vllm/attention/layers/mm_encoder_attention.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/keye.py` 等 24 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/platforms/interface.py`; `vllm/platforms/tpu.py`; `vllm/platforms/xpu.py`
  - runtime-model: `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/opencua.py`; `vllm/model_executor/models/ovis2_5.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 13 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/layers/mm_encoder_attention.py`; `vllm/attention/ops/vit_attn_wrappers.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/model_executor/models/qwen3_vl_moe.py`; `vllm/platforms/cuda.py`; `vllm/platforms/rocm.py`
  - tests: `tests/models/multimodal/generation/test_vit_backend_functionality.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cf3eacfe5` - Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389)

- 完整 hash: `cf3eacfe58fa9e745c2854782ada884a9f992cf7`
- 时间/作者: 2025-12-11 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `vllm/config/utils.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/afmoe.py` 等 83 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `benchmarks/kernels/benchmark_rope.py`
  - runtime-model: `vllm/config/utils.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/olmoe.py` 等 12 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `36c9ce255` - Ensure minimum frames for GLM 4.6V compatibility (#30285)

- 完整 hash: `36c9ce25543b4f48194d7adc4ba3d17f5b6102be`
- 时间/作者: 2025-12-11 / gh-wf
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/glm4_1v.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `bcb6f5947` - [Perf] Remove sync point in vit torch sdpa attn backend (#30232)

- 完整 hash: `bcb6f5947f8acac22f5d1d5fc92a91b06fd57e77`
- 时间/作者: 2025-12-08 / Dazhi Jiang
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen2_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/qwen2_vl.py`
  - runtime-perf: `vllm/attention/ops/vit_attn_wrappers.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e83b7e379` - Revert "[Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)" (#30199)

- 完整 hash: `e83b7e379c11bf136c1b96bc6a67b6d2207cfde4`
- 时间/作者: 2025-12-07 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py`, `tests/compile/test_fusion.py`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_pass_manager.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/distributed/test_kvlayout.py` 等 105 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/transcription.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/processor.py`; `vllm/v1/engine/async_llm.py` 等 12 个文件
  - runtime-model: `vllm/config/__init__.py`; `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/config/renderer.py`; `vllm/config/speculative.py`; `vllm/config/vllm.py`; `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py` 等 33 个文件
  - runtime-perf: `vllm/multimodal/cache.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/compile/distributed/test_sequence_parallelism.py`; `tests/compile/test_functionalization.py`; `tests/compile/test_fusion.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_pass_manager.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/distributed/test_kvlayout.py`; `tests/entrypoints/openai/test_chat_template.py` 等 56 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `27f4c2fd4` - [Renderer] Separate out `RendererConfig` from `ModelConfig` (#30145)

- 完整 hash: `27f4c2fd46b99778d7ea19dfe7751fbaab615177`
- 时间/作者: 2025-12-07 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/contributing/model/transcription.md`, `tests/compile/distributed/test_sequence_parallelism.py`, `tests/compile/test_functionalization.py`, `tests/compile/test_fusion.py`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_pass_manager.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/distributed/test_kvlayout.py` 等 105 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/transcription.md`
  - other: `vllm/engine/arg_utils.py`; `vllm/engine/protocol.py`; `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`; `vllm/tokenizers/registry.py`; `vllm/transformers_utils/processor.py`; `vllm/v1/engine/async_llm.py` 等 12 个文件
  - runtime-model: `vllm/config/__init__.py`; `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/config/renderer.py`; `vllm/config/speculative.py`; `vllm/config/vllm.py`; `vllm/entrypoints/chat_utils.py`; `vllm/entrypoints/llm.py` 等 33 个文件
  - runtime-perf: `vllm/multimodal/cache.py`; `vllm/v1/core/encoder_cache_manager.py`; `vllm/v1/core/sched/scheduler.py`
  - tests: `tests/compile/distributed/test_sequence_parallelism.py`; `tests/compile/test_functionalization.py`; `tests/compile/test_fusion.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_pass_manager.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/distributed/test_kvlayout.py`; `tests/entrypoints/openai/test_chat_template.py` 等 56 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `671427efb` - [Model] Move `multimodal_cpu_fields` definition to field config (#30181)

- 完整 hash: `671427efbf57d4e40370a336cf1d3a4d1fd8eb91`
- 时间/作者: 2025-12-06 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/distributed/test_shm_storage.py`, `tests/multimodal/test_cache.py`, `tests/v1/test_serial_utils.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/hunyuan_vision.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/opencua.py`, `vllm/model_executor/models/qwen2_5_vl.py` 等 15 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/utils.py`; `vllm/v1/serial_utils.py`
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/hunyuan_vision.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/opencua.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/v1/worker/gpu_model_runner.py` 等 9 个文件
  - tests: `tests/distributed/test_shm_storage.py`; `tests/multimodal/test_cache.py`; `tests/v1/test_serial_utils.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c46b932df` - [Chore] Deprecate `SupportsMultiModal.merge_by_field_config` (#30170)

- 完整 hash: `c46b932df2b801ba0a6452e436268f086029d82b`
- 时间/作者: 2025-12-06 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/blip2.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/cohere2_vision.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/deepseek_vl2.py` 等 61 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/utils.py`
  - runtime-model: `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/blip2.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/cohere2_vision.py`; `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/deepseek_vl2.py` 等 59 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b286a311c` - [Chore] Deprecate `merge_by_field_config` arg (#30035)

- 完整 hash: `b286a311c2bab639ce6edc998a9a67c0affc9cbf`
- 时间/作者: 2025-12-05 / Cyrus Leung
- 自动分类: 调度/缓存/PD
- 主要文件: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_glm4_1v.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/multimodal/test_cache.py`, `tests/multimodal/test_inputs.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/lightonocr.py` 等 19 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/inputs.py`; `vllm/multimodal/utils.py`; `vllm/v1/serial_utils.py`
  - runtime-model: `vllm/model_executor/models/deepseek_ocr.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/lightonocr.py`; `vllm/model_executor/models/nano_nemotron_vl.py`; `vllm/model_executor/models/opencua.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/paligemma.py`; `vllm/model_executor/models/qwen2_5_vl.py` 等 10 个文件
  - runtime-perf: `vllm/multimodal/cache.py`
  - tests: `tests/models/multimodal/processing/test_common.py`; `tests/models/multimodal/processing/test_glm4_1v.py`; `tests/models/multimodal/processing/test_tensor_schema.py`; `tests/multimodal/test_cache.py`; `tests/multimodal/test_inputs.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fe3398fab` - [Chore] Enable passing `tokenizer=None` into MM processor (#29724)

- 完整 hash: `fe3398fab2b11f92b4ada209a85558710c446a36`
- 时间/作者: 2025-11-29 / Cyrus Leung
- 自动分类: 模型支持/运行时入口
- 主要文件: `tests/multimodal/test_processing.py`, `vllm/entrypoints/openai/serving_engine.py`, `vllm/inputs/preprocess.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/qwen_vl.py`, `vllm/multimodal/processing.py`, `vllm/multimodal/registry.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/inputs/preprocess.py`; `vllm/multimodal/processing.py`; `vllm/multimodal/registry.py`
  - runtime-model: `vllm/entrypoints/openai/serving_engine.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/model_executor/models/qwen_vl.py`
  - tests: `tests/multimodal/test_processing.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `460d8bbf2` - Remove upstream fa checks (#29471)

- 完整 hash: `460d8bbf2d19fc4757b3253050a0a18b61c136e3`
- 时间/作者: 2025-11-28 / Mingyuan Ma
- 自动分类: 性能/后端优化
- 主要文件: `vllm/attention/layer.py`, `vllm/attention/ops/vit_attn_wrappers.py`, `vllm/attention/utils/fa_utils.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/paddleocr_vl.py` 等 13 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py` 等 9 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/ops/vit_attn_wrappers.py`; `vllm/attention/utils/fa_utils.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0ff70821c` - [Core] Deprecate `xformers` (#29262)

- 完整 hash: `0ff70821c9b0b991197fa7f3264bf9dd78b8d4b3`
- 时间/作者: 2025-11-23 / Roger Wang
- 自动分类: 性能/后端优化
- 主要文件: `docker/Dockerfile.nightly_torch`, `docs/contributing/ci/update_pytorch_version.md`, `docs/getting_started/quickstart.md`, `examples/online_serving/openai_embedding_long_text/service.sh`, `requirements/cuda.txt`, `tests/basic_correctness/test_basic_correctness.py`, `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_attention_selector.py` 等 31 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/ci/update_pytorch_version.md`; `docs/getting_started/quickstart.md`; `examples/online_serving/openai_embedding_long_text/service.sh`
  - other: `docker/Dockerfile.nightly_torch`; `vllm/envs.py`; `vllm/utils/__init__.py`
  - runtime-model: `vllm/config/multimodal.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/pixtral.py`; `vllm/model_executor/models/qwen2_5_vl.py` 等 10 个文件
  - runtime-perf: `requirements/cuda.txt`; `vllm/attention/backends/registry.py`; `vllm/attention/layer.py`; `vllm/attention/ops/vit_attn_wrappers.py`; `vllm/attention/selector.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/platforms/cuda.py`; `vllm/v1/attention/backends/xformers.py`
  - tests: `tests/basic_correctness/test_basic_correctness.py`; `tests/kernels/attention/test_attention.py`; `tests/kernels/attention/test_attention_selector.py`; `tests/kernels/attention/test_mha_attn.py`; `tests/kernels/utils.py`; `tests/lora/test_minicpmv_tp.py`; `tests/lora/test_qwen2vl.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0c80efd94` - GLM-V video segmentation solution adjustment (#28941)

- 完整 hash: `0c80efd94fb8c17cfc7d1bcb9cdb65f154340994`
- 时间/作者: 2025-11-20 / Yuxuan Zhang
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/models/glm4_1v.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `a8b70304d` - Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542)

- 完整 hash: `a8b70304d68497ac1c432a2ff343e9bfb516c227`
- 时间/作者: 2025-11-19 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/language/pooling/test_nomic_max_model_len.py` 等 104 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `examples/offline_inference/context_extension.py`
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py` 等 78 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 17 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; `tests/models/language/pooling/test_nomic_max_model_len.py`; `tests/test_config.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `3d4e7d34b` - [Model][QwenVL] Simplify cos/sin rotary embedding indexing  (#28962)

- 完整 hash: `3d4e7d34be856cc4f54033e6a019059afacb5e76`
- 时间/作者: 2025-11-19 / Lukas Geiger
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e4bb2684b` - [Models] Replace all `nn.Conv2d` with vLLM's Conv2dLayer (#28842)

- 完整 hash: `e4bb2684bcea12f72a36a6c48292f79534af849a`
- 时间/作者: 2025-11-19 / Isotr0py
- 自动分类: 模型支持/运行时入口
- 主要文件: `vllm/model_executor/layers/conv.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/blip.py`, `vllm/model_executor/models/chameleon.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/conv.py`; `vllm/model_executor/models/aimv2.py`; `vllm/model_executor/models/blip.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/deepencoder.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glm4v.py` 等 20 个文件
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `b9489f51e` - [Model][Perf] Use cos and sin cache in QwenVL (#28798)

- 完整 hash: `b9489f51e1c61c96378e12c9523f9de7043ca294`
- 时间/作者: 2025-11-18 / Canlin Guo
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/rotary_embedding/base.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/base.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `41b92f7d3` - [Model][MM] Extract conv layer as CustomOp (#28455)

- 完整 hash: `41b92f7d38d3f056004991c026f6a24846755ef4`
- 时间/作者: 2025-11-14 / Shanshan Shen
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/conv.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/vision.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/conv.py`; `vllm/model_executor/models/clip.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/qwen2_5_vl.py`; `vllm/model_executor/models/qwen2_vl.py`; `vllm/model_executor/models/qwen3_vl.py`; `vllm/model_executor/models/vision.py`
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `97d1c9930` - Rename clashing method names for vLLM model protocol (#27583)

- 完整 hash: `97d1c99302df6f7eadc0d0b32ec174db69cb4421`
- 时间/作者: 2025-11-13 / Harry Mellor
- 自动分类: 性能/后端优化
- 主要文件: `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/baichuan.py` 等 164 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/contributing/model/basic.md`; `docs/contributing/model/multimodal.md`
  - other: `vllm/multimodal/processing.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/bert.py` 等 144 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 16 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `afffd3cc8` - [Model] Pass `mm_features` directly into `get_mrope_input_positions` (#28399)

- 完整 hash: `afffd3cc8a99ce1cf0f6f1687852e5519d725a3b`
- 时间/作者: 2025-11-11 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/keye_vl1_5.py`, `vllm/model_executor/models/paddleocr_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 15 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `vllm/multimodal/inputs.py`
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/keye_vl1_5.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 13 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b30dfa03c` - [Attention] Refactor CUDA attention backend selection logic (#24794)

- 完整 hash: `b30dfa03c564ce51c56bf2dd16283f074253c27c`
- 时间/作者: 2025-11-11 / Matthew Bonanni
- 自动分类: 性能/后端优化
- 主要文件: `.buildkite/test-pipeline.yaml`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_fusions_e2e.py`, `tests/config/test_multimodal_config.py`, `tests/kernels/attention/test_attention_selector.py`, `tests/kernels/attention/test_mha_attn.py`, `tests/models/test_initialization.py`, `tests/v1/attention/test_attention_backends.py` 等 61 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.buildkite/test-pipeline.yaml`
  - other: `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/tpu.py`; `vllm/platforms/xpu.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/models/dots_ocr.py`; `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/ovis2_5.py`; `vllm/model_executor/models/paddleocr_vl.py` 等 14 个文件
  - runtime-perf: `vllm/attention/backends/abstract.py`; `vllm/attention/backends/registry.py`; `vllm/attention/layer.py`; `vllm/attention/selector.py`; `vllm/config/cache.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/model_executor/models/qwen3_omni_moe_thinker.py`; `vllm/platforms/cuda.py` 等 26 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_fusions_e2e.py`; `tests/config/test_multimodal_config.py`; `tests/kernels/attention/test_attention_selector.py`; `tests/kernels/attention/test_mha_attn.py`; `tests/models/test_initialization.py`; `tests/v1/attention/test_attention_backends.py`; `tests/v1/attention/test_mla_backends.py` 等 13 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d0e186c16` - [V0 Deprecation] Remove unused `context_len` and `seq_len` from M-RoPE (#28395)

- 完整 hash: `d0e186c16f0d62af8c128e2dc7c94cde1387ac02`
- 时间/作者: 2025-11-11 / Cyrus Leung
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm4v.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/keye.py`, `vllm/model_executor/models/keye_vl1_5.py`, `vllm/model_executor/models/paddleocr_vl.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 13 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/ernie45_vl.py`; `vllm/model_executor/models/glm4_1v.py`; `vllm/model_executor/models/glm4v.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/keye.py`; `vllm/model_executor/models/keye_vl1_5.py`; `vllm/model_executor/models/paddleocr_vl.py`; `vllm/model_executor/models/qwen2_5_omni_thinker.py` 等 12 个文件
  - runtime-perf: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `b13a44754` - [Bugfix][ROCm] Fix ViT rotary embeddings for torch.compile compatibility on ROCm (#27748)

- 完整 hash: `b13a44754674a0056d7c8113deb33ea858f6ef1c`
- 时间/作者: 2025-11-04 / vllmellm
- 自动分类: 性能/后端优化
- 主要文件: `vllm/model_executor/layers/rotary_embedding/common.py`, `vllm/model_executor/models/glm4_1v.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/common.py`; `vllm/model_executor/models/glm4_1v.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `7e06c40e6` - [Bugfix] Fix broken MRoPE for GLM-4.1V/GLM-4.5V (#27860)

- 完整 hash: `7e06c40e63c12c0ea5fb400fa8f06007e90ff84f`
- 时间/作者: 2025-11-01 / Isotr0py
- 自动分类: 缺陷修复
- 主要文件: `vllm/model_executor/models/glm4_1v.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `vllm/model_executor/models/glm4_1v.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。
