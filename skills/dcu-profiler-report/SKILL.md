---
name: dcu-profiler-report
description: 'Use when a LightOp DCU/ROCm operator needs profiling evidence: run hipprof
  or deeper ROCm/DTK profilers, capture synchronized benchmark logs, summarize API/kernel/memory
  time, inspect counters or AMDGPU ISA when available, and produce exactly one concrete
  next operator edit.'
---

# dcu-profiler-report

Use this skill when benchmark numbers are not enough and the next LightOp
HIP/ROCm kernel, binding, dispatch, or config-table edit should be driven by
DCU profiling evidence.

The rule is:

```text
profile first, diagnose second, optimize third
```

The output is not just "memory-bound" or "launch overhead". It must be an
inference chain from measured DCU evidence to a likely mechanism to one
actionable LightOp edit.

## Official Reference

Use the SourceFind DCU performance analysis tool guide as the local official
reference for first-pass DCU profiling:

```text
https://developer.sourcefind.cn/gitbook//dcu_developer/DeveloperGuide/dcu_programming/DCU_programming_chapter3_7.html
```

Prefer DTK/DCU tools first. Use `hipprof` for first-pass API/kernel/memcpy
timing. Escalate to `rocprof`, `rocprofv3`, `rocprof-compute`, counter tools,
or AMDGPU ISA/code-object inspection only when timing evidence cannot explain
the next edit.

## When To Invoke

Invoke `dcu-profiler-report` when any of these hold:

- A correctness-passing LightOp optimization candidate has just been benchmarked
  and the loop needs the mandatory per-candidate `hipprof --pmc` interpretation
  before the next edit.
- A LightOp baseline benchmark has passed and no baseline profile digest exists.
- A correct candidate is within +/-2% of baseline or the prior best.
- The second correctness-passing optimization attempt improves less than 5%
  over its parent or baseline. This requires a deep analysis pass before the
  next optimization edit.
- A correct candidate regresses on one or more important shapes.
- A candidate is much faster than expected and needs explanation.
- The next edit is unclear after benchmark results.
- A Humanize/RLCR reviewer asks for profile evidence.
- A candidate may be limited by launch overhead, host-device copies, global
  memory layout, LDS/bank conflicts, VGPR/occupancy pressure, wavefront
  divergence, MFMA underuse, or shape-dispatch choices.

Do not profile while correctness is failing unless the failure is itself a
profiler collection problem. Fix correctness first.

## Device Selection Gate

Before any benchmark or profiling capture, record current card state in the
same host/container environment that will run the workload.

- Run `hy-smi` or `rocm-smi`.
- Pick a card with low HCU utilization and low VRAM occupancy.
- Run benchmark and profiling commands with `HIP_VISIBLE_DEVICES=<idle-card>`.
- Keep the same selected card for paired baseline/candidate captures.
- Store the status output and the selected card in the artifact directory and
  digest. If the tools are unavailable, record the failed command and treat the
  resulting performance data as non-final unless the user accepts that caveat.
- Before the first optimization profile or baseline comparison, include the
  selected-card device bandwidth calibration from
  `.humanize/lightop-agent/device-bandwidth.txt`. If it is missing, run the
  calibration in the same environment and record actual read, write,
  copy/read-write, and triad bandwidth before interpreting operator bandwidth.

## Required Artifacts

Store artifacts under the LightOp loop state or user-specified evidence path:

```text
.humanize/lightop-agent/device-bandwidth.txt
.humanize/lightop-agent/profile-artifacts/<version>/
  device-status.txt           # hy-smi or rocm-smi before benchmark/profile
  benchmark.log
  hipprof.txt
  hipprof-pmc-all/            # mandatory for each correctness-passing optimization candidate
  sqtt-json/                  # mandatory when SQTT is available
  rocprof.csv                 # when rocprof/rocprofv3 is used
  rocprof-stats.csv           # when available
  rocprof-compute/            # when available
  code-object-metadata.txt    # when extracted
  amdgpu-isa.txt              # when extracted
  resource-usage.txt          # VGPR/SGPR/LDS/occupancy/code-object evidence
  digest.md
```

When comparing a candidate, include the baseline or parent artifact path in
the digest.

## Workflow

1. Pick one representative shape first. Prefer the smallest shape that still
   exposes the regression, plateau, launch overhead, or suspected bottleneck.
2. Build a focused benchmark harness with stable warmup, fixed dtype, fixed
   shape, fixed seed, and explicit synchronization around timed regions.
3. Run the device selection gate and pin the selected idle card with
   `HIP_VISIBLE_DEVICES`.
4. Before the first optimization edit or baseline profile, run or cite the
   selected-card device bandwidth calibration and compare the operator's
   effective-bandwidth target against the measured read/write/copy ceiling.
5. Capture normal benchmark output before profiling, so profiler overhead does
   not become the performance claim.
6. Run `hipprof` for first-pass API/kernel/memcpy timing.
7. For every correctness-passing optimization candidate, collect `hipprof`
   PMC evidence with supported variants such as `--pmc`, `--pmc-read`, and
   `--pmc-write`. Interpret cache behavior, memory/cache traffic, LDS or
   bank-conflict evidence, and occupancy/resource pressure before choosing the
   next edit. If a counter group or occupancy signal is unavailable, record the
   exact attempted command and error output.
8. For deep-analysis gates, add SQTT JSON when
   supported, `dccobjdump` disassembly, code-object resource usage, and
   LDS/register/occupancy evidence before choosing the next edit.
9. If `hipprof` shows one or a few dominant kernels but does not explain why,
   collect deeper counters with the installed ROCm/DTK profiler.
10. If the issue looks codegen-sensitive, inspect AMDGPU ISA or code-object
   metadata before choosing an edit.
11. Compare candidate against baseline or parent, not only absolute metrics.
12. Diagnose using the metric groups in [metrics.md](references/metrics.md).
13. Write `digest.md` using the template below. The final section must contain
   exactly one next edit.
14. Update the LightOp loop ledger with the digest path, bottleneck class, and
    selected next edit.

## Common Commands

Load [examples.md](references/examples.md) for copyable command variants.

Minimal first-pass capture from the LightOp root:

```bash
bash <skill-root>/scripts/measure-device-bandwidth.sh \
  --docker <container> \
  --workdir <container-lightop> \
  --hip-visible-devices <idle-card> \
  --output .humanize/lightop-agent/device-bandwidth.txt
mkdir -p .humanize/lightop-agent/profile-artifacts/v000_baseline
hy-smi 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v000_baseline/device-status.txt || \
  rocm-smi 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v000_baseline/device-status.txt
HIP_VISIBLE_DEVICES=<idle-card> python test/test_<op>.py 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v000_baseline/benchmark.log
HIP_VISIBLE_DEVICES=<idle-card> hipprof python test/test_<op>.py 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v000_baseline/hipprof.txt
```

For a benchmark script:

```bash
mkdir -p .humanize/lightop-agent/profile-artifacts/v001_candidate
hy-smi 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v001_candidate/device-status.txt || \
  rocm-smi 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v001_candidate/device-status.txt
HIP_VISIBLE_DEVICES=<idle-card> hipprof python test/<family>/benchmark_<op>.py 2>&1 \
  | tee .humanize/lightop-agent/profile-artifacts/v001_candidate/hipprof.txt
mkdir -p .humanize/lightop-agent/profile-artifacts/v001_candidate/hipprof-pmc-all
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc --pmc-type 3 \
  -o .humanize/lightop-agent/profile-artifacts/v001_candidate/hipprof-pmc-all/pmc \
  python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc-read --pmc-type 3 \
  -o .humanize/lightop-agent/profile-artifacts/v001_candidate/hipprof-pmc-all/pmc-read \
  python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc-write --pmc-type 3 \
  -o .humanize/lightop-agent/profile-artifacts/v001_candidate/hipprof-pmc-all/pmc-write \
  python test/<family>/benchmark_<op>.py
```

Deep-analysis capture, required after a second correctness-passing
optimization improves less than 5%:

```bash
mkdir -p .humanize/lightop-agent/profile-artifacts/v002_deep/{hipprof-pmc-all,sqtt-json}
hy-smi 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v002_deep/device-status.txt || \
  rocm-smi 2>&1 | tee .humanize/lightop-agent/profile-artifacts/v002_deep/device-status.txt
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc --pmc-type 3 \
  -o .humanize/lightop-agent/profile-artifacts/v002_deep/hipprof-pmc-all/pmc \
  python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc-read --pmc-type 3 \
  -o .humanize/lightop-agent/profile-artifacts/v002_deep/hipprof-pmc-all/pmc-read \
  python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof --pmc-write --pmc-type 3 \
  -o .humanize/lightop-agent/profile-artifacts/v002_deep/hipprof-pmc-all/pmc-write \
  python test/<family>/benchmark_<op>.py
HIP_VISIBLE_DEVICES=<idle-card> hipprof --sqtt --sqtt-type 1 --output-type 0 \
  -d .humanize/lightop-agent/profile-artifacts/v002_deep/sqtt-json/ \
  python test/<family>/benchmark_<op>.py
dccobjdump --inputs=<binary-or-so> --show-sass --show-instruction-encoding \
  --separate-functions > .humanize/lightop-agent/profile-artifacts/v002_deep/amdgpu-isa.txt
hipprof --codeobj-analyze <binary-or-so> \
  > .humanize/lightop-agent/profile-artifacts/v002_deep/resource-usage.txt
```

Adjust `<binary-or-so>` to the compiled extension, code object, or extracted
kernel binary produced by the actual build. If a command is unsupported by the
installed DTK, keep the command output or error in the artifact directory and
state the missing evidence in the digest.

Optional helper:

```bash
python3 <skill-root>/scripts/dcu_profile_digest.py \
  --hipprof .humanize/lightop-agent/profile-artifacts/v001_candidate/hipprof.txt \
  --baseline-hipprof .humanize/lightop-agent/profile-artifacts/v000_baseline/hipprof.txt \
  --benchmark-log .humanize/lightop-agent/profile-artifacts/v001_candidate/benchmark.log \
  --kernel-regex "<kernel-name-pattern>" \
  --output .humanize/lightop-agent/profile-artifacts/v001_candidate/digest.md
```

The helper is a first pass only. Inspect profiler output and any counter/ISA
evidence before treating the next edit as final.

## Metrics To Inspect

Start with these groups, then load [metrics.md](references/metrics.md) for the
full list and interpretation rules:

- Runtime identity: LightOp commit, operator, public API, shape, dtype, gfx
  arch, DTK/ROCm/PyTorch version, build command.
- Device selection: `hy-smi` or `rocm-smi` output, selected
  `HIP_VISIBLE_DEVICES`, HCU utilization, and VRAM occupancy.
- Benchmark timing: warmup, repeats, p50/p90/mean, synchronization points,
  variance, baseline and candidate deltas.
- `hipprof` timing: total HIP API time, kernel time, memcpy/memset time,
  launch overhead, top kernels by inclusive/exclusive time.
- Kernel launch shape: grid/block, waves per block, occupancy clues, block
  count relative to CU count, tiny-kernel overhead.
- Memory path: global load/store volume, coalescing, alignment/vector width,
  L2/HBM pressure, redundant reads/writes, temporary tensors.
- LDS path: LDS use, bank conflicts, barriers, shared staging cost.
- Compute path: MFMA/vector ALU utilization, conversion/quantization overhead,
  scalar control overhead, epilogue fusion cost.
- Resource pressure: VGPR/SGPR, spills/scratch, LDS per block, occupancy
  limiters, overly aggressive unroll.
- Dispatch/config: wrong shape branch, overly broad config, missing gfx
  specialization, fallback path accidentally selected.
- ISA/code object: hot instruction window, vector width, MFMA selection,
  excessive scalarization, scratch loads/stores.

For the mandatory <5% second-optimization gate, the digest must include all of
these sections: `hipprof` PMC all, SQTT JSON or the unavailable-tool reason,
`dccobjdump` disassembly, code-object resource usage, and explicit
LDS/register/occupancy interpretation.

Validate exact tool availability on the target machine:

```bash
which hipprof || true
which rocprof || true
which rocprofv3 || true
which rocprof-compute || true
hipcc --version
```

## Digest Template

```markdown
### DCU Profile Digest: <operator> @ <version>

Environment
- LightOp root:
- Repo commit:
- GPU / gfx:
- Device status command:
- Selected HIP_VISIBLE_DEVICES:
- HCU utilization / VRAM before run:
- DTK / ROCm / PyTorch:
- Build command:
- Benchmark command:
- Shape / dtype:
- Baseline or parent profile:
- Candidate profile:
- Artifacts:

Headline
- Bottleneck class:
- Dominant time sink or hotspot:
- Confidence: High | Medium | Low
- Why this profile is valid:

Evidence
| Signal | Baseline | Candidate | Delta | Interpretation |
|---|---:|---:|---:|---|
| <metric/log line> | <value> | <value> | <delta> | <meaning> |

Profiler Hotspots
- <kernel/API/copy/config branch>: <measured signal> -> <meaning>

Deep Analysis Artifacts
- hipprof PMC all:
- SQTT JSON:
- dccobjdump:
- code-object resource usage:
- LDS/register/occupancy:

Counter / ISA Analysis
- Counter source:
- Hot instruction window:
- Suspected codegen or resource issue:
- Instruction-level or launch-level edit:

Inference Chain
1. Measured signal:
2. Likely mechanism:
3. Why other hypotheses are weaker:
4. Risk:
5. Validation command after edit:

Next Edit
- <exactly one concrete LightOp code, binding, config, or benchmark edit>
```

## Diagnosis Hints

- High HIP API time with tiny kernel time: reduce Python/C++ launch count,
  fuse adjacent ops, or route to an existing fused LightOp path.
- High memcpy/memset time: remove host-device transfers, avoid temporary
  materialization, or make output allocation/reuse explicit.
- Dominant single kernel and poor benchmark scaling: inspect memory layout,
  vectorized loads/stores, block size, and dispatch config.
- Low occupancy clues or spills: reduce VGPR pressure, split the kernel,
  shrink unroll, or specialize for the target shape.
- LDS/barrier-heavy symptoms: reduce staging, fix bank conflicts, or simplify
  inter-wave synchronization.
- MFMA-capable GEMM/MoE path underperforms: verify the intended asm/rocBLAS/
  hipBLASLt/CK/Triton AMD route is selected and that shape config matches `W`.
- A candidate only wins on one shape: record it in the performance map and add
  shape/gfx dispatch instead of replacing the broader default.

## Ledger Rules

- Keep `hipprof.txt`, benchmark logs, deeper profiler exports, and digest paths
  in the attempt ledger.
- Only promote a profile-driven edit to the optimization ledger after
  correctness passes and the benchmark shows measured improvement.
- If the profiler tool is unavailable, record the command attempted, the
  failure, and the cheaper evidence used instead.

## Imported source metadata

The following source-specific frontmatter was preserved during import but is not part of the portable Agent Skills frontmatter contract.

```yaml
type: flow
```
