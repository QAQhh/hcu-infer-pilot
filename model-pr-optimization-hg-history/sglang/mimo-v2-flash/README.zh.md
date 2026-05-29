# sglang MiMo V2 Flash 本地提交优化历史

## 模型实现文件覆盖

| 文件 | 本地提交 |
| --- | --- |
| `python/sglang/srt/models/mimo_v2_flash.py` | `1924c63d6` |

## 本地提交覆盖总览

- 来源工作树: `/public/home/yangyn1/work_space/2026/minmax/skills/sglang`
- 生成日期: 2026-05-20
- 文档提交数: 3
- 自动归类说明: 直接命中模型文件或模型名的提交进入模型桶；无法安全锚定到单一模型家族的运行时、后端、调度、缓存、CI、测试提交进入 framework `shared/` 桶。
- 追溯命令: `git log --name-only`
- 过滤说明: 已剔除可从 `sgl-project/sglang` GitHub refs 到达的官方提交；本文件仅保留本地 fork 独有提交。

## 时间线

| 日期 | Commit | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-05-14 | `1924c63d6` | 性能/后端优化 | [BUG FIX] fix pp parallel bug for mimo model | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py` |
| 2026-04-14 | `47165f0fc` | 性能/后端优化 | [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash) | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` |
| 2026-04-03 | `30f4f1133` | 性能/后端优化 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` |

## 逐 Commit 审计卡

### Commit `1924c63d6` - [BUG FIX] fix pp parallel bug for mimo model

- 完整 hash: `1924c63d64f72fbbb4623956150b176dcdcde29c`
- 时间/作者: 2026-05-14 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/models/mimo_v2_flash.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/models/mimo_v2_flash.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `47165f0fc` - [FEAT] add triton attention support for mtp draft extend (MiMo-V2-Flash)

- 完整 hash: `47165f0fcf27c6d38edd4d230d750311f98ba387`
- 时间/作者: 2026-04-14 / ShiQiang Dai
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-model: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/managers/scheduler.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

### Commit `30f4f1133` - support mimo-v2-flash-int4 with triton attn

- 完整 hash: `30f4f1133f9a4d57d8cd3b971230048e0cf15b04`
- 时间/作者: 2026-04-03 / shiqiang
- 自动分类: 性能/后端优化
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- 实现线索: 该提交来自本地框架工作树 `git log --name-only`；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- 验证与风险: 涉及性能或后端路径；复用该思路前需要结合 trace 验证 prefill/decode 热点、端到端吞吐和正确性 smoke。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_START -->
## v0.5.8_dev 到 v0.5.12_dev 本地独有提交补充

### 覆盖说明

- 来源索引: `LOCAL_ONLY_COMMITS_v0.5.8_dev_to_v0.5.12_dev_by_branch.md`
- 来源工作树: `/public/home/yangyn1/work_space/2026/sglang/sglang`
- 口径: 仅记录不可从 `sgl-project/sglang` GitHub refs 到达的本地 fork 独有提交。
- 本章节提交数: 2
- 归类说明: 命中具体模型名、模型文件或已有模型族语义的提交进入对应模型桶；无法稳定锚定单一模型的运行时、后端、CI、merge/base、PD/缓存、量化通用提交进入 `shared`。

### 时间线

| 日期 | Commit | 分支更新段 | 分类 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- | --- |
| 2026-04-03 | `968d82d7f` | `v0.5.8_dev..v0.5.9_dev` | 模型支持/运行时入口 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` 等 4 个文件 |
| 2026-04-03 | `b4a02fae7` | `v0.5.9_dev..v0.5.10_dev` | 模型支持/运行时入口 | support mimo-v2-flash-int4 with triton attn | `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` 等 4 个文件 |

### 逐 Commit 审计卡

#### Commit `968d82d7f` - support mimo-v2-flash-int4 with triton attn

- 完整 hash: `968d82d7f8205f78236c345136a7cbf363f8fd9d`
- 时间/作者: 2026-04-03 / shiqiang
- 分支更新段: `v0.5.8_dev..v0.5.9_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- 重复/备注: 重复 patch-id: 与 v0.5.9_dev..v0.5.10_dev 的 b4a02fae7 相同
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

#### Commit `b4a02fae7` - support mimo-v2-flash-int4 with triton attn

- 完整 hash: `b4a02fae7e09fe663276907645cb77af61c25198`
- 时间/作者: 2026-04-03 / shiqiang
- 分支更新段: `v0.5.9_dev..v0.5.10_dev`
- 自动分类: 模型支持/运行时入口
- 主要文件: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `python/sglang/srt/layers/quantization/gptq_triton.py`
- 实现线索: 该提交来自本地 dev 分支更新，且未进入 `sgl-project/sglang` GitHub refs；优先关注命中的模型文件、性能后端、调度/缓存、parser/tokenizer 和测试覆盖。
- 已读文件:
  - runtime-perf: `python/sglang/srt/layers/attention/triton_backend.py`; `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`; `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`; `python/sglang/srt/layers/quantization/gptq_triton.py`
- 重复/备注: 重复 patch-id: 与 v0.5.8_dev..v0.5.9_dev 的 968d82d7 相同
- 验证与风险: 涉及模型入口或运行时适配；风险点是权重加载、并行切分、量化配置和短文本生成正确性。

<!-- LOCAL_ONLY_DEV_BRANCH_UPDATE_END -->
