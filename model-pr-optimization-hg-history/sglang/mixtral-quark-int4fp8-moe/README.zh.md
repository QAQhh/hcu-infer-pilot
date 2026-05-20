# sglang Mixtral Quark INT4/FP8 MoE 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/layers/quantization/quark/__init__.py` | 无直接提交 |
| `python/sglang/srt/layers/quantization/quark/quark.py` | `f0d78f2e2`, `150ed881b`, `0d49b13fd` |
| `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` | `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py` | `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` | `e9d6aefa9`, `5172c3784`, `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` | `61a902ce8`, `048d90e16`, `941945371`, `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py` | `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | `e9d6aefa9`, `150ed881b` |
| `python/sglang/srt/layers/quantization/quark/utils.py` | `8d2892330` |
| `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py` | `e9d6aefa9`, `5af84c8af` |
| `python/sglang/srt/models/mixtral.py` | `d1e95af28` |
| `python/sglang/srt/models/mixtral_quant.py` | `d1e95af28`, `20282f566` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 12
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-30 | `e9d6aefa9` | 性能/后端优化 | sglang dcu 0.5.10rc0 base bash(48739c3a) | `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py` |
| 2026-03-25 | `61a902ce8` | 性能/后端优化 | [AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype. (#21040) | `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/layers/quantization/fp8.py` |
| 2026-03-20 | `048d90e16` | 性能/后端优化 | Revert "[AMD] Add MoE weights and scales padding" (#21067) | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-21 | `941945371` | 性能/后端优化 | [AMD] Add MoE weights and scales padding (#18684) | `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` |
| 2026-03-18 | `d1e95af28` | 性能/后端优化 | Upgrade transformers==5.3.0 (#17784) | `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` |
| 2026-03-02 | `20282f566` | 性能/后端优化 | [fix typo] expert_indicies -> expert_indices (#19627) | `python/sglang/srt/models/mixtral_quant.py` |
| 2026-02-27 | `f0d78f2e2` | 性能/后端优化 | [AMD] Fix weight load shape mismatch for amd dsr1 0528 mxfp4 (#19425) | `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/deepseek_nextn.py` |
| 2026-02-27 | `5172c3784` | 性能/后端优化 | [AMD] Use fused GEMM with FP8 cast for FP8 prefill (#19422) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` |
| 2026-02-18 | `150ed881b` | 性能/后端优化 | [4/N] Quantization Refactor: Quark MoE schemes (#18252) | `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py` |
| 2026-02-11 | `8d2892330` | 性能/后端优化 | chore: fix some typos (#18577) | `python/sglang/srt/layers/attention/double_sparsity_backend.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/int8_kernel.py` |
| 2026-01-21 | `0d49b13fd` | 性能/后端优化 | Fix circular import in quantization modules (#17372) | `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/auto_round.py`, `python/sglang/srt/layers/quantization/petit.py` |
| 2026-01-14 | `5af84c8af` | 性能/后端优化 | [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm (#7392) | `docs/advanced_features/quantization.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/int4fp8_utils.py` |

## 逐 Commit 审计卡

### Commit `e9d6aefa9` - sglang dcu 0.5.10rc0 base bash(48739c3a)

- 完整 hash: `e9d6aefa947699a1edc971ecc2e3fdd2053f525f`
- 时间/作者: 2026-03-30 / lizhigong
- 自动分类: 性能/后端优化
- 主要文件: `README_DCU.md`, `python/sglang/bench_serving.py`, `python/sglang/srt/batch_overlap/single_batch_overlap.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` 等 114 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `README_DCU.md`; `python/sglang/bench_serving.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py` 等 25 个文件
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/server_args.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce_ops.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/dcu_mla_backend.py`; `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py` 等 79 个文件
  - tests: `test/manual/test_two_batch_overlap.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `61a902ce8` - [AMD][MoRI] Auto-select dispatch quantization type from MoE weight dtype. (#21040)

- 完整 hash: `61a902ce88ea278ccc1dad0b5d7437a67724d868`
- 时间/作者: 2026-03-25 / Duyi-Wang
- 自动分类: 性能/后端优化
- 主要文件: `docs/references/environment_variables.md`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/amd/test_moriep_small.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/references/environment_variables.md`
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`
  - tests: `test/registered/amd/test_moriep_small.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `048d90e16` - Revert "[AMD] Add MoE weights and scales padding" (#21067)

- 完整 hash: `048d90e1651a3842253ce5291162a4840e9ee5cc`
- 时间/作者: 2026-03-20 / Alison Shao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/model_executor/model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `941945371` - [AMD] Add MoE weights and scales padding (#18684)

- 完整 hash: `9419453713146b1be0c21e6d328f435f1db95da6`
- 时间/作者: 2026-03-21 / mqhc2020
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/model_executor/model_runner.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`
  - runtime-perf: `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/utils.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`; `python/sglang/srt/layers/quantization/fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`
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

### Commit `20282f566` - [fix typo] expert_indicies -> expert_indices (#19627)

- 完整 hash: `20282f5664cbf762860db79e34b034b211e83cc0`
- 时间/作者: 2026-03-02 / SoluMilken
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/mixtral_quant.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/models/mixtral_quant.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f0d78f2e2` - [AMD] Fix weight load shape mismatch for amd dsr1 0528 mxfp4 (#19425)

- 完整 hash: `f0d78f2e201aa7a2f21d291e20cf0154ee868a21`
- 时间/作者: 2026-02-27 / billishyahao
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/deepseek_nextn.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/deepseek_nextn.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/quark/quark.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5172c3784` - [AMD] Use fused GEMM with FP8 cast for FP8 prefill (#19422)

- 完整 hash: `5172c378456fa9735ba6429a2ca7688d1152d256`
- 时间/作者: 2026-02-27 / Thomas Wang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `150ed881b` - [4/N] Quantization Refactor: Quark MoE schemes (#18252)

- 完整 hash: `150ed881be2cf9a9e64b636226b3c6189d341a7d`
- 时间/作者: 2026-02-18 / Tamir Baydasov
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/quantization/quark/quark.py`; `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_scheme.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`; `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `8d2892330` - chore: fix some typos (#18577)

- 完整 hash: `8d2892330c05e4a0d0ee3085b25c035bfed07dcf`
- 时间/作者: 2026-02-11 / cutetocute
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/double_sparsity_backend.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/int8_kernel.py`, `python/sglang/srt/layers/quantization/quark/utils.py`, `python/sglang/srt/managers/io_struct.py`, `test/registered/rl/test_multi_instance_release_memory_occupation.py`, `test/registered/utils/test_bench_typebaseddispatcher.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/io_struct.py`
  - runtime-perf: `python/sglang/srt/layers/attention/double_sparsity_backend.py`; `python/sglang/srt/layers/quantization/fp8_kernel.py`; `python/sglang/srt/layers/quantization/int8_kernel.py`; `python/sglang/srt/layers/quantization/quark/utils.py`
  - tests: `test/registered/rl/test_multi_instance_release_memory_occupation.py`; `test/registered/utils/test_bench_typebaseddispatcher.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `0d49b13fd` - Fix circular import in quantization modules (#17372)

- 完整 hash: `0d49b13fdd7d96712efee7fbaf246c2e3a965304`
- 时间/作者: 2026-01-21 / Sam Shleifer
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/auto_round.py`, `python/sglang/srt/layers/quantization/petit.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/w4afp8.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/auto_round.py`; `python/sglang/srt/layers/quantization/petit.py`; `python/sglang/srt/layers/quantization/quark/quark.py`; `python/sglang/srt/layers/quantization/w4afp8.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5af84c8af` - [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm (#7392)

- 完整 hash: `5af84c8af554fa0e6fb55890b39b97f155275372`
- 时间/作者: 2026-01-14 / fxmarty-amd
- 自动分类: 性能/后端优化
- 主要文件: `docs/advanced_features/quantization.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/int4fp8_utils.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`, `python/sglang/srt/model_loader/utils.py`, `python/sglang/srt/model_loader/weight_utils.py` 等 12 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `docs/advanced_features/quantization.md`
  - other: `python/sglang/srt/layers/int4fp8_utils.py`; `python/sglang/srt/layers/linear.py`; `python/sglang/srt/model_loader/utils.py`; `python/sglang/srt/model_loader/weight_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/__init__.py`; `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`
  - tests: `test/srt/run_suite.py`; `test/srt/test_int4fp8_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。
