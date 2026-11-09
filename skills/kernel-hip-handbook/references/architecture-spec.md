> 本节内容从 `SKILL.md` 拆出，用于保持入口文件精简；正文内容未做删改。

## 1. BW 系列架构参数速查

> **当前机器提示**：本机 8 张卡为 BW1101，运行时架构 `gfx938:sramecc+:xnack-`，每卡 64 CU、约 144 GiB 可见显存。BW1101 与下文 BW1000/gfx926 参数不完全一致；针对当前机器调优时优先读取 `references/BW1101硬件介绍.md`，编译自定义 HIP 扩展时确保包含 `gfx938`。

### 1.1 计算单元规格

| 参数 | 值 |
|------|-----|
| 架构 | GPGPU，目标 `gfx926` |
| 产品型号 | BW1000_H / BW151 / BW101 |
| 计算引擎 (CE) | 8 个 |
| CU 数量 | 88 (full chip) / 80 (OAM) / 64-80 (PCIe) |
| 每 CE 的 CU 数 | 11 (full) / 10 (OAM) / 8-10 (PCIe) |
| 每 CU SIMD 数 | 4 |
| Wavefront 大小 | **64 threads** |
| 每 CU 最大 wave 数 | **40** |
| 每 SIMD 最大 wave 数 | **10** |
| SIMD Lane 数 | 16 |
| Wave 执行周期 | 4 cycles/wave（64 threads / 16 lanes） |
| 每 CU 矢量计算单元 | 64 (4 SIMD x 16 lanes) |
| 每 CU 张量计算单元 | 4 (1 per SIMD) |
| SFU（特殊函数单元） | 4 per SIMD |
| ACE（异步计算引擎） | 4 个，每个支持 8 个独立队列 |

### 1.2 矢量 ALU 算力（per SIMD per cycle）

| 精度 | FMA/cycle |
|------|-----------|
| FP64 | 16 |
| FP32 | 16 |
| FP16 | 32 |

### 1.3 Tensor Core (AI TC) 矩阵指令

| 指令 | A 矩阵 | B 矩阵 | C/D 矩阵 | A/B 精度 | C/D 精度 |
|------|---------|---------|-----------|----------|----------|
| `f64_16x16x4` | 16x4 | 4x16 | 16x16 | FP64 | FP64 |
| `f32_16x16x8` | 16x8 | 8x16 | 16x16 | FP32 | FP32 |
| `f32_16x16x8_tf32` | 16x8 | 8x16 | 16x16 | TF32 | FP32 |
| `f32_16x16x16_f16` | 16x16 | 16x16 | 16x16 | FP16 | FP32 |
| `f32_16x16x16_bf16` | 16x16 | 16x16 | 16x16 | BF16 | FP32 |
| `i32_16x16x32_iu8` | 16x32 | 32x16 | 16x16 | INT8/UINT8 | INT32 |
| `i32_16x16x64_iu4` | 16x64 | 64x16 | 16x16 | INT4/UINT4 | INT32 |

### 1.4 内存层级

| 层级 | 容量 | Cache Line | 带宽 | 备注 |
|------|------|------------|------|------|
| VGPR (per SIMD) | 192KB | - | 128 Bytes/cycle 读写 | 私有寄存器堆，16 lanes x 2 banks x 32-bit |
| LDS (per CU) | 64KB | - | 高带宽（片上） | 支持 HBM→LDS 直接 load |
| L1 Vector Cache (per CU) | 32KB | 64B | - | Write-through, 2 笔 64B 请求可合并为 128B |
| L1 Instruction Cache | 32KB | - | - | 2 个 CU 共享 |
| Constant Cache | 16KB | - | - | 2 个 CU 共享 |
| L2 Cache (全局共享) | 8MB | 128B | - | LRU + Stream policy, 支持 FP32/FP64 atomic add |
| HBM2E | 64GB | - | **1.8 TB/s** | 4 颗 HBM2E stack |

### 1.5 LD/ST 单元

| 参数 | 值 |
|------|-----|
| LD/ST 单元数 / CU | 1 |
| 每 LD/ST 单元带宽 | 32-bit: 合并 4 个地址 / 64-bit: 合并 2 个地址，单 LD/ST 单元每 cycle 处理 1 个 wavefront 的请求 |
| 总带宽 / CU / cycle | 64 Bytes |

### 1.6 互连

| 接口 | 规格 |
|------|------|
| PCIe | Gen5 x16, 128 GB/s 双向 |
| HSL 互连 | 7 ports x8 link, 总计 448 GB/s |

---
