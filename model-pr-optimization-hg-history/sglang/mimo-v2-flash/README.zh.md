# sglang MiMo V2 Flash 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/function_call/mimo_detector.py` | 无直接提交 |
| `python/sglang/srt/models/mimo.py` | 无直接提交 |
| `python/sglang/srt/models/mimo_mtp.py` | 无直接提交 |
| `python/sglang/srt/models/mimo_v2_flash.py` | `1924c63d6`, `d1e95af28`, `cbf150039`, `9227d4f74`, `fb683be6e` |
| `python/sglang/srt/models/mimo_v2_flash_nextn.py` | `d1e95af28`, `980d2936c`, `fb683be6e` |
| `test/registered/8-gpu-models/test_mimo_models.py` | `fb90c9d29`, `ae7c2397b`, `a0bae4c34` |
| `test/registered/ascend/llm_models/test_npu_mimo_7b_rl.py` | `895e56097` |
| `test/registered/ascend/vlm_models/test_npu_mimo_vl_7b_rl.py` | `895e56097` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 20
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-05-14 | `1924c63d6` | 性能/后端优化 | [BUG FIX] fix pp parallel bug for mimo model | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py` |
| 2026-04-14 | `47165f0fc` | 性能/后端优化 | [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash) | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-04-03 | `30f4f1133` | 性能/后端优化 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` |
| 2026-03-26 | `fb90c9d29` | 性能/后端优化 | [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047) | `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-03-12 | `ae7c2397b` | 性能/后端优化 | Fix FA3 swa spec pg_size > 1 (#20369) | `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/8-gpu-models/test_mimo_models.py` |
| 2026-02-03 | `cbf150039` | 性能/后端优化 | [MiMoV2Flash] [feat]: support two batch overlap (#17634) | `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/models/mimo_v2_flash.py` |
| 2026-02-03 | `980d2936c` | 性能/后端优化 | model: support Step-3.5-Flash (#18084) | `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py` |
| 2026-02-03 | `c781db0f6` | 调度/缓存/PD | [NPU] update nightly tests (#17952) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-02-02 | `9227d4f74` | 性能/后端优化 | [Fix] Remove no use code in MiMo-V2-Flash (#18051) | `python/sglang/srt/models/mimo_v2_flash.py` |
| 2026-01-31 | `a0bae4c34` | 性能/后端优化 | Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299) | `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py` |
| 2026-01-24 | `fb683be6e` | 性能/后端优化 | Use attn tp group in embedding for more models (#17570) | `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py` |
| 2026-01-20 | `91a4cd864` | 调度/缓存/PD | Update default attn backend to fa3 for mimo model (#17419) | `python/sglang/srt/utils/common.py` |
| 2026-01-04 | `b328cd20b` | 性能/后端优化 | Skip local attn init metadata for mimo swa model (#16349) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` |
| 2025-12-27 | `faecd37ed` | 性能/后端优化 | Add Mimo-v2-flash model to ci test (#15887) | `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `python/sglang/test/kits/spec_decoding_kit.py`, `test/srt/models/test_mimo_models.py` |
| 2025-12-25 | `bb9e6cdf9` | 性能/后端优化 | [MiMoV2Flash] fix: respect --swa-full-tokens-ratio arg (#15488) | `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py` |
| 2025-12-25 | `cbf9f1349` | 性能/后端优化 | Adjust server args for Mimo-v2-flash model (#15803) | `python/sglang/srt/server_args.py` |
| 2025-12-22 | `989d4b301` | 性能/后端优化 | [CI] Migrate nightly tests to test/registered/ (#15582) | `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py` |
| 2025-12-23 | `3c882db3a` | 性能/后端优化 | Adjust wrong `mtp` meaning introduce by mimo (#15632) | `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/scheduler.py` |

## 逐 Commit 审计卡

### Commit `1924c63d6` - [BUG FIX] fix pp parallel bug for mimo model

- 完整 hash: `1924c63d64f72fbbb4623956150b176dcdcde29c`
- 时间/作者: 2026-05-14 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/models/mimo_v2_flash.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `47165f0fc` - [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash)

- 完整 hash: `47165f0fcf27c6d38edd4d230d750311f98ba387`
- 时间/作者: 2026-04-14 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `30f4f1133` - support mimo-v2-flash-int4 with triton attn

- 完整 hash: `30f4f1133f9a4d57d8cd3b971230048e0cf15b04`
- 时间/作者: 2026-04-03 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `fb90c9d29` - [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047)

- 完整 hash: `fb90c9d298eeeb15fde5de1c7676cfc3d9a4b6ee`
- 时间/作者: 2026-03-26 / Liangsheng Yin
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/test/kits/eval_accuracy_kit.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_mimo_models.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

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

### Commit `ae7c2397b` - Fix FA3 swa spec pg_size > 1 (#20369)

- 完整 hash: `ae7c2397b96b342db1ebc89a21aa5c235fe9c14c`
- 时间/作者: 2026-03-12 / Ke Bao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/8-gpu-models/test_mimo_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
  - tests: `test/registered/8-gpu-models/test_mimo_models.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `cbf150039` - [MiMoV2Flash] [feat]: support two batch overlap (#17634)

- 完整 hash: `cbf15003903761c9b2f652e5185858545944e9c9`
- 时间/作者: 2026-02-03 / TZHelloWorld
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/models/mimo_v2_flash.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/batch_overlap/operations_strategy.py`
  - runtime-perf: `python/sglang/srt/models/mimo_v2_flash.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `980d2936c` - model: support Step-3.5-Flash (#18084)

- 完整 hash: `980d2936cd9a94a6346fb678a8134d5776fdf996`
- 时间/作者: 2026-02-03 / Yuhao Yang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/step3p5.py`, `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_loader/loader.py` 等 15 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/function_call/function_call_parser.py`; `python/sglang/srt/model_loader/loader.py`; `python/sglang/srt/parser/reasoning_parser.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/step3p5.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/step3p5.py`; `python/sglang/srt/models/step3p5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/moe_runner/triton.py`; `python/sglang/srt/models/mimo_v2_flash_nextn.py`
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

### Commit `9227d4f74` - [Fix] Remove no use code in MiMo-V2-Flash (#18051)

- 完整 hash: `9227d4f748834dd3d472f8fb188c131b09a379a1`
- 时间/作者: 2026-02-02 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/mimo_v2_flash.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/mimo_v2_flash.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a0bae4c34` - Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299)

- 完整 hash: `a0bae4c34349d09b3ad71db71d4fc3f4f32f221e`
- 时间/作者: 2026-01-31 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py` 等 39 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v32_basic.py`; `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v3_basic.py`; `test/registered/8-gpu-models/test_deepseek_v3_mtp.py` 等 37 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

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

### Commit `91a4cd864` - Update default attn backend to fa3 for mimo model (#17419)

- 完整 hash: `91a4cd86487b4cfc9718e5dcb1654b5bf3859a74`
- 时间/作者: 2026-01-20 / Ke Bao
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/utils/common.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/utils/common.py`
- 验证与风险: 未看到明确测试面；如借鉴此提交，需要补充最小复现实验和目标模型回归验证。

### Commit `b328cd20b` - Skip local attn init metadata for mimo swa model (#16349)

- 完整 hash: `b328cd20bbe8fcdb1d84e38c39e50852122e15b4`
- 时间/作者: 2026-01-04 / Ke Bao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/configs/model_config.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `faecd37ed` - Add Mimo-v2-flash model to ci test (#15887)

- 完整 hash: `faecd37ed420bbdf4f55464fd303d54293d1bb2d`
- 时间/作者: 2025-12-27 / Ke Bao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `python/sglang/test/kits/spec_decoding_kit.py`, `test/srt/models/test_mimo_models.py`, `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `python/sglang/test/kits/spec_decoding_kit.py`; `test/srt/models/test_mimo_models.py`; `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `bb9e6cdf9` - [MiMoV2Flash] fix: respect --swa-full-tokens-ratio arg (#15488)

- 完整 hash: `bb9e6cdf9e3c1868550c57439bd1bd6fdd0da679`
- 时间/作者: 2025-12-25 / Yingchun Lai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `cbf9f1349` - Adjust server args for Mimo-v2-flash model (#15803)

- 完整 hash: `cbf9f1349335334a7f242b7a111c9de4844a7dd0`
- 时间/作者: 2025-12-25 / Ke Bao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `3c882db3a` - Adjust wrong `mtp` meaning introduce by mimo (#15632)

- 完整 hash: `3c882db3adf506b058c10c3c9321723fd4d2b635`
- 时间/作者: 2025-12-23 / Liangsheng Yin
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker.py` 等 10 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`; `python/sglang/srt/speculative/multi_layer_eagle_utils.py`; `python/sglang/srt/speculative/spec_utils.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/managers/tp_worker.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker.py`; `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
