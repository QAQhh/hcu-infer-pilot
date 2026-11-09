> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 5. Wavefront 级优化

### 5.1 利用 Wavefront 天然同步

HCU wavefront 64 线程以 lockstep 方式执行，wavefront 内无需任何同步操作。

```cpp
// 不需要的同步（浪费） — 直接删除
__syncwarp();  // CUDA 遗留，HCU 上不需要

// wavefront 内数据交换不需要 barrier
// 直接使用 shuffle 即可
```

### 5.2 Wavefront 内 Reduction（最优实现）

```cpp
// 6 步 shuffle reduction（wavefront=64）
template<typename T>
__device__ T warp_reduce_sum(T val) {
    for (int offset = warpSize / 2; offset > 0; offset >>= 1)
        val += __shfl_down(val, offset);
    return val;
}
```

**⚠ wavefront=64 广播注意事项**：使用 `__shfl(val, 0, 64)` 广播时，如果逻辑处理维度 C < 64（例如 C=32），wavefront 内实际包含多个逻辑组。lane 0 的值会广播到全部 64 个 lane，但不同逻辑组可能期望不同的广播值。此时需要按逻辑组大小设定 width 参数：`__shfl(val, 0, C)` 确保每个逻辑组内独立广播。

### 5.3 DPP（Data Parallel Primitives）优化

DPP 允许在 SIMD 内直接在 lane 间传递数据，无需通过 LDS。适用于：
- 相邻线程间数据交换
- Scan / prefix sum 操作
- Butterfly reduction

具体 DPP 指令使用方式依赖 DTK 版本和内联汇编。

### 5.4 分支 Divergence

Wavefront 64 线程中任何分支 divergence 都会导致两条路径都执行（串行化）。

**影响比 CUDA 更大**：64 线程 vs 32 线程，更大的粒度意味着 divergence 概率更高。

**优化建议**：
1. 将具有相同执行路径的线程聚集到同一 wavefront
2. 使用谓词代替分支（`select` 操作）
3. 数据排序使相邻线程处理相似数据
4. 用算术运算替代条件分支（branchless 编程）

**谓词替代分支示例**：
```cpp
// 有 divergence
if (x > 0) {
    y = a;
} else {
    y = b;
}

// 无 divergence（branchless）
y = (x > 0) ? a : b;  // 编译器生成 v_cndmask 谓词指令

// 更复杂场景：用掩码消除分支
float mask = (float)(x > 0);  // 1.0 or 0.0
y = mask * a + (1.0f - mask) * b;
```

### 5.5 指令流水线与延迟隐藏

#### VALU 指令延迟与依赖

BW 系列 VALU（矢量 ALU）指令典型延迟：

| 指令类型 | 延迟（cycles） | 说明 |
|---------|--------------|------|
| V_FMA_F32 | 4 | FP32 乘加 |
| V_ADD_F32 | 4 | FP32 加法 |
| V_MUL_F32 | 4 | FP32 乘法 |
| V_CVT（类型转换） | 4 | 精度转换 |
| SFU（sin/cos/rcp/sqrt） | 4 | 特殊函数 |
| LDS 读写 | ~40-60 | 取决于 bank conflict 与访问模式 |
| 全局内存读取 | ~700-1000 | 取决于 L2 命中与否 |
| MFMA 矩阵指令 | 8（非流水线） | 对 SIMD 而言非流水线化，延迟固定 8 cycles |

#### 依赖停顿（Dependency Stall）分析

当连续指令之间存在数据依赖时，后续指令必须等待前序指令完成：

```cpp
// 有依赖停顿：每条指令都依赖上一条结果
float a = x * y;       // cycle 0-3
float b = a + z;       // cycle 4-7 (等待 a)
float c = b * w;       // cycle 8-11 (等待 b)
// 总计 12 cycles，VALU 利用率仅 33%

// 消除依赖停顿：交错独立计算
float a1 = x1 * y1;    // cycle 0
float a2 = x2 * y2;    // cycle 1 (与 a1 无依赖)
float a3 = x3 * y3;    // cycle 2
float a4 = x4 * y4;    // cycle 3
float b1 = a1 + z1;    // cycle 4 (a1 已就绪)
float b2 = a2 + z2;    // cycle 5
// VALU 利用率接近 100%
```

#### HCU 延迟隐藏机制

HCU 主要通过两种机制隐藏指令延迟：

1. **Wave-level parallelism（Occupancy）**：多个 wave 交替执行，一个 wave 等待时另一个 wave 执行。每 SIMD 最多 10 个 wave，理论上可隐藏 10× 的单 wave 延迟。

2. **Instruction-level parallelism（ILP）**：单个 wave 内，多条无数据依赖的指令可以流水线执行。这在 occupancy 受限时尤为重要。

**关键权衡**：
- 高 Occupancy + 低 ILP：依赖 wave 切换隐藏延迟，每 wave 寄存器少
- 低 Occupancy + 高 ILP：单 wave 内交错多组独立计算，需要更多寄存器
- **最佳实践**：两者结合。先保证合理的 occupancy（≥50%），再通过 ILP 优化剩余性能。

### 5.6 指令级并行（ILP）优化

#### 循环展开提升 ILP

```cpp
// 低 ILP：每次迭代只处理 1 个元素
for (int i = tid; i < N; i += stride) {
    sum += data[i] * weight;
}

// 高 ILP：每次迭代处理 4 个元素，4 组独立的乘加
for (int i = tid; i < N; i += stride * 4) {
    float a0 = data[i]              * weight;
    float a1 = data[i + stride]     * weight;
    float a2 = data[i + stride * 2] * weight;
    float a3 = data[i + stride * 3] * weight;
    sum += a0 + a1 + a2 + a3;
}
```

#### MFMA 与全局加载交错

在 GEMM 类 kernel 中，MFMA 指令对 SIMD 非流水线化，延迟固定为 8 cycles。利用这个窗口发起全局内存加载：

```cpp
// 低效：先加载，等待完成，再计算
global_load(A_tile_next);
global_load(B_tile_next);
wait_for_loads();
mfma(A_tile, B_tile, C_acc);

// 高效：MFMA 计算期间发起下一轮加载
mfma(A_tile, B_tile, C_acc);    // 开始 MFMA（8 cycles 非流水线延迟）
global_load(A_tile_next);        // 在 MFMA 执行期间发起加载
global_load(B_tile_next);        // 不阻塞，与 MFMA 并行
// ... 更多 MFMA 指令 ...
wait_for_loads();                 // 等加载完成（可能已经完成）
```

这是 GEMM 类 kernel 在 HCU 上获得高性能的关键技术。

### 5.7 快速数学内建函数

HCU SFU（特殊函数单元）提供标准精度和快速两种路径。快速内建函数精度损失约 1 ULP，但延迟显著降低，对 SFU 密集型 kernel 可带来 1.5-3.5× 加速。

**替换表**：

| 标准函数 | 快速替代 | 精度损失 | 适用场景 |
|---------|---------|---------|---------|
| `logf()` | `__logf()` | ~1 ULP | 回归编码、概率计算 |
| `sinf()` | `__sinf()` | ~1 ULP | 角度编码、旋转变换 |
| `cosf()` | `__cosf()` | ~1 ULP | 同上 |
| `expf()` | `__expf()` | ~1 ULP | Softmax、Sigmoid |
| `sqrtf()` | `__fsqrt_rn()` | 0 ULP (rounded) | 距离计算、归一化 |
| `sinf()+cosf()` | `__sincosf()` | ~1 ULP | 同时需要 sin 和 cos 时 |

**精度使用建议（三级场景）**：

| 精度要求 | 场景示例 | 建议 |
|---------|---------|------|
| ≤ 1e-5 | 训练中间计算、推理编码/解码 | 大胆使用快速函数 |
| ≤ 1e-7 | Loss 计算、梯度关键路径 | 测试验证后使用 |
| > 1e-7 | 数值敏感的归约操作 | 保留标准函数 |

**通用适用条件**：
- Kernel 中包含 SFU 函数调用（logf/sinf/cosf/expf/sqrtf）
- SFU 函数执行时间占总 kernel 时间的显著比例
- 精度容差在应用场景可接受范围内（通常训练和推理均可接受 ~1 ULP）
- 规模越大收益越明显（小规模被 launch overhead 掩盖）

### 5.8 CUDA↔HIP Shuffle 映射速查

将 CUDA warp（32 线程）shuffle 操作迁移到 HCU wavefront（64 线程）时的映射：

| CUDA | HIP | 注意事项 |
|------|-----|---------|
| `__shfl_down_sync(0xffffffff, val, offset, 32)` | `__shfl_down(val, offset, 64)` | width 从 32 改为 64（wavefront 大小） |
| `__shfl_sync(0xffffffff, val, lane, 32)` | `__shfl(val, lane, 64)` | 同上 |
| `threadIdx.x & 31` (lane_id) | `threadIdx.x & 63` | 掩码适配 wavefront=64 |
| `tid / 32` (warp_id) | `tid / 64` | warp→wavefront |
| `blockSize / 32` (num warps) | `blockSize / 64` (num wavefronts) | 共享内存大小调整 |
| `__ldg(&ptr[idx])` | `ptr[idx]`（配合 `const __restrict__`） | HIP 无直接等价，依赖编译器自动选择只读缓存路径 |
| CUDA 两级 reduction（`case 64:` 跨 warp） | 单级 shuffle reduction | 64 线程 = 1 wavefront，不需两级 |

**关键注意**：CUDA 的 warp=32 shuffle 模式直接映射到 wavefront=64 后，原本"一个 warp 内的 reduction"变成了"wavefront 前 32 lane 的 reduction"，需要检查 width 参数和 reduction 步数是否正确适配。

---
