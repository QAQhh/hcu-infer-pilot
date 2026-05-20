# sglang GLM-5/5.1 Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `docs/platforms/ascend_npu_glm5_examples.md` | `2d583799e`, `210d0fbae`, `56891e46b`, `f65c885e7`, `123f57b84`, `c34832c02` |
| `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` | `23adb5075` |
| `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py` | `23adb5075` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 18
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-30 | `752ed6468` | 性能/后端优化 | 修复glm5w4a8重排逻辑，减少显存占用 | `python/sglang/srt/layers/quantization/w4a8_utils.py` |
| 2026-04-30 | `262fa654e` | 调度/缓存/PD | 【GLM5】NSA indexer新增bf16路径 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` |
| 2026-04-28 | `74f1c1b27` | 调度/缓存/PD | 合入官方pr，解决glm5跑pd分离时page计算不一致崩溃 | `python/sglang/srt/disaggregation/mooncake/conn.py` |
| 2026-04-25 | `78557fe3d` | 通用实现调整 | 【GLM5】避免DCU路径加载TileLang和TVM依赖 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py` |
| 2026-04-23 | `c40804b20` | 性能/后端优化 | 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合 3. 融合get_logits_head_gate算子 | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py` |
| 2026-04-10 | `2854c89b4` | 性能/后端优化 | 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化 | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` |
| 2026-03-25 | `2d583799e` | 调度/缓存/PD | Update ascend docs (#20846) | `docs/platforms/ascend_npu_best_practice.md`, `docs/platforms/ascend_npu_deepseek_example.md`, `docs/platforms/ascend_npu_glm5_examples.md` |
| 2026-03-17 | `da2447891` | 性能/后端优化 | [AMD] Fix CI: update transformers in Qwen 3.5 and GLM-5 nightly tests (#20750) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml` |
| 2026-03-17 | `210d0fbae` | 调度/缓存/PD | Update ascend docs (#20674) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md` |
| 2026-03-09 | `be63f982b` | 性能/后端优化 | [V32/GLM5] Control the threshold of applying dense attention with an environ (#20062) | `docs/references/environment_variables.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa_backend.py` |
| 2026-03-07 | `d28f35240` | 通用实现调整 | [V32/GLM5] Change default setting of V32 nvfp4 on TP4 (#20086) | `python/sglang/srt/server_args.py` |
| 2026-02-25 | `56891e46b` | 模型支持/运行时入口 | [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339) | `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md` |
| 2026-02-24 | `23adb5075` | 性能/后端优化 | [AMD] [GLM-5 Day 0] Add GLM-5 nightly test (#18911) | `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py` |
| 2026-02-22 | `eddf19329` | 性能/后端优化 | [DSv32] [GLM5] Improve Model Quality by Avoiding FP32 Precision Loss in `weights_proj` (#19041) | `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py` |
| 2026-02-17 | `1b659bcb0` | 性能/后端优化 | Fix GLM-5 fused shared expert (#18804) | `python/sglang/srt/models/glm4_moe.py` |
| 2026-02-13 | `f65c885e7` | 测试/文档/基准 | Modify glm5 readme on npu (#18768) | `docs/platforms/ascend_npu_glm5_examples.md` |
| 2026-02-12 | `123f57b84` | 调度/缓存/PD | update glm5 readme on npu (#18657) | `docs/platforms/ascend_npu_glm5_examples.md` |
| 2026-02-12 | `c34832c02` | 测试/文档/基准 | glm5 md (#18655) | `docs/platforms/ascend_npu_glm5_examples.md` |

## Per-Commit Audit Cards

### Commit `752ed6468` - 修复glm5w4a8重排逻辑，减少显存占用

- Full hash: `752ed6468ffafbcd5743df06e40eb5ef2685a29c`
- Date/author: 2026-04-30 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/w4a8_utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/quantization/w4a8_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `262fa654e` - 【GLM5】NSA indexer新增bf16路径

- Full hash: `262fa654e806f504f9a20f5b7438975bb719d891`
- Date/author: 2026-04-30 / maxiao1
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `74f1c1b27` - 合入官方pr，解决glm5跑pd分离时page计算不一致崩溃

- Full hash: `74f1c1b27935b7b6fc83c3d25f962cc31e4f625e`
- Date/author: 2026-04-28 / maxiao1
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/disaggregation/mooncake/conn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/mooncake/conn.py`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `78557fe3d` - 【GLM5】避免DCU路径加载TileLang和TVM依赖

- Full hash: `78557fe3d0893bb8173b1322ef08fe722accf2af`
- Date/author: 2026-04-25 / maxiao1
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c40804b20` - 【GLM5-融合算子】1. 融合set_kv_buffer和quant算子 2. paged mqa logits算子融合  3. 融合get_logits_head_gate算子

- Full hash: `c40804b203877a1affe2cc3862fc26dc29b8efdd`
- Date/author: 2026-04-23 / maxiao
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/mem_cache/memory_pool.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2854c89b4` - 适配glm5 & 接入topk_transform融合算子 & 适配cp功能 & 暂时移除ttft优化

- Full hash: `2854c89b4ee838989dea9b7e403840dfcf4d7116`
- Date/author: 2026-04-10 / maxiao1
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/disaggregation/prefill.py`
  - runtime-model: `python/sglang/srt/models/deepseek_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`; `python/sglang/srt/layers/attention/nsa_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2d583799e` - Update ascend docs (#20846)

- Full hash: `2d583799ebb8ba67732e8bc5c70e814734491337`
- Date/author: 2026-03-25 / amote-i
- Auto category: 调度/缓存/PD
- Main files: `docs/platforms/ascend_npu_best_practice.md`, `docs/platforms/ascend_npu_deepseek_example.md`, `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_support_features.md`, `docs/platforms/ascend_npu_support_models.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_best_practice.md`; `docs/platforms/ascend_npu_deepseek_example.md`; `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_support_features.md`; `docs/platforms/ascend_npu_support_models.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `da2447891` - [AMD] Fix CI: update transformers in Qwen 3.5 and GLM-5 nightly tests (#20750)

- Full hash: `da24478913f5fbac87644c3679e051ed5276fdbe`
- Date/author: 2026-03-17 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `210d0fbae` - Update ascend docs (#20674)

- Full hash: `210d0fbaef41bb18a83320e1fbe8f50c9d0c9ead`
- Date/author: 2026-03-17 / amote-i
- Auto category: 调度/缓存/PD
- Main files: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`, `docs/platforms/ascend_npu_support_features.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`; `docs/platforms/ascend_npu_support_features.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `be63f982b` - [V32/GLM5] Control the threshold of applying dense attention with an environ (#20062)

- Full hash: `be63f982b7b7f0451a3ccbb13f6fe2ecf6c39796`
- Date/author: 2026-03-09 / Baizhou Zhang
- Auto category: 性能/后端优化
- Main files: `docs/references/environment_variables.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/server_args.py`, `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`, `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/references/environment_variables.md`
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa_backend.py`
  - tests: `test/registered/quant/test_deepseek_v32_fp4_4gpu.py`; `test/registered/quant/test_deepseek_v32_fp4_mtp_4gpu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d28f35240` - [V32/GLM5] Change default setting of V32 nvfp4 on TP4 (#20086)

- Full hash: `d28f35240a28de1e09967975e258b3dd7e74924f`
- Date/author: 2026-03-07 / Baizhou Zhang
- Auto category: 通用实现调整
- Main files: `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `56891e46b` - [Ascend ] Add qwen3.5 122B/35B/27B deployment examples on doc (#19339)

- Full hash: `56891e46bc1ac4f75e8e541b61810f777cda8209`
- Date/author: 2026-02-25 / Hexq0210
- Auto category: 模型支持/运行时入口
- Main files: `docs/platforms/ascend_npu_glm5_examples.md`, `docs/platforms/ascend_npu_qwen3_5_examples.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`; `docs/platforms/ascend_npu_qwen3_5_examples.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `23adb5075` - [AMD] [GLM-5 Day 0] Add GLM-5 nightly test (#18911)

- Full hash: `23adb50751d50638e52504ea223ad9d6677fd478`
- Date/author: 2026-02-24 / Michael
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`, `test/registered/amd/accuracy/mi30x/test_gsm8k_eval_amd.py`, `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.github/workflows/nightly-test-amd-rocm720.yml`; `.github/workflows/nightly-test-amd.yml`
  - tests: `test/registered/amd/accuracy/mi30x/test_glm5_eval_amd.py`; `test/registered/amd/accuracy/mi30x/test_gsm8k_eval_amd.py`; `test/registered/amd/accuracy/mi35x/test_glm5_eval_mi35x.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `eddf19329` - [DSv32] [GLM5] Improve Model Quality by Avoiding FP32 Precision Loss in `weights_proj` (#19041)

- Full hash: `eddf193292d310b416473815cffb0c9d13985be2`
- Date/author: 2026-02-22 / Ziang Li
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `test/registered/kernels/test_nsa_indexer.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`; `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`
  - runtime-perf: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`
  - tests: `test/registered/kernels/test_nsa_indexer.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1b659bcb0` - Fix GLM-5 fused shared expert (#18804)

- Full hash: `1b659bcb088fd303ee472c0720eeb1a3797cffa1`
- Date/author: 2026-02-17 / Frank Minors
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/glm4_moe.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/models/glm4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `f65c885e7` - Modify glm5 readme on npu (#18768)

- Full hash: `f65c885e7ccda97c31a8d6619d1620ff8bdb008e`
- Date/author: 2026-02-13 / BourneSun0527
- Auto category: 测试/文档/基准
- Main files: `docs/platforms/ascend_npu_glm5_examples.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `123f57b84` - update glm5 readme on npu (#18657)

- Full hash: `123f57b84bbaeb23e673d33598279fcf564f9607`
- Date/author: 2026-02-12 / fy
- Auto category: 调度/缓存/PD
- Main files: `docs/platforms/ascend_npu_glm5_examples.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `c34832c02` - glm5 md (#18655)

- Full hash: `c34832c02c28360cca5657f26741001dd9d3fe7c`
- Date/author: 2026-02-12 / liupeng374
- Auto category: 测试/文档/基准
- Main files: `docs/platforms/ascend_npu_glm5_examples.md`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/platforms/ascend_npu_glm5_examples.md`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.
