# vllm DeepSeek V3/R1 模型 PR 优化历史

## 模型实现文件覆盖

| 文件 | git 追溯到的 PR |
| --- | --- |
| `examples/ray_serving/elastic_ep/serve_deepseek_v2.sh` | 无直接 PR 号提交 |
| `examples/tool_chat_template_deepseekv3.jinja` | [#17784](https://github.com/vllm-project/vllm/pull/17784) |
| `examples/tool_chat_template_deepseekv31.jinja` | [#23454](https://github.com/vllm-project/vllm/pull/23454) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` | [#30356](https://github.com/vllm-project/vllm/pull/30356) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` | [#59666](https://github.com/vllm-project/vllm/pull/59666) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` | [#30356](https://github.com/vllm-project/vllm/pull/30356) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` | [#59666](https://github.com/vllm-project/vllm/pull/59666) |
| `tests/evals/gsm8k/configs/models-h200-deepseek-r1-dp.txt` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-h200-deepseek-r1-tp.txt` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-h200-deepseek-v32-dp.txt` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-h200-deepseek-v32-tp.txt` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-r1-dp.txt` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-r1-tp.txt` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-v32-dp.txt` | 无直接 PR 号提交 |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-v32-tp.txt` | 无直接 PR 号提交 |
| `tests/reasoning/test_deepseekv3_reasoning_parser.py` | [#24972](https://github.com/vllm-project/vllm/pull/24972), [#25589](https://github.com/vllm-project/vllm/pull/25589), [#58626](https://github.com/vllm-project/vllm/pull/58626) |
| `tests/tool_parsers/test_deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `tests/tool_parsers/test_deepseekv32_tool_parser.py` | [#33703](https://github.com/vllm-project/vllm/pull/33703), [#36056](https://github.com/vllm-project/vllm/pull/36056), [#41198](https://github.com/vllm-project/vllm/pull/41198), [#41801](https://github.com/vllm-project/vllm/pull/41801), [#43019](https://github.com/vllm-project/vllm/pull/43019), [#43255](https://github.com/vllm-project/vllm/pull/43255) |
| `tests/tool_parsers/test_deepseekv3_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `vllm/model_executor/models/deepseek_mtp.py` | [#25896](https://github.com/vllm-project/vllm/pull/25896), [#29545](https://github.com/vllm-project/vllm/pull/29545), [#38684](https://github.com/vllm-project/vllm/pull/38684), [#38870](https://github.com/vllm-project/vllm/pull/38870), [#48036](https://github.com/vllm-project/vllm/pull/48036) |
| `vllm/model_executor/models/deepseek_v2.py` | [#13833](https://github.com/vllm-project/vllm/pull/13833), [#23971](https://github.com/vllm-project/vllm/pull/23971), [#24119](https://github.com/vllm-project/vllm/pull/24119), [#25896](https://github.com/vllm-project/vllm/pull/25896), [#25999](https://github.com/vllm-project/vllm/pull/25999), [#26456](https://github.com/vllm-project/vllm/pull/26456), [#26465](https://github.com/vllm-project/vllm/pull/26465), [#26670](https://github.com/vllm-project/vllm/pull/26670), [#26763](https://github.com/vllm-project/vllm/pull/26763), [#27532](https://github.com/vllm-project/vllm/pull/27532), [#27568](https://github.com/vllm-project/vllm/pull/27568), [#28968](https://github.com/vllm-project/vllm/pull/28968), ... (30 total) |
| `vllm/reasoning/deepseek_r1_reasoning_parser.py` | 无直接 PR 号提交 |
| `vllm/tool_parsers/deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `vllm/tool_parsers/deepseekv32_engine_tool_parser.py` | 无直接 PR 号提交 |
| `vllm/tool_parsers/deepseekv3_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |

## PR 覆盖总览

- git 追溯 PR 数: 46
- 原文档显式引用补充 PR 数: 0
- 当前文档总 PR 数: 46

- 自动归类说明: 无法安全锚定到单一模型家族的 PR 会进入 framework `shared/` 桶；同一 PR 若同时触及多个模型线，会保留在主模型桶并在正文里标注为 cross-model 证据。
- 文件追溯命令: `git log --name-only -- <model-files>`
- diff 审计来源: GitHub Pull Request files API

## 时间线

| 日期 | PR | 状态 | 标题 | 主要文件 |
| --- | --- | --- | --- | --- |
| 2026-10-19 | [#60362](https://github.com/vllm-project/vllm/pull/60362) | merged | [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers | `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py` |
| 2026-10-01 | [#59666](https://github.com/vllm-project/vllm/pull/59666) | merged | [ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s | `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` |
| 2026-09-25 | [#58626](https://github.com/vllm-project/vllm/pull/58626) | merged | [Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers | `tests/reasoning/test_deepseekv3_reasoning_parser.py` |
| 2026-09-22 | [#51915](https://github.com/vllm-project/vllm/pull/51915) | merged | [ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-07-20 | [#45964](https://github.com/vllm-project/vllm/pull/45964) | merged | [Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5) | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-07-14 | [#48036](https://github.com/vllm-project/vllm/pull/48036) | merged | [CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel | `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-06-28 | [#46600](https://github.com/vllm-project/vllm/pull/46600) | merged | [Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-05-29 | [#42982](https://github.com/vllm-project/vllm/pull/42982) | merged | [ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts) | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-05-21 | [#43255](https://github.com/vllm-project/vllm/pull/43255) | merged | [CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers | `tests/tool_parsers/test_deepseekv32_tool_parser.py` |
| 2026-05-20 | [#43019](https://github.com/vllm-project/vllm/pull/43019) | merged | [Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser | `tests/tool_parsers/test_deepseekv32_tool_parser.py` |
| 2026-05-06 | [#41801](https://github.com/vllm-project/vllm/pull/41801) | merged | [Bugfix] DeepSeekV32/v4: respect string='true\|false' attribute andunwrap arguments/input wrapper | `tests/tool_parsers/test_deepseekv32_tool_parser.py` |
| 2026-05-01 | [#41217](https://github.com/vllm-project/vllm/pull/41217) | merged | [ROCm][Deepseek] dsv3.2 further optimization | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-04-29 | [#41198](https://github.com/vllm-project/vllm/pull/41198) | merged | [Bugfix] DSV32/V4 add missing type conversion for non-streaming tool calls | `tests/tool_parsers/test_deepseekv32_tool_parser.py` |
| 2026-04-08 | [#37421](https://github.com/vllm-project/vllm/pull/37421) | merged | [Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-04-04 | [#38870](https://github.com/vllm-project/vllm/pull/38870) | merged | [Bugfix] Fix DSV32 weight loading | `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-04-02 | [#38684](https://github.com/vllm-project/vllm/pull/38684) | merged | [Perf] DSV3.2 Indexer Fused Weights Projection | `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py` |
| 2026-03-30 | [#33703](https://github.com/vllm-project/vllm/pull/33703) | merged | [Bugfix] Support multi-type params parsing for DeepSeek v3.2 | `tests/tool_parsers/test_deepseekv32_tool_parser.py` |
| 2026-03-19 | [#36056](https://github.com/vllm-project/vllm/pull/36056) | merged | [Bugfix] Fix Deepseekv32 tool parser when stream interval > 1 | `tests/tool_parsers/test_deepseekv32_tool_parser.py` |
| 2026-03-07 | [#36247](https://github.com/vllm-project/vllm/pull/36247) | merged | [Bugfix] Fix compressed-tensors quantization failure for DeepSeek-R1 on MI300x | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-03-02 | [#35751](https://github.com/vllm-project/vllm/pull/35751) | merged | [MoE][Perf] Wrap DSV3 QKVAProj GEMM in custom op for torch.compile | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-02-23 | [#34302](https://github.com/vllm-project/vllm/pull/34302) | merged | [ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup) | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-02-19 | [#34876](https://github.com/vllm-project/vllm/pull/34876) | merged | [Bug] Fix DeepSeek V3 weight loading caused by incorrect prefix | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-02-18 | [#34758](https://github.com/vllm-project/vllm/pull/34758) | merged | [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup) | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-02-07 | [#24972](https://github.com/vllm-project/vllm/pull/24972) | closed | [Model] Deepseek-V3.1 reasoning parser | `tests/reasoning/test_deepseekv3_reasoning_parser.py` |
| 2026-01-21 | [#29287](https://github.com/vllm-project/vllm/pull/29287) | merged | [ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-16 | [#32175](https://github.com/vllm-project/vllm/pull/32175) | merged | [Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding | `vllm/model_executor/models/deepseek_v2.py` |
| 2026-01-05 | [#30356](https://github.com/vllm-project/vllm/pull/30356) | merged | [CI][DeepSeek] Add nightly DeepSeek R1 `lm_eval` tests on H200 | `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` |
| 2025-12-24 | [#31160](https://github.com/vllm-project/vllm/pull/31160) | merged | [Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2 | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-19 | [#31046](https://github.com/vllm-project/vllm/pull/31046) | merged | [Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2 | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-17 | [#30841](https://github.com/vllm-project/vllm/pull/30841) | merged | [Bugfix] deepseek-V3.2 self.weights_proj has no bias | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-12 | [#27532](https://github.com/vllm-project/vllm/pull/27532) | merged | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-08 | [#27568](https://github.com/vllm-project/vllm/pull/27568) | merged | [DeepSeek v3.2] Make top-k work for any logit values. | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-12-02 | [#29545](https://github.com/vllm-project/vllm/pull/29545) | merged | [Bugfix] Fix DeepSeek R1 MTP weight loading | `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-11-20 | [#26670](https://github.com/vllm-project/vllm/pull/26670) | merged | [ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-11-19 | [#28968](https://github.com/vllm-project/vllm/pull/28968) | merged | [DeepSeek] Fix DeepSeek V3.2 Rope Embedding | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-10-21 | [#26465](https://github.com/vllm-project/vllm/pull/26465) | merged | [Deepseek v3.2] Remove extra logics in indexer | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-10-21 | [#26763](https://github.com/vllm-project/vllm/pull/26763) | merged | [Deepseek v3.2] Optimize top_k_per_row | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-10-15 | [#26456](https://github.com/vllm-project/vllm/pull/26456) | merged | [Deepseek-V3.2][Kernel] Integrate cuda indexer k cache gather | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-10-15 | [#25589](https://github.com/vllm-project/vllm/pull/25589) | merged | [Model] Add DeepSeek-V3.1 reasoning parser (split from PR #24972) | `tests/reasoning/test_deepseekv3_reasoning_parser.py` |
| 2025-10-02 | [#25999](https://github.com/vllm-project/vllm/pull/25999) | merged | [Deepseek v3.2] Support indexer prefill chunking | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-09-30 | [#25896](https://github.com/vllm-project/vllm/pull/25896) | merged | [New Model] DeepSeek-V3.2 (Rebased to Main) | `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py` |
| 2025-09-02 | [#24119](https://github.com/vllm-project/vllm/pull/24119) | merged | [Bug] R1 Accuracy: Fix `routed_scaling_factor` Double Mul Issue | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-08-30 | [#23971](https://github.com/vllm-project/vllm/pull/23971) | merged | Add LoRA support for DeepSeek models (V2, V3, R1-0528) | `vllm/model_executor/models/deepseek_v2.py` |
| 2025-08-23 | [#23454](https://github.com/vllm-project/vllm/pull/23454) | merged | Support DeepSeek-V3.1 tool call | `examples/tool_chat_template_deepseekv31.jinja` |
| 2025-05-12 | [#17784](https://github.com/vllm-project/vllm/pull/17784) | merged | [Feature] Support DeepSeekV3 Function Call | `examples/tool_chat_template_deepseekv3.jinja` |
| 2025-02-26 | [#13833](https://github.com/vllm-project/vllm/pull/13833) | merged | DeepSeek V2/V3/R1 only place `lm_head` on last pp rank | `vllm/model_executor/models/deepseek_v2.py` |

## 逐 PR diff 审计卡

### PR #60362 - [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers

- 链接: https://github.com/vllm-project/vllm/pull/60362
- 状态/时间: merged / 2026-10-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv3_tool_parser.py`；关联提交 `e347836d68be`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+55/-4，可读 patch 108 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`；技术摘要: 覆盖「[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers」；主要实现面是 `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv3_tool_parser.py` modified +27/-0 (27 lines); hunks: -1,6 +1,7; -92,6 +93,32 @@ def test_config(self) -> ToolParserTestConfig:; symbols: test_config, test_multiline_json_arguments, test_preserves_text_after_tool_call，涉及 `test_config, test_multiline_json_arguments, test_preserves_text_after_tool_call`；`tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments，涉及 `test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments`；`vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__，涉及 `__init__`；`vllm/tool_parsers/deepseekv3_tool_parser.py` modified +3/-2 (5 lines); hunks: -46,12 +46,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv3_tool_parser.py` modified +27/-0 (27 lines); hunks: -1,6 +1,7; -92,6 +93,32 @@ def test_config(self) -> ToolParserTestConfig:; symbols: test_config, test_multiline_json_arguments, test_preserves_text_after_tool_call
  - `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments
  - `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__
  - `vllm/tool_parsers/deepseekv3_tool_parser.py` modified +3/-2 (5 lines); hunks: -46,12 +46,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv3_tool_parser.py
@@ -1,6 +1,7 @@
+import json
@@ -92,6 +93,32 @@ def test_config(self) -> ToolParserTestConfig:
+    def test_multiline_json_arguments(self, tool_parser, streaming: bool):
+        # The model may pretty-print the JSON arguments over several lines.
+        weather = {"city": "Tokyo", "unit": "celsius"}
+        hotels = {"location": "Tokyo", "check_in": "2025-01-15"}
diff -- tests/tool_parsers/test_deepseekv31_tool_parser.py
@@ -1,8 +1,11 @@
+import json
+from tests.tool_parsers.utils import run_tool_extraction
@@ -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):
+@pytest.mark.parametrize("streaming", [True, False])
+def test_extract_tool_calls_with_multiline_arguments(parser, streaming):
+    # The model may pretty-print the JSON arguments over several lines.
diff -- vllm/tool_parsers/deepseekv31_tool_parser.py
@@ -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Tool] | None = None):
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv3_tool_parser.py` modified +27/-0; `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0
  - runtime: `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2; `vllm/tool_parsers/deepseekv3_tool_parser.py` modified +3/-2
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_deepseekv3_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #59666 - [ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s

- 链接: https://github.com/vllm-project/vllm/pull/59666
- 状态/时间: merged / 2026-10-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`；关联提交 `d2125ea68178`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+2/-2，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s」；模型线: DeepSeek V3/R1；类别: 文档/测试/CI；主要 diff: `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`；技术摘要: 覆盖「[ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s」；主要实现面是 `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"；`tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"
  - `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml
@@ -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"
-startup_max_wait_seconds: 1200
+startup_max_wait_seconds: 1800
diff -- tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml
@@ -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"
-startup_max_wait_seconds: 1200
+startup_max_wait_seconds: 1800
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` modified +1/-1; `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` modified +1/-1
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #58626 - [Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers

- 链接: https://github.com/vllm-project/vllm/pull/58626
- 状态/时间: merged / 2026-09-25
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_deepseekv3_reasoning_parser.py`；关联提交 `064bc747ab42`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+136/-3，可读 patch 195 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/reasoning/test_deepseekv3_reasoning_parser.py`；技术摘要: 覆盖「[Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers」；主要实现面是 `tests/reasoning/test_deepseekv3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_deepseekv3_reasoning_parser.py` modified +11/-0 (11 lines); hunks: -87,3 +87,14 @@ def test_identity_reasoning_parser_basic(tokenizer):; symbols: test_identity_reasoning_parser_basic, test_count_reasoning_tokens_delegates，涉及 `test_identity_reasoning_parser_basic, test_count_reasoning_tokens_delegates`。
- 代码 diff 细节:
  - `tests/reasoning/test_deepseekv3_reasoning_parser.py` modified +11/-0 (11 lines); hunks: -87,3 +87,14 @@ def test_identity_reasoning_parser_basic(tokenizer):; symbols: test_identity_reasoning_parser_basic, test_count_reasoning_tokens_delegates
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_deepseekv3_reasoning_parser.py
@@ -87,3 +87,14 @@ def test_identity_reasoning_parser_basic(tokenizer):
+@pytest.mark.parametrize("thinking,expected", [(True, 3), (False, 0)])
+def test_count_reasoning_tokens_delegates(tokenizer, thinking, expected):
+    parser = DeepSeekV3ReasoningParser(
+        tokenizer, chat_template_kwargs={"thinking": thinking}
+    )
+    think = tokenizer.convert_tokens_to_ids(["<think>", "</think>"])
```

- 已读文件:
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py` modified +11/-0
- 验证与风险: diff 自带测试面 `tests/parser/test_harmony.py`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `tests/reasoning/test_step3_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #51915 - [ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness

- 链接: https://github.com/vllm-project/vllm/pull/51915
- 状态/时间: merged / 2026-09-22
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `1c0eee919db3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+319/-212，可读 patch 1215 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -665,6 +665,11 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVC...; symbols: get_kv_cache_spec, forward, uses_shuffled_layout, get_attn_backend，涉及 `get_kv_cache_spec, forward, uses_shuffled_layout`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -665,6 +665,11 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVC...; symbols: get_kv_cache_spec, forward, uses_shuffled_layout, get_attn_backend
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -665,6 +665,11 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
+    @property
+    def uses_shuffled_layout(self) -> bool:
+        """Whether this cache's reader expects the shuffled value layout."""
+        return False
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +5/-0
- 验证与风险: diff 自带测试面 `tests/kernels/test_fused_deepseek_v32_norm_rope.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #45964 - [Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5)

- 链接: https://github.com/vllm-project/vllm/pull/45964
- 状态/时间: merged / 2026-07-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `2396a611085d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+157/-15，可读 patch 443 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5)」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5)」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -33,6 +33,7; -56,6 +57,7; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -33,6 +33,7; -56,6 +57,7; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -33,6 +33,7 @@
+import vllm.envs as envs
@@ -56,6 +57,7 @@
+    DCPGroupColumnParallelLinear,
@@ -1015,17 +1017,25 @@ def __init__(
+        qrep_enabled = (
+            envs.VLLM_DCP_Q_REPLICATE
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_mla_backends.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #48036 - [CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel

- 链接: https://github.com/vllm-project/vllm/pull/48036
- 状态/时间: merged / 2026-07-14
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_mtp.py`；关联提交 `1ff9429655f0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+34/-3，可读 patch 79 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_mtp.py`；技术摘要: 覆盖「[CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel」；主要实现面是 `vllm/model_executor/models/deepseek_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_mtp.py` modified +24/-0 (24 lines); hunks: -10,6 +10,7; -40,6 +41,24; symbols: _restore_full_token_layout_if_needed, SharedHead, __init__, forward，涉及 `_restore_full_token_layout_if_needed, SharedHead, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_mtp.py` modified +24/-0 (24 lines); hunks: -10,6 +10,7; -40,6 +41,24; symbols: _restore_full_token_layout_if_needed, SharedHead, __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_mtp.py
@@ -10,6 +10,7 @@
+from vllm.distributed import tensor_model_parallel_all_gather
@@ -40,6 +41,24 @@
+def _restore_full_token_layout_if_needed(
+    hidden_states: torch.Tensor,
+    residual: torch.Tensor,
+    num_tokens: int,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_mtp.py` modified +24/-0
- 验证与风险: runtime 路径改动集中在 `vllm/config/parallel.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/deepseek_v32/nvidia/mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #46600 - [Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers

- 链接: https://github.com/vllm-project/vllm/pull/46600
- 状态/时间: merged / 2026-06-28
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `6eb63a1da699`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+10/-0，可读 patch 24 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +10/-0 (10 lines); hunks: -1438,6 +1438,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; -1446,6 +1451,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +10/-0 (10 lines); hunks: -1438,6 +1438,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; -1446,6 +1451,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -1438,6 +1438,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+        # With index_topk_freq>1 only some layers build an indexer, yet the
+        # checkpoint ships indexer weights for all of them; track the built ones.
+        indexer_present_prefixes = {
+            n.rsplit(".indexer.", 1)[0] for n in params_dict if ".indexer." in n
+        }
@@ -1446,6 +1451,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +10/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #42982 - [ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts)

- 链接: https://github.com/vllm-project/vllm/pull/42982
- 状态/时间: merged / 2026-05-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `0b56815a24f4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+59/-29，可读 patch 125 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts)」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts)」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +2/-4 (6 lines); hunks: -304,10 +304,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-4 (6 lines); hunks: -304,10 +304,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -304,10 +304,8 @@ def __init__(
-            # AITER biased_grouped_topk requires the correction bias dtype to
-            # match the router logits. Keep DeepSeek's correction bias in fp32
-            # by requesting fp32 router logits for this routing path.
-            self.gate.set_out_dtype(torch.float32)
+            # Accumulates in fp32; avoids bf16->fp32 cast.
+            self.gate.set_out_dtype(self.gate.weight.dtype)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-4
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #43255 - [CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers

- 链接: https://github.com/vllm-project/vllm/pull/43255
- 状态/时间: merged / 2026-05-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；关联提交 `63ea11709bd9`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+186/-0，可读 patch 204 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`；技术摘要: 覆盖「[CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers」；主要实现面是 `tests/tool_parsers/test_deepseekv32_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +137/-0 (137 lines); hunks: -221,6 +221,99 @@ def test_string_attr_false_allows_schema_conversion(self):; -581,6 +674,50 @@ def test_string_attr_true_preserves_literal_in_streaming(se...; symbols: test_string_attr_false_allows_schema_conversion, test_composed_schema_converts_object_and_array_params, test_string_attr_true_preserves_literal_for_composed_schema, test_arguments_wrapper_repaired，涉及 `test_string_attr_false_allows_schema_conversion, test_composed_schema_converts_object_and_array_params, test_string_attr_true_preserves_literal_for_composed_schema`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +137/-0 (137 lines); hunks: -221,6 +221,99 @@ def test_string_attr_false_allows_schema_conversion(self):; -581,6 +674,50 @@ def test_string_attr_true_preserves_literal_in_streaming(se...; symbols: test_string_attr_false_allows_schema_conversion, test_composed_schema_converts_object_and_array_params, test_string_attr_true_preserves_literal_for_composed_schema, test_arguments_wrapper_repaired
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv32_tool_parser.py
@@ -221,6 +221,99 @@ def test_string_attr_false_allows_schema_conversion(self):
+    @pytest.mark.skip_global_cleanup
+    def test_composed_schema_converts_object_and_array_params(self):
+        """Composed JSON Schema types must still drive DSML type coercion."""
+        tool = ChatCompletionToolsParam(
+            function=FunctionDefinition(
+                name="set_timer",
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +137/-0
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #43019 - [Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser

- 链接: https://github.com/vllm-project/vllm/pull/43019
- 状态/时间: merged / 2026-05-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；关联提交 `a10d69116cb2`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+270/-285，可读 patch 615 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser」；主要实现面是 `tests/tool_parsers/test_deepseekv32_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +261/-233 (494 lines); hunks: -16,7 +16,6; -65,58 +64,6 @@ def build_tool_call(func_name: str, params: dict[str, str]) -...; symbols: build_tool_call, TestConvertParamValue, parser, test_null，涉及 `build_tool_call, TestConvertParamValue, parser`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +261/-233 (494 lines); hunks: -16,7 +16,6; -65,58 +64,6 @@ def build_tool_call(func_name: str, params: dict[str, str]) -...; symbols: build_tool_call, TestConvertParamValue, parser, test_null
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv32_tool_parser.py
@@ -16,7 +16,6 @@
-from vllm.tokenizers import get_tokenizer
@@ -65,58 +64,6 @@ def build_tool_call(func_name: str, params: dict[str, str]) -> str:
-# ---------------------------------------------------------------------------
-# Tests: DeepSeekV32ToolParser._convert_param_value
-# ---------------------------------------------------------------------------
-class TestConvertParamValue:
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +261/-233
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41801 - [Bugfix] DeepSeekV32/v4: respect string='true|false' attribute andunwrap arguments/input wrapper

- 链接: https://github.com/vllm-project/vllm/pull/41801
- 状态/时间: merged / 2026-05-06
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；关联提交 `95582868efd4`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+224/-10，可读 patch 298 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] DeepSeekV32/v4: respect string='true|false' attribute andunwrap arguments/input wrapper」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`；技术摘要: 覆盖「[Bugfix] DeepSeekV32/v4: respect string='true|false' attribute andunwrap arguments/input wrapper」；主要实现面是 `tests/tool_parsers/test_deepseekv32_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +155/-2 (157 lines); hunks: -203,7 +203,14 @@ def test_type_conversion_in_non_streaming(self):; -212,6 +219,118 @@ def test_type_conversion_in_non_streaming(self):; symbols: test_type_conversion_in_non_streaming, test_string_attr_true_preserves_literal_despite_schema, test_string_attr_false_allows_schema_conversion, test_arguments_wrapper_repaired，涉及 `test_type_conversion_in_non_streaming, test_string_attr_true_preserves_literal_despite_schema, test_string_attr_false_allows_schema_conversion`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +155/-2 (157 lines); hunks: -203,7 +203,14 @@ def test_type_conversion_in_non_streaming(self):; -212,6 +219,118 @@ def test_type_conversion_in_non_streaming(self):; symbols: test_type_conversion_in_non_streaming, test_string_attr_true_preserves_literal_despite_schema, test_string_attr_false_allows_schema_conversion, test_arguments_wrapper_repaired
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv32_tool_parser.py
@@ -203,7 +203,14 @@ def test_type_conversion_in_non_streaming(self):
-        model_output = build_tool_call("toggle", {"enabled": "true", "count": "42"})
+        model_output = (
+            f"{FC_START}\n"
+            f'{INV_START}toggle">\n'
+            f'{PARAM_START}enabled" string="false">true{PARAM_END}\n'
+            f'{PARAM_START}count" string="false">42{PARAM_END}\n'
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +155/-2
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #41217 - [ROCm][Deepseek] dsv3.2 further optimization

- 链接: https://github.com/vllm-project/vllm/pull/41217
- 状态/时间: merged / 2026-05-01
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `bc635fad2389`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+293/-73，可读 patch 605 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Deepseek] dsv3.2 further optimization」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCm][Deepseek] dsv3.2 further optimization」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +38/-23 (61 lines); hunks: -674,30 +674,45 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +38/-23 (61 lines); hunks: -674,30 +674,45 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -674,30 +674,45 @@ def forward(
-        q_pe, q_nope = torch.split(
-            q, [self.rope_dim, self.head_dim - self.rope_dim], dim=-1
-        )
-        # Fused wk + weights_proj: one GEMM, then split
-        kw, _ = self.wk_weights_proj(hidden_states)
-        k = kw[:, : self.head_dim]
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +38/-23
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #41198 - [Bugfix] DSV32/V4 add missing type conversion for non-streaming tool calls

- 链接: https://github.com/vllm-project/vllm/pull/41198
- 状态/时间: merged / 2026-04-29
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；关联提交 `762022cafb1a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+26/-1，可读 patch 46 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] DSV32/V4 add missing type conversion for non-streaming tool calls」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`；技术摘要: 覆盖「[Bugfix] DSV32/V4 add missing type conversion for non-streaming tool calls」；主要实现面是 `tests/tool_parsers/test_deepseekv32_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +24/-0 (24 lines); hunks: -188,6 +188,30 @@ def test_multiple_tools(self, parser):; symbols: test_multiple_tools, test_type_conversion_in_non_streaming，涉及 `test_multiple_tools, test_type_conversion_in_non_streaming`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +24/-0 (24 lines); hunks: -188,6 +188,30 @@ def test_multiple_tools(self, parser):; symbols: test_multiple_tools, test_type_conversion_in_non_streaming
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv32_tool_parser.py
@@ -188,6 +188,30 @@ def test_multiple_tools(self, parser):
+    def test_type_conversion_in_non_streaming(self):
+        """Non-streaming extraction must convert params using the tool schema."""
+        tool = ChatCompletionToolsParam(
+            function=FunctionDefinition(
+                name="toggle",
+                parameters={
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +24/-0
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #37421 - [Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode

- 链接: https://github.com/vllm-project/vllm/pull/37421
- 状态/时间: merged / 2026-04-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `b55d830ec782`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+2039/-483，可读 patch 2698 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +6/-2 (8 lines); hunks: -67,7 +67,9; -1203,7 +1205,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-2 (8 lines); hunks: -67,7 +67,9; -1203,7 +1205,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -67,7 +67,9 @@
-from vllm.model_executor.layers.sparse_attn_indexer import SparseAttnIndexer
+from vllm.model_executor.layers.sparse_attn_indexer import (
+    SparseAttnIndexer,
+)
@@ -1203,7 +1205,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-                vllm_config, prefix, topk_indices_buffer=topk_indices_buffer
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-2
- 验证与风险: diff 自带测试面 `tests/kernels/test_top_k_per_row.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #38870 - [Bugfix] Fix DSV32 weight loading

- 链接: https://github.com/vllm-project/vllm/pull/38870
- 状态/时间: merged / 2026-04-04
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`；关联提交 `8617f8676b5a`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+68/-27，可读 patch 158 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix DSV32 weight loading」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`；技术摘要: 覆盖「[Bugfix] Fix DSV32 weight loading」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +55/-24 (79 lines); hunks: -625,6 +625,11 @@ def __init__(; -639,18 +644,36 @@ def __init__(; symbols: __init__, forward，涉及 `__init__, forward`；`vllm/model_executor/models/deepseek_mtp.py` modified +13/-3 (16 lines); hunks: -184,11 +184,16 @@ class DeepSeekMTP(nn.Module, DeepseekV2MixtureOfExperts):; -241,11 +246,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: DeepSeekMTP, __init__, set_moe_parameters, load_weights，涉及 `DeepSeekMTP, __init__, set_moe_parameters`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +55/-24 (79 lines); hunks: -625,6 +625,11 @@ def __init__(; -639,18 +644,36 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/deepseek_mtp.py` modified +13/-3 (16 lines); hunks: -184,11 +184,16 @@ class DeepSeekMTP(nn.Module, DeepseekV2MixtureOfExperts):; -241,11 +246,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: DeepSeekMTP, __init__, set_moe_parameters, load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -625,6 +625,11 @@ def __init__(
+        self.quant_config = quant_config
+        self.is_fp4_ckpt = (
+            self.quant_config is not None
+            and self.quant_config.get_name() == "modelopt_fp4"
+        )
@@ -639,18 +644,36 @@ def __init__(
diff -- vllm/model_executor/models/deepseek_mtp.py
@@ -184,11 +184,16 @@ class DeepSeekMTP(nn.Module, DeepseekV2MixtureOfExperts):
+        self.quant_config = vllm_config.quant_config
+        self.is_fp4_ckpt = (
+            self.quant_config is not None
+            and self.quant_config.get_name() == "modelopt_fp4"
+        )
@@ -241,11 +246,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +55/-24; `vllm/model_executor/models/deepseek_mtp.py` modified +13/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #38684 - [Perf] DSV3.2 Indexer Fused Weights Projection

- 链接: https://github.com/vllm-project/vllm/pull/38684
- 状态/时间: merged / 2026-04-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`；关联提交 `5f96f9aff10f`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+25/-14，可读 patch 79 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Perf] DSV3.2 Indexer Fused Weights Projection」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`；技术摘要: 覆盖「[Perf] DSV3.2 Indexer Fused Weights Projection」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +22/-14 (36 lines); hunks: -639,21 +639,19 @@ def __init__(; -694,7 +692,11 @@ def forward(; symbols: __init__, forward, load_weights，涉及 `__init__, forward, load_weights`；`vllm/model_executor/models/deepseek_mtp.py` modified +3/-0 (3 lines); hunks: -241,6 +241,9 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +22/-14 (36 lines); hunks: -639,21 +639,19 @@ def __init__(; -694,7 +692,11 @@ def forward(; symbols: __init__, forward, load_weights
  - `vllm/model_executor/models/deepseek_mtp.py` modified +3/-0 (3 lines); hunks: -241,6 +241,9 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -639,21 +639,19 @@ def __init__(
-        self.wk = ReplicatedLinear(
+        # Fused wk + weights_proj: single GEMM producing [head_dim + n_head].
+        # weights_proj does not get quantized, so we run both with quant_config=None
+        # wk may be upcasted from the default quant; experiments show fusion is always
+        # faster unless WK proj is in FP4, which is not the case for all known quants.
+        self.wk_weights_proj = MergedColumnParallelLinear(
diff -- vllm/model_executor/models/deepseek_mtp.py
@@ -241,6 +241,9 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+            # Fused indexer wk + weights_proj
+            ("wk_weights_proj", "wk", 0),
+            ("wk_weights_proj", "weights_proj", 1),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +22/-14; `vllm/model_executor/models/deepseek_mtp.py` modified +3/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #33703 - [Bugfix] Support multi-type params parsing for DeepSeek v3.2

- 链接: https://github.com/vllm-project/vllm/pull/33703
- 状态/时间: merged / 2026-03-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；关联提交 `a6db99ba02ec`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+201/-18，可读 patch 250 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Support multi-type params parsing for DeepSeek v3.2」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Support multi-type params parsing for DeepSeek v3.2」；主要实现面是 `tests/tool_parsers/test_deepseekv32_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +181/-0 (181 lines); hunks: -11,6 +11,7; -474,3 +475,183 @@ def test_no_emission_while_incomplete(self, parser):; symbols: test_no_emission_while_incomplete, deepseekv32_tokenizer, parser, test_convert_param_value_single_types，涉及 `test_no_emission_while_incomplete, deepseekv32_tokenizer, parser`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +181/-0 (181 lines); hunks: -11,6 +11,7; -474,3 +475,183 @@ def test_no_emission_while_incomplete(self, parser):; symbols: test_no_emission_while_incomplete, deepseekv32_tokenizer, parser, test_convert_param_value_single_types
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv32_tool_parser.py
@@ -11,6 +11,7 @@
+from vllm.tokenizers import get_tokenizer
@@ -474,3 +475,183 @@ def test_no_emission_while_incomplete(self, parser):
+@pytest.fixture(scope="module")
+def deepseekv32_tokenizer():
+    return get_tokenizer(tokenizer_name="deepseek-ai/DeepSeek-V3.2")
+@pytest.fixture
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +181/-0
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36056 - [Bugfix] Fix Deepseekv32 tool parser when stream interval > 1

- 链接: https://github.com/vllm-project/vllm/pull/36056
- 状态/时间: merged / 2026-03-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；关联提交 `be12afd284f3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+622/-437，可读 patch 1113 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix Deepseekv32 tool parser when stream interval > 1」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`；技术摘要: 覆盖「[Bugfix] Fix Deepseekv32 tool parser when stream interval > 1」；主要实现面是 `tests/tool_parsers/test_deepseekv32_tool_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/tool_parsers/test_deepseekv32_tool_parser.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: make_parser, make_tool_param, make_request, build_tool_call，涉及 `make_parser, make_tool_param, make_request`。
- 代码 diff 细节:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: make_parser, make_tool_param, make_request, build_tool_call
- 关键代码摘录:

```diff
diff -- tests/tool_parsers/test_deepseekv32_tool_parser.py
@@ -0,0 +1,476 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Unit tests for DeepSeekV32ToolParser.
+These tests use a minimal mock tokenizer so no real model weights are required.
+"""
+import json
```

- 已读文件:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` added +476/-0
- 验证与风险: diff 自带测试面 `tests/tool_parsers/test_deepseekv32_tool_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #36247 - [Bugfix] Fix compressed-tensors quantization failure for DeepSeek-R1 on MI300x

- 链接: https://github.com/vllm-project/vllm/pull/36247
- 状态/时间: merged / 2026-03-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `ee8a29511fc6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix compressed-tensors quantization failure for DeepSeek-R1 on MI300x」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bugfix] Fix compressed-tensors quantization failure for DeepSeek-R1 on MI300x」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -756,7 +756,7 @@ def _min_latency_fused_qkv_a_proj_fake(; -848,7 +848,7 @@ def __init__(; symbols: _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj, DeepSeekV2FusedQkvAProjLinear, __init__，涉及 `_min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj, DeepSeekV2FusedQkvAProjLinear`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -756,7 +756,7 @@ def _min_latency_fused_qkv_a_proj_fake(; -848,7 +848,7 @@ def __init__(; symbols: _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj, DeepSeekV2FusedQkvAProjLinear, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -756,7 +756,7 @@ def _min_latency_fused_qkv_a_proj_fake(
-class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):
+class DeepSeekV2FusedQkvAProjLinear(MergedColumnParallelLinear):
@@ -848,7 +848,7 @@ def __init__(
-            self.fused_qkv_a_proj = DeepSeekV2FusedQkvAProj(
+            self.fused_qkv_a_proj = DeepSeekV2FusedQkvAProjLinear(
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #35751 - [MoE][Perf] Wrap DSV3 QKVAProj GEMM in custom op for torch.compile

- 链接: https://github.com/vllm-project/vllm/pull/35751
- 状态/时间: merged / 2026-03-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `9319044ee9a1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+41/-13，可读 patch 75 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[MoE][Perf] Wrap DSV3 QKVAProj GEMM in custom op for torch.compile」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[MoE][Perf] Wrap DSV3 QKVAProj GEMM in custom op for torch.compile」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +41/-13 (54 lines); hunks: -75,6 +75,7; -717,6 +718,44 @@ def forward(; symbols: forward, _min_latency_fused_qkv_a_proj_impl, _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj，涉及 `forward, _min_latency_fused_qkv_a_proj_impl, _min_latency_fused_qkv_a_proj_fake`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +41/-13 (54 lines); hunks: -75,6 +75,7; -717,6 +718,44 @@ def forward(; symbols: forward, _min_latency_fused_qkv_a_proj_impl, _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -75,6 +75,7 @@
+from vllm.utils.torch_utils import direct_register_custom_op
@@ -717,6 +718,44 @@ def forward(
+def _min_latency_fused_qkv_a_proj_impl(
+    input_: torch.Tensor,
+    weight: torch.Tensor,
+) -> torch.Tensor:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +41/-13
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34302 - [ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup)

- 链接: https://github.com/vllm-project/vllm/pull/34302
- 状态/时间: merged / 2026-02-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `8435b2e04925`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+915/-3，可读 patch 971 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup)」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup)」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +75/-2 (77 lines); hunks: -221,6 +221,73 @@ def forward(self, x):; -249,10 +316,9 @@ def __init__(; symbols: forward, DeepSeekV2Gate, __init__, set_out_dtype，涉及 `forward, DeepSeekV2Gate, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +75/-2 (77 lines); hunks: -221,6 +221,73 @@ def forward(self, x):; -249,10 +316,9 @@ def __init__(; symbols: forward, DeepSeekV2Gate, __init__, set_out_dtype
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -221,6 +221,73 @@ def forward(self, x):
+class DeepSeekV2Gate(ReplicatedLinear):
+    def __init__(
+        self,
+        hidden_size: int,
+        n_experts: int,
+        quant_config: QuantizationConfig | None = None,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +75/-2
- 验证与风险: runtime 路径改动集中在 `vllm/_custom_ops.py`, `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34876 - [Bug] Fix DeepSeek V3 weight loading caused by incorrect prefix

- 链接: https://github.com/vllm-project/vllm/pull/34876
- 状态/时间: merged / 2026-02-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `7f51e9386470`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-2，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug] Fix DeepSeek V3 weight loading caused by incorrect prefix」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bug] Fix DeepSeek V3 weight loading caused by incorrect prefix」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -716,7 +716,7 @@ class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):; -726,7 +726,7 @@ def __init__(; symbols: DeepSeekV2FusedQkvAProj, __init__，涉及 `DeepSeekV2FusedQkvAProj, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -716,7 +716,7 @@ class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):; -726,7 +726,7 @@ def __init__(; symbols: DeepSeekV2FusedQkvAProj, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -716,7 +716,7 @@ class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):
-        output_size: int,
+        output_size: list[int],
@@ -726,7 +726,7 @@ def __init__(
-            prefix=f"{prefix}.kv_a_proj_with_mqa",
+            prefix=prefix,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #34758 - [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup)

- 链接: https://github.com/vllm-project/vllm/pull/34758
- 状态/时间: merged / 2026-02-18
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `6874638bc443`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 7 个文件，+855/-3，可读 patch 917 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup)」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup)」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +60/-3 (63 lines); hunks: -32,6 +32,7; -711,6 +712,64 @@ def forward(; symbols: forward, DeepSeekV2FusedQkvAProj, __init__, DeepseekV2MLAAttention，涉及 `forward, DeepSeekV2FusedQkvAProj, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +60/-3 (63 lines); hunks: -32,6 +32,7; -711,6 +712,64 @@ def forward(; symbols: forward, DeepSeekV2FusedQkvAProj, __init__, DeepseekV2MLAAttention
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -32,6 +32,7 @@
+import vllm._custom_ops as ops
@@ -711,6 +712,64 @@ def forward(
+class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):
+    def __init__(
+        self,
+        input_size: int,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +60/-3
- 验证与风险: runtime 路径改动集中在 `vllm/_custom_ops.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #24972 - [Model] Deepseek-V3.1 reasoning parser

- 链接: https://github.com/vllm-project/vllm/pull/24972
- 状态/时间: closed / 2026-02-07
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_deepseekv3_reasoning_parser.py`；关联提交 `85a65e7f51ad`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 15 个文件，+214/-11，可读 patch 330 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Deepseek-V3.1 reasoning parser」；模型线: DeepSeek V3/R1；类别: 文档/测试/CI；主要 diff: `tests/reasoning/test_deepseekv3_reasoning_parser.py`；技术摘要: 覆盖「[Model] Deepseek-V3.1 reasoning parser」；主要实现面是 `tests/reasoning/test_deepseekv3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +73/-0 (73 lines); hunks: -0,0 +1,73; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic，涉及 `tokenizer, test_parser_selection, test_identity_reasoning_parser_basic`。
- 代码 diff 细节:
  - `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +73/-0 (73 lines); hunks: -0,0 +1,73; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_deepseekv3_reasoning_parser.py
@@ -0,0 +1,73 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from transformers import AutoTokenizer
+from vllm.entrypoints.openai.protocol import (ChatCompletionRequest,
+                                              DeltaMessage)
```

- 已读文件:
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +73/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_deepseekv3_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29287 - [ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp

- 链接: https://github.com/vllm-project/vllm/pull/29287
- 状态/时间: merged / 2026-01-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `6c20e89c0209`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 8 个文件，+982/-323，可读 patch 1521 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +14/-233 (247 lines); hunks: -43,7 +43,6; -63,6 +62,7; symbols: get_attn_backend, sparse_attn_indexer, sparse_attn_indexer_fake, Indexer，涉及 `get_attn_backend, sparse_attn_indexer, sparse_attn_indexer_fake`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +14/-233 (247 lines); hunks: -43,7 +43,6; -63,6 +62,7; symbols: get_attn_backend, sparse_attn_indexer, sparse_attn_indexer_fake, Indexer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -43,7 +43,6 @@
-from vllm.forward_context import get_forward_context
@@ -63,6 +62,7 @@
+from vllm.model_executor.layers.sparse_attn_indexer import SparseAttnIndexer
@@ -74,16 +74,11 @@
-from vllm.utils.deep_gemm import fp8_mqa_logits, fp8_paged_mqa_logits
-from vllm.utils.torch_utils import direct_register_custom_op
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +14/-233
- 验证与风险: runtime 路径改动集中在 `vllm/_aiter_ops.py`, `vllm/config/compilation.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #32175 - [Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding

- 链接: https://github.com/vllm-project/vllm/pull/32175
- 状态/时间: merged / 2026-01-16
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `5de6dd0662da`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+9/-2，可读 patch 38 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +9/-2 (11 lines); hunks: -717,13 +717,20 @@ def sparse_attn_indexer(; -739,14 +746,14 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer，涉及 `sparse_attn_indexer`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +9/-2 (11 lines); hunks: -717,13 +717,20 @@ def sparse_attn_indexer(; -739,14 +746,14 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -717,13 +717,20 @@ def sparse_attn_indexer(
+            # [num_decode_tokens, n_head, head_dim] -> [bs, 1+next_n, n_head, head_dim]
+            # [num_decode_tokens, n_head] -> [bs, 1+next_n, n_head]
+            padded_weights = pack_seq_triton(weights[:num_decode_tokens], decode_lens)
+            # [bs, 1+next_n, n_head] -> [bs * next_n, n_head]
+            padded_weights = padded_weights.flatten(0, 1)
+            padded_weights = weights
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +9/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30356 - [CI][DeepSeek] Add nightly DeepSeek R1 `lm_eval` tests on H200

- 链接: https://github.com/vllm-project/vllm/pull/30356
- 状态/时间: merged / 2026-01-05
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`；关联提交 `276e03b92c16`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+33/-1，可读 patch 51 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[CI][DeepSeek] Add nightly DeepSeek R1 `lm_eval` tests on H200」；模型线: DeepSeek V3/R1；类别: 文档/测试/CI；主要 diff: `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`；技术摘要: 覆盖「[CI][DeepSeek] Add nightly DeepSeek R1 `lm_eval` tests on H200」；主要实现面是 `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11；`tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11。
- 代码 diff 细节:
  - `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11
  - `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11
- 关键代码摘录:

```diff
diff -- tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml
@@ -0,0 +1,11 @@
+model_name: "deepseek-ai/DeepSeek-R1"
+accuracy_threshold: 0.95
+num_questions: 1319
+num_fewshot: 5
+startup_max_wait_seconds: 1200
+server_args: >-
diff -- tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml
@@ -0,0 +1,11 @@
+model_name: "deepseek-ai/DeepSeek-R1"
+accuracy_threshold: 0.95
+num_questions: 1319
+num_fewshot: 5
+startup_max_wait_seconds: 1200
+server_args: >-
```

- 已读文件:
  - tests: `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` added +11/-0; `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` added +11/-0
- 验证与风险: diff 自带测试面 `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`, `tests/evals/gsm8k/configs/models-h200.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #31160 - [Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2

- 链接: https://github.com/vllm-project/vllm/pull/31160
- 状态/时间: merged / 2025-12-24
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `76e6a951925b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-3，可读 patch 18 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -878,11 +878,14 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -878,11 +878,14 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -878,11 +878,14 @@ def forward(
-        # `rotary_emb` is shape-preserving; `q_pe` is already
-        # [num_tokens, n_head, rope_dim].
+        # Note: RoPE (NeoX) can introduce extra leading dimensions during compilation
+        # so we need to reshape back to token-flattened shapes
+        q_pe = q_pe.reshape(-1, self.n_head, self.rope_dim)
+        k_pe = k_pe.reshape(-1, 1, self.rope_dim)
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #31046 - [Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2

- 链接: https://github.com/vllm-project/vllm/pull/31046
- 状态/时间: merged / 2025-12-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `4cf9429897c1`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-2，可读 patch 14 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -878,8 +878,11 @@ def forward(; symbols: forward，涉及 `forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -878,8 +878,11 @@ def forward(; symbols: forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -878,8 +878,11 @@ def forward(
-        q = torch.cat([q_pe.squeeze(0), q_nope], dim=-1)
-        k = torch.cat([k_pe.squeeze((0, 2)), k_nope], dim=-1)
+        # `rotary_emb` is shape-preserving; `q_pe` is already
+        # [num_tokens, n_head, rope_dim].
+        q = torch.cat([q_pe, q_nope], dim=-1)
+        # `k_pe` is [num_tokens, 1, rope_dim] (MQA).
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +5/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #30841 - [Bugfix] deepseek-V3.2 self.weights_proj has no bias

- 链接: https://github.com/vllm-project/vllm/pull/30841
- 状态/时间: merged / 2025-12-17
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `84896fda22d3`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+5/-1，可读 patch 13 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] deepseek-V3.2 self.weights_proj has no bias」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bugfix] deepseek-V3.2 self.weights_proj has no bias」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -835,7 +835,11 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -835,7 +835,11 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -835,7 +835,11 @@ def __init__(
-            hidden_size, self.n_head, quant_config=None, prefix=f"{prefix}.weights_proj"
+            hidden_size,
+            self.n_head,
+            bias=False,
+            quant_config=None,
+            prefix=f"{prefix}.weights_proj",
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +5/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #27532 - [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2

- 链接: https://github.com/vllm-project/vllm/pull/27532
- 状态/时间: merged / 2025-12-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `3e41992fecdc`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 30 个文件，+1372/-256，可读 patch 2323 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +18/-19 (37 lines); hunks: -83,6 +83,7; -618,8 +619,15 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake，涉及 `sparse_attn_indexer, sparse_attn_indexer_fake`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +18/-19 (37 lines); hunks: -83,6 +83,7; -618,8 +619,15 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -83,6 +83,7 @@
+from vllm.v1.worker.workspace import current_workspace_manager
@@ -618,8 +619,15 @@ def sparse_attn_indexer(
+        # Reserve workspace for indexer during profiling run
+        current_workspace_manager().get_simultaneous(
+            ((total_seq_lens, head_dim), torch.float8_e4m3fn),
+            ((total_seq_lens, 4), torch.uint8),
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +18/-19
- 验证与风险: diff 自带测试面 `tests/conftest.py`, `tests/kernels/moe/test_batched_deepgemm.py`, `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #27568 - [DeepSeek v3.2] Make top-k work for any logit values.

- 链接: https://github.com/vllm-project/vllm/pull/27568
- 状态/时间: merged / 2025-12-08
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `184076c3fecf`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+629/-210，可读 patch 1067 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek v3.2] Make top-k work for any logit values.」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeek v3.2] Make top-k work for any logit values.」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -684,18 +684,18 @@ def sparse_attn_indexer(; -738,7 +738,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer，涉及 `sparse_attn_indexer`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -684,18 +684,18 @@ def sparse_attn_indexer(; -738,7 +738,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -684,18 +684,18 @@ def sparse_attn_indexer(
-            assert topk_tokens == 2048, "top_k_per_row assumes size 2048"
-            torch.ops._C.top_k_per_row(
+            torch.ops._C.top_k_per_row_prefill(
+                topk_tokens,
@@ -738,7 +738,6 @@ def sparse_attn_indexer(
-        assert topk_tokens == 2048, "top_k_per_row assumes size 2048"
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +3/-3
- 验证与风险: diff 自带测试面 `tests/kernels/test_top_k_per_row.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #29545 - [Bugfix] Fix DeepSeek R1 MTP weight loading

- 链接: https://github.com/vllm-project/vllm/pull/29545
- 状态/时间: merged / 2025-12-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_mtp.py`；关联提交 `51c57b51dd51`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+11/-0，可读 patch 30 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bugfix] Fix DeepSeek R1 MTP weight loading」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_mtp.py`；技术摘要: 覆盖「[Bugfix] Fix DeepSeek R1 MTP weight loading」；主要实现面是 `vllm/model_executor/models/deepseek_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_mtp.py` modified +11/-0 (11 lines); hunks: -346,11 +346,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -377,6 +382,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights，涉及 `load_weights`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_mtp.py` modified +11/-0 (11 lines); hunks: -346,11 +346,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -377,6 +382,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_mtp.py
@@ -346,11 +346,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                    is_expert_weight = False
+                        # Anyway, this is an expert weight and should not be
+                        # attempted to load as other weights later
+                        is_expert_weight = True
@@ -377,6 +382,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                        if is_expert_weight:
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_mtp.py` modified +11/-0
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_mtp.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26670 - [ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA

- 链接: https://github.com/vllm-project/vllm/pull/26670
- 状态/时间: merged / 2025-11-20
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `06c20c990464`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 9 个文件，+583/-15，可读 patch 700 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +18/-4 (22 lines); hunks: -591,6 +591,7 @@ def sparse_attn_indexer(; -630,7 +631,7 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake，涉及 `sparse_attn_indexer, sparse_attn_indexer_fake`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +18/-4 (22 lines); hunks: -591,6 +591,7 @@ def sparse_attn_indexer(; -630,7 +631,7 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -591,6 +591,7 @@ def sparse_attn_indexer(
+    fp8_dtype = current_platform.fp8_dtype()
@@ -630,7 +631,7 @@ def sparse_attn_indexer(
-                dtype=torch.float8_e4m3fn,
+                dtype=fp8_dtype,
@@ -644,7 +645,12 @@ def sparse_attn_indexer(
-            logits = fp8_mqa_logits(
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +18/-4
- 验证与风险: runtime 路径改动集中在 `vllm/attention/ops/rocm_aiter_mla_sparse.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/platforms/rocm.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #28968 - [DeepSeek] Fix DeepSeek V3.2 Rope Embedding

- 链接: https://github.com/vllm-project/vllm/pull/28968
- 状态/时间: merged / 2025-11-19
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `88f5b19f0bc6`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 2 个文件，+17/-3，可读 patch 69 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[DeepSeek] Fix DeepSeek V3.2 Rope Embedding」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[DeepSeek] Fix DeepSeek V3.2 Rope Embedding」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -846,8 +846,8 @@ def forward(; -1000,6 +1000,14 @@ def __init__(; symbols: forward, __init__，涉及 `forward, __init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -846,8 +846,8 @@ def forward(; -1000,6 +1000,14 @@ def __init__(; symbols: forward, __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -846,8 +846,8 @@ def forward(
-        q = torch.cat([q_pe, q_nope], dim=-1)
-        k = torch.cat([k_pe.squeeze(1), k_nope], dim=-1)
+        q = torch.cat([q_pe.squeeze(0), q_nope], dim=-1)
+        k = torch.cat([k_pe.squeeze((0, 2)), k_nope], dim=-1)
@@ -1000,6 +1000,14 @@ def __init__(
+            self.indexer_rope_emb = get_rope(
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #26465 - [Deepseek v3.2] Remove extra logics in indexer

- 链接: https://github.com/vllm-project/vllm/pull/26465
- 状态/时间: merged / 2025-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `09a7e6f6179b`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+141/-40，可读 patch 272 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Deepseek v3.2] Remove extra logics in indexer」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek v3.2] Remove extra logics in indexer」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +11/-26 (37 lines); hunks: -574,9 +574,9 @@ def sparse_attn_indexer(; -586,9 +586,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer，涉及 `sparse_attn_indexer`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +11/-26 (37 lines); hunks: -574,9 +574,9 @@ def sparse_attn_indexer(; -586,9 +586,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -574,9 +574,9 @@ def sparse_attn_indexer(
-            topk_indices = torch.empty(
-                num_rows, topk_tokens, dtype=torch.int32, device=logits.device
-            )
+            topk_indices = topk_indices_buffer[
+                chunk.token_start : chunk.token_end, :topk_tokens
+            ]
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +11/-26
- 验证与风险: diff 自带测试面 `tests/kernels/test_top_k_per_row.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26763 - [Deepseek v3.2] Optimize top_k_per_row

- 链接: https://github.com/vllm-project/vllm/pull/26763
- 状态/时间: merged / 2025-10-21
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `80e94529845d`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 5 个文件，+13/-49，可读 patch 203 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Deepseek v3.2] Optimize top_k_per_row」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek v3.2] Optimize top_k_per_row」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +0/-8 (8 lines); hunks: -577,15 +577,11 @@ def sparse_attn_indexer(; -642,15 +638,11 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer，涉及 `sparse_attn_indexer`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +0/-8 (8 lines); hunks: -577,15 +577,11 @@ def sparse_attn_indexer(; -642,15 +638,11 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -577,15 +577,11 @@ def sparse_attn_indexer(
-            topk_values = torch.empty(
-                num_rows, topk_tokens, dtype=logits.dtype, device=logits.device
-            )
-                topk_values,
@@ -642,15 +638,11 @@ def sparse_attn_indexer(
-        topk_values = torch.empty(
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +0/-8
- 验证与风险: diff 自带测试面 `tests/kernels/test_top_k_per_row.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #26456 - [Deepseek-V3.2][Kernel] Integrate cuda indexer k cache gather

- 链接: https://github.com/vllm-project/vllm/pull/26456
- 状态/时间: merged / 2025-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `f5ed68ef63d0`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-68，可读 patch 104 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Deepseek-V3.2][Kernel] Integrate cuda indexer k cache gather」；模型线: DeepSeek V3/R1；类别: 性能/后端优化；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek-V3.2][Kernel] Integrate cuda indexer k cache gather」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +6/-68 (74 lines); hunks: -75,7 +75,7; -483,69 +483,6 @@ def get_attn_backend(self) -> AttentionBackend:; symbols: get_attn_backend, cp_gather_indexer_k_quant_cache, sparse_attn_indexer，涉及 `get_attn_backend, cp_gather_indexer_k_quant_cache, sparse_attn_indexer`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-68 (74 lines); hunks: -75,7 +75,7; -483,69 +483,6 @@ def get_attn_backend(self) -> AttentionBackend:; symbols: get_attn_backend, cp_gather_indexer_k_quant_cache, sparse_attn_indexer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -75,7 +75,7 @@
-from vllm.utils import cdiv, direct_register_custom_op
+from vllm.utils import direct_register_custom_op
@@ -483,69 +483,6 @@ def get_attn_backend(self) -> AttentionBackend:
-@torch.inference_mode()
-def cp_gather_indexer_k_quant_cache(
-    kv_cache,  # [num_blocks, block_size, head_dim + 1]
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-68
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #25589 - [Model] Add DeepSeek-V3.1 reasoning parser (split from PR #24972)

- 链接: https://github.com/vllm-project/vllm/pull/25589
- 状态/时间: merged / 2025-10-15
- 反查来源: `git log --name-only -- <model-files>` 反查到 `tests/reasoning/test_deepseekv3_reasoning_parser.py`；关联提交 `85a65e7f51ad`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 6 个文件，+215/-3，可读 patch 269 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Model] Add DeepSeek-V3.1 reasoning parser (split from PR #24972)」；模型线: DeepSeek V3/R1；类别: 文档/测试/CI；主要 diff: `tests/reasoning/test_deepseekv3_reasoning_parser.py`；技术摘要: 覆盖「[Model] Add DeepSeek-V3.1 reasoning parser (split from PR #24972)」；主要实现面是 `tests/reasoning/test_deepseekv3_reasoning_parser.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +76/-0 (76 lines); hunks: -0,0 +1,76; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic，涉及 `tokenizer, test_parser_selection, test_identity_reasoning_parser_basic`。
- 代码 diff 细节:
  - `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +76/-0 (76 lines); hunks: -0,0 +1,76; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic
- 关键代码摘录:

```diff
diff -- tests/reasoning/test_deepseekv3_reasoning_parser.py
@@ -0,0 +1,76 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+from transformers import AutoTokenizer
+from vllm.entrypoints.openai.protocol import ChatCompletionRequest, DeltaMessage
+from vllm.reasoning import (
```

- 已读文件:
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +76/-0
- 验证与风险: diff 自带测试面 `tests/reasoning/test_deepseekv3_reasoning_parser.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25999 - [Deepseek v3.2] Support indexer prefill chunking

- 链接: https://github.com/vllm-project/vllm/pull/25999
- 状态/时间: merged / 2025-10-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `1e50f1be7058`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+149/-79，可读 patch 324 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Deepseek v3.2] Support indexer prefill chunking」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Deepseek v3.2] Support indexer prefill chunking」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +37/-38 (75 lines); hunks: -583,44 +583,43 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer，涉及 `sparse_attn_indexer`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +37/-38 (75 lines); hunks: -583,44 +583,43 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -583,44 +583,43 @@ def sparse_attn_indexer(
-        num_prefills = attn_metadata.num_prefills
-        k_fp8 = torch.empty([prefill_metadata.total_seq_lens, head_dim],
-                            device=k.device,
-                            dtype=torch.float8_e4m3fn)
-        k_scale = torch.empty([prefill_metadata.total_seq_lens, 1],
-                              device=k.device,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +37/-38
- 验证与风险: diff 自带测试面 `tests/v1/attention/test_sparse_mla_backends.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #25896 - [New Model] DeepSeek-V3.2 (Rebased to Main)

- 链接: https://github.com/vllm-project/vllm/pull/25896
- 状态/时间: merged / 2025-09-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`；关联提交 `fa7e254a7f3e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 71 个文件，+3918/-221，可读 patch 5400 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[New Model] DeepSeek-V3.2 (Rebased to Main)」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`；技术摘要: 覆盖「[New Model] DeepSeek-V3.2 (Rebased to Main)」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +445/-4 (449 lines); hunks: -33,36 +33,57; -276,6 +297,7 @@ class DeepseekV2Attention(nn.Module):; symbols: DeepseekV2MLP, DeepseekV2Attention, __init__，涉及 `DeepseekV2MLP, DeepseekV2Attention, __init__`；`vllm/model_executor/models/deepseek_mtp.py` modified +13/-1 (14 lines); hunks: -53,8 +53,20 @@ def __init__(self, vllm_config: VllmConfig, prefix: str) -> N...; symbols: __init__, forward，涉及 `__init__, forward`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +445/-4 (449 lines); hunks: -33,36 +33,57; -276,6 +297,7 @@ class DeepseekV2Attention(nn.Module):; symbols: DeepseekV2MLP, DeepseekV2Attention, __init__
  - `vllm/model_executor/models/deepseek_mtp.py` modified +13/-1 (14 lines); hunks: -53,8 +53,20 @@ def __init__(self, vllm_config: VllmConfig, prefix: str) -> N...; symbols: __init__, forward
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -33,36 +33,57 @@
+from vllm.attention.backends.abstract import AttentionBackend
+from vllm.attention.ops.common import pack_seq_triton, unpack_seq_triton
-from vllm.config import CacheConfig, ParallelConfig, VllmConfig
+from vllm.config import (CacheConfig, ParallelConfig, VllmConfig,
+                         get_current_vllm_config)
+from vllm.forward_context import get_forward_context
diff -- vllm/model_executor/models/deepseek_mtp.py
@@ -53,8 +53,20 @@ def __init__(self, vllm_config: VllmConfig, prefix: str) -> None:
+        self.is_v32 = hasattr(config, "index_topk")
+        if self.is_v32:
+            topk_tokens = config.index_topk
+            topk_indices_buffer = torch.empty(
+                vllm_config.scheduler_config.max_num_batched_tokens,
+                topk_tokens,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +445/-4; `vllm/model_executor/models/deepseek_mtp.py` modified +13/-1
- 验证与风险: diff 自带测试面 `tests/compile/test_fusion_attn.py`, `tests/kernels/attention/test_cache.py`, `tests/kernels/attention/test_deepgemm_attention.py`, `tests/kernels/attention/test_flashmla.py`；如果继续改同一模型，优先复跑这些测试并补一个最小 launch/accuracy smoke。

### PR #24119 - [Bug] R1 Accuracy: Fix `routed_scaling_factor` Double Mul Issue

- 链接: https://github.com/vllm-project/vllm/pull/24119
- 状态/时间: merged / 2025-09-02
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `930a24144c07`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+2/-1，可读 patch 10 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Bug] R1 Accuracy: Fix `routed_scaling_factor` Double Mul Issue」；模型线: DeepSeek V3/R1；类别: 缺陷修复；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「[Bug] R1 Accuracy: Fix `routed_scaling_factor` Double Mul Issue」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -160,7 +160,8 @@ def __init__(; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -160,7 +160,8 @@ def __init__(; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -160,7 +160,8 @@ def __init__(
-            routed_scaling_factor=self.routed_scaling_factor,
+            # we do scaling outside, set factor to 1.0 to avoid double mul
+            routed_scaling_factor=1.0,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-1
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23971 - Add LoRA support for DeepSeek models (V2, V3, R1-0528)

- 链接: https://github.com/vllm-project/vllm/pull/23971
- 状态/时间: merged / 2025-08-30
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `379ea2823a75`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 3 个文件，+12/-7，可读 patch 54 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Add LoRA support for DeepSeek models (V2, V3, R1-0528)」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「Add LoRA support for DeepSeek models (V2, V3, R1-0528)」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +3/-2 (5 lines); hunks: -56,7 +56,7; -727,7 +727,8 @@ def forward(; symbols: forward, DeepseekV2ForCausalLM，涉及 `forward, DeepseekV2ForCausalLM`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +3/-2 (5 lines); hunks: -56,7 +56,7; -727,7 +727,8 @@ def forward(; symbols: forward, DeepseekV2ForCausalLM
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -56,7 +56,7 @@
-from .interfaces import MixtureOfExperts, SupportsPP
+from .interfaces import MixtureOfExperts, SupportsLoRA, SupportsPP
@@ -727,7 +727,8 @@ def forward(
-class DeepseekV2ForCausalLM(nn.Module, SupportsPP, MixtureOfExperts):
+class DeepseekV2ForCausalLM(nn.Module, SupportsPP, MixtureOfExperts,
+                            SupportsLoRA):
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +3/-2
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #23454 - Support DeepSeek-V3.1 tool call

- 链接: https://github.com/vllm-project/vllm/pull/23454
- 状态/时间: merged / 2025-08-23
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/tool_chat_template_deepseekv31.jinja`；关联提交 `b8f17f5d980e`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+468/-0，可读 patch 491 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「Support DeepSeek-V3.1 tool call」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `examples/tool_chat_template_deepseekv31.jinja`；技术摘要: 覆盖「Support DeepSeek-V3.1 tool call」；主要实现面是 `examples/tool_chat_template_deepseekv31.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91。
- 代码 diff 细节:
  - `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- 关键代码摘录:

```diff
diff -- examples/tool_chat_template_deepseekv31.jinja
@@ -0,0 +1,91 @@
+{% if not add_generation_prompt is defined %}
+  {% set add_generation_prompt = false %}
+{% endif %}
+{% if not thinking is defined %}
+  {% set thinking = false %}
+{% endif %}
```

- 已读文件:
  - docs: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0
- 验证与风险: runtime 路径改动集中在 `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv31_tool_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #17784 - [Feature] Support DeepSeekV3 Function Call

- 链接: https://github.com/vllm-project/vllm/pull/17784
- 状态/时间: merged / 2025-05-12
- 反查来源: `git log --name-only -- <model-files>` 反查到 `examples/tool_chat_template_deepseekv3.jinja`；关联提交 `3a5ea7512926`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 4 个文件，+473/-1，可读 patch 495 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「[Feature] Support DeepSeekV3 Function Call」；模型线: DeepSeek V3/R1；类别: 模型支持/运行时入口；主要 diff: `examples/tool_chat_template_deepseekv3.jinja`；技术摘要: 覆盖「[Feature] Support DeepSeekV3 Function Call」；主要实现面是 `examples/tool_chat_template_deepseekv3.jinja`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `examples/tool_chat_template_deepseekv3.jinja` added +96/-0 (96 lines); hunks: -0,0 +1,96。
- 代码 diff 细节:
  - `examples/tool_chat_template_deepseekv3.jinja` added +96/-0 (96 lines); hunks: -0,0 +1,96
- 关键代码摘录:

```diff
diff -- examples/tool_chat_template_deepseekv3.jinja
@@ -0,0 +1,96 @@
+{% if not add_generation_prompt is defined %}
+    {% set add_generation_prompt = false %}
+{% endif %}
+{% set ns = namespace(is_first=false, is_tool=false, is_output_first=true, system_prompt='', is_first_sp=true, is_last_user=false) %}
+{%- for message in messages %}
+    {%- if message['role'] == 'system' %}
```

- 已读文件:
  - docs: `examples/tool_chat_template_deepseekv3.jinja` added +96/-0
- 验证与风险: runtime 路径改动集中在 `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv3_tool_parser.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

### PR #13833 - DeepSeek V2/V3/R1 only place `lm_head` on last pp rank

- 链接: https://github.com/vllm-project/vllm/pull/13833
- 状态/时间: merged / 2025-02-26
- 反查来源: `git log --name-only -- <model-files>` 反查到 `vllm/model_executor/models/deepseek_v2.py`；关联提交 `24679788ed38`
- 代码 diff 已读范围: GitHub Pull Request files API 返回 1 个文件，+6/-3，可读 patch 16 行；本卡优先审计模型相关文件和高变更量文件。
- 动机: 标题「DeepSeek V2/V3/R1 only place `lm_head` on last pp rank」；模型线: DeepSeek V3/R1；类别: 模型实现调整；主要 diff: `vllm/model_executor/models/deepseek_v2.py`；技术摘要: 覆盖「DeepSeek V2/V3/R1 only place `lm_head` on last pp rank」；主要实现面是 `vllm/model_executor/models/deepseek_v2.py`。下方保留文件级证据、代码摘录和验证风险。
- 实现要点: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -636,9 +636,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__，涉及 `__init__`。
- 代码 diff 细节:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -636,9 +636,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- 关键代码摘录:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -636,9 +636,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-        self.lm_head = ParallelLMHead(config.vocab_size,
-                                      config.hidden_size,
-                                      quant_config=quant_config)
+        if get_pp_group().is_last_rank:
+            self.lm_head = ParallelLMHead(config.vocab_size,
+                                          config.hidden_size,
```

- 已读文件:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3
- 验证与风险: runtime 路径改动集中在 `vllm/model_executor/models/deepseek_v2.py`；风险点是权重加载、并行切分、attention/MoE 后端和 parser 输出，需要至少做一次真实 checkpoint 或等价 mock smoke。

## 补漏结论

- 验收规则: 每个 PR 卡片必须保留反查来源、diff 范围、实现要点、代码摘录、已读文件和验证风险。
- 如果新模型文件落在当前过滤规则之外，先补文件过滤规则，再重新执行本轮 `git log --name-only -- <model-files>` 追溯。
