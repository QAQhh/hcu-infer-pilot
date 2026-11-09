---
name: kernel-triton-baseline
description: 海光 HCU Python/Triton 正确性优先基线生成器。从 Torch/Python/Triton 参考实现 + shape hints 生成 benchmark 兼容的 kernel.py 和 ref.py 基线 case，作为 kernel-triton-optimize 的前置步骤。支持 matmul/GEMM/elementwise 的自动生成，Reduction/Attention/MoE 需人工手写。适用：需要从已有参考实现快速生成 Triton kernel 基线并验证正确性。不适用：已有完整 benchmark-compatible Triton kernel 的场景。
license: Apache-2.0
metadata:
  author: HCU Optimization Team
  version: 0.4.0
---

# Hygon Triton Baseline Generator

## 用途

在 `kernel-triton-optimize` 运行之前创建缺失的 baseline 阶段。将参考实现 + shape hints 转换为包含 benchmark 兼容的 `kernel.py`、`ref.py`、manifest 和验证通过的 `baseline_bench.json` 的 case 目录。

只有在远程 HCU 上 `validate_case.py` 通过后才启动迭代优化器。

## 路径解析

- `<baseline-skill>`：包含此 `SKILL.md` 的目录。
- `<optimizer-skill>`：同级 `<baseline-skill>/../kernel-triton-optimize`。
- 运行前验证：`inspect_ref.py`、`generate_baseline.py`、`validate_case.py` 和 optimizer `preflight.py` / `benchmark.py`。

从另一个项目使用时，使用该项目的 `hygon_tmp/` 进行探测和冒烟 case。不要将 `hygon_tmp/` 路径视为已提交的接口。

## 产出

```text
kernel.py
ref.py
ref_analysis.json
baseline_manifest.json
baseline_bench.json   # validate_case.py 之后
```

`kernel.py` 暴露 `setup(**kwargs)` 和 `run_kernel(**kwargs)`（无 `@triton.autotune`）。生成或手写的 `setup()` 必须嵌入目标 shape 默认值；`--dims` / `--dims-file` 是生成提示，不是必需的输出文件。
`ref.py` 暴露 `reference(**kwargs)`。

## 循环概览

```
0. inspect_ref.py     → ref_analysis.json（op_kind、signature_hint、unsupported_assumptions）
1. generate_baseline.py → kernel.py、ref.py、baseline_manifest.json
   如果 op_kind ∉ {matmul, elementwise*} → 停止；手写 kernel.py，然后验证
2. validate_case.py   → preflight + benchmark --disable-autotune → baseline_bench.json
3. 交接给 kernel-triton-optimize orchestrate.py setup
```

步骤 **0–2** 是**确定性脚本**。当 `unsupported_assumptions` 非空或 `op_kind` 为 `reduction` / `unknown` 时，步骤 **1** 可能需要 **agent 编写** `kernel.py`。

当前可自动生成的族：

- **matmul / GEMM**（dims 含 `M,N,K` 或 ref 中有 `tl.dot` / `torch.matmul`）
- **elementwise** 在 1D `N` 向量上的 copy / add / mul（compute 或 memory 风格冒烟 baseline）

Attention、paged attention、unified attention、MoE 和其他 layout 密集算子属于**交接族**：生成 manifest/参考包装器，然后手写 `kernel.py` 和一个有限配置种子列表。不要假装这些是安全的自动生成的 baseline。

## 工作流

### 1. 检查参考实现

```bash
python <baseline-skill>/scripts/inspect_ref.py \
  --ref <ref-file> \
  --dims '{"N":1048576}' \
  --out <case-dir>/ref_analysis.json
```

`--dims` / `--dims-file` 是生成提示。生成的 `kernel.py.setup()` 将它们用作默认目标 shape。

生成前读取 `ref_analysis.json`。检查 `classification.op_kind`、`signature_hint` 和 `unsupported_assumptions`。

操作族：

- `matmul`：dims 包含 `M,N,K`，或 ref 中有 `matmul` / `tl.dot`
- `elementwise` / `elementwise_add` / `elementwise_mul` / `elementwise_copy`：1D `N` 向量映射
- `reduction` / `unknown`：**不**自动生成 — agent 编写 `kernel.py`

HIPC/CUDA `.hip` / `.cu` 输入：`inspect_ref.py` 解析 `__global__` kernel。当前自动支持：

- GEMM 形 dims (`M,N,K`) → Triton `tl.dot` matmul baseline
- `atomicAdd` / 单输入 reduction 模式 → Triton block-sum + `atomic_add` baseline
- 简单 1D elementwise add/mul/copy

对于其他 HIPC/CUDA 情况，手写 `kernel.py` 或创建此 skill 外部的项目特定 baseline。

### 2. 生成 baseline case

```bash
python <baseline-skill>/scripts/generate_baseline.py \
  --analysis <case-dir>/ref_analysis.json \
  --out-dir <case-dir>
```

可选：`--op matmul` 或 `--output-name out` 覆盖自动分类。

如果脚本以非零退出并提示"需要 agent 编写的 kernel.py"，读取 `baseline_manifest.json` / `unsupported_assumptions`，手写 `kernel.py`，然后进入步骤 3。

### 3. 在 HCU 上验证（必需门控）

通过项目远程工作流在远程 HCU 上运行（远程主机与容器名由环境变量 `${HCU_HOST}` / `${HCU_CONTAINER}` 或项目配置提供，示例：`<your-hcu-host>` / `<your-triton-container>`）：

```bash
python <baseline-skill>/scripts/validate_case.py \
  --case-dir <case-dir> \
  --optimizer-skill <optimizer-skill>
```

这会运行 optimizer 的 `preflight.py` 和 `benchmark.py --disable-autotune`。在此通过之前不要启动 `orchestrate.py setup`。

### 4. 交接给优化器

```bash
python <optimizer-skill>/scripts/orchestrate.py setup \
  --baseline <case-dir>/kernel.py \
  --ref <case-dir>/ref.py \
  --iterations 1 \
  --branches 2 \
  --disable-autotune
```

可选：仅当 optimizer 运行应选择/覆盖支持的 shape 时传递 `--dims '<json>'`。

## 规则

- 保持 baseline 保守；仅使用固定的 `DEFAULT_CONFIG`（无 `@triton.autotune`）。
- 在 `setup()` 返回字典中记录 `active_config` / `config_source` 用于固定配置 profiling。
- 不要复制 aiter MoE/attention 业务 kernel；当语义不清楚时使用 manifest + 手写包装器。
- PyTorch tensor 使用 `device="cuda"`（HCU 上的 ROCm/HIP 栈）。

## 参考资料

- `references/ref_to_triton_baseline_patterns.md`
