# Iteration {{iter}} - Analysis

**Kernel profiled (input)**: `{{best_file_before}}`
**Time before**: {{best_ms_before}} ms
**GPU / arch**: {{gpu_name}} / {{gfx_arch}}

---

## Local KB Evidence

- **Evidence file**: `{{kb_evidence_path}}` (`kb_evidence.md/json` or `kb_unavailable.json`)
- **KB status**: {{kb_status}} (ok / unavailable / failed / degraded)
- **Queries used**: {{kb_queries}}
- **Source-backed references**: {{kb_source_refs}}
- **Claims adopted**: {{kb_claims_adopted}}
- **Unresolved gaps**: {{kb_unresolved_gaps}}

_If KB is unavailable, say so plainly and do not mark Hygon/Triton architecture, lowering, or config choices as KB-backed._

---

## Kernel Computation Logic

_For `iterv1`, write this section during the Semantic Pre-Pass after `orchestrate.py setup` and before initial config tuning. In later iterations, carry it forward from the current champion or write a delta when semantics, shape family, layout contract, or IR/profile evidence changes. Make it read like a short paper method section: define tensor roles and shapes, then write the mathematical formula for each output. This is operator meaning, not Triton tile details or a Python reference dump._

### Tensor Roles And Shapes

_List inputs, outputs, dtype/stride/layout assumptions, and the reduction or contracting axes._

### Mathematical Definition

_Use explicit formulas, for example `scale[row] = max(abs(x[row, :])) / dtype_max` and `q[row, col] = cast(x[row, col] / scale[row])`, or `C[m,n] = sum_k A[m,k] * B[k,n]`._

## Formula-First Analysis

_Write one or two serious semantic rewrite candidates, plus the important rejected/deferred ideas. Explain the formula reason, not just the Triton tile diff. Note whether `references/triton_optimization_memory.md` had a direct match, useful analogy, negative guard, or no relevant entry._

## Loop / Candidate Inventory

_Only discuss loops that affect the algorithmic decision. Say which loops are real reductions/maps/scans and which are implementation bookkeeping from the current program mapping. State the best first implementation target._

## Semantic Pre-Pass Result

- **Promoted semantic rewrite**: _name or `none`_
- **Historical case review**: _matched / inspiring / rejected entries and why, or `none`_
- **Rejected/deferred candidates**: _short reason_
- **Timeline recording**: _`record_attempt.py` event path/status, or `not applicable`_

---

## Shape Family / Config Prepass

_If `shape_family_plan.json` is required, state the current family (`small` / `middle` / `large`), representative dims, family guard, and the per-family autotune result used as the fixed active config. For later families, say whether a previous family champion was reused, partially borrowed, or rejected, and why. If no family split is required, say `single-shape workflow`._

_Tuning space: state whether the agent wrote `tuning_space.json` or used the automatic `tune_configs.py --search-level broad` sweep. List tunable keys accepted by `setup()` / `_config()` / `DEFAULT_CONFIG`, candidate ranges, shape/dtype/layout guards, and any excluded keys with reasons._

_For the final tuning iteration, mark it explicitly as `final_tune=true`. State why it was required, which prior source rewrite/config/branch made earlier tuning stale, whether `--promote-if-better` updated `state.best_config`, and where `tune_results.json` / `accepted_configs.json` are stored._

---

## Roofline Analysis (from `roofline.json`)

| Axis | delta (gap) | Utilization | Budget |
|------|-------------|-------------|--------|
| Compute | {{delta_compute}} | {{compute_util_pct}}% | {{budget_compute}} |
| Memory | {{delta_memory}} | {{memory_util_pct}}% | {{budget_memory}} |
| Latency | {{delta_latency}} | max stall {{max_stall_pct}}% | {{budget_latency}} |

**Primary bound**: {{bound}}

If any utilization field is `n/a` or `roofline.json.degraded=true`, do not
claim peak-utilization progress from this table. Use the `notes` field from
`roofline.json` and cite raw PMC counters only as raw counters, not as
percentages.

---

## Top HCU Metrics (from `hcu_top.json`)

### Compute
{{compute_metrics_table}}

### Memory
{{memory_metrics_table}}

### Latency / Stalls
{{latency_metrics_table}}

---

## Diagnosis

_Which axis is the dominant bottleneck right now? Cite specific hipprof/PMC/SQTT values. Explain how the roofline budget allocation reflects this diagnosis. If profiler evidence is degraded, say so._

## Chosen Methods

For each method, state: (a) priority level from the catalog, (b) HCU metric, Triton cache IR, dccobjdump, or local KB/source-backed evidence, (c) the exact implementation delta vs. current best, and (d) expected metric shift.

### {{axis_1}} - `{{method_1_id}}` (Priority: {{P_level_1}})
- **Budget for this axis**: {{budget_axis_1}}
- **Priority scan**: _List higher-priority methods that were scanned and why each was skipped._
- **Trigger evidence**: _(cite specific HCU metric / ISA evidence)_
- **KB/source evidence**: _(cite local KB finding or say unavailable/degraded)_
- **Method**:
- **Delta vs current best**:
- **Expected metric shift**:
- **Risks / coupling**:

### {{axis_2}} - `{{method_2_id}}` (Priority: {{P_level_2}})
- **Budget for this axis**: {{budget_axis_2}}
- **Priority scan**: _List higher-priority methods scanned and skip reasons._
- **Trigger evidence**:
- **KB/source evidence**:
- **Method**:
- **Delta vs current best**:
- **Expected metric shift**:
- **Risks / coupling**:

### {{axis_3}} - `{{method_3_id}}` (Priority: {{P_level_3}})
_(Only if a third method is selected; omit if the relevant axis budget is 0.)_
- **Budget for this axis**: {{budget_axis_3}}
- **Priority scan**:
- **Trigger evidence**:
- **KB/source evidence**:
- **Method**:
- **Delta vs current best**:
- **Expected metric shift**:
- **Risks / coupling**:

## Orthogonality Check

_Verify: (1) no pair is the same optimization under two names, (2) coupled pairs are counted once when they are the same code delta, (3) all methods are arch-compatible, (4) axis distribution matches roofline budget, and (5) Hygon/Triton-specific assumptions are backed by KB/source evidence or explicit IR/ISA proof._

## Excluded Candidates

_List every higher-priority method on each axis that was not selected, with the exact reason._

- `triton.dot_mmac_shape` (P1) - skipped: kernel is pure elementwise, no matmul semantics

## Branch Variants

_Describe the K hyperparameter variants generated for branch-and-select._

| Branch | Tile (MxNxK) | Stages | Wave/block shape | Other diff |
|--------|--------------|--------|------------------|------------|
| b1 | 128x128x32 | 3 | 256 threads | n/a |
| b2 | 128x256x32 | 3 | 256 threads | n/a |
| b3 | 256x128x32 | 4 | 512 threads | n/a |
| b4 | 128x128x64 | 5 | 256 threads | n/a |

---

## Result (filled after benchmarking)

- **Champion branch**: b{{champion_idx}}
- **New ms**: {{new_ms}}
- **Speedup vs previous best**: {{speedup_vs_best_before}}
- **Speedup vs reference**: {{speedup_vs_ref}} (N/A unless `benchmark.py --bench-reference` is used)
- **Validation**: {{validation_status}}
- **Retries needed**: {{retries}}
- **Outcome**: {{outcome}} (improved / regressed / failed_validation)

### Attribution (from ablation)

| Method | Ablated ms | Attribution ms | Contributed? | HCU ISA verified? |
|--------|------------|----------------|--------------|-------------------|
| {{m1_id}} | {{m1_ablated_ms}} | {{m1_attr_ms}} | {{m1_contributed}} | {{m1_isa}} |
| {{m2_id}} | {{m2_ablated_ms}} | {{m2_attr_ms}} | {{m2_contributed}} | {{m2_isa}} |
| {{m3_id}} | {{m3_ablated_ms}} | {{m3_attr_ms}} | {{m3_contributed}} | {{m3_isa}} |

### Post-Hoc vs Expected

_Did the metric shift match the prediction? If not, why?_

_Did attribution confirm the methods expected to be effective?_

_This note becomes part of the final retrospective._
