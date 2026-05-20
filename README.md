# HG-AI-Infra-SKILLS

`HG-AI-Infra-SKILLS` 是一套面向 LLM Serving、性能分析、SGLang 优化和模型优化历史检索的 Codex Skills 工程。它把常用的 AI Infra 工作流拆成可复用的 skill：benchmark、torch profiler trace 分析、模型架构图查询、SGLang 线上故障排查、SGLang SOTA 优化闭环，以及本地/社区优化历史知识库。

本工程适合下面这些场景：

- 对比 SGLang、vLLM、TensorRT-LLM 在同一模型和 workload 下的部署性能。
- 分析 torch profiler trace，拆分 prefill/decode 阶段，定位 kernel、overlap、fusion 和空泡问题。
- 查询模型架构图、模型相关 PR 历史、本地 fork 提交历史。
- 排查 SGLang 线上服务健康、延迟、吞吐、crash、hang、PD/EP/HiCache 问题。
- 围绕一个模型持续优化，直到追平或超过同环境下的。

## 目录结构

```text
HG-AI-Infra-SKILLS/
  README.md
  skills/
    llm-serving-auto-benchmark/
    llm-torch-profiler-analysis/
    model-architecture-diagram/
    model-optimization/
      model-pr-diff-dossier/
    sglang-prod-incident-triage/
    sglang-sota-humanize-loop/
  model-pr-optimization-history/
  model-pr-optimization-hg-history/
  tools/
  tests/
```

## Skills 一览

### `llm-serving-auto-benchmark`

路径：`skills/llm-serving-auto-benchmark/`

功能：跨框架 LLM Serving benchmark。用于在相同模型、相同 workload、相同 GPU 预算和相同 SLA 下比较 SGLang、vLLM、TensorRT-LLM 等框架。

主要能力：

- 根据 cookbook YAML 生成 SGLang/vLLM/TensorRT-LLM 启动候选。
- 校验目标框架 CLI 参数是否存在。
- 汇总 benchmark JSONL，输出 markdown/CSV 对比表。
- 保留失败、跳过、SLA 不通过的候选，便于复盘。

重要文件：

- `SKILL.md`：skill 主说明。
- `configs/cookbook-llm/`：模型 benchmark 配置，例如 `minimax-m2.5.yaml`、`qwen3-235b-a22b.yaml`、`deepseek-v3.2.yaml`。
- `scripts/validate_cookbook_configs.py`：校验 cookbook 配置并渲染候选命令。
- `scripts/compare_benchmark_results.py`：将 benchmark JSONL 转成结果表。
- `references/result-schema.md`：benchmark 结果 JSONL 字段约定。
- `references/framework-reference.md`：框架参数和注意事项。

常用命令：

```bash
cd HG-AI-Infra-SKILLS

python3 skills/llm-serving-auto-benchmark/scripts/validate_cookbook_configs.py \
  skills/llm-serving-auto-benchmark/configs/cookbook-llm

python3 skills/llm-serving-auto-benchmark/scripts/compare_benchmark_results.py \
  --input /path/to/results.jsonl \
  --output /path/to/summary.md
```

### `llm-torch-profiler-analysis`

路径：`skills/llm-torch-profiler-analysis/`

功能：统一分析 LLM Serving 的 torch profiler trace。支持 SGLang、vLLM、TensorRT-LLM。

主要能力：

- 分析已有 `trace.json` 或 `trace.json.gz`。
- 对 live server 进行 profiler capture。
- 区分 prefill 和 decode 阶段。
- 输出 kernel table、overlap-opportunity table、fuse-pattern table。
- 输出 bubble-gap 分析，包括 `Global idle bubble` 和 `Per-stream gap`。
- 分析前会参考本地提交历史和社区 PR 历史，寻找可借鉴优化思路。

重要文件：

- `SKILL.md`：英文主说明。
- `skill_ch.md`：中文说明。
- `scripts/analyze_llm_torch_profile.py`：统一 trace 分析入口。
- `scripts/analyze_sglang_torch_profile.py`：兼容旧 SGLang 分析入口。
- `scripts/render_triage_markdown_bundle.py`：将多份分析结果汇总成一个 markdown。
- `scripts/probe_llm_server.py`：探测 OpenAI-compatible 服务。
- `scripts/run_sglang_torch_profile_host.sh`、`run_vllm_torch_profile_host.sh`、`run_trtllm_pytorch_profile_host.sh`：host 侧 profile 示例脚本。
- `references/fuse-overlap-catalog.md`、`overlap-catalog.md`、`heuristics.md`：融合、重叠、启发式分析知识。

常用命令：

```bash
cd HG-AI-Infra-SKILLS

python3 skills/llm-torch-profiler-analysis/scripts/analyze_llm_torch_profile.py \
  --input /path/to/traces

python3 skills/llm-torch-profiler-analysis/scripts/render_triage_markdown_bundle.py \
  --analysis-root /path/to/analysis_root \
  --output /path/to/bundle.md
```

如果宿主机默认 `python3` 过老，可使用系统已有的 Python 3.8/3.10：

```bash
/usr/bin/python3.8 skills/llm-torch-profiler-analysis/scripts/analyze_llm_torch_profile.py \
  --input /path/to/traces
```

### `model-architecture-diagram`

路径：`skills/model-architecture-diagram/`

功能：查询公开原始模型架构图。支持 LLM、VLM、MoE、diffusion、OCR 等模型族。

主要能力：

- 根据模型名查询已索引的公开原始架构图。
- 返回原始图片 Markdown 和来源。
- 不复制远端图片，只保留公开原始 URL。

重要文件：

- `SKILL.md`：skill 主说明。
- `scripts/model_architecture_diagram.py`：模型架构图查询脚本。
- `references/diagram-index.json`：架构图索引。
- `references/source-notes.md`：来源说明。

常用命令：

```bash
cd HG-AI-Infra-SKILLS

python3 skills/model-architecture-diagram/scripts/model_architecture_diagram.py "minimax-m2.5"
python3 skills/model-architecture-diagram/scripts/model_architecture_diagram.py "GLM-5" --format json
python3 skills/model-architecture-diagram/scripts/model_architecture_diagram.py --list-known
```

### `model-pr-diff-dossier`

路径：`skills/model-optimization/model-pr-diff-dossier/`

功能：创建或审查模型 PR 优化历史文档时使用的质量门禁 skill。

主要能力：

- 要求每个 PR 卡片必须基于真实 diff，而不是标题级总结。
- 记录 PR 动机、实现要点、关键代码摘录、已读文件、验证风险。
- 用于维护 `model-pr-optimization-history` 的文档质量。

重要文件：

- `SKILL.md`：逐 PR diff 审计要求。
- `references/card-schema.md`：PR 卡片格式约定，如果存在则优先参考。

### `sglang-prod-incident-triage`

路径：`skills/sglang-prod-incident-triage/`

功能：SGLang 线上故障排查。核心原则是 replay-first：先保存现场和可复现请求，再进入 profiler、trace、coredump 或分布式 debug。

适用问题：

- `/health` 或 `/health_generate` 异常。
- 延迟、吞吐、TTFT、TPOT 回退。
- queue 堆积。
- 请求 timeout、hang。
- CUDA crash 或 crash dump。
- PD、EP、HiCache、分布式 stall。
- 部署后输出错误。

重要文件：

- `SKILL.md`：故障排查主流程。
- `scripts/incident_artifact_tool.py`：采集和汇总服务现场 bundle。
- `scripts/replay_trusted_request_dump.py`：重放可信 request dump。
- `references/decision-tree.md`：问题分类决策树。
- `references/endpoints-and-signals.md`：SGLang endpoint 和监控信号说明。
- `references/replay-trace-profile.md`：replay、trace、profile 流程。
- `references/case-studies.md`：案例。

常用命令：

```bash
cd HG-AI-Infra-SKILLS

python3 skills/sglang-prod-incident-triage/scripts/incident_artifact_tool.py collect-bundle \
  --base-url http://127.0.0.1:30000 \
  --outdir /tmp/incident_bundle

python3 skills/sglang-prod-incident-triage/scripts/incident_artifact_tool.py summarize-bundle \
  /tmp/incident_bundle
```

### `sglang-sota-humanize-loop`

路径：`skills/sglang-sota-humanize-loop/`

功能：围绕一个模型执行 SGLang SOTA 性能优化闭环。该 skill 是顶层编排流程，会串联 benchmark、profiler、history 查询和代码 patch。

流程概览：

1. 使用 `llm-serving-auto-benchmark` 做公平跨框架 benchmark。
2. 找出 SGLang 与 vLLM/TensorRT-LLM 的差距。
3. 使用 `llm-torch-profiler-analysis` 分析 SGLang 和领先框架。
4. 查询 `model-pr-optimization-history` 和 `model-pr-optimization-hg-history`。
5. 生成 root-cause、patch 计划和 Humanize RLCR 迭代。
6. 反复 benchmark/profile/patch，直到达到停止条件。

重要文件：

- `SKILL.md`：完整 SOTA loop 说明。
- `references/refined-plan-template.md`：Humanize plan 模板。

## 两个模型优化知识库

### `model-pr-optimization-history`

路径：`model-pr-optimization-history/`

功能：开源社区 GitHub PR 历史知识库。用于查询 SGLang/vLLM 社区在各模型上的历史优化、fast path、fusion、overlap、MoE、attention、cache、sampler、loader 等改动。

目录结构：

```text
model-pr-optimization-history/
  SKILL.md
  README.md
  scripts/query.py
  sglang/<model>/README.zh.md
  sglang/<model>/README.en.md
  vllm/<model>/README.zh.md
  vllm/<model>/README.en.md
```

常用命令：

```bash
cd HG-AI-Infra-SKILLS/model-pr-optimization-history

python3 scripts/query.py --list
python3 scripts/query.py --framework sglang --model minimax --lang zh minimax moe
python3 scripts/query.py --framework vllm "qwen3 fused qk norm" --limit 5
```

### `model-pr-optimization-hg-history`

路径：`model-pr-optimization-hg-history/`

功能：本地 `sglang` 和 `vllm` 工作树提交历史知识库。它记录本地 fork 中模型相关和框架级优化提交，和开源社区 PR 历史互补。

目录结构：

```text
model-pr-optimization-hg-history/
  SKILL.md
  README.md
  scripts/query.py
  sglang/<model>/README.zh.md
  sglang/<model>/README.en.md
  sglang/shared/README.zh.md
  vllm/<model>/README.zh.md
  vllm/<model>/README.en.md
  vllm/shared/README.zh.md
```

常用命令：

```bash
cd HG-AI-Infra-SKILLS/model-pr-optimization-hg-history

python3 scripts/query.py --list
python3 scripts/query.py --framework sglang --model minimax --lang zh minimax moe
python3 scripts/query.py --framework sglang --model shared --lang zh hicache
python3 scripts/query.py --framework vllm --model minimax --lang zh rms quant
```

## `tools/`

`tools/` 放知识库生成脚本。

- `rebuild_model_pr_history_from_git.py`：从框架 git trace 和 GitHub PR API 重建开源社区 PR history。需要能访问 GitHub API，通常还需要 `gh` CLI。
- `rebuild_model_pr_hg_history_from_local_git.py`：从本地 `sglang` / `vllm` 工作树的 `git log --name-only` 重建本地提交 history，不依赖 GitHub API。

常用命令：

```bash
cd HG-AI-Infra-SKILLS

python3 tools/rebuild_model_pr_hg_history_from_local_git.py --dry-run
python3 tools/rebuild_model_pr_hg_history_from_local_git.py

MODEL_PR_HG_HISTORY_LIMIT=5000 \
SGLANG_HG_HISTORY_ROOT=/path/to/sglang \
VLLM_HG_HISTORY_ROOT=/path/to/vllm \
python3 tools/rebuild_model_pr_hg_history_from_local_git.py
```

重建社区 PR history 示例：

```bash
cd HG-AI-Infra-SKILLS

SGLANG_PR_HISTORY_ROOT=/path/to/sglang \
VLLM_PR_HISTORY_ROOT=/path/to/vllm \
MODEL_PR_HISTORY_ROOT=$PWD/model-pr-optimization-history \
python3 tools/rebuild_model_pr_history_from_git.py --dry-run
```

## `tests/`

`tests/` 放基础回归测试，覆盖 benchmark 配置、profiler 分析脚本、模型架构图查询、SOTA 文档约束和 PR dossier 质量。

测试文件：

- `test_compare_benchmark_results.py`
- `test_llm_serving_cookbook_configs.py`
- `test_llm_serving_docs.py`
- `test_llm_torch_profiler_analysis.py`
- `test_model_architecture_diagram.py`
- `test_model_pr_dossier_quality.py`
- `test_sglang_sota_humanize_loop_docs.py`

运行测试：

```bash
cd HG-AI-Infra-SKILLS
python3 -m pytest tests
```

如果默认 `python3` 版本过老，请换成系统已有的新版本：

```bash
/usr/bin/python3.8 -m pytest tests
/usr/bin/python3.10 -m pytest tests
```

## 安装

### 方式一：作为 Codex skills 目录直接使用

如果你的 Codex 环境支持从指定目录加载 skills，可以直接把本仓库放到 Codex 可扫描的 skills 根目录下。例如：

```bash
mkdir -p ~/.codex/skills
cp -a /path/to/HG-AI-Infra-SKILLS ~/.codex/skills/
```

然后在对话中引用对应 skill，例如：

```text
$llm-torch-profiler-analysis 分析 /path/to/traces
$model-architecture-diagram 查询 minimax-m2.5 架构图
```

### 方式二：只安装 `skills/` 下的单个 skill

如果只想安装某个 skill，可以复制单个目录：

```bash
mkdir -p ~/.codex/skills

cp -a HG-AI-Infra-SKILLS/skills/llm-torch-profiler-analysis \
  ~/.codex/skills/

cp -a HG-AI-Infra-SKILLS/skills/llm-serving-auto-benchmark \
  ~/.codex/skills/
```

注意：`llm-torch-profiler-analysis` 会联动查询两个 history 知识库。如果需要完整能力，建议同时保留：

```text
model-pr-optimization-history/
model-pr-optimization-hg-history/
```

### 方式三：从 git 仓库安装

在线环境中可以 clone 后复制：

```bash
git clone <repo-url> HG-AI-Infra-SKILLS
mkdir -p ~/.codex/skills
cp -a HG-AI-Infra-SKILLS ~/.codex/skills/
```

如果使用内部 Git 服务：

```bash
git clone ssh://<your-git-server>/<group>/HG-AI-Infra-SKILLS.git
```

## 离线安装

离线安装推荐使用 tar 包或 zip 包。在线机器先打包：

```bash
cd /path/to
tar --exclude='__pycache__' -czf HG-AI-Infra-SKILLS.tar.gz HG-AI-Infra-SKILLS
```

把 `HG-AI-Infra-SKILLS.tar.gz` 拷贝到离线机器后解压：

```bash
mkdir -p ~/.codex/skills
tar -xzf HG-AI-Infra-SKILLS.tar.gz -C ~/.codex/skills
```

如果只离线分发工程而不接入 Codex，也可以解压到任意工作目录：

```bash
tar -xzf HG-AI-Infra-SKILLS.tar.gz -C /public/home/yangyn1/work_space/2026/minmax/skills
```

离线环境注意事项：

- `model-architecture-diagram` 默认返回远端原始图片 URL；离线环境无法直接显示远端图片，但仍可查询到 URL 和来源。
- `model-pr-optimization-history` 是已生成的社区 PR 文档，可离线查询；重建它通常需要 GitHub API 和 `gh` CLI。
- `model-pr-optimization-hg-history` 是已生成的本地提交文档，可离线查询；如果离线机器也有本地 `sglang` / `vllm` git 工作树，可以重新生成。
- profiler、benchmark、incident triage 相关脚本不自动安装 SGLang/vLLM/TensorRT-LLM，需要目标环境已有对应框架和依赖。

## Python 版本

部分脚本使用：

```python
from __future__ import annotations
```

如果默认 `python3` 太老，会出现类似错误：

```text
SyntaxError: future feature annotations is not defined
```

请使用 Python 3.8 或更高版本：

```bash
/usr/bin/python3.8 <script.py>
/usr/bin/python3.10 <script.py>
```

## 使用建议

### 进行一次模型性能优化

推荐顺序：

1. 用 `llm-serving-auto-benchmark` 做跨框架 benchmark。
2. 用 `llm-torch-profiler-analysis` 分析慢场景 trace。
3. 查询 `model-pr-optimization-history` 的社区 PR 先例。
4. 查询 `model-pr-optimization-hg-history` 的本地提交先例。
5. 如果目标是持续优化 SGLang，进入 `sglang-sota-humanize-loop`。

### 处理线上服务异常

推荐顺序：

1. 用 `sglang-prod-incident-triage` 采集 bundle。
2. 保存 request dump 或 crash dump。
3. 在干净环境 replay。
4. 只有在问题已经缩小到计算路径时，再进入 `llm-torch-profiler-analysis`。

### 查询模型资料

```bash
python3 skills/model-architecture-diagram/scripts/model_architecture_diagram.py "minimax-m2.5"

cd model-pr-optimization-hg-history
python3 scripts/query.py --framework sglang --model minimax --lang zh
```
