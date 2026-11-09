# Reference To Triton Baseline Patterns

- Elementwise and memory-bound copies use one `BLOCK_SIZE` constexpr and no `@triton.autotune`.
- Matmul baselines use `tl.dot` with a small fixed tile such as `16x16x32`.
- HIPC/CUDA `.hip` / `.cu` oracles: inspect with `inspect_ref.py`, then generate a conservative Triton `kernel.py` plus Torch `ref.py` wrapper.
- Sum reductions from HIPC (`atomicAdd` on a scalar `out`) map to a block `tl.sum` + `tl.atomic_add` Triton baseline.
- Complex MoE and attention references should produce a manifest and wrapper first; hand-author the baseline when shape/layout semantics are unclear.
- Keep `active_config` visible in `bench.json` so the optimizer can prove profiling used a fixed config.
