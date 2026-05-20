# sglang Qwen3 Next 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/configs/qwen3_next.py` | `44603764d`, `336dc4579` |
| `python/sglang/srt/models/qwen3_next.py` | `7738d2be5`, `0906e45ce`, `5bdc07d97`, `d9794ef9f`, `cabe171b6`, `c64274c74`, `a2ea5941d`, `d2885a909`, `b3202fe6d`, `b2c46fc60`, `5995bfec6`, `07a24f1a3`, ... (24 total) |
| `python/sglang/srt/models/qwen3_next_mtp.py` | `cabe171b6`, `07a24f1a3` |
| `test/registered/4-gpu-models/test_qwen3_next_models.py` | `fb90c9d29`, `067353f67`, `a0bae4c34` |
| `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py` | `fb90c9d29`, `067353f67`, `9457c049e`, `e4b708d3e`, `a0bae4c34` |
| `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_next.py` | `895e56097` |
| `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_next.py` | `895e56097` |
| `test/registered/core/test_qwen3_next_deterministic.py` | `989d4b301` |
| `test/registered/models/test_qwen3_next_models_fp4.py` | `fb90c9d29`, `067353f67`, `a2ea5941d` |
| `test/registered/models/test_qwen3_next_models_pcg.py` | `fb90c9d29`, `067353f67`, `c64274c74`, `8be18c655`, `a0bae4c34` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 42
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-03-26 | `7738d2be5` | 缺陷修复 | Revert "bugfix for weight loading for qwen3-next" (#21496) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-26 | `fb90c9d29` | 性能/后端优化 | [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047) | `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py` |
| 2026-03-26 | `0906e45ce` | 缺陷修复 | bugfix for weight loading for qwen3-next (#21313) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-23 | `5bdc07d97` | 性能/后端优化 | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019) | `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-20 | `d9794ef9f` | 性能/后端优化 | [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj (#19321) | `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-03-16 | `895e56097` | 调度/缓存/PD | Add NPU basic function testcases (#19382) | `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py` |
| 2026-03-15 | `574dbe23b` | 性能/后端优化 | Add piecewise cuda graph for Qwen3-Next FP8 flashinfer_trtllm moe backend (#18184) | `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` |
| 2026-03-12 | `067353f67` | 缺陷修复 | [Test] Refactor KL divergence and prefix cache branching to kits (#19715) | `python/sglang/test/kits/kl_divergence_kit.py`, `python/sglang/test/kits/prefix_cache_branching_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py` |
| 2026-03-09 | `cabe171b6` | 性能/后端优化 | Fix qwen3.5 mtp eplb related issues (#19767) | `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py` |
| 2026-03-06 | `f7de9375a` | 性能/后端优化 | [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775) | `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` |
| 2026-03-04 | `9457c049e` | 调度/缓存/PD | [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-03-02 | `c64274c74` | 性能/后端优化 | Piecewise Cuda Graph set default (#16331) | `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-02-28 | `a2ea5941d` | 性能/后端优化 | [feat] Support nvfp4 quantized model of Qwen3-Next (#17627) | `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_fp4.py` |
| 2026-02-27 | `d2885a909` | 性能/后端优化 | [Qwen3-Next] Support gdn fused_rms_norm_gated (#19434) | `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-02-27 | `4f0f6cd9d` | 性能/后端优化 | Add torch.compile support for qwen3-next on CPU (#12444) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-02-27 | `e4b708d3e` | 调度/缓存/PD | [Spec V2] Support specV2 for mamba hybrid attention (#18808) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py` |
| 2026-02-25 | `b3202fe6d` | 性能/后端优化 | [PCG] fix piecewise cuda graph for Qwen3.5 (#19220) | `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-26 | `b2c46fc60` | 性能/后端优化 | [AMD] Support Qwen3-Coder-Next on AMD platform (#18355) | `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-21 | `5995bfec6` | 性能/后端优化 | [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill (#18917) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-18 | `e2fccb2ee` | 缺陷修复 | Fix flaky Qwen3-Next KL divergence tests by reverting mamba slot release (#18910) | `python/sglang/srt/managers/scheduler.py` |
| 2026-02-16 | `07a24f1a3` | 性能/后端优化 | update pre-commit config (#18860) | `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `3rdparty/amd/tuning/benchmark_moe_rocm.py` |
| 2026-02-13 | `8be18c655` | 性能/后端优化 | [Perf] refactor piecewise cuda graph support of Qwen3-Next (#17613) | `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/model_executor/model_runner.py` |
| 2026-02-11 | `44603764d` | 缺陷修复 | fix(config): Support setting Mamba state dtype via config file (#18532) | `python/sglang/srt/configs/falcon_h1.py`, `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/configs/lfm2.py` |
| 2026-02-10 | `27c447653` | 性能/后端优化 | model: support Qwen3.5 (#18489) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py` |
| 2026-02-08 | `bf89cc380` | 性能/后端优化 | [ModelOPT] Support Qwen 3 Next Coder NVFP4 (#18224) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-02-01 | `3ca29dffc` | 模型支持/运行时入口 | support qwen3-next eagle3 (#14607) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-31 | `a0bae4c34` | 性能/后端优化 | Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299) | `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py` |
| 2026-01-31 | `81449b4be` | 性能/后端优化 | Optimize GDN decode for Qwen3 Next (#17094) | `python/sglang/srt/layers/attention/fla/fused_recurrent.py` |
| 2026-01-30 | `336dc4579` | 性能/后端优化 | [CPU] Optimize Qwen3-next model on CPU (#12525) | `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/layers/amx_utils.py` |
| 2026-01-27 | `d90c0837e` | 模型支持/运行时入口 | [hybrid-model] clean up and consolidate redundant fields in RadixLinearAttention (#17660) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py` |
| 2026-01-25 | `9bd92ba0f` | 调度/缓存/PD | Support PD disaggregation with different TP/DP size for Qwen3-Next (#16056) | `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-01-24 | `fb683be6e` | 性能/后端优化 | Use attn tp group in embedding for more models (#17570) | `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py` |
| 2026-01-22 | `419bbcee1` | 模型支持/运行时入口 | refactor Qwen3-Next with a new RadixLinearAttention (#17373) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-16 | `6f10e17b4` | 缺陷修复 | [bugfix] fix qwen3-next alt_stream none issue (#17016) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-13 | `c5e363e8e` | 模型支持/运行时入口 | test: split Qwen3 Next tests and disable PCG tests due to intermittent failures (#16989) | `test/srt/models/test_qwen3_next_models.py`, `test/srt/models/test_qwen3_next_models_mtp.py`, `test/srt/models/test_qwen3_next_models_pcg.py` |
| 2026-01-10 | `206db66f5` | 模型支持/运行时入口 | tiny refactor pcg split op registration (#16863) | `python/sglang/srt/compilation/compilation_config.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/radix_attention.py` |
| 2026-01-10 | `d1ec93e3a` | 性能/后端优化 | Optimize layernorm_gated for Qwen3-Next (#16397) | `benchmark/fla/benchmark_layernorm_gated.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/utils/common.py` |
| 2026-01-08 | `41609b52f` | 缺陷修复 | support page size large than 64 for mamba radix cache with fix (#16768) | `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/mamba_radix_cache.py` |
| 2026-01-03 | `6bc5a52fd` | 模型支持/运行时入口 | [NPU] Adapt qwen3-next W8A8 on NPU (#16164) | `python/sglang/srt/models/qwen3_next.py` |
| 2026-01-01 | `f6f7af406` | 性能/后端优化 | [Refactor] Clean up custom op (#15995) | `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py` |
| 2025-12-26 | `ef92b4eb8` | 缺陷修复 | [BUGFIX] fix edge case for qwen3-next (#14209) | `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2025-12-22 | `989d4b301` | 性能/后端优化 | [CI] Migrate nightly tests to test/registered/ (#15582) | `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py` |

## 逐 Commit 审计卡

### Commit `7738d2be5` - Revert "bugfix for weight loading for qwen3-next" (#21496)

- 完整 hash: `7738d2be519eff05e35727fc19b6662c8913eaf3`
- 时间/作者: 2026-03-26 / Baizhou Zhang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `fb90c9d29` - [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047)

- 完整 hash: `fb90c9d298eeeb15fde5de1c7676cfc3d9a4b6ee`
- 时间/作者: 2026-03-26 / Liangsheng Yin
- 自动分类: 性能/后端优化
- 主要文件: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/test/kits/eval_accuracy_kit.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_mimo_models.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `0906e45ce` - bugfix for weight loading for qwen3-next (#21313)

- 完整 hash: `0906e45cec97abf3aa8ee9cf8962f6a5d36ed4f1`
- 时间/作者: 2026-03-26 / McZyWu
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `5bdc07d97` - [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019)

- 完整 hash: `5bdc07d974f6cf236fa765a685453ea5e587a838`
- 时间/作者: 2026-03-23 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d9794ef9f` - [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj (#19321)

- 完整 hash: `d9794ef9f7602e3a61ee6b337eda3d364aa3ea1d`
- 时间/作者: 2026-03-20 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
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

### Commit `574dbe23b` - Add piecewise cuda graph for Qwen3-Next FP8 flashinfer_trtllm moe backend (#18184)

- 完整 hash: `574dbe23b25bb823601a55f76dd913fd3fbd9819`
- 时间/作者: 2026-03-15 / Xiaowei Wang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `067353f67` - [Test] Refactor KL divergence and prefix cache branching to kits (#19715)

- 完整 hash: `067353f67b56ea6143d9cd77b87b32edde74b6ac`
- 时间/作者: 2026-03-12 / roikoren755
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/test/kits/kl_divergence_kit.py`, `python/sglang/test/kits/prefix_cache_branching_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/models/test_qwen3_next_models_fp4.py`, `test/registered/models/test_qwen3_next_models_pcg.py`, `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `python/sglang/test/kits/kl_divergence_kit.py`; `python/sglang/test/kits/prefix_cache_branching_kit.py`; `python/sglang/test/server_fixtures/default_fixture.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/models/test_qwen3_next_models_fp4.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `cabe171b6` - Fix qwen3.5 mtp eplb related issues (#19767)

- 完整 hash: `cabe171b6ce3b0d4fb25ff9c88d5743430efaca6`
- 时间/作者: 2026-03-09 / luoyuyan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_next_mtp.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `f7de9375a` - [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775)

- 完整 hash: `f7de9375ace71f46882d095bb3fc23f706bad660`
- 时间/作者: 2026-03-06 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`; `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
  - tests: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9457c049e` - [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391)

- 完整 hash: `9457c049e19e1cfa75833ef4351ac5aa26941c2c`
- 时间/作者: 2026-03-04 / hlu1
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen35_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `c64274c74` - Piecewise Cuda Graph set default (#16331)

- 完整 hash: `c64274c746f210497c45bd1600d2046faf7f4b10`
- 时间/作者: 2026-03-02 / Yuwei An
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/awq.py` 等 34 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/compilation/compile.py`; `python/sglang/srt/compilation/piecewise_context_manager.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/minicpm3.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/flashinfer_backend.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/qwen2_moe.py`
  - tests: `test/manual/nightly/test_vlms_piecewise_cuda_graph.py`; `test/manual/nightly/test_vlms_vit_cuda_graph.py`; `test/manual/piecewise_cudagraph/test_disaggregation_piecewise_cuda_graph.py`; `test/registered/mla/test_mla_deepseek_v3.py`; `test/registered/models/test_generation_models.py`; `test/registered/models/test_kimi_linear_models_pcg.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/piecewise_cuda_graph/test_piecewise_cuda_graph_2_gpu.py` 等 13 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `a2ea5941d` - [feat] Support nvfp4 quantized model of Qwen3-Next (#17627)

- 完整 hash: `a2ea5941d562faa5a9a20083ffc81dd0d9dd2d6a`
- 时间/作者: 2026-02-28 / Zheng Duan
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_fp4.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - tests: `test/registered/models/test_qwen3_next_models_fp4.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `d2885a909` - [Qwen3-Next] Support gdn fused_rms_norm_gated (#19434)

- 完整 hash: `d2885a9094c3847769923322e51a85841a552662`
- 时间/作者: 2026-02-27 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`; `python/sglang/srt/layers/attention/fla/kda.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `4f0f6cd9d` - Add torch.compile support for qwen3-next on CPU (#12444)

- 完整 hash: `4f0f6cd9d0259fb5081ecc565dad2bb47643e8fa`
- 时间/作者: 2026-02-27 / Cao E
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/cpu_graph_runner.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/intel_amx_backend.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `e4b708d3e` - [Spec V2] Support specV2 for mamba hybrid attention (#18808)

- 完整 hash: `e4b708d3e9dd90613a9707c5c3cd4e98cd8c4cd8`
- 时间/作者: 2026-02-27 / zhangheng
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/managers/scheduler_output_processor_mixin.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `b2c46fc60` - [AMD] Support Qwen3-Coder-Next on AMD platform (#18355)

- 完整 hash: `b2c46fc60b14904857a37a02ceb633c898b23a63`
- 时间/作者: 2026-02-26 / jacky.cheng
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `5995bfec6` - [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill (#18917)

- 完整 hash: `5995bfec6368faa48fd8ad159bf9805c15ebc217`
- 时间/作者: 2026-02-21 / YAMY
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `e2fccb2ee` - Fix flaky Qwen3-Next KL divergence tests by reverting mamba slot release (#18910)

- 完整 hash: `e2fccb2ee0a0211b75961e40009fe02133fa9983`
- 时间/作者: 2026-02-18 / Alison Shao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
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

### Commit `8be18c655` - [Perf] refactor piecewise cuda graph support of Qwen3-Next (#17613)

- 完整 hash: `8be18c655d0ff1c2e673395102c97c9d5cbd7d1c`
- 时间/作者: 2026-02-13 / Minglei Zhu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_pcg.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/radix_linear_attention.py`
  - tests: `test/registered/models/test_qwen3_next_models_pcg.py`
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

### Commit `bf89cc380` - [ModelOPT] Support Qwen 3 Next Coder NVFP4 (#18224)

- 完整 hash: `bf89cc3803873a00879c516e247df611ad3247a7`
- 时间/作者: 2026-02-08 / Yi Zhong
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `3ca29dffc` - support qwen3-next eagle3 (#14607)

- 完整 hash: `3ca29dffc72ac8a1000d3dad988fd96ab3339b9d`
- 时间/作者: 2026-02-01 / lukec
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

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

### Commit `81449b4be` - Optimize GDN decode for Qwen3 Next (#17094)

- 完整 hash: `81449b4beebf761eab1ad67ad19e3cab4c0109d4`
- 时间/作者: 2026-01-31 / Sam (Kesen Li)
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `336dc4579` - [CPU] Optimize Qwen3-next model on CPU (#12525)

- 完整 hash: `336dc4579e944728d3efe902a49ad75f195da5e4`
- 时间/作者: 2026-01-30 / jianan-gu
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/mem_cache/memory_pool.py` 等 13 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/amx_utils.py`; `python/sglang/srt/model_loader/weight_utils.py`
  - runtime-model: `python/sglang/srt/configs/qwen3_next.py`; `python/sglang/srt/configs/update_config.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/intel_amx_backend.py`; `python/sglang/srt/layers/attention/mamba/mamba.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `sgl-kernel/csrc/cpu/topk.cpp`; `sgl-kernel/python/sgl_kernel/__init__.py`; `sgl-kernel/python/sgl_kernel/mamba.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d90c0837e` - [hybrid-model] clean up and consolidate redundant fields in RadixLinearAttention (#17660)

- 完整 hash: `d90c0837e5b812864a7570234b1a498740a01e85`
- 时间/作者: 2026-01-27 / Minglei Zhu
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/radix_linear_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `9bd92ba0f` - Support PD disaggregation with different TP/DP size for Qwen3-Next (#16056)

- 完整 hash: `9bd92ba0f6e8040c2f9fb211a50c5094d4cb5d53`
- 时间/作者: 2026-01-25 / xjx471258437
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/srt/test_disaggregation_hybrid_attention.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/srt/test_disaggregation_hybrid_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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

### Commit `419bbcee1` - refactor Qwen3-Next with a new RadixLinearAttention (#17373)

- 完整 hash: `419bbcee10a5a2f76b8b2612c7c2fbde3d0be645`
- 时间/作者: 2026-01-22 / Minglei Zhu
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/radix_linear_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6f10e17b4` - [bugfix] fix qwen3-next alt_stream none issue (#17016)

- 完整 hash: `6f10e17b4a68df3cea7d37d30859409f62f720dc`
- 时间/作者: 2026-01-16 / billishyahao
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `c5e363e8e` - test: split Qwen3 Next tests and disable PCG tests due to intermittent failures (#16989)

- 完整 hash: `c5e363e8e0ea7c1fe9873b951f556979fb949196`
- 时间/作者: 2026-01-13 / Alison Shao
- 自动分类: 模型支持/运行时入口
- 主要文件: `test/srt/models/test_qwen3_next_models.py`, `test/srt/models/test_qwen3_next_models_mtp.py`, `test/srt/models/test_qwen3_next_models_pcg.py`, `test/srt/run_suite.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - tests: `test/srt/models/test_qwen3_next_models.py`; `test/srt/models/test_qwen3_next_models_mtp.py`; `test/srt/models/test_qwen3_next_models_pcg.py`; `test/srt/run_suite.py`
- 验证与风险: 提交包含测试相关改动；优先复跑对应测试，并补充目标模型的最小启动或生成 smoke。

### Commit `206db66f5` - tiny refactor pcg split op registration (#16863)

- 完整 hash: `206db66f5c239bc13e6e4cfa7a4ea952612a2e59`
- 时间/作者: 2026-01-10 / Qiaolin Yu
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/compilation/compilation_config.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/compilation/compilation_config.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/radix_attention.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `d1ec93e3a` - Optimize layernorm_gated for Qwen3-Next (#16397)

- 完整 hash: `d1ec93e3acc483d37e33b1378f2b2ff7efbb3cfc`
- 时间/作者: 2026-01-10 / Yuan Luo
- 自动分类: 性能/后端优化
- 主要文件: `benchmark/fla/benchmark_layernorm_gated.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/utils/common.py`, `test/srt/run_suite.py`, `test/srt/test_fla_layernorm_guard.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - docs-bench: `benchmark/fla/benchmark_layernorm_gated.py`
  - other: `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`
  - tests: `test/srt/run_suite.py`; `test/srt/test_fla_layernorm_guard.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `41609b52f` - support page size large than 64 for mamba radix cache with fix (#16768)

- 完整 hash: `41609b52fe78b1d72b6d67caeb5c526bb47ea6f2`
- 时间/作者: 2026-01-08 / Hanming Lu
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/server_args.py`, `test/srt/models/test_qwen3_next_models.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/managers/schedule_batch.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/mem_cache/mamba_radix_cache.py`
  - tests: `test/srt/models/test_qwen3_next_models.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `6bc5a52fd` - [NPU] Adapt qwen3-next W8A8 on NPU (#16164)

- 完整 hash: `6bc5a52fd2d4807dcea21e822345fb5ea3e7bd4e`
- 时间/作者: 2026-01-03 / shengzhaotian
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/models/qwen3_next.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- 验证与风险: 涉及模型运行时入口；风险点是权重加载、并行切分、parser/tokenizer 行为和短文本生成正确性。

### Commit `f6f7af406` - [Refactor] Clean up custom op (#15995)

- 完整 hash: `f6f7af406822669d2ff043fc7aafc4f5dfdb9413`
- 时间/作者: 2026-01-01 / DarkSharpness
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/elementwise.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` 等 23 个文件
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - other: `python/sglang/srt/layers/elementwise.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/utils/common.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/utils.py`
  - runtime-perf: `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/dp_attention.py`; `python/sglang/srt/layers/flashinfer_comm_fusion.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 17 个文件
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `ef92b4eb8` - [BUGFIX] fix edge case for qwen3-next (#14209)

- 完整 hash: `ef92b4eb88905b7b9415548e060870a99d5b6104`
- 时间/作者: 2025-12-26 / Yi Zhang
- 自动分类: 缺陷修复
- 主要文件: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

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
