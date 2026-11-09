# Triton Optimization Memory

This file is the local, human-editable memory for historical optimized kernels
and useful Triton code idioms from previous Hygon Triton runs. Use it during the
Semantic Pre-Pass, after `orchestrate.py setup` and before the initial
`tune_configs.py`. During final report writing, append a new entry only when the
current run produced a reusable pattern or semantic rewrite with correctness and
timing evidence.

The entries here are hints, not proof. The current kernel does not need to have
the same name, op kind, or exact shape as an entry. Inspect this memory for
similar implementation patterns or semantic rewrites: indexing styles, masking
idioms, launch structures, fusion layouts, equivalent formulas, source rewrites,
or other Triton code shapes that may be worth referencing. The agent must still
prove equivalence with `ref.py`, benchmark the candidate, and record the result
in `analysis.md` and `attempt_timeline.json`.

When adding an entry after `orchestrate.py finalize`, prefer a pattern that can
help a future kernel with similar code or semantics. Do not add failed guesses,
one-off run notes, or tricks without a clear reuse guard.

## How To Inspect This Memory

For the current kernel, look for similar patterns or semantic rewrites rather
than exact kernel identity. Useful entries include:

- program id mapping, block traversal, vectorized loads/stores, mask handling,
  accumulation order, reductions, and epilogues;
- equivalent formulas, fused forms, eliminated intermediates, removable masks,
  or alternate parenthesizations;
- op kind and formula, when relevant, for example matmul, reduction, softmax, layernorm,
  transpose, scatter/gather, or elementwise fusion;
- shape family, dtype, layout, strides, masks, and broadcast behavior;
- target architecture, for example gfx936 or gfx938;
- constraints such as aliasing, output order, numerical tolerance, and upstream
  fusion availability.

It is valid to reference an entry from a differently named kernel, or even a
different op family, whenever the implementation pattern or semantic rewrite is
similar enough to be useful.

## Historical Case Review Contract

This file owns concrete historical cases. During the Semantic Pre-Pass, use the
current kernel's `## Kernel Computation Logic`, `## Formula-First Analysis`, and
loop/candidate inventory to find:

- direct pattern matches that can become candidate rewrites;
- analogous cases that inspire a different but related rewrite;
- negative examples or reuse guards that explain why a tempting rewrite should
  be rejected or deferred.

Search entries by:

- formula shape: matmul-like reduction, scan, map, quantization, normalization,
  transpose/materialization, scatter/gather, or fused elementwise form;
- loop and program mapping: per-row, per-token, per-block, j-first/k-first
  traversal, repeated global loads, causal/triangular loop bounds;
- memory/index/mask idioms: strides, broadcasts, mask simplification,
  contiguous vs transposed access, invariant loads, duplicate stores;
- shape/dtype/arch constraints: fixed vs variable length, reduction size,
  bf16/fp32/int8/fp8, gfx936/gfx938, register/LDS pressure;
- proof guard: why the historical rewrite should or should not apply to the
  current kernel contract.

Record the result in `iterv*/analysis.md` under `## Semantic Pre-Pass Result`:

```markdown
- Memory entries checked: `2. KDA per-sub-chunk rewrite: load reuse and separable-gate tl.dot`
- Historical case review: matched repeated causal sub-chunk loads; used the case
  to inspire per-sub-chunk program mapping; kept separable-gate head-wise
  `tl.dot` as a candidate to test or explicitly reject with layout/mask/timing
  evidence.
- Reuse guard: only apply when sub-chunk bounds, dtype tolerance, and program
  mapping preserve `ref.py`.
```

Do not copy an entry into a candidate by name alone. A historical case is useful
only when it helps explain the current formula, loop structure, candidate
decision, or correctness/timing guard.

## Entry Template

Keep each entry compact, ideally under 1000 tokens. Prefer one focused pattern
or semantic rewrite per entry; move long derivations, full reports, and raw logs
to the source case artifacts.

```markdown
### <N>. <short name>

- Key / keywords:
- Similar pattern / semantic rewrite:
- Why equivalent:
- Evidence:
- Reuse guard:
- Source case / kernel:
- Op / formula:
- Shapes / dtype / layout:
- Target arch / Triton version:
```

## Entries

### 1. Quantized store value narrowing before `tl.store`

- Key / keywords:
  `quantized-store`, `store-type-narrowing`, `explicit-cast-before-store`,
  `int8-output`, `fp8-output`, `quant-epilogue`
- Similar pattern / semantic rewrite:
  In quantization-style kernels, the arithmetic path often computes the output
  value in fp32 and then stores into an int8/fp8 output pointer. If the math
  contract already says the result is a quantized value, make that dtype
  transition explicit before `tl.store` instead of relying on store-time
  implicit casting through the pointer dtype. This gives Triton lowering a
  narrower store value and can shorten the live range of the fp32 temporary.

  ```python
  # Before: q remains fp32 until tl.store sees q_ptr's dtype.
  q = x * inv_scale[:, None]
  tl.store(q_ptr + offsets, q)

  # After: q has the intended narrow dtype before the store.
  q = (x * inv_scale[:, None]).to(tl.int8)
  tl.store(q_ptr + offsets, q)
  ```
- Why equivalent:
  The contract already stores `q = cast_to_quant_dtype(x / scale)`. Making the
  cast explicit preserves int8 semantics when checked against `ref.py`.
- Evidence:
  `per_token_quant` correctness passed (`atol=1e-2`, `rtol=1e-2`). Timing moved
  from `0.1456 ms` baseline to `0.09431 ms` final (`1.54x`). Final config stayed
  `BLOCK_M=32, BLOCK_N=512, num_warps=4, num_stages=1`, so the gain was
  attributed to the source rewrite, not tile geometry.
- Reuse guard:
  Use this as a similar pattern, not a name-based rule. Re-check for the target
  output dtype (`tl.int8`, fp8, or another narrow dtype), rounding/saturation
  expectations, scale-zero handling, and pointer dtype. Do not force `tl.int8`
  when the actual output dtype is fp8 or another quantized format.
- Source case / kernel:
  `per_token_quant`
- Op / formula:
  Per-token dynamic quantization:
  `q[row, col] = cast_to_quant_dtype(x[row, col] / scale[row])`.
- Shapes / dtype / layout:
  Observed on flattened `[M, topK, N]` rows,
  `M=4096, topK=8, N=512, bf16 -> int8`.
- Target arch / Triton version:
  Hygon BW1000B, gfx938, Triton 3.5.0.

### 2. KDA per-sub-chunk rewrite: load reuse and separable-gate `tl.dot`

- Key / keywords:
  `kda`, `gated-attention`, `intra-token`, `separable-exp`,
  `tl-dot-candidate`, `head-wise-dot`, `per-sub-chunk`,
  `causal-sub-chunk`, `program-mapping-change`
- Similar pattern / semantic rewrite:
  A token-parallel KDA kernel may compute each `(i, h, j)` with one program per
  token `i`, repeatedly loading the same j-side `k[j]` / `g[j]` values for
  neighboring tokens in a sub-chunk. This directly suggests a per-sub-chunk
  mapping for j-side load reuse. The same formula also exposes a `tl.dot`
  rewrite when each sub-chunk is viewed as `[BC, K]` per head:

  ```text
  Aqk[i,h,j] = scale * sum_k q[i,h,k] * k[j,h,k]
                            * exp2(g[i,h,k] - g[j,h,k])
  Akk[i,h,j] = (j < i) * beta[i,h] * sum_k k[i,h,k] * k[j,h,k]
                                      * exp2(g[i,h,k] - g[j,h,k])
  ```

  The gate is separable:

  ```text
  exp2(g[i,h,k] - g[j,h,k]) = exp2(g[i,h,k]) * exp2(-g[j,h,k])
  ```

  Therefore a sub-chunk can be loaded as `[BC, K]` per head and rewritten as:

  ```python
  eg = exp2(gv)
  right = kv * exp2(-gv)
  aq_left = qv * eg
  ak_left = kv * beta[:, None] * eg
  aq = tl.dot(aq_left, tl.trans(right), input_precision="ieee", out_dtype=tl.float32) * scale
  ak = tl.dot(ak_left, tl.trans(right), input_precision="ieee", out_dtype=tl.float32)
  ```

  Store only the valid triangular outputs with `j <= i` for `Aqk` and `j < i`
  for `Akk`. If multiple heads are handled per program, keep the dot head-wise
  with a static loop or another layout that does not mix head dimensions.
- Why equivalent:
  The rewrite is an algebraic factorization of the same per-head K reduction.
  The causal/diagonal rule is applied at store time, so it masks output elements
  rather than changing the K reduction domain. `beta[i,h]` belongs to the
  i-side `Akk` operand.
- Evidence:
  Historical commit `b3cae47430786bb28573ade024087daac5b4043c` removed a temp
  `chunk_kda_fwd_mat_kernel` / `chunk_kda_fwd_mat_h2_kernel` implementation
  that used exactly this `tl.dot` formulation. Treat that commit as existence
  evidence for the candidate shape, not as final performance proof by itself.
  A future run must still validate correctness and timing under fixed config.
- Reuse guard:
  Use this when the current formula has the separable gate above, the sub-chunk
  shape can be represented as `[BC, K]`, and causal/diagonal masks are only
  output masks. Do not reject the idea merely because the original per-token
  mapping or `BH > 1` layout makes a naive 2D dot mix heads; first consider
  per-head programs or a head-wise static loop. Defer or reject when the gate is
  not separable, the mask changes reduction membership over K, precision
  tolerance fails, or the dot layout increases resource pressure enough to lose
  timing.
- Source case / kernel:
  `examples/triton/kda_fwd/demo.py` parent of commit
  `b3cae47430786bb28573ade024087daac5b4043c`:
  `chunk_kda_fwd_mat_kernel`, `chunk_kda_fwd_mat_h2_kernel`
- Op / formula:
  KDA intra-token gated attention, producing `Aqk` and diagonal-block `Akk`.
- Shapes / dtype / layout:
  Observed with `BT=64`, `BC=16`, `K=128`, H heads, bf16 inputs, fp32 dot
  accumulation.
- Target arch / Triton version:
  Hygon HCU / Triton; verify generated IR/ISA for the target run.


## Applying Memory Entries

- Prefer source rewrites that remove work before tuning config parameters.
- Keep config-only wins separate from semantic or algorithmic wins.
- Do not copy a previous tactic blindly when its proof depends on a different
  layout, mask, aliasing contract, dtype, precision tolerance, or shape family.
- If the tactic is promising but needs upstream graph, allocator, layout, or
  dispatch changes, record it as deferred instead of forcing it into the final
  kernel.
