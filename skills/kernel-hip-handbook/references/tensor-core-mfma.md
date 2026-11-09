> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 6. Tensor Core (AI TC / MFMA) 使用指南

### 6.1 MFMA 矩阵指令概述

每个 CU 有 4 个张量计算单元（每个 SIMD 一个），执行 `D = A × B + C` 矩阵乘加。

可用指令及矩阵尺寸：

| 指令 | 计算 | A 尺寸 | B 尺寸 | C/D 尺寸 | A/B 精度 | C/D 精度 |
|------|------|--------|--------|----------|----------|----------|
| MFMA_F64_16x16x4 | 矩阵乘 | 16×4 | 4×16 | 16×16 | FP64 | FP64 |
| MFMA_F32_16x16x8 | 矩阵乘 | 16×8 | 8×16 | 16×16 | FP32 | FP32 |
| MFMA_F32_16x16x8_TF32 | 矩阵乘 | 16×8 | 8×16 | 16×16 | TF32 | FP32 |
| MFMA_F32_16x16x16_F16 | 矩阵乘 | 16×16 | 16×16 | 16×16 | FP16 | FP32 |
| MFMA_F32_16x16x16_BF16 | 矩阵乘 | 16×16 | 16×16 | 16×16 | BF16 | FP32 |
| MFMA_I32_16x16x32_IU8 | 矩阵乘 | 16×32 | 32×16 | 16×16 | INT8 | INT32 |
| MFMA_I32_16x16x64_IU4 | 矩阵乘 | 16×64 | 64×16 | 16×16 | INT4 | INT32 |

### 6.2 数据摆放

寄存器堆为 16 lanes，每 lane 有 2 个 32-bit bank。不同精度下每 cycle 的寄存器吞吐：

| 数据类型 | 每 cycle 吞吐 |
|----------|--------------|
| FP64 | 16 个元素 |
| FP32 / TF32 | 32 个元素 |
| FP16 / BF16 | 64 个元素 |
| INT8 | 128 个元素 |
| INT4 | 256 个元素 |

### 6.3 Tile Size 选择建议

- 基础 tile 尺寸与 MFMA 指令对齐：16×16 为基本单元
- 外层 tile 根据 LDS 容量和寄存器预算确定
- 示例（FP16 GEMM）：
  - MFMA tile: 16×16×16
  - Block tile: 128×128（LDS 中缓存 A 和 B 的 tile）
  - LDS 用量: 128×16×2 (FP16) × 2 (A+B) = 8KB（可多 buffer）

### 6.4 MFMA Pipeline 调度与 GEMM 优化

#### MFMA 指令延迟与吞吐

| 指令 | 延迟（cycles） | 吞吐（cycles/指令） | 说明 |
|------|--------------|-------------------|------|
| MFMA_F32_16x16x16_F16 | 8（非流水线） | 4 | 对 SIMD 非流水线化，8 cycles 后结果可用 |
| MFMA_F32_16x16x8 | 8（非流水线） | 4 | 同上 |
| MFMA_F64_16x16x4 | 8（非流水线） | 8 | 同上 |

**关键**：MFMA 对 SIMD 而言是非流水线指令，延迟固定为 8 cycles。虽然不同 MFMA 指令可以背靠背发射（吞吐为 4 或 8 cycles/指令），但每条 MFMA 指令的结果需要等待 8 cycles 后才能被后续依赖指令使用。因此需要通过多条独立 MFMA 指令交错或与全局内存加载交错来隐藏这 8 cycles 的延迟。

#### GEMM Kernel 的 HCU 优化策略

高性能 GEMM 在 HCU 上的关键要素：

**1. 分块策略（Tiling）**

```
问题规模: M × N × K
Block tile: BM × BN (每个 block 负责的输出子矩阵)
MFMA tile: 16 × 16 (基本计算单元)
K-loop tile: BK (每次从 K 维加载的宽度)
```

典型配置（FP16 GEMM）：

| 配置 | BM×BN | BK | LDS 用量 | VGPR 用量 | 说明 |
|------|-------|-----|---------|----------|------|
| 小 tile | 64×64 | 16 | 4KB | 较少 | 高 occupancy |
| **中 tile** | **128×128** | **16** | **8KB** | **适中** | **推荐起点** |
| 大 tile | 256×128 | 16 | 12KB | 较多 | 高计算强度 |

**2. LDS 数据布局**

A 矩阵和 B 矩阵加载到 LDS 时，需要考虑：
- Bank conflict 避免：padding 到 32+1（LDS 为 32 banks，行宽为 32 的倍数时列访问冲突）
- MFMA 读取模式：16 lanes 同时读取，确保每 lane 读到正确元素

```cpp
// A matrix in LDS: BM × BK, padded
__shared__ half lds_A[BM][BK + 4];  // +4 half = +8 bytes，避免 bank conflict（32 banks, 4-byte bank width）

// B matrix in LDS: BK × BN, padded
__shared__ half lds_B[BK][BN + 4];
```

**3. 寄存器累加器管理**

每个线程持有 C 矩阵的部分结果在 VGPR 中：

```cpp
// 每个线程的累加器（FP16→FP32 accumulate）
float acc[MFMA_M_TILES][MFMA_N_TILES][4];  // 16×16 MFMA 每线程持有 4 个 FP32 值

// K-loop 中不断累加
for (int k = 0; k < K; k += BK) {
    // Load A, B tiles to LDS (async, double buffer)
    // ...
    for (int kk = 0; kk < BK; kk += MFMA_K) {
        // 从 LDS 读取 A, B fragments 到 VGPR
        // 发射 MFMA 指令
        // acc 在寄存器中持续累加
    }
}
// 最终写回 C 到全局内存
```

**4. 流水线调度（关键优化）**

将 K-loop 内的操作分为三类并行执行：

```
Stage 1: Global Memory → LDS (async copy)
Stage 2: LDS → VGPR (register load)
Stage 3: VGPR → MFMA (compute)

时间线:
Iter 0: [Global→LDS tile0] [                    ] [                ]
Iter 1: [Global→LDS tile1] [LDS→VGPR tile0      ] [                ]
Iter 2: [Global→LDS tile2] [LDS→VGPR tile1      ] [MFMA tile0      ]
Iter 3: [Global→LDS tile3] [LDS→VGPR tile2      ] [MFMA tile1      ]
...
```

三级流水完全隐藏了全局内存延迟和 LDS 读取延迟。

### 6.5 与 rocBLAS/MIOpen 配合

对于标准矩阵运算（GEMM、卷积），优先使用 rocBLAS 和 MIOpen 库：
- 这些库已针对 BW 架构深度优化
- 自动选择最优 MFMA 指令和 tile 策略
- 只有当库不满足自定义需求时才手写 MFMA kernel

---
