---
name: kb-search
description: 在三个知识库里检索用户要的资料并给出可打开的出处链接：本地 fork 提交历史/上游 PR 历史（dcu-infer-pilot 的 model-pr-optimization-*，本机 query.py 直查）、HCU 大领域知识库（GitLab hcu-knowledge，节点容器 kb.py 语义检索）、以及 dcu-infer-pilot 自带的 skill 清单。当用户说「找资料」「查一下知识库」「有没有关于 X 的文档」「X 的优化历史」「有什么现成 skill」「检索」时使用。触发词：找资料、查知识库、检索、有没有文档、优化历史、PR 历史、skill 列表。
---

# 知识检索（hg-history / pr-history / hcu-knowledge / skills 路由）

用户要什么资料 → 判断意图 → 走对应检索链路 → 给结论 + 可打开的出处链接。三路全部复用现有工具，不造轮子。

## 第 0 节：链路自检（先检后查，断了给重起命令）

### 链路 A：本机 query.py（hg-history + pr-history）
- 位置：`C:\Users\yuchenyang\.dsh\bot\workspace\dcu-infer-pilot\model-pr-optimization-hg-history\` 和 `...\model-pr-optimization-history\`
- 自检：两个目录各存在 `scripts/query.py` 即可用，无外部依赖（纯 Python 标准库）

### 链路 B：hcu-knowledge（节点 26 容器 kb.py）
- 自检顺序：
  1. `ssh -p 10026 yuchenyang@127.0.0.1 "hostname"` 通不通
  2. 不通 → 告诉用户重起隧道：`ssh -N -L 10026:10.16.1.26:22 42.228.13.241`（需输一次 OTP），**不要硬跑后续命令**
  3. 通 → `ssh -p 10026 yuchenyang@127.0.0.1 "docker ps --format '{{.Names}}' | grep sglang_yuchenyang_1020"` 确认容器在跑；不在跑给 `docker start sglang_yuchenyang_1020`
- 调用模板（在容器内、仓库根执行）：
  ```bash
  ssh -p 10026 yuchenyang@127.0.0.1 \
    "docker exec -w /public/home/yuchenyang/hcu-knowledge sglang_yuchenyang_1020 \
     python3 -X utf8 kb.py search '<关键词>' --limit 12"
  ```
  （仓库实际路径以节点上克隆位置为准，先 `ls` 确认）
- 常用：`search`、`read <ITEM_ID>`、`original <ITEM_ID>`、`cases --operator X --technique Y`、`prof search --framework X --model Y`、`search-pr`

### 链路 C：dcu-infer-pilot skills/ 清单
- 位置：`C:\Users\yuchenyang\.dsh\bot\workspace\dcu-infer-pilot\skills\`，每个子目录一个 `SKILL.md`
- 检索方式：读各 `SKILL.md` 的 front matter description 做语义匹配；输出名称 + 一句话 + 仓库链接 `https://developer.sourcefind.cn/codes/OpenDAS/dcu-infer-pilot/tree/main/skills/<名>`

## 意图路由表

| 用户意图 | 链路 | 说明 |
|---|---|---|
| 某模型/某机制的**优化历史证据**、本地 fork 改过什么 | A（先 hg-history，必要时 pr-history 对照） | 秒回，关键词匹配 |
| 上游社区对某问题做过什么 PR | A（pr-history）或 B（`search-pr`） | 本地无答案时走 B 联查线上 |
| HCU 机制、DTK/算子库/通信知识、材料原文、Prof/trace 档案 | B | 最全，含硬件映射（北美洲=gfx936、南美洲=gfx938、少伯=gfx946） |
| 有没有现成 skill、工具怎么用 | C | 给 skill 链接 |
| 意图不清 | A+B+C 并行 | 按证据等级合并回答 |

## 查询要点

- **A 链路**：`python3 scripts/query.py --framework sglang --model <slug> "<关键词>" --limit 5`；不知道 slug 先 `query.py "<模型名>"` 推断；只要路径加 `--paths-only`
- **B 链路**：复杂问题拆实体与机制子问题分别查；查整仓先读 `local/overview/engineering-guide.md` 再沿专题/案例深入；性能数据必须连同硬件/版本/口径说明，历史提升百分比不当作当前预期收益
- 模型族 slug 表见 `model-pr-optimization-hg-history/SKILL.md`（deepseek-v4、kimi、qwen3-core 等 29 个）

## 回答格式

1. 结论 + 适用条件（一两句）
2. 出处：文档路径或链接（A/C 给仓库相对路径 + SourceFind/GitLab 链接；B 给 `read <ITEM_ID>` 可追的 ID）
3. 证据等级与缺口：区分源码事实/来源报告/未验证，未测的明确标出
4. 多个来源冲突时说明分歧，不选边

只读查询，不改任何库；查到该入库的新资料转 `kb-ingest`，该更新来源的转 `kb-update`。

## Workflow

1. 提取用户问题里的实体（模型/框架/机制/硬件）与意图
2. 第 0 节自检对应链路（B 链路先检隧道和容器）
3. 按路由表执行检索（意图不清就三路并行）
4. 读取命中正文核实（A 读文档段；B 用 `read`/`original`；不凭摘要下结论）
5. 按回答格式合并输出，附出处链接

## 推荐提示词

```text
$kb-search
找一下 <模型/机制> 的优化历史证据
```

```text
$kb-search
知识库里有没有关于 <主题> 的资料？给我链接
```
