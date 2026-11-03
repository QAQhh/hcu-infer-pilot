# sglang GLM-4.6/4.7 Local Commit Optimization History

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
- Commits in this section: 2 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/glm4_moe.py` | `1e2fec228`, `3604cec31` |
| `python/sglang/check_env.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/attn.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/elementwise.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/gemm.py` | `1e2fec228` |
| `python/sglang/jit_kernel/dsv4/moe.py` | `1e2fec228` |
| `python/sglang/jit_kernel/fp8_blockwise_gemm.py` | `1e2fec228` |
| `python/sglang/jit_kernel/include/sgl_kernel/tensor.h` | `1e2fec228` |
| `python/sglang/jit_kernel/mxfp8.py` | `1e2fec228` |
| `python/sglang/jit_kernel/sparse_mla_q8kv8_prefill_sm90.py` | `1e2fec228` |
| `python/sglang/jit_kernel/trtllm_lora_temp/jit.py` | `1e2fec228` |
| `python/sglang/kernels/ops/layernorm/mhc.py` | `1e2fec228` |
| `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` | `1e2fec228` |
| `python/sglang/kernels/ops/quantization/fp8_kernel.py` | `1e2fec228` |
| `python/sglang/kernels/ops/speculative/cache_locs.py` | `1e2fec228` |
| `python/sglang/multimodal_gen/csrc/render/hunyuan3d_rasterizer/__init__.py` | `1e2fec228` |
| `python/sglang/multimodal_gen/runtime/layers/attention/backends/rocm_sparse_linear_attn.py` | `1e2fec228` |
| `python/sglang/multimodal_gen/test/unit/test_rocm_sparse_linear_attn.py` | `1e2fec228` |
| `python/sglang/srt/arg_groups/overrides.py` | `1e2fec228` |
| `python/sglang/srt/batch_overlap/single_batch_overlap.py` | `1e2fec228` |
| `python/sglang/srt/disaggregation/mooncake/conn.py` | `1e2fec228` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` | `1e2fec228` |
| `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py` | `1e2fec228` |
| `python/sglang/srt/distributed/parallel_state.py` | `1e2fec228` |
| `python/sglang/srt/environ.py` | `1e2fec228` |
| `python/sglang/srt/layers/activation.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/aiter_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/attention_registry.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/deepseek_v4_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/index_buf_accessor.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/tilelang_kernel.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa/triton_kernel.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsa_backend.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsv4/compressor.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsv4/indexer.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/dsv4/metadata.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/fla/chunk_delta_h.py` | `1e2fec228` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `1e2fec228` |
| ... | 70 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-20 | `1e2fec228` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | feat(hcu): port runtime and kernel rename | `python/sglang/check_env.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` and 109 files in total |
| 2026-10-13 | `3604cec31` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | fix(hcu): 修复 GLM W4A8 target 的 BF16 MTP 加载与 DeepEP 通信 (#520) | `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/glm4_moe.py` |

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

#### Commit `3604cec31` - fix(hcu): 修复 GLM W4A8 target 的 BF16 MTP 加载与 DeepEP 通信 (#520)

- Full hash: `3604cec316cca9c1b9fb8da2e5d1a5a7d59e92a2`
- Date/author: 2026-10-13 / maxiaobetter
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/glm4_moe.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`; `python/sglang/srt/models/glm4_moe.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
