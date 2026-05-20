# sglang Nemotron Super 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/configs/jet_nemotron.py` | `6b8a6545b`, `44603764d` |
| `python/sglang/srt/configs/nano_nemotron_vl.py` | 无直接提交 |
| `python/sglang/srt/configs/nemotron_h.py` | `1ac6a2646`, `f8bbf56de`, `44603764d`, `b02133233` |
| `python/sglang/srt/models/jet_nemotron.py` | `d1e95af28` |
| `python/sglang/srt/models/nano_nemotron_vl.py` | `bebd625ba` |
| `python/sglang/srt/models/nemotron_h.py` | `466ff20e5`, `25bd83033`, `33c33a7de`, `0ff24159a`, `72bacc88c`, `ba625c2d9`, `b02133233`, `47a660d5b` |
| `python/sglang/srt/models/nemotron_h_mtp.py` | `4c95953b7`, `ba625c2d9` |
| `python/sglang/srt/models/nemotron_nas.py` | `d1e95af28`, `07a24f1a3` |
| `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py` | `4a757990a`, `bebd625ba` |
| `test/lm_eval_configs/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16.yaml` | `c6aa1863b` |
| `test/lm_eval_configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml` | `c6aa1863b` |
| `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py` | `e3a4a09c7`, `3879c466b`, `3e643967e` |
| `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_bf16.py` | `3879c466b`, `3e643967e` |
| `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_nightly.py` | `3879c466b` |
| `test/registered/models/test_nvidia_nemotron_3_nano.py` | `814202704`, `82a0bafc1`, `c6aa1863b` |
| `test/registered/models/test_nvidia_nemotron_nano_v2.py` | `fb90c9d29`, `814202704`, `63cc97f4e` |
| `test/registered/models/test_nvidia_nemotron_nano_v2_vl.py` | `fb90c9d29`, `814202704`, `146b5fcc8`, `f8411ded6` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 39
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-26 | `e3a4a09c7` | 缺陷修复 | [CI] Fix nemotron nvfp4 test estimated time (#21516) | `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py` |
| 2026-03-26 | `fb90c9d29` | 性能/后端优化 | [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047) | `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py` |
| 2026-03-25 | `77872a8d5` | 调度/缓存/PD | Update Nemotron Example docs to include Super v3 and Nano 4B (#21416) | `docs/supported_models/text_generation/generative_models.md` |
| 2026-03-23 | `814202704` | 性能/后端优化 | ci: unify PR test suite naming (#21187) | `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml` |
| 2026-03-18 | `6b8a6545b` | 性能/后端优化 | Add Mistral Small 4 (Pixtral) support (#20708) | `benchmark/mmmu/bench_sglang.py`, `benchmark/mmmu/eval_utils.py`, `python/sglang/srt/configs/deepseek_ocr.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-17 | `466ff20e5` | 缺陷修复 | [Model] Fix NemotronH OOM on unified-mem systems: stream weights + safetensors cleanup (#20580) | `python/sglang/srt/models/nemotron_h.py` |
| 2026-03-16 | `5ef580616` | 缺陷修复 | [Nemotron] Small reasoning parser fix (#20284) | `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py` |
| 2026-03-16 | `3879c466b` | 模型支持/运行时入口 | [CI] Add Nemotron 3 Super 120B nightly 8-GPU tests (#20616) | `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`, `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_bf16.py`, `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_nightly.py` |
| 2026-03-15 | `1ac6a2646` | 缺陷修复 | fix: Nemotron chunk size alias (#20458) | `python/sglang/srt/configs/nemotron_h.py` |
| 2026-03-15 | `3e643967e` | 模型支持/运行时入口 | [CI] Add Nemotron 3 Super 120B CI tests for BF16 and NVFP4 (#20575) | `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`, `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_bf16.py` |
| 2026-03-14 | `75a7879fd` | 性能/后端优化 | [Model] Support Nemotron 3 Super NVFP4 (#20407) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py` |
| 2026-03-11 | `25bd83033` | 性能/后端优化 | Enable Piecewise CUDA Graph for NemotronH Hybrid (Mamba+Attention) Models (#19903) | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-03-09 | `4a757990a` | 性能/后端优化 | [VLM] Replace decord with torchcodec for video decoding (#20055) | `examples/runtime/multimodal/llava_onevision_server.py`, `python/pyproject.toml`, `python/pyproject_cpu.toml` |
| 2026-03-07 | `f8bbf56de` | 模型支持/运行时入口 | Refactor NemotronHConfig to canonical layers_block_type and add MTP block-type support (#19950) | `python/sglang/srt/configs/nemotron_h.py` |
| 2026-03-05 | `ff6048fb9` | 模型支持/运行时入口 | rename nemotron reasoning parser (#19865) | `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/parser/reasoning_parser.py` |
| 2026-03-03 | `4c95953b7` | 性能/后端优化 | Fix/nemotron mtp quantaized (#19433) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/unquant.py` |
| 2026-02-21 | `33c33a7de` | 性能/后端优化 | [Quantization] Support config.json quantization_config format, fix exclude_modules matching, and fix KV cache scale loading for Nemotron (#18546) | `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-02-19 | `82a0bafc1` | 性能/后端优化 | Feat/add fi selective state update kernel call (#18070) | `python/sglang/srt/layers/attention/mamba/ops/__init__.py`, `python/sglang/srt/layers/attention/mamba/ops/ssu_dispatch.py`, `python/sglang/srt/managers/scheduler.py` |
| 2026-02-16 | `0ff24159a` | 性能/后端优化 | Fix modelopt FP8 create weights (#18447) | `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-02-11 | `44603764d` | 缺陷修复 | fix(config): Support setting Mamba state dtype via config file (#18532) | `python/sglang/srt/configs/falcon_h1.py`, `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/configs/lfm2.py` |
| 2026-02-06 | `c6aa1863b` | 模型支持/运行时入口 | Add Nemotron 3 Nano tests (#18119) | `python/pyproject.toml`, `python/sglang/test/kits/lm_eval_kit.py`, `test/lm_eval_configs/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16.yaml` |
| 2026-01-15 | `146b5fcc8` | 性能/后端优化 | [CI] Reorganize stage-b 1-GPU tests for 5090 compatibility (#16826) | `.github/workflows/pr-test.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py` |
| 2026-01-14 | `72bacc88c` | 模型支持/运行时入口 | [NemotronH] Use ReplicatedLinear for fc1_latent_proj (#16569) | `python/sglang/srt/models/nemotron_h.py` |
| 2026-01-14 | `ba625c2d9` | 模型支持/运行时入口 | Feat/support nemotron h mtp (#17013) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/nemotron_h.py` |
| 2026-01-09 | `5dcff9479` | 缺陷修复 | [nemetron/mtp] fix nemotron mtp (#16275) | `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/attention/mamba/ops/mamba_ssm.py`, `python/sglang/srt/server_args.py` |
| 2026-01-08 | `8726d30cb` | 模型支持/运行时入口 | [smg] Add Nemotron Nano V3 reasoning parser support (#16763) | `sgl-model-gateway/src/reasoning_parser/factory.rs` |
| 2026-01-07 | `63cc97f4e` | 调度/缓存/PD | ci: migrate 2-GPU tests to test/registered/ (#16529) | `.github/workflows/pr-test.yml`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/model_loader/weight_utils.py` |
| 2026-01-05 | `bebd625ba` | 调度/缓存/PD | EVS Framework: Support NemotronH_Nano_VL_V2 (#14051) | `docs/supported_models/multimodal_language_models.md`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/managers/mm_utils.py` |
| 2026-01-04 | `f8411ded6` | 模型支持/运行时入口 | ci: migrate 1-GPU model tests to test/registered/models/ (#16414) | `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `docker/xeon.Dockerfile` |
| 2026-01-02 | `b02133233` | 性能/后端优化 | [NemotronH] Add latent MoE support (#16227) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1344,device_name=NVIDIA_B200.json` |
| 2025-12-31 | `417e75a60` | 缺陷修复 | fix: use 2-gpu-runner for pp 2 NemotronH ut (#16239) | `test/srt/run_suite.py` |
| 2025-12-31 | `47a660d5b` | 模型支持/运行时入口 | [NemotronH] PP support (#16172) | `python/sglang/srt/models/nemotron_h.py`, `test/srt/models/test_nvidia_nemotron_nano_v2.py` |
| 2025-12-28 | `5969be2f0` | 缺陷修复 | Apply fixture-kit mode to MMMUVLMMixin (#15615) | `python/sglang/srt/environ.py`, `python/sglang/test/kits/mmmu_vlm_kit.py`, `python/sglang/test/server_fixtures/mmmu_fixture.py` |
| 2025-12-27 | `183b65190` | 调度/缓存/PD | Clean up logging (#15919) | `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/managers/tokenizer_manager.py` |
| 2025-12-25 | `de03b0cd3` | 性能/后端优化 | [Nemotron 3 Nano] Add triton MoE configs (#15815) | `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1856,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1856,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=232,device_name=NVIDIA_B200.json` |
| 2025-12-24 | `bd572360f` | 模型支持/运行时入口 | Tiny apply gsm8k mixin to ngram test (#15606) | `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/spec/test_ngram_speculative_decoding.py`, `test/srt/models/test_ministral3_models.py` |
| 2025-12-22 | `beae3f961` | 缺陷修复 | Adapt fixture-kit to gsm8k mixin (#15599) | `python/sglang/test/gsm8k_mixin.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `python/sglang/test/kits/mmmu_vlm_kit.py` |

## 逐 Commit 审计卡

### Commit `e3a4a09c7` - [CI] Fix nemotron nvfp4 test estimated time (#21516)

- 完整 hash: `e3a4a09c7b923024db3c834f82b4f30bba53ddde`
- 时间/作者: 2026-03-26 / Baizhou Zhang
- 自动分类: 缺陷修复
- 主要文件: `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `fb90c9d29` - [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047)

- 完整 hash: `fb90c9d298eeeb15fde5de1c7676cfc3d9a4b6ee`
- 时间/作者: 2026-03-26 / Liangsheng Yin
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/test/kits/eval_accuracy_kit.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_mimo_models.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `77872a8d5` - Update Nemotron Example docs to include Super v3 and Nano 4B (#21416)

- 完整 hash: `77872a8d55081c235e4b45397f9e3bf6af75c17a`
- 时间/作者: 2026-03-25 / Nave Assaf
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/supported_models/text_generation/generative_models.md`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/supported_models/text_generation/generative_models.md`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `814202704` - ci: unify PR test suite naming (#21187)

- 完整 hash: `814202704bf21525b5ae07029cb475da4c87f3b7`
- 时间/作者: 2026-03-23 / Lianmin Zheng
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`, `scripts/ci/utils/slash_command_handler.py`, `test/README.md` 等 283 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/actions/wait-for-jobs/action.yml`; `.github/workflows/pr-test-amd-rocm720.yml`; `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/jit_kernel/tests/test_moe_lora_align_block_size.py`; `test/README.md`; `test/registered/amd/disaggregation/test_disaggregation_basic.py`; `test/registered/attention/test_chunk_gated_delta_rule.py`; `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_hybrid_attn_backend.py` 等 278 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `6b8a6545b` - Add Mistral Small 4 (Pixtral) support (#20708)

- 完整 hash: `6b8a6545b231e175a9534ee50ed57fcd6d5b75e5`
- 时间/作者: 2026-03-18 / Xinyuan Tong
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/mmmu/bench_sglang.py`, `benchmark/mmmu/eval_utils.py`, `python/sglang/srt/configs/deepseek_ocr.py`, `python/sglang/srt/configs/deepseekvl2.py`, `python/sglang/srt/configs/janus_pro.py`, `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` 等 18 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/mmmu/bench_sglang.py`; `benchmark/mmmu/eval_utils.py`
  - other: `python/sglang/srt/function_call/mistral_detector.py`; `python/sglang/srt/multimodal/processors/pixtral.py`; `python/sglang/srt/parser/reasoning_parser.py`; `python/sglang/srt/utils/hf_transformers_utils.py`; `python/sglang/srt/utils/mistral_utils.py`
  - runtime-model: `python/sglang/srt/configs/deepseek_ocr.py`; `python/sglang/srt/configs/deepseekvl2.py`; `python/sglang/srt/configs/janus_pro.py`; `python/sglang/srt/configs/jet_nemotron.py`; `python/sglang/srt/entrypoints/openai/protocol.py`; `python/sglang/srt/entrypoints/openai/serving_chat.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/mistral_large_3_eagle.py` 等 10 个文件
  - runtime-perf: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
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

### Commit `466ff20e5` - [Model] Fix NemotronH OOM on unified-mem systems: stream weights + safetensors cleanup (#20580)

- 完整 hash: `466ff20e51489883625a9b11e832fe7775d2c88e`
- 时间/作者: 2026-03-17 / Serge Panev
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/nemotron_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/nemotron_h.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5ef580616` - [Nemotron] Small reasoning parser fix (#20284)

- 完整 hash: `5ef58061609ab7a73cd75a7ac1fe63ea4ef63f43`
- 时间/作者: 2026-03-16 / roikoren755
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/parser/reasoning_parser.py`
  - tests: `test/registered/unit/parser/test_reasoning_parser.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `3879c466b` - [CI] Add Nemotron 3 Super 120B nightly 8-GPU tests (#20616)

- 完整 hash: `3879c466b432be81088d72ccb9f1ea8cdec99205`
- 时间/作者: 2026-03-16 / Mohammad Miadh Angkad
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`, `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_bf16.py`, `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_nightly.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`; `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_bf16.py`; `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_nightly.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `1ac6a2646` - fix: Nemotron chunk size alias (#20458)

- 完整 hash: `1ac6a26464370847c2e3f3bb78c881324bd0644d`
- 时间/作者: 2026-03-15 / shuwenn
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/configs/nemotron_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/nemotron_h.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3e643967e` - [CI] Add Nemotron 3 Super 120B CI tests for BF16 and NVFP4 (#20575)

- 完整 hash: `3e643967e6d7696b03e05610dc7420356be06d98`
- 时间/作者: 2026-03-15 / Mohammad Miadh Angkad
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`, `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_bf16.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`; `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_bf16.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `75a7879fd` - [Model] Support Nemotron 3 Super NVFP4 (#20407)

- 完整 hash: `75a7879fd4c149e675b50f9b21964e557577cc4f`
- 时间/作者: 2026-03-14 / Mohammad Miadh Angkad
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/server_args.py`, `test/registered/model_loading/test_modelopt_loader.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/model_loader/loader.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/__init__.py`; `python/sglang/srt/layers/quantization/modelopt_quant.py`
  - tests: `test/registered/model_loading/test_modelopt_loader.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `25bd83033` - Enable Piecewise CUDA Graph for NemotronH Hybrid (Mamba+Attention) Models (#19903)

- 完整 hash: `25bd83033d098cee4706449f77bc5120d188003b`
- 时间/作者: 2026-03-11 / Vedant V Jhaveri
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/nemotron_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/nemotron_h.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `f8bbf56de` - Refactor NemotronHConfig to canonical layers_block_type and add MTP block-type support (#19950)

- 完整 hash: `f8bbf56de7b2bbbea959334e2a24f4bef06d0034`
- 时间/作者: 2026-03-07 / danielafrimi
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/configs/nemotron_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/nemotron_h.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ff6048fb9` - rename  nemotron reasoning parser (#19865)

- 完整 hash: `ff6048fb9c3fda17f7f0048bc6dce58993e8ede0`
- 时间/作者: 2026-03-05 / danielafrimi
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/parser/reasoning_parser.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/parser/reasoning_parser.py`
  - runtime-model: `python/sglang/srt/entrypoints/openai/serving_chat.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `4c95953b7` - Fix/nemotron mtp quantaized (#19433)

- 完整 hash: `4c95953b77335f42eae5d3b59a00279008a6e639`
- 时间/作者: 2026-03-03 / Shaun Kotek
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `test/registered/model_loading/test_modelopt_loader.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/models/nemotron_h_mtp.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/quantization/unquant.py`
  - tests: `test/registered/model_loading/test_modelopt_loader.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `33c33a7de` - [Quantization] Support config.json quantization_config format, fix exclude_modules matching, and fix KV cache scale loading for Nemotron (#18546)

- 完整 hash: `33c33a7de9bb15c5708f6ae9d78c5d72d74b0fa4`
- 时间/作者: 2026-02-21 / danielafrimi
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/nemotron_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/model_loader/weight_utils.py`
  - runtime-model: `python/sglang/srt/models/nemotron_h.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/modelopt_quant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `82a0bafc1` - Feat/add fi selective state update kernel call (#18070)

- 完整 hash: `82a0bafc1c3a0680b6389f5ae9c48def7800dcbd`
- 时间/作者: 2026-02-19 / shaharmor98
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/mamba/ops/__init__.py`, `python/sglang/srt/layers/attention/mamba/ops/ssu_dispatch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py`, `test/registered/layers/mamba/conftest.py`, `test/registered/models/test_nvidia_nemotron_3_nano.py`, `test/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/mamba/ops/__init__.py`; `python/sglang/srt/layers/attention/mamba/ops/ssu_dispatch.py`; `python/sglang/srt/managers/scheduler.py`
  - tests: `test/registered/layers/mamba/conftest.py`; `test/registered/models/test_nvidia_nemotron_3_nano.py`; `test/run_suite.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0ff24159a` - Fix modelopt FP8 create weights (#18447)

- 完整 hash: `0ff24159a5bcd0872a65135b0b1eeb3350273949`
- 时间/作者: 2026-02-16 / danielafrimi
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/nemotron_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/nemotron_h.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/modelopt_quant.py`
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

### Commit `44603764d` - fix(config): Support setting Mamba state dtype via config file (#18532)

- 完整 hash: `44603764d65e79d2406eab8d1928dfdec9290138`
- 时间/作者: 2026-02-11 / Zheng Li
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/configs/falcon_h1.py`, `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/configs/lfm2.py`, `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/configs/falcon_h1.py`; `python/sglang/srt/configs/jet_nemotron.py`; `python/sglang/srt/configs/lfm2.py`; `python/sglang/srt/configs/mamba_utils.py`; `python/sglang/srt/configs/nemotron_h.py`; `python/sglang/srt/configs/qwen3_next.py`; `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c6aa1863b` - Add Nemotron 3 Nano tests (#18119)

- 完整 hash: `c6aa1863be84c77bf423ee811e03e9129401c539`
- 时间/作者: 2026-02-06 / shaharmor98
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/pyproject.toml`, `python/sglang/test/kits/lm_eval_kit.py`, `test/lm_eval_configs/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16.yaml`, `test/lm_eval_configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml`, `test/registered/models/test_nvidia_nemotron_3_nano.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/pyproject.toml`
  - tests: `python/sglang/test/kits/lm_eval_kit.py`; `test/lm_eval_configs/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16.yaml`; `test/lm_eval_configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml`; `test/registered/models/test_nvidia_nemotron_3_nano.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `146b5fcc8` - [CI] Reorganize stage-b 1-GPU tests for 5090 compatibility (#16826)

- 完整 hash: `146b5fcc84101123baf743eb9480ad7ce60a0e92`
- 时间/作者: 2026-01-15 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test.yml`, `scripts/ci/slash_command_handler.py`, `test/registered/attention/test_create_kvindices.py`, `test/registered/attention/test_mamba_unittest.py`, `test/registered/attention/test_radix_attention.py`, `test/registered/attention/test_radix_cache_unit.py`, `test/registered/attention/test_swa_unittest.py`, `test/registered/attention/test_torch_native_attention_backend.py` 等 136 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/slash_command_handler.py`
  - tests: `test/registered/attention/test_create_kvindices.py`; `test/registered/attention/test_mamba_unittest.py`; `test/registered/attention/test_radix_attention.py`; `test/registered/attention/test_radix_cache_unit.py`; `test/registered/attention/test_swa_unittest.py`; `test/registered/attention/test_torch_native_attention_backend.py`; `test/registered/attention/test_triton_attention_backend.py`; `test/registered/attention/test_triton_attention_kernels.py` 等 134 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `72bacc88c` - [NemotronH] Use ReplicatedLinear for fc1_latent_proj (#16569)

- 完整 hash: `72bacc88c8a08c4a028ef452add7ccf550ae052e`
- 时间/作者: 2026-01-14 / roikoren755
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/nemotron_h.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/nemotron_h.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `ba625c2d9` - Feat/support nemotron h mtp (#17013)

- 完整 hash: `ba625c2d908ab10427bb9b4d459ad8902d127007`
- 时间/作者: 2026-01-14 / shaharmor98
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/nemotron_h.py`; `python/sglang/srt/models/nemotron_h_mtp.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5dcff9479` - [nemetron/mtp] fix nemotron mtp (#16275)

- 完整 hash: `5dcff94791749efb74d13fb09c99c45c02dbab00`
- 时间/作者: 2026-01-09 / Hanming Lu
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/attention/mamba/ops/mamba_ssm.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/mamba/mamba.py`; `python/sglang/srt/layers/attention/mamba/ops/mamba_ssm.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8726d30cb` - [smg] Add Nemotron Nano V3 reasoning parser support (#16763)

- 完整 hash: `8726d30cb2273bc4eaffd95317291e0f81e35b3b`
- 时间/作者: 2026-01-08 / Simo Lin
- 自动分类: 模型支持/运行时入口
- 主要文件: `sgl-model-gateway/src/reasoning_parser/factory.rs`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `sgl-model-gateway/src/reasoning_parser/factory.rs`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `63cc97f4e` - ci: migrate 2-GPU tests to test/registered/ (#16529)

- 完整 hash: `63cc97f4ef7a4641185a7e3655c75a5d039988c2`
- 时间/作者: 2026-01-07 / Alison Shao
- 自动分类: 调度/缓存/PD
- 主要文件: `.github/workflows/pr-test.yml`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/model_loader/weight_utils.py`, `scripts/ci/slash_command_handler.py`, `test/registered/disaggregation/test_disaggregation_basic.py`, `test/registered/distributed/test_data_parallelism.py`, `test/registered/distributed/test_dp_attention.py`, `test/registered/distributed/test_load_weights_from_remote_instance.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - other: `python/sglang/srt/model_loader/weight_utils.py`; `scripts/ci/slash_command_handler.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`
  - tests: `test/registered/disaggregation/test_disaggregation_basic.py`; `test/registered/distributed/test_data_parallelism.py`; `test/registered/distributed/test_dp_attention.py`; `test/registered/distributed/test_load_weights_from_remote_instance.py`; `test/registered/hicache/test_hicache_storage_3fs_backend.py`; `test/registered/hicache/test_hicache_storage_file_backend.py`; `test/registered/hicache/test_hicache_storage_mooncake_backend.py`; `test/registered/models/test_kimi_linear_models.py` 等 10 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bebd625ba` - EVS Framework: Support NemotronH_Nano_VL_V2 (#14051)

- 完整 hash: `bebd625ba145a1070d2636d3f56a86b195254df2`
- 时间/作者: 2026-01-05 / Netanel Haber
- 自动分类: 调度/缓存/PD
- 主要文件: `docs/supported_models/multimodal_language_models.md`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/mem_cache/multimodal_cache.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/evs/README.md`, `python/sglang/srt/multimodal/evs/__init__.py`, `python/sglang/srt/multimodal/evs/evs_core.py` 等 14 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/supported_models/multimodal_language_models.md`
  - other: `python/sglang/srt/managers/mm_utils.py`; `python/sglang/srt/multimodal/evs/README.md`; `python/sglang/srt/multimodal/evs/__init__.py`; `python/sglang/srt/multimodal/evs/evs_core.py`; `python/sglang/srt/multimodal/evs/evs_module.py`; `python/sglang/srt/multimodal/evs/evs_processor.py`; `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`
  - runtime-model: `python/sglang/srt/disaggregation/encode_server.py`; `python/sglang/srt/models/nano_nemotron_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/multimodal_cache.py`
  - tests: `python/sglang/test/test_utils.py`; `test/srt/run_suite.py`; `test/srt/test_evs.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f8411ded6` - ci: migrate 1-GPU model tests to test/registered/models/ (#16414)

- 完整 hash: `f8411ded6e28c9115cf03ee9b3ad926f3daa867e`
- 时间/作者: 2026-01-04 / Alison Shao
- 自动分类: 模型支持/运行时入口
- 主要文件: `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test.yml`, `docker/xeon.Dockerfile`, `docker/xpu.Dockerfile`, `scripts/ci/slash_command_handler.py`, `test/registered/models/test_compressed_tensors_models.py`, `test/registered/models/test_cross_encoder_models.py`, `test/registered/models/test_embedding_models.py` 等 17 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test-amd.yml`; `.github/workflows/pr-test.yml`
  - other: `docker/xeon.Dockerfile`; `docker/xpu.Dockerfile`; `scripts/ci/slash_command_handler.py`
  - tests: `test/registered/models/test_compressed_tensors_models.py`; `test/registered/models/test_cross_encoder_models.py`; `test/registered/models/test_embedding_models.py`; `test/registered/models/test_encoder_embedding_models.py`; `test/registered/models/test_generation_models.py`; `test/registered/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/registered/models/test_qwen_models.py`; `test/registered/models/test_reward_models.py` 等 12 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `b02133233` - [NemotronH] Add latent MoE support (#16227)

- 完整 hash: `b0213323397cc555ce563c5dce845b246dac73d5`
- 时间/作者: 2026-01-02 / roikoren755
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1344,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1344,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=2688,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=2688,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=1344,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=1344,device_name=NVIDIA_H100_80GB_HBM3.json` 等 23 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`
  - runtime-model: `python/sglang/srt/configs/nemotron_h.py`; `python/sglang/srt/models/nemotron_h.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1344,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1344,device_name=NVIDIA_H100_80GB_HBM3.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=2688,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=2688,device_name=NVIDIA_H100_80GB_HBM3.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=1344,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=1344,device_name=NVIDIA_H100_80GB_HBM3.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=2688,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=256,N=2688,device_name=NVIDIA_H100_80GB_HBM3.json` 等 20 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `417e75a60` - fix: use 2-gpu-runner for pp 2 NemotronH ut (#16239)

- 完整 hash: `417e75a60f0936d0a91e06ab45ea448795cd0bcd`
- 时间/作者: 2025-12-31 / Yineng Zhang
- 自动分类: 缺陷修复
- 主要文件: `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `47a660d5b` - [NemotronH] PP support (#16172)

- 完整 hash: `47a660d5b925e3b8a3083e4f3b81b4c97b2c4101`
- 时间/作者: 2025-12-31 / roikoren755
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/nemotron_h.py`, `test/srt/models/test_nvidia_nemotron_nano_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/nemotron_h.py`
  - tests: `test/srt/models/test_nvidia_nemotron_nano_v2.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5969be2f0` - Apply fixture-kit mode to MMMUVLMMixin (#15615)

- 完整 hash: `5969be2f06c9642c6c8583d48cbd4f363a594824`
- 时间/作者: 2025-12-28 / lif
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/environ.py`, `python/sglang/test/kits/mmmu_vlm_kit.py`, `python/sglang/test/server_fixtures/mmmu_fixture.py`, `test/srt/models/test_ministral3_models.py`, `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`, `test/srt/models/test_vlm_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/environ.py`
  - tests: `python/sglang/test/kits/mmmu_vlm_kit.py`; `python/sglang/test/server_fixtures/mmmu_fixture.py`; `test/srt/models/test_ministral3_models.py`; `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/srt/models/test_vlm_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `183b65190` - Clean up logging (#15919)

- 完整 hash: `183b65190a8525afda50300b837cada7da756556`
- 时间/作者: 2025-12-27 / Lianmin Zheng
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/hf_transformers_utils.py`, `python/sglang/test/test_utils.py`, `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py` 等 9 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/tokenizer_manager.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
  - tests: `python/sglang/test/test_utils.py`; `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/srt/test_vision_chunked_prefill.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `de03b0cd3` - [Nemotron 3 Nano] Add triton MoE configs (#15815)

- 完整 hash: `de03b0cd305bc5c2918dcfb8131606f4762e39e9`
- 时间/作者: 2025-12-25 / roikoren755
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1856,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1856,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=232,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=232,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=464,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=464,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=928,device_name=NVIDIA_B200.json`, `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=928,device_name=NVIDIA_H100_80GB_HBM3.json` 等 20 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1856,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=1856,device_name=NVIDIA_H100_80GB_HBM3.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=232,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=232,device_name=NVIDIA_H100_80GB_HBM3.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=464,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=464,device_name=NVIDIA_H100_80GB_HBM3.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=928,device_name=NVIDIA_B200.json`; `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=128,N=928,device_name=NVIDIA_H100_80GB_HBM3.json` 等 20 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `bd572360f` - Tiny apply gsm8k mixin to ngram test (#15606)

- 完整 hash: `bd572360f315095e69fbdce52b3029e26b8de3b2`
- 时间/作者: 2025-12-24 / Liangsheng Yin
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/spec/test_ngram_speculative_decoding.py`, `test/srt/models/test_ministral3_models.py`, `test/srt/models/test_nvidia_nemotron_nano_v2.py`, `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`, `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/spec/test_ngram_speculative_decoding.py`; `test/srt/models/test_ministral3_models.py`; `test/srt/models/test_nvidia_nemotron_nano_v2.py`; `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `beae3f961` - Adapt fixture-kit to gsm8k mixin (#15599)

- 完整 hash: `beae3f961cd517a03ca92ccbca1a030d4f549026`
- 时间/作者: 2025-12-22 / Liangsheng Yin
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/test/gsm8k_mixin.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `python/sglang/test/kits/mmmu_vlm_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `test/srt/models/test_ministral3_models.py`, `test/srt/models/test_nvidia_nemotron_nano_v2.py`, `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`, `test/srt/models/test_vlm_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/gsm8k_mixin.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `python/sglang/test/kits/mmmu_vlm_kit.py`; `python/sglang/test/server_fixtures/default_fixture.py`; `test/srt/models/test_ministral3_models.py`; `test/srt/models/test_nvidia_nemotron_nano_v2.py`; `test/srt/models/test_nvidia_nemotron_nano_v2_vl.py`; `test/srt/models/test_vlm_models.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。
