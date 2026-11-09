---
name: kernel-model-triage
description: 面向海光 HCU/BW 系列、HIP/DTK、PyTorch/torch.compile、自定义算子和真实模型工作负载的一体化测试、性能诊断、精度回归定位与优化闭环。适用场景：通用或未单独覆盖的 HCU 训练/推理任务、单卡或多卡性能下降/OOM/编译问题、模型到 HIP kernel 的跨层诊断，以及 Hygon-Hub 自动驾驶、HCU LLM/VLM、DriveDreamer、LingBot-VLA 等工作负载的验收与优化。不适用场景：非海光 HCU 平台、只需要设备状态查询的简单任务，或没有可比基线和正确性 reference 却要求直接改写 kernel 的任务。
license: Apache-2.0
metadata:
  author: HCU Optimization Team
  version: 0.4.0
---

# HCU Model and Kernel Optimizer

把“更快”做成可复现、可解释、可回退的工程结论。先保护基线并证明瓶颈，再选择 runtime、数据、分布式、模型、算子或 kernel 层的最小有效改动。

本 Skill 在流程知识、参考材料和随附分析脚本层面自包含，不依赖其他个人 Skill；它不捆绑 DTK、profiler、RCCL tests、模型、数据、checkpoint 或项目 evaluator。目标环境缺少外部执行器时标 `NOT_AVAILABLE`，不要编造或静默安装。

路径规则：把包含本 `SKILL.md` 的目录解析为 `<skill>`。不要假设当前项目或当前工作目录中存在 `skills/...` 相对路径；运行脚本前先验证 `<skill>/scripts/<script>` 存在。

## 按需读取

- 设计实验、选择稳定窗口或判断收益是否超过噪声时，读取 `references/measurement_protocol.md`。
- 建立算子/模型精度门禁或定位 accuracy regression 时，读取 `references/correctness_protocol.md`。
- 选择 profiler、解释 trace 或从模型热点下钻到 kernel 时，读取 `references/profiling_playbook.md`。
- profiler 已证明 HIP kernel 是端到端热点时，读取 `references/hip_kernel_tuning.md`。
- 处理 Hygon-Hub 自动驾驶、HCU LLM/VLM、DriveDreamer 或 LingBot-VLA 时，读取 `references/workload_playbooks.md` 中对应章节。
- 需要复现清单、交付证据和回退方案时，读取 `references/validation_and_repro.md`。
- 需要历史模型经验和失败模式时，读取 `references/case_studies.md`；历史数值不是当前基线。

## 自包含工具

| 任务 | 脚本 |
|---|---|
| 采集默认脱敏的 HCU/软件环境快照 | `scripts/collect_hcu_snapshot.sh` |
| 统计 benchmark 样本、分位数和 bootstrap CI | `scripts/benchmark_stats.py` |
| 安全比较 `.pt/.pth` 张量树 | `scripts/compare_tensors.py` |
| 静态扫描 HIP kernel 的 wave/LDS/stream/arch 风险 | `scripts/scan_hip_kernel.py` |
| 汇总 MMDetection 风格训练日志稳定窗口 | `scripts/summarize_mmdet_log.py` |
| 汇总 DriveDreamer stage timing | `scripts/analyze_step_timings.py` |
| 提取并统计 LingBot-VLA 当前运行日志 | `scripts/extract_current_log.py`、`scripts/parse_lingbot_step_times.py` |

脚本只提供确定性采集和分析，不能替代 profiler、正确性 reference 或人工审查。

## 不可跳过的证据链

一个优化结论必须同时回答：

1. 模型、commit/diff、镜像、数据、checkpoint、seed、shape、dtype、batch、world size 和入口是否一致？
2. 是否排除 compile、autotune、profiler flush、数据冷启动、DVFS 和后台负载，并保存稳定重复与离散度？
3. 是否覆盖生产 shape、边界语义、forward/backward、非有限值、顺序/截断和模型级指标？
4. microbenchmark 收益是否传导到完整 operator、模型稳定窗口和目标卡数/并发？
5. 是否保存命令、日志、环境快照、补丁、原始数据、适用边界和 rollback？

任一项缺失都标记为 `PROVISIONAL`，不要声称已经完成优化。

## 工作流

### 1. 锁定目标与验收标准

把用户目标写成可判定 contract：工作负载、主指标、正确性指标、资源/权限约束、最低收益和噪声门槛。未给最低收益时先测量噪声，再提出可检测阈值。

### 2. 保护现场并生成 run manifest

先读需求、README、启动脚本、配置、最近成功日志、当前 diff 和已有工具。把工作区现有改动视为用户基线，不回滚。

记录 host/硬件/runtime、容器 image 与 HostConfig、commit/diff、checkpoint/data fingerprint、seed、完整命令、环境变量白名单、设备/CPU/NUMA/线程设置、日志/trace/样本和回退路径。

可运行：

```bash
bash <skill>/scripts/collect_hcu_snapshot.sh > hcu_snapshot.md
```

默认保持标识符脱敏，但拓扑、软件版本和白名单变量仍可能敏感，分享前必须复核。不要记录 token、密码、SSH 私钥或完整环境变量。外部 checkpoint 优先使用 `safetensors`；把 pickle-backed 文件视为可执行输入，在限大小、无网络、非 root、无宿主 secrets 的隔离环境中验证来源和加载边界。`weights_only=True` 不是完整沙箱。

### 3. 建立可信基线

- 运行项目原生入口，不静默改变 batch、workers、compile、layout、checkpoint 或优化开关。
- 先通过最小 correctness smoke，再采集性能。
- 分开 cold start、compile/autotune 和 steady state。
- 保存每次迭代或请求的原始样本。
- 至少覆盖生产 shape、目标卡数和并发；synthetic case 只用于诊断。

用 `<skill>/scripts/benchmark_stats.py` 计算统计与 bootstrap CI；只有样本确实逐对匹配时才使用 `--paired`。

### 4. 从上到下定位瓶颈

依次排除：测量污染 → CPU/数据 → 分布式 → runtime/graph → 模型/算子 → 单 kernel。每个判断写成“证据 → 推论 → 下一实验”；无法区分的假设用最小 A/B 隔离。

### 5. 一次只验证一个假设

```text
Hypothesis:
Single change:
Expected signal:
Correctness gate:
Performance gate:
Observed evidence:
Decision: KEEP | REVERT | INCONCLUSIVE
```

优先顺序通常是：测量/配置修复 → 数据与分布式 → graph/layout/cache → 算法/融合 → kernel 微优化。

### 6. 运行精度门禁

- 同一 checkpoint/batch/seed 做逐层 forward/backward 对比，定位第一个发散点。
- 自定义算子覆盖生产 shape、空输入、边界、重复/排序/截断、所有梯度和架构分支。
- 按 dtype、归约长度和任务敏感性定义阈值。
- 检查 NaN/Inf、非确定性、side effect、alias/layout 和顺序语义。
- 高风险快路径保留显式 fallback；未完成门禁时默认关闭。

可使用 `<skill>/scripts/compare_tensors.py` 生成逐 key 误差 JSON。它不能验证 stride、alias、stream、副作用或自动生成 backward；这些必须由测试 harness 覆盖。默认安全加载；`--unsafe-pickle` 只用于来源完全可信的文件。

### 7. 逐级验证收益

```text
kernel microbench
  → 完整 operator forward/backward
  → 单模型稳定窗口
  → 目标卡数/并发/数据
  → 任务精度或完整评测
```

任一层收益消失、精度失败、资源超限或维护成本不合理，就回退或缩小适用边界。

### 8. 交付与停止

只保留通过全部门禁的改动。目标已达到、收益上限低于噪声、候选失败或需要扩大权限/高风险操作时停止并请求用户方向。

## 安全与远程边界

- 远程执行先做只读侦察，再做最小变更；不持久化密码、私钥或内部地址。
- 把用户已接受容器的 HostConfig 作为复现证据逐项审查，不整体照搬 privileged、host network、敏感挂载或凭据。新建容器从最小设备映射、bridge 网络、非 root 和只读模型/驱动挂载开始。
- 只有实际失败证明需要时才增加 privileged、host network、`SYS_PTRACE` 或 unconfined seccomp，并记录理由。
- 创建/停止/删除容器、杀进程、固定时钟、覆盖源码、修改生产配置或安装宿主机软件前，确认用户授权并保留回退。
- 模型服务默认只监听回环地址；外部暴露、API key、端口和防火墙变更必须单独授权。

## 输出格式

```text
Status: VALIDATED | PROVISIONAL | REJECTED
目标与验收：
基线与环境：
瓶颈证据：
实验与决策：
保留/回退改动：
性能结果（原始样本与统计）：
精度/稳定性结果：
资源变化：
复现命令与产物：
适用边界、风险和下一步：
```

历史数值只标为 dated evidence；当前结论必须来自本次运行或用户明确接受的 baseline。
