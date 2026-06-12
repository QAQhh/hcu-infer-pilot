# SGLang Local Commit Optimization History

Filter policy:

- SGLang bucket docs keep only local fork commits that are not reachable from local `refs/remotes/github-official/*`, fetched from `sgl-project/sglang`.
- Buckets with no remaining local-only commits keep an explicit empty result row instead of preserving GitHub upstream commits.

Current buckets:

- `AITER_LOCAL_COMMITS.md` - local-only AITER PR/commit index with source SGLang branch/update provenance
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
- `step35`
- `shared`
