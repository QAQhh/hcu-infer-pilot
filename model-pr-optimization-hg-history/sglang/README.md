# SGLang Local Commit Optimization History

Filter policy:

- SGLang bucket docs keep only local fork commits that are not reachable from local `refs/remotes/github-official/*`, fetched from `sgl-project/sglang`.
- Buckets with no remaining local-only commits keep an explicit empty result row instead of preserving GitHub upstream commits.

Current buckets:

- `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md` - local-only commit index for `v0.5.8_dev..v0.5.12_dev`
- `LOCAL_ONLY_COMMITS_v0.5.12_dev_to_v0.5.18_by_branch.md` - local-only commit index for `v0.5.12_dev..v0.5.15.post1_dev..release/20260825_v0.5.18`, generated from `HYGON-AI/sglang-das` by `tools/append_hg_history_branch_segments.py`
- `AITER_LOCAL_COMMITS.md` - local-only AITER PR/commit index with source SGLang branch/update provenance (not tracked in this repository)
- `deepseek-v3-r1`
- `deepseek-v31`
- `deepseek-v32`
- `deepseek-v4`
- `ernie45`
- `gemma4`
- `glm-vlm-ocr`
- `glm45`
- `glm46-glm47`
- `glm5-glm51`
- `gpt-oss`
- `hunyuan3-preview`
- `intern-s1`
- `internvl35`
- `kimi`
- `llama4`
- `mimo-v2-flash`
- `minimax`
- `mistral-small-4`
- `mixtral-quark-int4fp8-moe`
- `moss-vl`
- `nemotron-super`
- `qwen-vlm-omni-asr`
- `qwen3-coder`
- `qwen3-core`
- `qwen3-next`
- `qwen35`
- `qwen36`
- `qwen4-exp`
- `step35`
- `shared`
- `unclassified`
