# HG-AI-Infra-SKILLS

`HG-AI-Infra-SKILLS` 是一套面向 LLM Serving、性能分析、线上故障排查、模型优化历史检索和 DCU/ROCm kernel 经验沉淀的 Codex Skills 仓库。它把常见的 AI Infra 工作流拆成可复用的 skill、知识库和辅助脚本，方便你在同一个仓库里完成 benchmark、profiling、PR 分析、历史查询和优化闭环。

这个仓库适合下面几类工作：

- 比较 SGLang、vLLM、TensorRT-LLM 在同一模型、同一 workload 下的部署效果
- 分析 `torch.profiler` trace，定位 kernel、overlap、fusion 和 bubble 问题
- 查询模型架构图、社区 PR 优化历史、本地提交历史
- 排查 SGLang 线上服务异常
- 围绕一个模型持续做 SGLang SOTA 优化闭环
- 为 LightOp / DCU / ROCm 场景查找 kernel 证据、profiling 证据和下一步优化方向

## 仓库内容

仓库大体分成三类内容：

1. **直接可用的 skills**：可以作为对话指令使用，比如 `$llm-torch-profiler-analysis`。
2. **知识库型内容**：如 `model-pr-optimization-history`、`model-pr-optimization-hg-history`，用于为优化判断提供历史证据。
3. **辅助脚本与测试**：用于生成、校验、查询和回归测试这些 skills。

## Skills 总览

### 1. `llm-serving-auto-benchmark`

作用：跨框架 LLM Serving benchmark。适合比较 SGLang、vLLM、TensorRT-LLM 或其他 serving 框架在同一模型、同一 workload、同一 GPU 预算下的表现。

典型能力：

- 基于 cookbook 或本地配置生成候选启动命令
- 校验框架 CLI 参数是否真实存在
- 汇总 benchmark 结果并输出对比表
- 保留失败/跳过候选，便于复盘

推荐提示词：

```text
$llm-serving-auto-benchmark
工作目录是：<路径> 工作容器是：<容器名>
请针对模型 <模型名>，在 <GPU型号/数量> 和 <SLA> 约束下，对比 SGLang、vLLM 的最佳部署参数。
请先确认可用 cookbook / 启动命令，再设计候选搜索空间，最后输出可执行的 benchmark 方案和结果汇总格式。
```

### 2. `llm-torch-profiler-analysis`

作用：统一分析 LLM Serving 的 `torch.profiler` trace，支持 SGLang、vLLM

典型能力：

- 分析已有 `trace.json` / `trace.json.gz`
- 对 live server 进行 profiling
- 输出 kernel、overlap-opportunity、fuse-pattern、bubble-gap 分析
- 必要时生成模型结构图并嵌入报告

推荐提示词：

```text
$llm-torch-profiler-analysis
工作目录是：<路径> 工作容器是：<容器名>
请分析这个 trace 目录 / 文件：<trace 路径>。
模型是 <模型名>，框架是 <SGLang/vLLM/TensorRT-LLM>。
请输出一份完整的中文 triage 报告，包含 kernel、overlap、fuse-pattern、bubble-gap 和模型结构图。


工作目录是：<路径> 工作容器是：<容器名>
根据提供的起服务脚步指令，抓取输入4k输出1的trace并进行分析
模型是 <模型名>，框架是 <SGLang/vLLM/TensorRT-LLM>。
请输出一份完整的中文 triage 报告，包含 kernel、overlap、fuse-pattern、bubble-gap 和模型结构图。
```

### 3. `model-architecture-diagram`

作用：查询公开的原始模型架构图，适合 LLM、VLM、MoE、diffusion、OCR 等模型族。

典型能力：

- 返回公开原始图片链接
- 附带来源说明
- 找不到时明确返回 `no_match`

推荐提示词：

```text
$model-architecture-diagram
工作目录是：<路径> 工作容器是：<容器名>
请帮我查询 <模型名> 的公开原始架构图，返回可直接引用的图片 Markdown 和来源说明。
如果没有可用图，请明确告诉我没有匹配结果。
```

### 4. `model-compute-simulation`

作用：做 operator 级的计算模拟，估算 FLOPs、tensor shape、MFU，并用于并行方式和算子路径的 what-if 分析。

典型能力：

- 展开模型的 operator 序列
- 计算关键算子的 FLOPs / tensor shape
- 根据延迟估算 MFU
- 分析 TP / DP / batch / sequence 长度变化的影响

推荐提示词：

```text
$model-compute-simulation
工作目录是：<路径> 工作容器是：<容器名>
请基于模型 <模型名> 和 serving shape <batch/seq/并行配置>，展开 operator 级计算模板，估算关键算子的 FLOPs、tensor shape 和 MFU。
请同时给出不同并行策略或 batch 设定下的对比结论。
```

### 5. `sglang-prod-incident-triage`

作用：SGLang 线上故障排查，采用 replay-first 的流程先还原问题，再决定用 profiler、trace、coredump 还是分布式调试工具。

典型能力：

- 处理 health check 异常
- 排查延迟、吞吐、queue 堆积、timeout、hang
- 分析 crash dump、输出错误、PD/EP/HiCache 问题
- 采集现场 bundle 并回放请求

推荐提示词：

```text
$sglang-prod-incident-triage
工作目录是：<路径> 工作容器是：<容器名>
请帮我排查 SGLang 线上问题。
现象是 <错误现象>，服务地址是 <base url>，我手头有 <日志/请求样本/crash dump/trace>。
请先给出现场采集、回放和下一步 debug 的顺序，不要一上来就做 profiling。
```

### 6. `sglang-sota-humanize-loop`

作用：围绕一个模型自动跑 SGLang SOTA 优化闭环，先做公平 benchmark，再做 profiler 对比，再进入 patch 与 RLCR 迭代。

典型能力：

- 对比 SGLang / vLLM / TensorRT-LLM
- 找出差距并定位根因
- 结合历史知识库和 profiler 证据做 patch
- 迭代到追平或超过最优结果

推荐提示词：

```text
$sglang-sota-humanize-loop
请针对模型 <模型名>，在 <目标环境> 下启动 SGLang SOTA 优化闭环。
请先完成公平 benchmark，再分析领先框架的 profiler 证据，随后给出可执行 patch、验证计划和持续迭代策略。
```

### 7. `vllm-pr-summary`

作用：分析 vLLM 的某个 GitHub PR，输出中文结构化总结、代码分析、技术原理、讨论亮点和风险评估。

典型能力：

- 拉取 PR 数据和 diff
- 生成带 Mermaid 图的报告
- 适合 review、学习和决策前阅读

推荐提示词：

```text
$vllm-pr-summary
请分析 vllm 的 PR #<PR号>，输出一份中文总结报告。
要求覆盖背景、代码修改、技术原理、讨论亮点和风险分析，并给出最终结论。
```

### 8. `model-pr-optimization-history`

作用：查询开源社区 PR 历史，专门为 SGLang / vLLM / TensorRT-LLM 的模型优化提供证据。

典型能力：

- 查找某个模型在社区里做过哪些优化
- 对比 fast path、fusion、overlap、MoE、attention、cache、sampler 等方向
- 为后续 patch 选择提供历史依据

推荐提示词：

```text
$model-pr-history-knowledge
请帮我查询开源社区里与 <框架> / <模型> / <优化方向> 相关的 PR 历史。
重点告诉我之前做过哪些 fast path、fusion、overlap、cache 或 sampler 相关改动，以及它们对当前问题的启发。
```

### 9. `model-pr-optimization-hg-history`

作用：查询本地 `sglang` / `vllm` 工作树中的提交历史，和开源社区 PR 历史互补。

典型能力：

- 查找本地 fork 里的模型优化提交
- 按模型、模块、优化主题检索
- 为 profiling 和 patch 选择提供本地证据

推荐提示词：

```text
$model-pr-history-knowledge
请帮我查询本地仓库里与 <框架> / <模型> / <优化方向> 相关的提交历史。
重点告诉我本地 fork 已经有哪些类似优化、对应文件在哪里、以及我接下来该优先看哪条路径。
```

### 10. `lightop-kernel-knowledge`

作用：面向 LightOp / DCU / ROCm 的 kernel 证据检索 skill，优先查本地实现，再查 ROCm / PyTorch / upstream 证据。

典型能力：

- 找对应 operator 的本地实现与测试
- 查 dispatcher、binding、config table
- 参考 ROCm / HIP / MIOpen / rocBLAS / Triton AMD 证据
- 判断一个 CUDA 思路如何迁移到 DCU / HIP

推荐提示词：

```text
$lightop-kernel-knowledge
请围绕 <算子/模块名> 帮我查 LightOp / DCU / ROCm 的实现证据。
请优先从本地代码和测试出发，再补充 upstream 资料，并给出下一步最值得验证的优化方向。
```

## 安装方式

### 方式一：把单个 skill 安装到 Codex skills 目录

如果你只想用其中几个 skill，最稳妥的方式是把对应目录复制到 Codex 的 skills 根目录：

```bash
mkdir -p ~/.codex/skills

cp -a /path/to/HG-AI-Infra-SKILLS/skills/llm-serving-auto-benchmark ~/.codex/skills/
cp -a /path/to/HG-AI-Infra-SKILLS/skills/llm-torch-profiler-analysis ~/.codex/skills/
cp -a /path/to/HG-AI-Infra-SKILLS/skills/model-architecture-diagram ~/.codex/skills/
```

对知识库型内容，也可以按需一并复制：

```bash
cp -a /path/to/HG-AI-Infra-SKILLS/model-pr-optimization-history ~/.codex/skills/
cp -a /path/to/HG-AI-Infra-SKILLS/model-pr-optimization-hg-history ~/.codex/skills/
```

### 方式二：把整个仓库放到可扫描位置

如果你的 Codex 环境支持递归扫描子目录，可以直接把整个仓库放到 skills 根目录下管理：

```bash
mkdir -p ~/.codex/skills
cp -a /path/to/HG-AI-Infra-SKILLS ~/.codex/skills/
```

### 方式三：从 git 安装

```bash
git clone <repo-url> HG-AI-Infra-SKILLS
cp -a HG-AI-Infra-SKILLS/skills/<skill-name> ~/.codex/skills/
```

## 使用方式

安装后，在对话里直接用技能名触发：

```text
$llm-serving-auto-benchmark ...
$llm-torch-profiler-analysis ...
$sglang-prod-incident-triage ...
```

一般建议你一次只触发一个主 skill，再让它调用需要的历史知识库或辅助技能。比如：

- 做 benchmark 时，优先用 `llm-serving-auto-benchmark`
- 看 trace 时，优先用 `llm-torch-profiler-analysis`
- 排查线上问题时，优先用 `sglang-prod-incident-triage`
- 做 SGLang 持续优化时，优先用 `sglang-sota-humanize-loop`
- 查历史证据时，优先用 `model-pr-optimization-history` 或 `model-pr-optimization-hg-history`

## 测试与脚本

仓库里还带有回归测试和重建脚本，用来保证 skill 文档、查询逻辑和结果格式稳定：

- `tests/`：基础回归测试
- `tools/rebuild_model_pr_history_from_git.py`：重建社区 PR 历史
- `tools/rebuild_model_pr_hg_history_from_local_git.py`：重建本地提交历史

运行测试：

```bash
cd HG-AI-Infra-SKILLS
python3 -m pytest tests
```

如果默认 `python3` 版本过老，改用系统里的新版本即可：

```bash
/usr/bin/python3.8 -m pytest tests
/usr/bin/python3.10 -m pytest tests
```

## 使用建议

- 做性能优化时，先 benchmark，再 profiler，再查历史证据，最后 patch。
- 处理线上异常时，先采集现场和可复现请求，再决定要不要 profiling。
- 如果目标是 LightOp / DCU / ROCm kernel 优化，先用知识 skill 找证据，再用 profiling skill 量化瓶颈。
- `ask-codex` 和 `ask-gemini` 适合做辅助研究，不适合作为主流程替代品。

