---
schema_version: 1
owner: yangyinan
license: MIT AND Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/lightop-kernel-agent-loop
---
# Skill 说明卡

## 概述

在 DCU/ROCm 上运行新增或优化 LightOp 融合算子的HIP 证据驱动闭环：恢复 K/R/W，检查绑定和测试，实现 HIP/ROCm kernel 或分发修改，构建、测试、基准测量，使用 dcu-profiler-report 分析性能，记录 profile/ISA 证据并进行消融归因。

## 维护者

yangyinan

## 来源

在 `das/SkillHub` 中本地维护，路径为 `skills/lightop-kernel-agent-loop`。

## 许可证

声明为 `MIT AND Apache-2.0`；完整条款、来源署名和适用的混合包范围见内置 [LICENSE](LICENSE)。提供的来源声明为 MIT；此次导入不会重新许可这些内容。

## 运行环境与权限

工具、GPU、容器、网络和产物写入要求见 [SKILL.md](SKILL.md) 及其链接的领域参考。本流程不依赖外部循环运行时或 hook。导入不会自动执行推理或 GPU 调优。优化规则见 [HIP 优化规则](references/hip-optimization-rules.md)。

## 本地目录导入

此副本在 `das/SkillHub` 的 `skills/lightop-kernel-agent-loop` 中维护，不与上游同步。现有说明、署名和验证陈述描述的是导入来源，发布此副本前需复核其适用性。导入器没有执行 Skill 代码。

补充来源或署名：一次性从 lightop-skiils/humanize/skills/humanize-kernel-agent-loop/SKILL.md 导入领域 Skill。由 yangyinan 维护，保留原始作者署名及领域许可证声明；纳入目录不代表声明原创。Humanize 仅为历史来源署名，当前流程不再集成其运行时。 独立的 LightOp 设备带宽辅助脚本保留自提供的 LightOp 专用补充内容；记录的官方 Humanize 源码树中没有该脚本。
