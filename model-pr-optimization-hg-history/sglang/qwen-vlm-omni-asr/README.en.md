# sglang Qwen VLM/Omni/ASR Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/qwen3_vl.py` | `c1d308c60`, `32bd2422e` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 2
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-04-29 | `c1d308c60` | 缺陷修复 | 修复qwen3.5-397b-fp8报错问题 | `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |
| 2026-04-23 | `32bd2422e` | 缺陷修复 | 修复qwen3.5模型memory_Async问题 | `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py` |

## Per-Commit Audit Cards

### Commit `c1d308c60` - 修复qwen3.5-397b-fp8报错问题

- Full hash: `c1d308c602379d71d746bc50ed785c2bee05ba99`
- Date/author: 2026-04-29 / liucong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/layers/attention/fla/index.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/layers/attention/fla/index.py`; `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `32bd2422e` - 修复qwen3.5模型memory_Async问题

- Full hash: `32bd2422e7d17f0cee10413aad4a223ffb25dd74`
- Date/author: 2026-04-23 / liucong
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/sampling/sampling_batch_info.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - other: `python/sglang/srt/managers/schedule_batch.py`; `python/sglang/srt/sampling/sampling_batch_info.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/srt/mem_cache/common.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 3 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/environ.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/models/qwen3_5.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/models/qwen3_vl.py` | `123e9539e`, `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/distributed/parallel_state.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/layers/attention/linear/gdn_backend.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/slimquant_w4a8_marlin.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/layers/quantization/unquant.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/model_executor/model_runner.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_v2.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/models/deepseek_v4.py` | `123e9539e`, `7b3548f97` |
| `python/sglang/srt/server_args.py` | `123e9539e`, `f8bfbc60f` |
| `python/sglang/srt/speculative/draft_utils.py` | `7b3548f97`, `f8bfbc60f` |
| `python/sglang/srt/speculative/eagle_worker_v2.py` | `123e9539e`, `f8bfbc60f` |
| `benchmark/kernels/fused_moe_triton/common_utils.py` | `f8bfbc60f` |
| `python/sglang/check_env.py` | `123e9539e` |
| `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh` | `123e9539e` |
| `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` | `123e9539e` |
| `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh` | `123e9539e` |
| `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh` | `7b3548f97` |
| `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu` | `7b3548f97` |
| `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh` | `f8bfbc60f` |
| `python/sglang/kernels/ops/attention/qsa_indexer.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/elementwise/fast_topk.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/elementwise/hc_combine.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/elementwise/hc_mix.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/gemm/flashinfer_pr4266_dense_bf16_gemm_sm100_splitk.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/layernorm/grouped_gemma_rmsnorm.py` | `f8bfbc60f` |
| `python/sglang/kernels/ops/moe/ep_moe_kernels.py` | `7b3548f97` |
| ... | 172 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` and 91 files in total |
| 2026-08-25 | `7b3548f97` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix lint: apply pre-commit fixes across the 20260824 sync diff | `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` and 48 files in total |
| 2026-09-03 | `f8bfbc60f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat(hcu): Qwen3.8 flash next open support (#281) | `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh` and 100 files in total |

### Per-Commit Audit Cards

#### Commit `123e9539e` - fix lint: satisfy pre-commit on the forward-port diff

- Full hash: `123e9539ea23dde2f1a12b0374c1375bbfb10989`
- Date/author: 2026-07-31 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py` 等 91 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/check_env.py`; `python/sglang/srt/batch_overlap/two_batch_overlap.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/communicator.py`; `python/sglang/srt/layers/layernorm.py` 等 14 个文件
  - runtime-model: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_nextn.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py` 等 19 个文件
  - runtime-perf: `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`; `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`; `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`; `python/sglang/kernels/ops/quantization/fp8_kernel.py`; `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`; `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`; `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`; `python/sglang/srt/distributed/device_communicators/quick_all_reduce.py` 等 56 个文件
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/simple_eval_mmlu.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `7b3548f97` - fix lint: apply pre-commit fixes across the 20260824 sync diff

- Full hash: `7b3548f97409d83b7e7dde4c3ad71e2f30955267`
- Date/author: 2026-08-25 / RyeYuan
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/utils.py` 等 48 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/multimodal_gen/runtime/layers/usp.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/hardware_backend/npu/utils.py`; `python/sglang/srt/sampling/sampling_batch_info.py`; `python/sglang/srt/speculative/draft_utils.py`; `python/sglang/srt/speculative/eagle_utils.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/qwen3_5.py`; `python/sglang/srt/models/qwen3_vl.py`
  - runtime-perf: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`; `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`; `python/sglang/kernels/ops/moe/ep_moe_kernels.py`; `python/sglang/srt/distributed/parallel_state.py`; `python/sglang/srt/layers/attention/aiter_backend.py`; `python/sglang/srt/layers/attention/attention_registry.py`; `python/sglang/srt/layers/attention/base_attn_backend.py`; `python/sglang/srt/layers/attention/deepseek_v4_backend.py` 等 22 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_server_args.py`; `test/registered/hicache/test_hicache_storage_3fs_backend.py`; `test/registered/openai_server/validation/test_matched_stop.py`; `test/registered/pp/test_pp_single_node.py`; `test/registered/profiling/test_start_profile.py`; `test/registered/unit/entrypoints/openai/test_serving_embedding.py`; `test/registered/unit/function_call/test_function_call_parser.py`; `test/registered/unit/function_call/test_json_schema_constraint.py` 等 13 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f8bfbc60f` - feat(hcu): Qwen3.8 flash next open support (#281)

- Full hash: `f8bfbc60fbb9400391ab7cbf8f1c725bda5c2b59`
- Date/author: 2026-09-03 / GarrySnail
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`, `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh`, `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh`, `python/sglang/kernels/ops/attention/qsa_indexer.py`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/kernels/ops/elementwise/fast_topk.py` 等 100 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - docs-bench: `benchmark/kernels/fused_moe_triton/common_utils.py`
  - other: `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/arg_groups/speculative_hook.py`; `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/utils.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/hc_mix_triton.py`; `python/sglang/srt/layers/hyperconnection.py`; `python/sglang/srt/layers/rotary_embedding/mrope_rope_index.py` 等 14 个文件
  - runtime-model: `python/sglang/srt/configs/__init__.py`; `python/sglang/srt/configs/model_config.py`; `python/sglang/srt/configs/qwen3_5.py`; `python/sglang/srt/configs/qwen4_exp.py`; `python/sglang/srt/configs/update_config.py`; `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`; `python/sglang/srt/model_executor/pool_configurator.py` 等 15 个文件
  - runtime-perf: `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`; `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`; `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh`; `python/sglang/kernels/jit/csrc/elementwise/hc_combine.cuh`; `python/sglang/kernels/ops/attention/qsa_indexer.py`; `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`; `python/sglang/kernels/ops/elementwise/fast_topk.py`; `python/sglang/kernels/ops/elementwise/hc_combine.py` 等 45 个文件
  - tests: `python/sglang/test/run_eval.py`; `python/sglang/test/simple_eval_aime25.py`; `python/sglang/test/simple_eval_aime26.py`; `test/hcu_humaneval_judge.py`; `test/registered/kernels/benchmark/attention/bench_qsa_indexer.py`; `test/registered/kernels/benchmark/elementwise/bench_fast_topk.py`; `test/registered/kernels/benchmark/elementwise/bench_hc_combine.py`; `test/registered/kernels/benchmark/layernorm/bench_grouped_gemma_rmsnorm.py` 等 25 个文件
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
