# CSV installation and post-tune validation

Use this reference after a full tuned CSV has passed structural validation.

## 1. Select the correct table

The observed AITER mapping is:

| Tune quant key | no-shuffle table | shuffle table |
|---|---|---|
| `no_quant` | `tuned_fmoe_asm.csv` | `tuned_fmoe_asm_shuffle.csv` |
| `int4_w4a16` | `tuned_fmoe_asm_w4a16.csv` | verify current source |
| `int4_w4a8` | `tuned_fmoe_asm_w4a8_group.csv` | verify current source |
| `int8_w8a8_block` | `tuned_fmoe_asm_w8a8_group.csv` | `tuned_fmoe_asm_w8a8_group_shuffle.csv` |
| `f8_w8a8_block` | `tuned_fmoe_asm_w8a8_group.csv` | `tuned_fmoe_asm_w8a8_group_shuffle.csv` |
| `int8_w8a8_channel` | `tuned_fmoe_asm_w8a8_channel.csv` | `tuned_fmoe_asm_w8a8_channel_shuffle.csv` |
| `f8_w8a8_channel` | `tuned_fmoe_asm_w8a8_channel.csv` | `tuned_fmoe_asm_w8a8_channel_shuffle.csv` |

Treat the selected AITER revision's `CSV_FILE_MAPPING` as authoritative; mappings
can change. FP8 and INT8 channelwise rows share a file but remain distinct through
the `quant_type` key.

Locate the table used by the active runtime rather than assuming a site-packages
path:

```bash
python3 - <<'PY'
from pathlib import Path
import aiter
print(Path(aiter.__file__).resolve().parent / "configs")
PY
```

## 2. Merge safely

Installing into a live Python environment or source checkout is a separate mutation;
do it only when requested. Preserve the standalone accepted CSV first.

The replacement key is:

```text
arch,quant_type,indtype,token,inter_dim,model_dim,expert,topk,q_size_n,q_size_k
```

New rows should replace old rows with the same full key. Never append blindly:
duplicates make provenance unclear, and different quant/shape/arch rows must remain.
Also inspect the current runtime's `group_cols`/cache key. An observed AITER version
grouped by `arch, inter_dim, model_dim, expert, topk, quant_type` and token, ignoring
`indtype` and q-size columns. In that version, two rows that differ only in ignored
fields collide at runtime even though their full CSV keys differ. Resolve such a
collision in the lookup code/table design, or establish that the selected solution
is valid for both; do not rely on CSV columns the runtime does not read.

Before replacing a table:

1. validate the source against the full untuned input;
2. copy the target to a timestamped backup;
3. merge to a temporary file in the same directory;
4. preserve permissions and atomically replace the target;
5. rerun exact coverage against the installed file.

The bundled tool defaults to a non-destructive output file:

```bash
python3 scripts/aiter_moe_csv.py merge \
  --target tuned_fmoe_asm_w8a8_channel.csv \
  --source model-tuned.csv \
  --reference untuned.csv --arch gfx938 \
  --output merged.csv
```

For an explicitly authorized in-place install, it creates a backup:

```bash
python3 scripts/aiter_moe_csv.py merge \
  --target /path/to/active/table.csv \
  --source model-tuned.csv \
  --reference untuned.csv --arch gfx938 \
  --in-place
```

The utility rejects a new row that collides with an existing row under the observed
reduced runtime key. `--allow-runtime-key-collision` exists only for a revision whose
actual lookup has been inspected and can distinguish the rows, or when the collision
has otherwise been proven harmless.

If source and installed AITER trees are separate, decide which copies need updating.
Each container can have its own installed package even when the model workspace is
shared. Retain a source-tree copy if the result will be committed upstream.

## 3. Verify runtime lookup in a fresh process

AITER caches parsed CSV groups and solution lookups. Replacing the file does not
invalidate tables already loaded in a server or Python process. Restart the process
before verification and before serving.

Verify two layers:

- direct `get_moe_asm_solution` for every accepted input row;
- framework-facing `get_aiter_moe_config`, explicitly requesting ASM when possible.

Confirm the selected backend is ASM, solution ids match the new CSV, and
`need_shuffle` matches the installed table. Check exact CSV coverage separately,
because nearest-token selection can make untuned values appear successful.

When SGLang still chooses Triton/default despite a correct table, inspect the current
framework's quant-method selection, MoE runner backend, `block_size`, dtype, gating,
TP/EP arguments, shuffle flag, scale dtypes/layout, and actual imported AITER. The
CSV cannot repair a mismatched integration path.

## 4. Numerical and performance validation

Tuner fast modes may benchmark candidates without a full numerical reference. Run a
separate correctness test on representative decode and prefill M values using the
same quantization semantics:

- identical hidden states, expert routing, weights, and scales;
- AITER versus a quantized torch reference;
- optionally AITER versus the framework's prior backend, such as Triton;
- cosine similarity, normalized RMS error, max/mean absolute error, and nonfinite
  checks.

Previously useful smoke thresholds for channelwise W8A8 were cosine at least `0.999`
and NRMS at most `0.05`, but these are evidence from specific models, not universal
acceptance criteria. Keep raw metrics and use the model team's required tolerance.

Benchmark only after correctness passes. Use warmup, device synchronization,
multiple iterations, the same tensors/routing for both backends, and report robust
latency statistics. Test small decode M, transition points where solution ids change,
and large prefill M.

## 5. End-to-end SGLang validation

Force or unambiguously log the backend under test; otherwise a successful request
may still be using Triton/MOE_C. Start a fresh service after installation, then run
requests that contain both nontrivial prefill and multiple decode steps. Compare:

- startup/lookup logs and absence of default-config warnings;
- output sanity and task accuracy against the baseline backend;
- prefill/decode latency and throughput under representative concurrency;
- all TP ranks and any EP-specific behavior.

Keep dense INT8 Linear hipBLASLt/rocBLAS tuning separate from AITER fused-MoE ASM
tables. A model may need both, but their size schemas, collection methods, and output
artifacts are different.
