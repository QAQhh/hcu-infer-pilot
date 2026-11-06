# Precision debug

Canonical detail: `docs/precision-tuning.md` (repo root). Analysis is early-stage; treat rankings as candidates to test via `--ignore`, not ground truth.

## Fast→slow ladder

Calib + SmoothQuant/GPTQ is expensive. Prefer short loops first:

1. `--alg model_free_ptq` (no transformers load, no calib) — fastest baseline  
2. `--alg ptq`  
3. Default scheme path / SmoothQuant+GPTQ family  
4. Try newer `llmcompressor` main if a known release pair is broken  
5. Layer ignore via `--analysis` recommendations  

```bash
python3 main.py --model /models/xxx --scheme W8A8 --alg model_free_ptq
python3 main.py --model /models/xxx --scheme W8A8 --alg ptq
```

## Measure PPL

```bash
python3 main.py --lm-eval "pretrained=/models/xxx-quant,tensor_parallel_size=2,dtype=auto,gpu_memory_utilization=0.6"
```

Compare against BF16 / previous scheme. Keep eval args fixed when A/B testing ignore lists.

## Analysis modes

| `--analysis` | Needs | Use for |
|--------------|-------|---------|
| `outlier` | `--model` | Outlier-heavy layers → AWQ / ignore |
| `mse` | `--model` + `--save-dir` (quantized) | Static weight error after quant |
| `activation_sensi` | both + calib samples | Dynamic MSE; prefer `--num-calibration-samples 128 --max-seq-length 512` |
| `fisher` | `--model` | Grad-based sensitivity |
| `outlier_mse` | both | Combined |

```bash
python3 main.py --model /models/Base --analysis outlier --analysis-top 10
python3 main.py --model /models/Base --save-dir /models/Base-W8A8 --analysis mse --analysis-top 10
python3 main.py --model /models/Base --save-dir /models/Base-W8A8 \
  --analysis activation_sensi --num-calibration-samples 128 --max-seq-length 512
```

Focus columns: Outlier%, Mean MSE, activation MSE, Fisher Mean. Add worst layers to `--ignore`, re-quant, re-eval PPL.

**Ignore note:** CLI `--ignore` **replaces** defaults entirely — include `lm_head` / gates / embeds if still needed.

## Preprocess A/B

If using QuaRot/Flex:

- Quant **with** vs **without** preprocess (`--from-preprocessed`).
- Toggle individual transforms via `--transforms`.
- Optional real acts: `--act-stats` + `use_calib_acts: true`.

## OOM / hang (not precision but often confused)

- Calib: `--pipeline sequential`, `--sequential-targets Linear`, `--offload-hessians`, smaller `--batch-size` / `--max-seq-length`, `--device-map cpu`.
- Save OOM: `--patch-for-llmc`.
- Multi-GPU hang on >100B: prefer `nproc_per_node` 2 or 4.
