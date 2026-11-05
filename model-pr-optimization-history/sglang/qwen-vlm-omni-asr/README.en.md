# sglang Qwen VLM/Omni/ASR Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `docs/cookbook/autoregressive/NVIDIA/Nemotron3-Nano-Omni.mdx` | no direct PR-number commit |
| `docs/cookbook/omni/FishAudio/S2-Pro.mdx` | no direct PR-number commit |
| `docs/cookbook/omni/intro.mdx` | no direct PR-number commit |
| `docs/src/snippets/autoregressive/nemotron3-nano-omni-deployment.jsx` | no direct PR-number commit |
| `examples/chat_template/qwen3_vl_reranker.jinja` | no direct PR-number commit |
| `examples/runtime/qwen3_vl_reranker.py` | no direct PR-number commit |
| `python/sglang/srt/arg_groups/model_overrides/qwen3_vl.py` | [#36411](https://github.com/sgl-project/sglang/pull/36411) |
| `python/sglang/srt/configs/qwen3_asr.py` | [#22073](https://github.com/sgl-project/sglang/pull/22073), [#22181](https://github.com/sgl-project/sglang/pull/22181), [#24187](https://github.com/sgl-project/sglang/pull/24187) |
| `python/sglang/srt/configs/qwen3_omni.py` | [#10911](https://github.com/sgl-project/sglang/pull/10911) |
| `python/sglang/srt/configs/qwen3_vl.py` | [#10323](https://github.com/sgl-project/sglang/pull/10323), [#10911](https://github.com/sgl-project/sglang/pull/10911) |
| `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py` | [#32611](https://github.com/sgl-project/sglang/pull/32611) |
| `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py` | [#32611](https://github.com/sgl-project/sglang/pull/32611) |
| `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` | [#22089](https://github.com/sgl-project/sglang/pull/22089), [#22181](https://github.com/sgl-project/sglang/pull/22181) |
| `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` | [#43309](https://github.com/sgl-project/sglang/pull/43309) |
| `python/sglang/srt/models/dots3_common/dots_omni_audio.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/models/dots3_common/dots_omni_towers.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/models/dots3_common/dots_omni_vision.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/models/glmasr.py` | [#15570](https://github.com/sgl-project/sglang/pull/15570), [#15772](https://github.com/sgl-project/sglang/pull/15772), [#32611](https://github.com/sgl-project/sglang/pull/32611) |
| `python/sglang/srt/models/muse_spark_omni.py` | no direct PR-number commit |
| `python/sglang/srt/models/qwen2_5_vl.py` | [#5003](https://github.com/sgl-project/sglang/pull/5003), [#5349](https://github.com/sgl-project/sglang/pull/5349), [#6136](https://github.com/sgl-project/sglang/pull/6136), [#8801](https://github.com/sgl-project/sglang/pull/8801), [#13055](https://github.com/sgl-project/sglang/pull/13055), [#13075](https://github.com/sgl-project/sglang/pull/13075), [#13126](https://github.com/sgl-project/sglang/pull/13126), [#13904](https://github.com/sgl-project/sglang/pull/13904), [#14292](https://github.com/sgl-project/sglang/pull/14292), [#15138](https://github.com/sgl-project/sglang/pull/15138), [#15320](https://github.com/sgl-project/sglang/pull/15320), [#37043](https://github.com/sgl-project/sglang/pull/37043) |
| `python/sglang/srt/models/qwen2_audio.py` | no direct PR-number commit |
| `python/sglang/srt/models/qwen2_vl.py` | [#2055](https://github.com/sgl-project/sglang/pull/2055), [#5003](https://github.com/sgl-project/sglang/pull/5003), [#5349](https://github.com/sgl-project/sglang/pull/5349), [#5783](https://github.com/sgl-project/sglang/pull/5783), [#6136](https://github.com/sgl-project/sglang/pull/6136), [#13055](https://github.com/sgl-project/sglang/pull/13055), [#13736](https://github.com/sgl-project/sglang/pull/13736) |
| `python/sglang/srt/models/qwen3_asr.py` | [#22073](https://github.com/sgl-project/sglang/pull/22073) |
| `python/sglang/srt/models/qwen3_omni_moe.py` | [#10911](https://github.com/sgl-project/sglang/pull/10911), [#11791](https://github.com/sgl-project/sglang/pull/11791), [#12333](https://github.com/sgl-project/sglang/pull/12333), [#12662](https://github.com/sgl-project/sglang/pull/12662), [#18185](https://github.com/sgl-project/sglang/pull/18185) |
| `python/sglang/srt/models/qwen3_vl.py` | [#10323](https://github.com/sgl-project/sglang/pull/10323), [#10911](https://github.com/sgl-project/sglang/pull/10911), [#11458](https://github.com/sgl-project/sglang/pull/11458), [#11481](https://github.com/sgl-project/sglang/pull/11481), [#12333](https://github.com/sgl-project/sglang/pull/12333), [#12662](https://github.com/sgl-project/sglang/pull/12662), [#13724](https://github.com/sgl-project/sglang/pull/13724), [#13736](https://github.com/sgl-project/sglang/pull/13736), [#14292](https://github.com/sgl-project/sglang/pull/14292), [#15205](https://github.com/sgl-project/sglang/pull/15205), [#15320](https://github.com/sgl-project/sglang/pull/15320), [#16366](https://github.com/sgl-project/sglang/pull/16366), ... (22 total) |
| `python/sglang/srt/models/qwen3_vl_moe.py` | [#10323](https://github.com/sgl-project/sglang/pull/10323), [#10911](https://github.com/sgl-project/sglang/pull/10911), [#11481](https://github.com/sgl-project/sglang/pull/11481), [#13983](https://github.com/sgl-project/sglang/pull/13983), [#21469](https://github.com/sgl-project/sglang/pull/21469), [#34690](https://github.com/sgl-project/sglang/pull/34690) |
| `python/sglang/srt/multimodal/processors/dots_note_omni.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/__init__.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/flatten_runner.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/preprocess.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/v2core.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/video_qa_flattener.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |
| `python/sglang/srt/multimodal/processors/glmasr.py` | [#15570](https://github.com/sgl-project/sglang/pull/15570), [#15772](https://github.com/sgl-project/sglang/pull/15772), [#32611](https://github.com/sgl-project/sglang/pull/32611) |
| `python/sglang/srt/multimodal/processors/muse_spark_omni.py` | no direct PR-number commit |
| `python/sglang/srt/multimodal/processors/qwen3_asr.py` | [#22073](https://github.com/sgl-project/sglang/pull/22073), [#22089](https://github.com/sgl-project/sglang/pull/22089), [#22181](https://github.com/sgl-project/sglang/pull/22181) |
| `python/sglang/srt/multimodal/processors/qwen_vl.py` | [#10323](https://github.com/sgl-project/sglang/pull/10323), [#10911](https://github.com/sgl-project/sglang/pull/10911), [#11377](https://github.com/sgl-project/sglang/pull/11377), [#12240](https://github.com/sgl-project/sglang/pull/12240), [#12458](https://github.com/sgl-project/sglang/pull/12458), [#12662](https://github.com/sgl-project/sglang/pull/12662), [#26094](https://github.com/sgl-project/sglang/pull/26094), [#26116](https://github.com/sgl-project/sglang/pull/26116), [#26167](https://github.com/sgl-project/sglang/pull/26167), [#36411](https://github.com/sgl-project/sglang/pull/36411), [#39278](https://github.com/sgl-project/sglang/pull/39278) |
| `python/sglang/test/external_models/custom_qwen2_vl.py` | no direct PR-number commit |
| `test/manual/models/test_qwen3_asr.py` | [#22181](https://github.com/sgl-project/sglang/pull/22181), [#22848](https://github.com/sgl-project/sglang/pull/22848) |
| `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py` | [#21469](https://github.com/sgl-project/sglang/pull/21469) |
| `test/registered/npu/accuracy/qwen3_omni_30b_a3b_thinking/test_npu_qwen3_omni_30b_a3b_thinking_1p_mmmu.py` | no direct PR-number commit |
| `test/registered/npu/accuracy/qwen3_vl_30b_a3b/test_npu_qwen3_vl_30b_a3b_bf16_2p_gsm8k.py` | no direct PR-number commit |
| `test/registered/npu/accuracy/qwen3_vl_30b_a3b_thinking/test_npu_qwen3_vl_30b_a3b_thinking_1p_mmmu.py` | no direct PR-number commit |
| `test/registered/npu/accuracy/qwen3_vl_8b/test_npu_qwen3_vl_8b_bf16_2p_gsm8k.py` | no direct PR-number commit |
| `test/registered/npu/accuracy/qwen3_vl_8b_thinking/test_npu_qwen3_vl_8b_thinking_1p_mmmu.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_qwen2_5_vl_3b_instruct.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_qwen2_5_vl_72b_instruct.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_235b_a22b_instruct.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_30b_a3b_instruct.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_4b_instruct.py` | no direct PR-number commit |
| `test/registered/npu/vlm_models/test_npu_qwen3_vl_8b_instruct.py` | no direct PR-number commit |
| `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` | [#31596](https://github.com/sgl-project/sglang/pull/31596), [#36411](https://github.com/sgl-project/sglang/pull/36411) |
| `test/registered/unit/models/test_qwen3_vl_image_generation_reject.py` | no direct PR-number commit |
| `test/registered/unit/multimodal/test_dots_note_omni.py` | [#33829](https://github.com/sgl-project/sglang/pull/33829) |

## PR Coverage Summary

- Git-traced PRs: 53
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 53
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2024-11-21 | [#2055](https://github.com/sgl-project/sglang/pull/2055) | merged | Add support for Qwen2-VL-based embedding models | `python/sglang/srt/models/qwen2_vl.py` |
| 2025-04-14 | [#5003](https://github.com/sgl-project/sglang/pull/5003) | merged | Support for Qwen2.5-VL Model in bitsandbytes Format | `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-04-24 | [#5349](https://github.com/sgl-project/sglang/pull/5349) | merged | vlm: enable radix cache for qwen-vl models | `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-05-01 | [#5783](https://github.com/sgl-project/sglang/pull/5783) | merged | Remove unused method `calculate_num_image_tokens` from qwen2_vl.py | `python/sglang/srt/models/qwen2_vl.py` |
| 2025-05-16 | [#6136](https://github.com/sgl-project/sglang/pull/6136) | merged | Support precomputed multimodal features for Qwen-VL and Gemma3 models. | `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py` |
| 2025-09-08 | [#8801](https://github.com/sgl-project/sglang/pull/8801) | merged | Qwen2.5-VL eagle3 infer | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-09-23 | [#10323](https://github.com/sgl-project/sglang/pull/10323) | merged | model: support qwen3-vl series | `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/configs/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py` |
| 2025-10-12 | [#11481](https://github.com/sgl-project/sglang/pull/11481) | merged | [smol] [perf] Qwen3-VL in place op. | `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py` |
| 2025-10-15 | [#11458](https://github.com/sgl-project/sglang/pull/11458) | merged | [BugFix][Qwen3-VL]: fix cu_seqlens in qwen3-vl | `python/sglang/srt/models/qwen3_vl.py` |
| 2025-10-16 | [#10911](https://github.com/sgl-project/sglang/pull/10911) | merged | model: qwen3-omni (thinker-only) | `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/configs/qwen3_omni.py`, `python/sglang/srt/models/qwen3_vl_moe.py` |
| 2025-10-21 | [#11377](https://github.com/sgl-project/sglang/pull/11377) | merged | [BugFix][Qwen3-VL]: add metadata for video in qwen3-vl | `python/sglang/srt/multimodal/processors/qwen_vl.py` |
| 2025-11-06 | [#12240](https://github.com/sgl-project/sglang/pull/12240) | merged | [VLM] Optimize qwen_vl preprocess_video | `python/sglang/srt/multimodal/processors/qwen_vl.py` |
| 2025-11-12 | [#12458](https://github.com/sgl-project/sglang/pull/12458) | merged | fix: duplicate resize images logic of qwen-vl series models | `python/sglang/srt/multimodal/processors/qwen_vl.py` |
| 2025-11-12 | [#13075](https://github.com/sgl-project/sglang/pull/13075) | merged | [VLM] Support PP for Qwen2.5-VL | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-11-18 | [#13126](https://github.com/sgl-project/sglang/pull/13126) | merged | [VLM][feat] Support encoder DP for Qwen2.5-VL | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-11-20 | [#13055](https://github.com/sgl-project/sglang/pull/13055) | merged | [VLM] Support Piecewise CUDA Graph for Qwen2.5-VL | `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py` |
| 2025-11-22 | [#13736](https://github.com/sgl-project/sglang/pull/13736) | merged | [VLM] Replace torch.repeat_interleave with faster np.repeat for Qwen-VL series | `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen2_vl.py` |
| 2025-11-26 | [#13983](https://github.com/sgl-project/sglang/pull/13983) | merged | Support KTransformers for Qwen3-VL moe | `python/sglang/srt/models/qwen3_vl_moe.py` |
| 2025-11-28 | [#13904](https://github.com/sgl-project/sglang/pull/13904) | merged | [Bugfix] qwen2.5-vl spec decode accept_len low | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-11-28 | [#13724](https://github.com/sgl-project/sglang/pull/13724) | merged | support qwen3_vl vision model dp | `python/sglang/srt/models/qwen3_vl.py` |
| 2025-12-04 | [#14292](https://github.com/sgl-project/sglang/pull/14292) | merged | [VLM] Introduce Cache for positional embedding ids for Qwen-VL family | `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py` |
| 2025-12-06 | [#11791](https://github.com/sgl-project/sglang/pull/11791) | merged | fix rmsnorm -> layernorm in qwen3 omni | `python/sglang/srt/models/qwen3_omni_moe.py` |
| 2025-12-17 | [#12333](https://github.com/sgl-project/sglang/pull/12333) | merged | [PP] Add pp support for Qwen3-VL | `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_omni_moe.py` |
| 2025-12-17 | [#15138](https://github.com/sgl-project/sglang/pull/15138) | merged | [bug fix][pp] fix weight load for qwen2.5-vl | `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-12-18 | [#15205](https://github.com/sgl-project/sglang/pull/15205) | merged | [VLM] Support cos sin cache for Qwen3-VL & GLM-4.1V | `python/sglang/srt/models/qwen3_vl.py` |
| 2025-12-20 | [#15320](https://github.com/sgl-project/sglang/pull/15320) | merged | [VLM] Support ViT Piecewise CUDA Graph for Qwen3-VL | `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py` |
| 2025-12-23 | [#15570](https://github.com/sgl-project/sglang/pull/15570) | merged | [GLM-ASR] GLM-ASR Support | `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py` |
| 2025-12-25 | [#15772](https://github.com/sgl-project/sglang/pull/15772) | merged | Change GLM-ASR class name | `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py` |
| 2026-01-22 | [#16366](https://github.com/sgl-project/sglang/pull/16366) | merged | Optimize Qwen3-VL video memory usage | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-02-02 | [#18024](https://github.com/sgl-project/sglang/pull/18024) | merged | fix: correct weight loading prefix mapping for Qwen3-VL | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-02-05 | [#16781](https://github.com/sgl-project/sglang/pull/16781) | merged | Refactor(qwen3-vl) optimize position encoding interpolation | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-02-27 | [#19333](https://github.com/sgl-project/sglang/pull/19333) | merged | fix qwen3_vl visual module loading | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-03-14 | [#18185](https://github.com/sgl-project/sglang/pull/18185) | merged | [Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker | `python/sglang/srt/models/qwen3_omni_moe.py` |
| 2026-04-01 | [#21469](https://github.com/sgl-project/sglang/pull/21469) | merged | [3/n] lora moe - Support Qwen3-VL-30B-A3B-Instruct | `python/sglang/srt/models/qwen3_vl_moe.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py` |
| 2026-04-07 | [#22073](https://github.com/sgl-project/sglang/pull/22073) | merged | [Feature] Adding Qwen3-asr Model Support | `python/sglang/srt/models/qwen3_asr.py`, `python/sglang/srt/configs/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py` |
| 2026-04-08 | [#22181](https://github.com/sgl-project/sglang/pull/22181) | merged | [refactor] [asr] Add transcription adapter for extensible ASR models support | `python/sglang/srt/configs/qwen3_asr.py`, `test/manual/models/test_qwen3_asr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` |
| 2026-04-09 | [#22230](https://github.com/sgl-project/sglang/pull/22230) | merged | [Feature] Support eagle3 for qwen3-vl | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-04-09 | [#22089](https://github.com/sgl-project/sglang/pull/22089) | merged | [Feature] Add chunk-based streaming ASR for Qwen3-ASR | `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py` |
| 2026-05-12 | [#24187](https://github.com/sgl-project/sglang/pull/24187) | merged | [Fix] Qwen3-ASR config: set thinker_config before super().__init__ | `python/sglang/srt/configs/qwen3_asr.py` |
| 2026-05-23 | [#26116](https://github.com/sgl-project/sglang/pull/26116) | merged | [VLM] Reuse Qwen pretokenized ids | `python/sglang/srt/multimodal/processors/qwen_vl.py` |
| 2026-05-24 | [#26167](https://github.com/sgl-project/sglang/pull/26167) | merged | [VLM] feat: replace small H2D calls with a single one for qwen-vl | `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py` |
| 2026-05-25 | [#26094](https://github.com/sgl-project/sglang/pull/26094) | merged | [VLM] fix: fix only the grids from last split mm item is collected for qwen-vl | `python/sglang/srt/multimodal/processors/qwen_vl.py` |
| 2026-05-27 | [#12662](https://github.com/sgl-project/sglang/pull/12662) | merged | [CPU] Add support for Qwen3-vl and Qwen3-omni | `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/models/qwen3_vl.py` |
| 2026-05-27 | [#22848](https://github.com/sgl-project/sglang/pull/22848) | merged | [Feature] WebSocket streaming audio input for ASR | `test/manual/models/test_qwen3_asr.py` |
| 2026-06-24 | [#28940](https://github.com/sgl-project/sglang/pull/28940) | merged | [VLM] Qwen3-VL / Moss-VL ViT preprocessing optimizations | `python/sglang/srt/models/qwen3_vl.py` |
| 2026-07-29 | [#31596](https://github.com/sgl-project/sglang/pull/31596) | merged | fix(vlm): materialize Qwen3-VL features on the vision device | `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`, `python/sglang/srt/models/qwen3_vl.py` |
| 2026-08-19 | [#32611](https://github.com/sgl-project/sglang/pull/32611) | merged | Fix transcription & audio-understanding for ASR/audio/speech models | `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py` |
| 2026-08-22 | [#33829](https://github.com/sgl-project/sglang/pull/33829) | merged | [Model] Complete dots.note.omni support with native encoders, video preprocessing, and MTP decoding | `python/sglang/srt/models/dots3_common/dots_omni_audio.py`, `python/sglang/srt/models/dots3_common/dots_omni_vision.py`, `python/sglang/srt/multimodal/processors/dots_note_omni.py` |
| 2026-08-28 | [#34690](https://github.com/sgl-project/sglang/pull/34690) | merged | [BugFix][VLM] keep Qwen3-VL MoE inference deepstack order | `python/sglang/srt/models/qwen3_vl_moe.py`, `python/sglang/srt/models/qwen3_vl.py` |
| 2026-08-30 | [#37043](https://github.com/sgl-project/sglang/pull/37043) | merged | [vlm] fix: preserve per-request vit graph metadata for qwen-vl | `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py` |
| 2026-09-12 | [#36411](https://github.com/sgl-project/sglang/pull/36411) | merged | [Perf] Optimize Qwen3-VL unique-image serving on H100 | `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` |
| 2026-09-15 | [#39278](https://github.com/sgl-project/sglang/pull/39278) | merged | [Fix][Qwen-VL] Normalize sentinel on artifact fast path | `python/sglang/srt/multimodal/processors/qwen_vl.py` |
| 2026-10-12 | [#43309](https://github.com/sgl-project/sglang/pull/43309) | merged | [Fix] Adapt NPU Qwen-VL processor patch to transformers 5.19 resize() signature change | `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` |

## Per-PR Diff Audit Cards

### PR #2055 - Add support for Qwen2-VL-based embedding models

- Link: https://github.com/sgl-project/sglang/pull/2055
- Status/date: merged / 2024-11-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_vl.py`; associated commits `f6f713797bcb`
- Diff scope read: GitHub Pull Request files API returned 4 files, +39/-12, 114 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Add support for Qwen2-VL-based embedding models"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen2_vl.py`; technical summary: Covers "Add support for Qwen2-VL-based embedding models"; the main implementation surface is `python/sglang/srt/models/qwen2_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_vl.py` modified +12/-5 (17 lines); hunks: -44,6 +44,7; -559,6 +560,7 @@ def __init__(; symbols: __init__, _process_image_input, forward, touching `__init__, _process_image_input, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_vl.py` modified +12/-5 (17 lines); hunks: -44,6 +44,7; -559,6 +560,7 @@ def __init__(; symbols: __init__, _process_image_input, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_vl.py
@@ -44,6 +44,7 @@
+from sglang.srt.layers.pooler import Pooler, PoolingType
@@ -559,6 +560,7 @@ def __init__(
+        self.pooler = Pooler(pooling_type=PoolingType.LAST, normalize=True)
@@ -577,6 +579,7 @@ def forward(
+        get_embedding: bool = False,
@@ -599,8 +602,8 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_vl.py` modified +12/-5
- Risk and verification: The diff ships test coverage in `python/sglang/test/runners.py`, `test/srt/models/test_embedding_models.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #5003 - Support for Qwen2.5-VL Model in bitsandbytes Format

- Link: https://github.com/sgl-project/sglang/pull/5003
- Status/date: merged / 2025-04-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`; associated commits `072df753546b`
- Diff scope read: GitHub Pull Request files API returned 6 files, +375/-45, 531 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support for Qwen2.5-VL Model in bitsandbytes Format"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "Support for Qwen2.5-VL Model in bitsandbytes Format"; the main implementation surface is `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_vl.py` modified +24/-23 (47 lines); hunks: -152,7 +152,7 @@ def __init__(; -351,7 +351,7 @@ def __init__(; symbols: __init__, dtype, device, forward, touching `__init__, dtype, device`; `python/sglang/srt/models/qwen2_5_vl.py` modified +24/-22 (46 lines); hunks: -141,7 +141,7 @@ def __init__(; -325,7 +325,7 @@ def get_window_index(self, grid_thw):; symbols: __init__, get_window_index, dtype, device, touching `__init__, get_window_index, dtype`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_vl.py` modified +24/-23 (47 lines); hunks: -152,7 +152,7 @@ def __init__(; -351,7 +351,7 @@ def __init__(; symbols: __init__, dtype, device, forward
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +24/-22 (46 lines); hunks: -141,7 +141,7 @@ def __init__(; -325,7 +325,7 @@ def get_window_index(self, grid_thw):; symbols: __init__, get_window_index, dtype, device
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_vl.py
@@ -152,7 +152,7 @@ def __init__(
-            use_qkv_parallel=False,
+            use_qkv_parallel=True,
@@ -351,7 +351,7 @@ def __init__(
-        return next(self.parameters()).dtype
+        return self.patch_embed.proj.weight.dtype
@@ -423,6 +423,25 @@ def forward(
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -141,7 +141,7 @@ def __init__(
-            use_qkv_parallel=False,
+            use_qkv_parallel=True,
@@ -325,7 +325,7 @@ def get_window_index(self, grid_thw):
-        return self.blocks[0].mlp.gate_proj.weight.dtype
+        return self.patch_embed.proj.weight.dtype
@@ -429,6 +429,25 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_vl.py` modified +24/-23; `python/sglang/srt/models/qwen2_5_vl.py` modified +24/-22
- Risk and verification: The diff ships test coverage in `test/srt/run_suite.py`, `test/srt/test_bnb.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #5349 - vlm: enable radix cache for qwen-vl models

- Link: https://github.com/sgl-project/sglang/pull/5349
- Status/date: merged / 2025-04-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`; associated commits `c998d04b4692`
- Diff scope read: GitHub Pull Request files API returned 26 files, +435/-337, 1363 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "vlm: enable radix cache for qwen-vl models"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "vlm: enable radix cache for qwen-vl models"; the main implementation surface is `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_vl.py` modified +3/-7 (10 lines); hunks: -42,7 +42,7; -490,15 +490,11 @@ def __init__(; symbols: __init__, pad_input_ids, get_image_feature, touching `__init__, pad_input_ids, get_image_feature`; `python/sglang/srt/models/qwen2_5_vl.py` modified +3/-6 (9 lines); hunks: -49,7 +49,7; -488,11 +488,8 @@ def __init__(; symbols: __init__, pad_input_ids, get_image_feature, touching `__init__, pad_input_ids, get_image_feature`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_vl.py` modified +3/-7 (10 lines); hunks: -42,7 +42,7; -490,15 +490,11 @@ def __init__(; symbols: __init__, pad_input_ids, get_image_feature
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +3/-6 (9 lines); hunks: -49,7 +49,7; -488,11 +488,8 @@ def __init__(; symbols: __init__, pad_input_ids, get_image_feature
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_vl.py
@@ -42,7 +42,7 @@
-    MultiModalityDataPaddingPatternTokenPairs,
+    MultiModalityDataPaddingPatternMultimodalTokens,
@@ -490,15 +490,11 @@ def __init__(
-    # Use grid_t * grid_w * grid_h to pad tokens for each image
-    # add replaced padding by unique image hash
-        im_start_id: int = mm_inputs.im_start_id
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -49,7 +49,7 @@
-    MultiModalityDataPaddingPatternTokenPairs,
+    MultiModalityDataPaddingPatternMultimodalTokens,
@@ -488,11 +488,8 @@ def __init__(
-        im_start_id: int = mm_inputs.im_start_id
-        im_end_id: int = mm_inputs.im_end_id
-        media_token_pairs = [(im_start_id, im_end_id)]
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_vl.py` modified +3/-7; `python/sglang/srt/models/qwen2_5_vl.py` modified +3/-6
- Risk and verification: The diff ships test coverage in `python/sglang/test/runners.py`, `test/srt/run_suite.py`, `test/srt/test_vision_openai_server.py`, `test/srt/test_vlm_accuracy.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #5783 - Remove unused method `calculate_num_image_tokens` from qwen2_vl.py

- Link: https://github.com/sgl-project/sglang/pull/5783
- Status/date: merged / 2025-05-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_vl.py`; associated commits `e97e57e699e5`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-12, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Remove unused method `calculate_num_image_tokens` from qwen2_vl.py"; model line: Qwen VLM/Omni/ASR; category: model implementation change; main diff: `python/sglang/srt/models/qwen2_vl.py`; technical summary: Covers "Remove unused method `calculate_num_image_tokens` from qwen2_vl.py"; the main implementation surface is `python/sglang/srt/models/qwen2_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_vl.py` modified +0/-12 (12 lines); hunks: -442,18 +442,6 @@ class Qwen2VLForConditionalGeneration(nn.Module):; symbols: Qwen2VLForConditionalGeneration, calculate_num_image_tokens, __init__, touching `Qwen2VLForConditionalGeneration, calculate_num_image_tokens, __init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_vl.py` modified +0/-12 (12 lines); hunks: -442,18 +442,6 @@ class Qwen2VLForConditionalGeneration(nn.Module):; symbols: Qwen2VLForConditionalGeneration, calculate_num_image_tokens, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_vl.py
@@ -442,18 +442,6 @@ class Qwen2VLForConditionalGeneration(nn.Module):
-    def calculate_num_image_tokens(self, image_grid_thw: Tuple[int, int, int]):
-        processor = cached_get_processor(self.config._name_or_path)
-        grid_t, grid_h, grid_w = image_grid_thw
-        num_image_tokens = (
-            grid_t
-            * grid_h
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_vl.py` modified +0/-12
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen2_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #6136 - Support precomputed multimodal features for Qwen-VL and Gemma3 models.

- Link: https://github.com/sgl-project/sglang/pull/6136
- Status/date: merged / 2025-05-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`; associated commits `f19a9204cdbd`
- Diff scope read: GitHub Pull Request files API returned 14 files, +592/-125, 1118 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support precomputed multimodal features for Qwen-VL and Gemma3 models."; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`; technical summary: Covers "Support precomputed multimodal features for Qwen-VL and Gemma3 models."; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +6/-0 (6 lines); hunks: -497,6 +497,12 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: Mu...; symbols: pad_input_ids, get_image_feature, touching `pad_input_ids, get_image_feature`; `python/sglang/srt/models/qwen2_vl.py` modified +6/-0 (6 lines); hunks: -486,6 +486,12 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: Mu...; symbols: pad_input_ids, get_image_feature, touching `pad_input_ids, get_image_feature`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +6/-0 (6 lines); hunks: -497,6 +497,12 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: Mu...; symbols: pad_input_ids, get_image_feature
  - `python/sglang/srt/models/qwen2_vl.py` modified +6/-0 (6 lines); hunks: -486,6 +486,12 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: Mu...; symbols: pad_input_ids, get_image_feature
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -497,6 +497,12 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: MultimodalInputs):
+        if any(item.precomputed_features is not None for item in items):
+            if not all(item.precomputed_features is not None for item in items):
+                raise NotImplementedError(
+                    "MM inputs where only some items are precomputed."
+                )
+            return torch.concat([item.precomputed_features for item in items])
diff -- python/sglang/srt/models/qwen2_vl.py
@@ -486,6 +486,12 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: MultimodalInputs):
+        if any(item.precomputed_features is not None for item in items):
+            if not all(item.precomputed_features is not None for item in items):
+                raise NotImplementedError(
+                    "MM inputs where only some items are precomputed."
+                )
+            return torch.concat([item.precomputed_features for item in items])
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +6/-0; `python/sglang/srt/models/qwen2_vl.py` modified +6/-0
- Risk and verification: The diff ships test coverage in `test/srt/test_skip_tokenizer_init.py`, `test/srt/test_vlm_accuracy.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #8801 - Qwen2.5-VL eagle3 infer

- Link: https://github.com/sgl-project/sglang/pull/8801
- Status/date: merged / 2025-09-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`; associated commits `37d83c6e6d8a`
- Diff scope read: GitHub Pull Request files API returned 9 files, +114/-5, 260 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Qwen2.5-VL eagle3 infer"; model line: Qwen VLM/Omni/ASR; category: model implementation change; main diff: `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "Qwen2.5-VL eagle3 infer"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +24/-1 (25 lines); hunks: -517,6 +517,9 @@ def __init__(; -587,9 +590,13 @@ def forward(; symbols: __init__, pad_input_ids, forward, load_weights, touching `__init__, pad_input_ids, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +24/-1 (25 lines); hunks: -517,6 +517,9 @@ def __init__(; -587,9 +590,13 @@ def forward(; symbols: __init__, pad_input_ids, forward, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -517,6 +517,9 @@ def __init__(
+        # For EAGLE3 support
+        self.capture_aux_hidden_states = False
@@ -587,9 +590,13 @@ def forward(
+        aux_hidden_states = None
+        if self.capture_aux_hidden_states:
+            hidden_states, aux_hidden_states = hidden_states
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +24/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/forward_batch_info.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10323 - model: support qwen3-vl series

- Link: https://github.com/sgl-project/sglang/pull/10323
- Status/date: merged / 2025-09-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `4f564b9e8378`
- Diff scope read: GitHub Pull Request files API returned 7 files, +1898/-8, 2006 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "model: support qwen3-vl series"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/configs/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`; technical summary: Covers "model: support qwen3-vl series"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/configs/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` added +787/-0 (787 lines); hunks: -0,0 +1,787; symbols: Qwen3_VisionMLP, __init__, forward, Qwen3VLVisionPatchEmbed, touching `Qwen3_VisionMLP, __init__, forward`; `python/sglang/srt/configs/qwen3_vl.py` added +586/-0 (586 lines); hunks: -0,0 +1,586; symbols: Qwen3VLVisionConfig, __init__, Qwen3VLTextConfig, to, touching `Qwen3VLVisionConfig, __init__, Qwen3VLTextConfig`; `python/sglang/srt/models/qwen3_vl_moe.py` added +471/-0 (471 lines); hunks: -0,0 +1,471; symbols: Qwen3MoeLLMModel, __init__, get_input_embeddings, get_image_feature, touching `Qwen3MoeLLMModel, __init__, get_input_embeddings`; `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +8/-1 (9 lines); hunks: -12,6 +12,8; -209,7 +211,12 @@ async def preprocess_video(; symbols: preprocess_video, Qwen2_5VLImageProcessor, __init__, touching `preprocess_video, Qwen2_5VLImageProcessor, __init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` added +787/-0 (787 lines); hunks: -0,0 +1,787; symbols: Qwen3_VisionMLP, __init__, forward, Qwen3VLVisionPatchEmbed
  - `python/sglang/srt/configs/qwen3_vl.py` added +586/-0 (586 lines); hunks: -0,0 +1,586; symbols: Qwen3VLVisionConfig, __init__, Qwen3VLTextConfig, to
  - `python/sglang/srt/models/qwen3_vl_moe.py` added +471/-0 (471 lines); hunks: -0,0 +1,471; symbols: Qwen3MoeLLMModel, __init__, get_input_embeddings, get_image_feature
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +8/-1 (9 lines); hunks: -12,6 +12,8; -209,7 +211,12 @@ async def preprocess_video(; symbols: preprocess_video, Qwen2_5VLImageProcessor, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -0,0 +1,787 @@
+# Copyright 2025 Qwen Team
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
diff -- python/sglang/srt/configs/qwen3_vl.py
@@ -0,0 +1,586 @@
+from typing import Optional, Union
+from transformers import PretrainedConfig
+from transformers.modeling_rope_utils import rope_config_validation
+class Qwen3VLVisionConfig(PretrainedConfig):
+    model_type = "qwen3_vl"
+    base_config_key = "vision_config"
diff -- python/sglang/srt/models/qwen3_vl_moe.py
@@ -0,0 +1,471 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` added +787/-0; `python/sglang/srt/configs/qwen3_vl.py` added +586/-0; `python/sglang/srt/models/qwen3_vl_moe.py` added +471/-0; `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +8/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_vl.py`, `python/sglang/srt/layers/rotary_embedding.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11481 - [smol] [perf] Qwen3-VL in place op.

- Link: https://github.com/sgl-project/sglang/pull/11481
- Status/date: merged / 2025-10-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`; associated commits `be740acdb0ad`
- Diff scope read: GitHub Pull Request files API returned 2 files, +7/-11, 55 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[smol] [perf] Qwen3-VL in place op."; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`; technical summary: Covers "[smol] [perf] Qwen3-VL in place op."; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +4/-7 (11 lines); hunks: -189,10 +189,10 @@ def forward(; -441,7 +441,7 @@ def forward(; symbols: forward, touching `forward`; `python/sglang/srt/models/qwen3_vl_moe.py` modified +3/-4 (7 lines); hunks: -114,7 +114,7 @@ def forward(; -130,9 +130,8 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +4/-7 (11 lines); hunks: -189,10 +189,10 @@ def forward(; -441,7 +441,7 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/qwen3_vl_moe.py` modified +3/-4 (7 lines); hunks: -114,7 +114,7 @@ def forward(; -130,9 +130,8 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -189,10 +189,10 @@ def forward(
-        x = x + attn
+        x += attn
-        x = x + mlp
+        x += mlp
@@ -441,7 +441,7 @@ def forward(
-        x = x + pos_embeds
diff -- python/sglang/srt/models/qwen3_vl_moe.py
@@ -114,7 +114,7 @@ def forward(
-            layer_idx = layer_idx + self.start_layer
+            layer_idx += self.start_layer
@@ -130,9 +130,8 @@ def forward(
-                hidden_states = (
-                    hidden_states
-                    + input_deepstack_embeds[:, sep : sep + self.hidden_size]
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +4/-7; `python/sglang/srt/models/qwen3_vl_moe.py` modified +3/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11458 - [BugFix][Qwen3-VL]: fix cu_seqlens in qwen3-vl

- Link: https://github.com/sgl-project/sglang/pull/11458
- Status/date: merged / 2025-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `b2c856692092`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-3, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix][Qwen3-VL]: fix cu_seqlens in qwen3-vl"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[BugFix][Qwen3-VL]: fix cu_seqlens in qwen3-vl"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +5/-3 (8 lines); hunks: -452,13 +452,15 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +5/-3 (8 lines); hunks: -452,13 +452,15 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -452,13 +452,15 @@ def forward(
+        cu_seqlens = torch.repeat_interleave(
+            grid_thw[:, 1] * grid_thw[:, 2], grid_thw[:, 0]
+        ).cumsum(dim=0)
-                torch.tensor([0], device=grid_thw.device),
-                (grid_thw[:, 0] * grid_thw[:, 1] * grid_thw[:, 2]).cumsum(dim=0),
+                torch.zeros(1, dtype=torch.int32, device=cu_seqlens.device),
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +5/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #10911 - model: qwen3-omni (thinker-only)

- Link: https://github.com/sgl-project/sglang/pull/10911
- Status/date: merged / 2025-10-16
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_omni.py`, `python/sglang/srt/configs/qwen3_vl.py`, `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py` and 6 files; associated commits `86b04d25b3f6`
- Diff scope read: GitHub Pull Request files API returned 16 files, +1947/-328, 2837 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "model: qwen3-omni (thinker-only)"; model line: Qwen VLM/Omni/ASR; category: model implementation change; main diff: `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/configs/qwen3_omni.py`, `python/sglang/srt/models/qwen3_vl_moe.py`; technical summary: Covers "model: qwen3-omni (thinker-only)"; the main implementation surface is `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/configs/qwen3_omni.py`, `python/sglang/srt/models/qwen3_vl_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_omni_moe.py` added +661/-0 (661 lines); hunks: -0,0 +1,661; symbols: Qwen3OmniMoeAudioEncoderLayer, __init__, forward, SinusoidsPositionEmbedding, touching `Qwen3OmniMoeAudioEncoderLayer, __init__, forward`; `python/sglang/srt/configs/qwen3_omni.py` added +613/-0 (613 lines); hunks: -0,0 +1,613; symbols: Qwen3OmniMoeAudioEncoderConfig, __init__, Qwen3OmniMoeVisionEncoderConfig, Qwen3OmniMoeTextConfig, touching `Qwen3OmniMoeAudioEncoderConfig, __init__, Qwen3OmniMoeVisionEncoderConfig`; `python/sglang/srt/models/qwen3_vl_moe.py` modified +53/-168 (221 lines); hunks: -14,41 +14,27; -60,28 +46,16 @@ class Qwen3MoeLLMModel(Qwen3MoeModel):; symbols: Qwen3MoeLLMModel, __init__, get_input_embeddings, get_image_feature, touching `Qwen3MoeLLMModel, __init__, get_input_embeddings`; `python/sglang/srt/models/qwen3_vl.py` modified +38/-24 (62 lines); hunks: -15,7 +15,7; -27,7 +27,11; symbols: forward, Qwen3_VisionPatchMerger, Qwen3VLMoeVisionPatchMerger, __init__, touching `forward, Qwen3_VisionPatchMerger, Qwen3VLMoeVisionPatchMerger`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_omni_moe.py` added +661/-0 (661 lines); hunks: -0,0 +1,661; symbols: Qwen3OmniMoeAudioEncoderLayer, __init__, forward, SinusoidsPositionEmbedding
  - `python/sglang/srt/configs/qwen3_omni.py` added +613/-0 (613 lines); hunks: -0,0 +1,613; symbols: Qwen3OmniMoeAudioEncoderConfig, __init__, Qwen3OmniMoeVisionEncoderConfig, Qwen3OmniMoeTextConfig
  - `python/sglang/srt/models/qwen3_vl_moe.py` modified +53/-168 (221 lines); hunks: -14,41 +14,27; -60,28 +46,16 @@ class Qwen3MoeLLMModel(Qwen3MoeModel):; symbols: Qwen3MoeLLMModel, __init__, get_input_embeddings, get_image_feature
  - `python/sglang/srt/models/qwen3_vl.py` modified +38/-24 (62 lines); hunks: -15,7 +15,7; -27,7 +27,11; symbols: forward, Qwen3_VisionPatchMerger, Qwen3VLMoeVisionPatchMerger, __init__
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +40/-6 (46 lines); hunks: -12,6 +12,7; -209,22 +210,31 @@ async def preprocess_video(; symbols: preprocess_video, Qwen2_5VLImageProcessor, QwenVLImageProcessor, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_omni_moe.py
@@ -0,0 +1,661 @@
+# Copyright 2025 Qwen Team
+# Copyright 2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
diff -- python/sglang/srt/configs/qwen3_omni.py
@@ -0,0 +1,613 @@
+from transformers import PretrainedConfig
+from transformers.configuration_utils import layer_type_validation
+from transformers.modeling_rope_utils import rope_config_validation
+from sglang.utils import logger
+class Qwen3OmniMoeAudioEncoderConfig(PretrainedConfig):
+    model_type = "qwen3_omni_moe_audio_encoder"
diff -- python/sglang/srt/models/qwen3_vl_moe.py
@@ -14,41 +14,27 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_omni_moe.py` added +661/-0; `python/sglang/srt/configs/qwen3_omni.py` added +613/-0; `python/sglang/srt/models/qwen3_vl_moe.py` modified +53/-168; `python/sglang/srt/models/qwen3_vl.py` modified +38/-24; `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +40/-6; `python/sglang/srt/configs/qwen3_vl.py` modified +0/-10
- Risk and verification: The diff ships test coverage in `test/srt/test_vision_openai_server_a.py`, `test/srt/test_vision_openai_server_b.py`, `test/srt/test_vision_openai_server_common.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #11377 - [BugFix][Qwen3-VL]: add metadata for video in qwen3-vl

- Link: https://github.com/sgl-project/sglang/pull/11377
- Status/date: merged / 2025-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `fde2decf8b59`
- Diff scope read: GitHub Pull Request files API returned 1 files, +26/-8, 49 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix][Qwen3-VL]: add metadata for video in qwen3-vl"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/multimodal/processors/qwen_vl.py`; technical summary: Covers "[BugFix][Qwen3-VL]: add metadata for video in qwen3-vl"; the main implementation surface is `python/sglang/srt/multimodal/processors/qwen_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +26/-8 (34 lines); hunks: -214,7 +214,14 @@ async def preprocess_video(; -279,14 +286,25 @@ async def process_mm_data_async(; symbols: preprocess_video, process_mm_data_async, touching `preprocess_video, process_mm_data_async`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +26/-8 (34 lines); hunks: -214,7 +214,14 @@ async def preprocess_video(; -279,14 +286,25 @@ async def process_mm_data_async(; symbols: preprocess_video, process_mm_data_async
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -214,7 +214,14 @@ async def preprocess_video(
-    return video
+    video_metadata = {
+        "fps": video_fps,
+        "duration": total_frames / video_fps,
+        "total_num_frames": total_frames,
+        "frames_indices": idx,
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +26/-8
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/qwen_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12240 - [VLM] Optimize qwen_vl preprocess_video

- Link: https://github.com/sgl-project/sglang/pull/12240
- Status/date: merged / 2025-11-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `fd3034da7515`
- Diff scope read: GitHub Pull Request files API returned 1 files, +43/-10, 131 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Optimize qwen_vl preprocess_video"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/multimodal/processors/qwen_vl.py`; technical summary: Covers "[VLM] Optimize qwen_vl preprocess_video"; the main implementation surface is `python/sglang/srt/multimodal/processors/qwen_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +43/-10 (53 lines); hunks: -2,8 +2,10; -175,19 +177,25 @@ async def preprocess_video(; symbols: preprocess_video, process_mm_data_async, touching `preprocess_video, process_mm_data_async`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +43/-10 (53 lines); hunks: -2,8 +2,10; -175,19 +177,25 @@ async def preprocess_video(; symbols: preprocess_video, process_mm_data_async
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -2,8 +2,10 @@
+import time
+import numpy as np
@@ -175,19 +177,25 @@ async def preprocess_video(
+    entry_time = time.perf_counter()
-    idx = torch.linspace(0, total_frames - 1, nframes).round().long().tolist()
-    video = vr.get_batch(idx).asnumpy()
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +43/-10
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/qwen_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12458 - fix: duplicate resize images logic of qwen-vl series models

- Link: https://github.com/sgl-project/sglang/pull/12458
- Status/date: merged / 2025-11-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `ffeb28ba6fb7`
- Diff scope read: GitHub Pull Request files API returned 3 files, +1/-67, 136 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: duplicate resize images logic of qwen-vl series models"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/multimodal/processors/qwen_vl.py`; technical summary: Covers "fix: duplicate resize images logic of qwen-vl series models"; the main implementation surface is `python/sglang/srt/multimodal/processors/qwen_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +0/-40 (40 lines); hunks: -1,4 +1,3; -79,26 +78,6 @@ def smart_resize(; symbols: smart_resize, resize_image, round_by_factor, floor_by_factor, touching `smart_resize, resize_image, round_by_factor`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +0/-40 (40 lines); hunks: -1,4 +1,3; -79,26 +78,6 @@ def smart_resize(; symbols: smart_resize, resize_image, round_by_factor, floor_by_factor
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -1,4 +1,3 @@
-import asyncio
@@ -79,26 +78,6 @@ def smart_resize(
-def resize_image(
-    image,
-    min_pixels: int = MIN_PIXELS,
-    max_pixels: int = MAX_PIXELS,
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +0/-40
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/dots_vlm.py`, `python/sglang/srt/multimodal/processors/points_v15_chat.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13075 - [VLM] Support PP for Qwen2.5-VL

- Link: https://github.com/sgl-project/sglang/pull/13075
- Status/date: merged / 2025-11-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`; associated commits `706502ff6cff`
- Diff scope read: GitHub Pull Request files API returned 3 files, +88/-54, 244 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Support PP for Qwen2.5-VL"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "[VLM] Support PP for Qwen2.5-VL"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +44/-15 (59 lines); hunks: -40,6 +40,7; -50,13 +51,14; symbols: __init__, forward, load_weights, touching `__init__, forward, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +44/-15 (59 lines); hunks: -40,6 +40,7; -50,13 +51,14; symbols: __init__, forward, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -40,6 +40,7 @@
+from sglang.srt.distributed.parallel_state import get_pp_group
@@ -50,13 +51,14 @@
+from sglang.srt.layers.utils import PPMissingLayer, get_layer_id
-from sglang.srt.model_executor.forward_batch_info import ForwardBatch
+from sglang.srt.model_executor.forward_batch_info import ForwardBatch, PPProxyTensors
@@ -482,6 +484,7 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +44/-15
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/models/qwen2_5_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13126 - [VLM][feat] Support encoder DP for Qwen2.5-VL

- Link: https://github.com/sgl-project/sglang/pull/13126
- Status/date: merged / 2025-11-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`; associated commits `ac81db66c2d8`
- Diff scope read: GitHub Pull Request files API returned 6 files, +595/-6, 790 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM][feat] Support encoder DP for Qwen2.5-VL"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "[VLM][feat] Support encoder DP for Qwen2.5-VL"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +44/-2 (46 lines); hunks: -40,6 +40,10; -62,6 +66,8; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +44/-2 (46 lines); hunks: -40,6 +40,10; -62,6 +66,8; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -40,6 +40,10 @@
+from sglang.srt.distributed import (
+    get_tensor_model_parallel_rank,
+    get_tensor_model_parallel_world_size,
+)
@@ -62,6 +66,8 @@
+from sglang.srt.multimodal.mm_utils import run_dp_sharded_mrope_vision_model
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +44/-2
- Risk and verification: The diff ships test coverage in `test/srt/nightly/test_encoder_dp.py`, `test/srt/run_suite.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #13055 - [VLM] Support Piecewise CUDA Graph for Qwen2.5-VL

- Link: https://github.com/sgl-project/sglang/pull/13055
- Status/date: merged / 2025-11-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`; associated commits `af6bcadcf723`
- Diff scope read: GitHub Pull Request files API returned 10 files, +710/-29, 970 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Support Piecewise CUDA Graph for Qwen2.5-VL"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`; technical summary: Covers "[VLM] Support Piecewise CUDA Graph for Qwen2.5-VL"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen2_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +38/-7 (45 lines); hunks: -57,11 +57,12; -566,6 +567,25 @@ def get_video_feature(self, items: List[MultimodalDataItem]...; symbols: get_video_feature, post_process, get_input_embeddings, forward, touching `get_video_feature, post_process, get_input_embeddings`; `python/sglang/srt/models/qwen2_vl.py` modified +16/-7 (23 lines); hunks: -39,10 +39,7; -509,6 +506,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +38/-7 (45 lines); hunks: -57,11 +57,12; -566,6 +567,25 @@ def get_video_feature(self, items: List[MultimodalDataItem]...; symbols: get_video_feature, post_process, get_input_embeddings, forward
  - `python/sglang/srt/models/qwen2_vl.py` modified +16/-7 (23 lines); hunks: -39,10 +39,7; -509,6 +506,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -57,11 +57,12 @@
-from sglang.srt.managers.mm_utils import (
-    MultiModalityDataPaddingPatternMultimodalTokens,
-    general_mm_embed_routine,
+from sglang.srt.managers.mm_utils import MultiModalityDataPaddingPatternMultimodalTokens
+from sglang.srt.managers.schedule_batch import (
+    Modality,
diff -- python/sglang/srt/models/qwen2_vl.py
@@ -39,10 +39,7 @@
-from sglang.srt.managers.mm_utils import (
-    MultiModalityDataPaddingPatternMultimodalTokens,
-    general_mm_embed_routine,
-)
+from sglang.srt.managers.mm_utils import MultiModalityDataPaddingPatternMultimodalTokens
@@ -509,6 +506,7 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +38/-7; `python/sglang/srt/models/qwen2_vl.py` modified +16/-7
- Risk and verification: The diff ships test coverage in `test/srt/nightly/test_vlms_piecewise_cuda_graph.py`, `test/srt/run_suite.py`, `test/srt/test_piecewise_cuda_graph.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #13736 - [VLM] Replace torch.repeat_interleave with faster np.repeat for Qwen-VL series

- Link: https://github.com/sgl-project/sglang/pull/13736
- Status/date: merged / 2025-11-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_vl.py`, `python/sglang/srt/models/qwen3_vl.py`; associated commits `5625e32cae12`
- Diff scope read: GitHub Pull Request files API returned 5 files, +169/-13, 229 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Replace torch.repeat_interleave with faster np.repeat for Qwen-VL series"; model line: Qwen VLM/Omni/ASR; category: model implementation change; main diff: `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen2_vl.py`; technical summary: Covers "[VLM] Replace torch.repeat_interleave with faster np.repeat for Qwen-VL series"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen2_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +2/-9 (11 lines); hunks: -46,6 +46,7; -434,15 +435,7 @@ def forward(; symbols: forward, touching `forward`; `python/sglang/srt/models/qwen2_vl.py` modified +2/-4 (6 lines); hunks: -44,6 +44,7; -387,10 +388,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +2/-9 (11 lines); hunks: -46,6 +46,7; -434,15 +435,7 @@ def forward(; symbols: forward
  - `python/sglang/srt/models/qwen2_vl.py` modified +2/-4 (6 lines); hunks: -44,6 +44,7; -387,10 +388,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -46,6 +46,7 @@
+from sglang.srt.models.utils import compute_cu_seqlens_from_grid_numpy
@@ -434,15 +435,7 @@ def forward(
-        cu_seqlens = torch.repeat_interleave(
-            grid_thw[:, 1] * grid_thw[:, 2], grid_thw[:, 0]
-        ).cumsum(dim=0)
-        cu_seqlens = torch.cat(
diff -- python/sglang/srt/models/qwen2_vl.py
@@ -44,6 +44,7 @@
+from sglang.srt.models.utils import compute_cu_seqlens_from_grid_numpy
@@ -387,10 +388,7 @@ def forward(
-        cu_seqlens = torch.repeat_interleave(
-            grid_thw[:, 1] * grid_thw[:, 2], grid_thw[:, 0]
-        ).cumsum(dim=0, dtype=torch.int32)
-        cu_seqlens = torch.cat([cu_seqlens.new_zeros(1), cu_seqlens])
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +2/-9; `python/sglang/srt/models/qwen2_vl.py` modified +2/-4
- Risk and verification: The diff ships test coverage in `test/srt/ops/test_repeat_interleave.py`, `test/srt/run_suite.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #13983 - Support KTransformers for Qwen3-VL moe

- Link: https://github.com/sgl-project/sglang/pull/13983
- Status/date: merged / 2025-11-26
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl_moe.py`; associated commits `15ff6982b94f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-0, 22 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Support KTransformers for Qwen3-VL moe"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_vl_moe.py`; technical summary: Covers "Support KTransformers for Qwen3-VL moe"; the main implementation surface is `python/sglang/srt/models/qwen3_vl_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl_moe.py` modified +9/-0 (9 lines); hunks: -22,6 +22,7; -326,5 +327,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, get_model_config_for_expert_location, touching `load_weights, get_model_config_for_expert_location`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl_moe.py` modified +9/-0 (9 lines); hunks: -22,6 +22,7; -326,5 +327,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, get_model_config_for_expert_location
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl_moe.py
@@ -22,6 +22,7 @@
+from sglang.srt.eplb.expert_location import ModelConfigForExpertLocation
@@ -326,5 +327,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+    @classmethod
+    def get_model_config_for_expert_location(cls, config):
+        return ModelConfigForExpertLocation(
+            num_layers=config.text_config.num_hidden_layers,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl_moe.py` modified +9/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_vl_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13904 - [Bugfix] qwen2.5-vl spec decode accept_len low

- Link: https://github.com/sgl-project/sglang/pull/13904
- Status/date: merged / 2025-11-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`; associated commits `f6e37d3edb94`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] qwen2.5-vl spec decode accept_len low"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "[Bugfix] qwen2.5-vl spec decode accept_len low"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +1/-0 (1 lines); hunks: -654,6 +654,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +1/-0 (1 lines); hunks: -654,6 +654,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -654,6 +654,7 @@ def forward(
+                    aux_hidden_states,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen2_5_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #13724 - support qwen3_vl vision model dp

- Link: https://github.com/sgl-project/sglang/pull/13724
- Status/date: merged / 2025-11-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `ea1e9f6b3c3d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +50/-2, 208 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "support qwen3_vl vision model dp"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "support qwen3_vl vision model dp"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +49/-2 (51 lines); hunks: -28,6 +28,10; -47,6 +51,8; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +49/-2 (51 lines); hunks: -28,6 +28,10; -47,6 +51,8; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -28,6 +28,10 @@
+from sglang.srt.distributed import (
+    get_tensor_model_parallel_rank,
+    get_tensor_model_parallel_world_size,
+)
@@ -47,6 +51,8 @@
+from sglang.srt.multimodal.mm_utils import run_dp_sharded_mrope_vision_model
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +49/-2
- Risk and verification: The diff ships test coverage in `test/nightly/test_encoder_dp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #14292 - [VLM] Introduce Cache for positional embedding ids for Qwen-VL family

- Link: https://github.com/sgl-project/sglang/pull/14292
- Status/date: merged / 2025-12-04
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`; associated commits `b2b09f5f24b9`
- Diff scope read: GitHub Pull Request files API returned 3 files, +48/-47, 149 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Introduce Cache for positional embedding ids for Qwen-VL family"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[VLM] Introduce Cache for positional embedding ids for Qwen-VL family"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +5/-25 (30 lines); hunks: -69,7 +69,7; -246,7 +246,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward, Qwen2_5_VisionTransformer, __init__, device, touching `forward, Qwen2_5_VisionTransformer, __init__`; `python/sglang/srt/models/qwen3_vl.py` modified +5/-22 (27 lines); hunks: -50,7 +50,7; -257,7 +257,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward, Qwen3VLMoeVisionModel, __init__, device, touching `forward, Qwen3VLMoeVisionModel, __init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +5/-25 (30 lines); hunks: -69,7 +69,7; -246,7 +246,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward, Qwen2_5_VisionTransformer, __init__, device
  - `python/sglang/srt/models/qwen3_vl.py` modified +5/-22 (27 lines); hunks: -50,7 +50,7; -257,7 +257,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:; symbols: forward, Qwen3VLMoeVisionModel, __init__, device
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -69,7 +69,7 @@
-from sglang.srt.models.utils import permute_inv
+from sglang.srt.models.utils import RotaryPosMixin, permute_inv
@@ -246,7 +246,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:
-class Qwen2_5_VisionTransformer(nn.Module):
+class Qwen2_5_VisionTransformer(nn.Module, RotaryPosMixin):
@@ -362,30 +362,10 @@ def device(self) -> torch.device:
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -50,7 +50,7 @@
-from sglang.srt.models.utils import compute_cu_seqlens_from_grid_numpy
+from sglang.srt.models.utils import RotaryPosMixin, compute_cu_seqlens_from_grid_numpy
@@ -257,7 +257,7 @@ def forward(self, x: torch.Tensor) -> torch.Tensor:
-class Qwen3VLMoeVisionModel(nn.Module):
+class Qwen3VLMoeVisionModel(nn.Module, RotaryPosMixin):
@@ -339,26 +339,9 @@ def device(self) -> torch.device:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +5/-25; `python/sglang/srt/models/qwen3_vl.py` modified +5/-22
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #11791 - fix rmsnorm -> layernorm in qwen3 omni

- Link: https://github.com/sgl-project/sglang/pull/11791
- Status/date: merged / 2025-12-06
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_omni_moe.py`; associated commits `2ac5b9839508`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-2, 17 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix rmsnorm -> layernorm in qwen3 omni"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen3_omni_moe.py`; technical summary: Covers "fix rmsnorm -> layernorm in qwen3 omni"; the main implementation surface is `python/sglang/srt/models/qwen3_omni_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_omni_moe.py` modified +1/-2 (3 lines); hunks: -31,7 +31,6; -318,7 +317,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_omni_moe.py` modified +1/-2 (3 lines); hunks: -31,7 +31,6; -318,7 +317,7 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_omni_moe.py
@@ -31,7 +31,6 @@
-from sglang.srt.layers.layernorm import RMSNorm
@@ -318,7 +317,7 @@ def __init__(
-        self.ln_q = RMSNorm(
+        self.ln_q = nn.LayerNorm(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_omni_moe.py` modified +1/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_omni_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12333 - [PP] Add pp support for Qwen3-VL

- Link: https://github.com/sgl-project/sglang/pull/12333
- Status/date: merged / 2025-12-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl.py`; associated commits `45a959d3e971`
- Diff scope read: GitHub Pull Request files API returned 5 files, +119/-20, 243 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[PP] Add pp support for Qwen3-VL"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_omni_moe.py`; technical summary: Covers "[PP] Add pp support for Qwen3-VL"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_omni_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +53/-19 (72 lines); hunks: -32,11 +32,13; -599,6 +601,7 @@ def __init__(; symbols: __init__, forward, load_weights, touching `__init__, forward, load_weights`; `python/sglang/srt/models/qwen3_omni_moe.py` modified +4/-1 (5 lines); hunks: -614,7 +614,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +53/-19 (72 lines); hunks: -32,11 +32,13; -599,6 +601,7 @@ def __init__(; symbols: __init__, forward, load_weights
  - `python/sglang/srt/models/qwen3_omni_moe.py` modified +4/-1 (5 lines); hunks: -614,7 +614,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -32,11 +32,13 @@
+from sglang.srt.distributed.parallel_state import get_pp_group
+from sglang.srt.layers.utils import PPMissingLayer, get_layer_id
@@ -599,6 +601,7 @@ def __init__(
+        self.pp_group = get_pp_group()
@@ -626,19 +629,22 @@ def __init__(
-            if self.config.tie_word_embeddings:
diff -- python/sglang/srt/models/qwen3_omni_moe.py
@@ -614,7 +614,10 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-                        param = params_dict[name_mapped]
+                        if name_mapped in params_dict.keys():
+                            param = params_dict[name_mapped]
+                        else:
+                            continue
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +53/-19; `python/sglang/srt/models/qwen3_omni_moe.py` modified +4/-1
- Risk and verification: The diff ships test coverage in `python/sglang/test/test_utils.py`, `test/srt/test_pp_single_node.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #15138 - [bug fix][pp] fix weight load for qwen2.5-vl

- Link: https://github.com/sgl-project/sglang/pull/15138
- Status/date: merged / 2025-12-17
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`; associated commits `0071fe9c407a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +10/-4, 28 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[bug fix][pp] fix weight load for qwen2.5-vl"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "[bug fix][pp] fix weight load for qwen2.5-vl"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +10/-4 (14 lines); hunks: -743,6 +743,14 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -789,10 +797,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +10/-4 (14 lines); hunks: -743,6 +743,14 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; -789,10 +797,8 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -743,6 +743,14 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+            if self.pp_group.is_last_rank and "model.embed_tokens.weight" in name:
+                if "lm_head.weight" in params_dict:
+                    lm_head_param = params_dict["lm_head.weight"]
+                    weight_loader = getattr(
+                        lm_head_param, "weight_loader", default_weight_loader
+                    )
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +10/-4
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen2_5_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15205 - [VLM] Support cos sin cache for Qwen3-VL & GLM-4.1V

- Link: https://github.com/sgl-project/sglang/pull/15205
- Status/date: merged / 2025-12-18
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `8fa3dc36c565`
- Diff scope read: GitHub Pull Request files API returned 4 files, +100/-80, 345 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Support cos sin cache for Qwen3-VL & GLM-4.1V"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[VLM] Support cos sin cache for Qwen3-VL & GLM-4.1V"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +41/-20 (61 lines); hunks: -24,9 +24,6; -39,6 +36,7; symbols: forward, __init__, dtype, device, touching `forward, __init__, dtype`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +41/-20 (61 lines); hunks: -24,9 +24,6; -39,6 +36,7; symbols: forward, __init__, dtype, device
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -24,9 +24,6 @@
-from transformers.models.qwen2_5_vl.modeling_qwen2_5_vl import (
-    Qwen2_5_VisionRotaryEmbedding,
-)
@@ -39,6 +36,7 @@
+from sglang.srt.layers.rotary_embedding import get_rope
@@ -188,14 +186,16 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +41/-20
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/rotary_embedding.py`, `python/sglang/srt/models/glm4v.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15320 - [VLM] Support ViT Piecewise CUDA Graph for Qwen3-VL

- Link: https://github.com/sgl-project/sglang/pull/15320
- Status/date: merged / 2025-12-20
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`; associated commits `019517a35610`
- Diff scope read: GitHub Pull Request files API returned 6 files, +233/-64, 497 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Support ViT Piecewise CUDA Graph for Qwen3-VL"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`; technical summary: Covers "[VLM] Support ViT Piecewise CUDA Graph for Qwen3-VL"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen2_5_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +52/-1 (53 lines); hunks: -57,8 +57,9; -188,6 +189,7 @@ def forward(; symbols: forward, __init__, dtype, touching `forward, __init__, dtype`; `python/sglang/srt/models/qwen2_5_vl.py` modified +2/-3 (5 lines); hunks: -170,7 +170,6 @@ def forward(; -182,7 +181,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +52/-1 (53 lines); hunks: -57,8 +57,9; -188,6 +189,7 @@ def forward(; symbols: forward, __init__, dtype
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +2/-3 (5 lines); hunks: -170,7 +170,6 @@ def forward(; -182,7 +181,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -57,8 +57,9 @@
+from sglang.srt.multimodal.vit_cuda_graph_runner import ViTCudaGraphRunner
-from sglang.srt.utils import add_prefix, get_int_env_var
+from sglang.srt.utils import add_prefix, get_bool_env_var, get_int_env_var
@@ -188,6 +189,7 @@ def forward(
+        output_ws: Optional[torch.Tensor] = None,
@@ -196,6 +198,7 @@ def forward(
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -170,7 +170,6 @@ def forward(
-        ws = output_ws
@@ -182,7 +181,7 @@ def forward(
-            output_ws=ws,
+            output_ws=output_ws,
@@ -390,7 +389,7 @@ def forward(
-        if get_bool_env_var("SGLANG_VIT_ENABLE_CUDA_GRAPH") and self.tp_size == 1:
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +52/-1; `python/sglang/srt/models/qwen2_5_vl.py` modified +2/-3
- Risk and verification: The diff ships test coverage in `test/manual/nightly/test_vlms_vit_cuda_graph.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #15570 - [GLM-ASR] GLM-ASR Support

- Link: https://github.com/sgl-project/sglang/pull/15570
- Status/date: merged / 2025-12-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py`; associated commits `82f1d6157f8e`
- Diff scope read: GitHub Pull Request files API returned 4 files, +226/-1, 250 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[GLM-ASR] GLM-ASR Support"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py`; technical summary: Covers "[GLM-ASR] GLM-ASR Support"; the main implementation surface is `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glmasr.py` added +171/-0 (171 lines); hunks: -0,0 +1,171; symbols: GlmasrForConditionalGeneration, __init__, pad_input_ids, get_audio_feature, touching `GlmasrForConditionalGeneration, __init__, pad_input_ids`; `python/sglang/srt/multimodal/processors/glmasr.py` added +53/-0 (53 lines); hunks: -0,0 +1,53; symbols: GlmasrProcessor, __init__, process_mm_data_async, touching `GlmasrProcessor, __init__, process_mm_data_async`.
- Code diff details:
  - `python/sglang/srt/models/glmasr.py` added +171/-0 (171 lines); hunks: -0,0 +1,171; symbols: GlmasrForConditionalGeneration, __init__, pad_input_ids, get_audio_feature
  - `python/sglang/srt/multimodal/processors/glmasr.py` added +53/-0 (53 lines); hunks: -0,0 +1,53; symbols: GlmasrProcessor, __init__, process_mm_data_async
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glmasr.py
@@ -0,0 +1,171 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
diff -- python/sglang/srt/multimodal/processors/glmasr.py
@@ -0,0 +1,53 @@
+import re
+from sglang.srt.models.glmasr import GlmasrForConditionalGeneration
+from sglang.srt.multimodal.processors.base_processor import (
+    BaseMultimodalProcessor,
+    MultimodalSpecialTokens,
+)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glmasr.py` added +171/-0; `python/sglang/srt/multimodal/processors/glmasr.py` added +53/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/base_processor.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #15772 - Change GLM-ASR class name

- Link: https://github.com/sgl-project/sglang/pull/15772
- Status/date: merged / 2025-12-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py`; associated commits `f3ba71166262`
- Diff scope read: GitHub Pull Request files API returned 5 files, +19/-15, 103 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Change GLM-ASR class name"; model line: Qwen VLM/Omni/ASR; category: model implementation change; main diff: `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py`; technical summary: Covers "Change GLM-ASR class name"; the main implementation surface is `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/glmasr.py` modified +9/-9 (18 lines); hunks: -22,10 +22,10; -46,7 +46,7; symbols: GlmasrForConditionalGeneration, GlmAsrForConditionalGeneration, __init__, touching `GlmasrForConditionalGeneration, GlmAsrForConditionalGeneration, __init__`; `python/sglang/srt/multimodal/processors/glmasr.py` modified +3/-3 (6 lines); hunks: -1,14 +1,14; symbols: GlmasrProcessor, GlmAsrProcessor, __init__, touching `GlmasrProcessor, GlmAsrProcessor, __init__`.
- Code diff details:
  - `python/sglang/srt/models/glmasr.py` modified +9/-9 (18 lines); hunks: -22,10 +22,10; -46,7 +46,7; symbols: GlmasrForConditionalGeneration, GlmAsrForConditionalGeneration, __init__
  - `python/sglang/srt/multimodal/processors/glmasr.py` modified +3/-3 (6 lines); hunks: -1,14 +1,14; symbols: GlmasrProcessor, GlmAsrProcessor, __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/glmasr.py
@@ -22,10 +22,10 @@
-from transformers import GlmasrConfig, GlmasrEncoderConfig
+from transformers import GlmAsrConfig, GlmAsrEncoderConfig
-    GlmasrEncoder,
-    GlmasrMultiModalProjector,
+    GlmAsrEncoder,
+    GlmAsrMultiModalProjector,
diff -- python/sglang/srt/multimodal/processors/glmasr.py
@@ -1,14 +1,14 @@
-from sglang.srt.models.glmasr import GlmasrForConditionalGeneration
+from sglang.srt.models.glmasr import GlmAsrForConditionalGeneration
-class GlmasrProcessor(BaseMultimodalProcessor):
-    models = [GlmasrForConditionalGeneration]
+class GlmAsrProcessor(BaseMultimodalProcessor):
+    models = [GlmAsrForConditionalGeneration]
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/glmasr.py` modified +9/-9; `python/sglang/srt/multimodal/processors/glmasr.py` modified +3/-3
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/models/glmasr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16366 - Optimize Qwen3-VL video memory usage

- Link: https://github.com/sgl-project/sglang/pull/16366
- Status/date: merged / 2026-01-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `0c2993eed03a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-0, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Optimize Qwen3-VL video memory usage"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "Optimize Qwen3-VL video memory usage"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +8/-0 (8 lines); hunks: -852,10 +852,18 @@ def get_image_feature(self, items: List[MultimodalDataItem...; symbols: get_image_feature, get_video_feature, touching `get_image_feature, get_video_feature`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +8/-0 (8 lines); hunks: -852,10 +852,18 @@ def get_image_feature(self, items: List[MultimodalDataItem...; symbols: get_image_feature, get_video_feature
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -852,10 +852,18 @@ def get_image_feature(self, items: List[MultimodalDataItem]) -> torch.Tensor:
+        for item in items:
+            item.feature = item.feature.to(self.visual.device)
+        # Memory optimization for item.feature:
+        # 1. item.feature is released when request finished
+        # 2. High concurrency may cause device OOM due to delayed release
+        # 3. Fix: Offload item.feature to CPU, move to device only when needed
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +8/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18024 - fix: correct weight loading prefix mapping for Qwen3-VL

- Link: https://github.com/sgl-project/sglang/pull/18024
- Status/date: merged / 2026-02-02
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `522e13b4d2c1`
- Diff scope read: GitHub Pull Request files API returned 1 files, +7/-1, 15 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix: correct weight loading prefix mapping for Qwen3-VL"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "fix: correct weight loading prefix mapping for Qwen3-VL"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +7/-1 (8 lines); hunks: -959,7 +959,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +7/-1 (8 lines); hunks: -959,7 +959,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.T...; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -959,7 +959,13 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
-            if self.pp_group.is_last_rank and "model.embed_tokens.weight" in name:
+            # Only copy embed_tokens to lm_head when tie_word_embeddings=True
+            # For models with tie_word_embeddings=False (e.g. 8B), lm_head has independent weights
+            if (
+                self.pp_group.is_last_rank
+                and "model.embed_tokens.weight" in name
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +7/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #16781 - Refactor(qwen3-vl) optimize position encoding interpolation

- Link: https://github.com/sgl-project/sglang/pull/16781
- Status/date: merged / 2026-02-05
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `6a4b81e2d9fc`
- Diff scope read: GitHub Pull Request files API returned 2 files, +126/-25, 175 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Refactor(qwen3-vl) optimize position encoding interpolation"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "Refactor(qwen3-vl) optimize position encoding interpolation"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +123/-23 (146 lines); hunks: -19,6 +19,7; -396,31 +397,130 @@ def rot_pos_emb(; symbols: rot_pos_emb, fast_pos_embed_interpolate, _get_interpolation_indices, _calculate_indices_and_weights, touching `rot_pos_emb, fast_pos_embed_interpolate, _get_interpolation_indices`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +123/-23 (146 lines); hunks: -19,6 +19,7; -396,31 +397,130 @@ def rot_pos_emb(; symbols: rot_pos_emb, fast_pos_embed_interpolate, _get_interpolation_indices, _calculate_indices_and_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -19,6 +19,7 @@
+import numpy as np
@@ -396,31 +397,130 @@ def rot_pos_emb(
-    def fast_pos_embed_interpolate(self, grid_thw):
-        patch_pos_embeds_permute = []
-        m_size = self.spatial_merge_size
-        embeds = torch.arange(self.num_grid, device=self.pos_embed.weight.device)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +123/-23
- Risk and verification: The diff ships test coverage in `test/srt/test_embed_interpolate_unittest.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #19333 - fix qwen3_vl visual module loading

- Link: https://github.com/sgl-project/sglang/pull/19333
- Status/date: merged / 2026-02-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `d566816d838c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix qwen3_vl visual module loading"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "fix qwen3_vl visual module loading"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +1/-0 (1 lines); hunks: -1357,6 +1357,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: load_weights, touching `load_weights`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +1/-0 (1 lines); hunks: -1357,6 +1357,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch....; symbols: load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -1357,6 +1357,7 @@ def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
+                    name = name.replace(r"model.visual.", r"visual.")
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #18185 - [Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker

- Link: https://github.com/sgl-project/sglang/pull/18185
- Status/date: merged / 2026-03-14
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_omni_moe.py`; associated commits `22e67876d6aa`
- Diff scope read: GitHub Pull Request files API returned 1 files, +52/-28, 130 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_omni_moe.py`; technical summary: Covers "[Omni] Optimize AudioEncoder for Qwen3_Omni_Thinker"; the main implementation surface is `python/sglang/srt/models/qwen3_omni_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_omni_moe.py` modified +52/-28 (80 lines); hunks: -70,8 +70,18 @@ def __init__(; -98,9 +108,9 @@ def forward(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_omni_moe.py` modified +52/-28 (80 lines); hunks: -70,8 +70,18 @@ def __init__(; -98,9 +108,9 @@ def forward(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_omni_moe.py
@@ -70,8 +70,18 @@ def __init__(
-        self.fc1 = nn.Linear(self.embed_dim, config.encoder_ffn_dim)
-        self.fc2 = nn.Linear(config.encoder_ffn_dim, self.embed_dim)
+        self.fc1 = ColumnParallelLinear(
+            self.embed_dim,
+            config.encoder_ffn_dim,
+            bias=True,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_omni_moe.py` modified +52/-28
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_omni_moe.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #21469 - [3/n] lora moe - Support Qwen3-VL-30B-A3B-Instruct

- Link: https://github.com/sgl-project/sglang/pull/21469
- Status/date: merged / 2026-04-01
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl_moe.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py`; associated commits `cffc95edf455`
- Diff scope read: GitHub Pull Request files API returned 3 files, +152/-235, 397 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[3/n] lora moe - Support Qwen3-VL-30B-A3B-Instruct"; model line: Qwen VLM/Omni/ASR; category: docs/tests/CI; main diff: `python/sglang/srt/models/qwen3_vl_moe.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py`; technical summary: Covers "[3/n] lora moe - Support Qwen3-VL-30B-A3B-Instruct"; the main implementation surface is `python/sglang/srt/models/qwen3_vl_moe.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl_moe.py` modified +1/-2 (3 lines); hunks: -179,9 +179,8 @@ def __init__(; symbols: __init__, should_apply_lora, touching `__init__, should_apply_lora`; `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: kl_v2, get_prompt_logprobs, TestLoRAQwen3VL_30B_A3B_Instruct_LogprobDiff, test_lora_qwen3_vl_30b_a3b_instruct_logprob_accuracy, touching `kl_v2, get_prompt_logprobs, TestLoRAQwen3VL_30B_A3B_Instruct_LogprobDiff`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl_moe.py` modified +1/-2 (3 lines); hunks: -179,9 +179,8 @@ def __init__(; symbols: __init__, should_apply_lora
  - `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py` added +151/-0 (151 lines); hunks: -0,0 +1,151; symbols: kl_v2, get_prompt_logprobs, TestLoRAQwen3VL_30B_A3B_Instruct_LogprobDiff, test_lora_qwen3_vl_30b_a3b_instruct_logprob_accuracy
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl_moe.py
@@ -179,9 +179,8 @@ def __init__(
-    # Only allow LoRA on attention projections within text layers for MoE.
-        r"^model\.layers\.(\d+)\.self_attn\.(?:qkv_proj|o_proj)$"
+        r"^(?:model\.layers\.(\d+)\.(?:self_attn\.(?:qkv_proj|o_proj)|mlp\.experts)|lm_head|model\.embed_tokens)$"
diff -- test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py
@@ -0,0 +1,151 @@
+# Copyright 2023-2025 SGLang Team
+# Licensed under the Apache License, Version 2.0 (the "License");
+# you may not use this file except in compliance with the License.
+# You may obtain a copy of the License at
+#
+#     http://www.apache.org/licenses/LICENSE-2.0
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl_moe.py` modified +1/-2
  - tests: `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py` added +151/-0
- Risk and verification: The diff ships test coverage in `test/manual/lora/test_lora_qwen3_vl.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22073 - [Feature] Adding Qwen3-asr Model Support

- Link: https://github.com/sgl-project/sglang/pull/22073
- Status/date: merged / 2026-04-07
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_asr.py`, `python/sglang/srt/models/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py`; associated commits `f6e85676b578`
- Diff scope read: GitHub Pull Request files API returned 10 files, +571/-11, 689 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Adding Qwen3-asr Model Support"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_asr.py`, `python/sglang/srt/configs/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py`; technical summary: Covers "[Feature] Adding Qwen3-asr Model Support"; the main implementation surface is `python/sglang/srt/models/qwen3_asr.py`, `python/sglang/srt/configs/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_asr.py` added +199/-0 (199 lines); hunks: -0,0 +1,199; symbols: Qwen3ASRForConditionalGeneration, __init__, pad_input_ids, get_audio_feature, touching `Qwen3ASRForConditionalGeneration, __init__, pad_input_ids`; `python/sglang/srt/configs/qwen3_asr.py` added +172/-0 (172 lines); hunks: -0,0 +1,172; symbols: Qwen3ASRThinkerConfig, __init__, Qwen3ASRConfig, get_text_config, touching `Qwen3ASRThinkerConfig, __init__, Qwen3ASRConfig`; `python/sglang/srt/multimodal/processors/qwen3_asr.py` added +95/-0 (95 lines); hunks: -0,0 +1,95; symbols: Qwen3ASRMultimodalProcessor, __init__, _build_transcription_prompt, compute_mrope_positions, touching `Qwen3ASRMultimodalProcessor, __init__, _build_transcription_prompt`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_asr.py` added +199/-0 (199 lines); hunks: -0,0 +1,199; symbols: Qwen3ASRForConditionalGeneration, __init__, pad_input_ids, get_audio_feature
  - `python/sglang/srt/configs/qwen3_asr.py` added +172/-0 (172 lines); hunks: -0,0 +1,172; symbols: Qwen3ASRThinkerConfig, __init__, Qwen3ASRConfig, get_text_config
  - `python/sglang/srt/multimodal/processors/qwen3_asr.py` added +95/-0 (95 lines); hunks: -0,0 +1,95; symbols: Qwen3ASRMultimodalProcessor, __init__, _build_transcription_prompt, compute_mrope_positions
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_asr.py
@@ -0,0 +1,199 @@
+"""Qwen3-ASR model compatible with HuggingFace weights"""
+import logging
+from typing import Any, Iterable, List, Optional, Tuple
+import torch
+import torch.nn as nn
+from sglang.srt.configs.qwen3_asr import Qwen3ASRConfig
diff -- python/sglang/srt/configs/qwen3_asr.py
@@ -0,0 +1,172 @@
+import torch
+from transformers import (
+    AutoConfig,
+    AutoFeatureExtractor,
+    AutoTokenizer,
+    PretrainedConfig,
diff -- python/sglang/srt/multimodal/processors/qwen3_asr.py
@@ -0,0 +1,95 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_asr.py` added +199/-0; `python/sglang/srt/configs/qwen3_asr.py` added +172/-0; `python/sglang/srt/multimodal/processors/qwen3_asr.py` added +95/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/qwen3_asr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22181 - [refactor] [asr] Add transcription adapter for extensible ASR models support

- Link: https://github.com/sgl-project/sglang/pull/22181
- Status/date: merged / 2026-04-08
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_asr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py`, `test/manual/models/test_qwen3_asr.py`; associated commits `a5ed507a1639`
- Diff scope read: GitHub Pull Request files API returned 8 files, +473/-223, 809 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[refactor] [asr] Add transcription adapter for extensible ASR models support"; model line: Qwen VLM/Omni/ASR; category: docs/tests/CI; main diff: `python/sglang/srt/configs/qwen3_asr.py`, `test/manual/models/test_qwen3_asr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py`; technical summary: Covers "[refactor] [asr] Add transcription adapter for extensible ASR models support"; the main implementation surface is `python/sglang/srt/configs/qwen3_asr.py`, `test/manual/models/test_qwen3_asr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/configs/qwen3_asr.py` modified +63/-67 (130 lines); hunks: -14,72 +14,6; -167,6 +101,68 @@ def __call__(self, text=None, audio=None, audio_kwargs=None...; symbols: Qwen3ASRThinkerConfig, __init__, Qwen3ASRConfig, get_text_config, touching `Qwen3ASRThinkerConfig, __init__, Qwen3ASRConfig`; `test/manual/models/test_qwen3_asr.py` added +118/-0 (118 lines); hunks: -0,0 +1,118; symbols: download_audio, TestQwen3ASRTranscription, setUpClass, tearDownClass, touching `download_audio, TestQwen3ASRTranscription, setUpClass`; `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` added +49/-0 (49 lines); hunks: -0,0 +1,49; symbols: Qwen3ASRAdapter, build_sampling_params, postprocess_text, build_verbose_response, touching `Qwen3ASRAdapter, build_sampling_params, postprocess_text`; `python/sglang/srt/multimodal/processors/qwen3_asr.py` modified +8/-5 (13 lines); hunks: -10,11 +10,13; -23,7 +25,7 @@ class Qwen3ASRMultimodalProcessor(BaseMultimodalProcessor):; symbols: Qwen3ASRMultimodalProcessor, __init__, _build_transcription_prompt, touching `Qwen3ASRMultimodalProcessor, __init__, _build_transcription_prompt`.
- Code diff details:
  - `python/sglang/srt/configs/qwen3_asr.py` modified +63/-67 (130 lines); hunks: -14,72 +14,6; -167,6 +101,68 @@ def __call__(self, text=None, audio=None, audio_kwargs=None...; symbols: Qwen3ASRThinkerConfig, __init__, Qwen3ASRConfig, get_text_config
  - `test/manual/models/test_qwen3_asr.py` added +118/-0 (118 lines); hunks: -0,0 +1,118; symbols: download_audio, TestQwen3ASRTranscription, setUpClass, tearDownClass
  - `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` added +49/-0 (49 lines); hunks: -0,0 +1,49; symbols: Qwen3ASRAdapter, build_sampling_params, postprocess_text, build_verbose_response
  - `python/sglang/srt/multimodal/processors/qwen3_asr.py` modified +8/-5 (13 lines); hunks: -10,11 +10,13; -23,7 +25,7 @@ class Qwen3ASRMultimodalProcessor(BaseMultimodalProcessor):; symbols: Qwen3ASRMultimodalProcessor, __init__, _build_transcription_prompt
- Key code excerpts:

```diff
diff -- python/sglang/srt/configs/qwen3_asr.py
@@ -14,72 +14,6 @@
-class Qwen3ASRThinkerConfig(PretrainedConfig):
-    model_type = "qwen3_asr_thinker"
-    sub_configs = {
-        "audio_config": Qwen3OmniMoeAudioEncoderConfig,
-    }
-    def __init__(
diff -- test/manual/models/test_qwen3_asr.py
@@ -0,0 +1,118 @@
+"""
+Test Qwen3-ASR model support in SGLang.
+Tests /v1/audio/transcriptions endpoint (OpenAI-compatible).
+Usage:
+    python test/manual/models/test_qwen3_asr.py
+"""
diff -- python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py
@@ -0,0 +1,49 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/configs/qwen3_asr.py` modified +63/-67; `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` added +49/-0; `python/sglang/srt/multimodal/processors/qwen3_asr.py` modified +8/-5
  - tests: `test/manual/models/test_qwen3_asr.py` added +118/-0
- Risk and verification: The diff ships test coverage in `test/manual/models/test_qwen3_asr.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #22230 - [Feature] Support eagle3 for qwen3-vl

- Link: https://github.com/sgl-project/sglang/pull/22230
- Status/date: merged / 2026-04-09
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `a69be2e866fb`
- Diff scope read: GitHub Pull Request files API returned 1 files, +24/-0, 51 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Support eagle3 for qwen3-vl"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[Feature] Support eagle3 for qwen3-vl"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +24/-0 (24 lines); hunks: -1130,6 +1130,9 @@ def __init__(; -1246,13 +1249,18 @@ def forward(; symbols: __init__, separate_deepstack_embeds, forward, load_weights, touching `__init__, separate_deepstack_embeds, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +24/-0 (24 lines); hunks: -1130,6 +1130,9 @@ def __init__(; -1246,13 +1249,18 @@ def forward(; symbols: __init__, separate_deepstack_embeds, forward, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -1130,6 +1130,9 @@ def __init__(
+        # For EAGLE3 support
+        self.capture_aux_hidden_states = False
@@ -1246,13 +1249,18 @@ def forward(
+        aux_hidden_states = None
+        if self.capture_aux_hidden_states:
+            hidden_states, aux_hidden_states = hidden_states
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +24/-0
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/models/qwen3_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22089 - [Feature] Add chunk-based streaming ASR for Qwen3-ASR

- Link: https://github.com/sgl-project/sglang/pull/22089
- Status/date: merged / 2026-04-09
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py`; associated commits `8b991d98a12c`
- Diff scope read: GitHub Pull Request files API returned 5 files, +263/-2, 325 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] Add chunk-based streaming ASR for Qwen3-ASR"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py`; technical summary: Covers "[Feature] Add chunk-based streaming ASR for Qwen3-ASR"; the main implementation surface is `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py`, `python/sglang/srt/multimodal/processors/qwen3_asr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` modified +20/-0 (20 lines); hunks: -9,12 +9,32; symbols: Qwen3ASRAdapter, supports_chunked_streaming, chunked_streaming_config, prompt_template, touching `Qwen3ASRAdapter, supports_chunked_streaming, chunked_streaming_config`; `python/sglang/srt/multimodal/processors/qwen3_asr.py` modified +2/-2 (4 lines); hunks: -12,7 +12,7; -47,7 +47,7 @@ def _build_transcription_prompt(self, input_text: Union[str, l...; symbols: _build_transcription_prompt, compute_mrope_positions, touching `_build_transcription_prompt, compute_mrope_positions`.
- Code diff details:
  - `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` modified +20/-0 (20 lines); hunks: -9,12 +9,32; symbols: Qwen3ASRAdapter, supports_chunked_streaming, chunked_streaming_config, prompt_template
  - `python/sglang/srt/multimodal/processors/qwen3_asr.py` modified +2/-2 (4 lines); hunks: -12,7 +12,7; -47,7 +47,7 @@ def _build_transcription_prompt(self, input_text: Union[str, l...; symbols: _build_transcription_prompt, compute_mrope_positions
- Key code excerpts:

```diff
diff -- python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py
@@ -9,12 +9,32 @@
+from sglang.srt.multimodal.processors.qwen3_asr import DEFAULT_ASR_PROMPT
+    @property
+    def supports_chunked_streaming(self) -> bool:
+        return True
+    @property
+    def chunked_streaming_config(self) -> dict:
diff -- python/sglang/srt/multimodal/processors/qwen3_asr.py
@@ -12,7 +12,7 @@
-_DEFAULT_ASR_PROMPT = (
+DEFAULT_ASR_PROMPT = (
@@ -47,7 +47,7 @@ def _build_transcription_prompt(self, input_text: Union[str, list]) -> str:
-            return _DEFAULT_ASR_PROMPT
+            return DEFAULT_ASR_PROMPT
```

- Reviewed files:
  - runtime: `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen3_asr.py` modified +20/-0; `python/sglang/srt/multimodal/processors/qwen3_asr.py` modified +2/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/entrypoints/openai/serving_transcription.py`, `python/sglang/srt/entrypoints/openai/streaming_asr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/base.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #24187 - [Fix] Qwen3-ASR config: set thinker_config before super().__init__

- Link: https://github.com/sgl-project/sglang/pull/24187
- Status/date: merged / 2026-05-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/configs/qwen3_asr.py`; associated commits `0f3932c05540`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Qwen3-ASR config: set thinker_config before super().__init__"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/configs/qwen3_asr.py`; technical summary: Covers "[Fix] Qwen3-ASR config: set thinker_config before super().__init__"; the main implementation surface is `python/sglang/srt/configs/qwen3_asr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/configs/qwen3_asr.py` modified +1/-1 (2 lines); hunks: -148,7 +148,6 @@ class Qwen3ASRConfig(PretrainedConfig):; -159,6 +158,7 @@ def __init__(self, thinker_config=None, **kwargs):; symbols: Qwen3ASRConfig, __init__, get_text_config, touching `Qwen3ASRConfig, __init__, get_text_config`.
- Code diff details:
  - `python/sglang/srt/configs/qwen3_asr.py` modified +1/-1 (2 lines); hunks: -148,7 +148,6 @@ class Qwen3ASRConfig(PretrainedConfig):; -159,6 +158,7 @@ def __init__(self, thinker_config=None, **kwargs):; symbols: Qwen3ASRConfig, __init__, get_text_config
- Key code excerpts:

```diff
diff -- python/sglang/srt/configs/qwen3_asr.py
@@ -148,7 +148,6 @@ class Qwen3ASRConfig(PretrainedConfig):
-        super().__init__(**kwargs)
@@ -159,6 +158,7 @@ def __init__(self, thinker_config=None, **kwargs):
+        super().__init__(**kwargs)
```

- Reviewed files:
  - runtime: `python/sglang/srt/configs/qwen3_asr.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/configs/qwen3_asr.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26116 - [VLM] Reuse Qwen pretokenized ids

- Link: https://github.com/sgl-project/sglang/pull/26116
- Status/date: merged / 2026-05-23
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `19b60a4f9e14`
- Diff scope read: GitHub Pull Request files API returned 2 files, +110/-24, 197 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Reuse Qwen pretokenized ids"; model line: Qwen VLM/Omni/ASR; category: model implementation change; main diff: `python/sglang/srt/multimodal/processors/qwen_vl.py`; technical summary: Covers "[VLM] Reuse Qwen pretokenized ids"; the main implementation surface is `python/sglang/srt/multimodal/processors/qwen_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +86/-24 (110 lines); hunks: -398,6 +398,42 @@ def compute_mrope_positions(self, input_ids, mm_items):; -560,6 +596,27 @@ async def process_mm_data_async(; symbols: compute_mrope_positions, _get_processor_output_value, _get_precomputed_mrope_from_output, get_mm_data, touching `compute_mrope_positions, _get_processor_output_value, _get_precomputed_mrope_from_output`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +86/-24 (110 lines); hunks: -398,6 +398,42 @@ def compute_mrope_positions(self, input_ids, mm_items):; -560,6 +596,27 @@ async def process_mm_data_async(; symbols: compute_mrope_positions, _get_processor_output_value, _get_precomputed_mrope_from_output, get_mm_data
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -398,6 +398,42 @@ def compute_mrope_positions(self, input_ids, mm_items):
+    # TODO: consider moving it to SGLangBaseProcessor
+    @staticmethod
+    def _get_processor_output_value(ret, key):
+        """get value with key from returned value of processor"""
+        if ret is None:
+            return None
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +86/-24
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26167 - [VLM] feat: replace small H2D calls with a single one for qwen-vl

- Link: https://github.com/sgl-project/sglang/pull/26167
- Status/date: merged / 2026-05-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `64475965015f`
- Diff scope read: GitHub Pull Request files API returned 3 files, +48/-44, 187 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] feat: replace small H2D calls with a single one for qwen-vl"; model line: Qwen VLM/Omni/ASR; category: model implementation change; main diff: `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`; technical summary: Covers "[VLM] feat: replace small H2D calls with a single one for qwen-vl"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +2/-2 (4 lines); hunks: -756,7 +756,7 @@ def forward(; -938,7 +938,7 @@ def _prepare_graph_inputs(self, x: torch.Tensor, grid_thw: t...; symbols: forward, _prepare_graph_inputs, touching `forward, _prepare_graph_inputs`; `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +0/-2 (2 lines); hunks: -293,7 +293,6 @@ def build_input_ids_with_timestamps(; -312,7 +311,6 @@ def build_input_ids_with_timestamps(; symbols: build_input_ids_with_timestamps, touching `build_input_ids_with_timestamps`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +2/-2 (4 lines); hunks: -756,7 +756,7 @@ def forward(; -938,7 +938,7 @@ def _prepare_graph_inputs(self, x: torch.Tensor, grid_thw: t...; symbols: forward, _prepare_graph_inputs
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +0/-2 (2 lines); hunks: -293,7 +293,6 @@ def build_input_ids_with_timestamps(; -312,7 +311,6 @@ def build_input_ids_with_timestamps(; symbols: build_input_ids_with_timestamps
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -756,7 +756,7 @@ def forward(
-        x = x.to(device=self.device, dtype=self.dtype)
+        x = x.to(device=self.device, dtype=self.dtype, non_blocking=True)
@@ -938,7 +938,7 @@ def _prepare_graph_inputs(self, x: torch.Tensor, grid_thw: torch.Tensor) -> tupl
-        x = x.to(device=self.device, dtype=self.dtype)
+        x = x.to(device=self.device, dtype=self.dtype, non_blocking=True)
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -293,7 +293,6 @@ def build_input_ids_with_timestamps(
-        audio_token_id = getattr(self, "audio_token_id", None)
@@ -312,7 +311,6 @@ def build_input_ids_with_timestamps(
-        model_type = getattr(self, "model_type", None)
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +2/-2; `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +0/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #26094 - [VLM] fix: fix only the grids from last split mm item is collected for qwen-vl

- Link: https://github.com/sgl-project/sglang/pull/26094
- Status/date: merged / 2026-05-25
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `72c1582d4ef4`
- Diff scope read: GitHub Pull Request files API returned 1 files, +47/-19, 102 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] fix: fix only the grids from last split mm item is collected for qwen-vl"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/multimodal/processors/qwen_vl.py`; technical summary: Covers "[VLM] fix: fix only the grids from last split mm item is collected for qwen-vl"; the main implementation surface is `python/sglang/srt/multimodal/processors/qwen_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +47/-19 (66 lines); hunks: -374,13 +374,12 @@ def build_input_ids_with_timestamps(; -529,6 +528,32 @@ def _compute_image_only_mrope_positions_from_offsets(; symbols: build_input_ids_with_timestamps, compute_mrope_positions, _compute_image_only_mrope_positions_from_offsets, _concat_mm_item_grid, touching `build_input_ids_with_timestamps, compute_mrope_positions, _compute_image_only_mrope_positions_from_offsets`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +47/-19 (66 lines); hunks: -374,13 +374,12 @@ def build_input_ids_with_timestamps(; -529,6 +528,32 @@ def _compute_image_only_mrope_positions_from_offsets(; symbols: build_input_ids_with_timestamps, compute_mrope_positions, _compute_image_only_mrope_positions_from_offsets, _concat_mm_item_grid
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -374,13 +374,12 @@ def build_input_ids_with_timestamps(
-        image_grid_thw = None
-        video_grid_thw = None
-        for item in mm_items:
-            if "image_grid_thw" in item.model_specific_data:
-                image_grid_thw = item.model_specific_data["image_grid_thw"]
-            if "video_grid_thw" in item.model_specific_data:
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +47/-19
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/qwen_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #12662 - [CPU] Add support for Qwen3-vl and Qwen3-omni

- Link: https://github.com/sgl-project/sglang/pull/12662
- Status/date: merged / 2026-05-27
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `87c3171aaa55`
- Diff scope read: GitHub Pull Request files API returned 8 files, +250/-35, 545 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CPU] Add support for Qwen3-vl and Qwen3-omni"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[CPU] Add support for Qwen3-vl and Qwen3-omni"; the main implementation surface is `python/sglang/srt/models/qwen3_omni_moe.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_omni_moe.py` modified +62/-13 (75 lines); hunks: -31,8 +31,15; -43,7 +50,26; symbols: get_head_dim_and_projection_size, Qwen3OmniMoeAudioEncoderLayer, __init__, _get_feat_extract_output_lengths, touching `get_head_dim_and_projection_size, Qwen3OmniMoeAudioEncoderLayer, __init__`; `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +18/-0 (18 lines); hunks: -34,6 +34,7; -59,6 +60,23; symbols: smart_resize, touching `smart_resize`; `python/sglang/srt/models/qwen3_vl.py` modified +7/-2 (9 lines); hunks: -348,8 +348,13 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_omni_moe.py` modified +62/-13 (75 lines); hunks: -31,8 +31,15; -43,7 +50,26; symbols: get_head_dim_and_projection_size, Qwen3OmniMoeAudioEncoderLayer, __init__, _get_feat_extract_output_lengths
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +18/-0 (18 lines); hunks: -34,6 +34,7; -59,6 +60,23; symbols: smart_resize
  - `python/sglang/srt/models/qwen3_vl.py` modified +7/-2 (9 lines); hunks: -348,8 +348,13 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_omni_moe.py
@@ -31,8 +31,15 @@
+from sglang.srt.distributed import (
+    get_tensor_model_parallel_world_size,
+)
-from sglang.srt.layers.linear import ColumnParallelLinear, RowParallelLinear
+from sglang.srt.layers.linear import (
+    ColumnParallelLinear,
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -34,6 +34,7 @@
+from sglang.srt.utils import cpu_has_amx_support, is_cpu
@@ -59,6 +60,23 @@
+_is_cpu_amx_available = cpu_has_amx_support()
+_is_cpu = is_cpu()
+if _is_cpu and _is_cpu_amx_available:
+    try:
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -348,8 +348,13 @@ def __init__(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_omni_moe.py` modified +62/-13; `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +18/-0; `python/sglang/srt/models/qwen3_vl.py` modified +7/-2
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/conv.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #22848 - [Feature] WebSocket streaming audio input for ASR

- Link: https://github.com/sgl-project/sglang/pull/22848
- Status/date: merged / 2026-05-27
- Trace source: `git log --name-only -- <model-files>` found it through `test/manual/models/test_qwen3_asr.py`; associated commits `a95b4e2e09eb`
- Diff scope read: GitHub Pull Request files API returned 11 files, +1707/-49, 1980 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature] WebSocket streaming audio input for ASR"; model line: Qwen VLM/Omni/ASR; category: docs/tests/CI; main diff: `test/manual/models/test_qwen3_asr.py`; technical summary: Covers "[Feature] WebSocket streaming audio input for ASR"; the main implementation surface is `test/manual/models/test_qwen3_asr.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/manual/models/test_qwen3_asr.py` modified +547/-3 (550 lines); hunks: -1,17 +1,31; -29,8 +43,83; symbols: _normalize_for_wer, _wer, download_audio, _pcm16_from_audio_bytes, touching `_normalize_for_wer, _wer, download_audio`.
- Code diff details:
  - `test/manual/models/test_qwen3_asr.py` modified +547/-3 (550 lines); hunks: -1,17 +1,31; -29,8 +43,83; symbols: _normalize_for_wer, _wer, download_audio, _pcm16_from_audio_bytes
- Key code excerpts:

```diff
diff -- test/manual/models/test_qwen3_asr.py
@@ -1,17 +1,31 @@
-Tests /v1/audio/transcriptions endpoint (OpenAI-compatible).
+Tests /v1/audio/transcriptions (HTTP) and /v1/realtime (OpenAI Realtime
+transcription WebSocket).
+import asyncio
+import base64
+import json
```

- Reviewed files:
  - tests: `test/manual/models/test_qwen3_asr.py` modified +547/-3
- Risk and verification: The diff ships test coverage in `test/manual/models/test_qwen3_asr.py`, `test/registered/unit/entrypoints/openai/test_serving_transcription.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #28940 - [VLM] Qwen3-VL / Moss-VL ViT preprocessing optimizations

- Link: https://github.com/sgl-project/sglang/pull/28940
- Status/date: merged / 2026-06-24
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`; associated commits `0df796473b76`
- Diff scope read: GitHub Pull Request files API returned 6 files, +476/-10, 558 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[VLM] Qwen3-VL / Moss-VL ViT preprocessing optimizations"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[VLM] Qwen3-VL / Moss-VL ViT preprocessing optimizations"; the main implementation surface is `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl.py` modified +141/-2 (143 lines); hunks: -94,6 +94,10; -597,6 +601,131 @@ def fast_pos_embed_interpolate_from_list(self, grid_thw):; symbols: Qwen3_VisionMLP, fast_pos_embed_interpolate_from_list, _use_vectorized_pos_embed, fast_pos_embed_interpolate_vectorized, touching `Qwen3_VisionMLP, fast_pos_embed_interpolate_from_list, _use_vectorized_pos_embed`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl.py` modified +141/-2 (143 lines); hunks: -94,6 +94,10; -597,6 +601,131 @@ def fast_pos_embed_interpolate_from_list(self, grid_thw):; symbols: Qwen3_VisionMLP, fast_pos_embed_interpolate_from_list, _use_vectorized_pos_embed, fast_pos_embed_interpolate_vectorized
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -94,6 +94,10 @@
+# Below this image count the per-image loop beats the vectorized path (which has a
+# fixed setup cost; measured crossover ~6 on H20); both give the same result.
+_VECTORIZED_VL_POS_EMBED_MIN_IMAGES = 6
@@ -597,6 +601,131 @@ def fast_pos_embed_interpolate_from_list(self, grid_thw):
+    def _use_vectorized_pos_embed(self, num_images: int) -> bool:
+        """Use the vectorized path only past a few images.
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +141/-2
- Risk and verification: The diff ships test coverage in `test/registered/models/test_vit_pos_embed_interpolate.py`, `test/registered/unit/multimodal/test_base_processor_image_decode.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #31596 - fix(vlm): materialize Qwen3-VL features on the vision device

- Link: https://github.com/sgl-project/sglang/pull/31596
- Status/date: merged / 2026-07-29
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`, `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`; associated commits `da5528db3079`
- Diff scope read: GitHub Pull Request files API returned 2 files, +87/-7, 116 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "fix(vlm): materialize Qwen3-VL features on the vision device"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`, `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "fix(vlm): materialize Qwen3-VL features on the vision device"; the main implementation surface is `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`, `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` added +75/-0 (75 lines); hunks: -0,0 +1,75; symbols: _RecordingVisual, __init__, __call__, TestQwen3VLFeatureMaterialization, touching `_RecordingVisual, __init__, __call__`; `python/sglang/srt/models/qwen3_vl.py` modified +12/-7 (19 lines); hunks: -68,7 +68,10; -1330,9 +1333,10 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs:...; symbols: pad_input_ids, get_image_feature, get_video_feature, touching `pad_input_ids, get_image_feature, get_video_feature`.
- Code diff details:
  - `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` added +75/-0 (75 lines); hunks: -0,0 +1,75; symbols: _RecordingVisual, __init__, __call__, TestQwen3VLFeatureMaterialization
  - `python/sglang/srt/models/qwen3_vl.py` modified +12/-7 (19 lines); hunks: -68,7 +68,10; -1330,9 +1333,10 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs:...; symbols: pad_input_ids, get_image_feature, get_video_feature
- Key code excerpts:

```diff
diff -- test/registered/unit/models/test_qwen3_vl_feature_materialization.py
@@ -0,0 +1,75 @@
+"""Regression tests for Qwen3-VL multimodal feature materialization."""
+import unittest
+from types import SimpleNamespace
+import torch
+from sglang.srt.models.qwen3_vl import Qwen3VLForConditionalGeneration
+from sglang.test.ci.ci_register import register_cpu_ci
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -68,7 +68,10 @@
-from sglang.srt.multimodal.mm_utils import run_dp_sharded_mrope_vision_model
+from sglang.srt.multimodal.mm_utils import (
+    materialize_multimodal_features,
+    run_dp_sharded_mrope_vision_model,
+)
@@ -1330,9 +1333,10 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: MultimodalInputs):
```

- Reviewed files:
  - tests: `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` added +75/-0
  - runtime: `python/sglang/srt/models/qwen3_vl.py` modified +12/-7
- Risk and verification: The diff ships test coverage in `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #32611 - Fix transcription & audio-understanding for ASR/audio/speech models

- Link: https://github.com/sgl-project/sglang/pull/32611
- Status/date: merged / 2026-08-19
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/multimodal/processors/glmasr.py`; associated commits `3e5ce26c2dab`
- Diff scope read: GitHub Pull Request files API returned 10 files, +610/-16, 730 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix transcription & audio-understanding for ASR/audio/speech models"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py`; technical summary: Covers "Fix transcription & audio-understanding for ASR/audio/speech models"; the main implementation surface is `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py`, `python/sglang/srt/models/glmasr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py` added +91/-0 (91 lines); hunks: -0,0 +1,91; symbols: GlmAsrAdapter, build_sampling_params, postprocess_text, build_verbose_response, touching `GlmAsrAdapter, build_sampling_params, postprocess_text`; `python/sglang/srt/models/glmasr.py` modified +53/-12 (65 lines); hunks: -92,18 +92,59 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: Mul...; symbols: pad_input_ids, get_audio_feature, forward, touching `pad_input_ids, get_audio_feature, forward`; `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: Qwen2AudioAdapter, build_sampling_params, build_verbose_response, touching `Qwen2AudioAdapter, build_sampling_params, build_verbose_response`; `python/sglang/srt/multimodal/processors/glmasr.py` modified +34/-1 (35 lines); hunks: -29,14 +29,47 @@ def __init__(self, hf_config, server_args, _processor, *args...; symbols: __init__, _build_transcription_prompt, process_mm_data_async, touching `__init__, _build_transcription_prompt, process_mm_data_async`.
- Code diff details:
  - `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py` added +91/-0 (91 lines); hunks: -0,0 +1,91; symbols: GlmAsrAdapter, build_sampling_params, postprocess_text, build_verbose_response
  - `python/sglang/srt/models/glmasr.py` modified +53/-12 (65 lines); hunks: -92,18 +92,59 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: Mul...; symbols: pad_input_ids, get_audio_feature, forward
  - `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py` added +61/-0 (61 lines); hunks: -0,0 +1,61; symbols: Qwen2AudioAdapter, build_sampling_params, build_verbose_response
  - `python/sglang/srt/multimodal/processors/glmasr.py` modified +34/-1 (35 lines); hunks: -29,14 +29,47 @@ def __init__(self, hf_config, server_args, _processor, *args...; symbols: __init__, _build_transcription_prompt, process_mm_data_async
- Key code excerpts:

```diff
diff -- python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py
@@ -0,0 +1,91 @@
+from __future__ import annotations
+from sglang.srt.entrypoints.openai.protocol import (
+    TranscriptionRequest,
+    TranscriptionUsage,
+    TranscriptionVerboseResponse,
+)
diff -- python/sglang/srt/models/glmasr.py
@@ -92,18 +92,59 @@ def pad_input_ids(self, input_ids: List[int], mm_inputs: MultimodalInputs):
-        # Extract audio features from input items
-        input_features = torch.cat([item.feature for item in items], dim=0).type(
-            self.audio_tower.dtype
-        )
-        audio_embeds = self.audio_tower(input_features).last_hidden_state
-        audio_embeds = audio_embeds.reshape(
diff -- python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py
@@ -0,0 +1,61 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py` added +91/-0; `python/sglang/srt/models/glmasr.py` modified +53/-12; `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py` added +61/-0; `python/sglang/srt/multimodal/processors/glmasr.py` modified +34/-1
- Risk and verification: The diff ships test coverage in `test/registered/unit/entrypoints/openai/test_transcription_adapters.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #33829 - [Model] Complete dots.note.omni support with native encoders, video preprocessing, and MTP decoding

- Link: https://github.com/sgl-project/sglang/pull/33829
- Status/date: merged / 2026-08-22
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/dots3_common/dots_omni_audio.py`, `python/sglang/srt/models/dots3_common/dots_omni_towers.py`, `python/sglang/srt/models/dots3_common/dots_omni_vision.py`, `python/sglang/srt/multimodal/processors/dots_note_omni.py`, `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/__init__.py` and 10 files; associated commits `af39ad93493c`
- Diff scope read: GitHub Pull Request files API returned 55 files, +9639/-155, 7772 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Complete dots.note.omni support with native encoders, video preprocessing, and MTP decoding"; model line: Qwen VLM/Omni/ASR; category: model support/runtime entry; main diff: `python/sglang/srt/models/dots3_common/dots_omni_audio.py`, `python/sglang/srt/models/dots3_common/dots_omni_vision.py`, `python/sglang/srt/multimodal/processors/dots_note_omni.py`; technical summary: Covers "[Model] Complete dots.note.omni support with native encoders, video preprocessing, and MTP decoding"; the main implementation surface is `python/sglang/srt/models/dots3_common/dots_omni_audio.py`, `python/sglang/srt/models/dots3_common/dots_omni_vision.py`, `python/sglang/srt/multimodal/processors/dots_note_omni.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/dots3_common/dots_omni_audio.py` added +1027/-0 (1027 lines); hunks: -0,0 +1,1027; symbols: DotsWhisperConfig, __init__, RMSNorm, forward, touching `DotsWhisperConfig, __init__, RMSNorm`; `python/sglang/srt/models/dots3_common/dots_omni_vision.py` added +769/-0 (769 lines); hunks: -0,0 +1,769; symbols: VisionRotaryEmbedding, __init__, _compute_freqs, forward, touching `VisionRotaryEmbedding, __init__, _compute_freqs`; `python/sglang/srt/multimodal/processors/dots_note_omni.py` added +565/-0 (565 lines); hunks: -0,0 +1,565; symbols: _build_video_cfg, _video_payload, _cfg_for_pure_visual, _flat_video_to_content, touching `_build_video_cfg, _video_payload, _cfg_for_pure_visual`; `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/preprocess.py` added +338/-0 (338 lines); hunks: -0,0 +1,338; symbols: SkipSample, tokenize_len, system_block_tokens, audio_block_tokens, touching `SkipSample, tokenize_len, system_block_tokens`.
- Code diff details:
  - `python/sglang/srt/models/dots3_common/dots_omni_audio.py` added +1027/-0 (1027 lines); hunks: -0,0 +1,1027; symbols: DotsWhisperConfig, __init__, RMSNorm, forward
  - `python/sglang/srt/models/dots3_common/dots_omni_vision.py` added +769/-0 (769 lines); hunks: -0,0 +1,769; symbols: VisionRotaryEmbedding, __init__, _compute_freqs, forward
  - `python/sglang/srt/multimodal/processors/dots_note_omni.py` added +565/-0 (565 lines); hunks: -0,0 +1,565; symbols: _build_video_cfg, _video_payload, _cfg_for_pure_visual, _flat_video_to_content
  - `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/preprocess.py` added +338/-0 (338 lines); hunks: -0,0 +1,338; symbols: SkipSample, tokenize_len, system_block_tokens, audio_block_tokens
  - `test/registered/unit/multimodal/test_dots_note_omni.py` added +285/-0 (285 lines); hunks: -0,0 +1,285; symbols: _FakeMultimodalTokens, get_combined_regex, get_modality_of_token, _FakeTokenizer
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/dots3_common/dots_omni_audio.py
@@ -0,0 +1,1027 @@
+"""Dots-path speech encoder for inference only (single GPU).
+Ported from cybertron_alm ``dots_audio_encoder/modeling_whisper.py``.
+Upstream ``WhisperEncoder`` is exposed as :class:`DotsSpeechEncoder`.
+"""
+import math
+from functools import lru_cache
diff -- python/sglang/srt/models/dots3_common/dots_omni_vision.py
@@ -0,0 +1,769 @@
+import math
+from typing import Any
+import torch
+import torch.nn.functional as F
+from torch import nn
+from torch.nn import LayerNorm
diff -- python/sglang/srt/multimodal/processors/dots_note_omni.py
@@ -0,0 +1,565 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/dots3_common/dots_omni_audio.py` added +1027/-0; `python/sglang/srt/models/dots3_common/dots_omni_vision.py` added +769/-0; `python/sglang/srt/multimodal/processors/dots_note_omni.py` added +565/-0; `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/preprocess.py` added +338/-0; `python/sglang/srt/models/dots3_common/dots_omni_towers.py` added +240/-0; `python/sglang/srt/multimodal/processors/dots_note_omni_video_core/flatten_runner.py` added +180/-0
  - tests: `test/registered/unit/multimodal/test_dots_note_omni.py` added +285/-0
- Risk and verification: The diff ships test coverage in `test/registered/attention/unittests/swa/test_swa_out_cache_loc.py`, `test/registered/unit/function_call/test_dots_detector.py`, `test/registered/unit/layers/attention/test_dots_hybrid_backend.py`, `test/registered/unit/model_executor/test_mlp_sync_pad_unpad.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #34690 - [BugFix][VLM] keep Qwen3-VL MoE inference deepstack order

- Link: https://github.com/sgl-project/sglang/pull/34690
- Status/date: merged / 2026-08-28
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`; associated commits `1e6d041f78cd`
- Diff scope read: GitHub Pull Request files API returned 3 files, +156/-36, 253 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix][VLM] keep Qwen3-VL MoE inference deepstack order"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen3_vl_moe.py`, `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[BugFix][VLM] keep Qwen3-VL MoE inference deepstack order"; the main implementation surface is `python/sglang/srt/models/qwen3_vl_moe.py`, `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen3_vl_moe.py` modified +42/-18 (60 lines); hunks: -31,6 +31,7; -58,6 +59,11 @@ def __init__(; symbols: __init__, get_input_embeddings, forward, touching `__init__, get_input_embeddings, forward`; `python/sglang/srt/models/qwen3_vl.py` modified +41/-18 (59 lines); hunks: -1152,6 +1152,11 @@ def __init__(; -1196,25 +1201,43 @@ def forward(; symbols: __init__, get_deepstack_embeds, forward, touching `__init__, get_deepstack_embeds, forward`.
- Code diff details:
  - `python/sglang/srt/models/qwen3_vl_moe.py` modified +42/-18 (60 lines); hunks: -31,6 +31,7; -58,6 +59,11 @@ def __init__(; symbols: __init__, get_input_embeddings, forward
  - `python/sglang/srt/models/qwen3_vl.py` modified +41/-18 (59 lines); hunks: -1152,6 +1152,11 @@ def __init__(; -1196,25 +1201,43 @@ def forward(; symbols: __init__, get_deepstack_embeds, forward
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen3_vl_moe.py
@@ -31,6 +31,7 @@
+from sglang.srt.runtime_context import get_exec
@@ -58,6 +59,11 @@ def __init__(
+        # Use HF deepstack order only if rl_on_policy_target is set;
+        # otherwise, retain original order for inference accuracy.
+        self.use_hf_deepstack_order = (
+            get_exec().deterministic.rl_on_policy_target is not None
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -1152,6 +1152,11 @@ def __init__(
+        # Use HF deepstack order only if rl_on_policy_target is set;
+        # otherwise, retain original order for inference accuracy.
+        self.use_hf_deepstack_order = (
+            get_exec().deterministic.rl_on_policy_target is not None
+        )
@@ -1196,25 +1201,43 @@ def forward(
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen3_vl_moe.py` modified +42/-18; `python/sglang/srt/models/qwen3_vl.py` modified +41/-18
- Risk and verification: The diff ships test coverage in `test/registered/vlm/test_vision_openai_server_a.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #37043 - [vlm] fix: preserve per-request vit graph metadata for qwen-vl

- Link: https://github.com/sgl-project/sglang/pull/37043
- Status/date: merged / 2026-08-30
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`; associated commits `e6a64920572a`
- Diff scope read: GitHub Pull Request files API returned 5 files, +230/-45, 423 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[vlm] fix: preserve per-request vit graph metadata for qwen-vl"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`; technical summary: Covers "[vlm] fix: preserve per-request vit graph metadata for qwen-vl"; the main implementation surface is `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/models/qwen2_5_vl.py` modified +11/-0 (11 lines); hunks: -616,6 +616,11 @@ def forward_with_cuda_graph(; -658,13 +663,19 @@ def forward_with_cuda_graph(; symbols: forward_with_cuda_graph, touching `forward_with_cuda_graph`; `python/sglang/srt/models/qwen3_vl.py` modified +2/-0 (2 lines); hunks: -1053,6 +1053,7 @@ def forward_with_cuda_graph(; -1067,6 +1068,7 @@ def forward_with_cuda_graph(; symbols: forward_with_cuda_graph, load_weights, touching `forward_with_cuda_graph, load_weights`.
- Code diff details:
  - `python/sglang/srt/models/qwen2_5_vl.py` modified +11/-0 (11 lines); hunks: -616,6 +616,11 @@ def forward_with_cuda_graph(; -658,13 +663,19 @@ def forward_with_cuda_graph(; symbols: forward_with_cuda_graph
  - `python/sglang/srt/models/qwen3_vl.py` modified +2/-0 (2 lines); hunks: -1053,6 +1053,7 @@ def forward_with_cuda_graph(; -1067,6 +1068,7 @@ def forward_with_cuda_graph(; symbols: forward_with_cuda_graph, load_weights
- Key code excerpts:

```diff
diff -- python/sglang/srt/models/qwen2_5_vl.py
@@ -616,6 +616,11 @@ def forward_with_cuda_graph(
+        cu_window_layout = tuple(
+            value
+            for index, value in enumerate(cu_window_seqlens)
+            if index == 0 or value != cu_window_seqlens[index - 1]
+        )
@@ -658,13 +663,19 @@ def forward_with_cuda_graph(
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -1053,6 +1053,7 @@ def forward_with_cuda_graph(
+        attention_layout_key = (tuple(cu_seqlens.tolist()), None)
@@ -1067,6 +1068,7 @@ def forward_with_cuda_graph(
+            attention_layout_key=attention_layout_key,
```

- Reviewed files:
  - runtime: `python/sglang/srt/models/qwen2_5_vl.py` modified +11/-0; `python/sglang/srt/models/qwen3_vl.py` modified +2/-0
- Risk and verification: The diff ships test coverage in `test/registered/unit/multimodal/test_vit_cuda_graph_metadata_cuda.py`, `test/registered/unit/multimodal/test_vit_cuda_graph_runner.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #36411 - [Perf] Optimize Qwen3-VL unique-image serving on H100

- Link: https://github.com/sgl-project/sglang/pull/36411
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/arg_groups/model_overrides/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`, `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`; associated commits `0a574034680b`
- Diff scope read: GitHub Pull Request files API returned 30 files, +1370/-76, 1996 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Optimize Qwen3-VL unique-image serving on H100"; model line: Qwen VLM/Omni/ASR; category: performance/backend optimization; main diff: `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`; technical summary: Covers "[Perf] Optimize Qwen3-VL unique-image serving on H100"; the main implementation surface is `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +276/-7 (283 lines); hunks: -2,13 +2,17; -33,6 +37,11; symbols: QwenVLImagePreprocessArtifact, has_feature, cache_value, cache_size_items, touching `QwenVLImagePreprocessArtifact, has_feature, cache_value`; `python/sglang/srt/models/qwen3_vl.py` modified +124/-8 (132 lines); hunks: -72,6 +72,12; -1435,13 +1441,23 @@ def _get_visual_feature(; symbols: _get_visual_feature, _materialize_visual_items, _offload_packed_visual_inputs, get_input_embeddings, touching `_get_visual_feature, _materialize_visual_items, _offload_packed_visual_inputs`; `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` modified +101/-8 (109 lines); hunks: -1,16 +1,24; -69,7 +77,7 @@ def test_processor_defers_gpu_transport_for_encoder_dp(self):; symbols: test_processor_defers_gpu_transport_for_encoder_dp, test_processor_does_not_defer_cpu_transport, test_processor_defers_cuda_ipc_for_single_tp_qwen3_vl, test_retract_reprefill_waits_for_preserved_visual_input, touching `test_processor_defers_gpu_transport_for_encoder_dp, test_processor_does_not_defer_cpu_transport, test_processor_defers_cuda_ipc_for_single_tp_qwen3_vl`; `python/sglang/srt/arg_groups/model_overrides/qwen3_vl.py` modified +111/-2 (113 lines); hunks: -1,20 +1,69; -30,3 +79,63 @@ def _qwen3vl_overrides(server_args: Any, hf_config: Any) -> d...; symbols: large_hopper_qwen3_vl_model_type, expand_multimodal_decode_graph_to_running_limit, _qwen3vl_overrides, _qwen3vl_hopper_serving_overrides, touching `large_hopper_qwen3_vl_model_type, expand_multimodal_decode_graph_to_running_limit, _qwen3vl_overrides`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +276/-7 (283 lines); hunks: -2,13 +2,17; -33,6 +37,11; symbols: QwenVLImagePreprocessArtifact, has_feature, cache_value, cache_size_items
  - `python/sglang/srt/models/qwen3_vl.py` modified +124/-8 (132 lines); hunks: -72,6 +72,12; -1435,13 +1441,23 @@ def _get_visual_feature(; symbols: _get_visual_feature, _materialize_visual_items, _offload_packed_visual_inputs, get_input_embeddings
  - `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` modified +101/-8 (109 lines); hunks: -1,16 +1,24; -69,7 +77,7 @@ def test_processor_defers_gpu_transport_for_encoder_dp(self):; symbols: test_processor_defers_gpu_transport_for_encoder_dp, test_processor_does_not_defer_cpu_transport, test_processor_defers_cuda_ipc_for_single_tp_qwen3_vl, test_retract_reprefill_waits_for_preserved_visual_input
  - `python/sglang/srt/arg_groups/model_overrides/qwen3_vl.py` modified +111/-2 (113 lines); hunks: -1,20 +1,69; -30,3 +79,63 @@ def _qwen3vl_overrides(server_args: Any, hf_config: Any) -> d...; symbols: large_hopper_qwen3_vl_model_type, expand_multimodal_decode_graph_to_running_limit, _qwen3vl_overrides, _qwen3vl_hopper_serving_overrides
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -2,13 +2,17 @@
-from typing import List, Optional, Union
+from copy import deepcopy
+from dataclasses import dataclass, replace
+from functools import lru_cache
+from typing import Any, List, Optional, Union
+from transformers import BaseImageProcessor
diff -- python/sglang/srt/models/qwen3_vl.py
@@ -72,6 +72,12 @@
+from sglang.srt.multimodal.transport.cuda_ipc import (
+    BORROW_CUDA_IPC_FEATURE_KEY,
+    CUDA_IPC_FEATURE_COPY_EVENT_KEY,
+    RETAINED_CUDA_IPC_FEATURE_PROXY_KEY,
+    CudaIpcTensorTransportProxy,
+)
diff -- test/registered/unit/models/test_qwen3_vl_feature_materialization.py
@@ -1,16 +1,24 @@
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +276/-7; `python/sglang/srt/models/qwen3_vl.py` modified +124/-8; `python/sglang/srt/arg_groups/model_overrides/qwen3_vl.py` modified +111/-2
  - tests: `test/registered/unit/models/test_qwen3_vl_feature_materialization.py` modified +101/-8
- Risk and verification: The diff ships test coverage in `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #39278 - [Fix][Qwen-VL] Normalize sentinel on artifact fast path

- Link: https://github.com/sgl-project/sglang/pull/39278
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/multimodal/processors/qwen_vl.py`; associated commits `b510881157b8`
- Diff scope read: GitHub Pull Request files API returned 1 files, +61/-19, 119 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix][Qwen-VL] Normalize sentinel on artifact fast path"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/multimodal/processors/qwen_vl.py`; technical summary: Covers "[Fix][Qwen-VL] Normalize sentinel on artifact fast path"; the main implementation surface is `python/sglang/srt/multimodal/processors/qwen_vl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +61/-19 (80 lines); hunks: -393,12 +393,13 @@ def __init__(self, hf_config, server_args, _processor, *ar...; -864,8 +865,12 @@ def compose_image_artifacts(; symbols: __init__, compose_image_artifacts, _normalize_prompt_for_fast_path, touching `__init__, compose_image_artifacts, _normalize_prompt_for_fast_path`.
- Code diff details:
  - `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +61/-19 (80 lines); hunks: -393,12 +393,13 @@ def __init__(self, hf_config, server_args, _processor, *ar...; -864,8 +865,12 @@ def compose_image_artifacts(; symbols: __init__, compose_image_artifacts, _normalize_prompt_for_fast_path
- Key code excerpts:

```diff
diff -- python/sglang/srt/multimodal/processors/qwen_vl.py
@@ -393,12 +393,13 @@ def __init__(self, hf_config, server_args, _processor, *args, **kwargs):
+        # Also match the legacy sglang <image> sentinel used by /generate,
+        # so the artifact fast path can normalize it before build_input_ids.
-            # The regex that matches expanded image tokens.
-                r"<\|vision_start\|>(?:<\|image_pad\|>)+<\|vision_end\|>"
+                r"<\|vision_start\|>(?:<\|image_pad\|>)+<\|vision_end\|>|<image>"
@@ -864,8 +865,12 @@ def compose_image_artifacts(
```

- Reviewed files:
  - runtime: `python/sglang/srt/multimodal/processors/qwen_vl.py` modified +61/-19
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/multimodal/processors/qwen_vl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #43309 - [Fix] Adapt NPU Qwen-VL processor patch to transformers 5.19 resize() signature change

- Link: https://github.com/sgl-project/sglang/pull/43309
- Status/date: merged / 2026-10-12
- Trace source: `git log --name-only -- <model-files>` found it through `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`; associated commits `c6e822c29b9b`
- Diff scope read: GitHub Pull Request files API returned 1 files, +7/-31, 65 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Fix] Adapt NPU Qwen-VL processor patch to transformers 5.19 resize() signature change"; model line: Qwen VLM/Omni/ASR; category: bug fix; main diff: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`; technical summary: Covers "[Fix] Adapt NPU Qwen-VL processor patch to transformers 5.19 resize() signature change"; the main implementation surface is `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` modified +7/-31 (38 lines); hunks: -8,10 +8,6; -86,19 +82,12 @@ def _preprocess(; symbols: _preprocess, touching `_preprocess`.
- Code diff details:
  - `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` modified +7/-31 (38 lines); hunks: -8,10 +8,6; -86,19 +82,12 @@ def _preprocess(; symbols: _preprocess
- Key code excerpts:

```diff
diff -- python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py
@@ -8,10 +8,6 @@
-from transformers.models.qwen2_vl.image_processing_qwen2_vl import smart_resize
-from transformers.models.qwen3_vl.video_processing_qwen3_vl import (
-    smart_resize as smart_resize_video,
-)
@@ -86,19 +82,12 @@ def _preprocess(
-            height, width = stacked_images.shape[-2:]
```

- Reviewed files:
  - runtime: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` modified +7/-31
- Risk and verification: Runtime changes concentrate in `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
