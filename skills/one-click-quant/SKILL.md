---
name: one-click-quant
description: >-
  Guides quantization, preprocess (QuaRot/Flex), scheme/template extension, and
  precision debugging in the one-click-quant repo. Use when working with
  main.py, --scheme, --alg, slimquant_ptq, model_free_ptq, preprocess recipes,
  adapters, quant_templates.yaml, MoE-Quant, PPL/lm_eval, or precision-tuning.
---

# one-click-quant

Repo-local runbook for Hygon one-click quantization. Prefer these references over inventing new flows. Read `python3 main.py --help` when flags are unclear.

## Decision tree

1. **Environment / dataset / Docker** → [references/env-docker.md](references/env-docker.md)
2. **Run or choose a quant path** (scheme, alg, slimquant, examples) → [references/quant-runbook.md](references/quant-runbook.md)
3. **Add preprocess for a new model** (adapter + recipe) → [references/preprocess-new-model.md](references/preprocess-new-model.md)
4. **Add or wire a `--scheme` / template** → [references/add-quant-scheme.md](references/add-quant-scheme.md)
5. **PPL bad / ignore / analysis** → [references/precision-debug.md](references/precision-debug.md)

## Hard rules

- Preprocess and quant are **decoupled**: preprocess writes float BF16/FP16 HF dir; then run any quant alg on that dir (prefer `--from-preprocessed`).
- New preprocess model = **new** `preprocess/adapters/<model>.py` **and** `preprocess/recipes/<model>.yaml` + register in `ADAPTER_REGISTRY`. Do **not** reuse another model's recipe.
- Do **not** change absorb / pipeline / transform core for a new model unless fixing a shared bug.
- Scheme routing lives in `templates/quant_templates.yaml` (arch + `hidden_size`/`num_hidden_layers` signature).
- Prefer existing `examples/<model>/` scripts as ground truth for model-specific commands.
- Container/Docker issues are **not** one-size-fits-all: diagnose the actual error (image/tag/ID, GPU, shm, mount, network, missing deps), ask the user when the image or host layout is unknown, then fix that case. See [references/env-docker.md](references/env-docker.md); do not blindly re-run a canned `docker run`.
- **Model paths**: do not invent or scan the filesystem for checkpoints. If the user did not give an absolute HF dir, ask once and/or use:
  ```bash
  MODEL="<请替换为实际 HF 目录>"
  python3 main.py --model "$MODEL" --scheme ...
  ```
  Same for `--save-dir`, `--dataset`, `lm-eval pretrained=`.

## Quick validate

```bash
# Recipe YAML sanity (adapter registered, transforms known, include present)
python3 .cursor/skills/one-click-quant/scripts/check_recipe.py preprocess/recipes/deepseek_v3.yaml
```

## Canonical docs in repo

Paths relative to repository root:

- `README.md` — CLI overview
- `docs/preprocess.md` — preprocess architecture
- `docs/precision-tuning.md` — analysis modes
- `utils/MoE-Quant/README.md` — large MoE GPTQ
