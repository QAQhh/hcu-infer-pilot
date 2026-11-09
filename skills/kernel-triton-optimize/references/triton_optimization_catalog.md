# Hygon Triton Optimization Catalog

This is the active method catalog for `kernel-triton-optimize`.
Do not use the HIP catalog names directly in Triton runs. HIP source-level
`__builtin_*` methods map to Triton evidence through:

```text
Triton source / config
  -> TTIR / TTGIR artifacts (`.ttir` / `.ttgir`)
  -> hsaco / HCU ISA (dccobjdump) and resource metadata
  -> timing and correctness
```

`isa_check.py` matches `.ttgir` and HCU ISA only (see `hcu_triton_isa_signatures.json`).
Manual `.ll` / `IntrinsicsHCU.td` is optional debug, not automated proof.
Evidence claims in this catalog must be backed by durable signatures,
generated IRs, and automated before/after validation. When a method
requires before/after delta or runtime timing, a single TTGIR/ISA pattern is not
sufficient proof.
Buffer-op check: in `.ttgir`, hot-path loads/stores must appear as
`amdg.buffer_load` / `amdg.buffer_store` to claim buffer-op conversion. If they
remain `tt.load` / `tt.store`, buffer-op conversion failed for that path; later
ISA may show `global_*` / `flat_*`, but that is fallback, not buffer ops.

Triton translation rules:

- Do not port HIP builtins (`__builtin_hcu_*`, `__builtin_amdgcn_*`) directly
into Triton. Use Triton-native `tl.*`, `triton.Config`, and compiler options.
- Use `tl.inline_asm_elementwise` only as an escape hatch when no Triton-native
lowering exists, and only with generated TTGIR/ISA proof.
- Automated HCU proof is TTGIR (`tt.*` / `ttg.*` / `amdg.*`) plus final ISA, not
`llvm.hcu.*` in `isa_check.py`.
- Do not invent a Triton API from a HIP builtin. Find the real lowering path and
verify `.ttgir` plus hsaco ISA.

## Global Selection Rules

Each method entry should tell the agent: when to try it (`Trigger`), what to
change (`Implement`), how to prove it worked (`Evidence`), and when to skip it.
Use `references/triton_method_registry.json` for exact ids, priorities, arch
requirements, and validator metadata.

1. Run the full Semantic Pre-Pass after setup and before the
initial config tuning; later iterations only need a `## Kernel Computation
Logic` delta unless semantics changed.
2. Use local KB evidence when available; if KB is unavailable, mark the run
  degraded and rely on source, Triton cache IRs, `dccobjdump`, and
   benchmark evidence.
3. Keep config improvements separate from algorithmic method attribution.
4. For matrix paths, validate the whole data path: global load, LDS/tile
  staging, matrix-read or matrix-load intrinsic, MMAC, epilogue, and waits.
5. When `hipprof` or `dccobjdump` is unavailable, keep the faster correct
  kernel but mark profile/ISA evidence degraded or inconclusive.

## Semantic Pre-Pass

Use `references/triton_semantic_prepass.md` once after setup and
before the initial `tune_configs.py`; consult historical memory such as
`references/triton_optimization_memory.md` when present. Rerun it only after semantic rewrites or
suspected drift. Each iteration must still write `## Kernel Computation Logic`
in `iterv{i}/analysis.md`: either a fresh summary or a delta/carry-forward from
the previous champion. It is not a `methods.json` axis; budgets are only
`compute`, `memory`, and `latency`. `close-iter` rejects missing or placeholder
logic sections.

Record promoted semantic rewrites in `analysis.md`, `attempt_timeline.json`, and
final `summary.md` as algorithmic/source changes. Only add a compute/memory/latency
method to `methods.json` when the rewrite also has a hardware-axis effect, for
example `triton.mask_simplification`, `triton.work_granularity`, or
`triton.coalesced_load_store`.

Do not write the semantic checklist itself as a `methods.json` id; the registry
still owns the final method ids.

## Compute Axis

### P1: `triton.dot_mmac_shape` - `tl.dot` / HCU MMAC Shape

- HIP analogue: `compute.mmac_tensor_core`.
- Trigger: GEMM, attention, MoE, convolution, or batched matmul semantics exist
and timing/profile/IR suggests scalar VALU or weak dot lowering.
- Implement: tune `BLOCK_M`, `BLOCK_N`, `BLOCK_K`,
accumulator dtype, input layout, and dot operand order. On HCU targets, tile sizes
and dtype determine the `#ttg.amd_mfma` encoding selection, including `instrShape`
and `warpsPerCTA`.
- TTGIR evidence: `tt.dot` / `tt.dot_scaled`, `#ttg.amd_mfma<` (see signatures).
- ISA evidence: `v_mmac`, `MMOP`, or Hygon-specific matrix instructions.
- Skip: no matrix semantics, dtype unsupported, or generated code already uses
the intended MMAC path.

### P2: `triton.low_precision_fp8_bf8` - FP8/BF8/TF32 Triton Path

- HIP analogue: `compute.mixed_precision_fp8_bf8`.
- Architecture: split by sub-path. FP8/BF8 requires **gfx938+**. TF32 dot is a
candidate from **gfx928+** when the active Triton build exposes `tf32` as an
allowed dot input precision.
- Trigger: tolerant accuracy and memory-bandwidth or matrix-math benefit from
lower precision. Use the FP8/BF8 path on **gfx938+** when source uses FP8/BF8
packed formats or explicit scales. Use the TF32 path on **gfx928+** for **f32**
`tl.dot` / GEMM / attention matmul when the active HCU Triton build exposes `tf32`
as an allowed dot input precision and a TF32 branch **passes the case `ref.py`
correctness check** at the existing `atol`/`rtol` (do not relax tolerance to
force a pass).
- Implement FP8/BF8: use Triton dtype conversion and pack/unpack forms only
when the target Triton build lowers them correctly; otherwise branch as
experimental. For `dot_scaled` / MLS low-precision paths, verify the specific
target feature and scale support; do not infer full support from arch alone.
- Implement TF32: keep f32 operands. Use explicit
`tl.dot(..., input_precision="tf32", ...)` for a TF32 branch;
use `input_precision="ieee"` or `TRITON_F32_DEFAULT=ieee` to force f32 precision.
Confirm the active precision from source/env plus IR or ISA before attributing
the result.
- Final delivery: if the champion uses TF32 `tl.dot` explicitly, through env/knobs,
or by target default, add `## ⚠️ TF32 精度提醒` after `## Headline` with the active
precision evidence and final correctness (`passed`/`failed`, `atol`, `rtol`).
- Required evidence: the kernel reaches final backend code generation, and
TTGIR shows either `tt.dot` with f8/bf8 operands or `tt.dot_scaled` for
block-scaled/microscaling paths; for TF32, source/env/metadata plus TTGIR,
LLVM, or final ISA must show that f32 `tl.dot` used the TF32 path, and `bench.json`
must show `correctness.passed=true` for the promoted champion. `tt.dot_scaled`
is valid evidence only when that path also reaches final code generation on the
target backend.
- Supporting evidence: final AMDGCN/ISA contains FP8/BF8/TF32 MMAC or CVT
mnemonics exposed by the disassembler.
- Skip: FP8/BF8 on targets below gfx938; FP8/BF8 scaling/quantization missing for
quantized paths; TF32 branch fails `ref.py` correctness at existing tolerance;
or the active Triton build does not expose the requested FP8/BF8/TF32 lowering
for the chosen sub-path.

### P3: `triton.program_geometry_occupancy` - Program Geometry / Occupancy

- HIP analogue: `compute.launch_config_wave64`.
- Trigger: occupancy is low, program mapping underfills CUs, or latency hiding
is poor.
- Implement: tune `num_warps` when available,
`tl.program_id` mapping/grouping, launch grid tile count, and finite
`triton.Config` keys.
- Evidence: active config/metadata shows the geometry and `warp_size=64`;
timing improves without unacceptable VGPR/LDS/occupancy regression. ISA proof is
optional.

### P4: `triton.mask_simplification` - Compute-Side Mask Arithmetic Reduction

- Cross-axis method: primary registry axis is Memory P2, but it also belongs to
Compute Axis when the bottleneck is predicate, bounds, compare, select, or
address arithmetic used only to build masks.
- Trigger: TTGIR/LLVM/ISA or profiler triage shows many mask-related scalar/VALU
ops (`cmp`, `and`, `or`, `select`, bounds arithmetic) around otherwise simple
math, reductions, GEMM epilogues, attention loads, or elementwise paths.
- Implement: same method as Memory P2: specialize aligned shapes with
`tl.constexpr` / `@triton.heuristics`, split hot main path from tail path,
remove redundant `tl.where` / predicate construction, and keep masks only where
they are semantically required.
- Evidence: before/after TTGIR/LLVM/ISA shows fewer predicate/bounds/mask
arithmetic instructions on the hot path; timing improves with correctness
preserved for both aligned and tail/ragged cases. Do not require a
memory-instruction change when the win is compute-side arithmetic reduction.

### P5: `triton.work_granularity` - Per-Lane Work Granularity / Register Tile

- HIP analogue: `compute.thread_coarsening`.
- Trigger: one Triton program or lane computes too many output elements,
accumulator/register tiles are too large, VGPR pressure is high, spills appear,
occupancy drops, or scalar/address work grows with the per-lane element count.
Also consider the opposite direction when each lane does too little work and
loop/address overhead dominates.
- Implement: tune `BLOCK_SIZE`, `BLOCK_M`, `BLOCK_N`, `BLOCK_K`, output
elements per program/lane, accumulator tile shape, `tl.arange` vector shape,
`tl.static_range` extent, and `num_warps`. Reduce per-lane work when pressure or
occupancy is the bottleneck; increase it when overhead dominates and coalescing
remains healthy.
- Evidence: active config/source delta changes per-program/per-lane work; Triton
metadata, code-object AMDGCN, `hipprof`, or `xcu` shows VGPR/spill reduction,
better occupancy/waves, or lower instruction/request overhead; coalescing stays
healthy; timing improves with correctness preserved.

### P6: `triton.split_k_streamk` - Split-K / Stream-K for CU Fill

- Cross-axis method: primary registry axis is Latency P4, but it also belongs to
Compute Axis when split-K or Stream-K improves CU occupancy and compute
utilization.
- Trigger: large K, few output tiles, tail imbalance, or low CU activity leaves
matrix cores underfilled.
- Implement: split K or use Stream-K-style tile scheduling to create more
parallel work, write partial accumulators to a split-major partial buffer, then
reduce them with a dedicated Triton sum/reduce kernel. Avoid `tl.atomic_add` as
the normal accumulation path.
- Evidence: source/config proves partitioning, partial-buffer shape, and the
dedicated reduction kernel; occupancy/CU activity or tail latency improves, with
correctness and timing.

### P7: `triton.register_pressure_control` - VGPR/SGPR Pressure Control

- HIP analogue: `compute.register_pressure_control`.
- Trigger: spills, poor occupancy, or large TTGIR live ranges.
- Implement: reduce tile size, `num_stages` only for pipelined loops,
`tl.static_range` unroll, temporary tensors, and accumulator footprint; split
epilogue or reduce vector width when needed.
- Evidence: Triton metadata or AMDGCN resource comments show lower VGPR/SGPR,
spill/scratch, LDS, or better occupancy; timing improves.

### P8: `triton.fast_math_lowering` - Triton Math Lowering

- HIP analogue: `compute.fast_math_intrinsics`.
- Trigger: exp/log/div/sqrt/rsqrt or type conversions dominate.
- Implement: use explicit Triton controls only within tolerance: `tl.math.exp2`
forms, `tl.math.fdiv(..., ieee_rounding=False)` vs `tl.math.div_rn`,
`tl.math.sqrt` vs `tl.math.sqrt_rn`, HIP libdevice `fast_*` functions when
exposed, `allow_flush_denorm=True`, `enable_fp_fusion`, reciprocal multiply, or
dtype changes.
- Evidence: source/config delta plus TTGIR/LLVM/ISA special-function,
denorm/FTZ, FMA, or arithmetic-sequence change; accuracy and timing pass.

## Memory Axis

### P1: `triton.coalesced_load_store` - Coalesced Global Memory Access

- HIP analogue: `memory.coalesced_access`.
- Trigger: strided/scattered global access, high cache request pressure, or low
effective bandwidth.
- Implement: make `tl.load`/`tl.store` pointer expressions contiguous with
`tl.arange` on the fastest-moving dimension; adjust `tl.program_id` mapping,
`tl.max_contiguous` / `tl.multiple_of` hints, and avoid modulo/scatter addressing
on the hot path.
- Evidence: source indexing shows contiguous per-program/per-lane address
expressions, runtime shows lower request count or higher effective bandwidth,
and timing improves with correctness preserved. Final ISA load-store families are only
supporting context because `tt.load` / `tt.store` and generic
`global_`/`buffer_`/`flat_` instructions are ubiquitous and do not prove
coalescing by themselves.

### P2: `triton.mask_simplification` - Mask / Bounds Elimination for Hot Paths

- Trigger: hot aligned load/store paths carry non-semantic masks or bounds
arithmetic that keeps them as masked `tt.load` / `tt.store`, blocks
`amdg.buffer_load` / `amdg.buffer_store`, or limits coalescing/vectorization.
- Implement:
  - Use `@triton.heuristics` to compute `tl.constexpr` divisibility flags such
    as `EVEN_K`, `EVEN_M_N`, `n_dividable`, or `block_*_diviable`, then branch
    to unmasked `tl.load` / `tl.store` when the hot shape is aligned.
  - Split aligned main tiles/loops from true boundary tails, so only the tail
    path carries masks.
  - Prefer finite config buckets and block sizes that make hot dimensions
    divisible by tile sizes.
  - Keep masks for real semantic masks: causal attention, routing validity,
    padding, ragged sequences, or any load/store whose address may be invalid.
  - Treat `@triton.heuristics` as one common mechanism, not the only mechanism;
    source restructuring, shape guards, config dispatch, and main/tail splitting
    can all remove masks.
- Evidence:
  - TTGIR or pre-buffer-op IR: hot `tt.load` / `tt.store` masks are removed,
    all-true, or limited to true tail/ragged paths.
  - TTGIR/LLVM/ISA: predicate, compare, select, or bounds/address arithmetic for
    masks is reduced; before/after reduction is the proof.
  - Buffer-op side claim: in `.ttgir`, expected hot-path loads/stores must be
    `amdg.buffer_load` / `amdg.buffer_store`; remaining `tt.load` / `tt.store`
    means conversion failed for that path.
  - Runtime: timing and effective bandwidth improve; aligned and tail/ragged
    correctness cases pass.

### P3: `triton.vectorized_load_store` - Vectorized Memory Access

- HIP analogue: `memory.vectorized_global_access`.
- Trigger: contiguous aligned tensors and scalar memory instruction overhead.
- Conditions: expose contiguity, divisibility, and mask constancy on the hot
access path. Low mask constancy forces AMD lowering to shrink vector length.
- Implement:
  - Shape offsets so the hot dimension is produced by a simple `tl.arange`
    pattern in the fastest-moving dimension; avoid modulo/scatter expressions on
    the hot vectorized path when a main/tail split can isolate them.
  - Use `tl.multiple_of`, `tl.max_contiguous`, `tl.max_constancy`, finite shape
    buckets, or compiler attrs where correct to expose contiguity,
    divisibility, and mask constancy.
  - Combine with `triton.mask_simplification`: remove masks on aligned hot
    paths, or make the remaining mask constancy at least the desired vector
    width. `LoadStoreOpToLLVM.cpp` reduces vector length to the mask alignment
    when a mask is present.
  - Prefer pointer forms that canonicalize to `tt.addptr(tt.splat(base),
    tensor_i32_offset)`. Use `tt.pointer_range = 32` or int32-offset rewrites
    only with a real allocation/range contract; never cast offsets to int32 just
    because the tested shape is small.
  - Tune `BLOCK_SIZE`, vector-shaped offsets, aligned dtype packing, and block
    geometry so the resulting vector width is useful but still within the
    per-lane 128-bit lowering limit.
- Evidence: source, hints/attrs, runtime guards, or debug logs support the
contiguity/divisibility/mask-constancy/offset-range claim. For buffer-op claims,
post-conversion AMDGPU IR must show `amdg.buffer_load` / `amdg.buffer_store`.
LLVM/ISA proves final load/store family or vector width (`*_dwordx2/x3/x4`,
64/128-bit forms), fewer memory instructions, and improved bandwidth/timing.

### P4: `triton.layout_stride_transform` - Layout / Stride Transform

- HIP analogue: `memory.aligned_layout_transform`.
- Trigger: logical tensor layout mismatches the hot access order.
- Implement: rewrite pointer arithmetic/stride arguments, swap `tl.program_id`
axes, use finite shape-family `triton.Config` keys, or fuse/remove `tl.trans` /
source transposes when the target project contract allows it.
- Evidence: coalesced address order, lower memory traffic, correctness on
non-contiguous and edge shapes.

### P5: `triton.async_copy_global_to_lds` - Async Global-to-LDS Copy Path

- HIP analogue: `memory.global_to_lds_async`.
- Trigger: matrix/tile kernels stage global data through VGPRs before LDS,
causing register pressure or instruction overhead.
- Scope: non-MMAC / non-matrix-core paths only; matrix-core global-to-LDS paths
belong to `triton.matrix_ds_mls`.
- Implement: currently not enabled for ordinary Triton source on this path. When
enabled, use the Triton lowering that emits `ttg.async_copy_global_to_local` or
`amdg.buffer_load_to_local`; do not copy HIP
`__builtin_amdgcn_raw_buffer_load_lds` into Triton source.
- TTGIR evidence: `amdg.buffer_load_to_local`, `ttg.async_copy_global_to_local`.
- ISA evidence: buffer/global-to-LDS instruction family and correct waits.

### P6: `triton.matrix_ds_mls` - `tl.matrix_load` MLS / DS Matrix Path

- HIP analogues: `memory.matrix_load_mls` and `memory.ds_read_matrix_layout`
- Trigger: GEMM/attention/MoE/conv uses matrix cores, or matrix-core kernels show
high register pressure from `tl.load` / block-pointer loads feeding `tl.dot`.
- Implement: replace eligible `tl.make_block_ptr` + `tl.load` or raw `tl.load`
matrix tiles with `tl.matrix_load(base, shape, strides, block_shape, offsets)`.
Prefer hot paths with no `mask` and no `boundary_check`; do not try masked
`tl.matrix_load` as a performance branch.
- TTGIR evidence: `tt.matrix_load` before AMDGPU conversion; after conversion,
`amdg.matrix_load_to_local`, and `ttg.async_commit_group` /
`ttg.async_wait` or `amdg.async_wait` when pipeline waits are emitted.
`#ttg.dot_op<` is operand-context evidence only; normal `tl.dot` can produce it
without MLS.
- ISA evidence: `matrix_load`/`mls` plus `ds_read_m*` / `ds_read_matrix_*`
families; timing improves with correctness. Skip when no matrix core, masked
matrix load is required, or the path already uses `tl.matrix_load`.

### P7: `triton.layout_conversion_optimization` - Layout Conversion Overhead Reduction

- Triton addition: no direct HIP twin (Triton compiler manages layout).
- Trigger: `ttg.convert_layout` between `#ttg.blocked` and `#ttg.dot_op` generates
significant LDS traffic; TTGIR shows many layout conversion ops before `tl.dot`.
- Implement: choose `BLOCK_M/N/K` and `num_warps` to minimize blocked-to-dot_op
conversion; tune `num_stages` only when a loop can be pipelined. Adjust dot
operand order, `tl.trans` placement, or source layout so the compiler can reuse
LDS-staged data across K iterations.
- TTGIR evidence: `ttg.convert_layout` between `#ttg.blocked` and `#ttg.dot_op`;
count and arrangement of conversion ops. Presence of `ttg.convert_layout` is
only an opportunity signal, not proof that the method worked.
- Evidence: before/after TTGIR shows fewer or cheaper layout conversions on the
hot path, with lower LDS traffic or lower timing. Do not claim this method from
a single post-change TTGIR that merely still contains `ttg.convert_layout`.
- Skip: when no dot operation exists or conversions are already minimal.

### P8: `triton.tile_shape` - Tile Geometry

- Triton addition: tile geometry when not specifically MMAC-focused.
- Trigger: tile dimensions interact with MMAC instruction selection, LDS usage,
and layout conversion overhead, but the bottleneck is not clearly MMAC shape
alone.
- Implement: tune `BLOCK_M`, `BLOCK_N`, `BLOCK_K` as a config
method when the primary effect is on tile geometry rather than MFMA instruction
selection per se.
- Evidence: accepted config, active_config, timing.

### P9: `triton.cache_policy_buffer_ops` - Cache Policy / Buffer Ops

- HIP analogue: `memory.cache_policy_glc_slc`.
- Trigger: cache policy affects streaming/reused memory, or L1 set conflicts are
suspected on supported HCU buffer-op paths.
- Implement: branch explicit `tl.load` / `tl.store` cache policy values, for
example load `cache_modifier=".cg"` / `.ca` / `.cv`, store `.cg` / `.cs` /
`.wt`, and `eviction_policy="evict_first"` / `"evict_last"`. For L1 set-conflict
cases, try `TRITON_BUFFER_CACHE_SWIZZLE=1` only as a measured compile-time
branch; it requires buffer ops and is not a per-kernel source feature.
- Evidence: source/config shows the chosen cache policy and TTGIR/AMDGPU-dialect
IR shows the expected modifier, e.g. `cacheModifier = cg`; final AMDGCN cache
bits such as `glc` / `slc` are supporting evidence. For cache swizzle, check
`.ttgir` AMDGPU-dialect `amdg.buffer_*` ops for generated `stride = ...`; final
AMDGCN alone is not enough. Timing must improve.

### P10: `triton.epilogue_fusion` - Epilogue / Post-Op Fusion

- HIP analogue: `memory.epilogue_fusion`.
- Trigger: store followed by separate post-op kernel or global round trip.
- Implement: fuse bias, activation, scale, cast, or store transform into the
Triton kernel.
- Evidence: removed kernel/global round trip, correctness, timing.

### P11: `triton.block_size` - Memory Block Size Tuning

- HIP analogue: part of `memory.coalesced_access` and
`memory.vectorized_global_access`.
- Trigger: memory-bound elementwise/reduction kernels.
- Implement: tune `BLOCK_SIZE`, `num_warps`, `tl.arange` vector shape, and
aligned main/tail mask split.
- Evidence: accepted config, correctness, timing.

## Latency Axis

### P1: `triton.num_stages_pipeline` - Software Pipeline Stage Count

- HIP analogue: `latency.waitcnt_pipeline`.
- Trigger: a hot `for` loop with load/compute overlap has memory latency or
pipeline bubbles; too few/many stages hurt timing. Without such a loop,
`num_stages` has no effect.
- Implement: tune `num_stages`, `BLOCK_*` tile sizes, and live ranges together.
- Evidence: active config plus before/after timing and resource pressure. Wait
or stall counters are optional supporting evidence; the mere presence of
`s_waitcnt`, `ttg.async_wait`, or similar wait ops is not proof of a successful
stage-count change.

### P2: `triton.ilp_unroll` - ILP / Unroll via `tl.static_range`

- HIP analogue: `latency.ilp_unroll`.
- Trigger: issue slots idle with low register pressure; independent operations
can be overlapped.
- Implement: convert `for i in range(N)` to `for i in tl.static_range(N)` to
force the compiler to unroll the loop aggressively, increasing ILP. Monitor
register pressure because aggressive unroll may cause spills. Not controllable
via config parameters; requires source-level change.
- Evidence: lower loop overhead, higher instruction-level parallelism, timing,
resource usage.

### P3: `triton.barrier_scope_reduction` - Barrier and Sync Reduction

- HIP analogue: `latency.reduce_barrier`.
- Trigger: source has explicit `tl.debug_barrier` / mbarrier use, or TTGIR/ISA
shows hot-path waits generated by async copy, `tl.matrix_load`, or pipelined
loops.
- Implement: remove only proven-unnecessary explicit barriers; otherwise reduce
generated waits by changing source structure, `num_stages`, matrix-load/async-copy
use, or loop tiling. Do not treat ordinary `tl.load` / `tl.dot` as a manual
barrier-control surface.
- Evidence: before/after TTGIR/ISA counts show fewer hot-path barriers or waits,
with correctness and timing. Barrier-like ops alone are only an opportunity
signal.

### P4: `triton.split_k_streamk` - Split-K / Stream-K

- HIP analogue: `latency.split_k_streamk`.
- Trigger: large K or poor CU utilization.
- Implement: split the K dimension in the launch grid/config, write partial
accumulators to a split-major partial buffer, then launch a dedicated Triton
sum/reduce kernel to produce the final output. Use Stream-K-style tile
scheduling only when source/config proves the partitioning; do not use
`tl.atomic_add` as the default reduction path.
- Evidence: source/config proves split-K or Stream-K-style partitioning, partial
buffer layout, and the dedicated reduction kernel; reduction correctness is
preserved and timing/tail latency improves. Atomic or wait instructions are not
proof of this method.

### P5: `triton.persistent_programs` - Persistent Scheduling

- HIP analogue: `latency.persistent_scheduler`.
- Trigger: many tiny tiles, grouped GEMM/MoE/attention decode, or work
distribution overhead.
- Implement: persistent `tl.program_id` work queues, grouped tile traversal, or
finite grouped config strategy.
- Evidence: source/grid mapping or scheduler state proves persistent work
assignment, then occupancy/tail-balance and timing improve. Atomics or extra
looping in ISA are supporting context only and do not prove persistence by
themselves.

## Required Practices

### `triton.shape_family_workflow` - Shape-Family Split Before Axis Tuning

- Required when benchmark shapes are numerous or a key dimension spans widely.
- Keep at most three families: `small`, `middle`, `large`. Generate
`shape_family_plan.json`, run the normal single-shape workflow separately for
each representative family, then merge the family champions.
- Each family must do its own bounded autotune, fixed-config benchmark/profile,
method selection, and correctness/timing proof.
- Before starting the next family, inspect the previous family champion. For
ordinary source/config improvements, the same kernel may still be usable or
worth borrowing; let the agent decide based on correctness, fixed-config timing,
and IR/profile evidence. Do not blindly carry over algorithmic scheduling
changes such as Split-K or Stream-K.
- Final merge: use runtime config dispatch when the implementation is shared but
configs differ; use runtime variant dispatch when implementations differ. If one
implementation/config wins all families, prove that with per-family final bench
records.
- Evidence: `shape_family_plan.json`, per-family run dirs and final benches, and
`dispatch_manifest.json` covering every required family.

### `triton.runtime_config_key` - Runtime Config Dispatch

- Required when one config cannot serve all shape/dtype/layout families.
- Do not claim it as a standalone compute/memory/latency method in
`methods.json`; attribute the speedup to the carried method, such as tile shape,
program geometry, split-K, cache policy, or layout.
- Implement: finite registry keyed by arch, dtype, shape family, layout, and
role; never generate one config per arbitrary shape.
- Evidence: accepted configs with shape guards, fallback, and fixed-config
benchmark/profiling records for the carried method.

## Operator-Specific Shortcuts

- Elementwise / copy / vector add: start with `triton.coalesced_load_store`,
`triton.mask_simplification`, `triton.vectorized_load_store`,
`triton.async_copy_global_to_lds` when non-MMAC global-to-LDS staging applies,
and `triton.block_size`.
- GEMM / attention matmul / MoE: start with `triton.dot_mmac_shape`, then
`triton.mask_simplification`, `triton.matrix_ds_mls`,
`triton.low_precision_fp8_bf8`, `triton.program_geometry_occupancy`, and
`triton.persistent_programs`.
- Attention decode / paged attention: prioritize finite config registries,
KV/cache layout, `triton.matrix_ds_mls` when matrix-core loads or register
pressure matter, vectorized cache loads, split-K, online softmax/reduction, and
low precision only with explicit scale/tolerance evidence.
