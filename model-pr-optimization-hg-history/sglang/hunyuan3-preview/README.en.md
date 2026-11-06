# sglang Hunyuan3 Preview Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| - | no local-only commit |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 0
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| - | - | - | no local-only commit found | - |

## Per-Commit Audit Cards

### Local commit search conclusion

- Commits reachable from `sgl-project/sglang` GitHub refs were removed; no local-only commit remains in the baseline history.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 10 (merges: 1)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/hunyuan_v3.py` | `1e2fec228`, `123e9539e`, `32f86c628`, `aa89102b1`, `c2544d8ae`, `a12f08de7`, `f2379b09c` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `1e2fec228`, `a12f08de7`, `f2379b09c` |
| `python/sglang/srt/model_executor/forward_batch_info.py` | `1e2fec228`, `123e9539e`, `a12f08de7` |
| `python/sglang/srt/server_args.py` | `1e2fec228`, `123e9539e`, `a12f08de7` |
| `python/sglang/check_env.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/disaggregation/decode.py` | `123e9539e`, `f2379b09c` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `1e2fec228`, `a12f08de7` |
| `python/sglang/srt/disaggregation/prefill.py` | `123e9539e`, `f2379b09c` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/environ.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/layernorm.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/ep_moe/layer.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/moe/topk.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/fp8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/fp8_utils.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/moe_wna16.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/mxfp4.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_fp8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/layers/quantization/w8a8_int8.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/model_executor/model_runner.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/bailing_moe.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_common/utils.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/deepseek_v4.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/mimo_v2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/minimax_m2.py` | `1e2fec228`, `123e9539e` |
| `python/sglang/srt/models/qwen2.py` | `1e2fec228`, `123e9539e` |
| ... | 124 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` and 109 files in total |
| 2026-07-31 | `123e9539e` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | fix lint: satisfy pre-commit on the forward-port diff | `python/sglang/check_env.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/common.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh` and 91 files in total |
| 2026-08-26 | `32f86c628` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hy3): align LightOp routed scaling factor handling | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-08-26 | `c063dda9a` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | Merge pull request #234 from liuzj512/fix/hy3-lightop-rsf | no direct file change / merge |
| 2026-09-03 | `aa89102b1` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hy3): align MoE forward context with current API (#292) | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-09-04 | `c2544d8ae` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 缺陷修复 | fix(hcu): repair two upstream-refactor call-site regressions (#303) | `python/sglang/srt/models/hunyuan_v3.py` |
| 2026-09-07 | `a12f08de7` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Hy3 support sp ep (#311) | `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` and 9 files in total |
| 2026-09-14 | `feff664df` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | Hy3 sp ep lightop clean (#355) | `python/sglang/srt/layers/moe/utils.py` |
| 2026-09-14 | `f2379b09c` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | feat:Hy3 support sp ep (#360) | `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` and 5 files in total |
| 2026-11-03 | `2c841655f` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): limit INT8 marlin MoE bypass to DeepSeek so HY3 keeps lightop (#639) | `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py` |

### Per-Commit Audit Cards

#### Commit `1e2fec228` - feat(hcu): port runtime and kernel rename

- Full hash: `1e2fec228a9a8b1e781c3592eff356eeb8b584ed`
- Date/author: 2026-07-20 / tianlinyang77
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/jit_kernel/dsv4/moe.py`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`, `python/sglang/jit_kernel/mxfp8.py` 等 109 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/check_env.py`; `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py`; `python/sglang/srt/arg_groups/overrides.py`; `python/sglang/srt/batch_overlap/single_batch_overlap.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/environ.py`; `python/sglang/srt/layers/activation.py`; `python/sglang/srt/layers/layernorm.py` 等 13 个文件
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/model_executor/model_runner.py`; `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`; `python/sglang/srt/models/deepseek_common/utils.py`; `python/sglang/srt/models/deepseek_v2.py`; `python/sglang/srt/models/deepseek_v4.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/models/mimo_v2.py` 等 14 个文件
  - runtime-perf: `python/sglang/jit_kernel/dsv4/attn.py`; `python/sglang/jit_kernel/dsv4/elementwise.py`; `python/sglang/jit_kernel/dsv4/gemm.py`; `python/sglang/jit_kernel/dsv4/moe.py`; `python/sglang/jit_kernel/fp8_blockwise_gemm.py`; `python/sglang/jit_kernel/include/sgl_kernel/tensor.h`; `python/sglang/jit_kernel/mxfp8.py`; `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` 等 80 个文件
  - tests: `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py`; `sgl-kernel/tests/test_moe_align.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

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

#### Commit `32f86c628` - fix(hy3): align LightOp routed scaling factor handling

- Full hash: `32f86c628bcd8baebe8eb2b2a6a0b3924c73f566`
- Date/author: 2026-08-26 / liuzj512
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/hunyuan_v3.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `c063dda9a` - Merge pull request #234 from liuzj512/fix/hy3-lightop-rsf

- Full hash: `c063dda9a0f7dfdcab84c15cd7c1baa27cb860e9`
- Date/author: 2026-08-26 / lizhigong
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: no direct file change / merge
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Risk and verification: A merge commit has no direct file diff; the substance is in the commits it brings in.

#### Commit `aa89102b1` - fix(hy3): align MoE forward context with current API (#292)

- Full hash: `aa89102b1dacca122aec18d43547cb86e979d217`
- Date/author: 2026-09-03 / liuzj512
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/models/hunyuan_v3.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `c2544d8ae` - fix(hcu): repair two upstream-refactor call-site regressions (#303)

- Full hash: `c2544d8ae1a60d2b91ba275ed997bf1da4e1e833`
- Date/author: 2026-09-04 / Jane
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 缺陷修复
- Main files: `python/sglang/srt/models/hunyuan_v3.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
- Risk and verification: Touches model runtime entry points; risk is weight loading, parallel sharding, parser/tokenizer behavior, and short-generation correctness.

#### Commit `a12f08de7` - Hy3 support sp ep (#311)

- Full hash: `a12f08de78065aa75f5fefa6e6c17c738d022e53`
- Date/author: 2026-09-07 / Jane
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/hunyuan_v3.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/common.py` 等 9 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/common/conn.py`; `python/sglang/srt/disaggregation/fake/conn.py`; `python/sglang/srt/disaggregation/mooncake/conn.py`; `python/sglang/srt/utils/common.py`
  - runtime-model: `python/sglang/srt/model_executor/forward_batch_info.py`; `python/sglang/srt/models/hunyuan_v3.py`; `python/sglang/srt/server_args.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
  - tests: `test/registered/unit/models/test_hunyuan_v3_sp.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `feff664df` - Hy3 sp ep lightop clean (#355)

- Full hash: `feff664dfee687c0238ee95f5980467334093f29`
- Date/author: 2026-09-14 / liuzj512
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/utils.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f2379b09c` - feat:Hy3 support sp ep (#360)

- Full hash: `f2379b09c820f2ad5e9217af1c8a21a20b7b3d73`
- Date/author: 2026-09-14 / Jane
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/hunyuan_v3.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/disaggregation/decode.py`; `python/sglang/srt/disaggregation/prefill.py`; `python/sglang/srt/disaggregation/utils.py`
  - runtime-model: `python/sglang/srt/models/hunyuan_v3.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `2c841655f` - fix(hcu): limit INT8 marlin MoE bypass to DeepSeek so HY3 keeps lightop (#639)

- Full hash: `2c841655fe7852cde42eaaff2c1d414cf4038df1`
- Date/author: 2026-11-03 / lipenghui
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_marlin.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
