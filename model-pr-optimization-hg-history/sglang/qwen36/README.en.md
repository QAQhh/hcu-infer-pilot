# sglang Qwen3.6 Local Commit Optimization History

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
- Commits in this section: 8 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `python/sglang/srt/layers/attention/flashattention_interface.py` | `700649f36`, `4603df038`, `050129f5b`, `f4d13c6b8`, `b290dcf39` |
| `.github/workflows/nightly-test-hcu.yml` | `9b86479ac`, `5d0386fd4` |
| `python/sglang/srt/layers/attention/flashattention_backend.py` | `700649f36`, `b290dcf39` |
| `python/sglang/srt/models/dspark.py` | `4603df038`, `050129f5b` |
| `python/sglang/srt/speculative/dflash_utils.py` | `4603df038`, `050129f5b` |
| `python/sglang/srt/utils/hf_transformers/config.py` | `4603df038`, `050129f5b` |
| `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py` | `5d0386fd4`, `b86a8dc74` |
| `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py` | `5d0386fd4`, `b86a8dc74` |
| `test/run_suite.py` | `9b86479ac`, `5d0386fd4` |
| `.github/workflows/pr-test-hcu.yml` | `5d0386fd4` |
| `.gitignore` | `9b86479ac` |
| `THIRD_PARTY_NOTICES.md` | `9b86479ac` |
| `python/sglang/kernels/ops/speculative/dflash.py` | `b290dcf39` |
| `python/sglang/srt/configs/dspark.py` | `4603df038` |
| `python/sglang/srt/environ.py` | `050129f5b` |
| `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` | `700649f36` |
| `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py` | `f4d13c6b8` |
| `python/sglang/srt/layers/quantization/unquant.py` | `700649f36` |
| `python/sglang/srt/mem_cache/memory_pool.py` | `b290dcf39` |
| `python/sglang/srt/models/dflash.py` | `700649f36` |
| `python/sglang/srt/speculative/dflash_worker_v2.py` | `b290dcf39` |
| `python/sglang/srt/speculative/dspark_components/dspark_config.py` | `050129f5b` |
| `python/sglang/test/hcu_cookbook_utils.py` | `9b86479ac` |
| `python/sglang/test/hcu_reasoning_code_utils.py` | `9b86479ac` |
| `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh` | `9b86479ac` |
| `scripts/ci/hcu/hcu_ci_judge_humaneval.sh` | `9b86479ac` |
| `test/hcu_humaneval_judge.py` | `9b86479ac` |
| `test/manual/test_hcu_dflash_native_block16.py` | `f4d13c6b8` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen35_397b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen36_35b_a3b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_30b_a3b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_32b_hcu.py` | `9b86479ac` |
| `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/infra/test_hcu_server_guard_failures_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/kernels/test_attention_reference_hcu.py` | `5d0386fd4` |
| `test/registered/hcu/kernels/test_fp8_quant_reference_hcu.py` | `5d0386fd4` |
| ... | 4 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-07-21 | `9b86479ac` | `v0.5.12_dev..v0.5.15.post1_dev` | 模型支持/运行时入口 | test(hcu): add MATH-500 and HumanEval nightly coverage | `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md` and 14 files in total |
| 2026-08-06 | `5d0386fd4` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci(hcu): expand functional and numerical coverage | `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py` and 16 files in total |
| 2026-08-07 | `b86a8dc74` | `v0.5.12_dev..v0.5.15.post1_dev` | 调度/缓存/PD | test(hcu): bound backend smoke test setup | `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py` |
| 2026-09-08 | `700649f36` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | 【Feat】Qwen3.6‑35B‑A3B supported dflash2 (#331) | `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py` and 5 files in total |
| 2026-09-11 | `4603df038` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat]Qwen3.6-35B-A3B 支持--speculative-algorithm DSPARK (#341) | `python/sglang/srt/configs/dspark.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` and 5 files in total |
| 2026-09-12 | `050129f5b` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [bugfix] Isolate the use of --speculative-algorithm DSPARK for the Qwen3.6-35B-A3B model family via the SGLANG_USE_QWEN_DSPARK environment variable. (#352) | `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py` and 6 files in total |
| 2026-09-17 | `f4d13c6b8` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [Feat]Qwen3.6-35B-A3B DFLASH性能优化 (#388) | `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/manual/test_hcu_dflash_native_block16.py` |
| 2026-10-13 | `b290dcf39` | `v0.5.15.post1_dev..release/20260825_v0.5.18` | 性能/后端优化 | [feat] 优化 HCU 上 Qwen3.6-35B-A3B 使用 DFLASH 时（--speculative-algorithm DFLASH）的性能 (#522) | `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py` and 5 files in total |

### Per-Commit Audit Cards

#### Commit `9b86479ac` - test(hcu): add MATH-500 and HumanEval nightly coverage

- Full hash: `9b86479ac4f933649d4f777d1ffb92bfbfc375ab`
- Date/author: 2026-07-21 / tianlinyang77
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 模型支持/运行时入口
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.gitignore`, `THIRD_PARTY_NOTICES.md`, `python/sglang/test/hcu_cookbook_utils.py`, `python/sglang/test/hcu_reasoning_code_utils.py`, `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`, `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`, `test/hcu_humaneval_judge.py` 等 14 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`
  - other: `.gitignore`; `THIRD_PARTY_NOTICES.md`; `scripts/ci/hcu/hcu_ci_install_reasoning_code_deps.sh`; `scripts/ci/hcu/hcu_ci_judge_humaneval.sh`
  - tests: `python/sglang/test/hcu_cookbook_utils.py`; `python/sglang/test/hcu_reasoning_code_utils.py`; `test/hcu_humaneval_judge.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen35_397b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen36_35b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_30b_a3b_hcu.py`; `test/registered/hcu/accuracy/bw1100/test_reasoning_code_qwen3_32b_hcu.py`; `test/run_suite.py` 等 9 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `5d0386fd4` - ci(hcu): expand functional and numerical coverage

- Full hash: `5d0386fd4cfda35ce75a6519dd6008fac8d2dcc9`
- Date/author: 2026-08-06 / LvJIA-RG
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `.github/workflows/nightly-test-hcu.yml`, `.github/workflows/pr-test-hcu.yml`, `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`, `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py`, `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py`, `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`, `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py` 等 16 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - ci: `.github/workflows/nightly-test-hcu.yml`; `.github/workflows/pr-test-hcu.yml`
  - tests: `test/registered/hcu/backends/bw1100/test_torch_compile_cuda_graph_hcu.py`; `test/registered/hcu/distributed/bw1100/test_collectives_reference_hcu.py`; `test/registered/hcu/distributed/bw1100/test_dp_attention_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/distributed/bw1100/test_pp_consistency_hcu.py`; `test/registered/hcu/distributed/bw1100/test_tp_dp_consistency_hcu.py`; `test/registered/hcu/infra/test_hcu_server_guard_failures_hcu.py`; `test/registered/hcu/kernels/test_attention_reference_hcu.py` 等 14 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `b86a8dc74` - test(hcu): bound backend smoke test setup

- Full hash: `b86a8dc74ff9d3a2f535122c85966923e04f5037`
- Date/author: 2026-08-07 / LvJIA-RG
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 调度/缓存/PD
- Main files: `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`, `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `test/registered/hcu/distributed/bw1100/test_hicache_pp_hcu.py`; `test/registered/hcu/spec/bw1100/test_qwen36_nextn_consistency_hcu.py`
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

#### Commit `700649f36` - 【Feat】Qwen3.6‑35B‑A3B supported dflash2 (#331)

- Full hash: `700649f36306ad88b7322362f3262154b7b3adff`
- Date/author: 2026-09-08 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/dflash.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/attention/triton_vllm_flash_attn.py`; `python/sglang/srt/layers/quantization/unquant.py`; `python/sglang/srt/models/dflash.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `4603df038` - [feat]Qwen3.6-35B-A3B 支持--speculative-algorithm DSPARK (#341)

- Full hash: `4603df038bccfa86a42db00202c1cd25c8d6529b`
- Date/author: 2026-09-11 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/configs/dspark.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/utils/hf_transformers/config.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-model: `python/sglang/srt/configs/dspark.py`; `python/sglang/srt/models/dspark.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/speculative/dflash_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `050129f5b` - [bugfix] Isolate the use of --speculative-algorithm DSPARK for the Qwen3.6-35B-A3B model family via the SGLANG_USE_QWEN_DSPARK environment variable. (#352)

- Full hash: `050129f5b3406b3b003378dccd3009433df76d7a`
- Date/author: 2026-09-12 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dspark_components/dspark_config.py`, `python/sglang/srt/utils/hf_transformers/config.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - other: `python/sglang/srt/environ.py`
  - runtime-model: `python/sglang/srt/models/dspark.py`; `python/sglang/srt/speculative/dspark_components/dspark_config.py`; `python/sglang/srt/utils/hf_transformers/config.py`
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/speculative/dflash_utils.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `f4d13c6b8` - [Feat]Qwen3.6-35B-A3B DFLASH性能优化 (#388)

- Full hash: `f4d13c6b88c6a3494b1036d62de54f6849d73eed`
- Date/author: 2026-09-17 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/manual/test_hcu_dflash_native_block16.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`
  - tests: `test/manual/test_hcu_dflash_native_block16.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

#### Commit `b290dcf39` - [feat] 优化 HCU 上 Qwen3.6-35B-A3B 使用 DFLASH 时（--speculative-algorithm DFLASH）的性能 (#522)

- Full hash: `b290dcf39562e7ae6ed5f1646bbd20d1e1d8c7fc`
- Date/author: 2026-10-13 / chenyuege
- Branch update: `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Auto category: 性能/后端优化
- Main files: `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_interface.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - runtime-perf: `python/sglang/kernels/ops/speculative/dflash.py`; `python/sglang/srt/layers/attention/flashattention_backend.py`; `python/sglang/srt/layers/attention/flashattention_interface.py`; `python/sglang/srt/mem_cache/memory_pool.py`; `python/sglang/srt/speculative/dflash_worker_v2.py`
- Risk and verification: Touches performance or backend paths; validate the idea with prefill/decode trace evidence, throughput, and correctness smoke tests.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_START -->
## Local-only branch update from release/20260825_v0.5.18 to release_v0.5.18_deepseekv4

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `release/20260825_v0.5.18`@`2c841655f`, `main`@`5343b311c`, `release/20261023_v0.5.18_welm`@`962617b2d`, `release_v0.5.18_deepseekv4`@`c66f34363`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-05
- Commits in this section: 0 (merges: 0)
- Branch segments: `release/20260825_v0.5.18..main`, `release/20260825_v0.5.18..release/20261023_v0.5.18_welm`, `release/20260825_v0.5.18..release_v0.5.18_deepseekv4`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

- No local-only commit in these branch segments belongs to this bucket.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_18_TO_20261105_END -->
