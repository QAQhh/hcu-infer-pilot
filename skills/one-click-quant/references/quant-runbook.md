# Quant runbook

Entry point: `python3 main.py`. Always check `python3 main.py --help` for current flags.

## Path selection

| Goal | Preferred path |
|------|----------------|
| BF16 → per-channel FP8 | `--scheme FP8_DYNAMIC` |
| BF16 → per-channel INT8 | `--scheme W8A8` |
| Block FP8 → BF16 | `--scheme FP8_TO_BF16` |
| DeepSeek-V3 block FP8 → channel INT8/FP8 | `--scheme DeepseekV3_FP8_TO_INT8` / `DeepseekV3_FP8_TO_FP8` |
| Kimi W4 → channel INT8/FP8 | `--scheme Kimi_W4_TO_INT8` / `Kimi_W4_TO_FP8` |
| Qwen3.5 MoE BF16 → INT8 | `--scheme Qwen35_MOE_BF16_TO_INT8` |
| Fast data-free PTQ | `--alg model_free_ptq` (+ scheme) |
| W4A8 / MoE INT4 pack (safetensors, no transformers) | `--alg slimquant_ptq --scheme W4A8` |
| Float preprocess then quant | `--alg preprocess` → then slimquant/model_free/… with `--from-preprocessed` |
| Huge MoE GPTQ on one machine | `utils/MoE-Quant/` (see its README) |
| Model-specific one-offs | `examples/<family>/` |

Custom schemes are resolved via `templates/quant_templates.yaml` (architecture + size signature). More schemes: compressed-tensors `quant_scheme` upstream.

## Minimal commands

Paths are user-supplied. If unknown, ask or use `$MODEL` — do not invent `/models/...` or scan the disk.

```bash
MODEL="<请替换为实际 HF 目录>"
SAVE="${SAVE:-${MODEL}-FP8_DYNAMIC}"

# Generic FP8
python3 main.py --model "$MODEL" --scheme FP8_DYNAMIC --save-dir "$SAVE"

# Generic INT8
python3 main.py --model "$MODEL" --scheme W8A8 --save-dir "${MODEL}-W8A8"

# Force algorithm (overrides scheme inference)
python3 main.py --model "$MODEL" --scheme W8A8 --alg model_free_ptq
python3 main.py --model "$MODEL" --scheme W8A8 --alg ptq

# SlimQuant W4A8
python3 main.py --model "$MODEL" --alg slimquant_ptq --scheme W4A8 --save-dir "${MODEL}-W4A8"

# Preprocess → quant (two-stage)
python3 main.py --alg preprocess \
  --model "$MODEL" --save-dir "${MODEL}-preprocessed" \
  --recipe preprocess/recipes/<model>.yaml \
  --transforms quarot,flex_awq_ssz,flex_smooth_quant \
  --preprocess-gpus 8

python3 main.py --alg slimquant_ptq --scheme W4A8 \
  --model "${MODEL}-preprocessed" --save-dir "${MODEL}-W4A8" \
  --from-preprocessed
```

Default save dir: next to the input model unless `--save-dir` is set.

## Useful overrides

| Flag | When |
|------|------|
| `--needs-data true\|false` | Force/skip calibration dataset |
| `--dataset` | Calib data (default `./datasets/ultrachat_200k`) |
| `--ignore` | Override ignore list (replaces defaults entirely) |
| `--pipeline sequential` + `--sequential-targets Linear` | Save VRAM (slower) |
| `--device-map cpu` / `auto_offload` | Save VRAM |
| `--offload-hessians` | Save VRAM during GPTQ-like paths |
| `--patch-for-llmc` | OOM on `save_pretrained` |
| `--print-model` | Dump structure after load |
| `torchrun --nproc_per_node=N main.py …` | Multi-GPU (llmcompressor; N=2/4 preferred for >100B) |

## slimquant notes

- Best for **INT4 / W4A8**; INT8/FP8 prefer generic scheme paths unless model is unsupported by transformers.
- MoE experts: INT4 + 2×int4→int8 pack; non-MoE often INT8 in W4A8 mode.
- Built-in ignore for known models; unmatched models default to `lm_head, re:.*mlp.gate$, re:.*embed_tokens.*`.

## PPL eval

```bash
# $SAVE = quantized dir from the previous step (real absolute path)
python3 main.py --lm-eval "pretrained=$SAVE,tensor_parallel_size=2,dtype=auto,gpu_memory_utilization=0.6"
```

OOM → lower `gpu_memory_utilization`, or vLLM server + `lm_eval --model local-completions`.

## Examples map

| Family | Dir |
|--------|-----|
| DeepSeek | `examples/deepseek/` |
| Qwen / Flash-Next | `examples/qwen/` |
| GLM | `examples/glm/` |
| Kimi | `examples/kimi/` |
| MiMo / MiniMax / Hy4 | `examples/mimo/`, `examples/minimax/`, `examples/hy4/` |
| Preprocess writeups | `examples/preprocess/` |
