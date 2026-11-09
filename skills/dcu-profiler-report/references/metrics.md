# DCU Profiling Metrics

Use these groups when writing a `dcu-profiler-report` digest. Prefer exact
metric names from the installed DTK/ROCm profiler output; this file names the
signals to look for, not a fixed cross-version schema.

## Timing

- Benchmark p50/p90/mean latency with explicit synchronization.
- `hipprof` total runtime, HIP API time, kernel time, memcpy/memset time.
- Top kernel duration and percentage of profiled runtime.
- Launch count and launch overhead when many tiny kernels dominate.

## Environment

- DCU model and gfx arch from `torch.cuda.get_device_properties(0).gcnArchName`.
- DTK/ROCm version, PyTorch HIP version, `hipcc --version`.
- `PYTORCH_ROCM_ARCH`, build command, LightOp commit, active config branch.

## Memory Path

- Global load/store volume and throughput.
- Alignment and vector width of hot loads/stores.
- L2/HBM throughput or utilization counters when available.
- Host-device memcpy/memset time from `hipprof`.
- Temporary tensor allocation or materialization visible in benchmark code.

Interpretation:

- High memcpy/memset time points to data movement or allocation, not kernel
  math.
- High global traffic with low compute utilization suggests fusion, vectorized
  memory access, layout, or redundant read/write fixes.
- Small shapes with many launches often need fusion or dispatch changes more
  than micro-kernel tuning.

## LDS And Synchronization

- LDS usage per block, LDS bank conflict counters when available.
- Barrier/wait counters or timeline gaps when available.
- Staging buffer size and access stride from source/ISA inspection.

Interpretation:

- Bank conflicts suggest padding, swizzle, or different per-wave layout.
- Barrier-heavy kernels may need fewer phases, simpler staging, or a different
  split between waves/blocks.

## Compute Path

- MFMA utilization or instruction count for GEMM/MoE paths.
- VALU/SALU instruction mix for elementwise and reduction kernels.
- Conversion/quantization instruction count for int8/fp8/w4 paths.
- Epilogue overhead, especially bias/activation/quant/store fusion.

Interpretation:

- Low MFMA signal on a GEMM-like path often means the intended kernel route or
  config was not selected.
- High scalar/control overhead in simple elementwise kernels may point to
  branchy dispatch, shape checks in hot loops, or scalarized codegen.

## Resources

- VGPR/SGPR count.
- Scratch/spill loads and stores.
- LDS bytes per block.
- Achieved occupancy or occupancy limiter when the profiler reports it.
- Block size, waves per block, grid size, and CU count.

Interpretation:

- VGPR pressure and spills can make a seemingly better fused kernel slower.
- Too few blocks relative to CU count can create under-occupancy or tail waves.
- Too many tiny blocks can amplify launch/config overhead.

## Dispatch And Shape Coverage

- Config key selected from `lightop/config*.py`.
- gfx-specific branch selected.
- Fallback path vs intended optimized path.
- Per-shape benchmark deltas across `W`.

Interpretation:

- If only one regime improves, keep the candidate behind a dispatcher/config
  guard instead of replacing the default path.
- If the wrong config fires, fix the config table before editing kernel math.

## ISA / Code Object

Inspect AMDGPU ISA or code-object metadata when the profiler points to codegen:

- Hot instruction window.
- Vector width of memory operations.
- MFMA instruction shape.
- Scratch memory accesses.
- Excessive scalarization or predicate/control flow.
- Inlining/unroll pressure.

Use ISA evidence to pick a narrow edit: launch bounds, vector type, unroll
factor, split kernel, config specialization, or source-level layout rewrite.
