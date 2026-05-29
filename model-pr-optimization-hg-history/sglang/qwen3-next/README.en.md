# sglang Qwen3 Next Local Commit Optimization History

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

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## Local-only dev branch update from v0.5.8_dev to v0.5.12_dev

### Coverage Note

- Source index: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- Source worktree: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs.
- Commits in this section: 1
- Classification note: commits matching a concrete model name, model file, or model-family signal enter that model bucket; runtime, backend, CI, merge/base, PD/cache, and generic quantization commits that cannot be pinned to one model family enter `shared`.

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-03-13 | `446841129` | `v0.5.8_dev..v0.5.9_dev` | 调度/缓存/PD | 支持qwen3-next在fa3后端时打开radix cache | `python/sglang/srt/server_args.py` |

### Per-Commit Audit Cards

#### Commit `446841129` - 支持qwen3-next在fa3后端时打开radix cache

- Full hash: `4468411292399a06690dbbc2dc39d5b61a0ce2c5`
- Date/author: 2026-03-13 / niuhb
- Branch update: `v0.5.8_dev..v0.5.9_dev`
- Auto category: 调度/缓存/PD
- Main files: `python/sglang/srt/server_args.py`
- Implementation signal: This commit comes from a local dev branch update and is not reachable from `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Reviewed files:
  - runtime-model: `python/sglang/srt/server_args.py`
- Risk and verification: Touches scheduling, cache, PD, or MTP paths; verify prefill/decode ordering, first-token correctness, concurrency, and long-context stability.

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
