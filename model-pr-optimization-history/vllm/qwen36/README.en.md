# vllm Qwen3.6 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/evals/gsm8k/configs/humming/Qwen3.6-35B-A3B-NVFP4-humming.yaml` | no direct PR-number commit |
| `tests/lora/test_qwen36_moe_lora.py` | no direct PR-number commit |

## PR Coverage Summary

- Git-traced PRs: 0
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 0

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| - | - | - | no archived PR found | - |

## Per-PR Diff Audit Cards

### Public PR search conclusion

- Conclusion: No public PR was confirmed as part of the vllm Qwen3.6 model support or optimization line.
- Search method: `git log --name-only -- <model-files>` was run on the matched files, and explicit PR links in the previous history/skill were checked.
- Covered files: `tests/evals/gsm8k/configs/humming/Qwen3.6-35B-A3B-NVFP4-humming.yaml`; `tests/lora/test_qwen36_moe_lora.py`
- Acceptance rule: if implementation files or PRs appear later, add the same per-PR diff card format.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
