# sglang Qwen3 Next Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
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

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 42
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
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

## Per-Commit Audit Cards

### Commit `7738d2be5` - Revert "bugfix for weight loading for qwen3-next" (#21496)

- Full hash: `7738d2be519eff05e35727fc19b6662c8913eaf3`
- Date/author: 2026-03-26 / Baizhou Zhang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `fb90c9d29` - [Test] Consolidate eval accuracy test mixins into eval_accuracy_kit (#21047)

- Full hash: `fb90c9d298eeeb15fde5de1c7676cfc3d9a4b6ee`
- Date/author: 2026-03-26 / Liangsheng Yin
- Auto category: 性能/后端优化
- Main files: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/gsm8k_accuracy_kit.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py`, `test/registered/backends/test_torch_compile.py`, `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `.claude/skills/write-sglang-test/SKILL.md`; `python/sglang/test/kits/eval_accuracy_kit.py`; `python/sglang/test/kits/gsm8k_accuracy_kit.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_mimo_models.py`; `test/registered/backends/test_torch_compile.py`; `test/registered/core/test_cpp_radix_cache.py` 等 25 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `0906e45ce` - bugfix for weight loading for qwen3-next (#21313)

- Full hash: `0906e45cec97abf3aa8ee9cf8962f6a5d36ed4f1`
- Date/author: 2026-03-26 / McZyWu
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `5bdc07d97` - [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel (#21019)

- Full hash: `5bdc07d974f6cf236fa765a685453ea5e587a838`
- Date/author: 2026-03-23 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/jit_kernel/triton/gdn_fused_proj.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d9794ef9f` - [Qwen3-Next] Fuse Qwen3-Next GDN's qkvz_proj and ba_proj (#19321)

- Full hash: `d9794ef9f7602e3a61ee6b337eda3d364aa3ea1d`
- Date/author: 2026-03-20 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/linear.py`
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `895e56097` - Add NPU basic function testcases (#19382)

- Full hash: `895e56097cc25f762373f462fd027bc39163eb0c`
- Date/author: 2026-03-16 / Sugar920
- Auto category: 调度/缓存/PD
- Main files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`, `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py` 等 87 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-npu.yml`
  - tests: `python/sglang/test/ascend/disaggregation_utils.py`; `python/sglang/test/ascend/test_ascend_utils.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py`; `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`; `test/registered/ascend/basic_function/HiCache/test_npu_radix_cache.py`; `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py` 等 86 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `574dbe23b` - Add piecewise cuda graph for Qwen3-Next FP8 flashinfer_trtllm moe backend (#18184)

- Full hash: `574dbe23b25bb823601a55f76dd913fd3fbd9819`
- Date/author: 2026-03-15 / Xiaowei Wang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`; `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `067353f67` - [Test] Refactor KL divergence and prefix cache branching to kits (#19715)

- Full hash: `067353f67b56ea6143d9cd77b87b32edde74b6ac`
- Date/author: 2026-03-12 / roikoren755
- Auto category: 缺陷修复
- Main files: `python/sglang/test/kits/kl_divergence_kit.py`, `python/sglang/test/kits/prefix_cache_branching_kit.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/models/test_qwen3_next_models_fp4.py`, `test/registered/models/test_qwen3_next_models_pcg.py`, `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `python/sglang/test/kits/kl_divergence_kit.py`; `python/sglang/test/kits/prefix_cache_branching_kit.py`; `python/sglang/test/server_fixtures/default_fixture.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/models/test_qwen3_next_models_fp4.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/radix_cache/test_swa_radix_cache_kl.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `cabe171b6` - Fix qwen3.5 mtp eplb related issues (#19767)

- Full hash: `cabe171b6ce3b0d4fb25ff9c88d5743430efaca6`
- Date/author: 2026-03-09 / luoyuyan
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_next_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_next_mtp.py`
  - runtime-perf: `python/sglang/srt/models/qwen2_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f7de9375a` - [GDN][Qwen3-Next][Qwen3.5] Fuse fused_gdn_gating and fused_recurrent_gated_delta_rule_update in verify_target (#19775)

- Full hash: `f7de9375ace71f46882d095bb3fc23f706bad660`
- Date/author: 2026-03-06 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`, `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`; `python/sglang/srt/layers/attention/linear/gdn_backend.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`; `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`; `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`
  - tests: `python/sglang/jit_kernel/tests/test_fused_verify_triton_gdn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9457c049e` - [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 (#19391)

- Full hash: `9457c049e19e1cfa75833ef4351ac5aa26941c2c`
- Date/author: 2026-03-04 / hlu1
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen35_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/server_args.py`; `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/registered/4-gpu-models/test_qwen35_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c64274c74` - Piecewise Cuda Graph set default (#16331)

- Full hash: `c64274c746f210497c45bd1600d2046faf7f4b10`
- Date/author: 2026-03-02 / Yuwei An
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/awq.py` 等 34 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/compilation/compile.py`; `python/sglang/srt/compilation/piecewise_context_manager.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/minicpm3.py`; `python/sglang/srt/models/minimax_m2.py`; `python/sglang/srt/models/qwen3.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/flashinfer_backend.py`; `python/sglang/srt/layers/moe/topk.py`; `python/sglang/srt/layers/quantization/awq.py`; `python/sglang/srt/layers/quantization/fp8_utils.py`; `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`; `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`; `python/sglang/srt/models/qwen2_moe.py`
  - tests: `test/manual/nightly/test_vlms_piecewise_cuda_graph.py`; `test/manual/nightly/test_vlms_vit_cuda_graph.py`; `test/manual/piecewise_cudagraph/test_disaggregation_piecewise_cuda_graph.py`; `test/registered/mla/test_mla_deepseek_v3.py`; `test/registered/models/test_generation_models.py`; `test/registered/models/test_kimi_linear_models_pcg.py`; `test/registered/models/test_qwen3_next_models_pcg.py`; `test/registered/piecewise_cuda_graph/test_piecewise_cuda_graph_2_gpu.py` 等 13 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a2ea5941d` - [feat] Support nvfp4 quantized model of Qwen3-Next (#17627)

- Full hash: `a2ea5941d562faa5a9a20083ffc81dd0d9dd2d6a`
- Date/author: 2026-02-28 / Zheng Duan
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_fp4.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - tests: `test/registered/models/test_qwen3_next_models_fp4.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `d2885a909` - [Qwen3-Next] Support gdn fused_rms_norm_gated (#19434)

- Full hash: `d2885a9094c3847769923322e51a85841a552662`
- Date/author: 2026-02-27 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`, `python/sglang/srt/layers/attention/fla/kda.py`, `python/sglang/srt/models/kimi_linear.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_norm_gate.py`; `python/sglang/srt/layers/attention/fla/kda.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4f0f6cd9d` - Add torch.compile support for qwen3-next on CPU (#12444)

- Full hash: `4f0f6cd9d0259fb5081ecc565dad2bb47643e8fa`
- Date/author: 2026-02-27 / Cao E
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/cpu_graph_runner.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/intel_amx_backend.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e4b708d3e` - [Spec V2] Support specV2 for mamba hybrid attention (#18808)

- Full hash: `e4b708d3e9dd90613a9707c5c3cd4e98cd8c4cd8`
- Date/author: 2026-02-27 / zhangheng
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/speculative/eagle_info_v2.py`
  - runtime-model: `python/sglang/srt/speculative/eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/managers/scheduler_output_processor_mixin.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b3202fe6d` - [PCG] fix piecewise cuda graph for Qwen3.5 (#19220)

- Full hash: `b3202fe6d072c6afdfd8a567977d84de17c1d50d`
- Date/author: 2026-02-25 / Minglei Zhu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`, `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/quantization/fp8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b2c46fc60` - [AMD] Support Qwen3-Coder-Next on AMD platform (#18355)

- Full hash: `b2c46fc60b14904857a37a02ceb633c898b23a63`
- Date/author: 2026-02-26 / jacky.cheng
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/aiter_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `5995bfec6` - [Qwen3-Next] Enable fused_qkvzba_split_reshape_cat also for prefill (#18917)

- Full hash: `5995bfec6368faa48fd8ad159bf9805c15ebc217`
- Date/author: 2026-02-21 / YAMY
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `e2fccb2ee` - Fix flaky Qwen3-Next KL divergence tests by reverting mamba slot release (#18910)

- Full hash: `e2fccb2ee0a0211b75961e40009fe02133fa9983`
- Date/author: 2026-02-18 / Alison Shao
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/scheduler.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `8be18c655` - [Perf] refactor piecewise cuda graph support of Qwen3-Next (#17613)

- Full hash: `8be18c655d0ff1c2e673395102c97c9d5cbd7d1c`
- Date/author: 2026-02-13 / Minglei Zhu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/qwen3_next.py`, `test/registered/models/test_qwen3_next_models_pcg.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/radix_linear_attention.py`
  - tests: `test/registered/models/test_qwen3_next_models_pcg.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `44603764d` - fix(config): Support setting Mamba state dtype via config file (#18532)

- Full hash: `44603764d65e79d2406eab8d1928dfdec9290138`
- Date/author: 2026-02-11 / Zheng Li
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/configs/falcon_h1.py`, `python/sglang/srt/configs/jet_nemotron.py`, `python/sglang/srt/configs/lfm2.py`, `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/configs/falcon_h1.py`; `python/sglang/srt/configs/jet_nemotron.py`; `python/sglang/srt/configs/lfm2.py`; `python/sglang/srt/configs/mamba_utils.py`; `python/sglang/srt/configs/nemotron_h.py`; `python/sglang/srt/configs/qwen3_next.py`; `python/sglang/srt/server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `27c447653` - model: support Qwen3.5 (#18489)

- Full hash: `27c447653d9cf0f63aea1c190b931be4875cbf86`
- Date/author: 2026-02-10 / Zheng Li
- Auto category: 性能/后端优化
- Main files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_5.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`
  - other: `python/sglang/srt/layers/logits_processor.py`; `python/sglang/srt/layers/rotary_embedding.py`; `python/sglang/srt/managers/mm_utils.py`; `python/sglang/srt/multimodal/processors/qwen_vl.py`; `python/sglang/srt/utils/common.py`; `python/sglang/srt/utils/hf_transformers_utils.py`
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_5_mtp.py`; `python/sglang/srt/models/qwen3_next.py` 等 10 个文件
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `bf89cc380` - [ModelOPT] Support Qwen 3 Next Coder NVFP4 (#18224)

- Full hash: `bf89cc3803873a00879c516e247df611ad3247a7`
- Date/author: 2026-02-08 / Yi Zhong
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `3ca29dffc` - support qwen3-next eagle3 (#14607)

- Full hash: `3ca29dffc72ac8a1000d3dad988fd96ab3339b9d`
- Date/author: 2026-02-01 / lukec
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `a0bae4c34` - Migrate 4-GPU/8-GPU workflow jobs to stage-c and add CI registry decorators (#17299)

- Full hash: `a0bae4c34349d09b3ad71db71d4fc3f4f32f221e`
- Date/author: 2026-01-31 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `.github/workflows/pr-test.yml`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`, `test/registered/8-gpu-models/test_deepseek_v32_basic.py`, `test/registered/8-gpu-models/test_deepseek_v32_mtp.py` 等 39 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/pr-test.yml`
  - other: `scripts/ci/utils/slash_command_handler.py`
  - tests: `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`; `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`; `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/4-gpu-models/test_qwen3_next_models_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v32_basic.py`; `test/registered/8-gpu-models/test_deepseek_v32_mtp.py`; `test/registered/8-gpu-models/test_deepseek_v3_basic.py`; `test/registered/8-gpu-models/test_deepseek_v3_mtp.py` 等 37 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `81449b4be` - Optimize GDN decode for Qwen3 Next (#17094)

- Full hash: `81449b4beebf761eab1ad67ad19e3cab4c0109d4`
- Date/author: 2026-01-31 / Sam (Kesen Li)
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/fla/fused_recurrent.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `336dc4579` - [CPU] Optimize Qwen3-next model on CPU (#12525)

- Full hash: `336dc4579e944728d3efe902a49ad75f195da5e4`
- Date/author: 2026-01-30 / jianan-gu
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/mem_cache/memory_pool.py` 等 13 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/amx_utils.py`; `python/sglang/srt/model_loader/weight_utils.py`
  - runtime-model: `python/sglang/srt/configs/qwen3_next.py`; `python/sglang/srt/configs/update_config.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`; `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/attention/intel_amx_backend.py`; `python/sglang/srt/layers/attention/mamba/mamba.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `sgl-kernel/csrc/cpu/topk.cpp`; `sgl-kernel/python/sgl_kernel/__init__.py`; `sgl-kernel/python/sgl_kernel/mamba.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d90c0837e` - [hybrid-model] clean up and consolidate redundant fields in RadixLinearAttention (#17660)

- Full hash: `d90c0837e5b812864a7570234b1a498740a01e85`
- Date/author: 2026-01-27 / Minglei Zhu
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/kimi_linear.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/kimi_linear.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/radix_linear_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9bd92ba0f` - Support PD disaggregation with different TP/DP size for Qwen3-Next (#16056)

- Full hash: `9bd92ba0f6e8040c2f9fb211a50c5094d4cb5d53`
- Date/author: 2026-01-25 / xjx471258437
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/srt/test_disaggregation_hybrid_attention.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/base/conn.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-perf: `python/sglang/srt/mem_cache/memory_pool.py`
  - tests: `test/srt/test_disaggregation_hybrid_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `fb683be6e` - Use attn tp group in embedding for more models (#17570)

- Full hash: `fb683be6eb7c6960f3d37ea91ca836c1b8e4120c`
- Date/author: 2026-01-24 / Ke Bao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/falcon_h1.py`, `python/sglang/srt/models/glm4.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_nextn.py`, `python/sglang/srt/models/gpt_oss.py` 等 19 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/falcon_h1.py`; `python/sglang/srt/models/glm4.py`; `python/sglang/srt/models/gpt_oss.py`; `python/sglang/srt/models/llada2.py`; `python/sglang/srt/models/llama4.py`; `python/sglang/srt/models/qwen2.py`; `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/qwen3_vl.py` 等 9 个文件
  - runtime-perf: `python/sglang/srt/models/bailing_moe.py`; `python/sglang/srt/models/bailing_moe_nextn.py`; `python/sglang/srt/models/glm4_moe.py`; `python/sglang/srt/models/glm4_moe_lite.py`; `python/sglang/srt/models/glm4_moe_nextn.py`; `python/sglang/srt/models/longcat_flash.py`; `python/sglang/srt/models/longcat_flash_nextn.py`; `python/sglang/srt/models/mimo_v2_flash.py` 等 10 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `419bbcee1` - refactor Qwen3-Next with a new RadixLinearAttention (#17373)

- Full hash: `419bbcee10a5a2f76b8b2612c7c2fbde3d0be645`
- Date/author: 2026-01-22 / Minglei Zhu
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/layers/radix_linear_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6f10e17b4` - [bugfix] fix qwen3-next alt_stream none issue (#17016)

- Full hash: `6f10e17b4a68df3cea7d37d30859409f62f720dc`
- Date/author: 2026-01-16 / billishyahao
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c5e363e8e` - test: split Qwen3 Next tests and disable PCG tests due to intermittent failures (#16989)

- Full hash: `c5e363e8e0ea7c1fe9873b951f556979fb949196`
- Date/author: 2026-01-13 / Alison Shao
- Auto category: 模型支持/运行时入口
- Main files: `test/srt/models/test_qwen3_next_models.py`, `test/srt/models/test_qwen3_next_models_mtp.py`, `test/srt/models/test_qwen3_next_models_pcg.py`, `test/srt/run_suite.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `test/srt/models/test_qwen3_next_models.py`; `test/srt/models/test_qwen3_next_models_mtp.py`; `test/srt/models/test_qwen3_next_models_pcg.py`; `test/srt/run_suite.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `206db66f5` - tiny refactor pcg split op registration (#16863)

- Full hash: `206db66f5c239bc13e6e4cfa7a4ea952612a2e59`
- Date/author: 2026-01-10 / Qiaolin Yu
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/compilation/compilation_config.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/compilation/compilation_config.py`; `python/sglang/srt/models/qwen3_next.py`
  - runtime-perf: `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/radix_attention.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d1ec93e3a` - Optimize layernorm_gated for Qwen3-Next (#16397)

- Full hash: `d1ec93e3acc483d37e33b1378f2b2ff7efbb3cfc`
- Date/author: 2026-01-10 / Yuan Luo
- Auto category: 性能/后端优化
- Main files: `benchmark/fla/benchmark_layernorm_gated.py`, `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/utils/common.py`, `test/srt/run_suite.py`, `test/srt/test_fla_layernorm_guard.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmark/fla/benchmark_layernorm_gated.py`
  - other: `python/sglang/srt/utils/common.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`
  - tests: `test/srt/run_suite.py`; `test/srt/test_fla_layernorm_guard.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `41609b52f` - support page size large than 64 for mamba radix cache with fix (#16768)

- Full hash: `41609b52fe78b1d72b6d67caeb5c526bb47ea6f2`
- Date/author: 2026-01-08 / Hanming Lu
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/server_args.py`, `test/srt/models/test_qwen3_next_models.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/schedule_batch.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`; `python/sglang/srt/mem_cache/mamba_radix_cache.py`
  - tests: `test/srt/models/test_qwen3_next_models.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6bc5a52fd` - [NPU] Adapt qwen3-next W8A8 on NPU (#16164)

- Full hash: `6bc5a52fd2d4807dcea21e822345fb5ea3e7bd4e`
- Date/author: 2026-01-03 / shengzhaotian
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `f6f7af406` - [Refactor] Clean up custom op (#15995)

- Full hash: `f6f7af406822669d2ff043fc7aafc4f5dfdb9413`
- Date/author: 2026-01-01 / DarkSharpness
- Auto category: 性能/后端优化
- Main files: `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/elementwise.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` 等 23 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/elementwise.py`; `python/sglang/srt/layers/layernorm.py`; `python/sglang/srt/utils/common.py`; `python/sglang/srt/utils/custom_op.py`
  - runtime-model: `python/sglang/srt/models/qwen3_next.py`; `python/sglang/srt/models/utils.py`
  - runtime-perf: `python/sglang/jit_kernel/utils.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/dp_attention.py`; `python/sglang/srt/layers/flashinfer_comm_fusion.py`; `python/sglang/srt/layers/moe/ep_moe/layer.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`; `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` 等 17 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ef92b4eb8` - [BUGFIX] fix edge case for qwen3-next (#14209)

- Full hash: `ef92b4eb88905b7b9415548e060870a99d5b6104`
- Date/author: 2025-12-26 / Yi Zhang
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/managers/scheduler.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `989d4b301` - [CI] Migrate nightly tests to test/registered/ (#15582)

- Full hash: `989d4b301293ea8eb243d7c320c5c457cb718629`
- Date/author: 2025-12-22 / Alison Shao
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/__init__.py`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/vlm_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py`, `python/sglang/test/run_combined_tests.py` 等 64 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-nvidia.yml`
  - tests: `python/sglang/test/accuracy_test_runner.py`; `python/sglang/test/ascend/__init__.py`; `python/sglang/test/ascend/gsm8k_ascend_mixin.py`; `python/sglang/test/ascend/vlm_utils.py`; `python/sglang/test/nightly_utils.py`; `python/sglang/test/performance_test_runner.py`; `python/sglang/test/run_combined_tests.py`; `test/registered/8-gpu-models/test_deepseek_v31.py` 等 63 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.
