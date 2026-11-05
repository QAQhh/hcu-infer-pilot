# sglang Qwen3.6 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` | [#38678](https://github.com/sgl-project/sglang/pull/38678), [#44707](https://github.com/sgl-project/sglang/pull/44707) |
| `docs/src/snippets/autoregressive/qwen36-deployment.jsx` | [#38678](https://github.com/sgl-project/sglang/pull/38678), [#44707](https://github.com/sgl-project/sglang/pull/44707) |
| `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` | [#46212](https://github.com/sgl-project/sglang/pull/46212) |

## PR 覆盖总览

- git 追溯 PR 数: 3
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 3
- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-16 | [#44707](https://github.com/sgl-project/sglang/pull/44707) | merged | [Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe | `docs/src/snippets/autoregressive/qwen36-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` |
| 2026-10-21 | [#38678](https://github.com/sgl-project/sglang/pull/38678) | merged | [Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6 | `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx` |
| 2026-10-29 | [#46212](https://github.com/sgl-project/sglang/pull/46212) | merged | [Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE. | `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` |

## 逐 PR diff 审计卡

### PR #44707 - [Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe

- 链接: https://github.com/sgl-project/sglang/pull/44707
- 状态/时间: merged / 2026-10-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`；关联提交 `56a3c4fa1676`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+56/-7，可读 patch 130 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe」；模型线: Qwen3.6；类别: 性能/后端优化；主要 diff: `docs/src/snippets/autoregressive/qwen36-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`；技术摘要: 覆盖「[Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe」；主要实现面是 `docs/src/snippets/autoregressive/qwen36-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +36/-5 (41 lines); hunks: -10,21 +10,28 @@ export const Qwen36Deployment = () => {; -59,10 +66,12 @@ export const Qwen36Deployment = () => {；`docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +20/-2 (22 lines); hunks: -101,6 +101,24 @@ This section provides deployment configurations optimized f...; -115,12 +133,12 @@ This section provides deployment configurations optimized...。
- 代码 diff 细节:
  - `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +36/-5 (41 lines); hunks: -10,21 +10,28 @@ export const Qwen36Deployment = () => {; -59,10 +66,12 @@ export const Qwen36Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +20/-2 (22 lines); hunks: -101,6 +101,24 @@ This section provides deployment configurations optimized f...; -115,12 +133,12 @@ This section provides deployment configurations optimized...
- 关键代码摘录:

```diff
diff -- docs/src/snippets/autoregressive/qwen36-deployment.jsx
@@ -10,21 +10,28 @@ export const Qwen36Deployment = () => {
+        { id: 'rtx-spark', label: 'RTX Spark', default: false },
-      items: [
+      // RTX Spark only has a validated recipe for 35B-A3B NVFP4.
+      getDynamicItems: (values) => [
-        { id: '27b', label: '27B (Dense)', default: false },
+        { id: '27b', label: '27B (Dense)', default: false, disabled: values.hardware === 'rtx-spark',
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx
@@ -101,6 +101,24 @@ This section provides deployment configurations optimized for different hardware
+### RTX Spark: 35B-A3B NVFP4
+Select **RTX Spark** in the generator above to use the single-node, single-GPU recipe for
+[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)
+on [NVIDIA RTX Spark](https://www.nvidia.com/en-us/products/rtx-spark/), which
+pairs a Blackwell RTX GPU with a Grace CPU and offers up to 128GB of unified
+memory. The contributor tested this command on SGLang `main`. The recipe uses
```

- 已读文件:
  - docs: `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +36/-5; `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +20/-2
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #38678 - [Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6

- 链接: https://github.com/sgl-project/sglang/pull/38678
- 状态/时间: merged / 2026-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`；关联提交 `9c10e0dd61f0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+202/-5，可读 patch 275 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6」；模型线: Qwen3.6；类别: 文档/测试/CI；主要 diff: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`；技术摘要: 覆盖「[Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6」；主要实现面是 `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +155/-2 (157 lines); hunks: -90,13 +90,15 @@ For the full Docker setup and other installation methods, pl...; -130,7 +132,8 @@ environment.；`docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +47/-3 (50 lines); hunks: -11,6 +11,17 @@ export const Qwen36Deployment = () => {; -27,8 +38,12 @@ export const Qwen36Deployment = () => {。
- 代码 diff 细节:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +155/-2 (157 lines); hunks: -90,13 +90,15 @@ For the full Docker setup and other installation methods, pl...; -130,7 +132,8 @@ environment.
  - `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +47/-3 (50 lines); hunks: -11,6 +11,17 @@ export const Qwen36Deployment = () => {; -27,8 +38,12 @@ export const Qwen36Deployment = () => {
- 关键代码摘录:

```diff
diff -- docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx
@@ -90,13 +90,15 @@ For the full Docker setup and other installation methods, please refer to the [o
+On Ascend NPUs (Atlas 800I A3), follow [SGLang installation with NPU support](/docs/hardware-platforms/ascend-npus/getting-started/installation) and the [Ascend NPU quickstart](/d
-**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform and capabilities.
+**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform and capabilities, i
@@ -130,7 +132,8 @@ environment.
-- Hardware requirements:
+- **Ascend NPU (Atlas 800I A3):** Each card has 2 dies, so `--tp-size` is twice the card count (1 card → `--tp-size 2`). Add `--attention-backend ascend --device npu` and `--mamba
diff -- docs/src/snippets/autoregressive/qwen36-deployment.jsx
@@ -11,6 +11,17 @@ export const Qwen36Deployment = () => {
+        { id: 'a3', label: 'A3 (NPU)', default: false },
+      ],
+    },
+    // Atlas 800I A3: 1 card = 2 dies, so --tp-size is twice the card count.
+    npuCards: {
+      name: 'npuCards',
```

- 已读文件:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +155/-2; `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +47/-3
- 验证与风险: 该 PR 主要落在文档/示例 `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`；验证重点是文档命令仍能映射到当前 CLI 参数和模型仓库名。

### PR #46212 - [Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE.

- 链接: https://github.com/sgl-project/sglang/pull/46212
- 状态/时间: merged / 2026-10-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`；关联提交 `019008afe0b0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 11 个文件，+586/-54，可读 patch 830 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE.」；模型线: Qwen3.6；类别: 性能/后端优化；主要 diff: `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`；技术摘要: 覆盖「[Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE.」；主要实现面是 `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` added +141/-0 (141 lines); hunks: -0,0 +1,141; symbols: TestNpuQwen36BlockFp8Gsm8k, setUpClass, tearDownClass, test_gsm8k，涉及 `TestNpuQwen36BlockFp8Gsm8k, setUpClass, tearDownClass`。
- 代码 diff 细节:
  - `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` added +141/-0 (141 lines); hunks: -0,0 +1,141; symbols: TestNpuQwen36BlockFp8Gsm8k, setUpClass, tearDownClass, test_gsm8k
- 关键代码摘录:

```diff
diff -- test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py
@@ -0,0 +1,141 @@
+"""Qwen3.6 native block-FP8 or MXFP8 TP2 + NEXTN accuracy on Ascend 950DT.
+Set QWEN36_FP8_MODEL_PATH and GSM8K_DATA_PATH to local files for offline runs.
+ASCEND_RT_VISIBLE_DEVICES selects the two devices; the test never pins card IDs.
+SGLANG_NPU_ARCH35_REQUANT_BLOCK_FP8=0/1 selects native/MXFP8 (default: 0).
+The legacy run_eval backend is intentional: preserve the deployment's chat,
+5-shot scoring protocol. With a 1319-row test.jsonl, its first five rows are
```

- 已读文件:
  - tests: `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` added +141/-0
- 验证与风险: diff 自带测试面 `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`, `test/registered/unit/npu/quantization/test_npu_mxfp8_linear.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
