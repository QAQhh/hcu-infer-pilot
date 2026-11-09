# kernel-triton-optimize

> 需要对 HCU 上的 Triton kernel 进行 roofline驱动的迭代深度优化(setup→tune→branch→finalize闭环)时...


> **类型**: 🔧 自动化脚本

## 什么时候用

✅ 需要对 HCU 上的 Triton kernel 进行 roofline驱动的迭代深度优化(setup→tune→branch→finalize闭环)时

❌ 不要用于: 仅需单次 benchmark

## 快速开始

```bash
python scripts/orchestrate.py setup --baseline kernel.py --ref ref.py --dims '{"N":1048576}'
```

## 输入 → 输出

| 输入 | 输出 |
|------|------|
| kernel.py + ref.py | final_kernel.py + summary.md |

## 完整文档

→ [SKILL.md](SKILL.md)
