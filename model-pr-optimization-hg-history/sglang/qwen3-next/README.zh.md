# sglang Qwen3 Next 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| - | 无本地独有提交 |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 0
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| - | - | - | no local-only commit found | - |

## 逐 Commit 审计卡

### 本地提交检索结论

- 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；当前基线历史中没有保留的本地独有提交。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## v0.5.8_dev 到 v0.5.12_dev 本地独有提交补充

### 覆盖说明

- 来源索引: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- 来源工作树: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交。
- 本章节提交数: 1
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-03-13 | `446841129` | `v0.5.8_dev..v0.5.9_dev` | 调度/缓存/PD | 支持qwen3-next在fa3后端时打开radix cache | `python/sglang/srt/server_args.py` |

### 逐 Commit 审计卡

#### Commit `446841129` - 支持qwen3-next在fa3后端时打开radix cache

- 完整 hash: `4468411292399a06690dbbc2dc39d5b61a0ce2c5`
- 时间/作者: 2026-03-13 / niuhb
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 调度/缓存/PD
- 主要文件: `python/sglang/srt/server_args.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/server_args.py`
- 验证与风险: 涉及调度、缓存、PD 或 MTP 路径；需要验证 prefill/decode 时序、首 token 正确性、并发与长上下文稳定性。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
