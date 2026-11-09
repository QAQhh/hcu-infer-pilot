> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 3. Occupancy 优化

### 3.1 Occupancy 计算

```
occupancy = active_waves_per_CU / max_waves_per_CU
max_waves_per_CU = 40
max_waves_per_SIMD = 10
```

影响 occupancy 的三个因素：

#### 因素 1：VGPR 使用量

每个 SIMD 有 192KB VGPR。假设每个 VGPR 为 32-bit（4 bytes），16 lanes：
- 每个 wave 使用 N 个 VGPR → 占用 N × 4 × 16 = N × 64 bytes
- 每 SIMD 可容纳 wave 数 = floor(192KB / (N × 64))，上限 10

| VGPR per wave | 每 wave 占用 | 每 SIMD 最大 waves | CU Occupancy |
|---------------|-------------|-------------------|--------------|
| 24 | 1.5KB | 10 (上限) | 100% |
| 48 | 3KB | 10 (上限) | 100% |
| 96 | 6KB | 10 (上限) | 100% |
| 128 | 8KB | 10 (上限) | 100% |
| 192 | 12KB | 10 (上限) | 100% |
| 256 | 16KB | 10 (上限) | 100% |
| 384 | 24KB | 8 | 80% |
| 512 | 32KB | 6 | 60% |
| 768 | 48KB | 4 | 40% |

注意：以上为理论计算，实际 VGPR 分配粒度可能有对齐要求，需通过编译器输出确认。

#### 因素 2：LDS 使用量

每 CU 共 64KB LDS，多个 workgroup 共享：

| LDS per workgroup | 每 CU workgroup 数 | 对 occupancy 影响 |
|-------------------|-------------------|-----------------|
| ≤ 16KB | 4 | 可达上限 |
| 32KB | 2 | 最多 2 个 workgroup 的 waves |
| 64KB | 1 | 仅 1 个 workgroup |

#### 因素 3：Workgroup 大小

每个 workgroup 包含 N 个 wave = ceil(blockDim / 64)。每 CU 最多 40 waves，workgroup 数量受此限制。

### 3.2 查看寄存器使用量

```bash
# 编译时输出资源使用信息
hipcc --offload-arch=gfx926 --save-temps -c kernel.cpp
# 查看 .s 汇编文件中的 .vgpr_count 和 .sgpr_count
```

### 3.3 减少寄存器压力的技巧

1. 减少局部变量数量，复用变量
2. 将不频繁使用的数据放入 LDS
3. 使用 `__launch_bounds__(maxThreads, minBlocks)` 提示编译器
4. 拆分大 kernel 为多个小 kernel
5. 使用较低精度（FP16/BF16 代替 FP32）减半寄存器用量

---
