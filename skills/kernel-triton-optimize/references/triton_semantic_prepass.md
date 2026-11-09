# Triton Semantic Pre-Pass

Use this after `orchestrate.py setup` and before the first `tune_configs.py`
sweep. The pass has one job: understand the current kernel's math deeply enough
to propose cheaper equivalent computation before low-level tuning begins.

This file should shape the agent's attention, not constrain its imagination.
Do not ask "which checklist row applies?" Ask:

> If I were free to rewrite the computation, what equivalent formula, program
> mapping, or primitive would I try before tuning block sizes?

`references/triton_optimization_memory.md` owns historical case review: direct
matches, analogies, negative examples, and reuse guards. This file owns the
current-kernel reasoning and evidence standard.

## Thinking Loop

Run this loop on the agent/control side:

1. **Name the outputs.** For each output tensor, write the formula with explicit
   dimensions and masks. Do this before focusing on Triton tile details.
2. **Separate semantics from implementation.** Mark which loops are real
   mathematical reductions, which are maps/scans, and which exist only because
   of the current program mapping.
3. **Look for a different computation, not just a faster loop.** Consider
   algebraic factorization, hidden matmul, scan/reduction primitives, hoisting,
   work elimination, fusion/batching, or a different program ownership model.
4. **Use memory as a case library.** Search
   `references/triton_optimization_memory.md` for cases that match directly,
   inspire an analogy, or warn against a tempting rewrite. Historical entries
   are context, not proof.
5. **Pick candidates to promote, not boxes to fill.** A good pre-pass usually
   produces one or two serious candidates plus a short list of rejected/deferred
   ideas.

Later iterations can carry forward this analysis and only write deltas. Rerun
the full pass when the champion changes semantics, shape family, layout/stride
contract, or when profile/IR evidence contradicts the expected computation.

## Analysis Output

Write compact evidence in `iterv*/analysis.md`. **Do not force tables.** Tables
are optional and should be used only when they make the algorithmic decision
clearer. Prefer a few focused bullets over a large form. The non-negotiable goal
is to expose algorithm-level optimization candidates; everything else is
supporting evidence.

The exact format can vary, but the following sections must be findable:

```markdown
## Kernel Computation Logic

- Tensor roles, shapes, dtype/layout assumptions.
- Formula for each output, including masks and reduction/scan axes.
- Optional short pseudocode only when it clarifies semantics; the formula is the required artifact. Do not rely on a Python reference dump as the semantic explanation.

## Formula-First Analysis

- One or two candidate semantic rewrites worth trying, with the formula reason.
- Important candidates rejected or deferred, with the reason.
- Historical memory entries checked and how they affected thinking.

## Loop / Candidate Inventory

- Only discuss loops that affect the algorithmic decision.
- Note whether a loop is real mathematical work or implementation bookkeeping.
- State which candidate is the best first implementation target.

## Semantic Pre-Pass Result

- Promoted semantic rewrite: `<name>` or `none`.
- Historical case review: `<matched/inspiring/rejected entries + reason>` or `none`.
- Rejected/deferred candidates: `<short reason>`.
- Timeline recording: `record_attempt.py` path/event id, or `not applicable`.
```

If a source-changing candidate is created before proof/timing is complete,
record it as pending before the config sweep that follows:

```bash
python <skill>/scripts/record_attempt.py \
  --run-dir ./run_YYYYMMDD_HHMMSS \
  --iter 1 \
  --kind semantic_rewrite \
  --candidate "<rewrite name>" \
  --status pending \
  --outcome candidate_created_before_validation \
  --analysis ./run_YYYYMMDD_HHMMSS/iterv1/analysis.md
```

After `ref.py` correctness and fixed-config timing, append a second
`semantic_rewrite` event for the same candidate with `--status success` or
`--status failure` and a short proof/outcome. The following `tune_configs.py`
sweep writes one consolidated `config_tune` event automatically; do not record
each config as a separate manual attempt.

## Rewrite Prompts

These prompts are meant to provoke candidates. They are not exhaustive and they
are not rules.

- **Can the formula become a matmul-like primitive?**
  Look for `sum_k A[..., m, k] * B[..., k, n]` or
  `sum_k A[..., m, k] * B[..., n, k]`. If current program mapping would mix
  batch/head dimensions, consider a per-head, per-sub-chunk, or batched mapping
  before rejecting `tl.dot`.

- **Can a composite expression be separated?**
  Examples: `exp(a - b) = exp(a) * exp(-b)`, or grouping i-only and j-only
  factors before a reduction. A separated formula may expose `tl.dot`, hoisting,
  or reuse even when the original loop does not look like matmul.

- **Is the expensive loop real math or current ownership?**
  A loop over tokens/blocks may only exist because one program owns too little
  work. Ask whether a chunk, row group, head, or batch should own the work
  instead.

- **What data is reread by many programs?**
  Repeated global loads can suggest program remapping, larger tiles, cooperative
  reuse, or an upstream fused/batched kernel.

- **Is there a true scan or recurrence?**
  If the operator is associative over a bounded segment, consider
  `tl.associative_scan` or segmented scan. If it is not associative, do not
  pretend it is a reduction.

- **Can work disappear?**
  Constants, all-true/all-false masks, repeated stores, invariant expressions,
  unused intermediates, and tiny standalone kernels may be eliminated, hoisted,
  specialized with guards, fused, or batched.

- **What would a historical case make me try?**
  Do not copy an entry by name. Extract the idea: formula shape, loop ownership,
  indexing/mask idiom, reuse guard, or negative evidence.

## Promotion Standard

Use this standard to keep the pass open-ended but grounded:

- **Try** a candidate when it is semantically plausible and could reduce work,
  memory traffic, launch count, latency, or expose a stronger primitive.
- **Reject** it when it changes the output contract, fails correctness, makes
  precision/layout illegal, or produces clearly worse timing/resource evidence.
- **Defer** it when it likely needs upstream graph/layout/dispatcher changes,
  extra runtime guards, or broader shape coverage.
- **Promote** it only after correctness against `ref.py`, fixed-config timing,
  and acceptable resource/codegen evidence.

Do not time `ref.py` as an optimization metric. Use kernel timing for
before/after comparison. Historical memory entries and formula elegance are not
proof; they are reasons to build and test a candidate.
