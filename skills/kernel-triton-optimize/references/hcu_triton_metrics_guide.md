# HCU Triton Metrics Guide

Use this guide to translate timing, profiler, Triton cache, and ISA evidence
into `triton_method_registry.json` methods. Prefer `xcu`/XCompute when it is
available. If `xcu`, `hipprof`, PMC, SQTT, or `dccobjdump` is unavailable, keep
the benchmark result but mark profile/ISA evidence degraded or inconclusive.

## Evidence Sources

- `bench.json`: fixed-config timing, active config, config source, speedup.
- `tune_results.json` / `accepted_configs.json`: fixed-config tuning sweep result.
- Triton cache: `.ttir`, `.ttgir`, LLVM/AMDGCN text, metadata, `.hsaco`.
- `xcu profile -S memory_workload,speed_of_light,compute_workload -F csv -K <substring>`:
  preferred hardware evidence for HBM bandwidth (`L2_Fabric-Rd/Wr BW`), compute
  utilization, L2/VL1 hit rates, coalescing, LDS conflict, and stalled-on-L2
  signals. `profile_xcu.py` passes `-K` automatically from the first two tokens
  of the first `@triton.jit` function name (e.g. `chunk_kda`); override with
  `--kernel-name` or disable with `--no-kernel-filter`. Recorded in
  `hcu_top.json` as `xcu_kernel_filter` and `selected_kernel`. xcu does not
  expose HBM peak GB/s or peak-normalized utilization; use `hbm_bandwidth_gbs`
  directly instead of dividing by a hardcoded roof.
- `hipprof --pmc --pmc-type 3`: fallback PMC evidence when `xcu` is unavailable
  or fails. hipprof has no `-K`-style kernel filter; expect noisier dispatch lists
  than xcu when many kernels run in the same process.
- `hipprof --sqtt`: stall triage for unclear regressions or late iterations.
- `dccobjdump`: final ISA/resource proof when code objects are available.

## Preferred xcu Signals

| xcu signal | Why it matters for Triton kernel optimization |
|------------|-----------------------------------------------|
| `L2_Fabric-Rd BW` + `L2_Fabric-Wr BW` | Hardware HBM-facing bandwidth; use it instead of logical bytes/time when deciding whether a kernel is truly bandwidth-bound. |
| `L2-Hit Rate` | Distinguishes streaming HBM pressure from reuse-friendly kernels that miss compute, layout, or latency optimization. |
| `VL1-Hit Rate` and `VL1-Util` | Shows whether vector L1 is feeding lanes efficiently or whether access pattern/config changes are needed. |
| `VL1-Buffer Coalescing` | Direct evidence for coalescing quality; useful for offset layout, mask simplification, vectorized load/store, and block-size decisions. |
| `VL1-Stalled on L2 Data` | Points to memory latency or cache-miss waiting even when aggregate bandwidth is not high. |
| `LDS-Bank Conflicts/Access` / `LDS-Bank Conflict Rate` | Helps detect LDS/layout conversion pressure around dot/layout-heavy kernels. Treat it as diagnostic evidence, not a standalone Triton method unless the source/IR change can affect LDS layout. |
| `TA-Busy` / `TD-Busy` and derived load/store efficiency | Helps separate address generation, load/store issue pressure, and request amplification from HBM saturation. |
| `IL1-Hit Rate` and `VL1_UTCL1-Hit Ratio` | Useful context for instruction/cache or address-translation effects in small, branchy, or launch-latency-sensitive kernels. |

## Bottleneck Signals


| Signal                                                                     | Likely methods                                                                                                            |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Low compute utilization, matmul/attention/MoE semantics, weak dot lowering | `triton.dot_mmac_shape`, `triton.matrix_ds_mls`                                                                 |
| gfx938+ FP8/BF8 opportunity with explicit tolerance/scales                 | `triton.low_precision_fp8_bf8` (FP8/BF8 sub-path)                                                                         |
| gfx928+ f32 matmul, Triton `tf32` dot support, TF32 branch passes ref      | `triton.low_precision_fp8_bf8` (TF32 sub-path)                                                                            |
| Predicate/bounds/mask arithmetic dominates simple compute                  | `triton.mask_simplification`, `triton.fast_math_lowering`                                                                 |
| Low CU activity or poor latency hiding                                     | `triton.program_geometry_occupancy`, `triton.num_stages_pipeline`, `triton.persistent_programs`, `triton.split_k_streamk` |
| Too much or too little work per lane/program                               | `triton.work_granularity`, then check `triton.program_geometry_occupancy` and `triton.register_pressure_control`   |
| High VGPR/SGPR or spills                                                   | `triton.work_granularity`, `triton.register_pressure_control`, with tile/stage reductions                          |
| High memory traffic or low rough bandwidth                                 | `triton.coalesced_load_store`, `triton.mask_simplification`, `triton.vectorized_load_store`, `triton.block_size`, `triton.layout_stride_transform` |
| Reused operands repeatedly loaded from global                              | `triton.async_copy_global_to_lds`, `triton.matrix_ds_mls`, `triton.num_stages_pipeline`                             |
| LDS or matrix layout stalls/conflicts                                      | `triton.matrix_ds_mls`, `triton.layout_conversion_optimization`                                                 |
| Heavy LDS traffic from blocked→dot_op layout conversion                    | `triton.layout_conversion_optimization`, `triton.matrix_ds_mls`                             |
| Separate post-op kernel or output round trip                               | `triton.epilogue_fusion`                                                                                                  |
| Too many barriers/waits or wait bubbles                                    | `triton.num_stages_pipeline`, `triton.barrier_scope_reduction`                                                            |
| Scalar address/mask overhead, hot aligned loads/stores still masked        | `triton.mask_simplification`                                                                                              |
| Converted TTGIR lacks expected `amdg.buffer_load` / `amdg.buffer_store`    | `triton.mask_simplification`, `triton.coalesced_load_store`, `triton.cache_policy_buffer_ops`                            |
| Scalar `buffer_load/store_dword` where x2/x3/x4 is expected                | `triton.vectorized_load_store`, `triton.mask_simplification`, `triton.block_size`                                         |
| Shape families need different winning configs                              | required `triton.runtime_config_key` dispatch; attribute speedup to the carried method such as `triton.tile_shape`        |
| Exp/log/div/sqrt dominates                                                 | `triton.fast_math_lowering`                                                                                               |
| Cache policy affects streaming or reused memory                            | `triton.cache_policy_buffer_ops`                                                                                          |


## Interpretation Rules

1. Separate autotune/config gains from algorithmic method gains. A faster
   `BLOCK_SIZE` or `num_warps` is valid, but do not attribute it to MMAC, MLS,
   or barrier reduction unless IR/ISA evidence shows that change.
   For `triton.coalesced_load_store`, do not treat `tt.load`/`tt.store` in
   TTGIR as coalescing proof; use ISA (when available), timing/bandwidth, and
   source offset layout.
2. Do not claim `triton.lds_bank_conflict` — Triton shared/LDS layouts are
   compiler-chosen; LDS bank conflict is not a practical standalone Triton
   optimization axis on HCU (use HIP skill or manual SQTT triage only).
3. For matrix methods, require the full chain where possible: Triton config or
   source change, cache IR (`.ttgir`), final ISA/resource evidence,
   correctness, and timing.
4. For config-only methods, ISA may be optional. Require fixed config,
   reproducible timing, and cache directories for baseline/champion.
5. For cache-policy work, record cache-invalidating environment variables such
   as `AMDGCN_USE_BUFFER_OPS`, because they can create different Triton cache
   directories and codegen.
6. For `triton.mask_simplification`, separate the evidence stages: TTIR or
   pre-buffer-op IR proves the hot `tt.load` / `tt.store` mask was removed or
   made all-true; converted TTGIR proves whether the op became
   `amdg.buffer_load` / `amdg.buffer_store`; final ISA proves the emitted
   buffer/global instruction family when relevant. When the method is selected
   for Compute Axis, memory-op changes are optional; require before/after
   reduction in predicate, bounds, compare, select, or mask-construction
   arithmetic plus correctness and timing.
7. For `triton.vectorized_load_store`, check the AxisInfo chain before blaming
   the backend. The contiguity/divisibility/mask-constancy claim may come from
   source expressions, ASTSource attrs, explicit Triton hints, or debug pass
   logs; do not require those attrs to be printed in final TTGIR. Converted
   TTGIR should show `amdg.buffer_load` / `amdg.buffer_store` when buffer ops
   are expected; final ISA should show wider dwordx2/x3/x4 or 64/128-bit memory
   forms. `tt.pointer_range=32` and int32-safe offsets are useful only when the
   pointer range contract makes them correct.
8. If counters are empty, do not fabricate conclusions. Use timing plus
   generated IRs and write an explicit degraded note.
9. Do not treat raw PMC event counts as utilization percentages. Metrics such
   as `GRBM_GUI_ACTIVE`, `TA_TA_BUSY[*]`, `TCP_TOTAL_CACHE_ACCESSES`, and
   `SQ_WAIT_*` may be raw counts in hipprof CSV output; values larger than
   `100` are not "more than 100%" and must not be divided by 100 or clamped.
   Only claim compute or memory utilization when the metric is explicitly a
   percent/fraction, or when a valid numerator and denominator are both present
   (for example busy cycles divided by total cycles). Otherwise leave
   `compute_util_pct` / `memory_util_pct` as `n/a`, mark roofline evidence
   degraded, and use benchmark-visible logical GB/s as a separate, clearly
   labeled throughput signal.
