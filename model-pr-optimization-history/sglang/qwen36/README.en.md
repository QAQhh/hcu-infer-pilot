# sglang Qwen3.6 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` | [#38678](https://github.com/sgl-project/sglang/pull/38678), [#44707](https://github.com/sgl-project/sglang/pull/44707) |
| `docs/src/snippets/autoregressive/qwen36-deployment.jsx` | [#38678](https://github.com/sgl-project/sglang/pull/38678), [#44707](https://github.com/sgl-project/sglang/pull/44707) |
| `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` | [#46212](https://github.com/sgl-project/sglang/pull/46212) |

## PR Coverage Summary

- Git-traced PRs: 3
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 3
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-10-16 | [#44707](https://github.com/sgl-project/sglang/pull/44707) | merged | [Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe | `docs/src/snippets/autoregressive/qwen36-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` |
| 2026-10-21 | [#38678](https://github.com/sgl-project/sglang/pull/38678) | merged | [Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6 | `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx` |
| 2026-10-29 | [#46212](https://github.com/sgl-project/sglang/pull/46212) | merged | [Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE. | `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` |

## Per-PR Diff Audit Cards

### PR #44707 - [Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe

- Link: https://github.com/sgl-project/sglang/pull/44707
- Status/date: merged / 2026-10-16
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`; associated commits `56a3c4fa1676`
- Diff scope read: GitHub Pull Request files API returned 2 files, +56/-7, 130 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe"; model line: Qwen3.6; category: performance/backend optimization; main diff: `docs/src/snippets/autoregressive/qwen36-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`; technical summary: Covers "[Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe"; the main implementation surface is `docs/src/snippets/autoregressive/qwen36-deployment.jsx`, `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +36/-5 (41 lines); hunks: -10,21 +10,28 @@ export const Qwen36Deployment = () => {; -59,10 +66,12 @@ export const Qwen36Deployment = () => {; `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +20/-2 (22 lines); hunks: -101,6 +101,24 @@ This section provides deployment configurations optimized f...; -115,12 +133,12 @@ This section provides deployment configurations optimized....
- Code diff details:
  - `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +36/-5 (41 lines); hunks: -10,21 +10,28 @@ export const Qwen36Deployment = () => {; -59,10 +66,12 @@ export const Qwen36Deployment = () => {
  - `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +20/-2 (22 lines); hunks: -101,6 +101,24 @@ This section provides deployment configurations optimized f...; -115,12 +133,12 @@ This section provides deployment configurations optimized...
- Key code excerpts:

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

- Reviewed files:
  - docs: `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +36/-5; `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +20/-2
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #38678 - [Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6

- Link: https://github.com/sgl-project/sglang/pull/38678
- Status/date: merged / 2026-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`; associated commits `9c10e0dd61f0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +202/-5, 275 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6"; model line: Qwen3.6; category: docs/tests/CI; main diff: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`; technical summary: Covers "[Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6"; the main implementation surface is `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +155/-2 (157 lines); hunks: -90,13 +90,15 @@ For the full Docker setup and other installation methods, pl...; -130,7 +132,8 @@ environment.; `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +47/-3 (50 lines); hunks: -11,6 +11,17 @@ export const Qwen36Deployment = () => {; -27,8 +38,12 @@ export const Qwen36Deployment = () => {.
- Code diff details:
  - `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +155/-2 (157 lines); hunks: -90,13 +90,15 @@ For the full Docker setup and other installation methods, pl...; -130,7 +132,8 @@ environment.
  - `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +47/-3 (50 lines); hunks: -11,6 +11,17 @@ export const Qwen36Deployment = () => {; -27,8 +38,12 @@ export const Qwen36Deployment = () => {
- Key code excerpts:

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

- Reviewed files:
  - docs: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx` modified +155/-2; `docs/src/snippets/autoregressive/qwen36-deployment.jsx` modified +47/-3
- Risk and verification: This is mostly docs/examples in `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #46212 - [Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE.

- Link: https://github.com/sgl-project/sglang/pull/46212
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`; associated commits `019008afe0b0`
- Diff scope read: GitHub Pull Request files API returned 11 files, +586/-54, 830 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE."; model line: Qwen3.6; category: performance/backend optimization; main diff: `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`; technical summary: Covers "[Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE."; the main implementation surface is `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` added +141/-0 (141 lines); hunks: -0,0 +1,141; symbols: TestNpuQwen36BlockFp8Gsm8k, setUpClass, tearDownClass, test_gsm8k, touching `TestNpuQwen36BlockFp8Gsm8k, setUpClass, tearDownClass`.
- Code diff details:
  - `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` added +141/-0 (141 lines); hunks: -0,0 +1,141; symbols: TestNpuQwen36BlockFp8Gsm8k, setUpClass, tearDownClass, test_gsm8k
- Key code excerpts:

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

- Reviewed files:
  - tests: `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py` added +141/-0
- Risk and verification: The diff ships test coverage in `test/registered/accuracy/models/test_npu_qwen36_block_fp8_gsm8k.py`, `test/registered/unit/npu/quantization/test_npu_mxfp8_linear.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
