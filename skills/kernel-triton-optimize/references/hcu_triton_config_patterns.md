# HCU Triton Config Patterns

Use this file for reusable HCU Triton config-registry patterns that are too
specific for `SKILL.md` but broad enough to apply across operators. Keep it as
a pattern catalog, not a copy of any single project's configs.

Known source examples include:

```text
<aiter-root>/aiter/ops/triton
<aiter-root>/aiter/ops/triton/configs
```

Use those sources as examples of config design, fallback behavior, and bucket
selection. Do not copy project business logic into this skill.

## General Rules

- Use finite config registries keyed by shape family and codegen-relevant
  features. Avoid one config per arbitrary shape.
- If shapes are numerous or a key dimension has a large span, first generate a
  `shape_family_plan.json` with at most `small` / `middle` / `large` families.
  Run the normal optimizer workflow separately for each representative family,
  then merge with a `dispatch_manifest.json`.
- When moving to the next family, inspect the previous family champion first.
  Ordinary kernel/source improvements often transfer across nearby families;
  reuse or borrow them only after correctness, fixed-config timing, and IR/profile
  evidence. Do not blindly transfer Split-K / Stream-K style algorithmic
  scheduling changes.
- Separate registry keys from launch config. Keys describe when a config is
  valid; launch config contains Triton meta-parameters such as block sizes,
  `num_warps`, and `num_stages`.
- Record misses explicitly with fallback config, `config_hit=false`, and the
  key that failed to match.
- Treat config search as separate from algorithmic optimization. A faster fixed
  config is valid, but do not attribute it to MMAC, MLS, split-K, or fusion
  unless IR/ISA evidence shows that semantic change.
- Preserve the final fixed config in `final_kernel.py`, plus baseline and
  champion Triton cache directories.
- If a config toggles HCU-sensitive behavior, for example low precision,
  matrix load, buffer ops, or direct LDS paths, require Triton IR/LLIR/ISA
  evidence before making a hardware-path claim.

## Registry Shape

A config entry should usually have this shape:

```json
{
  "key": {
    "op": "moe|attention|gemm|elementwise|memory",
    "arch": "gfx938",
    "dtype": "fp16|bf16|fp8|int8|packed",
    "shape_family": "...",
    "layout": "...",
    "role": "optional"
  },
  "config": {
    "BLOCK_SIZE": 1024,
    "num_warps": 4,
    "num_stages": 2
  },
  "fallback": false,
  "evidence": {
    "correctness": "required",
    "benchmark": "required",
    "triton_cache": "required"
  }
}
```

Use exact dimensions in keys only for well-known model sizes that repeatedly
win a different config. Prefer buckets for everything else.

## Shape-Family Merge Manifest

When `shape_family_plan.json` has `required=true`, optimize each family with the
normal single-shape workflow, then write a compact `dispatch_manifest.json`:

```json
{
  "shape_family_plan": "shape_family_plan.json",
  "merge_policy": "runtime_config_dispatch",
  "final_kernel": "final_kernel.py",
  "families": [
    {
      "name": "small",
      "run_dir": "families/small/run_YYYYMMDD_HHMMSS",
      "final_bench": "families/small/run_YYYYMMDD_HHMMSS/final_bench.json",
      "dispatch_key": "M <= 8",
      "config_key": "small_M"
    },
    {
      "name": "large",
      "run_dir": "families/large/run_YYYYMMDD_HHMMSS",
      "final_bench": "families/large/run_YYYYMMDD_HHMMSS/final_bench.json",
      "dispatch_key": "M > 8",
      "config_key": "large_M"
    }
  ]
}
```

Use `runtime_config_dispatch` when the kernel body is shared and only configs
differ. Use `runtime_variant_dispatch` when families need different kernel
implementations. Use `single_config_proven` only when per-family final benches
show one implementation/config wins every required family.

## MoE-Like Patterns

MoE configs should be keyed by model role and routing shape rather than only
raw tensor dimensions.

- Useful key fields: expert count, output/intermediate width, token bucket,
  quant mode, device/arch family, top-k, projection role, and optional block
  quant shape.
- Runtime should choose the closest token/M bucket from a finite map.
- Bottom/top/shared projections may need distinct configs because layouts,
  packed dimensions, and workspace needs differ.
- Local expert count may differ from global expert count. If a tuned config is
  absent, fall back to a nearby expert-count family or a safe default, and
  record the fallback.
- Common launch fields: M/N/K tile sizes, grouping along M, scale-load policy,
  scheduling variant, `num_warps`, and `num_stages`.
- Quantized MoE configs must include quant mode and block-shape constraints in
  the key or guards.

## Attention-Like Patterns

Attention configs should distinguish decode, prefill, paged attention, and
unified/segmented variants when their memory access patterns differ.

- Useful key fields: attention family, arch, head size or padded head size,
  page/cache block size, query-per-KV bucket, sequence/page family,
  causal/sliding-window mode, alibi/softcap/sink flags, KV dtype, and layout.
- Config values may include block size, query/KV tile sizes, matrix-load
  toggle, `num_warps`, and `num_stages`.
- The matrix-load path interacts with attention blocking layout through the
  `#ttg.dot_op` encoding; different blocking strategies may produce different
  layout conversion overhead.
- Keep divisibility constraints explicit, especially page/cache block size
  versus selected block size.
- If no tuned config exists, derive a safe fallback from head size, element
  size, cache block size, and a tile-byte budget.
- Treat matrix-load and FP8 KV/cache choices as evidence-bearing toggles; they
  need generated Triton IR checks.

## GEMM-Like Patterns

GEMM configs should separate generic shape buckets from finite exceptions for
common model dimensions.

- Useful key fields: GEMM family, arch, M/N/K bucket or common exact N/K pair,
  batch/grouped mode, dtype or quant mode, group size, scale layout, split-K
  policy, and epilogue/fusion role.
- Common launch fields: `BLOCK_SIZE_M`, `BLOCK_SIZE_N`, `BLOCK_SIZE_K`,
  `num_warps`, `num_stages`, and matrix instruction shape
  hints when supported by the Triton build.
- For gfx938+ targets, `mmacLayout` (legacy vs interleave) should be a config key
  or guard because it changes the TTGIR encoding, LDS layout, and DS read
  instruction variant. The `instrShape` is derived from BLOCK_M/N/K, dtype, and
  the target's MFMA instruction table.
- The `waves_per_eu` config parameter affects occupancy and thus the MFMA
  instruction selection; include it in config keys when targeting gfx938+.
- Split-K configs need derived runtime fields, such as adjusted split count,
  split block size, reduction block sizes, partial workspace dtype, and whether
  reduction uses atomics or a second kernel.
- Low-precision or packed GEMM configs must be verified through `tl.dot`
  lowering, LLIR, and ISA before claiming matrix-core use.

## Elementwise / Reduction Patterns

Elementwise and small reductions often need rules more than large registries.

- Useful key fields: flattened element count bucket, row/hidden size bucket,
  dtype, alignment, reduction width, group size, top-k, and whether tails are
  present.
- Prefer one aligned fast path plus one robust masked fallback over many
  nearly identical tail configs.
- Common launch fields: `BLOCK_SIZE`, vector width, `num_warps`, and
  `num_stages`.
- Divisibility predicates such as `N % BLOCK_SIZE == 0` should be explicit so
  mask-removal gains are reproducible.
- Quant/cast configs should record logical shape, packed storage shape, scale
  shape, and group size.

## Memory-Bound Patterns

Memory-bound configs cover copy, cast, quant, KV-cache movement, decode-cache
loads, and simple streaming kernels.

- Useful key fields: element-count bucket, dtype width, alignment, vector width,
  stride/layout family, page/cache block size, group size, and tail policy.
- Prefer stable block-size buckets over exact shape entries.
- Keep feature toggles such as buffer ops, matrix load, and direct-LDS paths in
  the config key or config metadata because they affect Triton cache and ISA
  evidence.
- Validate with timing and rough bandwidth. ISA may be optional for pure
  block-size tuning, but cache IRs and the fixed active config still need
  to be preserved.

## Layout-Aware Config Rules

Triton's TTGIR encoding selection is influenced by config parameters. When config
changes affect the TTGIR layout encoding, the resulting ISA evidence may differ
even if the source code is unchanged.

- Tile sizes (BLOCK_M, BLOCK_N, BLOCK_K) determine the `#ttg.amd_mfma`
  encoding's `instrShape` and `warpsPerCTA`. Different encodings may trigger
  different layout conversion paths (e.g., `#ttg.blocked` → `#ttg.dot_op` via
  LDS vs. direct register shuffle).
- `mmacLayout` (legacy vs interleave) changes the linear layout, which affects
  DS read instruction selection (`ds_read_m32x16_b16` vs `_alt`) and LDS data
  arrangement. On gfx938+, configs that select interleave layout produce
  different Triton cache IRs and ISA than legacy layout.
- `num_stages` affects whether `ttg.async_copy_global_to_local` is generated,
  which changes the layout conversion path.
- When comparing configs, verify that observed timing differences come from
  the intended config change and not from an unintended layout encoding change.
  Check TTGIR IRs before attributing performance changes.

## Adding New Patterns

When adding a project-derived pattern:

1. Summarize the reusable key fields and fallback behavior.
2. Avoid embedding long project-specific JSON examples.
3. Use `<project-root>/path/to/file` style paths so the reference works on
   Windows and Linux.
4. Keep implementation details in the knowledge base when they are useful only
   for source lookup, not for the optimizer's core workflow.
