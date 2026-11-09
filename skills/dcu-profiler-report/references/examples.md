# dcu-profiler-report Examples

Run commands from the LightOp root unless noted otherwise.

## Environment Probe

```bash
python - <<'PY'
import torch
print("torch:", torch.__version__)
print("hip:", torch.version.hip)
print("device:", torch.cuda.get_device_name(0))
print("gcn:", torch.cuda.get_device_properties(0).gcnArchName)
PY
hipcc --version
which hipprof || true
which rocprof || true
which rocprofv3 || true
which rocprof-compute || true
```

## First-Pass hipprof Capture

```bash
version=v000_baseline
mkdir -p ".humanize/lightop-agent/profile-artifacts/$version"
python test/test_<op>.py 2>&1 \
  | tee ".humanize/lightop-agent/profile-artifacts/$version/benchmark.log"
hipprof python test/test_<op>.py 2>&1 \
  | tee ".humanize/lightop-agent/profile-artifacts/$version/hipprof.txt"
```

## Candidate Comparison

```bash
version=v001_candidate
mkdir -p ".humanize/lightop-agent/profile-artifacts/$version"
python test/<family>/benchmark_<op>.py 2>&1 \
  | tee ".humanize/lightop-agent/profile-artifacts/$version/benchmark.log"
hipprof python test/<family>/benchmark_<op>.py 2>&1 \
  | tee ".humanize/lightop-agent/profile-artifacts/$version/hipprof.txt"
python3 <skill-root>/scripts/dcu_profile_digest.py \
  --hipprof ".humanize/lightop-agent/profile-artifacts/$version/hipprof.txt" \
  --baseline-hipprof ".humanize/lightop-agent/profile-artifacts/v000_baseline/hipprof.txt" \
  --benchmark-log ".humanize/lightop-agent/profile-artifacts/$version/benchmark.log" \
  --kernel-regex "<kernel-name-pattern>" \
  --operator "<lightop-op>" \
  --version "$version" \
  --output ".humanize/lightop-agent/profile-artifacts/$version/digest.md"
```

## rocprof / rocprofv3 Escalation

Use this when `hipprof` identifies the hot kernel but does not explain the
mechanism.

```bash
version=v002_counters
mkdir -p ".humanize/lightop-agent/profile-artifacts/$version"
rocprof --stats -o ".humanize/lightop-agent/profile-artifacts/$version/rocprof.csv" \
  python test/<family>/benchmark_<op>.py
```

If the target system provides `rocprofv3`:

```bash
version=v002_trace
mkdir -p ".humanize/lightop-agent/profile-artifacts/$version"
rocprofv3 --kernel-trace --stats --output-format csv \
  --output-file ".humanize/lightop-agent/profile-artifacts/$version/rocprofv3" \
  -- python test/<family>/benchmark_<op>.py
```

## rocprof-compute Escalation

Use this when kernel-level counters are needed.

```bash
version=v003_compute
mkdir -p ".humanize/lightop-agent/profile-artifacts/$version"
rocprof-compute profile -n "$version" --path ".humanize/lightop-agent/profile-artifacts/$version" \
  -- python test/<family>/benchmark_<op>.py
rocprof-compute analyze -p ".humanize/lightop-agent/profile-artifacts/$version/$version" \
  | tee ".humanize/lightop-agent/profile-artifacts/$version/rocprof-compute.txt"
```

## Synchronization Pattern

Use explicit synchronization in ad hoc benchmark code:

```python
for _ in range(warmup):
    op(*args)
torch.cuda.synchronize()

start = torch.cuda.Event(enable_timing=True)
end = torch.cuda.Event(enable_timing=True)
start.record()
for _ in range(repeats):
    op(*args)
end.record()
torch.cuda.synchronize()
latency_ms = start.elapsed_time(end) / repeats
```

## Digest Checklist

Every digest should answer:

- Which operator, wrapper, binding, and kernel path was profiled?
- Which shape/dtype/gfx config was selected?
- What changed versus baseline or parent?
- Is the dominant cost HIP API launch, memcpy/memset, kernel execution, config
  dispatch, memory path, compute path, resource pressure, or codegen?
- What one edit should be tried next?
