# Finalization And Reporting

Use this file before final response for an optimization run. Finalization is a delivery gate, not background guidance.

## Final Tuning

Run a final tuning iteration when the kernel body or best candidate changed:

- If any iteration promoted a faster source rewrite, config, branch, or shape bucket, open a final tuning iteration, normally `iterv{last+1}`, and run `tune_configs.py --search-level broad --max-configs 64 --final-tune --promote-if-better` on the current champion before `orchestrate.py finalize`.
- Preserve `iterv{final}/tune_results.json`, `accepted_configs.json`, `config_acceptance.md`, and `attempt_timeline.json`.
- If the sweep finds a faster valid config, `--promote-if-better` writes it to `state.best_config` and `iterv{final}/config.json` so `final_kernel.py` bakes the retuned config.
- If no iteration improved over the initial champion and an initial config sweep was already run, the final tuning iteration may be skipped. Record the skip reason in `summary.md`.
- Keep final tuning on an idle/exclusive card when possible, fixed to the same benchmark shapes and correctness contract used for champion comparison.
- `ref.py` is a Python-callable correctness oracle only. Its `reference()` may use PyTorch, Triton, HIPC, or another backend wrapped behind Python. `benchmark.py` skips reference timing by default; final timing in `summary.md` is kernel-only unless you explicitly used `--bench-reference`.
- `orchestrate.py finalize` checks this by default and stops with a suggested `tune_configs.py` command when final tuning is required but absent. Use `--skip-final-tune-check` only with an explicit skip reason in `summary.md`.

## Finalization Writes

Finalization should write:

- `final_kernel.py`: champion kernel with tuned `DEFAULT_CONFIG`.
- `final_config.json` and `final_kernel_manifest.json`: exact baked config and provenance.
- `iterv*/kb_evidence.json` plus `iterv*/kb_evidence.md`, or `iterv*/kb_unavailable.json`.
- `iterv*/irs/best_input/<cache-key>/`: baseline Triton cache directory including `.ttir`, `.ttgir`, `.amdgcn`, and `.hsaco` when generated.
- `iterv*/irs/kernel/<cache-key>/`: optimized/champion Triton cache directory for the fixed champion config.
- `iterv*/attempt_timeline.json`: chronological branch/config attempt events, including successes and failed or not-promoted trials.
- `iterv{final_tune}/tune_results.json`, `accepted_configs.json`, and `config_acceptance.md` when final tuning was required.
- `attempt_timeline.svg`: final visual timeline linked or object-embedded from `summary.md`; each attempt point must expose hover details inside the SVG.
- Optional `references/triton_optimization_memory.md` entry when the run produced a reusable similar pattern or semantic rewrite with evidence.
- For multi-shape, multi-case, or shape-family work, case-root delivery artifacts:
  `optimization_summary.md`, `optimized_kernel.py` or `final_kernel.py` dispatcher,
  `optimized_config.json`, `final_bench.json`, `final_kernel_manifest.json`,
  `attempt_timeline.json`, `attempt_timeline.svg`, and `irs/final_cache/`.
  The case-level summary is the human-facing overview; per-run `summary.md`
  files remain the detailed evidence records.

## Finalize Gate

Do not send the final response until this checklist has passed or each missing item has a recorded failed attempt plus degraded-evidence note:

1. If required, run final tuning on the current champion and let `--promote-if-better` update `state.best_config` before generating `final_kernel.py`.
2. Rerun the champion with the fixed final config and record correctness plus timing.
3. Run `profile_hcu.py` for the final champion. Prefer `xcu`/XCompute when available and fall back to `hipprof` only when `xcu` is missing or fails. For Python/Triton kernels, xcu uses default `-K` filtering (see `hcu_top.json` `xcu_kernel_filter`); override with `--kernel-name` if needed.
4. Use profiler/device-counter evidence as the primary source for hardware-facing metrics such as memory bandwidth, compute utilization, occupancy, HBM traffic, L2 cache hit rate, and TFLOPS.
5. Capture Triton cache IRs for the final champion into `irs/final_cache/` with a fixed `TRITON_CACHE_DIR`; include `.ttir`, `.ttgir`, `.amdgcn`, and `.hsaco` when Triton generated them.
6. Generate or update `attempt_timeline.json` and `attempt_timeline.svg`; link or object-embed the SVG from `summary.md`. Do not replace it with PNG/JPEG. Each point in the SVG must provide hover information for attempt number, iter, candidate, timing, result, outcome, and methods.
7. Write `summary.md` primarily in Chinese. The opening `## 概要` section must start with a compact metrics table whose columns are `shape`, `baseline`, `best`, `speedup`, `final config`, and `xcu 利用率`; the reader should grasp the outcome immediately without scrolling. All explanatory text should be concise and avoid redundant boilerplate.
8. For multi-shape, multi-case, or shape-family work, synthesize a case-level
   `optimization_summary.md` before the final response. It must open with a
   compact comparison table for all final shapes/cases (command or case name,
   baseline, best/final verify, speedup, active config, correctness, compute%,
   memory%, HBM bandwidth) and then point to each run's detailed `summary.md`.
   Also write the case-root dispatch/packaging artifacts needed by
   `final_validate.py`.
9. Review final promoted changes for reusable Triton optimization memory. Append only compact, equivalent, evidence-backed reusable patterns; otherwise state why no memory entry was added. `summarize.py` may emit `not_appended_by_summarize` as a provisional status; final review must replace it with `appended` or `not_appended` plus the reason.
10. Verify the IR tree locally and, when remote execution was used, verify remote and pulled-back local copies match for required deliverables.
11. If any required item is missing, first attempt the step and save command output or logs. Then add a `degraded_evidence` entry explaining the failed attempt and why the final answer is still useful.

## Metric Honesty

`triton.testing.do_bench` or CUDA/HIP event timing is acceptable for `latency_us_event` and same-script relative comparisons. Do not present `GB/s`, `TFLOPS`, `compute%`, or `memory%` derived only from logical bytes/FLOP counts divided by event time as profiler truth. Label them as `logical GB/s`, `estimated TFLOPS`, or `estimated memory%`, and state that they are not profiler hardware counters.

If both `xcu` and `hipprof` are unavailable or fail, mark hardware-utilization evidence degraded rather than claiming precise utilization. When `xcu` is available, collect and report L2 cache hit rate from `hcu_top.json` / `roofline.json`. If `xcu` is unavailable and hipprof lacks stable L2 fields, write `n/a` and add the xcu installation hint instead of guessing.

## Minimal Self-Check

```bash
test -f final_kernel.py
test -f summary.md
test -f attempt_timeline.json
test -f attempt_timeline.svg
find irs/final_cache -type f \( -name '*.ttir' -o -name '*.ttgir' -o -name '*.amdgcn' -o -name '*.hsaco' \) | head
grep -q "## 最终 Kernel 快照与指标" summary.md
grep -q "## 算子计算逻辑" summary.md
grep -q "## 尝试时间线" summary.md
grep -q "## 知识沉淀" summary.md
# For multi-shape/multi-case delivery from a case root:
test -f optimization_summary.md
grep -q "## 最终 Kernel 快照" optimization_summary.md
grep -q "## 最终指标" optimization_summary.md
test -f optimized_config.json
test -f final_bench.json
# When the champion uses TF32 tl.dot:
grep -q "TF32 精度提醒" summary.md
```

When final tuning was required, `state.json` must contain a `final_tune` record. If it was intentionally skipped, `summary.md` / Retrospective must name the skip reason.

## Summary Requirements

The final `summary.md` must include:

- `## 概要` (executive summary) as the first section after the title: a one-row headline table with shape, baseline time, best time, overall speedup, final config, and xcu compute/memory utilization, followed by 1-2 short conclusion sentences;
- why optimization stopped: near-peak, no-improvement branches/sweeps, correctness/compile blocker, profiler inconclusive, or user/budget stop;
- final tuning iteration status: required and completed/promoted, completed with no promoted config, or explicitly skipped with reason;
- `## 最终 Kernel 快照与指标` with final kernel path, source kernel path, shape/dims, machine/GPU/arch/CU count, toolchain/profiler environment, final timing, active config, rough benchmark bandwidth, hardware HBM bandwidth, L2 cache hit rate when available, resource metrics, and links to final bench/profile/roofline artifacts;
- compute or memory utilization only when `roofline.json` marks `utilization_reliable=true`; otherwise write `n/a` plus the degraded-evidence note from `roofline.json.notes`;
- `## 算子计算逻辑` immediately after the final snapshot/metrics section, explaining tensor roles, shape assumptions, and explicit mathematical formulas. Do not include `Python Reference Form` or long executable reference dumps in final `summary.md`;
- multi-case or shape-bucketed results should be included in the snapshot/metrics section as additional rows or a compact per-case table, not as a separate verbose metrics dump;
- for multi-shape or multi-case tasks, a case-root `optimization_summary.md`
  that is short enough to read first: it must compare all shapes in one table,
  include the command/case names, final configs, correctness, best/final timing,
  speedup, compute/memory utilization, and links to per-run summaries/artifacts;
  do not make users open every run directory to understand the overall result;
- promoted changes inside successful iterations and attempted branches/sweeps that were not promoted;
- whether a reusable optimization-memory entry was appended to `references/triton_optimization_memory.md`, or why no entry was added;
- `## 尝试时间线` with a linked/object-embedded `attempt_timeline.svg` plus the table; **config sweep entries from the same iteration must be consolidated into a single row** (showing the best config's timing and whether any config beat the previous best), not one row per individual config. The SVG must keep hover details on each attempt point;
- semantic rewrites and the config tuning sweeps that follow them must be recorded in `attempt_timeline.json` with `kind: "semantic_rewrite"` and `kind: "config_tune"` respectively, so the timeline accurately reflects all optimization steps — not just branch exploration;
- `## 知识沉淀` stating whether `references/triton_optimization_memory.md` was appended. If appended, cite the entry title/number and the evidence. If not appended, state whether the reason was lack of reusable pattern, lack of proof/timing, or case-specific behavior;
- `## Torch Inductor AOT Feedback` when the input kernel was generated by Torch Inductor, AOTInductor, or `torch.compile`/AOT;
- degraded evidence such as missing KB, missing Triton cache IRs, missing ISA proof, unreliable utilization counters, or manual/ad-hoc workflow recovery;
- if the final champion uses `input_precision="tf32"` on f32 `tl.dot`, a prominent `## TF32 精度提醒` immediately after `## 概要`, with final correctness `passed`, `atol`, and `rtol`.
