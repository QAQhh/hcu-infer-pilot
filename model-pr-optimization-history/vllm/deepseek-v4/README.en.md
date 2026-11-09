# vllm DeepSeek V4 Model PR Optimization History

## Implementation File Coverage

| File | Git-traced PRs |
| --- | --- |
| `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-AITER-TEP4.yaml` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-FP8-TP4-ROCm.yaml` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-confidence-TEP4.yaml` | no direct PR-number commit |
| `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml` | [#59611](https://github.com/vllm-project/vllm/pull/59611) |
| `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-NVFP4.yaml` | [#47972](https://github.com/vllm-project/vllm/pull/47972) |
| `tests/evals/gsm8k/configs/DeepSeek-V4-Pro-NVFP4.yaml` | [#47972](https://github.com/vllm-project/vllm/pull/47972) |
| `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` | [#59655](https://github.com/vllm-project/vllm/pull/59655), [#61763](https://github.com/vllm-project/vllm/pull/61763) |
| `tests/evals/gsm8k/configs/moe-refactor/DeepSeek-V4-Flash-deepgemm-mega-moe.yaml` | [#42111](https://github.com/vllm-project/vllm/pull/42111) |
| `tests/kernels/test_deepseek_v4_cpu_kernels.py` | [#55355](https://github.com/vllm-project/vllm/pull/55355) |
| `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` | [#40860](https://github.com/vllm-project/vllm/pull/40860), [#42353](https://github.com/vllm-project/vllm/pull/42353), [#43073](https://github.com/vllm-project/vllm/pull/43073), [#43162](https://github.com/vllm-project/vllm/pull/43162), [#43827](https://github.com/vllm-project/vllm/pull/43827), [#45681](https://github.com/vllm-project/vllm/pull/45681), [#49236](https://github.com/vllm-project/vllm/pull/49236), [#52836](https://github.com/vllm-project/vllm/pull/52836), [#56215](https://github.com/vllm-project/vllm/pull/56215), [#56893](https://github.com/vllm-project/vllm/pull/56893), [#56935](https://github.com/vllm-project/vllm/pull/56935), [#61371](https://github.com/vllm-project/vllm/pull/61371), ... (13 total) |
| `tests/models/deepseek_v41/__init__.py` | [#61868](https://github.com/vllm-project/vllm/pull/61868) |
| `tests/models/deepseek_v41/nvidia/__init__.py` | [#61868](https://github.com/vllm-project/vllm/pull/61868) |
| `tests/models/deepseek_v41/nvidia/specialized_decode/__init__.py` | [#61868](https://github.com/vllm-project/vllm/pull/61868) |
| `tests/models/deepseek_v41/nvidia/specialized_decode/test_all_gather.py` | [#63921](https://github.com/vllm-project/vllm/pull/63921) |
| `tests/models/deepseek_v41/nvidia/specialized_decode/test_decode_topk.py` | [#63921](https://github.com/vllm-project/vllm/pull/63921) |
| `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` | [#61868](https://github.com/vllm-project/vllm/pull/61868), [#63914](https://github.com/vllm-project/vllm/pull/63914), [#63921](https://github.com/vllm-project/vllm/pull/63921), [#65552](https://github.com/vllm-project/vllm/pull/65552) |
| `tests/models/deepseek_v41/nvidia/specialized_decode/test_layers.py` | [#61868](https://github.com/vllm-project/vllm/pull/61868), [#63921](https://github.com/vllm-project/vllm/pull/63921) |
| `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` | [#61868](https://github.com/vllm-project/vllm/pull/61868), [#63914](https://github.com/vllm-project/vllm/pull/63914), [#63921](https://github.com/vllm-project/vllm/pull/63921) |
| `tests/models/deepseek_v41/nvidia/specialized_decode/test_sparse_mla_cute.py` | [#63921](https://github.com/vllm-project/vllm/pull/63921) |
| `tests/models/deepseek_v41/nvidia/test_fused_markov.py` | [#64442](https://github.com/vllm-project/vllm/pull/64442) |
| `tests/models/deepseek_v41/nvidia/test_swapab_decode.py` | [#62633](https://github.com/vllm-project/vllm/pull/62633) |
| `tests/models/multimodal/processing/test_deepseek_v4_vl.py` | [#59271](https://github.com/vllm-project/vllm/pull/59271), [#59373](https://github.com/vllm-project/vllm/pull/59373), [#61392](https://github.com/vllm-project/vllm/pull/61392), [#62802](https://github.com/vllm-project/vllm/pull/62802) |
| `tests/models/test_deepseek_v41_amd_replay_forward.py` | [#59039](https://github.com/vllm-project/vllm/pull/59039), [#62384](https://github.com/vllm-project/vllm/pull/62384) |
| `tests/models/test_deepseek_v41_decoder_replay_layers.py` | [#58132](https://github.com/vllm-project/vllm/pull/58132), [#59532](https://github.com/vllm-project/vllm/pull/59532), [#59894](https://github.com/vllm-project/vllm/pull/59894), [#60378](https://github.com/vllm-project/vllm/pull/60378), [#60392](https://github.com/vllm-project/vllm/pull/60392), [#61041](https://github.com/vllm-project/vllm/pull/61041), [#63155](https://github.com/vllm-project/vllm/pull/63155) |
| `tests/models/test_deepseek_v41_pcp.py` | [#59857](https://github.com/vllm-project/vllm/pull/59857), [#61994](https://github.com/vllm-project/vllm/pull/61994), [#62384](https://github.com/vllm-project/vllm/pull/62384), [#63098](https://github.com/vllm-project/vllm/pull/63098) |
| `tests/models/test_deepseek_v41_pipeline.py` | [#62208](https://github.com/vllm-project/vllm/pull/62208) |
| `tests/models/test_deepseek_v41_replay_batch.py` | [#58132](https://github.com/vllm-project/vllm/pull/58132), [#59039](https://github.com/vllm-project/vllm/pull/59039), [#59532](https://github.com/vllm-project/vllm/pull/59532), [#59894](https://github.com/vllm-project/vllm/pull/59894), [#61643](https://github.com/vllm-project/vllm/pull/61643), [#62009](https://github.com/vllm-project/vllm/pull/62009), [#62183](https://github.com/vllm-project/vllm/pull/62183), [#62384](https://github.com/vllm-project/vllm/pull/62384), [#62652](https://github.com/vllm-project/vllm/pull/62652) |
| `tests/models/test_deepseek_v41_replay_start.py` | [#56227](https://github.com/vllm-project/vllm/pull/56227), [#62183](https://github.com/vllm-project/vllm/pull/62183) |
| `tests/models/test_deepseek_v4_aiter_mega_moe.py` | [#59685](https://github.com/vllm-project/vllm/pull/59685), [#61004](https://github.com/vllm-project/vllm/pull/61004), [#61262](https://github.com/vllm-project/vllm/pull/61262), [#61345](https://github.com/vllm-project/vllm/pull/61345), [#61819](https://github.com/vllm-project/vllm/pull/61819) |
| `tests/models/test_deepseek_v4_dspark_rocm.py` | [#52362](https://github.com/vllm-project/vllm/pull/52362), [#60462](https://github.com/vllm-project/vllm/pull/60462) |
| `tests/models/test_deepseek_v4_fi_moe_ep.py` | [#49636](https://github.com/vllm-project/vllm/pull/49636) |
| `tests/models/test_deepseek_v4_mega_moe.py` | [#40860](https://github.com/vllm-project/vllm/pull/40860), [#43004](https://github.com/vllm-project/vllm/pull/43004), [#43077](https://github.com/vllm-project/vllm/pull/43077), [#43632](https://github.com/vllm-project/vllm/pull/43632), [#51368](https://github.com/vllm-project/vllm/pull/51368), [#53040](https://github.com/vllm-project/vllm/pull/53040), [#56214](https://github.com/vllm-project/vllm/pull/56214), [#56228](https://github.com/vllm-project/vllm/pull/56228), [#56266](https://github.com/vllm-project/vllm/pull/56266), [#56568](https://github.com/vllm-project/vllm/pull/56568), [#56599](https://github.com/vllm-project/vllm/pull/56599), [#56741](https://github.com/vllm-project/vllm/pull/56741), ... (17 total) |
| `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py` | [#53838](https://github.com/vllm-project/vllm/pull/53838) |
| `tests/models/test_deepseek_v4_rocm_wo_a.py` | [#54894](https://github.com/vllm-project/vllm/pull/54894) |
| `tests/models/test_deepseek_v4_vl.py` | no direct PR-number commit |
| `tests/models/test_deepseek_v4_vl_rocm.py` | [#51692](https://github.com/vllm-project/vllm/pull/51692), [#55107](https://github.com/vllm-project/vllm/pull/55107), [#56433](https://github.com/vllm-project/vllm/pull/56433), [#57132](https://github.com/vllm-project/vllm/pull/57132), [#57919](https://github.com/vllm-project/vllm/pull/57919), [#58740](https://github.com/vllm-project/vllm/pull/58740), [#59685](https://github.com/vllm-project/vllm/pull/59685) |
| `tests/parser/engine/test_deepseek_v4.py` | [#45877](https://github.com/vllm-project/vllm/pull/45877), [#51296](https://github.com/vllm-project/vllm/pull/51296), [#56271](https://github.com/vllm-project/vllm/pull/56271), [#58780](https://github.com/vllm-project/vllm/pull/58780) |
| `tests/parser/engine/test_deepseek_v41.py` | [#56208](https://github.com/vllm-project/vllm/pull/56208), [#56271](https://github.com/vllm-project/vllm/pull/56271), [#58780](https://github.com/vllm-project/vllm/pull/58780), [#62729](https://github.com/vllm-project/vllm/pull/62729) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_input_1.json` | [#40860](https://github.com/vllm-project/vllm/pull/40860) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_input_2.json` | [#40860](https://github.com/vllm-project/vllm/pull/40860) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_input_3.json` | [#40860](https://github.com/vllm-project/vllm/pull/40860) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_input_4.json` | [#40860](https://github.com/vllm-project/vllm/pull/40860) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json` | [#56882](https://github.com/vllm-project/vllm/pull/56882) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt` | [#40860](https://github.com/vllm-project/vllm/pull/40860), [#51856](https://github.com/vllm-project/vllm/pull/51856) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_output_2.txt` | [#40860](https://github.com/vllm-project/vllm/pull/40860) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_output_3.txt` | [#40860](https://github.com/vllm-project/vllm/pull/40860) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_output_4.txt` | [#40860](https://github.com/vllm-project/vllm/pull/40860) |
| `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt` | [#56882](https://github.com/vllm-project/vllm/pull/56882) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_input_2.json` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_input_4.json` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_input_5.json` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt` | [#56208](https://github.com/vllm-project/vllm/pull/56208), [#58316](https://github.com/vllm-project/vllm/pull/58316), [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt` | [#56208](https://github.com/vllm-project/vllm/pull/56208), [#58316](https://github.com/vllm-project/vllm/pull/58316), [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_output_3.txt` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_output_4.txt` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/fixtures/deepseek_v41/test_output_5.txt` | [#62199](https://github.com/vllm-project/vllm/pull/62199) |
| `tests/tokenizers_/test_deepseek_v4.py` | [#40860](https://github.com/vllm-project/vllm/pull/40860), [#40982](https://github.com/vllm-project/vllm/pull/40982), [#50580](https://github.com/vllm-project/vllm/pull/50580), [#51262](https://github.com/vllm-project/vllm/pull/51262), [#51856](https://github.com/vllm-project/vllm/pull/51856), [#53747](https://github.com/vllm-project/vllm/pull/53747), [#54566](https://github.com/vllm-project/vllm/pull/54566), [#56882](https://github.com/vllm-project/vllm/pull/56882) |
| `tests/tokenizers_/test_deepseek_v41.py` | [#56208](https://github.com/vllm-project/vllm/pull/56208), [#56299](https://github.com/vllm-project/vllm/pull/56299), [#58316](https://github.com/vllm-project/vllm/pull/58316), [#60792](https://github.com/vllm-project/vllm/pull/60792), [#62199](https://github.com/vllm-project/vllm/pull/62199), [#62647](https://github.com/vllm-project/vllm/pull/62647), [#62729](https://github.com/vllm-project/vllm/pull/62729), [#62802](https://github.com/vllm-project/vllm/pull/62802), [#64971](https://github.com/vllm-project/vllm/pull/64971) |
| `tests/transformers_utils/test_deepseek_v4_utils.py` | [#61392](https://github.com/vllm-project/vllm/pull/61392) |
| `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` | [#52362](https://github.com/vllm-project/vllm/pull/52362), [#58151](https://github.com/vllm-project/vllm/pull/58151), [#58689](https://github.com/vllm-project/vllm/pull/58689) |
| `tests/v1/attention/test_deepseek_v4_swa_visible.py` | [#54566](https://github.com/vllm-project/vllm/pull/54566), [#56227](https://github.com/vllm-project/vllm/pull/56227), [#56638](https://github.com/vllm-project/vllm/pull/56638), [#57152](https://github.com/vllm-project/vllm/pull/57152), [#57245](https://github.com/vllm-project/vllm/pull/57245), [#61392](https://github.com/vllm-project/vllm/pull/61392), [#64094](https://github.com/vllm-project/vllm/pull/64094) |
| `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` | [#40860](https://github.com/vllm-project/vllm/pull/40860), [#50175](https://github.com/vllm-project/vllm/pull/50175), [#56214](https://github.com/vllm-project/vllm/pull/56214), [#56227](https://github.com/vllm-project/vllm/pull/56227), [#56562](https://github.com/vllm-project/vllm/pull/56562), [#56741](https://github.com/vllm-project/vllm/pull/56741), [#63047](https://github.com/vllm-project/vllm/pull/63047) |
| `vllm/models/deepseek_v4/__init__.py` | [#42953](https://github.com/vllm-project/vllm/pull/42953), [#43004](https://github.com/vllm-project/vllm/pull/43004), [#43077](https://github.com/vllm-project/vllm/pull/43077), [#47419](https://github.com/vllm-project/vllm/pull/47419), [#47677](https://github.com/vllm-project/vllm/pull/47677), [#54566](https://github.com/vllm-project/vllm/pull/54566), [#55107](https://github.com/vllm-project/vllm/pull/55107), [#55355](https://github.com/vllm-project/vllm/pull/55355) |
| `vllm/models/deepseek_v4/amd/__init__.py` | [#43004](https://github.com/vllm-project/vllm/pull/43004) |
| `vllm/models/deepseek_v4/amd/dspark.py` | [#47419](https://github.com/vllm-project/vllm/pull/47419), [#51145](https://github.com/vllm-project/vllm/pull/51145), [#52362](https://github.com/vllm-project/vllm/pull/52362), [#52737](https://github.com/vllm-project/vllm/pull/52737), [#59685](https://github.com/vllm-project/vllm/pull/59685) |
| `vllm/models/deepseek_v4/amd/mega_moe.py` | [#59685](https://github.com/vllm-project/vllm/pull/59685), [#61004](https://github.com/vllm-project/vllm/pull/61004), [#61262](https://github.com/vllm-project/vllm/pull/61262), [#61345](https://github.com/vllm-project/vllm/pull/61345) |
| `vllm/models/deepseek_v4/amd/model.py` | [#43077](https://github.com/vllm-project/vllm/pull/43077), [#43162](https://github.com/vllm-project/vllm/pull/43162), [#43385](https://github.com/vllm-project/vllm/pull/43385), [#43629](https://github.com/vllm-project/vllm/pull/43629), [#43679](https://github.com/vllm-project/vllm/pull/43679), [#43746](https://github.com/vllm-project/vllm/pull/43746), [#43950](https://github.com/vllm-project/vllm/pull/43950), [#44246](https://github.com/vllm-project/vllm/pull/44246), [#44262](https://github.com/vllm-project/vllm/pull/44262), [#44569](https://github.com/vllm-project/vllm/pull/44569), [#45931](https://github.com/vllm-project/vllm/pull/45931), [#46720](https://github.com/vllm-project/vllm/pull/46720), ... (35 total) |
| `vllm/models/deepseek_v4/amd/mono/README.md` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/__init__.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/attention/__init__.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/attention/back.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/attention/device.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482), [#63689](https://github.com/vllm-project/vllm/pull/63689) |
| `vllm/models/deepseek_v4/amd/mono/attention/front.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/attention/gemv.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/attention/plan.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/common/__init__.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/common/mx.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| `vllm/models/deepseek_v4/amd/mono/common/ops.py` | [#61482](https://github.com/vllm-project/vllm/pull/61482) |
| ... | 194 more files omitted from table; all were used for git tracing. |

## PR Coverage Summary

- Git-traced PRs: 200
- Extra PRs preserved from existing docs: 0
- Total PRs in this document: 200
- Truncated: 294 PRs in total, newest 200 kept (`MODEL_PR_HISTORY_MAX_DOC_PRS`)
- Auto-classification note: PRs that cannot be safely pinned to one model family go into the framework `shared/` bucket; cross-model PRs stay under the primary model bucket and are labeled as cross-model evidence in the body.
- File trace command: `git log --name-only -- <model-files>`
- Diff audit source: GitHub Pull Request files API

## Timeline

| Date | PR | State | Title | Main files |
| --- | --- | --- | --- | --- |
| 2026-11-05 | [#64880](https://github.com/vllm-project/vllm/pull/64880) | merged | [Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters | `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` |
| 2026-11-05 | [#63891](https://github.com/vllm-project/vllm/pull/63891) | merged | [ROCm][Perf][DSv4.1] Run DSpark's fused Markov sampling on gfx950 with --monokernel | `vllm/models/deepseek_v41/amd/ops/fused_markov.py`, `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py` |
| 2026-11-05 | [#63027](https://github.com/vllm-project/vllm/pull/63027) | merged | [ROCm][Perf][DSv4.1] Mono: tuned K1/K2 for the TP2 compress-ratio-2 layers on MI355X | `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/stages/seam.py`, `vllm/models/deepseek_v41/amd/mono/layer.py` |
| 2026-11-05 | [#60762](https://github.com/vllm-project/vllm/pull/60762) | merged | [Bugfix][DSv4.1] Declare 64-token kernel blocks for SM120 sparse backends | `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` |
| 2026-11-05 | [#65552](https://github.com/vllm-project/vllm/pull/65552) | merged | [CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype | `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` |
| 2026-11-04 | [#63367](https://github.com/vllm-project/vllm/pull/63367) | merged | [ROCm][DSv4.1] Shard the Engram gate so TP ranks gather only the value slice | `vllm/models/deepseek_v41/amd/engram.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/amd/model.py` |
| 2026-11-04 | [#59802](https://github.com/vllm-project/vllm/pull/59802) | merged | [ROCm][DSv4.1][Perf] Overlap the mHC gate projection with attention and FFN | `vllm/models/deepseek_v41/amd/mhc.py`, `vllm/models/deepseek_v41/amd/model.py` |
| 2026-11-04 | [#63921](https://github.com/vllm-project/vllm/pull/63921) | merged | [Perf][DSv4.1] Extend the latency_specialized decode on NVIDIA | `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/decode_topk_cute.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla_cute.py`, `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` |
| 2026-11-04 | [#62729](https://github.com/vllm-project/vllm/pull/62729) | merged | [Bugfix] Honor add_generation_prompt and continue_final_message in the DeepSeek V4.1 tokenizer | `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `vllm/tokenizers/deepseek_v41.py` |
| 2026-11-04 | [#62647](https://github.com/vllm-project/vllm/pull/62647) | merged | [Bugfix][Frontend] Materialize DeepSeek V4.1 content iterators before deepcopy | `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py` |
| 2026-11-03 | [#62633](https://github.com/vllm-project/vllm/pull/62633) | merged | [Perf][Kernel][DSv4.1] Swap-AB CuTe DSL decode attention for small TP2/TP4 steps | `vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py`, `tests/models/deepseek_v41/nvidia/test_swapab_decode.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` |
| 2026-11-03 | [#65030](https://github.com/vllm-project/vllm/pull/65030) | merged | [Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes | `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py` |
| 2026-11-03 | [#57245](https://github.com/vllm-project/vllm/pull/57245) | merged | [LoRA] Add DeepSeek V4.1 language-model adapter support | `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`, `vllm/models/deepseek_v41/attention.py` |
| 2026-11-03 | [#65296](https://github.com/vllm-project/vllm/pull/65296) | merged | [Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-11-03 | [#64974](https://github.com/vllm-project/vllm/pull/64974) | merged | [Refactor][DSv4.1] Remove duplicated code | `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-11-03 | [#62802](https://github.com/vllm-project/vllm/pull/62802) | merged | [EPD] Support DeepSeek-V4.1 image metadata-only inputs | `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v41/common/mm_preprocess.py`, `vllm/models/deepseek_v41/amd/vl_model.py` |
| 2026-11-03 | [#64442](https://github.com/vllm-project/vllm/pull/64442) | merged | [Perf][DSpark][DSv4.1] Fuse the Markov sampling loop on NVIDIA by inverse CDF | `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py`, `tests/models/deepseek_v41/nvidia/test_fused_markov.py`, `vllm/models/deepseek_v41/nvidia/dspark.py` |
| 2026-11-02 | [#62632](https://github.com/vllm-project/vllm/pull/62632) | merged | [Perf][Kernel][DSv4.1] Copy-based Q zero-pad for large eager mega-attention steps | `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` |
| 2026-11-02 | [#64815](https://github.com/vllm-project/vllm/pull/64815) | merged | [Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel | `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` |
| 2026-11-02 | [#63892](https://github.com/vllm-project/vllm/pull/63892) | merged | [ROCm][Perf][DSv4.1] Mono: batch TP4 K2's X8 copies, load its push's peer bases late | `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/layer.py` |
| 2026-11-02 | [#64971](https://github.com/vllm-project/vllm/pull/64971) | merged | [Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages | `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py` |
| 2026-11-02 | [#64816](https://github.com/vllm-project/vllm/pull/64816) | merged | [Perf][DSv4.1] Vectorize first-layer HC expansion copy | `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-11-02 | [#60543](https://github.com/vllm-project/vllm/pull/60543) | merged | [Bugfix][DSv4.1] Autotune the sparse indexer's wq_b GEMM | `vllm/models/deepseek_v41/attention.py` |
| 2026-10-31 | [#63098](https://github.com/vllm-project/vllm/pull/63098) | merged | [Feature][DSv4.1] Enable PCP with PP or DP | `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-10-31 | [#64094](https://github.com/vllm-project/vllm/pull/64094) | merged | [ROCm][DSv4.1][Perf] Enable prefix-cache SWA replay on gfx950 | `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/amd/model.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py` |
| 2026-10-30 | [#61971](https://github.com/vllm-project/vllm/pull/61971) | merged | [Perf][DSv4.1] Bump FlashMLA to pass int64 positions to MegaAttn | `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` |
| 2026-10-30 | [#63885](https://github.com/vllm-project/vllm/pull/63885) | merged | [ROCm][Perf][DSv4.1] Build the SWA decode metadata in one launch | `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`, `vllm/models/deepseek_v41/amd/rocm.py` |
| 2026-10-29 | [#64101](https://github.com/vllm-project/vllm/pull/64101) | merged | [ROCm][Perf][DSv4.1] Mono decode at TP8 on MI355X | `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/stages/gemv.py`, `vllm/models/deepseek_v41/amd/mono/attention/plan.py` |
| 2026-10-29 | [#63816](https://github.com/vllm-project/vllm/pull/63816) | merged | [Bugfix][ROCm][DSv4.1] Guard NaN scores in gfx942 mono routing | `vllm/models/deepseek_v41/amd/mono/stages/moe.py` |
| 2026-10-29 | [#62359](https://github.com/vllm-project/vllm/pull/62359) | merged | [Perf][DSv4.1] Share Engram host tables as host-NUMA cuMem across DP ranks | `vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/config/engram.py` |
| 2026-10-29 | [#62009](https://github.com/vllm-project/vllm/pull/62009) | merged | [Perf][EPLB][DSv4] Add a symm_mem weight-migration backend and fuse MegaMoE replica mapping | `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_replay_batch.py` |
| 2026-10-29 | [#59131](https://github.com/vllm-project/vllm/pull/59131) | merged | [Perf][DSv4.1] Gather the compressed KV once per KV-source group in prefill | `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` |
| 2026-10-29 | [#58780](https://github.com/vllm-project/vllm/pull/58780) | merged | [Bugfix][Parser] Stream DeepSeek V4/V3.2 string tool arguments incrementally | `vllm/parser/deepseek_v4.py`, `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py` |
| 2026-10-29 | [#63047](https://github.com/vllm-project/vllm/pull/63047) | merged | [Bugfix][DSv4.1] Budget prefill memory the startup profile misses | `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` |
| 2026-10-28 | [#63914](https://github.com/vllm-project/vllm/pull/63914) | merged | [Bugfix][DSv4.1] Keep the specialized decode's FlashInfer paths on newer FlashInfer | `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` |
| 2026-10-28 | [#63018](https://github.com/vllm-project/vllm/pull/63018) | merged | [Perf][DSv4.1] Tile the NVFP4 compressed-KV dequant-gather | `vllm/models/deepseek_v41/common/ops/cache_utils.py` |
| 2026-10-27 | [#63155](https://github.com/vllm-project/vllm/pull/63155) | merged | [Perf][DSv4.1] Capture the decoder replay graphs on the model graphs' stream | `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py` |
| 2026-10-27 | [#62011](https://github.com/vllm-project/vllm/pull/62011) | merged | [Perf] Enable DeepGEMM sparse MQA logits on the FP8 indexer cache, DSv4.1 | `vllm/models/deepseek_v41/attention.py`, `vllm/config/attention.py` |
| 2026-10-27 | [#52970](https://github.com/vllm-project/vllm/pull/52970) | merged | [ROCm][aiter] officially supporting aiter Triton kernels+dsv4 on RDNA3 | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/platforms/rocm.py` |
| 2026-10-27 | [#60154](https://github.com/vllm-project/vllm/pull/60154) | merged | [ROCm][DSv4/4.1] Fuse inverse RoPE and MXFP8 quant into the aiter sparse MLA and sparse MLA gating changes | `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v4/amd/rocm.py` |
| 2026-10-27 | [#63063](https://github.com/vllm-project/vllm/pull/63063) | merged | [Perf][DSpark] Stack DeepSeek V41 context WKV projections | `vllm/models/deepseek_v41/nvidia/dspark.py` |
| 2026-10-27 | [#59986](https://github.com/vllm-project/vllm/pull/59986) | merged | [Bugfix][Attention] Keep DSV4.1 sparse prefill out of FULL cudagraphs | `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/sparse_mla.py` |
| 2026-10-27 | [#63689](https://github.com/vllm-project/vllm/pull/63689) | merged | [Bugfix][ROCm][DSv4] Give zero and subnormal mono MXFP8 groups vLLM's scale code | `vllm/models/deepseek_v4/amd/mono/attention/device.py`, `vllm/models/deepseek_v41/amd/mono/attention/device.py`, `vllm/models/deepseek_v4/amd/mono/stages/moe.py` |
| 2026-10-26 | [#61994](https://github.com/vllm-project/vllm/pull/61994) | merged | [Spec Decode] Support PCP with DSpark for DeepSeek-V4.1 | `vllm/models/deepseek_v41/compressor.py`, `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-10-26 | [#63576](https://github.com/vllm-project/vllm/pull/63576) | merged | [Bugfix][ROCm][DSv4.1] Await krdy before K2's combine reads klen in index-source launches | `vllm/models/deepseek_v41/amd/mono/attention/back.py` |
| 2026-10-26 | [#61875](https://github.com/vllm-project/vllm/pull/61875) | merged | [Perf][DeepSeek V4] Declare MXFP8 MoE activations and run them as block FP8 on Hopper | `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v41/quant_config.py` |
| 2026-10-26 | [#62091](https://github.com/vllm-project/vllm/pull/62091) | merged | [Perf][DSv4.1] Read GPU Engram tables from peers' HBM instead of DP collectives | `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/kernels/test_engram.py` |
| 2026-10-24 | [#61482](https://github.com/vllm-project/vllm/pull/61482) | merged | [ROCm][Perf][DSv4] Standalone mono decode layer for DeepSeek-V4-Pro on MI355X | `vllm/models/deepseek_v4/amd/mono/stages/moe.py`, `vllm/models/deepseek_v4/amd/mono/attention/back.py`, `vllm/models/deepseek_v4/amd/mono/layer.py` |
| 2026-10-23 | [#62384](https://github.com/vllm-project/vllm/pull/62384) | merged | [Feature][PCP] Support decoder-side SWA bounded replay with APC for DeepSeek-V4.1-Flash | `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/models/test_deepseek_v41_replay_batch.py` |
| 2026-10-23 | [#60613](https://github.com/vllm-project/vllm/pull/60613) | merged | [Bugfix][DSv4.1] Seed the -1 sentinel in the prefill sparse index workspace | `vllm/models/deepseek_v41/common/ops/cache_utils.py` |
| 2026-10-23 | [#60834](https://github.com/vllm-project/vllm/pull/60834) | merged | [ROCm][Perf] Apply opt-in paged MXFP4 sparse indexer dense path for DeepSeek-V4 | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v41/amd/rocm.py` |
| 2026-10-22 | [#63007](https://github.com/vllm-project/vllm/pull/63007) | merged | [Bugfix][ROCm][DSv4.1] Gather Engram hashes across DP replicas in the AMD model | `vllm/models/deepseek_v41/amd/model.py` |
| 2026-10-22 | [#63009](https://github.com/vllm-project/vllm/pull/63009) | merged | [ROCm][DSv4.1] Allocate offloaded Engram tables at their exact size | `vllm/models/deepseek_v41/common/engram.py`, `tests/kernels/test_engram.py`, `vllm/config/engram.py` |
| 2026-10-22 | [#61615](https://github.com/vllm-project/vllm/pull/61615) | merged | [Perf] Enable small-head FlashMLA sparse prefill for DS V4.1 on SM90 | `vllm/models/deepseek_v41/nvidia/flashmla.py` |
| 2026-10-21 | [#61868](https://github.com/vllm-project/vllm/pull/61868) | merged | [Perf][DSv4.1] DeepSeek-V4.1-Flash specialized decode on GB300 | `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` |
| 2026-10-21 | [#62652](https://github.com/vllm-project/vllm/pull/62652) | merged | [Bugfix][Model] Preserve target-token scoring rows during DeepSeek-V4.1 replay | `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py` |
| 2026-10-20 | [#59611](https://github.com/vllm-project/vllm/pull/59611) | merged | [Bugfix][DeepSeek V4] Load redundant EPLB expert slots | `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-10-20 | [#62421](https://github.com/vllm-project/vllm/pull/62421) | merged | [ROCm][Model] DeepSeek-V4.1 VL: stream language-model weights on ROCm | `vllm/models/deepseek_v41/amd/vl_model.py` |
| 2026-10-20 | [#60731](https://github.com/vllm-project/vllm/pull/60731) | merged | [ROCm][Perf][DSv4.1] Mono decode on MI300X and MI325X (gfx942) | `vllm/models/deepseek_v41/amd/ops/topk512_gfx942.cu`, `tests/kernels/models/amd/test_dsv41_mono_gfx942.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py` |
| 2026-10-19 | [#62208](https://github.com/vllm-project/vllm/pull/62208) | merged | [Bugfix][DeepSeek V4.1] Inject Engram at pipeline stage entry | `tests/models/test_deepseek_v41_pipeline.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-10-19 | [#62199](https://github.com/vllm-project/vllm/pull/62199) | merged | [Bugfix][Frontend] Match DeepSeek-V4.1 encoder to the 1017 reference encoding | `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json`, `tests/tokenizers_/test_deepseek_v41.py` |
| 2026-10-19 | [#61345](https://github.com/vllm-project/vllm/pull/61345) | merged | [ROCm][DSv4] Require explicit MXFP4 opt-in for MegaMoE shared-expert fusion | `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mega_moe.py` |
| 2026-10-19 | [#60118](https://github.com/vllm-project/vllm/pull/60118) | merged | [Perf][DSv4.1] MegaAttn: wo_a writes wo_b's MXFP8 input | `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` |
| 2026-10-19 | [#62183](https://github.com/vllm-project/vllm/pull/62183) | merged | [Feature][PCP] Support APC and encoder-side SWA bounded replay for DeepSeek-V4.1-Flash | `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py` |
| 2026-10-19 | [#60792](https://github.com/vllm-project/vllm/pull/60792) | merged | [Bugfix][Frontend] Align DeepSeek V4.1 images with rendered content | `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `vllm/tokenizers/deepseek_v41.py` |
| 2026-10-19 | [#62269](https://github.com/vllm-project/vllm/pull/62269) | merged | [Bugfix][DSv4.1] Keep the Engram all-to-all buffers in one allocator | `vllm/models/deepseek_v41/common/engram.py` |
| 2026-10-19 | [#62131](https://github.com/vllm-project/vllm/pull/62131) | merged | [ROCm][Perf][DSv4.1] Mono decode for the DSpark draft layers | `vllm/models/deepseek_v41/amd/mono_decode.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/runner.py` |
| 2026-10-18 | [#61819](https://github.com/vllm-project/vllm/pull/61819) | merged | [ROCm][DSv4] Overlap the unfused shared expert with AITER MegaMoE | `vllm/models/deepseek_v4/amd/model.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py` |
| 2026-10-17 | [#58857](https://github.com/vllm-project/vllm/pull/58857) | merged | [Model] DeepSeek-V4/V4.1 VL: stream language-model weights instead of sorting the checkpoint | `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py` |
| 2026-10-17 | [#61960](https://github.com/vllm-project/vllm/pull/61960) | merged | [CI][ROCm][Bugfix] DeepSeek V4.1: don't pass expert intermediate padding to AITER | `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v41/amd/model.py` |
| 2026-10-16 | [#59857](https://github.com/vllm-project/vllm/pull/59857) | merged | [Feature][PCP] Add DeepSeek-V4.1-Flash support | `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v41/compressor.py`, `tests/models/test_deepseek_v41_pcp.py` |
| 2026-10-16 | [#58872](https://github.com/vllm-project/vllm/pull/58872) | merged | [Perf][DSv4.1] Split fused_wqa_wkv by token across TP ranks on SM90 | `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py` |
| 2026-10-15 | [#61371](https://github.com/vllm-project/vllm/pull/61371) | merged | [Kernel][DSv4.1] Bump FlashMLA to the 2026.09.30 release and its interleaved V4.1 KV cache | `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` |
| 2026-10-15 | [#60282](https://github.com/vllm-project/vllm/pull/60282) | merged | [ROCm] Support DeepSeek-V4 hash routing in AITER Triton W4A16 MoE | `vllm/models/deepseek_v4/cpu/model.py` |
| 2026-10-15 | [#61643](https://github.com/vllm-project/vllm/pull/61643) | merged | [Bugfix][MoE] Keep routing rows during DeepSeek V4.1 decoder replay | `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py` |
| 2026-10-15 | [#58689](https://github.com/vllm-project/vllm/pull/58689) | merged | [ROCm][DSv4.1] Disambiguate ROCm attention class names | `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/mono_decode.py` |
| 2026-10-15 | [#61262](https://github.com/vllm-project/vllm/pull/61262) | merged | [ROCm][DSv4] AITER MegaMoE Fixed-Slot Dispatch For DeepSeek-V4 | `vllm/models/deepseek_v4/amd/mega_moe.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py` |
| 2026-10-15 | [#56054](https://github.com/vllm-project/vllm/pull/56054) | merged | [Bugfix][DSv4] Remap Quark MTP layer_quant_config onto draft prefixes | `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v4/amd/mtp.py` |
| 2026-10-15 | [#61392](https://github.com/vllm-project/vllm/pull/61392) | merged | [Chore] Use upstream Transformers DeepseekV4Config | `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py` |
| 2026-10-15 | [#61763](https://github.com/vllm-project/vllm/pull/61763) | merged | [CI] Pin DeepSeek-V4.1-Flash-NVFP4 eval to its FP8-Engram revision | `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` |
| 2026-10-15 | [#58151](https://github.com/vllm-project/vllm/pull/58151) | merged | [ROCm][DSv4.1] Enable DSpark adaptive verification | `vllm/models/deepseek_v41/amd/rocm.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` |
| 2026-10-15 | [#57773](https://github.com/vllm-project/vllm/pull/57773) | merged | [ROCm][Perf] Enable DPA+ETP prefill compute/comm dual-batch-overlap for DeepSeek-V4 | `vllm/models/deepseek_v4/amd/model.py` |
| 2026-10-14 | [#61378](https://github.com/vllm-project/vllm/pull/61378) | merged | [ROCm][Perf] Enqueue the default chain first in CSA/HCA at small batch sizes for DeepSeek-V4 | `vllm/models/deepseek_v4/amd/rocm.py` |
| 2026-10-13 | [#59709](https://github.com/vllm-project/vllm/pull/59709) | merged | [Bugfix][DSv4] Don't bake the C128 compressor skip into CUDA graphs | `vllm/models/deepseek_v4/compressor.py` |
| 2026-10-13 | [#59039](https://github.com/vllm-project/vllm/pull/59039) | merged | [ROCm][Perf][DSv4.1] Enable decoder SWA bounded replay | `tests/models/test_deepseek_v41_amd_replay_forward.py`, `vllm/models/deepseek_v41/amd/model.py`, `tests/models/test_deepseek_v41_replay_batch.py` |
| 2026-10-13 | [#61082](https://github.com/vllm-project/vllm/pull/61082) | merged | [ROCm][Perf][DSv4.1] Mono decode on every backbone layer | `vllm/models/deepseek_v41/amd/mono_decode.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `tests/models/test_dsv41_mono_decode.py` |
| 2026-10-12 | [#61041](https://github.com/vllm-project/vllm/pull/61041) | merged | [Bugfix][DSv4.1] Match decoder-replay input_ids dtype for FlashInfer MegaMoE | `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` |
| 2026-10-12 | [#57549](https://github.com/vllm-project/vllm/pull/57549) | merged | [EPLB] Add EPLB support to dspark draft models (DeepSeekV4) | `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/common/eplb_util.py`, `vllm/models/deepseek_v4/nvidia/model.py` |
| 2026-10-12 | [#61004](https://github.com/vllm-project/vllm/pull/61004) | merged | [ROCm][DSv4] Fuse the shared expert into AITER MegaMoE | `vllm/models/deepseek_v4/amd/mega_moe.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-10-10 | [#60397](https://github.com/vllm-project/vllm/pull/60397) | merged | [ROCm][Perf][DSv4.1] Mono decode layer for DeepSeek-V4.1-Flash on MI355X | `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/attention/back.py` |
| 2026-10-09 | [#59923](https://github.com/vllm-project/vllm/pull/59923) | merged | [Perf][DSv4.1] Exchange packed FP8 Engram rows across DP and feed wkv MXFP8 | `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/ops/engram_peer.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-10-09 | [#59894](https://github.com/vllm-project/vllm/pull/59894) | merged | [Perf][DSv4.1] Trim the last KV-source layer in decoder replay | `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py` |
| 2026-10-08 | [#56638](https://github.com/vllm-project/vllm/pull/56638) | merged | [ROCm][DSv4.1][Perf] Replace the Torch prefill combine with the shared combine_topk_swa_indices kernel | `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py` |
| 2026-10-08 | [#59655](https://github.com/vllm-project/vllm/pull/59655) | merged | [Bugfix] [Spec Decode] DeepSeek V4/V4.1 NVFP4: keep ignored MTP/DSpark experts on MXFP4 | `vllm/models/deepseek_v41/quant_config.py`, `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` |
| 2026-10-07 | [#60462](https://github.com/vllm-project/vllm/pull/60462) | merged | [CI] Fix failing test_deepseek_v4_rocm_dspark* tests | `tests/models/test_deepseek_v4_dspark_rocm.py` |
| 2026-10-07 | [#60392](https://github.com/vllm-project/vllm/pull/60392) | merged | [CI][ROCm] Re-enable the DSv4.1 decoder replay graph test on ROCm | `tests/models/test_deepseek_v41_decoder_replay_layers.py` |
| 2026-10-07 | [#59685](https://github.com/vllm-project/vllm/pull/59685) | merged | [ROCm][DSv4] AITER MegaMoEV2 Integration For DeepSeek V4 | `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-10-07 | [#60378](https://github.com/vllm-project/vllm/pull/60378) | merged | [CI][ROCm] Skip DSv4.1 decoder replay graph test on ROCm | `tests/models/test_deepseek_v41_decoder_replay_layers.py` |
| 2026-10-06 | [#60064](https://github.com/vllm-project/vllm/pull/60064) | merged | [Model][DeepSeek-V4.1] Permute mega-attention wq_b / wo_a while loading | `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/common/ops/fused_layout.py`, `vllm/models/deepseek_v41/nvidia/dspark.py` |
| 2026-10-06 | [#59532](https://github.com/vllm-project/vllm/pull/59532) | merged | [Perf][DSv4.1] Run decoder replay layers in CUDA graphs and trim in PIECEWISE graphs | `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py` |
| 2026-10-06 | [#56720](https://github.com/vllm-project/vllm/pull/56720) | merged | [ROCm][DSv4.1][Perf] One-pass dequantize and a gather-sized grid for the compressed K cache | `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/amd/rocm.py` |
| 2026-10-05 | [#59927](https://github.com/vllm-project/vllm/pull/59927) | merged | [Model][DeepSeek-V4] Make MegaMoE shared-expert finalize independent of linear post-load order | `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py` |
| 2026-10-05 | [#58560](https://github.com/vllm-project/vllm/pull/58560) | merged | [Bugfix][DSv4.1] Keep the compressor ring out of the null block | `vllm/models/deepseek_v41/compressor.py` |
| 2026-10-04 | [#59159](https://github.com/vllm-project/vllm/pull/59159) | merged | [Bugfix][XPU] Make DeepSeek V4 FP8 sparse decode graph-capturable | `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py` |
| 2026-10-01 | [#59327](https://github.com/vllm-project/vllm/pull/59327) | merged | [Perf][DSv4.1] Faster Engram host lookups: sorted rows, inline big lookups | `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-09-30 | [#59373](https://github.com/vllm-project/vllm/pull/59373) | merged | [BugFix][Multimodal] Pick worst-case DeepSeek-V4 VL dummy image size (#59271) | `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/mm_preprocess.py` |
| 2026-09-30 | [#58539](https://github.com/vllm-project/vllm/pull/58539) | merged | [ROCm][DSv4.1][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill | `vllm/models/deepseek_v41/amd/rocm.py` |
| 2026-09-30 | [#58405](https://github.com/vllm-project/vllm/pull/58405) | merged | [ROCm][DSv4][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill | `vllm/models/deepseek_v4/amd/rocm.py` |
| 2026-09-29 | [#57898](https://github.com/vllm-project/vllm/pull/57898) | merged | [Bugfix] Profile maximum DeepSeek V4.1 vision features | `vllm/models/deepseek_v41/common/mm_preprocess.py` |
| 2026-09-29 | [#58132](https://github.com/vllm-project/vllm/pull/58132) | merged | [Model] Decoder-side SWA bounded replay for DeepSeek-V4.1 | `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/models/test_deepseek_v41_replay_batch.py` |
| 2026-09-29 | [#59119](https://github.com/vllm-project/vllm/pull/59119) | merged | [DSv4.1] Avoid runtime recompiles of _ring_slot_mapping_kernel | `vllm/models/deepseek_v41/compressor.py` |
| 2026-09-29 | [#58671](https://github.com/vllm-project/vllm/pull/58671) | merged | [ROCm][DSv4.1] Paged MXFP4 sparse indexer on aiter's MQA-logits kernel | `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/config/attention.py` |
| 2026-09-29 | [#58655](https://github.com/vllm-project/vllm/pull/58655) | merged | [ROCm][DSv4.1][Perf] Run the delayed mHC seams through aiter's fused Triton kernel | `vllm/models/deepseek_v41/amd/model.py` |
| 2026-09-28 | [#58983](https://github.com/vllm-project/vllm/pull/58983) | merged | [ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/platforms/rocm.py` |
| 2026-09-28 | [#57568](https://github.com/vllm-project/vllm/pull/57568) | merged | [Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter | `vllm/models/deepseek_v4/amd/mtp.py` |
| 2026-09-27 | [#57407](https://github.com/vllm-project/vllm/pull/57407) | merged | [ROCm][Perf] Enable layer-aware CSA2 multi-stream overlap for DeepSeek-V4.1-Flash | `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py` |
| 2026-09-27 | [#58634](https://github.com/vllm-project/vllm/pull/58634) | merged | [Perf][DSv4.1] Fuse small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103 | `vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` |
| 2026-09-26 | [#58586](https://github.com/vllm-project/vllm/pull/58586) | merged | [Kernel][DSV4.1] Fuse MoE finalize into the TP all-reduce + mHC boundary | `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-09-26 | [#58499](https://github.com/vllm-project/vllm/pull/58499) | merged | [Bugfix][DSV4.1] Avoid host sync in ViT CUDA graph replay metadata | `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/models/deepseek_v4/common/vision.py` |
| 2026-09-26 | [#58316](https://github.com/vllm-project/vllm/pull/58316) | merged | [Bugfix][Frontend][Rust Frontend] Update DeepSeek V4.1 Flash reasoning effort mappings | `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt` |
| 2026-09-26 | [#57071](https://github.com/vllm-project/vllm/pull/57071) | merged | [Bugfix][ROCm] AMD-Quark mixed-precision DeepSeek-V4.1 support | `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/quant_config.py`, `vllm/models/deepseek_v4/quant_config.py` |
| 2026-09-26 | [#58678](https://github.com/vllm-project/vllm/pull/58678) | merged | [Perf][DSv4.1] Shard the Engram wkv projection across TP ranks | `vllm/models/deepseek_v41/common/engram.py`, `tests/kernels/test_engram.py` |
| 2026-09-25 | [#58740](https://github.com/vllm-project/vllm/pull/58740) | merged | [ROCm][CI] Test AMD DeepSeek V4 MoE routing against a PyTorch reference | `tests/models/test_deepseek_v4_vl_rocm.py` |
| 2026-09-25 | [#58621](https://github.com/vllm-project/vllm/pull/58621) | merged | [Perf][DSv4] Fuse inverse RoPE + FP8 quant into FlashInfer sparse MLA | `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py` |
| 2026-09-25 | [#57679](https://github.com/vllm-project/vllm/pull/57679) | merged | [Perf][DSv4.1] Restore the fused query RMSNorm + MXFP8 quantization path | `vllm/models/deepseek_v41/common/ops/query_quant.py` |
| 2026-09-24 | [#58456](https://github.com/vllm-project/vllm/pull/58456) | merged | [ROCm][DSv4.1][Perf] Emit MXFP8 from the sparse decode reduce and run wo_a as a grouped FP8 GEMM | `vllm/models/deepseek_v41/amd/rocm.py` |
| 2026-09-23 | [#44229](https://github.com/vllm-project/vllm/pull/44229) | merged | [Feature][Frontend] Add DeepSeek-V4 FIM completion rendering | `vllm/renderers/deepseek_v4.py` |
| 2026-09-23 | [#57451](https://github.com/vllm-project/vllm/pull/57451) | merged | [ROCm][DSv4][Perf] Fuse the inverse RoPE into the sparse decode reduce | `vllm/models/deepseek_v4/amd/rocm.py` |
| 2026-09-22 | [#57435](https://github.com/vllm-project/vllm/pull/57435) | merged | [ROCm][DSv4.1][Perf] Fuse the inverse RoPE into the sparse decode reduce | `vllm/models/deepseek_v41/amd/rocm.py` |
| 2026-09-22 | [#57428](https://github.com/vllm-project/vllm/pull/57428) | merged | [Kernel][DSV4.1] Fuse MXFP8 wo_b GEMM with sequence-parallel reduce-scatter | `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-09-22 | [#57919](https://github.com/vllm-project/vllm/pull/57919) | merged | [ROCm][Bugfix] Explicitly reject FSE=1 with DPA+ETP deployment for DeepSeek-V4 | `vllm/models/deepseek_v4/amd/model.py`, `tests/models/test_deepseek_v4_vl_rocm.py` |
| 2026-09-21 | [#52362](https://github.com/vllm-project/vllm/pull/52362) | merged | [ROCm][DSv4] Enable DSpark adaptive verification | `tests/models/test_deepseek_v4_dspark_rocm.py`, `vllm/models/deepseek_v4/amd/dspark.py`, `vllm/models/deepseek_v4/amd/rocm.py` |
| 2026-09-21 | [#57906](https://github.com/vllm-project/vllm/pull/57906) | merged | [Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm | `vllm/models/deepseek_v41/attention.py` |
| 2026-09-21 | [#57874](https://github.com/vllm-project/vllm/pull/57874) | merged | [Bugfix][DSV4.1] Restrict mHC overlap to full CUDA graphs | `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-09-21 | [#57643](https://github.com/vllm-project/vllm/pull/57643) | merged | [Perf][DSV4.1] Fuse TP all-reduce with mHC input preparation | `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py` |
| 2026-09-21 | [#57491](https://github.com/vllm-project/vllm/pull/57491) | merged | [ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm | `vllm/models/deepseek_v41/amd/model.py` |
| 2026-09-21 | [#57603](https://github.com/vllm-project/vllm/pull/57603) | merged | [Perf][DSV4.1] Overlap mHC coefficients for small TP batches | `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` |
| 2026-09-20 | [#56625](https://github.com/vllm-project/vllm/pull/56625) | merged | [DSV4.1] Add encoder cuda graph support for deepseek-v4.1-flash | `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/amd/vl_model.py` |
| 2026-09-20 | [#54894](https://github.com/vllm-project/vllm/pull/54894) | merged | [ROCm][DSV4][Perf] Use FP8 WO_A output projection | `vllm/models/deepseek_v4/amd/rocm.py`, `tests/models/test_deepseek_v4_rocm_wo_a.py` |
| 2026-09-20 | [#57434](https://github.com/vllm-project/vllm/pull/57434) | merged | [ROCm][DSv4.1][Perf] Reuse the decode topk ragged metadata across layers | `vllm/models/deepseek_v41/amd/rocm.py` |
| 2026-09-18 | [#56227](https://github.com/vllm-project/vllm/pull/56227) | merged | [Feat][Model] Support encoder-side SWA-bounded replay for DeepSeek-V4.1-Flash | `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_replay_start.py`, `vllm/models/deepseek_v41/attention.py` |
| 2026-09-18 | [#57604](https://github.com/vllm-project/vllm/pull/57604) | merged | [Perf][DSV4.1] Optimize MegaMoE staging and NVFP4 cache gathers | `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` |
| 2026-09-18 | [#57465](https://github.com/vllm-project/vllm/pull/57465) | merged | [DeepSeek V4] Fix fused MoE expert distribution | `vllm/models/deepseek_v4/nvidia/model.py` |
| 2026-09-18 | [#56882](https://github.com/vllm-project/vllm/pull/56882) | merged | [Bugfix][Multimodal] Preserve DeepSeek V4 image block spacing | `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json`, `tests/tokenizers_/test_deepseek_v4.py`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt` |
| 2026-09-18 | [#56271](https://github.com/vllm-project/vllm/pull/56271) | merged | [Frontend] Fix the parsing of missing `string=` in DeepSeek V4 | `tests/parser/engine/test_deepseek_v4.py`, `vllm/parser/deepseek_v4.py`, `vllm/parser/deepseek_v41.py` |
| 2026-09-18 | [#51856](https://github.com/vllm-project/vllm/pull/51856) | merged | [Bugfix] Attach request-level tools to existing system message in DeepSeek V4 Python renderer | `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4.py`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt` |
| 2026-09-17 | [#57432](https://github.com/vllm-project/vllm/pull/57432) | merged | [Bugfix][DSv4.1] Fix FlashInfer DSpark non-causal attention | `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` |
| 2026-09-17 | [#56266](https://github.com/vllm-project/vllm/pull/56266) | merged | [DSv4.1] Integrate Mega-Gate from DeepGEMM | `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/mtp.py` |
| 2026-09-17 | [#54674](https://github.com/vllm-project/vllm/pull/54674) | merged | [Perf][DSpark] Stack DeepSeek V4 context WKV projections | `vllm/models/deepseek_v4/nvidia/dspark.py` |
| 2026-09-17 | [#56853](https://github.com/vllm-project/vllm/pull/56853) | merged | [ROCm][Perf] Enable HCA dual-stream overlap for DeepSeek-V4 | `vllm/models/deepseek_v4/amd/rocm.py` |
| 2026-09-16 | [#57204](https://github.com/vllm-project/vllm/pull/57204) | merged | [Perf][DSV4.1] Remove MegaMoE padding and shared padding workaround | `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py` |
| 2026-09-16 | [#57132](https://github.com/vllm-project/vllm/pull/57132) | merged | [ROCm][Bugfix] Revert #56433 + #51692 to fix accuracy breakdown for DeepSeek-V4 | `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-09-16 | [#57152](https://github.com/vllm-project/vllm/pull/57152) | merged | [Bugfix][Model] Restore causal image SWA for DeepSeek V4.1 | `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` |
| 2026-09-16 | [#56935](https://github.com/vllm-project/vllm/pull/56935) | merged | [Model][DSv4.1] FlashMLA mega attention and the NVFP4 compressed KV cache | `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py` |
| 2026-09-16 | [#56568](https://github.com/vllm-project/vllm/pull/56568) | merged | [Perf][DSV4.1] Pad shared experts for native MegaMoE fusion | `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py` |
| 2026-09-16 | [#56441](https://github.com/vllm-project/vllm/pull/56441) | merged | [Perf][DSpark] Add KV-only context insertion across V4.1 cache formats | `vllm/models/deepseek_v41/nvidia/dspark.py` |
| 2026-09-15 | [#56254](https://github.com/vllm-project/vllm/pull/56254) | merged | [DSA] Wire DeepGEMM sparse MQA logits into the DeepSeek V4.1 indexer | `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` |
| 2026-09-15 | [#56962](https://github.com/vllm-project/vllm/pull/56962) | merged | [Perf][Kernel] Integrate Mega-mHC from DeepGEMM for DeepSeek V4.1 (reopen of #56255) | `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/__init__.py` |
| 2026-09-15 | [#56903](https://github.com/vllm-project/vllm/pull/56903) | merged | [Perf][DSpark] Collapse DeepSeek-V4.1 draft states before SP all-gather | `vllm/models/deepseek_v41/nvidia/dspark.py` |
| 2026-09-15 | [#56255](https://github.com/vllm-project/vllm/pull/56255) | closed | [DSv4.1] Integrate Mega-mHC from DeepGEMM | `vllm/models/deepseek_v4_1/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v4_1/nvidia/model.py`, `vllm/models/deepseek_v4_1/nvidia/ops/__init__.py` |
| 2026-09-15 | [#56893](https://github.com/vllm-project/vllm/pull/56893) | merged | [Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record) | `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` |
| 2026-09-14 | [#56513](https://github.com/vllm-project/vllm/pull/56513) | merged | [ROCm][DSV4.1][Perf] Fold the mHC post step into the delayed pre projection | `vllm/models/deepseek_v41/amd/model.py` |
| 2026-09-14 | [#56633](https://github.com/vllm-project/vllm/pull/56633) | merged | [Perf][DSv4.1] Fold the mHC post block into the delayed pre projection | `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/dspark.py` |
| 2026-09-14 | [#51794](https://github.com/vllm-project/vllm/pull/51794) | merged | [ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4 | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-09-14 | [#56741](https://github.com/vllm-project/vllm/pull/56741) | merged | [Refactor] Normalize DeepSeek V4.1 model package naming | `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/nvidia/engram.py` |
| 2026-09-14 | [#56299](https://github.com/vllm-project/vllm/pull/56299) | merged | [Bugfix][Frontend] Support Responses text types in DeepSeek V4.1 | `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py` |
| 2026-09-13 | [#55897](https://github.com/vllm-project/vllm/pull/55897) | merged | [LoRA] Add LoRA support for DeepSeek-V4 Flash Vision | `vllm/models/deepseek_v4/common/vl_model.py` |
| 2026-09-13 | [#50178](https://github.com/vllm-project/vllm/pull/50178) | merged | [9/N][warmup][DSv4] Migrate MHC TileLang kernels | `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/glm5next/nvidia/model.py` |
| 2026-09-12 | [#56599](https://github.com/vllm-project/vllm/pull/56599) | merged | [CI] Update DeepSeek V4.1 MegaMoE routing test | `tests/models/test_deepseek_v4_mega_moe.py` |
| 2026-09-12 | [#56562](https://github.com/vllm-project/vllm/pull/56562) | merged | [Perf] Fuse DSV4.1 input metadata preparation with Triton | `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` |
| 2026-09-12 | [#56554](https://github.com/vllm-project/vllm/pull/56554) | merged | [DSV4.1] Remove compressor-aware image sentinel token padding | `vllm/transformers_utils/configs/deepseek_v41.py` |
| 2026-09-12 | [#53566](https://github.com/vllm-project/vllm/pull/53566) | merged | [5/N][warmup][DSv4] Migrate NVIDIA CuTeDSL attention kernels | `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` |
| 2026-09-11 | [#55107](https://github.com/vllm-project/vllm/pull/55107) | merged | [Model][ROCm] Enable DeepSeek V4 Vision | `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/nvidia/vl_model.py`, `vllm/models/deepseek_v4/common/vl_model.py` |
| 2026-09-11 | [#56433](https://github.com/vllm-project/vllm/pull/56433) | merged | [ROCm][Bugfix] Fix AITER preshuffled FP8 block-scale kernel | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-09-11 | [#56214](https://github.com/vllm-project/vllm/pull/56214) | merged | [Model] Support DeepSeek-V4.1-Flash | `tests/models/test_deepseek_v4_mega_moe.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` |
| 2026-09-10 | [#51692](https://github.com/vllm-project/vllm/pull/51692) | merged | [ROCm][Perf] Add bpreshuffled blockscaled fp8 GEMM | `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/_aiter_ops.py` |
| 2026-09-10 | [#56228](https://github.com/vllm-project/vllm/pull/56228) | merged | [Model] DeepSeek-V4.1-Flash Model Definitions | `vllm/models/deepseek_v4_1/nvidia/model.py`, `vllm/models/deepseek_v4_1/amd/model.py`, `vllm/models/deepseek_v4_1/amd/vl_model.py` |
| 2026-09-10 | [#56208](https://github.com/vllm-project/vllm/pull/56208) | merged | [Model][Frontend] Support DeepSeek-V4.1-Flash in Rust and Python frontends | `vllm/tokenizers/deepseek_v41_encoding.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py` |
| 2026-09-10 | [#56215](https://github.com/vllm-project/vllm/pull/56215) | merged | [Kernel] Optional Q-norm in fused DSv4 MLA epilogue; group_size=32 for packed FP8 quant | `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` |
| 2026-09-10 | [#55355](https://github.com/vllm-project/vllm/pull/55355) | merged | [Model] Add DeepSeek-V4 CPU backend | `vllm/models/deepseek_v4/cpu/model.py`, `vllm/models/deepseek_v4/cpu/cpu_sparse.py`, `vllm/models/deepseek_v4/cpu/cpu_mla.py` |
| 2026-09-09 | [#56035](https://github.com/vllm-project/vllm/pull/56035) | merged | [Bugfix][ROCm][DSv4] Skip launch_pdl=True JIT warmup when PDL is unsupported | `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` |
| 2026-09-08 | [#50176](https://github.com/vllm-project/vllm/pull/50176) | merged | [4/N][warmup][DSv4] Migrate common attention kernels | `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm.py` |
| 2026-09-07 | [#53689](https://github.com/vllm-project/vllm/pull/53689) | merged | [XPU][LoRA] Support LoRA for DeepSeek V4 on XPU | `vllm/models/deepseek_v4/xpu/model.py` |
| 2026-09-07 | [#53161](https://github.com/vllm-project/vllm/pull/53161) | merged | [ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts | `vllm/models/deepseek_v4/amd/model.py` |
| 2026-09-05 | [#55299](https://github.com/vllm-project/vllm/pull/55299) | merged | [Bugfix][DSv4] Seed the -1 sentinel in the prefill sparse index workspace | `vllm/models/deepseek_v4/common/ops/cache_utils.py` |
| 2026-09-04 | [#55061](https://github.com/vllm-project/vllm/pull/55061) | merged | [Performance][DSv4] Size dequant gather launch grid by rows | `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` |
| 2026-09-03 | [#45091](https://github.com/vllm-project/vllm/pull/45091) | merged | Fix DeepSeek V4 FlashMLA auto KV cache dtype | `vllm/models/deepseek_v4/attention.py` |
| 2026-09-02 | [#54566](https://github.com/vllm-project/vllm/pull/54566) | merged | [New model][Multimodal] Add DeepSeek-V4-Flash-Vision-Exp support | `vllm/models/deepseek_v4/common/mm_preprocess.py`, `vllm/models/deepseek_v4/nvidia/vl_model.py`, `vllm/models/deepseek_v4/common/vision.py` |
| 2026-09-02 | [#54815](https://github.com/vllm-project/vllm/pull/54815) | merged | [Bugfix] Fix RoPE construction for deepseek-v4 sparse SWA layers | `vllm/models/deepseek_v4/common/rope.py` |
| 2026-09-01 | [#52724](https://github.com/vllm-project/vllm/pull/52724) | merged | [Attention] Enable adaptive verification for FLASHINFER_MLA_SPARSE_DSV4 | `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` |
| 2026-09-01 | [#50175](https://github.com/vllm-project/vllm/pull/50175) | merged | [1/N][warmup][DSv4] Migrate generic MLA metadata and indexing kernels | `vllm/models/deepseek_v4/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` |
| 2026-08-31 | [#53574](https://github.com/vllm-project/vllm/pull/53574) | merged | [Bugfix][SM120] DSv4: pass contiguous C128A decode topk indices on SM120 | `vllm/models/deepseek_v4/sparse_mla.py` |
| 2026-08-27 | [#53540](https://github.com/vllm-project/vllm/pull/53540) | merged | [ROCm][Perf] Fuse SWA q/kv RMSNorm and q FP8 group quant for DeepSeek-V4 | `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py` |
| 2026-08-26 | [#53697](https://github.com/vllm-project/vllm/pull/53697) | merged | [Model] Remove unused DeepSeek V4 top-k buffer helper | `vllm/models/deepseek_v4/attention.py` |
| 2026-08-26 | [#53838](https://github.com/vllm-project/vllm/pull/53838) | merged | [ROCm][DSV4][Perf] Fuse DeepSeek V4 C4 compressor GEMMs | `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py` |
| 2026-08-25 | [#53747](https://github.com/vllm-project/vllm/pull/53747) | merged | [Bugfix][Tokenizer] Replace bare asserts in the DeepSeek V4 encoder | `vllm/tokenizers/deepseek_v4_encoding.py`, `tests/tokenizers_/test_deepseek_v4.py` |
| 2026-08-25 | [#51262](https://github.com/vllm-project/vllm/pull/51262) | merged | [Bugfix][DeepSeek V4] Handle trailing system messages in prompt rendering | `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py` |
| 2026-08-25 | [#49636](https://github.com/vllm-project/vllm/pull/49636) | merged | [Model][MoE] DeepSeek-V4: add opt-in FlashInfer moe_ep expert backend | `tests/models/test_deepseek_v4_fi_moe_ep.py`, `vllm/models/deepseek_v4/nvidia/model.py` |
| 2026-08-24 | [#53361](https://github.com/vllm-project/vllm/pull/53361) | merged | [LoRA] feat: Support LoRA for DeepSeek V4 | `vllm/models/deepseek_v4/nvidia/model.py` |
| 2026-08-21 | [#52823](https://github.com/vllm-project/vllm/pull/52823) | merged | [DSv4 Perf] Adaptive topk width for dsv4, making #50004 back | `vllm/models/deepseek_v4/sparse_mla.py` |

## Per-PR Diff Audit Cards

### PR #64880 - [Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters

- Link: https://github.com/vllm-project/vllm/pull/64880
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/grouped_wo_a.py`, `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v4/nvidia/flashmla.py` and 8 files; associated commits `edc7181bdb59`
- Diff scope read: GitHub Pull Request files API returned 10 files, +215/-44, 470 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`; technical summary: Covers "[Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters"; the main implementation surface is `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/compressor.py` modified +16/-1 (17 lines); hunks: -197,6 +197,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:; -268,7 +276,14 @@ def __init__(; symbols: get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward, DeepseekCompressor, touching `get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward`; `vllm/models/deepseek_v4/attention.py` modified +5/-11 (16 lines); hunks: -48,6 +48,7; -268,9 +269,10 @@ def __init__(; symbols: __init__, _run_parallel_input_projections, compressor_kv_score, indexer_weights_proj, touching `__init__, _run_parallel_input_projections, compressor_kv_score`; `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +5/-8 (13 lines); hunks: -18,7 +18,6; -212,12 +211,10 @@ def get_padded_num_q_heads(cls, num_heads: int) -> int:; symbols: get_padded_num_q_heads, _o_proj, _alloc_attn_out, __init__, touching `get_padded_num_q_heads, _o_proj, _alloc_attn_out`; `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +10/-1 (11 lines); hunks: -1,6 +1,7; -15,6 +16,9; symbols: compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj, rope_quant_unsupported_reason, touching `compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj, rope_quant_unsupported_reason`.
- Code diff details:
  - `vllm/models/deepseek_v4/compressor.py` modified +16/-1 (17 lines); hunks: -197,6 +197,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:; -268,7 +276,14 @@ def __init__(; symbols: get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward, DeepseekCompressor
  - `vllm/models/deepseek_v4/attention.py` modified +5/-11 (16 lines); hunks: -48,6 +48,7; -268,9 +269,10 @@ def __init__(; symbols: __init__, _run_parallel_input_projections, compressor_kv_score, indexer_weights_proj
  - `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +5/-8 (13 lines); hunks: -18,7 +18,6; -212,12 +211,10 @@ def get_padded_num_q_heads(cls, num_heads: int) -> int:; symbols: get_padded_num_q_heads, _o_proj, _alloc_attn_out, __init__
  - `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +10/-1 (11 lines); hunks: -1,6 +1,7; -15,6 +16,9; symbols: compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj, rope_quant_unsupported_reason
  - `vllm/models/deepseek_v4/nvidia/flashmla.py` modified +3/-7 (10 lines); hunks: -12,10 +12,7; -59,12 +56,10 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _o_proj, get_padded_num_q_heads
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/compressor.py
@@ -197,6 +197,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:
+class DeepseekV4CompressorKVScoreLinear(MergedColumnParallelLinear):
+    """Fused ``wkv``/``wgate`` projection with the FP32 output the compressor
+    state accumulates in."""
+    def forward(self, input_: torch.Tensor) -> torch.Tensor:
+        return torch.mm(input_, self.weight.T, out_dtype=torch.float32)
@@ -268,7 +276,14 @@ def __init__(
diff -- vllm/models/deepseek_v4/attention.py
@@ -48,6 +48,7 @@
+from vllm.models.deepseek_v4.common.grouped_wo_a import DeepseekV4GroupedWoA
@@ -268,9 +269,10 @@ def __init__(
-        self.wo_a = ColumnParallelLinear(
+        self.wo_a = DeepseekV4GroupedWoA(
+            n_groups=self.n_groups,
@@ -696,11 +698,7 @@ def _run_parallel_input_projections(
diff -- vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py
@@ -18,7 +18,6 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/compressor.py` modified +16/-1; `vllm/models/deepseek_v4/attention.py` modified +5/-11; `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +5/-8; `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +10/-1; `vllm/models/deepseek_v4/nvidia/flashmla.py` modified +3/-7; `vllm/models/deepseek_v41/compressor.py` modified +1/-9
- Risk and verification: The diff ships test coverage in `tests/lora/test_layers.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63891 - [ROCm][Perf][DSv4.1] Run DSpark's fused Markov sampling on gfx950 with --monokernel

- Link: https://github.com/vllm-project/vllm/pull/63891
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/fused_markov.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`; associated commits `49c1a73a2ee9`
- Diff scope read: GitHub Pull Request files API returned 5 files, +91/-28, 227 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Run DSpark's fused Markov sampling on gfx950 with --monokernel"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/ops/fused_markov.py`, `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Run DSpark's fused Markov sampling on gfx950 with --monokernel"; the main implementation surface is `vllm/models/deepseek_v41/amd/ops/fused_markov.py`, `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/ops/fused_markov.py` modified +11/-6 (17 lines); hunks: -25,16 +25,16; -50,6 +50,8; symbols: _why_not, sample_sequential, touching `_why_not, sample_sequential`; `vllm/models/deepseek_v41/amd/ops/__init__.py` modified +7/-7 (14 lines); hunks: -1,7 +1,7; -10,7 +10,8; symbols: record_monokernel, enabled, swa_decode_meta_enabled, monokernel_cdna3_or_4, touching `record_monokernel, enabled, swa_decode_meta_enabled`; `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py` modified +3/-3 (6 lines); hunks: -23,7 +23,7; -32,7 +32,7; symbols: build, touching `build`; `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py` modified +1/-0 (1 lines); hunks: -39,6 +39,7 @@ def _set_gate(monkeypatch, on: bool):; symbols: _set_gate, _MarkovW2, touching `_set_gate, _MarkovW2`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/ops/fused_markov.py` modified +11/-6 (17 lines); hunks: -25,16 +25,16; -50,6 +50,8; symbols: _why_not, sample_sequential
  - `vllm/models/deepseek_v41/amd/ops/__init__.py` modified +7/-7 (14 lines); hunks: -1,7 +1,7; -10,7 +10,8; symbols: record_monokernel, enabled, swa_decode_meta_enabled, monokernel_cdna3_or_4
  - `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py` modified +3/-3 (6 lines); hunks: -23,7 +23,7; -32,7 +32,7; symbols: build
  - `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py` modified +1/-0 (1 lines); hunks: -39,6 +39,7 @@ def _set_gate(monkeypatch, on: bool):; symbols: _set_gate, _MarkovW2
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/ops/fused_markov.py
@@ -25,16 +25,16 @@
-It runs on gfx942 with --monokernel (``ops.enabled()``). The speculator asks
-the draft model's ``sample_sequential`` (dspark.py) before its loop, and that
-calls ``sample_sequential`` here.
+It runs on gfx942 and gfx950 with --monokernel (``ops.monokernel_cdna3_or_4()``).
+The speculator asks the draft model's ``sample_sequential`` (dspark.py)
+before its loop, and that calls ``sample_sequential`` here.
diff -- vllm/models/deepseek_v41/amd/ops/__init__.py
@@ -1,7 +1,7 @@
-also runs on gfx950 (MI355X).
+and fused_markov also run on gfx950 (MI355X).
@@ -10,7 +10,8 @@
-``swa_decode_meta``, which runs when ``swa_decode_meta_enabled()`` is true.
+``swa_decode_meta`` and ``fused_markov``, which run when
+``monokernel_cdna3_or_4()`` is true.
diff -- vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py
@@ -23,7 +23,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/ops/fused_markov.py` modified +11/-6; `vllm/models/deepseek_v41/amd/ops/__init__.py` modified +7/-7; `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py` modified +3/-3
  - tests: `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py`, `tests/models/test_dsv41_mono_decode.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63027 - [ROCm][Perf][DSv4.1] Mono: tuned K1/K2 for the TP2 compress-ratio-2 layers on MI355X

- Link: https://github.com/vllm-project/vllm/pull/63027
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/mono/README.md`, `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/attention/front.py`, `vllm/models/deepseek_v41/amd/mono/attention/plan.py`, `vllm/models/deepseek_v41/amd/mono/common/mx.py` and 11 files; associated commits `c6ae8d68f294`
- Diff scope read: GitHub Pull Request files API returned 12 files, +1248/-203, 2530 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Mono: tuned K1/K2 for the TP2 compress-ratio-2 layers on MI355X"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/stages/seam.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Mono: tuned K1/K2 for the TP2 compress-ratio-2 layers on MI355X"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/stages/seam.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +542/-79 (621 lines); hunks: -65,8 +65,12; -90,6 +94,7; symbols: scratch_layout, put_mxfp8_group_vllm, router_task_weights, stage_router, touching `scratch_layout, put_mxfp8_group_vllm, router_task_weights`; `vllm/models/deepseek_v41/amd/mono/stages/seam.py` modified +196/-6 (202 lines); hunks: -33,6 +33,8; -50,6 +52,7; symbols: slice_mix, stage_reduce_slice, reduce_slice_quad, slice_rest, touching `slice_mix, stage_reduce_slice, reduce_slice_quad`; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +133/-40 (173 lines); hunks: -34,10 +34,19; -89,6 +98,24 @@ class MonoBuild:; symbols: MonoBuild, tuned, _moe_key, _ffn_symbol_params, touching `MonoBuild, tuned, _moe_key`; `vllm/models/deepseek_v41/amd/mono/attention/front.py` modified +92/-27 (119 lines); hunks: -64,6 +64,7; -82,7 +83,10; symbols: FrontBuild, plus, publish, quant_x_half, touching `FrontBuild, plus, publish`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +542/-79 (621 lines); hunks: -65,8 +65,12; -90,6 +94,7; symbols: scratch_layout, put_mxfp8_group_vllm, router_task_weights, stage_router
  - `vllm/models/deepseek_v41/amd/mono/stages/seam.py` modified +196/-6 (202 lines); hunks: -33,6 +33,8; -50,6 +52,7; symbols: slice_mix, stage_reduce_slice, reduce_slice_quad, slice_rest
  - `vllm/models/deepseek_v41/amd/mono/layer.py` modified +133/-40 (173 lines); hunks: -34,10 +34,19; -89,6 +98,24 @@ class MonoBuild:; symbols: MonoBuild, tuned, _moe_key, _ffn_symbol_params
  - `vllm/models/deepseek_v41/amd/mono/attention/front.py` modified +92/-27 (119 lines); hunks: -64,6 +64,7; -82,7 +83,10; symbols: FrontBuild, plus, publish, quant_x_half
  - `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +86/-16 (102 lines); hunks: -67,6 +67,7; -77,9 +78,13; symbols: BackBuild, plus, p_row, publish
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono/stages/moe.py
@@ -65,8 +65,12 @@
+    oob,
+    oob_rsrc,
+    udiv,
+    umod,
@@ -90,6 +94,7 @@
+    uniform,
diff -- vllm/models/deepseek_v41/amd/mono/stages/seam.py
@@ -33,6 +33,8 @@
+    bf2_f32,
+    bf16_pair,
@@ -50,6 +52,7 @@
+    ld_vec,
@@ -246,6 +249,171 @@ def slice_mix(c, task, t0, n):
+# ---------------------------------------------------------------- reduce + slice
diff -- vllm/models/deepseek_v41/amd/mono/layer.py
@@ -34,10 +34,19 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +542/-79; `vllm/models/deepseek_v41/amd/mono/stages/seam.py` modified +196/-6; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +133/-40; `vllm/models/deepseek_v41/amd/mono/attention/front.py` modified +92/-27; `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +86/-16; `vllm/models/deepseek_v41/amd/mono/common/mx.py` modified +43/-8
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv41_mono_numerics.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60762 - [Bugfix][DSv4.1] Declare 64-token kernel blocks for SM120 sparse backends

- Link: https://github.com/vllm-project/vllm/pull/60762
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`; associated commits `7ecc83a98775`
- Diff scope read: GitHub Pull Request files API returned 2 files, +9/-0, 30 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Declare 64-token kernel blocks for SM120 sparse backends"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`; technical summary: Covers "[Bugfix][DSv4.1] Declare 64-token kernel blocks for SM120 sparse backends"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +5/-0 (5 lines); hunks: -31,6 +31,7; -63,6 +64,10 @@ class DeepseekV4FlashInferMLASparseBackend(DeepseekV4SparseML...; symbols: DeepseekV4FlashInferMLASparseBackend, get_supported_kernel_block_sizes, touching `DeepseekV4FlashInferMLASparseBackend, get_supported_kernel_block_sizes`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +5/-0 (5 lines); hunks: -31,6 +31,7; -63,6 +64,10 @@ class DeepseekV4FlashInferMLASparseBackend(DeepseekV4SparseML...; symbols: DeepseekV4FlashInferMLASparseBackend, get_supported_kernel_block_sizes
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py
@@ -31,6 +31,7 @@
+from vllm.platforms import current_platform
@@ -63,6 +64,10 @@ class DeepseekV4FlashInferMLASparseBackend(DeepseekV4SparseMLABackend):
+        # SM12x kernels only instantiate 64-token sparse-MLA blocks (128
+        # trips the block_kv assert, #59203).
+        if current_platform.is_device_capability_family(120):
+            return [64]
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +5/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/v1/attention/backends/mla/indexer.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #65552 - [CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype

- Link: https://github.com/vllm-project/vllm/pull/65552
- Status/date: merged / 2026-11-05
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`; associated commits `19e3cfb4f8bf`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`; technical summary: Covers "[CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype"; the main implementation surface is `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` modified +1/-0 (1 lines); hunks: -495,6 +495,7 @@ class _Mxfp8Linear(nn.Module):; symbols: _Mxfp8Linear, __init__, touching `_Mxfp8Linear, __init__`.
- Code diff details:
  - `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` modified +1/-0 (1 lines); hunks: -495,6 +495,7 @@ class _Mxfp8Linear(nn.Module):; symbols: _Mxfp8Linear, __init__
- Key code excerpts:

```diff
diff -- tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py
@@ -495,6 +495,7 @@ class _Mxfp8Linear(nn.Module):
+        self.params_dtype = torch.bfloat16
```

- Reviewed files:
  - tests: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63367 - [ROCm][DSv4.1] Shard the Engram gate so TP ranks gather only the value slice

- Link: https://github.com/vllm-project/vllm/pull/63367
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/engram.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/common/engram.py`; associated commits `586d2f7324bf`
- Diff scope read: GitHub Pull Request files API returned 4 files, +504/-12, 576 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1] Shard the Engram gate so TP ranks gather only the value slice"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v41/amd/engram.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/amd/model.py`; technical summary: Covers "[ROCm][DSv4.1] Shard the Engram gate so TP ranks gather only the value slice"; the main implementation surface is `vllm/models/deepseek_v41/amd/engram.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/engram.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: _shards_engram_gate, _engram_gate_partials_kernel, _engram_gate_finish_kernel, RocmEngram, touching `_shards_engram_gate, _engram_gate_partials_kernel, _engram_gate_finish_kernel`; `vllm/models/deepseek_v41/common/engram.py` modified +28/-11 (39 lines); hunks: -1701,17 +1701,8 @@ def __init__(; -1725,6 +1716,22 @@ def __init__(; symbols: __init__, _create_wkv, _create_embedding, forward, touching `__init__, _create_wkv, _create_embedding`; `vllm/models/deepseek_v41/amd/model.py` modified +2/-1 (3 lines); hunks: -65,6 +65,7; -212,7 +213,7 @@ def __init__(; symbols: __init__, touching `__init__`; `tests/kernels/test_engram.py` modified +193/-0 (193 lines); hunks: -7,16 +7,22; -144,6 +150,193 @@ def check_local_projection(_, args):; symbols: _reference_engram_post_wkv, check_local_projection, test_sharded_engram_post_wkv_matches_reference, record, touching `_reference_engram_post_wkv, check_local_projection, test_sharded_engram_post_wkv_matches_reference`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/engram.py` added +281/-0 (281 lines); hunks: -0,0 +1,281; symbols: _shards_engram_gate, _engram_gate_partials_kernel, _engram_gate_finish_kernel, RocmEngram
  - `vllm/models/deepseek_v41/common/engram.py` modified +28/-11 (39 lines); hunks: -1701,17 +1701,8 @@ def __init__(; -1725,6 +1716,22 @@ def __init__(; symbols: __init__, _create_wkv, _create_embedding, forward
  - `vllm/models/deepseek_v41/amd/model.py` modified +2/-1 (3 lines); hunks: -65,6 +65,7; -212,7 +213,7 @@ def __init__(; symbols: __init__
  - `tests/kernels/test_engram.py` modified +193/-0 (193 lines); hunks: -7,16 +7,22; -144,6 +150,193 @@ def check_local_projection(_, args):; symbols: _reference_engram_post_wkv, check_local_projection, test_sharded_engram_post_wkv_matches_reference, record
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/engram.py
@@ -0,0 +1,281 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Engram with a TP-sharded gate on gfx942 and gfx950."""
+import torch
+from vllm.distributed import (
+    get_tensor_model_parallel_rank,
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -1701,17 +1701,8 @@ def __init__(
-        # Without sequence parallelism every TP rank holds every token, so
-        # shard the output columns instead of replicating the projection.
-        self.wkv = ColumnParallelLinear(
-            n_hash_cols * layout.head_dim,
-            self.dim * (self.hc_mult + 1),
-            bias=False,
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -65,6 +65,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/engram.py` added +281/-0; `vllm/models/deepseek_v41/common/engram.py` modified +28/-11; `vllm/models/deepseek_v41/amd/model.py` modified +2/-1
  - tests: `tests/kernels/test_engram.py` modified +193/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_engram.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59802 - [ROCm][DSv4.1][Perf] Overlap the mHC gate projection with attention and FFN

- Link: https://github.com/vllm-project/vllm/pull/59802
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/mhc.py`, `vllm/models/deepseek_v41/amd/model.py`; associated commits `7871c62b61ac`
- Diff scope read: GitHub Pull Request files API returned 5 files, +592/-6, 741 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Overlap the mHC gate projection with attention and FFN"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/mhc.py`, `vllm/models/deepseek_v41/amd/model.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Overlap the mHC gate projection with attention and FFN"; the main implementation surface is `vllm/models/deepseek_v41/amd/mhc.py`, `vllm/models/deepseek_v41/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mhc.py` added +140/-0 (140 lines); hunks: -0,0 +1,140; symbols: supports_mhc_overlap, MHCOverlapStream, __init__, fork, touching `supports_mhc_overlap, MHCOverlapStream, __init__`; `vllm/models/deepseek_v41/amd/model.py` modified +44/-6 (50 lines); hunks: -2,6 +2,7; -15,8 +16,13; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mhc.py` added +140/-0 (140 lines); hunks: -0,0 +1,140; symbols: supports_mhc_overlap, MHCOverlapStream, __init__, fork
  - `vllm/models/deepseek_v41/amd/model.py` modified +44/-6 (50 lines); hunks: -2,6 +2,7; -15,8 +16,13; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mhc.py
@@ -0,0 +1,140 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Overlap the DSV4.1 mHC gate projection with the next sublayer on ROCm."""
+import torch
+from vllm.config import VllmConfig
+from vllm.model_executor.kernels.mhc.triton import mhc_post_collapse_rms_norm_triton
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -2,6 +2,7 @@
+from functools import partial
@@ -15,8 +16,13 @@
-from vllm.forward_context import get_forward_context, is_forward_context_available
+from vllm.forward_context import (
+    get_forward_context,
+    in_piecewise_cudagraph,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mhc.py` added +140/-0; `vllm/models/deepseek_v41/amd/model.py` modified +44/-6
- Risk and verification: The diff ships test coverage in `tests/kernels/mhc/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63921 - [Perf][DSv4.1] Extend the latency_specialized decode on NVIDIA

- Link: https://github.com/vllm-project/vllm/pull/63921
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/deepseek_v41/nvidia/specialized_decode/test_all_gather.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_decode_topk.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_layers.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` and 38 files; associated commits `c58e7f6d0531`
- Diff scope read: GitHub Pull Request files API returned 41 files, +6655/-790, 9732 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Extend the latency_specialized decode on NVIDIA"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/decode_topk_cute.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla_cute.py`, `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py`; technical summary: Covers "[Perf][DSv4.1] Extend the latency_specialized decode on NVIDIA"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/decode_topk_cute.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla_cute.py`, `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/decode_topk_cute.py` added +1331/-0 (1331 lines); hunks: -0,0 +1,1331; symbols: _asm, _v, _u32x4, load_u32x4, touching `_asm, _v, _u32x4`; `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla_cute.py` added +986/-0 (986 lines); hunks: -0,0 +1,986; symbols: _sdesc, _asm, _v, cp_async_16, touching `_sdesc, _asm, _v`; `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` modified +582/-124 (706 lines); hunks: -1,7 +1,29; -13,6 +35,22; symbols: _SharedOnlyPublishDeviceKernel, __init__, kernel, touching `_SharedOnlyPublishDeviceKernel, __init__, kernel`; `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py` modified +429/-126 (555 lines); hunks: -40,7 +40,7; -62,22 +62,36; symbols: RoutedExpertGemm, _launch, kernel, SharedStorage, touching `RoutedExpertGemm, _launch, kernel`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/decode_topk_cute.py` added +1331/-0 (1331 lines); hunks: -0,0 +1,1331; symbols: _asm, _v, _u32x4, load_u32x4
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla_cute.py` added +986/-0 (986 lines); hunks: -0,0 +1,986; symbols: _sdesc, _asm, _v, cp_async_16
  - `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` modified +582/-124 (706 lines); hunks: -1,7 +1,29; -13,6 +35,22; symbols: _SharedOnlyPublishDeviceKernel, __init__, kernel
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py` modified +429/-126 (555 lines); hunks: -40,7 +40,7; -62,22 +62,36; symbols: RoutedExpertGemm, _launch, kernel, SharedStorage
  - `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_gather.py` added +405/-0 (405 lines); hunks: -0,0 +1,405; symbols: _asm, _load_u32x4, _store_u32x4, _load_volatile_u32
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/specialized_decode/attention/decode_topk_cute.py
@@ -0,0 +1,1331 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Decode top-k of the dense indexers straight from their BF16 logits, in CuTe DSL.
+The problem. In a decode step each dense indexer layer scores every compressed
+token of a row (SM100's paged MQA logits are BF16) and keeps the ``k`` largest:
+the token top-512, and in the candidate source also the top-2048 of the rows'
diff -- vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla_cute.py
@@ -0,0 +1,986 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The sparse-MLA decode of small batches, in CuTe DSL.
+The problem. In a decode step every query token (DeepSeek-V4's MLA after the
+query projection: 16 heads a rank at TP4, FP8 E4M3, head dim 512) attends to
+its own sparse set of KV rows. A row is 512 FP8 bytes and serves as both K and
diff -- vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py
@@ -1,7 +1,29 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/decode_topk_cute.py` added +1331/-0; `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla_cute.py` added +986/-0; `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` modified +582/-124; `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py` modified +429/-126; `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_gather.py` added +405/-0; `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_route_cute.py` modified +265/-69
- Risk and verification: The diff ships test coverage in `tests/distributed/test_custom_all_reduce.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_all_gather.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_decode_topk.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62729 - [Bugfix] Honor add_generation_prompt and continue_final_message in the DeepSeek V4.1 tokenizer

- Link: https://github.com/vllm-project/vllm/pull/62729
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/engine/test_deepseek_v41.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/parser/deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`; associated commits `925db4c416b8`
- Diff scope read: GitHub Pull Request files API returned 5 files, +197/-6, 313 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Honor add_generation_prompt and continue_final_message in the DeepSeek V4.1 tokenizer"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `vllm/tokenizers/deepseek_v41.py`; technical summary: Covers "[Bugfix] Honor add_generation_prompt and continue_final_message in the DeepSeek V4.1 tokenizer"; the main implementation surface is `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `vllm/tokenizers/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v41.py` modified +110/-2 (112 lines); hunks: -48,21 +48,31 @@ def test_reference_encoder_fixtures(case_id):; -403,3 +413,101 @@ def test_dropped_developer_only_image_leaves_text_prompt(r...; symbols: test_reference_encoder_fixtures, test_dropped_developer_only_image_leaves_text_prompt, test_generation_prompt_only_controls_final_turn, test_continue_final_message_preserves_historical_eos, touching `test_reference_encoder_fixtures, test_dropped_developer_only_image_leaves_text_prompt, test_generation_prompt_only_controls_final_turn`; `vllm/tokenizers/deepseek_v41_encoding.py` modified +32/-3 (35 lines); hunks: -332,6 +332,8 @@ def render_message(; -350,7 +352,8 @@ def render_message(; symbols: render_message, touching `render_message`; `vllm/tokenizers/deepseek_v41.py` modified +2/-0 (2 lines); hunks: -127,6 +127,8 @@ def apply_chat_template(; symbols: apply_chat_template, touching `apply_chat_template`; `tests/parser/engine/test_deepseek_v41.py` modified +49/-1 (50 lines); hunks: -27,7 +27,7; -132,6 +132,54 @@ def test_reasoning_adapter_controls_and_usage(; symbols: tokenizer_for, test_reasoning_adapter_controls_and_usage, test_prompt_closed_reasoning_is_scoped_to_current_turn, test_python_argument_conversion_and_partial_values, touching `tokenizer_for, test_reasoning_adapter_controls_and_usage, test_prompt_closed_reasoning_is_scoped_to_current_turn`.
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v41.py` modified +110/-2 (112 lines); hunks: -48,21 +48,31 @@ def test_reference_encoder_fixtures(case_id):; -403,3 +413,101 @@ def test_dropped_developer_only_image_leaves_text_prompt(r...; symbols: test_reference_encoder_fixtures, test_dropped_developer_only_image_leaves_text_prompt, test_generation_prompt_only_controls_final_turn, test_continue_final_message_preserves_historical_eos
  - `vllm/tokenizers/deepseek_v41_encoding.py` modified +32/-3 (35 lines); hunks: -332,6 +332,8 @@ def render_message(; -350,7 +352,8 @@ def render_message(; symbols: render_message
  - `vllm/tokenizers/deepseek_v41.py` modified +2/-0 (2 lines); hunks: -127,6 +127,8 @@ def apply_chat_template(; symbols: apply_chat_template
  - `tests/parser/engine/test_deepseek_v41.py` modified +49/-1 (50 lines); hunks: -27,7 +27,7; -132,6 +132,54 @@ def test_reasoning_adapter_controls_and_usage(; symbols: tokenizer_for, test_reasoning_adapter_controls_and_usage, test_prompt_closed_reasoning_is_scoped_to_current_turn, test_python_argument_conversion_and_partial_values
  - `vllm/parser/deepseek_v41.py` modified +4/-0 (4 lines); hunks: -20,6 +20,9; -38,6 +41,7 @@ def deepseek_v41_config(thinking: bool = False) -> ParserEngin...; symbols: deepseek_v41_config
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -48,21 +48,31 @@ def test_reference_encoder_fixtures(case_id):
+    # The reference encodes a conversation that ends with an assistant message as
+    # closed history, which is add_generation_prompt=False here.
+    final_assistant = messages[-1]["role"] == "assistant"
+            add_generation_prompt=not final_assistant,
-        prompt = render(
-            messages,
diff -- vllm/tokenizers/deepseek_v41_encoding.py
@@ -332,6 +332,8 @@ def render_message(
+    add_generation_prompt: bool = True,
+    continue_final_message: bool = False,
@@ -350,7 +352,8 @@ def render_message(
-    wo_eos = msg.get("wo_eos", False)
+    is_last = index == len(messages) - 1
+    wo_eos = msg.get("wo_eos", False) or (is_last and continue_final_message)
diff -- vllm/tokenizers/deepseek_v41.py
@@ -127,6 +127,8 @@ def apply_chat_template(
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v41.py` modified +110/-2; `tests/parser/engine/test_deepseek_v41.py` modified +49/-1
  - runtime: `vllm/tokenizers/deepseek_v41_encoding.py` modified +32/-3; `vllm/tokenizers/deepseek_v41.py` modified +2/-0; `vllm/parser/deepseek_v41.py` modified +4/-0
- Risk and verification: The diff ships test coverage in `tests/parser/engine/test_deepseek_v41.py`, `tests/tokenizers_/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62647 - [Bugfix][Frontend] Materialize DeepSeek V4.1 content iterators before deepcopy

- Link: https://github.com/vllm-project/vllm/pull/62647
- Status/date: merged / 2026-11-04
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`; associated commits `643d6531feef`
- Diff scope read: GitHub Pull Request files API returned 2 files, +31/-1, 53 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Frontend] Materialize DeepSeek V4.1 content iterators before deepcopy"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`; technical summary: Covers "[Bugfix][Frontend] Materialize DeepSeek V4.1 content iterators before deepcopy"; the main implementation surface is `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v41.py` modified +24/-0 (24 lines); hunks: -175,6 +175,30 @@ def test_raw_text_parts_preserve_reference_separator():; symbols: test_raw_text_parts_preserve_reference_separator, test_request_content_iterator_can_be_rendered_repeatedly, touching `test_raw_text_parts_preserve_reference_separator, test_request_content_iterator_can_be_rendered_repeatedly`; `vllm/tokenizers/deepseek_v41.py` modified +7/-1 (8 lines); hunks: -2,6 +2,7; -30,7 +31,12 @@ def _normalize_messages(; symbols: _normalize_messages, touching `_normalize_messages`.
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v41.py` modified +24/-0 (24 lines); hunks: -175,6 +175,30 @@ def test_raw_text_parts_preserve_reference_separator():; symbols: test_raw_text_parts_preserve_reference_separator, test_request_content_iterator_can_be_rendered_repeatedly
  - `vllm/tokenizers/deepseek_v41.py` modified +7/-1 (8 lines); hunks: -2,6 +2,7; -30,7 +31,12 @@ def _normalize_messages(; symbols: _normalize_messages
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -175,6 +175,30 @@ def test_raw_text_parts_preserve_reference_separator():
+@pytest.mark.parametrize(
+    ("content", "stream"),
+    [
+        ([], False),
+        ([], True),
+        ([{"type": "text", "text": "hello"}], False),
diff -- vllm/tokenizers/deepseek_v41.py
@@ -2,6 +2,7 @@
+from collections.abc import Iterator
@@ -30,7 +31,12 @@ def _normalize_messages(
-    result = [dict(message) for message in copy.deepcopy(messages)]
+    result: list[dict[str, Any]] = []
+    for original_message in messages:
+        content = original_message.get("content")
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v41.py` modified +24/-0
  - runtime: `vllm/tokenizers/deepseek_v41.py` modified +7/-1
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62633 - [Perf][Kernel][DSv4.1] Swap-AB CuTe DSL decode attention for small TP2/TP4 steps

- Link: https://github.com/vllm-project/vllm/pull/62633
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/deepseek_v41/nvidia/test_swapab_decode.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py`; associated commits `4b01cbad1bb6`
- Diff scope read: GitHub Pull Request files API returned 5 files, +2030/-21, 2193 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][Kernel][DSv4.1] Swap-AB CuTe DSL decode attention for small TP2/TP4 steps"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py`, `tests/models/deepseek_v41/nvidia/test_swapab_decode.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; technical summary: Covers "[Perf][Kernel][DSv4.1] Swap-AB CuTe DSL decode attention for small TP2/TP4 steps"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py`, `tests/models/deepseek_v41/nvidia/test_swapab_decode.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py` added +1263/-0 (1263 lines); hunks: -0,0 +1,1263; symbols: _asm, _v, _fields, _ldg_s32, touching `_asm, _v, _fields`; `tests/models/deepseek_v41/nvidia/test_swapab_decode.py` added +606/-0 (606 lines); hunks: -0,0 +1,606; symbols: Case, cos_sin_cache, _swapab_module, swapab_kernel, touching `Case, cos_sin_cache, _swapab_module`; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +105/-6 (111 lines); hunks: -13,6 +13,9; -21,6 +24,7; symbols: is_flashmla_mega_attn_supported, _swapab_decode_supported, alloc_mega_attn_output, __init__, touching `is_flashmla_mega_attn_supported, _swapab_decode_supported, alloc_mega_attn_output`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py` added +1263/-0 (1263 lines); hunks: -0,0 +1,1263; symbols: _asm, _v, _fields, _ldg_s32
  - `tests/models/deepseek_v41/nvidia/test_swapab_decode.py` added +606/-0 (606 lines); hunks: -0,0 +1,606; symbols: Case, cos_sin_cache, _swapab_module, swapab_kernel
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +105/-6 (111 lines); hunks: -13,6 +13,9; -21,6 +24,7; symbols: is_flashmla_mega_attn_supported, _swapab_decode_supported, alloc_mega_attn_output, __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py
@@ -0,0 +1,1263 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Adapted from SGLang's swap-AB DSv4 decode attention (Apache-2.0):
+# https://github.com/sgl-project/sglang/blob/91b3692a4c39453694f53ff54b67186ca4a7f34c/python/sglang/kernels/ops/attention/dsv4/decode_attention_sm100.py
+# https://github.com/sgl-project/sglang/blob/91b3692a4c39453694f53ff54b67186ca4a7f34c/python/sglang/kernels/ops/attention/dsv4/decode_attention_sm100_gluon.py
+"""Swap-AB decode attention for DeepSeek V4.1's small decode steps (SM100).
diff -- tests/models/deepseek_v41/nvidia/test_swapab_decode.py
@@ -0,0 +1,606 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DeepSeek V4.1 swap-AB decode attention vs FlashMLA's mega kernel.
+The swap-AB kernel keeps the mega kernel's contract: it reads Q in the
+chunk-interleaved, head-padded layout and writes MXFP8 in the o-fused layout
+``wo_a`` reads, for the live heads' groups only. The caches are written by
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -13,6 +13,9 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/swapab_decode_attn.py` added +1263/-0; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +105/-6
  - tests: `tests/models/deepseek_v41/nvidia/test_swapab_decode.py` added +606/-0
- Risk and verification: The diff ships test coverage in `tests/models/deepseek_v41/nvidia/test_swapab_decode.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #65030 - [Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes

- Link: https://github.com/vllm-project/vllm/pull/65030
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`; associated commits `0eeae6a47333`
- Diff scope read: GitHub Pull Request files API returned 4 files, +71/-54, 188 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`; technical summary: Covers "[Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes"; the main implementation surface is `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/vision.py` modified +53/-0 (53 lines); hunks: -39,6 +39,7; -393,6 +394,58 @@ def forward_packed(; symbols: _compute_vision_cos_sin, forward_packed, encode_images, run_dp_sharded_vision_tower, touching `_compute_vision_cos_sin, forward_packed, encode_images`; `vllm/models/deepseek_v4/common/vl_model.py` modified +10/-34 (44 lines); hunks: -48,7 +48,7; -201,20 +201,6 @@ def _parse_and_validate_image_input(self, **kwargs: object)...; symbols: _make_deepseek_v4_vl_weights_mapper, _parse_and_validate_image_input, _encode_image, _process_image_input, touching `_make_deepseek_v4_vl_weights_mapper, _parse_and_validate_image_input, _encode_image`; `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -238,16 +239,9 @@ def _process_image_input(; symbols: _process_image_input, touching `_process_image_input`; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -220,16 +221,9 @@ def _process_image_input(; symbols: _process_image_input, touching `_process_image_input`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/vision.py` modified +53/-0 (53 lines); hunks: -39,6 +39,7; -393,6 +394,58 @@ def forward_packed(; symbols: _compute_vision_cos_sin, forward_packed, encode_images, run_dp_sharded_vision_tower
  - `vllm/models/deepseek_v4/common/vl_model.py` modified +10/-34 (44 lines); hunks: -48,7 +48,7; -201,20 +201,6 @@ def _parse_and_validate_image_input(self, **kwargs: object)...; symbols: _make_deepseek_v4_vl_weights_mapper, _parse_and_validate_image_input, _encode_image, _process_image_input
  - `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -238,16 +239,9 @@ def _process_image_input(; symbols: _process_image_input
  - `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-10 (14 lines); hunks: -39,6 +39,7; -220,16 +221,9 @@ def _process_image_input(; symbols: _process_image_input
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/vision.py
@@ -39,6 +39,7 @@
+from vllm.v1.attention.backends.registry import AttentionBackendEnum
@@ -393,6 +394,58 @@ def forward_packed(
+def encode_images(
+    vision_model: DeepseekV4ViT,
+    aligner: DeepseekV4Aligner,
+    patches: torch.Tensor,
diff -- vllm/models/deepseek_v4/common/vl_model.py
@@ -48,7 +48,7 @@
-from .vision import DeepseekV4Aligner, DeepseekV4ViT
+from .vision import DeepseekV4Aligner, DeepseekV4ViT, encode_images
@@ -201,20 +201,6 @@ def _parse_and_validate_image_input(self, **kwargs: object) -> dict | None:
-    def _encode_image(
-        self,
-        patches: torch.Tensor,
diff -- vllm/models/deepseek_v41/amd/vl_model.py
@@ -39,6 +39,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/vision.py` modified +53/-0; `vllm/models/deepseek_v4/common/vl_model.py` modified +10/-34; `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-10; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-10
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57245 - [LoRA] Add DeepSeek V4.1 language-model adapter support

- Link: https://github.com/vllm-project/vllm/pull/57245
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/compressor.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` and 6 files; associated commits `a5d8174ea05f`
- Diff scope read: GitHub Pull Request files API returned 11 files, +562/-13, 780 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[LoRA] Add DeepSeek V4.1 language-model adapter support"; model line: DeepSeek V4; category: model support/runtime entry; main diff: `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`, `vllm/models/deepseek_v41/attention.py`; technical summary: Covers "[LoRA] Add DeepSeek V4.1 language-model adapter support"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`, `vllm/models/deepseek_v41/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model.py` modified +19/-2 (21 lines); hunks: -238,6 +238,12 @@ def _select_dsv4_attn_cls(vllm_config: VllmConfig) -> type[...; -254,7 +260,9 @@ def _select_dsv4_attn_cls(vllm_config: VllmConfig) -> type[D...; symbols: _select_dsv4_attn_cls, maybe_init_gemm_rs, __init__, load_weights, touching `_select_dsv4_attn_cls, maybe_init_gemm_rs, __init__`; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +20/-0 (20 lines); hunks: -27,9 +27,11; -122,6 +124,7 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV41ForCausalLM, get_mtp_target_hidden_states, load_weights, get_mm_mapping, touching `DeepseekV41ForCausalLM, get_mtp_target_hidden_states, load_weights`; `vllm/models/deepseek_v41/attention.py` modified +4/-6 (10 lines); hunks: -66,6 +66,7; -447,9 +448,10 @@ def __init__(; symbols: __init__, _run_parallel_input_projections, compressor_kv_score, touching `__init__, _run_parallel_input_projections, compressor_kv_score`; `vllm/models/deepseek_v41/compressor.py` modified +9/-1 (10 lines); hunks: -271,6 +271,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:; -321,7 +329,7 @@ def __init__(; symbols: get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward, DeepseekCompressor, touching `get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +19/-2 (21 lines); hunks: -238,6 +238,12 @@ def _select_dsv4_attn_cls(vllm_config: VllmConfig) -> type[...; -254,7 +260,9 @@ def _select_dsv4_attn_cls(vllm_config: VllmConfig) -> type[D...; symbols: _select_dsv4_attn_cls, maybe_init_gemm_rs, __init__, load_weights
  - `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +20/-0 (20 lines); hunks: -27,9 +27,11; -122,6 +124,7 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV41ForCausalLM, get_mtp_target_hidden_states, load_weights, get_mm_mapping
  - `vllm/models/deepseek_v41/attention.py` modified +4/-6 (10 lines); hunks: -66,6 +66,7; -447,9 +448,10 @@ def __init__(; symbols: __init__, _run_parallel_input_projections, compressor_kv_score
  - `vllm/models/deepseek_v41/compressor.py` modified +9/-1 (10 lines); hunks: -271,6 +271,14 @@ def get_attn_backend(self) -> type[AttentionBackend]:; -321,7 +329,7 @@ def __init__(; symbols: get_attn_backend, DeepseekV4CompressorKVScoreLinear, forward, DeepseekCompressor
  - `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +6/-4 (10 lines); hunks: -16,7 +16,6; -32,6 +31,10 @@ def _fused_wo_a_max_tokens(layer: nn.Module) -> int:; symbols: _fused_wo_a_max_tokens, _can_fuse_wo_a, dsv41_o_proj
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -238,6 +238,12 @@ def _select_dsv4_attn_cls(vllm_config: VllmConfig) -> type[DeepseekV4Attention]:
+        # FlashMLA mega attention reads the grouped ``wo_a`` weight directly
+        # from its fused quantized output. LoRA wraps that layer after model
+        # construction, so use the split-KV path whose grouped projection
+        # explicitly applies the adapter delta.
+        if vllm_config.lora_config is not None:
+            return DeepseekV4FlashMLAAttention
diff -- vllm/models/deepseek_v41/nvidia/vl_model.py
@@ -27,9 +27,11 @@
+    SupportsLoRA,
+from vllm.model_executor.models.module_mapping import MultiModelKeys
@@ -122,6 +124,7 @@ class DeepseekV41ForCausalLM(
+    SupportsLoRA,
@@ -133,6 +136,15 @@ class DeepseekV41ForCausalLM(
+    packed_modules_mapping = {
diff -- vllm/models/deepseek_v41/attention.py
@@ -66,6 +66,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model.py` modified +19/-2; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +20/-0; `vllm/models/deepseek_v41/attention.py` modified +4/-6; `vllm/models/deepseek_v41/compressor.py` modified +9/-1; `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +6/-4
  - tests: `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/lora/test_layers.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #65296 - [Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters

- Link: https://github.com/vllm-project/vllm/pull/65296
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `22d05b87bbc9`
- Diff scope read: GitHub Pull Request files API returned 2 files, +18/-11, 84 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-8 (22 lines); hunks: -17,6 +17,7; -1100,7 +1101,6 @@ def prepare_attn_preshuffle(self) -> None:; symbols: prepare_attn_preshuffle, _prep, _prepare_fp8_wo_a, prepare_compressor_gemm_fusion, touching `prepare_attn_preshuffle, _prep, _prepare_fp8_wo_a`; `vllm/models/deepseek_v4/amd/model.py` modified +4/-3 (7 lines); hunks: -73,7 +73,7; -155,7 +155,6 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward, touching `prepare_gateup_preshuffle, forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-8 (22 lines); hunks: -17,6 +17,7; -1100,7 +1101,6 @@ def prepare_attn_preshuffle(self) -> None:; symbols: prepare_attn_preshuffle, _prep, _prepare_fp8_wo_a, prepare_compressor_gemm_fusion
  - `vllm/models/deepseek_v4/amd/model.py` modified +4/-3 (7 lines); hunks: -73,7 +73,7; -155,7 +155,6 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -17,6 +17,7 @@
+from vllm.model_executor.utils import refill_derived, replace_parameter
@@ -1100,7 +1101,6 @@ def prepare_attn_preshuffle(self) -> None:
-        from vllm.model_executor.utils import replace_parameter
@@ -1122,10 +1122,13 @@ def _prep(linear) -> torch.Tensor | None:
-            return ws
+            # A plain tensor: assigning the scale Parameter itself would register
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -73,7 +73,7 @@
-from vllm.model_executor.utils import refill_derived
+from vllm.model_executor.utils import refill_derived, replace_parameter
@@ -155,7 +155,6 @@ def prepare_gateup_preshuffle(self) -> None:
-        from vllm.model_executor.utils import replace_parameter
@@ -173,7 +172,9 @@ def prepare_gateup_preshuffle(self) -> None:
-        self._gateup_scale = ws
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-8; `vllm/models/deepseek_v4/amd/model.py` modified +4/-3
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #64974 - [Refactor][DSv4.1] Remove duplicated code

- Link: https://github.com/vllm-project/vllm/pull/64974
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py` and 8 files; associated commits `45d0ac9ee197`
- Diff scope read: GitHub Pull Request files API returned 9 files, +57/-328, 737 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor][DSv4.1] Remove duplicated code"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Refactor][DSv4.1] Remove duplicated code"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-159 (170 lines); hunks: -30,6 +30,10; -56,131 +60,6; symbols: quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, combine_topk_swa_indices, _hf_config_int, touching `quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, combine_topk_swa_indices`; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +13/-67 (80 lines); hunks: -9,6 +9,12; -33,72 +39,12; symbols: _get_flashinfer_dsv4_workspace, _packed_block_span, _pad_to_supported_q_heads, _required_sm120_sparse_topk, touching `_get_flashinfer_dsv4_workspace, _packed_block_span, _pad_to_supported_q_heads`; `vllm/models/deepseek_v41/nvidia/model.py` modified +4/-41 (45 lines); hunks: -54,7 +54,6; -76,13 +75,14; symbols: _make_deepseek_v4_weights_mapper, DeepseekV4MixtureOfExperts, extract_moe_parameters, update_physical_experts_metadata, touching `_make_deepseek_v4_weights_mapper, DeepseekV4MixtureOfExperts, extract_moe_parameters`; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +9/-23 (32 lines); hunks: -806,17 +806,6 @@ def combine_topk_swa_indices(; -960,12 +949,9 @@ def dispatch( # type: ignore[override]; symbols: combine_topk_swa_indices, _hf_config_int, _scheduler_config_int, CombineTopkSwaIndicesKernel, touching `combine_topk_swa_indices, _hf_config_int, _scheduler_config_int`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-159 (170 lines); hunks: -30,6 +30,10; -56,131 +60,6; symbols: quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, combine_topk_swa_indices, _hf_config_int
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +13/-67 (80 lines); hunks: -9,6 +9,12; -33,72 +39,12; symbols: _get_flashinfer_dsv4_workspace, _packed_block_span, _pad_to_supported_q_heads, _required_sm120_sparse_topk
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +4/-41 (45 lines); hunks: -54,7 +54,6; -76,13 +75,14; symbols: _make_deepseek_v4_weights_mapper, DeepseekV4MixtureOfExperts, extract_moe_parameters, update_physical_experts_metadata
  - `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +9/-23 (32 lines); hunks: -806,17 +806,6 @@ def combine_topk_swa_indices(; -960,12 +949,9 @@ def dispatch( # type: ignore[override]; symbols: combine_topk_swa_indices, _hf_config_int, _scheduler_config_int, CombineTopkSwaIndicesKernel
  - `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +11/-11 (22 lines); hunks: -47,7 +47,7; -59,7 +59,7 @@ def _get_flashinfer_dsv4_workspace(device: torch.device) -> to...; symbols: _get_flashinfer_dsv4_workspace, get_flashinfer_dsv4_workspace, _packed_block_span, packed_block_span
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -30,6 +30,10 @@
+from vllm.models.deepseek_v4.common.ops.cache_utils import (
+    quantize_and_insert_k_kernel,
+    remap_flashinfer_index,
+)
@@ -56,131 +60,6 @@
-@triton.jit
diff -- vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py
@@ -9,6 +9,12 @@
+from vllm.models.deepseek_v4.nvidia.flashinfer_sparse import (
+    get_flashinfer_dsv4_workspace,
+    packed_block_span,
+    pad_to_supported_q_heads,
+    required_sm120_sparse_topk,
+)
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -54,7 +54,6 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-159; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +13/-67; `vllm/models/deepseek_v41/nvidia/model.py` modified +4/-41; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +9/-23; `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +11/-11; `vllm/models/deepseek_v41/attention.py` modified +2/-20
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_flashinfer_sparse_mla_sm120_api.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62802 - [EPD] Support DeepSeek-V4.1 image metadata-only inputs

- Link: https://github.com/vllm-project/vllm/pull/62802
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/common/mm_preprocess.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py` and 7 files; associated commits `67791dd94d95`
- Diff scope read: GitHub Pull Request files API returned 7 files, +293/-30, 466 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[EPD] Support DeepSeek-V4.1 image metadata-only inputs"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v41/common/mm_preprocess.py`, `vllm/models/deepseek_v41/amd/vl_model.py`; technical summary: Covers "[EPD] Support DeepSeek-V4.1 image metadata-only inputs"; the main implementation surface is `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v41/common/mm_preprocess.py`, `vllm/models/deepseek_v41/amd/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_deepseek_v4_vl.py` modified +190/-0 (190 lines); hunks: -2,14 +2,32; -65,3 +83,175 @@ def test_get_image_size_with_most_features_respects_max_wh_r...; symbols: test_get_image_size_with_most_features_respects_max_wh_ratio, test_v41_image_metadata_only_roundtrip, unexpected_preprocessing, test_v41_renderer_keeps_metadata_when_image_order_is_unchanged, touching `test_get_image_size_with_most_features_respects_max_wh_ratio, test_v41_image_metadata_only_roundtrip, unexpected_preprocessing`; `vllm/models/deepseek_v41/common/mm_preprocess.py` modified +57/-23 (80 lines); hunks: -29,7 +29,12; -246,15 +251,62 @@ def __call__(; symbols: __call__, _get_image_fields, DeepseekV4VLMultiModalDataParser, _parse_image_data, touching `__call__, _get_image_fields, DeepseekV4VLMultiModalDataParser`; `vllm/models/deepseek_v41/amd/vl_model.py` modified +9/-1 (10 lines); hunks: -49,6 +49,7; -157,7 +158,7 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV41ForCausalLM, get_placeholder_str, _process_image_input, embed_multimodal, touching `DeepseekV41ForCausalLM, get_placeholder_str, _process_image_input`; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +9/-1 (10 lines); hunks: -49,6 +49,7; -139,7 +140,7 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV41ForCausalLM, get_placeholder_str, _process_image_input, embed_multimodal, touching `DeepseekV41ForCausalLM, get_placeholder_str, _process_image_input`.
- Code diff details:
  - `tests/models/multimodal/processing/test_deepseek_v4_vl.py` modified +190/-0 (190 lines); hunks: -2,14 +2,32; -65,3 +83,175 @@ def test_get_image_size_with_most_features_respects_max_wh_r...; symbols: test_get_image_size_with_most_features_respects_max_wh_ratio, test_v41_image_metadata_only_roundtrip, unexpected_preprocessing, test_v41_renderer_keeps_metadata_when_image_order_is_unchanged
  - `vllm/models/deepseek_v41/common/mm_preprocess.py` modified +57/-23 (80 lines); hunks: -29,7 +29,12; -246,15 +251,62 @@ def __call__(; symbols: __call__, _get_image_fields, DeepseekV4VLMultiModalDataParser, _parse_image_data
  - `vllm/models/deepseek_v41/amd/vl_model.py` modified +9/-1 (10 lines); hunks: -49,6 +49,7; -157,7 +158,7 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV41ForCausalLM, get_placeholder_str, _process_image_input, embed_multimodal
  - `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +9/-1 (10 lines); hunks: -49,6 +49,7; -139,7 +140,7 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV41ForCausalLM, get_placeholder_str, _process_image_input, embed_multimodal
  - `vllm/tokenizers/deepseek_v41.py` modified +7/-2 (9 lines); hunks: -50,7 +50,12 @@ def _normalize_messages(; -142,6 +147,6 @@ def __reduce__(self):; symbols: _normalize_messages, __reduce__, DeepseekV41Tokenizer, from_pretrained
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_deepseek_v4_vl.py
@@ -2,14 +2,32 @@
+import json
+from typing import cast
+import pytest
+import torch
+from tests.models.utils import build_model_context
+from vllm.config import VllmConfig
diff -- vllm/models/deepseek_v41/common/mm_preprocess.py
@@ -29,7 +29,12 @@
-from vllm.multimodal.parse import ImageSize, MultiModalDataItems
+from vllm.multimodal.parse import (
+    DictEmbeddingItems,
+    ImageSize,
+    MultiModalDataItems,
+    MultiModalDataParser,
diff -- vllm/models/deepseek_v41/amd/vl_model.py
@@ -49,6 +49,7 @@
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_deepseek_v4_vl.py` modified +190/-0; `tests/tokenizers_/test_deepseek_v41.py` modified +5/-1
  - runtime: `vllm/models/deepseek_v41/common/mm_preprocess.py` modified +57/-23; `vllm/models/deepseek_v41/amd/vl_model.py` modified +9/-1; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +9/-1; `vllm/tokenizers/deepseek_v41.py` modified +7/-2; `vllm/renderers/deepseek_v4.py` modified +16/-2
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `tests/tokenizers_/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64442 - [Perf][DSpark][DSv4.1] Fuse the Markov sampling loop on NVIDIA by inverse CDF

- Link: https://github.com/vllm-project/vllm/pull/64442
- Status/date: merged / 2026-11-03
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/deepseek_v41/nvidia/test_fused_markov.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`, `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py`; associated commits `3d18166d453a`
- Diff scope read: GitHub Pull Request files API returned 4 files, +313/-0, 343 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSpark][DSv4.1] Fuse the Markov sampling loop on NVIDIA by inverse CDF"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py`, `tests/models/deepseek_v41/nvidia/test_fused_markov.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`; technical summary: Covers "[Perf][DSpark][DSv4.1] Fuse the Markov sampling loop on NVIDIA by inverse CDF"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py`, `tests/models/deepseek_v41/nvidia/test_fused_markov.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py` added +203/-0 (203 lines); hunks: -0,0 +1,203; symbols: _markov_sample_kernel, _markov_select_kernel, FusedMarkovSampler, __init__, touching `_markov_sample_kernel, _markov_select_kernel, FusedMarkovSampler`; `tests/models/deepseek_v41/nvidia/test_fused_markov.py` added +88/-0 (88 lines); hunks: -0,0 +1,88; symbols: _sample, test_greedy_and_cache_match_loop, test_sampled_tokens_follow_softmax, touching `_sample, test_greedy_and_cache_match_loop, test_sampled_tokens_follow_softmax`; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +20/-0 (20 lines); hunks: -64,6 +64,7; -320,6 +321,25 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py` added +203/-0 (203 lines); hunks: -0,0 +1,203; symbols: _markov_sample_kernel, _markov_select_kernel, FusedMarkovSampler, __init__
  - `tests/models/deepseek_v41/nvidia/test_fused_markov.py` added +88/-0 (88 lines); hunks: -0,0 +1,88; symbols: _sample, test_greedy_and_cache_match_loop, test_sampled_tokens_follow_softmax
  - `vllm/models/deepseek_v41/nvidia/dspark.py` modified +20/-0 (20 lines); hunks: -64,6 +64,7; -320,6 +321,25 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/fused_markov.py
@@ -0,0 +1,203 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DSpark's sequential Markov sampling as the bias GEMM plus two kernels a step.
+Tokens are drawn by inverse CDF of softmax(cached logits / temperature), one exp
+per logit instead of Gumbel-max's hash and two logs; temperature 0 is argmax."""
+import torch
diff -- tests/models/deepseek_v41/nvidia/test_fused_markov.py
@@ -0,0 +1,88 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DeepSeek-V4.1's fused DSpark Markov sampling against DSparkSpeculator's loop:
+greedy tokens and the cached logits match, sampled tokens follow the softmax."""
+from types import SimpleNamespace
+import pytest
diff -- vllm/models/deepseek_v41/nvidia/dspark.py
@@ -64,6 +64,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py` added +203/-0; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +20/-0
  - tests: `tests/models/deepseek_v41/nvidia/test_fused_markov.py` added +88/-0
- Risk and verification: The diff ships test coverage in `tests/models/deepseek_v41/nvidia/test_fused_markov.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62632 - [Perf][Kernel][DSv4.1] Copy-based Q zero-pad for large eager mega-attention steps

- Link: https://github.com/vllm-project/vllm/pull/62632
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; associated commits `28dd9c36b5fa`
- Diff scope read: GitHub Pull Request files API returned 4 files, +167/-3, 254 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][Kernel][DSv4.1] Copy-based Q zero-pad for large eager mega-attention steps"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`; technical summary: Covers "[Perf][Kernel][DSv4.1] Copy-based Q zero-pad for large eager mega-attention steps"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` modified +108/-1 (109 lines); hunks: -60,6 +60,12; -90,6 +96,78; symbols: _pad_interleaved_q_kernel, _pad_interleaved_q_warmup_inputs, _pad_interleaved_q, _replace_layer_index, touching `_pad_interleaved_q_kernel, _pad_interleaved_q_warmup_inputs, _pad_interleaved_q`; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +2/-2 (4 lines); hunks: -5,7 +5,7; -282,7 +282,7 @@ def forward_mqa(; symbols: forward_mqa, touching `forward_mqa`; `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +56/-0 (56 lines); hunks: -715,6 +715,62 @@ def run(q_in, is_q_interleaved):; symbols: run, test_q_interleaved_pad_copy_matches_fused_insert, insert, touching `run, test_q_interleaved_pad_copy_matches_fused_insert, insert`.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` modified +108/-1 (109 lines); hunks: -60,6 +60,12; -90,6 +96,78; symbols: _pad_interleaved_q_kernel, _pad_interleaved_q_warmup_inputs, _pad_interleaved_q, _replace_layer_index
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +2/-2 (4 lines); hunks: -5,7 +5,7; -282,7 +282,7 @@ def forward_mqa(; symbols: forward_mqa
  - `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +56/-0 (56 lines); hunks: -715,6 +715,62 @@ def run(q_in, is_q_interleaved):; symbols: run, test_q_interleaved_pad_copy_matches_fused_insert, insert
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -60,6 +60,12 @@
+from vllm.model_executor.warmup.jit_warmup_triton_helper import (
+    DispatchSpec,
+    TritonWarmupTensor,
+    triton_kernel_dispatcher_with_warmup,
+)
+from vllm.models.deepseek_v41.common.ops.fused_layout import Q_CHUNK
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -5,7 +5,7 @@
-leaving the fused KV insert only the zero-pad to the kernel's head count -- and
+leaving Q only the zero-pad to the kernel's head count -- and
@@ -282,7 +282,7 @@ def forward_mqa(
-        # q was zero-padded to the kernel's head count by the fused KV insert.
+        # _fused_qnorm_rope_kv_insert zero-padded q to the kernel's head count.
diff -- tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py
@@ -715,6 +715,62 @@ def run(q_in, is_q_interleaved):
+@pytest.mark.parametrize("num_tokens", [17, 1024, 2049])
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` modified +108/-1; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +2/-2
  - tests: `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +56/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64815 - [Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel

- Link: https://github.com/vllm-project/vllm/pull/64815
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`; associated commits `b5814faa25cf`
- Diff scope read: GitHub Pull Request files API returned 4 files, +42/-7, 129 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`; technical summary: Covers "[Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-1 (9 lines); hunks: -140,12 +140,19 @@ def can_fuse_query_quant(linears: list[torch.nn.Module]) -...; symbols: can_fuse_query_quant, touching `can_fuse_query_quant`; `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +3/-1 (4 lines); hunks: -10,6 +10,7; -38,7 +39,8 @@ def _can_fuse_wo_a(layer: nn.Module) -> bool:; symbols: _can_fuse_wo_a, touching `_can_fuse_wo_a`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-1 (9 lines); hunks: -140,12 +140,19 @@ def can_fuse_query_quant(linears: list[torch.nn.Module]) -...; symbols: can_fuse_query_quant
  - `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +3/-1 (4 lines); hunks: -10,6 +10,7; -38,7 +39,8 @@ def _can_fuse_wo_a(layer: nn.Module) -> bool:; symbols: _can_fuse_wo_a
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/query_quant.py
@@ -140,12 +140,19 @@ def can_fuse_query_quant(linears: list[torch.nn.Module]) -> bool:
+    from vllm.model_executor.kernels.linear.mxfp8.pytorch import (
+        TorchMxFp8LinearKernel,
+    )
-        in (FlashInferCutedslMxfp8LinearKernel, FlashInferCutlassMxfp8LinearKernel)
+        in (
+            FlashInferCutedslMxfp8LinearKernel,
diff -- vllm/models/deepseek_v41/nvidia/ops/o_proj.py
@@ -10,6 +10,7 @@
+from vllm.model_executor.kernels.linear.mxfp8.pytorch import TorchMxFp8LinearKernel
@@ -38,7 +39,8 @@ def _can_fuse_wo_a(layer: nn.Module) -> bool:
-            getattr(method, "kernel", None), FlashInferCutedslMxfp8LinearKernel
+            getattr(method, "kernel", None),
+            (FlashInferCutedslMxfp8LinearKernel, TorchMxFp8LinearKernel),
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-1; `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` modified +3/-1
- Risk and verification: The diff ships test coverage in `tests/fusion/test_quant_activation_contract.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63892 - [ROCm][Perf][DSv4.1] Mono: batch TP4 K2's X8 copies, load its push's peer bases late

- Link: https://github.com/vllm-project/vllm/pull/63892
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py`; associated commits `cc6977482034`
- Diff scope read: GitHub Pull Request files API returned 3 files, +36/-1, 95 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Mono: batch TP4 K2's X8 copies, load its push's peer bases late"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Mono: batch TP4 K2's X8 copies, load its push's peer bases late"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +14/-1 (15 lines); hunks: -1069,9 +1069,16 @@ def load_x8_rows(c, words_mb, codes_mb, xl, xsl, token_of...; -1085,6 +1092,9 @@ def load_x8_rows(c, words_mb, codes_mb, xl, xsl, token_of,...; symbols: load_x8_rows, stage_down, moe_context, touching `load_x8_rows, stage_down, moe_context`; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +2/-0 (2 lines); hunks: -631,6 +631,7 @@ def mark(point, core_clock=False):; -859,6 +860,7 @@ def push(t, col, v0, v1):; symbols: mark, push, touching `mark, push`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +14/-1 (15 lines); hunks: -1069,9 +1069,16 @@ def load_x8_rows(c, words_mb, codes_mb, xl, xsl, token_of...; -1085,6 +1092,9 @@ def load_x8_rows(c, words_mb, codes_mb, xl, xsl, token_of,...; symbols: load_x8_rows, stage_down, moe_context
  - `vllm/models/deepseek_v41/amd/mono/layer.py` modified +2/-0 (2 lines); hunks: -631,6 +631,7 @@ def mark(point, core_clock=False):; -859,6 +860,7 @@ def push(t, col, v0, v1):; symbols: mark, push
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono/stages/moe.py
@@ -1069,9 +1069,16 @@ def load_x8_rows(c, words_mb, codes_mb, xl, xsl, token_of, live):
+    got, x8all = [], c["push_bases"] and not GFX942 and isinstance(live, int)
-        for i in range_constexpr(-(-TILE * quads // THREADS)):
+        for i in range_constexpr(-(-live * quads // THREADS) if x8all else 0):
+            q = fx.Uint32(fx.min(tid + THREADS * i, live * quads - 1))
+            row = fx.Int32(q // quads)
+            r, off = rsrc(c[mb].value), token_of(row) * width + fx.Int32(q % quads) * 4
diff -- vllm/models/deepseek_v41/amd/mono/layer.py
@@ -631,6 +631,7 @@ def mark(point, core_clock=False):
+    cb["push_bases"] = a.get("push_bases") if tp == 4 else None
@@ -859,6 +860,7 @@ def push(t, col, v0, v1):
+            push_bases=lambda: [b + par for b in peer_bases(peers, tp)],
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +14/-1; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +2/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv41_mono_numerics.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64971 - [Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages

- Link: https://github.com/vllm-project/vllm/pull/64971
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`; associated commits `c215f1483524`
- Diff scope read: GitHub Pull Request files API returned 5 files, +150/-11, 224 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`; technical summary: Covers "[Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages"; the main implementation surface is `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0 (18 lines); hunks: -263,6 +263,24 @@ def test_unsupported_media_is_a_request_error():; symbols: test_unsupported_media_is_a_request_error, test_tool_references_render_as_tool_names, render_with_media, touching `test_unsupported_media_is_a_request_error, test_tool_references_render_as_tool_names, render_with_media`; `vllm/tokenizers/deepseek_v41.py` modified +7/-1 (8 lines); hunks: -29,7 +29,7 @@ def _normalize_messages(; -54,12 +54,18 @@ def _normalize_messages(; symbols: _normalize_messages, touching `_normalize_messages`.
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0 (18 lines); hunks: -263,6 +263,24 @@ def test_unsupported_media_is_a_request_error():; symbols: test_unsupported_media_is_a_request_error, test_tool_references_render_as_tool_names, render_with_media
  - `vllm/tokenizers/deepseek_v41.py` modified +7/-1 (8 lines); hunks: -29,7 +29,7 @@ def _normalize_messages(; -54,12 +54,18 @@ def _normalize_messages(; symbols: _normalize_messages
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -263,6 +263,24 @@ def test_unsupported_media_is_a_request_error():
+def test_tool_references_render_as_tool_names():
+    messages = [
+        {"role": "assistant", "tool_calls": [tool_call("tool_search")]},
+        {
+            "role": "tool",
+            "tool_call_id": "tool_search",
diff -- vllm/tokenizers/deepseek_v41.py
@@ -29,7 +29,7 @@ def _normalize_messages(
-    # and ValueError (400) instead of the reference's asserts.
+    # tool_reference, and ValueError (400) instead of the reference's asserts.
@@ -54,12 +54,18 @@ def _normalize_messages(
+                elif part_type == "tool_reference":
+                    # The system prompt already lists every tool, deferred
+                    # ones included, so the name is all the model needs.
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0
  - runtime: `vllm/tokenizers/deepseek_v41.py` modified +7/-1
- Risk and verification: The diff ships test coverage in `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/scale_out/render/test_render.py`, `tests/tokenizers_/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64816 - [Perf][DSv4.1] Vectorize first-layer HC expansion copy

- Link: https://github.com/vllm-project/vllm/pull/64816
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`; associated commits `ea836290a716`
- Diff scope read: GitHub Pull Request files API returned 3 files, +69/-1, 106 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Vectorize first-layer HC expansion copy"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Perf][DSv4.1] Vectorize first-layer HC expansion copy"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +33/-0 (33 lines); hunks: -19,6 +19,7; -320,3 +321,35 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre, _hc_expand_kernel, hc_expand, touching `mhc_shifted_post_pre, _hc_expand_kernel, hc_expand`; `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1 (3 lines); hunks: -110,6 +110,7; -527,7 +528,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +33/-0 (33 lines); hunks: -19,6 +19,7; -320,3 +321,35 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre, _hc_expand_kernel, hc_expand
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1 (3 lines); hunks: -110,6 +110,7; -527,7 +528,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/mhc.py
@@ -19,6 +19,7 @@
+from vllm.triton_utils import tl, triton
@@ -320,3 +321,35 @@ def mhc_shifted_post_pre(
+@triton.jit
+def _hc_expand_kernel(
+    x,
+    out,
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -110,6 +110,7 @@
+    hc_expand,
@@ -527,7 +528,7 @@ def forward(
-                residual = x.unsqueeze(1).expand(-1, self.hc_mult, -1).contiguous()
+                residual = hc_expand(x, self.hc_mult)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +33/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/mhc/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60543 - [Bugfix][DSv4.1] Autotune the sparse indexer's wq_b GEMM

- Link: https://github.com/vllm-project/vllm/pull/60543
- Status/date: merged / 2026-11-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/attention.py`; associated commits `72a340466f0b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +17/-0, 35 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Autotune the sparse indexer's wq_b GEMM"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/attention.py`; technical summary: Covers "[Bugfix][DSv4.1] Autotune the sparse indexer's wq_b GEMM"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` modified +15/-0 (15 lines); hunks: -1610,3 +1610,18 @@ def _wq_b_proj(; symbols: _wq_b_proj, autotune_indexer_wq_b, touching `_wq_b_proj, autotune_indexer_wq_b`.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` modified +15/-0 (15 lines); hunks: -1610,3 +1610,18 @@ def _wq_b_proj(; symbols: _wq_b_proj, autotune_indexer_wq_b
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -1610,3 +1610,18 @@ def _wq_b_proj(
+def autotune_indexer_wq_b(model: nn.Module, num_tokens: int) -> None:
+    """Short-context dummy runs skip wq_b, so tune it directly."""
+    for module in model.modules():
+        if isinstance(module, DeepseekV4Indexer):
+            # Run every wq_b: FlashInfer keys on op, runner, shapes and dtype,
+            # and skips profiling on a cache hit, so duplicates are cheap.
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` modified +15/-0
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/models/deepseek_v41/attention.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #63098 - [Feature][DSv4.1] Enable PCP with PP or DP

- Link: https://github.com/vllm-project/vllm/pull/63098
- Status/date: merged / 2026-10-31
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `2b009fc6d149`
- Diff scope read: GitHub Pull Request files API returned 2 files, +62/-8, 123 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature][DSv4.1] Enable PCP with PP or DP"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Feature][DSv4.1] Enable PCP with PP or DP"; the main implementation surface is `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_pcp.py` modified +50/-0 (50 lines); hunks: -1,5 +1,6; -13,6 +14,55; symbols: test_pcp_generates_with_pipeline_or_data_parallelism, touching `test_pcp_generates_with_pipeline_or_data_parallelism`; `vllm/models/deepseek_v41/nvidia/model.py` modified +12/-8 (20 lines); hunks: -264,8 +264,7 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; -707,14 +706,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: _use_sequence_parallel, __init__, forward, touching `_use_sequence_parallel, __init__, forward`.
- Code diff details:
  - `tests/models/test_deepseek_v41_pcp.py` modified +50/-0 (50 lines); hunks: -1,5 +1,6; -13,6 +14,55; symbols: test_pcp_generates_with_pipeline_or_data_parallelism
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +12/-8 (20 lines); hunks: -264,8 +264,7 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; -707,14 +706,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: _use_sequence_parallel, __init__, forward
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_pcp.py
@@ -1,5 +1,6 @@
+import os
@@ -13,6 +14,55 @@
+from vllm.platforms import current_platform
+@pytest.mark.distributed(num_gpus=8)
+@pytest.mark.skipif(
+    not current_platform.is_cuda() or current_platform.device_count() < 8,
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -264,8 +264,7 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:
-        parallel_config.pipeline_parallel_size == 1
-        and parallel_config.enable_expert_parallel
+        parallel_config.enable_expert_parallel
@@ -707,14 +706,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-            self.parallel_config.pipeline_parallel_size != 1
-            or self.parallel_config.data_parallel_size != 1
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_pcp.py` modified +50/-0
  - runtime: `vllm/models/deepseek_v41/nvidia/model.py` modified +12/-8
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_pcp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64094 - [ROCm][DSv4.1][Perf] Enable prefix-cache SWA replay on gfx950

- Link: https://github.com/vllm-project/vllm/pull/64094
- Status/date: merged / 2026-10-31
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/attention.py`; associated commits `138dfa54636c`
- Diff scope read: GitHub Pull Request files API returned 3 files, +120/-9, 148 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Enable prefix-cache SWA replay on gfx950"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/amd/model.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Enable prefix-cache SWA replay on gfx950"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/amd/model.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` modified +14/-8 (22 lines); hunks: -550,15 +550,21 @@ def __init__(; symbols: __init__, touching `__init__`; `vllm/models/deepseek_v41/amd/model.py` modified +3/-1 (4 lines); hunks: -575,7 +575,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, touching `__init__`; `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +103/-0 (103 lines); hunks: -883,3 +883,106 @@ def common_metadata(seq_lens):; symbols: common_metadata, _StubLinear, __init__, _prefix_replay_attention_cls, touching `common_metadata, _StubLinear, __init__`.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` modified +14/-8 (22 lines); hunks: -550,15 +550,21 @@ def __init__(; symbols: __init__
  - `vllm/models/deepseek_v41/amd/model.py` modified +3/-1 (4 lines); hunks: -575,7 +575,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
  - `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +103/-0 (103 lines); hunks: -883,3 +883,106 @@ def common_metadata(seq_lens):; symbols: common_metadata, _StubLinear, __init__, _prefix_replay_attention_cls
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -550,15 +550,21 @@ def __init__(
+        # CDNA4 (MI350/MI355, gfx950) is where prefix-cache SWA replay is
+        # validated. The AITER sparse-MLA path and the default Triton gather
+        # path both clamp to replay_start. CDNA3 and other ROCm archs have
+        # not been validated, so the sliding-window cache stays in the prefix
+        # cache there. The CDNA version is imported only on ROCm: loading the
+        # ROCm platform resolves the GPU arch and fails when no GPU is visible.
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -575,7 +575,9 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-        # Config flag is the switch: ROCm forces swa_cache_layer.bounded_replay off.
+        # Config flag is the switch. On ROCm, attention forces
+        # swa_cache_layer.bounded_replay off only when the CDNA version is
+        # not 4. CDNA4 keeps the window in bounded replay.
diff -- tests/v1/attention/test_deepseek_v4_swa_visible.py
@@ -883,3 +883,106 @@ def common_metadata(seq_lens):
+class _StubLinear(torch.nn.Module):
+    def __init__(self, *args, **kwargs):
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` modified +14/-8; `vllm/models/deepseek_v41/amd/model.py` modified +3/-1
  - tests: `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +103/-0
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_deepseek_v4_swa_visible.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61971 - [Perf][DSv4.1] Bump FlashMLA to pass int64 positions to MegaAttn

- Link: https://github.com/vllm-project/vllm/pull/61971
- Status/date: merged / 2026-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; associated commits `53624fc952d1`
- Diff scope read: GitHub Pull Request files API returned 3 files, +8/-11, 87 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Bump FlashMLA to pass int64 positions to MegaAttn"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; technical summary: Covers "[Perf][DSv4.1] Bump FlashMLA to pass int64 positions to MegaAttn"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +6/-8 (14 lines); hunks: -293,14 +293,12 @@ def forward_mqa(; -309,7 +307,7 @@ def forward_mqa(; symbols: forward_mqa, _decode_compressed_kv_and_topk, _forward_decode_mega, touching `forward_mqa, _decode_compressed_kv_and_topk, _forward_decode_mega`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +6/-8 (14 lines); hunks: -293,14 +293,12 @@ def forward_mqa(; -309,7 +307,7 @@ def forward_mqa(; symbols: forward_mqa, _decode_compressed_kv_and_topk, _forward_decode_mega
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -293,14 +293,12 @@ def forward_mqa(
-        # The kernel takes int32 RoPE positions.
-        positions_int32 = positions.to(torch.int32)
-                positions_int32[num_decode_tokens:],
+                positions[num_decode_tokens:],
@@ -309,7 +307,7 @@ def forward_mqa(
-                positions_int32[:num_decode_tokens],
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +6/-8
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #63885 - [ROCm][Perf][DSv4.1] Build the SWA decode metadata in one launch

- Link: https://github.com/vllm-project/vllm/pull/63885
- Status/date: merged / 2026-10-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`, `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `e49ea84e929e`
- Diff scope read: GitHub Pull Request files API returned 4 files, +85/-9, 163 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Build the SWA decode metadata in one launch"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`, `vllm/models/deepseek_v41/amd/rocm.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Build the SWA decode metadata in one launch"; the main implementation surface is `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`, `vllm/models/deepseek_v41/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/ops/__init__.py` modified +19/-3 (22 lines); hunks: -1,14 +1,16; -28,15 +30,29 @@ def record_monokernel(vllm_config) -> None:; symbols: record_monokernel, enabled, swa_decode_meta_enabled, touching `record_monokernel, enabled, swa_decode_meta_enabled`; `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py` modified +6/-5 (11 lines); hunks: -22,16 +22,17; -182,7 +183,7 @@ def build(builder, common_prefix_len, cam, fast_build, repla...; symbols: build, touching `build`; `vllm/models/deepseek_v41/amd/rocm.py` modified +1/-1 (2 lines); hunks: -380,7 +380,7 @@ def build(; symbols: build, touching `build`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/ops/__init__.py` modified +19/-3 (22 lines); hunks: -1,14 +1,16; -28,15 +30,29 @@ def record_monokernel(vllm_config) -> None:; symbols: record_monokernel, enabled, swa_decode_meta_enabled
  - `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py` modified +6/-5 (11 lines); hunks: -22,16 +22,17; -182,7 +183,7 @@ def build(builder, common_prefix_len, cam, fast_build, repla...; symbols: build
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +1/-1 (2 lines); hunks: -380,7 +380,7 @@ def build(; symbols: build
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/ops/__init__.py
@@ -1,14 +1,16 @@
-"""gfx942 (MI300X, MI325X) decode helpers for DeepSeek-V4.1.
+"""gfx942 (MI300X, MI325X) decode helpers for DeepSeek-V4.1. swa_decode_meta
+also runs on gfx950 (MI355X).
-wvSplitK. All of them run only when ``enabled()`` is true.
+wvSplitK. All of them run only when ``enabled()`` is true, except
+``swa_decode_meta``, which runs when ``swa_decode_meta_enabled()`` is true.
diff -- vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py
@@ -22,16 +22,17 @@
-On gfx942 with --monokernel (``ops.enabled()``), decode
-batches of up to MAX_ROWS rows, causal or the draft block, use it. Other
-batches take the rest of DeepseekV41ROCMAiterSparseSWAMetadataBuilder.build.
+On gfx942 and gfx950 with --monokernel
+(``ops.swa_decode_meta_enabled()``), decode batches of up to MAX_ROWS rows,
+causal or the draft block, use it. Other batches take the rest of
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -380,7 +380,7 @@ def build(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/ops/__init__.py` modified +19/-3; `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py` modified +6/-5; `vllm/models/deepseek_v41/amd/rocm.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv41_mono_decode.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #64101 - [ROCm][Perf][DSv4.1] Mono decode at TP8 on MI355X

- Link: https://github.com/vllm-project/vllm/pull/64101
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/mono/README.md`, `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/attention/plan.py`, `vllm/models/deepseek_v41/amd/mono/stages/gemv.py`, `vllm/models/deepseek_v41/amd/mono_decode.py`; associated commits `f97a8d664796`
- Diff scope read: GitHub Pull Request files API returned 8 files, +72/-23, 188 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Mono decode at TP8 on MI355X"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/stages/gemv.py`, `vllm/models/deepseek_v41/amd/mono/attention/plan.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Mono decode at TP8 on MI355X"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/stages/gemv.py`, `vllm/models/deepseek_v41/amd/mono/attention/plan.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +20/-11 (31 lines); hunks: -370,7 +370,7 @@ def stage_split(c, unit):; -489,13 +489,22 @@ def stage_split(c, unit):; symbols: stage_split, store_part, back_lds_members, SplitLds, touching `stage_split, store_part, back_lds_members`; `vllm/models/deepseek_v41/amd/mono/stages/gemv.py` modified +12/-4 (16 lines); hunks: -96,18 +96,26 @@ def _fp8_step_load(c, r_w, r_ws, k, rg, st, row_major=False):; symbols: _fp8_step_load, touching `_fp8_step_load`; `vllm/models/deepseek_v41/amd/mono/attention/plan.py` modified +11/-2 (13 lines); hunks: -57,15 +57,24 @@ class Dims:; symbols: Dims, __post_init__, heads, head_tiles, touching `Dims, __post_init__, heads`; `vllm/models/deepseek_v41/amd/mono_decode.py` modified +2/-2 (4 lines); hunks: -354,8 +354,8 @@ def _create(; symbols: _create, touching `_create`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +20/-11 (31 lines); hunks: -370,7 +370,7 @@ def stage_split(c, unit):; -489,13 +489,22 @@ def stage_split(c, unit):; symbols: stage_split, store_part, back_lds_members, SplitLds
  - `vllm/models/deepseek_v41/amd/mono/stages/gemv.py` modified +12/-4 (16 lines); hunks: -96,18 +96,26 @@ def _fp8_step_load(c, r_w, r_ws, k, rg, st, row_major=False):; symbols: _fp8_step_load
  - `vllm/models/deepseek_v41/amd/mono/attention/plan.py` modified +11/-2 (13 lines); hunks: -57,15 +57,24 @@ class Dims:; symbols: Dims, __post_init__, heads, head_tiles
  - `vllm/models/deepseek_v41/amd/mono_decode.py` modified +2/-2 (4 lines); hunks: -354,8 +354,8 @@ def _create(; symbols: _create
  - `vllm/models/deepseek_v41/amd/mono/README.md` modified +1/-1 (2 lines); hunks: -25,7 +25,7 @@ new, reading vLLM's KV records and weights as loaded.
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono/attention/back.py
@@ -370,7 +370,7 @@ def stage_split(c, unit):
-        lst = st + d.heads * nkt
+        lst = st + d.heads_pad * nkt
@@ -489,13 +489,22 @@ def stage_split(c, unit):
-            for hlf in range_constexpr(2):
-                bo.buffer_store(
-                    fx.Vector.from_elements(words[4 * hlf : 4 * hlf + 4], fx.Int32),
diff -- vllm/models/deepseek_v41/amd/mono/stages/gemv.py
@@ -96,18 +96,26 @@ def _fp8_step_load(c, r_w, r_ws, k, rg, st, row_major=False):
-    layout, k % 64 == 0): the same registers from a row-major [N, K] weight --
-    lane l row 16 rg + l % 16, K bytes 128 st + 16 (l // 16) .. and + 64."""
+    layout, k % 32 == 0): the same registers from a row-major [N, K] weight --
+    lane l row 16 rg + l % 16, K bytes 128 st + 16 (l // 16) .. and + 64; with
+    k % 64 == 32 (TP8's shared expert, K = 288) the last step's upper lanes are
+    clamped into the row, as in the shuffled layout."""
diff -- vllm/models/deepseek_v41/amd/mono/attention/plan.py
@@ -57,15 +57,24 @@ class Dims:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +20/-11; `vllm/models/deepseek_v41/amd/mono/stages/gemv.py` modified +12/-4; `vllm/models/deepseek_v41/amd/mono/attention/plan.py` modified +11/-2; `vllm/models/deepseek_v41/amd/mono_decode.py` modified +2/-2; `vllm/models/deepseek_v41/amd/mono/README.md` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv41_mono_layers.py`, `tests/models/test_dsv41_mono_numerics.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63816 - [Bugfix][ROCm][DSv4.1] Guard NaN scores in gfx942 mono routing

- Link: https://github.com/vllm-project/vllm/pull/63816
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/mono/stages/moe.py`; associated commits `e18e2c70c5cd`
- Diff scope read: GitHub Pull Request files API returned 2 files, +109/-2, 135 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm][DSv4.1] Guard NaN scores in gfx942 mono routing"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/amd/mono/stages/moe.py`; technical summary: Covers "[Bugfix][ROCm][DSv4.1] Guard NaN scores in gfx942 mono routing"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono/stages/moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +4/-2 (6 lines); hunks: -427,13 +427,15 @@ def stage_route(c, t):; -453,7 +455,7 @@ def stage_route(c, t):; symbols: stage_route, touching `stage_route`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +4/-2 (6 lines); hunks: -427,13 +427,15 @@ def stage_route(c, t):; -453,7 +455,7 @@ def stage_route(c, t):; symbols: stage_route
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono/stages/moe.py
@@ -427,13 +427,15 @@ def stage_route(c, t):
+        neg = fx.Float32(float("-inf"))
-            vals.append(fx.max(sc + ld_f32(a["bias"], e), fx.Float32(float("-inf"))))
+            val = fx.max(sc + ld_f32(a["bias"], e), neg)
+            vals.append(fx.isnan(val).select(neg, val))
@@ -453,7 +455,7 @@ def stage_route(c, t):
-            ball = ballot(cv == best)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +4/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/models/amd/test_dsv41_mono_gfx942.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62359 - [Perf][DSv4.1] Share Engram host tables as host-NUMA cuMem across DP ranks

- Link: https://github.com/vllm-project/vllm/pull/62359
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py`; associated commits `4e0ad5720361`
- Diff scope read: GitHub Pull Request files API returned 6 files, +418/-68, 646 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Share Engram host tables as host-NUMA cuMem across DP ranks"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/config/engram.py`; technical summary: Covers "[Perf][DSv4.1] Share Engram host tables as host-NUMA cuMem across DP ranks"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/config/engram.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py` added +241/-0 (241 lines); hunks: -0,0 +1,241; symbols: ExportedHostTable, _chunk_ranges, _call_driver, _gpu_numa_node, touching `ExportedHostTable, _chunk_ranges, _call_driver`; `vllm/models/deepseek_v41/common/engram.py` modified +119/-42 (161 lines); hunks: -37,6 +37,7; -75,6 +76,7; symbols: gather_engram_hashes, describe_error, gather_errors, _shm_shortfall, touching `gather_engram_hashes, describe_error, gather_errors`; `vllm/config/engram.py` modified +5/-4 (9 lines); hunks: -44,10 +44,11 @@ class EngramConfig:; symbols: EngramConfig, touching `EngramConfig`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py` added +241/-0 (241 lines); hunks: -0,0 +1,241; symbols: ExportedHostTable, _chunk_ranges, _call_driver, _gpu_numa_node
  - `vllm/models/deepseek_v41/common/engram.py` modified +119/-42 (161 lines); hunks: -37,6 +37,7; -75,6 +76,7; symbols: gather_engram_hashes, describe_error, gather_errors, _shm_shortfall
  - `vllm/config/engram.py` modified +5/-4 (9 lines); hunks: -44,10 +44,11 @@ class EngramConfig:; symbols: EngramConfig
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py
@@ -0,0 +1,241 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Engram host tables in host-NUMA cuMem, shared across DP ranks by FABRIC handle.
+GPUs map cuMem host memory with 2M pages instead of the 64K pages of a registered
+/dev/shm mapping, so random row lookups miss the TLB far less.
+"""
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -37,6 +37,7 @@
+import platform
@@ -75,6 +76,7 @@
+from vllm.utils.cpu_resource_utils import get_available_memory
@@ -778,46 +780,132 @@ def gather_engram_hashes(
+def describe_error(exc: Exception) -> str:
+    return f"{type(exc).__name__}: {exc}"
diff -- vllm/config/engram.py
@@ -44,10 +44,11 @@ class EngramConfig:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/engram_host_table.py` added +241/-0; `vllm/models/deepseek_v41/common/engram.py` modified +119/-42; `vllm/config/engram.py` modified +5/-4
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62009 - [Perf][EPLB][DSv4] Add a symm_mem weight-migration backend and fuse MegaMoE replica mapping

- Link: https://github.com/vllm-project/vllm/pull/62009
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`; associated commits `b2f46e785fe1`
- Diff scope read: GitHub Pull Request files API returned 17 files, +811/-212, 1675 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][EPLB][DSv4] Add a symm_mem weight-migration backend and fuse MegaMoE replica mapping"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_replay_batch.py`; technical summary: Covers "[Perf][EPLB][DSv4] Add a symm_mem weight-migration backend and fuse MegaMoE replica mapping"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_replay_batch.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +16/-4 (20 lines); hunks: -234,9 +234,9 @@ def __init__(; -246,6 +246,9 @@ def __init__(; symbols: __init__, _prepare_replay_batch, touching `__init__, _prepare_replay_batch`; `tests/models/test_deepseek_v41_replay_batch.py` modified +7/-2 (9 lines); hunks: -178,15 +178,15 @@ def test_replay_batch_keeps_each_request_window(state):; -457,6 +457,7 @@ def test_idle_dp_rank_dummy_trims_with_its_peers(dp_state):; symbols: test_replay_batch_keeps_each_request_window, test_replay_context_restores_tp_routing_rows, test_idle_dp_rank_dummy_trims_with_its_peers, test_zero_prefix_window_warms_gather_and_skips_pad, touching `test_replay_batch_keeps_each_request_window, test_replay_context_restores_tp_routing_rows, test_idle_dp_rank_dummy_trims_with_its_peers`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +16/-4 (20 lines); hunks: -234,9 +234,9 @@ def __init__(; -246,6 +246,9 @@ def __init__(; symbols: __init__, _prepare_replay_batch
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +7/-2 (9 lines); hunks: -178,15 +178,15 @@ def test_replay_batch_keeps_each_request_window(state):; -457,6 +457,7 @@ def test_idle_dp_rank_dummy_trims_with_its_peers(dp_state):; symbols: test_replay_batch_keeps_each_request_window, test_replay_context_restores_tp_routing_rows, test_idle_dp_rank_dummy_trims_with_its_peers, test_zero_prefix_window_warms_gather_and_skips_pad
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -234,9 +234,9 @@ def __init__(
-            # positions, slot mappings (sized with the KV cache groups on first
-            # use) and the position from which each request holds replay-layer
-            # window KV.
+            # positions, MoE padding mask, slot mappings (sized with the KV cache
+            # groups on first use) and the position from which each request holds
+            # replay-layer window KV.
diff -- tests/models/test_deepseek_v41_replay_batch.py
@@ -178,15 +178,15 @@ def test_replay_batch_keeps_each_request_window(state):
-    assert context.dp_metadata is None and context.is_padding is None
+    assert context.dp_metadata is None and not context.is_padding.any()
-    assert context.is_padding is None and context.dp_metadata is None
+    assert context.dp_metadata is None
@@ -457,6 +457,7 @@ def test_idle_dp_rank_dummy_trims_with_its_peers(dp_state):
+    assert replay.forward_context.is_padding.tolist() == [True]
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +16/-4
  - tests: `tests/models/test_deepseek_v41_replay_batch.py` modified +7/-2
- Risk and verification: The diff ships test coverage in `tests/distributed/test_eplb_execute.py`, `tests/distributed/test_eplb_migration_scheduler.py`, `tests/distributed/test_eplb_utils.py`, `tests/kernels/moe/test_deep_gemm_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59131 - [Perf][DSv4.1] Gather the compressed KV once per KV-source group in prefill

- Link: https://github.com/vllm-project/vllm/pull/59131
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; associated commits `98fc6da9d735`
- Diff scope read: GitHub Pull Request files API returned 4 files, +155/-23, 261 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Gather the compressed KV once per KV-source group in prefill"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; technical summary: Covers "[Perf][DSv4.1] Gather the compressed KV once per KV-source group in prefill"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +40/-19 (59 lines); hunks: -324,9 +324,18 @@ def _reserve_prefill_workspace(self, q: torch.Tensor) -> None:; -424,27 +433,39 @@ def _forward_prefill_mega(; symbols: _reserve_prefill_workspace, _prefill_index_workspace_specs, _forward_prefill_mega, touching `_reserve_prefill_workspace, _prefill_index_workspace_specs, _forward_prefill_mega`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +40/-19 (59 lines); hunks: -324,9 +324,18 @@ def _reserve_prefill_workspace(self, q: torch.Tensor) -> None:; -424,27 +433,39 @@ def _forward_prefill_mega(; symbols: _reserve_prefill_workspace, _prefill_index_workspace_specs, _forward_prefill_mega
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -324,9 +324,18 @@ def _reserve_prefill_workspace(self, q: torch.Tensor) -> None:
-        combined_topk = round_up(top_k + self.window_size, 128)
+        # One request covers the KV chunk (retained at the tail at runtime) and
+        # the index scratch (taken from the head) side by side.
+            *self._prefill_index_workspace_specs(top_k),
+        )
+    def _prefill_index_workspace_specs(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +40/-19
- Risk and verification: The diff ships test coverage in `tests/v1/worker/test_workspace.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58780 - [Bugfix][Parser] Stream DeepSeek V4/V3.2 string tool arguments incrementally

- Link: https://github.com/vllm-project/vllm/pull/58780
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py`, `vllm/parser/deepseek_v4.py`, `vllm/parser/deepseek_v41.py`; associated commits `974927f80416`
- Diff scope read: GitHub Pull Request files API returned 7 files, +295/-4, 411 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Parser] Stream DeepSeek V4/V3.2 string tool arguments incrementally"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/parser/deepseek_v4.py`, `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py`; technical summary: Covers "[Bugfix][Parser] Stream DeepSeek V4/V3.2 string tool arguments incrementally"; the main implementation surface is `vllm/parser/deepseek_v4.py`, `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/parser/deepseek_v4.py` modified +68/-4 (72 lines); hunks: -28,6 +28,7; -64,24 +65,46 @@ def _param_patterns(; symbols: _param_patterns, _match_open_param, _dsml_arg_converter, touching `_param_patterns, _match_open_param, _dsml_arg_converter`; `tests/parser/engine/test_deepseek_v4.py` modified +50/-0 (50 lines); hunks: -33,6 +33,7; -1302,6 +1303,55 @@ def test_eos_not_leaked_when_reasoning_never_ends(self, c...; symbols: test_eos_not_leaked_when_reasoning_never_ends, TestArgValueExtender, test_stops_at_split_param_close, test_no_extender_unless_open_string_value, touching `test_eos_not_leaked_when_reasoning_never_ends, TestArgValueExtender, test_stops_at_split_param_close`; `tests/parser/engine/test_deepseek_v41.py` modified +49/-0 (49 lines); hunks: -148,3 +148,52 @@ def test_python_argument_conversion_and_partial_values():; symbols: test_python_argument_conversion_and_partial_values, test_partial_tag_after_gt_is_held_back, test_long_string_argument_streams_before_close, touching `test_python_argument_conversion_and_partial_values, test_partial_tag_after_gt_is_held_back, test_long_string_argument_streams_before_close`; `vllm/parser/deepseek_v41.py` modified +9/-0 (9 lines); hunks: -8,6 +8,7; -46,6 +47,14 @@ def deepseek_v41_config(thinking: bool = False) -> ParserEngi...; symbols: deepseek_v41_config, touching `deepseek_v41_config`.
- Code diff details:
  - `vllm/parser/deepseek_v4.py` modified +68/-4 (72 lines); hunks: -28,6 +28,7; -64,24 +65,46 @@ def _param_patterns(; symbols: _param_patterns, _match_open_param, _dsml_arg_converter
  - `tests/parser/engine/test_deepseek_v4.py` modified +50/-0 (50 lines); hunks: -33,6 +33,7; -1302,6 +1303,55 @@ def test_eos_not_leaked_when_reasoning_never_ends(self, c...; symbols: test_eos_not_leaked_when_reasoning_never_ends, TestArgValueExtender, test_stops_at_split_param_close, test_no_extender_unless_open_string_value
  - `tests/parser/engine/test_deepseek_v41.py` modified +49/-0 (49 lines); hunks: -148,3 +148,52 @@ def test_python_argument_conversion_and_partial_values():; symbols: test_python_argument_conversion_and_partial_values, test_partial_tag_after_gt_is_held_back, test_long_string_argument_streams_before_close
  - `vllm/parser/deepseek_v41.py` modified +9/-0 (9 lines); hunks: -8,6 +8,7; -46,6 +47,14 @@ def deepseek_v41_config(thinking: bool = False) -> ParserEngi...; symbols: deepseek_v41_config
- Key code excerpts:

```diff
diff -- vllm/parser/deepseek_v4.py
@@ -28,6 +28,7 @@
+    ArgValueExtender,
@@ -64,24 +65,46 @@ def _param_patterns(
+    The trailing-partial regex captures the open value up to the end of the
+    text; ``_match_open_param`` holds back an unfinished next parameter tag
+    so a streamed string value never includes it.
-        re.compile(rf"{head}(.*)$", re.DOTALL),
diff -- tests/parser/engine/test_deepseek_v4.py
@@ -33,6 +33,7 @@
+    _dsml_arg_value_extender,
@@ -1302,6 +1303,55 @@ def test_eos_not_leaked_when_reasoning_never_ends(self, chunk_size):
+# ── Open string values stream without re-running the converter (#52846) ──
+class TestArgValueExtender:
+    def test_stops_at_split_param_close(self):
+        extend = _dsml_arg_value_extender(
diff -- tests/parser/engine/test_deepseek_v41.py
@@ -148,3 +148,52 @@ def test_python_argument_conversion_and_partial_values():
```

- Reviewed files:
  - runtime: `vllm/parser/deepseek_v4.py` modified +68/-4; `vllm/parser/deepseek_v41.py` modified +9/-0
  - tests: `tests/parser/engine/test_deepseek_v4.py` modified +50/-0; `tests/parser/engine/test_deepseek_v41.py` modified +49/-0
- Risk and verification: The diff ships test coverage in `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py`, `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63047 - [Bugfix][DSv4.1] Budget prefill memory the startup profile misses

- Link: https://github.com/vllm-project/vllm/pull/63047
- Status/date: merged / 2026-10-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `7ab756940a89`
- Diff scope read: GitHub Pull Request files API returned 6 files, +69/-34, 207 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Budget prefill memory the startup profile misses"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; technical summary: Covers "[Bugfix][DSv4.1] Budget prefill memory the startup profile misses"; the main implementation surface is `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/model.py` modified +5/-6 (11 lines); hunks: -11,7 +11,6; -706,9 +705,8 @@ def forward(; symbols: forward, touching `forward`; `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-5 (11 lines); hunks: -13,7 +13,6; -583,6 +582,7 @@ def forward(; symbols: forward, touching `forward`; `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +26/-0 (26 lines); hunks: -668,3 +668,29 @@ def test_indexer_prefill_budget_matches_compressed_workspac...; symbols: test_indexer_prefill_budget_matches_compressed_workspace, test_indexer_expanded_block_table_sized_by_decode_tokens, touching `test_indexer_prefill_budget_matches_compressed_workspace, test_indexer_expanded_block_table_sized_by_decode_tokens`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/model.py` modified +5/-6 (11 lines); hunks: -11,7 +11,6; -706,9 +705,8 @@ def forward(; symbols: forward
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-5 (11 lines); hunks: -13,7 +13,6; -583,6 +582,7 @@ def forward(; symbols: forward
  - `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +26/-0 (26 lines); hunks: -668,3 +668,29 @@ def test_indexer_prefill_budget_matches_compressed_workspac...; symbols: test_indexer_prefill_budget_matches_compressed_workspace, test_indexer_expanded_block_table_sized_by_decode_tokens
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -11,7 +11,6 @@
-    get_engram_dp_size,
@@ -706,9 +705,8 @@ def forward(
-        # and consumed by the engram layers (1 and 14) below. Skipped on
-        # profile runs (KV cache unbound -> no slot space to key the rolling
-        # compressed-id cache into).
+        # and consumed by the engram layers (1 and 14) below. Profile runs
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -13,7 +13,6 @@
-    get_engram_dp_size,
@@ -583,6 +582,7 @@ def forward(
+            del previous_post
@@ -1000,8 +1000,8 @@ def forward(
-        # and consumed by the engram layers (1 and 14) below. Skipped on
-        # profile runs (KV cache unbound).
diff -- tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py
@@ -668,3 +668,29 @@ def test_indexer_prefill_budget_matches_compressed_workspace(compress_ratio):
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/model.py` modified +5/-6; `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-5
  - tests: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +26/-0
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63914 - [Bugfix][DSv4.1] Keep the specialized decode's FlashInfer paths on newer FlashInfer

- Link: https://github.com/vllm-project/vllm/pull/63914
- Status/date: merged / 2026-10-28
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md`, `vllm/models/deepseek_v41/nvidia/specialized_decode/__init__.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/mxfp8.py` and 6 files; associated commits `ed6b8f4cd2b4`
- Diff scope read: GitHub Pull Request files API returned 6 files, +71/-40, 228 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Keep the specialized decode's FlashInfer paths on newer FlashInfer"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py`; technical summary: Covers "[Bugfix][DSv4.1] Keep the specialized decode's FlashInfer paths on newer FlashInfer"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla.py` modified +31/-4 (35 lines); hunks: -18,19 +18,23; -41,17 +45,40; symbols: _takes_kv_counters, kv_counter_buffer, touching `_takes_kv_counters, kv_counter_buffer`; `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md` modified +14/-8 (22 lines); hunks: -36,22 +36,28 @@ collectives and would hang. Which forward steps use the exec...; `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` modified +9/-11 (20 lines); hunks: -18,13 +18,12; -809,14 +808,13 @@ def run(replays: int) -> str | None:; symbols: run, test_specialized_decode_numerics, touching `run, test_specialized_decode_numerics`; `vllm/models/deepseek_v41/nvidia/specialized_decode/__init__.py` modified +11/-9 (20 lines); hunks: -16,6 +16,7; -37,10 +38,11; symbols: DecodeConfig, uses_checked_flashinfer, touching `DecodeConfig, uses_checked_flashinfer`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla.py` modified +31/-4 (35 lines); hunks: -18,19 +18,23; -41,17 +45,40; symbols: _takes_kv_counters, kv_counter_buffer
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md` modified +14/-8 (22 lines); hunks: -36,22 +36,28 @@ collectives and would hang. Which forward steps use the exec...
  - `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` modified +9/-11 (20 lines); hunks: -18,13 +18,12; -809,14 +808,13 @@ def run(replays: int) -> str | None:; symbols: run, test_specialized_decode_numerics
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/__init__.py` modified +11/-9 (20 lines); hunks: -16,6 +16,7; -37,10 +38,11; symbols: DecodeConfig, uses_checked_flashinfer
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/mxfp8.py` modified +5/-7 (12 lines); hunks: -33,7 +33,7; -134,12 +134,10 @@ def run_zeros(linear: nn.Module, rows: int) -> torch.Tensor:; symbols: run_zeros, pinned_tactics
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla.py
@@ -18,19 +18,23 @@
+import inspect
+from functools import cache
+from vllm.logger import init_logger
-from .. import uses_checked_flashinfer
+logger = init_logger(__name__)
@@ -41,17 +45,40 @@
diff -- vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md
@@ -36,22 +36,28 @@ collectives and would hang. Which forward steps use the executor depends
-Four features run only on flashinfer-python 0.7.2 (`FLASHINFER_VERSION`, the
-version `requirements/cuda.txt` pins). Three use FlashInfer internals:
+Two features use FlashInfer internals and run on flashinfer-python 0.7.2 or
+newer (`MIN_FLASHINFER_VERSION`):
-  `flashinfer.cute_dsl.fp4_common`);
-- the pinned MXFP8 GEMM tactics: the low-latency GEMM's `autotune_tactics`.
diff -- tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py
@@ -18,13 +18,12 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/sparse_mla.py` modified +31/-4; `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md` modified +14/-8; `vllm/models/deepseek_v41/nvidia/specialized_decode/__init__.py` modified +11/-9; `vllm/models/deepseek_v41/nvidia/specialized_decode/attention/mxfp8.py` modified +5/-7
  - tests: `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` modified +9/-11; `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63018 - [Perf][DSv4.1] Tile the NVFP4 compressed-KV dequant-gather

- Link: https://github.com/vllm-project/vllm/pull/63018
- Status/date: merged / 2026-10-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/ops/cache_utils.py`; associated commits `6abdff59301f`
- Diff scope read: GitHub Pull Request files API returned 2 files, +205/-27, 288 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Tile the NVFP4 compressed-KV dequant-gather"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/ops/cache_utils.py`; technical summary: Covers "[Perf][DSv4.1] Tile the NVFP4 compressed-KV dequant-gather"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/cache_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +53/-27 (80 lines); hunks: -602,8 +602,12 @@ def _dequantize_and_gather_k_nvfp4_kernel(; -616,35 +620,52 @@ def _dequantize_and_gather_k_nvfp4_kernel(; symbols: _dequantize_and_gather_k_nvfp4_kernel, gather_num_workers, dequantize_and_gather_k_cache_triton, touching `_dequantize_and_gather_k_nvfp4_kernel, gather_num_workers, dequantize_and_gather_k_cache_triton`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +53/-27 (80 lines); hunks: -602,8 +602,12 @@ def _dequantize_and_gather_k_nvfp4_kernel(; -616,35 +620,52 @@ def _dequantize_and_gather_k_nvfp4_kernel(; symbols: _dequantize_and_gather_k_nvfp4_kernel, gather_num_workers, dequantize_and_gather_k_cache_triton
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -602,8 +602,12 @@ def _dequantize_and_gather_k_nvfp4_kernel(
+    TILE: tl.constexpr,  # tokens per iteration
-    """Gather and dequantize V4.1 NVFP4 rows into a bf16 workspace."""
+    """Gather and dequantize V4.1 NVFP4 rows into a bf16 workspace, TILE tokens
+    per iteration. A nibble placed as fp16 bits (sign at 15, exponent and
+    mantissa at 11:9) reads as e2m1 * 2^-14; times scale * 2^14 the fp32 product
+    is exact, so the bf16 result matches a direct decode."""
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +53/-27
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63155 - [Perf][DSv4.1] Capture the decoder replay graphs on the model graphs' stream

- Link: https://github.com/vllm-project/vllm/pull/63155
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `vllm/models/deepseek_v41/nvidia/model.py` and 7 files; associated commits `274a5e19a184`
- Diff scope read: GitHub Pull Request files API returned 13 files, +72/-17, 292 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Capture the decoder replay graphs on the model graphs' stream"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`; technical summary: Covers "[Perf][DSv4.1] Capture the decoder replay graphs on the model graphs' stream"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` modified +15/-3 (18 lines); hunks: -68,9 +68,21 @@ def __init__(self, vllm_config: VllmConfig, device, layers: D...; -86,7 +98,7 @@ def forward_fn(cg_mode: CUDAGraphMode) -> None:; symbols: __init__, capture_replay_graphs, create_forward_fn, forward_fn, touching `__init__, capture_replay_graphs, create_forward_fn`; `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +12/-2 (14 lines); hunks: -2,13 +2,15; -158,8 +160,16 @@ def test_replay_graph_matches_eager(monkeypatch, moe_backen...; symbols: test_replay_graph_matches_eager, fake_graph_capture, touching `test_replay_graph_matches_eager, fake_graph_capture`; `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +4/-0 (4 lines); hunks: -46,6 +46,8 @@ class DecoderReplayLayers:; -55,12 +57,14 @@ def __init__(; symbols: DecoderReplayLayers, __init__, touching `DecoderReplayLayers, __init__`; `vllm/models/deepseek_v41/nvidia/model_state.py` modified +2/-1 (3 lines); hunks: -635,6 +635,7 @@ def capture_inner_cudagraphs(; -654,7 +655,7 @@ def prepare(desc: BatchExecutionDescriptor) -> None:; symbols: capture_inner_cudagraphs, prepare, _kept_input_batch, touching `capture_inner_cudagraphs, prepare, _kept_input_batch`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` modified +15/-3 (18 lines); hunks: -68,9 +68,21 @@ def __init__(self, vllm_config: VllmConfig, device, layers: D...; -86,7 +98,7 @@ def forward_fn(cg_mode: CUDAGraphMode) -> None:; symbols: __init__, capture_replay_graphs, create_forward_fn, forward_fn
  - `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +12/-2 (14 lines); hunks: -2,13 +2,15; -158,8 +160,16 @@ def test_replay_graph_matches_eager(monkeypatch, moe_backen...; symbols: test_replay_graph_matches_eager, fake_graph_capture
  - `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +4/-0 (4 lines); hunks: -46,6 +46,8 @@ class DecoderReplayLayers:; -55,12 +57,14 @@ def __init__(; symbols: DecoderReplayLayers, __init__
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +2/-1 (3 lines); hunks: -635,6 +635,7 @@ def capture_inner_cudagraphs(; -654,7 +655,7 @@ def prepare(desc: BatchExecutionDescriptor) -> None:; symbols: capture_inner_cudagraphs, prepare, _kept_input_batch
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/runtime/model_state.py` modified +2/-1 (3 lines); hunks: -154,6 +154,7 @@ def capture_inner_cudagraphs(; -173,5 +174,5 @@ def capture_inner_cudagraphs(; symbols: capture_inner_cudagraphs
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py
@@ -68,9 +68,21 @@ def __init__(self, vllm_config: VllmConfig, device, layers: DecoderReplayLayers)
-        self, prepare: Callable[[BatchExecutionDescriptor], None]
+        self,
+        prepare: Callable[[BatchExecutionDescriptor], None],
+        stream: torch.cuda.Stream | None = None,
-        """Capture each size on the replay batch ``prepare`` sets on the layers."""
+        """Capture each size on the replay batch ``prepare`` sets on the layers.
diff -- tests/models/test_deepseek_v41_decoder_replay_layers.py
@@ -2,13 +2,15 @@
+from contextlib import contextmanager
+from vllm.distributed.parallel_state import GraphCaptureContext
@@ -158,8 +160,16 @@ def test_replay_graph_matches_eager(monkeypatch, moe_backend, ids_dtype):
-    capture = torch.cuda.stream(torch.cuda.Stream())
-    monkeypatch.setattr(cudagraph_utils, "graph_capture", lambda device: capture)
+    @contextmanager
diff -- vllm/models/deepseek_v41/decoder_replay_layers.py
@@ -46,6 +46,8 @@ class DecoderReplayLayers:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` modified +15/-3; `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +4/-0; `vllm/models/deepseek_v41/nvidia/model_state.py` modified +2/-1; `vllm/models/deepseek_v41/nvidia/specialized_decode/runtime/model_state.py` modified +2/-1; `vllm/models/deepseek_v41/amd/model.py` modified +1/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +1/-0
  - tests: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +12/-2
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/v1/cudagraph/test_breakable_cudagraph.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62011 - [Perf] Enable DeepGEMM sparse MQA logits on the FP8 indexer cache, DSv4.1

- Link: https://github.com/vllm-project/vllm/pull/62011
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/attention.py`; associated commits `a2ad4b74b9f7`
- Diff scope read: GitHub Pull Request files API returned 8 files, +210/-98, 590 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Enable DeepGEMM sparse MQA logits on the FP8 indexer cache, DSv4.1"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/attention.py`, `vllm/config/attention.py`; technical summary: Covers "[Perf] Enable DeepGEMM sparse MQA logits on the FP8 indexer cache, DSv4.1"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`, `vllm/config/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` modified +11/-5 (16 lines); hunks: -1434,10 +1434,12 @@ def __init__(; -1468,9 +1470,13 @@ def __init__(; symbols: __init__, _produce_k, touching `__init__, _produce_k`; `vllm/config/attention.py` modified +9/-7 (16 lines); hunks: -97,17 +97,19 @@ class AttentionConfig:; symbols: AttentionConfig, GPU, touching `AttentionConfig, GPU`.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` modified +11/-5 (16 lines); hunks: -1434,10 +1434,12 @@ def __init__(; -1468,9 +1470,13 @@ def __init__(; symbols: __init__, _produce_k
  - `vllm/config/attention.py` modified +9/-7 (16 lines); hunks: -97,17 +97,19 @@ class AttentionConfig:; symbols: AttentionConfig, GPU
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -1434,10 +1434,12 @@ def __init__(
-            if not self.use_fp4_kv:
+            # DeepGEMM's sparse kernels (SM100) take either indexer cache;
+            # aiter's ROCm path is MXFP4-only.
+            if current_platform.is_rocm() and not self.use_fp4_kv:
-                    "attention_config.indexer_sparse_logits requires the MXFP4 "
-                    "indexer cache (attention_config.indexer_kv_dtype='mxfp4')."
diff -- vllm/config/attention.py
@@ -97,17 +97,19 @@ class AttentionConfig:
-    indexer_sparse_logits: bool = False
+    indexer_sparse_logits: bool | None = None
-    the whole context and masking them. Requires `indexer_kv_dtype="mxfp4"`,
-    an SM100-class GPU, DeepGEMM >= 2.8 and the DeepSelect top-k extension
-    (the top-k runs on the kernels' bf16 logits). The sparse path costs
-    O(candidate blocks) per query regardless of context length, so it pays off
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` modified +11/-5; `vllm/config/attention.py` modified +9/-7
- Risk and verification: The diff ships test coverage in `tests/model_executor/layers/test_mla_short_prefill_indexer.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #52970 - [ROCm][aiter] officially supporting aiter Triton kernels+dsv4 on RDNA3

- Link: https://github.com/vllm-project/vllm/pull/52970
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `eaf1627c01f5`
- Diff scope read: GitHub Pull Request files API returned 8 files, +45/-33, 230 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][aiter] officially supporting aiter Triton kernels+dsv4 on RDNA3"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/platforms/rocm.py`; technical summary: Covers "[ROCm][aiter] officially supporting aiter Triton kernels+dsv4 on RDNA3"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/platforms/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +2/-2 (4 lines); hunks: -35,7 +35,7; -1489,7 +1489,7 @@ def forward_mqa(; symbols: forward_mqa, touching `forward_mqa`; `vllm/platforms/rocm.py` modified +5/-3 (8 lines); hunks: -559,8 +559,11 @@ def _get_backend_priorities(; -1422,7 +1425,6 @@ def get_default_ir_op_priority(; symbols: _get_backend_priorities, get_default_ir_op_priority, touching `_get_backend_priorities, get_default_ir_op_priority`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +2/-2 (4 lines); hunks: -35,7 +35,7; -1489,7 +1489,7 @@ def forward_mqa(; symbols: forward_mqa
  - `vllm/platforms/rocm.py` modified +5/-3 (8 lines); hunks: -559,8 +559,11 @@ def _get_backend_priorities(; -1422,7 +1425,6 @@ def get_default_ir_op_priority(; symbols: _get_backend_priorities, get_default_ir_op_priority
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -35,7 +35,7 @@
-from vllm.platforms.rocm import _ON_GFX950, on_gfx1250
+from vllm.platforms.rocm import _ON_GFX950, on_gfx1250, on_rdna
@@ -1489,7 +1489,7 @@ def forward_mqa(
-            fuse_decode_inv_rope = fuse_inv_rope and not on_gfx1250()
+            fuse_decode_inv_rope = fuse_inv_rope and not on_gfx1250() and not on_rdna()
diff -- vllm/platforms/rocm.py
@@ -559,8 +559,11 @@ def _get_backend_priorities(
-    elif rocm_aiter_ops.is_rdna_aiter_enabled():
-        backends.insert(0, AttentionBackendEnum.ROCM_AITER_UNIFIED_ATTN)
+    if rocm_aiter_ops.is_rdna_aiter_enabled():
+        if on_rdna4():
+            backends.insert(0, AttentionBackendEnum.ROCM_AITER_UNIFIED_ATTN)
+        else:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +2/-2; `vllm/platforms/rocm.py` modified +5/-3
- Risk and verification: Runtime changes concentrate in `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #60154 - [ROCm][DSv4/4.1] Fuse inverse RoPE and MXFP8 quant into the aiter sparse MLA and sparse MLA gating changes

- Link: https://github.com/vllm-project/vllm/pull/60154
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `8d88bc5d815f`
- Diff scope read: GitHub Pull Request files API returned 4 files, +465/-91, 819 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4/4.1] Fuse inverse RoPE and MXFP8 quant into the aiter sparse MLA and sparse MLA gating changes"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v4/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4/4.1] Fuse inverse RoPE and MXFP8 quant into the aiter sparse MLA and sparse MLA gating changes"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v4/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +44/-67 (111 lines); hunks: -548,7 +548,6 @@ class DeepseekV41ROCMAiterMLAAttention(DeepseekV4Attention):; -984,8 +983,8 @@ def forward_mqa(; symbols: DeepseekV41ROCMAiterMLAAttention, _indexer_cls, forward_mqa, touching `DeepseekV41ROCMAiterMLAAttention, _indexer_cls, forward_mqa`; `vllm/models/deepseek_v4/amd/rocm.py` modified +57/-22 (79 lines); hunks: -141,6 +141,18 @@ def _aiter_sparse_mla_enabled(has_kv_transfer: bool) -> bool:; -747,8 +759,13 @@ def __init__(self, *args, **kwargs):; symbols: _aiter_sparse_mla_enabled, _aiter_sparse_mla_prefill_enabled, _build_indptr_from_lengths, __init__, touching `_aiter_sparse_mla_enabled, _aiter_sparse_mla_prefill_enabled, _build_indptr_from_lengths`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +44/-67 (111 lines); hunks: -548,7 +548,6 @@ class DeepseekV41ROCMAiterMLAAttention(DeepseekV4Attention):; -984,8 +983,8 @@ def forward_mqa(; symbols: DeepseekV41ROCMAiterMLAAttention, _indexer_cls, forward_mqa
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +57/-22 (79 lines); hunks: -141,6 +141,18 @@ def _aiter_sparse_mla_enabled(has_kv_transfer: bool) -> bool:; -747,8 +759,13 @@ def __init__(self, *args, **kwargs):; symbols: _aiter_sparse_mla_enabled, _aiter_sparse_mla_prefill_enabled, _build_indptr_from_lengths, __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -548,7 +548,6 @@ class DeepseekV41ROCMAiterMLAAttention(DeepseekV4Attention):
-    _use_aiter_sparse_mla = False
@@ -984,8 +983,8 @@ def forward_mqa(
-            # are skipped this step. The aiter prefill reads the caches in place,
-            # so it asks only for the bf16 rows of the MXFP8 output.
+            # are skipped this step. The aiter prefill reads the caches in place
+            # and needs none.
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -141,6 +141,18 @@ def _aiter_sparse_mla_enabled(has_kv_transfer: bool) -> bool:
+# aiter's sparse MLA prefill is slower than gather + OPUS at 128 heads per
+# rank, so prefill takes it only up to 64; decode takes it at any head count.
+_AITER_SPARSE_MLA_PREFILL_MAX_HEADS = 64
+def _aiter_sparse_mla_prefill_enabled(num_heads: int, has_kv_transfer: bool) -> bool:
+    return (
+        _aiter_sparse_mla_enabled(has_kv_transfer)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +44/-67; `vllm/models/deepseek_v4/amd/rocm.py` modified +57/-22
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63063 - [Perf][DSpark] Stack DeepSeek V41 context WKV projections

- Link: https://github.com/vllm-project/vllm/pull/63063
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/dspark.py`; associated commits `08b989da99f0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +101/-12, 218 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSpark] Stack DeepSeek V41 context WKV projections"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/dspark.py`; technical summary: Covers "[Perf][DSpark] Stack DeepSeek V41 context WKV projections"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/dspark.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/dspark.py` modified +29/-6 (35 lines); hunks: -29,7 +29,10; -46,6 +49,7; symbols: __init__, precompute_and_store_context_kv, load_weights, _remap_dspark_name, touching `__init__, precompute_and_store_context_kv, load_weights`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/dspark.py` modified +29/-6 (35 lines); hunks: -29,7 +29,10; -46,6 +49,7; symbols: __init__, precompute_and_store_context_kv, load_weights, _remap_dspark_name
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/dspark.py
@@ -29,7 +29,10 @@
-from vllm.model_executor.layers.linear import ReplicatedLinear
+from vllm.model_executor.layers.linear import (
+    MergedColumnParallelLinear,
+    ReplicatedLinear,
+)
@@ -46,6 +49,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/dspark.py` modified +29/-6
- Risk and verification: The diff ships test coverage in `tests/models/test_dspark_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59986 - [Bugfix][Attention] Keep DSV4.1 sparse prefill out of FULL cudagraphs

- Link: https://github.com/vllm-project/vllm/pull/59986
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/compressor.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/sparse_mla.py`; associated commits `8977b13a1c38`
- Diff scope read: GitHub Pull Request files API returned 5 files, +122/-8, 230 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Attention] Keep DSV4.1 sparse prefill out of FULL cudagraphs"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/sparse_mla.py`; technical summary: Covers "[Bugfix][Attention] Keep DSV4.1 sparse prefill out of FULL cudagraphs"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/sparse_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +25/-3 (28 lines); hunks: -31,11 +31,13; -178,15 +180,35 @@ def get_builder_cls() -> type["DeepseekV4FlashInferSparseM...; symbols: get_builder_cls, DeepseekV4FlashInferSparseMLAMetadataBuilder, get_varlen_cudagraph_max_query_len, DeepseekSparseSWAFlashInferMetadataBuilder, touching `get_builder_cls, DeepseekV4FlashInferSparseMLAMetadataBuilder, get_varlen_cudagraph_max_query_len`; `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +14/-2 (16 lines); hunks: -5,6 +5,7; -24,12 +25,13; symbols: DeepseekSparseSWAFlashMLAMetadataBuilder, get_varlen_cudagraph_max_query_len, DeepseekSparseSWAFlashMLABackend, touching `DeepseekSparseSWAFlashMLAMetadataBuilder, get_varlen_cudagraph_max_query_len, DeepseekSparseSWAFlashMLABackend`; `vllm/models/deepseek_v41/sparse_mla.py` modified +13/-2 (15 lines); hunks: -19,6 +19,7; -28,7 +29,7; symbols: build, DeepseekV4FlashMLAMetadataBuilder, get_varlen_cudagraph_max_query_len, DeepseekV4FlashMLABackend, touching `build, DeepseekV4FlashMLAMetadataBuilder, get_varlen_cudagraph_max_query_len`; `vllm/models/deepseek_v41/compressor.py` modified +12/-1 (13 lines); hunks: -26,6 +26,7; -97,7 +98,17 @@ def _ring_slot_mapping_kernel(; symbols: _ring_slot_mapping_kernel, CompressorMetadataBuilder, get_varlen_cudagraph_max_query_len, __init__, touching `_ring_slot_mapping_kernel, CompressorMetadataBuilder, get_varlen_cudagraph_max_query_len`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +25/-3 (28 lines); hunks: -31,11 +31,13; -178,15 +180,35 @@ def get_builder_cls() -> type["DeepseekV4FlashInferSparseM...; symbols: get_builder_cls, DeepseekV4FlashInferSparseMLAMetadataBuilder, get_varlen_cudagraph_max_query_len, DeepseekSparseSWAFlashInferMetadataBuilder
  - `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +14/-2 (16 lines); hunks: -5,6 +5,7; -24,12 +25,13; symbols: DeepseekSparseSWAFlashMLAMetadataBuilder, get_varlen_cudagraph_max_query_len, DeepseekSparseSWAFlashMLABackend
  - `vllm/models/deepseek_v41/sparse_mla.py` modified +13/-2 (15 lines); hunks: -19,6 +19,7; -28,7 +29,7; symbols: build, DeepseekV4FlashMLAMetadataBuilder, get_varlen_cudagraph_max_query_len, DeepseekV4FlashMLABackend
  - `vllm/models/deepseek_v41/compressor.py` modified +12/-1 (13 lines); hunks: -26,6 +26,7; -97,7 +98,17 @@ def _ring_slot_mapping_kernel(; symbols: _ring_slot_mapping_kernel, CompressorMetadataBuilder, get_varlen_cudagraph_max_query_len, __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py
@@ -31,11 +31,13 @@
+    max_decode_query_len,
+from vllm.v1.kv_cache_interface import KVCacheSpec
@@ -178,15 +180,35 @@ def get_builder_cls() -> type["DeepseekV4FlashInferSparseMLAMetadataBuilder"]:
-    """Varlen-capable metadata builder for the FlashInfer sparse MLA backend."""
+    """Varlen-decode-capable metadata builder for the FlashInfer sparse MLA backend."""
-    _cudagraph_support: ClassVar[AttentionCGSupport] = AttentionCGSupport.ALWAYS
diff -- vllm/models/deepseek_v41/nvidia/flashmla.py
@@ -5,6 +5,7 @@
+from vllm.config import VllmConfig
@@ -24,12 +25,13 @@
-from vllm.v1.attention.backend import AttentionCGSupport
+from vllm.v1.attention.backend import AttentionCGSupport, max_decode_query_len
+from vllm.v1.kv_cache_interface import KVCacheSpec
@@ -39,7 +41,17 @@
diff -- vllm/models/deepseek_v41/sparse_mla.py
@@ -19,6 +19,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +25/-3; `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +14/-2; `vllm/models/deepseek_v41/sparse_mla.py` modified +13/-2; `vllm/models/deepseek_v41/compressor.py` modified +12/-1
- Risk and verification: The diff ships test coverage in `tests/v1/worker/test_attn_utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63689 - [Bugfix][ROCm][DSv4] Give zero and subnormal mono MXFP8 groups vLLM's scale code

- Link: https://github.com/vllm-project/vllm/pull/63689
- Status/date: merged / 2026-10-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/mono/attention/device.py`, `vllm/models/deepseek_v4/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/attention/device.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py`; associated commits `ed1a7307950a`
- Diff scope read: GitHub Pull Request files API returned 4 files, +12/-2, 42 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm][DSv4] Give zero and subnormal mono MXFP8 groups vLLM's scale code"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/amd/mono/attention/device.py`, `vllm/models/deepseek_v41/amd/mono/attention/device.py`, `vllm/models/deepseek_v4/amd/mono/stages/moe.py`; technical summary: Covers "[Bugfix][ROCm][DSv4] Give zero and subnormal mono MXFP8 groups vLLM's scale code"; the main implementation surface is `vllm/models/deepseek_v4/amd/mono/attention/device.py`, `vllm/models/deepseek_v41/amd/mono/attention/device.py`, `vllm/models/deepseek_v4/amd/mono/stages/moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/mono/attention/device.py` modified +4/-1 (5 lines); hunks: -334,7 +334,10 @@ def mx_code(amax):; symbols: mx_code, mx_mul, touching `mx_code, mx_mul`; `vllm/models/deepseek_v41/amd/mono/attention/device.py` modified +4/-1 (5 lines); hunks: -336,7 +336,10 @@ def mx_code(amax):; symbols: mx_code, mx_mul, touching `mx_code, mx_mul`; `vllm/models/deepseek_v4/amd/mono/stages/moe.py` modified +2/-0 (2 lines); hunks: -289,6 +289,8 @@ def vllm_mx_code(amax):; symbols: vllm_mx_code, touching `vllm_mx_code`; `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +2/-0 (2 lines); hunks: -317,6 +317,8 @@ def vllm_mx_code(amax):; symbols: vllm_mx_code, touching `vllm_mx_code`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/mono/attention/device.py` modified +4/-1 (5 lines); hunks: -334,7 +334,10 @@ def mx_code(amax):; symbols: mx_code, mx_mul
  - `vllm/models/deepseek_v41/amd/mono/attention/device.py` modified +4/-1 (5 lines); hunks: -336,7 +336,10 @@ def mx_code(amax):; symbols: mx_code, mx_mul
  - `vllm/models/deepseek_v4/amd/mono/stages/moe.py` modified +2/-0 (2 lines); hunks: -289,6 +289,8 @@ def vllm_mx_code(amax):; symbols: vllm_mx_code
  - `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +2/-0 (2 lines); hunks: -317,6 +317,8 @@ def vllm_mx_code(amax):; symbols: vllm_mx_code
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/mono/attention/device.py
@@ -334,7 +334,10 @@ def mx_code(amax):
-    return fx.min(fx.max(ceil_exp(q), fx.Int32(0)), fx.Int32(254))
+    bits = q.bitcast(fx.Int32)
+    sub = (bits > 0x400000).select(fx.Int32(1), fx.Int32(0))
+    e = (bits < 0x800000).select(sub, ceil_exp(q))
+    return fx.min(fx.max(e, fx.Int32(0)), fx.Int32(254))
diff -- vllm/models/deepseek_v41/amd/mono/attention/device.py
@@ -336,7 +336,10 @@ def mx_code(amax):
-    return fx.min(fx.max(ceil_exp(q), fx.Int32(0)), fx.Int32(254))
+    bits = q.bitcast(fx.Int32)
+    sub = (bits > 0x400000).select(fx.Int32(1), fx.Int32(0))
+    e = (bits < 0x800000).select(sub, ceil_exp(q))
+    return fx.min(fx.max(e, fx.Int32(0)), fx.Int32(254))
diff -- vllm/models/deepseek_v4/amd/mono/stages/moe.py
@@ -289,6 +289,8 @@ def vllm_mx_code(amax):
+    sub = (bits > 0x400000).select(fx.Int32(1), fx.Int32(0))
+    e = (bits < 0x800000).select(sub, e)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/mono/attention/device.py` modified +4/-1; `vllm/models/deepseek_v41/amd/mono/attention/device.py` modified +4/-1; `vllm/models/deepseek_v4/amd/mono/stages/moe.py` modified +2/-0; `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +2/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/mono/attention/device.py`, `vllm/models/deepseek_v4/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/attention/device.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #61994 - [Spec Decode] Support PCP with DSpark for DeepSeek-V4.1

- Link: https://github.com/vllm-project/vllm/pull/61994
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/compressor.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `af6665b5dd20`
- Diff scope read: GitHub Pull Request files API returned 7 files, +154/-32, 338 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Spec Decode] Support PCP with DSpark for DeepSeek-V4.1"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `vllm/models/deepseek_v41/compressor.py`, `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Spec Decode] Support PCP with DSpark for DeepSeek-V4.1"; the main implementation surface is `vllm/models/deepseek_v41/compressor.py`, `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/compressor.py` modified +35/-17 (52 lines); hunks: -61,9 +61,9 @@ class CompressorMetadata:; -113,8 +113,10 @@ def __init__(self, *args, **kwargs):; symbols: CompressorMetadata, __init__, build, _link_pcp_chunks, touching `CompressorMetadata, __init__, build`; `tests/models/test_deepseek_v41_pcp.py` modified +21/-0 (21 lines); hunks: -174,3 +174,24 @@ def test_pcp_replay_gathers_compacted_routing_ids(monkeypat...; symbols: test_pcp_replay_gathers_compacted_routing_ids, test_pcp_rejects_speculation_other_than_fixed_length_dspark, touching `test_pcp_replay_gathers_compacted_routing_ids, test_pcp_rejects_speculation_other_than_fixed_length_dspark`; `vllm/models/deepseek_v41/nvidia/model.py` modified +9/-2 (11 lines); hunks: -710,7 +710,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; -720,7 +726,8 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/models/deepseek_v41/compressor.py` modified +35/-17 (52 lines); hunks: -61,9 +61,9 @@ class CompressorMetadata:; -113,8 +113,10 @@ def __init__(self, *args, **kwargs):; symbols: CompressorMetadata, __init__, build, _link_pcp_chunks
  - `tests/models/test_deepseek_v41_pcp.py` modified +21/-0 (21 lines); hunks: -174,3 +174,24 @@ def test_pcp_replay_gathers_compacted_routing_ids(monkeypat...; symbols: test_pcp_replay_gathers_compacted_routing_ids, test_pcp_rejects_speculation_other_than_fixed_length_dspark
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +9/-2 (11 lines); hunks: -710,7 +710,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; -720,7 +726,8 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/compressor.py
@@ -61,9 +61,9 @@ class CompressorMetadata:
-    # PCP only: every rank gathers the last row of each rank's local requests.
+    # PCP gathers chunk tails, including rollback rows for speculative decoding.
-    # [pcp * rows] ring slot of each request's newest row if it is open, else -1.
+    # [pcp * rows] ring slots to publish, or -1 for unused/duplicate rows.
@@ -113,8 +113,10 @@ def __init__(self, *args, **kwargs):
-        # The ring keeps only the open row under PCP, too few for spec decoding.
diff -- tests/models/test_deepseek_v41_pcp.py
@@ -174,3 +174,24 @@ def test_pcp_replay_gathers_compacted_routing_ids(monkeypatch):
+@pytest.mark.parametrize("method,adaptive", [("mtp", False), ("dspark", True)])
+def test_pcp_rejects_speculation_other_than_fixed_length_dspark(method, adaptive):
+    config = SimpleNamespace(
+        model_config=SimpleNamespace(hf_config=SimpleNamespace()),
+        quant_config=None,
+        parallel_config=SimpleNamespace(
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -710,7 +710,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/compressor.py` modified +35/-17; `vllm/models/deepseek_v41/nvidia/model.py` modified +9/-2
  - tests: `tests/models/test_deepseek_v41_pcp.py` modified +21/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/v1/worker/test_gpu_pcp_manager.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63576 - [Bugfix][ROCm][DSv4.1] Await krdy before K2's combine reads klen in index-source launches

- Link: https://github.com/vllm-project/vllm/pull/63576
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/mono/attention/back.py`; associated commits `9744ada58292`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-1, 11 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm][DSv4.1] Await krdy before K2's combine reads klen in index-source launches"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/amd/mono/attention/back.py`; technical summary: Covers "[Bugfix][ROCm][DSv4.1] Await krdy before K2's combine reads klen in index-source launches"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono/attention/back.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +3/-1 (4 lines); hunks: -518,7 +518,9 @@ def stage_combine(c, unit):; symbols: stage_combine, touching `stage_combine`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +3/-1 (4 lines); hunks: -518,7 +518,9 @@ def stage_combine(c, unit):; symbols: stage_combine
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono/attention/back.py
@@ -518,7 +518,9 @@ def stage_combine(c, unit):
-    kv_len = ld_i32(a["klen"], t)
+    if const_expr("krdy" in c):
+        await_flags(c, c["krdy"], 1, lambda u: t)
+    kv_len = ld_i32(a["klen"], t, CM_DEV if const_expr("krdy" in c) else 0)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono/attention/back.py` modified +3/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/amd/mono/attention/back.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #61875 - [Perf][DeepSeek V4] Declare MXFP8 MoE activations and run them as block FP8 on Hopper

- Link: https://github.com/vllm-project/vllm/pull/61875
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v41/quant_config.py`; associated commits `fcb787055e85`
- Diff scope read: GitHub Pull Request files API returned 5 files, +47/-3, 89 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DeepSeek V4] Declare MXFP8 MoE activations and run them as block FP8 on Hopper"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v41/quant_config.py`; technical summary: Covers "[Perf][DeepSeek V4] Declare MXFP8 MoE activations and run them as block FP8 on Hopper"; the main implementation surface is `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v41/quant_config.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/quant_config.py` modified +2/-1 (3 lines); hunks: -16,6 +16,7; -223,7 +224,7 @@ def get_quant_method(self, layer, prefix):; symbols: get_quant_method, touching `get_quant_method`; `vllm/models/deepseek_v41/quant_config.py` modified +1/-1 (2 lines); hunks: -258,7 +258,7 @@ def get_quant_method(self, layer, prefix):; symbols: get_quant_method, touching `get_quant_method`.
- Code diff details:
  - `vllm/models/deepseek_v4/quant_config.py` modified +2/-1 (3 lines); hunks: -16,6 +16,7; -223,7 +224,7 @@ def get_quant_method(self, layer, prefix):; symbols: get_quant_method
  - `vllm/models/deepseek_v41/quant_config.py` modified +1/-1 (2 lines); hunks: -258,7 +258,7 @@ def get_quant_method(self, layer, prefix):; symbols: get_quant_method
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/quant_config.py
@@ -16,6 +16,7 @@
+    kMxfp8Dynamic,
@@ -223,7 +224,7 @@ def get_quant_method(self, layer, prefix):
-                return Mxfp4MoEMethod(layer.moe_config)
+                return Mxfp4MoEMethod(layer.moe_config, activation_key=kMxfp8Dynamic)
diff -- vllm/models/deepseek_v41/quant_config.py
@@ -258,7 +258,7 @@ def get_quant_method(self, layer, prefix):
-                return Mxfp4MoEMethod(layer.moe_config)
+                return Mxfp4MoEMethod(layer.moe_config, activation_key=kMxfp8Dynamic)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/quant_config.py` modified +2/-1; `vllm/models/deepseek_v41/quant_config.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/quantization/test_fp8.py`, `tests/quantization/test_humming_mxfp4_block_fp8.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62091 - [Perf][DSv4.1] Read GPU Engram tables from peers' HBM instead of DP collectives

- Link: https://github.com/vllm-project/vllm/pull/62091
- Status/date: merged / 2026-10-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `85e199e60ca8`
- Diff scope read: GitHub Pull Request files API returned 5 files, +164/-48, 436 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Read GPU Engram tables from peers' HBM instead of DP collectives"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/kernels/test_engram.py`; technical summary: Covers "[Perf][DSv4.1] Read GPU Engram tables from peers' HBM instead of DP collectives"; the main implementation surface is `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/kernels/test_engram.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/engram.py` modified +77/-10 (87 lines); hunks: -60,7 +60,7; -658,6 +658,7 @@ def _engram_lookup_kernel(; symbols: _engram_lookup_kernel, __init__, touching `_engram_lookup_kernel, __init__`; `vllm/models/deepseek_v41/nvidia/model.py` modified +11/-4 (15 lines); hunks: -902,11 +902,18 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`; `tests/kernels/test_engram.py` modified +3/-1 (4 lines); hunks: -574,6 +574,7 @@ def _make_embedding(cpu_offload, rows=4096, dim=256, block=32):; -627,7 +628,8 @@ def test_engram_rejects_empty_head_shards(tp_size, dp_size,...; symbols: _make_embedding, test_engram_rejects_empty_head_shards, touching `_make_embedding, test_engram_rejects_empty_head_shards`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/engram.py` modified +77/-10 (87 lines); hunks: -60,7 +60,7; -658,6 +658,7 @@ def _engram_lookup_kernel(; symbols: _engram_lookup_kernel, __init__
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +11/-4 (15 lines); hunks: -902,11 +902,18 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
  - `tests/kernels/test_engram.py` modified +3/-1 (4 lines); hunks: -574,6 +574,7 @@ def _make_embedding(cpu_offload, rows=4096, dim=256, block=32):; -627,7 +628,8 @@ def test_engram_rejects_empty_head_shards(tp_size, dp_size,...; symbols: _make_embedding, test_engram_rejects_empty_head_shards
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -60,7 +60,7 @@
-from vllm.distributed.parallel_state import GroupCoordinator
+from vllm.distributed.parallel_state import GroupCoordinator, in_the_same_node_as
@@ -658,6 +658,7 @@ def _engram_lookup_kernel(
+    PEER_ROWS: tl.constexpr = 0,
@@ -688,15 +689,22 @@ def _engram_lookup_kernel(
+        if PEER_ROWS:
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -902,11 +902,18 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-            local_engram = any(
-                isinstance(layer, DeepseekV4DecoderLayer) and layer.engram is not None
-                for layer in islice(self.layers, self.start_layer, self.end_layer)
+            engram = next(
+                (
+                    layer.engram
diff -- tests/kernels/test_engram.py
@@ -574,6 +574,7 @@ def _make_embedding(cpu_offload, rows=4096, dim=256, block=32):
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/engram.py` modified +77/-10; `vllm/models/deepseek_v41/nvidia/model.py` modified +11/-4
  - tests: `tests/kernels/test_engram.py` modified +3/-1
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_engram.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61482 - [ROCm][Perf][DSv4] Standalone mono decode layer for DeepSeek-V4-Pro on MI355X

- Link: https://github.com/vllm-project/vllm/pull/61482
- Status/date: merged / 2026-10-24
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mono/README.md`, `vllm/models/deepseek_v4/amd/mono/__init__.py`, `vllm/models/deepseek_v4/amd/mono/attention/__init__.py`, `vllm/models/deepseek_v4/amd/mono/attention/back.py` and 28 files; associated commits `139feb45348d`
- Diff scope read: GitHub Pull Request files API returned 33 files, +9865/-2, 9946 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4] Standalone mono decode layer for DeepSeek-V4-Pro on MI355X"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/mono/stages/moe.py`, `vllm/models/deepseek_v4/amd/mono/attention/back.py`, `vllm/models/deepseek_v4/amd/mono/layer.py`; technical summary: Covers "[ROCm][Perf][DSv4] Standalone mono decode layer for DeepSeek-V4-Pro on MI355X"; the main implementation surface is `vllm/models/deepseek_v4/amd/mono/stages/moe.py`, `vllm/models/deepseek_v4/amd/mono/attention/back.py`, `vllm/models/deepseek_v4/amd/mono/layer.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/mono/stages/moe.py` added +1733/-0 (1733 lines); hunks: -0,0 +1,1733; symbols: scratch_layout, peer_bytes, ffn_offset, red_tasks, touching `scratch_layout, peer_bytes, ffn_offset`; `vllm/models/deepseek_v4/amd/mono/attention/back.py` added +1021/-0 (1021 lines); hunks: -0,0 +1,1021; symbols: BackBuild, plus, head_groups, chunk_keys, touching `BackBuild, plus, head_groups`; `vllm/models/deepseek_v4/amd/mono/layer.py` added +927/-0 (927 lines); hunks: -0,0 +1,927; symbols: MonoBuild, _variant, _dims, _moe_key, touching `MonoBuild, _variant, _dims`; `vllm/models/deepseek_v4/amd/mono/attention/front.py` added +573/-0 (573 lines); hunks: -0,0 +1,573; symbols: FrontBuild, plus, publish, await_flags, touching `FrontBuild, plus, publish`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/mono/stages/moe.py` added +1733/-0 (1733 lines); hunks: -0,0 +1,1733; symbols: scratch_layout, peer_bytes, ffn_offset, red_tasks
  - `vllm/models/deepseek_v4/amd/mono/attention/back.py` added +1021/-0 (1021 lines); hunks: -0,0 +1,1021; symbols: BackBuild, plus, head_groups, chunk_keys
  - `vllm/models/deepseek_v4/amd/mono/layer.py` added +927/-0 (927 lines); hunks: -0,0 +1,927; symbols: MonoBuild, _variant, _dims, _moe_key
  - `vllm/models/deepseek_v4/amd/mono/attention/front.py` added +573/-0 (573 lines); hunks: -0,0 +1,573; symbols: FrontBuild, plus, publish, await_flags
  - `vllm/models/deepseek_v4/amd/mono/attention/device.py` added +504/-0 (504 lines); hunks: -0,0 +1,504; symbols: traced, kernel_symbol, first_task, rsrc
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/mono/stages/moe.py
@@ -0,0 +1,1733 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Adapted from ROCm/ATOM (https://github.com/ROCm/ATOM) at 97359d6, MIT License,
+# Copyright (C) 2026, Advanced Micro Devices, Inc.:
+# atom/models/deepseek_v41/mono/kernels/moe.py
+"""The mono layer's MoE stages: one layer's FFN, from the FFN seam's normed rows
diff -- vllm/models/deepseek_v4/amd/mono/attention/back.py
@@ -0,0 +1,1021 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""K2 ``back``: one attention layer from the rotated query to the rank's wo_b
+partial.
+One launch a layer and rank, ``BLOCKS`` x ``THREADS``, S rows:
+    split   (S x chunks of CK keys): flash-decoding over one chunk of a token's
diff -- vllm/models/deepseek_v4/amd/mono/layer.py
@@ -0,0 +1,927 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/mono/stages/moe.py` added +1733/-0; `vllm/models/deepseek_v4/amd/mono/attention/back.py` added +1021/-0; `vllm/models/deepseek_v4/amd/mono/layer.py` added +927/-0; `vllm/models/deepseek_v4/amd/mono/attention/front.py` added +573/-0; `vllm/models/deepseek_v4/amd/mono/attention/device.py` added +504/-0; `vllm/models/deepseek_v4/amd/mono/runner.py` added +463/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv4_mono_decode.py`, `tests/models/test_dsv4_mono_layers.py`, `tests/models/test_dsv4_mono_numerics.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62384 - [Feature][PCP] Support decoder-side SWA bounded replay with APC for DeepSeek-V4.1-Flash

- Link: https://github.com/vllm-project/vllm/pull/62384
- Status/date: merged / 2026-10-23
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_amd_replay_forward.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py` and 8 files; associated commits `c7476c7a6fc8`
- Diff scope read: GitHub Pull Request files API returned 12 files, +351/-57, 693 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature][PCP] Support decoder-side SWA bounded replay with APC for DeepSeek-V4.1-Flash"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/models/test_deepseek_v41_replay_batch.py`; technical summary: Covers "[Feature][PCP] Support decoder-side SWA bounded replay with APC for DeepSeek-V4.1-Flash"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/models/test_deepseek_v41_replay_batch.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +87/-25 (112 lines); hunks: -224,9 +224,15 @@ def __init__(; -235,14 +241,14 @@ def __init__(; symbols: __init__, prepare_attn, _prepare_replay_batch, touching `__init__, prepare_attn, _prepare_replay_batch`; `tests/models/test_deepseek_v41_pcp.py` modified +110/-0 (110 lines); hunks: -6,9 +6,68; -64,3 +123,54 @@ def test_pcp_gathers_routing_ids_once_after_local_input_prep...; symbols: test_replay_kv_publishes_all_pcp_owners, test_pcp_gathers_routing_ids_once_after_local_input_preparation, test_pcp_replay_pads_inputs_and_scatters_only_real_rows, run_layers, touching `test_replay_kv_publishes_all_pcp_owners, test_pcp_gathers_routing_ids_once_after_local_input_preparation, test_pcp_replay_pads_inputs_and_scatters_only_real_rows`; `tests/models/test_deepseek_v41_replay_batch.py` modified +63/-2 (65 lines); hunks: -25,6 +25,7; -58,7 +59,7; symbols: state, _input_batch, test_prompt_logprobs_requests_keep_their_rows, touching `state, _input_batch, test_prompt_logprobs_requests_keep_their_rows`; `vllm/models/deepseek_v41/attention.py` modified +21/-9 (30 lines); hunks: -548,10 +548,7 @@ def __init__(; -707,15 +704,26 @@ def forward_kv(self, positions: torch.Tensor, hidden_state...; symbols: __init__, forward_kv, bind_gemm_rs, touching `__init__, forward_kv, bind_gemm_rs`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +87/-25 (112 lines); hunks: -224,9 +224,15 @@ def __init__(; -235,14 +241,14 @@ def __init__(; symbols: __init__, prepare_attn, _prepare_replay_batch
  - `tests/models/test_deepseek_v41_pcp.py` modified +110/-0 (110 lines); hunks: -6,9 +6,68; -64,3 +123,54 @@ def test_pcp_gathers_routing_ids_once_after_local_input_prep...; symbols: test_replay_kv_publishes_all_pcp_owners, test_pcp_gathers_routing_ids_once_after_local_input_preparation, test_pcp_replay_pads_inputs_and_scatters_only_real_rows, run_layers
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +63/-2 (65 lines); hunks: -25,6 +25,7; -58,7 +59,7; symbols: state, _input_batch, test_prompt_logprobs_requests_keep_their_rows
  - `vllm/models/deepseek_v41/attention.py` modified +21/-9 (30 lines); hunks: -548,10 +548,7 @@ def __init__(; -707,15 +704,26 @@ def forward_kv(self, positions: torch.Tensor, hidden_state...; symbols: __init__, forward_kv, bind_gemm_rs
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +14/-7 (21 lines); hunks: -1059,6 +1059,7 @@ def forward(; -1095,7 +1096,9 @@ def forward(; symbols: forward, _run_replay_layers, _decoder_replay_supported
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -224,9 +224,15 @@ def __init__(
+            if self.pcp_size > 1:
+                assert self.decoder_replay_layers.window >= 2 * self.pcp_size, (
+                    "PCP replay requires window >= 2 * PCP size so each trimmed "
+                    "request is represented on every rank."
+                )
+                self._pcp_replay_start = UvaBufferPool(max_local_reqs, torch.int32)
diff -- tests/models/test_deepseek_v41_pcp.py
@@ -6,9 +6,68 @@
+from vllm.forward_context import ForwardContext, override_forward_context
+from vllm.models.deepseek_v41 import attention as attention_module
+from vllm.models.deepseek_v41.decoder_replay_layers import (
+    DecoderReplayLayers,
+    ReplayBatch,
+)
diff -- tests/models/test_deepseek_v41_replay_batch.py
@@ -25,6 +25,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +87/-25; `vllm/models/deepseek_v41/attention.py` modified +21/-9; `vllm/models/deepseek_v41/nvidia/model.py` modified +14/-7; `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +16/-4; `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +3/-4
  - tests: `tests/models/test_deepseek_v41_pcp.py` modified +110/-0; `tests/models/test_deepseek_v41_replay_batch.py` modified +63/-2; `tests/models/test_deepseek_v41_amd_replay_forward.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_amd_replay_forward.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `tests/v1/worker/test_gpu_pcp_manager.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60613 - [Bugfix][DSv4.1] Seed the -1 sentinel in the prefill sparse index workspace

- Link: https://github.com/vllm-project/vllm/pull/60613
- Status/date: merged / 2026-10-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/ops/cache_utils.py`; associated commits `9bd5c2a0582d`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Seed the -1 sentinel in the prefill sparse index workspace"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/common/ops/cache_utils.py`; technical summary: Covers "[Bugfix][DSv4.1] Seed the -1 sentinel in the prefill sparse index workspace"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/cache_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +1/-0 (1 lines); hunks: -946,6 +946,7 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices, touching `combine_topk_swa_indices`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +1/-0 (1 lines); hunks: -946,6 +946,7 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -946,6 +946,7 @@ def combine_topk_swa_indices(
+        combined_indices.fill_(-1)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/common/ops/cache_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #60834 - [ROCm][Perf] Apply opt-in paged MXFP4 sparse indexer dense path for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/60834
- Status/date: merged / 2026-10-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `022b43c66f6c`
- Diff scope read: GitHub Pull Request files API returned 10 files, +653/-106, 960 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Apply opt-in paged MXFP4 sparse indexer dense path for DeepSeek-V4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v41/amd/rocm.py`; technical summary: Covers "[ROCm][Perf] Apply opt-in paged MXFP4 sparse indexer dense path for DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v41/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +280/-2 (282 lines); hunks: -3,7 +3,7; -15,8 +15,20; symbols: _pack_global_topk_ragged_kernel, _compress_pool_kernel, _compress_pool_warmup_inputs, compress_pool, touching `_pack_global_topk_ragged_kernel, _compress_pool_kernel, _compress_pool_warmup_inputs`; `vllm/models/deepseek_v4/attention.py` modified +53/-24 (77 lines); hunks: -193,6 +193,11 @@ def _uses_fp8_ds_mla_layout(self) -> bool:; -302,7 +307,7 @@ def __init__(; symbols: _uses_fp8_ds_mla_layout, _get_indexer_cls, __init__, get_attn_backend, touching `_uses_fp8_ds_mla_layout, _get_indexer_cls, __init__`; `vllm/models/deepseek_v41/amd/rocm.py` modified +2/-72 (74 lines); hunks: -2,7 +2,6; -62,7 +61,8; symbols: build, _aiter_indexer_cache_ops, rocm_mxfp4_indexer_k_store, rocm_mxfp4_indexer_q_quant, touching `build, _aiter_indexer_cache_ops, rocm_mxfp4_indexer_k_store`; `vllm/models/deepseek_v4/compressor.py` modified +28/-3 (31 lines); hunks: -374,10 +374,7 @@ def forward(; -419,6 +416,34 @@ def forward(; symbols: forward, _compress_norm_rope_store, touching `forward, _compress_norm_rope_store`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +280/-2 (282 lines); hunks: -3,7 +3,7; -15,8 +15,20; symbols: _pack_global_topk_ragged_kernel, _compress_pool_kernel, _compress_pool_warmup_inputs, compress_pool
  - `vllm/models/deepseek_v4/attention.py` modified +53/-24 (77 lines); hunks: -193,6 +193,11 @@ def _uses_fp8_ds_mla_layout(self) -> bool:; -302,7 +307,7 @@ def __init__(; symbols: _uses_fp8_ds_mla_layout, _get_indexer_cls, __init__, get_attn_backend
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +2/-72 (74 lines); hunks: -2,7 +2,6; -62,7 +61,8; symbols: build, _aiter_indexer_cache_ops, rocm_mxfp4_indexer_k_store, rocm_mxfp4_indexer_q_quant
  - `vllm/models/deepseek_v4/compressor.py` modified +28/-3 (31 lines); hunks: -374,10 +374,7 @@ def forward(; -419,6 +416,34 @@ def forward(; symbols: forward, _compress_norm_rope_store
  - `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py` modified +4/-0 (4 lines); hunks: -1203,6 +1203,10 @@ def get_warmup_keys(self, vllm_config: Any) -> list[Compi...; symbols: get_warmup_keys
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -3,7 +3,7 @@
-from typing import cast
+from typing import Any, cast
@@ -15,8 +15,20 @@
-from vllm.models.deepseek_v4.attention import DeepseekV4Attention
+from vllm.model_executor.layers.rocm_paged_mxfp4_indexer import RocmSparseAttnIndexer
+from vllm.model_executor.layers.sparse_attn_indexer import SparseAttnIndexer
diff -- vllm/models/deepseek_v4/attention.py
@@ -193,6 +193,11 @@ def _uses_fp8_ds_mla_layout(self) -> bool:
+    def _get_indexer_cls(self, vllm_config: VllmConfig) -> type["DeepseekV4Indexer"]:
+        """The indexer for this layer. A platform subclass returns one that
+        writes and scores its own index K cache layout."""
+        return DeepseekV4Indexer
@@ -302,7 +307,7 @@ def __init__(
-            self.indexer = DeepseekV4Indexer(
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -2,7 +2,6 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +280/-2; `vllm/models/deepseek_v4/attention.py` modified +53/-24; `vllm/models/deepseek_v41/amd/rocm.py` modified +2/-72; `vllm/models/deepseek_v4/compressor.py` modified +28/-3; `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py` modified +4/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_dsv4_mxfp4_indexer.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63007 - [Bugfix][ROCm][DSv4.1] Gather Engram hashes across DP replicas in the AMD model

- Link: https://github.com/vllm-project/vllm/pull/63007
- Status/date: merged / 2026-10-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/model.py`; associated commits `6d1909a1f23e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +40/-6, 112 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm][DSv4.1] Gather Engram hashes across DP replicas in the AMD model"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/amd/model.py`; technical summary: Covers "[Bugfix][ROCm][DSv4.1] Gather Engram hashes across DP replicas in the AMD model"; the main implementation surface is `vllm/models/deepseek_v41/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/model.py` modified +26/-2 (28 lines); hunks: -11,6 +11,7; -67,7 +68,13; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/model.py` modified +26/-2 (28 lines); hunks: -11,6 +11,7; -67,7 +68,13; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -11,6 +11,7 @@
+    get_engram_dp_size,
@@ -67,7 +68,13 @@
-from ..common.engram import Engram, EngramLayout, NgramHashState
+from ..common.engram import (
+    Engram,
+    EngramLayout,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/model.py` modified +26/-2
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #63009 - [ROCm][DSv4.1] Allocate offloaded Engram tables at their exact size

- Link: https://github.com/vllm-project/vllm/pull/63009
- Status/date: merged / 2026-10-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/engram.py`; associated commits `f01a76f9503c`
- Diff scope read: GitHub Pull Request files API returned 3 files, +12/-6, 52 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1] Allocate offloaded Engram tables at their exact size"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `vllm/models/deepseek_v41/common/engram.py`, `tests/kernels/test_engram.py`, `vllm/config/engram.py`; technical summary: Covers "[ROCm][DSv4.1] Allocate offloaded Engram tables at their exact size"; the main implementation surface is `vllm/models/deepseek_v41/common/engram.py`, `tests/kernels/test_engram.py`, `vllm/config/engram.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/engram.py` modified +2/-1 (3 lines); hunks: -1053,7 +1053,8 @@ def _allocate_weights(self) -> tuple[torch.Tensor, torch.T...; symbols: _allocate_weights, touching `_allocate_weights`; `tests/kernels/test_engram.py` modified +8/-4 (12 lines); hunks: -755,9 +755,12 @@ def test_engram_lookup_matches_torch(cpu_offload, backgroun...; -768,13 +771,14 @@ def test_engram_use_thp_lookup_and_fallback(monkeypatch, r...; symbols: test_engram_lookup_matches_torch, test_engram_use_thp_lookup_and_fallback, touching `test_engram_lookup_matches_torch, test_engram_use_thp_lookup_and_fallback`; `vllm/config/engram.py` modified +2/-1 (3 lines); hunks: -52,7 +52,8 @@ class EngramConfig:; symbols: EngramConfig, _validate_shared_memory, touching `EngramConfig, _validate_shared_memory`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/engram.py` modified +2/-1 (3 lines); hunks: -1053,7 +1053,8 @@ def _allocate_weights(self) -> tuple[torch.Tensor, torch.T...; symbols: _allocate_weights
  - `tests/kernels/test_engram.py` modified +8/-4 (12 lines); hunks: -755,9 +755,12 @@ def test_engram_lookup_matches_torch(cpu_offload, backgroun...; -768,13 +771,14 @@ def test_engram_use_thp_lookup_and_fallback(monkeypatch, r...; symbols: test_engram_lookup_matches_torch, test_engram_use_thp_lookup_and_fallback
  - `vllm/config/engram.py` modified +2/-1 (3 lines); hunks: -52,7 +52,8 @@ class EngramConfig:; symbols: EngramConfig, _validate_shared_memory
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -1053,7 +1053,8 @@ def _allocate_weights(self) -> tuple[torch.Tensor, torch.Tensor]:
-        if self.use_thp:
+        # pin_memory rounds up to a power of two. ROCm pins huge pages either way.
+        if self.use_thp or current_platform.is_rocm():
diff -- tests/kernels/test_engram.py
@@ -755,9 +755,12 @@ def test_engram_lookup_matches_torch(cpu_offload, background, packed, num_tokens
-@pytest.mark.skipif(not current_platform.is_cuda(), reason="CUDA required")
+@pytest.mark.skipif(
+    not current_platform.is_cuda_alike(), reason="CUDA or ROCm required"
+)
+@pytest.mark.parametrize("use_thp", [False, True])
-def test_engram_use_thp_lookup_and_fallback(monkeypatch, register_fails):
diff -- vllm/config/engram.py
@@ -52,7 +52,8 @@ class EngramConfig:
-    startup takes longer. Requires cpu_offload without dp_shared_memory."""
+    startup takes longer. Requires cpu_offload without dp_shared_memory.
+    Always on for private tables on ROCm."""
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/engram.py` modified +2/-1; `vllm/config/engram.py` modified +2/-1
  - tests: `tests/kernels/test_engram.py` modified +8/-4
- Risk and verification: The diff ships test coverage in `tests/kernels/test_engram.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61615 - [Perf] Enable small-head FlashMLA sparse prefill for DS V4.1 on SM90

- Link: https://github.com/vllm-project/vllm/pull/61615
- Status/date: merged / 2026-10-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/flashmla.py`; associated commits `b579949edf93`
- Diff scope read: GitHub Pull Request files API returned 2 files, +14/-4, 48 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Enable small-head FlashMLA sparse prefill for DS V4.1 on SM90"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/flashmla.py`; technical summary: Covers "[Perf] Enable small-head FlashMLA sparse prefill for DS V4.1 on SM90"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flashmla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +13/-3 (16 lines); hunks: -22,6 +22,7; -63,6 +64,15 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _get_prefill_num_heads, _o_proj, _forward_prefill, touching `__init__, _get_prefill_num_heads, _o_proj`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +13/-3 (16 lines); hunks: -22,6 +22,7; -63,6 +64,15 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _get_prefill_num_heads, _o_proj, _forward_prefill
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flashmla.py
@@ -22,6 +22,7 @@
+from vllm.platforms import current_platform
@@ -63,6 +64,15 @@ def __init__(self, *args, **kwargs) -> None:
+        self._prefill_num_heads = self._get_prefill_num_heads()
+    def _get_prefill_num_heads(self) -> int:
+        return (
+            self.n_local_heads
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +13/-3
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/nvidia/flashmla.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #61868 - [Perf][DSv4.1] DeepSeek-V4.1-Flash specialized decode on GB300

- Link: https://github.com/vllm-project/vllm/pull/61868
- Status/date: merged / 2026-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/deepseek_v41/__init__.py`, `tests/models/deepseek_v41/nvidia/__init__.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/__init__.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_layers.py` and 41 files; associated commits `d0787e48394b`
- Diff scope read: GitHub Pull Request files API returned 42 files, +9996/-137, 10508 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] DeepSeek-V4.1-Flash specialized decode on GB300"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py`; technical summary: Covers "[Perf][DSv4.1] DeepSeek-V4.1-Flash specialized decode on GB300"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py` added +1284/-0 (1284 lines); hunks: -0,0 +1,1284; symbols: tile_scale_bytes, RoutedExpertGemm, __init__, _setup_attributes, touching `tile_scale_bytes, RoutedExpertGemm, __init__`; `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` added +1137/-0 (1137 lines); hunks: -0,0 +1,1137; symbols: _capture, _bf16_ulps, ordered, _routing, touching `_capture, _bf16_ulps, ordered`; `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` added +829/-0 (829 lines); hunks: -0,0 +1,829; symbols: _late, _randn, _mix, _partial, touching `_late, _randn, _mix`; `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_front_cute.py` added +675/-0 (675 lines); hunks: -0,0 +1,675; symbols: _asm, _f32, _u32, score_and_key, touching `_asm, _f32, _u32`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py` added +1284/-0 (1284 lines); hunks: -0,0 +1,1284; symbols: tile_scale_bytes, RoutedExpertGemm, __init__, _setup_attributes
  - `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` added +1137/-0 (1137 lines); hunks: -0,0 +1,1137; symbols: _capture, _bf16_ulps, ordered, _routing
  - `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` added +829/-0 (829 lines); hunks: -0,0 +1,829; symbols: _late, _randn, _mix, _partial
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_front_cute.py` added +675/-0 (675 lines); hunks: -0,0 +1,675; symbols: _asm, _f32, _u32, score_and_key
  - `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm.py` added +615/-0 (615 lines); hunks: -0,0 +1,615; symbols: max_ctas, cta_words, route_words, FrontConfig
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py
@@ -0,0 +1,1284 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# RoutedExpertGemm is modified from LowLatencyBlockscaledGemmKernel in
+# FlashInfer (flashinfer/gemm/kernels/cute_dsl/low_latency_blockscaled_gemm.py,
+# flashinfer-python 0.7.1), which carries the notice below: its operand and
+# scale-factor layouts, TMA partitioning, load warps, MMA warp and accumulator
diff -- tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py
@@ -0,0 +1,1137 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Single-GPU kernels of the DeepSeek-V4.1 specialized decode
+(``vllm/models/deepseek_v41/nvidia/specialized_decode``), each against the stock path
+it replaces, eagerly and replayed from a CUDA graph where the decode captures
+it. Needs one SM100-family GPU; about 5 minutes, mostly kernel compilation.
diff -- tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py
@@ -0,0 +1,829 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm_cute.py` added +1284/-0; `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_front_cute.py` added +675/-0; `vllm/models/deepseek_v41/nvidia/specialized_decode/moe/routed_expert_gemm.py` added +615/-0; `vllm/models/deepseek_v41/nvidia/specialized_decode/boundary/publishing_gemm.py` added +601/-0; `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` modified +331/-122
  - tests: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py` added +1137/-0; `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py` added +829/-0; `tests/models/deepseek_v41/nvidia/specialized_decode/test_layers.py` added +556/-0
- Risk and verification: The diff ships test coverage in `tests/models/deepseek_v41/__init__.py`, `tests/models/deepseek_v41/nvidia/__init__.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/__init__.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62652 - [Bugfix][Model] Preserve target-token scoring rows during DeepSeek-V4.1 replay

- Link: https://github.com/vllm-project/vllm/pull/62652
- Status/date: merged / 2026-10-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`; associated commits `85752a43c3ce`
- Diff scope read: GitHub Pull Request files API returned 2 files, +71/-10, 109 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] Preserve target-token scoring rows during DeepSeek-V4.1 replay"; model line: DeepSeek V4; category: bug fix; main diff: `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`; technical summary: Covers "[Bugfix][Model] Preserve target-token scoring rows during DeepSeek-V4.1 replay"; the main implementation surface is `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_replay_batch.py` modified +66/-9 (75 lines); hunks: -21,6 +21,7; -215,14 +216,70 @@ def test_replay_batch_keeps_device_decode_boundaries(state):; symbols: test_replay_batch_keeps_device_decode_boundaries, test_prompt_logprobs_requests_keep_their_rows, test_aux_output_requests_keep_every_routing_row, touching `test_replay_batch_keeps_device_decode_boundaries, test_prompt_logprobs_requests_keep_their_rows, test_aux_output_requests_keep_every_routing_row`; `vllm/models/deepseek_v41/nvidia/model_state.py` modified +5/-1 (6 lines); hunks: -278,7 +278,11 @@ def add_request(self, req_index: int, new_req_data: NewRequ...; symbols: add_request, prepare_inputs, touching `add_request, prepare_inputs`.
- Code diff details:
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +66/-9 (75 lines); hunks: -21,6 +21,7; -215,14 +216,70 @@ def test_replay_batch_keeps_device_decode_boundaries(state):; symbols: test_replay_batch_keeps_device_decode_boundaries, test_prompt_logprobs_requests_keep_their_rows, test_aux_output_requests_keep_every_routing_row
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +5/-1 (6 lines); hunks: -278,7 +278,11 @@ def add_request(self, req_index: int, new_req_data: NewRequ...; symbols: add_request, prepare_inputs
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_replay_batch.py
@@ -21,6 +21,7 @@
+from vllm.sampling_params import SamplingParams
@@ -215,14 +216,70 @@ def test_replay_batch_keeps_device_decode_boundaries(state):
-    """Every prompt row of a prompt-logprobs request is read, so it never
-    trims; the other prefills still do."""
-    state._keeps_rows_np[1] = True
-    batch = _input_batch([1, 300, 300], [500, 300, 300], PREFILLING)
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -278,7 +278,11 @@ def add_request(self, req_index: int, new_req_data: NewRequestData) -> None:
-                params is not None and params.prompt_logprobs is not None
+                params is not None
+                and (
+                    params.prompt_logprobs is not None
+                    or params.prompt_logprob_token_ids is not None
+                )
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_replay_batch.py` modified +66/-9
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +5/-1
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_replay_batch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59611 - [Bugfix][DeepSeek V4] Load redundant EPLB expert slots

- Link: https://github.com/vllm-project/vllm/pull/59611
- Status/date: merged / 2026-10-20
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `9d4192aaa107`
- Diff scope read: GitHub Pull Request files API returned 7 files, +74/-1, 118 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DeepSeek V4] Load redundant EPLB expert slots"; model line: DeepSeek V4; category: bug fix; main diff: `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Bugfix][DeepSeek V4] Load redundant EPLB expert slots"; the main implementation surface is `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml` added +23/-0 (23 lines); hunks: -0,0 +1,23; `vllm/models/deepseek_v4/nvidia/model.py` modified +1/-0 (1 lines); hunks: -1204,6 +1204,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int,...; symbols: get_expert_mapping, finalize_mhc_broadcast_weights, touching `get_expert_mapping, finalize_mhc_broadcast_weights`; `vllm/models/deepseek_v41/nvidia/model.py` modified +1/-0 (1 lines); hunks: -1456,6 +1456,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int,...; symbols: get_expert_mapping, finalize_mhc_broadcast_weights, touching `get_expert_mapping, finalize_mhc_broadcast_weights`.
- Code diff details:
  - `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml` added +23/-0 (23 lines); hunks: -0,0 +1,23
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +1/-0 (1 lines); hunks: -1204,6 +1204,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int,...; symbols: get_expert_mapping, finalize_mhc_broadcast_weights
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +1/-0 (1 lines); hunks: -1456,6 +1456,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int,...; symbols: get_expert_mapping, finalize_mhc_broadcast_weights
- Key code excerpts:

```diff
diff -- tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml
@@ -0,0 +1,23 @@
+model_name: "deepseek-ai/DeepSeek-V4-Flash"
+accuracy_threshold: 0.92
+num_questions: 1319
+num_fewshot: 5
+startup_max_wait_seconds: 1800
+startup_rpc_checks:
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -1204,6 +1204,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
+            num_redundant_experts=first_layer.ffn.n_redundant_experts,
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -1456,6 +1456,7 @@ def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
+            num_redundant_experts=first_layer.ffn.n_redundant_experts,
```

- Reviewed files:
  - tests: `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml` added +23/-0
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +1/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml`, `tests/evals/gsm8k/configs/models-spec-decode.txt`, `tests/evals/gsm8k/eplb_checks.py`, `tests/evals/gsm8k/test_gsm8k_correctness.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62421 - [ROCm][Model] DeepSeek-V4.1 VL: stream language-model weights on ROCm

- Link: https://github.com/vllm-project/vllm/pull/62421
- Status/date: merged / 2026-10-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/vl_model.py`; associated commits `428cd0cb4a42`
- Diff scope read: GitHub Pull Request files API returned 4 files, +10/-10, 64 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Model] DeepSeek-V4.1 VL: stream language-model weights on ROCm"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v41/amd/vl_model.py`; technical summary: Covers "[ROCm][Model] DeepSeek-V4.1 VL: stream language-model weights on ROCm"; the main implementation surface is `vllm/models/deepseek_v41/amd/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-6 (10 lines); hunks: -41,6 +41,7; -335,12 +336,9 @@ def get_mtp_target_hidden_states(self) -> torch.Tensor | None:; symbols: get_mtp_target_hidden_states, load_weights, touching `get_mtp_target_hidden_states, load_weights`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-6 (10 lines); hunks: -41,6 +41,7; -335,12 +336,9 @@ def get_mtp_target_hidden_states(self) -> torch.Tensor | None:; symbols: get_mtp_target_hidden_states, load_weights
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/vl_model.py
@@ -41,6 +41,7 @@
+from vllm.models.deepseek_v4.common.vl_model import stream_language_model_first
@@ -335,12 +336,9 @@ def get_mtp_target_hidden_states(self) -> torch.Tensor | None:
-        # Map HF names into this wrapper's namespace up front and sort, so
-        # the "language_model." group reaches the child loader as one
-        # contiguous block (AutoWeightsLoader delegates per contiguous group,
-        # and the child's load_weights finalizes fused expert weights, which
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/vl_model.py` modified +4/-6
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_vl_stream_weights.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60731 - [ROCm][Perf][DSv4.1] Mono decode on MI300X and MI325X (gfx942)

- Link: https://github.com/vllm-project/vllm/pull/60731
- Status/date: merged / 2026-10-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/dspark.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/attention/device.py`, `vllm/models/deepseek_v41/amd/mono/attention/front.py` and 30 files; associated commits `1a74cc7bb24e`
- Diff scope read: GitHub Pull Request files API returned 45 files, +8040/-164, 9391 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Mono decode on MI300X and MI325X (gfx942)"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/ops/topk512_gfx942.cu`, `tests/kernels/models/amd/test_dsv41_mono_gfx942.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Mono decode on MI300X and MI325X (gfx942)"; the main implementation surface is `vllm/models/deepseek_v41/amd/ops/topk512_gfx942.cu`, `tests/kernels/models/amd/test_dsv41_mono_gfx942.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/ops/topk512_gfx942.cu` added +1517/-0 (1517 lines); hunks: -0,0 +1,1517; symbols: to, touching `to`; `tests/kernels/models/amd/test_dsv41_mono_gfx942.py` added +626/-0 (626 lines); hunks: -0,0 +1,626; symbols: _on_gfx942, _ld, _st, _rel_err, touching `_on_gfx942, _ld, _st`; `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +552/-41 (593 lines); hunks: -49,6 +49,13; -66,6 +73,7; symbols: put_mxfp8_group, ug_tile_task, stage_ug_tile, ug_pass, touching `put_mxfp8_group, ug_tile_task, stage_ug_tile`; `tests/models/test_dsv41_mono_decode.py` modified +367/-17 (384 lines); hunks: -1,10 +1,11; -31,8 +32,8 @@ def forward(self, *args, **kwargs):; symbols: forward, first_pre_mix, ffn, _run, touching `forward, first_pre_mix, ffn`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/ops/topk512_gfx942.cu` added +1517/-0 (1517 lines); hunks: -0,0 +1,1517; symbols: to
  - `tests/kernels/models/amd/test_dsv41_mono_gfx942.py` added +626/-0 (626 lines); hunks: -0,0 +1,626; symbols: _on_gfx942, _ld, _st, _rel_err
  - `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +552/-41 (593 lines); hunks: -49,6 +49,13; -66,6 +73,7; symbols: put_mxfp8_group, ug_tile_task, stage_ug_tile, ug_pass
  - `tests/models/test_dsv41_mono_decode.py` modified +367/-17 (384 lines); hunks: -1,10 +1,11; -31,8 +32,8 @@ def forward(self, *args, **kwargs):; symbols: forward, first_pre_mix, ffn, _run
  - `vllm/models/deepseek_v41/amd/ops/sparse_indexer.py` added +379/-0 (379 lines); hunks: -0,0 +1,379; symbols: Gfx942SparseAttnIndexer, forward_hip, gfx942_sparse_attn_indexer, _decode_step
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/ops/topk512_gfx942.cu
@@ -0,0 +1,1517 @@
+// SPDX-License-Identifier: Apache-2.0
+// SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+//
+// The sparse indexer's decode top-512 for gfx942 (MI300X and MI325X).
+//
+// The helpers, processHistogramStep and topKPerRowJob in namespace vllm are
diff -- tests/kernels/models/amd/test_dsv41_mono_gfx942.py
@@ -0,0 +1,626 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The gfx942 parts of the DeepSeek-V4.1 mono decode kernels
+(vllm/models/deepseek_v41/amd/mono) on the GPU.
+  key lists  keylist.launch, which writes K2's key lists on an index layer,
+             against a reference built in torch from its documented format.
diff -- vllm/models/deepseek_v41/amd/mono/stages/moe.py
@@ -49,6 +49,13 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/ops/topk512_gfx942.cu` added +1517/-0; `vllm/models/deepseek_v41/amd/mono/stages/moe.py` modified +552/-41; `vllm/models/deepseek_v41/amd/ops/sparse_indexer.py` added +379/-0; `vllm/models/deepseek_v41/amd/ops/fused_markov.py` added +340/-0; `vllm/models/deepseek_v41/amd/ops/topk.py` added +299/-0
  - tests: `tests/kernels/models/amd/test_dsv41_mono_gfx942.py` added +626/-0; `tests/models/test_dsv41_mono_decode.py` modified +367/-17; `tests/kernels/models/amd/test_dsv41_gfx942_topk.py` added +358/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/models/__init__.py`, `tests/kernels/models/amd/__init__.py`, `tests/kernels/models/amd/test_dsv41_gfx942_cand_logits.py`, `tests/kernels/models/amd/test_dsv41_gfx942_decode_meta.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62208 - [Bugfix][DeepSeek V4.1] Inject Engram at pipeline stage entry

- Link: https://github.com/vllm-project/vllm/pull/62208
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_pipeline.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `8a1c02efca9b`
- Diff scope read: GitHub Pull Request files API returned 3 files, +78/-1, 98 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DeepSeek V4.1] Inject Engram at pipeline stage entry"; model line: DeepSeek V4; category: bug fix; main diff: `tests/models/test_deepseek_v41_pipeline.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Bugfix][DeepSeek V4.1] Inject Engram at pipeline stage entry"; the main implementation surface is `tests/models/test_deepseek_v41_pipeline.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_pipeline.py` added +70/-0 (70 lines); hunks: -0,0 +1,70; symbols: test_stage_entry_injects_engram_before_mhc_pre, StopAfterMhcPre, Engram, __call__, touching `test_stage_entry_injects_engram_before_mhc_pre, StopAfterMhcPre, Engram`; `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-0 (6 lines); hunks: -542,6 +542,12 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `tests/models/test_deepseek_v41_pipeline.py` added +70/-0 (70 lines); hunks: -0,0 +1,70; symbols: test_stage_entry_injects_engram_before_mhc_pre, StopAfterMhcPre, Engram, __call__
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-0 (6 lines); hunks: -542,6 +542,12 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_pipeline.py
@@ -0,0 +1,70 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from importlib import import_module
+from types import SimpleNamespace
+import pytest
+import torch
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -542,6 +542,12 @@ def forward(
+                if self.engram is not None and engram_hashes is not None:
+                    residual = self.engram(
+                        residual,
+                        engram_hashes[:, self.engram.layer_hash_index],
+                        engram_mask,
+                    )
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_pipeline.py` added +70/-0
  - runtime: `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_pipeline.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62199 - [Bugfix][Frontend] Match DeepSeek-V4.1 encoder to the 1017 reference encoding

- Link: https://github.com/vllm-project/vllm/pull/62199
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_2.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_4.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_5.json` and 13 files; associated commits `ddefe40e16dd`
- Diff scope read: GitHub Pull Request files API returned 13 files, +417/-11, 508 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Frontend] Match DeepSeek-V4.1 encoder to the 1017 reference encoding"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json`, `tests/tokenizers_/test_deepseek_v41.py`; technical summary: Covers "[Bugfix][Frontend] Match DeepSeek-V4.1 encoder to the 1017 reference encoding"; the main implementation surface is `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json`, `tests/tokenizers_/test_deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json` added +93/-0 (93 lines); hunks: -0,0 +1,93; `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json` added +82/-0 (82 lines); hunks: -0,0 +1,82; `tests/tokenizers_/test_deepseek_v41.py` modified +74/-6 (80 lines); hunks: -17,6 +17,7; -28,16 +29,83 @@ def render(messages, **kwargs):; symbols: render, tool_call, test_reference_encoder_fixtures, test_drop_thinking_keeps_current_turn_across_tool_results, touching `render, tool_call, test_reference_encoder_fixtures`; `tests/tokenizers_/fixtures/deepseek_v41/test_input_5.json` added +39/-0 (39 lines); hunks: -0,0 +1,39.
- Code diff details:
  - `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json` added +93/-0 (93 lines); hunks: -0,0 +1,93
  - `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json` added +82/-0 (82 lines); hunks: -0,0 +1,82
  - `tests/tokenizers_/test_deepseek_v41.py` modified +74/-6 (80 lines); hunks: -17,6 +17,7; -28,16 +29,83 @@ def render(messages, **kwargs):; symbols: render, tool_call, test_reference_encoder_fixtures, test_drop_thinking_keeps_current_turn_across_tool_results
  - `tests/tokenizers_/fixtures/deepseek_v41/test_input_5.json` added +39/-0 (39 lines); hunks: -0,0 +1,39
  - `tests/tokenizers_/fixtures/deepseek_v41/test_output_3.txt` added +35/-0 (35 lines); hunks: -0,0 +1,35
- Key code excerpts:

```diff
diff -- tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json
@@ -0,0 +1,93 @@
+[
+  {
+    "role": "system",
+    "content": "该助手为DeepSeek，由深度求索公司创造。"
+  },
+  {
diff -- tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json
@@ -0,0 +1,82 @@
+{
+    "thinking_mode": "thinking",
+    "tools": [
+        {
+            "type": "function",
+            "function": {
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -17,6 +17,7 @@
```

- Reviewed files:
  - tests: `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json` added +93/-0; `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json` added +82/-0; `tests/tokenizers_/test_deepseek_v41.py` modified +74/-6; `tests/tokenizers_/fixtures/deepseek_v41/test_input_5.json` added +39/-0; `tests/tokenizers_/fixtures/deepseek_v41/test_output_3.txt` added +35/-0; `tests/tokenizers_/fixtures/deepseek_v41/test_input_4.json` added +28/-0
  - runtime: `vllm/tokenizers/deepseek_v41.py` modified +15/-1
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_2.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_4.json`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61345 - [ROCm][DSv4] Require explicit MXFP4 opt-in for MegaMoE shared-expert fusion

- Link: https://github.com/vllm-project/vllm/pull/61345
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`; associated commits `ffa18e55a466`
- Diff scope read: GitHub Pull Request files API returned 8 files, +137/-37, 384 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4] Require explicit MXFP4 opt-in for MegaMoE shared-expert fusion"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`; technical summary: Covers "[ROCm][DSv4] Require explicit MXFP4 opt-in for MegaMoE shared-expert fusion"; the main implementation surface is `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +37/-0 (37 lines); hunks: -6,14 +6,20; -136,6 +142,37 @@ def test_runtime_selected_by_max_tokens_across_dp(; symbols: test_runtime_selected_by_max_tokens_across_dp, test_mega_moe_shared_expert_fusion_requires_mxfp4_target, test_shared_expert_route_appended, touching `test_runtime_selected_by_max_tokens_across_dp, test_mega_moe_shared_expert_fusion_requires_mxfp4_target, test_shared_expert_route_appended`; `vllm/models/deepseek_v4/amd/model.py` modified +19/-6 (25 lines); hunks: -1,5 +1,6; -35,6 +36,7; symbols: __init__, touching `__init__`; `vllm/models/deepseek_v4/amd/mega_moe.py` modified +7/-13 (20 lines); hunks: -11,13 +11,12; -134,19 +133,14 @@ def weight_loader(; symbols: weight_loader, load_shared_expert, touching `weight_loader, load_shared_expert`.
- Code diff details:
  - `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +37/-0 (37 lines); hunks: -6,14 +6,20; -136,6 +142,37 @@ def test_runtime_selected_by_max_tokens_across_dp(; symbols: test_runtime_selected_by_max_tokens_across_dp, test_mega_moe_shared_expert_fusion_requires_mxfp4_target, test_shared_expert_route_appended
  - `vllm/models/deepseek_v4/amd/model.py` modified +19/-6 (25 lines); hunks: -1,5 +1,6; -35,6 +36,7; symbols: __init__
  - `vllm/models/deepseek_v4/amd/mega_moe.py` modified +7/-13 (20 lines); hunks: -11,13 +11,12; -134,19 +133,14 @@ def weight_loader(; symbols: weight_loader, load_shared_expert
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_aiter_mega_moe.py
@@ -6,14 +6,20 @@
+from vllm.config.quantization import QuantizationConfigArgs
+from vllm.model_executor.layers.quantization.online.base import OnlineQuantizationConfig
+from vllm.model_executor.layers.quantization.utils.config_utils import (
+    is_shared_expert_quant_fse_compatible,
+)
+from vllm.models.deepseek_v41.quant_config import DeepseekV4FP8Config
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -1,5 +1,6 @@
+import copy
@@ -35,6 +36,7 @@
+    resolve_layer_fused_shared_expert,
@@ -677,6 +679,21 @@ def __init__(
+        self.use_mega_moe = vllm_config.kernel_config.moe_backend == "aiter_mega_moe"
+        fuse_mega_moe_shared_expert = (
diff -- vllm/models/deepseek_v4/amd/mega_moe.py
@@ -11,13 +11,12 @@
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +37/-0
  - runtime: `vllm/models/deepseek_v4/amd/model.py` modified +19/-6; `vllm/models/deepseek_v4/amd/mega_moe.py` modified +7/-13
- Risk and verification: The diff ships test coverage in `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60118 - [Perf][DSv4.1] MegaAttn: wo_a writes wo_b's MXFP8 input

- Link: https://github.com/vllm-project/vllm/pull/60118
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; associated commits `018f5ff71aa9`
- Diff scope read: GitHub Pull Request files API returned 3 files, +110/-7, 180 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] MegaAttn: wo_a writes wo_b's MXFP8 input"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; technical summary: Covers "[Perf][DSv4.1] MegaAttn: wo_a writes wo_b's MXFP8 input"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +34/-5 (39 lines); hunks: -16,6 +16,7; -37,14 +38,15; symbols: _o_proj, _can_quantize_o_proj, touching `_o_proj, _can_quantize_o_proj`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +34/-5 (39 lines); hunks: -16,6 +16,7; -37,14 +38,15; symbols: _o_proj, _can_quantize_o_proj
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -16,6 +16,7 @@
+from functools import cached_property
@@ -37,14 +38,15 @@
+from vllm.models.deepseek_v41.common.ops.query_quant import can_fuse_query_quant
-from vllm.utils.math_utils import round_up
+from vllm.utils.math_utils import cdiv, round_up
@@ -221,19 +223,46 @@ def _o_proj(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +34/-5
- Risk and verification: The diff ships test coverage in `tests/kernels/test_dsv41_mega_attn_layouts.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62183 - [Feature][PCP] Support APC and encoder-side SWA bounded replay for DeepSeek-V4.1-Flash

- Link: https://github.com/vllm-project/vllm/pull/62183
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_replay_batch.py`, `tests/models/test_deepseek_v41_replay_start.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`; associated commits `fc47cc8fff82`
- Diff scope read: GitHub Pull Request files API returned 5 files, +31/-16, 131 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature][PCP] Support APC and encoder-side SWA bounded replay for DeepSeek-V4.1-Flash"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py`; technical summary: Covers "[Feature][PCP] Support APC and encoder-side SWA bounded replay for DeepSeek-V4.1-Flash"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +19/-9 (28 lines); hunks: -10,7 +10,7; -200,23 +200,22 @@ def __init__(; symbols: __init__, prepare_attn, touching `__init__, prepare_attn`; `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-3 (9 lines); hunks: -703,13 +703,16 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`; `vllm/models/deepseek_v41/attention.py` modified +3/-4 (7 lines); hunks: -546,12 +546,11 @@ def __init__(; symbols: __init__, touching `__init__`; `tests/models/test_deepseek_v41_replay_batch.py` modified +2/-0 (2 lines); hunks: -66,6 +66,7 @@ def state(monkeypatch):; -374,6 +375,7 @@ def launch(*args, **kwargs):; symbols: state, launch, touching `state, launch`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +19/-9 (28 lines); hunks: -10,7 +10,7; -200,23 +200,22 @@ def __init__(; symbols: __init__, prepare_attn
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-3 (9 lines); hunks: -703,13 +703,16 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
  - `vllm/models/deepseek_v41/attention.py` modified +3/-4 (7 lines); hunks: -546,12 +546,11 @@ def __init__(; symbols: __init__
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +2/-0 (2 lines); hunks: -66,6 +66,7 @@ def state(monkeypatch):; -374,6 +375,7 @@ def launch(*args, **kwargs):; symbols: state, launch
  - `tests/models/test_deepseek_v41_replay_start.py` modified +1/-0 (1 lines); hunks: -44,6 +44,7 @@ def state(monkeypatch):; symbols: state
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -10,7 +10,7 @@
-from vllm.distributed.parallel_state import get_dp_group, get_pp_group
+from vllm.distributed.parallel_state import get_dp_group, get_pcp_group, get_pp_group
@@ -200,23 +200,22 @@ def __init__(
+        self.pcp_size = vllm_config.parallel_config.prefill_context_parallel_size
+        max_local_reqs = self.max_num_reqs * (2 if self.pcp_size > 1 else 1)
-            max_num_reqs = self.max_num_reqs
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -703,13 +703,16 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
-            or vllm_config.cache_config.enable_prefix_caching
+            or (
+                vllm_config.cache_config.enable_prefix_caching
+                and not vllm_config.cache_config.swa_bounded_replay
+            )
-                "microbatching, speculative decoding, KV transfer, prefix "
diff -- vllm/models/deepseek_v41/attention.py
@@ -546,12 +546,11 @@ def __init__(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +19/-9; `vllm/models/deepseek_v41/nvidia/model.py` modified +6/-3; `vllm/models/deepseek_v41/attention.py` modified +3/-4
  - tests: `tests/models/test_deepseek_v41_replay_batch.py` modified +2/-0; `tests/models/test_deepseek_v41_replay_start.py` modified +1/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_replay_batch.py`, `tests/models/test_deepseek_v41_replay_start.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60792 - [Bugfix][Frontend] Align DeepSeek V4.1 images with rendered content

- Link: https://github.com/vllm-project/vllm/pull/60792
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_deepseek_v41.py`, `vllm/renderers/deepseek_v4.py`, `vllm/tokenizers/deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`; associated commits `3c8245b73dbc`
- Diff scope read: GitHub Pull Request files API returned 5 files, +159/-18, 304 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Frontend] Align DeepSeek V4.1 images with rendered content"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `vllm/tokenizers/deepseek_v41.py`; technical summary: Covers "[Bugfix][Frontend] Align DeepSeek V4.1 images with rendered content"; the main implementation surface is `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `vllm/tokenizers/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v41.py` modified +104/-0 (104 lines); hunks: -1,15 +1,23; -185,3 +193,99 @@ def image_part(color):; symbols: image_part, test_unsupported_media_is_a_request_error, render_with_media, run, touching `image_part, test_unsupported_media_is_a_request_error, render_with_media`; `vllm/tokenizers/deepseek_v41_encoding.py` modified +20/-1 (21 lines); hunks: -89,6 +89,7 @@ def merge_tool_messages(messages: List[Dict[str, Any]]) -> Lis...; -107,7 +108,13 @@ def merge_tool_messages(messages: List[Dict[str, Any]]) ->...; symbols: merge_tool_messages, render_message, encode_messages, touching `merge_tool_messages, render_message, encode_messages`; `vllm/tokenizers/deepseek_v41.py` modified +6/-0 (6 lines); hunks: -21,7 +21,9 @@ def _normalize_messages(; -36,6 +38,8 @@ def _normalize_messages(; symbols: _normalize_messages, apply_chat_template, touching `_normalize_messages, apply_chat_template`; `vllm/renderers/deepseek_v4.py` modified +28/-16 (44 lines); hunks: -34,7 +34,23 @@ def __init__(; -52,19 +68,13 @@ def render_messages(; symbols: __init__, _apply_chat_template, _build_prompt, render_completion_suffix, touching `__init__, _apply_chat_template, _build_prompt`.
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v41.py` modified +104/-0 (104 lines); hunks: -1,15 +1,23; -185,3 +193,99 @@ def image_part(color):; symbols: image_part, test_unsupported_media_is_a_request_error, render_with_media, run
  - `vllm/tokenizers/deepseek_v41_encoding.py` modified +20/-1 (21 lines); hunks: -89,6 +89,7 @@ def merge_tool_messages(messages: List[Dict[str, Any]]) -> Lis...; -107,7 +108,13 @@ def merge_tool_messages(messages: List[Dict[str, Any]]) ->...; symbols: merge_tool_messages, render_message, encode_messages
  - `vllm/tokenizers/deepseek_v41.py` modified +6/-0 (6 lines); hunks: -21,7 +21,9 @@ def _normalize_messages(; -36,6 +38,8 @@ def _normalize_messages(; symbols: _normalize_messages, apply_chat_template
  - `vllm/renderers/deepseek_v4.py` modified +28/-16 (44 lines); hunks: -34,7 +34,23 @@ def __init__(; -52,19 +68,13 @@ def render_messages(; symbols: __init__, _apply_chat_template, _build_prompt, render_completion_suffix
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -1,15 +1,23 @@
+import asyncio
+from types import SimpleNamespace
+from typing import cast
+from vllm.renderers.chat_utils import BaseMultiModalItemTracker
+from vllm.renderers.deepseek_v4 import DeepseekV4Renderer
+from vllm.renderers.params import ChatParams
diff -- vllm/tokenizers/deepseek_v41_encoding.py
@@ -89,6 +89,7 @@ def merge_tool_messages(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
+                "_image_indices": msg.get("_image_indices", []),
@@ -107,7 +108,13 @@ def merge_tool_messages(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
-                content_blocks = [{"type": "text", "text": msg.get("content", "")}]
+                content_blocks = [
+                    {
+                        "type": "text",
diff -- vllm/tokenizers/deepseek_v41.py
@@ -21,7 +21,9 @@ def _normalize_messages(
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v41.py` modified +104/-0
  - runtime: `vllm/tokenizers/deepseek_v41_encoding.py` modified +20/-1; `vllm/tokenizers/deepseek_v41.py` modified +6/-0; `vllm/renderers/deepseek_v4.py` modified +28/-16
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #62269 - [Bugfix][DSv4.1] Keep the Engram all-to-all buffers in one allocator

- Link: https://github.com/vllm-project/vllm/pull/62269
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/engram.py`; associated commits `ed871c91c749`
- Diff scope read: GitHub Pull Request files API returned 1 files, +4/-1, 19 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Keep the Engram all-to-all buffers in one allocator"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/common/engram.py`; technical summary: Covers "[Bugfix][DSv4.1] Keep the Engram all-to-all buffers in one allocator"; the main implementation surface is `vllm/models/deepseek_v41/common/engram.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/engram.py` modified +4/-1 (5 lines); hunks: -1410,6 +1410,9 @@ def __init__(self, layers: list["Engram"], max_tokens: int...; -1477,7 +1480,7 @@ def _stage(self, hashes: torch.Tensor, slot: int, peer: bo...; symbols: __init__, _stage, touching `__init__, _stage`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/engram.py` modified +4/-1 (5 lines); hunks: -1410,6 +1410,9 @@ def __init__(self, layers: list["Engram"], max_tokens: int...; -1477,7 +1480,7 @@ def _stage(self, hashes: torch.Tensor, slot: int, peer: bo...; symbols: __init__, _stage
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -1410,6 +1410,9 @@ def __init__(self, layers: list["Engram"], max_tokens: int) -> None:
+        # Same allocator as the send buffer: NCCL hangs this all-to-all when its
+        # buffers mix the cumem pool and the caching allocator.
+        self.exchanged_rows = torch.empty_like(self.packed_rows)
@@ -1477,7 +1480,7 @@ def _stage(self, hashes: torch.Tensor, slot: int, peer: bool) -> None:
-            sent, rows = rows, torch.empty_like(rows)
+            sent, rows = rows, self.exchanged_rows[: rows.shape[0]]
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/engram.py` modified +4/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/common/engram.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #62131 - [ROCm][Perf][DSv4.1] Mono decode for the DSpark draft layers

- Link: https://github.com/vllm-project/vllm/pull/62131
- Status/date: merged / 2026-10-19
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/mono/README.md`, `vllm/models/deepseek_v41/amd/mono/attention/front.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/runner.py`, `vllm/models/deepseek_v41/amd/mono_decode.py`; associated commits `e719b41e2233`
- Diff scope read: GitHub Pull Request files API returned 6 files, +251/-56, 607 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Mono decode for the DSpark draft layers"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/mono_decode.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/runner.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Mono decode for the DSpark draft layers"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono_decode.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/runner.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono_decode.py` modified +95/-22 (117 lines); hunks: -13,9 +13,10; -47,17 +48,41; symbols: _mono_runner, MonoDecodeLayer, __init__, touching `_mono_runner, MonoDecodeLayer, __init__`; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +52/-12 (64 lines); hunks: -25,15 +25,15; -64,21 +64,49 @@ class MonoBuild:; symbols: MonoBuild, _moe_key, _front_key, _symbol_params, touching `MonoBuild, _moe_key, _front_key`; `vllm/models/deepseek_v41/amd/mono/runner.py` modified +44/-16 (60 lines); hunks: -22,7 +22,7; -35,7 +35,7; symbols: MonoLayerWeights, check, DSV41MonoLayer, __init__, touching `MonoLayerWeights, check, DSV41MonoLayer`; `tests/models/test_dsv41_mono_decode.py` modified +53/-3 (56 lines); hunks: -22,9 +22,10; -86,6 +87,7 @@ def _run(; symbols: _Runner, __init__, forward, first_pre_mix, touching `_Runner, __init__, forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono_decode.py` modified +95/-22 (117 lines); hunks: -13,9 +13,10; -47,17 +48,41; symbols: _mono_runner, MonoDecodeLayer, __init__
  - `vllm/models/deepseek_v41/amd/mono/layer.py` modified +52/-12 (64 lines); hunks: -25,15 +25,15; -64,21 +64,49 @@ class MonoBuild:; symbols: MonoBuild, _moe_key, _front_key, _symbol_params
  - `vllm/models/deepseek_v41/amd/mono/runner.py` modified +44/-16 (60 lines); hunks: -22,7 +22,7; -35,7 +35,7; symbols: MonoLayerWeights, check, DSV41MonoLayer, __init__
  - `tests/models/test_dsv41_mono_decode.py` modified +53/-3 (56 lines); hunks: -22,9 +22,10; -86,6 +87,7 @@ def _run(; symbols: _Runner, __init__, forward, first_pre_mix
  - `vllm/models/deepseek_v41/amd/mono/attention/front.py` modified +4/-2 (6 lines); hunks: -106,6 +106,7 @@ class FrontBuild:; -202,8 +203,8 @@ def stage_kt(c, t):; symbols: FrontBuild, plus, stage_kt, front_context
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono_decode.py
@@ -13,9 +13,10 @@
-a whole layer also needs causal SWA windows. Anything else runs the layer as
-before; the paths share every tensor at the layer boundary, so they interleave
-freely.
+a whole layer also needs its SWA rows as the kernels read them (causal windows;
+for the DSpark draft's layers, the block's non-causal rows). Anything else runs
+the layer as before; the paths share every tensor at the layer boundary, so they
diff -- vllm/models/deepseek_v41/amd/mono/layer.py
@@ -25,15 +25,15 @@
-from .attention.plan import HIDDEN, Dims, back_scratch, front_scratch
+from .attention.plan import HIDDEN, WINDOW, Dims, back_scratch, front_scratch
-from .stages.moe_shape import SORT_NETS, MoeBuild, route_shape
+from .stages.moe_shape import EXPERTS, SORT_NETS, TOPK, MoeBuild, route_shape
@@ -64,21 +64,49 @@ class MonoBuild:
+    # a layer of the DSpark draft: its routed experts and top-k, the FP4 groups
diff -- vllm/models/deepseek_v41/amd/mono/runner.py
@@ -22,7 +22,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono_decode.py` modified +95/-22; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +52/-12; `vllm/models/deepseek_v41/amd/mono/runner.py` modified +44/-16; `vllm/models/deepseek_v41/amd/mono/attention/front.py` modified +4/-2; `vllm/models/deepseek_v41/amd/mono/README.md` modified +3/-1
  - tests: `tests/models/test_dsv41_mono_decode.py` modified +53/-3
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv41_mono_decode.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61819 - [ROCm][DSv4] Overlap the unfused shared expert with AITER MegaMoE

- Link: https://github.com/vllm-project/vllm/pull/61819
- Status/date: merged / 2026-10-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`; associated commits `e80b6c642f21`
- Diff scope read: GitHub Pull Request files API returned 2 files, +48/-7, 104 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4] Overlap the unfused shared expert with AITER MegaMoE"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/model.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`; technical summary: Covers "[ROCm][DSv4] Overlap the unfused shared expert with AITER MegaMoE"; the main implementation surface is `vllm/models/deepseek_v4/amd/model.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/model.py` modified +39/-6 (45 lines); hunks: -82,6 +82,8; -713,6 +715,18 @@ def __init__(; symbols: __init__, forward, _forward_mega_moe, _forward_mega_moe_routed, touching `__init__, forward, _forward_mega_moe`; `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +9/-1 (10 lines); hunks: -15,6 +15,7; -156,7 +157,10 @@ def test_shared_expert_route_appended(monkeypatch):; symbols: test_shared_expert_route_appended, test_mega_moe_routing_matches_reference, experts, touching `test_shared_expert_route_appended, test_mega_moe_routing_matches_reference, experts`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/model.py` modified +39/-6 (45 lines); hunks: -82,6 +82,8; -713,6 +715,18 @@ def __init__(; symbols: __init__, forward, _forward_mega_moe, _forward_mega_moe_routed
  - `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +9/-1 (10 lines); hunks: -15,6 +15,7; -156,7 +157,10 @@ def test_shared_expert_route_appended(monkeypatch):; symbols: test_shared_expert_route_appended, test_mega_moe_routing_matches_reference, experts
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -82,6 +82,8 @@
+from vllm.utils.multi_stream_utils import maybe_execute_in_parallel
+from vllm.utils.torch_utils import aux_stream
@@ -713,6 +715,18 @@ def __init__(
+            self.shared_experts_stream = (
+                aux_stream()
+                if self.shared_experts is not None
diff -- tests/models/test_deepseek_v4_aiter_mega_moe.py
@@ -15,6 +15,7 @@
+from vllm.utils.torch_utils import aux_stream
@@ -156,7 +157,10 @@ def test_shared_expert_route_appended(monkeypatch):
-def test_mega_moe_routing_matches_reference(monkeypatch, hash_routing, num_tokens):
+@pytest.mark.parametrize("shared_stream", [False, True])
+def test_mega_moe_routing_matches_reference(
+    monkeypatch, hash_routing, num_tokens, shared_stream
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/model.py` modified +39/-6
  - tests: `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +9/-1
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_aiter_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58857 - [Model] DeepSeek-V4/V4.1 VL: stream language-model weights instead of sorting the checkpoint

- Link: https://github.com/vllm-project/vllm/pull/58857
- Status/date: merged / 2026-10-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`; associated commits `026f6ab26893`
- Diff scope read: GitHub Pull Request files API returned 4 files, +103/-8, 148 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] DeepSeek-V4/V4.1 VL: stream language-model weights instead of sorting the checkpoint"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`; technical summary: Covers "[Model] DeepSeek-V4/V4.1 VL: stream language-model weights instead of sorting the checkpoint"; the main implementation surface is `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/vl_model.py` modified +19/-1 (20 lines); hunks: -79,6 +79,24 @@ def _make_deepseek_v4_vl_weights_mapper(; -334,7 +352,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: _make_deepseek_v4_vl_weights_mapper, stream_language_model_first, load_weights, touching `_make_deepseek_v4_vl_weights_mapper, stream_language_model_first, load_weights`; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-6 (10 lines); hunks: -41,6 +41,7; -317,12 +318,9 @@ def get_mtp_target_hidden_states(self) -> torch.Tensor | None:; symbols: get_mtp_target_hidden_states, load_weights, touching `get_mtp_target_hidden_states, load_weights`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/vl_model.py` modified +19/-1 (20 lines); hunks: -79,6 +79,24 @@ def _make_deepseek_v4_vl_weights_mapper(; -334,7 +352,7 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Te...; symbols: _make_deepseek_v4_vl_weights_mapper, stream_language_model_first, load_weights
  - `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-6 (10 lines); hunks: -41,6 +41,7; -317,12 +318,9 @@ def get_mtp_target_hidden_states(self) -> torch.Tensor | None:; symbols: get_mtp_target_hidden_states, load_weights
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/vl_model.py
@@ -79,6 +79,24 @@ def _make_deepseek_v4_vl_weights_mapper(
+def stream_language_model_first(
+    weights: Iterable[tuple[str, torch.Tensor]],
+) -> Iterable[tuple[str, torch.Tensor]]:
+    """Yield ``language_model.*`` weights as they arrive, then the rest.
+    Keeps the language model's weights in one contiguous group without
+    materializing the stream. Deferred weights are cloned so they do not keep
diff -- vllm/models/deepseek_v41/nvidia/vl_model.py
@@ -41,6 +41,7 @@
+from vllm.models.deepseek_v4.common.vl_model import stream_language_model_first
@@ -317,12 +318,9 @@ def get_mtp_target_hidden_states(self) -> torch.Tensor | None:
-        # Map HF names into this wrapper's namespace up front and sort, so
-        # the "language_model." group reaches the child loader as one
-        # contiguous block (AutoWeightsLoader delegates per contiguous group,
-        # and the child's load_weights finalizes fused expert weights, which
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/vl_model.py` modified +19/-1; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +4/-6
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_vl_stream_weights.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61960 - [CI][ROCm][Bugfix] DeepSeek V4.1: don't pass expert intermediate padding to AITER

- Link: https://github.com/vllm-project/vllm/pull/61960
- Status/date: merged / 2026-10-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v41/amd/model.py`; associated commits `a0e7137c4bb9`
- Diff scope read: GitHub Pull Request files API returned 2 files, +8/-0, 29 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI][ROCm][Bugfix] DeepSeek V4.1: don't pass expert intermediate padding to AITER"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v41/amd/model.py`; technical summary: Covers "[CI][ROCm][Bugfix] DeepSeek V4.1: don't pass expert intermediate padding to AITER"; the main implementation surface is `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v41/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/model.py` modified +4/-0 (4 lines); hunks: -578,6 +578,9 @@ def _validate_aiter_mega_moe_config(vllm_config: VllmConfig)...; -726,6 +729,7 @@ def __init__(; symbols: _validate_aiter_mega_moe_config, DeepseekV4MoE, __init__, touching `_validate_aiter_mega_moe_config, DeepseekV4MoE, __init__`; `vllm/models/deepseek_v41/amd/model.py` modified +4/-0 (4 lines); hunks: -77,6 +77,10; symbols: DeepseekV4MoE, __init__, touching `DeepseekV4MoE, __init__`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/model.py` modified +4/-0 (4 lines); hunks: -578,6 +578,9 @@ def _validate_aiter_mega_moe_config(vllm_config: VllmConfig)...; -726,6 +729,7 @@ def __init__(; symbols: _validate_aiter_mega_moe_config, DeepseekV4MoE, __init__
  - `vllm/models/deepseek_v41/amd/model.py` modified +4/-0 (4 lines); hunks: -77,6 +77,10; symbols: DeepseekV4MoE, __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -578,6 +578,9 @@ def _validate_aiter_mega_moe_config(vllm_config: VllmConfig) -> None:
+    # None: use the padding vLLM added.
+    experts_intermediate_pad: int | None = None
@@ -726,6 +729,7 @@ def __init__(
+            intermediate_pad=self.experts_intermediate_pad,
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -77,6 +77,10 @@
+    # TODO: revert once https://github.com/ROCm/aiter/pull/6598 is in the
+    # pinned AITER; with the padding set, its FlyDSL MoE can output NaN.
+    experts_intermediate_pad = 0
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/model.py` modified +4/-0; `vllm/models/deepseek_v41/amd/model.py` modified +4/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v41/amd/model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #59857 - [Feature][PCP] Add DeepSeek-V4.1-Flash support

- Link: https://github.com/vllm-project/vllm/pull/59857
- Status/date: merged / 2026-10-16
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v41/compressor.py` and 9 files; associated commits `fa75d3456d60`
- Diff scope read: GitHub Pull Request files API returned 15 files, +873/-37, 1444 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature][PCP] Add DeepSeek-V4.1-Flash support"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v41/compressor.py`, `tests/models/test_deepseek_v41_pcp.py`; technical summary: Covers "[Feature][PCP] Add DeepSeek-V4.1-Flash support"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v41/compressor.py`, `tests/models/test_deepseek_v41_pcp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +84/-13 (97 lines); hunks: -30,6 +30,8 @@ def fused_save_compress_norm(; -58,6 +60,11 @@ def fused_save_compress_norm(; symbols: fused_save_compress_norm, touching `fused_save_compress_norm`; `vllm/models/deepseek_v41/compressor.py` modified +92/-3 (95 lines); hunks: -8,13 +8,15; -36,6 +38,10 @@ def __init__(self):; symbols: __init__, get_name, supports_pcp, get_supported_kernel_block_sizes, touching `__init__, get_name, supports_pcp`; `tests/models/test_deepseek_v41_pcp.py` added +66/-0 (66 lines); hunks: -0,0 +1,66; symbols: test_pcp_gathers_routing_ids_once_after_local_input_preparation, touching `test_pcp_gathers_routing_ids_once_after_local_input_preparation`; `vllm/models/deepseek_v41/attention.py` modified +53/-8 (61 lines); hunks: -49,7 +49,7; -289,6 +289,7 @@ def __init__(; symbols: __init__, project_query_and_cache_kv, prepare_indexer, touching `__init__, project_query_and_cache_kv, prepare_indexer`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +84/-13 (97 lines); hunks: -30,6 +30,8 @@ def fused_save_compress_norm(; -58,6 +60,11 @@ def fused_save_compress_norm(; symbols: fused_save_compress_norm
  - `vllm/models/deepseek_v41/compressor.py` modified +92/-3 (95 lines); hunks: -8,13 +8,15; -36,6 +38,10 @@ def __init__(self):; symbols: __init__, get_name, supports_pcp, get_supported_kernel_block_sizes
  - `tests/models/test_deepseek_v41_pcp.py` added +66/-0 (66 lines); hunks: -0,0 +1,66; symbols: test_pcp_gathers_routing_ids_once_after_local_input_preparation
  - `vllm/models/deepseek_v41/attention.py` modified +53/-8 (61 lines); hunks: -49,7 +49,7; -289,6 +289,7 @@ def __init__(; symbols: __init__, project_query_and_cache_kv, prepare_indexer
  - `vllm/models/deepseek_v41/sparse_mla.py` modified +44/-1 (45 lines); hunks: -9,6 +9,7; -24,6 +25,7; symbols: DeepseekV41SparseSWAMetadataBuilder, __init__, build, DeepseekV4SparseMLABackend
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py
@@ -30,6 +30,8 @@ def fused_save_compress_norm(
+    prev_rows: torch.Tensor | None = None,
+    prev_row_indices: torch.Tensor | None = None,
@@ -58,6 +60,11 @@ def fused_save_compress_norm(
+        prev_rows: FP32 [rows, 1024] rows gathered from all PCP ranks (CR2). A
+            chunk reads its predecessor here where ``prev_row_indices`` is set,
+            and the ring is left to ``save_ring_rows``.
diff -- vllm/models/deepseek_v41/compressor.py
@@ -8,13 +8,15 @@
+from vllm.distributed import get_pcp_group
+    save_ring_rows,
@@ -36,6 +38,10 @@ def __init__(self):
+    @classmethod
+    def supports_pcp(cls) -> bool:
+        return True
diff -- tests/models/test_deepseek_v41_pcp.py
@@ -0,0 +1,66 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +84/-13; `vllm/models/deepseek_v41/compressor.py` modified +92/-3; `vllm/models/deepseek_v41/attention.py` modified +53/-8; `vllm/models/deepseek_v41/sparse_mla.py` modified +44/-1; `vllm/models/deepseek_v41/nvidia/model.py` modified +34/-0; `vllm/models/deepseek_v41/nvidia/model_state.py` modified +13/-5
  - tests: `tests/models/test_deepseek_v41_pcp.py` added +66/-0
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_engram.py`, `tests/models/test_deepseek_v41_pcp.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58872 - [Perf][DSv4.1] Split fused_wqa_wkv by token across TP ranks on SM90

- Link: https://github.com/vllm-project/vllm/pull/58872
- Status/date: merged / 2026-10-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `05ad0a8ace9b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +32/-1, 83 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Split fused_wqa_wkv by token across TP ranks on SM90"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py`; technical summary: Covers "[Perf][DSv4.1] Split fused_wqa_wkv by token across TP ranks on SM90"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model.py` modified +17/-0 (17 lines); hunks: -16,6 +16,7; -255,6 +256,21 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; symbols: _use_sequence_parallel, _shard_fused_wqa_wkv, maybe_init_gemm_rs, __init__, touching `_use_sequence_parallel, _shard_fused_wqa_wkv, maybe_init_gemm_rs`; `vllm/models/deepseek_v41/attention.py` modified +15/-1 (16 lines); hunks: -27,7 +27,11; -82,6 +86,10; symbols: _replace_layer_index, __init__, prepare_indexer, _fused_wqa_wkv_gemm, touching `_replace_layer_index, __init__, prepare_indexer`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +17/-0 (17 lines); hunks: -16,6 +16,7; -255,6 +256,21 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; symbols: _use_sequence_parallel, _shard_fused_wqa_wkv, maybe_init_gemm_rs, __init__
  - `vllm/models/deepseek_v41/attention.py` modified +15/-1 (16 lines); hunks: -27,7 +27,11; -82,6 +86,10; symbols: _replace_layer_index, __init__, prepare_indexer, _fused_wqa_wkv_gemm
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -16,6 +16,7 @@
+    get_tp_group,
@@ -255,6 +256,21 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:
+def _shard_fused_wqa_wkv(vllm_config: VllmConfig) -> bool:
+    """Whether large batches shard fused_wqa_wkv by token and all-gather the output."""
+    ca_comm = getattr(get_tp_group().device_communicator, "ca_comm", None)
+    return (
diff -- vllm/models/deepseek_v41/attention.py
@@ -27,7 +27,11 @@
-from vllm.models.common.ops.sequence_parallel import sp_reduce_scatter
+from vllm.models.common.ops.sequence_parallel import (
+    sp_all_gather,
+    sp_reduce_scatter,
+    sp_shard,
+)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model.py` modified +17/-0; `vllm/models/deepseek_v41/attention.py` modified +15/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #61371 - [Kernel][DSv4.1] Bump FlashMLA to the 2026.09.30 release and its interleaved V4.1 KV cache

- Link: https://github.com/vllm-project/vllm/pull/61371
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`; associated commits `f8460ef23659`
- Diff scope read: GitHub Pull Request files API returned 13 files, +259/-162, 757 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel][DSv4.1] Bump FlashMLA to the 2026.09.30 release and its interleaved V4.1 KV cache"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`; technical summary: Covers "[Kernel][DSv4.1] Bump FlashMLA to the 2026.09.30 release and its interleaved V4.1 KV cache"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` modified +22/-12 (34 lines); hunks: -122,10 +122,10 @@ def _fill_short_context_topk_indices(; -515,8 +515,8 @@ def __init__(; symbols: _fill_short_context_topk_indices, _use_v41_mxfp8_kv_record, __init__, get_kv_cache_spec, touching `_fill_short_context_topk_indices, _use_v41_mxfp8_kv_record, __init__`; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-20 (31 lines); hunks: -35,16 +35,17; -211,10 +212,8 @@ def _quantize_and_insert_k_mxfp8_kernel(; symbols: _quantize_and_insert_k_mxfp8_kernel, _dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel, touching `_quantize_and_insert_k_mxfp8_kernel, _dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel`; `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +11/-6 (17 lines); hunks: -51,6 +51,12 @@ def kernel(compile_key: CompileKey) -> Any:; -273,23 +279,22 @@ def host_entrypoint(; symbols: kernel, load_g2s, host_entrypoint, touching `kernel, load_g2s, host_entrypoint`; `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +7/-9 (16 lines); hunks: -239,7 +239,8 @@ def rope_quant_insert(; -390,8 +391,8 @@ def _rope_quant_insert_mxfp8_kernel(; symbols: rope_quant_insert, _rope_quant_insert_mxfp8_kernel, _rope_quant_insert_nvfp4_kernel, touching `rope_quant_insert, _rope_quant_insert_mxfp8_kernel, _rope_quant_insert_nvfp4_kernel`.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` modified +22/-12 (34 lines); hunks: -122,10 +122,10 @@ def _fill_short_context_topk_indices(; -515,8 +515,8 @@ def __init__(; symbols: _fill_short_context_topk_indices, _use_v41_mxfp8_kv_record, __init__, get_kv_cache_spec
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-20 (31 lines); hunks: -35,16 +35,17; -211,10 +212,8 @@ def _quantize_and_insert_k_mxfp8_kernel(; symbols: _quantize_and_insert_k_mxfp8_kernel, _dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel
  - `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +11/-6 (17 lines); hunks: -51,6 +51,12 @@ def kernel(compile_key: CompileKey) -> Any:; -273,23 +279,22 @@ def host_entrypoint(; symbols: kernel, load_g2s, host_entrypoint
  - `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +7/-9 (16 lines); hunks: -239,7 +239,8 @@ def rope_quant_insert(; -390,8 +391,8 @@ def _rope_quant_insert_mxfp8_kernel(; symbols: rope_quant_insert, _rope_quant_insert_mxfp8_kernel, _rope_quant_insert_nvfp4_kernel
  - `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +2/-3 (5 lines); hunks: -525,9 +525,8 @@ def _dequant(cache_2d):; symbols: _dequant
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -122,10 +122,10 @@ def _fill_short_context_topk_indices(
-# UE8M0 scale per 32 dims, 512 data bytes + 16 scale bytes per token, pages
-# rounded to the kernel's 512 B TMA stride -- only in its SM100 sparse-decode
-# kernels. Every other arch keeps the V4 record: 448 fp8 NoPE + 64 bf16 RoPE
-# plus 7 UE8M0 scales of 64 dims and a pad byte (584 B, 576 B pages).
+# UE8M0 scale per 32 dims, each token's 512 data bytes followed by its 16 scale
+# bytes -- only in its SM100 sparse-decode kernels. Every other arch keeps the
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -35,16 +35,17 @@
-# Per-token byte width of the two paged fp8 records. Both put a page's whole
-# data region ahead of its whole scale region, so ``k_cache.shape[-1]`` -- the
+# Per-token byte width of the paged records; ``k_cache.shape[-1]`` -- the
-#                 dims each plus a pad byte.
+#                 dims each plus a pad byte. A page puts its whole data region
+#                 ahead of its whole scale region.
diff -- vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py
@@ -51,6 +51,12 @@ def kernel(compile_key: CompileKey) -> Any:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` modified +22/-12; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +11/-20; `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +11/-6; `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +7/-9
  - tests: `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +2/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `tests/model_executor/layers/test_mla_short_prefill_indexer.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60282 - [ROCm] Support DeepSeek-V4 hash routing in AITER Triton W4A16 MoE

- Link: https://github.com/vllm-project/vllm/pull/60282
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/cpu/model.py`; associated commits `105605b8e998`
- Diff scope read: GitHub Pull Request files API returned 7 files, +122/-43, 318 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm] Support DeepSeek-V4 hash routing in AITER Triton W4A16 MoE"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/cpu/model.py`; technical summary: Covers "[ROCm] Support DeepSeek-V4 hash routing in AITER Triton W4A16 MoE"; the main implementation surface is `vllm/models/deepseek_v4/cpu/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/cpu/model.py` modified +0/-8 (8 lines); hunks: -214,14 +214,6 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/cpu/model.py` modified +0/-8 (8 lines); hunks: -214,14 +214,6 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/cpu/model.py
@@ -214,14 +214,6 @@ def __init__(
-        if is_hash_moe:
-            # apply_monolithic() never sees hash_indices_table via the
-            # router path (modular-only) -- stash it on RoutedExperts
-            # directly. object.__setattr__ avoids nn.Module re-registering
-            # (and duplicating in the state_dict) this alias.
-            object.__setattr__(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/cpu/model.py` modified +0/-8
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_topk_softplus_sqrt.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61643 - [Bugfix][MoE] Keep routing rows during DeepSeek V4.1 decoder replay

- Link: https://github.com/vllm-project/vllm/pull/61643
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`; associated commits `d12d5460a58b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +23/-1, 45 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][MoE] Keep routing rows during DeepSeek V4.1 decoder replay"; model line: DeepSeek V4; category: bug fix; main diff: `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`; technical summary: Covers "[Bugfix][MoE] Keep routing rows during DeepSeek V4.1 decoder replay"; the main implementation surface is `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_replay_batch.py` modified +22/-0 (22 lines); hunks: -63,6 +63,7 @@ def state(monkeypatch):; -195,6 +196,27 @@ def test_prompt_logprobs_requests_keep_their_rows(state):; symbols: state, test_prompt_logprobs_requests_keep_their_rows, test_aux_output_requests_keep_every_routing_row, test_replay_batch_keeps_adaptive_verification_query_bound, touching `state, test_prompt_logprobs_requests_keep_their_rows, test_aux_output_requests_keep_every_routing_row`; `vllm/models/deepseek_v41/nvidia/model_state.py` modified +1/-1 (2 lines); hunks: -273,7 +273,7 @@ def add_request(self, req_index: int, new_req_data: NewReque...; symbols: add_request, prepare_inputs, touching `add_request, prepare_inputs`.
- Code diff details:
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +22/-0 (22 lines); hunks: -63,6 +63,7 @@ def state(monkeypatch):; -195,6 +196,27 @@ def test_prompt_logprobs_requests_keep_their_rows(state):; symbols: state, test_prompt_logprobs_requests_keep_their_rows, test_aux_output_requests_keep_every_routing_row, test_replay_batch_keeps_adaptive_verification_query_bound
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +1/-1 (2 lines); hunks: -273,7 +273,7 @@ def add_request(self, req_index: int, new_req_data: NewReque...; symbols: add_request, prepare_inputs
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_replay_batch.py
@@ -63,6 +63,7 @@ def state(monkeypatch):
+    cfg.aux_output_config.enable_return_routed_experts = False
@@ -195,6 +196,27 @@ def test_prompt_logprobs_requests_keep_their_rows(state):
+@pytest.mark.parametrize("cg_mode", [CUDAGraphMode.NONE, CUDAGraphMode.PIECEWISE])
+def test_aux_output_requests_keep_every_routing_row(state, cg_mode):
+    """R3 needs every prefill row even when final logits only need the window."""
+    state.vllm_config.aux_output_config.enable_return_routed_experts = True
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -273,7 +273,7 @@ def add_request(self, req_index: int, new_req_data: NewRequestData) -> None:
-            )
+            ) or self.vllm_config.aux_output_config.enable_return_routed_experts
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_replay_batch.py` modified +22/-0
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_replay_batch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58689 - [ROCm][DSv4.1] Disambiguate ROCm attention class names

- Link: https://github.com/vllm-project/vllm/pull/58689
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/mono_decode.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`; associated commits `0951fc183cc7`
- Diff scope read: GitHub Pull Request files API returned 11 files, +86/-29, 315 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1] Disambiguate ROCm attention class names"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/mono_decode.py`; technical summary: Covers "[ROCm][DSv4.1] Disambiguate ROCm attention class names"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/mono_decode.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +15/-15 (30 lines); hunks: -280,7 +280,7 @@ def _copy_ragged_to_graph_buffers(; -303,7 +303,7 @@ def get_cudagraph_support(; symbols: _copy_ragged_to_graph_buffers, DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV41ROCMAiterSparseSWAMetadata, get_cudagraph_support, touching `_copy_ragged_to_graph_buffers, DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV41ROCMAiterSparseSWAMetadata`; `vllm/models/deepseek_v41/amd/model.py` modified +11/-3 (14 lines); hunks: -141,12 +141,20 @@ def __init__(; symbols: __init__, _select_dsv4_attn_cls, touching `__init__, _select_dsv4_attn_cls`; `vllm/models/deepseek_v41/amd/mono_decode.py` modified +2/-2 (4 lines); hunks: -39,7 +39,7; -301,7 +301,7 @@ def _decode_step(layer: "DeepseekV4DecoderLayer", rows: int):; symbols: _decode_step, touching `_decode_step`; `vllm/models/deepseek_v41/attention.py` modified +1/-1 (2 lines); hunks: -646,7 +646,7 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +15/-15 (30 lines); hunks: -280,7 +280,7 @@ def _copy_ragged_to_graph_buffers(; -303,7 +303,7 @@ def get_cudagraph_support(; symbols: _copy_ragged_to_graph_buffers, DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV41ROCMAiterSparseSWAMetadata, get_cudagraph_support
  - `vllm/models/deepseek_v41/amd/model.py` modified +11/-3 (14 lines); hunks: -141,12 +141,20 @@ def __init__(; symbols: __init__, _select_dsv4_attn_cls
  - `vllm/models/deepseek_v41/amd/mono_decode.py` modified +2/-2 (4 lines); hunks: -39,7 +39,7; -301,7 +301,7 @@ def _decode_step(layer: "DeepseekV4DecoderLayer", rows: int):; symbols: _decode_step
  - `vllm/models/deepseek_v41/attention.py` modified +1/-1 (2 lines); hunks: -646,7 +646,7 @@ def __init__(; symbols: __init__
  - `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` modified +2/-2 (4 lines); hunks: -67,7 +67,7 @@ def test_deepseek_rocm_adaptive_builders_support_varlen_full_g...; -126,7 +126,7 @@ def test_deepseek_v41_rocm_fixed_k_path_is_unchanged(; symbols: test_deepseek_rocm_adaptive_builders_support_varlen_full_graphs, test_deepseek_v41_rocm_fixed_k_path_is_unchanged
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -280,7 +280,7 @@ def _copy_ragged_to_graph_buffers(
-class DeepseekV4ROCMAiterSparseSWAMetadata(DeepseekSparseSWAMetadata):
+class DeepseekV41ROCMAiterSparseSWAMetadata(DeepseekSparseSWAMetadata):
@@ -303,7 +303,7 @@ def get_cudagraph_support(
-class DeepseekV4ROCMAiterSparseSWAMetadataBuilder(DeepseekV41SparseSWAMetadataBuilder):
+class DeepseekV41ROCMAiterSparseSWAMetadataBuilder(DeepseekV41SparseSWAMetadataBuilder):
@@ -348,7 +348,7 @@ def build(
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -141,12 +141,20 @@ def __init__(
-    if backend is not None and (
-        backend is not AttentionBackendEnum.ROCM_FLASHMLA_SPARSE_DSV4
+    if backend is not None and backend not in (
+        AttentionBackendEnum.ROCM_FLASHMLA_SPARSE_DSV4,
+        AttentionBackendEnum.ROCM_FLASHMLA_SPARSE_DSV41,
-            "use ROCM_FLASHMLA_SPARSE_DSV4."
diff -- vllm/models/deepseek_v41/amd/mono_decode.py
@@ -39,7 +39,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +15/-15; `vllm/models/deepseek_v41/amd/model.py` modified +11/-3; `vllm/models/deepseek_v41/amd/mono_decode.py` modified +2/-2; `vllm/models/deepseek_v41/attention.py` modified +1/-1
  - tests: `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61262 - [ROCm][DSv4] AITER MegaMoE Fixed-Slot Dispatch For DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/61262
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`; associated commits `e8e1e9619672`
- Diff scope read: GitHub Pull Request files API returned 3 files, +84/-8, 165 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4] AITER MegaMoE Fixed-Slot Dispatch For DeepSeek-V4"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/amd/mega_moe.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`; technical summary: Covers "[ROCm][DSv4] AITER MegaMoE Fixed-Slot Dispatch For DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/mega_moe.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/mega_moe.py` modified +54/-8 (62 lines); hunks: -10,6 +10,7; -20,7 +21,7; symbols: make_param, weight_loader, load_shared_expert, finalize_weights, touching `make_param, weight_loader, load_shared_expert`; `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +25/-0 (25 lines); hunks: -110,6 +110,31 @@ def test_experts_load_into_local_slots(monkeypatch):; symbols: test_experts_load_into_local_slots, test_runtime_selected_by_max_tokens_across_dp, test_shared_expert_route_appended, touching `test_experts_load_into_local_slots, test_runtime_selected_by_max_tokens_across_dp, test_shared_expert_route_appended`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/mega_moe.py` modified +54/-8 (62 lines); hunks: -10,6 +10,7; -20,7 +21,7; symbols: make_param, weight_loader, load_shared_expert, finalize_weights
  - `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +25/-0 (25 lines); hunks: -110,6 +110,31 @@ def test_experts_load_into_local_slots(monkeypatch):; symbols: test_experts_load_into_local_slots, test_runtime_selected_by_max_tokens_across_dp, test_shared_expert_route_appended
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/mega_moe.py
@@ -10,6 +10,7 @@
+from vllm.forward_context import get_forward_context, is_forward_context_available
@@ -20,7 +21,7 @@
-from vllm.utils.math_utils import next_power_of_2
+from vllm.utils.math_utils import next_power_of_2, prev_power_of_2
@@ -108,7 +109,8 @@ def make_param(rows: int, cols: int) -> nn.Parameter:
-        self._runtime: Any = None
diff -- tests/models/test_deepseek_v4_aiter_mega_moe.py
@@ -110,6 +110,31 @@ def test_experts_load_into_local_slots(monkeypatch):
+@pytest.mark.cpu_test
+@pytest.mark.parametrize(
+    "tokens_across_dp, expected",
+    [([4, 128], "decode"), ([4, 129], "prefill")],
+)
+def test_runtime_selected_by_max_tokens_across_dp(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/mega_moe.py` modified +54/-8
  - tests: `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +25/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_aiter_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56054 - [Bugfix][DSv4] Remap Quark MTP layer_quant_config onto draft prefixes

- Link: https://github.com/vllm-project/vllm/pull/56054
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/quant_config.py`; associated commits `365aaa77bd2e`
- Diff scope read: GitHub Pull Request files API returned 2 files, +37/-1, 72 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4] Remap Quark MTP layer_quant_config onto draft prefixes"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v4/amd/mtp.py`; technical summary: Covers "[Bugfix][DSv4] Remap Quark MTP layer_quant_config onto draft prefixes"; the main implementation surface is `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v4/amd/mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/quant_config.py` modified +30/-0 (30 lines); hunks: -21,11 +21,41; symbols: align_mtp_quant_config, DeepseekV4FP8Config, touching `align_mtp_quant_config, DeepseekV4FP8Config`; `vllm/models/deepseek_v4/amd/mtp.py` modified +7/-1 (8 lines); hunks: -39,11 +39,12; -289,10 +290,15 @@ def get_top_tokens(; symbols: get_top_tokens, DeepSeekV4MTP, __init__, touching `get_top_tokens, DeepSeekV4MTP, __init__`.
- Code diff details:
  - `vllm/models/deepseek_v4/quant_config.py` modified +30/-0 (30 lines); hunks: -21,11 +21,41; symbols: align_mtp_quant_config, DeepseekV4FP8Config
  - `vllm/models/deepseek_v4/amd/mtp.py` modified +7/-1 (8 lines); hunks: -39,11 +39,12; -289,10 +290,15 @@ def get_top_tokens(; symbols: get_top_tokens, DeepSeekV4MTP, __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/quant_config.py
@@ -21,11 +21,41 @@
+    from transformers import PreTrainedConfig
+    from vllm.model_executor.layers.quantization import QuantizationConfig
+def align_mtp_quant_config(
+    quant_config: QuantizationConfig | None, config: PreTrainedConfig
+) -> None:
+    """Re-key the quant config's MTP entries onto the draft module prefixes.
diff -- vllm/models/deepseek_v4/amd/mtp.py
@@ -39,11 +39,12 @@
+from vllm.models.deepseek_v4.quant_config import align_mtp_quant_config
-from .model import DeepseekV4DecoderLayer
+from .model import DeepseekV4DecoderLayer, DeepseekV4ForCausalLM
@@ -289,10 +290,15 @@ def get_top_tokens(
+    # The draft head reuses DeepseekV4DecoderLayer, so its fused linears must
+    # unfold to the same checkpoint shards for per-layer quant config lookup.
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/quant_config.py` modified +30/-0; `vllm/models/deepseek_v4/amd/mtp.py` modified +7/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/quant_config.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #61392 - [Chore] Use upstream Transformers DeepseekV4Config

- Link: https://github.com/vllm-project/vllm/pull/61392
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `tests/models/test_deepseek_v4_mega_moe.py`, `tests/transformers_utils/test_deepseek_v4_utils.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v4/amd/model.py` and 16 files; associated commits `b965ee564d18`
- Diff scope read: GitHub Pull Request files API returned 31 files, +156/-121, 737 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Chore] Use upstream Transformers DeepseekV4Config"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`; technical summary: Covers "[Chore] Use upstream Transformers DeepseekV4Config"; the main implementation surface is `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_deepseek_v4_vl.py` modified +17/-3 (20 lines); hunks: -3,13 +3,27; -34,7 +48,7 @@ def test_get_image_size_with_most_features_beats_wide_real_ima...; symbols: _ConfigCtx, test_get_image_size_with_most_features_beats_wide_real_image, test_get_image_size_with_most_features_respects_max_wh_ratio, touching `_ConfigCtx, test_get_image_size_with_most_features_beats_wide_real_image, test_get_image_size_with_most_features_respects_max_wh_ratio`; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +7/-4 (11 lines); hunks: -34,6 +34,7; -393,7 +394,9 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; symbols: get_warmup_keys, dispatch, touching `get_warmup_keys, dispatch`; `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py` modified +4/-4 (8 lines); hunks: -436,7 +436,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; -934,7 +934,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; symbols: get_warmup_keys, touching `get_warmup_keys`; `vllm/models/deepseek_v4/amd/model.py` modified +4/-1 (5 lines); hunks: -607,7 +607,10 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/models/multimodal/processing/test_deepseek_v4_vl.py` modified +17/-3 (20 lines); hunks: -3,13 +3,27; -34,7 +48,7 @@ def test_get_image_size_with_most_features_beats_wide_real_ima...; symbols: _ConfigCtx, test_get_image_size_with_most_features_beats_wide_real_image, test_get_image_size_with_most_features_respects_max_wh_ratio
  - `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +7/-4 (11 lines); hunks: -34,6 +34,7; -393,7 +394,9 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; symbols: get_warmup_keys, dispatch
  - `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py` modified +4/-4 (8 lines); hunks: -436,7 +436,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; -934,7 +934,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; symbols: get_warmup_keys
  - `vllm/models/deepseek_v4/amd/model.py` modified +4/-1 (5 lines); hunks: -607,7 +607,10 @@ def __init__(; symbols: __init__
  - `vllm/models/deepseek_v4/common/vl_model.py` modified +5/-0 (5 lines); hunks: -40,6 +40,7; -105,6 +106,10 @@ class DeepseekV4ForConditionalGeneration(; symbols: DeepseekV4ForConditionalGeneration, get_placeholder_str
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_deepseek_v4_vl.py
@@ -3,13 +3,27 @@
+from transformers import DeepseekV4Config
-from vllm.transformers_utils.configs.deepseek_v4 import DeepseekV4Config
+# Vision fields of deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
+VISION_CONFIG = dict(
+    vision_n_layers=24,
+    vision_dim=1024,
diff -- vllm/models/deepseek_v4/common/ops/cache_utils.py
@@ -34,6 +34,7 @@
+from vllm.transformers_utils.deepseek_v4_utils import get_compress_ratios
@@ -393,7 +394,9 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileKey]:
-            for compress_ratio in vllm_config.model_config.hf_config.compress_ratios
+            for compress_ratio in get_compress_ratios(
+                vllm_config.model_config.hf_config
+            )
diff -- vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py
@@ -436,7 +436,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileKey]:
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_deepseek_v4_vl.py` modified +17/-3; `tests/models/test_deepseek_v4_mega_moe.py` modified +2/-2
  - runtime: `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +7/-4; `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py` modified +4/-4; `vllm/models/deepseek_v4/amd/model.py` modified +4/-1; `vllm/models/deepseek_v4/common/vl_model.py` modified +5/-0; `vllm/models/deepseek_v4/cpu/model.py` modified +3/-1; `vllm/models/deepseek_v4/nvidia/model.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/config/test_model_arch_config.py`, `tests/distributed/test_eplb_spec_decode.py`, `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/multimodal/processing/test_deepseek_v4_vl.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61763 - [CI] Pin DeepSeek-V4.1-Flash-NVFP4 eval to its FP8-Engram revision

- Link: https://github.com/vllm-project/vllm/pull/61763
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`; associated commits `32feecd91f4c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-0, 11 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Pin DeepSeek-V4.1-Flash-NVFP4 eval to its FP8-Engram revision"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`; technical summary: Covers "[CI] Pin DeepSeek-V4.1-Flash-NVFP4 eval to its FP8-Engram revision"; the main implementation surface is `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` modified +3/-0 (3 lines); hunks: -7,7 +7,10 @@ min_acceptance_length: 2.5.
- Code diff details:
  - `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` modified +3/-0 (3 lines); hunks: -7,7 +7,10 @@ min_acceptance_length: 2.5
- Key code excerpts:

```diff
diff -- tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml
@@ -7,7 +7,10 @@ min_acceptance_length: 2.5
+# Pinned to the revision before the checkpoint stored its Engram tables as
+# MXFP4, which vLLM cannot load until #61530 lands. Unpin with #61530.
+  --revision 3431dde3247c13b5957f682b1e3c6fcae2566079
```

- Reviewed files:
  - tests: `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` modified +3/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58151 - [ROCm][DSv4.1] Enable DSpark adaptive verification

- Link: https://github.com/vllm-project/vllm/pull/58151
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `10d2c6083d3b`
- Diff scope read: GitHub Pull Request files API returned 5 files, +360/-26, 510 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1] Enable DSpark adaptive verification"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `vllm/models/deepseek_v41/amd/rocm.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`; technical summary: Covers "[ROCm][DSv4.1] Enable DSpark adaptive verification"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +33/-2 (35 lines); hunks: -8,6 +8,7; -41,6 +42,7; symbols: DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV41ROCMAiterMLASparseMetadataBuilder, get_cudagraph_support, DeepseekV4ROCMAiterSparseSWAMetadataBuilder, touching `DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV41ROCMAiterMLASparseMetadataBuilder, get_cudagraph_support`; `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` modified +52/-17 (69 lines); hunks: -10,6 +10,10; -51,7 +55,7 @@ def _make_indexer_builder(*, adaptive: bool, capacity: int = 12):; symbols: _make_indexer_builder, test_deepseek_v4_rocm_adaptive_builders_support_varlen_full_graphs, test_deepseek_rocm_adaptive_builders_support_varlen_full_graphs, touching `_make_indexer_builder, test_deepseek_v4_rocm_adaptive_builders_support_varlen_full_graphs, test_deepseek_rocm_adaptive_builders_support_varlen_full_graphs`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +33/-2 (35 lines); hunks: -8,6 +8,7; -41,6 +42,7; symbols: DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV41ROCMAiterMLASparseMetadataBuilder, get_cudagraph_support, DeepseekV4ROCMAiterSparseSWAMetadataBuilder
  - `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` modified +52/-17 (69 lines); hunks: -10,6 +10,10; -51,7 +55,7 @@ def _make_indexer_builder(*, adaptive: bool, capacity: int = 12):; symbols: _make_indexer_builder, test_deepseek_v4_rocm_adaptive_builders_support_varlen_full_graphs, test_deepseek_rocm_adaptive_builders_support_varlen_full_graphs
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -8,6 +8,7 @@
+from vllm.config import VllmConfig
@@ -41,6 +42,7 @@
+    AttentionCGSupport,
@@ -61,6 +63,7 @@
+from vllm.v1.kv_cache_interface import KVCacheSpec
@@ -285,7 +288,35 @@ class DeepseekV4ROCMAiterSparseSWAMetadata(DeepseekSparseSWAMetadata):
diff -- tests/v1/attention/test_deepseek_v4_rocm_adaptive.py
@@ -10,6 +10,10 @@
+from vllm.models.deepseek_v41.amd import rocm as v41_rocm
+from vllm.models.deepseek_v41.amd.rocm import (
+    DeepseekV41ROCMAiterMLASparseMetadataBuilder,
+)
@@ -51,7 +55,7 @@ def _make_indexer_builder(*, adaptive: bool, capacity: int = 12):
-def test_deepseek_v4_rocm_adaptive_builders_support_varlen_full_graphs():
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +33/-2
  - tests: `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` modified +52/-17
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57773 - [ROCm][Perf] Enable DPA+ETP prefill compute/comm dual-batch-overlap for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/57773
- Status/date: merged / 2026-10-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/model.py`; associated commits `f46021a7faa6`
- Diff scope read: GitHub Pull Request files API returned 9 files, +319/-28, 503 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Enable DPA+ETP prefill compute/comm dual-batch-overlap for DeepSeek-V4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][Perf] Enable DPA+ETP prefill compute/comm dual-batch-overlap for DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/model.py` modified +8/-1 (9 lines); hunks: -82,6 +82,7; -1228,7 +1229,13 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/model.py` modified +8/-1 (9 lines); hunks: -82,6 +82,7; -1228,7 +1229,13 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -82,6 +82,7 @@
+from vllm.v1.worker.ubatching import dbo_current_ubatch_token_offset
@@ -1228,7 +1229,13 @@ def forward(
-            self._mtp_hidden_buffer[:num_tokens].copy_(hidden_states.flatten(1))
+            # Each DBO ubatch owns a different slice of the batch. Writing
+            # from row 0 in both threads would let one ubatch clobber the
+            # other's rows in the buffer the MTP drafter reads after the step.
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/model.py` modified +8/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/moe/test_naive_dp_ep_dbo.py`, `tests/v1/worker/test_ubatch_offsets.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61378 - [ROCm][Perf] Enqueue the default chain first in CSA/HCA at small batch sizes for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/61378
- Status/date: merged / 2026-10-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `2521446ac8c9`
- Diff scope read: GitHub Pull Request files API returned 1 files, +14/-0, 42 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Enqueue the default chain first in CSA/HCA at small batch sizes for DeepSeek-V4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`; technical summary: Covers "[ROCm][Perf] Enqueue the default chain first in CSA/HCA at small batch sizes for DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-0 (14 lines); hunks: -162,6 +162,16 @@ def apply_pre_quantized_block_scaled_mm(; -807,6 +817,8 @@ def _prepare_and_attn(; symbols: apply_pre_quantized_block_scaled_mm, _default_first_token_threshold, _combine_topk_swa_indices_kernel, _prepare_and_attn, touching `apply_pre_quantized_block_scaled_mm, _default_first_token_threshold, _combine_topk_swa_indices_kernel`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-0 (14 lines); hunks: -162,6 +162,16 @@ def apply_pre_quantized_block_scaled_mm(; -807,6 +817,8 @@ def _prepare_and_attn(; symbols: apply_pre_quantized_block_scaled_mm, _default_first_token_threshold, _combine_topk_swa_indices_kernel, _prepare_and_attn
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -162,6 +162,16 @@ def apply_pre_quantized_block_scaled_mm(
+def _default_first_token_threshold() -> int:
+    """Max tokens at which the CSA/HCA fork enqueues the default chain first.
+    At small batches starting the long default chain first shortens the step
+    tail; larger batches saturate the device and aux-first is faster. Only
+    tuned on gfx950 (24 tokens = conc 8 with MTP=2); 0 disables elsewhere.
+    """
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +14/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #59709 - [Bugfix][DSv4] Don't bake the C128 compressor skip into CUDA graphs

- Link: https://github.com/vllm-project/vllm/pull/59709
- Status/date: merged / 2026-10-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/compressor.py`; associated commits `877f6df88917`
- Diff scope read: GitHub Pull Request files API returned 2 files, +81/-3, 109 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4] Don't bake the C128 compressor skip into CUDA graphs"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/compressor.py`; technical summary: Covers "[Bugfix][DSv4] Don't bake the C128 compressor skip into CUDA graphs"; the main implementation surface is `vllm/models/deepseek_v4/compressor.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/compressor.py` modified +3/-3 (6 lines); hunks: -7,7 +7,7; -409,12 +409,12 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/compressor.py` modified +3/-3 (6 lines); hunks: -7,7 +7,7; -409,12 +409,12 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/compressor.py
@@ -7,7 +7,7 @@
-from vllm.config import CUDAGraphMode, VllmConfig, get_current_vllm_config
+from vllm.config import VllmConfig, get_current_vllm_config
@@ -409,12 +409,12 @@ def forward(
-        # full graph cannot branch on per-step CPU metadata after capture
+        # A captured graph would replay the capture batch's skip decision.
-            and forward_context.cudagraph_runtime_mode != CUDAGraphMode.FULL
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/compressor.py` modified +3/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59039 - [ROCm][Perf][DSv4.1] Enable decoder SWA bounded replay

- Link: https://github.com/vllm-project/vllm/pull/59039
- Status/date: merged / 2026-10-13
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_amd_replay_forward.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/attention.py` and 6 files; associated commits `c077dc663d92`
- Diff scope read: GitHub Pull Request files API returned 7 files, +705/-43, 866 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Enable decoder SWA bounded replay"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v41_amd_replay_forward.py`, `vllm/models/deepseek_v41/amd/model.py`, `tests/models/test_deepseek_v41_replay_batch.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Enable decoder SWA bounded replay"; the main implementation surface is `tests/models/test_deepseek_v41_amd_replay_forward.py`, `vllm/models/deepseek_v41/amd/model.py`, `tests/models/test_deepseek_v41_replay_batch.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_amd_replay_forward.py` added +329/-0 (329 lines); hunks: -0,0 +1,329; symbols: _RocmKvInsert, __init__, write, assert_matches_forward, touching `_RocmKvInsert, __init__, write`; `vllm/models/deepseek_v41/amd/model.py` modified +271/-20 (291 lines); hunks: -62,6 +62,7; -411,6 +412,42 @@ def forward(; symbols: forward, write_kv, DeepseekV4Model, __init__, touching `forward, write_kv, DeepseekV4Model`; `tests/models/test_deepseek_v41_replay_batch.py` modified +75/-0 (75 lines); hunks: -290,6 +290,81 @@ def test_idle_dp_rank_dummy_trims_with_its_peers(dp_state):; symbols: test_idle_dp_rank_dummy_trims_with_its_peers, test_zero_prefix_window_warms_gather_and_skips_pad, pad_warmup, gather_warmup, touching `test_idle_dp_rank_dummy_trims_with_its_peers, test_zero_prefix_window_warms_gather_and_skips_pad, pad_warmup`; `vllm/models/deepseek_v41/nvidia/model_state.py` modified +17/-17 (34 lines); hunks: -337,7 +337,7 @@ def prepare_attn(; -349,7 +349,7 @@ def prepare_attn(; symbols: prepare_attn, _warm_up_replay_kernels, touching `prepare_attn, _warm_up_replay_kernels`.
- Code diff details:
  - `tests/models/test_deepseek_v41_amd_replay_forward.py` added +329/-0 (329 lines); hunks: -0,0 +1,329; symbols: _RocmKvInsert, __init__, write, assert_matches_forward
  - `vllm/models/deepseek_v41/amd/model.py` modified +271/-20 (291 lines); hunks: -62,6 +62,7; -411,6 +412,42 @@ def forward(; symbols: forward, write_kv, DeepseekV4Model, __init__
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +75/-0 (75 lines); hunks: -290,6 +290,81 @@ def test_idle_dp_rank_dummy_trims_with_its_peers(dp_state):; symbols: test_idle_dp_rank_dummy_trims_with_its_peers, test_zero_prefix_window_warms_gather_and_skips_pad, pad_warmup, gather_warmup
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +17/-17 (34 lines); hunks: -337,7 +337,7 @@ def prepare_attn(; -349,7 +349,7 @@ def prepare_attn(; symbols: prepare_attn, _warm_up_replay_kernels
  - `vllm/models/deepseek_v41/attention.py` modified +5/-5 (10 lines); hunks: -547,11 +547,11 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_amd_replay_forward.py
@@ -0,0 +1,329 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""What the AMD replay forward does with a prefill longer than the window.
+The cut in this fixture is layer 1, so replay starts at layer 1. That is the
+same boundary as production layer 20, on a 4-layer stand-in. The final
+``mhc_post`` and the aux capture at that cut both run on the window rows.
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -62,6 +62,7 @@
+from vllm.models.deepseek_v41.decoder_replay_layers import DecoderReplayLayers
@@ -411,6 +412,42 @@ def forward(
+    def write_kv(
+        self,
+        x: torch.Tensor,
+        positions: torch.Tensor,
diff -- tests/models/test_deepseek_v41_replay_batch.py
@@ -290,6 +290,81 @@ def test_idle_dp_rank_dummy_trims_with_its_peers(dp_state):
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_amd_replay_forward.py` added +329/-0; `tests/models/test_deepseek_v41_replay_batch.py` modified +75/-0
  - runtime: `vllm/models/deepseek_v41/amd/model.py` modified +271/-20; `vllm/models/deepseek_v41/nvidia/model_state.py` modified +17/-17; `vllm/models/deepseek_v41/attention.py` modified +5/-5; `vllm/models/deepseek_v41/amd/vl_model.py` modified +5/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_amd_replay_forward.py`, `tests/models/test_deepseek_v41_replay_batch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61082 - [ROCm][Perf][DSv4.1] Mono decode on every backbone layer

- Link: https://github.com/vllm-project/vllm/pull/61082
- Status/date: merged / 2026-10-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/mono/README.md`, `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/attention/front.py`, `vllm/models/deepseek_v41/amd/mono/layer.py` and 8 files; associated commits `cc2a6eea1a9f`
- Diff scope read: GitHub Pull Request files API returned 13 files, +379/-111, 1026 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Mono decode on every backbone layer"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/mono_decode.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `tests/models/test_dsv41_mono_decode.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Mono decode on every backbone layer"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono_decode.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `tests/models/test_dsv41_mono_decode.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono_decode.py` modified +87/-28 (115 lines); hunks: -1,15 +1,16; -20,7 +21,7; symbols: _mono_runner, _unsupported_moe, _select, MonoDecodeLayer, touching `_mono_runner, _unsupported_moe, _select`; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +81/-3 (84 lines); hunks: -58,6 +58,12 @@ class MonoBuild:; -100,6 +106,7 @@ def place(regions):; symbols: MonoBuild, _moe_key, place, K1Lds, touching `MonoBuild, _moe_key, place`; `tests/models/test_dsv41_mono_decode.py` modified +69/-14 (83 lines); hunks: -27,21 +27,25 @@ def forward(self, *args, **kwargs):; -77,7 +81,12 @@ def run(monkeypatch):; symbols: forward, first_pre_mix, ffn, _layer, touching `forward, first_pre_mix, ffn`; `vllm/models/deepseek_v41/amd/mono/runner.py` modified +33/-6 (39 lines); hunks: -16,12 +16,13; -170,6 +171,12 @@ def __init__(self, tp: int, rank: int, group, device: torch...; symbols: __init__, scratch, first_pre_mix, supports, touching `__init__, scratch, first_pre_mix`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono_decode.py` modified +87/-28 (115 lines); hunks: -1,15 +1,16; -20,7 +21,7; symbols: _mono_runner, _unsupported_moe, _select, MonoDecodeLayer
  - `vllm/models/deepseek_v41/amd/mono/layer.py` modified +81/-3 (84 lines); hunks: -58,6 +58,12 @@ class MonoBuild:; -100,6 +106,7 @@ def place(regions):; symbols: MonoBuild, _moe_key, place, K1Lds
  - `tests/models/test_dsv41_mono_decode.py` modified +69/-14 (83 lines); hunks: -27,21 +27,25 @@ def forward(self, *args, **kwargs):; -77,7 +81,12 @@ def run(monkeypatch):; symbols: forward, first_pre_mix, ffn, _layer
  - `vllm/models/deepseek_v41/amd/mono/runner.py` modified +33/-6 (39 lines); hunks: -16,12 +16,13; -170,6 +171,12 @@ def __init__(self, tp: int, rank: int, group, device: torch...; symbols: __init__, scratch, first_pre_mix, supports
  - `vllm/models/deepseek_v41/amd/mono/attention/front.py` modified +23/-5 (28 lines); hunks: -188,6 +188,8 @@ def stage_kt(c, t):; -212,10 +214,10 @@ def stage_kt(c, t):; symbols: stage_kt, stage_qkv, run_front
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono_decode.py
@@ -1,15 +1,16 @@
-"""DeepSeek-V4.1 mono decode layer on ROCm CDNA4 (``VLLM_ROCM_MONO_DECODE=1``).
+"""DeepSeek-V4.1 mono decode layer on ROCm CDNA4 (``--monokernel``).
-weights, the TP reductions inside the kernels. A layer runs whole when it has
-the standard seam and no compressor or indexer of its own (compress ratio 1 or
-2) over ``fp8_ds_mla`` records. Any other backbone layer (the first, the Engram
-layers, the compressor / indexer layers) keeps vLLM's attention seam and
diff -- vllm/models/deepseek_v41/amd/mono/layer.py
@@ -58,6 +58,12 @@ class MonoBuild:
+    # K1's seam folds the previous layer's output into the residual; off for a
+    # residual that arrives settled (the first layer, after an Engram)
+    fold: bool = True
+    # the layer selects its own top-k (an index source): K1 hands its normed
+    # input and qr out for vLLM's indexer, K2 builds the key table
+    index: bool = False
diff -- tests/models/test_dsv41_mono_decode.py
@@ -27,21 +27,25 @@ def forward(self, *args, **kwargs):
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono_decode.py` modified +87/-28; `vllm/models/deepseek_v41/amd/mono/layer.py` modified +81/-3; `vllm/models/deepseek_v41/amd/mono/runner.py` modified +33/-6; `vllm/models/deepseek_v41/amd/mono/attention/front.py` modified +23/-5; `vllm/models/deepseek_v41/amd/mono/stages/seam.py` modified +15/-9; `vllm/models/deepseek_v41/amd/mono/README.md` modified +13/-10
  - tests: `tests/models/test_dsv41_mono_decode.py` modified +69/-14
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv41_mono_decode.py`, `tests/models/test_dsv41_mono_layers.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61041 - [Bugfix][DSv4.1] Match decoder-replay input_ids dtype for FlashInfer MegaMoE

- Link: https://github.com/vllm-project/vllm/pull/61041
- Status/date: merged / 2026-10-12
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`; associated commits `ffec221276fa`
- Diff scope read: GitHub Pull Request files API returned 2 files, +19/-5, 66 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Match decoder-replay input_ids dtype for FlashInfer MegaMoE"; model line: DeepSeek V4; category: bug fix; main diff: `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`; technical summary: Covers "[Bugfix][DSv4.1] Match decoder-replay input_ids dtype for FlashInfer MegaMoE"; the main implementation surface is `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +15/-2 (17 lines); hunks: -8,6 +8,7; -144,8 +145,18 @@ def test_piecewise_graphs_break_out_by_size():; symbols: test_piecewise_graphs_break_out_by_size, test_replay_graph_matches_eager, run_layers, touching `test_piecewise_graphs_break_out_by_size, test_replay_graph_matches_eager, run_layers`; `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` modified +4/-3 (7 lines); hunks: -10,7 +10,7; -56,8 +56,9 @@ def __init__(self, vllm_config: VllmConfig, device, layers: De...; symbols: __init__, touching `__init__`.
- Code diff details:
  - `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +15/-2 (17 lines); hunks: -8,6 +8,7; -144,8 +145,18 @@ def test_piecewise_graphs_break_out_by_size():; symbols: test_piecewise_graphs_break_out_by_size, test_replay_graph_matches_eager, run_layers
  - `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` modified +4/-3 (7 lines); hunks: -10,7 +10,7; -56,8 +56,9 @@ def __init__(self, vllm_config: VllmConfig, device, layers: De...; symbols: __init__
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_decoder_replay_layers.py
@@ -8,6 +8,7 @@
+from vllm.config.kernel import FLASHINFER_MOE_EP_BACKENDS, NATIVE_MEGA_MOE_BACKENDS
@@ -144,8 +145,18 @@ def test_piecewise_graphs_break_out_by_size():
-def test_replay_graph_matches_eager(monkeypatch):
-    """The replay graph of the next captured size pads and runs the rows."""
+@pytest.mark.parametrize(
+    ("moe_backend", "ids_dtype"),
diff -- vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py
@@ -10,7 +10,7 @@
-from vllm.config.kernel import MEGA_MOE_BACKENDS
+from vllm.config.kernel import NATIVE_MEGA_MOE_BACKENDS
@@ -56,8 +56,9 @@ def __init__(self, vllm_config: VllmConfig, device, layers: DecoderReplayLayers)
-        mega_moe = vllm_config.kernel_config.moe_backend in MEGA_MOE_BACKENDS
-        ids = torch.int64 if mega_moe else torch.int32
+        # DeepseekV4Model.forward casts input_ids to int64 for native MegaMoE only.
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +15/-2
  - runtime: `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` modified +4/-3
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_decoder_replay_layers.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57549 - [EPLB] Add EPLB support to dspark draft models (DeepSeekV4)

- Link: https://github.com/vllm-project/vllm/pull/57549
- Status/date: merged / 2026-10-12
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/common/eplb_util.py`, `vllm/models/deepseek_v4/nvidia/dspark.py`, `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `a281ad32f036`
- Diff scope read: GitHub Pull Request files API returned 12 files, +665/-76, 1058 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[EPLB] Add EPLB support to dspark draft models (DeepSeekV4)"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/common/eplb_util.py`, `vllm/models/deepseek_v4/nvidia/model.py`; technical summary: Covers "[EPLB] Add EPLB support to dspark draft models (DeepSeekV4)"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/common/eplb_util.py`, `vllm/models/deepseek_v4/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +95/-0 (95 lines); hunks: -15,6 +15,10; -28,6 +32,7; symbols: test_deepseek_v4_drafter_pwal_hooks_finalize_mega_moe, v4_dspark_config, test_dspark_draft_registers_mixture_of_experts, touching `test_deepseek_v4_drafter_pwal_hooks_finalize_mega_moe, v4_dspark_config, test_dspark_draft_registers_mixture_of_experts`; `vllm/models/deepseek_v4/common/eplb_util.py` added +50/-0 (50 lines); hunks: -0,0 +1,50; symbols: dspark_draft_supports_eplb, collect_moe_layers, touching `dspark_draft_supports_eplb, collect_moe_layers`; `vllm/models/deepseek_v4/nvidia/model.py` modified +8/-17 (25 lines); hunks: -81,6 +81,7; -1841,23 +1842,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: s...; symbols: __init__, set_moe_parameters, embed_input_ids, touching `__init__, set_moe_parameters, embed_input_ids`; `vllm/models/deepseek_v4/nvidia/dspark.py` modified +15/-1 (16 lines); hunks: -52,11 +52,14; -346,7 +349,7 @@ def _insert_context_kv(; symbols: _insert_context_kv, DSparkDeepseekV4ForCausalLM, __init__, set_moe_parameters, touching `_insert_context_kv, DSparkDeepseekV4ForCausalLM, __init__`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +95/-0 (95 lines); hunks: -15,6 +15,10; -28,6 +32,7; symbols: test_deepseek_v4_drafter_pwal_hooks_finalize_mega_moe, v4_dspark_config, test_dspark_draft_registers_mixture_of_experts
  - `vllm/models/deepseek_v4/common/eplb_util.py` added +50/-0 (50 lines); hunks: -0,0 +1,50; symbols: dspark_draft_supports_eplb, collect_moe_layers
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +8/-17 (25 lines); hunks: -81,6 +81,7; -1841,23 +1842,13 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: s...; symbols: __init__, set_moe_parameters, embed_input_ids
  - `vllm/models/deepseek_v4/nvidia/dspark.py` modified +15/-1 (16 lines); hunks: -52,11 +52,14; -346,7 +349,7 @@ def _insert_context_kv(; symbols: _insert_context_kv, DSparkDeepseekV4ForCausalLM, __init__, set_moe_parameters
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -15,6 +15,10 @@
+from vllm.model_executor.models.interfaces import (
+    get_mixture_of_experts_model,
+    is_mixture_of_experts,
+)
@@ -28,6 +32,7 @@
+from vllm.transformers_utils.configs.deepseek_v4 import DeepseekV4Config
diff -- vllm/models/deepseek_v4/common/eplb_util.py
@@ -0,0 +1,50 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Shared EPLB MoE registration helpers for DeepSeek V4 family models."""
+from collections.abc import Iterable
+from typing import Any
+import torch.nn as nn
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -81,6 +81,7 @@
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +95/-0
  - runtime: `vllm/models/deepseek_v4/common/eplb_util.py` added +50/-0; `vllm/models/deepseek_v4/nvidia/model.py` modified +8/-17; `vllm/models/deepseek_v4/nvidia/dspark.py` modified +15/-1
- Risk and verification: The diff ships test coverage in `tests/distributed/test_eplb_spec_decode.py`, `tests/models/test_deepseek_v4_mega_moe.py`, `tests/models/test_dspark_mla.py`, `tests/v1/worker/test_dspark_utils.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #61004 - [ROCm][DSv4] Fuse the shared expert into AITER MegaMoE

- Link: https://github.com/vllm-project/vllm/pull/61004
- Status/date: merged / 2026-10-12
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`; associated commits `e3bbaf23695f`
- Diff scope read: GitHub Pull Request files API returned 5 files, +151/-12, 289 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4] Fuse the shared expert into AITER MegaMoE"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/mega_moe.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][DSv4] Fuse the shared expert into AITER MegaMoE"; the main implementation surface is `vllm/models/deepseek_v4/amd/mega_moe.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/mega_moe.py` modified +109/-8 (117 lines); hunks: -10,10 +10,51; -28,16 +69,25 @@ def __init__(; symbols: _append_shared_expert_kernel, DeepseekV4AiterMegaMoEExperts, __init__, weight_loader, touching `_append_shared_expert_kernel, DeepseekV4AiterMegaMoEExperts, __init__`; `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +20/-0 (20 lines); hunks: -29,6 +29,7 @@ def _make_experts(; -47,6 +48,7 @@ def _make_experts(; symbols: _make_experts, test_experts_load_into_local_slots, test_shared_expert_route_appended, touching `_make_experts, test_experts_load_into_local_slots, test_shared_expert_route_appended`; `vllm/models/deepseek_v4/amd/model.py` modified +10/-3 (13 lines); hunks: -74,7 +74,10; -690,6 +693,10 @@ def __init__(; symbols: __init__, load_weights, process_weights_after_loading, touching `__init__, load_weights, process_weights_after_loading`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/mega_moe.py` modified +109/-8 (117 lines); hunks: -10,10 +10,51; -28,16 +69,25 @@ def __init__(; symbols: _append_shared_expert_kernel, DeepseekV4AiterMegaMoEExperts, __init__, weight_loader
  - `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +20/-0 (20 lines); hunks: -29,6 +29,7 @@ def _make_experts(; -47,6 +48,7 @@ def _make_experts(; symbols: _make_experts, test_experts_load_into_local_slots, test_shared_expert_route_appended
  - `vllm/models/deepseek_v4/amd/model.py` modified +10/-3 (13 lines); hunks: -74,7 +74,10; -690,6 +693,10 @@ def __init__(; symbols: __init__, load_weights, process_weights_after_loading
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/mega_moe.py
@@ -10,10 +10,51 @@
+from vllm.model_executor.layers.quantization.utils.fp8_utils import (
+    get_fp8_block_weight_scale,
+)
+from vllm.model_executor.layers.quantization.utils.mxfp4_utils import mxfp4_quantize
+from vllm.model_executor.layers.quantization.utils.quant_utils import (
+    GroupShape,
diff -- tests/models/test_deepseek_v4_aiter_mega_moe.py
@@ -29,6 +29,7 @@ def _make_experts(
+    fuse_shared_expert=False,
@@ -47,6 +48,7 @@ def _make_experts(
+        fuse_shared_expert=fuse_shared_expert,
@@ -108,6 +110,24 @@ def test_experts_load_into_local_slots(monkeypatch):
+@pytest.mark.skipif(not current_platform.is_rocm(), reason="Requires ROCm")
+def test_shared_expert_route_appended(monkeypatch):
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -74,7 +74,10 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/mega_moe.py` modified +109/-8; `vllm/models/deepseek_v4/amd/model.py` modified +10/-3
  - tests: `tests/models/test_deepseek_v4_aiter_mega_moe.py` modified +20/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_aiter_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60397 - [ROCm][Perf][DSv4.1] Mono decode layer for DeepSeek-V4.1-Flash on MI355X

- Link: https://github.com/vllm-project/vllm/pull/60397
- Status/date: merged / 2026-10-10
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/mono/README.md`, `vllm/models/deepseek_v41/amd/mono/__init__.py`, `vllm/models/deepseek_v41/amd/mono/attention/__init__.py`, `vllm/models/deepseek_v41/amd/mono/attention/back.py` and 28 files; associated commits `193922d6ff5f`
- Diff scope read: GitHub Pull Request files API returned 33 files, +9119/-2, 9218 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DSv4.1] Mono decode layer for DeepSeek-V4.1-Flash on MI355X"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/attention/back.py`; technical summary: Covers "[ROCm][Perf][DSv4.1] Mono decode layer for DeepSeek-V4.1-Flash on MI355X"; the main implementation surface is `vllm/models/deepseek_v41/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/attention/back.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` added +1635/-0 (1635 lines); hunks: -0,0 +1,1635; symbols: scratch_layout, peer_bytes, ffn_offset, region_pair, touching `scratch_layout, peer_bytes, ffn_offset`; `vllm/models/deepseek_v41/amd/mono/layer.py` added +940/-0 (940 lines); hunks: -0,0 +1,940; symbols: MonoBuild, _moe_key, _front_key, _back_key, touching `MonoBuild, _moe_key, _front_key`; `vllm/models/deepseek_v41/amd/mono/attention/back.py` added +884/-0 (884 lines); hunks: -0,0 +1,884; symbols: BackBuild, plus, head_groups, chunk_keys, touching `BackBuild, plus, head_groups`; `vllm/models/deepseek_v41/amd/mono/attention/front.py` added +662/-0 (662 lines); hunks: -0,0 +1,662; symbols: FrontBuild, plus, publish, await_flags, touching `FrontBuild, plus, publish`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/mono/stages/moe.py` added +1635/-0 (1635 lines); hunks: -0,0 +1,1635; symbols: scratch_layout, peer_bytes, ffn_offset, region_pair
  - `vllm/models/deepseek_v41/amd/mono/layer.py` added +940/-0 (940 lines); hunks: -0,0 +1,940; symbols: MonoBuild, _moe_key, _front_key, _back_key
  - `vllm/models/deepseek_v41/amd/mono/attention/back.py` added +884/-0 (884 lines); hunks: -0,0 +1,884; symbols: BackBuild, plus, head_groups, chunk_keys
  - `vllm/models/deepseek_v41/amd/mono/attention/front.py` added +662/-0 (662 lines); hunks: -0,0 +1,662; symbols: FrontBuild, plus, publish, await_flags
  - `vllm/models/deepseek_v41/amd/mono/attention/device.py` added +504/-0 (504 lines); hunks: -0,0 +1,504; symbols: traced, kernel_symbol, first_task, rsrc
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/mono/stages/moe.py
@@ -0,0 +1,1635 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Adapted from ROCm/ATOM (https://github.com/ROCm/ATOM) at 97359d6, MIT License,
+# Copyright (C) 2026, Advanced Micro Devices, Inc.:
+# atom/models/deepseek_v41/mono/kernels/moe.py
+"""The mono layer's MoE stages: one V4.1 layer's FFN, from the FFN seam's normed
diff -- vllm/models/deepseek_v41/amd/mono/layer.py
@@ -0,0 +1,940 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""The mono decode layer's two launches (README): K1 = the attention seam
+(``stages.seam``: slice, gate, the norm into vLLM's MXFP8) + the attention front
+(``attention.front``); K2 = the attention back (``attention.back``, wo_b pushed
+to every rank) + the FFN seam (the TP sum folded in) + the MoE (``stages.moe``,
diff -- vllm/models/deepseek_v41/amd/mono/attention/back.py
@@ -0,0 +1,884 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/mono/stages/moe.py` added +1635/-0; `vllm/models/deepseek_v41/amd/mono/layer.py` added +940/-0; `vllm/models/deepseek_v41/amd/mono/attention/back.py` added +884/-0; `vllm/models/deepseek_v41/amd/mono/attention/front.py` added +662/-0; `vllm/models/deepseek_v41/amd/mono/attention/device.py` added +504/-0; `vllm/models/deepseek_v41/amd/mono/runner.py` added +437/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_dsv41_mono_decode.py`, `tests/models/test_dsv41_mono_layers.py`, `tests/models/test_dsv41_mono_numerics.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59923 - [Perf][DSv4.1] Exchange packed FP8 Engram rows across DP and feed wkv MXFP8

- Link: https://github.com/vllm-project/vllm/pull/59923
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/engram_peer.py`; associated commits `efaca9547dbd`
- Diff scope read: GitHub Pull Request files API returned 6 files, +505/-31, 698 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Exchange packed FP8 Engram rows across DP and feed wkv MXFP8"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/ops/engram_peer.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Perf][DSv4.1] Exchange packed FP8 Engram rows across DP and feed wkv MXFP8"; the main implementation surface is `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/ops/engram_peer.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/engram.py` modified +213/-10 (223 lines); hunks: -62,16 +62,27; -644,8 +655,10 @@ def _engram_lookup_kernel(; symbols: _engram_lookup_kernel, engram_head_shard_rank, _storage, lookup, touching `_engram_lookup_kernel, engram_head_shard_rank, _storage`; `vllm/models/deepseek_v41/nvidia/ops/engram_peer.py` added +173/-0 (173 lines); hunks: -0,0 +1,173; symbols: _peer_lookup_kernel, EngramPeerExchange, __init__, create, touching `_peer_lookup_kernel, EngramPeerExchange, __init__`; `vllm/models/deepseek_v41/nvidia/model.py` modified +21/-9 (30 lines); hunks: -100,6 +100,7; -743,6 +744,14 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward, touching `__init__, forward`; `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +14/-10 (24 lines); hunks: -21,6 +21,18 @@ def _norm_row(x, weight, row, stride, eps, SIZE: tl.constexpr...; -68,14 +80,7 @@ def _q_kv_norm_quant_kernel(; symbols: _norm_row, mxfp8_scale_offset, mxfp8_scale_bytes, _q_kv_norm_quant_kernel, touching `_norm_row, mxfp8_scale_offset, mxfp8_scale_bytes`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/engram.py` modified +213/-10 (223 lines); hunks: -62,16 +62,27; -644,8 +655,10 @@ def _engram_lookup_kernel(; symbols: _engram_lookup_kernel, engram_head_shard_rank, _storage, lookup
  - `vllm/models/deepseek_v41/nvidia/ops/engram_peer.py` added +173/-0 (173 lines); hunks: -0,0 +1,173; symbols: _peer_lookup_kernel, EngramPeerExchange, __init__, create
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +21/-9 (30 lines); hunks: -100,6 +100,7; -743,6 +744,14 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward
  - `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +14/-10 (24 lines); hunks: -21,6 +21,18 @@ def _norm_row(x, weight, row, stride, eps, SIZE: tl.constexpr...; -68,14 +80,7 @@ def _q_kv_norm_quant_kernel(; symbols: _norm_row, mxfp8_scale_offset, mxfp8_scale_bytes, _q_kv_norm_quant_kernel
  - `tests/kernels/test_engram.py` modified +11/-2 (13 lines); hunks: -7,6 +7,9; -714,8 +717,9 @@ def test_engram_lookup_reuses_jit_across_token_shapes():; symbols: test_engram_lookup_reuses_jit_across_token_shapes, test_engram_lookup_matches_torch
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -62,16 +62,27 @@
+from vllm.model_executor.layers.fusion.quant_activation import QuantizedActivation
+from vllm.model_executor.layers.quantization.utils.quant_utils import kMxfp8Dynamic
+from vllm.models.deepseek_v41.common.ops.query_quant import (
+    can_fuse_query_quant,
+    mxfp8_scale_bytes,
+    mxfp8_scale_offset,
diff -- vllm/models/deepseek_v41/nvidia/ops/engram_peer.py
@@ -0,0 +1,173 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Symmetric-memory Engram exchange for slots below ENGRAM_A2A_MIN_SLOT."""
+from typing import TYPE_CHECKING
+import torch
+import torch.distributed as dist
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -100,6 +100,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/engram.py` modified +213/-10; `vllm/models/deepseek_v41/nvidia/ops/engram_peer.py` added +173/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +21/-9; `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +14/-10
  - tests: `tests/kernels/test_engram.py` modified +11/-2
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_engram.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59894 - [Perf][DSv4.1] Trim the last KV-source layer in decoder replay

- Link: https://github.com/vllm-project/vllm/pull/59894
- Status/date: merged / 2026-10-09
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/model.py` and 6 files; associated commits `ad73a4740dd7`
- Diff scope read: GitHub Pull Request files API returned 6 files, +219/-75, 550 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Trim the last KV-source layer in decoder replay"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`; technical summary: Covers "[Perf][DSv4.1] Trim the last KV-source layer in decoder replay"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +44/-30 (74 lines); hunks: -238,12 +238,13 @@ def __init__(; -263,7 +264,7 @@ def __init__(; symbols: __init__, add_request, _prepare_replay_batch, touching `__init__, add_request, _prepare_replay_batch`; `vllm/models/deepseek_v41/nvidia/model.py` modified +48/-14 (62 lines); hunks: -623,6 +623,40 @@ def forward(; -765,10 +799,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: forward, write_kv, DeepseekV4Model, __init__, touching `forward, write_kv, DeepseekV4Model`; `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +34/-14 (48 lines); hunks: -2,8 +2,8; -21,6 +21,7; symbols: ReplayBatch, DecoderReplayLayers, __init__, __call__, touching `ReplayBatch, DecoderReplayLayers, __init__`; `tests/models/test_deepseek_v41_replay_batch.py` modified +37/-8 (45 lines); hunks: -11,6 +11,12; -59,7 +65,7 @@ def state(monkeypatch):; symbols: state, prepare_attn, _slot_mappings, _prepare, touching `state, prepare_attn, _slot_mappings`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +44/-30 (74 lines); hunks: -238,12 +238,13 @@ def __init__(; -263,7 +264,7 @@ def __init__(; symbols: __init__, add_request, _prepare_replay_batch
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +48/-14 (62 lines); hunks: -623,6 +623,40 @@ def forward(; -765,10 +799,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: forward, write_kv, DeepseekV4Model, __init__
  - `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +34/-14 (48 lines); hunks: -2,8 +2,8; -21,6 +21,7; symbols: ReplayBatch, DecoderReplayLayers, __init__, __call__
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +37/-8 (45 lines); hunks: -11,6 +11,12; -59,7 +65,7 @@ def state(monkeypatch):; symbols: state, prepare_attn, _slot_mappings, _prepare
  - `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +28/-9 (37 lines); hunks: -67,10 +67,8 @@ def _states(num_tokens: int):; -80,7 +78,8 @@ def run_layers(hidden_states, positions, input_ids, pre_mix, p...; symbols: _states, test_run_gathers_states_and_realigns_shared_indexer_buffers, test_run_gathers_states, run_layers
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -238,12 +238,13 @@ def __init__(
-            self._replay_attn_groups: list[list[AttentionGroup]] | None = None
+            # The replay layers' and the first one's SWA attention groups.
+            self._replay_attn_groups: (
+                tuple[list[list[AttentionGroup]], list[list[AttentionGroup]]] | None
+            ) = None
-        # PIECEWISE graphs of this many tokens or more break out to the replay batch.
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -623,6 +623,40 @@ def forward(
+    def write_kv(
+        self,
+        x: torch.Tensor | MoEOutput,
+        positions: torch.Tensor,
+        input_ids: torch.Tensor | None,
+        pre_mix: torch.Tensor,
diff -- vllm/models/deepseek_v41/decoder_replay_layers.py
@@ -2,8 +2,8 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +44/-30; `vllm/models/deepseek_v41/nvidia/model.py` modified +48/-14; `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +34/-14; `vllm/models/deepseek_v41/attention.py` modified +28/-0
  - tests: `tests/models/test_deepseek_v41_replay_batch.py` modified +37/-8; `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +28/-9
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56638 - [ROCm][DSv4.1][Perf] Replace the Torch prefill combine with the shared combine_topk_swa_indices kernel

- Link: https://github.com/vllm-project/vllm/pull/56638
- Status/date: merged / 2026-10-08
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`; associated commits `fb2ac82458cf`
- Diff scope read: GitHub Pull Request files API returned 4 files, +185/-170, 439 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Replace the Torch prefill combine with the shared combine_topk_swa_indices kernel"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Replace the Torch prefill combine with the shared combine_topk_swa_indices kernel"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +4/-160 (164 lines); hunks: -26,7 +26,10; -129,165 +132,6 @@ def apply_pre_quantized_block_scaled_mm(; symbols: apply_pre_quantized_block_scaled_mm, _combine_topk_swa_indices_kernel, combine_topk_swa_indices, _compute_topk_lens_kernel, touching `apply_pre_quantized_block_scaled_mm, _combine_topk_swa_indices_kernel, combine_topk_swa_indices`; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +7/-3 (10 lines); hunks: -1089,7 +1089,8 @@ def kernel(; -1100,17 +1101,20 @@ def kernel(; symbols: kernel, touching `kernel`; `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +17/-6 (23 lines); hunks: -302,8 +302,13 @@ def combine_case(; -326,7 +331,11 @@ def combine_case(; symbols: combine_case, test_combine_topk_swa_with_image_spans, test_v41_combine_topk_swa_stops_at_replay_start, touching `combine_case, test_combine_topk_swa_with_image_spans, test_v41_combine_topk_swa_stops_at_replay_start`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +4/-160 (164 lines); hunks: -26,7 +26,10; -129,165 +132,6 @@ def apply_pre_quantized_block_scaled_mm(; symbols: apply_pre_quantized_block_scaled_mm, _combine_topk_swa_indices_kernel, combine_topk_swa_indices, _compute_topk_lens_kernel
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +7/-3 (10 lines); hunks: -1089,7 +1089,8 @@ def kernel(; -1100,17 +1101,20 @@ def kernel(; symbols: kernel
  - `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +17/-6 (23 lines); hunks: -302,8 +302,13 @@ def combine_case(; -326,7 +331,11 @@ def combine_case(; symbols: combine_case, test_combine_topk_swa_with_image_spans, test_v41_combine_topk_swa_stops_at_replay_start
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -26,7 +26,10 @@
-from vllm.models.deepseek_v41.common.ops import dequantize_and_gather_k_cache
+from vllm.models.deepseek_v41.common.ops import (
+    combine_topk_swa_indices,
+    dequantize_and_gather_k_cache,
+)
@@ -129,165 +132,6 @@ def apply_pre_quantized_block_scaled_mm(
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -1089,7 +1089,8 @@ def kernel(
-                topk_len = tl.minimum((pos + 1) // COMPRESS_RATIO, TOP_K)
+                # Warmup batches can put pos below zero; keep the length >= 0.
+                topk_len = tl.maximum(tl.minimum((pos + 1) // COMPRESS_RATIO, TOP_K), 0)
@@ -1100,17 +1101,20 @@ def kernel(
-            swa_len = pos - swa_start + 1
+            swa_len = tl.maximum(pos - swa_start + 1, 0)
diff -- tests/v1/attention/test_deepseek_v4_swa_visible.py
@@ -302,8 +302,13 @@ def combine_case(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +4/-160; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +7/-3
  - tests: `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +17/-6
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59655 - [Bugfix] [Spec Decode] DeepSeek V4/V4.1 NVFP4: keep ignored MTP/DSpark experts on MXFP4

- Link: https://github.com/vllm-project/vllm/pull/59655
- Status/date: merged / 2026-10-08
- Trace source: `git log --name-only -- <model-files>` found it through `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`, `vllm/models/deepseek_v41/quant_config.py`; associated commits `8faac3dd2af3`
- Diff scope read: GitHub Pull Request files API returned 6 files, +125/-2, 206 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] [Spec Decode] DeepSeek V4/V4.1 NVFP4: keep ignored MTP/DSpark experts on MXFP4"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/quant_config.py`, `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`; technical summary: Covers "[Bugfix] [Spec Decode] DeepSeek V4/V4.1 NVFP4: keep ignored MTP/DSpark experts on MXFP4"; the main implementation surface is `vllm/models/deepseek_v41/quant_config.py`, `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/quant_config.py` modified +30/-2 (32 lines); hunks: -4,8 +4,11; -23,6 +26,7; symbols: __init__, moe_quant_algo, _is_nvfp4_expert_layer, _get_nvfp4_config, touching `__init__, moe_quant_algo, _is_nvfp4_expert_layer`; `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` added +15/-0 (15 lines); hunks: -0,0 +1,15.
- Code diff details:
  - `vllm/models/deepseek_v41/quant_config.py` modified +30/-2 (32 lines); hunks: -4,8 +4,11; -23,6 +26,7; symbols: __init__, moe_quant_algo, _is_nvfp4_expert_layer, _get_nvfp4_config
  - `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` added +15/-0 (15 lines); hunks: -0,0 +1,15
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/quant_config.py
@@ -4,8 +4,11 @@
+import fnmatch
+import regex as re
@@ -23,6 +26,7 @@
+_EXPERTS_LAYER_RE = re.compile(r"(?:^|\.)layers\.(\d+)\.ffn\.experts$")
@@ -54,6 +58,7 @@ def __init__(self, *args, **kwargs):
+        self._modelopt_ignore: tuple[str, ...] = ()
diff -- tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml
@@ -0,0 +1,15 @@
+model_name: "nvidia/DeepSeek-V4.1-Flash-NVFP4"
+accuracy_threshold: 0.88
+tolerance: 0.03
+# The bundled DSpark draft (mtp.*) stays MXFP4 in this checkpoint. Loading it
+# as NVFP4 keeps accuracy but drops acceptance length to 1.0 (3.57 when correct).
+min_acceptance_length: 2.5
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/quant_config.py` modified +30/-2
  - tests: `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml` added +15/-0
- Risk and verification: The diff ships test coverage in `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`, `tests/evals/gsm8k/configs/models-spec-decode.txt`, `tests/quantization/test_fp8.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60462 - [CI] Fix failing test_deepseek_v4_rocm_dspark* tests

- Link: https://github.com/vllm-project/vllm/pull/60462
- Status/date: merged / 2026-10-07
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_dspark_rocm.py`; associated commits `947dd62c0700`
- Diff scope read: GitHub Pull Request files API returned 2 files, +5/-1, 20 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Fix failing test_deepseek_v4_rocm_dspark* tests"; model line: DeepSeek V4; category: bug fix; main diff: `tests/models/test_deepseek_v4_dspark_rocm.py`; technical summary: Covers "[CI] Fix failing test_deepseek_v4_rocm_dspark* tests"; the main implementation surface is `tests/models/test_deepseek_v4_dspark_rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_dspark_rocm.py` modified +4/-1 (5 lines); hunks: -15,7 +15,10 @@ def _make_uninitialized_model(confidence_head):; symbols: _make_uninitialized_model, touching `_make_uninitialized_model`.
- Code diff details:
  - `tests/models/test_deepseek_v4_dspark_rocm.py` modified +4/-1 (5 lines); hunks: -15,7 +15,10 @@ def _make_uninitialized_model(confidence_head):; symbols: _make_uninitialized_model
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_dspark_rocm.py
@@ -15,7 +15,10 @@ def _make_uninitialized_model(confidence_head):
-        SimpleNamespace(confidence_head=confidence_head),
+        SimpleNamespace(
+            confidence_head=confidence_head,
+            layers=[SimpleNamespace(ffn=SimpleNamespace(use_mega_moe=False))],
+        ),
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_dspark_rocm.py` modified +4/-1
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_dspark_rocm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60392 - [CI][ROCm] Re-enable the DSv4.1 decoder replay graph test on ROCm

- Link: https://github.com/vllm-project/vllm/pull/60392
- Status/date: merged / 2026-10-07
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_decoder_replay_layers.py`; associated commits `71f9a749203c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +2/-4, 27 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI][ROCm] Re-enable the DSv4.1 decoder replay graph test on ROCm"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v41_decoder_replay_layers.py`; technical summary: Covers "[CI][ROCm] Re-enable the DSv4.1 decoder replay graph test on ROCm"; the main implementation surface is `tests/models/test_deepseek_v41_decoder_replay_layers.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +2/-4 (6 lines); hunks: -21,7 +21,6; -126,16 +125,15 @@ def _graph_context(num_tokens):; symbols: _graph_context, test_replay_graph_matches_eager, touching `_graph_context, test_replay_graph_matches_eager`.
- Code diff details:
  - `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +2/-4 (6 lines); hunks: -21,7 +21,6; -126,16 +125,15 @@ def _graph_context(num_tokens):; symbols: _graph_context, test_replay_graph_matches_eager
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_decoder_replay_layers.py
@@ -21,7 +21,6 @@
-from vllm.platforms import current_platform
@@ -126,16 +125,15 @@ def _graph_context(num_tokens):
-@pytest.mark.skipif(
-    current_platform.is_rocm(), reason="decoder replay CUDA graphs are NVIDIA-only"
-)
+    # Mocking it true would capture into the cuMem pool, which breaks on ROCm.
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +2/-4
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_decoder_replay_layers.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59685 - [ROCm][DSv4] AITER MegaMoEV2 Integration For DeepSeek V4

- Link: https://github.com/vllm-project/vllm/pull/59685
- Status/date: merged / 2026-10-07
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/dspark.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py` and 6 files; associated commits `f6e3944e3100`
- Diff scope read: GitHub Pull Request files API returned 10 files, +454/-6, 656 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4] AITER MegaMoEV2 Integration For DeepSeek V4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][DSv4] AITER MegaMoEV2 Integration For DeepSeek V4"; the main implementation surface is `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_aiter_mega_moe.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: _make_experts, test_experts_load_into_local_slots, test_mega_moe_routing_matches_reference, Gate, touching `_make_experts, test_experts_load_into_local_slots, test_mega_moe_routing_matches_reference`; `vllm/models/deepseek_v4/amd/mega_moe.py` added +154/-0 (154 lines); hunks: -0,0 +1,154; symbols: DeepseekV4AiterMegaMoEExperts, __init__, make_param, weight_loader, touching `DeepseekV4AiterMegaMoEExperts, __init__, make_param`; `vllm/models/deepseek_v4/amd/model.py` modified +81/-0 (81 lines); hunks: -30,6 +30,9; -71,6 +74,7; symbols: _fuse_shared_experts_enabled, _validate_aiter_mega_moe_config, DeepseekV4MoE, __init__, touching `_fuse_shared_experts_enabled, _validate_aiter_mega_moe_config, DeepseekV4MoE`; `vllm/models/deepseek_v4/amd/dspark.py` modified +9/-5 (14 lines); hunks: -11,9 +11,8; -50,6 +49,7; symbols: load_weights, process_weights_after_loading, _remap_dspark_name, touching `load_weights, process_weights_after_loading, _remap_dspark_name`.
- Code diff details:
  - `tests/models/test_deepseek_v4_aiter_mega_moe.py` added +186/-0 (186 lines); hunks: -0,0 +1,186; symbols: _make_experts, test_experts_load_into_local_slots, test_mega_moe_routing_matches_reference, Gate
  - `vllm/models/deepseek_v4/amd/mega_moe.py` added +154/-0 (154 lines); hunks: -0,0 +1,154; symbols: DeepseekV4AiterMegaMoEExperts, __init__, make_param, weight_loader
  - `vllm/models/deepseek_v4/amd/model.py` modified +81/-0 (81 lines); hunks: -30,6 +30,9; -71,6 +74,7; symbols: _fuse_shared_experts_enabled, _validate_aiter_mega_moe_config, DeepseekV4MoE, __init__
  - `vllm/models/deepseek_v4/amd/dspark.py` modified +9/-5 (14 lines); hunks: -11,9 +11,8; -50,6 +49,7; symbols: load_weights, process_weights_after_loading, _remap_dspark_name
  - `vllm/models/deepseek_v4/amd/mtp.py` modified +8/-0 (8 lines); hunks: -46,6 +46,7; -392,12 +393,16 @@ def _resolve_scale_name(name: str) -> str:; symbols: _resolve_scale_name, process_weights_after_loading, _rewrite_spec_layer_name
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_aiter_mega_moe.py
@@ -0,0 +1,186 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from types import SimpleNamespace
+import pytest
+import torch
+from vllm.model_executor.layers.fused_moe import (
diff -- vllm/models/deepseek_v4/amd/mega_moe.py
@@ -0,0 +1,154 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""AITER MegaMoE experts (fused dispatch, MXFP4 GEMMs, combine) for DeepSeek V4."""
+from typing import Any
+import torch
+import torch.nn as nn
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -30,6 +30,9 @@
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_aiter_mega_moe.py` added +186/-0; `tests/models/test_deepseek_v4_vl_rocm.py` modified +3/-1
  - runtime: `vllm/models/deepseek_v4/amd/mega_moe.py` added +154/-0; `vllm/models/deepseek_v4/amd/model.py` modified +81/-0; `vllm/models/deepseek_v4/amd/dspark.py` modified +9/-5; `vllm/models/deepseek_v4/amd/mtp.py` modified +8/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `tests/models/test_deepseek_v4_vl_rocm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60378 - [CI][ROCm] Skip DSv4.1 decoder replay graph test on ROCm

- Link: https://github.com/vllm-project/vllm/pull/60378
- Status/date: merged / 2026-10-07
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_decoder_replay_layers.py`; associated commits `02d8a94e610f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +4/-0, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI][ROCm] Skip DSv4.1 decoder replay graph test on ROCm"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v41_decoder_replay_layers.py`; technical summary: Covers "[CI][ROCm] Skip DSv4.1 decoder replay graph test on ROCm"; the main implementation surface is `tests/models/test_deepseek_v41_decoder_replay_layers.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +4/-0 (4 lines); hunks: -21,6 +21,7; -125,6 +126,9 @@ def _graph_context(num_tokens):; symbols: _graph_context, test_replay_graph_matches_eager, touching `_graph_context, test_replay_graph_matches_eager`.
- Code diff details:
  - `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +4/-0 (4 lines); hunks: -21,6 +21,7; -125,6 +126,9 @@ def _graph_context(num_tokens):; symbols: _graph_context, test_replay_graph_matches_eager
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v41_decoder_replay_layers.py
@@ -21,6 +21,7 @@
+from vllm.platforms import current_platform
@@ -125,6 +126,9 @@ def _graph_context(num_tokens):
+@pytest.mark.skipif(
+    current_platform.is_rocm(), reason="decoder replay CUDA graphs are NVIDIA-only"
+)
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +4/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_decoder_replay_layers.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #60064 - [Model][DeepSeek-V4.1] Permute mega-attention wq_b / wo_a while loading

- Link: https://github.com/vllm-project/vllm/pull/60064
- Status/date: merged / 2026-10-06
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/ops/fused_layout.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `9a1f6fd4cbe4`
- Diff scope read: GitHub Pull Request files API returned 5 files, +48/-94, 251 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][DeepSeek-V4.1] Permute mega-attention wq_b / wo_a while loading"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/common/ops/fused_layout.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`; technical summary: Covers "[Model][DeepSeek-V4.1] Permute mega-attention wq_b / wo_a while loading"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/common/ops/fused_layout.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +11/-27 (38 lines); hunks: -32,8 +32,10; -182,7 +184,13 @@ def __init__(self, vllm_config: VllmConfig, *args, **kwargs...; symbols: __init__, _o_proj, finalize_loaded_weights, forward_mqa, touching `__init__, _o_proj, finalize_loaded_weights`; `vllm/models/deepseek_v41/common/ops/fused_layout.py` modified +12/-24 (36 lines); hunks: -12,6 +12,8; -60,27 +62,13 @@ def _bytes_view(t: torch.Tensor) -> torch.Tensor:; symbols: _bytes_view, permute_wq_b_, permute_wo_a_, permute_on_load, touching `_bytes_view, permute_wq_b_, permute_wo_a_`; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +0/-14 (14 lines); hunks: -500,22 +500,8 @@ def _finalize_moe(self) -> None:; symbols: _finalize_moe, _finalize_attn, process_weights_after_loading, _remap_dspark_name, touching `_finalize_moe, _finalize_attn, process_weights_after_loading`; `vllm/models/deepseek_v41/nvidia/model.py` modified +0/-12 (12 lines); hunks: -1354,17 +1354,6 @@ def finalize_mega_moe_weights(self) -> None:; -1637,7 +1626,6 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: finalize_mega_moe_weights, finalize_mega_attn_weights, finalize_mhc_broadcast_weights, load_weights, touching `finalize_mega_moe_weights, finalize_mega_attn_weights, finalize_mhc_broadcast_weights`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +11/-27 (38 lines); hunks: -32,8 +32,10; -182,7 +184,13 @@ def __init__(self, vllm_config: VllmConfig, *args, **kwargs...; symbols: __init__, _o_proj, finalize_loaded_weights, forward_mqa
  - `vllm/models/deepseek_v41/common/ops/fused_layout.py` modified +12/-24 (36 lines); hunks: -12,6 +12,8; -60,27 +62,13 @@ def _bytes_view(t: torch.Tensor) -> torch.Tensor:; symbols: _bytes_view, permute_wq_b_, permute_wo_a_, permute_on_load
  - `vllm/models/deepseek_v41/nvidia/dspark.py` modified +0/-14 (14 lines); hunks: -500,22 +500,8 @@ def _finalize_moe(self) -> None:; symbols: _finalize_moe, _finalize_attn, process_weights_after_loading, _remap_dspark_name
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +0/-12 (12 lines); hunks: -1354,17 +1354,6 @@ def finalize_mega_moe_weights(self) -> None:; -1637,7 +1626,6 @@ def load_weights(self, weights: Iterable[tuple[str, torch....; symbols: finalize_mega_moe_weights, finalize_mega_attn_weights, finalize_mhc_broadcast_weights, load_weights
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -32,8 +32,10 @@
-    permute_wo_a_,
-    permute_wq_b_,
+    o_fused_chunk_permutation,
+    o_fused_permutation,
+    permute_on_load,
+    q_fused_permutation,
diff -- vllm/models/deepseek_v41/common/ops/fused_layout.py
@@ -12,6 +12,8 @@
+from vllm.model_executor.model_loader.weight_utils import composed_weight_loader
@@ -60,27 +62,13 @@ def _bytes_view(t: torch.Tensor) -> torch.Tensor:
-def permute_wq_b_(
-    weight: torch.Tensor, weight_scale: torch.Tensor, num_local_heads: int
-) -> None:
-    """Permute an MXFP8 ``wq_b`` shard's rows and per-row scales, in place."""
diff -- vllm/models/deepseek_v41/nvidia/dspark.py
@@ -500,22 +500,8 @@ def _finalize_moe(self) -> None:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +11/-27; `vllm/models/deepseek_v41/common/ops/fused_layout.py` modified +12/-24; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +0/-14; `vllm/models/deepseek_v41/nvidia/model.py` modified +0/-12
- Risk and verification: The diff ships test coverage in `tests/kernels/test_dsv41_mega_attn_layouts.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59532 - [Perf][DSv4.1] Run decoder replay layers in CUDA graphs and trim in PIECEWISE graphs

- Link: https://github.com/vllm-project/vllm/pull/59532
- Status/date: merged / 2026-10-06
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `vllm/models/deepseek_v41/nvidia/model.py` and 6 files; associated commits `eb2901b7356d`
- Diff scope read: GitHub Pull Request files API returned 10 files, +445/-71, 801 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Run decoder replay layers in CUDA graphs and trim in PIECEWISE graphs"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`; technical summary: Covers "[Perf][DSv4.1] Run decoder replay layers in CUDA graphs and trim in PIECEWISE graphs"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +136/-32 (168 lines); hunks: -8,19 +8,28; -230,6 +239,31 @@ def __init__(; symbols: __init__, add_request, _prepare_replay_batch, touching `__init__, add_request, _prepare_replay_batch`; `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: DecoderReplayCudaGraphManager, __init__, capture_replay_graphs, create_forward_fn, touching `DecoderReplayCudaGraphManager, __init__, capture_replay_graphs`; `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +60/-17 (77 lines); hunks: -7,58 +7,101; symbols: ReplayBatch, DecoderReplayLayers, __init__, __call__, touching `ReplayBatch, DecoderReplayLayers, __init__`; `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +62/-6 (68 lines); hunks: -2,15 +2,26; -32,9 +43,9 @@ def _context(metadata):; symbols: _context, _set_replay_batch, run_layers, _graph_context, touching `_context, _set_replay_batch, run_layers`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +136/-32 (168 lines); hunks: -8,19 +8,28; -230,6 +239,31 @@ def __init__(; symbols: __init__, add_request, _prepare_replay_batch
  - `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` added +102/-0 (102 lines); hunks: -0,0 +1,102; symbols: DecoderReplayCudaGraphManager, __init__, capture_replay_graphs, create_forward_fn
  - `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +60/-17 (77 lines); hunks: -7,58 +7,101; symbols: ReplayBatch, DecoderReplayLayers, __init__, __call__
  - `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +62/-6 (68 lines); hunks: -2,15 +2,26; -32,9 +43,9 @@ def _context(metadata):; symbols: _context, _set_replay_batch, run_layers, _graph_context
  - `tests/models/test_deepseek_v41_replay_batch.py` modified +31/-14 (45 lines); hunks: -12,6 +12,7; -57,7 +58,8 @@ def state(monkeypatch):; symbols: state, _prepare, test_replay_batch_keeps_each_request_window, test_replay_batch_keeps_adaptive_verification_query_bound
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -8,19 +8,28 @@
+from vllm.compilation.breakable_cudagraph import is_breakable_cudagraph_enabled
-from vllm.distributed.parallel_state import get_dp_group
-from vllm.forward_context import DPMetadata, create_forward_context
-from vllm.models.deepseek_v41.decoder_replay_layers import DecoderReplayLayers
+from vllm.distributed.parallel_state import get_dp_group, get_pp_group
+from vllm.forward_context import BatchDescriptor, DPMetadata, create_forward_context
diff -- vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py
@@ -0,0 +1,102 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""CUDA graphs of the decoder replay layers on a step's replay batch."""
+from collections.abc import Callable
+from copy import copy
+from dataclasses import replace
diff -- vllm/models/deepseek_v41/decoder_replay_layers.py
@@ -7,58 +7,101 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +136/-32; `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py` added +102/-0; `vllm/models/deepseek_v41/decoder_replay_layers.py` modified +60/-17; `vllm/models/deepseek_v41/nvidia/model.py` modified +10/-0
  - tests: `tests/models/test_deepseek_v41_decoder_replay_layers.py` modified +62/-6; `tests/models/test_deepseek_v41_replay_batch.py` modified +31/-14
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56720 - [ROCm][DSv4.1][Perf] One-pass dequantize and a gather-sized grid for the compressed K cache

- Link: https://github.com/vllm-project/vllm/pull/56720
- Status/date: merged / 2026-10-06
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`; associated commits `97bd8c74ebf1`
- Diff scope read: GitHub Pull Request files API returned 3 files, +195/-2, 267 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] One-pass dequantize and a gather-sized grid for the compressed K cache"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] One-pass dequantize and a gather-sized grid for the compressed K cache"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +116/-2 (118 lines); hunks: -33,7 +33,7; -436,6 +436,95 @@ def _dequantize_and_gather_k_kernel(; symbols: _dequantize_and_gather_k_kernel, _dequantize_and_gather_k_one_pass_kernel, _dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel, touching `_dequantize_and_gather_k_kernel, _dequantize_and_gather_k_one_pass_kernel, _dequantize_and_gather_k_mxfp8_kernel`; `vllm/models/deepseek_v41/amd/rocm.py` modified +5/-0 (5 lines); hunks: -1387,6 +1387,9 @@ def _forward_prefill(; -1438,6 +1441,8 @@ def _forward_prefill(; symbols: _forward_prefill, touching `_forward_prefill`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +116/-2 (118 lines); hunks: -33,7 +33,7; -436,6 +436,95 @@ def _dequantize_and_gather_k_kernel(; symbols: _dequantize_and_gather_k_kernel, _dequantize_and_gather_k_one_pass_kernel, _dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +5/-0 (5 lines); hunks: -1387,6 +1387,9 @@ def _forward_prefill(; -1438,6 +1441,8 @@ def _forward_prefill(; symbols: _forward_prefill
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -33,7 +33,7 @@
-from vllm.utils.math_utils import next_power_of_2
+from vllm.utils.math_utils import cdiv, next_power_of_2
@@ -436,6 +436,95 @@ def _dequantize_and_gather_k_kernel(
+@triton.jit
+def _dequantize_and_gather_k_one_pass_kernel(
+    out_ptr,
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -1387,6 +1387,9 @@ def _forward_prefill(
+        # CPU copy, so sizing the gather grid from it does not sync.
+        seq_lens_cpu = swa_metadata.prefill_seq_lens_cpu
+        assert seq_lens_cpu is not None
@@ -1438,6 +1441,8 @@ def _forward_prefill(
+                    max_gather_len=int(seq_lens_cpu[chunk_start:chunk_end].max())
+                    // self.compress_ratio,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +116/-2; `vllm/models/deepseek_v41/amd/rocm.py` modified +5/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59927 - [Model][DeepSeek-V4] Make MegaMoE shared-expert finalize independent of linear post-load order

- Link: https://github.com/vllm-project/vllm/pull/59927
- Status/date: merged / 2026-10-05
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `4a30c4cad014`
- Diff scope read: GitHub Pull Request files API returned 2 files, +43/-18, 119 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][DeepSeek-V4] Make MegaMoE shared-expert finalize independent of linear post-load order"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`; technical summary: Covers "[Model][DeepSeek-V4] Make MegaMoE shared-expert finalize independent of linear post-load order"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +27/-7 (34 lines); hunks: -9,6 +9,9; -23,6 +26,7; symbols: test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights, FakeDeepGemm, scale_parameter, touching `test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights, FakeDeepGemm`; `vllm/models/deepseek_v4/nvidia/model.py` modified +16/-11 (27 lines); hunks: -409,13 +409,11 @@ def _finalize_shared_expert_weights(; -501,9 +499,13 @@ def _prepare_shared_expert_scale(; symbols: _finalize_shared_expert_weights, _prepare_shared_expert_scale, touching `_finalize_shared_expert_weights, _prepare_shared_expert_scale`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +27/-7 (34 lines); hunks: -9,6 +9,9; -23,6 +26,7; symbols: test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights, FakeDeepGemm, scale_parameter
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +16/-11 (27 lines); hunks: -409,13 +409,11 @@ def _finalize_shared_expert_weights(; -501,9 +499,13 @@ def _prepare_shared_expert_scale(; symbols: _finalize_shared_expert_weights, _prepare_shared_expert_scale
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -9,6 +9,9 @@
+from vllm.model_executor.layers.quantization.utils.fp8_utils import (
+    deepgemm_post_process_weight_scale_block,
+)
@@ -23,6 +26,7 @@
+from vllm.utils.deep_gemm import is_deep_gemm_supported
@@ -473,19 +477,23 @@ def test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions(
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -409,13 +409,11 @@ def _finalize_shared_expert_weights(
-        # 128x128). Build a dedicated, numerically equivalent scale view before
-        # the generic linear post-load hook replaces the raw checkpoint scales
-        # with its 128x128 DeepGEMM layout.
-        checkpoint_scale_dtypes = (torch.float8_e8m0fnu, torch.uint8)
+        # 128x128). Build a dedicated, numerically equivalent scale view.
+        ue8m0_scale_dtypes = (torch.float8_e8m0fnu, torch.uint8, torch.int32)
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +27/-7
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +16/-11
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58560 - [Bugfix][DSv4.1] Keep the compressor ring out of the null block

- Link: https://github.com/vllm-project/vllm/pull/58560
- Status/date: merged / 2026-10-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/compressor.py`; associated commits `49e0f4797853`
- Diff scope read: GitHub Pull Request files API returned 2 files, +20/-14, 67 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Keep the compressor ring out of the null block"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/compressor.py`; technical summary: Covers "[Bugfix][DSv4.1] Keep the compressor ring out of the null block"; the main implementation surface is `vllm/models/deepseek_v41/compressor.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/compressor.py` modified +5/-1 (6 lines); hunks: -75,8 +75,12 @@ def _ring_slot_mapping_kernel(; symbols: _ring_slot_mapping_kernel, touching `_ring_slot_mapping_kernel`.
- Code diff details:
  - `vllm/models/deepseek_v41/compressor.py` modified +5/-1 (6 lines); hunks: -75,8 +75,12 @@ def _ring_slot_mapping_kernel(; symbols: _ring_slot_mapping_kernel
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/compressor.py
@@ -75,8 +75,12 @@ def _ring_slot_mapping_kernel(
+    # Block 0 is the null block. A request without a ring block (dummy or padding
+    # rows, which the runners fill with the null block) must not write.
-        slot_mapping_ptr + offsets, tl.where(valid, slot, -1), mask=offsets < num_tokens
+        slot_mapping_ptr + offsets,
+        tl.where(valid & (block != 0), slot, -1),
+        mask=offsets < num_tokens,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/compressor.py` modified +5/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59159 - [Bugfix][XPU] Make DeepSeek V4 FP8 sparse decode graph-capturable

- Link: https://github.com/vllm-project/vllm/pull/59159
- Status/date: merged / 2026-10-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py`; associated commits `155d23cb008f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +36/-89, 155 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][XPU] Make DeepSeek V4 FP8 sparse decode graph-capturable"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py`; technical summary: Covers "[Bugfix][XPU] Make DeepSeek V4 FP8 sparse decode graph-capturable"; the main implementation surface is `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py` modified +36/-89 (125 lines); hunks: -166,8 +166,7 @@ def xpu_sparse_decode_fp8(; -176,109 +175,57 @@ def xpu_sparse_decode_fp8(; symbols: xpu_sparse_decode_fp8, touching `xpu_sparse_decode_fp8`.
- Code diff details:
  - `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py` modified +36/-89 (125 lines); hunks: -166,8 +166,7 @@ def xpu_sparse_decode_fp8(; -176,109 +175,57 @@ def xpu_sparse_decode_fp8(; symbols: xpu_sparse_decode_fp8
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py
@@ -166,8 +166,7 @@ def xpu_sparse_decode_fp8(
-    # Determine max topk and swa widths
-    if not swa_only and topk_indices is not None:
+    if not swa_only and topk_indices is not None and kv_cache is not None:
@@ -176,109 +175,57 @@ def xpu_sparse_decode_fp8(
+    use_topk = topk_idx_2d is not None
-    # Allocate flat workspace: [num_tokens * K_total, 512] bf16
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py` modified +36/-89
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #59327 - [Perf][DSv4.1] Faster Engram host lookups: sorted rows, inline big lookups

- Link: https://github.com/vllm-project/vllm/pull/59327
- Status/date: merged / 2026-10-01
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `4c2d277643e2`
- Diff scope read: GitHub Pull Request files API returned 6 files, +547/-556, 1396 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Faster Engram host lookups: sorted rows, inline big lookups"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Perf][DSv4.1] Faster Engram host lookups: sorted rows, inline big lookups"; the main implementation surface is `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/nvidia/engram.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/engram.py` modified +490/-22 (512 lines); hunks: -34,30 +34,60; -583,12 +613,14 @@ def _engram_head_shard_weight_loader(; symbols: _engram_lookup_thresholds, _is_prime, _engram_head_shard_weight_loader, _engram_lookup_kernel, touching `_engram_lookup_thresholds, _is_prime, _engram_head_shard_weight_loader`; `vllm/models/deepseek_v41/nvidia/engram.py` removed +0/-497 (497 lines); hunks: -1,497 +0,0; symbols: _allocate_huge_page_storage, engram_head_shard_rank, engram_gathered_num_tokens, gather_engram_hashes, touching `_allocate_huge_page_storage, engram_head_shard_rank, engram_gathered_num_tokens`; `vllm/models/deepseek_v41/nvidia/model.py` modified +7/-2 (9 lines); hunks: -98,9 +98,14; `vllm/models/deepseek_v41/amd/model.py` modified +1/-5 (6 lines); hunks: -65,13 +65,9.
- Code diff details:
  - `vllm/models/deepseek_v41/common/engram.py` modified +490/-22 (512 lines); hunks: -34,30 +34,60; -583,12 +613,14 @@ def _engram_head_shard_weight_loader(; symbols: _engram_lookup_thresholds, _is_prime, _engram_head_shard_weight_loader, _engram_lookup_kernel
  - `vllm/models/deepseek_v41/nvidia/engram.py` removed +0/-497 (497 lines); hunks: -1,497 +0,0; symbols: _allocate_huge_page_storage, engram_head_shard_rank, engram_gathered_num_tokens, gather_engram_hashes
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +7/-2 (9 lines); hunks: -98,9 +98,14
  - `vllm/models/deepseek_v41/amd/model.py` modified +1/-5 (6 lines); hunks: -65,13 +65,9
  - `tests/kernels/test_engram.py` modified +25/-25 (50 lines); hunks: -9,13 +9,10; -111,7 +108,7 @@ def test_fused_engram_post_wkv_matches_reference(; symbols: test_fused_engram_post_wkv_matches_reference, test_engram_rejects_empty_head_shards, test_engram_head_shards_reconstruct_checkpoint
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -34,30 +34,60 @@
+import ctypes
+import mmap
+import os
+import tempfile
+from contextlib import ExitStack
+from vllm.compilation.breakable_cudagraph import eager_break_during_capture
diff -- vllm/models/deepseek_v41/nvidia/engram.py
@@ -1,497 +0,0 @@
-# SPDX-License-Identifier: Apache-2.0
-# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
-"""NVIDIA Engram DP sharding, shared host storage, and asynchronous prefetch."""
-import ctypes
-import mmap
-import os
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -98,9 +98,14 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/engram.py` modified +490/-22; `vllm/models/deepseek_v41/nvidia/engram.py` removed +0/-497; `vllm/models/deepseek_v41/nvidia/model.py` modified +7/-2; `vllm/models/deepseek_v41/amd/model.py` modified +1/-5
  - tests: `tests/kernels/test_engram.py` modified +25/-25
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_engram.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59373 - [BugFix][Multimodal] Pick worst-case DeepSeek-V4 VL dummy image size (#59271)

- Link: https://github.com/vllm-project/vllm/pull/59373
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/mm_preprocess.py`; associated commits `17e9295dd565`
- Diff scope read: GitHub Pull Request files API returned 2 files, +80/-8, 97 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[BugFix][Multimodal] Pick worst-case DeepSeek-V4 VL dummy image size (#59271)"; model line: DeepSeek V4; category: bug fix; main diff: `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/mm_preprocess.py`; technical summary: Covers "[BugFix][Multimodal] Pick worst-case DeepSeek-V4 VL dummy image size (#59271)"; the main implementation surface is `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/mm_preprocess.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/multimodal/processing/test_deepseek_v4_vl.py` added +53/-0 (53 lines); hunks: -0,0 +1,53; symbols: _ConfigCtx, __init__, get_hf_config, _feature_counts, touching `_ConfigCtx, __init__, get_hf_config`; `vllm/models/deepseek_v4/common/mm_preprocess.py` modified +27/-8 (35 lines); hunks: -354,15 +354,34 @@ def get_image_size_with_most_features(self) -> ImageSize:; symbols: get_image_size_with_most_features, DeepseekV4VLDummyInputsBuilder, touching `get_image_size_with_most_features, DeepseekV4VLDummyInputsBuilder`.
- Code diff details:
  - `tests/models/multimodal/processing/test_deepseek_v4_vl.py` added +53/-0 (53 lines); hunks: -0,0 +1,53; symbols: _ConfigCtx, __init__, get_hf_config, _feature_counts
  - `vllm/models/deepseek_v4/common/mm_preprocess.py` modified +27/-8 (35 lines); hunks: -354,15 +354,34 @@ def get_image_size_with_most_features(self) -> ImageSize:; symbols: get_image_size_with_most_features, DeepseekV4VLDummyInputsBuilder
- Key code excerpts:

```diff
diff -- tests/models/multimodal/processing/test_deepseek_v4_vl.py
@@ -0,0 +1,53 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DeepSeek-V4 VL processing helpers."""
+from PIL import Image
+from vllm.models.deepseek_v4.common.mm_preprocess import (
+    DeepseekV4VLProcessingInfo,
diff -- vllm/models/deepseek_v4/common/mm_preprocess.py
@@ -354,15 +354,34 @@ def get_image_size_with_most_features(self) -> ImageSize:
-        # A square maximizes the ViT patch count (area) within the token
-        # budget; solve the budget-derived size directly to keep the dummy
-        # image small.
+        max_wh_ratio = hf_config.vision_max_wh_ratio
+        # Every aligner row costs an extra IMAGE_NEW_LINE token, so height is
+        # more expensive than width and a square is *not* optimal: search the
```

- Reviewed files:
  - tests: `tests/models/multimodal/processing/test_deepseek_v4_vl.py` added +53/-0
  - runtime: `vllm/models/deepseek_v4/common/mm_preprocess.py` modified +27/-8
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/processing/test_deepseek_v4_vl.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58539 - [ROCm][DSv4.1][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill

- Link: https://github.com/vllm-project/vllm/pull/58539
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `8ee40690331c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-10, 58 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +11/-10 (21 lines); hunks: -1379,7 +1379,6 @@ def _forward_prefill(; -1408,21 +1407,23 @@ def _forward_prefill(; symbols: _forward_prefill, touching `_forward_prefill`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +11/-10 (21 lines); hunks: -1379,7 +1379,6 @@ def _forward_prefill(; -1408,21 +1407,23 @@ def _forward_prefill(; symbols: _forward_prefill
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -1379,7 +1379,6 @@ def _forward_prefill(
-        num_prefills = swa_metadata.num_prefills
@@ -1408,21 +1407,23 @@ def _forward_prefill(
-        num_chunks = (num_prefills + self.PREFILL_CHUNK_SIZE - 1) // (
-            self.PREFILL_CHUNK_SIZE
+        chunk_plan = swa_metadata.get_prefill_chunk_plan(
+            compress_ratio=self.compress_ratio,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +11/-10
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/amd/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58405 - [ROCm][DSv4][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill

- Link: https://github.com/vllm-project/vllm/pull/58405
- Status/date: merged / 2026-09-30
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `fcd317cf33b5`
- Diff scope read: GitHub Pull Request files API returned 1 files, +11/-16, 63 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +11/-16 (27 lines); hunks: -1426,7 +1426,6 @@ def _forward_prefill(; -1458,26 +1457,22 @@ def _forward_prefill(; symbols: _forward_prefill, touching `_forward_prefill`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +11/-16 (27 lines); hunks: -1426,7 +1426,6 @@ def _forward_prefill(; -1458,26 +1457,22 @@ def _forward_prefill(; symbols: _forward_prefill
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -1426,7 +1426,6 @@ def _forward_prefill(
-        num_prefills = swa_metadata.num_prefills
@@ -1458,26 +1457,22 @@ def _forward_prefill(
-            N = (self.max_model_len + self.compress_ratio - 1) // self.compress_ratio
-            N = 0
-        M = N + self.window_size + self.max_num_batched_tokens
-        num_chunks = (num_prefills + self.PREFILL_CHUNK_SIZE - 1) // (
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +11/-16
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57898 - [Bugfix] Profile maximum DeepSeek V4.1 vision features

- Link: https://github.com/vllm-project/vllm/pull/57898
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/mm_preprocess.py`; associated commits `ac7f3e11ea88`
- Diff scope read: GitHub Pull Request files API returned 1 files, +21/-8, 37 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Profile maximum DeepSeek V4.1 vision features"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/common/mm_preprocess.py`; technical summary: Covers "[Bugfix] Profile maximum DeepSeek V4.1 vision features"; the main implementation surface is `vllm/models/deepseek_v41/common/mm_preprocess.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/mm_preprocess.py` modified +21/-8 (29 lines); hunks: -275,15 +275,28 @@ def get_image_size_with_most_features(self) -> ImageSize:; symbols: get_image_size_with_most_features, DeepseekV4VLDummyInputsBuilder, touching `get_image_size_with_most_features, DeepseekV4VLDummyInputsBuilder`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/mm_preprocess.py` modified +21/-8 (29 lines); hunks: -275,15 +275,28 @@ def get_image_size_with_most_features(self) -> ImageSize:; symbols: get_image_size_with_most_features, DeepseekV4VLDummyInputsBuilder
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/mm_preprocess.py
@@ -275,15 +275,28 @@ def get_image_size_with_most_features(self) -> ImageSize:
-        # A square maximizes the ViT patch count (area) within the token
-        # budget; solve the budget-derived size directly to keep the dummy
-        # image small.
-        side = budget * patch_size * downsample_ratio
-        best_h, best_w = solve_resize_ratio(
-            side, side, patch_size, downsample_ratio, budget
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/mm_preprocess.py` modified +21/-8
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/common/mm_preprocess.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58132 - [Model] Decoder-side SWA bounded replay for DeepSeek-V4.1

- Link: https://github.com/vllm-project/vllm/pull/58132
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/model_state.py` and 6 files; associated commits `4b2e1cfa7b80`
- Diff scope read: GitHub Pull Request files API returned 9 files, +1001/-60, 1223 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Decoder-side SWA bounded replay for DeepSeek-V4.1"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/models/test_deepseek_v41_replay_batch.py`; technical summary: Covers "[Model] Decoder-side SWA bounded replay for DeepSeek-V4.1"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model_state.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `tests/models/test_deepseek_v41_replay_batch.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +321/-2 (323 lines); hunks: -1,17 +1,24; -81,6 +88,61 @@ def _pad_replayed_slots_kernel(; symbols: _pad_replayed_slots_kernel, _gather_replay_batch_kernel, ReplayAttnMetadata, DeepseekV41ModelState, touching `_pad_replayed_slots_kernel, _gather_replay_batch_kernel, ReplayAttnMetadata`; `vllm/models/deepseek_v41/nvidia/model.py` modified +222/-40 (262 lines); hunks: -83,6 +83,7; -741,6 +742,35 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward, _mega_gate_metadata, _run_layers, touching `__init__, forward, _mega_gate_metadata`; `tests/models/test_deepseek_v41_replay_batch.py` added +259/-0 (259 lines); hunks: -0,0 +1,259; symbols: state, prepare_attn, _input_batch, _slot_mappings, touching `state, prepare_attn, _input_batch`; `tests/models/test_deepseek_v41_decoder_replay_layers.py` added +104/-0 (104 lines); hunks: -0,0 +1,104; symbols: _context, _set_replay_batch, _states, test_run_gathers_states_and_realigns_shared_indexer_buffers, touching `_context, _set_replay_batch, _states`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +321/-2 (323 lines); hunks: -1,17 +1,24; -81,6 +88,61 @@ def _pad_replayed_slots_kernel(; symbols: _pad_replayed_slots_kernel, _gather_replay_batch_kernel, ReplayAttnMetadata, DeepseekV41ModelState
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +222/-40 (262 lines); hunks: -83,6 +83,7; -741,6 +742,35 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, forward, _mega_gate_metadata, _run_layers
  - `tests/models/test_deepseek_v41_replay_batch.py` added +259/-0 (259 lines); hunks: -0,0 +1,259; symbols: state, prepare_attn, _input_batch, _slot_mappings
  - `tests/models/test_deepseek_v41_decoder_replay_layers.py` added +104/-0 (104 lines); hunks: -0,0 +1,104; symbols: _context, _set_replay_batch, _states, test_run_gathers_states_and_realigns_shared_indexer_buffers
  - `vllm/models/deepseek_v41/decoder_replay_layers.py` added +67/-0 (67 lines); hunks: -0,0 +1,67; symbols: DecoderReplayLayers, __init__, __call__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -1,17 +1,24 @@
+from dataclasses import replace
+import torch.distributed as dist
+from vllm.distributed.parallel_state import get_dp_group
+from vllm.forward_context import DPMetadata, create_forward_context
+from vllm.models.deepseek_v41.decoder_replay_layers import DecoderReplayLayers
+from vllm.v1.worker.dp_utils import should_skip_dp_coordination
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -83,6 +83,7 @@
+from vllm.models.deepseek_v41.decoder_replay_layers import DecoderReplayLayers
@@ -741,6 +742,35 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
+        # Decoder-side SWA bounded replay: in eager prefill steps the layers past
+        # the last KV source run on each request's trailing window only
+        # (decoder_replay_layers.py).
+        self.decoder_replay_layers: DecoderReplayLayers | None = None
diff -- tests/models/test_deepseek_v41_replay_batch.py
@@ -0,0 +1,259 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +321/-2; `vllm/models/deepseek_v41/nvidia/model.py` modified +222/-40; `vllm/models/deepseek_v41/decoder_replay_layers.py` added +67/-0; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +5/-0
  - tests: `tests/models/test_deepseek_v41_replay_batch.py` added +259/-0; `tests/models/test_deepseek_v41_decoder_replay_layers.py` added +104/-0
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #59119 - [DSv4.1] Avoid runtime recompiles of _ring_slot_mapping_kernel

- Link: https://github.com/vllm-project/vllm/pull/59119
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/compressor.py`; associated commits `30f5c01d4ebb`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-1, 9 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSv4.1] Avoid runtime recompiles of _ring_slot_mapping_kernel"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v41/compressor.py`; technical summary: Covers "[DSv4.1] Avoid runtime recompiles of _ring_slot_mapping_kernel"; the main implementation surface is `vllm/models/deepseek_v41/compressor.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/compressor.py` modified +1/-1 (2 lines); hunks: -57,7 +57,7 @@ class CompressorMetadata:; symbols: CompressorMetadata, _ring_slot_mapping_kernel, touching `CompressorMetadata, _ring_slot_mapping_kernel`.
- Code diff details:
  - `vllm/models/deepseek_v41/compressor.py` modified +1/-1 (2 lines); hunks: -57,7 +57,7 @@ class CompressorMetadata:; symbols: CompressorMetadata, _ring_slot_mapping_kernel
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/compressor.py
@@ -57,7 +57,7 @@ class CompressorMetadata:
-@triton.jit
+@triton.jit(do_not_specialize=["block_table_stride", "num_actual_tokens", "num_tokens"])
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/compressor.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/compressor.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58671 - [ROCm][DSv4.1] Paged MXFP4 sparse indexer on aiter's MQA-logits kernel

- Link: https://github.com/vllm-project/vllm/pull/58671
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`; associated commits `63b9931b7399`
- Diff scope read: GitHub Pull Request files API returned 9 files, +2276/-9, 2437 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1] Paged MXFP4 sparse indexer on aiter's MQA-logits kernel"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/config/attention.py`; technical summary: Covers "[ROCm][DSv4.1] Paged MXFP4 sparse indexer on aiter's MQA-logits kernel"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/config/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +149/-1 (150 lines); hunks: -2,8 +2,9; -15,8 +16,14; symbols: build, _aiter_indexer_cache_ops, rocm_mxfp4_indexer_k_store, rocm_mxfp4_indexer_q_quant, touching `build, _aiter_indexer_cache_ops, rocm_mxfp4_indexer_k_store`; `vllm/models/deepseek_v41/attention.py` modified +34/-6 (40 lines); hunks: -35,6 +35,9; -261,6 +264,13 @@ def _uses_fp8_ds_mla_layout(self) -> bool:; symbols: _uses_fp8_ds_mla_layout, _indexer_cls, __init__, touching `_uses_fp8_ds_mla_layout, _indexer_cls, __init__`; `vllm/config/attention.py` modified +4/-1 (5 lines); hunks: -93,7 +93,10 @@ class AttentionConfig:; symbols: AttentionConfig, GPU, touching `AttentionConfig, GPU`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +149/-1 (150 lines); hunks: -2,8 +2,9; -15,8 +16,14; symbols: build, _aiter_indexer_cache_ops, rocm_mxfp4_indexer_k_store, rocm_mxfp4_indexer_q_quant
  - `vllm/models/deepseek_v41/attention.py` modified +34/-6 (40 lines); hunks: -35,6 +35,9; -261,6 +264,13 @@ def _uses_fp8_ds_mla_layout(self) -> bool:; symbols: _uses_fp8_ds_mla_layout, _indexer_cls, __init__
  - `vllm/config/attention.py` modified +4/-1 (5 lines); hunks: -93,7 +93,10 @@ class AttentionConfig:; symbols: AttentionConfig, GPU
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -2,8 +2,9 @@
+from collections.abc import Callable
-from typing import cast
+from typing import Any, cast
@@ -15,8 +16,14 @@
+from vllm.model_executor.layers.rocm_paged_mxfp4_indexer import (
+    RocmSparseAttnIndexer,
diff -- vllm/models/deepseek_v41/attention.py
@@ -35,6 +35,9 @@
+    from vllm.model_executor.layers.rocm_paged_mxfp4_indexer import (
+        RocmSparseMQAIndexer,
+    )
@@ -261,6 +264,13 @@ def _uses_fp8_ds_mla_layout(self) -> bool:
+    def _indexer_cls(
+        self, k_cache: "DeepseekV4IndexerCache | None"
diff -- vllm/config/attention.py
@@ -93,7 +93,10 @@ class AttentionConfig:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +149/-1; `vllm/models/deepseek_v41/attention.py` modified +34/-6; `vllm/config/attention.py` modified +4/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_paged_mxfp4_indexer.py`, `tests/v1/attention/test_rocm_paged_mxfp4_indexer_plan.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58655 - [ROCm][DSv4.1][Perf] Run the delayed mHC seams through aiter's fused Triton kernel

- Link: https://github.com/vllm-project/vllm/pull/58655
- Status/date: merged / 2026-09-29
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/model.py`; associated commits `0af34418e99b`
- Diff scope read: GitHub Pull Request files API returned 6 files, +324/-16, 473 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Run the delayed mHC seams through aiter's fused Triton kernel"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/model.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Run the delayed mHC seams through aiter's fused Triton kernel"; the main implementation surface is `vllm/models/deepseek_v41/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/model.py` modified +29/-4 (33 lines); hunks: -22,7 +22,11; -251,6 +255,10 @@ def __init__(; symbols: __init__, _hc_collapse, forward, touching `__init__, _hc_collapse, forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/model.py` modified +29/-4 (33 lines); hunks: -22,7 +22,11; -251,6 +255,10 @@ def __init__(; symbols: __init__, _hc_collapse, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -22,7 +22,11 @@
-from vllm.model_executor.layers.mhc import MHCPostOp, MHCPreDelayedOp
+from vllm.model_executor.layers.mhc import (
+    HAS_AITER_MHC_FUSED_POST_PRE_DELAYED_RMS_NORM,
+    MHCPostOp,
+    MHCPreDelayedOp,
+)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/model.py` modified +29/-4
- Risk and verification: The diff ships test coverage in `tests/kernels/mhc/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58983 - [ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform

- Link: https://github.com/vllm-project/vllm/pull/58983
- Status/date: merged / 2026-09-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `7ba3df63cbe2`
- Diff scope read: GitHub Pull Request files API returned 4 files, +40/-37, 126 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/platforms/rocm.py`; technical summary: Covers "[ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/platforms/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +6/-19 (25 lines); hunks: -649,23 +649,6 @@ def __init__(self, *args, **kwargs):; -709,7 +692,9 @@ def forward(; symbols: __init__, _enable_multi_stream_overlap, _run_sequential_pipeline, forward, touching `__init__, _enable_multi_stream_overlap, _run_sequential_pipeline`; `vllm/models/deepseek_v41/amd/rocm.py` modified +3/-18 (21 lines); hunks: -615,23 +615,6 @@ def _run_parallel_input_projections(; -641,7 +624,9 @@ def forward(; symbols: _run_parallel_input_projections, _enable_multi_stream_overlap, forward, touching `_run_parallel_input_projections, _enable_multi_stream_overlap, forward`; `vllm/platforms/rocm.py` modified +21/-0 (21 lines); hunks: -1106,6 +1106,27 @@ def opaque_attention_op(cls) -> bool:; symbols: opaque_attention_op, is_navi, enable_multi_stream_overlap, get_static_graph_wrapper_cls, touching `opaque_attention_op, is_navi, enable_multi_stream_overlap`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +6/-19 (25 lines); hunks: -649,23 +649,6 @@ def __init__(self, *args, **kwargs):; -709,7 +692,9 @@ def forward(; symbols: __init__, _enable_multi_stream_overlap, _run_sequential_pipeline, forward
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +3/-18 (21 lines); hunks: -615,23 +615,6 @@ def _run_parallel_input_projections(; -641,7 +624,9 @@ def forward(; symbols: _run_parallel_input_projections, _enable_multi_stream_overlap, forward
  - `vllm/platforms/rocm.py` modified +21/-0 (21 lines); hunks: -1106,6 +1106,27 @@ def opaque_attention_op(cls) -> bool:; symbols: opaque_attention_op, is_navi, enable_multi_stream_overlap, get_static_graph_wrapper_cls
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -649,23 +649,6 @@ def __init__(self, *args, **kwargs):
-    def _enable_multi_stream_overlap(self) -> bool:
-        """ROCm multi-stream gates: streams and capture region.
-        Dict metadata marks piecewise cudagraph, whose eager breaks rebuild
-        the attention inputs on the owning stream. Forking side streams
-        there would rely on runtime HIP event sync, which is unreliable in
-        this overlap on ROCm (event waits can hang), so multi-stream only
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -615,23 +615,6 @@ def _run_parallel_input_projections(
-    def _enable_multi_stream_overlap(self) -> bool:
-        """ROCm multi-stream gates: streams and capture region.
-        Dict metadata marks piecewise cudagraph, whose eager breaks rebuild
-        the attention inputs on the owning stream. Forking side streams
-        there would rely on runtime HIP event sync, which is unreliable in
-        this overlap on ROCm (event waits can hang), so multi-stream only
diff -- vllm/platforms/rocm.py
@@ -1106,6 +1106,27 @@ def opaque_attention_op(cls) -> bool:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +6/-19; `vllm/models/deepseek_v41/amd/rocm.py` modified +3/-18; `vllm/platforms/rocm.py` modified +21/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/platforms/interface.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57568 - [Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter

- Link: https://github.com/vllm-project/vllm/pull/57568
- Status/date: merged / 2026-09-28
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/mtp.py`; associated commits `f6877f563c5b`
- Diff scope read: GitHub Pull Request files API returned 2 files, +200/-6, 237 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/amd/mtp.py`; technical summary: Covers "[Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter"; the main implementation surface is `vllm/models/deepseek_v4/amd/mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/mtp.py` modified +37/-6 (43 lines); hunks: -240,13 +240,11 @@ def forward(; -260,14 +258,38 @@ def compute_logits(; symbols: forward, compute_logits, _pre_head, touching `forward, compute_logits, _pre_head`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/mtp.py` modified +37/-6 (43 lines); hunks: -240,13 +240,11 @@ def forward(; -260,14 +258,38 @@ def compute_logits(; symbols: forward, compute_logits, _pre_head
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/mtp.py
@@ -240,13 +240,11 @@ def forward(
-    def compute_logits(
+    def _pre_head(
+        mtp_layer: DeepSeekV4MultiTokenPredictorLayer,
-        spec_step_idx: int = 0,
-        current_step_idx = spec_step_idx % self.num_mtp_layers
-        mtp_layer = self.layers[str(self.mtp_start_layer_idx + current_step_idx)]
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/mtp.py` modified +37/-6
- Risk and verification: The diff ships test coverage in `tests/v1/spec_decode/test_dsv4_mtp_local_argmax.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57407 - [ROCm][Perf] Enable layer-aware CSA2 multi-stream overlap for DeepSeek-V4.1-Flash

- Link: https://github.com/vllm-project/vllm/pull/57407
- Status/date: merged / 2026-09-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`; associated commits `44af287ebe38`
- Diff scope read: GitHub Pull Request files API returned 4 files, +496/-20, 592 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Enable layer-aware CSA2 multi-stream overlap for DeepSeek-V4.1-Flash"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`; technical summary: Covers "[ROCm][Perf] Enable layer-aware CSA2 multi-stream overlap for DeepSeek-V4.1-Flash"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +189/-0 (189 lines); hunks: -29,6 +29,7; -529,6 +530,9 @@ def __init__(self, *args, **kwargs):; symbols: __init__, get_padded_num_q_heads, _fused_wqa_wkv_gemm, _run_parallel_input_projections, touching `__init__, get_padded_num_q_heads, _fused_wqa_wkv_gemm`; `vllm/models/deepseek_v41/attention.py` modified +32/-18 (50 lines); hunks: -478,7 +478,6 @@ def __init__(; -1381,6 +1380,37 @@ def _produce_k(; symbols: __init__, _produce_k, forward_q, forward, touching `__init__, _produce_k, forward_q`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +189/-0 (189 lines); hunks: -29,6 +29,7; -529,6 +530,9 @@ def __init__(self, *args, **kwargs):; symbols: __init__, get_padded_num_q_heads, _fused_wqa_wkv_gemm, _run_parallel_input_projections
  - `vllm/models/deepseek_v41/attention.py` modified +32/-18 (50 lines); hunks: -478,7 +478,6 @@ def __init__(; -1381,6 +1380,37 @@ def _produce_k(; symbols: __init__, _produce_k, forward_q, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -29,6 +29,7 @@
+from vllm.utils.multi_stream_utils import execute_in_parallel
@@ -529,6 +530,9 @@ def __init__(self, *args, **kwargs):
+        if self.compressor is None and self.indexer is None:
+            # Dense layers have nothing to overlap; keep the base serial path.
+            self.aux_stream_list = None
@@ -600,8 +604,193 @@ def _fused_wqa_wkv_gemm(self, hidden_states: torch.Tensor) -> torch.Tensor:
diff -- vllm/models/deepseek_v41/attention.py
@@ -478,7 +478,6 @@ def __init__(
-        # Will be None on ROCm for now.
@@ -1381,6 +1380,37 @@ def _produce_k(
+    def forward_q(
+        self,
+        qr: torch.Tensor | QuantizedActivation,
+        qr_scale: torch.Tensor | None,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +189/-0; `vllm/models/deepseek_v41/attention.py` modified +32/-18
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58634 - [Perf][DSv4.1] Fuse small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103

- Link: https://github.com/vllm-project/vllm/pull/58634
- Status/date: merged / 2026-09-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`; associated commits `a9eafde59cbd`
- Diff scope read: GitHub Pull Request files API returned 6 files, +759/-55, 899 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Fuse small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`; technical summary: Covers "[Perf][DSv4.1] Fuse small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: _ue8m0_rp, _rope_fma, _scale, FusedWoAKernel, touching `_ue8m0_rp, _rope_fma, _scale`; `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` added +95/-0 (95 lines); hunks: -0,0 +1,95; symbols: _fused_wo_a_max_tokens, _can_fuse_wo_a, register_dsv41_o_proj_warmup, dsv41_o_proj, touching `_fused_wo_a_max_tokens, _can_fuse_wo_a, register_dsv41_o_proj_warmup`; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +8/-34 (42 lines); hunks: -9,15 +9,16; -242,27 +243,14 @@ def get_padded_num_q_heads(cls, num_heads: int) -> int:; symbols: get_padded_num_q_heads, _o_proj, __init__, touching `get_padded_num_q_heads, _o_proj, __init__`; `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +7/-19 (26 lines); hunks: -6,16 +6,17; -57,23 +58,10 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _o_proj, get_padded_num_q_heads, touching `__init__, _o_proj, get_padded_num_q_heads`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py` added +599/-0 (599 lines); hunks: -0,0 +1,599; symbols: _ue8m0_rp, _rope_fma, _scale, FusedWoAKernel
  - `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` added +95/-0 (95 lines); hunks: -0,0 +1,95; symbols: _fused_wo_a_max_tokens, _can_fuse_wo_a, register_dsv41_o_proj_warmup, dsv41_o_proj
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +8/-34 (42 lines); hunks: -9,15 +9,16; -242,27 +243,14 @@ def get_padded_num_q_heads(cls, num_heads: int) -> int:; symbols: get_padded_num_q_heads, _o_proj, __init__
  - `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +7/-19 (26 lines); hunks: -6,16 +6,17; -57,23 +58,10 @@ def __init__(self, *args, **kwargs) -> None:; symbols: __init__, _o_proj, get_padded_num_q_heads
  - `vllm/models/deepseek_v41/attention.py` modified +2/-2 (4 lines); hunks: -697,7 +697,7 @@ def bind_gemm_rs(self) -> None:; -707,7 +707,7 @@ def _wo_b_proj(self, z: torch.Tensor) -> torch.Tensor:; symbols: bind_gemm_rs, _wo_b_proj
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py
@@ -0,0 +1,599 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DSV4.1 small-batch MXFP8 WO-A with inverse RoPE and quantization."""
+from dataclasses import dataclass
+from typing import Any
+import cutlass
diff -- vllm/models/deepseek_v41/nvidia/ops/o_proj.py
@@ -0,0 +1,95 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DSV4.1 output projection with a small-batch SM100/SM103 fusion."""
+import torch
+from torch import nn
+from vllm.model_executor.kernels.linear.mxfp8.flashinfer import (
diff -- vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py
@@ -9,15 +9,16 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/fused_wo_a.py` added +599/-0; `vllm/models/deepseek_v41/nvidia/ops/o_proj.py` added +95/-0; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +8/-34; `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +7/-19; `vllm/models/deepseek_v41/attention.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/test_fused_inv_rope_fp8_quant.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58586 - [Kernel][DSV4.1] Fuse MoE finalize into the TP all-reduce + mHC boundary

- Link: https://github.com/vllm-project/vllm/pull/58586
- Status/date: merged / 2026-09-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/__init__.py`, `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`; associated commits `77871126f9b6`
- Diff scope read: GitHub Pull Request files API returned 8 files, +1807/-309, 2312 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel][DSV4.1] Fuse MoE finalize into the TP all-reduce + mHC boundary"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Kernel][DSV4.1] Fuse MoE finalize into the TP all-reduce + mHC boundary"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` added +1134/-0 (1134 lines); hunks: -0,0 +1,1134; symbols: _group_leader_block_sum, _SharedOnlyPublishDeviceKernel, __init__, __call__, touching `_group_leader_block_sum, _SharedOnlyPublishDeviceKernel, __init__`; `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +73/-18 (91 lines); hunks: -9,10 +9,15; -24,9 +29,17; symbols: supports_mhc_overlap, supports_mhc_all_reduce, init_mhc_all_reduce, mhc_pre_delayed_overlap, touching `supports_mhc_overlap, supports_mhc_all_reduce, init_mhc_all_reduce`; `vllm/models/deepseek_v41/nvidia/model.py` modified +76/-4 (80 lines); hunks: -33,6 +33,14; -94,6 +102,7; symbols: __init__, defer_finalize, defers_finalize, forward_unfinalized, touching `__init__, defer_finalize, defers_finalize`; `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/__init__.py` added +8/-0 (8 lines); hunks: -0,0 +1,8.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` added +1134/-0 (1134 lines); hunks: -0,0 +1,1134; symbols: _group_leader_block_sum, _SharedOnlyPublishDeviceKernel, __init__, __call__
  - `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +73/-18 (91 lines); hunks: -9,10 +9,15; -24,9 +29,17; symbols: supports_mhc_overlap, supports_mhc_all_reduce, init_mhc_all_reduce, mhc_pre_delayed_overlap
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +76/-4 (80 lines); hunks: -33,6 +33,14; -94,6 +102,7; symbols: __init__, defer_finalize, defers_finalize, forward_unfinalized
  - `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/__init__.py` added +8/-0 (8 lines); hunks: -0,0 +1,8
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py
@@ -0,0 +1,1134 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# Adapted from FlashInfer's low-latency MNNVL CuTe DSL all-reduce
+# (flashinfer/comm/mnnvl_cutedsl/kernel_ll, flashinfer-ai/flashinfer@139af6f6).
+"""Lamport all-reduce fused with DSV4.1's mHC post, collapse and RMSNorm.
+FlashInfer's LL kernels, copied: a publish kernel (or its MoE finalize
diff -- vllm/models/deepseek_v41/nvidia/ops/mhc.py
@@ -9,10 +9,15 @@
+from vllm.logger import init_logger
+from vllm.model_executor.layers.fused_moe.moe_output import (
+    MoEOutput,
+    UnfinalizedMoEOutput,
+)
@@ -24,9 +29,17 @@
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -33,6 +33,14 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc.py` added +1134/-0; `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +73/-18; `vllm/models/deepseek_v41/nvidia/model.py` modified +76/-4; `vllm/models/deepseek_v41/nvidia/ops/cute_dsl/__init__.py` added +8/-0
- Risk and verification: The diff ships test coverage in `tests/distributed/test_custom_all_reduce.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58499 - [Bugfix][DSV4.1] Avoid host sync in ViT CUDA graph replay metadata

- Link: https://github.com/vllm-project/vllm/pull/58499
- Status/date: merged / 2026-09-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/common/vl_cudagraph.py`; associated commits `7d8c5fe9a95d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +24/-15, 92 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSV4.1] Avoid host sync in ViT CUDA graph replay metadata"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/models/deepseek_v4/common/vision.py`; technical summary: Covers "[Bugfix][DSV4.1] Avoid host sync in ViT CUDA graph replay metadata"; the main implementation surface is `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/models/deepseek_v4/common/vision.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/vl_cudagraph.py` modified +14/-8 (22 lines); hunks: -25,6 +25,7; -370,18 +371,23 @@ def postprocess_encoder_output(; symbols: postprocess_encoder_output, touching `postprocess_encoder_output`; `vllm/models/deepseek_v4/common/vision.py` modified +10/-7 (17 lines); hunks: -38,6 +38,7; -219,8 +220,8 @@ def forward(; symbols: _compute_vision_cos_sin, forward, build_packed_vit_metadata, build_packed_merge_metadata, touching `_compute_vision_cos_sin, forward, build_packed_vit_metadata`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/vl_cudagraph.py` modified +14/-8 (22 lines); hunks: -25,6 +25,7; -370,18 +371,23 @@ def postprocess_encoder_output(; symbols: postprocess_encoder_output
  - `vllm/models/deepseek_v4/common/vision.py` modified +10/-7 (17 lines); hunks: -38,6 +38,7; -219,8 +220,8 @@ def forward(; symbols: _compute_vision_cos_sin, forward, build_packed_vit_metadata, build_packed_merge_metadata
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/vl_cudagraph.py
@@ -25,6 +25,7 @@
+from vllm.utils.torch_utils import async_tensor_h2d
@@ -370,18 +371,23 @@ def postprocess_encoder_output(
-        types = batch_mm_kwargs["types"].to(aligner_out.device)
+        types = batch_mm_kwargs["types"]
-        # Batched span assembly: one masked fill per role across all items.
-        dtype = aligner_out.dtype
diff -- vllm/models/deepseek_v4/common/vision.py
@@ -38,6 +38,7 @@
+from vllm.utils.torch_utils import async_tensor_h2d
@@ -219,8 +220,8 @@ def forward(
-        cos = cos.to(device=x.device)
-        sin = sin.to(device=x.device)
+        cos = async_tensor_h2d(cos, x.device)
+        sin = async_tensor_h2d(sin, x.device)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/vl_cudagraph.py` modified +14/-8; `vllm/models/deepseek_v4/common/vision.py` modified +10/-7
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/common/vl_cudagraph.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58316 - [Bugfix][Frontend][Rust Frontend] Update DeepSeek V4.1 Flash reasoning effort mappings

- Link: https://github.com/vllm-project/vllm/pull/58316
- Status/date: merged / 2026-09-26
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`; associated commits `ddd6fbca148a`
- Diff scope read: GitHub Pull Request files API returned 9 files, +20/-20, 119 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Frontend][Rust Frontend] Update DeepSeek V4.1 Flash reasoning effort mappings"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt`; technical summary: Covers "[Bugfix][Frontend][Rust Frontend] Update DeepSeek V4.1 Flash reasoning effort mappings"; the main implementation surface is `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41_encoding.py`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v41.py` modified +4/-4 (8 lines); hunks: -35,9 +35,9 @@ def test_reference_encoder_fixtures(case_id):; -138,7 +138,7 @@ def test_top_level_effort_overrides_template_effort():; symbols: test_reference_encoder_fixtures, test_top_level_effort_overrides_template_effort, test_encode_uses_one_bos_and_forwards_truncation, touching `test_reference_encoder_fixtures, test_top_level_effort_overrides_template_effort, test_encode_uses_one_bos_and_forwards_truncation`; `vllm/tokenizers/deepseek_v41_encoding.py` modified +2/-2 (4 lines); hunks: -181,8 +181,8 @@ def sort_tool_results_by_call_order(; symbols: sort_tool_results_by_call_order, touching `sort_tool_results_by_call_order`; `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt` modified +1/-1 (2 lines); hunks: -1,4 +1,4; `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt` modified +1/-1 (2 lines); hunks: -1,3 +1,3.
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v41.py` modified +4/-4 (8 lines); hunks: -35,9 +35,9 @@ def test_reference_encoder_fixtures(case_id):; -138,7 +138,7 @@ def test_top_level_effort_overrides_template_effort():; symbols: test_reference_encoder_fixtures, test_top_level_effort_overrides_template_effort, test_encode_uses_one_bos_and_forwards_truncation
  - `vllm/tokenizers/deepseek_v41_encoding.py` modified +2/-2 (4 lines); hunks: -181,8 +181,8 @@ def sort_tool_results_by_call_order(; symbols: sort_tool_results_by_call_order
  - `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt` modified +1/-1 (2 lines); hunks: -1,4 +1,4
  - `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt` modified +1/-1 (2 lines); hunks: -1,3 +1,3
  - `rust/src/chat/src/renderer/deepseek_v41/fixtures/test_output_1.txt` modified +1/-1 (2 lines); hunks: -1,4 +1,4
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -35,9 +35,9 @@ def test_reference_encoder_fixtures(case_id):
-        (None, 50),
-        ("low", 25),
-        ("high", 50),
+        (None, 75),
+        ("low", 50),
+        ("high", 75),
diff -- vllm/tokenizers/deepseek_v41_encoding.py
@@ -181,8 +181,8 @@ def sort_tool_results_by_call_order(
-    "low": 25,
-    "high": 50,
+    "low": 50,
+    "high": 75,
diff -- tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt
@@ -1,4 +1,4 @@
-<｜begin▁of▁sentence｜><｜System｜>Reasoning Effort: 50 (range 1-100, the higher the value, the more thorough the reasoning)
+<｜begin▁of▁sentence｜><｜System｜>Reasoning Effort: 75 (range 1-100, the higher the value, the more thorough the reasoning)
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v41.py` modified +4/-4; `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt` modified +1/-1; `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt` modified +1/-1
  - runtime: `vllm/tokenizers/deepseek_v41_encoding.py` modified +2/-2
  - other: `rust/src/chat/src/renderer/deepseek_v41/fixtures/test_output_1.txt` modified +1/-1; `rust/src/chat/src/renderer/deepseek_v41/fixtures/test_output_2.txt` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt`, `tests/tokenizers_/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57071 - [Bugfix][ROCm] AMD-Quark mixed-precision DeepSeek-V4.1 support

- Link: https://github.com/vllm-project/vllm/pull/57071
- Status/date: merged / 2026-09-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/quant_config.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/quant_config.py`; associated commits `5840d95284fe`
- Diff scope read: GitHub Pull Request files API returned 11 files, +647/-102, 1009 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm] AMD-Quark mixed-precision DeepSeek-V4.1 support"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/quant_config.py`, `vllm/models/deepseek_v4/quant_config.py`; technical summary: Covers "[Bugfix][ROCm] AMD-Quark mixed-precision DeepSeek-V4.1 support"; the main implementation surface is `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/quant_config.py`, `vllm/models/deepseek_v4/quant_config.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/vl_model.py` modified +26/-8 (34 lines); hunks: -79,20 +79,22 @@ class DeepseekV4VLImagePixelInputs(TensorSchema):; -131,6 +133,22 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, attributes, touching `DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM`; `vllm/models/deepseek_v41/quant_config.py` modified +9/-7 (16 lines); hunks: -139,15 +139,17 @@ def _is_quark_mxfp4_ocp(hf_quant_cfg: dict) -> bool:; symbols: _is_quark_mxfp4_ocp, override_quantization_method, touching `_is_quark_mxfp4_ocp, override_quantization_method`; `vllm/models/deepseek_v4/quant_config.py` modified +7/-7 (14 lines); hunks: -135,15 +135,15 @@ def _is_quark_mxfp4_ocp(hf_quant_cfg: dict) -> bool:; symbols: _is_quark_mxfp4_ocp, override_quantization_method, touching `_is_quark_mxfp4_ocp, override_quantization_method`; `vllm/models/deepseek_v41/amd/model.py` modified +10/-0 (10 lines); hunks: -895,6 +895,11 @@ def _make_deepseek_v4_weights_mapper(; -908,6 +913,11 @@ def _make_deepseek_v4_weights_mapper(; symbols: _make_deepseek_v4_weights_mapper, touching `_make_deepseek_v4_weights_mapper`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/vl_model.py` modified +26/-8 (34 lines); hunks: -79,20 +79,22 @@ class DeepseekV4VLImagePixelInputs(TensorSchema):; -131,6 +133,22 @@ class DeepseekV41ForCausalLM(; symbols: DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, attributes
  - `vllm/models/deepseek_v41/quant_config.py` modified +9/-7 (16 lines); hunks: -139,15 +139,17 @@ def _is_quark_mxfp4_ocp(hf_quant_cfg: dict) -> bool:; symbols: _is_quark_mxfp4_ocp, override_quantization_method
  - `vllm/models/deepseek_v4/quant_config.py` modified +7/-7 (14 lines); hunks: -135,15 +135,15 @@ def _is_quark_mxfp4_ocp(hf_quant_cfg: dict) -> bool:; symbols: _is_quark_mxfp4_ocp, override_quantization_method
  - `vllm/models/deepseek_v41/amd/model.py` modified +10/-0 (10 lines); hunks: -895,6 +895,11 @@ def _make_deepseek_v4_weights_mapper(; -908,6 +913,11 @@ def _make_deepseek_v4_weights_mapper(; symbols: _make_deepseek_v4_weights_mapper
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/vl_model.py
@@ -79,20 +79,22 @@ class DeepseekV4VLImagePixelInputs(TensorSchema):
+_VL_PREFIX_MAPPING: dict[str, str | None] = {
+    "layers.": "language_model.model.layers.",
+    "embed.": "language_model.model.embed.",
+    "norm.": "language_model.model.norm.",
+    "hc_head": "language_model.model.hc_head",
+    "mtp.": "language_model.model.mtp.",
diff -- vllm/models/deepseek_v41/quant_config.py
@@ -139,15 +139,17 @@ def _is_quark_mxfp4_ocp(hf_quant_cfg: dict) -> bool:
+        # Quark checkpoints are always handled by QuarkConfig, which knows
+        # how to dispatch each per-layer scheme (MXFP4, MXFP8, etc.).
+        # ``from_config`` below rewrites the config into a single global FP8
+        # scheme, which would discard per-layer specs — so never claim Quark.
+        if isinstance(hf_quant_cfg, dict) and (
+            hf_quant_cfg.get("quant_method") == "quark"
diff -- vllm/models/deepseek_v4/quant_config.py
@@ -135,15 +135,15 @@ def _is_quark_mxfp4_ocp(hf_quant_cfg: dict) -> bool:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/vl_model.py` modified +26/-8; `vllm/models/deepseek_v41/quant_config.py` modified +9/-7; `vllm/models/deepseek_v4/quant_config.py` modified +7/-7; `vllm/models/deepseek_v41/amd/model.py` modified +10/-0
- Risk and verification: The diff ships test coverage in `tests/quantization/test_fp8.py`, `tests/quantization/test_quark.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58678 - [Perf][DSv4.1] Shard the Engram wkv projection across TP ranks

- Link: https://github.com/vllm-project/vllm/pull/58678
- Status/date: merged / 2026-09-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/engram.py`; associated commits `4bb804cc5bf0`
- Diff scope read: GitHub Pull Request files API returned 2 files, +7/-3, 37 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Shard the Engram wkv projection across TP ranks"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/engram.py`, `tests/kernels/test_engram.py`; technical summary: Covers "[Perf][DSv4.1] Shard the Engram wkv projection across TP ranks"; the main implementation surface is `vllm/models/deepseek_v41/common/engram.py`, `tests/kernels/test_engram.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/engram.py` modified +6/-2 (8 lines); hunks: -47,7 +47,7; -923,13 +923,17 @@ def __init__(; symbols: __init__, touching `__init__`; `tests/kernels/test_engram.py` modified +1/-1 (2 lines); hunks: -827,7 +827,7 @@ def test_engram_constructor_honors_offload(monkeypatch, back...; symbols: test_engram_constructor_honors_offload, touching `test_engram_constructor_honors_offload`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/engram.py` modified +6/-2 (8 lines); hunks: -47,7 +47,7; -923,13 +923,17 @@ def __init__(; symbols: __init__
  - `tests/kernels/test_engram.py` modified +1/-1 (2 lines); hunks: -827,7 +827,7 @@ def test_engram_constructor_honors_offload(monkeypatch, back...; symbols: test_engram_constructor_honors_offload
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/engram.py
@@ -47,7 +47,7 @@
-from vllm.model_executor.layers.linear import ReplicatedLinear
+from vllm.model_executor.layers.linear import ColumnParallelLinear
@@ -923,13 +923,17 @@ def __init__(
-        self.wkv = ReplicatedLinear(
+        # Without sequence parallelism every TP rank holds every token, so
+        # shard the output columns instead of replicating the projection.
diff -- tests/kernels/test_engram.py
@@ -827,7 +827,7 @@ def test_engram_constructor_honors_offload(monkeypatch, backend, cpu_offload):
-        engram_ops, "ReplicatedLinear", lambda *a, **k: torch.nn.Identity()
+        engram_ops, "ColumnParallelLinear", lambda *a, **k: torch.nn.Identity()
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/engram.py` modified +6/-2
  - tests: `tests/kernels/test_engram.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/test_engram.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58740 - [ROCm][CI] Test AMD DeepSeek V4 MoE routing against a PyTorch reference

- Link: https://github.com/vllm-project/vllm/pull/58740
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_vl_rocm.py`; associated commits `e3dd5b5a758a`
- Diff scope read: GitHub Pull Request files API returned 1 files, +126/-0, 133 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][CI] Test AMD DeepSeek V4 MoE routing against a PyTorch reference"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v4_vl_rocm.py`; technical summary: Covers "[ROCm][CI] Test AMD DeepSeek V4 MoE routing against a PyTorch reference"; the main implementation surface is `tests/models/test_deepseek_v4_vl_rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_vl_rocm.py` modified +126/-0 (126 lines); hunks: -16,6 +16,132; symbols: test_rocm_moe_routing_and_shared_experts_match_reference, expert_reference, test_rocm_packed_kv_cache_auto_uses_ds_mla_layout, touching `test_rocm_moe_routing_and_shared_experts_match_reference, expert_reference, test_rocm_packed_kv_cache_auto_uses_ds_mla_layout`.
- Code diff details:
  - `tests/models/test_deepseek_v4_vl_rocm.py` modified +126/-0 (126 lines); hunks: -16,6 +16,132; symbols: test_rocm_moe_routing_and_shared_experts_match_reference, expert_reference, test_rocm_packed_kv_cache_auto_uses_ds_mla_layout
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_vl_rocm.py
@@ -16,6 +16,132 @@
+@pytest.mark.parametrize("hash_routing", [False, True], ids=["regular", "hash"])
+@pytest.mark.parametrize("vision", [False, True], ids=["text", "vision"])
+@torch.inference_mode()
+def test_rocm_moe_routing_and_shared_experts_match_reference(
+    hash_routing, vision, monkeypatch, default_vllm_config, dist_init
+) -> None:
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_vl_rocm.py` modified +126/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_vl_rocm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #58621 - [Perf][DSv4] Fuse inverse RoPE + FP8 quant into FlashInfer sparse MLA

- Link: https://github.com/vllm-project/vllm/pull/58621
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`; associated commits `5ff3bbfb089a`
- Diff scope read: GitHub Pull Request files API returned 5 files, +583/-104, 984 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4] Fuse inverse RoPE + FP8 quant into FlashInfer sparse MLA"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`; technical summary: Covers "[Perf][DSv4] Fuse inverse RoPE + FP8 quant into FlashInfer sparse MLA"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +116/-60 (176 lines); hunks: -9,6 +9,8; -17,6 +19,8; symbols: DeepseekV4FlashInferMLAAttention, get_padded_num_q_heads, _o_proj, touching `DeepseekV4FlashInferMLAAttention, get_padded_num_q_heads, _o_proj`; `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +83/-16 (99 lines); hunks: -5,11 +5,15; -29,7 +33,7 @@ def compute_fp8_einsum_recipe(; symbols: compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj, touching `compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj`; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +72/-8 (80 lines); hunks: -1099,6 +1099,7 @@ def build_flashinfer_mixed_sparse_indices(; -1109,6 +1110,9 @@ def build_flashinfer_mixed_sparse_indices(; symbols: build_flashinfer_mixed_sparse_indices, kernel, touching `build_flashinfer_mixed_sparse_indices, kernel`; `vllm/models/deepseek_v4/attention.py` modified +37/-20 (57 lines); hunks: -43,6 +43,7; -171,14 +172,20 @@ def forward_mqa(; symbols: forward_mqa, _o_proj, _uses_fp8_ds_mla_layout, forward, touching `forward_mqa, _o_proj, _uses_fp8_ds_mla_layout`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +116/-60 (176 lines); hunks: -9,6 +9,8; -17,6 +19,8; symbols: DeepseekV4FlashInferMLAAttention, get_padded_num_q_heads, _o_proj
  - `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +83/-16 (99 lines); hunks: -5,11 +5,15; -29,7 +33,7 @@ def compute_fp8_einsum_recipe(; symbols: compute_fp8_einsum_recipe, deep_gemm_fp8_o_proj
  - `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +72/-8 (80 lines); hunks: -1099,6 +1099,7 @@ def build_flashinfer_mixed_sparse_indices(; -1109,6 +1110,9 @@ def build_flashinfer_mixed_sparse_indices(; symbols: build_flashinfer_mixed_sparse_indices, kernel
  - `vllm/models/deepseek_v4/attention.py` modified +37/-20 (57 lines); hunks: -43,6 +43,7; -171,14 +172,20 @@ def forward_mqa(; symbols: forward_mqa, _o_proj, _uses_fp8_ds_mla_layout, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py
@@ -9,6 +9,8 @@
+from vllm.logger import init_logger
+from vllm.model_executor.layers.fusion.quant_activation import QuantizedActivation
@@ -17,6 +19,8 @@
+    rope_quant_attn_out,
+    rope_quant_unsupported_reason,
@@ -37,6 +41,8 @@
diff -- vllm/models/deepseek_v4/nvidia/ops/o_proj.py
@@ -5,11 +5,15 @@
+from vllm.model_executor.layers.fusion.quant_activation import QuantizedActivation
+from vllm.model_executor.layers.quantization.utils.quant_utils import (
+    kFp8Dynamic128Sym,
+)
-from vllm.utils.deep_gemm import fp8_einsum
+from vllm.utils.deep_gemm import fp8_einsum, get_tma_aligned_size
diff -- vllm/models/deepseek_v4/common/ops/cache_utils.py
@@ -1099,6 +1099,7 @@ def build_flashinfer_mixed_sparse_indices(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +116/-60; `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +83/-16; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +72/-8; `vllm/models/deepseek_v4/attention.py` modified +37/-20
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_flashmla_sparse.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57679 - [Perf][DSv4.1] Restore the fused query RMSNorm + MXFP8 quantization path

- Link: https://github.com/vllm-project/vllm/pull/57679
- Status/date: merged / 2026-09-25
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/common/ops/query_quant.py`; associated commits `609731e8f56c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +8/-3, 40 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Restore the fused query RMSNorm + MXFP8 quantization path"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/ops/query_quant.py`; technical summary: Covers "[Perf][DSv4.1] Restore the fused query RMSNorm + MXFP8 quantization path"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/query_quant.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-3 (11 lines); hunks: -3,7 +3,10; -102,6 +105,7 @@ def fused_q_kv_rmsnorm_quant(; symbols: fused_q_kv_rmsnorm_quant, can_fuse_query_quant, touching `fused_q_kv_rmsnorm_quant, can_fuse_query_quant`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-3 (11 lines); hunks: -3,7 +3,10; -102,6 +105,7 @@ def fused_q_kv_rmsnorm_quant(; symbols: fused_q_kv_rmsnorm_quant, can_fuse_query_quant
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/query_quant.py
@@ -3,7 +3,10 @@
-from vllm.model_executor.layers.fusion.quant_activation import QuantizedActivation
+from vllm.model_executor.layers.fusion.quant_activation import (
+    QuantizedActivation,
+    get_input_quant_key,
+)
@@ -102,6 +105,7 @@ def fused_q_kv_rmsnorm_quant(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/query_quant.py` modified +8/-3
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/common/ops/query_quant.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #58456 - [ROCm][DSv4.1][Perf] Emit MXFP8 from the sparse decode reduce and run wo_a as a grouped FP8 GEMM

- Link: https://github.com/vllm-project/vllm/pull/58456
- Status/date: merged / 2026-09-24
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `721d0e5c112a`
- Diff scope read: GitHub Pull Request files API returned 3 files, +664/-29, 957 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Emit MXFP8 from the sparse decode reduce and run wo_a as a grouped FP8 GEMM"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Emit MXFP8 from the sparse decode reduce and run wo_a as a grouped FP8 GEMM"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +136/-22 (158 lines); hunks: -13,6 +13,8; -37,7 +39,9; symbols: _split_qkv_and_norm, _o_proj, _alloc_attn_out, touching `_split_qkv_and_norm, _o_proj, _alloc_attn_out`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +136/-22 (158 lines); hunks: -13,6 +13,8; -37,7 +39,9; symbols: _split_qkv_and_norm, _o_proj, _alloc_attn_out
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -13,6 +13,8 @@
+from vllm.model_executor.layers.fusion.quant_activation import QuantizedActivation
+from vllm.model_executor.layers.quantization.utils.quant_utils import kMxfp8Dynamic
@@ -37,7 +39,9 @@
+    rocm_inverse_rope_mxfp8_rows,
+    rocm_mxfp8_wo_a_bmm,
@@ -663,7 +667,40 @@ def _split_qkv_and_norm(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +136/-22
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #44229 - [Feature][Frontend] Add DeepSeek-V4 FIM completion rendering

- Link: https://github.com/vllm-project/vllm/pull/44229
- Status/date: merged / 2026-09-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/renderers/deepseek_v4.py`; associated commits `d95a896ea612`
- Diff scope read: GitHub Pull Request files API returned 5 files, +243/-7, 323 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feature][Frontend] Add DeepSeek-V4 FIM completion rendering"; model line: DeepSeek V4; category: model support/runtime entry; main diff: `vllm/renderers/deepseek_v4.py`; technical summary: Covers "[Feature][Frontend] Add DeepSeek-V4 FIM completion rendering"; the main implementation surface is `vllm/renderers/deepseek_v4.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/renderers/deepseek_v4.py` modified +7/-0 (7 lines); hunks: -16,6 +16,10; -32,6 +36,9 @@ def __init__(; symbols: DeepseekV4Renderer, __init__, _apply_chat_template, render_completion_suffix, touching `DeepseekV4Renderer, __init__, _apply_chat_template`.
- Code diff details:
  - `vllm/renderers/deepseek_v4.py` modified +7/-0 (7 lines); hunks: -16,6 +16,10; -32,6 +36,9 @@ def __init__(; symbols: DeepseekV4Renderer, __init__, _apply_chat_template, render_completion_suffix
- Key code excerpts:

```diff
diff -- vllm/renderers/deepseek_v4.py
@@ -16,6 +16,10 @@
+_FIM_BEGIN = "<｜fim▁begin｜>"
+_FIM_HOLE = "<｜fim▁hole｜>"
+_FIM_END = "<｜fim▁end｜>"
@@ -32,6 +36,9 @@ def __init__(
+    def render_completion_suffix(self, prompt: str, suffix: str) -> str | None:
+        return f"{_FIM_BEGIN}{prompt}{_FIM_HOLE}{suffix}{_FIM_END}"
```

- Reviewed files:
  - runtime: `vllm/renderers/deepseek_v4.py` modified +7/-0
- Risk and verification: The diff ships test coverage in `tests/entrypoints/openai/completion/test_completion_error.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57451 - [ROCm][DSv4][Perf] Fuse the inverse RoPE into the sparse decode reduce

- Link: https://github.com/vllm-project/vllm/pull/57451
- Status/date: merged / 2026-09-23
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `f9dce295c96f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +27/-3, 84 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4][Perf] Fuse the inverse RoPE into the sparse decode reduce"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4][Perf] Fuse the inverse RoPE into the sparse decode reduce"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +27/-3 (30 lines); hunks: -37,6 +37,7; -1175,6 +1176,7 @@ def _o_proj(self, o: torch.Tensor, positions: torch.Tensor...; symbols: _o_proj, forward_mqa, _forward_decode, touching `_o_proj, forward_mqa, _forward_decode`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +27/-3 (30 lines); hunks: -37,6 +37,7; -1175,6 +1176,7 @@ def _o_proj(self, o: torch.Tensor, positions: torch.Tensor...; symbols: _o_proj, forward_mqa, _forward_decode
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -37,6 +37,7 @@
+    rocm_inverse_rope_rows_,
@@ -1175,6 +1176,7 @@ def _o_proj(self, o: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
+                inverse_rope=False,
@@ -1245,9 +1247,15 @@ def forward_mqa(
+        # The fp8 wo_a path rotates inside inverse_rope_group_quant, so folding
+        # the rotation into the decode reduce would apply it twice. Only the
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +27/-3
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57435 - [ROCm][DSv4.1][Perf] Fuse the inverse RoPE into the sparse decode reduce

- Link: https://github.com/vllm-project/vllm/pull/57435
- Status/date: merged / 2026-09-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `ca831d1c5571`
- Diff scope read: GitHub Pull Request files API returned 3 files, +184/-13, 412 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Fuse the inverse RoPE into the sparse decode reduce"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Fuse the inverse RoPE into the sparse decode reduce"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +22/-3 (25 lines); hunks: -37,6 +37,7; -673,6 +674,7 @@ def _o_proj(self, attn_out: torch.Tensor, positions: torch.T...; symbols: _o_proj, forward_mqa, _decode_topk_ragged, _forward_decode, touching `_o_proj, forward_mqa, _decode_topk_ragged`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +22/-3 (25 lines); hunks: -37,6 +37,7; -673,6 +674,7 @@ def _o_proj(self, attn_out: torch.Tensor, positions: torch.T...; symbols: _o_proj, forward_mqa, _decode_topk_ragged, _forward_decode
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -37,6 +37,7 @@
+    rocm_inverse_rope_rows_,
@@ -673,6 +674,7 @@ def _o_proj(self, attn_out: torch.Tensor, positions: torch.Tensor) -> torch.Tens
+            inverse_rope=False,
@@ -747,15 +749,28 @@ def forward_mqa(
+        rotated = 0
-            self._forward_decode(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +22/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57428 - [Kernel][DSV4.1] Fuse MXFP8 wo_b GEMM with sequence-parallel reduce-scatter

- Link: https://github.com/vllm-project/vllm/pull/57428
- Status/date: merged / 2026-09-22
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` and 7 files; associated commits `f92b78f6ef9c`
- Diff scope read: GitHub Pull Request files API returned 18 files, +1036/-623, 2293 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel][DSV4.1] Fuse MXFP8 wo_b GEMM with sequence-parallel reduce-scatter"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Kernel][DSV4.1] Fuse MXFP8 wo_b GEMM with sequence-parallel reduce-scatter"; the main implementation surface is `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/kimi_k3/nvidia/model.py` modified +13/-44 (57 lines); hunks: -160,54 +160,23 @@ def maybe_init_gemm_rs_ar(vllm_config: VllmConfig, use_seq...; -276,7 +245,7 @@ def __init__(; symbols: maybe_init_gemm_rs_ar, __init__, forward, touching `maybe_init_gemm_rs_ar, __init__, forward`; `vllm/models/deepseek_v41/attention.py` modified +40/-0 (40 lines); hunks: -26,13 +26,15; -389,6 +391,9 @@ def __init__(; symbols: __init__, forward, bind_gemm_rs, _wo_b_proj, touching `__init__, forward, bind_gemm_rs`; `vllm/models/deepseek_v41/nvidia/model.py` modified +37/-1 (38 lines); hunks: -193,6 +193,30 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; -202,6 +226,7 @@ def __init__(; symbols: _use_sequence_parallel, maybe_init_gemm_rs, DeepseekV4DecoderLayer, __init__, touching `_use_sequence_parallel, maybe_init_gemm_rs, DeepseekV4DecoderLayer`; `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +6/-2 (8 lines); hunks: -1,5 +1,7; -31,7 +33,7 @@ def deep_gemm_fp8_o_proj(; symbols: deep_gemm_fp8_o_proj, touching `deep_gemm_fp8_o_proj`.
- Code diff details:
  - `vllm/models/kimi_k3/nvidia/model.py` modified +13/-44 (57 lines); hunks: -160,54 +160,23 @@ def maybe_init_gemm_rs_ar(vllm_config: VllmConfig, use_seq...; -276,7 +245,7 @@ def __init__(; symbols: maybe_init_gemm_rs_ar, __init__, forward
  - `vllm/models/deepseek_v41/attention.py` modified +40/-0 (40 lines); hunks: -26,13 +26,15; -389,6 +391,9 @@ def __init__(; symbols: __init__, forward, bind_gemm_rs, _wo_b_proj
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +37/-1 (38 lines); hunks: -193,6 +193,30 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:; -202,6 +226,7 @@ def __init__(; symbols: _use_sequence_parallel, maybe_init_gemm_rs, DeepseekV4DecoderLayer, __init__
  - `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +6/-2 (8 lines); hunks: -1,5 +1,7; -31,7 +33,7 @@ def deep_gemm_fp8_o_proj(; symbols: deep_gemm_fp8_o_proj
  - `vllm/models/deepseek_v41/nvidia/dspark.py` modified +7/-0 (7 lines); hunks: -58,6 +58,7; -113,12 +114,18 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/models/kimi_k3/nvidia/model.py
@@ -160,54 +160,23 @@ def maybe_init_gemm_rs_ar(vllm_config: VllmConfig, use_sequence_parallel: bool)
-    enabled = envs.VLLM_KIMI_K3_GEMM_AR if all_reduce else envs.VLLM_KIMI_K3_GEMM_RS
+    enabled = envs.VLLM_KIMI_K3_GEMM_AR if all_reduce else envs.VLLM_ENABLE_GEMM_RS
-    parallel_config = vllm_config.parallel_config
-    tp_size = parallel_config.tensor_parallel_size
-    if parallel_config.use_ubatching:
-        reason = "ubatching is enabled"
diff -- vllm/models/deepseek_v41/attention.py
@@ -26,13 +26,15 @@
+from vllm.models.common.ops.sequence_parallel import sp_reduce_scatter
+    from vllm.model_executor.kernels.linear.cute_dsl.gemm_rs_ar import GemmRsAr
@@ -389,6 +391,9 @@ def __init__(
+        # Set by ``bind_gemm_rs`` when the decoder layer runs sequence
+        # parallel and the fused GEMM + reduce-scatter kernel accepts wo_b.
+        self.gemm_rs: GemmRsAr | None = None
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -193,6 +193,30 @@ def _use_sequence_parallel(vllm_config: VllmConfig) -> bool:
```

- Reviewed files:
  - runtime: `vllm/models/kimi_k3/nvidia/model.py` modified +13/-44; `vllm/models/deepseek_v41/attention.py` modified +40/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +37/-1; `vllm/models/deepseek_v4/nvidia/ops/o_proj.py` modified +6/-2; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +7/-0; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/test_gemm_rs_ar.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57919 - [ROCm][Bugfix] Explicitly reject FSE=1 with DPA+ETP deployment for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/57919
- Status/date: merged / 2026-09-22
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/model.py`; associated commits `42a85a497619`
- Diff scope read: GitHub Pull Request files API returned 2 files, +43/-5, 93 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Bugfix] Explicitly reject FSE=1 with DPA+ETP deployment for DeepSeek-V4"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/amd/model.py`, `tests/models/test_deepseek_v4_vl_rocm.py`; technical summary: Covers "[ROCm][Bugfix] Explicitly reject FSE=1 with DPA+ETP deployment for DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/model.py`, `tests/models/test_deepseek_v4_vl_rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/model.py` modified +21/-4 (25 lines); hunks: -12,7 +12,7; -504,11 +504,28 @@ def forward_modular(; symbols: forward_modular, _fuse_shared_experts_enabled, __init__, touching `forward_modular, _fuse_shared_experts_enabled, __init__`; `tests/models/test_deepseek_v4_vl_rocm.py` modified +22/-1 (23 lines); hunks: -7,6 +7,7; -100,7 +101,9 @@ def fake_factory(**kwargs):; symbols: fake_factory, test_rocm_fse_rejects_data_parallel_deployment, test_rocm_mtp_forwards_input_ids_for_vision_routing, touching `fake_factory, test_rocm_fse_rejects_data_parallel_deployment, test_rocm_mtp_forwards_input_ids_for_vision_routing`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/model.py` modified +21/-4 (25 lines); hunks: -12,7 +12,7; -504,11 +504,28 @@ def forward_modular(; symbols: forward_modular, _fuse_shared_experts_enabled, __init__
  - `tests/models/test_deepseek_v4_vl_rocm.py` modified +22/-1 (23 lines); hunks: -7,6 +7,7; -100,7 +101,9 @@ def fake_factory(**kwargs):; symbols: fake_factory, test_rocm_fse_rejects_data_parallel_deployment, test_rocm_mtp_forwards_input_ids_for_vision_routing
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -12,7 +12,7 @@
-from vllm.config import VllmConfig, get_current_vllm_config
+from vllm.config import ParallelConfig, VllmConfig
@@ -504,11 +504,28 @@ def forward_modular(
-def _fuse_shared_experts_enabled(config) -> bool:
+def _fuse_shared_experts_enabled(config, parallel_config: ParallelConfig) -> bool:
+    if (
diff -- tests/models/test_deepseek_v4_vl_rocm.py
@@ -7,6 +7,7 @@
+from vllm.config import ParallelConfig
@@ -100,7 +101,9 @@ def fake_factory(**kwargs):
-        model_config=SimpleNamespace(hf_config=config), quant_config=None
+        model_config=SimpleNamespace(hf_config=config),
+        quant_config=None,
+        parallel_config=ParallelConfig(),
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/model.py` modified +21/-4
  - tests: `tests/models/test_deepseek_v4_vl_rocm.py` modified +22/-1
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_vl_rocm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #52362 - [ROCm][DSv4] Enable DSpark adaptive verification

- Link: https://github.com/vllm-project/vllm/pull/52362
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_dspark_rocm.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `vllm/models/deepseek_v4/amd/dspark.py`, `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `e34685dfc0c9`
- Diff scope read: GitHub Pull Request files API returned 6 files, +725/-7, 895 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4] Enable DSpark adaptive verification"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v4_dspark_rocm.py`, `vllm/models/deepseek_v4/amd/dspark.py`, `vllm/models/deepseek_v4/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4] Enable DSpark adaptive verification"; the main implementation surface is `tests/models/test_deepseek_v4_dspark_rocm.py`, `vllm/models/deepseek_v4/amd/dspark.py`, `vllm/models/deepseek_v4/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_dspark_rocm.py` added +130/-0 (130 lines); hunks: -0,0 +1,130; symbols: _make_uninitialized_model, _prepare_loader_model, _disable_distributed_loader_paths, test_deepseek_v4_rocm_dspark_maps_enabled_confidence_head, touching `_make_uninitialized_model, _prepare_loader_model, _disable_distributed_loader_paths`; `vllm/models/deepseek_v4/amd/dspark.py` modified +28/-5 (33 lines); hunks: -44,6 +44,7; -102,7 +103,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, markov_embed, markov_bias, compute_confidence, touching `__init__, markov_embed, markov_bias`; `vllm/models/deepseek_v4/amd/rocm.py` modified +31/-0 (31 lines); hunks: -8,6 +8,7; -26,6 +27,7; symbols: DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV4ROCMAiterMLASparseMetadataBuilder, get_cudagraph_support, __init__, touching `DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV4ROCMAiterMLASparseMetadataBuilder, get_cudagraph_support`; `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: _make_indexer_config, _mock_rocm_platform, _make_indexer_builder, test_deepseek_v4_rocm_adaptive_builders_support_varlen_full_graphs, touching `_make_indexer_config, _mock_rocm_platform, _make_indexer_builder`.
- Code diff details:
  - `tests/models/test_deepseek_v4_dspark_rocm.py` added +130/-0 (130 lines); hunks: -0,0 +1,130; symbols: _make_uninitialized_model, _prepare_loader_model, _disable_distributed_loader_paths, test_deepseek_v4_rocm_dspark_maps_enabled_confidence_head
  - `vllm/models/deepseek_v4/amd/dspark.py` modified +28/-5 (33 lines); hunks: -44,6 +44,7; -102,7 +103,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str =...; symbols: __init__, markov_embed, markov_bias, compute_confidence
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +31/-0 (31 lines); hunks: -8,6 +8,7; -26,6 +27,7; symbols: DeepseekV4ROCMAiterSparseSWAMetadata, DeepseekV4ROCMAiterMLASparseMetadataBuilder, get_cudagraph_support, __init__
  - `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` added +249/-0 (249 lines); hunks: -0,0 +1,249; symbols: _make_indexer_config, _mock_rocm_platform, _make_indexer_builder, test_deepseek_v4_rocm_adaptive_builders_support_varlen_full_graphs
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_dspark_rocm.py
@@ -0,0 +1,130 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from types import SimpleNamespace
+import pytest
+import torch
+from vllm.models.deepseek_v4.amd import dspark as dspark_module
diff -- vllm/models/deepseek_v4/amd/dspark.py
@@ -44,6 +44,7 @@
+    DSparkConfidenceHead,
@@ -102,7 +103,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
-        # Heads: final norm + hc_head, and the Markov head
+        # Heads: final norm + hc_head, and the Markov + confidence heads
@@ -125,6 +126,12 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
+        self.confidence_head: DSparkConfidenceHead | None = None
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -8,6 +8,7 @@
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_dspark_rocm.py` added +130/-0; `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py` added +249/-0
  - runtime: `vllm/models/deepseek_v4/amd/dspark.py` modified +28/-5; `vllm/models/deepseek_v4/amd/rocm.py` modified +31/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/models/test_deepseek_v4_dspark_rocm.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57906 - [Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm

- Link: https://github.com/vllm-project/vllm/pull/57906
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/attention.py`; associated commits `04c1f4a40796`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-0, 16 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/attention.py`; technical summary: Covers "[Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` modified +9/-0 (9 lines); hunks: -531,6 +531,15 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` modified +9/-0 (9 lines); hunks: -531,6 +531,15 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -531,6 +531,15 @@ def __init__(
+        if swa_bounded_replay and current_platform.is_rocm():
+            logger.warning_once(
+                "SWA bounded replay is off on ROCm (the sparse SWA metadata "
+                "builders forward replay_start, but the window clamp it relies "
+                "on lives in the FlashInfer and FlashMLA prefill kernels, so "
+                "the padded slots fault); the sliding-window cache takes part "
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` modified +9/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/attention.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57874 - [Bugfix][DSV4.1] Restrict mHC overlap to full CUDA graphs

- Link: https://github.com/vllm-project/vllm/pull/57874
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`; associated commits `67513c8b67e2`
- Diff scope read: GitHub Pull Request files API returned 4 files, +45/-11, 108 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSV4.1] Restrict mHC overlap to full CUDA graphs"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Bugfix][DSV4.1] Restrict mHC overlap to full CUDA graphs"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +16/-0 (16 lines); hunks: -28,6 +28,22 @@ def is_mega_mhc_supported(hidden_size: int, hc_mult: int) ->...; symbols: is_mega_mhc_supported, can_use_mega_mhc, mhc_shifted_post_pre_deep_gemm, touching `is_mega_mhc_supported, can_use_mega_mhc, mhc_shifted_post_pre_deep_gemm`; `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +6/-8 (14 lines); hunks: -16,7 +16,10; -223,13 +226,8 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre, touching `mhc_shifted_post_pre`; `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1 (3 lines); hunks: -385,8 +385,9 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +16/-0 (16 lines); hunks: -28,6 +28,22 @@ def is_mega_mhc_supported(hidden_size: int, hc_mult: int) ->...; symbols: is_mega_mhc_supported, can_use_mega_mhc, mhc_shifted_post_pre_deep_gemm
  - `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +6/-8 (14 lines); hunks: -16,7 +16,10; -223,13 +226,8 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1 (3 lines); hunks: -385,8 +385,9 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py
@@ -28,6 +28,22 @@ def is_mega_mhc_supported(hidden_size: int, hc_mult: int) -> bool:
+def can_use_mega_mhc(
+    x: torch.Tensor,
+    residual: torch.Tensor,
+    pre_mix: torch.Tensor | None,
+    norm_weight: torch.Tensor | None,
+    capture_aux: bool,
diff -- vllm/models/deepseek_v41/nvidia/ops/mhc.py
@@ -16,7 +16,10 @@
-from .mega_mhc import is_mega_mhc_supported, mhc_shifted_post_pre_deep_gemm
+from .mega_mhc import (
+    can_use_mega_mhc,
+    mhc_shifted_post_pre_deep_gemm,
+)
@@ -223,13 +226,8 @@ def mhc_shifted_post_pre(
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -385,8 +385,9 @@ def forward(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +16/-0; `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +6/-8; `vllm/models/deepseek_v41/nvidia/model.py` modified +2/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57643 - [Perf][DSV4.1] Fuse TP all-reduce with mHC input preparation

- Link: https://github.com/vllm-project/vllm/pull/57643
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`; associated commits `9a70c233cd5d`
- Diff scope read: GitHub Pull Request files API returned 9 files, +549/-105, 890 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSV4.1] Fuse TP all-reduce with mHC input preparation"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`; technical summary: Covers "[Perf][DSV4.1] Fuse TP all-reduce with mHC input preparation"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +156/-4 (160 lines); hunks: -1,15 +1,26; -29,6 +40,20 @@ def supports_mhc_overlap(vllm_config: VllmConfig) -> bool:; symbols: supports_mhc_overlap, supports_mhc_all_reduce, mhc_pre_delayed_overlap, touching `supports_mhc_overlap, supports_mhc_all_reduce, mhc_pre_delayed_overlap`; `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +0/-98 (98 lines); hunks: -5,10 +5,6; -88,97 +84,3 @@ def mhc_shifted_post_pre_deep_gemm(; symbols: mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre, touching `mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre`; `vllm/models/deepseek_v41/nvidia/model.py` modified +19/-2 (21 lines); hunks: -17,6 +17,7; -88,10 +89,11; symbols: __init__, forward, touching `__init__, forward`; `vllm/models/deepseek_v4/nvidia/model.py` modified +3/-0 (3 lines); hunks: -793,6 +793,7 @@ def __init__(; -804,6 +805,7 @@ def __init__(; symbols: __init__, _init_fused_moe_experts, touching `__init__, _init_fused_moe_experts`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +156/-4 (160 lines); hunks: -1,15 +1,26; -29,6 +40,20 @@ def supports_mhc_overlap(vllm_config: VllmConfig) -> bool:; symbols: supports_mhc_overlap, supports_mhc_all_reduce, mhc_pre_delayed_overlap
  - `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +0/-98 (98 lines); hunks: -5,10 +5,6; -88,97 +84,3 @@ def mhc_shifted_post_pre_deep_gemm(; symbols: mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +19/-2 (21 lines); hunks: -17,6 +17,7; -88,10 +89,11; symbols: __init__, forward
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +3/-0 (3 lines); hunks: -793,6 +793,7 @@ def __init__(; -804,6 +805,7 @@ def __init__(; symbols: __init__, _init_fused_moe_experts
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/mhc.py
@@ -1,15 +1,26 @@
-"""Split shifted mHC pre so coefficient generation can overlap the sublayer."""
+"""Dispatch DSV4.1 mHC operations and overlap coefficient generation."""
+from typing import TYPE_CHECKING, cast
+from vllm.distributed import get_tp_group
+from vllm.model_executor.kernels.mhc.tilelang import (
+    mhc_fused_post_pre_delayed_tilelang,
diff -- vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py
@@ -5,10 +5,6 @@
-from vllm.model_executor.kernels.mhc.tilelang import (
-    mhc_fused_post_pre_delayed_tilelang,
-    mhc_post_tilelang,
-)
@@ -88,97 +84,3 @@ def mhc_shifted_post_pre_deep_gemm(
-def mhc_shifted_post_pre(
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -17,6 +17,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` modified +156/-4; `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +0/-98; `vllm/models/deepseek_v41/nvidia/model.py` modified +19/-2; `vllm/models/deepseek_v4/nvidia/model.py` modified +3/-0
- Risk and verification: The diff ships test coverage in `tests/distributed/test_custom_all_reduce.py`, `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57491 - [ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm

- Link: https://github.com/vllm-project/vllm/pull/57491
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/model.py`; associated commits `6dfd87f59658`
- Diff scope read: GitHub Pull Request files API returned 5 files, +20/-10, 96 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v41/amd/model.py`; technical summary: Covers "[ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm"; the main implementation surface is `vllm/models/deepseek_v41/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/model.py` modified +5/-1 (6 lines); hunks: -61,9 +61,13.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/model.py` modified +5/-1 (6 lines); hunks: -61,9 +61,13
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -61,9 +61,13 @@
-from ..common.engram import Engram, EngramLayout, NgramHashState
+from ..common.engram import EngramLayout, NgramHashState
+# Engram host offload and its prefetch stream are neither ROCm- nor
+# NVIDIA-specific, so they are imported rather than duplicated.
+from ..nvidia.engram import Engram
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/model.py` modified +5/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/test_engram.py`, `tests/test_config.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57603 - [Perf][DSV4.1] Overlap mHC coefficients for small TP batches

- Link: https://github.com/vllm-project/vllm/pull/57603
- Status/date: merged / 2026-09-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`; associated commits `9b49f9234431`
- Diff scope read: GitHub Pull Request files API returned 6 files, +357/-46, 645 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSV4.1] Overlap mHC coefficients for small TP batches"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`; technical summary: Covers "[Perf][DSV4.1] Overlap mHC coefficients for small TP batches"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` added +117/-0 (117 lines); hunks: -0,0 +1,117; symbols: supports_mhc_overlap, mhc_pre_delayed_overlap, touching `supports_mhc_overlap, mhc_pre_delayed_overlap`; `vllm/models/deepseek_v41/nvidia/model.py` modified +60/-16 (76 lines); hunks: -2,6 +2,7; -17,7 +18,11; symbols: __init__, forward, touching `__init__, forward`; `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +29/-1 (30 lines); hunks: -7,6 +7,7; -106,10 +107,37 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre, touching `mhc_shifted_post_pre`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/mhc.py` added +117/-0 (117 lines); hunks: -0,0 +1,117; symbols: supports_mhc_overlap, mhc_pre_delayed_overlap
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +60/-16 (76 lines); hunks: -2,6 +2,7; -17,7 +18,11; symbols: __init__, forward
  - `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +29/-1 (30 lines); hunks: -7,6 +7,7; -106,10 +107,37 @@ def mhc_shifted_post_pre(; symbols: mhc_shifted_post_pre
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/mhc.py
@@ -0,0 +1,117 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Split shifted mHC pre so coefficient generation can overlap the sublayer."""
+from functools import partial
+import torch
+from vllm.config import VllmConfig
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -2,6 +2,7 @@
+from functools import partial
@@ -17,7 +18,11 @@
-from vllm.forward_context import get_forward_context, is_forward_context_available
+from vllm.forward_context import (
+    get_forward_context,
+    in_piecewise_cudagraph,
diff -- vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py
@@ -7,6 +7,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/mhc.py` added +117/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +60/-16; `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` modified +29/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56625 - [DSV4.1] Add encoder cuda graph support for deepseek-v4.1-flash

- Link: https://github.com/vllm-project/vllm/pull/56625
- Status/date: merged / 2026-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`; associated commits `27757dde020e`
- Diff scope read: GitHub Pull Request files API returned 6 files, +599/-63, 809 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSV4.1] Add encoder cuda graph support for deepseek-v4.1-flash"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/amd/vl_model.py`; technical summary: Covers "[DSV4.1] Add encoder cuda graph support for deepseek-v4.1-flash"; the main implementation surface is `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/amd/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/vl_cudagraph.py` added +390/-0 (390 lines); hunks: -0,0 +1,390; symbols: DeepseekV4VLEncoderCudaGraphMixin, _encode_image, _build_image_span, _get_grid_list, touching `DeepseekV4VLEncoderCudaGraphMixin, _encode_image, _build_image_span`; `vllm/models/deepseek_v4/common/vision.py` modified +156/-7 (163 lines); hunks: -40,8 +40,7; -52,6 +51,13 @@ def get_vision_cos_sin(; symbols: get_vision_cos_sin, _compute_vision_cos_sin, apply_rotary, touching `get_vision_cos_sin, _compute_vision_cos_sin, apply_rotary`; `vllm/models/deepseek_v41/amd/vl_model.py` modified +12/-28 (40 lines); hunks: -26,6 +26,7; -44,15 +45,12; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, _parse_and_validate_image_input, _encode_image, touching `_make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, _parse_and_validate_image_input`; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +12/-28 (40 lines); hunks: -26,6 +26,7; -44,15 +45,12; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, _parse_and_validate_image_input, _encode_image, touching `_make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, _parse_and_validate_image_input`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/vl_cudagraph.py` added +390/-0 (390 lines); hunks: -0,0 +1,390; symbols: DeepseekV4VLEncoderCudaGraphMixin, _encode_image, _build_image_span, _get_grid_list
  - `vllm/models/deepseek_v4/common/vision.py` modified +156/-7 (163 lines); hunks: -40,8 +40,7; -52,6 +51,13 @@ def get_vision_cos_sin(; symbols: get_vision_cos_sin, _compute_vision_cos_sin, apply_rotary
  - `vllm/models/deepseek_v41/amd/vl_model.py` modified +12/-28 (40 lines); hunks: -26,6 +26,7; -44,15 +45,12; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, _parse_and_validate_image_input, _encode_image
  - `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +12/-28 (40 lines); hunks: -26,6 +26,7; -44,15 +45,12; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, _parse_and_validate_image_input, _encode_image
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/vl_cudagraph.py
@@ -0,0 +1,390 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Encoder CUDA graph support for the DeepSeek-V4.1 vision tower.
+Mixin implementing the ``SupportsEncoderCudaGraph`` protocol
+(``vllm/model_executor/models/interfaces.py``) on top of the shared
+``DeepseekV4ViT``/``DeepseekV4Aligner``. The captured graph packs a whole
diff -- vllm/models/deepseek_v4/common/vision.py
@@ -40,8 +40,7 @@
-@lru_cache(8)
-def get_vision_cos_sin(
+def _compute_vision_cos_sin(
@@ -52,6 +51,13 @@ def get_vision_cos_sin(
+@lru_cache(8)
+def get_vision_cos_sin(
diff -- vllm/models/deepseek_v41/amd/vl_model.py
@@ -26,6 +26,7 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/vl_cudagraph.py` added +390/-0; `vllm/models/deepseek_v4/common/vision.py` modified +156/-7; `vllm/models/deepseek_v41/amd/vl_model.py` modified +12/-28; `vllm/models/deepseek_v41/nvidia/vl_model.py` modified +12/-28
- Risk and verification: The diff ships test coverage in `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/models/multimodal/processing/test_tensor_schema.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #54894 - [ROCm][DSV4][Perf] Use FP8 WO_A output projection

- Link: https://github.com/vllm-project/vllm/pull/54894
- Status/date: merged / 2026-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_rocm_wo_a.py`, `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `0e110f696db4`
- Diff scope read: GitHub Pull Request files API returned 2 files, +217/-11, 264 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSV4][Perf] Use FP8 WO_A output projection"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `tests/models/test_deepseek_v4_rocm_wo_a.py`; technical summary: Covers "[ROCm][DSV4][Perf] Use FP8 WO_A output projection"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `tests/models/test_deepseek_v4_rocm_wo_a.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +173/-11 (184 lines); hunks: -7,6 +7,7; -42,6 +43,49; symbols: _wo_a_block_scale_to_e8m0, _trust_dsv4_extra_cache_nan_free, __init__, _prep, touching `_wo_a_block_scale_to_e8m0, _trust_dsv4_extra_cache_nan_free, __init__`; `tests/models/test_deepseek_v4_rocm_wo_a.py` added +44/-0 (44 lines); hunks: -0,0 +1,44; symbols: test_wo_a_block_scale_to_e8m0_from_float, test_wo_a_block_scale_to_e8m0_preserves_encoded_scales, test_wo_a_block_scale_to_e8m0_rejects_invalid_scales, touching `test_wo_a_block_scale_to_e8m0_from_float, test_wo_a_block_scale_to_e8m0_preserves_encoded_scales, test_wo_a_block_scale_to_e8m0_rejects_invalid_scales`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +173/-11 (184 lines); hunks: -7,6 +7,7; -42,6 +43,49; symbols: _wo_a_block_scale_to_e8m0, _trust_dsv4_extra_cache_nan_free, __init__, _prep
  - `tests/models/test_deepseek_v4_rocm_wo_a.py` added +44/-0 (44 lines); hunks: -0,0 +1,44; symbols: test_wo_a_block_scale_to_e8m0_from_float, test_wo_a_block_scale_to_e8m0_preserves_encoded_scales, test_wo_a_block_scale_to_e8m0_rejects_invalid_scales
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -7,6 +7,7 @@
+from vllm import envs
@@ -42,6 +43,49 @@
+def _wo_a_block_scale_to_e8m0(scale: torch.Tensor) -> torch.Tensor | None:
+    """Normalize checkpoint WO_A scales to raw OCP MX E8M0 bytes.
+    E8M0 is an unsigned exponent-only scale format with bias 127. A finite
+    encoded byte ``b`` in ``[0, 254]`` represents ``2 ** (b - 127)``;
diff -- tests/models/test_deepseek_v4_rocm_wo_a.py
@@ -0,0 +1,44 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import pytest
+import torch
+from vllm.models.deepseek_v4.amd.rocm import _wo_a_block_scale_to_e8m0
+def test_wo_a_block_scale_to_e8m0_from_float():
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +173/-11
  - tests: `tests/models/test_deepseek_v4_rocm_wo_a.py` added +44/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_rocm_wo_a.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57434 - [ROCm][DSv4.1][Perf] Reuse the decode topk ragged metadata across layers

- Link: https://github.com/vllm-project/vllm/pull/57434
- Status/date: merged / 2026-09-20
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/rocm.py`; associated commits `1596fa5f8825`
- Diff scope read: GitHub Pull Request files API returned 1 files, +66/-13, 118 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSv4.1][Perf] Reuse the decode topk ragged metadata across layers"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/rocm.py`; technical summary: Covers "[ROCm][DSv4.1][Perf] Reuse the decode topk ragged metadata across layers"; the main implementation surface is `vllm/models/deepseek_v41/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/rocm.py` modified +66/-13 (79 lines); hunks: -13,7 +13,10; -391,6 +394,10 @@ def _copy_ragged_to_graph_buffers(; symbols: _copy_ragged_to_graph_buffers, DeepseekV4ROCMAiterSparseSWAMetadata, __init__, get_padded_num_q_heads, touching `_copy_ragged_to_graph_buffers, DeepseekV4ROCMAiterSparseSWAMetadata, __init__`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/rocm.py` modified +66/-13 (79 lines); hunks: -13,7 +13,10; -391,6 +394,10 @@ def _copy_ragged_to_graph_buffers(; symbols: _copy_ragged_to_graph_buffers, DeepseekV4ROCMAiterSparseSWAMetadata, __init__, get_padded_num_q_heads
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -13,7 +13,10 @@
-from vllm.models.deepseek_v41.attention import DeepseekV4Attention
+from vllm.models.deepseek_v41.attention import (
+    DeepseekV4Attention,
+    _replace_layer_index,
+)
@@ -391,6 +394,10 @@ def _copy_ragged_to_graph_buffers(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/rocm.py` modified +66/-13
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v41/amd/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #56227 - [Feat][Model] Support encoder-side SWA-bounded replay for DeepSeek-V4.1-Flash

- Link: https://github.com/vllm-project/vllm/pull/56227
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v41_replay_start.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/sparse_mla.py` and 11 files; associated commits `1dc2d854c120`
- Diff scope read: GitHub Pull Request files API returned 30 files, +1067/-38, 1949 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Feat][Model] Support encoder-side SWA-bounded replay for DeepSeek-V4.1-Flash"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_replay_start.py`, `vllm/models/deepseek_v41/attention.py`; technical summary: Covers "[Feat][Model] Support encoder-side SWA-bounded replay for DeepSeek-V4.1-Flash"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model_state.py`, `tests/models/test_deepseek_v41_replay_start.py`, `vllm/models/deepseek_v41/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +143/-2 (145 lines); hunks: -2,15 +2,23; -41,14 +49,69 @@ def _gather_lookback_kernel(; symbols: _gather_lookback_kernel, _pad_replayed_slots_kernel, ReplayAttnMetadata, __init__, touching `_gather_lookback_kernel, _pad_replayed_slots_kernel, ReplayAttnMetadata`; `tests/models/test_deepseek_v41_replay_start.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: state, prepare_attn, _batch, _prepare, touching `state, prepare_attn, _batch`; `vllm/models/deepseek_v41/attention.py` modified +20/-0 (20 lines); hunks: -512,6 +512,25 @@ def __init__(; -522,6 +541,7 @@ def __init__(; symbols: __init__, touching `__init__`; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +13/-0 (13 lines); hunks: -978,6 +978,10 @@ def kernel(; -1124,6 +1128,8 @@ def build_flashinfer_mixed_sparse_indices(; symbols: kernel, build_flashinfer_mixed_sparse_indices, _build_flashinfer_mixed_sparse_indices_kernel, touching `kernel, build_flashinfer_mixed_sparse_indices, _build_flashinfer_mixed_sparse_indices_kernel`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model_state.py` modified +143/-2 (145 lines); hunks: -2,15 +2,23; -41,14 +49,69 @@ def _gather_lookback_kernel(; symbols: _gather_lookback_kernel, _pad_replayed_slots_kernel, ReplayAttnMetadata, __init__
  - `tests/models/test_deepseek_v41_replay_start.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: state, prepare_attn, _batch, _prepare
  - `vllm/models/deepseek_v41/attention.py` modified +20/-0 (20 lines); hunks: -512,6 +512,25 @@ def __init__(; -522,6 +541,7 @@ def __init__(; symbols: __init__
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +13/-0 (13 lines); hunks: -978,6 +978,10 @@ def kernel(; -1124,6 +1128,8 @@ def build_flashinfer_mixed_sparse_indices(; symbols: kernel, build_flashinfer_mixed_sparse_indices, _build_flashinfer_mixed_sparse_indices_kernel
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +6/-1 (7 lines); hunks: -200,8 +200,11 @@ def build(; -375,6 +378,7 @@ def _build_sparse_index_metadata(; symbols: build, _build_sparse_index_metadata
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model_state.py
@@ -2,15 +2,23 @@
+import numpy as np
-from vllm.config import VllmConfig
+from vllm.config import CUDAGraphMode, VllmConfig
+from vllm.v1.attention.backends.mla.sparse_swa import DeepseekSparseSWAMetadataBuilder
+from vllm.v1.attention.backends.utils import PAD_SLOT_ID
+from vllm.v1.core.sched.output import NewRequestData
diff -- tests/models/test_deepseek_v41_replay_start.py
@@ -0,0 +1,112 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""SWA bounded replay in DeepseekV41ModelState: the batch's replay starts reach
+the sliding-window builders, and the replayed tokens' slots are padded in the
+prefix-cacheable groups only."""
+from dataclasses import replace
diff -- vllm/models/deepseek_v41/attention.py
@@ -512,6 +512,25 @@ def __init__(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model_state.py` modified +143/-2; `vllm/models/deepseek_v41/attention.py` modified +20/-0; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +13/-0; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +6/-1; `vllm/models/deepseek_v4/amd/rocm.py` modified +2/-0; `vllm/models/deepseek_v41/amd/rocm.py` modified +2/-0
  - tests: `tests/models/test_deepseek_v41_replay_start.py` added +112/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v41_replay_start.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57604 - [Perf][DSV4.1] Optimize MegaMoE staging and NVFP4 cache gathers

- Link: https://github.com/vllm-project/vllm/pull/57604
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; associated commits `50d812b66a69`
- Diff scope read: GitHub Pull Request files API returned 5 files, +130/-62, 369 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSV4.1] Optimize MegaMoE staging and NVFP4 cache gathers"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; technical summary: Covers "[Perf][DSV4.1] Optimize MegaMoE staging and NVFP4 cache gathers"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +13/-9 (22 lines); hunks: -686,12 +686,14 @@ def forward(self, hidden_states):; -846,6 +848,7 @@ def test_deepseek_v4_mega_moe_stages_shared_scale_tma_layout...; symbols: forward, test_deepseek_v4_mega_moe_fused_input_staging_is_bitwise_exact, test_deepseek_v4_mega_moe_stages_shared_scale_tma_layout, test_deepseek_v4_pwal_hook_finalizes_mega_moe_and_mhc_broadcast, touching `forward, test_deepseek_v4_mega_moe_fused_input_staging_is_bitwise_exact, test_deepseek_v4_mega_moe_stages_shared_scale_tma_layout`; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +5/-1 (6 lines); hunks: -584,7 +584,11 @@ def dequantize_and_gather_k_cache_triton(; symbols: dequantize_and_gather_k_cache_triton, touching `dequantize_and_gather_k_cache_triton`; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +1/-1 (2 lines); hunks: -422,7 +422,7 @@ def _forward_prefill_mega(; symbols: _forward_prefill_mega, touching `_forward_prefill_mega`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +13/-9 (22 lines); hunks: -686,12 +686,14 @@ def forward(self, hidden_states):; -846,6 +848,7 @@ def test_deepseek_v4_mega_moe_stages_shared_scale_tma_layout...; symbols: forward, test_deepseek_v4_mega_moe_fused_input_staging_is_bitwise_exact, test_deepseek_v4_mega_moe_stages_shared_scale_tma_layout, test_deepseek_v4_pwal_hook_finalizes_mega_moe_and_mhc_broadcast
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +5/-1 (6 lines); hunks: -584,7 +584,11 @@ def dequantize_and_gather_k_cache_triton(; symbols: dequantize_and_gather_k_cache_triton
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +1/-1 (2 lines); hunks: -422,7 +422,7 @@ def _forward_prefill_mega(; symbols: _forward_prefill_mega
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -686,12 +686,14 @@ def forward(self, hidden_states):
-def test_deepseek_v4_mega_moe_fused_input_staging_is_bitwise_exact():
+@pytest.mark.parametrize("num_tokens", [7, 63, 64, 65, 127, 128, 135, 434, 16384])
+@pytest.mark.parametrize("hidden_size", [256, 5120])
+def test_deepseek_v4_mega_moe_fused_input_staging_is_bitwise_exact(
+    num_tokens, hidden_size
+):
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -584,7 +584,11 @@ def dequantize_and_gather_k_cache_triton(
-        _dequantize_and_gather_k_nvfp4_kernel[(num_reqs, NUM_WORKERS)](
+        # Keep short gathers unchanged; cap total workers for multi-request chunks.
+        num_workers = min(
+            max(128, 2048 // max(1, num_reqs)), max(128, out.shape[1] - offset)
+        )
+        _dequantize_and_gather_k_nvfp4_kernel[(num_reqs, num_workers)](
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -422,7 +422,7 @@ def _forward_prefill_mega(
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +13/-9
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +5/-1; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`, `tests/models/test_deepseek_v4_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57465 - [DeepSeek V4] Fix fused MoE expert distribution

- Link: https://github.com/vllm-project/vllm/pull/57465
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `017dced6a6fd`
- Diff scope read: GitHub Pull Request files API returned 1 files, +5/-7, 26 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DeepSeek V4] Fix fused MoE expert distribution"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/nvidia/model.py`; technical summary: Covers "[DeepSeek V4] Fix fused MoE expert distribution"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/model.py` modified +5/-7 (12 lines); hunks: -993,20 +993,18 @@ def _init_fused_moe_experts(; symbols: _init_fused_moe_experts, touching `_init_fused_moe_experts`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +5/-7 (12 lines); hunks: -993,20 +993,18 @@ def _init_fused_moe_experts(; symbols: _init_fused_moe_experts
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -993,20 +993,18 @@ def _init_fused_moe_experts(
-        self.tp_rank = get_tensor_model_parallel_rank()
+        ep_group = get_ep_group()
+        ep_size = ep_group.world_size
+        ep_rank = ep_group.rank_in_group
-        assert self.n_physical_experts % self.tp_size == 0, (
-            f"n_physical_experts={self.n_physical_experts} must be divisible by "
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +5/-7
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/nvidia/model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #56882 - [Bugfix][Multimodal] Preserve DeepSeek V4 image block spacing

- Link: https://github.com/vllm-project/vllm/pull/56882
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt`, `tests/tokenizers_/test_deepseek_v4.py`, `vllm/renderers/deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py`; associated commits `cc09352e5c50`
- Diff scope read: GitHub Pull Request files API returned 5 files, +60/-12, 132 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Multimodal] Preserve DeepSeek V4 image block spacing"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json`, `tests/tokenizers_/test_deepseek_v4.py`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt`; technical summary: Covers "[Bugfix][Multimodal] Preserve DeepSeek V4 image block spacing"; the main implementation surface is `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json`, `tests/tokenizers_/test_deepseek_v4.py`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json` added +39/-0 (39 lines); hunks: -0,0 +1,39; `tests/tokenizers_/test_deepseek_v4.py` modified +7/-7 (14 lines); hunks: -54,13 +54,9 @@ def _load_reference_case(case_id: int):; -397,6 +393,7 @@ def test_deepseek_v4_maps_xhigh_to_high_reasoning_effort():; symbols: _load_reference_case, _render_reference_case, test_deepseek_v4_maps_xhigh_to_high_reasoning_effort, test_deepseek_v4_matches_reference_golden_fixtures, touching `_load_reference_case, _render_reference_case, test_deepseek_v4_maps_xhigh_to_high_reasoning_effort`; `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt` added +9/-0 (9 lines); hunks: -0,0 +1,9; `vllm/tokenizers/deepseek_v4_encoding.py` modified +3/-3 (6 lines); hunks: -224,7 +224,7 @@ def flatten_content_blocks(content: Any) -> Any:; -267,7 +267,7 @@ def render_message(; symbols: flatten_content_blocks, render_message, touching `flatten_content_blocks, render_message`.
- Code diff details:
  - `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json` added +39/-0 (39 lines); hunks: -0,0 +1,39
  - `tests/tokenizers_/test_deepseek_v4.py` modified +7/-7 (14 lines); hunks: -54,13 +54,9 @@ def _load_reference_case(case_id: int):; -397,6 +393,7 @@ def test_deepseek_v4_maps_xhigh_to_high_reasoning_effort():; symbols: _load_reference_case, _render_reference_case, test_deepseek_v4_maps_xhigh_to_high_reasoning_effort, test_deepseek_v4_matches_reference_golden_fixtures
  - `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt` added +9/-0 (9 lines); hunks: -0,0 +1,9
  - `vllm/tokenizers/deepseek_v4_encoding.py` modified +3/-3 (6 lines); hunks: -224,7 +224,7 @@ def flatten_content_blocks(content: Any) -> Any:; -267,7 +267,7 @@ def render_message(; symbols: flatten_content_blocks, render_message
  - `vllm/renderers/deepseek_v4.py` modified +2/-2 (4 lines); hunks: -40,7 +40,7 @@ def render_messages(; -67,7 +67,7 @@ async def render_messages_async(; symbols: render_messages, render_messages_async
- Key code excerpts:

```diff
diff -- tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json
@@ -0,0 +1,39 @@
+{
+    "thinking_mode": "thinking",
+    "reasoning_effort": "max",
+    "messages": [
+        {
+            "role": "system",
diff -- tests/tokenizers_/test_deepseek_v4.py
@@ -54,13 +54,9 @@ def _load_reference_case(case_id: int):
-    conversation, _, _ = parse_chat_messages(
-        messages,
-        _model_config(),
-        content_format="string",
-    )
+    # Preserve content blocks for encoding without fetching fixture media.
diff -- tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt
@@ -0,0 +1,9 @@
```

- Reviewed files:
  - tests: `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json` added +39/-0; `tests/tokenizers_/test_deepseek_v4.py` modified +7/-7; `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt` added +9/-0
  - runtime: `vllm/tokenizers/deepseek_v4_encoding.py` modified +3/-3; `vllm/renderers/deepseek_v4.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt`, `tests/tokenizers_/test_deepseek_v4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56271 - [Frontend] Fix the parsing of missing `string=` in DeepSeek V4

- Link: https://github.com/vllm-project/vllm/pull/56271
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py`, `vllm/parser/deepseek_v4.py`, `vllm/parser/deepseek_v41.py`; associated commits `39e33db7f3b1`
- Diff scope read: GitHub Pull Request files API returned 8 files, +174/-29, 306 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Frontend] Fix the parsing of missing `string=` in DeepSeek V4"; model line: DeepSeek V4; category: bug fix; main diff: `tests/parser/engine/test_deepseek_v4.py`, `vllm/parser/deepseek_v4.py`, `vllm/parser/deepseek_v41.py`; technical summary: Covers "[Frontend] Fix the parsing of missing `string=` in DeepSeek V4"; the main implementation surface is `tests/parser/engine/test_deepseek_v4.py`, `vllm/parser/deepseek_v4.py`, `vllm/parser/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/parser/engine/test_deepseek_v4.py` modified +70/-0 (70 lines); hunks: -119,6 +119,35 @@ def test_empty_args(self):; -232,6 +261,47 @@ def test_streaming_split_next_parameter_tag_is_buffered(; symbols: test_empty_args, _bare, test_missing_string_attribute_keeps_literal, test_missing_string_attribute_parses_json, touching `test_empty_args, _bare, test_missing_string_attribute_keeps_literal`; `vllm/parser/deepseek_v4.py` modified +20/-12 (32 lines); hunks: -56,18 +56,24; -80,6 +86,8 @@ def _dsml_arg_converter(; symbols: _param_patterns, _dsml_arg_converter, touching `_param_patterns, _dsml_arg_converter`; `vllm/parser/deepseek_v41.py` modified +2/-13 (15 lines); hunks: -5,11 +5,10; -21,17 +20,7; `tests/parser/engine/test_deepseek_v41.py` modified +2/-0 (2 lines); hunks: -137,10 +137,12 @@ def test_python_argument_conversion_and_partial_values():; symbols: test_python_argument_conversion_and_partial_values, touching `test_python_argument_conversion_and_partial_values`.
- Code diff details:
  - `tests/parser/engine/test_deepseek_v4.py` modified +70/-0 (70 lines); hunks: -119,6 +119,35 @@ def test_empty_args(self):; -232,6 +261,47 @@ def test_streaming_split_next_parameter_tag_is_buffered(; symbols: test_empty_args, _bare, test_missing_string_attribute_keeps_literal, test_missing_string_attribute_parses_json
  - `vllm/parser/deepseek_v4.py` modified +20/-12 (32 lines); hunks: -56,18 +56,24; -80,6 +86,8 @@ def _dsml_arg_converter(; symbols: _param_patterns, _dsml_arg_converter
  - `vllm/parser/deepseek_v41.py` modified +2/-13 (15 lines); hunks: -5,11 +5,10; -21,17 +20,7
  - `tests/parser/engine/test_deepseek_v41.py` modified +2/-0 (2 lines); hunks: -137,10 +137,12 @@ def test_python_argument_conversion_and_partial_values():; symbols: test_python_argument_conversion_and_partial_values
- Key code excerpts:

```diff
diff -- tests/parser/engine/test_deepseek_v4.py
@@ -119,6 +119,35 @@ def test_empty_args(self):
+    def _bare(self, name: str, value: str) -> str:
+        return f'<｜DSML｜parameter name="{name}">{value}{_PARAM_CLOSE}'
+    def test_missing_string_attribute_keeps_literal(self):
+        """The model sometimes omits ``string``; the parameter must survive."""
+        raw = self._bare("name", "alpha")
+        assert json.loads(_dsml_arg_converter(raw, partial=False)) == {"name": "alpha"}
diff -- vllm/parser/deepseek_v4.py
@@ -56,18 +56,24 @@
-_ESCAPED_DSML = re.escape(_DSML)
-_PARAM_RE = re.compile(
-    rf'<{_ESCAPED_DSML}parameter\s+name="([^"]+)"\s+string="(true|false)">'
-    rf"(.*?)"
-    rf"(?:</{_ESCAPED_DSML}parameter>|(?=<{_ESCAPED_DSML}parameter\s+name=))",
-    re.DOTALL,
diff -- vllm/parser/deepseek_v41.py
@@ -5,11 +5,10 @@
```

- Reviewed files:
  - tests: `tests/parser/engine/test_deepseek_v4.py` modified +70/-0; `tests/parser/engine/test_deepseek_v41.py` modified +2/-0
  - runtime: `vllm/parser/deepseek_v4.py` modified +20/-12; `vllm/parser/deepseek_v41.py` modified +2/-13
- Risk and verification: The diff ships test coverage in `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #51856 - [Bugfix] Attach request-level tools to existing system message in DeepSeek V4 Python renderer

- Link: https://github.com/vllm-project/vllm/pull/51856
- Status/date: merged / 2026-09-18
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt`, `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4.py`; associated commits `2909ad8fa472`
- Diff scope read: GitHub Pull Request files API returned 3 files, +157/-4, 183 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Attach request-level tools to existing system message in DeepSeek V4 Python renderer"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4.py`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt`; technical summary: Covers "[Bugfix] Attach request-level tools to existing system message in DeepSeek V4 Python renderer"; the main implementation surface is `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4.py`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v4.py` modified +143/-0 (143 lines); hunks: -485,3 +485,146 @@ def convert_tokens_to_ids(self, token: str) -> int:; symbols: convert_tokens_to_ids, _request_tools, _encode_reference, test_deepseek_v4_attaches_request_tools_to_existing_system_message, touching `convert_tokens_to_ids, _request_tools, _encode_reference`; `vllm/tokenizers/deepseek_v4.py` modified +12/-2 (14 lines); hunks: -35,8 +35,18 @@ def apply_chat_template(; symbols: apply_chat_template, touching `apply_chat_template`; `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt` modified +2/-2 (4 lines); hunks: -1,4 +1,4; -26,7 +26,7 @@ Otherwise, output directly after with tool calls or final resp....
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v4.py` modified +143/-0 (143 lines); hunks: -485,3 +485,146 @@ def convert_tokens_to_ids(self, token: str) -> int:; symbols: convert_tokens_to_ids, _request_tools, _encode_reference, test_deepseek_v4_attaches_request_tools_to_existing_system_message
  - `vllm/tokenizers/deepseek_v4.py` modified +12/-2 (14 lines); hunks: -35,8 +35,18 @@ def apply_chat_template(; symbols: apply_chat_template
  - `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt` modified +2/-2 (4 lines); hunks: -1,4 +1,4; -26,7 +26,7 @@ Otherwise, output directly after with tool calls or final resp...
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v4.py
@@ -485,3 +485,146 @@ def convert_tokens_to_ids(self, token: str) -> int:
+def _request_tools():
+    return [
+        {
+            "type": "function",
+            "function": {
+                "name": "get_weather",
diff -- vllm/tokenizers/deepseek_v4.py
@@ -35,8 +35,18 @@ def apply_chat_template(
-                messages.insert(0, {"role": "system"})
-                messages[0]["tools"] = tools  # type: ignore[typeddict-unknown-key]
+                # Match the Rust renderer: request tools attach to the first
+                # system message; synthesize one only when none exists.
+                system_idx = next(
+                    (i for i, m in enumerate(messages) if m.get("role") == "system"),
diff -- tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt
@@ -1,4 +1,4 @@
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v4.py` modified +143/-0; `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt` modified +2/-2
  - runtime: `vllm/tokenizers/deepseek_v4.py` modified +12/-2
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt`, `tests/tokenizers_/test_deepseek_v4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57432 - [Bugfix][DSv4.1] Fix FlashInfer DSpark non-causal attention

- Link: https://github.com/vllm-project/vllm/pull/57432
- Status/date: merged / 2026-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`; associated commits `80447d276559`
- Diff scope read: GitHub Pull Request files API returned 3 files, +214/-6, 262 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4.1] Fix FlashInfer DSpark non-causal attention"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`; technical summary: Covers "[Bugfix][DSv4.1] Fix FlashInfer DSpark non-causal attention"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +62/-6 (68 lines); hunks: -26,7 +26,11; -183,6 +187,39 @@ class DeepseekSparseSWAFlashInferMetadataBuilder(DeepseekV4...; symbols: DeepseekSparseSWAFlashInferMetadataBuilder, __init__, build, DeepseekSparseSWAFlashInferBackend, touching `DeepseekSparseSWAFlashInferMetadataBuilder, __init__, build`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +62/-6 (68 lines); hunks: -26,7 +26,11; -183,6 +187,39 @@ class DeepseekSparseSWAFlashInferMetadataBuilder(DeepseekV4...; symbols: DeepseekSparseSWAFlashInferMetadataBuilder, __init__, build, DeepseekSparseSWAFlashInferBackend
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py
@@ -26,7 +26,11 @@
-from vllm.v1.attention.backend import AttentionCGSupport, MultipleOf
+from vllm.v1.attention.backend import (
+    AttentionCGSupport,
+    CommonAttentionMetadata,
+    MultipleOf,
+)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +62/-6
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56266 - [DSv4.1] Integrate Mega-Gate from DeepGEMM

- Link: https://github.com/vllm-project/vllm/pull/56266
- Status/date: merged / 2026-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/dspark.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`, `vllm/models/deepseek_v41/nvidia/dspark.py` and 6 files; associated commits `41f9104fa649`
- Diff scope read: GitHub Pull Request files API returned 9 files, +369/-35, 782 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSv4.1] Integrate Mega-Gate from DeepGEMM"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`; technical summary: Covers "[DSv4.1] Integrate Mega-Gate from DeepGEMM"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +138/-12 (150 lines); hunks: -15,13 +15,15; -33,6 +35,7; symbols: v41_moe_config, test_deepseek_v41_moe_routes_without_hash_table, touching `v41_moe_config, test_deepseek_v41_moe_routes_without_hash_table`; `vllm/models/deepseek_v4/nvidia/model.py` modified +110/-19 (129 lines); hunks: -98,6 +98,37; -803,6 +834,10 @@ def __init__(; symbols: MegaGateRoutingMetadata, prepare_mega_gate_routing_metadata, DeepseekV4MLP, __init__, touching `MegaGateRoutingMetadata, prepare_mega_gate_routing_metadata, DeepseekV4MLP`; `vllm/models/deepseek_v4/nvidia/mtp.py` modified +20/-1 (21 lines); hunks: -20,6 +20,7; -51,6 +52,7; symbols: __init__, forward, touching `__init__, forward`; `vllm/models/deepseek_v41/nvidia/model.py` modified +15/-1 (16 lines); hunks: -61,7 +61,9; -339,6 +341,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +138/-12 (150 lines); hunks: -15,13 +15,15; -33,6 +35,7; symbols: v41_moe_config, test_deepseek_v41_moe_routes_without_hash_table
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +110/-19 (129 lines); hunks: -98,6 +98,37; -803,6 +834,10 @@ def __init__(; symbols: MegaGateRoutingMetadata, prepare_mega_gate_routing_metadata, DeepseekV4MLP, __init__
  - `vllm/models/deepseek_v4/nvidia/mtp.py` modified +20/-1 (21 lines); hunks: -20,6 +20,7; -51,6 +52,7; symbols: __init__, forward
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +15/-1 (16 lines); hunks: -61,7 +61,9; -339,6 +341,7 @@ def forward(; symbols: forward
  - `vllm/models/deepseek_v4/nvidia/dspark.py` modified +14/-0 (14 lines); hunks: -17,6 +17,7; -51,12 +52,14; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -15,13 +15,15 @@
+    prepare_mega_gate_routing_metadata,
+from vllm.utils.torch_utils import set_default_torch_dtype
@@ -33,6 +35,7 @@
+            dtype=torch.bfloat16,
@@ -63,28 +66,52 @@ def v41_moe_config(dist_init):
+@pytest.mark.parametrize("use_cudagraph", [False, True])
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -98,6 +98,37 @@
+class MegaGateRoutingMetadata(typing.NamedTuple):
+    safe_hash_input_ids: torch.Tensor | None
+    image_token_mask: torch.Tensor | None
+    hash_token_mask: torch.Tensor | None
+def prepare_mega_gate_routing_metadata(
+    input_ids: torch.Tensor,
diff -- vllm/models/deepseek_v4/nvidia/mtp.py
@@ -20,6 +20,7 @@
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +138/-12
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +110/-19; `vllm/models/deepseek_v4/nvidia/mtp.py` modified +20/-1; `vllm/models/deepseek_v41/nvidia/model.py` modified +15/-1; `vllm/models/deepseek_v4/nvidia/dspark.py` modified +14/-0; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +14/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_mhc_kernels.py`, `tests/models/test_deepseek_v4_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #54674 - [Perf][DSpark] Stack DeepSeek V4 context WKV projections

- Link: https://github.com/vllm-project/vllm/pull/54674
- Status/date: merged / 2026-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/dspark.py`; associated commits `b3079e6e46a2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +119/-6, 189 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSpark] Stack DeepSeek V4 context WKV projections"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/nvidia/dspark.py`; technical summary: Covers "[Perf][DSpark] Stack DeepSeek V4 context WKV projections"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/dspark.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/dspark.py` modified +46/-6 (52 lines); hunks: -31,7 +31,10; -61,6 +64,24; symbols: _duplicate_context_wkv_weights, DSparkDeepseekV4Model, __init__, precompute_and_store_context_kv, touching `_duplicate_context_wkv_weights, DSparkDeepseekV4Model, __init__`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/dspark.py` modified +46/-6 (52 lines); hunks: -31,7 +31,10; -61,6 +64,24; symbols: _duplicate_context_wkv_weights, DSparkDeepseekV4Model, __init__, precompute_and_store_context_kv
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/dspark.py
@@ -31,7 +31,10 @@
-from vllm.model_executor.layers.linear import ReplicatedLinear
+from vllm.model_executor.layers.linear import (
+    MergedColumnParallelLinear,
+    ReplicatedLinear,
+)
@@ -61,6 +64,24 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/dspark.py` modified +46/-6
- Risk and verification: The diff ships test coverage in `tests/models/test_dspark_mla.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56853 - [ROCm][Perf] Enable HCA dual-stream overlap for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/56853
- Status/date: merged / 2026-09-17
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `fdcd42350bd2`
- Diff scope read: GitHub Pull Request files API returned 1 files, +35/-9, 102 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Enable HCA dual-stream overlap for DeepSeek-V4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`; technical summary: Covers "[ROCm][Perf] Enable HCA dual-stream overlap for DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +35/-9 (44 lines); hunks: -558,22 +558,25 @@ def __init__(self, *args, **kwargs):; -624,7 +627,7 @@ def forward(; symbols: __init__, _enable_csa_multi_stream, _enable_multi_stream_overlap, forward, touching `__init__, _enable_csa_multi_stream, _enable_multi_stream_overlap`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +35/-9 (44 lines); hunks: -558,22 +558,25 @@ def __init__(self, *args, **kwargs):; -624,7 +627,7 @@ def forward(; symbols: __init__, _enable_csa_multi_stream, _enable_multi_stream_overlap, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -558,22 +558,25 @@ def __init__(self, *args, **kwargs):
-            # Only enable multi-stream overlap for CSA layer now.
-            self.aux_stream_list = None
+            # Dense layers have no compressor work to overlap; HCA layers
+            # (compressor, no indexer) keep the streams for the dual-stream
+            # fork below.
+            if self.compressor is None:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +35/-9
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/rocm.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #57204 - [Perf][DSV4.1] Remove MegaMoE padding and shared padding workaround

- Link: https://github.com/vllm-project/vllm/pull/57204
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `30b847c1fa54`
- Diff scope read: GitHub Pull Request files API returned 2 files, +42/-157, 313 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSV4.1] Remove MegaMoE padding and shared padding workaround"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`; technical summary: Covers "[Perf][DSV4.1] Remove MegaMoE padding and shared padding workaround"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +37/-92 (129 lines); hunks: -300,8 +300,10 @@ def test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert_...; -333,50 +335,35 @@ def test_deepseek_v4_mega_moe_padding_preserves_weights(mo...; symbols: test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert_ownership, test_deepseek_v4_mega_moe_padding_preserves_weights, test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights, touching `test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert_ownership, test_deepseek_v4_mega_moe_padding_preserves_weights, test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions`; `vllm/models/deepseek_v4/nvidia/model.py` modified +5/-65 (70 lines); hunks: -204,7 +204,6 @@ def __init__(; -387,17 +386,6 @@ def _finalize_shared_expert_weights(; symbols: __init__, _finalize_shared_expert_weights, _prepare_shared_expert_scale, touching `__init__, _finalize_shared_expert_weights, _prepare_shared_expert_scale`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +37/-92 (129 lines); hunks: -300,8 +300,10 @@ def test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert_...; -333,50 +335,35 @@ def test_deepseek_v4_mega_moe_padding_preserves_weights(mo...; symbols: test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert_ownership, test_deepseek_v4_mega_moe_padding_preserves_weights, test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +5/-65 (70 lines); hunks: -204,7 +204,6 @@ def __init__(; -387,17 +386,6 @@ def _finalize_shared_expert_weights(; symbols: __init__, _finalize_shared_expert_weights, _prepare_shared_expert_scale
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -300,8 +300,10 @@ def test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert_ownership():
-def test_deepseek_v4_mega_moe_padding_preserves_weights(monkeypatch, intermediate_size):
-    """Pad gate/up separately and zero every added down-projection column."""
+def test_deepseek_v4_mega_moe_preserves_checkpoint_dimensions(
+    monkeypatch, intermediate_size
+):
+    """Keep native widths so V4.1 routed and shared experts can fuse."""
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -204,7 +204,6 @@ def __init__(
-        self.unpadded_intermediate_size = intermediate_size
@@ -387,17 +386,6 @@ def _finalize_shared_expert_weights(
-        unpadded_size = self.unpadded_intermediate_size * self.num_shared_experts
-        padding = self.intermediate_size * self.num_shared_experts - unpadded_size
-        pad_weights = (
-            padding > 0
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +37/-92
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +5/-65
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57132 - [ROCm][Bugfix] Revert #56433 + #51692 to fix accuracy breakdown for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/57132
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `bc0f47cd03d6`
- Diff scope read: GitHub Pull Request files API returned 8 files, +34/-402, 589 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Bugfix] Revert #56433 + #51692 to fix accuracy breakdown for DeepSeek-V4"; model line: DeepSeek V4; category: bug fix; main diff: `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][Bugfix] Revert #56433 + #51692 to fix accuracy breakdown for DeepSeek-V4"; the main implementation surface is `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_vl_rocm.py` modified +0/-125 (125 lines); hunks: -15,131 +15,6; symbols: _preshuffled_fp8_linear, test_rocm_wo_a_keeps_row_major_weights, test_rocm_gateup_shuffles_once_and_down_proj_keeps_preshuffled_backend, test_rocm_fused_qkv_quant_matches_preshuffled_gemm_scale_layout, touching `_preshuffled_fp8_linear, test_rocm_wo_a_keeps_row_major_weights, test_rocm_gateup_shuffles_once_and_down_proj_keeps_preshuffled_backend`; `vllm/models/deepseek_v4/amd/rocm.py` modified +16/-59 (75 lines); hunks: -62,21 +62,6 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torc...; -792,13 +777,12 @@ def _prep(linear) -> torch.Tensor | None:; symbols: _build_indptr_from_lengths, weight_already_preshuffled, apply_pre_quantized_block_scaled_mm, _prep, touching `_build_indptr_from_lengths, weight_already_preshuffled, apply_pre_quantized_block_scaled_mm`; `vllm/models/deepseek_v4/amd/model.py` modified +6/-11 (17 lines); hunks: -71,10 +71,7; -152,13 +149,11 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward, touching `prepare_gateup_preshuffle, forward`.
- Code diff details:
  - `tests/models/test_deepseek_v4_vl_rocm.py` modified +0/-125 (125 lines); hunks: -15,131 +15,6; symbols: _preshuffled_fp8_linear, test_rocm_wo_a_keeps_row_major_weights, test_rocm_gateup_shuffles_once_and_down_proj_keeps_preshuffled_backend, test_rocm_fused_qkv_quant_matches_preshuffled_gemm_scale_layout
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +16/-59 (75 lines); hunks: -62,21 +62,6 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torc...; -792,13 +777,12 @@ def _prep(linear) -> torch.Tensor | None:; symbols: _build_indptr_from_lengths, weight_already_preshuffled, apply_pre_quantized_block_scaled_mm, _prep
  - `vllm/models/deepseek_v4/amd/model.py` modified +6/-11 (17 lines); hunks: -71,10 +71,7; -152,13 +149,11 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_vl_rocm.py
@@ -15,131 +15,6 @@
-def _preshuffled_fp8_linear(
-    holder: str = "quant_method", weight_shape: tuple[int, int] = (256, 128)
-) -> nn.Module:
-    pytest.importorskip("aiter")
-    from vllm.model_executor.kernels.linear.scaled_mm.aiter import (
-        AiterPreshuffledFp8BlockScaledMMKernel,
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -62,21 +62,6 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torch.Tensor:
-def weight_already_preshuffled(linear: torch.nn.Module) -> bool:
-    """True when the linear's kernel already B-preshuffled ``weight``.
-    The hand-shuffles below (fused_wqa_wkv, wo_b, gate_up_proj) must be skipped
-    for those, since shuffle_weight is a permutation rather than an involution.
-    """
-    return any(
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -71,10 +71,7 @@
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_vl_rocm.py` modified +0/-125
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +16/-59; `vllm/models/deepseek_v4/amd/model.py` modified +6/-11
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_vl_rocm.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #57152 - [Bugfix][Model] Restore causal image SWA for DeepSeek V4.1

- Link: https://github.com/vllm-project/vllm/pull/57152
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` and 7 files; associated commits `9f9e1dac26ff`
- Diff scope read: GitHub Pull Request files API returned 8 files, +122/-174, 606 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Model] Restore causal image SWA for DeepSeek V4.1"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`; technical summary: Covers "[Bugfix][Model] Restore causal image SWA for DeepSeek V4.1"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +31/-108 (139 lines); hunks: -818,16 +818,12 @@ def combine_topk_swa_indices(; -856,9 +852,6 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices, CompileKey, kernel, touching `combine_topk_swa_indices, CompileKey, kernel`; `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +2/-19 (21 lines); hunks: -120,9 +120,7 @@ def forward_mqa(; -303,7 +301,7 @@ def _forward_prefill(; symbols: forward_mqa, _forward_prefill, touching `forward_mqa, _forward_prefill`; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +2/-17 (19 lines); hunks: -311,7 +311,7 @@ def _reserve_prefill_workspace(self, q: torch.Tensor) -> None:; -411,7 +411,7 @@ def _forward_prefill_mega(; symbols: _reserve_prefill_workspace, _forward_prefill_mega, touching `_reserve_prefill_workspace, _forward_prefill_mega`; `vllm/models/deepseek_v41/attention.py` modified +0/-8 (8 lines); hunks: -290,13 +290,6 @@ def __init__(; -578,7 +571,6 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +31/-108 (139 lines); hunks: -818,16 +818,12 @@ def combine_topk_swa_indices(; -856,9 +852,6 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices, CompileKey, kernel
  - `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +2/-19 (21 lines); hunks: -120,9 +120,7 @@ def forward_mqa(; -303,7 +301,7 @@ def _forward_prefill(; symbols: forward_mqa, _forward_prefill
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +2/-17 (19 lines); hunks: -311,7 +311,7 @@ def _reserve_prefill_workspace(self, q: torch.Tensor) -> None:; -411,7 +411,7 @@ def _forward_prefill_mega(; symbols: _reserve_prefill_workspace, _forward_prefill_mega
  - `vllm/models/deepseek_v41/attention.py` modified +0/-8 (8 lines); hunks: -290,13 +290,6 @@ def __init__(; -578,7 +571,6 @@ def __init__(; symbols: __init__
  - `vllm/transformers_utils/configs/deepseek_v41.py` modified +0/-8 (8 lines); hunks: -60,11 +60,3 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -818,16 +818,12 @@ def combine_topk_swa_indices(
-    left_visible: torch.Tensor | None = None,
-    right_visible: torch.Tensor | None = None,
-    max_image_tokens: int = 0,
-    # max_image_tokens widens the SWA column region for in-image
-    # bidirectional visibility; the width is fixed per model so the
-    # caller-provided workspace stays valid on image-free batches.
diff -- vllm/models/deepseek_v41/nvidia/flashmla.py
@@ -120,9 +120,7 @@ def forward_mqa(
-            combined_topk = round_up(
-                top_k + self.window_size + self.max_image_tokens, 128
-            )
+            combined_topk = round_up(top_k + self.window_size, 128)
@@ -303,7 +301,7 @@ def _forward_prefill(
-        combined_topk = round_up(top_k + self.window_size + self.max_image_tokens, 128)
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -311,7 +311,7 @@ def _reserve_prefill_workspace(self, q: torch.Tensor) -> None:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +31/-108; `vllm/models/deepseek_v41/nvidia/flashmla.py` modified +2/-19; `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` modified +2/-17; `vllm/models/deepseek_v41/attention.py` modified +0/-8; `vllm/transformers_utils/configs/deepseek_v41.py` modified +0/-8; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` modified +0/-4
  - tests: `tests/v1/attention/test_deepseek_v4_swa_visible.py` modified +81/-6
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_deepseek_v4_swa_visible.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56935 - [Model][DSv4.1] FlashMLA mega attention and the NVFP4 compressed KV cache

- Link: https://github.com/vllm-project/vllm/pull/56935
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` and 12 files; associated commits `d6a1677d5504`
- Diff scope read: GitHub Pull Request files API returned 20 files, +1811/-156, 2550 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][DSv4.1] FlashMLA mega attention and the NVFP4 compressed KV cache"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`; technical summary: Covers "[Model][DSv4.1] FlashMLA mega attention and the NVFP4 compressed KV cache"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` added +497/-0 (497 lines); hunks: -0,0 +1,497; symbols: is_flashmla_mega_attn_supported, alloc_mega_attn_output, _token_slice, DeepseekV4MegaAttnAttention, touching `is_flashmla_mega_attn_supported, alloc_mega_attn_output, _token_slice`; `vllm/models/deepseek_v41/attention.py` modified +150/-54 (204 lines); hunks: -44,6 +44,7; -127,34 +128,40 @@ def _use_v41_mxfp8_kv_record() -> bool:; symbols: _use_v41_mxfp8_kv_record, _resolve_dsv4_kv_cache_dtype, DeepseekV4Attention, accepts_unnormed_unroped_query, touching `_use_v41_mxfp8_kv_record, _resolve_dsv4_kv_cache_dtype, DeepseekV4Attention`; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +96/-2 (98 lines); hunks: -43,10 +43,16; -496,6 +502,73 @@ def _dequantize_and_gather_k_mxfp8_kernel(; symbols: _dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel, dequantize_and_gather_k_cache_triton, dequantize_and_gather_k_cache, touching `_dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel, dequantize_and_gather_k_cache_triton`; `vllm/models/deepseek_v41/common/ops/fused_layout.py` added +86/-0 (86 lines); hunks: -0,0 +1,86; symbols: q_fused_permutation, o_fused_permutation, o_fused_chunk_permutation, permute_q_to_fused, touching `q_fused_permutation, o_fused_permutation, o_fused_chunk_permutation`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` added +497/-0 (497 lines); hunks: -0,0 +1,497; symbols: is_flashmla_mega_attn_supported, alloc_mega_attn_output, _token_slice, DeepseekV4MegaAttnAttention
  - `vllm/models/deepseek_v41/attention.py` modified +150/-54 (204 lines); hunks: -44,6 +44,7; -127,34 +128,40 @@ def _use_v41_mxfp8_kv_record() -> bool:; symbols: _use_v41_mxfp8_kv_record, _resolve_dsv4_kv_cache_dtype, DeepseekV4Attention, accepts_unnormed_unroped_query
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +96/-2 (98 lines); hunks: -43,10 +43,16; -496,6 +502,73 @@ def _dequantize_and_gather_k_mxfp8_kernel(; symbols: _dequantize_and_gather_k_mxfp8_kernel, _dequantize_and_gather_k_nvfp4_kernel, dequantize_and_gather_k_cache_triton, dequantize_and_gather_k_cache
  - `vllm/models/deepseek_v41/common/ops/fused_layout.py` added +86/-0 (86 lines); hunks: -0,0 +1,86; symbols: q_fused_permutation, o_fused_permutation, o_fused_chunk_permutation, permute_q_to_fused
  - `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +71/-13 (84 lines); hunks: -4,6 +4,7; -232,13 +233,14 @@ def rope_quant_insert(; symbols: rope_quant_insert, _rope_quant_insert_mxfp8_kernel, _rope_quant_insert_nvfp4_kernel, _rope_plain_insert_kernel
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py
@@ -0,0 +1,497 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DeepSeek V4.1 attention on FlashMLA's mega-attention kernel (SM100).
+One kernel does Q RoPE, sparse attention, the inverse RoPE of the output and
+its FP8 cast, and writes straight into the buffer ``wo_a`` consumes. So the
+layer declares ``accepts_unnormed_unroped_query`` -- the kernel RoPEs Q itself,
diff -- vllm/models/deepseek_v41/attention.py
@@ -44,6 +44,7 @@
+from vllm.config.cache import CacheDType
@@ -127,34 +128,40 @@ def _use_v41_mxfp8_kv_record() -> bool:
-    kv_cache_dtype: str,
+    kv_cache_dtype: CacheDType,
-) -> tuple[str, torch.dtype]:
+    packed_kv_cache_dtype: CacheDType = "fp8_ds_mla",
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -43,10 +43,16 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` added +497/-0; `vllm/models/deepseek_v41/attention.py` modified +150/-54; `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +96/-2; `vllm/models/deepseek_v41/common/ops/fused_layout.py` added +86/-0; `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +71/-13; `vllm/models/deepseek_v41/sparse_mla.py` modified +51/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_dsv41_mega_attn_layouts.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56568 - [Perf][DSV4.1] Pad shared experts for native MegaMoE fusion

- Link: https://github.com/vllm-project/vllm/pull/56568
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `03f67b3ad1e6`
- Diff scope read: GitHub Pull Request files API returned 2 files, +128/-23, 259 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSV4.1] Pad shared experts for native MegaMoE fusion"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`; technical summary: Covers "[Perf][DSV4.1] Pad shared experts for native MegaMoE fusion"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +80/-18 (98 lines); hunks: -367,17 +367,21 @@ def test_deepseek_v4_mega_moe_padding_preserves_weights(mo...; -402,6 +406,7 @@ def fp8_fp4_mega_moe(; symbols: test_deepseek_v4_mega_moe_padding_preserves_weights, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights, FakeDeepGemm, get_symm_buffer_for_mega_moe, touching `test_deepseek_v4_mega_moe_padding_preserves_weights, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights, FakeDeepGemm`; `vllm/models/deepseek_v4/nvidia/model.py` modified +48/-5 (53 lines); hunks: -204,6 +204,7 @@ def __init__(; -386,6 +387,17 @@ def _finalize_shared_expert_weights(; symbols: __init__, _finalize_shared_expert_weights, _prepare_shared_expert_scale, touching `__init__, _finalize_shared_expert_weights, _prepare_shared_expert_scale`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +80/-18 (98 lines); hunks: -367,17 +367,21 @@ def test_deepseek_v4_mega_moe_padding_preserves_weights(mo...; -402,6 +406,7 @@ def fp8_fp4_mega_moe(; symbols: test_deepseek_v4_mega_moe_padding_preserves_weights, test_deepseek_v4_mega_moe_finalizes_native_shared_expert_weights, FakeDeepGemm, get_symm_buffer_for_mega_moe
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +48/-5 (53 lines); hunks: -204,6 +204,7 @@ def __init__(; -386,6 +387,17 @@ def _finalize_shared_expert_weights(; symbols: __init__, _finalize_shared_expert_weights, _prepare_shared_expert_scale
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -367,17 +367,21 @@ def test_deepseek_v4_mega_moe_padding_preserves_weights(monkeypatch, intermediat
-        pytest.param(5120, 2304, 32, False, False, id="deepseek-v41-flash"),
+        pytest.param(5120, 2304, 32, True, False, id="deepseek-v41-flash"),
+        pytest.param(128, 2304, 128, True, False, id="padded-block128"),
+        pytest.param(5120, 2304, 32, True, True, id="deepseek-v41-flash-mxfp8"),
+        pytest.param(128, 2304, 128, False, False, id="padded-packed-scale-fallback"),
-    """V4.1-Flash's routed padding must preserve the serial shared-expert fallback."""
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -204,6 +204,7 @@ def __init__(
+        self.unpadded_intermediate_size = intermediate_size
@@ -386,6 +387,17 @@ def _finalize_shared_expert_weights(
+        unpadded_size = self.unpadded_intermediate_size * self.num_shared_experts
+        padding = self.intermediate_size * self.num_shared_experts - unpadded_size
+        pad_weights = (
+            padding > 0
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +80/-18
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +48/-5
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56441 - [Perf][DSpark] Add KV-only context insertion across V4.1 cache formats

- Link: https://github.com/vllm-project/vllm/pull/56441
- Status/date: merged / 2026-09-16
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/dspark.py`; associated commits `6ecd97f1b7fb`
- Diff scope read: GitHub Pull Request files API returned 5 files, +234/-61, 345 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSpark] Add KV-only context insertion across V4.1 cache formats"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/dspark.py`; technical summary: Covers "[Perf][DSpark] Add KV-only context insertion across V4.1 cache formats"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/dspark.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/dspark.py` modified +17/-60 (77 lines); hunks: -234,67 +234,24 @@ def _insert_context_kv(; symbols: _insert_context_kv, DSparkDeepseekV4ForCausalLM, touching `_insert_context_kv, DSparkDeepseekV4ForCausalLM`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/dspark.py` modified +17/-60 (77 lines); hunks: -234,67 +234,24 @@ def _insert_context_kv(; symbols: _insert_context_kv, DSparkDeepseekV4ForCausalLM
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/dspark.py
@@ -234,67 +234,24 @@ def _insert_context_kv(
-    """RoPE + quant + paged-cache insert of (already kv_norm'd) context KV.
-    Reuses the DSV4 fused insert ops (which also process a query; we pass a dummy
-    query and discard it, since context tokens have no query). Mirrors
-    ``DeepseekV4Attention._fused_qnorm_rope_kv_insert``.
-    """
-    swa_cache = attn.swa_cache_layer.kv_cache
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/dspark.py` modified +17/-60
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56254 - [DSA] Wire DeepGEMM sparse MQA logits into the DeepSeek V4.1 indexer

- Link: https://github.com/vllm-project/vllm/pull/56254
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py`, `vllm/models/deepseek_v41/attention.py`; associated commits `12575123059c`
- Diff scope read: GitHub Pull Request files API returned 13 files, +1830/-26, 2149 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSA] Wire DeepGEMM sparse MQA logits into the DeepSeek V4.1 indexer"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py`; technical summary: Covers "[DSA] Wire DeepGEMM sparse MQA logits into the DeepSeek V4.1 indexer"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` modified +67/-20 (87 lines); hunks: -4,6 +4,7; -25,6 +26,7; symbols: __init__, get_kv_cache_spec, forward, get_attn_backend, touching `__init__, get_kv_cache_spec, forward`; `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +22/-2 (24 lines); hunks: -309,12 +309,22 @@ def __call__(; -434,12 +444,14 @@ def dispatch( # type: ignore[override]; symbols: __call__, _indexer_weights_out_dtypes, FusedIndexerQRopeMxFp4TritonKernel, CompileKey, touching `__call__, _indexer_weights_out_dtypes, FusedIndexerQRopeMxFp4TritonKernel`; `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` modified +15/-2 (17 lines); hunks: -165,6 +165,7 @@ class CompileKey:; -177,6 +178,7 @@ def kernel(compile_key: CompileKey) -> Any:; symbols: CompileKey, kernel, device_kernel, host_entrypoint, touching `CompileKey, kernel, device_kernel`; `vllm/config/attention.py` modified +9/-0 (9 lines); hunks: -86,6 +86,15 @@ class AttentionConfig:; symbols: AttentionConfig, GPU, touching `AttentionConfig, GPU`.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` modified +67/-20 (87 lines); hunks: -4,6 +4,7; -25,6 +26,7; symbols: __init__, get_kv_cache_spec, forward, get_attn_backend
  - `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +22/-2 (24 lines); hunks: -309,12 +309,22 @@ def __call__(; -434,12 +444,14 @@ def dispatch( # type: ignore[override]; symbols: __call__, _indexer_weights_out_dtypes, FusedIndexerQRopeMxFp4TritonKernel, CompileKey
  - `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` modified +15/-2 (17 lines); hunks: -165,6 +165,7 @@ class CompileKey:; -177,6 +178,7 @@ def kernel(compile_key: CompileKey) -> Any:; symbols: CompileKey, kernel, device_kernel, host_entrypoint
  - `vllm/config/attention.py` modified +9/-0 (9 lines); hunks: -86,6 +86,15 @@ class AttentionConfig:; symbols: AttentionConfig, GPU
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -4,6 +4,7 @@
+import math
@@ -25,6 +26,7 @@
+from vllm.model_executor.layers.sparse_mqa_indexer import SparseMQAIndexer
@@ -63,6 +65,9 @@
+from vllm.v1.attention.backends.mla.sparse_indexer import (
+    DeepseekV41SparseIndexerBackend,
diff -- vllm/models/deepseek_v4/common/ops/fused_indexer_q.py
@@ -309,12 +309,22 @@ def __call__(
+def _indexer_weights_out_dtypes(vllm_config: Any) -> tuple[torch.dtype, ...]:
+    """Weights dtypes the model's indexer layers ask for: fp32 for the dense
+    scoring kernels, plus bf16 when the DeepSeek V4.1 sparse-logits indexer
+    (`SparseMQAIndexer`) is enabled."""
+    if vllm_config.attention_config.indexer_sparse_logits:
+        return (torch.float32, torch.bfloat16)
diff -- vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py
@@ -165,6 +165,7 @@ class CompileKey:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` modified +67/-20; `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +22/-2; `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` modified +15/-2; `vllm/config/attention.py` modified +9/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_fused_indexer_q_rope_quant.py`, `tests/model_executor/layers/test_mla_short_prefill_indexer.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56962 - [Perf][Kernel] Integrate Mega-mHC from DeepGEMM for DeepSeek V4.1 (reopen of #56255)

- Link: https://github.com/vllm-project/vllm/pull/56962
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/__init__.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`; associated commits `bb5507741155`
- Diff scope read: GitHub Pull Request files API returned 6 files, +316/-41, 471 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][Kernel] Integrate Mega-mHC from DeepGEMM for DeepSeek V4.1 (reopen of #56255)"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/__init__.py`; technical summary: Covers "[Perf][Kernel] Integrate Mega-mHC from DeepGEMM for DeepSeek V4.1 (reopen of #56255)"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/__init__.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` added +156/-0 (156 lines); hunks: -0,0 +1,156; symbols: is_mega_mhc_supported, mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre, touching `is_mega_mhc_supported, mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre`; `vllm/models/deepseek_v41/nvidia/model.py` modified +34/-38 (72 lines); hunks: -20,7 +20,6; -79,6 +78,7; symbols: forward, touching `forward`; `vllm/models/deepseek_v41/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` added +156/-0 (156 lines); hunks: -0,0 +1,156; symbols: is_mega_mhc_supported, mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +34/-38 (72 lines); hunks: -20,7 +20,6; -79,6 +78,7; symbols: forward
  - `vllm/models/deepseek_v41/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py
@@ -0,0 +1,156 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import functools
+import torch
+from vllm.model_executor.kernels.mhc.tilelang import (
+    mhc_fused_post_pre_delayed_tilelang,
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -20,7 +20,6 @@
-    mhc_fused_post_pre_delayed_tilelang,
@@ -79,6 +78,7 @@
+from .ops.mega_mhc import mhc_shifted_post_pre
@@ -403,25 +403,23 @@ def forward(
-            residual, post_mix, res_mix, x, attn_pre, aux = (
-                mhc_fused_post_pre_delayed_tilelang(
diff -- vllm/models/deepseek_v41/nvidia/ops/__init__.py
@@ -0,0 +1,2 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py` added +156/-0; `vllm/models/deepseek_v41/nvidia/model.py` modified +34/-38; `vllm/models/deepseek_v41/nvidia/ops/__init__.py` added +2/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/quantization/test_block_fp8.py`, `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56903 - [Perf][DSpark] Collapse DeepSeek-V4.1 draft states before SP all-gather

- Link: https://github.com/vllm-project/vllm/pull/56903
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/dspark.py`; associated commits `073f883b56a5`
- Diff scope read: GitHub Pull Request files API returned 2 files, +23/-3, 46 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSpark] Collapse DeepSeek-V4.1 draft states before SP all-gather"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/dspark.py`; technical summary: Covers "[Perf][DSpark] Collapse DeepSeek-V4.1 draft states before SP all-gather"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/dspark.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/dspark.py` modified +2/-3 (5 lines); hunks: -217,15 +217,14 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/dspark.py` modified +2/-3 (5 lines); hunks: -217,15 +217,14 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/dspark.py
@@ -217,15 +217,14 @@ def forward(
-        if self.use_sequence_parallel:
-            hidden_states = sp_all_gather(hidden_states)[:full_num_tokens]
-            pre_mix = sp_all_gather(pre_mix)[:full_num_tokens]
+        if self.use_sequence_parallel:
+            hidden_states = sp_all_gather(hidden_states)[:full_num_tokens]
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/dspark.py` modified +2/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56255 - [DSv4.1] Integrate Mega-mHC from DeepGEMM

- Link: https://github.com/vllm-project/vllm/pull/56255
- Status/date: closed / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/__init__.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`; associated commits `bb5507741155`
- Diff scope read: GitHub Pull Request files API returned 11 files, +315/-43, 566 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSv4.1] Integrate Mega-mHC from DeepGEMM"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4_1/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v4_1/nvidia/model.py`, `vllm/models/deepseek_v4_1/nvidia/ops/__init__.py`; technical summary: Covers "[DSv4.1] Integrate Mega-mHC from DeepGEMM"; the main implementation surface is `vllm/models/deepseek_v4_1/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v4_1/nvidia/model.py`, `vllm/models/deepseek_v4_1/nvidia/ops/__init__.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4_1/nvidia/ops/mega_mhc.py` added +144/-0 (144 lines); hunks: -0,0 +1,144; symbols: is_mega_mhc_supported, mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre, touching `is_mega_mhc_supported, mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre`; `vllm/models/deepseek_v4_1/nvidia/model.py` modified +41/-21 (62 lines); hunks: -76,6 +76,7; -334,30 +335,48 @@ def forward(; symbols: forward, touching `forward`; `vllm/models/deepseek_v4_1/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2.
- Code diff details:
  - `vllm/models/deepseek_v4_1/nvidia/ops/mega_mhc.py` added +144/-0 (144 lines); hunks: -0,0 +1,144; symbols: is_mega_mhc_supported, mhc_shifted_post_pre_deep_gemm, mhc_shifted_post_pre
  - `vllm/models/deepseek_v4_1/nvidia/model.py` modified +41/-21 (62 lines); hunks: -76,6 +76,7; -334,30 +335,48 @@ def forward(; symbols: forward
  - `vllm/models/deepseek_v4_1/nvidia/ops/__init__.py` added +2/-0 (2 lines); hunks: -0,0 +1,2
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4_1/nvidia/ops/mega_mhc.py
@@ -0,0 +1,144 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import functools
+import torch
+from vllm.model_executor.kernels.mhc.tilelang import (
+    mhc_post_tilelang,
diff -- vllm/models/deepseek_v4_1/nvidia/model.py
@@ -76,6 +76,7 @@
+from .ops.mega_mhc import mhc_shifted_post_pre
@@ -334,30 +335,48 @@ def forward(
-            residual = mhc_post_tilelang(x, residual, post_mix, res_mix)
+                residual = mhc_post_tilelang(x, residual, post_mix, res_mix)
-            post_mix, res_mix, x, attn_pre = mhc_pre_delayed_tilelang(
-                residual,
diff -- vllm/models/deepseek_v4_1/nvidia/ops/__init__.py
@@ -0,0 +1,2 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4_1/nvidia/ops/mega_mhc.py` added +144/-0; `vllm/models/deepseek_v4_1/nvidia/model.py` modified +41/-21; `vllm/models/deepseek_v4_1/nvidia/ops/__init__.py` added +2/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/quantization/test_block_fp8.py`, `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56893 - [Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record)

- Link: https://github.com/vllm-project/vllm/pull/56893
- Status/date: merged / 2026-09-15
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`, `vllm/models/deepseek_v41/amd/dspark.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py` and 7 files; associated commits `e6eb0d120c48`
- Diff scope read: GitHub Pull Request files API returned 14 files, +709/-110, 1334 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record)"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`; technical summary: Covers "[Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record)"; the main implementation surface is `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +186/-8 (194 lines); hunks: -36,6 +36,18; -163,23 +175,81 @@ def quantize_and_insert_k_kernel(; symbols: quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, quantize_and_insert_k_cache, touching `quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, quantize_and_insert_k_cache`; `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +70/-6 (76 lines); hunks: -232,10 +232,13 @@ def rope_quant_insert(; -246,8 +249,15 @@ def rope_quant_insert(; symbols: rope_quant_insert, _rope_quant_insert_kernel, _rope_quant_insert_mxfp8_kernel, _rope_plain_insert_kernel, touching `rope_quant_insert, _rope_quant_insert_kernel, _rope_quant_insert_mxfp8_kernel`; `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +39/-23 (62 lines); hunks: -23,10 +23,11; -35,17 +36,20 @@ class DequantGatherKCacheKernel(; symbols: DequantGatherKCacheKernel, CompileKey, kernel, load_g2s, touching `DequantGatherKCacheKernel, CompileKey, kernel`; `vllm/models/deepseek_v41/attention.py` modified +34/-9 (43 lines); hunks: -51,6 +51,7; -109,6 +110,16 @@ def _fill_short_context_topk_indices(; symbols: _fill_short_context_topk_indices, _use_v41_mxfp8_kv_record, _resolve_dsv4_kv_cache_dtype, __init__, touching `_fill_short_context_topk_indices, _use_v41_mxfp8_kv_record, _resolve_dsv4_kv_cache_dtype`.
- Code diff details:
  - `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +186/-8 (194 lines); hunks: -36,6 +36,18; -163,23 +175,81 @@ def quantize_and_insert_k_kernel(; symbols: quantize_and_insert_k_kernel, _quantize_and_insert_k_mxfp8_kernel, quantize_and_insert_k_cache
  - `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +70/-6 (76 lines); hunks: -232,10 +232,13 @@ def rope_quant_insert(; -246,8 +249,15 @@ def rope_quant_insert(; symbols: rope_quant_insert, _rope_quant_insert_kernel, _rope_quant_insert_mxfp8_kernel, _rope_plain_insert_kernel
  - `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +39/-23 (62 lines); hunks: -23,10 +23,11; -35,17 +36,20 @@ class DequantGatherKCacheKernel(; symbols: DequantGatherKCacheKernel, CompileKey, kernel, load_g2s
  - `vllm/models/deepseek_v41/attention.py` modified +34/-9 (43 lines); hunks: -51,6 +51,7; -109,6 +110,16 @@ def _fill_short_context_topk_indices(; symbols: _fill_short_context_topk_indices, _use_v41_mxfp8_kv_record, _resolve_dsv4_kv_cache_dtype, __init__
  - `vllm/models/deepseek_v41/amd/dspark.py` modified +2/-0 (2 lines); hunks: -259,6 +259,8 @@ def _insert_context_kv(; symbols: _insert_context_kv
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/common/ops/cache_utils.py
@@ -36,6 +36,18 @@
+# Per-token byte width of the two paged fp8 records. Both put a page's whole
+# data region ahead of its whole scale region, so ``k_cache.shape[-1]`` -- the
+# width the KV-cache spec publishes -- identifies the record:
+#   V4   (584 B): 448 fp8 e4m3 NoPE + 64 bf16 RoPE, then 7 UE8M0 scales of 64
+#                 dims each plus a pad byte.
+#   V4.1 (528 B): all 512 dims as fp8 e4m3 (RoPE included), then 16 UE8M0
diff -- vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py
@@ -232,10 +232,13 @@ def rope_quant_insert(
-    layout: ``uint8`` is the fp8_ds_mla paged layout (576 value bytes and eight
-    segregated UE8M0 scale bytes per token, including one zero padding scale);
-    ``bfloat16`` and ``float8_e4m3fn`` are the plain [448 NoPE | 64 RoPE] rows
-    read by FlashInfer, the latter scaled by the per-tensor ``fp8_scale``.
+    layout: ``uint8`` is the fp8_ds_mla paged layout, whose record the
+    per-token byte width names -- 584 B for V4 (576 value bytes and eight
diff -- vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py
@@ -23,10 +23,11 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/common/ops/cache_utils.py` modified +186/-8; `vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py` modified +70/-6; `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +39/-23; `vllm/models/deepseek_v41/attention.py` modified +34/-9; `vllm/models/deepseek_v41/amd/dspark.py` modified +2/-0; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +2/-0
  - tests: `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +98/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56513 - [ROCm][DSV4.1][Perf] Fold the mHC post step into the delayed pre projection

- Link: https://github.com/vllm-project/vllm/pull/56513
- Status/date: merged / 2026-09-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/amd/model.py`; associated commits `00972dfd7298`
- Diff scope read: GitHub Pull Request files API returned 5 files, +346/-64, 633 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSV4.1][Perf] Fold the mHC post step into the delayed pre projection"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/amd/model.py`; technical summary: Covers "[ROCm][DSV4.1][Perf] Fold the mHC post step into the delayed pre projection"; the main implementation surface is `vllm/models/deepseek_v41/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/amd/model.py` modified +37/-17 (54 lines); hunks: -274,7 +274,7 @@ def forward(; -288,7 +288,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/amd/model.py` modified +37/-17 (54 lines); hunks: -274,7 +274,7 @@ def forward(; -288,7 +288,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/amd/model.py
@@ -274,7 +274,7 @@ def forward(
-                post_mix, res_mix, x, attn_pre = self.mhc_pre_delayed(
+                residual, post_mix, res_mix, x, attn_pre = self.mhc_pre_delayed(
@@ -288,7 +288,7 @@ def forward(
-                post_mix, res_mix, x, attn_pre = self.mhc_pre_delayed(
+                residual, post_mix, res_mix, x, attn_pre = self.mhc_pre_delayed(
@@ -301,18 +301,7 @@ def forward(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/amd/model.py` modified +37/-17
- Risk and verification: The diff ships test coverage in `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56633 - [Perf][DSv4.1] Fold the mHC post block into the delayed pre projection

- Link: https://github.com/vllm-project/vllm/pull/56633
- Status/date: merged / 2026-09-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v41/nvidia/dspark.py`, `vllm/models/deepseek_v41/nvidia/model.py`; associated commits `5372e72a9884`
- Diff scope read: GitHub Pull Request files API returned 8 files, +837/-92, 1316 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf][DSv4.1] Fold the mHC post block into the delayed pre projection"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`; technical summary: Covers "[Perf][DSv4.1] Fold the mHC post block into the delayed pre projection"; the main implementation surface is `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/nvidia/model.py` modified +126/-52 (178 lines); hunks: -20,6 +20,7; -214,17 +215,45 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +1/-1 (2 lines); hunks: -207,7 +207,7 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v41/nvidia/model.py` modified +126/-52 (178 lines); hunks: -20,6 +20,7; -214,17 +215,45 @@ def __init__(; symbols: __init__, forward
  - `vllm/models/deepseek_v41/nvidia/dspark.py` modified +1/-1 (2 lines); hunks: -207,7 +207,7 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/nvidia/model.py
@@ -20,6 +20,7 @@
+    mhc_fused_post_pre_delayed_tilelang,
@@ -214,17 +215,45 @@ def __init__(
+            from vllm.model_executor.kernels.mhc.tilelang_kernels import (
+                mhc_fused_post_pre_splits,
+            )
-            for input_size, use_pre_mix in (
diff -- vllm/models/deepseek_v41/nvidia/dspark.py
@@ -207,7 +207,7 @@ def forward(
-            hidden_states, residual, post_mix, res_mix, pre_mix = layer(
+            hidden_states, residual, post_mix, res_mix, pre_mix, _ = layer(
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/nvidia/model.py` modified +126/-52; `vllm/models/deepseek_v41/nvidia/dspark.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_mhc_jit_warmup.py`, `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #51794 - [ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/51794
- Status/date: merged / 2026-09-14
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/cpu/cpu_sparse.py`; associated commits `a6c5d6d0fcd7`
- Diff scope read: GitHub Pull Request files API returned 4 files, +214/-25, 317 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +194/-0 (194 lines); hunks: -23,6 +23,7; -571,6 +572,199 @@ def __init__(self, *args, **kwargs):; symbols: __init__, _enable_csa_multi_stream, _run_sequential_pipeline, forward, touching `__init__, _enable_csa_multi_stream, _run_sequential_pipeline`; `vllm/models/deepseek_v4/attention.py` modified +17/-14 (31 lines); hunks: -318,7 +318,6 @@ def __init__(; -584,7 +583,7 @@ def project_query_and_cache_kv() -> torch.Tensor:; symbols: __init__, project_query_and_cache_kv, _run_parallel_input_projections, forward, touching `__init__, project_query_and_cache_kv, _run_parallel_input_projections`; `vllm/models/deepseek_v4/amd/model.py` modified +1/-10 (11 lines); hunks: -957,16 +957,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__, touching `__init__`; `vllm/models/deepseek_v4/cpu/cpu_sparse.py` modified +2/-1 (3 lines); hunks: -198,11 +198,12 @@ def forward(; symbols: forward, touching `forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +194/-0 (194 lines); hunks: -23,6 +23,7; -571,6 +572,199 @@ def __init__(self, *args, **kwargs):; symbols: __init__, _enable_csa_multi_stream, _run_sequential_pipeline, forward
  - `vllm/models/deepseek_v4/attention.py` modified +17/-14 (31 lines); hunks: -318,7 +318,6 @@ def __init__(; -584,7 +583,7 @@ def project_query_and_cache_kv() -> torch.Tensor:; symbols: __init__, project_query_and_cache_kv, _run_parallel_input_projections, forward
  - `vllm/models/deepseek_v4/amd/model.py` modified +1/-10 (11 lines); hunks: -957,16 +957,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str...; symbols: __init__
  - `vllm/models/deepseek_v4/cpu/cpu_sparse.py` modified +2/-1 (3 lines); hunks: -198,11 +198,12 @@ def forward(; symbols: forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -23,6 +23,7 @@
+from vllm.utils.multi_stream_utils import execute_in_parallel
@@ -571,6 +572,199 @@ def __init__(self, *args, **kwargs):
+        if self.indexer is None:
+            # Only enable multi-stream overlap for CSA layer now.
+            self.aux_stream_list = None
+        else:
diff -- vllm/models/deepseek_v4/attention.py
@@ -318,7 +318,6 @@ def __init__(
-        # Will be None on ROCm for now.
@@ -584,7 +583,7 @@ def project_query_and_cache_kv() -> torch.Tensor:
-        # indexer. ROCm runs the same work sequentially without aux streams.
+        # indexer.
@@ -671,7 +670,6 @@ def _run_parallel_input_projections(
-        # On ROCm, aux_streams is None and execute_in_parallel runs serially.
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -957,16 +957,7 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +194/-0; `vllm/models/deepseek_v4/attention.py` modified +17/-14; `vllm/models/deepseek_v4/amd/model.py` modified +1/-10; `vllm/models/deepseek_v4/cpu/cpu_sparse.py` modified +2/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #56741 - [Refactor] Normalize DeepSeek V4.1 model package naming

- Link: https://github.com/vllm-project/vllm/pull/56741
- Status/date: merged / 2026-09-14
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/models/deepseek_v41/__init__.py`, `vllm/models/deepseek_v41/amd/__init__.py`, `vllm/models/deepseek_v41/amd/dspark.py` and 29 files; associated commits `cf1584f373d0`
- Diff scope read: GitHub Pull Request files API returned 44 files, +71/-72, 476 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Refactor] Normalize DeepSeek V4.1 model package naming"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/nvidia/engram.py`; technical summary: Covers "[Refactor] Normalize DeepSeek V4.1 model package naming"; the main implementation surface is `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/nvidia/engram.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v41/attention.py` renamed +7/-7 (14 lines); hunks: -26,7 +26,7; -49,8 +49,8; symbols: DeepseekV4Attention, __init__, forward, _can_fuse_query_quant, touching `DeepseekV4Attention, __init__, forward`; `vllm/models/deepseek_v41/amd/rocm.py` renamed +3/-3 (6 lines); hunks: -13,9 +13,9; `vllm/models/deepseek_v41/nvidia/engram.py` renamed +3/-3 (6 lines); hunks: -23,16 +23,16; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` renamed +3/-3 (6 lines); hunks: -13,12 +13,12.
- Code diff details:
  - `vllm/models/deepseek_v41/attention.py` renamed +7/-7 (14 lines); hunks: -26,7 +26,7; -49,8 +49,8; symbols: DeepseekV4Attention, __init__, forward, _can_fuse_query_quant
  - `vllm/models/deepseek_v41/amd/rocm.py` renamed +3/-3 (6 lines); hunks: -13,9 +13,9
  - `vllm/models/deepseek_v41/nvidia/engram.py` renamed +3/-3 (6 lines); hunks: -23,16 +23,16
  - `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` renamed +3/-3 (6 lines); hunks: -13,12 +13,12
  - `vllm/models/deepseek_v41/nvidia/flashmla.py` renamed +3/-3 (6 lines); hunks: -10,13 +10,13
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v41/attention.py
@@ -26,7 +26,7 @@
-from vllm.models.deepseek_v4_1.common.ops import (
+from vllm.models.deepseek_v41.common.ops import (
@@ -49,8 +49,8 @@
-from vllm.models.deepseek_v4_1.common.rope import build_deepseek_v4_rope
-from vllm.models.deepseek_v4_1.compressor import DeepseekCompressor
+from vllm.models.deepseek_v41.common.rope import build_deepseek_v4_rope
diff -- vllm/models/deepseek_v41/amd/rocm.py
@@ -13,9 +13,9 @@
-from vllm.models.deepseek_v4_1.attention import DeepseekV4Attention
-from vllm.models.deepseek_v4_1.common.ops import dequantize_and_gather_k_cache
-from vllm.models.deepseek_v4_1.sparse_mla import (
+from vllm.models.deepseek_v41.attention import DeepseekV4Attention
+from vllm.models.deepseek_v41.common.ops import dequantize_and_gather_k_cache
+from vllm.models.deepseek_v41.sparse_mla import (
diff -- vllm/models/deepseek_v41/nvidia/engram.py
@@ -23,16 +23,16 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v41/attention.py` renamed +7/-7; `vllm/models/deepseek_v41/amd/rocm.py` renamed +3/-3; `vllm/models/deepseek_v41/nvidia/engram.py` renamed +3/-3; `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py` renamed +3/-3; `vllm/models/deepseek_v41/nvidia/flashmla.py` renamed +3/-3; `vllm/models/deepseek_v41/nvidia/model.py` renamed +3/-3
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_engram.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56299 - [Bugfix][Frontend] Support Responses text types in DeepSeek V4.1

- Link: https://github.com/vllm-project/vllm/pull/56299
- Status/date: merged / 2026-09-14
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`; associated commits `eb42686a30cd`
- Diff scope read: GitHub Pull Request files API returned 2 files, +19/-1, 34 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Frontend] Support Responses text types in DeepSeek V4.1"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`; technical summary: Covers "[Bugfix][Frontend] Support Responses text types in DeepSeek V4.1"; the main implementation surface is `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0 (18 lines); hunks: -99,6 +99,24 @@ def test_raw_text_parts_preserve_reference_separator():; symbols: test_raw_text_parts_preserve_reference_separator, test_responses_text_parts_match_chat_text_parts, test_mid_system_gets_its_own_marker_and_generation_header, touching `test_raw_text_parts_preserve_reference_separator, test_responses_text_parts_match_chat_text_parts, test_mid_system_gets_its_own_marker_and_generation_header`; `vllm/tokenizers/deepseek_v41.py` modified +1/-1 (2 lines); hunks: -32,7 +32,7 @@ def _normalize_messages(; symbols: _normalize_messages, touching `_normalize_messages`.
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0 (18 lines); hunks: -99,6 +99,24 @@ def test_raw_text_parts_preserve_reference_separator():; symbols: test_raw_text_parts_preserve_reference_separator, test_responses_text_parts_match_chat_text_parts, test_mid_system_gets_its_own_marker_and_generation_header
  - `vllm/tokenizers/deepseek_v41.py` modified +1/-1 (2 lines); hunks: -32,7 +32,7 @@ def _normalize_messages(; symbols: _normalize_messages
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -99,6 +99,24 @@ def test_raw_text_parts_preserve_reference_separator():
+@pytest.mark.parametrize(
+    ("role", "responses_type"),
+    [("user", "input_text"), ("assistant", "output_text")],
+)
+def test_responses_text_parts_match_chat_text_parts(role, responses_type):
+    responses_message = {
diff -- vllm/tokenizers/deepseek_v41.py
@@ -32,7 +32,7 @@ def _normalize_messages(
-                if part_type == "text":
+                if part_type in ("text", "input_text", "output_text"):
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v41.py` modified +18/-0
  - runtime: `vllm/tokenizers/deepseek_v41.py` modified +1/-1
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/test_deepseek_v41.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55897 - [LoRA] Add LoRA support for DeepSeek-V4 Flash Vision

- Link: https://github.com/vllm-project/vllm/pull/55897
- Status/date: merged / 2026-09-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/vl_model.py`; associated commits `dd4c8410707b`
- Diff scope read: GitHub Pull Request files API returned 3 files, +42/-3, 97 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[LoRA] Add LoRA support for DeepSeek-V4 Flash Vision"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/common/vl_model.py`; technical summary: Covers "[LoRA] Add LoRA support for DeepSeek-V4 Flash Vision"; the main implementation surface is `vllm/models/deepseek_v4/common/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/vl_model.py` modified +40/-1 (41 lines); hunks: -25,16 +25,19; -81,17 +84,27 @@ def _make_deepseek_v4_vl_weights_mapper(; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, process_weights_after_loading, touching `_make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/vl_model.py` modified +40/-1 (41 lines); hunks: -25,16 +25,19; -81,17 +84,27 @@ def _make_deepseek_v4_vl_weights_mapper(; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, process_weights_after_loading
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/vl_model.py
@@ -25,16 +25,19 @@
+    SupportsLoRA,
+from vllm.model_executor.models.module_mapping import MultiModelKeys
+from vllm.multimodal.inputs import MultiModalKwargsItem
@@ -81,17 +84,27 @@ def _make_deepseek_v4_vl_weights_mapper(
-    nn.Module, SupportsMultiModal, SupportsPP, SupportsEagle3
+    nn.Module, SupportsMultiModal, SupportsPP, SupportsEagle3, SupportsLoRA
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/vl_model.py` modified +40/-1
- Risk and verification: Runtime changes concentrate in `vllm/lora/ops/triton_ops/lora_shrink_op.py`, `vllm/models/deepseek_v4/common/vl_model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #50178 - [9/N][warmup][DSv4] Migrate MHC TileLang kernels

- Link: https://github.com/vllm-project/vllm/pull/50178
- Status/date: merged / 2026-09-13
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `e52be1a62d38`
- Diff scope read: GitHub Pull Request files API returned 9 files, +1454/-489, 2222 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[9/N][warmup][DSv4] Migrate MHC TileLang kernels"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/glm5next/nvidia/model.py`; technical summary: Covers "[9/N][warmup][DSv4] Migrate MHC TileLang kernels"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/glm5next/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/model.py` modified +59/-0 (59 lines); hunks: -1210,6 +1210,53 @@ def __init__(; -1402,6 +1449,18 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: st...; symbols: __init__, forward, embed_input_ids, touching `__init__, forward, embed_input_ids`; `vllm/models/glm5next/nvidia/model.py` modified +44/-0 (44 lines); hunks: -403,6 +403,50 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +59/-0 (59 lines); hunks: -1210,6 +1210,53 @@ def __init__(; -1402,6 +1449,18 @@ def __init__(self, *, vllm_config: VllmConfig, prefix: st...; symbols: __init__, forward, embed_input_ids
  - `vllm/models/glm5next/nvidia/model.py` modified +44/-0 (44 lines); hunks: -403,6 +403,50 @@ def __init__(; symbols: __init__, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -1210,6 +1210,53 @@ def __init__(
+        if vllm_config.kernel_config.enable_jit_warmup:
+            from vllm.model_executor.kernels.mhc.tilelang_kernels import (
+                _HC_PRENORM_GEMM_TILELANG_KERNEL,
+                _MHC_FUSED_TILELANG_KERNEL,
+                _MHC_POST_TILELANG_KERNEL,
+                _MHC_PRE_BIG_FUSE_TILELANG_KERNEL,
diff -- vllm/models/glm5next/nvidia/model.py
@@ -403,6 +403,50 @@ def __init__(
+            if vllm_config.kernel_config.enable_jit_warmup:
+                from vllm.model_executor.kernels.mhc.tilelang_kernels import (
+                    _HC_PRENORM_GEMM_TILELANG_KERNEL,
+                    _MHC_FUSED_TILELANG_KERNEL,
+                    _MHC_POST_TILELANG_KERNEL,
+                    _MHC_PRE_BIG_FUSE_TILELANG_KERNEL,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +59/-0; `vllm/models/glm5next/nvidia/model.py` modified +44/-0
- Risk and verification: The diff ships test coverage in `tests/kernels/test_mhc_jit_warmup.py`, `tests/kernels/test_mhc_kernels.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56599 - [CI] Update DeepSeek V4.1 MegaMoE routing test

- Link: https://github.com/vllm-project/vllm/pull/56599
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`; associated commits `1ee4be4dbc57`
- Diff scope read: GitHub Pull Request files API returned 1 files, +3/-6, 30 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[CI] Update DeepSeek V4.1 MegaMoE routing test"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v4_mega_moe.py`; technical summary: Covers "[CI] Update DeepSeek V4.1 MegaMoE routing test"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +3/-6 (9 lines); hunks: -18,10 +18,7; -78,7 +75,7 @@ def test_deepseek_v41_moe_routes_without_hash_table(; symbols: test_deepseek_v41_moe_routes_without_hash_table, touching `test_deepseek_v41_moe_routes_without_hash_table`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +3/-6 (9 lines); hunks: -18,10 +18,7; -78,7 +75,7 @@ def test_deepseek_v41_moe_routes_without_hash_table(; symbols: test_deepseek_v41_moe_routes_without_hash_table
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -18,10 +18,7 @@
-from vllm.models.deepseek_v4_1.common.mm_preprocess import (
-    IMAGE_PAD_ID,
-    IMAGE_SENTINEL_BASE_ID,
-)
+from vllm.models.deepseek_v4_1.common.mm_preprocess import IMAGE_SENTINEL_BASE_ID
@@ -78,7 +75,7 @@ def test_deepseek_v41_moe_routes_without_hash_table(
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +3/-6
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_mega_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56562 - [Perf] Fuse DSV4.1 input metadata preparation with Triton

- Link: https://github.com/vllm-project/vllm/pull/56562
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; associated commits `13e221f83084`
- Diff scope read: GitHub Pull Request files API returned 4 files, +274/-63, 383 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Perf] Fuse DSV4.1 input metadata preparation with Triton"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; technical summary: Covers "[Perf] Fuse DSV4.1 input metadata preparation with Triton"; the main implementation surface is `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +105/-0 (105 lines); hunks: -32,6 +32,111; symbols: test_fused_indexer_decode_metadata, test_device_token_request_mapping, test_indexer_shares_uncompressed_block_size_with_deepseek_v4_mla, touching `test_fused_indexer_decode_metadata, test_device_token_request_mapping, test_indexer_shares_uncompressed_block_size_with_deepseek_v4_mla`.
- Code diff details:
  - `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +105/-0 (105 lines); hunks: -32,6 +32,111; symbols: test_fused_indexer_decode_metadata, test_device_token_request_mapping, test_indexer_shares_uncompressed_block_size_with_deepseek_v4_mla
- Key code excerpts:

```diff
diff -- tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py
@@ -32,6 +32,111 @@
+@pytest.mark.skipif(not torch.cuda.is_available(), reason="requires CUDA")
+@pytest.mark.parametrize("query_lens", [[1], [6] * 16, [0, 2, 6, 0, 4], [0, 0, 0]])
+@pytest.mark.parametrize("padding", [0, 17])
+def test_fused_indexer_decode_metadata(query_lens, padding):
+    """Flatten device query boundaries and clear graph padding on every replay."""
+    from vllm.v1.attention.ops.metadata import _indexer_decode_metadata_kernel
```

- Reviewed files:
  - tests: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +105/-0
- Risk and verification: The diff ships test coverage in `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56554 - [DSV4.1] Remove compressor-aware image sentinel token padding

- Link: https://github.com/vllm-project/vllm/pull/56554
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/transformers_utils/configs/deepseek_v41.py`; associated commits `30118ba27d1d`
- Diff scope read: GitHub Pull Request files API returned 4 files, +10/-132, 245 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSV4.1] Remove compressor-aware image sentinel token padding"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/transformers_utils/configs/deepseek_v41.py`; technical summary: Covers "[DSV4.1] Remove compressor-aware image sentinel token padding"; the main implementation surface is `vllm/transformers_utils/configs/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/transformers_utils/configs/deepseek_v41.py` modified +0/-6 (6 lines); hunks: -68,9 +68,3 @@ def __init__(; symbols: __init__, touching `__init__`.
- Code diff details:
  - `vllm/transformers_utils/configs/deepseek_v41.py` modified +0/-6 (6 lines); hunks: -68,9 +68,3 @@ def __init__(; symbols: __init__
- Key code excerpts:

```diff
diff -- vllm/transformers_utils/configs/deepseek_v41.py
@@ -68,9 +68,3 @@ def __init__(
-        # The visibility span covers the image block [IMAGE_START,
-        # IMAGE_END]; the mm placeholder additionally carries a leading
-        # compressor-alignment pad of ``COMPRESS_PAD_TO - 1 - offset %
-        # COMPRESS_PAD_TO`` tokens (see common/mm_preprocess.py), with
-        # COMPRESS_PAD_TO = 2 for v4.1's ratio-2 compressors.
-        self.mm_prefix_span_leading_pad_modulus = 2 if vision_n_layers > 0 else 0
```

- Reviewed files:
  - runtime: `vllm/transformers_utils/configs/deepseek_v41.py` modified +0/-6
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4_1/amd/vl_model.py`, `vllm/models/deepseek_v4_1/common/mm_preprocess.py`, `vllm/models/deepseek_v4_1/nvidia/vl_model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #53566 - [5/N][warmup][DSv4] Migrate NVIDIA CuTeDSL attention kernels

- Link: https://github.com/vllm-project/vllm/pull/53566
- Status/date: merged / 2026-09-12
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` and 12 files; associated commits `120ec4ebd280`
- Diff scope read: GitHub Pull Request files API returned 28 files, +3108/-2535, 2685 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[5/N][warmup][DSv4] Migrate NVIDIA CuTeDSL attention kernels"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`; technical summary: Covers "[5/N][warmup][DSv4] Migrate NVIDIA CuTeDSL attention kernels"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py`, `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py` modified +1945/-1606 (3551 lines); `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` modified +591/-510 (1101 lines); hunks: -1,6 +1,9; -14,601 +17,679; symbols: fused_indexer_q_rope_quant_mxfp4_cutedsl, fused_indexer_q_rope_quant_fp8_cutedsl, _load_q_and_rope, IndexerQRopeQuantKernel, touching `fused_indexer_q_rope_quant_mxfp4_cutedsl, fused_indexer_q_rope_quant_fp8_cutedsl, _load_q_and_rope`; `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +346/-279 (625 lines); hunks: -1,7 +1,8; -12,302 +13,340; symbols: dequantize_and_gather_k_cache_cutedsl, DequantGatherKCacheKernel, __init__, __call__, touching `dequantize_and_gather_k_cache_cutedsl, DequantGatherKCacheKernel, __init__`; `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +22/-22 (44 lines); hunks: -6,11 +6,11; -598,19 +598,19 @@ def fused_indexer_q_rope_quant(; symbols: fused_indexer_q_rope_quant, touching `fused_indexer_q_rope_quant`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py` modified +1945/-1606 (3551 lines)
  - `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` modified +591/-510 (1101 lines); hunks: -1,6 +1,9; -14,601 +17,679; symbols: fused_indexer_q_rope_quant_mxfp4_cutedsl, fused_indexer_q_rope_quant_fp8_cutedsl, _load_q_and_rope, IndexerQRopeQuantKernel
  - `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +346/-279 (625 lines); hunks: -1,7 +1,8; -12,302 +13,340; symbols: dequantize_and_gather_k_cache_cutedsl, DequantGatherKCacheKernel, __init__, __call__
  - `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +22/-22 (44 lines); hunks: -6,11 +6,11; -598,19 +598,19 @@ def fused_indexer_q_rope_quant(; symbols: fused_indexer_q_rope_quant
  - `vllm/models/deepseek_v4/compressor.py` modified +31/-5 (36 lines); hunks: -197,8 +197,8 @@ class DeepseekCompressor(nn.Module):; -311,7 +311,33 @@ def __init__(; symbols: DeepseekCompressor, __init__, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py
@@ -1,6 +1,9 @@
-from functools import cache
+# ruff: noqa: E501
+from dataclasses import dataclass
+from typing import Any
@@ -14,601 +17,679 @@
+    torch_to_cute_dtype,
diff -- vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py
@@ -1,7 +1,8 @@
-from functools import cache
+from dataclasses import dataclass
+from typing import Any
@@ -12,302 +13,340 @@
+from vllm.model_executor.warmup.jit_warmup import kernel_launcher, zip_inputs
+from vllm.model_executor.warmup.jit_warmup_cutedsl_helper import (
diff -- vllm/models/deepseek_v4/common/ops/fused_indexer_q.py
@@ -6,11 +6,11 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py` modified +1945/-1606; `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` modified +591/-510; `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +346/-279; `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +22/-22; `vllm/models/deepseek_v4/compressor.py` modified +31/-5; `vllm/models/deepseek_v4/attention.py` modified +23/-3
- Risk and verification: The diff ships test coverage in `tests/model_executor/test_jit_warmup_cutedsl_launcher.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55107 - [Model][ROCm] Enable DeepSeek V4 Vision

- Link: https://github.com/vllm-project/vllm/pull/55107
- Status/date: merged / 2026-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/amd/rocm.py` and 9 files; associated commits `9dd969da096e`
- Diff scope read: GitHub Pull Request files API returned 17 files, +1055/-347, 1656 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][ROCm] Enable DeepSeek V4 Vision"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/nvidia/vl_model.py`, `vllm/models/deepseek_v4/common/vl_model.py`; technical summary: Covers "[Model][ROCm] Enable DeepSeek V4 Vision"; the main implementation surface is `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/nvidia/vl_model.py`, `vllm/models/deepseek_v4/common/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_vl_rocm.py` added +458/-0 (458 lines); hunks: -0,0 +1,458; symbols: _preshuffled_fp8_linear, test_rocm_wo_a_keeps_row_major_weights, test_rocm_gateup_shuffles_once_and_down_proj_keeps_preshuffled_backend, test_rocm_fused_qkv_quant_matches_preshuffled_gemm_scale_layout, touching `_preshuffled_fp8_linear, test_rocm_wo_a_keeps_row_major_weights, test_rocm_gateup_shuffles_once_and_down_proj_keeps_preshuffled_backend`; `vllm/models/deepseek_v4/nvidia/vl_model.py` modified +10/-322 (332 lines); hunks: -1,333 +1,21; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, __init__, touching `_make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str`; `vllm/models/deepseek_v4/common/vl_model.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, __init__, touching `_make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str`; `vllm/models/deepseek_v4/amd/rocm.py` modified +61/-7 (68 lines); hunks: -67,8 +67,13 @@ def weight_already_preshuffled(linear: torch.nn.Module) -> bool:; -116,13 +121,18 @@ def _combine_topk_swa_indices_kernel(; symbols: weight_already_preshuffled, apply_pre_quantized_block_scaled_mm, _combine_topk_swa_indices_kernel, touching `weight_already_preshuffled, apply_pre_quantized_block_scaled_mm, _combine_topk_swa_indices_kernel`.
- Code diff details:
  - `tests/models/test_deepseek_v4_vl_rocm.py` added +458/-0 (458 lines); hunks: -0,0 +1,458; symbols: _preshuffled_fp8_linear, test_rocm_wo_a_keeps_row_major_weights, test_rocm_gateup_shuffles_once_and_down_proj_keeps_preshuffled_backend, test_rocm_fused_qkv_quant_matches_preshuffled_gemm_scale_layout
  - `vllm/models/deepseek_v4/nvidia/vl_model.py` modified +10/-322 (332 lines); hunks: -1,333 +1,21; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, __init__
  - `vllm/models/deepseek_v4/common/vl_model.py` added +331/-0 (331 lines); hunks: -0,0 +1,331; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, __init__
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +61/-7 (68 lines); hunks: -67,8 +67,13 @@ def weight_already_preshuffled(linear: torch.nn.Module) -> bool:; -116,13 +121,18 @@ def _combine_topk_swa_indices_kernel(; symbols: weight_already_preshuffled, apply_pre_quantized_block_scaled_mm, _combine_topk_swa_indices_kernel
  - `vllm/models/deepseek_v4/amd/model.py` modified +23/-1 (24 lines); hunks: -79,6 +79,8; -549,6 +551,10 @@ def __init__(; symbols: __init__, forward, _make_deepseek_v4_weights_mapper
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_vl_rocm.py
@@ -0,0 +1,458 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+from types import SimpleNamespace
+import pytest
+import torch
+from torch import nn
diff -- vllm/models/deepseek_v4/nvidia/vl_model.py
@@ -1,333 +1,21 @@
-"""DeepSeek-V4 vision variant (e.g. DeepSeek-V4-Flash-Vision-Exp).
+"""Compatibility imports for the platform-neutral DeepSeek-V4 vision model."""
-Thin multimodal wrapper around the text-only ``DeepseekV4ForCausalLM``:
-- ``vision`` ViT + ``aligner`` produce per-image embeddings for the IMAGE
-  sentinel positions; four learned vectors (``image_start`` / ``image_pad`` /
-  ``image_newline`` / ``image_end``) fill the remaining sentinel positions.
diff -- vllm/models/deepseek_v4/common/vl_model.py
@@ -0,0 +1,331 @@
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_vl_rocm.py` added +458/-0
  - runtime: `vllm/models/deepseek_v4/nvidia/vl_model.py` modified +10/-322; `vllm/models/deepseek_v4/common/vl_model.py` added +331/-0; `vllm/models/deepseek_v4/amd/rocm.py` modified +61/-7; `vllm/models/deepseek_v4/amd/model.py` modified +23/-1; `vllm/models/deepseek_v4/__init__.py` modified +4/-4; `vllm/models/deepseek_v4/vl_stub.py` modified +2/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/models/test_deepseek_v4_vl_rocm.py`, `tests/models/test_initialization.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56433 - [ROCm][Bugfix] Fix AITER preshuffled FP8 block-scale kernel

- Link: https://github.com/vllm-project/vllm/pull/56433
- Status/date: merged / 2026-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `b4da4d17ae0c`, `bc0f47cd03d6`
- Diff scope read: GitHub Pull Request files API returned 5 files, +120/-36, 279 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Bugfix] Fix AITER preshuffled FP8 block-scale kernel"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][Bugfix] Fix AITER preshuffled FP8 block-scale kernel"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +54/-16 (70 lines); hunks: -61,6 +61,16 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torc...; -551,12 +561,13 @@ def _prep(linear) -> torch.Tensor | None:; symbols: _build_indptr_from_lengths, weight_already_preshuffled, apply_pre_quantized_block_scaled_mm, _prep, touching `_build_indptr_from_lengths, weight_already_preshuffled, apply_pre_quantized_block_scaled_mm`; `vllm/models/deepseek_v4/amd/model.py` modified +11/-6 (17 lines); hunks: -71,7 +71,10; -147,11 +150,13 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward, touching `prepare_gateup_preshuffle, forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +54/-16 (70 lines); hunks: -61,6 +61,16 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torc...; -551,12 +561,13 @@ def _prep(linear) -> torch.Tensor | None:; symbols: _build_indptr_from_lengths, weight_already_preshuffled, apply_pre_quantized_block_scaled_mm, _prep
  - `vllm/models/deepseek_v4/amd/model.py` modified +11/-6 (17 lines); hunks: -71,7 +71,10; -147,11 +150,13 @@ def prepare_gateup_preshuffle(self) -> None:; symbols: prepare_gateup_preshuffle, forward
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -61,6 +61,16 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torch.Tensor:
+def weight_already_preshuffled(linear: torch.nn.Module) -> bool:
+    """True when the linear's kernel already B-preshuffled ``weight``.
+    The hand-shuffles below (fused_wqa_wkv, wo_b, gate_up_proj) must be skipped
+    for those, since shuffle_weight is a permutation rather than an involution.
+    """
+    kernel = getattr(getattr(linear, "quant_method", None), "fp8_linear", None)
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -71,7 +71,10 @@
-from vllm.models.deepseek_v4.amd.rocm import DeepseekV4ROCMAiterMLAAttention
+from vllm.models.deepseek_v4.amd.rocm import (
+    DeepseekV4ROCMAiterMLAAttention,
+    weight_already_preshuffled,
+)
@@ -147,11 +150,13 @@ def prepare_gateup_preshuffle(self) -> None:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +54/-16; `vllm/models/deepseek_v4/amd/model.py` modified +11/-6
- Risk and verification: Runtime changes concentrate in `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/linear.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #56214 - [Model] Support DeepSeek-V4.1-Flash

- Link: https://github.com/vllm-project/vllm/pull/56214
- Status/date: merged / 2026-09-11
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; associated commits `e77daef89e18`
- Diff scope read: GitHub Pull Request files API returned 49 files, +3996/-138, 4994 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Support DeepSeek-V4.1-Flash"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_mega_moe.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; technical summary: Covers "[Model] Support DeepSeek-V4.1-Flash"; the main implementation surface is `tests/models/test_deepseek_v4_mega_moe.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_mega_moe.py` modified +211/-4 (215 lines); hunks: -18,14 +18,147; -169,15 +302,79 @@ def test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert...; symbols: v41_moe_config, test_deepseek_v41_moe_routes_without_hash_table, check_routing, test_deepseek_v41_fused_moe_uses_draft_counts_or_main_defaults, touching `v41_moe_config, test_deepseek_v41_moe_routes_without_hash_table, check_routing`; `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +43/-1 (44 lines); hunks: -7,19 +7,61; symbols: test_indexer_shares_uncompressed_block_size_with_deepseek_v4_mla, test_indexer_preserves_deepseek_v41_mla_block_size, test_indexer_warmup_normalizes_zero_compress_ratios, touching `test_indexer_shares_uncompressed_block_size_with_deepseek_v4_mla, test_indexer_preserves_deepseek_v41_mla_block_size, test_indexer_warmup_normalizes_zero_compress_ratios`.
- Code diff details:
  - `tests/models/test_deepseek_v4_mega_moe.py` modified +211/-4 (215 lines); hunks: -18,14 +18,147; -169,15 +302,79 @@ def test_deepseek_v4_mega_moe_weight_loader_uses_ep_expert...; symbols: v41_moe_config, test_deepseek_v41_moe_routes_without_hash_table, check_routing, test_deepseek_v41_fused_moe_uses_draft_counts_or_main_defaults
  - `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +43/-1 (44 lines); hunks: -7,19 +7,61; symbols: test_indexer_shares_uncompressed_block_size_with_deepseek_v4_mla, test_indexer_preserves_deepseek_v41_mla_block_size, test_indexer_warmup_normalizes_zero_compress_ratios
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_mega_moe.py
@@ -18,14 +18,147 @@
+from vllm.models.deepseek_v4_1.common.mm_preprocess import (
+    IMAGE_PAD_ID,
+    IMAGE_SENTINEL_BASE_ID,
+)
+from vllm.models.deepseek_v4_1.nvidia.model import DeepseekV4MoE as DeepseekV41MoE
+from vllm.transformers_utils.configs.deepseek_v41 import DeepseekV41Config
diff -- tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py
@@ -7,19 +7,61 @@
+from vllm.models.deepseek_v4.sparse_mla import DeepseekV4SparseMLABackend
+from vllm.models.deepseek_v4_1.sparse_mla import (
+    DeepseekV4SparseMLABackend as DeepseekV41SparseMLABackend,
+)
+    DeepseekV4IndexerBackend,
+    DeepseekV41IndexerBackend,
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +211/-4; `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +43/-1
- Risk and verification: The diff ships test coverage in `tests/fusion/test_quant_activation_contract.py`, `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/kernels/quantization/test_rocm_mxfp8_linear.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #51692 - [ROCm][Perf] Add bpreshuffled blockscaled fp8 GEMM

- Link: https://github.com/vllm-project/vllm/pull/51692
- Status/date: merged / 2026-09-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `bc0f47cd03d6`
- Diff scope read: GitHub Pull Request files API returned 3 files, +159/-5, 217 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Add bpreshuffled blockscaled fp8 GEMM"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/_aiter_ops.py`; technical summary: Covers "[ROCm][Perf] Add bpreshuffled blockscaled fp8 GEMM"; the main implementation surface is `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/_aiter_ops.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/model_executor/kernels/linear/scaled_mm/aiter.py` modified +128/-0 (128 lines); hunks: -457,3 +457,131 @@ def apply_block_scaled_mm(; symbols: apply_block_scaled_mm, AiterPreshuffledFp8BlockScaledMMKernel, is_supported, can_implement, touching `apply_block_scaled_mm, AiterPreshuffledFp8BlockScaledMMKernel, is_supported`; `vllm/model_executor/kernels/linear/__init__.py` modified +4/-0 (4 lines); hunks: -178,6 +178,7; -316,6 +317,7 @@ def _get_linear_backend() -> str:; symbols: _get_linear_backend, _resolve_backend_kernels, register_linear_kernel, touching `_get_linear_backend, _resolve_backend_kernels, register_linear_kernel`; `vllm/_aiter_ops.py` modified +27/-5 (32 lines); hunks: -175,18 +175,26 @@ def is_aiter_found_and_supported_on_rdna4() -> bool:; -3200,6 +3208,20 @@ def is_per_token_w8a8_gemm_tuned(N: int, K: int, q_dtype_...; symbols: is_aiter_found_and_supported_on_rdna4, _load_gemm_tuned_configs, _check_kernel_tuned, is_per_token_w8a8_gemm_tuned, touching `is_aiter_found_and_supported_on_rdna4, _load_gemm_tuned_configs, _check_kernel_tuned`.
- Code diff details:
  - `vllm/model_executor/kernels/linear/scaled_mm/aiter.py` modified +128/-0 (128 lines); hunks: -457,3 +457,131 @@ def apply_block_scaled_mm(; symbols: apply_block_scaled_mm, AiterPreshuffledFp8BlockScaledMMKernel, is_supported, can_implement
  - `vllm/model_executor/kernels/linear/__init__.py` modified +4/-0 (4 lines); hunks: -178,6 +178,7; -316,6 +317,7 @@ def _get_linear_backend() -> str:; symbols: _get_linear_backend, _resolve_backend_kernels, register_linear_kernel
  - `vllm/_aiter_ops.py` modified +27/-5 (32 lines); hunks: -175,18 +175,26 @@ def is_aiter_found_and_supported_on_rdna4() -> bool:; -3200,6 +3208,20 @@ def is_per_token_w8a8_gemm_tuned(N: int, K: int, q_dtype_...; symbols: is_aiter_found_and_supported_on_rdna4, _load_gemm_tuned_configs, _check_kernel_tuned, is_per_token_w8a8_gemm_tuned
- Key code excerpts:

```diff
diff -- vllm/model_executor/kernels/linear/scaled_mm/aiter.py
@@ -457,3 +457,131 @@ def apply_block_scaled_mm(
+class AiterPreshuffledFp8BlockScaledMMKernel(Fp8BlockScaledMMLinearKernel):
+    """Aiter FP8 block-scaled GEMM using a pre-shuffled (bpreshuffle) weight."""
+    @classmethod
+    def is_supported(
+        cls, compute_capability: int | None = None
+    ) -> tuple[bool, str | None]:
diff -- vllm/model_executor/kernels/linear/__init__.py
@@ -178,6 +178,7 @@
+    AiterPreshuffledFp8BlockScaledMMKernel,
@@ -316,6 +317,7 @@ def _get_linear_backend() -> str:
+        AiterPreshuffledFp8BlockScaledMMKernel,
@@ -456,6 +458,7 @@ def _resolve_backend_kernels(
+        AiterPreshuffledFp8BlockScaledMMKernel,
@@ -1210,6 +1213,7 @@ def register_linear_kernel(
diff -- vllm/_aiter_ops.py
@@ -175,18 +175,26 @@ def is_aiter_found_and_supported_on_rdna4() -> bool:
```

- Reviewed files:
  - runtime: `vllm/model_executor/kernels/linear/scaled_mm/aiter.py` modified +128/-0; `vllm/model_executor/kernels/linear/__init__.py` modified +4/-0; `vllm/_aiter_ops.py` modified +27/-5
- Risk and verification: Runtime changes concentrate in `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #56228 - [Model] DeepSeek-V4.1-Flash Model Definitions

- Link: https://github.com/vllm-project/vllm/pull/56228
- Status/date: merged / 2026-09-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`, `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py` and 6 files; associated commits `9b959b86577c`
- Diff scope read: GitHub Pull Request files API returned 47 files, +12902/-196, 14210 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] DeepSeek-V4.1-Flash Model Definitions"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4_1/nvidia/model.py`, `vllm/models/deepseek_v4_1/amd/model.py`, `vllm/models/deepseek_v4_1/amd/vl_model.py`; technical summary: Covers "[Model] DeepSeek-V4.1-Flash Model Definitions"; the main implementation surface is `vllm/models/deepseek_v4_1/nvidia/model.py`, `vllm/models/deepseek_v4_1/amd/model.py`, `vllm/models/deepseek_v4_1/amd/vl_model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4_1/nvidia/model.py` added +1111/-0 (1111 lines); hunks: -0,0 +1,1111; symbols: DeepseekV4MoE, __init__, _select_dsv4_attn_cls, for, touching `DeepseekV4MoE, __init__, _select_dsv4_attn_cls`; `vllm/models/deepseek_v4_1/amd/model.py` added +1086/-0 (1086 lines); hunks: -0,0 +1,1086; symbols: DeepseekV4MoE, __init__, _select_dsv4_attn_cls, _use_sequence_parallel, touching `DeepseekV4MoE, __init__, _select_dsv4_attn_cls`; `vllm/models/deepseek_v4_1/amd/vl_model.py` added +357/-0 (357 lines); hunks: -0,0 +1,357; symbols: DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, get_placeholder_str, touching `DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM`; `vllm/models/deepseek_v4_1/nvidia/vl_model.py` added +357/-0 (357 lines); hunks: -0,0 +1,357; symbols: DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, get_placeholder_str, touching `DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM`.
- Code diff details:
  - `vllm/models/deepseek_v4_1/nvidia/model.py` added +1111/-0 (1111 lines); hunks: -0,0 +1,1111; symbols: DeepseekV4MoE, __init__, _select_dsv4_attn_cls, for
  - `vllm/models/deepseek_v4_1/amd/model.py` added +1086/-0 (1086 lines); hunks: -0,0 +1,1086; symbols: DeepseekV4MoE, __init__, _select_dsv4_attn_cls, _use_sequence_parallel
  - `vllm/models/deepseek_v4_1/amd/vl_model.py` added +357/-0 (357 lines); hunks: -0,0 +1,357; symbols: DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, get_placeholder_str
  - `vllm/models/deepseek_v4_1/nvidia/vl_model.py` added +357/-0 (357 lines); hunks: -0,0 +1,357; symbols: DeepseekV4VLImagePixelInputs, _make_deepseek_v4_vl_weights_mapper, DeepseekV41ForCausalLM, get_placeholder_str
  - `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +105/-70 (175 lines); hunks: -32,37 +32,39 @@ class CompileKey:; -74,8 +76,8 @@ def kernel(; symbols: CompileKey, varies, kernel
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4_1/nvidia/model.py
@@ -0,0 +1,1111 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import typing
+from collections.abc import Callable, Iterable
+from itertools import islice
+import regex as re
diff -- vllm/models/deepseek_v4_1/amd/model.py
@@ -0,0 +1,1086 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import typing
+from collections.abc import Callable, Iterable
+from itertools import islice
+import regex as re
diff -- vllm/models/deepseek_v4_1/amd/vl_model.py
@@ -0,0 +1,357 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4_1/nvidia/model.py` added +1111/-0; `vllm/models/deepseek_v4_1/amd/model.py` added +1086/-0; `vllm/models/deepseek_v4_1/amd/vl_model.py` added +357/-0; `vllm/models/deepseek_v4_1/nvidia/vl_model.py` added +357/-0; `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +105/-70; `vllm/models/deepseek_v4/common/vision.py` modified +93/-2
  - tests: `tests/models/test_deepseek_v4_mega_moe.py` modified +47/-11
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_mega_moe.py`, `tests/parser/engine/trace_builder.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56208 - [Model][Frontend] Support DeepSeek-V4.1-Flash in Rust and Python frontends

- Link: https://github.com/vllm-project/vllm/pull/56208
- Status/date: merged / 2026-09-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/parser/engine/test_deepseek_v41.py`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/parser/deepseek_v4.py` and 10 files; associated commits `b47b01cf3383`
- Diff scope read: GitHub Pull Request files API returned 52 files, +2986/-113, 3929 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][Frontend] Support DeepSeek-V4.1-Flash in Rust and Python frontends"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/tokenizers/deepseek_v41_encoding.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`; technical summary: Covers "[Model][Frontend] Support DeepSeek-V4.1-Flash in Rust and Python frontends"; the main implementation surface is `vllm/tokenizers/deepseek_v41_encoding.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tokenizers/deepseek_v41_encoding.py` added +577/-0 (577 lines); hunks: -0,0 +1,577; symbols: to_json, tools_from_openai_format, tool_calls_from_openai_format, merge_tool_messages, touching `to_json, tools_from_openai_format, tool_calls_from_openai_format`; `tests/tokenizers_/test_deepseek_v41.py` added +169/-0 (169 lines); hunks: -0,0 +1,169; symbols: render, test_reference_encoder_fixtures, test_numeric_reasoning_effort, test_invalid_effort_is_a_request_error, touching `render, test_reference_encoder_fixtures, test_numeric_reasoning_effort`; `vllm/tokenizers/deepseek_v41.py` added +121/-0 (121 lines); hunks: -0,0 +1,121; symbols: _normalize_messages, get_deepseek_v41_tokenizer, _DeepseekV41Tokenizer, apply_chat_template, touching `_normalize_messages, get_deepseek_v41_tokenizer, _DeepseekV41Tokenizer`; `vllm/transformers_utils/configs/deepseek_v41.py` added +76/-0 (76 lines); hunks: -0,0 +1,76; symbols: DeepseekV41Config, __init__, touching `DeepseekV41Config, __init__`.
- Code diff details:
  - `vllm/tokenizers/deepseek_v41_encoding.py` added +577/-0 (577 lines); hunks: -0,0 +1,577; symbols: to_json, tools_from_openai_format, tool_calls_from_openai_format, merge_tool_messages
  - `tests/tokenizers_/test_deepseek_v41.py` added +169/-0 (169 lines); hunks: -0,0 +1,169; symbols: render, test_reference_encoder_fixtures, test_numeric_reasoning_effort, test_invalid_effort_is_a_request_error
  - `vllm/tokenizers/deepseek_v41.py` added +121/-0 (121 lines); hunks: -0,0 +1,121; symbols: _normalize_messages, get_deepseek_v41_tokenizer, _DeepseekV41Tokenizer, apply_chat_template
  - `vllm/transformers_utils/configs/deepseek_v41.py` added +76/-0 (76 lines); hunks: -0,0 +1,76; symbols: DeepseekV41Config, __init__
  - `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt` added +38/-0 (38 lines); hunks: -0,0 +1,38
- Key code excerpts:

```diff
diff -- vllm/tokenizers/deepseek_v41_encoding.py
@@ -0,0 +1,577 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+# ruff: noqa
+"""Text encoding adapted from the DeepSeek V4.1 reference encoder.
+Message normalization and serving controls live in deepseek_v41.py.
+"""
diff -- tests/tokenizers_/test_deepseek_v41.py
@@ -0,0 +1,169 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import copy
+import json
+from pathlib import Path
+import pytest
diff -- vllm/tokenizers/deepseek_v41.py
@@ -0,0 +1,121 @@
```

- Reviewed files:
  - runtime: `vllm/tokenizers/deepseek_v41_encoding.py` added +577/-0; `vllm/tokenizers/deepseek_v41.py` added +121/-0; `vllm/transformers_utils/configs/deepseek_v41.py` added +76/-0; `vllm/reasoning/deepseek_v41_engine_reasoning_parser.py` added +6/-0
  - tests: `tests/tokenizers_/test_deepseek_v41.py` added +169/-0; `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt` added +38/-0; `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt` added +3/-0; `tests/parser/engine/test_deepseek_v41.py` added +146/-0
- Risk and verification: The diff ships test coverage in `rust/src/chat/tests/roundtrip.rs`, `tests/parser/engine/test_deepseek_v41.py`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_1.txt`, `tests/tokenizers_/fixtures/deepseek_v41/test_output_2.txt`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56215 - [Kernel] Optional Q-norm in fused DSv4 MLA epilogue; group_size=32 for packed FP8 quant

- Link: https://github.com/vllm-project/vllm/pull/56215
- Status/date: merged / 2026-09-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`; associated commits `be1cb9834b3d`
- Diff scope read: GitHub Pull Request files API returned 6 files, +267/-148, 857 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Kernel] Optional Q-norm in fused DSv4 MLA epilogue; group_size=32 for packed FP8 quant"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`; technical summary: Covers "[Kernel] Optional Q-norm in fused DSv4 MLA epilogue; group_size=32 for packed FP8 quant"; the main implementation surface is `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +99/-13 (112 lines); hunks: -4,11 +4,11; -146,9 +146,18 @@ def _full_cache_bf16_op_available() -> bool:; symbols: _full_cache_bf16_op_available, _call_fused, _as_stored_fp8, test_q_path_matches_reference, touching `_full_cache_bf16_op_available, _call_fused, _as_stored_fp8`.
- Code diff details:
  - `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +99/-13 (112 lines); hunks: -4,11 +4,11; -146,9 +146,18 @@ def _full_cache_bf16_op_available() -> bool:; symbols: _full_cache_bf16_op_available, _call_fused, _as_stored_fp8, test_q_path_matches_reference
- Key code excerpts:

```diff
diff -- tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py
@@ -4,11 +4,11 @@
-    - Q side:  per-head RMSNorm (no weight) + GPT-J RoPE on last 64 dims
+    - Q side:  optional per-head RMSNorm + GPT-J RoPE on last 64 dims
-  - PyTorch reference for RMSNorm + GPT-J RoPE on Q
+  - PyTorch references for RoPE with and without RMSNorm on Q
@@ -146,9 +146,18 @@ def _full_cache_bf16_op_available() -> bool:
-    q_in, q_head_padded, kv, k_cache, slot_mapping, positions, cos_sin_cache, eps, bs
```

- Reviewed files:
  - tests: `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` modified +99/-13
- Risk and verification: The diff ships test coverage in `tests/kernels/quantization/test_per_token_group_quant.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55355 - [Model] Add DeepSeek-V4 CPU backend

- Link: https://github.com/vllm-project/vllm/pull/55355
- Status/date: merged / 2026-09-10
- Trace source: `git log --name-only -- <model-files>` found it through `tests/kernels/test_deepseek_v4_cpu_kernels.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/cpu/__init__.py`, `vllm/models/deepseek_v4/cpu/cpu_compressor.py` and 11 files; associated commits `c3ccc0e957fb`
- Diff scope read: GitHub Pull Request files API returned 47 files, +9564/-627, 11219 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Add DeepSeek-V4 CPU backend"; model line: DeepSeek V4; category: model support/runtime entry; main diff: `vllm/models/deepseek_v4/cpu/model.py`, `vllm/models/deepseek_v4/cpu/cpu_sparse.py`, `vllm/models/deepseek_v4/cpu/cpu_mla.py`; technical summary: Covers "[Model] Add DeepSeek-V4 CPU backend"; the main implementation surface is `vllm/models/deepseek_v4/cpu/model.py`, `vllm/models/deepseek_v4/cpu/cpu_sparse.py`, `vllm/models/deepseek_v4/cpu/cpu_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/cpu/model.py` added +922/-0 (922 lines); hunks: -0,0 +1,922; symbols: DeepseekV4MLP, __init__, forward, DeepseekV4MoE, touching `DeepseekV4MLP, __init__, forward`; `vllm/models/deepseek_v4/cpu/cpu_sparse.py` added +648/-0 (648 lines); hunks: -0,0 +1,648; symbols: _deepseek_v4_cpu_prepare_and_attn, _deepseek_v4_cpu_prepare_and_attn_fake, _dequant_linear_weight, _fused_indexer_q_rope_quant_cpu, touching `_deepseek_v4_cpu_prepare_and_attn, _deepseek_v4_cpu_prepare_and_attn_fake, _dequant_linear_weight`; `vllm/models/deepseek_v4/cpu/cpu_mla.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: DeepseekV4CPUFlashMLAMetadataBuilder, _build_c128a_metadata, DeepseekV4CPUSparseBackend, get_name, touching `DeepseekV4CPUFlashMLAMetadataBuilder, _build_c128a_metadata, DeepseekV4CPUSparseBackend`; `vllm/models/deepseek_v4/cpu/cpu_compressor.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: DeepseekV4CPUCompressor, cache_norm_weight_fp32, forward, touching `DeepseekV4CPUCompressor, cache_norm_weight_fp32, forward`.
- Code diff details:
  - `vllm/models/deepseek_v4/cpu/model.py` added +922/-0 (922 lines); hunks: -0,0 +1,922; symbols: DeepseekV4MLP, __init__, forward, DeepseekV4MoE
  - `vllm/models/deepseek_v4/cpu/cpu_sparse.py` added +648/-0 (648 lines); hunks: -0,0 +1,648; symbols: _deepseek_v4_cpu_prepare_and_attn, _deepseek_v4_cpu_prepare_and_attn_fake, _dequant_linear_weight, _fused_indexer_q_rope_quant_cpu
  - `vllm/models/deepseek_v4/cpu/cpu_mla.py` added +126/-0 (126 lines); hunks: -0,0 +1,126; symbols: DeepseekV4CPUFlashMLAMetadataBuilder, _build_c128a_metadata, DeepseekV4CPUSparseBackend, get_name
  - `vllm/models/deepseek_v4/cpu/cpu_compressor.py` added +112/-0 (112 lines); hunks: -0,0 +1,112; symbols: DeepseekV4CPUCompressor, cache_norm_weight_fp32, forward
  - `vllm/models/deepseek_v4/cpu/cpu_utils.py` added +34/-0 (34 lines); hunks: -0,0 +1,34; symbols: map_local_to_global_slots_cpu
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/cpu/model.py
@@ -0,0 +1,922 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import typing
+from collections.abc import Callable, Iterable
+from itertools import islice
+import regex as re
diff -- vllm/models/deepseek_v4/cpu/cpu_sparse.py
@@ -0,0 +1,648 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""CPU DeepSeek-V4 attention subclass.
+``forward_mqa`` resolves SWA/compressed top-k indices to paged-cache slot
+ids and calls the fused ``flash_mla_with_kvcache_cpu`` kernel. ``_o_proj``
+stays eager -- not on the attention hot path.
diff -- vllm/models/deepseek_v4/cpu/cpu_mla.py
@@ -0,0 +1,126 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/cpu/model.py` added +922/-0; `vllm/models/deepseek_v4/cpu/cpu_sparse.py` added +648/-0; `vllm/models/deepseek_v4/cpu/cpu_mla.py` added +126/-0; `vllm/models/deepseek_v4/cpu/cpu_compressor.py` added +112/-0; `vllm/models/deepseek_v4/cpu/cpu_utils.py` added +34/-0; `vllm/models/deepseek_v4/cpu/mtp.py` added +19/-0
- Risk and verification: The diff ships test coverage in `.buildkite/hardware_tests/cpu.yaml`, `tests/kernels/moe/test_cpu_fused_moe.py`, `tests/kernels/moe/test_cpu_quant_fused_moe.py`, `tests/kernels/moe/test_zen_cpu_fused_moe.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #56035 - [Bugfix][ROCm][DSv4] Skip launch_pdl=True JIT warmup when PDL is unsupported

- Link: https://github.com/vllm-project/vllm/pull/56035
- Status/date: merged / 2026-09-09
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`; associated commits `62f3bf58a504`
- Diff scope read: GitHub Pull Request files API returned 2 files, +2/-2, 18 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][ROCm][DSv4] Skip launch_pdl=True JIT warmup when PDL is unsupported"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`; technical summary: Covers "[Bugfix][ROCm][DSv4] Skip launch_pdl=True JIT warmup when PDL is unsupported"; the main implementation surface is `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +1/-1 (2 lines); hunks: -249,7 +249,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; symbols: get_warmup_keys, warmup_inputs, touching `get_warmup_keys, warmup_inputs`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +1/-1 (2 lines); hunks: -249,7 +249,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileK...; symbols: get_warmup_keys, warmup_inputs
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py
@@ -249,7 +249,7 @@ def get_warmup_keys(self, vllm_config: Any) -> list[CompileKey]:
-            launch_pdl=(False, True),
+            launch_pdl=current_platform.is_arch_support_pdl(),
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +1/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/common/ops/fused_qk_rmsnorm.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #50176 - [4/N][warmup][DSv4] Migrate common attention kernels

- Link: https://github.com/vllm-project/vllm/pull/50176
- Status/date: merged / 2026-09-08
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/__init__.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py` and 13 files; associated commits `6ddbab03defe`
- Diff scope read: GitHub Pull Request files API returned 19 files, +2978/-1272, 4923 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[4/N][warmup][DSv4] Migrate common attention kernels"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm.py`; technical summary: Covers "[4/N][warmup][DSv4] Migrate common attention kernels"; the main implementation surface is `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +903/-454 (1357 lines); hunks: -22,10 +22,17; -225,166 +232,268 @@ def quantize_and_insert_k_cache(; symbols: quantize_and_insert_k_cache, _dequantize_and_gather_k_kernel, DequantizeAndGatherKCacheKernel, CompileKey, touching `quantize_and_insert_k_cache, _dequantize_and_gather_k_kernel, DequantizeAndGatherKCacheKernel`; `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +464/-245 (709 lines); hunks: -1,8 +1,17; -67,229 +76,459 @@ def _quantize_mxfp4_pair(x_lo, x_hi):; symbols: _quantize_mxfp4_pair, _fused_indexer_q_rope_quant_kernel, FusedIndexerQRopeQuantTritonKernel, CompileKey, touching `_quantize_mxfp4_pair, _fused_indexer_q_rope_quant_kernel, FusedIndexerQRopeQuantTritonKernel`; `vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm.py` modified +286/-149 (435 lines); hunks: -17,9 +17,19; -40,164 +50,291 @@ def _rmsnorm_row(; symbols: _rmsnorm_row, _fused_mtp_input_rmsnorm_kernel, FusedMTPInputRMSNormKernel, CompileKey, touching `_rmsnorm_row, _fused_mtp_input_rmsnorm_kernel, FusedMTPInputRMSNormKernel`; `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +304/-129 (433 lines); hunks: -7,145 +7,327; -256,33 +438,23 @@ def _fused_inv_rope_fp8_quant_kernel_impl(; symbols: _fused_inv_rope_fp8_quant_per_head, FusedInvRopeFP8QuantKernel, CompileKey, varies, touching `_fused_inv_rope_fp8_quant_per_head, FusedInvRopeFP8QuantKernel, CompileKey`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +903/-454 (1357 lines); hunks: -22,10 +22,17; -225,166 +232,268 @@ def quantize_and_insert_k_cache(; symbols: quantize_and_insert_k_cache, _dequantize_and_gather_k_kernel, DequantizeAndGatherKCacheKernel, CompileKey
  - `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +464/-245 (709 lines); hunks: -1,8 +1,17; -67,229 +76,459 @@ def _quantize_mxfp4_pair(x_lo, x_hi):; symbols: _quantize_mxfp4_pair, _fused_indexer_q_rope_quant_kernel, FusedIndexerQRopeQuantTritonKernel, CompileKey
  - `vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm.py` modified +286/-149 (435 lines); hunks: -17,9 +17,19; -40,164 +50,291 @@ def _rmsnorm_row(; symbols: _rmsnorm_row, _fused_mtp_input_rmsnorm_kernel, FusedMTPInputRMSNormKernel, CompileKey
  - `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +304/-129 (433 lines); hunks: -7,145 +7,327; -256,33 +438,23 @@ def _fused_inv_rope_fp8_quant_kernel_impl(; symbols: _fused_inv_rope_fp8_quant_per_head, FusedInvRopeFP8QuantKernel, CompileKey, varies
  - `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py` modified +281/-9 (290 lines); hunks: -19,13 +19,22; -68,14 +77,32 @@ def compress_norm_rope_store_triton(; symbols: compress_norm_rope_store_triton, compress_norm_rope_store_two_stage_triton, _fused_kv_compress_norm_rope_insert_indexer_attn, _fused_kv_compress_norm_rope_insert_indexer_mxfp4_attn
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/ops/cache_utils.py
@@ -22,10 +22,17 @@
-from vllm.model_executor.warmup.jit_warmup import VllmJitKernel, zip_inputs
+from vllm.model_executor.warmup.jit_warmup import (
+    WarmupIntRange,
+    zip_inputs,
+)
+    LaunchSpec,
diff -- vllm/models/deepseek_v4/common/ops/fused_indexer_q.py
@@ -1,8 +1,17 @@
+from dataclasses import dataclass
+from typing import Any
+from vllm.model_executor.warmup.jit_warmup_triton_helper import (
+    LaunchSpec,
+    TritonWarmupTensor,
+    VllmTritonJitKernel,
diff -- vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm.py
@@ -17,9 +17,19 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +903/-454; `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` modified +464/-245; `vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm.py` modified +286/-149; `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py` modified +304/-129; `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py` modified +281/-9; `vllm/models/deepseek_v4/common/ops/save_partial_states.py` modified +184/-92
- Risk and verification: The diff ships test coverage in `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/model_executor/test_jit_warmup.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53689 - [XPU][LoRA] Support LoRA for DeepSeek V4 on XPU

- Link: https://github.com/vllm-project/vllm/pull/53689
- Status/date: merged / 2026-09-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/xpu/model.py`; associated commits `86484465153f`
- Diff scope read: GitHub Pull Request files API returned 1 files, +31/-1, 80 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[XPU][LoRA] Support LoRA for DeepSeek V4 on XPU"; model line: DeepSeek V4; category: model support/runtime entry; main diff: `vllm/models/deepseek_v4/xpu/model.py`; technical summary: Covers "[XPU][LoRA] Support LoRA for DeepSeek V4 on XPU"; the main implementation surface is `vllm/models/deepseek_v4/xpu/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/xpu/model.py` modified +31/-1 (32 lines); hunks: -46,6 +46,7; -1183,6 +1184,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, _make_deepseek_v4_weights_mapper, touching `load_weights, _make_deepseek_v4_weights_mapper`.
- Code diff details:
  - `vllm/models/deepseek_v4/xpu/model.py` modified +31/-1 (32 lines); hunks: -46,6 +46,7; -1183,6 +1184,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, _make_deepseek_v4_weights_mapper
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/xpu/model.py
@@ -46,6 +46,7 @@
+    SupportsLoRA,
@@ -1183,6 +1184,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                if name not in params_dict:
+                    head, _, leaf = name.rpartition(".")
+                    suffixed = f"{head}.base_layer.{leaf}"
+                    if suffixed in params_dict:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/xpu/model.py` modified +31/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/xpu/model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #53161 - [ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts

- Link: https://github.com/vllm-project/vllm/pull/53161
- Status/date: merged / 2026-09-07
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/model.py`; associated commits `de69e821b7c8`
- Diff scope read: GitHub Pull Request files API returned 4 files, +839/-6, 1031 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts"; the main implementation surface is `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/model.py` modified +377/-5 (382 lines); hunks: -1,7 +1,9; -20,9 +22,14; symbols: forward, _use_heterogeneous_fhmoe, _validate_heterogeneous_routes, _heterogeneous_shared_expert_enabled, touching `forward, _use_heterogeneous_fhmoe, _validate_heterogeneous_routes`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/model.py` modified +377/-5 (382 lines); hunks: -1,7 +1,9; -20,9 +22,14; symbols: forward, _use_heterogeneous_fhmoe, _validate_heterogeneous_routes, _heterogeneous_shared_expert_enabled
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -1,7 +1,9 @@
+import weakref
+from dataclasses import replace
@@ -20,9 +22,14 @@
+    FusedMoEQuantConfig,
+    RoutedExperts,
+from vllm.model_executor.layers.fused_moe.experts.rocm_aiter_moe import (
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/model.py` modified +377/-5
- Risk and verification: The diff ships test coverage in `tests/model_executor/layers/test_fused_shared_expert.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #55299 - [Bugfix][DSv4] Seed the -1 sentinel in the prefill sparse index workspace

- Link: https://github.com/vllm-project/vllm/pull/55299
- Status/date: merged / 2026-09-05
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/ops/cache_utils.py`; associated commits `7fbd44cbe0a9`
- Diff scope read: GitHub Pull Request files API returned 1 files, +1/-0, 8 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DSv4] Seed the -1 sentinel in the prefill sparse index workspace"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/common/ops/cache_utils.py`; technical summary: Covers "[Bugfix][DSv4] Seed the -1 sentinel in the prefill sparse index workspace"; the main implementation surface is `vllm/models/deepseek_v4/common/ops/cache_utils.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +1/-0 (1 lines); hunks: -561,6 +561,7 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices, touching `combine_topk_swa_indices`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +1/-0 (1 lines); hunks: -561,6 +561,7 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/ops/cache_utils.py
@@ -561,6 +561,7 @@ def combine_topk_swa_indices(
+        combined_indices.fill_(-1)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +1/-0
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/common/ops/cache_utils.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #55061 - [Performance][DSv4] Size dequant gather launch grid by rows

- Link: https://github.com/vllm-project/vllm/pull/55061
- Status/date: merged / 2026-09-04
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`; associated commits `69cf05593606`
- Diff scope read: GitHub Pull Request files API returned 1 files, +6/-1, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Performance][DSv4] Size dequant gather launch grid by rows"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`; technical summary: Covers "[Performance][DSv4] Size dequant gather launch grid by rows"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +6/-1 (7 lines); hunks: -73,7 +73,12 @@ def __call__(; symbols: __call__, touching `__call__`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +6/-1 (7 lines); hunks: -73,7 +73,12 @@ def __call__(; symbols: __call__
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py
@@ -73,7 +73,12 @@ def __call__(
-        grid = (out.shape[0], 1024, 1)
+        num_reqs = out.shape[0]
+        max_rows = out.shape[1] - offset
+        num_workers = cutlass.max(
+            1, cutlass.min(cute.ceil_div(max_rows, 4), cute.ceil_div(8192, num_reqs))
+        )
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py` modified +6/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #45091 - Fix DeepSeek V4 FlashMLA auto KV cache dtype

- Link: https://github.com/vllm-project/vllm/pull/45091
- Status/date: merged / 2026-09-03
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/attention.py`; associated commits `fc8f10792c59`
- Diff scope read: GitHub Pull Request files API returned 1 files, +9/-4, 20 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "Fix DeepSeek V4 FlashMLA auto KV cache dtype"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/attention.py`; technical summary: Covers "Fix DeepSeek V4 FlashMLA auto KV cache dtype"; the main implementation surface is `vllm/models/deepseek_v4/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/attention.py` modified +9/-4 (13 lines); hunks: -102,10 +102,15 @@ def _resolve_dsv4_kv_cache_dtype(; symbols: _resolve_dsv4_kv_cache_dtype, touching `_resolve_dsv4_kv_cache_dtype`.
- Code diff details:
  - `vllm/models/deepseek_v4/attention.py` modified +9/-4 (13 lines); hunks: -102,10 +102,15 @@ def _resolve_dsv4_kv_cache_dtype(; symbols: _resolve_dsv4_kv_cache_dtype
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/attention.py
@@ -102,10 +102,15 @@ def _resolve_dsv4_kv_cache_dtype(
-        assert kv_cache_dtype.startswith("fp8"), (
-            f"DeepseekV4 fp8_ds_mla layout only supports fp8 kv-cache, "
-            f"got {kv_cache_dtype}"
-        )
+        if kv_cache_dtype == "auto":
+            kv_cache_dtype = "fp8"
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/attention.py` modified +9/-4
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/attention.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #54566 - [New model][Multimodal] Add DeepSeek-V4-Flash-Vision-Exp support

- Link: https://github.com/vllm-project/vllm/pull/54566
- Status/date: merged / 2026-09-02
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_deepseek_v4.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/mm_preprocess.py` and 14 files; associated commits `1356635d837c`
- Diff scope read: GitHub Pull Request files API returned 37 files, +2918/-152, 4087 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[New model][Multimodal] Add DeepSeek-V4-Flash-Vision-Exp support"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/common/mm_preprocess.py`, `vllm/models/deepseek_v4/nvidia/vl_model.py`, `vllm/models/deepseek_v4/common/vision.py`; technical summary: Covers "[New model][Multimodal] Add DeepSeek-V4-Flash-Vision-Exp support"; the main implementation surface is `vllm/models/deepseek_v4/common/mm_preprocess.py`, `vllm/models/deepseek_v4/nvidia/vl_model.py`, `vllm/models/deepseek_v4/common/vision.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/mm_preprocess.py` added +512/-0 (512 lines); hunks: -0,0 +1,512; symbols: image_sentinel_mask, validate_image_sentinel_ids, grid_tokens, solve_resize_ratio, touching `image_sentinel_mask, validate_image_sentinel_ids, grid_tokens`; `vllm/models/deepseek_v4/nvidia/vl_model.py` added +333/-0 (333 lines); hunks: -0,0 +1,333; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, __init__, touching `_make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str`; `vllm/models/deepseek_v4/common/vision.py` added +232/-0 (232 lines); hunks: -0,0 +1,232; symbols: get_vision_cos_sin, apply_rotary, DeepseekV4RMSNorm, __init__, touching `get_vision_cos_sin, apply_rotary, DeepseekV4RMSNorm`; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +107/-27 (134 lines); hunks: -536,10 +536,16 @@ def combine_topk_swa_indices(; -568,6 +574,9 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices, CompileKey, kernel, touching `combine_topk_swa_indices, CompileKey, kernel`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/mm_preprocess.py` added +512/-0 (512 lines); hunks: -0,0 +1,512; symbols: image_sentinel_mask, validate_image_sentinel_ids, grid_tokens, solve_resize_ratio
  - `vllm/models/deepseek_v4/nvidia/vl_model.py` added +333/-0 (333 lines); hunks: -0,0 +1,333; symbols: _make_deepseek_v4_vl_weights_mapper, DeepseekV4ForConditionalGeneration, get_placeholder_str, __init__
  - `vllm/models/deepseek_v4/common/vision.py` added +232/-0 (232 lines); hunks: -0,0 +1,232; symbols: get_vision_cos_sin, apply_rotary, DeepseekV4RMSNorm, __init__
  - `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +107/-27 (134 lines); hunks: -536,10 +536,16 @@ def combine_topk_swa_indices(; -568,6 +574,9 @@ def combine_topk_swa_indices(; symbols: combine_topk_swa_indices, CompileKey, kernel
  - `tests/tokenizers_/test_deepseek_v4.py` modified +58/-0 (58 lines); hunks: -6,6 +6,7; -427,3 +428,60 @@ def test_deepseek_v4_encode_messages_rejects_invalid_argume...; symbols: test_deepseek_v4_encode_messages_rejects_invalid_arguments, test_deepseek_v4_image_blocks_become_placeholders, test_deepseek_v4_image_sentinel_ids_match_tokenizer, FakeTokenizer
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/mm_preprocess.py
@@ -0,0 +1,512 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Multimodal preprocessing for the DeepSeek-V4 vision variants
+(DeepSeek-V4-Flash-Vision-Exp).
+The image transform and sentinel-block construction are ported from the
+official repository's ``image_processor.py`` so that token counts bit-match
diff -- vllm/models/deepseek_v4/nvidia/vl_model.py
@@ -0,0 +1,333 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""DeepSeek-V4 vision variant (e.g. DeepSeek-V4-Flash-Vision-Exp).
+Thin multimodal wrapper around the text-only ``DeepseekV4ForCausalLM``:
+- ``vision`` ViT + ``aligner`` produce per-image embeddings for the IMAGE
+  sentinel positions; four learned vectors (``image_start`` / ``image_pad`` /
diff -- vllm/models/deepseek_v4/common/vision.py
@@ -0,0 +1,232 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/mm_preprocess.py` added +512/-0; `vllm/models/deepseek_v4/nvidia/vl_model.py` added +333/-0; `vllm/models/deepseek_v4/common/vision.py` added +232/-0; `vllm/models/deepseek_v4/common/ops/cache_utils.py` modified +107/-27; `vllm/tokenizers/deepseek_v4_encoding.py` modified +35/-3; `vllm/models/deepseek_v4/nvidia/model.py` modified +30/-1
  - tests: `tests/tokenizers_/test_deepseek_v4.py` modified +58/-0
- Risk and verification: The diff ships test coverage in `tests/config/test_model_arch_config.py`, `tests/kernels/moe/test_topk_softplus_sqrt.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/models/registry.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #54815 - [Bugfix] Fix RoPE construction for deepseek-v4 sparse SWA layers

- Link: https://github.com/vllm-project/vllm/pull/54815
- Status/date: merged / 2026-09-02
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/common/rope.py`; associated commits `1d8d7a396527`
- Diff scope read: GitHub Pull Request files API returned 1 files, +17/-1, 33 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix] Fix RoPE construction for deepseek-v4 sparse SWA layers"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/common/rope.py`; technical summary: Covers "[Bugfix] Fix RoPE construction for deepseek-v4 sparse SWA layers"; the main implementation surface is `vllm/models/deepseek_v4/common/rope.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/common/rope.py` modified +17/-1 (18 lines); hunks: -15,15 +15,31 @@ def build_deepseek_v4_rope(; symbols: build_deepseek_v4_rope, touching `build_deepseek_v4_rope`.
- Code diff details:
  - `vllm/models/deepseek_v4/common/rope.py` modified +17/-1 (18 lines); hunks: -15,15 +15,31 @@ def build_deepseek_v4_rope(; symbols: build_deepseek_v4_rope
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/common/rope.py
@@ -15,15 +15,31 @@ def build_deepseek_v4_rope(
+    # Newer checkpoints nest per-layer-type rope dicts ({"main", "compress"});
+    # older ones ship a single flat dict shared by all layer types.
+    if isinstance(rope_parameters.get("main"), dict) and isinstance(
+        rope_parameters.get("compress"), dict
+    ):
+        key = "compress" if compress_ratio > 1 else "main"
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/common/rope.py` modified +17/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/common/rope.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #52724 - [Attention] Enable adaptive verification for FLASHINFER_MLA_SPARSE_DSV4

- Link: https://github.com/vllm-project/vllm/pull/52724
- Status/date: merged / 2026-09-01
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`; associated commits `25efcfa7887c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +30/-1, 63 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Attention] Enable adaptive verification for FLASHINFER_MLA_SPARSE_DSV4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`; technical summary: Covers "[Attention] Enable adaptive verification for FLASHINFER_MLA_SPARSE_DSV4"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +30/-1 (31 lines); hunks: -21,13 +21,18; -164,11 +169,34 @@ def supports_combination(; symbols: supports_combination, get_builder_cls, DeepseekV4FlashInferSparseMLAMetadataBuilder, DeepseekSparseSWAFlashInferMetadataBuilder, touching `supports_combination, get_builder_cls, DeepseekV4FlashInferSparseMLAMetadataBuilder`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +30/-1 (31 lines); hunks: -21,13 +21,18; -164,11 +169,34 @@ def supports_combination(; symbols: supports_combination, get_builder_cls, DeepseekV4FlashInferSparseMLAMetadataBuilder, DeepseekSparseSWAFlashInferMetadataBuilder
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py
@@ -21,13 +21,18 @@
+    DeepseekV4SparseMLAMetadataBuilder,
-from vllm.v1.attention.backend import MultipleOf
+from vllm.v1.attention.backend import AttentionCGSupport, MultipleOf
+from vllm.v1.attention.backends.mla.sparse_swa import (
+    DeepseekSparseSWABackend,
+    DeepseekSparseSWAMetadataBuilder,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` modified +30/-1
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #50175 - [1/N][warmup][DSv4] Migrate generic MLA metadata and indexing kernels

- Link: https://github.com/vllm-project/vllm/pull/50175
- Status/date: merged / 2026-09-01
- Trace source: `git log --name-only -- <model-files>` found it through `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/models/deepseek_v4/attention.py`; associated commits `e16b5e518db8`
- Diff scope read: GitHub Pull Request files API returned 17 files, +1269/-625, 2446 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[1/N][warmup][DSv4] Migrate generic MLA metadata and indexing kernels"; model line: DeepSeek V4; category: docs/tests/CI; main diff: `vllm/models/deepseek_v4/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`; technical summary: Covers "[1/N][warmup][DSv4] Migrate generic MLA metadata and indexing kernels"; the main implementation surface is `vllm/models/deepseek_v4/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/attention.py` modified +51/-0 (51 lines); hunks: -353,6 +353,57 @@ def __init__(; symbols: __init__, forward, touching `__init__, forward`; `vllm/model_executor/layers/attention/mla_attention.py` modified +47/-0 (47 lines); hunks: -604,6 +604,33 @@ def __init__(; -652,6 +679,26 @@ def __init__(; symbols: __init__, bind_kv_cache, chunked_prefill_workspace_size, touching `__init__, bind_kv_cache, chunked_prefill_workspace_size`; `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +43/-2 (45 lines); hunks: -8,10 +8,16; -20,7 +26,7 @@ def test_indexer_warmup_normalizes_zero_compress_ratios():; symbols: test_indexer_warmup_normalizes_zero_compress_ratios, test_compressed_slot_mapping_warmup_includes_index_kpool, test_index_conversion_warmup_uses_physical_block_stride, touching `test_indexer_warmup_normalizes_zero_compress_ratios, test_compressed_slot_mapping_warmup_includes_index_kpool, test_index_conversion_warmup_uses_physical_block_stride`.
- Code diff details:
  - `vllm/models/deepseek_v4/attention.py` modified +51/-0 (51 lines); hunks: -353,6 +353,57 @@ def __init__(; symbols: __init__, forward
  - `vllm/model_executor/layers/attention/mla_attention.py` modified +47/-0 (47 lines); hunks: -604,6 +604,33 @@ def __init__(; -652,6 +679,26 @@ def __init__(; symbols: __init__, bind_kv_cache, chunked_prefill_workspace_size
  - `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +43/-2 (45 lines); hunks: -8,10 +8,16; -20,7 +26,7 @@ def test_indexer_warmup_normalizes_zero_compress_ratios():; symbols: test_indexer_warmup_normalizes_zero_compress_ratios, test_compressed_slot_mapping_warmup_includes_index_kpool, test_index_conversion_warmup_uses_physical_block_stride
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/attention.py
@@ -353,6 +353,57 @@ def __init__(
+        if vllm_config.kernel_config.enable_jit_warmup:
+            from vllm.v1.attention.backends.mla.sparse_swa import (
+                _COMPUTE_PREFILL_METADATA_KERNEL,
+                _COMPUTE_SWA_INDICES_AND_LENS_KERNEL,
+            )
+            _COMPUTE_PREFILL_METADATA_KERNEL.register_warmup()
diff -- vllm/model_executor/layers/attention/mla_attention.py
@@ -604,6 +604,33 @@ def __init__(
+        if vllm_config.kernel_config.enable_jit_warmup:
+            backend_name = self.attn_backend.get_name()
+            if backend_name in (
+                "FLASHMLA_SPARSE",
+                "FLASHINFER_MLA_SPARSE",
+                "FLASHINFER_MLA_SPARSE_SM120",
diff -- tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py
@@ -8,10 +8,16 @@
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/attention.py` modified +51/-0; `vllm/model_executor/layers/attention/mla_attention.py` modified +47/-0
  - tests: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` modified +43/-2
- Risk and verification: The diff ships test coverage in `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/model_executor/test_jit_warmup.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53574 - [Bugfix][SM120] DSv4: pass contiguous C128A decode topk indices on SM120

- Link: https://github.com/vllm-project/vllm/pull/53574
- Status/date: merged / 2026-08-31
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/sparse_mla.py`; associated commits `699e180df48d`
- Diff scope read: GitHub Pull Request files API returned 2 files, +31/-7, 84 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][SM120] DSv4: pass contiguous C128A decode topk indices on SM120"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/models/deepseek_v4/sparse_mla.py`; technical summary: Covers "[Bugfix][SM120] DSv4: pass contiguous C128A decode topk indices on SM120"; the main implementation surface is `vllm/models/deepseek_v4/sparse_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/sparse_mla.py` modified +9/-2 (11 lines); hunks: -9,6 +9,7; -310,7 +311,7 @@ def build_c128a_topk_metadata(; symbols: build_c128a_topk_metadata, touching `build_c128a_topk_metadata`.
- Code diff details:
  - `vllm/models/deepseek_v4/sparse_mla.py` modified +9/-2 (11 lines); hunks: -9,6 +9,7; -310,7 +311,7 @@ def build_c128a_topk_metadata(; symbols: build_c128a_topk_metadata
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/sparse_mla.py
@@ -9,6 +9,7 @@
+from vllm.platforms import current_platform
@@ -310,7 +311,7 @@ def build_c128a_topk_metadata(
-    Returns slices of the buffers.
+    Returns views of the buffers.
@@ -322,7 +323,13 @@ def build_c128a_topk_metadata(
-    global_decode = global_decode_buffer[:num_decode_tokens, :max_compressed_tokens]
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/sparse_mla.py` modified +9/-2
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_flashmla_sparse.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53540 - [ROCm][Perf] Fuse SWA q/kv RMSNorm and q FP8 group quant for DeepSeek-V4

- Link: https://github.com/vllm-project/vllm/pull/53540
- Status/date: merged / 2026-08-27
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`; associated commits `32ad1400d7fa`
- Diff scope read: GitHub Pull Request files API returned 4 files, +333/-12, 479 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][Perf] Fuse SWA q/kv RMSNorm and q FP8 group quant for DeepSeek-V4"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`; technical summary: Covers "[ROCm][Perf] Fuse SWA q/kv RMSNorm and q FP8 group quant for DeepSeek-V4"; the main implementation surface is `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/amd/rocm.py` modified +96/-0 (96 lines); hunks: -1,6 +1,7; -60,6 +61,36 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torc...; symbols: _build_indptr_from_lengths, apply_pre_quantized_block_scaled_mm, _run_parallel_input_projections, _wq_b_uses_aiter_block_scaled, touching `_build_indptr_from_lengths, apply_pre_quantized_block_scaled_mm, _run_parallel_input_projections`; `vllm/models/deepseek_v4/attention.py` modified +67/-11 (78 lines); hunks: -373,19 +373,13 @@ def forward(; -397,12 +391,32 @@ def forward(; symbols: forward, _split_qkv_and_norm, _prepare_and_attn_eager, touching `forward, _split_qkv_and_norm, _prepare_and_attn_eager`.
- Code diff details:
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +96/-0 (96 lines); hunks: -1,6 +1,7; -60,6 +61,36 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torc...; symbols: _build_indptr_from_lengths, apply_pre_quantized_block_scaled_mm, _run_parallel_input_projections, _wq_b_uses_aiter_block_scaled
  - `vllm/models/deepseek_v4/attention.py` modified +67/-11 (78 lines); hunks: -373,19 +373,13 @@ def forward(; -397,12 +391,32 @@ def forward(; symbols: forward, _split_qkv_and_norm, _prepare_and_attn_eager
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -1,6 +1,7 @@
+import functools
@@ -60,6 +61,36 @@ def _build_indptr_from_lengths(lengths: torch.Tensor) -> torch.Tensor:
+def apply_pre_quantized_block_scaled_mm(
+    linear: torch.nn.Module,
+    x_fp8: torch.Tensor,
+    x_scale: torch.Tensor,
diff -- vllm/models/deepseek_v4/attention.py
@@ -373,19 +373,13 @@ def forward(
-        qr, kv = qr_kv.split([self.q_lora_rank, self.head_dim], dim=-1)
-        qr, kv = fused_q_kv_rmsnorm(
-            qr,
-            kv,
-            self.q_norm.weight.data,
-            self.kv_norm.weight.data,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +96/-0; `vllm/models/deepseek_v4/attention.py` modified +67/-11
- Risk and verification: The diff ships test coverage in `tests/kernels/core/test_rocm_aiter_ops.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53697 - [Model] Remove unused DeepSeek V4 top-k buffer helper

- Link: https://github.com/vllm-project/vllm/pull/53697
- Status/date: merged / 2026-08-26
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/attention.py`; associated commits `0a5ad6f0d42c`
- Diff scope read: GitHub Pull Request files API returned 1 files, +0/-7, 14 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model] Remove unused DeepSeek V4 top-k buffer helper"; model line: DeepSeek V4; category: model implementation change; main diff: `vllm/models/deepseek_v4/attention.py`; technical summary: Covers "[Model] Remove unused DeepSeek V4 top-k buffer helper"; the main implementation surface is `vllm/models/deepseek_v4/attention.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/attention.py` modified +0/-7 (7 lines); hunks: -685,13 +685,6 @@ def _fused_qnorm_rope_kv_insert(; symbols: _fused_qnorm_rope_kv_insert, _global_topk_output_buffers, bind_kv_cache, touching `_fused_qnorm_rope_kv_insert, _global_topk_output_buffers, bind_kv_cache`.
- Code diff details:
  - `vllm/models/deepseek_v4/attention.py` modified +0/-7 (7 lines); hunks: -685,13 +685,6 @@ def _fused_qnorm_rope_kv_insert(; symbols: _fused_qnorm_rope_kv_insert, _global_topk_output_buffers, bind_kv_cache
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/attention.py
@@ -685,13 +685,6 @@ def _fused_qnorm_rope_kv_insert(
-    def _global_topk_output_buffers(
-        self, topk_indices: torch.Tensor
-    ) -> tuple[torch.Tensor, torch.Tensor] | None:
-        if self.compress_ratio != 4 or self.eager_scratch_pool is None:
-            return None
-        return self.eager_scratch_pool.global_topk_outputs(topk_indices)
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/attention.py` modified +0/-7
- Risk and verification: Runtime changes concentrate in `vllm/models/deepseek_v4/attention.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #53838 - [ROCm][DSV4][Perf] Fuse DeepSeek V4 C4 compressor GEMMs

- Link: https://github.com/vllm-project/vllm/pull/53838
- Status/date: merged / 2026-08-26
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`; associated commits `657f9b9ce241`
- Diff scope read: GitHub Pull Request files API returned 3 files, +221/-0, 269 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[ROCm][DSV4][Perf] Fuse DeepSeek V4 C4 compressor GEMMs"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`; technical summary: Covers "[ROCm][DSV4][Perf] Fuse DeepSeek V4 C4 compressor GEMMs"; the main implementation surface is `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/amd/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py` added +141/-0 (141 lines); hunks: -0,0 +1,141; symbols: _WeightOnlyLinear, __init__, _Compressor, _IndexerWeightsProjection, touching `_WeightOnlyLinear, __init__, _Compressor`; `vllm/models/deepseek_v4/amd/rocm.py` modified +73/-0 (73 lines); hunks: -11,6 +11,7; -36,6 +37,8; symbols: _trust_dsv4_extra_cache_nan_free, __init__, get_padded_num_q_heads, _prep, touching `_trust_dsv4_extra_cache_nan_free, __init__, get_padded_num_q_heads`; `vllm/models/deepseek_v4/amd/model.py` modified +7/-0 (7 lines); hunks: -1044,11 +1044,18 @@ def load_weights(self, weights: Iterable[tuple[str, torc...; symbols: load_weights, process_weights_after_loading, get_expert_mapping, touching `load_weights, process_weights_after_loading, get_expert_mapping`.
- Code diff details:
  - `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py` added +141/-0 (141 lines); hunks: -0,0 +1,141; symbols: _WeightOnlyLinear, __init__, _Compressor, _IndexerWeightsProjection
  - `vllm/models/deepseek_v4/amd/rocm.py` modified +73/-0 (73 lines); hunks: -11,6 +11,7; -36,6 +37,8; symbols: _trust_dsv4_extra_cache_nan_free, __init__, get_padded_num_q_heads, _prep
  - `vllm/models/deepseek_v4/amd/model.py` modified +7/-0 (7 lines); hunks: -1044,11 +1044,18 @@ def load_weights(self, weights: Iterable[tuple[str, torc...; symbols: load_weights, process_weights_after_loading, get_expert_mapping
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py
@@ -0,0 +1,141 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+import torch
+import vllm.model_executor.offloader as offloader
+from vllm.models.deepseek_v4.amd.rocm import (
+    DeepseekV4ROCMAiterMLAAttention,
diff -- vllm/models/deepseek_v4/amd/rocm.py
@@ -11,6 +11,7 @@
+from vllm.logger import init_logger
@@ -36,6 +37,8 @@
+logger = init_logger(__name__)
@@ -486,6 +489,9 @@ def __init__(self, *args, **kwargs):
+        self._fused_compressor_weight: torch.Tensor | None
+        self.register_buffer("_fused_compressor_weight", None, persistent=False)
diff -- vllm/models/deepseek_v4/amd/model.py
@@ -1044,11 +1044,18 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py` added +141/-0
  - runtime: `vllm/models/deepseek_v4/amd/rocm.py` modified +73/-0; `vllm/models/deepseek_v4/amd/model.py` modified +7/-0
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53747 - [Bugfix][Tokenizer] Replace bare asserts in the DeepSeek V4 encoder

- Link: https://github.com/vllm-project/vllm/pull/53747
- Status/date: merged / 2026-08-25
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py`; associated commits `19406fae2873`
- Diff scope read: GitHub Pull Request files API returned 2 files, +41/-8, 81 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][Tokenizer] Replace bare asserts in the DeepSeek V4 encoder"; model line: DeepSeek V4; category: bug fix; main diff: `vllm/tokenizers/deepseek_v4_encoding.py`, `tests/tokenizers_/test_deepseek_v4.py`; technical summary: Covers "[Bugfix][Tokenizer] Replace bare asserts in the DeepSeek V4 encoder"; the main implementation surface is `vllm/tokenizers/deepseek_v4_encoding.py`, `tests/tokenizers_/test_deepseek_v4.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/tokenizers/deepseek_v4_encoding.py` modified +17/-8 (25 lines); hunks: -225,8 +225,12 @@ def render_message(; -248,10 +252,11 @@ def render_message(; symbols: render_message, touching `render_message`; `tests/tokenizers_/test_deepseek_v4.py` modified +24/-0 (24 lines); hunks: -403,3 +403,27 @@ def test_deepseek_v4_matches_reference_golden_fixtures(case...; symbols: test_deepseek_v4_matches_reference_golden_fixtures, test_deepseek_v4_rejects_empty_developer_content, test_deepseek_v4_encode_messages_rejects_invalid_arguments, touching `test_deepseek_v4_matches_reference_golden_fixtures, test_deepseek_v4_rejects_empty_developer_content, test_deepseek_v4_encode_messages_rejects_invalid_arguments`.
- Code diff details:
  - `vllm/tokenizers/deepseek_v4_encoding.py` modified +17/-8 (25 lines); hunks: -225,8 +225,12 @@ def render_message(; -248,10 +252,11 @@ def render_message(; symbols: render_message
  - `tests/tokenizers_/test_deepseek_v4.py` modified +24/-0 (24 lines); hunks: -403,3 +403,27 @@ def test_deepseek_v4_matches_reference_golden_fixtures(case...; symbols: test_deepseek_v4_matches_reference_golden_fixtures, test_deepseek_v4_rejects_empty_developer_content, test_deepseek_v4_encode_messages_rejects_invalid_arguments
- Key code excerpts:

```diff
diff -- vllm/tokenizers/deepseek_v4_encoding.py
@@ -225,8 +225,12 @@ def render_message(
-    assert 0 <= index < len(messages)
-    assert thinking_mode in ["chat", "thinking"], f"Invalid thinking_mode `{thinking_mode}`"
+    if not (0 <= index < len(messages)):
+        raise ValueError(
+            f"Index {index} out of range for messages list of length {len(messages)}"
+        )
diff -- tests/tokenizers_/test_deepseek_v4.py
@@ -403,3 +403,27 @@ def test_deepseek_v4_matches_reference_golden_fixtures(case_id, kwargs):
+def test_deepseek_v4_rejects_empty_developer_content():
+    with pytest.raises(ValueError):
+        _tokenizer().apply_chat_template(
+            [{"role": "developer", "content": ""}],
+            tokenize=False,
+            enable_thinking=True,
```

- Reviewed files:
  - runtime: `vllm/tokenizers/deepseek_v4_encoding.py` modified +17/-8
  - tests: `tests/tokenizers_/test_deepseek_v4.py` modified +24/-0
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/test_deepseek_v4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #51262 - [Bugfix][DeepSeek V4] Handle trailing system messages in prompt rendering

- Link: https://github.com/vllm-project/vllm/pull/51262
- Status/date: merged / 2026-08-25
- Trace source: `git log --name-only -- <model-files>` found it through `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py`; associated commits `59d7fc92ea03`
- Diff scope read: GitHub Pull Request files API returned 4 files, +150/-3, 188 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Bugfix][DeepSeek V4] Handle trailing system messages in prompt rendering"; model line: DeepSeek V4; category: bug fix; main diff: `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py`; technical summary: Covers "[Bugfix][DeepSeek V4] Handle trailing system messages in prompt rendering"; the main implementation surface is `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/tokenizers_/test_deepseek_v4.py` modified +77/-0 (77 lines); hunks: -113,6 +113,83 @@ def test_deepseek_v4_explicitly_disables_thinking(kwargs):; symbols: test_deepseek_v4_explicitly_disables_thinking, test_deepseek_v4_appends_assistant_transition_after_trailing_system, test_deepseek_v4_does_not_transition_after_mid_conversation_system, test_deepseek_v4_transitions_from_system_to_assistant, touching `test_deepseek_v4_explicitly_disables_thinking, test_deepseek_v4_appends_assistant_transition_after_trailing_system, test_deepseek_v4_does_not_transition_after_mid_conversation_system`; `vllm/tokenizers/deepseek_v4_encoding.py` modified +9/-1 (10 lines); hunks: -374,7 +374,15 @@ def render_message(; symbols: render_message, touching `render_message`.
- Code diff details:
  - `tests/tokenizers_/test_deepseek_v4.py` modified +77/-0 (77 lines); hunks: -113,6 +113,83 @@ def test_deepseek_v4_explicitly_disables_thinking(kwargs):; symbols: test_deepseek_v4_explicitly_disables_thinking, test_deepseek_v4_appends_assistant_transition_after_trailing_system, test_deepseek_v4_does_not_transition_after_mid_conversation_system, test_deepseek_v4_transitions_from_system_to_assistant
  - `vllm/tokenizers/deepseek_v4_encoding.py` modified +9/-1 (10 lines); hunks: -374,7 +374,15 @@ def render_message(; symbols: render_message
- Key code excerpts:

```diff
diff -- tests/tokenizers_/test_deepseek_v4.py
@@ -113,6 +113,83 @@ def test_deepseek_v4_explicitly_disables_thinking(kwargs):
+@pytest.mark.parametrize(
+    ("enable_thinking", "thinking_token"),
+    [(False, "</think>"), (True, "<think>")],
+)
+def test_deepseek_v4_appends_assistant_transition_after_trailing_system(
+    enable_thinking, thinking_token
diff -- vllm/tokenizers/deepseek_v4_encoding.py
@@ -374,7 +374,15 @@ def render_message(
-    elif messages[index].get("role") in ["user", "developer"]:
+    # A trailing system message opens generation, while a system message
+    # followed by assistant opens that assistant history turn.
+    elif role in ["user", "developer"] or (
+        role == "system"
+        and (
```

- Reviewed files:
  - tests: `tests/tokenizers_/test_deepseek_v4.py` modified +77/-0
  - runtime: `vllm/tokenizers/deepseek_v4_encoding.py` modified +9/-1
- Risk and verification: The diff ships test coverage in `tests/tokenizers_/test_deepseek_v4.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #49636 - [Model][MoE] DeepSeek-V4: add opt-in FlashInfer moe_ep expert backend

- Link: https://github.com/vllm-project/vllm/pull/49636
- Status/date: merged / 2026-08-25
- Trace source: `git log --name-only -- <model-files>` found it through `tests/models/test_deepseek_v4_fi_moe_ep.py`, `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `8fe9317f2e40`
- Diff scope read: GitHub Pull Request files API returned 5 files, +1083/-12, 1195 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[Model][MoE] DeepSeek-V4: add opt-in FlashInfer moe_ep expert backend"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `tests/models/test_deepseek_v4_fi_moe_ep.py`, `vllm/models/deepseek_v4/nvidia/model.py`; technical summary: Covers "[Model][MoE] DeepSeek-V4: add opt-in FlashInfer moe_ep expert backend"; the main implementation surface is `tests/models/test_deepseek_v4_fi_moe_ep.py`, `vllm/models/deepseek_v4/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `tests/models/test_deepseek_v4_fi_moe_ep.py` added +259/-0 (259 lines); hunks: -0,0 +1,259; symbols: _FakeBootstrapConfig, _FakeDeepGemmMegaMoeConfig, _FakeNvfp4CutedslMegaMoeConfig, _FakeMegaConfig, touching `_FakeBootstrapConfig, _FakeDeepGemmMegaMoeConfig, _FakeNvfp4CutedslMegaMoeConfig`; `vllm/models/deepseek_v4/nvidia/model.py` modified +32/-11 (43 lines); hunks: -11,6 +11,7; -83,6 +84,10; symbols: __init__, _init_mega_moe_experts, _init_fused_moe_experts, touching `__init__, _init_mega_moe_experts, _init_fused_moe_experts`.
- Code diff details:
  - `tests/models/test_deepseek_v4_fi_moe_ep.py` added +259/-0 (259 lines); hunks: -0,0 +1,259; symbols: _FakeBootstrapConfig, _FakeDeepGemmMegaMoeConfig, _FakeNvfp4CutedslMegaMoeConfig, _FakeMegaConfig
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +32/-11 (43 lines); hunks: -11,6 +11,7; -83,6 +84,10; symbols: __init__, _init_mega_moe_experts, _init_fused_moe_experts
- Key code excerpts:

```diff
diff -- tests/models/test_deepseek_v4_fi_moe_ep.py
@@ -0,0 +1,259 @@
+# SPDX-License-Identifier: Apache-2.0
+# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
+"""Unit tests for the flashinfer moe_ep backend plumbing.
+Everything here runs without a GPU or a flashinfer install: the flashinfer
+modules the helpers import lazily are replaced with capture fakes.
+"""
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -11,6 +11,7 @@
+from vllm.config.kernel import MEGA_MOE_BACKENDS
@@ -83,6 +84,10 @@
+from vllm.utils.flashinfer_moe_ep import (
+    is_fi_moe_ep_backend,
+    validate_fi_moe_ep_config,
+)
```

- Reviewed files:
  - tests: `tests/models/test_deepseek_v4_fi_moe_ep.py` added +259/-0
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +32/-11
- Risk and verification: The diff ships test coverage in `tests/models/test_deepseek_v4_fi_moe_ep.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

### PR #53361 - [LoRA] feat: Support LoRA for DeepSeek V4

- Link: https://github.com/vllm-project/vllm/pull/53361
- Status/date: merged / 2026-08-24
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/nvidia/model.py`; associated commits `702e1d718646`
- Diff scope read: GitHub Pull Request files API returned 3 files, +70/-5, 166 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[LoRA] feat: Support LoRA for DeepSeek V4"; model line: DeepSeek V4; category: model support/runtime entry; main diff: `vllm/models/deepseek_v4/nvidia/model.py`; technical summary: Covers "[LoRA] feat: Support LoRA for DeepSeek V4"; the main implementation surface is `vllm/models/deepseek_v4/nvidia/model.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/nvidia/model.py` modified +35/-1 (36 lines); hunks: -55,6 +55,7; -1468,6 +1469,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, _make_deepseek_v4_weights_mapper, update_physical_experts_metadata, touching `load_weights, _make_deepseek_v4_weights_mapper, update_physical_experts_metadata`.
- Code diff details:
  - `vllm/models/deepseek_v4/nvidia/model.py` modified +35/-1 (36 lines); hunks: -55,6 +55,7; -1468,6 +1469,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch...; symbols: load_weights, _make_deepseek_v4_weights_mapper, update_physical_experts_metadata
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/nvidia/model.py
@@ -55,6 +55,7 @@
+    SupportsLoRA,
@@ -1468,6 +1469,11 @@ def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
+                if name not in params_dict:
+                    head, _, leaf = name.rpartition(".")
+                    suffixed = f"{head}.base_layer.{leaf}"
+                    if suffixed in params_dict:
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/nvidia/model.py` modified +35/-1
- Risk and verification: Runtime changes concentrate in `vllm/lora/layers/base.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/models/deepseek_v4/nvidia/model.py`; regression risk is weight loading, parallel sharding, attention/MoE backend selection, and parser output.

### PR #52823 - [DSv4 Perf] Adaptive topk width for dsv4, making #50004 back

- Link: https://github.com/vllm-project/vllm/pull/52823
- Status/date: merged / 2026-08-21
- Trace source: `git log --name-only -- <model-files>` found it through `vllm/models/deepseek_v4/sparse_mla.py`; associated commits `e6f35d3c69b2`
- Diff scope read: GitHub Pull Request files API returned 2 files, +78/-3, 111 readable patch lines; this card prioritizes model-related and high-change files.
- Motivation: Title: "[DSv4 Perf] Adaptive topk width for dsv4, making #50004 back"; model line: DeepSeek V4; category: performance/backend optimization; main diff: `vllm/models/deepseek_v4/sparse_mla.py`; technical summary: Covers "[DSv4 Perf] Adaptive topk width for dsv4, making #50004 back"; the main implementation surface is `vllm/models/deepseek_v4/sparse_mla.py`. File-level evidence, code excerpts, and validation risks are preserved below.
- Key implementation: `vllm/models/deepseek_v4/sparse_mla.py` modified +21/-3 (24 lines); hunks: -257,6 +257,15 @@ def _build_c128a_metadata(; -269,7 +278,7 @@ def _build_c128a_metadata(; symbols: _build_c128a_metadata, build_c128a_topk_metadata, touching `_build_c128a_metadata, build_c128a_topk_metadata`.
- Code diff details:
  - `vllm/models/deepseek_v4/sparse_mla.py` modified +21/-3 (24 lines); hunks: -257,6 +257,15 @@ def _build_c128a_metadata(; -269,7 +278,7 @@ def _build_c128a_metadata(; symbols: _build_c128a_metadata, build_c128a_topk_metadata
- Key code excerpts:

```diff
diff -- vllm/models/deepseek_v4/sparse_mla.py
@@ -257,6 +257,15 @@ def _build_c128a_metadata(
+        active_topk_width = min(
+            max(
+                triton.next_power_of_2(max(cm.max_seq_len // self.compress_ratio, 1)),
+                _C128A_TOPK_ALIGNMENT,
+            ),
+            self.c128a_max_compressed,
```

- Reviewed files:
  - runtime: `vllm/models/deepseek_v4/sparse_mla.py` modified +21/-3
- Risk and verification: The diff ships test coverage in `tests/kernels/attention/test_flashmla_sparse.py`; future changes in this area should rerun those tests plus a minimal launch or accuracy smoke.

## Gap-Closure Notes

- Acceptance rule: every PR card must keep trace source, diff scope, implementation notes, code excerpts, reviewed files, and verification risk.
- If new model files fall outside the current filters, add the file filter first and rerun the same `git log --name-only -- <model-files>` trace.
