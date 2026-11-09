# vllm Mistral Small 4 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `examples/generate/multimodal/mistral-small_offline.py` | no direct PR-number commit |
| `examples/tool_chat_template_mistral.jinja` | [#5649](https://github.com/vllm-project/vllm/pull/5649) |
| `examples/tool_chat_template_mistral3.jinja` | [#17195](https://github.com/vllm-project/vllm/pull/17195), [#17644](https://github.com/vllm-project/vllm/pull/17644) |
| `examples/tool_chat_template_mistral_parallel.jinja` | [#5649](https://github.com/vllm-project/vllm/pull/5649) |
| `tests/model_executor/test_mistral_large_3_eagle.py` | [#45217](https://github.com/vllm-project/vllm/pull/45217), [#65449](https://github.com/vllm-project/vllm/pull/65449) |
| `tests/models/fixtures/ministral_3b_chat.json` | no direct PR-number commit |
| `tests/models/fixtures/mistral_small_3_chat.json` | [#14977](https://github.com/vllm-project/vllm/pull/14977) |
| `tests/models/language/generation/test_mistral.py` | [#20093](https://github.com/vllm-project/vllm/pull/20093), [#28659](https://github.com/vllm-project/vllm/pull/28659), [#29918](https://github.com/vllm-project/vllm/pull/29918), [#48947](https://github.com/vllm-project/vllm/pull/48947) |
| `tests/models/multimodal/processing/test_mistral3.py` | [#52874](https://github.com/vllm-project/vllm/pull/52874), [#53758](https://github.com/vllm-project/vllm/pull/53758), [#57531](https://github.com/vllm-project/vllm/pull/57531) |
| `tests/parser/mistral/__init__.py` | [#48947](https://github.com/vllm-project/vllm/pull/48947) |
| `tests/parser/mistral/test_reasoning.py` | [#48947](https://github.com/vllm-project/vllm/pull/48947) |
| `tests/parser/mistral/test_tool_calls.py` | [#48947](https://github.com/vllm-project/vllm/pull/48947), [#54844](https://github.com/vllm-project/vllm/pull/54844), [#64169](https://github.com/vllm-project/vllm/pull/64169), [#65118](https://github.com/vllm-project/vllm/pull/65118) |
| `tests/renderers/test_mistral.py` | [#63812](https://github.com/vllm-project/vllm/pull/63812) |
| `tests/tokenizers_/test_mistral.py` | [#29757](https://github.com/vllm-project/vllm/pull/29757), [#38150](https://github.com/vllm-project/vllm/pull/38150), [#41658](https://github.com/vllm-project/vllm/pull/41658), [#44622](https://github.com/vllm-project/vllm/pull/44622), [#48947](https://github.com/vllm-project/vllm/pull/48947), [#55735](https://github.com/vllm-project/vllm/pull/55735), [#63812](https://github.com/vllm-project/vllm/pull/63812), [#64169](https://github.com/vllm-project/vllm/pull/64169) |
| `tests/tool_use/mistral/__init__.py` | no direct PR-number commit |
| `tests/tool_use/mistral/conftest.py` | no direct PR-number commit |
| `tests/tool_use/mistral/test_mistral_tool_calls.py` | [#39217](https://github.com/vllm-project/vllm/pull/39217), [#48947](https://github.com/vllm-project/vllm/pull/48947), [#62638](https://github.com/vllm-project/vllm/pull/62638) |
| `tests/tool_use/mistral/utils.py` | [#39217](https://github.com/vllm-project/vllm/pull/39217) |
| `vllm/model_executor/models/mistral.py` | [#1196](https://github.com/vllm-project/vllm/pull/1196), [#1220](https://github.com/vllm-project/vllm/pull/1220), [#1254](https://github.com/vllm-project/vllm/pull/1254), [#1303](https://github.com/vllm-project/vllm/pull/1303), [#2868](https://github.com/vllm-project/vllm/pull/2868), [#32780](https://github.com/vllm-project/vllm/pull/32780), [#33095](https://github.com/vllm-project/vllm/pull/33095) |
| `vllm/model_executor/models/mistral3.py` | [#15505](https://github.com/vllm-project/vllm/pull/15505), [#15950](https://github.com/vllm-project/vllm/pull/15950), [#17270](https://github.com/vllm-project/vllm/pull/17270), [#17428](https://github.com/vllm-project/vllm/pull/17428), [#21945](https://github.com/vllm-project/vllm/pull/21945), [#33939](https://github.com/vllm-project/vllm/pull/33939), [#36928](https://github.com/vllm-project/vllm/pull/36928), [#52874](https://github.com/vllm-project/vllm/pull/52874), [#53758](https://github.com/vllm-project/vllm/pull/53758), [#56277](https://github.com/vllm-project/vllm/pull/56277), [#57531](https://github.com/vllm-project/vllm/pull/57531) |
| `vllm/model_executor/models/mistral_eagle.py` | [#41024](https://github.com/vllm-project/vllm/pull/41024) |
| `vllm/model_executor/models/mistral_large_3.py` | [#29757](https://github.com/vllm-project/vllm/pull/29757), [#48153](https://github.com/vllm-project/vllm/pull/48153) |
| `vllm/model_executor/models/mistral_large_3_eagle.py` | [#29757](https://github.com/vllm-project/vllm/pull/29757), [#36163](https://github.com/vllm-project/vllm/pull/36163), [#37232](https://github.com/vllm-project/vllm/pull/37232), [#45217](https://github.com/vllm-project/vllm/pull/45217), [#48153](https://github.com/vllm-project/vllm/pull/48153), [#57633](https://github.com/vllm-project/vllm/pull/57633), [#65449](https://github.com/vllm-project/vllm/pull/65449) |
| `vllm/parser/mistral.py` | [#44596](https://github.com/vllm-project/vllm/pull/44596), [#48947](https://github.com/vllm-project/vllm/pull/48947), [#50515](https://github.com/vllm-project/vllm/pull/50515), [#54844](https://github.com/vllm-project/vllm/pull/54844), [#64169](https://github.com/vllm-project/vllm/pull/64169), [#65118](https://github.com/vllm-project/vllm/pull/65118) |
| `vllm/reasoning/mistral_reasoning_parser.py` | [#30391](https://github.com/vllm-project/vllm/pull/30391), [#44596](https://github.com/vllm-project/vllm/pull/44596), [#48947](https://github.com/vllm-project/vllm/pull/48947) |
| `vllm/renderers/mistral.py` | [#63812](https://github.com/vllm-project/vllm/pull/63812) |
| `vllm/tokenizers/mistral.py` | [#29757](https://github.com/vllm-project/vllm/pull/29757), [#31138](https://github.com/vllm-project/vllm/pull/31138), [#34651](https://github.com/vllm-project/vllm/pull/34651), [#36971](https://github.com/vllm-project/vllm/pull/36971), [#37209](https://github.com/vllm-project/vllm/pull/37209), [#38150](https://github.com/vllm-project/vllm/pull/38150), [#39217](https://github.com/vllm-project/vllm/pull/39217), [#41658](https://github.com/vllm-project/vllm/pull/41658), [#41962](https://github.com/vllm-project/vllm/pull/41962), [#48947](https://github.com/vllm-project/vllm/pull/48947), [#55735](https://github.com/vllm-project/vllm/pull/55735), [#56325](https://github.com/vllm-project/vllm/pull/56325), ... (13 total) |
| `vllm/tool_parsers/mistral_tool_parser.py` | [#30724](https://github.com/vllm-project/vllm/pull/30724), [#34651](https://github.com/vllm-project/vllm/pull/34651), [#37209](https://github.com/vllm-project/vllm/pull/37209), [#38150](https://github.com/vllm-project/vllm/pull/38150), [#39217](https://github.com/vllm-project/vllm/pull/39217), [#39294](https://github.com/vllm-project/vllm/pull/39294), [#40043](https://github.com/vllm-project/vllm/pull/40043), [#40531](https://github.com/vllm-project/vllm/pull/40531), [#41658](https://github.com/vllm-project/vllm/pull/41658), [#41730](https://github.com/vllm-project/vllm/pull/41730), [#44596](https://github.com/vllm-project/vllm/pull/44596), [#47550](https://github.com/vllm-project/vllm/pull/47550), ... (14 total) |
| `vllm/transformers_utils/configs/mistral.py` | [#1196](https://github.com/vllm-project/vllm/pull/1196), [#1254](https://github.com/vllm-project/vllm/pull/1254), [#20570](https://github.com/vllm-project/vllm/pull/20570), [#28659](https://github.com/vllm-project/vllm/pull/28659), [#29172](https://github.com/vllm-project/vllm/pull/29172), [#29239](https://github.com/vllm-project/vllm/pull/29239), [#29757](https://github.com/vllm-project/vllm/pull/29757), [#33521](https://github.com/vllm-project/vllm/pull/33521), [#34028](https://github.com/vllm-project/vllm/pull/34028), [#34104](https://github.com/vllm-project/vllm/pull/34104), [#36163](https://github.com/vllm-project/vllm/pull/36163), [#37104](https://github.com/vllm-project/vllm/pull/37104), ... (13 total) |
| `vllm/utils/mistral.py` | [#34651](https://github.com/vllm-project/vllm/pull/34651), [#40043](https://github.com/vllm-project/vllm/pull/40043), [#48947](https://github.com/vllm-project/vllm/pull/48947) |

## PR Coverage Summary

- Git-traced PRs: 65
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 65

- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-11-04 | [#65449](https://github.com/vllm-project/vllm/pull/65449) | merged | [Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state | `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2026-11-03 | [#56277](https://github.com/vllm-project/vllm/pull/56277) | merged | [MM] Mistral vision Encoder CG support | `vllm/model_executor/models/mistral3.py` |
| 2026-11-02 | [#65118](https://github.com/vllm-project/vllm/pull/65118) | merged | [Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path | `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py` |
| 2026-10-29 | [#64169](https://github.com/vllm-project/vllm/pull/64169) | merged | [Mistral] Use get_grammar_for_chat_request in MistralParser and require mistral-common 1.13.0 | `tests/tokenizers_/test_mistral.py`, `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py` |
| 2026-10-27 | [#63812](https://github.com/vllm-project/vllm/pull/63812) | merged | [Frontend][Mistral] Forward response_format to mistral-common chat templating | `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `tests/renderers/test_mistral.py` |
| 2026-10-21 | [#62638](https://github.com/vllm-project/vllm/pull/62638) | merged | [XPU][Test] Relax streaming/non-streaming equality in mistral tool_choice=none test | `tests/tool_use/mistral/test_mistral_tool_calls.py` |
| 2026-10-09 | [#57633](https://github.com/vllm-project/vllm/pull/57633) | merged | [Bugfix][Spec Decode] Fix multimodal embedding merge in Llama 4 and Mistral Large 3 EAGLE drafters | `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2026-10-06 | [#54844](https://github.com/vllm-project/vllm/pull/54844) | merged | [Bugfix][Parser] Mistral pre-v11: don't fail requests on unexpected tool call JSON | `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py` |
| 2026-09-29 | [#57531](https://github.com/vllm-project/vllm/pull/57531) | merged | [MM][Mistral3] Image preprocessing optimization | `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py` |
| 2026-09-21 | [#53758](https://github.com/vllm-project/vllm/pull/53758) | merged | [Bugfix][Model] Mistral3: align placeholder grid with public processor | `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py` |
| 2026-09-18 | [#56325](https://github.com/vllm-project/vllm/pull/56325) | merged | [Tokenizer] Drop dead Mistral tokenizer shims for transformers#41962 | `vllm/tokenizers/mistral.py` |
| 2026-09-08 | [#55735](https://github.com/vllm-project/vllm/pull/55735) | merged | [Frontend] Migrate input-validation errors to VLLMValidationError (harmony/mistral/chat_utils/params) | `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py` |
| 2026-08-23 | [#52874](https://github.com/vllm-project/vllm/pull/52874) | merged | [Bugfix][Model] Mistral3: fix image placeholder grid for processor size overrides | `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py` |
| 2026-07-31 | [#50515](https://github.com/vllm-project/vllm/pull/50515) | merged | [ROCm][CI] Restore Mistral tool-parser compatibility after unification | `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/parser/mistral.py` |
| 2026-07-30 | [#48947](https://github.com/vllm-project/vllm/pull/48947) | merged | [PARSER][Mistral] unified engine-based parser for reasoning and tool calls | `vllm/tool_parsers/mistral_tool_parser.py`, `tests/parser/mistral/test_reasoning.py`, `tests/reasoning/test_mistral_reasoning_parser.py` |
| 2026-07-10 | [#48153](https://github.com/vllm-project/vllm/pull/48153) | merged | [Model] Migrate MistralLarge3ForCausalLM to AutoWeightsLoader | `vllm/model_executor/models/mistral_large_3.py`, `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2026-07-06 | [#47550](https://github.com/vllm-project/vllm/pull/47550) | merged | [ROCm][CI][Bugfix] Fix flaky parallel tool-call streaming (test assertion + Mistral/Granite parsers) | `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py` |
| 2026-06-12 | [#45217](https://github.com/vllm-project/vllm/pull/45217) | merged | [Bugfix] Initialize missing attributes in mistral eagle | `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2026-06-10 | [#44596](https://github.com/vllm-project/vllm/pull/44596) | merged | [Refactor][Mistral] Extract parsing logic into MistralParser | `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py` |
| 2026-06-05 | [#44622](https://github.com/vllm-project/vllm/pull/44622) | merged | [Bugfix] Update mistral tokenizer test for continue_final_message fix | `tests/tokenizers_/test_mistral.py` |
| 2026-05-06 | [#41658](https://github.com/vllm-project/vllm/pull/41658) | merged | [Mistral Tokenizer] allow more leniency in apply_chat_template | `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py` |
| 2026-05-05 | [#41730](https://github.com/vllm-project/vllm/pull/41730) | merged | [BUGFIX] Support streamed_args_for_tool in MistralToolParser | `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py` |
| 2026-04-28 | [#41024](https://github.com/vllm-project/vllm/pull/41024) | merged | [FEATURE] Add EagleMistralForCausalLM | `vllm/model_executor/models/mistral_eagle.py` |
| 2026-04-24 | [#39294](https://github.com/vllm-project/vllm/pull/39294) | merged | [Bugfix][Parser] Fix Mistral tool parser for HF tokenizers | `vllm/tool_parsers/mistral_tool_parser.py` |
| 2026-04-24 | [#40043](https://github.com/vllm-project/vllm/pull/40043) | merged | [Feature] Avoid eager import of the "mistral_common" package. | `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/utils/mistral.py` |
| 2026-04-22 | [#40531](https://github.com/vllm-project/vllm/pull/40531) | merged | [Bugfix][Parser] Fix Mistral pre-v11 tool parser failing on trailing model output | `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py` |
| 2026-04-16 | [#39217](https://github.com/vllm-project/vllm/pull/39217) | merged | [Mistral Grammar] Fix tool and reasoning parsing | `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/tokenizers/mistral.py` |
| 2026-04-07 | [#37292](https://github.com/vllm-project/vllm/pull/37292) | merged | Fix Mistral yarn warning in Transformers v5 | `vllm/transformers_utils/configs/mistral.py` |
| 2026-04-06 | [#38150](https://github.com/vllm-project/vllm/pull/38150) | merged | [Mistral Grammar] Support Grammar Factory | `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tokenizers_/test_mistral.py` |
| 2026-03-18 | [#36928](https://github.com/vllm-project/vllm/pull/36928) | merged | [LoRA][BugFix] Fix skipped LoRA adapters for Mistral3 | `vllm/model_executor/models/mistral3.py` |
| 2026-03-17 | [#37209](https://github.com/vllm-project/vllm/pull/37209) | merged | Fix some Mistral parser issues | `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py` |
| 2026-03-16 | [#37232](https://github.com/vllm-project/vllm/pull/37232) | merged | Fix EagleMistralLarge3Model initialization | `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2026-03-16 | [#37104](https://github.com/vllm-project/vllm/pull/37104) | merged | Patch Mistral config | `vllm/transformers_utils/configs/mistral.py` |
| 2026-03-14 | [#36971](https://github.com/vllm-project/vllm/pull/36971) | merged | Mistral common v10 | `vllm/tokenizers/mistral.py` |
| 2026-03-11 | [#36163](https://github.com/vllm-project/vllm/pull/36163) | merged | Add support to Mistral large 3 eagle with dense layers | `vllm/transformers_utils/configs/mistral.py`, `vllm/model_executor/models/mistral_large_3_eagle.py` |
| 2026-02-23 | [#34651](https://github.com/vllm-project/vllm/pull/34651) | merged | [Feature] Lazy import for the "mistral" tokenizer module. | `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/tokenizers/mistral.py`, `vllm/utils/mistral.py` |
| 2026-02-12 | [#34104](https://github.com/vllm-project/vllm/pull/34104) | merged | Fix Mistral config remap to accept compressed-tensors quantization #34028 | `vllm/transformers_utils/configs/mistral.py` |
| 2026-02-07 | [#33939](https://github.com/vllm-project/vllm/pull/33939) | merged | Enable Eagle3 speculative decoding for Mistral3ForConditionalGeneration to support eagle3 | `vllm/model_executor/models/mistral3.py` |
| 2026-02-02 | [#33521](https://github.com/vllm-project/vllm/pull/33521) | merged | Fix mistral sliding window parsing | `vllm/transformers_utils/configs/mistral.py` |
| 2026-01-26 | [#33095](https://github.com/vllm-project/vllm/pull/33095) | merged | Remove unused logic in `models/mistral.py` | `vllm/model_executor/models/mistral.py` |
| 2026-01-22 | [#32780](https://github.com/vllm-project/vllm/pull/32780) | merged | [Llama.py -> mistral.py] Extract mistral-only relevant code into separate file | `vllm/model_executor/models/mistral.py` |
| 2025-12-26 | [#31138](https://github.com/vllm-project/vllm/pull/31138) | merged | [Mistral common] Ensure all functions are imported from the top & only use public methods | `vllm/tokenizers/mistral.py` |
| 2025-12-23 | [#30724](https://github.com/vllm-project/vllm/pull/30724) | merged | Fix edge case Mistral tool parser | `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py` |
| 2025-12-11 | [#30391](https://github.com/vllm-project/vllm/pull/30391) | merged | [IMPROVEMENT] Change MistralReasoningParser behavior | `tests/reasoning/test_mistral_reasoning_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py` |
| 2025-12-02 | [#29918](https://github.com/vllm-project/vllm/pull/29918) | merged | [BUGFIX] Fix regex pattern for Mistral Tool Call | `tests/models/language/generation/test_mistral.py` |
| 2025-12-02 | [#29757](https://github.com/vllm-project/vllm/pull/29757) | merged | Add Mistral Large 3 and Ministral 3 | `vllm/model_executor/models/mistral_large_3_eagle.py`, `tests/tokenizers_/test_mistral.py`, `vllm/transformers_utils/configs/mistral.py` |
| 2025-11-22 | [#29239](https://github.com/vllm-project/vllm/pull/29239) | merged | [Bugfix] Use HF config fields as fallback when loading Mistral config | `vllm/transformers_utils/configs/mistral.py` |
| 2025-11-21 | [#28659](https://github.com/vllm-project/vllm/pull/28659) | merged | Default model load/config/tokenizer to `mistral` format if relevant files exist | `tests/models/language/generation/test_mistral.py`, `vllm/transformers_utils/configs/mistral.py` |
| 2025-11-21 | [#29172](https://github.com/vllm-project/vllm/pull/29172) | merged | Fix mistral config | `vllm/transformers_utils/configs/mistral.py` |
| 2025-08-20 | [#21945](https://github.com/vllm-project/vllm/pull/21945) | merged | Migrate Mistral3ImagePixelInputs to TensorSchema | `vllm/model_executor/models/mistral3.py` |
| 2025-07-07 | [#20570](https://github.com/vllm-project/vllm/pull/20570) | merged | [Config] Refactor mistral configs | `vllm/transformers_utils/configs/mistral.py` |
| 2025-06-26 | [#20093](https://github.com/vllm-project/vllm/pull/20093) | merged | [Bugfix] Fix Mistral tool-parser regex for nested JSON | `tests/models/language/generation/test_mistral.py` |
| 2025-05-08 | [#17644](https://github.com/vllm-project/vllm/pull/17644) | merged | [Bugfix] Fix tool call template validation for Mistral models | `examples/tool_chat_template_mistral3.jinja` |
| 2025-04-30 | [#17428](https://github.com/vllm-project/vllm/pull/17428) | merged | Support LoRA for Mistral3 | `vllm/model_executor/models/mistral3.py` |
| 2025-04-29 | [#17195](https://github.com/vllm-project/vllm/pull/17195) | merged | [Misc] Add a Jinja template to support Mistral3 function calling | `examples/tool_chat_template_mistral3.jinja` |
| 2025-04-28 | [#17270](https://github.com/vllm-project/vllm/pull/17270) | merged | [Bugfix] Fix Mistral3 spatial merge error | `vllm/model_executor/models/mistral3.py` |
| 2025-04-02 | [#15950](https://github.com/vllm-project/vllm/pull/15950) | merged | [V1] Support Mistral3 in V1 | `vllm/model_executor/models/mistral3.py` |
| 2025-04-01 | [#15505](https://github.com/vllm-project/vllm/pull/15505) | merged | [Model] Support Mistral3 in the HF Transformers format | `vllm/model_executor/models/mistral3.py` |
| 2025-03-18 | [#14977](https://github.com/vllm-project/vllm/pull/14977) | merged | [Mistral-Small 3.1] Update docs and tests | `tests/models/fixtures/mistral_small_3_chat.json` |
| 2024-09-04 | [#5649](https://github.com/vllm-project/vllm/pull/5649) | merged | [Feature] OpenAI-Compatible Tools API + Streaming for Hermes & Mistral models | `examples/tool_chat_template_mistral_parallel.jinja`, `examples/tool_chat_template_mistral.jinja` |
| 2024-02-22 | [#2868](https://github.com/vllm-project/vllm/pull/2868) | merged | Migrate MistralForCausalLM to LlamaForCausalLM | `vllm/model_executor/models/mistral.py` |
| 2023-10-13 | [#1254](https://github.com/vllm-project/vllm/pull/1254) | merged | Bump up transformers version & Remove MistralConfig | `vllm/transformers_utils/configs/mistral.py`, `vllm/model_executor/models/mistral.py` |
| 2023-10-10 | [#1303](https://github.com/vllm-project/vllm/pull/1303) | merged | [Minor] Fix comment in mistral.py | `vllm/model_executor/models/mistral.py` |
| 2023-09-28 | [#1220](https://github.com/vllm-project/vllm/pull/1220) | merged | Fix Mistral model | `vllm/model_executor/models/mistral.py` |
| 2023-09-28 | [#1196](https://github.com/vllm-project/vllm/pull/1196) | merged | [Mistral] Mistral-7B-v0.1 support | `vllm/model_executor/models/mistral.py`, `vllm/transformers_utils/configs/mistral.py` |

## Per-PR Diff Audit Cards

### PR #65449 - [Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state

- Link: https://github.com/vllm-project/vllm/pull/65449
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; associated commits `20d7dd9ac152`
- Diff scope read: GitHub Pull Request files API returned 2 files, +45/-5, 122 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state"; model line: Mistral Small 4; category: bug fix; main diff: `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; technical summary: Covers "[Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state"; the main implementation surface is `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/model_executor/test_mistral_large_3_eagle.py` modified +37/-5 (42 lines); hunks: -1,12 +1,15; -77,16 +80,14 @@ def make_vllm_config(; symbols: make_vllm_config, patch_heavy_modules, test_eagle_mistral_large3_initializes_deepseek_runtime_attrs, touching `make_vllm_config, patch_heavy_modules, test_eagle_mistral_large3_initializes_deepseek_runtime_attrs`; `vllm/model_executor/models/mistral_large_3_eagle.py` modified +8/-0 (8 lines); hunks: -20,6 +20,7; -31,6 +32,7; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/model_executor/test_mistral_large_3_eagle.py` modified +37/-5 (42 lines); hunks: -1,12 +1,15; -77,16 +80,14 @@ def make_vllm_config(; symbols: make_vllm_config, patch_heavy_modules, test_eagle_mistral_large3_initializes_deepseek_runtime_attrs
  - `vllm/model_executor/models/mistral_large_3_eagle.py` modified +8/-0 (8 lines); hunks: -20,6 +20,7; -31,6 +32,7; symbols: __init__
- Key code excerpts:

```diff
diff -- tests/model_executor/test_mistral_large_3_eagle.py
@@ -1,12 +1,15 @@
+from pathlib import Path
+from transformers import DeepseekV2Config
+from vllm.config import ModelConfig, ParallelConfig, VllmConfig, set_current_vllm_config
@@ -77,16 +80,14 @@ def make_vllm_config(
-        parallel_config=SimpleNamespace(
-            eplb_config=SimpleNamespace(num_redundant_experts=0),
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -20,6 +20,7 @@
+    DeepseekV2MoE,
@@ -31,6 +32,7 @@
+    get_fused_shared_expert_layers,
@@ -60,6 +62,7 @@ def __init__(
+        self.hidden_size = config.hidden_size
@@ -81,6 +84,11 @@ def __init__(
```

- Reviewed files:
  - tests: `tests/model_executor/test_mistral_large_3_eagle.py` modified +37/-5
  - runtime: `vllm/model_executor/models/mistral_large_3_eagle.py` modified +8/-0
- Risk and verification: The diff ships test coverage in `tests/model_executor/test_mistral_large_3_eagle.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56277 - [MM] Mistral vision Encoder CG support

- Link: https://github.com/vllm-project/vllm/pull/56277
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `2142c95e67bc`
- Diff scope read: GitHub Pull Request files API returned 7 files, +751/-141, 1185 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MM] Mistral vision Encoder CG support"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[MM] Mistral vision Encoder CG support"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` modified +43/-1 (44 lines); hunks: -48,7 +48,12; -136,6 +141,15 @@ def forward(; symbols: forward, forward_packed, Mistral3MultiModalProjector, __init__, touching `forward, forward_packed, Mistral3MultiModalProjector`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` modified +43/-1 (44 lines); hunks: -48,7 +48,12; -136,6 +141,15 @@ def forward(; symbols: forward, forward_packed, Mistral3MultiModalProjector, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -48,7 +48,12 @@
-from .pixtral import PixtralHFEncoderInfo, PixtralHFVisionModel
+from .pixtral import (
+    PixtralEncoderCudaGraphMixin,
+    PixtralHFEncoderInfo,
+    PixtralHFVisionModel,
+    _merge_patches_by_index,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` modified +43/-1
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/generation/test_pixtral.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #65118 - [Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path

- Link: https://github.com/vllm-project/vllm/pull/65118
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`; associated commits `3fbc8d8b4fe0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +26/-5, 52 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path"; model line: Mistral Small 4; category: bug fix; main diff: `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`; technical summary: Covers "[Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path"; the main implementation surface is `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/parser/mistral/test_tool_calls.py` modified +23/-0 (23 lines); hunks: -38,6 +38,7; -1925,6 +1926,28 @@ def test_adjust_request_non_mistral_tokenizer(; symbols: test_adjust_request_non_mistral_tokenizer, test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens, touching `test_adjust_request_non_mistral_tokenizer, test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens`; `vllm/parser/mistral.py` modified +3/-5 (8 lines); hunks: -396,11 +396,9 @@ def adjust_request(; symbols: adjust_request, touching `adjust_request`.
- Code diff details:
  - `tests/parser/mistral/test_tool_calls.py` modified +23/-0 (23 lines); hunks: -38,6 +38,7; -1925,6 +1926,28 @@ def test_adjust_request_non_mistral_tokenizer(; symbols: test_adjust_request_non_mistral_tokenizer, test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens
  - `vllm/parser/mistral.py` modified +3/-5 (8 lines); hunks: -396,11 +396,9 @@ def adjust_request(; symbols: adjust_request
- Key code excerpts:

```diff
diff -- tests/parser/mistral/test_tool_calls.py
@@ -38,6 +38,7 @@
+from vllm.entrypoints.openai.responses.protocol import ResponsesRequest
@@ -1925,6 +1926,28 @@ def test_adjust_request_non_mistral_tokenizer(
+@pytest.mark.parametrize("responses", [True, False])
+def test_adjust_request_mistral_tokenizer_keeps_skip_special_tokens(
+    mistral_tool_parser: MistralToolParser, responses: bool
+) -> None:
diff -- vllm/parser/mistral.py
@@ -396,11 +396,9 @@ def adjust_request(
-            request = super().adjust_request(request)
-            if request.tools and request.tool_choice != "none":
-                # Keep special tokens so the [TOOL_CALLS] marker
-                # survives for tool detection.
-                request.skip_special_tokens = False
+            # MistralTokenizer keeps the parser's special tokens when skipping.
```

- Reviewed files:
  - tests: `tests/parser/mistral/test_tool_calls.py` modified +23/-0
  - runtime: `vllm/parser/mistral.py` modified +3/-5
- Risk and verification: The diff ships test coverage in `tests/parser/mistral/test_tool_calls.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64169 - [Mistral] Use get_grammar_for_chat_request in MistralParser and require mistral-common 1.13.0

- Link: https://github.com/vllm-project/vllm/pull/64169
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/mistral/test_tool_calls.py`, `tests/tokenizers_/test_mistral.py`, `vllm/parser/mistral.py`; associated commits `e5571b97fce2`
- Diff scope read: GitHub Pull Request files API returned 13 files, +275/-175, 739 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Mistral] Use get_grammar_for_chat_request in MistralParser and require mistral-common 1.13.0"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/tokenizers_/test_mistral.py`, `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`; technical summary: Covers "[Mistral] Use get_grammar_for_chat_request in MistralParser and require mistral-common 1.13.0"; the main implementation surface is `tests/tokenizers_/test_mistral.py`, `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_mistral.py` modified +4/-12 (16 lines); hunks: -2276,7 +2276,10 @@ def test_convert_ids_to_tokens_pre_args_tekken():; -2286,17 +2289,6 @@ def test_validate_request_params_valid_effort(reasoning_e...; symbols: test_convert_ids_to_tokens_pre_args_tekken, test_validate_request_params_valid_effort, test_validate_request_params_rejects_unsupported_effort, test_validate_request_params_rejects_chat_template, touching `test_convert_ids_to_tokens_pre_args_tekken, test_validate_request_params_valid_effort, test_validate_request_params_rejects_unsupported_effort`; `tests/parser/mistral/test_tool_calls.py` modified +202/-66 (268 lines); hunks: -10,6 +10,9; -38,7 +41,7; symbols: _make_request, _adjusted_grammar, test_adjust_request_grammar_factory, touching `_make_request, _adjusted_grammar, test_adjust_request_grammar_factory`; `vllm/parser/mistral.py` modified +59/-84 (143 lines); hunks: -13,20 +13,12; -40,6 +32,7; symbols: is_valid_id, _mistral_response_format, _is_pre_v11_tokeniser, adjust_request, touching `is_valid_id, _mistral_response_format, _is_pre_v11_tokeniser`.
- Code diff details:
  - `tests/tokenizers_/test_mistral.py` modified +4/-12 (16 lines); hunks: -2276,7 +2276,10 @@ def test_convert_ids_to_tokens_pre_args_tekken():; -2286,17 +2289,6 @@ def test_validate_request_params_valid_effort(reasoning_e...; symbols: test_convert_ids_to_tokens_pre_args_tekken, test_validate_request_params_valid_effort, test_validate_request_params_rejects_unsupported_effort, test_validate_request_params_rejects_chat_template
  - `tests/parser/mistral/test_tool_calls.py` modified +202/-66 (268 lines); hunks: -10,6 +10,9; -38,7 +41,7; symbols: _make_request, _adjusted_grammar, test_adjust_request_grammar_factory
  - `vllm/parser/mistral.py` modified +59/-84 (143 lines); hunks: -13,20 +13,12; -40,6 +32,7; symbols: is_valid_id, _mistral_response_format, _is_pre_v11_tokeniser, adjust_request
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_mistral.py
@@ -2276,7 +2276,10 @@ def test_convert_ids_to_tokens_pre_args_tekken():
-@pytest.mark.parametrize("reasoning_effort", [None, "none", "high"])
+@pytest.mark.parametrize(
+    "reasoning_effort",
+    [None, "none", "minimal", "low", "medium", "high", "xhigh", "max"],
+)
@@ -2286,17 +2289,6 @@ def test_validate_request_params_valid_effort(reasoning_effort: str | None) -> N
diff -- tests/parser/mistral/test_tool_calls.py
@@ -10,6 +10,9 @@
+from mistral_common.protocol.instruct.request import (
+    ResponseFormats as MistralResponseFormats,
+)
@@ -38,7 +41,7 @@
-from vllm.parser.mistral import _DEFAULT_JSON_SCHEMA, MistralParser, mistral_config
+from vllm.parser.mistral import MistralParser, mistral_config
diff -- vllm/parser/mistral.py
@@ -13,20 +13,12 @@
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_mistral.py` modified +4/-12; `tests/parser/mistral/test_tool_calls.py` modified +202/-66
  - runtime: `vllm/parser/mistral.py` modified +59/-84
- Risk and verification: The diff ships test coverage in `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63812 - [Frontend][Mistral] Forward response_format to mistral-common chat templating

- Link: https://github.com/vllm-project/vllm/pull/63812
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `tests/renderers/test_mistral.py`, `tests/tokenizers_/test_mistral.py`, `vllm/renderers/mistral.py`, `vllm/tokenizers/mistral.py`; associated commits `5d35ce3934a7`
- Diff scope read: GitHub Pull Request files API returned 6 files, +139/-70, 328 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Frontend][Mistral] Forward response_format to mistral-common chat templating"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `tests/renderers/test_mistral.py`; technical summary: Covers "[Frontend][Mistral] Forward response_format to mistral-common chat templating"; the main implementation surface is `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `tests/renderers/test_mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_mistral.py` modified +21/-52 (73 lines); hunks: -2325,19 +2325,17 @@ def v15_mistral_tokenizer() -> MistralTokenizer:; -2352,54 +2350,25 @@ def fake_apply_chat_template(**kwargs):; symbols: v15_mistral_tokenizer, v13_mistral_tokenizer, test_v15_apply_chat_template_passes_reasoning_effort_high, test_apply_chat_template_forwards_kwargs, touching `v15_mistral_tokenizer, v13_mistral_tokenizer, test_v15_apply_chat_template_passes_reasoning_effort_high`; `vllm/tokenizers/mistral.py` modified +10/-12 (22 lines); hunks: -390,22 +390,20 @@ def apply_chat_template(; -416,7 +414,7 @@ def apply_chat_template(; symbols: apply_chat_template, decode, touching `apply_chat_template, decode`; `tests/renderers/test_mistral.py` modified +54/-0 (54 lines); hunks: -10,6 +10,12; -94,6 +100,54 @@ def mocked_apply_chat_template(*_args, **_kwargs):; symbols: mocked_apply_chat_template, test_renderer_passes_response_format_to_tokenizer, test_apply_mistral_chat_template_thinking_chunk, touching `mocked_apply_chat_template, test_renderer_passes_response_format_to_tokenizer, test_apply_mistral_chat_template_thinking_chunk`; `vllm/renderers/mistral.py` modified +16/-6 (22 lines); hunks: -1,6 +1,8; -47,6 +49,18 @@ def safe_apply_chat_template(; symbols: safe_apply_chat_template, _get_chat_template_kwargs, MistralRenderer, __init__, touching `safe_apply_chat_template, _get_chat_template_kwargs, MistralRenderer`.
- Code diff details:
  - `tests/tokenizers_/test_mistral.py` modified +21/-52 (73 lines); hunks: -2325,19 +2325,17 @@ def v15_mistral_tokenizer() -> MistralTokenizer:; -2352,54 +2350,25 @@ def fake_apply_chat_template(**kwargs):; symbols: v15_mistral_tokenizer, v13_mistral_tokenizer, test_v15_apply_chat_template_passes_reasoning_effort_high, test_apply_chat_template_forwards_kwargs
  - `vllm/tokenizers/mistral.py` modified +10/-12 (22 lines); hunks: -390,22 +390,20 @@ def apply_chat_template(; -416,7 +414,7 @@ def apply_chat_template(; symbols: apply_chat_template, decode
  - `tests/renderers/test_mistral.py` modified +54/-0 (54 lines); hunks: -10,6 +10,12; -94,6 +100,54 @@ def mocked_apply_chat_template(*_args, **_kwargs):; symbols: mocked_apply_chat_template, test_renderer_passes_response_format_to_tokenizer, test_apply_mistral_chat_template_thinking_chunk
  - `vllm/renderers/mistral.py` modified +16/-6 (22 lines); hunks: -1,6 +1,8; -47,6 +49,18 @@ def safe_apply_chat_template(; symbols: safe_apply_chat_template, _get_chat_template_kwargs, MistralRenderer, __init__
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_mistral.py
@@ -2325,19 +2325,17 @@ def v15_mistral_tokenizer() -> MistralTokenizer:
-@pytest.fixture(scope="module")
-def v13_mistral_tokenizer() -> MistralTokenizer:
-    """Load the v13 Mistral tokenizer; skip if unavailable."""
-    try:
-        return MistralTokenizer.from_pretrained("mistralai/Magistral-Small-2509")
-    except Exception:
diff -- vllm/tokenizers/mistral.py
@@ -390,22 +390,20 @@ def apply_chat_template(
-        continue_final_message = kwargs.get("continue_final_message", False)
-        tokenize = kwargs.get("tokenize", True)
-        padding = kwargs.get("padding", False)
-        truncation = kwargs.get("truncation", False)
-        max_length = kwargs.get("max_length")
-        version_kwargs = {}
diff -- tests/renderers/test_mistral.py
@@ -10,6 +10,12 @@
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_mistral.py` modified +21/-52; `tests/renderers/test_mistral.py` modified +54/-0
  - runtime: `vllm/tokenizers/mistral.py` modified +10/-12; `vllm/renderers/mistral.py` modified +16/-6
- Risk and verification: The diff ships test coverage in `tests/entrypoints/serve/tokenize/test_serving_tokenization.py`, `tests/renderers/test_mistral.py`, `tests/tokenizers_/test_mistral.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62638 - [XPU][Test] Relax streaming/non-streaming equality in mistral tool_choice=none test

- Link: https://github.com/vllm-project/vllm/pull/62638
- Status/date: merged / 2026-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_use/mistral/test_mistral_tool_calls.py`; associated commits `fc9b7e654643`
- Diff scope read: GitHub Pull Request files API returned 2 files, +11/-2, 41 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[XPU][Test] Relax streaming/non-streaming equality in mistral tool_choice=none test"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/tool_use/mistral/test_mistral_tool_calls.py`; technical summary: Covers "[XPU][Test] Relax streaming/non-streaming equality in mistral tool_choice=none test"; the main implementation surface is `tests/tool_use/mistral/test_mistral_tool_calls.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_use/mistral/test_mistral_tool_calls.py` modified +11/-1 (12 lines); hunks: -2,6 +2,7; -17,6 +18,7; symbols: test_tool_call_none_with_tools, touching `test_tool_call_none_with_tools`.
- Code diff details:
  - `tests/tool_use/mistral/test_mistral_tool_calls.py` modified +11/-1 (12 lines); hunks: -2,6 +2,7; -17,6 +18,7; symbols: test_tool_call_none_with_tools
- Key code excerpts:

```diff
diff -- tests/tool_use/mistral/test_mistral_tool_calls.py
@@ -2,6 +2,7 @@
+import os
@@ -17,6 +18,7 @@
+from vllm.platforms import current_platform
@@ -334,7 +336,15 @@ async def test_tool_call_none_with_tools(
-        assert streamed_content == non_streaming_content
+        if current_platform.is_xpu():
```

- Reviewed files:
  - tests: `tests/tool_use/mistral/test_mistral_tool_calls.py` modified +11/-1
- Risk and verification: The diff ships test coverage in `tests/tool_use/mistral/test_mistral_tool_calls.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57633 - [Bugfix][Spec Decode] Fix multimodal embedding merge in Llama 4 and Mistral Large 3 EAGLE drafters

- Link: https://github.com/vllm-project/vllm/pull/57633
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral_large_3_eagle.py`; associated commits `581692cc0fd5`
- Diff scope read: GitHub Pull Request files API returned 3 files, +71/-5, 114 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Spec Decode] Fix multimodal embedding merge in Llama 4 and Mistral Large 3 EAGLE drafters"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/model_executor/models/mistral_large_3_eagle.py`; technical summary: Covers "[Bugfix][Spec Decode] Fix multimodal embedding merge in Llama 4 and Mistral Large 3 EAGLE drafters"; the main implementation surface is `vllm/model_executor/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral_large_3_eagle.py` modified +26/-3 (29 lines); hunks: -23,8 +23,17; -148,7 +157,21 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, get_language_model, embed_input_ids, forward, touching `__init__, get_language_model, embed_input_ids`.
- Code diff details:
  - `vllm/model_executor/models/mistral_large_3_eagle.py` modified +26/-3 (29 lines); hunks: -23,8 +23,17; -148,7 +157,21 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, get_language_model, embed_input_ids, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -23,8 +23,17 @@
-from .interfaces import SupportsMultiModal, SupportsMultiModalEmbeddings
-from .utils import WeightsMapper, make_empty_intermediate_tensors_factory, maybe_prefix
+from .interfaces import (
+    MultiModalEmbeddings,
+    SupportsMultiModalEmbeddings,
+    _require_is_multimodal,
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral_large_3_eagle.py` modified +26/-3
- Risk and verification: The diff ships test coverage in `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #54844 - [Bugfix][Parser] Mistral pre-v11: don't fail requests on unexpected tool call JSON

- Link: https://github.com/vllm-project/vllm/pull/54844
- Status/date: merged / 2026-10-06
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`; associated commits `a3e0243b1c3e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +208/-56, 387 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Parser] Mistral pre-v11: don't fail requests on unexpected tool call JSON"; model line: Mistral Small 4; category: bug fix; main diff: `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`; technical summary: Covers "[Bugfix][Parser] Mistral pre-v11: don't fail requests on unexpected tool call JSON"; the main implementation surface is `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/parser/mistral/test_tool_calls.py` modified +128/-11 (139 lines); hunks: -475,17 +475,22 @@ def test_extract_tool_calls_pre_v11_tokenizer(; -506,15 +511,126 @@ def test_extract_tool_calls_pre_v11_regex_fallback(; symbols: test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls_pre_v11_multiple_bot_tokens_raises, test_extract_tool_calls_pre_v11_multiple_bot_tokens, test_extract_tool_calls_pre_v11_regex_fallback, touching `test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls_pre_v11_multiple_bot_tokens_raises, test_extract_tool_calls_pre_v11_multiple_bot_tokens`; `vllm/parser/mistral.py` modified +80/-45 (125 lines); hunks: -117,6 +117,37 @@ def _is_pre_v11_tokeniser(model_tokenizer: TokenizerLike) -...; -301,6 +332,7 @@ def __init__(; symbols: _is_pre_v11_tokeniser, _pre_v11_function_calls, mistral_config, __init__, touching `_is_pre_v11_tokeniser, _pre_v11_function_calls, mistral_config`.
- Code diff details:
  - `tests/parser/mistral/test_tool_calls.py` modified +128/-11 (139 lines); hunks: -475,17 +475,22 @@ def test_extract_tool_calls_pre_v11_tokenizer(; -506,15 +511,126 @@ def test_extract_tool_calls_pre_v11_regex_fallback(; symbols: test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls_pre_v11_multiple_bot_tokens_raises, test_extract_tool_calls_pre_v11_multiple_bot_tokens, test_extract_tool_calls_pre_v11_regex_fallback
  - `vllm/parser/mistral.py` modified +80/-45 (125 lines); hunks: -117,6 +117,37 @@ def _is_pre_v11_tokeniser(model_tokenizer: TokenizerLike) -...; -301,6 +332,7 @@ def __init__(; symbols: _is_pre_v11_tokeniser, _pre_v11_function_calls, mistral_config, __init__
- Key code excerpts:

```diff
diff -- tests/parser/mistral/test_tool_calls.py
@@ -475,17 +475,22 @@ def test_extract_tool_calls_pre_v11_tokenizer(
-def test_extract_tool_calls_pre_v11_multiple_bot_tokens_raises(
+def test_extract_tool_calls_pre_v11_multiple_bot_tokens(
+    """A second BOT token must not fail the request; like streaming, only the
+    calls after the first BOT token are extracted."""
-    with pytest.raises(ValueError, match="Only one BOT token"):
-        mistral_pre_v11_tool_parser.extract_tool_calls(
diff -- vllm/parser/mistral.py
@@ -117,6 +117,37 @@ def _is_pre_v11_tokeniser(model_tokenizer: TokenizerLike) -> bool:
+def _pre_v11_function_calls(parsed: Any) -> list[FunctionCall]:
+    """Decode the JSON after a pre-v11 ``[TOOL_CALLS]`` marker.
+    Mirrors the streaming path: a bare object is a single call, entries that
+    are not call objects are skipped, a missing or non-string name becomes
+    ``""`` (as in the v11+ path) and string arguments are kept as-is.
+    """
```

- Reviewed files:
  - tests: `tests/parser/mistral/test_tool_calls.py` modified +128/-11
  - runtime: `vllm/parser/mistral.py` modified +80/-45
- Risk and verification: The diff ships test coverage in `tests/parser/mistral/test_tool_calls.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57531 - [MM][Mistral3] Image preprocessing optimization

- Link: https://github.com/vllm-project/vllm/pull/57531
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`; associated commits `d86cf9124098`
- Diff scope read: GitHub Pull Request files API returned 6 files, +228/-25, 413 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[MM][Mistral3] Image preprocessing optimization"; model line: Mistral Small 4; category: performance/backend optimization; main diff: `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[MM][Mistral3] Image preprocessing optimization"; the main implementation surface is `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_mistral3.py` modified +128/-2 (130 lines); hunks: -4,14 +4,29; -21,6 +36,65; symbols: test_pixtral_patch_embed_preserves_image_order_and_strides, _process_images_with_hf, test_processor_size_override, test_mm_device_do_normalize, touching `test_pixtral_patch_embed_preserves_image_order_and_strides, _process_images_with_hf, test_processor_size_override`; `vllm/model_executor/models/mistral3.py` modified +19/-3 (22 lines); hunks: -7,13 +7,16; -56,6 +59,10; symbols: Mistral3ImagePixelInputs, get_vision_encoder_info, get_hf_processor, get_supported_mm_limits, touching `Mistral3ImagePixelInputs, get_vision_encoder_info, get_hf_processor`.
- Code diff details:
  - `tests/models/multimodal/processing/test_mistral3.py` modified +128/-2 (130 lines); hunks: -4,14 +4,29; -21,6 +36,65; symbols: test_pixtral_patch_embed_preserves_image_order_and_strides, _process_images_with_hf, test_processor_size_override, test_mm_device_do_normalize
  - `vllm/model_executor/models/mistral3.py` modified +19/-3 (22 lines); hunks: -7,13 +7,16; -56,6 +59,10; symbols: Mistral3ImagePixelInputs, get_vision_encoder_info, get_hf_processor, get_supported_mm_limits
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_mistral3.py
@@ -4,14 +4,29 @@
+import torch.nn.functional as F
+from transformers.models.pixtral import PixtralProcessor
-from vllm.model_executor.models.lightonocr import LightOnOCRProcessingInfo
+from vllm.model_executor.layers.fusion.mm_input_norm import (
+    FusedMMInputNorm,
+    IdentityInputNorm,
diff -- vllm/model_executor/models/mistral3.py
@@ -7,13 +7,16 @@
+import transformers
+from packaging.version import Version
+from vllm.model_executor.layers.fusion.mm_input_norm import build_mm_input_norm
@@ -56,6 +59,10 @@
+TRANSFORMERS_SUPPORTS_PIXTRAL_IMAGE_ONLY = Version(transformers.__version__) >= Version(
+    "5.15.0"
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_mistral3.py` modified +128/-2
  - runtime: `vllm/model_executor/models/mistral3.py` modified +19/-3
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_mistral3.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53758 - [Bugfix][Model] Mistral3: align placeholder grid with public processor

- Link: https://github.com/vllm-project/vllm/pull/53758
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`; associated commits `9598487bc182`
- Diff scope read: GitHub Pull Request files API returned 2 files, +54/-37, 165 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] Mistral3: align placeholder grid with public processor"; model line: Mistral Small 4; category: bug fix; main diff: `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[Bugfix][Model] Mistral3: align placeholder grid with public processor"; the main implementation surface is `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_mistral3.py` modified +49/-27 (76 lines); hunks: -5,7 +5,7; -22,25 +22,41; symbols: _processed_pixel_values, _process_images_with_hf, _placeholder_count_from_prompt_updates, _placeholder_tokens_from_prompt_updates, touching `_processed_pixel_values, _process_images_with_hf, _placeholder_count_from_prompt_updates`; `vllm/model_executor/models/mistral3.py` modified +5/-10 (15 lines); hunks: -192,18 +192,13 @@ def get_patch_grid_size(; symbols: get_patch_grid_size, touching `get_patch_grid_size`.
- Code diff details:
  - `tests/models/multimodal/processing/test_mistral3.py` modified +49/-27 (76 lines); hunks: -5,7 +5,7; -22,25 +22,41; symbols: _processed_pixel_values, _process_images_with_hf, _placeholder_count_from_prompt_updates, _placeholder_tokens_from_prompt_updates
  - `vllm/model_executor/models/mistral3.py` modified +5/-10 (15 lines); hunks: -192,18 +192,13 @@ def get_patch_grid_size(; symbols: get_patch_grid_size
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_mistral3.py
@@ -5,7 +5,7 @@
-from transformers import BatchFeature
+from transformers import AutoProcessor, BatchFeature
@@ -22,25 +22,41 @@
-def _processed_pixel_values(
+def _process_images_with_hf(
-) -> list[torch.Tensor]:
diff -- vllm/model_executor/models/mistral3.py
@@ -192,18 +192,13 @@ def get_patch_grid_size(
-        patch_size = self.vision_config.patch_size
-        spatial_merge_size = self.hf_config.spatial_merge_size
-        # The HF processor rounds each dimension up to the vision patch size
-        # before the projector drops incomplete spatial-merge groups. This is
-        # not equivalent to rounding directly to the merged patch size.
-        num_width_patches = (image_width - 1) // patch_size + 1
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_mistral3.py` modified +49/-27
  - runtime: `vllm/model_executor/models/mistral3.py` modified +5/-10
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_mistral3.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56325 - [Tokenizer] Drop dead Mistral tokenizer shims for transformers#41962

- Link: https://github.com/vllm-project/vllm/pull/56325
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tokenizers/mistral.py`; associated commits `e562003adbb9`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-17, 49 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Tokenizer] Drop dead Mistral tokenizer shims for transformers#41962"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/tokenizers/mistral.py`; technical summary: Covers "[Tokenizer] Drop dead Mistral tokenizer shims for transformers#41962"; the main implementation surface is `vllm/tokenizers/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tokenizers/mistral.py` modified +5/-17 (22 lines); hunks: -354,22 +354,13 @@ def __call__(; -389,8 +380,10 @@ def encode(; symbols: __call__, vocab, encode, apply_chat_template, touching `__call__, vocab, encode`.
- Code diff details:
  - `vllm/tokenizers/mistral.py` modified +5/-17 (22 lines); hunks: -354,22 +354,13 @@ def __call__(; -389,8 +380,10 @@ def encode(; symbols: __call__, vocab, encode, apply_chat_template
- Key code excerpts:

```diff
diff -- vllm/tokenizers/mistral.py
@@ -354,22 +354,13 @@ def __call__(
-        encoded = self.transformers_tokenizer(
+        return self.transformers_tokenizer(
-        # TODO(juliendenize): once https://github.com/huggingface/transformers/pull/41962
-        # is in, revert to only call self.transformers_tokenizer(...).
-        # Hack to fix wrongly added eos token, when fix will be supported the condition
-        # below will be False even before the revert is done.
```

- Reviewed files:
  - runtime: `vllm/tokenizers/mistral.py` modified +5/-17
- Risk and verification: Runtime changes concentrate in `vllm/tokenizers/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #55735 - [Frontend] Migrate input-validation errors to VLLMValidationError (harmony/mistral/chat_utils/params)

- Link: https://github.com/vllm-project/vllm/pull/55735
- Status/date: merged / 2026-09-08
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`; associated commits `5133e1d28594`
- Diff scope read: GitHub Pull Request files API returned 7 files, +63/-8, 160 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Frontend] Migrate input-validation errors to VLLMValidationError (harmony/mistral/chat_utils/params)"; model line: Mistral Small 4; category: bug fix; main diff: `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`; technical summary: Covers "[Frontend] Migrate input-validation errors to VLLMValidationError (harmony/mistral/chat_utils/params)"; the main implementation surface is `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_mistral.py` modified +14/-1 (15 lines); hunks: -11,6 +11,7; -2279,8 +2280,20 @@ def test_validate_request_params_rejects_unsupported_effo...; symbols: test_validate_request_params_rejects_unsupported_effort, test_validate_request_params_rejects_chat_template, touching `test_validate_request_params_rejects_unsupported_effort, test_validate_request_params_rejects_chat_template`; `vllm/tokenizers/mistral.py` modified +8/-3 (11 lines); hunks: -34,6 +34,7; -144,15 +145,19 @@ def _validate_apply_chat_template_args(; symbols: _validate_apply_chat_template_args, validate_request_params, touching `_validate_apply_chat_template_args, validate_request_params`.
- Code diff details:
  - `tests/tokenizers_/test_mistral.py` modified +14/-1 (15 lines); hunks: -11,6 +11,7; -2279,8 +2280,20 @@ def test_validate_request_params_rejects_unsupported_effo...; symbols: test_validate_request_params_rejects_unsupported_effort, test_validate_request_params_rejects_chat_template
  - `vllm/tokenizers/mistral.py` modified +8/-3 (11 lines); hunks: -34,6 +34,7; -144,15 +145,19 @@ def _validate_apply_chat_template_args(; symbols: _validate_apply_chat_template_args, validate_request_params
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_mistral.py
@@ -11,6 +11,7 @@
+from vllm.exceptions import VLLMValidationError
@@ -2279,8 +2280,20 @@ def test_validate_request_params_rejects_unsupported_effort() -> None:
-    with pytest.raises(ValueError, match="reasoning_effort"):
+    with pytest.raises(VLLMValidationError, match="reasoning_effort") as exc_info:
+    assert exc_info.value.parameter == "reasoning_effort"
+def test_validate_request_params_rejects_chat_template() -> None:
diff -- vllm/tokenizers/mistral.py
@@ -34,6 +34,7 @@
+from vllm.exceptions import VLLMValidationError
@@ -144,15 +145,19 @@ def _validate_apply_chat_template_args(
-        raise ValueError("chat_template is not supported for Mistral tokenizers.")
+        raise VLLMValidationError(
+            "chat_template is not supported for Mistral tokenizers.",
+            parameter="chat_template",
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_mistral.py` modified +14/-1
  - runtime: `vllm/tokenizers/mistral.py` modified +8/-3
- Risk and verification: The diff ships test coverage in `tests/entrypoints/openai/test_render_parity.py`, `tests/entrypoints/unit_tests/test_chat_utils.py`, `tests/tokenizers_/test_mistral.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #52874 - [Bugfix][Model] Mistral3: fix image placeholder grid for processor size overrides

- Link: https://github.com/vllm-project/vllm/pull/52874
- Status/date: merged / 2026-08-23
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`; associated commits `a3561ef8e49d`
- Diff scope read: GitHub Pull Request files API returned 3 files, +210/-7, 271 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] Mistral3: fix image placeholder grid for processor size overrides"; model line: Mistral Small 4; category: bug fix; main diff: `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[Bugfix][Model] Mistral3: fix image placeholder grid for processor size overrides"; the main implementation surface is `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_mistral3.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: _processed_pixel_values, _placeholder_count_from_prompt_updates, _expected_placeholder_tokens_per_image, test_processor_size_override, touching `_processed_pixel_values, _placeholder_count_from_prompt_updates, _expected_placeholder_tokens_per_image`; `vllm/model_executor/models/mistral3.py` modified +54/-5 (59 lines); hunks: -1,6 +1,7; -22,7 +23,11; symbols: Mistral3ImagePixelInputs, forward, Mistral3HFEncoderInfo, __init__, touching `Mistral3ImagePixelInputs, forward, Mistral3HFEncoderInfo`.
- Code diff details:
  - `tests/models/multimodal/processing/test_mistral3.py` added +143/-0 (143 lines); hunks: -0,0 +1,143; symbols: _processed_pixel_values, _placeholder_count_from_prompt_updates, _expected_placeholder_tokens_per_image, test_processor_size_override
  - `vllm/model_executor/models/mistral3.py` modified +54/-5 (59 lines); hunks: -1,6 +1,7; -22,7 +23,11; symbols: Mistral3ImagePixelInputs, forward, Mistral3HFEncoderInfo, __init__
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_mistral3.py
@@ -0,0 +1,143 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Tests for Mistral3's multimodal preprocessing kwargs."""
+import pytest
+import torch
+from PIL import Image
diff -- vllm/model_executor/models/mistral3.py
@@ -1,6 +1,7 @@
+import math
@@ -22,7 +23,11 @@
-from vllm.multimodal.parse import ImageProcessorItems, ImageSize, MultiModalDataItems
+from vllm.multimodal.parse import (
+    ImageProcessorItems,
+    ImageSize,
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_mistral3.py` added +143/-0
  - runtime: `vllm/model_executor/models/mistral3.py` modified +54/-5
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_mistral3.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #50515 - [ROCm][CI] Restore Mistral tool-parser compatibility after unification

- Link: https://github.com/vllm-project/vllm/pull/50515
- Status/date: merged / 2026-07-31
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/parser/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `8d8a4e0f2b11`
- Diff scope read: GitHub Pull Request files API returned 2 files, +21/-4, 52 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI] Restore Mistral tool-parser compatibility after unification"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/parser/mistral.py`; technical summary: Covers "[ROCm][CI] Restore Mistral tool-parser compatibility after unification"; the main implementation surface is `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/parser/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mistral_tool_parser.py` modified +10/-0 (10 lines); hunks: -25,6 +25,16 @@ class MistralToolParser(MistralParserToolAdapter): # type: ig...; symbols: MistralToolParser, bot_token, bot_token_id, adjust_request, touching `MistralToolParser, bot_token, bot_token_id`; `vllm/parser/mistral.py` modified +11/-4 (15 lines); hunks: -526,14 +526,21 @@ def extract_tool_calls_from_content(; -550,8 +557,8 @@ def _legacy_extract_tool_calls(; symbols: extract_tool_calls_from_content, _legacy_extract_tool_calls, touching `extract_tool_calls_from_content, _legacy_extract_tool_calls`.
- Code diff details:
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +10/-0 (10 lines); hunks: -25,6 +25,16 @@ class MistralToolParser(MistralParserToolAdapter): # type: ig...; symbols: MistralToolParser, bot_token, bot_token_id, adjust_request
  - `vllm/parser/mistral.py` modified +11/-4 (15 lines); hunks: -526,14 +526,21 @@ def extract_tool_calls_from_content(; -550,8 +557,8 @@ def _legacy_extract_tool_calls(; symbols: extract_tool_calls_from_content, _legacy_extract_tool_calls
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -25,6 +25,16 @@ class MistralToolParser(MistralParserToolAdapter):  # type: ignore[valid-type, m
+    @property
+    def bot_token(self) -> str:
+        """Return the Mistral tool-call marker exposed by the legacy parser."""
+        return self._parser_engine.bot_token
+    @property
+    def bot_token_id(self) -> int | None:
diff -- vllm/parser/mistral.py
@@ -526,14 +526,21 @@ def extract_tool_calls_from_content(
-        request: ChatCompletionRequest,
+        request: ChatCompletionRequest | None,
+        if request is None:
+            tool_choice = None
+            tools = None
+        else:
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +10/-0; `vllm/parser/mistral.py` modified +11/-4
- Risk and verification: Runtime changes concentrate in `vllm/parser/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #48947 - [PARSER][Mistral] unified engine-based parser for reasoning and tool calls

- Link: https://github.com/vllm-project/vllm/pull/48947
- Status/date: merged / 2026-07-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/language/generation/test_mistral.py`, `tests/parser/mistral/__init__.py`, `tests/parser/mistral/test_reasoning.py`, `tests/parser/mistral/test_tool_calls.py`, `tests/tokenizers_/test_mistral.py` and 11 files; associated commits `1a20d23dab6e`
- Diff scope read: GitHub Pull Request files API returned 30 files, +2931/-1492, 5023 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[PARSER][Mistral] unified engine-based parser for reasoning and tool calls"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `vllm/tool_parsers/mistral_tool_parser.py`, `tests/parser/mistral/test_reasoning.py`, `tests/reasoning/test_mistral_reasoning_parser.py`; technical summary: Covers "[PARSER][Mistral] unified engine-based parser for reasoning and tool calls"; the main implementation surface is `vllm/tool_parsers/mistral_tool_parser.py`, `tests/parser/mistral/test_reasoning.py`, `tests/reasoning/test_mistral_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mistral_tool_parser.py` modified +26/-756 (782 lines); hunks: -3,767 +3,37; symbols: MistralToolParser, StreamingState, MistralToolCall, generate_random_id, touching `MistralToolParser, StreamingState, MistralToolCall`; `tests/parser/mistral/test_reasoning.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: mistral_tokenizer, mistral_v11_tokenizer, _encode_v13, test_mistral_reasoning_v13, touching `mistral_tokenizer, mistral_v11_tokenizer, _encode_v13`; `tests/reasoning/test_mistral_reasoning_parser.py` removed +0/-348 (348 lines); hunks: -1,348 +0,0; symbols: mistral_tokenizer, test_mistral_reasoning, touching `mistral_tokenizer, test_mistral_reasoning`; `vllm/reasoning/mistral_reasoning_parser.py` modified +2/-158 (160 lines); hunks: -1,162 +1,6; symbols: MistralReasoningParser, __init__, start_token, end_token, touching `MistralReasoningParser, __init__, start_token`.
- Code diff details:
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +26/-756 (782 lines); hunks: -3,767 +3,37; symbols: MistralToolParser, StreamingState, MistralToolCall, generate_random_id
  - `tests/parser/mistral/test_reasoning.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: mistral_tokenizer, mistral_v11_tokenizer, _encode_v13, test_mistral_reasoning_v13
  - `tests/reasoning/test_mistral_reasoning_parser.py` removed +0/-348 (348 lines); hunks: -1,348 +0,0; symbols: mistral_tokenizer, test_mistral_reasoning
  - `vllm/reasoning/mistral_reasoning_parser.py` modified +2/-158 (160 lines); hunks: -1,162 +1,6; symbols: MistralReasoningParser, __init__, start_token, end_token
  - `tests/tokenizers_/test_mistral.py` modified +144/-2 (146 lines); hunks: -8,11 +8,13; -1247,7 +1249,9 @@ def test_convert_tokens_to_string(self, mistral_tokenizer:...; symbols: test_convert_tokens_to_string, test_apply_chat_template_reasoning_assistant, test_convert_ids_to_tokens_pre_args_tekken, test_validate_request_params_valid_effort
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -3,767 +3,37 @@
-import json
-from collections.abc import Sequence
-from enum import Enum, auto
-from random import choices
-from string import ascii_letters, digits
-from typing import Any
diff -- tests/parser/mistral/test_reasoning.py
@@ -0,0 +1,599 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import json
+import pytest
+from mistral_common.protocol.instruct.messages import (
+    AssistantMessage,
diff -- tests/reasoning/test_mistral_reasoning_parser.py
@@ -1,348 +0,0 @@
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +26/-756; `vllm/reasoning/mistral_reasoning_parser.py` modified +2/-158; `vllm/tokenizers/mistral.py` modified +15/-6; `vllm/reasoning/__init__.py` modified +1/-1
  - tests: `tests/parser/mistral/test_reasoning.py` added +599/-0; `tests/reasoning/test_mistral_reasoning_parser.py` removed +0/-348; `tests/tokenizers_/test_mistral.py` modified +144/-2; `tests/models/language/generation/test_mistral.py` modified +2/-4
- Risk and verification: The diff ships test coverage in `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #48153 - [Model] Migrate MistralLarge3ForCausalLM to AutoWeightsLoader

- Link: https://github.com/vllm-project/vllm/pull/48153
- Status/date: merged / 2026-07-10
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral_large_3.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; associated commits `fabec87f63cd`
- Diff scope read: GitHub Pull Request files API returned 2 files, +89/-57, 179 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Migrate MistralLarge3ForCausalLM to AutoWeightsLoader"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/model_executor/models/mistral_large_3.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; technical summary: Covers "[Model] Migrate MistralLarge3ForCausalLM to AutoWeightsLoader"; the main implementation surface is `vllm/model_executor/models/mistral_large_3.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral_large_3.py` modified +80/-51 (131 lines); hunks: -2,62 +2,91; symbols: MistralLarge3ForCausalLM, load_weights, _remap_mistral_to_ds, touching `MistralLarge3ForCausalLM, load_weights, _remap_mistral_to_ds`; `vllm/model_executor/models/mistral_large_3_eagle.py` modified +9/-6 (15 lines); hunks: -5,6 +5,7; -22,7 +23,7; symbols: forward, EagleMistralLarge3ForCausalLM, __init__, touching `forward, EagleMistralLarge3ForCausalLM, __init__`.
- Code diff details:
  - `vllm/model_executor/models/mistral_large_3.py` modified +80/-51 (131 lines); hunks: -2,62 +2,91; symbols: MistralLarge3ForCausalLM, load_weights, _remap_mistral_to_ds
  - `vllm/model_executor/models/mistral_large_3_eagle.py` modified +9/-6 (15 lines); hunks: -5,6 +5,7; -22,7 +23,7; symbols: forward, EagleMistralLarge3ForCausalLM, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral_large_3.py
@@ -2,62 +2,91 @@
-import regex as re
+import regex
+from vllm.model_executor.models.utils import AutoWeightsLoader, WeightsMapper
-    # fmt: off
-    remapping = {
-        r"layers\.(\d+)\.attention_norm\.weight": r"model.layers.\1.input_layernorm.weight",  # noqa: E501
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -5,6 +5,7 @@
+import regex
@@ -22,7 +23,7 @@
-from .utils import make_empty_intermediate_tensors_factory, maybe_prefix
+from .utils import WeightsMapper, make_empty_intermediate_tensors_factory, maybe_prefix
@@ -107,11 +108,13 @@ def forward(
-    remapping = MistralLarge3ForCausalLM.remapping | {
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral_large_3.py` modified +80/-51; `vllm/model_executor/models/mistral_large_3_eagle.py` modified +9/-6
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral_large_3.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #47550 - [ROCm][CI][Bugfix] Fix flaky parallel tool-call streaming (test assertion + Mistral/Granite parsers)

- Link: https://github.com/vllm-project/vllm/pull/47550
- Status/date: merged / 2026-07-06
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `5769a7382cb1`
- Diff scope read: GitHub Pull Request files API returned 6 files, +142/-47, 302 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI][Bugfix] Fix flaky parallel tool-call streaming (test assertion + Mistral/Granite parsers)"; model line: Mistral Small 4; category: bug fix; main diff: `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`; technical summary: Covers "[ROCm][CI][Bugfix] Fix flaky parallel tool-call streaming (test assertion + Mistral/Granite parsers)"; the main implementation surface is `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_mistral_tool_parser.py` modified +60/-13 (73 lines); hunks: -144,6 +144,7 @@ def stream_delta_message_generator(; -182,43 +183,53 @@ def stream_delta_message_generator(; symbols: stream_delta_message_generator, test_grammar_from_tool_parser_set_by_adjust_request, test_streaming_pre_v11_parallel_calls_batched_deltas, touching `stream_delta_message_generator, test_grammar_from_tool_parser_set_by_adjust_request, test_streaming_pre_v11_parallel_calls_batched_deltas`; `vllm/tool_parsers/mistral_tool_parser.py` modified +5/-12 (17 lines); hunks: -533,6 +533,7 @@ def update_stream_state_pre_v11_tokenizer(self):; -640,18 +641,10 @@ def _extract_tool_calls_streaming_pre_v11_tokenizer(; symbols: update_stream_state_pre_v11_tokenizer, _extract_tool_calls_streaming_pre_v11_tokenizer, touching `update_stream_state_pre_v11_tokenizer, _extract_tool_calls_streaming_pre_v11_tokenizer`.
- Code diff details:
  - `tests/tool_parsers/test_mistral_tool_parser.py` modified +60/-13 (73 lines); hunks: -144,6 +144,7 @@ def stream_delta_message_generator(; -182,43 +183,53 @@ def stream_delta_message_generator(; symbols: stream_delta_message_generator, test_grammar_from_tool_parser_set_by_adjust_request, test_streaming_pre_v11_parallel_calls_batched_deltas
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +5/-12 (17 lines); hunks: -533,6 +533,7 @@ def update_stream_state_pre_v11_tokenizer(self):; -640,18 +641,10 @@ def _extract_tool_calls_streaming_pre_v11_tokenizer(; symbols: update_stream_state_pre_v11_tokenizer, _extract_tool_calls_streaming_pre_v11_tokenizer
- Key code excerpts:

```diff
diff -- tests/tool_parsers/test_mistral_tool_parser.py
@@ -144,6 +144,7 @@ def stream_delta_message_generator(
+    chunk_size: int = 1,
@@ -182,43 +183,53 @@ def stream_delta_message_generator(
+    pending_text = ""
+    pending_token_ids: list[int] = []
-        delta_token_ids = [delta_token]
-        previous_token_ids = all_token_ids[:i]
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -533,6 +533,7 @@ def update_stream_state_pre_v11_tokenizer(self):
+                self.starting_new_tool = True
@@ -640,18 +641,10 @@ def _extract_tool_calls_streaming_pre_v11_tokenizer(
-            if (
-                (streaming_state_before_parse != self.streaming_state)
-                and streaming_state_before_parse
-                in [StreamingState.WAITING_FOR_TOOL_START, StreamingState.TOOL_COMPLETE]
```

- Reviewed files:
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py` modified +60/-13
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +5/-12
- Risk and verification: The diff ships test coverage in `tests/entrypoints/openai/chat_completion/test_thinking_token_budget.py`, `tests/tool_parsers/test_granite_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py`, `tests/tool_use/test_parallel_tool_calls.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #45217 - [Bugfix] Initialize missing attributes in mistral eagle

- Link: https://github.com/vllm-project/vllm/pull/45217
- Status/date: merged / 2026-06-12
- Trace source: `git log --name-only -- <model-files>` found it through `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; associated commits `6f573f486bc6`
- Diff scope read: GitHub Pull Request files API returned 2 files, +156/-0, 164 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Initialize missing attributes in mistral eagle"; model line: Mistral Small 4; category: bug fix; main diff: `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; technical summary: Covers "[Bugfix] Initialize missing attributes in mistral eagle"; the main implementation surface is `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/model_executor/test_mistral_large_3_eagle.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: DummyPPGroup, DummyEmbedding, __init__, forward, touching `DummyPPGroup, DummyEmbedding, __init__`; `vllm/model_executor/models/mistral_large_3_eagle.py` modified +10/-0 (10 lines); hunks: -75,6 +75,16 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/model_executor/test_mistral_large_3_eagle.py` added +146/-0 (146 lines); hunks: -0,0 +1,146; symbols: DummyPPGroup, DummyEmbedding, __init__, forward
  - `vllm/model_executor/models/mistral_large_3_eagle.py` modified +10/-0 (10 lines); hunks: -75,6 +75,16 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- tests/model_executor/test_mistral_large_3_eagle.py
@@ -0,0 +1,146 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from types import SimpleNamespace
+import pytest
+import torch
+import torch.nn as nn
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -75,6 +75,16 @@ def __init__(
+        # Needed by load_weights
+        qk_nope_head_dim = getattr(config, "qk_nope_head_dim", 0)
+        qk_rope_head_dim = getattr(config, "qk_rope_head_dim", 0)
+        self.use_mha = config.model_type == "deepseek" or all(
+            dim == 0 for dim in (qk_nope_head_dim, qk_rope_head_dim)
+        )
```

- Reviewed files:
  - tests: `tests/model_executor/test_mistral_large_3_eagle.py` added +146/-0
  - runtime: `vllm/model_executor/models/mistral_large_3_eagle.py` modified +10/-0
- Risk and verification: The diff ships test coverage in `tests/model_executor/test_mistral_large_3_eagle.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #44596 - [Refactor][Mistral] Extract parsing logic into MistralParser

- Link: https://github.com/vllm-project/vllm/pull/44596
- Status/date: merged / 2026-06-10
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/parser/mistral.py`, `vllm/reasoning/mistral_reasoning_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `d82ac0092392`
- Diff scope read: GitHub Pull Request files API returned 7 files, +136/-729, 1101 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor][Mistral] Extract parsing logic into MistralParser"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py`; technical summary: Covers "[Refactor][Mistral] Extract parsing logic into MistralParser"; the main implementation surface is `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_mistral_tool_parser.py` modified +0/-385 (385 lines); hunks: -3,7 +3,6; -29,22 +28,17; symbols: test_grammar_from_tool_parser_set_by_adjust_request, test_build_non_streaming_tool_calls, TestExtractMaybeReasoningAndToolStreaming, parser, touching `test_grammar_from_tool_parser_set_by_adjust_request, test_build_non_streaming_tool_calls, TestExtractMaybeReasoningAndToolStreaming`; `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-163 (165 lines); hunks: -5,11 +5,10; -40,19 +39,14; symbols: _is_pre_v11_tokeniser, MistralStreamingResult, MistralToolParser, adjust_request, touching `_is_pre_v11_tokeniser, MistralStreamingResult, MistralToolParser`; `vllm/reasoning/mistral_reasoning_parser.py` modified +10/-1 (11 lines); hunks: -1,7 +1,7; -76,6 +76,15 @@ def is_reasoning_end(self, input_ids: Sequence[int]) -> bool:; symbols: is_reasoning_end, is_reasoning_end_streaming, extract_content_ids, touching `is_reasoning_end, is_reasoning_end_streaming, extract_content_ids`; `vllm/parser/mistral.py` added +77/-0 (77 lines); hunks: -0,0 +1,77; symbols: MistralParser, __init__, _maybe_force_auto_tool_parsing, parse, touching `MistralParser, __init__, _maybe_force_auto_tool_parsing`.
- Code diff details:
  - `tests/tool_parsers/test_mistral_tool_parser.py` modified +0/-385 (385 lines); hunks: -3,7 +3,6; -29,22 +28,17; symbols: test_grammar_from_tool_parser_set_by_adjust_request, test_build_non_streaming_tool_calls, TestExtractMaybeReasoningAndToolStreaming, parser
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-163 (165 lines); hunks: -5,11 +5,10; -40,19 +39,14; symbols: _is_pre_v11_tokeniser, MistralStreamingResult, MistralToolParser, adjust_request
  - `vllm/reasoning/mistral_reasoning_parser.py` modified +10/-1 (11 lines); hunks: -1,7 +1,7; -76,6 +76,15 @@ def is_reasoning_end(self, input_ids: Sequence[int]) -> bool:; symbols: is_reasoning_end, is_reasoning_end_streaming, extract_content_ids
  - `vllm/parser/mistral.py` added +77/-0 (77 lines); hunks: -0,0 +1,77; symbols: MistralParser, __init__, _maybe_force_auto_tool_parsing, parse
- Key code excerpts:

```diff
diff -- tests/tool_parsers/test_mistral_tool_parser.py
@@ -3,7 +3,6 @@
-from typing import Any
@@ -29,22 +28,17 @@
-    DeltaFunctionCall,
-from vllm.entrypoints.openai.engine.protocol import FunctionCall as VllmFunctionCall
-from vllm.reasoning.mistral_reasoning_parser import MistralReasoningParser
-    MistralStreamingResult,
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -5,11 +5,10 @@
-from dataclasses import dataclass
-from typing import TYPE_CHECKING, Any
+from typing import Any
@@ -40,19 +39,14 @@
-from vllm.reasoning.mistral_reasoning_parser import MistralReasoningParser
-from vllm.tokenizers.mistral import MistralTokenizer
diff -- vllm/reasoning/mistral_reasoning_parser.py
@@ -1,7 +1,7 @@
```

- Reviewed files:
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py` modified +0/-385
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-163; `vllm/reasoning/mistral_reasoning_parser.py` modified +10/-1; `vllm/parser/mistral.py` added +77/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_mistral_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #44622 - [Bugfix] Update mistral tokenizer test for continue_final_message fix

- Link: https://github.com/vllm-project/vllm/pull/44622
- Status/date: merged / 2026-06-05
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_mistral.py`; associated commits `d61d8566ec30`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-2, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Update mistral tokenizer test for continue_final_message fix"; model line: Mistral Small 4; category: bug fix; main diff: `tests/tokenizers_/test_mistral.py`; technical summary: Covers "[Bugfix] Update mistral tokenizer test for continue_final_message fix"; the main implementation surface is `tests/tokenizers_/test_mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_mistral.py` modified +2/-2 (4 lines); hunks: -797,11 +797,11 @@ def test_call(self, mistral_tokenizer: MistralTokenizer):; symbols: test_call, touching `test_call`.
- Code diff details:
  - `tests/tokenizers_/test_mistral.py` modified +2/-2 (4 lines); hunks: -797,11 +797,11 @@ def test_call(self, mistral_tokenizer: MistralTokenizer):; symbols: test_call
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_mistral.py
@@ -797,11 +797,11 @@ def test_call(self, mistral_tokenizer: MistralTokenizer):
-                    [1, 3, 22177, 4304, 2662, 4, 22177, 2],
+                    [1, 3, 22177, 4304, 2662, 4, 22177],
-                    ("<s>[INST]Hello world ![/INST]Hello</s>"),
+                    "<s>[INST]Hello world ![/INST]Hello",
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_mistral.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/test_mistral.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41658 - [Mistral Tokenizer] allow more leniency in apply_chat_template

- Link: https://github.com/vllm-project/vllm/pull/41658
- Status/date: merged / 2026-05-06
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `16e336491e96`
- Diff scope read: GitHub Pull Request files API returned 10 files, +144/-397, 675 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Mistral Tokenizer] allow more leniency in apply_chat_template"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; technical summary: Covers "[Mistral Tokenizer] allow more leniency in apply_chat_template"; the main implementation surface is `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_mistral.py` modified +131/-332 (463 lines); hunks: -1,6 +1,7; -11,353 +12,34; symbols: test_prepare_apply_chat_template_tools_and_messages, test_prepare_apply_chat_template_tools_and_messages_list_content, test_prepare_apply_chat_template_generation_prompt_and_continue, test_validate_apply_chat_template_args, touching `test_prepare_apply_chat_template_tools_and_messages, test_prepare_apply_chat_template_tools_and_messages_list_content, test_prepare_apply_chat_template_generation_prompt_and_continue`; `vllm/tokenizers/mistral.py` modified +4/-51 (55 lines); hunks: -13,7 +13,6; -68,36 +67,6 @@ def _pop_unallowed_keys_and_warn(; symbols: _pop_unallowed_keys_and_warn, adapt_inplace_to_mistral_tool, maybe_serialize_tool_calls, truncate_tool_call_ids, touching `_pop_unallowed_keys_and_warn, adapt_inplace_to_mistral_tool, maybe_serialize_tool_calls`; `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-7 (9 lines); hunks: -43,7 +43,7; -241,12 +241,7 @@ def adjust_request(; symbols: adjust_request, touching `adjust_request`.
- Code diff details:
  - `tests/tokenizers_/test_mistral.py` modified +131/-332 (463 lines); hunks: -1,6 +1,7; -11,353 +12,34; symbols: test_prepare_apply_chat_template_tools_and_messages, test_prepare_apply_chat_template_tools_and_messages_list_content, test_prepare_apply_chat_template_generation_prompt_and_continue, test_validate_apply_chat_template_args
  - `vllm/tokenizers/mistral.py` modified +4/-51 (55 lines); hunks: -13,7 +13,6; -68,36 +67,6 @@ def _pop_unallowed_keys_and_warn(; symbols: _pop_unallowed_keys_and_warn, adapt_inplace_to_mistral_tool, maybe_serialize_tool_calls, truncate_tool_call_ids
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-7 (9 lines); hunks: -43,7 +43,7; -241,12 +241,7 @@ def adjust_request(; symbols: adjust_request
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_mistral.py
@@ -1,6 +1,7 @@
+import copy
@@ -11,353 +12,34 @@
-    _prepare_apply_chat_template_tools_and_messages,
+    _validate_apply_chat_template_args,
-@pytest.mark.parametrize(
-    "openai_request,expected_mistral_output",
diff -- vllm/tokenizers/mistral.py
@@ -13,7 +13,6 @@
-from mistral_common.protocol.instruct.tool_calls import Function, Tool
@@ -68,36 +67,6 @@ def _pop_unallowed_keys_and_warn(
-# TODO(juliendenize): remove this once OpenAI API is better supported by
-# `mistral-common`.
-def adapt_inplace_to_mistral_tool(
-    tool: dict[str, Any],
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -43,7 +43,7 @@
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_mistral.py` modified +131/-332
  - runtime: `vllm/tokenizers/mistral.py` modified +4/-51; `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-7
- Risk and verification: The diff ships test coverage in `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt`, `requirements/test/rocm.in`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41730 - [BUGFIX] Support streamed_args_for_tool in MistralToolParser

- Link: https://github.com/vllm-project/vllm/pull/41730
- Status/date: merged / 2026-05-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `c6235ed1803e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +55/-15, 145 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BUGFIX] Support streamed_args_for_tool in MistralToolParser"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py`; technical summary: Covers "[BUGFIX] Support streamed_args_for_tool in MistralToolParser"; the main implementation surface is `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mistral_tool_parser.py` modified +26/-15 (41 lines); hunks: -623,13 +623,6 @@ def _extract_tool_calls_streaming(; -642,6 +635,8 @@ def _generate_delta_tool_call(self, delta_text: str) -> list...; symbols: _extract_tool_calls_streaming, _generate_delta_tool_call, touching `_extract_tool_calls_streaming, _generate_delta_tool_call`; `tests/tool_parsers/test_mistral_tool_parser.py` modified +29/-0 (29 lines); hunks: -590,6 +590,33 @@ def _test_extract_tool_calls_streaming(; -855,6 +882,8 @@ def test_extract_tool_calls_streaming_v11_no_tools(; symbols: _test_extract_tool_calls_streaming, test_extract_tool_calls_streaming_v11_no_tools, touching `_test_extract_tool_calls_streaming, test_extract_tool_calls_streaming_v11_no_tools`.
- Code diff details:
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +26/-15 (41 lines); hunks: -623,13 +623,6 @@ def _extract_tool_calls_streaming(; -642,6 +635,8 @@ def _generate_delta_tool_call(self, delta_text: str) -> list...; symbols: _extract_tool_calls_streaming, _generate_delta_tool_call
  - `tests/tool_parsers/test_mistral_tool_parser.py` modified +29/-0 (29 lines); hunks: -590,6 +590,33 @@ def _test_extract_tool_calls_streaming(; -855,6 +882,8 @@ def test_extract_tool_calls_streaming_v11_no_tools(; symbols: _test_extract_tool_calls_streaming, test_extract_tool_calls_streaming_v11_no_tools
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -623,13 +623,6 @@ def _extract_tool_calls_streaming(
-        # HACK: serving_chat.py inspects the internal state of tool parsers
-        # when determining its final streaming delta, automatically
-        # adding autocompleted JSON.
-        # These two lines avoid that nonsense while ensuring finish_reason
-        # is set to tool_calls when at least one tool is called.
-        if delta_tool_calls and not self.prev_tool_call_arr:
diff -- tests/tool_parsers/test_mistral_tool_parser.py
@@ -590,6 +590,33 @@ def _test_extract_tool_calls_streaming(
+    if expected_tool_calls:
+        assert len(tool_parser.streamed_args_for_tool) == len(expected_tool_calls)
+        assert len(tool_parser.prev_tool_call_arr) == len(expected_tool_calls)
+        for i in range(len(expected_tool_calls)):
+            assert (
+                tool_parser.prev_tool_call_arr[i]["arguments"]
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +26/-15
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py` modified +29/-0
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_mistral_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #41024 - [FEATURE] Add EagleMistralForCausalLM

- Link: https://github.com/vllm-project/vllm/pull/41024
- Status/date: merged / 2026-04-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral_eagle.py`; associated commits `e9f8f31e9a4c`
- Diff scope read: GitHub Pull Request files API returned 3 files, +172/-0, 187 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[FEATURE] Add EagleMistralForCausalLM"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/model_executor/models/mistral_eagle.py`; technical summary: Covers "[FEATURE] Add EagleMistralForCausalLM"; the main implementation surface is `vllm/model_executor/models/mistral_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral_eagle.py` added +166/-0 (166 lines); hunks: -0,0 +1,166; symbols: EagleMistralDecoderLayer, __init__, get_quant_config, EagleMistralModel, touching `EagleMistralDecoderLayer, __init__, get_quant_config`.
- Code diff details:
  - `vllm/model_executor/models/mistral_eagle.py` added +166/-0 (166 lines); hunks: -0,0 +1,166; symbols: EagleMistralDecoderLayer, __init__, get_quant_config, EagleMistralModel
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral_eagle.py
@@ -0,0 +1,166 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Iterable
+import torch
+import torch.nn as nn
+from vllm.compilation.decorators import support_torch_compile
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral_eagle.py` added +166/-0
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39294 - [Bugfix][Parser] Fix Mistral tool parser for HF tokenizers

- Link: https://github.com/vllm-project/vllm/pull/39294
- Status/date: merged / 2026-04-24
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `2ec18f5df43e`
- Diff scope read: GitHub Pull Request files API returned 1 files, +13/-4, 59 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Parser] Fix Mistral tool parser for HF tokenizers"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/tool_parsers/mistral_tool_parser.py`; technical summary: Covers "[Bugfix][Parser] Fix Mistral tool parser for HF tokenizers"; the main implementation surface is `vllm/tool_parsers/mistral_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mistral_tool_parser.py` modified +13/-4 (17 lines); hunks: -91,7 +91,12 @@ def is_valid_id(id: str) -> bool:; -137,15 +142,15 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[T...; symbols: is_valid_id, _is_pre_v11_tokeniser, __init__, extract_tool_calls, touching `is_valid_id, _is_pre_v11_tokeniser, __init__`.
- Code diff details:
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +13/-4 (17 lines); hunks: -91,7 +91,12 @@ def is_valid_id(id: str) -> bool:; -137,15 +142,15 @@ def __init__(self, tokenizer: TokenizerLike, tools: list[T...; symbols: is_valid_id, _is_pre_v11_tokeniser, __init__, extract_tool_calls
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -91,7 +91,12 @@ def is_valid_id(id: str) -> bool:
-    return not (is_mistral_tokenizer(model_tokenizer) and model_tokenizer.version >= 11)
+    if is_mistral_tokenizer(model_tokenizer):
+        return model_tokenizer.version < 11
+    # For HF tokenizers, check if [ARGS] token exists in vocab
+    # which indicates a v11+ equivalent tokenizer
+    vocab: dict[str, int] = getattr(model_tokenizer, "get_vocab", lambda: {})()
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +13/-4
- Risk and verification: Runtime changes concentrate in `vllm/tool_parsers/mistral_tool_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #40043 - [Feature] Avoid eager import of the "mistral_common" package.

- Link: https://github.com/vllm-project/vllm/pull/40043
- Status/date: merged / 2026-04-24
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/utils/mistral.py`; associated commits `56bdf85e10b8`
- Diff scope read: GitHub Pull Request files API returned 5 files, +47/-23, 194 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Avoid eager import of the "mistral_common" package."; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/utils/mistral.py`; technical summary: Covers "[Feature] Avoid eager import of the "mistral_common" package."; the main implementation surface is `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/utils/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-0 (2 lines); hunks: -118,6 +118,8 @@ class MistralToolParser(ToolParser):; symbols: MistralToolParser, touching `MistralToolParser`; `vllm/utils/mistral.py` modified +15/-0 (15 lines); hunks: -12,8 +12,10; -26,3 +28,16 @@ def is_mistral_tokenizer(obj: TokenizerLike | None) -> TypeGu...; symbols: is_mistral_tokenizer, is_mistral_tool_parser, attribute, touching `is_mistral_tokenizer, is_mistral_tool_parser, attribute`.
- Code diff details:
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-0 (2 lines); hunks: -118,6 +118,8 @@ class MistralToolParser(ToolParser):; symbols: MistralToolParser
  - `vllm/utils/mistral.py` modified +15/-0 (15 lines); hunks: -12,8 +12,10; -26,3 +28,16 @@ def is_mistral_tokenizer(obj: TokenizerLike | None) -> TypeGu...; symbols: is_mistral_tokenizer, is_mistral_tool_parser, attribute
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -118,6 +118,8 @@ class MistralToolParser(ToolParser):
+    IS_MISTRAL_TOOL_PARSER = True  # used by vllm.utils.mistral
diff -- vllm/utils/mistral.py
@@ -12,8 +12,10 @@
+    import vllm.tool_parsers.mistral_tool_parser as mtp
+    mtp = LazyLoader("mtp", globals(), "vllm.tool_parsers.mistral_tool_parser")
@@ -26,3 +28,16 @@ def is_mistral_tokenizer(obj: TokenizerLike | None) -> TypeGuard[mt.MistralToken
+def is_mistral_tool_parser(cls: type | None) -> bool:
+    """Return true if *cls* is (a subclass of) MistralToolParser.
+    Uses a class attribute check so that importing
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +2/-0; `vllm/utils/mistral.py` modified +15/-0
- Risk and verification: Runtime changes concentrate in `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/engine/serving.py`, `vllm/entrypoints/serve/render/serving.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #40531 - [Bugfix][Parser] Fix Mistral pre-v11 tool parser failing on trailing model output

- Link: https://github.com/vllm-project/vllm/pull/40531
- Status/date: merged / 2026-04-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `cfa49213d778`
- Diff scope read: GitHub Pull Request files API returned 2 files, +66/-18, 160 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Parser] Fix Mistral pre-v11 tool parser failing on trailing model output"; model line: Mistral Small 4; category: bug fix; main diff: `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`; technical summary: Covers "[Bugfix][Parser] Fix Mistral pre-v11 tool parser failing on trailing model output"; the main implementation surface is `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_mistral_tool_parser.py` modified +49/-9 (58 lines); hunks: -24,7 +24,6; -250,6 +249,7 @@ def test_extract_tool_calls_no_tools(parser_fixture, request):; symbols: test_extract_tool_calls_no_tools, test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls_pre_v11_multiple_bot_tokens_raises, test_extract_tool_calls_pre_v11_regex_fallback_raises, touching `test_extract_tool_calls_no_tools, test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls_pre_v11_multiple_bot_tokens_raises`; `vllm/tool_parsers/mistral_tool_parser.py` modified +17/-9 (26 lines); hunks: -479,21 +479,28 @@ def extract_tool_calls(; -504,7 +511,8 @@ def extract_tool_calls(; symbols: extract_tool_calls, touching `extract_tool_calls`.
- Code diff details:
  - `tests/tool_parsers/test_mistral_tool_parser.py` modified +49/-9 (58 lines); hunks: -24,7 +24,6; -250,6 +249,7 @@ def test_extract_tool_calls_no_tools(parser_fixture, request):; symbols: test_extract_tool_calls_no_tools, test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls_pre_v11_multiple_bot_tokens_raises, test_extract_tool_calls_pre_v11_regex_fallback_raises
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +17/-9 (26 lines); hunks: -479,21 +479,28 @@ def extract_tool_calls(; -504,7 +511,8 @@ def extract_tool_calls(; symbols: extract_tool_calls
- Key code excerpts:

```diff
diff -- tests/tool_parsers/test_mistral_tool_parser.py
@@ -24,7 +24,6 @@
-from pydantic import ValidationError
@@ -250,6 +249,7 @@ def test_extract_tool_calls_no_tools(parser_fixture, request):
+        "trailing_data_after_json",
@@ -338,6 +338,24 @@ def test_extract_tool_calls_no_tools(parser_fixture, request):
+        (
+            """[TOOL_CALLS] [{"name": "get_current_weather", "arguments":{"city": "Dallas", "state": "TX", "unit": "fahrenheit"}}]\nextra trailing data""",  # noqa: E501
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -479,21 +479,28 @@ def extract_tool_calls(
-                tool_calls = json.loads(stringified_tool_calls)
+                # Use raw_decode to parse the first valid JSON value,
+                # ignoring trailing tokens the model may emit after
+                # the tool call array.
+                tool_calls, _ = json.JSONDecoder().raw_decode(stringified_tool_calls)
-                # use a regex to find the part corresponding to the tool call.
```

- Reviewed files:
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py` modified +49/-9
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +17/-9
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_mistral_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39217 - [Mistral Grammar] Fix tool and reasoning parsing

- Link: https://github.com/vllm-project/vllm/pull/39217
- Status/date: merged / 2026-04-16
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tool_use/mistral/test_mistral_tool_calls.py`, `tests/tool_use/mistral/utils.py`, `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `c0722f22de71`
- Diff scope read: GitHub Pull Request files API returned 10 files, +1601/-266, 2396 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Mistral Grammar] Fix tool and reasoning parsing"; model line: Mistral Small 4; category: bug fix; main diff: `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/tokenizers/mistral.py`; technical summary: Covers "[Mistral Grammar] Fix tool and reasoning parsing"; the main implementation surface is `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/tokenizers/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_mistral_tool_parser.py` modified +752/-180 (932 lines); hunks: -3,6 +3,7; -23,24 +24,33; symbols: mistral_pre_v11_tokenizer, stream_delta_message_generator, test_extract_tool_calls_no_tools, touching `mistral_pre_v11_tokenizer, stream_delta_message_generator, test_extract_tool_calls_no_tools`; `vllm/tool_parsers/mistral_tool_parser.py` modified +178/-10 (188 lines); hunks: -1,12 +1,15; -37,14 +40,19; symbols: _is_pre_v11_tokeniser, MistralToolParser, MistralStreamingResult, adjust_request, touching `_is_pre_v11_tokeniser, MistralToolParser, MistralStreamingResult`; `vllm/tokenizers/mistral.py` modified +49/-38 (87 lines); hunks: -54,6 +54,50; -159,44 +203,11 @@ def _prepare_apply_chat_template_tools_and_messages(; symbols: _pop_unallowed_keys_and_warn, adapt_inplace_to_mistral_tool, maybe_serialize_tool_calls, _prepare_apply_chat_template_tools_and_messages, touching `_pop_unallowed_keys_and_warn, adapt_inplace_to_mistral_tool, maybe_serialize_tool_calls`; `tests/tool_use/mistral/test_mistral_tool_calls.py` modified +480/-3 (483 lines); hunks: -1,25 +1,198; -28,3 +201,307 @@ async def test_tool_call_with_tool_choice(client: openai.As...; symbols: _requires_tool_parser, _is_pre_v11, StreamedToolCallResult, _collect_streamed_tool_call, touching `_requires_tool_parser, _is_pre_v11, StreamedToolCallResult`.
- Code diff details:
  - `tests/tool_parsers/test_mistral_tool_parser.py` modified +752/-180 (932 lines); hunks: -3,6 +3,7; -23,24 +24,33; symbols: mistral_pre_v11_tokenizer, stream_delta_message_generator, test_extract_tool_calls_no_tools
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +178/-10 (188 lines); hunks: -1,12 +1,15; -37,14 +40,19; symbols: _is_pre_v11_tokeniser, MistralToolParser, MistralStreamingResult, adjust_request
  - `vllm/tokenizers/mistral.py` modified +49/-38 (87 lines); hunks: -54,6 +54,50; -159,44 +203,11 @@ def _prepare_apply_chat_template_tools_and_messages(; symbols: _pop_unallowed_keys_and_warn, adapt_inplace_to_mistral_tool, maybe_serialize_tool_calls, _prepare_apply_chat_template_tools_and_messages
  - `tests/tool_use/mistral/test_mistral_tool_calls.py` modified +480/-3 (483 lines); hunks: -1,25 +1,198; -28,3 +201,307 @@ async def test_tool_call_with_tool_choice(client: openai.As...; symbols: _requires_tool_parser, _is_pre_v11, StreamedToolCallResult, _collect_streamed_tool_call
  - `tests/tool_use/mistral/utils.py` modified +24/-10 (34 lines); hunks: -2,16 +2,7; -21,6 +12,11 @@ class ServerConfig(TypedDict, total=False):; symbols: ServerConfig
- Key code excerpts:

```diff
diff -- tests/tool_parsers/test_mistral_tool_parser.py
@@ -3,6 +3,7 @@
+from typing import Any
@@ -23,24 +24,33 @@
+from pydantic import ValidationError
+    DeltaFunctionCall,
+    ExtractedToolCallInformation,
+from vllm.entrypoints.openai.engine.protocol import FunctionCall as VllmFunctionCall
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -1,12 +1,15 @@
+from __future__ import annotations
+from dataclasses import dataclass
-from typing import Any
+from typing import TYPE_CHECKING, Any
@@ -37,14 +40,19 @@
+from vllm.reasoning.mistral_reasoning_parser import MistralReasoningParser
diff -- vllm/tokenizers/mistral.py
@@ -54,6 +54,50 @@
```

- Reviewed files:
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py` modified +752/-180; `tests/tool_use/mistral/test_mistral_tool_calls.py` modified +480/-3; `tests/tool_use/mistral/utils.py` modified +24/-10
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +178/-10; `vllm/tokenizers/mistral.py` modified +49/-38
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_mistral_tool_parser.py`, `tests/tool_use/mistral/test_mistral_tool_calls.py`, `tests/tool_use/mistral/utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37292 - Fix Mistral yarn warning in Transformers v5

- Link: https://github.com/vllm-project/vllm/pull/37292
- Status/date: merged / 2026-04-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/mistral.py`; associated commits `edcc37a8cee2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-0, 21 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Mistral yarn warning in Transformers v5"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "Fix Mistral yarn warning in Transformers v5"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` modified +6/-0 (6 lines); hunks: -2,7 +2,9; -134,6 +136,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:; symbols: _remap_mistral_yarn_args, touching `_remap_mistral_yarn_args`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` modified +6/-0 (6 lines); hunks: -2,7 +2,9; -134,6 +136,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:; symbols: _remap_mistral_yarn_args
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -2,7 +2,9 @@
+from packaging.version import Version
+from transformers import __version__ as TRANSFORMERS_VERSION
@@ -134,6 +136,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:
+    # Ignore apply_yarn_scaling in Transformers > v5 RoPE validation to remove warnings
+    if Version(TRANSFORMERS_VERSION) >= Version("5.3.0.dev0"):
+        config["ignore_keys_at_rope_validation"] = {"apply_yarn_scaling"}
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +6/-0
- Risk and verification: Runtime changes concentrate in `vllm/transformers_utils/configs/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #38150 - [Mistral Grammar] Support Grammar Factory

- Link: https://github.com/vllm-project/vllm/pull/38150
- Status/date: merged / 2026-04-06
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_mistral.py`, `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `fef56c18555e`
- Diff scope read: GitHub Pull Request files API returned 10 files, +601/-29, 816 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Mistral Grammar] Support Grammar Factory"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tokenizers_/test_mistral.py`; technical summary: Covers "[Mistral Grammar] Support Grammar Factory"; the main implementation surface is `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tokenizers_/test_mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tool_parsers/test_mistral_tool_parser.py` modified +344/-3 (347 lines); hunks: -3,19 +3,43; -40,6 +64,13 @@ def mistral_tool_parser(mistral_tokenizer):; symbols: mistral_tool_parser, non_mistral_parser, assert_tool_calls, test_fast_detokenization_text_detection_pre_v11, touching `mistral_tool_parser, non_mistral_parser, assert_tool_calls`; `vllm/tool_parsers/mistral_tool_parser.py` modified +133/-9 (142 lines); hunks: -10,6 +10,18; -25,6 +37,7; symbols: StreamingState, MistralToolParser, __init__, adjust_request, touching `StreamingState, MistralToolParser, __init__`; `tests/tokenizers_/test_mistral.py` modified +28/-0 (28 lines); hunks: -3,8 +3,10; -2407,3 +2409,29 @@ def test_convert_ids_to_tokens(; symbols: test_convert_ids_to_tokens, test_grammar_factory, test_llg_tokenizer, touching `test_convert_ids_to_tokens, test_grammar_factory, test_llg_tokenizer`; `vllm/tokenizers/mistral.py` modified +25/-0 (25 lines); hunks: -1,9 +1,12; -45,6 +48,7; symbols: convert_ids_to_tokens, supports_grammar, grammar_factory, llg_tokenizer, touching `convert_ids_to_tokens, supports_grammar, grammar_factory`.
- Code diff details:
  - `tests/tool_parsers/test_mistral_tool_parser.py` modified +344/-3 (347 lines); hunks: -3,19 +3,43; -40,6 +64,13 @@ def mistral_tool_parser(mistral_tokenizer):; symbols: mistral_tool_parser, non_mistral_parser, assert_tool_calls, test_fast_detokenization_text_detection_pre_v11
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +133/-9 (142 lines); hunks: -10,6 +10,18; -25,6 +37,7; symbols: StreamingState, MistralToolParser, __init__, adjust_request
  - `tests/tokenizers_/test_mistral.py` modified +28/-0 (28 lines); hunks: -3,8 +3,10; -2407,3 +2409,29 @@ def test_convert_ids_to_tokens(; symbols: test_convert_ids_to_tokens, test_grammar_factory, test_llg_tokenizer
  - `vllm/tokenizers/mistral.py` modified +25/-0 (25 lines); hunks: -1,9 +1,12; -45,6 +48,7; symbols: convert_ids_to_tokens, supports_grammar, grammar_factory, llg_tokenizer
- Key code excerpts:

```diff
diff -- tests/tool_parsers/test_mistral_tool_parser.py
@@ -3,19 +3,43 @@
+from unittest.mock import MagicMock, patch
-from mistral_common.protocol.instruct.tool_calls import FunctionCall, ToolCall
+from mistral_common.protocol.instruct.tool_calls import (
+    FunctionCall,
+    ToolCall,
+)
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -10,6 +10,18 @@
+from mistral_common.protocol.instruct.tool_calls import (
+    NamedToolChoice as MistralNamedToolChoice,
+)
+from mistral_common.protocol.instruct.tool_calls import (
+    Tool as MistralTool,
+)
diff -- tests/tokenizers_/test_mistral.py
@@ -3,8 +3,10 @@
```

- Reviewed files:
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py` modified +344/-3; `tests/tokenizers_/test_mistral.py` modified +28/-0
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +133/-9; `vllm/tokenizers/mistral.py` modified +25/-0
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/test_mistral.py`, `tests/tool_parsers/test_mistral_tool_parser.py`, `tests/v1/structured_output/test_backend_guidance.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36928 - [LoRA][BugFix] Fix skipped LoRA adapters for Mistral3

- Link: https://github.com/vllm-project/vllm/pull/36928
- Status/date: merged / 2026-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `5bc1da147fb0`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-0, 10 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[LoRA][BugFix] Fix skipped LoRA adapters for Mistral3"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[LoRA][BugFix] Fix skipped LoRA adapters for Mistral3"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` modified +3/-0 (3 lines); hunks: -429,6 +429,9 @@ class Mistral3ForConditionalGeneration(; symbols: Mistral3ForConditionalGeneration, touching `Mistral3ForConditionalGeneration`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` modified +3/-0 (3 lines); hunks: -429,6 +429,9 @@ class Mistral3ForConditionalGeneration(; symbols: Mistral3ForConditionalGeneration
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -429,6 +429,9 @@ class Mistral3ForConditionalGeneration(
+            # Some PEFT LoRAs are trained against the text submodule directly
+            # and produce names like `base_model.model.model.layers.*`.
+            "model.": "language_model.model.",
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37209 - Fix some Mistral parser issues

- Link: https://github.com/vllm-project/vllm/pull/37209
- Status/date: merged / 2026-03-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `5db91f0aaf35`
- Diff scope read: GitHub Pull Request files API returned 3 files, +42/-34, 147 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix some Mistral parser issues"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; technical summary: Covers "Fix some Mistral parser issues"; the main implementation surface is `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tokenizers/mistral.py` modified +27/-26 (53 lines); hunks: -15,8 +15,15; -26,21 +33,20; symbols: from_pretrained, __init__, convert_tokens_to_ids, touching `from_pretrained, __init__, convert_tokens_to_ids`; `vllm/tool_parsers/mistral_tool_parser.py` modified +7/-3 (10 lines); hunks: -241,7 +241,10 @@ def extract_tool_calls_streaming(; -275,7 +278,8 @@ def _extract_tool_calls_streaming(; symbols: extract_tool_calls_streaming, _extract_tool_calls_streaming, _extract_tool_calls_streaming_pre_v11_tokenizer, touching `extract_tool_calls_streaming, _extract_tool_calls_streaming, _extract_tool_calls_streaming_pre_v11_tokenizer`.
- Code diff details:
  - `vllm/tokenizers/mistral.py` modified +27/-26 (53 lines); hunks: -15,8 +15,15; -26,21 +33,20; symbols: from_pretrained, __init__, convert_tokens_to_ids
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +7/-3 (10 lines); hunks: -241,7 +241,10 @@ def extract_tool_calls_streaming(; -275,7 +278,8 @@ def _extract_tool_calls_streaming(; symbols: extract_tool_calls_streaming, _extract_tool_calls_streaming, _extract_tool_calls_streaming_pre_v11_tokenizer
- Key code excerpts:

```diff
diff -- vllm/tokenizers/mistral.py
@@ -15,8 +15,15 @@
+    Tokenizer,
+)
+from mistral_common.tokens.tokenizers.instruct import (
+    InstructTokenizerBase,
+    InstructTokenizerV13,
+)
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -241,7 +241,10 @@ def extract_tool_calls_streaming(
-        if self.bot_token_id not in current_token_ids:
+        has_bot_token = (
+            self.bot_token_id in current_token_ids or self.bot_token in current_text
+        )
+        if not has_bot_token:
@@ -275,7 +278,8 @@ def _extract_tool_calls_streaming(
```

- Reviewed files:
  - runtime: `vllm/tokenizers/mistral.py` modified +27/-26; `vllm/tool_parsers/mistral_tool_parser.py` modified +7/-3
- Risk and verification: Runtime changes concentrate in `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37232 - Fix EagleMistralLarge3Model initialization

- Link: https://github.com/vllm-project/vllm/pull/37232
- Status/date: merged / 2026-03-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral_large_3_eagle.py`; associated commits `7961486a9b74`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix EagleMistralLarge3Model initialization"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/model_executor/models/mistral_large_3_eagle.py`; technical summary: Covers "Fix EagleMistralLarge3Model initialization"; the main implementation surface is `vllm/model_executor/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral_large_3_eagle.py` modified +1/-0 (1 lines); hunks: -74,6 +74,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/mistral_large_3_eagle.py` modified +1/-0 (1 lines); hunks: -74,6 +74,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -74,6 +74,7 @@ def __init__(
+        self.aux_hidden_state_layers: tuple[int, ...] = ()
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral_large_3_eagle.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral_large_3_eagle.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #37104 - Patch Mistral config

- Link: https://github.com/vllm-project/vllm/pull/37104
- Status/date: merged / 2026-03-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/mistral.py`; associated commits `ffbc2e5bdbfb`
- Diff scope read: GitHub Pull Request files API returned 3 files, +49/-30, 162 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Patch Mistral config"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "Patch Mistral config"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` modified +10/-7 (17 lines); hunks: -113,12 +113,13 @@ def _remap_mistral_vision_args(config: dict) -> dict:; -128,9 +129,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:; symbols: _remap_mistral_vision_args, _remap_mistral_yarn_args, _remap_general_mistral_args, touching `_remap_mistral_vision_args, _remap_mistral_yarn_args, _remap_general_mistral_args`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` modified +10/-7 (17 lines); hunks: -113,12 +113,13 @@ def _remap_mistral_vision_args(config: dict) -> dict:; -128,9 +129,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:; symbols: _remap_mistral_vision_args, _remap_mistral_yarn_args, _remap_general_mistral_args
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -113,12 +113,13 @@ def _remap_mistral_vision_args(config: dict) -> dict:
-        "factor": "factor",
-        "original_max_position_embeddings": "original_max_position_embeddings",
-        "beta": "beta_fast",
-        "alpha": "beta_slow",
-        "apply_scale": "apply_yarn_scaling",
+        "factor": ("factor", float),
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +10/-7
- Risk and verification: Runtime changes concentrate in `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/mistral.py`, `vllm/transformers_utils/model_arch_config_convertor.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36971 - Mistral common v10

- Link: https://github.com/vllm-project/vllm/pull/36971
- Status/date: merged / 2026-03-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tokenizers/mistral.py`; associated commits `e42b49bd69d4`
- Diff scope read: GitHub Pull Request files API returned 4 files, +22/-3, 74 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Mistral common v10"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/tokenizers/mistral.py`; technical summary: Covers "Mistral common v10"; the main implementation surface is `vllm/tokenizers/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tokenizers/mistral.py` modified +19/-0 (19 lines); hunks: -7,6 +7,9; -192,6 +195,15 @@ def validate_request_params(request: "ChatCompletionRequest"):; symbols: validate_request_params, _tekken_token_to_id, apply_chat_template, decode, touching `validate_request_params, _tekken_token_to_id, apply_chat_template`.
- Code diff details:
  - `vllm/tokenizers/mistral.py` modified +19/-0 (19 lines); hunks: -7,6 +7,9; -192,6 +195,15 @@ def validate_request_params(request: "ChatCompletionRequest"):; symbols: validate_request_params, _tekken_token_to_id, apply_chat_template, decode
- Key code excerpts:

```diff
diff -- vllm/tokenizers/mistral.py
@@ -7,6 +7,9 @@
+from mistral_common.protocol.instruct.request import (
+    ReasoningEffort,
+)
@@ -192,6 +195,15 @@ def validate_request_params(request: "ChatCompletionRequest"):
+    if request.reasoning_effort and request.reasoning_effort not in list(
+        ReasoningEffort
```

- Reviewed files:
  - runtime: `vllm/tokenizers/mistral.py` modified +19/-0
- Risk and verification: Runtime changes concentrate in `vllm/tokenizers/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #36163 - Add support to Mistral large 3 eagle with dense layers

- Link: https://github.com/vllm-project/vllm/pull/36163
- Status/date: merged / 2026-03-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral_large_3_eagle.py`, `vllm/transformers_utils/configs/mistral.py`; associated commits `afebeffbfbf2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +28/-1, 61 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add support to Mistral large 3 eagle with dense layers"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/transformers_utils/configs/mistral.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`; technical summary: Covers "Add support to Mistral large 3 eagle with dense layers"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` modified +23/-0 (23 lines); hunks: -19,6 +19,10 @@ def adapt_config_dict(; -291,3 +295,22 @@ def _remap_moe_args(config: dict) -> dict:; symbols: adapt_config_dict, _remap_moe_args, _remap_mistral_mla_args, touching `adapt_config_dict, _remap_moe_args, _remap_mistral_mla_args`; `vllm/model_executor/models/mistral_large_3_eagle.py` modified +5/-1 (6 lines); hunks: -1,6 +1,7; -33,7 +34,9 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` modified +23/-0 (23 lines); hunks: -19,6 +19,10 @@ def adapt_config_dict(; -291,3 +295,22 @@ def _remap_moe_args(config: dict) -> dict:; symbols: adapt_config_dict, _remap_moe_args, _remap_mistral_mla_args
  - `vllm/model_executor/models/mistral_large_3_eagle.py` modified +5/-1 (6 lines); hunks: -1,6 +1,7; -33,7 +34,9 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -19,6 +19,10 @@ def adapt_config_dict(
+    is_mla = bool(config_dict.get("qk_nope_head_dim"))
+    if is_mla:
+        config_dict = _remap_mistral_mla_args(config_dict)
@@ -291,3 +295,22 @@ def _remap_moe_args(config: dict) -> dict:
+def _remap_mistral_mla_args(config: dict) -> dict:
+    if not config.get("moe"):
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -1,6 +1,7 @@
+import copy
@@ -33,7 +34,9 @@ def __init__(
-        config = vllm_config.model_config.hf_config
+        config = copy.deepcopy(vllm_config.model_config.hf_config)
+        config.first_k_dense_replace += start_layer_id
@@ -53,6 +56,7 @@ def __init__(
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +23/-0; `vllm/model_executor/models/mistral_large_3_eagle.py` modified +5/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral_large_3_eagle.py`, `vllm/transformers_utils/configs/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #34651 - [Feature] Lazy import for the "mistral" tokenizer module.

- Link: https://github.com/vllm-project/vllm/pull/34651
- Status/date: merged / 2026-02-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tokenizers/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/utils/mistral.py`; associated commits `54e2f83d0a82`
- Diff scope read: GitHub Pull Request files API returned 14 files, +68/-48, 399 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Lazy import for the "mistral" tokenizer module."; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/tokenizers/mistral.py`, `vllm/utils/mistral.py`; technical summary: Covers "[Feature] Lazy import for the "mistral" tokenizer module."; the main implementation surface is `vllm/tool_parsers/mistral_tool_parser.py`, `vllm/tokenizers/mistral.py`, `vllm/utils/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mistral_tool_parser.py` modified +4/-6 (10 lines); hunks: -25,10 +25,10; -66,9 +66,7 @@ def is_valid_id(id: str) -> bool:; symbols: is_valid_id, _is_pre_v11_tokeniser, MistralToolParser, __init__, touching `is_valid_id, _is_pre_v11_tokeniser, MistralToolParser`; `vllm/tokenizers/mistral.py` modified +2/-0 (2 lines); hunks: -210,6 +210,8 @@ def _tekken_token_to_id(tokenizer: "Tekkenizer", t: str | by...; symbols: _tekken_token_to_id, MistralTokenizer, from_pretrained, touching `_tekken_token_to_id, MistralTokenizer, from_pretrained`; `vllm/utils/mistral.py` added +28/-0 (28 lines); hunks: -0,0 +1,28; symbols: is_mistral_tokenizer, attribute, touching `is_mistral_tokenizer, attribute`.
- Code diff details:
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +4/-6 (10 lines); hunks: -25,10 +25,10; -66,9 +66,7 @@ def is_valid_id(id: str) -> bool:; symbols: is_valid_id, _is_pre_v11_tokeniser, MistralToolParser, __init__
  - `vllm/tokenizers/mistral.py` modified +2/-0 (2 lines); hunks: -210,6 +210,8 @@ def _tekken_token_to_id(tokenizer: "Tekkenizer", t: str | by...; symbols: _tekken_token_to_id, MistralTokenizer, from_pretrained
  - `vllm/utils/mistral.py` added +28/-0 (28 lines); hunks: -0,0 +1,28; symbols: is_mistral_tokenizer, attribute
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -25,10 +25,10 @@
-from vllm.tokenizers.mistral import MistralTokenizer
+from vllm.utils.mistral import is_mistral_tokenizer
@@ -66,9 +66,7 @@ def is_valid_id(id: str) -> bool:
-    return not (
-        isinstance(model_tokenizer, MistralTokenizer) and model_tokenizer.version >= 11
-    )
diff -- vllm/tokenizers/mistral.py
@@ -210,6 +210,8 @@ def _tekken_token_to_id(tokenizer: "Tekkenizer", t: str | bytes) -> int:
+    IS_MISTRAL_TOKENIZER = True  # used by vllm.utils.mistral
diff -- vllm/utils/mistral.py
@@ -0,0 +1,28 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Provides lazy import of the vllm.tokenizers.mistral module."""
+from __future__ import annotations
+from typing import TYPE_CHECKING, TypeGuard
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +4/-6; `vllm/tokenizers/mistral.py` modified +2/-0; `vllm/utils/mistral.py` added +28/-0
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_common.py`, `tests/reasoning/utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #34104 - Fix Mistral config remap to accept compressed-tensors quantization #34028

- Link: https://github.com/vllm-project/vllm/pull/34104
- Status/date: merged / 2026-02-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/mistral.py`; associated commits `f5897613fb27`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-0, 15 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Mistral config remap to accept compressed-tensors quantization #34028"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "Fix Mistral config remap to accept compressed-tensors quantization #34028"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` modified +8/-0 (8 lines); hunks: -198,6 +198,14 @@ def _remap_mistral_quantization_args(config: dict) -> dict:; symbols: _remap_mistral_quantization_args, touching `_remap_mistral_quantization_args`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` modified +8/-0 (8 lines); hunks: -198,6 +198,14 @@ def _remap_mistral_quantization_args(config: dict) -> dict:; symbols: _remap_mistral_quantization_args
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -198,6 +198,14 @@ def _remap_mistral_quantization_args(config: dict) -> dict:
+        elif (
+            str(quantization.get("quant_method", "")).lower().replace("_", "-")
+            == "compressed-tensors"
+        ):
+            # Pass through compressed-tensors config, while normalizing
+            # quant_method to the canonical community spelling.
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +8/-0
- Risk and verification: Runtime changes concentrate in `vllm/transformers_utils/configs/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #33939 - Enable Eagle3 speculative decoding for Mistral3ForConditionalGeneration to support eagle3

- Link: https://github.com/vllm-project/vllm/pull/33939
- Status/date: merged / 2026-02-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `4df44c16ba8c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-1, 31 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Enable Eagle3 speculative decoding for Mistral3ForConditionalGeneration to support eagle3"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "Enable Eagle3 speculative decoding for Mistral3ForConditionalGeneration to support eagle3"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` modified +9/-1 (10 lines); hunks: -44,6 +44,7; -408,7 +409,7 @@ def init_vision_tower_for_llava(; symbols: init_vision_tower_for_llava, Mistral3ForConditionalGeneration, get_placeholder_str, set_aux_hidden_state_layers, touching `init_vision_tower_for_llava, Mistral3ForConditionalGeneration, get_placeholder_str`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` modified +9/-1 (10 lines); hunks: -44,6 +44,7; -408,7 +409,7 @@ def init_vision_tower_for_llava(; symbols: init_vision_tower_for_llava, Mistral3ForConditionalGeneration, get_placeholder_str, set_aux_hidden_state_layers
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -44,6 +44,7 @@
+    SupportsEagle3,
@@ -408,7 +409,7 @@ def init_vision_tower_for_llava(
-    nn.Module, SupportsLoRA, SupportsMultiModal, SupportsPP
+    nn.Module, SupportsLoRA, SupportsMultiModal, SupportsPP, SupportsEagle3
@@ -432,6 +433,13 @@ def get_placeholder_str(cls, modality: str, i: int) -> str | None:
+    def set_aux_hidden_state_layers(self, layers: tuple[int, ...]) -> None:
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` modified +9/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #33521 - Fix mistral sliding window parsing

- Link: https://github.com/vllm-project/vllm/pull/33521
- Status/date: merged / 2026-02-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/mistral.py`; associated commits `beb889948276`
- Diff scope read: GitHub Pull Request files API returned 2 files, +25/-22, 82 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix mistral sliding window parsing"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "Fix mistral sliding window parsing"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` modified +25/-9 (34 lines); hunks: -14,6 +14,7 @@ def adapt_config_dict(; -161,6 +162,29 @@ def _remap_general_mistral_args(config: dict) -> dict:; symbols: adapt_config_dict, _remap_general_mistral_args, _remap_mistral_sliding_window, _remap_mistral_quantization_args, touching `adapt_config_dict, _remap_general_mistral_args, _remap_mistral_sliding_window`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` modified +25/-9 (34 lines); hunks: -14,6 +14,7 @@ def adapt_config_dict(; -161,6 +162,29 @@ def _remap_general_mistral_args(config: dict) -> dict:; symbols: adapt_config_dict, _remap_general_mistral_args, _remap_mistral_sliding_window, _remap_mistral_quantization_args
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -14,6 +14,7 @@ def adapt_config_dict(
+    config_dict = _remap_mistral_sliding_window(config_dict)
@@ -161,6 +162,29 @@ def _remap_general_mistral_args(config: dict) -> dict:
+def _remap_mistral_sliding_window(config: dict) -> dict:
+    # Remap sliding_window (list) -> layer_types (list) + sliding window (int)
+    # for HF compatibility
+    # Mistral configs may define sliding_window as list[int]. Convert it
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +25/-9
- Risk and verification: Runtime changes concentrate in `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #33095 - Remove unused logic in `models/mistral.py`

- Link: https://github.com/vllm-project/vllm/pull/33095
- Status/date: merged / 2026-01-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral.py`; associated commits `d56afd45fd4e`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-8, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Remove unused logic in `models/mistral.py`"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/model_executor/models/mistral.py`; technical summary: Covers "Remove unused logic in `models/mistral.py`"; the main implementation surface is `vllm/model_executor/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral.py` modified +0/-8 (8 lines); hunks: -156,16 +156,8 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/model_executor/models/mistral.py` modified +0/-8 (8 lines); hunks: -156,16 +156,8 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral.py
@@ -156,16 +156,8 @@ def __init__(
-        quant_config = self.get_quant_config(vllm_config)
-        do_fusion = getattr(
-            quant_config, "enable_quantization_scaling_fusion", False
-        ) and vllm_config.cache_config.cache_dtype.startswith("fp8")
-        if do_fusion:
-            self.input_layernorm.quant_scaling_from = self.self_attn.qkv_proj
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral.py` modified +0/-8
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #32780 - [Llama.py -> mistral.py] Extract mistral-only relevant code into separate file

- Link: https://github.com/vllm-project/vllm/pull/32780
- Status/date: merged / 2026-01-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral.py`; associated commits `1579c9b5fd0f`
- Diff scope read: GitHub Pull Request files API returned 3 files, +248/-115, 426 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Llama.py -> mistral.py] Extract mistral-only relevant code into separate file"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/model_executor/models/mistral.py`; technical summary: Covers "[Llama.py -> mistral.py] Extract mistral-only relevant code into separate file"; the main implementation surface is `vllm/model_executor/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral.py` added +242/-0 (242 lines); hunks: -0,0 +1,242; symbols: MistralAttention, __init__, _get_llama_4_attn_scale, forward, touching `MistralAttention, __init__, _get_llama_4_attn_scale`.
- Code diff details:
  - `vllm/model_executor/models/mistral.py` added +242/-0 (242 lines); hunks: -0,0 +1,242; symbols: MistralAttention, __init__, _get_llama_4_attn_scale, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral.py
@@ -0,0 +1,242 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Mistral adaptation of the LLaMA architecture."""
+from collections.abc import Iterable
+import torch
+from torch import nn
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral.py` added +242/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/mistral.py`, `vllm/model_executor/models/registry.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #31138 - [Mistral common] Ensure all functions are imported from the top & only use public methods

- Link: https://github.com/vllm-project/vllm/pull/31138
- Status/date: merged / 2025-12-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tokenizers/mistral.py`; associated commits `48e744976cf4`
- Diff scope read: GitHub Pull Request files API returned 5 files, +24/-57, 181 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Mistral common] Ensure all functions are imported from the top & only use public methods"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/tokenizers/mistral.py`; technical summary: Covers "[Mistral common] Ensure all functions are imported from the top & only use public methods"; the main implementation surface is `vllm/tokenizers/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tokenizers/mistral.py` modified +20/-53 (73 lines); hunks: -3,17 +3,28; -101,8 +112,6 @@ def _prepare_apply_chat_template_tools_and_messages(; symbols: _prepare_apply_chat_template_tools_and_messages, validate_request_params, _tekken_token_to_id, from_pretrained, touching `_prepare_apply_chat_template_tools_and_messages, validate_request_params, _tekken_token_to_id`.
- Code diff details:
  - `vllm/tokenizers/mistral.py` modified +20/-53 (73 lines); hunks: -3,17 +3,28; -101,8 +112,6 @@ def _prepare_apply_chat_template_tools_and_messages(; symbols: _prepare_apply_chat_template_tools_and_messages, validate_request_params, _tekken_token_to_id, from_pretrained
- Key code excerpts:

```diff
diff -- vllm/tokenizers/mistral.py
@@ -3,17 +3,28 @@
+from mistral_common.protocol.instruct.request import (
+    ChatCompletionRequest as MistralChatCompletionRequest,
+)
+from mistral_common.protocol.instruct.tool_calls import Function, Tool
+from mistral_common.protocol.instruct.validator import ValidationMode
+from mistral_common.tokens.tokenizers.base import (
```

- Reviewed files:
  - runtime: `vllm/tokenizers/mistral.py` modified +20/-53
- Risk and verification: Runtime changes concentrate in `vllm/tokenizers/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #30724 - Fix edge case Mistral tool parser

- Link: https://github.com/vllm-project/vllm/pull/30724
- Status/date: merged / 2025-12-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/tool_parsers/mistral_tool_parser.py`; associated commits `38c361f99dff`
- Diff scope read: GitHub Pull Request files API returned 2 files, +115/-56, 224 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix edge case Mistral tool parser"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py`; technical summary: Covers "Fix edge case Mistral tool parser"; the main implementation surface is `vllm/tool_parsers/mistral_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tool_parsers/mistral_tool_parser.py` modified +81/-54 (135 lines); hunks: -131,78 +131,105 @@ def extract_tool_calls(; symbols: extract_tool_calls, extract_tool_calls_streaming, touching `extract_tool_calls, extract_tool_calls_streaming`; `tests/tool_parsers/test_mistral_tool_parser.py` modified +34/-2 (36 lines); hunks: -281,6 +281,8 @@ def test_extract_tool_calls_pre_v11_tokenizer(; -326,6 +328,36 @@ def test_extract_tool_calls_pre_v11_tokenizer(; symbols: test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls, test_extract_tool_calls_streaming, touching `test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls, test_extract_tool_calls_streaming`.
- Code diff details:
  - `vllm/tool_parsers/mistral_tool_parser.py` modified +81/-54 (135 lines); hunks: -131,78 +131,105 @@ def extract_tool_calls(; symbols: extract_tool_calls, extract_tool_calls_streaming
  - `tests/tool_parsers/test_mistral_tool_parser.py` modified +34/-2 (36 lines); hunks: -281,6 +281,8 @@ def test_extract_tool_calls_pre_v11_tokenizer(; -326,6 +328,36 @@ def test_extract_tool_calls_pre_v11_tokenizer(; symbols: test_extract_tool_calls_pre_v11_tokenizer, test_extract_tool_calls, test_extract_tool_calls_streaming
- Key code excerpts:

```diff
diff -- vllm/tool_parsers/mistral_tool_parser.py
@@ -131,78 +131,105 @@ def extract_tool_calls(
-        Extract the tool calls from a complete model response. Requires
-        find-and-replacing single quotes with double quotes for JSON parsing,
-        make sure your tool call arguments don't ever include quotes!
+        Extract the tool calls from a complete model response.
+        Content and tool calls formatting depends on the Mistral's tokenizer version
+        used to train the model:
diff -- tests/tool_parsers/test_mistral_tool_parser.py
@@ -281,6 +281,8 @@ def test_extract_tool_calls_pre_v11_tokenizer(
+        "complex",
+        "wrong_json",
@@ -326,6 +328,36 @@ def test_extract_tool_calls_pre_v11_tokenizer(
+        (
+            # Complex
+            """hi{hi[TOOL_CALLS]bash{"command": "print(\\"hello world!\\")\\nre.compile(r\'{}\')""",  # noqa: E501
```

- Reviewed files:
  - runtime: `vllm/tool_parsers/mistral_tool_parser.py` modified +81/-54
  - tests: `tests/tool_parsers/test_mistral_tool_parser.py` modified +34/-2
- Risk and verification: The diff ships test coverage in `tests/tool_parsers/test_mistral_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #30391 - [IMPROVEMENT] Change MistralReasoningParser behavior

- Link: https://github.com/vllm-project/vllm/pull/30391
- Status/date: merged / 2025-12-11
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/reasoning/mistral_reasoning_parser.py`; associated commits `aa3c250c487e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +186/-64, 383 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[IMPROVEMENT] Change MistralReasoningParser behavior"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/reasoning/test_mistral_reasoning_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py`; technical summary: Covers "[IMPROVEMENT] Change MistralReasoningParser behavior"; the main implementation surface is `tests/reasoning/test_mistral_reasoning_parser.py`, `vllm/reasoning/mistral_reasoning_parser.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/reasoning/test_mistral_reasoning_parser.py` modified +84/-61 (145 lines); hunks: -18,47 +18,53 @@ def mistral_tokenizer():; -78,17 +84,17 @@ def mistral_tokenizer():; symbols: mistral_tokenizer, touching `mistral_tokenizer`; `vllm/reasoning/mistral_reasoning_parser.py` modified +102/-3 (105 lines); hunks: -3,20 +3,29; -53,3 +62,93 @@ def end_token(self) -> str:; symbols: MistralReasoningParser, __init__, end_token, is_reasoning_end, touching `MistralReasoningParser, __init__, end_token`.
- Code diff details:
  - `tests/reasoning/test_mistral_reasoning_parser.py` modified +84/-61 (145 lines); hunks: -18,47 +18,53 @@ def mistral_tokenizer():; -78,17 +84,17 @@ def mistral_tokenizer():; symbols: mistral_tokenizer
  - `vllm/reasoning/mistral_reasoning_parser.py` modified +102/-3 (105 lines); hunks: -3,20 +3,29; -53,3 +62,93 @@ def end_token(self) -> str:; symbols: MistralReasoningParser, __init__, end_token, is_reasoning_end
- Key code excerpts:

```diff
diff -- tests/reasoning/test_mistral_reasoning_parser.py
@@ -18,47 +18,53 @@ def mistral_tokenizer():
-SIMPLE_REASONING = {
+INVALID_SIMPLE_REASONING = {
-    "reasoning": "This is a reasoning section",
-    "content": "This is the rest",
-    "is_reasoning_end": True,
+    "reasoning": None,
diff -- vllm/reasoning/mistral_reasoning_parser.py
@@ -3,20 +3,29 @@
+from vllm.entrypoints.openai.protocol import (
+    ChatCompletionRequest,
+    ResponsesRequest,
+)
-from vllm.reasoning.deepseek_r1_reasoning_parser import DeepSeekR1ReasoningParser
+from vllm.reasoning.basic_parsers import BaseThinkingReasoningParser
```

- Reviewed files:
  - tests: `tests/reasoning/test_mistral_reasoning_parser.py` modified +84/-61
  - runtime: `vllm/reasoning/mistral_reasoning_parser.py` modified +102/-3
- Risk and verification: The diff ships test coverage in `tests/reasoning/test_mistral_reasoning_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29918 - [BUGFIX] Fix regex pattern for Mistral Tool Call

- Link: https://github.com/vllm-project/vllm/pull/29918
- Status/date: merged / 2025-12-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/language/generation/test_mistral.py`; associated commits `1b1e35aaf9d9`
- Diff scope read: GitHub Pull Request files API returned 2 files, +36/-1, 48 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BUGFIX] Fix regex pattern for Mistral Tool Call"; model line: Mistral Small 4; category: bug fix; main diff: `tests/models/language/generation/test_mistral.py`; technical summary: Covers "[BUGFIX] Fix regex pattern for Mistral Tool Call"; the main implementation surface is `tests/models/language/generation/test_mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/language/generation/test_mistral.py` modified +35/-0 (35 lines); hunks: -315,3 +315,38 @@ def get_vocab():; symbols: get_vocab, touching `get_vocab`.
- Code diff details:
  - `tests/models/language/generation/test_mistral.py` modified +35/-0 (35 lines); hunks: -315,3 +315,38 @@ def get_vocab():; symbols: get_vocab
- Key code excerpts:

```diff
diff -- tests/models/language/generation/test_mistral.py
@@ -315,3 +315,38 @@ def get_vocab():
+    # multiple calls
+    multiple_args_dict = [
+        {
+            "city": "Dallas",
+            "state": "TX",
+            "unit": "fahrenheit",
```

- Reviewed files:
  - tests: `tests/models/language/generation/test_mistral.py` modified +35/-0
- Risk and verification: The diff ships test coverage in `tests/models/language/generation/test_mistral.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29757 - Add Mistral Large 3 and Ministral 3

- Link: https://github.com/vllm-project/vllm/pull/29757
- Status/date: merged / 2025-12-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_mistral.py`, `vllm/model_executor/models/mistral_large_3.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`, `vllm/tokenizers/mistral.py`, `vllm/transformers_utils/configs/mistral.py`; associated commits `d8c6210eeaa7`
- Diff scope read: GitHub Pull Request files API returned 16 files, +724/-30, 1015 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add Mistral Large 3 and Ministral 3"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `vllm/model_executor/models/mistral_large_3_eagle.py`, `tests/tokenizers_/test_mistral.py`, `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "Add Mistral Large 3 and Ministral 3"; the main implementation surface is `vllm/model_executor/models/mistral_large_3_eagle.py`, `tests/tokenizers_/test_mistral.py`, `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral_large_3_eagle.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: EagleMistralLarge3Model, __init__, forward, EagleMistralLarge3ForCausalLM, touching `EagleMistralLarge3Model, __init__, forward`; `tests/tokenizers_/test_mistral.py` modified +151/-7 (158 lines); hunks: -91,6 +91,118; -1108,13 +1220,6 @@ def test_decode(; symbols: test_prepare_apply_chat_template_tools_and_messages, test_decode, test_decode_empty, test_decode_int, touching `test_prepare_apply_chat_template_tools_and_messages, test_decode, test_decode_empty`; `vllm/transformers_utils/configs/mistral.py` modified +62/-12 (74 lines); hunks: -18,9 +18,31 @@ def adapt_config_dict(; -140,17 +162,20 @@ def _remap_general_mistral_args(config: dict) -> dict:; symbols: adapt_config_dict, _remap_general_mistral_args, _remap_mistral_quantization_args, _remap_mistral_audio_args, touching `adapt_config_dict, _remap_general_mistral_args, _remap_mistral_quantization_args`; `vllm/model_executor/models/mistral_large_3.py` added +63/-0 (63 lines); hunks: -0,0 +1,63; symbols: MistralLarge3ForCausalLM, load_weights, _remap_mistral_to_ds, touching `MistralLarge3ForCausalLM, load_weights, _remap_mistral_to_ds`.
- Code diff details:
  - `vllm/model_executor/models/mistral_large_3_eagle.py` added +165/-0 (165 lines); hunks: -0,0 +1,165; symbols: EagleMistralLarge3Model, __init__, forward, EagleMistralLarge3ForCausalLM
  - `tests/tokenizers_/test_mistral.py` modified +151/-7 (158 lines); hunks: -91,6 +91,118; -1108,13 +1220,6 @@ def test_decode(; symbols: test_prepare_apply_chat_template_tools_and_messages, test_decode, test_decode_empty, test_decode_int
  - `vllm/transformers_utils/configs/mistral.py` modified +62/-12 (74 lines); hunks: -18,9 +18,31 @@ def adapt_config_dict(; -140,17 +162,20 @@ def _remap_general_mistral_args(config: dict) -> dict:; symbols: adapt_config_dict, _remap_general_mistral_args, _remap_mistral_quantization_args, _remap_mistral_audio_args
  - `vllm/model_executor/models/mistral_large_3.py` added +63/-0 (63 lines); hunks: -0,0 +1,63; symbols: MistralLarge3ForCausalLM, load_weights, _remap_mistral_to_ds
  - `vllm/tokenizers/mistral.py` modified +36/-0 (36 lines); hunks: -97,6 +97,8 @@ def _prepare_apply_chat_template_tools_and_messages(; -139,6 +141,33 @@ def _prepare_apply_chat_template_tools_and_messages(; symbols: _prepare_apply_chat_template_tools_and_messages, decode, batch_decode, convert_tokens_to_string
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral_large_3_eagle.py
@@ -0,0 +1,165 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from collections.abc import Iterable
+from functools import partial
+import torch
+import torch.nn as nn
diff -- tests/tokenizers_/test_mistral.py
@@ -91,6 +91,118 @@
+        (
+            {
+                "messages": [
+                    {
+                        "role": "user",
+                        "content": "What is the current local date and time?",
diff -- vllm/transformers_utils/configs/mistral.py
@@ -18,9 +18,31 @@ def adapt_config_dict(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral_large_3_eagle.py` added +165/-0; `vllm/transformers_utils/configs/mistral.py` modified +62/-12; `vllm/model_executor/models/mistral_large_3.py` added +63/-0; `vllm/tokenizers/mistral.py` modified +36/-0
  - tests: `tests/tokenizers_/test_mistral.py` modified +151/-7
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`, `tests/tokenizers_/test_mistral.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29239 - [Bugfix] Use HF config fields as fallback when loading Mistral config

- Link: https://github.com/vllm-project/vllm/pull/29239
- Status/date: merged / 2025-11-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/mistral.py`; associated commits `d1cf8214e523`
- Diff scope read: GitHub Pull Request files API returned 4 files, +25/-4, 69 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Use HF config fields as fallback when loading Mistral config"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "[Bugfix] Use HF config fields as fallback when loading Mistral config"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` modified +10/-3 (13 lines); hunks: -9,14 +9,18; -52,6 +56,9 @@ def adapt_config_dict(config_dict: dict[str, Any], **kwargs) -...; symbols: adapt_config_dict, touching `adapt_config_dict`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` modified +10/-3 (13 lines); hunks: -9,14 +9,18; -52,6 +56,9 @@ def adapt_config_dict(config_dict: dict[str, Any], **kwargs) -...; symbols: adapt_config_dict
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -9,14 +9,18 @@
-def adapt_config_dict(config_dict: dict[str, Any], **kwargs) -> PretrainedConfig:
-    config_dict.update(kwargs)
+def adapt_config_dict(
+    config_dict: dict[str, Any],
+    defaults: dict[str, Any],
+) -> PretrainedConfig:
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +10/-3
- Risk and verification: Runtime changes concentrate in `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #28659 - Default model load/config/tokenizer to `mistral` format if relevant files exist

- Link: https://github.com/vllm-project/vllm/pull/28659
- Status/date: merged / 2025-11-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/language/generation/test_mistral.py`, `vllm/transformers_utils/configs/mistral.py`; associated commits `57430fc95c8a`
- Diff scope read: GitHub Pull Request files API returned 15 files, +230/-34, 497 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Default model load/config/tokenizer to `mistral` format if relevant files exist"; model line: Mistral Small 4; category: docs/tests/CI; main diff: `tests/models/language/generation/test_mistral.py`, `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "Default model load/config/tokenizer to `mistral` format if relevant files exist"; the main implementation surface is `tests/models/language/generation/test_mistral.py`, `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/language/generation/test_mistral.py` modified +1/-1 (2 lines); hunks: -208,7 +208,7 @@ def test_mistral_format(; symbols: test_mistral_format, touching `test_mistral_format`; `vllm/transformers_utils/configs/mistral.py` modified +1/-1 (2 lines); hunks: -118,7 +118,7 @@ def _remap_general_mistral_args(config: dict) -> dict:; symbols: _remap_general_mistral_args, touching `_remap_general_mistral_args`.
- Code diff details:
  - `tests/models/language/generation/test_mistral.py` modified +1/-1 (2 lines); hunks: -208,7 +208,7 @@ def test_mistral_format(; symbols: test_mistral_format
  - `vllm/transformers_utils/configs/mistral.py` modified +1/-1 (2 lines); hunks: -118,7 +118,7 @@ def _remap_general_mistral_args(config: dict) -> dict:; symbols: _remap_general_mistral_args
- Key code excerpts:

```diff
diff -- tests/models/language/generation/test_mistral.py
@@ -208,7 +208,7 @@ def test_mistral_format(
-        tokenizer_mode="auto",
+        tokenizer_mode="hf",
diff -- vllm/transformers_utils/configs/mistral.py
@@ -118,7 +118,7 @@ def _remap_general_mistral_args(config: dict) -> dict:
-        "max_seq_len": ("max_seq_len", 128_000),
+        "max_seq_len": ("max_seq_len", config.get("max_position_embeddings", 128_000)),
```

- Reviewed files:
  - tests: `tests/models/language/generation/test_mistral.py` modified +1/-1
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/language/generation/test_mistral.py`, `tests/models/multimodal/test_mapping.py`, `tests/models/quantization/test_bitsandbytes.py`, `tests/tool_use/utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #29172 - Fix mistral config

- Link: https://github.com/vllm-project/vllm/pull/29172
- Status/date: merged / 2025-11-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/mistral.py`; associated commits `434f3d3eb869`
- Diff scope read: GitHub Pull Request files API returned 1 files, +4/-0, 11 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix mistral config"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "Fix mistral config"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` modified +4/-0 (4 lines); hunks: -90,6 +90,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:; symbols: _remap_mistral_yarn_args, touching `_remap_mistral_yarn_args`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` modified +4/-0 (4 lines); hunks: -90,6 +90,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:; symbols: _remap_mistral_yarn_args
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -90,6 +90,10 @@ def _remap_mistral_yarn_args(config: dict) -> dict:
+    if rope_theta := config.pop("rope_theta", None):
+        config["rope_parameters"]["rope_theta"] = rope_theta
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` modified +4/-0
- Risk and verification: Runtime changes concentrate in `vllm/transformers_utils/configs/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21945 - Migrate Mistral3ImagePixelInputs to TensorSchema

- Link: https://github.com/vllm-project/vllm/pull/21945
- Status/date: merged / 2025-08-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `c4477f55e581`
- Diff scope read: GitHub Pull Request files API returned 1 files, +17/-21, 69 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Migrate Mistral3ImagePixelInputs to TensorSchema"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "Migrate Mistral3ImagePixelInputs to TensorSchema"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` modified +17/-21 (38 lines); hunks: -3,7 +3,7; -32,6 +32,7; symbols: Mistral3ImagePixelInputs, Mistral3PatchMerger, __init__, _validate_pixel_values, touching `Mistral3ImagePixelInputs, Mistral3PatchMerger, __init__`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` modified +17/-21 (38 lines); hunks: -3,7 +3,7; -32,6 +32,7; symbols: Mistral3ImagePixelInputs, Mistral3PatchMerger, __init__, _validate_pixel_values
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -3,7 +3,7 @@
-from typing import (Final, Literal, Optional, Protocol, TypedDict, TypeVar,
+from typing import (Annotated, Final, Literal, Optional, Protocol, TypeVar,
@@ -32,6 +32,7 @@
+from vllm.utils.tensor_schema import TensorSchema, TensorShape
@@ -42,16 +43,24 @@
-class Mistral3ImagePixelInputs(TypedDict):
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` modified +17/-21
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20570 - [Config] Refactor mistral configs

- Link: https://github.com/vllm-project/vllm/pull/20570
- Status/date: merged / 2025-07-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/mistral.py`; associated commits `14601f5fba13`
- Diff scope read: GitHub Pull Request files API returned 3 files, +167/-113, 320 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Config] Refactor mistral configs"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "[Config] Refactor mistral configs"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` added +120/-0 (120 lines); hunks: -0,0 +1,120; symbols: adapt_config_dict, _remap_mistral_vision_args, _remap_mistral_yarn_args, _remap_general_mistral_args, touching `adapt_config_dict, _remap_mistral_vision_args, _remap_mistral_yarn_args`.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` added +120/-0 (120 lines); hunks: -0,0 +1,120; symbols: adapt_config_dict, _remap_mistral_vision_args, _remap_mistral_yarn_args, _remap_general_mistral_args
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -0,0 +1,120 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from typing import Any
+from transformers import PretrainedConfig
+from vllm.logger import init_logger
+logger = init_logger(__name__)
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` added +120/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/llama.py`, `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #20093 - [Bugfix] Fix Mistral tool-parser regex for nested JSON

- Link: https://github.com/vllm-project/vllm/pull/20093
- Status/date: merged / 2025-06-26
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/language/generation/test_mistral.py`; associated commits `754b00edb3fd`
- Diff scope read: GitHub Pull Request files API returned 2 files, +53/-2, 73 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Mistral tool-parser regex for nested JSON"; model line: Mistral Small 4; category: bug fix; main diff: `tests/models/language/generation/test_mistral.py`; technical summary: Covers "[Bugfix] Fix Mistral tool-parser regex for nested JSON"; the main implementation surface is `tests/models/language/generation/test_mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/language/generation/test_mistral.py` modified +51/-0 (51 lines); hunks: -10,6 +10,7; -318,3 +319,53 @@ def test_mistral_guided_decoding(; symbols: test_mistral_guided_decoding, test_mistral_function_call_nested_json, _StubMistralTokenizer, __init__, touching `test_mistral_guided_decoding, test_mistral_function_call_nested_json, _StubMistralTokenizer`.
- Code diff details:
  - `tests/models/language/generation/test_mistral.py` modified +51/-0 (51 lines); hunks: -10,6 +10,7; -318,3 +319,53 @@ def test_mistral_guided_decoding(; symbols: test_mistral_guided_decoding, test_mistral_function_call_nested_json, _StubMistralTokenizer, __init__
- Key code excerpts:

```diff
diff -- tests/models/language/generation/test_mistral.py
@@ -10,6 +10,7 @@
+from vllm.transformers_utils.tokenizer import MistralTokenizer
@@ -318,3 +319,53 @@ def test_mistral_guided_decoding(
+def test_mistral_function_call_nested_json():
+    """Ensure that the function-name regex captures the entire outer-most
+    JSON block, including nested braces."""
+    # Create a minimal stub tokenizer that provides the few attributes the
```

- Reviewed files:
  - tests: `tests/models/language/generation/test_mistral.py` modified +51/-0
- Risk and verification: The diff ships test coverage in `tests/models/language/generation/test_mistral.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #17644 - [Bugfix] Fix tool call template validation for Mistral models

- Link: https://github.com/vllm-project/vllm/pull/17644
- Status/date: merged / 2025-05-08
- Trace source: `git log --name-only -- <model-files>` found it through `examples/tool_chat_template_mistral3.jinja`; associated commits `ca04b97c9361`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-2, 23 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix tool call template validation for Mistral models"; model line: Mistral Small 4; category: bug fix; main diff: `examples/tool_chat_template_mistral3.jinja`; technical summary: Covers "[Bugfix] Fix tool call template validation for Mistral models"; the main implementation surface is `examples/tool_chat_template_mistral3.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/tool_chat_template_mistral3.jinja` modified +9/-2 (11 lines); hunks: -29,7 +29,14; -116,4 +123,4.
- Code diff details:
  - `examples/tool_chat_template_mistral3.jinja` modified +9/-2 (11 lines); hunks: -29,7 +29,14; -116,4 +123,4
- Key code excerpts:

```diff
diff -- examples/tool_chat_template_mistral3.jinja
@@ -29,7 +29,14 @@
-{%- for message in loop_messages | rejectattr("role", "equalto", "tool") | rejectattr("role", "equalto", "tool_results") | selectattr("tool_calls", "undefined") %}
+{%- set filtered_messages = [] %}
+{%- for message in loop_messages %}
+    {%- if message["role"] not in ["tool", "tool_results"] and not message.get("tool_calls") %}
+        {%- set filtered_messages = filtered_messages + [message] %}
+    {%- endif %}
```

- Reviewed files:
  - docs: `examples/tool_chat_template_mistral3.jinja` modified +9/-2
- Risk and verification: This is mostly docs/examples in `examples/tool_chat_template_mistral3.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #17428 - Support LoRA for Mistral3

- Link: https://github.com/vllm-project/vllm/pull/17428
- Status/date: merged / 2025-04-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `a44c4f1d2f7c`
- Diff scope read: GitHub Pull Request files API returned 2 files, +15/-4, 51 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support LoRA for Mistral3"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "Support LoRA for Mistral3"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` modified +14/-3 (17 lines); hunks: -18,6 +18,7; -31,7 +32,8; symbols: init_vision_tower_for_llava, Mistral3ForConditionalGeneration, load_weights, get_mm_mapping, touching `init_vision_tower_for_llava, Mistral3ForConditionalGeneration, load_weights`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` modified +14/-3 (17 lines); hunks: -18,6 +18,7; -31,7 +32,8; symbols: init_vision_tower_for_llava, Mistral3ForConditionalGeneration, load_weights, get_mm_mapping
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -18,6 +18,7 @@
+from vllm.model_executor.models.module_mapping import MultiModelKeys
@@ -31,7 +32,8 @@
-from .interfaces import MultiModalEmbeddings, SupportsMultiModal, SupportsPP
+from .interfaces import (MultiModalEmbeddings, SupportsLoRA,
+                         SupportsMultiModal, SupportsPP)
@@ -382,8 +384,8 @@ def init_vision_tower_for_llava(
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` modified +14/-3
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #17195 - [Misc] Add a Jinja template to support Mistral3 function calling

- Link: https://github.com/vllm-project/vllm/pull/17195
- Status/date: merged / 2025-04-29
- Trace source: `git log --name-only -- <model-files>` found it through `examples/tool_chat_template_mistral3.jinja`; associated commits `96e06e3cb73f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +119/-0, 121 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Misc] Add a Jinja template to support Mistral3 function calling"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `examples/tool_chat_template_mistral3.jinja`; technical summary: Covers "[Misc] Add a Jinja template to support Mistral3 function calling"; the main implementation surface is `examples/tool_chat_template_mistral3.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/tool_chat_template_mistral3.jinja` added +119/-0 (119 lines); hunks: -0,0 +1,119.
- Code diff details:
  - `examples/tool_chat_template_mistral3.jinja` added +119/-0 (119 lines); hunks: -0,0 +1,119
- Key code excerpts:

```diff
diff -- examples/tool_chat_template_mistral3.jinja
@@ -0,0 +1,119 @@
+{%- set today = strftime_now("%Y-%m-%d") %}
+{%- set default_system_message = "You are Mistral Small 3, a Large Language Model (LLM) created by Mistral AI, a French startup headquartered in Paris.\nYour knowledge base was la
+{{- bos_token }}
+{%- if messages[0]['role'] == 'system' %}
+    {%- if messages[0]['content'] is string %}
+        {%- set system_message = messages[0]['content'] %}
```

- Reviewed files:
  - docs: `examples/tool_chat_template_mistral3.jinja` added +119/-0
- Risk and verification: This is mostly docs/examples in `examples/tool_chat_template_mistral3.jinja`; validation should confirm the documented command still maps to current CLI flags and model repo names.

### PR #17270 - [Bugfix] Fix Mistral3 spatial merge error

- Link: https://github.com/vllm-project/vllm/pull/17270
- Status/date: merged / 2025-04-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `cb3f2d8d10ff`
- Diff scope read: GitHub Pull Request files API returned 2 files, +5/-3, 22 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix Mistral3 spatial merge error"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[Bugfix] Fix Mistral3 spatial merge error"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` modified +3/-0 (3 lines); hunks: -272,6 +272,9 @@ def _get_prompt_updates(; symbols: _get_prompt_updates, get_replacement, touching `_get_prompt_updates, get_replacement`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` modified +3/-0 (3 lines); hunks: -272,6 +272,9 @@ def _get_prompt_updates(; symbols: _get_prompt_updates, get_replacement
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -272,6 +272,9 @@ def _get_prompt_updates(
+        # Need to sneak in spatial_merge_size for Mistral3
+        vision_config.spatial_merge_size = getattr(hf_config,
+                                                   "spatial_merge_size", 1)
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` modified +3/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral3.py`, `vllm/model_executor/models/pixtral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15950 - [V1] Support Mistral3 in V1

- Link: https://github.com/vllm-project/vllm/pull/15950
- Status/date: merged / 2025-04-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `f021b9799386`
- Diff scope read: GitHub Pull Request files API returned 2 files, +10/-7, 55 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[V1] Support Mistral3 in V1"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[V1] Support Mistral3 in V1"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` modified +9/-6 (15 lines); hunks: -31,12 +31,12; -425,7 +425,7 @@ def init_vision_tower_for_llava(; symbols: Mistral3ImagePixelInputs, init_vision_tower_for_llava, Mistral3ForConditionalGeneration, _parse_and_validate_image_input, touching `Mistral3ImagePixelInputs, init_vision_tower_for_llava, Mistral3ForConditionalGeneration`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` modified +9/-6 (15 lines); hunks: -31,12 +31,12; -425,7 +425,7 @@ def init_vision_tower_for_llava(; symbols: Mistral3ImagePixelInputs, init_vision_tower_for_llava, Mistral3ForConditionalGeneration, _parse_and_validate_image_input
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -31,12 +31,12 @@
-from .interfaces import (MultiModalEmbeddings, SupportsMultiModal, SupportsPP,
-                         SupportsV0Only)
+from .interfaces import MultiModalEmbeddings, SupportsMultiModal, SupportsPP
-from .vision import get_vision_encoder_info, select_patch_features
+from .vision import (get_vision_encoder_info, scatter_patch_features,
+                     select_patch_features)
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` modified +9/-6
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral3.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15505 - [Model] Support Mistral3 in the HF Transformers format

- Link: https://github.com/vllm-project/vllm/pull/15505
- Status/date: merged / 2025-04-01
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral3.py`; associated commits `51d7c6a2b23e`
- Diff scope read: GitHub Pull Request files API returned 9 files, +723/-4, 805 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Support Mistral3 in the HF Transformers format"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/model_executor/models/mistral3.py`; technical summary: Covers "[Model] Support Mistral3 in the HF Transformers format"; the main implementation surface is `vllm/model_executor/models/mistral3.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral3.py` added +656/-0 (656 lines); hunks: -0,0 +1,656; symbols: Mistral3ImagePixelInputs, Mistral3PatchMerger, __init__, forward, touching `Mistral3ImagePixelInputs, Mistral3PatchMerger, __init__`.
- Code diff details:
  - `vllm/model_executor/models/mistral3.py` added +656/-0 (656 lines); hunks: -0,0 +1,656; symbols: Mistral3ImagePixelInputs, Mistral3PatchMerger, __init__, forward
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral3.py
@@ -0,0 +1,656 @@
+# SPDX-License-Identifier: Apache-2.0
+from abc import abstractmethod
+from collections.abc import Iterable, Mapping, Sequence
+from functools import cached_property
+from typing import (Final, Literal, Optional, Protocol, Set, Tuple, TypedDict,
+                    TypeVar, Union)
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral3.py` added +656/-0
- Risk and verification: The diff ships test coverage in `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14977 - [Mistral-Small 3.1] Update docs and tests

- Link: https://github.com/vllm-project/vllm/pull/14977
- Status/date: merged / 2025-03-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/fixtures/mistral_small_3_chat.json`; associated commits `f863ffc96532`
- Diff scope read: GitHub Pull Request files API returned 5 files, +34/-60, 204 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Mistral-Small 3.1] Update docs and tests"; model line: Mistral Small 4; category: bug fix; main diff: `tests/models/fixtures/mistral_small_3_chat.json`; technical summary: Covers "[Mistral-Small 3.1] Update docs and tests"; the main implementation surface is `tests/models/fixtures/mistral_small_3_chat.json`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/fixtures/mistral_small_3_chat.json` added +1/-0 (1 lines); hunks: -0,0 +1.
- Code diff details:
  - `tests/models/fixtures/mistral_small_3_chat.json` added +1/-0 (1 lines); hunks: -0,0 +1
- Key code excerpts:

```diff
diff -- tests/models/fixtures/mistral_small_3_chat.json
@@ -0,0 +1 @@
+[[[1784, 3937, 6122, 1261, 7244, 10575, 28528, 1408, 1261, 32656, 11237, 1044, 7283, 2015, 1454, 1261, 38462, 4818, 1046, 2], "The image shows a black dog lying on a wooden floor,
```

- Reviewed files:
  - tests: `tests/models/fixtures/mistral_small_3_chat.json` added +1/-0
- Risk and verification: The diff ships test coverage in `tests/models/decoder_only/vision_language/test_pixtral.py`, `tests/models/fixtures/mistral_small_3_chat.json`, `tests/models/fixtures/pixtral_chat_engine.json`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #5649 - [Feature] OpenAI-Compatible Tools API + Streaming for Hermes & Mistral models

- Link: https://github.com/vllm-project/vllm/pull/5649
- Status/date: merged / 2024-09-04
- Trace source: `git log --name-only -- <model-files>` found it through `examples/tool_chat_template_mistral.jinja`, `examples/tool_chat_template_mistral_parallel.jinja`; associated commits `e02ce498be2e`
- Diff scope read: GitHub Pull Request files API returned 26 files, +2588/-83, 3136 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] OpenAI-Compatible Tools API + Streaming for Hermes & Mistral models"; model line: Mistral Small 4; category: model implementation change; main diff: `examples/tool_chat_template_mistral_parallel.jinja`, `examples/tool_chat_template_mistral.jinja`; technical summary: Covers "[Feature] OpenAI-Compatible Tools API + Streaming for Hermes & Mistral models"; the main implementation surface is `examples/tool_chat_template_mistral_parallel.jinja`, `examples/tool_chat_template_mistral.jinja`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `examples/tool_chat_template_mistral_parallel.jinja` added +94/-0 (94 lines); hunks: -0,0 +1,94; `examples/tool_chat_template_mistral.jinja` added +86/-0 (86 lines); hunks: -0,0 +1,86.
- Code diff details:
  - `examples/tool_chat_template_mistral_parallel.jinja` added +94/-0 (94 lines); hunks: -0,0 +1,94
  - `examples/tool_chat_template_mistral.jinja` added +86/-0 (86 lines); hunks: -0,0 +1,86
- Key code excerpts:

```diff
diff -- examples/tool_chat_template_mistral_parallel.jinja
@@ -0,0 +1,94 @@
+{%- if messages[0]["role"] == "system" %}
+    {%- set system_message = messages[0]["content"] %}
+    {%- set loop_messages = messages[1:] %}
+{%- else %}
+    {%- set loop_messages = messages %}
+{%- endif %}
diff -- examples/tool_chat_template_mistral.jinja
@@ -0,0 +1,86 @@
+{%- if messages[0]["role"] == "system" %}
+    {%- set system_message = messages[0]["content"] %}
+    {%- set loop_messages = messages[1:] %}
+{%- else %}
+    {%- set loop_messages = messages %}
+{%- endif %}
```

- Reviewed files:
  - docs: `examples/tool_chat_template_mistral_parallel.jinja` added +94/-0; `examples/tool_chat_template_mistral.jinja` added +86/-0
- Risk and verification: The diff ships test coverage in `tests/tool_use/__init__.py`, `tests/tool_use/conftest.py`, `tests/tool_use/test_chat_completions.py`, `tests/tool_use/test_parallel_tool_calls.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #2868 - Migrate MistralForCausalLM to LlamaForCausalLM

- Link: https://github.com/vllm-project/vllm/pull/2868
- Status/date: merged / 2024-02-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral.py`; associated commits `344020c926ad`
- Diff scope read: GitHub Pull Request files API returned 3 files, +6/-379, 421 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Migrate MistralForCausalLM to LlamaForCausalLM"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/model_executor/models/mistral.py`; technical summary: Covers "Migrate MistralForCausalLM to LlamaForCausalLM"; the main implementation surface is `vllm/model_executor/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral.py` removed +0/-377 (377 lines); hunks: -1,377 +0,0; symbols: MistralMLP, __init__, forward, MistralAttention, touching `MistralMLP, __init__, forward`.
- Code diff details:
  - `vllm/model_executor/models/mistral.py` removed +0/-377 (377 lines); hunks: -1,377 +0,0; symbols: MistralMLP, __init__, forward, MistralAttention
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral.py
@@ -1,377 +0,0 @@
-# coding=utf-8
-# Adapted from
-# https://github.com/huggingface/transformers/blob/v4.28.0/src/transformers/models/llama/modeling_llama.py
-# Copyright 2023 The vLLM team.
-# Copyright 2022 EleutherAI and the HuggingFace Inc. team. All rights reserved.
-#
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral.py` removed +0/-377
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/__init__.py`, `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #1254 - Bump up transformers version & Remove MistralConfig

- Link: https://github.com/vllm-project/vllm/pull/1254
- Status/date: merged / 2023-10-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral.py`, `vllm/transformers_utils/configs/mistral.py`; associated commits `e7c8555d0652`
- Diff scope read: GitHub Pull Request files API returned 6 files, +4/-81, 136 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Bump up transformers version & Remove MistralConfig"; model line: Mistral Small 4; category: model implementation change; main diff: `vllm/transformers_utils/configs/mistral.py`, `vllm/model_executor/models/mistral.py`; technical summary: Covers "Bump up transformers version & Remove MistralConfig"; the main implementation surface is `vllm/transformers_utils/configs/mistral.py`, `vllm/model_executor/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/mistral.py` removed +0/-66 (66 lines); hunks: -1,66 +0,0; symbols: MistralConfig, __init__, touching `MistralConfig, __init__`; `vllm/model_executor/models/mistral.py` modified +1/-1 (2 lines); hunks: -29,6 +29,7; -44,7 +45,6.
- Code diff details:
  - `vllm/transformers_utils/configs/mistral.py` removed +0/-66 (66 lines); hunks: -1,66 +0,0; symbols: MistralConfig, __init__
  - `vllm/model_executor/models/mistral.py` modified +1/-1 (2 lines); hunks: -29,6 +29,7; -44,7 +45,6
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/mistral.py
@@ -1,66 +0,0 @@
-# Licensed under the Apache License, Version 2.0 (the "License");
-# you may not use this file except in compliance with the License.
-# You may obtain a copy of the License at
-#
-#     http://www.apache.org/licenses/LICENSE-2.0
-#
diff -- vllm/model_executor/models/mistral.py
@@ -29,6 +29,7 @@
+from transformers import MistralConfig
@@ -44,7 +45,6 @@
-from vllm.transformers_utils.configs.mistral import MistralConfig
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/mistral.py` removed +0/-66; `vllm/model_executor/models/mistral.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/__init__.py`, `vllm/model_executor/models/mistral.py`, `vllm/transformers_utils/config.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #1303 - [Minor] Fix comment in mistral.py

- Link: https://github.com/vllm-project/vllm/pull/1303
- Status/date: merged / 2023-10-10
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral.py`; associated commits `b95ee898fe1c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Minor] Fix comment in mistral.py"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/model_executor/models/mistral.py`; technical summary: Covers "[Minor] Fix comment in mistral.py"; the main implementation surface is `vllm/model_executor/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral.py` modified +1/-1 (2 lines); hunks: -20,7 +20,7.
- Code diff details:
  - `vllm/model_executor/models/mistral.py` modified +1/-1 (2 lines); hunks: -20,7 +20,7
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral.py
@@ -20,7 +20,7 @@
-"""Inference-only LLaMA model compatible with HuggingFace weights.
+"""Inference-only Mistral model compatible with HuggingFace weights.
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #1220 - Fix Mistral model

- Link: https://github.com/vllm-project/vllm/pull/1220
- Status/date: merged / 2023-09-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral.py`; associated commits `a8e98aee0c16`
- Diff scope read: GitHub Pull Request files API returned 4 files, +27/-14, 124 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix Mistral model"; model line: Mistral Small 4; category: bug fix; main diff: `vllm/model_executor/models/mistral.py`; technical summary: Covers "Fix Mistral model"; the main implementation surface is `vllm/model_executor/models/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral.py` modified +1/-1 (2 lines); hunks: -29,7 +29,6; -46,6 +45,7.
- Code diff details:
  - `vllm/model_executor/models/mistral.py` modified +1/-1 (2 lines); hunks: -29,7 +29,6; -46,6 +45,7
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral.py
@@ -29,7 +29,6 @@
-from vllm.transformers_utils.configs.mistral import MistralConfig
@@ -46,6 +45,7 @@
+from vllm.transformers_utils.configs.mistral import MistralConfig
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/models/mistral.py`, `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/__init__.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #1196 - [Mistral] Mistral-7B-v0.1 support

- Link: https://github.com/vllm-project/vllm/pull/1196
- Status/date: merged / 2023-09-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/model_executor/models/mistral.py`, `vllm/transformers_utils/configs/mistral.py`; associated commits `bb1ba58f0647`
- Diff scope read: GitHub Pull Request files API returned 13 files, +571/-25, 795 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Mistral] Mistral-7B-v0.1 support"; model line: Mistral Small 4; category: model support/runtime entry; main diff: `vllm/model_executor/models/mistral.py`, `vllm/transformers_utils/configs/mistral.py`; technical summary: Covers "[Mistral] Mistral-7B-v0.1 support"; the main implementation surface is `vllm/model_executor/models/mistral.py`, `vllm/transformers_utils/configs/mistral.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/models/mistral.py` added +404/-0 (404 lines); hunks: -0,0 +1,404; symbols: MistralMLP, __init__, forward, MistralAttention, touching `MistralMLP, __init__, forward`; `vllm/transformers_utils/configs/mistral.py` added +66/-0 (66 lines); hunks: -0,0 +1,66; symbols: MistralConfig, __init__, touching `MistralConfig, __init__`.
- Code diff details:
  - `vllm/model_executor/models/mistral.py` added +404/-0 (404 lines); hunks: -0,0 +1,404; symbols: MistralMLP, __init__, forward, MistralAttention
  - `vllm/transformers_utils/configs/mistral.py` added +66/-0 (66 lines); hunks: -0,0 +1,66; symbols: MistralConfig, __init__
- Key code excerpts:

```diff
diff -- vllm/model_executor/models/mistral.py
@@ -0,0 +1,404 @@
+# coding=utf-8
+# Adapted from
+# https://github.com/huggingface/transformers/blob/v4.28.0/src/transformers/models/llama/modeling_llama.py
+# Copyright 2023 The vLLM team.
+# Copyright 2022 EleutherAI and the HuggingFace Inc. team. All rights reserved.
+#
diff -- vllm/transformers_utils/configs/mistral.py
@@ -0,0 +1,66 @@
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
+#
```

- Reviewed files:
  - runtime: `vllm/model_executor/models/mistral.py` added +404/-0; `vllm/transformers_utils/configs/mistral.py` added +66/-0
- Risk and verification: Runtime changes concentrate in `vllm/config.py`, `vllm/core/block_manager.py`, `vllm/core/scheduler.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
