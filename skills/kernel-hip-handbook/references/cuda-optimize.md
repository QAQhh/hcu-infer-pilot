# CUDA Optimization Patterns Library

This document catalogs proven optimization patterns extracted from real autonomous driving operator optimization (deformable aggregation kernel), with before/after code and rationale.

## Pattern 1: Parallel Granularity Restructuring (Block-per-Sample-Point)

### Problem
Naive kernels assign one thread per finest-grained element, causing:
- Massive atomicAdd contention when threads write to same output
- Redundant computation of shared values per thread
- Poor cache utilization from scattered access patterns

### Before (Origin)
```cuda
// One thread per (batch, anchor, pts, cam, scale, channel)
// Total threads = batch × anchor × pts × cam × scale × num_embeds
__global__ void naive_kernel(const int num_kernels, float* output, ...) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= num_kernels) return;

    // Each thread independently decodes its multi-dimensional index
    const int channel_index = idx % num_embeds;
    idx /= num_embeds;
    const int scale_index = idx % num_scale;
    idx /= num_scale;
    const int cam_index = idx % num_cams;
    // ... more index decoding ...

    // Each thread independently reads sampling location (redundant!)
    const float loc_w = sample_location[loc_offset];
    const float loc_h = sample_location[loc_offset + 1];

    // Each thread independently computes interpolation weights (redundant!)
    const float h_im = loc_h * h - 0.5;
    const float w_im = loc_w * w - 0.5;

    // Every thread does atomicAdd to same output position (contention!)
    atomicAdd(output + anchor_index * num_embeds + channel_index,
              bilinear_sampling(...) * weight);
}

// Launch: fixed 128 threads/block
<<<(int)ceil(((double)num_kernels/128)), 128>>>
```

### After (Optimized)
```cuda
// One block per (batch, anchor, pts, cam, scale) sample point
// Threads within block cooperatively process channels
// Total blocks = batch × anchor × pts × cam × scale
__global__ void optimized_kernel(const int num_sample_points,
    float* __restrict__ output,
    const float* __restrict__ mc_ms_feat, ...) {

    const int sample_idx = blockIdx.x;
    if (sample_idx >= num_sample_points) return;

    // Decode block-level index (shared across all threads in block)
    int idx = sample_idx;
    const int scale_index = idx % num_scale; idx /= num_scale;
    const int cam_index = idx % num_cams; idx /= num_cams;
    // ...

    // Sampling location read ONCE per block (not per thread)
    const float loc_w = sample_location[loc_offset];
    const float loc_h = sample_location[loc_offset + 1];

    // Interpolation weights computed ONCE per block
    const float h_im = loc_h * h - 0.5f;
    const float w_im = loc_w * w - 0.5f;
    const int h_low = floorf(h_im);
    // ... compute interp_w1..w4, validity flags, base pointers ...

    // Each thread handles a SUBSET of channels (no contention on output!)
    for (int c = threadIdx.x; c < num_embeds; c += blockDim.x) {
        float val = 0.0f;
        if (valid1) val += interp_w1 * mc_ms_feat[ptr1 + c];
        if (valid2) val += interp_w2 * mc_ms_feat[ptr2 + c];
        if (valid3) val += interp_w3 * mc_ms_feat[ptr3 + c];
        if (valid4) val += interp_w4 * mc_ms_feat[ptr4 + c];

        atomicAdd(output + out_base + c, val * weight);
    }
}

// Launch: dynamic thread count
const int threads = min(num_embeds, MAX_THREADS_PER_BLOCK);
<<<num_sample_points, threads>>>
```

### Impact
- Eliminates redundant coordinate and weight computation (~5× less instruction count)
- Reduces atomicAdd contention from `num_embeds` threads to 1 per output channel
- Better cache locality: adjacent threads access adjacent channels (coalesced)

---

## Pattern 2: Warp-Level and Block-Level Reduction

### Problem
Backward kernels compute per-channel gradients that must be summed into scalar values (sampling location gradient, weight gradient). Naive approach: every thread atomicAdds to same global address.

### Before (Origin)
```cuda
// Inside bilinear_sampling_grad, called per (batch, anchor, pts, cam, scale, channel):
// Every thread atomicAdds to the SAME grad_weights and grad_sampling_location address
atomicAdd(grad_weights, grad_output * val);
atomicAdd(grad_sampling_location, width * grad_w_weight * top_grad);
atomicAdd(grad_sampling_location + 1, height * grad_h_weight * top_grad);
```

With 256 channels, that's 256 atomicAdd calls to same address — massive contention.

### After (Optimized)
```cuda
// Step 1: Define reduction primitives
__device__ __forceinline__ float warpReduceSum(float val) {
    #pragma unroll
    for (int offset = WARP_SIZE / 2; offset > 0; offset /= 2) {
        val += __shfl_down_sync(0xffffffff, val, offset);
    }
    return val;
}

__device__ __forceinline__ float blockReduceSum(float val, float* shared) {
    int lane = threadIdx.x % WARP_SIZE;
    int wid = threadIdx.x / WARP_SIZE;
    val = warpReduceSum(val);
    if (lane == 0) shared[wid] = val;
    __syncthreads();
    val = (threadIdx.x < blockDim.x / WARP_SIZE) ? shared[lane] : 0.0f;
    if (wid == 0) val = warpReduceSum(val);
    return val;
}

// Step 2: Accumulate locally across channels
float local_grad_loc_w = 0.0f, local_grad_loc_h = 0.0f;
for (int c = threadIdx.x; c < num_embeds; c += blockDim.x) {
    // ... compute per-channel contribution ...
    local_grad_loc_w += w * grad_w_local * top_grad;
    local_grad_loc_h += h * grad_h_local * top_grad;
}

// Step 3: Block-level reduction (warp shuffle → shared memory → warp shuffle)
__shared__ float shared_mem[MAX_THREADS_PER_BLOCK / WARP_SIZE];
float total_w = blockReduceSum(local_grad_loc_w, shared_mem);
__syncthreads();
float total_h = blockReduceSum(local_grad_loc_h, shared_mem);

// Step 4: Single atomicAdd from thread 0
if (threadIdx.x == 0) {
    atomicAdd(grad_sampling_location + loc_offset, total_w);
    atomicAdd(grad_sampling_location + loc_offset + 1, total_h);
}
```

### Impact
- Reduces atomicAdd calls from `num_embeds` to 1 per sample point
- Warp shuffle is register-to-register (near zero latency)
- Shared memory reduction adds minimal overhead (~8 floats shared memory)

---

## Pattern 3: Group-wise Weight Gradient with Local Array + Unrolled Reduction

### Problem
When weights are grouped (num_groups groups sharing channels), each group needs its own gradient sum across its channels. Naive: atomicAdd per channel per group.

### Before (Origin)
```cuda
// Inside bilinear_sampling_grad, each thread handles one channel:
const float val = (w1 * v1 + w2 * v2 + w3 * v3 + w4 * v4);
atomicAdd(grad_weights, grad_output * val);  // one atomicAdd per thread
```

### After (Optimized)
```cuda
// Local accumulator array (lives in registers for small num_groups)
float local_grad_weights[8];  // Assume num_groups <= 8
#pragma unroll
for (int g = 0; g < 8; g++) local_grad_weights[g] = 0.0f;

// Accumulate across channels
for (int c = threadIdx.x; c < num_embeds; c += blockDim.x) {
    const int group_idx = c / group_size;
    float sampled_val = interp_w1 * v1 + interp_w2 * v2 + interp_w3 * v3 + interp_w4 * v4;
    local_grad_weights[group_idx] += grad_out * sampled_val;
}

// Reduce each group separately
#pragma unroll
for (int g = 0; g < 8; g++) {
    if (g < num_groups) {
        __syncthreads();
        float total = blockReduceSum(local_grad_weights[g], shared_mem);
        if (threadIdx.x == 0) {
            atomicAdd(grad_weights + weight_base + g, total);
        }
    }
}
```

### Impact
- Each group gets exactly 1 atomicAdd (total: num_groups atomicAdds vs num_embeds)
- Register arrays with `#pragma unroll` are efficient for small fixed sizes
- `__syncthreads()` inside the unrolled loop is safe because all threads participate

---

## Pattern 4: Read-Only Memory Hints (`__ldg()` + `__restrict__`)

### Before (Origin)
```cuda
__global__ void kernel(
    const float* mc_ms_feat,      // No restrict
    const float* weights,         // No restrict
    float* output                 // No restrict
) {
    float v1 = bottom_data[ptr1];                    // Generic load
    const float weight = weights[weights_ptr];        // Generic load
    const float grad = grad_output[anchor * C + c];   // Generic load
}
```

### After (Optimized)
```cuda
__global__ void kernel(
    const float* __restrict__ mc_ms_feat,     // restrict hint
    const float* __restrict__ weights,        // restrict hint
    float* __restrict__ output                // restrict hint
) {
    float v1 = __ldg(&mc_ms_feat[ptr1 + c]);                  // Read-only cache
    const float weight = __ldg(&weights[weight_base + idx]);    // Read-only cache
    const float grad_out = __ldg(&grad_output[base + c]);       // Read-only cache
}
```

### Impact
- `__ldg()` routes loads through texture/L2 read-only cache path (especially beneficial with H20's 60 MB L2)
- `__restrict__` tells compiler that pointers don't alias → enables better instruction reordering
- Combined effect: 10-30% memory throughput improvement for random-access patterns (typical in deformable sampling)

---

## Pattern 5: Precompute and Hoist Invariants

### Before (Origin)
Each thread independently computes everything:
```cuda
// Every thread (one per channel) recomputes:
anchor_index = batch_index * num_anchors + anchor_index;
const int loc_offset = ((anchor_index * num_pts + pts_index) * num_cams + cam_index) << 1;
const float loc_w = sample_location[loc_offset];
// ... boundary check, h/w lookup, interpolation weight computation ...
```

With 256 channels, same addresses read 256 times, same math done 256 times.

### After (Optimized)
Block-level precomputation, channel-level loop only does per-channel work:
```cuda
// BEFORE channel loop: computed once, shared by all threads
const int loc_offset = ((anchor_index * num_pts + pts_index) * num_cams + cam_index) * 2;
const float loc_w = sample_location[loc_offset];
const float loc_h = sample_location[loc_offset + 1];
if (loc_w <= 0.0f || loc_w >= 1.0f || ...) return;  // Early exit for entire block

const float h_im = loc_h * h - 0.5f;
const float w_im = loc_w * w - 0.5f;
const int h_low = floorf(h_im);
// ... all interpolation weights, validity flags, base pointers ...

// INSIDE channel loop: only per-channel work
for (int c = threadIdx.x; c < num_embeds; c += blockDim.x) {
    const int group_idx = c / group_size;
    const float weight = __ldg(&weights[weight_base + group_idx]);
    // 4 loads + 4 FMAs + 1 atomicAdd — minimal work per channel
}
```

### Impact
- Address computation: 1× instead of `num_embeds`×
- Boundary check: 1× instead of `num_embeds`× (entire block exits early)
- Interpolation weights: computed once in registers, reused by all threads
- Memory loads for coordinates/shapes: 1× instead of `num_embeds`×

---

## Pattern 6: Launch Configuration Optimization

### Before (Origin)
```cuda
// Fixed 128 threads, total threads = batch × anchor × pts × cam × scale × C
const int num_kernels = batch_size * num_pts * num_embeds * num_anchors * num_cams * num_scale;
kernel<<<(int)ceil(((double)num_kernels/128)), 128>>>(...);
```

Problems:
- 128 threads/block is suboptimal for modern GPUs (only 4 warps)
- num_kernels can be enormous (e.g., 1 × 900 × 8 × 6 × 4 × 256 = 44M threads)
- Many blocks with low utilization

### After (Optimized)
```cuda
// Dynamic thread count, blocks = sample points (without channel dimension)
const int num_sample_points = batch_size * num_anchors * num_pts * num_cams * num_scale;
const int threads_per_block = min(num_embeds, MAX_THREADS_PER_BLOCK);  // 256 for typical C=256
kernel<<<num_sample_points, threads_per_block>>>(...);
```

For backward with occupancy hint:
```cuda
__global__ void __launch_bounds__(256, 8)  // Max 256 threads, min 8 blocks/SM
backward_kernel(...) { ... }
```

### Impact
- Block count reduced from 344K (44M/128) to 172K (num_sample_points)
- Each block does meaningful cooperative work instead of single-element work
- `__launch_bounds__` ensures compiler manages register pressure for target occupancy
- Dynamic thread count adapts to different embedding dimensions

---

## Summary: Optimization Priority Order for H20

1. **Parallel granularity restructuring** (Patterns 1, 5, 6) — highest impact, often 2-5× speedup
2. **Atomic operation reduction** (Patterns 2, 3) — significant for backward kernels
3. **Memory access optimization** (Pattern 4) — consistent 10-30% improvement
4. **H20-specific features** (TMA, cp.async, clusters) — case-dependent, useful for structured access patterns
5. **Precision optimization** (FP16/BF16) — doubles effective bandwidth for memory-bound kernels
