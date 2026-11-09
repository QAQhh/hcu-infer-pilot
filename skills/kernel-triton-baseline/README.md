# kernel-triton-baseline

> 从 Torch/Python/Triton 参考实现快速生成 Triton kernel 基线并验证正确性, 支持 matmul/GEMM/elementwise 自动生成时...


> **类型**: 🔧 自动化脚本

## 什么时候用

✅ 从 Torch/Python/Triton 参考实现快速生成 Triton kernel 基线并验证正确性, 支持 matmul/GEMM/elementwise 自动生成时

❌ 不要用于: 已有完整 benchmark-compatible Triton kernel

## 快速开始

```bash
python scripts/inspect_ref.py --ref ref.py --dims '{"N":1048576}'
```

## 输入 → 输出

| 输入 | 输出 |
|------|------|
| 参考实现 | kernel.py + ref.py + baseline_bench.json |

## 完整文档

→ [SKILL.md](SKILL.md)
