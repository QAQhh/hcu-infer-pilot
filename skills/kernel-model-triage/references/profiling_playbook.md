# HCU Profiling Playbook

## 目录

1. 先回答的问题
2. 分层工具选择
3. Trace 解释
4. 从 operator 下钻到 kernel
5. 常见误判

## 1. 先回答的问题

一次 profiling 只为区分少量假设：CPU/data、通信、runtime/graph、库算子、自定义算子、单 kernel。先写问题和期望信号，再选择工具；不要默认开 full trace 跑长训练。

## 2. 分层工具选择

- 训练日志/stage timer：低开销定位 data/forward/backward/optimizer/EMA。
- PyTorch profiler：短 schedule，通常仅 rank 0 写 trace。
- Dynamo/Inductor：graph break、recompile、cache、generated code/layout。
- MIOpen/rocBLAS：算法/find/workspace，只在隔离实验启用。
- xprof/rocprof/供应商工具：先确认当前版本和 counter 支持。
- RCCL tests：测通信，不用模型 step time 反推链路。
- 编译证据：arch、VGPR/SGPR、LDS、spill、ISA 与实际 binary。

工具版本、命令、rank、schedule 和 overhead 都写入 manifest。

## 3. Trace 解释

- 区分 inclusive 与 self time。
- GPU 空洞可能是 CPU launch、同步、data wait、allocator 或 rank wait。
- device synchronize、`.item()`、CPU copy、日志和 profiler event 会切断异步流水。
- compile/autotune 反复出现时查 graph break、dynamic shape 和 cache key。
- 多 rank trace 对齐时间并找 straggler。

## 4. 从 operator 下钻到 kernel

只有满足以下条件才进入 kernel 优化：operator 位于关键路径且占比可观、有 correctness reference、wrapper/layout/allocation 已分离、shape/dtype/launch/call frequency 已知、理论上限足以影响 E2E。

依次检查 launch/fusion、lane→address、atomic/sync、wavefront 有效 lane、VGPR/SGPR/LDS/spill、指令/依赖链和 grid/block/CU 覆盖。硬件结论以当前 runtime、编译或 profiler 证据为准。

## 5. 常见误判

| 现象 | 可能误判 | 最小区分实验 |
|---|---|---|
| 首轮很慢 | kernel 慢 | 分离 compile/autotune 与 steady state |
| 单卡快多卡慢 | RCCL 差 | RCCL microbench + per-rank stage + CPU/NUMA |
| GPU util 低 | 需要更大 block | 看 CPU launch/data/sync 和 grid |
| microbench 提速大 | 模型会等比例提速 | operator E2E + 模型稳定窗口 |
| profiler OOM | 模型显存不足 | 无 profiler 复现 + trace schedule |
| loss 漂移 | 训练随机性 | 同 batch 前后向断点 + reference |
| occupancy 低 | 一定要提高 occupancy | 看 latency hiding、ILP、带宽/计算和 E2E |
