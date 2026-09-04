# AITER ASM MoE tuning runbook on HCU

Use this reference once the untuned CSV and target arch are known.

## 1. Freeze provenance

Record before running:

```bash
python3 - <<'PY'
import aiter, torch
print("aiter:", aiter.__file__)
print("torch:", torch.__version__, "hip:", torch.version.hip)
print("gpu:", torch.cuda.get_device_name(0))
print("arch:", torch.cuda.get_device_properties(0).gcnArchName)
print("visible:", torch.cuda.device_count())
PY
git -C "$AITER_ROOT" status --short --branch
git -C "$AITER_ROOT" rev-parse HEAD
```

Use the architecture string reported before any suffix, for example `gfx936` or
`gfx938`. Results are not portable between them. Prefer a clean AITER checkout or an
isolated worktree; never overwrite unrelated source changes.

The imported AITER runtime and `moe_tune/` source must be compatible. Set
`PYTHONPATH` intentionally and verify `aiter.__file__`; a preinstalled package can
otherwise shadow the intended build, or an unbuilt source checkout can shadow the
working runtime.

## 2. Preflight the tuner and mode

Check that the selected revision contains:

- `moe_tune/moe_tune_runner.py`, `moe_problem.py`, and `moe_tuner.py`;
- the exact quant key used in the input CSV;
- ASM solution enumeration/timing for that quant type;
- the intended input dtype, scale layout, and block sizes;
- a consistent shuffle state in generated weights and the kernel call.

Run the bundled read-only preflight when compatible with the selected AITER tree:

```bash
python3 scripts/preflight_aiter_moe.py \
  --aiter-root "$AITER_ROOT" \
  --quant-type f8_w8a8_channel \
  --expected-arch gfx938 \
  --mode no-shuffle
```

For no-shuffle, shuffled-weight statements must be inactive and the ASM call must
use `shuffle=0`. For shuffle, both weight transformations and the call argument must
be active. Do not edit the active AITER source back and forth without a reliable
backup/restore or an isolated worktree. Validate current alignment restrictions;
some observed channelwise shuffle kernels required gate/up N to be divisible by 128.

## 3. GPU selection and smoke test

Check that the selected devices are idle. Set both ROCm visibility variables and the
compile architecture:

```bash
export HIP_VISIBLE_DEVICES=0,1,2,3
export ROCR_VISIBLE_DEVICES=0,1,2,3
export GPU_ARCHS=gfx938
```

`--mp` controls candidate-level tuner parallelism. It does not set model TP, and it
must not exceed the count of visible GPU IDs. One GPU is valid but slower.

Make a smoke CSV containing a few small/transition shapes, validate it, and run it
before the complete list. The standard AITER runner is typically invoked from the
`moe_tune` directory:

```bash
python3 moe_tune_runner.py \
  --input_file /path/to/smoke.csv \
  --tuned_file /path/to/tuned.csv \
  --mp 4
```

The tuner uses synthetic tensors, so model weights and an SGLang service are not
required. Large `M`, `E`, and dimensions still consume substantial device memory.

## 4. Full run and resume

- Use one exclusive output file per arch, quant mode, logical shape, and shuffle
  mode. Do not let concurrent jobs append to the same CSV.
- Ensure each completed row is flushed to durable output. The observed AITER runner
  appends rows and can skip keys already present when the same result path is reused,
  but verify this behavior in the selected revision.
- Before resuming, validate every existing row. Then rerun with the same output path
  and full input. Never call a partial file complete merely because the process
  exited cleanly.
- If a multiprocessing worker is recreated and `mp_tuner` reports a transient
  `gpuIDMap`/worker error, stop leftover workers, confirm memory is released, and
  resume the same validated file. Do not discard completed rows.

Some general AITER runners benchmark CK and ASM and record the fastest backend. An
ASM table may contain only `sol_type=asm` with a two-part solution such as
`10008+20001`. If any row is labelled CK/default, do not merge it into an ASM table;
use an ASM-only runner or investigate why no valid ASM candidate survived.

## 5. Output validation

Expected input columns:

```text
quant_type,indtype,token,inter_dim,model_dim,expert,topk,q_size_n,q_size_k
```

Expected tuned columns:

```text
arch,quant_type,indtype,token,inter_dim,model_dim,expert,topk,q_size_n,q_size_k,sol_type,sol_id,time_us
```

Validate against the complete input:

```bash
python3 scripts/aiter_moe_csv.py validate \
  --kind tuned --csv tuned.csv --arch gfx938 --reference untuned.csv
```

Require:

- exact input-key coverage with no duplicates;
- the intended arch and quant/dtype/shape fields;
- `sol_type=asm`;
- a valid two-part ASM solution id;
- finite positive `time_us`.

One observed resumed FP8 output accumulated duplicate rows. If this occurs, preserve
the raw file and create a separate deduplicated file, keeping the latest row per full
logical key; then validate the deduplicated result against the complete input:

```bash
python3 scripts/aiter_moe_csv.py dedup \
  --input tuned.raw.csv --output tuned.dedup.csv --keep last
```

## 6. Measurement hygiene

Tune on idle devices with the same target GPU architecture and a compatible
ROCm/AITER stack. Record clocks/power policy if controlled in the environment, but
do not change system-wide settings without authorization. A solution chosen under
contention is structurally valid yet may be a poor performance choice.

Keep raw logs and report elapsed time, failed/resumed segments, input/output row
counts, duplicate handling, and a checksum of the accepted CSV.
