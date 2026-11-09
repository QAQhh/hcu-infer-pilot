# Example Walkthrough (Hygon Triton, Fixed Config, KB-Aware)

This is a Triton optimizer runbook. The agent uses the local skill instructions and local KB query results to decide what to write; the selected HCU runtime target only runs the runtime validation bundle. The target may be a remote machine/container, a local container, or the current shell.

## Layout Before The Run

```text
<case-dir>/
|-- kernel.py   # exposes setup(**kwargs) and run_kernel(...) — optimization target
`-- ref.py      # exposes reference(...) — Python-callable correctness oracle
```

`orchestrate.py` defaults to `scripts/benchmark.py`: runs `reference()` once, times only `kernel.py`.
Pass `--bench-reference` when you need reference latency or `speedup_vs_reference`.
`reference()` may use pure Python/PyTorch, Triton, HIPC, or another backend wrapped behind Python.

`kernel.py` should report the fixed config used by each benchmark:

```python
DEFAULT_CONFIG = {"BLOCK_SIZE": 1024, "num_warps": 4, "num_stages": 1}

def setup(**kwargs):
    cfg = dict(DEFAULT_CONFIG)
    cfg.update(kwargs.get("config") or {})
    return {
        "inputs": {...},
        "outputs": ["out"],
        "kernel_kwargs": cfg,
        "active_config": cfg,
        "config_source": "fixed" if kwargs.get("config") else "baseline",
        "config_key": kwargs.get("config_key", ""),
        "config_hit": bool(kwargs.get("config")),
    }
```

## Local Agent Step: KB Evidence

Run the KB evidence helper on the local agent/control host before writing `methods.json`, branch configs, or branch kernels:

```bash
python <runtime-tools>/scripts/query_kb.py \
  --out-dir <run-dir>/iterv1 \
  --iter 1 \
  --target-arch <detected-gfx-arch> \
  --op-kind memory \
  --dims '{"N":16777216}' \
  --context "memory-bound vector add, tuning BLOCK_SIZE/num_warps/num_stages"
```

If the local KB is unavailable, the helper must not block the run. It writes:

```text
iterv1/
|-- kb_unavailable.json
`-- kb_warning.txt
```

The iteration is then KB-degraded. Do not claim Hygon/Triton architecture, codegen, config, or method-selection guidance is KB-backed unless it is separately proven by source, Triton cache IRs, or `dccobjdump`.

## Remote Runtime Step: Setup

Run the runtime tools in the target HCU environment:

```bash
python <runtime-tools>/scripts/orchestrate.py setup \
  --baseline ./kernel.py \
  --ref ./ref.py \
  --dims '{"N":16777216}' \
  --iterations 3 \
  --branches 2 \
  --warmup 5 \
  --repeat 10
```

`check_env.py` records Triton-first runtime information in `env.json`, including:

- Python version
- PyTorch wheel version
- Triton wheel version
- Triton active target, for example `GPUTarget(backend='hip', arch='gfx938', warp_size=64)`
- Triton cache directory and cache-affecting environment variables
- optional low-level tools such as `hipprof`, `dccobjdump`, and `hipcc`

If `hipprof` or `dccobjdump` is unavailable, profiling and ISA checks are degraded/inconclusive, but benchmark correctness and timing can still prove the workflow.

## Local Agent Step: Semantic Pre-Pass

After setup creates the run directory and before the initial tuning sweep, write the analysis output requested by `references/triton_semantic_prepass.md` in `iterv1/analysis.md`: `Kernel Computation Logic`, `Formula-First Analysis`, `Loop / Candidate Inventory`, and `Semantic Pre-Pass Result`. Use `references/triton_optimization_memory.md` for historical case review: direct matches, analogous inspiration, negative guards, and reusable semantic rewrites. If this produces a source-changing candidate, record it before `tune_configs.py`:

```bash
python <runtime-tools>/scripts/record_attempt.py \
  --run-dir <run-dir> \
  --iter 1 \
  --kind semantic_rewrite \
  --candidate "<rewrite name>" \
  --status pending \
  --outcome candidate_created_before_validation \
  --analysis <run-dir>/iterv1/analysis.md
```

Only map a semantic rewrite to a compute/memory/latency method when it also has a hardware-axis effect.

## Iteration Loop

For each iteration:

1. Run the broad fixed-config tuning sweep after the semantic candidate is fixed:

```bash
python <runtime-tools>/scripts/tune_configs.py \
  --state <run-dir>/state.json \
  --iter 1 \
  --op-kind memory \
  --search-level broad \
  --max-configs 64
```

2. Copy or generate local KB evidence files into `itervN/` before method/branch selection.
3. The agent writes `itervN/methods.json`, updates `itervN/analysis.md`, and branch `config.json` files. `analysis.md` must show the semantic pre-pass result or carry-forward before the roofline-driven method list.
4. Close the iteration:

```bash
python <runtime-tools>/scripts/orchestrate.py close-iter \
  --run-dir <run-dir> \
  --iter 1
```

`close-iter` benchmarks branches, profiles when possible, attempts Triton IR/ISA checks, updates `state.json`, and opens the next iteration when needed.

## Finalize

If any iteration promoted a faster source rewrite, config, branch, or shape
bucket, first run a final tuning iteration on the current champion. Use the next
iteration number after the last real iteration:

```bash
python <runtime-tools>/scripts/tune_configs.py \
  --state <run-dir>/state.json \
  --iter <final_tune_iter> \
  --which best_input \
  --op-kind memory \
  --search-level broad \
  --max-configs 64 \
  --final-tune \
  --promote-if-better
```

This writes `iterv{final_tune_iter}/tune_results.json`,
`accepted_configs.json`, `config_acceptance.md`, and `attempt_timeline.json`.
When a faster valid config is found, `--promote-if-better` updates
`state.best_config` so `final_kernel.py` bakes the retuned config. If no prior
iteration improved over the initial champion and an initial tuning sweep already
ran, this final tuning iteration may be skipped, but `summary.md` must explain
why. `orchestrate.py finalize` refuses to continue when required final tuning is
missing unless `--skip-final-tune-check` is passed.

```bash
python <runtime-tools>/scripts/orchestrate.py finalize --run-dir <run-dir>
```

Finalization writes:

```text
<run-dir>/
|-- baseline_kernel.py
|-- final_kernel.py
|-- final_config.json
|-- final_kernel_manifest.json
|-- attempt_timeline.svg
`-- summary.md
```

`summary.md` is Chinese by default and must include `## 概要`, `## 最终 Kernel 快照与指标`, `## 算子计算逻辑`, `## 尝试时间线`, and `## 知识沉淀`. Final review should replace `not_appended_by_summarize` with `appended` or `not_appended` plus the reason, then fill `## 回顾与下一步`.

## Expected Reporting

The final answer should include:

- run path
- baseline time, best time, and speedup
- final fixed config
- correctness status
- local KB status
- profiling/ISA caveats
- locations of `summary.md`, `baseline_kernel.py`, `final_kernel.py`, `final_kernel_manifest.json`, and `attempt_timeline.svg`
