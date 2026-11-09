# HIP Kernel Tuning Gate

只有 profiler 证明某个自定义 HIP kernel 显著影响目标端到端指标时，才进入本流程。所有硬件参数和优化机理以当前目标机证据为准；未知值写 `UNKNOWN`，不要在 gfx926/gfx936/gfx938 或不同 BW SKU 之间照搬。

## 目录

1. 进入门禁
2. 采集目标硬件和构建证据
3. 建立四方基线
4. 静态风险扫描
5. 建立性能模型
6. 生成和实现候选
7. 三联门禁与接受标准

## 1. 进入门禁

开始改 kernel 前必须同时具备：

- exact source、wrapper 和 build entry；
- 目标设备属性、runtime wave size 和实际 compiled architecture；
- 生产 shapes、dtype、stride/layout、alignment、stream 和调用频率；
- CPU/框架/已接受实现作为 forward/backward reference；
- warmup、repetitions、同步方法、原始 latency 样本和 E2E 占比；
- 已知边界语义：空输入、tail、mask、重复、排序、截断、alias 和非有限值；
- 安全 fallback 和 rollback。

任一项未知时先测量或探测，不用记忆中的 BW/ROCm 数值代替。

## 2. 采集目标硬件和构建证据

记录并交叉验证：

- 产品名、`gcnArchName`、CU、runtime `warpSize`、驱动、DTK/HIP、hipcc/clang 和 torch；
- 实际 `--offload-arch`、架构宏、加载的 `.so` 路径/hash；
- per-kernel VGPR、SGPR、LDS、scratch/spill 和 launch metadata；
- profiler 可用工具/counter、时钟、功耗和温度状态；
- launch block/grid、dynamic shared memory、stream 和 occupancy 限制。

对 L2、LDS bank、峰值带宽/算力、MFMA、atomic lowering 等，优先使用目标版本官方规格、runtime probe、编译/反汇编和微基准；不能从其他型号推断。

## 3. 建立四方基线

尽可能保留：

```text
CPU/framework oracle
CUDA original（若确有可信原始实现）
HIP direct correctness port
HIP optimized candidate
```

同一序列化输入和 `grad_output` 覆盖生产/边界 shape、dtype/layout、forward、每个梯度、重复运行和非默认 stream。先证明 direct port 正确，再优化。

## 4. 静态风险扫描

运行：

```bash
python <skill>/scripts/scan_hip_kernel.py <source-or-directory> --format text
```

扫描结果只用于定位人工审查点，不能代替编译、profile 和 correctness。重点检查：

- CUDA 32-lane logical group 是否被错误改为 native wave64；
- shuffle width/active lanes、ballot/mask、partial reduction 和 tail block；
- `__syncwarp`、LDS producer/consumer、barrier 和 memory ordering；
- runtime-sized static shared array、bank/padding 假设、scratch/spill；
- 仅针对一个 gfx 架构的正确性路径、raw builtin/MFMA/atomic fast path；
- 默认 stream、缺 device guard/launch check、dtype/stride contract；
- wrapper 中多余的 `contiguous()`、clone、zero 和 temporary allocation。

架构路径必须有精确 compiler/arch gate 和通用 HIP fallback；不能把 `__gfx936__ || __gfx938__` 当作特性证据。

## 5. 建立性能模型

同时记录算法和实测两侧：

- 算法 FLOPs 和最小读写字节；
- profiler 的 DRAM/L2 traffic；
- 当前 dtype 的可持续带宽/矩阵基线；
- launch 数、grid/block、waves/block、活跃 CU 和 atomic 冲突度；
- occupancy 限制、关键依赖链和 wrapper/E2E 占比。

tensor 逻辑大小之和不能冒充物理 DRAM traffic。Roofline 只能使用匹配 dtype、当前设备和当前软件栈的可信数据。

## 6. 生成和实现候选

通常按以下顺序建立假设：

1. 消除 wrapper/layout/allocation 和多余同步；
2. 融合小 kernel 或改变算法，减少全局 round-trip；
3. 改并行所有权，降低冗余计算和高冲突 atomic；
4. scatter→gather、分桶、排序或两阶段归约；
5. 合并/对齐访问、缓存复用和 LDS tile；
6. logical subgroup reduction、有效 lane 和分支；
7. VGPR/SGPR/LDS 生命周期、spill 和 launch sweep；
8. 生产 shape 稳定时做精确 shape specialization；
9. 只有 compile+ISA+correctness+microbench 证明时才采用 raw builtin、MFMA 或 direct-to-LDS。

一次只实现一个候选：

- 保留 generic correct fallback，显式声明 shape/dtype/layout/arch 条件；
- 使用 caller 的 current stream、device guard 和 launch error check；
- 静态 shared memory 使用编译期常量，动态大小使用 `extern __shared__`；
- logical group=32 时显式验证 31/32/33/63/64 等 active count；
- 数值关键长归约先比较 pairwise/分层/补偿 FP32，再评估更高精度代价；
- 不承诺固定加速比。

## 7. 三联门禁与接受标准

每个候选依次通过：

1. **compile/ISA**：声明支持的目标均能 clean build；确认实际 binary、资源、spill 和关键指令。
2. **correctness/safety**：生产/边界 forward、每个 backward、确定性、非默认 stream、OOB/race 工具（按环境能力）。
3. **performance/E2E**：稳定 microbenchmark、完整 operator、模型稳定窗口；保存 median/P90/P95/CV/CI 和原始样本。

候选只有在 correctness、声明 arch build/dispatch、microbenchmark、完整 operator 和目标 E2E 均通过，且显存/功耗/稳定性不超限，并保留复现证据与回退时，才能标 `VALIDATED`。

microbenchmark 提速但 operator/E2E 无收益时标 `MICRO_ONLY` 或回退；其他失败标 `INCONCLUSIVE`/`REJECTED`，不要只报告最好看的 shape。

输出至少包含：operator contract、硬件/构建证据、瓶颈与理论上限、候选 KEEP/REVERT、ISA/资源变化、forward/backward 结果、kernel/operator/model 统计、资源影响、dispatch 边界、fallback 和复现产物。
