---
name: hcu-aiter-moe-tuning
description: Collect, tune, validate, and install AITER ASM fused-MoE configuration CSVs on HCU ROCm systems such as gfx936 and gfx938. Use for a new model, TP/EP layout, quantization mode, or GPU architecture that lacks exact AITER MoE sizes, including FP8/INT8 W8A8 and SGLang verification. Do not use for rocBLAS or hipBLASLt dense-GEMM tuning.
---

# HCU AITER MoE tuning

Produce a reproducible, architecture-specific AITER ASM MoE table rather than
merely making the missing-config warning disappear.

## Operating rules

- Respect the requested stopping point. Preparing a tune bundle does not authorize
  consuming GPUs, starting a server, installing into a live Python package, or
  committing an AITER branch.
- Treat `(arch, quant_type, indtype, token, inter_dim, model_dim, expert, topk,
  q_size_n, q_size_k, shuffle)` as the logical configuration identity. Never reuse
  a result across gfx architectures, quant modes, TP/EP shapes, input dtypes, or
  shuffle modes merely because its solution id looks plausible.
- Derive a candidate shape statically, then confirm it from post-sharding tensors or
  AITER runtime size logs. In particular, do not guess `expert` under EP.
- Keep tuning source and imported runtime AITER compatible. Always record
  `aiter.__file__`, AITER revision/version, torch/HIP versions, reported gfx arch,
  device count, and the exact input CSV.
- Prefer no-shuffle unless the framework actually supplies shuffled weights and the
  current kernel's alignment rules permit it. Tuning one mode and serving the other
  is invalid.
- A successful lookup does not prove that the exact token size was tuned: current
  AITER tables may select the nearest token row. Audit exact CSV coverage separately.
- Inspect the selected AITER revision's actual cache/group key. Some observed
  versions ignore `indtype` and q-size fields even though the CSV contains them;
  detect conflicting rows instead of assuming those fields disambiguate lookup.
- Keep the standalone tuned CSV as the primary artifact. Install by validated,
  key-based merge with a timestamped backup; restart the consuming process so cached
  tables are reloaded.

## Workflow

1. Inspect the model quantization config, AITER/SGLang call path, TP/EP layout, and
   post-sharding weight shapes. If shapes or representative runtime sizes are not yet
   known, read [shape and size collection](references/shape-and-size-collection.md).
2. Locate the table used by the imported AITER and calculate exact coverage. Tune
   only missing rows. Use `scripts/aiter_moe_csv.py` for log collection, input CSV
   generation, validation, deduplication, coverage checks, and safe merges.
3. Before using GPUs, establish that they are idle and that the requested action
   allows tuning. Run an environment/source preflight. For the actual runner,
   multi-GPU behavior, resume strategy, shuffle preparation, and failure recovery,
   read [tuning runbook](references/tuning-runbook.md).
4. Reject incomplete, duplicate, wrong-arch, wrong-shape, non-ASM, invalid-solution,
   or non-positive-timing rows. Do not merge smoke or partial output as a full table.
5. If installation or framework validation is in scope, read
   [CSV installation and validation](references/csv-install-and-validation.md).
   Verify exact table coverage, fresh-process AITER lookup, numerical accuracy,
   kernel performance, then an end-to-end SGLang request that exercises both prefill
   and decode.

## Deliverables

For a reusable tune handoff, provide:

- a machine-readable shape manifest containing model dimensions, TP/EP semantics,
  quant mode, input dtype, shuffle mode, target arch, and provenance;
- full and smoke untuned CSVs, preferably with full rows collected from realistic
  service traffic plus any deliberately added boundary grid;
- a portable launcher with preflight, explicit GPU selection, logs, per-row durable
  output, and resume behavior;
- a validator and exact-coverage report;
- the standalone tuned CSV and checksum after tuning;
- installation/rollback instructions and post-install lookup, accuracy, performance,
  and service-validation evidence.

Do not hardcode a particular user's home, host, container name, or model mount in a
bundle intended for another person. Use paths relative to the bundle and explicit
environment variables for AITER/model locations.

## Completion bar

A tuning task is complete only when every required logical key has one valid result
for the target architecture and mode, and any requested installation/verification
has actually passed. A prepared-only task is complete when the inputs, scripts,
assumptions, and commands are validated without launching GPU work.
