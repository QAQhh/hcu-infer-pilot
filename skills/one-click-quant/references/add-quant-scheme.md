# Add a quantization scheme / template

Three integration levels (prefer the lightest that works):

1. **YAML ignore only** — model already works via llmcompressor; add ignore in `templates/quant_templates.yaml`.
2. **Custom template script** — non-generic path; put code under `templates/` and point `template:` in YAML.
3. **examples/** — standalone script + README; good for experiments before promoting to templates.

## `quant_templates.yaml` match rules

File: `templates/quant_templates.yaml`.

- Top-level key = HF `architectures` name (e.g. `DeepseekV3ForCausalLM`), or `"*"` for any arch.
- Entries matched by `(hidden_size, num_hidden_layers)`; use `-1` as wildcard.
- Per-scheme fields:
  - `template`: path to Python under `templates/` (optional)
  - `ignore`: comma-separated names/regex (optional)
  - `quant_type`: hint for shared templates (optional)
- Ignore priority: **CLI `--ignore` > YAML `ignore` > llmc defaults**.

Example pattern:

```yaml
MyArchForCausalLM:
  - hidden_size: -1
    num_hidden_layers: -1
    schemes:
      MyScheme_NAME:
        template: "templates/my_scheme.py"
        quant_type: "int8"
      FP8_DYNAMIC:
        ignore: "lm_head,re:.*mlp.gate$"
```

After adding a named scheme, expose it in `main.py` `--scheme` help text if it should be user-facing.

## Template script conventions

- Place under `templates/`; reuse existing scripts when possible (`fp8_to_bf16.py`, `w8a8_block_cast_channel.py`, `w4_dequant_channel.py`, `slimquant_ptq.py`, …).
- New scripts should accept the same args style as peer templates (argparse / called from oneshot path).
- File header for first-party code:

```text
# Copyright (c) 2026 Hygon Information Technology Co., Ltd.
# SPDX-License-Identifier: Apache-2.0
```

## Force alg without new scheme

If only the algorithm differs, use existing scheme + `--alg`:

```bash
python3 main.py --model /models/xxx --scheme W8A8 --alg model_free_ptq
python3 main.py --model /models/xxx --alg slimquant_ptq --scheme W4A8
```

## PR-oriented checklist

```text
- [ ] Working command documented (README or examples/<model>/README.md)
- [ ] quant_templates.yaml entry OR templates/*.py wired
- [ ] --scheme help updated if new public scheme name
- [ ] Smoke on mini/build_mini model if available
```

See README「提交PR」and existing entries for DeepSeek / Kimi / Qwen3.5 MoE.
