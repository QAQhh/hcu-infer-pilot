---
schema_version: 1
owner: yangyinan
license: Apache-2.0
lifecycle: published
visibility: internal
source:
  repo: das/SkillHub
  path: skills/lightop-kernel-knowledge
---
# Skill 说明卡

## 概述

在 DCU/ROCm 上新增或优化 LightOp 融合算子且需要上游证据时使用：检查本地源码、测试和配置，检索 ROCm/HIP/MIOpen/rocBLAS/hipBLASLt/Composable Kernel/Triton AMD/PyTorch ROCm/SGLang 或 vLLM AMD 实现，查阅官方 DCU/DTK/ROCm 文档；内置 CUDA PR 语料仅用于跨平台启发。

## 维护者

yangyinan

## 来源

在 `das/SkillHub` 中本地维护，路径为 `skills/lightop-kernel-knowledge`。

## 许可证

声明为 `Apache-2.0`；参见原始来源许可，以及保留的 LICENSE/NOTICE 材料。导入不会重新许可这些内容。

## 运行环境与权限

工具、GPU、容器、网络和产物写入要求见 [SKILL.md](SKILL.md) 及其链接的领域参考。本流程不依赖外部循环运行时或 hook。导入不会自动执行推理或 GPU 调优。离线索引查询需要 Python 3.10+、PyYAML 6+ 和可写的用户缓存；完整证据快照仍是可选外部输入。

## 本地目录导入

此副本在 `das/SkillHub` 的 `skills/lightop-kernel-knowledge` 中维护，不与上游同步。现有说明、署名和验证陈述描述的是导入来源，发布此副本前需复核其适用性。导入器没有执行 Skill 代码。

补充来源或署名：一次性从 lightop-skiils/knowledge/SKILL.md 导入领域 Skill。由 yangyinan 维护，保留原始作者署名及领域许可证声明；纳入目录不代表声明原创。Humanize 仅为历史来源署名，当前流程不再集成其运行时。
