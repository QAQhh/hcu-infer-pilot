# HCU Architecture & Triton Notes (Hygon / AMDGPU)

Consolidated reference covering HCU/HCU architecture, Triton TTGIR dialects & layout
encodings, LinearLayout, and the critical `tt.load`/`tt.store` → `buffer_load`/`buffer_store`
lowering pipeline.

Primary Triton sources (local tree):

| Layer | Path |
| --- | --- |
| `tt.*` ops | `triton/include/triton/Dialect/Triton/IR/TritonOps.td` |
| `ttg.*` ops | `triton/include/triton/Dialect/TritonGPU/IR/TritonGPUOps.td` |
| HCU MMAC layout | `triton/include/triton/Dialect/TritonGPU/IR/TritonGPUAttrDefs.td` (`amd_mfma`, `MmacLayout`) |
| `amdg.*` ops | `triton/third_party/amd/include/Dialect/TritonAMDGPU/IR/TritonAMDGPUOps.td` |
| AxisInfo analysis | `triton/include/triton/Analysis/AxisInfo.h` |

---

## 1. HCU / HCU Architecture

### 1.1 Target Arch Defaults

Local source evidence from the Triton source tree, e.g. `<triton-root>/...`:

- Default HCU `mmacLayout` by target arch:
  - `gfx928`, `gfx92a`, `gfx936`: `LEGACY`
  - `gfx938`, `gfx946`, `gfx948`: `INTERLEAVE`
- `third_party/amd/lib/TritonAMDGPUToLLVM/TargetUtils.cpp` classifies HCU ISA families:
  - `gfx928`, `gfx936`, `gfx938`: CDNA3-like
  - `gfx92a`, `gfx946`: CDNA4-like
- The same file exposes HCU feature bits:
  - `gfx928`, `gfx936`: no extra HCU feature bits in that table
  - `gfx938`: MMAC layout, MAMC FP8, MLS, CVT FP8/F32
  - `gfx92a`: common HCU features except MMAC layout plus FP6/FP4 groups
  - `gfx946`: common HCU features plus FP6/FP4 and scale/B4 groups
- `include/triton/Tools/Sys/GetEnv.hpp` lists cache-invalidating env vars including
  `AMDGCN_USE_BUFFER_OPS`, `TRITON_HIP_USE_ASYNC_COPY`, `TRITON_HIP_USE_BLOCK_PINGPONG`,
  and `TRITON_HIP_USE_IN_THREAD_TRANSPOSE`.

### 1.2 Implementation Consequences

- Always record arch and cache-invalidating env vars in `env.json`.
- Prefer finite config registries with explicit tile sizes, `num_warps`, and `num_stages`.
- For gfx936, be conservative with MLS/MMAC-layout assumptions until code-object evidence confirms them.
- For gfx938, MLS/MMAC layout methods are candidates, but final proof still requires generated IRs and `dccobjdump`.
- Layout conversions (`#ttg.blocked` to `#ttg.dot_op`) are a major LDS traffic source; optimize tile sizes and `num_stages` to reduce conversion overhead.
- The `mmacLayout` attribute in `#ttg.amd_mfma` (legacy vs interleave) determines linear layout and thus DS read instruction selection; verify the generated instruction matches the expected layout path via `dccobjdump`, not by checking for `mmacLayout` in TTGIR (it is often absent).
- When analyzing TTGIR, note that `mmacLayout` is often omitted when it equals the default (`legacy`); rely on the target arch default and confirm via final ISA DS read variant.

### 1.3 HIP vs Triton (not automated)

- Do not copy HIP `__builtin_hcu_*` or HIP-style inline asm into Triton source.
  Triton 3.5.1 exposes `tl.inline_asm_elementwise`, but treat it as an explicit
  escape hatch only; prefer `tl.*` and `triton.Config`, then prove with
  **`.ttgir` + `.amdgcn` / hsaco ISA** (`isa_check.py`). Compiler-emitted `amdg.*` in TTGIR is
  normal lowering, not a HIP builtin port.
- Normal Triton iterations do not use a HIP method map. If porting a HIP idea,
  re-express it as Triton source/config, then prove it with TTGIR,
  AMDGCN/hsaco ISA, correctness, and timing.
- Manual `.ll` / `llvm.hcu.*` in cache (from `IntrinsicsHCU.td`) is optional debug only;
  **`isa_check.py` does not read `.ll`** — same rule as: `llvm.hcu.*` never appears in
  final `dccobjdump` HCU ISA.

---

## 2. TTGIR Dialects & Layout Encodings

Automated checks in `isa_check.py` match **MLIR text in `.ttgir` cache files** via
`ttgir_patterns` in `hcu_triton_isa_signatures.json`. Final machine proof uses
`isa_patterns` on **`.amdgcn` assembly plus `dccobjdump` hsaco output** (no `.llir`).

### 2.1 Dialect Mnemonics in Dumped `.ttgir`

| Dialect | Prefix | Role |
| --- | --- | --- |
| Triton | `tt.` | `dot`, `dot_scaled`, `load`, `store`, `matrix_load`, `atomic_*`, layout ops |
| TritonGPU | `ttg.` | `local_load`, `local_store`, `local_alloc`, `async_copy_global_to_local`, `async_wait`, `convert_layout`, `dot_op` / `amd_mfma` encodings |
| TritonAMDGPU | `amdg.` | `buffer_load`, `buffer_store`, `buffer_load_to_local`, `matrix_load_to_local`, `scaled_upcast_fp8`, barriers |

#### Naming: `dot_scaled` vs informal `scaled_dot`

| Layer | Canonical name | Source |
| --- | --- | --- |
| Python API | `tl.dot_scaled` | `python/triton/language/core.py` |
| MLIR / TTGIR | `tt.dot_scaled` | `TritonOps.td` → `TT_DotScaledOp` |
| Informal docs/tests | `scaled_dot` | comments only; **not** a separate MLIR op |

`isa_check.py` matches `tt.dot_scaled` via `tt.dot(?:_scaled)?` for matmul methods.
There is no `tt.scaled_dot` mnemonic in the Triton dialect.

On Hygon/HCU, `AccelerateHCUMatmul.cpp` may rewrite `tt.dot` → `tt.dot_scaled` when a
scaled MFMA/MMAC instruction is selected (`withScale=true`). Native FP8/BF8 `tl.dot`
(without block scales) can remain `tt.dot` with MLIR operand types `f8E4M3FN` / `f8E5M2`
on the same line as the op.

### 2.2 Layout Encodings

Triton's TTGIR uses *encodings* (MLIR attributes attached to tensor types) to describe how data is
distributed across GPU threads. Understanding which encoding appears where is essential for
diagnosing LDS traffic, bank conflicts, and dot-operation correctness.

#### 2.2.1 Block Layout (`#ttg.blocked`)

The default memory layout. When data is loaded via `tt.load`, it arrives in blocked layout.
Key attributes:

| Attribute | Meaning |
| --- | --- |
| `sizePerDim` | element count per dimension of the CTA-level tile |
| `threadsPerWarp` | how threads within a warp are distributed across dimensions |
| `warpsPerCTA` | how warps are distributed across dimensions |
| `order` | dimension traversal order (contiguous = row-major `[1, 0]` for 2-D) |

Blocked layout describes how a tensor is distributed across threads in a blocked/contiguous
fashion. It is the starting layout for all data loaded from global memory.

#### 2.2.2 Dot Op Layout (`#ttg.dot_op`)

The encoding that describes how matrix operands are distributed for the dot operation.
Key attributes:

| Attribute | Meaning |
| --- | --- |
| `opIdx` | 0 for LHS/A operand, 1 for RHS/B operand |
| `parent` | the parent MFMA encoding (`#ttg.amd_mfma<...>`) |

The `dot_op` encoding determines which threads hold which elements of the matrix operand.
Operands of `tt.dot` / `tt.dot_scaled` are always in `#ttg.dot_op` encoding; the `opIdx`
distinguishes the two operand positions.

#### 2.2.3 AMD MFMA Encoding (`#ttg.amd_mfma`)

The primary matmul encoding on AMDGPU/HCU targets. Key attributes:

| Attribute | Meaning | Example |
| --- | --- | --- |
| `warpsPerCTA` | how many warps participate in the MFMA | `[1, 2]`, `[2, 2]` |
| `instrShape` | the MFMA instruction shape (M, N, K per instruction) | `[16, 16, 32]` for f16 MMAC on gfx938 |
| `mmacLayout` | MMAC variant: `"legacy"` (default) or `"interleave"` | `"interleave"` for gfx938/gfx946 |
| `mtK` | whether the K dimension is split across multiple warps | `true` / `false` |

**Default behaviour**: `mmacLayout` defaults to `"legacy"` (`DefaultValuedParameter` in
`TritonGPUAttrDefs.td`). When omitted in printed IR, it is `"legacy"`. When present and
not `"legacy"`, it indicates an HCU MMAC layout (`isHCUMmac()` returns true).

`#ttg.amd_mfma<...>` is the primary matmul encoding in TTGIR. `mmacLayout` defaults to
`legacy` and is often **omitted** in printed IR (`DefaultValuedParameter` in
`TritonGPUAttrDefs.td`). When present, `mmacLayout != "mfma"` indicates HCU MMAC
(`isHCUMmac()`).

### 2.3 Method → Layout Encoding Evidence

| Method | Expected TTGIR Layout Evidence |
| --- | --- |
| `triton.dot_mmac_shape` | `#ttg.amd_mfma<...>` with instrShape, warpsPerCTA; `mmacLayout` often absent (defaults to `legacy`); operands in `#ttg.dot_op<opIdx=..., parent=#ttg.amd_mfma<...>>` |
| `triton.coalesced_load_store` | No standalone TTGIR proof; source indexing plus bandwidth/timing proves coalescing. |
| `triton.layout_stride_transform` | No standalone TTGIR proof; source stride/layout change plus correctness and bandwidth/timing proves the method. |
| `triton.matrix_ds_mls` | No standalone proof from `#ttg.dot_op`; require `tt.matrix_load`, `amdg.matrix_load_to_local`, `amdg.local_load_packed_tranposed`, or final DS matrix-read / matrix-load ISA. |
| `triton.layout_conversion_optimization` | `ttg.convert_layout` from `#ttg.blocked` to `#ttg.dot_op`; major LDS traffic source |

### 2.4 Method → TTGIR Evidence (High Signal)

| Method | TTGIR ops / attrs to expect |
| --- | --- |
| `triton.dot_mmac_shape` | `tt.dot` or `tt.dot_scaled`, `#ttg.dot_op<`, `#ttg.amd_mfma<`; `mmacLayout` may or may not appear (often absent, defaults to `legacy`); `lhs`/`rhs` on `dot_scaled` |
| `triton.low_precision_fp8_bf8` | FP8/BF8 on **gfx938+**: `tt.dot_scaled` + `lhs`/`rhs` = `#tt<"e4m3">` / `#tt<"e5m2">` / … (`ScaleDotElemType`); **or** native `tt.dot` with `f8E4M3FN` / `f8E5M2` operand types; `amdg.scaled_upcast_fp8`. TF32 on **gfx928+**: `tt.dot` with `input_precision="tf32"` on f32 operands |
| `triton.coalesced_load_store` | **No TTGIR/ISA-only check** (`tt.load` and generic load-store ISA are not coalescing proof). Coalescing quality comes from source indexing plus timing/bandwidth. |
| `triton.async_copy_global_to_lds` | `amdg.buffer_load_to_local`, `ttg.async_copy_global_to_local` |
| `triton.matrix_ds_mls` | `tt.matrix_load`, `amdg.matrix_load_to_local`, `amdg.local_load_packed_tranposed` (sic), or final DS matrix-read / matrix-load ISA. `#ttg.dot_op<` is only operand context; normal `tl.dot` produces it without MLS. |
| `triton.num_stages_pipeline` | `ttg.async_wait`, `ttg.async_commit_group`, `amdg.async_wait` are supporting IRs only; proof requires active config plus before/after timing/resource pressure. |
| `triton.barrier_scope_reduction` | `ttg.local_barrier`, `amdg.wait_barrier` / `arrive_barrier` are opportunity/supporting IRs only; proof requires reduced hot-path barrier/wait counts plus correctness/timing. |
| `triton.cache_policy_buffer_ops` | non-default `cacheModifier` on `tt.load` / `amdg.buffer_*` |
| `triton.persistent_programs` / `split_k_streamk` | Atomics/waits are supporting context only. Split-K proof requires source/config mapping, partial buffer, dedicated Triton reduction kernel, correctness, and timing/tail improvement. |
| `triton.layout_conversion_optimization` | `ttg.convert_layout` between `#ttg.blocked` and `#ttg.dot_op`; count and layout of conversion ops |

Config-only or delta-only methods (`num_warps`, `block_size`, `epilogue_fusion`,
`coalesced_load_store`, `layout_stride_transform`, `persistent_programs`, etc.)
keep empty `ttgir_patterns` and rely on `active_config`, source/config mapping,
timing, and optional supporting ISA/resource checks.

---

## 3. LinearLayout

In newer Triton versions, `#ttg.linear_layout` (or `LinearLayout` attribute) maps between
logical tensor element indices and physical (thread, lane, offset) positions. On HCU targets,
different MMAC layouts yield different linear layouts. This affects:

- How LDS data is arranged for matrix reads
- Which DS read instruction is generated:
  - `legacy` mmacLayout → `ds_read_m32x16_b16`
  - `interleave` mmacLayout → `ds_read_m32x16_b16_alt`

Linear layouts are the foundation for layout conversions and are increasingly used to replace
the older per-op layout-convert lowering paths. When converting from `#ttg.blocked` to
`#ttg.dot_op`, the linear layout determines the exact LDS read/write pattern and thus the
generated DS instruction variant.

---

## 4. tt.load / tt.store → buffer_load / buffer_store Lowering

This is the most critical optimization path for memory throughput on HCU. Getting `tt.load` /
`tt.store` to lower into AMD `amdg.buffer_load` / `amdg.buffer_store` (and further into
`buffer_load_dword` / `buffer_store_dwordx2` / `x3` / `x4` in LLVM IR) requires satisfying
specific conditions in the Triton compiler pipeline.

### 4.1 The Three Key Conditions: Contiguity, Divisibility, Constancy

For `tt.load`/`tt.store` to generate vectorized buffer ops (`buffer_load`/`buffer_store`),
three properties of the pointer's axis info must be favorable:

| Property | Meaning | Source |
| --- | --- | --- |
| **contiguity** | Length of shortest sequence of contiguous integers along each dim. `contiguity[d]` = power of 2. Determines vector size for buffer ops. | `AxisInfo.h` |
| **divisibility** | Largest power of 2 that divides the first element of all groups of length `contiguity[d]` along dim d. Ensures alignment. | `AxisInfo.h` |
| **constancy** | Length of shortest sequence of repeating integers along each dim. Critical when mask is present — tells compiler the mask is constant across groups, enabling vectorized predicated loads. | `AxisInfo.h` |

**Source definition**: `triton/include/triton/Analysis/AxisInfo.h`

These are computed by `ModuleAxisInfoAnalysis` (dataflow analysis) and propagated as
discardable attributes `tt.contiguity`, `tt.divisibility`, `tt.constancy` through the IR.

### 4.2 The Lowering Pipeline

The conversion from `tt.load`/`tt.store` to `buffer_load`/`buffer_store` goes through
four key passes:

```
tt.load / tt.store
       │
       ▼
  ① Coalesce.cpp          — AxisInfo analysis → coalesced memory layout
       │
       ▼
  ② CanonicalizePointers  — Decompose ptr → (scalar_base, tensor_offset)
       │
       ▼
  ③ ConvertToBufferOps    — Pattern match → amdg.buffer_load / buffer_store
       │
       ▼
  ④ LoadStoreOpToLLVM     — Emit LLVM IR buffer intrinsics (dwordx2/x3/x4)
```

#### Pass ①: Coalesce (`Coalesce.cpp`)

- **Path**: `triton/lib/Dialect/TritonGPU/Transforms/Coalesce.cpp`
- Runs `ModuleAxisInfoAnalysis` to compute contiguity, divisibility, constancy.
- Uses axis info to build coalesced memory layout via `buildCoalescedEncoding`.
- This is the earliest point where axis info shapes the memory access pattern.

#### Pass ②: CanonicalizePointers (`CanonicalizePointers.cpp`)

- **Path**: `triton/third_party/amd/lib/TritonAMDGPUTransforms/CanonicalizePointers.cpp`
- Introduces the "fat pointer" abstraction: every pointer is decomposed into
  `(basePtr: scalar, offset: tensor)`.
- Offset decomposition splits expressions into uniform (scalar) and non-uniform (tensor) parts.
- **Critical**: Propagates `tt.contiguity`, `tt.divisibility`, `tt.constancy` attributes through
  `tt.addptr` chains — but only when the pointer rank is preserved. When a non-uniform offset
  is added, these attributes are **not** propagated (the pattern may break original guarantees).
- **Small-tensor path**: For pointers with `tt.pointer_range=32`, keeps the original base pointer
  and accumulates all offsets into the tensor offset, ensuring non-negative offsets.
- Materializes the fat pointer back as `tt.addptr(tt.splat(base), offset)` at load/store sites,
  which is exactly the pattern `ConvertToBufferOps` looks for.

#### Pass ③: ConvertToBufferOps (`ConvertToBufferOps.cpp`)

- **Path**: `triton/third_party/amd/lib/TritonAMDGPUTransforms/ConvertToBufferOps.cpp`
- Central decision function: `canUseBufferOps()` checks:
  1. `ptr` must originate from `tt.AddPtrOp`
  2. The base pointer must be a `tt.SplatOp` (uniform base across threads)
  3. The offset must be a 32-bit integer tensor (`i32`)
  4. The byte offset must fit within 4GB (proved via one of):
     - `tt.pointer_range=32` on the base pointer (tensor fits in 4GB)
     - `llvm.assume` with non-negative assumption
     - Integer range analysis proving offset ∈ [0, 2³²-2]
- If all checks pass, replaces `tt.load`/`tt.store` with `amdg.buffer_load`/`amdg.buffer_store`.
- Mask handling: splat-all-ones masks are dropped (treated as no-mask); only non-trivial
  masks are forwarded to the buffer op.

#### Pass ④: LoadStoreOpToLLVM (`LoadStoreOpToLLVM.cpp`)

- **Path**: `triton/third_party/amd/lib/TritonAMDGPUToLLVM/LoadStoreOpToLLVM.cpp`
- `BufferLoadOpConversion` / `BufferStoreOpConversion` emit the AMDGPU buffer resource
  descriptor from the base pointer and emit `raw.ptr.buffer.load` / `raw.ptr.buffer.store`
  intrinsics with the tensor offset.
- Vector size is determined by `getVectorSize(ptr, offset, axisAnalysisPass)` using axis info
  contiguity — this is what produces `buffer_load_dwordx2`/`x3`/`x4` vs single `dword`.
- Mask alignment can reduce the vector size: `axisAnalysisPass.getMaskAlignment(mask)` is
  checked, and `vec` is reduced to `min(vec, maskAlignment)`.

### 4.3 How to Ensure buffer_load / buffer_store Generation

#### 4.3.1 Ensure High Contiguity

Contiguity determines the vector size. To maximize it:

- **Use power-of-2 block sizes**: `BLOCK_DMODEL_PADDED = next_power_of_2(head_size)` ensures
  `tl.arange(0, BLOCK_DMODEL_PADDED)` produces contiguous offsets.
- **Use `tl.multiple_of`** for loop variables:
  ```python
  for start_n in range(0, cur_batch_ctx_len, BLOCK_N):
      start_n = tl.multiple_of(start_n, BLOCK_N)
  ```
  This asserts `start_n` is always a multiple of `BLOCK_N`, proving the derived pointers
  have aligned offsets.
- **Construct pointers with contiguous arange patterns**:
  ```python
  off_q = (batch_idx * stride_b + offs_m[:, None] * stride_m + offs_d[None, :] * stride_d)
  ```

#### 4.3.2 Ensure Divisibility (Alignment)

Divisibility guarantees the pointer arithmetic produces aligned addresses:

- **Annotate function arguments with `tt.divisibility`**:
  ```python
  attrs={
      (3,): [["tt.divisibility", 16], ["tt.pointer_range", 32]],  # Q_buffer
      (4,): [["tt.divisibility", 16]],  # stride_q_batch
      (5,): [["tt.divisibility", 16]],  # stride_q_next_n
  }
  ```
  When strides have divisibility 16, the compiler proves addresses are 16-byte aligned,
  a prerequisite for `buffer_load`/`buffer_store`.
- **Pad dimensions to power-of-2** so stride arithmetic stays aligned:
  ```python
  Lk_padded = triton.next_power_of_2(Lk)
  ```
- **Align KV cache strides** at the launcher level:
  ```python
  is_padded_mode = kv_cache_fp8.stride(0) % 16 == 0
  if is_padded_mode:
      kv_cache_attr.append(["tt.divisibility", 16])
  ```

#### 4.3.3 Ensure Constancy (When Mask is Present)

When a mask is used, the compiler must know that the mask is "constant enough" across
groups of elements to emit vectorized predicated loads:

- **Use `tl.max_constancy`** on loaded values and masks:
  ```python
  bn = tl.load(B_Loc + ..., mask=..., other=0)
  bn = annotate_hint(bn, "non-negative")
  bn = tl.max_constancy(bn, [16])

  seq_mask = (start_n + offs_n[:, None]) < cur_batch_ctx_len
  seq_mask = tl.max_constancy(seq_mask, [8, BLOCK_DMODEL_PADDED])
  ```
  `tl.max_constancy(bn, [16])` tells the compiler the block index is constant across
  groups of 16 elements, enabling `buffer_load` / `load_dwordx4`.

#### 4.3.4 Use `tt.pointer_range=32` and i32 Offsets

- **`tt.pointer_range=32`** declares that the pointer's accessible memory range fits in 4GB.
  This directly satisfies the 4GB offset check in `canUseBufferOps()`:
  ```python
  attrs={
      (3,): [["tt.divisibility", 16], ["tt.pointer_range", 32]],  # Q_buffer
      (15,): [["tt.pointer_range", 32]],  # OutLogits_buffer
  }
  ```
- **Use `i32` offsets** when possible. The offset tensor must be 32-bit integer for buffer ops.
  `tt.pointer_range=32` enables the compiler to safely narrow 64-bit offsets to 32-bit.
- **Use `annotate_hint(x, "non-negative")`** to tell the compiler that loaded indices
  (e.g., block numbers from indirection tables) are non-negative, which helps the offset
  range analysis prove the 4GB bound.

#### 4.3.5 Eliminate Masks When Possible

When the data access pattern guarantees no out-of-bounds access, removing the mask
enables unconditional buffer loads (no predication):

```python
if block_size % BLOCK_N == 0:
    k_load = tl.load(K_cache + off_k)  # no mask → unconditional buffer_load
else:
    k_load = tl.load(K_cache + off_k,
                    mask=(start_n + offs_n[None, :]) < cur_batch_ctx_len,
                    other=0.0)  # masked → predicated buffer_load
```

When `block_size % BLOCK_N == 0`, tokens within a BLOCK_N range always fall in the same
cache block, so out-of-bounds from crossing block boundaries cannot occur.

### 4.4 Practical Example: paged-attention KV cache load

From `aiter/ops/triton/pa_prefill.py`:

```python
# Step 1: Load block index from indirection table
bn = tl.load(B_Loc + cur_batch * stride_b_loc_b +
            ((start_n + offs_n) // block_size) * stride_b_loc_s,
            mask=(start_n + offs_n) < cur_batch_ctx_len,
            other=0)

# Step 2: Help compiler with non-negative and constancy hints
bn = annotate_hint(bn, "non-negative")
bn = tl.max_constancy(bn, [16])

# Step 3: Compute KV offset using the block index
off_k = (bn[None, :] * stride_k_cache_bs +
        cur_kv_head * stride_k_cache_h +
        (offs_d[:, None] // x) * stride_k_cache_d +
        ((start_n + offs_n[None, :]) % block_size) * stride_k_cache_bl +
        (offs_d[:, None] % x) * stride_k_cache_x)

# Step 4: Load — mask elimination when block_size is aligned
if block_size % BLOCK_N == 0:
    k_load = tl.load(K_cache + off_k)  # unconditional buffer_load
else:
    k_load = tl.load(K_cache + off_k,
                    mask=(start_n + offs_n[None, :]) < cur_batch_ctx_len,
                    other=0.0)  # predicated buffer_load
```

From `aiter/ops/triton/attention/pa_mqa_logits.py` (launcher annotations):

```python
# Annotate arguments for buffer op generation
attrs={
    (2,): [["tt.divisibility", 16]],                  # heads_num
    (3,): [["tt.divisibility", 16], ["tt.pointer_range", 32]],  # Q_buffer
    (4,): [["tt.divisibility", 16]],                  # stride_q_batch
    (5,): [["tt.divisibility", 16]],                  # stride_q_next_n
    (6,): [["tt.divisibility", 16]],                  # stride_q_heads
    (7,): kv_cache_attr,                              # KV_buffer (divisibility if padded)
    (8,): kv_cache_attr,                              # stride_k_seq
    (13,): [["tt.divisibility", 16], ["tt.pointer_range", 32]], # weights
    (15,): [["tt.pointer_range", 32]],                # OutLogits_buffer
}
```

### 4.5 Summary: Checklist for buffer_load / buffer_store

| Condition | How to ensure | Key API |
| --- | --- | --- |
| High contiguity | Power-of-2 block sizes, contiguous arange patterns | `tl.arange`, `tl.multiple_of` |
| Divisibility (alignment) | Strides aligned to 16B+, annotate args | `tt.divisibility` attr, `tl.multiple_of` |
| Constancy (with mask) | Mask constant across groups of elements | `tl.max_constancy` |
| 4GB offset bound | Small tensors or proven range | `tt.pointer_range=32`, `annotate_hint("non-negative")` |
| i32 offsets | Let compiler narrow, or use pointer_range=32 | `tt.pointer_range=32` |
| Uniform base pointer | Pointer = scalar base + tensor offset | Natural from `tl.load(ptr + offset)` pattern |
| Mask elimination | Guarantee no OOB by construction | Align BLOCK_N to block_size |

---

## 5. Layout Conversion

`ttg.convert_layout` converts between different encodings. The most important conversion
path is `#ttg.blocked` → `#ttg.dot_op` (before `tl.dot`), which involves:

1. LDS stores from threads that have the data (in blocked layout)
2. LDS loads (including matrix-read forms) by threads that need the data (in dot_op layout)
3. This conversion is a major source of LDS traffic and bank conflicts

Other common conversions include `#ttg.dot_op` → `#ttg.blocked` (after the dot) and
conversions between different blocked encodings (e.g. after transpose operations).

---

## 6. Hygon Triton Rules

Use this section when a method depends on Hygon architecture, Triton lowering,
profiler interpretation, or ISA evidence.

### 6.1 General Rules

- Treat wavefront size as 64.
- Use HCU/gfx guards: gfx928/gfx92a/gfx936 use legacy MMAC layout; gfx938/gfx946 use interleave layouts.
- Keep `num_warps`, `num_stages`, tile sizes, and split/reduction blocks explicit in configs.
- Before benchmark or profiling, inspect visible HCU load with `rocm-smi`, `hy-smi`, or the platform equivalent and set `HIP_VISIBLE_DEVICES` / `CUDA_VISIBLE_DEVICES` to an idle or lowest-utilization card when possible.
- Do not run performance comparisons concurrently on the same card. If all cards are busy or the selected card is not exclusive, record that in `analysis.md` and `summary.md` and treat small timing deltas as inconclusive.
- `AMDGCN_USE_BUFFER_OPS` is cache-invalidating in Triton; record when it is set.
- For int32 pointer-offset or buffer-op enabling rewrites, require a real range proof before casting offsets. Acceptable proof includes an explicit Triton/compiler pointer-range attribute or a runtime-dispatched `tl.constexpr` branch selected only when all reachable tensor-relative offsets for that branch fit in signed 32 bits.
- If pointer range proof is absent, keep the original int64 path and mark the method unproven rather than forcing int32.
- `tl.matrix_load`/MLS methods require source evidence and final code-object/ISA evidence.
- For MoE/attention/memory-bound config registries, use small finite registries keyed by shape family, dtype, device/arch, layout, and role; do not generate one config per arbitrary shape.
- For multi-family optimization, final delivery must include `dispatch_manifest.json` showing whether the merge uses runtime config dispatch, runtime variant dispatch, or one config proven across all families.
- Do not copy aiter fused_moe or attention business code into this skill. Use it as a reference for config design and shape bucketing.
- Do not use removed HIP reference names such as `optimization_catalog.md` or `method_registry.json` in the Triton skill; use the `triton_*` reference files only.

### 6.2 Ambiguous Hygon/Triton Behavior

When a hardware-related error, profiler symptom, compiler lowering choice, cache IR, or performance regression is unclear, investigate in this order:

1. Search the local HCU KB for the exact gfx target, Triton feature, compiler diagnostic, environment variable, profiler counter, instruction mnemonic, or source-project hint.
2. Inspect source-backed reference projects found by the KB and copy only patterns whose target guards, layout contracts, call signatures, and config assumptions are visible in source.
3. If local evidence is insufficient, inspect the local Triton source tree or primary ROCm/LLVM/Triton sources. Treat non-Hygon AMD guidance as analogy until Hygon compilation and ISA verification confirm it.
4. Build a minimal probe under repository-root `hygon_tmp/` when a small compile/runtime test can answer the question faster than changing the main kernel.
5. Feed confirmed findings back into `methods.json`, branch code, config registries, or reference notes; quarantine unsupported assumptions.

Use this path for `tl.dot`/MMAC lowering, `tl.matrix_load`/MLS, buffer-op cache invalidation, missing or surprising AMDGCN, waitcnt/LDS hazards, profiler contradictions, and Triton cache/IR mismatches.

### 6.3 Triton Lowering And ISA Verification

For methods that depend on Triton lowering or Hygon-specific codegen:

1. Query local KB/source-backed examples first for the exact gfx target and Triton pattern.
2. Capture the relevant Triton cache directory before and after optimization.
3. Inspect `.ttir`, `.ttgir`, AMDGCN, metadata, and generated code objects when present.
4. Match `tt.*` / `ttg.*` / `amdg.*` ops in Triton cache `.ttgir` files.
5. Verify final ISA/resource behavior with `dccobjdump` on hsaco. Source intent and compile success alone are not proof.
6. Mark a method implementation-failed if the branch is fast but the claimed ISA or lowering evidence is absent.

Useful final evidence families include `v_mmac`, DS read matrix forms, buffer/global load-store families, `s_waitcnt`, barriers, VGPR/SGPR/LDS pressure, occupancy, and any Hygon-specific matrix-load lowering noted by local KB or source inspection.

### 6.4 Failure Modes

- Local KB CLI unavailable or index incomplete: write `kb_unavailable.json`, continue with degraded KB status, and do not make KB-backed claims.
- Selected HCU runtime target lacks KB: this is expected; do not install the KB into the runtime target for this workflow.
- `xcu` and `hipprof` both write degraded or empty metrics: continue with timing, Triton cache IRs, SQTT when useful, and ISA evidence, but disclose degraded profiling and include the xcu installation hint when missing.
- Triton code objects or cache dirs cannot be located: inspect `TRITON_CACHE_DIR`, config keys, env vars such as `AMDGCN_USE_BUFFER_OPS`, and benchmark logs before declaring ISA inconclusive.
- Expected ISA pattern is absent from a relevant dump: mark the method implementation-failed even if the champion is faster.
- Champion speedup comes only from autotune/config search: keep the faster fixed config, but do not attribute the gain to algorithmic methods unless ablation and evidence support it.
- All branches fail correctness or compilation: repair sources/configs and rerun; do not update method attribution from failed branches.
