# vllm MiMo V2 Flash Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `vllm/model_executor/models/mimo.py` | `df7041633`, `dcd80206b`, `97d1c9930`, `9d1c47470` |
| `vllm/model_executor/models/mimo_mtp.py` | `df7041633`, `dcd80206b`, `97d1c9930` |
| `vllm/model_executor/models/mimo_v2_flash.py` | `df7041633`, `dcd80206b`, `2612ba928`, `482914849`, `951302989`, `969bbc7c6` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 8
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-05 | `951302989` | 性能/后端优化 | [Bugfix] Properly apply v_scale for mimo_v2_flash (#31175) | `vllm/model_executor/models/mimo_v2_flash.py` |
| 2025-12-20 | `969bbc7c6` | 性能/后端优化 | [Model] Add MiMo-V2-Flash support (#30836) | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/__init__.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `9d1c47470` | 性能/后端优化 | [LoRA][1/N]Remove LoRA extra vocab (#28382) | `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py` |

## Per-Commit Audit Cards

### Commit `df7041633` - sync v0.15.1 (models)

- Full hash: `df7041633878cacfcd677cef5efc907705de6c98`
- Date/author: 2026-02-06 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/bagel.py` 等 169 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 147 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `dcd80206b` - [Chore] Update type annotation of `input_ids` in model forward (#33063)

- Full hash: `dcd80206b7a9143c81f7f2808e84914f8e38ce95`
- Date/author: 2026-01-26 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/audioflamingo3.py` 等 164 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/basic.md`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/audioflamingo3.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/bagel.py`; `vllm/model_executor/models/baichuan.py` 等 140 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/exaone_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_lite.py`; `vllm/model_executor/models/glm4_moe_lite_mtp.py` 等 22 个文件
  - tests: `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `2612ba928` - [1/N][Attention] Restructure attention: move files (#31916)

- Full hash: `2612ba9285d828f3179801334b6d2db0046b9b6c`
- Date/author: 2026-01-09 / Matthew Bonanni
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml`, `.github/CODEOWNERS`, `.github/mergify.yml`, `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`, `docs/contributing/model/basic.md`, `docs/design/custom_op.md` 等 195 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/kernels.yaml`; `.github/CODEOWNERS`; `.github/mergify.yml`
  - docs-bench: `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`; `docs/contributing/model/basic.md`; `docs/design/custom_op.md`; `docs/design/plugin_system.md`; `examples/offline_inference/basic/embed.py`; `examples/offline_inference/basic/score.py`
  - other: `tools/pre_commit/mypy.py`; `vllm/engine/arg_utils.py`; `vllm/envs.py`; `vllm/forward_context.py`; `vllm/platforms/cpu.py`; `vllm/platforms/interface.py`; `vllm/platforms/xpu.py`; `vllm/v1/kv_offload/cpu.py` 等 10 个文件
  - runtime-model: `vllm/config/model.py`; `vllm/config/multimodal.py`; `vllm/model_executor/layers/batch_invariant.py`; `vllm/model_executor/layers/kda.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/short_conv.py` 等 66 个文件
  - runtime-perf: `vllm/attention/layer.py`; `vllm/attention/ops/__init__.py`; `vllm/config/attention.py`; `vllm/distributed/kv_transfer/kv_connector/utils.py`; `vllm/distributed/kv_transfer/kv_connector/v1/base.py`; `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py` 等 73 个文件
  - tests: `tests/compile/fullgraph/test_full_cudagraph.py`; `tests/compile/fullgraph/test_full_graph.py`; `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/config/test_multimodal_config.py`; `tests/engine/test_arg_utils.py`; `tests/kernels/attention/test_aiter_flash_attn.py`; `tests/kernels/attention/test_attention.py` 等 35 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `482914849` - [BugFix] LoRA: Support loading base_layer of experts (#31104)

- Full hash: `482914849cf9ce61d3e0dffaa35096bb34de58f5`
- Date/author: 2026-01-07 / ℍ𝕠𝕝𝕝𝕠𝕨 𝕄𝕒𝕟
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/dots1.py`, `vllm/model_executor/models/ernie45_moe.py` 等 35 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/dots1.py`; `vllm/model_executor/models/gpt_oss.py`; `vllm/model_executor/models/grok1.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/jamba.py` 等 19 个文件
  - runtime-perf: `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py` 等 16 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `951302989` - [Bugfix] Properly apply v_scale for mimo_v2_flash (#31175)

- Full hash: `95130298981428053a23376e89a771afc7fc37af`
- Date/author: 2026-01-05 / Michael Goin
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/mimo_v2_flash.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/models/mimo_v2_flash.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `969bbc7c6` - [Model] Add MiMo-V2-Flash support (#30836)

- Full hash: `969bbc7c6166ce10a48df2fcdc2fba508dbafcce`
- Date/author: 2025-12-20 / Zhonghua Deng
- Auto category: 性能/后端优化
- Main files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/__init__.py`, `vllm/config/model.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`, `vllm/model_executor/models/mimo_v2_flash.py`, `vllm/model_executor/models/registry.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`
  - runtime-model: `vllm/config/__init__.py`; `vllm/config/model.py`; `vllm/model_executor/layers/linear.py`; `vllm/model_executor/models/registry.py`
  - runtime-perf: `vllm/model_executor/layers/quantization/utils/fp8_utils.py`; `vllm/model_executor/models/mimo_v2_flash.py`
  - tests: `tests/models/registry.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `97d1c9930` - Rename clashing method names for vLLM model protocol (#27583)

- Full hash: `97d1c99302df6f7eadc0d0b32ec174db69cb4421`
- Date/author: 2025-11-13 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/baichuan.py` 等 164 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/basic.md`; `docs/contributing/model/multimodal.md`
  - other: `vllm/multimodal/processing.py`; `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/aya_vision.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/bert.py` 等 144 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 16 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `9d1c47470` - [LoRA][1/N]Remove LoRA extra vocab (#28382)

- Full hash: `9d1c47470430ba31c02946aa1fd01aadf6e18b91`
- Date/author: 2025-11-12 / Jee Jee Li
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/baichuan.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/chameleon.py` 等 65 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 58 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/longcat_flash.py`; `vllm/model_executor/models/phimoe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.
