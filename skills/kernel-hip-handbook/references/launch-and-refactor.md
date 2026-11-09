> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 7. Launch 配置优化

### 7.1 Block Size 选择

```
推荐: blockDim = 256 (= 4 wavefronts)
```

| Block Size | Wavefronts/block | 说明 |
|------------|------------------|------|
| 64 | 1 | 最小单位，灵活但 occupancy 可能受限 |
| 128 | 2 | 适中 |
| **256** | **4** | **推荐值，平衡 occupancy 和资源** |
| 512 | 8 | 寄存器/LDS 压力大，仅当计算需要时使用 |
| 1024 | 16 | 极少使用，CU 可能仅容纳 1-2 个 block |

注意：block size 必须是 64 的整数倍（wavefront 大小），否则最后一个 wavefront 浪费线程。

### 7.2 Grid Size 策略

```
目标: grid 覆盖足够多 wave 以隐藏内存延迟
```

- 至少 num_CU × waves_per_CU = 80 × 40 = 3200 个 wave（OAM）
- 即至少 3200 × 64 = 204,800 个线程
- 实际按数据量计算：`gridDim = ceil(N / blockDim)`

### 7.3 多计算引擎利用

BW 系列有 8 个 CE，支持 4 个独立 ACE 管线。多 stream 并发可利用多 CE：

```cpp
// 多 stream 并发执行
hipStream_t streams[4];
for (int i = 0; i < 4; i++) {
    hipStreamCreate(&streams[i]);
    kernel<<<grid, block, 0, streams[i]>>>(data[i]);
}
```

---

## 8. 计算重构与 Atomic 优化模式

本节总结从实际算子优化中提取的通用模式，适用于各类 HIP kernel。

### 8.1 并行粒度重构（Block-per-Output / Block-per-Sample-Point）

#### 问题

朴素 kernel 将每个最细粒度元素分配给一个线程，导致：
- 大量 atomicAdd 竞争（多个线程写同一输出地址）
- 冗余计算（每个线程独立计算共享的坐标、权重）
- 缓存利用率差（访存模式分散）

有两种重构策略，根据 kernel 特征选择：

#### 策略 A：Block-per-Sample-Point（一 block 处理一个采样点）

**适用场景**：block 内线程协作处理 channel 维度，每个线程仍需 atomicAdd 但竞争减少。

```cpp
// 优化前：一个线程处理一个 (batch, anchor, pts, cam, scale, channel) 元素
// 总线程数 = batch × anchor × pts × cam × scale × num_embeds
__global__ void naive_kernel(const int num_kernels, ...) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= num_kernels) return;

    // 每个线程独立解码多维索引（冗余）
    const int channel_index = idx % num_embeds;
    // 每个线程独立读取采样位置（冗余 — num_embeds 个线程读同一地址）
    const float loc_w = sample_location[loc_offset];
    // 每个线程 atomicAdd 到同一输出位置（竞争）
    atomicAdd(output + out_offset, val);
}

// 优化后：一个 block 处理一个采样点，线程协作处理 channels
// 总 blocks = batch × anchor × pts × cam × scale
__global__ void optimized_kernel(const int num_sample_points, ...) {
    const int sample_idx = blockIdx.x;
    if (sample_idx >= num_sample_points) return;

    // 采样位置读取一次，整个 block 共享
    const float loc_w = sample_location[loc_offset];
    const float loc_h = sample_location[loc_offset + 1];

    // 插值权重计算一次
    const float h_im = loc_h * h - 0.5f;
    const float w_im = loc_w * w - 0.5f;

    // 每个线程处理一部分 channels（合并访存，无竞争）
    for (int c = threadIdx.x; c < num_embeds; c += blockDim.x) {
        float val = interp_w1 * feat[ptr1 + c] + interp_w2 * feat[ptr2 + c]
                  + interp_w3 * feat[ptr3 + c] + interp_w4 * feat[ptr4 + c];
        atomicAdd(output + out_base + c, val * weight);
    }
}
```

**收益**：消除冗余坐标/权重计算（~5×）、相邻线程访问相邻 channel（合并访存）。

#### 策略 B：Block-per-Output + 串行累加（thread 拥有固定输出位置）

**适用场景**：多个输入维度（pts/cam/scale 等）贡献到同一输出位置 `output[anchor][channel]`，且每个线程可以独占一个输出 channel，将多维遍历完全串行化到寄存器中，**最终只做一次 atomicAdd**。

```cpp
// 优化前：全维度展平并行
// 总线程数 = batch × anchors × pts × cams × scale × embeds
// 每个线程做 1 次采样 + 1 次 atomicAdd → 海量 atomic 竞争
__global__ void naive_kernel(int num_kernels, float* output, ...) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= num_kernels) return;
    // 解码 6 维索引...
    atomicAdd(output + anchor_index * num_embeds + channel_index,
              bilinear_sampling(...) * weight);  // 每次都 atomic！
}

// 优化后：block=(batch, anchor), thread=channel
// 总 blocks = batch × anchors, threads = num_embeds
// pts/cam/scale 在线程内串行遍历，累加到寄存器
__global__ void optimized_kernel(float* output, ...) {
    int anchor_index = blockIdx.x;  // block 拥有一个 anchor
    int channel = threadIdx.x;       // thread 拥有一个 channel
    if (channel >= num_embeds) return;

    double accum = 0.0;  // 寄存器累加器（double 防精度损失）

    for (int p = 0; p < num_pts; ++p) {
        for (int cam = 0; cam < num_cams; ++cam) {
            // 坐标有效性检查提到外层，跳过整个 scale 循环
            if (!(loc_w > 0 && loc_w < 1 && loc_h > 0 && loc_h < 1)) continue;

            for (int s = 0; s < num_scale; ++s) {
                float sampled = bilinear_sampling(...);
                accum += (double)sampled * (double)weights[w_idx];
            }
        }
    }
    // 最终只做 1 次 atomicAdd（减少 pts×cams×scale 倍）
    atomicAdd(output + anchor_index * num_embeds + channel, (float)accum);
}
```

**收益**：
- atomicAdd 次数从 `batch × anchors × pts × cams × scale × embeds` 降为 `batch × anchors × embeds`，**减少 pts × cams × scale 倍**
- 每线程拥有固定输出位置，寄存器累加无竞争
- 适合输出维度（embeds）≤ 1024 可直接映射到 block 内线程的场景

#### 策略 B 也适用于 Backward：block-per-(batch,anchor) 串行遍历 pts×cams×scale

**核心洞察**：Backward kernel 也可以用策略 B 的思路——一个 block 拥有一个 (batch, anchor)，每个线程拥有一个 channel，串行遍历 pts×cams×scale。虽然看上去"过度并行"（block-per-sample-point）似乎更好，但实际上：

1. **Block 数量爆炸**：block-per-sample-point 产生 `batch × anchors × pts × cams × scale` 个 block（生产配置 ~345K），而 block-per-(batch,anchor) 只有 `batch × anchors` 个 block（~1.8K）
2. **调度开销**：345K blocks 的 GPU 调度开销远大于 1.8K blocks
3. **`__syncthreads` 开销**：每个 block 内的 blockReduceSum 需要 `__syncthreads`，345K × N 次 sync vs 1.8K × 192 × N 次 sync，总量相近但后者 block 少调度更高效
4. **利用局部性**：同一 (batch, anchor) 的不同采样点共享 grad_output 读取，串行遍历可复用寄存器

```cpp
// 不推荐：block-per-sample-point（345K blocks, 大量调度开销）
const int num_sample_points = batch * anchors * pts * cams * scale; // 345,600
kernel<<<num_sample_points, 256>>>(...);

// 推荐：block-per-(batch,anchor) 串行遍历（1.8K blocks）
const int num_blocks = batch * anchors; // 1,800
kernel<<<num_blocks, num_embeds>>>(...);
// 每个 block 内串行: for(pts) for(cams) for(scale) { ... grad计算 + reduction ... }
```

**适用条件**：
- 串行维度的循环次数适中（50-200 次），有足够计算量隐藏延迟
- 每次循环迭代内需要 block-level reduction（如 backward 的标量梯度归约）
- 循环迭代之间无数据依赖（不同 pts×cams×scale 的梯度可独立累加）

**经验证案例**：Deformable Aggregation Backward 从 block-per-sample-point 改为 block-per-(batch,anchor)，在生产配置下 block 数从 345,600 降到 1,800（192x），backward kernel 性能显著提升。

#### 策略选择指南

| 条件 | 推荐策略 | 原因 |
|------|---------|------|
| 多维输入归约到少量输出位置，embeds ≤ 1024 | **B (串行累加)** | 可消除所有中间 atomic，只做一次最终写入 |
| 采样点数量大，需要 block 间并行 | **A (Block-per-Sample)** | 保持足够的并行度覆盖所有 CU |
| **Backward kernel + 循环次数适中（50-200）+ 需要 reduction** | **B (block-per-output 串行遍历)** | block 数大幅减少，调度开销和 sync 开销降低 |
| Backward kernel + 循环次数少（<50）| **A + Reduction (8.2)** | 先按 channel 并行计算梯度，再 reduction |
| 输入维度循环次数大（pts×cams×scale > 100） | **B** | 串行遍历有足够计算量隐藏延迟 |

> **⚠ 关键教训**：不要被"更多并行 = 更快"的直觉误导。在 HCU 上，block 数过多（>100K）会带来显著的调度开销，特别是每个 block 内有 `__syncthreads` 和 blockReduceSum 时。适当"粗化"并行粒度（减少 block 数、增加每 block 工作量）往往比极致并行更高效。

### 8.2 Warp-Level / Block-Level Reduction

#### 问题

Backward kernel 需要将 per-channel 梯度归约为标量值（采样位置梯度、权重梯度）。朴素方法：每个线程 atomicAdd 到同一全局地址。

#### Wavefront Shuffle Reduction（单 wavefront）

当 blockSize ≤ 64（一个 wavefront 内），直接用 shuffle：

```cpp
// 6 步 reduction, wavefront=64
__device__ __forceinline__ float warpReduceSum(float val) {
    for (int offset = 32; offset > 0; offset >>= 1)
        val += __shfl_down(val, offset, 64);
    return val;
}

// 使用：blockSize <= 64 时
float local_grad = 0.0f;
for (int c = threadIdx.x; c < num_embeds; c += blockDim.x) {
    local_grad += compute_grad(c);
}
float total = warpReduceSum(local_grad);
if (threadIdx.x == 0) {
    atomicAdd(grad_output_addr, total);  // 仅 1 次 atomicAdd
}
```

#### Block-Level Reduction（多 wavefront）

当 blockSize > 64，需要两级 reduction：wavefront shuffle → LDS → wavefront shuffle：

```cpp
__device__ __forceinline__ float blockReduceSum(float val, float* shared) {
    int lane = threadIdx.x % 64;      // wavefront=64
    int wid = threadIdx.x / 64;

    val = warpReduceSum(val);          // 第一级：wavefront 内 shuffle

    if (lane == 0) shared[wid] = val;  // 每个 wavefront 的结果写入 LDS
    __syncthreads();

    // 第二级：第一个 wavefront 归约所有 wavefront 的结果
    val = (threadIdx.x < blockDim.x / 64) ? shared[lane] : 0.0f;
    if (wid == 0) val = warpReduceSum(val);

    return val;
}
```

**注意**：HCU wavefront=64，所以 LDS 中间数组大小为 `blockDim.x / 64`（非 CUDA 的 `/32`）。

#### 收益
- atomicAdd 从 num_embeds 次减少到 1 次
- Shuffle 是寄存器到寄存器传输，接近零延迟
- LDS 仅用于跨 wavefront 通信，占用极少（几个 float）

### 8.3 分组权重梯度 — 本地数组 + 展开归约

当权重按 group 分组（num_groups 个 group 共享 channels），每个 group 需要独立的梯度和：

```cpp
// 本地累加器数组（小 num_groups 时在寄存器中）
float local_grad_weights[8];  // 假设 num_groups <= 8
#pragma unroll
for (int g = 0; g < 8; g++) local_grad_weights[g] = 0.0f;

// 按 channel 累加到对应 group
for (int c = threadIdx.x; c < num_embeds; c += blockDim.x) {
    const int group_idx = c / group_size;
    float sampled_val = /* bilinear interpolation */;
    local_grad_weights[group_idx] += grad_out * sampled_val;
}

// 每个 group 分别归约
__shared__ float shared_mem[blockDim.x / 64];
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

**收益**：每组仅 1 次 atomicAdd（总计 num_groups 次 vs 原来 num_embeds 次）。

### 8.9 Sub-Warp（半 Wavefront）Shuffle Reduction — 利用 Group Size 对齐硬件特征

#### 问题

当权重按 group 分组且 `group_size` 恰好等于 wavefront 的某个整数分割（如 group_size=32 = 半 wavefront），使用通用的 `blockReduceSum` 对每个 group 进行归约是浪费的——因为每个 group 的数据已经集中在 32 个连续线程中，可以用更少的 shuffle 步骤完成。

#### 优化：利用 group_size = 半 wavefront 的特性

当 `group_size=32`（HCU wavefront=64 的一半）时，每个 group 恰好占据 32 个连续 thread。可以用 5 步 `__shfl_down`（offset=16,8,4,2,1）在半 wavefront 内完成归约，完全避免 `__syncthreads` 和 LDS。

```cpp
// 通用方法：N 个 group 各做一次 blockReduceSum（含 __syncthreads + LDS）
// 开销 = num_groups × (2 × warpReduceSum + 2 × __syncthreads + LDS 读写)
for (int g = 0; g < num_groups; g++) {
    __syncthreads();
    float total = blockReduceSum(local_grad_weights[g], shared);
    if (threadIdx.x == 0) atomicAdd(grad_weights + g, total);
}

// 优化方法：半 warp shuffle（仅当 group_size=32 时生效）
// 开销 = 5 步 __shfl_down，零 __syncthreads，零 LDS
float wei = grad_output * val;  // 每个线程的 weight 梯度贡献

// 5 步 shuffle 在半 wavefront (32 threads) 内完成归约
for (int offset = 16; offset >= 1; offset >>= 1) {
    wei += __shfl_down(wei, offset);
}

// 每组的头线程（thread 0, 32, 64, ...）直接写结果
if (threadIdx.x % 32 == 0) {
    *grad_weights += wei;  // 直接写入，无 atomicAdd！
}
```

#### 泛化条件

| group_size | 对应 shuffle 步数 | 头线程条件 | 说明 |
|-----------|-----------------|-----------|------|
| 32 | 5 步 (16,8,4,2,1) | `threadIdx.x % 32 == 0` | 半 wavefront，**最常见场景** |
| 64 | 6 步 (32,16,...,1) | `threadIdx.x % 64 == 0` | 正好一个 wavefront |
| 16 | 4 步 (8,4,2,1) | `threadIdx.x % 16 == 0` | 四分之一 wavefront |

**适用条件**：
1. `group_size` 是 2 的幂且 ≤ wavefront size (64)
2. 每个 group 的线程在 block 内连续排列（channel / group_size = group_idx）
3. 同一 group 的线程在同一 wavefront 内（block 内 channel 连续映射时自动满足）

**与通用 blockReduceSum 对比**：

| 维度 | blockReduceSum (N groups) | 半 warp shuffle |
|------|--------------------------|-----------------|
| `__syncthreads` 次数 | 2 × N | **0** |
| LDS 使用 | 需要 shared memory | **零** |
| 总 shuffle 步数 | N × (6+6) = 12N | **5（一次性）** |
| 适用范围 | 任意 group_size | group_size 为 2 的幂且 ≤ 64 |

**经验证案例**：Deformable Aggregation Backward 中 `num_embeds=256, num_groups=8, group_size=32`，从 8 次 `blockReduceSum` 改为半 warp shuffle，消除了 16 次 `__syncthreads` 和所有 LDS 归约开销。

> **核心规则**：当生产配置中 `group_size` 恰好是 wavefront 的整除分割时，应生成特化的 sub-warp shuffle 路径，通过 `#ifdef` 或 host 端 dispatch 选择。这种面向特定参数的极致优化是人工调优超越通用代码生成的关键能力。

### 8.4 不变量提升（Invariant Hoisting）

#### 问题

当 block 内所有线程需要相同的坐标、权重、索引时，每个线程独立计算是浪费。

#### 优化

将不依赖 channel 的计算提升到 channel 循环之外：

```cpp
// 优化前：channel 循环内包含大量不变量计算
for (int c = threadIdx.x; c < C; c += blockDim.x) {
    // 每个线程重复计算相同的索引、坐标、插值权重 — 浪费！
    int loc_offset = ((anchor * num_pts + pt) * num_cams + cam) * 2;
    float loc_w = data[loc_offset];
    float h_im = loc_w * h - 0.5f;
    int h_low = floorf(h_im);
    // ... 计算 4 个插值权重 ...

    // 真正 per-channel 的工作
    float val = w1 * feat[p1 + c] + w2 * feat[p2 + c] + ...;
}

// 优化后：不变量在循环外计算一次
int loc_offset = ((anchor * num_pts + pt) * num_cams + cam) * 2;
float loc_w = data[loc_offset];
float h_im = loc_w * h - 0.5f;
int h_low = floorf(h_im);
// ... 所有插值权重一次性计算 ...

// 边界检查可以整个 block 提前退出
if (loc_w <= 0.0f || loc_w >= 1.0f || loc_h <= 0.0f || loc_h >= 1.0f) return;

// channel 循环内只做 per-channel 工作
for (int c = threadIdx.x; c < C; c += blockDim.x) {
    float val = w1 * feat[p1 + c] + w2 * feat[p2 + c] + ...;
    atomicAdd(output + out_base + c, val * weight);
}
```

**收益**：
- 地址计算：1 次 vs `num_embeds` 次
- 边界检查：1 次（整个 block 提前退出）vs `num_embeds` 次
- 插值权重：寄存器中计算一次，所有线程复用

### 8.5 多层循环提前剪枝（Early Exit Hoisting）

#### 问题

多维嵌套循环中，有效性检查（如坐标边界判断）放在最内层循环，导致无效迭代仍执行外层循环的开销。

#### 优化

将与内层循环无关的检查提升到外层，整体跳过无效的内层循环：

```cpp
// 优化前：检查在最内层
for (int p = 0; p < num_pts; ++p) {
    for (int cam = 0; cam < num_cams; ++cam) {
        for (int s = 0; s < num_scale; ++s) {
            float loc_w = sample_location[...];
            float loc_h = sample_location[...];
            if (loc_w <= 0 || loc_w >= 1 || loc_h <= 0 || loc_h >= 1) continue;
            // ... 采样 + 累加 ...
        }
    }
}

// 优化后：坐标检查提到 cam 循环内、scale 循环外
// 因为同一 (anchor, pts, cam) 对所有 scale 共享同一采样坐标
for (int p = 0; p < num_pts; ++p) {
    for (int cam = 0; cam < num_cams; ++cam) {
        float loc_w = sample_location[...];
        float loc_h = sample_location[...];
        if (!(loc_w > 0.f && loc_w < 1.f && loc_h > 0.f && loc_h < 1.f)) continue;
        // ↑ 跳过整个 scale 内层循环

        for (int s = 0; s < num_scale; ++s) {
            // ... 采样 + 累加 ...
        }
    }
}
```

**收益**：无效坐标时跳过 `num_scale` 次循环迭代，减少不必要的地址计算、全局内存读取、双线性插值。当无效采样点比例较高时（如 deformable attention 中大量坐标超出视野），提升显著。

**通用规则**：分析嵌套循环中每层的不变量，将条件判断尽可能提到最外层。

### 8.6 高精度寄存器累加（Double Accumulation）

#### 问题

在串行累加模式（8.1 策略 B）中，一个线程可能累加成百上千次 FP32 小数，导致显著的浮点舍入误差累积。

#### 优化

使用 `double`（FP64）寄存器作为累加器，最终转回 FP32 输出：

```cpp
double accum = 0.0;
for (int p = 0; p < num_pts; ++p) {
    for (int cam = 0; cam < num_cams; ++cam) {
        for (int s = 0; s < num_scale; ++s) {
            float sampled = bilinear_sampling(...);
            float w = weights[w_idx];
            accum += (double)sampled * (double)w;  // double 精度累加
        }
    }
}
float result = (float)accum;  // 最终转回 FP32
atomicAdd(output + offset, result);
```

**适用场景**：
- 累加次数 > 50 次（pts × cams × scale 的组合）
- 数值范围跨度大（小权重 × 大特征值）
- 需要与 CUDA FP32 版本严格对齐精度

**代价**：
- FP64 寄存器占用翻倍（每 VGPR 存 1 个 double vs 1 个 float）
- BW 系列 FP64 ALU 吞吐与 FP32 相同（16 FMA/cycle/SIMD），不会降低计算吞吐
- 可能略增加寄存器压力，降低 occupancy — 但串行累加模式本身 ILP 足够，低 occupancy 可接受

### 8.7 硬件原生原子指令（Architecture-Specific Atomics）

#### 问题

通用 `atomicAdd` 在 HIP 中编译为 CAS（Compare-And-Swap）循环，高竞争场景下性能差。

#### 优化

HCU gfx926/gfx936 等架构原生支持 FP32 global memory atomic add，可通过内建函数直接调用硬件指令：

```cpp
#ifdef __gfx936__
    // 硬件原生 global atomic fadd：单条指令，无 CAS 循环
    __builtin_amdgcn_global_atomic_fadd_f32(output + offset, result);
#else
    // 通用回退路径
    atomicAdd(output + offset, result);
#endif
```

**可用的硬件原子内建函数**：

| 内建函数 | 操作 | 支持架构 |
|---------|------|---------|
| `__builtin_amdgcn_global_atomic_fadd_f32` | Global FP32 atomic add | gfx936, gfx926 等 |
| `__builtin_amdgcn_ds_atomic_fadd_f32` | LDS FP32 atomic add | gfx926+ |

**使用建议**：
- 用 `#ifdef __gfx9XX__` 条件编译保证可移植性
- 仅在 atomic 竞争是瓶颈时使用（通过 profiling 确认）
- 配合 8.1 策略 B（串行累加减少 atomic 次数）效果最佳：先减少 atomic 次数，再加速剩余的 atomic 操作

### 8.8 自适应 Block Size（Dynamic Block Size Selection）

#### 问题

固定 block size 可能导致线程浪费（block size > 实际工作维度）或 wavefront 未对齐（block size 非 64 的倍数）。

#### 优化

在 host 端根据实际数据维度动态选择最优 block size：

```cpp
void launch_kernel(int num_embeds, ...) {
    // 选择 ≥ num_embeds 的最小 2 的幂次，且 ≤ 1024
    int threads = 256;  // 默认值
    if (num_embeds <= 64)       threads = 64;
    else if (num_embeds <= 128) threads = 128;
    else if (num_embeds <= 256) threads = 256;
    else if (num_embeds <= 512) threads = 512;
    else                        threads = 1024;

    kernel<<<grid, threads>>>(...);
}
```

#### 进阶：Occupancy 导向的 Over-Provisioned Block Size

**核心洞察**：对于内存延迟受限的 kernel（如双线性插值采样），"刚好够用"的 block size 不一定最优。**故意多分配线程（超过实际工作维度），让多出的线程闲置但增加活跃 wavefront 数量**，可以更好地隐藏不规则内存访问延迟。

```cpp
// 常规选择：num_embeds=256 → threads=256 (4 wavefronts)
int threads = select_block_size(num_embeds);  // 256

// Over-provisioned 选择：num_embeds=256 → threads=512 (8 wavefronts)
// 多出的 256 个线程被 `if (channel >= num_embeds) return` 过滤
// 但 8 wavefronts 比 4 wavefronts 能更好地隐藏内存延迟
int threads = select_forward_block_size(num_embeds);  // 512
```

**人工版的 block size 选择逻辑**（已验证性能更优）：
```cpp
int threads = 256;
if (num_embeds <= 128) threads = 128;
else if (num_embeds < 256) threads = 256;   // 注意是 < 不是 <=
else if (num_embeds <= 512) threads = 512;  // num_embeds=256 走到这里，选 512
else threads = 1024;
```

**适用条件**：
1. Kernel 是 memory-bound（全局内存不规则访问多，如 deformable 双线性采样）
2. 每 thread 只处理一个 channel（thread = channel 映射），多余线程早期退出
3. 多余的 wavefront 不会导致寄存器溢出（每 thread 寄存器使用 < 256 时安全）
4. 每 CU 上 block 数足够少（单个 block 内多 wavefront 的策略在 block 数少时更有效）

**不适用场景**：
- Compute-bound kernel：多余线程浪费 CU 计算资源
- 已经有高 occupancy 的 kernel：再增加 wavefront 无额外收益
- 寄存器压力大的 kernel：更多线程可能导致 spill

**经验证案例**：Deformable Aggregation Forward 在 `num_embeds=256` 时，threads=512（8 wavefronts）比 threads=256（4 wavefronts）性能更好，因为双线性插值采样涉及大量随机内存访问，更多 wavefront 能更好地隐藏 HBM 延迟。

**设计原则**：
1. **必须是 64 的整数倍**：HCU wavefront = 64，非对齐会浪费线程
2. **尽量接近实际工作维度**：减少 `if (threadIdx.x >= num_embeds) return` 的空闲线程
3. **选择 2 的幂次**：便于 reduction 等操作的实现
4. **考虑 occupancy**：更大的 block size 意味着更少的 block 并发（见 3.1 Occupancy 计算）
5. **Memory-bound kernel 优先考虑 over-provision**：多 wavefront 隐藏延迟的收益 > 空闲线程的浪费

**与策略 B（串行累加）配合**：当 thread=channel 映射时，block size 应 ≥ num_embeds 以确保覆盖所有 channel。对于 memory-bound 的 forward kernel，可以选择 > num_embeds 的 block size 提升 occupancy；对于 backward kernel，block size = num_embeds 通常已足够（每次 scale 循环内有 block_reduce_sum 提供足够的同步延迟隐藏）。

---
