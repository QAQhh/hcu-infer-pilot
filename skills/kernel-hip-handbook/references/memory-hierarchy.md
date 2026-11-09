> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 4. 内存层级优化

### 4.1 全局内存（HBM）访问优化

#### 合并访存（Coalesced Access）

BW 系列每个 CU 有 1 个 LD/ST 单元，wavefront 64 线程按顺序使用 LD/ST 单元。

**最优访问模式**：wavefront 内连续线程访问连续地址。

```cpp
// 合并访存（好）
float val = data[threadIdx.x + blockIdx.x * blockDim.x];

// 跨步访存（差） — stride 越大性能越差
float val = data[threadIdx.x * stride];
```

**对齐建议**：
- 起始地址对齐到 128B（L2 cache line size）
- 使用 `hipMalloc` 分配的内存默认 256B 对齐
- 每次访存事务按 64B 或 128B 粒度（L1 64B line, L2 128B line）

#### 向量化加载

使用宽数据类型减少指令数：

```cpp
// 标量加载（4 条指令加载 16 bytes）
float a = data[idx];
float b = data[idx+1];
float c = data[idx+2];
float d = data[idx+3];

// 向量化加载（1 条指令加载 16 bytes）
float4 vec = reinterpret_cast<float4*>(data)[idx/4];
```

推荐的向量宽度：`float4` / `double2` / `int4`（每次 16 bytes）。

#### 预取策略

减少访存延迟的方法：
1. 依靠足够的 wave 数（高 occupancy）隐藏内存延迟
2. 使用 software pipelining：在计算当前数据的同时预加载下一批数据到 LDS

### 4.2 LDS（Local Data Share）优化

LDS 是每 CU 64KB 的高带宽片上存储，用于 workgroup 内线程间数据共享。

#### 基本使用

```cpp
__shared__ float smem[1024];  // 编译时分配
extern __shared__ float smem[];  // 运行时通过 launch 参数指定大小
```

#### Bank Conflict 规避

HCU LDS 有 **32 个 bank**，每个 bank 宽度 4 bytes。

**无 conflict 条件**：wavefront 内线程访问 32 个不同 bank（每 32 个连续 4-byte 元素循环映射到 32 个 bank）。

```cpp
// 无 bank conflict — 连续线程访问连续地址
smem[threadIdx.x] = val;

// 有 bank conflict — stride 为 32 的倍数时最严重
smem[threadIdx.x * 32] = val;  // 所有线程访问同一个 bank！
```

**Padding 技巧消除 bank conflict**：

```cpp
// 矩阵转置场景 — 列访问有 conflict
// 32 banks: 行宽为 64 个 float = 256 bytes, 256/4 = 64 个 4-byte 元素
// 64 mod 32 = 0，所以同一列的相邻行元素映射到相同 bank
__shared__ float tile[64][64];  // 列访问时相邻行元素打到同一 bank

// 加 padding 消除 conflict
__shared__ float tile[64][64 + 1];  // +1 打破 bank 对齐
```

注意：因为 HCU 是 32 banks（非 CUDA 的 32 banks 但 wavefront=64），padding 策略需注意 bank 冲突模式：
- HCU: 32 banks，每 32 个连续 4-byte 元素循环映射到 32 个 bank
- 矩阵转置时列访问：同一列中相邻行元素间隔为一行宽度，若行宽为 32 的倍数则发生 bank conflict
- Padding: `tile[N][32+1]` 打破 bank 对齐（+1 使列元素偏移到不同 bank）

#### HBM→LDS 直接搬运

BW 系列支持 `Memory load` 指令从 HBM 直接加载到 LDS，减少寄存器中转开销。编译器可能自动使用此指令，但可通过内联汇编显式控制。

### 4.3 L2 Cache 优化

L2 Cache 是 8MB 全局共享缓存，128B cache line。

**优化建议**：
1. **数据复用**：如果多个 CU 读取相同数据，L2 可提供缓存命中
2. **访存粒度**：按 128B 对齐访存以充分利用 cache line
3. **避免 thrashing**：工作集大小超过 8MB 时，考虑分 tile 处理
4. **Cache policy 利用**：
   - LRU 适合数据复用场景
   - Stream 适合流式访问（一次性数据，避免污染缓存）
5. **L2 Atomic**：HCU L2 支持 32-bit 和 64-bit 浮点 atomic add，利用这一特性进行全局 reduction

### 4.4 寄存器文件优化

每 SIMD 192KB VGPR，每 cycle 128 Bytes 读写带宽。

**寄存器 vs Occupancy 权衡**：
- 更多寄存器 → kernel 速度更快（减少溢出和重计算）但 occupancy 降低
- 更少寄存器 → occupancy 更高但可能有溢出到 HBM 的开销
- 对于 compute-bound kernel：可以接受较低 occupancy 换取更多寄存器
- 对于 memory-bound kernel：优先保证高 occupancy

**溢出检测**：
```bash
# 查看是否有 scratch memory 使用（即寄存器溢出到 HBM）
# 编译时查看 .scratch_memory_size
hipcc --offload-arch=gfx926 --save-temps -c kernel.cpp
grep "scratch" kernel.s
```

### 4.5 Software Pipelining 与 LDS Double Buffering

Software pipelining 的核心思想：**将数据搬运和计算重叠执行**，用 LDS 多缓冲区隐藏全局内存延迟。

#### 基本原理

未优化的循环：
```
for each tile:
    Load tile from HBM → registers/LDS  (等待)
    Compute on tile                       (计算)
```
每次迭代都要等待 HBM 加载完成后才能计算，造成计算单元空闲。

优化后（double buffering）：
```
Prefetch tile[0] → LDS_buf[0]
for i = 0 to N-1:
    Prefetch tile[i+1] → LDS_buf[(i+1)%2]    // 异步加载下一批
    __syncthreads()
    Compute on LDS_buf[i%2]                    // 计算当前批
    __syncthreads()
```
当前 tile 的计算与下一个 tile 的加载同时进行。

#### Double Buffering 实现模式

```cpp
// LDS 分配两倍空间
__shared__ float lds_buf[2][TILE_K][TILE_M + 1];  // +1 避免 bank conflict（32 banks）

// 预加载第一个 tile
load_tile_async(global_ptr, lds_buf[0], ...);
__syncthreads();

int buf_idx = 0;
for (int k = 0; k < K; k += TILE_K) {
    // 异步预加载下一个 tile 到另一个 buffer
    if (k + TILE_K < K) {
        load_tile_async(global_ptr + TILE_K, lds_buf[1 - buf_idx], ...);
    }

    // 在当前 buffer 上计算
    compute_tile(lds_buf[buf_idx], ...);

    buf_idx = 1 - buf_idx;
    __syncthreads();
}
```

#### Triple Buffering（进阶）

当计算量不足以完全覆盖加载延迟时，使用三缓冲：

```cpp
__shared__ float lds_buf[3][TILE_SIZE];
// buf 0: 正在计算
// buf 1: 刚加载完，等待计算
// buf 2: 正在加载
```

适用场景：GEMM 等计算密集型 kernel，K 维度循环中 tile 加载与 MFMA 计算重叠。

#### LDS 用量与 Occupancy 平衡

| 缓冲策略 | LDS 用量（TILE=32×32×FP32） | 每 CU Workgroup 数 |
|----------|---------------------------|-------------------|
| 单缓冲 | 4KB | 最多 16 |
| 双缓冲 | 8KB | 最多 8 |
| 三缓冲 | 12KB | 最多 5 |

**建议**：优先使用双缓冲，仅在 profiling 确认加载延迟仍是瓶颈时升级到三缓冲。

### 4.6 Async Copy（HBM → LDS 直接搬运）

BW 系列支持从 HBM 直接加载数据到 LDS，绕过 VGPR 中转，减少寄存器压力。

#### 原理

传统路径：HBM → VGPR → LDS（两步，占用 VGPR）
直接路径：HBM → LDS（一步，不占 VGPR）

#### 使用方式

编译器在某些访存模式下自动使用 `buffer_load_dword` 直接写入 LDS。可通过以下方式提高使用概率：

1. **数据对齐**：确保 LDS 目标地址和全局内存源地址对齐
2. **连续访存**：wavefront 内线程按顺序访问连续全局内存地址
3. **编译器提示**：使用 `__builtin_nontemporal_load` 提示编译器数据仅用一次

```cpp
// 常规路径（经过 VGPR）
float tmp = global_data[gid];  // HBM → VGPR
lds[lid] = tmp;                // VGPR → LDS

// 编译器可能优化为直接路径的模式：
// 当 tmp 仅用于写入 LDS 且地址模式符合要求时
lds[lid] = global_data[gid];   // 编译器可能生成 HBM → LDS 直接指令
```

#### 与 Software Pipelining 配合

Async copy 与 double buffering 结合效果最佳：直接搬运减少了 VGPR 使用，为计算留出更多寄存器空间，同时降低了搬运延迟。

### 4.7 Read-Only 内存访问优化

#### `__restrict__` 指针限定

告诉编译器指针不会互相别名（alias），允许更激进的指令重排和优化：

```cpp
// 优化前：编译器必须假设指针可能别名，无法重排 load/store
__global__ void kernel(const float* input, float* output) { ... }

// 优化后：编译器可自由重排
__global__ void kernel(
    const float* __restrict__ input,
    float* __restrict__ output
) { ... }
```

**规则**：所有不会别名的指针参数都应加 `__restrict__`。

#### `__ldg()` 等效 — 利用 L2 Read-Only 路径

CUDA 的 `__ldg()` 在 HIP 上没有直接等价物，但 `const __restrict__` 指针的加载会自动路由到只读缓存路径：

```cpp
// HIP 中推荐写法：const __restrict__ + 直接访问
__global__ void kernel(const float* __restrict__ data) {
    float val = data[idx];  // 编译器自动选择最优缓存路径
}
```

对于随机访问模式（如 deformable sampling 的双线性插值），只读缓存路径可带来 10-30% 的内存吞吐提升。

---
