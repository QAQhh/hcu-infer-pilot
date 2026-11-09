---
name: hipblaslt-rocblas-tuning
description: 抓取模型真实 GEMM，对 hipBLASLt 和 NMZ rocBLAS 做幂次 token M 调优、最近兼容点配置补齐，并验证单算子精度与性能。适用于 AMD/海光 GPU 上 BLAS tuning 和配置交付；不覆盖自定义 MoE/Marlin kernel 调优。
---

# hipBLASLt / rocBLAS GEMM 调优

用户要求的核心流程：输入 **32768 tokens、输出 1 token** 抓取 GEMM；按真实本地 token M 上限调优 `1,2,4,8,…,cap`；同一 family 内复制最近调优点补齐全部整数 M；验证目标尺寸的单算子精度及前后耗时。

先读 [完整流程与命令](references/workflow.md)。执行 NMZ rocBLAS 分支时读 [原生配置与版本约束](references/native-config.md)；做单算子验证时读 [验证范围与验收](references/validation.md)。

## 必须保留的约束

- 从模型调用/张量布局确认 token 轴。TN 权重左乘常把 token M 记作 BLAS `-n`；32k、CP8→4096 只是已验证例子，不能直接硬编码。其他算子如 logits 可能只有 M=1。
- family 保留固定维度、dtype、compute/scale、transpose、batch、ld、stride、alpha/beta、epilogue。仅改变确认的 token 轴及随其变化的 stride。多头 batched B stride 可固定。
- cap 非幂次时补调 cap 本身；全部整数目标 `1..cap` 都要有配置、来源映射和目标实测耗时。模型内部 chunk/CP padding 会改变实际 cap；32k 单个请求也不保证发现动态 batching 或其他路径的全部 family。
- “最近”按绝对距离，平局取较小 M。kernel 不支持目标形状时按距离尝试下一个**同 family**调优点，记录实际来源。全部不支持或精度失败时停止该 family 的交付，诊断并增加所需点；不能静默留下空洞。
- config 复制的 `us/gflops` 是源点数据，不能冒充目标点实测值。单独产出全 M 测量 CSV；保留慢于 baseline 的结果。
- 使用当前 GPU 架构/CU、实际加载的库、匹配 bench/tuner。原生 solution index 与构建绑定。先固定版本和文件哈希，再生成 plan；不可跨构建、dtype 或布局复用。
- 调优目录和运行时配置用隔离副本。hipBLASLt override 与 rocBLAS 的 native library 目录分别交付；不覆盖系统库。profile/log 的 kernel 命中证据是实际加载确认的一部分。
- 按本次用户范围操作：整理 skill 时只写文件；实际抓取/调优时按用户指定节点、容器和脚本执行。遵从最近一次服务运行/停止要求，不自动重启已停止服务，不停止无关任务。无需重复询问已授权步骤。

## 附带工具

工具自身使用 Python 标准库；roc vendor 分支还依赖外部框架及其环境，C++ 验证依赖匹配 HIP/BLAS SDK。脚本路径相对本 skill：

| 工具 | 用途 |
|---|---|
| `scripts/capture_32k.py` | 已启动专用服务的精确 token 请求、warmup 后清 cache、日志字节边界及可选 prof；不启动服务 |
| `scripts/identity.py` | 当前库/工具文件 SHA256、GPU 和 Git Version 清单 |
| `scripts/gemm_plan.py` | 严格日志解析、完整 family 分组、幂次计划、hip native / roc CSV 最近点补齐 |
| `scripts/tune_hip.py` | 匹配版 hipblaslt-bench 全 heuristic 搜索，逐点日志及原生 config |
| `scripts/roc_vendor.py` | NMZ 外部 rocblas-autotune 的隔离复制、搜索及 native 配置生成；非通用 ROCm API |
| `scripts/verify_operators.py` | 编译并运行限定 TN INT8/BF16 C++ 验证器，全整数 M 检查与 GPU event 计时 |
| `scripts/report.py` | 各 family 上限 M 耗时、加速比、全范围统计和退化明细 |
| `scripts/self_check.py` | 无服务、无 GPU 的离线回归；可加 `--historical-run` 验证旧产物兼容性 |

[布局规则样例](assets/layout-rules.nmz-tn.json) 和 [NMZ tuner 配置样例](assets/nmz-tuning-args.txt) 是已验证布局的模板，使用前按当前捕获修改。其他 FP8、NN、融合 epilogue 或不同 vendor 框架须选匹配适配器，不能用本附带 INT8/BF16 验证器冒充覆盖。

## 完成标准

交付环境/文件哈希、32768/1 请求响应、原始日志/prof、family/幂次计划、逐点 tuning 结果、完整 native 配置、每个目标 M 的复制来源、baseline/tuned 精度与耗时 CSV、退化列表及运行时 kernel 命中证据。报告明确区分合成抽样算子检查、真实张量验证和用户另行要求的数据集精度；没有实际运行的步骤标为未运行。
