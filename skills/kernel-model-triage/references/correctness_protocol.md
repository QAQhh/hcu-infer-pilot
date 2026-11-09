# HCU Correctness and Accuracy Protocol

## 目录

1. 等价性契约
2. 算子测试矩阵
3. 数值误差
4. backward 与副作用
5. 模型级回归定位
6. 判定和回退

## 1. 等价性契约

先写必须保持的语义：shape/dtype/device/stride、排序和稳定性；NaN/Inf、边界与 rounding；重复项/tie-break/截断；alias/in-place/副作用/缓存；forward、所有梯度和高阶梯度。

对 voxelize、NMS、top-k、采样、scatter/gather 等，shape/count 相同远远不够。

## 2. 算子测试矩阵

至少覆盖生产 shape/dtype、small/medium/large、尾部、non-contiguous、空/单元素、零/常量/正负、边界、重复索引、最大容量、极值/非有限值、不同 arch dispatch/fallback/fast path 和重复运行。

reference 优先级：规范/数学定义 → 框架原生 → 已接受实现 → 高精度 CPU。两个 GPU 实现一致不等于正确。

## 3. 数值误差

- 报告 max/mean absolute、max/mean relative、RMSE、mismatch count 和非有限值位置。
- 接近零时同时检查 absolute error。
- 大归约可用随规模增长的误差模型，但不能无限放宽。
- FP16/BF16 路径通常用 FP32 reference 和任务级门禁。
- 使用逐元素 `|a-b| <= atol + rtol*|reference|`。
- 只有 contract 允许同位置 NaN 时才启用 `equal_nan`。

阈值在看到候选结果前确定并记录理由。

## 4. backward 与副作用

- 分别比较每个可导输入梯度。
- 小规模 double 可用 gradcheck/finite difference；复杂路径与可信 autograd/reference 对比。
- 覆盖零梯度、累加冲突、重复索引和 arch 宏分支。
- 检查未写梯度、错误广播、atomic 非确定性、workspace 复用和 stream race。
- 测试多次 forward、retain_graph、不同 stream 和连续 shape 变化（如支持）。

## 5. 模型级回归定位

1. 锁定同一 checkpoint、batch、seed 和执行开关。
2. 列出基线与候选实际代码/compile/layout 路径。
3. 在模块边界找第一个 forward 发散点。
4. 在同一 loss 找第一个 backward 发散点。
5. 对该算子建立真实-shape reference。
6. 短训练仅确认直接修复；全量训练/评测作最终门禁。

孤立 `grad_norm=nan/inf` 只触发诊断，不能单点误杀。

## 6. 判定和回退

```text
PASS: contract 全部满足，模型级门禁通过。
PASS_WITH_BOUNDARY: 仅明确 shape/dtype/arch 范围通过，dispatch 有 fallback。
INCONCLUSIVE: reference、阈值或覆盖不足。
FAIL: 任一关键语义、梯度或任务指标不满足。
```

高风险优化必须显式可回退；默认开启前需要生产 shape、当前架构、E2E 精度、重复稳定和 fallback 测试。
