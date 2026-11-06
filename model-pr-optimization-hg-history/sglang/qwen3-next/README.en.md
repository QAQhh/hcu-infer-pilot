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

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_START -->
## Local-only branch update from v0.5.12_dev to release/20260825_v0.5.18

### Coverage Note

- Source repository: `HYGON-AI/sglang-das`; branch tips: `v0.5.12_dev`@`6c946e92f`, `v0.5.15.post1_dev`@`c8ba30447`, `release/20260825_v0.5.18`@`2c841655f`
- Scope: only local fork commits that are not reachable from `sgl-project/sglang` GitHub refs; merge commits are kept.
- Generated date: 2026-11-03
- Commits in this section: 1 (merges: 0)
- Branch segments: `v0.5.12_dev..v0.5.15.post1_dev`, `v0.5.15.post1_dev..release/20260825_v0.5.18`
- Classification note: commits matching a concrete model name or model file enter that model bucket (possibly several); other runtime, backend, CI and test commits enter `shared`; merge-only or no-relevant-path commits enter `unclassified`. Bulk sync/rename commits touching more than 150 files (e.g. squash syncs of official main) also enter only `unclassified`: they carry upstream code and are not local-only implementations. Auto-classified; diffs were not reviewed one by one.

### Touched Files

| File | Local commits |
| --- | --- |
| `test/registered/4-gpu-models/test_qwen3_next_models.py` | `e47388196` |
| `test/registered/attention/test_fa3.py` | `e47388196` |
| `test/registered/attention/test_local_attn.py` | `e47388196` |
| `test/registered/core/test_gpt_oss_1gpu.py` | `e47388196` |
| `test/registered/core/test_page_size.py` | `e47388196` |
| `test/registered/core/test_score_api.py` | `e47388196` |
| `test/registered/disaggregation/test_dp_attention_large.py` | `e47388196` |
| `test/registered/embedding/test_embedding_models.py` | `e47388196` |
| `test/registered/embedding/test_encoder_embedding_models.py` | `e47388196` |
| `test/registered/embedding/test_input_embeddings.py` | `e47388196` |
| `test/registered/embedding/test_openai_embedding.py` | `e47388196` |
| `test/registered/eval/test_eval_accuracy_large.py` | `e47388196` |
| `test/registered/eval/test_moe_eval_accuracy_large.py` | `e47388196` |
| `test/registered/lora/test_lora_backend.py` | `e47388196` |
| `test/registered/metrics/test_metrics.py` | `e47388196` |
| `test/registered/metrics/test_priority_metrics.py` | `e47388196` |
| `test/registered/mla/test_mla.py` | `e47388196` |
| `test/registered/mla/test_mla_deepseek_v3.py` | `e47388196` |
| `test/registered/models/test_cross_encoder_models.py` | `e47388196` |
| `test/registered/models/test_nvidia_nemotron_nano_v2.py` | `e47388196` |
| `test/registered/models/test_qwen_models.py` | `e47388196` |
| `test/registered/models/test_reward_models.py` | `e47388196` |
| `test/registered/openai_server/basic/test_protocol.py` | `e47388196` |
| `test/registered/openai_server/basic/test_serving_chat.py` | `e47388196` |
| `test/registered/openai_server/basic/test_serving_completions.py` | `e47388196` |
| `test/registered/openai_server/basic/test_serving_rerank.py` | `e47388196` |
| `test/registered/openai_server/features/test_enable_thinking.py` | `e47388196` |
| `test/registered/openai_server/features/test_reasoning_content.py` | `e47388196` |
| `test/registered/openai_server/function_call/test_tool_choice.py` | `e47388196` |
| `test/registered/ops/test_repeat_interleave.py` | `e47388196` |
| `test/registered/perf/test_bench_one_batch_1gpu.py` | `e47388196` |
| `test/registered/quant/test_bnb.py` | `e47388196` |
| `test/registered/quant/test_eval_fp8_accuracy.py` | `e47388196` |
| `test/registered/quant/test_torchao.py` | `e47388196` |
| `test/registered/quant/test_w4a8_deepseek_v3.py` | `e47388196` |
| `test/registered/rotary/test_mrope.py` | `e47388196` |
| `test/registered/scheduler/test_abort.py` | `e47388196` |
| `test/registered/scheduler/test_chunked_prefill.py` | `e47388196` |
| `test/registered/scheduler/test_no_chunked_prefill.py` | `e47388196` |
| `test/registered/scheduler/test_no_overlap_scheduler.py` | `e47388196` |
| ... | 4 more files omitted |

### Timeline

| Date | Commit | Branch update | Category | Title | Main files |
| --- | --- | --- | --- | --- | --- |
| 2026-08-06 | `e47388196` | `v0.5.12_dev..v0.5.15.post1_dev` | 性能/后端优化 | ci: migrate legacy CUDA suite= registrations to stage=/runner_config= | `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_local_attn.py` and 44 files in total |

### Per-Commit Audit Cards

#### Commit `e47388196` - ci: migrate legacy CUDA suite= registrations to stage=/runner_config=

- Full hash: `e473881969aef386533c0fb29ce8fd036a733560`
- Date/author: 2026-08-06 / RyeYuan
- Branch update: `v0.5.12_dev..v0.5.15.post1_dev`
- Auto category: 性能/后端优化
- Main files: `test/registered/4-gpu-models/test_qwen3_next_models.py`, `test/registered/attention/test_fa3.py`, `test/registered/attention/test_local_attn.py`, `test/registered/core/test_gpt_oss_1gpu.py`, `test/registered/core/test_page_size.py`, `test/registered/core/test_score_api.py`, `test/registered/disaggregation/test_dp_attention_large.py`, `test/registered/embedding/test_embedding_models.py` 等 44 个文件
- Implementation signal: This commit comes from a local dev branch update and is not in `sgl-project/sglang` GitHub refs; prioritize matched model files, performance backends, scheduling/cache, parser/tokenizer, and test coverage.
- Touched files (grouped by path, not read file by file):
  - tests: `test/registered/4-gpu-models/test_qwen3_next_models.py`; `test/registered/attention/test_fa3.py`; `test/registered/attention/test_local_attn.py`; `test/registered/core/test_gpt_oss_1gpu.py`; `test/registered/core/test_page_size.py`; `test/registered/core/test_score_api.py`; `test/registered/disaggregation/test_dp_attention_large.py`; `test/registered/embedding/test_embedding_models.py` 等 44 个文件
- Risk and verification: Includes test-related changes; rerun the matching tests plus a minimal model launch or generation smoke.

<!-- LOCAL_ONLY_BRANCH_UPDATE_V0_5_12_TO_V0_5_18_END -->
