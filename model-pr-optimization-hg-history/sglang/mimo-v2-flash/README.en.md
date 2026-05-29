# sglang MiMo V2 Flash Local Commit Optimization History

## Implementation File Coverage

| File | Local commits |
| --- | --- |
| `python/sglang/srt/models/mimo_v2_flash.py` | `1924c63d6` |

## Local Commit Coverage Summary

- Source worktree: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- Generated date: 2026-05-20
- Commits in this document: 3
- Auto-classification note: commits matching model files or model names enter the model bucket; runtime, backend, scheduler, cache, CI, and test commits that cannot be pinned to one model family enter the framework `shared/` bucket.
- Trace command: `git log --name-only`
- Filter note: commits reachable from `sgl-project/sglang` GitHub refs were removed; this document keeps only local fork commits.

## Timeline

| Date | Commit | Category | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-05-14 | `1924c63d6` | 性能/后端优化 | [BUG FIX] fix pp parallel bug for mimo model | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py` |
| 2026-04-14 | `47165f0fc` | 性能/后端优化 | [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash) | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-04-03 | `30f4f1133` | 性能/后端优化 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` |

## Per-Commit Audit Cards

### Commit `1924c63d6` - [BUG FIX] fix pp parallel bug for mimo model

- Full hash: `1924c63d64f72fbbb4623956150b176dcdcde29c`
- Date/author: 2026-05-14 / shiqiang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/models/mimo_v2_flash.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `47165f0fc` - [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash)

- Full hash: `47165f0fcf27c6d38edd4d230d750311f98ba387`
- Date/author: 2026-04-14 / ShiQiang Dai
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/managers/scheduler.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

### Commit `30f4f1133` - support mimo-v2-flash-int4 with triton attn

- Full hash: `30f4f1133f9a4d57d8cd3b971230048e0cf15b04`
- Date/author: 2026-04-03 / shiqiang
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- Implementation signal: This commit comes from local framework `git log --name-only`; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## Local-only dev branch update from v0.5.8_dev to v0.5.12_dev

### Coverage Note

- Source index: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- Source worktree: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs.
- Commits in this section: 2
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-04-03 | `968d82d7f` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` 等 4 个文件 |
| 2026-04-03 | `b4a02fae7` | `v0.5.9_dev..v0.5.10_dev` | 模型支持/运行时入口 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` 等 4 个文件 |

### Per-Commit Audit Cards

#### Commit `968d82d7f` - support mimo-v2-flash-int4 with triton attn

- Full hash: `968d82d7f8205f78236c345136a7cbf363f8fd9d`
- Date/author: 2026-04-03 / shiqiang
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- Duplicate/note: 重复 patch-id: 与 v0.5.9_dev..v0.5.10_dev 的 b4a02fae7 相同
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

#### Commit `b4a02fae7` - support mimo-v2-flash-int4 with triton attn

- Full hash: `b4a02fae7e09fe663276907645cb77af61c25198`
- Date/author: 2026-04-03 / shiqiang
- Branch update: `v0.5.9_dev..v0.5.10_dev`
- Auto category: 模型支持/运行时入口
- Main files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- Duplicate/note: 重复 patch-id: 与 v0.5.8_dev..v0.5.9_dev 的 968d82d7 相同
- Risk and verification: Touches model entry or runtime adaptation; main risks are weight loading, parallel partitioning, quant config, and short-generation correctness.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
