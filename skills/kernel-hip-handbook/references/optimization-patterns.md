> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 13. 迁移与调优路径选择

当已有 CUDA 算子需要迁移到 HCU 时，有两条路径可选：

| 路径 | 步骤 |
|------|------|
| **路径 A：迁移→调优** | CUDA 原版 → HIP 直迁 → HCU 端针对 wavefront=64 等特性调优 |
| **路径 B：调优→迁移** | CUDA 原版 → CUDA 端按目标硬件特性优化 → 迁移到 HIP |

**路径 A 通常更优**，原因：
1. **CUDA 特有优化迁移后可能失效**：如 `__ldg()` 在 HIP 上无直接等价，只能依赖 `const __restrict__` 编译器提示
2. **HCU 专属优化无法在 CUDA 端预设**：如 wavefront=64 广播、32-bank LDS padding 等
3. **编译器差异**：hipcc (LLVM) 和 nvcc 对相同代码的优化策略不同，直接在 HIP 上调优能更好匹配 hipcc 行为

**策略推荐**：

| 场景 | 推荐路径 | 原因 |
|------|---------|------|
| 已有 CUDA 算子需要迁移到 HCU | **路径 A** | 先迁移保证正确性，再针对 HCU 特性调优 |
| CUDA 和 HCU 都需要部署 | 分别调优 | CUDA 端和 HIP 端各自按目标硬件优化 |
| 从零开始写算子 | 直接写 HIP | 避免迁移开销，直接利用 HCU 特性 |
| 快速评估 CUDA 优化是否有迁移价值 | 路径 B 快速验证 | 适合做 POC，但最终仍需 HCU 端调优 |

> **Shuffle 映射速查**：CUDA→HIP 的 shuffle 操作映射参见 5.8 节。

---

## 14. 优化模式：Backward Scatter→Gather 重构（消除 AtomicAdd）

### 14.1 模式定义

将 Backward kernel 从 **output-pixel-driven scatter + atomicAdd** 重构为 **input-pixel-driven gather + direct store**。

**适用前提**：
1. Forward 是 gather 模式（每个输出元素从有限个输入元素采样）
2. 每个输入元素被引用的输出元素数量有界且较小（≤ ~16）
3. 给定输入位置，可以高效计算引用它的输出位置集合（逆映射可解析计算）

### 14.2 通用实现模板

```cpp
// 原始：Output-pixel-driven scatter（每线程 1 个输出像素）
__global__ void backward_scatter(
    scalar_t* grad_input,
    const scalar_t* grad_output,
    ...) {
    int out_idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (out_idx >= num_output) return;

    // 正向映射：out_idx → input positions
    int inp_pos[K];  // K 个输入位置（bilinear: K=4）
    float weights[K];
    compute_forward_mapping(out_idx, inp_pos, weights);

    scalar_t grad_val = grad_output[out_idx];
    for (int k = 0; k < K; k++) {
        atomicAdd(&grad_input[inp_pos[k]], weights[k] * grad_val);  // 竞争！
    }
}

// 优化：Input-pixel-driven gather（每线程 1 个输入像素）
__global__ void backward_gather(
    scalar_t* grad_input,
    const scalar_t* grad_output,
    ...) {
    int inp_idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (inp_idx >= num_input) return;

    // 逆映射：inp_idx → 哪些输出像素引用了它
    int out_start, out_end;
    compute_inverse_range(inp_idx, &out_start, &out_end);

    float total_grad = 0.0f;
    for (int out_idx = out_start; out_idx <= out_end; out_idx++) {
        // 重计算正向映射，检查 inp_idx 是否在插值角点中
        float weight = compute_weight_if_referenced(out_idx, inp_idx);
        if (weight != 0.0f) {
            total_grad += grad_output[out_idx] * weight;
        }
    }

    grad_input[inp_idx] = total_grad;  // 直接写入，无 atomic
}
```

### 14.3 逆映射计算的通用方法

对于规则网格变换（upsample/resize），正向映射通常为：
```
src_pos = f(dst_pos, scale, align_corners)
```

逆映射就是求解：
```
dst_range = {dst | src_pos ∈ [inp_idx, inp_idx+1) when forward mapping from dst}
```

具体公式：

| 变换类型 | 正向映射 | 逆映射（保守范围） |
|---------|---------|-----------------|
| align_corners=true | `x = oh * (H_in-1)/(H_out-1)` | `oh ∈ [ceil((ih-1)/scale), ceil((ih+2)/scale+3)]` |
| align_corners=false | `x = (oh+0.5)*scale - 0.5` | `oh ∈ [ceil((ih-0.5)/scale - 0.5), ceil((ih+1.5)/scale - 1.5)]` |
| nearest | `x = round(oh * scale)` | `oh ∈ [ceil((ih-0.5)/scale), floor((ih+0.5)/scale)]` |

**注意**：逆映射范围可以取保守上界（多扫描几个输出像素），内层通过条件判断过滤无效像素，保证正确性。过于紧凑的范围可能遗漏边界情况。

### 14.4 性能特征与权衡

| 特征 | Scatter + AtomicAdd | Gather + Direct Store |
|------|--------------------|-----------------------|
| 线程数 | num_output（输出像素数） | num_input（输入像素数） |
| 每线程全局读取 | 1 次 | ~(scale²) 次 |
| 每线程全局写入 | K 次 atomic | 1 次 direct |
| 竞争 | K × scale² 倍 atomic 竞争 | **零竞争** |
| 确定性 | 非确定性 | **确定性** |
| 计算量 | 1 次正向映射 | ~scale² 次正向映射重计算 |
| 适合场景 | 高倍率上采样（scale > 4x） | 低/中倍率上采样（scale ≤ 4x） |
| HCU 优势 | 无 | **显著**（HCU atomicAdd CAS 代价高） |

### 14.5 与其他优化模式的组合

Scatter→Gather 重构可与以下模式叠加：
- **8.4 不变量提升**：逆映射范围计算（oh_start/oh_end）在输出扫描循环外一次计算
- **8.5 多层循环剪枝**：h 维权重为零时跳过整个 w 维循环
- **5.4 Branchless 编程**：4 个角点的 if 判断可用掩码乘法替代
- **8.6 高精度累加**：长序列累加时使用 double 防精度损失

---

## 15. 优化模式分类总结

根据实际算子优化实践，总结各类优化模式的适用性和预期收益：

### 15.1 高收益模式

| 模式 | 适用条件 | 典型收益 |
|------|---------|---------|
| 快速数学内建函数 (5.7) | Kernel 中有 logf/sinf/cosf/expf 等 SFU 调用 | 1.5-3.5× |
| 并行粒度重构 + 串行累加 (8.1B) | 多维输入归约到少量输出，有大量 atomicAdd | 2-10× |
| **Backward block-per-(batch,anchor) 串行遍历** (8.1B 变体) | Backward 用 block-per-sample-point 且循环次数适中 | 2-5× |
| **Backward Scatter→Gather 重构** (14) | Backward 用 atomicAdd scatter，逆映射可解析计算 | 1.2-1.5× |
| **Sub-warp shuffle for group reduction** (8.9) | group_size 为 2 的幂且 ≤ wavefront，可避免 blockReduceSum | 1.3-2× |
| Wavefront shuffle 替代 LDS reduction (8.2) | blockSize ≤ 64 且需要归约操作 | 1.2-1.3× |
| **Over-provisioned block size** (8.8 进阶) | Memory-bound kernel, thread=channel 映射, 不规则内存访问 | 1.1-1.3× |

### 15.2 中等收益模式

| 模式 | 适用条件 | 典型收益 |
|------|---------|---------|
| `__launch_bounds__` 编译器提示 | 所有 kernel（基线优化） | 1.02-1.10× |
| `__restrict__` 指针 | 所有 kernel（基线优化） | 1.01-1.05× |
| `__shfl` 广播共享数据 | Wavefront 内多线程读同一值 | 1.1-1.3× |
| 多层循环不变量提升 + 提前退出 (8.4, 8.5) | 嵌套循环有冗余计算或无效迭代 | 1.1-1.2× |

### 15.3 低收益/无效模式

| 模式 | 条件 | 原因 |
|------|------|------|
| 向量化 (float4) 对随机访问 | 非合并读取模式（如 deformable 双线性插值） | 寄存器爆炸 + 非对齐，可能反而变慢 |
| LDS 优化对已用 LDS 的 kernel | 原始版已使用共享内存 | 收益已被原始版吃掉 |
| 编译器提示对 memory-bound kernel | HBM 带宽是主要瓶颈 | 指令优化无法突破带宽限制 |
| Forward 全维度并行化 | 部分维度间存在计算共享（如 source index 复用） | 破坏计算复用，可能反而变慢 |

### 15.4 决策流程图

```
开始
  │
  ├─ 0. Kernel 是否已接近带宽天花板？
  │     └─ 是 → 考虑算子融合而非 kernel 内部优化 (10.1)
  │
  ├─ 1. 检查是否有 SFU 函数 (logf/sinf/cosf/expf/sqrtf)?
  │     └─ 是 → 替换为 __logf/__sinf 等快速版本 (5.7, 预期 1.5-3×)
  │
  ├─ 2. 检查 atomicAdd 次数 > 1000/block?
  │     └─ 是 → 重构并行粒度: 串行累加(8.1B) 或 block-per-sample(8.1A)
  │
  ├─ 2b. Backward kernel 用 block-per-sample-point 且 block 数 > 100K?
  │     └─ 是 → 改为 block-per-(batch,anchor) 串行遍历 (8.1B 变体)
  │
  ├─ 2c. Backward kernel 用 atomicAdd scatter 且逆映射可解析?
  │     └─ 是 → Scatter→Gather 重构 (14.2)，消除全部 atomicAdd
  │
  ├─ 3. 有 group 归约且 group_size 是 2 的幂 ≤ wavefront?
  │     ├─ group_size=32 → 半 warp shuffle (8.9, 预期 1.3-2×)
  │     └─ 否 → blockReduceSum (8.3)
  │
  ├─ 3b. blockSize ≤ 64 且有 LDS reduction?
  │     └─ 是 → 改为 wavefront shuffle reduction (8.2)
  │
  ├─ 4. 添加基线优化:
  │     ├─ __launch_bounds__(256, N)
  │     ├─ __restrict__ 全指针
  │     └─ __forceinline__ 辅助函数
  │
  ├─ 5. 分析 Roofline:
  │     ├─ Memory-bound + 不规则访存 → 考虑 over-provisioned block size (8.8)
  │     ├─ Memory-bound → 优化访存合并、LDS 缓存、向量化加载
  │     └─ Compute-bound → 优化 ILP、MFMA pipeline、循环展开
  │
  ├─ 6. 参数特化 dispatch:
  │     └─ 对生产配置的常见参数组合生成特化 kernel (host 端 if-else)
  │
  ├─ 7. 跨算子融合 (最高优先级但复杂度最高)
  │
  └─ 8. 用户提供了目标模型 shape 信息？
        └─ 是 → Shape 特化优化 (16)：基于实际参数精准调优 block size / reduction / 展开因子等
```

---
