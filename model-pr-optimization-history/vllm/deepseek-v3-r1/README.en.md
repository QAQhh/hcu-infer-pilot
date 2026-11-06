# vllm DeepSeek V3/R1 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `examples/ray_serving/elastic_ep/serve_deepseek_v2.sh` | no direct PR-number commit |
| `examples/tool_chat_template_deepseekv3.jinja` | [#17784](https://github.com/vllm-project/vllm/pull/17784) |
| `examples/tool_chat_template_deepseekv31.jinja` | [#23454](https://github.com/vllm-project/vllm/pull/23454) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` | [#30356](https://github.com/vllm-project/vllm/pull/30356) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` | [#59666](https://github.com/vllm-project/vllm/pull/59666) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` | [#30356](https://github.com/vllm-project/vllm/pull/30356) |
| `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` | [#59666](https://github.com/vllm-project/vllm/pull/59666) |
| `tests/evals/gsm8k/configs/models-h200-deepseek-r1-dp.txt` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/models-h200-deepseek-r1-tp.txt` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/models-h200-deepseek-v32-dp.txt` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/models-h200-deepseek-v32-tp.txt` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-r1-dp.txt` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-r1-tp.txt` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-v32-dp.txt` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/models-mi355-deepseek-v32-tp.txt` | no direct PR-number commit |
| `tests/reasoning/test_deepseekv3_reasoning_parser.py` | [#24972](https://github.com/vllm-project/vllm/pull/24972), [#25589](https://github.com/vllm-project/vllm/pull/25589), [#58626](https://github.com/vllm-project/vllm/pull/58626) |
| `tests/tool_parsers/test_deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `tests/tool_parsers/test_deepseekv32_tool_parser.py` | [#33703](https://github.com/vllm-project/vllm/pull/33703), [#36056](https://github.com/vllm-project/vllm/pull/36056), [#41198](https://github.com/vllm-project/vllm/pull/41198), [#41801](https://github.com/vllm-project/vllm/pull/41801), [#43019](https://github.com/vllm-project/vllm/pull/43019), [#43255](https://github.com/vllm-project/vllm/pull/43255) |
| `tests/tool_parsers/test_deepseekv3_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `vllm/model_executor/models/deepseek_mtp.py` | [#25896](https://github.com/vllm-project/vllm/pull/25896), [#29545](https://github.com/vllm-project/vllm/pull/29545), [#38684](https://github.com/vllm-project/vllm/pull/38684), [#38870](https://github.com/vllm-project/vllm/pull/38870), [#48036](https://github.com/vllm-project/vllm/pull/48036) |
| `vllm/model_executor/models/deepseek_v2.py` | [#13833](https://github.com/vllm-project/vllm/pull/13833), [#23971](https://github.com/vllm-project/vllm/pull/23971), [#24119](https://github.com/vllm-project/vllm/pull/24119), [#25896](https://github.com/vllm-project/vllm/pull/25896), [#25999](https://github.com/vllm-project/vllm/pull/25999), [#26456](https://github.com/vllm-project/vllm/pull/26456), [#26465](https://github.com/vllm-project/vllm/pull/26465), [#26670](https://github.com/vllm-project/vllm/pull/26670), [#26763](https://github.com/vllm-project/vllm/pull/26763), [#27532](https://github.com/vllm-project/vllm/pull/27532), [#27568](https://github.com/vllm-project/vllm/pull/27568), [#28968](https://github.com/vllm-project/vllm/pull/28968), ... (30 total) |
| `vllm/reasoning/deepseek_r1_reasoning_parser.py` | no direct PR-number commit |
| `vllm/tool_parsers/deepseekv31_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |
| `vllm/tool_parsers/deepseekv32_engine_tool_parser.py` | no direct PR-number commit |
| `vllm/tool_parsers/deepseekv3_tool_parser.py` | [#60362](https://github.com/vllm-project/vllm/pull/60362) |

## PR Coverage Summary

- Git-traced PRs: 46
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 46

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
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

## Per-PR Diff Audit Cards

### PR #60362 - [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers

- Link: https://github.com/vllm-project/vllm/pull/60362
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv3_tool_parser.py`; associated commits `e347836d68be`
- Diff scope read: GitHub Pull Request files API returned 4 files, +55/-4, 108 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`; technical summary: Covers "[Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers"; the main implementation surface is `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv3_tool_parser.py` modified +27/-0 (27 lines); hunks: -1,6 +1,7; -92,6 +93,32 @@ def test_config(self) -> ToolParserTestConfig:; symbols: test_config, test_multiline_json_arguments, test_preserves_text_after_tool_call, touching `test_config, test_multiline_json_arguments, test_preserves_text_after_tool_call`; `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments, touching `test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments`; `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__, touching `__init__`; `vllm/tool_parsers/deepseekv3_tool_parser.py` modified +3/-2 (5 lines); hunks: -46,12 +46,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv3_tool_parser.py` modified +27/-0 (27 lines); hunks: -1,6 +1,7; -92,6 +93,32 @@ def test_config(self) -> ToolParserTestConfig:; symbols: test_config, test_multiline_json_arguments, test_preserves_text_after_tool_call
  - `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0 (22 lines); hunks: -1,8 +1,11; -59,3 +62,22 @@ def test_extract_tool_calls_with_multiple_tools(parser):; symbols: test_extract_tool_calls_with_multiple_tools, test_extract_tool_calls_with_multiline_arguments
  - `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2 (5 lines); hunks: -43,12 +43,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__
  - `vllm/tool_parsers/deepseekv3_tool_parser.py` modified +3/-2 (5 lines); hunks: -46,12 +46,13 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[Too...; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv3_tool_parser.py` modified +27/-0; `tests/tool_parsers/test_deepseekv31_tool_parser.py` modified +22/-0
  - runtime: `vllm/tool_parsers/deepseekv31_tool_parser.py` modified +3/-2; `vllm/tool_parsers/deepseekv3_tool_parser.py` modified +3/-2
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_deepseekv3_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59666 - [ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s

- Link: https://github.com/vllm-project/vllm/pull/59666
- Status/date: merged / 2026-10-01
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`; associated commits `d2125ea68178`
- Diff scope read: GitHub Pull Request files API returned 2 files, +2/-2, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s"; model line: DeepSeek V3/R1; category: docs/tests/CI; main diff: `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`; technical summary: Covers "[ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s"; the main implementation surface is `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"; `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1".
- Code diff details:
  - `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"
  - `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` modified +1/-1 (2 lines); hunks: -2,7 +2,7 @@ model_name: "deepseek-ai/DeepSeek-R1"
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml` modified +1/-1; `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58626 - [Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers

- Link: https://github.com/vllm-project/vllm/pull/58626
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `tests/reasoning/test_deepseekv3_reasoning_parser.py`; associated commits `064bc747ab42`
- Diff scope read: GitHub Pull Request files API returned 6 files, +136/-3, 195 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/reasoning/test_deepseekv3_reasoning_parser.py`; technical summary: Covers "[Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers"; the main implementation surface is `tests/reasoning/test_deepseekv3_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/reasoning/test_deepseekv3_reasoning_parser.py` modified +11/-0 (11 lines); hunks: -87,3 +87,14 @@ def test_identity_reasoning_parser_basic(tokenizer):; symbols: test_identity_reasoning_parser_basic, test_count_reasoning_tokens_delegates, touching `test_identity_reasoning_parser_basic, test_count_reasoning_tokens_delegates`.
- Code diff details:
  - `tests/reasoning/test_deepseekv3_reasoning_parser.py` modified +11/-0 (11 lines); hunks: -87,3 +87,14 @@ def test_identity_reasoning_parser_basic(tokenizer):; symbols: test_identity_reasoning_parser_basic, test_count_reasoning_tokens_delegates
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py` modified +11/-0
- Risk and verification: The diff ships test coverage in `tests/parser/test_harmony.py`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `tests/reasoning/test_step3_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #51915 - [ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness

- Link: https://github.com/vllm-project/vllm/pull/51915
- Status/date: merged / 2026-09-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `1c0eee919db3`
- Diff scope read: GitHub Pull Request files API returned 8 files, +319/-212, 1215 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -665,6 +665,11 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVC...; symbols: get_kv_cache_spec, forward, uses_shuffled_layout, get_attn_backend, touching `get_kv_cache_spec, forward, uses_shuffled_layout`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +5/-0 (5 lines); hunks: -665,6 +665,11 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVC...; symbols: get_kv_cache_spec, forward, uses_shuffled_layout, get_attn_backend
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -665,6 +665,11 @@ def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
+    @property
+    def uses_shuffled_layout(self) -> bool:
+        """Whether this cache's reader expects the shuffled value layout."""
+        return False
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +5/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_fused_deepseek_v32_norm_rope.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45964 - [Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5)

- Link: https://github.com/vllm-project/vllm/pull/45964
- Status/date: merged / 2026-07-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `2396a611085d`
- Diff scope read: GitHub Pull Request files API returned 6 files, +157/-15, 443 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5)"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5)"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -33,6 +33,7; -56,6 +57,7; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -33,6 +33,7; -56,6 +57,7; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_mla_backends.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #48036 - [CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel

- Link: https://github.com/vllm-project/vllm/pull/48036
- Status/date: merged / 2026-07-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_mtp.py`; associated commits `1ff9429655f0`
- Diff scope read: GitHub Pull Request files API returned 3 files, +34/-3, 79 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_mtp.py`; technical summary: Covers "[CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel"; the main implementation surface is `vllm/model_executor/models/deepseek_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_mtp.py` modified +24/-0 (24 lines); hunks: -10,6 +10,7; -40,6 +41,24; symbols: _restore_full_token_layout_if_needed, SharedHead, __init__, forward, touching `_restore_full_token_layout_if_needed, SharedHead, __init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_mtp.py` modified +24/-0 (24 lines); hunks: -10,6 +10,7; -40,6 +41,24; symbols: _restore_full_token_layout_if_needed, SharedHead, __init__, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_mtp.py` modified +24/-0
- Risk and verification: Runtime changes concentrate in `vllm/config/parallel.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/deepseek_v32/nvidia/mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #46600 - [Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers

- Link: https://github.com/vllm-project/vllm/pull/46600
- Status/date: merged / 2026-06-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `6eb63a1da699`
- Diff scope read: GitHub Pull Request files API returned 1 files, +10/-0, 24 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +10/-0 (10 lines); hunks: -1438,6 +1438,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; -1446,6 +1451,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +10/-0 (10 lines); hunks: -1438,6 +1438,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; -1446,6 +1451,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +10/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #42982 - [ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts)

- Link: https://github.com/vllm-project/vllm/pull/42982
- Status/date: merged / 2026-05-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `0b56815a24f4`
- Diff scope read: GitHub Pull Request files API returned 2 files, +59/-29, 125 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts)"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts)"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +2/-4 (6 lines); hunks: -304,10 +304,8 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-4 (6 lines); hunks: -304,10 +304,8 @@ def __init__(; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-4
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #43255 - [CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers

- Link: https://github.com/vllm-project/vllm/pull/43255
- Status/date: merged / 2026-05-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv32_tool_parser.py`; associated commits `63ea11709bd9`
- Diff scope read: GitHub Pull Request files API returned 2 files, +186/-0, 204 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`; technical summary: Covers "[CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers"; the main implementation surface is `tests/tool_parsers/test_deepseekv32_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +137/-0 (137 lines); hunks: -221,6 +221,99 @@ def test_string_attr_false_allows_schema_conversion(self):; -581,6 +674,50 @@ def test_string_attr_true_preserves_literal_in_streaming(se...; symbols: test_string_attr_false_allows_schema_conversion, test_composed_schema_converts_object_and_array_params, test_string_attr_true_preserves_literal_for_composed_schema, test_arguments_wrapper_repaired, touching `test_string_attr_false_allows_schema_conversion, test_composed_schema_converts_object_and_array_params, test_string_attr_true_preserves_literal_for_composed_schema`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +137/-0 (137 lines); hunks: -221,6 +221,99 @@ def test_string_attr_false_allows_schema_conversion(self):; -581,6 +674,50 @@ def test_string_attr_true_preserves_literal_in_streaming(se...; symbols: test_string_attr_false_allows_schema_conversion, test_composed_schema_converts_object_and_array_params, test_string_attr_true_preserves_literal_for_composed_schema, test_arguments_wrapper_repaired
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +137/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #43019 - [Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser

- Link: https://github.com/vllm-project/vllm/pull/43019
- Status/date: merged / 2026-05-20
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv32_tool_parser.py`; associated commits `a10d69116cb2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +270/-285, 615 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`; technical summary: Covers "[Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser"; the main implementation surface is `tests/tool_parsers/test_deepseekv32_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +261/-233 (494 lines); hunks: -16,7 +16,6; -65,58 +64,6 @@ def build_tool_call(func_name: str, params: dict[str, str]) -...; symbols: build_tool_call, TestConvertParamValue, parser, test_null, touching `build_tool_call, TestConvertParamValue, parser`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +261/-233 (494 lines); hunks: -16,7 +16,6; -65,58 +64,6 @@ def build_tool_call(func_name: str, params: dict[str, str]) -...; symbols: build_tool_call, TestConvertParamValue, parser, test_null
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +261/-233
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv32_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41801 - [Bugfix] DeepSeekV32/v4: respect string='true|false' attribute andunwrap arguments/input wrapper

- Link: https://github.com/vllm-project/vllm/pull/41801
- Status/date: merged / 2026-05-06
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv32_tool_parser.py`; associated commits `95582868efd4`
- Diff scope read: GitHub Pull Request files API returned 3 files, +224/-10, 298 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] DeepSeekV32/v4: respect string='true|false' attribute andunwrap arguments/input wrapper"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`; technical summary: Covers "[Bugfix] DeepSeekV32/v4: respect string='true|false' attribute andunwrap arguments/input wrapper"; the main implementation surface is `tests/tool_parsers/test_deepseekv32_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +155/-2 (157 lines); hunks: -203,7 +203,14 @@ def test_type_conversion_in_non_streaming(self):; -212,6 +219,118 @@ def test_type_conversion_in_non_streaming(self):; symbols: test_type_conversion_in_non_streaming, test_string_attr_true_preserves_literal_despite_schema, test_string_attr_false_allows_schema_conversion, test_arguments_wrapper_repaired, touching `test_type_conversion_in_non_streaming, test_string_attr_true_preserves_literal_despite_schema, test_string_attr_false_allows_schema_conversion`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +155/-2 (157 lines); hunks: -203,7 +203,14 @@ def test_type_conversion_in_non_streaming(self):; -212,6 +219,118 @@ def test_type_conversion_in_non_streaming(self):; symbols: test_type_conversion_in_non_streaming, test_string_attr_true_preserves_literal_despite_schema, test_string_attr_false_allows_schema_conversion, test_arguments_wrapper_repaired
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +155/-2
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41217 - [ROCm][Deepseek] dsv3.2 further optimization

- Link: https://github.com/vllm-project/vllm/pull/41217
- Status/date: merged / 2026-05-01
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `bc635fad2389`
- Diff scope read: GitHub Pull Request files API returned 6 files, +293/-73, 605 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Deepseek] dsv3.2 further optimization"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[ROCm][Deepseek] dsv3.2 further optimization"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +38/-23 (61 lines); hunks: -674,30 +674,45 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +38/-23 (61 lines); hunks: -674,30 +674,45 @@ def forward(; symbols: forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +38/-23
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #41198 - [Bugfix] DSV32/V4 add missing type conversion for non-streaming tool calls

- Link: https://github.com/vllm-project/vllm/pull/41198
- Status/date: merged / 2026-04-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv32_tool_parser.py`; associated commits `762022cafb1a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +26/-1, 46 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] DSV32/V4 add missing type conversion for non-streaming tool calls"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`; technical summary: Covers "[Bugfix] DSV32/V4 add missing type conversion for non-streaming tool calls"; the main implementation surface is `tests/tool_parsers/test_deepseekv32_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +24/-0 (24 lines); hunks: -188,6 +188,30 @@ def test_multiple_tools(self, parser):; symbols: test_multiple_tools, test_type_conversion_in_non_streaming, touching `test_multiple_tools, test_type_conversion_in_non_streaming`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +24/-0 (24 lines); hunks: -188,6 +188,30 @@ def test_multiple_tools(self, parser):; symbols: test_multiple_tools, test_type_conversion_in_non_streaming
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +24/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv32_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37421 - [Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode

- Link: https://github.com/vllm-project/vllm/pull/37421
- Status/date: merged / 2026-04-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `b55d830ec782`
- Diff scope read: GitHub Pull Request files API returned 9 files, +2039/-483, 2698 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +6/-2 (8 lines); hunks: -67,7 +67,9; -1203,7 +1205,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-2 (8 lines); hunks: -67,7 +67,9; -1203,7 +1205,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/test_top_k_per_row.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #38870 - [Bugfix] Fix DSV32 weight loading

- Link: https://github.com/vllm-project/vllm/pull/38870
- Status/date: merged / 2026-04-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`; associated commits `8617f8676b5a`
- Diff scope read: GitHub Pull Request files API returned 2 files, +68/-27, 158 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix DSV32 weight loading"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`; technical summary: Covers "[Bugfix] Fix DSV32 weight loading"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +55/-24 (79 lines); hunks: -625,6 +625,11 @@ def __init__(; -639,18 +644,36 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`; `vllm/model_executor/models/deepseek_mtp.py` modified +13/-3 (16 lines); hunks: -184,11 +184,16 @@ class DeepSeekMTP(nn.Module, DeepseekV2MixtureOfExperts):; -241,11 +246,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: DeepSeekMTP, __init__, set_moe_parameters, load_weights, touching `DeepSeekMTP, __init__, set_moe_parameters`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +55/-24 (79 lines); hunks: -625,6 +625,11 @@ def __init__(; -639,18 +644,36 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/models/deepseek_mtp.py` modified +13/-3 (16 lines); hunks: -184,11 +184,16 @@ class DeepSeekMTP(nn.Module, DeepseekV2MixtureOfExperts):; -241,11 +246,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: DeepSeekMTP, __init__, set_moe_parameters, load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +55/-24; `vllm/model_executor/models/deepseek_mtp.py` modified +13/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #38684 - [Perf] DSV3.2 Indexer Fused Weights Projection

- Link: https://github.com/vllm-project/vllm/pull/38684
- Status/date: merged / 2026-04-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`; associated commits `5f96f9aff10f`
- Diff scope read: GitHub Pull Request files API returned 2 files, +25/-14, 79 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] DSV3.2 Indexer Fused Weights Projection"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`; technical summary: Covers "[Perf] DSV3.2 Indexer Fused Weights Projection"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +22/-14 (36 lines); hunks: -639,21 +639,19 @@ def __init__(; -694,7 +692,11 @@ def forward(; symbols: __init__, forward, load_weights, touching `__init__, forward, load_weights`; `vllm/model_executor/models/deepseek_mtp.py` modified +3/-0 (3 lines); hunks: -241,6 +241,9 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +22/-14 (36 lines); hunks: -639,21 +639,19 @@ def __init__(; -694,7 +692,11 @@ def forward(; symbols: __init__, forward, load_weights
  - `vllm/model_executor/models/deepseek_mtp.py` modified +3/-0 (3 lines); hunks: -241,6 +241,9 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +22/-14; `vllm/model_executor/models/deepseek_mtp.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #33703 - [Bugfix] Support multi-type params parsing for DeepSeek v3.2

- Link: https://github.com/vllm-project/vllm/pull/33703
- Status/date: merged / 2026-03-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv32_tool_parser.py`; associated commits `a6db99ba02ec`
- Diff scope read: GitHub Pull Request files API returned 2 files, +201/-18, 250 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Support multi-type params parsing for DeepSeek v3.2"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`; technical summary: Covers "[Bugfix] Support multi-type params parsing for DeepSeek v3.2"; the main implementation surface is `tests/tool_parsers/test_deepseekv32_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +181/-0 (181 lines); hunks: -11,6 +11,7; -474,3 +475,183 @@ def test_no_emission_while_incomplete(self, parser):; symbols: test_no_emission_while_incomplete, deepseekv32_tokenizer, parser, test_convert_param_value_single_types, touching `test_no_emission_while_incomplete, deepseekv32_tokenizer, parser`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +181/-0 (181 lines); hunks: -11,6 +11,7; -474,3 +475,183 @@ def test_no_emission_while_incomplete(self, parser):; symbols: test_no_emission_while_incomplete, deepseekv32_tokenizer, parser, test_convert_param_value_single_types
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` modified +181/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv32_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36056 - [Bugfix] Fix Deepseekv32 tool parser when stream interval > 1

- Link: https://github.com/vllm-project/vllm/pull/36056
- Status/date: merged / 2026-03-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_parsers/test_deepseekv32_tool_parser.py`; associated commits `be12afd284f3`
- Diff scope read: GitHub Pull Request files API returned 2 files, +622/-437, 1113 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Deepseekv32 tool parser when stream interval > 1"; model line: DeepSeek V3/R1; category: bug fix; main diff: `tests/tool_parsers/test_deepseekv32_tool_parser.py`; technical summary: Covers "[Bugfix] Fix Deepseekv32 tool parser when stream interval > 1"; the main implementation surface is `tests/tool_parsers/test_deepseekv32_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_deepseekv32_tool_parser.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: make_parser, make_tool_param, make_request, build_tool_call, touching `make_parser, make_tool_param, make_request`.
- Code diff details:
  - `tests/tool_parsers/test_deepseekv32_tool_parser.py` added +476/-0 (476 lines); hunks: -0,0 +1,476; symbols: make_parser, make_tool_param, make_request, build_tool_call
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/tool_parsers/test_deepseekv32_tool_parser.py` added +476/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_deepseekv32_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36247 - [Bugfix] Fix compressed-tensors quantization failure for DeepSeek-R1 on MI300x

- Link: https://github.com/vllm-project/vllm/pull/36247
- Status/date: merged / 2026-03-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `ee8a29511fc6`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix compressed-tensors quantization failure for DeepSeek-R1 on MI300x"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bugfix] Fix compressed-tensors quantization failure for DeepSeek-R1 on MI300x"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -756,7 +756,7 @@ def _min_latency_fused_qkv_a_proj_fake(; -848,7 +848,7 @@ def __init__(; symbols: _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj, DeepSeekV2FusedQkvAProjLinear, __init__, touching `_min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj, DeepSeekV2FusedQkvAProjLinear`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -756,7 +756,7 @@ def _min_latency_fused_qkv_a_proj_fake(; -848,7 +848,7 @@ def __init__(; symbols: _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj, DeepSeekV2FusedQkvAProjLinear, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -756,7 +756,7 @@ def _min_latency_fused_qkv_a_proj_fake(
-class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):
+class DeepSeekV2FusedQkvAProjLinear(MergedColumnParallelLinear):
@@ -848,7 +848,7 @@ def __init__(
-            self.fused_qkv_a_proj = DeepSeekV2FusedQkvAProj(
+            self.fused_qkv_a_proj = DeepSeekV2FusedQkvAProjLinear(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #35751 - [MoE][Perf] Wrap DSV3 QKVAProj GEMM in custom op for torch.compile

- Link: https://github.com/vllm-project/vllm/pull/35751
- Status/date: merged / 2026-03-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `9319044ee9a1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +41/-13, 75 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MoE][Perf] Wrap DSV3 QKVAProj GEMM in custom op for torch.compile"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[MoE][Perf] Wrap DSV3 QKVAProj GEMM in custom op for torch.compile"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +41/-13 (54 lines); hunks: -75,6 +75,7; -717,6 +718,44 @@ def forward(; symbols: forward, _min_latency_fused_qkv_a_proj_impl, _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj, touching `forward, _min_latency_fused_qkv_a_proj_impl, _min_latency_fused_qkv_a_proj_fake`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +41/-13 (54 lines); hunks: -75,6 +75,7; -717,6 +718,44 @@ def forward(; symbols: forward, _min_latency_fused_qkv_a_proj_impl, _min_latency_fused_qkv_a_proj_fake, DeepSeekV2FusedQkvAProj
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +41/-13
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34302 - [ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup)

- Link: https://github.com/vllm-project/vllm/pull/34302
- Status/date: merged / 2026-02-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `8435b2e04925`
- Diff scope read: GitHub Pull Request files API returned 9 files, +915/-3, 971 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup)"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup)"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +75/-2 (77 lines); hunks: -221,6 +221,73 @@ def forward(self, x):; -249,10 +316,9 @@ def __init__(; symbols: forward, DeepSeekV2Gate, __init__, set_out_dtype, touching `forward, DeepSeekV2Gate, __init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +75/-2 (77 lines); hunks: -221,6 +221,73 @@ def forward(self, x):; -249,10 +316,9 @@ def __init__(; symbols: forward, DeepSeekV2Gate, __init__, set_out_dtype
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +75/-2
- Risk and verification: Runtime changes concentrate in `vllm/_custom_ops.py`, `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34876 - [Bug] Fix DeepSeek V3 weight loading caused by incorrect prefix

- Link: https://github.com/vllm-project/vllm/pull/34876
- Status/date: merged / 2026-02-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `7f51e9386470`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug] Fix DeepSeek V3 weight loading caused by incorrect prefix"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bug] Fix DeepSeek V3 weight loading caused by incorrect prefix"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -716,7 +716,7 @@ class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):; -726,7 +726,7 @@ def __init__(; symbols: DeepSeekV2FusedQkvAProj, __init__, touching `DeepSeekV2FusedQkvAProj, __init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-2 (4 lines); hunks: -716,7 +716,7 @@ class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):; -726,7 +726,7 @@ def __init__(; symbols: DeepSeekV2FusedQkvAProj, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -716,7 +716,7 @@ class DeepSeekV2FusedQkvAProj(MergedColumnParallelLinear):
-        output_size: int,
+        output_size: list[int],
@@ -726,7 +726,7 @@ def __init__(
-            prefix=f"{prefix}.kv_a_proj_with_mqa",
+            prefix=prefix,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34758 - [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup)

- Link: https://github.com/vllm-project/vllm/pull/34758
- Status/date: merged / 2026-02-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `6874638bc443`
- Diff scope read: GitHub Pull Request files API returned 7 files, +855/-3, 917 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup)"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup)"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +60/-3 (63 lines); hunks: -32,6 +32,7; -711,6 +712,64 @@ def forward(; symbols: forward, DeepSeekV2FusedQkvAProj, __init__, DeepseekV2MLAAttention, touching `forward, DeepSeekV2FusedQkvAProj, __init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +60/-3 (63 lines); hunks: -32,6 +32,7; -711,6 +712,64 @@ def forward(; symbols: forward, DeepSeekV2FusedQkvAProj, __init__, DeepseekV2MLAAttention
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +60/-3
- Risk and verification: Runtime changes concentrate in `vllm/_custom_ops.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24972 - [Model] Deepseek-V3.1 reasoning parser

- Link: https://github.com/vllm-project/vllm/pull/24972
- Status/date: closed / 2026-02-07
- Trace source: `git log --name-only -- <model-files>` found it through `tests/reasoning/test_deepseekv3_reasoning_parser.py`; associated commits `85a65e7f51ad`
- Diff scope read: GitHub Pull Request files API returned 15 files, +214/-11, 330 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Deepseek-V3.1 reasoning parser"; model line: DeepSeek V3/R1; category: docs/tests/CI; main diff: `tests/reasoning/test_deepseekv3_reasoning_parser.py`; technical summary: Covers "[Model] Deepseek-V3.1 reasoning parser"; the main implementation surface is `tests/reasoning/test_deepseekv3_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +73/-0 (73 lines); hunks: -0,0 +1,73; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic, touching `tokenizer, test_parser_selection, test_identity_reasoning_parser_basic`.
- Code diff details:
  - `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +73/-0 (73 lines); hunks: -0,0 +1,73; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +73/-0
- Risk and verification: The diff ships test coverage in `tests/reasoning/test_deepseekv3_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29287 - [ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp

- Link: https://github.com/vllm-project/vllm/pull/29287
- Status/date: merged / 2026-01-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `6c20e89c0209`
- Diff scope read: GitHub Pull Request files API returned 8 files, +982/-323, 1521 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +14/-233 (247 lines); hunks: -43,7 +43,6; -63,6 +62,7; symbols: get_attn_backend, sparse_attn_indexer, sparse_attn_indexer_fake, Indexer, touching `get_attn_backend, sparse_attn_indexer, sparse_attn_indexer_fake`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +14/-233 (247 lines); hunks: -43,7 +43,6; -63,6 +62,7; symbols: get_attn_backend, sparse_attn_indexer, sparse_attn_indexer_fake, Indexer
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +14/-233
- Risk and verification: Runtime changes concentrate in `vllm/_aiter_ops.py`, `vllm/config/compilation.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #32175 - [Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding

- Link: https://github.com/vllm-project/vllm/pull/32175
- Status/date: merged / 2026-01-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `5de6dd0662da`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-2, 38 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bugfix] [DeepSeek-V3.2] fix sparse_attn_indexer padding"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +9/-2 (11 lines); hunks: -717,13 +717,20 @@ def sparse_attn_indexer(; -739,14 +746,14 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, touching `sparse_attn_indexer`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +9/-2 (11 lines); hunks: -717,13 +717,20 @@ def sparse_attn_indexer(; -739,14 +746,14 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +9/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #30356 - [CI][DeepSeek] Add nightly DeepSeek R1 `lm_eval` tests on H200

- Link: https://github.com/vllm-project/vllm/pull/30356
- Status/date: merged / 2026-01-05
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`; associated commits `276e03b92c16`
- Diff scope read: GitHub Pull Request files API returned 5 files, +33/-1, 51 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI][DeepSeek] Add nightly DeepSeek R1 `lm_eval` tests on H200"; model line: DeepSeek V3/R1; category: docs/tests/CI; main diff: `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`; technical summary: Covers "[CI][DeepSeek] Add nightly DeepSeek R1 `lm_eval` tests on H200"; the main implementation surface is `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11; `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11.
- Code diff details:
  - `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11
  - `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` added +11/-0 (11 lines); hunks: -0,0 +1,11
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml` added +11/-0; `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml` added +11/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gsm8k/configs/DeepSeek-R1-DP.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP.yaml`, `tests/evals/gsm8k/configs/models-h200.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31160 - [Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2

- Link: https://github.com/vllm-project/vllm/pull/31160
- Status/date: merged / 2025-12-24
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `76e6a951925b`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-3, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bug] Fix `Number of dimensions of tensors must match.` for Deepseek V3.2"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -878,11 +878,14 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -878,11 +878,14 @@ def forward(; symbols: forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31046 - [Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2

- Link: https://github.com/vllm-project/vllm/pull/31046
- Status/date: merged / 2025-12-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `4cf9429897c1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-2, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bug] Fix `error 'Dynamo failed to run FX node with fake tensors` for Deepseek V3.2"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -878,8 +878,11 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +5/-2 (7 lines); hunks: -878,8 +878,11 @@ def forward(; symbols: forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +5/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #30841 - [Bugfix] deepseek-V3.2 self.weights_proj has no bias

- Link: https://github.com/vllm-project/vllm/pull/30841
- Status/date: merged / 2025-12-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `84896fda22d3`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-1, 13 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] deepseek-V3.2 self.weights_proj has no bias"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bugfix] deepseek-V3.2 self.weights_proj has no bias"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -835,7 +835,11 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +5/-1 (6 lines); hunks: -835,7 +835,11 @@ def __init__(; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #27532 - [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2

- Link: https://github.com/vllm-project/vllm/pull/27532
- Status/date: merged / 2025-12-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `3e41992fecdc`
- Diff scope read: GitHub Pull Request files API returned 30 files, +1372/-256, 2323 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +18/-19 (37 lines); hunks: -83,6 +83,7; -618,8 +619,15 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake, touching `sparse_attn_indexer, sparse_attn_indexer_fake`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +18/-19 (37 lines); hunks: -83,6 +83,7; -618,8 +619,15 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +18/-19
- Risk and verification: The diff ships test coverage in `tests/conftest.py`, `tests/kernels/moe/test_batched_deepgemm.py`, `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_block_fp8.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #27568 - [DeepSeek v3.2] Make top-k work for any logit values.

- Link: https://github.com/vllm-project/vllm/pull/27568
- Status/date: merged / 2025-12-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `184076c3fecf`
- Diff scope read: GitHub Pull Request files API returned 5 files, +629/-210, 1067 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek v3.2] Make top-k work for any logit values."; model line: DeepSeek V3/R1; category: model implementation change; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[DeepSeek v3.2] Make top-k work for any logit values."; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -684,18 +684,18 @@ def sparse_attn_indexer(; -738,7 +738,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, touching `sparse_attn_indexer`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +3/-3 (6 lines); hunks: -684,18 +684,18 @@ def sparse_attn_indexer(; -738,7 +738,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +3/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/test_top_k_per_row.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29545 - [Bugfix] Fix DeepSeek R1 MTP weight loading

- Link: https://github.com/vllm-project/vllm/pull/29545
- Status/date: merged / 2025-12-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_mtp.py`; associated commits `51c57b51dd51`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-0, 30 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix DeepSeek R1 MTP weight loading"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_mtp.py`; technical summary: Covers "[Bugfix] Fix DeepSeek R1 MTP weight loading"; the main implementation surface is `vllm/model_executor/models/deepseek_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_mtp.py` modified +11/-0 (11 lines); hunks: -346,11 +346,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -377,6 +382,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_mtp.py` modified +11/-0 (11 lines); hunks: -346,11 +346,16 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; -377,6 +382,12 @@ def load_weights(self, weights: Iterable[tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_mtp.py` modified +11/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_mtp.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26670 - [ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA

- Link: https://github.com/vllm-project/vllm/pull/26670
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `06c20c990464`
- Diff scope read: GitHub Pull Request files API returned 9 files, +583/-15, 700 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[ROCm] Add AMD GPU support on Deepseek v3.2 and SparseMLA"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +18/-4 (22 lines); hunks: -591,6 +591,7 @@ def sparse_attn_indexer(; -630,7 +631,7 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake, touching `sparse_attn_indexer, sparse_attn_indexer_fake`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +18/-4 (22 lines); hunks: -591,6 +591,7 @@ def sparse_attn_indexer(; -630,7 +631,7 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, sparse_attn_indexer_fake
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +18/-4
- Risk and verification: Runtime changes concentrate in `vllm/attention/ops/rocm_aiter_mla_sparse.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/platforms/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28968 - [DeepSeek] Fix DeepSeek V3.2 Rope Embedding

- Link: https://github.com/vllm-project/vllm/pull/28968
- Status/date: merged / 2025-11-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `88f5b19f0bc6`
- Diff scope read: GitHub Pull Request files API returned 2 files, +17/-3, 69 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek] Fix DeepSeek V3.2 Rope Embedding"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[DeepSeek] Fix DeepSeek V3.2 Rope Embedding"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -846,8 +846,8 @@ def forward(; -1000,6 +1000,14 @@ def __init__(; symbols: forward, __init__, touching `forward, __init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +12/-2 (14 lines); hunks: -846,8 +846,8 @@ def forward(; -1000,6 +1000,14 @@ def __init__(; symbols: forward, __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +12/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26465 - [Deepseek v3.2] Remove extra logics in indexer

- Link: https://github.com/vllm-project/vllm/pull/26465
- Status/date: merged / 2025-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `09a7e6f6179b`
- Diff scope read: GitHub Pull Request files API returned 5 files, +141/-40, 272 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Deepseek v3.2] Remove extra logics in indexer"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Deepseek v3.2] Remove extra logics in indexer"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +11/-26 (37 lines); hunks: -574,9 +574,9 @@ def sparse_attn_indexer(; -586,9 +586,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, touching `sparse_attn_indexer`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +11/-26 (37 lines); hunks: -574,9 +574,9 @@ def sparse_attn_indexer(; -586,9 +586,6 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +11/-26
- Risk and verification: The diff ships test coverage in `tests/kernels/test_top_k_per_row.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #26763 - [Deepseek v3.2] Optimize top_k_per_row

- Link: https://github.com/vllm-project/vllm/pull/26763
- Status/date: merged / 2025-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `80e94529845d`
- Diff scope read: GitHub Pull Request files API returned 5 files, +13/-49, 203 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Deepseek v3.2] Optimize top_k_per_row"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Deepseek v3.2] Optimize top_k_per_row"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +0/-8 (8 lines); hunks: -577,15 +577,11 @@ def sparse_attn_indexer(; -642,15 +638,11 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, touching `sparse_attn_indexer`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +0/-8 (8 lines); hunks: -577,15 +577,11 @@ def sparse_attn_indexer(; -642,15 +638,11 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +0/-8
- Risk and verification: The diff ships test coverage in `tests/kernels/test_top_k_per_row.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #26456 - [Deepseek-V3.2][Kernel] Integrate cuda indexer k cache gather

- Link: https://github.com/vllm-project/vllm/pull/26456
- Status/date: merged / 2025-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `f5ed68ef63d0`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-68, 104 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Deepseek-V3.2][Kernel] Integrate cuda indexer k cache gather"; model line: DeepSeek V3/R1; category: performance/backend optimization; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Deepseek-V3.2][Kernel] Integrate cuda indexer k cache gather"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +6/-68 (74 lines); hunks: -75,7 +75,7; -483,69 +483,6 @@ def get_attn_backend(self) -> AttentionBackend:; symbols: get_attn_backend, cp_gather_indexer_k_quant_cache, sparse_attn_indexer, touching `get_attn_backend, cp_gather_indexer_k_quant_cache, sparse_attn_indexer`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-68 (74 lines); hunks: -75,7 +75,7; -483,69 +483,6 @@ def get_attn_backend(self) -> AttentionBackend:; symbols: get_attn_backend, cp_gather_indexer_k_quant_cache, sparse_attn_indexer
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-68
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #25589 - [Model] Add DeepSeek-V3.1 reasoning parser (split from PR #24972)

- Link: https://github.com/vllm-project/vllm/pull/25589
- Status/date: merged / 2025-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/reasoning/test_deepseekv3_reasoning_parser.py`; associated commits `85a65e7f51ad`
- Diff scope read: GitHub Pull Request files API returned 6 files, +215/-3, 269 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Add DeepSeek-V3.1 reasoning parser (split from PR #24972)"; model line: DeepSeek V3/R1; category: docs/tests/CI; main diff: `tests/reasoning/test_deepseekv3_reasoning_parser.py`; technical summary: Covers "[Model] Add DeepSeek-V3.1 reasoning parser (split from PR #24972)"; the main implementation surface is `tests/reasoning/test_deepseekv3_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +76/-0 (76 lines); hunks: -0,0 +1,76; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic, touching `tokenizer, test_parser_selection, test_identity_reasoning_parser_basic`.
- Code diff details:
  - `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +76/-0 (76 lines); hunks: -0,0 +1,76; symbols: tokenizer, test_parser_selection, test_identity_reasoning_parser_basic
- Key code excerpts:

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

- Reviewed files:
  - tests: `tests/reasoning/test_deepseekv3_reasoning_parser.py` added +76/-0
- Risk and verification: The diff ships test coverage in `tests/reasoning/test_deepseekv3_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #25999 - [Deepseek v3.2] Support indexer prefill chunking

- Link: https://github.com/vllm-project/vllm/pull/25999
- Status/date: merged / 2025-10-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `1e50f1be7058`
- Diff scope read: GitHub Pull Request files API returned 3 files, +149/-79, 324 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Deepseek v3.2] Support indexer prefill chunking"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Deepseek v3.2] Support indexer prefill chunking"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +37/-38 (75 lines); hunks: -583,44 +583,43 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer, touching `sparse_attn_indexer`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +37/-38 (75 lines); hunks: -583,44 +583,43 @@ def sparse_attn_indexer(; symbols: sparse_attn_indexer
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +37/-38
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_sparse_mla_backends.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #25896 - [New Model] DeepSeek-V3.2 (Rebased to Main)

- Link: https://github.com/vllm-project/vllm/pull/25896
- Status/date: merged / 2025-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`; associated commits `fa7e254a7f3e`
- Diff scope read: GitHub Pull Request files API returned 71 files, +3918/-221, 5400 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[New Model] DeepSeek-V3.2 (Rebased to Main)"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`; technical summary: Covers "[New Model] DeepSeek-V3.2 (Rebased to Main)"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/deepseek_mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +445/-4 (449 lines); hunks: -33,36 +33,57; -276,6 +297,7 @@ class DeepseekV2Attention(nn.Module):; symbols: DeepseekV2MLP, DeepseekV2Attention, __init__, touching `DeepseekV2MLP, DeepseekV2Attention, __init__`; `vllm/model_executor/models/deepseek_mtp.py` modified +13/-1 (14 lines); hunks: -53,8 +53,20 @@ def __init__(self, vllm_config: VllmConfig, prefix: str) -> N...; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +445/-4 (449 lines); hunks: -33,36 +33,57; -276,6 +297,7 @@ class DeepseekV2Attention(nn.Module):; symbols: DeepseekV2MLP, DeepseekV2Attention, __init__
  - `vllm/model_executor/models/deepseek_mtp.py` modified +13/-1 (14 lines); hunks: -53,8 +53,20 @@ def __init__(self, vllm_config: VllmConfig, prefix: str) -> N...; symbols: __init__, forward
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +445/-4; `vllm/model_executor/models/deepseek_mtp.py` modified +13/-1
- Risk and verification: The diff ships test coverage in `tests/compile/test_fusion_attn.py`, `tests/kernels/attention/test_cache.py`, `tests/kernels/attention/test_deepgemm_attention.py`, `tests/kernels/attention/test_flashmla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #24119 - [Bug] R1 Accuracy: Fix `routed_scaling_factor` Double Mul Issue

- Link: https://github.com/vllm-project/vllm/pull/24119
- Status/date: merged / 2025-09-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `930a24144c07`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-1, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bug] R1 Accuracy: Fix `routed_scaling_factor` Double Mul Issue"; model line: DeepSeek V3/R1; category: bug fix; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "[Bug] R1 Accuracy: Fix `routed_scaling_factor` Double Mul Issue"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -160,7 +160,8 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +2/-1 (3 lines); hunks: -160,7 +160,8 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/deepseek_v2.py
@@ -160,7 +160,8 @@ def __init__(
-            routed_scaling_factor=self.routed_scaling_factor,
+            # we do scaling outside, set factor to 1.0 to avoid double mul
+            routed_scaling_factor=1.0,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23971 - Add LoRA support for DeepSeek models (V2, V3, R1-0528)

- Link: https://github.com/vllm-project/vllm/pull/23971
- Status/date: merged / 2025-08-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `379ea2823a75`
- Diff scope read: GitHub Pull Request files API returned 3 files, +12/-7, 54 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add LoRA support for DeepSeek models (V2, V3, R1-0528)"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "Add LoRA support for DeepSeek models (V2, V3, R1-0528)"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +3/-2 (5 lines); hunks: -56,7 +56,7; -727,7 +727,8 @@ def forward(; symbols: forward, DeepseekV2ForCausalLM, touching `forward, DeepseekV2ForCausalLM`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +3/-2 (5 lines); hunks: -56,7 +56,7; -727,7 +727,8 @@ def forward(; symbols: forward, DeepseekV2ForCausalLM
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +3/-2
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek.py`, `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #23454 - Support DeepSeek-V3.1 tool call

- Link: https://github.com/vllm-project/vllm/pull/23454
- Status/date: merged / 2025-08-23
- Trace source: `git log --name-only -- <model-files>` found it through `examples/tool_chat_template_deepseekv31.jinja`; associated commits `b8f17f5d980e`
- Diff scope read: GitHub Pull Request files API returned 4 files, +468/-0, 491 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support DeepSeek-V3.1 tool call"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `examples/tool_chat_template_deepseekv31.jinja`; technical summary: Covers "Support DeepSeek-V3.1 tool call"; the main implementation surface is `examples/tool_chat_template_deepseekv31.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91.
- Code diff details:
  - `examples/tool_chat_template_deepseekv31.jinja` added +91/-0 (91 lines); hunks: -0,0 +1,91
- Key code excerpts:

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

- Reviewed files:
  - docs: `examples/tool_chat_template_deepseekv31.jinja` added +91/-0
- Risk and verification: Runtime changes concentrate in `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv31_tool_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17784 - [Feature] Support DeepSeekV3 Function Call

- Link: https://github.com/vllm-project/vllm/pull/17784
- Status/date: merged / 2025-05-12
- Trace source: `git log --name-only -- <model-files>` found it through `examples/tool_chat_template_deepseekv3.jinja`; associated commits `3a5ea7512926`
- Diff scope read: GitHub Pull Request files API returned 4 files, +473/-1, 495 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Support DeepSeekV3 Function Call"; model line: DeepSeek V3/R1; category: model support/runtime entry; main diff: `examples/tool_chat_template_deepseekv3.jinja`; technical summary: Covers "[Feature] Support DeepSeekV3 Function Call"; the main implementation surface is `examples/tool_chat_template_deepseekv3.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/tool_chat_template_deepseekv3.jinja` added +96/-0 (96 lines); hunks: -0,0 +1,96.
- Code diff details:
  - `examples/tool_chat_template_deepseekv3.jinja` added +96/-0 (96 lines); hunks: -0,0 +1,96
- Key code excerpts:

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

- Reviewed files:
  - docs: `examples/tool_chat_template_deepseekv3.jinja` added +96/-0
- Risk and verification: Runtime changes concentrate in `vllm/entrypoints/openai/tool_parsers/__init__.py`, `vllm/entrypoints/openai/tool_parsers/deepseekv3_tool_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13833 - DeepSeek V2/V3/R1 only place `lm_head` on last pp rank

- Link: https://github.com/vllm-project/vllm/pull/13833
- Status/date: merged / 2025-02-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/deepseek_v2.py`; associated commits `24679788ed38`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-3, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "DeepSeek V2/V3/R1 only place `lm_head` on last pp rank"; model line: DeepSeek V3/R1; category: model implementation change; main diff: `vllm/model_executor/models/deepseek_v2.py`; technical summary: Covers "DeepSeek V2/V3/R1 only place `lm_head` on last pp rank"; the main implementation surface is `vllm/model_executor/models/deepseek_v2.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -636,9 +636,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/deepseek_v2.py` modified +6/-3 (9 lines); hunks: -636,9 +636,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- Key code excerpts:

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

- Reviewed files:
  - runtime: `vllm/model_executor/models/deepseek_v2.py` modified +6/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/deepseek_v2.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
