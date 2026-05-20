# vllm Qwen3 Next Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `vllm/model_executor/models/qwen3_next.py` | `843c1822d`, `8cdc3a30b`, `df7041633`, `dcd80206b`, `5206e5e28`, `42135d689`, `9f430c94b`, `2612ba928`, `96fcd3c26`, `482914849`, `5708297e4`, `ace34e378`, ... (30 total) |
| `vllm/model_executor/models/qwen3_next_mtp.py` | `df7041633`, `dcd80206b`, `5206e5e28`, `600aaab8d`, `482914849`, `97d1c9930`, `9d1c47470`, `e50c45467` |
| `vllm/transformers_utils/configs/qwen3_next.py` | `e10c84e06`, `cd719de5c`, `a8b70304d` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/vllm`
- Generated date: 2026-05-20
- Commits in this document: 49
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-02-16 | `843c1822d` | 调度/缓存/PD | Add qwen3_5 | `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py` |
| 2026-02-10 | `8cdc3a30b` | 缺陷修复 | fix qwen3-next nn layout | `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/qwen3_next.py` |
| 2026-02-10 | `440222e9d` | 性能/后端优化 | fix qwen3-next run error | `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py` |
| 2026-02-06 | `df7041633` | 性能/后端优化 | sync v0.15.1 (models) | `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py` |
| 2026-01-26 | `dcd80206b` | 性能/后端优化 | [Chore] Update type annotation of `input_ids` in model forward (#33063) | `docs/contributing/model/basic.md`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_gemma_embedding.py`, `vllm/model_executor/models/afmoe.py` |
| 2026-01-24 | `5206e5e28` | 性能/后端优化 | [V1][Hybrid] Mamba Prefix Caching with align mode (#30877) | `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py` |
| 2026-01-21 | `42135d689` | 性能/后端优化 | [MoE Refactor] Oracle Select FP8+NVFP4 Kernels In Priority (#32414) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py` |
| 2026-01-15 | `1b5727520` | 性能/后端优化 | [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336) | `vllm/v1/attention/backends/rocm_attn.py` |
| 2026-01-15 | `e27078ea8` | 性能/后端优化 | [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336) | `vllm/v1/attention/backends/rocm_attn.py` |
| 2026-01-13 | `6fa6e7ef0` | 性能/后端优化 | [ROCm][CI] Disable Async Scheduling For Qwen3-Next-80B-A3B-Instruct MTP Async EPLB Accuracy Test (#32275) | `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2026-01-13 | `9f430c94b` | 缺陷修复 | [BUGFIX] Add missed remaping of the names of fp8 kv-scale (#32199) | `vllm/model_executor/models/qwen3_next.py` |
| 2026-01-12 | `600aaab8d` | 性能/后端优化 | [Model] Remove incorrect `SupportsPP` from MTP models (#32150) | `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py` |
| 2026-01-09 | `2612ba928` | 性能/后端优化 | [1/N][Attention] Restructure attention: move files (#31916) | `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/kernels.yaml` |
| 2026-01-09 | `1a19e9cd8` | 性能/后端优化 | [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten (#31380) | `tests/kernels/attention/test_prefix_prefill.py`, `vllm/attention/ops/chunked_prefill_paged_decode.py`, `vllm/attention/ops/prefix_prefill.py` |
| 2026-01-08 | `96fcd3c26` | 模型支持/运行时入口 | [Misc] Support qwen3-next lora (#31719) | `vllm/model_executor/models/qwen3_next.py` |
| 2026-01-07 | `482914849` | 性能/后端优化 | [BugFix] LoRA: Support loading base_layer of experts (#31104) | `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` |
| 2026-01-06 | `22dffca98` | 性能/后端优化 | [PERF] Speed-up of GDN attention decode part (Qwen3-Next) (#31722) | `vllm/model_executor/layers/fla/ops/fused_recurrent.py` |
| 2026-01-06 | `5708297e4` | 性能/后端优化 | [Misc][Model][Refactor] Pass the prefix into Linear layers (#31669) | `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/gpt_neox.py` |
| 2025-12-24 | `bc0a5a0c0` | 模型支持/运行时入口 | [CI] Add Qwen3-Next-FP8 to Blackwell model tests (#31049) | `tests/evals/gsm8k/configs/Qwen3-Next-FP8-EP2.yaml`, `tests/evals/gsm8k/configs/models-blackwell.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py` |
| 2025-12-18 | `41b6f9200` | 性能/后端优化 | Remove all2all backend envvar (#30363) | `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml` |
| 2025-12-18 | `717ac33d9` | 性能/后端优化 | [PERF] Qwen3-next. Add fp8 cutlass MoE tuned configs. `chmod -x *MI308X.json` (#29553) | `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=AMD_Instinct_MI308X.json`, `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json` |
| 2025-12-16 | `10ee1c64c` | 性能/后端优化 | [CI] Generalize gsm8k test args and add Qwen3-Next MTP B200 test (#30723) | `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/README.md`, `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml` |
| 2025-12-14 | `add1b9d3d` | 缺陷修复 | [main][BugFix] Fixed an accuracy bug of Qwen3-next-MTP when batched inferring (#30632) | `vllm/v1/attention/backends/gdn_attn.py` |
| 2025-12-14 | `97f2f160f` | 性能/后端优化 | [ROCm][CI] Add "Qwen3-Next-80B-A3B-Instruct MTP Async EPLB Accuracy Test" Back Into AMD CI (#30590) | `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml`, `vllm/distributed/eplb/rebalance_execute.py` |
| 2025-12-13 | `ace34e378` | 缺陷修复 | [Bugfix] Qwen3-next with --hf-overrides \{\"num_hidden_layers\":8\} (#30433) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-12-11 | `cf3eacfe5` | 性能/后端优化 | Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389) | `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py` |
| 2025-12-10 | `b4054c8ab` | 模型支持/运行时入口 | Revert "[CI] Add Async Eplb nightly CI tests (#29385)" (#30431) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2025-12-04 | `e10c84e06` | 性能/后端优化 | Access `partial_rotary_factor` from `rope_parameters` (#29966) | `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/apertus.py` |
| 2025-12-04 | `0765eb671` | 性能/后端优化 | Add new benchmark configurations for gfx936_80cu with E=512,N=64 and E=512,N=128 Qwen3-Next-80B-A3B-Instruct nn tp4 tp8 moe json | `benchmarks/kernels/E=512,N=128,device_name=gfx936_80cu_nn.json`, `benchmarks/kernels/E=512,N=64,device_name=gfx936_80cu_nn.json` |
| 2025-12-03 | `7fe9c1a22` | 模型支持/运行时入口 | [CI] Add Async Eplb nightly CI tests (#29385) | `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh` |
| 2025-11-30 | `cd719de5c` | 缺陷修复 | Fix RoPE failures in Transformers nightly (#29700) | `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/qwen3_next.py` |
| 2025-11-26 | `430dd4d9e` | 性能/后端优化 | [Attention] Remove imports from `vllm/attention/__init__.py` (#29342) | `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py` |
| 2025-11-25 | `77599fa7b` | 性能/后端优化 | [Qwen3-Next] MoE configs (TN) for BW1000 TP=4,8 | `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=gfx936_80cu.json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=64,device_name=gfx936_80cu.json` |
| 2025-11-19 | `a8b70304d` | 性能/后端优化 | Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542) | `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py` |
| 2025-11-20 | `d44e9df7d` | 模型支持/运行时入口 | [Model][Mamba] Add selector for mamba attention backend and make it pluggable for other device (#26487) | `docs/contributing/model/basic.md`, `vllm/attention/__init__.py`, `vllm/attention/backends/registry.py` |
| 2025-11-19 | `73ff872db` | 缺陷修复 | [Bugfix] Fix typo in Qwen3 Next model executor (#28960) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-13 | `97d1c9930` | 性能/后端优化 | Rename clashing method names for vLLM model protocol (#27583) | `docs/contributing/model/basic.md`, `docs/contributing/model/multimodal.md`, `vllm/model_executor/models/apertus.py` |
| 2025-11-12 | `9d1c47470` | 性能/后端优化 | [LoRA][1/N]Remove LoRA extra vocab (#28382) | `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/arctic.py` |
| 2025-11-11 | `f0359fffa` | 缺陷修复 | [Bugfix] fix qwen3-next crash (#28202) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-10 | `34553b9d2` | 性能/后端优化 | [Performance] Support FP8 flashinfer TRTLLM MOE on Qwen3 and Qwen-3next (#27492) | `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py` |
| 2025-11-10 | `c4768dcf4` | 性能/后端优化 | [Kernel] Fix fused_gdn_gating (#28343) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-09 | `7ae5a5fb1` | 模型支持/运行时入口 | [Misc] Add some comments in qwen3-next (#28267) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-06 | `b6a248bdd` | 性能/后端优化 | [PERF] Decouple projections from GDN custom op. Attempt 2 (#28083) | `vllm/config/compilation.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-06 | `c18f88c6c` | 性能/后端优化 | [Kernel] Fuse computation of g and beta for Gated Delta Net (#28095) | `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-05 | `e50c45467` | 性能/后端优化 | [BugFix] Support EP/DP + EPLB with MTP (#25311) | `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py` |
| 2025-11-05 | `4ea62b77f` | 性能/后端优化 | [Qwen3-Next] MOE configs for A100-SXM4-80GB TP4 TP8 (#27740) | `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_A100-SXM4-80GB.json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=64,device_name=NVIDIA_A100-SXM4-80GB.json` |
| 2025-11-05 | `d4e547bb7` | 性能/后端优化 | Revert "[PERF] Decouple projections from GDN custom op" (#28080) | `vllm/config/compilation.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/models/qwen3_next.py` |
| 2025-11-04 | `5fd8f02ea` | 性能/后端优化 | [PERF] Decouple projections from GDN custom op (#27512) | `vllm/config/compilation.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/models/qwen3_next.py` |
| 2025-10-29 | `8df98c216` | 性能/后端优化 | [perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next (#27578) | `vllm/model_executor/models/qwen3_next.py` |

## Per-Commit Audit Cards

### Commit `843c1822d` - Add qwen3_5

- Full hash: `843c1822de92edd962da42bbc490512a60aadbd5`
- Date/author: 2026-02-16 / Rayyyyy
- Auto category: 调度/缓存/PD
- Main files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next.py` 等 11 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/models/supported_models.md`
  - other: `vllm/v1/spec_decode/eagle.py`
  - runtime-model: `vllm/config/model.py`; `vllm/config/speculative.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/models/qwen3_5.py`; `vllm/model_executor/models/qwen3_5_mtp.py`; `vllm/model_executor/models/qwen3_next.py`; `vllm/model_executor/models/registry.py`; `vllm/transformers_utils/model_arch_config_convertor.py`
  - tests: `tests/models/registry.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `8cdc3a30b` - fix qwen3-next nn layout

- Full hash: `8cdc3a30b21b06a793c896ced997436b8f1cb255`
- Date/author: 2026-02-10 / zhuwenwen
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `440222e9d` - fix qwen3-next run error

- Full hash: `440222e9d56246e140274c7a9eb9a9df13756ddf`
- Date/author: 2026-02-10 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

### Commit `5206e5e28` - [V1][Hybrid] Mamba Prefix Caching with align mode (#30877)

- Full hash: `5206e5e28c25dcc43d3a2373b591a0cdf9792f5d`
- Date/author: 2026-01-24 / Harry Huang
- Auto category: 性能/后端优化
- Main files: `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/test_mamba_prefix_cache.py`, `vllm/config/cache.py`, `vllm/config/vllm.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py` 等 42 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `vllm/engine/arg_utils.py`; `vllm/v1/core/block_pool.py`
  - runtime-model: `vllm/config/vllm.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/mamba_mixer.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/mamba_utils.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/falcon_h1.py` 等 26 个文件
  - runtime-perf: `vllm/config/cache.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/v1/attention/backends/gdn_attn.py`; `vllm/v1/attention/backends/linear_attn.py`; `vllm/v1/attention/backends/mamba_attn.py`; `vllm/v1/attention/backends/utils.py`; `vllm/v1/core/kv_cache_coordinator.py` 等 12 个文件
  - tests: `tests/v1/core/test_single_type_kv_cache_manager.py`; `tests/v1/e2e/test_mamba_prefix_cache.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `42135d689` - [MoE Refactor] Oracle Select FP8+NVFP4 Kernels In Priority (#32414)

- Full hash: `42135d689830c0e764d925b6454bc68ba6c6cab4`
- Date/author: 2026-01-21 / Robert Shaw
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`, `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`, `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`, `benchmarks/kernels/benchmark_moe.py`, `docs/design/moe_kernel_features.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_silu_mul_quant_fusion.py` 等 82 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`; `benchmarks/kernels/benchmark_cutlass_moe_nvfp4.py`; `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`; `benchmarks/kernels/benchmark_moe.py`; `docs/design/moe_kernel_features.md`
  - other: `vllm/compilation/fusion.py`; `vllm/compilation/fusion_attn.py`; `vllm/compilation/matcher_utils.py`
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`; `vllm/model_executor/warmup/deep_gemm_warmup.py`
  - runtime-perf: `tools/vllm-rocm/pin_rocm_dependencies.py`; `vllm/compilation/activation_quant_fusion.py`; `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/cutlass_moe.py`; `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`; `vllm/model_executor/layers/fused_moe/fallback.py`; `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py` 等 38 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_silu_mul_quant_fusion.py`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ll.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-triton.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-cutlass.yaml`; `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-fi-trtllm.yaml` 等 33 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `1b5727520` - [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336)

- Full hash: `1b5727520749e533b532a8cfa76ad855447f9980`
- Date/author: 2026-01-15 / vllmellm
- Auto category: 性能/后端优化
- Main files: `vllm/v1/attention/backends/rocm_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/v1/attention/backends/rocm_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e27078ea8` - [Bugfix][ROCm][performance] Resolve the performance regression issue of the Qwen3-Next-80B-A3B-Thinking under rocm_atten (#32336)

- Full hash: `e27078ea807cf5655c6be3b59608e55c1682756d`
- Date/author: 2026-01-15 / vllmellm
- Auto category: 性能/后端优化
- Main files: `vllm/v1/attention/backends/rocm_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/v1/attention/backends/rocm_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `6fa6e7ef0` - [ROCm][CI] Disable Async Scheduling For Qwen3-Next-80B-A3B-Instruct MTP Async EPLB Accuracy Test (#32275)

- Full hash: `6fa6e7ef0c9b485e8a684211e96691731aad6faa`
- Date/author: 2026-01-13 / Micah Williamson
- Auto category: 性能/后端优化
- Main files: `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`
- Risk and verification: Mostly affects CI or engineering flow; use it as build, test, or dependency context for profiling work.

### Commit `9f430c94b` - [BUGFIX] Add missed remaping of the names of fp8 kv-scale (#32199)

- Full hash: `9f430c94bd0b5cf5a697ddeefd4507ae078bb0ed`
- Date/author: 2026-01-13 / Vadim Gimpelson
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `600aaab8d` - [Model] Remove incorrect `SupportsPP` from MTP models (#32150)

- Full hash: `600aaab8d626301f4dbfcd812ccf47b3e8d81ac9`
- Date/author: 2026-01-12 / Cyrus Leung
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/ernie_mtp.py`, `vllm/model_executor/models/glm4_moe_mtp.py`, `vllm/model_executor/models/longcat_flash_mtp.py`, `vllm/model_executor/models/openpangu_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/ernie_mtp.py`; `vllm/model_executor/models/openpangu_mtp.py`; `vllm/model_executor/models/qwen3_next_mtp.py`
  - runtime-perf: `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/longcat_flash_mtp.py`
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

### Commit `1a19e9cd8` - [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten (#31380)

- Full hash: `1a19e9cd87b6bb091fc9c530e6446601db52b58e`
- Date/author: 2026-01-09 / vllmellm
- Auto category: 性能/后端优化
- Main files: `tests/kernels/attention/test_prefix_prefill.py`, `vllm/attention/ops/chunked_prefill_paged_decode.py`, `vllm/attention/ops/prefix_prefill.py`, `vllm/attention/ops/triton_reshape_and_cache_flash.py`, `vllm/v1/attention/backends/rocm_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/attention/ops/chunked_prefill_paged_decode.py`; `vllm/attention/ops/prefix_prefill.py`; `vllm/attention/ops/triton_reshape_and_cache_flash.py`; `vllm/v1/attention/backends/rocm_attn.py`
  - tests: `tests/kernels/attention/test_prefix_prefill.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `96fcd3c26` - [Misc] Support qwen3-next lora (#31719)

- Full hash: `96fcd3c267a0b16e3f94abd59e05cb3708a67db8`
- Date/author: 2026-01-08 / BingjiaWang
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `22dffca98` - [PERF] Speed-up of GDN attention decode part (Qwen3-Next) (#31722)

- Full hash: `22dffca9822987f0e912bfd9635e94bbdd05def3`
- Date/author: 2026-01-06 / Vadim Gimpelson
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fla/ops/fused_recurrent.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/fla/ops/fused_recurrent.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `5708297e4` - [Misc][Model][Refactor] Pass the prefix into Linear layers (#31669)

- Full hash: `5708297e4e7f27c4d06d6e4f62d75c3d2d1fc674`
- Date/author: 2026-01-06 / Wang Kunpeng
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/gpt_neox.py`, `vllm/model_executor/models/hunyuan_v1.py`, `vllm/model_executor/models/jamba.py`, `vllm/model_executor/models/jina_vl.py`, `vllm/model_executor/models/minicpm.py`, `vllm/model_executor/models/minicpm_eagle.py` 等 17 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/mamba/mamba_mixer.py`; `vllm/model_executor/models/aria.py`; `vllm/model_executor/models/gpt_neox.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/jamba.py`; `vllm/model_executor/models/jina_vl.py`; `vllm/model_executor/models/minicpm.py`; `vllm/model_executor/models/minicpm_eagle.py` 等 15 个文件
  - runtime-perf: `vllm/model_executor/models/olmoe.py`; `vllm/model_executor/models/phimoe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `bc0a5a0c0` - [CI] Add Qwen3-Next-FP8 to Blackwell model tests (#31049)

- Full hash: `bc0a5a0c089844b17cb93f3294348f411e523586`
- Date/author: 2025-12-24 / Vadim Gimpelson
- Auto category: 模型支持/运行时入口
- Main files: `tests/evals/gsm8k/configs/Qwen3-Next-FP8-EP2.yaml`, `tests/evals/gsm8k/configs/models-blackwell.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py`, `tests/utils.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - tests: `tests/evals/gsm8k/configs/Qwen3-Next-FP8-EP2.yaml`; `tests/evals/gsm8k/configs/models-blackwell.txt`; `tests/evals/gsm8k/test_gsm8k_correctness.py`; `tests/utils.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

### Commit `41b6f9200` - Remove all2all backend envvar (#30363)

- Full hash: `41b6f9200fef27cd43b3299408a6f0e50654931f`
- Date/author: 2025-12-18 / Elizabeth Thomas
- Auto category: 性能/后端优化
- Main files: `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test-pipeline.yaml`, `.buildkite/test_areas/distributed.yaml`, `docs/design/moe_kernel_features.md`, `examples/online_serving/elastic_ep/serve_deepseek_v2.sh`, `tests/v1/cudagraph/test_cudagraph_dispatch.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`; `.buildkite/test-amd.yaml`; `.buildkite/test-pipeline.yaml`; `.buildkite/test_areas/distributed.yaml`
  - docs-bench: `docs/design/moe_kernel_features.md`; `examples/online_serving/elastic_ep/serve_deepseek_v2.sh`
  - other: `vllm/engine/arg_utils.py`; `vllm/envs.py`
  - runtime-model: `vllm/config/compilation.py`; `vllm/config/parallel.py`
  - tests: `tests/v1/cudagraph/test_cudagraph_dispatch.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `717ac33d9` - [PERF] Qwen3-next. Add fp8 cutlass MoE tuned configs. `chmod -x *MI308X.json` (#29553)

- Full hash: `717ac33d9cfa82357ea57dc0f6ee2aa325eba9f2`
- Date/author: 2025-12-18 / Vadim Gimpelson
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=AMD_Instinct_MI308X.json`, `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=256,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=64,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`; `vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=AMD_Instinct_MI308X.json`; `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`; `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`; `vllm/model_executor/layers/fused_moe/configs/E=512,N=256,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`; `vllm/model_executor/layers/fused_moe/configs/E=512,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`; `vllm/model_executor/layers/fused_moe/configs/E=64,N=512,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[128,128].json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `10ee1c64c` - [CI] Generalize gsm8k test args and add Qwen3-Next MTP B200 test (#30723)

- Full hash: `10ee1c64cfa7c0b7f68e9ee793435c9cafbf821a`
- Date/author: 2025-12-16 / Michael Goin
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `tests/evals/gsm8k/README.md`, `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml`, `tests/evals/gsm8k/configs/Llama-3-8B-Instruct-nonuniform-CT.yaml`, `tests/evals/gsm8k/configs/Llama-3.2-1B-Instruct-INT8-CT.yaml`, `tests/evals/gsm8k/configs/Qwen1.5-MoE-W4A16-CT.yaml`, `tests/evals/gsm8k/configs/Qwen2.5-VL-3B-Instruct-FP8-dynamic.yaml`, `tests/evals/gsm8k/configs/Qwen3-0.6B-FP8.yaml` 等 14 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`
  - tests: `tests/evals/gsm8k/README.md`; `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml`; `tests/evals/gsm8k/configs/Llama-3-8B-Instruct-nonuniform-CT.yaml`; `tests/evals/gsm8k/configs/Llama-3.2-1B-Instruct-INT8-CT.yaml`; `tests/evals/gsm8k/configs/Qwen1.5-MoE-W4A16-CT.yaml`; `tests/evals/gsm8k/configs/Qwen2.5-VL-3B-Instruct-FP8-dynamic.yaml`; `tests/evals/gsm8k/configs/Qwen3-0.6B-FP8.yaml`; `tests/evals/gsm8k/configs/Qwen3-30B-A3B-NVFP4.yaml` 等 12 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `add1b9d3d` - [main][BugFix] Fixed an accuracy bug of Qwen3-next-MTP when batched inferring (#30632)

- Full hash: `add1b9d3dec4a6d1b404f5793a210ff77482b7ae`
- Date/author: 2025-12-14 / drslark
- Auto category: 缺陷修复
- Main files: `vllm/v1/attention/backends/gdn_attn.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/v1/attention/backends/gdn_attn.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `97f2f160f` - [ROCm][CI] Add "Qwen3-Next-80B-A3B-Instruct MTP Async EPLB Accuracy Test" Back Into AMD CI (#30590)

- Full hash: `97f2f160fda2805f9149b0e44da76b5d3b1f7c7e`
- Date/author: 2025-12-14 / Micah Williamson
- Auto category: 性能/后端优化
- Main files: `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml`, `vllm/distributed/eplb/rebalance_execute.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`; `.buildkite/test-amd.yaml`
  - runtime-perf: `vllm/distributed/eplb/rebalance_execute.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `ace34e378` - [Bugfix] Qwen3-next with  --hf-overrides \{\"num_hidden_layers\":8\}  (#30433)

- Full hash: `ace34e3783208a31b185968a1e92c79ac8f633cb`
- Date/author: 2025-12-13 / Chen Zhang
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `cf3eacfe5` - Standardise `get_rope` to use `rope_parameters["partial_rotary_factor"]`, not `rotary_dim` (#30389)

- Full hash: `cf3eacfe58fa9e745c2854782ada884a9f992cf7`
- Date/author: 2025-12-11 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `benchmarks/kernels/benchmark_mrope.py`, `benchmarks/kernels/benchmark_rope.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `vllm/config/utils.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/afmoe.py` 等 83 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `benchmarks/kernels/benchmark_rope.py`
  - runtime-model: `vllm/config/utils.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/olmoe.py` 等 12 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `b4054c8ab` - Revert "[CI] Add Async Eplb nightly CI tests (#29385)" (#30431)

- Full hash: `b4054c8ab469a9c3c3c77a1c2f22f54a69b87145`
- Date/author: 2025-12-10 / Sage Moore
- Auto category: 模型支持/运行时入口
- Main files: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-pipeline.yaml`, `vllm/distributed/eplb/rebalance_execute.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`; `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/distributed/eplb/rebalance_execute.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `e10c84e06` - Access `partial_rotary_factor` from `rope_parameters` (#29966)

- Full hash: `e10c84e06af7264d5c0b3e7ec5604ada2eee7094`
- Date/author: 2025-12-04 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bamba.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/falcon_h1.py`, `vllm/model_executor/models/glm.py` 等 21 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/config.py`; `vllm/model_executor/models/falcon_h1.py`; `vllm/model_executor/models/glm.py`; `vllm/model_executor/models/glm4.py`; `vllm/model_executor/models/gpt_neox.py` 等 18 个文件
  - runtime-perf: `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/glm4_moe.py`
  - tests: `tests/kernels/core/test_mrope.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `0765eb671` - Add new benchmark configurations for gfx936_80cu with E=512,N=64 and E=512,N=128 Qwen3-Next-80B-A3B-Instruct nn tp4 tp8 moe json

- Full hash: `0765eb671881de3dc808e4d40a4c4e696ca1abc5`
- Date/author: 2025-12-04 / laibao
- Auto category: 性能/后端优化
- Main files: `benchmarks/kernels/E=512,N=128,device_name=gfx936_80cu_nn.json`, `benchmarks/kernels/E=512,N=64,device_name=gfx936_80cu_nn.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `benchmarks/kernels/E=512,N=128,device_name=gfx936_80cu_nn.json`; `benchmarks/kernels/E=512,N=64,device_name=gfx936_80cu_nn.json`
- Risk and verification: No explicit test surface is visible; reuse should add a minimal reproduction and target-model regression check.

### Commit `7fe9c1a22` - [CI] Add Async Eplb nightly CI tests (#29385)

- Full hash: `7fe9c1a2232275ee4cc7d65af3bc5b648543f367`
- Date/author: 2025-12-03 / WeiQing Chen
- Auto category: 模型支持/运行时入口
- Main files: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-pipeline.yaml`, `vllm/distributed/eplb/rebalance_execute.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`; `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`; `.buildkite/test-pipeline.yaml`
  - runtime-perf: `vllm/distributed/eplb/rebalance_execute.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `cd719de5c` - Fix RoPE failures in Transformers nightly (#29700)

- Full hash: `cd719de5cb2d0a7c8e1c93fedd206ca8eaa8c517`
- Date/author: 2025-11-30 / Harry Mellor
- Auto category: 缺陷修复
- Main files: `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/transformers_utils/config.py`; `vllm/transformers_utils/configs/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `430dd4d9e` - [Attention] Remove imports from `vllm/attention/__init__.py` (#29342)

- Full hash: `430dd4d9eb7e342e28012351df06d93892f86741`
- Date/author: 2025-11-26 / Matthew Bonanni
- Auto category: 性能/后端优化
- Main files: `docs/contributing/model/basic.md`, `tests/compile/test_fusion_attn.py`, `tests/compile/test_qk_norm_rope_fusion.py`, `tests/kernels/utils.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_utils.py`, `vllm/attention/__init__.py`, `vllm/attention/backends/abstract.py` 等 96 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/basic.md`
  - other: `vllm/compilation/fusion_attn.py`; `vllm/compilation/qk_norm_rope_fusion.py`; `vllm/v1/kv_offload/cpu.py`; `vllm/v1/kv_offload/spec.py`
  - runtime-model: `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/model_loader/utils.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bloom.py`; `vllm/model_executor/models/chameleon.py`; `vllm/model_executor/models/chatglm.py` 等 66 个文件
  - runtime-perf: `vllm/attention/__init__.py`; `vllm/attention/backends/abstract.py`; `vllm/attention/layer.py`; `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`; `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`; `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py` 等 20 个文件
  - tests: `tests/compile/test_fusion_attn.py`; `tests/compile/test_qk_norm_rope_fusion.py`; `tests/kernels/utils.py`; `tests/v1/worker/test_gpu_model_runner.py`; `tests/v1/worker/test_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `77599fa7b` - [Qwen3-Next] MoE configs (TN) for BW1000 TP=4,8

- Full hash: `77599fa7b6bf8c06465e6b89319d7e07f4300adc`
- Date/author: 2025-11-25 / zhuwenwen
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=gfx936_80cu.json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=64,device_name=gfx936_80cu.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=gfx936_80cu.json`; `vllm/model_executor/layers/fused_moe/configs/E=512,N=64,device_name=gfx936_80cu.json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `a8b70304d` - Update `rope_scaling` to `rope_parameters` in preparation for Transformers v5 (#28542)

- Full hash: `a8b70304d68497ac1c432a2ff343e9bfb516c227`
- Date/author: 2025-11-19 / Harry Mellor
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `benchmarks/kernels/benchmark_mrope.py`, `examples/offline_inference/context_extension.py`, `tests/compile/test_functionalization.py`, `tests/kernels/core/test_mrope.py`, `tests/kernels/core/test_pos_encoding.py`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/models/language/pooling/test_nomic_max_model_len.py` 等 104 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - docs-bench: `benchmarks/kernels/benchmark_mrope.py`; `examples/offline_inference/context_extension.py`
  - runtime-model: `vllm/config/model.py`; `vllm/model_executor/layers/rotary_embedding/__init__.py`; `vllm/model_executor/models/apertus.py`; `vllm/model_executor/models/arcee.py`; `vllm/model_executor/models/arctic.py`; `vllm/model_executor/models/baichuan.py`; `vllm/model_executor/models/bamba.py`; `vllm/model_executor/models/chameleon.py` 等 78 个文件
  - runtime-perf: `vllm/model_executor/models/afmoe.py`; `vllm/model_executor/models/bailing_moe.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/ernie45_vl_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/granitemoe.py`; `vllm/model_executor/models/granitemoehybrid.py`; `vllm/model_executor/models/granitemoeshared.py` 等 17 个文件
  - tests: `tests/compile/test_functionalization.py`; `tests/kernels/core/test_mrope.py`; `tests/kernels/core/test_pos_encoding.py`; `tests/kernels/moe/test_gpt_oss_triton_kernels.py`; `tests/models/language/pooling/test_nomic_max_model_len.py`; `tests/test_config.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d44e9df7d` - [Model][Mamba] Add selector for mamba attention backend and make it pluggable for other device (#26487)

- Full hash: `d44e9df7d49a9bb3400b002c38c06fae2dd7d1e8`
- Date/author: 2025-11-20 / Shanshan Shen
- Auto category: 模型支持/运行时入口
- Main files: `docs/contributing/model/basic.md`, `vllm/attention/__init__.py`, `vllm/attention/backends/registry.py`, `vllm/attention/selector.py`, `vllm/model_executor/layers/kda.py`, `vllm/model_executor/layers/mamba/abstract.py`, `vllm/model_executor/layers/mamba/linear_attn.py`, `vllm/model_executor/layers/mamba/mamba_mixer.py` 等 12 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - docs-bench: `docs/contributing/model/basic.md`
  - runtime-model: `vllm/model_executor/layers/kda.py`; `vllm/model_executor/layers/mamba/abstract.py`; `vllm/model_executor/layers/mamba/linear_attn.py`; `vllm/model_executor/layers/mamba/mamba_mixer.py`; `vllm/model_executor/layers/mamba/mamba_mixer2.py`; `vllm/model_executor/layers/mamba/short_conv.py`; `vllm/model_executor/models/plamo2.py`; `vllm/model_executor/models/qwen3_next.py`
  - runtime-perf: `vllm/attention/__init__.py`; `vllm/attention/backends/registry.py`; `vllm/attention/selector.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `73ff872db` - [Bugfix] Fix typo in Qwen3 Next model executor (#28960)

- Full hash: `73ff872db0d4e3f5e133d5d2a5307248619d93a6`
- Date/author: 2025-11-19 / Gleb Kurchanov
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

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

### Commit `f0359fffa` - [Bugfix] fix qwen3-next crash (#28202)

- Full hash: `f0359fffa434a4fce981389f9dff93a2a4c2b13e`
- Date/author: 2025-11-11 / Jiangyun Zhu
- Auto category: 缺陷修复
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `34553b9d2` - [Performance] Support FP8 flashinfer TRTLLM MOE on Qwen3 and Qwen-3next (#27492)

- Full hash: `34553b9d2702dd2a27a578fec819e88e76dcbfb4`
- Date/author: 2025-11-10 / jiahanc
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`, `vllm/model_executor/models/qwen3_moe.py`, `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
  - runtime-perf: `vllm/model_executor/layers/fused_moe/config.py`; `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`; `vllm/model_executor/layers/fused_moe/layer.py`; `vllm/model_executor/layers/quantization/fp8.py`; `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`; `vllm/model_executor/models/qwen3_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `c4768dcf4` - [Kernel] Fix fused_gdn_gating (#28343)

- Full hash: `c4768dcf47ae919257e31b49a03c00d383ba3c55`
- Date/author: 2025-11-10 / Jiangyun Zhu
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `7ae5a5fb1` - [Misc] Add some comments in qwen3-next (#28267)

- Full hash: `7ae5a5fb11151e029609009b7950cc46ff097407`
- Date/author: 2025-11-09 / Jiangyun Zhu
- Auto category: 模型支持/运行时入口
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `b6a248bdd` - [PERF] Decouple projections from GDN custom op. Attempt 2 (#28083)

- Full hash: `b6a248bdd7bff91a15c4f2395762f8ce4c19c759`
- Date/author: 2025-11-06 / Vadim Gimpelson
- Auto category: 性能/后端优化
- Main files: `vllm/config/compilation.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/config/compilation.py`; `vllm/model_executor/layers/layernorm.py`; `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `c18f88c6c` - [Kernel] Fuse computation of g and beta for Gated Delta Net (#28095)

- Full hash: `c18f88c6cae04b59136f7c932c6e6a11d04e6e76`
- Date/author: 2025-11-06 / Jiangyun Zhu
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `e50c45467` - [BugFix] Support EP/DP + EPLB with MTP (#25311)

- Full hash: `e50c45467215f96068d95736b08d8a25f624e67d`
- Date/author: 2025-11-05 / Ilya Markov
- Auto category: 性能/后端优化
- Main files: `.buildkite/test-pipeline.yaml`, `tests/distributed/test_eplb_spec_decode.py`, `vllm/distributed/eplb/eplb_state.py`, `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`, `vllm/model_executor/models/deepseek_eagle.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/ernie45_moe.py` 等 27 个文件
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - ci: `.buildkite/test-pipeline.yaml`
  - other: `vllm/v1/spec_decode/medusa.py`
  - runtime-model: `vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py`; `vllm/model_executor/models/deepseek_eagle.py`; `vllm/model_executor/models/deepseek_mtp.py`; `vllm/model_executor/models/deepseek_v2.py`; `vllm/model_executor/models/hunyuan_v1.py`; `vllm/model_executor/models/interfaces.py`; `vllm/model_executor/models/llama4.py`; `vllm/model_executor/models/llama4_eagle.py` 等 17 个文件
  - runtime-perf: `vllm/distributed/eplb/eplb_state.py`; `vllm/model_executor/models/ernie45_moe.py`; `vllm/model_executor/models/glm4_moe.py`; `vllm/model_executor/models/glm4_moe_mtp.py`; `vllm/model_executor/models/lfm2_moe.py`; `vllm/model_executor/models/qwen3_moe.py`; `vllm/model_executor/models/transformers/moe.py`
  - tests: `tests/distributed/test_eplb_spec_decode.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `4ea62b77f` - [Qwen3-Next] MOE configs for A100-SXM4-80GB TP4 TP8 (#27740)

- Full hash: `4ea62b77f5c009515f50d14cda24665101a5d910`
- Date/author: 2025-11-05 / tou
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_A100-SXM4-80GB.json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=64,device_name=NVIDIA_A100-SXM4-80GB.json`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_A100-SXM4-80GB.json`; `vllm/model_executor/layers/fused_moe/configs/E=512,N=64,device_name=NVIDIA_A100-SXM4-80GB.json`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `d4e547bb7` - Revert "[PERF] Decouple projections from GDN custom op" (#28080)

- Full hash: `d4e547bb7e06ab05c56a567b9a9f33b6c893dc66`
- Date/author: 2025-11-05 / Vadim Gimpelson
- Auto category: 性能/后端优化
- Main files: `vllm/config/compilation.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/config/compilation.py`; `vllm/model_executor/layers/layernorm.py`; `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `5fd8f02ea` - [PERF] Decouple projections from GDN custom op (#27512)

- Full hash: `5fd8f02ea9f2bb12b9b68d9dbd9629d555482d98`
- Date/author: 2025-11-04 / Vadim Gimpelson
- Auto category: 性能/后端优化
- Main files: `vllm/config/compilation.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/config/compilation.py`; `vllm/model_executor/layers/layernorm.py`; `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

### Commit `8df98c216` - [perf] Enable concurrent execution of "shared_experts" and "selected_experts" in qwen3-next (#27578)

- Full hash: `8df98c2161e28387391b667201f8458c2bdf29f4`
- Date/author: 2025-10-29 / Jiangyun Zhu
- Auto category: 性能/后端优化
- Main files: `vllm/model_executor/models/qwen3_next.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `vllm/model_executor/models/qwen3_next.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.
