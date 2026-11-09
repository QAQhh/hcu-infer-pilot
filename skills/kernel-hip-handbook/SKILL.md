---
name: kernel-hip-handbook
description: 海光 BW 系列 HCU HIP Kernel 深度性能优化指南（3500+ 行）。覆盖 roofline 分析、指令级优化（ISA 验证、dccobjdump）、共享内存/LDS 调优、Occupancy 计算、Branch 选择与 Ablation 归因、CK Tile kernel 优化等核心技术。适用：需要对 BW 系列 HCU 上的 HIP kernel 进行深度性能优化。不适用：NVIDIA GPU 环境。
license: Apache-2.0
metadata:
  author: HCU Optimization Team
  version: 0.4.0
---

# 海光 BW 系列 HCU 性能优化指南

你是一个海光 HCU 性能优化专家。当用户提供 HIP kernel 代码时，按照以下框架分析性能瓶颈并给出针对 BW 系列架构的优化建议。若用户提供了目标模型的 shape 信息，应结合第 16 节的 Shape 特化策略进行更精准的优化。

> **可用机型速查**: 多机型硬件规格见 `references/` 目录:
> - **BW10** (bw10-1): gfx936, 48CU/31GB/760MHz/150W (当前机器)
> - **BW150** (bw150-2): gfx936, 80CU/64GB/1400MHz
> - **BW1000** (bw22): gfx936, 80CU/64GB/**1500MHz**
> - **BW1100** (nmz21): gfx938, 64CU/**144GB**/800W
> - **BW1101**: gfx938, 64CU/144GB/800W
> - 编译: `--offload-arch=gfx936;gfx938` 覆盖全机型

---

## 1. BW 系列架构参数速查

> 详细内容见 [1. BW 系列架构参数速查](references/architecture-spec.md)。

## 2. 优化分析框架

对任何 kernel 进行优化前，先确定瓶颈类别：

### 2.1 Roofline 模型分析

**算术强度** = FLOPs / Bytes_accessed（计算量与访存量之比）

BW 系列关键性能参数（从 `references/gpu参数对比.csv` 读取，以下为参考值）：
- HBM 带宽: 1.8 TB/s（BW1000A，以 CSV 数据为准）
- FP32 峰值算力: 60 TFLOPS（BW1000A，以 CSV 数据为准）
- FP16 峰值算力: 480 TFLOPS（BW1000A，以 CSV 数据为准）

> **注意**：所有峰值参数优先从 `references/gpu参数对比.csv` 读取（通过 `scripts/gpu_specs.py`），避免硬编码。CSV 中未覆盖的参数可从运行时 `torch.cuda.get_device_properties` 获取。

**判断规则**：
- **计算受限** (Compute-bound): 算术强度高，优化重点在计算效率、Tensor Core 使用、指令级并行
- **带宽受限** (Memory-bound): 算术强度低，优化重点在访存合并、缓存利用、数据复用
- **延迟受限** (Latency-bound): Occupancy 不足无法隐藏延迟，优化重点在提高 occupancy

### 2.2 分析步骤

1. 估算 kernel 的 FLOPs 和 Bytes（包括读和写）
2. 计算算术强度
3. 对比 Roofline 确定瓶颈类别
4. 根据瓶颈类别选择对应的优化策略

---

## 3. Occupancy 优化

> 详细内容见 [3. Occupancy 优化](references/occupancy.md)。

## 4. 内存层级优化

> 详细内容见 [4. 内存层级优化](references/memory-hierarchy.md)。

## 5. Wavefront 级优化

> 详细内容见 [5. Wavefront 级优化](references/wavefront-optimization.md)。

## 6. Tensor Core (AI TC / MFMA) 使用指南

> 详细内容见 [6. Tensor Core (AI TC / MFMA) 使用指南](references/tensor-core-mfma.md)。

## 7. Launch 配置优化

> 详细内容见 [7. Launch 配置优化与 8. 计算重构与 Atomic 优化模式](references/launch-and-refactor.md)。

## 9. 优化 Checklist

对每个 HIP kernel 逐项检查：

### 内存访问
- [ ] 全局内存访问是否合并（wavefront 内连续线程 → 连续地址）
- [ ] 起始地址是否对齐到 128B（L2 cache line）
- [ ] 是否使用向量化加载（float4/double2）减少指令数
- [ ] 是否有不必要的全局内存读写可以用 LDS 替代
- [ ] LDS 是否有 bank conflict（注意 32 banks）
- [ ] LDS padding 策略是否正确（行宽为 32 的倍数时 +1 或 +4 打破 bank 对齐）
- [ ] 所有只读指针是否加了 `__restrict__`
- [ ] 是否采用 software pipelining / LDS double buffering 隐藏内存延迟

### Occupancy
- [ ] 寄存器使用量是否合理（检查 `.vgpr_count`）
- [ ] 是否有寄存器溢出到 scratch memory
- [ ] LDS 用量是否限制了 workgroup 并发数
- [ ] `__launch_bounds__` 是否设置得当

### 计算效率
- [ ] 是否有不必要的类型转换
- [ ] 是否可以使用低精度（FP16/BF16）提升吞吐
- [ ] 矩阵运算是否使用了 MFMA 指令 / rocBLAS
- [ ] 特殊函数（sin/cos/sqrt/rcp）是否在 SFU 上执行
- [ ] 是否有可以提前计算的常量
- [ ] 是否存在连续指令间的数据依赖停顿（可交错独立计算消除）
- [ ] MFMA 指令是否与全局内存加载交错执行
- [ ] 大量累加是否使用 double 精度防止精度损失 (8.6)

### Wavefront 执行
- [ ] Block size 是否为 64 的整数倍
- [ ] 是否有严重的分支 divergence
- [ ] Wavefront 内 reduction 是否使用了 shuffle（非 LDS）
- [ ] 是否移除了不必要的 `__syncwarp()`
- [ ] Warp-level 操作是否适配了 wavefront=64
- [ ] 是否用谓词/branchless 编程替代了条件分支

### Atomic 操作
- [ ] 是否有大量 atomicAdd 竞争可以用串行累加 (8.1B) 或 reduction (8.2) 消除
- [ ] Backward kernel 是否可以从 scatter+atomicAdd 重构为 gather+direct store (14)
- [ ] 剩余的 atomicAdd 是否可以使用硬件原生原子指令 (8.7)
- [ ] 是否通过 `#ifdef __gfx9XX__` 条件编译保证可移植性

### 计算重构
- [ ] 并行粒度是否合理（是否可以改为 block-per-output 或 block-per-sample-point 模式）
- [ ] **Backward kernel 的 block 数是否过多（>100K）？是否应改为 block-per-(batch,anchor) 串行遍历** (8.1B 变体)
- [ ] 不变量（坐标、权重、索引）是否提升到循环外 (8.4)
- [ ] 边界检查是否可以整个 block 提前退出
- [ ] 多层循环中的有效性检查是否提到了最外层 (8.5)
- [ ] Block size 是否根据实际数据维度自适应选择 (8.8)
- [ ] **Memory-bound kernel 是否应 over-provision block size 提升 occupancy** (8.8 进阶)
- [ ] **group 归约是否可以用 sub-warp shuffle 替代 blockReduceSum** (8.9)
- [ ] **是否需要为生产配置的常见参数组合生成特化 kernel（host 端 dispatch）**

### 全局优化
- [ ] Grid size 是否足够大以充分利用所有 CU
- [ ] 是否利用多 stream 并行
- [ ] 是否有不必要的 `hipDeviceSynchronize` 阻塞
- [ ] Host-Device 数据传输是否与计算重叠
- [ ] 是否可以使用 persistent kernel 减少 launch 开销

---

## 10. 优化模式优先级

### 10.1 优化前判断：是否值得 kernel 级优化

在投入优化工作前，先评估 kernel 级调优的空间上限：

1. **Roofline 带宽天花板**：如果 kernel 已在 Roofline 带宽线上（有效带宽接近 HBM 峰值的 70%+），且已使用 LDS/SFU 等片上资源，kernel 内部调优空间极小。此时应考虑**算子融合**（减少全局内存 round-trip）而非 kernel 内部优化。
2. **硬件带宽差距**：Memory-bound kernel 的性能上限由硬件带宽决定。不同设备间的性能差距（如 HBM2E 1.8 TB/s vs HBM3 4.0 TB/s ≈ 2.2×）无法通过 kernel 级优化弥补。
3. **结构性优化 >> 编译器提示优化**：并行粒度重构、Scatter→Gather 重构等结构性改变的收益通常远大于 `__launch_bounds__`、`__restrict__` 等编译器提示（前者可达 2-10×，后者通常 1.02-1.10×）。优先投入结构性优化。

### 10.2 优先级排序

对 HCU 上的 kernel 优化，按以下优先级排序：

| 优先级 | 优化类别 | 典型加速 | 适用场景 |
|--------|---------|---------|---------|
| 0 | **算子融合**（跨算子优化） | 2-10× | Kernel 已接近带宽天花板，减少全局内存 round-trip 是唯一出路 |
| 1 | **并行粒度重构 + 串行累加** (8.1A/B, 8.4) | 2-10× | 多维索引 kernel，大量冗余计算或 atomic 竞争 |
| 1b | **Backward 粗粒度并行**（block-per-output 串行遍历） | 2-5× | Backward block-per-sample-point 导致 block 数 >100K |
| 2 | **Backward Scatter→Gather 重构** (14) | 1.2-1.5× | Backward 用 atomicAdd scatter，逆映射可解析计算 |
| 2b | **Sub-warp shuffle for group reduction** (8.9) | 1.3-2× | group_size 为 2 的幂且 ≤ wavefront，特化路径可避免 blockReduceSum |
| 3 | **Atomic 操作归约** (8.2, 8.3, 8.7) | 1.5-3× | Backward kernel 梯度归约；配合硬件原生 atomic |
| 4 | **多层循环剪枝 + 不变量提升** (8.4, 8.5) | 1.2-2× | 嵌套循环有大量无效迭代或冗余计算 |
| 5 | **内存访问优化** (4.1-4.7) | 1.1-1.5× | Memory-bound kernel |
| 5b | **Over-provisioned block size** (8.8 进阶) | 1.1-1.3× | Memory-bound, 不规则访存, thread=channel 映射 |
| 6 | **Wavefront 对齐与 Shuffle** (5.1-5.4) | 1.1-1.3× | blockSize < 64 或 divergence 严重 |
| 7 | **流水线调度** (4.5, 5.5-5.6, 6.4) | 1.2-2× | Compute-bound GEMM 类 kernel |
| 8 | **精度优化** (FP16/BF16, 8.6) | 1.5-2× | 精度可接受时加倍有效带宽；或 double 累加防误差 |
| 9 | **Launch 配置 + 自适应 Block Size** (7.1-7.3, 8.8) | 1.05-1.2× | Occupancy 不足或线程浪费 |

---

## 11. 远程编译与验证

> 详细内容见 [11. 远程编译与验证、12. 生成本地验证报告](references/remote-build-and-report.md)。

## 13. 迁移与调优路径选择

> 详细内容见 [13. 迁移与调优路径选择、14. Backward Scatter→Gather 重构、15. 优化模式分类总结](references/optimization-patterns.md)。

## 16. Shape 特化优化

> 详细内容见 [16. Shape 特化优化](references/shape-specialization.md)。

## 详细参考

- 1. BW 系列架构参数速查：[references/architecture-spec.md](references/architecture-spec.md)
- 3. Occupancy 优化：[references/occupancy.md](references/occupancy.md)
- 4. 内存层级优化：[references/memory-hierarchy.md](references/memory-hierarchy.md)
- 5. Wavefront 级优化：[references/wavefront-optimization.md](references/wavefront-optimization.md)
- 6. Tensor Core (AI TC / MFMA) 使用指南：[references/tensor-core-mfma.md](references/tensor-core-mfma.md)
- 7. Launch 配置优化与 8. 计算重构与 Atomic 优化模式：[references/launch-and-refactor.md](references/launch-and-refactor.md)
- 11. 远程编译与验证、12. 生成本地验证报告：[references/remote-build-and-report.md](references/remote-build-and-report.md)
- 13. 迁移与调优路径选择、14. Backward Scatter→Gather 重构、15. 优化模式分类总结：[references/optimization-patterns.md](references/optimization-patterns.md)
- 16. Shape 特化优化：[references/shape-specialization.md](references/shape-specialization.md)
