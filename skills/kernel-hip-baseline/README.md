# kernel-hip-baseline

> 从 Torch/Triton/Python/CUDA 参考实现生成 HCU HIP baseline kernel 并验证正确性时...


> **类型**: 🔧 自动化脚本

## 什么时候用

✅ 从 Torch/Triton/Python/CUDA 参考实现生成 HCU HIP baseline kernel 并验证正确性时

❌ 不要用于: 已有完整 HIP 实现

## 快速开始

```bash
python scripts/cuda_to_hip.py --input kernel.cu
```

## 输入 → 输出

| 输入 | 输出 |
|------|------|
| 参考实现 | HIP baseline + 正确性验证 |

## 完整文档

→ [SKILL.md](SKILL.md)
