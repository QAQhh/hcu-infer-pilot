---
name: model-pr-history-knowledge
description: Use when an SGLang, vLLM, or TensorRT-LLM serving/model optimization task needs local framework commit-history evidence. Query and read the local-repo history docs under model-pr-optimization-hg-history before choosing source paths, fast paths, kernel/fusion ideas, regression risks, or validation lanes.
---

# Model PR History Knowledge

This is a local commit-history knowledge base for model optimization history.
It is not a set of per-model skills. Each model family keeps bilingual docs
generated from the local `sglang` and `vllm` worktrees, including commit
coverage, timelines, changed files, implementation notes, and validation/risk
notes. Framework-wide commits that cannot be pinned to one model family should
go into the framework `shared/` bucket instead of being dropped.

The `sglang/` framework history is local-fork only. Do not store commits that
are reachable from the upstream GitHub repository
`sgl-project/sglang`. When rebuilding or updating SGLang history, compare
against local `refs/remotes/github-official/*` refs and keep only commits that
are not reachable from those refs. Missing official refs should be treated as a
blocker for SGLang history regeneration rather than silently mixing upstream
GitHub commits into this local knowledge base.

Use it before patching model-specific serving paths, choosing an SGLang SOTA
optimization target, or explaining why the local framework fork already has a
faster path.
When `llm-torch-profiler-analysis` is tracing a hot kernel or decode/prefill
gap, this tree is the local-commit evidence source to consult alongside the
open-source community PR history in `model-pr-optimization-history`.

## Query

Run commands from this directory:

```bash
python3 scripts/query.py --list
python3 scripts/query.py --framework sglang --model qwen3-core --paths-only
python3 scripts/query.py --framework sglang --model qwen3-core "fused qk norm rope"
python3 scripts/query.py --framework vllm "DeepSeek-V4 fused norm router" --limit 5
```

Useful options:

- `--framework sglang|vllm`: restrict to one serving framework.
- `--model <slug>`: restrict to one model family directory.
- `--lang en|zh|both`: select English, Chinese, or both docs.
- `--paths-only`: print the exact docs to read without snippets.
- `--limit N`: bound search results.

## Workflow

1. Infer the model-family slug from the user's model id, checkpoint path, or
   SGLang source path. If unsure, run `scripts/query.py "<model name>"`.
2. Read the matching SGLang history first for SGLang patch work. Read the vLLM
   history too when vLLM is the leading competitor or its trace suggests a
   missing SGLang fast path. If the trace points to a framework-wide runtime,
   parser, or utility gap, also check the framework `shared/` bucket.
3. For SGLang updates, enforce the local-only filter before writing docs:
   fetch or verify `refs/remotes/github-official/*` from
   `https://github.com/sgl-project/sglang.git`, remove commits reachable from
   those refs, and preserve only local fork commits.
4. Extract only actionable evidence:
   - model implementation files and symbols
   - local commits that changed the hot source path
   - prior fusions, overlap work, quantization, MoE, attention, cache, sampler,
     or loader changes
   - local fork changes that may explain a known gap or pending support issue
   - validation lanes and regression risks implied by the commit cards
5. Save a short note in the active run artifacts, for example
   `history/model-pr-history-notes.md`, with paths read, commit hashes, source
   files, and the decision each item influenced.
6. Do not copy long commit cards into the final answer. Cite paths and summarize the
   relevant implementation/risk.

## Model Slugs

Current frameworks:

- `sglang`
- `vllm`

Each framework also exposes a `shared` bucket for relevant local commits that
are real but not safely attributable to one model family.

Current model-family slugs include:

```text
deepseek-v3-r1, deepseek-v31, deepseek-v32, deepseek-v4, ernie45,
gemma4, glm-vlm-ocr, glm45, glm46-glm47, glm5-glm51, gpt-oss,
hunyuan3-preview, intern-s1, internvl35, kimi, llama4, mimo-v2-flash,
minimax, mistral-small-4, mixtral-quark-int4fp8-moe, moss-vl,
nemotron-super, qwen-vlm-omni-asr, qwen3-coder, qwen3-core,
qwen3-next, qwen35, qwen36, qwen4-exp, step35
```

`qwen4-exp` (Qwen3.8-Flash-Next, `qwen4_exp`) exists for `sglang` only. The
`sglang` tree also has an `unclassified` bucket for merge-only and bulk
sync/rename commits that cannot be tied to one model or to shared runtime
code; search it last.

Branch coverage of the `sglang` tree (details in `sglang/README.md`):

- `v0.5.8_dev` to `v0.5.12_dev`: `sglang/LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- `v0.5.12_dev` to `v0.5.15.post1_dev` to `release/20260825_v0.5.18`:
  `sglang/LOCAL_ONLY_COMMITS_v0.5.12_dev_to_v0.5.18_by_branch.md`

Each model doc holds one marker-delimited block per update; read the newest
block first.

## SOTA Loop Contract

For `sglang-sota-humanize-loop`, this knowledge base is an early context
source:

- Read it after model identification and before patch planning.
- Include the history paths and key local commit evidence in `analysis/root-cause.md` or
  `history/model-pr-history-notes.md`.
- If the profiler points at a known model path, check whether the local history
  has prior changes on that file before writing a new patch.
- If a competitor is faster, search both local history and open-source
  community PR history for the same model family and stage before assuming the
  gap is kernel-local.
