---
name: kb-ingest
description: 把收到的资料（文件、文档内容、skill 草稿）分类入库到正确的知识库：HCU 机制/材料/PR 类资料进 GitLab 的 hcu-knowledge（走 kb.py 管道），可复用的对话指令 skill 进 dcu-infer-pilot 的 skills/ 目录。当用户说「把这份资料入库」「这个文件存到知识库」「收一下这个文档」「新增一个 skill」「把这个 skill 放进去」时使用。触发词：资料入库、存知识库、收录、入库、新增 skill、skill 入库。
---

# 资料入库（hcu-knowledge + dcu-infer-pilot）

把一份资料放进正确的库。核心是先分类、再走各库的正规管道，**绝不手写各库的受保护内容**。

## 判定树（收到任何东西先走这棵树）

```
收到的资料
├─ 是 skill / 工具说明书 / 流程手册？ → dcu-infer-pilot skills/（见②）
├─ 是上游 PR/MR 记录（gh-sglang 的新 PR）？ → 不直接收，转 kb-update skill 走管道
├─ 是原始材料（PDF/PPT/分享文档/手册）？ → hcu-knowledge materials/（管道收录，见①B）
└─ 是解释性内容（机制分析/优化案例/排障经验）？ → hcu-knowledge local/ 人工页（见①C）
```

## ① hcu-knowledge（GitLab `yangyn1/hcu-knowledge`，节点 26 容器内操作）

### ①A PR/MR 记录
- 唯一入口：`python3 -X utf8 kb.py update changes --source gh-sglang`（分批 + `--resume`）
- 禁止手写 `local/changes/gh-sglang-*.md`；INDEX/catalog/evidence 都由管道维护
- 完整流程见 `kb-update` skill

### ①B 原始材料
- 入口：`kb.py update local`（本地材料）或 `update feishu`（飞书文档），由管道解析、哈希、存 `evidence/objects/`
- ≥1MiB 自动走 Git LFS；主动排除：年度汇报/年终总结/周报、视频、容错性能
- 材料允许 tag 多个 project，不强制主归属；`topics` 字段登记相关专题

### ①C 解释性内容（人工页，有格式关）
| 落点 | 放什么 |
|---|---|
| `local/overview/engineering-guide.md` | 每项目唯一主工程报告（9 章固定结构） |
| `local/topics/` | 机制专题（问题/调用链/限制反例/证据/观察集） |
| `local/cases/` | 优化案例（按 optimization-case-format.md；没实测标 `hardware-not-run`） |
| `local/guides/` | 场景指南、维护线说明 |

- front matter 必须 `status: synthesized`，sources 带 id+sha256+revision
- 小修改优先修订已有页，不新凑页面；页面间用稳定 ID + 链接互引，不复制正文
- 入库前跑 `python -X utf8 tools/check_project_guides.py`

### ① 红线
- 绝不手改：`upstream/`、`knowledge/catalog/*.json`、`derived/ indexes/ staging/`
- 全程 `python3 -X utf8`；本机没有 kb.py 可用副本，一律 ssh 到节点 26 容器执行

## ② skill 进 dcu-infer-pilot（`skills/<名>/`）

- 目录 `skills/<skill名>/`，kebab-case，**与 front matter `name` 一致**
- front matter：`name` + `description`（前几句说清干什么，末尾列触发词）+ 可选 `metadata.requires.bins`
- 正文形制：标题 → 适用场景 → `## Workflow` 编号步骤 → `## 推荐提示词` → 运行上下文
- 可选子目录 `reference/`（范文）、`scripts/`（辅助脚本）
- **入库后必须两件配套**（漏了等于没入库）：
  1. `install_all_skills.sh` 的 `REGULAR_SKILLS` 加一行 `"<名>|${REPO_ROOT}/skills/<名>"`，名字同步进 usage() 清单
  2. `README.md` 的 Skills 总览加一节
- 知识库型内容（PR 历史/提交历史）不进 skills/，走 `model-pr-optimization-*/` 根目录（kb-update 流程）

## ③ 推送刹车（硬规则）

1. 入库完成后先给用户**变更清单**（改了哪些文件、各自进哪个库）
2. 用户确认后才 `git commit` + push feature 分支 + 建 MR
3. **绝不自动合并 MR**；双仓发布（hcu-knowledge 用 `tools/push_remotes.py`）同样需用户确认
4. skill 若要让飞书 bot 立即可用，确认后同步一份到 `C:\Users\yuchenyang\.dsh\skills\<名>\SKILL.md`（桌面端与飞书端共享此目录，watcher 热加载）

## Workflow

1. 判定资料类型（判定树），拿不准就问用户一句，不猜
2. 按对应分支准备入库物（材料走管道；人工页先过格式关；skill 按②的形制写好）
3. 环境自检：hcu-knowledge 需隧道 `ssh -p 10026` 通 + 容器 `sglang_yuchenyang_1020` 在跑
4. 执行入库（容器内 kb.py / 本地 skills/ 目录）
5. 出变更清单 → 等用户确认 → commit/push/MR
6. 报告 MR 链接，等用户合并；需要时同步 `~\.dsh\skills\`

## 推荐提示词

```text
$kb-ingest
这份文件请入库：<路径或说明>
```

```text
$kb-ingest
新建一个 skill：<名称>，用途：<一句话>，触发词：<几个>
```
