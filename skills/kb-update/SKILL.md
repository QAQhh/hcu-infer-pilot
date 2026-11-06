---
name: kb-update
description: 更新三个知识库——dcu-infer-pilot 的 model-pr-optimization-hg-history（海光 fork 本地提交历史）、model-pr-optimization-history（上游社区 PR 历史），以及 GitLab 上的 hcu-knowledge（sglang PR 同步）。触发词：更新知识库、更新 pr-history、更新 hg-history、同步 sglang PR。
---

# 更新知识库（dcu-infer-pilot + hcu-knowledge）

一次把三个知识库更新到当前上游。全部在节点 26 的容器里跑，产出提交后走 feature 分支 + MR，**等用户点合并，绝不自动合**。

三个库的分工与边界（铁律）：
- `model-pr-optimization-hg-history`：海光 fork 的**本地提交**历史，SGLang 侧必须 local-only（官方提交一律过滤，fail-closed）
- `model-pr-optimization-history`：上游官方仓库的**社区 PR** 历史，必须 upstream-only（不能用 fork，否则 fork PR 号混入）
- `hcu-knowledge`：**只做 sglang PR 同步**；与上面两个库独立、互不干涉，不建 history 目录

执行纪律：凡涉及 push / 建 MR / 合并 / 发布，一律「先出变更清单 → 等用户确认」，这是硬刹车，不允许自主发布。

---

## 0. 环境前置（先自检，不过不跑）

### 拓扑
```
[本机 Windows]
  │  ssh -N -L 10026:10.16.1.26:22 42.228.13.241   ← 用户手动开，输一次 OTP
  ▼
[跳板机 42.228.13.241:65024]  仅 password/OTP，禁 publickey
  ▼
[研发机 10.16.1.26 = nmz26]  Rocky Linux 8.6，容器 sglang_yuchenyang_1020 挂载 /public/home/yuchenyang
```
- bot 统一入口：`ssh -p 10026 yuchenyang@127.0.0.1 "<cmd>"`；22 节点已不可用，以 26 为跳板
- Windows OpenSSH 9.5 的 ControlMaster 不可用（`getsockname failed: Not a socket`），不要配它
- 长任务用 `setsid nohup ... < /dev/null &`，ssh 会话不返回属正常，用一次性 `ps`/`tail` 复查

### 容器与 Python（硬约束）
| 位置 | Python | |
|---|---|---|
| 宿主机 26 | 3.6.8 | 跑不了（脚本用 ≥3.7 语法） |
| 容器 sglang_yuchenyang_1020 | 3.10.12 | **所有 KB 脚本在这里跑** |

- 统一调用：`docker exec -w <repo> sglang_yuchenyang_1020 python3 -X utf8 kb.py ...`，`-X utf8` 不可省
- git-lfs 必须**容器内**装（3.0.2），宿主机装无效；容器因宿主机重启会 `Exited (137)`，先 `docker start`
- 容器内跑 git 要注入 `-e GIT_CONFIG_COUNT=1 -e GIT_CONFIG_KEY_0=safe.directory -e GIT_CONFIG_VALUE_0='*'`（否则 dubious ownership）

### 出网：本机出不去，走节点 26 中继
- 本机 hosts 把 github 域名指向 127.0.0.1（Watt Toolkit MITM，非常驻），npmjs/nodejs.org 不在其加速列表
- 节点 26 起 HTTP CONNECT 代理 `python3 proxy.py 18080`，本机 `ssh -N -L 18080:127.0.0.1:18080 -p 10026`，设 `HTTP_PROXY/HTTPS_PROXY=http://127.0.0.1:18080`
- **必须 HTTP CONNECT**：pnpm/npm 不认 socks（`fetch failed`）

### 本机 git 两个开关
```bash
git -c http.sslBackend=openssl <cmd>      # 不加走 schannel 报 SEC_E_NO_CREDENTIALS
$env:GIT_TERMINAL_PROMPT="0"              # 否则凭据缺失挂住等输入
```

### 凭据（只通过 $DSH_SECRET_<NAME> 读，不打印值）
| Secret | 用途 | 权限边界 |
|---|---|---|
| GITHUB_TOKEN | 读 sglang-das/vllm 上游 PR | 只读，5000 次/小时 |
| HCU_KNOWLEDGE_GITLAB_PAT | GitLab 42.228.13.241:10068 API | `glpat-`，read_api，**不能建 MR** |
| HCU_KNOWLEDGE_GITLAB_TOKEN | 同实例 git 读写 | write_repository，推不了受保护 main |
| SOURCEFIND_WRITE_TOKEN | 光源 dcu-infer-pilot 写 | 能推分支 + 读 MR API |

- 两个 GitLab 的 main 都是受保护分支 → 一律 feature 分支 + MR
- 光源 API 前缀是 `/codes/api/v4`（不是 `/api/v4`），用错 404

### 仓库位置（都在 26，容器内同路径）
| 仓库 | 路径 | 备注 |
|---|---|---|
| hcu-knowledge 工作克隆 | `~/hcu-knowledge-sync` | state/LFS/derived 不进 git，**绝不能删** |
| vllm 上游 | `~/pr-history-run/vllm-upstream` | blob:none 克隆后要 `read-tree HEAD` |
| sglang 上游 | `~/workspace/agent_pr_m3.1/repos/sglang-official` | 每次先 fetch 当天 main |
| pr-history 产物 | `~/pr-history-run/kb/` | 只拉回文档，不搬大文件 |

---

## 1. 更新 model-pr-optimization-hg-history（本地 fork 提交）

**准备**：`sglang-das` 已 fetch 官方 refs `refs/remotes/github-official/*` + `refs/remotes/origin/*`；官方 refs 缺失必须报错停住（fail-closed）。`--no-checkout` 克隆先 `git read-tree HEAD` 补索引。

```bash
SGLANG_HG_HISTORY_ROOT=<sglang-das> \
MODEL_PR_HG_HISTORY_ROOT=<kb> \
MODEL_PR_HG_HISTORY_LIMIT=200000 \
MODEL_PR_HG_HISTORY_MAX_DOC_COMMITS=1000 \
python3 -X utf8 tools/rebuild_model_pr_hg_history_from_local_git.py --framework sglang --dry-run
```
- `--framework` 只重建指定框架；全量段用 `append_hg_history_branch_segments.py --segment "hg-full-base..main"`（`hg-full-base` = 与官方 main 的 merge-base）
- `LIMIT` 默认 3000 会截断，全量要调大；`MAX_DOC_COMMITS` ≥ 最大桶

**验收**：本地独有提交数 == 文档覆盖数；抽查无 upstream 混入；无官方 refs 时脚本报错（fail-closed 自测）。

## 2. 更新 model-pr-optimization-history（上游社区 PR）

**准备**：纯上游工作树 `SGLANG_PR_HISTORY_ROOT`=sgl-project/sglang、`VLLM_PR_HISTORY_ROOT`=vllm-project/vllm（不能用 fork）。轻量克隆 `--filter=blob:none --no-checkout --single-branch --branch main` + `read-tree HEAD`。

**必须上节点容器跑**（本机经代理截断，140 文件的 PR 要 409 秒）。

GitHub token 在**容器内 `git credential fill` 自取**，绝不要从外部 shell 管道传（会被替换成占位符，废掉整批缓存）。

```bash
SGLANG_PR_HISTORY_ROOT=<upstream sglang> \
VLLM_PR_HISTORY_ROOT=<upstream vllm> \
MODEL_PR_HISTORY_ROOT=<kb> \
MODEL_PR_HISTORY_CACHE=<cache.json> \
MODEL_PR_HISTORY_MAX_DOC_PRS=200 \
python3 -X utf8 tools/rebuild_model_pr_history_from_git.py --framework sglang --dry-run
```
- `--all-refs` 读所有分支；`--no-renames` 已内置；`MAX_DOC_PRS` 每文档上限（按 merged_at 倒序留 200，超出注明截断）

**配额管理**：每 PR 2 次调用、5000/小时，全量约 6200 次必跨 2 个窗口。失败条目命中即返回不重试 → 补跑前**只删失败条目**（`fetch_error`），别整体删缓存。循环到 `fetch_error`=0（404=PR 已删，可接受）。`shared` 桶候选 PR 号是从旧文档反推的、可能上万 → 候选集和渲染都要截断。

**验收**：0 处 `unavailable PR`；每桶条目 == min(候选,200)，shared 带截断说明；单文档 <1MB；无本机路径（用仓库标识）。

## 3. 更新 hcu-knowledge（sglang PR 同步）

**铁律**：只能动 `local/changes/`（新增 gh-sglang-N.md）+ 重写 `local/changes/INDEX.md` + README 计数行；管道自动维护 `catalog/*.json`、`evidence/objects/`。绝不能手改 `local/{cases,topics,guides,overview}`（人工页）、`knowledge/catalog/*.json`、`upstream/`、`derived/ indexes/ staging/`。PAT 用 `glpat-` 那枚。

**步骤**（容器内，按序）：
```bash
git pull && git lfs pull                                  # fresh clone 必做
python3 -X utf8 kb.py restore-derived                     # 期望 restored 数千条
PYTHONUNBUFFERED=1 python3 -X utf8 kb.py update changes --source gh-sglang
# partial 退出正常（每批约 100）；续跑：
PYTHONUNBUFFERED=1 python3 -X utf8 kb.py update changes --source gh-sglang --resume <run-id>
# 项目复核闸门：9 个人工页 receipt（脚本 workspace\make_receipt.py）
python3 -X utf8 make_receipt.py            # dry-run
python3 -X utf8 make_receipt.py --record   # 确认输出 OK 才写 ledger
# finalize（闸门：exclusions→classification→impact→project-review→navigation→validation→publication）
python3 -X utf8 kb.py finalize --run --review-note "<日期+范围>" --allow-pending-review
```

**验收**：changes/ 无 unavailable PR、编号连续；INDEX 行数 = 记录数+2；README 计数已更新；git status 只含预期文件。

## 4. 发布与提交（三库通用）

- 一律 **feature 分支 + MR**，不直推 main（Developer 推不了受保护 main）
- push 用写权限 token 内联 URL；origin 里嵌的只读占位符不能用
- 分支命名：`feat/pr-history-sglang`、`feat/pr-history-vllm`、`sglang-pr-sync-YYYYMMDD`
- **先给用户变更清单 + MR 链接，等用户点合并**，不自动合

---

## 5. 坑速查表（本轮全部踩过）

| 现象 | 真因 | 处置 |
|---|---|---|
| `getsockname failed: Not a socket` | Windows ControlMaster 不可用 | 用一条 `-L` 隧道 |
| `Derivative snapshot corrupted` / `knowledge.py:45` None 下标 | 干净克隆没 `git lfs pull`，大对象是指针 | 容器内 git-lfs → `git lfs pull` → `restore-derived` |
| `Publication blocked: review pending` | project-review receipt 未记录 | 9 页 receipt（每页 ≥1 个 catalog 证据 id）→ `--record` |
| `Finalize requires --review-note` | 发布闸门要求复核说明 | 带 `--review-note` |
| `Writer lock exists: .../run-*.lock` | ssh 断连留下的 stale lock | 确认无进程后删锁，`docker exec -d` 单次跑 |
| 宿主机 python 语法错 | host 是 3.6.8 | 进容器跑 |
| `403 insufficient_scope`（建 MR） | PAT 只有 read_api | 人工建 MR 或换带 api 的 PAT |
| `pre-receive hook declined`（推 main） | 受保护分支 | 推 feature 分支 + MR |
| 光源 API 404 | 前缀错 | 用 `/codes/api/v4` |
| pnpm `fetch failed` | 走 socks | 用 HTTP CONNECT 代理 |
| git `SEC_E_NO_CREDENTIALS` | schannel | `-c http.sslBackend=openssl` |
| `KeyError: 'shared'` | MODEL_ORDER 含 shared 但过滤器无此键 | 模型循环跳过 shared |
| 单文档 34MB / 配额掏空 | shared 桶无上限、候选集不截断 | 渲染 + 候选集都截断 |
| 容器内 git 报 dubious ownership | root 身份 | 注入 safe.directory='*' |
