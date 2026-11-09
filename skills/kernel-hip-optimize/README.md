# kernel-hip-optimize

> 需要对 HIP kernel 进行 hipprof→ISA→branch→ablation 迭代深度优化时...


> **类型**: 🔧 自动化脚本

## 什么时候用

✅ 需要对 HIP kernel 进行 hipprof→ISA→branch→ablation 迭代深度优化时

❌ 不要用于: 仅需单次 benchmark

## 快速开始

```bash
python scripts/orchestrate.py setup --baseline kernel.hip --ref ref.py
```

## 输入 → 输出

| 输入 | 输出 |
|------|------|
| HIP kernel | optimized kernel + summary.md |

## 完整文档

→ [SKILL.md](SKILL.md)
